---
# Organization and Maintenance of Large Ordered Indexes
## تنظيم وصيانة الفهارس الكبيرة المرتبة

**Authors:** Rudolf Bayer, Edward M. McCreight
**Year:** 1972
**Publication:** Acta Informatica, Vol. 1, pp. 173-189, 1972
**DOI:** 10.1007/BF00288683
**Translation Quality:** 0.92
**Glossary Terms Used:** data structure, algorithm, index, storage, performance, optimization

### English Abstract
The paper considers organization and maintenance of an index for a dynamic random access file, where the index must be kept on some pseudo random access backup store like a disc or a drum. The index organization described allows retrieval, insertion, and deletion of keys in time proportional to logkI where I is the size of the index and k is a device dependent natural number such that the performance of the scheme becomes near optimal. Storage utilization is at least 50% but generally much higher, with the pages of the index organized in a special datastructure, so-called B-trees. The scheme is analyzed, performance bounds are obtained, and a near optimal k is computed.

### الملخص العربي
تتناول هذه الورقة تنظيم وصيانة فهرس لملف وصول عشوائي ديناميكي، حيث يجب الاحتفاظ بالفهرس على وسيط تخزين احتياطي شبه عشوائي الوصول مثل قرص أو أسطوانة. يسمح تنظيم الفهرس الموصوف باسترجاع وإدراج وحذف المفاتيح في وقت يتناسب مع logkI حيث I هو حجم الفهرس و k هو رقم طبيعي يعتمد على الجهاز بحيث يصبح أداء المخطط قريباً من الأمثل. يكون استخدام التخزين 50% على الأقل ولكن عموماً أعلى بكثير، مع تنظيم صفحات الفهرس في بنية بيانات خاصة تسمى أشجار B. يتم تحليل المخطط، والحصول على حدود الأداء، وحساب k القريبة من المثلى.

### Back-Translation (Validation)
This paper addresses the organization and maintenance of an index for a dynamic random access file, where the index must be kept on a pseudo-random access backup storage medium like a disc or drum. The described index organization allows retrieval, insertion, and deletion of keys in time proportional to logkI where I is the index size and k is a device-dependent natural number such that the scheme's performance becomes near optimal. Storage utilization is at least 50% but generally much higher, with index pages organized in a special data structure called B-trees. The scheme is analyzed, performance bounds are obtained, and a near-optimal k is computed.

### Translation Metrics
- Iterations: 1
- Final Score: 0.92
- Quality: High
- Key Technical Terms: index (فهرس), dynamic random access file (ملف وصول عشوائي ديناميكي), retrieval (استرجاع), insertion (إدراج), deletion (حذف), storage utilization (استخدام التخزين), data structure (بنية بيانات), B-trees (أشجار B), performance (أداء), optimal (أمثل)

### Historical Significance
B-trees, introduced by Bayer and McCreight in 1972, are one of the most important data structures in computer science. They are the foundation for indexing in virtually all modern database systems (including MySQL, PostgreSQL, Oracle, SQL Server) and file systems (NTFS, HFS+, ext4). The B-tree's ability to maintain sorted data and allow searches, insertions, and deletions in logarithmic time while being optimized for systems that read and write large blocks of data makes it ideal for disk-based storage systems.
---
