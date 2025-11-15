# Section 9: Combining and Splitting Value
## القسم 9: دمج وتقسيم القيمة

**Section:** combining-splitting-value
**Translation Quality:** 0.88
**Glossary Terms Used:** transaction, input, output, value, payment, change

---

### English Version

Although it would be possible to handle coins individually, it would be unwieldy to make a separate transaction for every cent in a transfer.

To allow value to be split and combined, transactions contain multiple inputs and outputs.

Typically, transactions feature either a single input from larger previous transactions or multiple inputs combining smaller amounts. Usually, there are at most two outputs: payment and change returned to sender.

It should be noted that fan-out, where a transaction depends on several transactions, and those transactions depend on many more, is not a problem here.

Complete standalone transaction history extraction isn't necessary.

---

### النسخة العربية

على الرغم من أنه سيكون من الممكن التعامل مع العملات بشكل فردي، إلا أنه سيكون من الصعب إجراء معاملة منفصلة لكل سنت في التحويل.

للسماح بتقسيم القيمة ودمجها، تحتوي المعاملات على مدخلات ومخرجات متعددة.

عادةً ما تحتوي المعاملات إما على مدخل واحد من معاملات سابقة أكبر أو مدخلات متعددة تجمع مبالغ أصغر. عادةً ما يكون هناك مخرجان على الأكثر: الدفع والباقي الذي يُعاد إلى المرسل.

تجدر الإشارة إلى أن التفرع، حيث تعتمد معاملة على عدة معاملات، وتعتمد تلك المعاملات على العديد من المعاملات الأخرى، ليس مشكلة هنا.

استخراج تاريخ المعاملات المستقل بالكامل ليس ضرورياً.

---

### Translation Notes

- **Figures referenced:** Figure 6 (transaction structure showing inputs and outputs - referenced in original paper)
- **Key terms introduced:** handle coins individually (التعامل مع العملات بشكل فردي), split and combine (تقسيم ودمج), multiple inputs (مدخلات متعددة), multiple outputs (مخرجات متعددة), change (الباقي), fan-out (التفرع), transaction history (تاريخ المعاملات)
- **Equations:** None
- **Citations:** None
- **Special handling:** UTXO (Unspent Transaction Output) model - explained transaction structure clearly in Arabic

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
