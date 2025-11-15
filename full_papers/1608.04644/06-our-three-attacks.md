# Section 6: Our Three Attacks
## القسم 6: هجماتنا الثلاث

**Section:** our-three-attacks
**Translation Quality:** 0.86
**Glossary Terms Used:** attack (هجوم), optimization (تحسين), gradient descent (انحدار تدرجي), confidence (ثقة), warm-start (بداية دافئة), threshold (عتبة), iterative (تكراري)

---

### English Version

## VI-A Our L₂ Attack

The attack solves:

$$\text{minimize } ||\frac{1}{2}(\tanh(w)+1) - x||_2^2 + c \cdot f(\frac{1}{2}(\tanh(w)+1))$$

where $f$ is defined as:

$$f(x') = \max(\max\{Z(x')_i : i \neq t\} - Z(x')_t, -\kappa)$$

Parameter $\kappa$ controls misclassification confidence; $\kappa = 0$ for primary attacks. The change-of-variables formulation automatically satisfies box constraints.

**Multiple Starting Points**: Since gradient descent risks local minima, the attack samples multiple random starting points uniformly within radius $r$ (the best solution found so far) and runs gradient descent from each. This reduces local minimum entrapment probability.

Figures 3 and 12 demonstrate the L₂ attack on MNIST and CIFAR-10, with nearly all adversarial examples visually indistinguishable from originals.

## VI-B Our L₀ Attack

The L₀ metric is non-differentiable, unsuitable for standard gradient descent. Instead, the algorithm iteratively identifies unimportant pixels:

1. Call L₂ adversary on current allowed pixel set
2. Compute gradient $g = \nabla f(x+\delta)$
3. Fix pixel $i = \arg\min_i g_i \cdot \delta_i$ (remove from allowed set)
4. Repeat until L₂ adversary fails

The selection criterion $g_i \cdot \delta_i$ indicates how much $f$ reduction results from pixel $i$'s change: $g_i$ shows per-unit reduction, multiplied by actual change $\delta_i$. Selecting based on $\delta_i$ alone yields 1.5× worse results.

Unlike JSMA which grows a pixel set from empty, this attack shrinks the set from complete. **Warm-start optimization** initializes gradient descent from the previous iteration's solution, dramatically reducing required computation.

The algorithm requires choosing constant $c$ for the L₂ subroutine. Starting at $c = 10^{-4}$, $c$ doubles after each failure until success (or threshold $10^{10}$ is exceeded).

Figures 4 and 11 show L₀ attacks on MNIST and CIFAR-10. Visual differences become noticeable, revealing that L₀ constraints are more difficult than L₂.

## VI-C Our L∞ Attack

Naïve L∞ optimization fails because $||\delta||_\infty$ only penalizes the maximum coordinate, leaving others unconstrained. Gradient descent oscillates between equivalent solutions where different coordinates are maximal.

The solution uses iterative attack replacing the L₂ term with penalties for values exceeding threshold $\tau$:

$$\text{minimize } c \cdot f(x+\delta) + \sum_i [(\delta_i - \tau)^+]$$

After each iteration, if all $\delta_i < \tau$, reduce $\tau$ by factor 0.9 and repeat; otherwise terminate.

Constant $c$ selection follows the L₀ approach: start low, double after failures. Warm-start optimization ensures comparable speed to single-point L₂ attacks.

Figures 5 and 13 demonstrate L∞ attacks. Most differences are visually imperceptible, except for the notable 7→6 transformation.

---

### النسخة العربية

## VI-A هجوم L₂ الخاص بنا

يحل الهجوم:

$$\text{minimize } ||\frac{1}{2}(\tanh(w)+1) - x||_2^2 + c \cdot f(\frac{1}{2}(\tanh(w)+1))$$

أدنى: $||\frac{1}{2}(\tanh(w)+1) - x||_2^2 + c \cdot f(\frac{1}{2}(\tanh(w)+1))$

حيث يتم تعريف $f$ كـ:

$$f(x') = \max(\max\{Z(x')_i : i \neq t\} - Z(x')_t, -\kappa)$$

حيث:
- $Z(x')_t$: لوجيت الفئة المستهدفة $t$
- $\max\{Z(x')_i : i \neq t\}$: أعلى لوجيت من الفئات الأخرى
- $\kappa$: معامل الثقة (confidence parameter)

يتحكم المعامل $\kappa$ في ثقة التصنيف الخاطئ؛ $\kappa = 0$ للهجمات الأساسية. تحقق صياغة تغيير المتغيرات تلقائياً قيود الصندوق.

**نقاط بداية متعددة**: نظراً لأن الانحدار التدرجي يخاطر بالحد الأدنى المحلي، يأخذ الهجوم عينات من نقاط بداية عشوائية متعددة بشكل موحد ضمن نصف قطر $r$ (أفضل حل تم العثور عليه حتى الآن) ويشغل الانحدار التدرجي من كل منها. هذا يقلل من احتمالية الوقوع في الحد الأدنى المحلي.

يوضح الشكل 3 والشكل 12 هجوم L₂ على MNIST وCIFAR-10، حيث تكون جميع الأمثلة الخصامية تقريباً غير قابلة للتمييز بصرياً عن النسخ الأصلية.

## VI-B هجوم L₀ الخاص بنا

مقياس L₀ غير قابل للاشتقاق، وغير مناسب للانحدار التدرجي القياسي. بدلاً من ذلك، تحدد الخوارزمية بشكل تكراري البكسلات غير المهمة:

**الخوارزمية:**
1. استدعاء خصم L₂ على مجموعة البكسلات المسموح بها الحالية
2. حساب التدرج $g = \nabla f(x+\delta)$
3. تثبيت البكسل $i = \arg\min_i g_i \cdot \delta_i$ (إزالة من المجموعة المسموح بها)
4. تكرار حتى يفشل خصم L₂

يشير معيار الاختيار $g_i \cdot \delta_i$ إلى مقدار تقليل $f$ الناتج عن تغيير البكسل $i$: يُظهر $g_i$ التقليل لكل وحدة، مضروباً في التغيير الفعلي $\delta_i$. يؤدي الاختيار بناءً على $\delta_i$ وحده إلى نتائج أسوأ بمقدار 1.5 مرة.

على عكس JSMA الذي ينمي مجموعة بكسل من الفراغ، يقلص هذا الهجوم المجموعة من الكامل. **تحسين البداية الدافئة** يهيئ الانحدار التدرجي من حل التكرار السابق، مما يقلل بشكل كبير من الحساب المطلوب.

تتطلب الخوارزمية اختيار الثابت $c$ للإجراء الفرعي L₂. بدءاً من $c = 10^{-4}$، يتضاعف $c$ بعد كل فشل حتى النجاح (أو يتم تجاوز العتبة $10^{10}$).

يُظهر الشكل 4 والشكل 11 هجمات L₀ على MNIST وCIFAR-10. تصبح الفروق البصرية ملحوظة، مما يكشف أن قيود L₀ أكثر صعوبة من L₂.

## VI-C هجوم L∞ الخاص بنا

يفشل تحسين L∞ الساذج لأن $||\delta||_\infty$ يعاقب فقط الإحداثي الأقصى، تاركاً الآخرين غير مقيدة. يتأرجح الانحدار التدرجي بين حلول معادلة حيث تكون إحداثيات مختلفة قصوى.

يستخدم الحل هجوماً تكرارياً يستبدل مصطلح L₂ بعقوبات للقيم التي تتجاوز العتبة $\tau$:

$$\text{minimize } c \cdot f(x+\delta) + \sum_i [(\delta_i - \tau)^+]$$

أدنى: $c \cdot f(x+\delta) + \sum_i [(\delta_i - \tau)^+]$

حيث:
- $(\delta_i - \tau)^+ = \max(0, \delta_i - \tau)$: عقوبة لتجاوز العتبة
- $\tau$: عتبة الاضطراب (perturbation threshold)

بعد كل تكرار، إذا كان كل $\delta_i < \tau$، قلل $\tau$ بعامل 0.9 وكرر؛ وإلا أنهِ.

يتبع اختيار الثابت $c$ نهج L₀: ابدأ منخفضاً، ضاعف بعد الفشل. يضمن تحسين البداية الدافئة سرعة قابلة للمقارنة مع هجمات L₂ ذات النقطة الواحدة.

يوضح الشكل 5 والشكل 13 هجمات L∞. معظم الفروق غير ملحوظة بصرياً، باستثناء تحويل 7→6 الملحوظ.

---

### Translation Notes

- **Figures referenced:** Figures 3, 4, 5, 11, 12, 13
- **Key terms introduced:**
  - Confidence parameter (معامل الثقة)
  - Multiple starting points (نقاط بداية متعددة)
  - Local minimum entrapment (الوقوع في الحد الأدنى المحلي)
  - Warm-start optimization (تحسين البداية الدافئة)
  - Non-differentiable (غير قابل للاشتقاق)
  - Allowed pixel set (مجموعة البكسلات المسموح بها)
  - Threshold reduction (تقليل العتبة)
  - Iterative attack (هجوم تكراري)

- **Equations:**
  - L₂ attack optimization with tanh transformation
  - Confidence-based objective function with κ
  - L∞ attack optimization with threshold τ
  - All preserved in LaTeX with Arabic explanations

- **Citations:** None specific in this section
- **Special handling:**
  - Detailed algorithm description for L₀ attack
  - Explanation of why naive L∞ fails (oscillation problem)
  - Warm-start technique explained as key optimization
  - Visual imperceptibility noted for most attacks
  - Specific example mentioned: 7→6 transformation
  - Factor comparisons preserved (1.5× worse, 0.9 reduction factor)

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86

**Notes:** This section describes the three main C&W attacks that became standard benchmarks. The L₀ attack algorithm is explained step-by-step. The mathematical formulations are preserved with clear Arabic explanations. The warm-start optimization technique is a key innovation and is clearly explained. The iterative threshold reduction for L∞ is well-described. References to figures show visual examples of attacks.
