# Section 4: Hybrid Collectors
## القسم 4: المُجمِّعات الهجينة

**Section:** hybrid-collectors
**Translation Quality:** 0.87
**Glossary Terms Used:** hybrid, generational, deferred reference counting, heap, nursery, mature space, tracing, reference counting, write barrier, remembered set, Train algorithm, garbage collection

---

### English Version

Having established that tracing and reference counting are duals, this section demonstrates that all high-performance garbage collectors are in fact hybrids that combine both approaches in various ways.

#### 4.1 Unified Heap Hybrids

These collectors maintain a single heap but use different techniques for different types of references.

**Deferred Reference Counting**

Deferred reference counting is one of the most important hybrid techniques. It combines:
- **Reference counting** for heap-to-heap pointers (normal object references)
- **Tracing** from roots (registers, stack, global variables)

The key optimization is that reference counts are *not* updated for pointers in roots. Instead, the collector periodically traces from roots to mark referenced objects, then sweeps the heap looking for objects with zero counts that are not marked.

**Why this works:** Root pointer updates are very frequent (every function call, every local variable assignment), so tracking them would impose high overhead. By deferring these updates and handling roots through periodic tracing, the system achieves better performance.

**Algorithm:**
```
// Normal execution (mutator):
On heap pointer write (p.field = q):
    if q != null: RC(q)++
    if p.field != null: RC(p.field)--
    p.field = q

// Periodic collection:
1. Trace from roots R, marking all reachable objects
2. For each object v in heap:
    if RC(v) == 0 and not marked:
        reclaim(v)
3. Clear all marks
```

**Duality interpretation:** Deferred RC uses reference counting (anti-matter) for most of the heap but tracing (matter) for the roots. It computes a hybrid fixed point.

**Partial Tracing**

The dual of deferred reference counting is partial tracing:
- **Tracing** for heap-to-heap pointers
- **Reference counting** for root-to-heap pointers

However, this combination is problematic: it combines the *worst* properties of both approaches—high mutation overhead (tracking all root updates) and long pause times (tracing entire heap). As a result, partial tracing is rarely used in practice.

#### 4.2 Split-Heap Collectors

These collectors partition the heap into multiple regions and use different collection strategies for each region.

**Generational Collection**

Generational collectors are the most widely deployed high-performance garbage collectors. They exploit the "generational hypothesis": most objects die young.

The heap is partitioned into:
- **Nursery (Young generation):** Newly allocated objects
- **Mature space (Old generation):** Objects that have survived one or more collections

**Collection strategy:**
- **Minor collection:** Frequently trace just the nursery. This is fast because the nursery is small.
- **Major collection:** Infrequently trace the entire heap (both nursery and mature space).
- **Write barrier:** Track pointers from mature to nursery objects (called "remembered sets" or using "card marking").

**Hybrid nature:**
The key insight is that generational collectors use:
- **Tracing** within each generation
- **Reference counting** (or remembered sets, which are equivalent) for inter-generational pointers

When a pointer from mature to nursery is created, it's like incrementing a reference count. When such a pointer is deleted, it's like decrementing. The remembered set is essentially a reference counting mechanism for cross-generational references.

**Algorithm (simplified):**
```
// Minor collection:
1. Trace from roots R into nursery
2. Trace from remembered set (mature→nursery pointers)
3. For surviving objects:
    if survived N times: promote to mature space
    else: copy to new nursery
4. Reclaim entire old nursery

// Write barrier (on every pointer write):
if target is in nursery and source is in mature:
    add to remembered set
```

**The Train Algorithm**

The Train algorithm extends generational collection by further partitioning the mature space into "cars" organized into "trains". Each car is a fixed-size region.

**Goals:**
- Reduce pause times by collecting mature space incrementally
- Avoid the long pauses of full major collections

**Strategy:**
- Collect one car at a time
- Use reference counting (or remembered sets) to track inter-car pointers
- Evacuate live objects from a car before reclaiming it
- Eventually collect entire trains when all cars in a train become garbage

**Hybrid nature:** The Train algorithm is deeply hybrid:
- Tracing within each car during car collection
- Reference counting (via remembered sets) between cars
- Generational division between nursery and trains

#### 4.3 Multi-Heap Collectors

More complex systems may have many heaps (regions), each with its own collection policy. Examples include:

- **Region-based collectors:** Partition heap into many regions, collect subsets
- **Thread-local heaps:** Each thread has its own nursery
- **Type-segregated heaps:** Different object types in different regions

All of these use hybrid strategies, applying tracing within regions and reference counting (or equivalent tracking mechanisms) between regions.

#### 4.4 Design Space

