# Section 3: Experiments (Part 1: Dataset, Decoding, and Reversing)
## القسم 3: التجارب (الجزء 1: مجموعة البيانات، فك التشفير، والعكس)

**Section:** experiments (3-3.3)
**Translation Quality:** 0.86
**Glossary Terms Used:** dataset, vocabulary, out-of-vocabulary, beam search, decoder, hypothesis, BLEU score, perplexity, backpropagation, optimization

---

### English Version

We applied our method to the WMT'14 English to French MT task in two ways. We used it to directly translate the input sentence without using a reference SMT system and we it to rescore the n-best lists of an SMT baseline. We report the accuracy of these translation methods, present sample translations, and visualize the resulting sentence representation.

**3.1 Dataset details**

We used the WMT'14 English to French dataset. We trained our models on a subset of 12M sentences consisting of 348M French words and 304M English words, which is a clean "selected" subset from [29]. We chose this translation task and this specific training set subset because of the public availability of a tokenized training and test set together with 1000-best lists from the baseline SMT [29].

As typical neural language models rely on a vector representation for each word, we used a fixed vocabulary for both languages. We used 160,000 of the most frequent words for the source language and 80,000 of the most frequent words for the target language. Every out-of-vocabulary word was replaced with a special "UNK" token.

**3.2 Decoding and Rescoring**

The core of our experiments involved training a large deep LSTM on many sentence pairs. We trained it by maximizing the log probability of a correct translation $T$ given the source sentence $S$, so the training objective is

$$\frac{1}{|S|} \sum_{(T,S) \in S} \log p(T|S)$$

where $S$ is the training set. Once training is complete, we produce translations by finding the most likely translation according to the LSTM:

$$\hat{T} = \arg\max_T p(T|S) \quad (2)$$

We search for the most likely translation using a simple left-to-right beam search decoder which maintains a small number $B$ of partial hypotheses, where a partial hypothesis is a prefix of some translation. At each timestep we extend each partial hypothesis in the beam with every possible word in the vocabulary. This greatly increases the number of the hypotheses so we discard all but the $B$ most likely hypotheses according to the model's log probability. As soon as the "<EOS>" symbol is appended to a hypothesis, it is removed from the beam and is added to the set of complete hypotheses. While this decoder is approximate, it is simple to implement. Interestingly, our system performs well even with a beam size of 1, and a beam of size 2 provides most of the benefits of beam search (Table 1).

We also used the LSTM to rescore the 1000-best lists produced by the baseline system [29]. To rescore an n-best list, we computed the log probability of every hypothesis with our LSTM and took an even average with their score and the LSTM's score.

**3.3 Reversing the Source Sentences**

While the LSTM is capable of solving problems with long term dependencies, we discovered that the LSTM learns much better when the source sentences are reversed (the target sentences are not reversed). By doing so, the LSTM's test perplexity dropped from 5.8 to 4.7, and the test BLEU scores of its decoded translations increased from 25.9 to 30.6.

While we do not have a complete explanation to this phenomenon, we believe that it is caused by the introduction of many short term dependencies to the dataset. Normally, when we concatenate a source sentence with a target sentence, each word in the source sentence is far from its corresponding word in the target sentence. As a result, the problem has a large "minimal time lag" [17]. By reversing the words in the source sentence, the average distance between corresponding words in the source and target language is unchanged. However, the first few words in the source language are now very close to the first few words in the target language, so the problem's minimal time lag is greatly reduced. Thus, backpropagation has an easier time "establishing communication" between the source sentence and the target sentence, which in turn results in substantially improved overall performance.

Initially, we believed that reversing the input sentences would only lead to more confident predictions in the early parts of the target sentence and to less confident predictions in the later parts. However, LSTMs trained on reversed source sentences did much better on long sentences than LSTMs trained on the raw source sentences (see sec. 3.7), which suggests that reversing the input sentences results in LSTMs with better memory utilization.

---

### النسخة العربية

طبقنا طريقتنا على مهمة الترجمة الآلية من الإنجليزية إلى الفرنسية WMT'14 بطريقتين. استخدمناها لترجمة جملة الإدخال مباشرة دون استخدام نظام SMT مرجعي واستخدمناها لإعادة تصنيف قوائم n-best من خط أساس SMT. نبلغ عن دقة طرق الترجمة هذه، ونقدم عينات من الترجمات، ونصور التمثيل الناتج للجملة.

**3.1 تفاصيل مجموعة البيانات**

استخدمنا مجموعة بيانات WMT'14 من الإنجليزية إلى الفرنسية. دربنا نماذجنا على مجموعة فرعية من 12 مليون جملة تتكون من 348 مليون كلمة فرنسية و 304 مليون كلمة إنجليزية، وهي مجموعة فرعية "مختارة" نظيفة من [29]. اخترنا مهمة الترجمة هذه ومجموعة التدريب الفرعية المحددة هذه بسبب التوفر العام لمجموعة تدريب واختبار مُقسمة إلى رموز مع قوائم أفضل 1000 من خط الأساس SMT [29].

