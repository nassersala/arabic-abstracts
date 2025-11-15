# Section 5: Experimental Evaluation
## القسم 5: التقييم التجريبي

**Section:** evaluation
**Translation Quality:** 0.88
**Glossary Terms Used:** benchmark, performance, speedup, overhead, profiling, instruction cache, code cache, fragment, optimization, throughput, latency, baseline

---

### English Version

This section presents experimental results evaluating Dynamo's performance, overhead, and effectiveness on a range of benchmark programs. The experiments aim to answer several key questions:

1. What performance improvements does Dynamo achieve on real programs?
2. What is the overhead of interpretation and profiling?
3. How effective is fragment linking in creating optimization regions?
4. How does cache size affect performance?
5. What is the memory overhead of the system?

#### Experimental Setup

**Hardware Platform:** Experiments were conducted on HP 9000/785 workstations with PA-8000 processors running at 180 MHz. The machines had:
- 512 MB RAM
- 1 MB L1 instruction cache
- 1 MB L1 data cache
- 4 MB L2 unified cache

**Operating System:** HP-UX 10.20

**Benchmarks:** The evaluation used the SPEC CPU95 integer benchmarks, which represent a variety of computational workloads:
- **gcc:** GNU C compiler
- **compress:** File compression utility
- **li:** Lisp interpreter
- **ijpeg:** Image compression (JPEG)
- **perl:** Perl interpreter
- **vortex:** Object-oriented database
- **m88ksim:** Motorola 88000 simulator
- **go:** Game playing program

All benchmarks were compiled with HP's production C compiler using maximum optimization (-O2 flag). This provides a strong baseline, as the binaries are already well-optimized.

**Metrics:**
- **Speedup:** Ratio of execution time under Dynamo versus native execution
- **Fragment coverage:** Percentage of executed instructions in cached fragments
- **Cache utilization:** Fragment cache hit rate and size
- **Memory overhead:** Additional memory consumed by Dynamo

#### Overall Performance Results

The table below summarizes the performance results across all benchmarks:

| Benchmark | Native Time (s) | Dynamo Time (s) | Speedup | Fragment Coverage |
|-----------|----------------|-----------------|---------|-------------------|
| gcc       | 97.2           | 38.5            | 2.52x   | 92.1%            |
| compress  | 45.8           | 14.2            | 3.23x   | 96.4%            |
| li        | 68.4           | 23.1            | 2.96x   | 94.7%            |
| ijpeg     | 112.5          | 49.3            | 2.28x   | 89.3%            |
| perl      | 83.7           | 31.2            | 2.68x   | 93.5%            |
| vortex    | 156.3          | 52.8            | 2.96x   | 91.8%            |
| m88ksim   | 91.6           | 27.4            | 3.34x   | 95.2%            |
| go        | 124.9          | 48.7            | 2.56x   | 90.6%            |
| **Average** | **97.6**     | **35.7**        | **2.82x** | **92.9%**      |

**Key Observations:**

1. **Significant Speedups:** Dynamo achieves speedups ranging from 2.28x to 3.34x, with an average of 2.82x across all benchmarks. These results are remarkable because the baseline is already optimized code from a production compiler.

2. **High Fragment Coverage:** On average, 92.9% of executed instructions run from cached fragments, meaning only 7.1% execute in the interpreter. This demonstrates that Dynamo successfully identifies and optimizes the hot code.

3. **Consistency Across Benchmarks:** All benchmarks show substantial speedups, indicating that Dynamo's techniques are broadly applicable.

The speedups come from several sources:
- Improved instruction scheduling reducing pipeline stalls
- Better code layout improving instruction cache locality
- Elimination of cold code paths reducing I-cache pollution
- Register allocation optimizations
- Interprocedural optimization through fragment linking

#### Analysis of Optimization Impact

To understand which optimizations contribute most to performance, experiments were conducted with individual optimizations disabled:

| Optimization              | Average Speedup | Impact |
|---------------------------|-----------------|--------|
| Full Dynamo               | 2.82x          | Baseline |
| Without Instruction Scheduling | 2.15x    | -24%   |
| Without Fragment Linking  | 1.98x          | -30%   |
| Without Code Layout       | 2.34x          | -17%   |
| Without Register Alloc    | 2.51x          | -11%   |
| Interpretation Only       | 0.28x          | -90%   |

**Key Findings:**

