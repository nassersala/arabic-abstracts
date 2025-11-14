# Section 2: Related Work
## القسم 2: الأعمال ذات الصلة

**Section:** Related Work
**Translation Quality:** 0.86
**Glossary Terms Used:** graphical models, latent variables, restricted Boltzmann machines, deep Boltzmann machines, partition function, Markov chain Monte Carlo, deep belief networks, score matching, noise-contrastive estimation, discriminative training, generative stochastic network, backpropagation

---

### English Version

An alternative to directed graphical models with latent variables are undirected graphical models with latent variables, such as restricted Boltzmann machines (RBMs) [27, 16], deep Boltzmann machines (DBMs) [26] and their numerous variants. The interactions within such models are represented as the product of unnormalized potential functions, normalized by a global summation/integration over all states of the random variables. This quantity (the partition function) and its gradient are intractable for all but the most trivial instances, although they can be estimated by Markov chain Monte Carlo (MCMC) methods. Mixing poses a significant problem for learning algorithms that rely on MCMC [3, 5].

Deep belief networks (DBNs) [16] are hybrid models containing a single undirected layer and several directed layers. While a fast approximate layer-wise training criterion exists, DBNs incur the computational difficulties associated with both undirected and directed models.

Alternative criteria that do not approximate or bound the log-likelihood have also been proposed, such as score matching [18] and noise-contrastive estimation (NCE) [13]. Both of these require the learned probability density to be analytically specified up to a normalization constant. Note that in many interesting generative models with several layers of latent variables (such as DBNs and DBMs), it is not even possible to derive a tractable unnormalized probability density. Some models such as denoising auto-encoders [30] and contractive autoencoders have learning rules very similar to score matching applied to RBMs. In NCE, as in this work, a discriminative training criterion is employed to fit a generative model. However, rather than fitting a separate discriminative model, the generative model itself is used to discriminate generated data from samples a fixed noise distribution. Because NCE uses a fixed noise distribution, learning slows dramatically after the model has learned even an approximately correct distribution over a small subset of the observed variables.

Finally, some techniques do not involve defining a probability distribution explicitly, but rather train a generative machine to draw samples from the desired distribution. This approach has the advantage that such machines can be designed to be trained by back-propagation. Prominent recent work in this area includes the generative stochastic network (GSN) framework [5], which extends generalized denoising auto-encoders [4]: both can be seen as defining a parameterized Markov chain, i.e., one learns the parameters of a machine that performs one step of a generative Markov chain. Compared to GSNs, the adversarial nets framework does not require a Markov chain for sampling. Because adversarial nets do not require feedback loops during generation, they are better able to leverage piecewise linear units [19, 9, 10], which improve the performance of backpropagation but have problems with unbounded activation when used ina feedback loop. More recent examples of training a generative machine by back-propagating into it include recent work on auto-encoding variational Bayes [20] and stochastic backpropagation [24].

---

### النسخة العربية

البديل للنماذج البيانية الموجهة ذات المتغيرات الكامنة هو النماذج البيانية غير الموجهة ذات المتغيرات الكامنة، مثل آلات بولتزمان المقيدة (RBMs) [27، 16]، وآلات بولتزمان العميقة (DBMs) [26] وتنويعاتها العديدة. يتم تمثيل التفاعلات داخل هذه النماذج كحاصل ضرب دوال الجهد غير المعيارية، المعيارة بواسطة جمع/تكامل شامل على جميع حالات المتغيرات العشوائية. هذه الكمية (دالة التقسيم) وتدرجها مستعصية لجميع الحالات باستثناء الحالات الأكثر تافهة، على الرغم من أنه يمكن تقديرها بواسطة أساليب مونت كارلو لسلاسل ماركوف (MCMC). يشكل الخلط مشكلة كبيرة لخوارزميات التعلم التي تعتمد على MCMC [3، 5].

شبكات المعتقدات العميقة (DBNs) [16] هي نماذج هجينة تحتوي على طبقة واحدة غير موجهة وعدة طبقات موجهة. بينما يوجد معيار تدريب طبقي تقريبي سريع، تتكبد DBNs الصعوبات الحسابية المرتبطة بكل من النماذج غير الموجهة والموجهة.

