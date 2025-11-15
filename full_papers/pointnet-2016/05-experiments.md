# Section 5: Experiments
## القسم 5: التجارب

**Section:** experiments
**Translation Quality:** 0.87
**Glossary Terms Used:** classification, segmentation, semantic, point cloud, benchmark, accuracy, IoU (Intersection over Union), dataset, baseline, robustness, ablation study

---

### English Version

## 5.1 Applications

**3D Object Classification**

Our network learns global point cloud features that can be used for object classification. We evaluate our model on the ModelNet40 [28] shape classification benchmark. There are 12,311 CAD models from 40 man-made object categories, split into 9,843 for training and 2,468 for testing. While previous methods focus on volumetric and multi-view image representations, we are the first to directly work on raw point clouds.

We uniformly sample 1024 points on mesh faces according to face area and normalize them into a unit sphere. During training we augment the point cloud on-the-fly by randomly rotating the object along the up-axis and jittering the position of each point by a Gaussian noise with zero mean and 0.02 standard deviation.

In Table 1 we compare with previous works as well as our baselines using traditional features [12, 22, 11, 27] on SVM. While achieving similar performance with a few hand-crafted feature combinations, we can learn a more robust feature (last row of Table 1). Compared with deep learning on multi-view representation [18, 23, 11, 21], we achieve comparable performance with 2D CNNs (90.7% in [23] and 91.4% in [11]) using the first version of our network. However, with a more optimized network structure, PointNet now performs on par with the state-of-the-art method MVCNN (95% from [23]), but with much reduced computation time (141x faster than MVCNN at test time) and much cleaner network structure.

We also convert point clouds to 3D voxel grids and use volumetric CNNs (Subvolume [17] and 3D CNN [28]). It is clear from the results that our method achieves much better performance.

**3D Object Part Segmentation**

Part segmentation is a challenging fine-grained 3D recognition task. Given a 3D scan or a mesh model, the task is to assign a part category label (e.g. chair leg, cup handle) to each point or face.

We evaluate on the ShapeNet part dataset from [29], which contains 16,881 shapes from 16 categories, annotated with 50 parts in total. Most object categories are labeled with two to five parts. Ground truth annotations are labeled on sampled points on the shapes.

We formulate part segmentation as a per-point classification problem. Evaluation metric is mIoU on points. For each shape S in category C, to calculate the IoU for a part type P, we compute: IoU_P^C = TP / (TP + FP + FN), where TP, FP, and FN are computed globally across all instances of category C. We then average IoUs for all part types to get the mIoU for that category. To calculate mIoU for all categories, we take the average of mIoUs for each category weighted by the number of shapes in that category.

In Table 2, we compare our method with two traditional methods [12, 27] and a 3D fully convolutional network baseline [3]. We compute IoUs by averaging across all instances per category. Our model can match or exceed the performance of these baselines for most categories.

Figure 4 shows qualitative results. We are able to produce smooth segmentations for the majority of examples, although there are also failure cases, as shown in the last column.

**Semantic Segmentation in Scenes**

Our network on semantic scene labeling has the same architecture as for part segmentation. The input and output are both N × 9 tensors where N is the number of points. For each input point, the nine input features are the XYZ position, RGB color, and the normalized location within the room (from 0 to 1).

We test our model on the Stanford 3D semantic parsing dataset [1]. The dataset contains 3D scans from Matterport scanners in 6 areas including 271 rooms. Each point in the scan is annotated with one of the semantic labels from 13 categories (chair, table, floor, wall etc. plus clutter).

To prepare the training data, we firstly split rooms into blocks of area 1m by 1m. We train our segmentation model on these blocks of points. Each block contains on average 2000 points. During training, we randomly sample rooms for training blocks. In testing, all rooms in Area 5 are used for evaluation.

We compare to a baseline algorithm based on hand-crafted point features (3DCNN [8]). We present results in Table 3 and qualitative results in Figure 6. Although we trained on rooms split into small blocks, the test is on whole rooms (all blocks). We average IoU on all the 13 categories to get the mIoU. PointNet achieves 47.71% overall accuracy, which outperforms the baseline by a large margin (20.12% baseline).

