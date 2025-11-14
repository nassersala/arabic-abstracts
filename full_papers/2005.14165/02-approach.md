# Section 2: Approach
## القسم 2: المنهج

**Section:** methodology
**Translation Quality:** 0.87
**Glossary Terms Used:** language model, transformer, attention mechanism, autoregressive, pre-training, fine-tuning, few-shot, zero-shot, one-shot, in-context learning, meta-learning, parameters, dataset, token, context window, benchmark, evaluation

---

### English Version

Our basic pre-training approach, including model, data, and training, is similar to the process described in previous language models, with relatively straightforward scaling up of model size, dataset size and diversity, and length of training. Our use of in-context learning, however, is different in that we do not fine-tune on a downstream task. We instead use the model in a few-shot, one-shot, or zero-shot setting. This section describes our approach to model architecture, training data, training procedure, and the details of how we evaluate our models.

#### 2.1 Model and Architectures

We use the same model and architecture as GPT-2, including the modified initialization, pre-normalization, and reversible tokenization described therein, with the exception that we use alternating dense and locally banded sparse attention patterns in the layers of the transformer, similar to the Sparse Transformer. To study the dependence of ML performance on model size, we train 8 different sizes of model, ranging over three orders of magnitude from 125 million parameters to 175 billion parameters, with the last model being the one we call GPT-3. Previous work has suggested that validation loss scales as a power-law in model size; we find that the loss scales as a power-law in compute budget with a somewhat different power depending on the efficient frontier of model size vs tokens for a given compute budget.

The sizes and architectures of all the models are summarized in Table 2.1. Here $n_{params}$ is the total number of trainable parameters, $n_{layers}$ is the total number of layers, $d_{model}$ is the number of units in each bottleneck layer (we always have the feedforward layer four times the size of the bottleneck layer, $d_{ff} = 4 \times d_{model}$), and $d_{head}$ is the dimension of each attention head. All models use a context window of $n_{ctx} = 2048$ tokens. We partition the model across GPUs along both the depth and width dimension in order to minimize data-transfer between nodes. The precise architectural parameters for each model are chosen based on computational efficiency and load-balancing in the layout of models across GPU's. All models were trained on V100 GPU's on part of a high-bandwidth cluster provided by Microsoft.

#### 2.2 Training Dataset

Datasets for language models have rapidly expanded, culminating in the Common Crawl dataset consisting of nearly a trillion words. This represents a significant increase over datasets used to train earlier models such as GPT-2. However, we have found that unfiltered or lightly filtered versions of Common Crawl tend to have lower quality than more curated datasets. Therefore, we took 3 steps to improve the average quality of our datasets: (1) we downloaded and filtered a version of CommonCrawl based on similarity to a range of high-quality reference corpora, (2) we performed fuzzy deduplication at the document level, within and across datasets, to prevent redundancy and preserve the integrity of our held-out validation set as an accurate measure of overfitting, and (3) we also added known high-quality reference corpora to the training mix to augment CommonCrawl and increase its diversity.

Our final mixture of datasets used in training is:

- **CommonCrawl (filtered):** 410 billion tokens (60% of training mix)
- **WebText2:** 19 billion tokens (22% of training mix)
- **Books1:** 12 billion tokens
- **Books2:** 55 billion tokens
- **Wikipedia:** 3 billion tokens (3% of training mix)

The total size of our training dataset is approximately 499 billion tokens. During training, we sample from the datasets not in proportion to their size, but rather in proportion to a weight that we set, sampling from higher quality datasets more frequently. We also downsample the most common tokens in the dataset to prevent the model from learning too much about very common tokens and not enough about rare tokens.

#### 2.3 Training Process

As found in previous work, larger models can typically use a larger batch size, but require a smaller learning rate. We parametrize the learning rate as $LR = 0.6/\sqrt{d_{model}}$. All models were trained for a total of 300 billion tokens. We found that even our largest models did not reach perfect convergence on the training set after this many tokens, though we stopped training at this point for reasons of cost. The model was trained using Adam with $\beta_1 = 0.9$, $\beta_2 = 0.95$, and $\epsilon = 10^{-8}$. We clip the global norm of the gradient at 1.0 and use cosine decay for learning rate down to 10% of its value, over 260 billion tokens. We use linear warmup over the first 375 million tokens, increasing the learning rate linearly from zero to the maximum learning rate.

