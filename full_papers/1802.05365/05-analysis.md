# Section 5: Analysis
## القسم 5: التحليل

**Section:** analysis
**Translation Quality:** 0.86
**Glossary Terms Used:** ablation analysis, contextualized representation, intrinsic evaluation, word sense disambiguation, part-of-speech tagging, layer weighting, polysemy, embedding, biLM, MT encoder, regularization, attention layer, sample efficiency, training set, development set

---

### English Version

This section provides an ablation analysis to validate our chief claims and to elucidate some interesting aspects of ELMo representations. Sec. 5.1 shows that using deep contextual representations in downstream tasks improves performance over previous work that uses just the top layer, regardless of whether they are produced from a biLM or MT encoder, and that ELMo representations provide the best overall performance. Sec. 5.3 explores the different types of contextual information captured in biLMs and uses two intrinsic evaluations to show that syntactic information is better represented at lower layers while semantic information is captured at higher layers, consistent with MT encoders. It also shows that our biLM consistently provides richer representations than CoVe. Additionally, we analyze the sensitivity to where ELMo is included in the task model (Sec. 5.2), training set size (Sec. 5.4), and visualize the ELMo learned weights across the tasks (Sec. 5.5).

**5.1 Alternate layer weighting schemes**

There are many alternatives to Equation 1 for combining the biLM layers. Previous work on contextual representations used only the last layer, whether it be from a biLM (Peters et al., 2017) or an MT encoder (CoVe; McCann et al., 2017). The choice of the regularization parameter λ is also important, as large values such as λ = 1 effectively reduce the weighting function to a simple average over the layers, while smaller values (e.g., λ = 0.001) allow the layer weights to vary.

Table 2 compares these alternatives for SQuAD, SNLI and SRL. Including representations from all layers improves overall performance over just using the last layer, and including contextual representations from the last layer improves performance over the baseline. For example, in the case of SQuAD, using just the last biLM layer improves development F1 by 3.9% over the baseline. Averaging all biLM layers instead of using just the last layer improves F1 another 0.3% (comparing "Last Only" to λ=1 columns), and allowing the task model to learn individual layer weights improves F1 another 0.2% (λ=1 vs. λ=0.001). A small λ is preferred in most cases with ELMo, although for NER, a task with a smaller training set, the results are insensitive to λ (not shown).

The overall trend is similar with CoVe but with smaller increases over the baseline. For SNLI, averaging all layers with λ=1 improves development accuracy from 88.2 to 88.7% over using just the last layer. SRL F1 increased a marginal 0.1% to 82.2 for the λ=1 case compared to using the last layer only.

**5.2 Where to include ELMo?**

All of the task architectures in this paper include word embeddings only as input to the lowest layer biRNN. However, we find that including ELMo at the output of the biRNN in task-specific architectures improves overall results for some tasks. As shown in Table 3, including ELMo at both the input and output layers for SNLI and SQuAD improves over just the input layer, but for SRL (and coreference resolution, not shown) performance is highest when it is included at just the input layer. One possible explanation for this result is that both the SNLI and SQuAD architectures use attention layers after the biRNN, so introducing ELMo at this layer allows the model to attend directly to the biLM's internal representations. In the SRL case, the task-specific context representations are likely more important than those from the biLM.

**Table 4:** Nearest neighbors to "play" using GloVe and the context embeddings from a biLM.

| Source | Nearest Neighbors |
|--------|-------------------|
| GloVe | play, playing, game, games, played, players, plays, player, Play, football, multiplayer |
| biLM | Chico Ruiz made a spectacular play on Alusik's grounder... / Kieffer, the only junior in the group, was commended for his ability to hit in the clutch, as well as his all-round excellent play. |
| biLM | Olivia De Havilland signed to do a Broadway play for Garson... / they were actors who had been handed fat roles in a successful play, and had talent enough to fill the roles competently, with nice understatement. |

**5.3 What information is captured by the biLM's representations?**

Since adding ELMo improves task performance over word vectors alone, the biLM's contextual representations must encode information generally useful for NLP tasks that is not captured in word vectors. Intuitively, the biLM must be disambiguating the meaning of words using their context. Consider "play", a highly polysemous word. The top of Table 4 lists nearest neighbors to "play" using GloVe vectors. They are spread across several parts of speech (e.g., "played", "playing" as verbs, and "player", "game" as nouns) but concentrated in the sports-related senses of "play". In contrast, the bottom two rows show nearest neighbor sentences from the SemCor dataset (see below) using the biLM context representation of "play" in the source sentence. In these cases, the biLM is able to disambiguate both the part of speech and word sense in the source sentence.

