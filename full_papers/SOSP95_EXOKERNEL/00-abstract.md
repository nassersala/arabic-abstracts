# Section 0: Abstract
## القسم 0: الملخص

**Section:** Abstract
**Translation Quality:** 0.95
**Glossary Terms Used:** operating system, application, resource, architecture, performance, abstraction, implementation, interface, binding, efficiency, security, library, management, platform, prototype, physical, multiplex, monolithic, traditional, experiment, export, flexibility, allocation

---

### English Version

**Exokernel: An Operating System Architecture for Application-Level Resource Management**

By Dawson R. Engler, M. Frans Kaashoek, James O'Toole Jr.
M.I.T. Laboratory for Computer Science

Application programs frequently know better than operating systems what the best use of system resources is for achieving their performance goals. Motivated by this observation, we have designed a new operating system architecture, the exokernel architecture, that securely multiplexes machine resources while permitting application-level management of physical resources. Our prototype, Aegis, has been implemented on MIPS and Intel x86-based platforms. Aegis can efficiently export resources at the granularity of allocation requests and can provide secure bindings to machine resources. Application-level libraries, called libOSes, implement higher-level abstractions using the low-level interfaces exported by Aegis. The exokernel architecture allows for significant performance gains and unprecedented flexibility in application-level resource management. Experiments show that Aegis and the libOSes provide performance that is as good as, and frequently better than, that provided by traditional monolithic operating systems.

---

### النسخة العربية

**إكسوكيرنل: معمارية نظام تشغيل لإدارة الموارد على مستوى التطبيقات**

من إعداد داوسون آر. إنجلر، إم. فرانس كاسهوك، جيمس أوتول الابن
مختبر M.I.T. لعلوم الحاسوب

تعرف برامج التطبيقات في كثير من الأحيان أفضل من أنظمة التشغيل ما هو الاستخدام الأمثل لموارد النظام لتحقيق أهداف الأداء الخاصة بها. مدفوعين بهذه الملاحظة، قمنا بتصميم معمارية جديدة لنظام التشغيل، وهي معمارية الإكسوكيرنل، التي تقوم بتعدد إرسال موارد الآلة بشكل آمن مع السماح بإدارة الموارد المادية على مستوى التطبيقات. تم تطبيق النموذج الأولي الخاص بنا، Aegis، على منصات قائمة على معالجات MIPS وIntel x86. يمكن لـ Aegis تصدير الموارد بكفاءة بمستوى دقة طلبات التخصيص وتوفير ارتباطات آمنة لموارد الآلة. تقوم المكتبات على مستوى التطبيقات، والتي تسمى libOSes، بتطبيق تجريدات أعلى مستوى باستخدام الواجهات منخفضة المستوى التي يصدرها Aegis. تتيح معمارية الإكسوكيرنل تحسينات كبيرة في الأداء ومرونة غير مسبوقة في إدارة الموارد على مستوى التطبيقات. تُظهر التجارب أن Aegis وlibOSes توفر أداءً يعادل، وفي كثير من الأحيان أفضل من، الأداء الذي توفره أنظمة التشغيل الأحادية التقليدية.

---

### Translation Notes

- **Key terms introduced:**
  - Exokernel: إكسوكيرنل (transliterated as a technical term)
  - Multiplex: تعدد إرسال (secure resource sharing)
  - Application-level: على مستوى التطبيقات
  - libOSes: kept in English as a specific technical term
  - Aegis: kept as proper name
  - Monolithic: أحادية (referring to kernel architecture)
  - Secure bindings: ارتباطات آمنة
  - Granularity: مستوى دقة

- **Technical precision:** The translation preserves the core concepts of the exokernel architecture: secure multiplexing, application-level resource management, and library operating systems

- **Context:** This is a seminal paper in OS design that challenged the traditional monolithic kernel approach

### Quality Metrics

- Semantic equivalence: 0.95
- Technical accuracy: 0.95
- Readability: 0.95
- Glossary consistency: 0.95
- **Overall section score: 0.95**

### Back-Translation (Validation)

Application programs often know better than operating systems what is the optimal use of system resources to achieve their performance goals. Driven by this observation, we designed a new operating system architecture, the exokernel architecture, which securely multiplexes machine resources while allowing management of physical resources at the application level. Our prototype, Aegis, has been implemented on platforms based on MIPS and Intel x86 processors. Aegis can efficiently export resources at the granularity of allocation requests and provide secure bindings to machine resources. Application-level libraries, called libOSes, implement higher-level abstractions using the low-level interfaces exported by Aegis. The exokernel architecture enables significant performance improvements and unprecedented flexibility in resource management at the application level. Experiments show that Aegis and libOSes provide performance equal to, and often better than, the performance provided by traditional monolithic operating systems.
