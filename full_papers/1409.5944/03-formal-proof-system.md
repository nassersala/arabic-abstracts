# Section 3: What is a Formal Proof System?
## القسم 3: ما هو نظام البرهان الصوري؟

**Section:** formal proof system
**Translation Quality:** 0.87
**Glossary Terms Used:** formal system, axiom, derivation, algorithm, mechanical

---

### English Version

How do we connect Theorem 2.1, which is about functions, to Gödel's first incompleteness theorem, which is about logical systems? We first must define a *formal proof system*.

**Definition:** A formal proof system $\Pi$ has three components:
1. A finite alphabet, and some finite subset words and phrases that can be used in forming (or writing) *statements*.

2. A finite list of *axioms* (statements that we take as true); and

3. A finite list of *rules of reasoning*, also called *logical inference, deduction or derivation* rules, that can be applied to create a new statement from axioms and the statements already created, in an unambiguous, mechanical way.

The word "mechanical" is central to the definition of rules of reasoning, and to the whole purpose of a formal proof system:

> ... we need to impose some condition to the effect that recognizing an axiom or applying a rule must be a mechanical matter ... it is required of a formal system that in order to verify that something is an axiom or an application of a rule of reasoning, we ... need only apply mechanical checking of the kind that can be carried out by a computer.

For example, the alphabet might be the standard ASCII alphabet with 256 symbols, and Axiom 1 might be: "for any integer $x$, $x+1 > x$." Axiom 2 might be: "for any integers $x$ and $y$, $x + y$ is an integer." A derivation rule might be: "for any three integers, $x, y, z$, if $x > y$ and $y > z$ then $x > z$." (Call this rule the "Transitivity Rule".)

The finite set of allowed English words and phrases might include the phrase: "for any integer". Of course, there will typically be more axioms, derivation rules, and known words and phrases than in this example.

### 3.1 What is a Formal Derivation?

**Definition:** A *formal derivation* in $\Pi$ of a statement $S$ is a series of statements that begin with some axioms of $\Pi$, and then successively apply derivation rules in $\Pi$ to obtain statement $S$.

For example, $S$ might be the statement: "For any integer $w$, $w + 1 + 1 > w$". A formal derivation of $S$ in $\Pi$ (using axioms and derivation rules introduced above) might be:

- $w$ is an integer, 1 is an integer, so $w+1$ is an integer (by Axiom 2).

- $w+1$ is an integer (by the previous statement), 1 is an integer, so $w+1 + 1 > w + 1$ (by Axiom 1).

- $w+1 + 1 + 1 > w + 1 > w$ (by the previous statement and Axiom 1).

- $w+1 + 1 > w$ (by the Transitivity Rule). This is statement $S$.

The finite subset of English used in this formal derivation includes the words and phrases "is an integer", "by the Transitivity Rule", "by the previous statement" etc. These would be part of the finite subset of English that is part of the definition of $\Pi$. Each phrase used must have a clear and precise meaning in $\Pi$, so that each statement in a formal derivation, other than an axiom, follows in a mechanical way from the preceding statements by the application of some derivation rule(s) or axioms.

Formal derivations are very tedious, and humans don't want to write derivations this way, but computers can write and check them, a fact that is key in our treatment of Gödel's theorem. (Note that what I have called a "formal derivation" is more often called a "formal proof". But that is confusing, because people usually think of a "proof" as something that establishes a *true* statement, not a statement that might be false. So here we use "formal derivation" to avoid that confusion.)

### 3.2 Mechanical Generation and Checking of Formal Derivations

We now make four key points about formal derivations.

1. It is easy to write a program $P$ that can begin generating, in order of the lengths of the strings, every string $s$ that can be written in the alphabet of $\Pi$, and using allowed words and phrases of the formal proof system $\Pi$. Program $P$ will never stop because there is no bound on the length of the strings, and most of the strings will not be formal derivations of anything. But, for any finite-length string $s$ using the alphabet of $\Pi$, $P$ will eventually (and in finite time) generate $s$.

2. A formal derivation, being a series of statements, is just a string formed from the alphabet and the allowed words and phrases of the formal proof system $\Pi$. Hence, if $s$ is any string specifying a formal derivation, $P$ will eventually (and in finite time) generate it.

3. We can create a program $P'$ that knows the alphabet, the axioms, the deduction rules, and the meaning of the words of the allowed subset of English used in $\Pi$, so that $P'$ can precisely interpret the effect of each line of a formal derivation. That is, $P'$ can *mechanically* check whether each line is an axiom, or follows from the previous lines by an application of some deduction rule(s) or axioms. Therefore, given a statement $S$, and a string $s$ that might be a formal derivation of $S$, program $P'$ can check (in a purely mechanical way, and in finite time) whether string $s$ is a formal derivation of statement $S$ in $\Pi$.

4. For any statement $S$, after program $P$ generates a string $s$, program $P'$ can check whether $s$ is a formal derivation of statement $S$ in $\Pi$, before $P$ generates the next string. Hence, if there is a formal derivation $s$ in $\Pi$ of statement $S$, then $s$ will be generated and recognized in finite time by interleaving the execution of programs $P$ and $P'$.

