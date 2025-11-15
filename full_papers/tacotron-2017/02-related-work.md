# Section 2: Related Work
## القسم 2: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.88
**Glossary Terms Used:** neural network, autoregressive, encoder, decoder, vocoder, spectrogram, alignment

---

### English Version

WaveNet is a powerful generative model of audio. It works well for TTS, but is slow due to its sample-level autoregressive nature. It also requires conditioning on linguistic features from an existing TTS frontend, and thus is not end-to-end: it only replaces the vocoder and acoustic model. Another recently-developed neural model is DeepVoice, which replaces every component in a typical TTS pipeline by a corresponding neural network. However, each component is independently trained, and it's nontrivial to change the system to train in an end-to-end fashion.

To our knowledge, Wang et al. is the earliest work touching end-to-end TTS using seq2seq with attention. However, it requires a pre-trained hidden Markov model (HMM) aligner to help the seq2seq model learn the alignment. It's unclear whether the model can learn to align without this guidance. Second, a few tricks are used to get the model trained, which the authors note hurts prosody. Third, it predicts vocoder parameters hence needs a vocoder. Furthermore, the model is trained on phoneme inputs and the experimental results seem to be somewhat limited.

Char2Wav is an independently-developed end-to-end model that can be trained on characters. However, Char2Wav still predicts vocoder parameters before using a SampleRNN neural vocoder, whereas Tacotron directly predicts raw spectrogram. Also, their seq2seq and SampleRNN models need to be separately pre-trained, but our model can be trained from scratch. Finally, we made several key modifications to the vanilla seq2seq paradigm. As shown later, a vanilla seq2seq model does not work well for character-level inputs.

---

### النسخة العربية

يُعد WaveNet نموذجاً توليدياً قوياً للصوت. يعمل بشكل جيد لتوليف الكلام من النص، لكنه بطيء بسبب طبيعته الانحدارية الذاتية على مستوى العينة. كما يتطلب الإشراط على الميزات اللغوية من واجهة أمامية موجودة لتوليف الكلام من النص، وبالتالي فهو ليس من طرف إلى طرف: فهو يستبدل فقط المُركِّب الصوتي والنموذج الصوتي. نموذج عصبي آخر تم تطويره مؤخراً هو DeepVoice، الذي يستبدل كل مكون في خط معالجة TTS النموذجي بشبكة عصبية مقابلة. ومع ذلك، يتم تدريب كل مكون بشكل مستقل، وليس من السهل تغيير النظام للتدريب بطريقة من طرف إلى طرف.

على حد علمنا، يُعد عمل Wang وآخرون أقدم عمل يتطرق إلى توليف الكلام من النص من طرف إلى طرف باستخدام seq2seq مع آلية الانتباه. ومع ذلك، يتطلب محاذياً مُدرباً مسبقاً لنموذج ماركوف المخفي (HMM) لمساعدة نموذج seq2seq على تعلم المحاذاة. من غير الواضح ما إذا كان النموذج يمكنه تعلم المحاذاة دون هذا التوجيه. ثانياً، يتم استخدام بعض الحيل لتدريب النموذج، والتي يشير المؤلفون إلى أنها تضر بالنبر. ثالثاً، يتنبأ بمعاملات المُركِّب الصوتي وبالتالي يحتاج إلى مُركِّب صوتي. علاوة على ذلك، يتم تدريب النموذج على مدخلات الفونيم ويبدو أن النتائج التجريبية محدودة إلى حد ما.

Char2Wav هو نموذج من طرف إلى طرف تم تطويره بشكل مستقل ويمكن تدريبه على الأحرف. ومع ذلك، لا يزال Char2Wav يتنبأ بمعاملات المُركِّب الصوتي قبل استخدام مُركِّب صوتي عصبي SampleRNN، بينما يتنبأ تاكوترون مباشرة بالمخطط الطيفي الخام. أيضاً، نماذج seq2seq وSampleRNN الخاصة بهم تحتاج إلى تدريب مسبق منفصل، لكن نموذجنا يمكن تدريبه من الصفر. أخيراً، أجرينا عدة تعديلات رئيسية على نموذج seq2seq الأساسي. كما هو موضح لاحقاً، لا يعمل نموذج seq2seq الأساسي بشكل جيد للمدخلات على مستوى الأحرف.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - WaveNet: ويف نت (kept in English with Arabic article)
  - sample-level autoregressive: الانحدارية الذاتية على مستوى العينة
  - DeepVoice: ديب فويس (kept in English with Arabic article)
  - hidden Markov model (HMM): نموذج ماركوف المخفي
  - prosody: النبر
  - Char2Wav: تشار تو واف (kept in English)
  - SampleRNN: سامبل آر إن إن (kept in English)
  - vanilla seq2seq: seq2seq الأساسي
  - character-level inputs: المدخلات على مستوى الأحرف
- **Equations:** 0
- **Citations:** Multiple references to Wang et al., WaveNet, DeepVoice, Char2Wav
- **Special handling:** Kept model names (WaveNet, DeepVoice, Char2Wav, SampleRNN) in English as they are proper names

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88
