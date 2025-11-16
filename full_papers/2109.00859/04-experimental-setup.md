# Section 4: Experimental Setup
## القسم 4: الإعداد التجريبي

**Section:** experimental setup
**Translation Quality:** 0.87
**Glossary Terms Used:** التدريب المسبق, مجموعة بيانات, ترميز, ترميز زوج البايت, المفردات, معيار, تلخيص الشفرة, توليد الشفرة, ترجمة الشفرة, تحسين الشفرة, كشف العيوب, كشف الاستنساخ, BLEU, دقة المطابقة التامة, مشفر, فك التشفير

---

### English Version

**4 Experimental Setup**

**4.1 Pre-training Dataset**

We follow Feng et al. (2020) to employ CodeSearchNet (Husain et al., 2019) to pre-train CodeT5, which consists of six PLs with both unimodal and bimodal data. Apart from that, we additionally collect two datasets of C/CSharp from BigQuery to ensure that all downstream tasks have overlapped PLs with the pre-training data. In total, we employ around 8.35 million instances for pre-training. Table 1 shows some basic statistics. To obtain the identifier labels from code, we leverage the tree-sitter to convert the PL into an abstract syntax tree and then extract its node type information. We filter out reserved keywords for each PL from its identifier list. We observe that PLs have different identifier rates, where Go has the least rate of 19% and Ruby has the highest rate of 32%.

**Table 1: Dataset statistics. "Identifier" denotes the proportion of identifiers over all code tokens for each PL.**

| PLs | W/ NL | W/o NL | Identifier |
|-----|-------|---------|------------|
| CodeSearchNet: Ruby | 49,009 | 110,551 | 32.08% |
| JavaScript | 125,166 | 1,717,933 | 19.82% |
| Go | 319,132 | 379,103 | 19.32% |
| Python | 453,772 | 657,030 | 30.02% |
| Java | 457,381 | 1,070,271 | 25.76% |
| PHP | 525,357 | 398,058 | 23.44% |
| Our: C | 1M | - | 24.94% |
| CSharp | 228,496 | 856,375 | 27.85% |
| **Total** | **3,158,313** | **5,189,321** | **8,347,634** |

**4.2 Code-specific Tokenizer**

Tokenization is a key ingredient for the success of pre-trained language models like BERT and GPT. They often employ a Byte-Pair Encoding (BPE) tokenizer (Sennrich et al., 2016) to alleviate the Out-of-Vocabulary (OoV) issues. Specifically, we train a Byte-level BPE tokenizer following Radford et al. (2019) and set the vocabulary size to 32,000 as T5. We add additional special tokens ([PAD], [CLS], [SEP], [MASK0], ..., [MASK99]). This tokenizer is trained on all of our pre-training data with non-printable characters and low-frequent tokens (occurring <3 times) filtered. We compare it with T5's default tokenizer and find that our tokenizer largely reduces the length of tokenized code sequence by 30%-45% on downstream tasks. This will accelerate the training and especially benefit generation tasks due to the shorter sequence to predict. We also spot a severe problem for applying the T5's default tokenizer on source code, where it would encode some common code tokens such as brackets ['{', '}'] into unknown tokens.

**4.3 Downstream Tasks and Metrics**

We cover most generation and understanding tasks in the CodeXGLUE benchmark (Lu et al., 2021) and employ the provided public datasets and the same data splits following it for all these tasks.

We first consider two cross-modal generation tasks. **Code summarization** aims to summarize a function-level code snippet into English descriptions. The dataset consists of six PLs including Ruby, JavaScript, Go, Python, Java, and PHP from CodeSearchNet (Husain et al., 2019). We employ the smoothed BLEU-4 (Lin and Och, 2004) to evaluate this task. **Code generation** is the task to generate a code snippet based on NL descriptions. We employ the Concode data (Iyer et al., 2018) in Java where the input contains both NL texts and class environment contexts, and the output is a function. We evaluate it with BLEU-4, exact match (EM) accuracy, and CodeBLEU (Ren et al., 2020) that considers syntactic and semantic matches based on the code structure in addition to the n-gram match.

