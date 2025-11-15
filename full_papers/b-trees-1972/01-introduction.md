# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** index, database, storage, performance, data structure, algorithm, disk, random access, sequential access, optimization

---

### English Version

The problem of organizing and maintaining an index for a dynamic random access file has received considerable attention in recent years. In many applications, the data is stored on secondary storage devices such as disks or drums, which have significantly different access characteristics compared to main memory. While main memory allows truly random access to any location in constant time, secondary storage devices require mechanical movements (such as disk seeks and rotational delays) that make access time highly dependent on the physical location of the data.

A common approach to organizing data on secondary storage is to divide it into pages or blocks, which match the natural unit of data transfer for these devices. Reading or writing a single byte from disk has essentially the same cost as reading or writing an entire page. This characteristic fundamentally changes the economics of data structure design: structures that minimize the number of page accesses are far more important than those that minimize the total number of comparisons.

Traditional data structures such as binary search trees, while excellent for main memory applications, perform poorly when implemented on secondary storage. A binary search tree of height h requires h page accesses in the worst case to search for a key. For a tree with n keys, the height h could be as large as n in the worst case (for a degenerate tree) or log₂n in the best case (for a balanced tree). Even the balanced case is problematic: for a file with one million keys, a balanced binary tree would require approximately 20 disk accesses for a single search operation.

The fundamental problem is that binary trees have a very high branching factor relative to page size. Each internal node has at most two children, which means the tree is very "tall" relative to the number of keys it contains. Since each level of the tree potentially requires a separate disk access, minimizing tree height is crucial for good performance on secondary storage.

Several approaches have been proposed to address this problem:

1. **AVL trees and Red-Black trees**: These balanced binary trees guarantee O(log n) height, but still suffer from the problem of requiring many disk accesses due to their binary branching.

2. **B(h) trees**: Earlier work introduced the concept of trees with higher branching factors, but lacked systematic methods for maintaining balance during insertions and deletions.

3. **Index sequential files**: These structures maintain an index at multiple levels, but typically do not support efficient arbitrary insertions and deletions. Periodic reorganization of the entire file is often required.

This paper introduces a new data structure called B-trees (the "B" stands for "balanced") that addresses these limitations. The key innovations of B-trees are:

1. **High branching factor**: Each node can contain many keys (typically hundreds), dramatically reducing tree height.

2. **Dynamic balancing**: The tree remains balanced automatically during insertions and deletions, without requiring periodic reorganization.

3. **Guaranteed performance**: All searches, insertions, and deletions require at most logₖn page accesses, where k is the branching factor and n is the number of keys.

4. **Excellent storage utilization**: Pages are guaranteed to be at least 50% full, and typically much higher in practice.

By organizing pages in this structure, we can maintain a large ordered index with guaranteed logarithmic performance for all operations, making B-trees ideal for database systems and file systems that must manage large amounts of data on secondary storage.

---

### النسخة العربية

لقد حظيت مشكلة تنظيم وصيانة فهرس لملف وصول عشوائي ديناميكي باهتمام كبير في السنوات الأخيرة. في العديد من التطبيقات، يتم تخزين البيانات على أجهزة تخزين ثانوية مثل الأقراص أو الأسطوانات، والتي لها خصائص وصول مختلفة بشكل كبير مقارنة بالذاكرة الرئيسية. بينما تسمح الذاكرة الرئيسية بالوصول العشوائي الحقيقي إلى أي موقع في وقت ثابت، تتطلب أجهزة التخزين الثانوية حركات ميكانيكية (مثل حركات البحث في القرص والتأخيرات الدورانية) التي تجعل وقت الوصول يعتمد بشكل كبير على الموقع الفعلي للبيانات.

النهج الشائع لتنظيم البيانات على التخزين الثانوي هو تقسيمها إلى صفحات أو كتل، والتي تتطابق مع الوحدة الطبيعية لنقل البيانات لهذه الأجهزة. قراءة أو كتابة بايت واحد من القرص لها في الأساس نفس التكلفة مثل قراءة أو كتابة صفحة كاملة. هذه الخاصية تغير بشكل جوهري اقتصاديات تصميم بنية البيانات: البنى التي تقلل من عدد الوصولات للصفحات هي أكثر أهمية بكثير من تلك التي تقلل من العدد الإجمالي للمقارنات.

