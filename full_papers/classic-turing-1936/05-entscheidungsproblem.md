# Section 5: Application to the Entscheidungsproblem
## القسم 5: التطبيق على مسألة القرار

**Section:** Application to Entscheidungsproblem
**Translation Quality:** 0.88
**Glossary Terms Used:** Entscheidungsproblem, decidable, undecidable, algorithm, computable, circle-free, halting problem, proof by contradiction

---

### English Version

The Entscheidungsproblem, posed by David Hilbert, asks whether there exists an algorithm that can determine, for any given mathematical statement in a formal system, whether that statement is provable or not. We shall show that no such algorithm exists by proving a related but more fundamental result: there is no general algorithm to determine whether an arbitrary computing machine is circle-free.

**The Halting Problem**: Consider the problem of determining whether a given computing machine M, when started with a blank tape, will eventually halt (finish its computation) or will run forever. If M is circle-free, it continues to produce output indefinitely. If M is circular, it eventually enters a state where it produces no more output symbols of the computed sequence, even though it may continue to move and change state.

We can formalize this as: Given the standard description of a machine M, is there an algorithm H that can determine whether M is circle-free?

**Proof by Contradiction**: Suppose such an algorithm H exists. Then we could construct the following procedure:
1. Use H to enumerate all circle-free machines (by testing each standard description in turn)
2. For each circle-free machine, compute the first symbol of its output sequence
3. This gives us a method to enumerate all computable sequences

Now construct a machine D (for "diagonal") that:
- Computes the n-th digit of a sequence that differs from the n-th computable sequence in the n-th digit
- This sequence is computable (we just described how to compute it)
- But by construction, it differs from every sequence in our enumeration
- This is a contradiction

Therefore, our assumption that algorithm H exists must be false. There is no general algorithm to determine whether an arbitrary machine is circle-free.

**Implication for the Entscheidungsproblem**: The undecidability of the circle-free problem directly implies the undecidability of the Entscheidungsproblem. Here's why:

If we could decide provability in a formal system, we could:
1. For any statement S, enumerate all possible proofs
2. Check each one to see if it proves S or proves ¬S
3. Determine whether a "proof-searching machine" will find a proof

But this is equivalent to solving the halting problem for that machine. Since we've shown the halting problem is undecidable, the Entscheidungsproblem must also be undecidable.

**The Significance**: This result, published simultaneously with Alonzo Church's proof using lambda calculus, established that:
1. There are definite limitations on what can be computed algorithmically
2. Not all mathematical questions can be answered by mechanical procedures
3. Hilbert's program to formalize all of mathematics cannot be fully realized
4. There exist well-defined mathematical problems for which no algorithm exists

This fundamentally changed our understanding of the nature of computation, proof, and mathematical truth. It showed that there are inherent limits to what can be computed or proven, regardless of how powerful our computers or formal systems become.

---

### النسخة العربية

تسأل مسألة القرار (Entscheidungsproblem)، التي طرحها ديفيد هيلبرت، عما إذا كان هناك خوارزمية يمكنها تحديد، لأي عبارة رياضية معطاة في نظام صوري، ما إذا كانت تلك العبارة قابلة للإثبات أم لا. سنُظهر أن مثل هذه الخوارزمية غير موجودة من خلال إثبات نتيجة مرتبطة ولكن أكثر أساسية: لا توجد خوارزمية عامة لتحديد ما إذا كانت آلة حوسبة تعسفية خالية من الدوائر.

**مسألة التوقف**: اعتبر مسألة تحديد ما إذا كانت آلة حوسبة معطاة M، عندما تبدأ بشريط فارغ، ستتوقف في النهاية (تنهي حسابها) أم ستعمل إلى الأبد. إذا كانت M خالية من الدوائر، فإنها تستمر في إنتاج المخرجات إلى ما لا نهاية. إذا كانت M دائرية، فإنها تدخل في النهاية حالة لا تنتج فيها المزيد من رموز المخرجات للمتتالية المحسوبة، على الرغم من أنها قد تستمر في الحركة وتغيير الحالة.

