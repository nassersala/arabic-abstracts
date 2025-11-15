# Section 3: Experiments (Part 2: Training, Parallelization, and Results)
## القسم 3: التجارب (الجزء 2: التدريب، التوازي، والنتائج)

**Section:** experiments (3.4-3.6)
**Translation Quality:** 0.87
**Glossary Terms Used:** LSTM, stochastic gradient descent, learning rate, minibatch, gradient, embedding, softmax, GPU, parallelization, BLEU score, ensemble

---

### English Version

**3.4 Training details**

We found that the LSTM models are fairly easy to train. We used deep LSTMs with 4 layers, with 1000 cells at each layer and 1000 dimensional word embeddings, with an input vocabulary of 160,000 and an output vocabulary of 80,000. Thus the deep LSTM uses 8000 real numbers to represent a sentence. We found deep LSTMs to significantly outperform shallow LSTMs, where each additional layer reduced perplexity by nearly 10%, possibly due to their much larger hidden state. We used a naive softmax over 80,000 words at each output. The resulting LSTM has 384M parameters of which 64M are pure recurrent connections (32M for the "encoder" LSTM and 32M for the "decoder" LSTM). The complete training details are given below:

• We initialized all of the LSTM's parameters with the uniform distribution between -0.08 and 0.08
• We used stochastic gradient descent without momentum, with a fixed learning rate of 0.7. After 5 epochs, we begun halving the learning rate every half epoch. We trained our models for a total of 7.5 epochs.
• We used batches of 128 sequences for the gradient and divided it the size of the batch (namely, 128).
• Although LSTMs tend to not suffer from the vanishing gradient problem, they can have exploding gradients. Thus we enforced a hard constraint on the norm of the gradient [10, 25] by scaling it when its norm exceeded a threshold. For each training batch, we compute $s = \|g\|_2$, where $g$ is the gradient divided by 128. If $s > 5$, we set $g = \frac{5g}{s}$.
• Different sentences have different lengths. Most sentences are short (e.g., length 20-30) but some sentences are long (e.g., length > 100), so a minibatch of 128 randomly chosen training sentences will have many short sentences and few long sentences, and as a result, much of the computation in the minibatch is wasted. To address this problem, we made sure that all sentences in a minibatch are roughly of the same length, yielding a 2x speedup.

**3.5 Parallelization**

A C++ implementation of deep LSTM with the configuration from the previous section on a single GPU processes a speed of approximately 1,700 words per second. This was too slow for our purposes, so we parallelized our model using an 8-GPU machine. Each layer of the LSTM was executed on a different GPU and communicated its activations to the next GPU / layer as soon as they were computed. Our models have 4 layers of LSTMs, each of which resides on a separate GPU. The remaining 4 GPUs were used to parallelize the softmax, so each GPU was responsible for multiplying by a 1000 × 20000 matrix. The resulting implementation achieved a speed of 6,300 (both English and French) words per second with a minibatch size of 128. Training took about a ten days with this implementation.

**3.6 Experimental Results**

We used the cased BLEU score [24] to evaluate the quality of our translations. We computed our BLEU scores using multi-bleu.pl¹ on the tokenized predictions and ground truth. This way of evaluating the BELU score is consistent with [5] and [2], and reproduces the 33.3 score of [29]. However, if we evaluate the best WMT'14 system [9] (whose predictions can be downloaded from statmt.org\matrix) in this manner, we get 37.0, which is greater than the 35.8 reported by statmt.org\matrix.

The results are presented in tables 1 and 2. Our best results are obtained with an ensemble of LSTMs that differ in their random initializations and in the random order of minibatches. While the decoded translations of the LSTM ensemble do not outperform the best WMT'14 system, it is the first time that a pure neural translation system outperforms a phrase-based SMT baseline on a large scale MT task by a sizeable margin, despite its inability to handle out-of-vocabulary words. The LSTM is within 0.5 BLEU points of the best WMT'14 result if it is used to rescore the 1000-best list of the baseline system.

¹There several variants of the BLEU score, and each variant is defined with a perl script.

---

### النسخة العربية

**3.4 تفاصيل التدريب**

وجدنا أن نماذج LSTM سهلة التدريب إلى حد ما. استخدمنا شبكات LSTM عميقة بـ 4 طبقات، مع 1000 خلية في كل طبقة وتضمينات كلمات بُعد 1000، مع مفردات إدخال 160,000 ومفردات إخراج 80,000. وبالتالي تستخدم LSTM العميقة 8000 رقم حقيقي لتمثيل جملة. وجدنا أن شبكات LSTM العميقة تتفوق بشكل كبير على شبكات LSTM الضحلة، حيث خفضت كل طبقة إضافية الحيرة بنحو 10٪، ربما بسبب حالتها المخفية الأكبر بكثير. استخدمنا softmax ساذجة على 80,000 كلمة في كل إخراج. تحتوي LSTM الناتجة على 384 مليون معامل منها 64 مليون هي اتصالات تكرارية خالصة (32 مليون لـ LSTM "المشفر" و 32 مليون لـ LSTM "فك التشفير"). تفاصيل التدريب الكاملة معطاة أدناه:

