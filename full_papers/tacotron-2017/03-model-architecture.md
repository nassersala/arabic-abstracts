# Section 3: Model Architecture
## القسم 3: معمارية النموذج

**Section:** model-architecture
**Translation Quality:** 0.87
**Glossary Terms Used:** encoder, decoder, attention mechanism, neural network, architecture, convolutional, layer, spectrogram, sequence

---

### English Version

The backbone of Tacotron is a seq2seq model with attention. Figure 1 depicts the model, which includes an encoder, an attention-based decoder, and a post-processing net. At a high-level, our model takes characters as input and produces spectrogram frames, which are then converted to waveforms using the Griffin-Lim reconstruction algorithm.

We describe these components below.

**3.1 CBHG Module**

We first describe a building block dubbed CBHG, illustrated in Figure 2. CBHG consists of a bank of 1-D convolutional filters, followed by highway networks and a bidirectional gated recurrent unit (GRU). CBHG is a powerful module for extracting representations from sequences. The input sequence is first convolved with K sets of 1-D convolutional filters, where the k-th set contains C_k filters of width k (i.e. k = 1, 2, ..., K). These filters explicitly model local and contextual information (akin to modeling unigrams, bigrams, up to K-grams). The convolution outputs are stacked together and further max pooled along time to increase local invariances. Note that we use a stride of 1 to preserve the original time resolution. We further pass the processed sequence to a few fixed-width 1-D convolutions, whose outputs are added with the original input sequence via residual connections. Batch normalization is used for all convolutional layers. The convolution outputs are fed into a multi-layer highway network to extract high-level features. Finally, we stack a bidirectional GRU on top to extract sequential features from both forward and backward context. CBHG is inspired from work in machine translation, where the main differences from those systems include using non-causal convolutions, batch normalization, residual connections, and stride=1 max pooling. We found that these modifications improved generalization.

**3.2 Encoder**

The goal of the encoder is to extract robust sequential representations of text. The input to the encoder is a character sequence, where each character is represented as a one-hot vector and embedded into a continuous vector. We then apply a set of non-linear transformations, collectively called a "pre-net", to each embedding. We use a bottleneck layer with dropout as the pre-net in this work, which helps convergence and improves generalization. A CBHG module transforms the pre-net outputs into the final encoder representation used by the attention module. We found that this CBHG-based encoder not only reduces overfitting, but also makes fewer mispronunciations than a standard multi-layer RNN encoder.

**3.3 Decoder**

We use a content-based tanh attention decoder, where a stateful recurrent layer produces the attention query at each decoder time step. We concatenate the context vector and the attention RNN cell output to form the input to the decoder RNNs. We use a stack of GRUs with vertical residual connections for the decoder. We found the residual connections speed up convergence. The decoder target is an important design choice. While we could directly predict raw spectrogram, it's a highly redundant representation for the purpose of learning alignment between speech signal and text (which is really the motivation of using seq2seq for this task). Because of this redundancy, we use a different target for seq2seq decoding and waveform synthesis. The seq2seq target can be highly compressed as long as it provides sufficient intelligibility and audio quality for an inversion process, which could be fixed or trained. We use 80-band mel-scale spectrogram as the target, though fewer bands or more concise targets such as cepstrum could be used. We use a post-processing network (discussed below) to convert from the seq2seq target to waveform.

We use a simple fully-connected output layer to predict the decoder targets. An important trick we discovered was predicting multiple, non-overlapping output frames at each decoder step. Predicting r frames at once divides the total number of decoder steps by r, which reduces model size, training time, and inference time. More importantly, we found this trick to substantially increase convergence speed, as measured by a much faster (and more stable) alignment learned from attention. This is likely because neighboring speech frames are correlated and each character usually corresponds to multiple frames. Emitting one frame at a time forces the model to attend to the same input token for multiple timesteps; emitting multiple frames allows the attention to move forward early in training. A similar trick is also used in Char2Wav but mainly to speed up inference.

