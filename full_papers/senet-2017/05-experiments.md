# Section 5: Experiments
## القسم 5: التجارب

**Section:** experiments
**Translation Quality:** 0.87
**Glossary Terms Used:** dataset, architecture, deep learning, convolutional neural network, top-1 error, top-5 error, training, validation, data augmentation, benchmark, GFLOPs

---

### English Version

#### 5.1 Image Classification

**ImageNet Dataset:**
The researchers trained models on ImageNet 2012, which contains "1.28 million training images and 50K validation images from 1000 different classes." They evaluated performance using top-1 and top-5 error metrics.

**Training Configuration:**
Models underwent "data augmentation with random cropping...to a size of 224×224 pixels" with "random horizontal flipping." The team employed "synchronous SGD with momentum 0.9 and a minibatch size of 1024," training for "100 epochs" with an initial learning rate of 0.6, reduced by 10x every 30 epochs.

**Key Results - ResNet Architectures:**

| Architecture | Top-1 Error | Top-5 Error | GFLOPs |
|---|---|---|---|
| ResNet-50 | 24.80% | 7.48% | 3.86 |
| SE-ResNet-50 | 23.29% | 6.62% | 3.87 |
| ResNet-101 | 23.17% | 6.52% | 7.58 |
| SE-ResNet-101 | 22.38% | 6.07% | 7.60 |

Notably, "SE-ResNet-50 achieves a single-crop top-5 validation error of 6.62%, exceeding ResNet-50 (7.48%) by 0.86%."

**Modern Architectures:**
SE blocks enhanced Inception-ResNet-v2 and ResNeXt designs. SE-ResNeXt-50 reached "5.49% top-5 error," outperforming the deeper ResNeXt-101 baseline.

**Mobile Networks:**
Testing MobileNet and ShuffleNet showed consistent improvements. SE-MobileNet achieved "25.3% top-1 error" versus the baseline's 28.4%, representing a "3.1% improvement."

#### 5.2 CIFAR Datasets

Experiments on CIFAR-10 and CIFAR-100 demonstrated universal benefits:

**CIFAR-10 Results:**
- Shake-Shake 26 2x96d + Cutout: 2.56% → 2.12% error
- WideResNet-16-8: 4.27% → 3.88% error

**CIFAR-100 Results:**
- ResNet-164: 24.33% → 21.31% error
- WideResNet-16-8: 20.43% → 19.14% error

#### 5.3 Beyond ImageNet

**Places365 Scene Classification:**
SE-ResNet-152 achieved "11.01% top-5 error," surpassing the previous benchmark of 11.48%.

**Object Detection (COCO):**
SE-ResNet-50 in Faster R-CNN improved "AP from 38.0 to 40.4," representing a 6.3% relative gain.

#### 5.4 ILSVRC 2017 Competition

The team's ensemble achieved first place with "2.251% top-5 error on the test set," approximately "25% relative improvement" over 2016's winning entry.

SENet-154 delivered "top-1 error of 18.68% and top-5 error of 4.47%" using standard evaluation protocols.

---

### النسخة العربية

#### 5.1 تصنيف الصور

**مجموعة بيانات ImageNet:**
دَرّب الباحثون النماذج على ImageNet 2012، التي تحتوي على "1.28 مليون صورة تدريبية و 50 ألف صورة تحقق من 1000 فئة مختلفة". قيّموا الأداء باستخدام مقاييس خطأ أعلى-1 وأعلى-5.

**إعدادات التدريب:**
خضعت النماذج "لزيادة البيانات مع القص العشوائي... إلى حجم 224×224 بكسل" مع "الانعكاس الأفقي العشوائي". استخدم الفريق "SGD المتزامن مع زخم 0.9 وحجم دفعة صغيرة 1024"، مع التدريب لـ "100 حقبة" بمعدل تعلم أولي 0.6، يُخفّض بمقدار 10x كل 30 حقبة.

**النتائج الرئيسية - معماريات ResNet:**

| المعمارية | خطأ أعلى-1 | خطأ أعلى-5 | GFLOPs |
|---|---|---|---|
| ResNet-50 | 24.80% | 7.48% | 3.86 |
| SE-ResNet-50 | 23.29% | 6.62% | 3.87 |
| ResNet-101 | 23.17% | 6.52% | 7.58 |
| SE-ResNet-101 | 22.38% | 6.07% | 7.60 |

