# Section 6: Evaluation
## القسم 6: التقييم

**Section:** evaluation
**Translation Quality:** 0.87
**Glossary Terms Used:** attack (هجوم), accuracy (دقة), precision (دقة), recall (استدعاء), overfitting (فرط الملاءمة), neural network (شبكة عصبية), baseline (خط الأساس)

---

### English Version

## VI. EVALUATION

We present empirical results evaluating our membership inference attacks across different models and datasets. Our key findings are:

1. Machine learning models are vulnerable to membership inference attacks
2. Attacks achieve high precision (up to 90%) on some models and datasets
3. Even well-generalized models can leak membership information
4. Commercial MLaaS platforms are also vulnerable

### A. Overall Attack Performance

**Table 1** summarizes the attack accuracy, precision, and recall across different datasets and models.

For neural network models trained on CIFAR-100, Texas-100, and Purchase-100, our attacks achieve:
- **Accuracy:** 60-85%
- **Precision:** 70-90%
- **Recall:** 50-75%

These results significantly outperform random guessing (50% accuracy) and simple baseline attacks.

**Key observations:**
1. Attack performance is higher on models trained with less regularization (more overfitting)
2. Larger models (more parameters) tend to be more vulnerable
3. More complex datasets (higher dimensionality) show higher attack success rates

### B. Attack on Different Model Types

We evaluate attacks on various machine learning algorithms:

**Deep Neural Networks:** Most vulnerable class of models
- CIFAR-100 (CNN): 82% accuracy, 85% precision
- Texas-100 (DNN): 78% accuracy, 81% precision
- Purchase-100 (DNN): 76% accuracy, 79% precision

**Other Algorithms:**
- Logistic Regression: 65% accuracy
- SVM: 63% accuracy
- Decision Trees: 71% accuracy
- k-NN: 58% accuracy

Neural networks show the highest vulnerability, likely due to their higher capacity and tendency to memorize training data.

### C. Commercial ML Services

We successfully attack models trained on Google Prediction API and Amazon Machine Learning:

**Google Prediction API:**
- Purchase-100 dataset: 75% attack accuracy, 78% precision
- Texas-100 dataset: 73% attack accuracy, 76% precision

**Amazon Machine Learning:**
- Purchase-100 dataset: 72% attack accuracy, 74% precision
- Texas-100 dataset: 70% attack accuracy, 72% precision

These results demonstrate that real-world commercial ML services leak membership information despite their built-in privacy protections.

### D. Effect of Dataset Size

We vary the size of the training dataset and measure attack performance:

**Small training sets (1,000-5,000 records):** Higher attack accuracy (80-90%)
- Models overfit more on smaller datasets
- Each training record has a larger impact on the model

**Medium training sets (10,000-50,000 records):** Moderate attack accuracy (70-80%)

**Large training sets (>100,000 records):** Lower but still significant attack accuracy (60-70%)
- Models generalize better
- Individual records have less influence

Even with large training sets, the attack achieves accuracy well above random guessing.

### E. Label-Specific vs. Global Attack Models

Comparing two attack variants:

**Per-class (label-specific) attack models:**
- Higher precision: 75-90%
- Requires more shadow training data
- Better at exploiting class-specific overfitting patterns

**Single global attack model:**
- Moderate precision: 65-80%
- Simpler to train
- Works across all classes with one model

For high-precision attacks, per-class models are preferable. For simplicity and generality, global models are adequate.

### F. Transfer Across Datasets

We test whether attack models trained on one dataset transfer to models trained on different datasets:

**Same domain transfer (e.g., CIFAR-10 → CIFAR-100):** Moderate success (60-70% accuracy)

**Cross-domain transfer (e.g., CIFAR → Purchase):** Limited success (52-58% accuracy)

This shows that domain-specific shadow training is important for high attack accuracy, though some transfer is possible.

### G. Comparison with Baselines

Our attack significantly outperforms baseline approaches:

| Method | Accuracy | Precision |
|--------|----------|-----------|
| Random guessing | 50% | 50% |
| Threshold-based | 58% | 62% |
| Entropy-based | 64% | 68% |
| Our attack (global) | 76% | 79% |
| Our attack (per-class) | 82% | 85% |

The improvement over baselines demonstrates the effectiveness of our shadow training approach and attack model.

### H. Robustness to Shadow Model Mismatch

We evaluate how attack performance degrades when shadow models don't perfectly match the target:

**Architecture mismatch:** Using different network depths/widths in shadow models
- Mild mismatch (±20% parameters): 5-10% accuracy drop
- Severe mismatch (±50% parameters): 15-20% accuracy drop

**Regularization mismatch:** Different dropout rates or L2 penalties
- Accuracy drop: 8-15%

**Training procedure mismatch:** Different optimizers or learning rates
- Accuracy drop: 5-12%

The attack remains effective even with moderate mismatches, showing robustness to uncertainty about the target model.

### I. Case Study: Texas Hospital Dataset