نظراً لأن نماذج اللغة العصبية النموذجية تعتمد على تمثيل متجه لكل كلمة، استخدمنا مفردات ثابتة لكلتا اللغتين. استخدمنا 160,000 من الكلمات الأكثر تكراراً للغة المصدر و 80,000 من الكلمات الأكثر تكراراً للغة الهدف. تم استبدال كل كلمة خارج المفردات برمز خاص "UNK".

**3.2 فك التشفير وإعادة التصنيف**

تضمن جوهر تجاربنا تدريب LSTM عميقة كبيرة على العديد من أزواج الجمل. دربناها عن طريق تعظيم اللوغاريتم الاحتمالي للترجمة الصحيحة $T$ بالنظر إلى الجملة المصدر $S$، لذلك فإن هدف التدريب هو

$$\frac{1}{|S|} \sum_{(T,S) \in S} \log p(T|S)$$

حيث $S$ هي مجموعة التدريب. بمجرد اكتمال التدريب، ننتج الترجمات عن طريق إيجاد الترجمة الأكثر احتمالاً وفقاً لـ LSTM:

$$\hat{T} = \arg\max_T p(T|S) \quad (2)$$

نبحث عن الترجمة الأكثر احتمالاً باستخدام مفكك بحث شعاعي بسيط من اليسار إلى اليمين يحافظ على عدد صغير $B$ من الفرضيات الجزئية، حيث الفرضية الجزئية هي بادئة لبعض الترجمة. في كل خطوة زمنية نمدد كل فرضية جزئية في الشعاع بكل كلمة ممكنة في المفردات. هذا يزيد بشكل كبير من عدد الفرضيات لذلك نتجاهل كل شيء ما عدا الفرضيات $B$ الأكثر احتمالاً وفقاً لاحتمال اللوغاريتم للنموذج. بمجرد إلحاق رمز "<EOS>" بفرضية، تتم إزالتها من الشعاع وتُضاف إلى مجموعة الفرضيات الكاملة. بينما هذا المفكك تقريبي، فإنه بسيط للتنفيذ. من المثير للاهتمام، أن نظامنا يؤدي بشكل جيد حتى مع حجم شعاع 1، وشعاع بحجم 2 يوفر معظم فوائد البحث الشعاعي (الجدول 1).

استخدمنا أيضاً LSTM لإعادة تصنيف قوائم أفضل 1000 التي أنتجها النظام الأساسي [29]. لإعادة تصنيف قائمة n-best، حسبنا احتمال اللوغاريتم لكل فرضية باستخدام LSTM الخاصة بنا وأخذنا متوسطاً متساوياً مع درجتهم ودرجة LSTM.

**3.3 عكس الجمل المصدر**

بينما LSTM قادرة على حل المشاكل ذات التبعيات طويلة المدى، اكتشفنا أن LSTM تتعلم بشكل أفضل بكثير عندما يتم عكس الجمل المصدر (لا يتم عكس الجمل المستهدفة). من خلال القيام بذلك، انخفض معدل الحيرة لاختبار LSTM من 5.8 إلى 4.7، وزادت درجات BLEU لاختبار ترجماتها المفككة من 25.9 إلى 30.6.

بينما ليس لدينا تفسير كامل لهذه الظاهرة، نعتقد أنها ناتجة عن إدخال العديد من التبعيات قصيرة المدى إلى مجموعة البيانات. عادة، عندما نربط جملة مصدر مع جملة مستهدفة، تكون كل كلمة في الجملة المصدر بعيدة عن كلمتها المقابلة في الجملة المستهدفة. ونتيجة لذلك، تحتوي المشكلة على "تأخير زمني أدنى" كبير [17]. من خلال عكس الكلمات في الجملة المصدر، تظل المسافة المتوسطة بين الكلمات المقابلة في اللغة المصدر واللغة الهدف دون تغيير. ومع ذلك، فإن الكلمات القليلة الأولى في اللغة المصدر الآن قريبة جداً من الكلمات القليلة الأولى في اللغة الهدف، لذلك يتم تقليل التأخير الزمني الأدنى للمشكلة بشكل كبير. وبالتالي، يكون للانتشار العكسي وقت أسهل في "إنشاء الاتصال" بين الجملة المصدر والجملة المستهدفة، مما يؤدي بدوره إلى تحسين الأداء العام بشكل كبير.

في البداية، اعتقدنا أن عكس جمل الإدخال سيؤدي فقط إلى تنبؤات أكثر ثقة في الأجزاء المبكرة من الجملة المستهدفة وإلى تنبؤات أقل ثقة في الأجزاء اللاحقة. ومع ذلك، فإن شبكات LSTM المدربة على الجمل المصدر المعكوسة أدت بشكل أفضل بكثير على الجمل الطويلة من شبكات LSTM المدربة على الجمل المصدر الخام (انظر القسم 3.7)، مما يشير إلى أن عكس جمل الإدخال ينتج عنه شبكات LSTM ذات استخدام أفضل للذاكرة.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:** beam search, partial hypothesis, n-best rescoring, minimal time lag, perplexity
- **Equations:** 2 equations (training objective and decoding objective)
- **Citations:** [29, 17]
- **Special handling:** Technical discussion of decoder implementation and reversing trick

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.86
