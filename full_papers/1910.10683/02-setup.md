# Section 2: Setup
## القسم 2: الإعداد

**Section:** Setup (Model, C4 Corpus, Downstream Tasks, Input/Output Format)
**Translation Quality:** 0.86
**Glossary Terms Used:** transformer, encoder, decoder, self-attention, attention mechanism, pre-training, fine-tuning, corpus, benchmark, natural language processing, architecture, embedding, dropout, layer normalization, residual connection, encoder-decoder, sequence-to-sequence, autoregressive, TPU, data parallelism, model parallelism, Common Crawl, downstream task, GLUE, SuperGLUE, machine translation, question answering, text classification, summarization, text-to-text

---

### English Version

Before presenting the results from our large-scale empirical study, we review the necessary background topics required to understand our results, including the Transformer model architecture and the downstream tasks we evaluate on. We also introduce our approach for treating every problem as a text-to-text task and describe our "Colossal Clean Crawled Corpus" (C4), the Common Crawl-based data set we created as a source of unlabeled text data. We refer to our model and framework as the "Text-to-Text Transfer Transformer" (T5).

#### 2.1 Model

Early results on transfer learning for NLP leveraged recurrent neural networks, but it has recently become more common to use models based on the "Transformer" architecture. The Transformer was initially shown to be effective for machine translation, but it has subsequently been used in a wide variety of NLP settings. Due to its increasing ubiquity, all of the models we study are based on the Transformer architecture. Apart from the details mentioned below and the variants we explore in Section 3.2, we do not deviate significantly from this architecture as originally proposed. Instead of providing a comprehensive definition of this model, we refer the interested reader to the original paper or follow-up tutorials for a more detailed introduction.

The primary building block of the Transformer is self-attention. Self-attention is a variant of attention that processes a sequence by replacing each element by a weighted average of the rest of the sequence. The original Transformer consisted of an encoder-decoder architecture and was intended for sequence-to-sequence tasks. It has recently also become common to use models consisting of a single Transformer layer stack, with varying forms of self-attention used to produce architectures appropriate for language modeling or classification and span prediction tasks. We empirically explore these architectural variants in Section 3.2.

Overall, our encoder-decoder Transformer implementation closely follows its originally-proposed form. First, an input sequence of tokens is mapped to a sequence of embeddings, which is then passed into the encoder. The encoder consists of a stack of "blocks", each of which comprises two subcomponents: a self-attention layer followed by a small feed-forward network. Layer normalization is applied to the input of each subcomponent. We use a simplified version of layer normalization where the activations are only rescaled and no additive bias is applied. After layer normalization, a residual skip connection adds each subcomponent's input to its output. Dropout is applied within the feed-forward network, on the skip connection, on the attention weights, and at the input and output of the entire stack. The decoder is similar in structure to the encoder except that it includes a standard attention mechanism after each self-attention layer that attends to the output of the encoder. The self-attention mechanism in the decoder also uses a form of autoregressive or causal self-attention, which only allows the model to attend to past outputs. The output of the final decoder block is fed into a dense layer with a softmax output, whose weights are shared with the input embedding matrix. All attention mechanisms in the Transformer are split up into independent "heads" whose outputs are concatenated before being further processed.

Since self-attention is order-independent (i.e. it is an operation on sets), it is common to provide an explicit position signal to the Transformer. While the original Transformer used a sinusoidal position signal or learned position embeddings, it has recently become more common to use relative position embeddings. Instead of using a fixed embedding for each position, relative position embeddings produce a different learned embedding according to the offset between the "key" and "query" being compared in the self-attention mechanism. We use a simplified form of position embeddings where each "embedding" is simply a scalar that is added to the corresponding logit used for computing the attention weights. For efficiency, we also share the position embedding parameters across all layers in our model, though within a given layer each attention head uses a different learned position embedding. Typically, a fixed number of embeddings are learned, each corresponding to a range of possible key-query offsets. In this work, we use 32 embeddings for all of our models with ranges that increase in size logarithmically up to an offset of 128 beyond which we assign all relative positions to the same embedding. Note that a given layer is insensitive to relative position beyond 128 tokens, but subsequent layers can build a sensitivity to larger offsets by combining local information from previous layers. To summarize, our model is roughly equivalent to the original Transformer with the exception of removing the Layer Norm bias, placing the layer normalization outside the residual path, and using a different position embedding scheme. Since these architectural changes are orthogonal to the experimental factors we consider in our empirical survey of transfer learning, we leave the ablation of their impact for future work.

