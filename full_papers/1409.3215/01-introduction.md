# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** deep neural networks, backpropagation, sequence, vector, LSTM, recurrent neural network, language model, attention mechanism, beam search, SMT, BLEU score

---

### English Version

Deep Neural Networks (DNNs) are extremely powerful machine learning models that achieve excellent performance on difficult problems such as speech recognition [13, 7] and visual object recognition [19, 6, 21, 20]. DNNs are powerful because they can perform arbitrary parallel computation for a modest number of steps. A surprising example of the power of DNNs is their ability to sort N N-bit numbers using only 2 hidden layers of quadratic size [27]. So, while neural networks are related to conventional statistical models, they learn an intricate computation. Furthermore, large DNNs can be trained with supervised backpropagation whenever the labeled training set has enough information to specify the network's parameters. Thus, if there exists a parameter setting of a large DNN that achieves good results (for example, because humans can solve the task very rapidly), supervised backpropagation will find these parameters and solve the problem.

Despite their flexibility and power, DNNs can only be applied to problems whose inputs and targets can be sensibly encoded with vectors of fixed dimensionality. It is a significant limitation, since many important problems are best expressed with sequences whose lengths are not known a-priori. For example, speech recognition and machine translation are sequential problems. Likewise, question answering can also be seen as mapping a sequence of words representing the question to a sequence of words representing the answer. It is therefore clear that a domain-independent method that learns to map sequences to sequences would be useful.

Sequences pose a challenge for DNNs because they require that the dimensionality of the inputs and outputs is known and fixed. In this paper, we show that a straightforward application of the Long Short-Term Memory (LSTM) architecture [16] can solve general sequence to sequence problems. The idea is to use one LSTM to read the input sequence, one timestep at a time, to obtain large fixed-dimensional vector representation, and then to use another LSTM to extract the output sequence from that vector (fig. 1). The second LSTM is essentially a recurrent neural network language model [28, 23, 30] except that it is conditioned on the input sequence. The LSTM's ability to successfully learn on data with long range temporal dependencies makes it a natural choice for this application due to the considerable time lag between the inputs and their corresponding outputs (fig. 1).

There have been a number of related attempts to address the general sequence to sequence learning problem with neural networks. Our approach is closely related to Kalchbrenner and Blunsom [18] who were the first to map the entire input sentence to vector, and is related to Cho et al. [5] although the latter was used only for rescoring hypotheses produced by a phrase-based system. Graves [10] introduced a novel differentiable attention mechanism that allows neural networks to focus on different parts of their input, and an elegant variant of this idea was successfully applied to machine translation by Bahdanau et al. [2]. The Connectionist Sequence Classification is another popular technique for mapping sequences to sequences with neural networks, but it assumes a monotonic alignment between the inputs and the outputs [11].

The main result of this work is the following. On the WMT'14 English to French translation task, we obtained a BLEU score of 34.81 by directly extracting translations from an ensemble of 5 deep LSTMs (with 384M parameters and 8,000 dimensional state each) using a simple left-to-right beam-search decoder. This is by far the best result achieved by direct translation with large neural networks. For comparison, the BLEU score of an SMT baseline on this dataset is 33.30 [29]. The 34.81 BLEU score was achieved by an LSTM with a vocabulary of 80k words, so the score was penalized whenever the reference translation contained a word not covered by these 80k. This result shows that a relatively unoptimized small-vocabulary neural network architecture which has much room for improvement outperforms a phrase-based SMT system.

Finally, we used the LSTM to rescore the publicly available 1000-best lists of the SMT baseline on the same task [29]. By doing so, we obtained a BLEU score of 36.5, which improves the baseline by 3.2 BLEU points and is close to the previous best published result on this task (which is 37.0 [9]).

Surprisingly, the LSTM did not suffer on very long sentences, despite the recent experience of other researchers with related architectures [26]. We were able to do well on long sentences because we reversed the order of words in the source sentence but not the target sentences in the training and test set. By doing so, we introduced many short term dependencies that made the optimization problem much simpler (see sec. 2 and 3.3). As a result, SGD could learn LSTMs that had no trouble with long sentences. The simple trick of reversing the words in the source sentence is one of the key technical contributions of this work.

