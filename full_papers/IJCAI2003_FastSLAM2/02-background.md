# Section 2-3: Simultaneous Localization and Mapping & FastSLAM
## القسم 2-3: التوطين والرسم الخرائطي المتزامن و FastSLAM

**Section:** background
**Translation Quality:** 0.87
**Glossary Terms Used:** SLAM, posterior distribution, landmarks, pose, motion model, measurement model, Gaussian noise, particle filter, EKF, data association, importance factor, resampling

---

### English Version

## 2 Simultaneous Localization and Mapping

SLAM addresses the problem of simultaneously recovering a map and a vehicle pose from sensor data. The map contains N features (landmarks) and shall be denoted m = {m₁, m₂, ..., mₙ}. The path of the vehicle will be denoted s₁:ₜ = {s₁, s₂, ..., sₜ}, where t is a time index and sₜ is the pose of the vehicle at time t.

Most state-of-the-art SLAM algorithms calculate (or approximate) variants of the following posterior distribution:

p(s₁:ₜ, m | z₁:ₜ, u₀:ₜ, n₁:ₜ)     (1)

where z₁:ₜ = {z₁, z₂, ..., zₜ} is a sequence of measurements (e.g., range and bearing to nearby landmarks), and u₀:ₜ = {u₀, u₁, ..., uₜ} is a sequence of robot controls (e.g., velocities for robot wheels). (As usual, we assume without loss of generality that only a single landmark is observed at each time t.) The variables n₁:ₜ = {n₁, n₂, ..., nₜ} are data association variables — each nₜ specifies the identity of the landmark observed at time t. Initially, we assume n₁:ₜ is known; we relax this assumption below.

To calculate the posterior (1), the vehicle is given a probabilistic motion model, in the form of the conditional probability distribution p(sₜ | sₜ₋₁, uₜ). This distribution describes how a control uₜ asserted in the time interval [t-1, t] affects the resulting pose. Additionally, the vehicle is given a probabilistic measurement model, denoted p(zₜ | sₜ, m, nₜ), describing how measurements evolve from state. In accordance to the rich SLAM literature, we will model both models by nonlinear functions with independent Gaussian noise:

sₜ = g(sₜ₋₁, uₜ) + εₜ     (2)
zₜ = h(sₜ, mₙₜ) + δₜ     (3)

Here g and h are nonlinear functions, and εₜ and δₜ are Gaussian noise variables with covariance Σₑ and Σδ, respectively.

## 3 FastSLAM

FastSLAM [15] is based on the important observation [17] that the posterior can be factored:

p(s₁:ₜ, m | z₁:ₜ, u₀:ₜ, n₁:ₜ) = p(s₁:ₜ | z₁:ₜ, u₀:ₜ, n₁:ₜ) ∏ₙ p(mₙ | s₁:ₜ, z₁:ₜ, n₁:ₜ)     (4)

This factorization is exact and universal in SLAM problems. It states that if one (hypothetically) knew the path of the vehicle, the landmark positions could be estimated independently of each other (hence the product over n). In practice, of course, one does not know the vehicle's path. Nevertheless, the independence makes it possible to factor the posterior into a term that estimates the probability of each path, and N terms that estimate the position of the landmarks, conditioned on each (hypothetical) path.

FastSLAM samples the path using a particle filter. Each particle has attached its own map, consisting of N extended Kalman filters. Formally, the m-th particle Yₜ[m] contains a path s₁:ₜ[m] along with N Gaussian landmark estimates, described by the mean μₙ,ₜ[m] and covariance Σₙ,ₜ[m]:

Yₜ[m] = {s₁:ₜ[m], μ₁,ₜ[m], Σ₁,ₜ[m], ..., μₙ,ₜ[m], Σₙ,ₜ[m]}     (5)

We briefly review the key equations of the regular FastSLAM algorithm, and refer the reader to [15]. Each update in FastSLAM begins with sampling new poses based on the most recent motion command uₜ:

sₜ[m] ~ p(sₜ | sₜ₋₁[m], uₜ)     (6)

Note that this proposal distribution only uses the motion command uₜ, but ignores the measurement zₜ.

Next, FastSLAM updates the estimate of the observed landmark mₙₜ according to the following posterior. This posterior takes the measurement zₜ into consideration:

p(mₙₜ | sₜ[m], Yₜ₋₁[m], zₜ) = η p(zₜ | sₜ[m], mₙₜ) p(mₙₜ | sₜ[m], Yₜ₋₁[m])     (7)

Here η is a constant. This posterior is the normalized product of two Gaussians as indicated. However, if h is non-linear, the product will not be Gaussian in general. To make the result Gaussian, FastSLAM employs the standard EKF "trick" [13]: h is approximated by a linear function (see below). Under this approximation, (7) is equivalent to the measurement update equation familiar from the EKF literature [13].

In a final step, FastSLAM corrects for the fact that the pose sample sₜ[m] has been generated without consideration of the most recent measurement. It does so by resampling the particles [20]. The probability for the m-th particle to be sampled (with replacement) is given by the following variable, commonly referred to as importance factor:

wₜ[m] = p(zₜ | sₜ[m], Yₜ₋₁[m])     (8)

As shown in [15], the resampling operation can be implemented in O(M log N) time using trees, where M is the number of samples and N the number of landmarks in the map. However, the number of particles M needed for convergence remains an open question.

FastSLAM has been extended to SLAM with unknown data associations [14]. If the data association is unknown, each particle m in FastSLAM makes its own local data association decision nₜ[m] by maximizing the measurement likelihood. The formula for finding the most likely data association maximizes the resulting importance weight:

nₜ[m] = arg maxₙ wₜ[m, n]     (8)

Here wₜ[m, n] makes the dependence of the factor wₜ[m] on the variable nₜ explicit. A key characteristic of FastSLAM is that each particle makes its own local data association. In contrast, EKF techniques must commit to a single data association hypothesis for the entire filter. Results in [14] show empirically that this difference renders FastSLAM significantly more robust to noise than EKF-style algorithms.

---

### النسخة العربية

## 2 التوطين والرسم الخرائطي المتزامن

يعالج SLAM مسألة استرجاع خريطة ووضعية المركبة من بيانات المستشعر في وقت واحد. تحتوي الخريطة على N من الخصائص (المعالم) ويُرمز لها بـ m = {m₁, m₂, ..., mₙ}. سيُرمز لمسار المركبة بـ s₁:ₜ = {s₁, s₂, ..., sₜ}، حيث t هو مؤشر الوقت و sₜ هي وضعية المركبة في الوقت t.

تحسب معظم خوارزميات SLAM المتطورة (أو تقرب) متغيرات التوزيع البعدي التالي:

p(s₁:ₜ, m | z₁:ₜ, u₀:ₜ, n₁:ₜ)     (1)

حيث z₁:ₜ = {z₁, z₂, ..., zₜ} هو تسلسل القياسات (على سبيل المثال، المدى والاتجاه إلى المعالم القريبة)، و u₀:ₜ = {u₀, u₁, ..., uₜ} هو تسلسل أوامر التحكم في الروبوت (على سبيل المثال، السرعات لعجلات الروبوت). (كالمعتاد، نفترض دون فقدان العمومية أن معلماً واحداً فقط يُلاحظ في كل وقت t.) المتغيرات n₁:ₜ = {n₁, n₂, ..., nₜ} هي متغيرات ربط البيانات — كل nₜ يحدد هوية المعلم الذي لوحظ في الوقت t. في البداية، نفترض أن n₁:ₜ معروف؛ نخفف هذا الافتراض أدناه.

لحساب البعدي (1)، تُعطى المركبة نموذج حركة احتمالي، في شكل توزيع احتمالي شرطي p(sₜ | sₜ₋₁, uₜ). يصف هذا التوزيع كيف يؤثر أمر التحكم uₜ المطبق في الفترة الزمنية [t-1, t] على الوضعية الناتجة. بالإضافة إلى ذلك، تُعطى المركبة نموذج قياس احتمالي، يُرمز له بـ p(zₜ | sₜ, m, nₜ)، يصف كيف تتطور القياسات من الحالة. وفقاً لأدبيات SLAM الغنية، سنمثل كلا النموذجين بدوال غير خطية مع ضوضاء غاوسية مستقلة:

sₜ = g(sₜ₋₁, uₜ) + εₜ     (2)
zₜ = h(sₜ, mₙₜ) + δₜ     (3)

هنا g و h دوال غير خطية، و εₜ و δₜ متغيرات ضوضاء غاوسية مع تباين مشترك Σₑ و Σδ، على التوالي.

## 3 FastSLAM

تستند FastSLAM [15] إلى الملاحظة المهمة [17] بأن البعدي يمكن تحليله إلى عوامل:

p(s₁:ₜ, m | z₁:ₜ, u₀:ₜ, n₁:ₜ) = p(s₁:ₜ | z₁:ₜ, u₀:ₜ, n₁:ₜ) ∏ₙ p(mₙ | s₁:ₜ, z₁:ₜ, n₁:ₜ)     (4)

هذا التحليل العاملي دقيق وشامل في مسائل SLAM. إنه ينص على أنه إذا كان أحدهم (افتراضياً) يعرف مسار المركبة، فيمكن تقدير مواقع المعالم بشكل مستقل عن بعضها البعض (ومن ثم الضرب على n). في الممارسة، بالطبع، لا يعرف المرء مسار المركبة. ومع ذلك، فإن الاستقلالية تجعل من الممكن تحليل البعدي إلى حد يقدر احتمالية كل مسار، و N من الحدود التي تقدر موقع المعالم، مشروطة بكل مسار (افتراضي).

