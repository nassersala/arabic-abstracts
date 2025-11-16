# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** formal methods (الطرق الرسمية), security property (خاصية الأمان), Dolev-Yao attacker (مهاجم Dolev-Yao), computational attacker (مهاجم حسابي), probabilistic polynomial time (زمن احتمالي متعدد الحدود), bitstring (سلسلة بتات), security parameter (معامل الأمان)

---

### English Version

It is important to increase our confidence in the security of protocols. Using formal methods to prove a formal security property is the best way to get a strong confidence. There is however a difficulty: we need not only to specify formally the programs and the security properties, but also the attacker.

One of the most popular attacker model, sometimes called the "Dolev-Yao" attacker, consists in assuming that, in between any message emission and the corresponding reception, the attacker may apply a fixed set of rules modifying the message. In addition, the attacker schedules the communications. More precisely, the messages are terms in a formal algebra and the rules are given by a fixed set of combination abilities, together with a rewrite system specifying how to simplify the terms.

There are several more or less automatic verification tools that rely on such a model. Let us cite ProVerif [8], Tamarin [22] and APTE [11] for instance. Completing a proof with one of these tools will however only prove the security in the corresponding DY model.

Another popular attacker model, the computational attacker, gives the same network control to the attacker as in the Dolev-Yao model, but does not limit the attacker computations to the combination of a fixed set of operations: any probabilistic polynomial time computation is possible. More precisely, messages are bitstrings, random numbers are typically bitstrings in {0, 1}^η (where η is the security parameter) and the attacker's computation time is bounded by a polynomial in η. This model reflects more accurately a real-world attacker than the Dolev-Yao model, but formal proofs are harder to complete and more error-prone.

There exist several formal verification tools in the computational model. For example EASYCRYPT [6] can be used for the construction of provably secure cryptographic primitives, and CRYPTOVERIF [9] and F* [5] have been used for the study of security protocols (e.g. [10], [7]). As expected, such tools are less automatic than the verification tools in the DY model. Using such tools, we may also fail to find a proof while there is one.

We advocate the use of another approach, sketched in [3], [4], which allows to complete formal proofs in the computational model that can be automated and formally checked. This method has many other advantages, some of which are given in these papers: it could be applied, in principle, to more powerful attacker models (such as attackers having access to some side-channels); it can be used to derive "minimal" properties of the primitives that are sufficient to entail the security of the protocol (we will come back to this feature later).

The main technique, which we will recall, is to express the security of a protocol as the unsatisfiability of a formula in first-order logic. The formula contains axioms, reflecting the assumed computational properties of the security primitives, and the negation of the security property, applied to terms reflecting the execution(s) of the protocol. This approach is, we believe, simpler than formally specifying computational security games, probabilistic machines and simulations: there is no security parameter, no probabilities, no timing constraints, no Turing machines... Nonetheless, in case of success, the proof is valid in any model of the axioms, including the computational model.

Compared to EASYCRYPT, our logic works at a more abstract level, using only first-order formulas and targeting full automation and a form of completeness (saturating the axioms and the negation of the security property implies that there is an attack).

As it is now, this approach does not provide any quantitative information: the protocol is computationally secure or it is not. We could however extract from a security proof a bound on the success probability of the attacker, depending on its computational power: we would only have to compose the adversary's advantages corresponding to each clause. Also, because the logic does not include the security parameter, we can only prove the security of a number of sessions of the protocol that does not depend on the security parameter (while there is no such limitation in CRYPTOVERIF for instance). Still, it subsumes the symbolic approach, in which the number of sessions is also independent of the security parameter.

A related logic for reachability security properties has been introduced in [3] and is implemented in the prototype tool SCARY [25]. It has been used for a few experiments. The logic for indistinguishability properties, introduced in [4], is not (yet) implemented. There is only one toy example provided in [4], another one in [2] and a more significant case study developed in [26].

We investigate in this paper the application of this approach to security proofs of RFID protocols, typically proofs of unlinkability. There are a lot of such protocols that appeared in the literature, most of which are very simple, due to the low computing capabilities of a RFID tag: the protocols often use only primitives such as hashing, xoring, pairing and splitting. These protocols have been studied, attacked, patched and automatically proved in the DY model (see for instance [17]). On the computational side, [28] investigates the computational definitions of unlinkability, together with examples of RFID protocols that satisfy (or not) the definitions. There are however very few proofs of security in the computational model and no (up to our knowledge) formal security proof.

For instance, an RFID protocol is proposed in [20], together with a universally composable (claimed) proof. The proof is however quite informal, and attacks were found on this protocol (see [23]). Admittedly, such attacks can be easily circumvented, but this shows that a formal approach is useful, if not necessary. Similarly, as reported in [18], other RFID protocols that were claimed secure turned out to be broken.

