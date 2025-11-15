# Section 6: Experiments
## القسم 6: التجارب

**Section:** Experimental Results
**Translation Quality:** 0.86
**Glossary Terms Used:** benchmark, experiment, hyperparameter, continuous control, neural network, optimization, policy gradient, baseline, normalized score, sample complexity, wall-time, robotics, locomotion

---

### English Version

## 6.1 Comparison of Surrogate Objectives

First, we compare several different surrogate objectives under different hyperparameters. Here, we compare the surrogate objective $L^{CLIP}$ to several natural variations and ablated versions.

**No clipping or penalty:** $L_t(\theta) = r_t(\theta)\hat{A}_t$

**Clipping:** $L_t(\theta) = \min(r_t(\theta)\hat{A}_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)\hat{A}_t)$

**KL penalty (fixed or adaptive):** $L_t(\theta) = r_t(\theta)\hat{A}_t - \beta \text{KL}[\pi_{\theta_\text{old}}, \pi_\theta]$

For the KL penalty, one can either use a fixed penalty coefficient $\beta$ or an adaptive coefficient as described in Section 4 using target KL value $d_\text{targ}$. Note that we also tried clipping in log space, but found the performance to be no better.

Because we are searching over hyperparameters for each algorithm variant, we chose a computationally cheap benchmark to test the algorithms on. Namely, we used 7 simulated robotics tasks² implemented in OpenAI Gym [Bro+16], which use the MuJoCo [TET12] physics engine. We do one million timesteps of training on each one. Besides the hyperparameters used for clipping ($\epsilon$) and the KL penalty ($\beta$, $d_\text{targ}$), which we search over, the other hyperparameters are provided in in Table 3.

To represent the policy, we used a fully-connected MLP with two hidden layers of 64 units, and tanh nonlinearities, outputting the mean of a Gaussian distribution, with variable standard deviations, following [Sch+15b; Dua+16]. We don't share parameters between the policy and value function (so coefficient $c_1$ is irrelevant), and we don't use an entropy bonus.

Each algorithm was run on all 7 environments, with 3 random seeds on each. We scored each run of the algorithm by computing the average total reward of the last 100 episodes. We shifted and scaled the scores for each environment so that the random policy gave a score of 0 and the best result was set to 1, and averaged over 21 runs to produce a single scalar for each algorithm setting.

The results are shown in Table 1. Note that the score is negative for the setting without clipping or penalties, because for one environment (half cheetah) it leads to a very negative score, which is worse than the initial random policy.

**Table 1:** Results from continuous control benchmark. Average normalized scores (over 21 runs of the algorithm, on 7 environments) for each algorithm / hyperparameter setting. $\beta$ was initialized at 1.

| algorithm | avg. normalized score |
|-----------|----------------------|
| No clipping or penalty | -0.39 |
| Clipping, $\epsilon = 0.1$ | 0.76 |
| **Clipping, $\epsilon = 0.2$** | **0.82** |
| Clipping, $\epsilon = 0.3$ | 0.70 |
| Adaptive KL $d_\text{targ} = 0.003$ | 0.68 |
| Adaptive KL $d_\text{targ} = 0.01$ | 0.74 |
| Adaptive KL $d_\text{targ} = 0.03$ | 0.71 |
| Fixed KL, $\beta = 0.3$ | 0.62 |
| Fixed KL, $\beta = 1.$ | 0.71 |
| Fixed KL, $\beta = 3.$ | 0.72 |
| Fixed KL, $\beta = 10.$ | 0.69 |

---

**Footnote:**

²HalfCheetah, Hopper, InvertedDoublePendulum, InvertedPendulum, Reacher, Swimmer, and Walker2d, all "-v1"

## 6.2 Comparison to Other Algorithms in the Continuous Domain

