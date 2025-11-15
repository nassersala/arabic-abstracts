# Section 1: Introduction
## القسم 1: المقدمة

**Section:** Introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** natural language processing, transfer learning, pre-training, fine-tuning, unsupervised learning, supervised learning, neural networks, transformer, text-to-text, benchmark, state-of-the-art, corpus, scalability

---

### English Version

Training a machine learning model to perform natural language processing (NLP) tasks often requires that the model can process text in a way that is amenable to downstream learning. This can be loosely viewed as developing general-purpose knowledge that allows the model to "understand" text. This knowledge can range from low-level (e.g. the spelling or meaning of words) to high-level (e.g. that a tuba is too large to fit in most backpacks). In modern machine learning practice, providing this knowledge is rarely done explicitly; instead, it is often learned as part of an auxiliary task. For example, a historically common approach is to use word vectors to map word identities to a continuous representation where, ideally, similar words map to similar vectors. These vectors are often learned through an objective that, for example, encourages co-occurring words to be positioned nearby in the continuous space.

Recently, it has become increasingly common to pre-train the entire model on a data-rich task. Ideally, this pre-training causes the model to develop general-purpose abilities and knowledge that can then be transferred to downstream tasks. In applications of transfer learning to computer vision, pre-training is typically done via supervised learning on a large labeled data set like ImageNet. In contrast, modern techniques for transfer learning in NLP often pre-train using unsupervised learning on unlabeled data. This approach has recently been used to obtain state-of-the-art results in many of the most common NLP benchmarks. Beyond its empirical strength, unsupervised pre-training for NLP is particularly attractive because unlabeled text data is available en masse thanks to the Internet---for example, the Common Crawl project produces about 20TB of text data extracted from web pages each month. This is a natural fit for neural networks, which have been shown to exhibit remarkable scalability, i.e. it is often possible to achieve better performance simply by training a larger model on a larger data set.

This synergy has resulted in a great deal of recent work developing transfer learning methodology for NLP, which has produced a wide landscape of pre-training objectives, unlabeled data sets, benchmarks, fine-tuning methods, and more. The rapid rate of progress and diversity of techniques in this burgeoning field can make it difficult to compare different algorithms, tease apart the effects of new contributions, and understand the space of existing methods for transfer learning. Motivated by a need for more rigorous understanding, we leverage a unified approach to transfer learning that allows us to systematically study different approaches and push the current limits of the field.

**Figure 1:** A diagram of our text-to-text framework. Every task we consider---including translation, question answering, and classification---is cast as feeding our model text as input and training it to generate some target text. This allows us to use the same model, loss function, hyperparameters, etc. across our diverse set of tasks. It also provides a standard testbed for the methods included in our empirical survey. "T5" refers to our model, which we dub the "Text-to-Text Transfer Transformer".

The basic idea underlying our work is to treat every text processing problem as a "text-to-text" problem, i.e. taking text as input and producing new text as output. This approach is inspired by previous unifying frameworks for NLP tasks, including casting all text problems as question answering, language modeling, or span extraction tasks. Crucially, the text-to-text framework allows us to directly apply the same model, objective, training procedure, and decoding process to every task we consider. We leverage this flexibility by evaluating performance on a wide variety of English-based NLP problems, including question answering, document summarization, and sentiment classification, to name a few. With this unified approach, we can compare the effectiveness of different transfer learning objectives, unlabeled data sets, and other factors, while exploring the limits of transfer learning for NLP by scaling up models and data sets beyond what has previously been considered.

We emphasize that our goal is not to propose new methods but instead to provide a comprehensive perspective on where the field stands. As such, our work primarily comprises a survey, exploration, and empirical comparison of existing techniques. We also explore the limits of current approaches by scaling up the insights from our systematic study (training models up to 11 billion parameters) to obtain state-of-the-art results in many of the tasks we consider. In order to perform experiments at this scale, we introduce the "Colossal Clean Crawled Corpus" (C4), a data set consisting of hundreds of gigabytes of clean English text scraped from the web. Recognizing that the main utility of transfer learning is the possibility of leveraging pre-trained models in data-scarce settings, we release our code, data sets, and pre-trained models.

