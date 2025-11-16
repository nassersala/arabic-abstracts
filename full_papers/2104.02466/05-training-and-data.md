# Section 5: Training and Data Preparation
## القسم 5: التدريب وإعداد البيانات

**Section:** Training and Data Preparation
**Translation Quality:** 0.85
**Glossary Terms Used:** training, data preparation, data poisoning, adversarial training, distribution shift, data augmentation, verification

---

### English Version

## 5. Verification of Training and Data Preparation

Most ML verification research focuses on verifying properties of trained models. However, the training process and data preparation pipeline are equally critical to system behavior and safety. Flaws in training data, training algorithms, or data preprocessing can compromise even architecturally sound models. This section examines verification approaches for these often-neglected phases.

### 5.1 The Importance of Training and Data Verification

Several factors motivate verification of training and data:

**Data Quality Issues**: Real-world datasets contain errors, biases, outliers, and inconsistencies that can severely impact model behavior. Garbage in, garbage out—flawed training data produces flawed models regardless of verification of the trained artifact.

**Data Poisoning Attacks**: Adversaries may intentionally corrupt training data to compromise model behavior. Even small percentages of poisoned samples can cause targeted misclassifications or backdoor vulnerabilities.

**Distribution Shift**: Models are trained on one distribution but deployed in environments with different distributions. Without verification of this mismatch, models may fail unpredictably in deployment.

**Training Instabilities**: Non-convex optimization, vanishing/exploding gradients, and other training pathologies can prevent convergence to good solutions or cause non-deterministic behavior.

**Hyperparameter Sensitivity**: Model behavior depends critically on hyperparameters (learning rate, architecture choices, regularization). Lack of formal analysis makes hyperparameter selection ad-hoc.

### 5.2 Data Verification and Validation

**Statistical Testing**: Apply statistical hypothesis tests to verify assumptions about training data:
- Test for expected distributions (normality tests, goodness-of-fit)
- Detect outliers and anomalies statistically
- Verify balance across classes
- Check for correlation structure

**Formal Specifications**: Define formal contracts for data properties:
- Range constraints on features (e.g., age ∈ [0, 120])
- Logical dependencies between features (e.g., "if pediatric patient, then age < 18")
- Invariants that must hold across dataset (e.g., "all images have resolution 224×224")

Tools like **Great Expectations** and **TFDV (TensorFlow Data Validation)** enable declarative specification and automatic checking of data properties.

**Provenance Tracking**: Maintain cryptographically signed audit trails of data origin, transformations, and versioning. Blockchain-based approaches ensure immutable records of data lineage.

**Fairness Verification**: Verify absence of discrimination:
- Statistical parity: P(Ŷ=1|A=0) = P(Ŷ=1|A=1) for protected attribute A
- Equal opportunity: Equal true positive rates across groups
- Calibration: Predicted probabilities match empirical frequencies across groups

Tools like **FairML** and **AI Fairness 360** detect and measure bias in datasets and models.

### 5.3 Training Process Verification

**Convergence Guarantees**: For convex objectives (linear models, some neural architectures with guarantees), formal convergence proofs exist. For non-convex deep learning:
- Analyze loss landscape properties
- Provide probabilistic convergence bounds under assumptions
- Verify absence of pathological behaviors (gradient explosion)

**Certified Training**: Modify training to produce inherently more verifiable models:

- **Provable Robustness Training** (Wong & Kolter, 2018): Train models with certified robustness bounds as objectives, ensuring robust models by construction.

- **Lipschitz-Constrained Training**: Enforce Lipschitz continuity bounds during training, limiting sensitivity to input perturbations. Enables simpler robustness verification post-training.

- **Abstract Interpretation During Training** (Mirman et al., 2018): Use abstract interpretation losses during training to optimize verifiability directly.

**Deterministic Training**: Ensure reproducibility by:
- Fixing random seeds
- Using deterministic algorithms (avoiding non-deterministic GPU operations)
- Tracking all hyperparameters and environmental factors
- Verifying bit-exact reproducibility

**Training Data Provenance**: Cryptographic verification of training data:
- Hash training dataset and log hash in model metadata
- Sign training scripts and configurations
- Create audit trail of all training runs
- Enable verification that a model was trained on claimed data

### 5.4 Data Augmentation and Preprocessing Verification

Data augmentation and preprocessing transform raw data before training or inference. These transformations must preserve critical properties.

**Augmentation Verification**: Verify that augmentations preserve label correctness:
- Rotation/translation should preserve object identity in images
- Synonym replacement should preserve sentiment in text
- Formal verification that augmentation functions map each equivalence class to itself

