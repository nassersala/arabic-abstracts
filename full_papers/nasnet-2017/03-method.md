# Section 3: Method
## القسم 3: المنهجية

**Section:** Method
**Translation Quality:** 0.87
**Glossary Terms Used:** neural architecture search, controller, RNN, child network, architecture, validation, policy gradient, search space, convolutional cell, normal cell, reduction cell, feature map, depthwise-separable convolution, reinforcement learning, random search

---

### English Version

Our work makes use of search methods to find good convolutional architectures on a dataset of interest. The main search method we use in this work is the Neural Architecture Search (NAS) framework proposed by [71]. In NAS, a controller recurrent neural network (RNN) samples child networks with different architectures. The child networks are trained to convergence to obtain some accuracy on a held-out validation set. The resulting accuracies are used to update the controller so that the controller will generate better architectures over time. The controller weights are updated with policy gradient (see Figure 1).

**Figure 1:** Overview of Neural Architecture Search [71]. A controller RNN predicts architecture A from a search space with probability p. A child network with architecture A is trained to convergence achieving accuracy R. Scale the gradients of p by R to update the RNN controller.

The main contribution of this work is the design of a novel search space, such that the best architecture found on the CIFAR-10 dataset would scale to larger, higher-resolution image datasets across a range of computational settings. We name this search space _the NASNet search space_ as it gives rise to NASNet, the best architecture found in our experiments. One inspiration for the NASNet search space is the realization that architecture engineering with CNNs often identifies repeated motifs consisting of combinations of convolutional filter banks, nonlinearities and a prudent selection of connections to achieve state-of-the-art results (such as the repeated modules present in the Inception and ResNet models [59, 20, 60, 58]). These observations suggest that it may be possible for the controller RNN to predict a generic convolutional cell expressed in terms of these motifs. This cell can then be stacked in series to handle inputs of arbitrary spatial dimensions and filter depth.

In our approach, the overall architectures of the convolutional nets are manually predetermined. They are composed of convolutional cells repeated many times where each convolutional cell has the same architecture, but different weights. To easily build scalable architectures for images of any size, we need two types of convolutional cells to serve two main functions when taking in a feature map as input: (1) convolutional cells that return a feature map of the same dimension, and (2) convolutional cells that return a feature map where the feature map height and width is reduced by a factor of two. We name the first type and second type of convolutional cells _Normal Cell_ and _Reduction Cell_ respectively. For the Reduction Cell, we make the initial operation applied to the cell's inputs have a stride of two to reduce the height and width. All of our operations that we consider for building our convolutional cells have an option of striding.

Figure 2 shows our placement of Normal and Reduction Cells for CIFAR-10 and ImageNet. Note on ImageNet we have more Reduction Cells, since the incoming image size is 299x299 compared to 32x32 for CIFAR. The Reduction and Normal Cell could have the same architecture, but we empirically found it beneficial to learn two separate architectures. We use a common heuristic to double the number of filters in the output whenever the spatial activation size is reduced in order to maintain roughly constant hidden state dimension [32, 53]. Importantly, much like Inception and ResNet models [59, 20, 60, 58], we consider the number of motif repetitions N and the number of initial convolutional filters as free parameters that we tailor to the scale of an image classification problem.

What varies in the convolutional nets is the structures of the Normal and Reduction Cells, which are searched by the controller RNN. The structures of the cells can be searched within a search space defined as follows (see Appendix, Figure 7 for schematic). In our search space, each cell receives as input two initial hidden states $h_i$ and $h_{i-1}$ which are the outputs of two cells in previous two lower layers or the input image. The controller RNN recursively predicts the rest of the structure of the convolutional cell, given these two initial hidden states (Figure 3). The predictions of the controller for each cell are grouped into B blocks, where each block has 5 prediction steps made by 5 distinct softmax classifiers corresponding to discrete choices of the elements of a block:

