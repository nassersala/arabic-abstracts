# Section 5: Optimizing a Neural Radiance Field
## القسم 5: تحسين حقل الإشعاع العصبي

**Section:** optimization
**Translation Quality:** 0.86
**Glossary Terms Used:** optimization, positional encoding, hierarchical sampling, high-frequency function, universal function approximator, spectral bias, Transformer, coarse network, fine network, inverse transform sampling, Adam optimizer, learning rate, batch size, NVIDIA V100 GPU

---

### English Version

In the previous section we have described the core components necessary for modeling a scene as a neural radiance field and rendering novel views from this representation. However, we observe that these components are not sufficient for achieving state-of-the-art quality, as demonstrated in Section 6.4). We introduce two improvements to enable representing high-resolution complex scenes. The first is a positional encoding of the input coordinates that assists the MLP in representing high-frequency functions, and the second is a hierarchical sampling procedure that allows us to efficiently sample this high-frequency representation.

## 5.1 Positional encoding

Despite the fact that neural networks are universal function approximators [14], we found that having the network F_Θ directly operate on xyzθφ input coordinates results in renderings that perform poorly at representing high-frequency variation in color and geometry. This is consistent with recent work by Rahaman et al. [35], which shows that deep networks are biased towards learning lower frequency functions. They additionally show that mapping the inputs to a higher dimensional space using high frequency functions before passing them to the network enables better fitting of data that contains high frequency variation.

We leverage these findings in the context of neural scene representations, and show that reformulating F_Θ as a composition of two functions F_Θ = F'_Θ ◦ γ, one learned and one not, significantly improves performance (see Fig. 4 and Table 2). Here γ is a mapping from ℝ into a higher dimensional space ℝ^(2L), and F'_Θ is still simply a regular MLP. Formally, the encoding function we use is:

$$\gamma(p) = \left(\sin(2^0\pi p), \cos(2^0\pi p), \cdots, \sin(2^{L-1}\pi p), \cos(2^{L-1}\pi p)\right).$$

This function γ(·) is applied separately to each of the three coordinate values in **x** (which are normalized to lie in [−1, 1]) and to the three components of the Cartesian viewing direction unit vector **d** (which by construction lie in [−1, 1]). In our experiments, we set L = 10 for γ(**x**) and L = 4 for γ(**d**).

A similar mapping is used in the popular Transformer architecture [47], where it is referred to as a positional encoding. However, Transformers use it for a different goal of providing the discrete positions of tokens in a sequence as input to an architecture that does not contain any notion of order. In contrast, we use these functions to map continuous input coordinates into a higher dimensional space to enable our MLP to more easily approximate a higher frequency function. Concurrent work on a related problem of modeling 3D protein structure from projections [51] also utilizes a similar input coordinate mapping.

## 5.2 Hierarchical volume sampling

Our rendering strategy of densely evaluating the neural radiance field network at N query points along each camera ray is inefficient: free space and occluded regions that do not contribute to the rendered image are still sampled repeatedly. We draw inspiration from early work in volume rendering [20] and propose a hierarchical representation that increases rendering efficiency by allocating samples proportionally to their expected effect on the final rendering.

Instead of just using a single network to represent the scene, we simultaneously optimize two networks: one "coarse" and one "fine". We first sample a set of N_c locations using stratified sampling, and evaluate the "coarse" network at these locations as described in Eqns. 2 and 3. Given the output of this "coarse" network, we then produce a more informed sampling of points along each ray where samples are biased towards the relevant parts of the volume. To do this, we first rewrite the alpha composited color from the coarse network $\hat{C}_c(\mathbf{r})$ in Eqn. 3 as a weighted sum of all sampled colors **c**_i along the ray:

$$\hat{C}_c(\mathbf{r}) = \sum_{i=1}^{N_c} w_i\mathbf{c}_i, \quad w_i = T_i(1 - \exp(-\sigma_i\delta_i)).$$

Normalizing these weights as $\hat{w}_i = w_i/\sum_{j=1}^{N_c} w_j$ produces a piecewise-constant PDF along the ray. We sample a second set of N_f locations from this distribution using inverse transform sampling, evaluate our "fine" network at the union of the first and second set of samples, and compute the final rendered color of the ray $\hat{C}_f(\mathbf{r})$ using Eqn. 3 but using all N_c+N_f samples. This procedure allocates more samples to regions we expect to contain visible content. This addresses a similar goal as importance sampling, but we use the sampled values as a nonuniform discretization of the whole integration domain rather than treating each sample as an independent probabilistic estimate of the entire integral.

