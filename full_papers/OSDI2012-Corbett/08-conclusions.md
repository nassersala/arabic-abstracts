# Section 8: Conclusions
## القسم 8: الاستنتاجات

**Section:** conclusions
**Translation Quality:** 0.89
**Glossary Terms Used:** scalability (قابلية التوسع), sharding (التجزئة), fault tolerance (تحمل الأخطاء), consistency (الاتساق), replication (النسخ المتماثل), external consistency (الاتساق الخارجي), distributed systems (الأنظمة الموزعة)

---

### English Version

To summarize, Spanner combines and extends on ideas from two research communities: from the database community, a familiar, easy-to-use, semi-relational interface, transactions, and an SQL-based query language; from the systems community, scalability, automatic sharding, fault tolerance, consistent replication, external consistency, and wide-area distribution. Since Spanner's inception, we have taken more than 5 years to iterate to the current design and implementation. Part of this long iteration phase was due to a slow realization that Spanner should do more than tackle the problem of a globally-replicated namespace, and should also focus on database features that Bigtable was missing.

One aspect of our design stands out: the linchpin of Spanner's feature set is TrueTime. We have shown that reifying clock uncertainty in the time API makes it possible to build distributed systems with much stronger time semantics. In addition, as the underlying system enforces tighter bounds on clock uncertainty, the overhead of the stronger semantics decreases. As a community, we should no longer depend on loosely synchronized clocks and weak time APIs in designing distributed algorithms.

---

### النسخة العربية

للتلخيص، تجمع سبانر وتوسع الأفكار من مجتمعي بحث: من مجتمع قواعد البيانات، واجهة شبه علائقية مألوفة وسهلة الاستخدام، ومعاملات، ولغة استعلام قائمة على SQL؛ من مجتمع الأنظمة، قابلية التوسع، والتجزئة التلقائية، وتحمل الأخطاء، والنسخ المتماثل المتسق، والاتساق الخارجي، والتوزيع واسع النطاق. منذ بداية سبانر، استغرق الأمر أكثر من 5 سنوات للتكرار إلى التصميم والتنفيذ الحاليين. كان جزء من هذه المرحلة الطويلة من التكرار بسبب الإدراك البطيء بأن سبانر يجب أن تفعل أكثر من مجرد معالجة مشكلة فضاء الأسماء المنسوخ عالمياً، ويجب أن تركز أيضاً على ميزات قاعدة البيانات التي كانت مفقودة في Bigtable.

جانب واحد من تصميمنا يبرز: حجر الزاوية في مجموعة ميزات سبانر هو TrueTime. لقد أظهرنا أن تجسيد عدم اليقين في الساعة في واجهة برمجة تطبيقات الوقت يجعل من الممكن بناء أنظمة موزعة بدلالات وقت أقوى بكثير. بالإضافة إلى ذلك، مع فرض النظام الأساسي حدوداً أكثر إحكاماً على عدم اليقين في الساعة، ينخفض الحمل الزائد للدلالات الأقوى. كمجتمع، يجب ألا نعتمد بعد الآن على الساعات المتزامنة بشكل فضفاض وواجهات برمجة تطبيقات الوقت الضعيفة في تصميم الخوارزميات الموزعة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Linchpin (حجر الزاوية)
  - Reifying (تجسيد)
  - Time semantics (دلالات الوقت)
  - Wide-area distribution (التوزيع واسع النطاق)
  - Globally-replicated namespace (فضاء الأسماء المنسوخ عالمياً)
- **Equations:** 0
- **Citations:** None
- **Special handling:**
  - Emphasizes TrueTime as the key innovation
  - Highlights combination of database and systems communities' contributions
  - Product names kept: Bigtable

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.93
- Readability: 0.88
- Glossary consistency: 0.95
- **Overall section score:** 0.89
