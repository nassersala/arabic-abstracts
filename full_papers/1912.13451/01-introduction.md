# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** لغة البرمجة, مصفوفات, نموذج حسابي, نظام الأنواع, تعدد الأشكال, رتبة, إطار, خلية

---

### English Version

The rank-polymorphic programming model was developed by Kenneth Iverson, first for his array-programming language APL [2], and then later refined for its successor J [3]. We have subsequently designed a statically typed, higher-order functional language, Remora, based on the same computational model. The primary aim of this article is to introduce the reader, in a gradual, gentle way, to programming in Remora. We'll also discuss the pragmatics of Remora programming, in particular, how the parallel semantics of the language permits efficient code to be written for execution on parallel hardware. Finally, the design of Remora can serve as an introduction to the general model of computation that it embodies, which may make it easier to learn other languages in the class. A formal semantics for Remora, both its dynamic semantics and static type system, is presented in other work [5, 6].

Rank-polymorphic languages are known for not requiring explicit iteration or recursion constructs. Instead, the "iteration space" of a program is made real, or "reified," in the shape of its aggregate data structures: when a function that processes an individual element of this space is applied to such a data structure, it is automatically lifted by a general polymorphic mechanism to apply across all of the elements of the aggregate.

In this tutorial, we'll look at the three core mechanisms that exist in Remora that work together to constitute its control story¹:
• Frame polymorphism
• Principal-frame cell replication
• Reranking

The interplay of these mechanisms permits sophisticated Remora (or APL, or J) programmers to write programs that are startlingly succinct.

Additionally, we will explore Remora's static type system, which permits the language to describe, at compile time, the dimensions of the arrays computed by Remora programs. We'll begin this tutorial by avoiding any mention of static types; once the dynamic mechanisms of the language are understood, we'll move on to the issue of how to capture the shapes of arrays with a static semantics, in ways that respect the above three mechanisms.

¹ Other languages, such as Python, Matlab, or R, have ad hoc mechanisms that permit programmers to do some of the same things, but without the same generality and design integrity of languages centrally based on Iverson's computational model.

---

### النسخة العربية

تم تطوير النموذج الحسابي للبرمجة متعددة الأشكال حسب الرتبة بواسطة Kenneth Iverson، أولاً للغة البرمجة للمصفوفات APL [2]، ومن ثم تم تحسينها لاحقاً للغة خليفتها J [3]. لقد قمنا لاحقاً بتصميم لغة وظيفية عالية المستوى ذات كتابة ثابتة تدعى Remora، بناءً على نفس النموذج الحسابي. الهدف الأساسي من هذا المقال هو تقديم القارئ، بطريقة تدريجية ولطيفة، إلى البرمجة في Remora. سنناقش أيضاً عمليات البرمجة في Remora، خاصةً كيف تسمح الدلالات المتوازية للغة بكتابة كود فعال للتنفيذ على الأجهزة المتوازية. أخيراً، يمكن لتصميم Remora أن يعمل كمقدمة للنموذج العام للحساب الذي تجسده، مما قد يسهل تعلم اللغات الأخرى في هذه الفئة. يتم تقديم الدلالات الرسمية لـ Remora، سواء دلالاتها الديناميكية ونظام الأنواع الثابت، في أعمال أخرى [5, 6].

تُعرف اللغات متعددة الأشكال حسب الرتبة بأنها لا تتطلب بنى تكرار أو استدعاء ذاتي صريحة. بدلاً من ذلك، يتم جعل "فضاء التكرار" للبرنامج حقيقياً، أو "مُجسداً"، في شكل بنى البيانات المجمعة: عندما يتم تطبيق دالة تعالج عنصراً فردياً من هذا الفضاء على بنية بيانات كهذه، يتم رفعها تلقائياً بواسطة آلية عامة متعددة الأشكال لتطبيقها على جميع عناصر المجموع.

في هذا الدليل التعليمي، سننظر في ثلاث آليات أساسية موجودة في Remora والتي تعمل معاً لتشكل قصة التحكم الخاصة بها¹:
• تعدد أشكال الإطار (Frame polymorphism)
• نسخ خلايا الإطار الرئيسي (Principal-frame cell replication)
• إعادة الترتيب (Reranking)

يسمح التفاعل بين هذه الآليات للمبرمجين المتطورين في Remora (أو APL، أو J) بكتابة برامج موجزة بشكل مذهل.

بالإضافة إلى ذلك، سنستكشف نظام الأنواع الثابت في Remora، والذي يسمح للغة بوصف، في وقت الترجمة، أبعاد المصفوفات المحسوبة بواسطة برامج Remora. سنبدأ هذا الدليل التعليمي بتجنب أي ذكر للأنواع الثابتة؛ بمجرد فهم الآليات الديناميكية للغة، سننتقل إلى مسألة كيفية التقاط أشكال المصفوفات بدلالات ثابتة، بطرق تحترم الآليات الثلاث المذكورة أعلاه.

¹ اللغات الأخرى، مثل Python وMatlab وR، لديها آليات مخصصة تسمح للمبرمجين بفعل بعض الأشياء نفسها، لكن بدون نفس العمومية وتكامل التصميم للغات المبنية بشكل أساسي على النموذج الحسابي لـ Iverson.

---

### Translation Notes

- **Key terms introduced:**
  - rank-polymorphic (متعددة الأشكال حسب الرتبة)
  - array-programming (برمجة المصفوفات)
  - computational model (نموذج حسابي)
  - iteration space (فضاء التكرار)
  - reified (مُجسد)
  - frame polymorphism (تعدد أشكال الإطار)
  - cell replication (نسخ الخلايا)
  - reranking (إعادة الترتيب)
  - static type system (نظام أنواع ثابت)

- **References:** [2], [3], [5], [6] maintained as in original
- **Programming languages:** APL, J, Remora, Python, Matlab, R (kept in English)
- **Special handling:** Footnote preserved with same numbering

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87

### Back-Translation (First and Last Paragraphs)

The computational model for rank-polymorphic programming was developed by Kenneth Iverson, first for the array programming language APL [2], and was later refined for its successor language J [3]. We subsequently designed a higher-order functional language with static typing called Remora, based on the same computational model. The primary goal of this article is to introduce the reader, in a gradual and gentle way, to programming in Remora. We will also discuss programming operations in Remora, particularly how the parallel semantics of the language allow writing efficient code for execution on parallel hardware. Finally, Remora's design can serve as an introduction to the general computational model it embodies, which may make learning other languages in this class easier. The formal semantics for Remora, both its dynamic semantics and static type system, are presented in other works [5, 6].

Additionally, we will explore Remora's static type system, which allows the language to describe, at compile time, the dimensions of arrays computed by Remora programs. We will begin this tutorial by avoiding any mention of static types; once the dynamic mechanisms of the language are understood, we will move on to the issue of how to capture array shapes with static semantics, in ways that respect the three mechanisms mentioned above.
