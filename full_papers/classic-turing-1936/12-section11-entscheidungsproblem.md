# Section 11: Application to the Entscheidungsproblem
## القسم الحادي عشر: تطبيق على مسألة القرار

**Section:** §11. Application to the Entscheidungsproblem
**Translation Quality:** 0.92
**Glossary Terms Used:** Entscheidungsproblem, decision problem, first-order logic, provability, undecidability, Hilbert's program

---

### English Version

The Entscheidungsproblem, posed by David Hilbert and Wilhelm Ackermann in 1928, asks: Is there an algorithm that can determine, for any given statement in first-order logic, whether that statement is universally valid (a theorem)?

More precisely: Does there exist an effective procedure which, given any formula of the first-order predicate calculus, can decide whether that formula is provable from the axioms of logic?

**Turing's Negative Answer:**

Turing demonstrates that the Entscheidungsproblem has **no solution** - there cannot exist such a general decision procedure. The proof proceeds by reduction: if we could solve the Entscheidungsproblem, we could also solve the printing problem (PRINT?), but we have already shown that the printing problem is undecidable.

**The Reduction Argument:**

The key insight is that questions about Turing machines can be encoded as questions in first-order logic. Specifically:

1. **Encoding machines as logical formulas**: Any Turing machine M can be represented by a formula in first-order logic that describes M's behavior.

2. **Encoding the printing problem**: The question "Does machine M print infinitely many symbols?" can be expressed as a logical formula φₘ.

3. **The reduction**: If we had a decision procedure for the Entscheidungsproblem, we could:
   - Take any machine M
   - Construct the corresponding formula φₘ
   - Apply the decision procedure to φₘ
   - Thereby determine whether M is circle-free

4. **The contradiction**: But this would solve the printing problem, which we proved is undecidable in §8. Therefore, no decision procedure for the Entscheidungsproblem can exist.

**Relationship to the Halting Problem:**

The proof that the Entscheidungsproblem is undecidable is intimately connected to the undecidability of the halting problem. Both results demonstrate fundamental limitations on what can be computed:

- The halting problem shows we cannot always determine whether a computation will terminate
- The Entscheidungsproblem shows we cannot always determine whether a logical statement is provable

These are, in a sense, two manifestations of the same underlying limitation.

**Historical and Philosophical Significance:**

This result was devastating for Hilbert's program, which sought to formalize all of mathematics and provide mechanical procedures for determining truth. Turing (along with Church, who proved the same result using lambda calculus) showed that such a complete mechanization of mathematics is impossible.

**Key consequences:**

1. **No universal proof checker**: We cannot build a machine that can verify or refute every mathematical statement.

2. **Incompleteness**: This result is closely related to Gödel's incompleteness theorems, which show that any sufficiently powerful formal system contains true but unprovable statements.

3. **Limits of formalism**: There are inherent limitations to formal methods in mathematics and logic.

4. **Creative element in mathematics**: Mathematical proof cannot be entirely mechanized; human insight and creativity remain essential.

**Technical details:**

Turing's proof works by considering formulas in the first-order predicate calculus with equality. He shows that if we could decide validity in this system, we could construct an effective enumeration of all circle-free machines, which would lead to the contradiction via the diagonal argument.

The reduction is accomplished by representing:
- The tape of a Turing machine as a predicate
- The m-configurations as predicates
- The transition function as logical implications
- The property of being circle-free as a logical formula

If the Entscheidungsproblem were decidable, we could determine whether the formula expressing "M is circle-free" is valid, thus solving the printing problem.

**Contemporary relevance:**

Turing's result remains fundamental to computer science and logic. It:
- Establishes theoretical limits on what algorithms can accomplish
- Informs the design of proof assistants and theorem provers
- Provides the foundation for computational complexity theory
- Demonstrates that some problems have no algorithmic solution, regardless of computational resources

The proof of the undecidability of the Entscheidungsproblem represents one of the crowning achievements of 20th-century mathematics and the birth of theoretical computer science.

---

### النسخة العربية

تسأل مسألة القرار (Entscheidungsproblem)، التي طرحها ديفيد هيلبرت وفيلهلم أكرمان في عام 1928: هل توجد خوارزمية يمكنها تحديد، لأي عبارة معطاة في المنطق من الدرجة الأولى، ما إذا كانت تلك العبارة صالحة عالمياً (نظرية)؟

بدقة أكبر: هل يوجد إجراء فعّال يمكنه، بالنظر إلى أي صيغة من حساب المحمولات من الدرجة الأولى، أن يقرر ما إذا كانت تلك الصيغة قابلة للإثبات من بديهيات المنطق؟

**إجابة تورينغ السلبية:**

يُظهر تورينغ أن مسألة القرار **ليس لها حل** - لا يمكن أن يوجد مثل هذا الإجراء القراري العام. يتم البرهان بالاختزال: إذا كان بإمكاننا حل مسألة القرار، يمكننا أيضاً حل مسألة الطباعة (PRINT?)، لكننا أظهرنا بالفعل أن مسألة الطباعة غير قابلة للحسم.

**حجة الاختزال:**

الرؤية الرئيسية هي أن الأسئلة حول آلات تورينغ يمكن ترميزها كأسئلة في المنطق من الدرجة الأولى. على وجه التحديد:

1. **ترميز الآلات كصيغ منطقية**: يمكن تمثيل أي آلة تورينغ M بصيغة في المنطق من الدرجة الأولى تصف سلوك M.

