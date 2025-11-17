# Sections 6-7: Carbon Footprint and Related Work
## الأقسام 6-7: البصمة الكربونية والأعمال ذات الصلة

**Section:** carbon footprint, related work
**Translation Quality:** 0.86
**Glossary Terms Used:** carbon emission, GPU, training, Watt-hour, Power Usage Effectiveness, n-gram, transformer, architecture, scaling laws, language model

---

### English Version

## 6 Carbon footprint

The training of our models have consumed a massive quantity of energy, responsible for the emission of carbon dioxide. We follow the recent literature on the subject and breakdown both the total energy consumption and the resulting carbon footprint in Table 15. We follow a formula for Wu et al. (2022) to estimate the Watt-hour, Wh, needed to train a model, as well as the tons of carbon emissions, tCO₂eq. For the Wh, we use the formula:

Wh = GPU-h×(GPU power consumption)×PUE,

where we set the Power Usage Effectiveness (PUE) at 1.1. The resulting carbon emission depends on the location of the data center used to train the network. For instance, BLOOM uses a grid that emits 0.057 kg CO₂eq/KWh leading to 27 tCO₂eq and OPT a grid that emits 0.231 kg CO₂eq/KWh, leading to 82 tCO₂eq. In this study, we are interested in comparing the cost in carbon emission of training of these models if they were trained in the same data center. Hence, we do not take the location of data center in consideration, and use, instead, the US national average carbon intensity factor of 0.385 kg CO₂eq/KWh. This leads to the following formula for the tons of carbon emissions:

tCO₂eq = MWh × 0.385.

We apply the same formula to OPT and BLOOM for fair comparison. For OPT, we assume training required 34 days on 992 A100-80B (see their logs). Finally, we estimate that we used 2048 A100-80GB for a period of approximately 5 months to develop our models. This means that developing these models would have cost around 2,638 MWh under our assumptions, and a total emission of 1,015 tCO₂eq. We hope that releasing these models will help to reduce future carbon emission since the training is already done, and some of the models are relatively small and can be run on a single GPU.

## 7 Related work

**Language models** are probability distributions over sequences of words, tokens or characters (Shannon, 1948, 1951). This task, often framed as next token prediction, has long been considered a core problem in natural language processing (Bahl et al., 1983; Brown et al., 1990). Because Turing (1950) proposed to measure machine intelligence by using language through the "imitation game", language modeling has been proposed as a benchmark to measure progress toward artificial intelligence (Mahoney, 1999).

**Architecture.** Traditionally, language models were based on n-gram count statistics (Bahl et al., 1983), and various smoothing techniques were proposed to improve the estimation of rare events (Katz, 1987; Kneser and Ney, 1995). In the past two decades, neural networks have been successfully applied to the language modelling task, starting from feed forward models (Bengio et al., 2000), recurrent neural networks (Elman, 1990; Mikolov et al., 2010) and LSTMs (Hochreiter and Schmidhuber, 1997; Graves, 2013). More recently, transformer networks, based on self-attention, have led to important improvements, especially for capturing long range dependencies (Vaswani et al., 2017; Radford et al., 2018; Dai et al., 2019).

**Scaling.** There is a long history of scaling for language models, for both the model and dataset sizes. Brants et al. (2007) showed the benefits of using language models trained on 2 trillion tokens, resulting in 300 billion n-grams, on the quality of machine translation. While this work relied on a simple smoothing technique, called Stupid Backoff, Heafield et al. (2013) later showed how to scale Kneser-Ney smoothing to Web-scale data. This allowed to train a 5-gram model on 975 billions tokens from CommonCrawl, resulting in a model with 500 billions n-grams (Buck et al., 2014). Chelba et al. (2013) introduced the One Billion Word benchmark, a large scale training dataset to measure the progress of language models.

