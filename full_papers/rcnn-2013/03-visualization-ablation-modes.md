# Section 3: Visualization, ablation, and modes of error
## القسم 3: التصور، والدراسات الاستئصالية، وأنماط الأخطاء

**Section:** visualization-ablation-modes
**Translation Quality:** 0.86
**Glossary Terms Used:** visualization, ablation, feature detector, pooling, receptive field, fine-tuning, architecture, regression, error analysis, precision

---

### English Version

## 3. Visualization, ablation, and modes of error

### 3.1. Visualizing learned features

First-layer filters can be visualized directly and are easy to understand [25]. They capture oriented edges and opponent colors. Understanding the subsequent layers is more challenging. Zeiler and Fergus present a visually attractive deconvolutional approach in [42]. We propose a simple (and complementary) non-parametric method that directly shows what the network learned.

The idea is to single out a particular unit (feature) in the network and use it as if it were an object detector in its own right. That is, we compute the unit's activations on a large set of held-out region proposals (about 10 million), sort the proposals from highest to lowest activation, perform non-maximum suppression, and then display the top-scoring regions. Our method lets the selected unit "speak for itself" by showing exactly which inputs it fires on. We avoid averaging in order to see different visual modes and gain insight into the invariances computed by the unit.

We visualize units from layer pool5, which is the max-pooled output of the network's fifth and final convolutional layer. The pool5 feature map is 6×6×256 = 9216-dimensional. Ignoring boundary effects, each pool5 unit has a receptive field of 195×195 pixels in the original 227×227 pixel input. A central pool5 unit has a nearly global view, while one near the edge has a smaller, clipped support.

Each row in Figure 4 displays the top 16 activations for a pool5 unit from a CNN that we fine-tuned on VOC 2007 trainval. Six of the 256 functionally unique units are visualized (Appendix D includes more). These units were selected to show a representative sample of what the network learns. In the second row, we see a unit that fires on dog faces and dot arrays. The unit corresponding to the third row is a red blob detector. There are also detectors for human faces and more abstract patterns such as text and triangular structures with windows. The network appears to learn a representation that combines a small number of class-tuned features together with a distributed representation of shape, texture, color, and material properties. The subsequent fully connected layer fc6 has the ability to model a large set of compositions of these rich features.

### 3.2. Ablation studies

**Performance layer-by-layer, without fine-tuning.** To understand which layers are critical for detection performance, we analyzed results on the VOC 2007 dataset for each of the CNN's last three layers. Layer pool5 was briefly described in Section 3.1. The final two layers are summarized below.

Layer fc6 is fully connected to pool5. To compute features, it multiplies a 4096×9216 weight matrix by the pool5 feature map (reshaped as a 9216-dimensional vector) and then adds a vector of biases. This intermediate vector is component-wise half-wave rectified (x → max(0,x)).

Layer fc7 is the final layer of the network. It is implemented by multiplying the features computed by fc6 by a 4096×4096 weight matrix, and similarly adding a vector of biases and applying half-wave rectification.

We start by looking at results from the CNN without fine-tuning on PASCAL, i.e. all CNN parameters were pre-trained on ILSVRC 2012 only. Analyzing performance layer-by-layer (Table 2 rows 1-3) reveals that features from fc7 generalize worse than features from fc6. This means that 29%, or about 16.8 million, of the CNN's parameters can be removed without degrading mAP. More surprising is that removing both fc7 and fc6 produces quite good results even though pool5 features are computed using only 6% of the CNN's parameters. Much of the CNN's representational power comes from its convolutional layers, rather than from the much larger densely connected layers. This finding suggests potential utility in computing a dense feature map, in the sense of HOG, of an arbitrary-sized image by using only the convolutional layers of the CNN. This representation would enable experimentation with sliding-window detectors, including DPM, on top of pool5 features.

**Performance layer-by-layer, with fine-tuning.** We now look at results from our CNN after having fine-tuned its parameters on VOC 2007 trainval. The improvement is striking (Table 2 rows 4-6): fine-tuning increases mAP by 8.0 percentage points to 54.2%. The boost from fine-tuning is much larger for fc6 and fc7 than for pool5, which suggests that the pool5 features learned from ImageNet are general and that most of the improvement is gained from learning domain-specific non-linear classifiers on top of them.

**Comparison to recent feature learning methods.** Relatively few feature learning methods have been tried on PASCAL VOC detection. We look at two recent approaches that build on deformable part models. For reference, we also include results for the standard HOG-based DPM [20].

