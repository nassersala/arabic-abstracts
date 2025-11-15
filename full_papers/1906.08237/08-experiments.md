# Section 3: Experiments
## القسم 3: التجارب

**Section:** experiments
**Translation Quality:** 0.85
**Glossary Terms Used:** pretraining, BERT, BooksCorpus, Wikipedia, tokenization, SentencePiece, TPU, Adam optimizer, learning rate decay, batch size, ablation study, finetuning, SQuAD, RACE, MNLI, reading comprehension, question answering, text classification, document ranking, RoBERTa

---

### English Version

## 3.1 Pretraining and Implementation

Following BERT [10], we use the BooksCorpus [40] and English Wikipedia as part of our pretraining data, which have 13GB plain text combined. In addition, we include Giga5 (16GB text) [26], ClueWeb 2012-B (extended from [5]), and Common Crawl [6] for pretraining. We use heuristics to aggressively filter out short or low-quality articles for ClueWeb 2012-B and Common Crawl, which results in 19GB and 110GB text respectively. After tokenization with SentencePiece [17], we obtain 2.78B, 1.09B, 4.75B, 4.30B, and 19.97B subword pieces for Wikipedia, BooksCorpus, Giga5, ClueWeb, and Common Crawl respectively, which are 32.89B in total.

Our largest model XLNet-Large has the same architecture hyperparameters as BERT-Large, which results in a similar model size. During pretraining, we always use a full sequence length of 512. Firstly, to provide a fair comparison with BERT (section 3.2), we also trained XLNet-Large-wikibooks on BooksCorpus and Wikipedia only, where we reuse all pretraining hyper-parameters as in the original BERT. Then, we scale up the training of XLNet-Large by using all the datasets described above. Specifically, we train on 512 TPU v3 chips for 500K steps with an Adam weight decay optimizer, linear learning rate decay, and a batch size of 8192, which takes about 5.5 days. It was observed that the model still underfits the data at the end of training. Finally, we perform ablation study (section 3.4) based on the XLNet-Base-wikibooks.

Since the recurrence mechanism is introduced, we use a bidirectional data input pipeline where each of the forward and backward directions takes half of the batch size. For training XLNet-Large, we set the partial prediction constant K as 6 (see Section 2.3). Our finetuning procedure follows BERT [10] except otherwise specified. We employ an idea of span-based prediction, where we first sample a length L ∈ [1, · · · , 5], and then randomly select a consecutive span of L tokens as prediction targets within a context of (KL) tokens.

We use a variety of natural language understanding datasets to evaluate the performance of our method. Detailed descriptions of the settings for all the datasets can be found in Appendix A.3.

## 3.2 Fair Comparison with BERT

Here, we first compare the performance of BERT and XLNet in a fair setting to decouple the effects of using more data and the improvement from BERT to XLNet. In Table 1, we compare (1) best performance of three different variants of BERT and (2) XLNet trained with the same data and hyperparameters. As we can see, trained on the same data with an almost identical training recipe, XLNet outperforms BERT by a sizable margin on all the considered datasets.

**Table 1: Fair comparison with BERT.** All models are trained using the same data and hyperparameters as in BERT. We use the best of 3 BERT variants for comparison; i.e., the original BERT, BERT with whole word masking, and BERT without next sentence prediction.

| Model | SQuAD1.1 | SQuAD2.0 | RACE | MNLI | QNLI | QQP | RTE | SST-2 | MRPC | CoLA | STS-B |
|-------|----------|----------|------|------|------|-----|-----|-------|------|------|-------|
| BERT-Large (Best of 3) | 86.7/92.8 | 82.8/85.5 | 75.1 | 87.3 | 93.0 | 91.4 | 74.0 | 94.0 | 88.7 | 63.7 | 90.2 |
| XLNet-Large-wikibooks | 88.2/94.0 | 85.1/87.8 | 77.4 | 88.4 | 93.9 | 91.8 | 81.2 | 94.4 | 90.0 | 65.2 | 91.1 |

## 3.3 Comparison with RoBERTa: Scaling Up

After the initial publication of our manuscript, a few other pretrained models were released such as RoBERTa [21] and ALBERT [19]. Since ALBERT involves increasing the model hidden size from 1024 to 2048/4096 and thus substantially increases the amount of computation in terms of FLOPs, we exclude ALBERT from the following results as it is hard to lead to scientific conclusions. To obtain relatively fair comparison with RoBERTa, the experiment in this section is based on full data and reuses the hyper-parameters of RoBERTa, as described in section 3.1.

