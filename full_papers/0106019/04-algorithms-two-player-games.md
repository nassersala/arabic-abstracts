# Section 4: Algorithms for Two-Player Games
## القسم 4: خوارزميات الألعاب ذات اللاعبين

**Section:** Algorithms for Two-Player Games
**Translation Quality:** 0.86
**Glossary Terms Used:** PSPACE-complete, EXPTIME-complete, NP-complete, NP-hard, polynomial-time, algorithm, graph, complexity theory, reduction

---

### English Version (Introduction)

Many bounded-length two-player games are PSPACE-complete. This is fairly natural because games are closely related to Boolean expressions with alternating quantifiers (for which deciding satisfiability is PSPACE-complete): there exists a move for Left such that, for all moves for Right, there exists another move for Left, etc. A PSPACE-completeness result has two consequences. First, being in PSPACE means that the game can be played optimally, and typically all positions can be enumerated, using possibly exponential time but only polynomial space. Thus such games lend themselves to a somewhat reasonable exhaustive search for small enough sizes. Second, the games cannot be solved in polynomial time unless P = PSPACE, which is even "less likely" than P equaling NP.

On the other hand, unbounded-length two-players games are often EXPTIME-complete. Such a result is one of the few types of true lower bounds in complexity theory, implying that all algorithms require exponential time in the worst case.

In this section we briefly survey many of these complexity results and related positive results.

