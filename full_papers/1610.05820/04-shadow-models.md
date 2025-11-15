# Section 4: Shadow Models
## القسم 4: النماذج الظلية

**Section:** shadow-models
**Translation Quality:** 0.87
**Glossary Terms Used:** shadow model (نموذج ظلي), shadow training (التدريب الظلي), synthetic data (بيانات اصطناعية), model architecture (معمارية النموذج), training dataset (مجموعة بيانات التدريب), hyperparameters (المعاملات الفائقة)

---

### English Version

## IV. SHADOW MODELS

The key challenge in our attack is training the attack model without access to the target model's training data. We solve this problem using shadow training: we train multiple shadow models that mimic the target model's behavior, then use these shadow models to generate labeled training data for the attack model.

### A. Shadow Training Overview

The shadow training technique works as follows:

1. **Generate synthetic training datasets:** Create multiple datasets $D_1, D_2, ..., D_k$ that are drawn from the same distribution as the target model's training data (or as close as possible).

2. **Train shadow models:** For each dataset $D_i$, train a shadow model $f_i$ using the same type of machine learning algorithm as the target model.

3. **Generate attack training data:** For each shadow model $f_i$:
   - **IN examples:** Query $f_i$ on records in $D_i$ (its training data) to get predictions labeled as "member"
   - **OUT examples:** Query $f_i$ on records not in $D_i$ to get predictions labeled as "non-member"

4. **Train attack model:** Combine the labeled examples from all shadow models to train the attack model.

The intuition is that if the shadow models are trained similarly to the target model and on similar data, they will exhibit similar overfitting patterns. The attack model learns to recognize these patterns and can then apply them to the target model.

### B. Obtaining Shadow Training Data

The effectiveness of shadow training depends on having access to data that is drawn from the same distribution as the target model's training data. We consider several scenarios:

**Scenario 1: Model-based synthesis.** If the adversary knows the statistical distribution of the target's training data, they can use statistical models to generate synthetic data. For example:
- For images, use generative models (e.g., GANs, VAEs) trained on similar images
- For structured data, use statistical sampling based on known distributions
- For text, use language models to generate synthetic text

**Scenario 2: Noisy real data.** The adversary may have access to a dataset from the same domain that is different from but similar to the target's training data. For example:
- A different hospital's patient records (for a medical model)
- Publicly available census data (for a demographic model)
- A different collection of images from the same category (for an image classifier)

**Scenario 3: Partial knowledge.** The adversary may have partial overlap with the target's training data. For example:
- Some records from the target's training set are publicly known
- The adversary has access to older versions of the training dataset
- The adversary can partially reconstruct the training data from domain knowledge

**Scenario 4: Worst-case assumption.** In the worst case, the adversary might train shadow models on completely different data and hope for transferability. Our experiments show that even with significant distribution mismatch, the attack can still succeed to some degree.

### C. Shadow Model Training

To maximize the effectiveness of shadow training, the shadow models should be as similar as possible to the target model:

**Architecture matching.** Use the same type of machine learning algorithm (e.g., neural network, decision tree, SVM). If the specific architecture is known (e.g., number of layers, layer sizes), replicate it. Otherwise, try multiple reasonable architectures.

**Training procedure.** Use similar training procedures:
- Same optimization algorithm (e.g., SGD, Adam)
- Similar learning rate schedule
- Similar number of training epochs
- Similar batch size

**Regularization.** If information is available about the target model's regularization (e.g., dropout rate, L2 penalty), match it. Otherwise, train shadow models with varying degrees of regularization to cover different possibilities.

**Ensemble of shadow models.** Training multiple shadow models with different random initializations and slightly different hyperparameters can provide more diverse examples for training the attack model, potentially improving its robustness.

### D. Number of Shadow Models

How many shadow models should we train? This involves a tradeoff:

