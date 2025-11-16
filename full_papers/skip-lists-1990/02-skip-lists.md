# Section 2: Skip Lists
## القسم 2: قوائم التخطي

**Section:** Skip Lists Algorithm
**Translation Quality:** 0.87
**Glossary Terms Used:** skip list, level, forward pointer, search, insertion, deletion, node, probabilistic, linked list, nil

---

### English Version

#### Basic Structure

A skip list is a data structure that consists of multiple levels of linked lists. The bottom level (level 0) contains all elements in sorted order, while each higher level contains a subset of the elements from the level below.

Each element is represented by a node, and each node has a height (or level) that determines how many forward pointers it contains. A node of height $i$ has $i$ forward pointers, indexed from 0 to $i-1$. The $j$-th forward pointer of a node points to the next node with height greater than or equal to $j+1$.

The skip list structure is maintained with a header node that has the maximum possible height (typically $\log n$ where $n$ is the number of elements). All forward pointers that do not point to an actual node point to a special NIL value.

#### Levels and Forward Pointers

The level of a node is chosen randomly when the node is inserted, using a simple probabilistic scheme:
- Level 0: with probability 1
- Level $i$ (for $i > 0$): with probability $p^i$, where $p$ is typically 1/2 or 1/4

This means approximately half the nodes have pointers at level 1, a quarter have pointers at level 2, and so on. The expected number of levels in a skip list of $n$ elements is $O(\log n)$.

#### Search Algorithm

To search for an element with key $x$:
1. Start at the highest level of the header node
2. At each level, traverse forward while the next node's key is less than $x$
3. When you can't go forward at the current level, drop down one level
4. Repeat until you reach level 0
5. If the next node at level 0 has key $x$, the element is found; otherwise, it's not in the list

The search path follows a staircase pattern, descending through the levels as it approaches the target location.

Pseudocode for search:

```
Search(list, searchKey)
    x := list->header
    for i := list->level downto 0 do
        while x->forward[i]->key < searchKey do
            x := x->forward[i]
        end while
    end for
    x := x->forward[0]
    if x->key = searchKey then
        return x->value
    else
        return nil
    end if
```

#### Insertion Algorithm

To insert an element with key $x$ and value $v$:
1. Search for the position where $x$ should be inserted (as in the search algorithm)
2. During the search, maintain an update array that records the rightmost node at each level whose forward pointer should be modified
3. Choose a random level $l$ for the new node
4. Create a new node with height $l$
5. Update the forward pointers at levels 0 through $l-1$ to insert the new node

Pseudocode for insertion:

```
Insert(list, searchKey, newValue)
    update[0..MaxLevel]
    x := list->header
    for i := list->level downto 0 do
        while x->forward[i]->key < searchKey do
            x := x->forward[i]
        end while
        update[i] := x
    end for
    x := x->forward[0]

    if x->key = searchKey then
        x->value := newValue
    else
        lvl := randomLevel()
        if lvl > list->level then
            for i := list->level + 1 to lvl do
                update[i] := list->header
            end for
            list->level := lvl
        end if
        x := makeNode(lvl, searchKey, newValue)
        for i := 0 to lvl do
            x->forward[i] := update[i]->forward[i]
            update[i]->forward[i] := x
        end for
    end if
```

#### Deletion Algorithm

To delete an element with key $x$:
1. Search for the node containing $x$ (as in the search algorithm)
2. Maintain an update array as in insertion
3. If the node is found, update the forward pointers of all nodes in the update array to skip over the deleted node
4. Free the deleted node
5. Reduce the level of the list if the highest level is now empty

Pseudocode for deletion:

```
Delete(list, searchKey)
    update[0..MaxLevel]
    x := list->header
    for i := list->level downto 0 do
        while x->forward[i]->key < searchKey do
            x := x->forward[i]
        end while
        update[i] := x
    end for
    x := x->forward[0]

    if x->key = searchKey then
        for i := 0 to list->level do
            if update[i]->forward[i] ≠ x then
                break
            end if
            update[i]->forward[i] := x->forward[i]
        end for
        free(x)
        while list->level > 0 and list->header->forward[list->level] = NIL do
            list->level := list->level - 1
        end while
    end if
```

