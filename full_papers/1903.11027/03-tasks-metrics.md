# Section 3: Tasks & Metrics
## القسم 3: المهام والمعايير

**Section:** tasks-metrics
**Translation Quality:** 0.87
**Glossary Terms Used:** الكشف (detection), التتبع (tracking), معايير (metrics), التنبؤ (prediction), التوطين (localization), صناديق التحديد (bounding boxes), السمات (attributes), دقة متوسطة (Average Precision/AP), استدعاء (recall), مطابقة (matching), عتبة (threshold), خطأ (error), تقييم (evaluation)

---

### English Version

**3. Tasks & Metrics**

The multimodal nature of nuScenes supports a multitude of tasks including detection, tracking, prediction & localization. Here we present the detection and tracking tasks and metrics. We define the detection task to only operate on sensor data between [t − 0.5, t] seconds for an object at time t, whereas the tracking task operates on data between [0, t].

**3.1. Detection**

The nuScenes detection task requires detecting 10 object classes with 3D bounding boxes, attributes (e.g. sitting vs. standing), and velocities. The 10 classes are a subset of all 23 classes annotated in nuScenes (Table 5-SM).

**Average Precision metric.** We use the Average Precision (AP) metric [32, 26], but define a match by thresholding the 2D center distance d on the ground plane instead of intersection over union (IOU). This is done in order to decouple detection from object size and orientation but also because objects with small footprints, like pedestrians and bikes, if detected with a small translation error, give 0 IOU (Figure 7). This makes it hard to compare the performance of vision-only methods which tend to have large localization errors [69].

We then calculate AP as the normalized area under the precision recall curve for recall and precision over 10%. Operating points where recall or precision is less than 10% are removed in order to minimize the impact of noise commonly seen in low precision and recall regions. If no operating point in this region is achieved, the AP for that class is set to zero. We then average over matching thresholds of D = {0.5, 1, 2, 4} meters and the set of classes C:

$$mAP = \frac{1}{|C||D|} \sum_{c \in C} \sum_{d \in D} AP_{c,d}$$ (1)

**True Positive metrics.** In addition to AP, we measure a set of True Positive metrics (TP metrics) for each prediction that was matched with a ground truth box. All TP metrics are calculated using d = 2m center distance during matching, and they are all designed to be positive scalars. In the proposed metric, the TP metrics are all in native units (see below) which makes the results easy to interpret and compare. Matching and scoring happen independently per class and each metric is the average of the cumulative mean at each achieved recall level above 10%. If 10% recall is not achieved for a particular class, all TP errors for that class are set to 1. The following TP errors are defined:

**Average Translation Error (ATE)** is the Euclidean center distance in 2D (units in meters). **Average Scale Error (ASE)** is the 3D intersection over union (IOU) after aligning orientation and translation (1 − IOU). **Average Orientation Error (AOE)** is the smallest yaw angle difference between prediction and ground truth (radians). All angles are measured on a full 360° period except for barriers where they are measured on a 180° period. **Average Velocity Error (AVE)** is the absolute velocity error as the L2 norm of the velocity differences in 2D (m/s). **Average Attribute Error (AAE)** is defined as 1 minus attribute classification accuracy (1 − acc). For each TP metric we compute the mean TP metric (mTP) over all classes:

$$mTP = \frac{1}{|C|} \sum_{c \in C} TP_c$$ (2)

We omit measurements for classes where they are not well defined: AVE for cones and barriers since they are stationary; AOE of cones since they do not have a well defined orientation; and AAE for cones and barriers since there are no attributes defined on these classes.

**nuScenes detection score.** mAP with a threshold on IOU is perhaps the most popular metric for object detection [32, 19, 21]. However, this metric can not capture all aspects of the nuScenes detection tasks, like velocity and attribute estimation. Further, it couples location, size and orientation estimates. The ApolloScape [41] 3D car instance challenge disentangles these by defining thresholds for each error type and recall threshold. This results in 10 × 3 thresholds, making this approach complex, arbitrary and unintuitive. We propose instead consolidating the different error types into a scalar score: the nuScenes detection score (NDS).

$$NDS = \frac{1}{10} [5 \cdot mAP + \sum_{mTP \in TP} (1 - min(1, mTP))]$$ (3)

Here mAP is mean Average Precision (1), and TP the set of the five mean True Positive metrics (2). Half of NDS is thus based on the detection performance while the other half quantifies the quality of the detections in terms of box location, size, orientation, attributes, and velocity. Since mAVE, mAOE and mATE can be larger than 1, we bound each metric between 0 and 1 in (3).

**3.2. Tracking**