Next, we compare PPO (with the "clipped" surrogate objective from Section 3) to several other methods from the literature, which are considered to be effective for continuous problems. We compared against tuned implementations of the following algorithms: trust region policy optimization [Sch+15b], cross-entropy method (CEM) [SL06], vanilla policy gradient with adaptive stepsize³, A2C [Mni+16], A2C with trust region [Wan+16]. A2C stands for advantage actor critic, and is a synchronous version of A3C, which we found to have the same or better performance than the asynchronous version. For PPO, we used the hyperparameters from the previous section, with $\epsilon = 0.2$. We see that PPO outperforms the previous methods on almost all the continuous control environments.

**Figure 3:** Comparison of several algorithms on several MuJoCo environments, training for one million timesteps.

[Figure shows learning curves for HalfCheetah-v1, Hopper-v1, InvertedDoublePendulum-v1, InvertedPendulum-v1, Reacher-v1, Swimmer-v1, and Walker2d-v1, comparing A2C, A2C + Trust Region, CEM, PPO (Clip), Vanilla PG Adaptive, and TRPO]

---

**Footnote:**

³After each batch of data, the Adam stepsize is adjusted based on the KL divergence of the original and updated policy, using a rule similar to the one shown in Section 4. An implementation is available at https://github.com/berkeleydeeprlcourse/homework/tree/master/hw4.

## 6.3 Showcase in the Continuous Domain: Humanoid Running and Steering

To showcase the performance of PPO on high-dimensional continuous control problems, we train on a set of problems involving a 3D humanoid, where the robot must run, steer, and get up off the ground, possibly while being pelted by cubes. The three tasks we test on are (1) RoboschoolHumanoid: forward locomotion only, (2) RoboschoolHumanoidFlagrun: position of target is randomly varied every 200 timesteps or whenever the goal is reached, (3) RoboschoolHumanoidFlagrunHarder, where the robot is pelted by cubes and needs to get up off the ground. See Figure 5 for still frames of a learned policy, and Figure 4 for learning curves on the three tasks. Hyperparameters are provided in Table 4. In concurrent work, Heess et al. [Hee+17] used the adaptive KL variant of PPO (Section 4) to learn locomotion policies for 3D robots.

**Figure 4:** Learning curves from PPO on 3D humanoid control tasks, using Roboschool.

[Figure shows learning curves for RoboschoolHumanoid-v0, RoboschoolHumanoidFlagrun-v0, and RoboschoolHumanoidFlagrunHarder-v0]

**Figure 5:** Still frames of the policy learned from RoboschoolHumanoidFlagrun. In the first six frames, the robot runs towards a target. Then the position is randomly changed, and the robot turns and runs toward the new target.

[Figure shows 12 still frames of humanoid robot running and turning]

## 6.4 Comparison to Other Algorithms on the Atari Domain

We also ran PPO on the Arcade Learning Environment [Bel+15] benchmark and compared against well-tuned implementations of A2C [Mni+16] and ACER [Wan+16]. For all three algorithms, we used the same policy network architechture as used in [Mni+16]. The hyperparameters for PPO are provided in Table 5. For the other two algorithms, we used hyperparameters that were tuned to maximize performance on this benchmark.

A table of results and learning curves for all 49 games is provided in Appendix B. We consider the following two scoring metrics: (1) average reward per episode over entire training period (which favors fast learning), and (2) average reward per episode over last 100 episodes of training (which favors final performance). Table 2 shows the number of games "won" by each algorithm, where we compute the victor by averaging the scoring metric across three trials.

**Table 2:** Number of games "won" by each algorithm, where the scoring metric is averaged across three trials.

|  | A2C | ACER | PPO | Tie |
|--|-----|------|-----|-----|
| (1) avg. episode reward over all of training | 1 | 18 | **30** | 0 |
| (2) avg. episode reward over last 100 episodes | 1 | **28** | 19 | 1 |

---

### النسخة العربية

## 6.1 مقارنة الدوال الهدفية البديلة

أولاً، نقارن عدة دوال هدفية بديلة مختلفة تحت معاملات فائقة مختلفة. هنا، نقارن الدالة الهدفية البديلة $L^{CLIP}$ بعدة تنويعات طبيعية ونسخ مستأصلة.

