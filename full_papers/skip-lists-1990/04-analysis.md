# Section 4: Probabilistic Analysis
## القسم 4: التحليل الاحتمالي

**Section:** probabilistic-analysis
**Translation Quality:** 0.85
**Glossary Terms Used:** probability, expected value, complexity, analysis, theorem, proof, logarithmic

---

### English Version

## Expected Search Time

The expected number of steps in a search is proportional to the expected length of the search path. We analyze this by considering the search path in reverse, from the target element up to the header.

**Theorem 1:** The expected search time in a skip list of n elements is O(log n).

**Proof Sketch:**
At any particular level, the probability of climbing up to the next level during a reverse search is p. The expected number of steps at each level before climbing up is 1/p. Since the maximum level is O(log n) with high probability, the expected total search path length is O((1/p) log n) = O(log n) when p is a constant.

More formally, let C(k) be the expected cost (in number of steps) of a search path that climbs up k levels. We have:

$$C(0) = 0$$

For k > 0, at the current level we move left an expected 1/p times before climbing up, giving:

$$C(k) = (1/p) + C(k-1)$$

Solving this recurrence:

$$C(k) = k/p$$

The maximum level L in a skip list of n elements satisfies:

$$\text{E}[L] = \log_{1/p} n$$

Therefore, the expected search path length is:

$$\text{E}[\text{path length}] = C(L) = L/p = (1/p) \log_{1/p} n = O(\log n)$$

## Expected Space

The space used by a skip list is determined by the total number of pointers across all nodes.

**Theorem 2:** The expected number of pointers in a skip list of n elements is n/(1-p).

**Proof:**
Each element appears at level 1 with probability 1. It appears at level 2 with probability p, at level 3 with probability p², and so on. The expected number of pointers per element is:

$$\text{E}[\text{pointers per element}] = \sum_{i=1}^{\infty} p^{i-1} = \frac{1}{1-p}$$

With n elements, the total expected number of pointers is:

$$\text{E}[\text{total pointers}] = \frac{n}{1-p}$$

For p = 1/2, this is 2n pointers on average.
For p = 1/4, this is (4/3)n pointers on average.

## Distribution of Maximum Level

The maximum level in a skip list grows logarithmically with the number of elements.

**Theorem 3:** In a skip list of n elements with parameter p, the probability that the maximum level exceeds c log_{1/p} n is at most 1/n^{c-1}.

**Proof:**
The probability that a specific element has level > L is p^L. The probability that any of n elements has level > L is at most n·p^L (by union bound).

Setting L = c log_{1/p} n:

$$p^L = p^{c \log_{1/p} n} = (p^{\log_{1/p} n})^c = (1/n)^c = 1/n^c$$

Therefore:

$$P[\text{max level} > L] \leq n \cdot p^L = n/n^c = 1/n^{c-1}$$

This shows that with high probability, the maximum level is O(log n).

## Practical Considerations

For a skip list with p = 1/2 and MaxLevel = 16:
- Can handle up to 2^16 = 65,536 elements efficiently
- Expected search path length is about 16 comparisons for 65,536 elements
- Average space overhead is one extra pointer per element

For p = 1/4:
- Less space overhead (only 1/3 extra pointers per element)
- Slightly longer search paths (factor of 1/(1-p) = 4/3 compared to p = 1/2)
- Better cache performance due to fewer pointers

The choice of p involves a trade-off between time and space. Smaller p reduces space but increases search time slightly.

---

### النسخة العربية

## زمن البحث المتوقع

العدد المتوقع من الخطوات في البحث يتناسب مع الطول المتوقع لمسار البحث. نحلل هذا من خلال النظر في مسار البحث بالعكس، من العنصر المستهدف حتى الرأس.

**المبرهنة 1:** زمن البحث المتوقع في قائمة تخطي من n عنصر هو O(log n).

**مخطط البرهان:**
في أي مستوى معين، احتمال الصعود إلى المستوى التالي أثناء البحث العكسي هو p. العدد المتوقع من الخطوات في كل مستوى قبل الصعود هو 1/p. نظراً لأن المستوى الأقصى هو O(log n) باحتمال كبير، فإن الطول الإجمالي المتوقع لمسار البحث هو O((1/p) log n) = O(log n) عندما تكون p ثابتة.

بشكل أكثر رسمية، لنفترض أن C(k) هي التكلفة المتوقعة (بعدد الخطوات) لمسار بحث يصعد k مستوى. لدينا:

$$C(0) = 0$$

بالنسبة لـ k > 0، في المستوى الحالي نتحرك يساراً 1/p مرة متوقعة قبل الصعود، مما يعطي:

$$C(k) = (1/p) + C(k-1)$$

حل هذا التكرار:

$$C(k) = k/p$$

المستوى الأقصى L في قائمة تخطي من n عنصر يحقق:

$$\text{E}[L] = \log_{1/p} n$$

وبالتالي، طول مسار البحث المتوقع هو:

$$\text{E}[\text{path length}] = C(L) = L/p = (1/p) \log_{1/p} n = O(\log n)$$

## المساحة المتوقعة

المساحة المستخدمة من قبل قائمة التخطي تتحدد بالعدد الإجمالي للمؤشرات عبر جميع العقد.

**المبرهنة 2:** العدد المتوقع للمؤشرات في قائمة تخطي من n عنصر هو n/(1-p).

**البرهان:**
كل عنصر يظهر في المستوى 1 باحتمال 1. يظهر في المستوى 2 باحتمال p، في المستوى 3 باحتمال p²، وهكذا. العدد المتوقع من المؤشرات لكل عنصر هو:

$$\text{E}[\text{pointers per element}] = \sum_{i=1}^{\infty} p^{i-1} = \frac{1}{1-p}$$

مع n عنصر، العدد الإجمالي المتوقع للمؤشرات هو:

$$\text{E}[\text{total pointers}] = \frac{n}{1-p}$$

بالنسبة لـ p = 1/2، هذا يعني 2n مؤشر في المتوسط.
بالنسبة لـ p = 1/4، هذا يعني (4/3)n مؤشر في المتوسط.

## توزيع المستوى الأقصى

ينمو المستوى الأقصى في قائمة التخطي لوغاريتمياً مع عدد العناصر.

**المبرهنة 3:** في قائمة تخطي من n عنصر مع معامل p، احتمال أن يتجاوز المستوى الأقصى c log_{1/p} n هو على الأكثر 1/n^{c-1}.

**البرهان:**
احتمال أن يكون لعنصر محدد مستوى > L هو p^L. احتمال أن يكون لأي من n عنصر مستوى > L هو على الأكثر n·p^L (بواسطة حد الاتحاد).

بتعيين L = c log_{1/p} n:

$$p^L = p^{c \log_{1/p} n} = (p^{\log_{1/p} n})^c = (1/n)^c = 1/n^c$$

وبالتالي:

$$P[\text{max level} > L] \leq n \cdot p^L = n/n^c = 1/n^{c-1}$$

هذا يظهر أنه باحتمال كبير، المستوى الأقصى هو O(log n).

## الاعتبارات العملية

بالنسبة لقائمة تخطي مع p = 1/2 و MaxLevel = 16:
- يمكن التعامل مع ما يصل إلى 2^16 = 65,536 عنصر بكفاءة
- طول مسار البحث المتوقع هو حوالي 16 مقارنة لـ 65,536 عنصر
- متوسط الزيادة في المساحة هو مؤشر إضافي واحد لكل عنصر

بالنسبة لـ p = 1/4:
- زيادة أقل في المساحة (فقط 1/3 مؤشرات إضافية لكل عنصر)
- مسارات بحث أطول قليلاً (عامل 1/(1-p) = 4/3 مقارنة بـ p = 1/2)
- أداء ذاكرة تخزين مؤقت أفضل بسبب عدد أقل من المؤشرات

اختيار p ينطوي على مفاضلة بين الزمن والمساحة. قيمة p الأصغر تقلل المساحة لكن تزيد زمن البحث قليلاً.

---

### Translation Notes

- **Key terms introduced:**
  - expected value (القيمة المتوقعة)
  - theorem (مبرهنة)
  - proof (برهان)
  - recurrence (تكرار)
  - union bound (حد الاتحاد)
  - trade-off (مفاضلة)
  - cache performance (أداء ذاكرة التخزين المؤقت)
  - space overhead (زيادة في المساحة)
- **Equations:** 10+ mathematical equations using LaTeX notation
- **Theorems:** 3 formal theorems with proofs
- **Special handling:**
  - All mathematical notation preserved in LaTeX
  - Summation and logarithm notation maintained
  - Probability notation kept standard
  - Formal proof structure preserved

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.87
- Readability: 0.84
- Glossary consistency: 0.83
- **Overall section score:** 0.85
