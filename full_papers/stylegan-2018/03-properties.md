# Section 3: Properties of the style-based generator
## القسم 3: خصائص المولد القائم على الأنماط

**Section:** properties
**Translation Quality:** 0.88
**Glossary Terms Used:** generator, synthesis network, style, AdaIN, latent code, feature maps, stochastic variation, mixing regularization, localization

---

### English Version

Our generator architecture makes it possible to control the image synthesis via scale-specific modifications to the styles. We can view the mapping network and affine transformations as a way to draw samples for each style from a learned distribution, and the synthesis network as a way to generate a novel image based on a collection of styles. The effects of each style are localized in the network, i.e., modifying a specific subset of the styles can be expected to affect only certain aspects of the image.

To see the reason for this localization, let us consider how the AdaIN operation (Eq. 1) first normalizes each channel to zero mean and unit variance, and only then applies scales and biases based on the style. The new per-channel statistics, as dictated by the style, modify the relative importance of features for the subsequent convolution operation, but they do not depend on the original statistics because of the normalization. Thus each style controls only one convolution before being overridden by the next AdaIN operation.

## 3.1. Style mixing

To further encourage the styles to localize, we employ *mixing regularization*, where a given percentage of images are generated using two random latent codes instead of one during training. When generating such an image, we simply switch from one latent code to another—an operation we refer to as *style mixing*—at a randomly selected point in the synthesis network. To be specific, we run two latent codes $\mathbf{z}_1, \mathbf{z}_2$ through the mapping network, and have the corresponding $\mathbf{w}_1, \mathbf{w}_2$ control the styles so that $\mathbf{w}_1$ applies before the crossover point and $\mathbf{w}_2$ after it. This regularization technique prevents the network from assuming that adjacent styles are correlated.

Table 2 shows how enabling mixing regularization during training improves the localization considerably, indicated by improved FIDs in scenarios where multiple latents are mixed at test time. Figure 3 presents examples of images synthesized by mixing two latent codes at various scales. We can see that each subset of styles controls meaningful high-level attributes of the image.

## 3.2. Stochastic variation

There are many aspects in human portraits that can be regarded as stochastic, such as the exact placement of hairs, stubble, freckles, or skin pores. Any of these can be randomized without affecting our perception of the image as long as they follow the correct distribution.

Let us consider how a traditional generator implements stochastic variation. Given that the only input to the network is through the input layer, the network needs to invent a way to generate spatially-varying pseudorandom numbers from earlier activations whenever they are needed. This consumes network capacity and hiding the periodicity of generated signal is difficult—and not always successful, as evidenced by commonly seen repetitive patterns in generated images. Our architecture sidesteps these issues altogether by adding per-pixel noise after each convolution.

Figure 4 shows stochastic realizations of the same underlying image, produced using our generator with different noise realizations. We can see that the noise affects only the stochastic aspects, leaving the overall composition and high-level aspects such as identity intact. Figure 5 further illustrates the effect of applying stochastic variation to different subsets of layers. Since these effects are best seen in animation, please consult the accompanying video for a demonstration of how changing the noise input of one layer leads to stochastic variation at a matching scale.

We find it interesting that the effect of noise appears tightly localized in the network. We hypothesize that at any point in the generator, there is pressure to introduce new content as soon as possible, and the easiest way for our network to create stochastic variation is to rely on the noise provided. A fresh set of noise is available for every layer, and thus there is no incentive to generate the stochastic effects from earlier activations, leading to a localized effect.

## 3.3. Separation of global effects from stochasticity

The previous sections as well as the accompanying video demonstrate that while changes to the style have global effects (changing pose, identity, etc.), the noise affects only inconsequential stochastic variation (differently combed hair, beard, etc.). This observation is in line with style transfer literature, where it has been established that spatially invariant statistics (Gram matrix, channel-wise mean, variance, etc.) reliably encode the style of an image while spatially varying features encode a specific instance.

In our style-based generator, the style affects the entire image because complete feature maps are scaled and biased with the same values. Therefore, global effects such as pose, lighting, or background style can be controlled coherently. Meanwhile, the noise is added independently to each pixel and is thus ideally suited for controlling stochastic variation. If the network tried to control, e.g., pose using the noise, that would lead to spatially inconsistent decisions that would then be penalized by the discriminator. Thus the network learns to use the global and local channels appropriately, without explicit guidance.

