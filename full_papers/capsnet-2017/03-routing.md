# Section 3: Dynamic Routing Algorithm and Margin Loss
## القسم 3: خوارزمية التوجيه الديناميكي ودالة خسارة الهامش

**Section:** methodology - routing algorithm and loss function
**Translation Quality:** 0.90
**Glossary Terms Used:** algorithm, routing, coupling coefficients, softmax, squashing function, iteration, prediction vector, scalar product, loss function, margin, down-weighting

---

### English Version

#### 3.1 Routing Algorithm

The dynamic routing algorithm is at the heart of capsule networks. The procedure is shown in Algorithm 1 below:

**Algorithm 1: Routing algorithm**

**Procedure:** ROUTING($\hat{u}_{j|i}$, $r$, $l$)

1. **for** all capsule $i$ in layer $l$ and capsule $j$ in layer $(l+1)$: $b_{ij} \leftarrow 0$
2. **for** $r$ iterations **do**:
3. &nbsp;&nbsp;&nbsp;&nbsp;**for** all capsule $i$ in layer $l$: $\mathbf{c}_i \leftarrow \text{softmax}(\mathbf{b}_i)$
4. &nbsp;&nbsp;&nbsp;&nbsp;**for** all capsule $j$ in layer $(l+1)$: $s_j \leftarrow \sum_i c_{ij} \hat{u}_{j|i}$
5. &nbsp;&nbsp;&nbsp;&nbsp;**for** all capsule $j$ in layer $(l+1)$: $v_j \leftarrow \text{squash}(s_j)$
6. &nbsp;&nbsp;&nbsp;&nbsp;**for** all capsule $i$ in layer $l$ and capsule $j$ in layer $(l+1)$: $b_{ij} \leftarrow b_{ij} + \hat{u}_{j|i} \cdot v_j$

**return** $v_j$

Where:
- $\hat{u}_{j|i}$ are the prediction vectors from capsules in layer $l$ to layer $l+1$
- $r$ is the number of routing iterations (typically 3)
- $l$ is the layer index
- $b_{ij}$ are the log prior probabilities (coupling logits)
- $c_{ij}$ are the coupling coefficients
- $s_j$ is the total input to capsule $j$
- $v_j$ is the output vector of capsule $j$

The routing procedure starts by initializing all coupling logits $b_{ij}$ to zero, meaning all coupling coefficients are equal. In each iteration, the algorithm computes coupling coefficients via softmax, calculates weighted sums of prediction vectors, applies the squashing function, and then updates the coupling logits based on the agreement (scalar product) between predictions and outputs.

#### 3.2 Margin Loss for Digit Existence

We are using the length of the instantiation vector to represent the probability that a capsule's entity exists. We would like the top-level capsule for digit class $k$ to have a long instantiation vector if and only if that digit is present in the image. To allow for multiple digits, we use a separate margin loss $L_k$ for each digit capsule $k$:

$$L_k = T_k \max(0, m^+ - \|v_k\|)^2 + \lambda (1 - T_k) \max(0, \|v_k\| - m^-)^2$$

where $T_k = 1$ if a digit of class $k$ is present and $m^+ = 0.9$ and $m^- = 0.1$. The $\lambda$ down-weighting of the loss for absent digit classes stops the initial learning from shrinking the lengths of the activity vectors of all the digit capsules. We use $\lambda = 0.5$. The total loss is simply the sum of the losses of all digit capsules.

This loss function has two terms:
1. The first term penalizes the model if a digit is present ($T_k = 1$) but the capsule length is less than $m^+ = 0.9$
2. The second term (down-weighted by $\lambda$) penalizes the model if a digit is absent ($T_k = 0$) but the capsule length is greater than $m^- = 0.1$

---

### النسخة العربية

#### 3.1 خوارزمية التوجيه

خوارزمية التوجيه الديناميكي هي جوهر شبكات الكبسولات. يتم عرض الإجراء في الخوارزمية 1 أدناه:

**الخوارزمية 1: خوارزمية التوجيه**

**الإجراء:** ROUTING($\hat{u}_{j|i}$, $r$, $l$)

1. **لكل** كبسولة $i$ في الطبقة $l$ وكبسولة $j$ في الطبقة $(l+1)$: $b_{ij} \leftarrow 0$
2. **لـ** $r$ تكرارات **قم بـ**:
3. &nbsp;&nbsp;&nbsp;&nbsp;**لكل** كبسولة $i$ في الطبقة $l$: $\mathbf{c}_i \leftarrow \text{softmax}(\mathbf{b}_i)$
4. &nbsp;&nbsp;&nbsp;&nbsp;**لكل** كبسولة $j$ في الطبقة $(l+1)$: $s_j \leftarrow \sum_i c_{ij} \hat{u}_{j|i}$
5. &nbsp;&nbsp;&nbsp;&nbsp;**لكل** كبسولة $j$ في الطبقة $(l+1)$: $v_j \leftarrow \text{squash}(s_j)$
6. &nbsp;&nbsp;&nbsp;&nbsp;**لكل** كبسولة $i$ في الطبقة $l$ وكبسولة $j$ في الطبقة $(l+1)$: $b_{ij} \leftarrow b_{ij} + \hat{u}_{j|i} \cdot v_j$