The Texas-100 dataset is particularly important due to its sensitivity. Our attacks achieve:
- **Accuracy:** 78%
- **Precision:** 81%
- **Recall:** 72%

This means that for a patient whose record is in the training set, our attack correctly identifies their membership 72% of the time. For records the attack labels as members, 81% are actual members.

**Privacy implications:** Simply knowing a person's record was in a hospital's dataset reveals they were a patient, potentially exposing health conditions. This demonstrates serious real-world privacy risks.

### J. Summary of Findings

1. **Membership inference is practical:** Our attacks achieve 60-85% accuracy across diverse models and datasets

2. **Commercial services are vulnerable:** Google and Amazon ML services leak membership information

3. **Neural networks most vulnerable:** DNNs show higher vulnerability than simpler models

4. **Attack transfers moderately:** Shadow training on similar data enables effective attacks

5. **Precision-recall tradeoffs:** By adjusting thresholds, we can achieve high precision (>90%) at the cost of lower recall

---

### النسخة العربية

## VI. التقييم

نقدم نتائج تجريبية لتقييم هجمات استنتاج العضوية عبر نماذج ومجموعات بيانات مختلفة. النتائج الرئيسية لدينا هي:

1. نماذج تعلم الآلة عرضة لهجمات استنتاج العضوية
2. تحقق الهجمات دقة عالية (تصل إلى 90%) على بعض النماذج ومجموعات البيانات
3. حتى النماذج المعممة جيداً يمكن أن تسرب معلومات العضوية
4. منصات MLaaS التجارية عرضة أيضاً

### أ. أداء الهجوم الإجمالي

يلخص **الجدول 1** صحة الهجوم، والدقة، والاستدعاء عبر مجموعات بيانات ونماذج مختلفة.

بالنسبة لنماذج الشبكات العصبية المدربة على CIFAR-100، وTexas-100، وPurchase-100، تحقق هجماتنا:
- **الصحة:** 60-85%
- **الدقة:** 70-90%
- **الاستدعاء:** 50-75%

هذه النتائج تتفوق بشكل كبير على التخمين العشوائي (50% صحة) والهجمات الأساسية البسيطة.

**الملاحظات الرئيسية:**
1. أداء الهجوم أعلى على النماذج المدربة بانتظام أقل (فرط ملاءمة أكثر)
2. النماذج الأكبر (معاملات أكثر) تميل إلى أن تكون أكثر عرضة
3. مجموعات البيانات الأكثر تعقيداً (أبعاد أعلى) تظهر معدلات نجاح هجوم أعلى

### ب. الهجوم على أنواع نماذج مختلفة

نقيّم الهجمات على خوارزميات تعلم آلة مختلفة:

**الشبكات العصبية العميقة:** فئة النماذج الأكثر عرضة
- CIFAR-100 (CNN): 82% صحة، 85% دقة
- Texas-100 (DNN): 78% صحة، 81% دقة
- Purchase-100 (DNN): 76% صحة، 79% دقة

**خوارزميات أخرى:**
- الانحدار اللوجستي: 65% صحة
- SVM: 63% صحة
- أشجار القرار: 71% صحة
- k-NN: 58% صحة

تظهر الشبكات العصبية أعلى قابلية للضرر، على الأرجح بسبب قدرتها الأعلى وميلها لحفظ بيانات التدريب.

### ج. خدمات تعلم الآلة التجارية

نهاجم بنجاح النماذج المدربة على Google Prediction API وAmazon Machine Learning:

**Google Prediction API:**
- مجموعة بيانات Purchase-100: 75% صحة الهجوم، 78% دقة
- مجموعة بيانات Texas-100: 73% صحة الهجوم، 76% دقة

**Amazon Machine Learning:**
- مجموعة بيانات Purchase-100: 72% صحة الهجوم، 74% دقة
- مجموعة بيانات Texas-100: 70% صحة الهجوم، 72% دقة

توضح هذه النتائج أن خدمات تعلم الآلة التجارية في العالم الحقيقي تسرب معلومات العضوية على الرغم من حمايات الخصوصية المدمجة فيها.

### د. تأثير حجم مجموعة البيانات

نتنوع في حجم مجموعة بيانات التدريب ونقيس أداء الهجوم:

**مجموعات تدريب صغيرة (1,000-5,000 سجل):** صحة هجوم أعلى (80-90%)
- تعاني النماذج من فرط ملاءمة أكثر على مجموعات بيانات أصغر
- لكل سجل تدريب تأثير أكبر على النموذج

**مجموعات تدريب متوسطة (10,000-50,000 سجل):** صحة هجوم معتدلة (70-80%)

**مجموعات تدريب كبيرة (>100,000 سجل):** صحة هجوم أقل ولكنها لا تزال كبيرة (60-70%)
- تعمم النماذج بشكل أفضل
- السجلات الفردية لها تأثير أقل

حتى مع مجموعات تدريب كبيرة، يحقق الهجوم صحة أعلى بكثير من التخمين العشوائي.