والجدير بالذكر أن "SE-ResNet-50 يحقق خطأ تحقق أعلى-5 بقطع واحد يبلغ 6.62٪، متفوقاً على ResNet-50 (7.48٪) بنسبة 0.86٪".

**المعماريات الحديثة:**
عززت كتل SE تصاميم Inception-ResNet-v2 و ResNeXt. وصل SE-ResNeXt-50 إلى "خطأ أعلى-5 بنسبة 5.49٪"، متفوقاً على ResNeXt-101 الأساسي الأعمق.

**الشبكات المحمولة:**
أظهر اختبار MobileNet و ShuffleNet تحسينات متسقة. حقق SE-MobileNet "خطأ أعلى-1 بنسبة 25.3٪" مقابل 28.4٪ للأساس، مما يمثل "تحسيناً بنسبة 3.1٪".

#### 5.2 مجموعات بيانات CIFAR

أظهرت التجارب على CIFAR-10 و CIFAR-100 فوائد شاملة:

**نتائج CIFAR-10:**
- Shake-Shake 26 2x96d + Cutout: 2.56٪ ← 2.12٪ خطأ
- WideResNet-16-8: 4.27٪ ← 3.88٪ خطأ

**نتائج CIFAR-100:**
- ResNet-164: 24.33٪ ← 21.31٪ خطأ
- WideResNet-16-8: 20.43٪ ← 19.14٪ خطأ

#### 5.3 ما وراء ImageNet

**تصنيف المشاهد Places365:**
حقق SE-ResNet-152 "خطأ أعلى-5 بنسبة 11.01٪"، متفوقاً على المعيار السابق البالغ 11.48٪.

**كشف الأجسام (COCO):**
حسّن SE-ResNet-50 في Faster R-CNN "AP من 38.0 إلى 40.4"، مما يمثل مكسباً نسبياً بنسبة 6.3٪.

#### 5.4 مسابقة ILSVRC 2017

حقق فريق الباحثين المركز الأول بـ "خطأ أعلى-5 بنسبة 2.251٪ على مجموعة الاختبار"، بتحسين نسبي يقارب "25٪" عن الفائز في 2016.

حقق SENet-154 "خطأ أعلى-1 بنسبة 18.68٪ وخطأ أعلى-5 بنسبة 4.47٪" باستخدام بروتوكولات التقييم القياسية.

---

### Translation Notes

- **Figures referenced:** Tables showing ImageNet results
- **Key terms introduced:**
  - ImageNet → ImageNet (kept as dataset name)
  - CIFAR-10/100 → CIFAR-10/100 (kept as dataset names)
  - Top-1 error → خطأ أعلى-1
  - Top-5 error → خطأ أعلى-5
  - Single-crop → بقطع واحد
  - Random cropping → القص العشوائي
  - Random horizontal flipping → الانعكاس الأفقي العشوائي
  - Synchronous SGD → SGD المتزامن
  - Momentum → زخم
  - Epoch → حقبة
  - Learning rate → معدل تعلم
  - Validation error → خطأ تحقق
  - Scene classification → تصنيف المشاهد
  - Object detection → كشف الأجسام
  - AP (Average Precision) → AP (متوسط الدقة)
  - Ensemble → مجموعة (في سياق ensemble models)
  - Test set → مجموعة الاختبار
  - Baseline → الأساس

- **Datasets mentioned:**
  - ImageNet 2012
  - CIFAR-10
  - CIFAR-100
  - Places365
  - COCO (Common Objects in Context)

- **Architecture names preserved:**
  - ResNet, SE-ResNet
  - ResNeXt, SE-ResNeXt
  - Inception-ResNet-v2
  - MobileNet, SE-MobileNet
  - ShuffleNet
  - WideResNet
  - Shake-Shake
  - Faster R-CNN

- **Key numerical results:**
  - ImageNet: SE-ResNet-50 improved from 7.48% to 6.62% top-5 error
  - ILSVRC 2017: Won with 2.251% top-5 error
  - COCO: Improved AP from 38.0 to 40.4
  - Mobile: 3.1% improvement on MobileNet

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
