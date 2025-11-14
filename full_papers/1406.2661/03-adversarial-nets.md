# Section 3: Adversarial Nets
## القسم 3: الشبكات التنافسية الخصامية

**Section:** Adversarial Nets
**Translation Quality:** 0.87
**Glossary Terms Used:** multilayer perceptron, generator, discriminator, prior, mapping, differentiable function, minimax game, value function, training, gradient, backpropagation

---

### English Version

The adversarial modeling framework is most straightforward to apply when the models are both multilayer perceptrons. To learn the generator's distribution $p_g$ over data $x$, we define a prior on input noise variables $p_z(z)$, then represent a mapping to data space as $G(z; \theta_g)$, where $G$ is a differentiable function represented by a multilayer perceptron with parameters $\theta_g$. We also define a second multilayer perceptron $D(x; \theta_d)$ that outputs a single scalar. $D(x)$ represents the probability that $x$ came from the data rather than $p_g$. We train $D$ to maximize the probability of assigning the correct label to both training examples and samples from $G$. We simultaneously train $G$ to minimize $\log(1 - D(G(z)))$:

In other words, $D$ and $G$ play the following two-player minimax game with value function $V(G, D)$:

$$\min_G \max_D V(D, G) = \mathbb{E}_{x \sim p_{data}(x)}[\log D(x)] + \mathbb{E}_{z \sim p_z(z)}[\log(1 - D(G(z)))].$$
(1)

In the next section, we present a theoretical analysis of adversarial nets, essentially showing that the training criterion allows one to recover the data generating distribution as $G$ and $D$ are given enough capacity, i.e., in the non-parametric limit. See Figure 1 for a less formal, more pedagogical explanation of the approach. In practice, we must implement the game using an iterative, numerical approach. Optimizing $D$ to completion in the inner loop of training is computationally prohibitive, and on finite datasets would result in overfitting. Instead, we alternate between $k$ steps of optimizing $D$ and one step of optimizing $G$. This results in $D$ being maintained near its optimal solution, so long as $G$ changes slowly enough. This strategy is analogous to the way that SML/PCD [31, 29] training maintains samples from a Markov chain from one learning step to the next in order to avoid burning in a Markov chain as part of the inner loop of learning. The procedure is formally presented in Algorithm 1.

In practice, equation 1 may not provide sufficient gradient for $G$ to learn well. Early in learning, when $G$ is poor, $D$ can reject samples with high confidence because they are clearly different from the training data. In this case, $\log(1 - D(G(z)))$ saturates. Rather than training $G$ to minimize $\log(1 - D(G(z)))$ we can train $G$ to maximize $\log D(G(z))$. This objective function results in the same fixed point of the dynamics of $G$ and $D$ but provides much stronger gradients early in learning.

---

### النسخة العربية

إطار النمذجة التنافسية الخصامية هو الأكثر وضوحاً في التطبيق عندما يكون كلا النموذجين عبارة عن بيرسبترونات متعددة الطبقات. لتعلم توزيع المولد $p_g$ على البيانات $x$، نحدد توزيعاً أولياً على متغيرات الضوضاء المدخلة $p_z(z)$، ثم نمثل تعييناً إلى فضاء البيانات بالصيغة $G(z; \theta_g)$، حيث $G$ دالة قابلة للاشتقاق ممثلة ببيرسبترون متعدد الطبقات بمعلمات $\theta_g$. نحدد أيضاً بيرسبتروناً ثانياً متعدد الطبقات $D(x; \theta_d)$ الذي يعطي قيمة قياسية واحدة. يمثل $D(x)$ الاحتمالية أن $x$ جاء من البيانات بدلاً من $p_g$. ندرب $D$ لتعظيم احتمالية تخصيص التسمية الصحيحة لكل من أمثلة التدريب والعينات من $G$. ندرب $G$ في نفس الوقت لتصغير $\log(1 - D(G(z)))$:

