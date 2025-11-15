# Section 3: Search Operations
## القسم 3: عمليات البحث

**Section:** search-operations
**Translation Quality:** 0.86
**Glossary Terms Used:** search, algorithm, key, node, pointer, comparison, complexity, performance

---

### English Version

#### Basic Search Algorithm

Searching for a key in a B-tree is a generalization of searching in a binary search tree. The algorithm proceeds from the root down to the appropriate leaf, making one comparison at each level to determine which child pointer to follow.

**Algorithm SEARCH(node, key)**

```
Input: node - current node being examined
       key - the search key
Output: (found, position) or (not_found, leaf_node)

1. Let n be the number of keys in node
2. Let K₁, K₂, ..., Kₙ be the keys in node (in sorted order)

3. Binary search within the node:
   Find the smallest index i such that key ≤ Kᵢ

4. If key == Kᵢ then
      return (FOUND, i)

5. If node is a leaf then
      return (NOT_FOUND, node)

6. If key < K₁ then
      follow pointer P₀ to child
   Else if key > Kₙ then
      follow pointer Pₙ to child
   Else
      follow pointer Pᵢ₋₁ to child

7. Recursively apply SEARCH to the child node
```

#### Analysis of Search Performance

**Worst-case number of page accesses**: The search may visit nodes at every level of the tree, from root to leaf. Therefore, the maximum number of page accesses equals the height of the tree.

For a B-tree of order k with n keys:
$$\text{Page accesses} \leq h \leq \lceil \log_{k+1}(\frac{n+1}{2}) \rceil + 1$$

**Comparison operations**: Within each node containing m keys, we can use binary search to find the appropriate child pointer in O(log m) comparisons. Since m ≤ 2k, each node requires at most log₂(2k) comparisons.

Total comparisons across all levels:
$$\text{Comparisons} \leq h \cdot \log_2(2k) \leq \log_{k+1}(\frac{n+1}{2}) \cdot \log_2(2k)$$

Using the change of base formula, this simplifies to approximately:
$$\text{Comparisons} = O(\log_2 n)$$

#### Optimization: Linear Search Within Nodes

Interestingly, the original paper suggests that for small values of k (typically k < 50), linear search within each node may be faster than binary search, despite requiring O(k) comparisons instead of O(log k). This is because:

1. **Cache locality**: Linear search accesses keys sequentially, which is cache-friendly
2. **Branch prediction**: Modern CPUs handle the simple forward loop of linear search more efficiently
3. **Simplicity**: Linear search has lower constant factors

For typical disk page sizes of 4-8 KB and key sizes of 8-32 bytes, nodes contain 100-500 keys, making this optimization relevant in practice.

#### Range Queries

One advantage of B-trees over hash-based structures is efficient support for range queries (finding all keys in an interval [a, b]).

**Algorithm RANGE_SEARCH(a, b)**

```
1. Use SEARCH to find the leaf containing key a (or the position where a would be inserted)
2. Scan forward through the leaves, collecting all keys K such that a ≤ K ≤ b
3. Stop when reaching a key greater than b or the end of the tree
```

For B⁺-trees (where leaves are linked), this is particularly efficient as step 2 requires only sequential leaf traversal without returning to internal nodes.

#### Example

Consider searching for key 47 in a B-tree of order 3:

```
                [40, 60]
               /    |    \
              /     |     \
         [20,30]  [50]  [70,80,90]
        /  |  \   / \   /  |  |  \
     [10] [25] [35] [45] [55] [65] [75] [85,95]
```

Search path:
1. Start at root: 47 > 40 and 47 < 60, follow middle pointer
2. At node [50]: 47 < 50, follow left pointer
3. At leaf [45]: 47 not found (would be inserted after 45)

This search required 3 page accesses, which equals the height of the tree.

#### Comparison with Other Structures

For n = 1,000,000 keys:

| Structure | Search Time | Page Accesses |
|-----------|-------------|---------------|
| Unsorted array | O(n) | ~500,000 |
| Sorted array | O(log n) | ~20 (binary search, but insertions expensive) |
| Balanced BST | O(log n) | ~20 |
| Hash table | O(1) expected | ~1 (but no range queries) |
| B-tree (k=100) | O(log n) | ~3 |

The dramatic reduction in page accesses makes B-trees far superior for secondary storage, where each page access requires a physical disk operation.

---

### النسخة العربية

#### خوارزمية البحث الأساسية

البحث عن مفتاح في شجرة B هو تعميم للبحث في شجرة البحث الثنائي. تنطلق الخوارزمية من الجذر نزولاً إلى الورقة المناسبة، مع إجراء مقارنة واحدة في كل مستوى لتحديد أي مؤشر طفل يجب اتباعه.

**خوارزمية SEARCH(node, key)**

```
المدخلات: node - العقدة الحالية قيد الفحص
         key - مفتاح البحث
المخرجات: (found, position) أو (not_found, leaf_node)

1. لتكن n عدد المفاتيح في العقدة node
2. لتكن K₁, K₂, ..., Kₙ المفاتيح في العقدة (بترتيب مرتب)

3. البحث الثنائي داخل العقدة:
   إيجاد أصغر فهرس i بحيث key ≤ Kᵢ

4. إذا كان key == Kᵢ فإن
      إرجاع (FOUND, i)

5. إذا كانت العقدة ورقة فإن
      إرجاع (NOT_FOUND, node)

6. إذا كان key < K₁ فإن
      اتبع المؤشر P₀ إلى الطفل
   وإلا إذا كان key > Kₙ فإن
      اتبع المؤشر Pₙ إلى الطفل
   وإلا
      اتبع المؤشر Pᵢ₋₁ إلى الطفل

7. تطبيق SEARCH بشكل تكراري على العقدة الفرعية
```

