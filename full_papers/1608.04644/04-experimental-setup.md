# Section 4: Experimental Setup
## القسم 4: الإعداد التجريبي

**Section:** experimental-setup
**Translation Quality:** 0.88
**Glossary Terms Used:** neural network (شبكة عصبية), accuracy (دقة), validation (تحقق), overfitting (إفراط في التلاؤم), training (تدريب), architecture (معمارية)

---

### English Version

The paper evaluates on three datasets:

**MNIST**: 99.5% accuracy achieved

**CIFAR-10**: 80% accuracy (matching original distillation work)

**ImageNet**: Pre-trained Inception v3 with 96% top-5 accuracy

Model architectures reproduce original distillation research exactly. CIFAR-10 models overfit significantly (98% training accuracy, 80% validation), matching the original work's configuration without augmentation or additional regularization.

---

### النسخة العربية

يقيّم البحث على ثلاث مجموعات بيانات:

**MNIST**: تم تحقيق دقة 99.5%

**CIFAR-10**: دقة 80% (مطابقة للعمل الأصلي للتقطير)

**ImageNet**: Inception v3 مدرب مسبقاً بدقة 96% في أفضل 5 تصنيفات

تعيد معماريات النموذج إنتاج بحث التقطير الأصلي بدقة. تفرط نماذج CIFAR-10 في التلاؤم بشكل كبير (دقة تدريب 98%، دقة تحقق 80%)، مطابقة لتكوين العمل الأصلي بدون تعزيز البيانات أو تنظيم إضافي.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Top-5 accuracy (دقة أفضل 5)
  - Pre-trained (مدرب مسبقاً)
  - Data augmentation (تعزيز البيانات)
  - Regularization (تنظيم)

- **Equations:** None
- **Citations:** Reference to original distillation work
- **Special handling:**
  - Dataset names (MNIST, CIFAR-10, ImageNet) kept in English as standard
  - Model name (Inception v3) kept in English
  - Accuracy percentages preserved exactly
  - Note on overfitting is important context for understanding attack success

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.89
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88

**Notes:** This short section establishes the experimental benchmarks. The translation maintains precision in reporting accuracy numbers and model configurations. The overfitting detail is important as it affects adversarial vulnerability.