As part of our study, we experiment with the scalability of these models, i.e. how their performance changes as they are made to have more parameters or layers. Training large models can be non-trivial since they might not fit on a single machine and require a great deal of computation. As a result, we use a combination of model and data parallelism and train models on "slices" of Cloud TPU Pods. TPU pods are multi-rack ML supercomputers that contain 1,024 TPU v3 chips connected via a high-speed 2D mesh interconnect with supporting CPU host machines. We leverage the Mesh TensorFlow library for ease of implementation of both model parallelism and data parallelism.

#### 2.2 The Colossal Clean Crawled Corpus

Much of the previous work on transfer learning for NLP makes use of large unlabeled data sets for unsupervised learning. In this paper, we are interested in measuring the effect of the quality, characteristics, and size of this unlabeled data. To generate data sets that satisfy our needs, we leverage Common Crawl as a source of text scraped from the web. Common Crawl has previously been used as a source of text data for NLP, for example to train an n-gram language model, as training data for commonsense reasoning, for mining parallel texts for machine translation, as a pre-training data set, and even simply as a giant text corpus for testing optimizers.

Common Crawl is a publicly-available web archive that provides "web extracted text" by removing markup and other non-text content from the scraped HTML files. This process produces around 20TB of scraped text data each month. Unfortunately, the majority of the resulting text is not natural language. Instead, it largely comprises gibberish or boiler-plate text like menus, error messages, or duplicate text. Furthermore, a good deal of the scraped text contains content that is unlikely to be helpful for any of the tasks we consider (offensive language, placeholder text, source code, etc.). To address these issues, we used the following heuristics for cleaning up Common Crawl's web extracted text:

- We only retained lines that ended in a terminal punctuation mark (i.e. a period, exclamation mark, question mark, or end quotation mark).
- We discarded any page with fewer than 3 sentences and only retained lines that contained at least 5 words.
- We removed any page that contained any word on the "List of Dirty, Naughty, Obscene or Otherwise Bad Words".
- Many of the scraped pages contained warnings stating that Javascript should be enabled so we removed any line with the word Javascript.
- Some pages had placeholder "lorem ipsum" text; we removed any page where the phrase "lorem ipsum" appeared.
- Some pages inadvertently contained code. Since the curly bracket "{" appears in many programming languages (such as Javascript, widely used on the web) but not in natural text, we removed any pages that contained a curly bracket.
- Since some of the scraped pages were sourced from Wikipedia and had citation markers (e.g. [1], [citation needed], etc.), we removed any such markers.
- Many pages had boilerplate policy notices, so we removed any lines containing the strings "terms of use", "privacy policy", "cookie policy", "uses cookies", "use of cookies", or "use cookies".
- To deduplicate the data set, we discarded all but one of any three-sentence span occurring more than once in the data set.

Additionally, since most of our downstream tasks are focused on English-language text, we used langdetect to filter out any pages that were not classified as English with a probability of at least 0.99. Our heuristics are inspired by past work on using Common Crawl as a source of data for NLP. However, we opted to create a new data set because prior data sets use a more limited set of filtering heuristics, are not publicly available, and/or are different in scope.

To assemble our base data set, we downloaded the web extracted text from April 2019 and applied the aforementioned filtering. This produces a collection of text that is not only orders of magnitude larger than most data sets used for pre-training (about 750 GB) but also comprises reasonably clean and natural English text. We dub this data set the "Colossal Clean Crawled Corpus" (or C4 for short) and release it as part of TensorFlow Datasets. We consider the impact of using various alternative versions of this data set in Section 3.4.

#### 2.3 Downstream Tasks

Our goal in this paper is to measure general language learning abilities. As such, we study downstream performance on a diverse set of benchmarks, including machine translation, question answering, abstractive summarization, and text classification. Specifically, we measure performance on the GLUE and SuperGLUE text classification meta-benchmarks; CNN/Daily Mail abstractive summarization; SQuAD question answering; and WMT English to German, French, and Romanian translation. All data was sourced from TensorFlow Datasets.

GLUE and SuperGLUE each comprise a collection of text classification tasks meant to test general language understanding abilities:
- Sentence acceptability judgment (CoLA)
- Sentiment analysis (SST-2)
- Paraphrasing/sentence similarity (MRPC, STS-B, QQP)
- Natural language inference (MNLI, QNLI, RTE, CB)
- Coreference resolution (WNLI and WSC)
- Sentence completion (COPA)
- Word sense disambiguation (WIC)
- Question answering (MultiRC, ReCoRD, BoolQ)