A large fraction of RFID protocols, the so-called Ultra-lightweight RFID protocols (e.g. [12], [24]), aim at ensuring only weak security properties, and against passive attackers, because of the strong constraints on the number of gates embedded in the RFID tags. We do not consider such protocols in this paper.

**Contributions:** The contributions of this paper are:

1) To design axioms that reflect security assumptions on the primitives that are used in the RFID protocols (typically hash functions, pseudo-random generators and xor), and to prove their correctness.

2) To express formally the computational unlinkability. There are various definitions; we chose to formalize one of them (from [18]). Most other definitions can be expressed in a similar way. The security property is expressed as the indistinguishability of two sequences of terms. These terms are computed from the protocol specification extended with corruption capabilities. We use a specific technique inspired by the folding of transition systems described in [4].

3) To illustrate the proof technique on two examples taken from [27]: KCL and LAK. As far as we know, all published RFID protocols, that do not rely on encryption, are computationally insecure. This is also the case of these two protocols. We propose small modifications of the protocols, which prevent the known attacks. Some of the modified versions are secure in the DY model. Depending on the assumptions on the primitives, they may however be insecure in the computational model. For instance, if we assume the hash function to be pre-image resistant and one-way, the corrected version of LAK, proved in [17], is not necessarily computationally secure: there might be attacks on both authentication and unlinkability. We actually need a family of keyed hash functions, which satisfies the pseudo-random functions (PRF) property. With the appropriate implementation assumptions, we formally prove the security of the two protocols. Up to our knowledge, these are the first formal security proofs of RFID protocols in the computational model.

**Outline:** In Section II, we briefly recall the methodology described in [4] and we propose some axioms for the hashing and exclusive or, that depend on the assumptions on the cryptographic libraries. In Section III we recall the definition of privacy of a RFID protocol given by Juels and Weis in [18], and we show how this property translates in the logic. In Section IV we recall the two protocols KCL and LAK, known attacks on them and formally prove the security of fixed versions of the protocols. We also show that relaxing the assumptions yields some attacks. Finally, in Section V, we show (as expected) that abstracting pseudo-random numbers with random numbers is sound, provided that the seed is not used for any other purpose.

---

### النسخة العربية

من المهم زيادة ثقتنا في أمان البروتوكولات. يُعد استخدام الطرق الرسمية لإثبات خاصية أمان رسمية أفضل طريقة للحصول على ثقة قوية. ومع ذلك، هناك صعوبة: نحتاج ليس فقط إلى تحديد البرامج وخصائص الأمان رسمياً، ولكن أيضاً المهاجم.

أحد نماذج المهاجم الأكثر شيوعاً، والذي يُسمى أحياناً مهاجم "Dolev-Yao"، يتكون من افتراض أنه بين أي إرسال رسالة والاستقبال المقابل لها، قد يطبق المهاجم مجموعة ثابتة من القواعد التي تعدل الرسالة. بالإضافة إلى ذلك، يقوم المهاجم بجدولة الاتصالات. بشكل أكثر دقة، الرسائل هي حدود في جبر رسمي والقواعد معطاة بمجموعة ثابتة من قدرات التركيب، مع نظام إعادة كتابة يحدد كيفية تبسيط الحدود.

هناك العديد من أدوات التحقق الآلية أو شبه الآلية التي تعتمد على مثل هذا النموذج. دعونا نذكر ProVerif [8] و Tamarin [22] و APTE [11] على سبيل المثال. ومع ذلك، فإن إكمال برهان باستخدام إحدى هذه الأدوات سيثبت الأمان في نموذج DY المقابل فقط.

نموذج مهاجم شائع آخر، وهو المهاجم الحسابي، يمنح المهاجم نفس السيطرة على الشبكة كما في نموذج Dolev-Yao، ولكنه لا يحد من حسابات المهاجم إلى تركيبة من مجموعة ثابتة من العمليات: أي حساب احتمالي متعدد الحدود في الزمن ممكن. بشكل أكثر دقة، الرسائل هي سلاسل بتات، والأرقام العشوائية هي عادةً سلاسل بتات في {0, 1}^η (حيث η هو معامل الأمان) ووقت حساب المهاجم محدود بمتعدد حدود في η. يعكس هذا النموذج بشكل أكثر دقة مهاجماً حقيقياً من نموذج Dolev-Yao، لكن البراهين الرسمية أصعب في الإكمال وأكثر عرضة للأخطاء.

توجد العديد من أدوات التحقق الرسمية في النموذج الحسابي. على سبيل المثال، يمكن استخدام EASYCRYPT [6] لبناء بدائل تشفيرية آمنة يمكن إثباتها، وقد تم استخدام CRYPTOVERIF [9] و F* [5] لدراسة بروتوكولات الأمان (مثل [10]، [7]). كما هو متوقع، هذه الأدوات أقل آلية من أدوات التحقق في نموذج DY. باستخدام هذه الأدوات، قد نفشل أيضاً في إيجاد برهان بينما يوجد واحد.

