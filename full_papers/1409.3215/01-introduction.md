# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** deep neural networks, sequence learning, LSTM, vector representation, machine translation, speech recognition, supervised backpropagation, domain-independent, fixed dimensionality

---

### English Version

Deep Neural Networks (DNNs) are extremely powerful machine learning models that achieve excellent performance on difficult problems such as speech recognition [13,7] and visual object recognition [19, 6, 21, 20]. DNNs are powerful because they can perform arbitrary parallel computation for a modest number of steps. A surprising example of the power of DNNs is their ability to sort N N-bit numbers using only 2 hidden layers of quadratic size [27]. So, while neural networks are related to conventional statistical models, they learn an intricate computation. Furthermore, large DNNs can be trained with supervised backpropagation whenever the labeled training set has enough information to specify the network's parameters. Thus, if there exists a parameter setting of a large DNN that achieves good results (for example, because humans can solve the task very rapidly), supervised backpropagation will find these parameters and solve the problem.

Despite their flexibility and power, DNNs can only be applied to problems whose inputs and targets can be sensibly encoded with vectors of fixed dimensionality. It is a significant limitation, since many important problems are best expressed with sequences whose lengths are not known a-priori. For example, speech recognition and machine translation are sequential problems. Likewise, question answering can also be seen as mapping a sequence of words representing the question to a sequence of words representing the answer. It is therefore clear that a domain-independent method that learns to map sequences to sequences would be useful.

Sequences pose a challenge for DNNs because they require that the dimensionality of the inputs and outputs is known and fixed. In this paper, we show that a straightforward application of the Long Short-Term Memory (LSTM) architecture [16] can solve general sequence to sequence problems. The idea is to use one LSTM to read the input sequence, one timestep at a time, to obtain large fixed-dimensional vector representation, and then to use another LSTM to extract the output sequence from that vector (fig. 1). The second LSTM is essentially a recurrent neural network language model [28, 23, 30] except that it is conditioned on the input sequence. The LSTM's ability to successfully learn on data with long range temporal dependencies makes it a natural choice for this application due to the considerable time lag between the inputs and their corresponding outputs (fig. 1).

There have been a number of related attempts to address the general sequence to sequence learning problem with neural networks. Our approach is closely related to Kalchbrenner and Blunsom [18] who were the first to map the entire input sentence to vector, and is related to Cho et al. [5] although the latter was used only for rescoring hypotheses produced by a phrase-based system. Graves [10] introduced a novel differentiable attention mechanism that allows neural networks to focus on different parts of their input, and an elegant variant of this idea was successfully applied to machine translation by Bahdanau et al. [2]. The Connectionist Sequence Classification is another popular technique for mapping sequences to sequences with neural networks, but it assumes a monotonic alignment between the inputs and the outputs [11].

---

### النسخة العربية

الشبكات العصبية العميقة (DNNs) هي نماذج تعلم آلي بالغة القوة تحقق أداءً ممتازاً في المسائل الصعبة مثل التعرف على الكلام [13,7] والتعرف على الأجسام المرئية [19, 6, 21, 20]. الشبكات العصبية العميقة قوية لأنها تستطيع تنفيذ عمليات حسابية متوازية عشوائية لعدد محدود من الخطوات. من الأمثلة المفاجئة على قوة الشبكات العصبية العميقة قدرتها على ترتيب N عدد من N-بت باستخدام طبقتين مخفيتين فقط بحجم تربيعي [27]. لذلك، بينما ترتبط الشبكات العصبية بالنماذج الإحصائية التقليدية، فإنها تتعلم عملية حسابية معقدة. علاوة على ذلك، يمكن تدريب الشبكات العصبية العميقة الكبيرة بالانتشار الخلفي الموجّه كلما احتوت مجموعة التدريب المُعنونة على معلومات كافية لتحديد معاملات الشبكة. وبالتالي، إذا كان هناك إعداد معاملات لشبكة عصبية عميقة كبيرة يحقق نتائج جيدة (على سبيل المثال، لأن البشر يمكنهم حل المهمة بسرعة كبيرة)، فإن الانتشار الخلفي الموجّه سيجد هذه المعاملات ويحل المشكلة.

