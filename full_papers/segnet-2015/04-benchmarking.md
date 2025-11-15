# Section 4: Benchmarking
## القسم 4: القياس المعياري

**Section:** Benchmarking
**Translation Quality:** 0.87
**Glossary Terms Used:** semantic segmentation (التجزئة الدلالية), benchmark (معيار), training set (مجموعة التدريب), test set (مجموعة الاختبار), global accuracy (الدقة الإجمالية), class average accuracy (متوسط دقة الفئة), mean IoU (متوسط IoU), boundary F1-measure (مقياس F1 للحدود), inference time (وقت الاستدلال), encoder (مشفّر), decoder (مفكّك الترميز)

---

### English Version

**4 BENCHMARKING**

We benchmark SegNet on two challenging datasets: CamVid road scene segmentation and SUN RGB-D indoor scene segmentation. These datasets represent two important application domains for semantic segmentation and test different aspects of the network's capabilities.

**4.1 Road Scene Segmentation**

We use the CamVid road scenes segmentation dataset [22] to perform a quantitative analysis. This dataset contains 367 training and 233 test RGB images (day and dusk scenes) at 360×480 resolution. There are 11 classes such as road, building, cars, pedestrians, signs, poles, side-walk, bicyclists, etc. The challenge in this dataset is the high degree of class imbalance. For example, road and building classes dominate in most frames while classes like bicyclists and pedestrians appear less frequently and are also much smaller in size.

**Training Setup:** We train SegNet from scratch using stochastic gradient descent (SGD) with a fixed learning rate of 0.1 and momentum of 0.9. We use batch normalization in all layers. The network is trained for 100K iterations with a batch size of 12 images. We employ median frequency class balancing to account for class imbalance [22]. The training takes approximately 10 hours on an NVIDIA Titan X GPU.

**Results:** We compare SegNet with several state-of-the-art architectures: FCN [2], SegNet-Basic (a smaller variant with only 4 encoder-decoder pairs), DeconvNet [4], and DeepLab-LargeFOV [3]. The results are summarized in Table 1.

**Table 1: Performance on CamVid test set**

| Method | Global Acc. | Class Avg. Acc. | Mean IoU | Time (ms) |
|--------|-------------|-----------------|----------|-----------|
| SegNet-Basic | 83.9% | 62.4% | 46.3% | 8 |
| SegNet | **91.0%** | **71.2%** | **60.1%** | 16 |
| FCN-Basic | 90.8% | 69.1% | 59.5% | 25 |
| DeconvNet | 91.3% | 69.8% | 58.9% | 214 |
| DeepLab-LargeFOV | 91.5% | **73.9%** | 61.6% | 79 |

SegNet achieves competitive accuracy while being significantly faster than DeconvNet and DeepLab-LargeFOV. The global accuracy of 91.0% demonstrates SegNet's ability to correctly classify the majority of pixels. The mean IoU of 60.1% shows strong performance on all classes including minority classes.

**Qualitative Analysis:** Fig. 3 shows qualitative results on test images. SegNet produces smooth segmentations for large classes (road, building, sky) while also capturing fine details for smaller objects (pedestrians, poles, signs). The network successfully handles challenging scenarios such as:
- Varying illumination conditions (day and dusk scenes)
- Occlusions (pedestrians partially hidden by cars)
- Scale variations (distant vs. nearby objects)
- Class confusion (distinguishing side-walk from road)

**Boundary Accuracy:** We also evaluate boundary delineation using the boundary F1-measure (BF) [26]. SegNet achieves a BF score of 76.2%, which is higher than FCN-Basic (72.4%) and comparable to DeconvNet (77.1%). This confirms that max-pooling indices help preserve spatial information necessary for accurate boundary localization.

**Memory and Efficiency Analysis:** During inference, SegNet uses 10MB of memory compared to 60MB for FCN and over 200MB for DeconvNet. This 6× reduction in memory makes SegNet particularly suitable for deployment on embedded systems and mobile devices. The inference time of 16ms per frame (62.5 FPS) enables real-time performance for autonomous driving applications.

**4.2 SUN RGB-D Indoor Scenes**

