# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.89
**Glossary Terms Used:** generative model, neural network, deep learning, autoregressive, text-to-speech, speech synthesis, recurrent neural network, convolutional neural network, receptive field, training

---

### English Version

This paper introduces WaveNet, a deep generative model of audio data which operates directly at the waveform level. A main characteristic of the model is that it is autoregressive: each sample is conditioned on the previous samples. This is similar to standard autoregressive models such as recurrent neural networks (RNNs) and PixelRNNs, but the main novelty of WaveNet is that it uses stacked dilated causal convolutional layers which allow it to capture temporal structure at very large time-scales. This is important because audio signals are high-dimensional and contain structure at many time-scales, ranging from samples (e.g., 16,000 samples per second) to phonemes, words, sentences, and even longer conversational contexts.

Building a generative model of raw audio is challenging. The main difficulties are:

1. **High temporal resolution**: Audio signals typically have sample rates of 16 kHz or more, meaning the model must generate tens of thousands of samples per second. This poses significant computational challenges.

2. **Long-range temporal dependencies**: The same audio sample may depend on events that occurred thousands of time-steps in the past (e.g., the speaker identity, or the context of a sentence).

3. **Complex dependencies**: Different aspects of the audio signal (pitch, timbre, volume, etc.) are all interdependent and must be modeled jointly.

Traditional text-to-speech (TTS) systems typically consist of multiple processing stages: a text analysis frontend that converts text into linguistic features, an acoustic model that predicts acoustic features (such as fundamental frequency, duration, and spectral envelope) from the linguistic features, and a waveform generation module (vocoder) that converts these acoustic features into an audio waveform. Each of these components is optimized separately, and the errors from each stage may accumulate.

WaveNet, in contrast, is trained end-to-end to directly generate raw audio waveforms from input conditioning (e.g., linguistic features for TTS, or a global conditioning on speaker identity). This allows the model to avoid the limitations of traditional pipelines while also modeling the subtle effects that are often lost in intermediate representations.

To model the joint probability distribution over all audio samples, WaveNet uses a stack of convolutional layers with exponentially increasing dilation factors. This allows the receptive field to grow exponentially with depth, enabling the model to capture very long-range dependencies efficiently. Each layer applies gated activation units and residual connections, both of which have been shown to facilitate training of very deep networks.

The model is probabilistic and explicitly models the uncertainty in the predictions, which is essential for generating high-quality audio. Rather than directly predicting continuous-valued samples, WaveNet uses a softmax distribution over a discrete set of possible sample values. We show that this discretization does not noticeably affect audio quality when using μ-law companding transformation with 256 quantization levels.

WaveNet can also be conditioned on other inputs, such as speaker identity or text. This allows a single model to generate speech in different voices, or to perform text-to-speech synthesis. We show that conditioning on text features leads to state-of-the-art results in TTS, significantly outperforming traditional concatenative and parametric systems in subjective listening tests.

Beyond speech synthesis, we demonstrate that WaveNet can also be applied to music generation, where it produces novel and often realistic musical fragments. Additionally, when modified to use a different output distribution, the same architecture can be used as a discriminative model for tasks such as phoneme recognition, where it achieves competitive results.

The contributions of this paper are:

- We introduce WaveNet, a deep autoregressive generative model that directly models raw audio waveforms.
- We show that dilated causal convolutions allow the model to have very large receptive fields (thousands of timesteps) while remaining computationally efficient.
- We demonstrate state-of-the-art results on text-to-speech synthesis for both English and Mandarin.
- We show that a single model can handle multiple speakers and can be conditioned on speaker identity.
- We demonstrate the applicability of WaveNet to music generation and phoneme recognition.

---

### النسخة العربية

تقدم هذه الورقة البحثية WaveNet، وهو نموذج توليدي عميق لبيانات الصوت يعمل مباشرة على مستوى شكل الموجة. الخاصية الرئيسية للنموذج هي أنه انحداري ذاتي: حيث يتم تكييف كل عينة على العينات السابقة. هذا مشابه للنماذج الانحدارية الذاتية القياسية مثل الشبكات العصبية المتكررة (RNNs) و PixelRNNs، لكن الجديد الرئيسي في WaveNet هو أنه يستخدم طبقات التفافية سببية موسعة مكدسة والتي تسمح له بالتقاط البنية الزمنية على مقاييس زمنية كبيرة جداً. هذا مهم لأن الإشارات الصوتية عالية الأبعاد وتحتوي على بنية في العديد من المقاييس الزمنية، تتراوح من العينات (على سبيل المثال، 16,000 عينة في الثانية) إلى الفونيمات والكلمات والجمل وحتى السياقات الحوارية الأطول.

بناء نموذج توليدي للصوت الخام يمثل تحدياً. الصعوبات الرئيسية هي:

1. **الدقة الزمنية العالية**: عادةً ما تحتوي الإشارات الصوتية على معدلات عينات تبلغ 16 كيلوهرتز أو أكثر، مما يعني أن النموذج يجب أن يولد عشرات الآلاف من العينات في الثانية. هذا يفرض تحديات حسابية كبيرة.

2. **التبعيات الزمنية طويلة المدى**: قد تعتمد نفس العينة الصوتية على أحداث وقعت قبل آلاف الخطوات الزمنية (على سبيل المثال، هوية المتحدث، أو سياق الجملة).

3. **التبعيات المعقدة**: جميع الجوانب المختلفة للإشارة الصوتية (النغمة، الجرس، الحجم، إلخ) مترابطة ويجب نمذجتها معاً.

