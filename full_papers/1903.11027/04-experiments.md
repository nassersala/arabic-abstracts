# Section 4: Experiments
## القسم 4: التجارب

**Section:** experiments
**Translation Quality:** 0.86
**Glossary Terms Used:** الكشف (detection), التتبع (tracking), خطوط الأساس (baselines), ليدار (lidar), الكاميرا (camera), سحب النقاط (point clouds), التدريب (training), التقييم (evaluation), دقة (precision), استدعاء (recall), الأداء (performance), التدريب المسبق (pre-training), معايير (metrics), مجموعة بيانات (dataset)

---

### English Version

**4. Experiments**

In this section we present object detection and tracking experiments on the nuScenes dataset, analyze their characteristics and suggest avenues for future research.

**4.1. Baselines**

We present a number of baselines with different modalities for detection and tracking.

**Lidar detection baseline.** To demonstrate the performance of a leading algorithm on nuScenes, we train a lidar-only 3D object detector, PointPillars [51]. We take advantage of temporal data available in nuScenes by accumulating lidar sweeps for a richer pointcloud as input. A single network was trained for all classes. The network was modified to also learn velocities as an additional regression target for each 3D box. We set the box attributes to the most common attribute for each class in the training data.

**Image detection baseline.** To examine image-only 3D object detection, we re-implement the Orthographic Feature Transform (OFT) [69] method. A single OFT network was used for all classes. We modified the original OFT to use a SSD detection head and confirmed that this matched published results on KITTI. The network takes in a single image from which the full 360° predictions are combined together from all 6 cameras using non-maximum suppression (NMS). We set the box velocity to zero and attributes to the most common attribute for each class in the train data.

**Detection challenge results.** We compare the results of the top submissions to the nuScenes detection challenge 2019. Among all submissions, Megvii [90] gave the best performance. It is a lidar based class-balanced multi-head network with sparse 3D convolutions. Among image-only submissions, MonoDIS [70] was the best, significantly outperforming our image baseline and even some lidar based methods. It uses a novel disentangling 2D and 3D detection loss. Note that the top methods all performed importance sampling, which shows the importance of addressing the class imbalance problem.

**Tracking baselines.** We present several baselines for tracking from camera and lidar data. From the detection challenge, we pick the best performing lidar method (Megvii [90]), the fastest reported method at inference time (PointPillars [51]), as well as the best performing camera method (MonoDIS [70]). Using the detections from each method, we setup baselines using the tracking approach described in [77]. We provide detection and tracking results for each of these methods on the train, val and test splits to facilitate more systematic research. See the Supplementary Material for the results of the 2019 nuScenes tracking challenge.

**4.2. Analysis**

Here we analyze the properties of the methods presented in Section 4.1, as well as the dataset and matching function.

**The case for a large benchmark dataset.** One of the contributions of nuScenes is the dataset size, and in particular the increase compared to KITTI (Table 1). Here we examine the benefits of the larger dataset size. We train PointPillars [51], OFT [69] and an additional image baseline, SSD+3D, with varying amounts of training data. SSD+3D has the same 3D parametrization as MonoDIS [70], but use a single stage design [53]. For this ablation study we train PointPillars with 6x fewer epochs and a one cycle optimizer schedule [71] to cut down the training time. Our main finding is that the method ordering changes with the amount of data (Figure 6). In particular, PointPillars performs similar to SSD+3D at data volumes commensurate with KITTI, but as more data is used, it is clear that PointPillars is stronger. This suggests that the full potential of complex algorithms can only be verified with a bigger and more diverse training set. A similar conclusion was reached by [56, 59] with [59] suggesting that the KITTI leaderboard reflects the data aug. method rather than the actual algorithms.

**The importance of the matching function.** We compare performance of published methods (Table 4) when using our proposed 2m center-distance matching versus the IOU matching used in KITTI. As expected, when using IOU matching, small objects like pedestrians and bicycles fail to achieve above 0 AP, making ordering impossible (Figure 7). In contrast, center distance matching declares MonoDIS a clear winner. The impact is smaller for the car class, but also in this case it is hard to resolve the difference between MonoDIS and OFT.

The matching function also changes the balance between lidar and image based methods. In fact, the ordering switches when using center distance matching to favour MonoDIS over both lidar based methods on the bicycle class (Figure 7). This makes sense since the thin structures of bicycles make them difficult to detect in lidar. We conclude that center distance matching is more appropriate to rank image based methods alongside lidar based methods.

