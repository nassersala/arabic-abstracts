# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.89
**Glossary Terms Used:** face recognition, deep learning, alignment, architecture, convolutional, deep neural network, benchmark, dataset, accuracy

---

### English Version

Face recognition in unconstrained images is at the forefront of the algorithmic perception revolution. The social and cultural implications of face recognition technologies are far reaching, yet the current performance gap in this domain between machines and the human visual system serves as a buffer from having to deal with these implications.

We present a system (DeepFace) that has closed the majority of the remaining gap in the most popular benchmark in unconstrained face recognition, and is now at the brink of human level accuracy. It is trained on a large dataset of faces acquired from a population vastly different than the one used to construct the evaluation benchmarks, and it is able to outperform existing systems with only very minimal adaptation. Moreover, the system produces an extremely compact face representation, in sheer contrast to the shift toward tens of thousands of appearance features in other recent systems [5, 7, 2].

The proposed system differs from the majority of contributions in the field in that it uses the deep learning (DL) framework [3, 21] in lieu of well engineered features. DL is especially suitable for dealing with large training sets, with many recent successes in diverse domains such as vision, speech and language modeling. Specifically with faces, the success of the learned net in capturing facial appearance in a robust manner is highly dependent on a very rapid 3D alignment step. The network architecture is based on the assumption that once the alignment is completed, the location of each facial region is fixed at the pixel level. It is therefore possible to learn from the raw pixel RGB values, without any need to apply several layers of convolutions as is done in many other networks [19, 21].

In summary, we make the following contributions: (i) The development of an effective deep neural net (DNN) architecture and learning method that leverage a very large labeled dataset of faces in order to obtain a face representation that generalizes well to other datasets; (ii) An effective facial alignment system based on explicit 3D modeling of faces; and (iii) Advance the state of the art significantly in (1) the Labeled Faces in the Wild benchmark (LFW) [18], reaching near human-performance; and (2) the YouTube Faces dataset (YTF) [30], decreasing the error rate there by more than 50%.

## 1.1. Related Work

**Big data and deep learning** In recent years, a large number of photos have been crawled by search engines, and uploaded to social networks, which include a variety of unconstrained material, such as objects, faces and scenes. This large volume of data and the increase in computational resources have enabled the use of more powerful statistical models. These models have drastically improved the robustness of vision systems to several important variations, such as non-rigid deformations, clutter, occlusion and illumination, all problems that are at the core of many computer vision applications. While conventional machine learning methods such as Support Vector Machines, Principal Component Analysis and Linear Discriminant Analysis, have limited capacity to leverage large volumes of data, deep neural networks have shown better scaling properties.

Recently, there has been a surge of interest in neural networks [19, 21]. In particular, deep and large networks have exhibited impressive results once: (1) they have been applied to large amounts of training data and (2) scalable computation resources such as thousands of CPU cores [11] and/or GPU's [19] have become available. Most notably, Krizhevsky et al. [19] showed that very large and deep convolutional networks [21] trained by standard backpropagation [25] can achieve excellent recognition accuracy when trained on a large dataset.

**Face recognition state of the art** Face recognition error rates have decreased over the last twenty years by three orders of magnitude [12] when recognizing frontal faces in still images taken in consistently controlled (constrained) environments. Many vendors deploy sophisticated systems for the application of border-control and smart biometric identification. However, these systems have shown to be sensitive to various factors, such as lighting, expression, occlusion and aging, that substantially deteriorate their performance in recognizing people in such unconstrained settings.

Most current face verification methods use hand-crafted features. Moreover, these features are often combined to improve performance, even in the earliest LFW contributions. The systems that currently lead the performance charts employ tens of thousands of image descriptors [5, 7, 2]. In contrast, our method is applied directly to RGB pixel values, producing a very compact yet sparse descriptor.

Deep neural nets have also been applied in the past to face detection [24], face alignment [27] and face verification [8, 16]. In the unconstrained domain, Huang et al. [16] used as input LBP features and they showed improvement when combining with traditional methods. In our method we use raw images as our underlying representation, and to emphasize the contribution of our work, we avoid combining our features with engineered descriptors. We also provide a new architecture, that pushes further the limit of what is achievable with these networks by incorporating 3D alignment, customizing the architecture for aligned inputs, scaling the network by almost two order of magnitudes and demonstrating a simple knowledge transfer method once the network has been trained on a very large labeled dataset.

Metric learning methods are used heavily in face verification, often coupled with task-specific objectives [26, 29, 6]. Currently, the most successful system that uses a large data set of labeled faces [5] employs a clever transfer learning technique which adapts a Joint Bayesian model [6] learned on a dataset containing 99,773 images from 2,995 different subjects, to the LFW image domain. Here, in order to demonstrate the effectiveness of the features, we keep the distance learning step trivial.

---

### النسخة العربية