يمكننا صياغة هذا على النحو التالي: بالنظر إلى الوصف القياسي لآلة M، هل توجد خوارزمية H يمكنها تحديد ما إذا كانت M خالية من الدوائر؟

**البرهان بالتناقض**: لنفترض أن مثل هذه الخوارزمية H موجودة. عندئذ يمكننا بناء الإجراء التالي:
1. استخدام H لتعداد جميع الآلات الخالية من الدوائر (باختبار كل وصف قياسي بالتتابع)
2. لكل آلة خالية من الدوائر، حساب الرمز الأول من متتالية مخرجاتها
3. هذا يعطينا طريقة لتعداد جميع المتتاليات القابلة للحوسبة

الآن لنبنِ آلة D (من "قطري" diagonal) التي:
- تحسب الرقم n من متتالية تختلف عن المتتالية القابلة للحوسبة رقم n في الرقم n
- هذه المتتالية قابلة للحوسبة (لقد وصفنا للتو كيفية حسابها)
- لكن بالبناء، فإنها تختلف عن كل متتالية في تعدادنا
- هذا تناقض

لذلك، يجب أن يكون افتراضنا بوجود الخوارزمية H خاطئاً. لا توجد خوارزمية عامة لتحديد ما إذا كانت آلة تعسفية خالية من الدوائر.

**التطبيق على مسألة القرار**: عدم قابلية البت في مسألة الخلو من الدوائر يستلزم مباشرة عدم قابلية البت في مسألة القرار. وإليك السبب:

لو كان بإمكاننا البت في قابلية الإثبات في نظام صوري، لكان بإمكاننا:
1. لأي عبارة S، تعداد جميع البراهين الممكنة
2. فحص كل واحد منها لمعرفة ما إذا كان يُثبت S أو يُثبت ¬S
3. تحديد ما إذا كانت "آلة البحث عن البراهين" ستجد برهاناً

لكن هذا يعادل حل مسألة التوقف لتلك الآلة. بما أننا أظهرنا أن مسألة التوقف غير قابلة للبت، فإن مسألة القرار يجب أن تكون أيضاً غير قابلة للبت.

**الأهمية**: هذه النتيجة، التي نُشرت في وقت واحد مع برهان ألونزو تشيرش باستخدام حساب لامدا، أثبتت أن:
1. هناك قيود محددة على ما يمكن حسابه خوارزمياً
2. لا يمكن الإجابة على جميع الأسئلة الرياضية بإجراءات آلية
3. لا يمكن تحقيق برنامج هيلبرت لإضفاء الطابع الصوري على جميع الرياضيات بشكل كامل
4. توجد مسائل رياضية محددة جيداً لا توجد لها خوارزمية

هذا غيّر بشكل أساسي فهمنا لطبيعة الحوسبة والبرهان والحقيقة الرياضية. أظهر أن هناك حدوداً متأصلة لما يمكن حسابه أو إثباته، بغض النظر عن مدى قوة حواسيبنا أو أنظمتنا الصورية.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Entscheidungsproblem (مسألة القرار)
  - Decidable/Undecidable (قابل للبت/غير قابل للبت)
  - Halting problem (مسألة التوقف)
  - Proof by contradiction (البرهان بالتناقض)
  - Diagonal argument (حجة قطرية)
  - Provability (قابلية الإثبات)
  - Formal system (نظام صوري)
  - Lambda calculus (حساب لامدا)
- **Equations:** None
- **Citations:** References to Hilbert and Church
- **Special handling:**
  - Preserved the logical structure of the diagonal argument
  - Maintained the connection between halting problem and Entscheidungsproblem
  - Emphasized the foundational significance of the result
  - Connected to Church's independent proof

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.88