**Multiple lidar sweeps improve performance.** According to our evaluation protocol (Section 3.1), one is only allowed to use 0.5s of previous data to make a detection decision. This corresponds to 10 previous lidar sweeps since the lidar is sampled at 20Hz. We device a simple way of incorporating multiple pointclouds into the PointPillars baseline and investigate the performance impact. Accumulation is implemented by moving all pointclouds to the coordinate system of the keyframe and appending a scalar time-stamp to each point indicating the time delta in seconds from the keyframe. The encoder includes the time delta as an extra decoration for the lidar points. Aside from the advantage of richer pointclouds, this also provides temporal information, which helps the network in localization and enables velocity prediction. We experiment with using 1, 5, and 10 lidar sweeps. The results show that both detection and velocity estimates improve with an increasing number of lidar sweeps but with diminishing rate of return (Table 3).

**Which sensor is most important?** An important question for AVs is which sensors are required to achieve the best detection performance. Here we compare the performance of leading lidar and image detectors. We focus on these modalities as there are no competitive radar-only methods in the literature and our preliminary study with PointPillars on radar data did not achieve promising results. We compare PointPillars, which is a fast and light lidar detector with MonoDIS, a top image detector (Table 4). The two methods achieve similar mAP (30.5% vs. 30.4%), but PointPillars has higher NDS (45.3% vs. 38.4%). The close mAP is, of itself, notable and speaks to the recent advantage in 3D estimation from monocular vision. However, as discussed above the differences would be larger with an IOU based matching function.

Class specific performance is in Table 7-SM. PointPillars was stronger for the two most common classes: cars (68.4% vs. 47.8% AP), and pedestrians (59.7% vs. 37.0% AP). MonoDIS, on the other hand, was stronger for the smaller classes bicycles (24.5% vs. 1.1% AP) and cones (48.7% vs. 30.8% AP). This is expected since 1) bicycles are thin objects with typically few lidar returns and 2) traffic cones are easy to detect in images, but small and easily overlooked in a lidar pointcloud. 3) MonoDIS applied importance sampling during training to boost rare classes. With similar detection performance, why was NDS lower for MonoDIS? The main reasons are the average translation errors (52cm vs. 74cm) and velocity errors (1.55m/s vs. 0.32m/s), both as expected. MonoDIS also had larger scale errors with mean IOU 74% vs. 71% but the difference is small, suggesting the strong ability for image-only methods to infer size from appearance.

**The importance of pre-training.** Using the lidar baseline we examine the importance of pre-training when training a detector on nuScenes. No pretraining means weights are initialized randomly using a uniform distribution as in [38]. ImageNet [21] pretraining [47] uses a backbone that was first trained to accurately classify images. KITTI [32] pretraining uses a backbone that was trained on the lidar pointclouds to predict 3D boxes. Interestingly, while the KITTI pretrained network did converge faster, the final performance of the network only marginally varied between different pretrainings (Table 3). One explanation may be that while KITTI is close in domain, the size is not large enough.

**Better detection gives better tracking.** Weng and Kitani [77] presented a simple baseline that achieved state-of-the-art 3d tracking results using powerful detections on KITTI. Here we analyze whether better detections also imply better tracking performance on nuScenes, using the image and lidar baselines presented in Section 4.1. Megvii, PointPillars and MonoDIS achieve an sAMOTA of 17.9%, 3.5% and 4.5%, and an AMOTP of 1.50m, 1.69m and 1.79m on the val set. Compared to the mAP and NDS detection results in Table 4, the ranking is similar. While the performance is correlated across most metrics, we notice that MonoDIS has the shortest LGD and highest number of track fragmentations. This may indicate that despite the lower performance, image based methods are less likely to miss an object for a protracted period of time.

**Table 3. PointPillars detection performance on the val set:**
| Lidar sweeps | Pretraining | NDS (%) | mAP (%) | mAVE (m/s) |
|--------------|-------------|---------|---------|------------|
| 1            | KITTI       | 31.8    | 21.9    | 1.21       |
| 5            | KITTI       | 42.9    | 27.7    | 0.34       |
| 10           | KITTI       | 44.8    | 28.8    | 0.30       |
| 10           | ImageNet    | 44.9    | 28.9    | 0.31       |
| 10           | None        | 44.2    | 27.6    | 0.33       |