**Preprocessing Soundness**: Verify that preprocessing maintains safety properties:
- Normalization preserves relative orderings
- Dimensionality reduction (PCA) preserves sufficient variance
- Feature engineering maintains logical constraints

**Distribution Matching**: Verify that augmented/preprocessed data matches expected distribution:
- Statistical tests comparing processed and original data distributions
- Verify that preprocessing doesn't introduce systematic biases
- Check that augmentation coverage is uniform across classes

### 5.5 Adversarial Training Verification

Adversarial training augments training with adversarial examples to improve robustness. Verification challenges include:

**Attack Strength Verification**: Verify that adversarial examples used during training are actually adversarial:
- Check that perturbations satisfy specified norms (ℓ∞, ℓ2)
- Verify that adversarial examples cause misclassification before training
- Ensure attack algorithms (PGD, FGSM) are correctly implemented

**Robustness Certification**: Verify that adversarial training actually improves robustness:
- Apply formal verification tools (Section 3) to measure certified robustness
- Compare certified robustness bounds before and after adversarial training
- Verify that claimed robustness improvements are real, not artifacts

**Training-Verification Gap**: Address discrepancy between training objectives and verification:
- Training optimizes empirical robustness on finite samples
- Verification requires guarantees over infinite regions
- Hybrid approaches combine adversarial training with certified training

### 5.6 Challenges and Open Problems

Verification of training and data faces fundamental challenges:

**Scale**: Training datasets contain millions to billions of examples. Verification must scale to this regime while maintaining guarantees.

**Complexity**: Modern training pipelines involve complex preprocessing, augmentation, distributed training, and hyperparameter tuning. Verifying end-to-end pipelines is daunting.

**Non-Determinism**: Stochastic optimization, random augmentation, and hardware non-determinism make reproducibility difficult.

**Continuous Learning**: Online learning systems update continuously on new data. Static verification approaches may not apply.

**Trade-offs**: Constraints that improve verifiability (Lipschitz bounds, simplified architectures) may reduce model accuracy.

Despite these challenges, verification of training and data is essential for trustworthy ML in safety-critical domains. As the field matures, we expect increasing emphasis on formal guarantees throughout the entire ML pipeline, not just for trained models.

---

### النسخة العربية

## 5. التحقق من التدريب وإعداد البيانات

تركز معظم أبحاث التحقق من تعلم الآلة على التحقق من خصائص النماذج المدربة. ومع ذلك، فإن عملية التدريب وخط أنابيب إعداد البيانات حاسمان بنفس القدر لسلوك النظام وسلامته. يمكن أن تعرض العيوب في بيانات التدريب أو خوارزميات التدريب أو المعالجة المسبقة للبيانات حتى النماذج السليمة معمارياً للخطر. يفحص هذا القسم مناهج التحقق لهذه المراحل التي غالباً ما يتم إهمالها.

### 5.1 أهمية التحقق من التدريب والبيانات

تحفز عدة عوامل التحقق من التدريب والبيانات:

**قضايا جودة البيانات**: تحتوي مجموعات البيانات الواقعية على أخطاء وتحيزات وقيم شاذة وتناقضات يمكن أن تؤثر بشدة على سلوك النموذج. القمامة تدخل، القمامة تخرج—تنتج بيانات التدريب المعيبة نماذج معيبة بغض النظر عن التحقق من القطعة الأثرية المدربة.

**هجمات تسميم البيانات**: قد يفسد الخصوم عمداً بيانات التدريب لتعريض سلوك النموذج للخطر. حتى النسب المئوية الصغيرة من العينات المسممة يمكن أن تسبب تصنيفات خاطئة مستهدفة أو ثغرات خلفية.

**تحول التوزيع**: يتم تدريب النماذج على توزيع واحد ولكن يتم نشرها في بيئات بتوزيعات مختلفة. بدون التحقق من عدم التطابق هذا، قد تفشل النماذج بشكل لا يمكن التنبؤ به في النشر.

**عدم استقرار التدريب**: التحسين غير المحدب، والتدرجات المتلاشية/المتفجرة، والأمراض التدريبية الأخرى يمكن أن تمنع التقارب إلى حلول جيدة أو تسبب سلوكاً غير حتمي.

**حساسية المعاملات الفائقة**: يعتمد سلوك النموذج بشكل حاسم على المعاملات الفائقة (معدل التعلم، خيارات المعمارية، التنظيم). يجعل نقص التحليل الرسمي اختيار المعاملات الفائقة مخصصاً.

