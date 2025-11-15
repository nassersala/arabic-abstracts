# Section 5: Experimental Setup
## القسم 5: الإعداد التجريبي

**Section:** experimental-setup
**Translation Quality:** 0.86
**Glossary Terms Used:** dataset (مجموعة بيانات), classification task (مهمة تصنيف), neural network (شبكة عصبية), training (تدريب), evaluation (تقييم), machine learning as a service (تعلم الآلة كخدمة)

---

### English Version

## V. EXPERIMENTAL SETUP

We evaluate our membership inference attacks on various machine learning models and datasets. This section describes our experimental methodology, including the datasets, models, and evaluation metrics.

### A. Datasets

We use six classification datasets from different domains to evaluate the generality of our attacks:

**CIFAR-10 and CIFAR-100.** Image classification datasets containing 32x32 color images. CIFAR-10 has 10 classes (e.g., airplane, automobile, bird) with 60,000 images (50,000 training, 10,000 test). CIFAR-100 has 100 fine-grained classes with the same number of images.

**Purchase-100.** A dataset derived from Kaggle's "Acquire Valued Shoppers Challenge," containing shopping records from various online stores. We use a subset with 100 classes representing different product categories, with approximately 200,000 records.

**Texas-100.** A dataset of hospital discharge records from the Texas Department of State Health Services. It contains approximately 600,000 patient records. We use a 100-class classification task based on procedure codes. This dataset is particularly relevant for privacy because membership information is sensitive.

**Location-30.** A dataset based on location check-ins from Foursquare. We use a 30-class classification task where the goal is to predict a user's location category based on their check-in history.

**MNIST.** A handwritten digit classification dataset with 10 classes (digits 0-9), containing 70,000 grayscale images (60,000 training, 10,000 test).

### B. Target Models

We evaluate attacks against several types of machine learning models:

**Deep Neural Networks (DNNs).** We train fully connected neural networks with multiple hidden layers. For image datasets (CIFAR, MNIST), we use convolutional neural networks (CNNs). We vary the architecture depth and width to evaluate different model complexities.

**Commercial MLaaS Platforms.** We evaluate attacks on models trained using:
- **Google Prediction API:** Upload training data and obtain a trained model accessible via API
- **Amazon Machine Learning:** Similar to Google, provides classification models as a service

For the commercial platforms, we train models on Purchase-100 and Texas-100 datasets and evaluate whether our attacks can infer membership of training records.

**Other Algorithms.** We also test on:
- Logistic Regression
- Support Vector Machines (SVM)
- Decision Trees
- k-Nearest Neighbors (k-NN)

### C. Training Configuration

**Model training.** For locally trained models (DNNs), we use:
- Optimization: Stochastic Gradient Descent (SGD) or Adam optimizer
- Learning rate: Tuned per dataset (typically 0.001 to 0.1)
- Batch size: 128 or 256
- Training epochs: Until convergence or validation accuracy plateaus
- Regularization: We experiment with different levels of L2 regularization and dropout

**Data split.** For each dataset:
- 50% used to train the target model (target training set)
- 50% held out (target test set)
- For shadow models, we use different random splits of available data

### D. Shadow Model Configuration

**Number of shadow models.** We train k = 3 to 10 shadow models per experiment, depending on computational constraints and dataset size.

**Shadow data.**
- For CIFAR and MNIST: We use the same dataset but with different training/test splits
- For Purchase, Texas, Location: We partition the available data into multiple disjoint subsets
- Each shadow model is trained on a different subset

**Shadow model architecture.** We match the target model architecture as closely as possible. When attacking commercial MLaaS, we approximate the model type based on documentation and observed behavior.

### E. Attack Model Configuration

**Architecture.** The attack model is a simple neural network:
- Input: Prediction vector (length = number of classes) + optional label
- Hidden layers: 2-3 fully connected layers with 128-256 neurons each
- Activation: ReLU
- Output: Single neuron with sigmoid activation (binary classification)
- Loss: Binary cross-entropy

**Training.** We train the attack model using:
- Optimizer: Adam
- Learning rate: 0.001
- Epochs: 50-100
- Early stopping based on validation loss

### F. Evaluation Metrics

We evaluate attack performance using:

**Accuracy.** Fraction of correct predictions (member vs. non-member)

**Precision.** $\text{Precision} = \frac{TP}{TP + FP}$ where TP = true positives (correctly identified members), FP = false positives (non-members incorrectly labeled as members)

**Recall.** $\text{Recall} = \frac{TP}{TP + FN}$ where FN = false negatives (members incorrectly labeled as non-members)

**ROC curve and AUC.** Receiver Operating Characteristic curve showing the tradeoff between true positive rate and false positive rate at different thresholds. Area Under Curve (AUC) provides a single score.

**Precision-Recall curve.** Shows the tradeoff between precision and recall.

### G. Baseline Comparisons

We compare our attack against several baselines:

**Random guessing.** Randomly predict member or non-member with 50% probability each. Expected accuracy: 50%.

**Threshold-based attack.** Use a simple threshold on the model's confidence: if the model's confidence exceeds a threshold, predict "member."

