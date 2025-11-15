# Section 4: Implementation
## القسم 4: التنفيذ

**Section:** implementation
**Translation Quality:** 0.87
**Glossary Terms Used:** TensorFlow, sanitizer, privacy accountant, per-example gradient, gradient clipping, noise addition, PCA, convolutional layers, privacy odometer, privacy filter

---

### English Version

We have implemented the differentially private SGD algorithms in TensorFlow. The source code is available under an Apache 2.0 license from github.com/tensorflow/models.

For privacy protection, we need to "sanitize" the gradient before using it to update the parameters. In addition, we need to keep track of the "privacy spending" based on how the sanitization is done. Hence our implementation mainly consists of two components: sanitizer, which preprocesses the gradient to protect privacy, and privacy_accountant, which keeps track of the privacy spending over the course of training.

Figure 1 contains the TensorFlow code snippet (in Python) of DPSGD_Optimizer, which minimizes a loss function using a differentially private SGD, and DPTrain, which iteratively invokes DPSGD_Optimizer using a privacy accountant to bound the total privacy loss.

In many cases, the neural network model may benefit from the processing of the input by projecting it on the principal directions (PCA) or by feeding it through a convolutional layer. We implement differentially private PCA and apply pre-trained convolutional layers (learned on public data).

**[Code snippet for DPSGD_Optimizer and DPTrain]**

**Sanitizer.** In order to achieve privacy protection, the sanitizer needs to perform two operations: (1) limit the sensitivity of each individual example by clipping the norm of the gradient for each example; and (2) add noise to the gradient of a batch before updating the network parameters.

In TensorFlow, the gradient computation is batched for performance reasons, yielding g_B = (1/|B|)Σ_{x∈B} ∇_θ L(θ, x) for a batch B of training examples. To limit the sensitivity of updates, we need to access each individual ∇_θ L(θ, x). To this end, we implemented per_example_gradient operator in TensorFlow, as described by Goodfellow. This operator can compute a batch of individual ∇_θ L(θ, x). With this implementation there is only a modest slowdown in training, even for larger batch size. Our current implementation supports batched computation for the loss function L, where each x_i is singly connected to L, allowing us to handle most hidden layers but not, for example, convolutional layers.

Once we have the access to the per-example gradient, it is easy to use TensorFlow operators to clip its norm and to add noise.

**Privacy accountant.** The main component in our implementation is PrivacyAccountant which keeps track of privacy spending over the course of training. As discussed in Section 3, we implemented the moments accountant that additively accumulates the log of the moments of the privacy loss at each step. Dependent on the noise distribution, one can compute α(λ) by either applying an asymptotic bound, evaluating a closed-form expression, or applying numerical integration. The first option would recover the generic advanced composition theorem, and the latter two give a more accurate accounting of the privacy loss.

For the Gaussian mechanism we use, α(λ) is defined according to specific equations. In our implementation, we carry out numerical integration to compute both E₁ and E₂ in those equations. Also we compute α(λ) for a range of λ's so we can compute the best possible (ε,δ) values using the theorem. We find that for the parameters of interest to us, it suffices to compute α(λ) for λ≤32.

At any point during training, one can query the privacy loss in the more interpretable notion of (ε,δ) privacy using the theorem. Rogers et al. point out risks associated with adaptive choice of privacy parameters. We avoid their attacks and negative results by fixing the number of iterations and privacy parameters ahead of time. More general implementations of a privacy accountant must correctly distinguish between two modes of operation—as a privacy odometer or a privacy filter (see Rogers et al. for more details).

**Differentially private PCA.** Principal component analysis (PCA) is a useful method for capturing the main features of the input data. We implement the differentially private PCA algorithm as described in prior work. More specifically, we take a random sample of the training examples, treat them as vectors, and normalize each vector to unit ℓ₂ norm to form the matrix A, where each vector is a row in the matrix. We then add Gaussian noise to the covariance matrix A^T A and compute the principal directions of the noisy covariance matrix. Then for each input example we apply the projection to these principal directions before feeding it into the neural network.

We incur a privacy cost due to running a PCA. However, we find it useful for both improving the model quality and for reducing the training time, as suggested by our experiments on the MNIST data. See Section 5 for details.