These observations can be quantified using an intrinsic evaluation of the contextual representations similar to Belinkov et al. (2017). To isolate the information encoded by the biLM, the representations are used to directly make predictions for a fine grained word sense disambiguation (WSD) task and a POS tagging task. Using this approach, it is also possible to compare to CoVe, and across each of the individual layers.

**Word sense disambiguation** Given a sentence, we can use the biLM representations to predict the sense of a target word using a simple 1-nearest neighbor approach, similar to Melamud et al. (2016). To do so, we first use the biLM to compute representations for all words in SemCor 3.0, our training corpus (Miller et al., 1994), and then take the average representation for each sense. At test time, we again use the biLM to compute representations for a given target word and take the nearest neighbor sense from the training set, falling back to the first sense from WordNet for lemmas not observed during training.

**Table 5:** All-words fine grained WSD F1. For CoVe and the biLM, we report scores for both the first and second layer biLSTMs.

| Model | F1 |
|-------|----|
| WordNet 1st Sense Baseline | 65.9 |
| Raganato et al. (2017a) | 69.9 |
| Iacobacci et al. (2016) | 70.1 |
| CoVe, First Layer | 59.4 |
| CoVe, Second Layer | 64.7 |
| biLM, First layer | 67.4 |
| biLM, Second layer | 69.0 |

Table 5 compares WSD results using the evaluation framework from Raganato et al. (2017b) across the same suite of four test sets in Raganato et al. (2017a). Overall, the biLM top layer representations have F1 of 69.0 and are better at WSD than the first layer. This is competitive with a state-of-the-art WSD-specific supervised model using hand crafted features (Iacobacci et al., 2016) and a task specific biLSTM that is also trained with auxiliary coarse-grained semantic labels and POS tags (Raganato et al., 2017a). The CoVe biLSTM layers follow a similar pattern to those from the biLM (higher overall performance at the second layer compared to the first); however, our biLM outperforms the CoVe biLSTM, which trails the WordNet first sense baseline.

**POS tagging** To examine whether the biLM captures basic syntax, we used the context representations as input to a linear classifier that predicts POS tags with the Wall Street Journal portion of the Penn Treebank (PTB) (Marcus et al., 1993). As the linear classifier adds only a small amount of model capacity, this is a direct test of the biLM representations.

**Table 6:** Test set POS tagging accuracies for PTB. For CoVe and the biLM, we report scores for both the first and second layer biLSTMs.

| Model | Acc. |
|-------|------|
| Collobert et al. (2011) | 97.3 |
| Ma and Hovy (2016) | 97.6 |
| Ling et al. (2015) | 97.8 |
| CoVe, First Layer | 93.3 |
| CoVe, Second Layer | 92.8 |
| biLM, First Layer | 97.3 |
| biLM, Second Layer | 96.8 |

Similar to WSD, the biLM representations are competitive with carefully tuned, task specific biLSTMs (Ling et al., 2015; Ma and Hovy, 2016). However, unlike WSD, accuracies using the first biLM layer are higher than the top layer, consistent with results from deep biLSTMs in multi-task training (Søgaard and Goldberg, 2016; Hashimoto et al., 2017) and MT (Belinkov et al., 2017). CoVe POS tagging accuracies follow the same pattern as those from the biLM, and just like for WSD, the biLM achieves higher accuracies than the CoVe encoder.

**Implications for supervised tasks** Taken together, these experiments confirm different layers in the biLM represent different types of information and explain why including all biLM layers is important for the highest performance in downstream tasks. In addition, the biLM's representations are more transferable to WSD and POS tagging than those in CoVe, helping to illustrate why ELMo outperforms CoVe in downstream tasks.

**5.4 Sample efficiency**

Adding ELMo to a model increases the sample efficiency considerably, both in terms of number of parameter updates to reach state-of-the-art performance and the overall training set size. For example, the SRL model reaches a maximum development F1 after 486 epochs of training without ELMo. After adding ELMo, the model exceeds the baseline maximum at epoch 10, a 98% relative decrease in the number of updates needed to reach the same level of performance.

In addition, ELMo-enhanced models use smaller training sets more efficiently than models without ELMo. Figure 1 compares the performance of baseline models with and without ELMo as the percentage of the full training set is varied from 0.1% to 100%. Improvements with ELMo are largest for smaller training sets and significantly reduce the amount of training data needed to reach a given level of performance. In the SRL case, the ELMo model with 1% of the training set has about the same F1 as the baseline model with 10% of the training set.

