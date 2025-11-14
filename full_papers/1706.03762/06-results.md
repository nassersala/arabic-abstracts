# Section 6: Results
## القسم 6: النتائج

**Section:** results
**Translation Quality:** 0.87
**Glossary Terms Used:** machine translation, BLEU score, training cost, ensemble, model variations, English constituency parsing

---

### English Version

## 6.1 Machine Translation

On the WMT 2014 English-to-German translation task, the big transformer model (Transformer (big) in Table 2) outperforms the best previously reported models (including ensembles) by more than 2.0 BLEU, establishing a new state-of-the-art BLEU score of 28.4. The configuration of this model is listed in the bottom line of Table 3. Training took 3.5 days on 8 P100 GPUs. Even our base model surpasses all previously published models and ensembles, at a fraction of the training cost of any of the competitive models.

On the WMT 2014 English-to-French translation task, our big model achieves a BLEU score of 41.0, outperforming all of the previously published single models, at less than 1/4 the training cost of the previous state-of-the-art model. The Transformer (big) model trained for English-to-French used dropout rate P_drop = 0.1, instead of 0.3.

For the base models, we used a single model obtained by averaging the last 5 checkpoints, which were written at 10-minute intervals. For the big models, we averaged the last 20 checkpoints. We used beam search with a beam size of 4 and length penalty α = 0.6 [38]. These hyperparameters were chosen after experimentation on the development set. We set the maximum output length during inference to input length + 50, but terminate early when possible [38].

Table 2 summarizes our results and compares our translation quality and training costs to other model architectures from the literature. We estimate the number of floating point operations used to train a model by multiplying the training time, the number of GPUs used, and an estimate of the sustained single-precision floating-point capacity of each GPU.

## 6.2 Model Variations

To evaluate the importance of different components of the Transformer, we varied our base model in different ways, measuring the change in performance on English-to-German translation on the development set, newstest2013. We used beam search as described in the previous section, but no checkpoint averaging. We present these results in Table 3.

In Table 3 rows (A), we vary the number of attention heads and the attention key and value dimensions, keeping the amount of computation constant, as described in Section 3.2.2. While single-head attention is 0.9 BLEU worse than the best setting, quality also drops off with too many heads.

In Table 3 rows (B), we observe that reducing the attention key size d_k hurts model quality. This suggests that determining compatibility is not easy and that a more sophisticated compatibility function than dot product may be beneficial. We further observe in rows (C) and (D) that, as expected, bigger models are better, and dropout is very helpful in avoiding over-fitting. In row (E) we replace our sinusoidal positional encoding with learned positional embeddings [9], and observe nearly identical results to the base model.

## 6.3 English Constituency Parsing

To evaluate if the Transformer can generalize to other tasks we performed experiments on English constituency parsing. This task presents specific challenges: the output is subject to strong structural constraints and is significantly longer than the input. Furthermore, RNN sequence-to-sequence models have not been able to attain state-of-the-art results in small-data regimes [37].

We trained a 4-layer transformer with d_model = 1024 on the Wall Street Journal (WSJ) portion of the Penn Treebank [25], about 40K training sentences. We also trained it in a semi-supervised setting, using the larger high-confidence and BerkleyParser corpora from with approximately 17M sentences [37]. We used a vocabulary of 16K tokens for the WSJ only setting and a vocabulary of 32K tokens for the semi-supervised setting.

We performed only a small number of experiments to select the dropout, both attention and residual (section 5.4), learning rates and beam size on the Section 22 development set, all other parameters remained unchanged from the English-to-German base translation model. During inference, we increased the maximum output length to input length + 300. We used a beam size of 21 and α = 0.3 for both WSJ only and the semi-supervised setting.

Our results in Table 4 show that despite the lack of task-specific tuning our model performs surprisingly well, yielding better results than all previously reported models with the exception of the Recurrent Neural Network Grammar [8].

In contrast to RNN sequence-to-sequence models [37], the Transformer outperforms the Berkeley-Parser [29] even when training only on the WSJ training set of 40K sentences.

---

### النسخة العربية

## 6.1 الترجمة الآلية

