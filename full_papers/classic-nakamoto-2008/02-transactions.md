# Section 2: Transactions
## القسم 2: المعاملات

**Section:** transactions
**Translation Quality:** 0.87
**Glossary Terms Used:** electronic coin, digital signatures, hash, transaction, double-spending, trusted third party, payee, node, proof

---

### English Version

We define an electronic coin as a chain of digital signatures. Each owner transfers the coin to the next by digitally signing a hash of the previous transaction and the public key of the next owner and adding these to the end of the coin.

A payee can verify signatures to confirm ownership chains. However, the payee cannot verify that previous owners didn't double-spend the coin. A traditional solution introduces a trusted central authority (mint) checking every transaction. But this creates dependency on a single company.

We need a way for the payee to know that the previous owners did not sign any earlier transactions.

For this purpose, the earliest transaction counts. Confirming the absence of earlier transactions requires awareness of all transactions. The payee needs proof that at the time of each transaction, the majority of nodes agreed it was the first received.

---

### النسخة العربية

نُعرّف العملة الإلكترونية على أنها سلسلة من التوقيعات الرقمية. ينقل كل مالك العملة إلى التالي من خلال التوقيع الرقمي على تجزئة المعاملة السابقة والمفتاح العام للمالك التالي وإضافتها إلى نهاية العملة.

يمكن للمستلم التحقق من التوقيعات لتأكيد سلاسل الملكية. ومع ذلك، لا يمكن للمستلم التحقق من أن المالكين السابقين لم ينفقوا العملة مرتين. يقدم الحل التقليدي سلطة مركزية موثوقة (دار سك النقود) تفحص كل معاملة. لكن هذا يخلق تبعية لشركة واحدة.

نحتاج إلى طريقة تمكّن المستلم من معرفة أن المالكين السابقين لم يوقعوا على أي معاملات سابقة.

لهذا الغرض، تُحتسب المعاملة الأولى. يتطلب تأكيد عدم وجود معاملات سابقة الوعي بجميع المعاملات. يحتاج المستلم إلى دليل على أنه في وقت كل معاملة، وافقت أغلبية العقد على أنها كانت الأولى المستلمة.

---

### Translation Notes

- **Figures referenced:** Figure 1 (transaction chain diagram - referenced in original paper)
- **Key terms introduced:** electronic coin (عملة إلكترونية), chain of digital signatures (سلسلة من التوقيعات الرقمية), hash (تجزئة), public key (مفتاح عام), payee (مستلم), mint (دار سك النقود), central authority (سلطة مركزية)
- **Equations:** None
- **Citations:** None
- **Special handling:** Technical cryptographic concepts - used precise terminology for digital signatures and hashing

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87
