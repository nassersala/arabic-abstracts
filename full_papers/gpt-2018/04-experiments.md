# Section 4: Experiments
## القسم 4: التجارب

**Section:** Experiments
**Translation Quality:** 0.86
**Glossary Terms Used:** dataset, benchmark, natural language inference, question answering, semantic similarity, classification, accuracy, transformer, decoder, attention, optimizer, dropout, learning rate, batch size

---

### English Version

### 4.1 Setup

**Unsupervised pre-training** We use the BooksCorpus dataset [71] for training the language model. It contains over 7,000 unique unpublished books from a variety of genres including Adventure, Fantasy, and Romance. Crucially, it contains long stretches of contiguous text, which allows the generative model to learn to condition on long-range information. An alternative dataset, the 1B Word Benchmark, which is used by a similar approach, ELMo [44], is approximately the same size but is shuffled at a sentence level - destroying long-range structure. Our language model achieves a very low token level perplexity of 18.4 on this corpus.

**Model specifications** Our model largely follows the original transformer work [62]. We trained a 12-layer decoder-only transformer with masked self-attention heads (768 dimensional states and 12 attention heads). For the position-wise feed-forward networks, we used 3072 dimensional inner states. We used the Adam optimization scheme [27] with a max learning rate of 2.5e-4. The learning rate was increased linearly from zero over the first 2000 updates and annealed to 0 using a cosine schedule. We train for 100 epochs on minibatches of 64 randomly sampled, contiguous sequences of 512 tokens. Since layernorm [2] is used extensively throughout the model, a simple weight initialization of $\mathcal{N}(0, 0.02)$ was sufficient. We used a bytepair encoding (BPE) vocabulary with 40,000 merges [53] and residual, embedding, and attention dropouts with a rate of 0.1 for regularization. We also employed a modified version of L2 regularization proposed in [37], with $w = 0.01$ on all non bias or gain weights. For the activation function, we used the Gaussian Error Linear Unit (GELU) [18]. We used learned position embeddings instead of the sinusoidal version proposed in the original work. We use the ftfy library² to clean the raw text in BooksCorpus, standardize some punctuation and whitespace, and use the spaCy tokenizer.³

**Fine-tuning details** Unless specified, we reuse the hyperparameter settings from unsupervised pre-training. We add dropout to the classifier with a rate of 0.1. For most tasks, we use a learning rate of 6.25e-5 and a batchsize of 32. Our model finetunes quickly and 3 epochs of training was sufficient for most cases. We use a linear learning rate decay schedule with warmup over 0.2% of training. $\lambda$ was set to 0.5.

### 4.2 Supervised fine-tuning

We perform experiments on a variety of supervised tasks including natural language inference, question answering, semantic similarity, and text classification. Some of these tasks are available as part of the recently released GLUE multi-task benchmark [64], which we make use of. Figure 1 provides an overview of all the tasks and datasets.

**Natural Language Inference** The task of natural language inference (NLI), also known as recognizing textual entailment, involves reading a pair of sentences and judging the relationship between them from one of entailment, contradiction or neutral. Although there has been a lot of recent interest [58,35,44], the task remains challenging due to the presence of a wide variety of phenomena like lexical entailment, coreference, and lexical and syntactic ambiguity. We evaluate on five datasets with diverse sources, including image captions (SNLI), transcribed speech, popular fiction, and government reports (MNLI), Wikipedia articles (QNLI), science exams (SciTail) or news articles (RTE).

Table 2 details various results on the different NLI tasks for our model and previous state-of-the-art approaches. Our method significantly outperforms the baselines on four of the five datasets, achieving absolute improvements of upto 1.5% on MNLI, 5% on SciTail, 5.8% on QNLI and 0.6% on SNLI over the previous best results. This demonstrates our model's ability to better reason over multiple sentences, and handle aspects of linguistic ambiguity. On RTE, one of the smaller datasets we evaluate on (2490 examples), we achieve an accuracy of 56%, which is below the 61.7% reported by a multi-task biLSTM model. Given the strong performance of our approach on larger NLI datasets, it is likely our model will benefit from multi-task training as well but we have not explored this currently.

