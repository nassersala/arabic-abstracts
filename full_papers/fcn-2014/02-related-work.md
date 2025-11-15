# Section 2: Related work
## القسم 2: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.87
**Glossary Terms Used:** deep learning, transfer learning, classification, fully convolutional, dense prediction, semantic segmentation, convolution, detection, fine-tuning, supervised pre-training, architecture

---

### English Version

Our approach draws on recent successes of deep nets for image classification [19, 31, 32] and transfer learning [4, 38]. Transfer was first demonstrated on various visual recognition tasks [4, 38], then on detection, and on both instance and semantic segmentation in hybrid proposal-classifier models [12, 16, 14]. We now re-architect and fine-tune classification nets to direct, dense prediction of semantic segmentation. We chart the space of FCNs and situate prior models, both historical and recent, in this framework.

**Fully convolutional networks** To our knowledge, the idea of extending a convnet to arbitrary-sized inputs first appeared in Matan et al. [25], which extended the classic LeNet [21] to recognize strings of digits. Because their net was limited to one-dimensional input strings, Matan et al. used Viterbi decoding to obtain their outputs. Wolf and Platt [37] expand convnet outputs to 2-dimensional maps of detection scores for the four corners of postal address blocks. Both of these historical works do inference and learning fully convolutionally for detection. Ning et al. [27] define a convnet for coarse multiclass segmentation of C. elegans tissues with fully convolutional inference.

Fully convolutional computation has also been exploited in the present era of many-layered nets. Sliding window detection by Sermanet et al. [29], semantic segmentation by Pinheiro and Collobert [28], and image restoration by Eigen et al. [5] do fully convolutional inference. Fully convolutional training is rare, but used effectively by Tompson et al. [35] to learn an end-to-end part detector and spatial model for pose estimation, although they do not exposit on or analyze this method.

Alternatively, He et al. [17] discard the nonconvolutional portion of classification nets to make a feature extractor. They combine proposals and spatial pyramid pooling to yield a localized, fixed-length feature for classification. While fast and effective, this hybrid model cannot be learned end-to-end.

**Dense prediction with convnets** Several recent works have applied convnets to dense prediction problems, including semantic segmentation by Ning et al. [27], Farabet et al. [8], and Pinheiro and Collobert [28]; boundary prediction for electron microscopy by Ciresan et al. [2] and for natural images by a hybrid neural net/nearest neighbor model by Ganin and Lempitsky [11]; and image restoration and depth estimation by Eigen et al. [5, 6]. Common elements of these approaches include

• small models restricting capacity and receptive fields;
• patchwise training [27, 2, 8, 28, 11];
• post-processing by superpixel projection, random field regularization, filtering, or local classification [8, 2, 11];
• input shifting and output interlacing for dense output [28, 11] as introduced by OverFeat [29];
• multi-scale pyramid processing [8, 28, 11];
• saturating tanh nonlinearities [8, 5, 28]; and
• ensembles [2, 11],

whereas our method does without this machinery. However, we do study patchwise training 3.4 and "shift-and-stitch" dense output 3.2 from the perspective of FCNs. We also discuss in-network upsampling 3.3, of which the fully connected prediction by Eigen et al. [6] is a special case.

Unlike these existing methods, we adapt and extend deep classification architectures, using image classification as supervised pre-training, and fine-tune fully convolutionally to learn simply and efficiently from whole image inputs and whole image ground truths.

Hariharan et al. [16] and Gupta et al. [14] likewise adapt deep classification nets to semantic segmentation, but do so in hybrid proposal-classifier models. These approaches fine-tune an R-CNN system [12] by sampling bounding boxes and/or region proposals for detection, semantic segmentation, and instance segmentation. Neither method is learned end-to-end.

They achieve state-of-the-art results on PASCAL VOC segmentation and NYUDv2 segmentation respectively, so we directly compare our standalone, end-to-end FCN to their semantic segmentation results in Section 5.

---

### النسخة العربية

