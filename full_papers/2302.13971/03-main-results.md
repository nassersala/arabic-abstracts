# Section 3: Main Results
## القسم 3: النتائج الرئيسية

**Section:** results/experiments
**Translation Quality:** 0.87
**Glossary Terms Used:** zero-shot, few-shot, benchmark, perplexity, exact match, pass@k, temperature, greedy decoding, majority voting

---

### English Version

Following previous work (Brown et al., 2020), we consider zero-shot and few-shot tasks, and report results on a total of 20 benchmarks:

• **Zero-shot.** We provide a textual description of the task and a test example. The model either provides an answer using open-ended generation, or ranks the proposed answers.

• **Few-shot.** We provide a few examples of the task (between 1 and 64) and a test example. The model takes this text as input and generates the answer or ranks different options.

We compare LLaMA with other foundation models, namely the non-publicly available language models GPT-3 (Brown et al., 2020), Gopher (Rae et al., 2021), Chinchilla (Hoffmann et al., 2022) and PaLM (Chowdhery et al., 2022), as well as the open-sourced OPT models (Zhang et al., 2022), GPT-J (Wang and Komatsuzaki, 2021), and GPTNeo (Black et al., 2022). In Section 4, we also briefly compare LLaMA with instruction-tuned models such as OPT-IML (Iyer et al., 2022) and Flan-PaLM (Chung et al., 2022).

We evaluate LLaMA on free-form generation tasks and multiple choice tasks. In the multiple choice tasks, the objective is to select the most appropriate completion among a set of given options, based on a provided context. We select the completion with the highest likelihood given the provided context. We follow Gao et al. (2021) and use the likelihood normalized by the number of characters in the completion, except for certain datasets (OpenBookQA, BoolQ), for which we follow Brown et al. (2020), and select a completion based on the likelihood normalized by the likelihood of the completion given "Answer:" as context: P(completion|context)/P(completion|"Answer:").

## 3.1 Common Sense Reasoning

We consider eight standard common sense reasoning benchmarks: BoolQ (Clark et al., 2019), PIQA (Bisk et al., 2020), SIQA (Sap et al., 2019), HellaSwag (Zellers et al., 2019), WinoGrande (Sakaguchi et al., 2021), ARC easy and challenge (Clark et al., 2018) and OpenBookQA (Mihaylov et al., 2018). These datasets include Cloze and Winograd style tasks, as well as multiple choice question answering. We evaluate in the zero-shot setting as done in the language modeling community.

In Table 3, we compare with existing models of various sizes and report numbers from the corresponding papers. First, LLaMA-65B outperforms Chinchilla-70B on all reported benchmarks but BoolQ. Similarly, this model surpasses PaLM-540B everywhere but on BoolQ and WinoGrande. LLaMA-13B model also outperforms GPT-3 on most benchmarks despite being 10× smaller.

## 3.2 Closed-book Question Answering

We compare LLaMA to existing large language models on two closed-book question answering benchmarks: Natural Questions (Kwiatkowski et al., 2019) and TriviaQA (Joshi et al., 2017). For both benchmarks, we report exact match performance in a closed book setting, i.e., where the models do not have access to documents that contain evidence to answer the question. In Table 4, we report performance on NaturalQuestions, and in Table 5, we report on TriviaQA. On both benchmarks, LLaMA-65B achieve state-of-the-arts performance in the zero-shot and few-shot settings. More importantly, the LLaMA-13B is also competitive on these benchmarks with GPT-3 and Chinchilla, despite being 5-10× smaller. This model runs on a single V100 GPU during inference.

## 3.3 Reading Comprehension

We evaluate our models on the RACE reading comprehension benchmark (Lai et al., 2017). This dataset was collected from English reading comprehension exams designed for middle and high school Chinese students. We follow the evaluation setup from Brown et al. (2020) and report results in Table 6. On these benchmarks, LLaMA-65B is competitive with PaLM-540B, and, LLaMA-13B outperforms GPT-3 by a few percents.

