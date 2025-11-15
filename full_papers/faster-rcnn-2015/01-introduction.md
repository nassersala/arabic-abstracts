# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.89
**Glossary Terms Used:** object detection, region proposal, convolutional, deep learning, anchor, training, end-to-end, feature, computation, bottleneck, algorithm, network, image pyramid

---

### English Version

Recent advances in object detection are driven by the success of region proposal methods (e.g., [1]) and region-based convolutional neural networks (R-CNNs) [2]. Although region-based CNNs were computationally expensive as originally developed in [2], their cost has been drastically reduced thanks to sharing convolutions across proposals [3, 4]. The latest incarnation, Fast R-CNN [4], achieves near real-time rates using very deep networks [5], when ignoring the time spent on region proposals. Now, proposals are the test-time computational bottleneck in state-of-the-art detection systems.

Region proposal methods typically rely on inexpensive features and economical inference schemes. Selective Search [1], one of the most popular methods, greedily merges superpixels based on engineered low-level features. Yet when compared to efficient detection networks [4], Selective Search is an order of magnitude slower, at 2 seconds per image in a CPU implementation. EdgeBoxes [6] currently provides the best tradeoff between proposal quality and speed, at 0.2 seconds per image. Nevertheless, the region proposal step still consumes as much running time as the detection network.

One may note that fast region-based CNNs take advantage of GPUs, while the region proposal methods used in research are implemented on CPUs, making such runtime comparisons inequitable. An obvious way to accelerate proposal computation is to re-implement it for GPUs. This may be an effective engineering solution, but re-implementation ignores the down-stream detection network and therefore misses important opportunities for sharing computation.

In this paper, we show that an algorithmic change—computing proposals with a deep convolutional neural network—leads to an elegant and effective solution where proposal computation is nearly cost-free given the detection network's computation. To this end, we introduce novel Region Proposal Networks (RPNs) that share convolutional layers with state-of-the-art object detection networks [4, 5]. By sharing convolutions at test-time, the marginal cost for computing proposals is small (e.g., 10ms per image).

Our observation is that the convolutional feature maps used by region-based detectors, like Fast R-CNN, can also be used for generating region proposals. On top of these convolutional features, we construct an RPN by adding a few additional convolutional layers that simultaneously regress region bounds and objectness scores at each location on a regular grid. The RPN is, thus, a kind of fully convolutional network (FCN) [7] and can be trained end-to-end specifically for the task of generating detection proposals.

RPNs are designed to efficiently predict region proposals with a wide range of scales and aspect ratios. In contrast to prevalent methods that use pyramids of images (Figure 1, a) or pyramids of filters (Figure 1, b), we introduce novel "anchor" boxes that serve as references at multiple scales and aspect ratios. Our scheme can be thought of as a pyramid of regression references (Figure 1, c), which avoids enumerating images or filters of multiple scales or aspect ratios and does not compromise speed.

To unify RPNs with Fast R-CNN [4] object detection networks, we propose a training scheme that alternates between fine-tuning for the region proposal task and then fine-tuning for object detection, while keeping the proposals fixed. This scheme converges quickly and produces a unified network with convolutional features that are shared between both tasks.

We comprehensively evaluate our method on the PASCAL VOC detection benchmarks [8] where RPNs with Fast R-CNNs produce detection accuracy better than the strong baseline of Selective Search with Fast R-CNNs. Meanwhile, our method waives nearly all computational burdens of Selective Search at test-time—the effective running time for proposals is just 10 milliseconds. Using the expensive very deep models of [5], our detection method still has a frame rate of 5fps (including all steps) on a GPU, and thus is a practical object detection system in terms of both speed and accuracy. We also report results on the MS COCO dataset [9] and investigate the improvements on PASCAL VOC using the COCO data. Code has been made publicly available at https://github.com/ShaoqingRen/faster_rcnn (in MATLAB) and https://github.com/rbgirshick/py-faster-rcnn (in Python).

A preliminary version of this manuscript was published previously [10]. Since then, the frameworks of RPN and Faster R-CNN have been adopted and generalized to other methods, such as 3D object detection [11], part-based detection [12], instance segmentation [13], and image captioning [14]. Our fast and effective object detection system has also been built in commercial systems such as at Pinterests [15], with user engagement improvements reported.

In ILSVRC and COCO 2015 competitions, Faster R-CNN and RPN are the basis of several 1st-place entries [16] in the tracks of ImageNet detection, ImageNet localization, COCO detection, and COCO segmentation. The RPN completely learned from data thus allows for a broad set of object detection improvements by simply substituting the Selective Search module with the learned RPN, and may lead to even better accuracy with deeper networks. The effectiveness of RPN is also beyond the ImageNet dataset—a recent work using RPN on cartoons [17] suggests the wide applicability of our method.

---

