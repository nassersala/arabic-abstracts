# Section 1: Introduction
## القسم 1: المقدمة

**Section:** Introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** operating system, abstraction, application, resource management, architecture, implementation, flexibility, performance, interface, hardware, kernel, virtual memory, file system, process

---

### English Version

**1. Introduction**

Traditional operating systems limit the performance and functionality of applications by fixing the interface and implementation of operating system abstractions. These fixed high-level abstractions hide information from applications and restrict functionality to the lowest common denominator. For instance, a relational database system may need direct access to disk blocks, a garbage collector may need to know which pages have been referenced, and a user-level threading system may need to control processor scheduling. Unfortunately, traditional operating systems force all applications to use the same abstractions, such as virtual memory, files, and processes, regardless of whether these abstractions match the application's needs.

The exokernel operating system architecture addresses this problem by providing application-level management of physical resources. An exokernel securely exports all hardware resources through a low-level interface to untrusted library operating systems. Library operating systems use this interface to implement higher-level abstractions, and applications can select or even build library operating systems specialized for their needs. This approach allows for unprecedented flexibility and performance because applications have the freedom to use resources in whatever ways are most appropriate for them.

The exokernel architecture separates resource protection from management. Traditional operating systems conflate these two concerns: the kernel both protects resources and manages them on behalf of applications. In contrast, an exokernel is responsible only for securely multiplexing resources. Management is left to library operating systems, which implement abstractions optimized for specific application domains. This separation of concerns is the key to the exokernel's efficiency and flexibility.

We have built a prototype exokernel called Aegis for MIPS and x86-based systems. Aegis exports processor time, physical memory, disk memory, TLB (translation lookaside buffer), and addressing context. We have also implemented a library operating system called ExOS that provides processes, virtual memory, and interprocess communication. Our measurements demonstrate that the exokernel approach can achieve excellent performance—often matching or exceeding that of specialized, hand-tuned implementations.

The primary contribution of this paper is the exokernel operating system architecture. Secondary contributions include the implementation and evaluation of Aegis and ExOS, which demonstrate that:

1. The exokernel architecture is practical and can be implemented efficiently
2. Applications can achieve high performance through application-level resource management
3. Library operating systems can implement traditional operating system abstractions with minimal overhead
4. The exokernel interface is sufficient to support diverse applications with different needs

The rest of this paper is organized as follows. Section 2 motivates the exokernel approach by examining the costs of fixed abstractions in traditional operating systems. Section 3 presents the exokernel architecture and its key design principles. Section 4 describes how exokernels implement secure bindings to resources. Section 5 describes the implementation of Aegis. Section 6 presents experimental results demonstrating the performance benefits of the exokernel approach. Section 7 discusses related work, and Section 8 concludes.

---

### النسخة العربية

**1. المقدمة**

تحد أنظمة التشغيل التقليدية من أداء ووظائف التطبيقات من خلال تثبيت واجهة وتنفيذ تجريدات نظام التشغيل. تخفي هذه التجريدات عالية المستوى الثابتة المعلومات عن التطبيقات وتقيد الوظائف إلى أدنى قاسم مشترك. على سبيل المثال، قد يحتاج نظام قاعدة بيانات علائقية إلى وصول مباشر إلى كتل القرص، وقد يحتاج جامع القمامة إلى معرفة الصفحات التي تمت الإشارة إليها، وقد يحتاج نظام الخيوط على مستوى المستخدم إلى التحكم في جدولة المعالج. لسوء الحظ، تجبر أنظمة التشغيل التقليدية جميع التطبيقات على استخدام نفس التجريدات، مثل الذاكرة الافتراضية والملفات والعمليات، بغض النظر عما إذا كانت هذه التجريدات تتطابق مع احتياجات التطبيق.

تعالج معمارية نظام التشغيل إكسوكيرنل هذه المشكلة من خلال توفير إدارة على مستوى التطبيقات للموارد المادية. يقوم الإكسوكيرنل بتصدير جميع موارد الأجهزة بشكل آمن من خلال واجهة منخفضة المستوى إلى أنظمة التشغيل المكتبية غير الموثوقة. تستخدم أنظمة التشغيل المكتبية هذه الواجهة لتطبيق تجريدات أعلى مستوى، ويمكن للتطبيقات اختيار أو حتى بناء أنظمة تشغيل مكتبية متخصصة لاحتياجاتها. يتيح هذا النهج مرونة وأداءً غير مسبوقين لأن التطبيقات لديها الحرية في استخدام الموارد بأي طرق تكون الأنسب لها.

