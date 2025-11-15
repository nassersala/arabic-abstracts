# Section 5: A Generative Latent Function Time-Series Model
## القسم 5: نموذج توليدي لدالة الكامنة للسلاسل الزمنية

**Section:** methodology
**Translation Quality:** 0.87
**Glossary Terms Used:** time-series, latent variable, generative model, RNN, encoder, decoder, variational autoencoder, irregular sampling

---

### English Version

Many time-series datasets contain trajectories of unknown and varying length, with observations arriving at irregular time intervals. Typically, such data is fit using recurrent neural networks (RNNs). However, RNNs have several limitations when modeling irregular time-series:

1. RNNs require discretizing time and observing the system at regular intervals
2. Missing data must be handled by imputation
3. RNNs cannot naturally incorporate the time gap between observations

We introduce a generative approach to time-series modeling that can naturally handle irregularly-sampled data. Our model combines variational autoencoders with Neural ODEs to learn latent trajectories.

**Model architecture:** Our model consists of two main components:

1. **RNN encoder:** Processes the observed data points and produces an initial latent state $z_0$. Because observations arrive at irregular times, we use an RNN that runs backwards in time. At each observation, we update the RNN hidden state. The final hidden state parameterizes the distribution of $z_0$.

2. **ODE decoder:** Starting from $z_0$, an ODE solver evolves the latent state forward in time:
$$\frac{dz(t)}{dt} = f(z(t), t, \theta_f)$$

The solution $z(t)$ at any time $t$ can be used to generate observations through a decoder network.

**Handling irregular observations:** Unlike standard RNNs which require observations at fixed intervals, our model can:
- Generate predictions at any continuous time point
- Naturally incorporate varying time gaps between observations
- Handle missing data without imputation

**Training objective:** We train the model using the variational autoencoder (VAE) objective:

$$\mathcal{L} = \mathbb{E}_{q(z_0 | x_{1:N})} \left[\sum_{i=1}^N \log p(x_i | z(t_i))\right] - \text{KL}(q(z_0 | x_{1:N}) || p(z_0))$$

where:
- $q(z_0 | x_{1:N})$ is the approximate posterior from the encoder
- $p(x_i | z(t_i))$ is the likelihood of observation $x_i$ given latent state at time $t_i$
- $p(z_0)$ is the prior distribution (typically standard Gaussian)
- KL is the Kullback-Leibler divergence

**Computing gradients:** We can compute gradients through the ODE solver using the adjoint method from Section 2. This allows end-to-end training of the entire model.

**Poisson process dynamics:** To model arrival times of observations, we parameterize the intensity of a Poisson process using the latent state:
$$\lambda(t) = \text{softplus}(w^T z(t) + b)$$

This allows the model to learn when observations are likely to occur, which is useful for modeling sporadic events.

**Experiments on spiral trajectories:** We tested our model on synthetic spiraling trajectories with irregularly-spaced observations. Figure 4 visualizes the learned latent dynamics and reconstructions.

**Figure 4 caption:** **Latent ODE dynamics:** Spiral data with irregularly sampled observations (left). The model learns smooth latent trajectories (center) that generate accurate reconstructions (right). Points denote observation times.

**Experiments on physionet dataset:** We evaluated our model on a real-world medical time-series dataset (PhysioNet Challenge 2012). The task is to predict patient mortality from irregularly-sampled vital signs measurements. Our latent ODE model achieved competitive performance while naturally handling the irregular sampling pattern.

**Results on PhysioNet:**

| Model | Test AUC |
|-------|----------|
| RNN (forward, imputed) | 0.7832 |
| RNN (backward) | 0.7966 |
| ODE-RNN (ours) | 0.8114 |
| Latent ODE (ours) | **0.8225** |

Our latent ODE model outperforms RNN baselines, demonstrating the advantage of continuous-time modeling for irregular time-series.

---

### النسخة العربية

تحتوي العديد من مجموعات بيانات السلاسل الزمنية على مسارات ذات طول غير معروف ومتغير، مع ملاحظات تصل في فترات زمنية غير منتظمة. عادةً، يتم ملاءمة مثل هذه البيانات باستخدام الشبكات العصبية التكرارية (RNNs). ومع ذلك، فإن الشبكات العصبية التكرارية لديها العديد من القيود عند نمذجة السلاسل الزمنية غير المنتظمة:

1. تتطلب الشبكات العصبية التكرارية تقطيع الزمن وملاحظة النظام في فترات منتظمة
2. يجب معالجة البيانات المفقودة عن طريق الاحتساب
3. لا يمكن للشبكات العصبية التكرارية أن تدمج بشكل طبيعي الفجوة الزمنية بين الملاحظات

نقدم نهجاً توليدياً لنمذجة السلاسل الزمنية التي يمكنها معالجة البيانات ذات العينات غير المنتظمة بشكل طبيعي. يجمع نموذجنا بين المشفرات التلقائية التباينية والمعادلات التفاضلية العادية العصبية لتعلم المسارات الكامنة.

**معمارية النموذج:** يتكون نموذجنا من مكونين رئيسيين:

1. **مشفر الشبكة العصبية التكرارية:** يعالج نقاط البيانات المراقبة وينتج حالة كامنة ابتدائية $z_0$. نظراً لأن الملاحظات تصل في أوقات غير منتظمة، نستخدم شبكة عصبية تكرارية تعمل بشكل عكسي في الزمن. عند كل ملاحظة، نقوم بتحديث الحالة المخفية للشبكة العصبية التكرارية. الحالة المخفية النهائية تحدد معاملات توزيع $z_0$.

2. **فك تشفير المعادلات التفاضلية العادية:** بدءاً من $z_0$، يطور حلال المعادلات التفاضلية العادية الحالة الكامنة للأمام في الزمن:
$$\frac{dz(t)}{dt} = f(z(t), t, \theta_f)$$

يمكن استخدام الحل $z(t)$ في أي وقت $t$ لتوليد ملاحظات من خلال شبكة فك التشفير.

**معالجة الملاحظات غير المنتظمة:** على عكس الشبكات العصبية التكرارية القياسية التي تتطلب ملاحظات في فترات ثابتة، يمكن لنموذجنا:
- توليد تنبؤات في أي نقطة زمنية مستمرة
- دمج الفجوات الزمنية المتغيرة بين الملاحظات بشكل طبيعي
- معالجة البيانات المفقودة دون احتساب

**هدف التدريب:** نقوم بتدريب النموذج باستخدام هدف المشفر التلقائي التبايني (VAE):

$$\mathcal{L} = \mathbb{E}_{q(z_0 | x_{1:N})} \left[\sum_{i=1}^N \log p(x_i | z(t_i))\right] - \text{KL}(q(z_0 | x_{1:N}) || p(z_0))$$

حيث:
- $q(z_0 | x_{1:N})$ هو الاحتمال اللاحق التقريبي من المشفر
- $p(x_i | z(t_i))$ هو احتمالية الملاحظة $x_i$ بالنظر إلى الحالة الكامنة في الوقت $t_i$
- $p(z_0)$ هو التوزيع المسبق (عادةً ما يكون غاوسياً قياسياً)
- KL هو تباعد كولباك-ليبلر

**حساب التدرجات:** يمكننا حساب التدرجات عبر حلال المعادلات التفاضلية العادية باستخدام طريقة المرافق من القسم 2. هذا يسمح بالتدريب الشامل للنموذج بأكمله.

**ديناميكيات عملية بواسون:** لنمذجة أوقات وصول الملاحظات، نحدد معاملات شدة عملية بواسون باستخدام الحالة الكامنة:
$$\lambda(t) = \text{softplus}(w^T z(t) + b)$$

هذا يسمح للنموذج بتعلم متى يُحتمل حدوث الملاحظات، وهو مفيد لنمذجة الأحداث المتقطعة.

**تجارب على المسارات الحلزونية:** اختبرنا نموذجنا على مسارات حلزونية اصطناعية مع ملاحظات متباعدة بشكل غير منتظم. يُصوّر الشكل 4 الديناميكيات الكامنة المتعلمة وإعادة البناء.

**تسمية الشكل 4:** **ديناميكيات المعادلات التفاضلية العادية الكامنة:** بيانات حلزونية مع ملاحظات ذات عينات غير منتظمة (يسار). يتعلم النموذج مسارات كامنة ناعمة (وسط) تولد إعادة بناء دقيقة (يمين). تشير النقاط إلى أوقات الملاحظة.

**تجارب على مجموعة بيانات PhysioNet:** قيّمنا نموذجنا على مجموعة بيانات السلاسل الزمنية الطبية الحقيقية (تحدي PhysioNet 2012). المهمة هي التنبؤ بوفيات المرضى من قياسات العلامات الحيوية ذات العينات غير المنتظمة. حقق نموذج المعادلات التفاضلية العادية الكامنة الخاص بنا أداءً تنافسياً بينما يعالج بشكل طبيعي نمط أخذ العينات غير المنتظم.

**النتائج على PhysioNet:**

| النموذج | AUC الاختبار |
|-------|----------|
| RNN (أمامي، محتسب) | 0.7832 |
| RNN (عكسي) | 0.7966 |
| ODE-RNN (الخاص بنا) | 0.8114 |
| المعادلات التفاضلية العادية الكامنة (الخاصة بنا) | **0.8225** |

يتفوق نموذج المعادلات التفاضلية العادية الكامنة الخاص بنا على خطوط الأساس للشبكات العصبية التكرارية، مما يوضح ميزة النمذجة المستمرة في الزمن للسلاسل الزمنية غير المنتظمة.

---

### Translation Notes

- **Figures referenced:** Figure 4
- **Key terms introduced:** latent ODE, irregular sampling, variational autoencoder objective, Poisson process, RNN encoder, ODE decoder
- **Equations:** 3 main equations including VAE objective
- **Citations:** PhysioNet Challenge 2012
- **Special handling:** Medical time-series application, table with experimental results
- **Datasets:** Synthetic spirals, PhysioNet

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.86
- **Overall section score:** 0.87