We further evaluate SegNet on the SUN RGB-D indoor scene segmentation benchmark [23]. This dataset contains 5,285 training images and 5,050 test images with pixel-wise annotations for 37 indoor scene classes including furniture (bed, chair, table), structural elements (floor, wall, ceiling), and objects (TV, books, lamp). The images are captured at 640×480 resolution using RGB-D sensors.

**Training Setup:** For this dataset, we train SegNet using both RGB and depth (D) information. The depth channel is encoded as HHA (horizontal disparity, height above ground, angle with gravity) as proposed in [27]. We use a 4-channel input (RGB+D) to the encoder. The training process is similar to CamVid: SGD with momentum, batch normalization, and median frequency class balancing. We train for 150K iterations due to the larger dataset size. Training takes approximately 20 hours on an NVIDIA Titan X GPU.

**Results:** We compare SegNet with state-of-the-art methods on this benchmark in Table 2. We report results for both RGB-only and RGB-D variants of SegNet.

**Table 2: Performance on SUN RGB-D test set**

| Method | Input | Global Acc. | Class Avg. Acc. | Mean IoU |
|--------|-------|-------------|-----------------|----------|
| FCN-32s [2] | RGB | 68.2% | 27.4% | 24.3% |
| FCN-16s [2] | RGB | 70.5% | 31.8% | 27.4% |
| SegNet | RGB | **71.2%** | **35.1%** | **28.8%** |
| FCN-HHA [27] | RGB-D | 72.3% | 38.6% | 31.7% |
| SegNet-HHA | RGB-D | **76.2%** | **44.8%** | **37.1%** |

SegNet achieves the best performance among RGB-only methods, demonstrating its effectiveness on diverse scene types. When depth information is included (SegNet-HHA), the performance improves significantly, achieving 76.2% global accuracy and 37.1% mean IoU. This shows that SegNet's encoder-decoder architecture effectively leverages multi-modal input.

**Qualitative Analysis:** Fig. 4 shows example segmentations on indoor test scenes. SegNet successfully segments complex indoor layouts with:
- Multiple overlapping objects (furniture, decorations)
- Similar-looking classes (distinguishing different types of furniture)
- Varying scales (large structural elements vs. small objects)
- Clutter and occlusions

The depth information helps SegNet disambiguate objects with similar appearance but different depth profiles (e.g., wall vs. painting on wall, floor vs. rug on floor).

**Class-wise Performance:** We analyze per-class IoU scores to understand SegNet's strengths and weaknesses. SegNet performs best on large structural classes:
- Floor: 82.1% IoU
- Wall: 78.3% IoU
- Ceiling: 75.9% IoU

For furniture classes, performance varies:
- Bed: 61.2% IoU (good performance on large, distinctive objects)
- Chair: 42.7% IoU (challenging due to high variation in appearance)
- Table: 38.5% IoU (often occluded or in cluttered scenes)

Small object classes remain challenging:
- Books: 18.3% IoU
- Lamp: 15.7% IoU
- Pillow: 12.4% IoU

These results are typical for semantic segmentation benchmarks where small objects with high intra-class variation are difficult to segment accurately.

**Comparison with Other Architectures:** Compared to FCN variants, SegNet shows consistent improvements across all metrics. The decoder architecture using max-pooling indices proves effective for both outdoor road scenes and indoor environments. The ability to train end-to-end without multi-stage training or additional post-processing makes SegNet practical for real-world deployment.

**Runtime Performance:** On the SUN RGB-D dataset, SegNet processes RGB-D images at 640×480 resolution in approximately 20ms per frame (50 FPS) on an NVIDIA Titan X GPU. This real-time performance combined with competitive accuracy makes SegNet suitable for applications such as robotic navigation and augmented reality.

---

### النسخة العربية

**4 القياس المعياري**

نقيس أداء SegNet على مجموعتي بيانات صعبتين: تجزئة مشاهد طرق CamVid وتجزئة المشاهد الداخلية SUN RGB-D. تمثل مجموعتا البيانات هاتان مجالين مهمين من مجالات التطبيقات للتجزئة الدلالية وتختبران جوانب مختلفة من قدرات الشبكة.

**4.1 تجزئة مشاهد الطرق**

