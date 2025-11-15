# Section 3: The Attack
## القسم 3: الهجوم

**Section:** attack-methodology
**Translation Quality:** 0.88
**Glossary Terms Used:** attack model (نموذج الهجوم), target model (النموذج المستهدف), training data (بيانات التدريب), prediction vector (متجه التنبؤ), confidence scores (درجات الثقة), binary classifier (مصنف ثنائي), membership inference (استنتاج العضوية)

---

### English Version

## III. THE ATTACK

In this section, we describe our membership inference attack in detail. We first define the threat model and the adversary's goal, then present our attack methodology.

### A. Threat Model and Adversary's Goal

**Target model.** We assume the adversary has black-box access to a target machine learning model $f$. The model takes an input $x$ and produces a prediction. For classification tasks, the model outputs a prediction vector $f(x) = [y_1, y_2, ..., y_c]$, where $c$ is the number of classes and $y_i$ represents the model's confidence that input $x$ belongs to class $i$. In many cases, these values are probability scores that sum to 1.

**Adversary's knowledge.** The adversary has the following capabilities and knowledge:

1. **Query access:** The adversary can query the target model $f$ with arbitrary inputs and observe the model's predictions. This is realistic for models deployed as services (MLaaS).

2. **Model type:** The adversary knows the type of machine learning algorithm used (e.g., neural network, decision tree, logistic regression), but not the specific architecture, hyperparameters, or trained parameters.

