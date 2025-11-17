# Section 2: Approach
## القسم 2: المنهجية

**Section:** methodology/approach
**Translation Quality:** 0.86
**Glossary Terms Used:** training, transformer, optimizer, dataset, token, tokenizer, pre-normalization, activation function, positional embeddings, learning rate, batch size, gradient clipping, attention mechanism

---

### English Version

Our training approach is similar to the methods described in previous work (Brown et al., 2020; Chowdhery et al., 2022), and is inspired by the Chinchilla scaling laws (Hoffmann et al., 2022). We train large transformers on a large quantity of textual data using a standard optimizer.

## 2.1 Pre-training Data

Our training dataset is a mixture of several sources, reported in Table 1, that cover a diverse set of domains. For the most part, we reuse data sources that have been leveraged to train other LLMs, with the restriction of only using data that is publicly available, and compatible with open sourcing. This leads to the following mixture of data and the percentage they represent in the training set:

**English CommonCrawl [67%].** We preprocess five CommonCrawl dumps, ranging from 2017 to 2020, with the CCNet pipeline (Wenzek et al., 2020). This process deduplicates the data at the line level, performs language identification with a fastText linear classifier to remove non-English pages and filters low quality content with an n-gram language model. In addition, we trained a linear model to classify pages used as references in Wikipedia v.s. randomly sampled pages, and discarded pages not classified as references.

**C4 [15%].** During exploratory experiments, we observed that using diverse pre-processed CommonCrawl datasets improves performance. We thus included the publicly available C4 dataset (Raffel et al., 2020) in our data. The preprocessing of C4 also contains deduplication and language identification steps: the main difference with CCNet is the quality filtering, which mostly relies on heuristics such as presence of punctuation marks or the number of words and sentences in a webpage.

**Github [4.5%].** We use the public GitHub dataset available on Google BigQuery. We only kept projects that are distributed under the Apache, BSD and MIT licenses. Additionally, we filtered low quality files with heuristics based on the line length or proportion of alphanumeric characters, and removed boilerplate, such as headers, with regular expressions. Finally, we deduplicate the resulting dataset at the file level, with exact matches.

**Wikipedia [4.5%].** We add Wikipedia dumps from the June-August 2022 period, covering 20 languages, which use either the Latin or Cyrillic scripts: bg, ca, cs, da, de, en, es, fr, hr, hu, it, nl, pl, pt, ro, ru, sl, sr, sv, uk. We process the data to remove hyperlinks, comments and other formatting boilerplate.

**Gutenberg and Books3 [4.5%].** We include two book corpora in our training dataset: the Gutenberg Project, which contains books that are in the public domain, and the Books3 section of ThePile (Gao et al., 2020), a publicly available dataset for training large language models. We perform deduplication at the book level, removing books with more than 90% content overlap.

**ArXiv [2.5%].** We process arXiv Latex files to add scientific data to our dataset. Following Lewkowycz et al. (2022), we removed everything before the first section, as well as the bibliography. We also removed the comments from the .tex files, and inline-expanded definitions and macros written by users to increase consistency across papers.

**Stack Exchange [2%].** We include a dump of Stack Exchange, a website of high quality questions and answers that covers a diverse set of domains, ranging from computer science to chemistry. We kept the data from the 28 largest websites, removed the HTML tags from text and sorted the answers by score (from highest to lowest).

**Tokenizer.** We tokenize the data with the byte-pair encoding (BPE) algorithm (Sennrich et al., 2015), using the implementation from SentencePiece (Kudo and Richardson, 2018). Notably, we split all numbers into individual digits, and fallback to bytes to decompose unknown UTF-8 characters.

Overall, our entire training dataset contains roughly 1.4T tokens after tokenization. For most of our training data, each token is used only once during training, with the exception of the Wikipedia and Books domains, over which we perform approximately two epochs.

## 2.2 Architecture

Following recent work on large language models, our network is based on the transformer architecture (Vaswani et al., 2017). We leverage various improvements that were subsequently proposed, and used in different models such as PaLM. Here are the main difference with the original architecture, and where we were found the inspiration for this change (in bracket):

**Pre-normalization [GPT3].** To improve the training stability, we normalize the input of each transformer sub-layer, instead of normalizing the output. We use the RMSNorm normalizing function, introduced by Zhang and Sennrich (2019).

