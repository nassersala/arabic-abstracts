---
# Space/Time Trade-offs in Hash Coding with Allowable Errors
## مقايضات المساحة/الوقت في ترميز التجزئة مع الأخطاء المسموحة

**Author:** Burton H. Bloom
**Year:** 1970
**Publication:** Communications of the ACM, Vol. 13, No. 7, July 1970, pp. 422-426
**DOI:** 10.1145/362686.362692
**Translation Quality:** 0.93
**Glossary Terms Used:** hash, data structure, algorithm, space, time complexity

### English Abstract
In this paper trade-offs among certain computational factors in hash coding are analyzed. The paradigm problem considered is that of testing a series of messages one-by-one for membership in a given set of messages. Two new hash-coding methods are examined and compared with a particular conventional hash-coding method. The computational factors considered are the size of the hash area (space), the time required to identify a message as a nonmember of the given set (reject time), and an allowable error frequency. Analysis of the paradigm problem demonstrates that allowing a small number of test messages to be falsely identified as members of the given set will permit a much smaller hash area to be used without increasing reject time.

### الملخص العربي
تحلل هذه الورقة المقايضات بين عوامل حسابية معينة في ترميز التجزئة. المشكلة النموذجية المعتبرة هي اختبار سلسلة من الرسائل واحدة تلو الأخرى للعضوية في مجموعة معينة من الرسائل. يتم فحص طريقتين جديدتين لترميز التجزئة ومقارنتهما بطريقة تقليدية معينة لترميز التجزئة. العوامل الحسابية المعتبرة هي حجم منطقة التجزئة (المساحة)، والوقت المطلوب لتحديد رسالة كغير عضو في المجموعة المعطاة (وقت الرفض)، ومعدل الخطأ المسموح به. يُظهر تحليل المشكلة النموذجية أن السماح بتحديد عدد صغير من رسائل الاختبار بشكل خاطئ كأعضاء في المجموعة المعطاة سيسمح باستخدام منطقة تجزئة أصغر بكثير دون زيادة وقت الرفض.

### Back-Translation (Validation)
This paper analyzes the trade-offs between certain computational factors in hash coding. The paradigm problem considered is testing a series of messages one by one for membership in a given set of messages. Two new hash coding methods are examined and compared with a particular conventional hash coding method. The computational factors considered are the size of the hash area (space), the time required to identify a message as a non-member of the given set (reject time), and the allowable error rate. Analysis of the paradigm problem shows that allowing a small number of test messages to be incorrectly identified as members of the given set will allow a much smaller hash area to be used without increasing reject time.

### Translation Metrics
- Iterations: 1
- Final Score: 0.93
- Quality: High
- Key Technical Terms: hash coding (ترميز التجزئة), trade-offs (مقايضات), computational factors (عوامل حسابية), membership (العضوية), hash area (منطقة التجزئة), space (المساحة), reject time (وقت الرفض), error frequency (معدل الخطأ), false positives (إيجابيات كاذبة)

### Historical Significance
The Bloom filter, introduced by Burton Bloom in 1970, is a space-efficient probabilistic data structure used to test whether an element is a member of a set. It can have false positives but never false negatives, making it perfect for many applications where approximate membership queries are acceptable. Bloom filters are widely used in databases (to avoid expensive disk lookups), web caching, network routers, blockchain systems, and many other applications where memory efficiency is critical. This paper has been cited thousands of times and remains highly relevant over 50 years after publication.
---
