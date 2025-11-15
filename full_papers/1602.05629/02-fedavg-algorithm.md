# Section 2: The FederatedAveraging Algorithm
## القسم 2: خوارزمية متوسط الاتحادي

**Section:** methodology
**Translation Quality:** 0.86
**Glossary Terms Used:** SGD (الانحدار التدرجي العشوائي), gradient (التدرج), optimization (التحسين), batch (دفعة), minibatch (الدفعة الصغيرة), learning rate (معدل التعلم), convergence (تقارب), parameter (معامل), loss function (دالة الخسارة), epoch (حقبة)

---

### English Version

**2. The FederatedAveraging Algorithm**

The recent multitude of successful applications of deep learning have almost exclusively relied on variants of stochastic gradient descent (SGD) for optimization. Thus, our approach to federated optimization is to build on this strong foundation.

**Naive Federated SGD.** A typical implementation of SGD on a single machine iterates over small minibatches taken randomly from the full training set, and computes the gradient of the loss on each minibatch. Naively applying this approach to the federated setting could be done by selecting a single random client on each round, computing the gradient of the loss over all the data on that client, and sending this gradient to the server which then applies the gradient with some learning rate to update the model. This approach is very computationally efficient, but as we show in the experiments section, requires very large numbers of rounds of training to produce good models.

**FedSGD.** For our baseline federated optimization algorithm, we select a C-fraction of clients on each round, and compute the gradient of the loss over all the data held by these clients. Thus, C controls the global batch size, with C=1 corresponding to full-batch (non-stochastic) gradient descent. We refer to this baseline as FedSGD. With the federated dataset corresponding to K clients, the parameter vector w is initialized randomly. Then, on each round of FedSGD, a random subset of C·K clients is selected, and the gradient of f is computed as:

$$g_t = \sum_{k \in S_t} \frac{n_k}{n} \nabla F_k(w_t)$$

where S_t denotes the set of K·C clients selected at round t. The server then uses this gradient to update the global model:

$$w_{t+1} \leftarrow w_t - \eta g_t$$

where η is the learning rate. In our experiments we typically have K ≥ 1000 and C ≥ 0.01, giving a minimum batch size of 10. Since we use a fixed learning rate η and never increase the batch size, this is quite similar to large-batch synchronous SGD as used for distributed training (e.g., Das et al., 2016).

**Extension to FedAvg.** From FedSGD, we can gain computational efficiency by adding more computation to each client, and this will form the foundation of FederatedAveraging. One approach to doing more computation per client is to iterate the local update w ← w - η∇F_k(w) multiple times before the averaging step. Analogous to how adding more data (increasing the batch size) can be important for reaching a given accuracy level, we might expect that doing more computation per client could also be beneficial. We show empirically that this is indeed the case.

The full FederatedAveraging algorithm involves three key hyperparameters: C, the fraction of clients that perform computation on each round; E, the number of training passes each client makes over its local dataset on each round; and B, the local minibatch size used for the client updates. We will write B = ∞ to indicate that the full local dataset is treated as a single minibatch. Thus, in this notation, B = ∞ and E = 1 corresponds exactly to FedSGD. Algorithm 1 below shows the complete FederatedAveraging algorithm.

**Algorithm 1: FederatedAveraging**

```
Server executes:
  initialize w_0
  for each round t = 1, 2, ... do
    m ← max(C · K, 1)
    S_t ← (random set of m clients)
    for each client k ∈ S_t in parallel do
      w_{t+1}^k ← ClientUpdate(k, w_t)
    w_{t+1} ← Σ_{k=1}^K (n_k/n) w_{t+1}^k

ClientUpdate(k, w):  // Run on client k
  ℬ ← (split 𝒫_k into batches of size B)
  for each local epoch i from 1 to E do
    for batch b ∈ ℬ do
      w ← w - η ∇ℓ(w; b)
  return w to server
```

Note that when E = 1 and B = |𝒫_k| (the size of the local dataset), the amount of computation is essentially identical to FedSGD while still allowing the system to scale to larger K by selecting a random sample of clients on each round. Another simple baseline is to use one local epoch (E = 1) but allow for smaller minibatches (B < |𝒫_k|), which makes each client update more computationally efficient but still requires computing the full gradient for each client on each round if the goal is to match the computation performed by FedSGD.

The expected number of gradient computations performed by each client per round is u = E·n_k/B. We will be particularly interested in how the number of communication rounds needed varies as we increase u while holding the total number of gradient computations fixed. Let G = u·K·C be the total number of gradient computations per round. We can increase u in two ways: either by increasing the number of local epochs E, or by decreasing the minibatch size B. We find that each has a different effect on convergence: reducing B tends to slow convergence (for B < |𝒫_k|), whereas increasing E can slow convergence when the data is IID but can speed convergence on non-IID data.

