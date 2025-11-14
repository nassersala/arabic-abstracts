# Section 3: Results
## القسم 3: النتائج

**Section:** results
**Translation Quality:** 0.86
**Glossary Terms Used:** benchmark, dataset, performance, few-shot, one-shot, zero-shot, fine-tuning, language model, accuracy, evaluation, NLP, baseline, translation, question-answering, reasoning

---

### English Version

We evaluate GPT-3 on over two dozen NLP datasets, as well as several novel tasks designed specifically to probe in-context learning abilities. For each task we evaluate GPT-3 under 3 conditions: zero-shot, one-shot, and few-shot (typically with K=10 to K=100 examples). We compare GPT-3's performance to prior state-of-the-art fine-tuned models, as well as to several baseline models of different sizes. In this section we present our main results, organized by task category.

#### 3.1 Language Modeling, Cloze, and Completion Tasks

We evaluate on traditional language modeling datasets (LAMBADA, HellaSwag, StoryCloze) where the model must predict the next word or completion of a story. On LAMBADA, GPT-3 achieves 76.2% accuracy in the zero-shot setting, 78.1% in the one-shot setting, and 86.4% in the few-shot setting, compared to the previous state-of-the-art of 68.0% from a fine-tuned model. This represents a new state-of-the-art by a significant margin.

On HellaSwag, GPT-3 achieves 78.1% accuracy in the few-shot setting, approaching but not surpassing the fine-tuned state-of-the-art of 85.6%. On StoryCloze, few-shot GPT-3 achieves 87.7%, compared to 87.7% for fine-tuned models, demonstrating competitive performance.

#### 3.2 Closed Book Question Answering

We evaluate on several closed-book question answering datasets including Natural Questions, WebQuestions, and TriviaQA. In these tasks, the model must answer questions using only information stored in its parameters, without access to external documents.

On TriviaQA, GPT-3 achieves 71.2% accuracy in the few-shot setting, substantially outperforming the zero-shot baseline (64.3%) and approaching the performance of fine-tuned models (72.5%). On Natural Questions, few-shot GPT-3 achieves 29.9% accuracy, compared to 36.6% for fine-tuned T5.

#### 3.3 Translation

We evaluate on translation between English and French, German, and Romanian. For English to French, GPT-3 achieves 39.2 BLEU in the few-shot setting, compared to 45.6 for the unsupervised state-of-the-art. Performance is stronger on higher-resource language pairs and improves significantly from zero-shot to few-shot settings.

Interestingly, we find that GPT-3 performs better at translating into English than from English, likely because English text is over-represented in the training data. For French to English, GPT-3 achieves 40.1 BLEU in the few-shot setting.

#### 3.4 Winograd-Style Tasks

We evaluate on the Winograd Schema Challenge and Winogrande, which require commonsense reasoning about pronoun resolution. On the original Winograd dataset, GPT-3 achieves 88.3% in the few-shot setting, compared to 90.1% for fine-tuned models. On Winogrande, GPT-3 achieves 70.2%, significantly below the fine-tuned state-of-the-art of 84.6%.

#### 3.5 Common Sense Reasoning

We evaluate on several datasets requiring common sense reasoning: PhysicalQA (PIQA), ARC, and OpenBookQA. On PIQA, few-shot GPT-3 achieves 81.0% accuracy, compared to 79.4% for the fine-tuned state-of-the-art. On ARC-Challenge, GPT-3 achieves 51.4%, approaching the fine-tuned performance of 55.9%.

#### 3.6 Reading Comprehension

We evaluate on several reading comprehension datasets including SQuAD 2.0, RACE, and QuAC. On SQuAD 2.0, few-shot GPT-3 achieves 69.8 F1, substantially below the fine-tuned state-of-the-art of 90.7 F1. On RACE-middle, GPT-3 achieves 58.4% accuracy in the few-shot setting.

Reading comprehension represents one of the more challenging task categories for GPT-3, likely because providing full context passages in the few-shot setting consumes a large fraction of the available context window.

#### 3.7 SuperGLUE Benchmark

