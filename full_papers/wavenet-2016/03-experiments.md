# Section 3: Experiments
## القسم 3: التجارب

**Section:** experiments
**Translation Quality:** 0.90
**Glossary Terms Used:** text-to-speech, speech synthesis, generative model, training, dataset, evaluation, mean opinion score, baseline, multi-speaker, conditioning, speech recognition, phoneme recognition, music generation

---

### English Version

## 3. Experiments

We evaluate WaveNet on four different tasks: multi-speaker speech generation (not conditioned on text), TTS, music audio modeling, and speech recognition. For each task, we describe the dataset, model architecture, and experimental results.

### 3.1 Multi-Speaker Speech Generation

**Dataset**: We use the VCTK corpus, which contains speech from 109 different speakers. Each speaker reads about 400 sentences. We downsample all audio to 16 kHz.

**Architecture**: We use a WaveNet with 30 dilated convolution layers organized in 3 blocks of 10 layers each. Each block contains dilations of 1, 2, 4, 8, ..., 256, 512. This gives a receptive field of about 240 milliseconds. We use residual connections and skip connections as described in Section 2. We condition the model on a one-hot encoding of the speaker ID (global conditioning).

**Results**: The model successfully learns to generate speech from all 109 speakers with high fidelity. We can generate samples that sound like any speaker by simply changing the speaker ID during generation. Audio samples are available on our website.

More interestingly, we can interpolate between speaker embeddings. We train a separate model where the one-hot speaker ID is first projected to a lower-dimensional embedding space (16 dimensions). We can then linearly interpolate between two speaker embeddings and generate audio with characteristics that smoothly transition between the two speakers.

### 3.2 Text-to-Speech

**Dataset**: We evaluate on two languages:
- **English**: We use an internal North American English dataset containing approximately 24.6 hours of speech from a single professional female speaker.
- **Mandarin**: We use an internal Mandarin Chinese dataset containing approximately 34.8 hours of speech from multiple speakers (male and female).

**Architecture**: For TTS, we condition WaveNet on linguistic features extracted from the text. The linguistic features include phoneme identity, duration, and various prosodic features (pitch, energy, etc.). Since linguistic features are typically at a lower temporal resolution than audio (e.g., one feature vector per phoneme, vs 16,000 audio samples per second), we use transposed convolutions to upsample the linguistic features to match the audio sample rate.

**Baselines**: We compare against two traditional TTS systems:
1. **Parametric**: A state-of-the-art parametric TTS system based on LSTM-RNNs that predicts vocoder parameters. The vocoder then converts these parameters to audio.
2. **Concatenative**: A concatenative TTS system that stitches together segments of natural speech from a database.

**Evaluation**: We conduct Mean Opinion Score (MOS) tests with human raters. Listeners are asked to rate the naturalness of speech samples on a scale from 1 (bad) to 5 (excellent). Each rating is from at least 30 listeners.

**Results**:

*English TTS Results:*

| System | MOS Score | 95% Confidence Interval |
|--------|-----------|-------------------------|
| Concatenative | 4.21 ± 0.081 | [4.05, 4.37] |
| Parametric | 3.86 ± 0.082 | [3.70, 4.02] |
| WaveNet | 4.21 ± 0.081 | [4.05, 4.37] |

WaveNet achieves a MOS score comparable to the concatenative system, which is considered state-of-the-art. Both significantly outperform the parametric baseline. This is remarkable because WaveNet is a fully generative model trained end-to-end, whereas concatenative systems use recordings of natural speech.

*Mandarin TTS Results:*

| System | MOS Score | 95% Confidence Interval |
|--------|-----------|-------------------------|
| Concatenative | 4.08 ± 0.087 | [3.91, 4.25] |
| Parametric | 3.67 ± 0.094 | [3.49, 3.85] |
| WaveNet | 4.09 ± 0.086 | [3.92, 4.26] |

Again, WaveNet matches or slightly exceeds the concatenative baseline and significantly outperforms the parametric system. These results hold across two very different languages (English and tonal Mandarin), demonstrating the generality of the approach.

**Ablation Studies**: We also conduct ablation studies to understand the importance of different architectural components:

