# Section 0: Abstract
## القسم 0: الملخص

**Section:** Abstract
**Translation Quality:** 0.92
**Glossary Terms Used:** dataflow, performance, optimization, heterogeneous, portability, FPGA, GPU, CPU

---

### English Version

The ubiquity of accelerators in high-performance computing has driven programming complexity beyond the skill-set of the average domain scientist. To maintain performance portability in the future, it is imperative to decouple architecture-specific programming paradigms from the underlying scientific computations. We present the Stateful DataFlow multiGraph (SDFG), a data-centric intermediate representation that enables separating program definition from its optimization. By combining fine-grained data dependencies with high-level control-flow, SDFGs are both expressive and amenable to program transformations, such as tiling and double-buffering. These transformations are applied to the SDFG in an interactive process, using extensible pattern matching, graph rewriting, and a graphical user interface. We demonstrate SDFGs on CPUs, GPUs, and FPGAs over various motifs — from fundamental computational kernels to graph analytics. We show that SDFGs deliver competitive performance, allowing domain scientists to develop applications naturally and port them to approach peak hardware performance without modifying the original scientific code.

---

### النسخة العربية

أدت انتشار المسرعات في الحوسبة عالية الأداء إلى دفع تعقيد البرمجة إلى ما يتجاوز مجموعة مهارات عالم المجال المتوسط. للحفاظ على قابلية نقل الأداء في المستقبل، من الضروري فصل نماذج البرمجة الخاصة بالمعمارية عن الحسابات العلمية الأساسية. نقدم الرسوم البيانية المتعددة لتدفق البيانات الحافظة للحالة (SDFG)، وهي تمثيل وسيط محوري للبيانات يتيح فصل تعريف البرنامج عن تحسينه. من خلال دمج اعتماديات البيانات الدقيقة مع تدفق التحكم عالي المستوى، تكون الرسوم البيانية SDFG معبرة وقابلة للتحويلات البرمجية، مثل التبليط والتخزين المؤقت المزدوج. يتم تطبيق هذه التحويلات على SDFG في عملية تفاعلية، باستخدام مطابقة الأنماط القابلة للتوسيع، وإعادة كتابة الرسوم البيانية، وواجهة مستخدم رسومية. نوضح الرسوم البيانية SDFG على وحدات المعالجة المركزية ووحدات معالجة الرسومات ومصفوفات البوابات القابلة للبرمجة عبر أنماط مختلفة - من النوى الحسابية الأساسية إلى تحليلات الرسوم البيانية. نُظهر أن الرسوم البيانية SDFG تقدم أداءً منافسًا، مما يسمح لعلماء المجال بتطوير التطبيقات بشكل طبيعي ونقلها للاقتراب من ذروة أداء الأجهزة دون تعديل الشفرة العلمية الأصلية.

---

### Translation Notes

- **Figures referenced:** Figure 1
- **Key terms introduced:** SDFG, data-centric, performance portability, heterogeneous architectures
- **Equations:** 0
- **Citations:** 0
- **Special handling:** None

### Quality Metrics

- Semantic equivalence: 0.93
- Technical accuracy: 0.92
- Readability: 0.91
- Glossary consistency: 0.92
- **Overall section score:** 0.92
