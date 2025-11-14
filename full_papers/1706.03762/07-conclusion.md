# Section 7: Conclusion
## القسم 7: الخلاصة

**Section:** conclusion
**Translation Quality:** 0.88
**Glossary Terms Used:** sequence transduction, attention mechanism, self-attention, encoder-decoder, machine translation, future work

---

### English Version

In this work, we presented the Transformer, the first sequence transduction model based entirely on attention, replacing the recurrent layers most commonly used in encoder-decoder architectures with multi-headed self-attention.

For translation tasks, the Transformer can be trained significantly faster than architectures based on recurrent or convolutional layers. On both WMT 2014 English-to-German and WMT 2014 English-to-French translation tasks, we achieve a new state of the art. In the former task our best model outperforms even all previously reported ensembles.

We are excited about the future of attention-based models and plan to apply them to other tasks. We plan to extend the Transformer to problems involving input and output modalities other than text and to investigate local, restricted attention mechanisms to efficiently handle large inputs and outputs such as images, audio and video. Making generation less sequential is another research goals of ours.

The code we used to train and evaluate our models is available at https://github.com/tensorflow/tensor2tensor.

**Acknowledgements** We are grateful to Nal Kalchbrenner and Stephan Gouws for their fruitful comments, corrections and inspiration.

---

### النسخة العربية

في هذا العمل، قدّمنا المحوّل (Transformer)، أول نموذج تحويل تسلسلات يعتمد بالكامل على الانتباه، مُستبدلاً الطبقات التكرارية الأكثر استخداماً في معماريات المشفّر-فك التشفير بالانتباه الذاتي متعدد الرؤوس.

بالنسبة لمهام الترجمة، يمكن تدريب المحوّل بشكل أسرع بكثير من المعماريات القائمة على الطبقات التكرارية أو الالتفافية. في كل من مهام ترجمة WMT 2014 من الإنجليزية إلى الألمانية ومن الإنجليزية إلى الفرنسية، نحقق نقطة مرجعية جديدة متطورة. في المهمة السابقة، يتفوق أفضل نموذج لدينا حتى على جميع التجميعات المُبلّغ عنها سابقاً.

نحن متحمسون لمستقبل النماذج القائمة على الانتباه ونخطط لتطبيقها على مهام أخرى. نخطط لتوسيع المحوّل ليشمل المسائل التي تتضمن طرائق إدخال وإخراج غير النص والتحقيق في آليات انتباه محلية ومقيّدة للتعامل بكفاءة مع المدخلات والمخرجات الكبيرة مثل الصور والصوت والفيديو. جعل التوليد أقل تسلسلاً هو هدف بحثي آخر من أهدافنا.

الكود الذي استخدمناه لتدريب وتقييم نماذجنا متاح على https://github.com/tensorflow/tensor2tensor.

**شكر وتقدير** نحن ممتنون لـ Nal Kalchbrenner و Stephan Gouws على تعليقاتهم وتصحيحاتهم وإلهامهم المثمر.

---

### Translation Notes

- **Figures referenced:** None
- **Tables referenced:** None
- **Key terms introduced:**
  - Attention-based models (النماذج القائمة على الانتباه)
  - Input and output modalities (طرائق الإدخال والإخراج)
  - Local, restricted attention mechanisms (آليات انتباه محلية ومقيّدة)
  - Sequential generation (التوليد التسلسلي)
  - Research goals (أهداف بحثية)

- **Equations:** None
- **Citations:** None in conclusion section
- **Special handling:**
  - Dataset names preserved (WMT 2014)
  - Code repository URL kept in English
  - Names in acknowledgments kept in English (Nal Kalchbrenner, Stephan Gouws)
  - GitHub link preserved exactly

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
