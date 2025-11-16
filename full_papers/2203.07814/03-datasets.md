# Section 3: Datasets
## القسم 3: مجموعات البيانات

**Section:** datasets
**Translation Quality:** 0.88
**Glossary Terms Used:** مجموعة بيانات, تدريب مسبق, ضبط دقيق, تصفية, معيار, اختبار, البرمجة التنافسية, إيجابية خاطئة

---

### English Version

## 3.1 Pre-training Dataset

The researchers built their foundational model using "a snapshot of selected public GitHub repositories taken on 2021/07/14." Their dataset encompassed twelve programming languages including C++, Python, Java, and others. They implemented standard filtering procedures, removing files exceeding 1MB and lines longer than 1000 characters to exclude automatically generated code. The final pre-training corpus contained approximately 715 gigabytes of code across all languages.

## 3.2 CodeContests Fine-tuning Dataset

The team created a new competitive programming dataset by combining multiple sources: freshly scraped Codeforces problems alongside existing datasets (Description2Code and CodeNet). A crucial feature was their temporal split strategy—"all pre-training and fine-tuning training data appeared online before any validation problems, and all validation problems before test ones." This prevented data leakage where unseen test problems could theoretically appear in training materials.

The dataset contained substantial statistics: approximately 13,328 training problems, 117 validation problems, and 165 test problems. Each problem included multiple test cases (averaging 2.0 example tests and 14.8 hidden tests in training data) and several solution submissions across C++, Python, and Java.

### 3.2.1 False Positives and Additional Generated Tests

A significant contribution involved addressing test coverage limitations. Existing datasets suffered from high false positive rates—where incorrect submissions appeared correct due to insufficient testing. The researchers generated additional test cases "by mutating existing test inputs" through bit flips, integer modifications, and character swaps. These mutations were validated by "running 30 correct solutions on them, checking that all solutions produce the same output."

The improvements were substantial: "generated tests and filtering reduced false positive rates from 62% to 4%." This represented a dramatic improvement over prior benchmarks like APPS (60% false positive rate) and HumanEval (30% rate). The enhancement ensured more reliable evaluation of submitted code solutions.

---

### النسخة العربية

## 3.1 مجموعة بيانات التدريب المسبق

بنى الباحثون نموذجهم الأساسي باستخدام "لقطة من مستودعات GitHub العامة المختارة مأخوذة في 2021/07/14". شملت مجموعة البيانات الخاصة بهم اثنتي عشرة لغة برمجة بما في ذلك ++C وبايثون وجافا وغيرها. نفذوا إجراءات تصفية قياسية، بإزالة الملفات التي تتجاوز 1 ميجابايت والأسطر الأطول من 1000 حرف لاستبعاد الشفرة المولدة تلقائياً. احتوت مدونة التدريب المسبق النهائية على ما يقرب من 715 جيجابايت من الشفرة البرمجية عبر جميع اللغات.

## 3.2 مجموعة بيانات CodeContests للضبط الدقيق

أنشأ الفريق مجموعة بيانات جديدة للبرمجة التنافسية من خلال دمج مصادر متعددة: مشاكل Codeforces المستخرجة حديثاً إلى جانب مجموعات البيانات الحالية (Description2Code و CodeNet). كانت الميزة الحاسمة هي استراتيجية التقسيم الزمني الخاصة بهم - "ظهرت جميع بيانات التدريب المسبق وبيانات تدريب الضبط الدقيق عبر الإنترنت قبل أي مشاكل تحقق، وظهرت جميع مشاكل التحقق قبل مشاكل الاختبار". منع هذا تسرب البيانات حيث يمكن نظرياً أن تظهر مشاكل الاختبار غير المرئية في مواد التدريب.

احتوت مجموعة البيانات على إحصائيات كبيرة: حوالي 13,328 مشكلة تدريب، و 117 مشكلة تحقق، و 165 مشكلة اختبار. تضمنت كل مشكلة حالات اختبار متعددة (بمتوسط 2.0 اختبار مثال و 14.8 اختبار مخفي في بيانات التدريب) وعدة حلول مقدمة عبر ++C وبايثون وجافا.

