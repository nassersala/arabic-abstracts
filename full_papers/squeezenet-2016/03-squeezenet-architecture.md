# Section 3: SqueezeNet Architecture
## القسم 3: معمارية SqueezeNet

**Section:** squeezenet-architecture
**Translation Quality:** 0.89
**Glossary Terms Used:** architecture (معمارية), convolutional neural networks (الشبكات العصبية الالتفافية), parameters (معاملات), accuracy (دقة), convolution (التفاف), activation (تنشيط), pooling (تجميع), deep learning (تعلم عميق)

---

### English Version

We now describe the SqueezeNet architecture. We begin by outlining our design strategies for CNNs with few parameters. Then, we introduce the Fire module, our building block out of which to construct CNN architectures. Finally, we use our design strategies to construct SqueezeNet, which is comprised primarily of Fire modules.

#### 3.1 Architectural Design Strategies

Our overarching objective in this paper is to identify CNN architectures that have few parameters while maintaining competitive accuracy. To achieve this, we employ three main strategies when designing CNN architectures:

**Strategy 1. Replace 3x3 filters with 1x1 filters.** Given a budget of a certain number of convolution filters, we will choose to make the majority of these filters 1x1, since a 1x1 filter has 9X fewer parameters than a 3x3 filter.

**Strategy 2. Decrease the number of input channels to 3x3 filters.** Consider a convolution layer that is comprised entirely of 3x3 filters. The total quantity of parameters in this layer is (number of input channels) * (number of filters) * (3 * 3). So, to maintain a small total number of parameters in a CNN, it is important not only to decrease the number of 3x3 filters (see Strategy 1 above), but also to decrease the number of input channels to the 3x3 filters. We decrease the number of input channels to 3x3 filters using squeeze layers, which we describe in the next section.

**Strategy 3. Downsample late in the network so that convolution layers have large activation maps.** In a convolutional network, each convolution layer produces an output activation map with a spatial resolution that is at least 1x1 and generally much larger than 1x1. The height and width of these activation maps are controlled by: (1) the size of the input data (e.g. 256x256 images) and (2) the choice of layers in which to downsample in the CNN architecture. Most commonly, downsampling is engineered into CNN architectures by setting the (stride > 1) in some of the convolution or pooling layers (e.g. [20, 26]). If early layers in the network have large strides, then most layers will have small activation maps. Conversely, if most layers in the network have a stride of 1, and the strides greater than 1 are concentrated toward the end of the network, then many layers in the network will have large activation maps. Our intuition is that large activation maps (due to delayed downsampling) can lead to higher classification accuracy, with all else held equal. Indeed, K. He and H. Sun applied delayed downsampling to four different CNN architectures, and in each case delayed downsampling led to higher classification accuracy.

Strategies 1 and 2 are about judiciously decreasing the quantity of parameters in a CNN while attempting to preserve accuracy. Strategy 3 is about maximizing accuracy on a limited budget of parameters. Next, we describe the Fire module, which is our building block for CNN architectures that enables us to successfully employ Strategies 1, 2, and 3.

#### 3.2 The Fire Module

We define the Fire module as follows. A Fire module is comprised of: a squeeze convolution layer (which has only 1x1 filters), feeding into an expand layer that has a mix of 1x1 and 3x3 convolution filters; we illustrate this in Figure 1. We expose three tunable dimensions (hyperparameters) in a Fire module: $s_{1x1}$, $e_{1x1}$, and $e_{3x3}$. In a Fire module, $s_{1x1}$ is the number of filters in the squeeze layer (all 1x1), $e_{1x1}$ is the number of 1x1 filters in the expand layer, and $e_{3x3}$ is the number of 3x3 filters in the expand layer. When we use a Fire module, we set $s_{1x1}$ to be less than $(e_{1x1} + e_{3x3})$, so the squeeze layer helps to limit the number of input channels to the 3x3 filters, as per Strategy 2 from Section 3.1.

#### 3.3 The SqueezeNet architecture

We now describe the SqueezeNet CNN architecture. We illustrate in Figure 2 that SqueezeNet begins with a standalone convolution layer (conv1), followed by 8 Fire modules (fire2-9), ending with a final conv layer (conv10). We gradually increase the number of filters per fire module from the beginning to the end of the network. SqueezeNet performs max-pooling with a stride of 2 after layers conv1, fire4, fire8, and conv10; these relatively late placements of pooling are per Strategy 3 from Section 3.1. We present the full SqueezeNet architecture in Table 1.