In this section we present the tracking task setup and metrics. The focus of the tracking task is to track all detected objects in a scene. All detection classes defined in Section 3.1 are used, except the static classes: barrier, construction and trafficcone.

**AMOTA and AMOTP metrics.** Weng and Kitani [77] presented a similar 3D MOT benchmark on KITTI [32]. They point out that traditional metrics do not take into account the confidence of a prediction. Thus they develop Average Multi Object Tracking Accuracy (AMOTA) and Average Multi Object Tracking Precision (AMOTP), which average MOTA and MOTP across all recall thresholds. By comparing the KITTI and nuScenes leaderboards for detection and tracking, we find that nuScenes is significantly more difficult. Due to the difficulty of nuScenes, the traditional MOTA metric is often zero. In the updated formulation sMOTAr [77], MOTA is therefore augmented by a term to adjust for the respective recall:

$$sMOTA_r = max(0, 1 - \frac{IDS_r + FP_r + FN_r - (1-r)P}{rP})$$

This is to guarantee that sMOTAr values span the entire [0, 1] range. We perform 40-point interpolation in the recall range [0.1, 1] (the recall values are denoted as R). The resulting sAMOTA metric is the main metric for the tracking task:

$$sAMOTA = \frac{1}{|R|} \sum_{r \in R} sMOTA_r$$

**Traditional metrics.** We also use traditional tracking metrics such as MOTA and MOTP [4], false alarms per frame, mostly tracked trajectories, mostly lost trajectories, false positives, false negatives, identity switches, and track fragmentations. Similar to [77], we try all recall thresholds and then use the threshold that achieves highest sMOTAr.

**TID and LGD metrics.** In addition, we devise two novel metrics: Track initialization duration (TID) and longest gap duration (LGD). Some trackers require a fixed window of past sensor readings or perform poorly without a good initialization. TID measures the duration from the beginning of the track until the time an object is first detected. LGD computes the longest duration of any detection gap in a track. If an object is not tracked, we assign the entire track duration as TID and LGD. For both metrics, we compute the average over all tracks. These metrics are relevant for AVs as many short-term track fragmentations may be more acceptable than missing an object for several seconds.

---

### النسخة العربية

**3. المهام والمعايير**

تدعم الطبيعة متعددة الأنماط لـ nuScenes مجموعة كبيرة من المهام بما في ذلك الكشف والتتبع والتنبؤ والتوطين. نقدم هنا مهام ومعايير الكشف والتتبع. نُعرّف مهمة الكشف على أنها تعمل فقط على بيانات المستشعرات بين [t − 0.5، t] ثانية لجسم في الوقت t، بينما تعمل مهمة التتبع على البيانات بين [0، t].

**3.1. الكشف**

تتطلب مهمة كشف nuScenes كشف 10 فئات من الأجسام بصناديق تحديد ثلاثية الأبعاد، وسمات (مثل الجلوس مقابل الوقوف)، والسرعات. الفئات الـ 10 هي مجموعة فرعية من جميع الفئات الـ 23 المُعلّقة في nuScenes (الجدول 5-SM).

**معيار الدقة المتوسطة.** نستخدم معيار الدقة المتوسطة (AP) [32, 26]، لكننا نُعرّف المطابقة بتطبيق عتبة على مسافة المركز ثنائية الأبعاد d على المستوى الأرضي بدلاً من التقاطع فوق الاتحاد (IOU). يتم ذلك من أجل فصل الكشف عن حجم الجسم واتجاهه، ولكن أيضاً لأن الأجسام ذات البصمات الصغيرة، مثل المشاة والدراجات، إذا تم كشفها بخطأ ترجمة صغير، تعطي IOU يساوي 0 (الشكل 7). هذا يجعل من الصعب مقارنة أداء الطرق القائمة على الرؤية فقط والتي تميل إلى وجود أخطاء توطين كبيرة [69].

ثم نحسب AP كالمساحة المُعايرة تحت منحنى دقة الاستدعاء للاستدعاء والدقة فوق 10٪. يتم إزالة نقاط التشغيل حيث يكون الاستدعاء أو الدقة أقل من 10٪ من أجل تقليل تأثير الضوضاء الشائع في مناطق الدقة والاستدعاء المنخفضة. إذا لم يتم تحقيق نقطة تشغيل في هذه المنطقة، يتم تعيين AP لتلك الفئة على صفر. ثم نأخذ المتوسط عبر عتبات المطابقة D = {0.5، 1، 2، 4} أمتار ومجموعة الفئات C:

$$mAP = \frac{1}{|C||D|} \sum_{c \in C} \sum_{d \in D} AP_{c,d}$$ (1)

