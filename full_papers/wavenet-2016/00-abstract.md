# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.92
**Glossary Terms Used:** deep learning, neural network, autoregressive, text-to-speech, generative model, training, probabilistic, conditioning

---

### English Version

This paper introduces WaveNet, a deep neural network for generating raw audio waveforms. The model is fully probabilistic and autoregressive, with the predictive distribution for each audio sample conditioned on all previous ones; nonetheless we show that it can be efficiently trained on data with tens of thousands of samples per second. When applied to text-to-speech (TTS), it yields state-of-the-art performance, with human listeners rating it as significantly more natural sounding than the best parametric and concatenative systems for both English and Mandarin. A single WaveNet can capture the characteristics of many different speakers with equal fidelity, and can switch between them by conditioning on the speaker identity. When trained to model music, we find that it generates novel and often highly realistic musical fragments. We also show that it can be employed as a discriminative model, returning promising results for phoneme recognition.

---

### النسخة العربية

تقدم هذه الورقة البحثية WaveNet، وهي شبكة عصبية عميقة لتوليد أشكال الموجات الصوتية الخام. يعمل النموذج بشكل احتمالي كامل وانحداري ذاتي، حيث يتم تكييف التوزيع التنبؤي لكل عينة صوتية على جميع العينات السابقة؛ ومع ذلك نُظهر أنه يمكن تدريبه بكفاءة على بيانات تحتوي على عشرات الآلاف من العينات في الثانية. عند تطبيقه على تحويل النص إلى كلام (TTS)، يحقق أداءً متقدماً في المجال، حيث يصنفه المستمعون البشريون على أنه أكثر طبيعية بشكل ملحوظ من أفضل الأنظمة البارامترية والتسلسلية لكل من اللغتين الإنجليزية والصينية. يمكن لنموذج WaveNet واحد التقاط خصائص العديد من المتحدثين المختلفين بدقة متساوية، ويمكنه التبديل بينهم من خلال التكييف على هوية المتحدث. عند تدريبه على نمذجة الموسيقى، نجد أنه يولد مقاطع موسيقية جديدة وغالباً واقعية للغاية. كما نُظهر أيضاً أنه يمكن استخدامه كنموذج تمييزي، مما يعطي نتائج واعدة للتعرف على الفونيمات.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:** WaveNet, raw audio waveforms, autoregressive model, text-to-speech (TTS), parametric systems, concatenative systems, speaker conditioning, phoneme recognition
- **Equations:** 0
- **Citations:** 0
- **Special handling:**
  - "raw audio waveforms" translated as "أشكال الموجات الصوتية الخام" to emphasize working directly with audio samples
  - "autoregressive" translated as "انحداري ذاتي" following glossary
  - "conditioning" translated as "تكييف" in the context of conditional generation
  - "TTS" kept as acronym with Arabic expansion "تحويل النص إلى كلام"
  - "parametric and concatenative systems" translated as "الأنظمة البارامترية والتسلسلية" referring to traditional speech synthesis approaches

### Quality Metrics

- Semantic equivalence: 0.93
- Technical accuracy: 0.95
- Readability: 0.90
- Glossary consistency: 0.90
- **Overall section score:** 0.92
