# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.88
**Glossary Terms Used:** computation-enabled object storage, query offloading, columnar storage, aggregate, sort, filter, HPC, performance

---

### English Version

Computation-Enabled Object Storage (COS) systems, such as MinIO and Ceph, have recently emerged as promising storage solutions for post hoc, SQL-based analysis on large-scale datasets in High-Performance Computing (HPC) environments. By supporting object-granular layouts, COS facilitates column-oriented access and supports in-storage execution of data reduction operators, such as filters, close to where the data resides. Despite growing interest and adoption, existing COS systems exhibit several fundamental limitations that hinder their effectiveness. First, they impose rigid constraints on output data formats, limiting flexibility and interoperability. Second, they support offloading for only a narrow set of operators and expressions, restricting their applicability to more complex analytical tasks. Third–and perhaps most critically–they fail to incorporate design strategies that enable compute offloading optimized for the characteristics of deep storage hierarchies.

To address these challenges, this paper proposes OASIS, a novel COS system that features: (i) flexible and interoperable output delivery through diverse formats, including columnar layouts such as Arrow; (ii) broad support for complex operators (e.g., aggregate, sort) and array-aware expressions, including element-wise predicates over array structures; and (iii) dynamic selection of optimal execution paths across internal storage layers, guided by operator characteristics and data movement costs.

We implemented a prototype of OASIS and integrated it into the Spark analytics framework. Through extensive evaluation using real-world scientific queries from HPC workflows, OASIS achieves up to a 32.7% performance improvement over Spark configured with existing COS-based storage systems.

---

### النسخة العربية

أنظمة تخزين الكائنات الممكّنة حسابياً (COS)، مثل MinIO و Ceph، ظهرت مؤخراً كحلول تخزين واعدة للتحليل اللاحق القائم على SQL على مجموعات البيانات واسعة النطاق في بيئات الحوسبة عالية الأداء (HPC). من خلال دعم التخطيطات الدقيقة للكائنات، يُسهّل COS الوصول الموجه نحو الأعمدة ويدعم التنفيذ داخل التخزين لمعاملات تقليل البيانات، مثل المرشحات، بالقرب من مكان تواجد البيانات. على الرغم من الاهتمام والاعتماد المتزايدين، تُظهر أنظمة COS الحالية عدة قيود أساسية تعيق فعاليتها. أولاً، تفرض قيوداً صارمة على تنسيقات بيانات الإخراج، مما يحد من المرونة وقابلية التشغيل البيني. ثانياً، تدعم التفريغ لمجموعة ضيقة فقط من المعاملات والتعبيرات، مما يقيد قابلية تطبيقها على المهام التحليلية الأكثر تعقيداً. ثالثاً - وربما الأهم - تفشل في دمج استراتيجيات التصميم التي تمكّن تفريغ الحساب المحسّن لخصائص التسلسلات الهرمية العميقة للتخزين.

لمعالجة هذه التحديات، يقترح هذا البحث OASIS، وهو نظام COS جديد يتميز بـ: (i) تسليم إخراج مرن وقابل للتشغيل البيني من خلال تنسيقات متنوعة، بما في ذلك التخطيطات العمودية مثل Arrow؛ (ii) دعم واسع للمعاملات المعقدة (مثل التجميع والفرز) والتعبيرات الواعية بالمصفوفات، بما في ذلك المحمولات العنصرية على بنى المصفوفات؛ و(iii) الاختيار الديناميكي لمسارات التنفيذ المثلى عبر طبقات التخزين الداخلية، موجهة بخصائص المعاملات وتكاليف نقل البيانات.

قمنا بتنفيذ نموذج أولي لـ OASIS ودمجه في إطار عمل التحليلات Spark. من خلال التقييم الشامل باستخدام استعلامات علمية حقيقية من سير عمل HPC، يحقق OASIS تحسيناً في الأداء يصل إلى 32.7٪ مقارنة بـ Spark المهيأ مع أنظمة التخزين القائمة على COS الموجودة.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:** COS, OASIS, query offloading, columnar layouts, Arrow, aggregate, sort, array-aware expressions
- **Equations:** None
- **Citations:** None in abstract
- **Special handling:** Technical acronyms (COS, HPC, SQL, MinIO, Ceph) kept in English where appropriate

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