**5.5 Visualization of learned weights**

Figure 2 visualizes the softmax-normalized learned layer weights. At the input layer, the task model favors the first biLSTM layer. For coreference and SQuAD, this is strongly favored, but the distribution is less peaked for the other tasks. The output layer weights are relatively balanced, with a slight preference for the lower layers.

---

### النسخة العربية

يوفر هذا القسم تحليل استئصال للتحقق من صحة ادعاءاتنا الرئيسية ولتوضيح بعض الجوانب المثيرة للاهتمام لتمثيلات ELMo. يُظهر القسم 5.1 أن استخدام التمثيلات السياقية العميقة في المهام النهائية يحسن الأداء على الأعمال السابقة التي تستخدم الطبقة العليا فقط، بغض النظر عما إذا كانت منتجة من نموذج لغة ثنائي الاتجاه (biLM) أو مشفر ترجمة آلية (MT)، وأن تمثيلات ELMo توفر أفضل أداء إجمالي. يستكشف القسم 5.3 الأنواع المختلفة من المعلومات السياقية الملتقطة في نماذج اللغة ثنائية الاتجاه ويستخدم تقييمين جوهريين لإظهار أن المعلومات التركيبية ممثلة بشكل أفضل في الطبقات الأدنى بينما يتم التقاط المعلومات الدلالية في الطبقات الأعلى، بما يتسق مع مشفرات الترجمة الآلية. يُظهر أيضاً أن نموذج اللغة ثنائي الاتجاه لدينا يوفر باستمرار تمثيلات أغنى من CoVe. بالإضافة إلى ذلك، نحلل الحساسية لمكان تضمين ELMo في نموذج المهمة (القسم 5.2)، وحجم مجموعة التدريب (القسم 5.4)، ونرسم بصرياً أوزان ELMo المتعلمة عبر المهام (القسم 5.5).

**5.1 مخططات ترجيح الطبقات البديلة**

هناك العديد من البدائل للمعادلة 1 لدمج طبقات نموذج اللغة ثنائي الاتجاه. الأعمال السابقة على التمثيلات السياقية استخدمت الطبقة الأخيرة فقط، سواء كانت من نموذج لغة ثنائي الاتجاه (Peters et al., 2017) أو مشفر ترجمة آلية (CoVe; McCann et al., 2017). اختيار معامل التنظيم λ مهم أيضاً، حيث أن القيم الكبيرة مثل λ = 1 تقلل بشكل فعال دالة الترجيح إلى متوسط بسيط على الطبقات، بينما القيم الأصغر (مثل λ = 0.001) تسمح لأوزان الطبقات بالتباين.

يقارن الجدول 2 هذه البدائل لـ SQuAD وSNLI وSRL. تضمين التمثيلات من جميع الطبقات يحسن الأداء الإجمالي مقارنة باستخدام الطبقة الأخيرة فقط، وتضمين التمثيلات السياقية من الطبقة الأخيرة يحسن الأداء على خط الأساس. على سبيل المثال، في حالة SQuAD، استخدام الطبقة الأخيرة من نموذج اللغة ثنائي الاتجاه فقط يحسن F1 للتطوير بنسبة 3.9% على خط الأساس. متوسط جميع طبقات نموذج اللغة ثنائي الاتجاه بدلاً من استخدام الطبقة الأخيرة فقط يحسن F1 بنسبة 0.3% إضافية (مقارنة أعمدة "الأخيرة فقط" مع λ=1)، والسماح لنموذج المهمة بتعلم أوزان الطبقات الفردية يحسن F1 بنسبة 0.2% إضافية (λ=1 مقابل λ=0.001). يُفضل λ صغير في معظم الحالات مع ELMo، على الرغم من أنه بالنسبة لـ NER، وهي مهمة بمجموعة تدريب أصغر، فإن النتائج غير حساسة لـ λ (لم تُظهر).

الاتجاه العام مشابه مع CoVe لكن مع زيادات أصغر على خط الأساس. بالنسبة لـ SNLI، متوسط جميع الطبقات مع λ=1 يحسن دقة التطوير من 88.2 إلى 88.7% مقارنة باستخدام الطبقة الأخيرة فقط. زادت F1 لـ SRL بنسبة هامشية 0.1% إلى 82.2 لحالة λ=1 مقارنة باستخدام الطبقة الأخيرة فقط.

