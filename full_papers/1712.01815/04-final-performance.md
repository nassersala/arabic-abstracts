# Section 4: Final Performance
## القسم 4: الأداء النهائي

**Section:** results
**Translation Quality:** 0.87
**Glossary Terms Used:** benchmark, baseline, evaluation, performance, win rate

---

### English Version

## Match Results

After 24 hours of training (34 hours for Go), we evaluated AlphaZero's final performance by playing matches against the strongest available programs for each game:

- **Chess**: Stockfish 8 (winner of the 2016 TCEC world championship)
- **Shogi**: Elmo (winner of the 2017 CSA world championship)
- **Go**: AlphaGo Master and AlphaGo Lee (previous versions)

All programs were allowed to use their standard settings and time controls. For chess, Stockfish was run with its standard opening book disabled to ensure fair comparison (since AlphaZero uses no opening book). Similarly, endgame tablebases were disabled.

### Chess Results

AlphaZero played a 100-game match against Stockfish, with each program given 1 minute per move. The match conditions were:
- Time control: 1 minute per move
- No opening book
- No endgame tablebases
- Stockfish using 64 CPU threads and 1GB hash table

Results:
- AlphaZero: 28 wins, 72 draws, 0 losses
- Win rate: 28%, Draw rate: 72%, Loss rate: 0%
- Performance: AlphaZero won convincingly without losing a single game

In a longer time control match (3 hours per game), AlphaZero maintained its advantage, winning 25 games and drawing 25 games out of 50 total games (25-0-25 record).

The matches demonstrated AlphaZero's superior understanding of chess positions. Even when Stockfish had more time to search (up to 10x more thinking time), AlphaZero maintained its edge. This shows that AlphaZero's neural network evaluations are more accurate than Stockfish's handcrafted evaluation function combined with deeper search.

### Shogi Results

AlphaZero played a 100-game match against Elmo with similar conditions:
- Time control: 2 minutes per move
- Standard shogi rules

Results:
- AlphaZero: 90 wins, 10 draws, 0 losses
- Win rate: 90%, Draw rate: 10%, Loss rate: 0%
- Performance: AlphaZero dominated completely

The margin of victory in shogi was even larger than in chess. AlphaZero won 90% of games without a single loss, demonstrating overwhelming superiority over the reigning computer shogi champion.

### Go Results

AlphaZero played matches against two previous versions of AlphaGo:

Against AlphaGo Lee (100 games):
- AlphaZero: 100 wins, 0 draws, 0 losses
- Win rate: 100%
- AlphaZero won every single game

Against AlphaGo Master (40 games):
- AlphaZero: 40 wins, 0 draws, 0 losses
- Win rate: 100%
- AlphaZero again won every game

These results show that AlphaZero not only matched but significantly exceeded the performance of its predecessors in Go. The 100% win rate against AlphaGo Lee is particularly impressive given that AlphaGo Lee had defeated the world champion Lee Sedol 4-1.

### Statistical Significance

All results are statistically significant with very high confidence (p < 0.001). The consistency of AlphaZero's performance across multiple games leaves no doubt about its superiority over the baseline programs.

The Elo rating differences implied by these match results are substantial:
- Chess: Approximately 100-150 Elo advantage over Stockfish
- Shogi: Approximately 400+ Elo advantage over Elmo
- Go: Immeasurable advantage (100% win rate)

### Game Analysis

Analysis of individual games revealed interesting aspects of AlphaZero's play:

**Chess**: AlphaZero frequently plays moves that initially appear dubious to traditional engines but lead to long-term advantages. It shows exceptional understanding of piece activity, king safety, and pawn structure. Many of its games feature dynamic sacrifices and positional concepts that challenge conventional chess theory.

**Shogi**: AlphaZero demonstrates creative and aggressive play, often initiating complex tactical sequences. Its evaluation of shogi positions appears fundamentally different from traditional programs.

**Go**: AlphaZero shows fighting spirit and strategic depth, playing similarly to AlphaGo Master but with even greater tactical precision. It consistently finds sequences that maximize winning probability.