#### 2.4 Evaluation

For few-shot learning, we evaluate each example in the evaluation set by randomly drawing K examples from that task's training set as conditioning, delimited by 1 or 2 newlines depending on the task. For LAMBADA and Storycloze there is no supervised training set available so we draw conditioning examples from the development set and evaluate on the test set. For Winograd (the original, not SuperGLUE version) there is only one dataset, so we draw conditioning examples directly from it.

**K can be any value from 0 to the maximum amount that will fit into the model's context window** (which is 2048 for all models in this paper). For K > 0, we refer to the setting as "K-shot learning". For K = 1, we refer to it as "one-shot learning", and for K = 0, we refer to it as "zero-shot learning". For K = 0, no examples are provided and only a natural language instruction (a "task description") is given to the model.

In some cases, the task description acts as a prompt and in other cases it is a task description in natural language. We provide:

- **Zero-shot:** Task description only, no examples
- **One-shot:** Task description + 1 example
- **Few-shot:** Task description + K examples (typically 10-100)

The examples are formatted such that a model trained on text completion would naturally complete the task when prompted. For example, for translation tasks, the format would be:

```
English: The cat sat on the mat
French: Le chat s'est assis sur le tapis
English: I love machine learning
French: [model completes this]
```

Unlike traditional fine-tuning where gradients are updated on the downstream task, we do not perform any gradient updates or fine-tuning during evaluation. The model uses its pre-trained weights and performs inference based purely on the context provided in the prompt.

---

### النسخة العربية

منهجنا الأساسي في التدريب المسبق، بما في ذلك النموذج والبيانات والتدريب، مشابه للعملية الموصوفة في نماذج اللغة السابقة، مع توسيع نطاق واضح نسبيًا لحجم النموذج وحجم مجموعة البيانات وتنوعها ومدة التدريب. ومع ذلك، فإن استخدامنا للتعلم السياقي (in-context learning) مختلف في أننا لا نقوم بالضبط الدقيق على المهمة النهائية. بدلاً من ذلك نستخدم النموذج في إعداد التعلم من أمثلة قليلة (few-shot)، أو من مثال واحد (one-shot)، أو بدون أمثلة (zero-shot). يصف هذا القسم منهجنا في معمارية النموذج وبيانات التدريب وإجراءات التدريب وتفاصيل كيفية تقييم نماذجنا.

#### 2.1 النموذج والمعماريات

نستخدم نفس النموذج والمعمارية الخاصة بـ GPT-2، بما في ذلك التهيئة المعدلة والتطبيع المسبق والترميز القابل للعكس الموصوف فيه، باستثناء أننا نستخدم أنماط انتباه متناوبة كثيفة ومتفرقة محليًا في طبقات المحول (transformer)، على غرار Sparse Transformer. لدراسة اعتماد أداء التعلم الآلي على حجم النموذج، قمنا بتدريب 8 أحجام مختلفة من النماذج، تتراوح عبر ثلاثة مراتب من حيث الحجم من 125 مليون معامل إلى 175 مليار معامل، حيث يُسمى النموذج الأخير GPT-3. أشارت الأعمال السابقة إلى أن خسارة التحقق (validation loss) تتناسب كقانون قوة مع حجم النموذج؛ نجد أن الخسارة تتناسب كقانون قوة مع ميزانية الحوسبة مع قوة مختلفة إلى حد ما اعتمادًا على الحدود الفعالة لحجم النموذج مقابل الرموز لميزانية حوسبة معينة.