• قمنا بتهيئة جميع معاملات LSTM بالتوزيع المنتظم بين -0.08 و 0.08
• استخدمنا الانحدار التدرجي العشوائي بدون زخم، بمعدل تعلم ثابت قدره 0.7. بعد 5 حقب، بدأنا في تقليل معدل التعلم إلى النصف كل نصف حقبة. دربنا نماذجنا لإجمالي 7.5 حقبة.
• استخدمنا دفعات من 128 تسلسلاً للتدرج وقسمناه على حجم الدفعة (أي 128).
• على الرغم من أن شبكات LSTM لا تميل إلى المعاناة من مشكلة التدرج المتلاشي، إلا أنها يمكن أن يكون لديها تدرجات متفجرة. وبالتالي فرضنا قيداً صارماً على معيار التدرج [10، 25] عن طريق قياسه عندما يتجاوز معياره حداً معيناً. لكل دفعة تدريب، نحسب $s = \|g\|_2$، حيث $g$ هو التدرج مقسوماً على 128. إذا كان $s > 5$، نضع $g = \frac{5g}{s}$.
• الجمل المختلفة لها أطوال مختلفة. معظم الجمل قصيرة (على سبيل المثال، الطول 20-30) ولكن بعض الجمل طويلة (على سبيل المثال، الطول > 100)، لذلك فإن دفعة صغيرة من 128 جملة تدريبية مختارة عشوائياً ستحتوي على العديد من الجمل القصيرة وقليل من الجمل الطويلة، ونتيجة لذلك، يتم إهدار الكثير من الحساب في الدفعة الصغيرة. لمعالجة هذه المشكلة، تأكدنا من أن جميع الجمل في دفعة صغيرة لها نفس الطول تقريباً، مما أدى إلى تسريع 2x.

**3.5 التوازي**

تنفيذ C++ لـ LSTM عميقة مع التكوين من القسم السابق على GPU واحدة يعالج بسرعة تقارب 1,700 كلمة في الثانية. كان هذا بطيئاً جداً لأغراضنا، لذلك قمنا بتوازي نموذجنا باستخدام جهاز 8-GPU. تم تنفيذ كل طبقة من LSTM على GPU مختلفة وأبلغت تنشيطاتها إلى GPU / الطبقة التالية بمجرد حسابها. نماذجنا لديها 4 طبقات من LSTMs، كل منها موجود على GPU منفصل. تم استخدام الـ 4 GPUs المتبقية لتوازي softmax، لذلك كانت كل GPU مسؤولة عن الضرب بمصفوفة 1000 × 20000. حقق التنفيذ الناتج سرعة 6,300 كلمة (الإنجليزية والفرنسية معاً) في الثانية بحجم دفعة صغيرة 128. استغرق التدريب حوالي عشرة أيام مع هذا التنفيذ.

**3.6 النتائج التجريبية**

استخدمنا درجة BLEU مع الحالة [24] لتقييم جودة ترجماتنا. حسبنا درجات BLEU الخاصة بنا باستخدام multi-bleu.pl¹ على التنبؤات المُقسمة إلى رموز والحقيقة الأرضية. هذه الطريقة لتقييم درجة BELU متسقة مع [5] و [2]، وتعيد إنتاج درجة 33.3 من [29]. ومع ذلك، إذا قيمنا أفضل نظام WMT'14 [9] (الذي يمكن تنزيل تنبؤاته من statmt.org\matrix) بهذه الطريقة، نحصل على 37.0، وهو أكبر من 35.8 المبلغ عنه بواسطة statmt.org\matrix.

يتم عرض النتائج في الجدولين 1 و 2. يتم الحصول على أفضل نتائجنا باستخدام مجموعة من LSTMs التي تختلف في تهيئاتها العشوائية وفي الترتيب العشوائي للدفعات الصغيرة. بينما الترجمات المفككة لمجموعة LSTM لا تتفوق على أفضل نظام WMT'14، إنها المرة الأولى التي يتفوق فيها نظام ترجمة عصبي خالص على خط أساس SMT قائم على العبارات في مهمة ترجمة آلية واسعة النطاق بهامش كبير، على الرغم من عدم قدرته على التعامل مع الكلمات خارج المفردات. LSTM في حدود 0.5 نقطة BLEU من أفضل نتيجة WMT'14 إذا تم استخدامها لإعادة تصنيف قائمة أفضل 1000 من النظام الأساسي.

¹هناك عدة متغيرات من درجة BLEU، وكل متغير يتم تعريفه بنص برمجي perl.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Tables referenced:** Table 1, Table 2
- **Key terms introduced:** gradient clipping, exploding gradient, minibatch optimization, model parallelization, ensemble learning
- **Equations:** 1 equation (gradient clipping formula)
- **Citations:** [10, 25, 24, 5, 2, 29, 9]
- **Special handling:** Detailed hyperparameter specifications, parallel training architecture

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87
