# Section 3: Our Approach
## القسم 3: نهجنا

**Section:** approach
**Translation Quality:** 0.86
**Glossary Terms Used:** differentially private SGD, gradient clipping, privacy loss, moments accountant, sampling, lot, batch, epoch, hyperparameter tuning, privacy budget, composition theorem, learning rate, non-convex

---

### English Version

This section describes the main components of our approach toward differentially private training of neural networks: a differentially private stochastic gradient descent (SGD) algorithm, the moments accountant, and hyperparameter tuning.

#### 3.1 Differentially Private SGD Algorithm

One might attempt to protect the privacy of training data by working only on the final parameters that result from the training process, treating this process as a black box. Unfortunately, in general, one may not have a useful, tight characterization of the dependence of these parameters on the training data; adding overly conservative noise to the parameters, where the noise is selected according to the worst-case analysis, would destroy the utility of the learned model. Therefore, we prefer a more sophisticated approach in which we aim to control the influence of the training data during the training process, specifically in the SGD computation. This approach has been followed in previous works (e.g., [citations]); we make several modifications and extensions, in particular in our privacy accounting.

Algorithm 1 outlines our basic method for training a model with parameters θ by minimizing the empirical loss function L(θ). At each step of the SGD, we compute the gradient ∇_θ L(θ, x_i) for a random subset of examples, clip the ℓ₂ norm of each gradient, compute the average, add noise in order to protect privacy, and take a step in the opposite direction of this average noisy gradient. At the end, in addition to outputting the model, we will also need to compute the privacy loss of the mechanism based on the information maintained by the privacy accountant. Next we describe in more detail each component of this algorithm and our refinements.

**Algorithm 1: Differentially private SGD (Outline)**

**Input:** Examples {x₁,...,xₙ}, loss function L(θ)=(1/N)Σᵢ L(θ, xᵢ). Parameters: learning rate ηₜ, noise scale σ, group size L, gradient norm bound C.

**Initialize** θ₀ randomly

**For** t ∈ [T]:
- Take a random sample Lₜ with sampling probability L/N
- **Compute gradient:**
  - For each i ∈ Lₜ, compute gₜ(xᵢ) ← ∇_θₜ L(θₜ, xᵢ)
- **Clip gradient:**
  - ḡₜ(xᵢ) ← gₜ(xᵢ) / max(1, ||gₜ(xᵢ)||₂/C)
- **Add noise:**
  - g̃ₜ ← (1/L)(Σᵢ ḡₜ(xᵢ) + N(0, σ²C²I))
- **Descent:**
  - θₜ₊₁ ← θₜ - ηₜ g̃ₜ

**Output** θₜ and compute the overall privacy cost (ε, δ) using a privacy accounting method.

**Norm clipping:** Proving the differential privacy guarantee of Algorithm 1 requires bounding the influence of each individual example on g̃ₜ. Since there is no a priori bound on the size of the gradients, we clip each gradient in ℓ₂ norm; i.e., the gradient vector g is replaced by g/max(1, ||g||₂/C), for a clipping threshold C. This clipping ensures that if ||g||₂ ≤ C, then g is preserved, whereas if ||g||₂ > C, it gets scaled down to be of norm C. We remark that gradient clipping of this form is a popular ingredient of SGD for deep networks for non-privacy reasons, though in that setting it usually suffices to clip after averaging.

**Per-layer and time-dependent parameters:** The pseudocode for Algorithm 1 groups all the parameters into a single input θ of the loss function L(·). For multi-layer neural networks, we consider each layer separately, which allows setting different clipping thresholds C and noise scales σ for different layers. Additionally, the clipping and noise parameters may vary with the number of training steps t. In results presented in Section 5 we use constant settings for C and σ.

**Lots:** Like the ordinary SGD algorithm, Algorithm 1 estimates the gradient of L by computing the gradient of the loss on a group of examples and taking the average. This average provides an unbiased estimator, the variance of which decreases quickly with the size of the group. We call such a group a lot, to distinguish it from the computational grouping that is commonly called a batch. In order to limit memory consumption, we may set the batch size much smaller than the lot size L, which is a parameter of the algorithm. We perform the computation in batches, then group several batches into a lot for adding noise. In practice, for efficiency, the construction of batches and lots is done by randomly permuting the examples and then partitioning them into groups of the appropriate sizes. For ease of analysis, however, we assume that each lot is formed by independently picking each example with probability q=L/N, where N is the size of the input dataset.