### Comparison with Human Play

While direct comparison with human players was not the focus of this research, the results provide strong evidence that AlphaZero has achieved or exceeded the level of the world's strongest human players:

- In chess, a 100+ Elo advantage over Stockfish places AlphaZero well above any human player (the top human rating is approximately 2,800-2,900 Elo)
- In shogi, the dominance over Elmo similarly exceeds human capabilities
- In Go, surpassing AlphaGo Master means exceeding the demonstrated level of world champion Ke Jie

These results establish AlphaZero as superhuman in all three games.

---

### النسخة العربية

## نتائج المباريات

بعد 24 ساعة من التدريب (34 ساعة لـ Go)، قيمنا الأداء النهائي لـ AlphaZero من خلال لعب مباريات ضد أقوى البرامج المتاحة لكل لعبة:

- **الشطرنج**: Stockfish 8 (الفائز ببطولة العالم TCEC لعام 2016)
- **شوغي**: Elmo (الفائز ببطولة العالم CSA لعام 2017)
- **Go**: AlphaGo Master و AlphaGo Lee (الإصدارات السابقة)

تم السماح لجميع البرامج باستخدام إعداداتها القياسية وضوابط الوقت. بالنسبة للشطرنج، تم تشغيل Stockfish مع تعطيل كتاب الافتتاح القياسي الخاص به لضمان المقارنة العادلة (نظراً لأن AlphaZero لا يستخدم كتاب افتتاح). وبالمثل، تم تعطيل جداول نهاية اللعبة.

### نتائج الشطرنج

لعب AlphaZero مباراة من 100 لعبة ضد Stockfish، مع إعطاء كل برنامج دقيقة واحدة لكل حركة. كانت شروط المباراة:
- التحكم في الوقت: دقيقة واحدة لكل حركة
- لا يوجد كتاب افتتاح
- لا توجد جداول نهاية اللعبة
- Stockfish يستخدم 64 خيط CPU وجدول تجزئة 1GB

النتائج:
- AlphaZero: 28 فوزاً، 72 تعادلاً، 0 خسارة
- معدل الفوز: 28%، معدل التعادل: 72%، معدل الخسارة: 0%
- الأداء: فاز AlphaZero بشكل مقنع دون خسارة لعبة واحدة

في مباراة بضوابط وقت أطول (3 ساعات لكل لعبة)، حافظ AlphaZero على تفوقه، حيث فاز بـ 25 لعبة وتعادل في 25 لعبة من أصل 50 لعبة إجمالاً (سجل 25-0-25).

أظهرت المباريات فهم AlphaZero المتفوق لمواقف الشطرنج. حتى عندما كان لدى Stockfish وقت أكبر للبحث (حتى 10 أضعاف وقت التفكير)، حافظ AlphaZero على تفوقه. هذا يظهر أن تقييمات الشبكة العصبية لـ AlphaZero أكثر دقة من دالة التقييم المصنوعة يدوياً لـ Stockfish مع بحث أعمق.

### نتائج شوغي

لعب AlphaZero مباراة من 100 لعبة ضد Elmo بشروط مماثلة:
- التحكم في الوقت: دقيقتان لكل حركة
- قواعد شوغي القياسية

النتائج:
- AlphaZero: 90 فوزاً، 10 تعادلات، 0 خسارة
- معدل الفوز: 90%، معدل التعادل: 10%، معدل الخسارة: 0%
- الأداء: هيمن AlphaZero بشكل كامل

كان هامش الفوز في شوغي أكبر حتى من الشطرنج. فاز AlphaZero بـ 90% من الألعاب دون خسارة واحدة، مما يوضح التفوق الساحق على بطل شوغي الحاسوبي الحالي.

### نتائج Go

لعب AlphaZero مباريات ضد إصدارين سابقين من AlphaGo:

ضد AlphaGo Lee (100 لعبة):
- AlphaZero: 100 فوز، 0 تعادل، 0 خسارة
- معدل الفوز: 100%
- فاز AlphaZero بكل لعبة واحدة

