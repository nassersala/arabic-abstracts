# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** data structure, algorithm, balanced tree, linked list, search, insertion, deletion, complexity, performance

---

### English Version

Search of a sorted linked list requires O(n) time. This can be improved by maintaining additional pointers that skip over some elements in the list. We call such a structure a skip list.

A skip list for a set of elements is a collection of sequences S_0, S_1, ..., S_h, where S_0 is a simple sorted linked list containing all the elements and each sequence S_i contains a subsequence of the elements in S_{i-1}, allowing us to skip over elements during search.

The idea of skip lists is to augment ordered linked lists with additional forward pointers. In a simple linked list, a search for element x starts at the head of the list and examines each element in sequence until x is found or the list is exhausted. If the list is sorted, we can add additional pointers that skip over some elements, creating express lanes that allow us to search faster.

Figure 1 shows a skip list of 7 elements. Each box represents a node. The top row contains only the header node. Below each node in level i is a node in level i-1. A search starts at the header node in the top level and proceeds horizontally until a key greater than or equal to the search key is found. Then the search drops down one level and continues.

Unlike balanced trees, a skip list does not require any global restructuring when elements are inserted or deleted. Instead, the structure of a skip list is determined randomly. When an element is inserted, the level of the node representing that element is chosen randomly, using a simple probabilistic scheme.

The expected search path length is proportional to log n. With high probability, all searches, insertions and deletions can be performed in O(log n) time. Skip lists are simpler to implement than balanced trees and, in practice, are about as fast as highly tuned implementations of balanced tree algorithms.

Skip lists are based on the observation that simple probabilistic balancing schemes are easier to implement and just as efficient as more complex deterministic balancing schemes used in AVL trees, red-black trees, and other balanced tree structures. For applications where consistency of performance is more important than guaranteed worst-case performance, skip lists are an attractive alternative.

---

### النسخة العربية

يتطلب البحث في قائمة مرتبطة مرتبة زمناً من الرتبة O(n). يمكن تحسين ذلك من خلال الحفاظ على مؤشرات إضافية تتخطى بعض العناصر في القائمة. نطلق على مثل هذه البنية اسم قائمة التخطي.

قائمة التخطي لمجموعة من العناصر هي مجموعة من المتسلسلات S_0, S_1, ..., S_h، حيث S_0 هي قائمة مرتبطة مرتبة بسيطة تحتوي على جميع العناصر وكل متسلسلة S_i تحتوي على متسلسلة فرعية من العناصر في S_{i-1}، مما يسمح لنا بتخطي العناصر أثناء البحث.

فكرة قوائم التخطي هي تعزيز القوائم المرتبطة المرتبة بمؤشرات أمامية إضافية. في قائمة مرتبطة بسيطة، يبدأ البحث عن العنصر x من رأس القائمة ويفحص كل عنصر بالتسلسل حتى يتم العثور على x أو تنفد القائمة. إذا كانت القائمة مرتبة، يمكننا إضافة مؤشرات إضافية تتخطى بعض العناصر، مما ينشئ مسارات سريعة تسمح لنا بالبحث بشكل أسرع.

يوضح الشكل 1 قائمة تخطي مكونة من 7 عناصر. كل صندوق يمثل عقدة. يحتوي الصف العلوي فقط على عقدة الرأس. أسفل كل عقدة في المستوى i توجد عقدة في المستوى i-1. يبدأ البحث عند عقدة الرأس في المستوى الأعلى ويتقدم أفقياً حتى يتم العثور على مفتاح أكبر من أو يساوي مفتاح البحث. ثم ينخفض البحث مستوى واحداً ويستمر.

على عكس الأشجار المتوازنة، لا تتطلب قائمة التخطي أي إعادة هيكلة شاملة عند إدراج العناصر أو حذفها. بدلاً من ذلك، يتم تحديد بنية قائمة التخطي بشكل عشوائي. عند إدراج عنصر، يتم اختيار مستوى العقدة التي تمثل ذلك العنصر بشكل عشوائي، باستخدام مخطط احتمالي بسيط.

طول مسار البحث المتوقع يتناسب مع log n. باحتمال كبير، يمكن إجراء جميع عمليات البحث والإدراج والحذف في زمن O(log n). قوائم التخطي أبسط في التنفيذ من الأشجار المتوازنة، وفي الممارسة العملية، تكون بنفس سرعة التطبيقات عالية الضبط لخوارزميات الأشجار المتوازنة.

تستند قوائم التخطي إلى ملاحظة أن مخططات الموازنة الاحتمالية البسيطة أسهل في التنفيذ وبنفس كفاءة مخططات الموازنة الحتمية الأكثر تعقيداً المستخدمة في أشجار AVL وأشجار الأحمر-الأسود وبنى الأشجار المتوازنة الأخرى. بالنسبة للتطبيقات التي يكون فيها اتساق الأداء أكثر أهمية من ضمان أداء أسوأ الحالات، تعد قوائم التخطي بديلاً جذاباً.

---

### Translation Notes

- **Figures referenced:** Figure 1 (skip list structure with 7 elements)
- **Key terms introduced:**
  - skip list (قائمة التخطي)
  - linked list (قائمة مرتبطة)
  - header node (عقدة الرأس)
  - level (مستوى)
  - express lanes (مسارات سريعة)
  - probabilistic scheme (مخطط احتمالي)
  - AVL trees (أشجار AVL)
  - red-black trees (أشجار الأحمر-الأسود)
- **Equations:** References to O(n), O(log n) complexity
- **Citations:** None in this section
- **Special handling:** Mathematical notation preserved, comparison with balanced trees maintained

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88
