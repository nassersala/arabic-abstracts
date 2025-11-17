# Section 4: Experiments
## القسم 4: التجارب

**Section:** Experiments
**Translation Quality:** 0.87
**Glossary Terms Used:** nuScenes, Waymo, benchmark (معيار), mAP (mAP), NDS (NDS), accuracy (دقة), precision (دقة), recall (استدعاء), ablation study (دراسة استئصال), baseline (خط أساس), IoU (IoU), bounding box (صندوق محيط), velocity (سرعة), occlusion (انسداد), visibility (رؤية), FPS (إطارات في الثانية), latency (كمون), multi-task learning (تعلم متعدد المهام)

---

### English Version

## 4.1 Datasets

We conduct experiments on two challenging public autonomous driving datasets, namely nuScenes dataset [4] and Waymo open dataset [40].

**The nuScenes dataset** [4] contains 1000 scenes of roughly 20s duration each, and the key samples are annotated at 2Hz. Each sample consists of RGB images from 6 cameras and has 360° horizontal FOV. For the detection task, there are 1.4M annotated 3D bounding boxes from 10 categories. We follow the settings in [32] to perform BEV segmentation task. This dataset also provides the official evaluation metrics for the detection task. The mean average precision (mAP) of nuScenes is computed using the center distance on the ground plane rather than the 3D Intersection over Union (IoU) to match the predicted results and ground truth. The nuScenes metrics also contain 5 types of true positive metrics (TP metrics), including ATE, ASE, AOE, AVE, and AAE for measuring translation, scale, orientation, velocity, and attribute errors, respectively. The nuScenes also defines a nuScenes detection score (NDS) as $\text{NDS} = \frac{1}{10}[5\text{mAP} + \sum_{mTP \in TP}(1 - \min(1, mTP))]$ to capture all aspects of the nuScenes detection tasks.

**Waymo Open Dataset** [40] is a large-scale autonomous driving dataset with 798 training sequences and 202 validation sequences. Note that the five images at each frame provided by Waymo have only about 252° horizontal FOV, but the provided annotated labels are 360° around the ego car. We remove these bounding boxes that can not be visible on any images in training and validation sets. Due to the Waymo Open Dataset being large-scale and high-rate [34], we use a subset of the training split by sampling every 5th frame from the training sequences and only detect the vehicle category. We use the thresholds of 0.5 and 0.7 for 3D IoU to compute the mAP on Waymo dataset.

## 4.2 Experimental Settings

Following previous methods [45, 47, 31], we adopt two types of backbone: ResNet101-DCN [15, 12] that initialized from FCOS3D [45] checkpoint, and VoVnet-99 [21] that initialized from DD3D [31] checkpoint. By default, we utilize the output multi-scale features from FPN [23] with sizes of 1/16, 1/32, 1/64 and the dimension of C = 256. For experiments on nuScenes, the default size of BEV queries is 200×200, the perception ranges are [−51.2m, 51.2m] for the X and Y axis and the size of resolution s of BEV's grid is 0.512m. We adopt learnable positional embedding for BEV queries. The BEV encoder contains 6 encoder layers and constantly refines the BEV queries in each layer. The input BEV features $B_{t-1}$ for each encoder layer are the same and require no gradients. For each local query, during the spatial cross-attention module implemented by deformable attention mechanism, it corresponds to $N_{\text{ref}} = 4$ target points with different heights in 3D space, and the predefined height anchors are sampled uniformly from −5 meters to 3 meters. For each reference point on 2D view features, we use four sampling points around this reference point for each head. By default, we train our models with 24 epochs, a learning rate of $2 \times 10^{-4}$.

For experiments on Waymo, we change a few settings. Due to the camera system of Waymo can not capture the whole scene around the ego car [40], the default spatial shape of BEV queries is 300×220, the perception ranges are [−35.0m, 75.0m] for the X-axis and [−75.0m, 75.0m] for the Y-axis. The size of resolution s of each gird is 0.5m. The ego car is at (70, 150) of the BEV.

**Baselines.** To eliminate the effect of task heads and compare other BEV generating methods fairly, we use VPN [30] and Lift-Splat [32] to replace our BEVFormer and keep task heads and other settings the same. We also adapt BEVFormer into a static model called **BEVFormer-S** via adjusting the temporal self-attention into a vanilla self-attention without using history BEV features.

## 4.3 3D Object Detection Results

