# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.89
**Glossary Terms Used:** word representation, pre-training, language model, contextualized, deep learning, LSTM, bidirectional, embedding, polysemy, syntax, semantics, neural network, word sense disambiguation, part-of-speech tagging, semi-supervision, question answering, textual entailment, sentiment analysis, NLP

---

### English Version

Pre-trained word representations (Mikolov et al., 2013; Pennington et al., 2014) are a key component in many neural language understanding models. However, learning high quality representations can be challenging. They should ideally model both (1) complex characteristics of word use (e.g., syntax and semantics), and (2) how these uses vary across linguistic contexts (i.e., to model polysemy). In this paper, we introduce a new type of deep contextualized word representation that directly addresses both challenges, can be easily integrated into existing models, and significantly improves the state of the art in every considered case across a range of challenging language understanding problems.

Our representations differ from traditional word type embeddings in that each token is assigned a representation that is a function of the entire input sentence. We use vectors derived from a bidirectional LSTM that is trained with a coupled language model (LM) objective on a large text corpus. For this reason, we call them ELMo (Embeddings from Language Models) representations. Unlike previous approaches for learning contextualized word vectors (Peters et al., 2017; McCann et al., 2017), ELMo representations are deep, in the sense that they are a function of all of the internal layers of the biLM. More specifically, we learn a linear combination of the vectors stacked above each input word for each end task, which markedly improves performance over just using the top LSTM layer.

Combining the internal states in this manner allows for very rich word representations. Using intrinsic evaluations, we show that the higher-level LSTM states capture context-dependent aspects of word meaning (e.g., they can be used without modification to perform well on supervised word sense disambiguation tasks) while lower-level states model aspects of syntax (e.g., they can be used to do part-of-speech tagging). Simultaneously exposing all of these signals is highly beneficial, allowing the learned models select the types of semi-supervision that are most useful for each end task.

Extensive experiments demonstrate that ELMo representations work extremely well in practice. We first show that they can be easily added to existing models for six diverse and challenging language understanding problems, including textual entailment, question answering and sentiment analysis. The addition of ELMo representations alone significantly improves the state of the art in every case, including up to 20% relative error reductions. For tasks where direct comparisons are possible, ELMo outperforms CoVe (McCann et al., 2017), which computes contextualized representations using a neural machine translation encoder. Finally, an analysis of both ELMo and CoVe reveals that deep representations outperform those derived from just the top layer of an LSTM. Our trained models and code are publicly available, and we expect that ELMo will provide similar gains for many other NLP problems.

---

### النسخة العربية

تمثيلات الكلمات المدربة مسبقاً (Mikolov et al., 2013; Pennington et al., 2014) هي مكون أساسي في العديد من نماذج فهم اللغة العصبية. ومع ذلك، يمكن أن يكون تعلم تمثيلات عالية الجودة أمراً صعباً. يجب أن تنمذج هذه التمثيلات في الحالة المثالية كلاً من (1) الخصائص المعقدة لاستخدام الكلمات (مثل البنية التركيبية والدلالات)، و(2) كيف تختلف هذه الاستخدامات عبر السياقات اللغوية (أي لنمذجة تعدد المعاني). في هذا البحث، نقدم نوعاً جديداً من تمثيلات الكلمات السياقية العميقة التي تعالج كلا التحديين بشكل مباشر، ويمكن دمجها بسهولة في النماذج الموجودة، وتحسن بشكل كبير أحدث ما توصل إليه العلم في كل حالة معتبرة عبر مجموعة من مسائل فهم اللغة الصعبة.

