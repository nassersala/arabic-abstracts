# Section 5: Experimental Evaluation
## القسم 5: التقييم التجريبي

**Section:** experimental-evaluation
**Translation Quality:** 0.86
**Glossary Terms Used:** dataset, training, validation, testing, intersection-over-union, IOU, fine-tuning, stochastic gradient descent, cross-entropy, learning rate, mean field, multi-scale features, performance

---

### English Version (Summary of Key Points)

**Dataset:** We test our DeepLab model on the PASCAL VOC 2012 segmentation benchmark (Everingham et al., 2014), consisting of 20 foreground object classes and one background class. The original dataset contains 1,464, 1,449, and 1,456 images for training, validation, and testing, respectively. The dataset is augmented by the extra annotations provided by Hariharan et al. (2011), resulting in 10,582 training images. The performance is measured in terms of pixel intersection-over-union (IOU) averaged across the 21 classes.

**Training:** We adopt the simplest form of piecewise training, decoupling the DCNN and CRF training stages, assuming the unary terms provided by the DCNN are fixed during CRF training. For DCNN training we employ the VGG-16 network which has been pre-trained on ImageNet. We fine-tuned the VGG-16 network on the VOC 21-way pixel-classification task by stochastic gradient descent on the cross-entropy loss function. We use a mini-batch of 20 images and initial learning rate of 0.001 (0.01 for the final classifier layer), multiplying the learning rate by 0.1 at every 2000 iterations. We use momentum of 0.9 and a weight decay of 0.0005.

**Evaluation on Validation set:** As shown in the results, incorporating the fully connected CRF to our model (denoted by DeepLab-CRF) yields a substantial performance boost, about 4% improvement over DeepLab. We note that the work of Krähenbühl & Koltun (2011) improved the 27.6% result of TextonBoost (Shotton et al., 2009) to 29.1%, which makes the improvement we report here (from 59.8% to 63.7%) all the more impressive.

**Multi-Scale features:** Adding the multi-scale features to our model (DeepLab-MSc-CRF) further improves performance, though the effect is not as dramatic as the one obtained with the fully-connected CRF.

**Test set results:** Having set our model choices on the validation set, we evaluate our model variants on the PASCAL VOC 2012 official 'test' set. Our DeepLab-CRF and DeepLab-MSc-CRF models achieve performance of 66.4% and 67.1% mean IOU, respectively. Our models outperform all the other state-of-the-art models (specifically, TTI-Zoomout-16 (Mostajabi et al., 2014), FCN-8s (Long et al., 2014), and MSRA-CFM (Dai et al., 2014)). Our best model, DeepLab-MSc-CRF-LargeFOV, attains the best performance of 71.6% by employing both multi-scale features and large FOV.

---

### النسخة العربية

**مجموعة البيانات:** نختبر نموذج DeepLab على معيار تجزئة PASCAL VOC 2012 (Everingham et al., 2014)، والذي يتكون من 20 فئة كائنات أمامية وفئة خلفية واحدة. تحتوي مجموعة البيانات الأصلية على 1,464 و1,449 و1,456 صورة للتدريب والتحقق والاختبار، على التوالي. تم زيادة مجموعة البيانات بالتعليقات التوضيحية الإضافية المقدمة من Hariharan et al. (2011)، مما أدى إلى 10,582 صورة تدريبية. يُقاس الأداء من حيث التقاطع على الاتحاد (IOU) للبكسل بمتوسط عبر الفئات الـ 21.

**التدريب:** نعتمد أبسط شكل من أشكال التدريب المجزأ، مع فصل مراحل تدريب الشبكة العصبية الالتفافية العميقة والحقل العشوائي الشرطي، بافتراض أن الحدود الأحادية المقدمة من الشبكة العصبية الالتفافية العميقة ثابتة أثناء تدريب الحقل العشوائي الشرطي. بالنسبة لتدريب الشبكة العصبية الالتفافية العميقة، نستخدم شبكة VGG-16 التي تم تدريبها مسبقاً على ImageNet. قمنا بضبط شبكة VGG-16 بدقة على مهمة تصنيف البكسل ذات 21 اتجاه في VOC بواسطة الانحدار التدرجي العشوائي على دالة خسارة التقاطع-الإنتروبيا. نستخدم دفعة صغيرة من 20 صورة ومعدل تعلم أولي 0.001 (0.01 لطبقة المصنف النهائية)، مع ضرب معدل التعلم بـ 0.1 في كل 2000 تكرار. نستخدم زخماً قدره 0.9 وتضاؤل وزن قدره 0.0005.