In the context of neural language models, Jozefowicz et al. (2016) obtained state-of-the-art results on the Billion Word benchmark by scaling LSTMs to 1 billion parameters. Later, scaling transformers lead to improvement on many NLP tasks. Notable models include BERT (Devlin et al., 2018), GPT-2 (Radford et al., 2019), Megatron-LM (Shoeybi et al., 2019), and T5 (Raffel et al., 2020). A significant breakthrough was obtained with GPT-3 (Brown et al., 2020), a model with 175 billion parameters. This lead to a series of Large Language Models, such as Jurassic-1 (Lieber et al., 2021), Megatron-Turing NLG (Smith et al., 2022), Gopher (Rae et al., 2021), Chinchilla (Hoffmann et al., 2022), PaLM (Chowdhery et al., 2022), OPT (Zhang et al., 2022), and GLM (Zeng et al., 2022). Hestness et al. (2017) and Rosenfeld et al. (2019) studied the impact of scaling on the performance of deep learning models, showing the existence of power laws between the model and dataset sizes and the performance of the system. Kaplan et al. (2020) derived power laws specifically for transformer based language models, which were later refined by Hoffmann et al. (2022), by adapting the learning rate schedule when scaling datasets. Finally, Wei et al. (2022) studied the effect of scaling on the abilities of large language models.

---

### النسخة العربية

## 6 البصمة الكربونية

استهلك تدريب نماذجنا كمية هائلة من الطاقة، المسؤولة عن انبعاث ثاني أكسيد الكربون. نتبع الأدبيات الحديثة حول الموضوع ونوضح كلاً من إجمالي استهلاك الطاقة والبصمة الكربونية الناتجة في الجدول 15. نتبع صيغة من Wu et al. (2022) لتقدير وات-ساعة، Wh، اللازمة لتدريب نموذج، بالإضافة إلى أطنان انبعاثات الكربون، tCO₂eq. بالنسبة لـ Wh، نستخدم الصيغة:

Wh = GPU-h×(استهلاك طاقة GPU)×PUE،

حيث نضبط فعالية استخدام الطاقة (PUE) على 1.1. يعتمد انبعاث الكربون الناتج على موقع مركز البيانات المستخدم لتدريب الشبكة. على سبيل المثال، يستخدم BLOOM شبكة تنبعث منها 0.057 كجم CO₂eq/KWh مما يؤدي إلى 27 tCO₂eq، ويستخدم OPT شبكة تنبعث منها 0.231 كجم CO₂eq/KWh، مما يؤدي إلى 82 tCO₂eq. في هذه الدراسة، نهتم بمقارنة تكلفة انبعاثات الكربون لتدريب هذه النماذج إذا تم تدريبها في نفس مركز البيانات. لذلك، لا نأخذ موقع مركز البيانات في الاعتبار، ونستخدم بدلاً من ذلك، متوسط عامل كثافة الكربون الوطني للولايات المتحدة البالغ 0.385 كجم CO₂eq/KWh. يؤدي هذا إلى الصيغة التالية لأطنان انبعاثات الكربون:

tCO₂eq = MWh × 0.385.

نطبق نفس الصيغة على OPT وBLOOM للمقارنة العادلة. بالنسبة لـ OPT، نفترض أن التدريب استغرق 34 يوماً على 992 A100-80B (انظر سجلاتهم). أخيراً، نقدر أننا استخدمنا 2048 A100-80GB لفترة حوالي 5 أشهر لتطوير نماذجنا. هذا يعني أن تطوير هذه النماذج كان سيكلف حوالي 2,638 MWh بموجب افتراضاتنا، وانبعاث إجمالي قدره 1,015 tCO₂eq. نأمل أن يساعد إطلاق هذه النماذج في تقليل انبعاثات الكربون المستقبلية حيث تم التدريب بالفعل، وبعض النماذج صغيرة نسبياً ويمكن تشغيلها على وحدة معالجة رسومية واحدة.

## 7 الأعمال ذات الصلة

**نماذج اللغة** هي توزيعات احتمالية على تسلسلات من الكلمات أو الرموز أو الأحرف (Shannon, 1948, 1951). تم اعتبار هذه المهمة، التي غالباً ما يتم صياغتها على أنها تنبؤ بالرمز التالي، منذ فترة طويلة مشكلة أساسية في معالجة اللغة الطبيعية (Bahl et al., 1983; Brown et al., 1990). نظراً لأن Turing (1950) اقترح قياس ذكاء الآلة باستخدام اللغة من خلال "لعبة التقليد"، تم اقتراح نمذجة اللغة كمعيار لقياس التقدم نحو الذكاء الاصطناعي (Mahoney, 1999).

