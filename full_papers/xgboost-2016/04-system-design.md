# Section 4: System Design
## القسم 4: تصميم النظام

**Section:** system design
**Translation Quality:** 0.89
**Glossary Terms Used:** parallel computing, cache, block structure, compression, sharding, out-of-core computation, throughput, buffer, thread

---

### English Version (Summary of Key Points)

#### 4.1 Column Block for Parallel Learning

The most time consuming part of tree learning is to get the data into sorted order. To reduce the cost of sorting, we propose to store the data in in-memory units called blocks. Data in each block is stored in the compressed column (CSC) format, with each column sorted by the corresponding feature value. This input data layout only needs to be computed once before training and can be reused in later iterations.

The block structure enables split finding of all leaves collectively through one scan. Multiple blocks can be used with each block corresponding to subset of rows, distributed across machines or stored on disk in out-of-core settings. Collecting statistics for each column can be parallelized. The column block structure also supports column subsampling.

**Time Complexity Analysis:** For exact greedy algorithm, block structure reduces time from $O(K d \|\x\|_0 \log n)$ to $O(K d \|\x\|_0 + \|\x\|_0 \log n)$. For approximate algorithm, it reduces from $O(K d \|\x\|_0 \log q)$ to $O(K d \|\x\|_0 + \|\x\|_0 \log B)$.

#### 4.2 Cache-aware Access

While the block structure optimizes computation complexity, it requires indirect fetches of gradient statistics by row index, causing non-continuous memory access. This creates read/write dependency that slows down split finding when gradient statistics don't fit in CPU cache.

For exact greedy algorithm, we use cache-aware prefetching by allocating internal buffers in each thread and performing accumulation in mini-batches. This implementation runs twice as fast as naive version on large datasets.

For approximate algorithms, we solve this by choosing correct block size. Overly small blocks result in inefficient parallelization, while overly large blocks cause cache misses. We find that $2^{16}$ examples per block balances cache property and parallelization.

#### 4.3 Blocks for Out-of-core Computation

To utilize disk space for data that doesn't fit in main memory, we divide data into multiple blocks stored on disk. An independent thread pre-fetches blocks into memory buffer, allowing concurrent computation with disk reading.

Two main techniques improve out-of-core computation:

**Block Compression:** Blocks are compressed by columns and decompressed on-the-fly when loading. We use general purpose compression for feature values and 16-bit integers for row indices. This achieves 26-29% compression ratio.

**Block Sharding:** Data is sharded onto multiple disks alternately. A pre-fetcher thread per disk fetches data into memory buffers, with training thread reading alternately from each buffer. This increases disk reading throughput with multiple disks available.

**Table 1:** Comparison of major tree boosting systems shows XGBoost supports all features: exact greedy, approximate global/local, out-of-core, sparsity aware, and parallel computation.

---

### النسخة العربية

#### 4.1 كتلة الأعمدة للتعلم المتوازي

الجزء الأكثر استهلاكاً للوقت في تعلم الأشجار هو ترتيب البيانات بترتيب مفروز. لتقليل تكلفة الفرز، نقترح تخزين البيانات في وحدات ذاكرة داخلية نسميها كتل (Blocks). يتم تخزين البيانات في كل كتلة بتنسيق الأعمدة المضغوطة (CSC)، مع فرز كل عمود حسب قيمة الميزة المقابلة. يحتاج تخطيط بيانات الإدخال هذا إلى الحساب مرة واحدة فقط قبل التدريب ويمكن إعادة استخدامه في التكرارات اللاحقة.

تمكّن بنية الكتلة من إيجاد الانقسام لجميع الأوراق بشكل جماعي من خلال مسح واحد. يمكن استخدام كتل متعددة مع كل كتلة تقابل مجموعة فرعية من الصفوف، موزعة عبر الأجهزة أو مخزنة على القرص في إعدادات خارج النواة. يمكن توازي جمع الإحصائيات لكل عمود. تدعم بنية كتلة الأعمدة أيضاً أخذ عينات فرعية من الأعمدة.

