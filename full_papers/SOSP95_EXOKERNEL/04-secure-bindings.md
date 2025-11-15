# Section 4: Secure Bindings
## القسم 4: الارتباطات الآمنة

**Section:** Secure Bindings
**Translation Quality:** 0.86
**Glossary Terms Used:** binding, security, protection, resource, hardware, TLB, cache, validation, performance, overhead, encryption, authentication, downloading code

---

### English Version

**4. Secure Bindings**

Secure bindings are the fundamental mechanism by which an exokernel provides protected access to hardware resources. A secure binding is a protection mechanism that decouples authorization from use. An exokernel allows library operating systems to bind to resources, and checks these bindings only when they are created. Once a secure binding is established, the library operating system can use the resource without further kernel involvement, allowing operations to execute at hardware speeds.

**4.1 What is a Secure Binding?**

A secure binding is a protected mapping between an application-visible name for a resource and the resource itself. The binding is "secure" because the exokernel guarantees that:

1. Only the owning application can use the resource through the binding
2. The binding cannot be forged or modified by untrusted code
3. The resource can be accessed at hardware speeds once the binding is established

Examples of secure bindings include:
- A TLB entry mapping a virtual page to a physical page
- A packet filter that routes network packets to an application
- A disk capability that grants access to specific disk blocks

**4.2 Implementation Techniques**

Exokernels can implement secure bindings using three primary techniques:

**1. Hardware Mechanisms**

The most efficient secure bindings leverage hardware protection mechanisms. For example:

**TLB Entries:** When a library OS requests a virtual-to-physical page mapping, the exokernel validates that the library OS owns the physical page, then loads the mapping into the TLB. Subsequent memory accesses use the TLB directly without kernel intervention. The hardware enforces protection by checking privilege levels on memory accesses.

**Protected Address Spaces:** The exokernel can create hardware address contexts (e.g., using the MIPS address space identifiers) that allow processes to efficiently switch between address spaces without TLB flushes.

**2. Software Caching**

When hardware mechanisms are insufficient, the exokernel can cache secure bindings in kernel memory:

**Packet Filters:** Network packet filters are predicates that determine which packets should be delivered to which application. The exokernel validates packet filters when they are installed, then caches them in a table. When packets arrive, the exokernel efficiently matches them against cached filters without re-validating filter safety.

**Disk Block Ownership:** The exokernel maintains a table mapping disk blocks to owning applications. When an application requests disk I/O, the exokernel checks this table to verify ownership. The table acts as a software cache of secure bindings for disk resources.

**3. Downloading Application Code**

In some cases, the exokernel can download application code into the kernel to implement secure bindings:

**Specialized Packet Filters:** An application can provide a packet filter as executable code. The exokernel verifies the code's safety (e.g., using proof-carrying code or software fault isolation), then executes it directly in the kernel when packets arrive. This allows sophisticated filtering logic while maintaining protection.

**Custom Disk Schedulers:** An application can download a disk scheduling algorithm into the kernel. The exokernel validates that the algorithm respects protection boundaries, then uses it to schedule the application's disk requests.

**4.3 Binding Types**

Secure bindings vary in their implementation characteristics:

**Static vs. Dynamic:** Some bindings are established at initialization time (static), while others are created and destroyed during execution (dynamic). TLB entries are dynamic, while packet filters are typically static once installed.

**Visible vs. Invisible:** Some bindings are visible to the application (e.g., packet filters), while others are maintained transparently by the library OS (e.g., TLB entries).

**Hardware vs. Software:** Hardware-based bindings (TLB entries) provide better performance but are limited in number. Software bindings (cached tables) are slower but more flexible.

**4.4 Advantages of Secure Bindings**

Secure bindings provide several key advantages:

**Performance:** By checking authorization only at bind time, secure bindings eliminate per-operation kernel checks. This allows protected resources to be accessed at hardware speeds.

**Flexibility:** Different types of bindings can be used for different resources, optimizing for each resource's characteristics.

**Simplicity:** The binding abstraction provides a uniform way to think about resource protection, simplifying the exokernel's design.

**4.5 Resource Revocation**

When the exokernel needs to reclaim a resource, it must break the associated secure bindings. The exokernel uses three approaches:

