# Section 4: Experiments
## القسم 4: التجارب

**Section:** experiments
**Translation Quality:** 0.86
**Glossary Terms Used:** كشف الأجسام (object detection), COCO (مجموعة بيانات COCO), المطابقة الثنائية (bipartite matching), محول (transformer), مشفر (encoder), فك التشفير (decoder), الانتباه الذاتي (self-attention), صناديق التحديد (bounding boxes), دالة الخسارة (loss function), الترميز الموضعي (positional encoding), تعزيز البيانات (data augmentation)

---

### English Version (Summary)

We show that DETR achieves competitive results compared to Faster R-CNN in quantitative evaluation on COCO. Then, we provide a detailed ablation study of the architecture and loss, with insights and qualitative results. Finally, to show that DETR is a versatile and extensible model, we present results on panoptic segmentation, training only a small extension on a fixed DETR model. We provide code and pretrained models to reproduce our experiments at https://github.com/facebookresearch/detr.

**Dataset.** We perform experiments on COCO 2017 detection and panoptic segmentation datasets [24,18], containing 118k training images and 5k validation images. Each image is annotated with bounding boxes and panoptic segmentation. There are 7 instances per image on average, up to 63 instances in a single image in training set, ranging from small to large on the same images. If not specified, we report AP as bbox AP, the integral metric over multiple thresholds. For comparison with Faster R-CNN we report validation AP at the last training epoch, for ablations we report median over validation results from the last 10 epochs.

**Technical details.** We train DETR with AdamW [26] setting the initial transformer's learning rate to 10⁻⁴, the backbone's to 10⁻⁵, and weight decay to 10⁻⁴. All transformer weights are initialized with Xavier init [11], and the backbone is with ImageNet-pretrained ResNet model [15] from torchvision with frozen batchnorm layers. We report results with two different backbones: a ResNet-50 and a ResNet-101. The corresponding models are called respectively DETR and DETR-R101.

**4.1 Comparison with Faster R-CNN**

Transformers are typically trained with Adam or Adagrad optimizers with very long training schedules and dropout, and this is true for DETR as well. Faster R-CNN, however, is trained with SGD with minimal data augmentation and we are not aware of successful applications of Adam or dropout. Despite these differences we attempt to make a Faster R-CNN baseline stronger. To align it with DETR, we add generalized IoU [38] to the box loss, the same random crop augmentation and long training known to improve results [13].

**Table 1:** Comparison with Faster R-CNN with a ResNet-50 and ResNet-101 backbones on the COCO validation set. DETR models achieve comparable results to heavily tuned Faster R-CNN baselines, having lower AP_S but greatly improved AP_L. Results without R101 in the name correspond to ResNet-50.

Key findings:
- DETR achieves 42.0 AP, comparable to Faster R-CNN
- DETR excels on large objects (AP_L = 61.1) but lags on small objects (AP_S = 20.5)
- DETR-DC5-R101 achieves best performance with 44.9 AP

**4.2 Ablations**

**Number of encoder layers** (Table 2): We evaluate the importance of global image-level self-attention by changing the number of encoder layers. Without encoder layers, overall AP drops by 3.9 points, with a more significant drop of 6.0 AP on large objects. We hypothesize that, by using global scene reasoning, the encoder is important for disentangling objects.

**Number of decoder layers** (Figure 4): We analyze the importance of each decoder layer by evaluating the objects that would be predicted at each stage of the decoding. Both AP and AP_50 improve after every layer, totalling into a very significant +8.2/9.5 AP improvement between the first and the last layer. With its set-based loss, DETR does not need NMS by design. We observe that the improvement brought by NMS diminishes as depth increases. At the last layers, we observe a small loss in AP as NMS incorrectly removes true positive predictions.

**Importance of FFN**: FFN inside transformers can be seen as 1×1 convolutional layers. By reducing the number of network parameters from 41.3M to 28.7M, leaving only 10.8M in the transformer, performance drops by 2.3 AP, we thus conclude that FFN are important for achieving good results.

**Importance of positional encodings** (Table 3): There are two kinds of positional encodings in our model: spatial positional encodings and output positional encodings (object queries). We experiment with various combinations of fixed and learned encodings. Output positional encodings are required and cannot be removed. Without any spatial positional encodings, the model still achieves more than 32 AP, losing 7.8 AP to the baseline.