Besides, we consider two code-to-code generation tasks. **Code translation** aims to migrate legacy software from one PL to another, where we focus on translating functions from Java to CSharp and vice versa. **Code refinement** aims to convert a buggy function into a correct one. We employ two Java datasets provided by Tufano et al. (2019) with various function lengths: small (fewer than 50 tokens) and medium (50-100 tokens). We use BLEU-4 and exact match to evaluate them.

We also investigate how CodeT5 performs on two understanding-based tasks. The first one is **defect detection** that aims to predict whether a code is vulnerable to software systems or not. We use the C dataset provided by Zhou et al. (2019) for experiment. The second task is **clone detection** which aims to measure the similarity between two code snippets and predict whether they have the same functionality. We experiment with the Java data provided by Wang et al. (2020). We employ F1 score and accuracy for evaluating these two tasks respectively. In total, our CodeT5 supports six tasks and fourteen sub-tasks in CodeXGLUE with a unified encoder-decoder model.

**4.4 Comparison Models**

We compare CodeT5 with state-of-the-art (SOTA) pre-trained models that can be categorized into three types: encoder-only, decoder-only, and encoder-decoder models. As encoder-only models, we consider RoBERTa (Liu et al., 2019b), RoBERTa (code) trained with masked language modeling (MLM) on code, CodeBERT (Feng et al., 2020) trained with both MLM and replaced token detection (Clark et al., 2020), GraphCodeBERT (Guo et al., 2021) using data flow from code, and DOBF (Rozière et al., 2021) trained with the identifier deobfuscation objective. Note that although DOBF employs a Seq2Seq model during pre-training, it only aims to train a better encoder for downstream tasks without exploring the potential benefit of the pre-trained decoder.

For decoder-only models, we compare GPT-2 (Radford et al., 2019) and its adaptations on code domain including CodeGPT-2, and CodeGPT-adapted. The difference is that the latter one utilizes a GPT-2 checkpoint for model initialization while the former one is trained from scratch. As encoder-decoder models, the current SOTA model for the CodeXGLUE benchmark is PLBART (Ahmad et al., 2021) based on BART (Lewis et al., 2020) architecture. For pre-training data, most of these models employ CodeSearchNet (Husain et al., 2019) except DOBF and PLBART. DOBF is pre-trained on 7.9M Java and 3.6M Python files from BigQuery while PLBART employs a much larger data with 470M Python and 210M Java functions, and 47M NL posts from StackOverflow.

**4.5 Model Configurations**

We build CodeT5 based on Huggingface's T5 (Raffel et al., 2020) PyTorch implementation and employ two sizes of CodeT5-small (60M) and CodeT5-base (220M). We set the maximum source and target sequence lengths to be 512 and 256, respectively. We use the mixed precision of FP16 to accelerate the pre-training. We set the batch size to 1024 and employ the peak learning rate of 2e-4 with linear decay. We pre-train the model with the denoising objective for 100 epochs and bimodal dual training for further 50 epochs on a cluster of 16 NVIDIA A100 GPUs with 40G memory. The total training time for CodeT5-small and CodeT5-base is 5 and 12 days, respectively.

In the fine-tuning phase, we find that the tasks in CodeXGLUE (Lu et al., 2021) are quite sensitive to some hyper parameters such as learning rate, training steps, and batch size. We conduct a grid search and select the best parameters based on the validation set. In multi-task learning, we cover all downstream tasks except clone detection.

---

### النسخة العربية

**4 الإعداد التجريبي**

**4.1 مجموعة بيانات التدريب المسبق**

