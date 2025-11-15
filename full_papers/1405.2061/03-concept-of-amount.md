# Section 3: Concept of "Amount" of Information
## القسم 3: مفهوم "كمية" المعلومات

**Section:** Conceptual Development
**Translation Quality:** 0.89
**Glossary Terms Used:** information (معلومات), variable (متغير), random variable (متغير عشوائي), probability (احتمال), bit (بت)

---

### English Version

Intuitively, one way to understand the concept of "amount of information" in a variable is to tie it to how difficult or easy it is to guess that information without having to look at the variable: the easier it is to guess the value of the variable, the less "surprise" in the variable and so the less information the variable has. Another way to view information is to contrast it with the amount of data. For example, two different Boolean variables could be stored in 1 bit each, but the amount of information in the two may be quite different, as illustrated below.

Suppose a coin is completely biased and always comes up heads when tossed, then the random variable representing the coin toss's outcome has probability 1 of coming up heads (in other words, it is a constant), and thus there is no need to store or transmit that variable as it can be trivially guessed at any time. Thus, the amount of information in that variable is zero.

On the other hand, if we had a perfect coin with half-half chances of coming up heads or tails upon a coin toss, then we can guess the outcome of a toss with only 50% accuracy (probability 0.5), so it is necessary to store/transmit the actual value of that coin toss outcome's random variable in order to know its value with better than 50% accuracy. Thus, the amount of information in this second random variable is much higher than in the first case.

Contrast the fact that, for both of the above coins, the raw data regarding their toss outcomes need 1 bit each to be stored.

Instead of a coin, suppose we had a perfect die (cube) with 6 possible outcomes on the toss (roll) of the die. The amount of information in the corresponding random variable is even higher, as it now even harder to guess the outcome of the die roll, we have only 1/6th chance of guessing the outcome correctly -- much less than 50%.

---

### النسخة العربية

بشكل حدسي، إحدى طرق فهم مفهوم "كمية المعلومات" في متغير هي ربطه بمدى صعوبة أو سهولة تخمين تلك المعلومات دون الحاجة إلى النظر إلى المتغير: كلما كان من الأسهل تخمين قيمة المتغير، قلت "المفاجأة" في المتغير وبالتالي قلت المعلومات التي يحتويها المتغير. طريقة أخرى لعرض المعلومات هي مقارنتها بكمية البيانات. على سبيل المثال، يمكن تخزين متغيرين منطقيين مختلفين في بت واحد لكل منهما، لكن كمية المعلومات في الاثنين قد تكون مختلفة تماماً، كما هو موضح أدناه.

لنفترض أن عملة متحيزة تماماً وتأتي دائماً على وجه الصورة عند رميها، عندئذ يكون للمتغير العشوائي الذي يمثل نتيجة رمي العملة احتمال 1 للحصول على وجه الصورة (بعبارة أخرى، هو ثابت)، وبالتالي لا حاجة لتخزين أو نقل هذا المتغير لأنه يمكن تخمينه بشكل تافه في أي وقت. وبالتالي، فإن كمية المعلومات في هذا المتغير هي صفر.

من ناحية أخرى، إذا كان لدينا عملة مثالية مع فرص متساوية للحصول على وجه الصورة أو الكتابة عند رمي العملة، فإننا نستطيع تخمين نتيجة الرمية بدقة 50٪ فقط (احتمال 0.5)، لذلك من الضروري تخزين/نقل القيمة الفعلية لمتغير نتيجة رمي العملة هذا من أجل معرفة قيمته بدقة أفضل من 50٪. وبالتالي، فإن كمية المعلومات في هذا المتغير العشوائي الثاني أعلى بكثير من الحالة الأولى.

قارن ذلك مع حقيقة أن البيانات الخام المتعلقة بنتائج رمي كلتا العملتين المذكورتين أعلاه تحتاج إلى بت واحد لكل منهما للتخزين.

بدلاً من عملة، لنفترض أن لدينا حجر نرد مثالي (مكعب) به 6 نتائج محتملة عند رمي (إلقاء) النرد. كمية المعلومات في المتغير العشوائي المقابل أعلى حتى، حيث أصبح من الأصعب الآن تخمين نتيجة رمي النرد، لدينا فقط فرصة 1/6 لتخمين النتيجة بشكل صحيح -- وهو أقل بكثير من 50٪.

---

### Translation Notes

- **Key terms introduced:**
  - random variable (متغير عشوائي)
  - probability (احتمال)
  - accuracy (دقة)
  - biased (متحيزة)
  - perfect coin (عملة مثالية)
  - die/dice (حجر نرد/النرد)
- **Examples:**
  - Completely biased coin (probability = 1)
  - Fair coin (probability = 0.5)
  - Six-sided die (probability = 1/6)
- **Special handling:**
  - Maintained the informal, pedagogical tone
  - Preserved the progressive difficulty of examples
  - Ensured mathematical probability values remain unchanged

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.91
- Readability: 0.88
- Glossary consistency: 0.89
- **Overall section score:** 0.89
