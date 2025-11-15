# Section 6: Experiments
## القسم 6: التجارب

**Section:** experiments
**Translation Quality:** 0.88
**Glossary Terms Used:** ImageNet classification (تصنيف ImageNet), training setup (إعداد التدريب), TensorFlow, RMSPropOptimizer, batch normalization (تطبيع الدفعة), weight decay (تناقص الوزن), learning rate (معدل التعلم), GPU, batch size (حجم الدفعة), object detection (كشف الأجسام), feature extractors (مستخرجات الميزات), Single Shot Detector (SSD), COCO dataset, YOLOv2, Faster-RCNN, RFCN, separable convolutions (التفافات قابلة للفصل), parameters (معاملات), semantic segmentation (التجزئة الدلالية), DeepLabv3, atrous convolution (الالتفاف الموسع), PASCAL VOC, mIOU, ablation study (دراسة الاستئصال), residual connections (اتصالات البقايا), bottleneck (عنق)

---

### English Version

## 6.1 ImageNet Classification

**Training setup**: We train our models using TensorFlow. We use the standard RMSPropOptimizer with both decay and momentum set to 0.9. We use batch normalization after every layer, and the standard weight decay is set to 0.00004. Following MobileNetV1 setup we use initial learning rate of 0.045, and learning rate decay rate of 0.98 per epoch. We use 16 GPU asynchronous workers, and a batch size of 96.

**Results**: We compare our networks against MobileNetV1, ShuffleNet and NASNet-A models. The statistics of a few selected models is shown in Table 3 with the full performance graph shown in Figure 4.

**Table 3: Performance on ImageNet**, comparison for different networks. As is common practice for ops, we count the total number of Multiply-Adds. In the last column we report running time in milliseconds (ms) for a single large core of the Google Pixel 1 phone (using TF-Lite). We do not report ShuffleNet numbers as efficient group convolutions and shuffling are not yet supported.

| Network | Top 1 | Params | MAdds | CPU |
|---------|-------|--------|-------|-----|
| MobileNetV1 | 70.6 | 4.2M | 575M | 113ms |
| ShuffleNet (1.5) | 71.5 | **3.4M** | 292M | - |
| ShuffleNet (x2) | 73.7 | 5.4M | 524M | - |
| NasNet-A | 74.0 | 5.3M | 564M | 183ms |
| **MobileNetV2** | **72.0** | **3.4M** | **300M** | **75ms** |
| **MobileNetV2 (1.4)** | **74.7** | 6.9M | 585M | **143ms** |

## 6.2 Object Detection

We evaluate and compare the performance of MobileNetV2 and MobileNetV1 as feature extractors for object detection with a modified version of the Single Shot Detector (SSD) on COCO dataset. We also compare to YOLOv2 and original SSD (with VGG-16 as base network) as baselines. We do not compare performance with other architectures such as Faster-RCNN and RFCN since our focus is on mobile/real-time models.

**SSDLite**: In this paper, we introduce a mobile friendly variant of regular SSD. We replace all the regular convolutions with separable convolutions (depthwise followed by $1\times1$ projection) in SSD prediction layers. This design is in line with the overall design of MobileNets and is seen to be much more computationally efficient. We call this modified version SSDLite. Compared to regular SSD, SSDLite dramatically reduces both parameter count and computational cost as shown in Table 4.

**Table 4:** Comparison of the size and the computational cost between SSD and SSDLite configured with MobileNetV2 and making predictions for 80 classes.

| | Params | MAdds |
|---|--------|-------|
| SSD | 14.8M | 1.25B |
| **SSDLite** | **2.1M** | **0.35B** |

For MobileNetV1, we follow the setup in [cite]. For MobileNetV2, the first layer of SSDLite is attached to the expansion of layer 15 (with output stride of 16). The second and the rest of SSDLite layers are attached on top of the last layer (with output stride of 32). This setup is consistent with MobileNetV1 as all layers are attached to the feature map of the same output strides.

