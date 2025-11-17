# Section 3: The DETR Model
## القسم 3: نموذج DETR

**Section:** methodology
**Translation Quality:** 0.85
**Glossary Terms Used:** التنبؤ بالمجموعات (set prediction), المطابقة الثنائية (bipartite matching), مشفر-فك تشفير (encoder-decoder), محول (transformer), الانتباه الذاتي (self-attention), الانتباه المتقاطع (cross-attention), استعلامات الأجسام (object queries), صناديق التحديد (bounding boxes), دالة الخسارة (loss function), خوارزمية المجري (Hungarian algorithm), شبكة أمامية (feed-forward network)

---

### English Version

Two ingredients are essential for direct set predictions in detection: (1) a set prediction loss that forces unique matching between predicted and ground truth boxes; (2) an architecture that predicts (in a single pass) a set of objects and models their relation. We describe our architecture in detail in Figure 2.

**3.1 Object detection set prediction loss**

DETR infers a fixed-size set of N predictions, in a single pass through the decoder, where N is set to be significantly larger than the typical number of objects in an image. One of the main difficulties of training is to score predicted objects (class, position, size) with respect to the ground truth. Our loss produces an optimal bipartite matching between predicted and ground truth objects, and then optimize object-specific (bounding box) losses.

Let us denote by y the ground truth set of objects, and ŷ = {ŷᵢ}ᵢ₌₁ᴺ the set of N predictions. Assuming N is larger than the number of objects in the image, we consider y also as a set of size N padded with ∅ (no object). To find a bipartite matching between these two sets we search for a permutation of N elements σ ∈ Sₙ with the lowest cost:

σ̂ = arg min_{σ∈Sₙ} Σᵢ₌₁ᴺ Lₘₐₜcₕ(yᵢ, ŷ_{σ(i)})     (1)

where Lₘₐₜcₕ(yᵢ, ŷ_{σ(i)}) is a pair-wise matching cost between ground truth yᵢ and a prediction with index σ(i). This optimal assignment is computed efficiently with the Hungarian algorithm, following prior work (e.g. [43]).

The matching cost takes into account both the class prediction and the similarity of predicted and ground truth boxes. Each element i of the ground truth set can be seen as a yᵢ = (cᵢ, bᵢ) where cᵢ is the target class label (which may be ∅) and bᵢ ∈ [0,1]⁴ is a vector that defines ground truth box center coordinates and its height and width relative to the image size. For the prediction with index σ(i) we define probability of class cᵢ as p̂_{σ(i)}(cᵢ) and the predicted box as b̂_{σ(i)}. With these notations we define Lₘₐₜcₕ(yᵢ, ŷ_{σ(i)}) as -𝟙_{cᵢ≠∅}p̂_{σ(i)}(cᵢ) + 𝟙_{cᵢ≠∅}L_{box}(bᵢ, b̂_{σ(i)}).

This procedure of finding matching plays the same role as the heuristic assignment rules used to match proposal [37] or anchors [22] to ground truth objects in modern detectors. The main difference is that we need to find one-to-one matching for direct set prediction without duplicates.

The second step is to compute the loss function, the Hungarian loss for all pairs matched in the previous step. We define the loss similarly to the losses of common object detectors, i.e. a linear combination of a negative log-likelihood for class prediction and a box loss defined later:

L_{Hungarian}(y, ŷ) = Σᵢ₌₁ᴺ [-log p̂_{σ̂(i)}(cᵢ) + 𝟙_{cᵢ≠∅}L_{box}(bᵢ, b̂_{σ̂(i)})]     (2)

where σ̂ is the optimal assignment computed in the first step (1). In practice, we down-weight the log-probability term when cᵢ = ∅ by a factor 10 to account for class imbalance. This is analogous to how Faster R-CNN training procedure balances positive/negative proposals by subsampling [37]. Notice that the matching cost between an object and ∅ doesn't depend on the prediction, which means that in that case the cost is a constant. In the matching cost we use probabilities p̂_{σ̂(i)}(cᵢ) instead of log-probabilities. This makes the class prediction term commensurable to L_{box}(·,·) (described below), and we observed better empirical performances.