**Table 4. Object detection results on the test set of nuScenes:**
| Method        | NDS (%) | mAP (%) | mATE (m) | mASE (1-iou) | mAOE (rad) | mAVE (m/s) | mAAE (1-acc) |
|---------------|---------|---------|----------|--------------|------------|------------|--------------|
| OFT [69]†     | 21.2    | 12.6    | 0.82     | 0.36         | 0.85       | 1.73       | 0.48         |
| SSD+3D†       | 26.8    | 16.4    | 0.90     | 0.33         | 0.62       | 1.31       | 0.29         |
| MDIS [70]†    | 38.4    | 30.4    | 0.74     | 0.26         | 0.55       | 1.55       | 0.13         |
| PP [51]       | 45.3    | 30.5    | 0.52     | 0.29         | 0.50       | 0.32       | 0.37         |
| Megvii [90]   | 63.3    | 52.8    | 0.30     | 0.25         | 0.38       | 0.25       | 0.14         |

(†) use only monocular camera images as input. All other methods use lidar.

---

### النسخة العربية

**4. التجارب**

في هذا القسم نقدم تجارب كشف وتتبع الأجسام على مجموعة بيانات nuScenes، ونحلل خصائصها ونقترح سبلاً للبحث المستقبلي.

**4.1. خطوط الأساس**

نقدم عدداً من خطوط الأساس بأنماط مختلفة للكشف والتتبع.

**خط أساس كشف الليدار.** لإظهار أداء خوارزمية رائدة على nuScenes، نقوم بتدريب كاشف أجسام ثلاثي الأبعاد قائم على الليدار فقط، PointPillars [51]. نستفيد من البيانات الزمنية المتاحة في nuScenes من خلال تجميع مسحات الليدار للحصول على سحابة نقاط أغنى كمدخل. تم تدريب شبكة واحدة لجميع الفئات. تم تعديل الشبكة أيضاً لتعلم السرعات كهدف انحدار إضافي لكل صندوق ثلاثي الأبعاد. قمنا بتعيين سمات الصندوق للسمة الأكثر شيوعاً لكل فئة في بيانات التدريب.

**خط أساس كشف الصور.** لفحص كشف الأجسام ثلاثي الأبعاد القائم على الصور فقط، نعيد تنفيذ طريقة Orthographic Feature Transform (OFT) [69]. تم استخدام شبكة OFT واحدة لجميع الفئات. قمنا بتعديل OFT الأصلي لاستخدام رأس كشف SSD وأكدنا أن هذا يطابق النتائج المنشورة على KITTI. تأخذ الشبكة صورة واحدة يتم من خلالها دمج التنبؤات الكاملة بزاوية 360 درجة معاً من جميع الكاميرات الـ 6 باستخدام كبت غير الحد الأقصى (NMS). قمنا بتعيين سرعة الصندوق على صفر والسمات للسمة الأكثر شيوعاً لكل فئة في بيانات التدريب.

**نتائج تحدي الكشف.** نقارن نتائج أفضل المشاركات في تحدي كشف nuScenes 2019. من بين جميع المشاركات، أعطت Megvii [90] أفضل أداء. إنها شبكة متعددة الرؤوس متوازنة الفئات قائمة على الليدار مع التفافات ثلاثية الأبعاد متفرقة. من بين المشاركات القائمة على الصور فقط، كانت MonoDIS [70] الأفضل، متفوقة بشكل كبير على خط أساس الصور الخاص بنا وحتى على بعض الطرق القائمة على الليدار. تستخدم خسارة كشف ثنائية وثلاثية الأبعاد مفككة جديدة. لاحظ أن جميع الطرق الأفضل أجرت أخذ عينات بالأهمية، مما يُظهر أهمية معالجة مشكلة عدم توازن الفئات.

**خطوط أساس التتبع.** نقدم عدة خطوط أساس للتتبع من بيانات الكاميرا والليدار. من تحدي الكشف، نختار طريقة الليدار الأفضل أداءً (Megvii [90])، والطريقة الأسرع المبلغ عنها في وقت الاستدلال (PointPillars [51])، بالإضافة إلى طريقة الكاميرا الأفضل أداءً (MonoDIS [70]). باستخدام الكشوفات من كل طريقة، نُعد خطوط أساس باستخدام نهج التتبع الموصوف في [77]. نوفر نتائج الكشف والتتبع لكل من هذه الطرق على تقسيمات التدريب والتحقق والاختبار لتسهيل بحث أكثر منهجية. انظر المادة التكميلية لنتائج تحدي تتبع nuScenes 2019.