Both MobileNet models are trained and evaluated with Open Source TensorFlow Object Detection API. The input resolution of both models is $320\times 320$. We benchmark and compare both mAP (COCO challenge metrics), number of parameters and number of Multiply-Adds. The results are shown in Table 5. MobileNetV2 SSDLite is not only the most efficient model, but also the most accurate of the three. Notably, MobileNetV2 SSDLite is **20× more efficient** and **10× smaller** while still outperforms YOLOv2 on COCO dataset.

**Table 5:** Performance comparison of MobileNetV2 + SSDLite and other realtime detectors on the COCO dataset object detection task. MobileNetV2 + SSDLite achieves competitive accuracy with significantly fewer parameters and smaller computational complexity. All models are trained on trainval35k and evaluated on test-dev.

| Network | mAP | Params | MAdd | CPU |
|---------|-----|--------|------|-----|
| SSD300 | 23.2 | 36.1M | 35.2B | - |
| SSD512 | 26.8 | 36.1M | 99.5B | - |
| YOLOv2 | 21.6 | 50.7M | 17.5B | - |
| MNet V1 + SSDLite | 22.2 | 5.1M | 1.3B | 270ms |
| **MNet V2 + SSDLite** | **22.1** | **4.3M** | **0.8B** | **200ms** |

## 6.3 Semantic Segmentation

In this section, we compare MobileNetV1 and MobileNetV2 models used as feature extractors with DeepLabv3 for the task of mobile semantic segmentation. DeepLabv3 adopts atrous convolution, a powerful tool to explicitly control the resolution of computed feature maps, and builds five parallel heads including (a) Atrous Spatial Pyramid Pooling module (ASPP) containing three $3\times 3$ convolutions with different atrous rates, (b) $1\times 1$ convolution head, and (c) Image-level features.

We denote by *output_stride* the ratio of input image spatial resolution to final output resolution, which is controlled by applying the atrous convolution properly. For semantic segmentation, we usually employ *output_stride*=16 or 8 for denser feature maps. We conduct the experiments on the PASCAL VOC 2012 dataset, with extra annotated images from [cite] and evaluation metric mIOU.

To build a mobile model, we experimented with three design variations: (1) different feature extractors, (2) simplifying the DeepLabv3 heads for faster computation, and (3) different inference strategies for boosting the performance. Our results are summarized in Table 6.

We have observed that: (a) the inference strategies, including multi-scale inputs and adding left-right flipped images, significantly increase the MAdds and thus are not suitable for on-device applications, (b) using *output_stride*=16 is more efficient than *output_stride*=8, (c) MobileNetV1 is already a powerful feature extractor and only requires about 4.9-5.7 times fewer MAdds than ResNet-101 (e.g., mIOU: 78.56 vs 82.70, and MAdds: 941.9B vs 4870.6B), (d) it is more efficient to build DeepLabv3 heads on top of the second last feature map of MobileNetV2 than on the original last-layer feature map, since the second to last feature map contains 320 channels instead of 1280, and by doing so, we attain similar performance, but require about 2.5 times fewer operations than the MobileNetV1 counterparts, and (e) DeepLabv3 heads are computationally expensive and removing the ASPP module significantly reduces the MAdds with only a slight performance degradation.

In the end of the Table 6, we identify a potential candidate for on-device applications (in bold face), which attains 75.32% mIOU and only requires 2.75B MAdds.

**Table 6:** MobileNet + DeepLabv3 inference strategy on the PASCAL VOC 2012 validation set. **MNet V2***: Second last feature map is used for DeepLabv3 heads. **OS**: *output_stride*. **ASPP**: Atrous Spatial Pyramid Pooling. **MF**: Multi-scale and left-right flipped inputs during test. All models have been pretrained on COCO.

