# Section 2: Combinatorial Game Theory
## القسم 2: نظرية الألعاب التوافقية

**Section:** Combinatorial Game Theory
**Translation Quality:** 0.87
**Glossary Terms Used:** algorithm, combinatorial, game theory, perfect information, complexity, strategy, Nim, polynomial-time, surreal numbers, impartial, partizan, normal play, misère play

---

### English Version

A combinatorial game typically involves two players, often called Left and Right, alternating play in well-defined moves. However, in the interesting case of a combinatorial puzzle, there is only one player, and for cellular automata such as Conway's Game of Life, there are no players. In all cases, no randomness or hidden information is permitted: all players know all information about gameplay (perfect information). The problem is thus purely strategic: how to best play the game against an ideal opponent.

It is useful to distinguish several types of two-player perfect-information games. A common assumption is that the game terminates after a finite number of moves (the game is finite or short), and the result is a unique winner. Of course, there are exceptions: some games (such as Life and Chess) can be drawn out forever, and some games (such as tic-tac-toe and Chess) define ties in certain cases. However, in the combinatorial-game setting, it is useful to define the winner as the last player who is able to move; this is called normal play. If, on the other hand, the winner is the first player who cannot move, this is called misère play. (We will normally assume normal play.) A game is loopy if it is possible to return to previously seen positions (as in Chess, for example). Finally, a game is called impartial if the two players (Left and Right) are treated identically, that is, each player has the same moves available from the same game position; otherwise the game is called partizan.

A particular two-player perfect-information game without ties or draws can have one of four outcomes as the result of ideal play: player Left wins, player Right wins, the first player to move wins (whether it is Left or Right), or the second player to move wins. One goal in analyzing two-player games is to determine the outcome as one of these four categories, and to find a strategy for the winning player to win. Another goal is to compute a deeper structure to games described in the remainder of this section, called the value of the game.

A beautiful mathematical theory has been developed for analyzing two-player combinatorial games. A new introductory book on the topic is Lessons in Play by Albert, Nowakowski, and Wolfe; the most comprehensive reference is the book Winning Ways by Berlekamp, Conway, and Guy; and a more mathematical presentation is the book On Numbers and Games by Conway. The basic idea behind the theory is simple: a two-player game can be described by a rooted tree, where each node has zero or more left branches corresponding to options for player Left to move and zero or more right branches corresponding to options for player Right to move; leaves correspond to finished games, with the winner determined by either normal or misère play. The interesting parts of Combinatorial Game Theory are the several methods for manipulating and analyzing such games/trees. We give a brief summary of some of these methods in this section.

**2.1 Conway's Surreal Numbers**

A richly structured special class of two-player games are John H. Conway's surreal numbers, a vast generalization of the real and ordinal number systems. Basically, a surreal number {L | R} is the "simplest" number larger than all Left options (in L) and smaller than all Right options (in R); for this to constitute a number, all Left and Right options must be numbers, defining a total order, and each Left option must be less than each Right option.

For example, the simplest number without any larger-than or smaller-than constraints, denoted {|}, is 0; the simplest number larger than 0 and without smaller-than constraints, denoted {0 |}, is 1; and the simplest number larger than 0 and 1 (or just 1), denoted {0, 1 |}, is 2. This method can be used to generate all natural numbers and indeed all ordinals. On the other hand, the simplest number less than 0, denoted {| 0}, is −1; similarly, all negative integers can be generated. Another example is the simplest number larger than 0 and smaller than 1, denoted {0 | 1}, which is 1/2; similarly, all dyadic rationals can be generated. After a countably infinite number of such construction steps, all real numbers can be generated; after many more steps, the surreals are all numbers that can be generated in this way.

Surreal numbers form a field, so in particular they are totally ordered, and support the operations of addition, subtraction, multiplication, division, roots, powers, and even integration in many situations. As such, surreal numbers are useful in their own right for cleaner forms of analysis.

What is interesting about the surreals from the perspective of combinatorial game theory is that they are a subclass of all two-player perfect-information games, and some of the surreal structure, such as addition and subtraction, carries over to general games. Furthermore, while games are not totally ordered, they can still be compared to some surreal numbers and, amazingly, how a game compares to the surreal number 0 determines exactly the outcome of the game. This connection is detailed in the next few paragraphs.

