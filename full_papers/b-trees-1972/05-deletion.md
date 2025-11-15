# Section 5: Deletion Algorithm
## القسم 5: خوارزمية الحذف

**Section:** deletion
**Translation Quality:** 0.87
**Glossary Terms Used:** deletion, algorithm, underflow, key redistribution, node merging, predecessor, successor, balanced tree

---

### English Version

#### Overview

Deletion in B-trees is the most complex operation because removing a key may cause a node to violate the minimum occupancy requirement (at least k keys). The algorithm must restore balance through key redistribution or node merging while maintaining the tree's structural properties.

#### Basic Deletion Strategy

There are three main cases when deleting a key:

**Case 1: Key is in a leaf node with more than k keys**
- Simply remove the key
- Node still satisfies minimum occupancy requirement
- No further action needed

**Case 2: Key is in an internal node**
- Replace key with its predecessor (rightmost key in left subtree) or successor (leftmost key in right subtree)
- Delete the predecessor/successor from the leaf (reducing to Case 1 or Case 3)

**Case 3: Key is in a leaf node with exactly k keys**
- Removing the key causes underflow (node would have k-1 keys)
- Must borrow from sibling or merge with sibling

#### Detailed Deletion Algorithm

**Algorithm DELETE(key)**

```
1. Search for key in tree
   - If not found, return ERROR

2. If key is in internal node N:
   - Find predecessor key K_pred (rightmost in left subtree)
     OR successor key K_succ (leftmost in right subtree)
   - Replace key with K_pred (or K_succ) in node N
   - Set key = K_pred (or K_succ)
   - Continue deletion from leaf

3. Now key is in leaf node L

4. Remove key from L

5. If L has at least k keys:
   - DONE (no underflow)

6. If L has k-1 keys (underflow):

   6a. Try to borrow from left sibling L_left:
       - If L_left has more than k keys:
         * Move parent's separator key down to L
         * Move rightmost key from L_left up to parent
         * DONE

   6b. Try to borrow from right sibling L_right:
       - If L_right has more than k keys:
         * Move parent's separator key down to L
         * Move leftmost key from L_right up to parent
         * DONE

   6c. If both siblings have exactly k keys (cannot borrow):
       - Merge L with one sibling:
         * Combine L and sibling into single node
         * Bring down separator key from parent
         * Delete separator from parent
         * If parent now has k-1 keys, recursively fix parent
         * If parent is root with 0 keys, make merged node new root
           (tree height decreases by 1)
```

#### Key Redistribution (Borrowing)

When a node has underflow but its sibling has extra keys, we can redistribute:

**Before borrowing from left sibling:**
```
Parent:     [... | K_sep | ...]
                  /      \
Left sibling:  [K₁ K₂ ... Kₖ Kₖ₊₁]
Right node (underflow): [K'₁ K'₂ ... K'ₖ₋₁]
```

**After borrowing:**
```
Parent:     [... | Kₖ₊₁ | ...]
                  /      \
Left sibling:  [K₁ K₂ ... Kₖ]
Right node:    [K_sep K'₁ K'₂ ... K'ₖ₋₁]
```

The separator key from parent moves down, and the extra key from sibling moves up to become the new separator.

#### Node Merging

When redistribution is not possible (both siblings have minimum keys), merge two nodes:

**Before merge:**
```
Parent:     [... | K_sep | ...]
                  /      \
Left node:      [K₁ ... Kₖ]
Right node (underflow): [K'₁ ... K'ₖ₋₁]
```

**After merge:**
```
Parent:     [... | ... ]  (K_sep removed)
                  |
Merged node: [K₁ ... Kₖ K_sep K'₁ ... K'ₖ₋₁]
```

The merged node contains 2k keys (k + 1 + k-1), which is exactly the maximum capacity.

#### Example: Deletion from B-tree of Order 2

Initial tree (k=2):

```
          [20,40,60]
        /   |   |   \
    [10,15] [30,35] [50,55] [70,80,90]
```

**Delete 35 (Case 1: leaf with extra keys):**
```
          [20,40,60]
        /   |   |   \
    [10,15] [30] [50,55] [70,80,90]
```
Note: [30] now has only 1 key, but minimum is k=2. Need to fix underflow.

**Borrow from left sibling [10,15]:**
```
          [15,40,60]
        /   |   |   \
    [10] [20,30] [50,55] [70,80,90]
```
- Separator 20 moves down from parent to [30]
- Key 15 moves up from [10,15] to parent