**Entropy-based attack.** Compute the entropy of the prediction vector; lower entropy suggests higher confidence and potential membership.

### H. Ethical Considerations

**Data privacy.** For datasets containing potentially sensitive information (Texas-100, Location-30):
- We use publicly available or de-identified data
- We do not attempt to re-identify individuals
- Results are reported in aggregate

**Responsible disclosure.** For attacks on commercial platforms:
- We notified the vendors (Google, Amazon) of our findings before publication
- We do not disclose vulnerabilities that could enable real-world attacks
- We focus on demonstrating the privacy risks to inform better defenses

---

### النسخة العربية

## V. الإعداد التجريبي

نقيّم هجمات استنتاج العضوية الخاصة بنا على نماذج ومجموعات بيانات متنوعة لتعلم الآلة. يصف هذا القسم منهجيتنا التجريبية، بما في ذلك مجموعات البيانات، والنماذج، ومقاييس التقييم.

### أ. مجموعات البيانات

نستخدم ست مجموعات بيانات للتصنيف من مجالات مختلفة لتقييم عمومية هجماتنا:

**CIFAR-10 وCIFAR-100.** مجموعات بيانات تصنيف الصور التي تحتوي على صور ملونة بحجم 32x32. تحتوي CIFAR-10 على 10 أصناف (مثل الطائرة، السيارة، الطائر) مع 60,000 صورة (50,000 للتدريب، 10,000 للاختبار). تحتوي CIFAR-100 على 100 صنف دقيق مع نفس عدد الصور.

**Purchase-100.** مجموعة بيانات مشتقة من "Acquire Valued Shoppers Challenge" في Kaggle، تحتوي على سجلات تسوق من متاجر عبر الإنترنت مختلفة. نستخدم مجموعة فرعية بها 100 صنف يمثل فئات منتجات مختلفة، مع حوالي 200,000 سجل.

**Texas-100.** مجموعة بيانات سجلات خروج المستشفى من إدارة ولاية تكساس للخدمات الصحية. تحتوي على حوالي 600,000 سجل مريض. نستخدم مهمة تصنيف من 100 صنف بناءً على رموز الإجراءات. هذه مجموعة البيانات ذات صلة خاصة بالخصوصية لأن معلومات العضوية حساسة.

**Location-30.** مجموعة بيانات تستند إلى تسجيلات دخول الموقع من Foursquare. نستخدم مهمة تصنيف من 30 صنفاً حيث الهدف هو التنبؤ بفئة موقع المستخدم بناءً على سجل تسجيل الدخول الخاص به.

**MNIST.** مجموعة بيانات تصنيف الأرقام المكتوبة بخط اليد مع 10 أصناف (أرقام 0-9)، تحتوي على 70,000 صورة ذات تدرج رمادي (60,000 للتدريب، 10,000 للاختبار).

### ب. النماذج المستهدفة

نقيّم الهجمات ضد عدة أنواع من نماذج تعلم الآلة:

**الشبكات العصبية العميقة (DNNs).** نقوم بتدريب شبكات عصبية متصلة بالكامل مع طبقات مخفية متعددة. بالنسبة لمجموعات بيانات الصور (CIFAR، MNIST)، نستخدم الشبكات العصبية التلافيفية (CNNs). نتنوع في عمق وعرض المعمارية لتقييم تعقيدات نموذج مختلفة.

**منصات MLaaS التجارية.** نقيّم الهجمات على النماذج المدربة باستخدام:
- **Google Prediction API:** تحميل بيانات التدريب والحصول على نموذج مدرب يمكن الوصول إليه عبر واجهة برمجة التطبيقات
- **Amazon Machine Learning:** مشابه لـ Google، يوفر نماذج تصنيف كخدمة

بالنسبة للمنصات التجارية، نقوم بتدريب النماذج على مجموعات بيانات Purchase-100 وTexas-100 ونقيّم ما إذا كانت هجماتنا يمكنها استنتاج عضوية سجلات التدريب.

**خوارزميات أخرى.** نختبر أيضاً على:
- الانحدار اللوجستي
- آلات المتجهات الداعمة (SVM)
- أشجار القرار
- أقرب k جار (k-NN)

### ج. إعداد التدريب

**تدريب النموذج.** بالنسبة للنماذج المدربة محلياً (DNNs)، نستخدم:
- التحسين: الانحدار التدرجي العشوائي (SGD) أو محسن Adam
- معدل التعلم: مضبوط لكل مجموعة بيانات (عادةً 0.001 إلى 0.1)
- حجم الدفعة: 128 أو 256
- حقب التدريب: حتى التقارب أو استقرار دقة التحقق
- الانتظام: نجرب مستويات مختلفة من انتظام L2 والإسقاط

**تقسيم البيانات.** لكل مجموعة بيانات:
- 50% تُستخدم لتدريب النموذج المستهدف (مجموعة تدريب الهدف)
- 50% محتفظ بها (مجموعة اختبار الهدف)
- بالنسبة للنماذج الظلية، نستخدم تقسيمات عشوائية مختلفة من البيانات المتاحة

### د. إعداد النماذج الظلية

