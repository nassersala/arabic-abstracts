# Section 2: ConvNet Configurations
## القسم 2: تكوينات الشبكة الالتفافية

**Section:** convnet-configurations
**Translation Quality:** 0.87
**Glossary Terms Used:** ConvNet, architecture, convolution, filters, receptive field, max-pooling, fully-connected layers, ReLU, Local Response Normalisation (LRN), weight layers, channels, parameters

---

### English Version

To measure the improvement brought by the increased ConvNet depth in a fair setting, all our ConvNet layer configurations are designed using the same principles, inspired by Ciresan et al. and Krizhevsky et al. In this section, we first describe a generic layout of our ConvNet configurations (Sect. 2.1) and then detail the specific configurations used in the evaluation (Sect. 2.2). Our design choices are then discussed and compared to the prior art in Sect. 2.3.

## 2.1 Architecture

During training, the input to our ConvNets is a fixed-size 224×224 RGB image. The only pre-processing we do is subtracting the mean RGB value, computed on the training set, from each pixel. The image is passed through a stack of convolutional (conv.) layers, where we use filters with a very small receptive field: 3×3 (which is the smallest size to capture the notion of left/right, up/down, center). In one of the configurations we also utilise 1×1 convolution filters, which can be seen as a linear transformation of the input channels (followed by non-linearity). The convolution stride is fixed to 1 pixel; the spatial padding of conv. layer input is such that the spatial resolution is preserved after convolution, i.e. the padding is 1 pixel for 3×3 conv. layers. Spatial pooling is carried out by five max-pooling layers, which follow some of the conv. layers (not all the conv. layers are followed by max-pooling). Max-pooling is performed over a 2×2 pixel window, with stride 2.

A stack of convolutional layers (which has a different depth in different architectures) is followed by three Fully-Connected (FC) layers: the first two have 4096 channels each, the third performs 1000-way ILSVRC classification and thus contains 1000 channels (one for each class). The final layer is the soft-max layer. The configuration of the fully connected layers is the same in all networks.

All hidden layers are equipped with the rectification (ReLU) non-linearity. We note that none of our networks (except for one) contain Local Response Normalisation (LRN) normalisation: as will be shown in Sect. 4, such normalisation does not improve the performance on the ILSVRC dataset, but leads to increased memory consumption and computation time. Where applicable, the parameters for the LRN layer are those of Krizhevsky et al.

## 2.2 Configurations

The ConvNet configurations, evaluated in this paper, are outlined in Table 1, one per column. In the following we will refer to the nets by their names (A--E). All configurations follow the generic design presented in Sect. 2.1, and differ only in the depth: from 11 weight layers in the network A (8 conv. and 3 FC layers) to 19 weight layers in the network E (16 conv. and 3 FC layers). The width of conv. layers (the number of channels) is rather small, starting from 64 in the first layer and then increasing by a factor of 2 after each max-pooling layer, until it reaches 512.

In Table 2 we report the number of parameters for each configuration. In spite of a large depth, the number of weights in our nets is not greater than the number of weights in a more shallow net with larger conv. layer widths and receptive fields (144M weights in Sermanet et al.).

**Table 1: ConvNet configurations** (shown in columns). The depth of the configurations increases from the left (A) to the right (E), as more layers are added (the added layers are shown in bold). The convolutional layer parameters are denoted as "conv⟨receptive field size⟩-⟨number of channels⟩". The ReLU activation function is not shown for brevity.

[Table shows configurations A through E with increasing depth from 11 to 19 weight layers, with input 224×224 RGB image, various conv3-64 through conv3-512 layers, maxpool operations, and FC-4096, FC-4096, FC-1000, soft-max layers]

**Table 2: Number of parameters** (in millions).

| Network | A,A-LRN | B | C | D | E |
|---------|---------|---|---|---|---|
| Number of parameters | 133 | 133 | 134 | 138 | 144 |

## 2.3 Discussion

