# Section 4: Evaluation
## القسم 4: التقييم

**Section:** evaluation
**Translation Quality:** 0.88
**Glossary Terms Used:** question answering, textual entailment, semantic role labeling, coreference resolution, named entity extraction, sentiment analysis, accuracy, F1 score, baseline, state-of-the-art, BiDAF, biLSTM, attention mechanism, GRU, CNN, CRF, ensemble, benchmark

---

### English Version

Table 1 shows the performance of ELMo across a diverse set of six benchmark NLP tasks. In every task considered, simply adding ELMo establishes a new state-of-the-art result, with relative error reductions ranging from 6 - 20% over strong base models. This is a very general result across a diverse set model architectures and language understanding tasks. In the remainder of this section we provide high-level sketches of the individual task results; see the supplemental material for full experimental details.

**Question answering** The Stanford Question Answering Dataset (SQuAD) (Rajpurkar et al., 2016) contains 100K+ crowd sourced question-answer pairs where the answer is a span in a given Wikipedia paragraph. Our baseline model (Clark and Gardner, 2017) is an improved version of the Bidirectional Attention Flow model in Seo et al. (BiDAF; 2017). It adds a self-attention layer after the bidirectional attention component, simplifies some of the pooling operations and substitutes the LSTMs for gated recurrent units (GRUs; Cho et al., 2014). After adding ELMo to the baseline model, test set F1 improved by 4.7% from 81.1% to 85.8%, a 24.9% relative error reduction over the baseline, and improving the overall single model state-of-the-art by 1.4%. A 11 member ensemble pushes F1 to 87.4, the overall state-of-the-art at time of submission to the leaderboard. The increase of 4.7% with ELMo is also significantly larger than the 1.8% improvement from adding CoVe to a baseline model (McCann et al., 2017).

**Table 1:** Test set comparison of ELMo enhanced neural models with state-of-the-art single model baselines across six benchmark NLP tasks.

| TASK | PREVIOUS SOTA | OUR BASELINE | ELMO + BASELINE | INCREASE (ABSOLUTE / RELATIVE) |
|------|---------------|--------------|-----------------|--------------------------------|
| SQuAD | Liu et al. (2017) 84.4 | 81.1 | 85.8 | 4.7 / 24.9% |
| SNLI | Chen et al. (2017) 88.6 | 88.0 ± 0.17 | 88.7 ± 0.17 | 0.7 / 5.8% |
| SRL | He et al. (2017) 81.7 | 81.4 | 84.6 | 3.2 / 17.2% |
| Coref | Lee et al. (2017) 67.2 | 67.2 | 70.4 | 3.2 / 9.8% |
| NER | Peters et al. (2017) 91.93 ± 0.19 | 90.15 | 92.22 ± 0.10 | 2.06 / 21% |
| SST-5 | McCann et al. (2017) 53.7 | 51.4 | 54.7 ± 0.5 | 3.3 / 6.8% |

The performance metric varies across tasks - accuracy for SNLI and SST-5; F1 for SQuAD, SRL and NER; average F1 for Coref. Due to the small test sizes for NER and SST-5, we report the mean and standard deviation across five runs with different random seeds.

**Textual entailment** Textual entailment is the task of determining whether a "hypothesis" is true, given a "premise". The Stanford Natural Language Inference (SNLI) corpus (Bowman et al., 2015) provides approximately 550K hypothesis/premise pairs. Our baseline, the ESIM sequence model from Chen et al. (2017), uses a biLSTM to encode the premise and hypothesis, followed by a matrix attention layer, a local inference layer, another biLSTM inference composition layer, and finally a pooling operation before the output layer. Overall, adding ELMo to the ESIM model improves accuracy by an average of 0.7% across five random seeds. A five member ensemble pushes the overall accuracy to 89.3%, exceeding the previous ensemble best of 88.9% (Gong et al., 2018).

