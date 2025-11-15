# Abstract
## الملخص

**Section:** abstract
**Translation Quality:** 0.93
**Glossary Terms Used:** hash coding, data structure, algorithm, space, time complexity, trade-offs, membership, error frequency

---

### English Version

In this paper trade-offs among certain computational factors in hash coding are analyzed. The paradigm problem considered is that of testing a series of messages one-by-one for membership in a given set of messages. Two new hash-coding methods are examined and compared with a particular conventional hash-coding method. The computational factors considered are the size of the hash area (space), the time required to identify a message as a nonmember of the given set (reject time), and an allowable error frequency. Analysis of the paradigm problem demonstrates that allowing a small number of test messages to be falsely identified as members of the given set will permit a much smaller hash area to be used without increasing reject time.

---

### النسخة العربية

تحلل هذه الورقة المقايضات بين عوامل حسابية معينة في ترميز التجزئة. المشكلة النموذجية المعتبرة هي اختبار سلسلة من الرسائل واحدة تلو الأخرى للعضوية في مجموعة معينة من الرسائل. يتم فحص طريقتين جديدتين لترميز التجزئة ومقارنتهما بطريقة تقليدية معينة لترميز التجزئة. العوامل الحسابية المعتبرة هي حجم منطقة التجزئة (المساحة)، والوقت المطلوب لتحديد رسالة كغير عضو في المجموعة المعطاة (وقت الرفض)، ومعدل الخطأ المسموح به. يُظهر تحليل المشكلة النموذجية أن السماح بتحديد عدد صغير من رسائل الاختبار بشكل خاطئ كأعضاء في المجموعة المعطاة سيسمح باستخدام منطقة تجزئة أصغر بكثير دون زيادة وقت الرفض.

---

### Translation Notes

- **Key terms introduced:** hash coding (ترميز التجزئة), trade-offs (مقايضات), computational factors (عوامل حسابية), membership testing (اختبار العضوية), hash area (منطقة التجزئة), reject time (وقت الرفض), error frequency (معدل الخطأ), false positives (إيجابيات كاذبة)
- **Mathematical concepts:** Space-time trade-offs, probabilistic error rates
- **Special handling:** The abstract introduces the key innovation - accepting false positives to achieve better space efficiency

### Quality Metrics

- Semantic equivalence: 0.94
- Technical accuracy: 0.95
- Readability: 0.92
- Glossary consistency: 0.91
- **Overall section score:** 0.93
