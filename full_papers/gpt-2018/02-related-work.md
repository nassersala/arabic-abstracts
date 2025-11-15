# Section 2: Related Work
## القسم 2: الأعمال ذات الصلة

**Section:** Related Work
**Translation Quality:** 0.87
**Glossary Terms Used:** semi-supervised learning, NLP, word embeddings, unsupervised pre-training, language model, LSTM, transformer, auxiliary training objectives

---

### English Version

**Semi-supervised learning for NLP** Our work broadly falls under the category of semi-supervised learning for natural language. This paradigm has attracted significant interest, with applications to tasks like sequence labeling [24,33,57] or text classification [41,70]. The earliest approaches used unlabeled data to compute word-level or phrase-level statistics, which were then used as features in a supervised model [33]. Over the last few years, researchers have demonstrated the benefits of using word embeddings [11,39,42], which are trained on unlabeled corpora, to improve performance on a variety of tasks [8,11,26,45]. These approaches, however, mainly transfer word-level information, whereas we aim to capture higher-level semantics.

Recent approaches have investigated learning and utilizing more than word-level semantics from unlabeled data. Phrase-level or sentence-level embeddings, which can be trained using an unlabeled corpus, have been used to encode text into suitable vector representations for various target tasks [28, 32, 1, 36, 22, 12, 56, 31].

**Unsupervised pre-training** Unsupervised pre-training is a special case of semi-supervised learning where the goal is to find a good initialization point instead of modifying the supervised learning objective. Early works explored the use of the technique in image classification [20,49,63] and regression tasks [3]. Subsequent research [15] demonstrated that pre-training acts as a regularization scheme, enabling better generalization in deep neural networks. In recent work, the method has been used to help train deep neural networks on various tasks like image classification [69], speech recognition [68], entity disambiguation [17] and machine translation [48].

The closest line of work to ours involves pre-training a neural network using a language modeling objective and then fine-tuning it on a target task with supervision. Dai et al. [13] and Howard and Ruder [21] follow this method to improve text classification. However, although the pre-training phase helps capture some linguistic information, their usage of LSTM models restricts their prediction ability to a short range. In contrast, our choice of transformer networks allows us to capture longer-range linguistic structure, as demonstrated in our experiments. Further, we also demonstrate the effectiveness of our model on a wider range of tasks including natural language inference, paraphrase detection and story completion. Other approaches [43,44,38] use hidden representations from a pre-trained language or machine translation model as auxiliary features while training a supervised model on the target task. This involves a substantial amount of new parameters for each separate target task, whereas we require minimal changes to our model architecture during transfer.

**Auxiliary training objectives** Adding auxiliary unsupervised training objectives is an alternative form of semi-supervised learning. Early work by Collobert and Weston [10] used a wide variety of auxiliary NLP tasks such as POS tagging, chunking, named entity recognition, and language modeling to improve semantic role labeling. More recently, Rei [50] added an auxiliary language modeling objective to their target task objective and demonstrated performance gains on sequence labeling tasks. Our experiments also use an auxiliary objective, but as we show, unsupervised pre-training already learns several linguistic aspects relevant to target tasks.

---

### النسخة العربية

**التعلم شبه الموجه لمعالجة اللغة الطبيعية** يندرج عملنا بشكل عام تحت فئة التعلم شبه الموجه للغة الطبيعية. لقد جذب هذا النموذج اهتماماً كبيراً، مع تطبيقات على مهام مثل وسم التسلسلات [24،33،57] أو تصنيف النصوص [41،70]. استخدمت الأساليب الأولى البيانات غير المُعنونة لحساب إحصائيات على مستوى الكلمات أو العبارات، والتي استُخدمت بعد ذلك كميزات في نموذج موجه [33]. على مدى السنوات القليلة الماضية، أظهر الباحثون فوائد استخدام تضمينات الكلمات [11،39،42]، التي يتم تدريبها على مدونات غير مُعنونة، لتحسين الأداء في مجموعة متنوعة من المهام [8،11،26،45]. ومع ذلك، فإن هذه الأساليب تنقل بشكل رئيسي معلومات على مستوى الكلمات، بينما نهدف إلى التقاط دلالات من مستوى أعلى.