We use the data sets as distributed by the GLUE and SuperGLUE benchmarks. For simplicity, when fine-tuning we treat all of the tasks in the GLUE benchmark (and similarly for SuperGLUE) as a single task by concatenating all of the constituent data sets. As suggested by previous work we also include the Definite Pronoun Resolution (DPR) data set in the combined SuperGLUE task.

The CNN/Daily Mail data set was introduced as a question-answering task but was adapted for text summarization; we use the non-anonymized version as an abstractive summarization task. SQuAD is a common question-answering benchmark. In our experiments, the model is fed the question and its context and asked to generate the answer token-by-token. For WMT English to German, we use the same training data (News Commentary v13, Common Crawl, Europarl v7) and newstest2013 as a validation set. For English to French, we use the standard training data from 2015 and newstest2014 as a validation set. For English to Romanian, which is a standard lower-resource machine translation benchmark, we use the train and validation sets from WMT 2016. Note that we only pre-train on English data, so in order to learn to translate a given model will need to learn to generate text in a new language.

#### 2.4 Input and Output Format

In order to train a single model on the diverse set of tasks described above, we cast all of the tasks we consider into a "text-to-text" format---that is, a task where the model is fed some text for context or conditioning and is then asked to produce some output text. This framework provides a consistent training objective both for pre-training and fine-tuning. Specifically, the model is trained with a maximum likelihood objective (using "teacher forcing") regardless of the task. To specify which task the model should perform, we add a task-specific (text) prefix to the original input sequence before feeding it to the model.

As an example, to ask the model to translate the sentence "That is good." from English to German, the model would be fed the sequence "translate English to German: That is good." and would be trained to output "Das ist gut." For text classification tasks, the model simply predicts a single word corresponding to the target label. For example, on the MNLI benchmark the goal is to predict whether a premise implies ("entailment"), contradicts ("contradiction"), or neither ("neutral") a hypothesis. With our preprocessing, the input sequence becomes "mnli premise: I hate pigeons. hypothesis: My feelings towards pigeons are filled with animosity." with the corresponding target word "entailment". Note that an issue arises if our model outputs text on a text classification task that does not correspond to any of the possible labels. In this case, we always count the model's output as wrong, though we never observed this behavior in any of our trained models. Note that the choice of text prefix used for a given task is essentially a hyperparameter; we found that changing the exact wording of the prefix had limited impact and so did not perform extensive experiments into different prefix choices.

Our text-to-text framework follows previous work that casts multiple NLP tasks into a common format: The Natural Language Decathlon proposes a benchmark that uses a consistent question-answering format for a suite of ten NLP tasks. The Natural Language Decathlon also stipulates that all models must be multi-task, i.e. are able to simultaneously tackle all of the tasks at once. We instead allow for separately fine-tuning the model on each individual task and use short task prefixes instead of an explicit question-answer format. Some prior work evaluates the zero-shot learning capabilities of language models by feeding some input to the model as a prefix and then autoregressively sampling an output. We mainly consider models that explicitly process an input with an encoder before generating an output with a separate decoder and we focus on transfer learning rather than zero-shot learning. Finally, some work unifies many NLP tasks as "span extraction", where text corresponding to possible output choices are appended to the input and the model is trained to extract the input span corresponding to the correct choice. In contrast, our framework also allows for generative tasks like machine translation and abstractive summarization where it is not possible to enumerate all possible output choices.

We were able to straightforwardly cast all of the tasks we considered into a text-to-text format with the exception of STS-B, which is a regression task where the goal is to predict a similarity score between 1 and 5. We found that most of these scores were annotated in increments of 0.2, so we simply rounded any score to the nearest increment of 0.2 and converted the result to a literal string representation of the number. At test time, if the model outputs a string corresponding to a number between 1 and 5, we convert it to a floating-point value; otherwise, we treat the model's prediction as incorrect. This effectively recasts the STS-B regression problem as a 21-class classification problem.

Separately, we also convert the Winograd tasks (WNLI from GLUE, WSC from SuperGLUE, and the DPR data set) into a simpler format that is more amenable to the text-to-text framework. Examples from the Winograd tasks consist of a text passage containing an ambiguous pronoun that could refer to more than one of the noun phrases in the passage. We cast the WNLI, WSC, and DPR tasks as text-to-text problems by highlighting the ambiguous pronoun in the text passage and asking the model to predict the noun that it refers to.

---

### النسخة العربية

