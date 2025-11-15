# Abstract
## الملخص

**Section:** abstract
**Translation Quality:** 0.92
**Glossary Terms Used:** deep neural networks, long short-term memory, sequence, vector, BLEU score, translation, optimization, phrase-based, representations, word order

---

### English Version

Deep Neural Networks (DNNs) are powerful models that have achieved excellent performance on difficult learning tasks. Although DNNs work well whenever large labeled training sets are available, they cannot be used to map sequences to sequences. In this paper, we present a general end-to-end approach to sequence learning that makes minimal assumptions on the sequence structure. Our method uses a multilayered Long Short-Term Memory (LSTM) to map the input sequence to a vector of a fixed dimensionality, and then another deep LSTM to decode the target sequence from the vector. Our main result is that on an English to French translation task from the WMT'14 dataset, the translations produced by the LSTM achieve a BLEU score of 34.8 on the entire test set, where the LSTM's BLEU score was penalized on out-of-vocabulary words. Additionally, the LSTM did not have difficulty on long sentences. For comparison, a phrase-based SMT system achieves a BLEU score of 33.3 on the same dataset. When we used the LSTM to rerank the 1000 hypotheses produced by the aforementioned SMT system, its BLEU score increases to 36.5, which is close to the previous best result on this task. The LSTM also learned sensible phrase and sentence representations that are sensitive to word order and are relatively invariant to the active and the passive voice. Finally, we found that reversing the order of the words in all source sentences (but not target sentences) improved the LSTM's performance markedly, because doing so introduced many short term dependencies between the source and the target sentence which made the optimization problem easier.

---

### النسخة العربية

الشبكات العصبية العميقة (DNNs) هي نماذج قوية حققت أداءً ممتازاً في مهام التعلم الصعبة. على الرغم من أن الشبكات العصبية العميقة تعمل بشكل جيد عندما تتوفر مجموعات تدريب كبيرة مُعنونة، إلا أنها لا يمكن استخدامها لتخطيط التسلسلات إلى تسلسلات. في هذا البحث، نقدم نهجاً عاماً شاملاً من طرف إلى طرف لتعلم التسلسلات يضع افتراضات قليلة على بنية التسلسل. تستخدم طريقتنا ذاكرة طويلة قصيرة المدى (LSTM) متعددة الطبقات لتخطيط تسلسل الإدخال إلى متجه ذي بُعد ثابت، ثم تستخدم LSTM عميقة أخرى لفك تشفير التسلسل المستهدف من المتجه. نتيجتنا الرئيسية هي أنه في مهمة الترجمة من الإنجليزية إلى الفرنسية من مجموعة بيانات WMT'14، حققت الترجمات التي أنتجتها LSTM درجة BLEU قدرها 34.8 على مجموعة الاختبار بأكملها، حيث تم تخفيض درجة BLEU الخاصة بـ LSTM على الكلمات غير الموجودة في المفردات. بالإضافة إلى ذلك، لم تواجه LSTM صعوبة في الجمل الطويلة. للمقارنة، يحقق نظام الترجمة الآلية الإحصائية القائم على العبارات (SMT) درجة BLEU قدرها 33.3 على نفس مجموعة البيانات. عندما استخدمنا LSTM لإعادة ترتيب الفرضيات الـ 1000 التي أنتجها نظام SMT المذكور، ارتفعت درجة BLEU إلى 36.5، وهي قريبة من أفضل نتيجة سابقة في هذه المهمة. تعلمت LSTM أيضاً تمثيلات معقولة للعبارات والجمل حساسة لترتيب الكلمات ومستقرة نسبياً تجاه الصيغة المبنية للمعلوم والمبنية للمجهول. أخيراً، وجدنا أن عكس ترتيب الكلمات في جميع الجمل المصدر (وليس الجمل المستهدفة) حسّن أداء LSTM بشكل ملحوظ، لأن ذلك أدخل العديد من التبعيات قصيرة المدى بين الجملة المصدر والجملة المستهدفة مما جعل مسألة التحسين أسهل.

---

### Quality Metrics

- Semantic equivalence: 0.94
- Technical accuracy: 0.92
- Readability: 0.91
- Glossary consistency: 0.93
- **Overall section score:** 0.92
