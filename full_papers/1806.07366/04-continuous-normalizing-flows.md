# Section 4: Continuous Normalizing Flows
## القسم 4: تدفقات التطبيع المستمرة

**Section:** methodology
**Translation Quality:** 0.88
**Glossary Terms Used:** normalizing flows, generative model, probability density, change of variables, Jacobian, invertible, maximum likelihood, training

---

### English Version

Normalizing flows are a powerful class of generative models (Rezende & Mohamed, 2015; Dinh et al., 2016). They use the change of variables formula to compute exact log-likelihoods of data. Like variational autoencoders and generative adversarial networks, normalizing flows can scale to high-dimensional data.

**Change of variables formula:** Let $z_0$ be a random variable with distribution $p(z_0)$ and $f$ an invertible smooth mapping. The distribution of $z_1 = f(z_0)$ is:

$$p(z_1) = p(z_0) \left|\det \frac{\partial f}{\partial z_0}\right|^{-1}$$

The absolute value of the determinant of the Jacobian measures how much the mapping $f$ expands or contracts space. Computing the determinant $\det(\partial f / \partial z)$ usually costs $O(D^3)$, where $D$ is the dimensionality of $z$.

**Normalizing flow models:** Normalizing flows transform a base distribution $p(z_0)$ (usually a standard Gaussian) through a sequence of invertible transformations $f_1, f_2, \ldots, f_K$ to produce samples in the data space:

$$z_K = f_K \circ f_{K-1} \circ \cdots \circ f_1(z_0)$$

The log-density is computed by summing the log-determinants:

$$\log p(z_K) = \log p(z_0) - \sum_{k=1}^K \log \left|\det \frac{\partial f_k}{\partial z_{k-1}}\right|$$

**Limitations of discrete flows:** To make computation tractable, most previous work has restricted the architecture such that the Jacobian of $f$ is triangular. This allows the determinant to be computed in linear time as the product of diagonal elements. However, this architectural restriction reduces the expressiveness of the model.

**Continuous normalizing flows:** An ODE can be seen as an infinite sequence of infinitesimal transformations. We can use the instantaneous change of variables formula (Chen & Duvenaud, 2018) to describe how the probability density changes along the continuous-time transformation:

$$\frac{d \log p(z(t))}{dt} = -\text{tr}\left(\frac{\partial f}{\partial z(t)}\right)$$

This formula is derived from taking the limit of a discrete normalizing flow as the step size approaches zero. The term $\text{tr}(\partial f / \partial z(t))$ is called the divergence of $f$, and measures the rate of expansion or contraction of the volume around $z(t)$.

**Computing the log-density:** Given an initial probability density $p(z(t_0))$, the log-density of $z(t_1)$ can be computed by integrating across time:

$$\log p(z(t_1)) = \log p(z(t_0)) - \int_{t_0}^{t_1} \text{tr}\left(\frac{\partial f(z(t), t, \theta)}{\partial z(t)}\right) dt$$

We can compute the trace of a Jacobian using automatic differentiation for roughly the same cost as evaluating $f$ (Griewank & Walther, 2008). This can be done using a "trace estimator" that uses vector-Jacobian products.

**Advantages:** Unlike discrete normalizing flows, continuous normalizing flows:
1. Do not require restricted architectures to make the Jacobian computation tractable
2. Can use any off-the-shelf ODE solver
3. Have more expressive dynamics since the transformation is defined continuously

**Training continuous normalizing flows:** We can train continuous normalizing flows by maximum likelihood. Given a dataset $\{x_1, \ldots, x_N\}$, we maximize:

$$\max_{\theta} \frac{1}{N} \sum_{i=1}^N \log p(x_i) = \max_{\theta} \frac{1}{N} \sum_{i=1}^N \left[\log p(z(t_0)) - \int_{t_0}^{t_1} \text{tr}\left(\frac{\partial f}{\partial z(t)}\right) dt\right]$$

where $z(t_0) = f^{-1}(x_i)$ is found by running the ODE solver backwards. The gradient with respect to $\theta$ can be computed using the adjoint method from Section 2.

**Experiments on toy 2D distributions:** We visualized the learned transformations on several 2D distributions. Figure 3 shows how continuous normalizing flows can learn complex multimodal distributions by continuously transforming a simple Gaussian.

**Figure 3 caption:** Samples and density of a continuous normalizing flow trained on 2D distributions. The model learns to transform a simple 2D Gaussian into complex target distributions.

---

### النسخة العربية

تدفقات التطبيع هي فئة قوية من النماذج التوليدية (Rezende & Mohamed, 2015; Dinh et al., 2016). تستخدم صيغة تغيير المتغيرات لحساب احتماليات لوغاريتمية دقيقة للبيانات. مثل المشفرات التلقائية التباينية والشبكات التوليدية التنافسية الخصامية، يمكن لتدفقات التطبيع أن تتوسع إلى بيانات عالية الأبعاد.

**صيغة تغيير المتغيرات:** لتكن $z_0$ متغيراً عشوائياً بتوزيع $p(z_0)$ و $f$ تطبيقاً أملس قابلاً للعكس. توزيع $z_1 = f(z_0)$ هو:

$$p(z_1) = p(z_0) \left|\det \frac{\partial f}{\partial z_0}\right|^{-1}$$