**Why does FedAvg work?** For general non-convex objectives, averaging models in parameter space could produce an arbitrarily bad model. For example, consider training an arbitrary neural network where the output of each node is multiplied by -1, and the weights on the next layer are also multiplied by -1. This leaves the overall network function unchanged, but averaging the parameters of such a network with a network without such a negation would produce a model with parameters of all zeros. However, practical experience suggests this pathological behavior is not common when training neural networks.

We empirically investigated this issue as follows: We initialized two models from the same random initialization, and then trained each model independently on a different subset of the data (corresponding to different clients in the federated setting), each for some number of epochs. We then created three test models: one by taking each trained model individually, and one by averaging the parameters of the two models. Figure 1 (not shown here) plots test accuracy versus train accuracy for these three models, for fully-connected networks trained on MNIST, showing that parameter averaging works well in practice.

Recent research has made progress in understanding neural network loss surfaces, suggesting they are surprisingly well-behaved. For instance, Choromanska et al. (2015) give results for spin-glass models that indicate the loss surfaces of sufficiently over-parameterized neural networks are less prone to bad local minima than previously thought. Goodfellow et al. (2015) show empirically that the straight line path in weight space between one local minimum and another is often itself of low loss. Our results on model averaging are consistent with this view.

Moreover, even for convex problems, it is not clear why FedAvg should work significantly better than FedSGD. Parallel training using synchronized SGD with even very large batches (say, all the data from C·K clients) has been shown to work well for deep networks (Das et al., 2016; Goyal et al., 2017). Thus, one might expect that the batch size implicit in FedSGD would be more than adequate, especially since we use C ≥ 0.01 in our experiments. We hypothesize that the improved performance of FedAvg is due to the implicit regularization effect of the local updates, which is similar to (but distinct from) the effect achieved by dropout (Srivastava et al., 2014) and other explicit regularization techniques. The local client updates act somewhat like stochastic perturbations to the global model, and such noise can have a regularizing effect in SGD-based training. We leave a more formal analysis of this hypothesis to future work.

---

### النسخة العربية

**2. خوارزمية متوسط الاتحادي**

اعتمدت التطبيقات الناجحة الحديثة العديدة للتعلم العميق بشكل حصري تقريباً على متغيرات الانحدار التدرجي العشوائي (SGD) للتحسين. وبالتالي، فإن نهجنا للتحسين الاتحادي هو البناء على هذا الأساس القوي.

**الانحدار التدرجي العشوائي الاتحادي الساذج.** التنفيذ النموذجي لـ SGD على جهاز واحد يتكرر على دفعات صغيرة مأخوذة عشوائياً من مجموعة التدريب الكاملة، ويحسب تدرج الخسارة على كل دفعة صغيرة. يمكن تطبيق هذا النهج بشكل ساذج على الإعداد الاتحادي عن طريق اختيار عميل عشوائي واحد في كل جولة، وحساب تدرج الخسارة على جميع البيانات الموجودة على ذلك العميل، وإرسال هذا التدرج إلى الخادم الذي يطبق بعد ذلك التدرج بمعدل تعلم معين لتحديث النموذج. هذا النهج فعال حسابياً جداً، ولكن كما نوضح في قسم التجارب، يتطلب أعداداً كبيرة جداً من جولات التدريب لإنتاج نماذج جيدة.

**FedSGD.** بالنسبة لخوارزمية التحسين الاتحادية الأساسية لدينا، نختار جزءاً C من العملاء في كل جولة، ونحسب تدرج الخسارة على جميع البيانات التي يحتفظ بها هؤلاء العملاء. وبالتالي، يتحكم C في حجم الدفعة العامة، مع C=1 يقابل الانحدار التدرجي الكامل للدفعة (غير العشوائي). نشير إلى هذا الخط الأساسي باسم FedSGD. مع مجموعة البيانات الاتحادية المقابلة لـ K عميل، يتم تهيئة متجه المعاملات w عشوائياً. ثم، في كل جولة من FedSGD، يتم اختيار مجموعة فرعية عشوائية من C·K عميل، ويتم حساب تدرج f كـ:

$$g_t = \sum_{k \in S_t} \frac{n_k}{n} \nabla F_k(w_t)$$

حيث $S_t$ يشير إلى مجموعة عملاء K·C المختارين في الجولة t. ثم يستخدم الخادم هذا التدرج لتحديث النموذج العام:

$$w_{t+1} \leftarrow w_t - \eta g_t$$

حيث η هو معدل التعلم. في تجاربنا عادة ما يكون لدينا K ≥ 1000 و C ≥ 0.01، مما يعطي حجم دفعة أدنى يبلغ 10. نظراً لأننا نستخدم معدل تعلم ثابت η ولا نزيد أبداً حجم الدفعة، فهذا مشابه تماماً لـ SGD المتزامن ذو الدفعة الكبيرة كما هو مستخدم للتدريب الموزع (على سبيل المثال، Das et al., 2016).

**التوسع إلى FedAvg.** من FedSGD، يمكننا الحصول على كفاءة حسابية عن طريق إضافة المزيد من الحساب إلى كل عميل، وهذا سيشكل أساس متوسط الاتحادي. إحدى الطرق للقيام بمزيد من الحساب لكل عميل هي تكرار التحديث المحلي w ← w - η∇F_k(w) عدة مرات قبل خطوة حساب المتوسط. بالمثل مع كيف يمكن أن تكون إضافة المزيد من البيانات (زيادة حجم الدفعة) مهمة للوصول إلى مستوى دقة معين، قد نتوقع أن القيام بمزيد من الحساب لكل عميل يمكن أن يكون مفيداً أيضاً. نوضح تجريبياً أن هذا هو الحال بالفعل.

تتضمن خوارزمية متوسط الاتحادي الكاملة ثلاثة معاملات فائقة رئيسية: C، وهو الجزء من العملاء الذين يقومون بالحساب في كل جولة؛ E، وهو عدد مرات التدريب التي يقوم بها كل عميل على مجموعة بياناته المحلية في كل جولة؛ و B، وهو حجم الدفعة الصغيرة المحلية المستخدمة لتحديثات العميل. سنكتب B = ∞ للإشارة إلى أن مجموعة البيانات المحلية الكاملة تعامل كدفعة صغيرة واحدة. وبالتالي، في هذا الترميز، B = ∞ و E = 1 يقابل بالضبط FedSGD. تُظهر الخوارزمية 1 أدناه خوارزمية متوسط الاتحادي الكاملة.

**الخوارزمية 1: متوسط الاتحادي (FederatedAveraging)**

```
يُنفذ الخادم:
  تهيئة w_0
  لكل جولة t = 1, 2, ... قم بـ
    m ← max(C · K, 1)
    S_t ← (مجموعة عشوائية من m عميل)
    لكل عميل k ∈ S_t بشكل متوازي قم بـ
      w_{t+1}^k ← ClientUpdate(k, w_t)
    w_{t+1} ← Σ_{k=1}^K (n_k/n) w_{t+1}^k

ClientUpdate(k, w):  // يُنفذ على العميل k
  ℬ ← (تقسيم 𝒫_k إلى دفعات بحجم B)
  لكل حقبة محلية i من 1 إلى E قم بـ
    لكل دفعة b ∈ ℬ قم بـ
      w ← w - η ∇ℓ(w; b)
  إرجاع w إلى الخادم
```

لاحظ أنه عندما E = 1 و B = |𝒫_k| (حجم مجموعة البيانات المحلية)، فإن كمية الحساب متطابقة بشكل أساسي مع FedSGD بينما لا تزال تسمح للنظام بالتوسع إلى K أكبر عن طريق اختيار عينة عشوائية من العملاء في كل جولة. خط أساسي بسيط آخر هو استخدام حقبة محلية واحدة (E = 1) ولكن السماح بدفعات صغيرة أصغر (B < |𝒫_k|)، مما يجعل كل تحديث للعميل أكثر كفاءة حسابياً ولكنه لا يزال يتطلب حساب التدرج الكامل لكل عميل في كل جولة إذا كان الهدف هو مطابقة الحساب الذي يتم إجراؤه بواسطة FedSGD.

العدد المتوقع لحسابات التدرج التي يقوم بها كل عميل لكل جولة هو u = E·n_k/B. سنكون مهتمين بشكل خاص بكيفية تباين عدد جولات الاتصال المطلوبة عندما نزيد u مع الحفاظ على العدد الإجمالي لحسابات التدرج ثابتاً. لتكن G = u·K·C هي العدد الإجمالي لحسابات التدرج لكل جولة. يمكننا زيادة u بطريقتين: إما عن طريق زيادة عدد الحقب المحلية E، أو عن طريق تقليل حجم الدفعة الصغيرة B. نجد أن كل منهما له تأثير مختلف على التقارب: يميل تقليل B إلى إبطاء التقارب (لـ B < |𝒫_k|)، في حين أن زيادة E يمكن أن تبطئ التقارب عندما تكون البيانات IID ولكن يمكن أن تسرع التقارب على بيانات non-IID.