**More shadow models:**
- **Advantage:** Provide more training data for the attack model, potentially improving its accuracy
- **Advantage:** Provide more diverse examples, improving generalization
- **Disadvantage:** Increased computational cost

**Fewer shadow models:**
- **Advantage:** Lower computational cost
- **Disadvantage:** Less training data for the attack model
- **Disadvantage:** Risk of overfitting attack model to specific shadow model behaviors

In our experiments, we found that using k = 3 to 10 shadow models provides a good balance. The marginal benefit of additional shadow models diminishes beyond this range.

### E. Data Partitioning for Shadow Models

For each shadow model, we need to partition the available data into:

1. **Shadow training set:** Used to train the shadow model (these records will be labeled "member" for attack model training)
2. **Shadow test set:** Not used for shadow model training (these records will be labeled "non-member" for attack model training)

The partitioning strategy affects the attack's effectiveness:

**Random partitioning.** Randomly split the available data into training and test sets for each shadow model. This is simple but may not reflect how the target model's training data was selected.

**Stratified partitioning.** Ensure that the class distribution in the shadow training and test sets matches the expected distribution in the target model's training data.

**Multiple partitions.** Use different random partitions for different shadow models to increase diversity in the attack training data.

### F. Attack Model Training from Shadow Models

Once we have trained k shadow models, we generate training data for the attack model:

**Per-class attack models.** For each class $c$:
- Collect all predictions from shadow models on records with true label $c$ that were in the shadow training sets (labeled "IN")
- Collect all predictions from shadow models on records with true label $c$ that were not in the shadow training sets (labeled "OUT")
- Train a binary classifier (attack model for class $c$) to distinguish "IN" from "OUT"

**Global attack model.** Alternatively, train a single attack model for all classes:
- Collect all predictions from all shadow models, labeled "IN" or "OUT"
- Train one binary classifier to work across all classes

The per-class approach typically performs better because it can learn class-specific overfitting patterns, but requires more shadow training data and is more complex.

### G. Transferability of Shadow Models

A key question is whether the attack model trained on shadow models will transfer to the target model. Transferability depends on:

1. **Data distribution similarity:** How similar is the shadow training data to the target training data?
2. **Model architecture similarity:** How similar are the shadow models to the target model?
3. **Training procedure similarity:** How similarly were the models trained?

Our experiments show that:
- The attack works best when there is high similarity in all three dimensions
- Even with moderate distribution mismatch, the attack can still be effective
- Model architecture similarity is more important than exact hyperparameter matching
- The attack is robust to some degree of uncertainty about the target model

### H. Practical Considerations

**Computational cost.** Training multiple shadow models can be computationally expensive, especially for large neural networks. However:
- Shadow models can be trained in parallel
- Smaller shadow models (with fewer parameters) can sometimes work well
- Shadow models don't need to achieve perfect accuracy, just similar overfitting behavior

**Data requirements.** The adversary needs access to data from a similar distribution. The amount of data needed depends on:
- The complexity of the data distribution
- The target model's training set size
- The desired attack accuracy

**Adaptation to target model.** If the adversary can query the target model to assess its accuracy or behavior, they can refine the shadow models to better match the target.

---

### النسخة العربية

## IV. النماذج الظلية

التحدي الرئيسي في هجومنا هو تدريب نموذج الهجوم دون الوصول إلى بيانات تدريب النموذج المستهدف. نحل هذه المشكلة باستخدام التدريب الظلي: نقوم بتدريب نماذج ظلية متعددة تحاكي سلوك النموذج المستهدف، ثم نستخدم هذه النماذج الظلية لتوليد بيانات تدريب مُسماة لنموذج الهجوم.

### أ. نظرة عامة على التدريب الظلي

تعمل تقنية التدريب الظلي على النحو التالي:

1. **توليد مجموعات بيانات تدريب اصطناعية:** إنشاء مجموعات بيانات متعددة $D_1, D_2, ..., D_k$ مسحوبة من نفس التوزيع الخاص ببيانات تدريب النموذج المستهدف (أو أقرب ما يمكن).

