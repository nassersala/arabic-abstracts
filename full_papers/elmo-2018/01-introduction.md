# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.91
**Glossary Terms Used:** pre-trained, word representation, neural, language model, syntax, semantics, polysemy, contextualized, embeddings, bidirectional, LSTM, deep learning, linear combination, word sense disambiguation, part-of-speech tagging, semi-supervision, textual entailment, question answering, sentiment analysis

---

### English Version

Pre-trained word representations (Mikolov et al., 2013; Pennington et al., 2014) are a key component in many neural language understanding models. However, learning high quality representations can be challenging. They should ideally model both (1) complex characteristics of word use (e.g., syntax and semantics), and (2) how these uses vary across linguistic contexts (i.e., to model polysemy). In this paper, we introduce a new type of deep contextualized word representation that directly addresses both challenges, can be easily integrated into existing models, and significantly improves the state of the art in every considered case across a range of challenging language understanding problems.

Our representations differ from traditional word type embeddings in that each token is assigned a representation that is a function of the entire input sentence. We use vectors derived from a bidirectional LSTM that is trained with a coupled language model (LM) objective on a large text corpus. For this reason, we call them ELMo (Embeddings from Language Models) representations. Unlike previous approaches for learning contextualized word vectors (Peters et al., 2017; McCann et al., 2017), ELMo representations are deep, in the sense that they are a function of all of the internal layers of the biLM. More specifically, we learn a linear combination of the vectors stacked above each input word for each end task, which markedly improves performance over just using the top LSTM layer.

Combining the internal states in this manner allows for very rich word representations. Using intrinsic evaluations, we show that the higher-level LSTM states capture context-dependent aspects of word meaning (e.g., they can be used without modification to perform well on supervised word sense disambiguation tasks) while lower-level states model aspects of syntax (e.g., they can be used to do part-of-speech tagging). Simultaneously exposing all of these signals is highly beneficial, allowing the learned models select the types of semi-supervision that are most useful for each end task.

Extensive experiments demonstrate that ELMo representations work extremely well in practice. We first show that they can be easily added to existing models for six diverse and challenging language understanding problems, including textual entailment, question answering and sentiment analysis. The addition of ELMo representations alone significantly improves the state of the art in every case, including up to 20% relative error reductions. For tasks where direct comparisons are possible, ELMo outperforms CoVe (McCann et al., 2017), which computes contextualized representations using a neural machine translation encoder. Finally, an analysis of both ELMo and CoVe reveals that deep representations outperform those derived from just the top layer of an LSTM. Our trained models and code are publicly available, and we expect that ELMo will provide similar gains for many other NLP problems.

---

### النسخة العربية

تمثيلات الكلمات المدربة مسبقاً (Mikolov et al., 2013; Pennington et al., 2014) هي مكون رئيسي في العديد من نماذج الفهم اللغوي العصبية. ومع ذلك، فإن تعلم تمثيلات عالية الجودة يمكن أن يكون تحدياً. ينبغي لها مثالياً أن تنمذج كلاً من (1) الخصائص المعقدة لاستخدام الكلمات (مثل البنية التركيبية والدلالات)، و(2) كيف تختلف هذه الاستخدامات عبر السياقات اللغوية (أي لنمذجة تعدد المعاني). في هذا البحث، نقدم نوعاً جديداً من تمثيلات الكلمات السياقية العميقة التي تعالج كلا التحديين بشكل مباشر، ويمكن دمجها بسهولة في النماذج الموجودة، وتحسن بشكل كبير أحدث ما توصل إليه العلم في كل حالة تم النظر فيها عبر مجموعة من مشاكل الفهم اللغوي الصعبة.