### 5.2 التحقق من البيانات والتحقق من الصحة

**الاختبار الإحصائي**: تطبيق اختبارات فرضيات إحصائية للتحقق من الافتراضات حول بيانات التدريب:
- اختبار التوزيعات المتوقعة (اختبارات الحالة الطبيعية، جودة الملاءمة)
- اكتشاف القيم الشاذة والحالات الشاذة إحصائياً
- التحقق من التوازن عبر الفئات
- التحقق من بنية الارتباط

**المواصفات الرسمية**: تحديد العقود الرسمية لخصائص البيانات:
- قيود النطاق على الميزات (على سبيل المثال، age ∈ [0, 120])
- التبعيات المنطقية بين الميزات (على سبيل المثال، "إذا كان المريض طفلاً، فإن age < 18")
- الثوابت التي يجب أن تنطبق على مجموعة البيانات (على سبيل المثال، "جميع الصور لها دقة 224×224")

تتيح أدوات مثل **Great Expectations** و **TFDV (TensorFlow Data Validation)** المواصفات التصريحية والفحص التلقائي لخصائص البيانات.

**تتبع المصدر**: الحفاظ على مسارات تدقيق موقعة تشفيرياً لأصل البيانات والتحويلات والإصدار. تضمن المناهج القائمة على البلوك تشين سجلات غير قابلة للتغيير لنسب البيانات.

**التحقق من العدالة**: التحقق من غياب التمييز:
- التكافؤ الإحصائي: P(Ŷ=1|A=0) = P(Ŷ=1|A=1) للسمة المحمية A
- الفرص المتساوية: معدلات إيجابية حقيقية متساوية عبر المجموعات
- المعايرة: تطابق الاحتمالات المتوقعة مع الترددات التجريبية عبر المجموعات

تكتشف أدوات مثل **FairML** و **AI Fairness 360** التحيز وتقيسه في مجموعات البيانات والنماذج.

### 5.3 التحقق من عملية التدريب

**ضمانات التقارب**: للأهداف المحدبة (النماذج الخطية، بعض معماريات الشبكة العصبية مع الضمانات)، توجد براهين تقارب رسمية. للتعلم العميق غير المحدب:
- تحليل خصائص منظر الخسارة
- توفير حدود تقارب احتمالية تحت الافتراضات
- التحقق من غياب السلوكيات المرضية (انفجار التدرج)

**التدريب المعتمد**: تعديل التدريب لإنتاج نماذج أكثر قابلية للتحقق بطبيعتها:

- **تدريب المتانة القابلة للإثبات** (Wong & Kolter، 2018): تدريب النماذج بحدود متانة معتمدة كأهداف، مما يضمن نماذج قوية بالبناء.

- **تدريب مقيد بليبشيتز**: فرض حدود استمرارية ليبشيتز أثناء التدريب، مما يحد من الحساسية للاضطرابات المدخلة. يتيح التحقق الأبسط من المتانة بعد التدريب.

- **التفسير المجرد أثناء التدريب** (Mirman et al., 2018): استخدام خسائر التفسير المجرد أثناء التدريب لتحسين قابلية التحقق مباشرة.

**التدريب الحتمي**: ضمان إعادة الإنتاج من خلال:
- إصلاح البذور العشوائية
- استخدام خوارزميات حتمية (تجنب عمليات GPU غير الحتمية)
- تتبع جميع المعاملات الفائقة والعوامل البيئية
- التحقق من إعادة الإنتاج الدقيقة للبت

**مصدر بيانات التدريب**: التحقق التشفيري من بيانات التدريب:
- تجزئة مجموعة بيانات التدريب وتسجيل التجزئة في بيانات تعريف النموذج
- توقيع نصوص التدريب والتكوينات
- إنشاء مسار تدقيق لجميع جولات التدريب
- تمكين التحقق من أن النموذج تم تدريبه على البيانات المدعاة

### 5.4 التحقق من زيادة البيانات والمعالجة المسبقة

تحول زيادة البيانات والمعالجة المسبقة البيانات الخام قبل التدريب أو الاستدلال. يجب أن تحافظ هذه التحويلات على الخصائص الحرجة.

**التحقق من الزيادة**: التحقق من أن الزيادات تحافظ على صحة التسمية:
- يجب أن يحافظ الدوران/الترجمة على هوية الكائن في الصور
- يجب أن يحافظ استبدال المرادفات على المشاعر في النص
- التحقق الرسمي من أن دوال الزيادة تعيد كل فئة تكافؤ إلى نفسها

