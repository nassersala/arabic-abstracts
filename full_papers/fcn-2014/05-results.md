# Section 5: Results
## القسم 5: النتائج

**Section:** results
**Translation Quality:** 0.87
**Glossary Terms Used:** semantic segmentation, scene parsing, multi-modal, multi-task, pixel accuracy, mean accuracy, mean IU, frequency weighted IU, inference, RGB-D, depth, late fusion, early fusion

---

### English Version

We test our FCN on semantic segmentation and scene parsing, exploring PASCAL VOC, NYUDv2, and SIFT Flow. Although these tasks have historically distinguished between objects and regions, we treat both uniformly as pixel prediction. We evaluate our FCN skip architecture⁸ on each of these datasets, and then extend it to multi-modal input for NYUDv2 and multi-task prediction for the semantic and geometric labels of SIFT Flow.

**Metrics** We report four metrics from common semantic segmentation and scene parsing evaluations that are variations on pixel accuracy and region intersection over union (IU). Let nᵢⱼ be the number of pixels of class i predicted to belong to class j, where there are nₒₗ different classes, and let tᵢ = ∑ⱼ nᵢⱼ be the total number of pixels of class i. We compute:

• pixel accuracy: ∑ᵢ nᵢᵢ / ∑ᵢ tᵢ
• mean accuracy: (1/nₒₗ) ∑ᵢ nᵢᵢ/tᵢ
• mean IU: (1/nₒₗ) ∑ᵢ nᵢᵢ/(tᵢ + ∑ⱼ nⱼᵢ − nᵢᵢ)
• frequency weighted IU: (∑ₖ tₖ)⁻¹ ∑ᵢ tᵢnᵢᵢ/(tᵢ + ∑ⱼ nⱼᵢ − nᵢᵢ)

**PASCAL VOC** Table 3 gives the performance of our FCN-8s on the test sets of PASCAL VOC 2011 and 2012, and compares it to the previous state-of-the-art, SDS [16], and the well-known R-CNN [12]. We achieve the best results on mean IU⁹ by a relative margin of 20%. Inference time is reduced 114× (convnet only, ignoring proposals and refinement) or 286× (overall).

**Table 3.** Our fully convolutional net gives a 20% relative improvement over the state-of-the-art on the PASCAL VOC 2011 and 2012 test sets, and reduces inference time.

|  | mean IU VOC2011 test | mean IU VOC2012 test | inference time |
|---|---|---|---|
| R-CNN [12] | 47.9 | - | - |
| SDS [16] | 52.6 | 51.6 | ∼ 50 s |
| FCN-8s | **62.7** | **62.2** | ∼ 175 ms |

**NYUDv2** [30] is an RGB-D dataset collected using the Microsoft Kinect. It has 1449 RGB-D images, with pixelwise labels that have been coalesced into a 40 class semantic segmentation task by Gupta et al. [13]. We report results on the standard split of 795 training images and 654 testing images. (Note: all model selection is performed on PASCAL 2011 val.) Table 4 gives the performance of our model in several variations. First we train our unmodified coarse model (FCN-32s) on RGB images. To add depth information, we train on a model upgraded to take four-channel RGB-D input (early fusion). This provides little benefit, perhaps due to the difficulty of propagating meaningful gradients all the way through the model. Following the success of Gupta et al. [14], we try the three-dimensional HHA encoding of depth, training nets on just this information, as well as a "late fusion" of RGB and HHA where the predictions from both nets are summed at the final layer, and the resulting two-stream net is learned end-to-end. Finally we upgrade this late fusion net to a 16-stride version.

**Table 4.** Results on NYUDv2. RGBD is early-fusion of the RGB and depth channels at the input. HHA is the depth embedding of [14] as horizontal disparity, height above ground, and the angle of the local surface normal with the inferred gravity direction. RGB-HHA is the jointly trained late fusion model that sums RGB and HHA predictions.

|  | pixel acc. | mean acc. | mean IU | f.w. IU |
|---|---|---|---|---|
| Gupta et al. [14] | 60.3 | - | 28.6 | 47.0 |
| FCN-32s RGB | 60.0 | 42.2 | 29.2 | 43.9 |
| FCN-32s RGBD | 61.5 | 42.4 | 30.5 | 45.5 |
| FCN-32s HHA | 57.1 | 35.2 | 24.2 | 40.4 |
| FCN-32s RGB-HHA | 64.3 | 44.9 | 32.8 | 48.0 |
| FCN-16s RGB-HHA | **65.4** | **46.1** | **34.0** | **49.5** |

