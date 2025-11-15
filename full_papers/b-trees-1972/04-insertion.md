# Section 4: Insertion Algorithm
## القسم 4: خوارزمية الإدراج

**Section:** insertion
**Translation Quality:** 0.89
**Glossary Terms Used:** insertion, algorithm, node splitting, overflow, key, pointer, balanced tree, page

---

### English Version

#### Overview

Insertion in a B-tree is more complex than in a binary search tree because we must maintain two critical properties:
1. All leaves must remain at the same level (balanced property)
2. Each node must contain between k and 2k keys (except the root)

The key insight is that when a node becomes full (contains 2k keys), we split it into two nodes, each containing k keys, and promote the median key to the parent. This process may cascade upward, potentially increasing the tree's height by splitting the root.

#### Basic Insertion Algorithm

**Algorithm INSERT(key)**

```
1. Search for the appropriate leaf node L where key should be inserted

2. If L has fewer than 2k keys:
   - Insert key into L in sorted order
   - DONE

3. If L is full (has 2k keys):
   - Split L into L and L':
     * L contains the first k keys
     * L' contains the last k keys
     * Let K_median be the (k+1)-th key
   - Insert K_median and pointer to L' into parent of L
   - If parent is full, recursively split the parent
   - If splitting reaches the root:
     * Create new root containing K_median
     * Old root becomes left child
     * New node becomes right child
     * Tree height increases by 1
```

#### Detailed Splitting Procedure

When a node N containing keys K₁, K₂, ..., K₂ₖ, K₂ₖ₊₁ needs to split:

**Before split:**
```
N: [K₁ K₂ ... Kₖ Kₖ₊₁ Kₖ₊₂ ... K₂ₖ K₂ₖ₊₁]
   [P₀ P₁ ... Pₖ Pₖ₊₁ Pₖ₊₂ ... P₂ₖ P₂ₖ₊₁]
```

**After split:**
```
N:  [K₁ K₂ ... Kₖ]
    [P₀ P₁ ... Pₖ]

N': [Kₖ₊₂ Kₖ₊₃ ... K₂ₖ K₂ₖ₊₁]
    [Pₖ₊₁ Pₖ₊₂ ... P₂ₖ P₂ₖ₊₁]

Promoted to parent: Kₖ₊₁ (with pointer to N')
```

The median key Kₖ₊₁ is promoted to the parent, leaving exactly k keys in each resulting node. This ensures both nodes satisfy the minimum occupancy requirement.

#### Example: Inserting into a B-tree of Order 2

Initial tree (k=2, each node can have 2-4 keys):

```
       [30]
      /    \
  [10,20]  [40,50]
```

**Insert 25:**
1. Search finds leaf [10,20]
2. Node has room, insert 25: [10,20,25]

```
       [30]
      /    \
  [10,20,25]  [40,50]
```

**Insert 35:**
1. Search finds leaf [40,50]
2. Node has room, insert 35: [35,40,50]

```
       [30]
      /    \
  [10,20,25]  [35,40,50]
```

**Insert 45:**
1. Search finds leaf [35,40,50]
2. Temporarily: [35,40,45,50] (node now has 4 keys)
3. Node is full, split required
4. Split into [35,40] and [45,50], promote 45 to parent
5. Parent becomes [30,45]

```
         [30,45]
       /    |    \
  [10,20,25] [35,40] [45,50]
```

**Insert 15:**
1. Search finds leaf [10,20,25]
2. Temporarily: [10,15,20,25] (node now has 4 keys)
3. Split into [10,15] and [20,25], promote 20 to parent
4. Parent becomes [20,30,45]

```
          [20,30,45]
        /    |   |   \
   [10,15] [20,25] [35,40] [45,50]
```

**Insert 60:**
1. Search finds leaf [45,50]
2. Temporarily: [45,50,60]

```
          [20,30,45]
        /    |   |   \
   [10,15] [20,25] [35,40] [45,50,60]
```

**Insert 65, 70, 75 (forcing root split):**

After inserting 65,70,75, the rightmost leaf [45,50,60,65,70,75] must split:
- Split into [45,50,60] and [70,75], promote 65

Parent [20,30,45,65] is now full (4 keys), must split:
- Split into [20,30] and [65], promote 45
- Create new root [45]

```
             [45]
           /      \
       [20,30]    [65]
      /   |   \   /   \
  [10,15] [20,25] [35,40] [45,50,60] [70,75]
```

#### Properties of Insertion

**Theorem**: Insertion of a single key requires at most h page accesses for search plus h page writes for splitting, where h is the tree height.

**Proof**:
- Search phase requires at most h page reads (one per level)
- In worst case, splitting propagates to root, requiring one page write per level
- Total: 2h page accesses

