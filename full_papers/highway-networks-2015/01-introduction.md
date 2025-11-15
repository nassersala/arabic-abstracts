# Section 1: Introduction & Previous Work
## القسم 1: المقدمة والأعمال السابقة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** deep learning, neural networks, supervised machine learning, training, optimization, gradient descent, LSTM, recurrent networks, activation function, skip connections, deep networks, plain networks, vanishing gradients, architecture, feedforward network

---

### English Version

Many recent empirical breakthroughs in supervised machine learning have been achieved through large and deep neural networks. Network depth (the number of successive computational layers) has played perhaps the most important role in these successes. For instance, within just a few years, the top-5 image classification accuracy on the 1000-class ImageNet dataset has increased from ∼84% [1] to ∼95% [2, 3] using deeper networks with rather small receptive fields [4, 5]. Other results on practical machine learning problems have also underscored the superiority of deeper networks [6] in terms of accuracy and/or performance.

In fact, deep networks can represent certain function classes far more efficiently than shallow ones. This is perhaps most obvious for recurrent nets, the deepest of them all. For example, the n bit parity problem can in principle be learned by a large feedforward net with n binary input units, 1 output unit, and a single but large hidden layer. But the natural solution for arbitrary n is a recurrent net with only 3 units and 5 weights, reading the input bit string one bit at a time, making a single recurrent hidden unit flip its state whenever a new 1 is observed [7]. Related observations hold for Boolean circuits [8, 9] and modern neural networks [10, 11, 12].

To deal with the difficulties of training deep networks, some researchers have focused on developing better optimizers (e.g. [13, 14, 15]). Well-designed initialization strategies, in particular the normalized variance-preserving initialization for certain activation functions [16, 17], have been widely adopted for training moderately deep networks. Other similarly motivated strategies have shown promising results in preliminary experiments [18, 19]. Experiments showed that certain activation functions based on local competition [20, 21] may help to train deeper networks. Skip connections between layers or to output layers (where error is "injected") have long been used in neural networks, more recently with the explicit aim to improve the flow of information [22, 23, 2, 24]. A related recent technique is based on using soft targets from a shallow teacher network to aid in training deeper student networks in multiple stages [25], similar to the neural history compressor for sequences, where a slowly ticking teacher recurrent net is "distilled" into a quickly ticking student recurrent net by forcing the latter to predict the hidden units of the former [26]. Finally, deep networks can be trained layer-wise to help in credit assignment [26, 27], but this approach is less attractive compared to direct training.

Very deep network training still faces problems, albeit perhaps less fundamental ones than the problem of vanishing gradients in standard recurrent networks [28]. The stacking of several non-linear transformations in conventional feed-forward network architectures typically results in poor propagation of activations and gradients. Hence it remains hard to investigate the benefits of very deep networks for a variety of problems.

To overcome this, we take inspiration from Long Short Term Memory (LSTM) recurrent networks [29, 30]. We propose to modify the architecture of very deep feedforward networks such that information flow across layers becomes much easier. This is accomplished through an LSTM-inspired adaptive gating mechanism that allows for computation paths along which information can flow across many layers without attenuation. We call such paths information highways. They yield highway networks, as opposed to traditional 'plain' networks.

Our primary contribution is to show that extremely deep highway networks can be trained directly using stochastic gradient descent (SGD), in contrast to plain networks which become hard to optimize as depth increases (Section 3.1). Deep networks with limited computational budget (for which a two-stage training procedure mentioned above was recently proposed [25]) can also be directly trained in a single stage when converted to highway networks. Their ease of training is supported by experimental results demonstrating that highway networks also generalize well to unseen data.

---

### النسخة العربية

حققت العديد من الإنجازات التجريبية الحديثة في التعلم الآلي الموجه من خلال الشبكات العصبية الكبيرة والعميقة. لقد لعب عمق الشبكة (عدد الطبقات الحسابية المتتالية) الدور الأكثر أهمية في هذه النجاحات. على سبيل المثال، في غضون بضع سنوات فقط، زادت دقة تصنيف الصور من أعلى 5 على مجموعة بيانات ImageNet المكونة من 1000 صنف من ~84% [1] إلى ~95% [2, 3] باستخدام شبكات أعمق ذات حقول استقبالية صغيرة نسبياً [4, 5]. كما أكدت النتائج الأخرى على مشاكل التعلم الآلي العملية تفوق الشبكات الأعمق [6] من حيث الدقة و/أو الأداء.

في الواقع، يمكن للشبكات العميقة تمثيل فئات دوال معينة بكفاءة أكبر بكثير من الشبكات الضحلة. وهذا واضح بشكل خاص في الشبكات التكرارية، الأعمق من بينها جميعاً. على سبيل المثال، يمكن من حيث المبدأ تعلم مشكلة التماثل (parity) لـ n بت بواسطة شبكة أمامية كبيرة تحتوي على n وحدة إدخال ثنائية، ووحدة إخراج واحدة، وطبقة مخفية واحدة ولكنها كبيرة. لكن الحل الطبيعي لـ n عشوائي هو شبكة تكرارية تحتوي على 3 وحدات فقط و5 أوزان، تقرأ سلسلة بت الإدخال بتة واحدة في كل مرة، مما يجعل وحدة مخفية تكرارية واحدة تقلب حالتها كلما لوحظت قيمة 1 جديدة [7]. وتنطبق ملاحظات مماثلة على الدوائر المنطقية (Boolean circuits) [8, 9] والشبكات العصبية الحديثة [10, 11, 12].