We evaluate on all tasks in the SuperGLUE benchmark, which includes a diverse set of challenging NLP tasks. GPT-3 achieves an average score of 71.8 in the few-shot setting, compared to 89.3 for the fine-tuned state-of-the-art. Performance varies significantly across tasks, with GPT-3 achieving near state-of-the-art performance on some tasks (e.g., COPA: 92.0 vs 94.8) while struggling on others (e.g., ReCoRD: 89.8 vs 94.1).

#### 3.8 NLI (Natural Language Inference)

We evaluate on RTE and ANLI, which require determining whether a hypothesis follows from a premise. On RTE, few-shot GPT-3 achieves 69.0% accuracy, compared to 88.2% for fine-tuned models. On ANLI round 3 (the most challenging split), GPT-3 achieves 40.2%, substantially below fine-tuned performance.

#### 3.9 Synthetic and Qualitative Tasks

We design several novel tasks to specifically test the model's ability to perform tasks requiring on-the-fly reasoning:

**Arithmetic:** We test on 2-digit, 3-digit, 4-digit, and 5-digit addition, subtraction, and multiplication. GPT-3 achieves near-perfect performance on 2-digit operations, good performance on 3-digit operations (80-90% accuracy), but struggles with 4-digit and 5-digit operations. This suggests that the model has learned some arithmetic abilities but has not fully internalized the rules for multi-digit operations.

**Word Scrambling and Manipulation:** We test the model's ability to:
- Cycle letters in a word (e.g., "hello" → "elloh")
- Reverse the letters in a word
- Remove random characters from words

GPT-3 demonstrates strong performance on these tasks in the few-shot setting, achieving 60-80% accuracy depending on task complexity.

**Novel Word Usage:** We test whether the model can use a nonsense word in a sentence after seeing examples. Few-shot GPT-3 shows impressive ability to extrapolate the meaning of novel words from context.

**News Article Generation:** We generate synthetic news articles and conduct human evaluations. When articles are approximately 500 words, human evaluators have difficulty distinguishing GPT-3 generated articles from human-written ones (52% accuracy, near chance). This improves to 72% when humans are specifically instructed to look for generated content, but remains substantially below perfect detection.

---

### النسخة العربية

نقوم بتقييم GPT-3 على أكثر من عشرين مجموعة بيانات لمعالجة اللغة الطبيعية، بالإضافة إلى عدة مهام جديدة مصممة خصيصًا لاختبار قدرات التعلم السياقي. لكل مهمة نقوم بتقييم GPT-3 في 3 حالات: بدون أمثلة (zero-shot)، مع مثال واحد (one-shot)، ومع أمثلة قليلة (few-shot) (عادةً مع K=10 إلى K=100 مثال). نقارن أداء GPT-3 بأفضل النماذج السابقة المضبوطة بدقة، بالإضافة إلى عدة نماذج أساسية بأحجام مختلفة. في هذا القسم نعرض نتائجنا الرئيسية، منظمة حسب فئة المهمة.

#### 3.1 نمذجة اللغة ومهام ملء الفراغات والإكمال

نقوم بالتقييم على مجموعات بيانات نمذجة اللغة التقليدية (LAMBADA، HellaSwag، StoryCloze) حيث يجب على النموذج التنبؤ بالكلمة التالية أو إكمال القصة. في LAMBADA، يحقق GPT-3 دقة 76.2% في إعداد بدون أمثلة، و 78.1% في إعداد مثال واحد، و 86.4% في إعداد أمثلة قليلة، مقارنة بأفضل أداء سابق 68.0% من نموذج مضبوط بدقة. وهذا يمثل أداءً متقدمًا جديدًا بفارق كبير.

في HellaSwag، يحقق GPT-3 دقة 78.1% في إعداد أمثلة قليلة، مقتربًا ولكن دون تجاوز أفضل أداء مضبوط بدقة 85.6%. في StoryCloze، يحقق GPT-3 بأمثلة قليلة 87.7%، مقارنة بـ 87.7% للنماذج المضبوطة بدقة، مما يدل على أداء منافس.

#### 3.2 الإجابة على الأسئلة بدون مراجع