**المعمارية.** تقليدياً، كانت نماذج اللغة تعتمد على إحصائيات عد n-gram (Bahl et al., 1983)، وتم اقتراح تقنيات تنعيم مختلفة لتحسين تقدير الأحداث النادرة (Katz, 1987; Kneser and Ney, 1995). في العقدين الماضيين، تم تطبيق الشبكات العصبية بنجاح على مهمة نمذجة اللغة، بدءاً من نماذج التغذية الأمامية (Bengio et al., 2000)، والشبكات العصبية المتكررة (Elman, 1990; Mikolov et al., 2010) وLSTMs (Hochreiter and Schmidhuber, 1997; Graves, 2013). مؤخراً، أدت شبكات المحول، القائمة على الانتباه الذاتي، إلى تحسينات مهمة، خاصة لالتقاط التبعيات بعيدة المدى (Vaswani et al., 2017; Radford et al., 2018; Dai et al., 2019).

**التوسيع.** هناك تاريخ طويل من التوسيع لنماذج اللغة، لكل من أحجام النموذج ومجموعات البيانات. أظهر Brants et al. (2007) فوائد استخدام نماذج اللغة المدربة على 2 تريليون رمز، مما أدى إلى 300 مليار n-gram، على جودة الترجمة الآلية. بينما اعتمد هذا العمل على تقنية تنعيم بسيطة، تسمى Stupid Backoff، أظهر Heafield et al. (2013) لاحقاً كيفية توسيع تنعيم Kneser-Ney إلى بيانات على نطاق الويب. سمح هذا بتدريب نموذج 5-gram على 975 مليار رمز من CommonCrawl، مما أدى إلى نموذج بـ 500 مليار n-gram (Buck et al., 2014). قدم Chelba et al. (2013) معيار One Billion Word، مجموعة بيانات تدريب واسعة النطاق لقياس تقدم نماذج اللغة.

في سياق نماذج اللغة العصبية، حصل Jozefowicz et al. (2016) على نتائج متقدمة على معيار Billion Word من خلال توسيع LSTMs إلى مليار معامل. لاحقاً، أدى توسيع المحولات إلى تحسين في العديد من مهام معالجة اللغة الطبيعية. تشمل النماذج البارزة BERT (Devlin et al., 2018)، وGPT-2 (Radford et al., 2019)، وMegatron-LM (Shoeybi et al., 2019)، وT5 (Raffel et al., 2020). تم الحصول على اختراق كبير مع GPT-3 (Brown et al., 2020)، نموذج بـ 175 مليار معامل. أدى هذا إلى سلسلة من نماذج اللغة الكبيرة، مثل Jurassic-1 (Lieber et al., 2021)، وMegatron-Turing NLG (Smith et al., 2022)، وGopher (Rae et al., 2021)، وChinchilla (Hoffmann et al., 2022)، وPaLM (Chowdhery et al., 2022)، وOPT (Zhang et al., 2022)، وGLM (Zeng et al., 2022). درس Hestness et al. (2017) وRosenfeld et al. (2019) تأثير التوسيع على أداء نماذج التعلم العميق، مما أظهر وجود قوانين القوة بين أحجام النموذج ومجموعات البيانات وأداء النظام. اشتق Kaplan et al. (2020) قوانين القوة خصيصاً لنماذج اللغة القائمة على المحول، والتي تم تحسينها لاحقاً بواسطة Hoffmann et al. (2022)، من خلال تكييف جدول معدل التعلم عند توسيع مجموعات البيانات. أخيراً، درس Wei et al. (2022) تأثير التوسيع على قدرات نماذج اللغة الكبيرة.

---

### Translation Notes

- **Table referenced:** Table 15 (carbon footprint comparison)
- **Key concepts:** Power Usage Effectiveness (PUE), carbon intensity factor, Watt-hour (Wh), GPU-hours
- **Historical coverage:** Comprehensive review from Shannon (1948) to Wei et al. (2022)
- **Major milestones:** n-gram models → neural LMs → transformers → large-scale LLMs
- **Special handling:**
  - Chemical formulas (CO₂eq) preserved
  - Model names (BERT, GPT-2, GPT-3, etc.) kept in original form
  - Technical terms (Stupid Backoff, Kneser-Ney) kept as-is

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.85
- **Overall section score:** 0.86
