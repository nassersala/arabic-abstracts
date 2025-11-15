# Section 2: Differential Privacy and Its Flavors
## القسم 2: الخصوصية التفاضلية وأشكالها المتنوعة

**Section:** background
**Translation Quality:** 0.87
**Glossary Terms Used:** differential privacy, mechanism, composition, privacy loss, Gaussian mechanism, Laplace mechanism, sensitivity, adjacent inputs

---

### English Version

## ε-DIFFERENTIAL PRIVACY [1]

We first recall the standard definition of ε-differential privacy.

**Definition 1 (ε-DP).** A randomized mechanism $f : \mathcal{D} \mapsto \mathcal{R}$ satisfies ε-differential privacy (ε-DP) if for any adjacent $D, D' \in \mathcal{D}$ and $S \subset \mathcal{R}$

$$\Pr[f(D) \in S] \leq e^{\varepsilon} \Pr[f(D') \in S].$$

The above definition is contingent on the notion of adjacent inputs $D$ and $D'$, which is domain-specific and is typically chosen to capture the contribution to the mechanism's input by a single individual.

The Laplace mechanism is a prototypical ε-differentially private algorithm, allowing release of an approximate (noisy) answer to an arbitrary query with values in $\mathbb{R}^n$. The mechanism is defined as

$$\mathcal{L}_{\varepsilon} f(x) \triangleq f(x) + \Lambda(0, \Delta_1 f/\varepsilon),$$

where $\Lambda$ is the Laplace distribution and $\ell_1$-sensitivity of the query $f$ is

$$\Delta_1 f \triangleq \max_{D,D'} \|f(D) - f(D')\|_1$$

taken over all adjacent inputs $D$ and $D'$.

The basic composition theorem states that if $f$ and $g$ are, respectively, $\varepsilon_1$- and $\varepsilon_2$-DP, then the simultaneous release of $f(D)$ and $g(D)$ satisfies $(\varepsilon_1 + \varepsilon_2)$-DP. Moreover, the mechanism $g$ may be selected adaptively, after seeing the output of $f(D)$.

## (ε, δ)-DIFFERENTIAL PRIVACY [2]

A relaxation of ε-differential privacy allows a δ additive term in its defining inequality:

**Definition 2 ((ε, δ)-DP).** A randomized mechanism $f : \mathcal{D} \mapsto \mathcal{R}$ offers (ε, δ)-differential privacy if for any adjacent $D, D' \in \mathcal{D}$ and $S \subset \mathcal{R}$

$$\Pr[f(D) \in S] \leq e^{\varepsilon} \Pr[f(D') \in S] + \delta.$$

The common interpretation of (ε, δ)-DP is that it is ε-DP "except with probability δ". Formalizing this statement runs into difficulties similar to the ones addressed by Mironov et al. [3] for a different (computational) relaxation. For any two adjacent inputs, $D_1$ and $D_2$, it is indeed possible to define an ε-DP mechanism that agrees with $f$ with all but δ probability. Extending this argument to domains of exponential sizes (for instance, to a boolean hypercube) cannot be done without diluting the guarantee exponentially [4]. We conclude that (ε, δ)-differential privacy is a qualitatively different definition than pure ε-DP (unless, of course, δ = 0, which we assume not to be the case through the rest of this section).

Even for the simple case of exactly two input databases (such as when the adversary knows the entire dataset except whether it contains a particular record), the δ additive term encompasses two very different modes in which privacy may fail. In both scenarios ε-DP holds with probability 1 − δ, they differ in what happens with the remaining probability δ. In the first scenario privacy degrades gracefully, such as to $\varepsilon_1$-DP with probability δ/2, to $\varepsilon_2$-DP with probability δ/4, etc. In the other scenario, with probability δ the secret—whether the record is part of the database or not—becomes completely exposed. The difference between the two failure modes can be quite stark. In the former, there is always some residual deniability; in the latter, the adversary occasionally learns the secret with certainty. Depending on the adversary's tolerance to false positives, plausible deniability may offer adequate protection, but a single (ε, δ)-DP privacy statement cannot differentiate between the two alternatives. For a lively parable of the different guarantees offered by the ε-DP and (ε, δ)-DP definitions see McSherry [5].

To avoid the worst-case scenario of always violating privacy of a δ fraction of the dataset, the standard recommendation is to choose $\delta \ll 1/N$ or even $\delta = \text{negl}(1/N)$, where $N$ is the number of contributors. This strategy forecloses possibility of one particularly devastating outcome, but other forms of information leakage remain.

The definition of (ε, δ)-differential privacy was initially proposed to capture privacy guarantees of the Gaussian mechanism, defined as follows:

$$\mathcal{G}_{\sigma} f(x) \triangleq f(x) + \mathcal{N}(0, \sigma^2).$$

Elementary analysis shows that the Gaussian mechanism cannot meet ε-DP for any ε. Instead, it satisfies a continuum of incomparable (ε, δ)-DP guarantees, for all combinations of $\varepsilon < 1$ and $\sigma > \sqrt{2\ln(1.25/\delta)}\Delta_2 f/\varepsilon$, where $f$'s $\ell_2$-sensitivity is defined as

$$\Delta_2 f \triangleq \max_{D,D'} \|f(D) - f(D')\|_2$$

taken over all adjacent inputs $D$ and $D'$.

There exist valid reasons for preferring the Gaussian mechanism over Laplace: the noise comes from the same Gaussian distribution (closed under addition) as the error that may already be present in the dataset; the standard deviation of the noise is proportional to the query's $\ell_2$ sensitivity, which is no larger and often much smaller than $\ell_1$; for the same standard deviation, the tails of the Gaussian (normal) distribution decay much faster than those of the Laplace (exponential) distribution. Unfortunately, distilling the guarantees of the Gaussian mechanism down to a single number or a small set of numbers using the language of (ε, δ)-DP always leaves a possibility of a complete privacy compromise that the mechanism itself may not allow.

Another common reason for bringing in (ε, δ)-differential privacy is application of advanced composition theorems. Consider the case of k-fold adaptive composition of an (ε, δ)-DP mechanism. For any $\delta' > 0$ it holds that the composite mechanism is $(\varepsilon', k\delta + \delta')$-DP, where $\varepsilon' \triangleq \sqrt{2k\ln(1/\delta')}\varepsilon + k\varepsilon(e^{\varepsilon} - 1)$ [6]. Note that, similarly to our discussion of the Gaussian mechanism, a single mechanism satisfies a continuum of incomparable (ε, δ)-DP guarantees.

Kairouz et al. give a procedure for computing an optimal k-fold composition of an (ε, δ)-DP mechanism [7]. Murtagh and Vadhan [8] demonstrate that generalizing this result to composition of heterogeneous mechanisms (i.e., satisfying $(ε_i, δ_i)$-DP for different $ε_i$'s) is #P-hard; they describe a PTAS for an approximate solution. None of these works tackles the problem of composing mechanisms that satisfy several (ε, δ)-DP guarantees simultaneously.

## (ZERO-)CONCENTRATED DIFFERENTIAL PRIVACY AND THE MOMENTS ACCOUNTANT

The closely related work by Dwork and Rothblum [9], followed by Bun and Steinke [10], explore privacy definitions—Concentrated Differential Privacy and zero-Concentrated Differential Privacy—that are framed using the language of, respectively, subgaussian tails and the Rényi divergence. The main difference between our approaches is that both Concentrated and zero-Concentrated DP require a linear bound on all positive moments of a privacy loss variable. In contrast, our definition applies to one moment at a time. Although less restrictive, it allows for more accurate numerical analyses.

The work by Abadi et al. [11] on differentially private stochastic gradient descent introduced the moments accountant as an internal tool for tracking privacy loss across multiple invocations of the Gaussian mechanism applied to random subsets of the input dataset. The paper's results are expressed via a necessarily lossy translation of the accountant's output (bounds on select moments of the privacy loss variable) to the language of (ε, δ)-differential privacy.

Taken together, the works on Concentrated DP, zero-Concentrated DP, and the moments accountant point towards adopting Rényi differential privacy as an effective and flexible mechanism for capturing privacy guarantees of a wide variety of algorithms and their combinations.

## OTHER RELAXATIONS

We briefly mention other relaxations and generalizations of differential privacy.

Under the indistinguishability-based Computational Differential Privacy (IND-CDP) definition [3], the test of closeness between distributions on adjacent inputs is computationally bounded (all other definitions considered in this paper hold against an unbounded, information-theoretic adversary). The IND-CDP notion allows much more accurate functionalities in the two-party setting [12]; in the traditional client-server setup there is a natural class of functionalities where the gap between IND-CDP and (ε, δ)-DP is minimal [13], and there are (contrived) examples where the computational relaxation permits tasks that are infeasible under information-theoretic definitions [14].

Several other works, most notably the Pufferfish and the coupled-worlds frameworks [15], [16], propose different stability constraints on the output distribution of privacy-preserving mechanisms. Although they differ in what distributions are compared, their notion of closeness is the same as in (ε, δ)-DP.

---

### النسخة العربية

## الخصوصية التفاضلية ε [1]

نستذكر أولاً التعريف القياسي للخصوصية التفاضلية ε.

**التعريف 1 (ε-DP).** تحقق آلية عشوائية $f : \mathcal{D} \mapsto \mathcal{R}$ الخصوصية التفاضلية ε (ε-DP) إذا كان لأي مدخلات متجاورة $D, D' \in \mathcal{D}$ وأي $S \subset \mathcal{R}$

$$\Pr[f(D) \in S] \leq e^{\varepsilon} \Pr[f(D') \in S].$$

يعتمد التعريف أعلاه على مفهوم المدخلات المتجاورة $D$ و$D'$، والذي يكون خاصًا بالمجال ويتم اختياره عادةً لالتقاط مساهمة فرد واحد في مدخل الآلية.

تعد آلية لابلاس خوارزمية نموذجية خاصة تفاضليًا من النوع ε، تسمح بإصدار إجابة تقريبية (مشوشة) لاستعلام عشوائي بقيم في $\mathbb{R}^n$. يتم تعريف الآلية على النحو التالي

$$\mathcal{L}_{\varepsilon} f(x) \triangleq f(x) + \Lambda(0, \Delta_1 f/\varepsilon),$$

حيث $\Lambda$ هو توزيع لابلاس وحساسية $\ell_1$ للاستعلام $f$ هي

$$\Delta_1 f \triangleq \max_{D,D'} \|f(D) - f(D')\|_1$$

مأخوذة على جميع المدخلات المتجاورة $D$ و$D'$.

تنص نظرية التركيب الأساسية على أنه إذا كانت $f$ و$g$ هما، على التوالي، $\varepsilon_1$-DP و$\varepsilon_2$-DP، فإن الإصدار المتزامن لـ $f(D)$ و$g(D)$ يحقق $(\varepsilon_1 + \varepsilon_2)$-DP. علاوة على ذلك، يمكن اختيار الآلية $g$ بشكل تكيفي، بعد رؤية مخرجات $f(D)$.

## الخصوصية التفاضلية (ε, δ) [2]

يسمح تخفيف الخصوصية التفاضلية ε بحد جمعي δ في معادلة تعريفها:

**التعريف 2 ((ε, δ)-DP).** تقدم آلية عشوائية $f : \mathcal{D} \mapsto \mathcal{R}$ خصوصية تفاضلية (ε, δ) إذا كان لأي مدخلات متجاورة $D, D' \in \mathcal{D}$ وأي $S \subset \mathcal{R}$

$$\Pr[f(D) \in S] \leq e^{\varepsilon} \Pr[f(D') \in S] + \delta.$$

التفسير الشائع لـ (ε, δ)-DP هو أنها ε-DP "باستثناء احتمالية δ". إن إضفاء الطابع الرسمي على هذا البيان يواجه صعوبات مماثلة لتلك التي عالجها Mironov وآخرون [3] لتخفيف (حسابي) مختلف. لأي مدخلين متجاورين، $D_1$ و$D_2$، من الممكن بالفعل تعريف آلية ε-DP تتفق مع $f$ باستثناء احتمالية δ. لا يمكن توسيع هذه الحجة إلى مجالات ذات أحجام أسية (على سبيل المثال، إلى مكعب فائق منطقي) دون إضعاف الضمان بشكل أسي [4]. نستنتج أن الخصوصية التفاضلية (ε, δ) هي تعريف مختلف نوعيًا عن ε-DP النقية (ما لم يكن، بالطبع، δ = 0، وهو ما نفترض أنه ليس الحال في بقية هذا القسم).

حتى بالنسبة للحالة البسيطة لقاعدتي بيانات مدخلة بالضبط (كما هو الحال عندما يعرف الخصم مجموعة البيانات بأكملها باستثناء ما إذا كانت تحتوي على سجل معين)، يشمل الحد الجمعي δ وضعين مختلفين جدًا يمكن أن تفشل فيهما الخصوصية. في كلا السيناريوهين تصمد ε-DP باحتمالية 1 − δ، ويختلفان فيما يحدث مع الاحتمالية المتبقية δ. في السيناريو الأول، تتدهور الخصوصية بلطف، مثل إلى $\varepsilon_1$-DP باحتمالية δ/2، إلى $\varepsilon_2$-DP باحتمالية δ/4، إلخ. في السيناريو الآخر، باحتمالية δ يصبح السر - ما إذا كان السجل جزءًا من قاعدة البيانات أم لا - مكشوفًا تمامًا. يمكن أن يكون الاختلاف بين وضعي الفشل صارخًا تمامًا. في السابق، يوجد دائمًا بعض القدرة المتبقية على الإنكار؛ في الأخير، يتعلم الخصم أحيانًا السر بيقين. اعتمادًا على تحمل الخصم للإيجابيات الكاذبة، قد يوفر الإنكار المعقول حماية كافية، لكن بيان خصوصية واحد (ε, δ)-DP لا يمكنه التمييز بين البديلين. للحصول على مثل حي للضمانات المختلفة التي تقدمها تعريفات ε-DP و(ε, δ)-DP، راجع McSherry [5].

لتجنب أسوأ سيناريو يتمثل في انتهاك الخصوصية دائمًا لجزء δ من مجموعة البيانات، فإن التوصية القياسية هي اختيار $\delta \ll 1/N$ أو حتى $\delta = \text{negl}(1/N)$، حيث $N$ هو عدد المساهمين. تمنع هذه الاستراتيجية إمكانية حدوث نتيجة واحدة مدمرة بشكل خاص، لكن أشكال أخرى من تسرب المعلومات تبقى.

تم اقتراح تعريف الخصوصية التفاضلية (ε, δ) في البداية لالتقاط ضمانات الخصوصية لآلية غاوس، المعرفة على النحو التالي:

$$\mathcal{G}_{\sigma} f(x) \triangleq f(x) + \mathcal{N}(0, \sigma^2).$$

يظهر التحليل الأساسي أن آلية غاوس لا يمكنها تحقيق ε-DP لأي ε. بدلاً من ذلك، تحقق سلسلة متصلة من ضمانات (ε, δ)-DP غير القابلة للمقارنة، لجميع مجموعات $\varepsilon < 1$ و$\sigma > \sqrt{2\ln(1.25/\delta)}\Delta_2 f/\varepsilon$، حيث يتم تعريف حساسية $\ell_2$ لـ $f$ على النحو التالي

$$\Delta_2 f \triangleq \max_{D,D'} \|f(D) - f(D')\|_2$$

مأخوذة على جميع المدخلات المتجاورة $D$ و$D'$.

توجد أسباب صحيحة لتفضيل آلية غاوس على لابلاس: الضوضاء تأتي من نفس التوزيع الغاوسي (المغلق تحت الجمع) مثل الخطأ الذي قد يكون موجودًا بالفعل في مجموعة البيانات؛ الانحراف المعياري للضوضاء يتناسب مع حساسية $\ell_2$ للاستعلام، والتي لا تكون أكبر وغالبًا ما تكون أصغر بكثير من $\ell_1$؛ لنفس الانحراف المعياري، تتلاشى ذيول التوزيع الغاوسي (الطبيعي) بشكل أسرع بكثير من تلك الخاصة بتوزيع لابلاس (الأسي). للأسف، فإن تقطير ضمانات آلية غاوس إلى رقم واحد أو مجموعة صغيرة من الأرقام باستخدام لغة (ε, δ)-DP يترك دائمًا احتمالية اختراق كامل للخصوصية قد لا تسمح به الآلية نفسها.

سبب شائع آخر لإدخال الخصوصية التفاضلية (ε, δ) هو تطبيق نظريات التركيب المتقدمة. ضع في اعتبارك حالة التركيب التكيفي k-fold لآلية (ε, δ)-DP. لأي $\delta' > 0$ فإنه يصح أن الآلية المركبة هي $(\varepsilon', k\delta + \delta')$-DP، حيث $\varepsilon' \triangleq \sqrt{2k\ln(1/\delta')}\varepsilon + k\varepsilon(e^{\varepsilon} - 1)$ [6]. لاحظ أنه، على غرار مناقشتنا لآلية غاوس، تحقق آلية واحدة سلسلة متصلة من ضمانات (ε, δ)-DP غير القابلة للمقارنة.

يعطي Kairouz وآخرون إجراءً لحساب التركيب الأمثل k-fold لآلية (ε, δ)-DP [7]. يوضح Murtagh وVadhan [8] أن تعميم هذه النتيجة على تركيب الآليات غير المتجانسة (أي التي تحقق $(ε_i, δ_i)$-DP لـ $ε_i$ مختلفة) هو #P-hard؛ ويصفان PTAS لحل تقريبي. لا يعالج أي من هذه الأعمال مشكلة تركيب الآليات التي تحقق عدة ضمانات (ε, δ)-DP في وقت واحد.

## الخصوصية التفاضلية المركزة (الصفرية) ومحاسب العزوم

يستكشف العمل ذو الصلة الوثيقة من قبل Dwork وRothblum [9]، متبوعًا بـ Bun وSteinke [10]، تعريفات الخصوصية - الخصوصية التفاضلية المركزة والخصوصية التفاضلية المركزة الصفرية - المؤطرة باستخدام لغة، على التوالي، الذيول شبه الغاوسية واختلاف ريني. الفرق الرئيسي بين نهجينا هو أن كلاً من DP المركزة وDP المركزة الصفرية تتطلب حدًا خطيًا على جميع العزوم الموجبة لمتغير خسارة الخصوصية. في المقابل، ينطبق تعريفنا على عزم واحد في كل مرة. على الرغم من أنه أقل تقييدًا، إلا أنه يسمح بتحليلات رقمية أكثر دقة.

قدم العمل من قبل Abadi وآخرين [11] حول الانحدار التدرجي العشوائي الخاص تفاضليًا محاسب العزوم كأداة داخلية لتتبع خسارة الخصوصية عبر استدعاءات متعددة لآلية غاوس المطبقة على مجموعات فرعية عشوائية من مجموعة البيانات المدخلة. يتم التعبير عن نتائج الورقة عبر ترجمة بالضرورة خاسرة لمخرجات المحاسب (حدود على عزوم مختارة من متغير خسارة الخصوصية) إلى لغة الخصوصية التفاضلية (ε, δ).

مجتمعة، تشير الأعمال حول DP المركزة، وDP المركزة الصفرية، ومحاسب العزوم نحو اعتماد الخصوصية التفاضلية لريني كآلية فعالة ومرنة لالتقاط ضمانات الخصوصية لمجموعة واسعة من الخوارزميات ومجموعاتها.

## تخفيفات أخرى

نذكر بإيجاز تخفيفات وتعميمات أخرى للخصوصية التفاضلية.

بموجب تعريف الخصوصية التفاضلية الحسابية القائمة على عدم القابلية للتمييز (IND-CDP) [3]، فإن اختبار القرب بين التوزيعات على المدخلات المتجاورة محدود حسابيًا (جميع التعريفات الأخرى التي تم النظر فيها في هذه الورقة تصمد ضد خصم غير محدود، نظري المعلومات). يسمح مفهوم IND-CDP بوظائف أكثر دقة بكثير في إعداد الطرفين [12]؛ في إعداد العميل-الخادم التقليدي، يوجد فئة طبيعية من الوظائف حيث تكون الفجوة بين IND-CDP و(ε, δ)-DP ضئيلة [13]، وهناك أمثلة (مفتعلة) حيث يسمح التخفيف الحسابي بمهام غير ممكنة بموجب التعريفات النظرية المعلوماتية [14].

تقترح العديد من الأعمال الأخرى، وأبرزها أطر Pufferfish والعوالم المقترنة [15]، [16]، قيود استقرار مختلفة على توزيع المخرجات لآليات الحفاظ على الخصوصية. على الرغم من أنها تختلف في التوزيعات التي تتم مقارنتها، فإن مفهوم القرب لديها هو نفسه كما في (ε, δ)-DP.

---

### Translation Notes

- **Key terms introduced:**
  - adjacent inputs (مدخلات متجاورة)
  - sensitivity (حساسية)
  - ℓ₁-sensitivity (حساسية $\ell_1$)
  - ℓ₂-sensitivity (حساسية $\ell_2$)
  - subgaussian tails (ذيول شبه غاوسية)
  - moments accountant (محاسب العزوم)
  - stochastic gradient descent (الانحدار التدرجي العشوائي)
  - plausible deniability (الإنكار المعقول)
  - Concentrated Differential Privacy (الخصوصية التفاضلية المركزة)
  - zero-Concentrated Differential Privacy (الخصوصية التفاضلية المركزة الصفرية)

- **Figures referenced:** None in this section
- **Equations:** Multiple mathematical definitions and equations
- **Citations:** [1]-[16]
- **Special handling:** Mathematical definitions require precise notation preservation

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