**Storage guarantees**: After an insertion:
- All nodes (except root) contain at least k keys
- All nodes contain at most 2k keys
- Tree remains balanced (all leaves at same level)

**Amortized analysis**: While a single insertion may trigger O(h) splits in the worst case, the amortized number of splits per insertion is constant. This is because:
- Each split creates a node with k keys (maximum slack)
- Must insert k more keys before that node can split again
- On average, insertions cause O(1) splits

#### Implementation Optimizations

**1. Top-down splitting**: Instead of splitting on the way up, split full nodes proactively on the way down during search. This simplifies implementation by avoiding recursion.

**2. Deferred splitting**: Allow temporary overflow (2k+1 keys) and redistribute keys among siblings before splitting. This improves storage utilization to 67% or higher.

**3. Bulk loading**: When building a B-tree from sorted data, pack nodes to maximum capacity bottom-up for optimal space utilization.

---

### النسخة العربية

#### نظرة عامة

الإدراج في شجرة B أكثر تعقيداً من الإدراج في شجرة البحث الثنائي لأننا يجب أن نحافظ على خاصيتين حاسمتين:
1. يجب أن تبقى جميع الأوراق في نفس المستوى (خاصية التوازن)
2. يجب أن تحتوي كل عقدة على ما بين k و 2k مفتاح (باستثناء الجذر)

الفكرة الرئيسية هي أنه عندما تصبح العقدة ممتلئة (تحتوي على 2k مفتاح)، نقسمها إلى عقدتين، كل منهما تحتوي على k مفتاح، ونرقي المفتاح الوسيط إلى العقدة الأب. قد تتسلسل هذه العملية صعوداً، مما قد يزيد من ارتفاع الشجرة عن طريق تقسيم الجذر.

#### خوارزمية الإدراج الأساسية

**خوارزمية INSERT(key)**

```
1. البحث عن عقدة الورقة المناسبة L حيث يجب إدراج المفتاح key

2. إذا كانت L تحتوي على أقل من 2k مفتاح:
   - إدراج المفتاح key في L بترتيب مرتب
   - انتهى

3. إذا كانت L ممتلئة (لديها 2k مفتاح):
   - تقسيم L إلى L و L':
     * L تحتوي على أول k مفتاح
     * L' تحتوي على آخر k مفتاح
     * لتكن K_median المفتاح الـ (k+1)
   - إدراج K_median ومؤشر إلى L' في أب L
   - إذا كان الأب ممتلئاً، تقسيم الأب بشكل تكراري
   - إذا وصل التقسيم إلى الجذر:
     * إنشاء جذر جديد يحتوي على K_median
     * الجذر القديم يصبح الطفل الأيسر
     * العقدة الجديدة تصبح الطفل الأيمن
     * يزداد ارتفاع الشجرة بمقدار 1
```

#### إجراء التقسيم التفصيلي

عندما تحتاج عقدة N تحتوي على المفاتيح K₁, K₂, ..., K₂ₖ, K₂ₖ₊₁ إلى التقسيم:

**قبل التقسيم:**
```
N: [K₁ K₂ ... Kₖ Kₖ₊₁ Kₖ₊₂ ... K₂ₖ K₂ₖ₊₁]
   [P₀ P₁ ... Pₖ Pₖ₊₁ Pₖ₊₂ ... P₂ₖ P₂ₖ₊₁]
```

**بعد التقسيم:**
```
N:  [K₁ K₂ ... Kₖ]
    [P₀ P₁ ... Pₖ]

N': [Kₖ₊₂ Kₖ₊₃ ... K₂ₖ K₂ₖ₊₁]
    [Pₖ₊₁ Pₖ₊₂ ... P₂ₖ P₂ₖ₊₁]

الترقية إلى الأب: Kₖ₊₁ (مع مؤشر إلى N')
```

يتم ترقية المفتاح الوسيط Kₖ₊₁ إلى الأب، مما يترك بالضبط k مفتاح في كل عقدة ناتجة. هذا يضمن أن كلتا العقدتين تحققان متطلب الإشغال الأدنى.

#### مثال: الإدراج في شجرة B من الرتبة 2

الشجرة الأولية (k=2، كل عقدة يمكن أن يكون لها 2-4 مفاتيح):

```
       [30]
      /    \
  [10,20]  [40,50]
```

**إدراج 25:**
1. البحث يجد الورقة [10,20]
2. العقدة لديها مساحة، إدراج 25: [10,20,25]

```
       [30]
      /    \
  [10,20,25]  [40,50]
```

**إدراج 35:**
1. البحث يجد الورقة [40,50]
2. العقدة لديها مساحة، إدراج 35: [35,40,50]

