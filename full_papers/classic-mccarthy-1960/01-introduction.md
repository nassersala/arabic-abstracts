# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** programming system, artificial intelligence, declarative, imperative, formalism, recursive, symbolic expression, computation, interpreter, machine learning

---

### English Version

A programming system called LISP (for LISt Processor) has been developed for the IBM 704 computer by the Artificial Intelligence group at M.I.T. The system was designed to facilitate experiments with a proposed system called the Advice Taker, whereby a machine could be instructed to handle declarative as well as imperative sentences and could exhibit "common sense" in carrying out its instructions.

The Advice Taker is a proposed program for solving problems by manipulating sentences in formal languages. The main difference between the Advice Taker and other programs is that the Advice Taker will be told what to do rather than being programmed in detail. The advice and other information are to be given to the machine in a formal language, and a certain amount of built-in reasoning capacity is required to enable the machine to draw conclusions from the information it is given.

In order to do this, the main requirement is a programming system for manipulating expressions representing formalized declarative and imperative sentences so that the Advice Taker system could make deductions. This system should have the following properties:

1. **Universality:** A single mechanism should be able to carry out all processes that can be specified, and should provide a clear and simple notation for doing this.

2. **Flexibility:** It should be possible to change programs and data in similar and simple ways.

3. **Efficiency:** Where the same calculation is done repeatedly, it should be possible to arrange that it be done only once.

These objectives led to the development of the LISP system, which has a notation based on S-expressions (symbolic expressions) that can represent all computable functions. The key innovation is that both programs and data are represented as S-expressions, allowing programs to manipulate other programs as data.

The article describes a formalism for defining functions recursively, which has advantages both as a programming language and as a vehicle for developing a theory of computation. The rest of this paper is organized as follows: Section 2 describes recursive functions and their properties. Section 3 introduces S-expressions and their linear notation. Section 4 describes S-functions, which operate on S-expressions. Section 5 discusses the representation of S-expressions in computer memory. Section 6 introduces the universal S-function `apply`, which plays the theoretical role of a universal Turing machine and the practical role of an interpreter. Section 7 describes conditional expressions and their use in defining functions. Section 8 provides examples and applications.

---

### النسخة العربية

تم تطوير نظام برمجي يسمى LISP (اختصار لـ LISt Processor) لحاسوب IBM 704 من قبل مجموعة الذكاء الاصطناعي في معهد ماساتشوستس للتكنولوجيا. صُمم النظام لتسهيل التجارب مع نظام مقترح يسمى Advice Taker، حيث يمكن توجيه الآلة للتعامل مع الجمل التصريحية والأمرية ويمكنها إظهار "الحس السليم" في تنفيذ تعليماتها.

نظام Advice Taker هو برنامج مقترح لحل المسائل عن طريق معالجة الجمل في اللغات الرسمية. الفرق الرئيسي بين Advice Taker والبرامج الأخرى هو أن Advice Taker سيتم إخباره بما يجب فعله بدلاً من برمجته بالتفصيل. يتم تقديم النصائح والمعلومات الأخرى للآلة بلغة رسمية، ويتطلب ذلك قدراً معيناً من القدرة الاستدلالية المدمجة لتمكين الآلة من استخلاص الاستنتاجات من المعلومات المقدمة لها.

لتحقيق هذا الهدف، كان المتطلب الرئيسي هو نظام برمجي لمعالجة التعبيرات التي تمثل الجمل التصريحية والأمرية الرسمية بحيث يمكن لنظام Advice Taker إجراء الاستنتاجات. يجب أن يتمتع هذا النظام بالخصائص التالية:

1. **العمومية (Universality):** يجب أن تكون آلية واحدة قادرة على تنفيذ جميع العمليات التي يمكن تحديدها، ويجب أن توفر تدويناً واضحاً وبسيطاً للقيام بذلك.

2. **المرونة (Flexibility):** يجب أن يكون من الممكن تغيير البرامج والبيانات بطرق مماثلة وبسيطة.

3. **الكفاءة (Efficiency):** حيث يتم إجراء نفس الحساب بشكل متكرر، يجب أن يكون من الممكن ترتيب الأمور بحيث يتم إجراؤه مرة واحدة فقط.

أدت هذه الأهداف إلى تطوير نظام LISP، الذي يحتوي على تدوين يعتمد على تعبيرات S (التعبيرات الرمزية) التي يمكنها تمثيل جميع الدوال القابلة للحوسبة. الابتكار الرئيسي هو أن كلاً من البرامج والبيانات يتم تمثيلها كتعبيرات S، مما يسمح للبرامج بمعالجة برامج أخرى كبيانات.

تصف المقالة شكلية لتعريف الدوال بشكل عودي، والتي لها مزايا كلغة برمجة وكوسيلة لتطوير نظرية الحساب. ينظم بقية هذا البحث على النحو التالي: يصف القسم 2 الدوال العودية وخصائصها. يقدم القسم 3 تعبيرات S وتدوينها الخطي. يصف القسم 4 دوال S، التي تعمل على تعبيرات S. يناقش القسم 5 تمثيل تعبيرات S في ذاكرة الحاسوب. يقدم القسم 6 دالة S العامة `apply`، التي تلعب الدور النظري لآلة تورينغ العامة والدور العملي للمفسر. يصف القسم 7 التعبيرات الشرطية واستخدامها في تعريف الدوال. يقدم القسم 8 أمثلة وتطبيقات.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** LISP, LISt Processor, Advice Taker, S-expressions, symbolic expressions, recursive functions, universality, flexibility, efficiency, universal Turing machine, interpreter, computable functions
- **Equations:** None
- **Citations:** None in this section
- **Special handling:**
  - "LISP" kept in English (standard name)
  - "Advice Taker" kept in English (proper name)
  - "S-expressions" translated as "تعبيرات S"
  - "apply" kept in English (core function name)
  - Technical properties (Universality, Flexibility, Efficiency) given in both languages
  - Paper structure described for reader orientation

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.86
- **Overall section score:** 0.87