في مهمة ترجمة WMT 2014 من الإنجليزية إلى الألمانية، يتفوق نموذج المحوّل الكبير (Transformer (big) في الجدول 2) على أفضل النماذج المُبلّغ عنها سابقاً (بما في ذلك التجميعات) بأكثر من 2.0 BLEU، مُؤسّساً نقطة مرجعية جديدة متطورة لنتيجة BLEU بقيمة 28.4. يُدرج تكوين هذا النموذج في السطر السفلي من الجدول 3. استغرق التدريب 3.5 يوم على 8 وحدات معالجة رسومية P100. حتى نموذجنا الأساسي يتجاوز جميع النماذج والتجميعات المنشورة سابقاً، بجزء صغير من تكلفة التدريب لأي من النماذج التنافسية.

في مهمة ترجمة WMT 2014 من الإنجليزية إلى الفرنسية، يحقق نموذجنا الكبير نتيجة BLEU بقيمة 41.0، متفوقاً على جميع النماذج الفردية المنشورة سابقاً، بأقل من 1/4 تكلفة التدريب للنموذج المتطور السابق. استخدم نموذج Transformer (big) المُدرّب للإنجليزية-الفرنسية معدل إسقاط P_drop = 0.1، بدلاً من 0.3.

بالنسبة للنماذج الأساسية، استخدمنا نموذجاً واحداً تم الحصول عليه من خلال حساب متوسط آخر 5 نقاط تفتيش، التي كُتبت على فترات 10 دقائق. بالنسبة للنماذج الكبيرة، حسبنا متوسط آخر 20 نقطة تفتيش. استخدمنا البحث الشعاعي (beam search) بحجم شعاع 4 وعقوبة طول α = 0.6 [38]. تم اختيار هذه المعاملات الفائقة بعد التجريب على مجموعة التطوير. حددنا الحد الأقصى لطول الإخراج أثناء الاستدلال إلى طول الإدخال + 50، لكننا نُنهي مبكراً عندما يكون ذلك ممكناً [38].

يلخّص الجدول 2 نتائجنا ويقارن جودة ترجمتنا وتكاليف التدريب بمعماريات نماذج أخرى من الأدبيات. نقدّر عدد عمليات الفاصلة العائمة المستخدمة لتدريب نموذج من خلال ضرب وقت التدريب، وعدد وحدات معالجة الرسومات المستخدمة، وتقدير السعة المستدامة للفاصلة العائمة أحادية الدقة لكل وحدة معالجة رسومات.

## 6.2 تباينات النموذج

لتقييم أهمية المكونات المختلفة للمحوّل، غيّرنا نموذجنا الأساسي بطرق مختلفة، لقياس التغيير في الأداء على ترجمة الإنجليزية إلى الألمانية على مجموعة التطوير، newstest2013. استخدمنا البحث الشعاعي كما هو موضح في القسم السابق، ولكن بدون حساب متوسط نقاط التفتيش. نقدم هذه النتائج في الجدول 3.

في صفوف الجدول 3 (A)، نغيّر عدد رؤوس الانتباه وأبعاد مفاتيح وقيم الانتباه، مع الحفاظ على كمية الحساب ثابتة، كما هو موضح في القسم 3.2.2. بينما الانتباه أحادي الرأس أسوأ بـ 0.9 BLEU من الإعداد الأفضل، تنخفض الجودة أيضاً مع وجود عدد كبير جداً من الرؤوس.

في صفوف الجدول 3 (B)، نلاحظ أن تقليل حجم مفتاح الانتباه d_k يضر بجودة النموذج. يشير هذا إلى أن تحديد التوافق ليس سهلاً وأن دالة توافق أكثر تطوراً من الجداء النقطي قد تكون مفيدة. نلاحظ أيضاً في الصفوف (C) و(D) أنه، كما هو متوقع، النماذج الأكبر أفضل، والإسقاط مفيد جداً في تجنب الإفراط في الملاءمة (over-fitting). في الصف (E) نستبدل ترميزنا الموضعي الجيبي بتضمينات موضعية مُتعلّمة [9]، ونلاحظ نتائج متطابقة تقريباً مع النموذج الأساسي.

## 6.3 تحليل البنية التركيبية للإنجليزية

