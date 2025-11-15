# Section 5: Discussion
## القسم 5: النقاش

**Section:** Discussion
**Translation Quality:** 0.87
**Glossary Terms Used:** model compactness (إدماج النموذج), feature reuse (إعادة استخدام الميزات), concatenation (ربط), summation (جمع), feature-maps (خرائط الميزات), parameters (معاملات), implicit deep supervision (إشراف عميق ضمني), loss function (دالة الخسارة), gradient (تدرج), transition layers (طبقات انتقالية), stochastic depth (عمق عشوائي), residual networks (شبكات متبقية), deterministic (حتمي), regularization (تنظيم), heat-map (خريطة حرارية), classifier (مصنف)

---

### English Version

Superficially, DenseNets are quite similar to ResNets: Eq. (2) differs from Eq. (1) only in that the inputs to Hₗ(·) are concatenated instead of summed. However, the implications of this seemingly small modification lead to substantially different behaviors of the two network architectures.

**Model compactness.** As a direct consequence of the input concatenation, the feature-maps learned by any of the DenseNet layers can be accessed by all subsequent layers. This encourages feature reuse throughout the network, and leads to more compact models.

The left two plots in Figure 4 show the result of an experiment that aims to compare the parameter efficiency of all variants of DenseNets (left) and also a comparable ResNet architecture (middle). We train multiple small networks with varying depths on C10+ and plot their test accuracies as a function of network parameters. In comparison with other popular network architectures, such as AlexNet [16] or VGG-net [29], ResNets with pre-activation use fewer parameters while typically achieving better results [12]. Hence, we compare DenseNet (k = 12) against this architecture. The training setting for DenseNet is kept the same as in the previous section.

The graph shows that DenseNet-BC is consistently the most parameter efficient variant of DenseNet. Further, to achieve the same level of accuracy, DenseNet-BC only requires around 1/3 of the parameters of ResNets (middle plot). This result is in line with the results on ImageNet we presented in Figure 3. The right plot in Figure 4 shows that a DenseNet-BC with only 0.8M trainable parameters is able to achieve comparable accuracy as the 1001-layer (pre-activation) ResNet [12] with 10.2M parameters.

**Implicit Deep Supervision.** One explanation for the improved accuracy of dense convolutional networks may be that individual layers receive additional supervision from the loss function through the shorter connections. One can interpret DenseNets to perform a kind of "deep supervision". The benefits of deep supervision have previously been shown in deeply-supervised nets (DSN; [20]), which have classifiers attached to every hidden layer, enforcing the intermediate layers to learn discriminative features.

DenseNets perform a similar deep supervision in an implicit fashion: a single classifier on top of the network provides direct supervision to all layers through at most two or three transition layers. However, the loss function and gradient of DenseNets are substantially less complicated, as the same loss function is shared between all layers.

**Stochastic vs. deterministic connection.** There is an interesting connection between dense convolutional networks and stochastic depth regularization of residual networks [13]. In stochastic depth, layers in residual networks are randomly dropped, which creates direct connections between the surrounding layers. As the pooling layers are never dropped, the network results in a similar connectivity pattern as DenseNet: there is a small probability for any two layers, between the same pooling layers, to be directly connected—if all intermediate layers are randomly dropped. Although the methods are ultimately quite different, the DenseNet interpretation of stochastic depth may provide insights into the success of this regularizer.

**Feature Reuse.** By design, DenseNets allow layers access to feature-maps from all of its preceding layers (although sometimes through transition layers). We conduct an experiment to investigate if a trained network takes advantage of this opportunity. We first train a DenseNet on C10+ with L = 40 and k = 12. For each convolutional layer ℓ within a block, we compute the average (absolute) weight assigned to connections with layer s. Figure 5 shows a heat-map for all three dense blocks. The average absolute weight serves as a surrogate for the dependency of a convolutional layer on its preceding layers. A red dot in position (ℓ, s) indicates that the layer ℓ makes, on average, strong use of feature-maps produced s-layers before. Several observations can be made from the plot:

1. All layers spread their weights over many inputs within the same block. This indicates that features extracted by very early layers are, indeed, directly used by deep layers throughout the same dense block.

2. The weights of the transition layers also spread their weight across all layers within the preceding dense block, indicating information flow from the first to the last layers of the DenseNet through few indirections.

