# Section 4: Disentanglement studies
## القسم 4: دراسات فك الترابط

**Section:** disentanglement
**Translation Quality:** 0.86
**Glossary Terms Used:** disentanglement, latent space, factors of variation, intermediate latent space, perceptual path length, linear separability, mapping network, interpolation, SVM, entropy

---

### English Version

There are various definitions for disentanglement, but a common goal is a latent space that consists of linear subspaces, each of which controls one factor of variation. However, the sampling probability of each combination of factors in $\mathcal{Z}$ needs to match the corresponding density in the training data. As illustrated in Figure 6, this precludes the factors from being fully disentangled with typical datasets and input latent distributions.

A major benefit of our generator architecture is that the intermediate latent space $\mathcal{W}$ does not have to support sampling according to any *fixed* distribution; its sampling density is induced by the *learned* piecewise continuous mapping $f(\mathbf{z})$. This mapping can be adapted to "unwarp" $\mathcal{W}$ so that the factors of variation become more linear. We posit that there is pressure for the generator to do so, as it should be easier to generate realistic images based on a disentangled representation than based on an entangled representation. As such, we expect the training to yield a less entangled $\mathcal{W}$ in an unsupervised setting, i.e., when the factors of variation are not known in advance.

Unfortunately the metrics recently proposed for quantifying disentanglement require an encoder network that maps input images to latent codes. These metrics are ill-suited for our purposes since our baseline GAN lacks such an encoder. While it is possible to add an extra network for this purpose, we want to avoid investing effort into a component that is not a part of the actual solution. To this end, we describe two new ways of quantifying disentanglement, neither of which requires an encoder or known factors of variation, and are therefore computable for any image dataset and generator.

## 4.1. Perceptual path length

As noted by Laine, interpolation of latent-space vectors may yield surprisingly non-linear changes in the image. For example, features that are absent in either endpoint may appear in the middle of a linear interpolation path. This is a sign that the latent space is entangled and the factors of variation are not properly separated. To quantify this effect, we can measure how drastic changes the image undergoes as we perform interpolation in the latent space. Intuitively, a less curved latent space should result in perceptually smoother transition than a highly curved latent space.

As a basis for our metric, we use a perceptually-based pairwise image distance that is calculated as a weighted difference between two VGG16 embeddings, where the weights are fit so that the metric agrees with human perceptual similarity judgments. If we subdivide a latent space interpolation path into linear segments, we can define the total perceptual length of this segmented path as the sum of perceptual differences over each segment, as reported by the image distance metric. A natural definition for the perceptual path length would be the limit of this sum under infinitely fine subdivision, but in practice we approximate it using a small subdivision epsilon $\epsilon=10^{-4}$. The average perceptual path length in latent space $\mathcal{Z}$, over all possible endpoints, is therefore

$$l_{\mathcal{Z}} = \mathbb{E}\left[\frac{1}{\epsilon^2}d\big(G(\mathrm{slerp}(\mathbf{z}_1,\mathbf{z}_2;t)), G(\mathrm{slerp}(\mathbf{z}_1,\mathbf{z}_2;t+\epsilon))\big)\right]$$

where $\mathbf{z}_1,\mathbf{z}_2\sim P(\mathbf{z}),t\sim U(0,1)$, $G$ is the generator (i.e., $g \circ f$ for style-based networks), and $d(\cdot,\cdot)$ evaluates the perceptual distance between the resulting images. Here $\mathrm{slerp}$ denotes spherical interpolation, which is the most appropriate way of interpolating in our normalized input latent space. To concentrate on the facial features instead of background, we crop the generated images to contain only the face prior to evaluating the pairwise image metric. As the metric $d$ is quadratic, we divide by $\epsilon^2$. We compute the expectation by taking 100,000 samples.

Computing the average perceptual path length in $\mathcal{W}$ is carried out in a similar fashion:

$$l_{\mathcal{W}} = \mathbb{E}\left[\frac{1}{\epsilon^2}d\big(g(\mathrm{lerp}(f(\mathbf{z}_1),f(\mathbf{z}_2);t)), g(\mathrm{lerp}(f(\mathbf{z}_1),f(\mathbf{z}_2);t+\epsilon))\big)\right]$$