2. **تدريب النماذج الظلية:** لكل مجموعة بيانات $D_i$، تدريب نموذج ظلي $f_i$ باستخدام نفس نوع خوارزمية تعلم الآلة مثل النموذج المستهدف.

3. **توليد بيانات تدريب الهجوم:** لكل نموذج ظلي $f_i$:
   - **أمثلة IN:** الاستعلام عن $f_i$ على السجلات في $D_i$ (بيانات تدريبه) للحصول على تنبؤات مُسماة "عضو"
   - **أمثلة OUT:** الاستعلام عن $f_i$ على السجلات غير الموجودة في $D_i$ للحصول على تنبؤات مُسماة "غير عضو"

4. **تدريب نموذج الهجوم:** دمج الأمثلة المُسماة من جميع النماذج الظلية لتدريب نموذج الهجوم.

الحدس هو أنه إذا تم تدريب النماذج الظلية بشكل مماثل للنموذج المستهدف وعلى بيانات مماثلة، فإنها ستظهر أنماط فرط ملاءمة مماثلة. يتعلم نموذج الهجوم التعرف على هذه الأنماط ويمكنه بعد ذلك تطبيقها على النموذج المستهدف.

### ب. الحصول على بيانات التدريب الظلية

تعتمد فعالية التدريب الظلي على الوصول إلى بيانات مسحوبة من نفس التوزيع الخاص ببيانات تدريب النموذج المستهدف. نعتبر عدة سيناريوهات:

**السيناريو 1: التوليف القائم على النموذج.** إذا كان الخصم يعرف التوزيع الإحصائي لبيانات تدريب الهدف، يمكنه استخدام نماذج إحصائية لتوليد بيانات اصطناعية. على سبيل المثال:
- للصور، استخدام نماذج توليدية (مثل GANs، VAEs) مدربة على صور مماثلة
- للبيانات المنظمة، استخدام أخذ عينات إحصائية بناءً على التوزيعات المعروفة
- للنص، استخدام نماذج اللغة لتوليد نص اصطناعي

**السيناريو 2: بيانات واقعية مشوشة.** قد يكون لدى الخصم وصول إلى مجموعة بيانات من نفس المجال مختلفة عن ولكن مماثلة لبيانات تدريب الهدف. على سبيل المثال:
- سجلات مرضى مستشفى مختلف (لنموذج طبي)
- بيانات تعداد متاحة للجمهور (لنموذج ديموغرافي)
- مجموعة مختلفة من الصور من نفس الفئة (لمصنف صور)

**السيناريو 3: معرفة جزئية.** قد يكون لدى الخصم تداخل جزئي مع بيانات تدريب الهدف. على سبيل المثال:
- بعض السجلات من مجموعة تدريب الهدف معروفة علناً
- لدى الخصم وصول إلى إصدارات أقدم من مجموعة بيانات التدريب
- يمكن للخصم إعادة بناء بيانات التدريب جزئياً من المعرفة بالمجال

**السيناريو 4: افتراض أسوأ حالة.** في أسوأ الحالات، قد يدرب الخصم النماذج الظلية على بيانات مختلفة تماماً ويأمل في القابلية للنقل. تظهر تجاربنا أنه حتى مع عدم تطابق كبير في التوزيع، يمكن للهجوم أن ينجح إلى حد ما.

### ج. تدريب النماذج الظلية

لتعظيم فعالية التدريب الظلي، يجب أن تكون النماذج الظلية مشابهة قدر الإمكان للنموذج المستهدف:

**مطابقة المعمارية.** استخدام نفس نوع خوارزمية تعلم الآلة (مثل الشبكة العصبية، شجرة القرار، SVM). إذا كانت المعمارية المحددة معروفة (مثل عدد الطبقات، أحجام الطبقات)، قم بتكرارها. وإلا، جرب معماريات متعددة معقولة.

