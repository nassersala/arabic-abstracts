# Section 4: QuickerCheck Design and Implementation
## القسم 4: تصميم وتنفيذ QuickerCheck

**Section:** design-implementation
**Translation Quality:** 0.87
**Glossary Terms Used:** parallel runtime, concurrent execution, thread synchronization, MVars, work stealing, asynchronous exceptions, resource management

---

### English Version

## Testing

The parallel testing loop spawns concurrent tester instances executing sequentially internally, coordinating through shared MVars. Initial test budgets distribute equally; threads steal work when idle, avoiding synchronization overhead by maintaining individual random seeds.

A crucial optimization uses strides to explore the same size distribution as sequential QuickCheck. With k threads, thread i uses sizes i, i+k, i+2k, i+3k, ... This approach balances synchronization costs against test coverage consistency. When work-stealing occurs, threads use locally-computed sizes rather than synchronizing results.

Upon finding counterexamples, threads signal the main thread via MVar and trigger asynchronous exceptions terminating sibling testers before shrinking begins.

## graceful

Abrupt termination via asynchronous exceptions risks orphaned resources (unclosed files, dangling processes). The `graceful` combinator takes an I/O action and handler, executing the handler if QuickCheck terminates evaluation. This ensures cleanup occurs during both testing and shrinking phases, complementing existing exception handling.

## Shrinking

The parallel shrink loop spawns workers sharing a candidate list in an MVar. Finding a counterexample signals siblings to stop current evaluation and restart with the new list.

The deterministic variant only restarts workers evaluating later candidates, allowing earlier evaluations to complete. If earlier candidates also fail, progress is discarded and restarted. This guarantees sequential output at the cost of potential redundant computation.

The greedy variant restarts all workers immediately upon any counterexample discovery, potentially finding non-leftmost local minima but faster.

Shared resource contention risks performance degradation when candidates evaluate quickly; parallelism effectiveness depends on sufficient per-candidate execution time.

---

### النسخة العربية

## الاختبار

تنشئ حلقة الاختبار المتوازية نسخ مختبِر متزامنة تنفذ بشكل تسلسلي داخلياً، وتنسق من خلال MVars مشتركة. تتوزع ميزانيات الاختبار الأولية بالتساوي؛ تسرق الخيوط العمل عندما تكون خاملة، متجنبة التكلفة العامة للتزامن من خلال الحفاظ على بذور عشوائية فردية.

يستخدم التحسين الحاسم خطوات لاستكشاف نفس توزيع الحجم كما في QuickCheck التسلسلي. مع k خيط، يستخدم الخيط i الأحجام i، i+k، i+2k، i+3k، ... يوازن هذا النهج بين تكاليف التزامن واتساق تغطية الاختبار. عندما تحدث سرقة العمل، تستخدم الخيوط أحجاماً محسوبة محلياً بدلاً من مزامنة النتائج.

عند إيجاد أمثلة مضادة، ترسل الخيوط إشارة إلى الخيط الرئيسي عبر MVar وتطلق استثناءات غير متزامنة تنهي المختبِرين الشقيقين قبل أن يبدأ التقليص.

## graceful

تخاطر الإنهاء المفاجئ عبر الاستثناءات غير المتزامنة بموارد يتيمة (ملفات غير مغلقة، عمليات متدلية). يأخذ المجمِّع `graceful` إجراء إدخال/إخراج ومعالج، ينفذ المعالج إذا أنهى QuickCheck التقييم. يضمن هذا حدوث التنظيف خلال مرحلتي الاختبار والتقليص، مكملاً معالجة الاستثناءات الموجودة.

## التقليص

تنشئ حلقة التقليص المتوازية عمالاً يشاركون قائمة مرشحين في MVar. يشير إيجاد مثال مضاد إلى الأشقاء بإيقاف التقييم الحالي وإعادة البدء بالقائمة الجديدة.

يعيد المتغير الحتمي فقط بدء العمال الذين يقيمون مرشحين لاحقين، سامحاً للتقييمات السابقة بالاكتمال. إذا فشلت المرشحات السابقة أيضاً، يُتجاهل التقدم ويُعاد البدء. يضمن هذا المخرجات التسلسلية بتكلفة الحساب الزائد المحتمل.

يعيد المتغير الجشع بدء جميع العمال فوراً عند اكتشاف أي مثال مضاد، مما قد يجد نقاط دنيا محلية غير يسارية لكنه أسرع.