where the only difference is that interpolation happens in $\mathcal{W}$ space. Because vectors in $\mathcal{W}$ are not normalized in any fashion, we use linear interpolation ($\mathrm{lerp}$).

Table 3 shows that this full-path length is substantially shorter for our style-based generator with noise inputs, indicating that $\mathcal{W}$ is perceptually more linear than $\mathcal{Z}$. Yet, this measurement is in fact slightly biased in favor of the input latent space $\mathcal{Z}$. If $\mathcal{W}$ is indeed a disentangled and "flattened" mapping of $\mathcal{Z}$, it may contain regions that are not on the input manifold—and are thus badly reconstructed by the generator—even between points that are mapped from the input manifold, whereas the input latent space $\mathcal{Z}$ has no such regions by definition. It is therefore to be expected that if we restrict our measure to path endpoints, i.e., $t \in \{0,1\}$, we should obtain a smaller $l_{\mathcal{W}}$ while $l_{\mathcal{Z}}$ is not affected. This is indeed what we observe in Table 3.

Table 4 shows how path lengths are affected by the mapping network. We see that both traditional and style-based generators benefit from having a mapping network, and additional depth generally improves the perceptual path length as well as FIDs. It is interesting that while $l_{\mathcal{W}}$ improves in the traditional generator, $l_{\mathcal{Z}}$ becomes considerably worse, illustrating our claim that the input latent space can indeed be arbitrarily entangled in GANs.

## 4.2. Linear separability

If a latent space is sufficiently disentangled, it should be possible to find direction vectors that consistently correspond to individual factors of variation. We propose another metric that quantifies this effect by measuring how well the latent-space points can be separated into two distinct sets via a linear hyperplane, so that each set corresponds to a specific binary attribute of the image.

In order to label the generated images, we train auxiliary classification networks for a number of binary attributes, e.g., to distinguish male and female faces. In our tests, the classifiers had the same architecture as the discriminator we use (i.e., same as in Karras et al.), and were trained using the CelebA-HQ dataset that retains the 40 attributes available in the original CelebA dataset. To measure the separability of one attribute, we generate 200,000 images with $\mathbf{z}\sim P(\mathbf{z})$ and classify them using the auxiliary classification network. We then sort the samples according to classifier confidence and remove the least confident half, yielding 100,000 labeled latent-space vectors.

For each attribute, we fit a linear SVM to predict the label based on the latent-space point—$\mathbf{z}$ for traditional and $\mathbf{w}$ for style-based—and classify the points by this plane. We then compute the conditional entropy $H(Y|X)$ where $X$ are the classes predicted by the SVM and $Y$ are the classes determined by the pre-trained classifier. This tells how much additional information is required to determine the true class of a sample, given that we know on which side of the hyperplane it lies. A low value suggests consistent latent space directions for the corresponding factor(s) of variation.

We calculate the final separability score as $\exp(\sum_i H(Y_i|X_i))$, where $i$ enumerates the 40 attributes. Similar to the inception score, the exponentiation brings the values from logarithmic to linear domain so that they are easier to compare.

Tables 3 and 4 show that $\mathcal{W}$ is consistently better separable than $\mathcal{Z}$, suggesting a less entangled representation. Furthermore, increasing the depth of the mapping network improves both image quality and separability in $\mathcal{W}$, which is in line with the hypothesis that the synthesis network inherently favors a disentangled input representation. Interestingly, adding a mapping network in front of a traditional generator results in severe loss of separability in $\mathcal{Z}$ but improves the situation in the intermediate latent space $\mathcal{W}$, and the FID improves as well. This shows that even the traditional generator architecture performs better when we introduce an intermediate latent space that does not have to follow the distribution of the training data.

---

### النسخة العربية

هناك تعريفات مختلفة لفك الترابط، لكن الهدف المشترك هو فضاء كامن يتكون من فضاءات فرعية خطية، كل منها يتحكم في عامل واحد من عوامل التباين. ومع ذلك، يجب أن يتطابق احتمال أخذ العينات لكل مجموعة من العوامل في $\mathcal{Z}$ مع الكثافة المقابلة في بيانات التدريب. كما هو موضح في الشكل 6، هذا يمنع العوامل من أن تكون مفصولة بالكامل مع مجموعات البيانات النموذجية وتوزيعات الفضاء الكامن المدخل.