The first DPM feature learning method, DPM ST [28], augments HOG features with histograms of "sketch token" probabilities. Intuitively, a sketch token is a tight distribution of contours passing through the center of an image patch. Sketch token probabilities are computed at each pixel by a random forest that was trained to classify 35×35 pixel patches into one of 150 sketch tokens or background.

The second method, DPM HSC [31], replaces HOG with histograms of sparse codes (HSC). To compute an HSC, sparse code activations are solved for at each pixel using a learned dictionary of 100 7×7 pixel (grayscale) atoms. The resulting activations are rectified in three ways (full and both half-waves), spatially pooled, unit ℓ2 normalized, and then power transformed (x → sign(x)|x|^α).

All R-CNN variants strongly outperform the three DPM baselines (Table 2 rows 8-10), including the two that use feature learning. Compared to the latest version of DPM, which uses only HOG features, our mAP is more than 20 percentage points higher: 54.2% vs. 33.7%—a 61% relative improvement. The combination of HOG and sketch tokens yields 2.5 mAP points over HOG alone, while HSC improves over HOG by 4 mAP points (when compared internally to their private DPM baselines—both use non-public implementations of DPM that underperform the open source version [20]). These methods achieve mAPs of 29.1% and 34.3%, respectively.

### 3.3. Network architectures

Most results in this paper use the network architecture from Krizhevsky et al. [25]. However, we have found that the choice of architecture has a large effect on R-CNN detection performance. In Table 3 we show results on VOC 2007 test using the 16-layer deep network recently proposed by Simonyan and Zisserman [43]. This network was one of the top performers in the recent ILSVRC 2014 classification challenge. The network has a homogeneous structure consisting of 13 layers of 3×3 convolution kernels, with five max pooling layers interspersed, and topped with three fully-connected layers. We refer to this network as "O-Net" for OxfordNet and the baseline as "T-Net" for TorontoNet.

To use O-Net in R-CNN, we downloaded the publicly available pre-trained network weights for the VGG_ILSVRC_16_layers model from the Caffe Model Zoo. We then fine-tuned the network using the same protocol as we used for T-Net. The only difference was to use smaller minibatches (24 examples) as required in order to fit within GPU memory. The results in Table 3 show that R-CNN with O-Net substantially outperforms R-CNN with T-Net, increasing mAP from 58.5% to 66.0%. However there is a considerable drawback in terms of compute time, with the forward pass of O-Net taking roughly 7 times longer than T-Net.

### 3.4. Detection error analysis

We applied the excellent detection analysis tool from Hoiem et al. [23] in order to reveal our method's error modes, understand how fine-tuning changes them, and to see how our error types compare with DPM. A full summary of the analysis tool is beyond the scope of this paper and we encourage readers to consult [23] to understand some finer details (such as "normalized AP"). Since the analysis is best absorbed in the context of the associated plots, we present the discussion within the captions of Figure 5 and Figure 6.

### 3.5. Bounding-box regression

Based on the error analysis, we implemented a simple method to reduce localization errors. Inspired by the bounding-box regression employed in DPM [17], we train a linear regression model to predict a new detection window given the pool5 features for a selective search region proposal. Full details are given in Appendix C. Results in Table 1, Table 2, and Figure 5 show that this simple approach fixes a large number of mislocalized detections, boosting mAP by 3 to 4 points.

### 3.6. Qualitative results

Qualitative detection results on ILSVRC2013 are presented in Figure 8 and Figure 9 at the end of the paper. Each image was sampled randomly from the val2 set and all detections from all detectors with a precision greater than 0.5 are shown. Note that these are not curated and give a realistic impression of the detectors in action. More qualitative results are presented in Figure 10 and Figure 11, but these have been curated. We selected each image because it contained interesting, surprising, or amusing results. Here, also, all detections at precision greater than 0.5 are shown.

---

### النسخة العربية

## 3. التصور، والدراسات الاستئصالية، وأنماط الأخطاء

### 3.1. تصور الميزات المتعلمة

يمكن تصور مرشحات الطبقة الأولى مباشرة وهي سهلة الفهم [25]. تلتقط الحواف الموجهة والألوان المتعارضة. فهم الطبقات اللاحقة أكثر تحدياً. يقدم Zeiler وFergus نهجاً تفكيكياً جذاباً بصرياً في [42]. نقترح طريقة غير بارامترية بسيطة (ومكملة) تُظهر مباشرة ما تعلمته الشبكة.

