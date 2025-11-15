# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.91
**Glossary Terms Used:** polyhedral model, compiler, code generation, optimization, loop transformation, data layout, multicore, GPU, distributed system, image processing, deep learning, linear algebra, scheduling language, intermediate representation

---

### English Version

This paper introduces TIRAMISU, a polyhedral framework designed to generate high performance code for multiple platforms including multicores, GPUs, and distributed machines. TIRAMISU introduces a scheduling language with novel extensions to explicitly manage the complexities that arise when targeting these systems. The framework is designed for the areas of image processing, stencils, linear algebra and deep learning. TIRAMISU has two main features: it relies on a flexible representation based on the polyhedral model and it has a rich scheduling language allowing fine-grained control of optimizations. TIRAMISU uses a four-level intermediate representation that allows full separation between the algorithms, loop transformations, data layouts, and communication. This separation simplifies targeting multiple hardware architectures with the same algorithm. We evaluate TIRAMISU by writing a set of image processing, deep learning, and linear algebra benchmarks and compare them with state-of-the-art compilers and hand-tuned libraries. We show that TIRAMISU matches or outperforms existing compilers and libraries on different hardware architectures, including multicore CPUs, GPUs, and distributed machines.

---

### النسخة العربية

تقدم هذه الورقة Tiramisu، وهو إطار عمل متعدد السطوح مصمم لتوليد شفرة عالية الأداء لمنصات متعددة بما في ذلك الأنظمة متعددة الأنوية، ووحدات معالجة الرسومات، والآلات الموزعة. يقدم Tiramisu لغة جدولة مع امتدادات جديدة لإدارة التعقيدات التي تنشأ عند استهداف هذه الأنظمة بشكل صريح. تم تصميم الإطار لمجالات معالجة الصور، والقوالب، والجبر الخطي، والتعلم العميق. لدى Tiramisu ميزتان رئيسيتان: يعتمد على تمثيل مرن قائم على النموذج متعدد السطوح ولديه لغة جدولة غنية تسمح بالتحكم الدقيق في التحسينات. يستخدم Tiramisu تمثيلاً وسيطاً من أربعة مستويات يسمح بالفصل الكامل بين الخوارزميات، وتحويلات الحلقات، وتخطيطات البيانات، والاتصال. يبسط هذا الفصل استهداف معماريات أجهزة متعددة بنفس الخوارزمية. نقيّم Tiramisu من خلال كتابة مجموعة من معايير معالجة الصور، والتعلم العميق، والجبر الخطي ومقارنتها بالمترجمات الحديثة والمكتبات المضبوطة يدوياً. نوضح أن Tiramisu يطابق أو يتفوق على المترجمات والمكتبات الموجودة على معماريات أجهزة مختلفة، بما في ذلك وحدات المعالجة المركزية متعددة الأنوية، ووحدات معالجة الرسومات، والآلات الموزعة.

---

### Translation Notes

- **Figures referenced:** Figure 1 (in abstract context on page 1)
- **Key terms introduced:** Tiramisu, polyhedral framework, scheduling language, four-level IR
- **Equations:** 0
- **Citations:** 0 (in abstract itself)
- **Special handling:** None

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.93
- Readability: 0.90
- Glossary consistency: 0.90
- **Overall section score:** 0.91