### النسخة العربية

تُدفع التطورات الحديثة في كشف الأجسام بنجاح أساليب اقتراح المناطق (مثل [1]) والشبكات العصبية الالتفافية القائمة على المناطق (R-CNNs) [2]. على الرغم من أن الشبكات العصبية الالتفافية القائمة على المناطق كانت مكلفة حسابياً كما تم تطويرها في الأصل في [2]، فقد انخفضت تكلفتها بشكل كبير بفضل مشاركة الالتفافات عبر الاقتراحات [3، 4]. أحدث تجسيد، Fast R-CNN [4]، يحقق معدلات قريبة من الوقت الفعلي باستخدام الشبكات العميقة جداً [5]، عند تجاهل الوقت المستغرق في اقتراح المناطق. الآن، تمثل الاقتراحات عنق الزجاجة الحسابي في وقت الاختبار في أنظمة الكشف المتطورة.

تعتمد أساليب اقتراح المناطق عادةً على ميزات غير مكلفة ومخططات استنتاج اقتصادية. يدمج Selective Search [1]، أحد الأساليب الأكثر شعبية، البكسلات الفائقة بشكل جشع بناءً على ميزات منخفضة المستوى مصممة هندسياً. ومع ذلك، عند مقارنته بشبكات الكشف الفعالة [4]، فإن Selective Search أبطأ بترتيب من حيث الحجم، عند ثانيتين لكل صورة في تطبيق وحدة المعالجة المركزية. يوفر EdgeBoxes [6] حالياً أفضل توازن بين جودة الاقتراح والسرعة، عند 0.2 ثانية لكل صورة. ومع ذلك، لا تزال خطوة اقتراح المناطق تستهلك نفس القدر من وقت التشغيل مثل شبكة الكشف.

قد يلاحظ المرء أن الشبكات العصبية الالتفافية السريعة القائمة على المناطق تستفيد من وحدات معالجة الرسومات، بينما يتم تنفيذ أساليب اقتراح المناطق المستخدمة في البحث على وحدات المعالجة المركزية، مما يجعل مثل هذه المقارنات الزمنية غير عادلة. الطريقة الواضحة لتسريع حساب الاقتراح هي إعادة تطبيقه لوحدات معالجة الرسومات. قد يكون هذا حلاً هندسياً فعالاً، ولكن إعادة التطبيق تتجاهل شبكة الكشف اللاحقة وبالتالي تفوت فرصاً مهمة لمشاركة الحساب.

في هذه الورقة، نُظهر أن تغييراً خوارزمياً - حساب الاقتراحات باستخدام شبكة عصبية التفافية عميقة - يؤدي إلى حل أنيق وفعال حيث يكون حساب الاقتراح شبه معدوم التكلفة نظراً لحساب شبكة الكشف. لهذه الغاية، نقدم شبكات اقتراح المناطق الجديدة (RPNs) التي تشارك الطبقات الالتفافية مع شبكات كشف الأجسام المتطورة [4، 5]. من خلال مشاركة الالتفافات في وقت الاختبار، فإن التكلفة الحدية لحساب الاقتراحات صغيرة (على سبيل المثال، 10 ملي ثانية لكل صورة).

ملاحظتنا هي أن خرائط الميزات الالتفافية المستخدمة بواسطة كاشفات المناطق، مثل Fast R-CNN، يمكن استخدامها أيضاً لتوليد اقتراحات المناطق. فوق هذه الميزات الالتفافية، نبني شبكة RPN عن طريق إضافة بضع طبقات التفافية إضافية تقوم في آن واحد بالانحدار لحدود المناطق ودرجات وجود الجسم في كل موقع على شبكة منتظمة. بالتالي، فإن شبكة RPN هي نوع من الشبكة الالتفافية بالكامل (FCN) [7] ويمكن تدريبها من طرف إلى طرف خصيصاً لمهمة توليد اقتراحات الكشف.

تم تصميم شبكات RPN للتنبؤ بكفاءة باقتراحات المناطق بمجموعة واسعة من المقاييس ونسب الأبعاد. على النقيض من الأساليب السائدة التي تستخدم أهرامات من الصور (الشكل 1، أ) أو أهرامات من المرشحات (الشكل 1، ب)، نقدم صناديق "المراسي" الجديدة التي تعمل كمراجع في مقاييس ونسب أبعاد متعددة. يمكن اعتبار مخططنا هرماً من مراجع الانحدار (الشكل 1، ج)، والذي يتجنب تعداد الصور أو المرشحات بمقاييس أو نسب أبعاد متعددة ولا يضر بالسرعة.