الفائدة الرئيسية من معمارية مولدنا هي أن الفضاء الكامن الوسيط $\mathcal{W}$ لا يحتاج إلى دعم أخذ العينات وفقاً لأي توزيع *ثابت*؛ يتم استحثاث كثافة أخذ العينات الخاصة به من خلال التعيين المستمر القطعي *المتعلم* $f(\mathbf{z})$. يمكن تكييف هذا التعيين "لفك التشوه" في $\mathcal{W}$ بحيث تصبح عوامل التباين أكثر خطية. نفترض أن هناك ضغطاً على المولد للقيام بذلك، لأنه ينبغي أن يكون من الأسهل توليد صور واقعية بناءً على تمثيل مفصول بدلاً من تمثيل مترابط. على هذا النحو، نتوقع أن يؤدي التدريب إلى $\mathcal{W}$ أقل ترابطاً في بيئة غير موجهة، أي عندما لا تكون عوامل التباين معروفة مسبقاً.

لسوء الحظ، تتطلب المقاييس المقترحة مؤخراً لقياس فك الترابط شبكة مشفر تعيّن الصور المدخلة إلى شفرات كامنة. هذه المقاييس غير مناسبة لأغراضنا لأن GAN الأساسي لدينا يفتقر إلى مثل هذا المشفر. بينما من الممكن إضافة شبكة إضافية لهذا الغرض، نريد تجنب استثمار الجهد في مكون ليس جزءاً من الحل الفعلي. لهذه الغاية، نصف طريقتين جديدتين لقياس فك الترابط، لا تتطلب أي منهما مشفراً أو عوامل تباين معروفة، وبالتالي يمكن حسابها لأي مجموعة بيانات صور ومولد.

## 4.1. طول المسار الإدراكي

كما لاحظ Laine، قد ينتج عن استيفاء متجهات الفضاء الكامن تغييرات غير خطية بشكل مفاجئ في الصورة. على سبيل المثال، قد تظهر ميزات غائبة في أي من نقطتي النهاية في منتصف مسار الاستيفاء الخطي. هذه علامة على أن الفضاء الكامن مترابط وأن عوامل التباين غير مفصولة بشكل صحيح. لقياس هذا التأثير، يمكننا قياس مدى التغيرات الجذرية التي تخضع لها الصورة بينما نقوم بالاستيفاء في الفضاء الكامن. بديهياً، يجب أن ينتج عن فضاء كامن أقل انحناءً انتقال أكثر سلاسة إدراكياً من فضاء كامن عالي الانحناء.

كأساس لمقياسنا، نستخدم مسافة صورة زوجية قائمة على الإدراك يتم حسابها كفرق موزون بين تضمينين من VGG16، حيث يتم ملاءمة الأوزان بحيث يتفق المقياس مع أحكام التشابه الإدراكي البشري. إذا قسمنا مسار استيفاء الفضاء الكامن إلى قطع خطية، يمكننا تعريف الطول الإدراكي الكلي لهذا المسار المقسم كمجموع الفروق الإدراكية على كل قطعة، كما هو مُبلغ عنه بواسطة مقياس مسافة الصورة. التعريف الطبيعي لطول المسار الإدراكي سيكون حد هذا المجموع في ظل تقسيم دقيق بشكل لا نهائي، لكننا في الممارسة نقاربه باستخدام إبسيلون تقسيم صغير $\epsilon=10^{-4}$. متوسط طول المسار الإدراكي في الفضاء الكامن $\mathcal{Z}$، على جميع نقاط النهاية المحتملة، هو إذن:

$$l_{\mathcal{Z}} = \mathbb{E}\left[\frac{1}{\epsilon^2}d\big(G(\mathrm{slerp}(\mathbf{z}_1,\mathbf{z}_2;t)), G(\mathrm{slerp}(\mathbf{z}_1,\mathbf{z}_2;t+\epsilon))\big)\right]$$

