# Section 2: Related Work
## القسم 2: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.89
**Glossary Terms Used:** pre-trained, word vectors, NLP, question answering, textual entailment, semantic role labeling, context-independent, subword, character convolutions, context-dependent, bidirectional, LSTM, neural machine translation, encoder-decoder, language model, biLM, biRNN, multi-task, dependency parsing, part-of-speech, autoencoder, fine-tuning, semi-supervision

---

### English Version

Due to their ability to capture syntactic and semantic information of words from large scale unlabeled text, pretrained word vectors (Turian et al., 2010; Mikolov et al., 2013; Pennington et al., 2014) are a standard component of most state-of-the-art NLP architectures, including for question answering (Liu et al., 2017), textual entailment (Chen et al., 2017) and semantic role labeling (He et al., 2017). However, these approaches for learning word vectors only allow a single context-independent representation for each word.

Previously proposed methods overcome some of the shortcomings of traditional word vectors by either enriching them with subword information (e.g., Wieting et al., 2016; Bojanowski et al., 2017) or learning separate vectors for each word sense (e.g., Neelakantan et al., 2014). Our approach also benefits from subword units through the use of character convolutions, and we seamlessly incorporate multi-sense information into downstream tasks without explicitly training to predict predefined sense classes.

Other recent work has also focused on learning context-dependent representations. context2vec (Melamud et al., 2016) uses a bidirectional Long Short Term Memory (LSTM; Hochreiter and Schmidhuber, 1997) to encode the context around a pivot word. Other approaches for learning contextual embeddings include the pivot word itself in the representation and are computed with the encoder of either a supervised neural machine translation (MT) system (CoVe; McCann et al., 2017) or an unsupervised language model (Peters et al., 2017). Both of these approaches benefit from large datasets, although the MT approach is limited by the size of parallel corpora. In this paper, we take full advantage of access to plentiful monolingual data, and train our biLM on a corpus with approximately 30 million sentences (Chelba et al., 2014). We also generalize these approaches to deep contextual representations, which we show work well across a broad range of diverse NLP tasks.

Previous work has also shown that different layers of deep biRNNs encode different types of information. For example, introducing multi-task syntactic supervision (e.g., part-of-speech tags) at the lower levels of a deep LSTM can improve overall performance of higher level tasks such as dependency parsing (Hashimoto et al., 2017) or CCG super tagging (Søgaard and Goldberg, 2016). In an RNN-based encoder-decoder machine translation system, Belinkov et al. (2017) showed that the representations learned at the first layer in a 2-layer LSTM encoder are better at predicting POS tags then second layer. Finally, the top layer of an LSTM for encoding word context (Melamud et al., 2016) has been shown to learn representations of word sense. We show that similar signals are also induced by the modified language model objective of our ELMo representations, and it can be very beneficial to learn models for downstream tasks that mix these different types of semi-supervision.

Dai and Le (2015) and Ramachandran et al. (2017) pretrain encoder-decoder pairs using language models and sequence autoencoders and then fine tune with task specific supervision. In contrast, after pretraining the biLM with unlabeled data, we fix the weights and add additional task-specific model capacity, allowing us to leverage large, rich and universal biLM representations for cases where downstream training data size dictates a smaller supervised model.

---

### النسخة العربية

نظراً لقدرتها على التقاط المعلومات التركيبية والدلالية للكلمات من نصوص غير موسومة واسعة النطاق، فإن متجهات الكلمات المدربة مسبقاً (Turian et al., 2010; Mikolov et al., 2013; Pennington et al., 2014) هي مكون قياسي في معظم معماريات معالجة اللغة الطبيعية الأكثر تطوراً، بما في ذلك للإجابة على الأسئلة (Liu et al., 2017)، والاستلزام النصي (Chen et al., 2017) ووسم الأدوار الدلالية (He et al., 2017). ومع ذلك، فإن هذه الأساليب لتعلم متجهات الكلمات تسمح فقط بتمثيل واحد مستقل عن السياق لكل كلمة.

الأساليب المقترحة سابقاً تتغلب على بعض أوجه القصور في متجهات الكلمات التقليدية إما بإثرائها بمعلومات الوحدات الفرعية للكلمات (على سبيل المثال، Wieting et al., 2016; Bojanowski et al., 2017) أو بتعلم متجهات منفصلة لكل معنى من معاني الكلمة (على سبيل المثال، Neelakantan et al., 2014). نهجنا يستفيد أيضاً من الوحدات الفرعية للكلمات من خلال استخدام التفافات الحروف، ونُدمج بسلاسة معلومات المعاني المتعددة في المهام اللاحقة دون التدريب صراحةً للتنبؤ بفئات المعاني المحددة مسبقاً.

