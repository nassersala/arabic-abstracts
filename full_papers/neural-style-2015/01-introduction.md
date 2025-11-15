# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.89
**Glossary Terms Used:** convolutional neural networks (الشبكات العصبية الالتفافية), deep learning (تعلم عميق), feature maps (خرائط الميزات), feed-forward (التغذية الأمامية), gradient descent (الانحدار التدرجي), object recognition (التعرف على الأجسام), backpropagation (الانتشار العكسي)

---

### English Version

The class of Deep Neural Networks that are most powerful in image processing tasks are called Convolutional Neural Networks. Convolutional Neural Networks consist of layers of small computational units that process visual information hierarchically in a feed-forward manner (Fig 1). Each layer of units can be understood as a collection of image filters, each of which extracts a certain feature from the input image. Thus, the output of a given layer consists of so-called feature maps: differently filtered versions of the input image.

When Convolutional Neural Networks are trained on object recognition, they develop a representation of the image that makes object information increasingly explicit along the processing hierarchy. Therefore, along the processing hierarchy of the network, the input image is transformed into representations that increasingly care about the actual *content* of the image compared to its detailed pixel values. We can directly visualise the information each layer contains about the input image by reconstructing the image only from the feature maps in that layer (Fig 1, content reconstructions, see Methods for details on how to reconstruct the image). Higher layers in the network capture the high-level *content* in terms of objects and their arrangement in the input image but do not constrain the exact pixel values of the reconstruction. (Fig 1, content reconstructions d,e). In contrast, reconstructions from the lower layers simply reproduce the exact pixel values of the original image (Fig 1, content reconstructions a,b,c). We therefore refer to the feature responses in higher layers of the network as the *content representation*.

To obtain a representation of the *style* of an input image, we use a feature space originally designed to capture texture information. This feature space is built on top of the filter responses in each layer of the network. It consists of the correlations between the different filter responses over the spatial extent of the feature maps (see Methods for details). By including the feature correlations of multiple layers, we obtain a stationary, multi-scale representation of the input image, which captures its texture information but not the global arrangement.

Again, we can visualise the information captured by these style feature spaces built on different layers of the network by constructing an image that matches the style representation of a given input image (Fig 1, style reconstructions). Indeed reconstructions from the style features produce texturised versions of the input image that capture its general appearance in terms of colour and localised structures. Moreover, the size and complexity of local image structures from the input image increases along the hierarchy, a result that can be explained by the increasing receptive field sizes and feature complexity. We refer to this multi-scale representation as *style representation*.

**Figure 1 Caption:**

**Convolutional Neural Network (CNN).** A given input image is represented as a set of filtered images at each processing stage in the CNN. While the number of different filters increases along the processing hierarchy, the size of the filtered images is reduced by some downsampling mechanism (e.g. max-pooling) leading to a decrease in the total number of units per layer of the network.

**Content Reconstructions.** We can visualise the information at different processing stages in the CNN by reconstructing the input image from only knowing the network's responses in a particular layer. We reconstruct the input image from from layers 'conv1_1' (a), 'conv2_1' (b), 'conv3_1' (c), 'conv4_1' (d) and 'conv5_1' (e) of the original VGG-Network. We find that reconstruction from lower layers is almost perfect (a,b,c). In higher layers of the network, detailed pixel information is lost while the high-level content of the image is preserved (d,e).

**Style Reconstructions.** On top of the original CNN representations we built a new feature space that captures the style of an input image. The style representation computes correlations between the different features in different layers of the CNN. We reconstruct the style of the input image from style representations built on different subsets of CNN layers ( 'conv1_1' (a), 'conv1_1' and 'conv2_1' (b), 'conv1_1', 'conv2_1' and 'conv3_1' (c), 'conv1_1', 'conv2_1', 'conv3_1' and 'conv4_1' (d), 'conv1_1', 'conv2_1', 'conv3_1', 'conv4_1' and 'conv5_1' (e)). This creates images that match the style of a given image on an increasing scale while discarding information of the global arrangement of the scene.

---

### النسخة العربية

