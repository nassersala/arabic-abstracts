# Section 3: Fast R-CNN Detection
## القسم 3: الكشف باستخدام Fast R-CNN

**Section:** detection
**Translation Quality:** 0.89
**Glossary Terms Used:** detection (كشف), fine-tuning (ضبط دقيق), object proposals (مقترحات الأجسام), forward pass (تمرير أمامي), bounding box (صندوق التحديد), fully connected (متصل بالكامل), convolutional (التفافي)

---

### English Version

Once a Fast R-CNN network is fine-tuned, detection amounts to little more than running a forward pass (assuming object proposals are pre-computed). The network takes as input an image (or an image pyramid, encoded as a list of images) and a list of R object proposals to score. At test-time, R is typically around 2000, although we will consider cases in which it is larger (~45k). When using an image pyramid, each RoI is assigned to the scale such that the scaled RoI is closest to 224² pixels in area [11].

For each test RoI r, the forward pass outputs a class posterior probability distribution p and a set of predicted bounding-box offsets relative to r (each of the K classes gets its own refined bounding-box prediction). We assign a detection confidence to r for each object class k using the estimated probability Pr(class = k | r) = pₖ. We then perform non-maximum suppression independently for each class using the algorithm and settings from R-CNN [9].

**3.1. Truncated SVD for faster detection**

For whole-image classification, the time spent computing the fully connected layers is small compared to the conv layers. On the contrary, for detection the number of RoIs to process is large and nearly half of the forward pass time is spent computing the fully connected layers (see Fig. 2). Large fully connected layers are easily accelerated by compressing them with truncated SVD [5, 23].

In this technique, a layer parameterized by the u×v weight matrix W is approximately factorized as

$$W \approx U \Sigma_t V^T\quad(5)$$

using SVD. In this factorization, U is a u×t matrix comprising the first t left-singular vectors of W, Σₜ is a t×t diagonal matrix containing the top t singular values of W, and V is v×t matrix comprising the first t right-singular vectors of W. Truncated SVD reduces the parameter count from uv to t(u+v), which can be significant if t is much smaller than min(u,v). To compress a network, the single fully connected layer corresponding to W is replaced by two fully connected layers, without a non-linearity between them. The first of these layers uses the weight matrix Σₜ V^T (and no biases) and the second uses U (with the original biases associated with W). This simple compression method gives good speedups when the number of RoIs is large.

---

### النسخة العربية

بمجرد إجراء الضبط الدقيق لشبكة Fast R-CNN، يصبح الكشف لا يتعدى تشغيل تمرير أمامي (بافتراض أن مقترحات الأجسام محسوبة مسبقاً). تأخذ الشبكة كمدخل صورة (أو هرم صور، مشفر كقائمة من الصور) وقائمة من R مقترح جسم للتقييم. في وقت الاختبار، عادةً ما تكون R حوالي 2000، على الرغم من أننا سننظر في حالات تكون فيها أكبر (~45k). عند استخدام هرم صور، يتم تعيين كل RoI إلى المقياس بحيث تكون RoI المقاسة الأقرب إلى 224² بكسل في المساحة [11].

لكل RoI اختبار r، يُخرج التمرير الأمامي توزيع احتمالي خلفي للفئة p ومجموعة من إزاحات صناديق التحديد المتوقعة نسبة إلى r (تحصل كل فئة من الفئات K على تنبؤ صندوق تحديد محسّن خاص بها). نقوم بتعيين ثقة كشف لـ r لكل فئة جسم k باستخدام الاحتمال المقدر Pr(class = k | r) = pₖ. ثم نقوم بإجراء قمع الحد الأقصى غير الأقصى بشكل مستقل لكل فئة باستخدام الخوارزمية والإعدادات من R-CNN [9].

**3.1. SVD المقطوع للكشف الأسرع**

بالنسبة لتصنيف الصورة الكاملة، يكون الوقت المستغرق في حساب الطبقات المتصلة بالكامل صغيراً مقارنة بالطبقات الالتفافية. على العكس من ذلك، بالنسبة للكشف، يكون عدد RoIs المراد معالجتها كبيراً وتُنفق ما يقرب من نصف وقت التمرير الأمامي في حساب الطبقات المتصلة بالكامل (انظر الشكل 2). يمكن تسريع الطبقات المتصلة بالكامل الكبيرة بسهولة عن طريق ضغطها باستخدام SVD المقطوع [5، 23].

في هذه التقنية، يتم تحليل طبقة معاملة بواسطة مصفوفة الأوزان u×v W تقريبياً على النحو التالي

$$W \approx U \Sigma_t V^T\quad(5)$$

باستخدام SVD. في هذا التحليل، U هي مصفوفة u×t تتألف من أول t متجه مفرد أيسر لـ W، Σₜ هي مصفوفة قطرية t×t تحتوي على أعلى t قيمة مفردة لـ W، و V هي مصفوفة v×t تتألف من أول t متجه مفرد أيمن لـ W. يقلل SVD المقطوع من عدد المعاملات من uv إلى t(u+v)، وهو ما يمكن أن يكون كبيراً إذا كانت t أصغر بكثير من min(u,v). لضغط شبكة، يتم استبدال الطبقة المتصلة بالكامل الواحدة المقابلة لـ W بطبقتين متصلتين بالكامل، دون لا خطية بينهما. تستخدم الطبقة الأولى من هاتين الطبقتين مصفوفة الأوزان Σₜ V^T (وبدون انحيازات) وتستخدم الثانية U (مع الانحيازات الأصلية المرتبطة بـ W). توفر طريقة الضغط البسيطة هذه تسريعات جيدة عندما يكون عدد RoIs كبيراً.

---

### Translation Notes

- **Figures referenced:** Figure 2 (timing for VGG16, detailed in Section 2)
- **Key terms introduced:**
  - test-time: وقت الاختبار
  - image pyramid: هرم صور
  - posterior probability distribution: توزيع احتمالي خلفي
  - detection confidence: ثقة الكشف
  - non-maximum suppression: قمع الحد الأقصى غير الأقصى
  - truncated SVD: SVD المقطوع (Singular Value Decomposition)
  - weight matrix: مصفوفة الأوزان
  - factorized: محلل
  - singular vectors: المتجهات المفردة
  - singular values: القيم المفردة
  - diagonal matrix: مصفوفة قطرية
  - parameter count: عدد المعاملات
  - compression: ضغط
  - non-linearity: لا خطية

- **Equations:** 1 equation (Eq. 5) preserved in LaTeX
- **Citations:** References [5, 9, 11, 23]
- **Special handling:**
  - Kept SVD (Singular Value Decomposition) in English as it's a standard mathematical term
  - Preserved mathematical notation (U, V, W, Σₜ, t, u, v, K, R, p, r, k)
  - Maintained numerical values (2000, 45k, 224²)
  - Kept "RoI" in English throughout

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.92
- Readability: 0.88
- Glossary consistency: 0.92
- **Overall section score:** 0.89

### Back-translation Verification

Key sentence back-translated:
Arabic: "يقلل SVD المقطوع من عدد المعاملات من uv إلى t(u+v)، وهو ما يمكن أن يكون كبيراً إذا كانت t أصغر بكثير من min(u,v)"
Back to English: "Truncated SVD reduces the parameter count from uv to t(u+v), which can be significant if t is much smaller than min(u,v)"
✓ Matches original semantics accurately
