# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** formalization, type theory, proof assistant, dependent types, inductive types, universal algebra, theorem, proof, structural induction, mechanization, verification

---

### English Version

To support formalization in type theory of research level mathematics in universal algebra and related fields, we present the Agda Universal Algebra Library (AgdaUALib), a software library containing formal statements and proofs of the core definitions and results of universal algebra. The UALib is written in Agda [17], a programming language and proof assistant based on Martin-Löf Type Theory (MLTT) that supports dependent and inductive types.

**1.1 Motivation**

The seminal idea for the AgdaUALib project was the observation that, on the one hand, a number of fundamental constructions in universal algebra can be defined recursively, and theorems about them proved by structural induction, while, on the other hand, inductive and dependent types make possible very precise formal representations of recursively defined objects, which often admit elegant constructive proofs of properties of such objects. An important feature of such proofs in type theory is that they are total functional programs and, as such, they are computable, composable, and machine-verifiable.

Finally, our own research experience has taught us that a proof assistant and programming language (like Agda), when equipped with specialized libraries and domain-specific tactics to automate the proof idioms of our field, can be an extremely powerful and effective asset. As such we believe that proof assistants and their supporting libraries will eventually become indispensable tools in the working mathematician's toolkit.

**1.2 Attributions and Contributions**

The mathematical results described in this paper have well known informal proofs. Our main contribution is the formalization, mechanization, and verification of the statements and proofs of these results in dependent type theory using Agda.

Unless explicitly stated otherwise, the Agda source code described in this paper is due to the author, with the following caveat: the UALib depends on the Type Topology library of Martín Escardó [10]. For convenience, we refer to Escardó's library as TypeTopo throughout the paper. For the sake of completeness and clarity, and to keep the paper mostly self-contained, we repeat some definitions from TypeTopo, but in each instance we cite the original source.

**1.3 Prior art**

There have been a number of efforts to formalize parts of universal algebra in type theory prior to ours, most notably:

- Capretta [4] (1999) formalized the basics of universal algebra in the Calculus of Inductive Constructions using the Coq proof assistant;
- Spitters and van der Weegen [19] (2011) formalized the basics of universal algebra and some classical algebraic structures, also in the Calculus of Inductive Constructions using the Coq proof assistant, promoting the use of type classes;
- Gunther, et al [11] (2018) developed what seems to be (prior to the UALib) the most extensive library of formal universal algebra to date; in particular, this work includes a formalization of some basic equational logic; also (unlike the UALib) it handles multisorted algebraic structures; (like the UALib) it is based on dependent type theory and the Agda proof assistant.

Some other projects aimed at formalizing mathematics generally, and algebra in particular, have developed into very extensive libraries that include definitions, theorems, and proofs about algebraic structures, such as groups, rings, modules, etc. However, the goals of these efforts seem to be the formalization of special classical algebraic structures, as opposed to the general theory of (universal) algebras. Moreover, the part of universal algebra and equational logic formalized in the UALib extends beyond the scope of prior efforts. In particular, the library now includes a proof of Birkhoff's variety theorem. Most other proofs of this theorem that we know of are informal and nonconstructive.

**1.4 Organization of the paper**

In this paper we limit ourselves to the presentation of the core foundational modules of the UALib so that we have space to discuss some of the more interesting type theoretic and foundational issues that arose when developing the library and attempting to represent advanced mathematical notions in type theory and formalize them in Agda. This is the first in a series of three papers describing the AgdaUALib. The second paper ([8]) covers homomorphisms, terms, and subalgebras. The third paper ([9]) covers free algebras, equational classes of algebras (i.e., varieties), and Birkhoff's HSP theorem.

This present paper is organized into three parts as follows. The first part is §2 which introduces the basic concepts of type theory with special emphasis on the way such concepts are formalized in Agda. Specifically, §2.1 introduces Sigma types and Agda's hierarchy of universes. The important topics of equality and function extensionality are discussed in §2.2 and §2.3; §2.4 covers inverses and inverse images of functions. In §2.5 we describe a technical problem that one frequently encounters when working in a noncumulative universe hierarchy and offer some tools for resolving the type-checking errors that arise from this.

The second part is §3 which covers relation types and quotient types. Specifically, §3.1 defines types that represent unary and binary relations as well as function kernels. These "discrete relation types," are all very standard. In §3.2 we introduce the (less standard) types that we use to represent general and dependent relations. We call these "continuous relations" because they can have arbitrary arity (general relations) and they can be defined over arbitrary families of types (dependent relations). In §3.3 we cover standard types for equivalence relations and quotients, and in §3.4 we discuss a family of concepts that are vital to the mechanization of mathematics using type theory; these are the closely related concepts of truncation, sets, propositions, and proposition extensionality.

