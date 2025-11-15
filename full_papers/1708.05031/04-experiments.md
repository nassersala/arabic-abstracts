# Section 4: Experiments
## القسم 4: التجارب

**Section:** experiments
**Translation Quality:** 0.87
**Glossary Terms Used:** dataset, evaluation, baseline, performance, metric, Hit Ratio, NDCG, implicit feedback, negative sampling, loss function, deep learning, architecture, hyperparameter, optimization, validation

---

### English Version

We conduct experiments to answer the following research questions:

**RQ1:** Do our proposed NCF methods outperform the state-of-the-art implicit collaborative filtering methods?
**RQ2:** How does our proposed optimization framework (log loss with negative sampling) work for the recommendation task?
**RQ3:** Are deeper layers of hidden units helpful for learning from user-item interaction data?

#### 4.1 Experimental Settings

**Datasets.** We experimented with two publicly accessible datasets: MovieLens and Pinterest. As MovieLens is a rating dataset with explicit feedback (rating scores ranging from 1 to 5), we transform it into implicit data, retaining only the observed entries and marking them all as 1s (indicating the user has interacted with the item), otherwise 0s (indicating the user has not interacted with the item). This leads to 1,000,209 interactions in total. Pinterest is a real-world implicit dataset collected from Pinterest interest boards; we use a subset that contains 1,500,809 interactions from 55,187 users and 9,916 items.

Statistics of the two datasets are summarized in Table 1:

| Dataset | #Interactions | #Items | #Users | Sparsity |
|---------|---------------|--------|--------|----------|
| MovieLens | 1,000,209 | 3,706 | 6,040 | 95.53% |
| Pinterest | 1,500,809 | 9,916 | 55,187 | 99.73% |

**Evaluation Protocols.** To evaluate the performance of item recommendation, we adopted the leave-one-out evaluation, which has been widely used for evaluating the performance of implicit collaborative filtering. Specifically, we held out the latest interaction of each user as the test set and utilized the remaining data for training. Since it is too time-consuming to rank all items for every user during evaluation, we followed the common strategy that randomly samples 100 items that are not interacted by the user, ranking the test item among the 100 items. The performance of a ranked list is judged by Hit Ratio (HR) and Normalized Discounted Cumulative Gain (NDCG). Without loss of generality, we truncated the ranked list at 10 for both metrics. As such, the HR intuitively measures whether the test item is present on the top-10 list, and the NDCG accounts for the position of the hit by assigning higher scores to hits at top ranks.

**Baselines.** We compared NCF methods with the following methods:
- **ItemPop.** Items are ranked by their popularity judged by the number of interactions. This is a non-personalized method that is used to test whether a recommendation method can beat non-personalized baselines.
- **ItemKNN.** This is the standard item-based collaborative filtering method.
- **BPR.** BPR optimizes MF with a pairwise ranking loss and is a highly competitive baseline for item recommendation. We set the learning rate to 0.05, regularization to 0.0025, and randomly sample one negative instance per positive instance.
- **eALS.** This is a state-of-the-art MF method that optimizes the squared loss. As a pointwise approach, it is a counterpart of our proposed NCF methods in terms of the learning methodology. We set the weight of negative instances to 0.01, as recommended by the original authors.

For the first two baselines, we obtained performance using the MyMediaLite library. We implemented the last two methods by ourselves as described in the original papers.

**Parameter Settings.** We implemented all NCF methods including GMF, MLP and NeuMF with Keras. To determine the hyper-parameters of the NCF methods, we randomly sampled one interaction for each user as the validation data, tuning hyper-parameters on it and using the remaining data for training. We tested all methods by initializing model parameters with a Gaussian distribution (with a mean of 0 and standard deviation of 0.01). We optimized all methods with the log loss and employed mini-batch Adam, which adapts learning rate for each parameter according to historical gradient information. We tested the batch size of [128, 256, 512, 1024] and the learning rate of [0.0001, 0.0005, 0.001, 0.005]. We empirically set the number of predictive factors to [8, 16, 32, 64]. For MLP, we tested the tower structure outlined in Section 3.3, e.g., for the predictive factor of 32 with 3 layers, the MLP architecture is 64→32→16→8. To have a fair comparison, we set the predictive factor of NeuMF as half of GMF and MLP, since NeuMF concatenates the two parts as the final hidden layer. As for regularization, we tested the L2 regularization and found it unhelpful for model performance. Presumably, this is owing to the inherent dropout-like effect of negative sampling, which has the regularization effect of preventing overfitting. For each positive instance, we randomly sampled four negative instances from items not interacted by the user.