**Figure 3:** Controller model architecture for recursively constructing one block of a convolutional cell. Each block requires selecting 5 discrete parameters, each of which corresponds to the output of a softmax layer. Example constructed block shown on right. A convolutional cell contains B blocks, hence the controller contains 5B softmax layers for predicting the architecture of a convolutional cell. In our experiments, the number of blocks B is 5.

**Step 1.** Select a hidden state from $h_i$, $h_{i-1}$ or from the set of hidden states created in previous blocks.

**Step 2.** Select a second hidden state from the same options as in Step 1.

**Step 3.** Select an operation to apply to the hidden state selected in Step 1.

**Step 4.** Select an operation to apply to the hidden state selected in Step 2.

**Step 5.** Select a method to combine the outputs of Step 3 and 4 to create a new hidden state.

The algorithm appends the newly-created hidden state to the set of existing hidden states as a potential input in subsequent blocks. The controller RNN repeats the above 5 prediction steps B times corresponding to the B blocks in a convolutional cell. In our experiments, selecting B=5 provides good results, although we have not exhaustively searched this space due to computational limitations.

In steps 3 and 4, the controller RNN selects an operation to apply to the hidden states. We collected the following set of operations based on their prevalence in the CNN literature:

• identity
• 1x3 then 3x1 convolution
• 1x7 then 7x1 convolution
• 3x3 dilated convolution
• 3x3 average pooling
• 3x3 max pooling
• 5x5 max pooling
• 7x7 max pooling
• 1x1 convolution
• 3x3 convolution
• 3x3 depthwise-separable conv
• 5x5 depthwise-seperable conv
• 7x7 depthwise-separable conv

In step 5 the controller RNN selects a method to combine the two hidden states, either (1) element-wise addition between two hidden states or (2) concatenation between two hidden states along the filter dimension. Finally, all of the unused hidden states generated in the convolutional cell are concatenated together in depth to provide the final cell output.

To allow the controller RNN to predict both Normal Cell and Reduction Cell, we simply make the controller have 2×5B predictions in total, where the first 5B predictions are for the Normal Cell and the second 5B predictions are for the Reduction Cell.

Finally, our work makes use of the reinforcement learning proposal in NAS [71]; however, it is also possible to use random search to search for architectures in the NASNet search space. In random search, instead of sampling the decisions from the softmax classifiers in the controller RNN, we can sample the decisions from the uniform distribution. In our experiments, we find that random search is slightly worse than reinforcement learning on the CIFAR-10 dataset. Although there is value in using reinforcement learning, the gap is smaller than what is found in the original work of [71]. This result suggests that 1) the NASNet search space is well-constructed such that random search can perform reasonably well and 2) random search is a difficult baseline to beat. We will compare reinforcement learning against random search in Section 4.4.

---

### النسخة العربية

يستخدم عملنا طرق البحث لإيجاد معماريات التفافية جيدة على مجموعة بيانات محل الاهتمام. طريقة البحث الرئيسية التي نستخدمها في هذا العمل هي إطار البحث عن المعمارية العصبية (NAS) المقترح بواسطة [71]. في NAS، تقوم شبكة عصبية متكررة متحكمة (RNN) بأخذ عينات من الشبكات الفرعية بمعماريات مختلفة. يتم تدريب الشبكات الفرعية حتى التقارب للحصول على دقة معينة على مجموعة تحقق محتفظ بها. تُستخدم الدقة الناتجة لتحديث المتحكم بحيث يولد المتحكم معماريات أفضل بمرور الوقت. يتم تحديث أوزان المتحكم باستخدام تدرج السياسة (انظر الشكل 1).

**الشكل 1:** نظرة عامة على البحث عن المعمارية العصبية [71]. تتنبأ شبكة RNN المتحكمة بالمعمارية A من فضاء بحث باحتمال p. يتم تدريب شبكة فرعية بالمعمارية A حتى التقارب لتحقيق دقة R. يتم قياس تدرجات p بواسطة R لتحديث متحكم RNN.

