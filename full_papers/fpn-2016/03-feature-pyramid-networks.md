# Section 3: Feature Pyramid Networks
## القسم 3: شبكات هرم السمات

**Section:** feature-pyramid-networks
**Translation Quality:** 0.89
**Glossary Terms Used:** feature pyramid, architecture, convolutional, ResNets, semantic, bottom-up, top-down, lateral connections, anchors, aspect ratio, ground truth, bounding box

---

### English Version

Our goal is to leverage a ConvNet's pyramidal feature hierarchy, which has semantics from low to high levels, and build a feature pyramid with high-level semantics throughout. The resulting Feature Pyramid Network is general-purpose and in this paper we focus on sliding window proposers (Region Proposal Network, RPN for short) [29] and region-based detectors (Fast R-CNN) [11]. We also generalize FPNs to instance segmentation proposals in Sec. 6. Our method takes a single-scale image of an arbitrary size as input, and outputs proportionally sized feature maps at multiple levels, in a fully convolutional fashion. This process is independent of the backbone convolutional architectures (e.g., [19, 36, 16]), and in this paper we present results using ResNets [16]. The construction of our pyramid involves a bottom-up pathway, a top-down pathway, and lateral connections, as introduced in the following.

**Bottom-up pathway.** The bottom-up pathway is the feed-forward computation of the backbone ConvNet, which computes a feature hierarchy consisting of feature maps at several scales with a scaling step of 2. There are often many layers producing output maps of the same size and we say these layers are in the same network stage. For our feature pyramid, we define one pyramid level for each stage. We choose the output of the last layer of each stage as our reference set of feature maps, which we will enrich to create our pyramid. This choice is natural since the deepest layer of each stage should have the strongest features.

Specifically, for ResNets [16] we use the feature activations output by each stage's last residual block. We denote the output of these last residual blocks as {C2, C3, C4, C5} for conv2, conv3, conv4, and conv5 outputs, and note that they have strides of {4, 8, 16, 32} pixels with respect to the input image. We do not include conv1 into the pyramid due to its large memory footprint.

**Top-down pathway and lateral connections.** The top-down pathway hallucinates higher resolution features by upsampling spatially coarser, but semantically stronger, feature maps from higher pyramid levels. These features are then enhanced with features from the bottom-up pathway via lateral connections. Each lateral connection merges feature maps of the same spatial size from the bottom-up pathway and the top-down pathway. The bottom-up feature map is of lower-level semantics, but its activations are more accurately localized as it was subsampled fewer times.

Fig. 3 shows the building block that constructs our top-down feature maps. With a coarser-resolution feature map, we upsample the spatial resolution by a factor of 2 (using nearest neighbor upsampling for simplicity). The upsampled map is then merged with the corresponding bottom-up map (which undergoes a 1×1 convolutional layer to reduce channel dimensions) by element-wise addition. This process is iterated until the finest resolution map is generated. To start the iteration, we simply attach a 1×1 convolutional layer on C5 to produce the coarsest resolution map. Finally, we append a 3×3 convolution on each merged map to generate the final feature map, which is to reduce the aliasing effect of upsampling. This final set of feature maps is called {P2, P3, P4, P5}, corresponding to {C2, C3, C4, C5} that are respectively of the same spatial sizes.

Because all levels of the pyramid use shared classifiers/regressors as in a traditional featurized image pyramid, we fix the feature dimension (numbers of channels, denoted as d) in all the feature maps. We set d = 256 in this paper and thus all extra convolutional layers have 256-channel outputs. There are no non-linearities in these extra layers, which we have empirically found to have minor impacts. Simplicity is central to our design and we have found that our model is robust to many design choices. We have experimented with more sophisticated blocks (e.g., using multi-layer residual blocks [16] as the connections) and observed marginally better results. Designing better connection modules is not the focus of this paper, so we opt for the simple design described above.

---

### النسخة العربية