**إرجاع** $v_j$

حيث:
- $\hat{u}_{j|i}$ هي متجهات التنبؤ من الكبسولات في الطبقة $l$ إلى الطبقة $l+1$
- $r$ هو عدد تكرارات التوجيه (عادة 3)
- $l$ هو مؤشر الطبقة
- $b_{ij}$ هي الاحتمالات السابقة اللوغاريتمية (لوجيتات الاقتران)
- $c_{ij}$ هي معاملات الاقتران
- $s_j$ هو مجموع المدخلات للكبسولة $j$
- $v_j$ هو متجه المخرجات للكبسولة $j$

يبدأ إجراء التوجيه بتهيئة جميع لوجيتات الاقتران $b_{ij}$ إلى الصفر، مما يعني أن جميع معاملات الاقتران متساوية. في كل تكرار، تحسب الخوارزمية معاملات الاقتران عبر softmax، وتحسب المجاميع المرجحة لمتجهات التنبؤ، وتطبق دالة الضغط، ثم تحدث لوجيتات الاقتران بناءً على الاتفاق (حاصل الضرب القياسي) بين التنبؤات والمخرجات.

#### 3.2 دالة خسارة الهامش لوجود الرقم

نستخدم طول متجه التجسيد لتمثيل احتمالية وجود كيان الكبسولة. نود أن تحتوي الكبسولة ذات المستوى الأعلى لفئة الرقم $k$ على متجه تجسيد طويل إذا وفقط إذا كان هذا الرقم موجوداً في الصورة. للسماح بأرقام متعددة، نستخدم دالة خسارة هامش منفصلة $L_k$ لكل كبسولة رقم $k$:

$$L_k = T_k \max(0, m^+ - \|v_k\|)^2 + \lambda (1 - T_k) \max(0, \|v_k\| - m^-)^2$$

حيث $T_k = 1$ إذا كان رقم من الفئة $k$ موجوداً و $m^+ = 0.9$ و $m^- = 0.1$. يمنع التقليل من وزن الخسارة بـ $\lambda$ للفئات الرقمية الغائبة التعلم الأولي من تقليص أطوال متجهات النشاط لجميع كبسولات الأرقام. نستخدم $\lambda = 0.5$. الخسارة الكلية هي ببساطة مجموع الخسائر لجميع كبسولات الأرقام.

تحتوي دالة الخسارة هذه على حدين:
1. الحد الأول يعاقب النموذج إذا كان الرقم موجوداً ($T_k = 1$) ولكن طول الكبسولة أقل من $m^+ = 0.9$
2. الحد الثاني (مع تقليل الوزن بـ $\lambda$) يعاقب النموذج إذا كان الرقم غائباً ($T_k = 0$) ولكن طول الكبسولة أكبر من $m^- = 0.1$

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - routing algorithm (خوارزمية التوجيه) - iterative procedure
  - coupling logits (لوجيتات الاقتران) - pre-softmax values
  - margin loss (دالة خسارة الهامش) - loss function with margins
  - down-weighting (تقليل الوزن) - reducing weight coefficient
  - instantiation vector (متجه التجسيد) - entity representation
  - digit capsule (كبسولة الرقم) - top-level capsule for digit class

- **Algorithms:** 1 complete routing algorithm with 6 steps
- **Equations:**
  1. Margin loss: $L_k = T_k \max(0, m^+ - \|v_k\|)^2 + \lambda (1 - T_k) \max(0, \|v_k\| - m^-)^2$

- **Hyperparameters:**
  - $r = 3$ (number of routing iterations)
  - $m^+ = 0.9$ (upper margin for present digits)
  - $m^- = 0.1$ (lower margin for absent digits)
  - $\lambda = 0.5$ (down-weighting factor)

- **Citations:** None
- **Special handling:**
  - Preserved algorithm pseudocode structure
  - Translated control flow keywords (for, do, return) while keeping mathematical notation
  - Maintained indentation for algorithm readability
  - Explained the two-term loss function clearly

### Quality Metrics

- Semantic equivalence: 0.91
- Technical accuracy: 0.92
- Readability: 0.88
- Glossary consistency: 0.90
- **Overall section score:** 0.90

### Semantic Analysis

The translation accurately captures:
1. The complete routing algorithm with initialization and iterative updates
2. The role of coupling coefficients and their computation via softmax
3. The agreement-based update mechanism using scalar products
4. The margin loss formulation for handling multiple digits
5. The purpose of the two loss terms (penalizing false negatives and false positives)
6. The hyperparameter choices and their rationale

The algorithm pseudocode maintains its structure while adapting control flow keywords to Arabic, and all mathematical notation is preserved exactly.
