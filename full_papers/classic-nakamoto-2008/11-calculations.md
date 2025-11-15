# Section 11: Calculations
## القسم 11: الحسابات

**Section:** calculations
**Translation Quality:** 0.84
**Glossary Terms Used:** attacker, chain, honest nodes, block, probability, transaction, proof-of-work, network

---

### English Version

We consider the scenario of an attacker trying to generate an alternate chain faster than the honest chain.

Even successful attempts don't enable arbitrary system changes—creating value or stealing—since nodes reject invalid transactions. An attacker can only try to change one of his own transactions to take back money he recently spent.

Honest and attacker chain races resemble Binomial Random Walks. Success extends the honest chain (+1), failure extends the attacker chain (-1).

Attacker catch-up probability mirrors the Gambler's Ruin problem: Suppose a gambler with unlimited credit starts at a deficit and plays potentially an infinite number of trials to try to reach breakeven.

Given p (probability honest node finds next block) > q (attacker probability), catch-up probability drops exponentially with deficit blocks. With the odds against him, if he doesn't make a lucky lunge forward early on, his chances become vanishingly small as he falls further behind.

Transaction security timing assumes a sender attacker wanting recipients to believe payment occurred before secretly switching it back. The receiver generates a new key pair and gives the public key to the sender shortly before signing.

This prevents preparing block chains ahead of time. After sending, dishonest senders work secretly on parallel chains with alternate transaction versions.

Recipients wait until transactions enter blocks with z subsequent linked blocks. Assuming honest blocks took average expected time, attacker progress follows Poisson distribution: λ = z q/p

Catch-up probability calculations multiply Poisson density for each progress amount by catch-up probability from that point. The provided C code implementation demonstrates exponential probability drop-off with z.

Results show dramatic probability reduction: at q=0.1, z=5 yields P=0.0009137; at q=0.3, z=24 yields P=0.0006132.

---

### النسخة العربية

نعتبر سيناريو مهاجم يحاول توليد سلسلة بديلة أسرع من السلسلة الأمينة.

حتى المحاولات الناجحة لا تمكن من إجراء تغييرات تعسفية على النظام - إنشاء قيمة أو سرقة - حيث ترفض العقد المعاملات غير الصالحة. يمكن للمهاجم فقط محاولة تغيير إحدى معاملاته الخاصة لاسترجاع الأموال التي أنفقها مؤخراً.

تشبه سباقات السلسلة الأمينة والمهاجم المشي العشوائي ذو الحدين. النجاح يمدد السلسلة الأمينة (+1)، والفشل يمدد سلسلة المهاجم (-1).

احتمال لحاق المهاجم يعكس مشكلة خراب المقامر: افترض أن مقامراً برصيد غير محدود يبدأ بعجز ويلعب عدداً لا نهائياً محتملاً من المحاولات لمحاولة الوصول إلى نقطة التعادل.

بالنظر إلى p (احتمال أن تجد العقدة الأمينة الكتلة التالية) > q (احتمال المهاجم)، ينخفض احتمال اللحاق بشكل أسي مع الكتل المتأخرة. مع الاحتمالات ضده، إذا لم يحقق قفزة محظوظة للأمام في وقت مبكر، فإن فرصه تصبح متلاشية تقريباً مع تخلفه أكثر.

توقيت أمان المعاملة يفترض مهاجماً مرسلاً يريد أن يعتقد المستلمون أن الدفع حدث قبل تبديله سراً. يولد المستلم زوج مفاتيح جديد ويعطي المفتاح العام للمرسل بفترة قصيرة قبل التوقيع.

يمنع هذا إعداد سلاسل الكتل مسبقاً. بعد الإرسال، يعمل المرسلون غير الأمناء سراً على سلاسل موازية بنسخ معاملات بديلة.

ينتظر المستلمون حتى تدخل المعاملات في كتل مع z كتلة مرتبطة لاحقة. بافتراض أن الكتل الأمينة استغرقت الوقت المتوسط المتوقع، يتبع تقدم المهاجم توزيع بواسون: λ = z q/p

حسابات احتمال اللحاق تضرب كثافة بواسون لكل مقدار تقدم في احتمال اللحاق من تلك النقطة. يوضح تنفيذ كود C المقدم الانخفاض الأسي للاحتمال مع z.

تظهر النتائج انخفاضاً كبيراً في الاحتمال: عند q=0.1، z=5 ينتج P=0.0009137؛ عند q=0.3، z=24 ينتج P=0.0006132.

---

### Translation Notes

- **Figures referenced:** Graph showing probability of attacker success vs. number of confirmations (referenced in original paper)
- **Key terms introduced:** alternate chain (سلسلة بديلة), arbitrary changes (تغييرات تعسفية), Binomial Random Walk (المشي العشوائي ذو الحدين), Gambler's Ruin (خراب المقامر), deficit (عجز), breakeven (نقطة التعادل), exponentially (بشكل أسي), vanishingly small (متلاشية تقريباً), parallel chain (سلسلة موازية), Poisson distribution (توزيع بواسون), confirmations (كتلة مرتبطة لاحقة)
- **Equations:** Multiple probability formulas including λ = z q/p and various probability calculations
- **Citations:** Reference to Gambler's Ruin problem, C code implementation
- **Special handling:** Heavy mathematical content - maintained technical precision while ensuring readability. Mathematical notation kept in English with Arabic explanations

### Quality Metrics

- Semantic equivalence: 0.85
- Technical accuracy: 0.84
- Readability: 0.83
- Glossary consistency: 0.85
- **Overall section score:** 0.84