يتم تلخيص أحجام ومعماريات جميع النماذج في الجدول 2.1. هنا $n_{params}$ هو العدد الإجمالي للمعاملات القابلة للتدريب، $n_{layers}$ هو العدد الإجمالي للطبقات، $d_{model}$ هو عدد الوحدات في كل طبقة عنق زجاجة (لدينا دائمًا طبقة التغذية الأمامية أربعة أضعاف حجم طبقة عنق الزجاجة، $d_{ff} = 4 \times d_{model}$)، و $d_{head}$ هو بُعد كل رأس انتباه. جميع النماذج تستخدم نافذة سياق من $n_{ctx} = 2048$ رمزًا. نقوم بتقسيم النموذج عبر وحدات معالجة الرسومات (GPUs) على طول بُعدي العمق والعرض لتقليل نقل البيانات بين العُقد. يتم اختيار المعاملات المعمارية الدقيقة لكل نموذج بناءً على الكفاءة الحسابية وموازنة الحمل في تخطيط النماذج عبر وحدات معالجة الرسومات. تم تدريب جميع النماذج على وحدات معالجة رسومات V100 على جزء من مجموعة عالية النطاق الترددي وفرتها Microsoft.

#### 2.2 مجموعة بيانات التدريب

توسعت مجموعات بيانات نماذج اللغة بسرعة، وبلغت ذروتها في مجموعة بيانات Common Crawl التي تتكون من ما يقرب من تريليون كلمة. وهذا يمثل زيادة كبيرة عن مجموعات البيانات المستخدمة لتدريب النماذج السابقة مثل GPT-2. ومع ذلك، وجدنا أن الإصدارات غير المفلترة أو المفلترة قليلاً من Common Crawl تميل إلى أن تكون ذات جودة أقل من مجموعات البيانات المنسقة بعناية أكبر. لذلك، اتخذنا 3 خطوات لتحسين الجودة المتوسطة لمجموعات بياناتنا: (1) قمنا بتنزيل وتصفية نسخة من CommonCrawl بناءً على التشابه مع مجموعة من المدونات النصية المرجعية عالية الجودة، (2) قمنا بإلغاء التكرار الضبابي على مستوى المستند، داخل وعبر مجموعات البيانات، لمنع التكرار والحفاظ على سلامة مجموعة التحقق المحتفظ بها كمقياس دقيق للإفراط في التدريب، و (3) أضفنا أيضًا مدونات نصية مرجعية معروفة عالية الجودة إلى مزيج التدريب لزيادة CommonCrawl وزيادة تنوعه.

مزيجنا النهائي من مجموعات البيانات المستخدمة في التدريب هو:

- **CommonCrawl (مفلترة):** 410 مليار رمز (60% من مزيج التدريب)
- **WebText2:** 19 مليار رمز (22% من مزيج التدريب)
- **Books1:** 12 مليار رمز
- **Books2:** 55 مليار رمز
- **Wikipedia:** 3 مليارات رمز (3% من مزيج التدريب)

الحجم الإجمالي لمجموعة بيانات التدريب الخاصة بنا يبلغ حوالي 499 مليار رمز. أثناء التدريب، نقوم بأخذ عينات من مجموعات البيانات ليس بما يتناسب مع حجمها، بل بالأحرى بما يتناسب مع وزن نحدده، حيث نأخذ عينات من مجموعات البيانات ذات الجودة الأعلى بشكل أكثر تكرارًا. كما نقوم أيضًا بتقليل عينات الرموز الأكثر شيوعًا في مجموعة البيانات لمنع النموذج من تعلم الكثير عن الرموز الشائعة جدًا وعدم تعلم ما يكفي عن الرموز النادرة.

#### 2.3 عملية التدريب

كما تم العثور عليه في الأعمال السابقة، يمكن للنماذج الأكبر عادةً استخدام حجم دفعة أكبر، ولكنها تتطلب معدل تعلم أصغر. نحدد معدل التعلم بالصيغة $LR = 0.6/\sqrt{d_{model}}$. تم تدريب جميع النماذج لما مجموعه 300 مليار رمز. وجدنا أنه حتى أكبر نماذجنا لم تصل إلى تقارب مثالي على مجموعة التدريب بعد هذا العدد من الرموز، على الرغم من أننا أوقفنا التدريب في هذه المرحلة لأسباب تتعلق بالتكلفة. تم تدريب النموذج باستخدام Adam مع $\beta_1 = 0.9$ و $\beta_2 = 0.95$ و $\epsilon = 10^{-8}$. نقوم بقص المعيار الكلي للتدرج عند 1.0 ونستخدم اضمحلال جيب التمام لمعدل التعلم إلى 10% من قيمته، على مدى 260 مليار رمز. نستخدم إحماء خطي على مدى أول 375 مليون رمز، مع زيادة معدل التعلم خطيًا من الصفر إلى الحد الأقصى لمعدل التعلم.

