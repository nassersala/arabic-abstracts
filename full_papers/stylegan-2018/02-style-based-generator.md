# Section 2: Style-based generator
## القسم 2: المولد القائم على الأنماط

**Section:** methodology
**Translation Quality:** 0.87
**Glossary Terms Used:** generator, latent code, latent space, mapping network, synthesis network, adaptive instance normalization (AdaIN), style transfer, feature maps, noise inputs, Fr​échet inception distance (FID), Progressive GAN

---

### English Version

Traditionally the latent code is provided to the generator through an input layer, i.e., the first layer of a feedforward network (Figure 1a). We depart from this design by omitting the input layer altogether and starting from a learned constant instead (Figure 1b, right). Given a latent code $\mathbf{z}$ in the input latent space $\mathcal{Z}$, a non-linear mapping network $f:\mathcal{Z}\to\mathcal{W}$ first produces $\mathbf{w} \in \mathcal{W}$ (Figure 1b, left). For simplicity, we set the dimensionality of both spaces to 512, and the mapping $f$ is implemented using an 8-layer MLP, a decision we will analyze in Section 4.1.

Learned affine transformations then specialize $\mathbf{w}$ to *styles* $\mathbf{y} = (\mathbf{y}_s, \mathbf{y}_b)$ that control adaptive instance normalization (AdaIN) operations after each convolution layer of the synthesis network $g$. The AdaIN operation is defined as

$$\textrm{AdaIN}(\mathbf{x}_i,\mathbf{y}) = \mathbf{y}_{s,i}\frac{\mathbf{x}_i-\mu(\mathbf{x}_i)}{\sigma(\mathbf{x}_i)} + \mathbf{y}_{b,i}$$

where each feature map $\mathbf{x}_i$ is normalized separately, and then scaled and biased using the corresponding scalar components from style $\mathbf{y}$. Thus the dimensionality of $\mathbf{y}$ is twice the number of feature maps on that layer.

Comparing our approach to style transfer, we compute the spatially invariant style $\mathbf{y}$ from vector $\mathbf{w}$ instead of an example image. We choose to reuse the word "style" for $\mathbf{y}$ because similar network architectures are already used for feedforward style transfer, unsupervised image-to-image translation, and domain mixtures. Compared to more general feature transforms, AdaIN is particularly well suited for our purposes due to its efficiency and compact representation.

Finally, we provide our generator with a direct means to generate stochastic detail by introducing explicit *noise inputs*. These are single-channel images consisting of uncorrelated Gaussian noise, and we feed a dedicated noise image to each layer of the synthesis network. The noise image is broadcasted to all feature maps using learned per-feature scaling factors and then added to the output of the corresponding convolution, as illustrated in Figure 1b. The implications of adding the noise inputs are discussed in Sections 3.2 and 3.3.

### Quality of generated images

Before studying the properties of our generator, we demonstrate experimentally that the redesign does not compromise image quality but, in fact, improves it considerably. Table 1 gives Fréchet inception distances (FID) for various generator architectures in CelebA-HQ and our new FFHQ dataset (Appendix A). Results for other datasets are given in Appendix B.

Our baseline configuration (A) is the Progressive GAN setup of Karras et al., from which we inherit the networks and all hyperparameters except where stated otherwise. We first switch to an improved baseline (B) by using bilinear up/downsampling operations, longer training, and tuned hyperparameters. A detailed description of training setups and hyperparameters is included in Appendix C.

We then improve this new baseline further by adding the mapping network and AdaIN operations (C), and make a surprising observation that the network no longer benefits from feeding the latent code into the first convolution layer. We therefore simplify the architecture by removing the traditional input layer and starting the image synthesis from a learned $4\times4\times512$ constant tensor (D). We find it quite remarkable that the synthesis network is able to produce meaningful results even though it receives input only through the styles that control the AdaIN operations.

Finally, we introduce the noise inputs (E) that improve the results further, as well as novel *mixing regularization* (F) that decorrelates neighboring styles and enables more fine-grained control over the generated imagery (Section 3.1).

We evaluate our methods using two different loss functions: for CelebA-HQ we rely on WGAN-GP, while FFHQ uses WGAN-GP for configuration A and non-saturating loss with $R_1$ regularization for configurations B-F. We found these choices to give the best results. Our contributions do not modify the loss function.

We observe that the style-based generator (E) improves FIDs quite significantly over the traditional generator (B), almost 20%, corroborating the large-scale ImageNet measurements made in parallel work. Figure 2 shows an uncurated set of novel images generated from the FFHQ dataset using our generator. As confirmed by the FIDs, the average quality is high, and even accessories such as eyeglasses and hats get successfully synthesized. For this figure, we avoided sampling from the extreme regions of $\mathcal{W}$ using the so-called truncation trick—Appendix D details how the trick can be performed in $\mathcal{W}$ instead of $\mathcal{Z}$. Note that our generator allows applying the truncation selectively to low resolutions only, so that high-resolution details are not affected.

All FIDs in this paper are computed without the truncation trick, and we only use it for illustrative purposes in Figure 2 and the video. All images are generated in $1024^2$ resolution.