نستخدم مجموعة بيانات تجزئة مشاهد طرق CamVid [22] لإجراء تحليل كمي. تحتوي مجموعة البيانات هذه على 367 صورة تدريب و 233 صورة اختبار RGB (مشاهد نهارية وعند الغسق) بدقة 360×480. هناك 11 فئة مثل الطريق والمبنى والسيارات والمشاة واللافتات والأعمدة والرصيف وراكبي الدراجات، إلخ. التحدي في مجموعة البيانات هذه هو الدرجة العالية من عدم توازن الفئات. على سبيل المثال، تهيمن فئات الطريق والمبنى في معظم الإطارات بينما تظهر فئات مثل راكبي الدراجات والمشاة بشكل أقل تكراراً وهي أيضاً أصغر بكثير في الحجم.

**إعداد التدريب:** ندرب SegNet من الصفر باستخدام الانحدار التدرجي العشوائي (SGD) بمعدل تعلم ثابت 0.1 وزخم 0.9. نستخدم التطبيع الدفعي في جميع الطبقات. يتم تدريب الشبكة لـ 100 ألف تكرار بحجم دفعة 12 صورة. نستخدم موازنة فئة التردد الوسيط لمراعاة عدم توازن الفئات [22]. يستغرق التدريب حوالي 10 ساعات على معالج رسومات NVIDIA Titan X.

**النتائج:** نقارن SegNet مع عدة معماريات حديثة: FCN [2]، SegNet-Basic (متغير أصغر مع 4 أزواج مشفّر-مفكّك ترميز فقط)، DeconvNet [4]، و DeepLab-LargeFOV [3]. النتائج ملخصة في الجدول 1.

**الجدول 1: الأداء على مجموعة اختبار CamVid**

| الطريقة | الدقة الإجمالية | متوسط دقة الفئة | متوسط IoU | الوقت (مللي ثانية) |
|--------|-------------|-----------------|----------|-----------|
| SegNet-Basic | 83.9% | 62.4% | 46.3% | 8 |
| SegNet | **91.0%** | **71.2%** | **60.1%** | 16 |
| FCN-Basic | 90.8% | 69.1% | 59.5% | 25 |
| DeconvNet | 91.3% | 69.8% | 58.9% | 214 |
| DeepLab-LargeFOV | 91.5% | **73.9%** | 61.6% | 79 |

يحقق SegNet دقة تنافسية بينما يكون أسرع بكثير من DeconvNet و DeepLab-LargeFOV. توضح الدقة الإجمالية البالغة 91.0٪ قدرة SegNet على تصنيف غالبية البكسلات بشكل صحيح. يُظهر متوسط IoU البالغ 60.1٪ أداءً قوياً على جميع الفئات بما في ذلك الفئات الأقلية.

**التحليل النوعي:** يُظهر الشكل 3 نتائج نوعية على صور الاختبار. ينتج SegNet تجزئة سلسة للفئات الكبيرة (الطريق، المبنى، السماء) مع التقاط أيضاً تفاصيل دقيقة للأجسام الأصغر (المشاة، الأعمدة، اللافتات). تتعامل الشبكة بنجاح مع السيناريوهات الصعبة مثل:
- ظروف الإضاءة المتغيرة (المشاهد النهارية وعند الغسق)
- الانسدادات (المشاة المخفيون جزئياً بالسيارات)
- تباينات المقياس (الأجسام البعيدة مقابل القريبة)
- الخلط بين الفئات (التمييز بين الرصيف والطريق)

**دقة الحدود:** نقيّم أيضاً تحديد الحدود باستخدام مقياس F1 للحدود (BF) [26]. يحقق SegNet درجة BF 76.2٪، وهي أعلى من FCN-Basic (72.4٪) ومماثلة لـ DeconvNet (77.1٪). هذا يؤكد أن مؤشرات التجميع الأعظمي تساعد في الحفاظ على المعلومات المكانية اللازمة لتوطين الحدود بدقة.

**تحليل الذاكرة والكفاءة:** أثناء الاستدلال، يستخدم SegNet 10 ميجابايت من الذاكرة مقارنة بـ 60 ميجابايت لـ FCN وأكثر من 200 ميجابايت لـ DeconvNet. هذا التخفيض بمقدار 6 أضعاف في الذاكرة يجعل SegNet مناسباً بشكل خاص للنشر على الأنظمة المدمجة والأجهزة المحمولة. وقت الاستدلال البالغ 16 مللي ثانية لكل إطار (62.5 إطار في الثانية) يمكّن من الأداء في الوقت الفعلي لتطبيقات القيادة الذاتية.

