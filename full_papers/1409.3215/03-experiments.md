# Section 3: Experiments
## القسم 3: التجارب

**Section:** experiments
**Translation Quality:** 0.86
**Glossary Terms Used:** machine translation, WMT'14 dataset, BLEU score, beam search, decoder, training, gradient descent, perplexity, ensemble

---

### English Version

We applied our method to the WMT'14 English to French MT task in two ways. We used it to directly translate the input sentence without using a reference SMT system and we it to rescore the n-best lists of an SMT baseline. We report the accuracy of these translation methods, present sample translations, and visualize the resulting sentence representations.

### 3.1 Dataset details

We used the WMT'14 English to French dataset. We trained our models on a subset of 12M sentences consisting of 348M French words and 304M English words, which is a clean "selected" subset from [29]. We chose this translation task and this specific training set subset because of the public availability of a tokenized training and test set together with 1000-best lists from the baseline SMT [29].

As typical neural language models rely on a vector representation for each word, we used a fixed vocabulary for both languages. We used 160,000 of the most frequent words for the source language and 80,000 of the most frequent words for the target language. Every out-of-vocabulary word was replaced with a special "UNK" token.

### 3.2 Decoding and Rescoring

The core of our experiments involved training a large deep LSTM on many sentence pairs. We trained it by maximizing the log probability of a correct translation $T$ given the source sentence $S$, so the training objective is

$$\frac{1}{|S|} \sum_{(T,S) \in S} \log p(T|S)$$

where $S$ is the training set. Once training is complete, we produce translations by finding the most likely translation according to the LSTM:

$$\hat{T} = \arg\max_T p(T|S) \qquad (2)$$

We search for the most likely translation using a simple left-to-right beam search decoder which maintains a small number $B$ of partial hypotheses, where a partial hypothesis is a prefix of some translation. At each timestep we extend each partial hypothesis in the beam with every possible word in the vocabulary. This greatly increases the number of the hypotheses so we discard all but the $B$ most likely hypotheses according to the model's log probability. As soon as the "$<$EOS$>$" symbol is appended to a hypothesis, it is removed from the beam and is added to the set of complete hypotheses. While this decoder is approximate, it is simple to implement. Interestingly, our system performs well even with a beam size of 1, and a beam of size 2 provides most of the benefits of beam search (Table 1).

We also used the LSTM to rescore the 1000-best lists produced by the baseline system [29]. To rescore an n-best list, we computed the log probability of every hypothesis with our LSTM and took an even average with their score and the LSTM's score.

### 3.3 Reversing the Source Sentences

While the LSTM is capable of solving problems with long term dependencies, we discovered that the LSTM learns much better when the source sentences are reversed (the target sentences are not reversed). By doing so, the LSTM's test perplexity dropped from 5.8 to 4.7, and the test BLEU scores of its decoded translations increased from 25.9 to 30.6.

While we do not have a complete explanation to this phenomenon, we believe that it is caused by the introduction of many short term dependencies to the dataset. Normally, when we concatenate a source sentence with a target sentence, each word in the source sentence is far from its corresponding word in the target sentence. As a result, the problem has a large "minimal time lag" [17]. By reversing the words in the source sentence, the average distance between corresponding words in the source and target language is unchanged. However, the first few words in the source language are now very close to the first few words in the target language, so the problem's minimal time lag is greatly reduced. Thus, backpropagation has an easier time "establishing communication" between the source sentence and the target sentence, which in turn results in substantially improved overall performance.

Initially, we believed that reversing the input sentences would only lead to more confident predictions in the early parts of the target sentence and to less confident predictions in the later parts. However, LSTMs trained on reversed source sentences did much better on long sentences than LSTMs trained on the raw source sentences (see sec. 3.7), which suggests that reversing the input sentences results in LSTMs with better memory utilization.

### 3.4 Training details