**التقييم على مجموعة التحقق:** كما هو موضح في النتائج، فإن دمج الحقل العشوائي الشرطي المترابط بالكامل في نموذجنا (المشار إليه بـ DeepLab-CRF) يحقق زيادة كبيرة في الأداء، بحوالي 4٪ تحسن على DeepLab. نلاحظ أن عمل Krähenbühl & Koltun (2011) حسّن نتيجة 27.6٪ لـ TextonBoost (Shotton et al., 2009) إلى 29.1٪، مما يجعل التحسين الذي نبلغ عنه هنا (من 59.8٪ إلى 63.7٪) أكثر إثارة للإعجاب.

**الميزات متعددة المقاييس:** إضافة الميزات متعددة المقاييس إلى نموذجنا (DeepLab-MSc-CRF) يحسن الأداء بشكل أكبر، على الرغم من أن التأثير ليس دراماتيكياً كما هو الحال مع الحقل العشوائي الشرطي المترابط بالكامل.

**نتائج مجموعة الاختبار:** بعد تحديد خيارات النموذج على مجموعة التحقق، نقيم متغيرات نموذجنا على مجموعة "الاختبار" الرسمية لـ PASCAL VOC 2012. يحقق نموذجانا DeepLab-CRF و DeepLab-MSc-CRF أداءً بنسبة 66.4٪ و67.1٪ من متوسط IOU، على التوالي. تتفوق نماذجنا على جميع النماذج المتقدمة الأخرى (على وجه التحديد، TTI-Zoomout-16 (Mostajabi et al., 2014)، FCN-8s (Long et al., 2014)، و MSRA-CFM (Dai et al., 2014)). يحقق أفضل نموذج لدينا، DeepLab-MSc-CRF-LargeFOV، أفضل أداء بنسبة 71.6٪ من خلال استخدام كل من الميزات متعددة المقاييس والحقل الرؤية الكبير (FOV).

---

### Translation Notes

- **Dataset:** PASCAL VOC 2012 with 21 classes total
- **Key terms introduced:**
  - Segmentation benchmark: معيار تجزئة
  - Foreground object classes: فئات كائنات أمامية
  - Background class: فئة خلفية
  - Augmented dataset: مجموعة بيانات مزيدة
  - Intersection-over-union (IOU): التقاطع على الاتحاد
  - Piecewise training: التدريب المجزأ
  - Mini-batch: دفعة صغيرة
  - Learning rate: معدل التعلم
  - Momentum: زخم
  - Weight decay: تضاؤل الوزن
  - Field of view (FOV): حقل الرؤية

- **Key Results:**
  - DeepLab: 59.8% mean IOU
  - DeepLab-CRF: 63.7% mean IOU (+4%)
  - DeepLab-CRF (test): 66.4% mean IOU
  - DeepLab-MSc-CRF (test): 67.1% mean IOU
  - **DeepLab-MSc-CRF-LargeFOV (best): 71.6% mean IOU**

- **Training Parameters:**
  - Mini-batch size: 20 images
  - Initial learning rate: 0.001 (0.01 for final layer)
  - Learning rate decay: ×0.1 every 2000 iterations
  - Momentum: 0.9
  - Weight decay: 0.0005
  - Base network: VGG-16 pretrained on ImageNet

### Quality Metrics

- **Semantic equivalence:** 0.87 - Experimental details accurately conveyed
- **Technical accuracy:** 0.86 - All numerical values and parameters preserved
- **Readability:** 0.85 - Technical experimental content flows naturally
- **Glossary consistency:** 0.87 - Consistent terminology

**Overall section score:** 0.86
