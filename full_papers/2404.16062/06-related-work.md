# Section 6: Related Work
## القسم 6: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.86
**Glossary Terms Used:** property-based testing, parallel execution, thread-safety, test drivers

---

### English Version

Most QuickCheck implementations across languages lack parallel support. FsCheck (.NET) independently discovered stride-based size distribution after initially using offsets. Hypothesis (Python) deliberately avoids parallelism due to thread-safety uncertainty in non-pure languages.

Tasty enables parallel execution across multiple independent tests but cannot introduce parallelism within individual test drivers. This leaves execution sequential when test suites contain few slow tests.

---

### النسخة العربية

تفتقر معظم تطبيقات QuickCheck عبر اللغات إلى دعم التوازي. اكتشف FsCheck (بيئة .NET) بشكل مستقل توزيع الحجم القائم على الخطوات بعد استخدام الإزاحات في البداية. يتجنب Hypothesis (بيئة Python) التوازي عمداً بسبب عدم اليقين في أمان الخيوط في اللغات غير النقية.

يمكّن Tasty من التنفيذ المتوازي عبر اختبارات مستقلة متعددة لكنه لا يمكنه إدخال التوازي داخل محركات الاختبار الفردية. يترك هذا التنفيذ تسلسلياً عندما تحتوي مجموعات الاختبار على اختبارات بطيئة قليلة.

---

### Translation Notes

- **Key terms introduced:**
  - QuickCheck implementations = تطبيقات QuickCheck
  - Across languages = عبر اللغات
  - Parallel support = دعم التوازي
  - FsCheck = FsCheck (proper noun, .NET testing library)
  - .NET = بيئة .NET
  - Independently discovered = اكتشف بشكل مستقل
  - Stride-based size distribution = توزيع الحجم القائم على الخطوات
  - Offsets = الإزاحات
  - Hypothesis = Hypothesis (proper noun, Python testing library)
  - Python = بيئة Python
  - Deliberately avoids = يتجنب عمداً
  - Thread-safety uncertainty = عدم اليقين في أمان الخيوط
  - Non-pure languages = اللغات غير النقية
  - Tasty = Tasty (proper noun, Haskell testing framework)
  - Parallel execution = التنفيذ المتوازي
  - Independent tests = اختبارات مستقلة
  - Introduce parallelism = إدخال التوازي
  - Individual test drivers = محركات الاختبار الفردية
  - Sequential execution = التنفيذ التسلسلي
  - Test suites = مجموعات الاختبار
  - Few slow tests = اختبارات بطيئة قليلة

- **Library/Framework names:**
  - Kept as proper nouns: FsCheck, Hypothesis, Tasty
  - Added context for language/platform: .NET, Python, Haskell

- **Technical concepts:**
  - Comparison of parallel testing approaches across different implementations
  - Stride-based vs offset-based size distribution
  - Limitations of test-level parallelism
  - Thread-safety challenges in impure languages

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86

### Back-Translation Check

Most QuickCheck implementations across languages lack parallel support. FsCheck (.NET environment) independently discovered stride-based size distribution after initially using offsets. Hypothesis (Python environment) deliberately avoids parallelism due to uncertainty in thread-safety in non-pure languages.

Tasty enables parallel execution across multiple independent tests but cannot introduce parallelism within individual test drivers. This leaves execution sequential when test suites contain few slow tests.

✓ Back-translation preserves comparative analysis and technical distinctions.