3. The layers within the second and third dense block consistently assign the least weight to the outputs of the transition layer (the top row of the triangles), indicating that the transition layer outputs many redundant features (with low weight on average). This is in keeping with the strong results of DenseNet-BC where exactly these outputs are compressed.

4. Although the final classification layer, shown on the very right, also uses weights across the entire dense block, there seems to be a concentration towards final feature-maps, suggesting that there may be some more high-level features produced late in the network.

---

### النسخة العربية

ظاهرياً، شبكات DenseNets مشابهة تماماً لشبكات ResNets: تختلف المعادلة (2) عن المعادلة (1) فقط في أن المدخلات إلى Hₗ(·) يتم ربطها بدلاً من جمعها. ومع ذلك، فإن آثار هذا التعديل الصغير ظاهرياً تؤدي إلى سلوكيات مختلفة بشكل كبير لمعماريتي الشبكة.

**إدماج النموذج.** كنتيجة مباشرة لربط المدخلات، يمكن لجميع الطبقات اللاحقة الوصول إلى خرائط الميزات المتعلمة بواسطة أي من طبقات DenseNet. يشجع هذا على إعادة استخدام الميزات في جميع أنحاء الشبكة، ويؤدي إلى نماذج أكثر إدماجاً.

تُظهر الرسمان البيانيان الأيسران في الشكل 4 نتيجة تجربة تهدف إلى مقارنة كفاءة المعاملات لجميع متغيرات DenseNets (يساراً) وأيضاً معمارية ResNet قابلة للمقارنة (في الوسط). نقوم بتدريب شبكات صغيرة متعددة بأعماق متفاوتة على C10+ ونرسم دقة الاختبار الخاصة بها كدالة لمعاملات الشبكة. بالمقارنة مع معماريات الشبكات الشائعة الأخرى، مثل AlexNet [16] أو VGG-net [29]، تستخدم شبكات ResNets مع التنشيط المسبق معاملات أقل بينما تحقق عادةً نتائج أفضل [12]. لذلك، نقارن DenseNet (k = 12) مع هذه المعمارية. يتم الحفاظ على إعداد التدريب لـ DenseNet كما هو في القسم السابق.

يُظهر الرسم البياني أن DenseNet-BC هو باستمرار المتغير الأكثر كفاءة في المعاملات من DenseNet. علاوة على ذلك، لتحقيق نفس مستوى الدقة، يتطلب DenseNet-BC فقط حوالي 1/3 من معاملات ResNets (الرسم الأوسط). هذه النتيجة تتماشى مع النتائج على ImageNet التي قدمناها في الشكل 3. يُظهر الرسم الأيمن في الشكل 4 أن DenseNet-BC بمعاملات قابلة للتدريب تبلغ 0.8M فقط قادر على تحقيق دقة مماثلة لشبكة ResNet (التنشيط المسبق) المكونة من 1001 طبقة [12] بمعاملات 10.2M.

**الإشراف العميق الضمني.** أحد التفسيرات لتحسين دقة الشبكات التلافيفية الكثيفة قد يكون أن الطبقات الفردية تتلقى إشرافاً إضافياً من دالة الخسارة من خلال الاتصالات الأقصر. يمكن للمرء أن يفسر شبكات DenseNets على أنها تؤدي نوعاً من "الإشراف العميق". تم إظهار فوائد الإشراف العميق سابقاً في الشبكات المشرفة بعمق (DSN؛ [20])، التي تحتوي على مصنفات مرفقة بكل طبقة مخفية، مما يفرض على الطبقات الوسيطة تعلم ميزات تمييزية.

تؤدي شبكات DenseNets إشرافاً عميقاً مماثلاً بطريقة ضمنية: يوفر مصنف واحد في أعلى الشبكة إشرافاً مباشراً لجميع الطبقات من خلال طبقتين أو ثلاث طبقات انتقالية على الأكثر. ومع ذلك، فإن دالة الخسارة والتدرج لشبكات DenseNets أقل تعقيداً بكثير، حيث يتم مشاركة نفس دالة الخسارة بين جميع الطبقات.