The third part of the paper is §4 which covers the basic domain-specific types offered by the UALib. It is here that we finally get to see some types representing algebraic structures. Specifically, we describe types for operations and signatures (§4.1), general algebras (§4.2), and product algebras (§4.3), including types for representing products over arbitrary classes of algebraic structures. Finally, we define types for congruence relations and quotient algebras in §4.4.

**1.5 Resources**

We conclude this introduction with some pointers to helpful reference materials. For the required background in Universal Algebra, we recommend the textbook by Clifford Bergman [1]. For the type theory background, we recommend the HoTT Book [18] and Escardó's Introduction to Univalent Foundations of Mathematics with Agda [10].

The following are informed the development of the UALib and are highly recommended:
- Introduction to Univalent Foundations of Mathematics with Agda, Escardó [10].
- Dependent Types at Work, Bove and Dybjer [2].
- Dependently Typed Programming in Agda, Norell and Chapman [16].
- Formalization of Universal Algebra in Agda, Gunther, Gadea, Pagano [11].
- Programming Languages Foundations in Agda, Philip Wadler [24].

More information about AgdaUALib can be obtained from the following official sources:
- ualib.org (the web site) documents every line of code in the library.
- gitlab.com/ualib/ualib.gitlab.io (the source code) AgdaUALib is open source.
- The Agda UALib, Part 2: homomorphisms, terms, and subalgebras [8].
- The Agda UALib, Part 3: free algebras, equational classes, and Birkhoff's theorem [9].

The first item links to the official UALib html documentation which includes complete proofs of every theorem we mention here, and much more, including the Agda modules covered in the first and third installments of this series of papers on the UALib.

Finally, readers will get much more out of reading the paper if they download the AgdaUALib from https://gitlab.com/ualib/ualib.gitlab.io, install the library, and try it out for themselves.

---

### النسخة العربية

لدعم الصياغة الرسمية في نظرية الأنواع للرياضيات على مستوى البحث في الجبر العام والمجالات ذات الصلة، نقدم مكتبة Agda للجبر العام (AgdaUALib)، وهي مكتبة برمجية تحتوي على العبارات والبراهين الرسمية للتعريفات والنتائج الأساسية في الجبر العام. كُتبت UALib بلغة Agda [17]، وهي لغة برمجة ومساعد برهان مبني على نظرية أنواع مارتن-لوف (MLTT) التي تدعم الأنواع التابعة والاستقرائية.

**1.1 الدافع**

كانت الفكرة الأساسية لمشروع AgdaUALib هي الملاحظة بأن، من جهة، يمكن تعريف عدد من البنى الأساسية في الجبر العام بشكل تكراري، ويمكن إثبات المبرهنات المتعلقة بها بواسطة الاستقراء البنيوي، بينما من جهة أخرى، تجعل الأنواع الاستقرائية والتابعة ممكنة تمثيلات رسمية دقيقة جداً للكائنات المعرّفة تكرارياً، والتي غالباً ما تسمح ببراهين بنائية أنيقة لخصائص هذه الكائنات. من السمات المهمة لهذه البراهين في نظرية الأنواع أنها برامج دالية كاملة، وعلى هذا النحو، فهي قابلة للحساب والتركيب والتحقق الآلي.

أخيراً، علّمتنا تجربتنا البحثية الخاصة أن مساعد البرهان ولغة البرمجة (مثل Agda)، عندما يكونان مجهزين بمكتبات متخصصة وتكتيكات خاصة بالمجال لأتمتة أنماط البرهان في مجالنا، يمكن أن يكونا أداة قوية وفعالة للغاية. وعلى هذا النحو نعتقد أن مساعدات البرهان ومكتباتها الداعمة ستصبح في النهاية أدوات لا غنى عنها في مجموعة أدوات الرياضي العامل.

**1.2 الإسهامات والإشادات**

النتائج الرياضية الموصوفة في هذا البحث لها براهين غير رسمية معروفة جيداً. إسهامنا الرئيسي هو الصياغة الرسمية والميكنة والتحقق من العبارات وبراهين هذه النتائج في نظرية الأنواع التابعة باستخدام Agda.

ما لم يُذكر خلاف ذلك صراحةً، فإن شفرة Agda المصدرية الموصوفة في هذا البحث هي من تأليف الباحث، مع التحفظ التالي: تعتمد UALib على مكتبة Type Topology لمارتن إسكاردو [10]. للراحة، نشير إلى مكتبة إسكاردو بـ TypeTopo في جميع أنحاء البحث. من أجل الاكتمال والوضوح، ولإبقاء البحث مكتفياً ذاتياً في معظمه، نكرر بعض التعريفات من TypeTopo، ولكننا في كل حالة نشير إلى المصدر الأصلي.

**1.3 الأعمال السابقة**

