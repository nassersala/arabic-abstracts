# Section 3: Approach
## القسم 3: المنهجية

**Section:** approach
**Translation Quality:** 0.88
**Glossary Terms Used:** group convolution, channel shuffle, pointwise convolution, depthwise convolution, feature map channels, computational complexity, bottleneck, residual learning, ShuffleNet unit, network architecture

---

### English Version

## 3. Approach

### 3.1 Channel Shuffle for Group Convolutions

Modern convolutional neural networks [28, 33, 29, 8] usually consist of repeated building blocks with the same structure. Among them, state-of-the-art networks such as Xception [3] and ResNeXt [40] have shown that group convolution is a powerful primitive in neural network design. However, we notice that both designs do not fully take the 1×1 convolutions (also called pointwise convolutions in [12]) into account, which require considerable complexity. For example, in ResNeXt [40] only 3×3 layers are equipped with group convolutions. As a result, for each residual unit in ResNeXt the pointwise convolutions occupy 93.4% of multiplication-adds (cardinality = 32 as suggested in [40]). In tiny networks, expensive pointwise convolutions result in limited number of channels to meet the complexity constraint, which might significantly damage the accuracy.

To address the issue, a straightforward solution is to apply channel sparse connections, for example by applying group convolutions also on 1×1 layers. By ensuring that each convolution operates only on the corresponding input channel group, group convolution significantly reduces computation cost. However, if multiple group convolutions stack together, there is one side effect: outputs from a certain channel are only derived from a small fraction of input channels. Fig 1 (a) illustrates a situation of two stacked group convolution layers. It is clear that outputs from a certain group only relate to the inputs within the group. This property blocks information flow between channel groups and weakens representation.

If we allow group convolution to obtain input data from different groups (as shown in Fig 1 (b)), the input and output channels will be fully related. Specifically, for the feature map generated from the previous group layer, we can first divide the channels in each group into several subgroups, then feed each group in the next layer with different subgroups. This can be efficiently and elegantly implemented by a channel shuffle operation (Fig 1 (c)): suppose a convolutional layer with g groups whose output has g × n channels; we first reshape the output channel dimension into (g, n), transposing and then flattening it back as the input of next layer. Note that the operation still takes effect even if the two convolutions have different numbers of groups. Moreover, channel shuffle is also differentiable, which means it can be embedded into network structures for end-to-end training.

### 3.2 ShuffleNet Unit

Taking advantage of the channel shuffle operation, we propose a novel ShuffleNet unit specially designed for small networks. We start from the design principle of bottleneck unit [8] in Fig 2 (a). It is a residual block. In its residual branch, for the 3×3 layer, we apply a computational economical 3×3 depthwise convolution [3] on the bottleneck feature map. Then, we replace the first 1×1 layer with pointwise group convolution followed by a channel shuffle operation, to form a ShuffleNet unit, as shown in Fig 2 (b). The purpose of the second pointwise group convolution is to recover the channel dimension to match the shortcut path. For simplicity, we do not apply an extra channel shuffle operation after the second pointwise layer as it results in comparable scores. The usage of batch normalization (BN) [14] and nonlinearity is similar to [40, 8], except that we do not use ReLU after depthwise convolution as suggested by [3]. As for the case where ShuffleNet is applied with stride, we simply make two modifications (see Fig 2 (c)): (i) add a 3×3 average pooling on the shortcut path; (ii) replace the element-wise addition with channel concatenation, which makes it easy to enlarge channel dimension with little extra computation cost.

Thanks to pointwise group convolution with channel shuffle, all components in ShuffleNet unit can be computed efficiently. Compared with ResNeXt [40], our structure has lower computation complexity under the same settings. For example, given the input size c×h×w and the bottleneck channels m, ResNeXt unit requires hw(2cm + 9m²/g) FLOPs while ShuffleNet unit requires only hw(2cm/g + 9m).

