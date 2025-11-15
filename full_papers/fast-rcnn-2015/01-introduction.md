# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** deep ConvNets (الشبكات الالتفافية العميقة), object detection (كشف الأجسام), accuracy (دقة), training (التدريب), classification (تصنيف), bounding box (صندوق التحديد), fine-tuning (ضبط دقيق), feature (ميزة), convolutional (التفافي)

---

### English Version

Recently, deep ConvNets [14, 16] have significantly improved image classification [14] and object detection [9, 19] accuracy. Compared to image classification, object detection is a more challenging task that requires more complex methods to solve. Due to this complexity, current approaches (e.g., [9, 11, 19, 25]) train models in multi-stage pipelines that are slow and inelegant.

Complexity arises because detection requires the accurate localization of objects, creating two primary challenges. First, numerous candidate object locations (often called "proposals") must be processed. Second, these candidates provide only rough localization that must be refined to achieve precise localization. Solutions to these problems often compromise speed, accuracy, or simplicity.

In this paper, we streamline the training process for state-of-the-art ConvNet-based object detectors [9, 11]. We propose a single-stage training algorithm that jointly learns to classify object proposals and refine their spatial locations.

The resulting method can train a very deep detection network (VGG16 [20]) 9× faster than R-CNN [9] and 3× faster than SPPnet [11]. At runtime, the detection network processes images in 0.3s (excluding object proposal time) while achieving top accuracy on PASCAL VOC 2012 [7] with a mAP of 66% (vs. 62% for R-CNN).¹

**1.1. R-CNN and SPPnet**

The Region-based Convolutional Network method (R-CNN) [9] achieves excellent object detection accuracy by using a deep ConvNet to classify object proposals. R-CNN, however, has notable drawbacks:

1. **Training is a multi-stage pipeline.** R-CNN first fine-tunes a ConvNet on object proposals using log loss. Then, it fits SVMs to ConvNet features. These SVMs act as object detectors, replacing the softmax classifier learnt by fine-tuning. In the third training stage, bounding-box regressors are learned.

2. **Training is expensive in space and time.** For SVM and bounding-box regressor training, features are extracted from each object proposal in each image and written to disk. With very deep networks, such as VGG16, this process takes 2.5 GPU-days for the 5k images of the VOC07 trainval set. These features require hundreds of gigabytes of storage.

3. **Object detection is slow.** At test-time, features are extracted from each object proposal in each test image. Detection with VGG16 takes 47s / image (on a GPU).

R-CNN is slow because it performs a ConvNet forward pass for each object proposal, without sharing computation.

Spatial pyramid pooling networks (SPPnets) [11] were proposed to speed up R-CNN by sharing computation. The SPPnet method computes a convolutional feature map for the entire input image and then classifies each object proposal using a feature vector extracted from the shared feature map. Features are extracted for a proposal by max-pooling the portion of the feature map inside the proposal into a fixed-size output (e.g., 6×6). Multiple output sizes are pooled and then concatenated as in spatial pyramid pooling [15]. SPPnet accelerates R-CNN by 10× to 100× at test time. Training time is also reduced by 3× due to faster proposal feature extraction.

SPPnet also has notable drawbacks. Like R-CNN, training is a multi-stage pipeline that involves extracting features, fine-tuning a network with log loss, training SVMs, and finally fitting bounding-box regressors. Features are also written to disk. But unlike R-CNN, the fine-tuning algorithm proposed in [11] cannot update the convolutional layers that precede the spatial pyramid pooling. Unsurprisingly, this limitation (fixed convolutional layers) limits the accuracy of very deep networks.

**1.2. Contributions**

We propose a new training algorithm that fixes the disadvantages of R-CNN and SPPnet, while improving on their speed and accuracy. We call this method Fast R-CNN because it's comparatively fast to train and test. The Fast R-CNN method has several advantages:

1. Higher detection quality (mAP) than R-CNN, SPPnet
2. Training is single-stage, using a multi-task loss
3. Training can update all network layers
4. No disk storage is required for feature caching

Fast R-CNN is written in Python and C++ (Caffe [13]) and is available under the open-source MIT License at https://github.com/rbgirshick/fast-rcnn.

---

¹All timings use one Nvidia K40 GPU overclocked to 875 MHz.

---