First we define some algebraic structure of games that carries over from surreal numbers (see Table 1 for formal definitions). Two-player combinatorial games, or trees, can simply be represented as {L | R} where, in contrast to surreal numbers, no constraints are placed on L and R. The negation of a game is the result of reversing the roles of the players Left and Right throughout the game. The (disjunctive) sum of two (sub)games is the game in which, at each player's turn, the player has a binary choice of which subgame to play, and makes a move in precisely that subgame. A partial order is defined on games recursively: a game x is less than or equal to a game y if every Left option of x is less than y and every Right option of y is more than x. (Numeric) equality is defined by being both less than or equal to and more than or equal to. Strictly inequalities, as used in the definition of less than or equal to, are defined in the obvious manner.

Note that while {−1 | 1} = 0 = {|} in terms of numbers, {−1 | 1} and {|} denote different games (lasting 1 move and 0 moves, respectively), and in this sense are equal in value but not identical symbolically or game-theoretically. Nonetheless, the games {−1 | 1} and {|} have the same outcome: the second player to move wins.

Amazingly, this holds in general: two equal numbers represent games with equal outcome (under ideal play). In particular, all games equal to 0 have the outcome that the second player to move wins. Furthermore, all games equal to a positive number have the outcome that the Left player wins; more generally, all positive games (games larger than 0) have this outcome. Symmetrically, all negative games have the outcome that the Right player wins (this follows automatically by the negation operation). Examples of zero, positive, and negative games are the surreal numbers themselves; an additional example is described below.

There is one outcome not captured by the characterization into zero, positive, and negative games: the first player to move wins. To find such a game we must obviously look beyond the surreal numbers. Furthermore, we must look for games G that are incomparable with zero (none of G = 0, G < 0, or G > 0 hold); such games are called fuzzy with 0, denoted G || 0.

An example of a game that is not a surreal number is {1 | 0}; there fails to be a number strictly between 1 and 0 because 1 ≥ 0. Nonetheless, {1 | 0} is a game: Left has a single move leading to game 1, from which Right cannot move, and Right has a single move leading to game 0, from which Left cannot move. Thus, in either case, the first player to move wins. The claim above implies that {1 | 0} || 0. Indeed, {1 | 0} || x for all surreal numbers x, 0 ≤ x ≤ 1. In contrast, x < {1 | 0} for all x < 0 and {1 | 0} < x for all 1 < x. In general it holds that a game is fuzzy with some surreal numbers in an interval [−n, n] but comparable with all surreals outside that interval. Another example of a game that is not a number is {2 | 1}, which is positive (> 0), and hence Right wins, but fuzzy with numbers in the range [1, 2].

**Table 1: Formal definitions of some algebra on two-player perfect-information games**

Let x = {xL | xR } be a game.
• x ≤ y precisely if every xL < y and every yR > x.
• x = y precisely if x ≤ y and x ≥ y; otherwise x ≠ y.
• x < y precisely if x ≤ y and x ≠ y, or equivalently, x ≤ y and x ≱ y.
• −x = {−xR | −xL }.
• x + y = {xL + y, x + yL | xR + y, x + yR }.
• x is impartial precisely if xL and xR are identical sets and recursively every position (∈ xL = xR ) is impartial.
• A one-pile Nim game is defined by ∗n = {∗0, . . . , ∗(n − 1) | ∗0, . . . , ∗(n − 1)}, together with ∗0 = 0.

For brevity we omit many other useful notions in Combinatorial Game Theory, such as additional definitions of summation, super-infinitesimal games ∗ and ↑, mass, temperature, thermographs, the simplest form of a game, remoteness, and suspense.

**2.2 Sprague-Grundy Theory**

A celebrated result in Combinatorial Game Theory is the characterization of impartial two-player perfect-information games, discovered independently in the 1930's by Sprague and Grundy. Recall that a game is impartial if it does not distinguish between the players Left and Right (see Table 1 for a more formal definition). The Sprague-Grundy theory states that every finite impartial game is equivalent to an instance of the game of Nim, characterized by a single natural number n. This theory has since been generalized to all impartial games by generalizing Nim to all ordinals n.