**Question answering and commonsense reasoning** Another task that requires aspects of single and multi-sentence reasoning is question answering. We use the recently released RACE dataset [30], consisting of English passages with associated questions from middle and high school exams. This corpus has been shown to contain more reasoning type questions that other datasets like CNN [19] or SQuAD [47], providing the perfect evaluation for our model which is trained to handle long-range contexts. In addition, we evaluate on the Story Cloze Test [40], which involves selecting the correct ending to multi-sentence stories from two options. On these tasks, our model again outperforms the previous best results by significant margins - up to 8.9% on Story Cloze, and 5.7% overall on RACE. This demonstrates the ability of our model to handle long-range contexts effectively.

**Semantic Similarity** Semantic similarity (or paraphrase detection) tasks involve predicting whether two sentences are semantically equivalent or not. The challenges lie in recognizing rephrasing of concepts, understanding negation, and handling syntactic ambiguity. We use three datasets for this task – the Microsoft Paraphrase corpus (MRPC) [14] (collected from news sources), the Quora Question Pairs (QQP) dataset [9], and the Semantic Textual Similarity benchmark (STS-B) [6]. We obtain state-of-the-art results on two of the three semantic similarity tasks (Table 4) with a 1 point absolute gain on STS-B. The performance delta on QQP is significant, with a 4.2% absolute improvement over Single-task BiLSTM + ELMo + Attn.

**Classification** Finally, we also evaluate on two different text classification tasks. The Corpus of Linguistic Acceptability (CoLA) [65] contains expert judgements on whether a sentence is grammatical or not, and tests the innate linguistic bias of trained models. The Stanford Sentiment Treebank (SST-2) [54], on the other hand, is a standard binary classification task. Our model obtains an score of 45.4 on CoLA, which is an especially big jump over the previous best result of 35.0, showcasing the innate linguistic bias learned by our model. The model also achieves 91.3% accuracy on SST-2, which is competitive with the state-of-the-art results. We also achieve an overall score of 72.8 on the GLUE benchmark, which is significantly better than the previous best of 68.9.

---

### النسخة العربية

### 4.1 الإعداد

**التدريب المسبق غير الموجه** نستخدم مجموعة بيانات BooksCorpus [71] لتدريب نموذج اللغة. تحتوي على أكثر من 7000 كتاب فريد غير منشور من مجموعة متنوعة من الأنواع بما في ذلك المغامرة والخيال والرومانسية. الأهم من ذلك، أنها تحتوي على امتدادات طويلة من النص المتجاور، مما يسمح للنموذج التوليدي بتعلم الاعتماد على معلومات طويلة المدى. مجموعة بيانات بديلة، وهي معيار 1B Word، والتي يتم استخدامها من قبل نهج مماثل، ELMo [44]، هي تقريباً بنفس الحجم ولكن يتم خلطها على مستوى الجملة - مما يدمر البنية طويلة المدى. يحقق نموذج اللغة الخاص بنا حيرة منخفضة جداً على مستوى الرموز تبلغ 18.4 على هذه المدونة.

**مواصفات النموذج** يتبع نموذجنا إلى حد كبير عمل المحوّل الأصلي [62]. قمنا بتدريب محوّل فك تشفير فقط من 12 طبقة مع رؤوس انتباه ذاتي مُقنعة (حالات بُعد 768 و 12 رأس انتباه). بالنسبة لشبكات التغذية الأمامية الموضعية، استخدمنا حالات داخلية بُعد 3072. استخدمنا مخطط تحسين Adam [27] بمعدل تعلم أقصى قدره 2.5e-4. تم زيادة معدل التعلم خطياً من الصفر على مدى أول 2000 تحديث وتم تخميره إلى 0 باستخدام جدول جيبي. نُدرّب لمدة 100 حقبة على دفعات صغيرة من 64 تسلسل متجاور تم أخذ عينات عشوائية منها من 512 رمز. نظراً لأنه يتم استخدام layernorm [2] على نطاق واسع في جميع أنحاء النموذج، فإن تهيئة وزن بسيطة من $\mathcal{N}(0, 0.02)$ كانت كافية. استخدمنا مفردات ترميز bytepair (BPE) مع 40,000 دمج [53] و dropout متبقي وتضمين وانتباه بمعدل 0.1 للتنظيم. استخدمنا أيضاً نسخة معدلة من تنظيم L2 المقترح في [37]، مع $w = 0.01$ على جميع الأوزان غير المنحازة أو أوزان الكسب. بالنسبة لدالة التنشيط، استخدمنا وحدة الخطية الخطأ الغوسي (GELU) [18]. استخدمنا تضمينات موضعية مُتعلمة بدلاً من النسخة الجيبية المقترحة في العمل الأصلي. نستخدم مكتبة ftfy² لتنظيف النص الخام في BooksCorpus، وتوحيد بعض علامات الترقيم والمسافات البيضاء، واستخدام مُرمّز spaCy.³

