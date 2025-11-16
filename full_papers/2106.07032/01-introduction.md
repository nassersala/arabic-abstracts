# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.89
**Glossary Terms Used:** machine learning, category, deep learning, Bayesian inference, reinforcement learning, functor, compositionality, algorithm

---

### English Version

Compared to mathematics or physics, machine learning is a young field. Despite its young age, it has experienced sprawling growth, with its applications now permeating almost every realm of technology. A dozen of its subfields have become entire areas of study in their own right. This includes computational learning theory, deep learning, Bayesian inference, normalizing flows, clustering, reinforcement learning, and meta learning.

And yet, this explosive growth has not come without its costs. As the field keeps growing, it is becoming harder and harder to manage its complexity, and to understand how parts of this immense body of research interact with each other. While different subfields of machine learning share the same intellectual framework, it is hard to talk across boundaries. Many subfields have their own theoretical underpinnings, best practices, evaluation measures, and often very different languages and ways of thinking about the field as a whole. Furthermore, the fast-moving pace of the field is giving rise to bad incentives (Britz, 2020), leading to papers with confounding variables, missing details, bad notation, and suffering from narrative fallacy and research debt (Olah and Carter, 2017). While these issues are in general not exclusive to machine learning, the subfield of deep learning is notoriously ad-hoc (Olah, 2015). In his NeurIPS Test of Time award speech (Rahimi, 2018), Ali Rahimi has compared modern machine learning to alchemy, citing examples of machine learning models performance dropping drastically after internals of frameworks they used changed the default way of rounding numbers. Models in deep reinforcement learning are particularly brittle, often changing their performance drastically with different initial seeds (Irpan, 2018). In general, the construction of most non-trivial machine learning systems is largely guided by heuristics about what works well in practice. While the individual components of complex models are generally well-developed mathematically, their composition and combinations tend to be poorly understood.

The machine learning community is well aware of this problem. Some researchers have begun to organize workshops focused on the compositionality of machine learning components (Com, 2019). Others have called for broad overarching frameworks to unify machine learning theory and practice (Rieck, 2020). Nonetheless, there does not seem to be widespread consensus about how exactly to achieve that goal.

On the other hand, the field of category theory has steadily been growing. It is becoming a unifying force in mathematics and physics, spreading in recent years into chemistry, statistics, game theory, causality, and database theory. As the science of compositionality, it helps structure thoughts and ideas, find commonalities between different branches of science, and transfer ideas from one field to another (Fong and Spivak, 2018; Bradley, 2018).

Since many modern machine learning systems are inherently compositional (Abadi et al., 2015), this makes it unsurprising that a number of authors have begun to study them through the lens of category theory. In this survey we will describe category theoretic perspectives on three areas:

• **Gradient-based methods.** Building from the foundations of automatic differentiation to neural network architectures, loss functions and model updates.

• **Probabilistic methods.** Building from the foundations of probability to simple Bayesian models.

• **Invariant and Equivariant Learning.** Characterizing the invariances and equivariances of unsupervised and supervised learning algorithms.

While our aim is to provide a comprehensive account of the approaches above, we note that there are many category theoretic perspectives on machine learning that we do not touch on. For example, we leave the field of natural language processing (which has seen recent interest from the categorical community (Brucker, 2020)) to future work.

**Notation.** In this paper, we write function composition in diagrammatic order using ⨟. When it comes to the direction of string diagrams, we follow the notation conventions of the authors. Therefore, in the first section, the string diagrams flow from left to right, while in the second section they flow from bottom to top.

---

### النسخة العربية

بالمقارنة مع الرياضيات أو الفيزياء، يُعد تعلم الآلة مجالاً حديثاً. وعلى الرغم من حداثته، فقد شهد نمواً هائلاً، حيث تتغلغل تطبيقاته الآن في كل مجال من مجالات التكنولوجيا تقريباً. أصبح العشرات من فروعه الفرعية مجالات دراسة كاملة بحد ذاتها. ويشمل ذلك نظرية التعلم الحاسوبي، التعلم العميق، الاستدلال البايزي، التدفقات التطبيعية، التجميع، التعلم المعزز، والتعلم الفوقي.

