# Appendix A: Harmonic Embeddings
## الملحق أ: التضمينات التوافقية

**Section:** Appendix - Harmonic Embeddings
**Translation Quality:** 0.85
**Glossary Terms Used:** embedding (التضمين), dimensionality (الأبعاد), compatibility (التوافق), optimization (تحسين), architecture (معمارية)

---

### English Version

**A.1 Harmonic Embedding Compatibility**

An interesting property of our face embeddings is that we can enforce compatibility between different embedding dimensions. This means that we can compare embeddings of different dimensionality directly, which is useful when upgrading models or deploying different model sizes for different platforms.

We achieve this through harmonic embeddings. Specifically, when training a model with d-dimensional embeddings, we structure the embedding layer such that the first k dimensions (where k < d) form a valid embedding on their own. This is done by adding additional triplet loss terms that enforce the constraint.

For example, if we train a 256-dimensional embedding model with harmonic structure, the first 128 dimensions alone form a valid 128-dimensional embedding. This has several advantages:

1. **Backward compatibility**: We can upgrade from a 128-dimensional model to a 256-dimensional model without needing to recompute all stored 128-dimensional embeddings. The new 256-dimensional embeddings are compatible with the old 128-dimensional ones for the first 128 dimensions.

2. **Multi-platform deployment**: We can deploy the full 256-dimensional model on servers while using the truncated 128-dimensional model on mobile devices. Comparisons between server and mobile embeddings remain valid.

3. **Flexible accuracy-size trade-off**: Users can choose their preferred embedding dimension based on available resources, with smooth degradation in accuracy as dimensions decrease.

**A.2 Training Procedure**

To train harmonic embeddings, we modify the triplet loss to include additional terms. Given an embedding f(x) ∈ R^d, we define truncated embeddings f_k(x) as the first k dimensions of f(x).

The harmonic triplet loss is:

L_harmonic = Σ_k w_k · L_k    (3)

where L_k is the standard triplet loss computed on f_k(x), and w_k are weights that determine the importance of each embedding dimension. In practice, we use k ∈ {64, 128, 256} with weights that emphasize the full dimensionality while still enforcing constraints on the truncated versions.

The training procedure is similar to standard FaceNet training:
1. Sample triplets from the training data
2. Compute embeddings f(x) for all images
3. For each dimension k, compute the truncated embedding f_k(x)
4. Compute the harmonic loss L_harmonic
5. Update network parameters using backpropagation

**A.3 Experimental Results**

We trained several models with harmonic embeddings and evaluated their performance. Table 8 shows the results on our hold-out test set.

The 256-dimensional harmonic embedding achieves 99.5% accuracy on the full 256 dimensions. When truncated to 128 dimensions, it achieves 99.2% accuracy, which is only slightly lower than a model trained specifically for 128 dimensions (99.3%). Similarly, the 128-dimensional harmonic model achieves 98.9% when truncated to 64 dimensions.

These results demonstrate that harmonic embeddings provide good flexibility with minimal performance loss. The ability to use a single model for multiple embedding dimensions is valuable for practical deployments where different platforms have different computational constraints.

**A.4 Implementation Details**

In our implementation, we structure the final embedding layer as a fully connected layer with d outputs. We apply L2 normalization to the full d-dimensional embedding as well as to each truncated embedding f_k(x).

During training, we use a batch size of 1,800 and compute triplet loss for each harmonic dimension within each batch. The weights w_k are set to emphasize higher dimensions: w_64 = 0.2, w_128 = 0.3, w_256 = 0.5. This ensures that the full model achieves the best possible performance while maintaining compatibility with truncated versions.

The additional computational cost of harmonic training is modest. Computing the loss for multiple dimensions increases training time by approximately 30% compared to standard training, but inference time is unchanged since we only compute the desired embedding dimension.

**A.5 Discussion**

Harmonic embeddings represent a useful technique for practical face recognition systems. They provide flexibility in deployment scenarios where different devices may have different computational capabilities. The ability to upgrade models while maintaining backward compatibility with stored embeddings is particularly valuable for large-scale systems with billions of stored face embeddings.

