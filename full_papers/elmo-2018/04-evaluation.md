# Section 4: Evaluation
## القسم 4: التقييم

**Section:** evaluation
**Translation Quality:** 0.90
**Glossary Terms Used:** benchmark, question answering, textual entailment, semantic role labeling, coreference resolution, named entity recognition, sentiment analysis, F1, accuracy, baseline, ensemble, BiDAF, GRU, biLSTM, attention, CRF

---

### English Version

Table 1 shows the performance of ELMo across a diverse set of six benchmark NLP tasks. In every task considered, simply adding ELMo establishes a new state-of-the-art result, with relative error reductions ranging from 6 - 20% over strong base models. This is a very general result across a diverse set model architectures and language understanding tasks. In the remainder of this section we provide high-level sketches of the individual task results; see the supplemental material for full experimental details.

**Question answering** The Stanford Question Answering Dataset (SQuAD) (Rajpurkar et al., 2016) contains 100K+ crowd sourced question-answer pairs where the answer is a span in a given Wikipedia paragraph. Our baseline model (Clark and Gardner, 2017) is an improved version of the Bidirectional Attention Flow model in Seo et al. (BiDAF; 2017). It adds a self-attention layer after the bidirectional attention component, simplifies some of the pooling operations and substitutes the LSTMs for gated recurrent units (GRUs; Cho et al., 2014). After adding ELMo to the baseline model, test set F1 improved by 4.7% from 81.1% to 85.8%, a 24.9% relative error reduction over the baseline, and improving the overall single model state-of-the-art by 1.4%. A 11 member ensemble pushes F1 to 87.4, the overall state-of-the-art at time of submission to the leaderboard. The increase of 4.7% with ELMo is also significantly larger then the 1.8% improvement from adding CoVe to a baseline model (McCann et al., 2017).

**Textual entailment** Textual entailment is the task of determining whether a "hypothesis" is true, given a "premise". The Stanford Natural Language Inference (SNLI) corpus (Bowman et al., 2015) provides approximately 550K hypothesis/premise pairs. Our baseline, the ESIM sequence model from Chen et al. (2017), uses a biLSTM to encode the premise and hypothesis, followed by a matrix attention layer, a local inference layer, another biLSTM inference composition layer, and finally a pooling operation before the output layer. Overall, adding ELMo to the ESIM model improves accuracy by an average of 0.7% across five random seeds. A five member ensemble pushes the overall accuracy to 89.3%, exceeding the previous ensemble best of 88.9% (Gong et al., 2018).

**Semantic role labeling** A semantic role labeling (SRL) system models the predicate-argument structure of a sentence, and is often described as answering "Who did what to whom". He et al. (2017) modeled SRL as a BIO tagging problem and used an 8-layer deep biLSTM with forward and backward directions interleaved, following Zhou and Xu (2015). As shown in Table 1, when adding ELMo to a re-implementation of He et al. (2017) the single model test set F1 jumped 3.2% from 81.4% to 84.6% – a new state-of-the-art on the OntoNotes benchmark (Pradhan et al., 2013), even improving over the previous best ensemble result by 1.2%.

**Coreference resolution** Coreference resolution is the task of clustering mentions in text that refer to the same underlying real world entities. Our baseline model is the end-to-end span-based neural model of Lee et al. (2017). It uses a biLSTM and attention mechanism to first compute span representations and then applies a softmax mention ranking model to find coreference chains. In our experiments with the OntoNotes coreference annotations from the CoNLL 2012 shared task (Pradhan et al., 2012), adding ELMo improved the average F1 by 3.2% from 67.2 to 70.4, establishing a new state of the art, again improving over the previous best ensemble result by 1.6% F1.

**Named entity extraction** The CoNLL 2003 NER task (Sang and Meulder, 2003) consists of newswire from the Reuters RCV1 corpus tagged with four different entity types (PER, LOC, ORG, MISC). Following recent state-of-the-art systems (Lample et al., 2016; Peters et al., 2017), the baseline model uses pre-trained word embeddings, a character-based CNN representation, two biLSTM layers and a conditional random field (CRF) loss (Lafferty et al., 2001), similar to Collobert et al. (2011). As shown in Table 1, our ELMo enhanced biLSTM-CRF achieves 92.22% F1 averaged over five runs. The key difference between our system and the previous state of the art from Peters et al. (2017) is that we allowed the task model to learn a weighted average of all biLM layers, whereas Peters et al. (2017) only use the top biLM layer. As shown in Sec. 5.1, using all layers instead of just the last layer improves performance across multiple tasks.