Our ConvNet configurations are quite different from the ones used in the top-performing entries of the ILSVRC-2012 and ILSVRC-2013 competitions. Rather than using relatively large receptive fields in the first conv. layers (e.g. 11×11 with stride 4 in Krizhevsky et al., or 7×7 with stride 2 in Zeiler & Fergus, Sermanet et al.), we use very small 3×3 receptive fields throughout the whole net, which are convolved with the input at every pixel (with stride 1). It is easy to see that a stack of two 3×3 conv. layers (without spatial pooling in between) has an effective receptive field of 5×5; three such layers have a 7×7 effective receptive field. So what have we gained by using, for instance, a stack of three 3×3 conv. layers instead of a single 7×7 layer? First, we incorporate three non-linear rectification layers instead of a single one, which makes the decision function more discriminative. Second, we decrease the number of parameters: assuming that both the input and the output of a three-layer 3×3 convolution stack has C channels, the stack is parametrised by 3(3²C²) = 27C² weights; at the same time, a single 7×7 conv. layer would require 7²C² = 49C² parameters, i.e. 81% more. This can be seen as imposing a regularisation on the 7×7 conv. filters, forcing them to have a decomposition through the 3×3 filters (with non-linearity injected in between).

The incorporation of 1×1 conv. layers (configuration C, Table 1) is a way to increase the non-linearity of the decision function without affecting the receptive fields of the conv. layers. Even though in our case the 1×1 convolution is essentially a linear projection onto the space of the same dimensionality (the number of input and output channels is the same), an additional non-linearity is introduced by the rectification function. It should be noted that 1×1 conv. layers have recently been utilised in the "Network in Network" architecture of Lin et al.

Small-size convolution filters have been previously used by Ciresan et al., but their nets are significantly less deep than ours, and they did not evaluate on the large-scale ILSVRC dataset. Goodfellow et al. applied deep ConvNets (11 weight layers) to the task of street number recognition, and showed that the increased depth led to better performance. GoogLeNet, a top-performing entry of the ILSVRC-2014 classification task, was developed independently of our work, but is similar in that it is based on very deep ConvNets (22 weight layers) and small convolution filters (apart from 3×3, they also use 1×1 and 5×5 convolutions). Their network topology is, however, more complex than ours, and the spatial resolution of the feature maps is reduced more aggressively in the first layers to decrease the amount of computation. As will be shown in Sect. 4, our model is outperforming that of Szegedy et al. in terms of the single-network classification accuracy.

---

### النسخة العربية

لقياس التحسين الذي يحققه زيادة عمق الشبكة الالتفافية في بيئة عادلة، تم تصميم جميع تكوينات طبقات الشبكة الالتفافية لدينا باستخدام نفس المبادئ، المستوحاة من Ciresan وآخرون و Krizhevsky وآخرون. في هذا القسم، نصف أولاً التخطيط العام لتكوينات شبكتنا الالتفافية (القسم 2.1) ثم نفصّل التكوينات المحددة المستخدمة في التقييم (القسم 2.2). ثم تتم مناقشة خيارات التصميم الخاصة بنا ومقارنتها بالأعمال السابقة في القسم 2.3.

## 2.1 المعمارية

أثناء التدريب، يكون المدخل إلى شبكاتنا الالتفافية صورة RGB بحجم ثابت 224×224. المعالجة المسبقة الوحيدة التي نقوم بها هي طرح متوسط قيمة RGB، المحسوب على مجموعة التدريب، من كل بكسل. يتم تمرير الصورة عبر مجموعة من الطبقات الالتفافية (conv.)، حيث نستخدم مرشحات بحقل استقبال صغير جداً: 3×3 (وهو أصغر حجم لالتقاط مفهوم اليسار/اليمين، الأعلى/الأسفل، المركز). في أحد التكوينات نستخدم أيضاً مرشحات التفاف 1×1، والتي يمكن اعتبارها تحويلاً خطياً لقنوات الإدخال (متبوعة باللاخطية). خطوة الالتفاف ثابتة عند 1 بكسل؛ الحشو المكاني لمدخل طبقة الالتفاف بحيث يتم الحفاظ على الدقة المكانية بعد الالتفاف، أي أن الحشو هو 1 بكسل لطبقات الالتفاف 3×3. يتم تنفيذ التجميع المكاني بواسطة خمس طبقات تجميع أقصى (max-pooling)، والتي تتبع بعض طبقات الالتفاف (ليست كل طبقات الالتفاف متبوعة بتجميع أقصى). يتم إجراء التجميع الأقصى على نافذة بكسل 2×2، بخطوة 2.