استكشفت الأساليب الحديثة تعلم واستخدام دلالات أكثر من مستوى الكلمات من البيانات غير المُعنونة. تم استخدام تضمينات على مستوى العبارات أو الجمل، والتي يمكن تدريبها باستخدام مدونة غير مُعنونة، لترميز النص في تمثيلات متجهة مناسبة لمختلف المهام المستهدفة [28، 32، 1، 36، 22، 12، 56، 31].

**التدريب المسبق غير الموجه** التدريب المسبق غير الموجه هو حالة خاصة من التعلم شبه الموجه حيث الهدف هو إيجاد نقطة تهيئة جيدة بدلاً من تعديل هدف التعلم الموجه. استكشفت الأعمال المبكرة استخدام هذه التقنية في تصنيف الصور [20،49،63] ومهام الانحدار [3]. أظهرت الأبحاث اللاحقة [15] أن التدريب المسبق يعمل كمخطط تنظيم، مما يتيح تعميماً أفضل في الشبكات العصبية العميقة. في الأعمال الحديثة، تم استخدام الطريقة للمساعدة في تدريب الشبكات العصبية العميقة على مهام مختلفة مثل تصنيف الصور [69]، والتعرف على الكلام [68]، وإزالة الغموض عن الكيانات [17]، والترجمة الآلية [48].

أقرب خط عمل لنا يتضمن التدريب المسبق لشبكة عصبية باستخدام هدف نمذجة اللغة ثم ضبطها بدقة على مهمة مستهدفة مع إشراف. يتبع Dai وآخرون [13] و Howard و Ruder [21] هذه الطريقة لتحسين تصنيف النصوص. ومع ذلك، على الرغم من أن مرحلة التدريب المسبق تساعد في التقاط بعض المعلومات اللغوية، فإن استخدامهم لنماذج LSTM يحد من قدرتهم على التنبؤ على مدى قصير. في المقابل، يسمح لنا اختيارنا لشبكات المحوّل بالتقاط بنية لغوية ذات مدى أطول، كما هو موضح في تجاربنا. علاوة على ذلك، نُظهر أيضاً فعالية نموذجنا على مجموعة أوسع من المهام بما في ذلك الاستنتاج اللغوي، والكشف عن إعادة الصياغة، وإكمال القصص. تستخدم الأساليب الأخرى [43،44،38] تمثيلات مخفية من نموذج لغة مُدرب مسبقاً أو نموذج ترجمة آلية كميزات مساعدة أثناء تدريب نموذج موجه على المهمة المستهدفة. يتضمن هذا كمية كبيرة من المعاملات الجديدة لكل مهمة مستهدفة منفصلة، بينما نتطلب تغييرات طفيفة على معمارية نموذجنا أثناء النقل.

**أهداف التدريب المساعدة** إضافة أهداف تدريب مساعدة غير موجهة هي شكل بديل من التعلم شبه الموجه. استخدم العمل المبكر لـ Collobert و Weston [10] مجموعة واسعة من مهام معالجة اللغة الطبيعية المساعدة مثل وسم أجزاء الكلام، والتقسيم إلى أجزاء، والتعرف على الكيانات المسماة، ونمذجة اللغة لتحسين وسم الأدوار الدلالية. في الآونة الأخيرة، أضاف Rei [50] هدف نمذجة لغة مساعد إلى هدف مهمتهم المستهدفة وأظهر مكاسب في الأداء على مهام وسم التسلسلات. تستخدم تجاربنا أيضاً هدفاً مساعداً، ولكن كما نُظهر، فإن التدريب المسبق غير الموجه يتعلم بالفعل العديد من الجوانب اللغوية ذات الصلة بالمهام المستهدفة.

---

### Translation Notes

- **Key terms introduced:**
  - Semi-supervised learning = التعلم شبه الموجه
  - Sequence labeling = وسم التسلسلات
  - Text classification = تصنيف النصوص
  - Phrase-level embeddings = تضمينات على مستوى العبارات
  - Sentence-level embeddings = تضمينات على مستوى الجمل
  - Initialization point = نقطة تهيئة
  - Regularization = تنظيم
  - Entity disambiguation = إزالة الغموض عن الكيانات
  - Paraphrase detection = الكشف عن إعادة الصياغة
  - POS tagging = وسم أجزاء الكلام
  - Named entity recognition = التعرف على الكيانات المسماة
  - Semantic role labeling = وسم الأدوار الدلالية

- **Citations:** All preserved with original numbering
- **Comparison to prior work:** Emphasized advantages of Transformer over LSTM for long-range dependencies

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