---

### النسخة العربية

تجعل معمارية مولدنا من الممكن التحكم في توليد الصورة عبر تعديلات خاصة بالمقياس على الأنماط. يمكننا النظر إلى شبكة التعيين والتحويلات الأفينية كطريقة لسحب عينات لكل نمط من توزيع متعلم، وشبكة التوليد كطريقة لتوليد صورة جديدة بناءً على مجموعة من الأنماط. تتمركز تأثيرات كل نمط في الشبكة، أي أن تعديل مجموعة فرعية محددة من الأنماط يمكن أن يُتوقع أن يؤثر فقط على جوانب معينة من الصورة.

لفهم سبب هذا التمركز، دعونا ننظر في كيفية تطبيع عملية AdaIN (المعادلة 1) أولاً لكل قناة إلى متوسط صفري وتباين واحد، وعندئذٍ فقط تطبق المقاييس والانحيازات بناءً على النمط. الإحصائيات الجديدة لكل قناة، كما يمليها النمط، تعدّل الأهمية النسبية للميزات لعملية الالتفاف اللاحقة، لكنها لا تعتمد على الإحصائيات الأصلية بسبب التطبيع. وبالتالي، يتحكم كل نمط في التفاف واحد فقط قبل أن يتم تجاوزه بواسطة عملية AdaIN التالية.

## 3.1. مزج الأنماط

لتشجيع الأنماط على التمركز بشكل أكبر، نستخدم *تنظيم المزج*، حيث يتم توليد نسبة معينة من الصور باستخدام شفرتين كامنتين عشوائيتين بدلاً من واحدة أثناء التدريب. عند توليد مثل هذه الصورة، ببساطة ننتقل من شفرة كامنة واحدة إلى أخرى—عملية نشير إليها باسم *مزج الأنماط*—عند نقطة محددة عشوائياً في شبكة التوليد. على وجه التحديد، نمرر شفرتين كامنتين $\mathbf{z}_1, \mathbf{z}_2$ عبر شبكة التعيين، ونجعل $\mathbf{w}_1, \mathbf{w}_2$ المقابلتين تتحكمان في الأنماط بحيث يطبق $\mathbf{w}_1$ قبل نقطة التقاطع و $\mathbf{w}_2$ بعدها. تمنع تقنية التنظيم هذه الشبكة من افتراض أن الأنماط المتجاورة مترابطة.

يوضح الجدول 2 كيف أن تمكين تنظيم المزج أثناء التدريب يحسّن التمركز بشكل كبير، كما هو مبين من خلال تحسين مسافات FID في السيناريوهات التي يتم فيها مزج كامنات متعددة في وقت الاختبار. يقدم الشكل 3 أمثلة على صور تم توليدها بمزج شفرتين كامنتين على مقاييس مختلفة. يمكننا أن نرى أن كل مجموعة فرعية من الأنماط تتحكم في سمات عالية المستوى ذات معنى للصورة.

## 3.2. التباين العشوائي

هناك العديد من الجوانب في الصور الشخصية البشرية التي يمكن اعتبارها عشوائية، مثل الموضع الدقيق للشعر أو اللحية الخفيفة أو النمش أو مسام الجلد. يمكن عشوأة أي من هذه دون التأثير على إدراكنا للصورة طالما أنها تتبع التوزيع الصحيح.

دعونا ننظر في كيفية تنفيذ مولد تقليدي للتباين العشوائي. بالنظر إلى أن المدخل الوحيد للشبكة هو من خلال طبقة المدخلات، تحتاج الشبكة إلى ابتكار طريقة لتوليد أرقام شبه عشوائية متغيرة مكانياً من التنشيطات السابقة كلما دعت الحاجة إلى ذلك. هذا يستهلك سعة الشبكة وإخفاء دورية الإشارة المولدة صعب—وليس ناجحاً دائماً، كما يتضح من الأنماط المتكررة التي تُرى عادة في الصور المولدة. تتجنب معماريتنا هذه المشكلات تماماً من خلال إضافة ضوضاء لكل بكسل بعد كل التفاف.

