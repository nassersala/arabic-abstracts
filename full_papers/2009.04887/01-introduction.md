# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** theorem, proof, incompleteness, consistency, axiom, formal system, recursively axiomatized, ω-consistent, provability

---

### English Version

Gödel's first and second incompleteness theorem are some of the most important and profound results in the foundations of mathematics and have had wide influence on the development of logic, philosophy, mathematics, computer science as well as other fields. Intuitively speaking, Gödel's incompleteness theorems express that any rich enough logical system cannot prove its own consistency, i.e. that no contradiction like 0 = 1 can be derived within this system.

Gödel [46] proves his first incompleteness theorem (G1) for a certain formal system P related to Russell-Whitehead's Principia Mathematica based on the simple theory of types over the natural number series and the Dedekind-Peano axioms (see [8], p.3). Gödel announces the second incompleteness theorem (G2) in an abstract published in October 1930: no consistency proof of systems such as Principia, Zermelo-Fraenkel set theory, or the systems investigated by Ackermann and von Neumann is possible by methods which can be formulated in these systems (see [153], p.431).

Gödel comments in a footnote of [46] that G2 is corollary of G1 (and in fact a formalized version of G1): if T is consistent, then the consistency of T is not provable in T where the consistency of T is formulated as the arithmetic formula which says that there exists an unprovable sentence in T. Gödel [46] sketches a proof of G2 and promises to provide full details in a subsequent publication. This promise is not fulfilled, and a detailed proof of G2 for first-order arithmetic only appears in a monograph by Hilbert and Bernays [62]. Abstract logic-free formulations of Gödel's incompleteness theorems have been given by Kleene [80] ("symmetric form"), Smullyan [124] ("representation systems"), and others. The following is a modern reformulation of Gödel's incompleteness theorems.

**Theorem 1.1 (Gödel, [46]).** Let T be a recursively axiomatized extension of PA.

**G1** If T is ω-consistent, then T is incomplete.

**G2** If T is consistent, then the consistency of T is not provable in T.

Gödel's incompleteness theorems G1 and G2 are of a rather different nature and scope. In this paper, we will discuss different versions of G1 and G2, from incompleteness for extensions of PA to incompleteness for systems weaker than PA w.r.t. interpretation. We will freely use G1 and G2 to refer to both Gödel's first and second incompleteness theorems, and their different versions. The meaning of G1 and G2 will be clear from the context in which we refer to them.

Gödel's incompleteness theorems exhibit certain weaknesses and limitations of a given formal system. For Gödel, his incompleteness theorems indicate the creative power of human reason. In Emil Post's celebrated words: mathematical proof is an essentially creative activity (see [102], p.339). The impact of Gödel's incompleteness theorems is not confined to the community of mathematicians and logicians; popular accounts are well-known within the general scientific community and beyond. Gödel's incompleteness theorems raise a number of philosophical questions concerning the nature of logic and mathematics as well as mind and machine. For the impact of Gödel's incompleteness theorems, Feferman said:

> their relevance to mathematical logic (and its offspring in the theory of computation) is paramount; further, their philosophical relevance is significant, but in just what way is far from settled; and finally, their mathematical relevance outside of logic is very much unsubstantiated but is the object of ongoing, tantalizing efforts (see [35], p.434).

From the literature, there are some good textbooks and survey papers on Gödel's incompleteness theorems. For textbooks, we refer to [30, 102, 95, 38, 121, 15, 123, 124, 55, 41]. For survey papers, we refer to [122, 8, 83, 17, 138, 13, 24]. In the last twenty years, there have been a lot of advances in the study of incompleteness. We felt that a comprehensive survey paper for the current state-of-art of this research field is missing from the literature.

The motivation of this paper is four-fold:
• Give the reader an overview of the current state-of-art of research on incompleteness.
• Classify these new advances on incompleteness under some important themes.
• Propose some new questions not covered in the literature.
• Set the direction for the future research of incompleteness.

Due to space limitations and our personal taste, it is impossible to cover all research results from the literature related to incompleteness in this survey. Therefore, we will focus on three aspects of new advances in research on incompleteness:
• classifications of different proofs of Gödel's incompleteness theorems;
• the limit of the applicability of G1;
• the limit of the applicability of G2.

We think these are the most important three aspects of research on incompleteness and reflect the depth and breadth of the research on incompleteness after Gödel. In this survey, we will focus on logical and mathematical aspects of research on incompleteness.

An important and interesting topic concerning incompleteness is missing in this paper: philosophy of Gödel's incompleteness theorems. For us, the widely discussed and most important philosophical questions about Gödel's incompleteness theorems are: the relationship between G1 and the mechanism thesis, the status of Gödel's disjunctive thesis, and the intensionality problem of G2. We leave a survey of philosophical discussions of Gödel's incompleteness theorems for a future philosophy paper.