### 3.3 Network Architecture

Built on ShuffleNet units, we present the overall ShuffleNet architecture in Table 1. The proposed network is mainly composed of a stack of ShuffleNet units grouped into three stages. The first building block in each stage is applied with stride = 2. Other hyper-parameters within a stage stay the same, and for the next stage the output channels are doubled. We set the number of bottleneck channels to 1/4 of the output channels for each ShuffleNet unit. Our intent is to provide a reference design as simple as possible, although we find that further hyper-parameter tunning might generate better results.

In ShuffleNet units, group number g controls the connection sparsity of pointwise convolutions. Table 1 explores different group numbers and we adapt the output channels to ensure overall computation cost roughly unchanged (~140 MFLOPs). Obviously, larger group numbers result in more output channels (thus more convolutional filters) for a given complexity constraint, which helps to encode more information, although it might also lead to degradation for an individual convolutional filter due to limited corresponding input channels. In Sec 4.1.1 we will study the impact of this number subject to different computational constrains.

To customize the network to a desired complexity, we can simply apply a scale factor s on the number of channels. For example, we denote the networks in Table 1 as "ShuffleNet 1×", then "ShuffleNet s×" means scaling the number of filters in ShuffleNet 1× by s times thus overall complexity will be roughly s² times of ShuffleNet 1×.

Note: Following [12] we do not apply group convolution on the first pointwise layer in each ShuffleNet unit, because the number of input channels is relatively small in those layers.

---

### النسخة العربية

## 3. المنهجية

### 3.1 خلط القنوات للالتفافات المجموعية

عادةً ما تتكون الشبكات العصبية الالتفافية الحديثة [28, 33, 29, 8] من كتل بناء متكررة بنفس الهيكل. من بينها، أظهرت الشبكات الحديثة مثل Xception [3] و ResNeXt [40] أن الالتفاف المجموعي هو عنصر أساسي قوي في تصميم الشبكات العصبية. ومع ذلك، نلاحظ أن كلا التصميمين لا يأخذان في الاعتبار بشكل كامل الالتفافات 1×1 (تسمى أيضاً الالتفافات النقطية في [12])، والتي تتطلب تعقيداً كبيراً. على سبيل المثال، في ResNeXt [40] فقط الطبقات 3×3 مجهزة بالالتفافات المجموعية. ونتيجة لذلك، بالنسبة لكل وحدة متبقية (residual unit) في ResNeXt تشغل الالتفافات النقطية 93.4% من عمليات الضرب والجمع (العددية = 32 كما هو مقترح في [40]). في الشبكات الصغيرة، تؤدي الالتفافات النقطية المكلفة إلى عدد محدود من القنوات لتلبية قيد التعقيد، مما قد يضر بشكل كبير بالدقة.

لمعالجة هذه المشكلة، الحل المباشر هو تطبيق الاتصالات المتفرقة للقنوات، على سبيل المثال من خلال تطبيق الالتفافات المجموعية أيضاً على طبقات 1×1. من خلال ضمان أن كل التفاف يعمل فقط على مجموعة قنوات الإدخال المقابلة، يقلل الالتفاف المجموعي بشكل كبير من التكلفة الحسابية. ومع ذلك، إذا تراكمت الالتفافات المجموعية المتعددة معاً، يوجد تأثير جانبي واحد: المخرجات من قناة معينة مشتقة فقط من جزء صغير من قنوات الإدخال. يوضح الشكل 1 (a) حالة طبقتي التفاف مجموعي متراكمتين. من الواضح أن المخرجات من مجموعة معينة تتعلق فقط بالمدخلات داخل المجموعة. هذه الخاصية تمنع تدفق المعلومات بين مجموعات القنوات وتضعف التمثيل.