يعتمد نهجنا على النجاحات الأخيرة للشبكات العميقة في تصنيف الصور [19، 31، 32] والتعلم بالنقل [4، 38]. تم إثبات التعلم بالنقل لأول مرة على مهام التعرف البصري المختلفة [4، 38]، ثم على الكشف، وعلى كل من تجزئة الكائنات والتجزئة الدلالية في نماذج المقترحات-المصنفات الهجينة [12، 16، 14]. نقوم الآن بإعادة تصميم شبكات التصنيف والضبط الدقيق لها للتنبؤ الكثيف المباشر للتجزئة الدلالية. نرسم خريطة فضاء شبكات FCN ونضع النماذج السابقة، التاريخية والحديثة على حد سواء، في هذا الإطار.

**الشبكات الالتفافية الكاملة** على حد علمنا، ظهرت فكرة توسيع الشبكة الالتفافية لتقبل مدخلات ذات أحجام تعسفية لأول مرة في Matan وآخرون [25]، الذي وسع LeNet الكلاسيكية [21] للتعرف على سلاسل الأرقام. نظراً لأن شبكتهم كانت محدودة بسلاسل إدخال أحادية البُعد، استخدم Matan وآخرون فك ترميز Viterbi للحصول على مخرجاتهم. وسّع Wolf وPlatt [37] مخرجات الشبكة الالتفافية إلى خرائط ثنائية الأبعاد لدرجات الكشف للزوايا الأربع لكتل عناوين البريد. كلا هذين العملين التاريخيين يقومان بالاستنتاج والتعلم بشكل التفافي كامل للكشف. عرّف Ning وآخرون [27] شبكة التفافية للتجزئة متعددة الفئات الخشنة لأنسجة C. elegans مع استنتاج التفافي كامل.

تم استغلال الحساب الالتفافي الكامل أيضاً في العصر الحالي للشبكات متعددة الطبقات. الكشف بالنافذة المنزلقة بواسطة Sermanet وآخرون [29]، والتجزئة الدلالية بواسطة Pinheiro وCollobert [28]، واستعادة الصور بواسطة Eigen وآخرون [5] تقوم بالاستنتاج الالتفافي الكامل. التدريب الالتفافي الكامل نادر، لكن استخدمه Tompson وآخرون [35] بفعالية لتعلم كاشف أجزاء من البداية إلى النهاية ونموذج مكاني لتقدير الوضعية، على الرغم من أنهم لا يشرحون أو يحللون هذه الطريقة.

بدلاً من ذلك، يتجاهل He وآخرون [17] الجزء غير الالتفافي من شبكات التصنيف لصنع مستخرج ميزات. يجمعون بين المقترحات والتجميع الهرمي المكاني لإنتاج ميزة موضعية ذات طول ثابت للتصنيف. في حين أن هذا النموذج الهجين سريع وفعال، لا يمكن تعلمه من البداية إلى النهاية.

**التنبؤ الكثيف باستخدام الشبكات الالتفافية** طبقت عدة أعمال حديثة الشبكات الالتفافية على مشاكل التنبؤ الكثيف، بما في ذلك التجزئة الدلالية بواسطة Ning وآخرون [27]، وFarabet وآخرون [8]، وPinheiro وCollobert [28]؛ والتنبؤ بالحدود للمجهر الإلكتروني بواسطة Ciresan وآخرون [2] وللصور الطبيعية بواسطة نموذج هجين للشبكة العصبية/الجار الأقرب بواسطة Ganin وLempitsky [11]؛ واستعادة الصور وتقدير العمق بواسطة Eigen وآخرون [5، 6]. تشمل العناصر المشتركة لهذه الأساليب ما يلي:

• نماذج صغيرة تحد من السعة والحقول الاستقبالية؛
• التدريب القائم على الرقع [27، 2، 8، 28، 11]؛
• المعالجة اللاحقة بواسطة إسقاط البكسلات الفائقة، أو تنظيم الحقول العشوائية، أو الترشيح، أو التصنيف الموضعي [8، 2، 11]؛
• تحويل الإدخال وتشابك المخرجات للمخرجات الكثيفة [28، 11] كما قدمتها OverFeat [29]؛
• معالجة الهرم متعدد المقاييس [8، 28، 11]؛
• اللاخطيات tanh المشبعة [8، 5، 28]؛ و
• المجموعات [2، 11]،

