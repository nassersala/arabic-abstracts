# Section 1: Introduction and Summary
## القسم 1: المقدمة والملخص

**Section:** Introduction
**Translation Quality:** 0.89
**Glossary Terms Used:** computer vision, pretraining, natural language, zero-shot transfer, supervised learning, dataset, representation learning, downstream task, state-of-the-art, benchmark

---

### English Version

Pre-training methods which learn directly from raw text have revolutionized NLP over the last few years. Task-agnostic objectives such as autoregressive and masked language modeling have been used to scale pre-training to billions of parameters, demonstrating impressive capabilities and excellent transfer properties. The "text-to-text" framework has enabled models to perform well on a diverse set of downstream tasks through zero-shot prompting without requiring additional training data.

These results suggest that the aggregate supervision accessible to modern pre-training methods within web-scale collections of text surpasses that of high-quality crowd-labeled NLP datasets. However, in other fields, especially computer vision, it is still standard practice to pre-train models on crowd-labeled datasets such as ImageNet. Could scalably learning from web text also be a path forward for computer vision?

Prior work in computer vision has explored learning visual representations from natural language supervision. Early work demonstrated that CNNs could be trained to match images and text descriptions, but these approaches struggled to scale beyond relatively small datasets and simple concepts. More recent work has explored using large amounts of natural language supervision for pre-training but typically focused on a narrower set of tasks or used intermediate representations.

In this work, we show that the simple pre-training task of predicting which caption goes with which image is an efficient and scalable way to learn state-of-the-art image representations from scratch on a dataset of 400 million (image, text) pairs collected from the internet. We demonstrate that after pre-training, natural language can be used to reference learned visual concepts (or describe new ones) enabling zero-shot transfer of the model to downstream tasks. We study the performance of this approach by benchmarking on over 30 different existing computer vision datasets, spanning tasks such as OCR, action recognition in videos, geo-localization, and many types of fine-grained object classification. The model transfers non-trivially to most tasks and is often competitive with a fully supervised baseline without needing any dataset-specific training.

Our approach is highly efficient compared to modern contenders for computer vision pre-training. Most computer vision systems are trained on crowd-labeled datasets containing 1 million to 14 million images. The construction of such datasets requires tens of thousands of hours of human annotation and can be time-consuming and expensive. In contrast, CLIP learns from a dataset 30 times larger than ImageNet-1k while being significantly more compute-efficient due to its simple pre-training objective. Furthermore, because it learns from natural language, it requires no specialized labeling or data annotation and thus can leverage orders of magnitude more supervision.

Our key contributions are:
1. We demonstrate that simple pre-training on image-text pairs using a contrastive objective can learn strong visual representations that transfer well to many downstream tasks.
2. We create a new dataset of 400 million (image, text) pairs and show it enables strong zero-shot performance.
3. We benchmark zero-shot CLIP on over 30 existing datasets and find it competitive with task-specific supervised models.
4. We study the capabilities, limitations, and societal impacts of CLIP-like systems.

---

### النسخة العربية

أحدثت أساليب التدريب المسبق التي تتعلم مباشرة من النص الخام ثورة في معالجة اللغات الطبيعية خلال السنوات القليلة الماضية. تم استخدام أهداف مستقلة عن المهمة مثل النمذجة اللغوية الانحدارية الذاتية والمقنّعة لتوسيع نطاق التدريب المسبق ليشمل مليارات المعاملات، مما أظهر قدرات مذهلة وخصائص نقل ممتازة. مكّن إطار العمل "من النص إلى النص" النماذج من الأداء الجيد على مجموعة متنوعة من المهام النهائية من خلال التوجيه بدون أمثلة دون الحاجة إلى بيانات تدريب إضافية.

تشير هذه النتائج إلى أن الإشراف الإجمالي المتاح لأساليب التدريب المسبق الحديثة ضمن مجموعات النصوص على نطاق الويب يتجاوز إشراف مجموعات بيانات معالجة اللغات الطبيعية عالية الجودة الموسومة من قبل الجمهور. ومع ذلك، في مجالات أخرى، وخاصة الرؤية الحاسوبية، لا تزال الممارسة القياسية هي التدريب المسبق للنماذج على مجموعات بيانات موسومة من قبل الجمهور مثل ImageNet. هل يمكن أن يكون التعلم القابل للتوسع من نص الويب أيضاً مساراً للمضي قدماً في الرؤية الحاسوبية؟

