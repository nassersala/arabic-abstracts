# Section 4: Proof-of-Work
## القسم 4: إثبات العمل

**Section:** proof-of-work
**Translation Quality:** 0.86
**Glossary Terms Used:** distributed, timestamp server, peer-to-peer, proof-of-work, hash, SHA-256, nonce, block, chain, CPU, node, difficulty

---

### English Version

To implement a distributed timestamp server on a peer-to-peer basis, we will need to use a proof-of-work system similar to Adam Back's Hashcash.

The proof-of-work involves scanning for a value that when hashed, such as with SHA-256, the hash begins with a number of zero bits.

Average work required grows exponentially with required zero bits and can be verified via single hash execution. Implementation increments a nonce until the block's hash exhibits required zero bits. Once expended, changing the block requires redoing the work.

The proof-of-work also solves the problem of determining representation in majority decision making.

One-IP-address-one-vote is vulnerable to manipulation. Proof-of-work is essentially one-CPU-one-vote. The longest chain represents majority decision, with greatest proof-of-work investment.

To modify a past block, an attacker would have to redo the proof-of-work of the block and all blocks after it and then catch up with and surpass the work of the honest nodes.

Probability of a slower attacker catching up diminishes exponentially as subsequent blocks are added. The proof-of-work difficulty is determined by a moving average targeting an average number of blocks per hour.

---

### النسخة العربية

لتطبيق خادم طوابع زمنية موزع على أساس من نظير إلى نظير، سنحتاج إلى استخدام نظام إثبات العمل مشابه لـ Hashcash الخاص بآدم باك.

يتضمن إثبات العمل البحث عن قيمة عند تجزئتها، كما هو الحال مع SHA-256، تبدأ التجزئة بعدد من البتات الصفرية.

ينمو متوسط العمل المطلوب بشكل أسي مع البتات الصفرية المطلوبة ويمكن التحقق منه عبر تنفيذ تجزئة واحدة. يزيد التنفيذ من قيمة nonce حتى تُظهر تجزئة الكتلة البتات الصفرية المطلوبة. بمجرد إنفاقه، يتطلب تغيير الكتلة إعادة العمل.

يحل إثبات العمل أيضاً مشكلة تحديد التمثيل في اتخاذ القرارات بالأغلبية.

نظام صوت واحد لكل عنوان IP معرض للتلاعب. إثبات العمل هو في الأساس صوت واحد لكل وحدة معالجة مركزية. تمثل السلسلة الأطول قرار الأغلبية، مع أكبر استثمار في إثبات العمل.

لتعديل كتلة سابقة، سيتعين على المهاجم إعادة إثبات العمل للكتلة وجميع الكتل بعدها ثم اللحاق بعمل العقد الأمينة وتجاوزه.

يتضاءل احتمال لحاق مهاجم أبطأ بشكل أسي مع إضافة كتل لاحقة. يتم تحديد صعوبة إثبات العمل بواسطة متوسط متحرك يستهدف متوسط عدد من الكتل في الساعة.

---

### Translation Notes

- **Figures referenced:** None (though original paper has Figure 3 showing proof-of-work chain)
- **Key terms introduced:** Hashcash (هاش كاش - transliteration), SHA-256 (SHA-256 - kept as is), zero bits (بتات صفرية), nonce (nonce - kept as technical term), moving average (متوسط متحرك), one-CPU-one-vote (صوت واحد لكل وحدة معالجة مركزية)
- **Equations:** None in text (formulas appear in original paper)
- **Citations:** Reference to Adam Back's Hashcash
- **Special handling:** Core mining concept - maintained technical precision for cryptographic terms

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.86