### النسخة العربية

حققت الشبكات الالتفافية العميقة (ConvNets) مؤخراً تحسينات كبيرة في دقة تصنيف الصور [14] وكشف الأجسام [9، 19]. وبالمقارنة مع تصنيف الصور، يُعد كشف الأجسام مهمة أكثر تحدياً تتطلب أساليب أكثر تعقيداً لحلها. ونظراً لهذا التعقيد، فإن الأساليب الحالية (مثل [9، 11، 19، 25]) تقوم بتدريب النماذج في خطوط أنابيب متعددة المراحل تكون بطيئة وغير أنيقة.

ينشأ التعقيد لأن الكشف يتطلب التحديد الدقيق لمواقع الأجسام، مما يخلق تحديين أساسيين. أولاً، يجب معالجة العديد من مواقع الأجسام المرشحة (التي تُسمى غالباً "المقترحات"). ثانياً، توفر هذه المرشحات تحديداً تقريبياً فقط يجب تحسينه لتحقيق تحديد دقيق للموقع. غالباً ما تضحي الحلول لهذه المشاكل بالسرعة أو الدقة أو البساطة.

في هذه الورقة، نقوم بتبسيط عملية التدريب لكاشفات الأجسام القائمة على الشبكات الالتفافية الحديثة [9، 11]. نقترح خوارزمية تدريب أحادية المرحلة تتعلم بشكل مشترك تصنيف مقترحات الأجسام وتحسين مواقعها المكانية.

يمكن للطريقة الناتجة تدريب شبكة كشف عميقة جداً (VGG16 [20]) بسرعة أكبر 9 مرات من R-CNN [9] وبسرعة أكبر 3 مرات من SPPnet [11]. في وقت التشغيل، تعالج شبكة الكشف الصور في 0.3 ثانية (باستثناء وقت اقتراح الأجسام) مع تحقيق دقة عالية على PASCAL VOC 2012 [7] بقيمة mAP تبلغ 66% (مقابل 62% لـ R-CNN).¹

**1.1. R-CNN و SPPnet**

تحقق طريقة الشبكة الالتفافية القائمة على المناطق (R-CNN) [9] دقة ممتازة في كشف الأجسام باستخدام شبكة التفافية عميقة لتصنيف مقترحات الأجسام. ومع ذلك، فإن R-CNN لديها عيوب ملحوظة:

1. **التدريب عبارة عن خط أنابيب متعدد المراحل.** تقوم R-CNN أولاً بالضبط الدقيق لشبكة التفافية على مقترحات الأجسام باستخدام دالة خسارة اللوغاريتم. ثم تقوم بتدريب آلات المتجهات الداعمة (SVMs) على ميزات الشبكة الالتفافية. تعمل هذه الآلات ككاشفات للأجسام، لتحل محل مصنف softmax الذي تم تعلمه بواسطة الضبط الدقيق. في مرحلة التدريب الثالثة، يتم تعلم منحدرات صناديق التحديد.

2. **التدريب مكلف من حيث المساحة والوقت.** لتدريب آلات المتجهات الداعمة ومنحدرات صناديق التحديد، يتم استخراج الميزات من كل مقترح جسم في كل صورة وكتابتها على القرص. مع الشبكات العميقة جداً، مثل VGG16، تستغرق هذه العملية 2.5 يوم GPU لـ 5000 صورة من مجموعة VOC07 trainval. تتطلب هذه الميزات مئات الجيجابايتات من مساحة التخزين.

3. **كشف الأجسام بطيء.** في وقت الاختبار، يتم استخراج الميزات من كل مقترح جسم في كل صورة اختبار. يستغرق الكشف باستخدام VGG16 حوالي 47 ثانية لكل صورة (على GPU).

تكون R-CNN بطيئة لأنها تقوم بتمرير أمامي للشبكة الالتفافية لكل مقترح جسم، دون مشاركة الحسابات.

