# Section 3: Pixel Recurrent Neural Networks
## القسم 3: الشبكات العصبية التكرارية للبكسل

**Section:** pixel-recurrent-neural-networks
**Translation Quality:** 0.89
**Glossary Terms Used:** LSTM, bidirectional, residual connections, masked convolution, convolutional neural network, receptive field, multi-scale

---

### English Version

## 3 Pixel Recurrent Neural Networks

### 3.1 Row LSTM

The Row LSTM processes images row-by-row from top to bottom, computing features for entire rows simultaneously using one-dimensional convolution. The layer captures a roughly triangular context above the pixel. The architecture uses masked k×1 convolutions where k≥3. The input-to-state component processes the entire 2D input map, producing a 4h×n×n tensor representing four gate vectors at each position (h = output feature maps). The state-to-state component combines previous hidden and cell states with input contributions via output, forget, and input gates using sigmoid activation, and a content gate using tanh activation. The key limitation is that the Row LSTM has a triangular receptive field unable to capture the complete available context.

### 3.2 Diagonal BiLSTM

This bidirectional layer processes diagonals rather than rows, achieving full dependency coverage. The computation involves a skewing operation where input maps are offset row-by-row, creating n×(2n-1) dimensions. After computing diagonal states with column-wise 2×1 convolutions, outputs are skewed back into an n×n map. Two directional passes scan from opposite corners. The right output is then shifted down by one row and added to the left output to prevent seeing future pixels. Advantages include parallelization potential and use of minimal 2×1 kernels. Larger kernels prove unnecessary given the already global receptive field.

### 3.3 Residual Connections

Networks up to twelve layers deep employ residual connections to improve convergence and signal propagation. The architecture maintains 2h input features, reduces to h features per gate through input-to-state convolutions, then upsamples back to 2h via 1×1 convolution before adding the residual connection. This approach relates to previous approaches using gating along network depth but avoids requiring additional gates. Both residual and layer-to-output skip connections prove effective, with combined use preserving advantages.

### 3.4 Masked Convolution

RGB channels are split into three feature parts. Prediction follows strict ordering: red channel from previous pixels, green from red plus previous pixels, blue from both R and G plus previous context. Two mask types enforce dependencies: Mask A (first layer only) restricts connections to previously-predicted neighbors and colors, while Mask B (subsequent layers) allows color self-connections while maintaining causal structure. Implementation involves zeroing out corresponding weights in input-to-state convolutions after each update.

### 3.5 PixelCNN

This fully convolutional alternative uses multiple convolutional layers that preserve the spatial resolution without pooling. Masked 3×3 convolutions across fifteen layers avoid viewing future context. The key trade-off is that parallelization advantage over PixelRNN is only available during training or evaluating test images. The image generation process is sequential for both kinds of networks.

### 3.6 Multi-Scale PixelRNN

Architecture combines unconditional and conditional components. An unconditional PixelRNN generates an s×s subsampled image, then a conditional PixelRNN takes the upsampled version as additional input for n×n generation. The upsampling network uses deconvolutional layers to construct enlarged feature maps, which are then added to each layer's input-to-state mappings via 1×1 unmasked convolution, biasing the conditional prediction process.

---

### النسخة العربية

## 3 الشبكات العصبية التكرارية للبكسل

### 3.1 صف LSTM

تعالج صف LSTM الصور صفاً تلو صف من الأعلى إلى الأسفل، محسبةً ميزات للصفوف بأكملها في وقت واحد باستخدام الالتفاف أحادي البُعد. تلتقط الطبقة سياقاً مثلثياً تقريباً فوق البكسل. تستخدم المعمارية التفافات مقنعة k×1 حيث k≥3. يعالج مكون الإدخال إلى الحالة خريطة الإدخال ثنائية الأبعاد بالكامل، منتجاً موتر 4h×n×n يمثل أربعة متجهات بوابة في كل موقع (h = خرائط الميزات الناتجة). يجمع مكون الحالة إلى الحالة الحالات المخفية والخلوية السابقة مع مساهمات الإدخال عبر بوابات الإخراج والنسيان والإدخال باستخدام تفعيل sigmoid، وبوابة محتوى باستخدام تفعيل tanh. القيد الرئيسي هو أن صف LSTM له مجال استقبال مثلثي غير قادر على التقاط السياق الكامل المتاح.

