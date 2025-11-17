# Section 2: Related Work
## القسم 2: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.86
**Glossary Terms Used:** التنبؤ بالمجموعات (set prediction), المطابقة الثنائية (bipartite matching), مشفر-فك تشفير (encoder-decoder), محول (transformer), فك التشفير المتوازي (parallel decoding), كشف الأجسام (object detection), آلية الانتباه (attention mechanism), الانتباه الذاتي (self-attention), قمع عدم الحد الأقصى (non-maximum suppression), المراسي (anchors), انحداري ذاتي (autoregressive)

---

### English Version

Our work build on prior work in several domains: bipartite matching losses for set prediction, encoder-decoder architectures based on the transformer, parallel decoding, and object detection methods.

**2.1 Set Prediction**

There is no canonical deep learning model to directly predict sets. The basic set prediction task is multilabel classification (see e.g., [40,33] for references in the context of computer vision) for which the baseline approach, one-vs-rest, does not apply to problems such as detection where there is an underlying structure between elements (i.e., near-identical boxes). The first difficulty in these tasks is to avoid near-duplicates. Most current detectors use postprocessings such as non-maximal suppression to address this issue, but direct set prediction are postprocessing-free. They need global inference schemes that model interactions between all predicted elements to avoid redundancy. For constant-size set prediction, dense fully connected networks [9] are sufficient but costly. A general approach is to use auto-regressive sequence models such as recurrent neural networks [48]. In all cases, the loss function should be invariant by a permutation of the predictions. The usual solution is to design a loss based on the Hungarian algorithm [20], to find a bipartite matching between ground-truth and prediction. This enforces permutation-invariance, and guarantees that each target element has a unique match. We follow the bipartite matching loss approach. In contrast to most prior work however, we step away from autoregressive models and use transformers with parallel decoding, which we describe below.

**2.2 Transformers and Parallel Decoding**

Transformers were introduced by Vaswani et al. [47] as a new attention-based building block for machine translation. Attention mechanisms [2] are neural network layers that aggregate information from the entire input sequence. Transformers introduced self-attention layers, which, similarly to Non-Local Neural Networks [49], scan through each element of a sequence and update it by aggregating information from the whole sequence. One of the main advantages of attention-based models is their global computations and perfect memory, which makes them more suitable than RNNs on long sequences. Transformers are now replacing RNNs in many problems in natural language processing, speech processing and computer vision [8,27,45,34,31].

Transformers were first used in auto-regressive models, following early sequence-to-sequence models [44], generating output tokens one by one. However, the prohibitive inference cost (proportional to output length, and hard to batch) lead to the development of parallel sequence generation, in the domains of audio [29], machine translation [12,10], word representation learning [8], and more recently speech recognition [6]. We also combine transformers and parallel decoding for their suitable trade-off between computational cost and the ability to perform the global computations required for set prediction.

**2.3 Object detection**

Most modern object detection methods make predictions relative to some initial guesses. Two-stage detectors [37,5] predict boxes w.r.t. proposals, whereas single-stage methods make predictions w.r.t. anchors [23] or a grid of possible object centers [53,46]. Recent work [52] demonstrate that the final performance of these systems heavily depends on the exact way these initial guesses are set. In our model we are able to remove this hand-crafted process and streamline the detection process by directly predicting the set of detections with absolute box prediction w.r.t. the input image rather than an anchor.

**Set-based loss.** Several object detectors [9,25,35] used the bipartite matching loss. However, in these early deep learning models, the relation between different prediction was modeled with convolutional or fully-connected layers only and a hand-designed NMS post-processing can improve their performance. More recent detectors [37,23,53] use non-unique assignment rules between ground truth and predictions together with an NMS.

Learnable NMS methods [16,4] and relation networks [17] explicitly model relations between different predictions with attention. Using direct set losses, they do not require any post-processing steps. However, these methods employ additional hand-crafted context features like proposal box coordinates to model relations between detections efficiently, while we look for solutions that reduce the prior knowledge encoded in the model.

