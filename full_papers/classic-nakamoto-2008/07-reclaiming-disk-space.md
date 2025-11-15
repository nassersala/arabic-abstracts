# Section 7: Reclaiming Disk Space
## القسم 7: استعادة مساحة القرص

**Section:** reclaiming-disk-space
**Translation Quality:** 0.86
**Glossary Terms Used:** transaction, block, hash, Merkle tree, disk space, storage, node

---

### English Version

Once the latest transaction in a coin is buried under enough blocks, the spent transactions before it can be discarded to save disk space.

To facilitate this without breaking the block's hash, transactions are hashed in a Merkle Tree, with only the root included in the block's hash.

Old blocks compress by removing tree branches. Interior hashes don't require storage.

A block header with no transactions occupies approximately 80 bytes. Assuming 10-minute block generation: 80 bytes * 6 * 24 * 365 = 4.2MB per year.

With 2008-era computer systems typically selling with 2GB RAM and Moore's Law predicting 1.2GB yearly growth, storage shouldn't pose problems even requiring block headers in memory.

---

### النسخة العربية

بمجرد أن تُدفن أحدث معاملة في عملة تحت كتل كافية، يمكن التخلص من المعاملات المنفقة قبلها لتوفير مساحة القرص.

لتسهيل ذلك دون كسر تجزئة الكتلة، يتم تجزئة المعاملات في شجرة ميركل، مع تضمين الجذر فقط في تجزئة الكتلة.

تُضغط الكتل القديمة عن طريق إزالة فروع الشجرة. التجزئات الداخلية لا تتطلب تخزيناً.

يشغل رأس الكتلة بدون معاملات حوالي 80 بايت تقريباً. بافتراض توليد كتلة كل 10 دقائق: 80 بايت * 6 * 24 * 365 = 4.2 ميجابايت سنوياً.

مع أنظمة الحاسوب في عصر 2008 التي كانت تُباع عادةً مع 2 جيجابايت من الذاكرة العشوائية وقانون مور الذي يتنبأ بنمو 1.2 جيجابايت سنوياً، لا ينبغي أن يشكل التخزين مشاكل حتى لو كان يتطلب رؤوس الكتل في الذاكرة.

---

### Translation Notes

- **Figures referenced:** Figure 4 (Merkle tree diagram showing pruning - referenced in original paper)
- **Key terms introduced:** spent transactions (معاملات منفقة), Merkle Tree (شجرة ميركل), root (جذر), compress (تُضغط), tree branches (فروع الشجرة), interior hashes (تجزئات داخلية), block header (رأس الكتلة), Moore's Law (قانون مور)
- **Equations:** Storage calculation: 80 bytes * 6 * 24 * 365 = 4.2MB per year
- **Citations:** Implicit reference to Moore's Law
- **Special handling:** Technical storage optimization using Merkle trees - maintained precision in data structure terminology

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.86