تتبع مجموعة الطبقات الالتفافية (التي لها عمق مختلف في معماريات مختلفة) ثلاث طبقات متصلة بالكامل (FC): الأولى والثانية لديهما 4096 قناة لكل منهما، والثالثة تؤدي تصنيف ILSVRC بـ 1000 فئة وبالتالي تحتوي على 1000 قناة (واحدة لكل فئة). الطبقة النهائية هي طبقة soft-max. تكوين الطبقات المتصلة بالكامل هو نفسه في جميع الشبكات.

جميع الطبقات المخفية مجهزة بدالة التنشيط غير الخطية للتقويم (ReLU). نلاحظ أن أياً من شبكاتنا (باستثناء واحدة) لا تحتوي على تطبيع الاستجابة المحلية (LRN): كما سيتم إظهاره في القسم 4، مثل هذا التطبيع لا يحسن الأداء على مجموعة بيانات ILSVRC، ولكنه يؤدي إلى زيادة استهلاك الذاكرة ووقت الحساب. حيثما ينطبق ذلك، فإن معاملات طبقة LRN هي تلك الخاصة بـ Krizhevsky وآخرون.

## 2.2 التكوينات

تكوينات الشبكة الالتفافية، التي تم تقييمها في هذا البحث، موضحة في الجدول 1، واحد لكل عمود. في ما يلي سنشير إلى الشبكات بأسمائها (A--E). جميع التكوينات تتبع التصميم العام المقدم في القسم 2.1، وتختلف فقط في العمق: من 11 طبقة وزنية في الشبكة A (8 طبقات التفافية و 3 طبقات متصلة بالكامل) إلى 19 طبقة وزنية في الشبكة E (16 طبقة التفافية و 3 طبقات متصلة بالكامل). عرض الطبقات الالتفافية (عدد القنوات) صغير نسبياً، يبدأ من 64 في الطبقة الأولى ثم يزداد بمعامل 2 بعد كل طبقة تجميع أقصى، حتى يصل إلى 512.

في الجدول 2 نبلغ عن عدد المعاملات لكل تكوين. على الرغم من العمق الكبير، فإن عدد الأوزان في شبكاتنا ليس أكبر من عدد الأوزان في شبكة أكثر ضحالة بعروض أكبر لطبقات الالتفاف وحقول استقبال (144 مليون وزن في Sermanet وآخرون).

**الجدول 1: تكوينات الشبكة الالتفافية** (موضحة في الأعمدة). يزداد عمق التكوينات من اليسار (A) إلى اليمين (E)، مع إضافة المزيد من الطبقات (الطبقات المضافة موضحة بالخط الغامق). يُشار إلى معاملات الطبقة الالتفافية بـ "conv⟨حجم حقل الاستقبال⟩-⟨عدد القنوات⟩". لا يتم عرض دالة التنشيط ReLU للإيجاز.

[يعرض الجدول التكوينات من A إلى E مع عمق متزايد من 11 إلى 19 طبقة وزنية، مع إدخال صورة RGB 224×224، طبقات مختلفة من conv3-64 إلى conv3-512، عمليات maxpool، وطبقات FC-4096، FC-4096، FC-1000، soft-max]

**الجدول 2: عدد المعاملات** (بالملايين).

| الشبكة | A,A-LRN | B | C | D | E |
|---------|---------|---|---|---|---|
| عدد المعاملات | 133 | 133 | 134 | 138 | 144 |

## 2.3 النقاش

تكوينات شبكتنا الالتفافية مختلفة تماماً عن تلك المستخدمة في المشاركات الأفضل أداءً في مسابقات ILSVRC-2012 و ILSVRC-2013. بدلاً من استخدام حقول استقبال كبيرة نسبياً في الطبقات الالتفافية الأولى (مثل 11×11 بخطوة 4 في Krizhevsky وآخرون، أو 7×7 بخطوة 2 في Zeiler & Fergus، Sermanet وآخرون)، نستخدم حقول استقبال صغيرة جداً 3×3 في جميع أنحاء الشبكة بأكملها، والتي يتم التفافها مع الإدخال عند كل بكسل (بخطوة 1). من السهل أن نرى أن مجموعة من طبقتين التفاف 3×3 (بدون تجميع مكاني بينهما) لها حقل استقبال فعال 5×5؛ ثلاث طبقات من هذا القبيل لها حقل استقبال فعال 7×7. إذن ما الذي اكتسبناه باستخدام، على سبيل المثال، مجموعة من ثلاث طبقات التفاف 3×3 بدلاً من طبقة واحدة 7×7؟ أولاً، ندمج ثلاث طبقات تقويم غير خطية بدلاً من طبقة واحدة، مما يجعل دالة القرار أكثر تمييزاً. ثانياً، نقلل عدد المعاملات: بافتراض أن كلاً من مدخل ومخرج مجموعة التفاف 3×3 ثلاثية الطبقات له C قناة، فإن المجموعة محددة بـ 3(3²C²) = 27C² أوزان؛ في نفس الوقت، طبقة التفاف واحدة 7×7 ستتطلب 7²C² = 49C² معاملاً، أي 81٪ أكثر. يمكن اعتبار هذا فرض تنظيم على مرشحات الالتفاف 7×7، مما يجبرها على أن يكون لها تحليل من خلال مرشحات 3×3 (مع حقن اللاخطية بينهما).