القيمة المطلقة لمحدد الجاكوبيان تقيس مدى توسع أو تقلص التطبيق $f$ للفضاء. حساب المحدد $\det(\partial f / \partial z)$ عادةً ما يكلف $O(D^3)$، حيث $D$ هو بُعد $z$.

**نماذج تدفقات التطبيع:** تحول تدفقات التطبيع توزيعاً أساسياً $p(z_0)$ (عادةً ما يكون غاوسياً قياسياً) من خلال تسلسل من التحويلات القابلة للعكس $f_1, f_2, \ldots, f_K$ لإنتاج عينات في فضاء البيانات:

$$z_K = f_K \circ f_{K-1} \circ \cdots \circ f_1(z_0)$$

يتم حساب كثافة اللوغاريتم من خلال جمع محددات اللوغاريتم:

$$\log p(z_K) = \log p(z_0) - \sum_{k=1}^K \log \left|\det \frac{\partial f_k}{\partial z_{k-1}}\right|$$

**قيود التدفقات المنفصلة:** لجعل الحساب قابلاً للمعالجة، قيّد معظم الأعمال السابقة المعمارية بحيث يكون جاكوبيان $f$ مثلثياً. هذا يسمح بحساب المحدد في وقت خطي كحاصل ضرب العناصر القطرية. ومع ذلك، فإن هذا القيد المعماري يقلل من تعبيرية النموذج.

**تدفقات التطبيع المستمرة:** يمكن النظر إلى المعادلة التفاضلية العادية على أنها تسلسل لا نهائي من التحويلات اللانهائية الصغر. يمكننا استخدام صيغة تغيير المتغيرات اللحظية (Chen & Duvenaud, 2018) لوصف كيفية تغير كثافة الاحتمال على طول التحويل المستمر في الزمن:

$$\frac{d \log p(z(t))}{dt} = -\text{tr}\left(\frac{\partial f}{\partial z(t)}\right)$$

تُشتق هذه الصيغة من أخذ حد تدفق التطبيع المنفصل عندما يقترب حجم الخطوة من الصفر. المصطلح $\text{tr}(\partial f / \partial z(t))$ يسمى تباعد $f$، ويقيس معدل التوسع أو التقلص للحجم حول $z(t)$.

**حساب كثافة اللوغاريتم:** بالنظر إلى كثافة احتمال ابتدائية $p(z(t_0))$، يمكن حساب كثافة اللوغاريتم لـ $z(t_1)$ من خلال التكامل عبر الزمن:

$$\log p(z(t_1)) = \log p(z(t_0)) - \int_{t_0}^{t_1} \text{tr}\left(\frac{\partial f(z(t), t, \theta)}{\partial z(t)}\right) dt$$

يمكننا حساب أثر الجاكوبيان باستخدام التفاضل الآلي بتكلفة تقريباً مماثلة لتقييم $f$ (Griewank & Walther, 2008). يمكن القيام بذلك باستخدام "مقدّر الأثر" الذي يستخدم جداءات المتجه-جاكوبيان.

**المزايا:** على عكس تدفقات التطبيع المنفصلة، فإن تدفقات التطبيع المستمرة:
1. لا تتطلب معماريات مقيدة لجعل حساب الجاكوبيان قابلاً للمعالجة
2. يمكنها استخدام أي حلال معادلات تفاضلية عادية جاهز
3. لديها ديناميكيات أكثر تعبيرية لأن التحويل محدد بشكل مستمر

**تدريب تدفقات التطبيع المستمرة:** يمكننا تدريب تدفقات التطبيع المستمرة بأقصى احتمالية. بالنظر إلى مجموعة بيانات $\{x_1, \ldots, x_N\}$، نقوم بتعظيم:

$$\max_{\theta} \frac{1}{N} \sum_{i=1}^N \log p(x_i) = \max_{\theta} \frac{1}{N} \sum_{i=1}^N \left[\log p(z(t_0)) - \int_{t_0}^{t_1} \text{tr}\left(\frac{\partial f}{\partial z(t)}\right) dt\right]$$

حيث يتم إيجاد $z(t_0) = f^{-1}(x_i)$ عن طريق تشغيل حلال المعادلات التفاضلية العادية بشكل عكسي. يمكن حساب التدرج بالنسبة لـ $\theta$ باستخدام طريقة المرافق من القسم 2.

**تجارب على التوزيعات ثنائية الأبعاد البسيطة:** قمنا بتصوير التحويلات المتعلمة على عدة توزيعات ثنائية الأبعاد. يُظهر الشكل 3 كيف يمكن لتدفقات التطبيع المستمرة تعلم توزيعات معقدة متعددة الأنماط من خلال التحويل المستمر لتوزيع غاوسي بسيط.

**تسمية الشكل 3:** عينات وكثافة تدفق التطبيع المستمر المدرب على توزيعات ثنائية الأبعاد. يتعلم النموذج تحويل توزيع غاوسي ثنائي الأبعاد بسيط إلى توزيعات مستهدفة معقدة.

---

### Translation Notes

- **Figures referenced:** Figure 3
- **Key terms introduced:** continuous normalizing flows, change of variables, Jacobian determinant, trace, divergence, invertible transformation, maximum likelihood
- **Equations:** 7 main equations including change of variables formula
- **Citations:** Rezende & Mohamed (2015), Dinh et al. (2016), Chen & Duvenaud (2018), Griewank & Walther (2008)
- **Special handling:** Mathematical derivations of continuous transformations, trace computation

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.91
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.88