**4.2. التحليل**

نحلل هنا خصائص الطرق المقدمة في القسم 4.1، بالإضافة إلى مجموعة البيانات ودالة المطابقة.

**الحجة لصالح مجموعة بيانات معيارية كبيرة.** إحدى مساهمات nuScenes هي حجم مجموعة البيانات، وخاصة الزيادة مقارنة بـ KITTI (الجدول 1). نفحص هنا فوائد حجم مجموعة البيانات الأكبر. نقوم بتدريب PointPillars [51] وOFT [69] وخط أساس صور إضافي، SSD+3D، بكميات متفاوتة من بيانات التدريب. يحتوي SSD+3D على نفس المعاملات ثلاثية الأبعاد مثل MonoDIS [70]، لكنه يستخدم تصميم مرحلة واحدة [53]. لهذه الدراسة الاستئصالية نقوم بتدريب PointPillars بعصور أقل بـ 6 مرات وجدول محسّن دورة واحدة [71] لتقليل وقت التدريب. اكتشافنا الرئيسي هو أن ترتيب الطريقة يتغير مع كمية البيانات (الشكل 6). على وجه الخصوص، يؤدي PointPillars أداءً مماثلاً لـ SSD+3D عند أحجام البيانات المتناسبة مع KITTI، ولكن مع استخدام المزيد من البيانات، من الواضح أن PointPillars أقوى. يشير هذا إلى أن الإمكانات الكاملة للخوارزميات المعقدة لا يمكن التحقق منها إلا بمجموعة تدريب أكبر وأكثر تنوعاً. تم التوصل إلى استنتاج مماثل بواسطة [56, 59] حيث اقترح [59] أن لوحة صدارة KITTI تعكس طريقة زيادة البيانات بدلاً من الخوارزميات الفعلية.

**أهمية دالة المطابقة.** نقارن أداء الطرق المنشورة (الجدول 4) عند استخدام مطابقة مسافة المركز 2 متر المقترحة مقابل مطابقة IOU المستخدمة في KITTI. كما هو متوقع، عند استخدام مطابقة IOU، تفشل الأجسام الصغيرة مثل المشاة والدراجات في تحقيق AP فوق 0، مما يجعل الترتيب مستحيلاً (الشكل 7). في المقابل، تعلن مطابقة مسافة المركز MonoDIS فائزاً واضحاً. التأثير أصغر بالنسبة لفئة السيارات، لكن في هذه الحالة أيضاً من الصعب حل الفرق بين MonoDIS وOFT.

تغير دالة المطابقة أيضاً التوازن بين الطرق القائمة على الليدار والصور. في الواقع، يتبدل الترتيب عند استخدام مطابقة مسافة المركز لصالح MonoDIS على كلتا الطريقتين القائمتين على الليدار في فئة الدراجات (الشكل 7). هذا منطقي لأن الهياكل الرفيعة للدراجات تجعل من الصعب كشفها في الليدار. نستنتج أن مطابقة مسافة المركز أكثر ملاءمة لترتيب الطرق القائمة على الصور جنباً إلى جنب مع الطرق القائمة على الليدار.

**مسحات ليدار متعددة تحسن الأداء.** وفقاً لبروتوكول التقييم الخاص بنا (القسم 3.1)، يُسمح فقط باستخدام 0.5 ثانية من البيانات السابقة لاتخاذ قرار كشف. يتوافق هذا مع 10 مسحات ليدار سابقة حيث يتم أخذ عينات من الليدار بتردد 20 هرتز. نبتكر طريقة بسيطة لدمج سحب نقاط متعددة في خط أساس PointPillars ونحقق في تأثير الأداء. يتم تنفيذ التجميع بنقل جميع سحب النقاط إلى نظام إحداثيات الإطار الرئيسي وإلحاق طابع زمني قياسي بكل نقطة يشير إلى الفارق الزمني بالثواني من الإطار الرئيسي. يتضمن المشفر الفارق الزمني كزخرفة إضافية لنقاط الليدار. بصرف النظر عن ميزة سحب النقاط الأغنى، يوفر هذا أيضاً معلومات زمنية، مما يساعد الشبكة في التوطين ويمكّن التنبؤ بالسرعة. نجرب استخدام 1 و5 و10 مسحات ليدار. تُظهر النتائج أن تقديرات الكشف والسرعة تتحسن مع زيادة عدد مسحات الليدار ولكن بمعدل عائد متناقص (الجدول 3).

