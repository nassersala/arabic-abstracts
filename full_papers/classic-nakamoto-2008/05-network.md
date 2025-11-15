# Section 5: Network
## القسم 5: الشبكة

**Section:** network
**Translation Quality:** 0.88
**Glossary Terms Used:** network, node, transaction, block, proof-of-work, hash, chain, broadcast

---

### English Version

Network operation follows these steps:

1. New transactions broadcast to all nodes
2. Each node collects transactions into a block
3. Nodes work on finding difficult proof-of-work for their block
4. Nodes finding proof-of-work broadcast blocks to all nodes
5. Nodes accept blocks only if transactions are valid and unspent
6. Nodes express acceptance by working on the next block, using the accepted block's hash as previous hash

Nodes always consider the longest chain to be the correct one and will keep working on extending it.

When nodes simultaneously broadcast different block versions, some receive one first. These nodes work on the first received but save the other branch if it becomes longer. The tie will be broken when the next proof-of-work is found and one branch becomes longer.

New transaction broadcasts do not necessarily need to reach all nodes. As long as they reach many nodes, they will get into a block before long.

Block broadcasts tolerate dropped messages. Nodes request missed blocks when receiving subsequent blocks.

---

### النسخة العربية

تتبع عملية الشبكة الخطوات التالية:

1. تُبث المعاملات الجديدة إلى جميع العقد
2. تجمع كل عقدة المعاملات في كتلة
3. تعمل العقد على إيجاد إثبات العمل الصعب لكتلتها
4. تبث العقد التي تجد إثبات العمل الكتل إلى جميع العقد
5. تقبل العقد الكتل فقط إذا كانت المعاملات صالحة وغير منفقة
6. تعبر العقد عن القبول من خلال العمل على الكتلة التالية، باستخدام تجزئة الكتلة المقبولة كتجزئة سابقة

تعتبر العقد دائماً السلسلة الأطول هي الصحيحة وستستمر في العمل على توسيعها.

عندما تبث العقد نسخاً مختلفة من الكتل في وقت واحد، يتلقى البعض واحدة أولاً. تعمل هذه العقد على الأولى المستلمة لكنها تحفظ الفرع الآخر إذا أصبح أطول. سيتم كسر التعادل عندما يتم العثور على إثبات العمل التالي ويصبح فرع واحد أطول.

لا يلزم بالضرورة أن تصل عمليات بث المعاملات الجديدة إلى جميع العقد. طالما أنها تصل إلى العديد من العقد، فسوف تدخل في كتلة قريباً.

تتحمل عمليات بث الكتل الرسائل المفقودة. تطلب العقد الكتل الفائتة عند تلقي الكتل اللاحقة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** broadcast (تُبث/بث), valid transactions (معاملات صالحة), unspent (غير منفقة), longest chain (السلسلة الأطول), branch (فرع), tie breaking (كسر التعادل), dropped messages (رسائل مفقودة)
- **Equations:** None
- **Citations:** None
- **Special handling:** Network protocol steps presented as numbered list - maintained structure in Arabic

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