The results are presented in Tables 2-5, where XLNet generally outperforms BERT and RoBERTa on reading comprehension (RACE), document ranking (ClueWeb09-B), question answering (SQuAD), text classification (IMDB, Yelp, Amazon, etc.), and natural language understanding tasks.

**Key Results:**
- **RACE (Reading Comprehension):** XLNet achieves 85.4% accuracy vs RoBERTa's 83.2%
- **SQuAD2.0 (Question Answering):** XLNet achieves 87.9 EM / 90.6 F1 vs RoBERTa's 86.5 EM / 89.4 F1
- **SQuAD1.1:** XLNet achieves 89.7 EM / 95.1 F1 vs RoBERTa's 88.9 EM / 94.6 F1
- **ClueWeb09-B (Document Ranking):** XLNet achieves 31.10 NDCG@20 / 20.28 ERR@20

## 3.4 Ablation Study

The ablation study examines the importance of different design choices in XLNet (detailed results in paper tables). Key findings include:
- Permutation language modeling objective is crucial for performance
- Two-stream attention mechanism significantly improves results
- Incorporating Transformer-XL ideas (segment recurrence, relative encodings) provides consistent gains
- Next sentence prediction objective does not consistently improve performance

---

### النسخة العربية

## 3.1 التدريب المسبق والتنفيذ

متبعين BERT [10]، نستخدم BooksCorpus [40] و Wikipedia الإنجليزية كجزء من بيانات التدريب المسبق لدينا، والتي تحتوي على 13 جيجابايت من النص العادي مجتمعة. بالإضافة إلى ذلك، نضمن Giga5 (16 جيجابايت نص) [26]، و ClueWeb 2012-B (الممتد من [5])، و Common Crawl [6] للتدريب المسبق. نستخدم إرشادات لتصفية المقالات القصيرة أو منخفضة الجودة بقوة لـ ClueWeb 2012-B و Common Crawl، مما ينتج عنه 19 جيجابايت و 110 جيجابايت نص على التوالي. بعد الترميز باستخدام SentencePiece [17]، نحصل على 2.78 مليار، 1.09 مليار، 4.75 مليار، 4.30 مليار، و 19.97 مليار قطعة كلمة فرعية لـ Wikipedia و BooksCorpus و Giga5 و ClueWeb و Common Crawl على التوالي، أي 32.89 مليار في المجموع.

أكبر نموذج لدينا XLNet-Large له نفس معاملات المعمارية الفائقة لـ BERT-Large، مما ينتج عنه حجم نموذج مماثل. أثناء التدريب المسبق، نستخدم دائماً طول تسلسل كامل يبلغ 512. أولاً، لتوفير مقارنة عادلة مع BERT (القسم 3.2)، قمنا أيضاً بتدريب XLNet-Large-wikibooks على BooksCorpus و Wikipedia فقط، حيث نعيد استخدام جميع معاملات التدريب المسبق الفائقة كما في BERT الأصلي. ثم، نقوم بتوسيع نطاق تدريب XLNet-Large باستخدام جميع مجموعات البيانات الموصوفة أعلاه. على وجه التحديد، نتدرب على 512 شريحة TPU v3 لـ 500 ألف خطوة مع محسن انحدار وزن Adam، وانحدار معدل التعلم الخطي، وحجم دفعة 8192، والتي تستغرق حوالي 5.5 أيام. لوحظ أن النموذج لا يزال يعاني من نقص التجهيز للبيانات في نهاية التدريب. أخيراً، نقوم بإجراء دراسة الاستئصال (القسم 3.4) بناءً على XLNet-Base-wikibooks.

نظراً لأننا قدمنا آلية التكرار، نستخدم خط أنابيب إدخال بيانات ثنائي الاتجاه حيث يأخذ كل من الاتجاهين الأمامي والخلفي نصف حجم الدفعة. لتدريب XLNet-Large، نضبط ثابت التنبؤ الجزئي K على 6 (انظر القسم 2.3). يتبع إجراء الضبط الدقيق لدينا BERT [10] ما لم يُحدد خلاف ذلك. نستخدم فكرة التنبؤ القائم على النطاق، حيث نأخذ أولاً عينة من طول L ∈ [1, · · · , 5]، ثم نختار بشكل عشوائي نطاقاً متتالياً من رموز L كأهداف تنبؤ ضمن سياق من رموز (KL).

نستخدم مجموعة متنوعة من مجموعات بيانات فهم اللغة الطبيعية لتقييم أداء طريقتنا. يمكن العثور على أوصاف تفصيلية للإعدادات لجميع مجموعات البيانات في الملحق A.3.

## 3.2 مقارنة عادلة مع BERT