## 3.4 Mathematical reasoning

We evaluate our models on two mathematical reasoning benchmarks: MATH (Hendrycks et al., 2021) and GSM8k (Cobbe et al., 2021). MATH is a dataset of 12K middle school and high school mathematics problems written in LaTeX. GSM8k is a set of middle school mathematical problems.

In Table 7, we compare with PaLM and Minerva (Lewkowycz et al., 2022). Minerva is a series of PaLM models finetuned on 38.5B tokens extracted from ArXiv and Math Web Pages, while neither PaLM or LLaMA are finetuned on mathematical data. The numbers for PaLM and Minerva are taken from Lewkowycz et al. (2022), and we compare with and without maj1@k. maj1@k denotes evaluations where we generate k samples for each problem and perform a majority voting (Wang et al., 2022). On GSM8k, we observe that LLaMA-65B outperforms Minerva-62B, although it has not been fine-tuned on mathematical data.

## 3.5 Code generation

We evaluate the ability of our models to write code from a natural language description on two benchmarks: HumanEval (Chen et al., 2021) and MBPP (Austin et al., 2021). For both tasks, the model receives a description of the program in a few sentences, as well as a few input-output examples. In HumanEval, it also receives a function signature, and the prompt is formatted as natural code with the textual description and tests in a docstring. The model needs to generate a Python program that fits the description and satisfies the test cases. In Table 8, we compare the pass@1 scores of our models with existing language models that have not been finetuned on code, namely PaLM and LaMDA (Thoppilan et al., 2022). PaLM and LLaMA were trained on datasets that contain a similar number of code tokens.

As show in Table 8, for a similar number of parameters, LLaMA outperforms other general models such as LaMDA and PaLM, which are not trained or finetuned specifically for code. LLaMA with 13B parameters and more outperforms LaMDA 137B on both HumanEval and MBPP. LLaMA 65B also outperforms PaLM 62B, even when it is trained longer. The pass@1 results reported in this table were obtained by sampling with temperature 0.1. The pass@100 and pass@80 metrics were obtained with temperature 0.8. We use the same method as Chen et al. (2021) to obtain unbiased estimates of the pass@k.

It is possible to improve the performance on code by finetuning on code-specific tokens. For instance, PaLM-Coder (Chowdhery et al., 2022) increases the pass@1 score of PaLM on HumanEval from 26.2% for PaLM to 36%. Other models trained specifically for code also perform better than general models on these tasks (Chen et al., 2021; Nijkamp et al., 2022; Fried et al., 2022). Finetuning on code tokens is beyond the scope of this paper.

## 3.6 Massive Multitask Language Understanding

The massive multitask language understanding benchmark, or MMLU, introduced by Hendrycks et al. (2020) consists of multiple choice questions covering various domains of knowledge, including humanities, STEM and social sciences. We evaluate our models in the 5-shot setting, using the examples provided by the benchmark, and report results in Table 9. On this benchmark, we observe that the LLaMA-65B is behind both Chinchilla-70B and PaLM-540B by a few percent in average, and across most domains. A potential explanation is that we have used a limited amount of books and academic papers in our pre-training data, i.e., ArXiv, Gutenberg and Books3, that sums up to only 177GB, while these models were trained on up to 2TB of books. This large quantity of books used by Gopher, Chinchilla and PaLM may also explain why Gopher outperforms GPT-3 on this benchmark, while it is comparable on other benchmarks.

## 3.7 Evolution of performance during training

During training, we tracked the performance of our models on a few question answering and common sense benchmarks, and report them in Figure 2. On most benchmarks, the performance improves steadily, and correlates with the training perplexity of the model (see Figure 1). The exceptions are SIQA and WinoGrande. Most notably, on SIQA, we observe a lot of variance in performance, that may indicate that this benchmark is not reliable. On WinoGrande, the performance does not correlate as well with training perplexity: the LLaMA-33B and LLaMA-65B have similar performance during the training.

---

### النسخة العربية