The first decoder step is conditioned on an all-zero frame, which represents a <GO> frame. In inference, at decoder step t, the last frame of the r predictions is fed as input to the decoder at step t+1. Note that feeding the last prediction is an ad-hoc choice here – we could use all r predictions. During training, we always feed every r-th ground truth frame to the decoder. The input frame is passed to a pre-net as is done in the encoder. Since we do not use techniques such as scheduled sampling (we found it to hurt audio quality), the dropout in the pre-net is critical for the model to generalize, as it provides a noise source to resolve the multiple modalities in the output distribution.

**3.4 Post-processing Net and Waveform Synthesis**

As mentioned above, the post-processing net's task is to convert the seq2seq target to a target that can be synthesized into waveforms. Since we use Griffin-Lim as the synthesizer, the post-processing net learns to predict spectral magnitude sampled on a linear-frequency scale. Another motivation of the post-processing net is that it can see the full decoded sequence. In contrast to seq2seq, which always runs from left to right, it has both forward and backward information to correct the prediction error for each individual frame. In this work, we use a CBHG module for the post-processing net, though a simpler architecture likely works as well. The concept of a post-processing network is highly general. It could be used to predict alternative targets such as vocoder parameters, or as a WaveNet-like neural vocoder that synthesizes waveform samples directly.

We use the Griffin-Lim algorithm to synthesize waveform from the predicted spectrogram. We found that raising the predicted magnitudes by a power of 1.2 before feeding to Griffin-Lim reduces artifacts, likely due to its harmonic enhancement effect. We observed that Griffin-Lim converges after 50 iterations (in fact, about 30 iterations seems to be enough), which is reasonably fast. We implemented Griffin-Lim in TensorFlow hence it's also part of the model.

---

### النسخة العربية

العمود الفقري لتاكوترون هو نموذج seq2seq مع آلية الانتباه. يصور الشكل 1 النموذج، الذي يتضمن مشفراً، وفك تشفير قائماً على الانتباه، وشبكة معالجة لاحقة. على مستوى عالٍ، يأخذ نموذجنا الأحرف كمدخل وينتج إطارات المخطط الطيفي، والتي يتم تحويلها بعد ذلك إلى موجات باستخدام خوارزمية إعادة البناء Griffin-Lim.

نصف هذه المكونات أدناه.

**3.1 وحدة CBHG**

نصف أولاً كتلة بناء تسمى CBHG، موضحة في الشكل 2. تتكون CBHG من مجموعة من المرشحات الالتفافية أحادية البعد، تليها شبكات الطرق السريعة (highway networks) ووحدة بوابية متكررة ثنائية الاتجاه (GRU). تعد CBHG وحدة قوية لاستخراج التمثيلات من التسلسلات. يتم أولاً إجراء التفاف للتسلسل المدخل مع K مجموعة من المرشحات الالتفافية أحادية البعد، حيث تحتوي المجموعة k على C_k مرشحات بعرض k (أي k = 1، 2، ...، K). تقوم هذه المرشحات صراحةً بنمذجة المعلومات المحلية والسياقية (مشابهة لنمذجة أحادية الكلمات، وثنائية الكلمات، حتى K-جرام). يتم تكديس مخرجات الالتفاف معاً ويتم إجراء تجميع أقصى (max pooling) على طول الزمن لزيادة الثبات المحلي. لاحظ أننا نستخدم خطوة (stride) قدرها 1 للحفاظ على الدقة الزمنية الأصلية. نمرر التسلسل المُعالَج إلى عدد قليل من الالتفافات أحادية البعد ذات العرض الثابت، والتي تُضاف مخرجاتها مع تسلسل المدخل الأصلي عبر اتصالات متبقية (residual connections). يتم استخدام التطبيع الدفعي (batch normalization) لجميع الطبقات الالتفافية. يتم إدخال مخرجات الالتفاف في شبكة طرق سريعة متعددة الطبقات لاستخراج الميزات عالية المستوى. أخيراً، نكدس GRU ثنائي الاتجاه في الأعلى لاستخراج الميزات التسلسلية من كل من السياق الأمامي والخلفي. مستوحاة CBHG من العمل في الترجمة الآلية، حيث تشمل الاختلافات الرئيسية عن تلك الأنظمة استخدام الالتفافات غير السببية، والتطبيع الدفعي، والاتصالات المتبقية، وتجميع الحد الأقصى بخطوة=1. وجدنا أن هذه التعديلات حسّنت التعميم.