نتبع Feng et al. (2020) لاستخدام CodeSearchNet (Husain et al., 2019) للتدريب المسبق لـ CodeT5، والذي يتكون من ست لغات برمجة مع بيانات أحادية الوضع وثنائية الوضع. بالإضافة إلى ذلك، نجمع مجموعتي بيانات إضافيتين من C/CSharp من BigQuery لضمان أن جميع المهام اللاحقة لديها لغات برمجة متداخلة مع بيانات التدريب المسبق. في المجموع، نستخدم حوالي 8.35 مليون حالة للتدريب المسبق. يُظهر الجدول 1 بعض الإحصائيات الأساسية. للحصول على تسميات المعرفات من الشفرة، نستفيد من tree-sitter لتحويل لغة البرمجة إلى شجرة بنية تركيبية مجردة ثم نستخرج معلومات نوع العقدة الخاصة بها. نقوم بتصفية الكلمات المفتاحية المحجوزة لكل لغة برمجة من قائمة المعرفات الخاصة بها. نلاحظ أن لغات البرمجة لها معدلات معرفات مختلفة، حيث تمتلك Go أقل معدل بنسبة 19٪ و Ruby لديها أعلى معدل بنسبة 32٪.

**الجدول 1: إحصائيات مجموعة البيانات. يشير "المعرف" إلى نسبة المعرفات على جميع رموز الشفرة لكل لغة برمجة.**

| لغات البرمجة | مع لغة طبيعية | بدون لغة طبيعية | المعرف |
|-----|-------|---------|------------|
| CodeSearchNet: Ruby | 49,009 | 110,551 | 32.08% |
| JavaScript | 125,166 | 1,717,933 | 19.82% |
| Go | 319,132 | 379,103 | 19.32% |
| Python | 453,772 | 657,030 | 30.02% |
| Java | 457,381 | 1,070,271 | 25.76% |
| PHP | 525,357 | 398,058 | 23.44% |
| لدينا: C | 1M | - | 24.94% |
| CSharp | 228,496 | 856,375 | 27.85% |
| **المجموع** | **3,158,313** | **5,189,321** | **8,347,634** |

**4.2 مرمّز خاص بالشفرة**

يعد الترميز عنصراً أساسياً لنجاح النماذج اللغوية المُدربة مسبقاً مثل BERT و GPT. غالباً ما تستخدم مرمّز ترميز زوج البايت (BPE) (Sennrich et al., 2016) لتخفيف مشاكل خارج المفردات (OoV). على وجه التحديد، ندرب مرمّز BPE على مستوى البايت متبعين Radford et al. (2019) ونضع حجم المفردات إلى 32,000 كـ T5. نضيف رموزاً خاصة إضافية ([PAD]، [CLS]، [SEP]، [MASK0]، ...، [MASK99]). يتم تدريب هذا المرمّز على جميع بيانات التدريب المسبق الخاصة بنا مع تصفية الأحرف غير القابلة للطباعة والرموز منخفضة التكرار (التي تحدث <3 مرات). نقارنه مع مرمّز T5 الافتراضي ونجد أن مرمّزنا يقلل إلى حد كبير طول تسلسل الشفرة المرمّز بنسبة 30٪-45٪ في المهام اللاحقة. سيؤدي هذا إلى تسريع التدريب ويفيد بشكل خاص مهام التوليد بسبب التسلسل الأقصر للتنبؤ به. نكتشف أيضاً مشكلة خطيرة في تطبيق مرمّز T5 الافتراضي على الشفرة المصدرية، حيث سيُرمّز بعض رموز الشفرة الشائعة مثل الأقواس ['{', '}'] إلى رموز غير معروفة.

**4.3 المهام اللاحقة والمقاييس**

نغطي معظم مهام التوليد والفهم في معيار CodeXGLUE (Lu et al., 2021) ونستخدم مجموعات البيانات العامة المقدمة ونفس تقسيمات البيانات متبعينه لجميع هذه المهام.