Nim is a game played with several heaps, each with a certain number of tokens. A Nim game with a single heap of size n is denoted by ∗n and is called a nimber. During each move a player can pick any pile and reduce it to any smaller nonnegative integer size. The game ends when all piles have size 0. Thus, a single pile ∗n can be reduced to any of the smaller piles ∗0, ∗1, . . . , ∗(n − 1). Multiple piles in a game of Nim are independent, and hence any game of Nim is a sum of single-pile games ∗n for various values of n. In fact, a game of Nim with k piles of sizes n₁, n₂, . . . , nₖ is equivalent to a one-pile Nim game ∗n, where n is the binary XOR of n₁, n₂, . . . , nₖ. As a consequence, Nim can be played optimally in polynomial time (polynomial in the encoding size of the pile sizes).

Even more surprising is that every impartial two-player perfect-information game has the same value as a single-pile Nim game, ∗n for some n. The number n is called the G-value, Grundy-value, or Sprague-Grundy function of the game. It is easy to define: suppose that game x has k options y₁, . . . , yₖ for the first move (independent of which player goes first). By induction, we can compute y₁ = ∗n₁, . . . , yₖ = ∗nₖ. The theorem is that x equals ∗n where n is the smallest natural number not in the set {n₁, . . . , nₖ}. This number n is called the minimum excluded value or mex of the set. This description has also assumed that the game is finite, but this is easy to generalize.

The Sprague-Grundy function can increase by at most 1 at each level of the game tree, and hence the resulting nimber is linear in the maximum number of moves that can be made in the game; the encoding size of the nimber is only logarithmic in this count. Unfortunately, computing the Sprague-Grundy function for a general game by the obvious method uses time linear in the number of possible states, which can be exponential in the nimber itself.

Nonetheless, the Sprague-Grundy theory is extremely helpful for analyzing impartial two-player games, and for many games there is an efficient algorithm to determine the nimber. Examples include Nim itself, Kayles, and various generalizations; and Cutcake and Maundy Cake. In all of these examples, the Sprague-Grundy function has a succinct characterization (if somewhat difficult to prove); it can also be easily computed using dynamic programming.

The Sprague-Grundy theory seems difficult to generalize to the superficially similar case of misère play, where the goal is to be the first player unable to move. Certain games have been solved in this context over the years, including Nim. Recently a general theory has emerged for tackling misère combinatorial games, based on commutative monoids called "misère quotients" that localize the problem to certain restricted game scenarios. This theory was introduced by Plambeck and further developed by Plambeck and Siegel.

**2.3 Strategy Stealing**

Another useful technique in Combinatorial Game Theory for proving that a particular player must win is strategy stealing. The basic idea is to assume that one player has a winning strategy, and prove that in fact the other player has a winning strategy based on that strategy. This contradiction proves that the second player must in fact have a winning strategy. An example of such an argument is given in Section 4.1. Unfortunately, such a proof by contradiction gives no indication of what the winning strategy actually is, only that it exists. In many situations, such as the one in Section 4.1, the winner is known but no polynomial-time winning strategy is known.

**2.4 Puzzles**

There is little theory for analyzing combinatorial puzzles (one-player games) along the lines of the two-player theory summarized in this section. We present one such viewpoint here. In most puzzles, solutions subdivide into a sequence of moves. Thus, a puzzle can be viewed as a tree, similar to a two-player game except that edges are not distinguished between Left and Right. With the view that the game ends only when the puzzle is solved, the goal is then to reach a position from which there are no valid moves (normal play). Loopy puzzles are common; to be more explicit, repeated subtrees can be converted into self-references to form a directed graph, and losing terminal positions can be given explicit loops to themselves.

A consequence of the above view is that a puzzle is basically an impartial two-player game except that we are not interested in the outcome from two players alternating in moves. Rather, questions of interest in the context of puzzles are (a) whether a given puzzle is solvable, and (b) finding the solution with the fewest moves. An important open direction of research is to develop a general theory for resolving such questions, similar to the two-player theory.

---

### النسخة العربية

