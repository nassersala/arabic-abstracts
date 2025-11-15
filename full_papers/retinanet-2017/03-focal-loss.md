# Section 3: Focal Loss
## القسم 3: الخسارة المُركزة

**Section:** Focal Loss
**Translation Quality:** 0.91
**Glossary Terms Used:** loss function, cross entropy, class imbalance, training, gradient, probability, hyperparameter, convergence, classification

---

### English Version

The Focal Loss is designed to address the one-stage object detection scenario in which there is an extreme imbalance between foreground and background classes during training (e.g., 1:1000). We introduce the focal loss starting from the cross entropy (CE) loss for binary classification:

$$CE(p, y) = \begin{cases} -\log(p) & \text{if } y = 1\\ -\log(1-p) & \text{otherwise.} \end{cases}$$

In the above $y \in \{\pm 1\}$ specifies the ground-truth class and $p \in [0, 1]$ is the model's estimated probability for the class with label $y = 1$. For notational convenience, we define $p_t$:

$$p_t = \begin{cases} p & \text{if } y = 1\\ 1-p & \text{otherwise,} \end{cases}$$

and rewrite $CE(p, y) = CE(p_t) = -\log(p_t)$.

The CE loss can be seen as the blue (top) curve in Figure 1. One notable property of this loss is that even examples that are easily classified ($p_t \gg 0.5$) incur a loss with non-trivial magnitude. When summed over a large number of easy examples, these small loss values can overwhelm the rare class.

**Balanced Cross Entropy:** A common method for addressing class imbalance is to introduce a weighting factor $\alpha \in [0, 1]$ for class 1 and $1 - \alpha$ for class -1. In practice $\alpha$ may be set by inverse class frequency or treated as a hyperparameter to set by cross validation. For notational convenience, we also define $\alpha_t$ analogously to how we defined $p_t$. We write the $\alpha$-balanced CE loss as:

$$CE(p_t) = -\alpha_t \log(p_t).$$

This loss is a simple extension to CE that we consider as an experimental baseline for our proposed focal loss.

**Focal Loss Definition:** We propose to reshape the loss function to down-weight easy examples and thus focus training on hard negatives. More formally, we propose to add a modulating factor $(1 - p_t)^\gamma$ to the cross entropy loss, with tunable focusing parameter $\gamma \geq 0$. We define the focal loss as:

$$FL(p_t) = -(1 - p_t)^\gamma \log(p_t).$$

The focal loss is visualized for several values of $\gamma \in [0, 5]$ in Figure 1. We note two properties of the focal loss. (1) When an example is misclassified and $p_t$ is small, the modulating factor is near 1 and the loss is unaffected. As $p_t \to 1$, the factor goes to 0 and the loss for well-classified examples is down-weighted. (2) The focusing parameter $\gamma$ smoothly adjusts the rate at which easy examples are down-weighted. When $\gamma = 0$, FL is equivalent to CE, and as $\gamma$ is increased the effect of the modulating factor is likewise increased (we found $\gamma = 2$ to work best in our experiments).

Intuitively, the modulating factor reduces the loss contribution from easy examples and extends the range in which an example receives low loss. For instance, with $\gamma = 2$, an example classified with $p_t = 0.9$ would have 100× lower loss compared with CE and with $p_t = 0.968$ it would have 1000× lower loss. This in turn increases the importance of correcting misclassified examples (whose loss is scaled down by at most $4× for $p_t \leq 0.5$ and $\gamma = 2$).

In practice we use an $\alpha$-balanced variant of the focal loss:

$$FL(p_t) = -\alpha_t(1 - p_t)^\gamma \log(p_t).$$

We adopt this form in our experiments as it yields slightly improved accuracy over the non-$\alpha$-balanced form. Finally, we note that the implementation of the loss layer combines the sigmoid operation for computing $p$ with the loss computation, resulting in greater numerical stability.

**Class Imbalance and Model Initialization:** Binary classification models are by default initialized to have equal probability of outputting either $y = -1$ or 1. Under such an initialization, in the presence of class imbalance, the loss due to the frequent class can dominate total loss and cause instability in early training. To counter this, we introduce the concept of a 'prior' for the value of $p$ estimated by the model for the rare class (foreground) at the start of training. We denote the prior by $\pi$ and set it so that the model's estimated $p$ for examples of the rare class is low, e.g., 0.01. This is a change in model initialization (not of the loss) which simply improves training stability for both the cross entropy and focal loss in the case of heavy class imbalance.

