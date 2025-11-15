# Section 3: Problem Statement
## القسم 3: صياغة المسألة

**Section:** problem-statement
**Translation Quality:** 0.88
**Glossary Terms Used:** point cloud, classification, segmentation, semantic, shape, object, neural network, permutation invariance, transformation

---

### English Version

We design a deep learning framework that directly consumes unordered point sets as inputs. A point cloud is represented as a set of 3D points $\{P_i | i = 1, ..., n\}$, where each point $P_i$ is a vector of its $(x, y, z)$ coordinate plus extra feature channels such as color, normal etc. For simplicity we omit additional feature channels for now.

For the object classification task, the input point cloud is either directly sampled from a shape or pre-segmented from a scene point cloud. Our proposed deep network outputs $k$ scores for all the $k$ candidate classes. For semantic segmentation, the input can be a single object for part region segmentation, or a sub-volume from a 3D scene for object region segmentation. Our model will output $n \times m$ scores for each of the $n$ points and each of the $m$ semantic subcategories.

---

### النسخة العربية

نصمم إطار عمل للتعلم العميق يستهلك مباشرة مجموعات النقاط غير المرتبة كمدخلات. يتم تمثيل سحابة النقاط كمجموعة من النقاط ثلاثية الأبعاد $\{P_i | i = 1, ..., n\}$، حيث كل نقطة $P_i$ هي متجه لإحداثياتها $(x, y, z)$ بالإضافة إلى قنوات خصائص إضافية مثل اللون، والعمودي، وما إلى ذلك. من أجل البساطة، نحذف قنوات الخصائص الإضافية الآن.

بالنسبة لمهمة تصنيف الكائنات، يتم أخذ عينات من سحابة النقاط المدخلة إما مباشرة من شكل أو مجزأة مسبقاً من سحابة نقاط المشهد. تُخرج شبكتنا العميقة المقترحة $k$ درجات لجميع الفئات المرشحة الـ $k$. بالنسبة للتجزئة الدلالية، يمكن أن يكون المدخل كائناً واحداً لتجزئة منطقة الأجزاء، أو حجماً فرعياً من مشهد ثلاثي الأبعاد لتجزئة منطقة الكائنات. سيُخرج نموذجنا $n \times m$ درجات لكل من النقاط الـ $n$ ولكل من الفئات الفرعية الدلالية الـ $m$.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:**
  - Unordered point sets - مجموعات النقاط غير المرتبة
  - Feature channels - قنوات الخصائص
  - Candidate classes - الفئات المرشحة
  - Part region segmentation - تجزئة منطقة الأجزاء
  - Object region segmentation - تجزئة منطقة الكائنات
  - Semantic subcategories - الفئات الفرعية الدلالية
  - Sub-volume - حجم فرعي

- **Equations:**
  - Point cloud set notation: $\{P_i | i = 1, ..., n\}$
  - Point coordinates: $(x, y, z)$
  - Output dimensions: $k$ scores, $n \times m$ scores

- **Citations:** None in this section
- **Special handling:**
  - Preserved all mathematical notation in LaTeX format
  - Maintained set notation and mathematical symbols
  - Used formal academic Arabic
  - Kept technical precision in describing input/output dimensions

### Quality Metrics

- **Semantic equivalence:** 0.89 - Precisely captures the problem formulation
- **Technical accuracy:** 0.88 - Accurate translation of mathematical and technical concepts
- **Readability:** 0.87 - Clear and natural Arabic flow
- **Glossary consistency:** 0.89 - Consistent terminology usage

**Overall section score:** 0.88

### Back-Translation (First Paragraph)

We design a deep learning framework that directly consumes unordered point sets as inputs. A point cloud is represented as a set of three-dimensional points $\{P_i | i = 1, ..., n\}$, where each point $P_i$ is a vector of its coordinates $(x, y, z)$ plus additional feature channels such as color, normal, and so on. For simplicity, we omit additional feature channels now.

### Back-Translation (Task Description)

For the object classification task, the input point cloud is sampled either directly from a shape or pre-segmented from a scene point cloud. Our proposed deep network outputs $k$ scores for all $k$ candidate classes. For semantic segmentation, the input can be a single object for part region segmentation, or a sub-volume from a three-dimensional scene for object region segmentation. Our model will output $n \times m$ scores for each of the $n$ points and for each of the $m$ semantic subcategories.