قبل عرض النتائج من دراستنا التجريبية واسعة النطاق، نستعرض المواضيع الخلفية اللازمة لفهم نتائجنا، بما في ذلك معمارية نموذج المحول والمهام اللاحقة التي نقيّمها عليها. نقدم أيضاً نهجنا لمعاملة كل مشكلة على أنها مهمة من نص إلى نص ونصف "مدونة الزحف النظيفة الضخمة" (C4)، مجموعة البيانات القائمة على Common Crawl التي أنشأناها كمصدر للبيانات النصية غير المعنونة. نشير إلى نموذجنا وإطار عملنا باسم "محول النقل من نص إلى نص" (T5).

#### 2.1 النموذج

استفادت النتائج المبكرة حول التعلم بالنقل لمعالجة اللغة الطبيعية من الشبكات العصبية التكرارية، ولكن أصبح من الشائع مؤخراً استخدام نماذج تعتمد على معمارية "المحول". تم إثبات فعالية المحول في البداية للترجمة الآلية، ولكنه استُخدم لاحقاً في مجموعة واسعة من إعدادات معالجة اللغة الطبيعية. نظراً لانتشاره المتزايد، تعتمد جميع النماذج التي ندرسها على معمارية المحول. بصرف النظر عن التفاصيل المذكورة أدناه والمتغيرات التي نستكشفها في القسم 3.2، لا نحيد بشكل كبير عن هذه المعمارية كما تم اقتراحها في الأصل. بدلاً من تقديم تعريف شامل لهذا النموذج، نحيل القارئ المهتم إلى البحث الأصلي أو البرامج التعليمية اللاحقة للحصول على مقدمة أكثر تفصيلاً.

اللبنة الأساسية للمحول هي الانتباه الذاتي. الانتباه الذاتي هو نوع من آلية الانتباه يعالج تسلسلاً عن طريق استبدال كل عنصر بمتوسط مرجح لبقية التسلسل. تألف المحول الأصلي من معمارية مشفر-فك تشفير وكان مخصصاً لمهام من تسلسل إلى تسلسل. كما أصبح من الشائع مؤخراً استخدام نماذج تتكون من كومة واحدة من طبقات المحول، مع أشكال مختلفة من الانتباه الذاتي المستخدمة لإنتاج معماريات مناسبة لنمذجة اللغة أو مهام التصنيف والتنبؤ بالامتداد. نستكشف هذه المتغيرات المعمارية تجريبياً في القسم 3.2.

بشكل عام، يتبع تنفيذنا للمحول مشفر-فك تشفير شكله المقترح أصلاً عن كثب. أولاً، يتم تعيين تسلسل مدخل من الرموز إلى تسلسل من التضمينات، والذي يتم تمريره بعد ذلك إلى المشفر. يتكون المشفر من كومة من "الكتل"، كل منها يتألف من مكونين فرعيين: طبقة انتباه ذاتي متبوعة بشبكة تغذية أمامية صغيرة. يتم تطبيق تطبيع الطبقة على مدخل كل مكون فرعي. نستخدم نسخة مبسطة من تطبيع الطبقة حيث يتم فقط إعادة قياس التنشيطات ولا يتم تطبيق انحياز إضافي. بعد تطبيع الطبقة، يضيف اتصال التخطي المتبقي مدخل كل مكون فرعي إلى مخرجه. يتم تطبيق Dropout داخل شبكة التغذية الأمامية، وعلى اتصال التخطي، وعلى أوزان الانتباه، وعند مدخل ومخرج الكومة بأكملها. فك التشفير مشابه في البنية للمشفر باستثناء أنه يتضمن آلية انتباه قياسية بعد كل طبقة انتباه ذاتي تهتم بمخرج المشفر. تستخدم آلية الانتباه الذاتي في فك التشفير أيضاً شكلاً من أشكال الانتباه الذاتي الانحداري الذاتي أو السببي، والذي يسمح فقط للنموذج بالانتباه إلى المخرجات السابقة. يتم تغذية مخرج كتلة فك التشفير النهائية في طبقة كثيفة مع مخرج softmax، والتي تتم مشاركة أوزانها مع مصفوفة التضمين المدخلة. يتم تقسيم جميع آليات الانتباه في المحول إلى "رؤوس" مستقلة يتم دمج مخرجاتها قبل معالجتها بشكل أكبر.