## 5.3 Implementation details

We optimize a separate neural continuous volume representation network for each scene. This requires only a dataset of captured RGB images of the scene, the corresponding camera poses and intrinsic parameters, and scene bounds (we use ground truth camera poses, intrinsics, and bounds for synthetic data, and use the COLMAP structure-from-motion package [39] to estimate these parameters for real data). At each optimization iteration, we randomly sample a batch of camera rays from the set of all pixels in the dataset, and then follow the hierarchical sampling described in Sec. 5.2 to query N_c samples from the coarse network and N_c + N_f samples from the fine network. We then use the volume rendering procedure described in Sec. 4 to render the color of each ray from both sets of samples. Our loss is simply the total squared error between the rendered and true pixel colors for both the coarse and fine renderings:

$$\mathcal{L} = \sum_{\mathbf{r}\in\mathcal{R}} \left[\left\|\hat{C}_c(\mathbf{r}) - C(\mathbf{r})\right\|_2^2 + \left\|\hat{C}_f(\mathbf{r}) - C(\mathbf{r})\right\|_2^2\right]$$

where ℝ is the set of rays in each batch, and C(**r**), $\hat{C}_c(\mathbf{r})$, and $\hat{C}_f(\mathbf{r})$ are the ground truth, coarse volume predicted, and fine volume predicted RGB colors for ray **r** respectively. Note that even though the final rendering comes from $\hat{C}_f(\mathbf{r})$, we also minimize the loss of $\hat{C}_c(\mathbf{r})$ so that the weight distribution from the coarse network can be used to allocate samples in the fine network.

In our experiments, we use a batch size of 4096 rays, each sampled at N_c = 64 coordinates in the coarse volume and N_f = 128 additional coordinates in the fine volume. We use the Adam optimizer [18] with a learning rate that begins at 5 × 10^(−4) and decays exponentially to 5 × 10^(−5) over the course of optimization (other Adam hyperparameters are left at default values of β_1 = 0.9, β_2 = 0.999, and ε = 10^(−7)). The optimization for a single scene typically take around 100–300k iterations to converge on a single NVIDIA V100 GPU (about 1–2 days).

---

### النسخة العربية

في القسم السابق، وصفنا المكونات الأساسية اللازمة لنمذجة مشهد كحقل إشعاع عصبي وتصيير مناظر جديدة من هذا التمثيل. ومع ذلك، نلاحظ أن هذه المكونات ليست كافية لتحقيق جودة متقدمة، كما هو موضح في القسم 6.4). نقدم تحسينين لتمكين تمثيل مشاهد معقدة عالية الدقة. الأول هو ترميز موضعي للإحداثيات المدخلة يساعد MLP في تمثيل دوال عالية التردد، والثاني هو إجراء أخذ عينات هرمي يسمح لنا بأخذ عينات فعالة من هذا التمثيل عالي التردد.

## 5.1 الترميز الموضعي

على الرغم من أن الشبكات العصبية هي مقربات دوال شاملة [14]، وجدنا أن جعل الشبكة F_Θ تعمل مباشرة على إحداثيات مدخلة xyzθφ ينتج عنه عمليات تصيير ذات أداء ضعيف في تمثيل التباين عالي التردد في اللون والهندسة. هذا يتوافق مع العمل الحديث بواسطة Rahaman وآخرين [35]، الذي يوضح أن الشبكات العميقة منحازة نحو تعلم دوال التردد المنخفض. كما يوضحون أن تعيين المدخلات إلى فضاء ذي أبعاد أعلى باستخدام دوال عالية التردد قبل تمريرها إلى الشبكة يمكّن من ملاءمة أفضل للبيانات التي تحتوي على تباين عالي التردد.

نستفيد من هذه النتائج في سياق تمثيلات المشاهد العصبية، ونوضح أن إعادة صياغة F_Θ كتركيب دالتين F_Θ = F'_Θ ◦ γ، واحدة متعلمة والأخرى ليست كذلك، يحسن الأداء بشكل كبير (انظر الشكل 4 والجدول 2). هنا γ هو تعيين من ℝ إلى فضاء ذي أبعاد أعلى ℝ^(2L)، و F'_Θ لا تزال ببساطة MLP عادية. رسمياً، دالة الترميز التي نستخدمها هي:

$$\gamma(p) = \left(\sin(2^0\pi p), \cos(2^0\pi p), \cdots, \sin(2^{L-1}\pi p), \cos(2^{L-1}\pi p)\right).$$

يتم تطبيق هذه الدالة γ(·) بشكل منفصل على كل من قيم الإحداثيات الثلاث في **x** (والتي يتم تطبيعها لتقع في [−1, 1]) وعلى المكونات الثلاثة لمتجه وحدة اتجاه المشاهدة الديكارتي **d** (والتي تقع بالإنشاء في [−1, 1]). في تجاربنا، نضع L = 10 لـ γ(**x**) و L = 4 لـ γ(**d**).

يُستخدم تعيين مماثل في معمارية Transformer الشائعة [47]، حيث يُشار إليه باسم ترميز موضعي. ومع ذلك، تستخدمه Transformers لهدف مختلف وهو توفير المواضع المتقطعة للرموز في تسلسل كمدخل لمعمارية لا تحتوي على أي مفهوم للترتيب. في المقابل، نستخدم هذه الدوال لتعيين الإحداثيات المدخلة المستمرة إلى فضاء ذي أبعاد أعلى لتمكين MLP الخاص بنا من تقريب دالة تردد أعلى بسهولة أكبر. يستخدم العمل المتزامن على مشكلة ذات صلة بنمذجة بنية البروتين ثلاثية الأبعاد من الإسقاطات [51] أيضاً تعيين إحداثيات مدخلة مماثل.

## 5.2 أخذ عينات الحجم الهرمي

استراتيجية التصيير الخاصة بنا لتقييم شبكة حقل الإشعاع العصبي بكثافة عند N نقطة استعلام على طول كل شعاع كاميرا غير فعالة: الفضاء الحر والمناطق المحجوبة التي لا تساهم في الصورة المصيّرة لا تزال تُعيّن بشكل متكرر. نستلهم من العمل المبكر في تصيير الحجم [20] ونقترح تمثيلاً هرمياً يزيد من كفاءة التصيير من خلال تخصيص العينات بما يتناسب مع تأثيرها المتوقع على التصيير النهائي.

بدلاً من استخدام شبكة واحدة فقط لتمثيل المشهد، نحسّن شبكتين في وقت واحد: واحدة "خشنة" وواحدة "دقيقة". نأخذ أولاً عينة من مجموعة من N_c مواقع باستخدام أخذ العينات الطبقي، ونقيّم الشبكة "الخشنة" عند هذه المواقع كما هو موضح في المعادلات 2 و3. بالنظر إلى مخرجات هذه الشبكة "الخشنة"، ننتج بعد ذلك أخذ عينات أكثر استنارة من النقاط على طول كل شعاع حيث تكون العينات منحازة نحو الأجزاء ذات الصلة من الحجم. للقيام بذلك، نعيد أولاً كتابة اللون المركب ألفا من الشبكة الخشنة $\hat{C}_c(\mathbf{r})$ في المعادلة 3 كمجموع موزون لجميع الألوان المعيّنة **c**_i على طول الشعاع:

$$\hat{C}_c(\mathbf{r}) = \sum_{i=1}^{N_c} w_i\mathbf{c}_i, \quad w_i = T_i(1 - \exp(-\sigma_i\delta_i)).$$

تطبيع هذه الأوزان كـ $\hat{w}_i = w_i/\sum_{j=1}^{N_c} w_j$ ينتج دالة كثافة احتمالية ثابتة متعددة القطع على طول الشعاع. نأخذ عينة من مجموعة ثانية من N_f مواقع من هذا التوزيع باستخدام أخذ عينات التحويل العكسي، ونقيّم شبكتنا "الدقيقة" عند اتحاد المجموعتين الأولى والثانية من العينات، ونحسب اللون المصيّر النهائي للشعاع $\hat{C}_f(\mathbf{r})$ باستخدام المعادلة 3 ولكن باستخدام جميع عينات N_c+N_f. يخصص هذا الإجراء المزيد من العينات للمناطق التي نتوقع أن تحتوي على محتوى مرئي. يتناول هذا هدفاً مشابهاً لأخذ عينات الأهمية، ولكننا نستخدم القيم المعيّنة كتقطيع غير منتظم لمجال التكامل بالكامل بدلاً من معاملة كل عينة كتقدير احتمالي مستقل للتكامل بالكامل.

