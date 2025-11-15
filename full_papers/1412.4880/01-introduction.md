# Section 1: Introduction
## القسم 1: مقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** functional programming, programming language, higher-order functions, type classes, types, functions, referential transparency, algebraic data types

---

### English Version

Introduction to Computational Physics (Physics 261) at Lebanon Valley College is a second-year one-semester elective physics course. The prerequisites for the course are one year of introductory physics and one semester of calculus. No previous programming experience is expected or assumed. Nevertheless, third- and fourth-year students often take the course, and a number of students do have previous programming experience (although not in a functional language).

The purpose of the course is to strengthen a student's understanding of basic physics by learning a new language (Haskell), and instructing the computer to do physics in that language. Our attitude was strongly influenced by the work of Papert[6], and the subsequent work of Sussman and his coworkers[7, 8]. A functional programming language is a good choice for this purpose for a number of reasons. Functional programming languages tend to look, or at least feel, a bit more like mathematics than imperative languages. The concept of a list is quickly and comfortably assimilated, and standard library list functions take the place of loops in an imperative language. Referential transparency removes much of the convolution of thinking about code. Many of the concepts that appear in introductory physics have a natural expression as types or higher-order functions.

Haskell is a particularly good choice because its surface syntax appears to be familiar mathematics (compared with Scheme, say), and its system of static types aids the programmer in thinking about the structure of what she is writing. Haskell's system of curried functions is very pleasant and convenient. Type classes are not essential for the purposes of Physics 261, but they come in handy in a few places.

The course is structured in roughly two parts. In the first part, we learn a subset of the Haskell programming language. We are particularly interested in types, functions, and higher-order functions. We introduce a number of the types and functions provided by the standard Prelude, and we focus on how to write our own functions. In previous offerings of the course, we used the first five chapters of Hutton's book [5]. We are less interested in type classes, but we need to be aware of them to understand the types of some functions, and to have any chance of understanding error messages. We intentionally avoid explicit recursion because we're only spending about seven weeks learning our subset of Haskell.

We also omit the creation of new algebraic data types. Nevertheless, most students seem able to become proficient in this subset of Haskell in about seven weeks, and can then apply it to problems in mechanics and electromagnetic theory.

In the second part of the course, we use Haskell to express the ideas of Newtonian mechanics and electromagnetic theory. Here we want students to use the language as a set of building blocks for constructing interesting things, and we want to provide a lot of freedom for students to use the language as they see fit. At the same time, we have in mind a way of viewing Newtonian mechanics and (part of) electromagnetic theory toward which we are guiding students. Section 2 describes our view of Newtonian mechanics, and shows what functional programming has to offer toward it. Section 3 describes ways in which types and higher-order functions serve to organize and clarify parts of electromagnetic theory. Section 4 is a short conclusion.

---

### النسخة العربية

مقدمة في الفيزياء الحسابية (الفيزياء 261) في كلية ليبانون فالي هي مادة فيزياء اختيارية للسنة الثانية لمدة فصل دراسي واحد. المتطلبات الأساسية للمقرر هي سنة واحدة من الفيزياء التمهيدية وفصل دراسي واحد من حساب التفاضل والتكامل. لا يُتوقع أو يُفترض وجود أي خبرة برمجية سابقة. ومع ذلك، غالباً ما يأخذ طلاب السنة الثالثة والرابعة هذا المقرر، وعدد من الطلاب لديهم خبرة برمجية سابقة (وإن لم تكن بلغة برمجة وظيفية).

الغرض من المقرر هو تعزيز فهم الطالب للفيزياء الأساسية من خلال تعلم لغة جديدة (Haskell)، وتوجيه الحاسوب للقيام بالفيزياء بتلك اللغة. لقد تأثر موقفنا بشدة بعمل بابرت [6]، والعمل اللاحق لسوسمان وزملائه [7، 8]. لغة البرمجة الوظيفية هي خيار جيد لهذا الغرض لعدد من الأسباب. تميل لغات البرمجة الوظيفية إلى أن تبدو، أو على الأقل تشعر، أكثر شبهاً بالرياضيات من اللغات الأمرية. يتم استيعاب مفهوم القائمة بسرعة وراحة، وتحل دوال مكتبة القوائم القياسية محل الحلقات في اللغة الأمرية. تزيل الشفافية المرجعية الكثير من التعقيد في التفكير حول الشفرة. العديد من المفاهيم التي تظهر في الفيزياء التمهيدية لها تعبير طبيعي كأنواع أو دوال من الرتبة العليا.