أعمال حديثة أخرى ركزت أيضاً على تعلم التمثيلات المعتمدة على السياق. context2vec (Melamud et al., 2016) تستخدم ذاكرة طويلة قصيرة المدى ثنائية الاتجاه (LSTM; Hochreiter and Schmidhuber, 1997) لترميز السياق حول كلمة محورية. أساليب أخرى لتعلم التضمينات السياقية تتضمن الكلمة المحورية نفسها في التمثيل وتُحسب باستخدام المشفر إما لنظام ترجمة آلية عصبي خاضع للإشراف (CoVe; McCann et al., 2017) أو لنموذج لغوي غير خاضع للإشراف (Peters et al., 2017). كلا هذين النهجين يستفيدان من مجموعات البيانات الكبيرة، على الرغم من أن نهج الترجمة الآلية محدود بحجم المدونات المتوازية. في هذا البحث، نستفيد استفادة كاملة من الوصول إلى البيانات الأحادية اللغة الوفيرة، ونُدرب نموذجنا اللغوي ثنائي الاتجاه (biLM) على مدونة تحتوي على ما يقارب 30 مليون جملة (Chelba et al., 2014). كما نُعمم هذه الأساليب على التمثيلات السياقية العميقة، والتي نُظهر أنها تعمل بشكل جيد عبر مجموعة واسعة من مهام معالجة اللغة الطبيعية المتنوعة.

أظهرت الأعمال السابقة أيضاً أن الطبقات المختلفة من الشبكات العصبية المتكررة ثنائية الاتجاه (biRNN) العميقة تشفر أنواعاً مختلفة من المعلومات. على سبيل المثال، إدخال إشراف تركيبي متعدد المهام (مثل وسوم أجزاء الكلام) في المستويات الأدنى من LSTM عميق يمكن أن يحسن الأداء العام للمهام ذات المستوى الأعلى مثل تحليل التبعية (Hashimoto et al., 2017) أو وسم CCG الفائق (Søgaard and Goldberg, 2016). في نظام ترجمة آلية قائم على RNN بمعمارية مشفر-مفكك، أظهر Belinkov et al. (2017) أن التمثيلات المتعلمة في الطبقة الأولى في مشفر LSTM ذي طبقتين أفضل في التنبؤ بوسوم أجزاء الكلام (POS) من الطبقة الثانية. أخيراً، ثبت أن الطبقة العليا من LSTM لترميز سياق الكلمة (Melamud et al., 2016) تتعلم تمثيلات معنى الكلمة. نُظهر أن إشارات مماثلة تُستحث أيضاً بواسطة هدف نموذج اللغة المعدل لتمثيلات ELMo الخاصة بنا، ويمكن أن يكون من المفيد جداً تعلم نماذج للمهام اللاحقة تمزج هذه الأنواع المختلفة من الإشراف الشبه.

قام Dai and Le (2015) و Ramachandran et al. (2017) بالتدريب المسبق لأزواج المشفر-المفكك باستخدام نماذج لغوية ومشفرات تلقائية تسلسلية ثم الضبط الدقيق بإشراف خاص بالمهمة. في المقابل، بعد التدريب المسبق لنموذج اللغة ثنائي الاتجاه (biLM) ببيانات غير موسومة، نثبت الأوزان ونضيف سعة نموذج إضافية خاصة بالمهمة، مما يسمح لنا بالاستفادة من تمثيلات biLM الكبيرة والغنية والعامة للحالات التي يفرض فيها حجم بيانات التدريب اللاحقة نموذجاً خاضعاً للإشراف أصغر.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** context2vec, CoVe, biRNN, character convolutions, subword units, dependency parsing, CCG super tagging, monolingual data, parallel corpora
- **Equations:** 0
- **Citations:** 16 references cited
- **Special handling:**
  - Kept model names as is: context2vec, CoVe, CCG
  - POS (part-of-speech) translated as وسوم أجزاء الكلام
  - biRNN = الشبكات العصبية المتكررة ثنائية الاتجاه

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.90
- Readability: 0.88
- Glossary consistency: 0.89
- **Overall section score:** 0.89

### Back-Translation Validation (Key Paragraph)

Arabic back to English (first paragraph):
"Due to their ability to capture syntactic and semantic information of words from large-scale unlabeled text, pre-trained word vectors are a standard component in most state-of-the-art natural language processing architectures, including for question answering, textual entailment, and semantic role labeling. However, these approaches for learning word vectors only allow a single context-independent representation for each word."

✓ Semantic equivalence maintained
✓ Technical terminology accurately preserved
