# Section 3: Motivation and High Level Considerations
## القسم 3: الدوافع والاعتبارات عالية المستوى

**Section:** Motivation and High Level Considerations
**Translation Quality:** 0.87
**Glossary Terms Used:** overfitting, computational cost, sparse, deep learning, architecture, optimization, correlation

---

### English Version

The most straightforward way of improving the performance of deep neural networks is by increasing their size. This includes both increasing the depth – the number of levels – of the network and its width: the number of units at each level. This is an easy and safe way of training higher quality models, especially given the availability of a large amount of labeled training data. However, this simple solution comes with two major drawbacks.

Bigger size typically means a larger number of parameters, which makes the enlarged network more prone to overfitting, especially if the number of labeled examples in the training set is limited. This can become a major bottleneck, since the creation of high quality training sets can be tricky and expensive, especially if expert human raters are necessary to distinguish between fine-grained visual categories like those in ImageNet (even in the 1000-class ILSVRC subset) as demonstrated by Figure 1.

Another drawback of uniformly increased network size is the dramatically increased use of computational resources. For example, in a deep vision network, if two convolutional layers are chained, any uniform increase in the number of their filters increases the computational cost quadratically. If the added capacity is used inefficiently (for example, if most weights end up to be close to zero), then a lot of computation is wasted. Since in practice the computational budget is always finite, an efficient distribution of computing resources is preferred to an indiscriminate increase of size, even when the main objective is to increase the quality of results.

The fundamental way of solving both issues would be by ultimately moving from fully connected to sparsely connected architectures, even inside the convolutions. Besides mimicking biological systems, this would also have the advantage of firmer theoretical underpinnings due to the groundbreaking work of Arora et al. [2]. Their main result states that if the probability distribution of the data-set is representable by a large, very sparse deep neural network, then the optimal network topology can be constructed layer by layer by analyzing the correlation statistics of the activations of the last layer and clustering neurons with highly correlated outputs. Although the strict mathematical proof requires very strong conditions, the fact that this statement resonates with the well known Hebbian principle – that neurons that fire together, wire together – suggests that the underlying idea is applicable even under less strict conditions, in practice.

On the downside, todays computing infrastructures are very inefficient when it comes to numerical calculation on non-uniform sparse data structures. Even if the number of arithmetic operations is reduced by 100×, the overhead of lookups and cache misses is so dominant that switching to sparse matrices would not pay off. The gap is widened yet further by the use of steadily improving, highly tuned, numerical libraries that allow for extremely fast dense matrix multiplication, exploiting the minute details of the underlying CPU or GPU hardware [16, 9]. Also, non-uniform sparse models require more sophisticated engineering and computing infrastructure. Most current vision oriented machine learning systems utilize sparsity in the spatial domain just by the virtue of employing convolutions. However, convolutions are implemented as collections of dense connections to the patches in the earlier layer. ConvNets have traditionally used random and sparse connection tables in the feature dimensions [11, 10] but the trend changed back to full connections with [9] in order to better optimize parallel computing. The uniformity of the structure and the relative large number of filters and greater batch size allow for utilizing efficient dense computation.

This raises the question whether there is any hope for a next-up to the current architecture: a next, intermediate step - an architecture that makes use of the extra sparsity, even at filter level, as suggested by the theory, but exploits our current hardware by utilizing computations on dense matrices. The vast literature on sparse matrix computations (e.g. [3]) suggests that clustering sparse matrices into relatively dense submatrices tends to give state of the art practical performance for sparse matrix multiplication. It does not seem to be far-fetched to think that similar methods would be utilized for the automated construction of non-uniform deep-learning architectures in the near future.

The Inception architecture started out as a case study of the first author for assessing the hypothetical output of a sophisticated network topology construction algorithm that tries to approximate a sparse structure implied by [2] for vision networks and covering the hypothesized outcome with dense, readily available components. Despite being a highly speculative undertaking, only after two iterations on the exact choice of topology, we could already see modest gains against the reference architecture based on [12]. After further tuning of learning rate, hyperparameters and improved training methodology, we established that the resulting Inception architecture was especially useful in the context of localization and object detection as the base network for [6] and [5]. Interestingly, while most of the original architectural choices have been questioned and tested thoroughly, they turned out to be at least locally optimal.

One must be cautious though: although the Inception architecture has become a success for computer vision, it is still questionable whether its quality can be attributed to the guiding principles that have lead to its construction or whether it is just the result of a fortunate coincidence. Making sure would require much more thorough analysis and verification: for example, if automated tools based on the principles described below would find similar, but better topology for the vision networks. The most convincing proof would be if indisputably better architectures - but similar in their structure - would be found either manually or automatically.