**بدون قص أو عقوبة:** $L_t(\theta) = r_t(\theta)\hat{A}_t$

**القص:** $L_t(\theta) = \min(r_t(\theta)\hat{A}_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)\hat{A}_t)$

**عقوبة KL (ثابتة أو تكيفية):** $L_t(\theta) = r_t(\theta)\hat{A}_t - \beta \text{KL}[\pi_{\theta_\text{old}}, \pi_\theta]$

بالنسبة لعقوبة KL، يمكن استخدام معامل عقوبة ثابت $\beta$ أو معامل تكيفي كما هو موصوف في القسم 4 باستخدام قيمة KL المستهدفة $d_\text{targ}$. لاحظ أننا حاولنا أيضاً القص في الفضاء اللوغاريتمي، لكننا وجدنا أن الأداء ليس أفضل.

نظراً لأننا نبحث عن المعاملات الفائقة لكل متغير خوارزمية، اخترنا معياراً رخيصاً حسابياً لاختبار الخوارزميات عليه. وهي، استخدمنا 7 مهام روبوتية محاكاة² منفذة في OpenAI Gym [Bro+16]، والتي تستخدم محرك الفيزياء MuJoCo [TET12]. نقوم بمليون خطوة زمنية من التدريب على كل واحدة. بالإضافة إلى المعاملات الفائقة المستخدمة للقص ($\epsilon$) وعقوبة KL ($\beta$، $d_\text{targ}$)، التي نبحث عنها، المعاملات الفائقة الأخرى مقدمة في الجدول 3.

لتمثيل السياسة، استخدمنا MLP متصل بالكامل مع طبقتين مخفيتين من 64 وحدة، ودوال غير خطية tanh، تخرج متوسط توزيع غاوسي، مع انحرافات معيارية متغيرة، متبعين [Sch+15b; Dua+16]. لا نشارك المعاملات بين دالة السياسة ودالة القيمة (لذا المعامل $c_1$ غير ذي صلة)، ولا نستخدم مكافأة الإنتروبيا.

تم تشغيل كل خوارزمية على جميع البيئات السبع، مع 3 بذور عشوائية على كل منها. قمنا بتسجيل كل تشغيل للخوارزمية من خلال حساب متوسط المكافأة الإجمالية للـ100 حلقة الأخيرة. قمنا بإزاحة وقياس النتائج لكل بيئة بحيث أعطت السياسة العشوائية درجة 0 وتم تعيين أفضل نتيجة على 1، وحسبنا المتوسط على 21 تشغيلاً لإنتاج قيمة قياسية واحدة لكل إعداد خوارزمية.

النتائج معروضة في الجدول 1. لاحظ أن الدرجة سالبة للإعداد بدون قص أو عقوبات، لأنه بالنسبة لبيئة واحدة (half cheetah) يؤدي إلى درجة سالبة جداً، وهي أسوأ من السياسة العشوائية الأولية.

**الجدول 1:** نتائج من معيار التحكم المستمر. متوسط الدرجات المعيارية (على 21 تشغيلاً للخوارزمية، على 7 بيئات) لكل خوارزمية/إعداد معامل فائق. تم تهيئة $\beta$ عند 1.

| الخوارزمية | متوسط الدرجة المعيارية |
|-----------|----------------------|
| بدون قص أو عقوبة | -0.39 |
| القص، $\epsilon = 0.1$ | 0.76 |
| **القص، $\epsilon = 0.2$** | **0.82** |
| القص، $\epsilon = 0.3$ | 0.70 |
| KL تكيفي $d_\text{targ} = 0.003$ | 0.68 |
| KL تكيفي $d_\text{targ} = 0.01$ | 0.74 |
| KL تكيفي $d_\text{targ} = 0.03$ | 0.71 |
| KL ثابت، $\beta = 0.3$ | 0.62 |
| KL ثابت، $\beta = 1.$ | 0.71 |
| KL ثابت، $\beta = 3.$ | 0.72 |
| KL ثابت، $\beta = 10.$ | 0.69 |

