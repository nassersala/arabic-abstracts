# Section 7: Mathematical Approximation of Required Storage
## القسم 7: التقريب الرياضي للتخزين المطلوب

**Section:** Advanced Concepts
**Translation Quality:** 0.87
**Glossary Terms Used:** entropy (إنتروبيا), bit (بت), logarithm (لوغاريتم), quantum computing (الحوسبة الكمية), qubit (كيوبت)

---

### English Version

So far so good, but the intuition break down a bit when we have probabilities that have numerators or denominators that are not powers of 2. For example, suppose 'a' occurs with probability 9/27, that means there might be 27 different values the variable can take on, and 'a' is 9 of them. Now, log₂(27) = 4.75488.., and that is not an integral number of bits! So how do we interpret log₂(p) in this scenario? Obviously we can't say that we need {log₂(27)-log₂(9)} = (4.75488-3.1699) = 1.5849-odd bits to store 'a'! In digital storage, bits come whole, in counts of integers, and not in fractions!

In this case, the entropy formula becomes a mathematical entity, perhaps having no exact real-world analogue in today's world. However, to understand the results of the Shannon's Entropy formula in these scenarios, we can imagine strange new kinds of technology where storage units can come in non-integral amounts and can take on non-integral values. Such technologies may not be all that strange after all: for example, in quantum computers, a "qubit" is a single bit that can simultaneously have the values 0 and 1 with different probabilities α and β (or something like that, anyway!). A little more mundanely, in the above example, suppose we had tri-state logic where each storage unit could take on one of 3 possible values. Now, if we change the base of the logarithm in the entropy formula to 3, we suddenly have -p*log₃(p) = -(9/27)*log(9/27) = (9/27)*{log(27)-log(9)} = (9/27)*{3-2} = 1/3. That is, 'a' can be represented in one unit of tri-state storage, and 'a' occurs 1/3-rd of the time!

Thus, a simple change in the base of the logarithm used in the entropy formula tells us the absolute minimum number of bits required to store the information in a technology where each storage unit allows as many states as the base of the logarithm. In any case, even for digital storage having binary bits, Shannon's Entropy represents a lower-bound on the number of actual bits required to store or transmit information. In the above example, we will need 2 bits to represent 'a', 2 being the next integer higher than 1.263.

---

### النسخة العربية

حتى الآن كل شيء على ما يرام، لكن الحدس ينهار قليلاً عندما يكون لدينا احتمالات ذات بسط أو مقام ليست قوى للعدد 2. على سبيل المثال، لنفترض أن 'a' تحدث باحتمال 9/27، وهذا يعني أنه قد يكون هناك 27 قيمة مختلفة يمكن للمتغير أن يأخذها، و 'a' هي 9 منها. الآن، log₂(27) = 4.75488..، وهذا ليس عدداً صحيحاً من البتات! فكيف نفسر log₂(p) في هذا السيناريو؟ من الواضح أننا لا نستطيع أن نقول إننا نحتاج إلى {log₂(27)-log₂(9)} = (4.75488-3.1699) = 1.5849 بت غريب لتخزين 'a'! في التخزين الرقمي، تأتي البتات كاملة، في أعداد صحيحة، وليس في كسور!

في هذه الحالة، تصبح صيغة الإنتروبيا كياناً رياضياً، ربما ليس له نظير دقيق في العالم الحقيقي اليوم. ومع ذلك، لفهم نتائج صيغة إنتروبيا شانون في هذه السيناريوهات، يمكننا تخيل أنواع جديدة غريبة من التكنولوجيا حيث يمكن أن تأتي وحدات التخزين بكميات غير صحيحة ويمكن أن تأخذ قيماً غير صحيحة. قد لا تكون هذه التقنيات غريبة بعد كل شيء: على سبيل المثال، في أجهزة الكمبيوتر الكمومية، "الكيوبت" هو بت واحد يمكن أن يحمل في نفس الوقت القيمتين 0 و 1 باحتمالات مختلفة α و β (أو شيء من هذا القبيل على أي حال!). بشكل أكثر عملية، في المثال أعلاه، لنفترض أن لدينا منطقاً ثلاثي الحالات حيث يمكن لكل وحدة تخزين أن تأخذ واحدة من 3 قيم محتملة. الآن، إذا غيرنا أساس اللوغاريتم في صيغة الإنتروبيا إلى 3، فجأة لدينا -p×log₃(p) = -(9/27)×log(9/27) = (9/27)×{log(27)-log(9)} = (9/27)×{3-2} = 1/3. أي أنه يمكن تمثيل 'a' في وحدة واحدة من التخزين ثلاثي الحالات، و 'a' تحدث ثلث الوقت!

وبالتالي، فإن تغييراً بسيطاً في أساس اللوغاريتم المستخدم في صيغة الإنتروبيا يخبرنا بالحد الأدنى المطلق لعدد البتات المطلوبة لتخزين المعلومات في تقنية حيث تسمح كل وحدة تخزين بعدد من الحالات يساوي أساس اللوغاريتم. في كل الأحوال، حتى بالنسبة للتخزين الرقمي الذي يحتوي على بتات ثنائية، فإن إنتروبيا شانون تمثل حداً أدنى لعدد البتات الفعلية المطلوبة لتخزين أو نقل المعلومات. في المثال أعلاه، سنحتاج إلى 2 بت لتمثيل 'a'، حيث أن 2 هو العدد الصحيح التالي الأعلى من 1.263.

---

### Translation Notes

- **Key terms introduced:**
  - quantum computers (أجهزة الكمبيوتر الكمومية)
  - qubit (كيوبت)
  - tri-state logic (منطق ثلاثي الحالات)
  - lower-bound (حد أدنى)
  - power of 2 (قوة للعدد 2)
  - integral number (عدد صحيح)
  - base of logarithm (أساس اللوغاريتم)
- **Mathematical concepts:**
  - Non-integral probabilities (9/27)
  - Logarithm base change
  - Lower-bound interpretation
  - Connection to quantum computing
- **Special handling:**
  - Preserved the speculative nature of quantum computing reference
  - Maintained informal tone ("or something like that, anyway!")
  - Ensured mathematical precision throughout
  - Explained why fractional bits are theoretical
- **Advanced topics:**
  - Quantum computing (superficial mention)
  - Multi-valued logic systems
  - Logarithm base changes

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.87
