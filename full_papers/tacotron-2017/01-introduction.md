# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.89
**Glossary Terms Used:** neural network, encoder, decoder, attention mechanism, sequence, architecture, text-to-speech, end-to-end

---

### English Version

Modern text-to-speech (TTS) pipelines are complex and involve multiple stages. A typical production TTS system consists of a text frontend extracting various linguistic features, a duration model, an acoustic feature prediction model, and a complex signal-processing-based vocoder. Building these components often requires extensive domain expertise and may contain brittle design choices. Furthermore, since these components are trained independently, errors from each component compound.

An integrated end-to-end model that can be trained on <text, audio> pairs with minimal human annotation offers several advantages. First, such a model reduces the need for laborious feature engineering, which may involve heuristics and brittle design choices. Second, it more easily allows for rich conditioning on various attributes, such as speaker or language, or high-level features like sentiment. This is because conditioning can occur at the very beginning of the model rather than only on certain components. Similarly, adaptation to new data might also be easier. Finally, a single model is likely to be more robust than a multi-stage model where each component's errors can compound. These advantages imply that an end-to-end model could allow us to train on huge amounts of rich, expressive yet often noisy data found in the real world.

TTS is a large-scale inverse problem: a highly compressed source (text) is "decompressed" into audio. Since the same text can correspond to different pronunciations or speaking styles (e.g., the word "read" can be pronounced as /ɹid/ or /ɹɛd/ depending on context), this is a particularly difficult learning problem for an end-to-end model: it must cope with large variations at the signal level for a given input. Moreover, unlike end-to-end speech recognition or machine translation, TTS outputs are continuous, and output sequences are usually much longer than those of the input. These attributes cause prediction errors to accumulate quickly.

In this paper, we propose Tacotron, an end-to-end generative TTS model based on the sequence-to-sequence (seq2seq) with attention paradigm. Our model takes characters as input and outputs the corresponding raw spectrogram, which is then fed to the Griffin-Lim reconstruction algorithm to synthesize speech. Given <text, audio> pairs, Tacotron can be trained completely from scratch with random initialization. It does not require phoneme-level alignment, so it can easily scale to using large amounts of acoustic data with transcripts. With a simple waveform synthesis technique, it achieves a 3.82 mean opinion score (MOS) on US English, outperforming a production parametric system in terms of naturalness. In addition, since Tacotron generates speech at the frame level, it's substantially faster than sample-level autoregressive methods.

---

### النسخة العربية

تتسم خطوط معالجة توليف الكلام من النص (TTS) الحديثة بالتعقيد وتتضمن مراحل متعددة. يتكون نظام TTS الإنتاجي النموذجي من واجهة أمامية للنص تستخرج ميزات لغوية متنوعة، ونموذج للمدة الزمنية، ونموذج للتنبؤ بالميزات الصوتية، ومُركِّب صوتي (vocoder) معقد قائم على معالجة الإشارات. غالباً ما يتطلب بناء هذه المكونات خبرة واسعة في المجال وقد يحتوي على خيارات تصميمية هشة. علاوة على ذلك، نظراً لأن هذه المكونات يتم تدريبها بشكل مستقل، فإن الأخطاء من كل مكون تتراكم.

يقدم النموذج المتكامل من طرف إلى طرف الذي يمكن تدريبه على أزواج <النص، الصوت> بأقل قدر من التعليقات التوضيحية البشرية عدة مزايا. أولاً، يقلل هذا النموذج من الحاجة إلى هندسة الميزات الشاقة، والتي قد تتضمن استدلالات وخيارات تصميمية هشة. ثانياً، يسمح بسهولة أكبر بالإشراط الغني على سمات متنوعة، مثل المتحدث أو اللغة، أو الميزات عالية المستوى مثل المشاعر. ذلك لأن الإشراط يمكن أن يحدث في بداية النموذج مباشرة بدلاً من المكونات المعينة فقط. وبالمثل، قد يكون التكيف مع البيانات الجديدة أسهل أيضاً. أخيراً، من المرجح أن يكون النموذج الواحد أكثر قوة من نموذج متعدد المراحل حيث يمكن أن تتراكم أخطاء كل مكون. تشير هذه المزايا إلى أن النموذج من طرف إلى طرف يمكن أن يسمح لنا بالتدريب على كميات هائلة من البيانات الغنية والمعبرة ولكن غالباً ما تكون صاخبة الموجودة في العالم الحقيقي.

يعد توليف الكلام من النص مسألة عكسية واسعة النطاق: يتم "فك ضغط" مصدر مضغوط للغاية (النص) إلى صوت. نظراً لأن النص نفسه يمكن أن يتوافق مع نطق مختلف أو أساليب تحدث مختلفة (على سبيل المثال، يمكن نطق كلمة "read" كـ /ɹid/ أو /ɹɛd/ اعتماداً على السياق)، فإن هذه مسألة تعلم صعبة بشكل خاص بالنسبة للنموذج من طرف إلى طرف: يجب أن يتعامل مع تباينات كبيرة على مستوى الإشارة لمدخل معين. علاوة على ذلك، على عكس التعرف على الكلام من طرف إلى طرف أو الترجمة الآلية، فإن مخرجات TTS مستمرة، وعادةً ما تكون تسلسلات المخرجات أطول بكثير من تسلسلات المدخلات. تتسبب هذه السمات في تراكم أخطاء التنبؤ بسرعة.

في هذا البحث، نقترح تاكوترون (Tacotron)، وهو نموذج توليدي من طرف إلى طرف لتوليف الكلام من النص بناءً على نموذج التسلسل إلى التسلسل (seq2seq) مع آلية الانتباه. يأخذ نموذجنا الأحرف كمدخل ويُخرج المخطط الطيفي الخام المقابل، والذي يتم إدخاله بعد ذلك إلى خوارزمية إعادة البناء Griffin-Lim لتوليف الكلام. عند إعطاء أزواج <النص، الصوت>، يمكن تدريب تاكوترون بالكامل من الصفر مع التهيئة العشوائية. لا يتطلب محاذاة على مستوى الفونيم، لذا يمكنه التوسع بسهولة لاستخدام كميات كبيرة من البيانات الصوتية مع النصوص المكتوبة. مع تقنية توليف موجي بسيطة، يحقق 3.82 في متوسط تقييم الرأي (MOS) للغة الإنجليزية الأمريكية، متفوقاً على نظام بارامتري إنتاجي من حيث الطبيعية. بالإضافة إلى ذلك، نظراً لأن تاكوترون يولد الكلام على مستوى الإطار، فإنه أسرع بكثير من الطرق الانحدارية الذاتية على مستوى العينة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - text-to-speech (TTS): توليف الكلام من النص
  - vocoder: مُركِّب صوتي
  - end-to-end model: النموذج من طرف إلى طرف
  - feature engineering: هندسة الميزات
  - conditioning: الإشراط
  - inverse problem: مسألة عكسية
  - sequence-to-sequence (seq2seq): التسلسل إلى التسلسل
  - spectrogram: المخطط الطيفي
  - Griffin-Lim algorithm: خوارزمية Griffin-Lim
  - phoneme-level alignment: محاذاة على مستوى الفونيم
  - mean opinion score (MOS): متوسط تقييم الرأي
  - frame level: مستوى الإطار
  - sample-level autoregressive: الانحدارية الذاتية على مستوى العينة
- **Equations:** 0
- **Citations:** 0
- **Special handling:** Preserved IPA phonetic symbols (/ɹid/, /ɹɛd/) and technical terms like "Griffin-Lim" in original form

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.91
- Readability: 0.88
- Glossary consistency: 0.87
- **Overall section score:** 0.89
