# Section 2: Preliminaries
## القسم 2: المفاهيم الأولية

**Section:** preliminaries
**Translation Quality:** 0.88
**Glossary Terms Used:** implicit feedback, matrix factorization, interaction, latent feature, model, function, data, regression, loss function, pointwise, pairwise

---

### English Version

#### 2.1 Learning from Implicit Data

We first formulate the problem of learning from implicit feedback. Let $M$ and $N$ denote the number of users and items, respectively. We define the user-item interaction matrix from users' implicit feedback as $\mathbf{Y} \in \mathbb{R}^{M \times N}$ from users' implicit feedback:

$$y_{ui} = \begin{cases} 1, & \text{if interaction (user } u, \text{ item } i) \text{ is observed;} \\ 0, & \text{otherwise.} \end{cases}$$

Here a value of 1 for $y_{ui}$ indicates that there is an interaction between user $u$ and item $i$; however, it does not mean $u$ actually likes $i$. Similarly, a value of 0 does not necessarily mean $u$ does not like $i$, it can be that the user is not aware of the item. This poses challenges for learning from implicit data, because it provides only noisy signals about users' preference on items. While observed entries at least reflect users' interest on items, the unobserved entries can be just missing data and there is a natural scarcity of negative feedback.

The recommendation problem with implicit feedback is formulated as the problem of estimating the scores of unobserved entries in $\mathbf{Y}$, which are used for ranking the items. Model-based approaches assume that data can be generated (or described) by an underlying model. Formally, they can be abstracted as learning $\hat{y}_{ui} = f(u, i|\Theta)$, where $\hat{y}_{ui}$ denotes the predicted score of interaction $y_{ui}$, $\Theta$ denotes model parameters, and $f$ denotes the function that maps model parameters to the predicted score (which we term as an interaction function).

To estimate parameters $\Theta$, existing approaches generally follow the machine learning paradigm that optimizes an objective function. Two types of objective functions are most commonly used – pointwise loss and pairwise loss. As natural extensions of MF, the representative methods of pointwise learning factorize the $\mathbf{Y}$ matrix under a regression framework by minimizing the squared loss between $\hat{y}_{ui}$ and its target value $y_{ui}$. To address the lack of negative data, they either treat all unobserved entries as negative feedback or sample negative instances from unobserved entries. For pairwise learning, the idea is that observed entries should be ranked higher than the unobserved ones. As such, instead of minimizing the loss between $\hat{y}_{ui}$ and $y_{ui}$, pairwise learning maximizes the margin between observed entry $\hat{y}_{ui}$ and unobserved entry $\hat{y}_{uj}$.

As our NCF framework is capable of supporting both learning approaches, we opt to leverage the pointwise learning method in this work for brevity.

#### 2.2 Matrix Factorization

Matrix Factorization associates each user and each item with a real-valued vector of latent features. Let $\mathbf{p}_u$ and $\mathbf{q}_i$ denote the latent vector for user $u$ and item $i$, respectively; MF estimates an interaction $y_{ui}$ as the inner product of $\mathbf{p}_u$ and $\mathbf{q}_i$:

$$\hat{y}_{ui} = f(u, i|\mathbf{p}_u, \mathbf{q}_i) = \mathbf{p}_u^T \mathbf{q}_i = \sum_{k=1}^{K} p_{uk} q_{ik}$$

where $K$ denotes the dimension of the latent space.

As can be seen, MF models the two-way interaction of user and item latent factors, assuming each dimension of the latent space is independent of each other and linearly combining them with the same weight. As such, MF can be seen as a linear model of latent factors.

---

### النسخة العربية

#### 2.1 التعلم من البيانات الضمنية

نقوم أولاً بصياغة مشكلة التعلم من التغذية الراجعة الضمنية. لنفترض أن $M$ و $N$ يمثلان عدد المستخدمين والعناصر، على التوالي. نحدد مصفوفة تفاعل المستخدم والعنصر من التغذية الراجعة الضمنية للمستخدمين على أنها $\mathbf{Y} \in \mathbb{R}^{M \times N}$:

$$y_{ui} = \begin{cases} 1, & \text{إذا لوحظ التفاعل (المستخدم } u, \text{ العنصر } i); \\ 0, & \text{خلاف ذلك.} \end{cases}$$

هنا القيمة 1 لـ $y_{ui}$ تشير إلى أن هناك تفاعلاً بين المستخدم $u$ والعنصر $i$؛ ومع ذلك، فإن هذا لا يعني أن $u$ يحب $i$ فعلياً. وبالمثل، فإن القيمة 0 لا تعني بالضرورة أن $u$ لا يحب $i$، بل يمكن أن يكون المستخدم غير مدرك للعنصر. هذا يطرح تحديات للتعلم من البيانات الضمنية، لأنها توفر فقط إشارات صاخبة حول تفضيلات المستخدمين للعناصر. في حين أن الإدخالات الملاحظة على الأقل تعكس اهتمام المستخدمين بالعناصر، فإن الإدخالات غير الملاحظة يمكن أن تكون مجرد بيانات مفقودة وهناك ندرة طبيعية في التغذية الراجعة السلبية.