نؤيد استخدام نهج آخر، موضح في [3]، [4]، والذي يسمح بإكمال براهين رسمية في النموذج الحسابي يمكن أتمتتها والتحقق منها رسمياً. هذه الطريقة لها العديد من المزايا الأخرى، بعضها مذكور في هذه الأوراق: يمكن تطبيقها، من حيث المبدأ، على نماذج مهاجم أقوى (مثل المهاجمين الذين لديهم وصول إلى بعض القنوات الجانبية)؛ ويمكن استخدامها لاشتقاق خصائص "دنيا" للبدائل التي تكفي لضمان أمان البروتوكول (سنعود إلى هذه الميزة لاحقاً).

التقنية الرئيسية، التي سنذكرها، هي التعبير عن أمان البروتوكول كعدم قابلية للإرضاء لصيغة في المنطق من الدرجة الأولى. تحتوي الصيغة على بديهيات، تعكس الخصائص الحسابية المفترضة للبدائل الأمنية، ونفي خاصية الأمان، مطبقة على حدود تعكس تنفيذ (تنفيذات) البروتوكول. هذا النهج، كما نعتقد، أبسط من التحديد الرسمي لألعاب الأمان الحسابية، والآلات الاحتمالية والمحاكاة: لا يوجد معامل أمان، ولا احتمالات، ولا قيود زمنية، ولا آلات تورينج... ومع ذلك، في حالة النجاح، يكون البرهان صالحاً في أي نموذج للبديهيات، بما في ذلك النموذج الحسابي.

بالمقارنة مع EASYCRYPT، يعمل منطقنا على مستوى أكثر تجريداً، باستخدام صيغ من الدرجة الأولى فقط ويستهدف الأتمتة الكاملة وشكلاً من الاكتمال (إشباع البديهيات ونفي خاصية الأمان يعني أن هناك هجوماً).

كما هو الحال الآن، لا يوفر هذا النهج أي معلومات كمية: إما أن البروتوكول آمن حسابياً أو غير آمن. يمكننا مع ذلك استخراج من برهان الأمان حد لاحتمال نجاح المهاجم، اعتماداً على قدرته الحسابية: سنحتاج فقط إلى تركيب مزايا الخصم المقابلة لكل بند. أيضاً، لأن المنطق لا يتضمن معامل الأمان، يمكننا فقط إثبات أمان عدد من جلسات البروتوكول لا يعتمد على معامل الأمان (بينما لا يوجد مثل هذا القيد في CRYPTOVERIF على سبيل المثال). ومع ذلك، فإنه يشمل النهج الرمزي، حيث عدد الجلسات مستقل أيضاً عن معامل الأمان.

تم تقديم منطق ذي صلة لخصائص الأمان القابلة للوصول في [3] وهو مُنفذ في الأداة النموذجية SCARY [25]. تم استخدامه لبعض التجارب. المنطق لخصائص عدم القابلية للتمييز، المقدم في [4]، لم يُنفذ (بعد). يوجد مثال لعبة واحد فقط في [4]، وآخر في [2] ودراسة حالة أكثر أهمية مطورة في [26].

نستقصي في هذه الورقة تطبيق هذا النهج على براهين أمان بروتوكولات RFID، عادةً براهين عدم الربط. هناك الكثير من هذه البروتوكولات التي ظهرت في الأدبيات، معظمها بسيط جداً، بسبب قدرات الحوسبة المنخفضة لوسم RFID: غالباً ما تستخدم البروتوكولات بدائل فقط مثل التجزئة، والـ xor، والإقران والتقسيم. تمت دراسة هذه البروتوكولات، ومهاجمتها، وترقيعها وإثباتها تلقائياً في نموذج DY (انظر على سبيل المثال [17]). على الجانب الحسابي، يستقصي [28] التعريفات الحسابية لعدم الربط، مع أمثلة على بروتوكولات RFID التي تلبي (أو لا تلبي) التعريفات. ومع ذلك، هناك عدد قليل جداً من براهين الأمان في النموذج الحسابي ولا يوجد (حسب علمنا) برهان أمان رسمي.

على سبيل المثال، تم اقتراح بروتوكول RFID في [20]، مع برهان (مزعوم) قابل للتركيب عالمياً. ومع ذلك، فإن البرهان غير رسمي إلى حد كبير، وتم العثور على هجمات على هذا البروتوكول (انظر [23]). من المسلم به أن مثل هذه الهجمات يمكن تجنبها بسهولة، لكن هذا يظهر أن النهج الرسمي مفيد، إن لم يكن ضرورياً. وبالمثل، كما ورد في [18]، تبين أن بروتوكولات RFID الأخرى التي ادُّعي أنها آمنة مكسورة.