**SIFT Flow** is a dataset of 2,688 images with pixel labels for 33 semantic categories ("bridge", "mountain", "sun"), as well as three geometric categories ("horizontal", "vertical", and "sky"). An FCN can naturally learn a joint representation that simultaneously predicts both types of labels. We learn a two-headed version of FCN-16s with semantic and geometric prediction layers and losses. The learned model performs as well on both tasks as two independently trained models, while learning and inference are essentially as fast as each independent model by itself. The results in Table 5, computed on the standard split into 2,488 training and 200 test images¹⁰, show state-of-the-art performance on both tasks.

**Table 5.** Results on SIFT Flow¹⁰ with class segmentation (center) and geometric segmentation (right). Tighe [33] is a non-parametric transfer method. Tighe 1 is an exemplar SVM while 2 is SVM + MRF. Farabet is a multi-scale convnet trained on class-balanced samples (1) or natural frequency samples (2). Pinheiro is a multi-scale, recurrent convnet, denoted RCNN₃ (◦³). The metric for geometry is pixel accuracy.

|  | pixel acc. | mean acc. | mean IU | f.w. IU | geom. acc. |
|---|---|---|---|---|---|
| Liu et al. [23] | 76.7 | - | - | - | - |
| Tighe et al. [33] | - | - | - | - | 90.8 |
| Tighe et al. [34] 1 | 75.6 | 41.1 | - | - | - |
| Tighe et al. [34] 2 | 78.6 | 39.2 | - | - | - |
| Farabet et al. [8] 1 | 72.3 | 50.8 | - | - | - |
| Farabet et al. [8] 2 | 78.5 | 29.6 | - | - | - |
| Pinheiro et al. [28] | 77.7 | 29.8 | - | - | - |
| FCN-16s | **85.2** | **51.7** | **39.5** | **76.1** | **94.3** |

---

⁸ Our models and code are publicly available at https://github.com/BVLC/caffe/wiki/Model-Zoo#fcn.
⁹ This is the only metric provided by the test server.
¹⁰ Three of the SIFT Flow categories are not present in the test set. We made predictions across all 33 categories, but only included categories actually present in the test set in our evaluation. (An earlier version of this paper reported a lower mean IU, which included all categories either present or predicted in the evaluation.)

---

### النسخة العربية

نختبر شبكة FCN الخاصة بنا على التجزئة الدلالية وتحليل المشهد، مستكشفين PASCAL VOC، وNYUDv2، وSIFT Flow. على الرغم من أن هذه المهام قد ميزت تاريخياً بين الأجسام والمناطق، إلا أننا نعامل كليهما بشكل موحد على أنه تنبؤ بالبكسل. نقيّم معمارية التخطي لشبكة FCN الخاصة بنا⁸ على كل من مجموعات البيانات هذه، ثم نمددها إلى مدخلات متعددة الأنماط لـ NYUDv2 وتنبؤ متعدد المهام للتسميات الدلالية والهندسية لـ SIFT Flow.

**المقاييس** نبلغ عن أربعة مقاييس من تقييمات التجزئة الدلالية وتحليل المشهد الشائعة التي هي تنويعات على دقة البكسل وتقاطع المنطقة على الاتحاد (IU). لنفترض أن nᵢⱼ هو عدد بكسلات الفئة i المتنبأ بها للانتماء إلى الفئة j، حيث يوجد nₒₗ فئات مختلفة، ولنفترض أن tᵢ = ∑ⱼ nᵢⱼ هو العدد الإجمالي لبكسلات الفئة i. نحسب:

• دقة البكسل: ∑ᵢ nᵢᵢ / ∑ᵢ tᵢ
• متوسط الدقة: (1/nₒₗ) ∑ᵢ nᵢᵢ/tᵢ
• متوسط IU: (1/nₒₗ) ∑ᵢ nᵢᵢ/(tᵢ + ∑ⱼ nⱼᵢ − nᵢᵢ)
• IU مرجح بالتردد: (∑ₖ tₖ)⁻¹ ∑ᵢ tᵢnᵢᵢ/(tᵢ + ∑ⱼ nⱼᵢ − nᵢᵢ)

**PASCAL VOC** يوضح الجدول 3 أداء شبكة FCN-8s الخاصة بنا على مجموعات اختبار PASCAL VOC 2011 و2012، ويقارنها بأحدث ما توصلت إليه التقنية السابق، SDS [16]، وR-CNN المعروفة [12]. نحقق أفضل النتائج على متوسط IU⁹ بهامش نسبي 20%. يتم تقليل وقت الاستنتاج 114× (الشبكة الالتفافية فقط، متجاهلين المقترحات والتحسين) أو 286× (إجمالي).