**عدد النماذج الظلية.** نقوم بتدريب k = 3 إلى 10 نماذج ظلية لكل تجربة، اعتماداً على القيود الحسابية وحجم مجموعة البيانات.

**بيانات الظل.**
- بالنسبة لـ CIFAR وMNIST: نستخدم نفس مجموعة البيانات ولكن مع تقسيمات تدريب/اختبار مختلفة
- بالنسبة لـ Purchase، Texas، Location: نقسم البيانات المتاحة إلى مجموعات فرعية منفصلة متعددة
- يتم تدريب كل نموذج ظلي على مجموعة فرعية مختلفة

**معمارية النموذج الظلي.** نطابق معمارية النموذج المستهدف بأقرب ما يمكن. عند مهاجمة MLaaS التجاري، نقرب نوع النموذج بناءً على التوثيق والسلوك الملحوظ.

### هـ. إعداد نموذج الهجوم

**المعمارية.** نموذج الهجوم هو شبكة عصبية بسيطة:
- المدخل: متجه التنبؤ (الطول = عدد الأصناف) + تسمية اختيارية
- الطبقات المخفية: 2-3 طبقات متصلة بالكامل مع 128-256 خلية عصبية لكل منها
- التنشيط: ReLU
- المخرج: خلية عصبية واحدة مع تنشيط سيغمويد (تصنيف ثنائي)
- الخسارة: الإنتروبيا التبادلية الثنائية

**التدريب.** نقوم بتدريب نموذج الهجوم باستخدام:
- المحسن: Adam
- معدل التعلم: 0.001
- الحقب: 50-100
- الإيقاف المبكر بناءً على خسارة التحقق

### و. مقاييس التقييم

نقيّم أداء الهجوم باستخدام:

**الصحة.** نسبة التنبؤات الصحيحة (عضو مقابل غير عضو)

**الدقة.** $\text{Precision} = \frac{TP}{TP + FP}$ حيث TP = الإيجابيات الحقيقية (الأعضاء المحددون بشكل صحيح)، FP = الإيجابيات الكاذبة (غير الأعضاء المُسمّون بشكل خاطئ كأعضاء)

**الاستدعاء.** $\text{Recall} = \frac{TP}{TP + FN}$ حيث FN = السلبيات الكاذبة (الأعضاء المُسمّون بشكل خاطئ كغير أعضاء)

**منحنى ROC وAUC.** منحنى خصائص تشغيل المستقبل الذي يظهر المفاضلة بين معدل الإيجابية الحقيقية ومعدل الإيجابية الكاذبة عند عتبات مختلفة. توفر المساحة تحت المنحنى (AUC) درجة واحدة.

**منحنى الدقة-الاستدعاء.** يظهر المفاضلة بين الدقة والاستدعاء.

### ز. مقارنات خط الأساس

نقارن هجومنا بعدة خطوط أساس:

**التخمين العشوائي.** التنبؤ عشوائياً بعضو أو غير عضو باحتمال 50% لكل منهما. الصحة المتوقعة: 50%.

**الهجوم القائم على العتبة.** استخدام عتبة بسيطة على ثقة النموذج: إذا تجاوزت ثقة النموذج عتبة، تنبأ "عضو".

**الهجوم القائم على الإنتروبيا.** حساب إنتروبيا متجه التنبؤ؛ تشير الإنتروبيا الأقل إلى ثقة أعلى وعضوية محتملة.

### ح. الاعتبارات الأخلاقية

**خصوصية البيانات.** بالنسبة لمجموعات البيانات التي تحتوي على معلومات حساسة محتملة (Texas-100، Location-30):
- نستخدم بيانات متاحة للجمهور أو مُزالة الهوية
- لا نحاول إعادة تحديد هوية الأفراد
- يتم الإبلاغ عن النتائج بشكل إجمالي

**الإفصاح المسؤول.** بالنسبة للهجمات على المنصات التجارية:
- أبلغنا البائعين (Google، Amazon) بنتائجنا قبل النشر
- لا نكشف عن نقاط الضعف التي يمكن أن تمكّن من هجمات في العالم الحقيقي
- نركز على إظهار مخاطر الخصوصية لإعلام دفاعات أفضل

---

### Translation Notes

- **Key terms introduced:**
  - Classification task (مهمة تصنيف)
  - Convolutional neural networks (الشبكات العصبية التلافيفية)
  - MLaaS platforms (منصات MLaaS)
  - Stochastic Gradient Descent (الانحدار التدرجي العشوائي)
  - Batch size (حجم الدفعة)
  - Training epochs (حقب التدريب)
  - ROC curve (منحنى ROC)
  - AUC (المساحة تحت المنحنى)
  - True positives (الإيجابيات الحقيقية)
  - False positives (الإيجابيات الكاذبة)
  - False negatives (السلبيات الكاذبة)
  - Responsible disclosure (الإفصاح المسؤول)

- **Datasets:** CIFAR-10, CIFAR-100, Purchase-100, Texas-100, Location-30, MNIST
- **Equations:** 2 formulas for precision and recall
- **Subsections:** A-H structure preserved

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