**تفاصيل الضبط الدقيق** ما لم يُحدد خلاف ذلك، نُعيد استخدام إعدادات المعاملات الفائقة من التدريب المسبق غير الموجه. نضيف dropout إلى المُصنف بمعدل 0.1. بالنسبة لمعظم المهام، نستخدم معدل تعلم قدره 6.25e-5 وحجم دفعة 32. يتم ضبط نموذجنا بدقة بسرعة وكانت 3 حقبات من التدريب كافية لمعظم الحالات. نستخدم جدول تحلل معدل تعلم خطي مع إحماء على 0.2٪ من التدريب. تم تعيين $\lambda$ على 0.5.

### 4.2 الضبط الدقيق الموجه

نُجري تجارب على مجموعة متنوعة من المهام الموجهة بما في ذلك الاستنتاج اللغوي، والإجابة على الأسئلة، والتشابه الدلالي، وتصنيف النصوص. بعض هذه المهام متاحة كجزء من معيار GLUE متعدد المهام الذي تم إصداره مؤخراً [64]، والذي نستخدمه. يوفر الشكل 1 نظرة عامة على جميع المهام ومجموعات البيانات.

**الاستنتاج اللغوي** تتضمن مهمة الاستنتاج اللغوي (NLI)، المعروفة أيضاً بالتعرف على الاستلزام النصي، قراءة زوج من الجمل والحكم على العلاقة بينهما من أحد الاستلزام، أو التناقض، أو المحايد. على الرغم من وجود الكثير من الاهتمام الأخير [58،35،44]، تظل المهمة صعبة بسبب وجود مجموعة واسعة من الظواهر مثل الاستلزام المعجمي، والإشارة المرجعية، والغموض المعجمي والنحوي. نُقيّم على خمس مجموعات بيانات من مصادر متنوعة، بما في ذلك تسميات الصور (SNLI)، والكلام المُنسوخ، والخيال الشعبي، والتقارير الحكومية (MNLI)، ومقالات ويكيبيديا (QNLI)، وامتحانات العلوم (SciTail)، أو المقالات الإخبارية (RTE).

يوضح الجدول 2 النتائج المختلفة على مهام NLI المختلفة لنموذجنا والأساليب الحديثة المتقدمة السابقة. تتفوق طريقتنا بشكل كبير على الخطوط الأساسية في أربع من المجموعات الخمس، محققة تحسينات مطلقة تصل إلى 1.5٪ على MNLI، و5٪ على SciTail، و5.8٪ على QNLI، و0.6٪ على SNLI مقارنة بالنتائج الأفضل السابقة. يُظهر هذا قدرة نموذجنا على الاستدلال بشكل أفضل على جمل متعددة، والتعامل مع جوانب الغموض اللغوي. على RTE، واحدة من مجموعات البيانات الأصغر التي نُقيّمها (2490 مثالاً)، نحقق دقة 56٪، وهي أقل من 61.7٪ التي أبلغ عنها نموذج biLSTM متعدد المهام. بالنظر إلى الأداء القوي لنهجنا على مجموعات بيانات NLI الأكبر، من المحتمل أن نموذجنا سيستفيد من التدريب متعدد المهام أيضاً ولكننا لم نستكشف هذا حالياً.