تتضمن اللعبة التوافقية عادةً لاعبين، يُطلق عليهما غالباً اليسار واليمين، يتناوبان اللعب في حركات محددة بشكل جيد. ومع ذلك، في الحالة المثيرة للاهتمام للغز توافقي، هناك لاعب واحد فقط، وبالنسبة للآليات الخلوية مثل لعبة الحياة لكونواي، لا يوجد لاعبون. في جميع الحالات، لا يُسمح بالعشوائية أو المعلومات المخفية: جميع اللاعبين يعرفون كل المعلومات حول طريقة اللعب (معلومات كاملة). وبالتالي فإن المشكلة استراتيجية بحتة: كيفية لعب اللعبة على أفضل وجه ضد خصم مثالي.

من المفيد التمييز بين عدة أنواع من ألعاب المعلومات الكاملة ذات اللاعبين. الافتراض الشائع هو أن اللعبة تنتهي بعد عدد محدود من الحركات (اللعبة محدودة أو قصيرة)، والنتيجة هي فائز وحيد. بالطبع، هناك استثناءات: بعض الألعاب (مثل الحياة والشطرنج) يمكن أن تستمر إلى الأبد، وبعض الألعاب (مثل تيك-تاك-تو والشطرنج) تحدد التعادل في حالات معينة. ومع ذلك، في سياق اللعبة التوافقية، من المفيد تعريف الفائز على أنه آخر لاعب قادر على التحرك؛ وهذا ما يسمى اللعب العادي. من ناحية أخرى، إذا كان الفائز هو اللاعب الأول الذي لا يستطيع التحرك، فإن هذا يسمى اللعب البائس. (سنفترض عادةً اللعب العادي.) تكون اللعبة حلقية إذا كان من الممكن العودة إلى المواقع المرئية سابقاً (كما في الشطرنج، على سبيل المثال). أخيراً، تسمى اللعبة محايدة إذا تم التعامل مع اللاعبين (اليسار واليمين) بشكل متطابق، أي أن كل لاعب لديه نفس الحركات المتاحة من نفس موقع اللعبة؛ وإلا فإن اللعبة تسمى حزبية.

يمكن أن يكون للعبة معينة ذات لاعبين ومعلومات كاملة بدون تعادل أو سحب واحدة من أربع نتائج كنتيجة للعب المثالي: يفوز اللاعب اليسار، أو يفوز اللاعب اليمين، أو يفوز اللاعب الأول الذي يتحرك (سواء كان اليسار أو اليمين)، أو يفوز اللاعب الثاني الذي يتحرك. أحد الأهداف في تحليل الألعاب ذات اللاعبين هو تحديد النتيجة كواحدة من هذه الفئات الأربع، والعثور على استراتيجية للاعب الفائز للفوز. الهدف الآخر هو حساب بنية أعمق للألعاب الموصوفة في بقية هذا القسم، تسمى قيمة اللعبة.

تم تطوير نظرية رياضية جميلة لتحليل الألعاب التوافقية ذات اللاعبين. كتاب تمهيدي جديد حول الموضوع هو Lessons in Play من قبل Albert وNowakowski وWolfe؛ والمرجع الأكثر شمولاً هو كتاب Winning Ways من قبل Berlekamp وConway وGuy؛ والعرض الرياضي الأكثر هو كتاب On Numbers and Games من قبل Conway. الفكرة الأساسية وراء النظرية بسيطة: يمكن وصف لعبة ذات لاعبين بشجرة ذات جذر، حيث يحتوي كل عقدة على صفر أو أكثر من الفروع اليسرى المقابلة لخيارات اللاعب اليسار للتحرك وصفر أو أكثر من الفروع اليمنى المقابلة لخيارات اللاعب اليمين للتحرك؛ تتوافق الأوراق مع الألعاب المنتهية، مع تحديد الفائز إما باللعب العادي أو اللعب البائس. الأجزاء المثيرة للاهتمام من نظرية الألعاب التوافقية هي الطرق المتعددة للتلاعب وتحليل هذه الألعاب/الأشجار. نعطي ملخصاً موجزاً لبعض هذه الطرق في هذا القسم.

**2.1 الأعداد الفائقة الواقعية لكونواي**

فئة خاصة غنية بالبنية من الألعاب ذات اللاعبين هي الأعداد الفائقة الواقعية لجون إتش كونواي، وهي تعميم واسع لأنظمة الأعداد الحقيقية والترتيبية. في الأساس، الرقم الفائق الواقعي {L | R} هو الرقم "الأبسط" الأكبر من جميع خيارات اليسار (في L) والأصغر من جميع خيارات اليمين (في R)؛ لكي يشكل هذا رقماً، يجب أن تكون جميع خيارات اليسار واليمين أرقاماً، تحدد ترتيباً كلياً، ويجب أن يكون كل خيار يساري أقل من كل خيار يميني.