```
       [30]
      /    \
  [10,20,25]  [35,40,50]
```

**إدراج 45:**
1. البحث يجد الورقة [35,40,50]
2. مؤقتاً: [35,40,45,50] (العقدة الآن لديها 4 مفاتيح)
3. العقدة ممتلئة، يلزم التقسيم
4. التقسيم إلى [35,40] و [45,50]، ترقية 45 إلى الأب
5. الأب يصبح [30,45]

```
         [30,45]
       /    |    \
  [10,20,25] [35,40] [45,50]
```

**إدراج 15:**
1. البحث يجد الورقة [10,20,25]
2. مؤقتاً: [10,15,20,25] (العقدة الآن لديها 4 مفاتيح)
3. التقسيم إلى [10,15] و [20,25]، ترقية 20 إلى الأب
4. الأب يصبح [20,30,45]

```
          [20,30,45]
        /    |   |   \
   [10,15] [20,25] [35,40] [45,50]
```

**إدراج 60:**
1. البحث يجد الورقة [45,50]
2. مؤقتاً: [45,50,60]

```
          [20,30,45]
        /    |   |   \
   [10,15] [20,25] [35,40] [45,50,60]
```

**إدراج 65، 70، 75 (إجبار تقسيم الجذر):**

بعد إدراج 65،70،75، الورقة اليمنى القصوى [45,50,60,65,70,75] يجب أن تنقسم:
- التقسيم إلى [45,50,60] و [70,75]، ترقية 65

الأب [20,30,45,65] الآن ممتلئ (4 مفاتيح)، يجب التقسيم:
- التقسيم إلى [20,30] و [65]، ترقية 45
- إنشاء جذر جديد [45]

```
             [45]
           /      \
       [20,30]    [65]
      /   |   \   /   \
  [10,15] [20,25] [35,40] [45,50,60] [70,75]
```

#### خصائص الإدراج

**نظرية**: إدراج مفتاح واحد يتطلب على الأكثر h وصولاً للصفحات للبحث بالإضافة إلى h كتابة للصفحات للتقسيم، حيث h هو ارتفاع الشجرة.

**البرهان**:
- مرحلة البحث تتطلب على الأكثر h قراءة للصفحات (واحدة لكل مستوى)
- في أسوأ الحالات، ينتشر التقسيم إلى الجذر، مما يتطلب كتابة صفحة واحدة لكل مستوى
- الإجمالي: 2h وصولاً للصفحات

**ضمانات التخزين**: بعد الإدراج:
- جميع العقد (باستثناء الجذر) تحتوي على k مفتاح على الأقل
- جميع العقد تحتوي على 2k مفتاح على الأكثر
- الشجرة تبقى متوازنة (جميع الأوراق في نفس المستوى)

**التحليل المطفأ**: بينما قد يؤدي إدراج واحد إلى O(h) تقسيمات في أسوأ الحالات، فإن عدد التقسيمات المطفأة لكل إدراج هو ثابت. هذا لأن:
- كل تقسيم ينشئ عقدة بها k مفتاح (أقصى تراخي)
- يجب إدراج k مفتاح إضافي قبل أن تتمكن تلك العقدة من الانقسام مرة أخرى
- في المتوسط، تسبب الإدراجات O(1) تقسيمات

#### تحسينات التنفيذ

**1. التقسيم من الأعلى للأسفل**: بدلاً من التقسيم في الطريق إلى الأعلى، قسم العقد الممتلئة بشكل استباقي في الطريق إلى الأسفل أثناء البحث. هذا يبسط التنفيذ عن طريق تجنب التكرار.

**2. التقسيم المؤجل**: السماح بالفيض المؤقت (2k+1 مفتاح) وإعادة توزيع المفاتيح بين الأشقاء قبل التقسيم. هذا يحسن استخدام التخزين إلى 67% أو أعلى.

**3. التحميل الجماعي**: عند بناء شجرة B من بيانات مرتبة، احزم العقد إلى الحد الأقصى من السعة من الأسفل إلى الأعلى للحصول على أمثل استخدام للمساحة.

---

### Translation Notes

- **Figures referenced:** Multiple B-tree insertion diagrams showing step-by-step progression
- **Key terms introduced:** node splitting (تقسيم العقدة), overflow (فيض), median key (مفتاح وسيط), promotion (ترقية), amortized analysis (تحليل مطفأ), bulk loading (تحميل جماعي)
- **Algorithms:** INSERT with detailed splitting procedure
- **Equations:** Page access complexity: 2h
- **Citations:** None
- **Special handling:** Tree diagrams preserved in ASCII art, algorithm steps numbered, mathematical notation maintained

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.92
- Readability: 0.87
- Glossary consistency: 0.87
- **Overall section score:** 0.89