**Loss ablations** (Table 4): To evaluate the importance of different components of the matching cost and the loss, we train several models. There are three components to the loss: classification loss, ℓ₁ bounding box distance loss, and GIoU [38] loss. GIoU loss on its own accounts for most of the model performance, losing only 0.7 AP to the baseline with combined losses. Using ℓ₁ without GIoU shows poor results.

Given these ablations, we conclude that transformer components: the global self-attention in encoder, FFN, multiple decoder layers, and positional encodings, all significantly contribute to the final object detection performance.

---

### النسخة العربية (ملخص)

نُظهر أن DETR يحقق نتائج تنافسية مقارنة بـ Faster R-CNN في التقييم الكمي على COCO. ثم نقدم دراسة استئصال مفصلة للمعمارية والخسارة، مع رؤى ونتائج نوعية. وأخيراً، لإظهار أن DETR نموذج متعدد الاستخدامات وقابل للتوسع، نقدم نتائج على التجزئة الشاملة، بتدريب امتداد صغير فقط على نموذج DETR ثابت. نوفر الكود والنماذج المدربة مسبقاً لإعادة إنتاج تجاربنا على https://github.com/facebookresearch/detr.

**مجموعة البيانات.** نُجري تجارب على مجموعات بيانات كشف COCO 2017 والتجزئة الشاملة [24,18]، التي تحتوي على 118 ألف صورة تدريب و5 آلاف صورة تحقق. كل صورة مُعلَّمة بصناديق تحديد وتجزئة شاملة. يوجد 7 نسخ لكل صورة في المتوسط، تصل إلى 63 نسخة في صورة واحدة في مجموعة التدريب، تتراوح من صغيرة إلى كبيرة في نفس الصور. إذا لم يُحدد، نبلغ عن AP كـ bbox AP، المقياس المتكامل عبر عتبات متعددة. للمقارنة مع Faster R-CNN نبلغ عن تحقق AP في عصر التدريب الأخير، وللاستئصالات نبلغ عن الوسيط على نتائج التحقق من آخر 10 عصور.

**التفاصيل التقنية.** ندرب DETR باستخدام AdamW [26] مع تعيين معدل التعلم الأولي للمحول على 10⁻⁴، والعمود الفقري على 10⁻⁵، وانحلال الوزن على 10⁻⁴. يتم تهيئة جميع أوزان المحول باستخدام Xavier init [11]، والعمود الفقري بنموذج ResNet المدرب مسبقاً على ImageNet [15] من torchvision مع طبقات batchnorm مجمدة. نبلغ عن النتائج مع عمودين فقريين مختلفين: ResNet-50 و ResNet-101. النماذج المقابلة تُسمى على التوالي DETR و DETR-R101.

**4.1 المقارنة مع Faster R-CNN**

عادةً ما تُدرب المحولات باستخدام محسنات Adam أو Adagrad مع جداول تدريب طويلة جداً وإسقاط، وهذا صحيح لـ DETR أيضاً. ومع ذلك، يتم تدريب Faster R-CNN باستخدام SGD مع الحد الأدنى من تعزيز البيانات ولسنا على علم بتطبيقات ناجحة لـ Adam أو الإسقاط. على الرغم من هذه الاختلافات، نحاول جعل خط أساس Faster R-CNN أقوى. لمواءمته مع DETR، نضيف IoU المعممة [38] إلى خسارة الصندوق، ونفس تعزيز القص العشوائي والتدريب الطويل المعروف بتحسين النتائج [13].

**الجدول 1:** مقارنة مع Faster R-CNN بأعمدة فقرية ResNet-50 و ResNet-101 على مجموعة تحقق COCO. تحقق نماذج DETR نتائج مماثلة لخطوط أساس Faster R-CNN المضبوطة بشكل كبير، مع AP_S أقل ولكن AP_L محسّن بشكل كبير. النتائج بدون R101 في الاسم تتوافق مع ResNet-50.

النتائج الرئيسية:
- يحقق DETR 42.0 AP، مماثل لـ Faster R-CNN
- يتفوق DETR على الأجسام الكبيرة (AP_L = 61.1) لكنه يتأخر على الأجسام الصغيرة (AP_S = 20.5)
- يحقق DETR-DC5-R101 أفضل أداء مع 44.9 AP