**أي مستشعر هو الأهم؟** سؤال مهم للمركبات الذاتية هو ما هي المستشعرات المطلوبة لتحقيق أفضل أداء كشف. نقارن هنا أداء كاشفات ليدار وصور رائدة. نركز على هذه الأنماط لأنه لا توجد طرق تنافسية قائمة على الرادار فقط في الأدبيات ودراستنا الأولية مع PointPillars على بيانات الرادار لم تحقق نتائج واعدة. نقارن PointPillars، وهو كاشف ليدار سريع وخفيف مع MonoDIS، كاشف صور رائد (الجدول 4). تحقق الطريقتان mAP مماثل (30.5٪ مقابل 30.4٪)، لكن PointPillars لديه NDS أعلى (45.3٪ مقابل 38.4٪). mAP القريب ملحوظ في حد ذاته ويتحدث عن الميزة الحديثة في التقدير ثلاثي الأبعاد من الرؤية الأحادية. ومع ذلك، كما نوقش أعلاه، ستكون الفروق أكبر مع دالة مطابقة قائمة على IOU.

الأداء الخاص بالفئة موجود في الجدول 7-SM. كان PointPillars أقوى بالنسبة للفئتين الأكثر شيوعاً: السيارات (68.4٪ مقابل 47.8٪ AP)، والمشاة (59.7٪ مقابل 37.0٪ AP). من ناحية أخرى، كان MonoDIS أقوى بالنسبة للفئات الأصغر الدراجات (24.5٪ مقابل 1.1٪ AP) والمخاريط (48.7٪ مقابل 30.8٪ AP). هذا متوقع لأن 1) الدراجات أجسام رفيعة بعوائد ليدار قليلة عادةً و2) مخاريط المرور سهلة الكشف في الصور، لكنها صغيرة ويسهل التغاضي عنها في سحابة نقاط الليدار. 3) طبق MonoDIS أخذ عينات بالأهمية أثناء التدريب لتعزيز الفئات النادرة. مع أداء كشف مماثل، لماذا كان NDS أقل لـ MonoDIS؟ الأسباب الرئيسية هي متوسط أخطاء الترجمة (52 سم مقابل 74 سم) وأخطاء السرعة (1.55 م/ث مقابل 0.32 م/ث)، وكلاهما كما هو متوقع. كان لدى MonoDIS أيضاً أخطاء مقياس أكبر بمتوسط IOU 74٪ مقابل 71٪ لكن الفرق صغير، مما يشير إلى القدرة القوية للطرق القائمة على الصور فقط على استنتاج الحجم من المظهر.

**أهمية التدريب المسبق.** باستخدام خط أساس الليدار نفحص أهمية التدريب المسبق عند تدريب كاشف على nuScenes. عدم وجود تدريب مسبق يعني تهيئة الأوزان عشوائياً باستخدام توزيع موحد كما في [38]. التدريب المسبق على ImageNet [21] [47] يستخدم عموداً فقرياً تم تدريبه أولاً لتصنيف الصور بدقة. التدريب المسبق على KITTI [32] يستخدم عموداً فقرياً تم تدريبه على سحب نقاط الليدار للتنبؤ بصناديق ثلاثية الأبعاد. من المثير للاهتمام، بينما تقاربت الشبكة المُدربة مسبقاً على KITTI بشكل أسرع، اختلف الأداء النهائي للشبكة بشكل هامشي فقط بين التدريبات المسبقة المختلفة (الجدول 3). قد يكون أحد التفسيرات أنه بينما KITTI قريب في المجال، فإن الحجم ليس كبيراً بما فيه الكفاية.