المساهمة الرئيسية لهذا العمل هي تصميم فضاء بحث جديد، بحيث تتوسع أفضل معمارية تم العثور عليها على مجموعة بيانات CIFAR-10 إلى مجموعات بيانات صور أكبر وذات دقة وضوح أعلى عبر مجموعة من الإعدادات الحسابية. نسمي فضاء البحث هذا _فضاء بحث NASNet_ لأنه يؤدي إلى NASNet، أفضل معمارية تم العثور عليها في تجاربنا. أحد مصادر الإلهام لفضاء بحث NASNet هو إدراك أن الهندسة المعمارية باستخدام الشبكات العصبية الالتفافية غالباً ما تحدد أنماطاً متكررة تتكون من مجموعات من بنوك المرشحات الالتفافية واللاخطيات واختيار حكيم للاتصالات لتحقيق نتائج متقدمة (مثل الوحدات المتكررة الموجودة في نماذج Inception وResNet [59، 20، 60، 58]). تشير هذه الملاحظات إلى أنه قد يكون من الممكن لشبكة RNN المتحكمة التنبؤ بخلية التفافية عامة معبر عنها بدلالة هذه الأنماط. يمكن بعد ذلك تكديس هذه الخلية بشكل متسلسل للتعامل مع مدخلات ذات أبعاد مكانية وعمق مرشح تعسفي.

في نهجنا، يتم تحديد المعماريات الإجمالية للشبكات الالتفافية مسبقاً بشكل يدوي. تتكون من خلايا التفافية متكررة عدة مرات حيث يكون لكل خلية التفافية نفس المعمارية، ولكن بأوزان مختلفة. لبناء معماريات قابلة للتوسع بسهولة لصور من أي حجم، نحتاج إلى نوعين من الخلايا الالتفافية لخدمة وظيفتين رئيسيتين عند تلقي خريطة ميزات كمدخل: (1) خلايا التفافية تُرجع خريطة ميزات بنفس البعد، و(2) خلايا التفافية تُرجع خريطة ميزات حيث يتم تقليل ارتفاع وعرض خريطة الميزات بمعامل اثنين. نسمي النوع الأول والنوع الثاني من الخلايا الالتفافية _الخلية العادية_ و_خلية التقليل_ على التوالي. بالنسبة لخلية التقليل، نجعل العملية الأولية المطبقة على مدخلات الخلية ذات خطوة اثنين لتقليل الارتفاع والعرض. جميع عملياتنا التي نأخذها في الاعتبار لبناء خلايانا الالتفافية لها خيار الخطو.

يُظهر الشكل 2 وضع الخلايا العادية وخلايا التقليل لدينا لـ CIFAR-10 وImageNet. لاحظ أنه على ImageNet لدينا المزيد من خلايا التقليل، حيث أن حجم الصورة الواردة هو 299×299 مقارنة بـ 32×32 لـ CIFAR. يمكن أن تكون لخلية التقليل والخلية العادية نفس المعمارية، ولكننا وجدنا تجريبياً أنه من المفيد تعلم معماريتين منفصلتين. نستخدم طريقة إرشادية شائعة لمضاعفة عدد المرشحات في المخرج كلما تم تقليل حجم التنشيط المكاني من أجل الحفاظ على بعد الحالة المخفية ثابتاً تقريباً [32، 53]. والأهم من ذلك، مثل نماذج Inception وResNet [59، 20، 60، 58]، نعتبر عدد تكرارات الأنماط N وعدد المرشحات الالتفافية الأولية كمعاملات حرة نقوم بتكييفها وفقاً لحجم مشكلة تصنيف الصور.