| Network | OS | ASPP | MF | mIOU | Params | MAdds |
|---------|----|----|-----|------|--------|-------|
| MNet V1 | 16 | ✓ | | 75.29 | 11.15M | 14.25B |
| | 8 | ✓ | ✓ | 78.56 | 11.15M | 941.9B |
| MNet V2* | 16 | ✓ | | 75.70 | 4.52M | 5.8B |
| | 8 | ✓ | ✓ | 78.42 | 4.52M | 387B |
| MNet V2* | 16 | | | **75.32** | **2.11M** | **2.75B** |
| | 8 | | ✓ | 77.33 | 2.11M | 152.6B |
| ResNet-101 | 16 | ✓ | | 80.49 | 58.16M | 81.0B |
| | 8 | ✓ | ✓ | 82.70 | 58.16M | 4870.6B |

## 6.4 Ablation Study

**Inverted residual connections**: The importance of residual connection has been studied extensively. The new result reported in this paper is that the shortcut connecting bottleneck perform better than shortcuts connecting the expanded layers (see Figure 5 for comparison).

**Importance of linear bottlenecks**: The linear bottleneck models are strictly less powerful than models with non-linearities, because the activations can always operate in linear regime with appropriate changes to biases and scaling. However our experiments shown in Figure 5 indicate that linear bottlenecks improve performance, providing support that non-linearity destroys information in low-dimensional space. We note that in the presence of shortcuts the information loss is actually less strong.

---

### النسخة العربية

## 6.1 تصنيف ImageNet

**إعداد التدريب**: ندرب نماذجنا باستخدام TensorFlow. نستخدم RMSPropOptimizer القياسي مع ضبط كل من التناقص والزخم على 0.9. نستخدم تطبيع الدفعة بعد كل طبقة، ويتم ضبط تناقص الوزن القياسي على 0.00004. بعد إعداد MobileNetV1 نستخدم معدل تعلم أولي 0.045، ومعدل تناقص معدل التعلم 0.98 لكل حقبة. نستخدم 16 عامل غير متزامن من GPU، وحجم دفعة 96.

**النتائج**: نقارن شبكاتنا مع نماذج MobileNetV1 وShuffleNet وNASNet-A. تظهر إحصائيات بعض النماذج المختارة في الجدول 3 مع الرسم البياني الكامل للأداء الموضح في الشكل 4.

**الجدول 3: الأداء على ImageNet**، مقارنة لشبكات مختلفة. كما هو الممارسة الشائعة للعمليات، نحسب العدد الإجمالي لعمليات الضرب والجمع. في العمود الأخير نبلغ عن وقت التشغيل بالمللي ثانية (ms) لنواة كبيرة واحدة من هاتف Google Pixel 1 (باستخدام TF-Lite). لا نبلغ عن أرقام ShuffleNet لأن التفافات المجموعة الفعالة والخلط لم يتم دعمهما بعد.

| الشبكة | Top 1 | المعاملات | MAdds | CPU |
|---------|-------|--------|-------|-----|
| MobileNetV1 | 70.6 | 4.2M | 575M | 113ms |
| ShuffleNet (1.5) | 71.5 | **3.4M** | 292M | - |
| ShuffleNet (x2) | 73.7 | 5.4M | 524M | - |
| NasNet-A | 74.0 | 5.3M | 564M | 183ms |
| **MobileNetV2** | **72.0** | **3.4M** | **300M** | **75ms** |
| **MobileNetV2 (1.4)** | **74.7** | 6.9M | 585M | **143ms** |

## 6.2 كشف الأجسام

نقيم ونقارن أداء MobileNetV2 وMobileNetV1 كمستخرجات ميزات لكشف الأجسام مع نسخة معدلة من الكاشف أحادي التسديد (SSD) على مجموعة بيانات COCO. نقارن أيضاً بـ YOLOv2 وSSD الأصلي (مع VGG-16 كشبكة أساسية) كخطوط أساس. لا نقارن الأداء مع معماريات أخرى مثل Faster-RCNN وRFCN لأن تركيزنا على النماذج المحمولة/الفورية.