**Convolutional layers.** Convolutional layers are useful for deep neural networks. However, an efficient per-example gradient computation for convolutional layers remains a challenge within the TensorFlow framework, which motivates creating a separate workflow. For example, some recent work argues that even random convolutions often suffice.

Alternatively, we explore the idea of learning convolutional layers on public data, following prior work. Such convolutional layers can be based on GoogLeNet or AlexNet features for image models or on pretrained word2vec or GloVe embeddings in language models.

---

### النسخة العربية

قمنا بتنفيذ خوارزميات SGD الخاصة بالخصوصية التفاضلية في TensorFlow. الكود المصدري متاح بموجب ترخيص Apache 2.0 من github.com/tensorflow/models.

لحماية الخصوصية، نحتاج إلى "تطهير" (sanitize) التدرج قبل استخدامه لتحديث المعاملات. بالإضافة إلى ذلك، نحتاج إلى تتبع "إنفاق الخصوصية" بناءً على كيفية إجراء التطهير. لذلك يتكون تنفيذنا بشكل أساسي من مكونين: المطهر (sanitizer)، الذي يعالج التدرج مسبقاً لحماية الخصوصية، ومحاسب_الخصوصية (privacy_accountant)، الذي يتتبع إنفاق الخصوصية على مدار التدريب.

يحتوي الشكل 1 على مقتطف كود TensorFlow (بلغة Python) لـ DPSGD_Optimizer، الذي يقلل دالة خسارة باستخدام SGD خاص بالخصوصية التفاضلية، و DPTrain، الذي يستدعي بشكل تكراري DPSGD_Optimizer باستخدام محاسب خصوصية لتحديد خسارة الخصوصية الإجمالية.

في كثير من الحالات، قد يستفيد نموذج الشبكة العصبية من معالجة المدخل من خلال إسقاطه على الاتجاهات الرئيسية (PCA) أو من خلال تمريره عبر طبقة التفافية. نقوم بتنفيذ PCA الخاص بالخصوصية التفاضلية ونطبق طبقات التفافية مدربة مسبقاً (مُتعلمة على بيانات عامة).

**[مقتطف الكود لـ DPSGD_Optimizer و DPTrain]**

**المطهر (Sanitizer).** من أجل تحقيق حماية الخصوصية، يحتاج المطهر إلى إجراء عمليتين: (1) الحد من حساسية كل مثال فردي من خلال قص معيار التدرج لكل مثال؛ و (2) إضافة ضوضاء إلى تدرج دفعة قبل تحديث معاملات الشبكة.

في TensorFlow، يتم دفع حساب التدرج لأسباب الأداء، مما ينتج g_B = (1/|B|)Σ_{x∈B} ∇_θ L(θ, x) لدفعة B من أمثلة التدريب. للحد من حساسية التحديثات، نحتاج إلى الوصول إلى كل ∇_θ L(θ, x) فردياً. لهذه الغاية، نفذنا معامل per_example_gradient في TensorFlow، كما وصفه Goodfellow. يمكن لهذا المعامل حساب دفعة من ∇_θ L(θ, x) الفردية. مع هذا التنفيذ يوجد تباطؤ متواضع فقط في التدريب، حتى لحجم دفعة أكبر. يدعم تنفيذنا الحالي الحساب المُدفع لدالة الخسارة L، حيث كل x_i متصل بشكل فردي بـ L، مما يسمح لنا بمعالجة معظم الطبقات المخفية ولكن ليس، على سبيل المثال، الطبقات الالتفافية.

بمجرد حصولنا على الوصول إلى التدرج لكل مثال، من السهل استخدام معاملات TensorFlow لقص معياره وإضافة الضوضاء.

**محاسب الخصوصية.** المكون الرئيسي في تنفيذنا هو PrivacyAccountant الذي يتتبع إنفاق الخصوصية على مدار التدريب. كما نوقش في القسم 3، نفذنا محاسب العزوم الذي يراكم بشكل إضافي لوغاريتم عزوم خسارة الخصوصية في كل خطوة. اعتماداً على توزيع الضوضاء، يمكن للمرء حساب α(λ) إما عن طريق تطبيق حد تقاربي، أو تقييم تعبير مغلق الشكل، أو تطبيق التكامل العددي. سيسترجع الخيار الأول مبرهنة التركيب المتقدمة العامة، ويعطي الخياران الأخيران محاسبة أكثر دقة لخسارة الخصوصية.