بعبارة أخرى، $D$ و $G$ يلعبان لعبة minimax ثنائية اللاعبين التالية بدالة القيمة $V(G, D)$:

$$\min_G \max_D V(D, G) = \mathbb{E}_{x \sim p_{data}(x)}[\log D(x)] + \mathbb{E}_{z \sim p_z(z)}[\log(1 - D(G(z)))].$$
(1)

في القسم التالي، نقدم تحليلاً نظرياً للشبكات التنافسية الخصامية، نبين فيه بشكل أساسي أن معيار التدريب يسمح باسترداد توزيع توليد البيانات عندما يُعطى $G$ و $D$ سعة كافية، أي في الحد اللامعلمي. انظر الشكل 1 للحصول على شرح أقل رسمية وأكثر تعليمية للنهج. في الممارسة العملية، يجب أن ننفذ اللعبة باستخدام نهج تكراري عددي. تحسين $D$ حتى الاكتمال في الحلقة الداخلية للتدريب مكلف حسابياً، وعلى مجموعات البيانات المحدودة سيؤدي إلى الإفراط في التلاؤم. بدلاً من ذلك، نتناوب بين $k$ خطوات لتحسين $D$ وخطوة واحدة لتحسين $G$. ينتج عن هذا الحفاظ على $D$ بالقرب من حله الأمثل، طالما أن $G$ يتغير ببطء كافٍ. هذه الاستراتيجية مماثلة للطريقة التي يحافظ بها تدريب SML/PCD [31، 29] على العينات من سلسلة ماركوف من خطوة تعلم إلى التالية لتجنب الحرق في سلسلة ماركوف كجزء من الحلقة الداخلية للتعلم. يتم عرض الإجراء رسمياً في الخوارزمية 1.

في الممارسة العملية، قد لا توفر المعادلة 1 تدرجاً كافياً لـ $G$ للتعلم بشكل جيد. في وقت مبكر من التعلم، عندما يكون $G$ ضعيفاً، يمكن لـ $D$ رفض العينات بثقة عالية لأنها مختلفة بوضوح عن بيانات التدريب. في هذه الحالة، يتشبع $\log(1 - D(G(z)))$. بدلاً من تدريب $G$ لتصغير $\log(1 - D(G(z)))$ يمكننا تدريب $G$ لتعظيم $\log D(G(z))$. تنتج دالة الهدف هذه نفس النقطة الثابتة لديناميكيات $G$ و $D$ ولكنها توفر تدرجات أقوى بكثير في وقت مبكر من التعلم.

---

### Translation Notes

- **Figures referenced:** Figure 1 (mentioned but not shown in this section)
- **Key terms introduced:**
  - minimax game (لعبة minimax)
  - value function (دالة القيمة)
  - non-parametric limit (الحد اللامعلمي)
  - saturate (يتشبع)
  - fixed point (النقطة الثابتة)
- **Equations:**
  - Equation (1): Main minimax objective function (preserved in LaTeX)
  - Multiple inline equations with $G$, $D$, $p_g$, $p_z$ notation
- **Citations:** [31, 29]
- **Special handling:**
  - Mathematical notation kept in LaTeX format as specified
  - "minimax" kept in English as it's a standard game theory term
  - Algorithm 1 reference preserved (algorithm itself will be in section 4)
  - SML/PCD acronyms kept as-is (Stochastic Maximum Likelihood / Persistent Contrastive Divergence)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87

### Back-Translation (Key Technical Paragraph)

"In other words, $D$ and $G$ play the following two-player minimax game with value function $V(G, D)$:
[equation]
In the next section, we present a theoretical analysis of adversarial nets, showing essentially that the training criterion allows recovering the data generation distribution when $G$ and $D$ are given sufficient capacity, i.e., in the non-parametric limit."

**Validation:** ✅ Technical content accurately preserved. Mathematical formulation intact.