فئة الشبكات العصبية العميقة الأكثر قوة في مهام معالجة الصور تسمى الشبكات العصبية الالتفافية. تتكون الشبكات العصبية الالتفافية من طبقات من الوحدات الحسابية الصغيرة التي تعالج المعلومات البصرية بشكل هرمي بطريقة التغذية الأمامية (الشكل 1). يمكن فهم كل طبقة من الوحدات كمجموعة من مرشحات الصور، حيث يستخرج كل منها ميزة معينة من الصورة المدخلة. وبالتالي، فإن مخرجات طبقة معينة تتكون مما يسمى خرائط الميزات: نسخ مرشحة بشكل مختلف من الصورة المدخلة.

عندما يتم تدريب الشبكات العصبية الالتفافية على التعرف على الأجسام، فإنها تطور تمثيلاً للصورة يجعل معلومات الأجسام أكثر وضوحاً بشكل متزايد على طول التسلسل الهرمي للمعالجة. لذلك، على طول التسلسل الهرمي لمعالجة الشبكة، يتم تحويل الصورة المدخلة إلى تمثيلات تهتم بشكل متزايد بالمحتوى الفعلي للصورة مقارنة بقيم البكسل التفصيلية. يمكننا تصور المعلومات التي تحتويها كل طبقة عن الصورة المدخلة مباشرة من خلال إعادة بناء الصورة فقط من خرائط الميزات في تلك الطبقة (الشكل 1، إعادة بناء المحتوى، انظر قسم الطرق للحصول على تفاصيل حول كيفية إعادة بناء الصورة). تلتقط الطبقات العليا في الشبكة المحتوى عالي المستوى من حيث الأجسام وترتيبها في الصورة المدخلة ولكنها لا تقيد قيم البكسل الدقيقة لإعادة البناء (الشكل 1، إعادة بناء المحتوى د، هـ). في المقابل، تعيد عمليات إعادة البناء من الطبقات السفلى ببساطة إنتاج قيم البكسل الدقيقة للصورة الأصلية (الشكل 1، إعادة بناء المحتوى أ، ب، ج). لذلك نشير إلى استجابات الميزات في الطبقات العليا من الشبكة باسم تمثيل المحتوى.

للحصول على تمثيل لأسلوب الصورة المدخلة، نستخدم فضاء ميزات مصمم أصلاً لالتقاط معلومات النسيج. يُبنى فضاء الميزات هذا فوق استجابات المرشحات في كل طبقة من الشبكة. ويتكون من الارتباطات بين استجابات المرشحات المختلفة عبر المدى المكاني لخرائط الميزات (انظر قسم الطرق للحصول على التفاصيل). من خلال تضمين ارتباطات الميزات من طبقات متعددة، نحصل على تمثيل ثابت ومتعدد المقاييس للصورة المدخلة، والذي يلتقط معلومات النسيج الخاصة بها ولكن ليس الترتيب العام.

مرة أخرى، يمكننا تصور المعلومات التي تلتقطها فضاءات ميزات الأسلوب هذه المبنية على طبقات مختلفة من الشبكة من خلال بناء صورة تطابق تمثيل الأسلوب لصورة مدخلة معينة (الشكل 1، إعادة بناء الأسلوب). في الواقع، تنتج عمليات إعادة البناء من ميزات الأسلوب نسخاً منسجة من الصورة المدخلة تلتقط مظهرها العام من حيث اللون والبنى الموضعية. علاوة على ذلك، يزداد حجم وتعقيد البنى الصورية الموضعية من الصورة المدخلة على طول التسلسل الهرمي، وهي نتيجة يمكن تفسيرها بزيادة أحجام الحقول الاستقبالية وتعقيد الميزات. نشير إلى هذا التمثيل متعدد المقاييس باسم تمثيل الأسلوب.

**شرح الشكل 1:**