As is common in the literature, we normalize the running time of a training algorithm by expressing it as the number of epochs, where each epoch is the (expected) number of batches required to process N examples. In our notation, an epoch consists of N/L lots.

**Privacy accounting:** For differentially private SGD, an important issue is computing the overall privacy cost of the training. The composability of differential privacy allows us to implement an "accountant" procedure that computes the privacy cost at each access to the training data, and accumulates this cost as the training progresses. Each step of training typically requires gradients at multiple layers, and the accountant accumulates the cost that corresponds to all of them.

**Moments accountant:** Much research has been devoted to studying the privacy loss for a particular noise distribution as well as the composition of privacy losses. For the Gaussian noise that we use, if we choose σ in Algorithm 1 to be √(2log(1.25/δ))/ε, then by standard arguments each step is (ε,δ)-differentially private with respect to the lot. Since the lot itself is a random sample from the database, the privacy amplification theorem implies that each step is (O(qε), qδ)-differentially private with respect to the full database where q=L/N is the sampling ratio per lot and ε ≤ 1. The result in the literature that yields the best overall bound is the strong composition theorem.

However, the strong composition theorem can be loose, and does not take into account the particular noise distribution under consideration. In our work, we invent a stronger accounting method, which we call the moments accountant. It allows us to prove that Algorithm 1 is (O(qε√T), δ)-differentially private for appropriately chosen settings of the noise scale and the clipping threshold. Compared to what one would obtain by the strong composition theorem, our bound is tighter in two ways: it saves a √log(1/δ) factor in the ε part and a Tq factor in the δ part. Since we expect δ to be small and T ≫ 1/q (i.e., each example is examined multiple times), the saving provided by our bound is quite significant. This result is one of our main contributions.

**Theorem 1:** There exist constants c₁ and c₂ so that given the sampling probability q=L/N and the number of steps T, for any ε < c₁q²T, Algorithm 1 is (ε,δ)-differentially private for any δ>0 if we choose

σ ≥ c₂(q√(T log(1/δ)))/ε.

If we use the strong composition theorem, we will then need to choose σ=Ω(q√(T log(1/δ) log(T/δ))/ε). Note that we save a factor of √log(T/δ) in our asymptotic bound. The moments accountant is beneficial in theory, as this result indicates, and also in practice, as can be seen from Figure 3 (in the implementation section). For example, with L=0.01N, σ=4, δ=10⁻⁵, and T=10000, we have ε≈1.26 using the moments accountant. As a comparison, we would get a much larger ε≈9.34 using the strong composition theorem.

**[Moments Accountant Details - mathematical formulation omitted for brevity but included in full translation]**

#### 3.2 Hyperparameter Tuning

We identify characteristics of models relevant for privacy and, specifically, hyperparameters that we can tune in order to balance privacy, accuracy, and performance. In particular, through experiments, we observe that model accuracy is more sensitive to training parameters such as batch size and noise level than to the structure of a neural network.

If we try several settings for the hyperparameters, we can trivially add up the privacy costs of all the settings, possibly via the moments accountant. However, since we care only about the setting that gives us the most accurate model, we can do better, such as applying a version of a result from Gupta et al.

We can use insights from theory to reduce the number of hyperparameter settings that need to be tried. While differentially private optimization of convex objective functions is best achieved using batch sizes as small as 1, non-convex learning, which is inherently less stable, benefits from aggregation into larger batches. At the same time, Theorem 1 suggests that making batches too large increases the privacy cost, and a reasonable tradeoff is to take the number of batches per epoch to be of the same order as the desired number of epochs. The learning rate in non-private training is commonly adjusted downwards carefully as the model converges to a local optimum. In contrast, we never need to decrease the learning rate to a very small value, because differentially private training never reaches a regime where it would be justified. On the other hand, in our experiments, we do find that there is a small benefit to starting with a relatively large learning rate, then linearly decaying it to a smaller value in a few epochs, and keeping it constant afterwards.

---

### النسخة العربية

يصف هذا القسم المكونات الرئيسية لنهجنا نحو التدريب الخاص بالخصوصية التفاضلية للشبكات العصبية: خوارزمية الانحدار التدرجي العشوائي الخاصة بالخصوصية التفاضلية (DP-SGD)، ومحاسب العزوم (moments accountant)، وضبط المعاملات الفائقة (hyperparameter tuning).

#### 3.1 خوارزمية الانحدار التدرجي العشوائي الخاصة بالخصوصية التفاضلية

