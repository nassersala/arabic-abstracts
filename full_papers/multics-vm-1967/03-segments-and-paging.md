# Section 3: Segmentation and Paging
## القسم 3: التجزئة والترحيل

**Section:** segments-and-paging
**Translation Quality:** 0.86
**Glossary Terms Used:** segment, paging, page, page table, page frame, physical memory, secondary storage, demand paging, page fault, locality

---

### English Version

MULTICS combines segmentation and paging to achieve both logical modularity and efficient memory management. While segments provide the logical structure visible to programs, paging provides the physical memory management mechanism.

#### Paging Within Segments

Each segment is divided into fixed-size pages, typically 1024 words (4096 bytes) in length. This page size was chosen to balance several competing concerns:

1. **Internal Fragmentation**: Smaller pages reduce wasted space within partially filled pages
2. **Page Table Size**: Larger pages reduce the number of entries needed in page tables
3. **Transfer Efficiency**: Larger pages amortize the overhead of disk I/O operations
4. **Working Set Granularity**: Page size affects the granularity at which the working set can be measured

When a segment is created, the system does not immediately allocate physical memory for the entire segment. Instead, pages are allocated on demand as they are referenced. This demand-paging approach provides several advantages:

1. **Reduced Memory Consumption**: Only pages that are actually used consume physical memory
2. **Faster Process Creation**: New processes can begin execution immediately without waiting for all segments to be loaded
3. **Efficient Memory Utilization**: Physical memory is devoted to active pages across all processes

#### Page Tables

Each segment has an associated page table that maps virtual page numbers within the segment to physical page frame numbers. The page table is itself stored as a segment, allowing it to be paged like any other data structure.

A page table entry contains:

1. **Page Frame Number**: The physical memory frame containing the page (if present)
2. **Presence Bit**: Indicates whether the page is currently in physical memory
3. **Modified Bit**: Set when the page is written, indicating it must be written back to disk if evicted
4. **Access Control**: Some implementations include per-page access controls

The address translation process for a virtual address (s, w) proceeds as follows:

1. Extract the segment number `s` and word offset `w` from the virtual address
2. Use `s` to index the descriptor segment and retrieve the segment descriptor
3. Divide `w` by the page size to obtain the page number `p` and offset within page `o`
4. Access the page table for segment `s` and retrieve the entry for page `p`
5. If the page is present, combine the page frame number from the page table with offset `o` to form the physical address
6. If the page is not present, generate a page fault

#### Page Replacement

When physical memory is full and a new page must be brought in, the system must select a page to evict. MULTICS uses a global page replacement policy based on usage information:

1. **Reference Bits**: The hardware sets a reference bit in the page table entry each time a page is accessed
2. **Clock Algorithm**: The system periodically scans page table entries, using the reference bits to identify less recently used pages
3. **Modified Pages**: Modified pages must be written to secondary storage before the physical frame can be reused

The page replacement algorithm treats all pages equally, regardless of which segment they belong to. This global approach allows the system to allocate memory dynamically among processes and segments based on actual usage patterns.

#### Segment Length and Growth

Segments have a current length that may be less than the maximum possible length. The segment length is stored in the segment descriptor. When a program attempts to reference a word beyond the current segment length:

1. If the reference is beyond the maximum allowed segment size, a bounds fault occurs
2. If the reference is within the allowed range but beyond the current length, the segment is automatically extended

Automatic segment extension simplifies programming by allowing data structures to grow dynamically. The programmer need not predict maximum sizes or manage explicit allocation calls.

#### Integration of Segmentation and Paging

The combination of segmentation and paging provides complementary benefits:

**Segmentation provides:**
- Logical modularity matching program structure
- Variable-size units for sharing and protection
- Symbolic naming through the directory hierarchy
- Support for dynamic linking

**Paging provides:**
- Fixed-size units simplifying memory allocation
- Elimination of external fragmentation
- Efficient utilization of physical memory through demand paging
- Simple mechanism for memory-to-disk mapping

This two-level organization was novel for its time. Earlier systems typically used either segmentation or paging, but not both. The MULTICS approach demonstrated that the benefits of both techniques could be achieved simultaneously, though at the cost of additional address translation complexity.