بعد الأعمال السابقة (Brown et al., 2020)، نأخذ في الاعتبار المهام بدون أمثلة والمهام بأمثلة قليلة، ونُبلّغ عن النتائج على إجمالي 20 معياراً:

• **بدون أمثلة.** نقدم وصفاً نصياً للمهمة ومثالاً اختبارياً. يقدم النموذج إما إجابة باستخدام التوليد المفتوح، أو يرتب الإجابات المقترحة.

• **أمثلة قليلة.** نقدم بضعة أمثلة للمهمة (بين 1 و64) ومثالاً اختبارياً. يأخذ النموذج هذا النص كمدخل ويولد الإجابة أو يرتب الخيارات المختلفة.

نقارن LLaMA مع نماذج أساسية أخرى، وهي نماذج اللغة غير المتاحة للعموم GPT-3 (Brown et al., 2020)، وGopher (Rae et al., 2021)، وChinchilla (Hoffmann et al., 2022)، وPaLM (Chowdhery et al., 2022)، بالإضافة إلى نماذج OPT مفتوحة المصدر (Zhang et al., 2022)، وGPT-J (Wang and Komatsuzaki, 2021)، وGPTNeo (Black et al., 2022). في القسم 4، نقارن LLaMA أيضاً بإيجاز مع النماذج المضبوطة بالتعليمات مثل OPT-IML (Iyer et al., 2022) وFlan-PaLM (Chung et al., 2022).

نقيّم LLaMA على مهام التوليد المفتوح ومهام الاختيار من متعدد. في مهام الاختيار من متعدد، الهدف هو اختيار الإكمال الأكثر ملاءمة من بين مجموعة من الخيارات المقدمة، بناءً على سياق مقدم. نختار الإكمال ذو أعلى احتمال نظراً للسياق المقدم. نتبع Gao et al. (2021) ونستخدم الاحتمال المُطَبَّع بعدد الأحرف في الإكمال، باستثناء مجموعات بيانات معينة (OpenBookQA، BoolQ)، التي نتبع فيها Brown et al. (2020)، ونختار إكمالاً بناءً على الاحتمال المُطَبَّع بواسطة احتمال الإكمال بالنظر إلى "Answer:" كسياق: P(completion|context)/P(completion|"Answer:").

## 3.1 التفكير بالحس السليم

نأخذ في الاعتبار ثمانية معايير قياسية للتفكير بالحس السليم: BoolQ (Clark et al., 2019)، وPIQA (Bisk et al., 2020)، وSIQA (Sap et al., 2019)، وHellaSwag (Zellers et al., 2019)، وWinoGrande (Sakaguchi et al., 2021)، وARC السهل والتحدي (Clark et al., 2018)، وOpenBookQA (Mihaylov et al., 2018). تتضمن هذه المجموعات من البيانات مهام نمط Cloze وWinograd، بالإضافة إلى الإجابة على الأسئلة متعددة الخيارات. نقيّم في إعداد بدون أمثلة كما هو معمول به في مجتمع نمذجة اللغة.

في الجدول 3، نقارن مع النماذج الموجودة ذات الأحجام المختلفة ونُبلّغ عن الأرقام من الأوراق المقابلة. أولاً، يتفوق LLaMA-65B على Chinchilla-70B في جميع المعايير المُبلّغ عنها باستثناء BoolQ. وبالمثل، يتفوق هذا النموذج على PaLM-540B في كل مكان باستثناء BoolQ وWinoGrande. يتفوق نموذج LLaMA-13B أيضاً على GPT-3 في معظم المعايير على الرغم من أنه أصغر بعشر مرات.

## 3.2 الإجابة على الأسئلة المغلقة