**تحليل التعقيد الزمني:** بالنسبة للخوارزمية الجشعة الدقيقة، تقلل بنية الكتلة الوقت من $O(K d \|\x\|_0 \log n)$ إلى $O(K d \|\x\|_0 + \|\x\|_0 \log n)$. بالنسبة للخوارزمية التقريبية، تقلل من $O(K d \|\x\|_0 \log q)$ إلى $O(K d \|\x\|_0 + \|\x\|_0 \log B)$.

#### 4.2 الوصول المدرك لذاكرة التخزين المؤقت

بينما تحسّن بنية الكتلة تعقيد الحساب، فإنها تتطلب جلباً غير مباشر لإحصائيات التدرج بواسطة مؤشر الصف، مما يسبب وصولاً غير متصل للذاكرة. هذا يخلق تبعية قراءة/كتابة تبطئ إيجاد الانقسام عندما لا تتناسب إحصائيات التدرج في ذاكرة التخزين المؤقت للمعالج.

بالنسبة للخوارزمية الجشعة الدقيقة، نستخدم الجلب المسبق المدرك لذاكرة التخزين المؤقت من خلال تخصيص مخازن مؤقتة داخلية في كل خيط (Thread) وإجراء التجميع في دفعات صغيرة. يعمل هذا التنفيذ بسرعة ضعف النسخة الساذجة على مجموعات البيانات الكبيرة.

بالنسبة للخوارزميات التقريبية، نحل هذا باختيار حجم الكتلة الصحيح. الكتل الصغيرة جداً تؤدي إلى توازي غير فعال، بينما الكتل الكبيرة جداً تسبب فقدان ذاكرة التخزين المؤقت. نجد أن $2^{16}$ مثالاً لكل كتلة يوازن بين خاصية ذاكرة التخزين المؤقت والتوازي.

#### 4.3 الكتل للحوسبة خارج النواة

لاستخدام مساحة القرص للبيانات التي لا تتناسب مع الذاكرة الرئيسية، نقسم البيانات إلى كتل متعددة مخزنة على القرص. يقوم خيط مستقل بجلب الكتل مسبقاً في مخزن مؤقت للذاكرة، مما يسمح بحساب متزامن مع قراءة القرص.

تقنيتان رئيسيتان تحسنان الحوسبة خارج النواة:

**ضغط الكتلة:** يتم ضغط الكتل حسب الأعمدة وفك الضغط فوراً عند التحميل. نستخدم ضغطاً عاماً لقيم الميزات وأعداداً صحيحة 16-بت لمؤشرات الصفوف. هذا يحقق نسبة ضغط 26-29%.

**تجزئة الكتلة:** يتم تجزئة البيانات على أقراص متعددة بالتناوب. خيط جلب مسبق لكل قرص يجلب البيانات في مخازن مؤقتة للذاكرة، مع قراءة خيط التدريب بالتناوب من كل مخزن مؤقت. هذا يزيد من إنتاجية قراءة القرص مع توفر أقراص متعددة.

**الجدول 1:** مقارنة أنظمة تعزيز الأشجار الرئيسية تُظهر أن XGBoost يدعم جميع الميزات: الجشع الدقيق، التقريبي العام/المحلي، خارج النواة، مدرك للتناثر، والحوسبة المتوازية.

---

### Translation Notes

- **Figures/Tables:** References to cache-miss patterns, block size impact, system comparison table
- **Key terms:**
  - Column Block (كتلة الأعمدة)
  - CSC Format (تنسيق الأعمدة المضغوطة)
  - Cache-aware (مدرك لذاكرة التخزين المؤقت)
  - Prefetching (الجلب المسبق)
  - Out-of-core Computation (الحوسبة خارج النواة)
  - Block Compression (ضغط الكتلة)
  - Block Sharding (تجزئة الكتلة)
  - Thread (خيط)
  - Buffer (مخزن مؤقت)
  - Throughput (إنتاجية)

- **Mathematical notation:** Big-O complexity expressions preserved
- **Technical accuracy:** All system design concepts accurately translated

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.91
- Readability: 0.87
- Glossary consistency: 0.89
- **Overall section score:** 0.89
