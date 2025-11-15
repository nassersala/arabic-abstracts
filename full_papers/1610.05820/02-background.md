# Section 2: Background and Related Work
## القسم 2: الخلفية والأعمال ذات الصلة

**Section:** background
**Translation Quality:** 0.86
**Glossary Terms Used:** privacy (خصوصية), differential privacy (خصوصية تفاضلية), machine learning (تعلم الآلة), training data (بيانات التدريب), cryptographic (تشفيري), homomorphic encryption (التشفير المتماثل), secure computation (حوسبة آمنة), model inversion (انعكاس النموذج), adversarial examples (أمثلة خصامية)

---

### English Version

## Machine Learning

Machine learning algorithms learn predictive models from training data. In supervised learning, the training dataset consists of input-output pairs $(x_i, y_i)$, where $x_i$ is a feature vector and $y_i$ is the corresponding label. The goal is to learn a function $f: X \rightarrow Y$ that maps inputs to outputs. For classification tasks, the output $y$ is a discrete class label; for regression tasks, it is a continuous value.

The learning algorithm produces a model by optimizing some objective function on the training data. For example, in neural networks, the model parameters (weights and biases) are adjusted to minimize a loss function such as cross-entropy loss for classification or mean squared error for regression. The model is then deployed to make predictions on new, previously unseen inputs.

A fundamental challenge in machine learning is to ensure that the learned model generalizes well to new data. Overfitting occurs when a model learns patterns specific to the training data that do not generalize. Regularization techniques, such as L1 and L2 regularization, dropout, and early stopping, are commonly used to prevent overfitting and improve generalization.

## Privacy in Machine Learning

Privacy concerns in machine learning arise because training data often contains sensitive information about individuals. Several approaches have been proposed to protect privacy in machine learning:

**Differential privacy.** Differential privacy [1, 2] is a rigorous mathematical framework for privacy that provides strong guarantees. A randomized algorithm $\mathcal{M}$ satisfies $(\epsilon, \delta)$-differential privacy if for all neighboring datasets $D$ and $D'$ that differ in one record, and for all possible outputs $S$:

$$Pr[\mathcal{M}(D) \in S] \leq e^\epsilon \cdot Pr[\mathcal{M}(D') \in S] + \delta$$

Differential privacy has been applied to machine learning through techniques such as adding noise to gradients during training [3, 4] or to the model's outputs. However, differential privacy often comes with a utility cost: the added noise can reduce model accuracy.

**Cryptographic approaches.** Secure multi-party computation and homomorphic encryption enable training machine learning models on encrypted data without revealing the raw data to any party [5, 6]. While these approaches provide strong cryptographic guarantees, they often incur significant computational overhead and may not scale to large models or datasets.

**Federated learning.** In federated learning [7], multiple parties collaboratively train a model without sharing their raw data. Each party trains a local model on its own data and shares only model updates (e.g., gradients) with a central server, which aggregates them to update a global model. However, recent work has shown that even sharing gradients can leak information about training data [8, 9].

## Privacy Attacks on Machine Learning

Several types of privacy attacks on machine learning models have been studied:

**Model inversion attacks.** Model inversion attacks [10, 11] aim to reconstruct training data or extract sensitive features from a trained model. For example, Fredrikson et al. [10] showed that given a person's name and access to a facial recognition model, an attacker can reconstruct an image of that person's face. These attacks typically require white-box access to the model or knowledge of the model's gradients.

**Property inference attacks.** Property inference attacks [12] infer statistical properties of the training dataset, such as the proportion of records with a certain attribute, without targeting specific individuals.

**Adversarial examples.** Adversarial examples [13, 14] are inputs crafted to cause a model to make incorrect predictions. While primarily studied in the context of model robustness, adversarial examples can also reveal information about the model's training data and decision boundaries.

**Membership inference.** Membership inference is the problem we address in this paper. The goal is to determine whether a specific record was in the model's training dataset. Prior work on membership inference has been limited. Dwork et al. [15] showed that overfitted models can leak information about individual training records. Homer et al. [16] demonstrated membership inference attacks on genomic data in genome-wide association studies. However, no prior work has systematically studied membership inference attacks on general machine learning models, particularly in the black-box setting.

## Machine Learning as a Service

Cloud providers now offer machine learning as a service (MLaaS), where users can upload training data and obtain trained models, or directly query pre-trained models. Examples include Google Prediction API, Amazon Machine Learning, Microsoft Azure ML, and BigML. In these services, the model is typically accessed via an API that allows users to submit queries and receive predictions. Users cannot directly access the model's parameters or training data.

This deployment model creates new privacy risks. Even if the service provider does not intentionally leak training data, the model itself—through its predictions—may inadvertently reveal information about the training data to adversaries who can query the model.

## Our Contribution

Our work differs from prior work in several important ways:

1. We develop a general, black-box membership inference attack that works on various types of machine learning models without requiring access to model parameters or gradients.

2. We introduce the shadow training technique to generate training data for the attack model when the adversary does not have access to the target model's training data.

3. We provide the first comprehensive evaluation of membership inference attacks on real-world machine learning models, including commercial MLaaS platforms.

4. We analyze the factors that make models vulnerable to membership inference and evaluate practical mitigation strategies.

---

### النسخة العربية

## تعلم الآلة

تتعلم خوارزميات تعلم الآلة نماذج تنبؤية من بيانات التدريب. في التعلم الخاضع للإشراف، تتكون مجموعة بيانات التدريب من أزواج مدخلات-مخرجات $(x_i, y_i)$، حيث $x_i$ هو متجه خصائص و$y_i$ هي التسمية المقابلة. الهدف هو تعلم دالة $f: X \rightarrow Y$ التي تربط المدخلات بالمخرجات. بالنسبة لمهام التصنيف، المخرج $y$ هو تسمية صنف منفصلة؛ وبالنسبة لمهام الانحدار، هو قيمة مستمرة.

تنتج خوارزمية التعلم نموذجاً من خلال تحسين دالة هدف معينة على بيانات التدريب. على سبيل المثال، في الشبكات العصبية، يتم ضبط معاملات النموذج (الأوزان والانحيازات) لتقليل دالة الخسارة مثل خسارة الإنتروبيا التبادلية للتصنيف أو متوسط الخطأ التربيعي للانحدار. ثم يتم نشر النموذج لإجراء تنبؤات على مدخلات جديدة لم يسبق رؤيتها.

التحدي الأساسي في تعلم الآلة هو ضمان أن النموذج المتعلم يعمم جيداً على بيانات جديدة. يحدث فرط الملاءمة عندما يتعلم النموذج أنماطاً خاصة ببيانات التدريب لا تعمم. تُستخدم تقنيات الانتظام، مثل انتظام L1 وL2، والإسقاط، والإيقاف المبكر، بشكل شائع لمنع فرط الملاءمة وتحسين التعميم.

## الخصوصية في تعلم الآلة

تنشأ مخاوف الخصوصية في تعلم الآلة لأن بيانات التدريب غالباً ما تحتوي على معلومات حساسة عن الأفراد. تم اقتراح عدة نهج لحماية الخصوصية في تعلم الآلة:

**الخصوصية التفاضلية.** الخصوصية التفاضلية [1، 2] هي إطار رياضي صارم للخصوصية يوفر ضمانات قوية. تحقق خوارزمية عشوائية $\mathcal{M}$ خصوصية تفاضلية $(\epsilon, \delta)$ إذا كانت لجميع مجموعات البيانات المتجاورة $D$ و$D'$ التي تختلف في سجل واحد، ولجميع المخرجات الممكنة $S$:

$$Pr[\mathcal{M}(D) \in S] \leq e^\epsilon \cdot Pr[\mathcal{M}(D') \in S] + \delta$$

تم تطبيق الخصوصية التفاضلية على تعلم الآلة من خلال تقنيات مثل إضافة ضوضاء إلى التدرجات أثناء التدريب [3، 4] أو إلى مخرجات النموذج. ومع ذلك، غالباً ما تأتي الخصوصية التفاضلية بتكلفة فائدة: يمكن للضوضاء المضافة أن تقلل من دقة النموذج.

**النهج التشفيرية.** تمكّن الحوسبة الآمنة متعددة الأطراف والتشفير المتماثل من تدريب نماذج تعلم الآلة على بيانات مشفرة دون الكشف عن البيانات الخام لأي طرف [5، 6]. بينما توفر هذه النهج ضمانات تشفيرية قوية، فإنها غالباً ما تتكبد عبئاً حسابياً كبيراً وقد لا تتوسع لنماذج أو مجموعات بيانات كبيرة.

**التعلم الموحد.** في التعلم الموحد [7]، تتعاون عدة أطراف لتدريب نموذج دون مشاركة بياناتها الخام. يقوم كل طرف بتدريب نموذج محلي على بياناته الخاصة ويشارك فقط تحديثات النموذج (مثل التدرجات) مع خادم مركزي، والذي يجمعها لتحديث نموذج عالمي. ومع ذلك، أظهرت الأعمال الحديثة أن حتى مشاركة التدرجات يمكن أن تسرب معلومات عن بيانات التدريب [8، 9].

## هجمات الخصوصية على تعلم الآلة

تمت دراسة عدة أنواع من هجمات الخصوصية على نماذج تعلم الآلة:

**هجمات انعكاس النموذج.** تهدف هجمات انعكاس النموذج [10، 11] إلى إعادة بناء بيانات التدريب أو استخراج خصائص حساسة من نموذج مدرب. على سبيل المثال، أظهر Fredrikson وآخرون [10] أنه بإعطاء اسم شخص والوصول إلى نموذج التعرف على الوجوه، يمكن للمهاجم إعادة بناء صورة لوجه ذلك الشخص. تتطلب هذه الهجمات عادةً وصول الصندوق الأبيض إلى النموذج أو معرفة تدرجات النموذج.

**هجمات استنتاج الخصائص.** تستنتج هجمات استنتاج الخصائص [12] خصائص إحصائية لمجموعة بيانات التدريب، مثل نسبة السجلات ذات سمة معينة، دون استهداف أفراد محددين.

**الأمثلة الخصامية.** الأمثلة الخصامية [13، 14] هي مدخلات مصممة للتسبب في قيام النموذج بعمل تنبؤات غير صحيحة. بينما تمت دراستها بشكل أساسي في سياق متانة النموذج، يمكن للأمثلة الخصامية أيضاً الكشف عن معلومات حول بيانات تدريب النموذج وحدود القرار.

**استنتاج العضوية.** استنتاج العضوية هو المشكلة التي نعالجها في هذا البحث. الهدف هو تحديد ما إذا كان سجل معين موجوداً في مجموعة بيانات تدريب النموذج. كانت الأعمال السابقة على استنتاج العضوية محدودة. أظهر Dwork وآخرون [15] أن النماذج ذات فرط الملاءمة يمكن أن تسرب معلومات عن سجلات التدريب الفردية. أظهر Homer وآخرون [16] هجمات استنتاج العضوية على البيانات الجينومية في دراسات الارتباط على مستوى الجينوم. ومع ذلك، لم تدرس أي أعمال سابقة بشكل منهجي هجمات استنتاج العضوية على نماذج تعلم الآلة العامة، خاصة في إعداد الصندوق الأسود.

## تعلم الآلة كخدمة

تقدم موفرو السحابة الآن تعلم الآلة كخدمة (MLaaS)، حيث يمكن للمستخدمين تحميل بيانات التدريب والحصول على نماذج مدربة، أو الاستعلام المباشر عن نماذج مدربة مسبقاً. تشمل الأمثلة Google Prediction API، وAmazon Machine Learning، وMicrosoft Azure ML، وBigML. في هذه الخدمات، يتم الوصول إلى النموذج عادةً عبر واجهة برمجة تطبيقات تسمح للمستخدمين بإرسال استعلامات وتلقي تنبؤات. لا يمكن للمستخدمين الوصول مباشرة إلى معاملات النموذج أو بيانات التدريب.

يخلق نموذج النشر هذا مخاطر خصوصية جديدة. حتى لو لم يسرّب مزود الخدمة بيانات التدريب عمداً، فإن النموذج نفسه - من خلال تنبؤاته - قد يكشف عن غير قصد معلومات عن بيانات التدريب للخصوم الذين يمكنهم الاستعلام عن النموذج.

## مساهمتنا

يختلف عملنا عن الأعمال السابقة بعدة طرق مهمة:

1. نطور هجوم استنتاج عضوية عام من نوع الصندوق الأسود يعمل على أنواع مختلفة من نماذج تعلم الآلة دون الحاجة إلى الوصول إلى معاملات النموذج أو تدرجاته.

2. نقدم تقنية التدريب الظلي لتوليد بيانات تدريب لنموذج الهجوم عندما لا يكون للخصم وصول إلى بيانات تدريب النموذج المستهدف.

3. نقدم أول تقييم شامل لهجمات استنتاج العضوية على نماذج تعلم الآلة في العالم الواقعي، بما في ذلك منصات MLaaS التجارية.

4. نحلل العوامل التي تجعل النماذج عرضة لاستنتاج العضوية ونقيّم استراتيجيات التخفيف العملية.

---

### Translation Notes

- **Key terms introduced:**
  - Supervised learning (التعلم الخاضع للإشراف)
  - Feature vector (متجه خصائص)
  - Cross-entropy loss (خسارة الإنتروبيا التبادلية)
  - Mean squared error (متوسط الخطأ التربيعي)
  - Overfitting (فرط الملاءمة)
  - Regularization (انتظام)
  - Differential privacy (خصوصية تفاضلية)
  - Neighboring datasets (مجموعات البيانات المتجاورة)
  - Federated learning (التعلم الموحد)
  - Model inversion (انعكاس النموذج)
  - Property inference (استنتاج الخصائص)
  - White-box access (وصول الصندوق الأبيض)
  - Machine learning as a service (تعلم الآلة كخدمة)

- **Equations:** 2 mathematical formulas (function notation and differential privacy definition)
- **Citations:** References [1-16] maintained in brackets
- **Special handling:** Mathematical notation preserved, formal academic terminology

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