We found that the LSTM models are fairly easy to train. We used deep LSTMs with 4 layers, with 1000 cells at each layer and 1000 dimensional word embeddings, with an input vocabulary of 160,000 and an output vocabulary of 80,000. Thus the deep LSTM uses 8000 real numbers to represent a sentence. We found deep LSTMs to significantly outperform shallow LSTMs, where each additional layer reduced perplexity by nearly 10%, possibly due to their much larger hidden state. We used a naive softmax over 80,000 words at each output. The resulting LSTM has 384M parameters of which 64M are pure recurrent connections (32M for the "encoder" LSTM and 32M for the "decoder" LSTM). The complete training details are given below:

• We initialized all of the LSTM's parameters with the uniform distribution between -0.08 and 0.08
• We used stochastic gradient descent without momentum, with a fixed learning rate of 0.7. After 5 epochs, we begun halving the learning rate every half epoch. We trained our models for a total of 7.5 epochs.
• We used batches of 128 sequences for the gradient and divided it the size of the batch (namely, 128).
• Although LSTMs tend to not suffer from the vanishing gradient problem, they can have exploding gradients. Thus we enforced a hard constraint on the norm of the gradient [10, 25] by scaling it when its norm exceeded a threshold. For each training batch, we compute $s = ||g||_2$, where $g$ is the gradient divided by 128. If $s > 5$, we set $g = \frac{5g}{s}$.
• Different sentences have different lengths. Most sentences are short (e.g., length 20-30) but some sentences are long (e.g., length >100), so a minibatch of 128 randomly chosen training sentences will have many short sentences and few long sentences, and as a result, much of the computation in the minibatch is wasted. To address this problem, we made sure that all sentences in a minibatch are roughly of the same length, yielding a 2x speedup.

### 3.5 Parallelization

A C++ implementation of deep LSTM with the configuration from the previous section on a single GPU processes a speed of approximately 1,700 words per second. This was too slow for our purposes, so we parallelized our model using an 8-GPU machine. Each layer of the LSTM was executed on a different GPU and communicated its activations to the next GPU / layer as soon as they were computed. Our models have 4 layers of LSTMs, each of which resides on a separate GPU. The remaining 4 GPUs were used to parallelize the softmax, so each GPU was responsible for multiplying by a $1000 \times 20000$ matrix. The resulting implementation achieved a speed of 6,300 (both English and French) words per second with a minibatch size of 128. Training took about a ten days with this implementation.

### 3.6 Experimental Results

We used the cased BLEU score [24] to evaluate the quality of our translations. We computed our BLEU scores using multi-bleu.pl on the tokenized predictions and ground truth. This way of evaluating the BELU score is consistent with [5] and [2], and reproduces the 33.3 score of [29]. However, if we evaluate the best WMT'14 system [9] (whose predictions can be downloaded from statmt.org\matrix) in this manner, we get 37.0, which is greater than the 35.8 reported by statmt.org\matrix.

The results are presented in tables 1 and 2. Our best results are obtained with an ensemble of LSTMs that differ in their random initializations and in the random order of minibatches. While the decoded translations of the LSTM ensemble do not outperform the best WMT'14 system, it is the first time that a pure neural translation system outperforms a phrase-based SMT baseline on a large scale MT task by a sizeable margin, despite its inability to handle out-of-vocabulary words. The LSTM is within 0.5 BLEU points of the best WMT'14 result if it is used to rescore the 1000-best list of the baseline system.

**Table 1:** The performance of the LSTM on WMT'14 English to French test set (ntst14).

| Method | test BLEU score (ntst14) |
|--------|--------------------------|
| Bahdanau et al. [2] | 28.45 |
| Baseline System [29] | 33.30 |
| Single forward LSTM, beam size 12 | 26.17 |
| Single reversed LSTM, beam size 12 | 30.59 |
| Ensemble of 5 reversed LSTMs, beam size 1 | 33.00 |
| Ensemble of 2 reversed LSTMs, beam size 12 | 33.27 |
| Ensemble of 5 reversed LSTMs, beam size 2 | 34.50 |
| Ensemble of 5 reversed LSTMs, beam size 12 | 34.81 |

**Table 2:** Methods that use neural networks together with an SMT system on the WMT'14 English to French test set (ntst14).