We train our model on the detection task with the detection head only for fairly comparing with previous state-of-the-art 3D object detection methods. In Tab. 1 and Tab. 2, we report our main results on nuScenes test and val splits. Our method outperforms previous best method DETR3D [47] over 9.2 points on val set (51.7% NDS vs. 42.5% NDS), under fair training strategy and comparable model scales. On the test set, our model achieves 56.9% NDS without bells and whistles, 9.0 points higher than DETR3D (47.9% NDS). Our method can even achieve comparable performance to some LiDAR-based baselines such as SSN (56.9% NDS) [55] and PointPainting (58.1% NDS) [43].

Previous camera-based methods [47, 31, 45] were almost unable to estimate the velocity, and our method demonstrates that temporal information plays a crucial role in velocity estimation for multi-camera detection. The mean Average Velocity Error (mAVE) of BEVFormer is 0.378 m/s on the test set, outperforming other camera-based methods by a vast margin and approaching the performance of LiDAR-based methods [43].

We also conduct experiments on Waymo, as shown in Tab. 3. Following [34], we evaluate the vehicle category with IoU criterias of 0.7 and 0.5. In addition, We also adopt the nuScenes metrics to evaluate the results since the IoU-based metrics are too challenging for camera-based methods. Due to a few camera-based works reported results on Waymo, we also use the official codes of DETR3D to perform experiments on Waymo for comparison. We can observe that BEVFormer outperforms DETR3D by Average Precision with Heading information (APH) [40] of 6.0% and 2.5% on LEVEL_1 and LEVEL_2 difficulties with IoU criteria of 0.5. On nuScenes metrics, BEVFormer outperforms DETR3D with a margin of 3.2% NDS and 5.2% AP. We also conduct experiments on the front camera to compare BEVFormer with CaDNN [34], a monocular 3D detection method that reported their results on the Waymo dataset. BEVFormer outperforms CaDNN with APH of 13.3% and 11.2% on LEVEL_1 and LEVEL_2 difficulties with IoU criteria of 0.5.

## 4.4 Multi-tasks Perception Results

We train our model with both detection and segmentation heads to verify the learning ability of our model for multiple tasks, and the results are shown in Tab. 4. While comparing different BEV encoders under same settings, BEVFormer achieves higher performances of all tasks except for road segmentation results is comparable with BEVFormer-S. For example, with joint training, BEVFormer outperforms Lift-Splat*[32] by 11.0 points on detation task (52.0% NDS v.s. 41.0% NDS) and IoU of 5.6 points on lane segmentation (23.9% v.s. 18.3%). Compared with training tasks individually, multi-task learning saves computational cost and reduces the inference time by sharing more modules, including the backbone and the BEV encoder. In this paper, we show that the BEV features generated by our BEV encoder can be well adapted to different tasks, and the model training with multi-task heads performs even better on detection tasks and vehicles segmentation. However, the jointly trained model does not perform as well as individually trained models for road and lane segmentation, which is a common phenomenon called negative transfer [11, 13] in multi-task learning.

## 4.5 Ablation Study

To delve into the effect of different modules, we conduct ablation experiments on nuScenes val set with detection head. More ablation studies are in Appendix.

**Effectiveness of Spatial Cross-Attention.** To verify the effect of spatial cross-attention, we use BEVFormer-S to perform ablation experiments to exclude the interference of temporal information, and the results are shown in Tab. 5. The default spatial cross-attention is based on deformable attention. For comparison, we also construct two other baselines with different attention mechanisms: (1) Using the global attention to replace deformable attention; (2) Making each query only interact with its reference points rather than the surrounding local regions, and it is similar to previous methods [36, 37]. For a broader comparison, we also replace the BEVFormer with the BEV generation methods proposed by VPN [30] and Lift-Spalt [32]. We can observe that deformable attention significantly outperforms other attention mechanisms under a comparable model scale. Global attention consumes too much GPU memory, and point interaction has a limited receptive field. Sparse attention achieves better performance because it interacts with a priori determined regions of interest, balancing receptive field and GPU consumption.

