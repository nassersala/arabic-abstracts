# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.91
**Glossary Terms Used:** distributed system, event, ordering, causality, timestamp, algorithm, mutual exclusion, synchronization, processor, state machine

---

### English Version

The concept of one event happening before another in a distributed system is examined, and is shown to define a partial ordering of the events. A distributed algorithm is given for synchronizing a system of logical clocks which can be used to totally order the events. The use of the total ordering is illustrated with a method for solving synchronization problems. The algorithm is then specialized for synchronizing physical clocks, and a bound is derived on how far out of synchrony the clocks can become.

---

### النسخة العربية

يعالج هذا البحث مفهوم حدوث حدث ما قبل آخر في نظام موزع، ويُظهر أن هذا المفهوم يُعرِّف ترتيباً جزئياً للأحداث. يُقدَّم خوارزمية موزعة لتزامن نظام من الساعات المنطقية التي يمكن استخدامها لإنشاء ترتيب كامل للأحداث. يُوضَّح استخدام الترتيب الكامل من خلال طريقة لحل مسائل التزامن. ثم تُخصَّص الخوارزمية لتزامن الساعات الفيزيائية، ويُشتَق حد أعلى لمقدار عدم التزامن الذي يمكن أن تصل إليه الساعات.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:** partial ordering, logical clocks, total ordering, physical clocks, synchronization
- **Equations:** 0
- **Citations:** 0
- **Special handling:** Core distributed systems terminology preserved

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.91
- Readability: 0.90
- Glossary consistency: 0.91
- **Overall section score:** 0.91
