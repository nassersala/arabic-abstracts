# Section 2: Definition and Properties of B-trees
## القسم 2: تعريف وخصائص أشجار B

**Section:** b-tree-definition
**Translation Quality:** 0.88
**Glossary Terms Used:** B-tree, data structure, node, key, pointer, leaf node, internal node, root, height, branching factor, balanced

---

### English Version

#### Formal Definition

A B-tree of order k (or degree k) is a tree data structure with the following properties:

1. **Every node contains at most 2k keys**: This defines the maximum capacity of each node.

2. **Every node (except the root) contains at least k keys**: This ensures minimum occupancy, guaranteeing storage utilization of at least 50%.

3. **The root contains at least 1 key** (unless the tree is empty).

4. **All leaves appear at the same level**: This is the crucial balancing property that ensures all paths from root to leaf have the same length.

5. **A non-leaf node with n keys contains n+1 children**: The keys act as separators, defining n+1 intervals.

6. **Keys within each node are maintained in sorted order**: For a node containing keys K₁, K₂, ..., Kₙ, we have K₁ ≤ K₂ ≤ ... ≤ Kₙ.

#### Node Structure

Each node in a B-tree has the following structure:

```
[n | K₁ P₁ K₂ P₂ ... Kₙ Pₙ P₀]
```

Where:
- n is the number of keys currently stored in the node
- K₁, K₂, ..., Kₙ are the keys stored in ascending order
- P₀, P₁, ..., Pₙ are pointers to child nodes (for internal nodes) or data records (for leaf nodes)
- For internal nodes, pointer Pᵢ points to the subtree containing all keys K such that Kᵢ ≤ K < Kᵢ₊₁

#### Search Tree Property

The B-tree maintains the search tree property at every level. For any internal node containing keys K₁, K₂, ..., Kₙ with child pointers P₀, P₁, ..., Pₙ:

- All keys in the subtree pointed to by P₀ are less than K₁
- All keys in the subtree pointed to by Pᵢ (for 1 ≤ i < n) satisfy: Kᵢ ≤ key < Kᵢ₊₁
- All keys in the subtree pointed to by Pₙ are greater than or equal to Kₙ

#### Height and Capacity

For a B-tree of order k containing n keys:

**Minimum height**: The tree has minimum height when every node (except possibly the root) is as full as possible:
$$h_{min} = \lceil \log_{2k+1}(n+1) \rceil$$

**Maximum height**: The tree has maximum height when every node contains the minimum number of keys:
$$h_{max} = \lfloor \log_{k+1}(\frac{n+1}{2}) \rfloor + 1$$

In both cases, the height grows logarithmically with the number of keys, ensuring efficient search, insertion, and deletion operations.

#### Storage Utilization

The minimum storage utilization of a B-tree is 50%, which occurs when every node (except the root) contains exactly k keys (the minimum allowed). In practice, after random insertions and deletions, B-trees typically achieve 65-70% storage utilization.

**Theorem**: A B-tree of order k storing n keys requires at most $\lceil \frac{n}{k} \rceil + 1$ pages.

**Proof**: In the worst case (minimum utilization), each internal page contains k keys. The maximum number of keys that can be stored in p pages is therefore 2kp (since each page can hold at most 2k keys). Setting 2kp = n gives p = n/(2k), so at most $\lceil \frac{n}{k} \rceil$ pages are needed, plus one for the root.

#### Comparison with Binary Trees

To illustrate the advantage of B-trees, consider storing 1,000,000 keys:

- **Balanced binary tree** (k=1): Height ≈ log₂(1,000,000) ≈ 20 levels
- **B-tree with k=100**: Height ≈ log₂₀₁(1,000,000) ≈ 3 levels

This dramatic reduction in height translates directly to fewer disk accesses, making B-trees far superior for secondary storage applications.

#### Variants

While this paper focuses on the basic B-tree structure, several important variants exist:

- **B⁺-trees**: All data is stored in leaf nodes, with internal nodes containing only keys and pointers
- **B*-trees**: Maintains higher minimum occupancy (approximately 67%) by redistributing keys before splitting

---

### النسخة العربية

#### التعريف الرسمي

شجرة B من الرتبة k (أو الدرجة k) هي بنية بيانات شجرية ذات الخصائص التالية:

1. **كل عقدة تحتوي على 2k مفتاح على الأكثر**: هذا يحدد السعة القصوى لكل عقدة.

2. **كل عقدة (باستثناء الجذر) تحتوي على k مفتاح على الأقل**: هذا يضمن الإشغال الأدنى، مما يضمن استخدام التخزين بنسبة 50% على الأقل.

3. **الجذر يحتوي على مفتاح واحد على الأقل** (ما لم تكن الشجرة فارغة).

4. **جميع الأوراق تظهر في نفس المستوى**: هذه هي خاصية التوازن الحاسمة التي تضمن أن جميع المسارات من الجذر إلى الأوراق لها نفس الطول.

5. **عقدة غير ورقية تحتوي على n مفتاح تحتوي على n+1 طفل**: المفاتيح تعمل كفواصل، تحدد n+1 فترة.

6. **المفاتيح داخل كل عقدة محفوظة بترتيب مرتب**: لعقدة تحتوي على المفاتيح K₁, K₂, ..., Kₙ، لدينا K₁ ≤ K₂ ≤ ... ≤ Kₙ.