---

**حاشية:**

²HalfCheetah، Hopper، InvertedDoublePendulum، InvertedPendulum، Reacher، Swimmer، و Walker2d، جميعها "-v1"

## 6.2 المقارنة مع خوارزميات أخرى في المجال المستمر

بعد ذلك، نقارن PPO (مع الدالة الهدفية البديلة "المقصوصة" من القسم 3) بعدة طرق أخرى من الأدبيات، والتي تعتبر فعالة للمشاكل المستمرة. قارنا مع تطبيقات محسّنة للخوارزميات التالية: تحسين السياسة بمنطقة الثقة [Sch+15b]، طريقة الإنتروبيا المتقاطعة (CEM) [SL06]، تدرج السياسة البسيط مع حجم خطوة تكيفي³، A2C [Mni+16]، A2C مع منطقة الثقة [Wan+16]. A2C تعني فاعل-ناقد الأفضلية، وهي نسخة متزامنة من A3C، والتي وجدنا أن لها نفس الأداء أو أفضل من النسخة اللامتزامنة. بالنسبة لـ PPO، استخدمنا المعاملات الفائقة من القسم السابق، مع $\epsilon = 0.2$. نرى أن PPO تتفوق على الطرق السابقة في تقريباً جميع بيئات التحكم المستمر.

**الشكل 3:** مقارنة عدة خوارزميات على عدة بيئات MuJoCo، التدريب لمليون خطوة زمنية.

[يظهر الشكل منحنيات التعلم لـ HalfCheetah-v1، Hopper-v1، InvertedDoublePendulum-v1، InvertedPendulum-v1، Reacher-v1، Swimmer-v1، و Walker2d-v1، مقارنة A2C، A2C + منطقة الثقة، CEM، PPO (القص)، PG البسيط التكيفي، و TRPO]

---

**حاشية:**

³بعد كل دفعة من البيانات، يتم تعديل حجم خطوة Adam بناءً على تباعد KL للسياسة الأصلية والمحدثة، باستخدام قاعدة مشابهة لتلك الموضحة في القسم 4. يتوفر تطبيق على https://github.com/berkeleydeeprlcourse/homework/tree/master/hw4.

## 6.3 عرض توضيحي في المجال المستمر: الجري والتوجيه البشري

لعرض أداء PPO على مشاكل التحكم المستمر عالية الأبعاد، نتدرب على مجموعة من المشاكل التي تتضمن إنساناً ثلاثي الأبعاد، حيث يجب على الروبوت الجري والتوجيه والنهوض من الأرض، ربما أثناء قذفه بالمكعبات. المهام الثلاث التي نختبرها هي (1) RoboschoolHumanoid: الحركة الأمامية فقط، (2) RoboschoolHumanoidFlagrun: يتم تغيير موضع الهدف عشوائياً كل 200 خطوة زمنية أو عندما يتم الوصول إلى الهدف، (3) RoboschoolHumanoidFlagrunHarder، حيث يتم قذف الروبوت بالمكعبات ويحتاج إلى النهوض من الأرض. انظر الشكل 5 لإطارات ثابتة من سياسة متعلمة، والشكل 4 لمنحنيات التعلم على المهام الثلاث. المعاملات الفائقة مقدمة في الجدول 4. في عمل متزامن، استخدم Heess وآخرون [Hee+17] متغير KL التكيفي من PPO (القسم 4) لتعلم سياسات الحركة للروبوتات ثلاثية الأبعاد.

**الشكل 4:** منحنيات التعلم من PPO على مهام التحكم البشري ثلاثي الأبعاد، باستخدام Roboschool.

[يظهر الشكل منحنيات التعلم لـ RoboschoolHumanoid-v0، RoboschoolHumanoidFlagrun-v0، و RoboschoolHumanoidFlagrunHarder-v0]

