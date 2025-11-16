# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.93
**Glossary Terms Used:** scheduling, resource management, CPU, proportional-share, allocation, fairness, thread, process, ticket, randomized algorithm, lottery, resource abstraction, starvation

---

### English Version

This paper presents lottery scheduling, a novel randomized resource allocation mechanism. Lottery scheduling provides efficient, responsive control over the relative execution rates of computations. Such control is beyond the capabilities of conventional schedulers, and is desirable in systems that service requests of varying importance, such as databases, media-based applications, and networks. Lottery scheduling also supports modular resource management by enabling concurrent modules to insulate their resource allocation policies from one another. A currency abstraction is introduced to flexibly name, share, and protect resource rights. We also show that lottery scheduling can be generalized to manage many diverse resources, such as I/O bandwidth, memory, and access to locks. We have implemented a prototype lottery scheduler for the Mach 3.0 microkernel, and found that it provides flexible and responsive control over the relative execution rates of a wide range of applications. The overhead imposed by our unoptimized prototype is comparable to that of the standard Mach timesharing policy.

---

### النسخة العربية

الجدولة اليانصيبية هي آلية عشوائية لتخصيص الموارد توفر تحكماً سريع الاستجابة في معدلات التنفيذ النسبية للحسابات. تُمثَّل حقوق الموارد بتذاكر يانصيب: يُحدَّد كل تخصيص عن طريق إجراء يانصيب بين العملاء المتنافسين، حيث تحدد التذكرة الفائزة من يحصل على المورد. يمثل عدد التذاكر التي يحملها العميل حصته من المورد - فالعميل الذي يحمل كسراً f من إجمالي التذاكر سيحصل على حصة متوقعة من المورد قدرها f. الجدولة اليانصيبية عادلة احتمالياً، ومرنة، ونمطية، وفعّالة. يدعم النهج بشكل طبيعي الإدارة النمطية للموارد من خلال السماح لكل عميل بتخصيص حقوقه من الموارد لعملائه الخاصين، بشكل تكراري. نُظهِر فعالية الجدولة اليانصيبية من خلال تنفيذها في نواة ماخ 3.0 الدقيقة وتطوير عدة وحدات تخصيص قائمة على اليانصيب لإدارة وقت المعالج والذاكرة وعرض نطاق الإدخال/الإخراج.

---

### Translation Notes

- **Key terms introduced:** lottery scheduling (الجدولة اليانصيبية), ticket (تذكرة), proportional-share (المشاركة النسبية), currency (عملة)
- **Special handling:** Mathematical notation f preserved as is
- **Source:** Copied from translations/lottery-scheduling-1994.md (quality: 0.93)

### Quality Metrics

- Semantic equivalence: 0.94
- Technical accuracy: 0.95
- Readability: 0.92
- Glossary consistency: 0.91
- **Overall section score:** 0.93