1. **Fragment Linking Most Important:** Removing fragment linking reduces speedup by 30%, making it the single most important optimization. This validates the design decision to focus on linking traces into larger optimization regions.

2. **Instruction Scheduling Critical:** The 24% impact shows that exploiting PA-RISC's exposed pipeline through careful scheduling is highly effective.

3. **Code Layout Significant:** Improving instruction cache locality through better code layout provides a 17% benefit.

4. **Interpretation Overhead Large:** Running entirely in the interpreter (profiling but no optimization) incurs 3.6x slowdown, showing the importance of migrating hot code to the fragment cache.

#### Fragment Cache Analysis

**Cache Size Sensitivity:**

Experiments varied the fragment cache size to determine optimal configuration:

| Cache Size | Average Speedup | Fragment Coverage |
|------------|-----------------|-------------------|
| 256 KB     | 2.14x          | 78.3%            |
| 512 KB     | 2.51x          | 87.6%            |
| 1 MB       | 2.82x          | 92.9%            |
| 2 MB       | 2.86x          | 93.5%            |
| 4 MB       | 2.87x          | 93.7%            |

**Analysis:**
- Performance improves significantly from 256 KB to 1 MB
- Diminishing returns beyond 1 MB (only 2% improvement going to 4 MB)
- 1 MB cache size provides good balance of performance and memory overhead
- Larger caches have minimal benefit because hot working sets fit in 1 MB

**Cache Behavior:**

The fragment cache exhibits high temporal locality:
- Average cache hit rate: 98.7%
- Cache evictions are rare once hot working set is captured
- Flush-all cache management works well because hot code quickly repopulates

#### Profiling and Trace Formation Overhead

**Profiling Cost:** The lightweight profiling adds approximately 12% overhead when executing in the interpreter. This is much lower than traditional instrumentation-based profiling (typically 50-100% overhead).

**Trace Formation Time:** On average, trace formation and optimization takes:
- 45 microseconds per trace
- Most time spent in optimization (70%)
- Code generation and linking (30%)

**Amortization:** Each fragment executes an average of 12,500 times before eviction, thoroughly amortizing the optimization cost. The optimization overhead is less than 0.4% of total execution time.

#### Fragment Linking Effectiveness

**Linking Statistics:**

| Benchmark | Fragments | Links Created | Avg Links/Fragment | Max Chain Length |
|-----------|-----------|---------------|-------------------|------------------|
| gcc       | 2,847     | 8,932         | 3.1               | 47              |
| compress  | 412       | 1,683         | 4.1               | 63              |
| li        | 1,923     | 6,241         | 3.2               | 52              |
| ijpeg     | 3,156     | 9,874         | 3.1               | 41              |
| perl      | 2,634     | 8,127         | 3.1               | 58              |
| vortex    | 4,892     | 16,743        | 3.4               | 71              |
| m88ksim   | 1,547     | 5,936         | 3.8               | 68              |
| go        | 3,341     | 10,234        | 3.1               | 49              |

**Observations:**
- Fragments have 3-4 links on average, creating well-connected optimization regions
- Long fragment chains form (up to 71 consecutive fragments), enabling large-scale optimization
- 67% of fragment exits link to other fragments (vs. 33% returning to interpreter)

#### Memory Overhead

**Memory Consumption:**

| Component              | Average Size |
|------------------------|--------------|
| Fragment Cache         | 1.2 MB      |
| Basic Block Map        | 450 KB      |
| Profiling Counters     | 180 KB      |
| Fragment Metadata      | 320 KB      |
| **Total Dynamo Overhead** | **2.15 MB** |

Compared to typical program memory footprints (50-200 MB for these benchmarks), Dynamo adds only 1-4% memory overhead. This is acceptable given the performance benefits.

#### Comparison with Static Optimization

To verify that speedups come from runtime optimization (not just better compilation), programs were recompiled with aggressive profile-guided optimization (PGO):

| Benchmark | Native | Native+PGO | Dynamo | Dynamo vs PGO |
|-----------|--------|------------|--------|---------------|
| gcc       | 97.2   | 82.3       | 38.5   | 2.14x        |
| compress  | 45.8   | 38.6       | 14.2   | 2.72x        |
| li        | 68.4   | 59.2       | 23.1   | 2.56x        |
| Average   | 97.6   | 84.1       | 35.7   | 2.47x        |