الفكرة هي عزل وحدة معينة (ميزة) في الشبكة واستخدامها كما لو كانت كاشف أجسام في حد ذاتها. أي، نحسب تنشيطات الوحدة على مجموعة كبيرة من مقترحات المناطق المحتفظ بها (حوالي 10 ملايين)، نرتب المقترحات من أعلى إلى أدنى تنشيط، نجري كبت غير الحد الأقصى، ثم نعرض المناطق الأعلى تسجيلاً. تتيح طريقتنا للوحدة المختارة "التحدث عن نفسها" من خلال إظهار بالضبط المدخلات التي تنشطها. نتجنب حساب المتوسط لنرى الأنماط المرئية المختلفة ونكتسب رؤية ثاقبة حول الثوابت المحسوبة بواسطة الوحدة.

نصور وحدات من طبقة pool5، وهي المخرجات المجمعة بالحد الأقصى من الطبقة الالتفافية الخامسة والأخيرة للشبكة. خريطة ميزات pool5 هي 6×6×256 = 9216 بُعد. بتجاهل تأثيرات الحدود، كل وحدة pool5 لها حقل استقبالي 195×195 بكسل في المدخل الأصلي 227×227 بكسل. وحدة pool5 المركزية لها رؤية شبه عالمية، بينما الوحدة القريبة من الحافة لها دعم أصغر ومقتطع.

يعرض كل صف في الشكل 4 أعلى 16 تنشيطاً لوحدة pool5 من شبكة عصبية التفافية قمنا بضبطها بدقة على VOC 2007 trainval. تم تصور ستة من 256 وحدة فريدة وظيفياً (يتضمن الملحق D المزيد). تم اختيار هذه الوحدات لإظهار عينة تمثيلية مما تتعلمه الشبكة. في الصف الثاني، نرى وحدة تنشط على وجوه الكلاب ومصفوفات النقاط. الوحدة المقابلة للصف الثالث هي كاشف للبقع الحمراء. هناك أيضاً كواشف لوجوه البشر والأنماط الأكثر تجريداً مثل النص والهياكل المثلثية مع النوافذ. يبدو أن الشبكة تتعلم تمثيلاً يجمع بين عدد صغير من الميزات المضبوطة للصنف مع تمثيل موزع للشكل والملمس واللون وخصائص المادة. الطبقة المتصلة بالكامل اللاحقة fc6 لديها القدرة على نمذجة مجموعة كبيرة من تركيبات هذه الميزات الغنية.

### 3.2. الدراسات الاستئصالية

**الأداء طبقة تلو الأخرى، بدون ضبط دقيق.** لفهم الطبقات الحاسمة لأداء الكشف، قمنا بتحليل النتائج على مجموعة بيانات VOC 2007 لكل من الطبقات الثلاث الأخيرة للشبكة العصبية الالتفافية. تم وصف طبقة pool5 بإيجاز في القسم 3.1. يتم تلخيص الطبقتين الأخيرتين أدناه.

الطبقة fc6 متصلة بالكامل بـ pool5. لحساب الميزات، تضرب مصفوفة أوزان 4096×9216 في خريطة ميزات pool5 (المعاد تشكيلها كمتجه 9216 بُعد) ثم تضيف متجه التحيزات. يتم تصحيح هذا المتجه الوسيط بموجة نصفية عنصراً بعنصر (x → max(0,x)).

الطبقة fc7 هي الطبقة النهائية للشبكة. يتم تنفيذها بضرب الميزات المحسوبة بواسطة fc6 في مصفوفة أوزان 4096×4096، وبالمثل إضافة متجه من التحيزات وتطبيق التصحيح بالموجة النصفية.

نبدأ بالنظر إلى النتائج من الشبكة العصبية الالتفافية بدون ضبط دقيق على PASCAL، أي تم التدريب المسبق لجميع معاملات الشبكة العصبية الالتفافية على ILSVRC 2012 فقط. يكشف تحليل الأداء طبقة تلو الأخرى (الجدول 2 الصفوف 1-3) أن ميزات fc7 تعمم بشكل أسوأ من ميزات fc6. هذا يعني أن 29%، أو حوالي 16.8 مليون، من معاملات الشبكة العصبية الالتفافية يمكن إزالتها دون تدهور mAP. الأكثر إثارة للدهشة هو أن إزالة كل من fc7 وfc6 ينتج نتائج جيدة جداً على الرغم من أن ميزات pool5 تُحسب باستخدام 6% فقط من معاملات الشبكة العصبية الالتفافية. الكثير من القوة التمثيلية للشبكة العصبية الالتفافية يأتي من طبقاتها الالتفافية، بدلاً من الطبقات المتصلة بكثافة الأكبر بكثير. يشير هذا الاكتشاف إلى فائدة محتملة في حساب خريطة ميزات كثيفة، بمعنى HOG، لصورة ذات حجم تعسفي باستخدام الطبقات الالتفافية للشبكة العصبية الالتفافية فقط. سيمكّن هذا التمثيل من التجريب مع كواشف النافذة المنزلقة، بما في ذلك DPM، فوق ميزات pool5.