إذا سمحنا للالتفاف المجموعي بالحصول على بيانات الإدخال من مجموعات مختلفة (كما هو موضح في الشكل 1 (b))، فستكون قنوات الإدخال والإخراج مرتبطة بالكامل. على وجه التحديد، بالنسبة لخريطة الميزات الناتجة عن طبقة المجموعة السابقة، يمكننا أولاً تقسيم القنوات في كل مجموعة إلى عدة مجموعات فرعية، ثم تغذية كل مجموعة في الطبقة التالية بمجموعات فرعية مختلفة. يمكن تنفيذ هذا بكفاءة وأناقة من خلال عملية خلط القنوات (الشكل 1 (c)): لنفترض طبقة التفافية بها g مجموعات يحتوي مخرجها على g × n قناة؛ نقوم أولاً بإعادة تشكيل بُعد قناة الإخراج إلى (g, n)، ثم تبديله (transposing) ثم تسطيحه مرة أخرى كمدخل للطبقة التالية. لاحظ أن العملية لا تزال سارية حتى لو كان للالتفافين أعداد مختلفة من المجموعات. علاوة على ذلك، خلط القنوات قابل للتفاضل أيضاً، مما يعني أنه يمكن تضمينه في هياكل الشبكة للتدريب من البداية إلى النهاية.

### 3.2 وحدة ShuffleNet

من خلال الاستفادة من عملية خلط القنوات، نقترح وحدة ShuffleNet جديدة مصممة خصيصاً للشبكات الصغيرة. نبدأ من مبدأ تصميم وحدة عنق الزجاجة [8] في الشكل 2 (a). إنها كتلة متبقية (residual block). في فرعها المتبقي، بالنسبة لطبقة 3×3، نطبق التفافاً عميقاً 3×3 اقتصادياً حسابياً [3] على خريطة ميزات عنق الزجاجة. ثم، نستبدل الطبقة الأولى 1×1 بالالتفاف النقطي المجموعي يليها عملية خلط القنوات، لتشكيل وحدة ShuffleNet، كما هو موضح في الشكل 2 (b). الغرض من الالتفاف النقطي المجموعي الثاني هو استعادة بُعد القناة لمطابقة مسار الاختصار (shortcut path). من أجل البساطة، لا نطبق عملية خلط قنوات إضافية بعد الطبقة النقطية الثانية حيث أنها تؤدي إلى نتائج مماثلة. استخدام التطبيع الدفعي (BN) [14] واللاخطية مشابه لـ [40, 8]، باستثناء أننا لا نستخدم ReLU بعد الالتفاف العميق كما اقترح [3]. أما بالنسبة للحالة التي يتم فيها تطبيق ShuffleNet مع خطوة (stride)، فنحن ببساطة نجري تعديلين (انظر الشكل 2 (c)): (i) إضافة تجميع متوسط 3×3 على مسار الاختصار؛ (ii) استبدال الجمع العنصري بتسلسل القنوات (channel concatenation)، مما يسهل توسيع بُعد القناة بتكلفة حسابية إضافية قليلة.

بفضل الالتفاف النقطي المجموعي مع خلط القنوات، يمكن حساب جميع المكونات في وحدة ShuffleNet بكفاءة. بالمقارنة مع ResNeXt [40]، يتمتع هيكلنا بتعقيد حسابي أقل تحت نفس الإعدادات. على سبيل المثال، بالنظر إلى حجم الإدخال c×h×w وقنوات عنق الزجاجة m، تتطلب وحدة ResNeXt hw(2cm + 9m²/g) عمليات FLOPs بينما تتطلب وحدة ShuffleNet hw(2cm/g + 9m) فقط.

### 3.3 معمارية الشبكة