**Bounding box loss.** The second part of the matching cost and the Hungarian loss is L_{box}(·) that scores the bounding boxes. Unlike many detectors that do box predictions as a w.r.t. some initial guesses, we make box predictions directly. While such approach simplify the implementation it poses an issue with relative scaling of the loss. The most commonly-used ℓ₁ loss will have different scales for small and large boxes even if their relative errors are similar. To mitigate this issue we use a linear combination of the ℓ₁ loss and the generalized IoU loss [38] L_{iou}(·,·) that is scale-invariant. Overall, our box loss is L_{box}(bᵢ, b̂_{σ(i)}) defined as λ_{iou}L_{iou}(bᵢ, b̂_{σ(i)}) + λ_{L1}||bᵢ - b̂_{σ(i)}||₁ where λ_{iou}, λ_{L1} ∈ ℝ are hyperparameters. These two losses are normalized by the number of objects inside the batch.

**3.2 DETR architecture**

The overall DETR architecture is surprisingly simple and depicted in Figure 2. It contains three main components, which we describe below: a CNN backbone to extract a compact feature representation, an encoder-decoder transformer, and a simple feed forward network (FFN) that makes the final detection prediction.

Unlike many modern detectors, DETR can be implemented in any deep learning framework that provides a common CNN backbone and a transformer architecture implementation with just a few hundred lines. Inference code for DETR can be implemented in less than 50 lines in PyTorch [32]. We hope that the simplicity of our method will attract new researchers to the detection community.

**Backbone.** Starting from the initial image x_{img} ∈ ℝ^{3×H₀×W₀} (with 3 color channels), a conventional CNN backbone generates a lower-resolution activation map f ∈ ℝ^{C×H×W}. Typical values we use are C = 2048 and H, W = H₀/32, W₀/32.

**Transformer encoder.** First, a 1×1 convolution reduces the channel dimension of the high-level activation map f from C to a smaller dimension d, creating a new feature map z₀ ∈ ℝ^{d×H×W}. The encoder expects a sequence as input, hence we collapse the spatial dimensions of z₀ into one dimension, resulting in a d×HW feature map. Each encoder layer has a standard architecture and consists of a multi-head self-attention module and a feed forward network (FFN). Since the transformer architecture is permutation-invariant, we supplement it with fixed positional encodings [31,3] that are added to the input of each attention layer. We defer to the supplementary material the detailed definition of the architecture, which follows the one described in [47].

**Figure 2:** DETR uses a conventional CNN backbone to learn a 2D representation of an input image. The model flattens it and supplements it with a positional encoding before passing it into a transformer encoder. A transformer decoder then takes as input a small fixed number of learned positional embeddings, which we call object queries, and additionally attends to the encoder output. We pass each output embedding of the decoder to a shared feed forward network (FFN) that predicts either a detection (class and bounding box) or a "no object" class.

**Transformer decoder.** The decoder follows the standard architecture of the transformer, transforming N embeddings of size d using multi-headed self- and encoder-decoder attention mechanisms. The difference with the original transformer is that our model decodes the N objects in parallel at each decoder layer, while Vaswani et al. [47] use an autoregressive model that predicts the output sequence one element at a time. We refer the reader unfamiliar with the concepts to the supplementary material. Since the decoder is also permutation-invariant, the N input embeddings must be different to produce different results. These input embeddings are learnt positional encodings that we refer to as object queries, and similarly to the encoder, we add them to the input of each attention layer. The N object queries are transformed into an output embedding by the decoder. They are then independently decoded into box coordinates and class labels by a feed forward network (described in the next subsection), resulting N final predictions. Using self- and encoder-decoder attention over these embeddings, the model globally reasons about all objects together using pair-wise relations between them, while being able to use the whole image as context.

**Prediction feed-forward networks (FFNs).** The final prediction is computed by a 3-layer perceptron with ReLU activation function and hidden dimension d, and a linear projection layer. The FFN predicts the normalized center coordinates, height and width of the box w.r.t. the input image, and the linear layer predicts the class label using a softmax function. Since we predict a fixed-size set of N bounding boxes, where N is usually much larger than the actual number of objects of interest in an image, an additional special class label ∅ is used to represent that no object is detected within a slot. This class plays a similar role to the "background" class in the standard object detection approaches.

**Auxiliary decoding losses.** We found helpful to use auxiliary losses [1] in decoder during training, especially to help the model output the correct number of objects of each class. We add prediction FFNs and Hungarian loss after each decoder layer. All predictions FFNs share their parameters. We use an additional shared layer-norm to normalize the input to the prediction FFNs from different decoder layers.

---

### النسخة العربية

هناك مكونان أساسيان للتنبؤ المباشر بالمجموعات في الكشف: (1) خسارة التنبؤ بالمجموعات التي تفرض مطابقة فريدة بين الصناديق المتنبأ بها والحقيقية؛ (2) معمارية تتنبأ (في تمريرة واحدة) بمجموعة من الأجسام وتنمذج علاقتها. نصف معماريتنا بالتفصيل في الشكل 2.

