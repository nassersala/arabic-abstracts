# Section 7: Optional Homework Questions
## القسم 7: أسئلة واجب اختيارية

**Section:** homework questions
**Translation Quality:** 0.86
**Glossary Terms Used:** program, computable, theorem, proof, ordering

---

### English Version

1. In two places in the proofs, ties in the lengths of strings are broken lexicographically. I claim that this detail is not needed in either place. Is this true?

2. In the proof of Theorem 2.1, what is the point of requiring the computer programs to be listed in order of their lengths? Would the given proof of Theorem 2.1 remain correct if the programs were (somehow) listed in no predictable order?

3. In program $P^*$, what is the point of requiring program $P$ to generate strings in order of their lengths? Would the given proof of Theorem 4.1 remain correct if $P$ did not generate the strings in that order, but could (somehow) generate all the strings in no predictable order?

4. Doesn't the following approach show that $\overline{f}(x)$ is computable?

First, create a computer program $P'$ that can look at a string $s$ over the finite alphabet used for computer programs (in some fixed computer language, for example, C), and determine if $s$ is a legal computer program that computes a function $f$ in $Q$. Certainly, a compiler for C can check if $s$ is a syntactically correct program in C.

Then given any positive integer $x$, use program $P$ to generate the strings over the finite alphabet used for computer programs, in order of their length, and in the same order as used in table $T$. After each string $s$ is generated, use program $P'$ to determine if $s$ is a program that computes a function in $Q$. Continue doing this until $x$ such programs have been found. In terms of table $T$, that program, call it $F$, will compute function $f_x$. Program $F$ has finite length, so $P$ will only generate a finite number of strings before $F$ is generated. Then once $F$ is generated, run it with input $x$. By definition, program $F$ will compute $f_x(x)$ in finite time. Then output $\overline{f}(x) = 1 - f_x(x)$.

So, this approach seems to be able to compute $\overline{f}(x)$ in finite time, for any positive integer $x$, showing that $\overline{f}$ is a computable function. Doesn't it?

Discuss and resolve.

5. Use the resolution to the issue in problem 4, to state and prove an interesting theorem about computer programs (yes, this is a vague question, but the kind that real researchers face daily).

6. Show that theorems 4.1 and 4.2 are equivalent.

7. Show that a formal proof-system that is sound is also consistent. Then ponder whether it is true that any formal proof-system that is consistent must be sound. Hint: no.

---

### النسخة العربية

1. في مكانين في البراهين، يتم كسر التعادلات في أطوال السلاسل النصية معجمياً. أزعم أن هذا التفصيل غير مطلوب في أي من المكانين. هل هذا صحيح؟

2. في برهان النظرية 2.1، ما الفائدة من اشتراط أن تكون البرامج الحاسوبية مدرجة حسب ترتيب أطوالها؟ هل سيظل البرهان المعطى للنظرية 2.1 صحيحاً إذا كانت البرامج (بطريقة ما) مدرجة بترتيب غير متوقع؟

3. في البرنامج $P^*$، ما الفائدة من اشتراط أن يولد البرنامج $P$ السلاسل النصية حسب ترتيب أطوالها؟ هل سيظل البرهان المعطى للنظرية 4.1 صحيحاً إذا لم يولد $P$ السلاسل النصية بهذا الترتيب، لكن يمكنه (بطريقة ما) توليد جميع السلاسل النصية بترتيب غير متوقع؟

4. ألا يظهر النهج التالي أن $\overline{f}(x)$ قابل للحوسبة؟

أولاً، أنشئ برنامج حاسوبي $P'$ يمكنه النظر إلى سلسلة نصية $s$ على الأبجدية المحدودة المستخدمة للبرامج الحاسوبية (ببعض اللغات البرمجية الثابتة، على سبيل المثال، C)، وتحديد ما إذا كانت $s$ برنامج حاسوبي قانوني يحسب دالة $f$ في $Q$. بالتأكيد، يمكن لمترجم C التحقق مما إذا كانت $s$ برنامجاً صحيحاً نحوياً في C.

ثم بالنظر إلى أي عدد صحيح موجب $x$، استخدم البرنامج $P$ لتوليد السلاسل النصية على الأبجدية المحدودة المستخدمة للبرامج الحاسوبية، حسب ترتيب طولها، وبنفس الترتيب المستخدم في الجدول $T$. بعد توليد كل سلسلة نصية $s$، استخدم البرنامج $P'$ لتحديد ما إذا كانت $s$ برنامجاً يحسب دالة في $Q$. استمر في القيام بذلك حتى يتم العثور على $x$ من هذه البرامج. من حيث الجدول $T$، سيحسب ذلك البرنامج، أطلق عليه اسم $F$، الدالة $f_x$. البرنامج $F$ له طول محدود، لذلك سيولد $P$ فقط عدداً محدوداً من السلاسل النصية قبل توليد $F$. ثم بمجرد توليد $F$، قم بتشغيله بالمدخل $x$. بالتعريف، سيحسب البرنامج $F$ $f_x(x)$ في وقت محدود. ثم اخرج $\overline{f}(x) = 1 - f_x(x)$.

لذلك، يبدو أن هذا النهج قادر على حساب $\overline{f}(x)$ في وقت محدود، لأي عدد صحيح موجب $x$، مما يظهر أن $\overline{f}$ دالة قابلة للحوسبة. أليس كذلك؟

ناقش واحل.

5. استخدم حل المشكلة في السؤال 4، لصياغة وإثبات نظرية مثيرة للاهتمام حول البرامج الحاسوبية (نعم، هذا سؤال غامض، لكنه من النوع الذي يواجهه الباحثون الحقيقيون يومياً).

6. أظهر أن النظريتين 4.1 و 4.2 متكافئتان.

7. أظهر أن نظام البرهان الصوري السليم متسق أيضاً. ثم تأمل ما إذا كان صحيحاً أن أي نظام برهان صوري متسق يجب أن يكون سليماً. تلميح: لا.

---

### Translation Notes

- **Figures referenced:** Table T (الجدول T)
- **Key terms introduced:** lexicographic ordering (الترتيب المعجمي), syntactically correct (صحيح نحوياً), halting problem (مسألة التوقف - implicit)
- **Equations:** Multiple program descriptions
- **Citations:** 0
- **Special handling:** Questions are pedagogical; Question 4 presents a paradox that students need to resolve

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