**SwiGLU activation function [PaLM].** We replace the ReLU non-linearity by the SwiGLU activation function, introduced by Shazeer (2020) to improve the performance. We use a dimension of 2/3·4d instead of 4d as in PaLM.

**Rotary Embeddings [GPTNeo].** We remove the absolute positional embeddings, and instead, add rotary positional embeddings (RoPE), introduced by Su et al. (2021), at each layer of the network.

The details of the hyper-parameters for our different models are given in Table 2.

## 2.3 Optimizer

Our models are trained using the AdamW optimizer (Loshchilov and Hutter, 2017), with the following hyper-parameters: β₁ = 0.9, β₂ = 0.95. We use a cosine learning rate schedule, such that the final learning rate is equal to 10% of the maximal learning rate. We use a weight decay of 0.1 and gradient clipping of 1.0. We use 2,000 warmup steps, and vary the learning rate and batch size with the size of the model (see Table 2 for details).

## 2.4 Efficient implementation

We make several optimizations to improve the training speed of our models. First, we use an efficient implementation of the causal multi-head attention to reduce memory usage and runtime. This implementation, available in the xformers library, is inspired by Rabe and Staats (2021) and uses the backward from Dao et al. (2022). This is achieved by not storing the attention weights and not computing the key/query scores that are masked due to the causal nature of the language modeling task.

To further improve training efficiency, we reduced the amount of activations that are recomputed during the backward pass with checkpointing. More precisely, we save the activations that are expensive to compute, such as the outputs of linear layers. This is achieved by manually implementing the backward function for the transformer layers, instead of relying on the PyTorch autograd. To fully benefit from this optimization, we need to reduce the memory usage of the model by using model and sequence parallelism, as described by Korthikanti et al. (2022). Moreover, we also overlap the computation of activations and the communication between GPUs over the network (due to all_reduce operations) as much as possible.

When training a 65B-parameter model, our code processes around 380 tokens/sec/GPU on 2048 A100 GPU with 80GB of RAM. This means that training over our dataset containing 1.4T tokens takes approximately 21 days.

---

### النسخة العربية

منهجية التدريب الخاصة بنا مشابهة للطرق الموصوفة في الأعمال السابقة (Brown et al., 2020; Chowdhery et al., 2022)، ومستوحاة من قوانين التوسيع الخاصة بـ Chinchilla (Hoffmann et al., 2022). ندرب محولات كبيرة على كمية كبيرة من البيانات النصية باستخدام محسِّن قياسي.

## 2.1 بيانات التدريب المسبق

مجموعة بيانات التدريب الخاصة بنا عبارة عن مزيج من عدة مصادر، موضحة في الجدول 1، تغطي مجموعة متنوعة من المجالات. في معظم الأحيان، نعيد استخدام مصادر البيانات التي تم الاستفادة منها لتدريب نماذج لغة كبيرة أخرى، مع قيد استخدام البيانات المتاحة للعموم فقط والمتوافقة مع المصادر المفتوحة. يؤدي ذلك إلى المزيج التالي من البيانات والنسبة المئوية التي تمثلها في مجموعة التدريب:

**CommonCrawl الإنجليزية [67%].** نعالج مسبقاً خمس نسخ من CommonCrawl، تتراوح من 2017 إلى 2020، باستخدام خط أنابيب CCNet (Wenzek et al., 2020). تقوم هذه العملية بإزالة التكرار على مستوى السطر، وتنفذ تحديد اللغة باستخدام مصنف خطي fastText لإزالة الصفحات غير الإنجليزية وتصفية المحتوى منخفض الجودة باستخدام نموذج لغة n-gram. بالإضافة إلى ذلك، درّبنا نموذجاً خطياً لتصنيف الصفحات المستخدمة كمراجع في ويكيبيديا مقابل الصفحات المختارة عشوائياً، واستبعدنا الصفحات التي لم يتم تصنيفها كمراجع.

**C4 [15%].** خلال التجارب الاستكشافية، لاحظنا أن استخدام مجموعات بيانات CommonCrawl المعالجة مسبقاً المتنوعة يحسن الأداء. لذلك قمنا بتضمين مجموعة بيانات C4 المتاحة للعموم (Raffel et al., 2020) في بياناتنا. تحتوي المعالجة المسبقة لـ C4 أيضاً على خطوات إزالة التكرار وتحديد اللغة: الفرق الرئيسي مع CCNet هو تصفية الجودة، التي تعتمد في الغالب على الاستدلالات مثل وجود علامات الترقيم أو عدد الكلمات والجمل في صفحة الويب.