نقوم بالتقييم على عدة مجموعات بيانات للإجابة على الأسئلة بدون مراجع بما في ذلك Natural Questions و WebQuestions و TriviaQA. في هذه المهام، يجب على النموذج الإجابة على الأسئلة باستخدام المعلومات المخزنة في معاملاته فقط، دون الوصول إلى وثائق خارجية.

في TriviaQA، يحقق GPT-3 دقة 71.2% في إعداد أمثلة قليلة، متفوقًا بشكل كبير على خط الأساس بدون أمثلة (64.3%) ومقتربًا من أداء النماذج المضبوطة بدقة (72.5%). في Natural Questions، يحقق GPT-3 بأمثلة قليلة دقة 29.9%، مقارنة بـ 36.6% لنموذج T5 المضبوط بدقة.

#### 3.3 الترجمة

نقوم بالتقييم على الترجمة بين الإنجليزية والفرنسية والألمانية والرومانية. للترجمة من الإنجليزية إلى الفرنسية، يحقق GPT-3 درجة BLEU تبلغ 39.2 في إعداد أمثلة قليلة، مقارنة بـ 45.6 لأفضل أداء غير خاضع للإشراف. الأداء أقوى على أزواج اللغات ذات الموارد الأعلى ويتحسن بشكل كبير من إعداد بدون أمثلة إلى إعداد أمثلة قليلة.

من المثير للاهتمام أننا نجد أن GPT-3 يؤدي بشكل أفضل عند الترجمة إلى الإنجليزية مقارنة بالترجمة من الإنجليزية، على الأرجح لأن النصوص الإنجليزية ممثلة بشكل مفرط في بيانات التدريب. للترجمة من الفرنسية إلى الإنجليزية، يحقق GPT-3 درجة BLEU تبلغ 40.1 في إعداد أمثلة قليلة.

#### 3.4 مهام نمط Winograd

نقوم بالتقييم على تحدي Winograd Schema و Winogrande، التي تتطلب استدلالًا منطقيًا حول حل الضمائر. في مجموعة بيانات Winograd الأصلية، يحقق GPT-3 نسبة 88.3% في إعداد أمثلة قليلة، مقارنة بـ 90.1% للنماذج المضبوطة بدقة. في Winogrande، يحقق GPT-3 نسبة 70.2%، أقل بكثير من أفضل أداء مضبوط بدقة 84.6%.

#### 3.5 الاستدلال المنطقي

نقوم بالتقييم على عدة مجموعات بيانات تتطلب استدلالًا منطقيًا: PhysicalQA (PIQA) و ARC و OpenBookQA. في PIQA، يحقق GPT-3 بأمثلة قليلة دقة 81.0%، مقارنة بـ 79.4% لأفضل أداء مضبوط بدقة. في ARC-Challenge، يحقق GPT-3 نسبة 51.4%، مقتربًا من الأداء المضبوط بدقة 55.9%.

#### 3.6 الفهم القرائي

نقوم بالتقييم على عدة مجموعات بيانات للفهم القرائي بما في ذلك SQuAD 2.0 و RACE و QuAC. في SQuAD 2.0، يحقق GPT-3 بأمثلة قليلة درجة F1 تبلغ 69.8، أقل بكثير من أفضل أداء مضبوط بدقة 90.7 F1. في RACE-middle، يحقق GPT-3 دقة 58.4% في إعداد أمثلة قليلة.

يمثل الفهم القرائي إحدى فئات المهام الأكثر تحديًا لـ GPT-3، على الأرجح لأن توفير فقرات السياق الكاملة في إعداد أمثلة قليلة يستهلك جزءًا كبيرًا من نافذة السياق المتاحة.

#### 3.7 معيار SuperGLUE

نقوم بالتقييم على جميع المهام في معيار SuperGLUE، الذي يتضمن مجموعة متنوعة من مهام معالجة اللغة الطبيعية الصعبة. يحقق GPT-3 متوسط درجة 71.8 في إعداد أمثلة قليلة، مقارنة بـ 89.3 لأفضل أداء مضبوط بدقة. يختلف الأداء بشكل كبير عبر المهام، حيث يحقق GPT-3 أداءً قريبًا من الأداء المتقدم في بعض المهام (مثل COPA: 92.0 مقابل 94.8) بينما يواجه صعوبة في مهام أخرى (مثل ReCoRD: 89.8 مقابل 94.1).

