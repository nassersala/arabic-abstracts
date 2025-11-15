# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.88
**Glossary Terms Used:** neural network, deep learning, computer vision, natural language, collaborative, matrix, factorization, architecture, function, data, framework, multi-layer perceptron, interaction, dataset, layer, performance, speech recognition, state-of-the-art, recommender system, implicit feedback, inner product, latent feature, user-item interaction, non-linearity

---

### English Version

In recent years, deep neural networks have yielded immense success on speech recognition, computer vision and natural language processing. However, the exploration of deep neural networks on recommender systems has received relatively less scrutiny. In this work, we strive to develop techniques based on neural networks to tackle the key problem in recommendation -- collaborative filtering -- on the basis of implicit feedback. Although some recent work has employed deep learning for recommendation, they primarily used it to model auxiliary information, such as textual descriptions of items and acoustic features of musics. When it comes to model the key factor in collaborative filtering -- the interaction between user and item features, they still resorted to matrix factorization and applied an inner product on the latent features of users and items. By replacing the inner product with a neural architecture that can learn an arbitrary function from data, we present a general framework named NCF, short for Neural network-based Collaborative Filtering. NCF is generic and can express and generalize matrix factorization under its framework. To supercharge NCF modelling with non-linearities, we propose to leverage a multi-layer perceptron to learn the user-item interaction function. Extensive experiments on two real-world datasets show significant improvements of our proposed NCF framework over the state-of-the-art methods. Empirical evidence shows that using deeper layers of neural networks offers better recommendation performance.

---

### النسخة العربية

في السنوات الأخيرة، حققت الشبكات العصبية العميقة نجاحاً هائلاً في التعرف على الكلام ورؤية حاسوبية ومعالجة اللغة الطبيعية. ومع ذلك، فإن استكشاف الشبكات العصبية العميقة في أنظمة التوصية لم يحظ بالاهتمام الكافي. في هذا العمل، نسعى إلى تطوير تقنيات قائمة على الشبكات العصبية لمعالجة المشكلة الأساسية في التوصية -- وهي التصفية التعاونية -- على أساس التغذية الراجعة الضمنية. على الرغم من أن بعض الأعمال الحديثة استخدمت تعلم عميق للتوصية، إلا أنها استخدمته بشكل أساسي لنمذجة المعلومات المساعدة، مثل الأوصاف النصية للعناصر والميزات الصوتية للموسيقى. وعندما يتعلق الأمر بنمذجة العامل الرئيسي في التصفية التعاونية -- وهو التفاعل بين ميزات المستخدم والعنصر -- فإنها لا تزال تلجأ إلى تحليل المصفوفات وتطبيق حاصل الضرب الداخلي على الميزات الكامنة للمستخدمين والعناصر. من خلال استبدال حاصل الضرب الداخلي بمعمارية عصبية يمكنها تعلم دالة تعسفية من البيانات، نقدم إطار عمل عام يُدعى NCF، اختصار للتصفية التعاونية القائمة على الشبكات العصبية. إن NCF عام ويمكنه التعبير عن تحليل المصفوفات وتعميمه في إطار عمله. لتعزيز نمذجة NCF باللاخطيات، نقترح الاستفادة من الشبكات الإدراكية متعددة الطبقات لتعلم دالة التفاعل بين المستخدم والعنصر. أظهرت تجارب واسعة على مجموعتي بيانات من العالم الحقيقي تحسينات كبيرة في إطار عمل NCF المقترح مقارنة بأحدث الطرق. تُظهر الأدلة التجريبية أن استخدام طبقات أعمق من الشبكات العصبية يقدم أداء توصية أفضل.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:** NCF (Neural network-based Collaborative Filtering), collaborative filtering, implicit feedback, matrix factorization, user-item interaction
- **Equations:** None
- **Citations:** None
- **Special handling:** Acronym NCF kept in both English and explained in Arabic

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