A useful property of the LSTM is that it learns to map an input sentence of variable length into a fixed-dimensional vector representation. Given that translations tend to be paraphrases of the source sentences, the translation objective encourages the LSTM to find sentence representations that capture their meaning, as sentences with similar meanings are close to each other while different sentences meanings will be far. A qualitative evaluation supports this claim, showing that our model is aware of word order and is fairly invariant to the active and passive voice.

---

### النسخة العربية

الشبكات العصبية العميقة (DNNs) هي نماذج تعلم آلي قوية للغاية تحقق أداءً ممتازاً في المشاكل الصعبة مثل التعرف على الكلام [13، 7] والتعرف على الأجسام المرئية [19، 6، 21، 20]. الشبكات العصبية العميقة قوية لأنها تستطيع تنفيذ حسابات متوازية تعسفية لعدد معتدل من الخطوات. مثال مفاجئ على قوة الشبكات العصبية العميقة هو قدرتها على ترتيب N عدد من N بت باستخدام طبقتين مخفيتين فقط بحجم تربيعي [27]. لذلك، في حين أن الشبكات العصبية مرتبطة بالنماذج الإحصائية التقليدية، فإنها تتعلم حسابات معقدة. علاوة على ذلك، يمكن تدريب الشبكات العصبية العميقة الكبيرة باستخدام الانتشار العكسي الموجه كلما كانت مجموعة التدريب المُعنونة تحتوي على معلومات كافية لتحديد معاملات الشبكة. وبالتالي، إذا كان هناك إعداد معاملات لشبكة عصبية عميقة كبيرة يحقق نتائج جيدة (على سبيل المثال، لأن البشر يمكنهم حل المهمة بسرعة كبيرة)، فإن الانتشار العكسي الموجه سيجد هذه المعاملات ويحل المشكلة.

على الرغم من مرونتها وقوتها، يمكن تطبيق الشبكات العصبية العميقة فقط على المشاكل التي يمكن ترميز مدخلاتها ومخرجاتها بشكل معقول باستخدام متجهات ذات أبعاد ثابتة. إنه قيد كبير، حيث أن العديد من المشاكل المهمة يُعبَّر عنها بشكل أفضل باستخدام تسلسلات لا تُعرف أطوالها مسبقاً. على سبيل المثال، التعرف على الكلام والترجمة الآلية هي مشاكل تسلسلية. وبالمثل، يمكن أيضاً رؤية الإجابة على الأسئلة على أنها تخطيط تسلسل من الكلمات يمثل السؤال إلى تسلسل من الكلمات يمثل الإجابة. لذلك من الواضح أن طريقة مستقلة عن المجال تتعلم تخطيط التسلسلات إلى تسلسلات ستكون مفيدة.

تشكل التسلسلات تحدياً للشبكات العصبية العميقة لأنها تتطلب أن تكون أبعاد المدخلات والمخرجات معروفة وثابتة. في هذا البحث، نوضح أن تطبيقاً مباشراً لمعمارية ذاكرة طويلة قصيرة المدى (LSTM) [16] يمكن أن يحل مشاكل التسلسل إلى التسلسل العامة. الفكرة هي استخدام LSTM واحدة لقراءة تسلسل الإدخال، خطوة زمنية واحدة في كل مرة، للحصول على تمثيل متجه كبير ذي أبعاد ثابتة، ثم استخدام LSTM أخرى لاستخراج تسلسل الإخراج من ذلك المتجه (الشكل 1). LSTM الثانية هي في الأساس نموذج لغوي للشبكة العصبية التكرارية [28، 23، 30] باستثناء أنها مشروطة بتسلسل الإدخال. قدرة LSTM على التعلم بنجاح من البيانات ذات التبعيات الزمنية طويلة المدى تجعلها خياراً طبيعياً لهذا التطبيق نظراً للتأخر الزمني الكبير بين المدخلات ومخرجاتها المقابلة (الشكل 1).

كانت هناك عدة محاولات ذات صلة لمعالجة مشكلة تعلم التسلسل إلى التسلسل العامة باستخدام الشبكات العصبية. نهجنا مرتبط بشكل وثيق بـ Kalchbrenner وBlunsom [18] اللذين كانا أول من خطط الجملة الكاملة للإدخال إلى متجه، ومرتبط بـ Cho وآخرين [5] على الرغم من أن الأخير استُخدم فقط لإعادة تصنيف الفرضيات التي أنتجها نظام قائم على العبارات. قدم Graves [10] آلية انتباه قابلة للتفاضل جديدة تسمح للشبكات العصبية بالتركيز على أجزاء مختلفة من مدخلاتها، وتم تطبيق نسخة أنيقة من هذه الفكرة بنجاح على الترجمة الآلية بواسطة Bahdanau وآخرين [2]. التصنيف التسلسلي الترابطي هو تقنية شائعة أخرى لتخطيط التسلسلات إلى تسلسلات باستخدام الشبكات العصبية، لكنها تفترض محاذاة رتيبة بين المدخلات والمخرجات [11].

