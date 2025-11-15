# Section 4: Abbreviated Tables
## القسم الرابع: الجداول المختصرة

**Section:** §4. Abbreviated tables
**Translation Quality:** 0.87
**Glossary Terms Used:** machine table, m-functions, skeleton tables, abbreviation, notation

---

### English Version

To make the description of computing machines more manageable, Turing introduces a system of abbreviations and higher-level constructs, similar to subroutines in modern programming.

**M-functions:** These are named sequences of operations that can be invoked repeatedly. An m-function is like a subroutine: it performs a specific task (such as "find the next blank square" or "copy a symbol") and can be called from multiple places in the machine's operation.

**Skeleton tables:** These are machine tables that contain calls to m-functions rather than spelling out every individual operation. This makes complex machines easier to design and understand.

**Example m-functions:**
- **f(𝔉, b, a)**: Find the next square marked with symbol b to the right of the current position, and change to m-configuration a
- **e(a)**: Erase the current square and change to m-configuration a
- **r(a)**, **l(a)**: Move right or left and change to m-configuration a

These abbreviations significantly reduce the complexity of machine descriptions while maintaining precise semantics. A skeleton table using m-functions can be expanded into a complete standard description by replacing each m-function call with its full definition.

This notational innovation makes it practical to describe complex computing machines, including the universal machine constructed in later sections.

---

### النسخة العربية

لجعل وصف آلات الحوسبة أكثر قابلية للإدارة، يقدم تورينغ نظاماً من الاختصارات والبنى عالية المستوى، مشابهاً للإجراءات الفرعية في البرمجة الحديثة.

**دوال-m:** هي تسلسلات مسماة من العمليات يمكن استدعاؤها بشكل متكرر. دالة-m تشبه إجراءً فرعياً: تنفذ مهمة محددة (مثل "ابحث عن المربع الفارغ التالي" أو "انسخ رمزاً") ويمكن استدعاؤها من أماكن متعددة في عمل الآلة.

**الجداول الهيكلية:** هي جداول آلة تحتوي على استدعاءات لدوال-m بدلاً من تفصيل كل عملية فردية. هذا يجعل الآلات المعقدة أسهل في التصميم والفهم.

**أمثلة على دوال-m:**
- **f(𝔉, b, a)**: ابحث عن المربع التالي الموسوم بالرمز b إلى يمين الموضع الحالي، وتغير إلى تشكيل-الآلة a
- **e(a)**: امسح المربع الحالي وتغير إلى تشكيل-الآلة a
- **r(a)**، **l(a)**: تحرك يميناً أو يساراً وتغير إلى تشكيل-الآلة a

تقلل هذه الاختصارات بشكل كبير من تعقيد أوصاف الآلة مع الحفاظ على الدلالات الدقيقة. يمكن توسيع جدول هيكلي يستخدم دوال-m إلى وصف معياري كامل عن طريق استبدال كل استدعاء لدالة-m بتعريفها الكامل.

هذا الابتكار الترميزي يجعل من العملي وصف آلات الحوسبة المعقدة، بما في ذلك الآلة العامة المبنية في الأقسام اللاحقة.

---

### Quality Metrics
- **Overall section score:** 0.87
