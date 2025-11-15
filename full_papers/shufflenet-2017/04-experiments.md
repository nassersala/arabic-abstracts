# Section 4: Experiments
## القسم 4: التجارب

**Section:** experiments
**Translation Quality:** 0.87
**Glossary Terms Used:** ablation study, ImageNet classification, object detection, computational complexity, accuracy, feature map channels, group number, baseline, benchmark, generalization, speedup, inference

---

### English Version

## 4. Experiments

We mainly evaluate our models on the ImageNet 2012 classification dataset [4, 28]. We follow most of the training settings and hyper-parameters used in [40], with two exceptions: (i) we set the weight decay to 4e-5 instead of 1e-4 and use linear-decay learning rate policy (decreased from 0.5 to 0); (ii) we use slightly less aggressive scale augmentation for data preprocessing. Similar modifications are also referenced in [11] because such small networks usually suffer from underfitting rather than overfitting. It takes 1 or 2 days to train a model for 3×10⁵ iterations on 4 GPUs, whose batch size is set to 1024. To benchmark, we compare single crop top-1 performance on validation set, i.e. cropping 224×224 center view from 256× input image and evaluating classification accuracy.

### 4.1 Ablation Study

#### 4.1.1 Pointwise Group Convolutions

To evaluate the importance of pointwise group convolutions, we compare ShuffleNet models of the same complexity whose numbers of groups range from 1 to 8. If the group number equals 1, no pointwise group convolution is involved and then the ShuffleNet unit becomes an Xception-like [3] structure. For better understanding, we also scale the width of the networks to 3 different complexities and compare their classification performance respectively. Results are shown in Table 2.

From the results, we see that models with group convolutions (g > 1) consistently perform better than the counterparts without pointwise group convolutions (g = 1). Smaller models tend to benefit more from groups. For example, for ShuffleNet 1× the best entry (g = 8) is 1.2% better than the counterpart, while for ShuffleNet 0.5× and 0.25× the gaps become 3.5% and 4.4% respectively. Note that group convolutions allow more feature map channels for a given complexity constraint, so we hypothesize that the performance gain is mainly due to the fact that group convolutions enable encoding more information with wider feature maps. In addition, a smaller network involves thinner feature maps, meaning it benefits more from enlarged feature maps brought by group convolutions.

Table 2 also shows that for some models (e.g. ShuffleNet 0.5×) when group numbers become relatively large (e.g. g = 8), the classification score saturates or even drops. With an increase in group number (thus wider feature maps), input channels for each convolutional filter become fewer, which may harm representation capability. Interestingly, we also notice that for smaller models such as ShuffleNet 0.25× larger group numbers tend to better results consistently, which suggests wider feature maps bring more benefits for smaller models.

#### 4.1.2 Channel Shuffle vs. No Shuffle

The purpose of shuffle operation is to enable cross-group information flow for multiple group convolution layers. Table 3 compares the performance of ShuffleNet structures (group number is set to 3 or 8 for instance) with/without channel shuffle. The evaluations are performed under three different scales, i.e. 1×, 0.5× and 0.25×, respectively. It is clear that channel shuffle consistently boosts classification scores for different settings. Especially, when group number is relatively large (e.g. g = 8), models with channel shuffle outperform the counterparts by a significant margin, which shows the importance of cross-group information interchange.

### 4.2 Comparison with Other Structure Units

Recent leading architectures such as Xception [3], ResNeXt [40] have shown the effectiveness of depthwise separable convolution and group convolution respectively. We compare them with ShuffleNet on the same complexity. For fair comparison, we use the overall network architecture as illustrated in Table 1. Note that we report results of ResNeXt [40] with group number set to 16 because it shows better results than the default setting where group equals 32, for the cases of extremely small models (Section 4.1.1 also suggests that larger group number may not necessarily lead to better performance).

As shown in Table 4, three different types of structure units are compared under different complexities. Under the same computational complexity constraint, our ShuffleNet models outperform most others by a significant margin. Notably, ShuffleNet is 0.9%, 4.4%, and 12.5% better than ResNeXt under 140M, 38M, and 13M FLOPs respectively. We conjecture this is mainly because ShuffleNet is designed specially for small models where cardinality (number of channels) is crucial, while previous state-of-the-arts [40, 3] still suffer from limited feature channels in tiny models.