**SSDLite**: في هذا البحث، نقدم متغيراً ملائماً للأجهزة المحمولة من SSD العادي. نستبدل جميع الالتفافات العادية بالتفافات قابلة للفصل (حسب العمق متبوعة بإسقاط $1\times1$) في طبقات التنبؤ SSD. يتماشى هذا التصميم مع التصميم الشامل لـ MobileNets ويُرى أنه أكثر كفاءة حسابياً بكثير. نسمي هذه النسخة المعدلة SSDLite. بالمقارنة مع SSD العادي، يقلل SSDLite بشكل كبير من عدد المعاملات والتكلفة الحسابية كما هو موضح في الجدول 4.

**الجدول 4:** مقارنة الحجم والتكلفة الحسابية بين SSD وSSDLite المُهيأ مع MobileNetV2 والتنبؤ بـ 80 صنف.

| | المعاملات | MAdds |
|---|--------|-------|
| SSD | 14.8M | 1.25B |
| **SSDLite** | **2.1M** | **0.35B** |

بالنسبة لـ MobileNetV1، نتبع الإعداد في [cite]. بالنسبة لـ MobileNetV2، يتم إرفاق الطبقة الأولى من SSDLite بتوسيع الطبقة 15 (مع خطوة إخراج 16). يتم إرفاق الطبقة الثانية وبقية طبقات SSDLite أعلى الطبقة الأخيرة (مع خطوة إخراج 32). يتسق هذا الإعداد مع MobileNetV1 حيث يتم إرفاق جميع الطبقات بخريطة الميزات بنفس خطوات الإخراج.

يتم تدريب وتقييم كلا نموذجي MobileNet باستخدام واجهة برمجة تطبيقات كشف الأجسام TensorFlow مفتوحة المصدر. دقة الإدخال لكلا النموذجين هي $320\times 320$. نقيس ونقارن كلاً من mAP (مقاييس تحدي COCO)، وعدد المعاملات وعدد عمليات الضرب والجمع. تظهر النتائج في الجدول 5. MobileNetV2 SSDLite ليس فقط النموذج الأكثر كفاءة، بل هو أيضاً الأكثر دقة من الثلاثة. والجدير بالذكر أن MobileNetV2 SSDLite **أكثر كفاءة بـ 20 مرة** و**أصغر بـ 10 مرات** بينما لا يزال يتفوق على YOLOv2 على مجموعة بيانات COCO.

**الجدول 5:** مقارنة أداء MobileNetV2 + SSDLite والكواشف الفورية الأخرى في مهمة كشف الأجسام على مجموعة بيانات COCO. يحقق MobileNetV2 + SSDLite دقة منافسة مع معاملات أقل بكثير وتعقيد حسابي أصغر. يتم تدريب جميع النماذج على trainval35k وتقييمها على test-dev.

| الشبكة | mAP | المعاملات | MAdd | CPU |
|---------|-----|--------|------|-----|
| SSD300 | 23.2 | 36.1M | 35.2B | - |
| SSD512 | 26.8 | 36.1M | 99.5B | - |
| YOLOv2 | 21.6 | 50.7M | 17.5B | - |
| MNet V1 + SSDLite | 22.2 | 5.1M | 1.3B | 270ms |
| **MNet V2 + SSDLite** | **22.1** | **4.3M** | **0.8B** | **200ms** |

## 6.3 التجزئة الدلالية

في هذا القسم، نقارن نماذج MobileNetV1 وMobileNetV2 المستخدمة كمستخرجات ميزات مع DeepLabv3 لمهمة التجزئة الدلالية المحمولة. يتبنى DeepLabv3 الالتفاف الموسع، وهو أداة قوية للتحكم صراحة في دقة خرائط الميزات المحسوبة، ويبني خمسة رؤوس متوازية بما في ذلك (أ) وحدة التجميع الهرمي المكاني الموسع (ASPP) التي تحتوي على ثلاثة التفافات $3\times 3$ بمعدلات توسيع مختلفة، (ب) رأس التفاف $1\times 1$، و(ج) ميزات مستوى الصورة.

