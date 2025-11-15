# Section 3: Results
## القسم 3: النتائج

**Section:** results
**Translation Quality:** 0.86
**Glossary Terms Used:** accuracy, training data, semantic, syntactic, benchmark, dataset, computational complexity, dimensionality, epoch

---

### English Version

To compare the quality of different versions of word vectors, previous papers typically use a table showing example words and their most similar words, and understand them intuitively. Although it is easy to show that word France is similar to Italy and perhaps some other countries, it is much more challenging to show that for example the word for big and bigger has a similar relationship as for small and smaller. We follow previous observation that there is a large number of types of similarities that can be exploited for training and evaluation of word vectors, and present a new comprehensive test set that contains five types of semantic questions, and nine types of syntactic questions.

#### 3.1 Task Description

The Semantic-Syntactic Word Relationship test set contains examples like: big → bigger as small → ?. The test set contains 8869 semantic questions and 10675 syntactic questions. Each category contains examples of a specific type of relationship. For the semantic questions, there are categories like: capital-common-countries (e.g. Athens-Greece, Oslo-Norway), capital-world (e.g. Abuja-Nigeria, Astana-Kazakhstan), currency (e.g. Angola-kwanza, Iran-rial), city-in-state (e.g. Chicago-Illinois, Stockton-California), man-woman (e.g. brother-sister, grandson-granddaughter). For the syntactic questions, there are categories like: adjectives to adverbs (e.g. amazing-amazingly, apparent-apparently), opposite (e.g. acceptable-unacceptable, aware-unaware), comparative (e.g. bad-worse, big-bigger), superlative (e.g. bad-worst, big-biggest), present-participle (e.g. code-coding, dance-dancing), nationality-adjective (e.g. Albania-Albanian, Argentina-Argentinean), past-tense (e.g. dancing-danced, decreasing-decreased), plural-nouns (e.g. banana-bananas, bird-birds), and plural-verbs (e.g. decrease-decreases, describe-describes).

We note that the test set is designed in such a way that different types of relationships are distributed evenly. We provide the test set for research purposes.

#### 3.2 Maximization of Accuracy

The task is to find the answer using the most similar word vector, according to the cosine distance (we discard the input question words during this search). The overall accuracy is defined as the total number of correct answers divided by the total number of questions. The question is assumed to be correctly answered only if the closest word to the vector computed from the question is exactly the same as the correct answer from the test set; synonyms are thus counted as errors. This also means that reaching 100% accuracy is likely to be impossible, as the current models do not have any input information about word morphology. However, we believe that usefulness of the word vectors for certain applications should be positively correlated with this accuracy metric.

The accuracy depends mainly on three parameters: the training data size, the model architecture, and the dimensionality of the word vectors.

#### 3.3 Comparison of Model Architectures

First we compare different model architectures for deriving the word vectors using the same training data. In the further experiments, we use full set of questions in the new Semantic-Syntactic Word Relationship test set, i.e., unrestricted to only questions containing test set words. We trained several architectures: the Feedforward NNLM proposed in [1], the Recurrent NNLM proposed in [15], and the new proposed CBOW and Skip-gram models.

The results are summarized in Table 1. The RNNLM performs better than NNLM, and the best results are achieved by the new Skip-gram model. One surprising result is that the Skip-gram model works well with very high dimensional vectors, even better than with the more commonly used dimensionality of 200. This is probably because in Skip-gram model, different parts of the vectors become specialized on different types of relationships.

We also experimented with the hierarchical softmax that became popular after the publication of [23]. We found that the binary Huffman tree with target frequency-based encoding gives better performance than the balanced binary tree. When we compare the results of the CBOW and Skip-gram models trained on the same data with different hyper-parameters, the best configuration of CBOW achieves about 50% accuracy, while the best Skip-gram model achieves about 55% accuracy.

#### 3.4 Large Scale Parallel Training of Models

As mentioned earlier, we have implemented various models in a distributed framework called DistBelief. Below we report the results of several models trained on the Google News corpus. We used different model architectures and different training data sizes. The training data size varies from 6B tokens to 783B tokens. For all the following experiments, we used the same test set as described in Section 3.1.

The results are presented in Table 2. For the Skip-gram model, we experimented with 640-dimensional word vectors and used negative sampling with 5 negative samples. The training took three days using one hundred machines, each with sixteen CPU cores. Accuracy on the syntactic questions increases from 53% (using 6B training words) to 66% (using 783B training words), and accuracy on semantic questions increases from 55% to 60%. We found that doubling the amount of training data increases accuracy by 2-4%.

Interestingly, we found that the accuracy on the semantic test set improves more slowly with increasing model size than the accuracy on the syntactic test set. This suggests that the current training set of semantic questions is easier to fit, and the model becomes mostly limited by the semantic test set size rather than the training data size.