نقارن LLaMA مع نماذج اللغة الكبيرة الموجودة على معيارين للإجابة على الأسئلة المغلقة: Natural Questions (Kwiatkowski et al., 2019) وTriviaQA (Joshi et al., 2017). لكلا المعيارين، نُبلّغ عن أداء المطابقة الدقيقة في إعداد مغلق، أي حيث لا تملك النماذج وصولاً إلى المستندات التي تحتوي على أدلة للإجابة على السؤال. في الجدول 4، نُبلّغ عن الأداء على NaturalQuestions، وفي الجدول 5، نُبلّغ عن TriviaQA. على كلا المعيارين، يحقق LLaMA-65B أداءً متقدماً في إعدادات بدون أمثلة وأمثلة قليلة. والأهم من ذلك، أن LLaMA-13B منافس أيضاً على هذه المعايير مع GPT-3 وChinchilla، على الرغم من أنه أصغر بـ 5-10 مرات. يعمل هذا النموذج على وحدة معالجة رسومية V100 واحدة أثناء الاستنتاج.

## 3.3 الفهم القرائي

نقيّم نماذجنا على معيار الفهم القرائي RACE (Lai et al., 2017). تم جمع مجموعة البيانات هذه من اختبارات الفهم القرائي باللغة الإنجليزية المصممة لطلاب المدارس المتوسطة والثانوية الصينيين. نتبع إعداد التقييم من Brown et al. (2020) ونُبلّغ عن النتائج في الجدول 6. على هذه المعايير، LLaMA-65B منافس لـ PaLM-540B، ويتفوق LLaMA-13B على GPT-3 بنسب مئوية قليلة.

## 3.4 التفكير الرياضي

نقيّم نماذجنا على معيارين للتفكير الرياضي: MATH (Hendrycks et al., 2021) وGSM8k (Cobbe et al., 2021). MATH عبارة عن مجموعة بيانات من 12 ألف مسألة رياضية للمدارس المتوسطة والثانوية مكتوبة بصيغة LaTeX. GSM8k عبارة عن مجموعة من المسائل الرياضية للمدارس المتوسطة.

في الجدول 7، نقارن مع PaLM وMinerva (Lewkowycz et al., 2022). Minerva عبارة عن سلسلة من نماذج PaLM المضبوطة على 38.5B رمز مستخرج من ArXiv وصفحات الويب الرياضية، بينما لم يتم ضبط PaLM أو LLaMA على بيانات رياضية. تم أخذ الأرقام لـ PaLM وMinerva من Lewkowycz et al. (2022)، ونقارن مع وبدون maj1@k. maj1@k يشير إلى التقييمات حيث نولّد k عينة لكل مسألة ونجري تصويتاً بالأغلبية (Wang et al., 2022). على GSM8k، نلاحظ أن LLaMA-65B يتفوق على Minerva-62B، على الرغم من أنه لم يتم ضبطه على بيانات رياضية.

## 3.5 توليد الشفرة

نقيّم قدرة نماذجنا على كتابة الشفرة من وصف بلغة طبيعية على معيارين: HumanEval (Chen et al., 2021) وMBPP (Austin et al., 2021). لكلا المهمتين، يتلقى النموذج وصفاً للبرنامج في بضع جمل، بالإضافة إلى بضعة أمثلة للمدخلات والمخرجات. في HumanEval، يتلقى أيضاً توقيع دالة، ويتم تنسيق المطالبة كشفرة طبيعية مع الوصف النصي والاختبارات في سلسلة توثيق. يحتاج النموذج إلى توليد برنامج Python يناسب الوصف ويُرضي حالات الاختبار. في الجدول 8، نقارن درجات pass@1 لنماذجنا مع نماذج اللغة الموجودة التي لم يتم ضبطها على الشفرة، وهي PaLM وLaMDA (Thoppilan et al., 2022). تم تدريب PaLM وLLaMA على مجموعات بيانات تحتوي على عدد مماثل من رموز الشفرة.