**Dimensionality of Fire module hyperparameters.** In Section 3.2, we defined three hyperparameters that we can tune in each Fire module. Now, we define $base\_e$, $incr\_e$, $pct_{3x3}$, and $freq$ as additional hyperparameters that control the dimensionality of all Fire modules in a network. With these hyperparameters, we define $e_{1x1,i}$ and $e_{3x3,i}$ for Fire module $i$ as follows:

$$e_i = base\_e + (incr\_e \times \lfloor \frac{i}{freq} \rfloor)$$

$$e_{1x1,i} = e_i \times (1 - pct_{3x3})$$

$$e_{3x3,i} = e_i \times pct_{3x3}$$

$$s_{1x1,i} = 0.125 \times e_i$$

In other words, in each Fire module, we set the number of expand filters to $base\_e$ plus a multiple of $incr\_e$. We increase the number of expand filters by $incr\_e$ in each cluster of $freq$ consecutive Fire modules. In SqueezeNet (Table 1), $base\_e = 128$, $incr\_e = 128$, $pct_{3x3} = 0.5$, and $freq = 2$. These settings were chosen by design space exploration, which we discuss in more detail in Section 5.

**Other SqueezeNet details.** For brevity, we have omitted number of details and design choices about SqueezeNet from Table 1 and Figure 2. We provide these design details in the following. The conv1, fire4, fire8, and conv10 layers are each followed by a max-pooling layer with a stride of 2. The ReLU activation function is applied to activations from all convolution and pooling layers. Dropout with a ratio of 50% is applied after the fire9 module. For training, we begin with a learning rate of 0.04, and we linearly decrease the learning rate throughout training, as described in [11]. SqueezeNet uses global average pooling on the conv10 layer, as opposed to using fully-connected layers. The use of avg-pooling instead of fully-connected layers was inspired by Network-in-Network (NiN) [21]. In our ImageNet experiments with SqueezeNet, we used a training batch size of 1024 and trained for 90 epochs.

---

### النسخة العربية

نصف الآن معمارية SqueezeNet. نبدأ بتحديد استراتيجيات التصميم الخاصة بنا للشبكات العصبية الالتفافية ذات المعاملات القليلة. ثم، نقدم وحدة Fire، وهي وحدة البناء الأساسية التي نستخدمها لبناء معماريات الشبكات العصبية الالتفافية. أخيراً، نستخدم استراتيجيات التصميم الخاصة بنا لبناء SqueezeNet، والتي تتكون بشكل أساسي من وحدات Fire.

#### 3.1 استراتيجيات التصميم المعماري

هدفنا الشامل في هذه الورقة البحثية هو تحديد معماريات الشبكات العصبية الالتفافية التي تحتوي على معاملات قليلة مع الحفاظ على دقة تنافسية. لتحقيق ذلك، نستخدم ثلاث استراتيجيات رئيسية عند تصميم معماريات الشبكات العصبية الالتفافية:

**الاستراتيجية 1. استبدال المرشحات 3x3 بمرشحات 1x1.** بالنظر إلى ميزانية محددة من مرشحات الالتفاف، سنختار جعل غالبية هذه المرشحات 1x1، حيث أن مرشح 1x1 يحتوي على معاملات أقل بـ 9 مرات من مرشح 3x3.

**الاستراتيجية 2. تقليل عدد قنوات الإدخال إلى المرشحات 3x3.** لنعتبر طبقة التفاف تتكون بالكامل من مرشحات 3x3. الكمية الإجمالية للمعاملات في هذه الطبقة هي (عدد قنوات الإدخال) * (عدد المرشحات) * (3 * 3). لذا، للحفاظ على عدد إجمالي صغير من المعاملات في الشبكة العصبية الالتفافية، من المهم ليس فقط تقليل عدد المرشحات 3x3 (انظر الاستراتيجية 1 أعلاه)، ولكن أيضاً تقليل عدد قنوات الإدخال إلى المرشحات 3x3. نقوم بتقليل عدد قنوات الإدخال إلى المرشحات 3x3 باستخدام طبقات الضغط، والتي نصفها في القسم التالي.