We also tested the performance of our vectors on the Microsoft sentence completion challenge [32]. The task is to select the most coherent sentence from five given sentences, where one word is missing and must be selected from five candidate words. Using a single model with Skip-gram vectors, we achieved 58.9% accuracy on this task. The previous state-of-the-art published result is 55.4% [19], and human performance is estimated at 63.4%.

---

### النسخة العربية

لمقارنة جودة الإصدارات المختلفة من متجهات الكلمات، عادةً ما تستخدم الأوراق السابقة جدولاً يوضح أمثلة الكلمات والكلمات الأكثر تشابهاً معها، وفهمها بشكل حدسي. على الرغم من أنه من السهل إظهار أن كلمة فرنسا مشابهة لإيطاليا وربما بعض البلدان الأخرى، إلا أنه من الأصعب بكثير إظهار أن كلمة كبير وأكبر لها علاقة مماثلة لكلمة صغير وأصغر على سبيل المثال. نتبع الملاحظة السابقة بأن هناك عدداً كبيراً من أنواع التشابهات التي يمكن استغلالها لتدريب وتقييم متجهات الكلمات، ونقدم مجموعة اختبار شاملة جديدة تحتوي على خمسة أنواع من الأسئلة الدلالية، وتسعة أنواع من الأسئلة النحوية.

#### 3.1 وصف المهمة

تحتوي مجموعة اختبار العلاقات الدلالية-النحوية للكلمات على أمثلة مثل: كبير ← أكبر كما صغير ← ؟. تحتوي مجموعة الاختبار على 8869 سؤالاً دلالياً و10675 سؤالاً نحوياً. كل فئة تحتوي على أمثلة لنوع معين من العلاقات. بالنسبة للأسئلة الدلالية، هناك فئات مثل: العاصمة-الدول الشائعة (مثل أثينا-اليونان، أوسلو-النرويج)، العاصمة-العالم (مثل أبوجا-نيجيريا، أستانا-كازاخستان)، العملة (مثل أنغولا-كوانزا، إيران-ريال)، المدينة-في-الولاية (مثل شيكاغو-إلينوي، ستوكتون-كاليفورنيا)، رجل-امرأة (مثل أخ-أخت، حفيد-حفيدة). بالنسبة للأسئلة النحوية، هناك فئات مثل: الصفات إلى الظروف (مثل مذهل-بشكل مذهل، واضح-بوضوح)، العكس (مثل مقبول-غير مقبول، واعٍ-غير واعٍ)، المقارنة (مثل سيء-أسوأ، كبير-أكبر)، التفضيل (مثل سيء-الأسوأ، كبير-الأكبر)، المضارع-اسم الفاعل (مثل برمجة-البرمجة، رقص-الرقص)، الجنسية-الصفة (مثل ألبانيا-ألباني، الأرجنتين-أرجنتيني)، الماضي (مثل الرقص-رقص، التناقص-تناقص)، الأسماء الجمع (مثل موز-موز، طائر-طيور)، والأفعال الجمع (مثل ينقص-ينقصون، يصف-يصفون).

نلاحظ أن مجموعة الاختبار مصممة بحيث يتم توزيع أنواع مختلفة من العلاقات بشكل متساوٍ. نقدم مجموعة الاختبار لأغراض البحث.

#### 3.2 تعظيم الدقة

المهمة هي إيجاد الإجابة باستخدام متجه الكلمة الأكثر تشابهاً، وفقاً لمسافة جيب التمام (نتجاهل كلمات السؤال المدخلة أثناء هذا البحث). يتم تعريف الدقة الإجمالية على أنها العدد الإجمالي للإجابات الصحيحة مقسوماً على العدد الإجمالي للأسئلة. يُفترض أن السؤال قد تمت الإجابة عليه بشكل صحيح فقط إذا كانت الكلمة الأقرب إلى المتجه المحسوب من السؤال هي نفسها تماماً الإجابة الصحيحة من مجموعة الاختبار؛ وبالتالي تُحسب المرادفات كأخطاء. هذا يعني أيضاً أن الوصول إلى دقة 100٪ من المحتمل أن يكون مستحيلاً، حيث أن النماذج الحالية ليس لديها أي معلومات إدخال حول صرف الكلمات. ومع ذلك، نعتقد أن فائدة متجهات الكلمات لتطبيقات معينة يجب أن تكون مرتبطة إيجابياً بمقياس الدقة هذا.

تعتمد الدقة بشكل أساسي على ثلاثة معاملات: حجم بيانات التدريب، ومعمارية النموذج، وأبعاد متجهات الكلمات.

#### 3.3 مقارنة معماريات النماذج

أولاً نقارن معماريات النماذج المختلفة لاشتقاق متجهات الكلمات باستخدام نفس بيانات التدريب. في التجارب الإضافية، نستخدم المجموعة الكاملة من الأسئلة في مجموعة اختبار العلاقات الدلالية-النحوية للكلمات الجديدة، أي غير مقيدة بالأسئلة التي تحتوي على كلمات مجموعة الاختبار فقط. قمنا بتدريب عدة معماريات: NNLM بالتغذية الأمامية المقترح في [1]، وRNNLM المتكرر المقترح في [15]، ونماذج CBOW وSkip-gram الجديدة المقترحة.

