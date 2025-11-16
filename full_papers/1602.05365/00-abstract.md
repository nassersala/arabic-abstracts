# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.87
**Glossary Terms Used:** transactional memory, concurrent, composable, atomicity, isolation, opacity

---

### English Version

Transactional memory (TM) has emerged as a promising abstraction for concurrent programming alternative to lock-based synchronizations. However, most TM models admit only isolated transactions, which are not adequate in multi-threaded programming where transactions have to interact via shared data before committing. In this paper, we present Open Transactional Memory (OTM), a programming abstraction supporting safe, data-driven interactions between composable memory transactions. This is achieved by relaxing isolation between transactions, still ensuring atomicity: threads of different transactions can interact by accessing shared variables, but then their transactions have to commit together—actually, these transactions are transparently merged. This model allows for loosely-coupled interactions since transaction merging is driven only by accesses to shared data, with no need to specify participants beforehand. In this paper we provide a specification of the OTM in the setting of Concurrent Haskell, showing that it is a conservative extension of current STM abstraction. In particular, we provide a formal semantics, which allows us to prove that OTM satisfies the opacity criterion.

---

### النسخة العربية

ظهرت ذاكرة المعاملات (TM) كتجريد واعد للبرمجة المتزامنة بديلاً عن المزامنات المعتمدة على الأقفال. ومع ذلك، تقبل معظم نماذج ذاكرة المعاملات معاملات معزولة فقط، والتي ليست كافية في البرمجة متعددة الخيوط حيث يجب أن تتفاعل المعاملات عبر البيانات المشتركة قبل الالتزام. في هذا البحث، نقدم ذاكرة المعاملات المفتوحة (OTM)، وهو تجريد برمجي يدعم التفاعلات الآمنة والمدفوعة بالبيانات بين معاملات الذاكرة القابلة للتركيب. يتحقق ذلك من خلال تخفيف العزل بين المعاملات، مع الاستمرار في ضمان الذرية: يمكن للخيوط من معاملات مختلفة التفاعل عن طريق الوصول إلى المتغيرات المشتركة، ولكن بعد ذلك يجب أن تلتزم معاملاتها معاً - في الواقع، يتم دمج هذه المعاملات بشفافية. يتيح هذا النموذج التفاعلات ضعيفة الاقتران حيث يتم دفع دمج المعاملات فقط من خلال الوصول إلى البيانات المشتركة، دون الحاجة إلى تحديد المشاركين مسبقاً. في هذا البحث نقدم مواصفة لذاكرة المعاملات المفتوحة في إطار Haskell المتزامن، موضحين أنها امتداد محافظ لتجريد ذاكرة المعاملات البرمجية (STM) الحالي. بشكل خاص، نقدم دلالات رسمية تسمح لنا بإثبات أن ذاكرة المعاملات المفتوحة تحقق معيار العتامة.

---

### Translation Notes

- **Key concepts introduced:**
  - Open Transactional Memory (OTM) → ذاكرة المعاملات المفتوحة
  - Software Transactional Memory (STM) → ذاكرة المعاملات البرمجية
  - Opacity → العتامة
  - Transaction merging → دمج المعاملات
  - Loosely-coupled interactions → التفاعلات ضعيفة الاقتران

- **Technical accuracy:** The translation maintains the core technical concepts of TM, OTM, atomicity, and isolation while explaining how OTM differs from traditional STM.

- **Citations:** None in abstract

- **Special handling:** Preserved acronyms (TM, OTM, STM) with Arabic translations provided

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