تختلف تمثيلاتنا عن التضمينات التقليدية لأنواع الكلمات في أن كل رمز يُعطى تمثيلاً هو دالة للجملة الكاملة المُدخلة. نستخدم متجهات مستمدة من LSTM ثنائي الاتجاه يتم تدريبه بهدف نموذج لغوي مزدوج (LM) على مدونة نصية كبيرة. لهذا السبب، نسميها تمثيلات ELMo (التضمينات من النماذج اللغوية). على عكس الطرق السابقة لتعلم متجهات الكلمات السياقية (Peters et al., 2017; McCann et al., 2017)، تمثيلات ELMo عميقة، بمعنى أنها دالة لجميع الطبقات الداخلية لنموذج اللغة ثنائي الاتجاه (biLM). بشكل أكثر تحديداً، نتعلم مزيجاً خطياً من المتجهات المكدسة فوق كل كلمة مُدخلة لكل مهمة نهائية، مما يحسن الأداء بشكل ملحوظ مقارنة باستخدام الطبقة العليا من LSTM فقط.

الجمع بين الحالات الداخلية بهذه الطريقة يسمح بتمثيلات كلمات غنية جداً. باستخدام التقييمات الجوهرية، نُظهر أن حالات LSTM ذات المستوى الأعلى تلتقط الجوانب المعتمدة على السياق لمعنى الكلمة (على سبيل المثال، يمكن استخدامها دون تعديل للأداء الجيد في مهام توضيح معنى الكلمة المشرفة) بينما تنمذج الحالات ذات المستوى الأدنى جوانب البنية التركيبية (على سبيل المثال، يمكن استخدامها لأداء وسم أجزاء الكلام). الكشف المتزامن عن جميع هذه الإشارات مفيد للغاية، مما يسمح للنماذج المتعلمة باختيار أنواع الإشراف الشبه الأكثر فائدة لكل مهمة نهائية.

تُظهر التجارب الواسعة أن تمثيلات ELMo تعمل بشكل جيد للغاية في الممارسة العملية. نُظهر أولاً أنه يمكن إضافتها بسهولة إلى النماذج الموجودة لست مسائل متنوعة وصعبة في فهم اللغة، بما في ذلك الاستلزام النصي والإجابة على الأسئلة وتحليل المشاعر. إضافة تمثيلات ELMo وحدها تحسن بشكل كبير أحدث ما توصل إليه العلم في كل حالة، بما في ذلك تخفيضات في الخطأ النسبي تصل إلى 20%. بالنسبة للمهام التي تكون فيها المقارنات المباشرة ممكنة، يتفوق ELMo على CoVe (McCann et al., 2017)، الذي يحسب التمثيلات السياقية باستخدام مشفر الترجمة الآلية العصبية. أخيراً، يكشف تحليل كل من ELMo وCoVe أن التمثيلات العميقة تتفوق على تلك المستمدة من الطبقة العليا لـ LSTM فقط. نماذجنا المدربة والشفرة متاحة للجمهور، ونتوقع أن يوفر ELMo مكاسب مماثلة للعديد من مسائل معالجة اللغة الطبيعية الأخرى.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** ELMo (Embeddings from Language Models), biLM (bidirectional language model), CoVe, intrinsic evaluations
- **Equations:** None
- **Citations:** Mikolov et al. 2013, Pennington et al. 2014, Peters et al. 2017, McCann et al. 2017
- **Special handling:**
  - Maintained "ELMo" as-is (technical name)
  - Kept "biLM" with Arabic explanation in parentheses
  - Preserved citation format
  - Used established glossary terms consistently

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.90
- Readability: 0.88
- Glossary consistency: 0.88
- **Overall section score:** 0.89

### Back-Translation Validation (First Paragraph)

Pre-trained word representations are a fundamental component in many neural language understanding models. However, learning high-quality representations can be challenging. These representations should ideally model both (1) complex characteristics of word use (such as syntax and semantics), and (2) how these uses vary across linguistic contexts (i.e., to model polysemy). In this research, we introduce a new type of deep contextualized word representations that directly address both challenges, can be easily integrated into existing models, and significantly improve the state of the art in every considered case across a range of challenging language understanding problems.

**Validation:** ✓ Excellent semantic match with original