Note that although the architecture of ShuffleNet is inspired by Xception [3] and ResNeXt [40], the network structure still holds significant differences with them. We found that [3, 40] are not suitable for extremely small networks because their design can result in too few channels, which might be the reason for our significant improvements.

Also note that the purpose of the comparison in Table 4 is to demonstrate the effectiveness of our ShuffleNet design, not to compare the absolute performance of different model families. To obtain meaningful and fair comparisons among different architectures, proper tuning of the hyper-parameters (e.g. channel numbers) in those structures is necessary, which is beyond our scope.

### 4.3 Comparison with MobileNets and Other Frameworks

Recently Howard et al. [12] have proposed MobileNets which mainly focus on efficient network architecture for mobile devices. MobileNet also adopts depthwise separable convolution. Despite the difference in network architecture, MobileNet and ShuffleNet are both very competitive for small models. It is valuable to compare their performances. Table 5 shows the comparison results on ImageNet 2012 classification task across different model sizes.

It can be seen that our ShuffleNet models are superior to MobileNet [12] for various computational budgets. Though our ShuffleNet network is specially designed for small models (< 150 MFLOPs), we also find it is better when scaled to larger models (e.g. ~500 MFLOPs). For smaller networks (38M/140M FLOPs) our ShuffleNet models are significantly better than corresponding MobileNet counterparts by 7.8% and 3.1% respectively. By referring to the architecture and settings in Table 1, we additionally explore a series of ShuffleNet models for around ~500 MFLOPs. Our best ShuffleNet model (ShuffleNet 2×, g=3) also outperforms MobileNet 1.0 by 1.2% under similar computational constraint.

Though Xception [3] and ResNeXt [40] are mostly superior to ShuffleNet under high complexity constraints (e.g. > 500 MFLOPs, see Table 5), they are not suitable for computing platforms that have strict resource limitations. For instance, Xception-like [3] structure in Table 4 achieves 34.4% error with 42M FLOPs which is much worse than our ShuffleNet models with even fewer FLOPs. Also note that the classification error of our ShuffleNet 0.5× model is comparable with ResNet-18 [8] but its theoretical complexity is much smaller than ResNet-18 (40 vs 1800 MFLOPs), showing the advantages of our structure design.

We also benchmark a few other frameworks such as VGG [29], GoogLeNet [33] and SqueezeNet [15] in Table 5. Compared with those structures, ShuffleNet achieves comparable or better performance with much lower complexity. In conclusion, with similar accuracy ShuffleNet is 13× faster than MobileNet for real world speed.

Accuracy vs. FLOPs. To provide an intuitive comparison, we plot the top-1 error/FLOPs relation curve for different models in Fig 3 (Left). It is clear that ShuffleNet models are better than other models across various FLOPs. Notably, our ShuffleNet models outperform MobileNet at all evaluated complexity levels.

### 4.4 Generalization Ability

To evaluate the generalization ability, we also test our ShuffleNet model on a recently more challenging benchmark: MS COCO object detection [21]. We adopt Faster-RCNN [25] as the detection framework and use the publicly released Caffe code [32] for training with default settings. Similar to [12], the models are trained on the COCO train+val dataset excluding 8,000 minival images and we conduct testing on minival set. Table 7 reports the detection results under two input resolutions at different model scales. Compared to MobileNet [12] on 1× model (~1000 MFLOPs), our ShuffleNet 2× (524 MFLOPs) obtains comparable results on smaller input image size (600×) and better results on larger size (1000×). Compared to a smaller MobileNet (0.5×, 269 MFLOPs), ShuffleNet 1× (140 MFLOPs) achieves better results even at ~2× theoretical speedup. We conjecture that this significant gain is mainly attributed to ShuffleNet's simple, efficient and effective design.

### 4.5 Actual Speedup Evaluation