**لماذا يعمل FedAvg؟** بالنسبة للأهداف غير المحدبة العامة، يمكن أن ينتج حساب متوسط النماذج في فضاء المعاملات نموذجاً سيئاً بشكل تعسفي. على سبيل المثال، ضع في اعتبارك تدريب شبكة عصبية تعسفية حيث يتم ضرب إخراج كل عقدة بـ -1، ويتم أيضاً ضرب الأوزان على الطبقة التالية بـ -1. هذا يترك دالة الشبكة الإجمالية دون تغيير، ولكن حساب متوسط معاملات مثل هذه الشبكة مع شبكة بدون مثل هذا النفي سينتج نموذجاً بمعاملات كلها أصفار. ومع ذلك، تشير التجربة العملية إلى أن هذا السلوك المرضي ليس شائعاً عند تدريب الشبكات العصبية.

قمنا بالتحقيق تجريبياً في هذه المسألة على النحو التالي: قمنا بتهيئة نموذجين من نفس التهيئة العشوائية، ثم قمنا بتدريب كل نموذج بشكل مستقل على مجموعة فرعية مختلفة من البيانات (المقابلة لعملاء مختلفين في الإعداد الاتحادي)، كل منهما لعدد معين من الحقب. ثم قمنا بإنشاء ثلاثة نماذج اختبار: واحد عن طريق أخذ كل نموذج مدرب بشكل فردي، وواحد عن طريق حساب متوسط معاملات النموذجين. الشكل 1 (غير موضح هنا) يرسم دقة الاختبار مقابل دقة التدريب لهذه النماذج الثلاثة، للشبكات المتصلة بالكامل المدربة على MNIST، مما يدل على أن حساب متوسط المعاملات يعمل بشكل جيد في الممارسة.

أحرزت الأبحاث الحديثة تقدماً في فهم أسطح خسارة الشبكات العصبية، مما يشير إلى أنها ذات سلوك جيد بشكل مفاجئ. على سبيل المثال، Choromanska et al. (2015) يعطون نتائج لنماذج الزجاج الدوراني تشير إلى أن أسطح الخسارة للشبكات العصبية المفرطة المعاملات بشكل كافٍ أقل عرضة للحد الأدنى المحلي السيئ مما كان يعتقد سابقاً. Goodfellow et al. (2015) يوضحون تجريبياً أن مسار الخط المستقيم في فضاء الأوزان بين حد أدنى محلي وآخر غالباً ما يكون نفسه ذو خسارة منخفضة. نتائجنا على حساب متوسط النماذج متسقة مع وجهة النظر هذه.

علاوة على ذلك، حتى بالنسبة للمشاكل المحدبة، ليس من الواضح لماذا يجب أن يعمل FedAvg بشكل أفضل بكثير من FedSGD. تم إظهار أن التدريب المتوازي باستخدام SGD المتزامن بدفعات كبيرة جداً (على سبيل المثال، جميع البيانات من عملاء C·K) يعمل بشكل جيد للشبكات العميقة (Das et al., 2016; Goyal et al., 2017). وبالتالي، قد يتوقع المرء أن يكون حجم الدفعة الضمني في FedSGD أكثر من كافٍ، خاصة وأننا نستخدم C ≥ 0.01 في تجاربنا. نفترض أن الأداء المحسّن لـ FedAvg يرجع إلى تأثير التنظيم الضمني للتحديثات المحلية، والذي يشبه (ولكنه يختلف عن) التأثير الذي يتم تحقيقه بواسطة dropout (Srivastava et al., 2014) وتقنيات التنظيم الصريحة الأخرى. تعمل تحديثات العميل المحلية إلى حد ما مثل الاضطرابات العشوائية للنموذج العام، ومثل هذا الضجيج يمكن أن يكون له تأثير تنظيمي في التدريب القائم على SGD. نترك تحليلاً أكثر رسمية لهذه الفرضية للعمل المستقبلي.

---

### Translation Notes

- **Figures referenced:** Figure 1 (mentioned but not reproduced in text)
- **Key terms introduced:** FedSGD, FedAvg (متوسط الاتحادي), ClientUpdate function, hyperparameters C, E, B
- **Equations:** 2 main equations for gradient computation and weight update
- **Citations:** Approximately 10 references
- **Special handling:** Algorithm 1 pseudocode translated with Arabic comments; mathematical notation preserved

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.89
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.86