### Prior art

Much of the work on GAN architectures has focused on improving the discriminator by, e.g., using multiple discriminators, multiresolution discrimination, or self-attention. The work on generator side has mostly focused on the exact distribution in the input latent space or shaping the input latent space via Gaussian mixture models, clustering, or encouraging convexity.

Recent conditional generators feed the class identifier through a separate embedding network to a large number of layers in the generator, while the latent is still provided though the input layer. A few authors have considered feeding parts of the latent code to multiple generator layers. In parallel work, Chen et al. "self modulate" the generator using AdaINs, similarly to our work, but do not consider an intermediate latent space or noise inputs.

---

### النسخة العربية

تقليدياً، تُقدّم الشفرة الكامنة إلى المولد من خلال طبقة مدخلات، أي الطبقة الأولى من شبكة أمامية التغذية (الشكل 1أ). نحن نبتعد عن هذا التصميم بحذف طبقة المدخلات تماماً والبدء من ثابت متعلم بدلاً من ذلك (الشكل 1ب، يمين). بالنظر إلى شفرة كامنة $\mathbf{z}$ في فضاء الكامن المدخل $\mathcal{Z}$، تنتج أولاً شبكة تعيين غير خطية $f:\mathcal{Z}\to\mathcal{W}$ القيمة $\mathbf{w} \in \mathcal{W}$ (الشكل 1ب، يسار). من أجل البساطة، نضبط بُعد كلا الفضاءين على 512، ويتم تنفيذ التعيين $f$ باستخدام شبكة عصبية متعددة الطبقات (MLP) من 8 طبقات، وهو قرار سنحلله في القسم 4.1.

ثم تخصص التحويلات الأفينية المتعلمة القيمة $\mathbf{w}$ إلى *أنماط* $\mathbf{y} = (\mathbf{y}_s, \mathbf{y}_b)$ التي تتحكم في عمليات التطبيع المثيلي التكيفي (AdaIN) بعد كل طبقة التفاف في شبكة التوليد $g$. تُعرّف عملية AdaIN كالتالي:

$$\textrm{AdaIN}(\mathbf{x}_i,\mathbf{y}) = \mathbf{y}_{s,i}\frac{\mathbf{x}_i-\mu(\mathbf{x}_i)}{\sigma(\mathbf{x}_i)} + \mathbf{y}_{b,i}$$

حيث يتم تطبيع كل خريطة ميزات $\mathbf{x}_i$ بشكل منفصل، ثم تُقاس وتُضاف إليها الانحياز باستخدام المكونات القياسية المقابلة من النمط $\mathbf{y}$. وبالتالي فإن بُعد $\mathbf{y}$ هو ضعف عدد خرائط الميزات في تلك الطبقة.

بمقارنة نهجنا بنقل الأنماط، نحسب النمط الثابت مكانياً $\mathbf{y}$ من المتجه $\mathbf{w}$ بدلاً من صورة مثال. نختار إعادة استخدام كلمة "نمط" لـ $\mathbf{y}$ لأن معماريات شبكات مشابهة تُستخدم بالفعل لنقل الأنماط الأمامي التغذية، والترجمة غير الموجهة من صورة إلى صورة، ومزيج المجالات. بالمقارنة مع تحويلات الميزات الأكثر عمومية، فإن AdaIN مناسب بشكل خاص لأغراضنا نظراً لكفاءته وتمثيله المدمج.

أخيراً، نزود مولدنا بوسيلة مباشرة لتوليد التفاصيل العشوائية من خلال إدخال *مدخلات ضوضاء* صريحة. هذه صور أحادية القناة تتكون من ضوضاء غاوسية غير مترابطة، ونغذي صورة ضوضاء مخصصة لكل طبقة من شبكة التوليد. يتم بث صورة الضوضاء إلى جميع خرائط الميزات باستخدام عوامل قياس متعلمة لكل ميزة ثم تضاف إلى مخرجات الالتفاف المقابل، كما هو موضح في الشكل 1ب. تُناقش آثار إضافة مدخلات الضوضاء في القسمين 3.2 و3.3.

### جودة الصور المولدة

قبل دراسة خصائص مولدنا، نثبت تجريبياً أن إعادة التصميم لا تضر بجودة الصورة بل تحسّنها بشكل كبير في الواقع. يعطي الجدول 1 مسافات Fréchet الاستنتاجية (FID) لمعماريات مولدات مختلفة في CelebA-HQ ومجموعة بيانات FFHQ الجديدة (الملحق A). تُعطى النتائج لمجموعات بيانات أخرى في الملحق B.

تكوين خط الأساس لدينا (A) هو إعداد Progressive GAN لـ Karras وآخرون، والذي نرث منه الشبكات وجميع المعاملات الفائقة إلا حيث ذُكر خلاف ذلك. ننتقل أولاً إلى خط أساس محسّن (B) باستخدام عمليات أخذ عينات أعلى/أسفل خطية ثنائية، وتدريب أطول، ومعاملات فائقة مضبوطة. يتضمن الملحق C وصفاً تفصيلياً لإعدادات التدريب والمعاملات الفائقة.

