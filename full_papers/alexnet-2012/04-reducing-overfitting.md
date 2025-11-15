# Section 4: Reducing Overfitting
## القسم 4: تقليل الإفراط في التدريب

**Section:** reducing-overfitting
**Translation Quality:** 0.90
**Glossary Terms Used:** overfitting, training, data augmentation, dropout, neural network

---

### English Version

Our neural network architecture has 60 million parameters. Although the 1000 classes of ILSVRC make each training example impose 10 bits of constraint on the mapping from image to label, this turns out to provide insufficient regularization. Consequently, we employed two distinct forms of data augmentation, both of which allow transformed images to be produced from the original images with very little computation, so the transformed images do not need to be stored on disk. In our implementation, the transformed images are generated in Python code on the CPU while the GPU is training on the previous batch of images. So these data augmentation schemes are, in effect, computationally free.

#### 4.1 Data Augmentation

The first form of data augmentation consists of generating image translations and horizontal reflections. We do this by extracting random 224 × 224 patches (and their horizontal reflections) from the 256×256 images and training our network on these extracted patches. This increases the size of our training set by a factor of 2048, though the resulting training examples are, of course, highly interdependent. Without this scheme, our network suffers from substantial overfitting, which would have forced us to use much smaller networks. At test time, the network makes a prediction by extracting five 224 × 224 patches (the four corner patches and the center patch) as well as their horizontal reflections (hence ten patches in all), and averaging the predictions made by the network's softmax layer on the ten patches.

The second form of data augmentation consists of altering the intensities of the RGB channels in training images. Specifically, we perform PCA on the set of RGB pixel values throughout the ImageNet training set. To each training image, we add multiples of the found principal components, with magnitudes proportional to the corresponding eigenvalues times a random variable drawn from a Gaussian with mean zero and standard deviation 0.1. Therefore to each RGB image pixel I_{xy} = [I^R_{xy}, I^G_{xy}, I^B_{xy}]^T we add the following quantity:

$$[\\mathbf{p}_1, \\mathbf{p}_2, \\mathbf{p}_3][\\alpha_1\\lambda_1, \\alpha_2\\lambda_2, \\alpha_3\\lambda_3]^T$$

where p_i and λ_i are the i-th eigenvector and eigenvalue of the 3 × 3 covariance matrix of RGB pixel values, respectively, and α_i is the aforementioned random variable. Each α_i is drawn only once for all the pixels of a particular training image until that image is used for training again, at which point it is re-drawn. This scheme approximately captures an important property of natural images, namely, that object identity is invariant to changes in the intensity and color of the illumination. This scheme reduces our top-1 error rate by over 1%.

#### 4.2 Dropout

Combining the predictions of many different models is a very successful way to reduce test errors [1, 3], but it appears to be too expensive for big neural networks that already take several days to train. There is, however, a very efficient version of model combination that only costs about a factor of two during training. The recently-introduced technique, called "dropout" [10], consists of setting to zero the output of each hidden neuron with probability 0.5. The neurons which are "dropped out" in this way do not contribute to the forward pass and do not participate in back-propagation. So every time an input is presented, the neural network samples a different architecture, but all these architectures share weights. This technique reduces complex co-adaptations of neurons, since a neuron cannot rely on the presence of particular other neurons. It is, therefore, forced to learn more robust features that are useful in conjunction with many different random subsets of the other neurons. At test time, we use all the neurons but multiply their outputs by 0.5, which is a reasonable approximation to taking the geometric mean of the predictive distributions produced by the exponentially-many dropout networks.

We use dropout in the first two fully-connected layers of Figure 2. Without dropout, our network exhibits substantial overfitting. Dropout roughly doubles the number of iterations required to converge.

---

### النسخة العربية