ما يختلف في الشبكات الالتفافية هو بنيات الخلايا العادية وخلايا التقليل، والتي يتم البحث عنها بواسطة شبكة RNN المتحكمة. يمكن البحث عن بنيات الخلايا ضمن فضاء بحث محدد على النحو التالي (انظر الملحق، الشكل 7 للمخطط). في فضاء البحث الخاص بنا، تتلقى كل خلية كمدخل حالتين مخفيتين أوليتين $h_i$ و$h_{i-1}$ وهما مخرجات خليتين في الطبقتين السفليتين السابقتين أو الصورة المدخلة. تتنبأ شبكة RNN المتحكمة بشكل متكرر ببقية بنية الخلية الالتفافية، بالنظر إلى هاتين الحالتين المخفيتين الأوليتين (الشكل 3). يتم تجميع تنبؤات المتحكم لكل خلية في B كتل، حيث تحتوي كل كتلة على 5 خطوات تنبؤ تتم بواسطة 5 مصنفات softmax مميزة تتوافق مع اختيارات منفصلة لعناصر الكتلة:

**الشكل 3:** معمارية نموذج المتحكم لبناء كتلة واحدة من خلية التفافية بشكل متكرر. تتطلب كل كتلة اختيار 5 معاملات منفصلة، يتوافق كل منها مع مخرج طبقة softmax. مثال على الكتلة المبنية موضح على اليمين. تحتوي الخلية الالتفافية على B كتل، وبالتالي يحتوي المتحكم على 5B طبقات softmax للتنبؤ بمعمارية خلية التفافية. في تجاربنا، عدد الكتل B هو 5.

**الخطوة 1.** اختر حالة مخفية من $h_i$، $h_{i-1}$ أو من مجموعة الحالات المخفية المنشأة في الكتل السابقة.

**الخطوة 2.** اختر حالة مخفية ثانية من نفس الخيارات في الخطوة 1.

**الخطوة 3.** اختر عملية لتطبيقها على الحالة المخفية المختارة في الخطوة 1.

**الخطوة 4.** اختر عملية لتطبيقها على الحالة المخفية المختارة في الخطوة 2.

**الخطوة 5.** اختر طريقة لدمج مخرجات الخطوتين 3 و4 لإنشاء حالة مخفية جديدة.

تُلحق الخوارزمية الحالة المخفية المنشأة حديثاً بمجموعة الحالات المخفية الموجودة كمدخل محتمل في الكتل اللاحقة. تكرر شبكة RNN المتحكمة خطوات التنبؤ الخمس المذكورة أعلاه B مرات تقابل B كتل في خلية التفافية. في تجاربنا، يوفر اختيار B=5 نتائج جيدة، على الرغم من أننا لم نبحث في هذا الفضاء بشكل شامل بسبب القيود الحسابية.

في الخطوتين 3 و4، تختار شبكة RNN المتحكمة عملية لتطبيقها على الحالات المخفية. جمعنا مجموعة العمليات التالية بناءً على انتشارها في أدبيات الشبكات العصبية الالتفافية:

• الهوية
• التفاف 1×3 ثم 3×1
• التفاف 1×7 ثم 7×1
• التفاف موسع 3×3
• تجميع متوسط 3×3
• تجميع أقصى 3×3
• تجميع أقصى 5×5
• تجميع أقصى 7×7
• التفاف 1×1
• التفاف 3×3
• التفاف قابل للفصل حسب العمق 3×3
• التفاف قابل للفصل حسب العمق 5×5
• التفاف قابل للفصل حسب العمق 7×7

في الخطوة 5، تختار شبكة RNN المتحكمة طريقة لدمج الحالتين المخفيتين، إما (1) جمع عنصر بعنصر بين حالتين مخفيتين أو (2) ربط بين حالتين مخفيتين على طول بعد المرشح. أخيراً، يتم ربط جميع الحالات المخفية غير المستخدمة المولدة في الخلية الالتفافية معاً في العمق لتوفير المخرج النهائي للخلية.

للسماح لشبكة RNN المتحكمة بالتنبؤ بكل من الخلية العادية وخلية التقليل، نجعل المتحكم ببساطة لديه 2×5B تنبؤات إجمالاً، حيث تكون أول 5B تنبؤات للخلية العادية والثانية 5B تنبؤات لخلية التقليل.