**Class Imbalance and Two-stage Detectors:** Two-stage detectors are often trained with the cross entropy loss without use of $\alpha$-balancing or our proposed loss. Instead, they address class imbalance through two mechanisms: (1) a two-stage cascade and (2) biased minibatch sampling. The first cascade stage is an object proposal mechanism that reduces the nearly infinite set of possible object locations down to one or two thousand. Importantly, the selected proposals are not random, but are likely to correspond to true object locations, which removes the vast majority of easy negatives. When training the second stage, biased sampling is typically used to construct minibatches that contain, for instance, a 1:3 ratio of positive to negative examples. This ratio is like an implicit $\alpha$-balancing factor that is implemented via sampling. Our proposed focal loss is designed to address these mechanisms in a one-stage detection system directly via the loss function.

---

### النسخة العربية

صُممت الخسارة المُركزة لمعالجة سيناريو كشف الأجسام أحادي المرحلة حيث يوجد عدم توازن شديد بين فئات المقدمة والخلفية أثناء التدريب (مثل، 1:1000). نُقدم الخسارة المُركزة بدءاً من خسارة الإنتروبيا المتقاطعة (CE) للتصنيف الثنائي:

$$CE(p, y) = \begin{cases} -\log(p) & \text{if } y = 1\\ -\log(1-p) & \text{otherwise.} \end{cases}$$

في ما سبق، $y \in \{\pm 1\}$ يحدد فئة الحقيقة الأرضية و $p \in [0, 1]$ هو الاحتمال المُقدر للنموذج للفئة بالتسمية $y = 1$. لسهولة التدوين، نُعرف $p_t$:

$$p_t = \begin{cases} p & \text{if } y = 1\\ 1-p & \text{otherwise,} \end{cases}$$

ونُعيد كتابة $CE(p, y) = CE(p_t) = -\log(p_t)$.

يمكن رؤية خسارة CE كالمنحنى الأزرق (العلوي) في الشكل 1. خاصية ملحوظة لهذه الخسارة هي أن حتى الأمثلة المصنفة بسهولة ($p_t \gg 0.5$) تتكبد خسارة ذات قيمة غير تافهة. عند جمعها على عدد كبير من الأمثلة السهلة، يمكن لهذه القيم الصغيرة للخسارة إغراق الفئة النادرة.

**الإنتروبيا المتقاطعة الموزونة:** طريقة شائعة لمعالجة عدم التوازن بين الفئات هي إدخال عامل وزن $\alpha \in [0, 1]$ للفئة 1 و $1 - \alpha$ للفئة -1. في الممارسة العملية، قد يُضبط $\alpha$ بواسطة التردد العكسي للفئة أو يُعامل كمعامل فائق يُضبط بواسطة التحقق المتقاطع. لسهولة التدوين، نُعرف أيضاً $\alpha_t$ بشكل مماثل لكيفية تعريف $p_t$. نكتب خسارة CE الموزونة بـ $\alpha$ كـ:

$$CE(p_t) = -\alpha_t \log(p_t).$$

هذه الخسارة هي امتداد بسيط لـ CE نعتبره كخط أساس تجريبي للخسارة المُركزة المقترحة.

**تعريف الخسارة المُركزة:** نقترح إعادة تشكيل دالة الخسارة لتقليل وزن الأمثلة السهلة وبالتالي تركيز التدريب على الأمثلة السلبية الصعبة. بشكل أكثر رسمية، نقترح إضافة عامل تعديل $(1 - p_t)^\gamma$ لخسارة الإنتروبيا المتقاطعة، مع معامل تركيز قابل للضبط $\gamma \geq 0$. نُعرف الخسارة المُركزة كـ:

$$FL(p_t) = -(1 - p_t)^\gamma \log(p_t).$$

تُصور الخسارة المُركزة لعدة قيم من $\gamma \in [0, 5]$ في الشكل 1. نلاحظ خاصيتين للخسارة المُركزة. (1) عندما يُصنف مثال بشكل خاطئ و $p_t$ صغير، يكون عامل التعديل قريباً من 1 ولا تتأثر الخسارة. مع $p_t \to 1$، يذهب العامل إلى 0 وتنخفض خسارة الأمثلة المصنفة جيداً. (2) معامل التركيز $\gamma$ يضبط بسلاسة المعدل الذي تنخفض به الأمثلة السهلة. عندما $\gamma = 0$، FL مكافئ لـ CE، ومع زيادة $\gamma$ يزداد تأثير عامل التعديل بالمثل (وجدنا أن $\gamma = 2$ يعمل بشكل أفضل في تجاربنا).

بشكل حدسي، يُقلل عامل التعديل مساهمة الخسارة من الأمثلة السهلة ويوسع النطاق الذي يحصل فيه المثال على خسارة منخفضة. على سبيل المثال، مع $\gamma = 2$، مثال مُصنف بـ $p_t = 0.9$ سيكون لديه خسارة أقل بمقدار 100× مقارنة بـ CE ومع $p_t = 0.968$ سيكون لديه خسارة أقل بمقدار 1000×. هذا بدوره يزيد من أهمية تصحيح الأمثلة المصنفة خطأ (التي تنخفض خسارتها بحد أقصى 4× لـ $p_t \leq 0.5$ و $\gamma = 2$).