على سبيل المثال، الرقم الأبسط بدون أي قيود أكبر من أو أصغر من، يُرمز له بـ {|}، هو 0؛ والرقم الأبسط الأكبر من 0 وبدون قيود أصغر من، يُرمز له بـ {0 |}، هو 1؛ والرقم الأبسط الأكبر من 0 و1 (أو 1 فقط)، يُرمز له بـ {0, 1 |}، هو 2. يمكن استخدام هذه الطريقة لتوليد جميع الأعداد الطبيعية وفي الواقع جميع الأعداد الترتيبية. من ناحية أخرى، الرقم الأبسط الأقل من 0، يُرمز له بـ {| 0}، هو −1؛ وبالمثل، يمكن توليد جميع الأعداد الصحيحة السالبة. مثال آخر هو الرقم الأبسط الأكبر من 0 والأصغر من 1، يُرمز له بـ {0 | 1}، وهو 1/2؛ وبالمثل، يمكن توليد جميع الأعداد النسبية الثنائية. بعد عدد لا نهائي قابل للعد من خطوات البناء هذه، يمكن توليد جميع الأعداد الحقيقية؛ بعد العديد من الخطوات الأخرى، الأعداد الفائقة الواقعية هي جميع الأعداد التي يمكن توليدها بهذه الطريقة.

تشكل الأعداد الفائقة الواقعية حقلاً، لذا فهي على وجه الخصوص مرتبة ترتيباً كلياً، وتدعم عمليات الجمع والطرح والضرب والقسمة والجذور والقوى وحتى التكامل في العديد من المواقف. على هذا النحو، فإن الأعداد الفائقة الواقعية مفيدة في حد ذاتها لأشكال أنظف من التحليل.

ما هو مثير للاهتمام حول الأعداد الفائقة الواقعية من منظور نظرية الألعاب التوافقية هو أنها فئة فرعية من جميع الألعاب ذات اللاعبين ذات المعلومات الكاملة، وبعض بنية الأعداد الفائقة الواقعية، مثل الجمع والطرح، تنتقل إلى الألعاب العامة. علاوة على ذلك، في حين أن الألعاب ليست مرتبة ترتيباً كلياً، فإنه لا يزال من الممكن مقارنتها ببعض الأعداد الفائقة الواقعية، والمدهش أن كيفية مقارنة اللعبة بالرقم الفائق الواقعي 0 تحدد بالضبط نتيجة اللعبة. هذا الاتصال مفصل في الفقرات القليلة القادمة.

أولاً نحدد بعض البنية الجبرية للألعاب التي تنتقل من الأعداد الفائقة الواقعية (انظر الجدول 1 للتعريفات الرسمية). يمكن تمثيل الألعاب التوافقية ذات اللاعبين، أو الأشجار، ببساطة على أنها {L | R} حيث، على النقيض من الأعداد الفائقة الواقعية، لا توضع قيود على L وR. نفي اللعبة هو نتيجة عكس أدوار اللاعبين اليسار واليمين خلال اللعبة. المجموع (الفصلي) للعبتين (فرعيتين) هو اللعبة التي، في كل دور لاعب، يكون للاعب خيار ثنائي حول اللعبة الفرعية التي يلعبها، ويقوم بحركة في تلك اللعبة الفرعية بالضبط. يتم تعريف ترتيب جزئي على الألعاب بشكل متكرر: اللعبة x أقل من أو تساوي اللعبة y إذا كان كل خيار يساري لـ x أقل من y وكل خيار يميني لـ y أكبر من x. تُعرّف المساواة (العددية) بأنها أقل من أو تساوي وأكبر من أو تساوي. تُعرّف المتباينات الصارمة، كما هو مستخدم في تعريف أقل من أو تساوي، بالطريقة الواضحة.