كانت هناك عدة جهود لصياغة أجزاء من الجبر العام رسمياً في نظرية الأنواع قبل جهودنا، والأبرز من بينها:

- صاغ Capretta [4] (1999) أساسيات الجبر العام رسمياً في حساب البنى الاستقرائية باستخدام مساعد البرهان Coq؛
- صاغ Spitters وvan der Weegen [19] (2011) أساسيات الجبر العام وبعض البنى الجبرية الكلاسيكية رسمياً، أيضاً في حساب البنى الاستقرائية باستخدام مساعد البرهان Coq، مع تعزيز استخدام فئات الأنواع؛
- طور Gunther وآخرون [11] (2018) ما يبدو أنه (قبل UALib) المكتبة الأكثر شمولاً للجبر العام الرسمي حتى الآن؛ وعلى وجه الخصوص، يتضمن هذا العمل صياغة رسمية لبعض المنطق المعادلاتي الأساسي؛ كما أنه (على عكس UALib) يتعامل مع البنى الجبرية متعددة الأصناف؛ (مثل UALib) فهو يعتمد على نظرية الأنواع التابعة ومساعد البرهان Agda.

بعض المشاريع الأخرى التي تهدف إلى صياغة الرياضيات عموماً، والجبر خصوصاً، رسمياً قد تطورت إلى مكتبات واسعة جداً تتضمن تعريفات ومبرهنات وبراهين حول البنى الجبرية، مثل الزمر والحلقات والوحدات النمطية، إلخ. ومع ذلك، يبدو أن أهداف هذه الجهود هي الصياغة الرسمية للبنى الجبرية الكلاسيكية الخاصة، بدلاً من النظرية العامة للجبر (العام). علاوة على ذلك، فإن الجزء من الجبر العام والمنطق المعادلاتي المصاغ رسمياً في UALib يمتد إلى ما هو أبعد من نطاق الجهود السابقة. وعلى وجه الخصوص، تتضمن المكتبة الآن برهاناً لمبرهنة التنوع لبيركوف. معظم البراهين الأخرى لهذه المبرهنة التي نعرفها هي غير رسمية وغير بنائية.

**1.4 تنظيم البحث**

في هذا البحث نقتصر على عرض الوحدات الأساسية الجوهرية لـ UALib حتى يتوفر لدينا مساحة لمناقشة بعض القضايا الأكثر إثارة للاهتمام المتعلقة بنظرية الأنواع والأسس التي ظهرت عند تطوير المكتبة ومحاولة تمثيل المفاهيم الرياضية المتقدمة في نظرية الأنواع وصياغتها رسمياً في Agda. هذا هو الأول في سلسلة من ثلاثة أبحاث تصف AgdaUALib. يغطي البحث الثاني ([8]) التشاكلات والحدود والجبور الجزئية. يغطي البحث الثالث ([9]) الجبور الحرة والفئات المعادلاتية للجبور (أي التنوعات) ومبرهنة HSP لبيركوف.

هذا البحث الحالي منظم في ثلاثة أجزاء على النحو التالي. الجزء الأول هو §2 الذي يقدم المفاهيم الأساسية لنظرية الأنواع مع التركيز بشكل خاص على الطريقة التي تُصاغ بها هذه المفاهيم رسمياً في Agda. على وجه التحديد، يقدم §2.1 أنواع سيجما والتسلسل الهرمي للأكوان في Agda. تُناقش الموضوعات المهمة المتعلقة بالمساواة والتوسعية الدالية في §2.2 و§2.3؛ يغطي §2.4 المعكوسات والصور المعكوسة للدوال. في §2.5 نصف مشكلة تقنية كثيراً ما يواجهها المرء عند العمل في تسلسل هرمي للأكوان غير تراكمي ونقدم بعض الأدوات لحل أخطاء فحص الأنواع الناتجة عن ذلك.

الجزء الثاني هو §3 الذي يغطي أنواع العلاقات وأنواع الحاصل القسمي. على وجه التحديد، يُعرّف §3.1 الأنواع التي تمثل العلاقات الأحادية والثنائية بالإضافة إلى نوى الدوال. "أنواع العلاقات المتقطعة" هذه كلها قياسية جداً. في §3.2 نقدم الأنواع (الأقل قياسية) التي نستخدمها لتمثيل العلاقات العامة والتابعة. نسمي هذه "العلاقات المستمرة" لأنها يمكن أن تكون لها قوى عشوائية (العلاقات العامة) ويمكن تعريفها على عائلات عشوائية من الأنواع (العلاقات التابعة). في §3.3 نغطي الأنواع القياسية لعلاقات التكافؤ والحاصلات القسمية، وفي §3.4 نناقش مجموعة من المفاهيم الحيوية لميكنة الرياضيات باستخدام نظرية الأنواع؛ وهي المفاهيم المرتبطة ارتباطاً وثيقاً بالاقتطاع والمجموعات والقضايا والتوسعية القضوية.

