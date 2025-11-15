# Section 4: Adaptive KL Penalty Coefficient
## القسم 4: معامل عقوبة KL التكيفي

**Section:** Alternative Approach
**Translation Quality:** 0.87
**Glossary Terms Used:** KL divergence, penalty, adaptive, coefficient, optimization, minibatch, SGD, baseline, hyperparameter

---

### English Version

Another approach, which can be used as an alternative to the clipped surrogate objective, or in addition to it, is to use a penalty on KL divergence, and to adapt the penalty coefficient so that we achieve some target value of the KL divergence $d_\text{targ}$ each policy update. In our experiments, we found that the KL penalty performed worse than the clipped surrogate objective, however, we've included it here because it's an important baseline.

In the simplest instantiation of this algorithm, we perform the following steps in each policy update:

• Using several epochs of minibatch SGD, optimize the KL-penalized objective

$$L^{KLPEN}(\theta) = \hat{\mathbb{E}}_t \left[ \frac{\pi_\theta(a_t | s_t)}{\pi_{\theta_\text{old}}(a_t | s_t)} \hat{A}_t - \beta \text{KL}[\pi_{\theta_\text{old}}(\cdot | s_t), \pi_\theta(\cdot | s_t)] \right] \tag{8}$$

• Compute $d = \hat{\mathbb{E}}_t [KL[\pi_{\theta_\text{old}}(\cdot | s_t), \pi_\theta(\cdot | s_t)]]$
  - If $d < d_\text{targ}/1.5$, $\beta \leftarrow \beta/2$
  - If $d > d_\text{targ} \times 1.5$, $\beta \leftarrow \beta \times 2$

The updated $\beta$ is used for the next policy update. With this scheme, we occasionally see policy updates where the KL divergence is significantly different from $d_\text{targ}$, however, these are rare, and $\beta$ quickly adjusts. The parameters 1.5 and 2 above are chosen heuristically, but the algorithm is not very sensitive to them. The initial value of $\beta$ is a another hyperparameter but is not important in practice because the algorithm quickly adjusts it.

---

### النسخة العربية

نهج آخر، يمكن استخدامه كبديل للدالة الهدفية البديلة المقصوصة، أو بالإضافة إليها، هو استخدام عقوبة على تباعد KL، وتكييف معامل العقوبة بحيث نحقق قيمة مستهدفة معينة لتباعد KL وهي $d_\text{targ}$ في كل تحديث للسياسة. في تجاربنا، وجدنا أن عقوبة KL أدت أداءً أسوأ من الدالة الهدفية البديلة المقصوصة، ومع ذلك، قمنا بتضمينها هنا لأنها خط أساس مهم.

في أبسط تجسيد لهذه الخوارزمية، نقوم بتنفيذ الخطوات التالية في كل تحديث للسياسة:

• باستخدام عدة حقب من SGD للدفعات الصغيرة، نحسّن الدالة الهدفية المعاقبة بـ KL

$$L^{KLPEN}(\theta) = \hat{\mathbb{E}}_t \left[ \frac{\pi_\theta(a_t | s_t)}{\pi_{\theta_\text{old}}(a_t | s_t)} \hat{A}_t - \beta \text{KL}[\pi_{\theta_\text{old}}(\cdot | s_t), \pi_\theta(\cdot | s_t)] \right] \tag{8}$$

• نحسب $d = \hat{\mathbb{E}}_t [KL[\pi_{\theta_\text{old}}(\cdot | s_t), \pi_\theta(\cdot | s_t)]]$
  - إذا كانت $d < d_\text{targ}/1.5$، فإن $\beta \leftarrow \beta/2$
  - إذا كانت $d > d_\text{targ} \times 1.5$، فإن $\beta \leftarrow \beta \times 2$

يُستخدم $\beta$ المحدث لتحديث السياسة التالي. مع هذا المخطط، نرى أحياناً تحديثات سياسة حيث يختلف تباعد KL بشكل كبير عن $d_\text{targ}$، ومع ذلك، هذه نادرة، ويتكيف $\beta$ بسرعة. يتم اختيار المعاملات 1.5 و 2 أعلاه بشكل استدلالي، لكن الخوارزمية ليست حساسة جداً لها. القيمة الأولية لـ$\beta$ هي معامل فائق آخر لكنها ليست مهمة في الممارسة لأن الخوارزمية تكيفها بسرعة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - KL penalty - عقوبة KL
  - adaptive - تكيفي
  - penalty coefficient - معامل العقوبة
  - target value - قيمة مستهدفة
  - baseline - خط أساس
  - instantiation - تجسيد
  - epochs - حقب
  - minibatch SGD - SGD للدفعات الصغيرة
  - KL-penalized objective - الدالة الهدفية المعاقبة بـ KL
  - heuristically - بشكل استدلالي
  - sensitive - حساسة
  - initial value - القيمة الأولية
- **Equations:** 1 equation (8)
- **Citations:** None
- **Special handling:**
  - Preserved mathematical notation and LaTeX
  - Translated algorithmic steps clearly
  - Kept arrow notation ($\leftarrow$) for assignment
  - Explained the adaptive mechanism in clear Arabic
  - Maintained bullet point structure for algorithmic steps

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