Future work could explore extending harmonic embeddings to other domains beyond face recognition, such as object recognition or image retrieval. The technique may also be applicable to other metric learning scenarios where embedding dimensionality is an important consideration.

---

### النسخة العربية

**أ.1 توافق التضمين التوافقي**

خاصية مثيرة للاهتمام لتضمينات الوجوه لدينا هي أنه يمكننا فرض التوافق بين أبعاد التضمين المختلفة. وهذا يعني أنه يمكننا مقارنة التضمينات ذات الأبعاد المختلفة مباشرة، وهو أمر مفيد عند ترقية النماذج أو نشر أحجام نماذج مختلفة لمنصات مختلفة.

نحقق ذلك من خلال التضمينات التوافقية. على وجه التحديد، عند تدريب نموذج بتضمينات ذات d بُعد، نبني طبقة التضمين بحيث تشكل الأبعاد k الأولى (حيث k < d) تضميناً صالحاً بمفردها. يتم ذلك عن طريق إضافة حدود خسارة ثلاثية إضافية تفرض القيد.

على سبيل المثال، إذا قمنا بتدريب نموذج تضمين ذي 256 بُعداً ببنية توافقية، فإن الأبعاد الـ 128 الأولى وحدها تشكل تضميناً صالحاً ذا 128 بُعداً. لهذا عدة مزايا:

1. **التوافق العكسي**: يمكننا الترقية من نموذج ذي 128 بُعداً إلى نموذج ذي 256 بُعداً دون الحاجة إلى إعادة حساب جميع التضمينات المخزنة ذات 128 بُعداً. التضمينات الجديدة ذات 256 بُعداً متوافقة مع القديمة ذات 128 بُعداً للأبعاد الـ 128 الأولى.

2. **النشر متعدد المنصات**: يمكننا نشر النموذج الكامل ذي 256 بُعداً على الخوادم بينما نستخدم النموذج المقتطع ذا 128 بُعداً على الأجهزة المحمولة. تظل المقارنات بين التضمينات على الخادم والأجهزة المحمولة صالحة.

3. **مفاضلة مرنة بين الدقة والحجم**: يمكن للمستخدمين اختيار بُعد التضمين المفضل لديهم بناءً على الموارد المتاحة، مع تدهور سلس في الدقة مع انخفاض الأبعاد.

**أ.2 إجراء التدريب**

لتدريب التضمينات التوافقية، نعدل الخسارة الثلاثية لتشمل حدوداً إضافية. بالنظر إلى تضمين f(x) ∈ R^d، نعرف التضمينات المقتطعة f_k(x) على أنها الأبعاد k الأولى من f(x).

الخسارة الثلاثية التوافقية هي:

L_harmonic = Σ_k w_k · L_k    (3)

حيث L_k هي الخسارة الثلاثية القياسية المحسوبة على f_k(x)، و w_k هي الأوزان التي تحدد أهمية كل بُعد تضمين. عملياً، نستخدم k ∈ {64, 128, 256} مع أوزان تؤكد على البُعد الكامل بينما لا تزال تفرض قيوداً على النسخ المقتطعة.

إجراء التدريب مشابه لتدريب فيس نت القياسي:
1. أخذ عينات من الثلاثيات من بيانات التدريب
2. حساب التضمينات f(x) لجميع الصور
3. لكل بُعد k، حساب التضمين المقتطع f_k(x)
4. حساب الخسارة التوافقية L_harmonic
5. تحديث معاملات الشبكة باستخدام الانتشار العكسي

**أ.3 النتائج التجريبية**

دربنا عدة نماذج بتضمينات توافقية وقيمنا أدائها. يظهر الجدول 8 النتائج على مجموعة الاختبار المحتفظ بها.

