# Section 5: Experiments
## القسم 5: التجارب

**Section:** Experiments
**Translation Quality:** 0.86
**Glossary Terms Used:** baseline, speedup, timeout, test set, training, generalization, beam search, GRU, sequence-to-sequence

---

### English Version

In this section we report results from two categories of experiments. Our main experiments (Sect. 5.1) show that the LIPS framework can lead to significant performance gains in solving IPS by demonstrating such gains with DeepCoder. In Sect. 5.2 we illustrate the robustness of the method by demonstrating a strong kind of generalization ability across programs of different lengths.

#### 5.1 DeepCoder Compared to Baselines

We trained a neural network as described in Sect. 4.3 to predict used functions from input-output examples and constructed a test set of P = 500 programs, guaranteed to be semantically disjoint from all programs on which the neural network was trained (similarly to the equivalence check described in Sect. 4.2, we have ensured that all test programs behave differently from all programs used during training on at least one input). For each test program we generated M = 5 input-output examples involving integers of magnitudes up to 256, passed the examples to the trained neural network, and fed the obtained predictions to the search procedures from Sect. 4.4. We also considered a RNN-based decoder generating programs using beam search (see Sect. 5.3 for details).

To evaluate DeepCoder, we then recorded the time the search procedures needed to find a program consistent with the M input-output examples. As a baseline, we also ran all search procedures using a simple prior as function probabilities, computed from their global incidence in the program corpus.

**Table 1:** Search speedups on programs of length T = 3 due to using neural network predictions.

| Timeout needed to solve | DFS | | | Enumeration | | | λ2 | | | Sketch | | Beam |
|-------------------------|-----|-----|-----|-------------|-----|-----|-----|-----|-----|--------|-----|------|
| | 20% | 40% | 60% | 20% | 40% | 60% | 20% | 40% | 60% | 20% | 40% | 20% |
| Baseline | 41ms | 126ms | 314ms | 80ms | 335ms | 861ms | 18.9s | 49.6s | 84.2s | >10³s | >10³s | >10³s |
| DeepCoder | 2.7ms | 33ms | 110ms | 1.3ms | 6.1ms | 27ms | 0.23s | 0.52s | 13.5s | 2.13s | 455s | 292s |
| Speedup | 15.2× | 3.9× | 2.9× | 62.2× | 54.6× | 31.5× | 80.4× | 94.6× | 6.2× | >467× | >2.2× | >3.4× |

In the first, smaller-scale experiment (program search space size ~ 2 × 10⁶) we trained the neural network on programs of length T = 3, and the test programs were of the same length. Table 1 shows the per-task timeout required such that a solution could be found for given proportions of the test tasks (in time less than or equal to the timeout). For example, in a hypothetical test set with 4 tasks and runtimes of 3s, 2s, 1s, 4s, the timeout required to solve 50% of tasks would be 2s. More detailed experimental results are discussed in Appendix B.

In the main experiment, we tackled a large-scale problem of searching for programs consistent with input-output examples generated from programs of length T = 5 (search space size on the order of 10¹⁰), supported by a neural network trained with programs of shorter length T = 4. Here, we only consider P = 100 programs for reasons of computational efficiency, after having verified that this does not significantly affect the results in Table 1. The table in Fig. 3a shows significant speedups for DFS, Sort and add enumeration, and λ2 with Sort and add enumeration, the search techniques capable of solving the search problem in reasonable time frames. Note that Sort and add enumeration without the neural network (using prior probabilities of functions) exceeded the 10⁴ second timeout in two cases, so the relative speedups shown are crude lower bounds.

**Table in Fig. 3a:** Search speedups on programs of length T = 5

| Timeout needed to solve | DFS | | | Enumeration | | | λ2 |
|-------------------------|-----|-----|-----|-------------|-----|-----|-----|
| | 20% | 40% | 60% | 20% | 40% | 60% | 20% |
| Baseline | 163s | 2887s | 6832s | 8181s | >10⁴s | >10⁴s | 463s |
| DeepCoder | 24s | 514s | 2654s | 9s | 264s | 4640s | 48s |
| Speedup | 6.8× | 5.6× | 2.6× | 907× | >37× | >2× | 9.6× |

**Figure 3:** Search speedups on programs of length T = 5 and influence of length of training programs.

We hypothesize that the substantially larger performance gains on Sort and add schemes as compared to gains on DFS can be explained by the fact that the choice of attribute function (predicting presence of functions anywhere in the program) and learning objective of the neural network are better matched to the Sort and add schemes. Indeed, a more appropriate attribute function for DFS would be one that is more informative of the functions appearing early in the program, since exploring an incorrect first function is costly with DFS. On the other hand, the discussion in Sect. 4.5 provides theoretical indication that ignoring the correlations between functions is not cataclysmic for Sort and add enumeration, since a Rank loss that upper bounds the Sort and add runtime can still be minimized.