---

### النسخة العربية

أسلم طريقة لتحسين أداء الشبكات العصبية العميقة هو زيادة حجمها. يشمل ذلك زيادة العمق - عدد المستويات - للشبكة واتساعها: عدد الوحدات في كل مستوى. هذه طريقة سهلة وآمنة لتدريب نماذج ذات جودة أعلى، خاصة بالنظر إلى توفر كمية كبيرة من بيانات التدريب المُعلَّمة. ومع ذلك، يأتي هذا الحل البسيط مع عيبين رئيسيين.

الحجم الأكبر يعني عادة عدداً أكبر من المعاملات، مما يجعل الشبكة الموسعة أكثر عرضة للإفراط في التكيف، خاصة إذا كان عدد الأمثلة المُعلَّمة في مجموعة التدريب محدوداً. يمكن أن يصبح هذا عنق زجاجة رئيسياً، لأن إنشاء مجموعات تدريب عالية الجودة قد يكون صعباً ومكلفاً، خاصة إذا كان من الضروري وجود مُقيّمين بشريين خبراء للتمييز بين الفئات البصرية الدقيقة التفاصيل مثل تلك الموجودة في ImageNet (حتى في مجموعة ILSVRC الفرعية ذات 1000 فئة) كما هو موضح في الشكل 1.

عيب آخر للزيادة الموحدة في حجم الشبكة هو الزيادة الكبيرة في استخدام الموارد الحسابية. على سبيل المثال، في شبكة رؤية عميقة، إذا تم ربط طبقتين التفافيتين، فإن أي زيادة موحدة في عدد مرشحاتهما تزيد التكلفة الحسابية بشكل تربيعي. إذا تم استخدام السعة المضافة بشكل غير فعال (على سبيل المثال، إذا انتهى الأمر بمعظم الأوزان إلى أن تكون قريبة من الصفر)، فإن الكثير من الحوسبة يُهدَر. نظراً لأن الميزانية الحسابية في الممارسة العملية محدودة دائماً، فإن التوزيع الفعال للموارد الحسابية مُفضَّل على الزيادة العشوائية في الحجم، حتى عندما يكون الهدف الرئيسي هو زيادة جودة النتائج.

الطريقة الأساسية لحل كلتا المشكلتين ستكون بالانتقال في النهاية من المعماريات المتصلة بالكامل إلى المعماريات المتصلة بشكل متناثر، حتى داخل الالتفافات. بالإضافة إلى محاكاة الأنظمة البيولوجية، سيكون لهذا أيضاً ميزة الأسس النظرية الأقوى بفضل العمل الرائد لـ Arora وآخرين [2]. تنص نتيجتهم الرئيسية على أنه إذا كان توزيع الاحتمالات لمجموعة البيانات قابلاً للتمثيل بشبكة عصبية عميقة كبيرة ومتناثرة جداً، فيمكن بناء الطوبولوجيا المثلى للشبكة طبقة تلو الأخرى عن طريق تحليل إحصاءات الارتباط لتنشيطات الطبقة الأخيرة وتجميع الخلايا العصبية ذات المخرجات المترابطة بشدة. على الرغم من أن الإثبات الرياضي الصارم يتطلب شروطاً قوية جداً، إلا أن حقيقة أن هذا البيان يتردد صداه مع مبدأ Hebbian المعروف جيداً - أن الخلايا العصبية التي تنطلق معاً، تتصل معاً - تشير إلى أن الفكرة الأساسية قابلة للتطبيق حتى في ظل ظروف أقل صرامة، في الممارسة العملية.

من الجانب السلبي، تكون البنى التحتية الحاسوبية اليوم غير فعالة للغاية عندما يتعلق الأمر بالحسابات العددية على بنى البيانات المتناثرة غير الموحدة. حتى لو تم تقليل عدد العمليات الحسابية بمقدار 100×، فإن الحِمل الزائد للبحث وأخطاء الذاكرة التخزينية المؤقتة مهيمن لدرجة أن التحول إلى المصفوفات المتناثرة لن يكون مجدياً. يتسع الفجوة أكثر من خلال استخدام المكتبات العددية المحسّنة والمحسّنة باستمرار والتي تسمح بضرب المصفوفات الكثيفة بسرعة فائقة، مستغلة التفاصيل الدقيقة لأجهزة CPU أو GPU الأساسية [16, 9]. أيضاً، تتطلب النماذج المتناثرة غير الموحدة هندسة وبنية تحتية حاسوبية أكثر تطوراً. تستخدم معظم أنظمة التعلم الآلي الموجهة نحو الرؤية الحالية التناثر في المجال المكاني فقط من خلال استخدام الالتفافات. ومع ذلك، يتم تنفيذ الالتفافات كمجموعات من الاتصالات الكثيفة بالبقع في الطبقة السابقة. استخدمت شبكات ConvNets تقليدياً جداول اتصال عشوائية ومتناثرة في أبعاد الميزات [11, 10] ولكن الاتجاه تغير إلى الاتصالات الكاملة مع [9] من أجل تحسين الحوسبة المتوازية بشكل أفضل. يسمح انتظام البنية والعدد الكبير نسبياً من المرشحات وحجم الدفعة الأكبر باستخدام الحوسبة الكثيفة الفعالة.