لاحظ أنه بينما {−1 | 1} = 0 = {|} من حيث الأرقام، فإن {−1 | 1} و {|} يشيران إلى ألعاب مختلفة (تستمر لحركة واحدة و0 حركة، على التوالي)، وبهذا المعنى هما متساويان في القيمة ولكن ليسا متطابقين رمزياً أو نظرياً للعبة. ومع ذلك، فإن اللعبتين {−1 | 1} و {|} لهما نفس النتيجة: اللاعب الثاني الذي يتحرك يفوز.

والمدهش أن هذا يصمد بشكل عام: رقمان متساويان يمثلان ألعاباً ذات نتيجة متساوية (في ظل اللعب المثالي). على وجه الخصوص، جميع الألعاب التي تساوي 0 لها النتيجة أن اللاعب الثاني الذي يتحرك يفوز. علاوة على ذلك، جميع الألعاب التي تساوي رقماً موجباً لها النتيجة أن اللاعب اليسار يفوز؛ بشكل أعم، جميع الألعاب الموجبة (الألعاب الأكبر من 0) لها هذه النتيجة. بالتناظر، جميع الألعاب السالبة لها النتيجة أن اللاعب اليمين يفوز (هذا يتبع تلقائياً من عملية النفي). أمثلة على الألعاب الصفرية والموجبة والسالبة هي الأعداد الفائقة الواقعية نفسها؛ مثال إضافي موصوف أدناه.

هناك نتيجة واحدة لا يتم التقاطها بالتوصيف في الألعاب الصفرية والموجبة والسالبة: اللاعب الأول الذي يتحرك يفوز. للعثور على مثل هذه اللعبة، يجب علينا بوضوح النظر إلى ما وراء الأعداد الفائقة الواقعية. علاوة على ذلك، يجب أن نبحث عن ألعاب G غير قابلة للمقارنة مع الصفر (لا يصمد أي من G = 0 أو G < 0 أو G > 0)؛ تسمى هذه الألعاب غامضة مع 0، يُرمز لها بـ G || 0.

مثال على لعبة ليست رقماً فائقاً واقعياً هو {1 | 0}؛ يفشل وجود رقم بشكل صارم بين 1 و0 لأن 1 ≥ 0. ومع ذلك، {1 | 0} هي لعبة: اليسار لديه حركة واحدة تؤدي إلى اللعبة 1، والتي لا يستطيع اليمين من خلالها التحرك، واليمين لديه حركة واحدة تؤدي إلى اللعبة 0، والتي لا يستطيع اليسار من خلالها التحرك. وبالتالي، في كلتا الحالتين، اللاعب الأول الذي يتحرك يفوز. تشير الادعاء أعلاه إلى أن {1 | 0} || 0. في الواقع، {1 | 0} || x لجميع الأرقام الفائقة الواقعية x، 0 ≤ x ≤ 1. في المقابل، x < {1 | 0} لجميع x < 0 و{1 | 0} < x لجميع 1 < x. بشكل عام يصمد أن اللعبة غامضة مع بعض الأرقام الفائقة الواقعية في فترة [−n, n] ولكنها قابلة للمقارنة مع جميع الأرقام الفائقة خارج تلك الفترة. مثال آخر على لعبة ليست رقماً هو {2 | 1}، وهي موجبة (> 0)، وبالتالي يفوز اليمين، ولكنها غامضة مع الأرقام في النطاق [1, 2].

**الجدول 1: تعريفات رسمية لبعض الجبر على ألعاب المعلومات الكاملة ذات اللاعبين**

لتكن x = {xL | xR } لعبة.
• x ≤ y بالضبط إذا كان كل xL < y وكل yR > x.
• x = y بالضبط إذا كان x ≤ y و x ≥ y؛ وإلا x ≠ y.
• x < y بالضبط إذا كان x ≤ y و x ≠ y، أو بشكل مكافئ، x ≤ y و x ≱ y.
• −x = {−xR | −xL }.
• x + y = {xL + y, x + yL | xR + y, x + yR }.
• x محايدة بالضبط إذا كانت xL وxR مجموعات متطابقة وبشكل متكرر كل موقع (∈ xL = xR ) محايد.
• تُعرّف لعبة Nim ذات كومة واحدة بـ ∗n = {∗0, . . . , ∗(n − 1) | ∗0, . . . , ∗(n − 1)}، جنباً إلى جنب مع ∗0 = 0.