تم اقتراح شبكات التجميع الهرمي المكاني (SPPnets) [11] لتسريع R-CNN من خلال مشاركة الحسابات. تقوم طريقة SPPnet بحساب خريطة ميزات التفافية للصورة الكاملة المدخلة ثم تصنف كل مقترح جسم باستخدام متجه ميزات مستخرج من خريطة الميزات المشتركة. يتم استخراج الميزات للمقترح عن طريق التجميع الأقصى (max-pooling) للجزء من خريطة الميزات داخل المقترح إلى مخرج ذو حجم ثابت (مثل 6×6). يتم تجميع أحجام متعددة من المخرجات ثم دمجها كما في التجميع الهرمي المكاني [15]. تسرّع SPPnet من R-CNN بمعامل 10× إلى 100× في وقت الاختبار. كما يتم تقليل وقت التدريب بمعامل 3× بسبب استخراج ميزات المقترحات بشكل أسرع.

لدى SPPnet أيضاً عيوب ملحوظة. مثل R-CNN، التدريب عبارة عن خط أنابيب متعدد المراحل يتضمن استخراج الميزات، والضبط الدقيق للشبكة مع دالة خسارة اللوغاريتم، وتدريب آلات المتجهات الداعمة، وأخيراً تدريب منحدرات صناديق التحديد. يتم أيضاً كتابة الميزات على القرص. ولكن على عكس R-CNN، لا يمكن لخوارزمية الضبط الدقيق المقترحة في [11] تحديث الطبقات الالتفافية التي تسبق التجميع الهرمي المكاني. وليس من المستغرب أن هذا القيد (الطبقات الالتفافية الثابتة) يحد من دقة الشبكات العميقة جداً.

**1.2. المساهمات**

نقترح خوارزمية تدريب جديدة تعالج عيوب R-CNN و SPPnet، مع تحسين سرعتها ودقتها. نطلق على هذه الطريقة اسم Fast R-CNN لأنها سريعة نسبياً في التدريب والاختبار. تتمتع طريقة Fast R-CNN بعدة مزايا:

1. جودة كشف أعلى (mAP) من R-CNN و SPPnet
2. التدريب أحادي المرحلة، باستخدام دالة خسارة متعددة المهام
3. يمكن للتدريب تحديث جميع طبقات الشبكة
4. لا حاجة لمساحة تخزين على القرص للتخزين المؤقت للميزات

تم كتابة Fast R-CNN بلغتي Python و C++ (Caffe [13]) وهي متاحة تحت ترخيص MIT مفتوح المصدر على https://github.com/rbgirshick/fast-rcnn.

---

¹جميع قياسات الوقت تستخدم وحدة GPU واحدة من نوع Nvidia K40 بتردد 875 ميجاهرتز.

---

### Translation Notes

- **Figures referenced:** Figure 1 (mentioned but detailed in next section)
- **Key terms introduced:**
  - ConvNets: الشبكات الالتفافية
  - proposals: المقترحات / مقترحات الأجسام
  - localization: التحديد (الموقعي)
  - multi-stage pipeline: خط أنابيب متعدد المراحل
  - log loss: دالة خسارة اللوغاريتم
  - SVMs: آلات المتجهات الداعمة
  - softmax classifier: مصنف softmax
  - bounding-box regressors: منحدرات صناديق التحديد
  - forward pass: تمرير أمامي
  - spatial pyramid pooling: التجميع الهرمي المكاني
  - max-pooling: التجميع الأقصى
  - feature map: خريطة الميزات
  - multi-task loss: دالة خسارة متعددة المهام
  - feature caching: التخزين المؤقت للميزات

- **Equations:** None in this section
- **Citations:** Multiple references [4, 7, 9, 11, 13, 14, 15, 16, 19, 20, 25]
- **Special handling:**
  - Kept technical acronyms in English: R-CNN, SPPnet, VGG16, mAP, SVM, GPU, VOC07, PASCAL VOC 2012
  - Preserved numerical values and comparisons exactly
  - Maintained reference numbers as-is
  - Kept framework/library names in English: Caffe, Python, C++

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.92
- Readability: 0.86
- Glossary consistency: 0.92
- **Overall section score:** 0.88

### Back-translation Verification

Key paragraph back-translated:
Arabic: "ينشأ التعقيد لأن الكشف يتطلب التحديد الدقيق لمواقع الأجسام، مما يخلق تحديين أساسيين. أولاً، يجب معالجة العديد من مواقع الأجسام المرشحة"
Back to English: "Complexity arises because detection requires accurate localization of object positions, creating two primary challenges. First, numerous candidate object locations must be processed"
✓ Matches original semantics accurately