حيث $\mathbf{z}_1,\mathbf{z}_2\sim P(\mathbf{z}),t\sim U(0,1)$، $G$ هو المولد (أي $g \circ f$ للشبكات القائمة على الأنماط)، و $d(\cdot,\cdot)$ يقيّم المسافة الإدراكية بين الصور الناتجة. هنا $\mathrm{slerp}$ يشير إلى الاستيفاء الكروي، وهو الطريقة الأنسب للاستيفاء في فضاء الكامن المدخل المطبّع لدينا. للتركيز على ملامح الوجه بدلاً من الخلفية، نقص الصور المولدة لتحتوي فقط على الوجه قبل تقييم مقياس الصورة الزوجي. نظراً لأن المقياس $d$ تربيعي، نقسم على $\epsilon^2$. نحسب التوقع من خلال أخذ 100,000 عينة.

يتم إجراء حساب متوسط طول المسار الإدراكي في $\mathcal{W}$ بطريقة مماثلة:

$$l_{\mathcal{W}} = \mathbb{E}\left[\frac{1}{\epsilon^2}d\big(g(\mathrm{lerp}(f(\mathbf{z}_1),f(\mathbf{z}_2);t)), g(\mathrm{lerp}(f(\mathbf{z}_1),f(\mathbf{z}_2);t+\epsilon))\big)\right]$$

حيث الفرق الوحيد هو أن الاستيفاء يحدث في فضاء $\mathcal{W}$. نظراً لأن المتجهات في $\mathcal{W}$ غير مطبّعة بأي شكل، نستخدم الاستيفاء الخطي ($\mathrm{lerp}$).

يوضح الجدول 3 أن طول المسار الكامل هذا أقصر بشكل كبير لمولدنا القائم على الأنماط مع مدخلات الضوضاء، مما يشير إلى أن $\mathcal{W}$ أكثر خطية إدراكياً من $\mathcal{Z}$. ومع ذلك، هذا القياس في الواقع متحيز قليلاً لصالح فضاء الكامن المدخل $\mathcal{Z}$. إذا كان $\mathcal{W}$ في الواقع تعييناً مفصولاً و"مسطحاً" لـ $\mathcal{Z}$، فقد يحتوي على مناطق ليست على متعدد الشعب المدخل—وبالتالي يتم إعادة بنائها بشكل سيئ بواسطة المولد—حتى بين النقاط المعيّنة من متعدد الشعب المدخل، بينما فضاء الكامن المدخل $\mathcal{Z}$ ليس لديه مثل هذه المناطق بالتعريف. لذلك من المتوقع أنه إذا قصرنا مقياسنا على نقاط نهاية المسار، أي $t \in \{0,1\}$، يجب أن نحصل على $l_{\mathcal{W}}$ أصغر بينما $l_{\mathcal{Z}}$ لا يتأثر. هذا في الواقع ما نلاحظه في الجدول 3.

يوضح الجدول 4 كيف تتأثر أطوال المسارات بشبكة التعيين. نرى أن كلاً من المولدات التقليدية والقائمة على الأنماط تستفيد من وجود شبكة تعيين، والعمق الإضافي بشكل عام يحسّن طول المسار الإدراكي وكذلك مسافات FID. من المثير للاهتمام أنه بينما يتحسن $l_{\mathcal{W}}$ في المولد التقليدي، يصبح $l_{\mathcal{Z}}$ أسوأ بكثير، مما يوضح ادعاءنا أن فضاء الكامن المدخل يمكن أن يكون في الواقع مترابطاً بشكل تعسفي في GANs.

## 4.2. الانفصال الخطي

إذا كان الفضاء الكامن مفصولاً بما فيه الكفاية، يجب أن يكون من الممكن العثور على متجهات اتجاه تتوافق باستمرار مع عوامل تباين فردية. نقترح مقياساً آخر يقيس هذا التأثير من خلال قياس مدى إمكانية فصل نقاط الفضاء الكامن إلى مجموعتين متميزتين عبر مستوى فائق خطي، بحيث تتوافق كل مجموعة مع سمة ثنائية محددة للصورة.