In Appendix G we analyse the performance of the neural networks used in these experiments, by investigating which attributes (program instructions) tend to be difficult to distinguish from each other.

#### 5.2 Generalization Across Program Lengths

To investigate the encoder's generalization ability across programs of different lengths, we trained a network to predict used functions from input-output examples that were generated from programs of length T_train ∈ {1, ..., 4}. We then used each of these networks to predict functions on 5 test sets containing input-output examples generated from programs of lengths T_test ∈ {1, ..., 5}, respectively. The test programs of a given length T were semantically disjoint from all training programs of the same length T and also from all training and test programs of shorter lengths T' < T.

For each of the combinations of T_train and T_test, Sort and add enumerative search was run both with and without using the neural network's predictions (in the latter case using prior probabilities) until it solved 20% of the test set tasks. Fig. 3b shows the relative speedup of the solver having access to predictions from the trained neural networks. These results indicate that the neural networks are able to generalize beyond programs of the same length that they were trained on. This is partly due to the search procedure on top of their predictions, which has the opportunity to correct for the presence of functions that the neural network failed to predict. Note that a sequence-to-sequence model trained on programs of a fixed length could not be expected to exhibit this kind of generalization ability.

#### 5.3 Alternative Models

**Encoder:** We evaluated replacing the feed-forward architecture encoder (Sect. 4.3) with an RNN, a natural baseline. Using a GRU-based RNN we were able to achieve results almost as good as using the feed-forward architecture, but found the RNN encoder more difficult to train.

**Decoder:** We also considered a purely neural network-based approach, where an RNN decoder is trained to predict the entire program token-by-token. We combined this with our feed-forward encoder by initializing the RNN using the pooled final layer of the encoder. We found it substantially more difficult to train an RNN decoder as compared to the independent binary classifiers employed above. Beam search was used to explore likely programs predicted by the RNN, but it only lead to a solution comparable with the other techniques when searching for programs of lengths T ≤ 2, where the search space size is very small (on the order of 10³). Note that using an RNN for both the encoder and decoder corresponds to a standard sequence-to-sequence model. However, we do not rule out that a more sophisticated RNN decoder or training procedure could be possibly more successful.

---

### النسخة العربية

في هذا القسم نبلغ عن نتائج من فئتين من التجارب. تُظهر تجاربنا الرئيسية (القسم 5.1) أن إطار LIPS يمكن أن يؤدي إلى مكاسب أداء كبيرة في حل IPS من خلال إظهار هذه المكاسب مع DeepCoder. في القسم 5.2 نوضح قوة الطريقة من خلال إظهار نوع قوي من قدرة التعميم عبر البرامج بأطوال مختلفة.

#### 5.1 DeepCoder مقارنة بخطوط الأساس

دربنا شبكة عصبية كما هو موضح في القسم 4.3 للتنبؤ بالدوال المستخدمة من أمثلة الإدخال والإخراج وأنشأنا مجموعة اختبار من P = 500 برنامج، مضمون أن تكون منفصلة دلالياً عن جميع البرامج التي تم تدريب الشبكة العصبية عليها (على غرار فحص التكافؤ الموضح في القسم 4.2، تأكدنا من أن جميع برامج الاختبار تتصرف بشكل مختلف عن جميع البرامج المستخدمة أثناء التدريب على مدخل واحد على الأقل). لكل برنامج اختبار قمنا بتوليد M = 5 أمثلة إدخال-إخراج تتضمن أعداداً صحيحة بقيم مطلقة تصل إلى 256، مررنا الأمثلة إلى الشبكة العصبية المدربة، وغذينا التنبؤات المحصل عليها إلى إجراءات البحث من القسم 4.4. اعتبرنا أيضاً فك تشفير قائم على RNN يولد البرامج باستخدام بحث الشعاع (انظر القسم 5.3 للتفاصيل).

لتقييم DeepCoder، سجلنا بعد ذلك الوقت الذي احتاجته إجراءات البحث للعثور على برنامج متسق مع أمثلة الإدخال والإخراج M. كخط أساس، قمنا أيضاً بتشغيل جميع إجراءات البحث باستخدام احتمال سابق بسيط كاحتماليات الدوال، محسوب من حدوثها العالمي في مدونة البرامج.

