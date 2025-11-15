# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** artificial intelligence, reinforcement learning, neural network, Monte Carlo Tree Search, self-play, evaluation function, policy, value function

---

### English Version

Games have been a landmark activity in the development of artificial intelligence. From the early days of computer science, games like chess have provided a grand challenge for artificial intelligence research. In 1997, Deep Blue became the first computer program to defeat a reigning world champion in chess under tournament conditions. Deep Blue combined sophisticated alpha-beta search with handcrafted evaluation functions that had been tuned by grandmasters and computer scientists over several decades.

More recently, the game of Go presented an even greater challenge for artificial intelligence. The traditional game-playing programs that succeeded in chess failed in Go, due to the greater branching factor and the difficulty of evaluating positions. AlphaGo addressed these challenges by using deep neural networks for both policy and value estimation, combined with Monte Carlo tree search. In 2016, AlphaGo defeated the world champion Lee Sedol.

The AlphaGo Zero program refined this approach even further. By starting from random play, without any domain knowledge or human data, AlphaGo Zero achieved superhuman performance purely through reinforcement learning from games of self-play. It quickly exceeded the performance of all previous versions of AlphaGo.

In this paper, we introduce AlphaZero: a more general algorithm based on the same principles. AlphaZero takes AlphaGo Zero's approach and applies it to chess and shogi as well as Go, without any game-specific enhancements or modifications. We demonstrate that AlphaZero achieves, tabula rasa, superhuman performance in all three games within 24 hours, and convincingly defeats world-champion programs in each case.

---

### النسخة العربية

لقد كانت الألعاب نشاطاً بارزاً في تطوير الذكاء الاصطناعي. منذ الأيام الأولى لعلوم الحاسوب، قدمت ألعاب مثل الشطرنج تحدياً كبيراً لأبحاث الذكاء الاصطناعي. في عام 1997، أصبح Deep Blue أول برنامج حاسوبي يهزم بطل العالم الحالي في الشطرنج في ظروف البطولة. جمع Deep Blue بين البحث المتطور من نوع alpha-beta ودوال التقييم المصنوعة يدوياً التي تم ضبطها من قبل أساتذة كبار وعلماء حاسوب على مدى عدة عقود.

في الآونة الأخيرة، قدمت لعبة Go تحدياً أكبر للذكاء الاصطناعي. فشلت برامج اللعب التقليدية التي نجحت في الشطرنج في Go، بسبب معامل التفرع الأكبر وصعوبة تقييم المواقف. عالج AlphaGo هذه التحديات باستخدام الشبكات العصبية العميقة لتقدير كل من السياسة والقيمة، جنباً إلى جنب مع بحث شجرة مونت كارلو. في عام 2016، هزم AlphaGo بطل العالم Lee Sedol.

قام برنامج AlphaGo Zero بتحسين هذا النهج بشكل أكبر. من خلال البدء من اللعب العشوائي، دون أي معرفة بالمجال أو بيانات بشرية، حقق AlphaGo Zero أداءً فوق بشري بشكل خالص من خلال التعلم المعزز من ألعاب اللعب الذاتي. تجاوز بسرعة أداء جميع الإصدارات السابقة من AlphaGo.

في هذا البحث، نقدم AlphaZero: خوارزمية أكثر عمومية تستند إلى نفس المبادئ. يأخذ AlphaZero نهج AlphaGo Zero ويطبقه على الشطرنج وشوغي بالإضافة إلى Go، دون أي تحسينات أو تعديلات خاصة باللعبة. نوضح أن AlphaZero يحقق، من الصفر (tabula rasa)، أداءً فوق بشري في جميع الألعاب الثلاثة خلال 24 ساعة، ويهزم بشكل مقنع برامج بطل العالم في كل حالة.

---

### Translation Notes

- **Key terms introduced:**
  - alpha-beta search (البحث alpha-beta) - kept Greek letters as standard CS term
  - branching factor (معامل التفرع)
  - policy estimation (تقدير السياسة)
  - value estimation (تقدير القيمة)
  - tabula rasa (من الصفر) - explained in parentheses

- **Figures referenced:** None in this section
- **Equations:** None
- **Citations:** References to Deep Blue (1997), AlphaGo (2016), AlphaGo Zero
- **Special handling:**
  - Proper nouns (Deep Blue, AlphaGo, AlphaGo Zero, AlphaZero, Lee Sedol) kept in English
  - Game names: Chess (الشطرنج), Shogi (شوغي), Go (Go)

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.88
- Glossary consistency: 0.87
- **Overall section score:** 0.88