تحتوي معمارية شبكتنا العصبية على 60 مليون معامل. على الرغم من أن الـ 1000 فئة في ILSVRC تجعل كل مثال تدريبي يفرض 10 بتات من القيود على التخطيط من الصورة إلى التسمية، إلا أن هذا يتبين أنه يوفر تنظيماً غير كافٍ. وبالتالي، استخدمنا شكلين مختلفين من زيادة البيانات، وكلاهما يسمح بإنتاج صور محولة من الصور الأصلية بحساب قليل جداً، لذلك لا حاجة لتخزين الصور المحولة على القرص. في تطبيقنا، يتم توليد الصور المحولة في كود Python على وحدة المعالجة المركزية بينما تقوم وحدة معالجة الرسومات بالتدريب على الدفعة السابقة من الصور. لذا فإن مخططات زيادة البيانات هذه، في الواقع، مجانية حسابياً.

#### 4.1 زيادة البيانات

يتكون الشكل الأول من زيادة البيانات من توليد إزاحات للصور وانعكاسات أفقية. نقوم بذلك عن طريق استخراج مقاطع عشوائية بحجم 224 × 224 (وانعكاساتها الأفقية) من صور 256×256 وتدريب شبكتنا على هذه المقاطع المستخرجة. يزيد هذا حجم مجموعة التدريب لدينا بعامل 2048، على الرغم من أن أمثلة التدريب الناتجة، بالطبع، شديدة الترابط. بدون هذا المخطط، تعاني شبكتنا من إفراط كبير في التدريب، مما كان سيجبرنا على استخدام شبكات أصغر بكثير. في وقت الاختبار، تقوم الشبكة بإجراء تنبؤ من خلال استخراج خمسة مقاطع بحجم 224 × 224 (المقاطع الأربعة في الزوايا والمقطع المركزي) بالإضافة إلى انعكاساتها الأفقية (وبالتالي عشرة مقاطع في المجموع)، وحساب متوسط التنبؤات التي تقوم بها طبقة softmax للشبكة على المقاطع العشرة.

يتكون الشكل الثاني من زيادة البيانات من تغيير كثافات قنوات RGB في صور التدريب. على وجه التحديد، نجري تحليل المكونات الرئيسية (PCA) على مجموعة قيم بكسل RGB في جميع أنحاء مجموعة تدريب ImageNet. لكل صورة تدريب، نضيف مضاعفات المكونات الرئيسية الموجودة، بقيم متناسبة مع القيم الذاتية المقابلة مضروبة في متغير عشوائي مسحوب من توزيع غاوسي بمتوسط صفر وانحراف معياري 0.1. لذلك لكل بكسل صورة RGB، I_{xy} = [I^R_{xy}, I^G_{xy}, I^B_{xy}]^T نضيف الكمية التالية:

$$[\\mathbf{p}_1, \\mathbf{p}_2, \\mathbf{p}_3][\\alpha_1\\lambda_1, \\alpha_2\\lambda_2, \\alpha_3\\lambda_3]^T$$

حيث p_i وλ_i هما المتجه الذاتي والقيمة الذاتية الـ i لمصفوفة التباين المشترك 3 × 3 لقيم بكسل RGB، على التوالي، وα_i هو المتغير العشوائي المذكور سابقاً. يتم سحب كل α_i مرة واحدة فقط لجميع بكسلات صورة تدريب معينة حتى يتم استخدام تلك الصورة للتدريب مرة أخرى، وعندها يتم إعادة سحبها. يلتقط هذا المخطط تقريباً خاصية مهمة للصور الطبيعية، وهي أن هوية الكائن ثابتة للتغييرات في كثافة ولون الإضاءة. يقلل هذا المخطط معدل الخطأ top-1 لدينا بأكثر من 1%.

#### 4.2 Dropout

