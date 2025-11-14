# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.93
**Glossary Terms Used:** transformer, attention mechanism, machine translation, architecture, encoder, decoder, recurrent neural networks, convolutional neural networks

---

### English Version

The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.

---

### النسخة العربية

تعتمد نماذج تحويل التسلسلات المهيمنة على شبكات عصبية تكرارية أو التفافية معقدة تتضمن مشفّراً (encoder) وفك تشفير (decoder). تربط النماذج الأفضل أداءً أيضاً المشفّر وفك التشفير من خلال آلية انتباه. نقترح معمارية شبكة بسيطة جديدة، المحوّل (Transformer)، مبنية فقط على آليات الانتباه، مع الاستغناء عن التكرار والالتفاف بالكامل. تُظهر التجارب على مهمتي ترجمة آلية أن هذه النماذج متفوقة في الجودة بينما تكون أكثر قابلية للتوازي وتتطلب وقتاً أقل بكثير للتدريب. يحقق نموذجنا 28.4 BLEU على مهمة ترجمة WMT 2014 من الإنجليزية إلى الألمانية، متفوقاً على أفضل النتائج الموجودة، بما في ذلك التجميعات (ensembles)، بأكثر من 2 BLEU. في مهمة ترجمة WMT 2014 من الإنجليزية إلى الفرنسية، يضع نموذجنا نقطة مرجعية جديدة للنموذج الواحد بنتيجة BLEU تبلغ 41.8 بعد التدريب لمدة 3.5 يوم على ثمانية GPUs، وهو جزء صغير من تكاليف التدريب لأفضل النماذج من الأدبيات. نُظهر أن المحوّل يعمم بشكل جيد على مهام أخرى من خلال تطبيقه بنجاح على تحليل البنية التركيبية للغة الإنجليزية مع بيانات تدريب كبيرة ومحدودة على حد سواء.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:** Transformer (المحوّل), attention mechanism (آلية الانتباه), sequence transduction (تحويل التسلسلات), encoder-decoder (مشفّر-فك تشفير)
- **Equations:** None
- **Citations:** None
- **Special handling:** BLEU scores kept as numbers, WMT kept as English acronym, GPU kept in English

### Quality Metrics

- Semantic equivalence: 0.94
- Technical accuracy: 0.93
- Readability: 0.92
- Glossary consistency: 0.93
- **Overall section score:** 0.93