**Recurrent detectors.** Closest to our approach are end-to-end set predictions for object detection [43] and instance segmentation [41,30,36,42]. Similarly to us, they use bipartite-matching losses with encoder-decoder architectures based on CNN activations to directly produce a set of bounding boxes. These approaches, however, were only evaluated on small datasets and not against modern baselines. In particular, they are based on autoregressive models (more precisely RNNs), so they do not leverage the recent transformers with parallel decoding.

---

### النسخة العربية

يعتمد عملنا على الأعمال السابقة في عدة مجالات: خسائر المطابقة الثنائية للتنبؤ بالمجموعات، ومعماريات مشفر-فك تشفير القائمة على المحول، وفك التشفير المتوازي، وطرق كشف الأجسام.

**2.1 التنبؤ بالمجموعات**

لا يوجد نموذج تعلم عميق قانوني للتنبؤ المباشر بالمجموعات. مهمة التنبؤ بالمجموعات الأساسية هي التصنيف متعدد التسميات (انظر على سبيل المثال [40,33] للمراجع في سياق رؤية الحاسوب) والتي لا ينطبق عليها النهج الأساسي واحد-مقابل-الباقي على مسائل مثل الكشف حيث توجد بنية أساسية بين العناصر (أي صناديق متطابقة تقريباً). الصعوبة الأولى في هذه المهام هي تجنب النسخ المتكررة تقريباً. تستخدم معظم الكاشفات الحالية معالجات لاحقة مثل قمع عدم الحد الأقصى لمعالجة هذه المسألة، لكن التنبؤ المباشر بالمجموعات خالٍ من المعالجة اللاحقة. تحتاج إلى مخططات استنتاج عامة تنمذج التفاعلات بين جميع العناصر المتنبأ بها لتجنب التكرار. بالنسبة للتنبؤ بمجموعات ذات حجم ثابت، فإن الشبكات الكثيفة المتصلة بالكامل [9] كافية ولكنها مكلفة. النهج العام هو استخدام نماذج تسلسل انحداري ذاتي مثل الشبكات العصبية المتكررة [48]. في جميع الحالات، يجب أن تكون دالة الخسارة غير متغيرة بالنسبة لتبديل التنبؤات. الحل المعتاد هو تصميم خسارة تعتمد على خوارزمية المجري [20]، لإيجاد مطابقة ثنائية بين الحقيقة الأرضية والتنبؤ. يفرض هذا عدم التباين بالنسبة للتبديل، ويضمن أن لكل عنصر هدف مطابقة فريدة. نتبع نهج خسارة المطابقة الثنائية. ومع ذلك، على عكس معظم الأعمال السابقة، نبتعد عن النماذج الانحدارية الذاتية ونستخدم المحولات مع فك التشفير المتوازي، والذي نصفه أدناه.

**2.2 المحولات وفك التشفير المتوازي**

قدم Vaswani وآخرون [47] المحولات كمكون بناء جديد قائم على الانتباه للترجمة الآلية. آليات الانتباه [2] هي طبقات شبكة عصبية تجمع المعلومات من تسلسل الإدخال بأكمله. قدمت المحولات طبقات الانتباه الذاتي، والتي بشكل مشابه للشبكات العصبية غير المحلية [49]، تفحص كل عنصر من تسلسل وتحدثه من خلال تجميع المعلومات من التسلسل بأكمله. واحدة من المزايا الرئيسية للنماذج القائمة على الانتباه هي حساباتها العامة والذاكرة الكاملة، مما يجعلها أكثر ملاءمة من الشبكات العصبية المتكررة على التسلسلات الطويلة. تحل المحولات الآن محل الشبكات العصبية المتكررة في العديد من المسائل في معالجة اللغة الطبيعية ومعالجة الكلام ورؤية الحاسوب [8,27,45,34,31].

استُخدمت المحولات لأول مرة في النماذج الانحدارية الذاتية، تبعاً لنماذج التسلسل إلى التسلسل المبكرة [44]، التي تولد الرموز الناتجة واحداً تلو الآخر. ومع ذلك، أدت تكلفة الاستنتاج الباهظة (متناسبة مع طول الإخراج، ويصعب تجميعها في دفعات) إلى تطوير توليد التسلسل المتوازي، في مجالات الصوت [29] والترجمة الآلية [12,10] وتعلم تمثيل الكلمات [8]، وفي الآونة الأخيرة التعرف على الكلام [6]. نجمع أيضاً المحولات وفك التشفير المتوازي لمقايضتهما المناسبة بين التكلفة الحسابية والقدرة على أداء الحسابات العامة المطلوبة للتنبؤ بالمجموعات.