#### بنية العقدة

كل عقدة في شجرة B لها البنية التالية:

```
[n | K₁ P₁ K₂ P₂ ... Kₙ Pₙ P₀]
```

حيث:
- n هو عدد المفاتيح المخزنة حالياً في العقدة
- K₁, K₂, ..., Kₙ هي المفاتيح المخزنة بترتيب تصاعدي
- P₀, P₁, ..., Pₙ هي مؤشرات إلى العقد الفرعية (للعقد الداخلية) أو سجلات البيانات (لعقد الأوراق)
- بالنسبة للعقد الداخلية، المؤشر Pᵢ يشير إلى الشجرة الفرعية التي تحتوي على جميع المفاتيح K بحيث Kᵢ ≤ K < Kᵢ₊₁

#### خاصية شجرة البحث

تحتفظ شجرة B بخاصية شجرة البحث في كل مستوى. لأي عقدة داخلية تحتوي على المفاتيح K₁, K₂, ..., Kₙ مع مؤشرات الأطفال P₀, P₁, ..., Pₙ:

- جميع المفاتيح في الشجرة الفرعية التي يشير إليها P₀ أقل من K₁
- جميع المفاتيح في الشجرة الفرعية التي يشير إليها Pᵢ (لـ 1 ≤ i < n) تحقق: Kᵢ ≤ مفتاح < Kᵢ₊₁
- جميع المفاتيح في الشجرة الفرعية التي يشير إليها Pₙ أكبر من أو تساوي Kₙ

#### الارتفاع والسعة

بالنسبة لشجرة B من الرتبة k تحتوي على n مفتاح:

**الارتفاع الأدنى**: الشجرة لها ارتفاع أدنى عندما تكون كل عقدة (باستثناء الجذر ربما) ممتلئة قدر الإمكان:
$$h_{min} = \lceil \log_{2k+1}(n+1) \rceil$$

**الارتفاع الأقصى**: الشجرة لها ارتفاع أقصى عندما تحتوي كل عقدة على الحد الأدنى من المفاتيح:
$$h_{max} = \lfloor \log_{k+1}(\frac{n+1}{2}) \rfloor + 1$$

في كلتا الحالتين، ينمو الارتفاع لوغاريتمياً مع عدد المفاتيح، مما يضمن عمليات بحث وإدراج وحذف فعالة.

#### استخدام التخزين

استخدام التخزين الأدنى لشجرة B هو 50%، والذي يحدث عندما تحتوي كل عقدة (باستثناء الجذر) على k مفتاح بالضبط (الحد الأدنى المسموح به). في الممارسة العملية، بعد عمليات الإدراج والحذف العشوائية، تحقق أشجار B عادةً استخدام تخزين بنسبة 65-70%.

**نظرية**: شجرة B من الرتبة k تخزن n مفتاح تتطلب على الأكثر $\lceil \frac{n}{k} \rceil + 1$ صفحة.

**البرهان**: في أسوأ الحالات (الحد الأدنى من الاستخدام)، تحتوي كل صفحة داخلية على k مفتاح. العدد الأقصى من المفاتيح التي يمكن تخزينها في p صفحة هو إذن 2kp (لأن كل صفحة يمكن أن تحمل 2k مفتاح على الأكثر). بضبط 2kp = n نحصل على p = n/(2k)، لذا نحتاج على الأكثر إلى $\lceil \frac{n}{k} \rceil$ صفحة، بالإضافة إلى واحدة للجذر.

#### المقارنة مع الأشجار الثنائية

لتوضيح ميزة أشجار B، لنأخذ مثال تخزين 1,000,000 مفتاح:

- **شجرة ثنائية متوازنة** (k=1): الارتفاع ≈ log₂(1,000,000) ≈ 20 مستوى
- **شجرة B مع k=100**: الارتفاع ≈ log₂₀₁(1,000,000) ≈ 3 مستويات

هذا الانخفاض الدراماتيكي في الارتفاع يترجم مباشرة إلى وصولات أقل للقرص، مما يجعل أشجار B متفوقة بكثير لتطبيقات التخزين الثانوي.

#### المتغيرات

بينما تركز هذه الورقة على بنية شجرة B الأساسية، توجد عدة متغيرات مهمة:

- **أشجار B⁺**: جميع البيانات مخزنة في عقد الأوراق، مع العقد الداخلية التي تحتوي فقط على المفاتيح والمؤشرات
- **أشجار B***: تحتفظ بإشغال أدنى أعلى (حوالي 67%) عن طريق إعادة توزيع المفاتيح قبل الانقسام

---

### Translation Notes

- **Figures referenced:** Node structure diagram (conceptual)
- **Key terms introduced:** order (رتبة), degree (درجة), leaf node (عقدة ورقية), internal node (عقدة داخلية), root (جذر), height (ارتفاع), minimum occupancy (الإشغال الأدنى)
- **Equations:** $h_{min} = \lceil \log_{2k+1}(n+1) \rceil$, $h_{max} = \lfloor \log_{k+1}(\frac{n+1}{2}) \rfloor + 1$, $\lceil \frac{n}{k} \rceil + 1$
- **Citations:** None
- **Special handling:** Mathematical notation preserved, theorem and proof structure maintained, code-like node structure kept in monospace format

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.91
- Readability: 0.86
- Glossary consistency: 0.86
- **Overall section score:** 0.88