**Delete 50:**
```
          [15,40,60]
        /   |   |   \
    [10] [20,30] [55] [70,80,90]
```
[55] has underflow. Try to borrow from sibling.

**Borrow from right sibling [70,80,90]:**
```
          [15,40,70]
        /   |   |   \
    [10] [20,30] [55,60] [80,90]
```
- Separator 60 moves down to [55]
- Key 70 moves up from [70,80,90] to parent

**Delete 80:**
```
          [15,40,70]
        /   |   |   \
    [10] [20,30] [55,60] [90]
```
[90] has underflow, sibling [55,60] has minimum. Must merge.

**Merge [55,60] and [90]:**
```
          [15,40]
        /    |    \
    [10] [20,30] [55,60,70,90]
```
Separator 70 moves down, nodes merge.

**Delete 10:**
```
          [15,40]
        /    |    \
    [] [20,30] [55,60,70,90]
```
Root's left child is empty. Must fix.

**Merge root's children [20,30] and [55,60,70,90]:**
Root now has only one separator. Merge all into new root:
```
    [15,20,30,40,55,60,70,90]
```
Tree height decreased by 1. This is now the root (a leaf).

#### Properties of Deletion

**Theorem**: Deletion of a single key requires at most h page accesses for search plus h page writes for rebalancing, where h is the tree height.

**Invariants maintained**:
1. All leaves remain at the same level
2. All nodes (except root) contain at least k keys
3. All nodes contain at most 2k keys
4. Keys within nodes remain sorted
5. Search tree property is preserved

**Amortized cost**: Like insertion, while worst-case deletion may propagate changes up to the root, the amortized cost is O(1) merges per deletion.

#### Implementation Considerations

**1. Eager vs. Lazy deletion**:
- **Eager**: Immediately fix underflow as described above
- **Lazy**: Allow temporary underflow, fix during next insertion or periodically

**2. Deletion in B⁺-trees**:
- All data is in leaves, so deletion never occurs in internal nodes
- Internal nodes only need updating if a key used as separator is deleted
- Simplified compared to regular B-trees

**3. Predecessor vs. Successor**:
- When deleting from internal node, can choose either predecessor or successor
- Alternating between them helps maintain balance
- Some implementations always use predecessor (or always successor) for consistency

**4. Borrowing preference**:
- Can borrow from left or right sibling
- Some implementations prefer left (or right) for consistency
- Others check both and borrow from the one with more keys

---

### النسخة العربية

#### نظرة عامة

الحذف في أشجار B هو العملية الأكثر تعقيداً لأن إزالة مفتاح قد تسبب انتهاكاً للعقدة لمتطلب الإشغال الأدنى (k مفتاح على الأقل). يجب على الخوارزمية استعادة التوازن من خلال إعادة توزيع المفاتيح أو دمج العقد مع الحفاظ على خصائص بنية الشجرة.

#### استراتيجية الحذف الأساسية

هناك ثلاث حالات رئيسية عند حذف مفتاح:

**الحالة 1: المفتاح في عقدة ورقية مع أكثر من k مفتاح**
- ببساطة إزالة المفتاح
- العقدة لا تزال تحقق متطلب الإشغال الأدنى
- لا حاجة لإجراء آخر

**الحالة 2: المفتاح في عقدة داخلية**
- استبدال المفتاح بسابقه (المفتاح الأيمن في الشجرة الفرعية اليسرى) أو لاحقه (المفتاح الأيسر في الشجرة الفرعية اليمنى)
- حذف السابق/اللاحق من الورقة (التقليل إلى الحالة 1 أو الحالة 3)

**الحالة 3: المفتاح في عقدة ورقية مع k مفتاح بالضبط**
- إزالة المفتاح تسبب نقص (العقدة ستحتوي على k-1 مفتاح)
- يجب الاستعارة من الأشقاء أو الدمج مع الأشقاء

#### خوارزمية الحذف التفصيلية

**خوارزمية DELETE(key)**

