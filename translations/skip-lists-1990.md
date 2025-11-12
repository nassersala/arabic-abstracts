---
# Skip Lists: A Probabilistic Alternative to Balanced Trees
## قوائم التخطي: بديل احتمالي للأشجار المتوازنة

**Author:** William Pugh
**Year:** 1990
**Publication:** Communications of the ACM, Vol. 33, No. 6, June 1990, pp. 668-676
**DOI:** 10.1145/78973.78977
**Translation Quality:** 0.94
**Glossary Terms Used:** data structure, algorithm, probabilistic, balanced tree, performance

### English Abstract
Skip lists use probabilistic balancing rather than strictly enforced balancing and as a result the algorithms for insertion and deletion in skip lists are much simpler and significantly faster than equivalent algorithms for balanced trees. Although skip lists have bad worst-case performance, no input sequence consistently produces the worst-case performance (much like quicksort when the pivot element is chosen randomly). Skip lists have balance properties similar to that of search trees built by random insertions, yet do not require insertions to be random. Balancing a data structure probabilistically is easier than explicitly maintaining the balance. For many applications, skip lists are a more natural representation than trees, also leading to simpler algorithms.

### الملخص العربي
تستخدم قوائم التخطي الموازنة الاحتمالية بدلاً من الموازنة المفروضة بصرامة، ونتيجة لذلك فإن خوارزميات الإدراج والحذف في قوائم التخطي أبسط بكثير وأسرع بشكل ملحوظ من الخوارزميات المكافئة للأشجار المتوازنة. على الرغم من أن قوائم التخطي لديها أداء سيء في أسوأ الحالات، لا يوجد تسلسل إدخال ينتج باستمرار أداء أسوأ الحالات (تماماً مثل الترتيب السريع عندما يتم اختيار العنصر المحوري عشوائياً). تتمتع قوائم التخطي بخصائص توازن مشابهة لتلك الخاصة بأشجار البحث المبنية بعمليات إدراج عشوائية، ومع ذلك لا تتطلب أن تكون عمليات الإدراج عشوائية. موازنة بنية البيانات احتمالياً أسهل من الحفاظ على التوازن بشكل صريح. بالنسبة للعديد من التطبيقات، تعد قوائم التخطي تمثيلاً أكثر طبيعية من الأشجار، مما يؤدي أيضاً إلى خوارزميات أبسط.

### Back-Translation (Validation)
Skip lists use probabilistic balancing instead of strictly enforced balancing, and as a result, the algorithms for insertion and deletion in skip lists are much simpler and significantly faster than equivalent algorithms for balanced trees. Although skip lists have poor worst-case performance, no input sequence consistently produces worst-case performance (just like quicksort when the pivot element is chosen randomly). Skip lists have balance properties similar to those of search trees built with random insertions, yet do not require insertions to be random. Balancing a data structure probabilistically is easier than explicitly maintaining balance. For many applications, skip lists are a more natural representation than trees, also leading to simpler algorithms.

### Translation Metrics
- Iterations: 1
- Final Score: 0.94
- Quality: High
- Key Technical Terms: skip lists (قوائم التخطي), probabilistic balancing (موازنة احتمالية), insertion (إدراج), deletion (حذف), balanced trees (أشجار متوازنة), worst-case performance (أداء في أسوأ الحالات), data structure (بنية بيانات), algorithms (خوارزميات), search trees (أشجار بحث)

### Historical Significance
Skip lists, introduced by William Pugh in 1990, provide a simple probabilistic alternative to balanced trees like AVL trees and red-black trees. They are used in many practical systems including Redis (sorted sets), LevelDB, and RocksDB. Their simplicity makes them easier to implement correctly than self-balancing trees, while still providing O(log n) expected time complexity for search, insertion, and deletion operations.
---
