# Section 4: Learning Capability
## القسم 4: قدرة التعلم

**Section:** methodology
**Translation Quality:** 0.85
**Glossary Terms Used:** ReLU, DNN, piecewise linear, manifold, embedding, complexity, autoencoder, encoder, Peano curve, rectified linear complexity, homeomorphic, cell decomposition, hyperplane, polyhedron

---

### English Version

### 4.1 Main Ideas

Fig. 7 shows another example, an Archimedean spiral curve embedded in $\mathbb{R}^2$, the curve equation is given by $\rho(\theta) = (a + b\theta)e^{iw\theta}$, $a, b, w > 0$ are constants, $\theta \in (0, T]$. For relatively small range $T$, the encoder successfully maps it onto a straight line segment, and the decoder reconstructs a piecewise linear curve with good approximation quality. When we extend the spiral curve by enlarging $T$, then at some threshold, the autoencoder with the same architecture fails to encode it.

The central problems we want to answer are as follows:

1. How to decide the bound of the encoding or representation capability for an autoencoder with a fixed ReLU DNN architecture?

2. How to describe and compute the complexity of a manifold embedded in the ambient space to be encoded?

3. How to verify whether a embedded manifold can be encoded by a ReLU DNN autoencoder?

For the first problem, our solutions are based on the geometric intuition of the piecewise linear nature of encoder/decoder maps. By examining fig. 3 and fig. 7, we can see the mapping $\varphi_\theta$ and $\psi_\theta$ induces polyhedral cell decompositions of the ambient space $\mathcal{X}$, $\mathcal{D}(\varphi_\theta)$ and $\mathcal{D}(\psi_\theta \circ \varphi_\theta)$ respectively. The number of cells offers a measurement to describing the representation capabilities of these maps, the upper bound of the number of cells $\max_\theta |\mathcal{D}(\varphi_\theta)|$ describes the limit of the encoding capability of $\varphi_\theta$. We call this upper bound as the rectified linear complexity of the autoencoder. The rectified linear complexity can be deduced from the architecture of the encoder network, as claimed in our theorem 4.5.

For the second problem, we introduce the similar concept to the embedded manifold. The encoder map $\varphi_\theta$ has a very strong geometric requirement: suppose $U_k$ is a cell in $\mathcal{D}(\varphi_\theta)$, then $\varphi_\theta : U_k \to \mathcal{F}$ is an affine map to the latent space, its restriction on $U_k \cap \Sigma$ is a homeomorphism $\varphi_\theta : U_k \cap \Sigma \to \varphi_\theta(U_k \cap \Sigma)$. In order to satisfy the two stringent requirements for the encoding map: the piecewise ambient linearity and the local homeomorphism, the number of cells of the decomposition of $\Sigma$ (and of $\mathcal{X}$) must be greater than a lower bound. Similarly, we call this lower bound the rectified linear complexity of the pair of the manifold and the ambient space $(\mathcal{X}, \Sigma)$. The rectified linear complexity can be derived from the geometry of $\Sigma$ and its embedding in $\mathcal{X}$. Our theorem 4.12 gives a criteria to verify if a manifold can be rectified by a linear map.

For the third problem, we can compare the rectified linear complexity of the manifold and the autoencoder. If the RL complexity of the autoencoder is less than that of the manifold, then the autoencoder can not encode the manifold. Specifically, we show that for any autoencoder with a fixed architecture, there exists an embedded manifold, which can not be encoded by it.

### 4.2 ReLU Deep Neuron Networks

We extend the ReLU activation function to vectors $x \in \mathbb{R}^n$ through entry-wise operation:

$$\sigma(x) = (\max\{0, x_1\}, \max\{0, x_2\}, \ldots, \max\{0, x_n\}).$$

For any $(m, n) \in \mathbb{N}$, let $\mathcal{A}_m^n$ and $\mathcal{L}_m^n$ denote the class of affine and linear transformations from $\mathbb{R}^m \to \mathbb{R}^n$, respectively.