تتم صياغة مشكلة التوصية مع التغذية الراجعة الضمنية على أنها مشكلة تقدير درجات الإدخالات غير الملاحظة في $\mathbf{Y}$، والتي تُستخدم لترتيب العناصر. تفترض النهج القائمة على النماذج أن البيانات يمكن توليدها (أو وصفها) بواسطة نموذج أساسي. بشكل رسمي، يمكن تجريدها على أنها تعلم $\hat{y}_{ui} = f(u, i|\Theta)$، حيث $\hat{y}_{ui}$ يشير إلى الدرجة المتوقعة للتفاعل $y_{ui}$، و $\Theta$ يشير إلى معاملات النموذج، و $f$ تشير إلى الدالة التي تربط معاملات النموذج بالدرجة المتوقعة (والتي نسميها دالة التفاعل).

لتقدير المعاملات $\Theta$، تتبع النهج الحالية عموماً نموذج التعلم الآلي الذي يحسّن دالة هدف. يتم استخدام نوعين من دوال الهدف بشكل أكثر شيوعاً – الخسارة النقطية والخسارة الزوجية. كامتدادات طبيعية لتحليل المصفوفات، تقوم الطرق التمثيلية للتعلم النقطي بتحليل مصفوفة $\mathbf{Y}$ في إطار انحداري من خلال تقليل الخسارة التربيعية بين $\hat{y}_{ui}$ وقيمتها المستهدفة $y_{ui}$. لمعالجة نقص البيانات السلبية، إما أن تعامل جميع الإدخالات غير الملاحظة على أنها تغذية راجعة سلبية أو تقوم بأخذ عينات من حالات سلبية من الإدخالات غير الملاحظة. بالنسبة للتعلم الزوجي، فإن الفكرة هي أن الإدخالات الملاحظة يجب أن تُرتب أعلى من غير الملاحظة. على هذا النحو، بدلاً من تقليل الخسارة بين $\hat{y}_{ui}$ و $y_{ui}$، يزيد التعلم الزوجي من الهامش بين الإدخال الملاحظ $\hat{y}_{ui}$ والإدخال غير الملاحظ $\hat{y}_{uj}$.

نظراً لأن إطار عمل NCF الخاص بنا قادر على دعم كلا نهجي التعلم، فإننا نختار الاستفادة من طريقة التعلم النقطي في هذا العمل من أجل الإيجاز.

#### 2.2 تحليل المصفوفات

يربط تحليل المصفوفات كل مستخدم وكل عنصر بمتجه ذي قيمة حقيقية من الميزات الكامنة. لنفترض أن $\mathbf{p}_u$ و $\mathbf{q}_i$ يمثلان المتجه الكامن للمستخدم $u$ والعنصر $i$، على التوالي؛ يقدر تحليل المصفوفات التفاعل $y_{ui}$ على أنه حاصل الضرب الداخلي لـ $\mathbf{p}_u$ و $\mathbf{q}_i$:

$$\hat{y}_{ui} = f(u, i|\mathbf{p}_u, \mathbf{q}_i) = \mathbf{p}_u^T \mathbf{q}_i = \sum_{k=1}^{K} p_{uk} q_{ik}$$

حيث $K$ يشير إلى بُعد الفضاء الكامن.

كما يمكن ملاحظته، يقوم تحليل المصفوفات بنمذجة التفاعل الثنائي بين العوامل الكامنة للمستخدم والعنصر، مفترضاً أن كل بُعد من الفضاء الكامن مستقل عن الآخر ويجمعها بشكل خطي بنفس الوزن. على هذا النحو، يمكن اعتبار تحليل المصفوفات نموذجاً خطياً للعوامل الكامنة.

---

### Translation Notes

- **Figures referenced:** None mentioned but section likely references Figure 1 in original
- **Key terms introduced:** Interaction matrix Y, predicted score ŷ, model parameters Θ, interaction function, pointwise loss, pairwise loss, latent vectors p_u and q_i, latent space dimension K
- **Equations:** 3 main equations:
  1. Definition of y_ui (piecewise function)
  2. Model abstraction ŷ_ui = f(u, i|Θ)
  3. Matrix factorization formula
- **Citations:** Not visible in extracted text
- **Special handling:**
  - All mathematical notation preserved in LaTeX format
  - Subscripts and superscripts maintained
  - Matrix notation kept in original form
  - Technical terms like "pointwise" and "pairwise" translated as "نقطي" and "زوجي"

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.86
- Glossary consistency: 0.89
- **Overall section score:** 0.88