| Method | test BLEU score (ntst14) |
|--------|--------------------------|
| Baseline System [29] | 33.30 |
| Cho et al. [5] | 34.54 |
| Best WMT'14 result [9] | 37.0 |
| Rescoring the baseline 1000-best with a single forward LSTM | 35.61 |
| Rescoring the baseline 1000-best with a single reversed LSTM | 35.85 |
| Rescoring the baseline 1000-best with an ensemble of 5 reversed LSTMs | 36.5 |
| Oracle Rescoring of the Baseline 1000-best lists | ~45 |

### 3.7 Performance on long sentences

We were surprised to discover that the LSTM did well on long sentences, which is shown quantitatively in figure 3. Table 3 presents several examples of long sentences and their translations.

### 3.8 Model Analysis

One of the attractive features of our model is its ability to turn a sequence of words into a vector of fixed dimensionality. Figure 2 visualizes some of the learned representations. The figure clearly shows that the representations are sensitive to the order of words, while being fairly insensitive to the replacement of an active voice with a passive voice. The two-dimensional projections are obtained using PCA.

---

### النسخة العربية

طبقنا طريقتنا على مهمة الترجمة الآلية من الإنجليزية إلى الفرنسية في WMT'14 بطريقتين. استخدمناها لترجمة جملة الإدخال مباشرة دون استخدام نظام SMT مرجعي واستخدمناها لإعادة تسجيل قوائم n-best لنظام SMT أساسي. نُبلّغ عن دقة طرق الترجمة هذه، ونقدم عينات من الترجمات، ونعرض تمثيلات الجمل الناتجة بصرياً.

### 3.1 تفاصيل مجموعة البيانات

استخدمنا مجموعة بيانات WMT'14 للترجمة من الإنجليزية إلى الفرنسية. دربنا نماذجنا على مجموعة فرعية من 12 مليون جملة تتكون من 348 مليون كلمة فرنسية و304 مليون كلمة إنجليزية، وهي مجموعة فرعية "مختارة" نظيفة من [29]. اخترنا مهمة الترجمة هذه ومجموعة التدريب الفرعية المحددة هذه بسبب التوفر العام لمجموعة تدريب واختبار مُرمَّزة مع قوائم 1000-best من نظام SMT الأساسي [29].

نظراً لأن نماذج اللغة العصبية النموذجية تعتمد على تمثيل متجهي لكل كلمة، استخدمنا مفردات ثابتة لكلتا اللغتين. استخدمنا 160,000 من الكلمات الأكثر تكراراً للغة المصدر و80,000 من الكلمات الأكثر تكراراً للغة الهدف. تم استبدال كل كلمة خارج المفردات برمز "UNK" خاص.

### 3.2 فك التشفير وإعادة التسجيل

كان جوهر تجاربنا هو تدريب LSTM عميقة كبيرة على العديد من أزواج الجمل. دربناها عن طريق تعظيم الاحتمال اللوغاريتمي للترجمة الصحيحة $T$ بمعلومية الجملة المصدر $S$، لذلك فإن هدف التدريب هو

$$\frac{1}{|S|} \sum_{(T,S) \in S} \log p(T|S)$$

حيث $S$ هي مجموعة التدريب. بمجرد اكتمال التدريب، ننتج الترجمات من خلال إيجاد الترجمة الأكثر احتمالاً وفقاً لـ LSTM:

$$\hat{T} = \arg\max_T p(T|S) \qquad (2)$$