**Key Insight:** Dynamo outperforms even profile-guided static optimization by 2.47x on average. This demonstrates that runtime optimization can exploit execution patterns that static PGO cannot capture, including:
- Cross-module optimization (PGO limited to single compilation units)
- Adaptation to actual runtime behavior (vs. training runs)
- Optimization of dynamically loaded libraries

#### Case Study: Why Dynamo Outperforms Static Compilation

Analysis of gcc benchmark reveals several sources of Dynamo's advantage:

1. **Interprocedural Traces:** Dynamo creates traces spanning multiple function calls, enabling optimization across procedure boundaries without expensive whole-program analysis.

2. **Actual Path Selection:** Static compilers predict hot paths using heuristics. Dynamo observes actual paths, eliminating mispredictions.

3. **Code Specialization:** Dynamo specializes code for actual runtime values (e.g., constant function pointers), which static compilers cannot do without aggressive speculation.

4. **I-Cache Optimization:** By packing hot code densely in the fragment cache, Dynamo achieves better instruction cache utilization than the original binary's layout.

5. **Eliminated Cold Code:** Cold paths are excluded from fragments, reducing I-cache pollution. Static binaries must include all paths.

#### Sensitivity Analysis

**Hotness Threshold:** The threshold for marking a basic block as a trace head affects performance:

| Threshold | Speedup | Fragments | Coverage |
|-----------|---------|-----------|----------|
| 10        | 2.43x   | 8,942     | 94.2%   |
| 50        | 2.82x   | 3,247     | 92.9%   |
| 100       | 2.79x   | 2,156     | 91.3%   |
| 500       | 2.51x   | 987       | 87.6%   |

**Analysis:** A threshold of 50 provides optimal balance - higher thresholds reduce fragment count but miss some hot code; lower thresholds create too many fragments with marginal benefit.

---

### النسخة العربية

يقدم هذا القسم النتائج التجريبية لتقييم أداء دينامو والتكلفة العامة والفعالية على مجموعة من برامج المعايير. تهدف التجارب إلى الإجابة على عدة أسئلة رئيسية:

1. ما هي تحسينات الأداء التي يحققها دينامو على البرامج الحقيقية؟
2. ما هي التكلفة العامة للتفسير والتصنيف؟
3. ما مدى فعالية ربط الأجزاء في إنشاء مناطق التحسين؟
4. كيف يؤثر حجم الذاكرة المؤقتة على الأداء؟
5. ما هي التكلفة العامة للذاكرة للنظام؟

#### الإعداد التجريبي

**منصة الأجهزة:** أُجريت التجارب على محطات عمل HP 9000/785 مع معالجات PA-8000 تعمل بسرعة 180 ميجاهرتز. كانت لدى الأجهزة:
- 512 ميجابايت ذاكرة وصول عشوائي
- 1 ميجابايت ذاكرة تخزين مؤقت L1 للتعليمات
- 1 ميجابايت ذاكرة تخزين مؤقت L1 للبيانات
- 4 ميجابايت ذاكرة تخزين مؤقت L2 موحدة

**نظام التشغيل:** HP-UX 10.20

**المعايير:** استخدم التقييم معايير SPEC CPU95 للأعداد الصحيحة، والتي تمثل مجموعة متنوعة من أحمال العمل الحسابية:
- **gcc:** مترجم GNU C
- **compress:** أداة ضغط الملفات
- **li:** مفسِّر Lisp
- **ijpeg:** ضغط الصور (JPEG)
- **perl:** مفسِّر Perl
- **vortex:** قاعدة بيانات موجهة نحو الكائنات
- **m88ksim:** محاكي Motorola 88000
- **go:** برنامج لعب اللعبة

تمت ترجمة جميع المعايير باستخدام مترجم C الإنتاجي من HP باستخدام أقصى تحسين (علامة -O2). هذا يوفر خط أساس قوي، حيث أن الملفات الثنائية محسَّنة بالفعل بشكل جيد.

**المقاييس:**
- **التسريع:** نسبة وقت التنفيذ تحت دينامو مقابل التنفيذ الأصلي
- **تغطية الأجزاء:** نسبة التعليمات المنفَّذة في الأجزاء المخزَّنة مؤقتاً
- **استخدام الذاكرة المؤقتة:** معدل إصابة ذاكرة التخزين المؤقت للأجزاء والحجم
- **التكلفة العامة للذاكرة:** الذاكرة الإضافية المستهلكة بواسطة دينامو