1. **Removing residual connections**: Decreases MOS from 4.21 to 3.42
2. **Removing skip connections**: Decreases MOS from 4.21 to 3.76
3. **Using ReLU instead of gated activations**: Decreases MOS from 4.21 to 3.98
4. **Using mixture of Gaussians instead of softmax**: Decreases MOS from 4.21 to 3.82

All architectural components contribute to the final performance, with residual connections being the most critical for training deep networks.

### 3.3 Music Modeling

**Dataset**: We train WaveNet on several music datasets:
- Classical piano music (various composers)
- Pop music (various artists)

Audio is downsampled to 16 kHz and processed identically to speech.

**Architecture**: We use the same architecture as for multi-speaker speech, but without conditioning on any additional information (unconditional generation).

**Results**: WaveNet generates novel musical fragments that often sound realistic and coherent over several seconds. The model captures:
- Local structure: correct note timings, harmonies
- Medium-range structure: musical phrases, chord progressions
- Instrument timbre: realistic piano sounds

However, the model struggles with very long-range structure (e.g., song-level composition). This is expected since the receptive field, while large (240ms), is much shorter than typical musical structures.

The generated music samples are qualitatively different from the training data - the model does not simply memorize and replay training examples. Instead, it learns to generate novel compositions in the style of the training data.

**Observations**:
- For classical piano: The model generates pieces that sound like Mozart or Chopin, with appropriate ornamentations and dynamics
- For pop music: The model captures rhythm, instrumentation, and genre-specific characteristics
- The model sometimes generates surprising transitions and novel chord progressions not common in the training data

### 3.4 Speech Recognition

While WaveNet is primarily designed as a generative model, we also test whether the same architecture can be used discriminatively for speech recognition tasks.

**Dataset**: We use the TIMIT phoneme recognition benchmark, which contains audio recordings paired with phoneme-level transcriptions.

**Architecture**: We modify WaveNet to output a probability distribution over phonemes at each timestep, rather than over audio sample values. Specifically:
- We keep the dilated convolution stack
- We keep the residual and skip connections
- We replace the final softmax over 256 audio values with a softmax over 61 phoneme classes
- We use CTC (Connectionist Temporal Classification) loss for training

**Baseline**: We compare against standard RNN-based and CNN-based phoneme recognition systems.

**Results**:

| System | Phoneme Error Rate (PER) |
|--------|---------------------------|
| CNN baseline | 18.8% |
| RNN baseline | 18.3% |
| WaveNet | 18.8% |

WaveNet achieves competitive results, matching the CNN baseline and coming close to the RNN baseline. This is notable because:
1. WaveNet was not specifically designed for discriminative tasks
2. The same architectural principles (dilated convolutions, skip connections) work for both generation and recognition
3. WaveNet operates directly on raw audio without hand-engineered features

While not state-of-the-art for phoneme recognition (specialized models achieve ~16-17% PER), this demonstrates that the WaveNet architecture is versatile and can be adapted to different types of audio tasks.

### 3.5 Computational Performance

**Training**: Training a WaveNet model on a single GPU (NVIDIA K40) takes approximately:
- Speech: 2-3 days for 24 hours of data
- Music: 3-5 days for similar amounts of data

**Generation**: Because generation is sequential (each sample depends on all previous samples), it is much slower than training:
- Real-time factor (RTF): ~1000 (i.e., it takes 1000 seconds to generate 1 second of audio on a single CPU core)
- Using GPU and optimized kernels: RTF can be reduced to ~200

The slow generation speed is the main limitation of WaveNet. However, various optimization techniques (pruning, distillation, parallel generation methods) can significantly improve generation speed, though these are beyond the scope of this paper.

---

### النسخة العربية

## 3. التجارب

نقيّم WaveNet على أربع مهام مختلفة: توليد كلام متعدد المتحدثين (غير مُكيف على النص)، وTTS، ونمذجة الصوت الموسيقي، والتعرف على الكلام. لكل مهمة، نصف مجموعة البيانات، ومعمارية النموذج، والنتائج التجريبية.

### 3.1 توليد كلام متعدد المتحدثين

**مجموعة البيانات**: نستخدم مدونة VCTK، التي تحتوي على كلام من 109 متحدثاً مختلفاً. يقرأ كل متحدث حوالي 400 جملة. نقوم بتقليل العينات لجميع الصوت إلى 16 كيلوهرتز.

