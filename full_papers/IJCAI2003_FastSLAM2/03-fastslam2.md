# Section 4: FastSLAM 2.0
## القسم 4: FastSLAM 2.0

**Section:** methodology
**Translation Quality:** 0.86
**Glossary Terms Used:** algorithm, proposal distribution, sampling, pose, measurement, landmark, particle filter, linearization, Jacobian, covariance, Gaussian, importance weights, resampling, data association

---

### English Version

## 4 FastSLAM 2.0

Our new FastSLAM algorithm is based on an obvious inefficiency arising from the proposal distribution of regular FastSLAM. In regular FastSLAM, the pose sₜ[m] is sampled in accordance to the prediction arising from the motion command uₜ as specified in (6). It does not consider the measurement zₜ acquired at time t; instead, the measurement is incorporated through resampling. This approach is particularly troublesome if the noise in the vehicle motion is large relative to the measurement noise. In such situations, sampled poses will mostly fall into areas of low measurement likelihood, and will subsequently be terminated in the resampling phase with high probability. Unfortunately, many real-world robot systems are characterized by relatively high motion noise. As illustrated in the experimental results section of this paper, the waste incurred by this inefficient sampling scheme can be significant.

### 4.1 Sampling The Pose

FastSLAM 2.0 implements a single new idea: Poses are sampled under consideration of both the motion uₜ and the measurement zₜ. This is formally denoted by the following sampling distribution, which now takes the measurement zₜ into consideration:

sₜ[m] ~ p(sₜ | sₜ₋₁[m], uₜ, zₜ, Yₜ₋₁[m], nₜ)     (9)

In comparison to (6), incorporating the measurement zₜ only makes sense if we incorporate our current estimate of the observed landmark—obtained from the variables μₙₜ,ₜ₋₁[m] and Σₙₜ,ₜ₋₁[m] (which are included of the conditioning variables above). So in essence, the difference to FastSLAM is that the measurement zₜ is incorporated. However, this change has important ramifications.

The proposal distribution (9) can be reformulated as follows:

p(sₜ | sₜ₋₁[m], uₜ, zₜ, Yₜ₋₁[m], nₜ)
∝ p(zₜ | sₜ, Yₜ₋₁[m], nₜ) p(sₜ | sₜ₋₁[m], uₜ)     (10)

That is, the proposal distribution is the product of two factors: the familiar next state distribution p(sₜ | sₜ₋₁[m], uₜ) and the probability of the measurement p(zₜ | sₜ, Yₜ₋₁[m], nₜ). Calculating the latter involves an integration over possible landmark locations mₙₜ.

Unfortunately, sampling directly from this distribution is impossible in the general case; it does not even possess a closed form. Luckily, a closed form solution can be attained if g is approximated by a linear function (h may remain non-linear!):

g(sₜ₋₁, uₜ) ≈ g(s̄ₜ, uₜ) + Gₜ(sₜ₋₁ - s̄ₜ)

where s̄ₜ denotes the predicted robot pose, s̄ₜ = g(sₜ₋₁[m], uₜ), ẑₜ denotes the predicted measurement, ẑₜ = h(s̄ₜ, μ̄ₙₜ,ₜ₋₁[m]), and μ̄ₙₜ,ₜ₋₁[m] the predicted landmark location. The matrices Gₜ and Hₜ are the Jacobians (first derivatives) of g and h with respect to sₜ and s, respectively:

Gₜ = ∂g(sₜ₋₁, uₜ)/∂sₜ₋₁ |sₜ₋₁=s̄ₜ     (11)

Hₜ = ∂h(sₜ, mₙₜ)/∂sₜ |sₜ=s̄ₜ,mₙₜ=μ̄ₙₜ,ₜ₋₁[m]     (12)

Under this EKF-style approximation, the proposal distribution (9) is Gaussian with the following parameters:

μ̂ₜ[m] = s̄ₜ + Kₜ(zₜ - ẑₜ)     (13)

Σ̂ₜ[m] = (I - KₜHₜ)Σ̄ₜ     (14)

where