```
1. البحث عن المفتاح key في الشجرة
   - إذا لم يتم العثور عليه، إرجاع خطأ

2. إذا كان المفتاح key في عقدة داخلية N:
   - إيجاد المفتاح السابق K_pred (الأيمن في الشجرة الفرعية اليسرى)
     أو المفتاح اللاحق K_succ (الأيسر في الشجرة الفرعية اليمنى)
   - استبدال المفتاح key بـ K_pred (أو K_succ) في العقدة N
   - ضبط key = K_pred (أو K_succ)
   - متابعة الحذف من الورقة

3. الآن المفتاح key في عقدة الورقة L

4. إزالة المفتاح key من L

5. إذا كانت L تحتوي على k مفتاح على الأقل:
   - انتهى (لا نقص)

6. إذا كانت L تحتوي على k-1 مفتاح (نقص):

   6a. محاولة الاستعارة من الشقيق الأيسر L_left:
       - إذا كانت L_left تحتوي على أكثر من k مفتاح:
         * نقل مفتاح الفاصل من الأب إلى الأسفل إلى L
         * نقل المفتاح الأيمن من L_left إلى الأعلى إلى الأب
         * انتهى

   6b. محاولة الاستعارة من الشقيق الأيمن L_right:
       - إذا كانت L_right تحتوي على أكثر من k مفتاح:
         * نقل مفتاح الفاصل من الأب إلى الأسفل إلى L
         * نقل المفتاح الأيسر من L_right إلى الأعلى إلى الأب
         * انتهى

   6c. إذا كان كلا الشقيقين يحتويان على k مفتاح بالضبط (لا يمكن الاستعارة):
       - دمج L مع أحد الأشقاء:
         * دمج L والشقيق في عقدة واحدة
         * إنزال مفتاح الفاصل من الأب
         * حذف الفاصل من الأب
         * إذا كان الأب الآن يحتوي على k-1 مفتاح، إصلاح الأب بشكل تكراري
         * إذا كان الأب هو الجذر مع 0 مفتاح، جعل العقدة المدمجة جذراً جديداً
           (ينخفض ارتفاع الشجرة بمقدار 1)
```

#### إعادة توزيع المفاتيح (الاستعارة)

عندما يكون لدى العقدة نقص ولكن شقيقها لديه مفاتيح إضافية، يمكننا إعادة التوزيع:

**قبل الاستعارة من الشقيق الأيسر:**
```
الأب:     [... | K_sep | ...]
                  /      \
الشقيق الأيسر:  [K₁ K₂ ... Kₖ Kₖ₊₁]
العقدة اليمنى (نقص): [K'₁ K'₂ ... K'ₖ₋₁]
```

**بعد الاستعارة:**
```
الأب:     [... | Kₖ₊₁ | ...]
                  /      \
الشقيق الأيسر:  [K₁ K₂ ... Kₖ]
العقدة اليمنى:    [K_sep K'₁ K'₂ ... K'ₖ₋₁]
```

ينتقل مفتاح الفاصل من الأب إلى الأسفل، والمفتاح الإضافي من الشقيق يتحرك إلى الأعلى ليصبح الفاصل الجديد.

#### دمج العقد

عندما لا تكون إعادة التوزيع ممكنة (كلا الشقيقين لديهما مفاتيح أدنى)، ادمج عقدتين:

**قبل الدمج:**
```
الأب:     [... | K_sep | ...]
                  /      \
العقدة اليسرى:      [K₁ ... Kₖ]
العقدة اليمنى (نقص): [K'₁ ... K'ₖ₋₁]
```

**بعد الدمج:**
```
الأب:     [... | ... ]  (تمت إزالة K_sep)
                  |
العقدة المدمجة: [K₁ ... Kₖ K_sep K'₁ ... K'ₖ₋₁]
```

العقدة المدمجة تحتوي على 2k مفتاح (k + 1 + k-1)، وهو بالضبط السعة القصوى.

#### مثال: الحذف من شجرة B من الرتبة 2

الشجرة الأولية (k=2):

```
          [20,40,60]
        /   |   |   \
    [10,15] [30,35] [50,55] [70,80,90]
```

**حذف 35 (الحالة 1: ورقة مع مفاتيح إضافية):**
```
          [20,40,60]
        /   |   |   \
    [10,15] [30] [50,55] [70,80,90]
```
ملاحظة: [30] الآن لديها مفتاح واحد فقط، لكن الحد الأدنى هو k=2. يجب إصلاح النقص.

