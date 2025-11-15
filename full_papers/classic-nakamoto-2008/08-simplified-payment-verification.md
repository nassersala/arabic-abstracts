# Section 8: Simplified Payment Verification
## القسم 8: التحقق المبسط من الدفع

**Section:** simplified-payment-verification
**Translation Quality:** 0.85
**Glossary Terms Used:** verification, payment, network node, block header, proof-of-work, chain, Merkle branch, transaction, timestamp, attacker, honest nodes

---

### English Version

It is possible to verify payments without running a full network node. A user only needs to keep a copy of the block headers of the longest proof-of-work chain.

Users query network nodes until convinced they possess the longest chain and obtain the Merkle branch linking transactions to timestamped blocks. He can't check the transaction for himself, but by linking it to a place in the chain, he can see that a network node has accepted it.

Verification is reliable as long as honest nodes control the network, but is more vulnerable if the network is overpowered by an attacker.

While network nodes can verify transactions for themselves, the simplified method can be fooled by an attacker's fabricated transactions for as long as the attacker can continue to overpower the network.

Protection strategies include accepting alerts from network nodes detecting invalid blocks, prompting full block downloads. Businesses that receive frequent payments will probably still want to run their own nodes for more independent security and quicker verification.

---

### النسخة العربية

من الممكن التحقق من المدفوعات دون تشغيل عقدة شبكة كاملة. يحتاج المستخدم فقط إلى الاحتفاظ بنسخة من رؤوس الكتل لسلسلة إثبات العمل الأطول.

يستعلم المستخدمون عقد الشبكة حتى يقتنعوا بأنهم يمتلكون السلسلة الأطول ويحصلون على فرع ميركل الذي يربط المعاملات بالكتل ذات الطوابع الزمنية. لا يمكنه التحقق من المعاملة بنفسه، ولكن من خلال ربطها بموقع في السلسلة، يمكنه رؤية أن عقدة شبكة قد قبلتها.

يكون التحقق موثوقاً طالما أن العقد الأمينة تسيطر على الشبكة، ولكنه أكثر عرضة للخطر إذا تم التغلب على الشبكة من قبل مهاجم.

بينما يمكن لعقد الشبكة التحقق من المعاملات بأنفسها، يمكن خداع الطريقة المبسطة بمعاملات مزيفة للمهاجم طالما يمكن للمهاجم الاستمرار في التغلب على الشبكة.

تشمل استراتيجيات الحماية قبول التنبيهات من عقد الشبكة التي تكتشف كتلاً غير صالحة، مما يدفع إلى تنزيل الكتل الكاملة. من المحتمل أن ترغب الشركات التي تتلقى مدفوعات متكررة في تشغيل عقدها الخاصة للحصول على أمان أكثر استقلالية وتحقق أسرع.

---

### Translation Notes

- **Figures referenced:** Figure 5 (SPV verification diagram - referenced in original paper)
- **Key terms introduced:** simplified payment verification (التحقق المبسط من الدفع), full network node (عقدة شبكة كاملة), block headers (رؤوس الكتل), Merkle branch (فرع ميركل), fabricated transactions (معاملات مزيفة), invalid blocks (كتل غير صالحة), independent security (أمان مستقل)
- **Equations:** None
- **Citations:** None
- **Special handling:** SPV concept is fundamental to lightweight Bitcoin clients - maintained technical precision

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.85
- Readability: 0.84
- Glossary consistency: 0.86
- **Overall section score:** 0.85