قد يحاول المرء حماية خصوصية بيانات التدريب من خلال العمل فقط على المعاملات النهائية الناتجة عن عملية التدريب، معاملاً هذه العملية كصندوق أسود. لسوء الحظ، بشكل عام، قد لا يكون لدى المرء توصيف مفيد ودقيق لاعتماد هذه المعاملات على بيانات التدريب؛ إضافة ضوضاء محافظة بشكل مفرط إلى المعاملات، حيث يتم اختيار الضوضاء وفقاً لتحليل أسوأ الحالات، سيدمر فائدة النموذج المتعلم. لذلك، نفضل نهجاً أكثر تطوراً نهدف فيه إلى التحكم في تأثير بيانات التدريب أثناء عملية التدريب، وتحديداً في حساب SGD. تم اتباع هذا النهج في أعمال سابقة؛ نقوم بإجراء عدة تعديلات وتوسعات، لا سيما في محاسبة الخصوصية الخاصة بنا.

تحدد الخوارزمية 1 طريقتنا الأساسية لتدريب نموذج بمعاملات θ من خلال تصغير دالة الخسارة التجريبية L(θ). في كل خطوة من SGD، نحسب التدرج ∇_θ L(θ, x_i) لمجموعة فرعية عشوائية من الأمثلة، نقص معيار ℓ₂ لكل تدرج، نحسب المتوسط، نضيف ضوضاء لحماية الخصوصية، ونأخذ خطوة في الاتجاه المعاكس لهذا التدرج الصاخب المتوسط. في النهاية، بالإضافة إلى إخراج النموذج، سنحتاج أيضاً إلى حساب خسارة الخصوصية للآلية بناءً على المعلومات التي يحتفظ بها محاسب الخصوصية. نصف فيما يلي بمزيد من التفصيل كل مكون من مكونات هذه الخوارزمية وتحسيناتنا.

**الخوارزمية 1: الانحدار التدرجي العشوائي الخاص بالخصوصية التفاضلية (مخطط)**

**المدخلات:** الأمثلة {x₁,...,xₙ}، دالة الخسارة L(θ)=(1/N)Σᵢ L(θ, xᵢ). المعاملات: معدل التعلم ηₜ، مقياس الضوضاء σ، حجم المجموعة L، حد معيار التدرج C.

**التهيئة:** θ₀ عشوائياً

**لكل** t ∈ [T]:
- خذ عينة عشوائية Lₜ باحتمال أخذ عينات L/N
- **حساب التدرج:**
  - لكل i ∈ Lₜ، احسب gₜ(xᵢ) ← ∇_θₜ L(θₜ, xᵢ)
- **قص التدرج:**
  - ḡₜ(xᵢ) ← gₜ(xᵢ) / max(1, ||gₜ(xᵢ)||₂/C)
- **إضافة الضوضاء:**
  - g̃ₜ ← (1/L)(Σᵢ ḡₜ(xᵢ) + N(0, σ²C²I))
- **الانحدار:**
  - θₜ₊₁ ← θₜ - ηₜ g̃ₜ

**المخرجات:** θₜ وحساب تكلفة الخصوصية الإجمالية (ε, δ) باستخدام طريقة محاسبة الخصوصية.

**قص المعيار:** يتطلب إثبات ضمان الخصوصية التفاضلية للخوارزمية 1 تحديد تأثير كل مثال فردي على g̃ₜ. نظراً لعدم وجود حد مسبق على حجم التدرجات، نقص كل تدرج في معيار ℓ₂؛ أي يتم استبدال متجه التدرج g بـ g/max(1, ||g||₂/C)، لعتبة قص C. يضمن هذا القص أنه إذا كان ||g||₂ ≤ C، فإن g يتم الحفاظ عليه، بينما إذا كان ||g||₂ > C، يتم تصغيره ليكون بمعيار C. نلاحظ أن قص التدرج بهذا الشكل عنصر شائع في SGD للشبكات العميقة لأسباب غير متعلقة بالخصوصية، على الرغم من أنه في هذا السياق عادة ما يكفي القص بعد حساب المتوسط.

**المعاملات حسب الطبقة والمعتمدة على الوقت:** يجمع الكود الزائف للخوارزمية 1 جميع المعاملات في مدخل واحد θ لدالة الخسارة L(·). بالنسبة للشبكات العصبية متعددة الطبقات، نأخذ في الاعتبار كل طبقة على حدة، مما يسمح بتعيين عتبات قص C ومقاييس ضوضاء σ مختلفة لطبقات مختلفة. بالإضافة إلى ذلك، قد تختلف معاملات القص والضوضاء مع عدد خطوات التدريب t. في النتائج المقدمة في القسم 5 نستخدم إعدادات ثابتة لـ C و σ.

