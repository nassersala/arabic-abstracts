# Section 5: Experiments
## القسم 5: التجارب

**Section:** Experiments
**Translation Quality:** 0.86
**Glossary Terms Used:** accuracy (دقة), embedding (التضمين), deep learning (تعلم عميق), architecture (معمارية), benchmark (معيار), convolutional neural network (الشبكة العصبية الالتفافية), dataset (مجموعة بيانات), optimization (تحسين)

---

### English Version

We evaluate the performance of our method on the four different datasets described in section 4. In addition to evaluating the final performance, we also investigate the following questions:

1. What is the optimal way to use triplets in training?
2. How large can we make the mini-batch size?
3. What is the optimal embedding dimension?
4. What is the trade-off between model size and accuracy?

**5.1 Computation Accuracy Trade-off**

We investigate the trade-off between model size and accuracy by comparing various model architectures on our hold-out test set. The results are shown in Table 2. As can be seen, NN1 has the best performance but also the most parameters. While NN2 has a similar number of FLOPS to NN1, it has fewer parameters and also slightly lower performance.

The smaller NN3 and NN4 models are inspired by the Inception architecture and show that with careful design it is possible to reduce the model size dramatically (up to 20x) while only losing a small amount of accuracy. This is particularly important for mobile deployment scenarios. Table 2 shows that NN3 achieves 98.9% accuracy on the hold-out test set while being 5x smaller than NN1. The smallest model NN4 still achieves 98.1% accuracy.

**5.2 Effect of CNN Model**

We train several models on a large dataset and compare them on the LFW benchmark. Table 3 shows that all models achieve high performance. The NN1 model achieves 99.63% accuracy, which is a new state-of-the-art result. The NN2 model achieves 99.47% and the smaller NN3 model achieves 98.87%. These results demonstrate that compact models can achieve competitive performance.

We also compare our results to other published methods. Table 4 shows that FaceNet achieves significantly better performance than all previous methods. We reduce the error rate by approximately 30% compared to the previous best published result on LFW.

**5.3 Sensitivity to Image Quality**

To understand the sensitivity to image quality we ran FaceNet on the YouTube Faces DB which contains lower quality images from video frames. Table 5 shows our results compared to prior work. We achieve 95.12% accuracy on set-level face verification and 91.64% on the harder frame-level verification. This represents a significant improvement over previous methods.

The results demonstrate that FaceNet embeddings generalize well across different image qualities and settings. The embeddings learned from high-quality images in the training set transfer effectively to the lower quality YouTube videos.

**5.4 Embedding Dimensionality**

We investigate the effect of embedding dimensionality on accuracy. Figure 5 shows the validation rate as a function of embedding dimension on our hold-out test set. As expected, accuracy increases with dimensionality, but the gains diminish after 128 dimensions. We chose 128-dimensional embeddings as a good trade-off between accuracy and compactness.

At 128 dimensions we achieve 99.3% validation rate at 10^-4 FAR. Increasing to 256 dimensions only provides a small improvement to 99.5%. The compact 64-dimensional embedding still achieves 97.7% which may be suitable for extremely resource-constrained applications.

**5.5 Amount of Training Data**

We investigate the impact of training data size by training models on datasets of varying sizes. Figure 6 shows that performance continues to improve with more training data, even up to 200 million face images. This suggests that FaceNet can benefit from even larger training sets.

The results show that with 10 million training images we achieve around 98.5% accuracy on our test set. This increases to 99.3% with 100 million images and 99.6% with 200 million images. The continued improvement with more data indicates that we have not yet saturated the model capacity.

**5.6 Performance on LFW**

Table 6 shows detailed results on the LFW dataset. We report accuracy for both the restricted and unrestricted training protocols. Under the unrestricted protocol, where we can use external training data, FaceNet achieves 99.63% accuracy. This is significantly better than all previous published results.

Our method does not use any alignment beyond the similarity transform computed from detected face landmarks. This makes our system simpler and more robust than methods that require explicit 3D alignment or complex preprocessing.

**5.7 Performance on YouTube Faces DB**

Table 7 shows results on the YouTube Faces DB dataset. We achieve 95.12% accuracy on the standard average pooling protocol and 91.64% using a single frame from each video. Both results represent significant improvements over prior art.