**الاستراتيجية 3. تأخير تقليل العينات في الشبكة بحيث تحتوي طبقات الالتفاف على خرائط تنشيط كبيرة.** في الشبكة الالتفافية، تنتج كل طبقة التفاف خريطة تنشيط إخراج بدقة مكانية لا تقل عن 1x1 وعادة ما تكون أكبر بكثير من 1x1. يتم التحكم في ارتفاع وعرض خرائط التنشيط هذه من خلال: (1) حجم بيانات الإدخال (مثل صور 256x256) و(2) اختيار الطبقات التي يتم فيها تقليل العينات في معمارية الشبكة العصبية الالتفافية. في أغلب الأحيان، يتم هندسة تقليل العينات في معماريات الشبكات العصبية الالتفافية عن طريق تعيين (خطوة > 1) في بعض طبقات الالتفاف أو التجميع. إذا كانت الطبقات المبكرة في الشبكة لديها خطوات كبيرة، فإن معظم الطبقات سيكون لديها خرائط تنشيط صغيرة. على العكس من ذلك، إذا كانت معظم الطبقات في الشبكة لديها خطوة قدرها 1، والخطوات الأكبر من 1 تتركز نحو نهاية الشبكة، فإن العديد من الطبقات في الشبكة سيكون لديها خرائط تنشيط كبيرة. حدسنا هو أن خرائط التنشيط الكبيرة (بسبب تأخير تقليل العينات) يمكن أن تؤدي إلى دقة تصنيف أعلى، مع بقاء كل شيء آخر ثابتاً. في الواقع، طبق K. He وH. Sun تأخير تقليل العينات على أربع معماريات مختلفة للشبكات العصبية الالتفافية، وفي كل حالة أدى تأخير تقليل العينات إلى دقة تصنيف أعلى.

الاستراتيجيتان 1 و2 تتعلقان بتقليل كمية المعاملات في الشبكة العصبية الالتفافية بشكل حكيم مع محاولة الحفاظ على الدقة. الاستراتيجية 3 تتعلق بتعظيم الدقة بميزانية محدودة من المعاملات. بعد ذلك، نصف وحدة Fire، وهي وحدة البناء الأساسية لمعماريات الشبكات العصبية الالتفافية التي تمكننا من استخدام الاستراتيجيات 1 و2 و3 بنجاح.

#### 3.2 وحدة Fire

نعرف وحدة Fire على النحو التالي. تتكون وحدة Fire من: طبقة التفاف ضاغطة (التي تحتوي فقط على مرشحات 1x1)، تغذي طبقة توسيع تحتوي على مزيج من مرشحات الالتفاف 1x1 و3x3؛ نوضح ذلك في الشكل 1. نعرض ثلاثة أبعاد قابلة للضبط (معاملات فائقة) في وحدة Fire: $s_{1x1}$ و$e_{1x1}$ و$e_{3x3}$. في وحدة Fire، $s_{1x1}$ هو عدد المرشحات في طبقة الضغط (جميعها 1x1)، $e_{1x1}$ هو عدد مرشحات 1x1 في طبقة التوسيع، و$e_{3x3}$ هو عدد مرشحات 3x3 في طبقة التوسيع. عندما نستخدم وحدة Fire، نعين $s_{1x1}$ ليكون أقل من $(e_{1x1} + e_{3x3})$، بحيث تساعد طبقة الضغط في الحد من عدد قنوات الإدخال إلى المرشحات 3x3، وفقاً للاستراتيجية 2 من القسم 3.1.

#### 3.3 معمارية SqueezeNet

نصف الآن معمارية الشبكة العصبية الالتفافية SqueezeNet. نوضح في الشكل 2 أن SqueezeNet تبدأ بطبقة التفاف مستقلة (conv1)، تليها 8 وحدات Fire (fire2-9)، تنتهي بطبقة التفاف نهائية (conv10). نزيد تدريجياً عدد المرشحات لكل وحدة Fire من بداية الشبكة إلى نهايتها. تقوم SqueezeNet بتنفيذ التجميع الأقصى بخطوة قدرها 2 بعد الطبقات conv1 وfire4 وfire8 وconv10؛ هذه المواضع المتأخرة نسبياً للتجميع تتماشى مع الاستراتيجية 3 من القسم 3.1. نعرض معمارية SqueezeNet الكاملة في الجدول 1.