الجزء الثالث من البحث هو §4 الذي يغطي الأنواع الأساسية الخاصة بالمجال التي تقدمها UALib. هنا نرى أخيراً بعض الأنواع التي تمثل البنى الجبرية. على وجه التحديد، نصف الأنواع الخاصة بالعمليات والتواقيع (§4.1)، والجبور العامة (§4.2)، وجبور الجداء (§4.3)، بما في ذلك الأنواع الخاصة بتمثيل الجداءات على فئات عشوائية من البنى الجبرية. أخيراً، نُعرّف الأنواع الخاصة بعلاقات التطابق والجبور الحاصل القسمي في §4.4.

**1.5 الموارد**

نختتم هذه المقدمة ببعض الإشارات إلى المواد المرجعية المفيدة. للخلفية المطلوبة في الجبر العام، نوصي بكتاب كليفورد بيرغمان [1]. للخلفية في نظرية الأنواع، نوصي بكتاب HoTT [18] ومقدمة إسكاردو للأسس الأحادية للرياضيات مع Agda [10].

المراجع التالية أرشدت تطوير UALib ويوصى بها بشدة:
- مقدمة للأسس الأحادية للرياضيات مع Agda، إسكاردو [10].
- الأنواع التابعة في العمل، Bove وDybjer [2].
- البرمجة بالأنواع التابعة في Agda، Norell وChapman [16].
- الصياغة الرسمية للجبر العام في Agda، Gunther وGadea وPagano [11].
- أسس لغات البرمجة في Agda، فيليب وادلر [24].

يمكن الحصول على مزيد من المعلومات حول AgdaUALib من المصادر الرسمية التالية:
- ualib.org (الموقع الإلكتروني) يوثق كل سطر من التعليمات البرمجية في المكتبة.
- gitlab.com/ualib/ualib.gitlab.io (الشفرة المصدرية) AgdaUALib مفتوحة المصدر.
- مكتبة Agda UALib، الجزء 2: التشاكلات والحدود والجبور الجزئية [8].
- مكتبة Agda UALib، الجزء 3: الجبور الحرة والفئات المعادلاتية ومبرهنة بيركوف [9].

يرتبط العنصر الأول بالتوثيق الرسمي لـ UALib بصيغة html الذي يتضمن براهين كاملة لكل مبرهنة نذكرها هنا، وأكثر من ذلك بكثير، بما في ذلك وحدات Agda المغطاة في الأجزاء الأولى والثالثة من هذه السلسلة من الأبحاث حول UALib.

أخيراً، سيستفيد القراء كثيراً من قراءة البحث إذا قاموا بتنزيل AgdaUALib من https://gitlab.com/ualib/ualib.gitlab.io، وتثبيت المكتبة، وتجربتها بأنفسهم.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** AgdaUALib, UALib, Martin-Löf Type Theory (MLTT), TypeTopo, Birkhoff's variety theorem, HSP theorem, structural induction, mechanization
- **Equations:** 0
- **Citations:** Multiple references to prior work [1], [2], [4], [8], [9], [10], [11], [16], [17], [18], [19], [24]
- **Special handling:** Technical terms like "Sigma types," "universe hierarchy," "function extensionality" maintained with Arabic explanations

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88

### Back-Translation Key Paragraph

English (original): "The seminal idea for the AgdaUALib project was the observation that, on the one hand, a number of fundamental constructions in universal algebra can be defined recursively, and theorems about them proved by structural induction, while, on the other hand, inductive and dependent types make possible very precise formal representations of recursively defined objects, which often admit elegant constructive proofs of properties of such objects."

Arabic translation: "كانت الفكرة الأساسية لمشروع AgdaUALib هي الملاحظة بأن، من جهة، يمكن تعريف عدد من البنى الأساسية في الجبر العام بشكل تكراري، ويمكن إثبات المبرهنات المتعلقة بها بواسطة الاستقراء البنيوي، بينما من جهة أخرى، تجعل الأنواع الاستقرائية والتابعة ممكنة تمثيلات رسمية دقيقة جداً للكائنات المعرّفة تكرارياً، والتي غالباً ما تسمح ببراهين بنائية أنيقة لخصائص هذه الكائنات."

Back-translation to English: "The fundamental idea for the AgdaUALib project was the observation that, on one hand, a number of fundamental structures in universal algebra can be defined recursively, and theorems related to them can be proved by structural induction, while on the other hand, inductive and dependent types make possible very precise formal representations of recursively defined objects, which often allow elegant constructive proofs of the properties of these objects."

**Verification:** ✓ Semantic equivalence maintained