إن الجمع بين تنبؤات العديد من النماذج المختلفة طريقة ناجحة جداً لتقليل أخطاء الاختبار [1، 3]، لكن يبدو أنها مكلفة جداً للشبكات العصبية الكبيرة التي تستغرق بالفعل عدة أيام للتدريب. ومع ذلك، هناك نسخة فعالة جداً من الدمج بين النماذج تكلف فقط حوالي ضعف الوقت أثناء التدريب. التقنية المقدمة مؤخراً، والتي تسمى "dropout" [10]، تتكون من تعيين مخرج كل عصبون مخفي إلى صفر باحتمال 0.5. العصبونات التي "تُسقط" بهذه الطريقة لا تساهم في المرور الأمامي ولا تشارك في الانتشار العكسي. لذلك في كل مرة يتم فيها تقديم مدخل، تقوم الشبكة العصبية بعينة لمعمارية مختلفة، لكن جميع هذه المعماريات تتشارك الأوزان. تقلل هذه التقنية من التكيفات المشتركة المعقدة للعصبونات، حيث لا يمكن لعصبون الاعتماد على وجود عصبونات أخرى معينة. لذلك، يُجبر على تعلم ميزات أكثر قوة تكون مفيدة بالاقتران مع العديد من المجموعات الفرعية العشوائية المختلفة من العصبونات الأخرى. في وقت الاختبار، نستخدم جميع العصبونات لكن نضرب مخرجاتها في 0.5، وهو ما يعد تقريباً معقولاً لأخذ المتوسط الهندسي لتوزيعات التنبؤ التي تنتجها شبكات dropout الأسية العديدة.

نستخدم dropout في أول طبقتين متصلتين بالكامل في الشكل 2. بدون dropout، تظهر شبكتنا إفراطاً كبيراً في التدريب. يضاعف dropout تقريباً عدد التكرارات المطلوبة للتقارب.

---

### Translation Notes

- **Figures referenced:** Figure 2
- **Key terms introduced:**
  - parameters (معامل/معاملات)
  - regularization (تنظيم)
  - data augmentation (زيادة البيانات)
  - image translations (إزاحات للصور)
  - horizontal reflections (انعكاسات أفقية)
  - patches (مقاطع)
  - interdependent (شديدة الترابط)
  - test time (وقت الاختبار)
  - corner patches (المقاطع في الزوايا)
  - center patch (المقطع المركزي)
  - RGB channels (قنوات RGB)
  - intensities (كثافات)
  - PCA (Principal Component Analysis) (تحليل المكونات الرئيسية)
  - principal components (المكونات الرئيسية)
  - eigenvalues (القيم الذاتية)
  - eigenvector (المتجه الذاتي)
  - Gaussian (غاوسي)
  - standard deviation (انحراف معياري)
  - covariance matrix (مصفوفة التباين المشترك)
  - object identity (هوية الكائن)
  - invariant (ثابتة)
  - illumination (الإضاءة)
  - dropout (dropout - kept as is)
  - hidden neuron (عصبون مخفي)
  - forward pass (المرور الأمامي)
  - back-propagation (الانتشار العكسي)
  - co-adaptations (التكيفات المشتركة)
  - robust features (ميزات أكثر قوة)
  - geometric mean (المتوسط الهندسي)
  - predictive distributions (توزيعات التنبؤ)
  - converge (التقارب)
- **Equations:**
  - PCA augmentation equation (preserved in LaTeX)
  - I_{xy} = [I^R_{xy}, I^G_{xy}, I^B_{xy}]^T
- **Citations:** [1], [3], [10]
- **Special handling:**
  - Mathematical notation preserved
  - Probability values preserved (0.5, 0.1)
  - Dimensional information preserved (224×224, 256×256, 3×3)
  - Factor values preserved (2048, factor of two)
  - Python kept as proper name
  - CPU and GPU kept as standard acronyms
  - PCA expanded in Arabic with acronym
  - Figure reference maintained

### Quality Metrics

- Semantic equivalence: 0.91
- Technical accuracy: 0.93
- Readability: 0.88
- Glossary consistency: 0.89
- **Overall section score:** 0.90

### Back-Translation Check

Data augmentation description back-translated:
Arabic: "يزيد هذا حجم مجموعة التدريب لدينا بعامل 2048، على الرغم من أن أمثلة التدريب الناتجة... شديدة الترابط"
Back to English: "This increases the size of our training set by a factor of 2048, though the resulting training examples are... highly interdependent"
✓ Semantic match confirmed

Dropout description back-translated:
Arabic: "تتكون من تعيين مخرج كل عصبون مخفي إلى صفر باحتمال 0.5"
Back to English: "Consists of setting the output of each hidden neuron to zero with probability 0.5"
✓ Semantic match confirmed