**الإجابة على الأسئلة والاستدلال المنطقي** مهمة أخرى تتطلب جوانب من الاستدلال على جملة واحدة ومتعددة هي الإجابة على الأسئلة. نستخدم مجموعة بيانات RACE التي تم إصدارها مؤخراً [30]، والتي تتكون من مقاطع باللغة الإنجليزية مع أسئلة مرتبطة من امتحانات المدارس المتوسطة والثانوية. تبين أن هذه المدونة تحتوي على أسئلة من نوع الاستدلال أكثر من مجموعات البيانات الأخرى مثل CNN [19] أو SQuAD [47]، مما يوفر التقييم المثالي لنموذجنا الذي تم تدريبه للتعامل مع السياقات طويلة المدى. بالإضافة إلى ذلك، نُقيّم على اختبار Story Cloze [40]، والذي يتضمن اختيار النهاية الصحيحة لقصص متعددة الجمل من خيارين. في هذه المهام، يتفوق نموذجنا مرة أخرى على أفضل النتائج السابقة بهوامش كبيرة - تصل إلى 8.9٪ على Story Cloze، و5.7٪ بشكل عام على RACE. يُظهر هذا قدرة نموذجنا على التعامل مع السياقات طويلة المدى بفعالية.

**التشابه الدلالي** تتضمن مهام التشابه الدلالي (أو كشف إعادة الصياغة) التنبؤ بما إذا كانت جملتان متكافئتان دلالياً أم لا. تكمن التحديات في التعرف على إعادة صياغة المفاهيم، وفهم النفي، والتعامل مع الغموض النحوي. نستخدم ثلاث مجموعات بيانات لهذه المهمة - مدونة Microsoft Paraphrase (MRPC) [14] (التي تم جمعها من مصادر إخبارية)، ومجموعة بيانات Quora Question Pairs (QQP) [9]، ومعيار Semantic Textual Similarity (STS-B) [6]. نحصل على نتائج حديثة في اثنتين من مهام التشابه الدلالي الثلاث (الجدول 4) مع مكسب مطلق نقطة واحدة على STS-B. الفرق في الأداء على QQP كبير، مع تحسين مطلق بنسبة 4.2٪ مقارنة بـ Single-task BiLSTM + ELMo + Attn.

**التصنيف** أخيراً، نُقيّم أيضاً على مهمتي تصنيف نصوص مختلفتين. تحتوي مدونة المقبولية اللغوية (CoLA) [65] على أحكام خبراء حول ما إذا كانت الجملة نحوية أم لا، وتختبر التحيز اللغوي الفطري للنماذج المُدربة. من ناحية أخرى، فإن Stanford Sentiment Treebank (SST-2) [54] هي مهمة تصنيف ثنائي قياسية. يحصل نموذجنا على درجة 45.4 على CoLA، وهي قفزة كبيرة بشكل خاص على أفضل نتيجة سابقة وهي 35.0، مما يُظهر التحيز اللغوي الفطري الذي تعلمه نموذجنا. يحقق النموذج أيضاً دقة 91.3٪ على SST-2، وهو ما ينافس النتائج الحديثة. نحقق أيضاً درجة إجمالية قدرها 72.8 على معيار GLUE، وهو أفضل بكثير من الأفضل السابق وهو 68.9.

---

### Translation Notes

- **Tables referenced:** Table 2 (NLI results), Table 4 (Semantic similarity and classification results)
- **Datasets mentioned:** BooksCorpus, 1B Word Benchmark, SNLI, MNLI, QNLI, SciTail, RTE, RACE, CNN, SQuAD, Story Cloze, MRPC, QQP, STS-B, CoLA, SST-2, GLUE
- **Key terms introduced:**
  - Perplexity = حيرة
  - Decoder-only = فك تشفير فقط
  - Masked self-attention = انتباه ذاتي مُقنع
  - Adam optimizer = مُحسّن Adam
  - Learning rate = معدل التعلم
  - Annealing = تخمير
  - Cosine schedule = جدول جيبي
  - Minibatch = دفعة صغيرة
  - Layer normalization = تطبيع الطبقة
  - Bytepair encoding (BPE) = ترميز bytepair
  - Warmup = إحماء
  - Lexical entailment = الاستلزام المعجمي
  - Coreference = الإشارة المرجعية
  - Paraphrase detection = كشف إعادة الصياغة
  - Grammatical = نحوية

- **All numerical results preserved exactly**
- **Citations preserved:** [71], [44], [62], [27], [2], [53], [37], [18], etc.

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