**Semantic role labeling** A semantic role labeling (SRL) system models the predicate-argument structure of a sentence, and is often described as answering "Who did what to whom". He et al. (2017) modeled SRL as a BIO tagging problem and used an 8-layer deep biLSTM with forward and backward directions interleaved, following Zhou and Xu (2015). As shown in Table 1, when adding ELMo to a re-implementation of He et al. (2017) the single model test set F1 jumped 3.2% from 81.4% to 84.6% - a new state-of-the-art on the OntoNotes benchmark (Pradhan et al., 2013), even improving over the previous best ensemble result by 1.2%.

**Coreference resolution** Coreference resolution is the task of clustering mentions in text that refer to the same underlying real world entities. Our baseline model is the end-to-end span-based neural model of Lee et al. (2017). It uses a biLSTM and attention mechanism to first compute span representations and then applies a softmax mention ranking model to find coreference chains. In our experiments with the OntoNotes coreference annotations from the CoNLL 2012 shared task (Pradhan et al., 2012), adding ELMo improved the average F1 by 3.2% from 67.2 to 70.4, establishing a new state of the art, again improving over the previous best ensemble result by 1.6% F1.

**Named entity extraction** The CoNLL 2003 NER task (Sang and Meulder, 2003) consists of newswire from the Reuters RCV1 corpus tagged with four different entity types (PER, LOC, ORG, MISC). Following recent state-of-the-art systems (Lample et al., 2016; Peters et al., 2017), the baseline model uses pre-trained word embeddings, a character-based CNN representation, two biLSTM layers and a conditional random field (CRF) loss (Lafferty et al., 2001), similar to Collobert et al. (2011). As shown in Table 1, our ELMo enhanced biLSTM-CRF achieves 92.22% F1 averaged over five runs. The key difference between our system and the previous state of the art from Peters et al. (2017) is that we allowed the task model to learn a weighted average of all biLM layers, whereas Peters et al. (2017) only use the top biLM layer. As shown in Sec. 5.1, using all layers instead of just the last layer improves performance across multiple tasks.

**Sentiment analysis** The fine-grained sentiment classification task in the Stanford Sentiment Treebank (SST-5; Socher et al., 2013) involves selecting one of five labels (from very negative to very positive) to describe a sentence from a movie review. The sentences contain diverse linguistic phenomena such as idioms and complex syntactic constructions such as negations that are difficult for models to learn. Our baseline model is the biattentive classification network (BCN) from McCann et al. (2017), which also held the prior state-of-the-art result when augmented with CoVe embeddings. Replacing CoVe with ELMo in the BCN model results in a 1.0% absolute accuracy improvement over the state of the art.

**Table 2:** Development set performance for SQuAD, SNLI and SRL comparing using all layers of the biLM (with different choices of regularization strength λ) to just the top layer.

| Task | Baseline | Last Only | All layers λ=1 | All layers λ=0.001 |
|------|----------|-----------|----------------|---------------------|
| SQuAD | 80.8 | 84.7 | 85.0 | 85.2 |
| SNLI | 88.1 | 89.1 | 89.3 | 89.5 |
| SRL | 81.6 | 84.1 | 84.6 | 84.8 |

**Table 3:** Development set performance for SQuAD, SNLI and SRL when including ELMo at different locations in the supervised model.

| Task | Input Only | Input & Output | Output Only |
|------|------------|----------------|-------------|
| SQuAD | 85.1 | 85.6 | 84.8 |
| SNLI | 88.9 | 89.5 | 88.7 |
| SRL | 84.7 | 84.3 | 80.9 |

---

### النسخة العربية

