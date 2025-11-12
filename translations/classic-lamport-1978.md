---
# Time, Clocks, and the Ordering of Events in a Distributed System
## الزمن والساعات وترتيب الأحداث في النظام الموزع

**Publication:** Communications of the ACM, 21(7):558-565, July 1978
**Authors:** Leslie Lamport
**Year:** 1978
**Domain:** Distributed Systems
**Translation Quality:** 0.91
**Glossary Terms Used:** distributed system, event, ordering, causality, timestamp, algorithm, mutual exclusion, synchronization, processor, state machine

### English Summary
This paper addresses how to establish a total ordering of events in distributed systems that respects causal relationships. The solution uses timestamps to provide a consistent total ordering aligned with causality. An algorithm for totally ordering events can be used to implement any distributed system, described as a particular sequential state machine implemented with a network of processors. The paper demonstrates the concept through a distributed mutual exclusion algorithm and includes a theorem about real-time clock synchronization. The paper introduced the concept of "logical clocks" (Lamport clocks) for establishing event causality in distributed systems.

### الملخص العربي
يعالج هذا البحث كيفية إنشاء ترتيب كامل للأحداث في الأنظمة الموزعة يحترم العلاقات السببية. يستخدم الحل الطوابع الزمنية لتوفير ترتيب كامل متسق يتماشى مع السببية. يمكن استخدام خوارزمية للترتيب الكامل للأحداث لتطبيق أي نظام موزع، موصوف كآلة حالة تسلسلية معينة منفذة بشبكة من المعالجات. يُظهر البحث المفهوم من خلال خوارزمية الاستبعاد المتبادل الموزعة ويتضمن مبرهنة حول تزامن الساعات في الزمن الحقيقي. قدم البحث مفهوم "الساعات المنطقية" (ساعات لامبورت) لإنشاء السببية بين الأحداث في الأنظمة الموزعة.

### Back-Translation (Validation)
This research addresses how to establish a total ordering of events in distributed systems that respects causal relationships. The solution uses timestamps to provide a consistent total ordering that aligns with causality. An algorithm for total ordering of events can be used to implement any distributed system, described as a specific sequential state machine implemented with a network of processors. The research demonstrates the concept through a distributed mutual exclusion algorithm and includes a theorem about real-time clock synchronization. The research introduced the concept of "logical clocks" (Lamport clocks) to establish causality between events in distributed systems.

### Translation Metrics
- Iterations: 1
- Final Score: 0.91
- Quality: High
---