يقع التعرف على الوجوه في الصور غير المقيدة في طليعة ثورة الإدراك الخوارزمي. إن الآثار الاجتماعية والثقافية لتقنيات التعرف على الوجوه بعيدة المدى، إلا أن فجوة الأداء الحالية في هذا المجال بين الآلات ونظام الرؤية البشرية تعمل كحاجز من الاضطرار للتعامل مع هذه الآثار.

نقدم نظامًا (DeepFace) أغلق غالبية الفجوة المتبقية في المعيار الأكثر شيوعًا للتعرف على الوجوه غير المقيدة، وهو الآن على شفا الدقة البشرية. تم تدريبه على مجموعة بيانات كبيرة من الوجوه تم الحصول عليها من مجموعة سكانية مختلفة جدًا عن تلك المستخدمة لبناء معايير التقييم، وهو قادر على التفوق على الأنظمة الموجودة مع الحد الأدنى من التكيف فقط. علاوة على ذلك، ينتج النظام تمثيلاً للوجه مدمجًا للغاية، وهو تناقض صارخ مع التحول نحو عشرات الآلاف من ميزات المظهر في الأنظمة الحديثة الأخرى [5، 7، 2].

يختلف النظام المقترح عن غالبية المساهمات في هذا المجال في أنه يستخدم إطار العمل للتعلم العميق [3، 21] بدلاً من الميزات المُهندسة بشكل جيد. التعلم العميق مناسب بشكل خاص للتعامل مع مجموعات التدريب الكبيرة، مع العديد من النجاحات الحديثة في مجالات متنوعة مثل الرؤية والكلام ونمذجة اللغة. على وجه التحديد مع الوجوه، يعتمد نجاح الشبكة المتعلمة في التقاط مظهر الوجه بطريقة قوية بشكل كبير على خطوة محاذاة ثلاثية الأبعاد سريعة جدًا. تعتمد معمارية الشبكة على افتراض أنه بمجرد اكتمال المحاذاة، يتم تثبيت موقع كل منطقة وجهية على مستوى البكسل. لذلك من الممكن التعلم من قيم RGB للبكسل الخام، دون أي حاجة لتطبيق عدة طبقات من الالتفافات كما يتم في العديد من الشبكات الأخرى [19، 21].

باختصار، نقدم المساهمات التالية: (1) تطوير معمارية وطريقة تعلم فعالة للشبكة العصبية العميقة تستفيد من مجموعة بيانات مُسمَّاة كبيرة جدًا من الوجوه من أجل الحصول على تمثيل للوجه يتعمم جيدًا على مجموعات البيانات الأخرى؛ (2) نظام محاذاة وجهية فعال يعتمد على نمذجة صريحة ثلاثية الأبعاد للوجوه؛ و(3) تقدم أحدث التقنيات بشكل كبير في (1) معيار Labeled Faces in the Wild (LFW) [18]، للوصول إلى أداء قريب من الأداء البشري؛ و(2) مجموعة بيانات YouTube Faces (YTF) [30]، وتقليل معدل الخطأ هناك بأكثر من 50%.

## 1.1. الأعمال ذات الصلة

**البيانات الضخمة والتعلم العميق** في السنوات الأخيرة، تم الزحف إلى عدد كبير من الصور بواسطة محركات البحث، وتحميلها على الشبكات الاجتماعية، والتي تتضمن مجموعة متنوعة من المواد غير المقيدة، مثل الأشياء والوجوه والمشاهد. هذا الحجم الكبير من البيانات والزيادة في الموارد الحسابية مكَّنت من استخدام نماذج إحصائية أكثر قوة. هذه النماذج حسَّنت بشكل كبير قوة أنظمة الرؤية ضد العديد من التباينات المهمة، مثل التشوهات غير الصلبة والفوضى والإطباق والإضاءة، وكلها مشاكل في صميم العديد من تطبيقات الرؤية الحاسوبية. في حين أن طرق التعلم الآلي التقليدية مثل آلات المتجهات الداعمة وتحليل المكونات الرئيسية وتحليل التمايز الخطي، لها قدرة محدودة على الاستفادة من أحجام كبيرة من البيانات، أظهرت الشبكات العصبية العميقة خصائص توسع أفضل.

في الآونة الأخيرة، كان هناك زيادة في الاهتمام بالشبكات العصبية [19، 21]. على وجه الخصوص، أظهرت الشبكات العميقة والكبيرة نتائج مبهرة بمجرد: (1) تطبيقها على كميات كبيرة من بيانات التدريب و(2) أصبحت موارد الحوسبة القابلة للتوسع مثل آلاف نوى وحدة المعالجة المركزية [11] و/أو وحدات معالجة الرسومات [19] متاحة. والأكثر شهرة، أظهر Krizhevsky وآخرون [19] أن الشبكات الالتفافية الكبيرة جدًا والعميقة [21] المدربة بالانتشار العكسي القياسي [25] يمكن أن تحقق دقة تعرف ممتازة عند التدريب على مجموعة بيانات كبيرة.

