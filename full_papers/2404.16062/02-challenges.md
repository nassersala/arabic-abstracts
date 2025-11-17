# Section 2: What are the Challenges?
## القسم 2: ما هي التحديات؟

**Section:** challenges
**Translation Quality:** 0.87
**Glossary Terms Used:** test case, data dependency, sequential execution, parallelization, shrinking, greedy algorithm, leftward traversal

---

### English Version

## Test Size

QuickCheck gradually increases test input size as more tests pass successfully. Generators receive a size parameter; many use it as an upper bound for data structure dimensions (e.g., list length). The default configuration runs 100 tests, ensuring the generator receives all sizes from 0 to 99.

The critical dependency emerges from test discarding. Properties can discard test cases when preconditions fail. Discarded tests don't count toward the 100-test target, creating a data dependency: appropriate test size depends on whether previous tests succeeded or were discarded. This sequential dependency prevents straightforward parallelization.

## Shrinking

When a test fails, shrinking searches for smaller failing cases through a greedy leftward traversal of shrink candidates. Users must define shrink functions returning lists of reduced variants. The sequential algorithm tries candidates in order until finding a new failure, then recurses.

Two parallel approaches are proposed:

**Greedy shrinking** evaluates candidates in parallel, immediately continuing with the first failure found. This may skip earlier candidates that would also fail, potentially producing less-reduced counterexamples.

**Deterministic shrinking** speculatively evaluates candidates but only commits to choices matching sequential behavior, ensuring identical minimal counterexamples despite potential wasted computation.

---

### النسخة العربية

## حجم الاختبار

يزيد QuickCheck تدريجياً من حجم مدخلات الاختبار كلما نجحت المزيد من الاختبارات. تتلقى المولدات معامل حجم؛ يستخدمه الكثير منها كحد أعلى لأبعاد بنية البيانات (مثل طول القائمة). يقوم التكوين الافتراضي بتشغيل 100 اختبار، مما يضمن حصول المولد على جميع الأحجام من 0 إلى 99.

يظهر الاعتماد الحاسم من تجاهل الاختبارات. يمكن للخصائص تجاهل حالات الاختبار عندما تفشل الشروط المسبقة. لا تُحتسب الاختبارات المتجاهلة ضمن هدف الـ 100 اختبار، مما يخلق اعتمادية بيانات: يعتمد حجم الاختبار المناسب على ما إذا كانت الاختبارات السابقة قد نجحت أم تم تجاهلها. تمنع هذه الاعتمادية التسلسلية التوازي المباشر.

## التقليص

عندما يفشل اختبار، يبحث التقليص عن حالات فاشلة أصغر من خلال اجتياز جشع نحو اليسار لمرشحي التقليص. يجب على المستخدمين تعريف دوال تقليص تُرجع قوائم من المتغيرات المختزلة. تحاول الخوارزمية التسلسلية المرشحين بالترتيب حتى إيجاد فشل جديد، ثم تتكرر.

يُقترح نهجان متوازيان:

**التقليص الجشع** يقيّم المرشحين بالتوازي، ويواصل فوراً مع أول فشل يُعثر عليه. قد يتخطى هذا المرشحين الأوائل الذين كانوا سيفشلون أيضاً، مما ينتج عنه أمثلة مضادة أقل اختزالاً.

**التقليص الحتمي** يقيّم المرشحين تكهنياً لكنه يلتزم فقط بالخيارات التي تطابق السلوك التسلسلي، مما يضمن أمثلة مضادة دنيا متطابقة رغم الحساب المهدر المحتمل.

---

### Translation Notes

- **Key terms introduced:**
  - Test input size = حجم مدخلات الاختبار
  - Generators = المولدات
  - Size parameter = معامل حجم
  - Upper bound = حد أعلى
  - Data structure dimensions = أبعاد بنية البيانات
  - Test discarding = تجاهل الاختبارات
  - Preconditions = الشروط المسبقة
  - Data dependency = اعتمادية بيانات
  - Straightforward parallelization = التوازي المباشر
  - Greedy leftward traversal = اجتياز جشع نحو اليسار
  - Shrink candidates = مرشحي التقليص
  - Reduced variants = المتغيرات المختزلة
  - Speculative evaluation = التقييم التكهني
  - Wasted computation = الحساب المهدر

- **Technical concepts:**
  - Test size progression in QuickCheck
  - Sequential dependencies from test discarding
  - Shrinking algorithms (greedy vs deterministic)
  - Trade-offs between parallelism and determinism

- **Special handling:**
  - Preserved technical accuracy in describing the two shrinking approaches
  - Maintained clear distinction between "greedy" (جشع) and "deterministic" (حتمي)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-Translation Check

**Test Size**
QuickCheck gradually increases test input size as more tests succeed. Generators receive a size parameter; many use it as an upper bound for data structure dimensions (such as list length). The default configuration runs 100 tests, ensuring the generator receives all sizes from 0 to 99.

The critical dependency emerges from test discarding. Properties can discard test cases when preconditions fail. Discarded tests are not counted toward the 100-test target, creating a data dependency: the appropriate test size depends on whether previous tests succeeded or were discarded. This sequential dependency prevents straightforward parallelization.

**Shrinking**
When a test fails, shrinking searches for smaller failing cases through a greedy leftward traversal of shrink candidates. Users must define shrink functions that return lists of reduced variants. The sequential algorithm tries candidates in order until finding a new failure, then recurses.

Two parallel approaches are proposed:

**Greedy shrinking** evaluates candidates in parallel, immediately continuing with the first failure found. This may skip earlier candidates that would also fail, producing less-reduced counterexamples.

**Deterministic shrinking** evaluates candidates speculatively but only commits to choices matching sequential behavior, ensuring identical minimal counterexamples despite potential wasted computation.

✓ Back-translation accurately preserves technical content and meaning.