Most of the classes are classified correctly, and the network is able to learn contextual information. For example, in the lower left of Figure 6, even though the table object is missing in the middle, the network is able to detect the shape. Our network also performs well at identifying objects in cluttered scenes. For example, in the bottom row second from right, the chairs can be correctly segmented though the scene is very crowded with 2 chairs, 1 table, and several boards.

## 5.2 Architecture Design Analysis

In this section we validate our design choices by control experiments and visualizations.

**Comparison with Alternative Order-Invariant Methods**

As discussed in Sec 4.2, there are at least three options to achieve order invariance when consuming point sets. We tried implementations of three approaches:

1. Sort points into a canonical order
2. Treat the point cloud as a sequence and train with sequence model (RNN)
3. Use a symmetric function to aggregate information from each point (our method)

To see the effect fairly, all networks have the same architecture comprising five hidden layers with neuron numbers 64, 64, 64, 128, 1024, all points share the same set of weights, and all other training configurations are the same.

From Fig 5, we can see that though the sorting approach improves over the baseline where no input transform is used, it still performs much worse than our method. Since sorting in high dimensions is in general not a bijection, the ordering can be easily disrupted when points undergo transformation, thus the network fails to learn a consistent mapping.

The RNN method works worse than sorting, possibly due to the long point set sequence is harder to learn. The sorted RNN method improves upon plain RNN but is still much worse than our max pooling method.

**Effectiveness of Input and Feature Transformations**

In Table 4 we demonstrate the positive effects of our input and feature transformation networks. The interesting observation here is that the most basic architecture already achieves quite reasonable results. Using input transform improves the performance by 0.8%. The regularized version of feature transform gives another boost in performance.

**Robustness Test**

We show that our learned representation by PointNet is robust to various kinds of input corruptions. We use the same network trained for object classification on ModelNet40 and test how it performs on inputs with point perturbations or missing parts.

In Fig 7 we show the results. As point density decreases, the classification accuracy decreases slowly. Compared with multi-view-based method [23] (87.3% from 98.4%, a 11.1% drop, with the same number of input points) and volumetric CNN based method VoxNet [17] (68% from 83%, a 15% drop, with voxel resolution reduced from 30 to 12), our method demonstrates much stronger robustness, degrading to 87% accuracy from 89.2% (2.2% drop) when we drop from 1024 points to 512 points (about 50% loss).

Similarly, when we randomly remove points, PointNet also performs the best. We show the results when removing furthest points and closest points to the origin. The conclusion is consistent. Interestingly, removing points close to the origin appears to have little effect on the network output. This suggests that the network learns to summarize a shape using a sparse set of key points. The visualization in the supplementary also supports this (see Fig 11 of the supplementary).

## 5.3 Visualizing PointNet

In Fig 8 we give intuition for what the network learns by visualizing the critical points and upper-bound shapes for some units (neurons) of the max pooling layer.

For visualizing the critical points (defined in Sec 4.3), we input shapes from the test set and collect the critical points that contribute to the max pooling feature. Intuitively, the critical points form a skeleton of the input object. They distribute on different parts of the object (e.g., on chair legs and seats for a chair) and summarize the shape of the object. Fig 8 (c) shows all critical points collected from the test set on chairs. We can clearly see characteristic points like the chair legs, armrests, and back support.

Another way to understand the expressiveness is to study what is the upper-bound shape for each function (neuron). Intuitively, the sub-network after max pooling can distinguish different shapes. So there exists a tightest shape (or critical point set) that leads to maximum activation of a specific neuron. This shape is the upper-bound shape of the neuron. In Fig 8 (b) we show the 3D models whose point sets activate the neuron the most. We can see that the neuron gets maximally activated by a plane.

---

### النسخة العربية

## 5.1 التطبيقات

**تصنيف الكائنات ثلاثية الأبعاد**