**5.2 أين يتم تضمين ELMo؟**

جميع معماريات المهام في هذا البحث تتضمن تضمينات الكلمات فقط كإدخال لطبقة biRNN الأدنى. ومع ذلك، نجد أن تضمين ELMo في إخراج biRNN في المعماريات الخاصة بالمهمة يحسن النتائج الإجمالية لبعض المهام. كما هو موضح في الجدول 3، تضمين ELMo في كل من طبقات الإدخال والإخراج لـ SNLI وSQuAD يحسن على طبقة الإدخال فقط، ولكن بالنسبة لـ SRL (وحل الإحالة المرجعية، لم يُظهر) يكون الأداء أعلى عندما يتم تضمينه في طبقة الإدخال فقط. أحد التفسيرات المحتملة لهذه النتيجة هو أن كلاً من معماريات SNLI وSQuAD تستخدم طبقات انتباه بعد biRNN، لذا فإن إدخال ELMo في هذه الطبقة يسمح للنموذج بالانتباه مباشرة إلى التمثيلات الداخلية لنموذج اللغة ثنائي الاتجاه. في حالة SRL، من المرجح أن تمثيلات السياق الخاصة بالمهمة أكثر أهمية من تلك الخاصة بنموذج اللغة ثنائي الاتجاه.

**الجدول 4:** أقرب الجيران لـ "play" باستخدام GloVe والتضمينات السياقية من نموذج لغة ثنائي الاتجاه.

| المصدر | أقرب الجيران |
|--------|---------------|
| GloVe | play, playing, game, games, played, players, plays, player, Play, football, multiplayer |
| biLM | Chico Ruiz made a spectacular play on Alusik's grounder... / Kieffer, the only junior in the group, was commended for his ability to hit in the clutch, as well as his all-round excellent play. |
| biLM | Olivia De Havilland signed to do a Broadway play for Garson... / they were actors who had been handed fat roles in a successful play, and had talent enough to fill the roles competently, with nice understatement. |

**5.3 ما المعلومات التي تلتقطها تمثيلات نموذج اللغة ثنائي الاتجاه؟**

بما أن إضافة ELMo تحسن أداء المهمة على متجهات الكلمات وحدها، فإن التمثيلات السياقية لنموذج اللغة ثنائي الاتجاه يجب أن تشفر معلومات مفيدة بشكل عام لمهام معالجة اللغة الطبيعية التي لا يتم التقاطها في متجهات الكلمات. بديهياً، يجب أن يكون نموذج اللغة ثنائي الاتجاه يزيل الغموض عن معنى الكلمات باستخدام سياقها. فكر في "play"، وهي كلمة عالية التعدد في المعاني. يسرد أعلى الجدول 4 أقرب الجيران لـ "play" باستخدام متجهات GloVe. إنها منتشرة عبر عدة أجزاء من الكلام (مثل "played"، "playing" كأفعال، و"player"، "game" كأسماء) لكنها مركزة في المعاني المتعلقة بالرياضة لـ "play". في المقابل، يُظهر الصفان السفليان أقرب الجمل المجاورة من مجموعة بيانات SemCor (انظر أدناه) باستخدام التمثيل السياقي لنموذج اللغة ثنائي الاتجاه لـ "play" في الجملة المصدر. في هذه الحالات، نموذج اللغة ثنائي الاتجاه قادر على إزالة الغموض عن كل من جزء الكلام ومعنى الكلمة في الجملة المصدر.

يمكن تحديد هذه الملاحظات كمياً باستخدام تقييم جوهري للتمثيلات السياقية مشابه لـ Belinkov et al. (2017). لعزل المعلومات المشفرة بواسطة نموذج اللغة ثنائي الاتجاه، تُستخدم التمثيلات مباشرة لعمل تنبؤات لمهمة توضيح معنى الكلمة الدقيقة (WSD) ومهمة وسم أجزاء الكلام (POS). باستخدام هذا النهج، من الممكن أيضاً المقارنة مع CoVe، وعبر كل طبقة فردية.

