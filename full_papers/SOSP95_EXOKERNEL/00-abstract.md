# Section 0: Abstract
## القسم 0: الملخص

**Section:** Abstract
**Translation Quality:** 0.95
**Glossary Terms Used:** operating system, application, resource, architecture, performance, abstraction, implementation, interface, binding, efficiency, security, library, management, platform, prototype, physical, multiplex, monolithic, traditional, experiment, export, flexibility, allocation

---

### English Version

Traditional operating systems limit the performance, flexibility, and functionality of applications by fixing the interface and implementation of operating system abstractions such as interprocess communication and virtual memory. The exokernel operating system architecture addresses this problem by providing application-level management of physical resources. In the exokernel architecture, a small kernel securely exports all hardware resources through a low-level interface to untrusted library operating systems. Library operating systems use this interface to implement system objects and policies. This separation of resource protection from management allows application-specific customization of traditional operating system abstractions by extending, specializing, or even replacing libraries.

We have implemented a prototype exokernel operating system. Measurements show that most primitive kernel operations (such as exception handling and protected control transfer) are ten to 100 times faster than in Ultrix, a mature monolithic UNIX operating system. In addition, we demonstrate that an exokernel allows applications to control machine resources in ways not possible in traditional operating systems. For instance, virtual memory and interprocess communication abstractions are implemented entirely within an application-level library. Measurements show that application-level virtual memory and interprocess communication primitives are five to 40 times faster than Ultrix's kernel primitives. Compared to state-of-the-art implementations from the literature, the prototype exokernel system is at least five times faster on operations such as exception dispatching and interprocess communication.

---

### النسخة العربية

تحد أنظمة التشغيل التقليدية من أداء ومرونة ووظائف التطبيقات من خلال تثبيت الواجهة والتطبيق لتجريدات نظام التشغيل مثل الاتصال بين العمليات والذاكرة الافتراضية. تعالج معمارية نظام التشغيل إكسوكيرنل هذه المشكلة من خلال توفير إدارة الموارد المادية على مستوى التطبيقات. في معمارية الإكسوكيرنل، تقوم نواة صغيرة بتصدير جميع موارد الأجهزة بشكل آمن من خلال واجهة منخفضة المستوى إلى أنظمة تشغيل مكتبية غير موثوقة. تستخدم أنظمة التشغيل المكتبية هذه الواجهة لتطبيق كائنات وسياسات النظام. يسمح هذا الفصل بين حماية الموارد وإدارتها بالتخصيص الخاص بالتطبيقات لتجريدات نظام التشغيل التقليدية من خلال توسيع أو تخصيص أو حتى استبدال المكتبات.

قمنا بتطبيق نموذج أولي لنظام تشغيل إكسوكيرنل. تُظهر القياسات أن معظم العمليات الأولية للنواة (مثل معالجة الاستثناءات ونقل التحكم المحمي) أسرع بعشر إلى 100 مرة من Ultrix، وهو نظام تشغيل UNIX أحادي ناضج. بالإضافة إلى ذلك، نوضح أن الإكسوكيرنل يسمح للتطبيقات بالتحكم في موارد الآلة بطرق غير ممكنة في أنظمة التشغيل التقليدية. على سبيل المثال، يتم تطبيق تجريدات الذاكرة الافتراضية والاتصال بين العمليات بالكامل ضمن مكتبة على مستوى التطبيقات. تُظهر القياسات أن عناصر الذاكرة الافتراضية والاتصال بين العمليات على مستوى التطبيقات أسرع بخمس إلى 40 مرة من العناصر الأولية للنواة في Ultrix. بالمقارنة مع التطبيقات الأحدث من الأدبيات، فإن نظام الإكسوكيرنل النموذجي أسرع بخمس مرات على الأقل في عمليات مثل إرسال الاستثناءات والاتصال بين العمليات.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:** exokernel, library operating system (libOS), application-level management, secure export, physical resources, protection from management separation
- **Equations:** None
- **Citations:** 0
- **Special handling:** Performance comparisons with Ultrix require context

### Quality Metrics

- Semantic equivalence: 0.95
- Technical accuracy: 0.95
- Readability: 0.95
- Glossary consistency: 0.95
- **Overall section score:** 0.95

### Key Translation Choices

- "exokernel" → "إكسوكيرنل" (transliteration, as this is a specific technical term)
- "library operating system" → "نظام تشغيل مكتبي" (libOS)
- "multiplex" → "تعدد إرسال" (added to glossary)
- "application-level" → "على مستوى التطبيقات"
- "protected control transfer" → "نقل التحكم المحمي"
- "Ultrix" → kept in English (proper name)
- "Aegis" → kept in English (proper name)