Note that most of the strings that $P$ generates will be garbage, and most of the strings that are not garbage will not be formal derivations of $S$ in $\Pi$. But, if string $s$ is a formal derivation of statement $S$, then in finite time, program $P$ will generate $s$, and program $P'$ will recognize that $s$ is a formal derivation in $\Pi$ of statement $S$.

Similarly, we can have another program $P''$ that checks whether a string $s$ is a formal derivation of the statement "not $S$", written $\neg S$. So if $\neg S$ is a statement that can be derived in $\Pi$, the interleaved execution of programs $P$ and $P''$ will, in finite time, generate and recognize that $s$ is a formal derivation of $\neg S$.

---

### النسخة العربية

كيف نربط النظرية 2.1، التي تتعلق بالدوال، بنظرية عدم الاكتمال الأولى لغودل، التي تتعلق بالأنظمة المنطقية؟ يجب علينا أولاً تعريف *نظام برهان صوري*.

**تعريف:** نظام البرهان الصوري $\Pi$ له ثلاثة مكونات:
1. أبجدية محدودة، وبعض المجموعات الفرعية المحدودة من الكلمات والعبارات التي يمكن استخدامها في تكوين (أو كتابة) *العبارات*.

2. قائمة محدودة من *البديهيات* (العبارات التي نعتبرها صحيحة)؛ و

3. قائمة محدودة من *قواعد الاستدلال*، تسمى أيضاً قواعد *الاستنتاج المنطقي أو الاستنباط أو الاشتقاق*، التي يمكن تطبيقها لإنشاء عبارة جديدة من البديهيات والعبارات التي تم إنشاؤها بالفعل، بطريقة واضحة وآلية.

كلمة "آلية" محورية في تعريف قواعد الاستدلال، ولغرض نظام البرهان الصوري بأكمله:

> ... نحتاج إلى فرض شرط ما يفيد بأن التعرف على بديهية أو تطبيق قاعدة يجب أن يكون مسألة آلية ... من المطلوب من نظام صوري أنه للتحقق من أن شيئاً ما هو بديهية أو تطبيق لقاعدة استدلال، نحتاج فقط ... إلى تطبيق فحص آلي من النوع الذي يمكن تنفيذه بواسطة حاسوب.

على سبيل المثال، قد تكون الأبجدية هي أبجدية ASCII القياسية بـ 256 رمزاً، وقد تكون البديهية 1: "لأي عدد صحيح $x$، $x+1 > x$." قد تكون البديهية 2: "لأي عددين صحيحين $x$ و $y$، $x + y$ عدد صحيح." قد تكون قاعدة اشتقاق: "لأي ثلاثة أعداد صحيحة، $x, y, z$، إذا كان $x > y$ و $y > z$ فإن $x > z$." (اسم هذه القاعدة "قاعدة التعدية".)

المجموعة المحدودة من الكلمات والعبارات الإنجليزية المسموح بها قد تتضمن العبارة: "لأي عدد صحيح". بالطبع، عادة ما سيكون هناك المزيد من البديهيات وقواعد الاشتقاق والكلمات والعبارات المعروفة أكثر من هذا المثال.

### 3.1 ما هو الاشتقاق الصوري؟

**تعريف:** *الاشتقاق الصوري* في $\Pi$ للعبارة $S$ هو سلسلة من العبارات التي تبدأ ببعض بديهيات $\Pi$، ثم تطبق بشكل متتابع قواعد الاشتقاق في $\Pi$ للحصول على العبارة $S$.

على سبيل المثال، قد تكون $S$ العبارة: "لأي عدد صحيح $w$، $w + 1 + 1 > w$". قد يكون الاشتقاق الصوري لـ $S$ في $\Pi$ (باستخدام البديهيات وقواعد الاشتقاق المقدمة أعلاه):

- $w$ عدد صحيح، 1 عدد صحيح، إذن $w+1$ عدد صحيح (بواسطة البديهية 2).

- $w+1$ عدد صحيح (بواسطة العبارة السابقة)، 1 عدد صحيح، إذن $w+1 + 1 > w + 1$ (بواسطة البديهية 1).

- $w+1 + 1 + 1 > w + 1 > w$ (بواسطة العبارة السابقة والبديهية 1).

- $w+1 + 1 > w$ (بواسطة قاعدة التعدية). هذه هي العبارة $S$.

المجموعة الفرعية المحدودة من اللغة الإنجليزية المستخدمة في هذا الاشتقاق الصوري تتضمن الكلمات والعبارات "عدد صحيح"، "بواسطة قاعدة التعدية"، "بواسطة العبارة السابقة" إلخ. ستكون هذه جزءاً من المجموعة الفرعية المحدودة من اللغة الإنجليزية التي هي جزء من تعريف $\Pi$. يجب أن يكون لكل عبارة مستخدمة معنى واضح ودقيق في $\Pi$، بحيث أن كل عبارة في الاشتقاق الصوري، بخلاف البديهية، تتبع بطريقة آلية من العبارات السابقة عن طريق تطبيق بعض قواعد الاشتقاق أو البديهيات.

