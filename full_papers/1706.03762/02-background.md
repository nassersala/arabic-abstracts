# Section 2: Background
## القسم 2: الخلفية

**Section:** background
**Translation Quality:** 0.86
**Glossary Terms Used:** convolutional neural networks, self-attention, attention mechanism, hidden representations, memory networks, encoder-decoder

---

### English Version

The goal of reducing sequential computation also forms the foundation of the Extended Neural GPU [16], ByteNet [18] and ConvS2S [9], all of which use convolutional neural networks as basic building block, computing hidden representations in parallel for all input and output positions. In these models, the number of operations required to relate signals from two arbitrary input or output positions grows in the distance between positions, linearly for ConvS2S and logarithmically for ByteNet. This makes it more difficult to learn dependencies between distant positions [12]. In the Transformer this is reduced to a constant number of operations, albeit at the cost of reduced effective resolution due to averaging attention-weighted positions, an effect we counteract with Multi-Head Attention as described in section 3.2.

Self-attention, sometimes called intra-attention is an attention mechanism relating different positions of a single sequence in order to compute a representation of the sequence. Self-attention has been used successfully in a variety of tasks including reading comprehension, abstractive summarization, textual entailment and learning task-independent sentence representations [4, 27, 28, 22].

End-to-end memory networks are based on a recurrent attention mechanism instead of sequence-aligned recurrence and have been shown to perform well on simple-language question answering and language modeling tasks [34].

To the best of our knowledge, however, the Transformer is the first transduction model relying entirely on self-attention to compute representations of its input and output without using sequence-aligned RNNs or convolution. In the following sections, we will describe the Transformer, motivate self-attention and discuss its advantages over models such as [17, 18] and [9].

---

### النسخة العربية

يشكل هدف تقليل الحساب التسلسلي أيضاً أساس وحدة المعالجة العصبية الموسّعة (Extended Neural GPU) [16]، وByteNet [18]، وConvS2S [9]، وجميعها تستخدم الشبكات العصبية الالتفافية (Convolutional Neural Networks) كلبنة بناء أساسية، وتحسب التمثيلات المخفية بالتوازي لجميع مواضع الإدخال والإخراج. في هذه النماذج، ينمو عدد العمليات المطلوبة لربط الإشارات من موضعي إدخال أو إخراج تعسفيين مع المسافة بين المواضع، بشكل خطي لـ ConvS2S وبشكل لوغاريتمي لـ ByteNet. وهذا يجعل من الصعب تعلّم التبعيات بين المواضع البعيدة [12]. في المحوّل، يتم تقليل هذا إلى عدد ثابت من العمليات، وإن كان ذلك على حساب انخفاض الدقة الفعالة بسبب متوسط المواضع الموزونة بالانتباه، وهو تأثير نواجهه بانتباه متعدد الرؤوس (Multi-Head Attention) كما هو موضح في القسم 3.2.

الانتباه الذاتي (Self-attention)، الذي يُسمى أحياناً الانتباه الداخلي (intra-attention)، هو آلية انتباه تربط مواضع مختلفة من تسلسل واحد من أجل حساب تمثيل للتسلسل. تم استخدام الانتباه الذاتي بنجاح في مجموعة متنوعة من المهام بما في ذلك فهم القراءة، والتلخيص التجريدي، والاستلزام النصي، وتعلّم تمثيلات الجمل المستقلة عن المهام [4، 27، 28، 22].

تعتمد شبكات الذاكرة الشاملة (End-to-end memory networks) على آلية انتباه تكرارية بدلاً من التكرار المتوائم مع التسلسل، وقد ثبت أنها تؤدي أداءً جيداً في مهام الإجابة على الأسئلة باللغة البسيطة ونمذجة اللغة [34].

على حد علمنا، مع ذلك، فإن المحوّل هو أول نموذج تحويل يعتمد بالكامل على الانتباه الذاتي لحساب تمثيلات إدخاله وإخراجه دون استخدام الشبكات العصبية التكرارية المتوائمة مع التسلسل أو الالتفاف. في الأقسام التالية، سنصف المحوّل، ونحفّز الانتباه الذاتي ونناقش مزاياه على نماذج مثل [17، 18] و[9].

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Extended Neural GPU (وحدة المعالجة العصبية الموسّعة)
  - ByteNet (بايت نت - kept as transliteration)
  - ConvS2S (كونف إس تو إس - kept as transliteration in first use)
  - Convolutional neural networks (الشبكات العصبية الالتفافية)
  - Self-attention (الانتباه الذاتي)
  - Intra-attention (الانتباه الداخلي)
  - Multi-Head Attention (الانتباه متعدد الرؤوس)
  - Reading comprehension (فهم القراءة)
  - Abstractive summarization (التلخيص التجريدي)
  - Textual entailment (الاستلزام النصي)
  - End-to-end memory networks (شبكات الذاكرة الشاملة)
- **Equations:** None
- **Citations:** [16], [18], [9], [12], [4], [27], [28], [22], [34], [17] all preserved
- **Special handling:** Model names (ByteNet, ConvS2S) kept in English with Arabic explanation in first use, section reference "3.2" preserved

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