نشير بـ *output_stride* إلى نسبة دقة الصورة المكانية للإدخال إلى دقة الإخراج النهائي، والتي يتم التحكم فيها من خلال تطبيق الالتفاف الموسع بشكل صحيح. بالنسبة للتجزئة الدلالية، نستخدم عادة *output_stride*=16 أو 8 لخرائط ميزات أكثر كثافة. نجري التجارب على مجموعة بيانات PASCAL VOC 2012، مع صور مُعلّمة إضافية من [cite] ومقياس التقييم mIOU.

لبناء نموذج محمول، جرّبنا ثلاثة أشكال تصميم: (1) مستخرجات ميزات مختلفة، (2) تبسيط رؤوس DeepLabv3 لحساب أسرع، و(3) استراتيجيات استدلال مختلفة لتعزيز الأداء. تُلخّص نتائجنا في الجدول 6.

لاحظنا أن: (أ) استراتيجيات الاستدلال، بما في ذلك مدخلات متعددة المقاييس وإضافة صور مقلوبة يميناً-يساراً، تزيد بشكل كبير من MAdds وبالتالي غير مناسبة للتطبيقات على الجهاز، (ب) استخدام *output_stride*=16 أكثر كفاءة من *output_stride*=8، (ج) MobileNetV1 هو بالفعل مستخرج ميزات قوي ويتطلب فقط حوالي 4.9-5.7 مرات أقل من MAdds من ResNet-101 (على سبيل المثال، mIOU: 78.56 مقابل 82.70، وMAdds: 941.9B مقابل 4870.6B)، (د) من الأكثر كفاءة بناء رؤوس DeepLabv3 أعلى خريطة الميزات قبل الأخيرة لـ MobileNetV2 بدلاً من خريطة الميزات الأخيرة الأصلية، نظراً لأن خريطة الميزات قبل الأخيرة تحتوي على 320 قناة بدلاً من 1280، وبذلك، نحصل على أداء مماثل، ولكن نحتاج إلى حوالي 2.5 مرة عمليات أقل من نظيراتها في MobileNetV1، و(هـ) رؤوس DeepLabv3 مكلفة حسابياً وإزالة وحدة ASPP تقلل بشكل كبير من MAdds مع تدهور طفيف فقط في الأداء.

في نهاية الجدول 6، نحدد مرشحاً محتملاً للتطبيقات على الجهاز (بخط عريض)، والذي يحقق 75.32% mIOU ويتطلب فقط 2.75B MAdds.

**الجدول 6:** استراتيجية استدلال MobileNet + DeepLabv3 على مجموعة التحقق PASCAL VOC 2012. **MNet V2***: يتم استخدام خريطة الميزات قبل الأخيرة لرؤوس DeepLabv3. **OS**: *output_stride*. **ASPP**: التجميع الهرمي المكاني الموسع. **MF**: مدخلات متعددة المقاييس ومقلوبة يميناً-يساراً أثناء الاختبار. جميع النماذج تم تدريبها مسبقاً على COCO.

| الشبكة | OS | ASPP | MF | mIOU | المعاملات | MAdds |
|---------|----|----|-----|------|--------|-------|
| MNet V1 | 16 | ✓ | | 75.29 | 11.15M | 14.25B |
| | 8 | ✓ | ✓ | 78.56 | 11.15M | 941.9B |
| MNet V2* | 16 | ✓ | | 75.70 | 4.52M | 5.8B |
| | 8 | ✓ | ✓ | 78.42 | 4.52M | 387B |
| MNet V2* | 16 | | | **75.32** | **2.11M** | **2.75B** |
| | 8 | | ✓ | 77.33 | 2.11M | 152.6B |
| ResNet-101 | 16 | ✓ | | 80.49 | 58.16M | 81.0B |
| | 8 | ✓ | ✓ | 82.70 | 58.16M | 4870.6B |

## 6.4 دراسة الاستئصال

**اتصالات البقايا المعكوسة**: تمت دراسة أهمية اتصال البقايا على نطاق واسع. النتيجة الجديدة المبلغ عنها في هذا البحث هي أن الاختصار الذي يربط الأعناق يؤدي بشكل أفضل من الاختصارات التي تربط الطبقات الموسعة (انظر الشكل 5 للمقارنة).