هنا، نقارن أولاً أداء BERT و XLNet في إعداد عادل لفصل تأثيرات استخدام المزيد من البيانات والتحسين من BERT إلى XLNet. في الجدول 1، نقارن (1) أفضل أداء لثلاثة متغيرات مختلفة من BERT و (2) XLNet المدرب بنفس البيانات والمعاملات الفائقة. كما نرى، عند التدريب على نفس البيانات بوصفة تدريب متطابقة تقريباً، يتفوق XLNet على BERT بهامش كبير في جميع مجموعات البيانات المدروسة.

**الجدول 1: مقارنة عادلة مع BERT.** يتم تدريب جميع النماذج باستخدام نفس البيانات والمعاملات الفائقة كما في BERT. نستخدم أفضل 3 متغيرات BERT للمقارنة؛ أي BERT الأصلي، و BERT مع إخفاء الكلمة الكاملة، و BERT بدون التنبؤ بالجملة التالية.

| النموذج | SQuAD1.1 | SQuAD2.0 | RACE | MNLI | QNLI | QQP | RTE | SST-2 | MRPC | CoLA | STS-B |
|-------|----------|----------|------|------|------|-----|-----|-------|------|------|-------|
| BERT-Large (أفضل من 3) | 86.7/92.8 | 82.8/85.5 | 75.1 | 87.3 | 93.0 | 91.4 | 74.0 | 94.0 | 88.7 | 63.7 | 90.2 |
| XLNet-Large-wikibooks | 88.2/94.0 | 85.1/87.8 | 77.4 | 88.4 | 93.9 | 91.8 | 81.2 | 94.4 | 90.0 | 65.2 | 91.1 |

## 3.3 مقارنة مع RoBERTa: توسيع النطاق

بعد النشر الأولي لمخطوطتنا، تم إصدار عدد قليل من النماذج المدربة مسبقاً الأخرى مثل RoBERTa [21] و ALBERT [19]. نظراً لأن ALBERT يتضمن زيادة حجم النموذج المخفي من 1024 إلى 2048/4096 وبالتالي يزيد بشكل كبير من كمية الحساب من حيث FLOPs، نستبعد ALBERT من النتائج التالية حيث يصعب الوصول إلى استنتاجات علمية. للحصول على مقارنة عادلة نسبياً مع RoBERTa، تستند التجربة في هذا القسم إلى البيانات الكاملة وتعيد استخدام المعاملات الفائقة لـ RoBERTa، كما هو موضح في القسم 3.1.

يتم عرض النتائج في الجداول 2-5، حيث يتفوق XLNet بشكل عام على BERT و RoBERTa في الفهم القرائي (RACE)، وترتيب المستندات (ClueWeb09-B)، والإجابة على الأسئلة (SQuAD)، وتصنيف النصوص (IMDB، Yelp، Amazon، إلخ)، ومهام فهم اللغة الطبيعية.

**النتائج الرئيسية:**
- **RACE (الفهم القرائي):** يحقق XLNet دقة 85.4٪ مقابل 83.2٪ لـ RoBERTa
- **SQuAD2.0 (الإجابة على الأسئلة):** يحقق XLNet 87.9 EM / 90.6 F1 مقابل 86.5 EM / 89.4 F1 لـ RoBERTa
- **SQuAD1.1:** يحقق XLNet 89.7 EM / 95.1 F1 مقابل 88.9 EM / 94.6 F1 لـ RoBERTa
- **ClueWeb09-B (ترتيب المستندات):** يحقق XLNet 31.10 NDCG@20 / 20.28 ERR@20

## 3.4 دراسة الاستئصال

تفحص دراسة الاستئصال أهمية خيارات التصميم المختلفة في XLNet (نتائج مفصلة في جداول الورقة). النتائج الرئيسية تشمل:
- هدف النمذجة اللغوية بالتبديل حاسم للأداء
- آلية الانتباه ثنائي التدفق تحسن النتائج بشكل كبير
- دمج أفكار Transformer-XL (تكرار القطاعات، الترميزات النسبية) يوفر مكاسب متسقة
- هدف التنبؤ بالجملة التالية لا يحسن الأداء بشكل متسق

---

### Translation Notes

- **Figures referenced:** None explicitly, references to Tables 1-5
- **Key terms introduced:** Ablation study, span-based prediction, subword pieces, TPU, Adam weight decay optimizer, underfitting
- **Equations:** None in experiments section
- **Citations:** Multiple references to datasets and comparison models
- **Special handling:** Table data preserved with structure, benchmark names kept in English

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.84
- Glossary consistency: 0.83
- **Overall section score:** 0.85
