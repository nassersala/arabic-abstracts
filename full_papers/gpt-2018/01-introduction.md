# Section 1: Introduction
## القسم 1: المقدمة

**Section:** Introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** deep learning, supervised learning, language model, pre-trained, word embeddings, semi-supervised, transformer, fine-tuning, natural language inference, question answering, semantic similarity, text classification

---

### English Version

The ability to learn effectively from raw text is crucial to alleviating the dependence on supervised learning in natural language processing (NLP). Most deep learning methods require substantial amounts of manually labeled data, which restricts their applicability in many domains that suffer from a dearth of annotated resources [61]. In these situations, models that can leverage linguistic information from unlabeled data provide a valuable alternative to gathering more annotation, which can be time-consuming and expensive. Further, even in cases where considerable supervision is available, learning good representations in an unsupervised fashion can provide a significant performance boost. The most compelling evidence for this so far has been the extensive use of pre-trained word embeddings [10,39,42] to improve performance on a range of NLP tasks [8,11,26,45].

Leveraging more than word-level information from unlabeled text, however, is challenging for two main reasons. First, it is unclear what type of optimization objectives are most effective at learning text representations that are useful for transfer. Recent research has looked at various objectives such as language modeling [44], machine translation [38], and discourse coherence [22], with each method outperforming the others on different tasks. Second, there is no consensus on the most effective way to transfer these learned representations to the target task. Existing techniques involve a combination of making task-specific changes to the model architecture [43,44], using intricate learning schemes [21] and adding auxiliary learning objectives [50]. These uncertainties have made it difficult to develop effective semi-supervised learning approaches for language processing.

In this paper, we explore a semi-supervised approach for language understanding tasks using a combination of unsupervised pre-training and supervised fine-tuning. Our goal is to learn a universal representation that transfers with little adaptation to a wide range of tasks. We assume access to a large corpus of unlabeled text and several datasets with manually annotated training examples (target tasks). Our setup does not require these target tasks to be in the same domain as the unlabeled corpus. We employ a two-stage training procedure. First, we use a language modeling objective on the unlabeled data to learn the initial parameters of a neural network model. Subsequently, we adapt these parameters to a target task using the corresponding supervised objective.

For our model architecture, we use the Transformer [62], which has been shown to perform strongly on various tasks such as machine translation [62], document generation [34], and syntactic parsing [29]. This model choice provides us with a more structured memory for handling long-term dependencies in text, compared to alternatives like recurrent networks, resulting in robust transfer performance across diverse tasks. During transfer, we utilize task-specific input adaptations derived from traversal-style approaches [52], which process structured text input as a single contiguous sequence of tokens. As we demonstrate in our experiments, these adaptations enable us to fine-tune effectively with minimal changes to the architecture of the pre-trained model.

We evaluate our approach on four types of language understanding tasks – natural language inference, question answering, semantic similarity, and text classification. Our general task-agnostic model outperforms discriminatively trained models that employ architectures specifically crafted for each task, significantly improving upon the state of the art in 9 out of the 12 tasks studied. For instance, we achieve absolute improvements of 8.9% on commonsense reasoning (Stories Cloze Test) [40], 5.7% on question answering (RACE) [30], 1.5% on textual entailment (MultiNLI) [66] and 5.5% on the recently introduced GLUE multi-task benchmark [64]. We also analyzed zero-shot behaviors of the pre-trained model on four different settings and demonstrate that it acquires useful linguistic knowledge for downstream tasks.

---

### النسخة العربية

إن القدرة على التعلم بفعالية من النصوص الخام أمر بالغ الأهمية للتخفيف من الاعتماد على التعلم الموجّه في معالجة اللغة الطبيعية (NLP). تتطلب معظم أساليب التعلم العميق كميات كبيرة من البيانات المُعنونة يدوياً، مما يحد من قابلية تطبيقها في العديد من المجالات التي تعاني من ندرة الموارد المُشروحة [61]. في هذه الحالات، توفر النماذج التي يمكنها الاستفادة من المعلومات اللغوية من البيانات غير المُعنونة بديلاً قيّماً لجمع المزيد من التعليقات التوضيحية، والتي يمكن أن تستغرق وقتاً طويلاً ومكلفة. علاوة على ذلك، حتى في الحالات التي يتوفر فيها إشراف كبير، فإن تعلم تمثيلات جيدة بطريقة غير موجهة يمكن أن يوفر تعزيزاً كبيراً في الأداء. الدليل الأكثر إقناعاً على ذلك حتى الآن هو الاستخدام الواسع لتضمينات الكلمات المُدربة مسبقاً [10،39،42] لتحسين الأداء في مجموعة من مهام معالجة اللغة الطبيعية [8،11،26،45].

