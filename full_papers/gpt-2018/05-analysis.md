# Section 5: Analysis
## القسم 5: التحليل

**Section:** Analysis
**Translation Quality:** 0.87
**Glossary Terms Used:** transformer, LSTM, pre-training, fine-tuning, zero-shot, embeddings, auxiliary objective, ablation, generative model, language model

---

### English Version

**Impact of number of layers transferred** We observed the impact of transferring a variable number of layers from unsupervised pre-training to the supervised target task. Figure 2(left) illustrates the performance of our approach on MultiNLI and RACE as a function of the number of layers transferred. We observe the standard result that transferring embeddings improves performance and that each transformer layer provides further benefits up to 9% for full transfer on MultiNLI. This indicates that each layer in the pre-trained model contains useful functionality for solving target tasks.

**Zero-shot Behaviors** We'd like to better understand why language model pre-training of transformers is effective. A hypothesis is that the underlying generative model learns to perform many of the tasks we evaluate on in order to improve its language modeling capability and that the more structured attentional memory of the transformer assists in transfer compared to LSTMs. We designed a series of heuristic solutions that use the underlying generative model to perform tasks without supervised finetuning. We visualize the effectiveness of these heuristic solutions over the course of generative pre-training in Fig 2(right). We observe the performance of these heuristics is stable and steadily increases over training suggesting that generative pretraining supports the learning of a wide variety of task relevant functionality. We also observe the LSTM exhibits higher variance in its zero-shot performance suggesting that the inductive bias of the Transformer architecture assists in transfer.

For CoLA (linguistic acceptability), examples are scored as the average token log-probability the generative model assigns and predictions are made by thresholding. For SST-2 (sentiment analysis), we append the token very to each example and restrict the language model's output distribution to only the words positive and negative and guess the token it assigns higher probability to as the prediction. For RACE (question answering), we pick the answer the generative model assigns the highest average token log-probability when conditioned on the document and question. For DPRD [46] (winograd schemas), we replace the definite pronoun with the two possible referrents and predict the resolution that the generative model assigns higher average token log-probability to the rest of the sequence after the substitution.

**Ablation studies** We perform three different ablation studies (Table 5). First, we examine the performance of our method without the auxiliary LM objective during fine-tuning. We observe that the auxiliary objective helps on the NLI tasks and QQP. Overall, the trend suggests that larger datasets benefit from the auxiliary objective but smaller datasets do not. Second, we analyze the effect of the Transformer by comparing it with a single layer 2048 unit LSTM using the same framework. We observe a 5.6 average score drop when using the LSTM instead of the Transformer. The LSTM only outperforms the Transformer on one dataset – MRPC. Finally, we also compare with our transformer architecture directly trained on supervised target tasks, without pre-training. We observe that the lack of pre-training hurts performance across all the tasks, resulting in a 14.8% decrease compared to our full model.

---

### النسخة العربية

**تأثير عدد الطبقات المنقولة** لاحظنا تأثير نقل عدد متغير من الطبقات من التدريب المسبق غير الموجه إلى المهمة المستهدفة الموجهة. يوضح الشكل 2 (يسار) أداء نهجنا على MultiNLI و RACE كدالة لعدد الطبقات المنقولة. نلاحظ النتيجة القياسية بأن نقل التضمينات يحسن الأداء وأن كل طبقة من طبقات المحوّل توفر فوائد إضافية تصل إلى 9٪ للنقل الكامل على MultiNLI. يشير هذا إلى أن كل طبقة في النموذج المُدرب مسبقاً تحتوي على وظائف مفيدة لحل المهام المستهدفة.