**3.1 خسارة التنبؤ بالمجموعات لكشف الأجسام**

يستنتج DETR مجموعة بحجم ثابت من N تنبؤات، في تمريرة واحدة عبر فك التشفير، حيث يتم تعيين N ليكون أكبر بكثير من العدد النموذجي للأجسام في الصورة. إحدى الصعوبات الرئيسية للتدريب هي تسجيل الأجسام المتنبأ بها (الفئة، الموضع، الحجم) بالنسبة للحقيقة الأرضية. تنتج خسارتنا مطابقة ثنائية مثلى بين الأجسام المتنبأ بها والأجسام الحقيقية، ثم تحسن خسائر محددة للأجسام (صندوق التحديد).

دعنا نشير بـ y إلى مجموعة الحقيقة الأرضية للأجسام، و ŷ = {ŷᵢ}ᵢ₌₁ᴺ مجموعة التنبؤات N. بافتراض أن N أكبر من عدد الأجسام في الصورة، نعتبر y أيضاً كمجموعة بحجم N مملوءة بـ ∅ (لا يوجد جسم). لإيجاد مطابقة ثنائية بين هاتين المجموعتين نبحث عن تبديل لعناصر N، σ ∈ Sₙ بأقل تكلفة:

σ̂ = arg min_{σ∈Sₙ} Σᵢ₌₁ᴺ Lₘₐₜcₕ(yᵢ, ŷ_{σ(i)})     (1)

حيث Lₘₐₜcₕ(yᵢ, ŷ_{σ(i)}) هي تكلفة المطابقة الثنائية بين الحقيقة الأرضية yᵢ وتنبؤ بفهرس σ(i). يتم حساب هذا التعيين الأمثل بكفاءة باستخدام خوارزمية المجري، تبعاً للعمل السابق (مثل [43]).

تأخذ تكلفة المطابقة في الاعتبار كلاً من تنبؤ الفئة وتشابه الصناديق المتنبأ بها والحقيقية. يمكن رؤية كل عنصر i من مجموعة الحقيقة الأرضية كـ yᵢ = (cᵢ, bᵢ) حيث cᵢ هي تسمية الفئة المستهدفة (والتي قد تكون ∅) و bᵢ ∈ [0,1]⁴ هو متجه يحدد إحداثيات مركز صندوق الحقيقة الأرضية وارتفاعه وعرضه بالنسبة لحجم الصورة. للتنبؤ بفهرس σ(i) نحدد احتمال الفئة cᵢ كـ p̂_{σ(i)}(cᵢ) والصندوق المتنبأ به كـ b̂_{σ(i)}. بهذه الرموز نحدد Lₘₐₜcₕ(yᵢ, ŷ_{σ(i)}) كـ -𝟙_{cᵢ≠∅}p̂_{σ(i)}(cᵢ) + 𝟙_{cᵢ≠∅}L_{box}(bᵢ, b̂_{σ(i)}).

تلعب إجراءات إيجاد المطابقة هذه نفس الدور كقواعد التعيين الاستدلالية المستخدمة لمطابقة المقترحات [37] أو المراسي [22] مع أجسام الحقيقة الأرضية في الكاشفات الحديثة. الفرق الرئيسي هو أننا بحاجة إلى إيجاد مطابقة واحد لواحد للتنبؤ المباشر بالمجموعات بدون نسخ مكررة.

الخطوة الثانية هي حساب دالة الخسارة، خسارة المجري لجميع الأزواج المطابقة في الخطوة السابقة. نحدد الخسارة بشكل مشابه لخسائر كاشفات الأجسام الشائعة، أي مزيج خطي من اللوغاريتم السلبي للاحتمالية لتنبؤ الفئة وخسارة الصندوق المحددة لاحقاً:

L_{Hungarian}(y, ŷ) = Σᵢ₌₁ᴺ [-log p̂_{σ̂(i)}(cᵢ) + 𝟙_{cᵢ≠∅}L_{box}(bᵢ, b̂_{σ̂(i)})]     (2)