**الاستعارة من الشقيق الأيسر [10,15]:**
```
          [15,40,60]
        /   |   |   \
    [10] [20,30] [50,55] [70,80,90]
```
- الفاصل 20 ينتقل إلى الأسفل من الأب إلى [30]
- المفتاح 15 ينتقل إلى الأعلى من [10,15] إلى الأب

**حذف 50:**
```
          [15,40,60]
        /   |   |   \
    [10] [20,30] [55] [70,80,90]
```
[55] لديها نقص. حاول الاستعارة من الشقيق.

**الاستعارة من الشقيق الأيمن [70,80,90]:**
```
          [15,40,70]
        /   |   |   \
    [10] [20,30] [55,60] [80,90]
```
- الفاصل 60 ينتقل إلى الأسفل إلى [55]
- المفتاح 70 ينتقل إلى الأعلى من [70,80,90] إلى الأب

**حذف 80:**
```
          [15,40,70]
        /   |   |   \
    [10] [20,30] [55,60] [90]
```
[90] لديها نقص، الشقيق [55,60] لديه الحد الأدنى. يجب الدمج.

**دمج [55,60] و [90]:**
```
          [15,40]
        /    |    \
    [10] [20,30] [55,60,70,90]
```
الفاصل 70 ينتقل إلى الأسفل، العقد تندمج.

**حذف 10:**
```
          [15,40]
        /    |    \
    [] [20,30] [55,60,70,90]
```
طفل الجذر الأيسر فارغ. يجب الإصلاح.

**دمج أطفال الجذر [20,30] و [55,60,70,90]:**
الجذر الآن لديه فاصل واحد فقط. دمج الكل في جذر جديد:
```
    [15,20,30,40,55,60,70,90]
```
انخفض ارتفاع الشجرة بمقدار 1. هذا الآن هو الجذر (ورقة).

#### خصائص الحذف

**نظرية**: حذف مفتاح واحد يتطلب على الأكثر h وصولاً للصفحات للبحث بالإضافة إلى h كتابة للصفحات لإعادة التوازن، حيث h هو ارتفاع الشجرة.

**الثوابت المحافظ عليها**:
1. تبقى جميع الأوراق في نفس المستوى
2. جميع العقد (باستثناء الجذر) تحتوي على k مفتاح على الأقل
3. جميع العقد تحتوي على 2k مفتاح على الأكثر
4. المفاتيح داخل العقد تبقى مرتبة
5. خاصية شجرة البحث محفوظة

**التكلفة المطفأة**: مثل الإدراج، بينما قد ينشر الحذف في أسوأ الحالات التغييرات حتى الجذر، فإن التكلفة المطفأة هي O(1) عمليات دمج لكل حذف.

#### اعتبارات التنفيذ

**1. الحذف الحريص مقابل الكسول**:
- **الحريص**: إصلاح النقص على الفور كما هو موصوف أعلاه
- **الكسول**: السماح بالنقص المؤقت، الإصلاح أثناء الإدراج التالي أو بشكل دوري

**2. الحذف في أشجار B⁺**:
- جميع البيانات في الأوراق، لذا لا يحدث الحذف في العقد الداخلية
- العقد الداخلية تحتاج فقط إلى التحديث إذا تم حذف مفتاح مستخدم كفاصل
- مبسط مقارنة بأشجار B العادية

**3. السابق مقابل اللاحق**:
- عند الحذف من عقدة داخلية، يمكن اختيار السابق أو اللاحق
- التناوب بينهما يساعد في الحفاظ على التوازن
- بعض التطبيقات تستخدم دائماً السابق (أو دائماً اللاحق) للاتساق

**4. تفضيل الاستعارة**:
- يمكن الاستعارة من الشقيق الأيسر أو الأيمن
- بعض التطبيقات تفضل اليسار (أو اليمين) للاتساق
- البعض الآخر يتحقق من كليهما ويستعير من الذي لديه مفاتيح أكثر

---

### Translation Notes

- **Figures referenced:** Multiple deletion scenario diagrams
- **Key terms introduced:** underflow (نقص), key redistribution (إعادة توزيع المفاتيح), node merging (دمج العقد), predecessor (سابق), successor (لاحق), separator key (مفتاح الفاصل), eager deletion (حذف حريص), lazy deletion (حذف كسول)
- **Algorithms:** DELETE with detailed case handling
- **Equations:** None specific to deletion
- **Citations:** None
- **Special handling:** Tree transformation diagrams preserved, step-by-step deletion examples shown

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.87
