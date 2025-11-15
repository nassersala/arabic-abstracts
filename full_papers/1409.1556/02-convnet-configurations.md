# Section 2: ConvNet Configurations
## القسم 2: تكوينات الشبكات الالتفافية

**Section:** methodology/architecture
**Translation Quality:** 0.87
**Glossary Terms Used:** ConvNet, architecture, convolution, layers, filters, max-pooling, fully-connected, ReLU, normalization, depth, parameters

---

### English Version

To measure the improvement brought by the increased ConvNet depth in a fair setting, all our ConvNet layer configurations are designed using the same principles, inspired by Ciresan et al. (2011); Krizhevsky et al. (2012). In this section, we first describe a generic layout of our ConvNet configurations (Sect. 2.1) and then detail the specific configurations used in the evaluation (Sect. 2.2). Our design choices are then discussed and compared to the prior art in Sect. 2.3.

**2.1 ARCHITECTURE**

During training, the input to our ConvNets is a fixed-size 224 × 224 RGB image. The only preprocessing we do is subtracting the mean RGB value, computed on the training set, from each pixel. The image is passed through a stack of convolutional (conv.) layers, where we use filters with a very small receptive field: 3 × 3 (which is the smallest size to capture the notion of left/right, up/down, center). In one of the configurations we also utilise 1 × 1 convolution filters, which can be seen as a linear transformation of the input channels (followed by non-linearity). The convolution stride is fixed to 1 pixel; the spatial padding of conv. layer input is such that the spatial resolution is preserved after convolution, i.e. the padding is 1 pixel for 3 × 3 conv. layers. Spatial pooling is carried out by five max-pooling layers, which follow some of the conv. layers (not all the conv. layers are followed by max-pooling). Max-pooling is performed over a 2 × 2 pixel window, with stride 2.

A stack of convolutional layers (which has a different depth in different architectures) is followed by three Fully-Connected (FC) layers: the first two have 4096 channels each, the third performs 1000-way ILSVRC classification and thus contains 1000 channels (one for each class). The final layer is the soft-max layer. The configuration of the fully connected layers is the same in all networks.

All hidden layers are equipped with the rectification (ReLU (Krizhevsky et al., 2012)) non-linearity. We note that none of our networks (except for one) contain Local Response Normalisation (LRN) normalisation (Krizhevsky et al., 2012): as will be shown in Sect. 4, such normalisation does not improve the performance on the ILSVRC dataset, but leads to increased memory consumption and computation time. Where applicable, the parameters for the LRN layer are those of (Krizhevsky et al., 2012).

**2.2 CONFIGURATIONS**

The ConvNet configurations, evaluated in this paper, are outlined in Table 1, one per column. In the following we will refer to the nets by their names (A–E). All configurations follow the generic design presented in Sect. 2.1, and differ only in the depth: from 11 weight layers in the network A (8 conv. and 3 FC layers) to 19 weight layers in the network E (16 conv. and 3 FC layers). The width of conv. layers (the number of channels) is rather small, starting from 64 in the first layer and then increasing by a factor of 2 after each max-pooling layer, until it reaches 512.

In Table 2 we report the number of parameters for each configuration. In spite of a large depth, the number of weights in our nets is not greater than the number of weights in a more shallow net with larger conv. layer widths and receptive fields (144M weights in (Sermanet et al., 2014)).

**2.3 DISCUSSION**