كما هو موضح في الجدول 8، لعدد مماثل من المعاملات، يتفوق LLaMA على النماذج العامة الأخرى مثل LaMDA وPaLM، التي لم يتم تدريبها أو ضبطها خصيصاً للشفرة. LLaMA بـ 13B معامل وأكثر يتفوق على LaMDA 137B على كل من HumanEval وMBPP. يتفوق LLaMA 65B أيضاً على PaLM 62B، حتى عندما يتم تدريبه لفترة أطول. تم الحصول على نتائج pass@1 المُبلّغ عنها في هذا الجدول من خلال العينات بدرجة حرارة 0.1. تم الحصول على مقاييس pass@100 وpass@80 بدرجة حرارة 0.8. نستخدم نفس الطريقة كما في Chen et al. (2021) للحصول على تقديرات غير متحيزة لـ pass@k.

من الممكن تحسين الأداء على الشفرة بالضبط على رموز خاصة بالشفرة. على سبيل المثال، يزيد PaLM-Coder (Chowdhery et al., 2022) درجة pass@1 لـ PaLM على HumanEval من 26.2% لـ PaLM إلى 36%. النماذج الأخرى المُدربة خصيصاً للشفرة تؤدي أيضاً بشكل أفضل من النماذج العامة على هذه المهام (Chen et al., 2021; Nijkamp et al., 2022; Fried et al., 2022). الضبط على رموز الشفرة يتجاوز نطاق هذه الورقة.

## 3.6 الفهم اللغوي الهائل متعدد المهام

معيار الفهم اللغوي الهائل متعدد المهام، أو MMLU، الذي قدمه Hendrycks et al. (2020) يتكون من أسئلة اختيار من متعدد تغطي مجالات مختلفة من المعرفة، بما في ذلك العلوم الإنسانية وSTEM والعلوم الاجتماعية. نقيّم نماذجنا في إعداد 5 أمثلة، باستخدام الأمثلة المقدمة من المعيار، ونُبلّغ عن النتائج في الجدول 9. على هذا المعيار، نلاحظ أن LLaMA-65B متأخر عن كل من Chinchilla-70B وPaLM-540B بنسبة مئوية قليلة في المتوسط، وعبر معظم المجالات. التفسير المحتمل هو أننا استخدمنا كمية محدودة من الكتب والأوراق الأكاديمية في بيانات التدريب المسبق الخاصة بنا، أي ArXiv وGutenberg وBooks3، التي يبلغ مجموعها 177 جيجابايت فقط، بينما تم تدريب هذه النماذج على ما يصل إلى 2 تيرابايت من الكتب. هذه الكمية الكبيرة من الكتب المستخدمة من قبل Gopher وChinchilla وPaLM قد تفسر أيضاً لماذا يتفوق Gopher على GPT-3 على هذا المعيار، بينما هو مماثل على المعايير الأخرى.

## 3.7 تطور الأداء أثناء التدريب

أثناء التدريب، تتبعنا أداء نماذجنا على بعض معايير الإجابة على الأسئلة والحس السليم، ونُبلّغ عنها في الشكل 2. على معظم المعايير، يتحسن الأداء بشكل مطرد، ويرتبط بحيرة التدريب للنموذج (انظر الشكل 1). الاستثناءات هي SIQA وWinoGrande. والأبرز، على SIQA، نلاحظ تبايناً كبيراً في الأداء، مما قد يشير إلى أن هذا المعيار غير موثوق. على WinoGrande، لا يرتبط الأداء جيداً بحيرة التدريب: LLaMA-33B وLLaMA-65B لهما أداء مماثل أثناء التدريب.

---

### Translation Notes

- **Tables referenced:** Table 3-9 (extensive benchmark results)
- **Figures referenced:** Figure 1 (training loss), Figure 2 (evolution of performance)
- **Key benchmarks covered:**
  - Common sense: BoolQ, PIQA, SIQA, HellaSwag, WinoGrande, ARC, OpenBookQA
  - QA: Natural Questions, TriviaQA
  - Reading: RACE
  - Math: MATH, GSM8k
  - Code: HumanEval, MBPP
  - General: MMLU (57 subjects across humanities, STEM, social sciences)
- **Special handling:**
  - Dataset names kept in original form
  - Score percentages and numbers preserved
  - Model comparisons maintained with exact figures
  - pass@k metric notation preserved

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.86
- **Overall section score:** 0.87