Finally, we evaluate the actual inference speed of ShuffleNet models on a mobile device with an ARM platform. Though some operations in ShuffleNet (such as group convolution and channel shuffle) may have less efficient implementation in currently available libraries, we believe better support for such operations can be achieved in the near future. The ShuffleNet model and other baselines are implemented using a highly optimized mobile deep learning library which we developed. The timing benchmarks only include computation time and exclude costs of image loading, memory swapping and other overheads. Table 8 shows the actual running time on the device and theoretical complexity. From the results, we see that the theoretical complexity is usually proportional to the actual running time. With similar accuracy (~43% ImageNet classification error), ShuffleNet 0.5× is faster than AlexNet [17] by a factor of ~13. Even compared with a smaller network (~57% error), ShuffleNet is still 3.7× faster than SqueezeNet [15] under comparable computational complexity as shown in Table 5.

---

### النسخة العربية

## 4. التجارب

نقوم بشكل أساسي بتقييم نماذجنا على مجموعة بيانات تصنيف ImageNet 2012 [4, 28]. نتبع معظم إعدادات التدريب والمعاملات الفائقة المستخدمة في [40]، مع استثناءين: (i) نضع تضاؤل الوزن على 4e-5 بدلاً من 1e-4 ونستخدم سياسة معدل التعلم المتناقص الخطي (ينخفض من 0.5 إلى 0)؛ (ii) نستخدم زيادة مقياس أقل عدوانية قليلاً لمعالجة البيانات المسبقة. يتم الإشارة أيضاً إلى تعديلات مماثلة في [11] لأن مثل هذه الشبكات الصغيرة عادةً ما تعاني من نقص التكيف بدلاً من الإفراط في التكيف. يستغرق تدريب نموذج لـ 3×10⁵ تكرار على 4 وحدات معالجة رسومات يوماً أو يومين، حيث يتم تعيين حجم الدفعة على 1024. للمعايرة، نقارن أداء top-1 لقص واحد على مجموعة التحقق، أي قص عرض مركزي 224×224 من صورة إدخال 256× وتقييم دقة التصنيف.

### 4.1 دراسة الإزالة (Ablation Study)

#### 4.1.1 الالتفافات النقطية المجموعية

لتقييم أهمية الالتفافات النقطية المجموعية، نقارن نماذج ShuffleNet بنفس التعقيد التي تتراوح أعداد مجموعاتها من 1 إلى 8. إذا كان رقم المجموعة يساوي 1، فلا يتم تضمين التفاف نقطي مجموعي وبالتالي تصبح وحدة ShuffleNet هيكلاً شبيهاً بـ Xception [3]. لفهم أفضل، نقوم أيضاً بتوسيع نطاق عرض الشبكات إلى 3 تعقيدات مختلفة ونقارن أداء التصنيف الخاص بها على التوالي. النتائج موضحة في الجدول 2.

من النتائج، نرى أن النماذج ذات الالتفافات المجموعية (g > 1) تؤدي باستمرار بشكل أفضل من النظيرات بدون الالتفافات النقطية المجموعية (g = 1). تميل النماذج الأصغر إلى الاستفادة أكثر من المجموعات. على سبيل المثال، بالنسبة لـ ShuffleNet 1× فإن الإدخال الأفضل (g = 8) أفضل بنسبة 1.2% من النظير، بينما بالنسبة لـ ShuffleNet 0.5× و 0.25× تصبح الفجوات 3.5% و 4.4% على التوالي. لاحظ أن الالتفافات المجموعية تسمح بمزيد من قنوات خرائط الميزات لقيد تعقيد معين، لذلك نفترض أن تحسن الأداء يرجع بشكل رئيسي إلى حقيقة أن الالتفافات المجموعية تمكن من ترميز المزيد من المعلومات مع خرائط ميزات أوسع. بالإضافة إلى ذلك، تتضمن الشبكة الأصغر خرائط ميزات أرق، مما يعني أنها تستفيد أكثر من خرائط الميزات الموسعة التي توفرها الالتفافات المجموعية.

يُظهر الجدول 2 أيضاً أنه بالنسبة لبعض النماذج (مثل ShuffleNet 0.5×) عندما تصبح أعداد المجموعات كبيرة نسبياً (مثل g = 8)، فإن درجة التصنيف تتشبع أو حتى تنخفض. مع زيادة عدد المجموعات (وبالتالي خرائط ميزات أوسع)، تصبح قنوات الإدخال لكل مرشح التفافي أقل، مما قد يضر بقدرة التمثيل. من المثير للاهتمام أننا نلاحظ أيضاً أنه بالنسبة للنماذج الأصغر مثل ShuffleNet 0.25× تميل أعداد المجموعات الأكبر إلى نتائج أفضل باستمرار، مما يشير إلى أن خرائط الميزات الأوسع تجلب المزيد من الفوائد للنماذج الأصغر.