Our ConvNet configurations are quite different from the ones used in the top-performing entries of the ILSVRC-2012 (Krizhevsky et al., 2012) and ILSVRC-2013 competitions (Zeiler & Fergus, 2013; Sermanet et al., 2014). Rather than using relatively large receptive fields in the first conv. layers (e.g. 11×11 with stride 4 in (Krizhevsky et al., 2012), or 7×7 with stride 2 in (Zeiler & Fergus, 2013; Sermanet et al., 2014)), we use very small 3 × 3 receptive fields throughout the whole net, which are convolved with the input at every pixel (with stride 1). It is easy to see that a stack of two 3×3 conv. layers (without spatial pooling in between) has an effective receptive field of 5×5; three such layers have a 7 × 7 effective receptive field. So what have we gained by using, for instance, a stack of three 3×3 conv. layers instead of a single 7×7 layer? First, we incorporate three non-linear rectification layers instead of a single one, which makes the decision function more discriminative. Second, we decrease the number of parameters: assuming that both the input and the output of a three-layer 3 × 3 convolution stack has C channels, the stack is parametrised by 3(3²C²) = 27C² weights; at the same time, a single 7 × 7 conv. layer would require 7²C² = 49C² parameters, i.e. 81% more. This can be seen as imposing a regularisation on the 7 × 7 conv. filters, forcing them to have a decomposition through the 3 × 3 filters (with non-linearity injected in between).

The incorporation of 1 × 1 conv. layers (configuration C, Table 1) is a way to increase the non-linearity of the decision function without affecting the receptive fields of the conv. layers. Even though in our case the 1 × 1 convolution is essentially a linear projection onto the space of the same dimensionality (the number of input and output channels is the same), an additional non-linearity is introduced by the rectification function. It should be noted that 1×1 conv. layers have recently been utilised in the "Network in Network" architecture of Lin et al. (2014).

Small-size convolution filters have been previously used by Ciresan et al. (2011), but their nets are significantly less deep than ours, and they did not evaluate on the large-scale ILSVRC dataset. Goodfellow et al. (2014) applied deep ConvNets (11 weight layers) to the task of street number recognition, and showed that the increased depth led to better performance. GoogLeNet (Szegedy et al., 2014), a top-performing entry of the ILSVRC-2014 classification task, was developed independently of our work, but is similar in that it is based on very deep ConvNets (22 weight layers) and small convolution filters (apart from 3 × 3, they also use 1 × 1 and 5 × 5 convolutions). Their network topology is, however, more complex than ours, and the spatial resolution of the feature maps is reduced more aggressively in the first layers to decrease the amount of computation. As will be shown in Sect. 4.5, our model is outperforming that of Szegedy et al. (2014) in terms of the single-network classification accuracy.

---

### النسخة العربية

لقياس التحسين الذي يجلبه زيادة عمق الشبكة الالتفافية في بيئة عادلة، تم تصميم جميع تكوينات طبقات الشبكة الالتفافية الخاصة بنا باستخدام نفس المبادئ، مستوحاة من Ciresan et al. (2011); Krizhevsky et al. (2012). في هذا القسم، نصف أولاً التخطيط العام لتكوينات الشبكة الالتفافية الخاصة بنا (القسم 2.1) ثم نوضح بالتفصيل التكوينات المحددة المستخدمة في التقييم (القسم 2.2). ثم تتم مناقشة خيارات التصميم الخاصة بنا ومقارنتها بالأعمال السابقة في القسم 2.3.

**2.1 المعمارية**

أثناء التدريب، يكون المدخل إلى شبكاتنا الالتفافية عبارة عن صورة RGB ذات حجم ثابت 224 × 224. المعالجة المسبقة الوحيدة التي نقوم بها هي طرح متوسط قيمة RGB، المحسوبة على مجموعة التدريب، من كل بكسل. تمر الصورة عبر مجموعة من الطبقات الالتفافية (conv.)، حيث نستخدم مرشحات ذات مجال استقبال صغير جداً: 3 × 3 (وهو أصغر حجم لالتقاط مفهوم يسار/يمين، أعلى/أسفل، مركز). في أحد التكوينات نستخدم أيضاً مرشحات التفاف 1 × 1، والتي يمكن رؤيتها كتحويل خطي لقنوات المدخل (متبوعاً باللاخطية). خطوة الالتفاف ثابتة عند 1 بكسل؛ الحشو المكاني لمدخل الطبقة الالتفافية بحيث يتم الحفاظ على الدقة المكانية بعد الالتفاف، أي أن الحشو يكون 1 بكسل لطبقات conv. بحجم 3 × 3. يتم تنفيذ التجميع المكاني بواسطة خمس طبقات تجميع أقصى (max-pooling)، والتي تتبع بعض طبقات conv. (ليست كل طبقات conv. متبوعة بتجميع أقصى). يتم إجراء التجميع الأقصى عبر نافذة بكسل 2 × 2، بخطوة 2.

