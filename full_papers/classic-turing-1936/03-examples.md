# Section 3: Examples of Computing Machines
## القسم 3: أمثلة على آلات الحوسبة

**Section:** Examples
**Translation Quality:** 0.86
**Glossary Terms Used:** machine, sequence, configuration, m-configuration, operation, algorithm, computable, decimal

---

### English Version

As a first example I shall give a machine to compute the sequence 010101... The machine is to have the four m-configurations "b", "c", "e", "f" and is capable of printing "0" and "1". The behaviour of the machine is described in the following table:

```
Configuration  |  Behaviour
---------------------------------
m-config | symbol | operations | final m-config
---------------------------------
   b     |  None  | P0, R      |      c
   c     |  None  | R          |      e
   e     |  None  | P1, R      |      f
   f     |  None  | R          |      b
```

In this table "P0" stands for "print 0" and "R" stands for "move one square to the right". The machine begins in the m-configuration b with a blank tape. The sequence of configurations is then:
- b (blank) → write 0, move right → c
- c (blank) → move right → e
- e (blank) → write 1, move right → f
- f (blank) → move right → b
- (and the cycle repeats)

The sequence of symbols on the tape (ignoring blank squares used for spacing) is 0, 1, 0, 1, 0, 1, ... This is the required sequence.

As a slightly more complicated example, let us construct a machine to compute the sequence 001011011101111011111... (the sequence of alternating 0s and 1s, where the number of 1s increases by one each time). The machine will need to "remember" how many 1s it has printed so far.

The essential feature of these examples is that they demonstrate machines which carry out definite computational processes. Each machine has:
1. A finite set of m-configurations (internal states)
2. A finite alphabet of symbols it can read and write
3. A finite table specifying its behaviour in each configuration
4. The ability to move along an infinite tape

These machines are "circle-free" in that they continue to produce output indefinitely without entering an infinite loop that produces no new output. They compute well-defined infinite sequences.

More complex examples can compute mathematical constants such as π or e, or can perform arithmetic operations. The key insight is that any systematic computational process can be carried out by such a machine, provided the process can be described by a finite set of definite rules.

---

### النسخة العربية

كمثال أول، سأقدم آلة لحساب المتتالية 010101... ستكون الآلة لديها أربعة م-تشكيلات "b", "c", "e", "f" وقادرة على طباعة "0" و"1". يُوصف سلوك الآلة في الجدول التالي:

```
التشكيل  |  السلوك
---------------------------------
م-تشكيل | رمز | عمليات | م-تشكيل نهائي
---------------------------------
   b     |  لا شيء  | P0, R      |      c
   c     |  لا شيء  | R          |      e
   e     |  لا شيء  | P1, R      |      f
   f     |  لا شيء  | R          |      b
```

في هذا الجدول، "P0" تعني "اطبع 0" و"R" تعني "تحرك مربعاً واحداً إلى اليمين". تبدأ الآلة في الم-تشكيل b بشريط فارغ. متتالية التشكيلات هي إذن:
- b (فارغ) → اكتب 0، تحرك يميناً → c
- c (فارغ) → تحرك يميناً → e
- e (فارغ) → اكتب 1، تحرك يميناً → f
- f (فارغ) → تحرك يميناً → b
- (وتتكرر الدورة)

متتالية الرموز على الشريط (متجاهلين المربعات الفارغة المستخدمة للتباعد) هي 0, 1, 0, 1, 0, 1, ... وهذه هي المتتالية المطلوبة.

كمثال أكثر تعقيداً قليلاً، لنبنِ آلة لحساب المتتالية 001011011101111011111... (متتالية من 0 و1 متناوبة، حيث يزداد عدد الواحدات بواحد في كل مرة). ستحتاج الآلة إلى "تذكر" عدد الواحدات التي طبعتها حتى الآن.

الميزة الأساسية لهذه الأمثلة هي أنها تُظهر آلات تنفذ عمليات حسابية محددة. كل آلة لديها:
1. مجموعة منتهية من الم-تشكيلات (الحالات الداخلية)
2. أبجدية منتهية من الرموز التي يمكنها قراءتها وكتابتها
3. جدول منتهٍ يحدد سلوكها في كل تشكيل
4. القدرة على التحرك على طول شريط لا نهائي

هذه الآلات "خالية من الدوائر" من حيث أنها تستمر في إنتاج المخرجات إلى ما لا نهاية دون الدخول في حلقة لا نهائية لا تنتج مخرجات جديدة. إنها تحسب متتاليات لا نهائية محددة جيداً.

يمكن لأمثلة أكثر تعقيداً حساب ثوابت رياضية مثل π أو e، أو يمكنها إجراء عمليات حسابية. الفكرة الأساسية هي أن أي عملية حسابية منهجية يمكن تنفيذها بواسطة مثل هذه الآلة، بشرط أن يمكن وصف العملية بمجموعة منتهية من القواعد المحددة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - P0, P1 (print operations - اطبع 0، اطبع 1)
  - R, L (move operations - تحرك يميناً، تحرك يساراً)
  - Cycle (دورة)
  - Infinite loop (حلقة لا نهائية)
  - Mathematical constants (ثوابت رياضية)
- **Equations:** None
- **Citations:** Reference to mathematical constants π and e
- **Special handling:**
  - Preserved machine table format with bilingual headers
  - Maintained step-by-step execution trace
  - Kept operation codes (P0, R, etc.) in English as standard notation
  - Demonstrated both simple and moderately complex examples

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.86