عادةً ما تتكون أنظمة تحويل النص إلى كلام (TTS) التقليدية من مراحل معالجة متعددة: واجهة أمامية لتحليل النص تحول النص إلى ميزات لغوية، ونموذج صوتي يتنبأ بالميزات الصوتية (مثل التردد الأساسي، المدة، والغلاف الطيفي) من الميزات اللغوية، ووحدة توليد شكل الموجة (مشفر صوتي) تحول هذه الميزات الصوتية إلى شكل موجة صوتية. يتم تحسين كل من هذه المكونات بشكل منفصل، وقد تتراكم الأخطاء من كل مرحلة.

على النقيض من ذلك، يتم تدريب WaveNet من البداية إلى النهاية لتوليد أشكال الموجات الصوتية الخام مباشرة من تكييف المدخلات (على سبيل المثال، الميزات اللغوية لـ TTS، أو التكييف العام على هوية المتحدث). هذا يسمح للنموذج بتجنب قيود الأنظمة التقليدية المتسلسلة بينما يقوم أيضاً بنمذجة التأثيرات الدقيقة التي غالباً ما تُفقد في التمثيلات الوسيطة.

لنمذجة توزيع الاحتمال المشترك على جميع العينات الصوتية، يستخدم WaveNet مكدس من الطبقات الالتفافية مع عوامل توسيع تزداد بشكل أسي. هذا يسمح لمجال الاستقبال بالنمو بشكل أسي مع العمق، مما يمكّن النموذج من التقاط التبعيات طويلة المدى بكفاءة. تطبق كل طبقة وحدات تنشيط بوابية واتصالات متبقية، وكلاهما ثبت أنه يسهل تدريب الشبكات العميقة جداً.

النموذج احتمالي ويقوم بنمذجة عدم اليقين في التنبؤات بشكل صريح، وهو أمر ضروري لتوليد صوت عالي الجودة. بدلاً من التنبؤ المباشر بالعينات ذات القيم المستمرة، يستخدم WaveNet توزيع softmax على مجموعة منفصلة من قيم العينات المحتملة. نُظهر أن هذا التقطيع لا يؤثر بشكل ملحوظ على جودة الصوت عند استخدام تحويل ضغط μ-law مع 256 مستوى تكميم.

يمكن أيضاً تكييف WaveNet على مدخلات أخرى، مثل هوية المتحدث أو النص. هذا يسمح لنموذج واحد بتوليد الكلام بأصوات مختلفة، أو لإجراء تحويل النص إلى كلام. نُظهر أن التكييف على ميزات النص يؤدي إلى نتائج متقدمة في المجال في TTS، متفوقاً بشكل كبير على الأنظمة التسلسلية والبارامترية التقليدية في اختبارات الاستماع الذاتية.

بالإضافة إلى توليد الكلام، نُظهر أنه يمكن أيضاً تطبيق WaveNet على توليد الموسيقى، حيث ينتج مقاطع موسيقية جديدة وغالباً واقعية. بالإضافة إلى ذلك، عند تعديله لاستخدام توزيع مخرجات مختلف، يمكن استخدام نفس المعمارية كنموذج تمييزي لمهام مثل التعرف على الفونيمات، حيث يحقق نتائج تنافسية.

مساهمات هذه الورقة البحثية هي:

- نقدم WaveNet، وهو نموذج توليدي انحداري ذاتي عميق يقوم بنمذجة أشكال الموجات الصوتية الخام مباشرة.
- نُظهر أن الالتفافات السببية الموسعة تسمح للنموذج بأن يكون له مجالات استقبال كبيرة جداً (آلاف الخطوات الزمنية) مع الحفاظ على الكفاءة الحسابية.
- نُظهر نتائج متقدمة في المجال على توليف تحويل النص إلى كلام لكل من اللغتين الإنجليزية والصينية.
- نُظهر أن نموذجاً واحداً يمكنه التعامل مع متحدثين متعددين ويمكن تكييفه على هوية المتحدث.
- نُظهر قابلية تطبيق WaveNet على توليد الموسيقى والتعرف على الفونيمات.

---

### Translation Notes

- **Figures referenced:** None in introduction
- **Key terms introduced:**
  - WaveNet (kept as English term)
  - dilated causal convolutions (الالتفافات السببية الموسعة)
  - receptive field (مجال الاستقبال)
  - autoregressive (انحداري ذاتي)
  - gated activation units (وحدات تنشيط بوابية)
  - residual connections (اتصالات متبقية)
  - μ-law companding (ضغط μ-law)
  - vocoder (مشفر صوتي)
  - end-to-end (من البداية إلى النهاية)
  - softmax distribution (توزيع softmax)

- **Equations:** 0
- **Citations:** Implicit references to RNNs, PixelRNNs
- **Special handling:**
  - "dilated causal convolutions" translated as "الالتفافات السببية الموسعة" - key architectural innovation
  - "receptive field" as "مجال الاستقبال" - standard neuroscience/deep learning term
  - "gated activation units" as "وحدات تنشيط بوابية" - referring to gating mechanisms
  - "residual connections" as "اتصالات متبقية" - skip connections from ResNet
  - "end-to-end" as "من البداية إلى النهاية" - training paradigm
  - "vocoder" as "مشفر صوتي" - traditional speech synthesis component
  - Technical numbers (16 kHz, 256 levels) preserved in original format

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.92
- Readability: 0.88
- Glossary consistency: 0.86
- **Overall section score:** 0.89