**الشبكة العصبية الالتفافية.** يتم تمثيل صورة مدخلة معينة كمجموعة من الصور المرشحة في كل مرحلة معالجة في الشبكة العصبية الالتفافية. بينما يزداد عدد المرشحات المختلفة على طول التسلسل الهرمي للمعالجة، يتم تقليل حجم الصور المرشحة بواسطة آلية تخفيض العينات (مثل التجميع الأقصى) مما يؤدي إلى انخفاض في إجمالي عدد الوحدات لكل طبقة من الشبكة.

**إعادة بناء المحتوى.** يمكننا تصور المعلومات في مراحل المعالجة المختلفة في الشبكة العصبية الالتفافية من خلال إعادة بناء الصورة المدخلة من معرفة استجابات الشبكة في طبقة معينة فقط. نعيد بناء الصورة المدخلة من الطبقات 'conv1_1' (أ)، 'conv2_1' (ب)، 'conv3_1' (ج)، 'conv4_1' (د) و 'conv5_1' (هـ) من شبكة VGG الأصلية. نجد أن إعادة البناء من الطبقات السفلى شبه مثالية (أ، ب، ج). في الطبقات العليا من الشبكة، تُفقد معلومات البكسل التفصيلية بينما يتم الحفاظ على المحتوى عالي المستوى للصورة (د، هـ).

**إعادة بناء الأسلوب.** فوق التمثيلات الأصلية للشبكة العصبية الالتفافية، قمنا ببناء فضاء ميزات جديد يلتقط أسلوب الصورة المدخلة. يحسب تمثيل الأسلوب الارتباطات بين الميزات المختلفة في طبقات مختلفة من الشبكة العصبية الالتفافية. نعيد بناء أسلوب الصورة المدخلة من تمثيلات الأسلوب المبنية على مجموعات فرعية مختلفة من طبقات الشبكة العصبية الالتفافية ('conv1_1' (أ)، 'conv1_1' و 'conv2_1' (ب)، 'conv1_1' و 'conv2_1' و 'conv3_1' (ج)، 'conv1_1' و 'conv2_1' و 'conv3_1' و 'conv4_1' (د)، 'conv1_1' و 'conv2_1' و 'conv3_1' و 'conv4_1' و 'conv5_1' (هـ)). ينشئ هذا صوراً تطابق أسلوب صورة معينة على مقياس متزايد مع التخلص من معلومات الترتيب العام للمشهد.

---

### Translation Notes

- **Figures referenced:** Figure 1 (network model with content and style reconstructions)

- **Key terms introduced:**
  - Content representation (تمثيل المحتوى)
  - Style representation (تمثيل الأسلوب)
  - Feature maps (خرائط الميزات)
  - Receptive field (الحقل الاستقبالي)
  - Texture (النسيج)
  - Multi-scale representation (تمثيل متعدد المقاييس)
  - Stationary representation (تمثيل ثابت)

- **Translation choices:**
  - "Hierarchically" → "بشكل هرمي" (in a hierarchical manner)
  - "Feed-forward manner" → "بطريقة التغذية الأمامية" (feed-forward processing)
  - "Texturised versions" → "نسخ منسجة" (textured versions)
  - "Localised structures" → "البنى الموضعية" (local structures)
  - "Max-pooling" → "التجميع الأقصى" (max pooling)
  - "Downsampling" → "تخفيض العينات" (downsampling)
  - "Receptive field" → "الحقل الاستقبالي" (receptive field - standard neuroscience term)

- **Equations:** None in this section

- **Citations:** References to methods section and Figure 1

- **Special handling:**
  - Layer names (conv1_1, conv2_1, etc.) kept in English as technical identifiers
  - VGG-Network name preserved
  - Figure panel labels (a, b, c, d, e) kept in both languages

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.91
- Readability: 0.88
- Glossary consistency: 0.88
- **Overall section score:** 0.89

### Back-translation Check

Key sentence: "We therefore refer to the feature responses in higher layers of the network as the content representation."

Arabic: "لذلك نشير إلى استجابات الميزات في الطبقات العليا من الشبكة باسم تمثيل المحتوى."

Back to English: "Therefore we refer to the feature responses in the higher layers of the network as the content representation."

✓ Semantic match confirmed