يُظهر الجدول 1 أداء ELMo عبر مجموعة متنوعة من ست مهام معيارية في معالجة اللغة الطبيعية. في كل مهمة معتبرة، مجرد إضافة ELMo يؤسس نتيجة جديدة لأحدث ما توصل إليه العلم، مع تخفيضات في الخطأ النسبي تتراوح من 6 - 20% على نماذج أساسية قوية. هذه نتيجة عامة جداً عبر مجموعة متنوعة من معماريات النماذج ومهام فهم اللغة. في بقية هذا القسم، نقدم رسومات عالية المستوى لنتائج المهام الفردية؛ راجع المواد التكميلية للحصول على التفاصيل التجريبية الكاملة.

**الإجابة على الأسئلة** مجموعة بيانات ستانفورد للإجابة على الأسئلة (SQuAD) (Rajpurkar et al., 2016) تحتوي على أكثر من 100 ألف زوج سؤال-إجابة من مصادر جماعية حيث تكون الإجابة مقطعاً في فقرة ويكيبيديا معينة. نموذجنا الأساسي (Clark and Gardner, 2017) هو نسخة محسنة من نموذج تدفق الانتباه ثنائي الاتجاه في Seo et al. (BiDAF; 2017). يضيف طبقة انتباه ذاتي بعد مكون الانتباه ثنائي الاتجاه، ويبسط بعض عمليات التجميع ويستبدل LSTMs بوحدات متكررة ببوابات (GRUs; Cho et al., 2014). بعد إضافة ELMo إلى النموذج الأساسي، تحسنت F1 لمجموعة الاختبار بنسبة 4.7% من 81.1% إلى 85.8%، وهو تخفيض خطأ نسبي بنسبة 24.9% على الأساس، وتحسين أحدث ما توصل إليه العلم للنموذج الفردي الإجمالي بنسبة 1.4%. مجموعة من 11 عضواً تدفع F1 إلى 87.4، وهو أحدث ما توصل إليه العلم الإجمالي في وقت التقديم إلى لوحة الصدارة. الزيادة بنسبة 4.7% مع ELMo أيضاً أكبر بكثير من التحسن بنسبة 1.8% من إضافة CoVe إلى نموذج أساسي (McCann et al., 2017).

**الجدول 1:** مقارنة مجموعة الاختبار للنماذج العصبية المحسنة بـ ELMo مع خطوط الأساس للنماذج الفردية الحديثة عبر ست مهام معيارية في معالجة اللغة الطبيعية.

| المهمة | أحدث ما توصل إليه العلم السابق | خط الأساس لدينا | ELMo + خط الأساس | الزيادة (مطلقة / نسبية) |
|--------|--------------------------------|------------------|------------------|------------------------|
| SQuAD | Liu et al. (2017) 84.4 | 81.1 | 85.8 | 4.7 / 24.9% |
| SNLI | Chen et al. (2017) 88.6 | 88.0 ± 0.17 | 88.7 ± 0.17 | 0.7 / 5.8% |
| SRL | He et al. (2017) 81.7 | 81.4 | 84.6 | 3.2 / 17.2% |
| Coref | Lee et al. (2017) 67.2 | 67.2 | 70.4 | 3.2 / 9.8% |
| NER | Peters et al. (2017) 91.93 ± 0.19 | 90.15 | 92.22 ± 0.10 | 2.06 / 21% |
| SST-5 | McCann et al. (2017) 53.7 | 51.4 | 54.7 ± 0.5 | 3.3 / 6.8% |

يختلف مقياس الأداء عبر المهام - الدقة لـ SNLI وSST-5؛ F1 لـ SQuAD وSRL وNER؛ متوسط F1 لـ Coref. نظراً لصغر أحجام الاختبار لـ NER وSST-5، نُبلغ عن المتوسط والانحراف المعياري عبر خمس تشغيلات ببذور عشوائية مختلفة.