في حين أن طريقتنا تستغني عن هذه الآليات. ومع ذلك، ندرس التدريب القائم على الرقع 3.4 والمخرجات الكثيفة "التحويل والتشابك" 3.2 من منظور شبكات FCN. نناقش أيضاً الرفع الداخلي في الشبكة 3.3، والذي يُعتبر التنبؤ المتصل بالكامل بواسطة Eigen وآخرون [6] حالة خاصة منه.

على عكس هذه الأساليب الموجودة، نقوم بتكييف وتوسيع معماريات التصنيف العميقة، باستخدام تصنيف الصور كتدريب مسبق خاضع للإشراف، والضبط الدقيق بشكل التفافي كامل للتعلم ببساطة وكفاءة من مدخلات الصور الكاملة والحقائق الأرضية للصور الكاملة.

يقوم Hariharan وآخرون [16] وGupta وآخرون [14] بالمثل بتكييف شبكات التصنيف العميقة للتجزئة الدلالية، لكنهم يفعلون ذلك في نماذج المقترحات-المصنفات الهجينة. تقوم هذه الأساليب بالضبط الدقيق لنظام R-CNN [12] عن طريق أخذ عينات من صناديق التحديد و/أو مقترحات المناطق للكشف والتجزئة الدلالية وتجزئة الكائنات. لا يتم تعلم أي من الطريقتين من البداية إلى النهاية.

يحققون نتائج أحدث ما توصلت إليه التقنية على تجزئة PASCAL VOC وتجزئة NYUDv2 على التوالي، لذلك نقارن بشكل مباشر شبكة FCN المستقلة من البداية إلى النهاية بنتائج التجزئة الدلالية الخاصة بهم في القسم 5.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Transfer learning (التعلم بالنقل)
  - Hybrid proposal-classifier models (نماذج المقترحات-المصنفات الهجينة)
  - Fully convolutional network (الشبكة الالتفافية الكاملة)
  - Sliding window detection (الكشف بالنافذة المنزلقة)
  - Feature extractor (مستخرج ميزات)
  - Spatial pyramid pooling (التجميع الهرمي المكاني)
  - Dense prediction (التنبؤ الكثيف)
  - Patchwise training (التدريب القائم على الرقع)
  - Superpixel projection (إسقاط البكسلات الفائقة)
  - Random field regularization (تنظيم الحقول العشوائية)
  - Input shifting (تحويل الإدخال)
  - Output interlacing (تشابك المخرجات)
  - Multi-scale pyramid processing (معالجة الهرم متعدد المقاييس)
  - Supervised pre-training (التدريب المسبق الخاضع للإشراف)
  - Ground truth (الحقيقة الأرضية)

- **Equations:** None
- **Citations:** Numerous references [2, 4, 5, 6, 8, 11, 12, 14, 16, 17, 19, 21, 25, 27, 28, 29, 31, 32, 35, 37, 38]
- **Special handling:**
  - Kept network names (LeNet, R-CNN, OverFeat) in English as proper nouns
  - Maintained reference numbers in brackets
  - Preserved the bulleted list structure
  - Technical terms translated consistently with glossary

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87

### Back-translation Check

Key sentence:
Arabic: "نقوم الآن بإعادة تصميم شبكات التصنيف والضبط الدقيق لها للتنبؤ الكثيف المباشر للتجزئة الدلالية"
Back: "We now redesign and fine-tune classification networks for direct dense prediction of semantic segmentation"
Original: "We now re-architect and fine-tune classification nets to direct, dense prediction of semantic segmentation"
✓ Semantic equivalence confirmed

Arabic: "على عكس هذه الأساليب الموجودة، نقوم بتكييف وتوسيع معماريات التصنيف العميقة"
Back: "Unlike these existing methods, we adapt and extend deep classification architectures"
Original: "Unlike these existing methods, we adapt and extend deep classification architectures"
✓ Perfect match
