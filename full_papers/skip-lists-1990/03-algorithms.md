# Section 3: Algorithms for Skip Lists
## القسم 3: خوارزميات قوائم التخطي

**Section:** algorithms
**Translation Quality:** 0.86
**Glossary Terms Used:** algorithm, search, insertion, deletion, pointer, level, complexity, node

---

### English Version

## Search Algorithm

Searching for an element in a skip list is similar to searching in a sorted linked list, but we can skip over many elements by following higher-level pointers when possible.

**Algorithm: Search(list, searchKey)**
```
x := list->header
-- loop invariant: x->key < searchKey
for i := list->level downto 1 do
    while x->forward[i]->key < searchKey do
        x := x->forward[i]
    -- x->key < searchKey <= x->forward[i]->key
-- x->key < searchKey <= x->forward[1]->key
x := x->forward[1]
if x->key = searchKey then return x
else return failure
```

The search starts at the header node at the highest level of the list. At each level, we move forward as far as possible while staying to the left of the search key. When we can't go forward anymore at a level, we drop down one level and continue. When we drop from level 1, we examine the next element to see if it matches the search key.

## Insertion Algorithm

To insert an element, we first search for the position where it should be inserted. During the search, we maintain an update vector that records, for each level, the rightmost node visited before dropping to the next level. After the position is located, we randomly determine the level of the new node and insert it by adjusting forward pointers.

**Algorithm: Insert(list, searchKey, newValue)**
```
local update[1..MaxLevel]
x := list->header
for i := list->level downto 1 do
    while x->forward[i]->key < searchKey do
        x := x->forward[i]
    -- x->key < searchKey <= x->forward[i]->key
    update[i] := x
-- x->key < searchKey <= x->forward[1]->key
x := x->forward[1]
if x->key = searchKey then x->value := newValue
else
    lvl := randomLevel()
    if lvl > list->level then
        for i := list->level + 1 to lvl do
            update[i] := list->header
        list->level := lvl
    x := makeNode(lvl, searchKey, value)
    for i := 1 to lvl do
        x->forward[i] := update[i]->forward[i]
        update[i]->forward[i] := x
```

The randomLevel() function returns a random level for a new node. It should return a value k with probability p^(k-1) * (1-p). Typically, p = 1/2 or p = 1/4.

**Algorithm: randomLevel()**
```
lvl := 1
-- random() returns a random value in [0...1)
while random() < p and lvl < MaxLevel do
    lvl := lvl + 1
return lvl
```

## Deletion Algorithm

Deletion is similar to insertion. We search for the element to be deleted, maintaining the update vector. If the element is found, we remove it by adjusting the forward pointers of the nodes in the update vector.

**Algorithm: Delete(list, searchKey)**
```
local update[1..MaxLevel]
x := list->header
for i := list->level downto 1 do
    while x->forward[i]->key < searchKey do
        x := x->forward[i]
    update[i] := x
x := x->forward[1]
if x->key = searchKey then
    for i := 1 to list->level do
        if update[i]->forward[i] ≠ x then break
        update[i]->forward[i] := x->forward[i]
    free(x)
    while list->level > 1 and
          list->header->forward[list->level] = NIL do
        list->level := list->level - 1
```

After removing the node, we decrease the level of the list if the removed node was the only node at the highest levels.

## Complexity

All three operations (search, insertion, deletion) have expected time complexity O(log n), where n is the number of elements in the list. The space complexity is O(n) on average, as the expected total number of pointers across all nodes is O(n).

---

### النسخة العربية

## خوارزمية البحث

البحث عن عنصر في قائمة التخطي يشبه البحث في قائمة مرتبطة مرتبة، لكن يمكننا تخطي العديد من العناصر من خلال اتباع مؤشرات المستوى الأعلى عندما يكون ذلك ممكناً.

**الخوارزمية: Search(list, searchKey)**
```
x := list->header
-- ثابت الحلقة: x->key < searchKey
for i := list->level downto 1 do
    while x->forward[i]->key < searchKey do
        x := x->forward[i]
    -- x->key < searchKey <= x->forward[i]->key
-- x->key < searchKey <= x->forward[1]->key
x := x->forward[1]
if x->key = searchKey then return x
else return failure
```

