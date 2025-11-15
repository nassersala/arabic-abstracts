# Section 3: Fully convolutional networks
## القسم 3: الشبكات الالتفافية الكاملة

**Section:** fully-convolutional-networks
**Translation Quality:** 0.86
**Glossary Terms Used:** convolutional networks, layer, convolution, pooling, activation function, kernel, stride, fully convolutional network, dense prediction, receptive field, gradient descent, backpropagation, upsampling, deconvolution, patchwise training

---

### English Version

Each layer of data in a convnet is a three-dimensional array of size h × w × d, where h and w are spatial dimensions, and d is the feature or channel dimension. The first layer is the image, with pixel size h × w, and d color channels. Locations in higher layers correspond to the locations in the image they are path-connected to, which are called their receptive fields.

Convnets are built on translation invariance. Their basic components (convolution, pooling, and activation functions) operate on local input regions, and depend only on relative spatial coordinates. Writing xᵢⱼ for the data vector at location (i, j) in a particular layer, and yᵢⱼ for the following layer, these functions compute outputs yᵢⱼ by

$$y_{ij} = f_{ks}(\{x_{si+\delta i,sj+\delta j}\}_{0\leq\delta i,\delta j\leq k})$$

where k is called the kernel size, s is the stride or subsampling factor, and fₖₛ determines the layer type: a matrix multiplication for convolution or average pooling, a spatial max for max pooling, or an elementwise nonlinearity for an activation function, and so on for other types of layers.

This functional form is maintained under composition, with kernel size and stride obeying the transformation rule