من أجل تصنيف الصور المولدة، ندرب شبكات تصنيف مساعدة لعدد من السمات الثنائية، على سبيل المثال، للتمييز بين الوجوه الذكورية والأنثوية. في اختباراتنا، كان للمصنفات نفس معمارية المميز الذي نستخدمه (أي نفس معمارية Karras وآخرون)، وتم تدريبها باستخدام مجموعة بيانات CelebA-HQ التي تحتفظ بالسمات الأربعين المتوفرة في مجموعة بيانات CelebA الأصلية. لقياس انفصال سمة واحدة، نولد 200,000 صورة مع $\mathbf{z}\sim P(\mathbf{z})$ ونصنفها باستخدام شبكة التصنيف المساعدة. ثم نفرز العينات وفقاً لثقة المصنف ونزيل النصف الأقل ثقة، مما ينتج عنه 100,000 متجه فضاء كامن مُصنف.

لكل سمة، نلائم SVM خطي للتنبؤ بالتصنيف بناءً على نقطة الفضاء الكامن—$\mathbf{z}$ للتقليدي و $\mathbf{w}$ للقائم على الأنماط—ونصنف النقاط بواسطة هذا المستوى. ثم نحسب الإنتروبيا الشرطية $H(Y|X)$ حيث $X$ هي الفئات المتنبأ بها بواسطة SVM و $Y$ هي الفئات المحددة بواسطة المصنف المدرب مسبقاً. هذا يخبرنا بمقدار المعلومات الإضافية المطلوبة لتحديد الفئة الحقيقية للعينة، بالنظر إلى أننا نعرف على أي جانب من المستوى الفائق تقع. تشير القيمة المنخفضة إلى اتجاهات فضاء كامن متسقة لعامل (عوامل) التباين المقابل.

نحسب درجة الانفصال النهائية كـ $\exp(\sum_i H(Y_i|X_i))$، حيث $i$ يعدد السمات الأربعين. على غرار درجة الاستنتاج، يجلب الأس القيم من المجال اللوغاريتمي إلى المجال الخطي بحيث يكون من الأسهل مقارنتها.

تُظهر الجداول 3 و4 أن $\mathcal{W}$ قابل للفصل بشكل أفضل باستمرار من $\mathcal{Z}$، مما يشير إلى تمثيل أقل ترابطاً. علاوة على ذلك، فإن زيادة عمق شبكة التعيين يحسّن كلاً من جودة الصورة والانفصال في $\mathcal{W}$، مما يتماشى مع الفرضية القائلة بأن شبكة التوليد تفضل بطبيعتها تمثيل مدخل مفصول. من المثير للاهتمام أن إضافة شبكة تعيين أمام مولد تقليدي تؤدي إلى فقدان حاد في الانفصال في $\mathcal{Z}$ ولكنها تحسن الوضع في الفضاء الكامن الوسيط $\mathcal{W}$، ويتحسن FID أيضاً. هذا يوضح أنه حتى معمارية المولد التقليدية تؤدي بشكل أفضل عندما نقدم فضاء كامن وسيط لا يجب أن يتبع توزيع بيانات التدريب.

---

### Translation Notes

- **Figures referenced:** Figure 6 (disentanglement illustration), Table 3 (path length comparison), Table 4 (mapping network depth effects)
- **Key terms introduced:**
  - Linear subspaces (فضاءات فرعية خطية)
  - Piecewise continuous mapping (التعيين المستمر القطعي)
  - Unwarp (فك التشوه)
  - Spherical interpolation - slerp (الاستيفاء الكروي)
  - Linear interpolation - lerp (الاستيفاء الخطي)
  - VGG16 embeddings (تضمينات VGG16)
  - Input manifold (متعدد الشعب المدخل)
  - Linear hyperplane (مستوى فائق خطي)
  - Binary attribute (سمة ثنائية)
  - Auxiliary classification network (شبكة تصنيف مساعدة)
  - Conditional entropy (الإنتروبيا الشرطية)
  - Inception score (درجة الاستنتاج)
- **Equations:** 2 (perceptual path length formulas for Z and W spaces)
- **Citations:** References to Laine, Karras et al., VGG16, etc.
- **Special handling:** Mathematical formulations preserved, statistical notation maintained

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.86