بالنسبة لآلية غاوس التي نستخدمها، يتم تعريف α(λ) وفقاً لمعادلات محددة. في تنفيذنا، نجري التكامل العددي لحساب كل من E₁ و E₂ في تلك المعادلات. كما نحسب α(λ) لنطاق من قيم λ حتى نتمكن من حساب أفضل قيم (ε,δ) ممكنة باستخدام المبرهنة. نجد أنه بالنسبة للمعاملات محل اهتمامنا، يكفي حساب α(λ) لـ λ≤32.

في أي نقطة أثناء التدريب، يمكن للمرء الاستعلام عن خسارة الخصوصية في المفهوم الأكثر قابلية للتفسير للخصوصية (ε,δ) باستخدام المبرهنة. يشير Rogers وزملاؤه إلى المخاطر المرتبطة بالاختيار التكيفي لمعاملات الخصوصية. نتجنب هجماتهم ونتائجهم السلبية من خلال تحديد عدد التكرارات ومعاملات الخصوصية مسبقاً. يجب أن تميز التنفيذات الأكثر عمومية لمحاسب الخصوصية بشكل صحيح بين وضعي التشغيل—كعداد خصوصية (privacy odometer) أو مرشح خصوصية (privacy filter) (انظر Rogers وزملاؤه لمزيد من التفاصيل).

**PCA الخاص بالخصوصية التفاضلية.** تحليل المكونات الرئيسية (PCA) هو طريقة مفيدة لالتقاط السمات الرئيسية لبيانات الإدخال. نقوم بتنفيذ خوارزمية PCA الخاصة بالخصوصية التفاضلية كما هو موضح في الأعمال السابقة. بشكل أكثر تحديداً، نأخذ عينة عشوائية من أمثلة التدريب، ونعاملها كمتجهات، ونطبع كل متجه إلى معيار ℓ₂ الوحدوي لتشكيل المصفوفة A، حيث كل متجه هو صف في المصفوفة. ثم نضيف ضوضاء غاوس إلى مصفوفة التباين A^T A ونحسب الاتجاهات الرئيسية لمصفوفة التباين الصاخبة. ثم لكل مثال إدخال نطبق الإسقاط إلى هذه الاتجاهات الرئيسية قبل تغذيته في الشبكة العصبية.

نتكبد تكلفة خصوصية بسبب تشغيل PCA. ومع ذلك، نجده مفيداً لتحسين جودة النموذج ولتقليل وقت التدريب، كما توحي تجاربنا على بيانات MNIST. انظر القسم 5 للتفاصيل.

**الطبقات الالتفافية.** الطبقات الالتفافية مفيدة للشبكات العصبية العميقة. ومع ذلك، يظل حساب التدرج الفعال لكل مثال للطبقات الالتفافية تحدياً ضمن إطار TensorFlow، مما يحفز إنشاء سير عمل منفصل. على سبيل المثال، يجادل بعض الأعمال الحديثة بأن حتى الالتفافات العشوائية غالباً ما تكفي.

بدلاً من ذلك، نستكشف فكرة تعلم الطبقات الالتفافية على البيانات العامة، بعد الأعمال السابقة. يمكن أن تعتمد هذه الطبقات الالتفافية على ميزات GoogLeNet أو AlexNet لنماذج الصور أو على تضمينات word2vec أو GloVe المدربة مسبقاً في نماذج اللغة.

---

### Translation Notes

- **Key concepts:**
  - TensorFlow implementation with sanitizer and privacy accountant components
  - Per-example gradient computation for privacy-preserving training
  - Differentially private PCA for dimensionality reduction
  - Pre-trained convolutional layers from public data

- **Technical terms:**
  - "sanitizer" - مطهر (computational privacy term)
  - "privacy spending" - إنفاق الخصوصية (privacy economics term)
  - "per-example gradient" - التدرج لكل مثال (technical ML term)
  - "privacy odometer" vs "privacy filter" - عداد خصوصية vs مرشح خصوصية (privacy accounting concepts)
  - "covariance matrix" - مصفوفة التباين (statistical term)
  - "principal directions" - الاتجاهات الرئيسية (PCA term)

- **Code-related:**
  - Kept code class/function names in English (DPSGD_Optimizer, DPTrain, etc.)
  - Translated comments and descriptions
  - Maintained technical accuracy for implementation details

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