هدفنا هو الاستفادة من التسلسل الهرمي الهرمي للسمات في الشبكة الالتفافية، والذي يحتوي على دلالات من المستويات المنخفضة إلى العالية، وبناء هرم سمات ذي دلالات عالية المستوى في جميع الأنحاء. شبكة هرم السمات الناتجة ذات أغراض عامة وفي هذا البحث نركز على مقترحي النوافذ المنزلقة (شبكة مقترحات المناطق، RPN اختصارًا) [29] والكاشفات القائمة على المناطق (Fast R-CNN) [11]. نقوم أيضًا بتعميم شبكات FPN على مقترحات التجزئة حسب المثيل في القسم 6. تأخذ طريقتنا صورة أحادية المقياس بحجم تعسفي كمدخل، وتُخرج خرائط سمات ذات أحجام متناسبة على مستويات متعددة، بطريقة التفافية بالكامل. هذه العملية مستقلة عن معماريات الشبكات الالتفافية الأساسية (على سبيل المثال، [19، 36، 16])، وفي هذا البحث نقدم النتائج باستخدام ResNets [16]. يتضمن بناء الهرم الخاص بنا مسارًا من الأسفل إلى الأعلى، ومسارًا من الأعلى إلى الأسفل، واتصالات جانبية، كما هو موضح فيما يلي.

**المسار من الأسفل إلى الأعلى.** المسار من الأسفل إلى الأعلى هو الحساب الأمامي للشبكة الالتفافية الأساسية، والذي يحسب تسلسلاً هرميًا للسمات يتكون من خرائط سمات على عدة مقاييس بخطوة قياس تساوي 2. غالبًا ما توجد طبقات عديدة تنتج خرائط إخراج بنفس الحجم ونقول إن هذه الطبقات في نفس مرحلة الشبكة. بالنسبة لهرم السمات الخاص بنا، نحدد مستوى هرم واحد لكل مرحلة. نختار إخراج الطبقة الأخيرة من كل مرحلة كمجموعة مرجعية من خرائط السمات، والتي سنثريها لإنشاء الهرم الخاص بنا. هذا الاختيار طبيعي نظرًا لأن الطبقة الأعمق من كل مرحلة يجب أن يكون لها أقوى السمات.

على وجه التحديد، بالنسبة لشبكات ResNets [16] نستخدم تفعيلات السمات التي تُخرجها الكتلة المتبقية الأخيرة لكل مرحلة. نشير إلى إخراج هذه الكتل المتبقية الأخيرة بـ {C2, C3, C4, C5} لإخراجات conv2 و conv3 و conv4 و conv5، ونلاحظ أن لديها خطوات {4، 8، 16، 32} بكسل بالنسبة إلى صورة الإدخال. لا نُدرج conv1 في الهرم بسبب بصمتها الكبيرة في الذاكرة.

**المسار من الأعلى إلى الأسفل والاتصالات الجانبية.** يتخيل المسار من الأعلى إلى الأسفل سمات بدقة أعلى عن طريق رفع العينات مكانيًا لخرائط السمات الأخشن مكانيًا، ولكن الأقوى دلاليًا، من مستويات الهرم الأعلى. يتم بعد ذلك تحسين هذه السمات بالسمات من المسار من الأسفل إلى الأعلى عبر الاتصالات الجانبية. يدمج كل اتصال جانبي خرائط السمات بنفس الحجم المكاني من المسار من الأسفل إلى الأعلى والمسار من الأعلى إلى الأسفل. خريطة السمات من الأسفل إلى الأعلى ذات دلالات منخفضة المستوى، ولكن تفعيلاتها موضعية بدقة أكبر لأنها تم أخذ عينات فرعية منها عدد أقل من المرات.