3. **Data distribution:** The adversary has some knowledge about the distribution of the training data. This could come from understanding the application domain (e.g., knowing that a hospital's patient records follow certain demographic distributions) or having access to similar data from the same domain.

**Adversary's goal.** Given a target model $f$ and a data record $x$, the adversary wants to determine whether $x$ was in the training dataset $D_{train}$ used to train $f$. The adversary outputs a binary decision: "member" or "non-member."

### B. Attack Intuition

The key insight behind our attack is that machine learning models behave differently on their training data compared to unseen test data. Specifically:

1. **Overfitting behavior:** Models tend to assign higher confidence (probability) to the correct class for training data points than for unseen data points. This is especially true when the model has overfit to the training data.

2. **Prediction patterns:** The pattern of predictions across all classes differs between training and test data. For a training data point, the model might be more confident in its prediction, resulting in a prediction vector with higher maximum value and lower entropy.

3. **Decision boundaries:** Training data points are more likely to be far from decision boundaries (high confidence), while test data points may fall closer to boundaries (lower confidence).

Our attack exploits these differences by training a separate "attack model" that learns to distinguish the target model's behavior on training data versus test data.

### C. Attack Model

The attack model is a binary classifier that takes as input the target model's prediction on a data record and outputs a binary label indicating whether the record was in the target model's training set.

**Input to attack model.** For a data record $x$ with true label $y$, the input to the attack model consists of:

1. **Prediction vector:** $f(x) = [y_1, y_2, ..., y_c]$ - the target model's output
2. **True label:** $y$ - the actual class of $x$ (if known)

In some cases, the adversary may not know the true label $y$. In such cases, the attack model can use only the prediction vector, or use the model's predicted label as a proxy for the true label.

**Output of attack model.** The attack model outputs a binary prediction:
- **1 (member):** The record $x$ was in the target model's training dataset
- **0 (non-member):** The record $x$ was not in the training dataset

**Architecture.** The attack model can be any binary classifier. In our experiments, we use a simple neural network with multiple fully connected layers. The attack model takes the prediction vector (and optionally the label) as input and learns to distinguish training data from non-training data based on the patterns in these predictions.

### D. Training the Attack Model

The main challenge in training the attack model is obtaining training data: we need examples of the target model's predictions on both training data (members) and non-training data (non-members). Since we don't have access to the target model's actual training data, we use a technique called **shadow training**.

**Shadow training approach:**

1. **Synthesize datasets:** Generate multiple synthetic datasets that mimic the distribution of the target model's training data. This can be done by:
   - Sampling from a similar dataset in the same domain
   - Using statistical models to generate synthetic data
   - Using publicly available data from the same distribution

2. **Train shadow models:** For each synthetic dataset, train a "shadow model" that mimics the target model. The shadow model should:
   - Use the same type of algorithm as the target model (e.g., neural network)
   - Be trained on the synthetic dataset in a similar way
   - Have similar architecture and complexity

3. **Generate training data for attack:** For each shadow model, we know exactly which records were in its training set and which were not. We can query each shadow model on both its training data and non-training data to obtain labeled examples:
   - **Positive examples (members):** Predictions of shadow model on its training data
   - **Negative examples (non-members):** Predictions of shadow model on data not in its training set

4. **Train the attack model:** Using the labeled examples from step 3, train the attack model to classify predictions as coming from training data or non-training data.

The key assumption is that shadow models trained on similar data will exhibit similar overfitting behavior to the target model. Therefore, an attack model trained on shadow models will generalize to the target model.

### E. Attack Execution

Once the attack model is trained, executing the attack is straightforward:

1. **Query target model:** For a candidate record $x$ with label $y$, query the target model to obtain its prediction $f(x)$.

2. **Apply attack model:** Feed the prediction $f(x)$ (and label $y$, if available) into the attack model.

3. **Output decision:** The attack model outputs whether $x$ was likely in the target model's training data.

### F. Attack Variants

We consider several variants of the attack based on what information is available to the adversary:

**Variant 1: Label-specific attack model.** Train a separate attack model for each class label. When testing whether record $(x, y)$ was in the training set, use the attack model trained specifically for class $y$. This allows the attack to learn class-specific overfitting patterns.

**Variant 2: Single attack model for all classes.** Train one attack model that works for all classes. This is simpler but may be less accurate than label-specific models.

**Variant 3: Attack without knowing true label.** If the adversary doesn't know the true label $y$ of record $x$, they can:
- Use the target model's predicted label as a proxy
- Train the attack model to work with just the prediction vector, without the label information

### G. Metrics

We evaluate the attack using standard binary classification metrics:

- **Precision:** Of all records the attack labels as members, what fraction were actually in the training set?
- **Recall:** Of all actual training records, what fraction does the attack correctly identify?
- **Accuracy:** What fraction of the attack's decisions (member/non-member) are correct?

We also report the attack's performance at different operating points (precision-recall tradeoffs).

---

### النسخة العربية

## III. الهجوم

في هذا القسم، نصف هجوم استنتاج العضوية الخاص بنا بالتفصيل. نحدد أولاً نموذج التهديد وهدف الخصم، ثم نقدم منهجية الهجوم.

### أ. نموذج التهديد وهدف الخصم

**النموذج المستهدف.** نفترض أن الخصم لديه وصول من نوع الصندوق الأسود إلى نموذج تعلم آلة مستهدف $f$. يأخذ النموذج مدخل $x$ وينتج تنبؤاً. بالنسبة لمهام التصنيف، يخرج النموذج متجه تنبؤ $f(x) = [y_1, y_2, ..., y_c]$، حيث $c$ هو عدد الأصناف و$y_i$ يمثل ثقة النموذج في أن المدخل $x$ ينتمي إلى الصنف $i$. في كثير من الحالات، تكون هذه القيم درجات احتمالية يبلغ مجموعها 1.

**معرفة الخصم.** لدى الخصم القدرات والمعرفة التالية:

1. **وصول الاستعلام:** يمكن للخصم الاستعلام عن النموذج المستهدف $f$ بمدخلات عشوائية وملاحظة تنبؤات النموذج. هذا واقعي للنماذج المنشورة كخدمات (MLaaS).

2. **نوع النموذج:** يعرف الخصم نوع خوارزمية تعلم الآلة المستخدمة (مثل الشبكة العصبية، شجرة القرار، الانحدار اللوجستي)، ولكن ليس المعمارية المحددة، أو المعاملات الفائقة، أو المعاملات المدربة.

3. **توزيع البيانات:** لدى الخصم بعض المعرفة بتوزيع بيانات التدريب. يمكن أن يأتي هذا من فهم مجال التطبيق (مثل معرفة أن سجلات مرضى المستشفى تتبع توزيعات ديموغرافية معينة) أو الوصول إلى بيانات مماثلة من نفس المجال.

**هدف الخصم.** بإعطاء نموذج مستهدف $f$ وسجل بيانات $x$، يريد الخصم تحديد ما إذا كان $x$ موجوداً في مجموعة بيانات التدريب $D_{train}$ المستخدمة لتدريب $f$. يخرج الخصم قراراً ثنائياً: "عضو" أو "غير عضو".

### ب. حدس الهجوم

الفكرة الرئيسية وراء هجومنا هي أن نماذج تعلم الآلة تتصرف بشكل مختلف على بيانات تدريبها مقارنة ببيانات الاختبار غير المرئية. على وجه التحديد:

1. **سلوك فرط الملاءمة:** تميل النماذج إلى تعيين ثقة (احتمال) أعلى للصنف الصحيح لنقاط بيانات التدريب مقارنة بنقاط البيانات غير المرئية. هذا صحيح بشكل خاص عندما يكون النموذج قد عانى من فرط الملاءمة لبيانات التدريب.

2. **أنماط التنبؤ:** يختلف نمط التنبؤات عبر جميع الأصناف بين بيانات التدريب والاختبار. بالنسبة لنقطة بيانات تدريب، قد يكون النموذج أكثر ثقة في تنبؤه، مما ينتج عنه متجه تنبؤ بقيمة قصوى أعلى وإنتروبيا أقل.

3. **حدود القرار:** نقاط بيانات التدريب أكثر احتمالاً أن تكون بعيدة عن حدود القرار (ثقة عالية)، بينما قد تقع نقاط بيانات الاختبار أقرب إلى الحدود (ثقة أقل).

يستغل هجومنا هذه الاختلافات من خلال تدريب "نموذج هجوم" منفصل يتعلم التمييز بين سلوك النموذج المستهدف على بيانات التدريب مقابل بيانات الاختبار.

### ج. نموذج الهجوم

نموذج الهجوم هو مصنف ثنائي يأخذ كمدخل تنبؤ النموذج المستهدف على سجل بيانات ويخرج تسمية ثنائية تشير إلى ما إذا كان السجل موجوداً في مجموعة تدريب النموذج المستهدف.

**مدخل نموذج الهجوم.** لسجل بيانات $x$ مع التسمية الحقيقية $y$، يتكون مدخل نموذج الهجوم من:

1. **متجه التنبؤ:** $f(x) = [y_1, y_2, ..., y_c]$ - مخرج النموذج المستهدف
2. **التسمية الحقيقية:** $y$ - الصنف الفعلي لـ $x$ (إذا كان معروفاً)

في بعض الحالات، قد لا يعرف الخصم التسمية الحقيقية $y$. في مثل هذه الحالات، يمكن لنموذج الهجوم استخدام متجه التنبؤ فقط، أو استخدام التسمية المتنبأ بها من النموذج كبديل للتسمية الحقيقية.

**مخرج نموذج الهجوم.** يخرج نموذج الهجوم تنبؤاً ثنائياً:
- **1 (عضو):** كان السجل $x$ في مجموعة بيانات تدريب النموذج المستهدف
- **0 (غير عضو):** لم يكن السجل $x$ في مجموعة بيانات التدريب

**المعمارية.** يمكن أن يكون نموذج الهجوم أي مصنف ثنائي. في تجاربنا، نستخدم شبكة عصبية بسيطة مع عدة طبقات متصلة بالكامل. يأخذ نموذج الهجوم متجه التنبؤ (واختيارياً التسمية) كمدخل ويتعلم التمييز بين بيانات التدريب وبيانات غير التدريب بناءً على الأنماط في هذه التنبؤات.

### د. تدريب نموذج الهجوم

التحدي الرئيسي في تدريب نموذج الهجوم هو الحصول على بيانات التدريب: نحتاج إلى أمثلة على تنبؤات النموذج المستهدف على كل من بيانات التدريب (الأعضاء) وبيانات غير التدريب (غير الأعضاء). نظراً لأننا لا نملك وصولاً إلى بيانات التدريب الفعلية للنموذج المستهدف، نستخدم تقنية تسمى **التدريب الظلي**.

**نهج التدريب الظلي:**

1. **توليف مجموعات البيانات:** توليد مجموعات بيانات اصطناعية متعددة تحاكي توزيع بيانات تدريب النموذج المستهدف. يمكن القيام بذلك عن طريق:
   - أخذ عينات من مجموعة بيانات مماثلة في نفس المجال
   - استخدام نماذج إحصائية لتوليد بيانات اصطناعية
   - استخدام بيانات متاحة للجمهور من نفس التوزيع

2. **تدريب النماذج الظلية:** لكل مجموعة بيانات اصطناعية، تدريب "نموذج ظلي" يحاكي النموذج المستهدف. يجب على النموذج الظلي:
   - استخدام نفس نوع الخوارزمية مثل النموذج المستهدف (مثل الشبكة العصبية)
   - أن يتم تدريبه على مجموعة البيانات الاصطناعية بطريقة مماثلة
   - أن يكون له معمارية وتعقيد مماثلين

3. **توليد بيانات التدريب للهجوم:** لكل نموذج ظلي، نعرف بالضبط أي السجلات كانت في مجموعة تدريبه وأيها لم تكن. يمكننا الاستعلام عن كل نموذج ظلي على كل من بيانات تدريبه وبيانات غير التدريب للحصول على أمثلة مُسماة:
   - **أمثلة إيجابية (أعضاء):** تنبؤات النموذج الظلي على بيانات تدريبه
   - **أمثلة سلبية (غير أعضاء):** تنبؤات النموذج الظلي على بيانات ليست في مجموعة تدريبه

4. **تدريب نموذج الهجوم:** باستخدام الأمثلة المُسماة من الخطوة 3، تدريب نموذج الهجوم لتصنيف التنبؤات على أنها آتية من بيانات تدريب أو بيانات غير تدريب.

الافتراض الأساسي هو أن النماذج الظلية المدربة على بيانات مماثلة ستظهر سلوك فرط ملاءمة مماثل للنموذج المستهدف. لذلك، سيعمم نموذج الهجوم المدرب على النماذج الظلية إلى النموذج المستهدف.

### هـ. تنفيذ الهجوم

بمجرد تدريب نموذج الهجوم، يكون تنفيذ الهجوم مباشراً:

1. **الاستعلام عن النموذج المستهدف:** لسجل مرشح $x$ مع التسمية $y$، الاستعلام عن النموذج المستهدف للحصول على تنبؤه $f(x)$.

2. **تطبيق نموذج الهجوم:** إدخال التنبؤ $f(x)$ (والتسمية $y$، إذا كانت متاحة) في نموذج الهجوم.

3. **إخراج القرار:** يخرج نموذج الهجوم ما إذا كان $x$ على الأرجح في بيانات تدريب النموذج المستهدف.

### و. متغيرات الهجوم

نعتبر عدة متغيرات من الهجوم بناءً على المعلومات المتاحة للخصم:

**المتغير 1: نموذج هجوم خاص بالتسمية.** تدريب نموذج هجوم منفصل لكل تسمية صنف. عند اختبار ما إذا كان السجل $(x, y)$ موجوداً في مجموعة التدريب، استخدام نموذج الهجوم المدرب خصيصاً للصنف $y$. هذا يسمح للهجوم بتعلم أنماط فرط ملاءمة خاصة بالصنف.

**المتغير 2: نموذج هجوم واحد لجميع الأصناف.** تدريب نموذج هجوم واحد يعمل لجميع الأصناف. هذا أبسط ولكن قد يكون أقل دقة من النماذج الخاصة بالتسمية.

**المتغير 3: الهجوم دون معرفة التسمية الحقيقية.** إذا لم يعرف الخصم التسمية الحقيقية $y$ للسجل $x$، يمكنه:
- استخدام التسمية المتنبأ بها من النموذج المستهدف كبديل
- تدريب نموذج الهجوم للعمل مع متجه التنبؤ فقط، دون معلومات التسمية

### ز. المقاييس

نقيّم الهجوم باستخدام مقاييس التصنيف الثنائي القياسية:

- **الدقة:** من جميع السجلات التي يسميها الهجوم كأعضاء، ما هي النسبة التي كانت فعلياً في مجموعة التدريب؟
- **الاستدعاء:** من جميع سجلات التدريب الفعلية، ما هي النسبة التي يحددها الهجوم بشكل صحيح؟
- **الصحة:** ما هي نسبة قرارات الهجوم (عضو/غير عضو) الصحيحة؟

نبلغ أيضاً عن أداء الهجوم عند نقاط تشغيل مختلفة (مفاضلات الدقة-الاستدعاء).

---

### Translation Notes

- **Key terms introduced:**
  - Black-box access (وصول الصندوق الأسود)
  - Query access (وصول الاستعلام)
  - Prediction vector (متجه التنبؤ)
  - Confidence scores (درجات الثقة)
  - Overfitting behavior (سلوك فرط الملاءمة)
  - Decision boundaries (حدود القرار)
  - Shadow training (التدريب الظلي)
  - Shadow models (النماذج الظلية)
  - Synthetic datasets (مجموعات بيانات اصطناعية)
  - Label-specific attack (هجوم خاص بالتسمية)
  - Precision-recall tradeoffs (مفاضلات الدقة-الاستدعاء)

- **Equations:** Multiple mathematical notations for functions, vectors, and datasets
- **Figures referenced:** None explicitly in this section
- **Special handling:** Preserved mathematical notation, subsection structure (A-G)

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