تتبع مجموعة من الطبقات الالتفافية (التي لها عمق مختلف في معماريات مختلفة) ثلاث طبقات متصلة بالكامل (FC): الأولتان لهما 4096 قناة لكل منهما، والثالثة تنفذ تصنيف ILSVRC ذو 1000 طريق وبالتالي تحتوي على 1000 قناة (واحدة لكل صنف). الطبقة الأخيرة هي طبقة soft-max. تكوين الطبقات المتصلة بالكامل هو نفسه في جميع الشبكات.

جميع الطبقات المخفية مجهزة بدالة التصحيح اللاخطية (ReLU (Krizhevsky et al., 2012)). نلاحظ أنه لا توجد أي من شبكاتنا (باستثناء واحدة) تحتوي على تطبيع الاستجابة المحلية (LRN) (Krizhevsky et al., 2012): كما سيتم عرضه في القسم 4، مثل هذا التطبيع لا يحسن الأداء على مجموعة بيانات ILSVRC، ولكنه يؤدي إلى زيادة استهلاك الذاكرة ووقت الحساب. عند الاقتضاء، فإن المعاملات لطبقة LRN هي تلك الخاصة بـ (Krizhevsky et al., 2012).

**2.2 التكوينات**

تكوينات الشبكة الالتفافية، التي تم تقييمها في هذه الورقة، موضحة في الجدول 1، واحدة لكل عمود. فيما يلي سنشير إلى الشبكات بأسمائها (A-E). تتبع جميع التكوينات التصميم العام المقدم في القسم 2.1، وتختلف فقط في العمق: من 11 طبقة وزنية في الشبكة A (8 طبقات conv. و 3 طبقات FC) إلى 19 طبقة وزنية في الشبكة E (16 طبقة conv. و 3 طبقات FC). عرض طبقات conv. (عدد القنوات) صغير نسبياً، يبدأ من 64 في الطبقة الأولى ثم يزيد بمعامل 2 بعد كل طبقة تجميع أقصى، حتى يصل إلى 512.

في الجدول 2 نقرر عدد المعاملات لكل تكوين. على الرغم من العمق الكبير، فإن عدد الأوزان في شبكاتنا ليس أكبر من عدد الأوزان في شبكة أكثر سطحية بعروض طبقات conv. ومجالات استقبال أكبر (144 مليون وزن في (Sermanet et al., 2014)).

**2.3 المناقشة**