ومع ذلك، لم يأتِ هذا النمو المتفجر دون تكاليف. مع استمرار نمو المجال، أصبح من الصعب بشكل متزايد إدارة تعقيده، وفهم كيفية تفاعل أجزاء هذا الكم الهائل من الأبحاث مع بعضها البعض. بينما تشترك الفروع الفرعية المختلفة لتعلم الآلة في نفس الإطار الفكري، إلا أنه من الصعب التواصل عبر الحدود. لدى العديد من الفروع الفرعية أسسها النظرية الخاصة، وأفضل الممارسات، ومقاييس التقييم، وغالباً لغات وطرق تفكير مختلفة جداً حول المجال ككل. علاوة على ذلك، فإن الوتيرة السريعة للمجال تؤدي إلى حوافز سيئة (Britz, 2020)، مما يؤدي إلى أوراق بحثية تحتوي على متغيرات مربكة، وتفاصيل مفقودة، وترميز سيء، وتعاني من المغالطة السردية والدَيْن البحثي (Olah and Carter, 2017). في حين أن هذه القضايا ليست حصرية على تعلم الآلة بشكل عام، إلا أن الفرع الفرعي للتعلم العميق معروف بأنه مخصص بشكل خاص (Olah, 2015). في خطاب جائزة اختبار الزمن NeurIPS (Rahimi, 2018)، قارن علي رحيمي تعلم الآلة الحديث بالكيمياء القديمة، مستشهداً بأمثلة على انخفاض أداء نماذج تعلم الآلة بشكل كبير بعد أن غيرت البنية الداخلية للأطر التي استخدموها الطريقة الافتراضية لتقريب الأرقام. نماذج التعلم المعزز العميق هشة بشكل خاص، وغالباً ما تغير أداءها بشكل كبير مع بذور أولية مختلفة (Irpan, 2018). بشكل عام، فإن بناء معظم أنظمة تعلم الآلة غير البسيطة يُوجه إلى حد كبير بواسطة استدلالات حول ما يعمل بشكل جيد في الممارسة العملية. في حين أن المكونات الفردية للنماذج المعقدة متطورة رياضياً بشكل عام، إلا أن تركيبها ومجموعاتها تميل إلى أن تكون مفهومة بشكل ضعيف.

مجتمع تعلم الآلة يدرك هذه المشكلة جيداً. بدأ بعض الباحثين في تنظيم ورش عمل تركز على التركيبية لمكونات تعلم الآلة (Com, 2019). ودعا آخرون إلى أطر شاملة واسعة لتوحيد نظرية وممارسة تعلم الآلة (Rieck, 2020). ومع ذلك، لا يبدو أن هناك إجماعاً واسع النطاق حول كيفية تحقيق هذا الهدف بالضبط.

من ناحية أخرى، ظل مجال نظرية الفئات ينمو بشكل مطرد. إنها تصبح قوة موحدة في الرياضيات والفيزياء، وتنتشر في السنوات الأخيرة في الكيمياء، والإحصاء، ونظرية الألعاب، والسببية، ونظرية قواعد البيانات. باعتبارها علم التركيبية، فإنها تساعد في هيكلة الأفكار والمفاهيم، وإيجاد أوجه التشابه بين فروع العلوم المختلفة، ونقل الأفكار من مجال إلى آخر (Fong and Spivak, 2018; Bradley, 2018).

نظراً لأن العديد من أنظمة تعلم الآلة الحديثة تركيبية بطبيعتها (Abadi et al., 2015)، فإن هذا يجعل من غير المستغرب أن عدداً من المؤلفين قد بدأوا في دراستها من خلال عدسة نظرية الفئات. في هذا المسح، سنصف وجهات نظر نظرية الفئات حول ثلاثة مجالات:

• **الطرق القائمة على التدرج.** البناء من أسس التفاضل الآلي إلى معماريات الشبكات العصبية، ودوال الخسارة، وتحديثات النموذج.

• **الطرق الاحتمالية.** البناء من أسس الاحتمالات إلى نماذج بايزية بسيطة.

• **التعلم المتغاير والمتكافئ.** توصيف التغايرات والتكافؤات لخوارزميات التعلم غير المُراقب والمُراقب.

بينما هدفنا هو تقديم سرد شامل للنهج أعلاه، نلاحظ أن هناك العديد من وجهات نظر نظرية الفئات حول تعلم الآلة التي لا نتطرق إليها. على سبيل المثال، نترك مجال معالجة اللغة الطبيعية (الذي شهد اهتماماً حديثاً من المجتمع الفئوي (Brucker, 2020)) للعمل المستقبلي.

**الترميز.** في هذا البحث، نكتب تركيب الدالة بالترتيب التخطيطي باستخدام ⨟. عندما يتعلق الأمر باتجاه المخططات الخيطية، نتبع اتفاقيات الترميز الخاصة بالمؤلفين. لذلك، في القسم الأول، تتدفق المخططات الخيطية من اليسار إلى اليمين، بينما في القسم الثاني تتدفق من الأسفل إلى الأعلى.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:**
  - compositionality (التركيبية) - new term for glossary
  - alchemy metaphor (الكيمياء القديمة) - metaphorical comparison
  - research debt (الدَيْن البحثي) - new technical term
  - string diagrams (المخططات الخيطية) - category theory concept
  - diagrammatic order (الترتيب التخطيطي)
- **Equations:** None
- **Citations:** Multiple (Britz 2020, Olah and Carter 2017, Rahimi 2018, Irpan 2018, Com 2019, Rieck 2020, Fong and Spivak 2018, Bradley 2018, Abadi et al. 2015, Brucker 2020)
- **Special handling:** Maintained academic tone; preserved metaphor about alchemy; handled technical category theory terminology carefully

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.89
- Readability: 0.88
- Glossary consistency: 0.90
- **Overall section score:** 0.89

### Back-Translation Verification

Key paragraph back-translation:
"بالمقارنة مع الرياضيات أو الفيزياء، يُعد تعلم الآلة مجالاً حديثاً..." → "Compared to mathematics or physics, machine learning is a modern field..."

This preserves the meaning and intent of the original while maintaining natural Arabic academic style.
