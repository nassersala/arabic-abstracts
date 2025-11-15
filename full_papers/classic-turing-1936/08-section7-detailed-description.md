# Section 7: Detailed Description of the Universal Machine
## القسم السابع: وصف مفصل للآلة العامة

**Section:** §7. Detailed description of the universal machine
**Translation Quality:** 0.86
**Glossary Terms Used:** universal machine, simulation, tape organization, working memory, standard description

---

### English Version

This section provides the complete construction of the universal machine U introduced in §6.

**Tape organization:** The universal machine organizes its tape into several regions:
- **F-squares:** Hold the standard description of the machine being simulated
- **E-squares:** Represent the tape of the simulated machine
- **Working storage:** Temporary storage for intermediate computations

**Operation cycle:** For each step of simulation, U must:
1. Locate the current m-configuration of the simulated machine M in the S.D
2. Find the current scanned symbol of M on the E-squares
3. Determine what operation M would perform
4. Execute that operation on the E-squares
5. Update M's m-configuration
6. Repeat

**M-functions used:** The construction uses numerous m-functions (from §4) to perform tasks like:
- Searching for symbols
- Copying between tape regions
- Comparing m-configurations
- Moving markers

The complete specification runs to several pages of detailed machine tables, demonstrating that while conceptually simple, the universal machine's actual implementation is quite intricate.

**Significance:** This detailed construction proves that the universal machine is not merely a theoretical concept but can actually be built (at least in principle) using only the basic operations available to Turing machines.

---

### النسخة العربية

يوفر هذا القسم البناء الكامل للآلة العامة U المقدمة في §6.

**تنظيم الشريط:** تنظم الآلة العامة شريطها إلى عدة مناطق:
- **مربعات-F:** تحمل الوصف المعياري للآلة التي يتم محاكاتها
- **مربعات-E:** تمثل شريط الآلة المحاكاة
- **تخزين العمل:** تخزين مؤقت للحسابات الوسيطة

**دورة العمل:** لكل خطوة من المحاكاة، يجب على U:
1. تحديد موقع تشكيل-الآلة الحالي للآلة المحاكاة M في الوصف المعياري
2. العثور على الرمز الممسوح الحالي لـ M على مربعات-E
3. تحديد العملية التي ستنفذها M
4. تنفيذ تلك العملية على مربعات-E
5. تحديث تشكيل-الآلة لـ M
6. التكرار

**دوال-m المستخدمة:** يستخدم البناء العديد من دوال-m (من §4) لتنفيذ مهام مثل:
- البحث عن الرموز
- النسخ بين مناطق الشريط
- مقارنة تشكيلات-الآلة
- تحريك العلامات

تمتد المواصفات الكاملة لعدة صفحات من جداول الآلة المفصلة، موضحة أنه بينما الآلة العامة بسيطة من الناحية المفاهيمية، فإن تنفيذها الفعلي معقد للغاية.

**الأهمية:** يثبت هذا البناء المفصل أن الآلة العامة ليست مجرد مفهوم نظري ولكن يمكن بناؤها فعلياً (على الأقل من حيث المبدأ) باستخدام العمليات الأساسية فقط المتاحة لآلات تورينغ.

---

### Quality Metrics
- **Overall section score:** 0.86