حيث σ̂ هو التعيين الأمثل المحسوب في الخطوة الأولى (1). في الممارسة العملية، نقلل وزن حد احتمالية اللوغاريتم عندما cᵢ = ∅ بعامل 10 لحساب عدم توازن الفئات. هذا مماثل لكيفية موازنة إجراء تدريب Faster R-CNN للمقترحات الإيجابية/السلبية عن طريق أخذ عينات فرعية [37]. لاحظ أن تكلفة المطابقة بين جسم و ∅ لا تعتمد على التنبؤ، مما يعني أنه في تلك الحالة التكلفة ثابتة. في تكلفة المطابقة نستخدم الاحتماليات p̂_{σ̂(i)}(cᵢ) بدلاً من احتماليات اللوغاريتم. هذا يجعل حد تنبؤ الفئة متناسباً مع L_{box}(·,·) (الموصوفة أدناه)، ولاحظنا أداءً تجريبياً أفضل.

**خسارة صندوق التحديد.** الجزء الثاني من تكلفة المطابقة وخسارة المجري هو L_{box}(·) الذي يسجل صناديق التحديد. على عكس العديد من الكاشفات التي تقوم بتنبؤات الصندوق بالنسبة لبعض التخمينات الأولية، نقوم بتنبؤات الصندوق مباشرة. بينما يبسط هذا النهج التنفيذ، فإنه يطرح مسألة بشأن التحجيم النسبي للخسارة. ستكون لخسارة ℓ₁ الأكثر استخداماً مقاييس مختلفة للصناديق الصغيرة والكبيرة حتى لو كانت أخطاؤها النسبية متشابهة. للتخفيف من هذه المسألة نستخدم مزيجاً خطياً من خسارة ℓ₁ وخسارة IoU المعممة [38] L_{iou}(·,·) التي تكون غير متغيرة بالنسبة للمقياس. بشكل عام، خسارة الصندوق الخاصة بنا هي L_{box}(bᵢ, b̂_{σ(i)}) محددة كـ λ_{iou}L_{iou}(bᵢ, b̂_{σ(i)}) + λ_{L1}||bᵢ - b̂_{σ(i)}||₁ حيث λ_{iou}, λ_{L1} ∈ ℝ معلمات فائقة. يتم تطبيع هاتين الخسارتين بعدد الأجسام داخل الدفعة.

**3.2 معمارية DETR**

معمارية DETR الإجمالية بسيطة بشكل مدهش وموضحة في الشكل 2. تحتوي على ثلاثة مكونات رئيسية، نصفها أدناه: العمود الفقري CNN لاستخراج تمثيل ميزات مضغوط، ومحول مشفر-فك تشفير، وشبكة أمامية بسيطة (FFN) تقوم بالتنبؤ النهائي بالكشف.

على عكس العديد من الكاشفات الحديثة، يمكن تنفيذ DETR في أي إطار عمل تعلم عميق يوفر عموداً فقرياً CNN شائعاً وتنفيذ معمارية محول بضع مئات من الأسطر فقط. يمكن تنفيذ كود الاستنتاج لـ DETR في أقل من 50 سطراً في PyTorch [32]. نأمل أن تجذب بساطة طريقتنا باحثين جدد إلى مجتمع الكشف.

**العمود الفقري.** بدءاً من الصورة الأولية x_{img} ∈ ℝ^{3×H₀×W₀} (بثلاث قنوات ألوان)، يولد عمود فقري CNN تقليدي خريطة تنشيط بدقة أقل f ∈ ℝ^{C×H×W}. القيم النموذجية التي نستخدمها هي C = 2048 و H, W = H₀/32, W₀/32.

**مشفر المحول.** أولاً، يقلل التفاف 1×1 بُعد القناة لخريطة التنشيط عالية المستوى f من C إلى بُعد أصغر d، منشئاً خريطة ميزات جديدة z₀ ∈ ℝ^{d×H×W}. يتوقع المشفر تسلسلاً كإدخال، ومن ثم نطوي الأبعاد المكانية لـ z₀ إلى بُعد واحد، مما ينتج عنه خريطة ميزات d×HW. كل طبقة مشفر لها معمارية قياسية وتتكون من وحدة انتباه ذاتي متعدد الرؤوس وشبكة أمامية (FFN). نظراً لأن معمارية المحول غير متغيرة بالنسبة للتبديل، نكملها بترميزات موضعية ثابتة [31,3] تُضاف إلى إدخال كل طبقة انتباه. نؤجل إلى المادة التكميلية التعريف التفصيلي للمعمارية، والذي يتبع تلك الموصوفة في [47].