#### نتائج الأداء الإجمالي

يلخص الجدول أدناه نتائج الأداء عبر جميع المعايير:

| المعيار    | الوقت الأصلي (ثانية) | وقت دينامو (ثانية) | التسريع | تغطية الأجزاء |
|-----------|---------------------|-------------------|---------|---------------|
| gcc       | 97.2                | 38.5              | 2.52x   | 92.1%         |
| compress  | 45.8                | 14.2              | 3.23x   | 96.4%         |
| li        | 68.4                | 23.1              | 2.96x   | 94.7%         |
| ijpeg     | 112.5               | 49.3              | 2.28x   | 89.3%         |
| perl      | 83.7                | 31.2              | 2.68x   | 93.5%         |
| vortex    | 156.3               | 52.8              | 2.96x   | 91.8%         |
| m88ksim   | 91.6                | 27.4              | 3.34x   | 95.2%         |
| go        | 124.9               | 48.7              | 2.56x   | 90.6%         |
| **المتوسط** | **97.6**          | **35.7**          | **2.82x** | **92.9%**   |

**الملاحظات الرئيسية:**

1. **تسريعات كبيرة:** يحقق دينامو تسريعات تتراوح من 2.28x إلى 3.34x، بمتوسط 2.82x عبر جميع المعايير. هذه النتائج ملفتة للنظر لأن خط الأساس هو بالفعل شيفرة محسَّنة من مترجم إنتاجي.

2. **تغطية عالية للأجزاء:** في المتوسط، يتم تشغيل 92.9% من التعليمات المنفَّذة من الأجزاء المخزَّنة مؤقتاً، مما يعني أن 7.1% فقط تُنفَّذ في المفسِّر. هذا يُظهِر أن دينامو ينجح في تحديد وتحسين الشيفرة الساخنة.

3. **الاتساق عبر المعايير:** تُظهِر جميع المعايير تسريعات كبيرة، مما يشير إلى أن تقنيات دينامو قابلة للتطبيق على نطاق واسع.

تأتي التسريعات من عدة مصادر:
- تحسين جدولة التعليمات مما يقلل توقفات خط الأنابيب
- تخطيط أفضل للشيفرة يحسِّن محلية ذاكرة التخزين المؤقت للتعليمات
- إزالة مسارات الشيفرة الباردة مما يقلل تلوث ذاكرة التخزين المؤقت للتعليمات
- تحسينات تخصيص السجلات
- التحسين بين الإجراءات من خلال ربط الأجزاء

#### تحليل تأثير التحسين

لفهم أي التحسينات تساهم أكثر في الأداء، أُجريت تجارب مع تعطيل تحسينات فردية:

| التحسين                  | متوسط التسريع | التأثير |
|--------------------------|--------------|---------|
| دينامو كامل              | 2.82x        | خط الأساس |
| بدون جدولة تعليمات       | 2.15x        | -24%    |
| بدون ربط أجزاء           | 1.98x        | -30%    |
| بدون تخطيط شيفرة         | 2.34x        | -17%    |
| بدون تخصيص سجلات         | 2.51x        | -11%    |
| التفسير فقط              | 0.28x        | -90%    |

**النتائج الرئيسية:**

1. **ربط الأجزاء الأكثر أهمية:** إزالة ربط الأجزاء يقلل التسريع بنسبة 30%، مما يجعله التحسين الأكثر أهمية. هذا يتحقق من قرار التصميم للتركيز على ربط الآثار في مناطق تحسين أكبر.

2. **جدولة التعليمات حاسمة:** التأثير البالغ 24% يُظهِر أن استغلال خط أنابيب PA-RISC المكشوف من خلال الجدولة الدقيقة فعال للغاية.

3. **تخطيط الشيفرة كبير:** تحسين محلية ذاكرة التخزين المؤقت للتعليمات من خلال تخطيط أفضل للشيفرة يوفر فائدة 17%.

4. **التكلفة العامة للتفسير كبيرة:** التشغيل بالكامل في المفسِّر (التصنيف ولكن بدون تحسين) يتكبد تباطؤاً 3.6x، مما يُظهِر أهمية نقل الشيفرة الساخنة إلى ذاكرة التخزين المؤقت للأجزاء.

#### تحليل ذاكرة التخزين المؤقت للأجزاء

**حساسية حجم الذاكرة المؤقتة:**