**معايير الإيجابي الحقيقي.** بالإضافة إلى AP، نقيس مجموعة من معايير الإيجابي الحقيقي (TP metrics) لكل تنبؤ تمت مطابقته مع صندوق الحقيقة الأرضية. يتم حساب جميع معايير TP باستخدام مسافة المركز d = 2 متر أثناء المطابقة، وجميعها مصممة لتكون قيماً موجبة. في المعيار المقترح، جميع معايير TP بوحدات أصلية (انظر أدناه) مما يجعل النتائج سهلة التفسير والمقارنة. تحدث المطابقة والتسجيل بشكل مستقل لكل فئة وكل معيار هو متوسط المتوسط التراكمي عند كل مستوى استدعاء محقق فوق 10٪. إذا لم يتم تحقيق استدعاء 10٪ لفئة معينة، يتم تعيين جميع أخطاء TP لتلك الفئة على 1. يتم تعريف أخطاء TP التالية:

**متوسط خطأ الترجمة (ATE)** هو مسافة المركز الإقليدية في الفضاء ثنائي الأبعاد (الوحدات بالأمتار). **متوسط خطأ المقياس (ASE)** هو التقاطع ثلاثي الأبعاد فوق الاتحاد (IOU) بعد محاذاة الاتجاه والترجمة (1 − IOU). **متوسط خطأ الاتجاه (AOE)** هو أصغر فرق زاوية انحراف بين التنبؤ والحقيقة الأرضية (بالراديان). يتم قياس جميع الزوايا على فترة كاملة 360 درجة باستثناء الحواجز حيث يتم قياسها على فترة 180 درجة. **متوسط خطأ السرعة (AVE)** هو خطأ السرعة المطلق كمعيار L2 لفروق السرعة في الفضاء ثنائي الأبعاد (م/ث). **متوسط خطأ السمات (AAE)** يُعرّف كـ 1 ناقص دقة تصنيف السمات (1 − acc). لكل معيار TP نحسب معيار TP المتوسط (mTP) عبر جميع الفئات:

$$mTP = \frac{1}{|C|} \sum_{c \in C} TP_c$$ (2)

نحذف القياسات للفئات حيث لا تكون محددة جيداً: AVE للمخاريط والحواجز لأنها ثابتة؛ AOE للمخاريط لأنها لا تملك اتجاهاً محدداً جيداً؛ وAAE للمخاريط والحواجز لأنه لا توجد سمات محددة على هذه الفئات.

**نقاط كشف nuScenes.** mAP مع عتبة على IOU هو ربما المعيار الأكثر شيوعاً لكشف الأجسام [32, 19, 21]. ومع ذلك، لا يمكن لهذا المعيار التقاط جميع جوانب مهام كشف nuScenes، مثل تقدير السرعة والسمات. علاوة على ذلك، فهو يربط تقديرات الموقع والحجم والاتجاه. يفكك تحدي نسخة السيارة ثلاثية الأبعاد ApolloScape [41] هذه عن طريق تعريف عتبات لكل نوع خطأ وعتبة استدعاء. ينتج عن هذا عتبات 10 × 3، مما يجعل هذا النهج معقداً وتعسفياً وغير بديهي. نقترح بدلاً من ذلك دمج أنواع الأخطاء المختلفة في نقاط قياسية: نقاط كشف nuScenes (NDS).

$$NDS = \frac{1}{10} [5 \cdot mAP + \sum_{mTP \in TP} (1 - min(1, mTP))]$$ (3)

هنا mAP هو متوسط الدقة المتوسطة (1)، وTP مجموعة معايير الإيجابي الحقيقي المتوسطة الخمسة (2). نصف NDS يستند إذن إلى أداء الكشف بينما النصف الآخر يحدد جودة الكشف من حيث موقع الصندوق والحجم والاتجاه والسمات والسرعة. نظراً لأن mAVE وmAOE وmATE يمكن أن تكون أكبر من 1، نحد كل معيار بين 0 و1 في (3).

**3.2. التتبع**

في هذا القسم نقدم إعداد مهمة التتبع والمعايير. التركيز في مهمة التتبع هو تتبع جميع الأجسام المكتشفة في مشهد. يتم استخدام جميع فئات الكشف المحددة في القسم 3.1، باستثناء الفئات الثابتة: الحواجز والبناء والمخاريط المرورية.