This paper is structured as follows. In Section 1, we introduce the motivation, the main content and the structure of this paper. In Section 2, we list the preliminary notions and definitions used in this paper. In Section 3, we examine different proofs of Gödel's incompleteness theorems and classify these proofs based on nine criteria. In Section 4, we examine the limit of the applicability of G1 both for extensions of PA, and for theories weaker than PA w.r.t. interpretation. In Section 5, we examine the limit of the applicability of G2, and discuss sources of indeterminacy in the formulation of the consistency statement.

---

### النسخة العربية

تُعد نظريتا عدم الاكتمال الأولى والثانية لغودل من أهم وأعمق النتائج في أسس الرياضيات، وكان لهما تأثير واسع على تطور المنطق والفلسفة والرياضيات وعلوم الحاسوب وغيرها من المجالات. بشكل بديهي، تعبر نظريات عدم الاكتمال لغودل عن أن أي نظام منطقي غني بما فيه الكفاية لا يمكنه إثبات اتساقه الذاتي، أي أنه لا يمكن اشتقاق تناقض مثل 0 = 1 داخل هذا النظام.

أثبت غودل [46] نظرية عدم الاكتمال الأولى (G1) لنظام صوري معين P مرتبط بكتاب Principia Mathematica لراسل وايتهيد، استناداً إلى نظرية الأنواع البسيطة على سلسلة الأعداد الطبيعية وبديهيات ديديكايند-بيانو (انظر [8]، ص. 3). أعلن غودل عن نظرية عدم الاكتمال الثانية (G2) في ملخص نُشر في أكتوبر 1930: لا يمكن إثبات اتساق أنظمة مثل Principia أو نظرية المجموعات لزيرميلو-فرانكل أو الأنظمة التي بحثها أكرمان وفون نيومان بطرق يمكن صياغتها في هذه الأنظمة (انظر [153]، ص. 431).

علّق غودل في حاشية [46] بأن G2 هي نتيجة طبيعية من G1 (وفي الواقع نسخة مُصاغة بشكل صوري من G1): إذا كان T متسقاً، فإن اتساق T غير قابل للإثبات في T، حيث يُصاغ اتساق T كصيغة حسابية تقول إن هناك جملة غير قابلة للإثبات في T. رسم غودل [46] مخططاً لبرهان G2 ووعد بتقديم تفاصيل كاملة في منشور لاحق. لم يتحقق هذا الوعد، ولم يظهر برهان مفصل لـ G2 للحساب من الدرجة الأولى إلا في مونوغراف لهيلبرت وبرنايس [62]. قُدمت صياغات مجردة خالية من المنطق لنظريات عدم الاكتمال لغودل من قبل كليني [80] ("الشكل المتماثل")، وسمليان [124] ("أنظمة التمثيل")، وآخرين. فيما يلي إعادة صياغة حديثة لنظريات عدم الاكتمال لغودل.

**النظرية 1.1 (غودل، [46]).** لتكن T امتداداً مبدئياً بشكل عودي لـ PA.

**G1** إذا كانت T متسقة-ω، فإن T غير مكتملة.

**G2** إذا كانت T متسقة، فإن اتساق T غير قابل للإثبات في T.

نظريتا عدم الاكتمال لغودل G1 و G2 لهما طبيعة ونطاق مختلفان إلى حد ما. في هذا البحث، سنناقش إصدارات مختلفة من G1 و G2، من عدم الاكتمال لامتدادات PA إلى عدم الاكتمال لأنظمة أضعف من PA فيما يتعلق بالتفسير. سنستخدم G1 و G2 بحرية للإشارة إلى نظريتي عدم الاكتمال الأولى والثانية لغودل، وإصداراتهما المختلفة. سيكون معنى G1 و G2 واضحاً من السياق الذي نشير إليهما فيه.

تُظهر نظريات عدم الاكتمال لغودل نقاط ضعف وقيود معينة لنظام صوري معين. بالنسبة لغودل، تشير نظريات عدم الاكتمال الخاصة به إلى القوة الإبداعية للعقل البشري. بكلمات إميل بوست الشهيرة: البرهان الرياضي هو نشاط إبداعي بالأساس (انظر [102]، ص. 339). لا يقتصر تأثير نظريات عدم الاكتمال لغودل على مجتمع الرياضيين والمنطقيين؛ فالعروض الشعبية معروفة جيداً داخل المجتمع العلمي العام وخارجه. تثير نظريات عدم الاكتمال لغودل عدداً من الأسئلة الفلسفية المتعلقة بطبيعة المنطق والرياضيات وكذلك العقل والآلة. بخصوص تأثير نظريات عدم الاكتمال لغودل، قال فيفرمان:

> إن صلتها بالمنطق الرياضي (ونسله في نظرية الحوسبة) ذات أهمية قصوى؛ علاوة على ذلك، فإن صلتها الفلسفية كبيرة، ولكن الطريقة التي تكون بها بعيدة عن الاستقرار؛ وأخيراً، فإن صلتها الرياضية خارج المنطق غير مدعومة إلى حد كبير ولكنها موضوع جهود مستمرة ومثيرة للاهتمام (انظر [35]، ص. 434).