The strong performance on video data demonstrates that FaceNet embeddings are robust to the variations in pose, lighting, and image quality that occur in real-world videos. This makes FaceNet well-suited for practical face recognition applications.

---

### النسخة العربية

نقيم أداء طريقتنا على أربع مجموعات بيانات مختلفة موضحة في القسم 4. بالإضافة إلى تقييم الأداء النهائي، نستكشف أيضاً الأسئلة التالية:

1. ما هي الطريقة المثلى لاستخدام الثلاثيات في التدريب؟
2. ما مدى كبر حجم الدفعة الصغيرة الذي يمكننا جعله؟
3. ما هو بُعد التضمين الأمثل؟
4. ما هي المفاضلة بين حجم النموذج والدقة؟

**5.1 مفاضلة دقة الحساب**

نستكشف المفاضلة بين حجم النموذج والدقة من خلال مقارنة معماريات نماذج مختلفة على مجموعة الاختبار المحتفظ بها. النتائج موضحة في الجدول 2. كما يمكن ملاحظته، NN1 لديه أفضل أداء ولكن أيضاً أكثر المعاملات. بينما NN2 لديه عدد مماثل من FLOPS لـ NN1، لديه معاملات أقل وأيضاً أداء أقل قليلاً.

النماذج الأصغر NN3 و NN4 مستوحاة من معمارية Inception وتظهر أنه مع التصميم الدقيق من الممكن تقليل حجم النموذج بشكل كبير (حتى 20 ضعفاً) مع فقدان كمية صغيرة فقط من الدقة. هذا مهم بشكل خاص لسيناريوهات النشر على الأجهزة المحمولة. يظهر الجدول 2 أن NN3 يحقق دقة 98.9% على مجموعة الاختبار المحتفظ بها بينما يكون أصغر بـ 5 مرات من NN1. النموذج الأصغر NN4 لا يزال يحقق دقة 98.1%.

**5.2 تأثير نموذج الشبكة العصبية الالتفافية**

ندرب عدة نماذج على مجموعة بيانات كبيرة ونقارنها على معيار LFW. يظهر الجدول 3 أن جميع النماذج تحقق أداءً عالياً. يحقق نموذج NN1 دقة 99.63%، وهي نتيجة متطورة جديدة. يحقق نموذج NN2 دقة 99.47% والنموذج الأصغر NN3 يحقق 98.87%. توضح هذه النتائج أن النماذج المدمجة يمكن أن تحقق أداءً تنافسياً.

نقارن أيضاً نتائجنا بطرق أخرى منشورة. يظهر الجدول 4 أن فيس نت يحقق أداءً أفضل بكثير من جميع الطرق السابقة. نخفض معدل الخطأ بحوالي 30% مقارنة بأفضل نتيجة منشورة سابقة على LFW.

**5.3 الحساسية لجودة الصورة**

لفهم الحساسية لجودة الصورة، قمنا بتشغيل فيس نت على قاعدة بيانات يوتيوب للوجوه التي تحتوي على صور ذات جودة أقل من إطارات الفيديو. يظهر الجدول 5 نتائجنا مقارنة بالأعمال السابقة. نحقق دقة 95.12% على التحقق من الوجوه على مستوى المجموعة و91.64% على التحقق الأصعب على مستوى الإطار. وهذا يمثل تحسناً كبيراً على الطرق السابقة.

توضح النتائج أن تضمينات فيس نت تعمم بشكل جيد عبر جودات وإعدادات صور مختلفة. التضمينات المتعلمة من صور عالية الجودة في مجموعة التدريب تنتقل بفعالية إلى مقاطع فيديو يوتيوب ذات الجودة الأقل.

**5.4 أبعاد التضمين**

نستكشف تأثير أبعاد التضمين على الدقة. يظهر الشكل 5 معدل التحقق كدالة لبُعد التضمين على مجموعة الاختبار المحتفظ بها. كما هو متوقع، تزداد الدقة مع الأبعاد، ولكن المكاسب تتضاءل بعد 128 بُعداً. اخترنا تضمينات ذات 128 بُعداً كمفاضلة جيدة بين الدقة والإيجاز.