للتعامل مع صعوبات تدريب الشبكات العميقة، ركز بعض الباحثين على تطوير محسنات أفضل (مثل [13, 14, 15]). تم اعتماد استراتيجيات التهيئة المصممة جيداً على نطاق واسع، وعلى وجه الخصوص التهيئة الطبيعية التي تحافظ على التباين لدوال تنشيط معينة [16, 17]، لتدريب الشبكات ذات العمق المتوسط. أظهرت استراتيجيات أخرى بدافع مماثل نتائج واعدة في تجارب أولية [18, 19]. أظهرت التجارب أن دوال تنشيط معينة مبنية على المنافسة المحلية [20, 21] قد تساعد في تدريب شبكات أعمق. تم استخدام الاتصالات التخطية (skip connections) بين الطبقات أو إلى طبقات الإخراج (حيث يتم "حقن" الخطأ) منذ فترة طويلة في الشبكات العصبية، وبشكل أكثر حداثة بهدف صريح لتحسين تدفق المعلومات [22, 23, 2, 24]. تقنية حديثة ذات صلة تعتمد على استخدام أهداف ناعمة من شبكة معلم ضحلة للمساعدة في تدريب شبكات طالب أعمق على مراحل متعددة [25]، على غرار ضاغط التاريخ العصبي للتسلسلات، حيث يتم "تقطير" شبكة معلم تكرارية بطيئة النبض إلى شبكة طالب تكرارية سريعة النبض عن طريق إجبار الأخيرة على التنبؤ بالوحدات المخفية للأولى [26]. أخيراً، يمكن تدريب الشبكات العميقة طبقة تلو الأخرى للمساعدة في إسناد الفضل (credit assignment) [26, 27]، لكن هذا النهج أقل جاذبية مقارنة بالتدريب المباشر.

لا يزال تدريب الشبكات العميقة جداً يواجه مشاكل، وإن كانت أقل جوهرية من مشكلة اختفاء التدرجات في الشبكات التكرارية القياسية [28]. يؤدي تكديس عدة تحويلات غير خطية في معماريات الشبكات الأمامية التقليدية عادة إلى انتشار ضعيف للتنشيطات والتدرجات. وبالتالي يبقى من الصعب دراسة فوائد الشبكات العميقة جداً لمجموعة متنوعة من المشاكل.

للتغلب على ذلك، نستوحي الإلهام من شبكات الذاكرة طويلة-قصيرة المدى (LSTM) التكرارية [29, 30]. نقترح تعديل معمارية الشبكات الأمامية العميقة جداً بحيث يصبح تدفق المعلومات عبر الطبقات أسهل بكثير. يتم تحقيق ذلك من خلال آلية بوابة تكيفية مستوحاة من LSTM تسمح بمسارات حسابية يمكن للمعلومات على طولها أن تتدفق عبر العديد من الطبقات دون توهين. نسمي هذه المسارات طرق المعلومات السريعة (information highways). وهي تنتج شبكات الطرق السريعة، على عكس الشبكات "العادية" التقليدية.

مساهمتنا الأساسية هي إظهار أن شبكات الطرق السريعة العميقة جداً يمكن تدريبها مباشرة باستخدام الانحدار التدرجي العشوائي (SGD)، على عكس الشبكات العادية التي يصبح من الصعب تحسينها مع زيادة العمق (القسم 3.1). يمكن أيضاً تدريب الشبكات العميقة ذات الميزانية الحسابية المحدودة (التي تم اقتراح إجراء تدريب من مرحلتين لها مؤخراً [25]) مباشرة في مرحلة واحدة عند تحويلها إلى شبكات طرق سريعة. يدعم سهولة تدريبها نتائج تجريبية تثبت أن شبكات الطرق السريعة تعمم جيداً أيضاً على البيانات غير المرئية.

---

### Translation Notes

- **Figures referenced:** None in introduction
- **Key terms introduced:**
  - network depth → عمق الشبكة
  - receptive fields → حقول استقبالية
  - parity problem → مشكلة التماثل
  - feedforward net → شبكة أمامية
  - recurrent net → شبكة تكرارية
  - Boolean circuits → دوائر منطقية
  - optimizers → محسنات
  - initialization strategies → استراتيجيات التهيئة
  - variance-preserving → الحافظة على التباين
  - activation functions → دوال تنشيط
  - skip connections → اتصالات تخطية
  - credit assignment → إسناد الفضل
  - vanishing gradients → اختفاء التدرجات
  - stochastic gradient descent (SGD) → الانحدار التدرجي العشوائي
  - plain networks → شبكات عادية
  - attenuation → توهين
- **Equations:** None
- **Citations:** Multiple references [1] through [30]
- **Special handling:**
  - Maintained all citation numbers
  - Translated technical terms consistently with glossary
  - Preserved comparative language (~84% to ~95%)

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.89
- **Overall section score:** 0.88