يوضح الشكل 3 كتلة البناء التي تبني خرائط السمات من الأعلى إلى الأسفل. مع خريطة سمات بدقة أخشن، نرفع عينة الدقة المكانية بمعامل 2 (باستخدام رفع عينة أقرب جار للبساطة). يتم بعد ذلك دمج الخريطة المرفوعة العينة مع خريطة الأسفل إلى الأعلى المقابلة (التي تخضع لطبقة التفاف 1×1 لتقليل أبعاد القنوات) عن طريق الجمع عنصرًا بعنصر. تتكرر هذه العملية حتى يتم إنشاء خريطة الدقة الأدق. لبدء التكرار، نرفق ببساطة طبقة التفاف 1×1 على C5 لإنتاج خريطة الدقة الأخشن. أخيرًا، نُلحق التفافًا 3×3 على كل خريطة مدمجة لإنشاء خريطة السمات النهائية، وهو لتقليل تأثير التسمية المستعار لرفع العينة. تسمى مجموعة خرائط السمات النهائية هذه {P2, P3, P4, P5}، المقابلة لـ {C2, C3, C4, C5} التي لها على التوالي نفس الأحجام المكانية.

نظرًا لأن جميع مستويات الهرم تستخدم مصنفات/منحدرات مشتركة كما في هرم الصورة المُسمّت التقليدي، فإننا نحدد بُعد السمة (أعداد القنوات، المشار إليها بـ d) في جميع خرائط السمات. نضع d = 256 في هذا البحث وبالتالي فإن جميع الطبقات الالتفافية الإضافية لها مخرجات بـ 256 قناة. لا توجد لاخطية في هذه الطبقات الإضافية، والتي وجدنا تجريبيًا أن لها تأثيرات طفيفة. البساطة أمر محوري في تصميمنا ووجدنا أن نموذجنا قوي بالنسبة للعديد من خيارات التصميم. لقد جربنا كتل أكثر تعقيدًا (على سبيل المثال، استخدام كتل متبقية متعددة الطبقات [16] كاتصالات) ولاحظنا نتائج أفضل بشكل هامشي. تصميم وحدات اتصال أفضل ليس محور هذا البحث، لذلك نختار التصميم البسيط الموضح أعلاه.

---

### Translation Notes

- **Figures referenced:** Figure 3
- **Key terms introduced:**
  - bottom-up pathway: المسار من الأسفل إلى الأعلى
  - top-down pathway: المسار من الأعلى إلى الأسفل
  - lateral connections: الاتصالات الجانبية
  - feed-forward computation: الحساب الأمامي
  - network stage: مرحلة الشبكة
  - residual block: الكتلة المتبقية
  - upsampling: رفع العينات
  - nearest neighbor upsampling: رفع عينة أقرب جار
  - element-wise addition: الجمع عنصرًا بعنصر
  - aliasing effect: تأثير التسمية المستعار
  - memory footprint: بصمة في الذاكرة
- **Equations:** 0
- **Citations:** References to [11, 16, 19, 29, 36]
- **Special handling:**
  - Mathematical notation {C2, C3, C4, C5} and {P2, P3, P4, P5} kept as is
  - Technical terms like "RPN", "Fast R-CNN", "ResNets" kept in English
  - Convolution sizes "1×1", "3×3" kept as is
  - Channel dimension "d = 256" kept as is

### Quality Metrics

- Semantic equivalence: 0.91
- Technical accuracy: 0.93
- Readability: 0.88
- Glossary consistency: 0.86
- **Overall section score:** 0.89

### Back-Translation Check

Key phrases verified:
- "التسلسل الهرمي الهرمي للسمات" → Pyramidal feature hierarchy ✓
- "المسار من الأسفل إلى الأعلى" → Bottom-up pathway ✓
- "المسار من الأعلى إلى الأسفل" → Top-down pathway ✓
- "الاتصالات الجانبية" → Lateral connections ✓
- "رفع العينات" → Upsampling ✓
- "الجمع عنصرًا بعنصر" → Element-wise addition ✓
