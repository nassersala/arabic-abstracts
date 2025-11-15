# Section 4: Experiment Settings
## القسم 4: إعدادات التجارب

**Section:** Experiment Settings
**Translation Quality:** 0.86
**Glossary Terms Used:** dataset, parallel corpora, bilingual, training, validation, test set, tokenization, vocabulary, minibatch, stochastic gradient descent (SGD), Adadelta, maxout, beam search, hidden units

---

### English Version

We evaluate the proposed approach on the task of English-to-French translation. We use the bilingual, parallel corpora provided by ACL WMT '14. As a comparison, we also report the performance of an RNN Encoder–Decoder which was proposed recently by Cho et al. (2014a). We use the same training procedures and the same dataset for both models.

**4.1 DATASET**

WMT '14 contains the following English-French parallel corpora: Europarl (61M words), news commentary (5.5M), UN (421M) and two crawled corpora of 90M and 272.5M words respectively, totaling 850M words. Following the procedure described in Cho et al. (2014a), we reduce the size of the combined corpus to have 348M words using the data selection method by Axelrod et al. (2011). We do not use any monolingual data other than the mentioned parallel corpora, although it may be possible to use a much larger monolingual corpus to pretrain an encoder. We concatenate news-test-2012 and news-test-2013 to make a development (validation) set, and evaluate the models on the test set (news-test-2014) from WMT '14, which consists of 3003 sentences not present in the training data.

After a usual tokenization, we use a shortlist of 30,000 most frequent words in each language to train our models. Any word not included in the shortlist is mapped to a special token ([UNK]). We do not apply any other special preprocessing, such as lowercasing or stemming, to the data.

**4.2 MODELS**

We train two types of models. The first one is an RNN Encoder–Decoder (RNNencdec, Cho et al., 2014a), and the other is the proposed model, to which we refer as RNNsearch. We train each model twice: first with the sentences of length up to 30 words (RNNencdec-30, RNNsearch-30) and then with the sentences of length up to 50 word (RNNencdec-50, RNNsearch-50).

The encoder and decoder of the RNNencdec have 1000 hidden units each. The encoder of the RNNsearch consists of forward and backward recurrent neural networks (RNN) each having 1000 hidden units. Its decoder has 1000 hidden units. In both cases, we use a multilayer network with a single maxout (Goodfellow et al., 2013) hidden layer to compute the conditional probability of each target word (Pascanu et al., 2014).

We use a minibatch stochastic gradient descent (SGD) algorithm together with Adadelta (Zeiler, 2012) to train each model. Each SGD update direction is computed using a minibatch of 80 sentences. We trained each model for approximately 5 days.

Once a model is trained, we use a beam search to find a translation that approximately maximizes the conditional probability (see, e.g., Graves, 2012; Boulanger-Lewandowski et al., 2013). Sutskever et al. (2014) used this approach to generate translations from their neural machine translation model.

For more details on the architectures of the models and training procedure used in the experiments, see Appendices A and B.

---

### النسخة العربية

نقيّم النهج المقترح على مهمة الترجمة من الإنجليزية إلى الفرنسية. نستخدم المدونات المتوازية ثنائية اللغة المقدمة من ACL WMT '14. كمقارنة، نبلغ أيضاً عن أداء المشفر-مفكك الشفرة للشبكة العصبية التكرارية الذي اقترحه مؤخراً تشو وآخرون (2014أ). نستخدم نفس إجراءات التدريب ونفس مجموعة البيانات لكلا النموذجين.

**4.1 مجموعة البيانات**

تحتوي WMT '14 على المدونات المتوازية الإنجليزية-الفرنسية التالية: يوروبارل (61 مليون كلمة)، تعليقات الأخبار (5.5 مليون)، الأمم المتحدة (421 مليون)، ومدونتان مجمعتان بـ 90 مليون و 272.5 مليون كلمة على التوالي، بإجمالي 850 مليون كلمة. باتباع الإجراء الموصوف في تشو وآخرون (2014أ)، نقلل حجم المدونة المجمعة لتحتوي على 348 مليون كلمة باستخدام طريقة اختيار البيانات من أكسلرود وآخرون (2011). لا نستخدم أي بيانات أحادية اللغة بخلاف المدونات المتوازية المذكورة، على الرغم من أنه قد يكون من الممكن استخدام مدونة أحادية اللغة أكبر بكثير للتدريب المسبق للمشفر. نربط news-test-2012 و news-test-2013 لإنشاء مجموعة تطوير (تحقق)، ونقيّم النماذج على مجموعة الاختبار (news-test-2014) من WMT '14، والتي تتكون من 3003 جملة غير موجودة في بيانات التدريب.