تتعلم شبكتنا خصائص سحابة النقاط العامة التي يمكن استخدامها لتصنيف الكائنات. نقيّم نموذجنا على معيار تصنيف الأشكال ModelNet40 [28]. هناك 12,311 نموذج CAD من 40 فئة من الكائنات من صنع الإنسان، مقسمة إلى 9,843 للتدريب و 2,468 للاختبار. بينما تركز الأساليب السابقة على التمثيلات الحجمية وصور متعددة المناظر، نحن الأوائل في العمل مباشرة على سحب النقاط الخام.

نأخذ عينات بشكل موحد من 1024 نقطة على وجوه الشبكة وفقاً لمساحة الوجه ونطبعها في كرة وحدة. أثناء التدريب، نعزز سحابة النقاط على الفور عن طريق تدوير الكائن عشوائياً على طول المحور العمودي واهتزاز موضع كل نقطة بضوضاء غاوسية بمتوسط صفر وانحراف معياري 0.02.

في الجدول 1 نقارن مع الأعمال السابقة بالإضافة إلى خطوط الأساس الخاصة بنا باستخدام الخصائص التقليدية [12, 22, 11, 27] على SVM. بينما نحقق أداءً مماثلاً مع عدد قليل من تركيبات الخصائص المصممة يدوياً، يمكننا تعلم خاصية أكثر قوة (الصف الأخير من الجدول 1). مقارنة بالتعلم العميق على تمثيل متعدد المناظر [18, 23, 11, 21]، نحقق أداءً مماثلاً للشبكات العصبية التلافيفية ثنائية الأبعاد (90.7% في [23] و 91.4% في [11]) باستخدام الإصدار الأول من شبكتنا. ومع ذلك، مع بنية شبكة أكثر تحسيناً، يؤدي PointNet الآن على قدم المساواة مع طريقة أحدث النتائج MVCNN (95% من [23])، ولكن مع وقت حساب أقل بكثير (أسرع 141 مرة من MVCNN في وقت الاختبار) وبنية شبكة أنظف بكثير.

نحوّل أيضاً سحب النقاط إلى شبكات فوكسل ثلاثية الأبعاد ونستخدم الشبكات العصبية التلافيفية الحجمية (Subvolume [17] و 3D CNN [28]). من الواضح من النتائج أن طريقتنا تحقق أداءً أفضل بكثير.

**تجزئة أجزاء الكائنات ثلاثية الأبعاد**

تجزئة الأجزاء هي مهمة تعرف ثلاثي الأبعاد دقيق ومُصنف ضمن الحبيبات الدقيقة. بالنظر إلى مسح ثلاثي الأبعاد أو نموذج شبكة، المهمة هي تعيين تصنيف فئة الجزء (على سبيل المثال، ساق الكرسي، مقبض الكوب) لكل نقطة أو وجه.

نقيّم على مجموعة بيانات أجزاء ShapeNet من [29]، والتي تحتوي على 16,881 شكلاً من 16 فئة، مشروحة بـ 50 جزءاً في المجموع. معظم فئات الكائنات مُصنَّفة بجزأين إلى خمسة أجزاء. يتم وضع تعليقات توضيحية للحقيقة الأرضية على نقاط معينة على الأشكال.

نصيغ تجزئة الأجزاء كمشكلة تصنيف لكل نقطة. مقياس التقييم هو mIoU على النقاط. لكل شكل S في الفئة C، لحساب IoU لنوع الجزء P، نحسب: IoU_P^C = TP / (TP + FP + FN)، حيث TP و FP و FN محسوبة عالمياً عبر جميع نماذج الفئة C. ثم نحسب متوسط IoUs لجميع أنواع الأجزاء للحصول على mIoU لتلك الفئة. لحساب mIoU لجميع الفئات، نأخذ متوسط mIoUs لكل فئة موزونة بعدد الأشكال في تلك الفئة.