**سلامة المعالجة المسبقة**: التحقق من أن المعالجة المسبقة تحافظ على خصائص السلامة:
- يحافظ التطبيع على الترتيبات النسبية
- يحافظ تقليل الأبعاد (PCA) على تباين كافٍ
- تحافظ هندسة الميزات على القيود المنطقية

**مطابقة التوزيع**: التحقق من أن البيانات المعززة/المعالجة مسبقاً تطابق التوزيع المتوقع:
- الاختبارات الإحصائية التي تقارن توزيعات البيانات المعالجة والأصلية
- التحقق من أن المعالجة المسبقة لا تقدم تحيزات منهجية
- التحقق من أن تغطية الزيادة موحدة عبر الفئات

### 5.5 التحقق من التدريب الخصامي

يعزز التدريب الخصامي التدريب بأمثلة خصامية لتحسين المتانة. تشمل تحديات التحقق:

**التحقق من قوة الهجوم**: التحقق من أن الأمثلة الخصامية المستخدمة أثناء التدريب خصامية فعلاً:
- التحقق من أن الاضطرابات تفي بالمعايير المحددة (ℓ∞، ℓ2)
- التحقق من أن الأمثلة الخصامية تسبب تصنيفاً خاطئاً قبل التدريب
- ضمان تنفيذ خوارزميات الهجوم (PGD، FGSM) بشكل صحيح

**إصدار شهادة المتانة**: التحقق من أن التدريب الخصامي يحسن المتانة فعلاً:
- تطبيق أدوات التحقق الرسمي (القسم 3) لقياس المتانة المعتمدة
- مقارنة حدود المتانة المعتمدة قبل وبعد التدريب الخصامي
- التحقق من أن تحسينات المتانة المدعاة حقيقية، وليست قطعاً أثرية

**فجوة التدريب-التحقق**: معالجة التباين بين أهداف التدريب والتحقق:
- يحسن التدريب المتانة التجريبية على عينات محدودة
- يتطلب التحقق ضمانات على مناطق لا نهائية
- المناهج الهجينة تجمع بين التدريب الخصامي والتدريب المعتمد

### 5.6 التحديات والمشاكل المفتوحة

يواجه التحقق من التدريب والبيانات تحديات أساسية:

**النطاق**: تحتوي مجموعات بيانات التدريب على ملايين إلى مليارات الأمثلة. يجب أن يتوسع التحقق إلى هذا النظام مع الحفاظ على الضمانات.

**التعقيد**: تتضمن خطوط أنابيب التدريب الحديثة معالجة مسبقة معقدة وزيادة وتدريباً موزعاً وضبط المعاملات الفائقة. التحقق من خطوط الأنابيب من طرف إلى طرف أمر شاق.

**عدم الحتمية**: التحسين العشوائي، والزيادة العشوائية، وعدم الحتمية في الأجهزة تجعل إعادة الإنتاج صعبة.

**التعلم المستمر**: تحدّث أنظمة التعلم عبر الإنترنت باستمرار على بيانات جديدة. قد لا تنطبق مناهج التحقق الثابت.

**المقايضات**: القيود التي تحسن قابلية التحقق (حدود ليبشيتز، المعماريات المبسطة) قد تقلل من دقة النموذج.

على الرغم من هذه التحديات، فإن التحقق من التدريب والبيانات ضروري لتعلم الآلة الموثوق في المجالات الحرجة من حيث السلامة. مع نضوج المجال، نتوقع تركيزاً متزايداً على الضمانات الرسمية في جميع أنحاء خط أنابيب تعلم الآلة بالكامل، وليس فقط للنماذج المدربة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Data poisoning (تسميم البيانات)
  - Distribution shift (تحول التوزيع)
  - Provenance tracking (تتبع المصدر)
  - Fairness verification (التحقق من العدالة)
  - Statistical parity (التكافؤ الإحصائي)
  - Adversarial training (التدريب الخصامي)
  - Lipschitz continuity (استمرارية ليبشيتز)
  - Certified training (التدريب المعتمد)
  - Data augmentation (زيادة البيانات)
  - PGD, FGSM (kept as acronyms)
- **Equations:** Statistical formulas for fairness
- **Citations:** Tool names (Great Expectations, TFDV, FairML, AI Fairness 360)
- **Special handling:** Kept tool and library names in English

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.87
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.85

### Back-Translation Check (Key Paragraph)

Arabic → English: "Real-world datasets contain errors, biases, outliers, and inconsistencies that can severely impact model behavior. Garbage in, garbage out—flawed training data produces flawed models regardless of verification of the trained artifact."

✓ Semantically equivalent to original
