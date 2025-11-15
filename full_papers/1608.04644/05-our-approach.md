# Section 5: Our Approach
## القسم 5: نهجنا

**Section:** our-approach
**Translation Quality:** 0.87
**Glossary Terms Used:** objective function (دالة هدفية), optimization (تحسين), gradient descent (انحدار تدرجي), binary search (بحث ثنائي), constraint (قيد), hyperparameter (معامل فائق), Adam optimizer (محسن Adam), momentum (زخم)

---

### English Version

## V-A Objective Function

Rather than directly constraining $C(x+\delta) = t$, the authors express this as $f(x+\delta) \leq 0$ for various objective functions:

- $f_1(x') = -\text{loss}_{F,t}(x') + 1$
- $f_2(x') = (\max_{i \neq t}(F(x')_i) - F(x')_t)^+$
- $f_3(x') = \text{softplus}(\max_{i \neq t}(F(x')_i) - F(x')_t) - \log(2)$
- $f_4(x') = (0.5 - F(x')_t)^+$
- $f_5(x') = -\log(2F(x')_t - 2)$
- $f_6(x') = (\max_{i \neq t}(Z(x')_i) - Z(x')_t)^+$
- $f_7(x') = \text{softplus}(\max_{i \neq t}(Z(x')_i) - Z(x')_t) - \log(2)$

The reformulated optimization becomes:

$$\text{minimize } ||\delta||_p + c \cdot f(x+\delta)$$
$$\text{subject to } x+\delta \in [0,1]^n$$

**Choosing constant c**: "We have found that often the best way to choose c is to use the smallest value of c for which the resulting solution x* has f(x*) ≤ 0." This prevents gradient descent from optimizing only one term initially. Binary search over 20 iterations determines optimal c values. Testing shows that using the minimal c places solutions within 5% of optimal 70% of the time and within 30% of optimal 98% of the time.

**Why some loss functions perform better**: When $c = 0$, no movement occurs; large $c$ causes premature greedy optimization. Functions $f_1$ and $f_4$ have no good fixed $c$ throughout optimization. The paper demonstrates that as linear interpolation moves from $x$ to $x'$, $Z(\cdot)_t$ behaves approximately linearly with Pearson correlation $r > 0.9$, making $F(\cdot)_t$ logistic-shaped.

For $f_4$, requiring gradient descent progress demands $c > 1/|\nabla f_1(x)|$. Since $F(\cdot)_t$ near the initial image is tiny (around $2^{-20}$), $c$ must reach $10^6$. However, at adversarial examples, gradients reach $2^{-1}$, making $c$ one million times larger than necessary and causing overly greedy behavior.

Empirically, $f_6$ and $f_7$ (using logits $Z$ rather than softmax $F$) perform best with three-fold performance advantages over worst approaches. Cross-entropy loss, widely suggested in literature, ranked worst.

## V-B Box Constraints

Three methods enforce $0 \leq x_i + \delta_i \leq 1$:

**Projected Gradient Descent**: Performs standard gradient descent then clips to valid range. Complications arise with momentum-based optimizers where clipping unexpectedly alters next iteration inputs.

**Clipped Gradient Descent**: Incorporates clipping into the objective by replacing $f(x+\delta)$ with $f(\min(\max(x+\delta,0),1))$. However, components can exceed bounds with zero gradients, creating flat spots preventing progress.

**Change of Variables**: Optimizes auxiliary variable $w$ with:

$$\delta_i = \frac{1}{2}(\tanh(w_i) + 1) - x_i$$

Since $-1 \leq \tanh(w_i) \leq 1$, validity is automatically satisfied. This smooths clipped descent, eliminating extreme value problems.

The paper uses the Adam optimizer almost exclusively, finding it dramatically faster than standard gradient descent or momentum methods while producing identical solution quality.

## V-C Evaluation of Approaches

Testing combinations of seven objective functions and three constraint encodings on 1000 random MNIST instances using 20 binary search iterations and 10,000 Adam optimizer iterations per c value reveals:

- Factor of three difference between best and worst objective functions
- Cross-entropy loss ($f_1$) performs worst despite literature suggestions
- $f_6$ and $f_7$ achieve 100% success rates in best/average/worst cases
- Box constraint method selection matters less for best-performing functions

## V-D Discretization

Since actual images use discrete pixel values $\{0,1,...,255\}$ rather than continuous $[0,1]$, the paper rounds solutions: $\lfloor 255(x_i+\delta_i) \rfloor$ becomes the final pixel value. When quality degradation occurs, greedy single-pixel modifications restore attack quality, never failing in practice.

"Prior work has largely ignored the integrality constraints." The authors show that for small perturbations (as in their work), discretization effects are non-negligible and must be properly addressed.

---

### النسخة العربية

## V-A الدالة الهدفية

بدلاً من تقييد $C(x+\delta) = t$ مباشرة، يعبر المؤلفون عن هذا كـ $f(x+\delta) \leq 0$ لدوال هدفية مختلفة:

- $f_1(x') = -\text{loss}_{F,t}(x') + 1$
- $f_2(x') = (\max_{i \neq t}(F(x')_i) - F(x')_t)^+$
- $f_3(x') = \text{softplus}(\max_{i \neq t}(F(x')_i) - F(x')_t) - \log(2)$
- $f_4(x') = (0.5 - F(x')_t)^+$
- $f_5(x') = -\log(2F(x')_t - 2)$
- $f_6(x') = (\max_{i \neq t}(Z(x')_i) - Z(x')_t)^+$
- $f_7(x') = \text{softplus}(\max_{i \neq t}(Z(x')_i) - Z(x')_t) - \log(2)$

حيث:
- $(x)^+ = \max(0, x)$ (دالة ReLU)
- $F(x')_i$: احتمال softmax للفئة $i$
- $Z(x')_i$: لوجيت الفئة $i$ (قبل softmax)
- $t$: الفئة المستهدفة

يصبح التحسين المعاد صياغته:

$$\text{minimize } ||\delta||_p + c \cdot f(x+\delta)$$
$$\text{subject to } x+\delta \in [0,1]^n$$

أدنى: $||\delta||_p + c \cdot f(x+\delta)$ (موازنة بين المسافة والتصنيف)
بحيث: $x+\delta \in [0,1]^n$ (قيم بكسل صالحة)

**اختيار الثابت c**: "وجدنا أن أفضل طريقة لاختيار $c$ غالباً هي استخدام أصغر قيمة لـ $c$ التي ينتج عنها حل $x^*$ يحقق $f(x^*) \leq 0$." هذا يمنع الانحدار التدرجي من تحسين مصطلح واحد فقط في البداية. يحدد البحث الثنائي على مدى 20 تكراراً قيم $c$ المثلى. يُظهر الاختبار أن استخدام $c$ الأدنى يضع الحلول ضمن 5% من الأمثل في 70% من الحالات وضمن 30% من الأمثل في 98% من الحالات.

**لماذا تؤدي بعض دوال الخسارة بشكل أفضل**: عندما $c = 0$، لا يحدث أي تحرك؛ $c$ كبير يسبب تحسيناً جشعاً مبكراً. الدوال $f_1$ و $f_4$ ليس لديها $c$ ثابت جيد طوال التحسين. يوضح البحث أنه عندما يتحرك الاستيفاء الخطي من $x$ إلى $x'$، يتصرف $Z(\cdot)_t$ بشكل خطي تقريباً مع ارتباط بيرسون $r > 0.9$، مما يجعل $F(\cdot)_t$ بشكل لوجستي.

بالنسبة لـ $f_4$، يتطلب تقدم الانحدار التدرجي $c > 1/|\nabla f_1(x)|$. نظراً لأن $F(\cdot)_t$ بالقرب من الصورة الأولية صغيرة جداً (حوالي $2^{-20}$)، يجب أن يصل $c$ إلى $10^6$. ومع ذلك، عند الأمثلة الخصامية، تصل التدرجات إلى $2^{-1}$، مما يجعل $c$ أكبر بمليون مرة من اللازم ويسبب سلوكاً جشعاً مفرطاً.

تجريبياً، تؤدي $f_6$ و $f_7$ (استخدام اللوجيتات $Z$ بدلاً من softmax $F$) بشكل أفضل مع مزايا أداء ثلاثية مقارنة بأسوأ النهج. احتلت خسارة cross-entropy، المقترحة على نطاق واسع في الأدبيات، المرتبة الأسوأ.

## V-B قيود الصندوق

ثلاث طرق تفرض $0 \leq x_i + \delta_i \leq 1$:

**الانحدار التدرجي المُسقط**: يقوم بانحدار تدرجي قياسي ثم يقص إلى النطاق الصالح. تنشأ مضاعفات مع محسنات قائمة على الزخم حيث يؤدي القص بشكل غير متوقع إلى تغيير مدخلات التكرار التالي.

**الانحدار التدرجي المقصوص**: يدمج القص في الهدف عن طريق استبدال $f(x+\delta)$ بـ $f(\min(\max(x+\delta,0),1))$. ومع ذلك، يمكن للمكونات تجاوز الحدود مع تدرجات صفرية، مما يخلق نقاط مسطحة تمنع التقدم.

**تغيير المتغيرات**: يحسّن متغير مساعد $w$ مع:

$$\delta_i = \frac{1}{2}(\tanh(w_i) + 1) - x_i$$

حيث يتم التحسين على $w$ بدلاً من $\delta$ مباشرة.

نظراً لأن $-1 \leq \tanh(w_i) \leq 1$، يتم تلبية الصلاحية تلقائياً. هذا ينعم الانحدار المقصوص، مما يلغي مشاكل القيم القصوى.

يستخدم البحث محسن Adam بشكل شبه حصري، ويجده أسرع بشكل كبير من الانحدار التدرجي القياسي أو طرق الزخم مع إنتاج جودة حل متطابقة.

## V-C تقييم النهج

اختبار مجموعات من سبع دوال هدفية وثلاثة ترميزات قيد على 1000 عينة MNIST عشوائية باستخدام 20 تكرار بحث ثنائي و 10,000 تكرار محسن Adam لكل قيمة $c$ يكشف:

- فارق بمعامل ثلاثة بين أفضل وأسوأ الدوال الهدفية
- تؤدي خسارة cross-entropy ($f_1$) بشكل أسوأ على الرغم من اقتراحات الأدبيات
- تحقق $f_6$ و $f_7$ معدلات نجاح 100% في حالات أفضل/متوسط/أسوأ
- اختيار طريقة قيد الصندوق يهم بشكل أقل للدوال الأفضل أداءً

## V-D التقطيع

نظراً لأن الصور الفعلية تستخدم قيم بكسل منفصلة $\{0,1,...,255\}$ بدلاً من $[0,1]$ المستمر، يقرب البحث الحلول: $\lfloor 255(x_i+\delta_i) \rfloor$ تصبح قيمة البكسل النهائية. عندما يحدث تدهور في الجودة، تستعيد التعديلات الجشعة لبكسل واحد جودة الهجوم، دون فشل أبداً في الممارسة.

"تجاهل العمل السابق إلى حد كبير قيود التكامل." يُظهر المؤلفون أنه بالنسبة للاضطرابات الصغيرة (كما في عملهم)، تأثيرات التقطيع غير ضئيلة ويجب معالجتها بشكل صحيح.

---

### Translation Notes

- **Figures referenced:** Figure 3, Figure 12 (mentioned for L₂ attack visualization)
- **Key terms introduced:**
  - Objective function (دالة هدفية)
  - softplus function (دالة softplus - kept in English)
  - Cross-entropy loss (خسارة cross-entropy)
  - Projected gradient descent (انحدار تدرجي مُسقط)
  - Change of variables (تغيير المتغيرات)
  - Pearson correlation (ارتباط بيرسون)
  - Integrality constraints (قيود التكامل)
  - Greedy modification (تعديل جشع)

- **Equations:**
  - Seven objective functions (f₁ through f₇)
  - Main optimization problem
  - Change of variables formula for δᵢ
  - Discretization formula
  - All preserved in LaTeX with Arabic explanations

- **Citations:** Reference to prior work on cross-entropy loss
- **Special handling:**
  - Detailed explanation of why f₆ and f₇ outperform f₁ and f₄
  - Mathematical analysis of gradient magnitudes (2⁻²⁰ vs 2⁻¹)
  - Three-fold performance advantage quantified
  - Adam optimizer kept in English as standard
  - ReLU notation explained as (x)⁺ = max(0, x)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87

**Notes:** This is a highly technical section with complex mathematical analysis. All seven objective functions are preserved in LaTeX with Arabic explanations. The discussion of why certain functions perform better includes detailed gradient analysis. The change of variables technique using tanh is a key innovation and is clearly explained. The section maintains technical rigor while being accessible to Arabic-speaking researchers in adversarial ML.