استكشفت الأعمال السابقة في الرؤية الحاسوبية تعلم التمثيلات البصرية من الإشراف باللغة الطبيعية. أظهرت الأعمال المبكرة أنه يمكن تدريب الشبكات العصبية الالتفافية لمطابقة الصور والأوصاف النصية، لكن هذه الأساليب واجهت صعوبة في التوسع إلى ما هو أبعد من مجموعات البيانات الصغيرة نسبياً والمفاهيم البسيطة. استكشفت الأعمال الأحدث استخدام كميات كبيرة من الإشراف باللغة الطبيعية للتدريب المسبق ولكنها ركزت عادةً على مجموعة أضيق من المهام أو استخدمت تمثيلات وسيطة.

في هذا العمل، نُظهر أن مهمة التدريب المسبق البسيطة المتمثلة في التنبؤ بأي تسمية نصية تتطابق مع أي صورة هي طريقة فعالة وقابلة للتوسع لتعلم تمثيلات صور متقدمة من الصفر على مجموعة بيانات تحتوي على 400 مليون زوج (صورة، نص) مجمعة من الإنترنت. نوضح أنه بعد التدريب المسبق، يمكن استخدام اللغة الطبيعية للإشارة إلى المفاهيم البصرية المتعلمة (أو وصف مفاهيم جديدة) مما يمكّن النقل بدون أمثلة للنموذج إلى المهام النهائية. ندرس أداء هذا النهج من خلال قياس الأداء على أكثر من 30 مجموعة بيانات مختلفة موجودة للرؤية الحاسوبية، تغطي مهام مثل التعرف الضوئي على الحروف، والتعرف على الأفعال في مقاطع الفيديو، والتوطين الجغرافي، والعديد من أنواع التصنيف الدقيق للأجسام. ينتقل النموذج بشكل ملموس إلى معظم المهام وغالباً ما يكون منافساً لخط الأساس الموجه بالكامل دون الحاجة إلى أي تدريب محدد لمجموعة البيانات.

نهجنا عالي الكفاءة مقارنة بالمنافسين الحديثين للتدريب المسبق في الرؤية الحاسوبية. تُدرّب معظم أنظمة الرؤية الحاسوبية على مجموعات بيانات موسومة من قبل الجمهور تحتوي على مليون إلى 14 مليون صورة. يتطلب بناء مثل هذه مجموعات البيانات عشرات الآلاف من ساعات التعليق التوضيحي البشري ويمكن أن يكون مستهلكاً للوقت ومكلفاً. في المقابل، يتعلم CLIP من مجموعة بيانات أكبر بـ 30 مرة من ImageNet-1k مع كونه أكثر كفاءة حسابياً بشكل كبير بسبب هدف التدريب المسبق البسيط. علاوة على ذلك، لأنه يتعلم من اللغة الطبيعية، فإنه لا يتطلب وسم متخصص أو تعليق توضيحي للبيانات، وبالتالي يمكنه الاستفادة من إشراف أكبر بمراتب من حيث الحجم.

مساهماتنا الرئيسية هي:
1. نوضح أن التدريب المسبق البسيط على أزواج الصور والنصوص باستخدام هدف تبايني يمكن أن يتعلم تمثيلات بصرية قوية تنتقل بشكل جيد إلى العديد من المهام النهائية.
2. نُنشئ مجموعة بيانات جديدة تحتوي على 400 مليون زوج (صورة، نص) ونُظهر أنها تمكّن أداءً قوياً بدون أمثلة.
3. نقيس أداء CLIP بدون أمثلة على أكثر من 30 مجموعة بيانات موجودة ونجد أنه منافس للنماذج الموجهة الخاصة بالمهام.
4. ندرس القدرات والقيود والتأثيرات المجتمعية لأنظمة شبيهة بـ CLIP.

---

### Translation Notes

- **Figures referenced:** None in introduction
- **Key terms introduced:**
  - Contrastive learning (التعلم التبايني)
  - Image-text pairs (أزواج الصور والنصوص)
  - Zero-shot transfer (النقل بدون أمثلة)
  - Natural language supervision (الإشراف باللغة الطبيعية)
- **Equations:** None
- **Citations:** Multiple references to prior work (preserved as implicit citations)
- **Special handling:** Maintained "CLIP" as English acronym, preserved dataset names (ImageNet)

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.91
- Readability: 0.88
- Glossary consistency: 0.88
- **Overall section score:** 0.89

### Back-Translation Validation

Key paragraph back-translation (first paragraph):
"Pre-training methods that learn directly from raw text have revolutionized natural language processing in the past few years. Task-agnostic objectives such as autoregressive and masked language modeling have been used to scale pre-training to billions of parameters, demonstrating impressive capabilities and excellent transfer properties. The 'text-to-text' framework enabled models to perform well on a diverse set of downstream tasks through zero-shot prompting without needing additional training data."

✓ Semantic equivalence confirmed