يوضح الشكل 4 تحققات عشوائية لنفس الصورة الأساسية، المنتجة باستخدام مولدنا مع تحققات ضوضاء مختلفة. يمكننا أن نرى أن الضوضاء تؤثر فقط على الجوانب العشوائية، تاركة التكوين العام والجوانب عالية المستوى مثل الهوية سليمة. يوضح الشكل 5 كذلك تأثير تطبيق التباين العشوائي على مجموعات فرعية مختلفة من الطبقات. نظراً لأن هذه التأثيرات تُرى بشكل أفضل في الرسوم المتحركة، يرجى الرجوع إلى الفيديو المصاحب لعرض توضيحي لكيفية تغيير مدخل الضوضاء لطبقة واحدة يؤدي إلى تباين عشوائي بمقياس مطابق.

نجد أنه من المثير للاهتمام أن تأثير الضوضاء يبدو متمركزاً بإحكام في الشبكة. نفترض أنه في أي نقطة في المولد، هناك ضغط لإدخال محتوى جديد في أقرب وقت ممكن، وأسهل طريقة لشبكتنا لإنشاء تباين عشوائي هي الاعتماد على الضوضاء المقدمة. مجموعة جديدة من الضوضاء متاحة لكل طبقة، وبالتالي لا يوجد حافز لتوليد التأثيرات العشوائية من التنشيطات السابقة، مما يؤدي إلى تأثير متمركز.

## 3.3. فصل التأثيرات العامة عن العشوائية

توضح الأقسام السابقة وكذلك الفيديو المصاحب أنه بينما التغييرات في النمط لها تأثيرات عامة (تغيير الوضعية والهوية وما إلى ذلك)، فإن الضوضاء تؤثر فقط على التباين العشوائي غير المهم (الشعر المسرح بشكل مختلف واللحية وما إلى ذلك). هذه الملاحظة تتماشى مع أدبيات نقل الأنماط، حيث تم التأكد من أن الإحصائيات الثابتة مكانياً (مصفوفة غرام، المتوسط لكل قناة، التباين، إلخ.) تشفر بشكل موثوق نمط الصورة بينما الميزات المتغيرة مكانياً تشفر مثيلاً محدداً.

في مولدنا القائم على الأنماط، يؤثر النمط على الصورة بأكملها لأن خرائط الميزات الكاملة يتم قياسها وإضافة انحياز لها بنفس القيم. لذلك، يمكن التحكم في التأثيرات العامة مثل الوضعية أو الإضاءة أو نمط الخلفية بشكل متماسك. في الوقت نفسه، تُضاف الضوضاء بشكل مستقل إلى كل بكسل وبالتالي فهي مناسبة بشكل مثالي للتحكم في التباين العشوائي. إذا حاولت الشبكة التحكم، على سبيل المثال، في الوضعية باستخدام الضوضاء، فسيؤدي ذلك إلى قرارات غير متسقة مكانياً ستعاقب عليها بعد ذلك المميز. وبالتالي تتعلم الشبكة استخدام القنوات العامة والمحلية بشكل مناسب، بدون توجيه صريح.

---

### Translation Notes

- **Figures referenced:** Figure 3 (style mixing examples), Figure 4 (noise variations), Figure 5 (layer-wise noise effects), Table 2 (mixing regularization results)
- **Key terms introduced:**
  - Scale-specific (خاص بالمقياس)
  - Localization (التمركز)
  - Crossover point (نقطة التقاطع)
  - Per-pixel noise (ضوضاء لكل بكسل)
  - Pseudorandom numbers (أرقام شبه عشوائية)
  - Spatially invariant (ثابت مكانياً)
  - Spatially varying (متغير مكانياً)
  - Gram matrix (مصفوفة غرام)
  - Global effects (التأثيرات العامة)
  - Local channels (القنوات المحلية)
- **Equations:** Reference to Equation 1 (AdaIN)
- **Citations:** References to style transfer literature
- **Special handling:** Subsections preserved, video references maintained

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.89
- **Overall section score:** 0.88