الاشتقاقات الصورية مملة جداً، والبشر لا يريدون كتابة الاشتقاقات بهذه الطريقة، لكن الحواسيب يمكنها كتابتها والتحقق منها، وهذه حقيقة أساسية في معالجتنا لنظرية غودل. (لاحظ أن ما سميته "اشتقاق صوري" غالباً ما يسمى "برهان صوري". لكن هذا مربك، لأن الناس عادة ما يفكرون في "البرهان" على أنه شيء يثبت عبارة *صحيحة*، وليس عبارة قد تكون خاطئة. لذلك نستخدم هنا "اشتقاق صوري" لتجنب هذا الالتباس.)

### 3.2 التوليد الآلي والتحقق من الاشتقاقات الصورية

نقدم الآن أربع نقاط رئيسية حول الاشتقاقات الصورية.

1. من السهل كتابة برنامج $P$ يمكنه البدء في توليد، حسب ترتيب أطوال السلاسل النصية، كل سلسلة نصية $s$ يمكن كتابتها بأبجدية $\Pi$، وباستخدام الكلمات والعبارات المسموح بها في نظام البرهان الصوري $\Pi$. لن يتوقف البرنامج $P$ أبداً لأنه لا يوجد حد لطول السلاسل النصية، ومعظم السلاسل النصية لن تكون اشتقاقات صورية لأي شيء. لكن، لأي سلسلة نصية $s$ بطول محدود تستخدم أبجدية $\Pi$، سيولد $P$ في النهاية (وفي وقت محدود) $s$.

2. الاشتقاق الصوري، كونه سلسلة من العبارات، هو مجرد سلسلة نصية مكونة من الأبجدية والكلمات والعبارات المسموح بها في نظام البرهان الصوري $\Pi$. وبالتالي، إذا كانت $s$ أي سلسلة نصية تحدد اشتقاقاً صورياً، فإن $P$ سيولدها في النهاية (وفي وقت محدود).

3. يمكننا إنشاء برنامج $P'$ يعرف الأبجدية والبديهيات وقواعد الاستنباط ومعنى الكلمات من المجموعة الفرعية المسموح بها من اللغة الإنجليزية المستخدمة في $\Pi$، بحيث يمكن لـ $P'$ تفسير تأثير كل سطر من الاشتقاق الصوري بدقة. أي، يمكن لـ $P'$ أن يتحقق *آلياً* مما إذا كان كل سطر بديهية، أو يتبع من الأسطر السابقة عن طريق تطبيق بعض قواعد الاستنباط أو البديهيات. لذلك، بالنظر إلى عبارة $S$، وسلسلة نصية $s$ قد تكون اشتقاقاً صورياً لـ $S$، يمكن للبرنامج $P'$ التحقق (بطريقة آلية بحتة، وفي وقت محدود) مما إذا كانت السلسلة النصية $s$ اشتقاقاً صورياً للعبارة $S$ في $\Pi$.

4. لأي عبارة $S$، بعد أن يولد البرنامج $P$ سلسلة نصية $s$، يمكن للبرنامج $P'$ التحقق مما إذا كانت $s$ اشتقاقاً صورياً للعبارة $S$ في $\Pi$، قبل أن يولد $P$ السلسلة النصية التالية. وبالتالي، إذا كان هناك اشتقاق صوري $s$ في $\Pi$ للعبارة $S$، فإن $s$ سيتم توليده والتعرف عليه في وقت محدود عن طريق التنفيذ المتشابك للبرنامجين $P$ و $P'$.

لاحظ أن معظم السلاسل النصية التي يولدها $P$ ستكون عشوائية، ومعظم السلاسل النصية التي ليست عشوائية لن تكون اشتقاقات صورية لـ $S$ في $\Pi$. لكن، إذا كانت السلسلة النصية $s$ اشتقاقاً صورياً للعبارة $S$، فإنه في وقت محدود، سيولد البرنامج $P$ $s$، وسيتعرف البرنامج $P'$ على أن $s$ اشتقاق صوري في $\Pi$ للعبارة $S$.

بالمثل، يمكننا الحصول على برنامج آخر $P''$ يتحقق مما إذا كانت السلسلة النصية $s$ اشتقاقاً صورياً للعبارة "ليس $S$"، مكتوبة $\neg S$. لذلك إذا كانت $\neg S$ عبارة يمكن اشتقاقها في $\Pi$، فإن التنفيذ المتشابك للبرنامجين $P$ و $P''$ سيولد ويتعرف، في وقت محدود، على أن $s$ اشتقاق صوري لـ $\neg S$.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** formal proof system (نظام برهان صوري), axiom (بديهية), rules of reasoning (قواعد الاستدلال), derivation rules (قواعد الاشتقاق), logical inference (الاستنتاج المنطقي), formal derivation (اشتقاق صوري), mechanical (آلي), transitivity (التعدية)
- **Equations:** Multiple mathematical examples in formal derivations
- **Citations:** Quote from Torkel Franzen's book "Gödel's Theorem"
- **Special handling:** The distinction between "formal proof" and "formal derivation" is carefully maintained in Arabic

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