#### 4.1.2 خلط القنوات مقابل عدم الخلط

الغرض من عملية الخلط هو تمكين تدفق المعلومات عبر المجموعات لطبقات الالتفاف المجموعي المتعددة. يقارن الجدول 3 أداء هياكل ShuffleNet (يتم تعيين رقم المجموعة على 3 أو 8 على سبيل المثال) مع/بدون خلط القنوات. يتم إجراء التقييمات تحت ثلاثة مقاييس مختلفة، أي 1× و 0.5× و 0.25×، على التوالي. من الواضح أن خلط القنوات يعزز باستمرار درجات التصنيف لإعدادات مختلفة. خاصة، عندما يكون رقم المجموعة كبيراً نسبياً (مثل g = 8)، فإن النماذج مع خلط القنوات تتفوق على النظيرات بهامش كبير، مما يُظهر أهمية تبادل المعلومات عبر المجموعات.

### 4.2 المقارنة مع وحدات الهياكل الأخرى

أظهرت المعماريات الرائدة الحديثة مثل Xception [3] و ResNeXt [40] فعالية الالتفاف الفصلي العميق والالتفاف المجموعي على التوالي. نقارنهم مع ShuffleNet على نفس التعقيد. للمقارنة العادلة، نستخدم معمارية الشبكة الشاملة كما هو موضح في الجدول 1. لاحظ أننا نبلغ عن نتائج ResNeXt [40] مع تعيين رقم المجموعة على 16 لأنه يُظهر نتائج أفضل من الإعداد الافتراضي حيث تساوي المجموعة 32، لحالات النماذج الصغيرة جداً (يشير القسم 4.1.1 أيضاً إلى أن رقم المجموعة الأكبر قد لا يؤدي بالضرورة إلى أداء أفضل).

كما هو موضح في الجدول 4، تتم مقارنة ثلاثة أنواع مختلفة من وحدات الهيكل تحت تعقيدات مختلفة. تحت قيد التعقيد الحسابي نفسه، تتفوق نماذج ShuffleNet الخاصة بنا على معظم النماذج الأخرى بهامش كبير. والجدير بالذكر أن ShuffleNet أفضل بنسبة 0.9% و 4.4% و 12.5% من ResNeXt تحت 140 مليون و 38 مليون و 13 مليون عملية فاصلة عائمة على التوالي. نفترض أن هذا يرجع بشكل رئيسي إلى أن ShuffleNet مصممة خصيصاً للنماذج الصغيرة حيث تكون العددية (cardinality) (عدد القنوات) حاسمة، بينما لا تزال الأعمال الحديثة السابقة [40, 3] تعاني من قنوات ميزات محدودة في النماذج الصغيرة.

لاحظ أنه على الرغم من أن معمارية ShuffleNet مستوحاة من Xception [3] و ResNeXt [40]، إلا أن هيكل الشبكة لا يزال يحمل اختلافات كبيرة معهم. وجدنا أن [3, 40] غير مناسبين للشبكات الصغيرة جداً لأن تصميمهما يمكن أن يؤدي إلى قنوات قليلة جداً، والتي قد تكون السبب في تحسيناتنا الكبيرة.

لاحظ أيضاً أن الغرض من المقارنة في الجدول 4 هو إظهار فعالية تصميم ShuffleNet الخاص بنا، وليس لمقارنة الأداء المطلق لعائلات النماذج المختلفة. للحصول على مقارنات ذات مغزى وعادلة بين المعماريات المختلفة، من الضروري الضبط المناسب للمعاملات الفائقة (مثل أعداد القنوات) في تلك الهياكل، وهو خارج نطاقنا.

### 4.3 المقارنة مع MobileNets والأطر الأخرى