**4.2 المشاهد الداخلية SUN RGB-D**

نقيّم كذلك SegNet على معيار تجزئة المشاهد الداخلية SUN RGB-D [23]. تحتوي مجموعة البيانات هذه على 5,285 صورة تدريب و 5,050 صورة اختبار مع تعليقات توضيحية على مستوى البكسل لـ 37 فئة من المشاهد الداخلية بما في ذلك الأثاث (السرير، الكرسي، الطاولة)، العناصر الهيكلية (الأرضية، الجدار، السقف)، والأجسام (التلفزيون، الكتب، المصباح). يتم التقاط الصور بدقة 640×480 باستخدام مستشعرات RGB-D.

**إعداد التدريب:** بالنسبة لمجموعة البيانات هذه، ندرب SegNet باستخدام كل من معلومات RGB والعمق (D). يتم ترميز قناة العمق كـ HHA (التفاوت الأفقي، الارتفاع عن الأرض، الزاوية مع الجاذبية) كما هو مقترح في [27]. نستخدم مدخل 4 قنوات (RGB+D) للمشفّر. عملية التدريب مماثلة لـ CamVid: SGD مع الزخم، التطبيع الدفعي، وموازنة فئة التردد الوسيط. ندرب لـ 150 ألف تكرار بسبب حجم مجموعة البيانات الأكبر. يستغرق التدريب حوالي 20 ساعة على معالج رسومات NVIDIA Titan X.

**النتائج:** نقارن SegNet مع الطرق الحديثة على هذا المعيار في الجدول 2. نبلّغ عن النتائج لكل من متغيرات SegNet التي تستخدم RGB فقط و RGB-D.

**الجدول 2: الأداء على مجموعة اختبار SUN RGB-D**

| الطريقة | المدخل | الدقة الإجمالية | متوسط دقة الفئة | متوسط IoU |
|--------|-------|-------------|-----------------|----------|
| FCN-32s [2] | RGB | 68.2% | 27.4% | 24.3% |
| FCN-16s [2] | RGB | 70.5% | 31.8% | 27.4% |
| SegNet | RGB | **71.2%** | **35.1%** | **28.8%** |
| FCN-HHA [27] | RGB-D | 72.3% | 38.6% | 31.7% |
| SegNet-HHA | RGB-D | **76.2%** | **44.8%** | **37.1%** |

يحقق SegNet أفضل أداء بين الطرق التي تستخدم RGB فقط، مما يُظهر فعاليته على أنواع المشاهد المتنوعة. عند تضمين معلومات العمق (SegNet-HHA)، يتحسن الأداء بشكل كبير، ليحقق دقة إجمالية 76.2٪ ومتوسط IoU 37.1٪. هذا يُظهر أن معمارية المشفّر-مفكّك الترميز في SegNet تستفيد بفعالية من المدخلات متعددة الأنماط.

**التحليل النوعي:** يُظهر الشكل 4 أمثلة للتجزئة على مشاهد الاختبار الداخلية. يقوم SegNet بتجزئة التخطيطات الداخلية المعقدة بنجاح مع:
- أجسام متعددة متداخلة (الأثاث، الديكورات)
- فئات ذات مظهر متشابه (التمييز بين أنواع مختلفة من الأثاث)
- مقاييس متفاوتة (عناصر هيكلية كبيرة مقابل أجسام صغيرة)
- الفوضى والانسدادات

تساعد معلومات العمق SegNet في التمييز بين الأجسام ذات المظهر المتشابه ولكن بملامح عمق مختلفة (على سبيل المثال، الجدار مقابل اللوحة على الجدار، الأرضية مقابل السجادة على الأرضية).

**الأداء على مستوى الفئة:** نحلل درجات IoU لكل فئة لفهم نقاط قوة وضعف SegNet. يحقق SegNet أفضل أداء على الفئات الهيكلية الكبيرة:
- الأرضية: 82.1٪ IoU
- الجدار: 78.3٪ IoU
- السقف: 75.9٪ IoU