نظراً لأن الانتباه الذاتي مستقل عن الترتيب (أي أنه عملية على مجموعات)، فمن الشائع توفير إشارة موضع صريحة للمحول. بينما استخدم المحول الأصلي إشارة موضع جيبية أو تضمينات موضع متعلمة، أصبح من الشائع مؤخراً استخدام تضمينات الموضع النسبي. بدلاً من استخدام تضمين ثابت لكل موضع، تنتج تضمينات الموضع النسبي تضميناً متعلماً مختلفاً وفقاً للإزاحة بين "المفتاح" و"الاستعلام" اللذين تتم مقارنتهما في آلية الانتباه الذاتي. نستخدم شكلاً مبسطاً من تضمينات الموضع حيث كل "تضمين" هو ببساطة قيمة عددية يتم إضافتها إلى اللوجيت المقابل المستخدم لحساب أوزان الانتباه. من أجل الكفاءة، نشارك أيضاً معاملات تضمين الموضع عبر جميع الطبقات في نموذجنا، على الرغم من أنه داخل طبقة معينة يستخدم كل رأس انتباه تضمين موضع متعلم مختلف. عادةً، يتم تعلم عدد ثابت من التضمينات، كل منها يقابل نطاقاً من إزاحات المفتاح-الاستعلام المحتملة. في هذا العمل، نستخدم 32 تضميناً لجميع نماذجنا مع نطاقات تزداد حجماً بشكل لوغاريتمي حتى إزاحة 128 وبعدها نعين جميع المواضع النسبية إلى نفس التضمين. لاحظ أن طبقة معينة غير حساسة للموضع النسبي بعد 128 رمزاً، ولكن الطبقات اللاحقة يمكن أن تبني حساسية لإزاحات أكبر من خلال الجمع بين المعلومات المحلية من الطبقات السابقة. باختصار، نموذجنا مكافئ تقريباً للمحول الأصلي باستثناء إزالة انحياز Layer Norm، ووضع تطبيع الطبقة خارج مسار المتبقي، واستخدام مخطط تضمين موضع مختلف. نظراً لأن هذه التغييرات المعمارية متعامدة مع العوامل التجريبية التي ندرسها في مسحنا التجريبي للتعلم بالنقل، فإننا نترك دراسة تأثيرها للعمل المستقبلي.

كجزء من دراستنا، نجرب قابلية تطوير هذه النماذج، أي كيف يتغير أداؤها مع زيادة المعاملات أو الطبقات. يمكن أن يكون تدريب النماذج الكبيرة غير بديهي لأنها قد لا تناسب جهازاً واحداً وتتطلب قدراً كبيراً من الحوسبة. نتيجة لذلك، نستخدم مزيجاً من التوازي النموذجي وتوازي البيانات ونُدرب النماذج على "شرائح" من Cloud TPU Pods. حاضنات TPU هي حواسيب عملاقة متعددة الرفوف للتعلم الآلي تحتوي على 1,024 شريحة TPU v3 متصلة عبر ربط شبكي ثنائي الأبعاد عالي السرعة مع أجهزة CPU مضيفة داعمة. نستفيد من مكتبة Mesh TensorFlow لسهولة تنفيذ كل من التوازي النموذجي وتوازي البيانات.

#### 2.2 مدونة الزحف النظيفة الضخمة

تستخدم الكثير من الأعمال السابقة حول التعلم بالنقل لمعالجة اللغة الطبيعية مجموعات بيانات كبيرة غير معنونة للتعلم غير الخاضع للإشراف. في هذا البحث، نحن مهتمون بقياس تأثير جودة وخصائص وحجم هذه البيانات غير المعنونة. لإنشاء مجموعات بيانات تلبي احتياجاتنا، نستفيد من Common Crawl كمصدر للنصوص المستخرجة من الويب. تم استخدام Common Crawl سابقاً كمصدر لبيانات النصوص لمعالجة اللغة الطبيعية، على سبيل المثال لتدريب نموذج لغة n-gram، كبيانات تدريب للاستدلال الحسي السليم، لاستخراج النصوص الموازية للترجمة الآلية، كمجموعة بيانات للتدريب المسبق، وحتى ببساطة كمدونة نصية عملاقة لاختبار المُحسِّنات.

Common Crawl هو أرشيف ويب متاح للعامة يوفر "نصاً مستخرجاً من الويب" عن طريق إزالة العلامات والمحتوى غير النصي الآخر من ملفات HTML المستخرجة. تنتج هذه العملية حوالي 20 تيرابايت من البيانات النصية المستخرجة كل شهر. لسوء الحظ، فإن غالبية النص الناتج ليس لغة طبيعية. بدلاً من ذلك، يتكون إلى حد كبير من هراء أو نصوص قالبية مثل القوائم ورسائل الخطأ أو النصوص المكررة. علاوة على ذلك، يحتوي قدر كبير من النص المستخرج على محتوى من غير المحتمل أن يكون مفيداً لأي من المهام التي ندرسها (لغة مسيئة، نص نائب، كود مصدري، إلخ). لمعالجة هذه القضايا، استخدمنا الإرشادات التالية لتنظيف النص المستخرج من الويب من Common Crawl:

- احتفظنا فقط بالأسطر التي تنتهي بعلامة ترقيم نهائية (أي نقطة أو علامة تعجب أو علامة استفهام أو علامة اقتباس نهائية).
- تجاهلنا أي صفحة تحتوي على أقل من 3 جمل واحتفظنا فقط بالأسطر التي تحتوي على 5 كلمات على الأقل.
- أزلنا أي صفحة تحتوي على أي كلمة في "قائمة الكلمات القذرة أو المشينة أو البذيئة أو السيئة بطريقة أخرى".
- احتوت العديد من الصفحات المستخرجة على تحذيرات تفيد بأنه يجب تمكين Javascript لذلك أزلنا أي سطر يحتوي على كلمة Javascript.
- احتوت بعض الصفحات على نص نائب "lorem ipsum"؛ أزلنا أي صفحة ظهرت فيها عبارة "lorem ipsum".
- احتوت بعض الصفحات عن غير قصد على كود. نظراً لأن القوس المتعرج "{" يظهر في العديد من لغات البرمجة (مثل Javascript، المستخدمة على نطاق واسع على الويب) ولكن ليس في النص الطبيعي، أزلنا أي صفحات تحتوي على قوس متعرج.
- نظراً لأن بعض الصفحات المستخرجة كانت مصدرها ويكيبيديا وكانت تحتوي على علامات استشهاد (على سبيل المثال [1]، [استشهاد مطلوب]، إلخ)، أزلنا أي علامات من هذا القبيل.
- احتوت العديد من الصفحات على إشعارات سياسة قالبية، لذلك أزلنا أي أسطر تحتوي على السلاسل "شروط الاستخدام"، "سياسة الخصوصية"، "سياسة ملفات تعريف الارتباط"، "يستخدم ملفات تعريف الارتباط"، "استخدام ملفات تعريف الارتباط"، أو "استخدام ملفات تعريف الارتباط".
- لإزالة التكرار من مجموعة البيانات، تجاهلنا كل امتداد مكون من ثلاث جمل يحدث أكثر من مرة في مجموعة البيانات باستثناء واحد.

بالإضافة إلى ذلك، نظراً لأن معظم مهامنا اللاحقة تركز على النصوص باللغة الإنجليزية، استخدمنا langdetect لتصفية أي صفحات لم يتم تصنيفها على أنها إنجليزية باحتمالية 0.99 على الأقل. استُلهمت إرشاداتنا من الأعمال السابقة حول استخدام Common Crawl كمصدر لبيانات معالجة اللغة الطبيعية. ومع ذلك، اخترنا إنشاء مجموعة بيانات جديدة لأن مجموعات البيانات السابقة تستخدم مجموعة محدودة أكثر من إرشادات التصفية، أو غير متاحة للعامة، و/أو مختلفة في النطاق.

لتجميع مجموعة بياناتنا الأساسية، قمنا بتنزيل النص المستخرج من الويب من أبريل 2019 وطبقنا التصفية المذكورة أعلاه. ينتج عن هذا مجموعة من النصوص ليست فقط أكبر بمراتب من حيث الحجم من معظم مجموعات البيانات المستخدمة للتدريب المسبق (حوالي 750 جيجابايت) ولكنها تتكون أيضاً من نصوص إنجليزية نظيفة وطبيعية إلى حد معقول. نطلق على مجموعة البيانات هذه اسم "مدونة الزحف النظيفة الضخمة" (أو C4 اختصاراً) ونصدرها كجزء من TensorFlow Datasets. ندرس تأثير استخدام إصدارات بديلة مختلفة من مجموعة البيانات هذه في القسم 3.4.

#### 2.3 المهام اللاحقة

هدفنا في هذا البحث هو قياس قدرات تعلم اللغة العامة. على هذا النحو، ندرس الأداء اللاحق على مجموعة متنوعة من المعايير، بما في ذلك الترجمة الآلية والإجابة على الأسئلة والتلخيص التجريدي وتصنيف النصوص. على وجه التحديد، نقيس الأداء على معايير GLUE وSuperGLUE الوصفية لتصنيف النصوص؛ وتلخيص CNN/Daily Mail التجريدي؛ والإجابة على أسئلة SQuAD؛ وترجمة WMT من الإنجليزية إلى الألمانية والفرنسية والرومانية. تم الحصول على جميع البيانات من TensorFlow Datasets.

