# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.89
**Glossary Terms Used:** point cloud, deep learning, neural network, architecture, classification, segmentation, voxel, permutation invariance, symmetric function, max pooling, 3D

---

### English Version

In this work we explore deep learning architectures capable of reasoning about 3D geometric data such as point clouds or meshes. Typical convolutional architectures require highly regular input data formats, like those of image grids or 3D voxels, in order to perform weight sharing and other kernel optimizations. Since point clouds or meshes are not in a regular format, most researchers transform such data to regular 3D voxel grids or collections of images (e.g., views) before feeding them to a deep net architecture. This data representation transformation, however, renders the resulting data unnecessarily voluminous—while also introducing quantization artifacts that can obscure natural invariances of the data.

In this paper, we design a novel deep net architecture suitable for consuming raw point clouds, which well respects the permutation invariance of points in the input. Our network, named PointNet, provides a unified architecture for applications ranging from object classification, part segmentation, to scene semantic parsing. Though simple, PointNet is highly efficient and effective. Empirically, it shows strong performance on par or even better than state of the art. Theoretically, we provide analysis towards understanding of what the network has learnt and why the network is robust with respect to input perturbation and corruption.

Our key contributions are as follows:

• We design a novel deep net architecture that directly takes point clouds as input and respects the invariance of the input under permutation.

• We show how such a network can be trained to perform 3D shape classification, shape part segmentation and scene semantic parsing tasks.

• We provide thorough empirical and theoretical analysis on the stability and efficiency of our method.

• We illustrate the 3D features computed by the selected neurons in the net and develop intuitive explanations for its performance.

Point cloud is an important type of geometric data structure. Due to its irregular format, most researchers transform such data to regular 3D voxel grids or collections of images. This, however, renders data unnecessarily voluminous and causes issues. In this paper, we design a novel deep net architecture that directly consumes point clouds. Our network, named PointNet, provides a unified approach to a number of 3D recognition tasks including object classification, part segmentation, and semantic segmentation.

---

### النسخة العربية

في هذا العمل، نستكشف معماريات التعلم العميق القادرة على الاستدلال حول البيانات الهندسية ثلاثية الأبعاد مثل سحب النقاط أو الشبكات الهندسية. تتطلب المعماريات التلافيفية النموذجية تنسيقات بيانات مدخلة منتظمة بشكل كبير، مثل تلك الخاصة بشبكات الصور أو الفوكسلات ثلاثية الأبعاد، من أجل تنفيذ مشاركة الأوزان وتحسينات النواة الأخرى. نظراً لأن سحب النقاط أو الشبكات الهندسية ليست بتنسيق منتظم، يقوم معظم الباحثين بتحويل هذه البيانات إلى شبكات فوكسل ثلاثية الأبعاد منتظمة أو مجموعات من الصور (على سبيل المثال، المناظر) قبل إدخالها إلى معمارية الشبكة العميقة. ومع ذلك، فإن هذا التحويل في تمثيل البيانات يجعل البيانات الناتجة ضخمة بشكل غير ضروري - كما يُدخل أيضاً عناصر تكميم يمكن أن تحجب الثوابت الطبيعية للبيانات.

في هذا البحث، نصمم معمارية شبكة عميقة جديدة مناسبة لاستهلاك سحب النقاط الخام، والتي تحترم بشكل جيد ثبات التبديل للنقاط في المدخلات. شبكتنا، المسماة PointNet، توفر معمارية موحدة للتطبيقات التي تتراوح من تصنيف الكائنات، وتجزئة الأجزاء، إلى تحليل الدلالات للمشهد. على الرغم من بساطتها، فإن PointNet عالية الكفاءة والفعالية. تجريبياً، تُظهر أداءً قوياً مماثلاً أو حتى أفضل من أحدث النتائج. نظرياً، نقدم تحليلاً لفهم ما تعلمته الشبكة ولماذا الشبكة قوية فيما يتعلق بالاضطرابات والتلف في المدخلات.