في الجدول 2، نقارن طريقتنا مع طريقتين تقليديتين [12, 27] وخط أساس للشبكة التلافيفية الكاملة ثلاثية الأبعاد [3]. نحسب IoUs عن طريق حساب المتوسط عبر جميع النماذج لكل فئة. يمكن لنموذجنا مطابقة أو تجاوز أداء خطوط الأساس هذه لمعظم الفئات.

يُظهر الشكل 4 نتائج نوعية. نحن قادرون على إنتاج تجزئات سلسة لمعظم الأمثلة، على الرغم من وجود حالات فشل أيضاً، كما هو موضح في العمود الأخير.

**التجزئة الدلالية في المشاهد**

شبكتنا على وضع التصنيفات الدلالية للمشاهد لها نفس المعمارية كما هو الحال لتجزئة الأجزاء. المدخل والمخرج كلاهما موترات N × 9 حيث N هو عدد النقاط. لكل نقطة مدخلة، الخصائص التسع المدخلة هي موضع XYZ، لون RGB، والموقع المطبع داخل الغرفة (من 0 إلى 1).

نختبر نموذجنا على مجموعة بيانات تحليل دلالات Stanford ثلاثية الأبعاد [1]. تحتوي مجموعة البيانات على مسوحات ثلاثية الأبعاد من ماسحات Matterport في 6 مناطق تشمل 271 غرفة. كل نقطة في المسح مُشروحة بأحد التصنيفات الدلالية من 13 فئة (كرسي، طاولة، أرضية، جدار إلخ. بالإضافة إلى الفوضى).

لإعداد بيانات التدريب، نقسم أولاً الغرف إلى كتل بمساحة 1 متر × 1 متر. نقوم بتدريب نموذج التجزئة الخاص بنا على هذه الكتل من النقاط. تحتوي كل كتلة على متوسط 2000 نقطة. أثناء التدريب، نأخذ عينات عشوائياً من الغرف لكتل التدريب. في الاختبار، تُستخدم جميع الغرف في المنطقة 5 للتقييم.

نقارن مع خوارزمية خط أساس بناءً على خصائص النقاط المصممة يدوياً (3DCNN [8]). نقدم النتائج في الجدول 3 والنتائج النوعية في الشكل 6. على الرغم من أننا دربنا على غرف مقسمة إلى كتل صغيرة، فإن الاختبار على غرف كاملة (جميع الكتل). نحسب متوسط IoU على جميع الفئات الـ 13 للحصول على mIoU. يحقق PointNet دقة إجمالية 47.71%، متفوقاً على خط الأساس بهامش كبير (خط الأساس 20.12%).

معظم الفئات مُصنَّفة بشكل صحيح، والشبكة قادرة على تعلم المعلومات السياقية. على سبيل المثال، في الجزء السفلي الأيسر من الشكل 6، على الرغم من أن كائن الطاولة مفقود في المنتصف، فإن الشبكة قادرة على اكتشاف الشكل. تؤدي شبكتنا أيضاً بشكل جيد في تحديد الكائنات في المشاهد المزدحمة. على سبيل المثال، في الصف السفلي الثاني من اليمين، يمكن تجزئة الكراسي بشكل صحيح على الرغم من أن المشهد مزدحم جداً بـ 2 كراسي، 1 طاولة، والعديد من الألواح.

## 5.2 تحليل تصميم المعمارية

في هذا القسم نتحقق من صحة خيارات التصميم الخاصة بنا من خلال تجارب التحكم والتصورات.

**المقارنة مع الأساليب البديلة الثابتة تحت الترتيب**

كما نوقش في القسم 4.2، هناك ثلاث خيارات على الأقل لتحقيق الثبات تحت الترتيب عند استهلاك مجموعات النقاط. حاولنا تطبيقات ثلاثة نُهج:

1. ترتيب النقاط في ترتيب قانوني
2. معاملة سحابة النقاط كتسلسل والتدريب مع نموذج تسلسل (RNN)
3. استخدام دالة متماثلة لتجميع المعلومات من كل نقطة (طريقتنا)