**كشف أفضل يعطي تتبع أفضل.** قدم Weng وKitani [77] خط أساس بسيط حقق نتائج تتبع ثلاثية الأبعاد متطورة باستخدام كشوفات قوية على KITTI. نحلل هنا ما إذا كانت الكشوفات الأفضل تعني أيضاً أداء تتبع أفضل على nuScenes، باستخدام خطوط الأساس للصور والليدار المقدمة في القسم 4.1. تحقق Megvii وPointPillars وMonoDIS sAMOTA بنسبة 17.9٪ و3.5٪ و4.5٪، وAMOTP بمقدار 1.50 متر و1.69 متر و1.79 متر على مجموعة التحقق. بالمقارنة مع نتائج كشف mAP وNDS في الجدول 4، الترتيب مماثل. بينما الأداء مترابط عبر معظم المعايير، نلاحظ أن MonoDIS لديه أقصر LGD وأعلى عدد من تجزئات المسارات. قد يشير هذا إلى أنه على الرغم من الأداء الأقل، فإن الطرق القائمة على الصور أقل احتمالاً لفقدان جسم لفترة طويلة من الوقت.

**الجدول 3. أداء كشف PointPillars على مجموعة التحقق:**
| مسحات الليدار | التدريب المسبق | NDS (%) | mAP (%) | mAVE (م/ث) |
|---------------|-----------------|---------|---------|-------------|
| 1             | KITTI           | 31.8    | 21.9    | 1.21        |
| 5             | KITTI           | 42.9    | 27.7    | 0.34        |
| 10            | KITTI           | 44.8    | 28.8    | 0.30        |
| 10            | ImageNet        | 44.9    | 28.9    | 0.31        |
| 10            | لا يوجد         | 44.2    | 27.6    | 0.33        |

**الجدول 4. نتائج كشف الأجسام على مجموعة الاختبار لـ nuScenes:**
| الطريقة       | NDS (%) | mAP (%) | mATE (م) | mASE (1-iou) | mAOE (راديان) | mAVE (م/ث) | mAAE (1-acc) |
|---------------|---------|---------|----------|--------------|---------------|------------|--------------|
| OFT [69]†     | 21.2    | 12.6    | 0.82     | 0.36         | 0.85          | 1.73       | 0.48         |
| SSD+3D†       | 26.8    | 16.4    | 0.90     | 0.33         | 0.62          | 1.31       | 0.29         |
| MDIS [70]†    | 38.4    | 30.4    | 0.74     | 0.26         | 0.55          | 1.55       | 0.13         |
| PP [51]       | 45.3    | 30.5    | 0.52     | 0.29         | 0.50          | 0.32       | 0.37         |
| Megvii [90]   | 63.3    | 52.8    | 0.30     | 0.25         | 0.38          | 0.25       | 0.14         |

(†) تستخدم فقط صور الكاميرا الأحادية كمدخل. جميع الطرق الأخرى تستخدم الليدار.

---

### Translation Notes

- **Figures referenced:** Figure 6 (training data vs mAP), Figure 7 (AP vs matching function)
- **Tables referenced:** Table 1, Table 3 (PointPillars performance), Table 4 (detection results), Table 7-SM (class-specific performance)
- **Key terms introduced:** PointPillars, OFT, MonoDIS, Megvii, SSD, NMS, ablation study, importance sampling, matching function, pretraining
- **Equations:** 0
- **Citations:** Extensive citations [21, 32, 38, 47, 51, 53, 56, 59, 69, 70, 71, 77, 90]
- **Special handling:**
  - Method names (PointPillars, OFT, MonoDIS, Megvii, SSD+3D) kept in English as proper nouns
  - Abbreviations (NMS, AP, IOU, mAP, NDS, sAMOTA, AMOTP, LGD) kept in English
  - Percentages and measurements preserved exactly
  - Tables translated with headers in Arabic

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86

### Back-Translation Verification

**Baseline paragraph back-translated:**
"To demonstrate the performance of a leading algorithm on nuScenes, we train a 3D object detector based on lidar only, PointPillars [51]. We leverage the temporal data available in nuScenes by accumulating lidar sweeps to obtain a richer point cloud as input. A single network was trained for all classes. The network was also modified to learn velocities as an additional regression target for each 3D box."

**Analysis paragraph back-translated:**
"One of the contributions of nuScenes is the dataset size, and particularly the increase compared to KITTI (Table 1). Here we examine the benefits of the larger dataset size. We train PointPillars [51], OFT [69] and an additional image baseline, SSD+3D, with varying amounts of training data. Our main finding is that the method ordering changes with the amount of data (Figure 6)."

**Semantic match:** 0.86 ✓ (Excellent preservation of experimental details and analysis)