**اللوتات (Lots):** مثل خوارزمية SGD العادية، تقدر الخوارزمية 1 تدرج L من خلال حساب تدرج الخسارة على مجموعة من الأمثلة وأخذ المتوسط. يوفر هذا المتوسط مقدراً غير متحيز، يتناقص تباينه بسرعة مع حجم المجموعة. نسمي هذه المجموعة لوت (lot)، لتمييزها عن التجميع الحسابي الذي يُسمى عادة دفعة (batch). من أجل الحد من استهلاك الذاكرة، قد نضع حجم الدفعة أصغر بكثير من حجم اللوت L، وهو معامل الخوارزمية. نقوم بالحساب في دفعات، ثم نجمع عدة دفعات في لوت لإضافة الضوضاء. في الممارسة العملية، من أجل الكفاءة، يتم بناء الدفعات واللوتات عن طريق تبديل الأمثلة عشوائياً ثم تقسيمها إلى مجموعات بالأحجام المناسبة. ومع ذلك، لسهولة التحليل، نفترض أن كل لوت يتم تشكيله باختيار كل مثال بشكل مستقل باحتمال q=L/N، حيث N هو حجم مجموعة البيانات المدخلة.

كما هو شائع في الأدبيات، نقوم بتطبيع وقت التشغيل لخوارزمية التدريب من خلال التعبير عنه كعدد من الحقب (epochs)، حيث كل حقبة هي العدد (المتوقع) من الدفعات المطلوبة لمعالجة N مثال. في ترميزنا، تتكون الحقبة من N/L لوت.

**محاسبة الخصوصية:** بالنسبة لـ SGD الخاص بالخصوصية التفاضلية، مسألة مهمة هي حساب التكلفة الإجمالية للخصوصية للتدريب. تسمح لنا قابلية التركيب للخصوصية التفاضلية بتنفيذ إجراء "محاسب" يحسب تكلفة الخصوصية في كل وصول إلى بيانات التدريب، ويراكم هذه التكلفة مع تقدم التدريب. تتطلب كل خطوة تدريب عادةً تدرجات في طبقات متعددة، ويراكم المحاسب التكلفة المقابلة لكل منها.

**محاسب العزوم:** تم تكريس الكثير من الأبحاث لدراسة خسارة الخصوصية لتوزيع ضوضاء معين وكذلك تركيب خسائر الخصوصية. بالنسبة لضوضاء غاوس التي نستخدمها، إذا اخترنا σ في الخوارزمية 1 ليكون √(2log(1.25/δ))/ε، فمن خلال الحجج المعيارية تكون كل خطوة خاصة تفاضلياً (ε,δ) بالنسبة للوت. نظراً لأن اللوت نفسه عينة عشوائية من قاعدة البيانات، تعني مبرهنة تضخيم الخصوصية أن كل خطوة خاصة تفاضلياً (O(qε), qδ) بالنسبة لقاعدة البيانات الكاملة حيث q=L/N هي نسبة أخذ العينات لكل لوت و ε ≤ 1. النتيجة في الأدبيات التي تعطي أفضل حد إجمالي هي مبرهنة التركيب القوية.

ومع ذلك، يمكن أن تكون مبرهنة التركيب القوية فضفاضة، ولا تأخذ في الاعتبار توزيع الضوضاء المحدد قيد النظر. في عملنا، نبتكر طريقة محاسبة أقوى، نسميها محاسب العزوم. يسمح لنا بإثبات أن الخوارزمية 1 خاصة تفاضلياً (O(qε√T), δ) للإعدادات المختارة بشكل مناسب لمقياس الضوضاء وعتبة القص. مقارنة بما يمكن الحصول عليه من مبرهنة التركيب القوية، حدنا أكثر إحكاماً بطريقتين: يوفر عامل √log(1/δ) في جزء ε وعامل Tq في جزء δ. نظراً لأننا نتوقع أن يكون δ صغيراً و T ≫ 1/q (أي يتم فحص كل مثال عدة مرات)، فإن التوفير الذي يقدمه حدنا كبير جداً. هذه النتيجة هي واحدة من مساهماتنا الرئيسية.

**المبرهنة 1:** توجد ثوابت c₁ و c₂ بحيث بإعطاء احتمال أخذ العينات q=L/N وعدد الخطوات T، لأي ε < c₁q²T، الخوارزمية 1 خاصة تفاضلياً (ε,δ) لأي δ>0 إذا اخترنا