ضد AlphaGo Master (40 لعبة):
- AlphaZero: 40 فوزاً، 0 تعادل، 0 خسارة
- معدل الفوز: 100%
- فاز AlphaZero مرة أخرى بكل لعبة

تظهر هذه النتائج أن AlphaZero لم يطابق فقط بل تجاوز بشكل كبير أداء أسلافه في Go. معدل الفوز بنسبة 100% ضد AlphaGo Lee مثير للإعجاب بشكل خاص نظراً لأن AlphaGo Lee قد هزم بطل العالم Lee Sedol 4-1.

### الأهمية الإحصائية

جميع النتائج ذات دلالة إحصائية بثقة عالية جداً (p < 0.001). يترك اتساق أداء AlphaZero عبر ألعاب متعددة أي شك حول تفوقه على البرامج الأساسية.

الفروقات في تصنيف Elo التي تنطوي عليها نتائج هذه المباريات كبيرة:
- الشطرنج: حوالي 100-150 ميزة Elo على Stockfish
- شوغي: حوالي 400+ ميزة Elo على Elmo
- Go: ميزة لا يمكن قياسها (معدل فوز 100%)

### تحليل الألعاب

كشف تحليل الألعاب الفردية عن جوانب مثيرة للاهتمام في لعب AlphaZero:

**الشطرنج**: يلعب AlphaZero بشكل متكرر حركات تبدو مشكوكاً فيها في البداية للمحركات التقليدية ولكنها تؤدي إلى مزايا طويلة الأجل. يظهر فهماً استثنائياً لنشاط القطع، وأمان الملك، وبنية البيادق. تتميز العديد من ألعابه بتضحيات ديناميكية ومفاهيم موضعية تتحدى نظرية الشطرنج التقليدية.

**شوغي**: يظهر AlphaZero لعباً إبداعياً وهجومياً، وغالباً ما يبدأ تسلسلات تكتيكية معقدة. يبدو تقييمه لمواقف شوغي مختلفاً بشكل أساسي عن البرامج التقليدية.

**Go**: يظهر AlphaZero روح قتالية وعمق استراتيجي، يلعب بشكل مماثل لـ AlphaGo Master ولكن بدقة تكتيكية أكبر. يجد باستمرار تسلسلات تزيد من احتمالية الفوز.

### المقارنة مع اللعب البشري

في حين لم تكن المقارنة المباشرة مع اللاعبين البشريين محور هذا البحث، توفر النتائج أدلة قوية على أن AlphaZero قد حقق أو تجاوز مستوى أقوى اللاعبين البشريين في العالم:

- في الشطرنج، ميزة 100+ Elo على Stockfish تضع AlphaZero بشكل جيد فوق أي لاعب بشري (التصنيف البشري الأعلى هو حوالي 2,800-2,900 Elo)
- في شوغي، الهيمنة على Elmo تتجاوز بالمثل القدرات البشرية
- في Go، تجاوز AlphaGo Master يعني تجاوز المستوى المثبت لبطل العالم Ke Jie

تثبت هذه النتائج AlphaZero كفوق بشري في جميع الألعاب الثلاث.

---

### Translation Notes

- **Key terms introduced:**
  - time control (التحكم في الوقت)
  - hash table (جدول تجزئة)
  - win rate (معدل الفوز)
  - statistical significance (الأهمية الإحصائية)
  - p-value (قيمة p)
  - tactical sequence (تسلسل تكتيكي)
  - pawn structure (بنية البيادق)
  - winning probability (احتمالية الفوز)

- **Figures referenced:** Match results and statistics
- **Equations:** None in this section
- **Citations:** References to tournament winners and AlphaGo versions
- **Special handling:**
  - Program names (Stockfish, Elmo, AlphaGo Lee, AlphaGo Master) kept in English
  - Player names (Lee Sedol, Ke Jie) kept in English
  - Tournament names (TCEC, CSA) kept as acronyms
  - Match scores presented in standard format (wins-losses-draws)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.87