**توضيح معنى الكلمة** بالنظر إلى جملة، يمكننا استخدام تمثيلات نموذج اللغة ثنائي الاتجاه للتنبؤ بمعنى كلمة مستهدفة باستخدام نهج بسيط لأقرب جار واحد، مشابه لـ Melamud et al. (2016). للقيام بذلك، نستخدم أولاً نموذج اللغة ثنائي الاتجاه لحساب التمثيلات لجميع الكلمات في SemCor 3.0، مدونتنا التدريبية (Miller et al., 1994)، ثم نأخذ متوسط التمثيل لكل معنى. في وقت الاختبار، نستخدم مرة أخرى نموذج اللغة ثنائي الاتجاه لحساب التمثيلات لكلمة مستهدفة معينة ونأخذ أقرب معنى جار من مجموعة التدريب، مع الرجوع إلى المعنى الأول من WordNet للموالفات التي لم تُلاحظ أثناء التدريب.

**الجدول 5:** F1 لتوضيح معنى الكلمة الدقيقة لجميع الكلمات. بالنسبة لـ CoVe ونموذج اللغة ثنائي الاتجاه، نُبلغ عن النتائج لكل من طبقات biLSTMs الأولى والثانية.

| النموذج | F1 |
|--------|----|
| خط أساس المعنى الأول لـ WordNet | 65.9 |
| Raganato et al. (2017a) | 69.9 |
| Iacobacci et al. (2016) | 70.1 |
| CoVe، الطبقة الأولى | 59.4 |
| CoVe، الطبقة الثانية | 64.7 |
| biLM، الطبقة الأولى | 67.4 |
| biLM، الطبقة الثانية | 69.0 |

يقارن الجدول 5 نتائج WSD باستخدام إطار التقييم من Raganato et al. (2017b) عبر نفس مجموعة اختبارات الأربعة في Raganato et al. (2017a). بشكل عام، تمثيلات الطبقة العليا لنموذج اللغة ثنائي الاتجاه لها F1 تبلغ 69.0 وهي أفضل في WSD من الطبقة الأولى. هذا تنافسي مع نموذج مُشرف خاص بـ WSD حديث يستخدم ميزات مصنوعة يدوياً (Iacobacci et al., 2016) وbiLSTM خاص بالمهمة يتم تدريبه أيضاً بتسميات دلالية خشنة الحبيبات مساعدة ووسوم POS (Raganato et al., 2017a). تتبع طبقات CoVe biLSTM نمطاً مشابهاً لتلك الخاصة بنموذج اللغة ثنائي الاتجاه (أداء إجمالي أعلى في الطبقة الثانية مقارنة بالأولى)؛ ومع ذلك، يتفوق نموذج اللغة ثنائي الاتجاه لدينا على CoVe biLSTM، الذي يتخلف عن خط أساس المعنى الأول لـ WordNet.

**وسم أجزاء الكلام** لفحص ما إذا كان نموذج اللغة ثنائي الاتجاه يلتقط البنية التركيبية الأساسية، استخدمنا تمثيلات السياق كإدخال لمصنف خطي يتنبأ بوسوم POS مع جزء وول ستريت جورنال من Penn Treebank (PTB) (Marcus et al., 1993). نظراً لأن المصنف الخطي يضيف فقط كمية صغيرة من سعة النموذج، فهذا اختبار مباشر لتمثيلات نموذج اللغة ثنائي الاتجاه.

**الجدول 6:** دقة وسم POS لمجموعة الاختبار لـ PTB. بالنسبة لـ CoVe ونموذج اللغة ثنائي الاتجاه، نُبلغ عن النتائج لكل من طبقات biLSTMs الأولى والثانية.

| النموذج | الدقة |
|---------|------|
| Collobert et al. (2011) | 97.3 |
| Ma and Hovy (2016) | 97.6 |
| Ling et al. (2015) | 97.8 |
| CoVe، الطبقة الأولى | 93.3 |
| CoVe، الطبقة الثانية | 92.8 |
| biLM، الطبقة الأولى | 97.3 |
| biLM، الطبقة الثانية | 96.8 |

مشابهة لـ WSD، تمثيلات نموذج اللغة ثنائي الاتجاه تنافسية مع biLSTMs خاصة بالمهام ومضبوطة بعناية (Ling et al., 2015; Ma and Hovy, 2016). ومع ذلك، على عكس WSD، فإن الدقة باستخدام طبقة نموذج اللغة ثنائي الاتجاه الأولى أعلى من الطبقة العليا، بما يتسق مع النتائج من biLSTMs العميقة في التدريب متعدد المهام (Søgaard and Goldberg, 2016; Hashimoto et al., 2017) والترجمة الآلية (Belinkov et al., 2017). تتبع دقة وسم POS لـ CoVe نفس النمط كتلك من نموذج اللغة ثنائي الاتجاه، ومثل WSD تماماً، يحقق نموذج اللغة ثنائي الاتجاه دقة أعلى من مشفر CoVe.