The hardware support in the GE-645, particularly the associative memory for caching segment descriptors and page table entries, was essential for making this two-level address translation acceptably fast. Without this hardware support, the overhead of translating every memory reference through both segment and page tables would have been prohibitive.

---

### النسخة العربية

يجمع مَلتِكس بين التجزئة والترحيل لتحقيق النمطية المنطقية وإدارة الذاكرة الفعالة. بينما توفر المقاطع البنية المنطقية المرئية للبرامج، يوفر الترحيل آلية إدارة الذاكرة الفيزيائية.

#### الترحيل داخل المقاطع

يتم تقسيم كل مقطع إلى صفحات ذات حجم ثابت، عادةً 1024 كلمة (4096 بايت) في الطول. تم اختيار حجم الصفحة هذا لموازنة عدة اعتبارات متنافسة:

1. **التجزئة الداخلية**: تقلل الصفحات الأصغر من المساحة المهدرة داخل الصفحات المملوءة جزئياً
2. **حجم جدول الصفحات**: تقلل الصفحات الأكبر من عدد الإدخالات المطلوبة في جداول الصفحات
3. **كفاءة النقل**: تعمل الصفحات الأكبر على إطفاء التكلفة الزائدة لعمليات إدخال/إخراج القرص
4. **دقة مجموعة العمل**: يؤثر حجم الصفحة على الدقة التي يمكن بها قياس مجموعة العمل

عندما يتم إنشاء مقطع، لا يخصص النظام فوراً ذاكرة فيزيائية للمقطع بأكمله. بدلاً من ذلك، يتم تخصيص الصفحات عند الطلب عند الإشارة إليها. يوفر نهج الترحيل عند الطلب هذا عدة مزايا:

1. **استهلاك ذاكرة مخفض**: فقط الصفحات المستخدمة فعلياً تستهلك الذاكرة الفيزيائية
2. **إنشاء عملية أسرع**: يمكن للعمليات الجديدة بدء التنفيذ فوراً دون انتظار تحميل جميع المقاطع
3. **استخدام فعال للذاكرة**: تُخصص الذاكرة الفيزيائية للصفحات النشطة عبر جميع العمليات

#### جداول الصفحات

لكل مقطع جدول صفحات مرتبط يربط أرقام الصفحات الافتراضية داخل المقطع بأرقام إطارات الصفحات الفيزيائية. يتم تخزين جدول الصفحات نفسه كمقطع، مما يسمح بترحيله مثل أي بنية بيانات أخرى.

يحتوي إدخال جدول الصفحات على:

1. **رقم إطار الصفحة**: الإطار الفيزيائي للذاكرة الذي يحتوي على الصفحة (إذا كانت موجودة)
2. **بت الحضور**: يشير إلى ما إذا كانت الصفحة موجودة حالياً في الذاكرة الفيزيائية
3. **بت التعديل**: يتم تعيينه عند كتابة الصفحة، مما يشير إلى أنه يجب كتابتها مرة أخرى إلى القرص إذا تم طردها
4. **التحكم في الوصول**: تتضمن بعض التطبيقات عناصر تحكم وصول لكل صفحة

تستمر عملية ترجمة العنوان للعنوان الافتراضي (s, w) على النحو التالي:

1. استخراج رقم المقطع `s` وإزاحة الكلمة `w` من العنوان الافتراضي
2. استخدام `s` لفهرسة مقطع الواصفات واسترجاع واصف المقطع
3. قسمة `w` على حجم الصفحة للحصول على رقم الصفحة `p` والإزاحة داخل الصفحة `o`
4. الوصول إلى جدول الصفحات للمقطع `s` واسترجاع الإدخال للصفحة `p`
5. إذا كانت الصفحة موجودة، يتم دمج رقم إطار الصفحة من جدول الصفحات مع الإزاحة `o` لتكوين العنوان الفيزيائي
6. إذا لم تكن الصفحة موجودة، يتم توليد خطأ صفحة

#### استبدال الصفحات