غيرت التجارب حجم ذاكرة التخزين المؤقت للأجزاء لتحديد التكوين الأمثل:

| حجم الذاكرة المؤقتة | متوسط التسريع | تغطية الأجزاء |
|--------------------|--------------|---------------|
| 256 كيلوبايت      | 2.14x        | 78.3%         |
| 512 كيلوبايت      | 2.51x        | 87.6%         |
| 1 ميجابايت         | 2.82x        | 92.9%         |
| 2 ميجابايت         | 2.86x        | 93.5%         |
| 4 ميجابايت         | 2.87x        | 93.7%         |

**التحليل:**
- يتحسن الأداء بشكل كبير من 256 كيلوبايت إلى 1 ميجابايت
- عوائد متناقصة بعد 1 ميجابايت (تحسين 2% فقط للوصول إلى 4 ميجابايت)
- حجم ذاكرة مؤقتة 1 ميجابايت يوفر توازناً جيداً للأداء والتكلفة العامة للذاكرة
- الذواكر المؤقتة الأكبر لها فائدة ضئيلة لأن مجموعات العمل الساخنة تتناسب مع 1 ميجابايت

**سلوك الذاكرة المؤقتة:**

تُظهِر ذاكرة التخزين المؤقت للأجزاء محلية زمنية عالية:
- متوسط معدل إصابة الذاكرة المؤقتة: 98.7%
- طرد الذاكرة المؤقتة نادر بمجرد التقاط مجموعة العمل الساخنة
- إدارة الذاكرة المؤقتة بمسح الكل تعمل بشكل جيد لأن الشيفرة الساخنة تعيد الملء بسرعة

#### التكلفة العامة للتصنيف وتشكيل الآثار

**تكلفة التصنيف:** يضيف التصنيف الخفيف الوزن تكلفة عامة تقريباً 12% عند التنفيذ في المفسِّر. هذا أقل بكثير من التصنيف القائم على التجهيز التقليدي (عادةً 50-100% تكلفة عامة).

**وقت تشكيل الآثار:** في المتوسط، يستغرق تشكيل الآثار والتحسين:
- 45 ميكروثانية لكل أثر
- معظم الوقت يُنفق في التحسين (70%)
- توليد الشيفرة والربط (30%)

**التوزيع:** كل جزء يُنفَّذ بمتوسط 12,500 مرة قبل الطرد، مما يوزع تكلفة التحسين بشكل شامل. التكلفة العامة للتحسين أقل من 0.4% من إجمالي وقت التنفيذ.

#### فعالية ربط الأجزاء

**إحصائيات الربط:**

| المعيار    | الأجزاء | الروابط المُنشأة | متوسط الروابط/جزء | أقصى طول للسلسلة |
|-----------|---------|------------------|-------------------|------------------|
| gcc       | 2,847   | 8,932            | 3.1               | 47               |
| compress  | 412     | 1,683            | 4.1               | 63               |
| li        | 1,923   | 6,241            | 3.2               | 52               |
| ijpeg     | 3,156   | 9,874            | 3.1               | 41               |
| perl      | 2,634   | 8,127            | 3.1               | 58               |
| vortex    | 4,892   | 16,743           | 3.4               | 71               |
| m88ksim   | 1,547   | 5,936            | 3.8               | 68               |
| go        | 3,341   | 10,234           | 3.1               | 49               |

**الملاحظات:**
- الأجزاء لديها 3-4 روابط في المتوسط، مما ينشئ مناطق تحسين جيدة الاتصال
- تتشكل سلاسل أجزاء طويلة (حتى 71 جزءاً متتالياً)، مما يمكِّن من التحسين على نطاق واسع
- 67% من مخارج الأجزاء ترتبط بأجزاء أخرى (مقابل 33% تعود إلى المفسِّر)

#### التكلفة العامة للذاكرة

**استهلاك الذاكرة:**

| المكون                        | متوسط الحجم |
|------------------------------|-------------|
| ذاكرة التخزين المؤقت للأجزاء | 1.2 ميجابايت |
| خريطة الكتل الأساسية         | 450 كيلوبايت |
| عدادات التصنيف               | 180 كيلوبايت |
| البيانات الوصفية للأجزاء     | 320 كيلوبايت |
| **إجمالي التكلفة العامة لدينامو** | **2.15 ميجابايت** |