**Github [4.5%].** نستخدم مجموعة بيانات GitHub العامة المتاحة على Google BigQuery. احتفظنا فقط بالمشاريع الموزعة بموجب تراخيص Apache وBSD وMIT. بالإضافة إلى ذلك، قمنا بتصفية الملفات منخفضة الجودة باستخدام الاستدلالات بناءً على طول السطر أو نسبة الأحرف الأبجدية الرقمية، وأزلنا النصوص النمطية، مثل الرؤوس، باستخدام التعبيرات العادية. أخيراً، نزيل التكرار من مجموعة البيانات الناتجة على مستوى الملف، بمطابقات دقيقة.

**ويكيبيديا [4.5%].** نضيف نسخ ويكيبيديا من فترة يونيو-أغسطس 2022، تغطي 20 لغة، والتي تستخدم إما النصوص اللاتينية أو السيريلية: bg, ca, cs, da, de, en, es, fr, hr, hu, it, nl, pl, pt, ro, ru, sl, sr, sv, uk. نعالج البيانات لإزالة الروابط التشعبية والتعليقات والنصوص النمطية الأخرى للتنسيق.

**Gutenberg وBooks3 [4.5%].** نضمّن مجموعتي كتب في مجموعة بيانات التدريب الخاصة بنا: مشروع Gutenberg، الذي يحتوي على كتب في المجال العام، وقسم Books3 من ThePile (Gao et al., 2020)، وهي مجموعة بيانات متاحة للعموم لتدريب نماذج لغة كبيرة. نجري إزالة التكرار على مستوى الكتاب، ونزيل الكتب التي يزيد تداخل محتواها عن 90%.

**ArXiv [2.5%].** نعالج ملفات LaTeX من arXiv لإضافة بيانات علمية إلى مجموعة البيانات الخاصة بنا. بعد Lewkowycz et al. (2022)، أزلنا كل شيء قبل القسم الأول، بالإضافة إلى الببليوغرافيا. كما أزلنا التعليقات من ملفات .tex، ووسّعنا التعريفات والماكرو المكتوبة من قبل المستخدمين بشكل مضمّن لزيادة الاتساق عبر الأوراق البحثية.

**Stack Exchange [2%].** نضمّن نسخة من Stack Exchange، وهو موقع ويب يحتوي على أسئلة وأجوبة عالية الجودة تغطي مجموعة متنوعة من المجالات، تتراوح من علوم الكمبيوتر إلى الكيمياء. احتفظنا بالبيانات من أكبر 28 موقعاً، وأزلنا علامات HTML من النص ورتبنا الإجابات حسب النقاط (من الأعلى إلى الأدنى).

**المرمّز.** نرمّز البيانات باستخدام خوارزمية ترميز زوج البايتات (BPE) (Sennrich et al., 2015)، باستخدام التنفيذ من SentencePiece (Kudo and Richardson, 2018). نقسم جميع الأرقام إلى أرقام فردية، ونعود إلى البايتات لتحليل أحرف UTF-8 غير المعروفة.

بشكل عام، تحتوي مجموعة بيانات التدريب الكاملة الخاصة بنا على ما يقرب من 1.4T رمز بعد الترميز. بالنسبة لمعظم بيانات التدريب الخاصة بنا، يتم استخدام كل رمز مرة واحدة فقط أثناء التدريب، باستثناء مجالات ويكيبيديا والكتب، حيث نجري ما يقرب من حقبتين.

## 2.2 المعمارية

بعد الأعمال الحديثة على نماذج اللغة الكبيرة، تعتمد شبكتنا على معمارية المحول (Vaswani et al., 2017). نستفيد من التحسينات المختلفة التي تم اقتراحها لاحقاً، والمستخدمة في نماذج مختلفة مثل PaLM. فيما يلي الاختلافات الرئيسية مع المعمارية الأصلية، وأين وجدنا الإلهام لهذا التغيير (بين قوسين):

**التطبيع المسبق [GPT3].** لتحسين استقرار التدريب، نطبّع مدخلات كل طبقة فرعية من المحول، بدلاً من تطبيع المخرجات. نستخدم دالة التطبيع RMSNorm، التي قدمها Zhang and Sennrich (2019).