$$f_{ks} \circ g_{k's'} = (f \circ g)_{k'+(k-1)s',ss'}$$

While a general deep net computes a general nonlinear function, a net with only layers of this form computes a nonlinear filter, which we call a deep filter or fully convolutional network. An FCN naturally operates on an input of any size, and produces an output of corresponding (possibly resampled) spatial dimensions.

A real-valued loss function composed with an FCN defines a task. If the loss function is a sum over the spatial dimensions of the final layer, $\ell(x; \theta) = \sum_{ij} \ell'(x_{ij}; \theta)$, its gradient will be a sum over the gradients of each of its spatial components. Thus stochastic gradient descent on ℓ computed on whole images will be the same as stochastic gradient descent on ℓ', taking all of the final layer receptive fields as a minibatch.

When these receptive fields overlap significantly, both feedforward computation and backpropagation are much more efficient when computed layer-by-layer over an entire image instead of independently patch-by-patch.

We next explain how to convert classification nets into fully convolutional nets that produce coarse output maps. For pixelwise prediction, we need to connect these coarse outputs back to the pixels. Section 3.2 describes a trick that OverFeat [29] introduced for this purpose. We gain insight into this trick by reinterpreting it as an equivalent network modification. As an efficient, effective alternative, we introduce deconvolution layers for upsampling in Section 3.3. In Section 3.4 we consider training by patchwise sampling, and give evidence in Section 4.3 that our whole image training is faster and equally effective.

**3.1. Adapting classifiers for dense prediction**

Typical recognition nets, including LeNet [21], AlexNet [19], and its deeper successors [31, 32], ostensibly take fixed-sized inputs and produce nonspatial outputs. The fully connected layers of these nets have fixed dimensions and throw away spatial coordinates. However, these fully connected layers can also be viewed as convolutions with kernels that cover their entire input regions. Doing so casts them into fully convolutional networks that take input of any size and output classification maps. This transformation is illustrated in Figure 2. (By contrast, nonconvolutional nets, such as the one by Le et al. [20], lack this capability.)

Furthermore, while the resulting maps are equivalent to the evaluation of the original net on particular input patches, the computation is highly amortized over the overlapping regions of those patches. For example, while AlexNet takes 1.2 ms (on a typical GPU) to produce the classification scores of a 227 × 227 image, the fully convolutional version takes 22 ms to produce a 10 × 10 grid of outputs from a 500 × 500 image, which is more than 5 times faster than the naïve approach¹.

The spatial output maps of these convolutionalized models make them a natural choice for dense problems like semantic segmentation. With ground truth available at every output cell, both the forward and backward passes are straightforward, and both take advantage of the inherent computational efficiency (and aggressive optimization) of convolution.

The corresponding backward times for the AlexNet example are 2.4 ms for a single image and 37 ms for a fully convolutional 10 × 10 output map, resulting in a speedup similar to that of the forward pass. This dense backpropagation is illustrated in Figure 1.

While our reinterpretation of classification nets as fully convolutional yields output maps for inputs of any size, the output dimensions are typically reduced by subsampling. The classification nets subsample to keep filters small and computational requirements reasonable. This coarsens the output of a fully convolutional version of these nets, reducing it from the size of the input by a factor equal to the pixel stride of the receptive fields of the output units.

**3.2. Shift-and-stitch is filter rarefaction**

Input shifting and output interlacing is a trick that yields dense predictions from coarse outputs without interpolation, introduced by OverFeat [29]. If the outputs are downsampled by a factor of f, the input is shifted (by left and top padding) x pixels to the right and y pixels down, once for every value of (x, y) ∈ {0, . . . , f − 1} × {0, . . . , f − 1}. These f² inputs are each run through the convnet, and the outputs are interlaced so that the predictions correspond to the pixels at the centers of their receptive fields.

Changing only the filters and layer strides of a convnet can produce the same output as this shift-and-stitch trick. Consider a layer (convolution or pooling) with input stride s, and a following convolution layer with filter weights fᵢⱼ (eliding the feature dimensions, irrelevant here). Setting the lower layer's input stride to 1 upsamples its output by a factor of s, just like shift-and-stitch. However, convolving the original filter with the upsampled output does not produce the same result as the trick, because the original filter only sees a reduced portion of its (now upsampled) input. To reproduce the trick, rarefy the filter by enlarging it as

$$f'_{ij} = \begin{cases} f_{i/s,j/s} & \text{if } s \text{ divides both } i \text{ and } j; \\ 0 & \text{otherwise,} \end{cases}$$

(with i and j zero-based). Reproducing the full net output of the trick involves repeating this filter enlargement layer-by-layer until all subsampling is removed.

Simply decreasing subsampling within a net is a tradeoff: the filters see finer information, but have smaller receptive fields and take longer to compute. We have seen that the shift-and-stitch trick is another kind of tradeoff: the output is made denser without decreasing the receptive field sizes of the filters, but the filters are prohibited from accessing information at a finer scale than their original design.

Although we have done preliminary experiments with shift-and-stitch, we do not use it in our model. We find learning through upsampling, as described in the next section, to be more effective and efficient, especially when combined with the skip layer fusion described later on.

**3.3. Upsampling is backwards strided convolution**

Another way to connect coarse outputs to dense pixels is interpolation. For instance, simple bilinear interpolation computes each output yᵢⱼ from the nearest four inputs by a linear map that depends only on the relative positions of the input and output cells.

In a sense, upsampling with factor f is convolution with a fractional input stride of 1/f. So long as f is integral, a natural way to upsample is therefore backwards convolution (sometimes called deconvolution) with an output stride of f. Such an operation is trivial to implement, since it simply reverses the forward and backward passes of convolution. Thus upsampling is performed in-network for end-to-end learning by backpropagation from the pixelwise loss.

Note that the deconvolution filter in such a layer need not be fixed (e.g., to bilinear upsampling), but can be learned. A stack of deconvolution layers and activation functions can even learn a nonlinear upsampling.

In our experiments, we find that in-network upsampling is fast and effective for learning dense prediction. Our best segmentation architecture uses these layers to learn to upsample for refined prediction in Section 4.2.

**3.4. Patchwise training is loss sampling**

In stochastic optimization, gradient computation is driven by the training distribution. Both patchwise training and fully-convolutional training can be made to produce any distribution, although their relative computational efficiency depends on overlap and minibatch size. Whole image fully convolutional training is identical to patchwise training where each batch consists of all the receptive fields of the units below the loss for an image (or collection of images). While this is more efficient than uniform sampling of patches, it reduces the number of possible batches. However, random selection of patches within an image may be recovered simply. Restricting the loss to a randomly sampled subset of its spatial terms (or, equivalently applying a DropConnect mask [36] between the output and the loss) excludes patches from the gradient computation.

If the kept patches still have significant overlap, fully convolutional computation will still speed up training. If gradients are accumulated over multiple backward passes, batches can include patches from several images².

Sampling in patchwise training can correct class imbalance [27, 8, 2] and mitigate the spatial correlation of dense patches [28, 16]. In fully convolutional training, class balance can also be achieved by weighting the loss, and loss sampling can be used to address spatial correlation.

We explore training with sampling in Section 4.3, and do not find that it yields faster or better convergence for dense prediction. Whole image training is effective and efficient.

---

¹ Assuming efficient batching of single image inputs. The classification scores for a single image by itself take 5.4 ms to produce, which is nearly 25 times slower than the fully convolutional version.

² Note that not every possible patch is included this way, since the receptive fields of the final layer units lie on a fixed, strided grid. However, by shifting the image left and down by a random value up to the stride, random selection from all possible patches may be recovered.

---

### النسخة العربية

كل طبقة من البيانات في الشبكة الالتفافية هي مصفوفة ثلاثية الأبعاد بحجم h × w × d، حيث h وw هما الأبعاد المكانية، وd هو بُعد الميزة أو القناة. الطبقة الأولى هي الصورة، بحجم بكسل h × w، وd من قنوات الألوان. تتوافق المواقع في الطبقات العليا مع المواقع في الصورة التي ترتبط بها عبر المسار، والتي تسمى حقولها الاستقبالية.

تُبنى الشبكات الالتفافية على ثبات الترجمة. مكوناتها الأساسية (الالتفاف، والتجميع، ودوال التنشيط) تعمل على مناطق إدخال موضعية، وتعتمد فقط على الإحداثيات المكانية النسبية. بكتابة xᵢⱼ لمتجه البيانات عند الموقع (i, j) في طبقة معينة، وyᵢⱼ للطبقة التالية، تحسب هذه الدوال المخرجات yᵢⱼ بواسطة

$$y_{ij} = f_{ks}(\{x_{si+\delta i,sj+\delta j}\}_{0\leq\delta i,\delta j\leq k})$$

حيث k يُسمى حجم النواة، وs هو الخطوة أو عامل العينات الفرعية، وfₖₛ يحدد نوع الطبقة: ضرب مصفوفة للالتفاف أو التجميع المتوسط، أو حد أقصى مكاني لتجميع الحد الأقصى، أو لاخطية عنصرية لدالة التنشيط، وهكذا لأنواع الطبقات الأخرى.

يتم الحفاظ على هذا الشكل الوظيفي تحت التركيب، مع حجم النواة والخطوة التي تطيع قاعدة التحويل

$$f_{ks} \circ g_{k's'} = (f \circ g)_{k'+(k-1)s',ss'}$$

بينما تحسب الشبكة العميقة العامة دالة لاخطية عامة، فإن الشبكة التي تحتوي فقط على طبقات من هذا الشكل تحسب مرشحاً لاخطياً، والذي نسميه مرشحاً عميقاً أو شبكة التفافية كاملة. تعمل شبكة FCN بشكل طبيعي على مدخلات من أي حجم، وتنتج مخرجات ذات أبعاد مكانية مطابقة (وربما معاد أخذ عيناتها).

دالة الخسارة ذات القيمة الحقيقية المركبة مع شبكة FCN تحدد مهمة. إذا كانت دالة الخسارة هي مجموع على الأبعاد المكانية للطبقة النهائية، $\ell(x; \theta) = \sum_{ij} \ell'(x_{ij}; \theta)$، فإن تدرجها سيكون مجموع تدرجات كل من مكوناتها المكانية. وبالتالي فإن الانحدار التدرجي العشوائي على ℓ المحسوب على الصور الكاملة سيكون نفسه الانحدار التدرجي العشوائي على ℓ'، مع أخذ جميع الحقول الاستقبالية للطبقة النهائية كحزمة صغيرة.

عندما تتداخل هذه الحقول الاستقبالية بشكل كبير، فإن كلاً من الحساب الأمامي والانتشار العكسي يكونان أكثر كفاءة عند حسابهما طبقة تلو الأخرى على الصورة بأكملها بدلاً من رقعة تلو الأخرى بشكل مستقل.

نشرح بعد ذلك كيفية تحويل شبكات التصنيف إلى شبكات التفافية كاملة تنتج خرائط مخرجات خشنة. للتنبؤ على مستوى البكسل، نحتاج إلى ربط هذه المخرجات الخشنة مرة أخرى بالبكسلات. يصف القسم 3.2 حيلة قدمتها OverFeat [29] لهذا الغرض. نكتسب رؤية لهذه الحيلة من خلال إعادة تفسيرها كتعديل شبكة مكافئ. كبديل فعال وكفء، نقدم طبقات فك الالتفاف للرفع في القسم 3.3. في القسم 3.4 نعتبر التدريب بأخذ عينات الرقع، ونقدم دليلاً في القسم 4.3 على أن تدريبنا بالصورة الكاملة أسرع ومتساوي الفعالية.

**3.1. تكييف المصنفات للتنبؤ الكثيف**

شبكات التعرف النموذجية، بما في ذلك LeNet [21]، وAlexNet [19]، وخلفائها الأعمق [31، 32]، تأخذ ظاهرياً مدخلات ذات حجم ثابت وتنتج مخرجات غير مكانية. الطبقات المتصلة بالكامل لهذه الشبكات لها أبعاد ثابتة وتتخلص من الإحداثيات المكانية. ومع ذلك، يمكن أيضاً النظر إلى هذه الطبقات المتصلة بالكامل على أنها التفافات بنوى تغطي مناطق إدخالها بالكامل. يؤدي القيام بذلك إلى تحويلها إلى شبكات التفافية كاملة تأخذ مدخلات من أي حجم وتخرج خرائط تصنيف. يتم توضيح هذا التحويل في الشكل 2. (على النقيض من ذلك، تفتقر الشبكات غير الالتفافية، مثل تلك التي قدمها Le وآخرون [20]، إلى هذه القدرة.)

علاوة على ذلك، في حين أن الخرائط الناتجة تعادل تقييم الشبكة الأصلية على رقع إدخال معينة، فإن الحساب يتم توزيعه بشكل كبير على المناطق المتداخلة من تلك الرقع. على سبيل المثال، بينما تستغرق AlexNet 1.2 ميلي ثانية (على وحدة معالجة الرسومات النموذجية) لإنتاج درجات التصنيف لصورة 227 × 227، فإن النسخة الالتفافية الكاملة تستغرق 22 ميلي ثانية لإنتاج شبكة 10 × 10 من المخرجات من صورة 500 × 500، وهو أسرع بأكثر من 5 مرات من النهج الساذج¹.

تجعل خرائط المخرجات المكانية لهذه النماذج الالتفافية المحولة خياراً طبيعياً للمشاكل الكثيفة مثل التجزئة الدلالية. مع توفر الحقيقة الأرضية في كل خلية إخراج، فإن كلاً من الممرات الأمامية والعكسية واضحة ومباشرة، وكلاهما يستفيد من الكفاءة الحسابية الكامنة (والتحسين القوي) للالتفاف.

أوقات العودة المقابلة لمثال AlexNet هي 2.4 ميلي ثانية لصورة واحدة و37 ميلي ثانية لخريطة مخرجات التفافية كاملة 10 × 10، مما ينتج عنه تسريع مماثل لتسريع الممر الأمامي. يتم توضيح هذا الانتشار العكسي الكثيف في الشكل 1.

بينما تنتج إعادة تفسيرنا لشبكات التصنيف على أنها التفافية كاملة خرائط مخرجات لمدخلات من أي حجم، عادةً ما يتم تقليل أبعاد المخرجات بواسطة أخذ العينات الفرعية. تأخذ شبكات التصنيف عينات فرعية للحفاظ على المرشحات صغيرة ومتطلبات الحساب معقولة. هذا يجعل مخرجات النسخة الالتفافية الكاملة من هذه الشبكات أكثر خشونة، مما يقللها من حجم المدخلات بعامل يساوي خطوة البكسل للحقول الاستقبالية لوحدات المخرجات.

**3.2. التحويل والتشابك هو ترقيق المرشح**

تحويل الإدخال وتشابك المخرجات هو حيلة تنتج تنبؤات كثيفة من مخرجات خشنة دون استيفاء، قدمتها OverFeat [29]. إذا تم أخذ عينات فرعية من المخرجات بعامل f، يتم تحويل الإدخال (بواسطة الحشو الأيسر والعلوي) x بكسلات إلى اليمين وy بكسلات لأسفل، مرة واحدة لكل قيمة من (x, y) ∈ {0, . . . , f − 1} × {0, . . . , f − 1}. يتم تشغيل كل من هذه المدخلات f² من خلال الشبكة الالتفافية، ويتم تشابك المخرجات بحيث تتوافق التنبؤات مع البكسلات في مراكز حقولها الاستقبالية.

يمكن أن ينتج تغيير المرشحات وخطوات الطبقة فقط في الشبكة الالتفافية نفس المخرجات مثل حيلة التحويل والتشابك هذه. ضع في اعتبارك طبقة (التفاف أو تجميع) مع خطوة إدخال s، وطبقة التفاف تالية مع أوزان مرشح fᵢⱼ (إغفال أبعاد الميزة، غير ذات صلة هنا). يؤدي تعيين خطوة إدخال الطبقة السفلى إلى 1 إلى رفع مخرجاتها بعامل s، تماماً مثل التحويل والتشابك. ومع ذلك، فإن التفاف المرشح الأصلي مع المخرجات المرفوعة لا ينتج نفس النتيجة مثل الحيلة، لأن المرشح الأصلي يرى فقط جزءاً مخفضاً من إدخاله (المرفوع الآن). لإعادة إنتاج الحيلة، قم بترقيق المرشح عن طريق تكبيره كـ

$$f'_{ij} = \begin{cases} f_{i/s,j/s} & \text{إذا كان } s \text{ يقسم كلاً من } i \text{ و } j; \\ 0 & \text{خلاف ذلك,} \end{cases}$$

(مع i وj على أساس الصفر). يتضمن إعادة إنتاج مخرجات الشبكة الكاملة للحيلة تكرار تكبير المرشح هذا طبقة تلو الأخرى حتى تتم إزالة جميع العينات الفرعية.

إن تقليل أخذ العينات الفرعية ببساطة داخل الشبكة هو مقايضة: ترى المرشحات معلومات أدق، ولكن لديها حقول استقبالية أصغر وتستغرق وقتاً أطول للحساب. لقد رأينا أن حيلة التحويل والتشابك هي نوع آخر من المقايضة: يتم جعل المخرجات أكثر كثافة دون تقليل أحجام الحقول الاستقبالية للمرشحات، لكن يُمنع المرشحات من الوصول إلى المعلومات على مقياس أدق من تصميمها الأصلي.

على الرغم من أننا قمنا بتجارب أولية مع التحويل والتشابك، إلا أننا لا نستخدمه في نموذجنا. نجد أن التعلم من خلال الرفع، كما هو موضح في القسم التالي، أكثر فعالية وكفاءة، خاصة عند دمجه مع دمج طبقة التخطي الموصوفة لاحقاً.

**3.3. الرفع هو التفاف خلفي بخطوات**

طريقة أخرى لربط المخرجات الخشنة بالبكسلات الكثيفة هي الاستيفاء. على سبيل المثال، يحسب الاستيفاء الخطي الثنائي البسيط كل مخرج yᵢⱼ من أقرب أربعة مدخلات بواسطة خريطة خطية تعتمد فقط على المواقع النسبية لخلايا الإدخال والإخراج.

بمعنى ما، الرفع بعامل f هو التفاف مع خطوة إدخال كسرية 1/f. طالما أن f عدد صحيح، فإن الطريقة الطبيعية للرفع هي الالتفاف الخلفي (يسمى أحياناً فك الالتفاف) مع خطوة إخراج f. هذه العملية تافهة للتنفيذ، حيث إنها ببساطة تعكس الممرات الأمامية والعكسية للالتفاف. وبالتالي يتم تنفيذ الرفع داخل الشبكة للتعلم من البداية إلى النهاية عن طريق الانتشار العكسي من خسارة البكسل.

لاحظ أن مرشح فك الالتفاف في مثل هذه الطبقة لا يحتاج إلى أن يكون ثابتاً (على سبيل المثال، للرفع الخطي الثنائي)، ولكن يمكن تعلمه. يمكن حتى لكومة من طبقات فك الالتفاف ودوال التنشيط تعلم رفع لاخطي.

في تجاربنا، وجدنا أن الرفع داخل الشبكة سريع وفعال لتعلم التنبؤ الكثيف. تستخدم أفضل معمارية تجزئة لدينا هذه الطبقات لتعلم الرفع للتنبؤ المحسّن في القسم 4.2.

**3.4. التدريب القائم على الرقع هو أخذ عينات الخسارة**

في التحسين العشوائي، يكون حساب التدرج مدفوعاً بتوزيع التدريب. يمكن أن ينتج كل من التدريب القائم على الرقع والتدريب الالتفافي الكامل أي توزيع، على الرغم من أن كفاءتهما الحسابية النسبية تعتمد على التداخل وحجم الحزمة الصغيرة. التدريب الالتفافي الكامل للصورة الكاملة مطابق للتدريب القائم على الرقع حيث تتكون كل حزمة من جميع الحقول الاستقبالية للوحدات أسفل الخسارة لصورة (أو مجموعة من الصور). في حين أن هذا أكثر كفاءة من أخذ العينات الموحدة للرقع، فإنه يقلل من عدد الحزم الممكنة. ومع ذلك، يمكن استرداد الاختيار العشوائي للرقع داخل الصورة ببساطة. إن تقييد الخسارة بمجموعة فرعية تم أخذ عينات منها عشوائياً من حدودها المكانية (أو ما يعادل تطبيق قناع DropConnect [36] بين المخرجات والخسارة) يستبعد الرقع من حساب التدرج.

إذا كانت الرقع المحتفظ بها لا تزال تحتوي على تداخل كبير، فإن الحساب الالتفافي الكامل سيظل يسرع التدريب. إذا تم تجميع التدرجات على ممرات خلفية متعددة، يمكن أن تتضمن الحزم رقعاً من صور متعددة².

يمكن أن يصحح أخذ العينات في التدريب القائم على الرقع عدم توازن الفئات [27، 8، 2] ويخفف من الارتباط المكاني للرقع الكثيفة [28، 16]. في التدريب الالتفافي الكامل، يمكن أيضاً تحقيق توازن الفئات عن طريق ترجيح الخسارة، ويمكن استخدام أخذ عينات الخسارة لمعالجة الارتباط المكاني.

نستكشف التدريب بأخذ العينات في القسم 4.3، ولا نجد أنه ينتج تقارباً أسرع أو أفضل للتنبؤ الكثيف. تدريب الصورة الكاملة فعال وكفء.

---

¹ بافتراض تجميع فعال لمدخلات الصور الفردية. تستغرق درجات التصنيف لصورة واحدة بمفردها 5.4 ميلي ثانية للإنتاج، وهو أبطأ بنحو 25 مرة من النسخة الالتفافية الكاملة.

² لاحظ أنه لا يتم تضمين كل رقعة ممكنة بهذه الطريقة، نظراً لأن الحقول الاستقبالية لوحدات الطبقة النهائية تقع على شبكة ثابتة بخطوات. ومع ذلك، من خلال تحويل الصورة إلى اليسار وإلى الأسفل بقيمة عشوائية حتى الخطوة، يمكن استرداد الاختيار العشوائي من جميع الرقع الممكنة.

---

### Translation Notes

- **Figures referenced:** Figure 1, Figure 2
- **Key terms introduced:**
  - Receptive field (الحقول الاستقبالية / الحقل الاستقبالي)
  - Translation invariance (ثبات الترجمة)
  - Kernel size (حجم النواة)
  - Stride/subsampling factor (الخطوة / عامل العينات الفرعية)
  - Deep filter (مرشح عميق)
  - Feedforward computation (الحساب الأمامي)
  - Backpropagation (الانتشار العكسي)
  - Convolutionalized (التفافية محولة)
  - Ground truth (الحقيقة الأرضية)
  - Shift-and-stitch (التحويل والتشابك)
  - Filter rarefaction (ترقيق المرشح)
  - Upsampling (الرفع)
  - Backwards strided convolution/deconvolution (الالتفاف الخلفي بخطوات / فك الالتفاف)
  - Bilinear interpolation (الاستيفاء الخطي الثنائي)
  - In-network upsampling (الرفع داخل الشبكة)
  - Patchwise training (التدريب القائم على الرقع)
  - Loss sampling (أخذ عينات الخسارة)
  - DropConnect mask (قناع DropConnect)
  - Class imbalance (عدم توازن الفئات)
  - Spatial correlation (الارتباط المكاني)

- **Equations:** 3 mathematical equations preserved in LaTeX format
- **Citations:** References [2, 8, 16, 19, 20, 21, 27, 28, 29, 31, 32, 36]
- **Special handling:**
  - Preserved all mathematical notation in LaTeX
  - Kept network names (LeNet, AlexNet, OverFeat) in English
  - Translated footnotes at bottom of section
  - Maintained technical precision throughout

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.86

### Back-translation Check

Key sentence:
Arabic: "تُبنى الشبكات الالتفافية على ثبات الترجمة. مكوناتها الأساسية تعمل على مناطق إدخال موضعية، وتعتمد فقط على الإحداثيات المكانية النسبية"
Back: "Convolutional networks are built on translation invariance. Their basic components operate on local input regions, and depend only on relative spatial coordinates"
Original: "Convnets are built on translation invariance. Their basic components (convolution, pooling, and activation functions) operate on local input regions, and depend only on relative spatial coordinates"
✓ Semantic equivalence confirmed (minor difference in level of detail)
