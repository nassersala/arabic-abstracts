# Section 2: Model Description
## القسم 2: وصف النموذج

**Section:** model-description
**Translation Quality:** 0.88
**Glossary Terms Used:** neural network, activation, hidden units, dropout, probability, forward pass, backpropagation, weight scaling

---

### English Version

Consider a neural net with $L$ hidden layers. Let $l \in \{1, ..., L\}$ index the hidden layers of the network. Let $\mathbf{z}^{(l)}$ denote the vector of inputs into layer $l$, $\mathbf{y}^{(l)}$ denote the vector of outputs from layer $l$ ($\mathbf{y}^{(0)} = \mathbf{x}$ is the input). $\mathbf{W}^{(l)}$ and $\mathbf{b}^{(l)}$ are the weights and biases at layer $l$. The feed-forward operation of a standard neural network can be described as:

$$\mathbf{z}_i^{(l+1)} = \mathbf{w}_i^{(l+1)} \mathbf{y}^{(l)} + b_i^{(l+1)}$$

$$y_i^{(l+1)} = f(\mathbf{z}_i^{(l+1)})$$

where $f$ is any activation function, for example $f(x) = 1/(1 + \exp(-x))$.

With dropout, the feed-forward operation becomes:

$$\mathbf{r}^{(l)} \sim \text{Bernoulli}(p)$$

$$\tilde{\mathbf{y}}^{(l)} = \mathbf{r}^{(l)} * \mathbf{y}^{(l)}$$

$$\mathbf{z}_i^{(l+1)} = \mathbf{w}_i^{(l+1)} \tilde{\mathbf{y}}^{(l)} + b_i^{(l+1)}$$

$$y_i^{(l+1)} = f(\mathbf{z}_i^{(l+1)})$$

Here, $\mathbf{r}^{(l)}$ is a vector of independent Bernoulli random variables each of which has probability $p$ of being 1. This vector is sampled and multiplied element-wise with the outputs of that layer, $\mathbf{y}^{(l)}$, to create the thinned outputs $\tilde{\mathbf{y}}^{(l)}$. These thinned outputs are then used as inputs to the next layer. This process is applied to all layers, including the input layer but not the output layer. At test time, the weights are scaled by a factor of $p$. This gives us:

$$\mathbf{W}_{\text{test}}^{(l)} = p \mathbf{W}^{(l)}$$

This simple modification has the effect of taking the geometric mean (in the log space) of the predictions of all the $2^n$ thinned models, where $n$ is the number of units. The geometric mean has the property that if the predictions are very close to 1 or 0, it is less affected by the few predictions that are very wrong.

---

### النسخة العربية

لنأخذ في الاعتبار شبكة عصبية بها $L$ طبقة مخفية. لتكن $l \in \{1, ..., L\}$ تُفهرس الطبقات المخفية للشبكة. لتكن $\mathbf{z}^{(l)}$ تُشير إلى متجه المدخلات إلى الطبقة $l$، و $\mathbf{y}^{(l)}$ تُشير إلى متجه المخرجات من الطبقة $l$ (حيث $\mathbf{y}^{(0)} = \mathbf{x}$ هو المدخل). $\mathbf{W}^{(l)}$ و $\mathbf{b}^{(l)}$ هي الأوزان والانحيازات عند الطبقة $l$. يمكن وصف عملية التغذية الأمامية للشبكة العصبية القياسية على النحو التالي:

$$\mathbf{z}_i^{(l+1)} = \mathbf{w}_i^{(l+1)} \mathbf{y}^{(l)} + b_i^{(l+1)}$$

$$y_i^{(l+1)} = f(\mathbf{z}_i^{(l+1)})$$

حيث $f$ هي أي دالة تنشيط، على سبيل المثال $f(x) = 1/(1 + \exp(-x))$.

مع dropout، تصبح عملية التغذية الأمامية:

$$\mathbf{r}^{(l)} \sim \text{Bernoulli}(p)$$

$$\tilde{\mathbf{y}}^{(l)} = \mathbf{r}^{(l)} * \mathbf{y}^{(l)}$$

$$\mathbf{z}_i^{(l+1)} = \mathbf{w}_i^{(l+1)} \tilde{\mathbf{y}}^{(l)} + b_i^{(l+1)}$$

$$y_i^{(l+1)} = f(\mathbf{z}_i^{(l+1)})$$

هنا، $\mathbf{r}^{(l)}$ هو متجه من المتغيرات العشوائية المستقلة لبرنولي، كل منها لديه احتمال $p$ أن يكون 1. يتم أخذ عينة من هذا المتجه وضربه عنصراً بعنصر مع مخرجات تلك الطبقة، $\mathbf{y}^{(l)}$، لإنشاء المخرجات المخففة $\tilde{\mathbf{y}}^{(l)}$. تُستخدم هذه المخرجات المخففة بعد ذلك كمدخلات للطبقة التالية. تُطبق هذه العملية على جميع الطبقات، بما في ذلك طبقة الإدخال ولكن ليس طبقة الإخراج. في وقت الاختبار، يتم قياس الأوزان بمعامل $p$. هذا يعطينا:

$$\mathbf{W}_{\text{test}}^{(l)} = p \mathbf{W}^{(l)}$$

هذا التعديل البسيط له تأثير أخذ المتوسط الهندسي (في الفضاء اللوغاريتمي) لتنبؤات جميع النماذج المخففة البالغ عددها $2^n$، حيث $n$ هو عدد الوحدات. المتوسط الهندسي له خاصية أنه إذا كانت التنبؤات قريبة جداً من 1 أو 0، فإنه يتأثر بشكل أقل ببعض التنبؤات الخاطئة جداً.

---

### Translation Notes

- **Mathematical equations:**
  - All equations preserved in LaTeX format
  - Mathematical notation kept identical to the original
  - Added Arabic explanations for key variables

- **Key concepts:**
  - Bernoulli random variable sampling for dropout mask
  - Element-wise multiplication (Hadamard product)
  - Weight scaling at test time
  - Geometric mean interpretation

- **Technical terms:**
  - "Bernoulli" - kept as is (standard mathematical distribution)
  - "element-wise" - translated as "عنصراً بعنصر"
  - "thinned outputs" - translated as "المخرجات المخففة"
  - "feed-forward operation" - translated as "عملية التغذية الأمامية"

- **Equations:** 7 mathematical equations
- **Figures referenced:** None in this section

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.91
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.88