**Effectiveness of Temporal Self-Attention.** From Tab. 1 and Tab. 4, we can observe that BEVFormer outperforms BEVFormer-S with remarkable improvements under the same setting, especially on challenging detection tasks. The effect of temporal information is mainly in the following aspects: (1) The introduction of temporal information greatly benefits the accuracy of the velocity estimation; (2) The predicted locations and orientations of the objects are more accurate with temporal information; (3) We obtain higher recall on heavily occluded objects since the temporal information contains past objects clues, as showed in Fig. 3. To evaluate the performance of BEVFormer on objects with different occlusion levels, we divide the validation set of nuScenes into four subsets according to the official visibility label provided by nuScenes. In each subset, we also compute the average recall of all categories with a center distance threshold of 2 meters during matching. The maximum number of predicted boxes is 300 for all methods to compare recall fairly. On the subset that only 0-40% of objects can be visible, the average recall of BEVFormer outperforms BEVFormer-S and DETR3D with a margin of more than 6.0%.

**Model Scale and Latency.** We compare the performance and latency of different configurations in Tab. 6. We ablate the scales of BEVFormer in three aspects, including whether to use multi-scale view features, the shape of BEV queries, and the number of layers, to verify the trade-off between performance and inference latency. We can observe that configuration C using one encoder layer in BEVFormer achieves 50.1 % NDS and reduces the latency of BEVFormer from the original 130ms to 25ms. Configuration D, with single-scale view features, smaller BEV size, and only 1 encoder layer, consumes only 7ms during inference, although it loses 3.9 points compared to the default configuration. However, due to the multi-view image inputs, the bottleneck that limits the efficiency lies in the backbone, and efficient backbones for autonomous driving deserve in-depth study. Overall, our architecture can adapt to various model scales and be flexible to trade off performance and efficiency.

## 4.6 Visualization Results

We show the detection results of a complex scene in Fig. 4. BEVFormer produces impressive results except for a few mistakes in small and remote objects. More qualitative results are provided in Appendix.

---

### النسخة العربية

## 4.1 مجموعات البيانات

نُجري تجارب على مجموعتي بيانات عامتين صعبتين للقيادة الذاتية، وهما مجموعة بيانات nuScenes [4] ومجموعة بيانات Waymo المفتوحة [40].

**مجموعة بيانات nuScenes** [4] تحتوي على 1000 مشهد بمدة تقريبية 20 ثانية لكل منها، والعينات الرئيسية مُعلّمة بمعدل 2Hz. تتكون كل عينة من صور RGB من 6 كاميرات ولديها مجال رؤية أفقي 360°. بالنسبة لمهمة الكشف، هناك 1.4 مليون صندوق محيط ثلاثي الأبعاد مُعلّم من 10 فئات. نتبع الإعدادات في [32] لأداء مهمة تقسيم BEV. توفر هذه المجموعة أيضاً مقاييس التقييم الرسمية لمهمة الكشف. يتم حساب متوسط الدقة المتوسطة (mAP) لـ nuScenes باستخدام مسافة المركز على المستوى الأرضي بدلاً من التقاطع ثلاثي الأبعاد على الاتحاد (IoU) لمطابقة النتائج المتوقعة والحقيقة الأرضية. تحتوي مقاييس nuScenes أيضاً على 5 أنواع من مقاييس الإيجابية الحقيقية (مقاييس TP)، بما في ذلك ATE وASE وAOE وAVE وAAE لقياس أخطاء الترجمة والمقياس والتوجيه والسرعة والسمات، على التوالي. يُعرّف nuScenes أيضاً درجة كشف nuScenes (NDS) على أنها $\text{NDS} = \frac{1}{10}[5\text{mAP} + \sum_{mTP \in TP}(1 - \min(1, mTP))]$ لالتقاط جميع جوانب مهام كشف nuScenes.

**مجموعة بيانات Waymo المفتوحة** [40] هي مجموعة بيانات واسعة النطاق للقيادة الذاتية مع 798 تسلسل تدريب و202 تسلسل تحقق. لاحظ أن الصور الخمس في كل إطار المقدمة من Waymo لديها فقط حوالي 252° مجال رؤية أفقي، لكن التسميات المُعلّمة المقدمة هي 360° حول السيارة الذاتية. نزيل هذه الصناديق المحيطة التي لا يمكن رؤيتها على أي صور في مجموعات التدريب والتحقق. نظراً لأن مجموعة بيانات Waymo المفتوحة واسعة النطاق وعالية المعدل [34]، نستخدم مجموعة فرعية من تقسيم التدريب عن طريق أخذ عينات من كل إطار خامس من تسلسلات التدريب ونكتشف فقط فئة المركبات. نستخدم عتبات 0.5 و0.7 لـ IoU ثلاثي الأبعاد لحساب mAP على مجموعة بيانات Waymo.

## 4.2 إعدادات التجارب