نأخذ في الاعتبار أولاً مهمتي توليد عبر الأنماط. يهدف **تلخيص الشفرة** إلى تلخيص مقتطف شفرة على مستوى الدالة إلى أوصاف إنجليزية. تتكون مجموعة البيانات من ست لغات برمجة بما في ذلك Ruby و JavaScript و Go و Python و Java و PHP من CodeSearchNet (Husain et al., 2019). نستخدم BLEU-4 الناعم (Lin and Och, 2004) لتقييم هذه المهمة. **توليد الشفرة** هي المهمة لتوليد مقتطف شفرة بناءً على أوصاف اللغة الطبيعية. نستخدم بيانات Concode (Iyer et al., 2018) في Java حيث يحتوي الإدخال على نصوص اللغة الطبيعية وسياقات بيئة الفئة، والمخرج هو دالة. نقيّمها باستخدام BLEU-4 ودقة المطابقة التامة (EM) و CodeBLEU (Ren et al., 2020) الذي يأخذ في الاعتبار المطابقات النحوية والدلالية بناءً على بنية الشفرة بالإضافة إلى مطابقة n-gram.

بالإضافة إلى ذلك، نأخذ في الاعتبار مهمتي توليد من شفرة إلى شفرة. تهدف **ترجمة الشفرة** إلى ترحيل البرمجيات القديمة من لغة برمجة واحدة إلى أخرى، حيث نركز على ترجمة الدوال من Java إلى CSharp والعكس. يهدف **تحسين الشفرة** إلى تحويل دالة بها أخطاء إلى دالة صحيحة. نستخدم مجموعتي بيانات Java المقدمتين من Tufano et al. (2019) بأطوال دوال مختلفة: صغيرة (أقل من 50 رمزاً) ومتوسطة (50-100 رمز). نستخدم BLEU-4 والمطابقة التامة لتقييمها.

نستكشف أيضاً كيف يؤدي CodeT5 في مهمتين قائمتين على الفهم. الأولى هي **كشف العيوب** التي تهدف إلى التنبؤ بما إذا كانت الشفرة عرضة لأنظمة البرمجيات أم لا. نستخدم مجموعة بيانات C المقدمة من Zhou et al. (2019) للتجربة. المهمة الثانية هي **كشف الاستنساخ** التي تهدف إلى قياس التشابه بين مقتطفي شفرة والتنبؤ بما إذا كان لهما نفس الوظيفة. نجرب بيانات Java المقدمة من Wang et al. (2020). نستخدم درجة F1 والدقة لتقييم هاتين المهمتين على التوالي. في المجموع، يدعم CodeT5 الخاص بنا ست مهام وأربع عشرة مهمة فرعية في CodeXGLUE بنموذج مشفر-فك تشفير موحد.

**4.4 نماذج المقارنة**

نقارن CodeT5 مع نماذج متقدمة (SOTA) مُدربة مسبقاً يمكن تصنيفها إلى ثلاثة أنواع: نماذج بمشفر فقط، ونماذج بفك تشفير فقط، ونماذج مشفر-فك تشفير. كنماذج بمشفر فقط، نأخذ في الاعتبار RoBERTa (Liu et al., 2019b)، RoBERTa (شفرة) المُدرب بنمذجة لغة مقنعة (MLM) على الشفرة، CodeBERT (Feng et al., 2020) المُدرب بكل من MLM وكشف الرموز المستبدلة (Clark et al., 2020)، GraphCodeBERT (Guo et al., 2021) الذي يستخدم تدفق البيانات من الشفرة، و DOBF (Rozière et al., 2021) المُدرب بهدف إزالة تعتيم المعرفات. لاحظ أنه على الرغم من أن DOBF يستخدم نموذج تسلسل إلى تسلسل أثناء التدريب المسبق، إلا أنه يهدف فقط إلى تدريب مشفر أفضل للمهام اللاحقة دون استكشاف الفائدة المحتملة لفك التشفير المُدرب مسبقاً.