**دالة تنشيط SwiGLU [PaLM].** نستبدل اللاخطية ReLU بدالة تنشيط SwiGLU، التي قدمها Shazeer (2020) لتحسين الأداء. نستخدم بُعداً قدره 2/3·4d بدلاً من 4d كما في PaLM.

**التضمينات الدوارة [GPTNeo].** نزيل التضمينات الموضعية المطلقة، وبدلاً من ذلك، نضيف التضمينات الموضعية الدوارة (RoPE)، التي قدمها Su et al. (2021)، في كل طبقة من طبقات الشبكة.

تُعطى تفاصيل المعاملات الفائقة لنماذجنا المختلفة في الجدول 2.

## 2.3 المحسِّن

يتم تدريب نماذجنا باستخدام محسِّن AdamW (Loshchilov and Hutter, 2017)، مع المعاملات الفائقة التالية: β₁ = 0.9، β₂ = 0.95. نستخدم جدول معدل تعلم جيبي، بحيث يكون معدل التعلم النهائي مساوياً لـ 10% من معدل التعلم الأقصى. نستخدم تناقص الوزن بمقدار 0.1 وقص التدرج بمقدار 1.0. نستخدم 2000 خطوة إحماء، ونُغيّر معدل التعلم وحجم الدفعة بحسب حجم النموذج (انظر الجدول 2 للتفاصيل).

## 2.4 التنفيذ الفعّال

نجري عدة تحسينات لتحسين سرعة تدريب نماذجنا. أولاً، نستخدم تنفيذاً فعّالاً للانتباه السببي متعدد الرؤوس لتقليل استخدام الذاكرة ووقت التشغيل. هذا التنفيذ، المتاح في مكتبة xformers، مستوحى من Rabe and Staats (2021) ويستخدم المرور العكسي من Dao et al. (2022). يتحقق ذلك بعدم تخزين أوزان الانتباه وعدم حساب نقاط المفتاح/الاستعلام المقنّعة بسبب الطبيعة السببية لمهمة نمذجة اللغة.

لتحسين كفاءة التدريب بشكل أكبر، قللنا كمية التنشيطات التي يتم إعادة حسابها أثناء المرور العكسي باستخدام نقاط التحقق. وبشكل أكثر تحديداً، نحفظ التنشيطات التي يكون حسابها مكلفاً، مثل مخرجات الطبقات الخطية. يتحقق ذلك من خلال تنفيذ دالة المرور العكسي يدوياً لطبقات المحول، بدلاً من الاعتماد على التفاضل التلقائي في PyTorch. للاستفادة الكاملة من هذا التحسين، نحتاج إلى تقليل استخدام الذاكرة للنموذج باستخدام نماذج ومتوازيات متسلسلة، كما هو موضح في Korthikanti et al. (2022). علاوة على ذلك، نتداخل أيضاً حساب التنشيطات والاتصال بين وحدات معالجة الرسومات عبر الشبكة (بسبب عمليات all_reduce) قدر الإمكان.

عند تدريب نموذج بـ 65B معامل، يعالج رمزنا حوالي 380 رمزاً/ثانية/GPU على 2048 وحدة معالجة رسومية A100 بسعة 80 جيجابايت من ذاكرة الوصول العشوائي. هذا يعني أن التدريب على مجموعة بياناتنا التي تحتوي على 1.4T رمز يستغرق حوالي 21 يوماً.

---

### Translation Notes

- **Tables referenced:** Table 1 (pre-training data), Table 2 (model architectures and hyperparameters)
- **Figures referenced:** Figure 1 (training loss curves)
- **Key terms introduced:** byte-pair encoding (BPE), SentencePiece, RMSNorm, SwiGLU, RoPE (Rotary Positional Embeddings), AdamW, cosine learning rate schedule, gradient clipping, xformers, checkpointing
- **Equations:** Mathematical notation for optimizer hyperparameters (β₁, β₂)
- **Special handling:**
  - Data percentages preserved in English notation
  - Language codes kept as-is (bg, ca, cs, etc.)
  - Library names (CCNet, fastText, SentencePiece, PyTorch, xformers) kept in original form
  - Model variants (GPT3, PaLM, GPTNeo) kept in original form

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.85
- **Overall section score:** 0.86