The duality framework reveals that garbage collector design involves choosing points along multiple axes:

1. **Heap partitioning:** Unified vs. split (2-way, N-way)
2. **Intra-partition strategy:** Tracing vs. reference counting
3. **Inter-partition strategy:** Tracing vs. reference counting
4. **Collection timing:** Batch vs. incremental vs. concurrent

**Key insight:** Almost all practical high-performance collectors are hybrids. Pure tracing or pure reference counting is rare in production systems. The hybridization allows combining the strengths of both approaches:
- Use tracing where it's efficient (small regions, infrequent collections)
- Use reference counting where it's efficient (cross-region pointers, immediate reclamation)

---

### النسخة العربية

بعد إثبات أن التتبع وعد المراجع هما ثنائيان، يُظهِر هذا القسم أن جميع مُجمِّعات القمامة عالية الأداء هي في الواقع هجينة تجمع بين كلا النهجين بطرق مختلفة.

#### 4.1 هجين الكومة الموحدة

تحافظ هذه المُجمِّعات على كومة واحدة ولكنها تستخدم تقنيات مختلفة لأنواع مختلفة من المراجع.

**عد المراجع المؤجل**

عد المراجع المؤجل هو أحد أهم التقنيات الهجينة. يجمع بين:
- **عد المراجع** لمؤشرات الكومة إلى الكومة (مراجع الكائنات العادية)
- **التتبع** من الجذور (السجلات، المكدس، المتغيرات العامة)

التحسين الأساسي هو أن عدادات المراجع *لا* يتم تحديثها للمؤشرات في الجذور. بدلاً من ذلك، يتتبع المُجمِّع بشكل دوري من الجذور لوسم الكائنات المشار إليها، ثم يمسح الكومة بحثاً عن كائنات ذات عدادات صفرية غير موسومة.

**لماذا يعمل هذا:** تحديثات مؤشرات الجذر متكررة جداً (كل استدعاء دالة، كل تعيين متغير محلي)، لذا فإن تتبعها سيفرض عبئاً عالياً. من خلال تأجيل هذه التحديثات ومعالجة الجذور من خلال التتبع الدوري، يحقق النظام أداءً أفضل.

**الخوارزمية:**
```
// التنفيذ العادي (المحوِّر):
On heap pointer write (p.field = q):
    if q != null: RC(q)++
    if p.field != null: RC(p.field)--
    p.field = q

// الجمع الدوري:
1. التتبع من الجذور R، وسم جميع الكائنات القابلة للوصول
2. لكل كائن v في الكومة:
    if RC(v) == 0 and not marked:
        reclaim(v)
3. مسح جميع الوسوم
```

**تفسير الثنائية:** يستخدم RC المؤجل عد المراجع (المادة المضادة) لمعظم الكومة ولكن التتبع (المادة) للجذور. يحسب نقطة ثابتة هجينة.

**التتبع الجزئي**

ثنائي عد المراجع المؤجل هو التتبع الجزئي:
- **التتبع** لمؤشرات الكومة إلى الكومة
- **عد المراجع** لمؤشرات الجذر إلى الكومة

ومع ذلك، هذا التركيب إشكالي: إنه يجمع بين أسوأ خصائص كلا النهجين—عبء تحوير عالي (تتبع جميع تحديثات الجذر) وأوقات توقف طويلة (تتبع الكومة بأكملها). نتيجة لذلك، نادراً ما يُستخدَم التتبع الجزئي في الممارسة.

#### 4.2 مُجمِّعات الكومة المقسمة

تُقسِّم هذه المُجمِّعات الكومة إلى مناطق متعددة وتستخدم استراتيجيات جمع مختلفة لكل منطقة.

**الجمع الجيلي**

المُجمِّعات الجيلية هي مُجمِّعات القمامة عالية الأداء الأكثر انتشاراً. إنها تستغل "فرضية الأجيال": معظم الكائنات تموت صغيرة.

تُقسَّم الكومة إلى:
- **الحضانة (الجيل الشاب):** الكائنات المخصصة حديثاً
- **الفضاء الناضج (الجيل القديم):** الكائنات التي نجت من واحد أو أكثر من الجمعيات

**استراتيجية الجمع:**
- **الجمع الصغير:** تتبع الحضانة فقط بشكل متكرر. هذا سريع لأن الحضانة صغيرة.
- **الجمع الكبير:** تتبع الكومة بأكملها (كل من الحضانة والفضاء الناضج) بشكل غير متكرر.
- **حاجز الكتابة:** تتبع المؤشرات من الكائنات الناضجة إلى الحضانة (تُسمَّى "مجموعات متذكرة" أو باستخدام "وسم البطاقة").