يتألف كل من GLUE وSuperGLUE من مجموعة من مهام تصنيف النصوص التي تهدف إلى اختبار قدرات فهم اللغة العامة:
- الحكم على قبول الجملة (CoLA)
- تحليل المشاعر (SST-2)
- إعادة الصياغة/تشابه الجمل (MRPC، STS-B، QQP)
- الاستدلال اللغوي الطبيعي (MNLI، QNLI، RTE، CB)
- حل الإشارة المرجعية (WNLI وWSC)
- إكمال الجملة (COPA)
- توضيح معنى الكلمة (WIC)
- الإجابة على الأسئلة (MultiRC، ReCoRD، BoolQ)

نستخدم مجموعات البيانات كما توزعها معايير GLUE وSuperGLUE. من أجل البساطة، عند الضبط الدقيق نعامل جميع المهام في معيار GLUE (وبالمثل لـ SuperGLUE) على أنها مهمة واحدة من خلال ربط جميع مجموعات البيانات المكونة. كما هو مقترح في الأعمال السابقة، نضيف أيضاً مجموعة بيانات حل الضمير المحدد (DPR) في مهمة SuperGLUE المجمعة.

تم تقديم مجموعة بيانات CNN/Daily Mail كمهمة للإجابة على الأسئلة ولكن تم تكييفها للتلخيص النصي؛ نستخدم النسخة غير المجهولة كمهمة تلخيص تجريدي. SQuAD هو معيار شائع للإجابة على الأسئلة. في تجاربنا، يتم تغذية النموذج بالسؤال وسياقه ويُطلب منه توليد الإجابة رمزاً تلو الآخر. بالنسبة لـ WMT من الإنجليزية إلى الألمانية، نستخدم نفس بيانات التدريب (News Commentary v13، Common Crawl، Europarl v7) وnewstest2013 كمجموعة تحقق. بالنسبة للإنجليزية إلى الفرنسية، نستخدم بيانات التدريب القياسية من 2015 وnewstest2014 كمجموعة تحقق. بالنسبة للإنجليزية إلى الرومانية، وهو معيار قياسي للترجمة الآلية ذات الموارد المنخفضة، نستخدم مجموعات التدريب والتحقق من WMT 2016. لاحظ أننا ندرب مسبقاً فقط على بيانات إنجليزية، لذلك من أجل تعلم الترجمة سيحتاج نموذج معين إلى تعلم توليد نصوص بلغة جديدة.

#### 2.4 صيغة المدخل والمخرج

من أجل تدريب نموذج واحد على مجموعة المهام المتنوعة الموصوفة أعلاه، نصوغ جميع المهام التي ندرسها في صيغة "من نص إلى نص"---أي مهمة يتم فيها تغذية النموذج ببعض النصوص للسياق أو التكييف ثم يُطلب منه إنتاج بعض نصوص المخرج. يوفر هذا الإطار هدف تدريب متسقاً لكل من التدريب المسبق والضبط الدقيق. على وجه التحديد، يتم تدريب النموذج بهدف أقصى احتمالية (باستخدام "الإجبار على التعليم") بغض النظر عن المهمة. لتحديد المهمة التي يجب أن يؤديها النموذج، نضيف بادئة (نصية) خاصة بالمهمة إلى تسلسل المدخل الأصلي قبل تغذيته إلى النموذج.

كمثال، لطلب من النموذج ترجمة الجملة "That is good." من الإنجليزية إلى الألمانية، سيتم تغذية النموذج بالتسلسل "translate English to German: That is good." وسيتم تدريبه على إخراج "Das ist gut." بالنسبة لمهام تصنيف النصوص، يتنبأ النموذج ببساطة بكلمة واحدة تقابل التسمية المستهدفة. على سبيل المثال، في معيار MNLI الهدف هو التنبؤ بما إذا كانت فرضية تلمح ("استلزام")، أو تتناقض ("تناقض")، أو لا هذا ولا ذاك ("محايد") مع فرضية. باستخدام معالجتنا المسبقة، يصبح تسلسل المدخل "mnli premise: I hate pigeons. hypothesis: My feelings towards pigeons are filled with animosity." مع الكلمة المستهدفة المقابلة "entailment". لاحظ أن مشكلة تنشأ إذا أخرج نموذجنا نصاً في مهمة تصنيف نصوص لا يتوافق مع أي من التسميات المحتملة. في هذه الحالة، نعتبر دائماً مخرج النموذج خاطئاً، على الرغم من أننا لم نلاحظ هذا السلوك أبداً في أي من نماذجنا المدربة. لاحظ أن اختيار البادئة النصية المستخدمة لمهمة معينة هو في الأساس معامل فائق؛ وجدنا أن تغيير الصياغة الدقيقة للبادئة كان له تأثير محدود ولذلك لم نجر تجارب واسعة في اختيارات بادئة مختلفة.