لرؤية التأثير بشكل عادل، جميع الشبكات لها نفس المعمارية تتكون من خمس طبقات مخفية بأعداد عصبونات 64، 64، 64، 128، 1024، جميع النقاط تشترك في نفس مجموعة الأوزان، وجميع تكوينات التدريب الأخرى هي نفسها.

من الشكل 5، يمكننا أن نرى أنه على الرغم من أن نهج الترتيب يحسّن على خط الأساس حيث لا يُستخدم تحويل مدخل، إلا أنه لا يزال يؤدي بشكل أسوأ بكثير من طريقتنا. نظراً لأن الترتيب في الأبعاد العالية ليس بشكل عام تقابلاً، يمكن تعطيل الترتيب بسهولة عندما تخضع النقاط للتحويل، وبالتالي تفشل الشبكة في تعلم تعيين متسق.

طريقة RNN تعمل أسوأ من الترتيب، ربما بسبب أن تسلسل مجموعة النقاط الطويلة أصعب في التعلم. طريقة RNN المرتبة تتحسن على RNN العادي لكنها لا تزال أسوأ بكثير من طريقة التجميع الأقصى لدينا.

**فعالية تحويلات المدخلات والخصائص**

في الجدول 4 نوضح التأثيرات الإيجابية لشبكات تحويل المدخلات والخصائص الخاصة بنا. الملاحظة المثيرة للاهتمام هنا هي أن المعمارية الأساسية الأكثر تحقق بالفعل نتائج معقولة تماماً. استخدام تحويل المدخل يحسّن الأداء بنسبة 0.8%. الإصدار المنظم من تحويل الخصائص يعطي دفعة أخرى في الأداء.

**اختبار القوة**

نُظهر أن تمثيلنا المُتعلَّم بواسطة PointNet قوي تجاه أنواع مختلفة من أضرار المدخلات. نستخدم نفس الشبكة المدربة لتصنيف الكائنات على ModelNet40 ونختبر كيف تؤدي على المدخلات مع اضطرابات النقاط أو الأجزاء المفقودة.

في الشكل 7 نُظهر النتائج. مع انخفاض كثافة النقاط، تنخفض دقة التصنيف ببطء. مقارنة بالطريقة القائمة على المناظر المتعددة [23] (87.3% من 98.4%، انخفاض 11.1%، مع نفس عدد نقاط المدخل) والطريقة القائمة على الشبكة العصبية التلافيفية الحجمية VoxNet [17] (68% من 83%، انخفاض 15%، مع تقليل دقة الفوكسل من 30 إلى 12)، تُظهر طريقتنا قوة أقوى بكثير، تنخفض إلى دقة 87% من 89.2% (انخفاض 2.2%) عندما ننخفض من 1024 نقطة إلى 512 نقطة (حوالي 50% فقدان).

بالمثل، عندما نزيل النقاط عشوائياً، يؤدي PointNet أيضاً بشكل أفضل. نُظهر النتائج عند إزالة النقاط الأبعد والنقاط الأقرب إلى الأصل. الاستنتاج متسق. من المثير للاهتمام، أن إزالة النقاط القريبة من الأصل يبدو أن لها تأثير ضئيل على مخرج الشبكة. هذا يشير إلى أن الشبكة تتعلم تلخيص شكل باستخدام مجموعة متفرقة من النقاط الرئيسية. التصور في الملحق يدعم هذا أيضاً (انظر الشكل 11 من الملحق).

## 5.3 تصور PointNet

في الشكل 8 نعطي حدساً لما تتعلمه الشبكة من خلال تصور النقاط الحرجة والأشكال ذات الحد الأعلى لبعض الوحدات (العصبونات) من طبقة التجميع الأقصى.