**الطبيعة الهجينة:**
الاستبصار الأساسي هو أن المُجمِّعات الجيلية تستخدم:
- **التتبع** داخل كل جيل
- **عد المراجع** (أو المجموعات المتذكرة، والتي هي مكافئة) للمؤشرات بين الأجيال

عندما يُنشَأ مؤشر من الناضج إلى الحضانة، فإنه مثل زيادة عداد مراجع. عندما يُحذَف مثل هذا المؤشر، فإنه مثل التقليل. المجموعة المتذكرة هي في الأساس آلية عد مراجع للمراجع عبر الأجيال.

**الخوارزمية (مبسطة):**
```
// الجمع الصغير:
1. التتبع من الجذور R إلى الحضانة
2. التتبع من المجموعة المتذكرة (مؤشرات ناضج→حضانة)
3. للكائنات الباقية:
    if survived N times: ترقية إلى الفضاء الناضج
    else: نسخ إلى حضانة جديدة
4. استعادة الحضانة القديمة بالكامل

// حاجز الكتابة (عند كل كتابة مؤشر):
if target is in nursery and source is in mature:
    إضافة إلى المجموعة المتذكرة
```

**خوارزمية القطار**

تُمدِّد خوارزمية القطار الجمع الجيلي من خلال تقسيم الفضاء الناضج بشكل أكبر إلى "عربات" منظمة في "قطارات". كل عربة هي منطقة ذات حجم ثابت.

**الأهداف:**
- تقليل أوقات التوقف من خلال جمع الفضاء الناضج بشكل تدريجي
- تجنب التوقفات الطويلة للجمعيات الكبيرة الكاملة

**الاستراتيجية:**
- جمع عربة واحدة في كل مرة
- استخدام عد المراجع (أو المجموعات المتذكرة) لتتبع المؤشرات بين العربات
- إخلاء الكائنات الحية من عربة قبل استعادتها
- في النهاية جمع قطارات كاملة عندما تصبح جميع العربات في قطار قمامة

**الطبيعة الهجينة:** خوارزمية القطار هجينة بعمق:
- التتبع داخل كل عربة أثناء جمع العربة
- عد المراجع (عبر المجموعات المتذكرة) بين العربات
- التقسيم الجيلي بين الحضانة والقطارات

#### 4.3 مُجمِّعات متعددة الكومة

قد تحتوي الأنظمة الأكثر تعقيداً على العديد من الأكوام (المناطق)، كل منها بسياسة جمع خاصة بها. تتضمن الأمثلة:

- **مُجمِّعات قائمة على المناطق:** تقسيم الكومة إلى مناطق عديدة، جمع مجموعات فرعية
- **أكوام محلية للخيوط:** كل خيط له حضانته الخاصة
- **أكوام مفصولة حسب النوع:** أنواع كائنات مختلفة في مناطق مختلفة

كل هذه تستخدم استراتيجيات هجينة، تطبق التتبع داخل المناطق وعد المراجع (أو آليات تتبع مكافئة) بين المناطق.

#### 4.4 فضاء التصميم

يكشف إطار الثنائية أن تصميم مُجمِّع القمامة يتضمن اختيار نقاط على طول محاور متعددة:

1. **تقسيم الكومة:** موحد مقابل مقسم (ثنائي الاتجاه، N-اتجاه)
2. **استراتيجية داخل القسم:** التتبع مقابل عد المراجع
3. **استراتيجية بين الأقسام:** التتبع مقابل عد المراجع
4. **توقيت الجمع:** دفعي مقابل تدريجي مقابل متزامن

**الاستبصار الأساسي:** تقريباً جميع المُجمِّعات العملية عالية الأداء هجينة. التتبع النقي أو عد المراجع النقي نادر في أنظمة الإنتاج. يسمح الهجين بالجمع بين نقاط القوة في كلا النهجين:
- استخدام التتبع حيث يكون فعالاً (مناطق صغيرة، جمعيات نادرة)
- استخدام عد المراجع حيث يكون فعالاً (مؤشرات عبر المناطق، استعادة فورية)

---

### Translation Notes

- **Hybrid collectors:** Translated all major types (deferred RC, generational, Train algorithm)
- **Technical precision:** Maintained distinction between "minor" (صغير) and "major" (كبير) collections
- **Write barrier:** Translated as حاجز الكتابة (established term)
- **Remembered sets:** Translated as المجموعات المتذكرة
- **Pseudocode:** Kept in English with Arabic comments for clarity
- **Design space:** Preserved the multi-dimensional analysis framework

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87

**Note:** This section demonstrates how real-world high-performance garbage collectors are hybrids combining tracing and reference counting in sophisticated ways.