#### 4.2 Performance Comparison (RQ1)

Table 2 summarizes the performance of all methods. We show the best performance of eALS and BPR obtained from a variety of predictive factors and do not report ItemPop and ItemKNN since their performance is much lower and not competitive.

From Table 2, we can observe that: (1) NeuMF achieves the best performance on both datasets with significant improvements over other methods. Compared to eALS, our best method achieves a relative improvement of 4.5% on MovieLens and 4.9% on Pinterest for HR@10 on average. (2) Among the three NCF methods, MLP shows the lowest performance, which is even slightly weaker than GMF on Pinterest. We believe the main reason is that MLP does not use pre-training and random initialization plays an important role in the performance. (3) GMF consistently outperforms BPR, which shares the same model structure with GMF but optimizes a pairwise ranking loss. This highlights the effectiveness of classification-aware log loss for implicit collaborative filtering. (4) NeuMF with a small predictive factor of 8 substantially outperforms that of eALS and BPR with a large factor of 64. This demonstrates the high expressiveness of NeuMF in learning the user-item interaction function.

To provide more insight, we plot the performance of HR@K and NDCG@K with respect to K for the best predictive factor (i.e., 16) in Figures 4 and 5, respectively. It is clear that our NeuMF consistently outperforms other methods for all ranking positions. Moreover, the improvements are statistically significant by performing a paired t-test (with p-value smaller than 0.01).

##### 4.2.1 Utility of Pre-training

Recall that to train NeuMF, we employ a pre-training strategy that initializes NeuMF with pre-trained GMF and MLP. To justify the utility of pre-training, we compare the performance of NeuMF with and without pre-training. Table 2 shows the results, where we can see that pre-training brings in a relative improvement of 2.2% for MovieLens and 1.1% for Pinterest on HR@10. The performance gain on NDCG@10 is even larger. This demonstrates the effectiveness of the pre-training strategy for deep neural network models like NeuMF. We stress that, beyond performance improvement, pre-training also provides a principled way to initialize the parameters of deep learning models, which is of independent interest.

To give more details, we initialized NeuMF's GMF and MLP parts with the pre-trained models of Section 4.2, concatenating the output layer weights with: $\mathbf{h} \leftarrow [\alpha \mathbf{h}^{GMF}, (1-\alpha) \mathbf{h}^{MLP}]^T$, where we set $\alpha = 0.5$ to allow equal importance of GMF and MLP. We then trained NeuMF with vanilla SGD by fixing the learning rate to 0.001 (smaller values like 0.0001 led to very slow convergence).

#### 4.3 Log Loss with Negative Sampling (RQ2)

Having shown the high effectiveness of our NCF methods, we now investigate the second research question concerning the optimization framework. To this end, we show the training loss on the training data and the recommendation performance (HR@10) on the test data with respect to the number of training iterations in Figure 6. As we can see, the training loss keeps decreasing and converging for both datasets. Meanwhile, the recommendation performance increases quickly at the first few iterations and becomes stable after about 10 iterations. This shows that log loss is appropriate and effective for optimizing the recommendation task with implicit feedback.

We further investigate the impact of negative sampling ratio (i.e., the number of negative instances per positive instance). Figure 7 plots the performance w.r.t. the sampling ratio from 1 to 7. On both datasets, we see that just sampling one negative instance is insufficient to achieve optimal performance. Sampling more (e.g., 3 to 6) negative instances leads to consistently better performance. For MovieLens, the performance keeps increasing when we sample more negative instances; for Pinterest, the performance achieves the peak at the sampling ratio of 6 and becomes worse afterwards. This may indicate that a too large sampling ratio may be adversarial for model learning. Overall, the results empirically verify that pointwise log loss — which allows a flexible sampling ratio — is more suitable than pairwise log loss for learning from implicit feedback data.

#### 4.4 Is Deep Learning Helpful? (RQ3)

Lastly, we address the key research question — whether deep learning, specifically the multiple non-linear layers, is helpful for learning the user-item interaction function. To this end, we vary the number of hidden layers for the MLP model from 0 to 4. Note that MLP-0 corresponds to the variant without any hidden layer (i.e., the concatenation of user and item embeddings is directly projected to the predicted score). Figure 8 shows the performance of MLP with respect to the number of hidden layers.