بعد التجزئة المعتادة، نستخدم قائمة مختصرة من 30,000 كلمة الأكثر تكراراً في كل لغة لتدريب نماذجنا. يتم ربط أي كلمة غير مدرجة في القائمة المختصرة برمز خاص ([UNK]). لا نطبق أي معالجة مسبقة خاصة أخرى، مثل تحويل الأحرف إلى صغيرة أو استخلاص الجذور، على البيانات.

**4.2 النماذج**

ندرب نوعين من النماذج. الأول هو المشفر-مفكك الشفرة للشبكة العصبية التكرارية (RNNencdec، تشو وآخرون، 2014أ)، والآخر هو النموذج المقترح، والذي نشير إليه باسم RNNsearch. ندرب كل نموذج مرتين: أولاً بجمل يصل طولها إلى 30 كلمة (RNNencdec-30، RNNsearch-30) ثم بجمل يصل طولها إلى 50 كلمة (RNNencdec-50، RNNsearch-50).

يحتوي المشفر ومفكك الشفرة لـ RNNencdec على 1000 وحدة مخفية لكل منهما. يتكون مشفر RNNsearch من شبكات عصبية تكرارية أمامية وخلفية، تحتوي كل منها على 1000 وحدة مخفية. يحتوي مفكك الشفرة الخاص به على 1000 وحدة مخفية. في كلتا الحالتين، نستخدم شبكة متعددة الطبقات مع طبقة مخفية واحدة من نوع maxout (جودفيلو وآخرون، 2013) لحساب الاحتمال الشرطي لكل كلمة مستهدفة (باسكانو وآخرون، 2014).

نستخدم خوارزمية الانحدار التدرجي العشوائي (SGD) بالحزم الصغيرة مع Adadelta (زيلر، 2012) لتدريب كل نموذج. يتم حساب كل اتجاه تحديث لـ SGD باستخدام حزمة صغيرة من 80 جملة. دربنا كل نموذج لمدة 5 أيام تقريباً.

بمجرد تدريب النموذج، نستخدم بحث الشعاع للعثور على ترجمة تعظم تقريباً الاحتمال الشرطي (انظر، على سبيل المثال، جريفز، 2012؛ بولانجر-ليواندوسكي وآخرون، 2013). استخدم سوتسكيفر وآخرون (2014) هذا النهج لتوليد ترجمات من نموذج الترجمة الآلية العصبية الخاص بهم.

لمزيد من التفاصيل حول معماريات النماذج وإجراءات التدريب المستخدمة في التجارب، انظر الملاحق أ و ب.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - WMT (ورشة عمل الترجمة الآلية - kept as WMT)
  - parallel corpora (مدونات متوازية)
  - bilingual (ثنائية اللغة)
  - tokenization (التجزئة)
  - shortlist (قائمة مختصرة)
  - unknown token [UNK] (رمز خاص [UNK])
  - lowercasing (تحويل الأحرف إلى صغيرة)
  - stemming (استخلاص الجذور)
  - minibatch SGD (الانحدار التدرجي العشوائي بالحزم الصغيرة)
  - Adadelta (kept as is - algorithm name)
  - maxout (kept as is - activation function name)
  - beam search (بحث الشعاع)
  - hidden units (وحدات مخفية)
- **Equations:** None
- **Citations:** Multiple references to datasets and prior work
- **Special handling:**
  - Dataset names and sizes preserved
  - Model names (RNNencdec, RNNsearch) kept in English as they are proper names
  - Algorithm names (Adadelta, maxout) kept in English as conventional

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.86

### Back-Translation (Key Paragraph)

"We train two types of models. The first is the RNN Encoder-Decoder (RNNencdec, Cho et al., 2014a), and the other is the proposed model, which we refer to as RNNsearch. We train each model twice: first with sentences up to 30 words in length (RNNencdec-30, RNNsearch-30) and then with sentences up to 50 words in length (RNNencdec-50, RNNsearch-50)."

**Validation:** ✅ Accurate preservation of experimental setup details.
