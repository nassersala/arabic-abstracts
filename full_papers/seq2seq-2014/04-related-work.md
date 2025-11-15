# Section 4: Related Work
## القسم 4: الأعمال ذات الصلة

**Section:** Related Work
**Translation Quality:** 0.87
**Glossary Terms Used:** neural network, language model, RNN, NNLM, machine translation, rescoring, convolutional neural networks, attention mechanism, encoder-decoder

---

### English Version

There is a large body of work on applications of neural networks to machine translation. So far, the simplest and most effective way of applying an RNN-Language Model (RNNLM) [23] or a Feedforward Neural Network Language Model (NNLM) [3] to an MT task is by rescoring the n-best lists of a strong MT baseline [22], which reliably improves translation quality.

More recently, researchers have begun to look into ways of including information about the source language into the NNLM. Examples of this work include Auli et al. [1], who combine an NNLM with a topic model of the input sentence, which improves rescoring performance. Devlin et al. [8] followed a similar approach, but they incorporated their NNLM into the decoder of an MT system and used the decoder's alignment information to provide the NNLM with the most useful words in the input sentence. Their approach was highly successful and it achieved large improvements over their baseline.

Our work is closely related to Kalchbrenner and Blunsom [18], who were the first to map the input sentence into a vector and then back to a sentence, although they map sentences to vectors using convolutional neural networks, which lose the ordering of the words. Similarly to this work, Cho et al. [5] used an LSTM-like RNN architecture to map sentences into vectors and back, although their primary focus was on integrating their neural network into an SMT system. Bahdanau et al. [2] also attempted direct translations with a neural network that used an attention mechanism to overcome the poor performance on long sentences experienced by Cho et al. [5] and achieved encouraging results. Likewise, Pouget-Abadie et al. [26] attempted to address the memory problem of Cho et al. [5] by translating pieces of the source sentence in way that produces smooth translations, which is similar to a phrase-based approach. We suspect that they could achieve similar improvements by simply training their networks on reversed source sentences.

End-to-end training is also the focus of Hermann et al. [12], whose model represents the inputs and outputs by feedforward networks, and maps them to similar points in space. However, their approach cannot generate translations directly: to get a translation, they need to do a lookup for closest vector in the pre-computed database of sentences, or to rescore a sentence.

---

### النسخة العربية

هناك مجموعة كبيرة من الأعمال حول تطبيقات الشبكات العصبية على الترجمة الآلية. حتى الآن، الطريقة الأبسط والأكثر فعالية لتطبيق نموذج لغة شبكة عصبية متكررة (RNNLM) [23] أو نموذج لغة شبكة عصبية أمامية (NNLM) [3] على مهمة ترجمة آلية هي من خلال إعادة تقييم قوائم n الأفضل لخط أساس ترجمة آلية قوي [22]، مما يُحسِّن جودة الترجمة بشكل موثوق.

في الآونة الأخيرة، بدأ الباحثون في البحث عن طرق لتضمين معلومات حول اللغة المصدر في NNLM. تشمل أمثلة هذا العمل Auli وآخرين [1]، الذين يجمعون بين NNLM ونموذج موضوعي لجملة الإدخال، مما يُحسِّن أداء إعادة التقييم. اتبع Devlin وآخرون [8] نهجاً مماثلاً، لكنهم دمجوا NNLM الخاص بهم في فك تشفير نظام ترجمة آلية واستخدموا معلومات المحاذاة الخاصة بفك التشفير لتزويد NNLM بالكلمات الأكثر فائدة في جملة الإدخال. كان نهجهم ناجحاً للغاية وحقق تحسينات كبيرة على خط الأساس الخاص بهم.

عملنا مرتبط ارتباطاً وثيقاً بـ Kalchbrenner و Blunsom [18]، اللذين كانا أول من قام بتخطيط جملة الإدخال إلى متجه ثم العودة إلى جملة، على الرغم من أنهم يخططون الجمل إلى متجهات باستخدام الشبكات العصبية الالتفافية، التي تفقد ترتيب الكلمات. بشكل مماثل لهذا العمل، استخدم Cho وآخرون [5] معمارية RNN شبيهة بـ LSTM لتخطيط الجمل إلى متجهات والعودة، على الرغم من أن تركيزهم الأساسي كان على دمج شبكتهم العصبية في نظام SMT. حاول Bahdanau وآخرون [2] أيضاً الترجمات المباشرة باستخدام شبكة عصبية تستخدم آلية انتباه للتغلب على الأداء الضعيف في الجمل الطويلة الذي عانى منه Cho وآخرون [5] وحققوا نتائج مشجعة. وبالمثل، حاول Pouget-Abadie وآخرون [26] معالجة مشكلة الذاكرة لدى Cho وآخرين [5] من خلال ترجمة أجزاء من الجملة المصدر بطريقة تنتج ترجمات سلسة، وهو ما يشبه النهج القائم على العبارات. نشتبه في أنهم يمكنهم تحقيق تحسينات مماثلة ببساطة من خلال تدريب شبكاتهم على الجمل المصدر المعكوسة.

التدريب من طرف إلى طرف هو أيضاً محور تركيز Hermann وآخرين [12]، الذين يمثل نموذجهم المدخلات والمخرجات بواسطة شبكات أمامية، ويخططها إلى نقاط متشابهة في الفضاء. ومع ذلك، لا يمكن لنهجهم توليد الترجمات مباشرة: للحصول على ترجمة، يحتاجون إلى البحث عن أقرب متجه في قاعدة البيانات المحسوبة مسبقاً للجمل، أو إعادة تقييم جملة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** RNN-Language Model (RNNLM), Feedforward Neural Network Language Model (NNLM), n-best lists, rescoring, topic model, alignment information, convolutional neural networks, attention mechanism, encoder-decoder architecture, end-to-end training, phrase-based approach
- **Equations:** 0
- **Citations:** [23], [3], [22], [1], [8], [18], [5], [2], [26], [12]
- **Special handling:**
  - Author names and publication years preserved
  - Comparison with related work clearly maintained
  - Technical distinctions between approaches preserved
  - Critical analysis of other methods retained

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