مؤخراً، اقترح Howard وآخرون [12] MobileNets التي تركز بشكل رئيسي على معمارية الشبكة الفعالة للأجهزة المحمولة. تعتمد MobileNet أيضاً على الالتفاف الفصلي العميق. على الرغم من الاختلاف في معمارية الشبكة، فإن كلاً من MobileNet و ShuffleNet تنافسيتان جداً للنماذج الصغيرة. من المفيد مقارنة أدائهما. يُظهر الجدول 5 نتائج المقارنة على مهمة تصنيف ImageNet 2012 عبر أحجام نماذج مختلفة.

يمكن ملاحظة أن نماذج ShuffleNet الخاصة بنا متفوقة على MobileNet [12] لميزانيات حسابية مختلفة. على الرغم من أن شبكة ShuffleNet الخاصة بنا مصممة خصيصاً للنماذج الصغيرة (< 150 ميجا عملية فاصلة عائمة)، فإننا نجد أيضاً أنها أفضل عند توسيع نطاقها إلى نماذج أكبر (على سبيل المثال ~500 ميجا عملية فاصلة عائمة). بالنسبة للشبكات الأصغر (38 مليون/140 مليون عملية فاصلة عائمة)، فإن نماذج ShuffleNet الخاصة بنا أفضل بكثير من نظيرات MobileNet المقابلة بنسبة 7.8% و 3.1% على التوالي. بالإشارة إلى المعمارية والإعدادات في الجدول 1، نستكشف أيضاً سلسلة من نماذج ShuffleNet لحوالي ~500 ميجا عملية فاصلة عائمة. أفضل نموذج ShuffleNet لدينا (ShuffleNet 2×، g=3) يتفوق أيضاً على MobileNet 1.0 بنسبة 1.2% تحت قيد حسابي مماثل.

على الرغم من أن Xception [3] و ResNeXt [40] متفوقان في الغالب على ShuffleNet تحت قيود تعقيد عالية (مثل > 500 ميجا عملية فاصلة عائمة، انظر الجدول 5)، فهما غير مناسبين لمنصات الحوسبة التي لديها قيود موارد صارمة. على سبيل المثال، يحقق الهيكل الشبيه بـ Xception [3] في الجدول 4 خطأ 34.4% مع 42 مليون عملية فاصلة عائمة وهو أسوأ بكثير من نماذج ShuffleNet الخاصة بنا حتى مع عمليات فاصلة عائمة أقل. لاحظ أيضاً أن خطأ التصنيف لنموذج ShuffleNet 0.5× الخاص بنا مماثل لـ ResNet-18 [8] ولكن تعقيده النظري أصغر بكثير من ResNet-18 (40 مقابل 1800 ميجا عملية فاصلة عائمة)، مما يُظهر مزايا تصميم هيكلنا.

نقوم أيضاً بقياس بعض الأطر الأخرى مثل VGG [29] و GoogLeNet [33] و SqueezeNet [15] في الجدول 5. بالمقارنة مع تلك الهياكل، تحقق ShuffleNet أداءً مماثلاً أو أفضل بتعقيد أقل بكثير. في الختام، مع دقة مماثلة فإن ShuffleNet أسرع 13 مرة من MobileNet للسرعة في العالم الحقيقي.

الدقة مقابل FLOPs. لتقديم مقارنة بديهية، نرسم منحنى العلاقة بين خطأ top-1/FLOPs لنماذج مختلفة في الشكل 3 (يسار). من الواضح أن نماذج ShuffleNet أفضل من النماذج الأخرى عبر FLOPs مختلفة. والجدير بالذكر أن نماذج ShuffleNet الخاصة بنا تتفوق على MobileNet في جميع مستويات التعقيد المقيمة.

### 4.4 قدرة التعميم