As can be seen, stacking more layers brings consistent performance improvements. Specifically, the MLP-0 method performs rather poorly, even weaker than ItemPop which is a non-personalized method (HR@10 of 0.452 vs. 0.495 on MovieLens and 0.275 vs. 0.479 on Pinterest). This result demonstrates that simply concatenating user and item latent vectors is insufficient and some layers of non-linear transformations are necessary to reveal the complex user-item interaction patterns. In terms of the number of layers, we observe that three hidden layers perform the best on both datasets, and stacking more layers does not bring obvious improvement. This may suggest that for this particular problem of top-N recommendation, a relatively shallow architecture is sufficient. We leave more investigation as future work.

Table 3 shows the detailed performance comparison between MLP-0 to MLP-4 with different predictive factors on both datasets:

| Factors | MLP-0 | MLP-1 | MLP-2 | MLP-3 | MLP-4 |
|---------|-------|-------|-------|-------|-------|
| MovieLens HR@10 (8) | 0.452 | 0.628 | 0.655 | 0.671 | 0.678 |
| MovieLens NDCG@10 (8) | 0.268 | 0.373 | 0.391 | 0.403 | 0.410 |
| Pinterest HR@10 (8) | 0.275 | 0.848 | 0.855 | 0.859 | 0.862 |
| Pinterest NDCG@10 (8) | 0.142 | 0.510 | 0.518 | 0.522 | 0.525 |

---

### النسخة العربية

نجري تجارب للإجابة على أسئلة البحث التالية:

**سؤال البحث 1:** هل تتفوق طرق NCF المقترحة على أحدث طرق التصفية التعاونية الضمنية؟
**سؤال البحث 2:** كيف يعمل إطار التحسين المقترح (خسارة اللوغاريتم مع أخذ العينات السلبية) لمهمة التوصية؟
**سؤال البحث 3:** هل الطبقات الأعمق من الوحدات المخفية مفيدة للتعلم من بيانات تفاعل المستخدم والعنصر؟

#### 4.1 إعدادات التجارب

**مجموعات البيانات.** أجرينا تجارب على مجموعتي بيانات متاحتين للعامة: MovieLens و Pinterest. نظراً لأن MovieLens هي مجموعة بيانات تقييم مع تغذية راجعة صريحة (درجات تقييم تتراوح من 1 إلى 5)، نحولها إلى بيانات ضمنية، محتفظين فقط بالإدخالات الملاحظة ونضع علامة عليها جميعاً بـ 1 (تشير إلى أن المستخدم قد تفاعل مع العنصر)، وإلا 0 (تشير إلى أن المستخدم لم يتفاعل مع العنصر). هذا يؤدي إلى 1,000,209 تفاعل في المجموع. Pinterest هي مجموعة بيانات ضمنية من العالم الحقيقي تم جمعها من لوحات اهتمامات Pinterest؛ نستخدم مجموعة فرعية تحتوي على 1,500,809 تفاعل من 55,187 مستخدم و 9,916 عنصر.

يتم تلخيص إحصاءات مجموعتي البيانات في الجدول 1:

| مجموعة البيانات | عدد التفاعلات | عدد العناصر | عدد المستخدمين | التناثر |
|-----------------|---------------|-------------|----------------|---------|
| MovieLens | 1,000,209 | 3,706 | 6,040 | 95.53% |
| Pinterest | 1,500,809 | 9,916 | 55,187 | 99.73% |

**بروتوكولات التقييم.** لتقييم أداء توصية العناصر، اعتمدنا تقييم إخراج واحد، والذي تم استخدامه على نطاق واسع لتقييم أداء التصفية التعاونية الضمنية. على وجه التحديد، احتفظنا بأحدث تفاعل لكل مستخدم كمجموعة اختبار واستخدمنا البيانات المتبقية للتدريب. نظراً لأنه يستغرق وقتاً طويلاً جداً لترتيب جميع العناصر لكل مستخدم أثناء التقييم، اتبعنا الاستراتيجية الشائعة التي تأخذ عينات عشوائياً من 100 عنصر لم يتفاعل معها المستخدم، وترتيب عنصر الاختبار بين 100 عنصر. يتم الحكم على أداء القائمة المرتبة من خلال نسبة النجاح (HR) والمكسب التراكمي المخفض المُطبَّع (NDCG). دون فقدان العمومية، قطعنا القائمة المرتبة عند 10 لكلا المقياسين. على هذا النحو، تقيس HR بشكل حدسي ما إذا كان عنصر الاختبار موجوداً في قائمة أفضل 10، وتأخذ NDCG في الاعتبار موضع النجاح من خلال تعيين درجات أعلى للنجاحات في المراتب العليا.

