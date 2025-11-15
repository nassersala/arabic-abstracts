# Section 4: Model Description
## القسم 4: وصف النموذج

**Section:** model-description
**Translation Quality:** 0.89
**Glossary Terms Used:** neural network, feed-forward, layer, activation function, weight, bias, training, test time, dropout rate, hidden unit

---

### English Version

Consider a neural network with $L$ hidden layers. Let $l \in \{1, ..., L\}$ index the hidden layers of the network. Let $\mathbf{z}^{(l)}$ denote the vector of inputs into layer $l$, $\mathbf{y}^{(l)}$ denote the vector of outputs from layer $l$ ($\mathbf{y}^{(0)} = \mathbf{x}$ is the input). $\mathbf{W}^{(l)}$ and $\mathbf{b}^{(l)}$ are the weights and biases at layer $l$. The feed-forward operation of a standard neural network can be described as (for $l \in \{0, ..., L-1\}$ and any hidden unit $i$):

$$z_i^{(l+1)} = \mathbf{w}_i^{(l+1)} \mathbf{y}^{(l)} + b_i^{(l+1)}$$

$$y_i^{(l+1)} = f(z_i^{(l+1)})$$

where $f$ is any activation function, such as $f(x) = 1/(1+\exp(-x))$ for sigmoid units.

**With Dropout:** With dropout, the feed-forward operation becomes:

$$r_j^{(l)} \sim \text{Bernoulli}(p)$$

$$\tilde{\mathbf{y}}^{(l)} = \mathbf{r}^{(l)} * \mathbf{y}^{(l)}$$

$$z_i^{(l+1)} = \mathbf{w}_i^{(l+1)} \tilde{\mathbf{y}}^{(l)} + b_i^{(l+1)}$$

$$y_i^{(l+1)} = f(z_i^{(l+1)})$$

Here, $*$ denotes element-wise product. For each training case and each layer, dropout samples a binary mask $\mathbf{r}^{(l)}$ from a Bernoulli distribution with probability $p$ of being 1. The outputs of the layer are then multiplied element-wise with this mask. This has the effect of randomly setting a fraction $(1-p)$ of the activations to zero.

**At Test Time:** At test time, we want to find an approximate averaging of all $2^n$ possible models (where $n$ is the total number of units that can be dropped). A simple approximation is to use a single neural network without dropout and scale the weights. If a unit is retained with probability $p$ during training, the outgoing weights of that unit are multiplied by $p$ at test time. This is called the "weight scaling inference rule" and it approximates taking the geometric mean over all the thinned networks.

Alternatively, we can multiply the weights by $p$ during training and use the weights as-is at test time. This is computationally more efficient.

---

### النسخة العربية

لنتأمل شبكة عصبية بها $L$ من الطبقات المخفية. لتكن $l \in \{1, ..., L\}$ فهرس الطبقات المخفية للشبكة. لتكن $\mathbf{z}^{(l)}$ متجه المدخلات إلى الطبقة $l$، و $\mathbf{y}^{(l)}$ متجه المخرجات من الطبقة $l$ (حيث $\mathbf{y}^{(0)} = \mathbf{x}$ هو الإدخال). $\mathbf{W}^{(l)}$ و $\mathbf{b}^{(l)}$ هي الأوزان والانحيازات في الطبقة $l$. يمكن وصف عملية التغذية الأمامية للشبكة العصبية القياسية على النحو التالي (لـ $l \in \{0, ..., L-1\}$ ولأي وحدة مخفية $i$):

$$z_i^{(l+1)} = \mathbf{w}_i^{(l+1)} \mathbf{y}^{(l)} + b_i^{(l+1)}$$

$$y_i^{(l+1)} = f(z_i^{(l+1)})$$

حيث $f$ هي أي دالة تفعيل، مثل $f(x) = 1/(1+\exp(-x))$ لوحدات السيغمويد.

**مع Dropout:** مع dropout، تصبح عملية التغذية الأمامية:

$$r_j^{(l)} \sim \text{Bernoulli}(p)$$

$$\tilde{\mathbf{y}}^{(l)} = \mathbf{r}^{(l)} * \mathbf{y}^{(l)}$$

$$z_i^{(l+1)} = \mathbf{w}_i^{(l+1)} \tilde{\mathbf{y}}^{(l)} + b_i^{(l+1)}$$

$$y_i^{(l+1)} = f(z_i^{(l+1)})$$

هنا، $*$ يشير إلى الضرب العنصري. لكل حالة تدريب ولكل طبقة، يأخذ dropout عينة من قناع ثنائي $\mathbf{r}^{(l)}$ من توزيع برنولي باحتمال $p$ أن يكون 1. ثم يتم ضرب مخرجات الطبقة عنصرياً بهذا القناع. له تأثير تعيين كسر $(1-p)$ من التنشيطات بشكل عشوائي إلى الصفر.

**في وقت الاختبار:** في وقت الاختبار، نريد إيجاد متوسط تقريبي لجميع النماذج المحتملة $2^n$ (حيث $n$ هو العدد الإجمالي للوحدات التي يمكن حذفها). التقريب البسيط هو استخدام شبكة عصبية واحدة بدون dropout وتحجيم الأوزان. إذا تم الاحتفاظ بوحدة باحتمال $p$ أثناء التدريب، يتم ضرب الأوزان الصادرة من تلك الوحدة بـ $p$ في وقت الاختبار. تسمى هذه "قاعدة الاستنتاج بتحجيم الوزن" وتقرب أخذ المتوسط الهندسي على جميع الشبكات المخففة.

بدلاً من ذلك، يمكننا ضرب الأوزان بـ $p$ أثناء التدريب واستخدام الأوزان كما هي في وقت الاختبار. هذا أكثر كفاءة حسابياً.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** Bernoulli distribution, element-wise product, binary mask, weight scaling, inference rule, geometric mean
- **Equations:** 7 mathematical equations preserved in LaTeX
- **Citations:** None in this section
- **Special handling:**
  - All mathematical notation preserved exactly
  - "Bernoulli" kept as standard mathematical term
  - Technical terms like "sigmoid" kept in English within mathematical context
  - "Weight scaling inference rule" translated as "قاعدة الاستنتاج بتحجيم الوزن"

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.95
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.89