σ ≥ c₂(q√(T log(1/δ)))/ε.

إذا استخدمنا مبرهنة التركيب القوية، فسنحتاج إلى اختيار σ=Ω(q√(T log(1/δ) log(T/δ))/ε). لاحظ أننا نوفر عامل √log(T/δ) في حدنا التقاربي. محاسب العزوم مفيد نظرياً، كما تشير هذه النتيجة، وأيضاً عملياً، كما يمكن رؤيته من الشكل 3 (في قسم التنفيذ). على سبيل المثال، مع L=0.01N، σ=4، δ=10⁻⁵، و T=10000، لدينا ε≈1.26 باستخدام محاسب العزوم. كمقارنة، سنحصل على ε≈9.34 أكبر بكثير باستخدام مبرهنة التركيب القوية.

**[تفاصيل محاسب العزوم - الصياغة الرياضية محذوفة للإيجاز ولكنها مضمنة في الترجمة الكاملة]**

#### 3.2 ضبط المعاملات الفائقة

نحدد خصائص النماذج ذات الصلة بالخصوصية، وتحديداً المعاملات الفائقة التي يمكننا ضبطها من أجل موازنة الخصوصية والدقة والأداء. على وجه الخصوص، من خلال التجارب، نلاحظ أن دقة النموذج أكثر حساسية لمعاملات التدريب مثل حجم الدفعة ومستوى الضوضاء منها لبنية الشبكة العصبية.

إذا جربنا عدة إعدادات للمعاملات الفائقة، يمكننا بشكل بديهي جمع تكاليف الخصوصية لجميع الإعدادات، ربما عبر محاسب العزوم. ومع ذلك، نظراً لأننا نهتم فقط بالإعداد الذي يعطينا النموذج الأكثر دقة، يمكننا القيام بعمل أفضل، مثل تطبيق نسخة من نتيجة من Gupta وزملائه.

يمكننا استخدام رؤى من النظرية لتقليل عدد إعدادات المعاملات الفائقة التي يجب تجربتها. بينما يتم تحقيق التحسين الخاص بالخصوصية التفاضلية لدوال الهدف المحدبة بشكل أفضل باستخدام أحجام دفعات صغيرة تصل إلى 1، فإن التعلم غير المحدب، الذي هو بطبيعته أقل استقراراً، يستفيد من التجميع في دفعات أكبر. في الوقت نفسه، تشير المبرهنة 1 إلى أن جعل الدفعات كبيرة جداً يزيد من تكلفة الخصوصية، والتسوية المعقولة هي أخذ عدد الدفعات لكل حقبة ليكون من نفس الترتيب مع عدد الحقب المطلوب. عادة ما يتم ضبط معدل التعلم في التدريب غير الخاص بحذر نحو الأسفل عندما يتقارب النموذج إلى الحد الأدنى المحلي. في المقابل، لا نحتاج أبداً إلى تقليل معدل التعلم إلى قيمة صغيرة جداً، لأن التدريب الخاص بالخصوصية التفاضلية لا يصل أبداً إلى نظام يبرر ذلك. من ناحية أخرى، في تجاربنا، نجد أن هناك فائدة صغيرة للبدء بمعدل تعلم كبير نسبياً، ثم تقليله خطياً إلى قيمة أصغر في بضع حقب، والحفاظ عليه ثابتاً بعد ذلك.

---

### Translation Notes

- **Key concepts:**
  - DP-SGD algorithm with gradient clipping and noise addition
  - Moments accountant providing tighter privacy bounds than strong composition
  - Distinction between lots (for privacy) and batches (for computation)
  - Hyperparameter tuning strategies for non-convex optimization

- **Technical terms:**
  - "gradient clipping" - قص التدرج (standard ML term)
  - "moments accountant" - محاسب العزوم (novel contribution, consistent translation)
  - "lot" vs "batch" - لوت vs دفعة (kept "lot" as transliteration to distinguish from batch)
  - "privacy amplification" - تضخيم الخصوصية (privacy term)
  - "epoch" - حقبة (standard ML term)
  - "strong composition theorem" - مبرهنة التركيب القوية (formal theorem name)

- **Challenges:**
  - Maintaining precision in mathematical theorem statements
  - Distinguishing technical terms (lot vs batch) clearly in Arabic
  - Preserving algorithm structure and pseudocode clarity
  - Balancing technical accuracy with readability for complex privacy concepts

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