**الاتصال العشوائي مقابل الحتمي.** هناك صلة مثيرة للاهتمام بين الشبكات التلافيفية الكثيفة وتنظيم العمق العشوائي للشبكات المتبقية [13]. في العمق العشوائي، يتم إسقاط الطبقات في الشبكات المتبقية عشوائياً، مما يخلق اتصالات مباشرة بين الطبقات المحيطة. نظراً لأن طبقات التجميع لا تُسقط أبداً، تؤدي الشبكة إلى نمط اتصال مماثل لـ DenseNet: هناك احتمال صغير لأي طبقتين، بين نفس طبقات التجميع، أن تكونا متصلتين مباشرة—إذا تم إسقاط جميع الطبقات الوسيطة عشوائياً. على الرغم من أن الطرق مختلفة تماماً في النهاية، فإن تفسير DenseNet للعمق العشوائي قد يوفر رؤى حول نجاح هذا المنظم.

**إعادة استخدام الميزات.** بالتصميم، تسمح شبكات DenseNets للطبقات بالوصول إلى خرائط الميزات من جميع طبقاتها السابقة (وإن كان أحياناً من خلال الطبقات الانتقالية). نجري تجربة للتحقيق فيما إذا كانت الشبكة المدربة تستفيد من هذه الفرصة. نقوم أولاً بتدريب DenseNet على C10+ مع L = 40 وk = 12. لكل طبقة التفافية ℓ داخل كتلة، نحسب متوسط الوزن (المطلق) المخصص للاتصالات مع الطبقة s. يُظهر الشكل 5 خريطة حرارية لجميع الكتل الكثيفة الثلاث. يعمل متوسط الوزن المطلق كبديل لاعتماد الطبقة التلافيفية على طبقاتها السابقة. تشير النقطة الحمراء في الموضع (ℓ، s) إلى أن الطبقة ℓ تستخدم، في المتوسط، بشكل قوي خرائط الميزات المنتجة من s طبقات قبلها. يمكن إجراء عدة ملاحظات من الرسم البياني:

1. تنشر جميع الطبقات أوزانها على العديد من المدخلات داخل نفس الكتلة. هذا يشير إلى أن الميزات المستخرجة بواسطة الطبقات المبكرة جداً تُستخدم، في الواقع، مباشرة بواسطة الطبقات العميقة في جميع أنحاء نفس الكتلة الكثيفة.

2. تنشر أوزان الطبقات الانتقالية أيضاً وزنها عبر جميع الطبقات داخل الكتلة الكثيفة السابقة، مما يشير إلى تدفق المعلومات من الطبقات الأولى إلى الأخيرة من DenseNet من خلال عمليات إعادة توجيه قليلة.

3. تخصص الطبقات داخل الكتلة الكثيفة الثانية والثالثة باستمرار أقل وزن لمخرجات الطبقة الانتقالية (الصف العلوي من المثلثات)، مما يشير إلى أن الطبقة الانتقالية تخرج العديد من الميزات الزائدة (بوزن منخفض في المتوسط). هذا يتماشى مع النتائج القوية لـ DenseNet-BC حيث يتم ضغط هذه المخرجات بالضبط.

4. على الرغم من أن طبقة التصنيف النهائية، الموضحة في أقصى اليمين، تستخدم أيضاً أوزاناً عبر الكتلة الكثيفة بأكملها، يبدو أن هناك تركيزاً نحو خرائط الميزات النهائية، مما يشير إلى أنه قد يكون هناك بعض الميزات عالية المستوى أكثر المنتجة في وقت متأخر في الشبكة.

---

### Translation Notes

- **Figures referenced:** Figure 4 (parameter efficiency plots), Figure 5 (feature reuse heat-map)
- **Key terms introduced:** Model compactness, implicit deep supervision, stochastic vs. deterministic connection, heat-map analysis
- **Equations:** References to Equations (1) and (2)
- **Citations:** [16], [29], [12], [20], [13]
- **Special handling:** Heat-map analysis preserved with numbered observations, mathematical notation maintained

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-translation Check

Key insight: "يشجع هذا على إعادة استخدام الميزات في جميع أنحاء الشبكة، ويؤدي إلى نماذج أكثر إدماجاً" → "This encourages feature reuse throughout the network, and leads to more compact models" - accurately preserves the causal relationship and technical meaning.