من الأدبيات، هناك بعض الكتب الدراسية والمقالات الاستقصائية الجيدة حول نظريات عدم الاكتمال لغودل. للكتب الدراسية، نشير إلى [30، 102، 95، 38، 121، 15، 123، 124، 55، 41]. للمقالات الاستقصائية، نشير إلى [122، 8، 83، 17، 138، 13، 24]. في العشرين عاماً الماضية، كانت هناك تطورات كثيرة في دراسة عدم الاكتمال. شعرنا أن هناك نقصاً في مقال استقصائي شامل للحالة الحالية للفن في هذا المجال البحثي في الأدبيات.

دافع هذا البحث رباعي:
• إعطاء القارئ نظرة عامة على الحالة الحالية للفن في البحث حول عدم الاكتمال.
• تصنيف هذه التطورات الجديدة حول عدم الاكتمال تحت موضوعات مهمة.
• اقتراح أسئلة جديدة غير مغطاة في الأدبيات.
• تحديد اتجاه البحث المستقبلي لعدم الاكتمال.

بسبب قيود المساحة وذوقنا الشخصي، من المستحيل تغطية جميع نتائج الأبحاث من الأدبيات المتعلقة بعدم الاكتمال في هذا الاستقصاء. لذلك، سنركز على ثلاثة جوانب من التطورات الجديدة في البحث حول عدم الاكتمال:
• تصنيفات البراهين المختلفة لنظريات عدم الاكتمال لغودل؛
• حد قابلية التطبيق لـ G1؛
• حد قابلية التطبيق لـ G2.

نعتقد أن هذه هي الجوانب الثلاثة الأكثر أهمية للبحث حول عدم الاكتمال وتعكس عمق واتساع البحث حول عدم الاكتمال بعد غودل. في هذا الاستقصاء، سنركز على الجوانب المنطقية والرياضية للبحث حول عدم الاكتمال.

موضوع مهم ومثير للاهتمام يتعلق بعدم الاكتمال مفقود في هذا البحث: فلسفة نظريات عدم الاكتمال لغودل. بالنسبة لنا، الأسئلة الفلسفية الأكثر نقاشاً والأكثر أهمية حول نظريات عدم الاكتمال لغودل هي: العلاقة بين G1 وأطروحة الآلية، ووضع أطروحة غودل الفصلية، ومشكلة الامتداد الداخلي لـ G2. نترك استقصاءً للمناقشات الفلسفية لنظريات عدم الاكتمال لغودل لبحث فلسفي مستقبلي.

يُنظّم هذا البحث على النحو التالي. في القسم 1، نقدم الدافع والمحتوى الرئيسي وبنية هذا البحث. في القسم 2، نسرد المفاهيم والتعريفات الأولية المستخدمة في هذا البحث. في القسم 3، نفحص البراهين المختلفة لنظريات عدم الاكتمال لغودل ونصنف هذه البراهين بناءً على تسعة معايير. في القسم 4، نفحص حد قابلية التطبيق لـ G1 لكل من امتدادات PA والنظريات الأضعف من PA فيما يتعلق بالتفسير. في القسم 5، نفحص حد قابلية التطبيق لـ G2، ونناقش مصادر عدم التحديد في صياغة عبارة الاتساق.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Gödel's incompleteness theorems (نظريات عدم الاكتمال لغودل)
  - G1 (first incompleteness theorem) (نظرية عدم الاكتمال الأولى)
  - G2 (second incompleteness theorem) (نظرية عدم الاكتمال الثانية)
  - PA (Peano Arithmetic) (حساب بيانو)
  - ω-consistent (متسقة-ω)
  - Recursively axiomatized (مبدئي بشكل عودي)
  - Formal system (نظام صوري)
  - Consistency (الاتساق)
  - Provability (قابلية الإثبات)
  - Incompleteness (عدم الاكتمال)

- **Equations:** Theorem 1.1 formulation (kept in same format)
- **Citations:** Multiple references [46], [8], [153], [62], [80], [124], [35], [102], [30-41], [122-24], [8-138]
- **Special handling:**
  - Preserved proper names (Gödel, Russell, Whitehead, Hilbert, Bernays, Kleene, Smullyan, Post, Feferman)
  - Kept mathematical notation (T, PA, G1, G2)
  - Preserved the block quote from Feferman
  - Maintained structure of four-fold motivation and three-aspect focus

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87

### Back-Translation (First Paragraph)

Gödel's first and second incompleteness theorems are among the most important and profound results in the foundations of mathematics, and have had a wide impact on the development of logic, philosophy, mathematics, computer science, and other fields. Intuitively, Gödel's incompleteness theorems express that any sufficiently rich logical system cannot prove its own consistency, that is, a contradiction such as 0 = 1 cannot be derived within this system.