**الجدول 1:** تسريعات البحث على البرامج بطول T = 3 بسبب استخدام تنبؤات الشبكة العصبية.

| المهلة المطلوبة للحل | DFS | | | التعداد | | | λ2 | | | Sketch | | Beam |
|----------------------|-----|-----|-----|-------|-----|-----|-----|-----|-----|--------|-----|------|
| | 20% | 40% | 60% | 20% | 40% | 60% | 20% | 40% | 60% | 20% | 40% | 20% |
| خط الأساس | 41ms | 126ms | 314ms | 80ms | 335ms | 861ms | 18.9s | 49.6s | 84.2s | >10³s | >10³s | >10³s |
| DeepCoder | 2.7ms | 33ms | 110ms | 1.3ms | 6.1ms | 27ms | 0.23s | 0.52s | 13.5s | 2.13s | 455s | 292s |
| التسريع | 15.2× | 3.9× | 2.9× | 62.2× | 54.6× | 31.5× | 80.4× | 94.6× | 6.2× | >467× | >2.2× | >3.4× |

في التجربة الأولى ذات النطاق الأصغر (حجم فضاء بحث البرامج ~ 2 × 10⁶) دربنا الشبكة العصبية على برامج بطول T = 3، وكانت برامج الاختبار بنفس الطول. يُظهر الجدول 1 المهلة المطلوبة لكل مهمة بحيث يمكن العثور على حل لنسب معينة من مهام الاختبار (في وقت أقل من أو يساوي المهلة). على سبيل المثال، في مجموعة اختبار افتراضية بها 4 مهام وأوقات تشغيل 3s، 2s، 1s، 4s، ستكون المهلة المطلوبة لحل 50% من المهام هي 2s. تمت مناقشة النتائج التجريبية الأكثر تفصيلاً في الملحق B.

في التجربة الرئيسية، تعاملنا مع مشكلة واسعة النطاق للبحث عن برامج متسقة مع أمثلة الإدخال والإخراج المولدة من برامج بطول T = 5 (حجم فضاء البحث بترتيب 10¹⁰)، مدعومة بشبكة عصبية مدربة على برامج بطول أقصر T = 4. هنا، نعتبر فقط P = 100 برنامج لأسباب الكفاءة الحسابية، بعد التحقق من أن هذا لا يؤثر بشكل كبير على النتائج في الجدول 1. يُظهر الجدول في الشكل 3a تسريعات كبيرة لـ DFS، وتعداد الفرز والإضافة، و λ2 مع تعداد الفرز والإضافة، تقنيات البحث القادرة على حل مشكلة البحث في أطر زمنية معقولة. لاحظ أن تعداد الفرز والإضافة بدون الشبكة العصبية (باستخدام الاحتماليات السابقة للدوال) تجاوز مهلة 10⁴ ثانية في حالتين، لذا فإن التسريعات النسبية الموضحة هي حدود دنيا تقريبية.

**الجدول في الشكل 3a:** تسريعات البحث على البرامج بطول T = 5

| المهلة المطلوبة للحل | DFS | | | التعداد | | | λ2 |
|----------------------|-----|-----|-----|-------|-----|-----|-----|
| | 20% | 40% | 60% | 20% | 40% | 60% | 20% |
| خط الأساس | 163s | 2887s | 6832s | 8181s | >10⁴s | >10⁴s | 463s |
| DeepCoder | 24s | 514s | 2654s | 9s | 264s | 4640s | 48s |
| التسريع | 6.8× | 5.6× | 2.6× | 907× | >37× | >2× | 9.6× |

**الشكل 3:** تسريعات البحث على البرامج بطول T = 5 وتأثير طول برامج التدريب.

نفترض أن المكاسب الأكبر بكثير في الأداء على مخططات الفرز والإضافة مقارنة بالمكاسب على DFS يمكن تفسيرها بحقيقة أن اختيار دالة الخاصية (التنبؤ بوجود الدوال في أي مكان في البرنامج) وهدف التعلم للشبكة العصبية متطابقان بشكل أفضل مع مخططات الفرز والإضافة. في الواقع، دالة خاصية أكثر ملاءمة لـ DFS ستكون واحدة أكثر إفادة عن الدوال الظاهرة في وقت مبكر في البرنامج، حيث أن استكشاف دالة أولى غير صحيحة مكلف مع DFS. من ناحية أخرى، توفر المناقشة في القسم 4.5 إشارة نظرية إلى أن تجاهل الارتباطات بين الدوال ليس كارثياً لتعداد الفرز والإضافة، حيث أن خسارة الرتبة التي تحد من وقت تشغيل الفرز والإضافة لا تزال يمكن تصغيرها.

