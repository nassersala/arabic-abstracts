# Section 5: Results and Analysis
## القسم 5: النتائج والتحليل

**Section:** results and analysis
**Translation Quality:** 0.86
**Glossary Terms Used:** تلخيص الشفرة, توليد الشفرة, ترجمة الشفرة, تحسين الشفرة, كشف العيوب, كشف الاستنساخ, مشفر-فك تشفير, التوليد المزدوج ثنائي الوضع, التعلم متعدد المهام, دراسة استئصال, وسم المعرفات, التنبؤ بالمعرفات المخفية, التنبؤ بالنطاق المخفي

---

### English Version

**5 Results and Analysis**

In this section, we compare CodeT5 with SOTA models on a broad set of CodeXGLUE downstream tasks (§5.1), and investigate the effects of our bimodal dual generation and multi-task learning (§5.2), followed by a detailed analysis on the proposed identifier-aware pre-training (§5.3).

**5.1 CodeXGLUE Downstream Tasks**

We evaluate two sizes of our model: CodeT5-small and CodeT5-base that are pre-trained with identifier-aware denoising. In addition, we consider the model that continues to train with bimodal dual generation (dual-gen) and show the results with multi-task fine-tuning. The results of all comparison models are obtained from their original papers and also the CodeXGLUE paper (Lu et al., 2021).

**Code Summarization.** We show code summarization results of smoothed BLEU-4 on six PL data in Table 2. We observe all our model variants significantly outperform prior work with either an encode-only (RoBERTa, CodeBERT, DOBF) or encoder-decoder framework (PLBART). Moreover, the salient performance gap between these two groups of models confirms that encode-only frameworks are suboptimal for generation tasks. Compared to the SOTA encoder-decoder model PLBART, we find that even our CodeT5-small yields better overall scores (also on Python and Java) given that our model is much smaller (60M vs. 140M) and PLBART is pre-trained with much larger Python and Java data (> 100 times). We attribute such improvement to our identifier-aware denoising pre-training and better employment of bimodal training data. By increasing the model size, our CodeT5-base boosts the overall performance by over 1.2 absolute points over PLBART.

**Code Generation.** We compare CodeT5 with GPT-style models and PLBART in Table 3. Our CodeT5-small outperforms all decoder-only models and also the SOTA PLBART, which again confirms the superiority of encoder-decoder models at generating code snippets. Moreover, our CodeT5-base further significantly pushes the SOTA results across three metrics. Particularly, it achieves around 4.7 points improvement on CodeBLEU over PLBART, indicating our CodeT5 can better comprehend the code syntax and semantics with the help of identifier-aware pre-training.

**Code-to-Code Generation Tasks.** We compare two code-to-code generation tasks: code translation and code refinement in Table 4 and further consider one naive copy baseline by copying the source input as the target prediction. In the code translation task, our CodeT5-small outperforms most of baselines and obtains comparable results with PLBART, which shows the advantages of encoder-decoder models in the code-to-code generation setting. Our CodeT5-base further achieves consistent improvements over PLBART across various metrics for translating from Java to C# and vice versa.

Here we show one CodeT5's output of translating C# to Java in Figure 3. In this case, despite the poor BLEU score, CodeT5 is able to generate a function that reserves the same functionality and even has better readability compared to the ground-truth. This reveals that CodeT5 has a good generalization ability instead of memorizing and repeating what it has seen before. On the other hand, it also suggests that BLEU score is not a perfect evaluation metric for code generation tasks, where sometimes a higher score can instead reflect the problematic copy issues of neural models.