النتيجة الرئيسية لهذا العمل هي التالية. في مهمة الترجمة من الإنجليزية إلى الفرنسية WMT'14، حصلنا على درجة BLEU قدرها 34.81 عن طريق استخراج الترجمات مباشرة من مجموعة من 5 شبكات LSTM عميقة (مع 384 مليون معامل وحالة بُعد 8000 لكل منها) باستخدام مفكك بحث شعاعي بسيط من اليسار إلى اليمين. هذه هي أفضل نتيجة بكثير تم تحقيقها عن طريق الترجمة المباشرة باستخدام الشبكات العصبية الكبيرة. للمقارنة، درجة BLEU لخط الأساس SMT على مجموعة البيانات هذه هي 33.30 [29]. تم تحقيق درجة BLEU 34.81 بواسطة LSTM بمفردات 80 ألف كلمة، لذلك تم تخفيض الدرجة كلما احتوت الترجمة المرجعية على كلمة لا تغطيها هذه الـ 80 ألف. توضح هذه النتيجة أن معمارية شبكة عصبية ذات مفردات صغيرة غير محسّنة نسبياً والتي لديها مجال كبير للتحسين تتفوق على نظام SMT قائم على العبارات.

أخيراً، استخدمنا LSTM لإعادة تصنيف قوائم أفضل 1000 المتاحة للعموم من خط الأساس SMT في نفس المهمة [29]. من خلال القيام بذلك، حصلنا على درجة BLEU قدرها 36.5، مما يحسن خط الأساس بمقدار 3.2 نقطة BLEU وهي قريبة من أفضل نتيجة منشورة سابقة في هذه المهمة (وهي 37.0 [9]).

بشكل مفاجئ، لم تعاني LSTM من الجمل الطويلة جداً، على الرغم من التجربة الحديثة للباحثين الآخرين مع المعماريات ذات الصلة [26]. تمكنا من الأداء الجيد في الجمل الطويلة لأننا عكسنا ترتيب الكلمات في الجملة المصدر وليس الجمل المستهدفة في مجموعة التدريب والاختبار. من خلال القيام بذلك، قدمنا العديد من التبعيات قصيرة المدى التي جعلت مشكلة التحسين أبسط بكثير (انظر القسم 2 و 3.3). ونتيجة لذلك، تمكن SGD من تعلم شبكات LSTM لم تواجه أي مشكلة مع الجمل الطويلة. الحيلة البسيطة لعكس الكلمات في الجملة المصدر هي واحدة من المساهمات التقنية الرئيسية لهذا العمل.

خاصية مفيدة لـ LSTM هي أنها تتعلم تخطيط جملة إدخال ذات طول متغير إلى تمثيل متجه ذي أبعاد ثابتة. نظراً لأن الترجمات تميل إلى أن تكون إعادة صياغة للجمل المصدر، فإن هدف الترجمة يشجع LSTM على إيجاد تمثيلات جمل تلتقط معناها، حيث أن الجمل ذات المعاني المتشابهة قريبة من بعضها البعض بينما ستكون معاني الجمل المختلفة بعيدة. يدعم التقييم النوعي هذا الادعاء، ويُظهر أن نموذجنا يدرك ترتيب الكلمات ومستقر إلى حد ما تجاه الصيغة المبنية للمعلوم والمبنية للمجهول.

---

### Translation Notes

- **Figures referenced:** Figure 1
- **Key terms introduced:** sequence-to-sequence learning, encoder-decoder architecture, reversing source sentences, beam search
- **Equations:** 0
- **Citations:** [13, 7, 19, 6, 21, 20, 27, 16, 28, 23, 30, 18, 5, 10, 2, 11, 29, 9, 26]
- **Special handling:** Technical discussion of architectural choices and empirical results

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.89
- **Overall section score:** 0.88