بناءً على وحدات ShuffleNet، نقدم معمارية ShuffleNet الشاملة في الجدول 1. تتكون الشبكة المقترحة بشكل رئيسي من مكدس من وحدات ShuffleNet مجمعة في ثلاث مراحل. يتم تطبيق كتلة البناء الأولى في كل مرحلة مع خطوة = 2. تظل المعاملات الفائقة الأخرى ضمن المرحلة كما هي، وبالنسبة للمرحلة التالية تتضاعف قنوات الإخراج. نضع عدد قنوات عنق الزجاجة على 1/4 من قنوات الإخراج لكل وحدة ShuffleNet. هدفنا هو توفير تصميم مرجعي بسيط قدر الإمكان، على الرغم من أننا نجد أن مزيداً من ضبط المعاملات الفائقة قد يولد نتائج أفضل.

في وحدات ShuffleNet، يتحكم رقم المجموعة g في تفرق الاتصال للالتفافات النقطية. يستكشف الجدول 1 أرقام مجموعات مختلفة ونقوم بتكييف قنوات الإخراج لضمان أن تكلفة الحساب الإجمالية تظل دون تغيير تقريباً (~140 ميجا عملية فاصلة عائمة). من الواضح أن أعداد المجموعات الأكبر تؤدي إلى مزيد من قنوات الإخراج (وبالتالي مزيد من مرشحات الالتفاف) لقيد تعقيد معين، مما يساعد على ترميز المزيد من المعلومات، على الرغم من أنه قد يؤدي أيضاً إلى تدهور لمرشح التفاف فردي بسبب قنوات الإدخال المقابلة المحدودة. في القسم 4.1.1 سندرس تأثير هذا الرقم وفقاً لقيود حسابية مختلفة.

لتخصيص الشبكة لتعقيد مطلوب، يمكننا ببساطة تطبيق عامل مقياس s على عدد القنوات. على سبيل المثال، نشير إلى الشبكات في الجدول 1 باسم "ShuffleNet 1×"، ثم "ShuffleNet s×" يعني ضرب عدد المرشحات في ShuffleNet 1× بـ s مرة وبالتالي سيكون التعقيد الإجمالي تقريباً s² مرة من ShuffleNet 1×.

ملاحظة: اتباعاً لـ [12] لا نطبق الالتفاف المجموعي على الطبقة النقطية الأولى في كل وحدة ShuffleNet، لأن عدد قنوات الإدخال صغير نسبياً في تلك الطبقات.

---

### Translation Notes

- **Figures referenced:** Figure 1 (a), (b), (c) - Channel shuffle operation; Figure 2 (a), (b), (c) - ShuffleNet units; Table 1 - Network architecture
- **Key terms introduced:**
  - Pointwise convolutions (الالتفافات النقطية)
  - Channel sparse connections (الاتصالات المتفرقة للقنوات)
  - Channel shuffle (خلط القنوات)
  - Bottleneck unit (وحدة عنق الزجاجة)
  - Residual block (كتلة متبقية)
  - Depthwise convolution (التفاف عميق)
  - Shortcut path (مسار الاختصار)
  - Batch normalization (التطبيع الدفعي)
  - Average pooling (تجميع متوسط)
  - Channel concatenation (تسلسل القنوات)
  - Connection sparsity (تفرق الاتصال)
  - Scale factor (عامل المقياس)

- **Equations:** 2 computational complexity formulas (FLOPs calculations)
- **Citations:** [28, 33, 29, 8, 3, 40, 12, 14]
- **Special handling:**
  - Preserved mathematical notation (c×h×w, g×n, hw(2cm/g + 9m), etc.)
  - Translated technical concepts with precision
  - Kept architecture names in English (Xception, ResNeXt, ShuffleNet)
  - Maintained figure and table references

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.92
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.88

### Back-translation Check (Key Paragraph)

Arabic (from 3.1): "إذا سمحنا للالتفاف المجموعي بالحصول على بيانات الإدخال من مجموعات مختلفة، فستكون قنوات الإدخال والإخراج مرتبطة بالكامل"
Back to English: "If we allow group convolution to obtain input data from different groups, the input and output channels will be fully related"
✓ Semantically equivalent to original