عند 128 بُعداً نحقق معدل تحقق 99.3% عند FAR يبلغ 10^-4. الزيادة إلى 256 بُعداً توفر فقط تحسناً صغيراً إلى 99.5%. التضمين المدمج ذو 64 بُعداً لا يزال يحقق 97.7% والذي قد يكون مناسباً للتطبيقات المقيدة بالموارد بشكل شديد.

**5.5 كمية بيانات التدريب**

نستكشف تأثير حجم بيانات التدريب من خلال تدريب النماذج على مجموعات بيانات بأحجام متفاوتة. يظهر الشكل 6 أن الأداء يستمر في التحسن مع المزيد من بيانات التدريب، حتى ما يصل إلى 200 مليون صورة وجه. يشير هذا إلى أن فيس نت يمكن أن يستفيد من مجموعات تدريب أكبر.

تظهر النتائج أنه مع 10 ملايين صورة تدريب نحقق حوالي 98.5% دقة على مجموعة الاختبار الخاصة بنا. يزداد هذا إلى 99.3% مع 100 مليون صورة و99.6% مع 200 مليون صورة. الزيادة المستمرة مع المزيد من البيانات تشير إلى أننا لم نشبع قدرة النموذج بعد.

**5.6 الأداء على LFW**

يظهر الجدول 6 نتائج مفصلة على مجموعة بيانات LFW. نبلغ عن الدقة لكل من بروتوكولات التدريب المقيدة وغير المقيدة. تحت البروتوكول غير المقيد، حيث يمكننا استخدام بيانات تدريب خارجية، يحقق فيس نت دقة 99.63%. وهذا أفضل بكثير من جميع النتائج المنشورة سابقاً.

لا تستخدم طريقتنا أي محاذاة تتجاوز تحويل التشابه المحسوب من معالم الوجه المكتشفة. هذا يجعل نظامنا أبسط وأكثر قوة من الطرق التي تتطلب محاذاة ثلاثية الأبعاد صريحة أو معالجة مسبقة معقدة.

**5.7 الأداء على قاعدة بيانات يوتيوب للوجوه**

يظهر الجدول 7 النتائج على مجموعة بيانات قاعدة بيانات يوتيوب للوجوه. نحقق دقة 95.12% على بروتوكول التجميع المتوسط القياسي و91.64% باستخدام إطار واحد من كل فيديو. كلا النتيجتين تمثلان تحسينات كبيرة على الفن السابق.

يُظهر الأداء القوي على بيانات الفيديو أن تضمينات فيس نت قوية في مواجهة الاختلافات في الوضعية والإضاءة وجودة الصورة التي تحدث في مقاطع الفيديو في العالم الحقيقي. وهذا يجعل فيس نت مناسباً تماماً لتطبيقات التعرف على الوجوه العملية.

---

### Translation Notes

- **Figures referenced:** Figure 5, Figure 6
- **Tables referenced:** Table 2, Table 3, Table 4, Table 5, Table 6, Table 7
- **Key terms introduced:**
  - Model size (حجم النموذج)
  - Trade-off (مفاضلة)
  - State-of-the-art (متطور / نتيجة متطورة)
  - Mobile deployment (النشر على الأجهزة المحمولة)
  - Set-level verification (التحقق على مستوى المجموعة)
  - Frame-level verification (التحقق على مستوى الإطار)
  - Average pooling (التجميع المتوسط)
  - Restricted/Unrestricted protocol (بروتوكول مقيد/غير مقيد)
  - External training data (بيانات تدريب خارجية)
  - Similarity transform (تحويل التشابه)
  - 3D alignment (محاذاة ثلاثية الأبعاد)
  - Model capacity (قدرة النموذج)
  - Resource-constrained (مقيد بالموارد)

- **Equations:**
  - FAR notation: 10^-4, 10^-3
  - Percentage values preserved

- **Citations:**
  - References to prior work and published methods

- **Special handling:**
  - Model names kept in English: NN1, NN2, NN3, NN4
  - Dataset names kept in English: LFW, YouTube Faces DB
  - Technical measurements and statistics preserved
  - Comparative statements carefully translated

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.86