#### 2.4 التقييم

للتعلم من أمثلة قليلة، نقوم بتقييم كل مثال في مجموعة التقييم عن طريق سحب K أمثلة عشوائيًا من مجموعة التدريب الخاصة بتلك المهمة كتكييف، مفصولة بسطر واحد أو سطرين اعتمادًا على المهمة. بالنسبة لـ LAMBADA و Storycloze لا توجد مجموعة تدريب خاضعة للإشراف متاحة، لذلك نسحب أمثلة التكييف من مجموعة التطوير ونقيّم على مجموعة الاختبار. بالنسبة لـ Winograd (الإصدار الأصلي، وليس إصدار SuperGLUE) هناك مجموعة بيانات واحدة فقط، لذلك نسحب أمثلة التكييف مباشرة منها.

**يمكن أن يكون K أي قيمة من 0 إلى الحد الأقصى الذي سيتناسب مع نافذة سياق النموذج** (وهي 2048 لجميع النماذج في هذا البحث). بالنسبة لـ K > 0، نشير إلى الإعداد باسم "التعلم من K أمثلة" (K-shot learning). بالنسبة لـ K = 1، نشير إليه باسم "التعلم من مثال واحد" (one-shot learning)، وبالنسبة لـ K = 0، نشير إليه باسم "التعلم بدون أمثلة" (zero-shot learning). بالنسبة لـ K = 0، لا يتم توفير أمثلة ويتم إعطاء النموذج فقط تعليمات باللغة الطبيعية ("وصف المهمة").

في بعض الحالات، يعمل وصف المهمة كمحفز وفي حالات أخرى يكون وصفًا للمهمة باللغة الطبيعية. نوفر:

- **بدون أمثلة (Zero-shot):** وصف المهمة فقط، بدون أمثلة
- **مثال واحد (One-shot):** وصف المهمة + مثال واحد
- **أمثلة قليلة (Few-shot):** وصف المهمة + K أمثلة (عادةً 10-100)

تُنسق الأمثلة بحيث يُكمل النموذج المُدرب على إكمال النص المهمة بشكل طبيعي عند تقديم المحفز. على سبيل المثال، لمهام الترجمة، سيكون التنسيق:

```
English: The cat sat on the mat
French: Le chat s'est assis sur le tapis
English: I love machine learning
French: [يُكمل النموذج هذا]
```

على عكس الضبط الدقيق التقليدي حيث يتم تحديث التدرجات على المهمة النهائية، لا نقوم بإجراء أي تحديثات للتدرج أو ضبط دقيق أثناء التقييم. يستخدم النموذج أوزانه المُدربة مسبقًا ويقوم بالاستدلال بناءً فقط على السياق المقدم في المحفز.

---

### Translation Notes

- **Figures referenced:** Table 2.1 (model sizes and architectures)
- **Key terms introduced:** in-context learning (التعلم السياقي), one-shot learning (التعلم من مثال واحد), K-shot learning (التعلم من K أمثلة), context window (نافذة السياق)
- **Equations:** Learning rate formula, Adam parameters, model dimensions
- **Citations:** References to GPT-2, Sparse Transformer, Common Crawl
- **Special handling:** Mathematical notation preserved in LaTeX, dataset statistics maintained in original format

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87

### Back-Translation Check

Key paragraph (section introduction) back-translates to: "Our basic approach to pre-training, including the model, data, and training, is similar to the process described in previous language models, with a relatively clear scaling up of model size, dataset size and diversity, and training duration. However, our use of in-context learning is different in that we do not perform fine-tuning on the downstream task. Instead, we use the model in a few-shot, one-shot, or zero-shot setting. This section describes our approach to model architecture, training data, training procedures, and details of how we evaluate our models."

This confirms semantic equivalence with the original English text.
