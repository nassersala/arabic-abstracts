# Section 2.5: Modeling Multiple Segments
## القسم 2.5: نمذجة قطاعات متعددة

**Section:** modeling-segments
**Translation Quality:** 0.87
**Glossary Terms Used:** downstream tasks, question answering, pretraining, autoregressive, BERT, permutation language modeling, relative encoding, segment encoding, attention, generalization, finetuning

---

### English Version

Many downstream tasks have multiple input segments, e.g., a question and a context paragraph in question answering. We now discuss how we pretrain XLNet to model multiple segments in the autoregressive framework. During the pretraining phase, following BERT, we randomly sample two segments (either from the same context or not) and treat the concatenation of two segments as one sequence to perform permutation language modeling. We only reuse the memory that belongs to the same context. Specifically, the input to our model is the same as BERT: [CLS, A, SEP, B, SEP], where "SEP" and "CLS" are two special symbols and "A" and "B" are the two segments. Although we follow the two-segment data format, XLNet-Large does not use the objective of next sentence prediction [10] as it does not show consistent improvement in our ablation study (see Section 3.4).

**Relative Segment Encodings:** Architecturally, different from BERT that adds an absolute segment embedding to the word embedding at each position, we extend the idea of relative encodings from Transformer-XL to also encode the segments. Given a pair of positions $i$ and $j$ in the sequence, if $i$ and $j$ are from the same segment, we use a segment encoding $s_{ij} = s_+$ or otherwise $s_{ij} = s_-$, where $s_+$ and $s_-$ are learnable model parameters for each attention head. In other words, we only consider whether the two positions are within the same segment, as opposed to considering which specific segments they are from. This is consistent with the core idea of relative encodings; i.e., only modeling the relationships between positions. When $i$ attends to $j$, the segment encoding $s_{ij}$ is used to compute an attention weight $a_{ij} = (q_i + b)^{\top} s_{ij}$, where $q_i$ is the query vector as in a standard attention operation and $b$ is a learnable head-specific bias vector. Finally, the value $a_{ij}$ is added to the normal attention weight. There are two benefits of using relative segment encodings. First, the inductive bias of relative encodings improves generalization [9]. Second, it opens the possibility of finetuning on tasks that have more than two input segments, which is not possible using absolute segment encodings.

---

### النسخة العربية

تحتوي العديد من المهام اللاحقة على قطاعات إدخال متعددة، على سبيل المثال، سؤال وفقرة سياقية في الإجابة على الأسئلة. نناقش الآن كيف نقوم بالتدريب المسبق لـ XLNet لنمذجة قطاعات متعددة في إطار الانحدار الذاتي. خلال مرحلة التدريب المسبق، متبعين BERT، نأخذ عينات عشوائية من قطاعين (إما من نفس السياق أم لا) ونعامل تسلسل القطاعين كتسلسل واحد لإجراء النمذجة اللغوية بالتبديل. نعيد استخدام فقط الذاكرة التي تنتمي إلى نفس السياق. على وجه التحديد، المدخلات إلى نموذجنا هي نفسها في BERT: [CLS, A, SEP, B, SEP]، حيث "SEP" و "CLS" رمزان خاصان و "A" و "B" هما القطاعان. على الرغم من أننا نتبع تنسيق البيانات ذي القطاعين، لا يستخدم XLNet-Large هدف التنبؤ بالجملة التالية [10] حيث لا يظهر تحسناً متسقاً في دراسة الاستئصال الخاصة بنا (انظر القسم 3.4).

**ترميزات القطاعات النسبية:** من الناحية المعمارية، على عكس BERT الذي يضيف تضميناً مطلقاً للقطاع إلى تضمين الكلمة في كل موضع، نوسع فكرة الترميزات النسبية من Transformer-XL لترميز القطاعات أيضاً. بالنظر إلى زوج من المواضع $i$ و $j$ في التسلسل، إذا كان $i$ و $j$ من نفس القطاع، نستخدم ترميز قطاع $s_{ij} = s_+$ أو بخلاف ذلك $s_{ij} = s_-$، حيث $s_+$ و $s_-$ هما معاملات نموذج قابلة للتعلم لكل رأس انتباه. بعبارة أخرى، نأخذ في الاعتبار فقط ما إذا كان الموضعان ضمن نفس القطاع، على عكس النظر في القطاعات المحددة التي ينتميان إليها. هذا يتوافق مع الفكرة الأساسية للترميزات النسبية؛ أي نمذجة العلاقات بين المواضع فقط. عندما ينتبه $i$ إلى $j$، يتم استخدام ترميز القطاع $s_{ij}$ لحساب وزن انتباه $a_{ij} = (q_i + b)^{\top} s_{ij}$، حيث $q_i$ هو متجه الاستعلام كما في عملية الانتباه القياسية و $b$ هو متجه تحيز قابل للتعلم خاص بالرأس. أخيراً، يتم إضافة القيمة $a_{ij}$ إلى وزن الانتباه العادي. هناك فائدتان من استخدام ترميزات القطاعات النسبية. أولاً، يحسن التحيز الاستقرائي للترميزات النسبية التعميم [9]. ثانياً، يفتح إمكانية الضبط الدقيق على المهام التي تحتوي على أكثر من قطاعي إدخال، وهو أمر غير ممكن باستخدام ترميزات القطاعات المطلقة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** Relative segment encodings, segment encoding, inductive bias, head-specific bias
- **Equations:** Attention weight computation with segment encoding
- **Citations:** [10] for BERT next sentence prediction, [9] for Transformer-XL
- **Special handling:** Special tokens [CLS] and [SEP] kept in English as standard notation

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
