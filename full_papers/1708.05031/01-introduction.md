# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** recommender system, collaborative filtering, matrix factorization, neural network, deep learning, latent feature, inner product, implicit feedback, framework, multi-layer perceptron, state-of-the-art, data, architecture

---

### English Version

In the era of information explosion, recommender systems play a pivotal role in alleviating information overload, having been widely adopted by many online services, including e-commerce, online news and social media sites. The key to a personalized recommender system is in modelling users' preference on items based on their past interactions (e.g., ratings, clicks). Among the various collaborative filtering techniques developed, matrix factorization (MF) is the most popular one, which projects users and items into a shared latent space, using a vector of latent features to represent a user or an item. Thereafter, a user's interaction on an item is modelled as the inner product of their latent vectors.

Benefited from the high effectiveness and simplicity of inner product, MF has been extensively studied and become the de facto method for latent factor modelling of collaborative filtering. However, the performance of MF can be easily hindered by the simple choice of the interaction function – inner product. For example, for the task of rating prediction, it is well known that the performance of MF can be improved by incorporating user and item bias terms into the interaction function. While it addresses the prediction of rating in collaborative filtering to some extent, we argue that the inner product, which simply combines the multiplication of latent features linearly, may not be sufficient to capture the complex structure of user interaction data.

In this work, we address this limitation of MF by learning the interaction function from data using neural networks. Neural networks have been proven to be able of approximating any continuous function, and have recently revolutionized many research areas including speech recognition, computer vision and natural language processing. However, there is relatively less work on using neural networks to address the key problem in collaborative filtering – modelling the interaction between user and item features based on implicit feedback.

By replacing the inner product with a neural architecture that can learn an arbitrary function from data, we present a general framework named NCF, short for Neural network-based Collaborative Filtering. NCF is generic and can express and generalize matrix factorization under its framework. To supercharge NCF modelling with non-linearities, we propose to leverage a multi-layer perceptron to learn the user-item interaction function. Extensive experiments on two real-world datasets show significant improvements of our proposed NCF framework over the state-of-the-art methods. Empirical evidence shows that using deeper layers of neural networks offers better recommendation performance.

The main contributions of this work are threefold:
1) We present a neural network architecture for collaborative filtering, named NCF, to model user-item interactions. Unlike traditional neural recommender systems that use neural networks to model auxiliary information, NCF models the user-item interaction directly.
2) We show that matrix factorization can be interpreted as a specialization of NCF, and leverage a multi-layer perceptron to endow NCF with a high level of non-linearities.
3) We perform extensive experiments on two real-world datasets to demonstrate the effectiveness of the NCF approach and the promise of deep learning for collaborative filtering.

---

### النسخة العربية

في عصر الانفجار المعلوماتي، تلعب أنظمة التوصية دوراً محورياً في تخفيف عبء المعلومات الزائدة، وقد تم اعتمادها على نطاق واسع من قبل العديد من الخدمات عبر الإنترنت، بما في ذلك التجارة الإلكترونية ومواقع الأخبار عبر الإنترنت ووسائل التواصل الاجتماعي. يكمن مفتاح نظام التوصية الشخصي في نمذجة تفضيلات المستخدمين للعناصر بناءً على تفاعلاتهم السابقة (مثل التقييمات والنقرات). من بين تقنيات التصفية التعاونية المختلفة التي تم تطويرها، يعد تحليل المصفوفات الأكثر شيوعاً، والذي يقوم بإسقاط المستخدمين والعناصر في فضاء كامن مشترك، باستخدام متجه من الميزات الكامنة لتمثيل مستخدم أو عنصر. بعد ذلك، يتم نمذجة تفاعل المستخدم مع العنصر على أنه حاصل الضرب الداخلي لمتجهاتهم الكامنة.