عندما تكون الذاكرة الفيزيائية ممتلئة ويجب إحضار صفحة جديدة، يجب على النظام اختيار صفحة لطردها. يستخدم مَلتِكس سياسة استبدال صفحات عامة بناءً على معلومات الاستخدام:

1. **بتات المرجعية**: تقوم الأجهزة بتعيين بت مرجعية في إدخال جدول الصفحات في كل مرة يتم الوصول إلى صفحة
2. **خوارزمية الساعة**: يفحص النظام بشكل دوري إدخالات جدول الصفحات، باستخدام بتات المرجعية لتحديد الصفحات الأقل استخداماً مؤخراً
3. **الصفحات المعدلة**: يجب كتابة الصفحات المعدلة إلى التخزين الثانوي قبل إعادة استخدام الإطار الفيزيائي

تعامل خوارزمية استبدال الصفحات جميع الصفحات بالتساوي، بغض النظر عن المقطع الذي تنتمي إليه. يسمح هذا النهج العام للنظام بتخصيص الذاكرة ديناميكياً بين العمليات والمقاطع بناءً على أنماط الاستخدام الفعلية.

#### طول المقطع والنمو

للمقاطع طول حالي قد يكون أقل من الطول الأقصى الممكن. يتم تخزين طول المقطع في واصف المقطع. عندما يحاول البرنامج الإشارة إلى كلمة تتجاوز طول المقطع الحالي:

1. إذا كانت المرجعية تتجاوز الحجم الأقصى المسموح به للمقطع، يحدث خطأ حدود
2. إذا كانت المرجعية ضمن النطاق المسموح به ولكن تتجاوز الطول الحالي، يتم تمديد المقطع تلقائياً

يبسِّط التمديد التلقائي للمقطع البرمجة من خلال السماح لبنى البيانات بالنمو ديناميكياً. لا يحتاج المبرمج إلى التنبؤ بالأحجام القصوى أو إدارة استدعاءات التخصيص الصريحة.

#### تكامل التجزئة والترحيل

يوفر الجمع بين التجزئة والترحيل فوائد تكميلية:

**توفر التجزئة:**
- النمطية المنطقية المطابقة لبنية البرنامج
- وحدات متغيرة الحجم للمشاركة والحماية
- التسمية الرمزية من خلال التسلسل الهرمي للدليل
- دعم الربط الديناميكي

**يوفر الترحيل:**
- وحدات ذات حجم ثابت تبسط تخصيص الذاكرة
- القضاء على التجزئة الخارجية
- استخدام فعال للذاكرة الفيزيائية من خلال الترحيل عند الطلب
- آلية بسيطة لربط الذاكرة بالقرص

كان هذا التنظيم ثنائي المستوى جديداً في وقته. كانت الأنظمة السابقة عادةً تستخدم إما التجزئة أو الترحيل، ولكن ليس كليهما. أظهر نهج مَلتِكس أن فوائد كلا التقنيتين يمكن تحقيقها في وقت واحد، وإن كان ذلك على حساب تعقيد ترجمة العناوين الإضافي.

كان دعم الأجهزة في GE-645، وخاصة الذاكرة الترابطية لتخزين واصفات المقاطع وإدخالات جدول الصفحات مؤقتاً، ضرورياً لجعل ترجمة العناوين ثنائية المستوى هذه سريعة بشكل مقبول. بدون دعم الأجهزة هذا، كانت التكلفة الزائدة لترجمة كل مرجعية ذاكرة من خلال جداول المقاطع والصفحات ستكون باهظة.

---

### Translation Notes

- **Figures referenced:** None explicitly
- **Key terms introduced:** demand paging (الترحيل عند الطلب), page fault (خطأ صفحة), page frame (إطار الصفحة), page table (جدول الصفحات), internal fragmentation (التجزئة الداخلية), external fragmentation (التجزئة الخارجية), working set (مجموعة العمل), clock algorithm (خوارزمية الساعة), bounds fault (خطأ حدود)
- **Equations:** Page size (1024 words = 4096 bytes), address decomposition formulas
- **Citations:** Reference to GE-645 hardware
- **Special handling:** Maintained the two-level address translation algorithm steps

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