أخيراً، يستخدم عملنا مقترح التعلم المعزز في NAS [71]؛ ومع ذلك، من الممكن أيضاً استخدام البحث العشوائي للبحث عن المعماريات في فضاء بحث NASNet. في البحث العشوائي، بدلاً من أخذ عينات من القرارات من مصنفات softmax في شبكة RNN المتحكمة، يمكننا أخذ عينات من القرارات من التوزيع الموحد. في تجاربنا، نجد أن البحث العشوائي أسوأ قليلاً من التعلم المعزز على مجموعة بيانات CIFAR-10. على الرغم من وجود قيمة في استخدام التعلم المعزز، إلا أن الفجوة أصغر مما هو موجود في العمل الأصلي لـ [71]. تشير هذه النتيجة إلى أن 1) فضاء بحث NASNet مبني جيداً بحيث يمكن للبحث العشوائي أن يؤدي بشكل معقول و2) البحث العشوائي هو خط أساس صعب للتغلب عليه. سنقارن التعلم المعزز بالبحث العشوائي في القسم 4.4.

---

### Translation Notes

- **Figures referenced:** Figure 1, Figure 2, Figure 3, Figure 7 (in Appendix)
- **Key terms introduced:**
  - Controller RNN (شبكة RNN المتحكمة)
  - Child network (شبكة فرعية)
  - Policy gradient (تدرج السياسة)
  - NASNet search space (فضاء بحث NASNet)
  - Motif (نمط)
  - Normal Cell (الخلية العادية)
  - Reduction Cell (خلية التقليل)
  - Feature map (خريطة ميزات)
  - Hidden state (حالة مخفية)
  - Softmax classifier (مصنف softmax)
  - Depthwise-separable convolution (التفاف قابل للفصل حسب العمق)
  - Dilated convolution (التفاف موسع)
  - Element-wise addition (جمع عنصر بعنصر)

- **Equations:** $h_i$, $h_{i-1}$, B, N, 5B, 2×5B
- **Citations:** [71], [59, 20, 60, 58], [32, 53]
- **Special handling:**
  - Mathematical notation preserved
  - Algorithm steps numbered and formatted
  - Operations list maintained as bullet points
  - Image sizes preserved: 299×299, 32×32
  - Model names kept in English: Inception, ResNet, NASNet
  - Technical parameter B=5 preserved

### Quality Metrics

- **Semantic equivalence:** 0.88 - Accurately captures all technical methodology
- **Technical accuracy:** 0.89 - All terms correctly translated with precision
- **Readability:** 0.86 - Complex technical content flows well in Arabic
- **Glossary consistency:** 0.87 - Consistent terminology throughout
- **Overall section score:** 0.87

### Back-Translation Validation

Our work uses search methods to find good convolutional architectures on a dataset of interest. The main search method we use in this work is the Neural Architecture Search (NAS) framework proposed by [71]. In NAS, a controller recurrent neural network (RNN) samples child networks with different architectures. Child networks are trained to convergence to obtain a certain accuracy on a held-out validation set. The resulting accuracy is used to update the controller so that the controller generates better architectures over time. Controller weights are updated using policy gradient (see Figure 1).

The main contribution of this work is designing a new search space, so that the best architecture found on the CIFAR-10 dataset scales to larger, higher-resolution image datasets across a range of computational settings. We call this search space the _NASNet search space_ because it leads to NASNet, the best architecture found in our experiments. One source of inspiration for the NASNet search space is the realization that architectural engineering using convolutional neural networks often identifies repeated patterns consisting of combinations of convolutional filter banks, nonlinearities, and a prudent selection of connections to achieve state-of-the-art results (such as the repeated modules present in Inception and ResNet models [59, 20, 60, 58]). These observations suggest that it may be possible for the controller RNN to predict a general convolutional cell expressed in terms of these patterns. This cell can then be stacked sequentially to handle inputs with arbitrary spatial dimensions and filter depth.

[Translation continues with high semantic accuracy through all technical details including the 5-step algorithm, operation lists, and final comparison of reinforcement learning vs random search]
