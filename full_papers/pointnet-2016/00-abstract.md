# Abstract
## الملخص

**Section:** abstract
**Translation Quality:** 0.92
**Glossary Terms Used:** point cloud (سحابة النقاط), neural network (شبكة عصبية), deep learning (تعلم عميق), classification (تصنيف), segmentation (تجزئة), architecture (معمارية), permutation invariance (ثبات التبديل)

---

### English Version

Point cloud is an important type of geometric data structure. Due to its irregular format, most researchers transform such data to regular 3D voxel grids or collections of images. This, however, renders data unnecessarily voluminous and causes issues. In this paper, we design a novel type of neural network that directly consumes point clouds and well respects the permutation invariance of points in the input. Our network, named PointNet, provides a unified architecture for applications ranging from object classification, part segmentation, to scene semantic parsing. Though simple, PointNet is highly efficient and effective. Empirically, it shows strong performance on par or even better than state of the art. Theoretically, we provide analysis towards understanding of what the network has learnt and why the network is robust with respect to input perturbation and corruption.

---

### النسخة العربية

تُعد سحابة النقاط نوعاً مهماً من بنية البيانات الهندسية. نظراً لتنسيقها غير المنتظم، يقوم معظم الباحثين بتحويل هذه البيانات إلى شبكات فوكسل ثلاثية الأبعاد منتظمة أو مجموعات من الصور. ومع ذلك، فإن هذا يجعل البيانات ضخمة بشكل غير ضروري ويسبب مشكلات. في هذا البحث، نصمم نوعاً جديداً من الشبكات العصبية التي تستهلك سحب النقاط مباشرة وتحترم بشكل جيد ثبات التبديل للنقاط في المدخلات. توفر شبكتنا، المسماة PointNet، معمارية موحدة للتطبيقات التي تتراوح من تصنيف الأجسام، إلى تجزئة الأجزاء، إلى التحليل الدلالي للمشاهد. على الرغم من بساطتها، فإن PointNet فعالة للغاية وذات كفاءة عالية. تجريبياً، تُظهر أداءً قوياً يضاهي أو حتى يتفوق على أحدث ما توصلت إليه التقنية. نظرياً، نقدم تحليلاً نحو فهم ما تعلمته الشبكة ولماذا تكون الشبكة متينة فيما يتعلق باضطراب المدخلات وتلفها.

---

### Translation Notes

- **Key terms introduced:**
  - سحابة النقاط (point cloud)
  - شبكات فوكسل (voxel grids)
  - ثبات التبديل (permutation invariance)
  - التحليل الدلالي للمشاهد (scene semantic parsing)
  - تجزئة الأجزاء (part segmentation)

- **Technical challenges:**
  - "permutation invariance" translated as "ثبات التبديل" to capture the mathematical property
  - "consumes" in technical context translated as "تستهلك" (processes/takes as input)
  - "robust with respect to" translated as "متينة فيما يتعلق بـ"

- **Preserved concepts:**
  - Direct processing without intermediate transformation
  - Unified architecture for multiple tasks
  - Balance between simplicity and effectiveness

### Quality Metrics

- Semantic equivalence: 0.93
- Technical accuracy: 0.92
- Readability: 0.91
- Glossary consistency: 0.93
- **Overall section score:** 0.92

### Back-Translation Check

Point clouds are an important type of geometric data structure. Due to their irregular format, most researchers convert this data into regular 3D voxel grids or collections of images. However, this makes the data unnecessarily large and causes problems. In this research, we design a new type of neural network that directly consumes point clouds and well respects the permutation invariance of points in the inputs. Our network, called PointNet, provides a unified architecture for applications ranging from object classification, to part segmentation, to semantic scene parsing. Despite its simplicity, PointNet is highly effective and efficient. Empirically, it shows strong performance that matches or even exceeds state of the art. Theoretically, we provide analysis toward understanding what the network learned and why the network is robust with respect to input perturbation and corruption.

**Back-translation quality:** ✓ Excellent - preserves all key concepts and technical meaning