جزء كبير من بروتوكولات RFID، ما يسمى ببروتوكولات RFID فائقة الخفة (مثل [12]، [24])، تهدف إلى ضمان خصائص أمان ضعيفة فقط، وضد مهاجمين سلبيين، بسبب القيود القوية على عدد البوابات المدمجة في وسوم RFID. نحن لا ننظر في مثل هذه البروتوكولات في هذه الورقة.

**المساهمات:** مساهمات هذه الورقة هي:

1) تصميم بديهيات تعكس افتراضات الأمان على البدائل المستخدمة في بروتوكولات RFID (عادةً دوال التجزئة، ومولدات شبه عشوائية، و xor)، وإثبات صحتها.

2) التعبير رسمياً عن عدم الربط الحسابي. هناك تعريفات متنوعة؛ اخترنا صياغة أحدها (من [18]). يمكن التعبير عن معظم التعريفات الأخرى بطريقة مماثلة. يتم التعبير عن خاصية الأمان كعدم قابلية للتمييز بين تسلسلين من الحدود. يتم حساب هذه الحدود من مواصفات البروتوكول الموسعة بقدرات الإفساد. نستخدم تقنية محددة مستوحاة من طي أنظمة الانتقال الموصوفة في [4].

3) توضيح تقنية البرهان على مثالين مأخوذين من [27]: KCL و LAK. حسب علمنا، جميع بروتوكولات RFID المنشورة، التي لا تعتمد على التشفير، غير آمنة حسابياً. هذا هو الحال أيضاً مع هذين البروتوكولين. نقترح تعديلات صغيرة على البروتوكولات، تمنع الهجمات المعروفة. بعض النسخ المعدلة آمنة في نموذج DY. اعتماداً على الافتراضات على البدائل، قد تكون غير آمنة في النموذج الحسابي. على سبيل المثال، إذا افترضنا أن دالة التجزئة مقاومة للصورة الأولية وأحادية الاتجاه، فإن النسخة المصححة من LAK، المُثبتة في [17]، ليست بالضرورة آمنة حسابياً: قد تكون هناك هجمات على كل من المصادقة وعدم الربط. نحتاج في الواقع إلى عائلة من دوال التجزئة ذات المفاتيح، والتي تحقق خاصية الدوال شبه العشوائية (PRF). مع افتراضات التنفيذ المناسبة، نثبت رسمياً أمان البروتوكولين. حسب علمنا، هذه هي أول براهين أمان رسمية لبروتوكولات RFID في النموذج الحسابي.

**المخطط:** في القسم II، نذكر بإيجاز المنهجية الموصوفة في [4] ونقترح بعض البديهيات للتجزئة والـ or الحصري، التي تعتمد على الافتراضات على مكتبات التشفير. في القسم III نذكر تعريف خصوصية بروتوكول RFID المقدم من Juels و Weis في [18]، ونوضح كيف تُترجم هذه الخاصية في المنطق. في القسم IV نذكر البروتوكولين KCL و LAK، والهجمات المعروفة عليهما ونثبت رسمياً أمان النسخ المصححة من البروتوكولات. نوضح أيضاً أن تخفيف الافتراضات ينتج عنه بعض الهجمات. أخيراً، في القسم V، نُظهر (كما هو متوقع) أن تجريد الأرقام شبه العشوائية بأرقام عشوائية صحيح، بشرط عدم استخدام البذرة لأي غرض آخر.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Dolev-Yao attacker (مهاجم Dolev-Yao)
  - Computational attacker (مهاجم حسابي)
  - ProVerif, Tamarin, APTE (أسماء أدوات - تُبقى كما هي)
  - EASYCRYPT, CRYPTOVERIF, F* (أسماء أدوات - تُبقى كما هي)
  - First-order logic (منطق من الدرجة الأولى)
  - Unsatisfiability (عدم قابلية للإرضاء)
  - Security parameter (معامل الأمان)
  - Reachability properties (خصائص القابلية للوصول)
  - Indistinguishability properties (خصائص عدم القابلية للتمييز)
  - Ultra-lightweight RFID protocols (بروتوكولات RFID فائقة الخفة)
  - PRF - Pseudo-Random Function (دالة شبه عشوائية)
  - Corruption capabilities (قدرات الإفساد)
- **Equations:** None
- **Citations:** Multiple references [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [17], [18], [20], [22], [23], [24], [25], [26], [27], [28]
- **Special handling:**
  - Tool names kept in English
  - Mathematical notation {0,1}^η preserved
  - Technical terminology carefully translated

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