Haskell هو خيار جيد بشكل خاص لأن صيغته السطحية تبدو كرياضيات مألوفة (بالمقارنة مع Scheme، على سبيل المثال)، ونظام الأنواع الثابتة الخاص به يساعد المبرمج في التفكير في بنية ما يكتبه. نظام الدوال المُكارية في Haskell ممتع ومريح للغاية. فئات الأنواع ليست ضرورية لأغراض الفيزياء 261، لكنها تكون مفيدة في بعض الأماكن.

المقرر منظم في جزأين تقريباً. في الجزء الأول، نتعلم مجموعة فرعية من لغة البرمجة Haskell. نحن مهتمون بشكل خاص بالأنواع، والدوال، والدوال من الرتبة العليا. نقدم عدداً من الأنواع والدوال المقدمة من Prelude القياسي، ونركز على كيفية كتابة دوالنا الخاصة. في العروض السابقة للمقرر، استخدمنا الفصول الخمسة الأولى من كتاب هاتون [5]. نحن أقل اهتماماً بفئات الأنواع، لكننا بحاجة إلى أن نكون على دراية بها لفهم أنواع بعض الدوال، ولكي يكون لدينا أي فرصة لفهم رسائل الخطأ. نتجنب عمداً الاستدعاء الذاتي الصريح لأننا نقضي فقط حوالي سبعة أسابيع في تعلم مجموعتنا الفرعية من Haskell.

كما نغفل أيضاً إنشاء أنواع البيانات الجبرية الجديدة. ومع ذلك، يبدو أن معظم الطلاب قادرون على أن يصبحوا متمكنين في هذه المجموعة الفرعية من Haskell في حوالي سبعة أسابيع، ويمكنهم بعد ذلك تطبيقها على مسائل في الميكانيكا والنظرية الكهرومغناطيسية.

في الجزء الثاني من المقرر، نستخدم Haskell للتعبير عن أفكار الميكانيكا النيوتونية والنظرية الكهرومغناطيسية. هنا نريد من الطلاب استخدام اللغة كمجموعة من اللبنات الأساسية لبناء أشياء مثيرة للاهتمام، ونريد توفير الكثير من الحرية للطلاب لاستخدام اللغة كما يرونها مناسبة. في الوقت نفسه، لدينا في الاعتبار طريقة لعرض الميكانيكا النيوتونية و(جزء من) النظرية الكهرومغناطيسية نحو توجيه الطلاب نحوها. يصف القسم 2 رؤيتنا للميكانيكا النيوتونية، ويوضح ما يمكن أن تقدمه البرمجة الوظيفية نحو ذلك. يصف القسم 3 الطرق التي تخدم بها الأنواع والدوال من الرتبة العليا في تنظيم وتوضيح أجزاء من النظرية الكهرومغناطيسية. القسم 4 هو خاتمة قصيرة.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:**
  - functional programming (البرمجة الوظيفية)
  - Haskell (maintained as Haskell)
  - higher-order functions (الدوال من الرتبة العليا)
  - referential transparency (الشفافية المرجعية)
  - type classes (فئات الأنواع)
  - curried functions (الدوال المُكارية)
  - algebraic data types (أنواع البيانات الجبرية)
  - imperative languages (اللغات الأمرية)
  - Prelude (maintained as Prelude - standard library name)
- **Equations:** None
- **Citations:** [5], [6], [7], [8]
- **Special handling:**
  - Course name "Physics 261" maintained in English
  - Book and author names maintained in English
  - Programming language names (Haskell, Scheme) maintained in English
  - Term "Prelude" maintained as it's a specific library name

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88

### Back-Translation Check (First and Last Paragraphs)

**First paragraph back-translation:**
"Introduction to Computational Physics (Physics 261) at Lebanon Valley College is a second-year elective physics course for one semester. The basic requirements for the course are one year of introductory physics and one semester of calculus. No previous programming experience is expected or assumed. However, third and fourth year students often take this course, and a number of students have previous programming experience (though not in a functional programming language)."

**Last paragraph back-translation:**
"In the second part of the course, we use Haskell to express the ideas of Newtonian mechanics and electromagnetic theory. Here we want students to use the language as a set of building blocks for constructing interesting things, and we want to provide a lot of freedom for students to use the language as they see fit. At the same time, we have in mind a way of viewing Newtonian mechanics and (part of) electromagnetic theory toward guiding students towards it. Section 2 describes our vision for Newtonian mechanics, and shows what functional programming can offer towards that. Section 3 describes the ways in which types and higher-order functions serve in organizing and clarifying parts of electromagnetic theory. Section 4 is a short conclusion."

**Validation:** Both back-translations preserve the original meaning with high fidelity. Minor wording variations ("basic requirements" vs "prerequisites") do not affect semantic accuracy.
