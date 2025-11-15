# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.92
**Glossary Terms Used:** index, dynamic random access file, retrieval, insertion, deletion, storage utilization, data structure, B-trees, performance, optimal

---

### English Version

The paper considers organization and maintenance of an index for a dynamic random access file, where the index must be kept on some pseudo random access backup store like a disc or a drum. The index organization described allows retrieval, insertion, and deletion of keys in time proportional to logkI where I is the size of the index and k is a device dependent natural number such that the performance of the scheme becomes near optimal. Storage utilization is at least 50% but generally much higher, with the pages of the index organized in a special datastructure, so-called B-trees. The scheme is analyzed, performance bounds are obtained, and a near optimal k is computed.

---

### النسخة العربية

تتناول هذه الورقة تنظيم وصيانة فهرس لملف وصول عشوائي ديناميكي، حيث يجب الاحتفاظ بالفهرس على وسيط تخزين احتياطي شبه عشوائي الوصول مثل قرص أو أسطوانة. يسمح تنظيم الفهرس الموصوف باسترجاع وإدراج وحذف المفاتيح في وقت يتناسب مع logkI حيث I هو حجم الفهرس و k هو رقم طبيعي يعتمد على الجهاز بحيث يصبح أداء المخطط قريباً من الأمثل. يكون استخدام التخزين 50% على الأقل ولكن عموماً أعلى بكثير، مع تنظيم صفحات الفهرس في بنية بيانات خاصة تسمى أشجار B. يتم تحليل المخطط، والحصول على حدود الأداء، وحساب k القريبة من المثلى.

---

### Translation Notes

- **Key terms introduced:** B-tree (شجرة B), index (فهرس), dynamic random access file (ملف وصول عشوائي ديناميكي), storage utilization (استخدام التخزين)
- **Mathematical notation:** logkI preserved as-is
- **Historical context:** This abstract introduces the fundamental B-tree data structure

### Quality Metrics

- Semantic equivalence: 0.94
- Technical accuracy: 0.93
- Readability: 0.91
- Glossary consistency: 0.90
- **Overall section score:** 0.92