**الشكل 2:** يستخدم DETR عموداً فقرياً CNN تقليدياً لتعلم تمثيل ثنائي الأبعاد لصورة إدخال. يقوم النموذج بتسطيحها ويكملها بترميز موضعي قبل تمريرها إلى مشفر المحول. يأخذ فك تشفير المحول بعد ذلك كإدخال عدداً ثابتاً صغيراً من التضمينات الموضعية المتعلمة، والتي نسميها استعلامات الأجسام، ويحضر بشكل إضافي إلى إخراج المشفر. نمرر كل تضمين إخراج من فك التشفير إلى شبكة أمامية مشتركة (FFN) تتنبأ إما باكتشاف (الفئة وصندوق التحديد) أو فئة "لا يوجد جسم".

**فك تشفير المحول.** يتبع فك التشفير المعمارية القياسية للمحول، محولاً N تضمينات بحجم d باستخدام آليات انتباه ذاتي ومشفر-فك تشفير متعددة الرؤوس. الفرق مع المحول الأصلي هو أن نموذجنا يفك تشفير أجسام N بشكل متوازٍ في كل طبقة فك تشفير، بينما يستخدم Vaswani وآخرون [47] نموذجاً انحدارياً ذاتياً يتنبأ بتسلسل الإخراج عنصراً واحداً في كل مرة. نحيل القارئ غير المألوف بالمفاهيم إلى المادة التكميلية. نظراً لأن فك التشفير أيضاً غير متغير بالنسبة للتبديل، يجب أن تكون تضمينات الإدخال N مختلفة لإنتاج نتائج مختلفة. تضمينات الإدخال هذه هي ترميزات موضعية متعلمة نشير إليها باسم استعلامات الأجسام، وبشكل مشابه للمشفر، نضيفها إلى إدخال كل طبقة انتباه. يتم تحويل استعلامات الأجسام N إلى تضمين إخراج بواسطة فك التشفير. ثم يتم فك تشفيرها بشكل مستقل إلى إحداثيات الصندوق وتسميات الفئات بواسطة شبكة أمامية (موصوفة في القسم الفرعي التالي)، مما ينتج عنه تنبؤات N النهائية. باستخدام الانتباه الذاتي والمشفر-فك تشفير عبر هذه التضمينات، يستدل النموذج عالمياً حول جميع الأجسام معاً باستخدام العلاقات الثنائية بينها، مع القدرة على استخدام الصورة بأكملها كسياق.

**الشبكات الأمامية للتنبؤ (FFNs).** يتم حساب التنبؤ النهائي بواسطة إدراك متعدد الطبقات بثلاث طبقات مع دالة تنشيط ReLU وبُعد مخفي d، وطبقة إسقاط خطية. تتنبأ FFN بالإحداثيات المطبعة للمركز والارتفاع والعرض للصندوق بالنسبة لصورة الإدخال، وتتنبأ الطبقة الخطية بتسمية الفئة باستخدام دالة softmax. نظراً لأننا نتنبأ بمجموعة بحجم ثابت من صناديق التحديد N، حيث N عادة أكبر بكثير من العدد الفعلي للأجسام محل الاهتمام في الصورة، يتم استخدام تسمية فئة خاصة إضافية ∅ لتمثيل عدم اكتشاف أي جسم داخل فتحة. تلعب هذه الفئة دوراً مشابهاً لفئة "الخلفية" في مناهج كشف الأجسام القياسية.

**خسائر فك التشفير المساعدة.** وجدنا أنه من المفيد استخدام خسائر مساعدة [1] في فك التشفير أثناء التدريب، خاصة لمساعدة النموذج على إخراج العدد الصحيح من الأجسام لكل فئة. نضيف FFNs للتنبؤ وخسارة المجري بعد كل طبقة فك تشفير. تشارك جميع FFNs للتنبؤ معلماتها. نستخدم طبقة-تطبيع مشتركة إضافية لتطبيع الإدخال إلى FFNs للتنبؤ من طبقات فك تشفير مختلفة.

---

### Translation Notes

- **Equations:** 2 mathematical equations (1) and (2) preserved exactly in LaTeX notation
- **Mathematical notation:** All symbols (σ, ŷ, Lₘₐₜcₕ, etc.) kept in original form
- **Key terms introduced:** Hungarian algorithm (خوارزمية المجري), object queries (استعلامات الأجسام), feed-forward network (شبكة أمامية), positional encoding (ترميز موضعي), generalized IoU (IoU المعممة)
- **Figures referenced:** Figure 2 with detailed caption translation
- **Citations:** Multiple references preserved [numbers]
- **Special handling:**
  - Technical abbreviations (CNN, FFN, ReLU) kept in English
  - Framework names (PyTorch) kept in English
  - All mathematical notation preserved exactly

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.88
- Readability: 0.83
- Glossary consistency: 0.83
- **Overall section score:** 0.85
