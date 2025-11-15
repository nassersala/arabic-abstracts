# Section 1: Introduction - Conventional Programming Languages: Fat and Flabby
## القسم 1: المقدمة - لغات البرمجة التقليدية: منتفخة وضعيفة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** programming languages, functional programming, von Neumann computer, combining forms, algebra of programs, formal methods

---

### English Version

Conventional programming languages are growing ever more enormous, but not stronger. Inherent defects at the most basic level cause them to be both fat and weak: their primitive word-at-a-time style of programming inherited from their common ancestor—the von Neumann computer, their close coupling of semantics to state transitions, their division of programming into a world of expressions and a world of statements, their inability to effectively use powerful combining forms for building new programs from existing ones, and their lack of useful mathematical properties for reasoning about programs.

This paper describes a functional style of programming and a set of programming language features that support that style. The functional style is founded on the use of combining forms for creating programs. It emphasizes the applicative use of functions and, in particular, the use of functional forms that combine existing programs to form new ones. It maintains a sharp distinction between the world of functions and the world of objects.

The paper proposes an alternative to conventional languages in the form of FP systems, which are characterized by:

1. **Simplicity**: FP systems have a very simple syntax and semantics
2. **Function-level programming**: Operations work on entire functions rather than on their arguments
3. **Combining forms**: Fixed set of operators for combining programs
4. **Mathematical properties**: An algebra of programs for reasoning and transformation
5. **No variables**: Programs are built from functions without naming parameters

The structure of this paper is as follows: First, we discuss models of computing systems and the nature of conventional von Neumann computers and languages. Then we introduce functional programming systems (FP systems), describe their semantics, and demonstrate their use through examples. Next, we develop an algebra of programs for FP systems. We then describe formal functional programming (FFP) systems, which provide a formal framework for functional programming. Finally, we discuss applicative state transition (AST) systems as a way to combine functional programming with state.

The goal is to show that programming can indeed be liberated from the von Neumann style, and that a functional style offers significant advantages in terms of simplicity, mathematical tractability, and program construction through composition.

---

### النسخة العربية

تنمو لغات البرمجة التقليدية بشكل متزايد ضخامة، لكن ليس قوة. تتسبب عيوب متأصلة على المستوى الأساسي في جعلها منتفخة وضعيفة معاً: أسلوب البرمجة البدائي كلمة بكلمة الموروث من سلفها المشترك - حاسوب فون نيومان، والاقتران الوثيق بين الدلالات وانتقالات الحالة، وتقسيم البرمجة إلى عالم من التعبيرات وعالم من العبارات، وعدم قدرتها على استخدام أشكال التركيب القوية بفعالية لبناء برامج جديدة من برامج موجودة، وافتقارها إلى خصائص رياضية مفيدة للاستدلال حول البرامج.

تصف هذه الورقة نمطاً وظيفياً للبرمجة ومجموعة من ميزات لغات البرمجة التي تدعم هذا النمط. يتأسس النمط الوظيفي على استخدام أشكال التركيب لإنشاء البرامج. يُركز على الاستخدام التطبيقي للدوال، وبشكل خاص، استخدام الأشكال الوظيفية التي تجمع البرامج الموجودة لتشكيل برامج جديدة. يحافظ هذا النمط على تمييز واضح بين عالم الدوال وعالم الكائنات.

تقترح الورقة بديلاً للغات التقليدية في شكل أنظمة FP، التي تتميز بـ:

1. **البساطة**: تمتلك أنظمة FP بنية تركيبية ودلالات بسيطة جداً
2. **البرمجة على مستوى الدوال**: تعمل العمليات على دوال كاملة بدلاً من العمل على وسائطها
3. **أشكال التركيب**: مجموعة ثابتة من المعاملات لتركيب البرامج
4. **الخصائص الرياضية**: جبر للبرامج للاستدلال والتحويل
5. **بدون متغيرات**: تُبنى البرامج من دوال دون تسمية المعاملات

هيكل هذه الورقة كما يلي: أولاً، نناقش نماذج أنظمة الحوسبة وطبيعة حواسيب ولغات فون نيومان التقليدية. ثم نقدم أنظمة البرمجة الوظيفية (أنظمة FP)، ونصف دلالاتها، ونوضح استخدامها من خلال أمثلة. بعد ذلك، نطور جبراً للبرامج لأنظمة FP. ثم نصف أنظمة البرمجة الوظيفية الرسمية (أنظمة FFP)، التي توفر إطاراً رسمياً للبرمجة الوظيفية. وأخيراً، نناقش أنظمة الانتقال الحالي التطبيقية (أنظمة AST) كطريقة لدمج البرمجة الوظيفية مع الحالة.

الهدف هو إظهار أنه يمكن بالفعل تحرير البرمجة من نمط فون نيومان، وأن النمط الوظيفي يقدم مزايا كبيرة من حيث البساطة، وقابلية المعالجة الرياضية، وبناء البرامج من خلال التركيب.

---

### Translation Notes

- **Key terms introduced:**
  - fat and weak (منتفخة وضعيفة)
  - word-at-a-time (كلمة بكلمة)
  - combining forms (أشكال التركيب)
  - functional forms (الأشكال الوظيفية)
  - function-level programming (البرمجة على مستوى الدوال)
  - algebra of programs (جبر البرامج)
  - applicative use (الاستخدام التطبيقي)

- **Equations:** None
- **Citations:** None in introduction
- **Special handling:** Introduction sets up the main thesis and roadmap for the paper

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.86
- **Overall section score:** 0.87