نبحث عن الترجمة الأكثر احتمالاً باستخدام فك تشفير بحث شعاعي بسيط من اليسار إلى اليمين يحافظ على عدد صغير $B$ من الفرضيات الجزئية، حيث الفرضية الجزئية هي بادئة لبعض الترجمات. في كل خطوة زمنية نوسّع كل فرضية جزئية في الشعاع بكل كلمة ممكنة في المفردات. هذا يزيد بشكل كبير من عدد الفرضيات لذلك نتجاهل كل الفرضيات باستثناء الـ $B$ الأكثر احتمالاً وفقاً للاحتمال اللوغاريتمي للنموذج. بمجرد إضافة الرمز "$<$EOS$>$" إلى فرضية، يتم إزالتها من الشعاع وإضافتها إلى مجموعة الفرضيات الكاملة. على الرغم من أن فك التشفير هذا تقريبي، إلا أنه بسيط للتنفيذ. من المثير للاهتمام أن نظامنا يؤدي بشكل جيد حتى مع حجم شعاع 1، والشعاع بحجم 2 يوفر معظم فوائد البحث الشعاعي (الجدول 1).

استخدمنا أيضاً LSTM لإعادة تسجيل قوائم 1000-best التي أنتجها النظام الأساسي [29]. لإعادة تسجيل قائمة n-best، حسبنا الاحتمال اللوغاريتمي لكل فرضية باستخدام LSTM الخاصة بنا وأخذنا متوسطاً متساوياً مع درجتها ودرجة LSTM.

### 3.3 عكس الجمل المصدر

على الرغم من أن LSTM قادرة على حل المسائل ذات التبعيات طويلة المدى، اكتشفنا أن LSTM تتعلم بشكل أفضل بكثير عندما تكون الجمل المصدر معكوسة (لا تُعكس الجمل الهدف). من خلال القيام بذلك، انخفض الحيرة (perplexity) للاختبار في LSTM من 5.8 إلى 4.7، وزادت درجات BLEU للاختبار لترجماتها المفكوكة من 25.9 إلى 30.6.

على الرغم من أنه ليس لدينا تفسير كامل لهذه الظاهرة، نعتقد أنها ناتجة عن إدخال العديد من التبعيات قصيرة المدى إلى مجموعة البيانات. عادةً، عندما نربط جملة مصدر بجملة هدف، تكون كل كلمة في الجملة المصدر بعيدة عن الكلمة المقابلة لها في الجملة الهدف. ونتيجة لذلك، تحتوي المسألة على "تأخر زمني أدنى" كبير [17]. من خلال عكس الكلمات في الجملة المصدر، تبقى المسافة المتوسطة بين الكلمات المقابلة في اللغة المصدر واللغة الهدف دون تغيير. ومع ذلك، فإن الكلمات القليلة الأولى في اللغة المصدر الآن قريبة جداً من الكلمات القليلة الأولى في اللغة الهدف، لذلك يتم تقليل التأخر الزمني الأدنى للمسألة بشكل كبير. وبالتالي، يكون للانتشار الخلفي وقت أسهل في "إنشاء اتصال" بين الجملة المصدر والجملة الهدف، مما يؤدي بدوره إلى تحسين كبير في الأداء العام.

في البداية، اعتقدنا أن عكس جمل الإدخال سيؤدي فقط إلى تنبؤات أكثر ثقة في الأجزاء المبكرة من الجملة الهدف وإلى تنبؤات أقل ثقة في الأجزاء اللاحقة. ومع ذلك، قامت شبكات LSTM المدربة على الجمل المصدر المعكوسة بعمل أفضل بكثير على الجمل الطويلة من شبكات LSTM المدربة على الجمل المصدر الأولية (انظر القسم 3.7)، مما يشير إلى أن عكس جمل الإدخال ينتج عنه شبكات LSTM باستخدام أفضل للذاكرة.

### 3.4 تفاصيل التدريب

وجدنا أن نماذج LSTM سهلة التدريب نسبياً. استخدمنا شبكات LSTM عميقة بـ 4 طبقات، مع 1000 خلية في كل طبقة وتضمينات كلمات بأبعاد 1000، مع مفردات إدخال من 160,000 ومفردات إخراج من 80,000. وبالتالي تستخدم LSTM العميقة 8000 عدد حقيقي لتمثيل جملة. وجدنا أن شبكات LSTM العميقة تفوقت بشكل كبير على شبكات LSTM الضحلة، حيث أدت كل طبقة إضافية إلى تقليل الحيرة بنسبة 10% تقريباً، ربما بسبب حالتها المخفية الأكبر بكثير. استخدمنا softmax بسيط على 80,000 كلمة في كل مخرج. تحتوي LSTM الناتجة على 384 مليون معامل منها 64 مليون هي اتصالات متكررة خالصة (32 مليون لـ LSTM "المُشفِّر" و32 مليون لـ LSTM "فك التشفير"). تفاصيل التدريب الكاملة معطاة أدناه:

• قمنا بتهيئة جميع معاملات LSTM بالتوزيع الموحد بين -0.08 و0.08
• استخدمنا الانحدار التدرجي العشوائي بدون زخم، بمعدل تعلم ثابت 0.7. بعد 5 حقب، بدأنا في تقسيم معدل التعلم إلى النصف كل نصف حقبة. دربنا نماذجنا لإجمالي 7.5 حقبة.
• استخدمنا دفعات من 128 تسلسل للتدرج وقسمناه على حجم الدفعة (أي 128).
• على الرغم من أن شبكات LSTM لا تعاني عادةً من مشكلة اختفاء التدرج، إلا أنها يمكن أن تحتوي على تدرجات متفجرة. لذلك فرضنا قيداً صارماً على معيار التدرج [10, 25] عن طريق قياسه عندما يتجاوز معياره عتبة معينة. لكل دفعة تدريب، نحسب $s = ||g||_2$، حيث $g$ هو التدرج مقسوماً على 128. إذا كان $s > 5$، نحدد $g = \frac{5g}{s}$.
• الجمل المختلفة لها أطوال مختلفة. معظم الجمل قصيرة (مثلاً، الطول 20-30) لكن بعض الجمل طويلة (مثلاً، الطول >100)، لذلك ستحتوي دفعة صغيرة من 128 جملة تدريبية مختارة عشوائياً على العديد من الجمل القصيرة وبعض الجمل الطويلة، ونتيجة لذلك، يتم إهدار الكثير من الحسابات في الدفعة الصغيرة. لمعالجة هذه المشكلة، تأكدنا من أن جميع الجمل في دفعة صغيرة تقريباً لها نفس الطول، مما أدى إلى تسريع بمقدار 2x.

### 3.5 المعالجة المتوازية

معالجة تنفيذ C++ لـ LSTM عميقة بالتكوين من القسم السابق على GPU واحدة بسرعة تقارب 1,700 كلمة في الثانية. كانت هذه بطيئة جداً لأغراضنا، لذلك قمنا بتوازي نموذجنا باستخدام جهاز 8-GPU. تم تنفيذ كل طبقة من LSTM على GPU مختلفة وتواصل تفعيلاتها إلى GPU/الطبقة التالية بمجرد حسابها. تحتوي نماذجنا على 4 طبقات من LSTMs، كل منها موجود على GPU منفصلة. تم استخدام الـ 4 GPUs المتبقية لتوازي softmax، لذلك كانت كل GPU مسؤولة عن الضرب بمصفوفة $1000 \times 20000$. حقق التنفيذ الناتج سرعة 6,300 كلمة (إنجليزية وفرنسية) في الثانية مع حجم دفعة صغيرة 128. استغرق التدريب حوالي عشرة أيام بهذا التنفيذ.

### 3.6 النتائج التجريبية

استخدمنا درجة BLEU مع حساسية الحالة [24] لتقييم جودة ترجماتنا. حسبنا درجات BLEU الخاصة بنا باستخدام multi-bleu.pl على التنبؤات المُرمَّزة والحقيقة الأرضية. هذه الطريقة لتقييم درجة BELU متسقة مع [5] و[2]، وتعيد إنتاج درجة 33.3 من [29]. ومع ذلك، إذا قيّمنا أفضل نظام WMT'14 [9] (الذي يمكن تنزيل تنبؤاته من statmt.org\matrix) بهذه الطريقة، نحصل على 37.0، وهي أكبر من 35.8 التي أبلغت عنها statmt.org\matrix.