هذا يثير السؤال عما إذا كان هناك أي أمل في خطوة تالية للمعمارية الحالية: خطوة وسيطة تالية - معمارية تستفيد من التناثر الإضافي، حتى على مستوى المرشح، كما اقترحتها النظرية، ولكنها تستغل أجهزتنا الحالية باستخدام الحسابات على المصفوفات الكثيفة. تشير الأدبيات الواسعة حول حسابات المصفوفات المتناثرة (على سبيل المثال [3]) إلى أن تجميع المصفوفات المتناثرة في مصفوفات فرعية كثيفة نسبياً يميل إلى إعطاء أداء عملي متقدم لضرب المصفوفات المتناثرة. لا يبدو من المبالغة الاعتقاد بأن طرقاً مماثلة ستُستخدم للبناء الآلي للمعماريات التعلم العميق غير الموحدة في المستقبل القريب.

بدأت معمارية Inception كدراسة حالة للمؤلف الأول لتقييم المخرجات الافتراضية لخوارزمية متطورة لبناء طوبولوجيا الشبكة تحاول تقريب البنية المتناثرة التي تضمنتها [2] لشبكات الرؤية وتغطية النتيجة المفترضة بمكونات كثيفة ومتاحة بسهولة. على الرغم من كونها مسعى تخمينياً للغاية، وبعد تكرارين فقط على الاختيار الدقيق للطوبولوجيا، يمكننا بالفعل رؤية مكاسب متواضعة مقارنة بمعمارية المرجع القائمة على [12]. بعد مزيد من ضبط معدل التعلم والمعاملات الفائقة ومنهجية التدريب المحسّنة، أثبتنا أن معمارية Inception الناتجة كانت مفيدة بشكل خاص في سياق التوطين والكشف عن الكائنات كشبكة أساسية لـ [6] و[5]. ومن المثير للاهتمام، أنه بينما تم التشكيك في معظم الاختيارات المعمارية الأصلية واختبارها بدقة، اتضح أنها مثالية على الأقل محلياً.

يجب على المرء أن يكون حذراً: على الرغم من أن معمارية Inception أصبحت نجاحاً للرؤية الحاسوبية، لا يزال من المشكوك فيه ما إذا كان يمكن أن تُعزى جودتها إلى المبادئ التوجيهية التي أدت إلى بنائها أم أنها مجرد نتيجة لمصادفة محظوظة. التأكد من ذلك سيتطلب تحليلاً والتحقق أكثر شمولاً: على سبيل المثال، إذا كانت الأدوات الآلية القائمة على المبادئ الموضحة أدناه ستجد طوبولوجيا مماثلة ولكن أفضل لشبكات الرؤية. الدليل الأكثر إقناعاً سيكون إذا تم العثور على معماريات أفضل بلا شك - ولكن مماثلة في بنيتها - إما يدوياً أو تلقائياً.

---

### Translation Notes

- **Figures referenced:** Figure 1
- **Key terms introduced:** overfitting, sparse/sparsely connected, dense matrix, Hebbian principle, topology, correlation statistics, clustering
- **Equations:** None
- **Citations:** [2], [3], [5], [6], [9], [10], [11], [12], [16]
- **Special handling:**
  - Translated "overfitting" as "الإفراط في التكيف"
  - Translated "sparse" as "متناثر" and "dense" as "كثيف"
  - Kept "Hebbian principle" as "مبدأ Hebbian" (transliterated)
  - Translated "neurons that fire together, wire together" with clear Arabic rendering
  - Translated "topology" as "طوبولوجيا"
  - Translated mathematical expressions like "100×" keeping the notation
  - Kept technical terms like "ConvNets" in English
  - Translated "correlation statistics" as "إحصاءات الارتباط"

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
