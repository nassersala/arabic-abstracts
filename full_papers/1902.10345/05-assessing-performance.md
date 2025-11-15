# Section 5: Assessing Performance Without Transformations
## القسم 5: تقييم الأداء بدون تحويلات

**Section:** Performance Assessment
**Translation Quality:** 0.85
**Glossary Terms Used:** benchmark, Polybench, compiler, optimization, CPU, GPU, FPGA

---

### English Version

To understand how the inherently-concurrent representation of the SDFG creates reasonably performing naïve code, we reimplement and run the Polybench benchmark over SDFGs, without any optimizing transformations. We show that the representation itself exposes enough parallelism to compete with state-of-the-art polyhedral compilers, outperform them on GPUs, and provide the first complete set of placed-and-routed Polybench kernels on an FPGA.

The results are shown in Fig. 13, comparing SDFGs both with general-purpose compilers (green bars), and with pattern-matching and polyhedral compilers (blue bars). On the CPU, we see that for most kernels, the performance of unoptimized SDFGs is closer to that of the polyhedral compilers than to the general-purpose compilers. On the GPU, in most cases SDFGs generate code that outperforms PPCG, a tool specifically designed to transform polyhedral applications to GPUs. We attribute these speedups to avoiding unnecessary array copies due to explicit data dependencies, as well as the inherent parallel construction of the data-centric representation.

---

### النسخة العربية

لفهم كيف ينشئ التمثيل المتزامن بطبيعته لـ SDFG شفرة ساذجة ذات أداء معقول، نعيد تنفيذ وتشغيل معيار Polybench على SDFGs، بدون أي تحويلات تحسين. نُظهر أن التمثيل نفسه يكشف عن توازٍ كافٍ للمنافسة مع المترجمات متعددة الوجوه الحديثة، والتفوق عليها على GPUs، وتوفير المجموعة الكاملة الأولى من نوى Polybench المُوضَّعة والمُوجَّهة على FPGA.

تُظهر النتائج في الشكل 13، مقارنة SDFGs مع كل من المترجمات ذات الأغراض العامة (الأشرطة الخضراء)، والمترجمات متعددة الوجوه ومطابقة الأنماط (الأشرطة الزرقاء). على CPU، نرى أنه بالنسبة لمعظم النوى، فإن أداء SDFGs غير المحسّنة أقرب إلى أداء المترجمات متعددة الوجوه منه إلى المترجمات ذات الأغراض العامة. على GPU، في معظم الحالات تولد SDFGs شفرة تتفوق على PPCG، وهي أداة مصممة خصيصًا لتحويل التطبيقات متعددة الوجوه إلى GPUs. نعزو هذه التسريعات إلى تجنب نسخ المصفوفات غير الضرورية بسبب اعتماديات البيانات الصريحة، بالإضافة إلى البنية المتوازية المتأصلة للتمثيل المحوري للبيانات.

---

### Translation Notes

- **Figures referenced:** Figure 13
- **Key terms introduced:** Polybench, PPCG, polyhedral compilers
- **Equations:** 0
- **Citations:** Polybench, PPCG, polyhedral compiler references
- **Special handling:** Performance comparison data

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.85
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.85
