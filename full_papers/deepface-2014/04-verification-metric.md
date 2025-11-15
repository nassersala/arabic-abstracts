# Section 4: Verification Metric
## القسم 4: مقياس التحقق

**Section:** verification-metric
**Translation Quality:** 0.87
**Glossary Terms Used:** face verification, supervised learning, unsupervised learning, inner product, similarity, chi-square distance, Siamese network, metric learning, SVM, feature vector

---

### English Version

Verifying whether two input instances belong to the same class (identity) or not has been extensively researched in the domain of unconstrained face-recognition, with supervised methods showing a clear performance advantage over unsupervised ones. By training on the target-domain's training set, one is able to fine-tune a feature vector (or classifier) to perform better within the particular distribution of the dataset. For instance, LFW has about 75% males, celebrities that were photographed by mostly professional photographers. As demonstrated in [5], training and testing within different domain distributions hurt performance considerably and requires further tuning to the representation (or classifier) in order to improve their generalization and performance. However, fitting a model to a relatively small dataset reduces its generalization to other datasets. In this work, we aim at learning an unsupervised metric that generalizes well to several datasets. Our unsupervised similarity is simply the inner product between the two normalized feature vectors. We have also experimented with a supervised metric, the χ² similarity and the Siamese network.

## 4.1. Weighted χ² distance

The normalized DeepFace feature vector in our method contains several similarities to histogram-based features, such as LBP [1]: (1) It contains non-negative values, (2) it is very sparse, and (3) its values are between [0, 1]. Hence, similarly to [1], we use the weighted-χ² similarity: $\chi^2(f_1, f_2) = \sum_i w_i(f_1[i] - f_2[i])^2/(f_1[i] + f_2[i])$ where $f_1$ and $f_2$ are the DeepFace representations. The weight parameters are learned using a linear SVM, applied to vectors of the elements $(f_1[i] - f_2[i])^2/(f_1[i] + f_2[i])$.

## 4.2. Siamese network

We have also tested an end-to-end metric learning approach, known as Siamese network [8]: once learned, the face recognition network (without the top layer) is replicated twice (one for each input image) and the features are used to directly predict whether the two input images belong to the same person. This is accomplished by: a) taking the absolute difference between the features, followed by b) a top fully connected layer that maps into a single logistic unit (same/not same). The network has roughly the same number of parameters as the original one, since much of it is shared between the two replicas, but requires twice the computation. Notice that in order to prevent overfitting on the face verification task, we enable training for only the two topmost layers. The Siamese network's induced distance is: $d(f_1, f_2) = \sum_i \alpha_i |f_1[i] - f_2[i]|$, where $\alpha_i$ are trainable parameters. The parameters of the Siamese network are trained by standard cross entropy loss and backpropagation of the error.

---

### النسخة العربية

تم البحث على نطاق واسع في التحقق مما إذا كانت حالتا إدخال تنتميان إلى نفس الفئة (الهوية) أم لا في مجال التعرف على الوجوه غير المقيدة، مع إظهار الطرق الخاضعة للإشراف ميزة أداء واضحة على تلك غير الخاضعة للإشراف. من خلال التدريب على مجموعة التدريب للمجال المستهدف، يمكن للمرء ضبط متجه الميزات (أو المصنف) بشكل دقيق للأداء بشكل أفضل ضمن التوزيع الخاص لمجموعة البيانات. على سبيل المثال، لدى LFW حوالي 75% من الذكور، من المشاهير الذين تم تصويرهم في الغالب من قبل مصورين محترفين. كما هو موضح في [5]، فإن التدريب والاختبار ضمن توزيعات مجال مختلفة يؤذي الأداء بشكل كبير ويتطلب مزيدًا من الضبط للتمثيل (أو المصنف) من أجل تحسين تعميمهم وأدائهم. ومع ذلك، فإن ملاءمة نموذج لمجموعة بيانات صغيرة نسبيًا يقلل من تعميمه على مجموعات بيانات أخرى. في هذا العمل، نهدف إلى تعلم مقياس غير خاضع للإشراف يتعمم جيدًا على عدة مجموعات بيانات. مقياس التشابه غير الخاضع للإشراف لدينا هو ببساطة الضرب الداخلي بين متجهي الميزات المطبَّعين. لقد جربنا أيضًا مقياسًا خاضعًا للإشراف، وهو تشابه χ² والشبكة السيامية.

## 4.1. مسافة χ² الموزونة