[Section continues with 17 subsections covering Hex, Games on Graphs, Games of Pursuit, Checkers, Go, Five-in-a-Row, Chess, Shogi, Othello, Hackenbush, Domineering, Dots-and-Boxes, Amazons, Konane, Phutball, Conway's Angel Problem, and Jenga]

**Key Results Summary:**
- **Hex (4.1):** PSPACE-complete; first player wins (by strategy stealing) but no polynomial winning strategy known
- **Geography (4.2):** Edge Geography and Vertex Geography are PSPACE-complete
- **Node Kayles (4.2):** PSPACE-complete
- **Checkers (4.4):** EXPTIME-complete (unbounded); PSPACE-complete (bounded)
- **Go (4.5):** EXPTIME-complete (Japanese rules with kos); PSPACE-hard (without kos)
- **Chess (4.7):** EXPTIME-complete (generalized n×n boards)
- **Shogi (4.8):** EXPTIME-complete
- **Othello (4.9):** PSPACE-complete
- **Amazons (4.13):** PSPACE-complete
- **Konane (4.14):** PSPACE-complete
- **Phutball (4.15):** "Mate in 1" problem is NP-complete
- **Jenga (4.17):** Completely solved with explicit winning strategy characterization

---

### النسخة العربية (المقدمة)

العديد من الألعاب ذات اللاعبين ذات الطول المحدود هي مكتملة من نوع PSPACE. هذا طبيعي إلى حد ما لأن الألعاب مرتبطة ارتباطاً وثيقاً بالتعبيرات المنطقية مع الكميات المتناوبة (التي يعتبر تحديد استيفائها مكتملاً من نوع PSPACE): يوجد حركة لليسار بحيث، لجميع حركات اليمين، توجد حركة أخرى لليسار، إلخ. نتيجة الاكتمال من نوع PSPACE لها عواقب اثنتان. أولاً، الانتماء إلى PSPACE يعني أن اللعبة يمكن لعبها بشكل مثالي، وعادةً يمكن تعداد جميع المواقع، باستخدام وقت أسي محتمل ولكن مساحة متعددة الحدود فقط. وبالتالي فإن هذه الألعاب تصلح لبحث شامل معقول إلى حد ما للأحجام الصغيرة بما فيه الكفاية. ثانياً، لا يمكن حل الألعاب في وقت متعدد الحدود ما لم يكن P = PSPACE، وهو "أقل احتمالاً" حتى من مساواة P لـ NP.

من ناحية أخرى، الألعاب ذات اللاعبين ذات الطول غير المحدود غالباً ما تكون مكتملة من نوع EXPTIME. مثل هذه النتيجة هي واحدة من الأنواع القليلة من الحدود الدنيا الحقيقية في نظرية التعقيد، مما يعني أن جميع الخوارزميات تتطلب وقتاً أسياً في أسوأ الحالات.

في هذا القسم نستعرض بإيجاز العديد من نتائج التعقيد هذه والنتائج الإيجابية ذات الصلة.

**4.1 Hex**

Hex هي لعبة صممها Piet Hein وتُلعب على لوحة سداسية على شكل ماس. يتناوب اللاعبون ملء السداسيات الفارغة بلونهم. هدف اللاعب هو ربط الجانبين المتقابلين من لونهم بسداسيات من لونهم. لا يمكن أن تنتهي لعبة Hex بالتعادل أبداً.

أثبت John Nash أن اللاعب الأول الذي يتحرك يمكنه الفوز باستخدام حجة سرقة الاستراتيجية (انظر القسم 2.3). ومع ذلك، لا يزال من المفتوح إعطاء توصيف متعدد الحدود لاستراتيجية فوز للاعب الأول.

في ربما أول نتيجة صعوبة PSPACE للألعاب "المثيرة للاهتمام"، أثبت Even وTarjan أن تعميم Hex للرسوم البيانية هو مكتمل من نوع PSPACE، حتى للرسوم البيانية ذات الدرجة القصوى 5. بعد بضع سنوات، أثبت Reisch النتيجة الأقوى أن تحديد نتيجة موقع في Hex هو مكتمل من نوع PSPACE على لوحة عادية على شكل ماس.

**4.2 المزيد من الألعاب على الرسوم البيانية: Kayles، Snort، Geography، Peek، والهاملتونية التفاعلية**

**Kayles:** لعبة محايدة حيث يقوم اللاعبون بإزالة دبوس واحد أو دبوسين متجاورين. يمكن حل Kayles في وقت متعدد الحدود باستخدام نظرية Sprague-Grundy.

**Node Kayles:** تعميم Kayles للرسوم البيانية حيث تزيل كل "كرة بولينغ" رأساً مرغوباً وجميع رؤوسه المجاورة. أثبت Schaefer أن تحديد نتيجة هذه اللعبة هو مكتمل من نوع PSPACE.

**Geography:** عائلة لعبة رسم بياني تتكون من رسم بياني موجه مع عقدة واحدة تحتوي في البداية على رمز. يتناوب اللاعبون تحريك الرمز على طول حافة موجهة. في Edge Geography، يتم مسح تلك الحافة بعد ذلك؛ في Vertex Geography، يتم مسح الرأس الذي تم التحرك منه. أثبت Schaefer أن Edge Geography هي مكتملة من نوع PSPACE؛ وأظهر Lichtenstein وSipser أن Vertex Geography هي أيضاً مكتملة من نوع PSPACE.

**Peek و Interactive Hamiltonicity:** أول ألعاب تم إثباتها على أنها صعبة من نوع EXPTIME بواسطة Stockmeyer وChandra.

**4.3 ألعاب المطاردة: Annihilation، Remove، Capture، Contrajunctive، Blocking، Target، وCops and Robbers**

**Annihilation (المحايدة):** يمكن لعبها بشكل مثالي في O(n⁶) من الوقت (Fraenkel وYesha).

**Annihilation (مع أنواع رموز متعددة):** مكتملة من نوع PSPACE للرسوم البيانية اللادورية؛ التعقيد الدقيق للرسوم البيانية الدورية لا يزال مفتوحاً.

**Capture:** نسخة حزبية من Annihilation؛ مكتملة من نوع EXPTIME للرسوم البيانية العامة، مكتملة من نوع PSPACE للرسوم البيانية اللادورية.

**Target:** تعميم Node Blocking؛ مكتملة من نوع EXPTIME.

**Pursuit (Cops and Robbers):** لاعب واحد (اللص) لديه رمز واحد؛ اللاعب الآخر (الشرطة) لديه k رموز. في حالة شرطي واحد (k = 1)، هناك خوارزمية بسيطة في وقت متعدد الحدود؛ بشكل عام، العديد من إصدارات اللعبة مكتملة من نوع EXPTIME.

**4.4 الداما (Checkers/Draughts)**

لعبة الداما القياسية 8×8 محدودة وبالتالي يمكن لعبها بشكل مثالي في وقت ثابت (نظرياً). في الواقع، حسب Schaeffer وآخرون مؤخراً أن اللعب المثالي يؤدي إلى التعادل من التكوين الأولي. من ناحية أخرى، تحديد نتيجة تكوين تعسفي هو صعب من نوع PSPACE. بدون قيد متعدد الحدود على عدد الحركات، الداما مكتملة من نوع EXPTIME.

**4.5 Go**

أثبت Lichtenstein وSipser أن لعبة Go الآسيوية الكلاسيكية هي أيضاً صعبة من نوع PSPACE لتكوين تعسفي على لوحة n×n. أثبت Robson أن Go مكتملة من نوع EXPTIME بموجب القواعد اليابانية عندما يتم استخدام kos. بالنسبة لمجموعات القواعد الأخرى، كل ما هو معروف هو أن Go صعبة من نوع PSPACE وفي EXPSPACE.

**4.6 Five-in-a-Row (Gobang)**

لعبة على لوحة Go حيث يتناوب اللاعبون وضع حجر من لونهم. الهدف هو وضع 5 أحجار على الأقل من لونهم في صف أفقياً أو عمودياً أو قطرياً. أثبت Reisch أن تحديد نتيجة موقع Gobang هو مكتمل من نوع PSPACE.

**4.7 الشطرنج (Chess)**

أثبت Fraenkel وLichtenstein أن تعميم لعبة الشطرنج الكلاسيكية إلى لوحات n×n هو مكتمل من نوع EXPTIME.

**4.8 Shogi**

Shogi هي لعبة يابانية على غرار الشطرنج. أثبت Adachi وKamekawa وIwata أن تحديد نتيجة موقع Shogi هو مكتمل من نوع EXPTIME.

**4.9 Othello (Reversi)**

Othello هي لعبة كلاسيكية على لوحة 8×8. معممة إلى لوحة n×n مع تكوين أولي تعسفي، اللعبة بوضوح في PSPACE. علاوة على ذلك، أثبت Iwata وKasai أن اللعبة مكتملة من نوع PSPACE.

**4.10 Hackenbush**

Hackenbush هو أحد الأمثلة القياسية للعبة توافقية. الفصل 7 من Winning Ways يثبت أن تحديد قيمة موقع Hackenbush الأحمر-الأزرق هو صعب من نوع NP.

**4.11 Domineering (Crosscram) وCram**

Domineering هي لعبة حزبية تتضمن وضع دومينو أفقي وعمودي في شبكة. التعقيد لا يزال مفتوحاً. Cram هو الإصدار المحايد من Domineering. نتيجة Cram سهلة التحديد للمستطيلات ذات عدد زوجي من المربعات. تعقيد Cram للوحات العامة لا يزال مفتوحاً أيضاً.

**4.12 Dots-and-Boxes، Strings-and-Coins، وNimstring**

Dots-and-Boxes هي لعبة أطفال معروفة جيداً حيث يتناوب اللاعبون رسم حواف أفقية وعمودية تربط أزواج النقاط في مجموعة فرعية m×n من الشبكة. Winning Ways يجادل بأن Strings-and-Coins صعبة من نوع NP. يظل مفتوحاً ما إذا كانت Dots-and-Boxes أو Strings-and-Coins في NP أو مكتملة من نوع PSPACE من تكوين تعسفي.

**4.13 Amazons**

Amazons هي لعبة اخترعها Walter Zamkauskas في 1988، تحتوي على عناصر من الشطرنج وGo. أثبت Furtak وKiyomi وTakeaki وBuro (ومستقل Hearn) أن Amazons مكتملة من نوع PSPACE.

**4.14 Konane**

Konane، أو الداما الهاوائية، هي لعبة تُلعب في هاواي منذ العصور ما قبل القراءة. أثبت Hearn أن Konane مكتملة من نوع PSPACE من خلال اختزال من المنطق القيدي.

**4.15 Phutball**

لعبة كرة قدم الفلاسفة لـ Conway أو Phutball تتضمن أحجار بيضاء وسوداء على شبكة مستطيلة. Phutball حلقية بطبيعتها وليس من الواضح أن أي لاعب لديه استراتيجية فوز. ومع ذلك، أثبت Demaine وDemaine وEppstein أن تحديد ما إذا كان اللاعب الحالي يمكنه الفوز في حركة واحدة ("كش مات في 1") هو مكتمل من نوع NP.

**4.16 مشكلة الملاك لـ Conway**

كانت مشكلة مفتوحة طويلة الأمد سابقاً. مؤخراً، أثبتت أربعة براهين مستقلة أن ملاكاً قوياً بما فيه الكفاية يمكنه التحرك إلى الأبد، مما يضمن الملاك كفائز. أظهر Máthé وKloster أن k = 2 يكفي؛ أظهر Bowditch أن k = 4 يكفي؛ وأظهر Gács أن بعض k يكفي.

**4.17 Jenga**

Jenga هي لعبة كتل مكدسة شعبية. أثبت Zwick أن شرط الاستقرار الفيزيائي لـ Jenga يمكن إعادة صياغته تجميعياً. باستخدام هذا التوصيف، يثبت Zwick أن اللاعب الأول يفوز من التكوين الأولي إذا وفقط إذا كان n = 2 أو n ≥ 4 و n ≡ 1 أو 2 (mod 3)، ويعطي توصيفاً بسيطاً للحركات الفائزة.

---

### Translation Notes

- **Figures referenced:** Figures 1-9 showing game positions and moves
- **Key terms introduced:** PSPACE-complete, EXPTIME-complete, strategy stealing, bounded/unbounded games, planar graphs, Hamiltonian cycle, endgame analysis
- **Game names:** Kept in English as proper nouns with Arabic descriptions
- **Mathematical notation:** Preserved complexity classes, Big-O notation, modular arithmetic
- **Citations:** All references maintained in English format
- **Special handling:** Technical game terminology and complexity results carefully translated to maintain precision

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.89
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.86