**4.2 الاستئصالات**

**عدد طبقات المشفر** (الجدول 2): نقيّم أهمية الانتباه الذاتي على مستوى الصورة العامة من خلال تغيير عدد طبقات المشفر. بدون طبقات المشفر، ينخفض AP الإجمالي بمقدار 3.9 نقطة، مع انخفاض أكثر أهمية قدره 6.0 AP على الأجسام الكبيرة. نفترض أنه باستخدام الاستدلال العام للمشهد، يكون المشفر مهماً لفصل الأجسام.

**عدد طبقات فك التشفير** (الشكل 4): نحلل أهمية كل طبقة فك تشفير من خلال تقييم الأجسام التي سيتم التنبؤ بها في كل مرحلة من فك التشفير. يتحسن كل من AP و AP_50 بعد كل طبقة، بإجمالي تحسن كبير جداً +8.2/9.5 AP بين الطبقة الأولى والأخيرة. بفضل خسارته القائمة على المجموعات، لا يحتاج DETR إلى NMS بالتصميم. نلاحظ أن التحسن الذي يجلبه NMS يتناقص مع زيادة العمق. في الطبقات الأخيرة، نلاحظ خسارة صغيرة في AP حيث يزيل NMS بشكل غير صحيح تنبؤات إيجابية حقيقية.

**أهمية FFN**: يمكن رؤية FFN داخل المحولات كطبقات التفافية 1×1. بتقليل عدد معلمات الشبكة من 41.3M إلى 28.7M، تاركين فقط 10.8M في المحول، ينخفض الأداء بمقدار 2.3 AP، وبالتالي نستنتج أن FFN مهم لتحقيق نتائج جيدة.

**أهمية الترميزات الموضعية** (الجدول 3): هناك نوعان من الترميزات الموضعية في نموذجنا: الترميزات الموضعية المكانية والترميزات الموضعية للإخراج (استعلامات الأجسام). نُجرب تركيبات مختلفة من الترميزات الثابتة والمتعلمة. الترميزات الموضعية للإخراج مطلوبة ولا يمكن إزالتها. بدون أي ترميزات موضعية مكانية، لا يزال النموذج يحقق أكثر من 32 AP، بخسارة 7.8 AP لخط الأساس.

**استئصالات الخسارة** (الجدول 4): لتقييم أهمية المكونات المختلفة لتكلفة المطابقة والخسارة، ندرب عدة نماذج. هناك ثلاثة مكونات للخسارة: خسارة التصنيف، وخسارة مسافة صندوق التحديد ℓ₁، وخسارة GIoU [38]. تمثل خسارة GIoU وحدها معظم أداء النموذج، بخسارة 0.7 AP فقط لخط الأساس مع الخسائر المدمجة. استخدام ℓ₁ بدون GIoU يُظهر نتائج سيئة.

بناءً على هذه الاستئصالات، نستنتج أن مكونات المحول: الانتباه الذاتي العام في المشفر، وFFN، وطبقات فك التشفير المتعددة، والترميزات الموضعية، جميعها تساهم بشكل كبير في أداء كشف الأجسام النهائي.

---

### Translation Notes

- **Tables referenced:** Table 1 (comparison with Faster R-CNN), Table 2 (encoder layers), Table 3 (positional encodings), Table 4 (loss components)
- **Figures referenced:** Figure 3 (encoder attention), Figure 4 (decoder layers performance), Figure 6 (decoder attention visualization)
- **Key findings:** DETR achieves competitive results (42.0 AP), excels on large objects, requires long training, benefits from all architectural components
- **Citations:** Multiple references to prior work [numbers preserved]
- **Special handling:**
  - Technical metrics (AP, AP_50, AP_S, AP_M, AP_L) kept with English abbreviations
  - Model names (DETR, DETR-DC5, Faster R-CNN) kept in English
  - Hyperparameters preserved in scientific notation (10⁻⁴, 10⁻⁵)
  - GitHub URL kept in English

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.89
- Readability: 0.84
- Glossary consistency: 0.84
- **Overall section score:** 0.86

**Note:** This is a condensed translation focusing on key experimental findings. The full section contains extensive tables, figures, and additional ablation studies that are summarized here for brevity while maintaining technical accuracy.