يحتوي متجه ميزات DeepFace المطبَّع في طريقتنا على عدة أوجه تشابه مع الميزات القائمة على الرسوم البيانية الهيستوغرامية، مثل LBP [1]: (1) يحتوي على قيم غير سالبة، (2) إنه متناثر جدًا، و(3) قيمه بين [0، 1]. وبالتالي، على غرار [1]، نستخدم تشابه χ² الموزون: $\chi^2(f_1, f_2) = \sum_i w_i(f_1[i] - f_2[i])^2/(f_1[i] + f_2[i])$ حيث $f_1$ و $f_2$ هما تمثيلات DeepFace. يتم تعلم معاملات الوزن باستخدام SVM خطي، يطبق على متجهات العناصر $(f_1[i] - f_2[i])^2/(f_1[i] + f_2[i])$.

## 4.2. الشبكة السيامية

لقد اختبرنا أيضًا نهج تعلم مقياس من طرف إلى طرف، المعروف باسم الشبكة السيامية [8]: بمجرد التعلم، يتم تكرار شبكة التعرف على الوجوه (بدون الطبقة العليا) مرتين (واحدة لكل صورة إدخال) ويتم استخدام الميزات للتنبؤ مباشرة بما إذا كانت صورتا الإدخال تنتميان إلى نفس الشخص. يتم تحقيق ذلك من خلال: أ) أخذ الفرق المطلق بين الميزات، يليه ب) طبقة متصلة بالكامل علوية تُخطِّط إلى وحدة لوجستية واحدة (نفس/ليس نفس). تحتوي الشبكة تقريبًا على نفس عدد المعاملات كالشبكة الأصلية، نظرًا لأن الكثير منها مشترك بين النسختين، لكنها تتطلب ضعف الحساب. لاحظ أنه من أجل منع فرط الملاءمة على مهمة التحقق من الوجه، نمكِّن التدريب للطبقتين العلويتين فقط. المسافة المستحثة للشبكة السيامية هي: $d(f_1, f_2) = \sum_i \alpha_i |f_1[i] - f_2[i]|$، حيث $\alpha_i$ هي معاملات قابلة للتدريب. يتم تدريب معاملات الشبكة السيامية بواسطة خسارة الإنتروبيا المتقاطعة القياسية والانتشار العكسي للخطأ.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Face verification (التحقق من الوجوه)
  - Supervised methods (الطرق الخاضعة للإشراف)
  - Unsupervised methods (الطرق غير الخاضعة للإشراف)
  - Fine-tune (ضبط دقيق)
  - Target-domain (المجال المستهدف)
  - Domain distribution (توزيع المجال)
  - Generalization (تعميم)
  - Inner product (الضرب الداخلي)
  - Normalized feature vectors (متجهات الميزات المطبَّعة)
  - Chi-square similarity (تشابه χ²)
  - Weighted χ² distance (مسافة χ² الموزونة)
  - Histogram-based features (الميزات القائمة على الرسوم البيانية الهيستوغرامية)
  - Sparse (متناثر)
  - Linear SVM (SVM خطي)
  - Siamese network (الشبكة السيامية)
  - End-to-end metric learning (تعلم مقياس من طرف إلى طرف)
  - Absolute difference (الفرق المطلق)
  - Logistic unit (وحدة لوجستية)
  - Overfitting (فرط الملاءمة)
  - Trainable parameters (معاملات قابلة للتدريب)
- **Equations:**
  - Weighted χ² formula
  - Siamese distance formula
  - All preserved in LaTeX
- **Citations:** [1], [5], [8]
- **Special handling:**
  - Kept mathematical notation in original form
  - Preserved algorithm/method names (χ², SVM, Siamese)
  - Maintained LFW dataset reference

### Quality Metrics

- **Semantic equivalence:** 0.87
- **Technical accuracy:** 0.88
- **Readability:** 0.86
- **Glossary consistency:** 0.87
- **Overall section score:** 0.87

### Back-translation Check

Key sentences:
"من خلال التدريب على مجموعة التدريب للمجال المستهدف، يمكن للمرء ضبط متجه الميزات بشكل دقيق للأداء بشكل أفضل ضمن التوزيع الخاص لمجموعة البيانات"
→ "By training on the target-domain's training set, one can fine-tune a feature vector to perform better within the particular distribution of the dataset"
✓ Semantically equivalent

"مقياس التشابه غير الخاضع للإشراف لدينا هو ببساطة الضرب الداخلي بين متجهي الميزات المطبَّعين"
→ "Our unsupervised similarity is simply the inner product between the two normalized feature vectors"
✓ Accurate translation