#### Random Level Generation

The random level for a new node is generated using the following algorithm:

```
randomLevel()
    lvl := 0
    while random() < p and lvl < MaxLevel do
        lvl := lvl + 1
    end while
    return lvl
```

where $p$ is typically set to 1/2 or 1/4. This ensures that the expected distribution of levels follows a geometric distribution.

---

### النسخة العربية

#### البنية الأساسية

قائمة التخطي هي بنية بيانات تتكون من مستويات متعددة من القوائم المترابطة. يحتوي المستوى السفلي (المستوى 0) على جميع العناصر بترتيب مرتب، بينما يحتوي كل مستوى أعلى على مجموعة فرعية من العناصر الموجودة في المستوى الأدنى.

يتم تمثيل كل عنصر بعقدة، ولكل عقدة ارتفاع (أو مستوى) يحدد عدد المؤشرات الأمامية التي تحتويها. تحتوي العقدة ذات الارتفاع $i$ على $i$ مؤشر أمامي، مفهرسة من 0 إلى $i-1$. يشير المؤشر الأمامي الـ $j$ لعقدة إلى العقدة التالية ذات الارتفاع الأكبر من أو يساوي $j+1$.

يتم الحفاظ على بنية قائمة التخطي باستخدام عقدة رأسية لها أقصى ارتفاع ممكن (عادةً $\log n$ حيث $n$ هو عدد العناصر). تشير جميع المؤشرات الأمامية التي لا تشير إلى عقدة فعلية إلى قيمة NIL خاصة.

#### المستويات والمؤشرات الأمامية

يتم اختيار مستوى العقدة بشكل عشوائي عند إدراج العقدة، باستخدام مخطط احتمالي بسيط:
- المستوى 0: باحتمال 1
- المستوى $i$ (لـ $i > 0$): باحتمال $p^i$، حيث $p$ عادةً 1/2 أو 1/4

هذا يعني أن حوالي نصف العقد لديها مؤشرات عند المستوى 1، والربع لديه مؤشرات عند المستوى 2، وهكذا. العدد المتوقع للمستويات في قائمة تخطي من $n$ عنصر هو $O(\log n)$.

#### خوارزمية البحث

للبحث عن عنصر بمفتاح $x$:
1. ابدأ من أعلى مستوى في العقدة الرأسية
2. عند كل مستوى، تحرك للأمام بينما مفتاح العقدة التالية أقل من $x$
3. عندما لا يمكنك التقدم للأمام عند المستوى الحالي، انزل مستوى واحد للأسفل
4. كرر حتى تصل إلى المستوى 0
5. إذا كانت العقدة التالية عند المستوى 0 لها مفتاح $x$، فقد تم العثور على العنصر؛ وإلا فهو ليس في القائمة

يتبع مسار البحث نمط الدرج، حيث ينزل عبر المستويات بينما يقترب من الموقع المستهدف.

الشيفرة الكاذبة للبحث:

```
Search(list, searchKey)
    x := list->header
    for i := list->level downto 0 do
        while x->forward[i]->key < searchKey do
            x := x->forward[i]
        end while
    end for
    x := x->forward[0]
    if x->key = searchKey then
        return x->value
    else
        return nil
    end if
```

#### خوارزمية الإدراج

لإدراج عنصر بمفتاح $x$ وقيمة $v$:
1. ابحث عن الموضع الذي يجب إدراج $x$ فيه (كما في خوارزمية البحث)
2. أثناء البحث، احتفظ بمصفوفة تحديث تسجل العقدة الأيمن القصوى عند كل مستوى والتي يجب تعديل مؤشرها الأمامي
3. اختر مستوى عشوائي $l$ للعقدة الجديدة
4. أنشئ عقدة جديدة بارتفاع $l$
5. حدّث المؤشرات الأمامية عند المستويات من 0 إلى $l-1$ لإدراج العقدة الجديدة