**خطوط الأساس.** قارنا طرق NCF بالطرق التالية:
- **ItemPop.** يتم ترتيب العناصر حسب شعبيتها المحكوم عليها من خلال عدد التفاعلات. هذه طريقة غير شخصية تُستخدم لاختبار ما إذا كانت طريقة التوصية يمكنها التفوق على خطوط الأساس غير الشخصية.
- **ItemKNN.** هذه هي طريقة التصفية التعاونية القياسية القائمة على العنصر.
- **BPR.** يحسّن BPR تحليل المصفوفات مع خسارة ترتيب زوجي وهو خط أساس تنافسي للغاية لتوصية العنصر. قمنا بتعيين معدل التعلم إلى 0.05، والتنظيم إلى 0.0025، وأخذ عينات عشوائياً من حالة سلبية واحدة لكل حالة إيجابية.
- **eALS.** هذه طريقة تحليل مصفوفات حديثة تحسّن الخسارة التربيعية. كنهج نقطي، فهي نظير لطرق NCF المقترحة من حيث منهجية التعلم. قمنا بتعيين وزن الحالات السلبية إلى 0.01، كما أوصى به المؤلفون الأصليون.

بالنسبة لخطي الأساس الأولين، حصلنا على الأداء باستخدام مكتبة MyMediaLite. قمنا بتنفيذ الطريقتين الأخيرتين بأنفسنا كما هو موضح في الأوراق الأصلية.

**إعدادات المعاملات.** قمنا بتنفيذ جميع طرق NCF بما في ذلك GMF و MLP و NeuMF باستخدام Keras. لتحديد المعاملات الفائقة لطرق NCF، أخذنا عينات عشوائياً من تفاعل واحد لكل مستخدم كبيانات التحقق، وضبط المعاملات الفائقة عليها واستخدام البيانات المتبقية للتدريب. اختبرنا جميع الطرق من خلال تهيئة معاملات النموذج بتوزيع غاوسي (بمتوسط 0 وانحراف معياري 0.01). قمنا بتحسين جميع الطرق بخسارة اللوغاريتم واستخدمنا Adam المصغر الدفعي، الذي يكيف معدل التعلم لكل معامل وفقاً لمعلومات التدرج التاريخية. اختبرنا حجم الدفعة [128، 256، 512، 1024] ومعدل التعلم [0.0001، 0.0005، 0.001، 0.005]. قمنا تجريبياً بتعيين عدد العوامل التنبؤية إلى [8، 16، 32، 64]. بالنسبة لـ MLP، اختبرنا بنية البرج الموضحة في القسم 3.3، على سبيل المثال، للعامل التنبؤي 32 مع 3 طبقات، تكون معمارية MLP 64→32→16→8. للحصول على مقارنة عادلة، قمنا بتعيين العامل التنبؤي لـ NeuMF على أنه نصف GMF و MLP، نظراً لأن NeuMF يدمج الجزأين كطبقة مخفية نهائية. أما بالنسبة للتنظيم، اختبرنا تنظيم L2 ووجدناه غير مفيد لأداء النموذج. يفترض أن هذا يرجع إلى تأثير شبيه بـ dropout الكامن في أخذ العينات السلبية، والذي له تأثير تنظيمي لمنع الإفراط في التلاؤم. لكل حالة إيجابية، أخذنا عينات عشوائياً من أربع حالات سلبية من العناصر التي لم يتفاعل معها المستخدم.

#### 4.2 مقارنة الأداء (سؤال البحث 1)

يلخص الجدول 2 أداء جميع الطرق. نعرض أفضل أداء لـ eALS و BPR الذي تم الحصول عليه من مجموعة متنوعة من العوامل التنبؤية ولا نبلغ عن ItemPop و ItemKNN نظراً لأن أدائهما أقل بكثير وغير تنافسي.