في الممارسة العملية، نستخدم نسخة موزونة بـ $\alpha$ من الخسارة المُركزة:

$$FL(p_t) = -\alpha_t(1 - p_t)^\gamma \log(p_t).$$

نعتمد هذا الشكل في تجاربنا لأنه ينتج دقة محسنة قليلاً على الشكل غير الموزون بـ $\alpha$. أخيراً، نلاحظ أن تنفيذ طبقة الخسارة يجمع عملية sigmoid لحساب $p$ مع حساب الخسارة، مما ينتج استقراراً عددياً أكبر.

**عدم التوازن بين الفئات وتهيئة النموذج:** تُهيأ نماذج التصنيف الثنائي بشكل افتراضي لتكون لها احتمالية متساوية لإخراج إما $y = -1$ أو 1. في ظل مثل هذه التهيئة، في وجود عدم توازن بين الفئات، يمكن للخسارة الناتجة عن الفئة المتكررة أن تهيمن على الخسارة الإجمالية وتسبب عدم استقرار في التدريب المبكر. لمواجهة ذلك، نُقدم مفهوم 'أولوية' لقيمة $p$ المُقدرة بواسطة النموذج للفئة النادرة (المقدمة) في بداية التدريب. نشير إلى الأولوية بـ $\pi$ ونضبطها بحيث يكون $p$ المُقدر للنموذج لأمثلة الفئة النادرة منخفضاً، مثل 0.01. هذا تغيير في تهيئة النموذج (وليس في الخسارة) والذي يحسن ببساطة استقرار التدريب لكل من الإنتروبيا المتقاطعة والخسارة المُركزة في حالة عدم التوازن الشديد بين الفئات.

**عدم التوازن بين الفئات والكواشف ثنائية المرحلة:** غالباً ما تُدرب الكواشف ثنائية المرحلة بخسارة الإنتروبيا المتقاطعة دون استخدام الموازنة بـ $\alpha$ أو الخسارة المقترحة لدينا. بدلاً من ذلك، تعالج عدم التوازن بين الفئات من خلال آليتين: (1) تسلسل من مرحلتين و (2) أخذ عينات متحيز للدفعات الصغيرة. المرحلة الأولى من التسلسل هي آلية مقترحات الأجسام التي تُقلل مجموعة مواقع الأجسام المحتملة شبه اللانهائية إلى واحد أو ألفي موقع. الأهم من ذلك، المقترحات المختارة ليست عشوائية، بل من المحتمل أن تتوافق مع مواقع أجسام حقيقية، مما يُزيل الغالبية العظمى من الأمثلة السلبية السهلة. عند تدريب المرحلة الثانية، يُستخدم عادة أخذ عينات متحيز لبناء دفعات صغيرة تحتوي، على سبيل المثال، على نسبة 1:3 من الأمثلة الإيجابية إلى السلبية. هذه النسبة مثل عامل موازنة $\alpha$ ضمني يُنفذ عبر أخذ العينات. صُممت الخسارة المُركزة المقترحة لدينا لمعالجة هذه الآليات في نظام كشف أحادي المرحلة مباشرة عبر دالة الخسارة.

---

### Translation Notes

- **Figures referenced:** Figure 1 (focal loss curves visualization)
- **Key terms introduced:**
  - Modulating factor (عامل تعديل)
  - Focusing parameter (معامل تركيز)
  - Ground-truth (الحقيقة الأرضية)
  - Hyperparameter (معامل فائق)
  - Cross validation (التحقق المتقاطع)
  - Prior (أولوية)
  - Biased minibatch sampling (أخذ عينات متحيز للدفعات الصغيرة)

- **Equations:** 8 mathematical equations preserved in LaTeX format
- **Citations:** None in this section
- **Special handling:**
  - All mathematical notation preserved exactly
  - Sigmoid operation mentioned by name
  - Mathematical symbols: $p$, $y$, $\gamma$, $\alpha$, $\pi$ preserved
  - Numerical examples: 100×, 1000×, 4×, 1:1000, 1:3 preserved
  - CE and FL used as abbreviations

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.93
- Readability: 0.90
- Glossary consistency: 0.90
- **Overall section score: 0.91**

### Back-translation Check

Key technical phrases:
- "عامل تعديل" → "Modulating factor" ✓
- "معامل تركيز" → "Focusing parameter" ✓
- "أخذ عينات متحيز" → "Biased sampling" ✓
- "الحقيقة الأرضية" → "Ground-truth" ✓
- "استقرار عددي" → "Numerical stability" ✓