**2.3 كشف الأجسام**

تقوم معظم طرق كشف الأجسام الحديثة بالتنبؤات نسبة إلى بعض التخمينات الأولية. تتنبأ الكاشفات ذات المرحلتين [37,5] بالصناديق نسبة إلى المقترحات، بينما تقوم الطرق ذات المرحلة الواحدة بالتنبؤات نسبة إلى المراسي [23] أو شبكة من مراكز الأجسام المحتملة [53,46]. يُظهر العمل الحديث [52] أن الأداء النهائي لهذه الأنظمة يعتمد بشكل كبير على الطريقة الدقيقة التي يتم بها تعيين هذه التخمينات الأولية. في نموذجنا نستطيع إزالة هذه العملية المصنوعة يدوياً وتبسيط عملية الكشف من خلال التنبؤ المباشر بمجموعة الاكتشافات مع تنبؤ مطلق بالصندوق نسبة إلى صورة الإدخال بدلاً من مرساة.

**الخسارة القائمة على المجموعات.** استخدمت العديد من كاشفات الأجسام [9,25,35] خسارة المطابقة الثنائية. ومع ذلك، في نماذج التعلم العميق المبكرة هذه، تم نمذجة العلاقة بين التنبؤات المختلفة باستخدام الطبقات الالتفافية أو المتصلة بالكامل فقط ويمكن أن تحسن معالجة NMS اللاحقة المصممة يدوياً من أدائها. تستخدم الكاشفات الأحدث [37,23,53] قواعد تعيين غير فريدة بين الحقيقة الأرضية والتنبؤات مع NMS.

تنمذج طرق NMS القابلة للتعلم [16,4] وشبكات العلاقات [17] صراحةً العلاقات بين التنبؤات المختلفة باستخدام الانتباه. باستخدام خسائر المجموعات المباشرة، لا تتطلب أي خطوات معالجة لاحقة. ومع ذلك، تستخدم هذه الطرق ميزات سياق مصنوعة يدوياً إضافية مثل إحداثيات صندوق المقترح لنمذجة العلاقات بين الاكتشافات بكفاءة، بينما نبحث عن حلول تقلل من المعرفة المسبقة المشفرة في النموذج.

**الكاشفات المتكررة.** الأقرب إلى نهجنا هو التنبؤات من طرف إلى طرف بالمجموعات لكشف الأجسام [43] وتجزئة النسخ [41,30,36,42]. بشكل مشابه لنا، يستخدمون خسائر المطابقة الثنائية مع معماريات مشفر-فك تشفير القائمة على تفعيلات CNN لإنتاج مجموعة من صناديق التحديد مباشرة. ومع ذلك، تم تقييم هذه الأساليب فقط على مجموعات بيانات صغيرة وليس مقابل الخطوط الأساسية الحديثة. على وجه الخصوص، تعتمد على النماذج الانحدارية الذاتية (بشكل أكثر دقة الشبكات العصبية المتكررة)، لذلك لا تستفيد من المحولات الحديثة مع فك التشفير المتوازي.

---

### Translation Notes

- **Key terms introduced:** Hungarian algorithm (خوارزمية المجري), permutation-invariance (عدم التباين بالنسبة للتبديل), sequence-to-sequence (التسلسل إلى التسلسل), two-stage detectors (الكاشفات ذات المرحلتين), single-stage methods (الطرق ذات المرحلة الواحدة)
- **Citations:** Multiple references preserved [numbers]
- **Special handling:**
  - Subsection headings numbered (2.1, 2.2, 2.3)
  - Technical abbreviations (RNN, CNN, NMS) kept in English
  - Author names kept in English (Vaswani et al.)

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.89
- Readability: 0.84
- Glossary consistency: 0.84
- **Overall section score:** 0.86