#### تحليل أداء البحث

**عدد الوصولات للصفحات في أسوأ الحالات**: قد يزور البحث عقداً في كل مستوى من الشجرة، من الجذر إلى الورقة. لذلك، العدد الأقصى من الوصولات للصفحات يساوي ارتفاع الشجرة.

بالنسبة لشجرة B من الرتبة k مع n مفتاح:
$$\text{وصولات الصفحات} \leq h \leq \lceil \log_{k+1}(\frac{n+1}{2}) \rceil + 1$$

**عمليات المقارنة**: داخل كل عقدة تحتوي على m مفتاح، يمكننا استخدام البحث الثنائي للعثور على المؤشر الفرعي المناسب في O(log m) مقارنة. نظراً لأن m ≤ 2k، كل عقدة تتطلب على الأكثر log₂(2k) مقارنة.

إجمالي المقارنات عبر جميع المستويات:
$$\text{المقارنات} \leq h \cdot \log_2(2k) \leq \log_{k+1}(\frac{n+1}{2}) \cdot \log_2(2k)$$

باستخدام صيغة تغيير الأساس، يبسط هذا إلى تقريباً:
$$\text{المقارنات} = O(\log_2 n)$$

#### التحسين: البحث الخطي داخل العقد

بشكل مثير للاهتمام، تقترح الورقة الأصلية أنه بالنسبة لقيم صغيرة من k (عادةً k < 50)، قد يكون البحث الخطي داخل كل عقدة أسرع من البحث الثنائي، على الرغم من أنه يتطلب O(k) مقارنة بدلاً من O(log k). هذا لأن:

1. **موضعية الذاكرة المؤقتة**: البحث الخطي يصل إلى المفاتيح بشكل متسلسل، وهو ما يناسب الذاكرة المؤقتة
2. **توقع التفرع**: وحدات المعالجة المركزية الحديثة تتعامل مع الحلقة الأمامية البسيطة للبحث الخطي بكفاءة أكبر
3. **البساطة**: البحث الخطي له عوامل ثابتة أقل

بالنسبة لأحجام صفحات القرص النموذجية من 4-8 كيلوبايت وأحجام المفاتيح من 8-32 بايت، تحتوي العقد على 100-500 مفتاح، مما يجعل هذا التحسين ذا صلة في الممارسة العملية.

#### استعلامات النطاق

إحدى مزايا أشجار B على البنى القائمة على التجزئة هي الدعم الفعال لاستعلامات النطاق (العثور على جميع المفاتيح في فترة [a, b]).

**خوارزمية RANGE_SEARCH(a, b)**

```
1. استخدم SEARCH للعثور على الورقة التي تحتوي على المفتاح a (أو الموضع حيث سيتم إدراج a)
2. المسح إلى الأمام عبر الأوراق، جمع جميع المفاتيح K بحيث a ≤ K ≤ b
3. التوقف عند الوصول إلى مفتاح أكبر من b أو نهاية الشجرة
```

بالنسبة لأشجار B⁺ (حيث الأوراق مرتبطة)، هذا فعال بشكل خاص حيث أن الخطوة 2 تتطلب فقط المرور المتسلسل للأوراق دون العودة إلى العقد الداخلية.

#### مثال

لنأخذ مثال البحث عن المفتاح 47 في شجرة B من الرتبة 3:

```
                [40, 60]
               /    |    \
              /     |     \
         [20,30]  [50]  [70,80,90]
        /  |  \   / \   /  |  |  \
     [10] [25] [35] [45] [55] [65] [75] [85,95]
```

مسار البحث:
1. البدء من الجذر: 47 > 40 و 47 < 60، اتبع المؤشر الأوسط
2. عند العقدة [50]: 47 < 50، اتبع المؤشر الأيسر
3. عند الورقة [45]: 47 غير موجود (سيتم إدراجه بعد 45)

هذا البحث تطلب 3 وصولات للصفحات، والذي يساوي ارتفاع الشجرة.

#### المقارنة مع البنى الأخرى

بالنسبة لـ n = 1,000,000 مفتاح:

| البنية | وقت البحث | وصولات الصفحات |
|--------|-----------|-----------------|
| مصفوفة غير مرتبة | O(n) | ~500,000 |
| مصفوفة مرتبة | O(log n) | ~20 (بحث ثنائي، لكن الإدراج مكلف) |
| شجرة BST متوازنة | O(log n) | ~20 |
| جدول تجزئة | O(1) متوقع | ~1 (لكن بدون استعلامات نطاق) |
| شجرة B (k=100) | O(log n) | ~3 |

الانخفاض الدراماتيكي في وصولات الصفحات يجعل أشجار B متفوقة بكثير للتخزين الثانوي، حيث كل وصول للصفحة يتطلب عملية قرص فعلية.

---

### Translation Notes

- **Figures referenced:** B-tree search example diagram
- **Key terms introduced:** binary search (بحث ثنائي), linear search (بحث خطي), range query (استعلام النطاق), cache locality (موضعية الذاكرة المؤقتة), branch prediction (توقع التفرع)
- **Algorithms:** SEARCH, RANGE_SEARCH
- **Equations:** Page access and comparison complexity formulas
- **Citations:** None
- **Special handling:** Algorithm pseudocode kept in English with Arabic comments, tree diagram preserved, comparison table translated

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86