Kₜ = Σ̄ₜHₜᵀ(HₜΣ̄ₜHₜᵀ + Σδ)⁻¹     (15)
Σ̄ₜ = GₜΣₜ₋₁[m]Gₜᵀ + Σₑ

### 4.2 Updating The Observed Landmark Estimate

The updating step remains the same as in FastSLAM (see (7)). As stated in the previous section, h is linearized to retain Gaussianity of the posterior. This leads to the following update equations, whose derivation is equivalent to that of the standard EKF measurement update [13]:

μₙₜ,ₜ[m] = μₙₜ,ₜ₋₁[m] + Lₜ(zₜ - h(sₜ[m], μₙₜ,ₜ₋₁[m]))     (16)

Σₙₜ,ₜ[m] = (I - LₜH̄ₜ)Σₙₜ,ₜ₋₁[m]     (17)

where

Lₜ = Σₙₜ,ₜ₋₁[m]H̄ₜᵀ(H̄ₜΣₙₜ,ₜ₋₁[m]H̄ₜᵀ + Σδ)⁻¹     (18)

and H̄ₜ = ∂h(sₜ,mₙₜ)/∂mₙₜ |sₜ=sₜ[m],mₙₜ=μₙₜ,ₜ₋₁[m]

### 4.3 The Importance Weights

Resampling is necessary even in our new version of FastSLAM, since the particles generated do not yet match the desired posterior. The culprit is the normalizer η in (10), which may be different for different particles m. This normalizer is the inverse of the probability of the measurement under the m-th particle: p(zₜ | Yₜ₋₁[m], uₜ, nₜ). To account for this mismatch, our algorithm resamples in proportion to the following importance factor:

wₜ[m] = p(zₜ | Yₜ₋₁[m], uₜ, nₜ)     (18)

This expression can once again be approximated as a Gaussian by linearizing h. The mean of this Gaussian is ẑₜ and its covariance is:

Qₜ = HₜΣ̄ₜHₜᵀ + H̄ₜΣₙₜ,ₜ₋₁[m]H̄ₜᵀ + Σδ     (19)

### 4.4 Unknown Data Associations

The approach for handling data association is similar to the one in regular FastSLAM: Again, we select the data association that maximizes the probability of the measurement zₜ for the m-th particle:

nₜ[m] = arg maxₙ p(zₜ | Yₜ₋₁[m], uₜ, n)     (20)

At first glance, one may be tempted to substitute wₜ[m] for the probability on the right-hand side, as in regular FastSLAM. However, wₜ[m] does not consider the sampled pose sₜ[m], whereas the expression here does. This leads to a slightly different probability, which is calculated as follows:

p(zₜ | Yₜ₋₁[m], uₜ, n) = ∫ p(zₜ | sₜ, Yₜ₋₁[m], n) p(sₜ | sₜ₋₁[m], uₜ, zₜ, Yₜ₋₁[m], n) dsₜ     (21)

Linearization of g leads to a Gaussian over zₜ with mean ẑₜ(n) and covariance Qₜ(n). Both are functions of the data association variable n.

### 4.5 Feature Management

Finally, in cases with unknown data associations, features have to be created dynamically. As is common for SLAM algorithms [5], our approach creates new features when the measurement probability in (20) is below a threshold. However, real-world data with frequent outliers will generate spurious landmarks using this rule. Following [5], our approach removes such spurious landmarks by keeping track of their posterior probability of existence. Our mechanism analyzes measurement to the presence and absence of features. Observing a landmark provides positive evidence for its existence, whereas not observing it when mₙₜ falls within the robot's perceptual range provides negative evidence. The posterior probability of landmark existence is accumulated by the following Bayes filter, whose log-odds form is familiar from the literature on occupancy grid maps [16]:

log p(mₙ exists | ...) / (1 - p(mₙ exists | ...)) = log p(mₙ exists | ...) / (1 - p(mₙ exists | ...))ₜ₋₁ + log p(observed/not observed | mₙ exists)     (22)