لتقييم ما إذا كان يمكن للمحوّل التعميم على مهام أخرى، أجرينا تجارب على تحليل البنية التركيبية للإنجليزية (English constituency parsing). تقدّم هذه المهمة تحديات محددة: الإخراج يخضع لقيود هيكلية قوية وأطول بكثير من الإدخال. علاوة على ذلك، لم تتمكن نماذج الشبكات العصبية التكرارية من التسلسل إلى التسلسل من تحقيق نتائج متطورة في أنظمة البيانات الصغيرة [37].

درّبنا محوّلاً من 4 طبقات مع d_model = 1024 على جزء Wall Street Journal (WSJ) من Penn Treebank [25]، حوالي 40 ألف جملة تدريب. درّبناه أيضاً في إعداد شبه إشرافي، باستخدام مجموعات البيانات الأكبر عالية الثقة و BerkleyParser مع حوالي 17 مليون جملة [37]. استخدمنا مفردات من 16 ألف رمز لإعداد WSJ فقط ومفردات من 32 ألف رمز للإعداد شبه الإشرافي.

أجرينا عدداً صغيراً فقط من التجارب لاختيار الإسقاط، سواء الانتباه والمتبقي (القسم 5.4)، ومعدلات التعلّم وحجم الشعاع على مجموعة التطوير القسم 22، وظلت جميع المعاملات الأخرى دون تغيير من نموذج الترجمة الأساسي من الإنجليزية إلى الألمانية. أثناء الاستدلال، زدنا الحد الأقصى لطول الإخراج إلى طول الإدخال + 300. استخدمنا حجم شعاع 21 و α = 0.3 لكل من إعداد WSJ فقط والإعداد شبه الإشرافي.

تُظهر نتائجنا في الجدول 4 أنه على الرغم من عدم وجود ضبط خاص بالمهمة، فإن نموذجنا يؤدي بشكل جيد بشكل مدهش، مُحققاً نتائج أفضل من جميع النماذج المُبلّغ عنها سابقاً باستثناء قواعد الشبكات العصبية التكرارية (Recurrent Neural Network Grammar) [8].

على عكس نماذج الشبكات العصبية التكرارية من التسلسل إلى التسلسل [37]، يتفوق المحوّل على Berkeley-Parser [29] حتى عند التدريب فقط على مجموعة تدريب WSJ المكونة من 40 ألف جملة.

---

### Translation Notes

- **Figures referenced:** None
- **Tables referenced:** Table 2 (الجدول 2), Table 3 (الجدول 3), Table 4 (الجدول 4)
- **Key terms introduced:**
  - State-of-the-art (متطور / نقطة مرجعية جديدة متطورة)
  - Ensemble (تجميعات)
  - Training cost (تكلفة التدريب)
  - Checkpoint (نقطة تفتيش)
  - Checkpoint averaging (حساب متوسط نقاط التفتيش)
  - Beam search (البحث الشعاعي)
  - Beam size (حجم الشعاع)
  - Length penalty (عقوبة الطول)
  - Development set (مجموعة التطوير)
  - Inference (الاستدلال)
  - Floating point operations (عمليات الفاصلة العائمة)
  - Single-precision (أحادية الدقة)
  - Model variations (تباينات النموذج)
  - Attention heads (رؤوس الانتباه)
  - Over-fitting (الإفراط في الملاءمة)
  - English constituency parsing (تحليل البنية التركيبية للإنجليزية)
  - Structural constraints (قيود هيكلية)
  - Small-data regimes (أنظمة البيانات الصغيرة)
  - Semi-supervised setting (إعداد شبه إشرافي)
  - Task-specific tuning (ضبط خاص بالمهمة)
  - Recurrent Neural Network Grammar (قواعد الشبكات العصبية التكرارية)

- **Equations:** None
- **Citations:** [38], [9], [37], [25], [8], [29] all preserved

- **Special handling:**
  - Dataset names kept in English (WMT 2014, newstest2013, WSJ, Penn Treebank, BerkleyParser)
  - BLEU scores preserved as numbers
  - Model names preserved (Transformer (big), Berkeley-Parser)
  - GPU models (P100) kept in English
  - Variable names preserved: P_drop, d_k, d_model, α
  - Section references preserved (Section 3.2.2, Section 5.4, Section 22)
  - Table row references preserved (rows (A), (B), (C), (D), (E))

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