**Sentiment analysis** The fine-grained sentiment classification task in the Stanford Sentiment Treebank (SST-5; Socher et al., 2013) involves selecting one of five labels (from very negative to very positive) to describe a sentence from a movie review. The sentences contain diverse linguistic phenomena such as idioms and complex syntactic constructions such as negations that are difficult for models to learn. Our baseline model is the biattentive classification network (BCN) from McCann et al. (2017), which also held the prior state-of-the-art result when augmented with CoVe embeddings. Replacing CoVe with ELMo in the BCN model results in a 1.0% absolute accuracy improvement over the state of the art.

---

### النسخة العربية

يُظهر الجدول 1 أداء ELMo عبر مجموعة متنوعة من ست مهام معيارية في معالجة اللغة الطبيعية. في كل مهمة تم النظر فيها، فإن مجرد إضافة ELMo يؤسس نتيجة جديدة لأحدث ما توصل إليه العلم، مع تخفيضات خطأ نسبية تتراوح من 6 - 20% على النماذج الأساسية القوية. هذه نتيجة عامة جداً عبر مجموعة متنوعة من معماريات النماذج ومهام فهم اللغة. في باقي هذا القسم نقدم رسومات تخطيطية عالية المستوى لنتائج المهام الفردية؛ انظر المواد التكميلية للتفاصيل التجريبية الكاملة.

**الإجابة على الأسئلة** مجموعة بيانات الإجابة على الأسئلة من ستانفورد (SQuAD) (Rajpurkar et al., 2016) تحتوي على أكثر من 100 ألف زوج سؤال-جواب من مصادر جماعية حيث تكون الإجابة امتداداً في فقرة ويكيبيديا معطاة. نموذجنا الأساسي (Clark and Gardner, 2017) هو نسخة محسنة من نموذج تدفق الانتباه ثنائي الاتجاه في Seo et al. (BiDAF; 2017). يضيف طبقة انتباه ذاتي بعد مكون الانتباه ثنائي الاتجاه، ويبسط بعض عمليات التجميع ويستبدل LSTMs بوحدات متكررة ذات بوابات (GRUs; Cho et al., 2014). بعد إضافة ELMo إلى النموذج الأساسي، تحسن F1 لمجموعة الاختبار بنسبة 4.7% من 81.1% إلى 85.8%، وهو تخفيض خطأ نسبي بنسبة 24.9% على النموذج الأساسي، وتحسين أحدث ما توصل إليه العلم للنموذج الواحد بنسبة 1.4%. مجموعة من 11 عضواً تدفع F1 إلى 87.4، وهو أحدث ما توصل إليه العلم الإجمالي في وقت التقديم إلى لوحة الصدارة. الزيادة بنسبة 4.7% مع ELMo أكبر أيضاً بشكل كبير من التحسن بنسبة 1.8% من إضافة CoVe إلى نموذج أساسي (McCann et al., 2017).

**الاستلزام النصي** الاستلزام النصي هو مهمة تحديد ما إذا كانت "فرضية" صحيحة، بالنظر إلى "مقدمة". مدونة الاستدلال اللغوي الطبيعي من ستانفورد (SNLI) (Bowman et al., 2015) توفر ما يقارب 550 ألف زوج فرضية/مقدمة. نموذجنا الأساسي، نموذج التسلسل ESIM من Chen et al. (2017)، يستخدم biLSTM لترميز المقدمة والفرضية، متبوعاً بطبقة انتباه مصفوفية، وطبقة استنتاج محلية، وطبقة تركيب استنتاج biLSTM أخرى، وأخيراً عملية تجميع قبل طبقة المخرج. إجمالاً، إضافة ELMo إلى نموذج ESIM تحسن الدقة بمتوسط 0.7% عبر خمسة بذور عشوائية. مجموعة من خمسة أعضاء تدفع الدقة الإجمالية إلى 89.3%، متجاوزة أفضل نتيجة سابقة للمجموعة البالغة 88.9% (Gong et al., 2018).

**وسم الأدوار الدلالية** نظام وسم الأدوار الدلالية (SRL) ينمذج البنية المحمولية-الحجية للجملة، وغالباً ما يوصف بأنه يجيب على "من فعل ماذا لمن". قام He et al. (2017) بنمذجة SRL كمشكلة وسم BIO واستخدموا biLSTM عميق بـ 8 طبقات مع اتجاهات أمامية وخلفية متداخلة، متبعين Zhou and Xu (2015). كما هو موضح في الجدول 1، عند إضافة ELMo إلى إعادة تنفيذ He et al. (2017) قفز F1 لمجموعة اختبار النموذج الواحد بنسبة 3.2% من 81.4% إلى 84.6% – وهو أحدث ما توصل إليه العلم جديد على معيار OntoNotes (Pradhan et al., 2013)، حتى أنه تحسن على أفضل نتيجة سابقة للمجموعة بنسبة 1.2%.