بالنسبة لنماذج فك التشفير فقط، نقارن GPT-2 (Radford et al., 2019) وتكييفاته على مجال الشفرة بما في ذلك CodeGPT-2 و CodeGPT-adapted. الفرق هو أن الأخير يستخدم نقطة تحقق GPT-2 لتهيئة النموذج بينما الأول يتم تدريبه من الصفر. كنماذج مشفر-فك تشفير، النموذج المتقدم الحالي لمعيار CodeXGLUE هو PLBART (Ahmad et al., 2021) المبني على معمارية BART (Lewis et al., 2020). بالنسبة لبيانات التدريب المسبق، تستخدم معظم هذه النماذج CodeSearchNet (Husain et al., 2019) باستثناء DOBF و PLBART. يتم تدريب DOBF مسبقاً على 7.9 مليون ملف Java و 3.6 مليون ملف Python من BigQuery بينما يستخدم PLBART بيانات أكبر بكثير مع 470 مليون دالة Python و 210 مليون دالة Java، و 47 مليون منشور باللغة الطبيعية من StackOverflow.

**4.5 تكوينات النموذج**

نبني CodeT5 بناءً على تنفيذ PyTorch من Huggingface لـ T5 (Raffel et al., 2020) ونستخدم حجمين من CodeT5-small (60M) و CodeT5-base (220M). نضع أقصى أطوال تسلسل المصدر والهدف إلى 512 و 256 على التوالي. نستخدم الدقة المختلطة FP16 لتسريع التدريب المسبق. نضع حجم الدفعة إلى 1024 ونستخدم معدل التعلم الأقصى 2e-4 مع انخفاض خطي. ندرب النموذج مسبقاً بهدف إزالة التشويش لـ 100 حقبة والتدريب المزدوج ثنائي الوضع لـ 50 حقبة إضافية على مجموعة من 16 وحدة معالجة رسومات NVIDIA A100 بذاكرة 40 جيجابايت. إجمالي وقت التدريب لـ CodeT5-small و CodeT5-base هو 5 و 12 يوماً على التوالي.

في مرحلة الضبط الدقيق، نجد أن المهام في CodeXGLUE (Lu et al., 2021) حساسة جداً لبعض المعاملات الفائقة مثل معدل التعلم وخطوات التدريب وحجم الدفعة. نجري بحثاً شبكياً ونختار أفضل المعاملات بناءً على مجموعة التحقق. في التعلم متعدد المهام، نغطي جميع المهام اللاحقة باستثناء كشف الاستنساخ.

---

### Translation Notes

- **Figures referenced:** None
- **Tables referenced:** Table 1 (dataset statistics)
- **Key terms introduced:** ترميز زوج البايت (Byte-Pair Encoding - BPE), خارج المفردات (Out-of-Vocabulary - OoV), تلخيص الشفرة (code summarization), توليد الشفرة (code generation), ترجمة الشفرة (code translation), تحسين الشفرة (code refinement), كشف العيوب (defect detection), كشف الاستنساخ (clone detection), BLEU-4, دقة المطابقة التامة (exact match - EM), CodeBLEU, درجة F1 (F1 score)
- **Equations:** 0
- **Citations:** 15 references cited (Feng 2020, Husain 2019, Sennrich 2016, Radford 2019, Lu 2021, Lin 2004, Och 2004, Iyer 2018, Ren 2020, Tufano 2019, Zhou 2019, Wang 2020, Liu 2019b, Clark 2020, Guo 2021, Rozière 2021, Ahmad 2021, Lewis 2020, Raffel 2020)
- **Special handling:**
  - Preserved dataset names (CodeSearchNet, CodeXGLUE, Concode) in English
  - Preserved model names (RoBERTa, CodeBERT, GraphCodeBERT, DOBF, GPT-2, PLBART) in English
  - Preserved special tokens ([PAD], [CLS], [SEP], [MASK0-99]) in English
  - Maintained table structure with bilingual headers

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