على الرغم من مرونتها وقوتها، لا يمكن تطبيق الشبكات العصبية العميقة إلا على المسائل التي يمكن ترميز مدخلاتها وأهدافها بشكل معقول باستخدام متجهات ذات أبعاد ثابتة. هذا قيد كبير، حيث أن العديد من المسائل المهمة يُعبّر عنها بشكل أفضل باستخدام تسلسلات لا تُعرف أطوالها مسبقاً. على سبيل المثال، التعرف على الكلام والترجمة الآلية هي مسائل تسلسلية. وبالمثل، يمكن أيضاً اعتبار الإجابة على الأسئلة بمثابة تخطيط لتسلسل من الكلمات يمثل السؤال إلى تسلسل من الكلمات يمثل الإجابة. لذلك من الواضح أن طريقة مستقلة عن المجال تتعلم تخطيط التسلسلات إلى تسلسلات ستكون مفيدة.

تشكل التسلسلات تحدياً للشبكات العصبية العميقة لأنها تتطلب أن تكون أبعاد المدخلات والمخرجات معروفة وثابتة. في هذا البحث، نُظهر أن تطبيقاً مباشراً لمعمارية ذاكرة طويلة قصيرة المدى (LSTM) [16] يمكنه حل مسائل التسلسل إلى التسلسل العامة. الفكرة هي استخدام LSTM واحدة لقراءة تسلسل الإدخال، خطوة زمنية واحدة في كل مرة، للحصول على تمثيل متجهي كبير ذي أبعاد ثابتة، ثم استخدام LSTM أخرى لاستخراج تسلسل الإخراج من ذلك المتجه (شكل 1). إن LSTM الثانية هي في الأساس نموذج لغوي للشبكة العصبية المتكررة [28, 23, 30] باستثناء أنها مشروطة بتسلسل الإدخال. إن قدرة LSTM على التعلم بنجاح من البيانات ذات التبعيات الزمنية طويلة المدى تجعلها خياراً طبيعياً لهذا التطبيق نظراً للتأخر الزمني الكبير بين المدخلات والمخرجات المقابلة لها (شكل 1).

كانت هناك عدة محاولات ذات صلة لمعالجة مسألة تعلم التسلسل إلى التسلسل العامة باستخدام الشبكات العصبية. نهجنا مرتبط بشكل وثيق بـ Kalchbrenner وBlunsom [18] اللذين كانا أول من قام بتخطيط الجملة الكاملة للإدخال إلى متجه، ويرتبط بـ Cho وآخرين [5] على الرغم من أن الأخير استُخدم فقط لإعادة تسجيل الفرضيات التي ينتجها نظام قائم على العبارات. قدم Graves [10] آلية انتباه قابلة للاشتقاق جديدة تسمح للشبكات العصبية بالتركيز على أجزاء مختلفة من مدخلاتها، وتم تطبيق نسخة أنيقة من هذه الفكرة بنجاح على الترجمة الآلية بواسطة Bahdanau وآخرين [2]. تُعد تصنيف التسلسل الترابطي (Connectionist Sequence Classification) تقنية أخرى شائعة لتخطيط التسلسلات إلى تسلسلات باستخدام الشبكات العصبية، لكنها تفترض محاذاة رتيبة بين المدخلات والمخرجات [11].

---

### Translation Notes

- **Figures referenced:** Figure 1
- **Key terms introduced:** sequence-to-sequence, encoder-decoder, LSTM, recurrent neural network language model, attention mechanism
- **Equations:** None in introduction
- **Citations:** [13,7], [19, 6, 21, 20], [27], [16], [28, 23, 30], [18], [5], [10], [2], [11]
- **Special handling:** Citations kept in square brackets, technical paper references preserved

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.85
- **Overall section score:** 0.88