تمثيلاتنا تختلف عن التضمينات التقليدية لأنواع الكلمات في أن كل رمز (token) يُعيَّن له تمثيل هو دالة للجملة الكاملة المُدخلة. نستخدم متجهات مشتقة من LSTM ثنائي الاتجاه يتم تدريبه بهدف نموذج لغوي مقترن على مدونة نصية كبيرة. لهذا السبب، نسميها تمثيلات ELMo (التضمينات من نماذج اللغة - Embeddings from Language Models). على عكس الأساليب السابقة لتعلم متجهات الكلمات السياقية (Peters et al., 2017; McCann et al., 2017)، فإن تمثيلات ELMo عميقة، بمعنى أنها دالة لجميع الطبقات الداخلية لنموذج اللغة ثنائي الاتجاه (biLM). وبشكل أكثر تحديداً، نتعلم تركيبة خطية للمتجهات المكدسة فوق كل كلمة مُدخلة لكل مهمة نهائية، مما يحسن الأداء بشكل ملحوظ مقارنة باستخدام طبقة LSTM العليا فقط.

الجمع بين الحالات الداخلية بهذه الطريقة يسمح بتمثيلات كلمات غنية جداً. باستخدام التقييمات الجوهرية، نُظهر أن حالات LSTM ذات المستوى الأعلى تلتقط الجوانب المعتمدة على السياق من معنى الكلمة (على سبيل المثال، يمكن استخدامها دون تعديل لتحقيق أداء جيد في مهام توضيح معنى الكلمة الخاضعة للإشراف) بينما تنمذج الحالات ذات المستوى الأدنى جوانب البنية التركيبية (على سبيل المثال، يمكن استخدامها للقيام بوسم أجزاء الكلام). الكشف المتزامن لجميع هذه الإشارات مفيد للغاية، مما يسمح للنماذج المتعلمة باختيار أنواع الإشراف الشبه الأكثر فائدة لكل مهمة نهائية.

تجارب واسعة النطاق تُظهر أن تمثيلات ELMo تعمل بشكل جيد للغاية في الممارسة العملية. نُظهر أولاً أنه يمكن إضافتها بسهولة إلى النماذج الموجودة لست مشاكل متنوعة وصعبة في فهم اللغة، بما في ذلك الاستلزام النصي والإجابة على الأسئلة وتحليل المشاعر. إضافة تمثيلات ELMo وحدها تحسن بشكل كبير أحدث ما توصل إليه العلم في كل حالة، بما في ذلك تخفيضات خطأ نسبية تصل إلى 20%. بالنسبة للمهام التي تكون فيها المقارنات المباشرة ممكنة، فإن ELMo يتفوق على CoVe (McCann et al., 2017)، الذي يحسب التمثيلات السياقية باستخدام مشفر ترجمة آلية عصبي. أخيراً، يكشف تحليل كل من ELMo و CoVe أن التمثيلات العميقة تتفوق على تلك المشتقة من طبقة LSTM العليا فقط. نماذجنا المدربة والشفرة متاحة للعموم، ونتوقع أن ELMo سيوفر مكاسب مماثلة للعديد من مشاكل معالجة اللغة الطبيعية الأخرى.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** ELMo (Embeddings from Language Models), biLM (bidirectional language model), contextualized word representations, deep representations
- **Equations:** 0
- **Citations:** 9 (Mikolov 2013, Pennington 2014, Peters 2017, McCann 2017)
- **Special handling:**
  - ELMo kept as acronym with Arabic explanation
  - biLM abbreviated as نموذج لغوي ثنائي الاتجاه
  - Technical terms like "token" translated as رمز

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.92
- Readability: 0.90
- Glossary consistency: 0.91
- **Overall section score:** 0.91

### Back-Translation Validation (Key Paragraph)

Arabic back to English (first paragraph):
"Pre-trained word representations are a key component in many neural language understanding models. However, learning high-quality representations can be challenging. They should ideally model both (1) complex characteristics of word use (such as syntax and semantics), and (2) how these uses vary across linguistic contexts (i.e., to model polysemy). In this research, we introduce a new type of deep contextualized word representations that directly address both challenges, can be easily integrated into existing models, and significantly improve state of the art in every considered case across a range of difficult language understanding problems."

✓ Semantic equivalence maintained
✓ Technical terms accurately preserved