**سلوكيات الصفر-لقطة** نود أن نفهم بشكل أفضل لماذا يكون التدريب المسبق لنموذج اللغة للمحولات فعالاً. الفرضية هي أن النموذج التوليدي الأساسي يتعلم أداء العديد من المهام التي نُقيّمها من أجل تحسين قدرته على نمذجة اللغة وأن الذاكرة الانتباهية الأكثر تنظيماً للمحوّل تساعد في النقل مقارنة بـ LSTM. صممنا سلسلة من الحلول الاستدلالية التي تستخدم النموذج التوليدي الأساسي لأداء المهام دون ضبط دقيق موجه. نُصور فعالية هذه الحلول الاستدلالية على مدار التدريب المسبق التوليدي في الشكل 2 (يمين). نلاحظ أن أداء هذه الاستدلالات مستقر ويزداد بشكل مطرد خلال التدريب مما يشير إلى أن التدريب المسبق التوليدي يدعم تعلم مجموعة واسعة من الوظائف ذات الصلة بالمهام. نلاحظ أيضاً أن LSTM يُظهر تباينا أعلى في أدائه في الصفر-لقطة مما يشير إلى أن التحيز الاستقرائي لمعمارية المحوّل يساعد في النقل.

بالنسبة لـ CoLA (المقبولية اللغوية)، يتم تسجيل الأمثلة كمتوسط احتمال اللوغاريتم للرموز الذي يخصصه النموذج التوليدي ويتم إجراء التنبؤات بالعتبة. بالنسبة لـ SST-2 (تحليل المشاعر)، نُلحق الرمز "very" بكل مثال ونقيد توزيع إخراج نموذج اللغة على الكلمات "positive" و "negative" فقط ونخمن الرمز الذي يخصص له احتمالية أعلى كتنبؤ. بالنسبة لـ RACE (الإجابة على الأسئلة)، نختار الإجابة التي يخصص لها النموذج التوليدي أعلى متوسط احتمال لوغاريتم للرموز عند الاعتماد على المستند والسؤال. بالنسبة لـ DPRD [46] (مخططات Winograd)، نستبدل الضمير المحدد بالمُحالين المحتملين ونتنبأ بالقرار الذي يخصص له النموذج التوليدي احتمال لوغاريتم رموز متوسط أعلى لبقية التسلسل بعد الاستبدال.

**دراسات الاستئصال** نُجري ثلاث دراسات استئصال مختلفة (الجدول 5). أولاً، نفحص أداء طريقتنا بدون هدف نموذج اللغة المساعد أثناء الضبط الدقيق. نلاحظ أن الهدف المساعد يساعد في مهام NLI و QQP. بشكل عام، يشير الاتجاه إلى أن مجموعات البيانات الأكبر تستفيد من الهدف المساعد ولكن مجموعات البيانات الأصغر لا تستفيد. ثانياً، نحلل تأثير المحوّل بمقارنته مع LSTM من طبقة واحدة 2048 وحدة باستخدام نفس الإطار. نلاحظ انخفاضاً متوسطاً في الدرجة قدره 5.6 عند استخدام LSTM بدلاً من المحوّل. يتفوق LSTM على المحوّل في مجموعة بيانات واحدة فقط - MRPC. أخيراً، نقارن أيضاً بمعمارية المحوّل الخاصة بنا المُدربة مباشرة على المهام المستهدفة الموجهة، بدون تدريب مسبق. نلاحظ أن عدم وجود التدريب المسبق يضر بالأداء عبر جميع المهام، مما يؤدي إلى انخفاض بنسبة 14.8٪ مقارنة بنموذجنا الكامل.

---

### Translation Notes

- **Figures referenced:** Figure 2 (left: layer transfer impact, right: zero-shot performance evolution)
- **Tables referenced:** Table 5 (ablation studies results)
- **Key terms introduced:**
  - Variable number = عدد متغير
  - Zero-shot = الصفر-لقطة
  - Heuristic solutions = الحلول الاستدلالية
  - Attentional memory = الذاكرة الانتباهية
  - Inductive bias = التحيز الاستقرائي
  - Log-probability = احتمال اللوغاريتم
  - Thresholding = بالعتبة
  - Sentiment analysis = تحليل المشاعر
  - Winograd schemas = مخططات Winograd
  - Definite pronoun = الضمير المحدد
  - Referrents = المُحالين
  - Ablation studies = دراسات الاستئصال

- **Specific tasks mentioned:** CoLA, SST-2, RACE, DPRD (with Arabic transliterations where appropriate)
- **Numerical results preserved:** 9%, 5.6, 14.8%
- **Citations preserved:** [46]

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