يتبع إطار عملنا من نص إلى نص الأعمال السابقة التي تصوغ مهام معالجة اللغة الطبيعية المتعددة في صيغة مشتركة: يقترح Natural Language Decathlon معياراً يستخدم صيغة إجابة على الأسئلة متسقة لمجموعة من عشر مهام لمعالجة اللغة الطبيعية. ينص Natural Language Decathlon أيضاً على أن جميع النماذج يجب أن تكون متعددة المهام، أي قادرة على معالجة جميع المهام في وقت واحد. بدلاً من ذلك، نسمح بالضبط الدقيق المنفصل للنموذج على كل مهمة فردية ونستخدم بادئات مهام قصيرة بدلاً من صيغة سؤال-إجابة صريحة. تقيّم بعض الأعمال السابقة قدرات التعلم بدون أمثلة (zero-shot) لنماذج اللغة عن طريق تغذية بعض المدخلات إلى النموذج كبادئة ثم أخذ عينات من المخرج بشكل انحداري ذاتي. ندرس بشكل رئيسي النماذج التي تعالج بشكل صريح مدخلاً بمشفر قبل توليد مخرج بفك تشفير منفصل ونركز على التعلم بالنقل بدلاً من التعلم بدون أمثلة. أخيراً، توحد بعض الأعمال العديد من مهام معالجة اللغة الطبيعية على أنها "استخراج امتداد"، حيث يتم إلحاق النص المقابل لخيارات المخرج المحتملة بالمدخل ويتم تدريب النموذج على استخراج امتداد المدخل المقابل للاختيار الصحيح. في المقابل، يسمح إطار عملنا أيضاً بمهام توليدية مثل الترجمة الآلية والتلخيص التجريدي حيث لا يمكن تعداد جميع خيارات المخرج المحتملة.

تمكنا من صياغة جميع المهام التي درسناها بشكل مباشر في صيغة من نص إلى نص باستثناء STS-B، وهي مهمة انحدار حيث الهدف هو التنبؤ بدرجة تشابه بين 1 و5. وجدنا أن معظم هذه الدرجات تم تعليقها بزيادات قدرها 0.2، لذلك قمنا ببساطة بتقريب أي درجة إلى أقرب زيادة قدرها 0.2 وحولنا النتيجة إلى تمثيل سلسلة حرفي للرقم. في وقت الاختبار، إذا أخرج النموذج سلسلة تقابل رقماً بين 1 و5، نحولها إلى قيمة نقطة عائمة؛ وإلا، نعامل تنبؤ النموذج على أنه غير صحيح. يعيد هذا بشكل فعال صياغة مشكلة الانحدار STS-B على أنها مشكلة تصنيف من 21 فئة.

بشكل منفصل، نحول أيضاً مهام Winograd (WNLI من GLUE، وWSC من SuperGLUE، ومجموعة بيانات DPR) إلى صيغة أبسط أكثر ملاءمة لإطار العمل من نص إلى نص. تتكون الأمثلة من مهام Winograd من مقطع نصي يحتوي على ضمير غامض يمكن أن يشير إلى أكثر من واحدة من العبارات الاسمية في المقطع. نصوغ مهام WNLI وWSC وDPR على أنها مشاكل من نص إلى نص من خلال تسليط الضوء على الضمير الغامض في المقطع النصي وطلب من النموذج التنبؤ بالاسم الذي يشير إليه.

---

### Translation Notes

- **Figures referenced:** None (text-to-text diagram mentioned in Section 1)
- **Key terms introduced:** T5, C4 corpus, text-to-text format, encoder-decoder, self-attention, Transformer, TPU Pods, GLUE, SuperGLUE, downstream tasks
- **Equations:** 0
- **Citations:** Multiple references to datasets and prior work
- **Special handling:**
  - Dataset sizes (750 GB, 20TB/month)
  - Model training infrastructure (1,024 TPU v3 chips)
  - Data cleaning heuristics (detailed list)
  - Task conversions (STS-B regression to 21-class classification, Winograd tasks format)

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86