**Definition 4.1 (ReLU DNN).** For any number of hidden layers $k \in \mathbb{N}$, input and output dimensions $w_0, w_{k+1} \in \mathbb{N}$, a $\mathbb{R}^{w_0} \to \mathbb{R}^{w_{k+1}}$ ReLU DNN is given by specifying a sequence of $k$ natural numbers $w_1, w_2, \ldots, w_k$ representing widths of the hidden layers, a set of $k$ affine transformations $T_i: \mathbb{R}^{w_{i-1}} \to \mathbb{R}^{w_i}$ for $i = 1, \ldots, k$ and a linear transformation $T_{k+1}: \mathbb{R}^{w_k} \to \mathbb{R}^{w_{k+1}}$ corresponding to weights of hidden layers. Such a ReLU DNN is called a $(k + 1)$-layer ReLU DNN, and is said to have $k$ hidden layers, denoted as $\mathcal{N}(w_0, w_1, \ldots, w_k, w_{k+1})$.

The mapping $\varphi_\theta : \mathbb{R}^{w_0} \to \mathbb{R}^{w_{k+1}}$ represented by this ReLU DNN is

$$\varphi_\theta = T_{k+1} \circ \sigma \circ T_k \circ \cdots \circ T_2 \circ \sigma \circ T_1,$$

where $\circ$ denotes mapping composition, $\theta$ represent all the weight and bias parameters. The depth of the ReLU DNN is $k + 1$, the width is $\max\{w_1, \ldots, w_k\}$, the size $w_1 + w_2 + \cdots + w_k$.

**Definition 4.2 (PL Mapping).** A mapping $\varphi : \mathbb{R}^n \to \mathbb{R}^m$ is a piecewise linear mapping if there exists a finite set of polyhedra whose union is $\mathbb{R}^n$, and $\varphi$ is affine linear over each polyhedron. The number of pieces of $\varphi$ is the number of maximal connected subsets of $\mathbb{R}^n$ over which $\varphi$ is affine linear, denoted as $\mathcal{N}(\varphi)$. We call $\mathcal{N}(\varphi)$ as the rectified linear complexity of $\varphi$.

**Definition 4.3 (Rectified Linear Complexity of a ReLU DNN).** Given a ReLU DNN $\mathcal{N}(w_0, \ldots, w_{k+1})$, its rectified linear complexity is the upper bound of the rectified linear complexities of all PL functions $\varphi_\theta$ represented by $\mathcal{N}$,

$$\mathcal{N}(\mathcal{N}) := \max_\theta \mathcal{N}(\varphi_\theta).$$

**Lemma 4.4.** The maximum number of parts one can get when cutting $d$-dimensional space $\mathbb{R}^d$ with $n$ hyperplanes is denoted as $\mathcal{C}(d, n)$, then

$$\mathcal{C}(d, n) = \binom{n}{0} + \binom{n}{1} + \binom{n}{2} + \cdots + \binom{n}{d}.$$

**Theorem 4.5 (Rectified Linear Complexity of a ReLU DNN).** Given a ReLU DNN $\mathcal{N}(w_0, \ldots, w_{k+1})$, representing PL mappings $\varphi_\theta : \mathbb{R}^{w_0} \to \mathbb{R}^{w_{k+1}}$ with $k$ hidden layers of widths $\{w_i\}_{i=1}^k$, then the linear rectified complexity of $\mathcal{N}$ has an upper bound,

$$\mathcal{N}(\mathcal{N}) \leq \Pi_{i=1}^{k+1} \mathcal{C}(w_{i-1}, w_i).$$

### 4.3 Cell Decomposition

The PL mappings induces cell decompositions of both the ambient space $\mathcal{X}$ and the latent space $\mathcal{F}$. The number of cells is closely related to the rectified linear complexity.

Fix the encoding map $\varphi_\theta$, let the set of all neurons in the network is denoted as $S$, all the subsets is denoted as $2^S$.

**Definition 4.6 (Activated Path).** Given a point $x \in \mathcal{X}$, the activated path of $x$ consists all the activated neurons when $\varphi_\theta(x)$ is evaluated, and denoted as $\rho(x)$. Then the activated path defines a set-valued function $\rho : \mathcal{X} \to 2^S$.

**Definition 4.7 (Cell Decomposition).** Fix an encoding map $\varphi_\theta$ represented by a ReLU RNN, two data points $x_1, x_2 \in \mathcal{X}$ are equivalent, denoted as $x_1 \sim x_2$, if they share the same activated path, $\rho(x_1) = \rho(x_2)$. Then each equivalence relation partitions the ambient space $\mathcal{X}$ into cells,

$$\mathcal{D}(\varphi_\theta) : \mathcal{X} = \bigcup_\alpha U_\alpha,$$