**إجراء التدريب.** استخدام إجراءات تدريب مماثلة:
- نفس خوارزمية التحسين (مثل SGD، Adam)
- جدول معدل تعلم مماثل
- عدد مماثل من حقب التدريب
- حجم دفعة مماثل

**الانتظام.** إذا كانت المعلومات متاحة حول انتظام النموذج المستهدف (مثل معدل الإسقاط، عقوبة L2)، قم بمطابقتها. وإلا، قم بتدريب النماذج الظلية بدرجات متفاوتة من الانتظام لتغطية احتمالات مختلفة.

**مجموعة من النماذج الظلية.** تدريب نماذج ظلية متعددة بتهيئات عشوائية مختلفة ومعاملات فائقة مختلفة قليلاً يمكن أن يوفر أمثلة أكثر تنوعاً لتدريب نموذج الهجوم، مما قد يحسن متانته.

### د. عدد النماذج الظلية

كم عدد النماذج الظلية التي يجب أن ندربها؟ هذا ينطوي على مفاضلة:

**المزيد من النماذج الظلية:**
- **الميزة:** توفير المزيد من بيانات التدريب لنموذج الهجوم، مما قد يحسن دقته
- **الميزة:** توفير أمثلة أكثر تنوعاً، تحسين التعميم
- **العيب:** زيادة التكلفة الحسابية

**عدد أقل من النماذج الظلية:**
- **الميزة:** تكلفة حسابية أقل
- **العيب:** بيانات تدريب أقل لنموذج الهجوم
- **العيب:** خطر فرط ملاءمة نموذج الهجوم لسلوكيات نماذج ظلية محددة

في تجاربنا، وجدنا أن استخدام k = 3 إلى 10 نماذج ظلية يوفر توازناً جيداً. تتناقص الفائدة الحدية للنماذج الظلية الإضافية بعد هذا النطاق.

### هـ. تقسيم البيانات للنماذج الظلية

لكل نموذج ظلي، نحتاج إلى تقسيم البيانات المتاحة إلى:

1. **مجموعة التدريب الظلية:** تُستخدم لتدريب النموذج الظلي (ستُسمى هذه السجلات "عضو" لتدريب نموذج الهجوم)
2. **مجموعة الاختبار الظلية:** لا تُستخدم لتدريب النموذج الظلي (ستُسمى هذه السجلات "غير عضو" لتدريب نموذج الهجوم)

تؤثر استراتيجية التقسيم على فعالية الهجوم:

**التقسيم العشوائي.** تقسيم البيانات المتاحة عشوائياً إلى مجموعات تدريب واختبار لكل نموذج ظلي. هذا بسيط ولكن قد لا يعكس كيفية اختيار بيانات تدريب النموذج المستهدف.

**التقسيم الطبقي.** التأكد من أن توزيع الصنف في مجموعات التدريب والاختبار الظلية يطابق التوزيع المتوقع في بيانات تدريب النموذج المستهدف.

**أقسام متعددة.** استخدام أقسام عشوائية مختلفة لنماذج ظلية مختلفة لزيادة التنوع في بيانات تدريب الهجوم.

### و. تدريب نموذج الهجوم من النماذج الظلية

بمجرد تدريب k نموذج ظلي، نقوم بتوليد بيانات تدريب لنموذج الهجوم:

**نماذج هجوم لكل صنف.** لكل صنف $c$:
- جمع جميع التنبؤات من النماذج الظلية على السجلات ذات التسمية الحقيقية $c$ التي كانت في مجموعات التدريب الظلية (مُسماة "IN")
- جمع جميع التنبؤات من النماذج الظلية على السجلات ذات التسمية الحقيقية $c$ التي لم تكن في مجموعات التدريب الظلية (مُسماة "OUT")
- تدريب مصنف ثنائي (نموذج هجوم للصنف $c$) للتمييز بين "IN" و"OUT"