مقارنةً ببصمات ذاكرة البرامج النموذجية (50-200 ميجابايت لهذه المعايير)، يضيف دينامو فقط 1-4% تكلفة عامة للذاكرة. هذا مقبول نظراً لفوائد الأداء.

#### المقارنة مع التحسين الساكن

للتحقق من أن التسريعات تأتي من التحسين في وقت التشغيل (وليس فقط ترجمة أفضل)، تمت إعادة ترجمة البرامج بتحسين عدواني موجه بالملف الشخصي (PGO):

| المعيار  | أصلي | أصلي+PGO | دينامو | دينامو مقابل PGO |
|---------|------|----------|--------|------------------|
| gcc     | 97.2 | 82.3     | 38.5   | 2.14x            |
| compress | 45.8 | 38.6    | 14.2   | 2.72x            |
| li      | 68.4 | 59.2     | 23.1   | 2.56x            |
| المتوسط | 97.6 | 84.1     | 35.7   | 2.47x            |

**الفكرة الرئيسية:** يتفوق دينامو حتى على التحسين الساكن الموجه بالملف الشخصي بمعدل 2.47x في المتوسط. هذا يُظهِر أن التحسين في وقت التشغيل يمكنه استغلال أنماط التنفيذ التي لا يمكن لـ PGO الساكن التقاطها، بما في ذلك:
- تحسين عبر الوحدات (PGO محدود لوحدات ترجمة واحدة)
- التكيف مع السلوك الفعلي في وقت التشغيل (مقابل تشغيلات التدريب)
- تحسين المكتبات المحمَّلة ديناميكياً

#### دراسة حالة: لماذا يتفوق دينامو على الترجمة الساكنة

يكشف تحليل معيار gcc عن عدة مصادر لميزة دينامو:

1. **آثار بين الإجراءات:** ينشئ دينامو آثاراً تمتد عبر استدعاءات دوال متعددة، مما يمكِّن من التحسين عبر حدود الإجراءات دون تحليل مكلف للبرنامج بالكامل.

2. **اختيار المسار الفعلي:** تتنبأ المترجمات الساكنة بالمسارات الساخنة باستخدام الاستدلال. يلاحظ دينامو المسارات الفعلية، مما يزيل التنبؤات الخاطئة.

3. **تخصص الشيفرة:** يتخصص دينامو الشيفرة للقيم الفعلية في وقت التشغيل (مثلاً، مؤشرات الدوال الثابتة)، وهو ما لا يمكن للمترجمات الساكنة القيام به دون تكهن عدواني.

4. **تحسين ذاكرة التخزين المؤقت للتعليمات:** من خلال تعبئة الشيفرة الساخنة بكثافة في ذاكرة التخزين المؤقت للأجزاء، يحقق دينامو استخداماً أفضل لذاكرة التخزين المؤقت للتعليمات من تخطيط الملف الثنائي الأصلي.

5. **الشيفرة الباردة المحذوفة:** يتم استبعاد المسارات الباردة من الأجزاء، مما يقلل من تلوث ذاكرة التخزين المؤقت للتعليمات. يجب على الملفات الثنائية الساكنة تضمين جميع المسارات.

#### تحليل الحساسية

**عتبة السخونة:** تؤثر عتبة وضع علامة على كتلة أساسية كرأس أثر على الأداء:

| العتبة | التسريع | الأجزاء | التغطية |
|--------|---------|---------|----------|
| 10     | 2.43x   | 8,942   | 94.2%    |
| 50     | 2.82x   | 3,247   | 92.9%    |
| 100    | 2.79x   | 2,156   | 91.3%    |
| 500    | 2.51x   | 987     | 87.6%    |

**التحليل:** توفر عتبة 50 توازناً أمثل - العتبات الأعلى تقلل عدد الأجزاء لكنها تفوت بعض الشيفرة الساخنة؛ العتبات الأدنى تنشئ أجزاء كثيرة جداً بفائدة هامشية.

---

### Translation Notes

- **Figures referenced:** Multiple performance tables showing benchmark results, optimization impact, cache sensitivity, linking statistics, memory overhead
- **Key terms introduced:** SPEC CPU95, speedup, fragment coverage, cache hit rate, profile-guided optimization (PGO), amortization, temporal locality
- **Equations:** None
- **Citations:** SPEC CPU95 benchmarks, HP-UX operating system
- **Special handling:** Preserved all numerical data, percentages, and performance metrics exactly as reported

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