تم اقتراح معايير بديلة لا تقرب أو تحد من اللوغاريتم الاحتمالي، مثل مطابقة النتيجة [18] وتقدير التباين الضوضائي (NCE) [13]. كلاهما يتطلب أن تكون كثافة الاحتمال المتعلمة محددة تحليلياً حتى ثابت المعايرة. لاحظ أنه في العديد من النماذج التوليدية المثيرة للاهتمام مع عدة طبقات من المتغيرات الكامنة (مثل DBNs وDBMs)، لا يمكن حتى اشتقاق كثافة احتمالية غير معيارية قابلة للتتبع. بعض النماذج مثل المشفرات التلقائية لإزالة الضوضاء [30] والمشفرات التلقائية الانكماشية لديها قواعد تعلم مشابهة جداً لمطابقة النتيجة المطبقة على RBMs. في NCE، كما في هذا العمل، يتم استخدام معيار تدريب تمييزي لملاءمة نموذج توليدي. ومع ذلك، بدلاً من ملاءمة نموذج تمييزي منفصل، يُستخدم النموذج التوليدي نفسه للتمييز بين البيانات المولدة والعينات من توزيع ضوضاء ثابت. نظراً لأن NCE يستخدم توزيع ضوضاء ثابت، يتباطأ التعلم بشكل كبير بعد أن يتعلم النموذج توزيعاً صحيحاً تقريباً حتى على مجموعة فرعية صغيرة من المتغيرات الملاحظة.

أخيراً، بعض التقنيات لا تتضمن تعريف توزيع احتمالي بشكل صريح، بل تدرب آلة توليدية لسحب العينات من التوزيع المرغوب. يتمتع هذا النهج بميزة أنه يمكن تصميم هذه الآلات لتدريبها بواسطة الانتشار العكسي. تتضمن الأعمال البارزة الحديثة في هذا المجال إطار عمل الشبكة العشوائية التوليدية (GSN) [5]، الذي يوسع المشفرات التلقائية المعممة لإزالة الضوضاء [4]: يمكن رؤية كليهما على أنهما يحددان سلسلة ماركوف معلمية، أي أن المرء يتعلم معلمات آلة تؤدي خطوة واحدة من سلسلة ماركوف توليدية. بالمقارنة مع GSNs، لا يتطلب إطار عمل الشبكات التنافسية الخصامية سلسلة ماركوف لأخذ العينات. نظراً لأن الشبكات التنافسية الخصامية لا تتطلب حلقات تغذية راجعة أثناء التوليد، فإنها أكثر قدرة على الاستفادة من الوحدات الخطية المتقطعة [19، 9، 10]، التي تحسن أداء الانتشار العكسي ولكن لديها مشاكل مع التنشيط غير المحدود عند استخدامها في حلقة تغذية راجعة. تتضمن الأمثلة الحديثة لتدريب آلة توليدية بالانتشار العكسي فيها الأعمال الحديثة حول التشفير التلقائي للبايز المتغير [20] والانتشار العكسي العشوائي [24].

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Restricted Boltzmann Machines (آلات بولتزمان المقيدة)
  - Deep Boltzmann Machines (آلات بولتزمان العميقة)
  - partition function (دالة التقسيم)
  - Deep Belief Networks (شبكات المعتقدات العميقة)
  - score matching (مطابقة النتيجة)
  - noise-contrastive estimation (تقدير التباين الضوضائي)
  - generative stochastic network (الشبكة العشوائية التوليدية)
- **Equations:** None
- **Citations:** Multiple [27, 16], [26], [3, 5], [18], [13], [30], [4], [19, 9, 10], [20], [24]
- **Special handling:**
  - Technical acronyms (RBMs, DBMs, DBNs, NCE, GSN) kept in English with Arabic expansions
  - "mixing" in MCMC context translated as "الخلط" (refers to chain convergence)

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.88
- **Overall section score:** 0.86

### Back-Translation (Key Paragraph)

"The alternative to directed graphical models with latent variables is undirected graphical models with latent variables, such as restricted Boltzmann machines (RBMs) [27, 16], deep Boltzmann machines (DBMs) [26] and their numerous variants. Interactions within these models are represented as the product of unnormalized potential functions, normalized by a comprehensive summation/integration over all states of random variables. This quantity (the partition function) and its gradient are intractable for all cases except the most trivial ones, although they can be estimated by Markov chain Monte Carlo (MCMC) methods."

**Validation:** ✅ Semantic match confirmed. Technical terminology accurately preserved.