### 3.2 القطرية BiLSTM

تعالج هذه الطبقة ثنائية الاتجاه الأقطار بدلاً من الصفوف، محققةً تغطية كاملة للتبعيات. يتضمن الحساب عملية انحراف حيث يتم إزاحة خرائط الإدخال صفاً تلو صف، مما يخلق أبعاد n×(2n-1). بعد حساب الحالات القطرية بالتفافات عمودية 2×1، يتم إعادة انحراف المخرجات إلى خريطة n×n. يمسح ممران اتجاهيان من زوايا متقابلة. يتم بعد ذلك إزاحة المخرج الأيمن لأسفل صفاً واحداً وإضافته إلى المخرج الأيسر لمنع رؤية البكسلات المستقبلية. تشمل المزايا إمكانية التوازي واستخدام نوى 2×1 صغيرة. تثبت النوى الأكبر أنها غير ضرورية نظراً لمجال الاستقبال العالمي بالفعل.

### 3.3 الاتصالات المتبقية

تستخدم الشبكات التي يصل عمقها إلى اثنتي عشرة طبقة اتصالات متبقية لتحسين التقارب وانتشار الإشارة. تحافظ المعمارية على ميزات إدخال 2h، وتقلل إلى ميزات h لكل بوابة من خلال التفافات الإدخال إلى الحالة، ثم تقوم بزيادة العينات مرة أخرى إلى 2h عبر التفاف 1×1 قبل إضافة الاتصال المتبقي. يرتبط هذا النهج بالمناهج السابقة التي تستخدم البوابات على طول عمق الشبكة ولكنه يتجنب الحاجة إلى بوابات إضافية. تثبت كل من الاتصالات المتبقية واتصالات التخطي من الطبقة إلى المخرج فعاليتها، مع الاستخدام المشترك الذي يحفظ المزايا.

### 3.4 الالتفاف المقنع

يتم تقسيم قنوات RGB إلى ثلاثة أجزاء من الميزات. يتبع التنبؤ ترتيباً صارماً: القناة الحمراء من البكسلات السابقة، والخضراء من الحمراء بالإضافة إلى البكسلات السابقة، والزرقاء من كل من R و G بالإضافة إلى السياق السابق. يفرض نوعان من الأقنعة التبعيات: القناع A (الطبقة الأولى فقط) يقيد الاتصالات بالجوار والألوان المتنبأ بها سابقاً، بينما يسمح القناع B (الطبقات اللاحقة) باتصالات الألوان الذاتية مع الحفاظ على البنية السببية. يتضمن التنفيذ تصفير الأوزان المقابلة في التفافات الإدخال إلى الحالة بعد كل تحديث.

### 3.5 PixelCNN

يستخدم هذا البديل الالتفافي بالكامل طبقات التفافية متعددة تحافظ على الدقة المكانية دون تجميع. تتجنب الالتفافات المقنعة 3×3 عبر خمس عشرة طبقة عرض السياق المستقبلي. المقايضة الرئيسية هي أن ميزة التوازي على PixelRNN متاحة فقط أثناء التدريب أو تقييم صور الاختبار. عملية توليد الصورة تسلسلية لكلا النوعين من الشبكات.

### 3.6 متعددة المقاييس PixelRNN

تجمع المعمارية بين المكونات غير الشرطية والشرطية. تولد PixelRNN غير شرطية صورة معاينة s×s، ثم تأخذ PixelRNN شرطية النسخة المكبرة كإدخال إضافي لتوليد n×n. تستخدم شبكة زيادة العينات طبقات إلغاء الالتفاف لبناء خرائط ميزات موسعة، والتي يتم إضافتها بعد ذلك إلى تعيينات الإدخال إلى الحالة لكل طبقة عبر التفاف 1×1 غير مقنع، مما يحيز عملية التنبؤ الشرطي.

---

### Translation Notes

- **Figures referenced:** Figures mentioned conceptually (skewing operation, diagonal processing)
- **Key terms introduced:** Row LSTM, Diagonal BiLSTM, receptive field, masked convolution (Mask A, Mask B), deconvolutional layers
- **Equations:** Implicit mathematical operations described
- **Citations:** None
- **Special handling:** Technical architecture terms like "skewing" translated as "انحراف". Gate types (sigmoid, tanh) kept as transliterations.

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.91
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.89