**الأداء طبقة تلو الأخرى، مع الضبط الدقيق.** ننظر الآن إلى النتائج من شبكتنا العصبية الالتفافية بعد ضبط معاملاتها بدقة على VOC 2007 trainval. التحسن مذهل (الجدول 2 الصفوف 4-6): يزيد الضبط الدقيق mAP بمقدار 8.0 نقاط مئوية إلى 54.2%. الدفعة من الضبط الدقيق أكبر بكثير لـ fc6 وfc7 من pool5، مما يشير إلى أن ميزات pool5 المتعلمة من ImageNet عامة وأن معظم التحسين يُكتسب من تعلم مصنفات غير خطية خاصة بالمجال فوقها.

**المقارنة مع طرق تعلم الميزات الحديثة.** تم تجربة عدد قليل نسبياً من طرق تعلم الميزات على كشف PASCAL VOC. ننظر إلى نهجين حديثين يبنيان على نماذج الأجزاء القابلة للتشوه. للمرجع، نضمّن أيضاً نتائج DPM القياسي القائم على HOG [20].

طريقة تعلم ميزات DPM الأولى، DPM ST [28]، تعزز ميزات HOG بهيستوجرامات احتماليات "رمز الرسم". بشكل حدسي، رمز الرسم هو توزيع ضيق للحواف التي تمر عبر مركز رقعة الصورة. يتم حساب احتماليات رمز الرسم عند كل بكسل بواسطة غابة عشوائية تم تدريبها لتصنيف رقع البكسل 35×35 إلى واحدة من 150 رمز رسم أو خلفية.

الطريقة الثانية، DPM HSC [31]، تستبدل HOG بهيستوجرامات الرموز المتفرقة (HSC). لحساب HSC، يتم حل تنشيطات الرموز المتفرقة عند كل بكسل باستخدام قاموس متعلم من 100 ذرة بكسل 7×7 (تدرج رمادي). يتم تصحيح التنشيطات الناتجة بثلاث طرق (كاملة وكلا الموجتين النصفيتين)، مجمعة مكانياً، ومُعايرة ℓ2 للوحدة، ثم محولة بالقوة (x → sign(x)|x|^α).

تتفوق جميع متغيرات R-CNN بقوة على خطوط الأساس الثلاثة لـ DPM (الجدول 2 الصفوف 8-10)، بما في ذلك الاثنان اللذان يستخدمان تعلم الميزات. مقارنة بأحدث نسخة من DPM، التي تستخدم ميزات HOG فقط، فإن mAP الخاص بنا أعلى بأكثر من 20 نقطة مئوية: 54.2% مقابل 33.7% - تحسن نسبي بنسبة 61%. يحقق الجمع بين HOG ورموز الرسم 2.5 نقطة mAP على HOG وحده، بينما يحسن HSC على HOG بمقدار 4 نقاط mAP (عند المقارنة داخلياً بخطوط الأساس الخاصة لـ DPM - كلاهما يستخدم تطبيقات غير عامة لـ DPM تؤدي أداءً أقل من النسخة مفتوحة المصدر [20]). تحقق هذه الطرق mAP بنسبة 29.1% و34.3%، على التوالي.

### 3.3. معماريات الشبكات

تستخدم معظم النتائج في هذا البحث معمارية الشبكة من Krizhevsky وآخرين [25]. ومع ذلك، وجدنا أن اختيار المعمارية له تأثير كبير على أداء كشف R-CNN. في الجدول 3 نُظهر النتائج على اختبار VOC 2007 باستخدام الشبكة العميقة ذات 16 طبقة المقترحة مؤخراً من Simonyan وZisserman [43]. كانت هذه الشبكة واحدة من الأداء الأفضل في تحدي تصنيف ILSVRC 2014 الأخير. الشبكة لها بنية متجانسة تتكون من 13 طبقة من نوى التفاف 3×3، مع خمس طبقات تجميع بالحد الأقصى متخللة، ومغطاة بثلاث طبقات متصلة بالكامل. نشير إلى هذه الشبكة باسم "O-Net" لـ OxfordNet وخط الأساس باسم "T-Net" لـ TorontoNet.

