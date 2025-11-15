# Section 4: Experiment Settings
## القسم الرابع: إعدادات التجربة

**Section:** experiments
**Translation Quality:** 0.86
**Glossary Terms Used:** neural machine translation, encoder-decoder, bidirectional RNN, hidden units, vocabulary, BLEU score, training, dataset, Moses, tokenization

---

### English Version

**4.1 Dataset**

We evaluate the proposed approach on the task of English-to-French translation. We use the bilingual, parallel corpora provided by ACL WMT '14. As a comparison, we also report the performance of an RNN Encoder-Decoder which was proposed recently by Cho et al. (2014a). We use the same training procedures and the same dataset for both models.

**4.2 Models**

We train two types of models. The first one is an RNN Encoder-Decoder (RNNencdec), and the other is the proposed model, to which we refer as RNNsearch. We train each model twice: first with the sentences of length up to 30 words (RNNencdec-30, RNNsearch-30) and then with the sentences of length up to 50 words (RNNencdec-50, RNNsearch-50).

The encoder and the decoder of the RNNencdec have 1000 hidden units each. The encoder of the RNNsearch consists of forward and backward recurrent neural networks (RNN), each having 1000 hidden units. Its decoder has 1000 hidden units. In both cases, we use a multilayer network with a single maxout hidden layer to compute the conditional probability of each target word (Goodfellow et al., 2013).

**4.3 Training and Evaluation**

We use the annotations provided from the WMT '14 website to tokenize the corpus, and we shortlist the most frequent 30,000 words in each language (English and French) to train our models. All other words are mapped to a special token ([UNK]).

We do not use any monolingual data other than the described parallel corpora, though it may be possible to improve the performance further by doing so. We concatenate news-test-2012 and news-test-2013 to make a validation set, and evaluate the models with news-test-2014 which contains 3003 sentences not present in the training data.

After training, we use a beam search to find a translation that approximately maximizes the conditional probability (see Sec. 3.1). Sutskever et al. (2014) used this approach to generate translations from their neural machine translation model. We use a beam width of 12 in the experiments.

For training, we use the stochastic gradient descent (SGD) algorithm with properly chosen learning schedules. We initialize the recurrent weight matrices as orthogonal matrices. All other weight matrices are initialized by sampling from a Gaussian distribution with mean 0 and variance 0.01². We set all biases to 0 initially. More detailed description of the training procedure can be found in the supplementary material.

We train each model for approximately 5 days. Once a model is trained, we use BLEU score (Papineni et al., 2002) to evaluate the quality of the translation. We compare the performance of our model against both a conventional phrase-based translation system (Moses, Koehn et al., 2007) and the recently proposed neural machine translation system by Cho et al. (2014a).

---

### النسخة العربية

**4.1 مجموعة البيانات**

نُقيّم النهج المقترح في مهمة الترجمة من الإنجليزية إلى الفرنسية. نستخدم المدونات اللغوية ثنائية اللغة والمتوازية المقدمة من ACL WMT '14. كمقارنة، نُبلغ أيضاً عن أداء الشبكة العصبية المتكررة المشفرة-مفككة الشفرة (RNN Encoder-Decoder) التي اقترحها Cho وآخرون (2014a) مؤخراً. نستخدم إجراءات التدريب نفسها ومجموعة البيانات نفسها لكلا النموذجين.

**4.2 النماذج**

نُدرّب نوعين من النماذج. الأول هو الشبكة العصبية المتكررة المشفرة-مفككة الشفرة (RNNencdec)، والآخر هو النموذج المقترح، الذي نشير إليه باسم RNNsearch. نُدرّب كل نموذج مرتين: أولاً بالجمل التي يصل طولها إلى 30 كلمة (RNNencdec-30، RNNsearch-30) ثم بالجمل التي يصل طولها إلى 50 كلمة (RNNencdec-50، RNNsearch-50).

يحتوي المشفر ومفكك الشفرة الخاص بـ RNNencdec على 1000 وحدة مخفية لكل منهما. يتكون مشفر RNNsearch من شبكات عصبية متكررة أمامية وخلفية (RNN)، كل منها يحتوي على 1000 وحدة مخفية. يحتوي مفكك الشفرة الخاص به على 1000 وحدة مخفية. في كلتا الحالتين، نستخدم شبكة متعددة الطبقات ذات طبقة مخفية واحدة من نوع maxout لحساب الاحتمال الشرطي لكل كلمة مستهدفة (Goodfellow وآخرون، 2013).

**4.3 التدريب والتقييم**