each equivalence class corresponds to a cell: $x_1, x_2 \in U_\alpha$ if and only if $x_1 \sim x_2$. $\mathcal{D}(\varphi_\theta)$ is called the cell decomposition induced by the encoding map $\varphi_\theta$.

### 4.4 Learning Difficulty

**Definition 4.8 (Linear Rectifiable Manifold).** Suppose $\Sigma$ is a $m$-dimensional manifold, embedded in $\mathbb{R}^n$, we say $\Sigma$ is linear rectifiable, if there exists an affine map $\varphi : \mathbb{R}^n \to \mathbb{R}^m$, such that the restriction of $\varphi$ on $\Sigma$, $\varphi|_\Sigma : \Sigma \to \varphi(\Sigma) \subset \mathbb{R}^m$, is homeomorphic. $\varphi$ is called the corresponding rectified linear map of $M$.

**Definition 4.9 (Linear Rectifiable Atlas).** Suppose $\Sigma$ is a $m$-dimensional manifold, embedded in $\mathbb{R}^n$, $\mathcal{A} = \{(U_\alpha, \varphi_\alpha\}$ is an atlas of $M$. If each chart $(U_\alpha, \varphi_\alpha)$ is linear rectifiable, $\varphi_\alpha : U_\alpha \to \mathbb{R}^m$ is the rectified linear map of $U_\alpha$, then the atlas is called a linear rectifiable atlas of $\Sigma$.

Given a compact manifold $\Sigma$ and its atlas $\mathcal{A}$, one can select a finite number of local charts $\tilde{\mathcal{A}} = \{(U_i, \varphi_i)\}_{i=1}^n$, $\tilde{\mathcal{A}}$ still covers $\Sigma$. The number of charts of an atlas $\mathcal{A}$ is denoted as $|\mathcal{A}|$.

**Definition 4.10 (Rectified Linear Complexity of a Manifold).** Suppose $\Sigma$ is a $m$-dimensional manifold embedded in $\mathbb{R}^n$, the rectified linear complexity of $\Sigma$ is denoted as $\mathcal{N}(\mathbb{R}^n, \Sigma)$ and defined as,

$$\mathcal{N}(\mathbb{R}^n, \Sigma) := \min \{|\mathcal{A}| ~|~ \mathcal{A} \text{ is a linear rectifiable altas of } \Sigma\}.$$

### 4.5 Learnable Condition

**Definition 4.11 (Encoding Map).** Suppose $M$ is a $m$-dimensional manifold, embedded in $\mathbb{R}^n$, a continuous mapping $\varphi : \mathbb{R}^n \to \mathbb{R}^m$ is called an encoding map of $(\mathbb{R}^n, \Sigma)$, if restricted on $\Sigma$, $\varphi|_\Sigma : \Sigma \to \varphi(\Sigma) \subset \mathbb{R}^m$ is homeomorphic.

**Theorem 4.12.** Suppose a ReLU DNN $\mathcal{N}(w_0, \ldots, w_{k+1})$ represents a PL mapping $\varphi_\theta : \mathbb{R}^n \to \mathbb{R}^m$, $\Sigma$ is a $m$-dimensional manifold embedded in $\mathbb{R}^n$. If $\varphi_\theta$ is an encoding mapping of $(\mathbb{R}^n, \Sigma)$, then the rectified linear complexity of $\mathcal{N}$ is no less that the rectified linear complexity of $(\mathbb{R}^n, \Sigma)$,

$$\mathcal{N}(\mathbb{R}^n, \Sigma) \leq \mathcal{N}(\varphi_\theta) \leq \mathcal{N}(\mathcal{N}).$$

The encoding map $\varphi_\theta : \mathcal{X} \to \mathcal{F}$ is required to be homeomorphic, this adds strong topological constraints to the manifold $\Sigma$. For example, if $\Sigma$ is a surface, $\mathcal{F}$ is $\mathbb{R}^2$, then $\Sigma$ must be a genus zero surface with boundaries. In general, assume $\varphi_\theta(\Sigma)$ is a simply connected domain in $\mathcal{F} = \mathbb{R}^m$, then $\Sigma$ must be a $m$-dimensional topological disk. The topological constraint implies that autoencoder can only learn manifolds with simple topologies, or a local chart of the whole manifold.

On the other hand, the geometry and the embedding of $\Sigma$ determines the linear rectifiability of $(\Sigma, \mathbb{R}^n)$.

**Lemma 4.13.** Suppose a $n$ dimensional manifold $\Sigma$ is embedded in $\mathbb{R}^{n+1}$,

$$M \xrightarrow{G} \mathbb{S}^n \xrightarrow{p} \mathbb{RP}^n$$

where $G : \Sigma \to \mathbb{S}^n$ is the Gauss map, $\mathbb{RP}^n$ is the real projective space, the projection $p : \mathbb{S}^n \to \mathbb{RP}^n$ maps antipodal points to the same point, if $p \circ G(\Sigma)$ covers the whole $\mathbb{RP}^n$, then $\Sigma$ is not linear rectifiable.

**Theorem 4.14.** Given any ReLU deep neural network $\mathcal{N}(w_0, w_1, \ldots, w_k, w_{k+1})$, there is a manifold $\Sigma$ embedded in $\mathbb{R}^{w_0}$, such that $\Sigma$ can not be encoded by $\mathcal{N}$.

**Proof.** First, we prove the simplest case. When $(w_0, w_{k+1}) = (2, 1)$, we can construct space filling Peano curves, as shown in Fig. 8. Suppose $C_1$ is shown in the left frame, we make 4 copies of $C_1$, by translation, rotation, reconnection and scaling to construct $C_2$, as shown in the right frame. Similarly, we can construct all $C_k$'s. The red square shows one unit, $C_1$ has 16 units, $C_n$ has $4^{n+1}$ units. Each unit is not rectifiable, therefore

$$\mathcal{N}(\mathbb{R}^2, C_n) \geq 4^{n+1}.$$

We can choose $n$ big enough, such that $4^{n+1} > \mathcal{N}(\mathcal{N})$, then $C_n$ can not be encoded by $\mathcal{N}$.

Similarly, for any $w_0$ and $w_{k+1} = 1$, we can construct Peano curves to fill $\mathbb{R}^{w_0}$, which can not be encoded by $\mathcal{N}$. The Peano curve construction can be generalized to higher dimensional manifolds by direct product with unit intervals. $\square$

---

### النسخة العربية

### 4.1 الأفكار الرئيسية

يوضح الشكل 7 مثالاً آخر، منحنى حلزوني أرخميدي مضمن في $\mathbb{R}^2$، معادلة المنحنى معطاة بـ $\rho(\theta) = (a + b\theta)e^{iw\theta}$، $a, b, w > 0$ ثوابت، $\theta \in (0, T]$. لنطاق $T$ صغير نسبياً، يرسم المشفر بنجاح على قطعة خط مستقيمة، ويعيد فك التشفير بناء منحنى خطي متعدد القطع بجودة تقريب جيدة. عندما نمد المنحنى الحلزوني عن طريق تكبير $T$، ثم عند عتبة معينة، يفشل المشفر التلقائي بنفس المعمارية في ترميزه.

المشاكل المركزية التي نريد الإجابة عليها هي كما يلي:

1. كيفية تحديد حد قدرة الترميز أو التمثيل لمشفر تلقائي بمعمارية شبكة عصبية عميقة ReLU ثابتة؟

2. كيفية وصف وحساب تعقيد متعدد مضمن في الفضاء المحيط ليتم ترميزه؟

3. كيفية التحقق مما إذا كان متعدد مضمن يمكن ترميزه بواسطة مشفر تلقائي لشبكة عصبية عميقة ReLU؟

بالنسبة للمشكلة الأولى، تستند حلولنا على الحدس الهندسي للطبيعة الخطية متعددة القطع لخرائط المشفر/فك التشفير. من خلال فحص الشكل 3 والشكل 7، يمكننا أن نرى أن الخريطة $\varphi_\theta$ و $\psi_\theta$ تستحثان تحليلات خلوية متعددة السطوح للفضاء المحيط $\mathcal{X}$، $\mathcal{D}(\varphi_\theta)$ و $\mathcal{D}(\psi_\theta \circ \varphi_\theta)$ على التوالي. عدد الخلايا يوفر قياساً لوصف قدرات التمثيل لهذه الخرائط، والحد الأعلى لعدد الخلايا $\max_\theta |\mathcal{D}(\varphi_\theta)|$ يصف حد قدرة الترميز لـ $\varphi_\theta$. نسمي هذا الحد الأعلى التعقيد الخطي المصحح للمشفر التلقائي. يمكن استنتاج التعقيد الخطي المصحح من معمارية شبكة المشفر، كما هو مدعى في نظريتنا 4.5.

بالنسبة للمشكلة الثانية، نقدم مفهوماً مشابهاً للمتعدد المضمن. خريطة المشفر $\varphi_\theta$ لديها متطلب هندسي قوي جداً: افترض أن $U_k$ خلية في $\mathcal{D}(\varphi_\theta)$، إذن $\varphi_\theta : U_k \to \mathcal{F}$ هي خريطة أفينية إلى الفضاء الكامن، وقصرها على $U_k \cap \Sigma$ هو تشاكل $\varphi_\theta : U_k \cap \Sigma \to \varphi_\theta(U_k \cap \Sigma)$. من أجل تلبية المتطلبين الصارمين لخريطة الترميز: الخطية المحيطة متعددة القطع والتشاكل المحلي، يجب أن يكون عدد خلايا تحليل $\Sigma$ (ولـ $\mathcal{X}$) أكبر من حد أدنى. وبالمثل، نسمي هذا الحد الأدنى التعقيد الخطي المصحح لزوج المتعدد والفضاء المحيط $(\mathcal{X}, \Sigma)$. يمكن اشتقاق التعقيد الخطي المصحح من هندسة $\Sigma$ وتضمينه في $\mathcal{X}$. نظريتنا 4.12 تعطي معياراً للتحقق مما إذا كان متعدد يمكن تصحيحه بواسطة خريطة خطية.

بالنسبة للمشكلة الثالثة، يمكننا مقارنة التعقيد الخطي المصحح للمتعدد والمشفر التلقائي. إذا كان تعقيد RL للمشفر التلقائي أقل من تعقيد المتعدد، فإن المشفر التلقائي لا يمكنه ترميز المتعدد. على وجه التحديد، نظهر أنه لأي مشفر تلقائي بمعمارية ثابتة، يوجد متعدد مضمن، لا يمكن ترميزه به.

### 4.2 شبكات العصبونات العميقة ReLU

نمد دالة التنشيط ReLU إلى المتجهات $x \in \mathbb{R}^n$ من خلال عملية عنصر بعنصر:

$$\sigma(x) = (\max\{0, x_1\}, \max\{0, x_2\}, \ldots, \max\{0, x_n\}).$$

لأي $(m, n) \in \mathbb{N}$، لتكن $\mathcal{A}_m^n$ و $\mathcal{L}_m^n$ تشير إلى صنف التحويلات الأفينية والخطية من $\mathbb{R}^m \to \mathbb{R}^n$، على التوالي.

**التعريف 4.1 (شبكة عصبية عميقة ReLU).** لأي عدد من الطبقات المخفية $k \in \mathbb{N}$، وأبعاد مدخلات ومخرجات $w_0, w_{k+1} \in \mathbb{N}$، شبكة عصبية عميقة ReLU من $\mathbb{R}^{w_0} \to \mathbb{R}^{w_{k+1}}$ تُعطى بتحديد تسلسل من $k$ أعداد طبيعية $w_1, w_2, \ldots, w_k$ تمثل عروض الطبقات المخفية، ومجموعة من $k$ تحويلات أفينية $T_i: \mathbb{R}^{w_{i-1}} \to \mathbb{R}^{w_i}$ لـ $i = 1, \ldots, k$ وتحويل خطي $T_{k+1}: \mathbb{R}^{w_k} \to \mathbb{R}^{w_{k+1}}$ يقابل أوزان الطبقات المخفية. تسمى هذه الشبكة العصبية العميقة ReLU شبكة عصبية عميقة ReLU من $(k + 1)$ طبقة، ويقال إن لديها $k$ طبقات مخفية، يُرمز لها بـ $\mathcal{N}(w_0, w_1, \ldots, w_k, w_{k+1})$.

الخريطة $\varphi_\theta : \mathbb{R}^{w_0} \to \mathbb{R}^{w_{k+1}}$ الممثلة بواسطة هذه الشبكة العصبية العميقة ReLU هي

$$\varphi_\theta = T_{k+1} \circ \sigma \circ T_k \circ \cdots \circ T_2 \circ \sigma \circ T_1,$$

حيث $\circ$ يشير إلى تركيب الخرائط، و$\theta$ يمثل جميع بارامترات الأوزان والتحيز. عمق الشبكة العصبية العميقة ReLU هو $k + 1$، والعرض هو $\max\{w_1, \ldots, w_k\}$، والحجم $w_1 + w_2 + \cdots + w_k$.

**التعريف 4.2 (خريطة PL).** الخريطة $\varphi : \mathbb{R}^n \to \mathbb{R}^m$ هي خريطة خطية متعددة القطع إذا كانت هناك مجموعة محدودة من متعددات السطوح التي اتحادها $\mathbb{R}^n$، و$\varphi$ أفينية خطية على كل متعدد سطوح. عدد قطع $\varphi$ هو عدد المجموعات الفرعية المتصلة القصوى لـ $\mathbb{R}^n$ التي عليها $\varphi$ أفينية خطية، يُرمز لها بـ $\mathcal{N}(\varphi)$. نسمي $\mathcal{N}(\varphi)$ التعقيد الخطي المصحح لـ $\varphi$.

**التعريف 4.3 (التعقيد الخطي المصحح لشبكة عصبية عميقة ReLU).** لشبكة عصبية عميقة ReLU معطاة $\mathcal{N}(w_0, \ldots, w_{k+1})$، تعقيدها الخطي المصحح هو الحد الأعلى للتعقيدات الخطية المصححة لجميع الدوال PL $\varphi_\theta$ الممثلة بواسطة $\mathcal{N}$،

$$\mathcal{N}(\mathcal{N}) := \max_\theta \mathcal{N}(\varphi_\theta).$$

**المبرهنة 4.4.** الحد الأقصى لعدد الأجزاء التي يمكن الحصول عليها عند قطع فضاء بُعد $d$ $\mathbb{R}^d$ بـ $n$ مستويات فائقة يُرمز له بـ $\mathcal{C}(d, n)$، إذن

$$\mathcal{C}(d, n) = \binom{n}{0} + \binom{n}{1} + \binom{n}{2} + \cdots + \binom{n}{d}.$$

**النظرية 4.5 (التعقيد الخطي المصحح لشبكة عصبية عميقة ReLU).** لشبكة عصبية عميقة ReLU معطاة $\mathcal{N}(w_0, \ldots, w_{k+1})$، تمثل خرائط PL $\varphi_\theta : \mathbb{R}^{w_0} \to \mathbb{R}^{w_{k+1}}$ مع $k$ طبقات مخفية بعروض $\{w_i\}_{i=1}^k$، إذن التعقيد الخطي المصحح لـ $\mathcal{N}$ له حد أعلى،

$$\mathcal{N}(\mathcal{N}) \leq \Pi_{i=1}^{k+1} \mathcal{C}(w_{i-1}, w_i).$$

### 4.3 التحليل الخلوي

الخرائط PL تستحث تحليلات خلوية لكل من الفضاء المحيط $\mathcal{X}$ والفضاء الكامن $\mathcal{F}$. عدد الخلايا مرتبط بشكل وثيق بالتعقيد الخطي المصحح.

اختر خريطة الترميز $\varphi_\theta$، ولتكن مجموعة جميع العصبونات في الشبكة يُرمز لها بـ $S$، وجميع المجموعات الفرعية يُرمز لها بـ $2^S$.

**التعريف 4.6 (المسار المنشط).** لنقطة معطاة $x \in \mathcal{X}$، المسار المنشط لـ $x$ يتكون من جميع العصبونات المنشطة عندما يتم تقييم $\varphi_\theta(x)$، ويُرمز له بـ $\rho(x)$. ثم يحدد المسار المنشط دالة قيمة مجموعة $\rho : \mathcal{X} \to 2^S$.

**التعريف 4.7 (التحليل الخلوي).** اختر خريطة ترميز $\varphi_\theta$ ممثلة بواسطة RNN ReLU، نقطتا بيانات $x_1, x_2 \in \mathcal{X}$ متكافئتان، يُرمز بـ $x_1 \sim x_2$، إذا كانتا تشتركان في نفس المسار المنشط، $\rho(x_1) = \rho(x_2)$. ثم تقسم كل علاقة تكافؤ الفضاء المحيط $\mathcal{X}$ إلى خلايا،

$$\mathcal{D}(\varphi_\theta) : \mathcal{X} = \bigcup_\alpha U_\alpha,$$

كل صنف تكافؤ يقابل خلية: $x_1, x_2 \in U_\alpha$ إذا وفقط إذا $x_1 \sim x_2$. $\mathcal{D}(\varphi_\theta)$ يسمى التحليل الخلوي المستحث بواسطة خريطة الترميز $\varphi_\theta$.

### 4.4 صعوبة التعلم

**التعريف 4.8 (متعدد قابل للتصحيح الخطي).** افترض أن $\Sigma$ متعدد بُعد $m$، مضمن في $\mathbb{R}^n$، نقول إن $\Sigma$ قابل للتصحيح الخطي، إذا كانت هناك خريطة أفينية $\varphi : \mathbb{R}^n \to \mathbb{R}^m$، بحيث أن قصر $\varphi$ على $\Sigma$، $\varphi|_\Sigma : \Sigma \to \varphi(\Sigma) \subset \mathbb{R}^m$، متشاكل. $\varphi$ تسمى الخريطة الخطية المصححة المقابلة لـ $M$.

**التعريف 4.9 (أطلس قابل للتصحيح الخطي).** افترض أن $\Sigma$ متعدد بُعد $m$، مضمن في $\mathbb{R}^n$، $\mathcal{A} = \{(U_\alpha, \varphi_\alpha\}$ أطلس لـ $M$. إذا كانت كل خريطة $(U_\alpha, \varphi_\alpha)$ قابلة للتصحيح الخطي، $\varphi_\alpha : U_\alpha \to \mathbb{R}^m$ هي الخريطة الخطية المصححة لـ $U_\alpha$، فإن الأطلس يسمى أطلساً قابلاً للتصحيح الخطي لـ $\Sigma$.

لمتعدد مضغوط معطى $\Sigma$ وأطلسه $\mathcal{A}$، يمكن اختيار عدد محدود من الخرائط المحلية $\tilde{\mathcal{A}} = \{(U_i, \varphi_i)\}_{i=1}^n$، $\tilde{\mathcal{A}}$ لا يزال يغطي $\Sigma$. عدد خرائط الأطلس $\mathcal{A}$ يُرمز له بـ $|\mathcal{A}|$.

**التعريف 4.10 (التعقيد الخطي المصحح لمتعدد).** افترض أن $\Sigma$ متعدد بُعد $m$ مضمن في $\mathbb{R}^n$، التعقيد الخطي المصحح لـ $\Sigma$ يُرمز له بـ $\mathcal{N}(\mathbb{R}^n, \Sigma)$ ويُعرّف كـ،

$$\mathcal{N}(\mathbb{R}^n, \Sigma) := \min \{|\mathcal{A}| ~|~ \mathcal{A} \text{ أطلس قابل للتصحيح الخطي لـ } \Sigma\}.$$

### 4.5 شرط القابلية للتعلم

**التعريف 4.11 (خريطة الترميز).** افترض أن $M$ متعدد بُعد $m$، مضمن في $\mathbb{R}^n$، خريطة متصلة $\varphi : \mathbb{R}^n \to \mathbb{R}^m$ تسمى خريطة ترميز لـ $(\mathbb{R}^n, \Sigma)$، إذا كانت مقصورة على $\Sigma$، $\varphi|_\Sigma : \Sigma \to \varphi(\Sigma) \subset \mathbb{R}^m$ متشاكلة.

**النظرية 4.12.** افترض أن شبكة عصبية عميقة ReLU $\mathcal{N}(w_0, \ldots, w_{k+1})$ تمثل خريطة PL $\varphi_\theta : \mathbb{R}^n \to \mathbb{R}^m$، $\Sigma$ متعدد بُعد $m$ مضمن في $\mathbb{R}^n$. إذا كانت $\varphi_\theta$ خريطة ترميز لـ $(\mathbb{R}^n, \Sigma)$، فإن التعقيد الخطي المصحح لـ $\mathcal{N}$ ليس أقل من التعقيد الخطي المصحح لـ $(\mathbb{R}^n, \Sigma)$،

$$\mathcal{N}(\mathbb{R}^n, \Sigma) \leq \mathcal{N}(\varphi_\theta) \leq \mathcal{N}(\mathcal{N}).$$

خريطة الترميز $\varphi_\theta : \mathcal{X} \to \mathcal{F}$ مطلوب أن تكون متشاكلة، وهذا يضيف قيوداً طوبولوجية قوية على المتعدد $\Sigma$. على سبيل المثال، إذا كان $\Sigma$ سطحاً، و$\mathcal{F}$ هو $\mathbb{R}^2$، فإن $\Sigma$ يجب أن يكون سطحاً من جنس صفر مع حدود. بشكل عام، افترض أن $\varphi_\theta(\Sigma)$ مجال متصل بسيط في $\mathcal{F} = \mathbb{R}^m$، ثم $\Sigma$ يجب أن يكون قرصاً طوبولوجياً بُعد $m$. القيد الطوبولوجي يعني أن المشفر التلقائي يمكنه فقط تعلم متعددات ذات طوبولوجيات بسيطة، أو خريطة محلية للمتعدد الكامل.

من ناحية أخرى، الهندسة والتضمين لـ $\Sigma$ يحددان القابلية للتصحيح الخطي لـ $(\Sigma, \mathbb{R}^n)$.

**المبرهنة 4.13.** افترض أن متعدداً بُعد $n$ $\Sigma$ مضمن في $\mathbb{R}^{n+1}$،

$$M \xrightarrow{G} \mathbb{S}^n \xrightarrow{p} \mathbb{RP}^n$$

حيث $G : \Sigma \to \mathbb{S}^n$ هي خريطة غاوس، $\mathbb{RP}^n$ هو الفضاء الإسقاطي الحقيقي، الإسقاط $p : \mathbb{S}^n \to \mathbb{RP}^n$ يرسم النقاط المتضادة إلى نفس النقطة، إذا كان $p \circ G(\Sigma)$ يغطي $\mathbb{RP}^n$ بالكامل، فإن $\Sigma$ ليس قابلاً للتصحيح الخطي.

**النظرية 4.14.** لأي شبكة عصبية عميقة ReLU معطاة $\mathcal{N}(w_0, w_1, \ldots, w_k, w_{k+1})$، يوجد متعدد $\Sigma$ مضمن في $\mathbb{R}^{w_0}$، بحيث لا يمكن ترميز $\Sigma$ بواسطة $\mathcal{N}$.

**البرهان.** أولاً، نثبت الحالة الأبسط. عندما $(w_0, w_{k+1}) = (2, 1)$، يمكننا بناء منحنيات بيانو المالئة للفضاء، كما هو موضح في الشكل 8. افترض أن $C_1$ موضح في الإطار الأيسر، نصنع 4 نسخ من $C_1$، عن طريق الترجمة، والدوران، وإعادة الاتصال والتحجيم لبناء $C_2$، كما هو موضح في الإطار الأيمن. وبالمثل، يمكننا بناء جميع $C_k$. المربع الأحمر يوضح وحدة واحدة، $C_1$ لديه 16 وحدة، $C_n$ لديه $4^{n+1}$ وحدة. كل وحدة ليست قابلة للتصحيح، لذلك

$$\mathcal{N}(\mathbb{R}^2, C_n) \geq 4^{n+1}.$$

يمكننا اختيار $n$ كبيراً بما فيه الكفاية، بحيث $4^{n+1} > \mathcal{N}(\mathcal{N})$، ثم لا يمكن ترميز $C_n$ بواسطة $\mathcal{N}$.

وبالمثل، لأي $w_0$ و $w_{k+1} = 1$، يمكننا بناء منحنيات بيانو لملء $\mathbb{R}^{w_0}$، والتي لا يمكن ترميزها بواسطة $\mathcal{N}$. يمكن تعميم بناء منحنى بيانو إلى متعددات ذات أبعاد أعلى عن طريق الضرب المباشر مع فترات الوحدة. $\square$

---

### Translation Notes

- **Figures referenced:** Figure 7, Figure 8
- **Key terms introduced:**
  - Archimedean spiral → حلزوني أرخميدي
  - activated path → المسار المنشط
  - linear rectifiable → قابل للتصحيح الخطي
  - Gauss map → خريطة غاوس
  - projective space → الفضاء الإسقاطي
  - Peano curve → منحنى بيانو
  - space filling curve → منحنى مالئ للفضاء

- **Equations:** Extensive LaTeX throughout
- **Theorems/Lemmas:** All mathematical statements preserved
- **Proofs:** Proof structure maintained

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.85
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.85