يتم تلخيص النتائج في الجدول 1. يؤدي RNNLM أداءً أفضل من NNLM، وأفضل النتائج يتم تحقيقها بواسطة نموذج Skip-gram الجديد. إحدى النتائج المفاجئة هي أن نموذج Skip-gram يعمل بشكل جيد مع متجهات عالية الأبعاد، بل وأفضل من الأبعاد الأكثر استخداماً وهي 200. هذا على الأرجح لأن في نموذج Skip-gram، تتخصص أجزاء مختلفة من المتجهات في أنواع مختلفة من العلاقات.

جربنا أيضاً softmax الهرمي الذي أصبح شائعاً بعد نشر [23]. وجدنا أن شجرة هافمان الثنائية مع الترميز القائم على تردد الهدف تعطي أداءً أفضل من الشجرة الثنائية المتوازنة. عندما نقارن نتائج نماذج CBOW وSkip-gram المدربة على نفس البيانات بمعاملات فائقة مختلفة، فإن أفضل تكوين لـ CBOW يحقق حوالي 50٪ دقة، بينما يحقق أفضل نموذج Skip-gram حوالي 55٪ دقة.

#### 3.4 التدريب المتوازي واسع النطاق للنماذج

كما ذكرنا سابقاً، قمنا بتنفيذ نماذج مختلفة في إطار عمل موزع يسمى DistBelief. أدناه نبلغ عن نتائج عدة نماذج مدربة على مدونة أخبار جوجل. استخدمنا معماريات نماذج مختلفة وأحجام بيانات تدريب مختلفة. يختلف حجم بيانات التدريب من 6 مليار رمز إلى 783 مليار رمز. لجميع التجارب التالية، استخدمنا نفس مجموعة الاختبار كما هو موضح في القسم 3.1.

يتم تقديم النتائج في الجدول 2. بالنسبة لنموذج Skip-gram، جربنا متجهات كلمات بأبعاد 640 واستخدمنا أخذ العينات السلبي مع 5 عينات سلبية. استغرق التدريب ثلاثة أيام باستخدام مائة جهاز، كل منها بستة عشر نواة معالجة مركزية. تزداد الدقة على الأسئلة النحوية من 53٪ (باستخدام 6 مليارات كلمة تدريب) إلى 66٪ (باستخدام 783 مليار كلمة تدريب)، وتزداد الدقة على الأسئلة الدلالية من 55٪ إلى 60٪. وجدنا أن مضاعفة كمية بيانات التدريب تزيد الدقة بنسبة 2-4٪.

من المثير للاهتمام أننا وجدنا أن الدقة على مجموعة الاختبار الدلالية تتحسن بشكل أبطأ مع زيادة حجم النموذج مقارنة بالدقة على مجموعة الاختبار النحوية. هذا يشير إلى أن مجموعة التدريب الحالية من الأسئلة الدلالية أسهل في الملاءمة، ويصبح النموذج محدوداً في الغالب بحجم مجموعة الاختبار الدلالية بدلاً من حجم بيانات التدريب.

اختبرنا أيضاً أداء متجهاتنا في تحدي إكمال الجملة من مايكروسوفت [32]. المهمة هي اختيار الجملة الأكثر تماسكاً من بين خمس جمل معطاة، حيث كلمة واحدة مفقودة ويجب اختيارها من خمس كلمات مرشحة. باستخدام نموذج واحد مع متجهات Skip-gram، حققنا دقة 58.9٪ في هذه المهمة. النتيجة المنشورة الأحدث والأفضل سابقاً هي 55.4٪ [19]، ويُقدر الأداء البشري بـ 63.4٪.

---

### Translation Notes

- **Tables referenced:** Table 1, Table 2
- **Key terms introduced:** semantic-syntactic test set, cosine distance, accuracy metric, negative sampling, Microsoft sentence completion challenge, word morphology
- **Equations:** 0
- **Citations:** [1], [15], [23], [32], [19]
- **Special handling:** Detailed description of test categories and evaluation metrics; preserving exact accuracy percentages and data sizes

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.86

### Back-Translation (Validation)

To compare the quality of different versions of word vectors, previous papers typically use a table showing example words and their most similar words, and understand them intuitively. Although it is easy to show that the word France is similar to Italy and perhaps some other countries, it is much more difficult to show that for example the word big and bigger has a similar relationship as small and smaller.

The test set contains 8869 semantic questions and 10675 syntactic questions. Each category contains examples of a specific type of relationship.

Accuracy on syntactic questions increases from 53% (using 6 billion training words) to 66% (using 783 billion training words), and accuracy on semantic questions increases from 55% to 60%.