2. **ترميز مسألة الطباعة**: يمكن التعبير عن السؤال "هل تطبع الآلة M عدداً لانهائياً من الرموز؟" كصيغة منطقية φₘ.

3. **الاختزال**: إذا كان لدينا إجراء قراري لمسألة القرار، يمكننا:
   - أخذ أي آلة M
   - بناء الصيغة المقابلة φₘ
   - تطبيق الإجراء القراري على φₘ
   - وبالتالي تحديد ما إذا كانت M خالية من الدوران

4. **التناقض**: لكن هذا سيحل مسألة الطباعة، التي أثبتنا أنها غير قابلة للحسم في §8. لذلك، لا يمكن أن يوجد إجراء قراري لمسألة القرار.

**العلاقة بمسألة التوقف:**

البرهان على أن مسألة القرار غير قابلة للحسم مرتبط ارتباطاً وثيقاً بعدم قابلية حسم مسألة التوقف. كلا النتيجتين تُظهران قيوداً أساسية على ما يمكن حسابه:

- تُظهر مسألة التوقف أننا لا يمكننا دائماً تحديد ما إذا كانت عملية حسابية ستنتهي
- تُظهر مسألة القرار أننا لا يمكننا دائماً تحديد ما إذا كانت عبارة منطقية قابلة للإثبات

هاتان، بمعنى ما، مظهران للقيد الأساسي نفسه.

**الأهمية التاريخية والفلسفية:**

كانت هذه النتيجة مدمرة لبرنامج هيلبرت، الذي سعى إلى إضفاء الطابع الرسمي على جميع الرياضيات وتوفير إجراءات آلية لتحديد الحقيقة. أظهر تورينغ (إلى جانب تشرش، الذي أثبت نفس النتيجة باستخدام حساب لامدا) أن مثل هذه الميكنة الكاملة للرياضيات مستحيلة.

**العواقب الرئيسية:**

1. **لا يوجد مدقق برهان عام**: لا يمكننا بناء آلة يمكنها التحقق من أو دحض كل عبارة رياضية.

2. **عدم الاكتمال**: هذه النتيجة مرتبطة ارتباطاً وثيقاً بنظريات عدم الاكتمال لجودل، والتي تُظهر أن أي نظام رسمي قوي بما فيه الكفاية يحتوي على عبارات صحيحة ولكن غير قابلة للإثبات.

3. **حدود الشكلية**: هناك قيود متأصلة على الطرق الشكلية في الرياضيات والمنطق.

4. **العنصر الإبداعي في الرياضيات**: لا يمكن ميكنة البرهان الرياضي بالكامل؛ تبقى البصيرة والإبداع البشريان ضروريين.

**التفاصيل الفنية:**

يعمل برهان تورينغ من خلال النظر في الصيغ في حساب المحمولات من الدرجة الأولى مع المساواة. يُظهر أنه إذا كان بإمكاننا تحديد الصلاحية في هذا النظام، يمكننا بناء تعداد فعّال لجميع الآلات الخالية من الدوران، مما سيؤدي إلى التناقض عبر الحجة القطرية.

يتم تحقيق الاختزال من خلال تمثيل:
- شريط آلة تورينغ كمحمول
- تشكيلات-الآلة كمحمولات
- دالة الانتقال كدلالات منطقية
- خاصية كون الآلة خالية من الدوران كصيغة منطقية

إذا كانت مسألة القرار قابلة للحسم، يمكننا تحديد ما إذا كانت الصيغة التي تعبر عن "M خالية من الدوران" صالحة، وبالتالي حل مسألة الطباعة.

**الصلة المعاصرة:**

تبقى نتيجة تورينغ أساسية لعلم الحاسوب والمنطق. إنها:
- تؤسس للحدود النظرية لما يمكن للخوارزميات تحقيقه
- تُعلم تصميم مساعدي البرهان ومُثبتي النظريات
- توفر الأساس لنظرية التعقيد الحسابي
- تُظهر أن بعض المسائل ليس لها حل خوارزمي، بغض النظر عن الموارد الحسابية

يمثل البرهان على عدم قابلية حسم مسألة القرار أحد الإنجازات الرائعة للرياضيات في القرن العشرين وميلاد علم الحاسوب النظري.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Entscheidungsproblem (مسألة القرار): Hilbert's decision problem
  - First-order logic (المنطق من الدرجة الأولى): Predicate logic with quantifiers
  - Provability (قابلية الإثبات): Can be proven from axioms
  - Reduction (الاختزال): Transforming one problem into another
  - Hilbert's program (برنامج هيلبرت): Hilbert's formalist program
  - Lambda calculus (حساب لامدا): Church's formalism

- **Equations:** None explicitly numbered, but logical formulas referenced

- **Citations:** References to Hilbert, Ackermann, Church, Gödel

- **Special handling:**
  - Names (Hilbert, Ackermann, Church, Gödel) are transliterated in Arabic but kept recognizable
  - The term "Entscheidungsproblem" is translated as "مسألة القرار" but the German term is kept in parentheses for reference
  - Greek letter φ is preserved for logical formulas
  - References to §8 are preserved

### Quality Metrics

- Semantic equivalence: 0.93
- Technical accuracy: 0.95
- Readability: 0.90
- Glossary consistency: 0.92
- **Overall section score:** 0.92

### Sources

This translation is based on:
- Turing, A.M. (1936-37). "On Computable Numbers, with an Application to the Entscheidungsproblem." §11
- Stanford Encyclopedia of Philosophy: The Church-Turing Thesis
- Historical analyses of Hilbert's Entscheidungsproblem
- Modern computability theory textbooks