بنى البيانات التقليدية مثل أشجار البحث الثنائي، على الرغم من كونها ممتازة لتطبيقات الذاكرة الرئيسية، فإنها تعمل بشكل سيئ عند تنفيذها على التخزين الثانوي. تتطلب شجرة البحث الثنائي ذات الارتفاع h عدد h من الوصولات للصفحات في أسوأ الحالات للبحث عن مفتاح. بالنسبة لشجرة تحتوي على n مفتاح، يمكن أن يكون الارتفاع h كبيراً بقدر n في أسوأ الحالات (لشجرة منحطة) أو log₂n في أفضل الحالات (لشجرة متوازنة). حتى الحالة المتوازنة تشكل مشكلة: بالنسبة لملف يحتوي على مليون مفتاح، ستتطلب شجرة ثنائية متوازنة حوالي 20 وصولاً للقرص لعملية بحث واحدة.

المشكلة الأساسية هي أن الأشجار الثنائية لها عامل تفرع عالٍ جداً بالنسبة لحجم الصفحة. كل عقدة داخلية لها على الأكثر طفلين، مما يعني أن الشجرة "طويلة" جداً بالنسبة لعدد المفاتيح التي تحتوي عليها. نظراً لأن كل مستوى من الشجرة يحتمل أن يتطلب وصولاً منفصلاً للقرص، فإن تقليل ارتفاع الشجرة أمر حاسم للأداء الجيد على التخزين الثانوي.

تم اقتراح عدة نهج لمعالجة هذه المشكلة:

1. **أشجار AVL والأشجار الحمراء-السوداء**: هذه الأشجار الثنائية المتوازنة تضمن ارتفاعاً O(log n)، لكنها لا تزال تعاني من مشكلة الحاجة إلى العديد من الوصولات للقرص بسبب تفرعها الثنائي.

2. **أشجار B(h)**: الأعمال السابقة قدمت مفهوم الأشجار ذات عوامل التفرع الأعلى، لكنها تفتقر إلى الطرق المنهجية للحفاظ على التوازن أثناء الإدراج والحذف.

3. **الملفات المفهرسة المتسلسلة**: هذه البنى تحتفظ بفهرس على مستويات متعددة، لكنها عادة لا تدعم عمليات الإدراج والحذف التعسفية الفعالة. غالباً ما تكون هناك حاجة لإعادة تنظيم دورية للملف بأكمله.

تقدم هذه الورقة بنية بيانات جديدة تسمى أشجار B (حرف "B" يرمز إلى "balanced" أي متوازن) والتي تعالج هذه القيود. الابتكارات الرئيسية لأشجار B هي:

1. **عامل تفرع عالي**: يمكن أن تحتوي كل عقدة على العديد من المفاتيح (عادة مئات)، مما يقلل بشكل كبير من ارتفاع الشجرة.

2. **التوازن الديناميكي**: تبقى الشجرة متوازنة تلقائياً أثناء عمليات الإدراج والحذف، دون الحاجة إلى إعادة تنظيم دورية.

3. **أداء مضمون**: تتطلب جميع عمليات البحث والإدراج والحذف على الأكثر logₖn وصولاً للصفحات، حيث k هو عامل التفرع و n هو عدد المفاتيح.

4. **استخدام ممتاز للتخزين**: الصفحات مضمونة أن تكون ممتلئة بنسبة 50% على الأقل، وعادة أعلى بكثير في الممارسة العملية.

من خلال تنظيم الصفحات في هذه البنية، يمكننا الحفاظ على فهرس كبير مرتب مع أداء لوغاريتمي مضمون لجميع العمليات، مما يجعل أشجار B مثالية لأنظمة قواعد البيانات وأنظمة الملفات التي يجب أن تدير كميات كبيرة من البيانات على التخزين الثانوي.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:** B-tree (شجرة B), branching factor (عامل التفرع), page (صفحة), secondary storage (تخزين ثانوي), balanced tree (شجرة متوازنة), AVL trees (أشجار AVL), Red-Black trees (الأشجار الحمراء-السوداء)
- **Equations:** O(log n), logₖn, log₂n
- **Citations:** General references to prior work
- **Special handling:** Mathematical notation preserved, tree names kept in English/transliterated

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