من الجدول 2، يمكننا ملاحظة ما يلي: (1) تحقق NeuMF أفضل أداء على كلتا مجموعتي البيانات مع تحسينات كبيرة على الطرق الأخرى. بالمقارنة مع eALS، تحقق أفضل طريقة لدينا تحسيناً نسبياً بنسبة 4.5% على MovieLens و 4.9% على Pinterest لـ HR@10 في المتوسط. (2) من بين طرق NCF الثلاث، يُظهر MLP أقل أداء، وهو أضعف قليلاً حتى من GMF على Pinterest. نعتقد أن السبب الرئيسي هو أن MLP لا يستخدم التدريب المسبق والتهيئة العشوائية تلعب دوراً مهماً في الأداء. (3) يتفوق GMF باستمرار على BPR، الذي يشترك في نفس بنية النموذج مع GMF ولكنه يحسّن خسارة ترتيب زوجي. هذا يسلط الضوء على فعالية خسارة اللوغاريتم الواعية بالتصنيف للتصفية التعاونية الضمنية. (4) يتفوق NeuMF بعامل تنبؤي صغير من 8 بشكل كبير على eALS و BPR بعامل كبير من 64. هذا يوضح التعبيرية العالية لـ NeuMF في تعلم دالة تفاعل المستخدم والعنصر.

لتوفير المزيد من الفهم، نرسم أداء HR@K و NDCG@K فيما يتعلق بـ K لأفضل عامل تنبؤي (أي 16) في الشكلين 4 و 5، على التوالي. من الواضح أن NeuMF يتفوق باستمرار على الطرق الأخرى لجميع مواضع الترتيب. علاوة على ذلك، التحسينات ذات دلالة إحصائية من خلال إجراء اختبار t المزدوج (بقيمة p أصغر من 0.01).

##### 4.2.1 فائدة التدريب المسبق

تذكر أنه لتدريب NeuMF، نستخدم استراتيجية تدريب مسبق تهيئ NeuMF بـ GMF و MLP المدربين مسبقاً. لتبرير فائدة التدريب المسبق، نقارن أداء NeuMF مع وبدون التدريب المسبق. يُظهر الجدول 2 النتائج، حيث يمكننا أن نرى أن التدريب المسبق يجلب تحسيناً نسبياً بنسبة 2.2% لـ MovieLens و 1.1% لـ Pinterest على HR@10. المكسب في الأداء على NDCG@10 أكبر حتى. هذا يوضح فعالية استراتيجية التدريب المسبق لنماذج الشبكات العصبية العميقة مثل NeuMF. نؤكد أنه، بخلاف تحسين الأداء، يوفر التدريب المسبق أيضاً طريقة منهجية لتهيئة معاملات نماذج التعلم العميق، وهو أمر ذو اهتمام مستقل.

لإعطاء المزيد من التفاصيل، قمنا بتهيئة أجزاء GMF و MLP في NeuMF بالنماذج المدربة مسبقاً من القسم 4.2، ودمج أوزان طبقة الإخراج بـ: $\mathbf{h} \leftarrow [\alpha \mathbf{h}^{GMF}, (1-\alpha) \mathbf{h}^{MLP}]^T$، حيث قمنا بتعيين $\alpha = 0.5$ للسماح بأهمية متساوية لـ GMF و MLP. ثم قمنا بتدريب NeuMF باستخدام SGD الفانيليا من خلال تثبيت معدل التعلم على 0.001 (القيم الأصغر مثل 0.0001 أدت إلى تقارب بطيء جداً).

#### 4.3 خسارة اللوغاريتم مع أخذ العينات السلبية (سؤال البحث 2)

بعد أن أظهرنا الفعالية العالية لطرق NCF، نحقق الآن في سؤال البحث الثاني المتعلق بإطار التحسين. لهذه الغاية، نعرض خسارة التدريب على بيانات التدريب وأداء التوصية (HR@10) على بيانات الاختبار فيما يتعلق بعدد التكرارات التدريبية في الشكل 6. كما نرى، تستمر خسارة التدريب في الانخفاض والتقارب لكلتا مجموعتي البيانات. في الوقت نفسه، يزداد أداء التوصية بسرعة في التكرارات القليلة الأولى ويصبح مستقراً بعد حوالي 10 تكرارات. هذا يُظهر أن خسارة اللوغاريتم مناسبة وفعالة لتحسين مهمة التوصية مع التغذية الراجعة الضمنية.