Here [log p(mₙ exists | ...) / (1 - p(mₙ exists | ...))]ₜ₋₁ are the log-odds of the physical existence of landmark mₙ in map Yₜ₋₁[m], and p(observed/not observed | mₙ exists) is the probabilistic evidence provided by a measurement. Under appropriate definition of the latter, this rule provides for a simple evidence counting rule. If the log odds drops below a predefined threshold, the corresponding landmark is removed from the map. This mechanism enables particles to free themselves of spurious features.

---

### النسخة العربية

## 4 FastSLAM 2.0

تستند خوارزمية FastSLAM الجديدة الخاصة بنا إلى عدم كفاءة واضحة ناشئة عن توزيع الاقتراح في FastSLAM العادي. في FastSLAM العادي، يتم أخذ عينة من الوضعية sₜ[m] وفقاً للتنبؤ الناشئ عن أمر الحركة uₜ كما هو محدد في (6). إنه لا يأخذ في الاعتبار القياس zₜ المكتسب في الوقت t؛ بدلاً من ذلك، يتم دمج القياس من خلال إعادة أخذ العينات. يكون هذا النهج مزعجاً بشكل خاص إذا كانت الضوضاء في حركة المركبة كبيرة نسبياً إلى ضوضاء القياس. في مثل هذه الحالات، ستقع الوضعيات المأخوذة منها العينات في الغالب في مناطق ذات احتمالية قياس منخفضة، وسيتم إنهاؤها لاحقاً في مرحلة إعادة أخذ العينات باحتمالية عالية. لسوء الحظ، تتميز العديد من أنظمة الروبوتات في العالم الحقيقي بضوضاء حركة عالية نسبياً. كما هو موضح في قسم النتائج التجريبية من هذه الورقة، يمكن أن يكون الهدر الناتج عن مخطط أخذ العينات غير الفعال هذا كبيراً.

### 4.1 أخذ عينات الوضعية

تطبق FastSLAM 2.0 فكرة جديدة واحدة: يتم أخذ عينات الوضعيات مع الأخذ في الاعتبار كل من الحركة uₜ والقياس zₜ. يُرمز لهذا رسمياً بتوزيع أخذ العينات التالي، والذي يأخذ الآن القياس zₜ في الاعتبار:

sₜ[m] ~ p(sₜ | sₜ₋₁[m], uₜ, zₜ, Yₜ₋₁[m], nₜ)     (9)

بالمقارنة مع (6)، فإن دمج القياس zₜ لا معنى له إلا إذا قمنا بدمج تقديرنا الحالي للمعلم الملاحظ—الذي تم الحصول عليه من المتغيرات μₙₜ,ₜ₋₁[m] و Σₙₜ,ₜ₋₁[m] (والتي تُدرج ضمن المتغيرات الشرطية أعلاه). لذا في جوهره، الفرق عن FastSLAM هو أن القياس zₜ مدمج. ومع ذلك، فإن هذا التغيير له تداعيات مهمة.

يمكن إعادة صياغة توزيع الاقتراح (9) على النحو التالي:

p(sₜ | sₜ₋₁[m], uₜ, zₜ, Yₜ₋₁[m], nₜ)
∝ p(zₜ | sₜ, Yₜ₋₁[m], nₜ) p(sₜ | sₜ₋₁[m], uₜ)     (10)

أي أن توزيع الاقتراح هو حاصل ضرب عاملين: توزيع الحالة التالية المألوف p(sₜ | sₜ₋₁[m], uₜ) واحتمالية القياس p(zₜ | sₜ, Yₜ₋₁[m], nₜ). يتضمن حساب الأخير تكاملاً على مواقع المعالم المحتملة mₙₜ.

لسوء الحظ، فإن أخذ العينات مباشرة من هذا التوزيع مستحيل في الحالة العامة؛ فهو لا يمتلك حتى شكلاً مغلقاً. لحسن الحظ، يمكن الحصول على حل ذي شكل مغلق إذا تم تقريب g بدالة خطية (قد تظل h غير خطية!):

g(sₜ₋₁, uₜ) ≈ g(s̄ₜ, uₜ) + Gₜ(sₜ₋₁ - s̄ₜ)

