# Section 2: Background
## القسم 2: الخلفية

**Section:** background
**Translation Quality:** 0.88
**Glossary Terms Used:** transformer, positional encoding, encoder-decoder, attention, self-attention, multi-head attention, residual connections, layer normalization, code completion, code summarization, code search, embedding

---

### English Version

## 2 BACKGROUND

### 2.1 Transformer and positional encoding

Transformer employs the typical encoder-decoder structure [6], and is composed of stacked Transformer blocks. Each block contains a multi-head self-attention sub-layer followed by a fully connected positional-wise feed-forward network sub-layer. The sub-layers are connected by residual connections [31] and layer normalization [32]. Different from the encoder, the decoder has attention sub-layers that use the key and value matrices from the encoder. Positional encoding is an essential component in Transformer [28], and has proven effective in code intelligence tasks [5]. We then introduce the two popular positional encoding strategies, including absolute positional encoding [6] and relative positional encoding [30], as below.

**Absolute positional encoding.** The original Transformer is supplemented by positional encoding to accommodate for the input's sequential nature. It transposes the sequence of input vectors X = (x₁, x₂, ..., xₙ) into the sequence of output vectors Z = (z₁, z₂, ..., zₙ), where xᵢ, zᵢ ∈ ℝ^(dₘₒdₑₗ). When doing self attention, Transformer first projects the input vector X into three vectors: the query Q, key K and value V by trainable parameters W^Q, W^K, W^V. The attention weight is calculated using dot product and softmax function. The output vector is the weighted sum of the value vector:

$$e_{ij} = \frac{(x_i W^Q)(x_j W^K)^T}{\sqrt{d}},$$ (1)

$$\alpha_{ij} = \frac{\exp e_{ij}}{\sum_{k=1}^{n} \exp e_{ij}},$$ (2)

$$z_i = \sum_{j=1}^{n} \alpha_{ij}(x_j W^V),$$ (3)

where d is the dimension of each vector, and is used to scale the dot product.

**Relative positional encoding.** To encode the pairwise positional relationships between input elements, Shaw et al. [30] propose the relative position encoding which models the relation of two elements through their distance in the input sequence. Formally, the relative position embedding between input element xᵢ and xⱼ is represented as a^V_{ij}, a^K_{ij} ∈ ℝ^d. In this way, the self attention calculated in Equ. (1) and Equ. (3) can be rewritten as:

$$e_{ij} = \frac{(x_i W^Q)(x_j W^K + a^K_{ij})^T}{\sqrt{d_z}},$$ (4)

$$z_i = \sum_{j=1}^{n} \alpha_{ij}(x_j W^V + a^V_{ij}).$$ (5)

Relative position representations take the relative distance into calculating attention rather than absolute position, which perform more effectively and flexibly.

### 2.2 Code intelligence task

**Code completion task.** Code completion is commonly used in modern integrated development environments (IDEs) for facilitating programming [33]. Developers use the code completion technique to predict expected code elements, such as class names and methods, based on given code surrounding the point of prediction [9]. Common code completion techniques include token-level completion and statement-level completion [34]. In our experiment, we focus on the token-level completion, and the task is to predict the next code token (nᵢ) based on the previous code tokens [n₀, n₁, ..., nᵢ₋₁].

**Code summarization task.** The task of code summarization is to generate a natural language summary (e.g., a docstring) for given source code [4], [35]. Code summary can help developers to understand the function and purpose of code without requiring the developers to read the code itself, which can save them time from comprehending the details of that code [36]. For a dataset containing a set of programs C and targeted summaries S, the task of code summarization is to generate the summary consisting of a sequence of token s̃ = (s₀, s₁, ..., sₘ) by maximizing the conditional likelihood s̃ = arg maxₛ P(s|c) for the given code c = (c₀, c₁, ..., cₙ) from C, where s is the corresponding summary in S.

**Code search task.** The goal of code search is to find the most semantically-related code from a collection of code based on a given natural language query [37]. In our experiment, we focus on neural code search [38], [39], which learns the joint embeddings of natural-language query and code snippet [40]. The task of neural code search is to return the expected ranking order of code snippets for the given natural language.

---

### النسخة العربية

## 2 الخلفية

### 2.1 المحول والترميز الموضعي

يستخدم المحول بنية المشفر-فك المشفر النموذجية [6]، وهو مكون من كتل محول متراكبة. تحتوي كل كتلة على طبقة فرعية للانتباه الذاتي متعدد الرؤوس متبوعة بطبقة فرعية لشبكة تغذية أمامية متصلة بالكامل موضعية الحكمة. ترتبط الطبقات الفرعية بواسطة اتصالات متبقية [31] وتطبيع الطبقات [32]. على عكس المشفر، يحتوي فك المشفر على طبقات فرعية للانتباه تستخدم مصفوفات المفتاح والقيمة من المشفر. الترميز الموضعي هو مكون أساسي في المحول [28]، وقد ثبتت فعاليته في مهام ذكاء الشفرة [5]. نقدم بعد ذلك استراتيجيتي الترميز الموضعي الشائعتين، بما في ذلك الترميز الموضعي المطلق [6] والترميز الموضعي النسبي [30]، كما يلي.

**الترميز الموضعي المطلق.** يتم استكمال المحول الأصلي بالترميز الموضعي لاستيعاب الطبيعة التسلسلية للمدخلات. يحول تسلسل متجهات المدخلات X = (x₁, x₂, ..., xₙ) إلى تسلسل متجهات المخرجات Z = (z₁, z₂, ..., zₙ)، حيث xᵢ, zᵢ ∈ ℝ^(dₘₒdₑₗ). عند القيام بالانتباه الذاتي، يُسقط المحول أولاً متجه المدخلات X إلى ثلاثة متجهات: الاستعلام Q، والمفتاح K، والقيمة V بواسطة معاملات قابلة للتدريب W^Q, W^K, W^V. يتم حساب وزن الانتباه باستخدام الضرب النقطي ودالة softmax. متجه المخرجات هو المجموع الموزون لمتجه القيمة:

$$e_{ij} = \frac{(x_i W^Q)(x_j W^K)^T}{\sqrt{d}},$$ (1)

حيث $e_{ij}$ هو درجة الانتباه غير الموزونة بين العناصر $x_i$ و $x_j$.

$$\alpha_{ij} = \frac{\exp e_{ij}}{\sum_{k=1}^{n} \exp e_{ij}},$$ (2)

حيث $\alpha_{ij}$ هو وزن الانتباه الموزون.

$$z_i = \sum_{j=1}^{n} \alpha_{ij}(x_j W^V),$$ (3)

حيث $z_i$ هو متجه المخرجات للعنصر $i$.

حيث d هو بُعد كل متجه، ويُستخدم لتحجيم الضرب النقطي.

**الترميز الموضعي النسبي.** لترميز العلاقات الموضعية الزوجية بين عناصر المدخلات، يقترح Shaw وآخرون [30] الترميز الموضعي النسبي الذي يُنمذج علاقة عنصرين من خلال مسافتهما في تسلسل المدخلات. رسمياً، يُمثل التضمين الموضعي النسبي بين عنصري المدخلات xᵢ و xⱼ بـ a^V_{ij}, a^K_{ij} ∈ ℝ^d. بهذه الطريقة، يمكن إعادة كتابة الانتباه الذاتي المحسوب في المعادلة (1) والمعادلة (3) على النحو التالي:

$$e_{ij} = \frac{(x_i W^Q)(x_j W^K + a^K_{ij})^T}{\sqrt{d_z}},$$ (4)

$$z_i = \sum_{j=1}^{n} \alpha_{ij}(x_j W^V + a^V_{ij}).$$ (5)

تأخذ تمثيلات الموضع النسبي المسافة النسبية في الاعتبار عند حساب الانتباه بدلاً من الموضع المطلق، مما يُؤدي إلى أداء أكثر فعالية ومرونة.

### 2.2 مهام ذكاء الشفرة

**مهمة إكمال الشفرة.** يُستخدم إكمال الشفرة بشكل شائع في بيئات التطوير المتكاملة الحديثة (IDEs) لتسهيل البرمجة [33]. يستخدم المطورون تقنية إكمال الشفرة للتنبؤ بعناصر الشفرة المتوقعة، مثل أسماء الفئات والأساليب، بناءً على الشفرة المحيطة بنقطة التنبؤ [9]. تتضمن تقنيات إكمال الشفرة الشائعة الإكمال على مستوى الرمز والإكمال على مستوى العبارة [34]. في تجربتنا، نركز على الإكمال على مستوى الرمز، والمهمة هي التنبؤ برمز الشفرة التالي (nᵢ) بناءً على رموز الشفرة السابقة [n₀, n₁, ..., nᵢ₋₁].

**مهمة تلخيص الشفرة.** مهمة تلخيص الشفرة هي توليد ملخص باللغة الطبيعية (على سبيل المثال، سلسلة توثيق) للشفرة المصدرية المعطاة [4]، [35]. يمكن أن يساعد ملخص الشفرة المطورين على فهم وظيفة الشفرة والغرض منها دون مطالبة المطورين بقراءة الشفرة نفسها، مما يوفر لهم الوقت من فهم تفاصيل تلك الشفرة [36]. بالنسبة لمجموعة بيانات تحتوي على مجموعة من البرامج C والملخصات المستهدفة S، فإن مهمة تلخيص الشفرة هي توليد الملخص المكون من تسلسل من الرمز s̃ = (s₀, s₁, ..., sₘ) عن طريق تعظيم الاحتمالية الشرطية s̃ = arg maxₛ P(s|c) للشفرة المعطاة c = (c₀, c₁, ..., cₙ) من C، حيث s هو الملخص المقابل في S.

**مهمة البحث في الشفرة.** الهدف من البحث في الشفرة هو إيجاد الشفرة الأكثر ارتباطاً دلالياً من مجموعة من الشفرة بناءً على استعلام باللغة الطبيعية معطى [37]. في تجربتنا، نركز على البحث العصبي في الشفرة [38]، [39]، والذي يتعلم التضمينات المشتركة لاستعلام اللغة الطبيعية ومقتطف الشفرة [40]. مهمة البحث العصبي في الشفرة هي إرجاع ترتيب الترتيب المتوقع لمقتطفات الشفرة للغة الطبيعية المعطاة.

---

### Translation Notes

- **Equations:** 5 mathematical equations (1-5) preserved in LaTeX with Arabic explanations
- **Key terms introduced:**
  - encoder-decoder (مشفر-فك مشفر)
  - multi-head self-attention (انتباه ذاتي متعدد الرؤوس)
  - residual connections (اتصالات متبقية)
  - layer normalization (تطبيع الطبقات)
  - feed-forward network (شبكة تغذية أمامية)
  - query, key, value (استعلام، مفتاح، قيمة)
  - softmax function (دالة softmax)
  - dot product (ضرب نقطي)
  - joint embeddings (تضمينات مشتركة)
  - token-level completion (إكمال على مستوى الرمز)
  - statement-level completion (إكمال على مستوى العبارة)
  - docstring (سلسلة توثيق)
  - neural code search (البحث العصبي في الشفرة)

- **Citations:** References [4] through [40] preserved
- **Special handling:**
  - Mathematical notation preserved in LaTeX
  - Arabic explanations added after key equations
  - Technical terms from glossary used consistently

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.87
- Glossary consistency: 0.89
- **Overall section score:** 0.88