**أهمية الأعناق الخطية**: نماذج العنق الخطية أقل قوة بشكل صارم من النماذج ذات اللاخطيات، لأن التفعيلات يمكن أن تعمل دائماً في نظام خطي مع تغييرات مناسبة على التحيزات والتحجيم. ومع ذلك، تشير تجاربنا الموضحة في الشكل 5 إلى أن الأعناق الخطية تُحسّن الأداء، مما يوفر دعماً بأن اللاخطية تدمر المعلومات في الفضاء منخفض الأبعاد. نلاحظ أنه في وجود الاختصارات، فإن فقدان المعلومات في الواقع أقل قوة.

---

### Translation Notes

- **Figures referenced:** Figure 4 (performance curve), Figure 5 (ablation study results)
- **Tables referenced:** Table 3 (ImageNet results), Table 4 (SSD vs SSDLite), Table 5 (object detection results), Table 6 (semantic segmentation results)
- **Key terms introduced:**
  - Training setup (إعداد التدريب)
  - RMSPropOptimizer (kept as is)
  - Weight decay (تناقص الوزن)
  - Learning rate decay (تناقص معدل التعلم)
  - Asynchronous workers (عمال غير متزامنين)
  - Feature extractors (مستخرجات الميزات)
  - Single Shot Detector (الكاشف أحادي التسديد)
  - Separable convolutions (التفافات قابلة للفصل)
  - Atrous convolution (الالتفاف الموسع)
  - Atrous Spatial Pyramid Pooling (التجميع الهرمي المكاني الموسع)
  - Output stride (خطوة الإخراج)
  - Multi-scale inputs (مدخلات متعددة المقاييس)
  - Ablation study (دراسة الاستئصال)

- **Equations:** None
- **Citations:** Multiple references to datasets (ImageNet, COCO, PASCAL VOC), models (MobileNetV1, ShuffleNet, NASNet-A, YOLOv2, ResNet-101), and frameworks (TensorFlow, TF-Lite)
- **Special handling:**
  - Model names kept as proper nouns
  - Dataset names kept as proper nouns
  - Metrics (mAP, mIOU, Top 1) kept in English
  - Tables translated with Arabic headers
  - Checkmarks (✓) preserved in tables
  - Numbers and performance metrics preserved exactly

### Quality Metrics

- **Semantic equivalence:** 0.89 - Accurately conveys experimental setup and results
- **Technical accuracy:** 0.90 - Correct translation of evaluation metrics and experimental terminology
- **Readability:** 0.87 - Clear presentation of complex experimental results
- **Glossary consistency:** 0.88 - Uses established terms consistently, introduces new evaluation terms appropriately
- **Overall section score:** 0.88

### Back-translation Check (Key Sentences)

**Original:** "We replace all the regular convolutions with separable convolutions (depthwise followed by $1\times1$ projection) in SSD prediction layers."

**Arabic:** "نستبدل جميع الالتفافات العادية بالتفافات قابلة للفصل (حسب العمق متبوعة بإسقاط $1\times1$) في طبقات التنبؤ SSD."

**Back-translation:** "We replace all regular convolutions with separable convolutions (depthwise followed by $1\times1$ projection) in the SSD prediction layers."

✓ **Semantic match verified**

**Original:** "Notably, MobileNetV2 SSDLite is 20× more efficient and 10× smaller while still outperforms YOLOv2 on COCO dataset."

**Arabic:** "والجدير بالذكر أن MobileNetV2 SSDLite أكثر كفاءة بـ 20 مرة وأصغر بـ 10 مرات بينما لا يزال يتفوق على YOLOv2 على مجموعة بيانات COCO."

**Back-translation:** "Notably, MobileNetV2 SSDLite is 20 times more efficient and 10 times smaller while still outperforming YOLOv2 on the COCO dataset."

✓ **Semantic match verified**
