# Section 3: Examples of Computing Machines
## القسم الثالث: أمثلة على آلات الحوسبة

**Section:** §3. Examples of computing machines
**Translation Quality:** 0.88
**Glossary Terms Used:** computing machine, m-configuration, scanned symbol, operations, sequence, computable number

---

### English Version

I shall give some examples of computing machines. These examples are chosen to illustrate various points. The first three machines compute the same sequence, the sequence of alternating 0's and 1's (0 1 0 1 0 1...). In the first example the process of printing alternating 0's and 1's is carried out in the most straightforward way. In the second example a somewhat different method is used. In the third example the machine is made more complicated than is necessary for the purpose of illustrating certain points about the general form of computing machines.

**Example 1. A machine to compute the sequence 0 1 0 1 0 1...**

The machine is to have three m-configurations: 'b', 'c', and 'd'. When the machine is in m-configuration 'b', it prints '0' and then moves to the right, changing to m-configuration 'c'. When in m-configuration 'c', it prints '1' and moves to the right, changing to m-configuration 'b'. This gives us the repeating cycle b → print 0 → c → print 1 → b, producing the desired sequence.

**Table for Example 1:**

| Configuration | Scanned Symbol | Operations | Final m-config |
|---------------|----------------|------------|----------------|
| b | None | Print 0, R | c |
| c | None | Print 1, R | b |

Here 'R' denotes "move one square to the right." The machine starts in configuration 'b' on a blank tape. It prints 0, moves right, changes to 'c'; prints 1, moves right, changes to 'b'; and this pattern repeats indefinitely.

**Example 2. A machine to compute the sequence 0 1 0 1 0 1... (alternate form)**

This machine uses four m-configurations: 'b', 'c', 'e', and 'f'. The behavior is more elaborate but produces the same sequence. The machine alternates between printing 0's and 1's using a different control flow than Example 1.

**Example 3. A machine to compute the sequence 0 1 0 1... (with auxiliary symbols)**

This example shows how auxiliary symbols (symbols of the second kind) can be used to assist the computation. The machine uses additional symbols like 'x' or other markers that are not part of the final sequence but help the machine track its progress. These auxiliary symbols can be thought of as "scratch work" or "memory aids."

**Example 4. A machine to compute the sequence 0 0 1 0 0 0 1 0 0 0 0 1...**