## 5.3 تفاصيل التنفيذ

نحسّن شبكة تمثيل حجم مستمر عصبية منفصلة لكل مشهد. يتطلب ذلك فقط مجموعة بيانات من صور RGB ملتقطة للمشهد، ومواضع الكاميرا المقابلة والمعاملات الداخلية، وحدود المشهد (نستخدم مواضع الكاميرا الحقيقية والمعاملات الداخلية والحدود للبيانات الاصطناعية، ونستخدم حزمة COLMAP للبنية من الحركة [39] لتقدير هذه المعاملات للبيانات الحقيقية). في كل تكرار تحسين، نأخذ عينة عشوائية من دفعة من أشعة الكاميرا من مجموعة جميع البكسلات في مجموعة البيانات، ثم نتبع أخذ العينات الهرمي الموصوف في القسم 5.2 للاستعلام عن N_c عينات من الشبكة الخشنة و N_c + N_f عينات من الشبكة الدقيقة. ثم نستخدم إجراء تصيير الحجم الموصوف في القسم 4 لتصيير لون كل شعاع من كلتا مجموعتي العينات. خسارتنا هي ببساطة إجمالي الخطأ التربيعي بين الألوان المصيّرة والحقيقية للبكسلات لكل من التصييرات الخشنة والدقيقة:

$$\mathcal{L} = \sum_{\mathbf{r}\in\mathcal{R}} \left[\left\|\hat{C}_c(\mathbf{r}) - C(\mathbf{r})\right\|_2^2 + \left\|\hat{C}_f(\mathbf{r}) - C(\mathbf{r})\right\|_2^2\right]$$

حيث ℝ هي مجموعة الأشعة في كل دفعة، و C(**r**)، و $\hat{C}_c(\mathbf{r})$، و $\hat{C}_f(\mathbf{r})$ هي ألوان RGB الحقيقية والمتنبأ بها من الحجم الخشن والمتنبأ بها من الحجم الدقيق للشعاع **r** على التوالي. لاحظ أنه على الرغم من أن التصيير النهائي يأتي من $\hat{C}_f(\mathbf{r})$، إلا أننا نقلل أيضاً خسارة $\hat{C}_c(\mathbf{r})$ بحيث يمكن استخدام توزيع الأوزان من الشبكة الخشنة لتخصيص العينات في الشبكة الدقيقة.

في تجاربنا، نستخدم حجم دفعة قدره 4096 شعاعاً، كل منها معيّن عند N_c = 64 إحداثياً في الحجم الخشن و N_f = 128 إحداثياً إضافياً في الحجم الدقيق. نستخدم محسّن Adam [18] بمعدل تعلم يبدأ عند 5 × 10^(−4) ويتناقص أسياً إلى 5 × 10^(−5) على مدار التحسين (تُترك معاملات Adam الأخرى عند القيم الافتراضية β_1 = 0.9، β_2 = 0.999، و ε = 10^(−7)). يستغرق التحسين لمشهد واحد عادةً حوالي 100-300 ألف تكرار للتقارب على وحدة معالجة رسومات NVIDIA V100 واحدة (حوالي 1-2 يوم).

---

### Translation Notes

- **Figures referenced:** Figure 4, Table 2
- **Key terms introduced:** universal function approximator (مقرب دوال شامل), spectral bias (انحياز طيفي), piecewise-constant PDF (دالة كثافة احتمالية ثابتة متعددة القطع), inverse transform sampling (أخذ عينات التحويل العكسي), structure-from-motion (البنية من الحركة), ground truth (حقيقة أرضية)
- **Equations:** Equations 4, 5, 6 from paper
- **Citations:** [14], [18], [20], [35], [39], [47], [51]
- **Special handling:** Complex mathematical formulations, hyperparameters preserved

### Quality Metrics

- Semantic equivalence: 0.88 - Excellent preservation of optimization details
- Technical accuracy: 0.87 - Accurate translation of ML/optimization terminology
- Readability: 0.85 - Clear despite technical complexity
- Glossary consistency: 0.84 - Consistent use of established terms
- **Overall section score:** 0.86