في الملحق G نحلل أداء الشبكات العصبية المستخدمة في هذه التجارب، من خلال التحقيق في الخصائص (تعليمات البرنامج) التي تميل إلى أن يكون من الصعب التمييز بينها.

#### 5.2 التعميم عبر أطوال البرامج

للتحقيق في قدرة المشفر على التعميم عبر البرامج بأطوال مختلفة، دربنا شبكة للتنبؤ بالدوال المستخدمة من أمثلة الإدخال والإخراج التي تم توليدها من برامج بطول T_train ∈ {1, ..., 4}. ثم استخدمنا كل من هذه الشبكات للتنبؤ بالدوال على 5 مجموعات اختبار تحتوي على أمثلة إدخال-إخراج مولدة من برامج بأطوال T_test ∈ {1, ..., 5}، على التوالي. كانت برامج الاختبار بطول معين T منفصلة دلالياً عن جميع برامج التدريب بنفس الطول T وأيضاً عن جميع برامج التدريب والاختبار بأطوال أقصر T' < T.

لكل من مجموعات T_train و T_test، تم تشغيل البحث التعدادي للفرز والإضافة سواء باستخدام تنبؤات الشبكة العصبية أو بدونها (في الحالة الأخيرة باستخدام الاحتماليات السابقة) حتى حل 20% من مهام مجموعة الاختبار. يُظهر الشكل 3b التسريع النسبي للحلال الذي له وصول إلى تنبؤات من الشبكات العصبية المدربة. تشير هذه النتائج إلى أن الشبكات العصبية قادرة على التعميم إلى ما هو أبعد من البرامج بنفس الطول التي تم تدريبها عليها. يرجع هذا جزئياً إلى إجراء البحث فوق تنبؤاتها، والذي لديه فرصة للتصحيح لوجود الدوال التي فشلت الشبكة العصبية في التنبؤ بها. لاحظ أن نموذج تسلسل إلى تسلسل مدرب على برامج بطول ثابت لا يمكن أن يُتوقع منه إظهار هذا النوع من قدرة التعميم.

#### 5.3 النماذج البديلة

**المشفر:** قيمنا استبدال مشفر معمارية التغذية الأمامية (القسم 4.3) بـ RNN، وهو خط أساس طبيعي. باستخدام RNN قائم على GRU تمكنا من تحقيق نتائج جيدة تقريباً مثل استخدام معمارية التغذية الأمامية، لكننا وجدنا أن مشفر RNN أكثر صعوبة في التدريب.

**فك التشفير:** اعتبرنا أيضاً نهجاً قائماً على الشبكات العصبية بحتة، حيث يتم تدريب فك تشفير RNN للتنبؤ بالبرنامج بالكامل رمزاً تلو الآخر. جمعنا هذا مع مشفر التغذية الأمامية الخاص بنا من خلال تهيئة RNN باستخدام الطبقة النهائية المجمعة للمشفر. وجدنا أنه من الصعب بشكل كبير تدريب فك تشفير RNN مقارنة بالمصنفات الثنائية المستقلة المستخدمة أعلاه. تم استخدام بحث الشعاع لاستكشاف البرامج المحتملة التي تنبأت بها RNN، لكنه لم يؤدِ إلا إلى حل مماثل للتقنيات الأخرى عند البحث عن برامج بأطوال T ≤ 2، حيث يكون حجم فضاء البحث صغيراً جداً (بترتيب 10³). لاحظ أن استخدام RNN لكل من المشفر وفك التشفير يتوافق مع نموذج تسلسل إلى تسلسل قياسي. ومع ذلك، لا نستبعد أن فك تشفير RNN أكثر تطوراً أو إجراء تدريب قد يكون أكثر نجاحاً.

---

### Translation Notes

- **Key terms introduced:**
  - test set = مجموعة اختبار
  - baseline = خط الأساس
  - speedup = تسريع
  - timeout = مهلة
  - beam search = بحث الشعاع
  - generalization = التعميم
  - GRU (Gated Recurrent Unit) = GRU (kept as transliteration)
  - sequence-to-sequence = تسلسل إلى تسلسل
  - token-by-token = رمزاً تلو الآخر

- **Tables:** Table 1 and table in Fig. 3a with experimental results
- **Figures referenced:** Figure 3 (search speedups and generalization)
- **Mathematical notation:** Preserved (T = 3, T = 5, P = 500, M = 5, 10⁶, 10¹⁰, etc.)
- **Citations:** References to appendices (Appendix B, Appendix G)
- **Special handling:** Preserved experimental data in tables with Arabic headers

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
