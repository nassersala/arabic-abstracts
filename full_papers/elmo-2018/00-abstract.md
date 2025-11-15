# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.94 (from translations/1802.05365.md)
**Glossary Terms Used:** word representation, contextualized, deep learning, syntax, semantics, polysemy, word vector, bidirectional, language model, pre-training, NLP, question answering, sentiment analysis, semi-supervision

---

### English Version

We introduce a new type of deep contextualized word representation that models both (1) complex characteristics of word use (e.g., syntax and semantics), and (2) how these uses vary across linguistic contexts (i.e., to model polysemy). Our word vectors are learned functions of the internal states of a deep bidirectional language model (biLM), which is pre-trained on a large text corpus. We show that these representations can be easily added to existing models and significantly improve the state of the art across six challenging NLP problems, including question answering, textual entailment and sentiment analysis. We also present an analysis showing that exposing the deep internals of the pre-trained network is crucial, allowing downstream models to mix different types of semi-supervision signals.

---

### النسخة العربية

نقدم نوعاً جديداً من تمثيلات الكلمات السياقية العميقة التي تنمذج كلاً من (1) الخصائص المعقدة لاستخدام الكلمات (مثل البنية التركيبية والدلالات)، و(2) كيف تختلف هذه الاستخدامات عبر السياقات اللغوية (أي لنمذجة تعدد المعاني). متجهات كلماتنا هي دوال متعلمة من الحالات الداخلية لنموذج لغوي ثنائي الاتجاه عميق (biLM)، يتم تدريبه مسبقاً على مدونة نصية كبيرة. نُظهر أن هذه التمثيلات يمكن إضافتها بسهولة إلى النماذج الموجودة وتحسن بشكل كبير أحدث ما توصل إليه العلم عبر ست مسائل صعبة في معالجة اللغة الطبيعية، بما في ذلك الإجابة على الأسئلة والاستلزام النصي وتحليل المشاعر. نقدم أيضاً تحليلاً يُظهر أن كشف الأجزاء الداخلية العميقة للشبكة المدربة مسبقاً أمر حاسم، مما يسمح للنماذج اللاحقة بمزج أنواع مختلفة من إشارات الإشراف الشبه.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** deep contextualized word representations, bidirectional language model (biLM), polysemy, semi-supervision
- **Equations:** 0
- **Citations:** 0 (abstract contains no explicit citations)
- **Special handling:** Technical NLP terminology preserved with Arabic equivalents

### Quality Metrics

- Semantic equivalence: 0.95
- Technical accuracy: 0.95
- Readability: 0.93
- Glossary consistency: 0.94
- **Overall section score:** 0.94