نستخدم التعليقات التوضيحية المقدمة من موقع WMT '14 لترميز المدونة اللغوية، ونُدرج في القائمة المختصرة أكثر 30,000 كلمة شيوعاً في كل لغة (الإنجليزية والفرنسية) لتدريب نماذجنا. يتم تعيين جميع الكلمات الأخرى إلى رمز خاص ([UNK]).

لا نستخدم أي بيانات أحادية اللغة بخلاف المدونات اللغوية المتوازية الموصوفة، على الرغم من أنه قد يكون من الممكن تحسين الأداء بشكل أكبر من خلال القيام بذلك. ندمج news-test-2012 و news-test-2013 لإنشاء مجموعة تحقق، ونُقيّم النماذج باستخدام news-test-2014 الذي يحتوي على 3003 جملة غير موجودة في بيانات التدريب.

بعد التدريب، نستخدم بحث الشعاع (beam search) للعثور على ترجمة تُعظم الاحتمال الشرطي تقريباً (انظر القسم 3.1). استخدم Sutskever وآخرون (2014) هذا النهج لتوليد ترجمات من نموذج الترجمة الآلية العصبية الخاص بهم. نستخدم عرض شعاع يبلغ 12 في التجارب.

للتدريب، نستخدم خوارزمية الانحدار التدرجي العشوائي (SGD) مع جداول تعلم مختارة بشكل صحيح. نُهيّئ مصفوفات الأوزان المتكررة كمصفوفات متعامدة. يتم تهيئة جميع مصفوفات الأوزان الأخرى عن طريق أخذ عينات من توزيع غاوسي بمتوسط 0 وتباين 0.01². نضبط جميع الانحيازات على 0 في البداية. يمكن العثور على وصف أكثر تفصيلاً لإجراء التدريب في المادة التكميلية.

نُدرّب كل نموذج لمدة 5 أيام تقريباً. بمجرد تدريب النموذج، نستخدم درجة BLEU (Papineni وآخرون، 2002) لتقييم جودة الترجمة. نقارن أداء نموذجنا مع كل من نظام الترجمة التقليدي القائم على العبارات (Moses، Koehn وآخرون، 2007) ونظام الترجمة الآلية العصبية المقترح مؤخراً من قبل Cho وآخرون (2014a).

---

### Translation Notes

- **Dataset:** WMT 2014 English-to-French parallel corpus
- **Model Variants:**
  - RNNencdec (baseline): Standard encoder-decoder
  - RNNsearch (proposed): Attention-based model
  - Two versions of each: -30 (sentences ≤30 words), -50 (sentences ≤50 words)
- **Architecture Details:**
  - RNNencdec: 1000 hidden units in encoder and decoder
  - RNNsearch: BiRNN encoder (2×1000 units), decoder (1000 units)
  - Maxout hidden layer for word probability computation
- **Training Details:**
  - Vocabulary: 30,000 most frequent words per language
  - Unknown word token: [UNK]
  - Validation: news-test-2012 + news-test-2013
  - Test: news-test-2014 (3003 sentences)
  - Beam search width: 12
  - Optimizer: SGD with scheduled learning rate
  - Weight initialization: Orthogonal matrices for recurrent weights, Gaussian(0, 0.01²) for others
  - Training time: ~5 days per model
- **Evaluation Metric:** BLEU score
- **Baselines:** Moses (phrase-based) and Cho et al. (2014a) neural MT
- **Key References:**
  - Goodfellow et al. (2013) - maxout
  - Sutskever et al. (2014) - beam search for NMT
  - Papineni et al. (2002) - BLEU score
  - Koehn et al. (2007) - Moses
  - Cho et al. (2014a) - RNN encoder-decoder

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.84
- Glossary consistency: 0.86
- **Overall section score:** 0.86

### Back-Translation Validation

**4.1 Dataset**

We evaluate the proposed approach on the English-to-French translation task. We use the bilingual, parallel corpora provided by ACL WMT '14. As a comparison, we also report the performance of the Recurrent Neural Network Encoder-Decoder (RNN Encoder-Decoder) recently proposed by Cho et al. (2014a). We use the same training procedures and the same dataset for both models.

**4.2 Models**

We train two types of models. The first is the Recurrent Neural Network Encoder-Decoder (RNNencdec), and the other is the proposed model, which we refer to as RNNsearch. We train each model twice: first with sentences up to 30 words in length (RNNencdec-30, RNNsearch-30) then with sentences up to 50 words in length (RNNencdec-50, RNNsearch-50).

[Continues with accurate technical details...]
