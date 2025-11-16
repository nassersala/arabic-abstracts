# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** نماذج لغوية مُدربة مسبقاً, مشفر, فك التشفير, معالجة اللغة الطبيعية, التدريب المسبق, الضبط الدقيق, لغة البرمجة, المعرفات, تسلسل إلى تسلسل, محول, دلالات الشفرة, توليد الشفرة, فهم الشفرة, التعلم متعدد المهام

---

### English Version

**1 Introduction**

Pre-trained language models such as BERT (Devlin et al., 2019), GPT (Radford et al., 2019), and T5 (Raffel et al., 2020) have greatly boosted performance in a wide spectrum of natural language processing (NLP) tasks. They typically employ a pre-train then fine-tune paradigm that aims to derive generic language representations by self-supervised training on large-scale unlabeled data, which can be transferred to benefit multiple downstream tasks, especially those with limited data annotation. Inspired by their success, there are many recent attempts to adapt these pre-training methods for programming language (PL) (Svyatkovskiy et al., 2020; Kanade et al., 2020; Feng et al., 2020), showing promising results on code-related tasks.

However, despite their success, most of these models rely on either an encoder-only model similar to BERT (Svyatkovskiy et al., 2020; Feng et al., 2020) or a decoder-only model like GPT (Kanade et al., 2020), which is suboptimal for generation and understanding tasks, respectively. For example, CodeBERT (Feng et al., 2020) requires an additional decoder when applied for the code summarization task, where this decoder cannot benefit from the pre-training. Besides, most existing methods simply employ the conventional NLP pre-training techniques on source code by regarding it as a sequence of tokens like NL. This largely ignores the rich structural information in code, which is vital to fully comprehend the code semantics.

In this work, we present CodeT5, a pre-trained encoder-decoder model that considers the token type information in code. Our CodeT5 builds on the T5 architecture (Raffel et al., 2020) that employs denoising sequence-to-sequence (Seq2Seq) pre-training and has been shown to benefit both understanding and generation tasks in natural language. In addition, we propose to leverage the developer-assigned identifiers in code. When writing programs, developers tend to employ informative identifiers to make the code more understandable, so that these identifiers would generally preserve rich code semantics, e.g., the "binarySearch" identifier in Figure 2 directly indicates its functionality. To fuse such code-specific knowledge, we propose a novel identifier-aware objective that trains the model to distinguish which tokens are identifiers and recover them when they are masked.

Furthermore, we propose to leverage the code and its accompanying comments to learn a better NL-PL alignment. Developers often provide documentation for programs to facilitate better software maintenance (de Souza et al., 2005), so that such PL-NL pairs are widely available in most source code. Specifically, we regard the NL→PL generation and PL→NL generation as dual tasks and simultaneously optimize the model on them.

We pre-train CodeT5 on the CodeSearchNet data (Husain et al., 2019) following (Feng et al., 2020) that consists of both unimodal (PL-only) and bimodal (PL-NL) data on six PLs. In addition to that, we further collect extra data of C/C# from open-source Github repositories. We fine-tune CodeT5 on most tasks in the CodeXGLUE benchmark (Lu et al., 2021), including two understanding tasks: code defect detection and clone detection, and generation tasks such as code summarization, generation, translation, and refinement. As shown in Figure 1, we also explore multi-task learning to fine-tune CodeT5 on multiple tasks at a time using a task control code as the source prompt.

In summary, we make the following contributions:
• We present one of the first unified encoder-decoder models CodeT5 to support both code-related understanding and generation tasks, and also allows for multi-task learning.
• We propose a novel identifier-aware pre-training objective that considers the crucial token type information (identifiers) from code. Besides, we propose to leverage the NL-PL pairs that are naturally available in source code to learn a better cross-modal alignment.
• Extensive experiments show that CodeT5 yields state-of-the-art results on the fourteen sub-tasks in CodeXGLUE. Further analysis shows our CodeT5 can better capture the code semantics with the proposed identifier-aware pre-training and bimodal dual generation primarily benefits NL↔PL tasks.

---

### النسخة العربية

**1 المقدمة**

عززت النماذج اللغوية المُدربة مسبقاً مثل BERT (Devlin et al., 2019) و GPT (Radford et al., 2019) و T5 (Raffel et al., 2020) الأداء بشكل كبير في مجموعة واسعة من مهام معالجة اللغة الطبيعية (NLP). تستخدم هذه النماذج عادةً نموذج التدريب المسبق ثم الضبط الدقيق الذي يهدف إلى اشتقاق تمثيلات لغوية عامة من خلال التدريب ذاتي الإشراف على بيانات واسعة النطاق غير المُعنونة، والتي يمكن نقلها لإفادة مهام متعددة لاحقة، خاصة تلك ذات التعليق التوضيحي المحدود للبيانات. مستوحاة من نجاحها، هناك العديد من المحاولات الأخيرة لتكييف أساليب التدريب المسبق هذه للغة البرمجة (PL) (Svyatkovskiy et al., 2020; Kanade et al., 2020; Feng et al., 2020)، مما أظهر نتائج واعدة في المهام المتعلقة بالشفرة.