**3.2 المشفر**

الهدف من المشفر هو استخراج تمثيلات تسلسلية قوية للنص. المدخل إلى المشفر هو تسلسل من الأحرف، حيث يتم تمثيل كل حرف كمتجه أحادي ساخن (one-hot vector) ومضمّن في متجه مستمر. ثم نطبق مجموعة من التحويلات غير الخطية، تسمى مجتمعة "pre-net"، على كل تضمين. نستخدم طبقة اختناق (bottleneck layer) مع إسقاط (dropout) كـ pre-net في هذا العمل، مما يساعد في التقارب ويحسن التعميم. تحول وحدة CBHG مخرجات pre-net إلى تمثيل المشفر النهائي المستخدم بواسطة وحدة الانتباه. وجدنا أن هذا المشفر القائم على CBHG لا يقلل فقط من الإفراط في التوفيق، بل يرتكب أيضاً أخطاء نطق أقل من مشفر RNN متعدد الطبقات القياسي.

**3.3 فك التشفير**

نستخدم فك تشفير انتباه tanh قائم على المحتوى، حيث تنتج طبقة متكررة حالتية استعلام الانتباه في كل خطوة زمنية لفك التشفير. نربط متجه السياق ومخرج خلية RNN للانتباه لتشكيل المدخل إلى شبكات RNN لفك التشفير. نستخدم مكدس من وحدات GRU مع اتصالات متبقية عمودية لفك التشفير. وجدنا أن الاتصالات المتبقية تسرع التقارب. الهدف من فك التشفير هو خيار تصميمي مهم. بينما يمكننا التنبؤ مباشرة بالمخطط الطيفي الخام، إلا أنه تمثيل زائد للغاية لغرض تعلم المحاذاة بين إشارة الكلام والنص (وهو حقاً الدافع لاستخدام seq2seq لهذه المهمة). بسبب هذا التكرار، نستخدم هدفاً مختلفاً لفك تشفير seq2seq وتوليف الموجة. يمكن ضغط هدف seq2seq بشكل كبير طالما أنه يوفر قابلية فهم وجودة صوتية كافية لعملية الانعكاس، والتي يمكن أن تكون ثابتة أو مُدرَّبة. نستخدم مخطط طيفي بمقياس ميل (mel-scale) من 80 نطاقاً كهدف، على الرغم من أنه يمكن استخدام نطاقات أقل أو أهداف أكثر إيجازاً مثل الكبسترم (cepstrum). نستخدم شبكة معالجة لاحقة (تمت مناقشتها أدناه) للتحويل من هدف seq2seq إلى الموجة.

نستخدم طبقة مخرج متصلة بالكامل بسيطة للتنبؤ بأهداف فك التشفير. حيلة مهمة اكتشفناها هي التنبؤ بإطارات مخرج متعددة غير متداخلة في كل خطوة لفك التشفير. التنبؤ بـ r إطار في وقت واحد يقسم إجمالي عدد خطوات فك التشفير على r، مما يقلل من حجم النموذج ووقت التدريب ووقت الاستدلال. والأهم من ذلك، وجدنا أن هذه الحيلة تزيد بشكل كبير من سرعة التقارب، كما يُقاس بمحاذاة أسرع بكثير (وأكثر استقراراً) تم تعلمها من الانتباه. من المحتمل أن يكون هذا لأن إطارات الكلام المجاورة مترابطة وعادة ما يتوافق كل حرف مع إطارات متعددة. إصدار إطار واحد في كل مرة يجبر النموذج على الانتباه إلى نفس الرمز المدخل لخطوات زمنية متعددة؛ إصدار إطارات متعددة يسمح للانتباه بالتحرك للأمام في وقت مبكر من التدريب. يتم استخدام حيلة مماثلة أيضاً في Char2Wav ولكن بشكل أساسي لتسريع الاستدلال.