ثم نحسّن خط الأساس الجديد هذا بشكل أكبر من خلال إضافة شبكة التعيين وعمليات AdaIN (C)، ونلاحظ بشكل مفاجئ أن الشبكة لم تعد تستفيد من تغذية الشفرة الكامنة في طبقة الالتفاف الأولى. لذلك نبسّط المعمارية بإزالة طبقة المدخلات التقليدية وبدء توليد الصورة من موتر ثابت متعلم بأبعاد $4\times4\times512$ (D). نجد أنه من الرائع جداً أن شبكة التوليد قادرة على إنتاج نتائج ذات معنى على الرغم من أنها تتلقى المدخلات فقط من خلال الأنماط التي تتحكم في عمليات AdaIN.

أخيراً، نقدم مدخلات الضوضاء (E) التي تحسّن النتائج أكثر، بالإضافة إلى *تنظيم المزج* الجديد (F) الذي يفك الترابط بين الأنماط المتجاورة ويمكّن من تحكم أكثر دقة في الصور المولدة (القسم 3.1).

نقيّم أساليبنا باستخدام دالتي خسارة مختلفتين: بالنسبة لـ CelebA-HQ نعتمد على WGAN-GP، بينما تستخدم FFHQ WGAN-GP للتكوين A وخسارة عدم التشبع مع تنظيم $R_1$ للتكوينات B-F. وجدنا أن هذه الخيارات تعطي أفضل النتائج. مساهماتنا لا تعدّل دالة الخسارة.

نلاحظ أن المولد القائم على الأنماط (E) يحسّن مسافات FID بشكل ملحوظ جداً مقارنة بالمولد التقليدي (B)، بنسبة تقارب 20%، مما يؤكد القياسات واسعة النطاق على ImageNet التي تمت في عمل موازٍ. يوضح الشكل 2 مجموعة غير منسقة من الصور الجديدة المولدة من مجموعة بيانات FFHQ باستخدام مولدنا. كما تؤكد مسافات FID، الجودة المتوسطة عالية، وحتى الإكسسوارات مثل النظارات والقبعات يتم توليدها بنجاح. لهذا الشكل، تجنبنا أخذ العينات من المناطق القصوى في $\mathcal{W}$ باستخدام ما يسمى حيلة الاقتطاع—يفصّل الملحق D كيف يمكن تنفيذ الحيلة في $\mathcal{W}$ بدلاً من $\mathcal{Z}$. لاحظ أن مولدنا يسمح بتطبيق الاقتطاع بشكل انتقائي على الدقة المنخفضة فقط، بحيث لا تتأثر التفاصيل عالية الدقة.

يتم حساب جميع مسافات FID في هذه الورقة بدون حيلة الاقتطاع، ونستخدمها فقط لأغراض توضيحية في الشكل 2 والفيديو. يتم توليد جميع الصور بدقة $1024^2$.

### الأعمال السابقة

ركز الكثير من العمل على معماريات GAN على تحسين المميز باستخدام، على سبيل المثال، مميزات متعددة، أو التمييز متعدد الدقة، أو الانتباه الذاتي. ركز العمل على جانب المولد في الغالب على التوزيع الدقيق في فضاء الكامن المدخل أو تشكيل فضاء الكامن المدخل عبر نماذج مزيج غاوسي، أو التجميع، أو تشجيع التحدب.

تغذي المولدات الشرطية الحديثة معرّف الفئة من خلال شبكة تضمين منفصلة إلى عدد كبير من الطبقات في المولد، بينما لا يزال الكامن يُقدم من خلال طبقة المدخلات. نظر عدد قليل من المؤلفين في تغذية أجزاء من الشفرة الكامنة إلى طبقات مولد متعددة. في عمل موازٍ، "يعدّل ذاتياً" Chen وآخرون المولد باستخدام AdaINs، بشكل مشابه لعملنا، لكنهم لا يأخذون في الاعتبار فضاء كامن وسيط أو مدخلات ضوضاء.

---

### Translation Notes

- **Figures referenced:** Figure 1 (architecture diagrams), Figure 2 (generated images), Table 1 (FID scores)
- **Key terms introduced:**
  - Feedforward network (شبكة أمامية التغذية)
  - Mapping network (شبكة التعيين)
  - Synthesis network (شبكة التوليد)
  - Adaptive instance normalization - AdaIN (التطبيع المثيلي التكيفي)
  - Affine transformation (التحويل الأفيني)
  - Feature map (خريطة الميزات)
  - Gaussian noise (ضوضاء غاوسية)
  - Truncation trick (حيلة الاقتطاع)
  - Mixing regularization (تنظيم المزج)
  - Non-saturating loss (خسارة عدم التشبع)
- **Equations:** 1 (AdaIN formula)
- **Citations:** Multiple references to Karras2017, Huang2017, Goodfellow2014, etc.
- **Special handling:** Mathematical equations preserved in LaTeX format, references to appendices maintained

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87