لتصور النقاط الحرجة (المعرفة في القسم 4.3)، نُدخل أشكالاً من مجموعة الاختبار ونجمع النقاط الحرجة التي تساهم في خاصية التجميع الأقصى. بديهياً، النقاط الحرجة تشكل هيكلاً عظمياً للكائن المدخل. تتوزع على أجزاء مختلفة من الكائن (على سبيل المثال، على أرجل الكرسي والمقاعد للكرسي) وتلخص شكل الكائن. يُظهر الشكل 8 (c) جميع النقاط الحرجة المجمعة من مجموعة الاختبار على الكراسي. يمكننا أن نرى بوضوح النقاط المميزة مثل أرجل الكرسي، ومساند الذراعين، ودعم الظهر.

طريقة أخرى لفهم قوة التعبير هي دراسة ما هو الشكل ذو الحد الأعلى لكل دالة (عصبون). بديهياً، الشبكة الفرعية بعد التجميع الأقصى يمكن أن تميز أشكالاً مختلفة. لذلك يوجد شكل أكثر إحكاماً (أو مجموعة نقاط حرجة) يؤدي إلى أقصى تفعيل لعصبون محدد. هذا الشكل هو الشكل ذو الحد الأعلى للعصبون. في الشكل 8 (b) نُظهر نماذج ثلاثية الأبعاد مجموعات نقاطها تُفعِّل العصبون بشكل أكبر. يمكننا أن نرى أن العصبون يتم تفعيله بشكل أقصى بواسطة مستوى.

---

### Translation Notes

- **Figures referenced:** Figure 4 (Segmentation results), Figure 5 (Method comparison), Figure 6 (Scene segmentation), Figure 7 (Robustness test), Figure 8 (Visualization)
- **Key terms introduced:**
  - ModelNet40 - ModelNet40 (اسم مجموعة بيانات)
  - ShapeNet - ShapeNet (اسم مجموعة بيانات)
  - mIoU (mean Intersection over Union) - mIoU (متوسط تقاطع على اتحاد)
  - CAD models - نماذج CAD
  - Ground truth - الحقيقة الأرضية
  - Fine-grained recognition - التعرف ضمن الحبيبات الدقيقة
  - On-the-fly augmentation - التعزيز على الفور
  - Jittering - الاهتزاز
  - Critical points - النقاط الحرجة
  - Upper-bound shape - الشكل ذو الحد الأعلى
  - Ablation study - دراسة الإزالة

- **Equations:**
  - IoU formula: IoU_P^C = TP / (TP + FP + FN)
  - Gaussian noise parameters: zero mean, 0.02 standard deviation

- **Citations:** Multiple references to datasets and baseline methods [1-29]
- **Special handling:**
  - Maintained table references (Table 1, 2, 3, 4)
  - Kept dataset names in English (ModelNet40, ShapeNet, Stanford 3D)
  - Preserved numerical results and percentages exactly
  - Translated experimental protocols and methodologies accurately
  - Used formal academic Arabic throughout

### Quality Metrics

- **Semantic equivalence:** 0.88 - Accurately captures experimental setup and results
- **Technical accuracy:** 0.87 - All technical terms and metrics correctly translated
- **Readability:** 0.86 - Natural flow while maintaining technical precision
- **Glossary consistency:** 0.88 - Consistent terminology usage

**Overall section score:** 0.87

### Back-Translation (3D Object Classification - first paragraph)

Our network learns global point cloud features that can be used for object classification. We evaluate our model on the ModelNet40 [28] shape classification benchmark. There are 12,311 CAD models from 40 human-made object categories, divided into 9,843 for training and 2,468 for testing. While previous methods focus on volumetric and multi-view image representations, we are the first to work directly on raw point clouds.

### Back-Translation (Robustness Test - excerpt)

As point density decreases, classification accuracy decreases slowly. Compared with the multi-view-based method [23] (87.3% from 98.4%, an 11.1% drop, with the same number of input points) and the volumetric CNN-based method VoxNet [17] (68% from 83%, a 15% drop, with voxel resolution reduced from 30 to 12), our method demonstrates much stronger robustness, degrading to 87% accuracy from 89.2% (2.2% drop) when we drop from 1024 points to 512 points (about 50% loss).