The remainder of the paper is structured as follows: In the following section, we discuss our base model and its implementation, our procedure for formulating every text processing problem as a text-to-text task, and the suite of tasks we consider. In Section 3, we present a large set of experiments that explore the field of transfer learning for NLP. At the end of the section, we combine insights from our systematic study to obtain state-of-the-art results on a wide variety of benchmarks. Finally, we provide a summary of our results and wrap up with a look towards the future in Section 4.

---

### النسخة العربية

غالباً ما يتطلب تدريب نموذج تعلم آلي لأداء مهام معالجة اللغة الطبيعية أن يكون النموذج قادراً على معالجة النصوص بطريقة تكون ملائمة للتعلم اللاحق. يمكن النظر إلى هذا بشكل عام على أنه تطوير معرفة عامة الغرض تسمح للنموذج "بفهم" النصوص. يمكن أن تتراوح هذه المعرفة من المستوى المنخفض (مثل تهجئة الكلمات أو معناها) إلى المستوى العالي (مثل أن التوبا كبيرة جداً بحيث لا تناسب معظم حقائب الظهر). في ممارسات التعلم الآلي الحديثة، نادراً ما يتم توفير هذه المعرفة بشكل صريح؛ بدلاً من ذلك، غالباً ما يتم تعلمها كجزء من مهمة مساعدة. على سبيل المثال، من الأساليب الشائعة تاريخياً استخدام متجهات الكلمات لتعيين هويات الكلمات إلى تمثيل مستمر حيث، بشكل مثالي، تُعيَّن الكلمات المتشابهة إلى متجهات متشابهة. غالباً ما يتم تعلم هذه المتجهات من خلال هدف يشجع، على سبيل المثال، الكلمات المتواجدة معاً على أن تكون موضعة بالقرب من بعضها البعض في الفضاء المستمر.

في الآونة الأخيرة، أصبح من الشائع بشكل متزايد التدريب المسبق للنموذج بأكمله على مهمة غنية بالبيانات. بشكل مثالي، يتسبب هذا التدريب المسبق في تطوير النموذج لقدرات ومعرفة عامة الغرض يمكن نقلها بعد ذلك إلى المهام اللاحقة. في تطبيقات التعلم بالنقل على الرؤية الحاسوبية، يتم التدريب المسبق عادةً عبر التعلم الخاضع للإشراف على مجموعة بيانات معنونة كبيرة مثل ImageNet. في المقابل، تستخدم التقنيات الحديثة للتعلم بالنقل في معالجة اللغة الطبيعية غالباً التدريب المسبق باستخدام التعلم غير الخاضع للإشراف على البيانات غير المعنونة. تم استخدام هذا النهج مؤخراً للحصول على نتائج متقدمة في العديد من معايير معالجة اللغة الطبيعية الأكثر شيوعاً. بالإضافة إلى قوته التجريبية، فإن التدريب المسبق غير الخاضع للإشراف لمعالجة اللغة الطبيعية جذاب بشكل خاص لأن البيانات النصية غير المعنونة متوفرة بكميات كبيرة بفضل الإنترنت---على سبيل المثال، ينتج مشروع Common Crawl حوالي 20 تيرابايت من البيانات النصية المستخرجة من صفحات الويب كل شهر. هذا يتناسب بشكل طبيعي مع الشبكات العصبية، التي ثبت أنها تُظهر قابلية تطوير ملحوظة، أي أنه من الممكن غالباً تحقيق أداء أفضل ببساطة عن طريق تدريب نموذج أكبر على مجموعة بيانات أكبر.

أدى هذا التآزر إلى قدر كبير من الأعمال الحديثة لتطوير منهجيات التعلم بالنقل لمعالجة اللغة الطبيعية، والتي أنتجت مشهداً واسعاً من أهداف التدريب المسبق ومجموعات البيانات غير المعنونة والمعايير وأساليب الضبط الدقيق، والمزيد. يمكن أن يجعل معدل التقدم السريع وتنوع التقنيات في هذا المجال الناشئ من الصعب مقارنة الخوارزميات المختلفة، والفصل بين تأثيرات المساهمات الجديدة، وفهم مجال الطرق الموجودة للتعلم بالنقل. بدافع من الحاجة إلى فهم أكثر دقة، نستفيد من نهج موحد للتعلم بالنقل يسمح لنا بدراسة الأساليب المختلفة بشكل منهجي ودفع الحدود الحالية للمجال.