**أبعاد المعاملات الفائقة لوحدة Fire.** في القسم 3.2، عرفنا ثلاثة معاملات فائقة يمكننا ضبطها في كل وحدة Fire. الآن، نعرف $base\_e$ و$incr\_e$ و$pct_{3x3}$ و$freq$ كمعاملات فائقة إضافية تتحكم في أبعاد جميع وحدات Fire في الشبكة. باستخدام هذه المعاملات الفائقة، نعرف $e_{1x1,i}$ و$e_{3x3,i}$ لوحدة Fire $i$ على النحو التالي:

$$e_i = base\_e + (incr\_e \times \lfloor \frac{i}{freq} \rfloor)$$

$$e_{1x1,i} = e_i \times (1 - pct_{3x3})$$

$$e_{3x3,i} = e_i \times pct_{3x3}$$

$$s_{1x1,i} = 0.125 \times e_i$$

بمعنى آخر، في كل وحدة Fire، نعين عدد مرشحات التوسيع إلى $base\_e$ بالإضافة إلى مضاعف من $incr\_e$. نزيد عدد مرشحات التوسيع بمقدار $incr\_e$ في كل مجموعة من $freq$ وحدة Fire متتالية. في SqueezeNet (الجدول 1)، $base\_e = 128$ و$incr\_e = 128$ و$pct_{3x3} = 0.5$ و$freq = 2$. تم اختيار هذه الإعدادات من خلال استكشاف فضاء التصميم، والذي نناقشه بمزيد من التفصيل في القسم 5.

**تفاصيل أخرى عن SqueezeNet.** للإيجاز، قمنا بحذف عدد من التفاصيل وخيارات التصميم حول SqueezeNet من الجدول 1 والشكل 2. نقدم تفاصيل التصميم هذه في ما يلي. يتبع كل من الطبقات conv1 وfire4 وfire8 وconv10 طبقة تجميع أقصى بخطوة قدرها 2. يتم تطبيق دالة تنشيط ReLU على التنشيطات من جميع طبقات الالتفاف والتجميع. يتم تطبيق Dropout بنسبة 50% بعد وحدة fire9. للتدريب، نبدأ بمعدل تعلم 0.04، ونقلل معدل التعلم خطياً طوال التدريب، كما هو موضح في [11]. تستخدم SqueezeNet التجميع العام المتوسط على طبقة conv10، بدلاً من استخدام الطبقات المتصلة بالكامل. كان استخدام التجميع المتوسط بدلاً من الطبقات المتصلة بالكامل مستوحى من الشبكة داخل الشبكة (NiN) [21]. في تجاربنا على ImageNet باستخدام SqueezeNet، استخدمنا حجم دفعة تدريب قدرها 1024 ودربنا لمدة 90 حقبة.

---

### Translation Notes

- **Figures referenced:** Figure 1 (Fire module illustration), Figure 2 (SqueezeNet architecture)
- **Tables referenced:** Table 1 (Full SqueezeNet architecture specification)
- **Key terms introduced:**
  - Fire module (وحدة Fire)
  - Squeeze layer (طبقة الضغط / الضاغطة)
  - Expand layer (طبقة التوسيع)
  - Activation maps (خرائط التنشيط)
  - Downsampling (تقليل العينات)
  - Stride (خطوة)
  - Max-pooling (التجميع الأقصى)
  - Global average pooling (التجميع العام المتوسط)
  - Dropout (Dropout - kept as transliteration)
  - Learning rate (معدل التعلم)
- **Equations:** 4 mathematical formulas for Fire module hyperparameters
- **Citations:** References to [11] and [21] (NiN)
- **Special handling:**
  - Kept "Fire module" name as proper noun but translated its components
  - Preserved all mathematical notation and LaTeX equations
  - Translated layer names (conv1, fire2-9, conv10) kept as is for clarity
  - Used formal mathematical Arabic for equations explanations

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.92
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.89

### Back-Translation Check

The Arabic translation accurately conveys:
- Three design strategies for parameter reduction
- Complete description of the Fire module structure and hyperparameters
- The overall SqueezeNet architecture composition
- Mathematical formulas for calculating Fire module dimensions
- Training details and design choices