ومع ذلك، على الرغم من نجاحها، تعتمد معظم هذه النماذج إما على نموذج بمشفر فقط مشابه لـ BERT (Svyatkovskiy et al., 2020; Feng et al., 2020) أو نموذج بفك تشفير فقط مثل GPT (Kanade et al., 2020)، وهو دون المستوى الأمثل لمهام التوليد والفهم على التوالي. على سبيل المثال، يتطلب CodeBERT (Feng et al., 2020) فك تشفير إضافي عند تطبيقه على مهمة تلخيص الشفرة، حيث لا يمكن لفك التشفير هذا الاستفادة من التدريب المسبق. بالإضافة إلى ذلك، تستخدم معظم الأساليب الحالية ببساطة تقنيات التدريب المسبق التقليدية لمعالجة اللغة الطبيعية على الشفرة المصدرية من خلال اعتبارها تسلسلاً من الرموز مثل اللغة الطبيعية. هذا يتجاهل إلى حد كبير المعلومات البنيوية الغنية في الشفرة، والتي تعتبر حيوية لفهم دلالات الشفرة بالكامل.

في هذا العمل، نقدم CodeT5، وهو نموذج مشفر-فك تشفير مُدرب مسبقاً يأخذ في الاعتبار معلومات نوع الرمز في الشفرة. يبني CodeT5 الخاص بنا على معمارية T5 (Raffel et al., 2020) التي تستخدم التدريب المسبق لإزالة التشويش من تسلسل إلى تسلسل (Seq2Seq) وقد ثبت أنها تفيد كلاً من مهام الفهم والتوليد في اللغة الطبيعية. بالإضافة إلى ذلك، نقترح الاستفادة من المعرفات المُعينة من قبل المطور في الشفرة. عند كتابة البرامج، يميل المطورون إلى استخدام معرفات إعلامية لجعل الشفرة أكثر قابلية للفهم، بحيث تحفظ هذه المعرفات عمومًا دلالات شفرة غنية، على سبيل المثال، المعرف "binarySearch" في الشكل 2 يشير مباشرة إلى وظيفته. لدمج هذه المعرفة الخاصة بالشفرة، نقترح هدفاً جديداً مدركاً للمعرفات يدرب النموذج على تمييز الرموز التي هي معرفات واستعادتها عندما تكون مخفية.

علاوة على ذلك، نقترح الاستفادة من الشفرة والتعليقات المصاحبة لها لتعلم محاذاة أفضل بين اللغة الطبيعية ولغة البرمجة. غالباً ما يوفر المطورون توثيقاً للبرامج لتسهيل صيانة البرمجيات بشكل أفضل (de Souza et al., 2005)، بحيث تكون هذه الأزواج من لغة البرمجة واللغة الطبيعية متاحة على نطاق واسع في معظم الشفرات المصدرية. على وجه التحديد، نعتبر توليد اللغة الطبيعية→لغة البرمجة وتوليد لغة البرمجة→اللغة الطبيعية كمهام مزدوجة ونحسّن النموذج عليهما في وقت واحد.

ندرب CodeT5 مسبقاً على بيانات CodeSearchNet (Husain et al., 2019) متبعين (Feng et al., 2020) والتي تتكون من بيانات أحادية الوضع (لغة برمجة فقط) وثنائية الوضع (لغة برمجة-لغة طبيعية) على ست لغات برمجة. بالإضافة إلى ذلك، نجمع بيانات إضافية من C/C# من مستودعات Github مفتوحة المصدر. نضبط CodeT5 بدقة على معظم المهام في معيار CodeXGLUE (Lu et al., 2021)، بما في ذلك مهمتا فهم: كشف عيوب الشفرة وكشف الاستنساخ، ومهام التوليد مثل تلخيص الشفرة، والتوليد، والترجمة، والتحسين. كما هو موضح في الشكل 1، نستكشف أيضاً التعلم متعدد المهام لضبط CodeT5 بدقة على مهام متعددة في وقت واحد باستخدام رمز تحكم في المهمة كموجه مصدر.

باختصار، نقدم المساهمات التالية:
• نقدم أحد أوائل نماذج المشفر-فك التشفير الموحدة CodeT5 لدعم كل من مهام الفهم والتوليد المتعلقة بالشفرة، ويسمح أيضاً بالتعلم متعدد المهام.
• نقترح هدفاً جديداً للتدريب المسبق مدركاً للمعرفات يأخذ في الاعتبار معلومات نوع الرمز الحاسمة (المعرفات) من الشفرة. بالإضافة إلى ذلك، نقترح الاستفادة من أزواج اللغة الطبيعية-لغة البرمجة المتاحة بشكل طبيعي في الشفرة المصدرية لتعلم محاذاة أفضل عبر الأنماط.
• تُظهر التجارب الشاملة أن CodeT5 يحقق نتائج متقدمة في المهام الفرعية الأربع عشرة في CodeXGLUE. يُظهر التحليل الإضافي أن CodeT5 الخاص بنا يمكنه التقاط دلالات الشفرة بشكل أفضل مع التدريب المسبق المدرك للمعرفات المقترح والتوليد المزدوج ثنائي الوضع يفيد بشكل أساسي مهام اللغة الطبيعية↔لغة البرمجة.

---

### Translation Notes

- **Figures referenced:** Figure 1, Figure 2
- **Key terms introduced:** نماذج لغوية مُدربة مسبقاً (pre-trained language models), معرفات (identifiers), تسلسل إلى تسلسل (sequence-to-sequence), أحادي الوضع (unimodal), ثنائي الوضع (bimodal), محاذاة عبر الأنماط (cross-modal alignment)
- **Equations:** 0
- **Citations:** 12 references cited (Devlin 2019, Radford 2019, Raffel 2020, Svyatkovskiy 2020, Kanade 2020, Feng 2020, de Souza 2005, Husain 2019, Lu 2021)
- **Special handling:** Preserved model names (BERT, GPT, T5, CodeBERT, CodeT5) and dataset names (CodeSearchNet, CodeXGLUE) in English as per industry standard

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