باتباع الطرق السابقة [45, 47, 31]، نعتمد نوعين من العمود الفقري: ResNet101-DCN [15, 12] المُهيّأ من نقطة تفتيش FCOS3D [45]، وVoVnet-99 [21] المُهيّأ من نقطة تفتيش DD3D [31]. بشكل افتراضي، نستخدم ميزات الإخراج متعددة المقاييس من FPN [23] بأحجام 1/16، 1/32، 1/64 وبُعد C = 256. بالنسبة للتجارب على nuScenes، الحجم الافتراضي لاستعلامات BEV هو 200×200، نطاقات الإدراك هي [−51.2m, 51.2m] للمحورين X وY وحجم دقة s لشبكة BEV هو 0.512m. نعتمد تضميناً موضعياً قابلاً للتعلم لاستعلامات BEV. يحتوي مشفر BEV على 6 طبقات مشفر ويُنقّح باستمرار استعلامات BEV في كل طبقة. ميزات BEV المدخلة $B_{t-1}$ لكل طبقة مشفر هي نفسها ولا تتطلب تدرجات. لكل استعلام محلي، أثناء وحدة الانتباه المتقاطع المكاني المُنفّذة بآلية الانتباه القابل للتشوه، يتوافق مع $N_{\text{ref}} = 4$ نقاط هدف بارتفاعات مختلفة في الفضاء ثلاثي الأبعاد، ومراسي الارتفاع المُحددة مسبقاً مأخوذة بشكل موحد من −5 أمتار إلى 3 أمتار. لكل نقطة مرجعية على ميزات العرض ثنائي الأبعاد، نستخدم أربع نقاط أخذ عينات حول هذه النقطة المرجعية لكل رأس. بشكل افتراضي، نُدرّب نماذجنا لـ 24 حقبة، بمعدل تعلم $2 \times 10^{-4}$.

بالنسبة للتجارب على Waymo، نُغيّر بعض الإعدادات. نظراً لأن نظام الكاميرا في Waymo لا يمكنه التقاط المشهد الكامل حول السيارة الذاتية [40]، فإن الشكل المكاني الافتراضي لاستعلامات BEV هو 300×220، نطاقات الإدراك هي [−35.0m, 75.0m] للمحور X و[−75.0m, 75.0m] للمحور Y. حجم دقة s لكل شبكة هو 0.5m. السيارة الذاتية في (70, 150) من BEV.

**الخطوط الأساسية.** للتخلص من تأثير رؤوس المهام ومقارنة طرق توليد BEV الأخرى بشكل عادل، نستخدم VPN [30] وLift-Splat [32] لاستبدال BEVFormer الخاص بنا ونحتفظ برؤوس المهام والإعدادات الأخرى نفسها. نُكيّف أيضاً BEVFormer إلى نموذج ثابت يُسمى **BEVFormer-S** عن طريق تعديل الانتباه الذاتي الزمني إلى انتباه ذاتي أساسي بدون استخدام ميزات BEV التاريخية.

## 4.3 نتائج الكشف عن الأجسام ثلاثية الأبعاد

نُدرّب نموذجنا على مهمة الكشف برأس الكشف فقط للمقارنة بشكل عادل مع طرق الكشف عن الأجسام ثلاثية الأبعاد الحديثة. في الجدولين 1 و2، نُبلّغ عن نتائجنا الرئيسية على تقسيمات اختبار وتحقق nuScenes. يتفوق منهجنا على أفضل طريقة سابقة DETR3D [47] بأكثر من 9.2 نقاط على مجموعة التحقق (51.7% NDS مقابل 42.5% NDS)، تحت استراتيجية تدريب عادلة ومقاييس نموذج قابلة للمقارنة. على مجموعة الاختبار، يحقق نموذجنا 56.9% NDS بدون حيل إضافية، أعلى بـ 9.0 نقاط من DETR3D (47.9% NDS). يمكن لطريقتنا حتى تحقيق أداء مماثل لبعض الخطوط الأساسية القائمة على الليدار مثل SSN (56.9% NDS) [55] وPointPainting (58.1% NDS) [43].

كانت الطرق السابقة القائمة على الكاميرا [47, 31, 45] غير قادرة تقريباً على تقدير السرعة، وتُظهر طريقتنا أن المعلومات الزمنية تلعب دوراً حاسماً في تقدير السرعة للكشف متعدد الكاميرات. متوسط خطأ السرعة المتوسط (mAVE) لـ BEVFormer هو 0.378 m/s على مجموعة الاختبار، متفوقاً على طرق أخرى قائمة على الكاميرا بهامش كبير ومقترباً من أداء الطرق القائمة على الليدار [43].