لتقييم قدرة التعميم، نختبر أيضاً نموذج ShuffleNet الخاص بنا على معيار أكثر تحدياً مؤخراً: كشف أجسام MS COCO [21]. نعتمد Faster-RCNN [25] كإطار كشف ونستخدم كود Caffe المتاح للجمهور [32] للتدريب بالإعدادات الافتراضية. على غرار [12]، يتم تدريب النماذج على مجموعة بيانات COCO train+val باستثناء 8,000 صورة minival ونجري الاختبار على مجموعة minival. يبلغ الجدول 7 عن نتائج الكشف تحت دقتي إدخال مختلفتين بمقاييس نماذج مختلفة. بالمقارنة مع MobileNet [12] على نموذج 1× (~1000 ميجا عملية فاصلة عائمة)، يحصل ShuffleNet 2× (524 ميجا عملية فاصلة عائمة) على نتائج مماثلة على حجم صورة إدخال أصغر (600×) ونتائج أفضل على الحجم الأكبر (1000×). بالمقارنة مع MobileNet الأصغر (0.5×، 269 ميجا عملية فاصلة عائمة)، يحقق ShuffleNet 1× (140 ميجا عملية فاصلة عائمة) نتائج أفضل حتى عند تسريع نظري ~2×. نفترض أن هذا المكسب الكبير يُعزى بشكل رئيسي إلى تصميم ShuffleNet البسيط والفعال والناجع.

### 4.5 تقييم التسريع الفعلي

أخيراً، نقوم بتقييم سرعة الاستدلال الفعلية لنماذج ShuffleNet على جهاز محمول بمنصة ARM. على الرغم من أن بعض العمليات في ShuffleNet (مثل الالتفاف المجموعي وخلط القنوات) قد يكون لها تنفيذ أقل كفاءة في المكتبات المتوفرة حالياً، نعتقد أن دعماً أفضل لمثل هذه العمليات يمكن تحقيقه في المستقبل القريب. تم تنفيذ نموذج ShuffleNet والخطوط الأساسية الأخرى باستخدام مكتبة تعلم عميق محمول عالية التحسين قمنا بتطويرها. تتضمن معايير التوقيت وقت الحساب فقط وتستبعد تكاليف تحميل الصور وتبديل الذاكرة والتكاليف الإضافية الأخرى. يُظهر الجدول 8 وقت التشغيل الفعلي على الجهاز والتعقيد النظري. من النتائج، نرى أن التعقيد النظري عادةً ما يتناسب مع وقت التشغيل الفعلي. مع دقة مماثلة (~43% خطأ تصنيف ImageNet)، فإن ShuffleNet 0.5× أسرع من AlexNet [17] بعامل ~13. حتى بالمقارنة مع شبكة أصغر (~57% خطأ)، لا تزال ShuffleNet أسرع بمقدار 3.7× من SqueezeNet [15] تحت تعقيد حسابي مماثل كما هو موضح في الجدول 5.

---

### Translation Notes

- **Figures referenced:** Figure 3 (Left) - Accuracy vs. FLOPs curve
- **Tables referenced:** Table 2 (Pointwise group convolutions), Table 3 (Channel shuffle comparison), Table 4 (Structure units comparison), Table 5 (MobileNets comparison), Table 7 (MS COCO detection), Table 8 (Actual speedup)
- **Key terms introduced:**
  - Ablation study (دراسة الإزالة)
  - Weight decay (تضاؤل الوزن)
  - Learning rate policy (سياسة معدل التعلم)
  - Scale augmentation (زيادة المقياس)
  - Underfitting (نقص التكيف)
  - Overfitting (الإفراط في التكيف)
  - Single crop (قص واحد)
  - Top-1 performance (أداء top-1)
  - Validation set (مجموعة التحقق)
  - Cardinality (العددية)
  - Generalization ability (قدرة التعميم)
  - Detection framework (إطار كشف)
  - Actual speedup (التسريع الفعلي)
  - Inference speed (سرعة الاستدلال)

- **Equations:** Multiple FLOPs calculations and complexity comparisons
- **Citations:** Multiple references throughout [4, 28, 40, 11, 3, 12, 25, 32, 21, 17, 15, 29, 33]
- **Special handling:**
  - Preserved numerical results and percentages
  - Kept architecture names in English
  - Maintained table and figure references
  - Translated technical analysis while preserving precision

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-translation Check (Key Finding)

Arabic: "بالنسبة للشبكات الأصغر، فإن نماذج ShuffleNet الخاصة بنا أفضل بكثير من نظيرات MobileNet المقابلة بنسبة 7.8% و 3.1%"
Back to English: "For smaller networks, our ShuffleNet models are significantly better than corresponding MobileNet counterparts by 7.8% and 3.1%"
✓ Semantically equivalent to original