لاستخدام O-Net في R-CNN، قمنا بتحميل أوزان الشبكة المدربة مسبقاً المتاحة للعامة لنموذج VGG_ILSVRC_16_layers من Caffe Model Zoo. ثم قمنا بالضبط الدقيق للشبكة باستخدام نفس البروتوكول الذي استخدمناه لـ T-Net. الفرق الوحيد كان استخدام دفعات صغيرة أصغر (24 مثالاً) كما هو مطلوب لتلائم ذاكرة GPU. تُظهر النتائج في الجدول 3 أن R-CNN مع O-Net يتفوق بشكل كبير على R-CNN مع T-Net، مما يزيد mAP من 58.5% إلى 66.0%. ومع ذلك، هناك عيب كبير من حيث وقت الحساب، حيث يستغرق المرور الأمامي لـ O-Net حوالي 7 مرات أطول من T-Net.

### 3.4. تحليل أخطاء الكشف

طبقنا أداة تحليل الكشف الممتازة من Hoiem وآخرين [23] من أجل الكشف عن أنماط أخطاء طريقتنا، وفهم كيف يغيرها الضبط الدقيق، ولمعرفة كيف تقارن أنواع أخطائنا مع DPM. الملخص الكامل لأداة التحليل يتجاوز نطاق هذا البحث ونشجع القراء على استشارة [23] لفهم بعض التفاصيل الدقيقة (مثل "AP المعاير"). نظراً لأن التحليل يُستوعب بشكل أفضل في سياق الرسوم البيانية المرتبطة، نقدم المناقشة ضمن تسميات الشكل 5 والشكل 6.

### 3.5. انحدار صندوق التحديد

بناءً على تحليل الأخطاء، قمنا بتنفيذ طريقة بسيطة لتقليل أخطاء التوطين. مستوحاة من انحدار صندوق التحديد المستخدم في DPM [17]، ندرب نموذج انحدار خطي للتنبؤ بنافذة كشف جديدة بناءً على ميزات pool5 لمقترح منطقة البحث الانتقائي. التفاصيل الكاملة معطاة في الملحق C. تُظهر النتائج في الجدول 1 والجدول 2 والشكل 5 أن هذا النهج البسيط يصلح عدداً كبيراً من الكشوفات المحددة بشكل خاطئ، مما يعزز mAP بمقدار 3 إلى 4 نقاط.

### 3.6. النتائج النوعية

يتم عرض نتائج الكشف النوعية على ILSVRC2013 في الشكل 8 والشكل 9 في نهاية البحث. تم أخذ عينة عشوائية من كل صورة من مجموعة val2 ويتم عرض جميع الكشوفات من جميع الكواشف بدقة أكبر من 0.5. لاحظ أن هذه ليست منتقاة وتعطي انطباعاً واقعياً عن الكواشف أثناء العمل. يتم عرض المزيد من النتائج النوعية في الشكل 10 والشكل 11، لكن هذه تم تنظيمها. اخترنا كل صورة لأنها تحتوي على نتائج مثيرة للاهتمام أو مفاجئة أو مسلية. هنا أيضاً، يتم عرض جميع الكشوفات بدقة أكبر من 0.5.

---

### Translation Notes

- **Figures referenced:** Figure 4 (pool5 unit visualizations), Figure 5 (error distribution), Figure 6 (sensitivity analysis), Figure 8-11 (qualitative results), Table 1-3 (performance comparisons)
- **Key terms introduced:** ablation (الدراسات الاستئصالية), receptive field (حقل استقبالي), max pooling (تجميع بالحد الأقصى), deformable part models (نماذج الأجزاء القابلة للتشوه), sketch token (رمز الرسم), sparse codes (الرموز المتفرقة)
- **Equations:** Mathematical notation for half-wave rectification (x → max(0,x)), power transformation (x → sign(x)|x|^α)
- **Citations:** Multiple references [17, 20, 23, 25, 28, 31, 42, 43] cited throughout
- **Special handling:**
  - Preserved layer names: pool5, fc6, fc7
  - Maintained network names: T-Net (TorontoNet), O-Net (OxfordNet), VGG
  - Kept technical terms: HOG, DPM, mAP
  - Preserved mathematical notation and dimensionality (6×6×256, 4096×9216, etc.)
  - Maintained percentage values and improvement metrics

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.84
- Glossary consistency: 0.86
- **Overall section score:** 0.86