بفضل الفعالية العالية والبساطة لحاصل الضرب الداخلي، تمت دراسة تحليل المصفوفات على نطاق واسع وأصبح الطريقة القياسية لنمذجة العوامل الكامنة في التصفية التعاونية. ومع ذلك، يمكن أن يتعرقل أداء تحليل المصفوفات بسهولة بسبب الاختيار البسيط لدالة التفاعل – حاصل الضرب الداخلي. على سبيل المثال، بالنسبة لمهمة التنبؤ بالتقييم، من المعروف جيداً أن أداء تحليل المصفوفات يمكن تحسينه من خلال دمج حدود الانحياز للمستخدم والعنصر في دالة التفاعل. في حين أن هذا يعالج التنبؤ بالتقييم في التصفية التعاونية إلى حد ما، فإننا نزعم أن حاصل الضرب الداخلي، الذي يجمع ببساطة بين ضرب الميزات الكامنة بشكل خطي، قد لا يكون كافياً لالتقاط البنية المعقدة لبيانات تفاعل المستخدم.

في هذا العمل، نعالج هذا القيد في تحليل المصفوفات من خلال تعلم دالة التفاعل من البيانات باستخدام الشبكات العصبية. لقد ثبت أن الشبكات العصبية قادرة على تقريب أي دالة مستمرة، وقد أحدثت مؤخراً ثورة في العديد من مجالات البحث بما في ذلك التعرف على الكلام ورؤية حاسوبية ومعالجة اللغة الطبيعية. ومع ذلك، هناك عمل أقل نسبياً على استخدام الشبكات العصبية لمعالجة المشكلة الأساسية في التصفية التعاونية – نمذجة التفاعل بين ميزات المستخدم والعنصر بناءً على التغذية الراجعة الضمنية.

من خلال استبدال حاصل الضرب الداخلي بمعمارية عصبية يمكنها تعلم دالة تعسفية من البيانات، نقدم إطار عمل عام يُدعى NCF، اختصار للتصفية التعاونية القائمة على الشبكات العصبية. إن NCF عام ويمكنه التعبير عن تحليل المصفوفات وتعميمه في إطار عمله. لتعزيز نمذجة NCF باللاخطيات، نقترح الاستفادة من الشبكات الإدراكية متعددة الطبقات لتعلم دالة التفاعل بين المستخدم والعنصر. أظهرت تجارب واسعة على مجموعتي بيانات من العالم الحقيقي تحسينات كبيرة في إطار عمل NCF المقترح مقارنة بأحدث الطرق. تُظهر الأدلة التجريبية أن استخدام طبقات أعمق من الشبكات العصبية يقدم أداء توصية أفضل.

المساهمات الرئيسية لهذا العمل ثلاثية:
1) نقدم معمارية شبكة عصبية للتصفية التعاونية، تُدعى NCF، لنمذجة تفاعلات المستخدم والعنصر. على عكس أنظمة التوصية العصبية التقليدية التي تستخدم الشبكات العصبية لنمذجة المعلومات المساعدة، تقوم NCF بنمذجة تفاعل المستخدم والعنصر مباشرة.
2) نُظهر أن تحليل المصفوفات يمكن تفسيره على أنه حالة خاصة من NCF، ونستفيد من الشبكات الإدراكية متعددة الطبقات لتزويد NCF بمستوى عالٍ من اللاخطيات.
3) نجري تجارب واسعة على مجموعتي بيانات من العالم الحقيقي لإثبات فعالية نهج NCF وإمكانات تعلم عميق للتصفية التعاونية.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** NCF (Neural network-based Collaborative Filtering), matrix factorization (MF), inner product, latent features, user-item interaction, implicit feedback, multi-layer perceptron (MLP)
- **Equations:** None in introduction
- **Citations:** References mentioned but specific numbers not available in extracted text
- **Special handling:**
  - Acronym NCF maintained in English with Arabic translation
  - Technical term "de facto method" translated as "الطريقة القياسية" (standard method)
  - Three-fold contribution list formatted as numbered list in both languages

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87

### Methodology Note
This translation was created from content extracted from multiple sources including the arXiv HTML version and academic databases, as direct PDF text extraction was not available through current tools.