**الشكل 1:** رسم تخطيطي لإطار عملنا من نص إلى نص. كل مهمة ندرسها---بما في ذلك الترجمة والإجابة على الأسئلة والتصنيف---يتم صياغتها على أنها تغذية نموذجنا بنص كمدخل وتدريبه على توليد نص مستهدف. يتيح لنا هذا استخدام نفس النموذج ودالة الخسارة والمعاملات الفائقة، إلخ. عبر مجموعتنا المتنوعة من المهام. كما أنه يوفر منصة اختبار قياسية للطرق المضمنة في مسحنا التجريبي. يشير "T5" إلى نموذجنا، الذي نطلق عليه اسم "محول النقل من نص إلى نص" (Text-to-Text Transfer Transformer).

الفكرة الأساسية وراء عملنا هي معاملة كل مشكلة معالجة نصوص على أنها مشكلة "من نص إلى نص"، أي أخذ النص كمدخل وإنتاج نص جديد كمخرج. هذا النهج مستوحى من أطُر العمل الموحدة السابقة لمهام معالجة اللغة الطبيعية، بما في ذلك صياغة جميع مشاكل النصوص على أنها مهام إجابة على الأسئلة أو نمذجة اللغة أو استخراج الامتدادات. والأهم من ذلك، يسمح لنا إطار العمل من نص إلى نص بتطبيق نفس النموذج والهدف وإجراء التدريب وعملية فك التشفير مباشرة على كل مهمة ندرسها. نستفيد من هذه المرونة من خلال تقييم الأداء على مجموعة واسعة من مشاكل معالجة اللغة الطبيعية القائمة على اللغة الإنجليزية، بما في ذلك الإجابة على الأسئلة وتلخيص المستندات وتصنيف المشاعر، على سبيل المثال لا الحصر. باستخدام هذا النهج الموحد، يمكننا مقارنة فعالية أهداف التعلم بالنقل المختلفة ومجموعات البيانات غير المعنونة وعوامل أخرى، مع استكشاف حدود التعلم بالنقل لمعالجة اللغة الطبيعية من خلال توسيع نطاق النماذج ومجموعات البيانات إلى ما هو أبعد مما تم النظر فيه سابقاً.

نؤكد أن هدفنا ليس اقتراح طرق جديدة ولكن بدلاً من ذلك توفير منظور شامل عن الوضع الحالي للمجال. على هذا النحو، يتضمن عملنا بشكل أساسي مسحاً واستكشافاً ومقارنة تجريبية للتقنيات الموجودة. نستكشف أيضاً حدود الأساليب الحالية من خلال توسيع نطاق الرؤى من دراستنا المنهجية (تدريب نماذج تصل إلى 11 مليار معامل) للحصول على نتائج متقدمة في العديد من المهام التي ندرسها. من أجل إجراء تجارب على هذا النطاق، نقدم "مدونة الزحف النظيفة الضخمة" (C4)، وهي مجموعة بيانات تتكون من مئات الجيجابايتات من النصوص الإنجليزية النظيفة المستخرجة من الويب. إدراكاً منا أن الفائدة الرئيسية للتعلم بالنقل هي إمكانية الاستفادة من النماذج المدربة مسبقاً في البيئات الشحيحة بالبيانات، نصدر الكود ومجموعات البيانات والنماذج المدربة مسبقاً.

يتم تنظيم بقية البحث على النحو التالي: في القسم التالي، نناقش نموذجنا الأساسي وتنفيذه، وإجراءنا لصياغة كل مشكلة معالجة نصوص على أنها مهمة من نص إلى نص، ومجموعة المهام التي ندرسها. في القسم 3، نقدم مجموعة كبيرة من التجارب التي تستكشف مجال التعلم بالنقل لمعالجة اللغة الطبيعية. في نهاية القسم، نجمع الرؤى من دراستنا المنهجية للحصول على نتائج متقدمة على مجموعة واسعة من المعايير. أخيراً، نقدم ملخصاً لنتائجنا ونختتم بنظرة نحو المستقبل في القسم 4.

---

### Translation Notes

- **Figures referenced:** Figure 1 (text-to-text framework diagram)
- **Key terms introduced:** text-to-text framework, T5 model, C4 corpus, transfer learning, pre-training
- **Equations:** 0
- **Citations:** Multiple citations to previous work (preserved in translation)
- **Special handling:** Model size (11 billion parameters), dataset size (20TB/month, hundreds of GB)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