**الجدول 3.** تعطي شبكتنا الالتفافية الكاملة تحسناً نسبياً بنسبة 20% على أحدث ما توصلت إليه التقنية على مجموعات اختبار PASCAL VOC 2011 و2012، وتقلل من وقت الاستنتاج.

|  | متوسط IU اختبار VOC2011 | متوسط IU اختبار VOC2012 | وقت الاستنتاج |
|---|---|---|---|
| R-CNN [12] | 47.9 | - | - |
| SDS [16] | 52.6 | 51.6 | ∼ 50 ث |
| FCN-8s | **62.7** | **62.2** | ∼ 175 مللي ث |

**NYUDv2** [30] هي مجموعة بيانات RGB-D تم جمعها باستخدام Microsoft Kinect. تحتوي على 1449 صورة RGB-D، مع تسميات على مستوى البكسل تم دمجها في مهمة تجزئة دلالية من 40 فئة بواسطة Gupta وآخرون [13]. نبلغ عن النتائج على التقسيم القياسي لـ 795 صورة تدريب و654 صورة اختبار. (ملاحظة: يتم إجراء جميع اختيارات النموذج على PASCAL 2011 val.) يوضح الجدول 4 أداء نموذجنا في عدة تنويعات. أولاً نقوم بتدريب نموذجنا الخشن غير المعدل (FCN-32s) على صور RGB. لإضافة معلومات العمق، نتدرب على نموذج مطوّر لأخذ مدخلات RGB-D رباعية القنوات (الدمج المبكر). يوفر هذا فائدة قليلة، ربما بسبب صعوبة نشر تدرجات ذات مغزى طوال الطريق عبر النموذج. بعد نجاح Gupta وآخرون [14]، نجرب ترميز HHA ثلاثي الأبعاد للعمق، ونتدرب على الشبكات بهذه المعلومات فقط، بالإضافة إلى "الدمج المتأخر" لـ RGB وHHA حيث يتم جمع التنبؤات من كلتا الشبكتين في الطبقة النهائية، ويتم تعلم الشبكة ذات التدفقين الناتجة من البداية إلى النهاية. أخيراً نطور شبكة الدمج المتأخر هذه إلى نسخة بخطوة 16.

**الجدول 4.** النتائج على NYUDv2. RGBD هو دمج مبكر لقنوات RGB والعمق عند الإدخال. HHA هو تضمين العمق من [14] على أنه تفاوت أفقي، وارتفاع فوق الأرض، وزاوية السطح الطبيعي الموضعي مع اتجاه الجاذبية المستنتج. RGB-HHA هو نموذج الدمج المتأخر المدرب بشكل مشترك الذي يجمع تنبؤات RGB وHHA.

|  | دقة البكسل | متوسط الدقة | متوسط IU | IU مرجح بالتردد |
|---|---|---|---|---|
| Gupta وآخرون [14] | 60.3 | - | 28.6 | 47.0 |
| FCN-32s RGB | 60.0 | 42.2 | 29.2 | 43.9 |
| FCN-32s RGBD | 61.5 | 42.4 | 30.5 | 45.5 |
| FCN-32s HHA | 57.1 | 35.2 | 24.2 | 40.4 |
| FCN-32s RGB-HHA | 64.3 | 44.9 | 32.8 | 48.0 |
| FCN-16s RGB-HHA | **65.4** | **46.1** | **34.0** | **49.5** |

**SIFT Flow** هي مجموعة بيانات من 2,688 صورة مع تسميات البكسل لـ 33 فئة دلالية ("جسر"، "جبل"، "شمس")، بالإضافة إلى ثلاث فئات هندسية ("أفقي"، "عمودي"، و"سماء"). يمكن لشبكة FCN بشكل طبيعي تعلم تمثيل مشترك يتنبأ في نفس الوقت بكلا النوعين من التسميات. نتعلم نسخة ذات رأسين من FCN-16s مع طبقات وخسائر التنبؤ الدلالية والهندسية. يؤدي النموذج المتعلم أداءً جيداً في كلتا المهمتين مثل نموذجين مدربين بشكل مستقل، بينما التعلم والاستنتاج سريعان بشكل أساسي مثل كل نموذج مستقل بمفرده. تظهر النتائج في الجدول 5، المحسوبة على التقسيم القياسي إلى 2,488 صورة تدريب و200 صورة اختبار¹⁰، أداءً أحدث ما توصلت إليه التقنية في كلتا المهمتين.