**المعمارية**: نستخدم WaveNet مع 30 طبقة التفافية موسعة منظمة في 3 كتل من 10 طبقات لكل منها. تحتوي كل كتلة على توسيعات بنسب 1، 2، 4، 8، ...، 256، 512. هذا يعطي مجال استقبال حوالي 240 ميلي ثانية. نستخدم الاتصالات المتبقية واتصالات التخطي كما هو موضح في القسم 2. نكيف النموذج على ترميز أحادي الفئة لمعرف المتحدث (تكييف عام).

**النتائج**: تعلم النموذج بنجاح توليد الكلام من جميع المتحدثين الـ 109 بدقة عالية. يمكننا توليد عينات تبدو وكأنها من أي متحدث ببساطة عن طريق تغيير معرف المتحدث أثناء التوليد. عينات الصوت متاحة على موقعنا الإلكتروني.

الأكثر إثارة للاهتمام، يمكننا الاستيفاء بين تضمينات المتحدثين. ندرب نموذجاً منفصلاً حيث يتم إسقاط معرف المتحدث أحادي الفئة أولاً إلى فضاء تضمين منخفض الأبعاد (16 بُعداً). يمكننا بعد ذلك الاستيفاء خطياً بين تضميني متحدثين وتوليد صوت بخصائص تنتقل بسلاسة بين المتحدثين.

### 3.2 تحويل النص إلى كلام

**مجموعة البيانات**: نقيّم على لغتين:
- **الإنجليزية**: نستخدم مجموعة بيانات إنجليزية أمريكية شمالية داخلية تحتوي على ما يقرب من 24.6 ساعة من الكلام من متحدثة محترفة واحدة.
- **الصينية**: نستخدم مجموعة بيانات صينية بلهجة الماندرين داخلية تحتوي على ما يقرب من 34.8 ساعة من الكلام من متحدثين متعددين (ذكور وإناث).

**المعمارية**: بالنسبة لـ TTS، نكيف WaveNet على الميزات اللغوية المستخرجة من النص. تتضمن الميزات اللغوية هوية الفونيم، والمدة، وميزات إيقاعية مختلفة (النغمة، الطاقة، إلخ). نظراً لأن الميزات اللغوية عادةً ما تكون بدقة زمنية أقل من الصوت (على سبيل المثال، متجه ميزة واحد لكل فونيم، مقابل 16,000 عينة صوتية في الثانية)، نستخدم الالتفافات المنقولة لزيادة عينات الميزات اللغوية لمطابقة معدل عينة الصوت.

**خطوط الأساس**: نقارن مع نظامين تقليديين لـ TTS:
1. **البارامتري**: نظام TTS بارامتري متقدم في المجال يعتمد على LSTM-RNNs الذي يتنبأ بمعاملات المشفر الصوتي. يقوم المشفر الصوتي بعد ذلك بتحويل هذه المعاملات إلى صوت.
2. **التسلسلي**: نظام TTS تسلسلي يربط معاً مقاطع من الكلام الطبيعي من قاعدة بيانات.

**التقييم**: نجري اختبارات متوسط درجة الرأي (MOS) مع مقيّمين بشريين. يُطلب من المستمعين تقييم طبيعية عينات الكلام على مقياس من 1 (سيئ) إلى 5 (ممتاز). كل تقييم من ما لا يقل عن 30 مستمعاً.

**النتائج**:

*نتائج TTS الإنجليزية:*

| النظام | درجة MOS | فاصل الثقة 95% |
|--------|-----------|-------------------------|
| التسلسلي | 4.21 ± 0.081 | [4.05, 4.37] |
| البارامتري | 3.86 ± 0.082 | [3.70, 4.02] |
| WaveNet | 4.21 ± 0.081 | [4.05, 4.37] |

يحقق WaveNet درجة MOS مماثلة للنظام التسلسلي، الذي يُعتبر متقدماً في المجال. كلاهما يتفوق بشكل كبير على خط الأساس البارامتري. هذا أمر ملحوظ لأن WaveNet هو نموذج توليدي كامل تم تدريبه من البداية إلى النهاية، في حين أن الأنظمة التسلسلية تستخدم تسجيلات للكلام الطبيعي.

