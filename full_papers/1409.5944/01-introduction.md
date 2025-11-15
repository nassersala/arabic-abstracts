# Section 1: Introduction: Why I wrote this
## القسم 1: المقدمة: لماذا كتبت هذا

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** theorem, proof, formal system, formal logic, paradox

---

### English Version

Gödel's famous incompleteness theorems (there are two of them) concern the ability of a formal system to state and derive all true statements, and only true statements, in some fixed domain; and concern the ability of logic to determine if a formal system has that property. They were developed in the early 1930s. Very loosely, the first theorem says that in any "sufficiently rich" formal proof system where it is not possible to prove a false statement about *arithmetic*, there will also be true statements about arithmetic that cannot be proved.

Most discussions of Gödel's theorems fall into one of two types: either they emphasize perceived cultural and philosophical meanings of the theorems, and perhaps sketch some of the ideas of the proofs, usually relating Gödel's proofs to riddles and paradoxes, but do not attempt rigorous, complete proofs; or they do present rigorous proofs, but in the traditional style of mathematical logic, with all of its heavy notation, difficult definitions, technical issues in Gödel's original approach, and connections to broader logical theory before and after Gödel. Many people are frustrated by these two extreme types of expositions and want a short, straight-forward, rigorous proof that they can understand.

Over time, various people have realized that somewhat weaker, but still meaningful, variants of Gödel's first incompleteness theorem can be rigorously proved by simpler arguments based on notions of computability. This approach avoids the heavy machinery of mathematical logic at one extreme; and does not rely on analogies, paradoxes, philosophical discussions or hand-waiving, at the other extreme. This is the just-right *Goldilocks* approach. However, the available expositions of this middle approach have still been aimed at a relatively sophisticated audience, and have either been too brief, or have been embedded in larger, more involved discussions. A short, self-contained Goldilocks exposition of a version of Gödel's first theorem, aimed at a broad audience, has been lacking. Here I offer such an exposition.

---

### النسخة العربية

تتعلق نظريات عدم الاكتمال الشهيرة لغودل (وهناك نظريتان منها) بقدرة النظام الصوري على صياغة واشتقاق جميع العبارات الصحيحة، وفقط العبارات الصحيحة، في مجال محدد؛ وتتعلق بقدرة المنطق على تحديد ما إذا كان النظام الصوري يمتلك هذه الخاصية. تم تطويرها في أوائل الثلاثينيات من القرن الماضي. بشكل تقريبي جداً، تقول النظرية الأولى أنه في أي نظام برهان صوري "غني بما يكفي" حيث لا يمكن إثبات عبارة خاطئة حول *الحساب*، ستكون هناك أيضاً عبارات صحيحة حول الحساب لا يمكن إثباتها.

تقع معظم المناقشات حول نظريات غودل في واحد من نوعين: إما أنها تركز على المعاني الثقافية والفلسفية المدركة للنظريات، وربما تقدم رسماً تخطيطياً لبعض أفكار البراهين، وعادة ما تربط براهين غودل بالألغاز والمفارقات، لكنها لا تحاول تقديم براهين صارمة وكاملة؛ أو أنها تقدم براهين صارمة، لكن بالأسلوب التقليدي للمنطق الرياضي، مع كل الترميزات الثقيلة والتعريفات الصعبة والقضايا التقنية في نهج غودل الأصلي، والروابط بالنظرية المنطقية الأوسع قبل غودل وبعده. كثير من الناس محبطون من هذين النوعين المتطرفين من العروض ويريدون برهاناً قصيراً ومباشراً وصارماً يمكنهم فهمه.

مع مرور الوقت، أدرك عدة أشخاص أن متغيرات أضعف نوعاً ما، لكنها لا تزال ذات معنى، من نظرية عدم الاكتمال الأولى لغودل يمكن إثباتها بصرامة بحجج أبسط تستند إلى مفاهيم القابلية للحوسبة. يتجنب هذا النهج الآليات الثقيلة للمنطق الرياضي من طرف؛ ولا يعتمد على التشبيهات أو المفارقات أو المناقشات الفلسفية أو التلويح باليد، من الطرف الآخر. هذا هو نهج *غولديلوكس* المناسب تماماً. ومع ذلك، فإن العروض المتاحة لهذا النهج المتوسط لا تزال موجهة لجمهور متطور نسبياً، وكانت إما موجزة جداً، أو مضمنة في مناقشات أكبر وأكثر تعقيداً. كان هناك نقص في عرض غولديلوكس قصير ومكتفٍ ذاتياً لنسخة من نظرية غودل الأولى، موجه لجمهور واسع. أقدم هنا مثل هذا العرض.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** incompleteness theorem (نظرية عدم الاكتمال), formal system (نظام صوري), formal proof system (نظام برهان صوري), arithmetic (الحساب), computability (القابلية للحوسبة), Goldilocks approach (نهج غولديلوكس)
- **Equations:** 0
- **Citations:** References to Scott Aaronson's book and Sipser's book in footnotes
- **Special handling:** The term "Goldilocks" kept as transliteration غولديلوكس as it refers to the fairy tale character and the metaphor of finding the "just right" middle ground

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