**الاستلزام النصي** الاستلزام النصي هو مهمة تحديد ما إذا كانت "فرضية" صحيحة، بالنظر إلى "مقدمة". مدونة ستانفورد للاستدلال اللغوي الطبيعي (SNLI) (Bowman et al., 2015) توفر حوالي 550 ألف زوج فرضية/مقدمة. خط أساسنا، نموذج التسلسل ESIM من Chen et al. (2017)، يستخدم biLSTM لترميز المقدمة والفرضية، متبوعاً بطبقة انتباه مصفوفية، وطبقة استدلال محلية، وطبقة تركيب استدلال biLSTM أخرى، وأخيراً عملية تجميع قبل طبقة الإخراج. بشكل عام، إضافة ELMo إلى نموذج ESIM يحسن الدقة بمتوسط 0.7% عبر خمس بذور عشوائية. مجموعة من خمسة أعضاء تدفع الدقة الإجمالية إلى 89.3%، متجاوزة أفضل نتيجة سابقة للمجموعة وهي 88.9% (Gong et al., 2018).

**وسم الأدوار الدلالية** نظام وسم الأدوار الدلالية (SRL) ينمذج بنية الحمل-المحمول للجملة، وغالباً ما يُوصف بأنه يجيب على "من فعل ماذا لمن". He et al. (2017) نمذجوا SRL كمشكلة وسم BIO واستخدموا biLSTM عميق من 8 طبقات مع اتجاهات أمامية وخلفية متشابكة، متبعين Zhou and Xu (2015). كما هو موضح في الجدول 1، عند إضافة ELMo إلى إعادة تنفيذ He et al. (2017)، قفزت F1 لمجموعة الاختبار للنموذج الفردي بنسبة 3.2% من 81.4% إلى 84.6% - وهو أحدث ما توصل إليه العلم الجديد على معيار OntoNotes (Pradhan et al., 2013)، حتى التحسين على أفضل نتيجة سابقة للمجموعة بنسبة 1.2%.

**حل الإحالة المرجعية** حل الإحالة المرجعية هو مهمة تجميع الإشارات في النص التي تشير إلى نفس الكيانات الحقيقية الأساسية. نموذجنا الأساسي هو النموذج العصبي القائم على النطاق من طرف إلى طرف لـ Lee et al. (2017). يستخدم biLSTM وآلية انتباه لحساب تمثيلات النطاق أولاً ثم يطبق نموذج ترتيب إشارة softmax لإيجاد سلاسل الإحالة المرجعية. في تجاربنا مع تعليقات الإحالة المرجعية OntoNotes من مهمة CoNLL 2012 المشتركة (Pradhan et al., 2012)، أدت إضافة ELMo إلى تحسين متوسط F1 بنسبة 3.2% من 67.2 إلى 70.4، مؤسسة أحدث ما توصل إليه العلم الجديد، مرة أخرى التحسين على أفضل نتيجة سابقة للمجموعة بنسبة 1.6% F1.

**استخراج الكيانات المسماة** مهمة CoNLL 2003 لاستخراج الكيانات المسماة (NER) (Sang and Meulder, 2003) تتكون من أخبار من مدونة Reuters RCV1 موسومة بأربعة أنواع مختلفة من الكيانات (PER، LOC، ORG، MISC). متبعين أحدث الأنظمة (Lample et al., 2016; Peters et al., 2017)، يستخدم النموذج الأساسي تضمينات كلمات مدربة مسبقاً، وتمثيل CNN قائم على الأحرف، وطبقتي biLSTM وخسارة حقل عشوائي شرطي (CRF) (Lafferty et al., 2001)، مشابه لـ Collobert et al. (2011). كما هو موضح في الجدول 1، يحقق biLSTM-CRF المحسن بـ ELMo 92.22% F1 بمتوسط خمس تشغيلات. الفرق الرئيسي بين نظامنا وأحدث ما توصل إليه العلم السابق من Peters et al. (2017) هو أننا سمحنا لنموذج المهمة بتعلم متوسط مرجح لجميع طبقات biLM، بينما Peters et al. (2017) يستخدمون فقط طبقة biLM العليا. كما هو موضح في القسم 5.1، استخدام جميع الطبقات بدلاً من الطبقة الأخيرة فقط يحسن الأداء عبر مهام متعددة.

