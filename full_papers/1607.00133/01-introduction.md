# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** neural networks, machine learning, deep learning, training, differential privacy, privacy guarantees, adversary, model parameters, TensorFlow, MNIST, CIFAR-10, privacy loss, privacy budget, non-convex, regularization, overfitting

---

### English Version

Recent progress in neural networks has led to impressive successes in a wide range of applications, including image classification, language representation, move selection for Go, and many more (e.g., [citations]). These advances are enabled, in part, by the availability of large and representative datasets for training neural networks. These datasets are often crowdsourced, and may contain sensitive information. Their use requires techniques that meet the demands of the applications while offering principled and rigorous privacy guarantees.

In this paper, we combine state-of-the-art machine learning methods with advanced privacy-preserving mechanisms, training neural networks within a modest ("single-digit") privacy budget. We treat models with non-convex objectives, several layers, and tens of thousands to millions of parameters. (In contrast, previous work obtains strong results on convex models with smaller numbers of parameters, or treats complex neural networks but with a large privacy loss.) For this purpose, we develop new algorithmic techniques, a refined analysis of privacy costs within the framework of differential privacy, and careful implementation strategies:

1. We demonstrate that, by tracking detailed information (higher moments) of the privacy loss, we can obtain much tighter estimates on the overall privacy loss, both asymptotically and empirically.

2. We improve the computational efficiency of differentially private training by introducing new techniques. These techniques include efficient algorithms for computing gradients for individual training examples, subdividing tasks into smaller batches to reduce memory footprint, and applying differentially private principal projection at the input layer.

3. We build on the machine learning framework TensorFlow for training models with differential privacy. We evaluate our approach on two standard image classification tasks, MNIST and CIFAR-10. We chose these two tasks because they are based on public datasets and have a long record of serving as benchmarks in machine learning. Our experience indicates that privacy protection for deep neural networks can be achieved at a modest cost in software complexity, training efficiency, and model quality.

Machine learning systems often comprise elements that contribute to protecting their training data. In particular, regularization techniques, which aim to avoid overfitting to the examples used for training, may hide details of those examples. On the other hand, explaining the internal representations in deep neural networks is notoriously difficult, and their large capacity entails that these representations may potentially encode fine details of at least some of the training data. In some cases, a determined adversary may be able to extract parts of the training data. For example, Fredrikson et al. demonstrated a model-inversion attack that recovers images from a facial recognition system.

While the model-inversion attack requires only "black-box" access to a trained model (that is, interaction with the model via inputs and outputs), we consider adversaries with additional capabilities, much like Shokri and Shmatikov. Our approach offers protection against a strong adversary with full knowledge of the training mechanism and access to the model's parameters.

This protection is attractive, in particular, for applications of machine learning on mobile phones, tablets, and other devices. Storing models on-device enables power-efficient, low-latency inference, and may contribute to privacy since inference does not require communicating user data to a central server; on the other hand, we must assume that the model parameters themselves may be exposed to hostile inspection.

Furthermore, when we are concerned with preserving the privacy of one record in the training data, we allow for the possibility that the adversary controls some or even all of the rest of the training data. In practice, this possibility cannot always be excluded, for example when the data is crowdsourced.

The next section reviews background on deep learning and on differential privacy. Sections 3 and 4 explain our approach and implementation. Section 5 describes our experimental results. Section 6 discusses related work, and Section 7 concludes.

---

### النسخة العربية

أدى التقدم الأخير في الشبكات العصبية إلى نجاحات مذهلة في مجموعة واسعة من التطبيقات، بما في ذلك تصنيف الصور، والتمثيل اللغوي، واختيار الحركات في لعبة Go، والعديد من التطبيقات الأخرى. تُمكَّن هذه التطورات، جزئياً، من خلال توفر مجموعات بيانات كبيرة وممثلة لتدريب الشبكات العصبية. غالباً ما يتم جمع هذه البيانات من مصادر عامة (crowdsourced)، وقد تحتوي على معلومات حساسة. يتطلب استخدامها تقنيات تلبي متطلبات التطبيقات مع تقديم ضمانات خصوصية مبدئية وصارمة.

في هذا البحث، نجمع بين أحدث طرق تعلم الآلة وآليات متقدمة للحفاظ على الخصوصية، حيث ندرب الشبكات العصبية ضمن ميزانية خصوصية متواضعة ("رقم أحادي"). نتعامل مع نماذج ذات أهداف غير محدبة، وعدة طبقات، وعشرات الآلاف إلى ملايين المعاملات. (في المقابل، تحصل الأبحاث السابقة على نتائج قوية على نماذج محدبة بأعداد أقل من المعاملات، أو تتعامل مع شبكات عصبية معقدة ولكن بخسارة خصوصية كبيرة). لهذا الغرض، نطور تقنيات خوارزمية جديدة، وتحليلاً محسّناً لتكاليف الخصوصية ضمن إطار الخصوصية التفاضلية، واستراتيجيات تنفيذ دقيقة:

1. نوضح أنه من خلال تتبع معلومات تفصيلية (العزوم الأعلى) لخسارة الخصوصية، يمكننا الحصول على تقديرات أكثر دقة لخسارة الخصوصية الإجمالية، سواء بشكل تقاربي أو تجريبي.

2. نحسّن الكفاءة الحسابية للتدريب الخاص بالخصوصية التفاضلية من خلال تقديم تقنيات جديدة. تشمل هذه التقنيات خوارزميات فعالة لحساب التدرجات لأمثلة التدريب الفردية، وتقسيم المهام إلى دفعات أصغر لتقليل استخدام الذاكرة، وتطبيق الإسقاط الرئيسي الخاص بالخصوصية التفاضلية في طبقة الإدخال.

3. نبني على إطار تعلم الآلة TensorFlow لتدريب النماذج مع الخصوصية التفاضلية. نقيّم نهجنا على مهمتي تصنيف الصور المعياريتين، MNIST و CIFAR-10. اخترنا هاتين المهمتين لأنهما تعتمدان على مجموعات بيانات عامة ولهما سجل طويل في العمل كمعايير في تعلم الآلة. تشير تجربتنا إلى أن حماية الخصوصية للشبكات العصبية العميقة يمكن تحقيقها بتكلفة متواضعة من حيث تعقيد البرمجيات وكفاءة التدريب وجودة النموذج.

غالباً ما تتضمن أنظمة تعلم الآلة عناصر تساهم في حماية بيانات التدريب الخاصة بها. على وجه الخصوص، تقنيات التنظيم (regularization)، التي تهدف إلى تجنب الإفراط في التدريب على الأمثلة المستخدمة للتدريب، قد تخفي تفاصيل تلك الأمثلة. من ناحية أخرى، يُعد تفسير التمثيلات الداخلية في الشبكات العصبية العميقة صعباً بشكل معروف، وسعتها الكبيرة تعني أن هذه التمثيلات قد تشفر تفاصيل دقيقة لبعض بيانات التدريب على الأقل. في بعض الحالات، قد يتمكن خصم مصمم من استخراج أجزاء من بيانات التدريب. على سبيل المثال، أظهر Fredrikson وزملاؤه هجوم انعكاس النموذج (model-inversion attack) الذي يستعيد الصور من نظام التعرف على الوجوه.

بينما يتطلب هجوم انعكاس النموذج وصولاً من نوع "الصندوق الأسود" فقط إلى النموذج المدرب (أي التفاعل مع النموذج عبر المدخلات والمخرجات)، فإننا نأخذ في الاعتبار خصوماً بقدرات إضافية، مثل Shokri و Shmatikov. يقدم نهجنا حماية ضد خصم قوي لديه معرفة كاملة بآلية التدريب ووصول إلى معاملات النموذج.

هذه الحماية جذابة، بشكل خاص، لتطبيقات تعلم الآلة على الهواتف المحمولة والأجهزة اللوحية والأجهزة الأخرى. يتيح تخزين النماذج على الجهاز استنتاجاً موفراً للطاقة ومنخفض الكمون، وقد يساهم في الخصوصية لأن الاستنتاج لا يتطلب إرسال بيانات المستخدم إلى خادم مركزي؛ من ناحية أخرى، يجب أن نفترض أن معاملات النموذج نفسها قد تتعرض للفحص العدائي.

علاوة على ذلك، عندما نكون معنيين بالحفاظ على خصوصية سجل واحد في بيانات التدريب، نسمح بإمكانية أن يتحكم الخصم في بعض أو حتى كل بقية بيانات التدريب. في الممارسة العملية، لا يمكن دائماً استبعاد هذا الاحتمال، على سبيل المثال عندما يتم جمع البيانات من مصادر عامة.

يستعرض القسم التالي الخلفية حول التعلم العميق والخصوصية التفاضلية. يشرح القسمان 3 و 4 نهجنا وتنفيذه. يصف القسم 5 نتائجنا التجريبية. يناقش القسم 6 الأعمال ذات الصلة، ويختتم القسم 7.

---

### Translation Notes

- **Key concepts:**
  - Privacy-preserving machine learning with differential privacy
  - Moments accountant for tighter privacy bounds
  - Protection against strong adversaries with full model access
  - Trade-off between privacy budget and model quality

- **Technical terms:**
  - "crowdsourced" - جمع البيانات من مصادر عامة (descriptive translation)
  - "single-digit privacy budget" - ميزانية خصوصية "رقم أحادي" (kept in quotes for emphasis)
  - "higher moments" - العزوم الأعلى (statistical term)
  - "model-inversion attack" - هجوم انعكاس النموذج (security term)
  - "black-box access" - وصول "الصندوق الأسود" (kept in quotes as technical term)
  - "regularization" - التنظيم (established ML term)

- **Challenges:**
  - Balancing formal academic Arabic with technical accessibility
  - Maintaining precision in privacy and security terminology
  - Preserving the logical flow of arguments across paragraphs

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
