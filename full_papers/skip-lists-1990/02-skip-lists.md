# Section 2: Skip Lists
## القسم 2: قوائم التخطي

**Section:** skip-lists
**Translation Quality:** 0.87
**Glossary Terms Used:** data structure, pointer, node, level, probability, forward pointer, NIL

---

### English Version

## Informal Description

In an ordinary sorted linked list, search requires scanning the list until the desired element is found or it is determined that the element is not in the list. With n elements, this takes O(n) time. If we have a pointer to every other element, we can reduce the time to O(n/2) by checking the element pointed to and skipping forward if it is less than the element we are searching for.

We can continue this idea recursively. If we have a pointer to every 2^i-th element, we get search time O(n/2^i + 2^i). The optimal i is log n, giving O(log n) search time. The problem is that inserting a new element into such a structure would require restructuring the entire list.

Skip lists solve this problem by determining the level of each element randomly when it is inserted. An element of level i has i forward pointers, indexed 1 through i. We do not need to keep track of the levels of elements; the level of an element is determined by the number of forward pointers it has.

The level of a list is the maximum level of any element in the list (or 1 if the list is empty). The header of the list has forward pointers at levels 1 through the maximum level of the list. The forward pointers of the header at levels higher than the current maximum level of the list are NIL.

## Formal Description

A skip list is a probabilistic data structure that allows O(log n) average time for search as well as insertion and deletion of elements. It consists of a hierarchy of linked lists, with the bottom-level list containing all elements in sorted order, and each higher level containing a sparser subsequence of the elements.

Formally, a skip list for a set S of elements consists of a header node and a collection of nodes, each node having:
- A key value (except for the header)
- An array forward[1..MaxLevel] of pointers to successor nodes
- The level of the node (the highest index in forward with a non-NIL pointer)

Properties:
1. All elements are present in the level 1 list in sorted order
2. Each element at level i appears in level i+1 with probability p (typically p = 1/2 or p = 1/4)
3. The header is at level MaxLevel and all its forward pointers initially point to NIL
4. Levels are numbered starting from 1 (the bottom level containing all elements)

The probability that a node at level i has a pointer at level i+1 is p. This means:
- All nodes have a level ≥ 1
- 1/p nodes have level ≥ 2
- 1/p² nodes have level ≥ 3
- And so on...

With p = 1/2, we expect:
- 50% of nodes to be at level 1 only
- 25% of nodes to be at level 2 or higher
- 12.5% of nodes to be at level 3 or higher
- The maximum level is approximately log₂ n with high probability

---

### النسخة العربية

## وصف غير رسمي

في قائمة مرتبطة مرتبة عادية، يتطلب البحث مسح القائمة حتى يتم العثور على العنصر المطلوب أو يتم تحديد أن العنصر غير موجود في القائمة. مع n عنصر، يستغرق هذا زمن O(n). إذا كان لدينا مؤشر إلى كل عنصر آخر، يمكننا تقليل الزمن إلى O(n/2) عن طريق التحقق من العنصر المشار إليه والتخطي للأمام إذا كان أقل من العنصر الذي نبحث عنه.

يمكننا الاستمرار في هذه الفكرة بشكل تكراري. إذا كان لدينا مؤشر إلى كل عنصر 2^i، نحصل على زمن بحث O(n/2^i + 2^i). القيمة المثلى لـ i هي log n، مما يعطي زمن بحث O(log n). المشكلة هي أن إدراج عنصر جديد في مثل هذه البنية سيتطلب إعادة هيكلة القائمة بأكملها.

تحل قوائم التخطي هذه المشكلة من خلال تحديد مستوى كل عنصر بشكل عشوائي عند إدراجه. عنصر من المستوى i لديه i مؤشر أمامي، مفهرسة من 1 إلى i. لا نحتاج إلى تتبع مستويات العناصر؛ يتم تحديد مستوى العنصر من خلال عدد المؤشرات الأمامية التي يمتلكها.

مستوى القائمة هو أقصى مستوى لأي عنصر في القائمة (أو 1 إذا كانت القائمة فارغة). رأس القائمة لديه مؤشرات أمامية في المستويات من 1 إلى المستوى الأقصى للقائمة. المؤشرات الأمامية للرأس في المستويات الأعلى من المستوى الأقصى الحالي للقائمة هي NIL.

## وصف رسمي

قائمة التخطي هي بنية بيانات احتمالية تسمح بزمن متوسط O(log n) للبحث وكذلك إدراج وحذف العناصر. تتكون من تسلسل هرمي من القوائم المرتبطة، مع قائمة المستوى السفلي التي تحتوي على جميع العناصر بترتيب مرتب، وكل مستوى أعلى يحتوي على متسلسلة فرعية أكثر تباعداً من العناصر.

بشكل رسمي، قائمة التخطي لمجموعة S من العناصر تتكون من عقدة رأس ومجموعة من العقد، كل عقدة لديها:
- قيمة مفتاح (باستثناء الرأس)
- مصفوفة forward[1..MaxLevel] من المؤشرات إلى العقد اللاحقة
- مستوى العقدة (أعلى فهرس في forward مع مؤشر غير NIL)

الخصائص:
1. جميع العناصر موجودة في قائمة المستوى 1 بترتيب مرتب
2. كل عنصر في المستوى i يظهر في المستوى i+1 باحتمال p (عادةً p = 1/2 أو p = 1/4)
3. الرأس في المستوى MaxLevel وجميع مؤشراته الأمامية تشير في البداية إلى NIL
4. يتم ترقيم المستويات بدءاً من 1 (المستوى السفلي الذي يحتوي على جميع العناصر)

احتمال أن تمتلك عقدة في المستوى i مؤشراً في المستوى i+1 هو p. هذا يعني:
- جميع العقد لديها مستوى ≥ 1
- 1/p عقدة لديها مستوى ≥ 2
- 1/p² عقدة لديها مستوى ≥ 3
- وهكذا دواليك...

مع p = 1/2، نتوقع:
- 50% من العقد أن تكون في المستوى 1 فقط
- 25% من العقد أن تكون في المستوى 2 أو أعلى
- 12.5% من العقد أن تكون في المستوى 3 أو أعلى
- المستوى الأقصى هو تقريباً log₂ n باحتمال كبير

---

### Translation Notes

- **Key terms introduced:**
  - forward pointer (مؤشر أمامي)
  - header node (عقدة رأس)
  - level (مستوى)
  - MaxLevel (المستوى الأقصى)
  - NIL (NIL - kept in English as standard programming term)
  - probability p (احتمال p)
  - sparse subsequence (متسلسلة فرعية أكثر تباعداً)
  - hierarchy (تسلسل هرمي)
- **Equations:** Multiple complexity notations O(n), O(n/2), O(log n), probability formulas
- **Special handling:**
  - Mathematical notation preserved in both English and Arabic
  - Programming terminology like NIL kept in English as standard
  - Subscript and superscript notation maintained
- **Figures referenced:** Informal description references conceptual list structure

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