تُعرض النتائج في الجدولين 1 و2. يتم الحصول على أفضل نتائجنا بمجموعة من شبكات LSTM التي تختلف في تهيئاتها العشوائية وفي الترتيب العشوائي للدفعات الصغيرة. بينما لا تتفوق الترجمات المفكوكة لمجموعة LSTM على أفضل نظام WMT'14، إلا أنها المرة الأولى التي يتفوق فيها نظام ترجمة عصبي خالص على نظام SMT أساسي قائم على العبارات في مهمة ترجمة آلية واسعة النطاق بهامش كبير، على الرغم من عدم قدرته على التعامل مع الكلمات خارج المفردات. تقع LSTM ضمن 0.5 نقطة BLEU من أفضل نتيجة WMT'14 إذا تم استخدامها لإعادة تسجيل قائمة 1000-best للنظام الأساسي.

**الجدول 1:** أداء LSTM على مجموعة اختبار WMT'14 من الإنجليزية إلى الفرنسية (ntst14).

| الطريقة | درجة BLEU للاختبار (ntst14) |
|---------|------------------------------|
| Bahdanau وآخرون [2] | 28.45 |
| النظام الأساسي [29] | 33.30 |
| LSTM أمامية واحدة، حجم شعاع 12 | 26.17 |
| LSTM معكوسة واحدة، حجم شعاع 12 | 30.59 |
| مجموعة من 5 LSTMs معكوسة، حجم شعاع 1 | 33.00 |
| مجموعة من 2 LSTMs معكوسة، حجم شعاع 12 | 33.27 |
| مجموعة من 5 LSTMs معكوسة، حجم شعاع 2 | 34.50 |
| مجموعة من 5 LSTMs معكوسة، حجم شعاع 12 | 34.81 |

**الجدول 2:** الطرق التي تستخدم الشبكات العصبية مع نظام SMT على مجموعة اختبار WMT'14 من الإنجليزية إلى الفرنسية (ntst14).

| الطريقة | درجة BLEU للاختبار (ntst14) |
|---------|------------------------------|
| النظام الأساسي [29] | 33.30 |
| Cho وآخرون [5] | 34.54 |
| أفضل نتيجة WMT'14 [9] | 37.0 |
| إعادة تسجيل 1000-best الأساسية بـ LSTM أمامية واحدة | 35.61 |
| إعادة تسجيل 1000-best الأساسية بـ LSTM معكوسة واحدة | 35.85 |
| إعادة تسجيل 1000-best الأساسية بمجموعة من 5 LSTMs معكوسة | 36.5 |
| إعادة التسجيل المثلى لقوائم 1000-best الأساسية | ~45 |

### 3.7 الأداء على الجمل الطويلة

كنا مندهشين عندما اكتشفنا أن LSTM قامت بعمل جيد على الجمل الطويلة، وهو ما يظهر كمياً في الشكل 3. يقدم الجدول 3 عدة أمثلة على الجمل الطويلة وترجماتها.

### 3.8 تحليل النموذج

إحدى السمات الجذابة لنموذجنا هي قدرته على تحويل تسلسل من الكلمات إلى متجه ذي أبعاد ثابتة. يعرض الشكل 2 بعض التمثيلات المتعلمة بصرياً. يُظهر الشكل بوضوح أن التمثيلات حساسة لترتيب الكلمات، بينما تكون غير حساسة إلى حد كبير لاستبدال الصيغة المبنية للمعلوم بالصيغة المبنية للمجهول. يتم الحصول على الإسقاطات ثنائية الأبعاد باستخدام تحليل المكونات الأساسية (PCA).

---

### Translation Notes

- **Figures referenced:** Figure 2, Figure 3
- **Tables referenced:** Table 1, Table 2, Table 3
- **Key terms introduced:** beam search, perplexity, gradient clipping, ensemble, n-best lists, rescoring
- **Equations:** 2 equations (training objective, argmax for decoding)
- **Citations:** [29], [5], [2], [17], [10, 25], [24], [9]
- **Special handling:** Extensive experimental details with hyperparameters, BLEU scores, training procedures

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86