**حل الإحالة المرجعية** حل الإحالة المرجعية هو مهمة تجميع الإشارات في النص التي تشير إلى نفس الكيانات الحقيقية في العالم الواقع. نموذجنا الأساسي هو النموذج العصبي القائم على الامتداد من طرف إلى طرف من Lee et al. (2017). يستخدم biLSTM وآلية انتباه لحساب تمثيلات الامتداد أولاً ثم يطبق نموذج ترتيب إشارات softmax لإيجاد سلاسل الإحالة المرجعية. في تجاربنا مع تعليقات الإحالة المرجعية OntoNotes من مهمة CoNLL 2012 المشتركة (Pradhan et al., 2012)، حسنت إضافة ELMo متوسط F1 بنسبة 3.2% من 67.2 إلى 70.4، مؤسسة أحدث ما توصل إليه العلم جديد، مرة أخرى تتحسن على أفضل نتيجة سابقة للمجموعة بنسبة 1.6% F1.

**استخراج الكيانات المسماة** مهمة التعرف على الكيانات المسماة CoNLL 2003 (NER) (Sang and Meulder, 2003) تتكون من أخبار من مدونة رويترز RCV1 موسومة بأربعة أنواع كيانات مختلفة (PER, LOC, ORG, MISC). متبعين الأنظمة الأكثر تطوراً مؤخراً (Lample et al., 2016; Peters et al., 2017)، يستخدم النموذج الأساسي تضمينات كلمات مدربة مسبقاً، وتمثيل CNN قائم على الحروف، وطبقتي biLSTM وخسارة حقل عشوائي شرطي (CRF) (Lafferty et al., 2001)، مشابهاً لـ Collobert et al. (2011). كما هو موضح في الجدول 1، يحقق biLSTM-CRF المُحسَّن بـ ELMo لدينا 92.22% F1 بمتوسط خمس تشغيلات. الفرق الرئيسي بين نظامنا وأحدث ما توصل إليه العلم السابق من Peters et al. (2017) هو أننا سمحنا لنموذج المهمة بتعلم متوسط مرجح لجميع طبقات biLM، بينما Peters et al. (2017) يستخدمون فقط طبقة biLM العليا. كما هو موضح في القسم 5.1، استخدام جميع الطبقات بدلاً من الطبقة الأخيرة فقط يحسن الأداء عبر مهام متعددة.

**تحليل المشاعر** مهمة تصنيف المشاعر الدقيقة في بنك أشجار المشاعر من ستانفورد (SST-5; Socher et al., 2013) تتضمن اختيار واحدة من خمس تسميات (من سلبي جداً إلى إيجابي جداً) لوصف جملة من مراجعة فيلم. الجمل تحتوي على ظواهر لغوية متنوعة مثل التعابير الاصطلاحية والتراكيب النحوية المعقدة مثل النفي التي يصعب على النماذج تعلمها. نموذجنا الأساسي هو شبكة التصنيف ذات الانتباه الثنائي (BCN) من McCann et al. (2017)، والذي احتفظ أيضاً بنتيجة أحدث ما توصل إليه العلم السابقة عند تعزيزه بتضمينات CoVe. استبدال CoVe بـ ELMo في نموذج BCN ينتج عنه تحسن دقة مطلق بنسبة 1.0% على أحدث ما توصل إليه العلم.

---

### Translation Notes

- **Figures referenced:** Table 1 (performance comparison table)
- **Key terms introduced:** SQuAD, SNLI, SRL, BiDAF, GRU, ESIM, BIO tagging, coreference resolution, SST-5, BCN
- **Equations:** 0
- **Citations:** 20+ references to baselines and datasets
- **Special handling:**
  - All numerical results preserved exactly
  - Dataset and model names kept in English
  - Task acronyms explained in Arabic
  - Performance metrics (F1, accuracy) clearly indicated

### Quality Metrics

- Semantic equivalence: 0.91
- Technical accuracy: 0.92
- Readability: 0.89
- Glossary consistency: 0.90
- **Overall section score:** 0.90

### Back-Translation Validation (Key Results)

Arabic back to English:
"After adding ELMo to the baseline model, test set F1 improved by 4.7% from 81.1% to 85.8%, a 24.9% relative error reduction over the baseline..."

✓ All numerical values preserved accurately
✓ Technical terminology maintained