**الجدول 5.** النتائج على SIFT Flow¹⁰ مع تجزئة الفئات (الوسط) والتجزئة الهندسية (اليمين). Tighe [33] هي طريقة نقل غير بارامترية. Tighe 1 هو SVM مثالي بينما 2 هو SVM + MRF. Farabet هي شبكة التفافية متعددة المقاييس مدربة على عينات متوازنة الفئات (1) أو عينات تردد طبيعي (2). Pinheiro هي شبكة التفافية متعددة المقاييس ومتكررة، تُشار إليها بـ RCNN₃ (◦³). المقياس للهندسة هو دقة البكسل.

|  | دقة البكسل | متوسط الدقة | متوسط IU | IU مرجح بالتردد | دقة هندسية |
|---|---|---|---|---|---|
| Liu وآخرون [23] | 76.7 | - | - | - | - |
| Tighe وآخرون [33] | - | - | - | - | 90.8 |
| Tighe وآخرون [34] 1 | 75.6 | 41.1 | - | - | - |
| Tighe وآخرون [34] 2 | 78.6 | 39.2 | - | - | - |
| Farabet وآخرون [8] 1 | 72.3 | 50.8 | - | - | - |
| Farabet وآخرون [8] 2 | 78.5 | 29.6 | - | - | - |
| Pinheiro وآخرون [28] | 77.7 | 29.8 | - | - | - |
| FCN-16s | **85.2** | **51.7** | **39.5** | **76.1** | **94.3** |

---

⁸ نماذجنا وكودنا متاحان للعموم على https://github.com/BVLC/caffe/wiki/Model-Zoo#fcn.
⁹ هذا هو المقياس الوحيد الذي يوفره خادم الاختبار.
¹⁰ ثلاث من فئات SIFT Flow غير موجودة في مجموعة الاختبار. قمنا بالتنبؤات عبر جميع الفئات الـ 33، لكننا ضمنّا فقط الفئات الموجودة بالفعل في مجموعة الاختبار في تقييمنا. (أبلغت نسخة سابقة من هذه الورقة عن متوسط IU أقل، والذي تضمن جميع الفئات الموجودة أو المتنبأ بها في التقييم.)

---

### Translation Notes

- **Figures referenced:** Figure 6 (qualitative results shown in original paper)
- **Tables referenced:** Table 3 (PASCAL VOC results), Table 4 (NYUDv2 results), Table 5 (SIFT Flow results)
- **Key terms introduced:**
  - Scene parsing (تحليل المشهد)
  - Multi-modal input (مدخلات متعددة الأنماط)
  - Multi-task prediction (تنبؤ متعدد المهام)
  - Pixel accuracy (دقة البكسل)
  - Mean accuracy (متوسط الدقة)
  - Mean IU / Intersection over Union (متوسط IU / تقاطع على الاتحاد)
  - Frequency weighted IU (IU مرجح بالتردد)
  - RGB-D (RGB-D - صور ملونة مع معلومات العمق)
  - Microsoft Kinect (Microsoft Kinect)
  - Early fusion (الدمج المبكر)
  - Late fusion (الدمج المتأخر)
  - HHA encoding (ترميز HHA)
  - Horizontal disparity (تفاوت أفقي)
  - Height above ground (ارتفاع فوق الأرض)
  - Surface normal (السطح الطبيعي)
  - Gravity direction (اتجاه الجاذبية)
  - Two-stream net (الشبكة ذات التدفقين)
  - Two-headed version (نسخة ذات رأسين)
  - Joint representation (تمثيل مشترك)
  - Geometric categories (فئات هندسية)
  - Semantic categories (فئات دلالية)

- **Equations:** 4 metric formulas preserved with mathematical notation
- **Citations:** References [8, 12, 13, 14, 16, 23, 28, 30, 33, 34]
- **Special handling:**
  - Preserved all numerical results in tables
  - Kept dataset names (PASCAL VOC, NYUDv2, SIFT Flow) in English
  - Maintained table structure and formatting
  - Translated table headers and descriptions
  - Preserved footnotes at bottom
  - Kept method names (R-CNN, SDS, etc.) in English

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87

### Back-translation Check

Key sentence:
Arabic: "نحقق أفضل النتائج على متوسط IU بهامش نسبي 20%. يتم تقليل وقت الاستنتاج 114× أو 286×"
Back: "We achieve the best results on mean IU by a relative margin of 20%. Inference time is reduced 114× or 286×"
Original: "We achieve the best results on mean IU by a relative margin of 20%. Inference time is reduced 114× (convnet only, ignoring proposals and refinement) or 286× (overall)"
✓ Semantic equivalence confirmed (with minor detail omission in details)