### 3.2.1 الإيجابيات الخاطئة والاختبارات المولدة الإضافية

تضمنت مساهمة كبيرة معالجة قيود التغطية الاختبارية. عانت مجموعات البيانات الحالية من معدلات إيجابية خاطئة عالية - حيث بدت الحلول المقدمة غير الصحيحة صحيحة بسبب الاختبار غير الكافي. ولّد الباحثون حالات اختبار إضافية "عن طريق تحوير مدخلات الاختبار الموجودة" من خلال قلب البتات، وتعديلات الأعداد الصحيحة، وتبديل الأحرف. تم التحقق من صحة هذه التحويرات "عن طريق تشغيل 30 حلاً صحيحاً عليها، والتحقق من أن جميع الحلول تنتج نفس المخرجات".

كانت التحسينات كبيرة: "خفضت الاختبارات المولدة والتصفية معدلات الإيجابية الخاطئة من 62% إلى 4%". مثل هذا تحسناً كبيراً مقارنة بالمعايير السابقة مثل APPS (معدل إيجابية خاطئة 60%) و HumanEval (معدل 30%). ضمن هذا التحسين تقييماً أكثر موثوقية للحلول البرمجية المقدمة.

---

### Translation Notes

- **Subsections:** 3.1 Pre-training dataset, 3.2 CodeContests fine-tuning dataset, 3.2.1 False positives and additional generated tests

- **Key terms introduced:**
  - pre-training dataset (مجموعة بيانات التدريب المسبق)
  - fine-tuning dataset (مجموعة بيانات الضبط الدقيق)
  - GitHub repositories (مستودعات GitHub)
  - filtering procedures (إجراءات تصفية)
  - corpus (مدونة)
  - CodeContests dataset (مجموعة بيانات CodeContests)
  - temporal split strategy (استراتيجية التقسيم الزمني)
  - data leakage (تسرب البيانات)
  - validation problems (مشاكل التحقق)
  - test cases (حالات اختبار)
  - example tests (اختبارات الأمثلة)
  - hidden tests (اختبارات مخفية)
  - false positive rate (معدل الإيجابية الخاطئة)
  - test coverage (التغطية الاختبارية)
  - bit flips (قلب البتات)
  - mutations (تحويرات)

- **Numbers and statistics:**
  - Snapshot date: 2021/07/14 preserved
  - 12 programming languages preserved
  - 1MB file size limit preserved
  - 1000 characters line length limit preserved
  - 715 gigabytes corpus size preserved
  - 13,328 training problems preserved
  - 117 validation problems preserved
  - 165 test problems preserved
  - 2.0 average example tests preserved
  - 14.8 average hidden tests preserved
  - 30 correct solutions for validation preserved
  - 62% → 4% false positive rate reduction preserved
  - APPS: 60% false positive rate preserved
  - HumanEval: 30% false positive rate preserved

- **Platform/Dataset names:** GitHub, Codeforces, Description2Code, CodeNet, APPS, HumanEval - kept in English as proper nouns

- **Programming languages:** C++, Python, Java - kept in English as standard practice

- **Direct quotes:** Preserved in quotation marks in both versions

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.88

### Back-Translation Validation

The Arabic translation accurately conveys: the pre-training dataset construction from GitHub repositories (snapshot date 2021/07/14, 12 languages including C++/Python/Java, filtering for files >1MB and lines >1000 characters, final 715GB corpus), the CodeContests fine-tuning dataset creation (combining Codeforces, Description2Code, and CodeNet sources, temporal split strategy to prevent data leakage, statistics of 13,328 training/117 validation/165 test problems with average 2.0 example tests and 14.8 hidden tests), and the false positive problem solution (high rates in existing datasets, generation of additional test cases through mutations, validation with 30 correct solutions, dramatic reduction from 62% to 4%, comparison with APPS 60% and HumanEval 30%).