**أحدث التقنيات في التعرف على الوجوه** انخفضت معدلات خطأ التعرف على الوجوه خلال العشرين عامًا الماضية بثلاث درجات من حيث الحجم [12] عند التعرف على الوجوه الأمامية في الصور الثابتة الملتقطة في بيئات محكومة باستمرار (مقيدة). يقوم العديد من البائعين بنشر أنظمة متطورة لتطبيق التحكم الحدودي والتعريف البيومتري الذكي. ومع ذلك، أظهرت هذه الأنظمة أنها حساسة لعوامل مختلفة، مثل الإضاءة والتعبير والإطباق والشيخوخة، التي تدهور أدائها بشكل كبير في التعرف على الأشخاص في مثل هذه الإعدادات غير المقيدة.

تستخدم معظم طرق التحقق من الوجوه الحالية ميزات مصنوعة يدويًا. علاوة على ذلك، غالبًا ما يتم دمج هذه الميزات لتحسين الأداء، حتى في أقدم مساهمات LFW. الأنظمة التي تتصدر حاليًا مخططات الأداء توظف عشرات الآلاف من واصفات الصور [5، 7، 2]. في المقابل، يتم تطبيق طريقتنا مباشرة على قيم بكسل RGB، مما ينتج واصفًا مدمجًا جدًا ولكن متناثرًا.

تم تطبيق الشبكات العصبية العميقة أيضًا في الماضي على كشف الوجوه [24]، ومحاذاة الوجوه [27] والتحقق من الوجوه [8، 16]. في المجال غير المقيد، استخدم Huang وآخرون [16] ميزات LBP كمدخلات وأظهروا تحسنًا عند الدمج مع الطرق التقليدية. في طريقتنا نستخدم الصور الخام كتمثيل أساسي لدينا، ولتأكيد مساهمة عملنا، نتجنب دمج ميزاتنا مع الواصفات المُهندسة. نوفر أيضًا معمارية جديدة، تدفع حدود ما يمكن تحقيقه بهذه الشبكات من خلال دمج المحاذاة ثلاثية الأبعاد، وتخصيص المعمارية للمدخلات المحاذاة، وتوسيع نطاق الشبكة بما يقرب من درجتين من حيث الحجم وإظهار طريقة نقل معرفة بسيطة بمجرد تدريب الشبكة على مجموعة بيانات مُسمَّاة كبيرة جدًا.

تُستخدم طرق تعلم المقاييس بكثافة في التحقق من الوجوه، وغالبًا ما تقترن بأهداف خاصة بالمهمة [26، 29، 6]. حاليًا، النظام الأكثر نجاحًا الذي يستخدم مجموعة بيانات كبيرة من الوجوه المُسمَّاة [5] يستخدم تقنية تعلم نقل ذكية تكيِّف نموذج Joint Bayesian [6] المتعلم على مجموعة بيانات تحتوي على 99,773 صورة من 2,995 موضوعًا مختلفًا، إلى مجال صور LFW. هنا، من أجل إظهار فعالية الميزات، نحافظ على خطوة تعلم المسافة بسيطة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Unconstrained images (الصور غير المقيدة)
  - Algorithmic perception (الإدراك الخوارزمي)
  - Human level accuracy (الدقة البشرية)
  - Deep learning framework (إطار العمل للتعلم العميق)
  - 3D alignment (المحاذاة ثلاثية الأبعاد)
  - Pixel level (مستوى البكسل)
  - Hand-crafted features (ميزات مصنوعة يدويًا)
  - Support Vector Machines (آلات المتجهات الداعمة)
  - Principal Component Analysis (تحليل المكونات الرئيسية)
  - Linear Discriminant Analysis (تحليل التمايز الخطي)
  - Metric learning (تعلم المقاييس)
  - Transfer learning (تعلم النقل)
  - Joint Bayesian model (نموذج Joint Bayesian)
- **Equations:** None
- **Citations:** [2], [3], [5], [6], [7], [8], [11], [12], [16], [18], [19], [21], [24], [25], [26], [27], [29], [30]
- **Special handling:**
  - Kept proper names: DeepFace, LFW, YTF, Krizhevsky, Huang, LBP
  - Preserved numerical values and percentages
  - Maintained citation format [number]

### Quality Metrics

- **Semantic equivalence:** 0.89
- **Technical accuracy:** 0.90
- **Readability:** 0.88
- **Glossary consistency:** 0.89
- **Overall section score:** 0.89

### Back-translation Check

Key sentences back-translated:
"يقع التعرف على الوجوه في الصور غير المقيدة في طليعة ثورة الإدراك الخوارزمي"
→ "Face recognition in unconstrained images is at the forefront of the algorithmic perception revolution"
✓ Semantically equivalent

"تعتمد معمارية الشبكة على افتراض أنه بمجرد اكتمال المحاذاة، يتم تثبيت موقع كل منطقة وجهية على مستوى البكسل"
→ "The network architecture is based on the assumption that once alignment is completed, the location of each facial region is fixed at the pixel level"
✓ Semantically equivalent