### هـ. نماذج الهجوم الخاصة بالتسمية مقابل العامة

مقارنة متغيرين من الهجوم:

**نماذج هجوم لكل صنف (خاصة بالتسمية):**
- دقة أعلى: 75-90%
- تتطلب المزيد من بيانات التدريب الظلية
- أفضل في استغلال أنماط فرط الملاءمة الخاصة بالصنف

**نموذج هجوم عام واحد:**
- دقة معتدلة: 65-80%
- أبسط في التدريب
- يعمل عبر جميع الأصناف مع نموذج واحد

للهجمات عالية الدقة، نماذج كل صنف أفضل. للبساطة والعمومية، النماذج العامة كافية.

### و. النقل عبر مجموعات البيانات

نختبر ما إذا كانت نماذج الهجوم المدربة على مجموعة بيانات واحدة تنتقل إلى نماذج مدربة على مجموعات بيانات مختلفة:

**النقل في نفس المجال (مثل CIFAR-10 → CIFAR-100):** نجاح معتدل (60-70% صحة)

**النقل عبر المجالات (مثل CIFAR → Purchase):** نجاح محدود (52-58% صحة)

هذا يظهر أن التدريب الظلي الخاص بالمجال مهم لصحة هجوم عالية، على الرغم من أن بعض النقل ممكن.

### ز. المقارنة مع خطوط الأساس

يتفوق هجومنا بشكل كبير على النهج الأساسية:

| الطريقة | الصحة | الدقة |
|---------|-------|-------|
| التخمين العشوائي | 50% | 50% |
| القائم على العتبة | 58% | 62% |
| القائم على الإنتروبيا | 64% | 68% |
| هجومنا (عام) | 76% | 79% |
| هجومنا (لكل صنف) | 82% | 85% |

يوضح التحسن على خطوط الأساس فعالية نهج التدريب الظلي ونموذج الهجوم.

### ح. المتانة أمام عدم تطابق النموذج الظلي

نقيّم كيف يتدهور أداء الهجوم عندما لا تطابق النماذج الظلية الهدف بشكل مثالي:

**عدم تطابق المعمارية:** استخدام أعماق/عروض شبكة مختلفة في النماذج الظلية
- عدم تطابق خفيف (±20% معاملات): انخفاض صحة 5-10%
- عدم تطابق شديد (±50% معاملات): انخفاض صحة 15-20%

**عدم تطابق الانتظام:** معدلات إسقاط مختلفة أو عقوبات L2
- انخفاض الصحة: 8-15%

**عدم تطابق إجراء التدريب:** محسنات أو معدلات تعلم مختلفة
- انخفاض الصحة: 5-12%

يظل الهجوم فعالاً حتى مع عدم تطابقات معتدلة، مما يظهر المتانة أمام عدم اليقين حول النموذج المستهدف.

### ط. دراسة حالة: مجموعة بيانات مستشفى تكساس

مجموعة بيانات Texas-100 مهمة بشكل خاص بسبب حساسيتها. تحقق هجماتنا:
- **الصحة:** 78%
- **الدقة:** 81%
- **الاستدعاء:** 72%

هذا يعني أنه بالنسبة لمريض يكون سجله في مجموعة التدريب، يحدد هجومنا بشكل صحيح عضويته 72% من الوقت. بالنسبة للسجلات التي يسميها الهجوم كأعضاء، 81% هم أعضاء فعليون.

**آثار الخصوصية:** مجرد معرفة أن سجل شخص كان في مجموعة بيانات مستشفى يكشف أنه كان مريضاً، مما قد يكشف عن حالات صحية. هذا يوضح مخاطر خصوصية جدية في العالم الحقيقي.

### ي. ملخص النتائج

1. **استنتاج العضوية عملي:** تحقق هجماتنا صحة 60-85% عبر نماذج ومجموعات بيانات متنوعة

2. **الخدمات التجارية عرضة:** خدمات تعلم الآلة من Google وAmazon تسرب معلومات العضوية

3. **الشبكات العصبية الأكثر عرضة:** تظهر DNNs قابلية ضرر أعلى من النماذج الأبسط

4. **الهجوم ينتقل بشكل معتدل:** التدريب الظلي على بيانات مماثلة يمكّن من هجمات فعالة

5. **مفاضلات الدقة-الاستدعاء:** من خلال ضبط العتبات، يمكننا تحقيق دقة عالية (>90%) على حساب استدعاء أقل

---

### Translation Notes

- **Key terms introduced:**
  - Attack performance (أداء الهجوم)
  - Attack accuracy (صحة الهجوم)
  - Per-class attack models (نماذج هجوم لكل صنف)
  - Global attack model (نموذج هجوم عام)
  - Transfer across datasets (النقل عبر مجموعات البيانات)
  - Architecture mismatch (عدم تطابق المعمارية)
  - Case study (دراسة حالة)

- **Tables:** 1 comparison table included
- **Subsections:** A-J structure preserved
- **Special handling:** Maintained percentage values and numerical data

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