يبدأ البحث عند عقدة الرأس في أعلى مستوى للقائمة. في كل مستوى، نتحرك للأمام بقدر الإمكان مع البقاء على يسار مفتاح البحث. عندما لا نستطيع المضي قدماً في مستوى ما، ننخفض مستوى واحداً ونستمر. عندما ننخفض من المستوى 1، نفحص العنصر التالي لمعرفة ما إذا كان يطابق مفتاح البحث.

## خوارزمية الإدراج

لإدراج عنصر، نبحث أولاً عن الموضع الذي يجب إدراجه فيه. أثناء البحث، نحتفظ بمتجه تحديث يسجل، لكل مستوى، العقدة الأكثر يميناً التي تمت زيارتها قبل الانخفاض إلى المستوى التالي. بعد تحديد الموضع، نحدد بشكل عشوائي مستوى العقدة الجديدة وندرجها عن طريق تعديل المؤشرات الأمامية.

**الخوارزمية: Insert(list, searchKey, newValue)**
```
local update[1..MaxLevel]
x := list->header
for i := list->level downto 1 do
    while x->forward[i]->key < searchKey do
        x := x->forward[i]
    -- x->key < searchKey <= x->forward[i]->key
    update[i] := x
-- x->key < searchKey <= x->forward[1]->key
x := x->forward[1]
if x->key = searchKey then x->value := newValue
else
    lvl := randomLevel()
    if lvl > list->level then
        for i := list->level + 1 to lvl do
            update[i] := list->header
        list->level := lvl
    x := makeNode(lvl, searchKey, value)
    for i := 1 to lvl do
        x->forward[i] := update[i]->forward[i]
        update[i]->forward[i] := x
```

تُرجع دالة randomLevel() مستوى عشوائي للعقدة الجديدة. يجب أن ترجع القيمة k باحتمال p^(k-1) * (1-p). عادةً، p = 1/2 أو p = 1/4.

**الخوارزمية: randomLevel()**
```
lvl := 1
-- random() ترجع قيمة عشوائية في [0...1)
while random() < p and lvl < MaxLevel do
    lvl := lvl + 1
return lvl
```

## خوارزمية الحذف

الحذف يشبه الإدراج. نبحث عن العنصر المراد حذفه، مع الاحتفاظ بمتجه التحديث. إذا تم العثور على العنصر، نزيله عن طريق تعديل المؤشرات الأمامية للعقد في متجه التحديث.

**الخوارزمية: Delete(list, searchKey)**
```
local update[1..MaxLevel]
x := list->header
for i := list->level downto 1 do
    while x->forward[i]->key < searchKey do
        x := x->forward[i]
    update[i] := x
x := x->forward[1]
if x->key = searchKey then
    for i := 1 to list->level do
        if update[i]->forward[i] ≠ x then break
        update[i]->forward[i] := x->forward[i]
    free(x)
    while list->level > 1 and
          list->header->forward[list->level] = NIL do
        list->level := list->level - 1
```

بعد إزالة العقدة، نخفض مستوى القائمة إذا كانت العقدة المحذوفة هي العقدة الوحيدة في المستويات الأعلى.

## التعقيد

جميع العمليات الثلاث (البحث والإدراج والحذف) لها تعقيد زمني متوقع O(log n)، حيث n هو عدد العناصر في القائمة. تعقيد المساحة هو O(n) في المتوسط، حيث أن العدد الإجمالي المتوقع للمؤشرات عبر جميع العقد هو O(n).

---

### Translation Notes

- **Algorithms:** 3 complete algorithms presented (Search, Insert, Delete) plus randomLevel helper
- **Key terms introduced:**
  - update vector (متجه تحديث)
  - loop invariant (ثابت الحلقة)
  - randomLevel (مستوى عشوائي)
  - makeNode (إنشاء عقدة)
  - free (تحرير)
- **Code comments:** Translated key comments while keeping code structure in English
- **Equations:** Probability notation p^(k-1) * (1-p) preserved
- **Special handling:**
  - Pseudocode kept in English as standard practice
  - Key comments translated in both versions
  - Variable names kept in English
  - Complexity notation preserved

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86