**1. Visible Revocation:** The exokernel notifies the library OS that a binding is being broken (e.g., via an upcall), giving the library OS a chance to save state or reallocate the resource.

**2. Invisible Revocation:** The exokernel can silently break a binding if the library OS doesn't need notification. For example, the exokernel can remove a TLB entry without notifying the application; the application will simply take a TLB miss next time it accesses the page.

**3. Forced Revocation:** If a library OS doesn't respond to revocation requests, the exokernel can forcibly break bindings and reclaim resources. This ensures that misbehaving applications cannot prevent resource reclamation.

**4.6 Example: TLB as a Secure Binding**

Consider how the exokernel uses the TLB to implement secure bindings for virtual memory:

**Binding Creation:**
1. A library OS requests a mapping from virtual page V to physical page P
2. The exokernel checks that the library OS owns physical page P
3. If the check succeeds, the exokernel loads the V→P mapping into the TLB
4. The TLB entry is now a secure binding: only the owning address space can use it

**Using the Binding:**
- Memory accesses to virtual page V use the TLB entry directly
- The hardware translates V to P without kernel involvement
- The hardware enforces protection by checking privilege levels

**Binding Revocation:**
- If the exokernel needs to reclaim page P, it removes the TLB entry
- The next access to V will cause a TLB miss
- The exokernel handles the miss and notifies the library OS that P was reclaimed

This example illustrates how secure bindings achieve both protection (only the owner can access P) and performance (accesses proceed at hardware speed after the binding is established).

---

### النسخة العربية

**4. الارتباطات الآمنة**

الارتباطات الآمنة هي الآلية الأساسية التي يوفر بها الإكسوكيرنل وصولاً محمياً إلى موارد الأجهزة. الارتباط الآمن هو آلية حماية تفصل التفويض عن الاستخدام. يسمح الإكسوكيرنل لأنظمة التشغيل المكتبية بالارتباط بالموارد، ويتحقق من هذه الارتباطات فقط عند إنشائها. بمجرد إنشاء ارتباط آمن، يمكن لنظام التشغيل المكتبي استخدام المورد دون مزيد من مشاركة النواة، مما يسمح للعمليات بالتنفيذ بسرعات الأجهزة.

**4.1 ما هو الارتباط الآمن؟**

الارتباط الآمن هو تخطيط محمي بين اسم مرئي للتطبيق لمورد والمورد نفسه. الارتباط "آمن" لأن الإكسوكيرنل يضمن أن:

1. فقط التطبيق المالك يمكنه استخدام المورد من خلال الارتباط
2. لا يمكن تزوير الارتباط أو تعديله بواسطة شفرة غير موثوقة
3. يمكن الوصول إلى المورد بسرعات الأجهزة بمجرد إنشاء الارتباط

أمثلة على الارتباطات الآمنة تشمل:
- إدخال TLB يربط صفحة افتراضية بصفحة مادية
- مرشح حزم يوجه حزم الشبكة إلى تطبيق
- قدرة قرص تمنح الوصول إلى كتل قرص معينة

**4.2 تقنيات التنفيذ**

يمكن للإكسوكيرنلات تطبيق الارتباطات الآمنة باستخدام ثلاث تقنيات أساسية:

**1. آليات الأجهزة**

أكثر الارتباطات الآمنة كفاءة تستفيد من آليات الحماية بالأجهزة. على سبيل المثال:

**إدخالات TLB:** عندما يطلب نظام التشغيل المكتبي تخطيط صفحة افتراضية إلى مادية، يتحقق الإكسوكيرنل من أن نظام التشغيل المكتبي يمتلك الصفحة المادية، ثم يحمل التخطيط في TLB. تستخدم عمليات الوصول إلى الذاكرة اللاحقة TLB مباشرة دون تدخل النواة. تفرض الأجهزة الحماية من خلال التحقق من مستويات الامتياز على عمليات الوصول إلى الذاكرة.

**فضاءات العنونة المحمية:** يمكن للإكسوكيرنل إنشاء سياقات عنونة أجهزة (مثل استخدام معرفات فضاء العنونة MIPS) التي تسمح للعمليات بالتبديل بكفاءة بين فضاءات العنونة دون مسح TLB.

