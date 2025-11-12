# Exokernel: An Operating System Architecture for Application-Level Resource Management
## إكسوكيرنل: معمارية نظام تشغيل لإدارة الموارد على مستوى التطبيقات

**Publication:** SOSP '95 (Symposium on Operating Systems Principles)
**Authors:** Dawson R. Engler, M. Frans Kaashoek, James O'Toole Jr.
**Year:** 1995
**Venue:** Fifteenth ACM Symposium on Operating Systems Principles
**Translation Quality:** 0.95
**Glossary Terms Used:** operating system, application, resource, architecture, performance, abstraction, implementation, interface, binding, efficiency, security, library, management, platform, prototype, physical, multiplex, monolithic, traditional, experiment, export, flexibility, allocation

### English Abstract
Application programs frequently know better than operating systems what the best use of system resources is for achieving their performance goals. Motivated by this observation, we have designed a new operating system architecture, the exokernel architecture, that securely multiplexes machine resources while permitting application-level management of physical resources. Our prototype, Aegis, has been implemented on MIPS and Intel x86-based platforms. Aegis can efficiently export resources at the granularity of allocation requests and can provide secure bindings to machine resources. Application-level libraries, called libOSes, implement higher-level abstractions using the low-level interfaces exported by Aegis. The exokernel architecture allows for significant performance gains and unprecedented flexibility in application-level resource management. Experiments show that Aegis and the libOSes provide performance that is as good as, and frequently better than, that provided by traditional monolithic operating systems.

### الملخص العربي
تعرف برامج التطبيقات في كثير من الأحيان أفضل من أنظمة التشغيل ما هو الاستخدام الأمثل لموارد النظام لتحقيق أهداف الأداء الخاصة بها. مدفوعين بهذه الملاحظة، قمنا بتصميم معمارية جديدة لنظام التشغيل، وهي معمارية الإكسوكيرنل، التي تقوم بتعدد إرسال موارد الآلة بشكل آمن مع السماح بإدارة الموارد المادية على مستوى التطبيقات. تم تطبيق النموذج الأولي الخاص بنا، Aegis، على منصات قائمة على معالجات MIPS وIntel x86. يمكن لـ Aegis تصدير الموارد بكفاءة بمستوى دقة طلبات التخصيص وتوفير ارتباطات آمنة لموارد الآلة. تقوم المكتبات على مستوى التطبيقات، والتي تسمى libOSes، بتطبيق تجريدات أعلى مستوى باستخدام الواجهات منخفضة المستوى التي يصدرها Aegis. تتيح معمارية الإكسوكيرنل تحسينات كبيرة في الأداء ومرونة غير مسبوقة في إدارة الموارد على مستوى التطبيقات. تُظهر التجارب أن Aegis وlibOSes توفر أداءً يعادل، وفي كثير من الأحيان أفضل من، الأداء الذي توفره أنظمة التشغيل الأحادية التقليدية.

### Back-Translation (Validation)
Application programs often know better than operating systems what is the optimal use of system resources to achieve their performance goals. Driven by this observation, we designed a new operating system architecture, the exokernel architecture, which securely multiplexes machine resources while allowing management of physical resources at the application level. Our prototype, Aegis, has been implemented on platforms based on MIPS and Intel x86 processors. Aegis can efficiently export resources at the granularity of allocation requests and provide secure bindings to machine resources. Application-level libraries, called libOSes, implement higher-level abstractions using the low-level interfaces exported by Aegis. The exokernel architecture enables significant performance improvements and unprecedented flexibility in resource management at the application level. Experiments show that Aegis and libOSes provide performance equal to, and often better than, the performance provided by traditional monolithic operating systems.

### Translation Metrics
- Iterations: 1
- Final Score: 0.95
- Quality: High

### Scoring Breakdown
- **Semantic equivalence:** 0.95 - Captures all key concepts accurately
- **Technical accuracy:** 0.95 - All technical terms correctly translated using glossary
- **Completeness:** 1.0 - Nothing omitted from original abstract
- **Coherence:** 0.95 - Flows naturally in Modern Standard Arabic
- **Consistency with glossary:** 0.90 - Uses existing glossary terms where available

### Notes
This is a seminal paper in operating systems from SOSP 1995. The exokernel architecture represents a significant departure from traditional monolithic OS design by pushing resource management to the application level while maintaining secure multiplexing at the kernel level. The translation preserves the technical precision of terms like "multiplex," "binding," "libOSes," and "granularity" which are critical to understanding the architecture's novelty.

Key translation choices:
- "exokernel" → "إكسوكيرنل" (transliteration, as this is a specific technical term)
- "multiplex" → "تعدد إرسال" (newly added to glossary)
- "application-level" → "على مستوى التطبيقات" (newly added to glossary)
- "libOSes" → left in English as it's a specific term from the paper
- "Aegis" → left in English as it's a proper name

The translation maintains the formal academic tone appropriate for a systems research paper while ensuring accessibility to Arabic-speaking computer science students and researchers.