**الآثار المترتبة على المهام المُشرفة** معاً، تؤكد هذه التجارب أن الطبقات المختلفة في نموذج اللغة ثنائي الاتجاه تمثل أنواعاً مختلفة من المعلومات وتشرح لماذا يعد تضمين جميع طبقات نموذج اللغة ثنائي الاتجاه مهماً لأعلى أداء في المهام النهائية. بالإضافة إلى ذلك، تمثيلات نموذج اللغة ثنائي الاتجاه أكثر قابلية للنقل إلى WSD ووسم POS من تلك في CoVe، مما يساعد في توضيح سبب تفوق ELMo على CoVe في المهام النهائية.

**5.4 كفاءة العينة**

إضافة ELMo إلى نموذج يزيد كفاءة العينة بشكل كبير، سواء من حيث عدد تحديثات المعاملات للوصول إلى أداء أحدث ما توصل إليه العلم وحجم مجموعة التدريب الإجمالي. على سبيل المثال، يصل نموذج SRL إلى أقصى F1 للتطوير بعد 486 حقبة من التدريب بدون ELMo. بعد إضافة ELMo، يتجاوز النموذج الحد الأقصى لخط الأساس في الحقبة 10، وهو انخفاض نسبي بنسبة 98% في عدد التحديثات اللازمة للوصول إلى نفس مستوى الأداء.

بالإضافة إلى ذلك، تستخدم النماذج المحسنة بـ ELMo مجموعات التدريب الأصغر بشكل أكثر كفاءة من النماذج بدون ELMo. يقارن الشكل 1 أداء نماذج خط الأساس مع وبدون ELMo حيث تختلف نسبة مجموعة التدريب الكاملة من 0.1% إلى 100%. التحسينات مع ELMo هي الأكبر لمجموعات التدريب الأصغر وتقلل بشكل كبير من كمية بيانات التدريب اللازمة للوصول إلى مستوى أداء معين. في حالة SRL، نموذج ELMo مع 1% من مجموعة التدريب لديه حوالي نفس F1 كنموذج خط الأساس مع 10% من مجموعة التدريب.

**5.5 تصور الأوزان المتعلمة**

يرسم الشكل 2 بصرياً أوزان الطبقات المتعلمة المنظمة بواسطة softmax. في طبقة الإدخال، يفضل نموذج المهمة طبقة biLSTM الأولى. بالنسبة للإحالة المرجعية وSQuAD، يتم تفضيل هذا بقوة، لكن التوزيع أقل ذروة للمهام الأخرى. أوزان طبقة الإخراج متوازنة نسبياً، مع تفضيل طفيف للطبقات الأدنى.

---

### Translation Notes

- **Figures referenced:** Figure 1 (training set size comparison), Figure 2 (layer weight visualization), Table 4 (nearest neighbors), Table 5 (WSD results), Table 6 (POS tagging results)
- **Key terms introduced:** ablation analysis, GloVe, SemCor, WordNet, Penn Treebank (PTB), layer weighting, nearest neighbor, sample efficiency, intrinsic evaluation, linear classifier
- **Equations:** Reference to Equation 1 from Section 3
- **Citations:** Peters et al. 2017, McCann et al. 2017, Belinkov et al. 2017, Melamud et al. 2016, Miller et al. 1994, Raganato et al. 2017a, Raganato et al. 2017b, Iacobacci et al. 2016, Marcus et al. 1993, Collobert et al. 2011, Ma and Hovy 2016, Ling et al. 2015, Søgaard and Goldberg 2016, Hashimoto et al. 2017
- **Special handling:**
  - Preserved technical dataset names (SemCor, WordNet, PTB)
  - Maintained table structures with Arabic headers
  - Kept numerical results and percentages exact
  - Used consistent terminology for metrics and evaluations

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.86

### Back-Translation Validation (Opening Paragraph)

This section provides an ablation analysis to validate our main claims and to elucidate some interesting aspects of ELMo representations. Section 5.1 shows that using deep contextual representations in downstream tasks improves performance over previous work that uses just the top layer, regardless of whether they are produced from a biLM or MT encoder, and that ELMo representations provide the best overall performance. Section 5.3 explores the different types of contextual information captured in biLMs and uses two intrinsic evaluations to show that syntactic information is better represented at lower layers while semantic information is captured at higher layers, consistent with MT encoders. It also shows that our biLM consistently provides richer representations than CoVe.

**Validation:** ✓ Excellent semantic match with original