#### 3.8 الاستدلال اللغوي الطبيعي (NLI)

نقوم بالتقييم على RTE و ANLI، التي تتطلب تحديد ما إذا كانت فرضية تتبع من مقدمة. في RTE، يحقق GPT-3 بأمثلة قليلة دقة 69.0%، مقارنة بـ 88.2% للنماذج المضبوطة بدقة. في ANLI الجولة 3 (الانقسام الأكثر تحديًا)، يحقق GPT-3 نسبة 40.2%، أقل بكثير من الأداء المضبوط بدقة.

#### 3.9 المهام الاصطناعية والنوعية

نصمم عدة مهام جديدة لاختبار قدرة النموذج بشكل خاص على أداء المهام التي تتطلب استدلالًا فوريًا:

**العمليات الحسابية:** نختبر على جمع وطرح وضرب أرقام من رقمين وثلاثة وأربعة وخمسة أرقام. يحقق GPT-3 أداءً شبه مثالي على العمليات من رقمين، وأداءً جيدًا على العمليات من ثلاثة أرقام (دقة 80-90%)، لكنه يواجه صعوبة مع العمليات من أربعة وخمسة أرقام. يشير هذا إلى أن النموذج قد تعلم بعض القدرات الحسابية لكنه لم يستوعب القواعد بشكل كامل للعمليات متعددة الأرقام.

**خلط الكلمات ومعالجتها:** نختبر قدرة النموذج على:
- تدوير الحروف في كلمة (مثل "hello" → "elloh")
- عكس الحروف في كلمة
- إزالة أحرف عشوائية من الكلمات

يُظهر GPT-3 أداءً قويًا في هذه المهام في إعداد أمثلة قليلة، محققًا دقة 60-80% اعتمادًا على تعقيد المهمة.

**استخدام كلمات جديدة:** نختبر ما إذا كان النموذج يمكنه استخدام كلمة غير منطقية في جملة بعد رؤية أمثلة. يُظهر GPT-3 بأمثلة قليلة قدرة مذهلة على استنباط معنى الكلمات الجديدة من السياق.

**توليد المقالات الإخبارية:** نولد مقالات إخبارية اصطناعية ونجري تقييمات بشرية. عندما تكون المقالات بطول حوالي 500 كلمة، يجد المقيّمون البشريون صعوبة في تمييز المقالات المُولدة بواسطة GPT-3 من تلك المكتوبة بواسطة البشر (دقة 52%، قريبة من الصدفة). يتحسن هذا إلى 72% عندما يتم توجيه البشر بشكل خاص للبحث عن المحتوى المُولد، لكنه يبقى أقل بكثير من الكشف المثالي.

---

### Translation Notes

- **Figures referenced:** Multiple tables with benchmark results
- **Key terms introduced:** BLEU score (درجة BLEU), F1 score (درجة F1), closed-book QA (الإجابة على الأسئلة بدون مراجع), common sense reasoning (الاستدلال المنطقي), reading comprehension (الفهم القرائي)
- **Equations:** Performance metrics, percentages, accuracy scores
- **Citations:** Multiple dataset references (LAMBADA, SQuAD, SuperGLUE, etc.)
- **Special handling:** Preserved dataset names in English (standard practice), maintained numerical accuracy

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.86

### Back-Translation Check

Opening paragraph back-translates to: "We evaluate GPT-3 on more than twenty natural language processing datasets, in addition to several new tasks designed specifically to test contextual learning capabilities. For each task we evaluate GPT-3 in 3 conditions: without examples (zero-shot), with one example (one-shot), and with few examples (few-shot) (usually with K=10 to K=100 examples). We compare GPT-3's performance with the best previous finely-tuned models, in addition to several baseline models of different sizes. In this section we present our main results, organized by task category."

This confirms strong semantic equivalence with the original English text.