يخاطر التنافس على الموارد المشتركة بتدهور الأداء عندما يقيم المرشحون بسرعة؛ تعتمد فعالية التوازي على وقت تنفيذ كافٍ لكل مرشح.

---

### Translation Notes

- **Key terms introduced:**
  - Parallel testing loop = حلقة الاختبار المتوازية
  - Concurrent tester instances = نسخ مختبِر متزامنة
  - Execute sequentially internally = تنفذ بشكل تسلسلي داخلياً
  - Shared MVars = MVars مشتركة (MVar is Haskell synchronization primitive)
  - Test budgets = ميزانيات الاختبار
  - Work stealing = سرقة العمل
  - Synchronization overhead = التكلفة العامة للتزامن
  - Individual random seeds = بذور عشوائية فردية
  - Strides = خطوات (for size distribution)
  - Test coverage consistency = اتساق تغطية الاختبار
  - Locally-computed sizes = أحجام محسوبة محلياً
  - Main thread = الخيط الرئيسي
  - Asynchronous exceptions = استثناءات غير متزامنة
  - Sibling testers = المختبِرين الشقيقين
  - Abrupt termination = الإنهاء المفاجئ
  - Orphaned resources = موارد يتيمة
  - Unclosed files = ملفات غير مغلقة
  - Dangling processes = عمليات متدلية
  - Combinator = المجمِّع (functional programming term)
  - I/O action = إجراء إدخال/إخراج
  - Handler = معالج
  - Cleanup = التنظيف
  - Exception handling = معالجة الاستثناءات
  - Parallel shrink loop = حلقة التقليص المتوازية
  - Workers = عمال
  - Candidate list = قائمة مرشحين
  - Restart = إعادة البدء
  - Deterministic variant = المتغير الحتمي
  - Later candidates = مرشحين لاحقين
  - Earlier evaluations = التقييمات السابقة
  - Redundant computation = الحساب الزائد
  - Greedy variant = المتغير الجشع
  - Non-leftmost local minima = نقاط دنيا محلية غير يسارية
  - Shared resource contention = التنافس على الموارد المشتركة
  - Performance degradation = تدهور الأداء
  - Per-candidate execution time = وقت تنفيذ لكل مرشح

- **Code elements:**
  - Preserved `graceful` as code element
  - MVar is a Haskell concurrency primitive (kept as-is)

- **Technical concepts:**
  - Work-stealing scheduler
  - Stride-based size distribution
  - Asynchronous exception handling
  - Resource cleanup patterns
  - Deterministic vs greedy shrinking strategies
  - Trade-offs between parallelism and determinism

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-Translation Check

**Testing**
The parallel testing loop creates concurrent tester instances that execute sequentially internally, coordinating through shared MVars. Initial test budgets distribute equally; threads steal work when idle, avoiding synchronization overhead by maintaining individual random seeds.

The critical optimization uses strides to explore the same size distribution as sequential QuickCheck. With k threads, thread i uses sizes i, i+k, i+2k, i+3k, ... This approach balances synchronization costs with test coverage consistency. When work-stealing occurs, threads use locally-computed sizes instead of synchronizing results.

Upon finding counterexamples, threads signal the main thread via MVar and trigger asynchronous exceptions that terminate sibling testers before shrinking begins.

**graceful**
Abrupt termination via asynchronous exceptions risks orphaned resources (unclosed files, dangling processes). The `graceful` combinator takes an I/O action and handler, executing the handler if QuickCheck terminates evaluation. This ensures cleanup occurs during both testing and shrinking phases, complementing existing exception handling.

**Shrinking**
The parallel shrink loop creates workers that share a candidate list in an MVar. Finding a counterexample signals siblings to stop current evaluation and restart with the new list.

The deterministic variant only restarts workers evaluating later candidates, allowing earlier evaluations to complete. If earlier candidates also fail, progress is discarded and restarted. This guarantees sequential output at the cost of potential redundant computation.

The greedy variant restarts all workers immediately upon discovering any counterexample, potentially finding non-leftmost local minima but faster.

Shared resource contention risks performance degradation when candidates evaluate quickly; parallelism effectiveness depends on sufficient execution time per candidate.

✓ Back-translation accurately preserves technical details and implementation concepts.
