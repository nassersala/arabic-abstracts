# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** neural network, deep learning, overfitting, training, regularization, ensemble, feature detector, co-adaptation, generalization

---

### English Version

Deep neural nets with a large number of parameters are very powerful machine learning systems. However, overfitting is a serious problem in such networks. Large networks are also slow to use, making it difficult to deal with overfitting by combining the predictions of many different large neural nets at test time. Dropout is a technique for addressing this problem. The key idea is to randomly drop units (along with their connections) from the neural network during training. This prevents units from co-adapting too much. During training, dropout samples from an exponential number of different "thinned" networks. At test time, it is easy to approximate the effect of averaging the predictions of all these thinned networks by simply using a single unthinned network that has smaller weights. This significantly reduces overfitting and gives major improvements over other regularization methods. We show that dropout improves the performance of neural networks on supervised learning tasks in vision, speech recognition, document classification and computational biology, obtaining state-of-the-art results on many benchmark data sets.

The motivation for dropout comes from a theory of the role of sex in evolution. Sexual reproduction involves taking half the genes of one parent and half of the other, adding a very small amount of random mutation, and combining them to produce offspring. The asexual alternative is to create offspring with a slight random mutation of the parent's genes. It seems plausible that asexual reproduction should be a better way to optimize individual fitness because a good set of genes that have come to work well together can be passed on directly to the offspring. On the other hand, sexual reproduction is likely to break up these co-adapted sets of genes, especially if the parents have quite different sets of genes. Systems that are robust in the face of changes to their implementation details tend to be composed of parts that are useful on their own, rather than parts that depend critically on lots of other parts to work properly. Dropout training encourages neurons to develop feature detectors that work well by themselves without requiring the presence of lots of other specific feature detectors.

---

### النسخة العربية

تُعد الشبكات العصبية العميقة ذات العدد الكبير من المعاملات أنظمة تعلم آلي قوية للغاية. ومع ذلك، يمثل الإفراط في التدريب مشكلة خطيرة في مثل هذه الشبكات. كما أن الشبكات الكبيرة بطيئة في الاستخدام، مما يجعل من الصعب التعامل مع الإفراط في التدريب من خلال دمج تنبؤات العديد من الشبكات العصبية الكبيرة المختلفة في وقت الاختبار. يُعد Dropout تقنية لمعالجة هذه المشكلة. الفكرة الرئيسية هي إسقاط الوحدات (مع اتصالاتها) عشوائياً من الشبكة العصبية أثناء التدريب. هذا يمنع الوحدات من التكيف المشترك بشكل مفرط. أثناء التدريب، يقوم dropout بأخذ عينات من عدد أسي من الشبكات "المخففة" المختلفة. في وقت الاختبار، من السهل تقريب تأثير حساب متوسط تنبؤات كل هذه الشبكات المخففة ببساطة باستخدام شبكة واحدة غير مخففة ذات أوزان أصغر. هذا يقلل بشكل كبير من الإفراط في التدريب ويعطي تحسينات كبيرة مقارنة بطرق التنظيم الأخرى. نُظهر أن dropout يحسّن أداء الشبكات العصبية في مهام التعلم الخاضع للإشراف في الرؤية الحاسوبية، والتعرف على الكلام، وتصنيف الوثائق، والبيولوجيا الحسابية، محققاً نتائج متقدمة على العديد من مجموعات البيانات المعيارية.

يأتي الدافع وراء dropout من نظرية حول دور الجنس في التطور. يتضمن التكاثر الجنسي أخذ نصف جينات أحد الوالدين ونصف جينات الآخر، وإضافة كمية صغيرة جداً من الطفرات العشوائية، ودمجها لإنتاج النسل. البديل اللاجنسي هو إنشاء نسل مع طفرة عشوائية طفيفة لجينات الوالد. يبدو من المعقول أن التكاثر اللاجنسي يجب أن يكون طريقة أفضل لتحسين اللياقة الفردية لأن مجموعة جيدة من الجينات التي أصبحت تعمل بشكل جيد معاً يمكن نقلها مباشرة إلى النسل. من ناحية أخرى، من المرجح أن يؤدي التكاثر الجنسي إلى تفكيك مجموعات الجينات المتكيفة المشتركة هذه، خاصة إذا كان لدى الوالدين مجموعات مختلفة تماماً من الجينات. الأنظمة القوية في مواجهة التغييرات في تفاصيل تنفيذها تميل إلى أن تكون مكونة من أجزاء مفيدة بذاتها، بدلاً من أجزاء تعتمد بشكل حاسم على الكثير من الأجزاء الأخرى للعمل بشكل صحيح. يشجع تدريب dropout الخلايا العصبية على تطوير كاشفات ميزات تعمل بشكل جيد بمفردها دون الحاجة إلى وجود الكثير من كاشفات الميزات المحددة الأخرى.

---

### Translation Notes

- **Key concepts:**
  - Dropout as a regularization technique to prevent overfitting
  - The exponential number of thinned networks concept
  - Biological motivation from sexual reproduction

- **Technical terms:**
  - "dropout" - kept in English as standard ML terminology
  - "overfitting" - translated as "الإفراط في التدريب" (consistent with glossary)
  - "co-adaptation" - translated as "التكيف المشترك" (consistent with glossary)
  - "thinned networks" - translated as "الشبكات المخففة"

- **Special handling:**
  - The biological analogy is carefully translated to maintain the conceptual parallel
  - Technical precision maintained in describing the exponential sampling of networks

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