**نموذج هجوم عام.** بدلاً من ذلك، تدريب نموذج هجوم واحد لجميع الأصناف:
- جمع جميع التنبؤات من جميع النماذج الظلية، مُسماة "IN" أو "OUT"
- تدريب مصنف ثنائي واحد للعمل عبر جميع الأصناف

يؤدي النهج لكل صنف عادةً بشكل أفضل لأنه يمكن أن يتعلم أنماط فرط ملاءمة خاصة بالصنف، ولكنه يتطلب المزيد من بيانات التدريب الظلية وأكثر تعقيداً.

### ز. قابلية نقل النماذج الظلية

السؤال الرئيسي هو ما إذا كان نموذج الهجوم المدرب على النماذج الظلية سينتقل إلى النموذج المستهدف. تعتمد القابلية للنقل على:

1. **تشابه توزيع البيانات:** ما مدى تشابه بيانات التدريب الظلية مع بيانات التدريب المستهدفة؟
2. **تشابه معمارية النموذج:** ما مدى تشابه النماذج الظلية مع النموذج المستهدف؟
3. **تشابه إجراء التدريب:** ما مدى تشابه تدريب النماذج؟

تظهر تجاربنا أن:
- يعمل الهجوم بشكل أفضل عندما يكون هناك تشابه كبير في جميع الأبعاد الثلاثة
- حتى مع عدم تطابق متوسط في التوزيع، يمكن للهجوم أن يكون فعالاً
- تشابه معمارية النموذج أكثر أهمية من المطابقة الدقيقة للمعاملات الفائقة
- الهجوم متين إلى حد ما من عدم اليقين حول النموذج المستهدف

### ح. اعتبارات عملية

**التكلفة الحسابية.** يمكن أن يكون تدريب نماذج ظلية متعددة مكلفاً حسابياً، خاصة للشبكات العصبية الكبيرة. ومع ذلك:
- يمكن تدريب النماذج الظلية بالتوازي
- النماذج الظلية الأصغر (بمعاملات أقل) يمكن أن تعمل بشكل جيد أحياناً
- لا تحتاج النماذج الظلية إلى تحقيق دقة مثالية، فقط سلوك فرط ملاءمة مماثل

**متطلبات البيانات.** يحتاج الخصم إلى الوصول إلى بيانات من توزيع مماثل. تعتمد كمية البيانات المطلوبة على:
- تعقيد توزيع البيانات
- حجم مجموعة تدريب النموذج المستهدف
- دقة الهجوم المطلوبة

**التكيف مع النموذج المستهدف.** إذا كان الخصم يمكنه الاستعلام عن النموذج المستهدف لتقييم دقته أو سلوكه، يمكنه تحسين النماذج الظلية لتطابق الهدف بشكل أفضل.

---

### Translation Notes

- **Key terms introduced:**
  - Shadow training (التدريب الظلي)
  - Shadow model (نموذج ظلي)
  - Synthetic training datasets (مجموعات بيانات تدريب اصطناعية)
  - IN examples (أمثلة IN)
  - OUT examples (أمثلة OUT)
  - Model-based synthesis (التوليف القائم على النموذج)
  - Generative models (نماذج توليدية)
  - Architecture matching (مطابقة المعمارية)
  - Training procedure (إجراء التدريب)
  - Shadow training set (مجموعة التدريب الظلية)
  - Shadow test set (مجموعة الاختبار الظلية)
  - Stratified partitioning (التقسيم الطبقي)
  - Per-class attack models (نماذج هجوم لكل صنف)
  - Global attack model (نموذج هجوم عام)
  - Transferability (قابلية النقل)

- **Equations:** Multiple mathematical notations for datasets and models
- **Figures referenced:** None explicitly mentioned
- **Subsections:** A-H structure preserved

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