نحقق أيضاً في تأثير نسبة أخذ العينات السلبية (أي عدد الحالات السلبية لكل حالة إيجابية). يرسم الشكل 7 الأداء فيما يتعلق بنسبة أخذ العينات من 1 إلى 7. على كلتا مجموعتي البيانات، نرى أن مجرد أخذ عينة من حالة سلبية واحدة غير كافٍ لتحقيق الأداء الأمثل. أخذ عينات أكثر (على سبيل المثال، 3 إلى 6) من الحالات السلبية يؤدي إلى أداء أفضل باستمرار. بالنسبة لـ MovieLens، يستمر الأداء في الزيادة عندما نأخذ عينات من المزيد من الحالات السلبية؛ بالنسبة لـ Pinterest، يحقق الأداء الذروة عند نسبة أخذ العينات 6 ويصبح أسوأ بعد ذلك. قد يشير هذا إلى أن نسبة أخذ العينات الكبيرة جداً قد تكون ضارة لتعلم النموذج. بشكل عام، تتحقق النتائج تجريبياً من أن خسارة اللوغاريتم النقطية — التي تسمح بنسبة أخذ عينات مرنة — أكثر ملاءمة من خسارة اللوغاريتم الزوجية للتعلم من بيانات التغذية الراجعة الضمنية.

#### 4.4 هل التعلم العميق مفيد؟ (سؤال البحث 3)

أخيراً، نتناول سؤال البحث الرئيسي — ما إذا كان التعلم العميق، وتحديداً الطبقات غير الخطية المتعددة، مفيداً لتعلم دالة تفاعل المستخدم والعنصر. لهذه الغاية، نغير عدد الطبقات المخفية لنموذج MLP من 0 إلى 4. لاحظ أن MLP-0 يتوافق مع المتغير بدون أي طبقة مخفية (أي يتم إسقاط دمج تضمينات المستخدم والعنصر مباشرة على الدرجة المتوقعة). يُظهر الشكل 8 أداء MLP فيما يتعلق بعدد الطبقات المخفية.

كما يمكن ملاحظته، فإن تكديس المزيد من الطبقات يجلب تحسينات أداء متسقة. على وجه التحديد، تؤدي طريقة MLP-0 بشكل ضعيف إلى حد ما، حتى أضعف من ItemPop وهي طريقة غير شخصية (HR@10 من 0.452 مقابل 0.495 على MovieLens و 0.275 مقابل 0.479 على Pinterest). هذه النتيجة توضح أن مجرد دمج متجهات المستخدم والعنصر الكامنة غير كافٍ وبعض طبقات التحويلات غير الخطية ضرورية للكشف عن أنماط تفاعل المستخدم والعنصر المعقدة. من حيث عدد الطبقات، نلاحظ أن ثلاث طبقات مخفية تؤدي بشكل أفضل على كلتا مجموعتي البيانات، وتكديس المزيد من الطبقات لا يجلب تحسيناً واضحاً. قد يشير هذا إلى أنه لهذه المشكلة بالذات للتوصية بأعلى N، فإن المعمارية الضحلة نسبياً كافية. نترك المزيد من التحقيق كعمل مستقبلي.

يُظهر الجدول 3 مقارنة الأداء التفصيلية بين MLP-0 إلى MLP-4 بعوامل تنبؤية مختلفة على كلتا مجموعتي البيانات:

| العوامل | MLP-0 | MLP-1 | MLP-2 | MLP-3 | MLP-4 |
|---------|-------|-------|-------|-------|-------|
| MovieLens HR@10 (8) | 0.452 | 0.628 | 0.655 | 0.671 | 0.678 |
| MovieLens NDCG@10 (8) | 0.268 | 0.373 | 0.391 | 0.403 | 0.410 |
| Pinterest HR@10 (8) | 0.275 | 0.848 | 0.855 | 0.859 | 0.862 |
| Pinterest NDCG@10 (8) | 0.142 | 0.510 | 0.518 | 0.522 | 0.525 |

---

### Translation Notes

- **Figures referenced:** Figures 4, 5 (performance plots), Figure 6 (training loss and performance), Figure 7 (negative sampling ratio impact), Figure 8 (depth analysis)
- **Tables referenced:** Table 1 (dataset statistics), Table 2 (performance comparison), Table 3 (depth comparison)
- **Key terms introduced:**
  - Leave-one-out evaluation
  - Hit Ratio (HR@10)
  - Normalized Discounted Cumulative Gain (NDCG@10)
  - ItemPop, ItemKNN, BPR, eALS (baseline methods)
  - Negative sampling ratio
  - Pre-training strategy
  - Tower structure
- **Equations:** Pre-training weight formula
- **Citations:** References to MyMediaLite library and original papers
- **Special handling:**
  - Dataset names (MovieLens, Pinterest) kept in English
  - Method names (GMF, MLP, NeuMF, BPR, eALS) kept as acronyms
  - Metrics (HR, NDCG) kept as acronyms with Arabic explanations
  - Statistical significance (p-value) notation preserved
  - Hyperparameter values preserved in original form
  - Table structure maintained in both languages

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87