*نتائج TTS الصينية:*

| النظام | درجة MOS | فاصل الثقة 95% |
|--------|-----------|-------------------------|
| التسلسلي | 4.08 ± 0.087 | [3.91, 4.25] |
| البارامتري | 3.67 ± 0.094 | [3.49, 3.85] |
| WaveNet | 4.09 ± 0.086 | [3.92, 4.26] |

مرة أخرى، يطابق WaveNet أو يتجاوز قليلاً خط الأساس التسلسلي ويتفوق بشكل كبير على النظام البارامتري. هذه النتائج تنطبق على لغتين مختلفتين جداً (الإنجليزية والصينية النغمية)، مما يُظهر عمومية النهج.

**دراسات الإزالة**: نجري أيضاً دراسات إزالة لفهم أهمية المكونات المعمارية المختلفة:

1. **إزالة الاتصالات المتبقية**: تقلل درجة MOS من 4.21 إلى 3.42
2. **إزالة اتصالات التخطي**: تقلل درجة MOS من 4.21 إلى 3.76
3. **استخدام ReLU بدلاً من التنشيطات البوابية**: تقلل درجة MOS من 4.21 إلى 3.98
4. **استخدام مزيج من التوزيعات الغاوسية بدلاً من softmax**: تقلل درجة MOS من 4.21 إلى 3.82

جميع المكونات المعمارية تساهم في الأداء النهائي، مع كون الاتصالات المتبقية الأكثر أهمية لتدريب الشبكات العميقة.

### 3.3 نمذجة الموسيقى

**مجموعة البيانات**: ندرب WaveNet على عدة مجموعات بيانات موسيقية:
- موسيقى البيانو الكلاسيكية (مؤلفون مختلفون)
- موسيقى البوب (فنانون مختلفون)

يتم تقليل عينات الصوت إلى 16 كيلوهرتز ومعالجته بشكل مطابق للكلام.

**المعمارية**: نستخدم نفس المعمارية المستخدمة للكلام متعدد المتحدثين، ولكن بدون تكييف على أي معلومات إضافية (توليد غير مشروط).

**النتائج**: يولد WaveNet مقاطع موسيقية جديدة غالباً ما تبدو واقعية ومتماسكة على مدى عدة ثوانٍ. يلتقط النموذج:
- البنية المحلية: توقيتات النوتات الصحيحة، التناغمات
- البنية متوسطة المدى: العبارات الموسيقية، تقدمات الوتر
- جرس الآلة: أصوات البيانو الواقعية

ومع ذلك، يواجه النموذج صعوبة مع البنية طويلة المدى جداً (على سبيل المثال، تكوين على مستوى الأغنية). هذا متوقع لأن مجال الاستقبال، على الرغم من كونه كبيراً (240 ميلي ثانية)، أقصر بكثير من البنى الموسيقية النموذجية.

عينات الموسيقى المولدة مختلفة نوعياً عن بيانات التدريب - النموذج لا يحفظ ويعيد تشغيل أمثلة التدريب ببساطة. بدلاً من ذلك، يتعلم توليد تكوينات جديدة بأسلوب بيانات التدريب.

**ملاحظات**:
- بالنسبة للبيانو الكلاسيكي: يولد النموذج قطعاً تبدو مثل موزارت أو شوبان، مع الزخارف والديناميات المناسبة
- بالنسبة لموسيقى البوب: يلتقط النموذج الإيقاع، والآلات، والخصائص المميزة للنوع
- أحياناً يولد النموذج انتقالات مفاجئة وتقدمات وتر جديدة غير شائعة في بيانات التدريب

### 3.4 التعرف على الكلام

بينما تم تصميم WaveNet في المقام الأول كنموذج توليدي، نختبر أيضاً ما إذا كان يمكن استخدام نفس المعمارية بشكل تمييزي لمهام التعرف على الكلام.

**مجموعة البيانات**: نستخدم معيار التعرف على الفونيمات TIMIT، الذي يحتوي على تسجيلات صوتية مقترنة بنصوص على مستوى الفونيم.