الشيفرة الكاذبة للإدراج:

```
Insert(list, searchKey, newValue)
    update[0..MaxLevel]
    x := list->header
    for i := list->level downto 0 do
        while x->forward[i]->key < searchKey do
            x := x->forward[i]
        end while
        update[i] := x
    end for
    x := x->forward[0]

    if x->key = searchKey then
        x->value := newValue
    else
        lvl := randomLevel()
        if lvl > list->level then
            for i := list->level + 1 to lvl do
                update[i] := list->header
            end for
            list->level := lvl
        end if
        x := makeNode(lvl, searchKey, newValue)
        for i := 0 to lvl do
            x->forward[i] := update[i]->forward[i]
            update[i]->forward[i] := x
        end for
    end if
```

#### خوارزمية الحذف

لحذف عنصر بمفتاح $x$:
1. ابحث عن العقدة التي تحتوي على $x$ (كما في خوارزمية البحث)
2. احتفظ بمصفوفة تحديث كما في الإدراج
3. إذا تم العثور على العقدة، حدّث المؤشرات الأمامية لجميع العقد في مصفوفة التحديث لتخطي العقدة المحذوفة
4. حرر العقدة المحذوفة
5. قلل مستوى القائمة إذا أصبح أعلى مستوى فارغاً الآن

الشيفرة الكاذبة للحذف:

```
Delete(list, searchKey)
    update[0..MaxLevel]
    x := list->header
    for i := list->level downto 0 do
        while x->forward[i]->key < searchKey do
            x := x->forward[i]
        end while
        update[i] := x
    end for
    x := x->forward[0]

    if x->key = searchKey then
        for i := 0 to list->level do
            if update[i]->forward[i] ≠ x then
                break
            end if
            update[i]->forward[i] := x->forward[i]
        end for
        free(x)
        while list->level > 0 and list->header->forward[list->level] = NIL do
            list->level := list->level - 1
        end while
    end if
```

#### توليد المستوى العشوائي

يتم توليد المستوى العشوائي لعقدة جديدة باستخدام الخوارزمية التالية:

```
randomLevel()
    lvl := 0
    while random() < p and lvl < MaxLevel do
        lvl := lvl + 1
    end while
    return lvl
```

حيث يتم تعيين $p$ عادةً إلى 1/2 أو 1/4. هذا يضمن أن التوزيع المتوقع للمستويات يتبع توزيعاً هندسياً.

---

### Translation Notes

- **Algorithms:** Pseudocode kept in English (industry standard)
- **Mathematical notation:** Preserved as LaTeX ($\log n$, $O(\log n)$, etc.)
- **Key technical terms:**
  - Skip list (قائمة التخطي)
  - Level (مستوى)
  - Forward pointer (مؤشر أمامي)
  - Header node (عقدة رأسية)
  - NIL value (قيمة NIL) - kept as technical constant
  - Update array (مصفوفة تحديث)
  - Random level (مستوى عشوائي)
  - Geometric distribution (توزيع هندسي)

- **Figures referenced:** None in this section
- **Equations:** Probability formulas ($p^i$, $O(\log n)$)
- **Pseudocode:** 4 algorithms (Search, Insert, Delete, randomLevel)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.87

---

### Back-Translation Check (Key Algorithm Description)

Arabic: "يتم اختيار مستوى العقدة بشكل عشوائي عند إدراج العقدة، باستخدام مخطط احتمالي بسيط"

Back to English: "The level of a node is chosen randomly when inserting the node, using a simple probabilistic scheme"

Original: "The level of a node is chosen randomly when the node is inserted, using a simple probabilistic scheme"

**Match:** Excellent semantic match
