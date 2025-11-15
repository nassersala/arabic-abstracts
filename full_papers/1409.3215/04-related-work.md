# Section 4: Related Work
## القسم 4: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.86
**Glossary Terms Used:** recurrent neural network, language model, feedforward neural network, machine translation, attention mechanism, convolutional neural network, rescoring, phrase-based, end-to-end training

---

### English Version

There is a large body of work on applications of neural networks to machine translation. So far, the simplest and most effective way of applying an RNN-Language Model (RNNLM) [23] or a Feedforward Neural Network Language Model (NNLM) [3] to an MT task is by rescoring the n-best lists of a strong MT baseline [22], which reliably improves translation quality.

More recently, researchers have begun to look into ways of including information about the source language into the NNLM. Examples of this work include Auli et al. [1], who combine an NNLM with a topic model of the input sentence, which improves rescoring performance. Devlin et al. [8] followed a similar approach, but they incorporated their NNLM into the decoder of an MT system and used the decoder's alignment information to provide the NNLM with the most useful words in the input sentence. Their approach was highly successful and it achieved large improvements over their baseline.

Our work is closely related to Kalchbrenner and Blunsom [18], who were the first to map the input sentence into a vector and then back to a sentence, although they map sentences to vectors using convolutional neural networks, which lose the ordering of the words. Similarly to this work, Cho et al. [5] used an LSTM-like RNN architecture to map sentences into vectors and back, although their primary focus was on integrating their neural network into an SMT system. Bahdanau et al. [2] also attempted direct translations with a neural network that used an attention mechanism to overcome the poor performance on long sentences experienced by Cho et al. [5] and achieved encouraging results. Likewise, Pouget-Abadie et al. [26] attempted to address the memory problem of Cho et al. [5] by translating pieces of the source sentence in way that produces smooth translations, which is similar to a phrase-based approach. We suspect that they could achieve similar improvements by simply training their networks on reversed source sentences.

End-to-end training is also the focus of Hermann et al. [12], whose model represents the inputs and outputs by feedforward networks, and map them to similar points in space. However, their approach cannot generate translations directly: to get a translation, they need to do a look up for closest vector in the pre-computed database of sentences, or to rescore a sentence.

---

### النسخة العربية

هناك مجموعة كبيرة من الأعمال حول تطبيقات الشبكات العصبية على الترجمة الآلية. حتى الآن، فإن أبسط وأكثر الطرق فعالية لتطبيق نموذج لغوي للشبكة العصبية التكرارية (RNNLM) [23] أو نموذج لغوي للشبكة العصبية ذات التغذية الأمامية (NNLM) [3] على مهمة ترجمة آلية هي عن طريق إعادة تصنيف قوائم n-best من خط أساس ترجمة آلية قوي [22]، والذي يحسن جودة الترجمة بشكل موثوق.

في الآونة الأخيرة، بدأ الباحثون في البحث عن طرق لتضمين معلومات حول اللغة المصدر في NNLM. تتضمن أمثلة هذا العمل Auli وآخرين [1]، الذين يجمعون NNLM مع نموذج موضوع لجملة الإدخال، مما يحسن أداء إعادة التصنيف. اتبع Devlin وآخرون [8] نهجاً مشابهاً، لكنهم دمجوا NNLM الخاص بهم في مفكك نظام ترجمة آلية واستخدموا معلومات المحاذاة الخاصة بالمفكك لتزويد NNLM بأكثر الكلمات فائدة في جملة الإدخال. كان نهجهم ناجحاً للغاية وحقق تحسينات كبيرة على خط الأساس الخاص بهم.

عملنا مرتبط بشكل وثيق بـ Kalchbrenner وBlunsom [18]، اللذين كانا أول من خطط جملة الإدخال إلى متجه ثم عاد إلى جملة، على الرغم من أنهم يخططون الجمل إلى متجهات باستخدام الشبكات العصبية الالتفافية، والتي تفقد ترتيب الكلمات. بشكل مماثل لهذا العمل، استخدم Cho وآخرون [5] معمارية RNN شبيهة بـ LSTM لتخطيط الجمل إلى متجهات والعودة، على الرغم من أن تركيزهم الأساسي كان على دمج شبكتهم العصبية في نظام SMT. حاول Bahdanau وآخرون [2] أيضاً الترجمات المباشرة باستخدام شبكة عصبية استخدمت آلية انتباه للتغلب على الأداء الضعيف على الجمل الطويلة الذي واجهه Cho وآخرون [5] وحققوا نتائج مشجعة. وبالمثل، حاول Pouget-Abadie وآخرون [26] معالجة مشكلة الذاكرة لدى Cho وآخرين [5] عن طريق ترجمة أجزاء من الجملة المصدر بطريقة تنتج ترجمات سلسة، وهو ما يشبه النهج القائم على العبارات. نعتقد أنهم يمكنهم تحقيق تحسينات مماثلة ببساطة عن طريق تدريب شبكاتهم على جمل مصدر معكوسة.

التدريب الشامل من طرف إلى طرف هو أيضاً محور تركيز Hermann وآخرين [12]، الذين يمثل نموذجهم المدخلات والمخرجات بواسطة شبكات التغذية الأمامية، ويخططها إلى نقاط متشابهة في الفضاء. ومع ذلك، لا يمكن لنهجهم توليد ترجمات مباشرة: للحصول على ترجمة، يحتاجون إلى البحث عن أقرب متجه في قاعدة بيانات الجمل المحسوبة مسبقاً، أو لإعادة تصنيف جملة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** topic model, alignment information, encoder-decoder with attention, direct translation
- **Equations:** 0
- **Citations:** [23, 3, 22, 1, 8, 18, 5, 2, 26, 12]
- **Special handling:** Comparison with multiple related approaches in neural machine translation

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.86