Another code-to-code generation task is code refinement, a challenging task that requires to detect which parts of code are buggy and fix them via generating a bug-free code sequence. Due to the large overlap of source and target code, even the naive copy approach yields very high BLEU scores but zero exact matches. Therefore, we focus on the exact match (EM) metric to evaluate on this task. As shown in Table 4, we observe that EM scores for the small data are consistently higher than the medium one, indicating that it is harder to fix bugs for a longer code snippet. Our CodeT5-base significantly outperforms all baselines on EM and especially boosts over 4.8 points for the more challenging medium task (13.96 vs. GraphCodeBERT's 9.10), reflecting its strong code understanding capability.

**Understanding Tasks.** We compare with two understanding tasks of defect detection and clone detection in Table 5. Specifically, we generate the binary labels as a unigram sequence from the decoder for the defect detection task, while for the clone detection task, we first obtain the sequence embedding of each code snippet using the last decoder state following Lewis et al. (2020) and then predict the labels by measuring their similarity. Both CodeT5-small and CodeT5-base outperform all baselines on the defect detection task while CodeT5-base yields 2.6 accuracy score improvement than PLBART. For the clone detection task, our CodeT5 models achieve comparable results to the SOTA GraphCodeBERT and PLBART models. These results demonstrate that with an encode-decoder framework, our CodeT5 can still be adapted well for understanding tasks.

**5.2 Effects of Bimodal Dual Generation and Multi-task Learning**

We examine the effects of bimodal dual generation at pre-training and multi-task learning at fine-tuning. The bimodal pre-training brings consistent improvements for code summarization and generation tasks on both CodeT5-small and CodeT5-base. However, this pre-training task does not help and even sometimes slightly hurts the performance for PL-PL generation and understanding tasks. We anticipate this is because bimodal dual generation learns a better alignment between PL and NL that naturally benefits the former tasks involving both PL and NL. As a side effect, this objective could bias the model towards the PL-NL tasks and affect its performance on PL-PL tasks.

In multi-task learning, it generally improves most of downstream tasks except the code translation and defect detection. Particularly, it largely boosts the performance on code summarization, which is not surprising as code summarization takes up the largest portion of sub tasks (six out of thirteen) and thereby benefit the most from the multi-task learning. Besides, we observe that multi-task learning consistently improves the performance of code refinement, which might benefit from the joint training of both small and medium refinement data. Another possible reason is that multi-task training with defect detection would enable the model to better comprehend the code semantics for bug detection, which is also a necessary intermediate step for code refinement.

**5.3 Analyzing Identifier-aware Pre-training**

We provide an ablation study to examine the contribution of each component in our identifier-aware objective. Specifically, we compare the performance of our CodeT5-small on four selected tasks by ablating each of the three objectives: masked span prediction (MSP), identifier tagging (IT), and masked identifier prediction (MIP). As shown in Table 6, we observe that generally removing one of the objectives would reduce the performance for all tasks, indicating that all objectives contribute to the better code understanding of our CodeT5. However, the effect of each objective differs across tasks. Specifically, removing MSP would largely reduce the performance of all generation tasks but instead increase the defect detection performance. This shows that masked span prediction is more crucial for capturing syntactic information for generation tasks. On the contrary, removing MIP would hurt the defect detection task the most, indicating that it might focus more on code semantic understanding. By combining these objectives, our CodeT5 can better capture both syntactic and semantic information from code.

We further provide outputs from CodeT5 and its variant without MIP and IT on code generation in Figure 4. We observe that CodeT5 can correctly generate the exact function, while the model without MIP and IT fails to recover the identifiers of "s2" and "hasField". This shows our identifier-aware denoising pre-training can better distinguish and leverage the identifier information.

We also investigate the identifier tagging performance and find it achieves over 99% F1 for all PLs, showing that our CodeT5 can confidently distinguish identifiers in code. We then check whether MSP and MIP tasks would have conflicts as they employ the same sentinel tokens for masking. In identifier masking, all occurrences of one unique identifier are replaced with the same sentinel token, resulting in a many-to-one mapping compared to the one-to-one mapping in span prediction. We compare models pre-trained with either MSP or MIP, and both on these two tasks in Table 7. We report the prediction accuracy and also the ratio of how often they can generate the same number of predictions as the sentinel tokens. We observe that pre-training only with either MIP or MSP would bias the model towards that task, achieving poor accuracy and higher mismatch in number of predictions when applied to the other task. Interestingly, we find that MIP-only objective can better recover the correct number of predictions in the MSP task than MSP-only does for the MIP task, meaning that it is easier to adapt from many-to-one mapping to one-to-one mapping and difficult for the opposite. At last, combining them can help our model to make a good trade-off on both tasks.

---

### النسخة العربية

**5 النتائج والتحليل**

في هذا القسم، نقارن CodeT5 مع نماذج متقدمة على مجموعة واسعة من المهام اللاحقة في CodeXGLUE (§5.1)، ونستكشف تأثيرات التوليد المزدوج ثنائي الوضع والتعلم متعدد المهام (§5.2)، متبوعاً بتحليل تفصيلي للتدريب المسبق المدرك للمعرفات المقترح (§5.3).

**5.1 مهام CodeXGLUE اللاحقة**

نقيّم حجمين من نموذجنا: CodeT5-small و CodeT5-base المُدربان مسبقاً بإزالة التشويش المدركة للمعرفات. بالإضافة إلى ذلك، نأخذ في الاعتبار النموذج الذي يستمر في التدريب بالتوليد المزدوج ثنائي الوضع (dual-gen) ونعرض النتائج مع الضبط الدقيق متعدد المهام. يتم الحصول على نتائج جميع نماذج المقارنة من أوراقها الأصلية وأيضاً ورقة CodeXGLUE (Lu et al., 2021).

**تلخيص الشفرة.** نعرض نتائج تلخيص الشفرة من BLEU-4 الناعم على بيانات ست لغات برمجة في الجدول 2. نلاحظ أن جميع متغيرات نموذجنا تتفوق بشكل كبير على العمل السابق إما بإطار عمل مشفر فقط (RoBERTa، CodeBERT، DOBF) أو إطار عمل مشفر-فك تشفير (PLBART). علاوة على ذلك، تؤكد الفجوة البارزة في الأداء بين هاتين المجموعتين من النماذج أن أطر العمل بمشفر فقط دون المستوى الأمثل لمهام التوليد. بالمقارنة مع نموذج مشفر-فك التشفير المتقدم PLBART، نجد أن حتى CodeT5-small الخاص بنا يحقق درجات إجمالية أفضل (أيضاً على Python و Java) بالنظر إلى أن نموذجنا أصغر بكثير (60M مقابل 140M) و PLBART مُدرب مسبقاً ببيانات Python و Java أكبر بكثير (> 100 مرة). نعزو هذا التحسن إلى التدريب المسبق لإزالة التشويش المدرك للمعرفات والاستخدام الأفضل لبيانات التدريب ثنائية الوضع. من خلال زيادة حجم النموذج، يعزز CodeT5-base الخاص بنا الأداء الإجمالي بأكثر من 1.2 نقطة مطلقة على PLBART.

**توليد الشفرة.** نقارن CodeT5 مع نماذج على طراز GPT و PLBART في الجدول 3. يتفوق CodeT5-small الخاص بنا على جميع نماذج فك التشفير فقط وأيضاً PLBART المتقدم، مما يؤكد مرة أخرى تفوق نماذج مشفر-فك التشفير في توليد مقتطفات الشفرة. علاوة على ذلك، يدفع CodeT5-base الخاص بنا النتائج المتقدمة بشكل كبير عبر ثلاثة مقاييس. على وجه الخصوص، يحقق حوالي 4.7 نقطة تحسن على CodeBLEU على PLBART، مما يشير إلى أن CodeT5 الخاص بنا يمكنه فهم بناء جملة الشفرة ودلالاتها بشكل أفضل بمساعدة التدريب المسبق المدرك للمعرفات.

**مهام التوليد من شفرة إلى شفرة.** نقارن مهمتي توليد من شفرة إلى شفرة: ترجمة الشفرة وتحسين الشفرة في الجدول 4 ونأخذ في الاعتبار أيضاً خط أساس نسخ ساذج من خلال نسخ إدخال المصدر كتنبؤ مستهدف. في مهمة ترجمة الشفرة، يتفوق CodeT5-small الخاص بنا على معظم خطوط الأساس ويحصل على نتائج قابلة للمقارنة مع PLBART، مما يُظهر مزايا نماذج مشفر-فك التشفير في إعداد التوليد من شفرة إلى شفرة. يحقق CodeT5-base الخاص بنا أيضاً تحسينات متسقة على PLBART عبر مقاييس مختلفة للترجمة من Java إلى C# والعكس.

هنا نعرض أحد مخرجات CodeT5 لترجمة C# إلى Java في الشكل 3. في هذه الحالة، على الرغم من درجة BLEU الضعيفة، يمكن لـ CodeT5 توليد دالة تحتفظ بنفس الوظيفة وحتى لديها قابلية قراءة أفضل بالمقارنة مع الحقيقة الأرضية. هذا يكشف أن CodeT5 لديه قدرة تعميم جيدة بدلاً من الحفظ وتكرار ما رآه من قبل. من ناحية أخرى، يشير أيضاً إلى أن درجة BLEU ليست مقياس تقييم مثالياً لمهام توليد الشفرة، حيث يمكن أن تعكس الدرجة الأعلى أحياناً مشاكل النسخ الإشكالية للنماذج العصبية.

مهمة أخرى للتوليد من شفرة إلى شفرة هي تحسين الشفرة، وهي مهمة صعبة تتطلب اكتشاف أي أجزاء من الشفرة بها أخطاء وإصلاحها عبر توليد تسلسل شفرة خالٍ من الأخطاء. بسبب التداخل الكبير بين شفرة المصدر والهدف، حتى نهج النسخ الساذج يحقق درجات BLEU عالية جداً ولكن صفر مطابقات تامة. لذلك، نركز على مقياس المطابقة التامة (EM) للتقييم في هذه المهمة. كما هو موضح في الجدول 4، نلاحظ أن درجات EM للبيانات الصغيرة أعلى باستمرار من المتوسطة، مما يشير إلى أنه من الأصعب إصلاح الأخطاء لمقتطف شفرة أطول. يتفوق CodeT5-base الخاص بنا بشكل كبير على جميع خطوط الأساس في EM ويعزز بشكل خاص أكثر من 4.8 نقطة للمهمة المتوسطة الأكثر تحدياً (13.96 مقابل 9.10 من GraphCodeBERT)، مما يعكس قدرته القوية على فهم الشفرة.

**مهام الفهم.** نقارن مع مهمتي فهم لكشف العيوب وكشف الاستنساخ في الجدول 5. على وجه التحديد، نولد التسميات الثنائية كتسلسل أحادي الكلمة من فك التشفير لمهمة كشف العيوب، بينما لمهمة كشف الاستنساخ، نحصل أولاً على تضمين التسلسل لكل مقتطف شفرة باستخدام آخر حالة لفك التشفير متبعين Lewis et al. (2020) ثم نتنبأ بالتسميات من خلال قياس تشابهها. يتفوق كل من CodeT5-small و CodeT5-base على جميع خطوط الأساس في مهمة كشف العيوب بينما يحقق CodeT5-base تحسناً في درجة الدقة بمقدار 2.6 عن PLBART. بالنسبة لمهمة كشف الاستنساخ، تحقق نماذج CodeT5 الخاصة بنا نتائج قابلة للمقارنة مع نماذج GraphCodeBERT و PLBART المتقدمة. تُظهر هذه النتائج أنه مع إطار عمل مشفر-فك تشفير، لا يزال بإمكان CodeT5 الخاص بنا التكيف جيداً لمهام الفهم.

**5.2 تأثيرات التوليد المزدوج ثنائي الوضع والتعلم متعدد المهام**

نفحص تأثيرات التوليد المزدوج ثنائي الوضع في التدريب المسبق والتعلم متعدد المهام في الضبط الدقيق. يحقق التدريب المسبق ثنائي الوضع تحسينات متسقة لمهام تلخيص الشفرة وتوليدها على كل من CodeT5-small و CodeT5-base. ومع ذلك، فإن مهمة التدريب المسبق هذه لا تساعد وأحياناً حتى تضر قليلاً بالأداء لمهام التوليد والفهم من لغة برمجة إلى لغة برمجة. نتوقع أن هذا لأن التوليد المزدوج ثنائي الوضع يتعلم محاذاة أفضل بين لغة البرمجة واللغة الطبيعية مما يفيد بشكل طبيعي المهام السابقة التي تتضمن كلاً من لغة البرمجة واللغة الطبيعية. كأثر جانبي، يمكن أن يحيز هذا الهدف النموذج نحو مهام لغة البرمجة-اللغة الطبيعية ويؤثر على أدائه في مهام لغة البرمجة-لغة البرمجة.

في التعلم متعدد المهام، يحسّن بشكل عام معظم المهام اللاحقة باستثناء ترجمة الشفرة وكشف العيوب. على وجه الخصوص، يعزز إلى حد كبير الأداء في تلخيص الشفرة، وهو أمر ليس مفاجئاً لأن تلخيص الشفرة يشكل أكبر جزء من المهام الفرعية (ستة من أصل ثلاثة عشر) وبالتالي يستفيد أكثر من التعلم متعدد المهام. بالإضافة إلى ذلك، نلاحظ أن التعلم متعدد المهام يحسّن باستمرار أداء تحسين الشفرة، والذي قد يستفيد من التدريب المشترك لكل من بيانات التحسين الصغيرة والمتوسطة. سبب محتمل آخر هو أن التدريب متعدد المهام مع كشف العيوب سيمكّن النموذج من فهم دلالات الشفرة بشكل أفضل لكشف الأخطاء، وهي أيضاً خطوة وسيطة ضرورية لتحسين الشفرة.

**5.3 تحليل التدريب المسبق المدرك للمعرفات**

نقدم دراسة استئصال لفحص مساهمة كل مكون في هدفنا المدرك للمعرفات. على وجه التحديد، نقارن أداء CodeT5-small الخاص بنا على أربع مهام مختارة من خلال استئصال كل واحد من الأهداف الثلاثة: التنبؤ بالنطاق المخفي (MSP)، ووسم المعرفات (IT)، والتنبؤ بالمعرفات المخفية (MIP). كما هو موضح في الجدول 6، نلاحظ أن إزالة أحد الأهداف بشكل عام سيقلل من الأداء لجميع المهام، مما يشير إلى أن جميع الأهداف تساهم في الفهم الأفضل للشفرة في CodeT5 الخاص بنا. ومع ذلك، يختلف تأثير كل هدف عبر المهام. على وجه التحديد، ستقلل إزالة MSP إلى حد كبير من أداء جميع مهام التوليد ولكن بدلاً من ذلك تزيد من أداء كشف العيوب. هذا يُظهر أن التنبؤ بالنطاق المخفي أكثر أهمية لالتقاط المعلومات النحوية لمهام التوليد. على العكس من ذلك، ستضر إزالة MIP بمهمة كشف العيوب أكثر من غيرها، مما يشير إلى أنها قد تركز أكثر على فهم دلالات الشفرة. من خلال الجمع بين هذه الأهداف، يمكن لـ CodeT5 الخاص بنا التقاط كل من المعلومات النحوية والدلالية من الشفرة بشكل أفضل.

نقدم أيضاً مخرجات من CodeT5 ومتغيره بدون MIP و IT على توليد الشفرة في الشكل 4. نلاحظ أن CodeT5 يمكنه توليد الدالة الصحيحة بشكل صحيح، بينما يفشل النموذج بدون MIP و IT في استرداد المعرفات "s2" و "hasField". هذا يُظهر أن التدريب المسبق لإزالة التشويش المدرك للمعرفات يمكنه تمييز واستغلال معلومات المعرفات بشكل أفضل.

نستكشف أيضاً أداء وسم المعرفات ونجد أنه يحقق أكثر من 99٪ F1 لجميع لغات البرمجة، مما يُظهر أن CodeT5 الخاص بنا يمكنه تمييز المعرفات في الشفرة بثقة. ثم نتحقق مما إذا كانت مهام MSP و MIP ستتعارض حيث تستخدم نفس الرموز الحارسة للإخفاء. في إخفاء المعرفات، يتم استبدال جميع حالات ظهور معرّف فريد واحد بنفس الرمز الحارس، مما ينتج عنه تعيين متعدد إلى واحد بالمقارنة مع التعيين واحد إلى واحد في التنبؤ بالنطاق. نقارن النماذج المُدربة مسبقاً إما مع MSP أو MIP، وكليهما على هاتين المهمتين في الجدول 7. نقرر دقة التنبؤ وأيضاً نسبة عدد المرات التي يمكنهم فيها توليد نفس عدد التنبؤات كرموز الحراسة. نلاحظ أن التدريب المسبق فقط مع إما MIP أو MSP سيحيز النموذج نحو تلك المهمة، محققاً دقة ضعيفة وعدم تطابق أعلى في عدد التنبؤات عند تطبيقه على المهمة الأخرى. من المثير للاهتمام، نجد أن هدف MIP فقط يمكنه استرداد العدد الصحيح من التنبؤات في مهمة MSP بشكل أفضل من MSP فقط لمهمة MIP، مما يعني أنه من الأسهل التكيف من التعيين متعدد إلى واحد إلى التعيين واحد إلى واحد وصعب للعكس. أخيراً، يمكن أن يساعد الجمع بينهما نموذجنا على تحقيق مقايضة جيدة على كلتا المهمتين.

---

### Translation Notes

- **Figures referenced:** Figure 3, Figure 4
- **Tables referenced:** Table 2, Table 3, Table 4, Table 5, Table 6, Table 7
- **Key terms introduced:** دراسة استئصال (ablation study), مطابقة تامة (exact match), قابلية القراءة (readability), الحقيقة الأرضية (ground-truth), تضمين التسلسل (sequence embedding), تعيين متعدد إلى واحد (many-to-one mapping), تعيين واحد إلى واحد (one-to-one mapping)
- **Equations:** 0
- **Citations:** 2 references cited (Lu 2021, Lewis 2020)
- **Special handling:**
  - Preserved model names (CodeT5-small, CodeT5-base, RoBERTa, CodeBERT, DOBF, PLBART, GraphCodeBERT) in English
  - Preserved metric names (BLEU-4, CodeBLEU, EM, F1) in English where appropriate
  - Maintained table references for results discussion
  - Preserved code examples in English (Figure 3, Figure 4)

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