يتم إشراط خطوة فك التشفير الأولى على إطار جميع أصفار، والذي يمثل إطار <GO>. في الاستدلال، في خطوة فك التشفير t، يتم إدخال الإطار الأخير من تنبؤات r كمدخل لفك التشفير في الخطوة t+1. لاحظ أن إدخال التنبؤ الأخير هو خيار مخصص هنا - يمكننا استخدام جميع تنبؤات r. أثناء التدريب، نقوم دائماً بإدخال كل إطار حقيقة أرضية r إلى فك التشفير. يتم تمرير إطار المدخل إلى pre-net كما هو الحال في المشفر. نظراً لأننا لا نستخدم تقنيات مثل أخذ العينات المجدولة (scheduled sampling) (وجدنا أنها تضر بجودة الصوت)، فإن الإسقاط في pre-net أمر بالغ الأهمية لتعميم النموذج، حيث يوفر مصدر ضوضاء لحل الطرائق المتعددة في توزيع المخرجات.

**3.4 شبكة المعالجة اللاحقة وتوليف الموجة**

كما ذُكر أعلاه، مهمة شبكة المعالجة اللاحقة هي تحويل هدف seq2seq إلى هدف يمكن تحويله إلى موجات. نظراً لأننا نستخدم Griffin-Lim كمُركِّب، فإن شبكة المعالجة اللاحقة تتعلم التنبؤ بالمقدار الطيفي المأخوذ على مقياس تردد خطي. دافع آخر لشبكة المعالجة اللاحقة هو أنه يمكنها رؤية التسلسل المفكوك بالكامل. على النقيض من seq2seq، الذي يعمل دائماً من اليسار إلى اليمين، فإنه يحتوي على معلومات أمامية وخلفية لتصحيح خطأ التنبؤ لكل إطار فردي. في هذا العمل، نستخدم وحدة CBHG لشبكة المعالجة اللاحقة، على الرغم من أن معمارية أبسط من المحتمل أن تعمل أيضاً. مفهوم شبكة المعالجة اللاحقة عام للغاية. يمكن استخدامها للتنبؤ بأهداف بديلة مثل معاملات المُركِّب الصوتي، أو كمُركِّب صوتي عصبي شبيه بـ WaveNet يولف عينات الموجة مباشرة.

نستخدم خوارزمية Griffin-Lim لتوليف الموجة من المخطط الطيفي المتنبأ به. وجدنا أن رفع المقادير المتنبأ بها بقوة 1.2 قبل الإدخال إلى Griffin-Lim يقلل من العيوب، على الأرجح بسبب تأثير التعزيز التوافقي. لاحظنا أن Griffin-Lim يتقارب بعد 50 تكراراً (في الواقع، حوالي 30 تكراراً يبدو كافياً)، وهو سريع بشكل معقول. قمنا بتنفيذ Griffin-Lim في TensorFlow وبالتالي فهو أيضاً جزء من النموذج.

---

### Translation Notes

- **Figures referenced:** Figure 1, Figure 2
- **Key terms introduced:**
  - seq2seq: من تسلسل إلى تسلسل
  - CBHG module: وحدة CBHG
  - 1-D convolutional filters: المرشحات الالتفافية أحادية البعد
  - highway networks: شبكات الطرق السريعة
  - bidirectional GRU: وحدة بوابية متكررة ثنائية الاتجاه
  - max pooling: تجميع الحد الأقصى
  - residual connections: اتصالات متبقية
  - batch normalization: التطبيع الدفعي
  - one-hot vector: متجه أحادي ساخن
  - pre-net: الشبكة الأولية
  - bottleneck layer: طبقة اختناق
  - dropout: إسقاط
  - content-based attention: انتباه قائم على المحتوى
  - mel-scale spectrogram: مخطط طيفي بمقياس ميل
  - cepstrum: كبسترم
  - scheduled sampling: أخذ العينات المجدولة
  - Griffin-Lim algorithm: خوارزمية Griffin-Lim
  - linear-frequency scale: مقياس تردد خطي
- **Equations:** 0
- **Citations:** References to Char2Wav, machine translation work
- **Special handling:** Kept technical acronyms (CBHG, GRU, RNN) and algorithm names (Griffin-Lim) in English as they are standard in the field

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.90
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.87