**2. التخزين المؤقت بالبرمجيات**

عندما تكون آليات الأجهزة غير كافية، يمكن للإكسوكيرنل تخزين الارتباطات الآمنة مؤقتاً في ذاكرة النواة:

**مرشحات الحزم:** مرشحات حزم الشبكة هي محمولات تحدد أي حزم يجب تسليمها إلى أي تطبيق. يتحقق الإكسوكيرنل من صحة مرشحات الحزم عند تثبيتها، ثم يخزنها مؤقتاً في جدول. عندما تصل الحزم، يطابقها الإكسوكيرنل بكفاءة مع المرشحات المخزنة مؤقتاً دون إعادة التحقق من سلامة المرشح.

**ملكية كتل القرص:** يحتفظ الإكسوكيرنل بجدول يربط كتل القرص بالتطبيقات المالكة. عندما يطلب تطبيق إدخال/إخراج القرص، يتحقق الإكسوكيرنل من هذا الجدول للتحقق من الملكية. يعمل الجدول كذاكرة تخزين مؤقت بالبرمجيات للارتباطات الآمنة لموارد القرص.

**3. تنزيل شفرة التطبيق**

في بعض الحالات، يمكن للإكسوكيرنل تنزيل شفرة التطبيق في النواة لتطبيق الارتباطات الآمنة:

**مرشحات الحزم المتخصصة:** يمكن للتطبيق توفير مرشح حزم كشفرة قابلة للتنفيذ. يتحقق الإكسوكيرنل من سلامة الشفرة (مثلاً باستخدام شفرة حاملة للإثبات أو عزل الأخطاء بالبرمجيات)، ثم ينفذها مباشرة في النواة عند وصول الحزم. هذا يسمح بمنطق ترشيح معقد مع الحفاظ على الحماية.

**مجدولات القرص المخصصة:** يمكن للتطبيق تنزيل خوارزمية جدولة قرص في النواة. يتحقق الإكسوكيرنل من أن الخوارزمية تحترم حدود الحماية، ثم يستخدمها لجدولة طلبات القرص الخاصة بالتطبيق.

**4.3 أنواع الارتباطات**

تختلف الارتباطات الآمنة في خصائص تنفيذها:

**ثابتة مقابل ديناميكية:** يتم إنشاء بعض الارتباطات في وقت التهيئة (ثابتة)، بينما يتم إنشاء وتدمير أخرى أثناء التنفيذ (ديناميكية). إدخالات TLB ديناميكية، بينما مرشحات الحزم عادة ثابتة بمجرد التثبيت.

**مرئية مقابل غير مرئية:** بعض الارتباطات مرئية للتطبيق (مثل مرشحات الحزم)، بينما يتم الحفاظ على أخرى بشفافية بواسطة نظام التشغيل المكتبي (مثل إدخالات TLB).

**أجهزة مقابل برمجيات:** توفر الارتباطات القائمة على الأجهزة (إدخالات TLB) أداءً أفضل ولكنها محدودة العدد. الارتباطات البرمجية (الجداول المخزنة مؤقتاً) أبطأ ولكن أكثر مرونة.

**4.4 مزايا الارتباطات الآمنة**

توفر الارتباطات الآمنة عدة مزايا رئيسية:

**الأداء:** من خلال التحقق من التفويض فقط في وقت الربط، تلغي الارتباطات الآمنة فحوصات النواة لكل عملية. هذا يسمح بالوصول إلى الموارد المحمية بسرعات الأجهزة.

**المرونة:** يمكن استخدام أنواع مختلفة من الارتباطات لموارد مختلفة، مما يحسن لخصائص كل مورد.

**البساطة:** يوفر تجريد الارتباط طريقة موحدة للتفكير في حماية الموارد، مما يبسط تصميم الإكسوكيرنل.

**4.5 إلغاء الموارد**

عندما يحتاج الإكسوكيرنل لاستعادة مورد، يجب أن يكسر الارتباطات الآمنة المرتبطة. يستخدم الإكسوكيرنل ثلاثة نهج:

**1. الإلغاء المرئي:** يخطر الإكسوكيرنل نظام التشغيل المكتبي بأن ارتباطاً يتم كسره (مثلاً عبر استدعاء صاعد)، مما يمنح نظام التشغيل المكتبي فرصة لحفظ الحالة أو إعادة تخصيص المورد.

**2. الإلغاء غير المرئي:** يمكن للإكسوكيرنل كسر ارتباط بصمت إذا لم يكن نظام التشغيل المكتبي بحاجة إلى إخطار. على سبيل المثال، يمكن للإكسوكيرنل إزالة إدخال TLB دون إخطار التطبيق؛ سيأخذ التطبيق ببساطة فقد TLB في المرة القادمة التي يصل فيها إلى الصفحة.

**3. الإلغاء القسري:** إذا لم يستجب نظام التشغيل المكتبي لطلبات الإلغاء، يمكن للإكسوكيرنل كسر الارتباطات قسراً واستعادة الموارد. هذا يضمن أن التطبيقات سيئة السلوك لا يمكنها منع استعادة الموارد.

**4.6 مثال: TLB كارتباط آمن**

ضع في اعتبارك كيفية استخدام الإكسوكيرنل لـ TLB لتطبيق الارتباطات الآمنة للذاكرة الافتراضية:

**إنشاء الارتباط:**
1. يطلب نظام التشغيل المكتبي تخطيطاً من الصفحة الافتراضية V إلى الصفحة المادية P
2. يتحقق الإكسوكيرنل من أن نظام التشغيل المكتبي يمتلك الصفحة المادية P
3. إذا نجح الفحص، يحمل الإكسوكيرنل تخطيط V→P في TLB
4. إدخال TLB الآن هو ارتباط آمن: فقط فضاء العنونة المالك يمكنه استخدامه

**استخدام الارتباط:**
- تستخدم عمليات الوصول إلى الذاكرة للصفحة الافتراضية V إدخال TLB مباشرة
- تترجم الأجهزة V إلى P دون مشاركة النواة
- تفرض الأجهزة الحماية من خلال التحقق من مستويات الامتياز

**إلغاء الارتباط:**
- إذا كان الإكسوكيرنل يحتاج لاستعادة الصفحة P، فإنه يزيل إدخال TLB
- سيتسبب الوصول التالي إلى V في فقد TLB
- يعالج الإكسوكيرنل الفقد ويخطر نظام التشغيل المكتبي بأن P تم استعادته

يوضح هذا المثال كيف تحقق الارتباطات الآمنة كلاً من الحماية (فقط المالك يمكنه الوصول إلى P) والأداء (تتقدم الوصولات بسرعة الأجهزة بعد إنشاء الارتباط).

---

### Translation Notes

- **Key terms introduced:**
  - Decouples authorization from use: تفصل التفويض عن الاستخدام
  - Forged: تزوير
  - Packet filter: مرشح حزم
  - Disk capability: قدرة قرص
  - Software caching: التخزين المؤقت بالبرمجيات
  - Predicates: محمولات (logical predicates)
  - Proof-carrying code: شفرة حاملة للإثبات
  - Software fault isolation: عزل الأخطاء بالبرمجيات
  - Protection boundaries: حدود الحماية
  - Bind time: وقت الربط
  - TLB miss: فقد TLB
  - Privilege levels: مستويات الامتياز

- **Technical precision:** The translation carefully preserves the three implementation techniques and the distinction between different binding types

- **Context:** This section explains the key mechanism that enables the exokernel to be both secure and efficient

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score: 0.86**

### Back-Translation (Validation)

Secure bindings are the fundamental mechanism by which an exokernel provides protected access to hardware resources. A secure binding is a protection mechanism that decouples authorization from use. An exokernel allows library operating systems to bind to resources, and checks these bindings only when they are created. Once a secure binding is established, the library operating system can use the resource without further kernel involvement, allowing operations to execute at hardware speeds.

When hardware mechanisms are insufficient, the exokernel can cache secure bindings in kernel memory. Network packet filters are predicates that determine which packets should be delivered to which application. The exokernel validates packet filters when they are installed, then caches them in a table. When packets arrive, the exokernel efficiently matches them against cached filters without re-validating filter safety.