نُجري أيضاً تجارب على Waymo، كما هو موضح في الجدول 3. باتباع [34]، نُقيّم فئة المركبات بمعايير IoU 0.7 و0.5. بالإضافة إلى ذلك، نعتمد أيضاً مقاييس nuScenes لتقييم النتائج لأن المقاييس القائمة على IoU صعبة للغاية بالنسبة للطرق القائمة على الكاميرا. نظراً لأن عدداً قليلاً من الأعمال القائمة على الكاميرا أبلغت عن نتائج على Waymo، نستخدم أيضاً الأكواد الرسمية لـ DETR3D لإجراء تجارب على Waymo للمقارنة. يمكننا ملاحظة أن BEVFormer يتفوق على DETR3D بمتوسط دقة مع معلومات العنوان (APH) [40] بنسبة 6.0% و2.5% على صعوبات LEVEL_1 وLEVEL_2 بمعيار IoU 0.5. على مقاييس nuScenes، يتفوق BEVFormer على DETR3D بهامش 3.2% NDS و5.2% AP. نُجري أيضاً تجارب على الكاميرا الأمامية لمقارنة BEVFormer مع CaDNN [34]، وهي طريقة كشف ثلاثي الأبعاد أحادية الكاميرا أبلغت عن نتائجها على مجموعة بيانات Waymo. يتفوق BEVFormer على CaDNN بـ APH بنسبة 13.3% و11.2% على صعوبات LEVEL_1 وLEVEL_2 بمعيار IoU 0.5.

## 4.4 نتائج الإدراك متعدد المهام

نُدرّب نموذجنا برأسي الكشف والتقسيم للتحقق من قدرة التعلم لنموذجنا لمهام متعددة، والنتائج موضحة في الجدول 4. عند مقارنة مشفرات BEV المختلفة تحت نفس الإعدادات، يحقق BEVFormer أداءً أعلى في جميع المهام باستثناء نتائج تقسيم الطرق التي تُقارن مع BEVFormer-S. على سبيل المثال، مع التدريب المشترك، يتفوق BEVFormer على Lift-Splat*[32] بـ 11.0 نقطة على مهمة الكشف (52.0% NDS مقابل 41.0% NDS) وIoU بـ 5.6 نقاط على تقسيم الممرات (23.9% مقابل 18.3%). مقارنة بتدريب المهام بشكل فردي، يوفر التعلم متعدد المهام التكلفة الحسابية ويقلل وقت الاستدلال من خلال مشاركة المزيد من الوحدات، بما في ذلك العمود الفقري ومشفر BEV. في هذه الورقة، نُظهر أن ميزات BEV المُولدة بواسطة مشفر BEV الخاص بنا يمكن أن تتكيف جيداً مع مهام مختلفة، والنموذج المُدرّب برؤوس مهام متعددة يؤدي أداءً أفضل على مهام الكشف وتقسيم المركبات. ومع ذلك، لا يؤدي النموذج المُدرّب بشكل مشترك أداءً جيداً مثل النماذج المُدرّبة بشكل فردي لتقسيم الطرق والممرات، وهي ظاهرة شائعة تُسمى النقل السلبي [11, 13] في التعلم متعدد المهام.

## 4.5 دراسة استئصال

للتعمق في تأثير الوحدات المختلفة، نُجري تجارب استئصال على مجموعة تحقق nuScenes برأس الكشف. المزيد من دراسات الاستئصال في الملحق.

**فعالية الانتباه المتقاطع المكاني.** للتحقق من تأثير الانتباه المتقاطع المكاني، نستخدم BEVFormer-S لإجراء تجارب استئصال لاستبعاد تداخل المعلومات الزمنية، والنتائج موضحة في الجدول 5. الانتباه المتقاطع المكاني الافتراضي يعتمد على الانتباه القابل للتشوه. للمقارنة، نُنشئ أيضاً خطين أساسيين آخرين بآليات انتباه مختلفة: (1) استخدام الانتباه الشامل لاستبدال الانتباه القابل للتشوه؛ (2) جعل كل استعلام يتفاعل فقط مع نقاطه المرجعية بدلاً من المناطق المحلية المحيطة، وهو مشابه للطرق السابقة [36, 37]. للمقارنة الأوسع، نستبدل أيضاً BEVFormer بطرق توليد BEV المُقترحة من VPN [30] وLift-Spalt [32]. يمكننا ملاحظة أن الانتباه القابل للتشوه يتفوق بشكل كبير على آليات الانتباه الأخرى تحت مقياس نموذج قابل للمقارنة. الانتباه الشامل يستهلك ذاكرة GPU كثيرة جداً، والتفاعل النقطي له مجال استقبالي محدود. يحقق الانتباه المتناثر أداءً أفضل لأنه يتفاعل مع مناطق اهتمام محددة مسبقاً، موازناً بين مجال الاستقبال واستهلاك GPU.