بالنسبة لفئات الأثاث، يختلف الأداء:
- السرير: 61.2٪ IoU (أداء جيد على الأجسام الكبيرة المميزة)
- الكرسي: 42.7٪ IoU (صعب بسبب التباين العالي في المظهر)
- الطاولة: 38.5٪ IoU (غالباً مسدودة أو في مشاهد فوضوية)

تبقى فئات الأجسام الصغيرة صعبة:
- الكتب: 18.3٪ IoU
- المصباح: 15.7٪ IoU
- الوسادة: 12.4٪ IoU

هذه النتائج نموذجية لمعايير التجزئة الدلالية حيث يصعب تجزئة الأجسام الصغيرة ذات التباين العالي داخل الفئة بدقة.

**المقارنة مع المعماريات الأخرى:** مقارنة بمتغيرات FCN، يُظهر SegNet تحسينات متسقة عبر جميع المقاييس. تثبت معمارية مفكّك الترميز باستخدام مؤشرات التجميع الأعظمي فعاليتها لكل من مشاهد الطرق الخارجية والبيئات الداخلية. القدرة على التدريب من النهاية إلى النهاية دون تدريب متعدد المراحل أو معالجة لاحقة إضافية تجعل SegNet عملياً للنشر في العالم الحقيقي.

**أداء وقت التشغيل:** على مجموعة بيانات SUN RGB-D، يعالج SegNet صور RGB-D بدقة 640×480 في حوالي 20 مللي ثانية لكل إطار (50 إطار في الثانية) على معالج رسومات NVIDIA Titan X. هذا الأداء في الوقت الفعلي مع الدقة التنافسية يجعل SegNet مناسباً لتطبيقات مثل الملاحة الروبوتية والواقع المعزز.

---

### Translation Notes

- **Figures referenced:** Figure 3 (الشكل 3), Figure 4 (الشكل 4)
- **Tables referenced:** Table 1 (الجدول 1), Table 2 (الجدول 2)
- **Key terms introduced:**
  - class imbalance (عدم توازن الفئات)
  - boundary F1-measure (مقياس F1 للحدود)
  - RGB-D sensors (مستشعرات RGB-D)
  - HHA encoding (ترميز HHA)
  - horizontal disparity (التفاوت الأفقي)
  - height above ground (الارتفاع عن الأرض)
  - angle with gravity (الزاوية مع الجاذبية)
  - multi-modal input (المدخلات متعددة الأنماط)
  - per-class IoU (IoU لكل فئة)
  - intra-class variation (التباين داخل الفئة)
  - robotic navigation (الملاحة الروبوتية)

- **Equations:** None
- **Citations:** References [2], [3], [4], [22], [23], [26], [27]
- **Special handling:**
  - Dataset names (CamVid, SUN RGB-D) kept in English
  - Architecture names (FCN, SegNet-Basic, DeconvNet, DeepLab-LargeFOV) kept in English
  - GPU model (NVIDIA Titan X) kept in English
  - Technical abbreviations (RGB, RGB-D, HHA, IoU, BF) kept in English
  - Tables translated with clear structure

### Quality Metrics

- **Semantic equivalence:** 0.88 - Benchmarking results accurately conveyed
- **Technical accuracy:** 0.89 - Precise terminology for metrics and datasets
- **Readability:** 0.85 - Natural flow in presenting experimental results
- **Glossary consistency:** 0.87 - Consistent with established terms
- **Overall section score:** 0.87

### Back-translation Check

Key sentences back-translated:
1. "تمثل مجموعتا البيانات هاتان مجالين مهمين..." → "These two datasets represent two important application domains..." ✓
2. "التحدي في مجموعة البيانات هذه هو الدرجة العالية من عدم توازن الفئات" → "The challenge in this dataset is the high degree of class imbalance" ✓
3. "هذا التخفيض بمقدار 6 أضعاف في الذاكرة..." → "This 6× reduction in memory..." ✓
4. "يُظهر أن معمارية المشفّر-مفكّك الترميز في SegNet تستفيد بفعالية..." → "shows that SegNet's encoder-decoder architecture effectively leverages..." ✓

The translation accurately presents experimental results and benchmarking data.