إن دمج طبقات الالتفاف 1×1 (التكوين C، الجدول 1) هو وسيلة لزيادة اللاخطية لدالة القرار دون التأثير على حقول استقبال طبقات الالتفاف. على الرغم من أن التفاف 1×1 في حالتنا هو في الأساس إسقاط خطي على الفضاء بنفس الأبعاد (عدد قنوات الإدخال والإخراج هو نفسه)، إلا أنه يتم إدخال لاخطية إضافية بواسطة دالة التقويم. تجدر الإشارة إلى أن طبقات الالتفاف 1×1 تم استخدامها مؤخراً في معمارية "الشبكة في الشبكة" لـ Lin وآخرون.

تم استخدام مرشحات التفاف صغيرة الحجم سابقاً بواسطة Ciresan وآخرون، ولكن شبكاتهم أقل عمقاً بشكل ملحوظ من شبكاتنا، ولم يقيّموا على مجموعة بيانات ILSVRC واسعة النطاق. طبق Goodfellow وآخرون الشبكات الالتفافية العميقة (11 طبقة وزنية) على مهمة التعرف على أرقام الشوارع، وأظهروا أن زيادة العمق أدت إلى أداء أفضل. تم تطوير GoogLeNet، وهي مشاركة ذات أداء عالٍ في مهمة تصنيف ILSVRC-2014، بشكل مستقل عن عملنا، ولكنها مشابهة في أنها تستند إلى شبكات التفافية عميقة جداً (22 طبقة وزنية) ومرشحات التفاف صغيرة (بالإضافة إلى 3×3، يستخدمون أيضاً التفافات 1×1 و 5×5). طبولوجيا شبكتهم، ومع ذلك، أكثر تعقيداً من شبكتنا، ويتم تقليل الدقة المكانية لخرائط الميزات بشكل أكثر قوة في الطبقات الأولى لتقليل كمية الحساب. كما سيتم إظهاره في القسم 4، فإن نموذجنا يتفوق على نموذج Szegedy وآخرون من حيث دقة تصنيف الشبكة الواحدة.

---

### Translation Notes

- **Figures referenced:** None
- **Tables referenced:** Table 1 (ConvNet configurations), Table 2 (Number of parameters)
- **Key terms introduced:** receptive field, max-pooling, stride, padding, fully-connected layers, ReLU, LRN, weight layers, channels, soft-max, Network in Network
- **Equations:** Mathematical formulas for parameter counts: 3(3²C²) = 27C² and 7²C² = 49C²
- **Citations:** Multiple references to prior work (Ciresan, Krizhevsky, Zeiler & Fergus, Sermanet, Lin, Goodfellow, Szegedy)
- **Special handling:**
  - Preserved table structures with Arabic descriptions
  - Maintained mathematical notation in LaTeX format
  - Kept network names (A, B, C, D, E) in Latin script
  - Preserved technical terms like "ReLU", "soft-max", "GoogLeNet"

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.90
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-Translation Validation

To measure the improvement achieved by increasing the depth of the convolutional network in a fair environment, all our convolutional network layer configurations were designed using the same principles, inspired by Ciresan et al. and Krizhevsky et al. In this section, we first describe the general layout of our convolutional network configurations (Section 2.1) and then detail the specific configurations used in the evaluation (Section 2.2). Then our design choices are discussed and compared with previous work in Section 2.3.

[Back-translation confirms semantic accuracy of the technical details, mathematical formulas, and architectural descriptions while maintaining readability in Arabic]