**فعالية الانتباه الذاتي الزمني.** من الجدولين 1 و4، يمكننا ملاحظة أن BEVFormer يتفوق على BEVFormer-S بتحسينات ملحوظة تحت نفس الإعداد، خاصة على مهام الكشف الصعبة. تأثير المعلومات الزمنية يكون بشكل رئيسي في الجوانب التالية: (1) إدخال المعلومات الزمنية يفيد بشكل كبير دقة تقدير السرعة؛ (2) المواقع والتوجيهات المتوقعة للأجسام أكثر دقة مع المعلومات الزمنية؛ (3) نحصل على استدعاء أعلى على الأجسام المحجوبة بشدة لأن المعلومات الزمنية تحتوي على إشارات الأجسام السابقة، كما هو موضح في الشكل 3. لتقييم أداء BEVFormer على الأجسام بمستويات انسداد مختلفة، نُقسّم مجموعة التحقق من nuScenes إلى أربع مجموعات فرعية وفقاً لتسمية الرؤية الرسمية المُقدمة من nuScenes. في كل مجموعة فرعية، نحسب أيضاً متوسط الاستدعاء لجميع الفئات بعتبة مسافة مركز 2 متر أثناء المطابقة. العدد الأقصى للصناديق المتوقعة هو 300 لجميع الطرق لمقارنة الاستدعاء بشكل عادل. على المجموعة الفرعية التي يمكن رؤية 0-40% فقط من الأجسام، متوسط استدعاء BEVFormer يتفوق على BEVFormer-S وDETR3D بهامش أكثر من 6.0%.

**مقياس النموذج والكمون.** نُقارن الأداء والكمون للتكوينات المختلفة في الجدول 6. نستأصل مقاييس BEVFormer في ثلاثة جوانب، بما في ذلك ما إذا كان سيتم استخدام ميزات عرض متعددة المقاييس، وشكل استعلامات BEV، وعدد الطبقات، للتحقق من المقايضة بين الأداء وكمون الاستدلال. يمكننا ملاحظة أن التكوين C الذي يستخدم طبقة مشفر واحدة في BEVFormer يحقق 50.1% NDS ويقلل كمون BEVFormer من 130ms الأصلية إلى 25ms. التكوين D، مع ميزات عرض أحادية المقياس، وحجم BEV أصغر، وطبقة مشفر واحدة فقط، يستهلك 7ms فقط أثناء الاستدلال، على الرغم من أنه يفقد 3.9 نقاط مقارنة بالتكوين الافتراضي. ومع ذلك، بسبب مدخلات الصور متعددة الرؤية، فإن الاختناق الذي يحد من الكفاءة يكمن في العمود الفقري، والأعمدة الفقرية الفعالة للقيادة الذاتية تستحق دراسة متعمقة. بشكل عام، يمكن لمعماريتنا التكيف مع مقاييس نماذج مختلفة وأن تكون مرنة للمقايضة بين الأداء والكفاءة.

## 4.6 نتائج التصور

نُظهر نتائج الكشف لمشهد معقد في الشكل 4. ينتج BEVFormer نتائج مذهلة باستثناء بعض الأخطاء في الأجسام الصغيرة والبعيدة. يتم توفير المزيد من النتائج النوعية في الملحق.

---

### Translation Notes

- **Figures referenced:** Figure 3, Figure 4
- **Tables referenced:** Tables 1, 2, 3, 4, 5, 6
- **Key terms introduced:** nuScenes dataset, Waymo dataset, NDS score, mAP, IoU, ATE, ASE, AOE, AVE, AAE, APH, mAVE, negative transfer, ablation study
- **Equations:** 1 equation (NDS formula)
- **Citations:** Extensive citations to evaluation results
- **Special handling:** Preserved all numerical results, table references, and metric names

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87