حيث s̄ₜ تشير إلى وضعية الروبوت المتنبأ بها، s̄ₜ = g(sₜ₋₁[m], uₜ)، ẑₜ تشير إلى القياس المتنبأ به، ẑₜ = h(s̄ₜ, μ̄ₙₜ,ₜ₋₁[m])، و μ̄ₙₜ,ₜ₋₁[m] موقع المعلم المتنبأ به. المصفوفتان Gₜ و Hₜ هما اليعاقبة (المشتقات الأولى) لـ g و h بالنسبة إلى sₜ و s، على التوالي:

Gₜ = ∂g(sₜ₋₁, uₜ)/∂sₜ₋₁ |sₜ₋₁=s̄ₜ     (11)

Hₜ = ∂h(sₜ, mₙₜ)/∂sₜ |sₜ=s̄ₜ,mₙₜ=μ̄ₙₜ,ₜ₋₁[m]     (12)

تحت هذا التقريب بنمط مرشح كالمان الممتد، فإن توزيع الاقتراح (9) غاوسي مع المعاملات التالية:

μ̂ₜ[m] = s̄ₜ + Kₜ(zₜ - ẑₜ)     (13)

Σ̂ₜ[m] = (I - KₜHₜ)Σ̄ₜ     (14)

حيث

Kₜ = Σ̄ₜHₜᵀ(HₜΣ̄ₜHₜᵀ + Σδ)⁻¹     (15)
Σ̄ₜ = GₜΣₜ₋₁[m]Gₜᵀ + Σₑ

### 4.2 تحديث تقدير المعلم الملاحظ

تبقى خطوة التحديث كما هي في FastSLAM (انظر (7)). كما ذكر في القسم السابق، يتم تخطيط h للحفاظ على الغاوسية للبعدي. يؤدي هذا إلى معادلات التحديث التالية، التي اشتقاقها مكافئ لاشتقاق تحديث القياس القياسي لمرشح كالمان الممتد [13]:

μₙₜ,ₜ[m] = μₙₜ,ₜ₋₁[m] + Lₜ(zₜ - h(sₜ[m], μₙₜ,ₜ₋₁[m]))     (16)

Σₙₜ,ₜ[m] = (I - LₜH̄ₜ)Σₙₜ,ₜ₋₁[m]     (17)

حيث

Lₜ = Σₙₜ,ₜ₋₁[m]H̄ₜᵀ(H̄ₜΣₙₜ,ₜ₋₁[m]H̄ₜᵀ + Σδ)⁻¹     (18)

و H̄ₜ = ∂h(sₜ,mₙₜ)/∂mₙₜ |sₜ=sₜ[m],mₙₜ=μₙₜ,ₜ₋₁[m]

### 4.3 أوزان الأهمية

تعد إعادة أخذ العينات ضرورية حتى في نسختنا الجديدة من FastSLAM، نظراً لأن الجسيمات الناتجة لا تتطابق بعد مع البعدي المرغوب. الجاني هو المعيار η في (10)، والذي قد يكون مختلفاً لجسيمات m مختلفة. هذا المعيار هو معكوس احتمالية القياس تحت الجسيمة m-th: p(zₜ | Yₜ₋₁[m], uₜ, nₜ). لحساب عدم التطابق هذا، تعيد خوارزميتنا أخذ العينات بما يتناسب مع عامل الأهمية التالي:

wₜ[m] = p(zₜ | Yₜ₋₁[m], uₜ, nₜ)     (18)

يمكن مرة أخرى تقريب هذا التعبير كغاوسي بتخطيط h. متوسط هذا الغاوسي هو ẑₜ والتباين المشترك الخاص به هو:

Qₜ = HₜΣ̄ₜHₜᵀ + H̄ₜΣₙₜ,ₜ₋₁[m]H̄ₜᵀ + Σδ     (19)

### 4.4 ربطات البيانات غير المعروفة

النهج لمعالجة ربط البيانات مشابه للنهج المتبع في FastSLAM العادي: مرة أخرى، نختار ربط البيانات الذي يعظم احتمالية القياس zₜ للجسيمة m-th:

nₜ[m] = arg maxₙ p(zₜ | Yₜ₋₁[m], uₜ, n)     (20)