**الشكل 5:** إطارات ثابتة من السياسة المتعلمة من RoboschoolHumanoidFlagrun. في الإطارات الستة الأولى، يجري الروبوت نحو الهدف. ثم يتم تغيير الموضع عشوائياً، ويدور الروبوت ويجري نحو الهدف الجديد.

[يظهر الشكل 12 إطاراً ثابتاً للروبوت البشري يجري ويدور]

## 6.4 المقارنة مع خوارزميات أخرى في مجال Atari

قمنا أيضاً بتشغيل PPO على معيار بيئة التعلم من الآركيد [Bel+15] وقارنا مع تطبيقات محسّنة جيداً من A2C [Mni+16] و ACER [Wan+16]. بالنسبة للخوارزميات الثلاثة جميعها، استخدمنا نفس معمارية شبكة السياسة المستخدمة في [Mni+16]. المعاملات الفائقة لـ PPO مقدمة في الجدول 5. بالنسبة للخوارزميتين الأخريين، استخدمنا معاملات فائقة تم ضبطها لتعظيم الأداء على هذا المعيار.

جدول النتائج ومنحنيات التعلم لجميع الألعاب الـ49 مقدم في الملحق B. نعتبر المقياسين التاليين للتسجيل: (1) متوسط المكافأة لكل حلقة على فترة التدريب بأكملها (والذي يفضل التعلم السريع)، و (2) متوسط المكافأة لكل حلقة على آخر 100 حلقة من التدريب (والذي يفضل الأداء النهائي). يوضح الجدول 2 عدد الألعاب "المكسوبة" من قبل كل خوارزمية، حيث نحسب الفائز من خلال حساب متوسط مقياس التسجيل عبر ثلاث تجارب.

**الجدول 2:** عدد الألعاب "المكسوبة" من قبل كل خوارزمية، حيث يتم حساب متوسط مقياس التسجيل عبر ثلاث تجارب.

|  | A2C | ACER | PPO | تعادل |
|--|-----|------|-----|-----|
| (1) متوسط مكافأة الحلقة على كل التدريب | 1 | 18 | **30** | 0 |
| (2) متوسط مكافأة الحلقة على آخر 100 حلقة | 1 | **28** | 19 | 1 |

---

### Translation Notes

- **Figures referenced:** Figure 3 (MuJoCo comparison), Figure 4 (Humanoid learning curves), Figure 5 (Humanoid still frames)
- **Tables referenced:** Table 1 (Surrogate objective comparison), Table 2 (Atari comparison), Table 3 (Hyperparameters), Table 4 (Roboschool hyperparameters), Table 5 (Atari hyperparameters)
- **Key terms introduced:**
  - surrogate objective - دالة هدفية بديلة
  - ablated versions - نسخ مستأصلة
  - computationally cheap - رخيص حسابياً
  - simulated robotics - روبوتية محاكاة
  - physics engine - محرك الفيزياء
  - fully-connected MLP - MLP متصل بالكامل
  - hidden layers - طبقات مخفية
  - tanh nonlinearities - دوال غير خطية tanh
  - Gaussian distribution - توزيع غاوسي
  - random seeds - بذور عشوائية
  - normalized scores - درجات معيارية
  - continuous control - التحكم المستمر
  - cross-entropy method - طريقة الإنتروبيا المتقاطعة
  - synchronous version - نسخة متزامنة
  - asynchronous version - نسخة لامتزامنة
  - high-dimensional - عالية الأبعاد
  - locomotion - الحركة
  - Arcade Learning Environment - بيئة التعلم من الآركيد
  - scoring metric - مقياس التسجيل
  - fast learning - التعلم السريع
  - final performance - الأداء النهائي
- **Equations:** 3 objective function definitions
- **Citations:** [Bro+16], [TET12], [Sch+15b], [Dua+16], [SL06], [Mni+16], [Wan+16], [Hee+17], [Bel+15]
- **Special handling:**
  - Translated table headers and content
  - Described figures comprehensively
  - Maintained numerical results accuracy
  - Kept environment names in English (HalfCheetah, Hopper, etc.)
  - Translated footnotes

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