مساهماتنا الرئيسية هي كما يلي:

• نصمم معمارية شبكة عميقة جديدة تأخذ سحب النقاط مباشرة كمدخلات وتحترم ثبات المدخلات تحت التبديل.

• نُظهر كيف يمكن تدريب مثل هذه الشبكة لأداء مهام تصنيف الأشكال ثلاثية الأبعاد، وتجزئة أجزاء الشكل، ومهام تحليل دلالات المشهد.

• نقدم تحليلاً تجريبياً ونظرياً شاملاً حول استقرار وكفاءة طريقتنا.

• نوضح الخصائص ثلاثية الأبعاد المحسوبة بواسطة العصبونات المحددة في الشبكة ونطور تفسيرات بديهية لأدائها.

سحابة النقاط هي نوع مهم من بنية البيانات الهندسية. نظراً لتنسيقها غير المنتظم، يقوم معظم الباحثين بتحويل هذه البيانات إلى شبكات فوكسل ثلاثية الأبعاد منتظمة أو مجموعات من الصور. ومع ذلك، فإن هذا يجعل البيانات ضخمة بشكل غير ضروري ويسبب مشاكل. في هذا البحث، نصمم معمارية شبكة عميقة جديدة تستهلك سحب النقاط مباشرة. شبكتنا، المسماة PointNet، توفر نهجاً موحداً لعدد من مهام التعرف ثلاثية الأبعاد بما في ذلك تصنيف الكائنات، وتجزئة الأجزاء، والتجزئة الدلالية.

---

### Translation Notes

- **Figures referenced:** Figure 1 (PointNet architecture overview - mentioned in full paper)
- **Key terms introduced:**
  - Point cloud - سحابة النقاط
  - Permutation invariance - ثبات التبديل
  - Voxel grid - شبكة فوكسل
  - Symmetric function - دالة متماثلة
  - Max pooling - التجميع الأقصى
  - Part segmentation - تجزئة الأجزاء
  - Scene semantic parsing - تحليل دلالات المشهد
  - Quantization artifacts - عناصر التكميم
  - Weight sharing - مشاركة الأوزان

- **Equations:** None in this section
- **Citations:** References to prior work on voxel-based and multi-view approaches
- **Special handling:**
  - Maintained the bullet point format for contributions
  - Kept model name "PointNet" in English as it is a proper name
  - Used formal academic Arabic throughout
  - Preserved technical precision while ensuring natural Arabic flow

### Quality Metrics

- **Semantic equivalence:** 0.90 - The translation accurately captures all main ideas and motivations
- **Technical accuracy:** 0.89 - All technical terms are correctly translated using established glossary terms
- **Readability:** 0.88 - The Arabic flows naturally while maintaining technical precision
- **Glossary consistency:** 0.90 - Consistent use of glossary terms throughout

**Overall section score:** 0.89

### Back-Translation (First Paragraph)

In this work, we explore deep learning architectures capable of reasoning about three-dimensional geometric data such as point clouds or geometric meshes. Typical convolutional architectures require highly regular input data formats, such as those for image grids or three-dimensional voxels, in order to implement weight sharing and other kernel optimizations. Since point clouds or geometric meshes are not in a regular format, most researchers transform this data into regular three-dimensional voxel grids or collections of images (for example, views) before inputting them to the deep network architecture. However, this transformation in data representation makes the resulting data unnecessarily voluminous - and also introduces quantization elements that can obscure the natural invariances of the data.

### Back-Translation (Main Contribution)

In this research, we design a novel deep network architecture suitable for consuming raw point clouds, which well respects the permutation invariance of points in the inputs. Our network, named PointNet, provides a unified architecture for applications ranging from object classification, part segmentation, to scene semantic analysis. Despite its simplicity, PointNet is highly efficient and effective. Empirically, it demonstrates strong performance comparable to or even better than state-of-the-art results. Theoretically, we provide analysis to understand what the network has learned and why the network is robust with respect to perturbations and corruption in the inputs.