تأخذ FastSLAM عينات من المسار باستخدام مرشح جسيمات. لكل جسيمة خريطتها الخاصة الملحقة، تتكون من N من مرشحات كالمان الممتدة. رسمياً، تحتوي الجسيمة m-th على Yₜ[m] مسار s₁:ₜ[m] مع N من تقديرات المعالم الغاوسية، الموصوفة بالمتوسط μₙ,ₜ[m] والتباين المشترك Σₙ,ₜ[m]:

Yₜ[m] = {s₁:ₜ[m], μ₁,ₜ[m], Σ₁,ₜ[m], ..., μₙ,ₜ[m], Σₙ,ₜ[m]}     (5)

نراجع بإيجاز المعادلات الرئيسية لخوارزمية FastSLAM العادية، ونحيل القارئ إلى [15]. يبدأ كل تحديث في FastSLAM بأخذ عينات من الوضعيات الجديدة بناءً على أمر الحركة الأحدث uₜ:

sₜ[m] ~ p(sₜ | sₜ₋₁[m], uₜ)     (6)

لاحظ أن توزيع الاقتراح هذا يستخدم فقط أمر الحركة uₜ، لكنه يتجاهل القياس zₜ.

بعد ذلك، تقوم FastSLAM بتحديث تقدير المعلم الملاحظ mₙₜ وفقاً للبعدي التالي. يأخذ هذا البعدي القياس zₜ في الاعتبار:

p(mₙₜ | sₜ[m], Yₜ₋₁[m], zₜ) = η p(zₜ | sₜ[m], mₙₜ) p(mₙₜ | sₜ[m], Yₜ₋₁[m])     (7)

هنا η ثابت. هذا البعدي هو الضرب المعياري لاثنين من الغاوسيات كما هو موضح. ومع ذلك، إذا كانت h غير خطية، فإن الضرب لن يكون غاوسياً بشكل عام. لجعل النتيجة غاوسية، تستخدم FastSLAM "الحيلة" القياسية لمرشح كالمان الممتد [13]: يتم تقريب h بدالة خطية (انظر أدناه). تحت هذا التقريب، (7) مكافئ لمعادلة تحديث القياس المألوفة من أدبيات مرشح كالمان الممتد [13].

في الخطوة الأخيرة، تصحح FastSLAM حقيقة أن عينة الوضعية sₜ[m] قد تم توليدها دون النظر في القياس الأحدث. إنها تفعل ذلك عن طريق إعادة أخذ العينات من الجسيمات [20]. يُعطى احتمال أخذ عينة من الجسيمة m-th (مع الاستبدال) بالمتغير التالي، المشار إليه عادةً باسم عامل الأهمية:

wₜ[m] = p(zₜ | sₜ[m], Yₜ₋₁[m])     (8)

كما هو موضح في [15]، يمكن تنفيذ عملية إعادة أخذ العينات في وقت O(M log N) باستخدام الأشجار، حيث M هو عدد العينات و N عدد المعالم في الخريطة. ومع ذلك، يظل عدد الجسيمات M اللازمة للتقارب سؤالاً مفتوحاً.

تم توسيع FastSLAM إلى SLAM مع ربطات بيانات غير معروفة [14]. إذا كان ربط البيانات غير معروف، فإن كل جسيمة m في FastSLAM تتخذ قرار ربط البيانات المحلي الخاص بها nₜ[m] من خلال تعظيم احتمالية القياس. تعظم صيغة إيجاد ربط البيانات الأكثر احتمالاً وزن الأهمية الناتج:

nₜ[m] = arg maxₙ wₜ[m, n]     (8)

هنا wₜ[m, n] يجعل اعتماد العامل wₜ[m] على المتغير nₜ صريحاً. خاصية رئيسية لـ FastSLAM هي أن كل جسيمة تتخذ قرار ربط البيانات المحلي الخاص بها. في المقابل، يجب أن تلتزم تقنيات مرشح كالمان الممتد بفرضية ربط بيانات واحدة للمرشح بأكمله. تُظهر النتائج في [14] تجريبياً أن هذا الاختلاف يجعل FastSLAM أكثر متانة بشكل كبير للضوضاء من خوارزميات نمط مرشح كالمان الممتد.

---

### Translation Notes

- **Equations:** 8 numbered equations (1-8)
- **Key terms introduced:** posterior distribution, factorization, importance factor, resampling, conditional independence
- **Citations:** [15], [17], [13], [20], [14]
- **Special handling:**
  - Mathematical notation preserved exactly (subscripts, superscripts, Greek letters)
  - Probability distributions p(...) kept in original notation
  - O(M log N) complexity notation preserved
  - Product symbol ∏ preserved

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-Translation Validation (Key Technical Paragraph)

**Original Key Paragraph:**
FastSLAM samples the path using a particle filter. Each particle has attached its own map, consisting of N extended Kalman filters. Formally, the m-th particle contains a path along with N Gaussian landmark estimates, described by the mean and covariance.

**Back-Translation:**
FastSLAM takes samples from the path using a particle filter. Each particle has its own attached map, consisting of N extended Kalman filters. Formally, the m-th particle contains a path with N Gaussian landmark estimates, described by the mean and covariance.