للوهلة الأولى، قد يميل المرء إلى استبدال wₜ[m] بالاحتمالية على الجانب الأيمن، كما في FastSLAM العادي. ومع ذلك، فإن wₜ[m] لا يأخذ في الاعتبار الوضعية المأخوذة منها العينة sₜ[m]، بينما التعبير هنا يفعل ذلك. يؤدي هذا إلى احتمالية مختلفة قليلاً، والتي يتم حسابها على النحو التالي:

p(zₜ | Yₜ₋₁[m], uₜ, n) = ∫ p(zₜ | sₜ, Yₜ₋₁[m], n) p(sₜ | sₜ₋₁[m], uₜ, zₜ, Yₜ₋₁[m], n) dsₜ     (21)

يؤدي التخطيط لـ g إلى غاوسي على zₜ مع متوسط ẑₜ(n) وتباين مشترك Qₜ(n). كلاهما دوال لمتغير ربط البيانات n.

### 4.5 إدارة الخصائص

أخيراً، في الحالات مع ربطات البيانات غير المعروفة، يجب إنشاء الخصائص ديناميكياً. كما هو شائع بالنسبة لخوارزميات SLAM [5]، ينشئ نهجنا خصائص جديدة عندما تكون احتمالية القياس في (20) أقل من عتبة. ومع ذلك، فإن بيانات العالم الحقيقي مع القيم الشاذة المتكررة ستولد معالم زائفة باستخدام هذه القاعدة. باتباع [5]، يزيل نهجنا مثل هذه المعالم الزائفة من خلال تتبع احتمالية وجودها البعدية. تحلل آليتنا القياس لوجود وغياب الخصائص. توفر ملاحظة المعلم دليلاً إيجابياً على وجوده، بينما عدم ملاحظته عندما يقع mₙₜ ضمن نطاق إدراك الروبوت يوفر دليلاً سلبياً. يتم تجميع الاحتمالية البعدية لوجود المعلم بواسطة مرشح بايز التالي، الذي شكله اللوغاريتمي-الاحتمالات مألوف من أدبيات خرائط شبكة الإشغال [16]:

log p(mₙ exists | ...) / (1 - p(mₙ exists | ...)) = log p(mₙ exists | ...) / (1 - p(mₙ exists | ...))ₜ₋₁ + log p(observed/not observed | mₙ exists)     (22)

هنا [log p(mₙ exists | ...) / (1 - p(mₙ exists | ...))]ₜ₋₁ هي الاحتمالات اللوغاريتمية للوجود الفيزيائي للمعلم mₙ في الخريطة Yₜ₋₁[m]، و p(observed/not observed | mₙ exists) هو الدليل الاحتمالي الذي يوفره القياس. تحت تعريف مناسب للأخير، توفر هذه القاعدة قاعدة عد أدلة بسيطة. إذا انخفضت الاحتمالات اللوغاريتمية إلى ما دون عتبة محددة مسبقاً، تتم إزالة المعلم المقابل من الخريطة. تمكّن هذه الآلية الجسيمات من تحرير نفسها من الخصائص الزائفة.

---

### Translation Notes

- **Equations:** 14 numbered equations (9-22)
- **Key terms introduced:** Jacobian, linearization, Kalman gain, log-odds, occupancy grid, feature management
- **Citations:** [13], [5], [16]
- **Special handling:**
  - Complex mathematical derivations preserved exactly
  - Matrix operations (transpose ᵀ, inverse ⁻¹) preserved
  - Subscripts and superscripts maintained
  - Integration symbol ∫ preserved
  - "log-odds" translated as "اللوغاريتمي-الاحتمالات"

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86

### Back-Translation Validation (Key Paragraph)

**Original:**
FastSLAM 2.0 implements a single new idea: Poses are sampled under consideration of both the motion and the measurement. This is formally denoted by the following sampling distribution, which now takes the measurement into consideration.

**Back-Translation:**
FastSLAM 2.0 implements a single new idea: Poses are sampled while taking into account both the motion and the measurement. This is formally denoted by the following sampling distribution, which now takes the measurement into consideration.