تفصل معمارية الإكسوكيرنل حماية الموارد عن إدارتها. تدمج أنظمة التشغيل التقليدية هذين الشاغلين: تقوم النواة بحماية الموارد وإدارتها نيابة عن التطبيقات. في المقابل، يكون الإكسوكيرنل مسؤولاً فقط عن تعدد إرسال الموارد بشكل آمن. يُترك الإدارة لأنظمة التشغيل المكتبية، التي تطبق تجريدات محسّنة لمجالات تطبيقات معينة. هذا الفصل بين الشواغل هو المفتاح لكفاءة ومرونة الإكسوكيرنل.

لقد قمنا ببناء نموذج أولي للإكسوكيرنل يسمى Aegis لأنظمة قائمة على MIPS و x86. يصدر Aegis وقت المعالج والذاكرة المادية وذاكرة القرص و TLB (ذاكرة التخزين المؤقت للترجمة الجانبية) وسياق العنونة. كما قمنا بتطبيق نظام تشغيل مكتبي يسمى ExOS يوفر العمليات والذاكرة الافتراضية والاتصال بين العمليات. تُظهر قياساتنا أن نهج الإكسوكيرنل يمكن أن يحقق أداءً ممتازاً - غالباً ما يعادل أو يتجاوز أداء التطبيقات المتخصصة والمضبوطة يدوياً.

المساهمة الأساسية لهذه الورقة هي معمارية نظام التشغيل إكسوكيرنل. تشمل المساهمات الثانوية التطبيق والتقييم لـ Aegis و ExOS، والتي تُظهر أن:

1. معمارية الإكسوكيرنل عملية ويمكن تطبيقها بكفاءة
2. يمكن للتطبيقات تحقيق أداء عالٍ من خلال إدارة الموارد على مستوى التطبيقات
3. يمكن لأنظمة التشغيل المكتبية تطبيق تجريدات نظام التشغيل التقليدية مع حد أدنى من النفقات العامة
4. واجهة الإكسوكيرنل كافية لدعم تطبيقات متنوعة باحتياجات مختلفة

يتم تنظيم بقية هذه الورقة على النحو التالي. يحفز القسم 2 نهج الإكسوكيرنل من خلال فحص تكاليف التجريدات الثابتة في أنظمة التشغيل التقليدية. يقدم القسم 3 معمارية الإكسوكيرنل ومبادئ التصميم الرئيسية. يصف القسم 4 كيفية تطبيق الإكسوكيرنلات للارتباطات الآمنة بالموارد. يصف القسم 5 تطبيق Aegis. يقدم القسم 6 نتائج تجريبية توضح فوائد الأداء لنهج الإكسوكيرنل. يناقش القسم 7 الأعمال ذات الصلة، ويختتم القسم 8.

---

### Translation Notes

- **Key terms introduced:**
  - Fixed abstractions: تجريدات ثابتة
  - Lowest common denominator: أدنى قاسم مشترك
  - Library operating system: نظام تشغيل مكتبي
  - Untrusted: غير موثوقة
  - Resource protection: حماية الموارد
  - Secure multiplexing: تعدد إرسال آمن
  - TLB (Translation Lookaside Buffer): ذاكرة التخزين المؤقت للترجمة الجانبية
  - Addressing context: سياق العنونة
  - Hand-tuned: مضبوطة يدوياً
  - Overhead: النفقات العامة

- **Technical precision:** The translation preserves the key architectural concepts: separation of protection from management, library operating systems, and secure resource multiplexing

- **Context:** This introduction establishes the fundamental problem with traditional OSes and introduces the exokernel solution

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score: 0.88**

### Back-Translation (Validation)

Traditional operating systems limit the performance and functionality of applications by fixing the interface and implementation of operating system abstractions. These fixed high-level abstractions hide information from applications and restrict functionality to the lowest common denominator. For example, a relational database system may need direct access to disk blocks, a garbage collector may need to know which pages were referenced, and a user-level thread system may need to control processor scheduling. Unfortunately, traditional operating systems force all applications to use the same abstractions, such as virtual memory, files, and processes, regardless of whether these abstractions match the application's needs.

The exokernel operating system architecture addresses this problem by providing application-level management of physical resources. The exokernel securely exports all hardware resources through a low-level interface to untrusted library operating systems. Library operating systems use this interface to implement higher-level abstractions, and applications can select or even build library operating systems specialized for their needs. This approach enables unprecedented flexibility and performance because applications have the freedom to use resources in whatever ways are most appropriate for them.