يحقق التضمين التوافقي ذو 256 بُعداً دقة 99.5% على الأبعاد الـ 256 الكاملة. عند اقتطاعه إلى 128 بُعداً، يحقق دقة 99.2%، وهي أقل قليلاً فقط من نموذج مدرب خصيصاً لـ 128 بُعداً (99.3%). وبالمثل، يحقق النموذج التوافقي ذو 128 بُعداً 98.9% عند اقتطاعه إلى 64 بُعداً.

توضح هذه النتائج أن التضمينات التوافقية توفر مرونة جيدة مع فقدان أداء ضئيل. القدرة على استخدام نموذج واحد لأبعاد تضمين متعددة قيمة للنشر العملي حيث تكون لدى المنصات المختلفة قيود حسابية مختلفة.

**أ.4 تفاصيل التنفيذ**

في تنفيذنا، نبني طبقة التضمين النهائية كطبقة متصلة بالكامل مع مخرجات d. نطبق تطبيع L2 على التضمين الكامل ذي d بُعد وكذلك على كل تضمين مقتطع f_k(x).

أثناء التدريب، نستخدم حجم دفعة يبلغ 1,800 ونحسب الخسارة الثلاثية لكل بُعد توافقي داخل كل دفعة. يتم تعيين الأوزان w_k للتأكيد على أبعاد أعلى: w_64 = 0.2، w_128 = 0.3، w_256 = 0.5. يضمن هذا أن النموذج الكامل يحقق أفضل أداء ممكن مع الحفاظ على التوافق مع النسخ المقتطعة.

التكلفة الحسابية الإضافية للتدريب التوافقي معتدلة. يزيد حساب الخسارة لأبعاد متعددة من وقت التدريب بحوالي 30% مقارنة بالتدريب القياسي، ولكن وقت الاستنتاج لا يتغير حيث نحسب فقط بُعد التضمين المطلوب.

**أ.5 المناقشة**

تمثل التضمينات التوافقية تقنية مفيدة لأنظمة التعرف على الوجوه العملية. توفر المرونة في سيناريوهات النشر حيث قد يكون لدى الأجهزة المختلفة قدرات حسابية مختلفة. القدرة على ترقية النماذج مع الحفاظ على التوافق العكسي مع التضمينات المخزنة ذات قيمة خاصة للأنظمة واسعة النطاق مع مليارات من تضمينات الوجوه المخزنة.

يمكن للأعمال المستقبلية استكشاف توسيع التضمينات التوافقية إلى مجالات أخرى تتجاوز التعرف على الوجوه، مثل التعرف على الأشياء أو استرجاع الصور. قد تكون التقنية أيضاً قابلة للتطبيق على سيناريوهات تعلم المقاييس الأخرى حيث تكون أبعاد التضمين اعتباراً مهماً.

---

### Translation Notes

- **Figures referenced:** None
- **Tables referenced:** Table 8
- **Key terms introduced:**
  - Harmonic embeddings (التضمينات التوافقية)
  - Backward compatibility (التوافق العكسي)
  - Truncated embeddings (التضمينات المقتطعة)
  - Multi-platform deployment (النشر متعدد المنصات)
  - Flexible trade-off (مفاضلة مرنة)
  - Smooth degradation (تدهور سلس)
  - Harmonic triplet loss (الخسارة الثلاثية التوافقية)
  - Fully connected layer (طبقة متصلة بالكامل)
  - Inference time (وقت الاستنتاج)
  - Metric learning (تعلم المقاييس)
  - Image retrieval (استرجاع الصور)
  - Computational capabilities (القدرات الحسابية)
  - Large-scale systems (الأنظمة واسعة النطاق)

- **Equations:**
  - Equation (3): Harmonic triplet loss
  - Mathematical notation preserved: f(x), f_k(x), w_k, Σ_k

- **Citations:**
  - Reference to future work and other domains

- **Special handling:**
  - Mathematical formulation carefully translated
  - Technical implementation details preserved
  - Practical deployment considerations emphasized
  - Dimension values preserved: 64, 128, 256
  - Weight values preserved: 0.2, 0.3, 0.5
  - Performance percentages preserved

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.87
- Readability: 0.84
- Glossary consistency: 0.83
- **Overall section score:** 0.85