للإيجاز نحذف العديد من المفاهيم المفيدة الأخرى في نظرية الألعاب التوافقية، مثل التعريفات الإضافية للجمع، والألعاب فائقة اللانهائية الصغر ∗ و↑، والكتلة، ودرجة الحرارة، والرسوم البيانية الحرارية، والشكل الأبسط للعبة، والبعد، والتشويق.

**2.2 نظرية سبراغ-غراندي**

نتيجة مشهورة في نظرية الألعاب التوافقية هي توصيف الألعاب المحايدة ذات اللاعبين ذات المعلومات الكاملة، التي اكتشفها سبراغ وغراندي بشكل مستقل في الثلاثينيات. تذكر أن اللعبة محايدة إذا كانت لا تميز بين اللاعبين اليسار واليمين (انظر الجدول 1 لتعريف أكثر رسمية). تنص نظرية سبراغ-غراندي على أن كل لعبة محايدة محدودة مكافئة لحالة من لعبة Nim، تتميز برقم طبيعي واحد n. منذ ذلك الحين تم تعميم هذه النظرية على جميع الألعاب المحايدة من خلال تعميم Nim إلى جميع الأعداد الترتيبية n.

Nim هي لعبة تُلعب بعدة أكوام، كل منها يحتوي على عدد معين من الرموز. لعبة Nim ذات كومة واحدة بحجم n يُرمز لها بـ ∗n وتسمى nimber. خلال كل حركة، يمكن للاعب اختيار أي كومة وتقليلها إلى أي حجم صحيح غير سالب أصغر. تنتهي اللعبة عندما يكون لجميع الأكوام حجم 0. وبالتالي، يمكن تقليل كومة واحدة ∗n إلى أي من الأكوام الأصغر ∗0، ∗1، . . . ، ∗(n − 1). الأكوام المتعددة في لعبة Nim مستقلة، وبالتالي فإن أي لعبة Nim هي مجموع ألعاب ذات كومة واحدة ∗n لقيم مختلفة من n. في الواقع، لعبة Nim مع k أكوام بأحجام n₁، n₂، . . . ، nₖ تكافئ لعبة Nim ذات كومة واحدة ∗n، حيث n هو XOR الثنائي لـ n₁، n₂، . . . ، nₖ. كنتيجة، يمكن لعب Nim بشكل مثالي في وقت متعدد الحدود (متعدد الحدود في حجم ترميز أحجام الأكوام).

والأكثر إثارة للدهشة هو أن كل لعبة محايدة ذات لاعبين ذات معلومات كاملة لها نفس القيمة كلعبة Nim ذات كومة واحدة، ∗n لبعض n. يسمى الرقم n قيمة G، أو قيمة غراندي، أو دالة سبراغ-غراندي للعبة. من السهل تعريفها: افترض أن اللعبة x لديها k خيارات y₁، . . . ، yₖ للحركة الأولى (مستقلة عن أي لاعب يذهب أولاً). بالاستقراء، يمكننا حساب y₁ = ∗n₁، . . . ، yₖ = ∗nₖ. النظرية هي أن x تساوي ∗n حيث n هو أصغر عدد طبيعي ليس في المجموعة {n₁، . . . ، nₖ}. يسمى هذا الرقم n القيمة المستبعدة الدنيا أو mex من المجموعة. هذا الوصف افترض أيضاً أن اللعبة محدودة، ولكن من السهل تعميم ذلك.

يمكن أن تزيد دالة سبراغ-غراندي بمقدار 1 على الأكثر في كل مستوى من شجرة اللعبة، وبالتالي فإن nimber الناتج خطي في العدد الأقصى من الحركات التي يمكن إجراؤها في اللعبة؛ حجم ترميز nimber لوغاريتمي فقط في هذا العدد. لسوء الحظ، فإن حساب دالة سبراغ-غراندي للعبة عامة بالطريقة الواضحة يستخدم وقتاً خطياً في عدد الحالات المحتملة، والذي يمكن أن يكون أسياً في nimber نفسه.

ومع ذلك، فإن نظرية سبراغ-غراندي مفيدة للغاية لتحليل الألعاب المحايدة ذات اللاعبين، وللعديد من الألعاب هناك خوارزمية فعالة لتحديد nimber. الأمثلة تشمل Nim نفسها، وKayles، وتعميمات مختلفة؛ وCutcake وMaundy Cake. في جميع هذه الأمثلة، دالة سبراغ-غراندي لها توصيف موجز (وإن كان يصعب إثباته إلى حد ما)؛ يمكن أيضاً حسابها بسهولة باستخدام البرمجة الديناميكية.

