# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** artificial intelligence, programming system, symbolic expressions, recursive functions, formalism, computation, machine

---

### English Version

**1. Introduction**

This paper describes a system for doing symbolic manipulation in a computer and presents a programming language designed for it. The motivation for this system and language was the desire to solve the problem of making a computer program mechanically deduce theorems in logic and mathematics, and exhibit "common sense" in carrying out its instructions. The key is being able to manipulate symbolic expressions in both their deductive and imperative aspects.

The system we have designed is called LISP, which stands for LISt Processor. It was developed for the IBM 704 computer at the M.I.T. Computation Center under the sponsorship of the Artificial Intelligence Project. The programming system was intended to facilitate experiments with a proposed system called the Advice Taker, whereby a machine would be instructed to handle both declarative sentences (facts and rules) and imperative sentences (commands to be executed).

The design of LISP was influenced by certain ideas from mathematical logic and recursive function theory. In this paper we shall describe a formalism for defining functions recursively, which has advantages both as a programming language and as a vehicle for developing a theory of computation. The basic data structure is the S-expression (symbolic expression), and the basic operations are S-functions that operate on S-expressions. This formalism provides a uniform way to represent both programs and data as S-expressions.

A distinctive feature of LISP is its ability to treat programs as data. Since both programs and data are represented as S-expressions, a LISP program can manipulate other LISP programs as well as ordinary data structures. This makes LISP particularly suitable for applications in artificial intelligence, where programs often need to reason about other programs or generate new programs.

The paper is organized as follows: We first introduce the concept of functions and function definitions in a general mathematical context. We then develop the theory of symbolic expressions (S-expressions) and functions on symbolic expressions (S-functions). Next, we describe how these concepts are realized in the LISP programming system for the IBM 704. We conclude by describing the universal S-function `apply`, which serves as an interpreter for LISP and plays a role analogous to the universal Turing machine in computability theory.

---

### النسخة العربية

**1. المقدمة**

تصف هذه الورقة نظامًا لإجراء المعالجة الرمزية في الحاسوب وتقدم لغة برمجية مصممة لهذا الغرض. كان الدافع وراء هذا النظام واللغة هو الرغبة في حل مشكلة جعل برنامج حاسوبي يستنتج النظريات في المنطق والرياضيات بشكل آلي، وأن يُظهر "الحس السليم" في تنفيذ تعليماته. المفتاح هو القدرة على معالجة التعبيرات الرمزية في جوانبها الاستنتاجية والأمرية.

النظام الذي صممناه يسمى LISP، وهو اختصار لـ LISt Processor (معالج القوائم). تم تطويره لحاسوب IBM 704 في مركز الحوسبة بمعهد ماساتشوستس للتكنولوجيا تحت رعاية مشروع الذكاء الاصطناعي. صُمم النظام البرمجي لتسهيل التجارب مع نظام مقترح يسمى Advice Taker (مُقدِّم النصيحة)، حيث يتم توجيه الآلة للتعامل مع كل من الجمل التصريحية (الحقائق والقواعد) والجمل الأمرية (الأوامر المراد تنفيذها).

تأثر تصميم LISP بأفكار معينة من المنطق الرياضي ونظرية الدوال العودية. في هذه الورقة سنصف شكلية لتعريف الدوال بشكل عودي، والتي لها مزايا كلغة برمجية وكوسيلة لتطوير نظرية الحساب. بنية البيانات الأساسية هي تعبير S (التعبير الرمزي)، والعمليات الأساسية هي دوال S التي تعمل على تعبيرات S. توفر هذه الشكلية طريقة موحدة لتمثيل كل من البرامج والبيانات كتعبيرات S.

من السمات المميزة لـ LISP قدرته على معاملة البرامج كبيانات. نظرًا لأن كلاً من البرامج والبيانات ممثلة كتعبيرات S، يمكن لبرنامج LISP معالجة برامج LISP أخرى بالإضافة إلى بنى البيانات العادية. وهذا يجعل LISP مناسبًا بشكل خاص للتطبيقات في الذكاء الاصطناعي، حيث غالبًا ما تحتاج البرامج إلى الاستدلال حول برامج أخرى أو توليد برامج جديدة.

تنظيم الورقة كما يلي: نقدم أولاً مفهوم الدوال وتعريفات الدوال في سياق رياضي عام. ثم نطور نظرية التعبيرات الرمزية (تعبيرات S) والدوال على التعبيرات الرمزية (دوال S). بعد ذلك، نصف كيفية تحقيق هذه المفاهيم في نظام البرمجة LISP لحاسوب IBM 704. نختتم بوصف دالة S العامة `apply`، التي تعمل كمفسر لـ LISP وتلعب دورًا مماثلاً لآلة تورينغ العامة في نظرية الحوسبة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** LISP, S-expression (تعبير S), S-function (دالة S), Advice Taker, symbolic manipulation (المعالجة الرمزية), recursive function (دالة عودية)
- **Equations:** None in this section
- **Citations:** Mentions Advice Taker project and AI context
- **Special handling:**
  - "LISP" kept in English as it's a proper name
  - "apply" kept in backticks as a function name
  - IBM 704 kept in English (product name)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.86
- Glossary consistency: 0.84
- **Overall section score:** 0.87