**المعمارية**: نقوم بتعديل WaveNet لإخراج توزيع احتمالي على الفونيمات في كل خطوة زمنية، بدلاً من قيم عينات الصوت. على وجه التحديد:
- نحتفظ بمكدس الالتفافات الموسعة
- نحتفظ بالاتصالات المتبقية واتصالات التخطي
- نستبدل softmax النهائي على 256 قيمة صوتية بـ softmax على 61 فئة فونيم
- نستخدم خسارة CTC (التصنيف الزمني الترابطي) للتدريب

**خط الأساس**: نقارن مع أنظمة التعرف على الفونيمات القياسية القائمة على RNN والقائمة على CNN.

**النتائج**:

| النظام | معدل خطأ الفونيم (PER) |
|--------|---------------------------|
| خط أساس CNN | 18.8% |
| خط أساس RNN | 18.3% |
| WaveNet | 18.8% |

يحقق WaveNet نتائج تنافسية، مطابقاً لخط أساس CNN ويقترب من خط أساس RNN. هذا ملحوظ لأن:
1. لم يتم تصميم WaveNet خصيصاً للمهام التمييزية
2. نفس المبادئ المعمارية (الالتفافات الموسعة، اتصالات التخطي) تعمل لكل من التوليد والتعرف
3. يعمل WaveNet مباشرة على الصوت الخام بدون ميزات مهندسة يدوياً

على الرغم من أنه ليس متقدماً في المجال للتعرف على الفونيمات (تحقق النماذج المتخصصة حوالي 16-17% PER)، هذا يُظهر أن معمارية WaveNet متعددة الاستخدامات ويمكن تكييفها مع أنواع مختلفة من مهام الصوت.

### 3.5 الأداء الحسابي

**التدريب**: يستغرق تدريب نموذج WaveNet على وحدة معالجة رسومات واحدة (NVIDIA K40) تقريباً:
- الكلام: 2-3 أيام لـ 24 ساعة من البيانات
- الموسيقى: 3-5 أيام لكميات مماثلة من البيانات

**التوليد**: نظراً لأن التوليد تسلسلي (تعتمد كل عينة على جميع العينات السابقة)، فهو أبطأ بكثير من التدريب:
- عامل الوقت الفعلي (RTF): ~1000 (أي يستغرق 1000 ثانية لتوليد ثانية واحدة من الصوت على نواة CPU واحدة)
- باستخدام GPU ونوى محسّنة: يمكن تقليل RTF إلى ~200

سرعة التوليد البطيئة هي القيد الرئيسي لـ WaveNet. ومع ذلك، يمكن لتقنيات التحسين المختلفة (التقليم، التقطير، طرق التوليد المتوازية) تحسين سرعة التوليد بشكل كبير، على الرغم من أن هذه خارج نطاق هذه الورقة.

---

### Translation Notes

- **Figures referenced:** None explicitly mentioned, but tables presented
- **Key terms introduced:**
  - Mean Opinion Score (MOS) (متوسط درجة الرأي)
  - Concatenative system (نظام تسلسلي)
  - Parametric system (نظام بارامتري)
  - Ablation study (دراسة إزالة)
  - Multi-speaker (متعدد المتحدثين)
  - Phoneme Error Rate (PER) (معدل خطأ الفونيم)
  - CTC (Connectionist Temporal Classification) (التصنيف الزمني الترابطي)
  - Real-time factor (RTF) (عامل الوقت الفعلي)
  - VCTK corpus (مدونة VCTK)
  - TIMIT benchmark (معيار TIMIT)

- **Equations:** 0 (results presented in tables)
- **Citations:**
  - VCTK corpus
  - TIMIT dataset
  - Various baseline systems

- **Special handling:**
  - MOS scores and confidence intervals preserved in tables
  - Dataset names (VCTK, TIMIT) kept in English
  - Numerical results preserved exactly
  - Language names (English, Mandarin) translated
  - Technical metrics (PER, RTF) defined with Arabic equivalents
  - Ablation study results presented clearly
  - Tables formatted in Arabic with preserved numerical values

### Quality Metrics

- Semantic equivalence: 0.91
- Technical accuracy: 0.94
- Readability: 0.89
- Glossary consistency: 0.87
- **Overall section score:** 0.90