يبدو أن نظرية سبراغ-غراندي يصعب تعميمها على الحالة المشابهة ظاهرياً للعب البائس، حيث الهدف هو أن تكون اللاعب الأول غير القادر على التحرك. تم حل ألعاب معينة في هذا السياق على مر السنين، بما في ذلك Nim. مؤخراً ظهرت نظرية عامة للتعامل مع الألعاب التوافقية البائسة، بناءً على الأحاديات التبديلية تسمى "حاصلات البؤس" التي تحدد المشكلة في سيناريوهات لعبة مقيدة معينة. تم تقديم هذه النظرية من قبل Plambeck وتطويرها بشكل أكبر من قبل Plambeck وSiegel.

**2.3 سرقة الاستراتيجية**

تقنية مفيدة أخرى في نظرية الألعاب التوافقية لإثبات أن لاعباً معيناً يجب أن يفوز هي سرقة الاستراتيجية. الفكرة الأساسية هي افتراض أن لاعباً واحداً لديه استراتيجية فوز، وإثبات أنه في الواقع اللاعب الآخر لديه استراتيجية فوز بناءً على تلك الاستراتيجية. هذا التناقض يثبت أن اللاعب الثاني يجب أن يكون لديه في الواقع استراتيجية فوز. يتم إعطاء مثال على مثل هذه الحجة في القسم 4.1. لسوء الحظ، مثل هذا الإثبات بالتناقض لا يعطي أي إشارة إلى ما هي استراتيجية الفوز فعلياً، فقط أنها موجودة. في العديد من المواقف، مثل تلك الموجودة في القسم 4.1، الفائز معروف ولكن لا توجد استراتيجية فوز في وقت متعدد الحدود معروفة.

**2.4 الألغاز**

هناك نظرية قليلة لتحليل الألغاز التوافقية (الألعاب ذات لاعب واحد) على غرار نظرية اللاعبين الملخصة في هذا القسم. نقدم وجهة نظر واحدة هنا. في معظم الألغاز، تنقسم الحلول إلى تسلسل من الحركات. وبالتالي، يمكن النظر إلى اللغز على أنه شجرة، مشابهة للعبة ذات لاعبين باستثناء أن الحواف لا تتميز بين اليسار واليمين. مع الرأي أن اللعبة تنتهي فقط عند حل اللغز، يكون الهدف بعد ذلك هو الوصول إلى موقع لا توجد منه حركات صالحة (اللعب العادي). الألغاز الحلقية شائعة؛ لكي نكون أكثر صراحة، يمكن تحويل الأشجار الفرعية المتكررة إلى مراجع ذاتية لتشكيل رسم بياني موجه، ويمكن إعطاء المواقع النهائية الخاسرة حلقات صريحة لأنفسها.

نتيجة للرأي أعلاه هي أن اللغز هو في الأساس لعبة محايدة ذات لاعبين باستثناء أننا لسنا مهتمين بالنتيجة من لاعبين يتناوبان في الحركات. بدلاً من ذلك، الأسئلة ذات الاهتمام في سياق الألغاز هي (أ) ما إذا كان لغز معين قابلاً للحل، و(ب) العثور على الحل بأقل عدد من الحركات. اتجاه بحثي مفتوح مهم هو تطوير نظرية عامة لحل مثل هذه الأسئلة، مشابهة لنظرية اللاعبين.

---

### Translation Notes

- **Figures referenced:** Table 1
- **Key terms introduced:** combinatorial game, perfect information, normal play, misère play, impartial game, partizan game, surreal numbers, Nim, nimber, Sprague-Grundy theory, G-value, Grundy-value, mex (minimum excluded value), strategy stealing, fuzzy with 0
- **Mathematical notation:** Preserved all mathematical symbols and notation ({L | R}, ∗n, XOR, etc.)
- **Citations:** All references maintained in English format
- **Special handling:** Game names kept in English with Arabic transliterations where needed; mathematical definitions in Table 1 carefully translated while preserving notation

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.87