ومع ذلك، فإن الاستفادة من معلومات تتجاوز مستوى الكلمات من النص غير المُعنون أمر صعب لسببين رئيسيين. أولاً، ليس من الواضح ما هو نوع أهداف التحسين الأكثر فعالية في تعلم تمثيلات نصية مفيدة للنقل. بحثت الأبحاث الحديثة في أهداف مختلفة مثل نمذجة اللغة [44]، والترجمة الآلية [38]، والتماسك الخطابي [22]، حيث تتفوق كل طريقة على الأخريات في مهام مختلفة. ثانياً، لا يوجد إجماع على الطريقة الأكثر فعالية لنقل هذه التمثيلات المُتعلمة إلى المهمة المستهدفة. تتضمن التقنيات الموجودة مزيجاً من إجراء تغييرات خاصة بالمهمة على معمارية النموذج [43،44]، واستخدام مخططات تعلم معقدة [21]، وإضافة أهداف تعلم مساعدة [50]. جعلت هذه الشكوك من الصعب تطوير أساليب تعلم شبه موجه فعالة لمعالجة اللغة.

في هذه الورقة، نستكشف نهجاً شبه موجه لمهام فهم اللغة باستخدام مزيج من التدريب المسبق غير الموجه والضبط الدقيق الموجه. هدفنا هو تعلم تمثيل عالمي ينتقل مع تكيّف بسيط إلى مجموعة واسعة من المهام. نفترض الوصول إلى مدونة كبيرة من النصوص غير المُعنونة والعديد من مجموعات البيانات مع أمثلة تدريب مُشروحة يدوياً (المهام المستهدفة). لا يتطلب إعدادنا أن تكون هذه المهام المستهدفة في نفس المجال الذي تنتمي إليه المدونة غير المُعنونة. نستخدم إجراء تدريب من مرحلتين. أولاً، نستخدم هدف نمذجة اللغة على البيانات غير المُعنونة لتعلم المعاملات الأولية لنموذج شبكة عصبية. لاحقاً، نُكيّف هذه المعاملات مع المهمة المستهدفة باستخدام الهدف الموجه المقابل.

بالنسبة لمعمارية نموذجنا، نستخدم المحوّل (Transformer) [62]، الذي ثبت أنه يؤدي بقوة في مهام مختلفة مثل الترجمة الآلية [62]، وتوليد المستندات [34]، والتحليل النحوي [29]. يوفر لنا هذا الاختيار للنموذج ذاكرة أكثر تنظيماً للتعامل مع التبعيات طويلة المدى في النص، مقارنةً بالبدائل مثل الشبكات المتكررة، مما يؤدي إلى أداء نقل قوي عبر المهام المتنوعة. أثناء النقل، نستخدم تكيفات إدخال خاصة بالمهمة مستمدة من أساليب النمط الاجتيازي [52]، والتي تعالج إدخال النص المنظم كتسلسل متجاور واحد من الرموز. كما نوضح في تجاربنا، تمكننا هذه التكيفات من إجراء ضبط دقيق فعال مع الحد الأدنى من التغييرات على معمارية النموذج المُدرب مسبقاً.

نُقيّم نهجنا على أربعة أنواع من مهام فهم اللغة - الاستنتاج اللغوي، والإجابة على الأسئلة، والتشابه الدلالي، وتصنيف النصوص. يتفوق نموذجنا العام المستقل عن المهام على النماذج المُدربة تمييزياً التي تستخدم معماريات مصممة خصيصاً لكل مهمة، محققاً تحسينات كبيرة على أحدث ما توصلت إليه التقنية في 9 من أصل 12 مهمة تمت دراستها. على سبيل المثال، نحقق تحسينات مطلقة بنسبة 8.9% في الاستدلال المنطقي (اختبار Stories Cloze) [40]، و5.7% في الإجابة على الأسئلة (RACE) [30]، و1.5% في الاستلزام النصي (MultiNLI) [66]، و5.5% في معيار GLUE متعدد المهام الذي تم تقديمه مؤخراً [64]. قمنا أيضاً بتحليل سلوكيات الصفر-لقطة للنموذج المُدرب مسبقاً في أربعة إعدادات مختلفة ونُظهر أنه يكتسب معرفة لغوية مفيدة للمهام النهائية.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:**
  - Supervised learning = التعلم الموجّه
  - Unsupervised = غير موجه
  - Semi-supervised = شبه موجه
  - Pre-trained word embeddings = تضمينات الكلمات المُدربة مسبقاً
  - Language modeling = نمذجة اللغة
  - Transfer learning = التعلم بالنقل
  - Transformer = المحوّل
  - Recurrent networks = الشبكات المتكررة
  - Tokens = الرموز
  - Zero-shot = الصفر-لقطة
  - Downstream tasks = المهام النهائية

- **Equations:** None in this section
- **Citations:** Preserved with original numbering [61], [10,39,42], etc.
- **Benchmark names:** Kept in English (Stories Cloze Test, RACE, MultiNLI, GLUE)

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.88