تكوينات شبكتنا الالتفافية مختلفة تماماً عن تلك المستخدمة في المشاركات الأفضل أداءً في مسابقات ILSVRC-2012 (Krizhevsky et al., 2012) و ILSVRC-2013 (Zeiler & Fergus, 2013; Sermanet et al., 2014). بدلاً من استخدام مجالات استقبال كبيرة نسبياً في طبقات conv. الأولى (على سبيل المثال 11×11 بخطوة 4 في (Krizhevsky et al., 2012)، أو 7×7 بخطوة 2 في (Zeiler & Fergus, 2013; Sermanet et al., 2014))، نستخدم مجالات استقبال صغيرة جداً 3 × 3 في جميع أنحاء الشبكة بأكملها، والتي يتم التفافها مع المدخل عند كل بكسل (بخطوة 1). من السهل أن نرى أن مجموعة من طبقتي conv. بحجم 3×3 (بدون تجميع مكاني بينهما) لها مجال استقبال فعال بحجم 5×5؛ ثلاث طبقات من هذا القبيل لها مجال استقبال فعال 7 × 7. إذن ماذا استفدنا باستخدام، على سبيل المثال، مجموعة من ثلاث طبقات conv. بحجم 3×3 بدلاً من طبقة واحدة بحجم 7×7؟ أولاً، ندمج ثلاث طبقات تصحيح لاخطية بدلاً من طبقة واحدة، مما يجعل دالة القرار أكثر تمييزاً. ثانياً، نقلل عدد المعاملات: بافتراض أن كلاً من المدخل والمخرج لمجموعة التفاف ثلاثية الطبقات 3 × 3 لها C قناة، فإن المجموعة تكون معلمة بـ 3(3²C²) = 27C² وزناً؛ في الوقت نفسه، ستتطلب طبقة conv. واحدة بحجم 7 × 7 معاملات 7²C² = 49C²، أي أكثر بنسبة 81٪. يمكن رؤية هذا كفرض تنظيم على مرشحات conv. بحجم 7 × 7، مما يجبرها على الحصول على تحلل من خلال مرشحات 3 × 3 (مع حقن اللاخطية بينهما).

إن دمج طبقات conv. بحجم 1 × 1 (التكوين C، الجدول 1) هو وسيلة لزيادة اللاخطية لدالة القرار دون التأثير على مجالات الاستقبال لطبقات conv. على الرغم من أنه في حالتنا يكون الالتفاف 1 × 1 في الأساس إسقاطاً خطياً على فضاء نفس الأبعاد (عدد قنوات المدخل والمخرج هو نفسه)، إلا أنه يتم إدخال لاخطية إضافية بواسطة دالة التصحيح. تجدر الإشارة إلى أن طبقات conv. بحجم 1×1 تم استخدامها مؤخراً في معمارية "Network in Network" لـ Lin et al. (2014).

تم استخدام مرشحات التفاف صغيرة الحجم سابقاً بواسطة Ciresan et al. (2011)، لكن شبكاتهم أقل عمقاً بكثير من شبكاتنا، ولم يقيّموا على مجموعة بيانات ILSVRC واسعة النطاق. طبق Goodfellow et al. (2014) شبكات التفافية عميقة (11 طبقة وزنية) على مهمة التعرف على أرقام الشوارع، وأظهروا أن زيادة العمق أدت إلى أداء أفضل. تم تطوير GoogLeNet (Szegedy et al., 2014)، وهي مشاركة عالية الأداء في مهمة تصنيف ILSVRC-2014، بشكل مستقل عن عملنا، ولكنها مشابهة في أنها تستند إلى شبكات التفافية عميقة جداً (22 طبقة وزنية) ومرشحات التفاف صغيرة (بصرف النظر عن 3 × 3، يستخدمون أيضاً التفافات 1 × 1 و 5 × 5). ومع ذلك، فإن طوبولوجيا شبكتهم أكثر تعقيداً من شبكتنا، ويتم تقليل الدقة المكانية لخرائط الميزات بشكل أكثر عدوانية في الطبقات الأولى لتقليل كمية الحساب. كما سيتم عرضه في القسم 4.5، فإن نموذجنا يتفوق على نموذج Szegedy et al. (2014) من حيث دقة تصنيف الشبكة الواحدة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** receptive field, stride, spatial padding, max-pooling, fully-connected layers, soft-max, ReLU, Local Response Normalisation (LRN), weight layers, channels, configuration, depth, parameters, regularisation
- **Equations:** Mathematical expressions for parameter counts: 3(3²C²) = 27C² and 7²C² = 49C²
- **Citations:** Multiple references to Krizhevsky, Zeiler & Fergus, Sermanet, Lin, Goodfellow, Szegedy (GoogLeNet)
- **Special handling:** Preserved Table 1 and Table 2 references; kept mathematical notation intact

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