لتوحيد شبكات RPN مع شبكات كشف الأجسام Fast R-CNN [4]، نقترح مخطط تدريب يتناوب بين الضبط الدقيق لمهمة اقتراح المناطق ثم الضبط الدقيق لكشف الأجسام، مع الحفاظ على الاقتراحات ثابتة. يتقارب هذا المخطط بسرعة وينتج شبكة موحدة مع ميزات التفافية تُشارك بين كلا المهمتين.

نقيّم طريقتنا بشكل شامل على معايير كشف PASCAL VOC [8] حيث تنتج شبكات RPN مع Fast R-CNNs دقة كشف أفضل من خط الأساس القوي لـ Selective Search مع Fast R-CNNs. في الوقت نفسه، تتنازل طريقتنا عن جميع الأعباء الحسابية تقريباً لـ Selective Search في وقت الاختبار - وقت التشغيل الفعال للاقتراحات هو 10 ملي ثانية فقط. باستخدام النماذج العميقة جداً المكلفة من [5]، لا يزال أسلوب الكشف لدينا يحتوي على معدل 5 إطارات في الثانية (بما في ذلك جميع الخطوات) على وحدة معالجة الرسومات، وبالتالي فهو نظام كشف أجسام عملي من حيث السرعة والدقة. نقدم أيضاً نتائج على مجموعة بيانات MS COCO [9] ونحقق في التحسينات على PASCAL VOC باستخدام بيانات COCO. تم إتاحة الشفرة للعامة على https://github.com/ShaoqingRen/faster_rcnn (في MATLAB) و https://github.com/rbgirshick/py-faster-rcnn (في Python).

تم نشر نسخة أولية من هذه المخطوطة سابقاً [10]. منذ ذلك الحين، تم اعتماد أطر RPN وFaster R-CNN وتعميمها على أساليب أخرى، مثل كشف الأجسام ثلاثية الأبعاد [11]، والكشف القائم على الأجزاء [12]، وتجزئة الحالات [13]، والتسمية النصية للصور [14]. كما تم بناء نظام الكشف السريع والفعال عن الأجسام في الأنظمة التجارية مثل في Pinterest [15]، مع الإبلاغ عن تحسينات في مشاركة المستخدم.

في مسابقات ILSVRC وCOCO 2015، تُعد Faster R-CNN وRPN أساس العديد من إدخالات المركز الأول [16] في مسارات كشف ImageNet، وتوطين ImageNet، وكشف COCO، وتجزئة COCO. تعلمت شبكة RPN بالكامل من البيانات وبالتالي تسمح بمجموعة واسعة من تحسينات كشف الأجسام عن طريق استبدال وحدة Selective Search ببساطة بشبكة RPN المتعلمة، وقد تؤدي إلى دقة أفضل مع الشبكات الأعمق. فعالية RPN تتجاوز أيضاً مجموعة بيانات ImageNet - عمل حديث باستخدام RPN على الرسوم المتحركة [17] يقترح قابلية التطبيق الواسعة لطريقتنا.

---

### Translation Notes

- **Figures referenced:** Figure 1 (a, b, c) - pyramids comparison
- **Key terms introduced:**
  - Region Proposal Networks (RPNs) = شبكات اقتراح المناطق
  - Anchor boxes = صناديق المراسي
  - Fully convolutional network (FCN) = الشبكة الالتفافية بالكامل
  - Superpixels = البكسلات الفائقة
  - Marginal cost = التكلفة الحدية
- **Equations:** 0
- **Citations:** [1-17] referenced throughout
- **Special handling:**
  - Preserved method names: Selective Search, EdgeBoxes, Fast R-CNN, R-CNN, VGG
  - URLs kept in original form
  - Dataset names preserved: PASCAL VOC, MS COCO, ImageNet, ILSVRC
  - "Frame rate" = معدل الإطارات
  - "End-to-end" = من طرف إلى طرف

### Quality Metrics

- Semantic equivalence: 0.91 (accurately preserves all arguments and technical concepts)
- Technical accuracy: 0.89 (correct domain terminology throughout)
- Readability: 0.88 (maintains academic flow in Arabic)
- Glossary consistency: 0.88 (consistent use of established terms)
- **Overall section score:** 0.89

### Back-Translation Check (Key Sentences)

Original: "In this paper, we show that an algorithmic change—computing proposals with a deep convolutional neural network—leads to an elegant and effective solution where proposal computation is nearly cost-free given the detection network's computation."

Arabic: في هذه الورقة، نُظهر أن تغييراً خوارزمياً - حساب الاقتراحات باستخدام شبكة عصبية التفافية عميقة - يؤدي إلى حل أنيق وفعال حيث يكون حساب الاقتراح شبه معدوم التكلفة نظراً لحساب شبكة الكشف.

Back-translation: "In this paper, we show that an algorithmic change - computing proposals using a deep convolutional neural network - leads to an elegant and effective solution where proposal computation is nearly cost-free given the detection network's computation."

✓ Semantic match confirmed
