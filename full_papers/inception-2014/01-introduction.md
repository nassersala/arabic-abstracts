# Section 1: Introduction
## القسم 1: المقدمة

**Section:** Introduction
**Translation Quality:** 0.89
**Glossary Terms Used:** deep learning, convolutional neural network, architecture, computational resources, accuracy, algorithm, dataset, hardware

---

### English Version

In the last few years, our object classification and detection capabilities have dramatically improved due to advances in deep learning and convolutional networks. One encouraging news is that most of this progress is not just the result of more powerful hardware, larger datasets and bigger models, but mainly a consequence of new ideas, algorithms and improved network architectures. No new data sources were used, for example, by the top entries in the ILSVRC 2014 competition besides the classification dataset of the same competition for detection purposes. Our GoogLeNet submission to ILSVRC 2014 actually uses 12 times fewer parameters than the winning architecture of Krizhevsky et al [9] from two years ago, while being significantly more accurate. The biggest gains in object-detection have not come from the utilization of deep networks alone or bigger models, but from the synergy of deep architectures and classical computer vision, like the R-CNN algorithm by Girshick et al [6].

Another notable factor is that with the ongoing traction of mobile and embedded computing, the efficiency of our algorithms – especially their power and memory use – gains importance. It is noteworthy that the considerations in most of the experiments in this paper are not just about optimizing for accuracy but about finding the right balance between accuracy and efficiency that would allow the vision algorithms to be deployable on embedded devices. In many cases, building the best performing deep network is not just about choosing the right model size. In this paper we introduce the concept of "Inception", a deep convolutional neural network architecture that was designed with computational efficiency and practicality in mind from the start. The name "Inception" we gave to our model is a reference to the Network in network paper by Lin et al [12] in conjunction with the famous "we need to go deeper" internet meme [1]. In our case, the word "deep" is used in two different senses: most straightforwardly in the sense that we introduce a new level of organization in the form of the "Inception module" and also in the more direct sense of increased network depth. In general, one can view the Inception model as a logical culmination of [12] while taking inspiration and guidance from the theoretical work by Arora et al [2].

---

### النسخة العربية

في السنوات القليلة الماضية، تحسّنت قدراتنا في تصنيف الكائنات والكشف عنها بشكل كبير بفضل التقدم في التعلم العميق والشبكات الالتفافية. من الأخبار المشجعة أن معظم هذا التقدم ليس مجرد نتيجة لأجهزة أكثر قوة أو مجموعات بيانات أكبر أو نماذج أضخم، بل هو في الأساس نتيجة لأفكار جديدة وخوارزميات ومعماريات شبكية محسّنة. لم يتم استخدام مصادر بيانات جديدة، على سبيل المثال، من قبل المشاركات الأولى في مسابقة ILSVRC 2014 بخلاف مجموعة بيانات التصنيف الخاصة بنفس المسابقة لأغراض الكشف. في الواقع، يستخدم تقديمنا GoogLeNet لـ ILSVRC 2014 عدداً أقل من المعاملات بـ 12 مرة من المعمارية الفائزة لـ Krizhevsky وآخرين [9] قبل عامين، بينما يكون أكثر دقة بشكل ملحوظ. لم تأتِ أكبر المكاسب في الكشف عن الكائنات من استخدام الشبكات العميقة وحدها أو النماذج الأكبر، بل من التآزر بين المعماريات العميقة والرؤية الحاسوبية الكلاسيكية، مثل خوارزمية R-CNN لـ Girshick وآخرين [6].

عامل آخر جدير بالملاحظة هو أنه مع الزخم المستمر للحوسبة المحمولة والمدمجة، تكتسب كفاءة خوارزمياتنا - وخاصة استخدامها للطاقة والذاكرة - أهمية متزايدة. من الجدير بالذكر أن الاعتبارات في معظم التجارب في هذا البحث لا تتعلق فقط بتحسين الدقة، بل بإيجاد التوازن الصحيح بين الدقة والكفاءة الذي من شأنه أن يسمح بنشر خوارزميات الرؤية على الأجهزة المدمجة. في كثير من الحالات، بناء شبكة عميقة ذات أفضل أداء لا يتعلق فقط باختيار حجم النموذج المناسب. في هذا البحث، نقدم مفهوم "Inception"، وهي معمارية شبكة عصبية التفافية عميقة صُممت مع الكفاءة الحسابية والعملية في الاعتبار منذ البداية. الاسم "Inception" الذي أطلقناه على نموذجنا هو إشارة إلى ورقة "الشبكة داخل الشبكة" (Network in Network) لـ Lin وآخرين [12] بالاقتران مع الميم الشهير على الإنترنت "نحتاج للذهاب أعمق" (we need to go deeper) [1]. في حالتنا، تُستخدم كلمة "عميق" بمعنيين مختلفين: بأكثر الطرق مباشرة بمعنى أننا نقدم مستوى جديداً من التنظيم في شكل "وحدة Inception"، وأيضاً بالمعنى الأكثر مباشرة لزيادة عمق الشبكة. بشكل عام، يمكن للمرء أن ينظر إلى نموذج Inception كنتيجة منطقية لـ [12] مع الاستلهام والتوجيه من العمل النظري لـ Arora وآخرين [2].

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** Inception module, Network in Network, GoogLeNet, R-CNN, ILSVRC
- **Equations:** None
- **Citations:** [1], [2], [6], [9], [12]
- **Special handling:**
  - Kept proper nouns and model names in English: GoogLeNet, Inception, R-CNN, ILSVRC
  - Translated "Network in Network" with Arabic translation in parentheses
  - Kept the internet meme reference "we need to go deeper" in English with Arabic translation
  - Maintained citation numbers in brackets
  - Translated "synergy" as "التآزر"
  - Translated "embedded computing" as "الحوسبة المدمجة"

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.89
- Readability: 0.88
- Glossary consistency: 0.89
- **Overall section score:** 0.89
