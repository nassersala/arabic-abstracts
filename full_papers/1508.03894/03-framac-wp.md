# Section 3: Frama-C, WP Plugin and Alt-Ergo
## القسم 3: Frama-C وإضافة WP و Alt-Ergo

**Section:** Frama-C, WP Plugin and Alt-Ergo
**Translation Quality:** 0.87
**Glossary Terms Used:** avionics (إلكترونيات الطيران), real-time (الوقت الفعلي), embedded (مدمجة), algorithm (خوارزمية), pointer (مؤشر), formal methods (الأساليب الرسمية)

---

### English Version

Avionics software is usually real-time, embedded, i.e. hardware related, resource constrained software that often implements complex arithmetic algorithms. One will find type casts, especially between integer and hardware addresses, and low level pointer handling, as well as floating point calculations.

Embedded projects often do not use an operating system so that the developer must directly access and manipulate the hardware.

The strict real-time requirements sometimes lead to the application of the most efficient programming constructs that may be difficult to verify with formal methods.

A formal notation and its supporting tools must address these constraints. This is the case with the open source tool platform Frama-C together with its WP plugin. Frama-C is organized into a plug-in architecture with a common kernel that allows the plug-ins to interact with each other using ACSL as lingua franca.

The WP plugin was selected because it well supports the aforementioned properties of avionics software. WP uses memory and arithmetic models in order to model memory management of dynamic structures (pointers) and properties of integer and real variables [3].

---

### النسخة العربية

عادةً ما تكون برمجيات إلكترونيات الطيران عاملة في الوقت الفعلي، ومدمجة، أي متعلقة بالعتاد، ومحدودة الموارد، وغالباً ما تنفذ خوارزميات حسابية معقدة. سيجد المرء تحويلات الأنواع، وخاصة بين الأعداد الصحيحة وعناوين العتاد، ومعالجة المؤشرات منخفضة المستوى، بالإضافة إلى حسابات الفاصلة العائمة.

غالباً ما لا تستخدم المشاريع المدمجة نظام تشغيل بحيث يجب على المطور الوصول مباشرة إلى العتاد ومعالجته.

تؤدي متطلبات الوقت الفعلي الصارمة أحياناً إلى تطبيق تركيبات البرمجة الأكثر كفاءة والتي قد يكون من الصعب التحقق منها باستخدام الأساليب الرسمية.

يجب أن يعالج التدوين الرسمي وأدوات دعمه هذه القيود. هذا هو الحال مع منصة الأدوات مفتوحة المصدر Frama-C مع إضافة WP الخاصة بها. يتم تنظيم Frama-C في معمارية إضافات مع نواة مشتركة تسمح للإضافات بالتفاعل مع بعضها البعض باستخدام ACSL كلغة مشتركة.

تم اختيار إضافة WP لأنها تدعم بشكل جيد الخصائص المذكورة أعلاه لبرمجيات إلكترونيات الطيران. يستخدم WP نماذج الذاكرة والحساب من أجل نمذجة إدارة الذاكرة للبنى الديناميكية (المؤشرات) وخصائص المتغيرات الصحيحة والحقيقية [3].

---

### Translation Notes

- **Key Terms:**
  - Real-time: الوقت الفعلي
  - Embedded: مدمجة
  - Hardware related: متعلقة بالعتاد
  - Resource constrained: محدودة الموارد
  - Type casts: تحويلات الأنواع
  - Hardware addresses: عناوين العتاد
  - Low level pointer handling: معالجة المؤشرات منخفضة المستوى
  - Floating point calculations: حسابات الفاصلة العائمة
  - Operating system: نظام تشغيل
  - Lingua franca: لغة مشتركة
  - Memory management: إدارة الذاكرة
  - Dynamic structures: البنى الديناميكية
  - Integer variables: المتغيرات الصحيحة
  - Real variables: المتغيرات الحقيقية

- **Citations:** [3]

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