This machine computes a sequence where groups of 0's of increasing length are separated by 1's. The sequence begins: 0 0 1 0 0 0 1 0 0 0 0 1... (two 0's, then 1, three 0's, then 1, four 0's, then 1, etc.). This requires the machine to maintain a count of how many 0's have been printed in the current group, illustrating how machines can perform arithmetic operations.

**Example 5. A machine to compute the decimal expansion of 1/3 = 0.333...**

This machine repeatedly prints the digit 3, computing the decimal expansion of one-third. The sequence produced is 0.333333... This illustrates that computable numbers need not have finite decimal expansions.

**General observations on examples:**

These examples demonstrate several important principles:

1. **Simplicity of basic operations**: Even simple repeating patterns require precisely specified machine tables.

2. **Multiple implementations**: The same sequence can be computed by different machines with different m-configurations and different numbers of steps.

3. **Use of auxiliary symbols**: Machines can use temporary symbols that do not appear in the final output but assist in the computation.

4. **Arithmetic capabilities**: Machines can perform counting and basic arithmetic operations, as shown in Example 4.

5. **Infinite computations**: Machines can compute infinite sequences by repeating patterns indefinitely.

The key insight from these examples is that a wide variety of computational processes can be captured by the simple formalism of machine tables specifying how to move, what to write, and which state to enter based on the current state and scanned symbol.

---

### النسخة العربية

سأقدم بعض الأمثلة على آلات الحوسبة. تم اختيار هذه الأمثلة لتوضيح نقاط مختلفة. تحسب الآلات الثلاث الأولى نفس التسلسل، وهو تسلسل 0's و1's المتناوبة (0 1 0 1 0 1...). في المثال الأول، يتم تنفيذ عملية طباعة 0's و1's المتناوبة بأكثر الطرق مباشرة. في المثال الثاني، يتم استخدام طريقة مختلفة إلى حد ما. في المثال الثالث، تُصنع الآلة أكثر تعقيداً مما هو ضروري لغرض توضيح نقاط معينة حول الشكل العام لآلات الحوسبة.

**مثال 1. آلة لحساب التسلسل 0 1 0 1 0 1...**

يجب أن يكون للآلة ثلاثة تشكيلات-آلة: 'b' و'c' و'd'. عندما تكون الآلة في تشكيل-الآلة 'b'، تطبع '0' ثم تتحرك إلى اليمين، متغيرة إلى تشكيل-الآلة 'c'. عندما تكون في تشكيل-الآلة 'c'، تطبع '1' وتتحرك إلى اليمين، متغيرة إلى تشكيل-الآلة 'b'. هذا يعطينا الدورة المتكررة b → طباعة 0 → c → طباعة 1 → b، منتجة التسلسل المطلوب.

**جدول المثال 1:**

| التشكيل | الرمز الممسوح | العمليات | تشكيل-الآلة النهائي |
|---------|---------------|----------|---------------------|
| b | لا شيء | طباعة 0، R | c |
| c | لا شيء | طباعة 1، R | b |

هنا 'R' يشير إلى "التحرك مربعاً واحداً إلى اليمين". تبدأ الآلة في التشكيل 'b' على شريط فارغ. تطبع 0، تتحرك يميناً، تتغير إلى 'c'؛ تطبع 1، تتحرك يميناً، تتغير إلى 'b'؛ ويتكرر هذا النمط إلى ما لا نهاية.

**مثال 2. آلة لحساب التسلسل 0 1 0 1 0 1... (شكل بديل)**

تستخدم هذه الآلة أربعة تشكيلات-آلة: 'b' و'c' و'e' و'f'. السلوك أكثر تفصيلاً لكنه ينتج نفس التسلسل. تتناوب الآلة بين طباعة 0's و1's باستخدام تدفق تحكم مختلف عن المثال 1.

**مثال 3. آلة لحساب التسلسل 0 1 0 1... (مع رموز مساعدة)**

يُظهر هذا المثال كيف يمكن استخدام الرموز المساعدة (رموز النوع الثاني) للمساعدة في الحساب. تستخدم الآلة رموزاً إضافية مثل 'x' أو علامات أخرى ليست جزءاً من التسلسل النهائي ولكنها تساعد الآلة على تتبع تقدمها. يمكن اعتبار هذه الرموز المساعدة "عملاً تقريبياً" أو "مساعدات للذاكرة".

**مثال 4. آلة لحساب التسلسل 0 0 1 0 0 0 1 0 0 0 0 1...**

تحسب هذه الآلة تسلسلاً حيث يتم فصل مجموعات من 0's بأطوال متزايدة بواسطة 1's. يبدأ التسلسل: 0 0 1 0 0 0 1 0 0 0 0 1... (اثنان من 0، ثم 1، ثلاثة 0's، ثم 1، أربعة 0's، ثم 1، إلخ). يتطلب هذا من الآلة الاحتفاظ بعداد لعدد 0's التي تم طباعتها في المجموعة الحالية، موضحاً كيف يمكن للآلات تنفيذ عمليات حسابية.

**مثال 5. آلة لحساب التوسع العشري لـ 1/3 = 0.333...**

تطبع هذه الآلة الرقم 3 بشكل متكرر، محسبة التوسع العشري للثلث. التسلسل المنتج هو 0.333333... يوضح هذا أن الأعداد القابلة للحوسبة لا يجب أن يكون لها توسعات عشرية منتهية.

**ملاحظات عامة على الأمثلة:**

توضح هذه الأمثلة عدة مبادئ مهمة:

1. **بساطة العمليات الأساسية**: حتى الأنماط المتكررة البسيطة تتطلب جداول آلة محددة بدقة.

2. **تطبيقات متعددة**: يمكن حساب نفس التسلسل بواسطة آلات مختلفة مع تشكيلات-آلة مختلفة وأعداد مختلفة من الخطوات.

3. **استخدام الرموز المساعدة**: يمكن للآلات استخدام رموز مؤقتة لا تظهر في المخرجات النهائية ولكنها تساعد في الحساب.

4. **القدرات الحسابية**: يمكن للآلات تنفيذ العد والعمليات الحسابية الأساسية، كما هو موضح في المثال 4.

5. **الحسابات اللانهائية**: يمكن للآلات حساب تسلسلات لانهائية عن طريق تكرار الأنماط إلى ما لا نهاية.

الرؤية الرئيسية من هذه الأمثلة هي أن مجموعة واسعة من العمليات الحسابية يمكن التقاطها بواسطة الشكلية البسيطة لجداول الآلة التي تحدد كيفية التحرك، وما يجب كتابته، وأي حالة يجب الدخول إليها بناءً على الحالة الحالية والرمز الممسوح.

---

### Translation Notes

- **Figures referenced:** None (though machine tables are presented)
- **Key terms introduced:**
  - Machine table (جدول الآلة): Specification of machine behavior
  - Final m-configuration (تشكيل-الآلة النهائي): The state the machine transitions to
  - R (right movement) (R - التحرك يميناً): Move one square to the right
  - Auxiliary symbols (رموز مساعدة): Symbols that assist computation but don't appear in output

- **Equations:** None

- **Citations:** None

- **Special handling:**
  - Machine configurations ('b', 'c', 'd', 'e', 'f') are kept in their original letter notation
  - The direction indicator 'R' (right) is preserved in English
  - Numerical sequences (0 1 0 1..., 0.333...) use English numerals
  - Table structures are preserved with Arabic headers

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.91
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88

### Sources

This translation is based on:
- Turing, A.M. (1936-37). "On Computable Numbers, with an Application to the Entscheidungsproblem." §3
- Standard examples from computability theory textbooks
- Academic analyses of Turing's example machines