**تحليل المشاعر** مهمة تصنيف المشاعر الدقيقة في بنك أشجار المشاعر ستانفورد (SST-5; Socher et al., 2013) تتضمن اختيار واحدة من خمس تسميات (من سلبي جداً إلى إيجابي جداً) لوصف جملة من مراجعة فيلم. تحتوي الجمل على ظواهر لغوية متنوعة مثل التعابير الاصطلاحية والبنى التركيبية المعقدة مثل النفي التي يصعب على النماذج تعلمها. نموذجنا الأساسي هو شبكة التصنيف ثنائية الانتباه (BCN) من McCann et al. (2017)، التي كانت أيضاً تحمل نتيجة أحدث ما توصل إليه العلم السابقة عند تعزيزها بتضمينات CoVe. استبدال CoVe بـ ELMo في نموذج BCN ينتج عنه تحسن دقة مطلق بنسبة 1.0% على أحدث ما توصل إليه العلم.

**الجدول 2:** أداء مجموعة التطوير لـ SQuAD وSNLI وSRL مقارنة استخدام جميع طبقات biLM (مع خيارات مختلفة لقوة التنظيم λ) مقابل الطبقة العليا فقط.

| المهمة | خط الأساس | الأخيرة فقط | جميع الطبقات λ=1 | جميع الطبقات λ=0.001 |
|--------|-----------|-------------|------------------|-----------------------|
| SQuAD | 80.8 | 84.7 | 85.0 | 85.2 |
| SNLI | 88.1 | 89.1 | 89.3 | 89.5 |
| SRL | 81.6 | 84.1 | 84.6 | 84.8 |

**الجدول 3:** أداء مجموعة التطوير لـ SQuAD وSNLI وSRL عند تضمين ELMo في مواقع مختلفة في النموذج المُشرف.

| المهمة | الإدخال فقط | الإدخال والإخراج | الإخراج فقط |
|--------|-------------|------------------|-------------|
| SQuAD | 85.1 | 85.6 | 84.8 |
| SNLI | 88.9 | 89.5 | 88.7 |
| SRL | 84.7 | 84.3 | 80.9 |

---

### Translation Notes

- **Figures referenced:** Table 1, Table 2, Table 3
- **Key terms introduced:** SQuAD, SNLI, SRL (semantic role labeling), Coref (coreference resolution), NER (named entity recognition), SST-5 (Stanford Sentiment Treebank), BiDAF, ESIM, BIO tagging, OntoNotes, CoNLL, BCN
- **Equations:** None
- **Citations:** Rajpurkar et al. 2016, Clark and Gardner 2017, Seo et al. 2017, Cho et al. 2014, Liu et al. 2017, McCann et al. 2017, Chen et al. 2017, Bowman et al. 2015, Gong et al. 2018, He et al. 2017, Zhou and Xu 2015, Pradhan et al. 2013, Pradhan et al. 2012, Lee et al. 2017, Sang and Meulder 2003, Lample et al. 2016, Peters et al. 2017, Lafferty et al. 2001, Collobert et al. 2011, Socher et al. 2013
- **Special handling:**
  - Maintained all dataset names and abbreviations
  - Preserved table structures with Arabic headers
  - Kept percentage improvements and statistical values exact
  - Used consistent terminology for metrics (F1, accuracy)

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88

### Back-Translation Validation (First Paragraph)

Table 1 shows the performance of ELMo across a diverse set of six benchmark NLP tasks. In every task considered, simply adding ELMo establishes a new state-of-the-art result, with relative error reductions ranging from 6 - 20% over strong baseline models. This is a very general result across a diverse set of model architectures and language understanding tasks. In the remainder of this section we provide high-level sketches of the individual task results; see the supplemental material for full experimental details.

**Validation:** ✓ Excellent semantic match with original
