# Section 8: Implementation
## القسم 8: التنفيذ

**Section:** Implementation
**Translation Quality:** 0.88
**Glossary Terms Used:** implementation, solver, optimization, parallel

---

### English Version

The complete framework presented in this paper is implemented in C++. We use OpenMP to parallelize the local step and we solve the global step in parallel for the x, y and z coordinates by prefactorizing the linear system using sparse Cholesky factorization and performing three times back-substitution in parallel. Dynamic constraints are handled by rank updates and downdates of the linear system. The Eigen library (eigen.tuxfamily.org) is used for dense and sparse linear algebra. We use either the standard simplicial mass discretization or its lumped version to compute the mass matrix without any noticeable difference.

**Timing.** For simulation of medium sized models (<30K constraints and <30K DoFs), 5-10 iterations are usually sufficient. At 1-6ms per iteration, this enables realtime simulation on a MacBook Pro 2.7 GHz Intel Quad-core i7 with 16GB of memory. Statistics on timings and meshes can be found in the accompanying video. Moreover, the accompanying application demonstrates the performance on multiple examples.

---

### النسخة العربية

تم تنفيذ الإطار الكامل المقدم في هذه الورقة بلغة C++. نستخدم OpenMP لتوازي الخطوة المحلية ونحل الخطوة العامة بالتوازي للإحداثيات x و y و z من خلال التحليل المسبق للنظام الخطي باستخدام تحليل تشوليسكي المتناثر وإجراء الاستبدال العكسي ثلاث مرات بالتوازي. يتم التعامل مع القيود الديناميكية من خلال تحديثات الرتبة وانخفاضاتها للنظام الخطي. تُستخدم مكتبة Eigen (eigen.tuxfamily.org) للجبر الخطي الكثيف والمتناثر. نستخدم إما تفصيل الكتلة البسيط القياسي أو نسخته المُجمّعة لحساب مصفوفة الكتلة دون أي فرق ملحوظ.

**التوقيت.** بالنسبة لمحاكاة النماذج متوسطة الحجم (<30K قيد و <30K درجة حرية)، عادة ما تكون 5-10 تكرارات كافية. عند 1-6 ميلي ثانية لكل تكرار، يمكّن هذا من المحاكاة الفورية على MacBook Pro 2.7 GHz Intel Quad-core i7 مع ذاكرة 16GB. يمكن العثور على إحصاءات عن التوقيتات والشبكات في الفيديو المرفق. علاوة على ذلك، يوضح التطبيق المرفق الأداء على أمثلة متعددة.

---

### Translation Notes

- **Libraries:** OpenMP, Eigen
- **Hardware specs:** Kept in English
- **Key terms:** Cholesky factorization (تحليل تشوليسكي), Back-substitution (الاستبدال العكسي), Rank updates (تحديثات الرتبة)

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.89
- **Overall section score:** 0.88