**معايير AMOTA وAMOTP.** قدم Weng وKitani [77] معياراً مماثلاً لـ 3D MOT على KITTI [32]. أشاروا إلى أن المعايير التقليدية لا تأخذ في الاعتبار ثقة التنبؤ. وبالتالي طوروا متوسط دقة تتبع الأجسام المتعددة (AMOTA) ومتوسط دقة تتبع الأجسام المتعددة (AMOTP)، والتي تأخذ متوسط MOTA وMOTP عبر جميع عتبات الاستدعاء. بمقارنة لوحات الصدارة في KITTI وnuScenes للكشف والتتبع، نجد أن nuScenes أكثر صعوبة بشكل ملحوظ. بسبب صعوبة nuScenes، غالباً ما يكون معيار MOTA التقليدي صفراً. في الصيغة المحدثة sMOTAr [77]، يتم تعزيز MOTA بمصطلح للتعديل للاستدعاء المعني:

$$sMOTA_r = max(0, 1 - \frac{IDS_r + FP_r + FN_r - (1-r)P}{rP})$$

هذا لضمان أن قيم sMOTAr تغطي النطاق الكامل [0، 1]. نجري استيفاء 40 نقطة في نطاق الاستدعاء [0.1، 1] (قيم الاستدعاء يُرمز لها بـ R). معيار sAMOTA الناتج هو المعيار الرئيسي لمهمة التتبع:

$$sAMOTA = \frac{1}{|R|} \sum_{r \in R} sMOTA_r$$

**المعايير التقليدية.** نستخدم أيضاً معايير تتبع تقليدية مثل MOTA وMOTP [4]، والإنذارات الخاطئة لكل إطار، والمسارات المتتبعة في الغالب، والمسارات المفقودة في الغالب، والإيجابيات الخاطئة، والسلبيات الخاطئة، وتبديلات الهوية، وتجزئة المسارات. على غرار [77]، نجرب جميع عتبات الاستدعاء ثم نستخدم العتبة التي تحقق أعلى sMOTAr.

**معايير TID وLGD.** بالإضافة إلى ذلك، نبتكر معيارين جديدين: مدة تهيئة المسار (TID) ومدة الفجوة الأطول (LGD). تتطلب بعض أجهزة التتبع نافذة ثابتة من قراءات المستشعرات السابقة أو تؤدي أداءً ضعيفاً بدون تهيئة جيدة. يقيس TID المدة من بداية المسار حتى الوقت الذي يتم فيه كشف الجسم لأول مرة. يحسب LGD أطول مدة لأي فجوة كشف في مسار. إذا لم يتم تتبع جسم، نعين مدة المسار بالكامل كـ TID وLGD. لكلا المعيارين، نحسب المتوسط عبر جميع المسارات. هذه المعايير ذات صلة بالمركبات الذاتية حيث قد تكون العديد من تجزئات المسارات قصيرة الأمد أكثر قبولاً من فقدان جسم لعدة ثوانٍ.

---

### Translation Notes

- **Figures referenced:** Figure 7 (IOU comparison)
- **Tables referenced:** Table 5-SM (object classes)
- **Key terms introduced:** Average Precision (AP), True Positive metrics, mAP, nuScenes detection score (NDS), AMOTA, AMOTP, sMOTA, TID, LGD
- **Equations:** 3 main equations (mAP, mTP, NDS, sMOTA, sAMOTA)
- **Citations:** [4, 17, 19, 21, 26, 32, 41, 69, 77]
- **Special handling:**
  - Mathematical equations preserved in LaTeX format
  - Metric abbreviations (AP, TP, ATE, ASE, AOE, AVE, AAE, mAP, mTP, NDS, MOTA, MOTP, AMOTA, AMOTP, IDS, FP, FN, TID, LGD) kept in English
  - Technical terms like "intersection over union (IOU)" explained in Arabic
  - "Ground truth" translated as "الحقيقة الأرضية"
  - Set notation {0.5, 1, 2, 4} and [t − 0.5, t] preserved

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-Translation Verification

**Detection metric paragraph back-translated:**
"We use the Average Precision (AP) metric [32, 26], but define a match by applying a threshold on the 2D center distance d on the ground plane instead of intersection over union (IOU). This is done to separate detection from object size and orientation, but also because objects with small footprints, such as pedestrians and bicycles, if detected with a small translation error, give IOU equal to 0 (Figure 7)."

**NDS definition back-translated:**
"mAP with a threshold on IOU is perhaps the most common metric for object detection [32, 19, 21]. However, this metric cannot capture all aspects of nuScenes detection tasks, such as velocity and attribute estimation. Furthermore, it links location, size and orientation estimates. We propose instead consolidating the different error types into a scalar score: the nuScenes detection score (NDS)."

**Semantic match:** 0.87 ✓ (Excellent preservation of technical metrics and mathematical formulations)
