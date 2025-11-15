# Section 2: Related Work
## القسم 2: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.87
**Glossary Terms Used:** model compression (ضغط النموذج), architecture (معمارية), convolutional neural networks (الشبكات العصبية الالتفافية), accuracy (دقة), parameters (معاملات), deep learning (تعلم عميق), quantization (تكميم), pruning (تقليم), hash function (دالة التجزئة), low-rank (منخفض الرتبة), knowledge distillation (تقطير المعرفة)

---

### English Version

**Model Compression.** The overarching goal of our work is to identify a model that has very few parameters while preserving accuracy. To address this problem, a sensible approach is to take an existing CNN model and compress it in a lossy fashion. In fact, a research community has emerged around the topic of model compression, and several approaches have been reported. A fairly straightforward approach by Denton et al. is to apply singular value decomposition (SVD) to a pretrained CNN model. Han et al. developed Network Pruning, which begins with a pretrained model, then replaces parameters that are below a certain threshold with zeros to form a sparse matrix, and finally performs a few iterations of training on the sparse CNN. Recently, Han et al. extended their work by combining Network Pruning with quantization (to 8 bits or less) and huffman encoding to create an approach called Deep Compression, and further designed a hardware accelerator called EIE that operates directly on the compressed model, achieving substantial speedups and energy savings.

**CNN Microarchitecture.** Convolution filters can be decomposed as a sequence of smaller filters. Vedalai and Marr were the first to explore this idea. The idea of using 1x1 convolutions appeared in the Network-in-Network (NiN) architecture of Lin et al. We draw inspiration from these works and use 1x1 filters as a major component of the Fire module in SqueezeNet. Szegedy et al. developed the Inception architecture, which uses a sophisticated microarchitecture with multiple different-sized convolutions per layer. SqueezeNet uses a much less complex microarchitecture, which enables microarchitecture design space exploration on limited computational resources.

**CNN Macroarchitecture.** VGGNet and ResNet are each well-known examples of a respective CNN macroarchitecture approach. VGGNet uses the same convolution filter shape (3x3) in most layers, while ResNet uses identity mappings, also called skip connections or shortcuts, to achieve higher accuracy in networks with tens or hundreds of layers. SqueezeNet uses ResNet-like skip connections to improve accuracy while keeping the model small.

**Neural Network Design Space Exploration.** Neural networks (including deep and convolutional NNs) have a large design space, with numerous options for microarchitectures, macroarchitectures, solvers, and other hyperparameters. It seems natural that the community would want to gain intuition about how these factors impact a NN's accuracy. Ciresan et al. varied the number of layers and the number of neurons per layer. Snoek et al. developed a method for hyperparmeter search using Bayesian optimization. Maclaurin et al. developed an approach to take the gradient of (i.e. backpropagate through) the training procedure, which they applied to optimize hyperparameters. This line of work has inspired us to systematically explore the design space of SqueezeNet, as we discuss in Section 5.

**Compact network architectures for embedded systems.** One recent work in this area is MobileNets, developed by Howard et al., which use a form of depthwise separable convolutions similar to those in Inception. MobileNets introduce two hyperparameters that enable a designer to choose a model architecture with the right size and speed for their application. In another approach, Collins and Kohli developed a method to train compact models trained from scratch. Our approach to identifying compact architectures is complementary to both of these approaches.

---

### النسخة العربية

**ضغط النموذج.** الهدف الشامل لعملنا هو تحديد نموذج يحتوي على عدد قليل جداً من المعاملات مع الحفاظ على الدقة. لمعالجة هذه المشكلة، النهج المنطقي هو أخذ نموذج شبكة عصبية التفافية موجود وضغطه بطريقة فاقدة. في الواقع، ظهر مجتمع بحثي حول موضوع ضغط النموذج، وتم الإبلاغ عن عدة نهج. نهج مباشر إلى حد ما من قبل Denton وآخرين هو تطبيق تحليل القيم المفردة (SVD) على نموذج شبكة عصبية التفافية مدرب مسبقاً. طور Han وآخرون تقليم الشبكة، والذي يبدأ بنموذج مدرب مسبقاً، ثم يستبدل المعاملات التي تقل عن حد معين بأصفار لتشكيل مصفوفة متناثرة، وأخيراً يقوم بتنفيذ عدة تكرارات من التدريب على الشبكة العصبية الالتفافية المتناثرة. مؤخراً، وسع Han وآخرون عملهم من خلال الجمع بين تقليم الشبكة والتكميم (إلى 8 بتات أو أقل) وترميز هافمان لإنشاء نهج يسمى الضغط العميق، كما صمموا مسرّعاً للأجهزة يسمى EIE يعمل مباشرة على النموذج المضغوط، محققاً تسريعات كبيرة ووفورات في الطاقة.

**المعمارية الدقيقة للشبكات العصبية الالتفافية.** يمكن تحليل مرشحات الالتفاف كتسلسل من المرشحات الأصغر. كان Vedalai وMarr أول من استكشف هذه الفكرة. ظهرت فكرة استخدام التفافات 1x1 في معمارية الشبكة داخل الشبكة (NiN) لـ Lin وآخرين. نستمد الإلهام من هذه الأعمال ونستخدم مرشحات 1x1 كمكون رئيسي من وحدة Fire في SqueezeNet. طور Szegedy وآخرون معمارية Inception، والتي تستخدم معمارية دقيقة متطورة مع تفافات متعددة بأحجام مختلفة لكل طبقة. تستخدم SqueezeNet معمارية دقيقة أقل تعقيداً بكثير، مما يتيح استكشاف فضاء تصميم المعمارية الدقيقة على موارد حسابية محدودة.

**المعمارية الكلية للشبكات العصبية الالتفافية.** تعد VGGNet وResNet مثالين معروفين جيداً لنهج المعمارية الكلية للشبكات العصبية الالتفافية. تستخدم VGGNet نفس شكل مرشح الالتفاف (3x3) في معظم الطبقات، بينما تستخدم ResNet تخطيطات الهوية، والتي تسمى أيضاً اتصالات القفز أو الاختصارات، لتحقيق دقة أعلى في الشبكات ذات عشرات أو مئات الطبقات. تستخدم SqueezeNet اتصالات قفز مشابهة لـ ResNet لتحسين الدقة مع الحفاظ على صغر حجم النموذج.

**استكشاف فضاء تصميم الشبكات العصبية.** تمتلك الشبكات العصبية (بما في ذلك الشبكات العصبية العميقة والالتفافية) فضاء تصميم كبير، مع خيارات عديدة للمعماريات الدقيقة والمعماريات الكلية والحلالات والمعاملات الفائقة الأخرى. يبدو من الطبيعي أن يرغب المجتمع في اكتساب حدس حول كيفية تأثير هذه العوامل على دقة الشبكة العصبية. غيّر Ciresan وآخرون عدد الطبقات وعدد العصبونات لكل طبقة. طور Snoek وآخرون طريقة للبحث عن المعاملات الفائقة باستخدام التحسين البايزي. طور Maclaurin وآخرون نهجاً لأخذ التدرج من (أي الانتشار العكسي عبر) إجراء التدريب، والذي طبقوه لتحسين المعاملات الفائقة. ألهمنا هذا الخط من العمل لاستكشاف فضاء تصميم SqueezeNet بشكل منهجي، كما نناقش في القسم 5.

**معماريات الشبكات المدمجة للأنظمة المدمجة.** أحد الأعمال الحديثة في هذا المجال هو MobileNets، الذي طوره Howard وآخرون، والذي يستخدم شكلاً من التفافات قابلة للفصل حسب العمق مشابهة لتلك الموجودة في Inception. تقدم MobileNets معاملين فائقين يمكّنان المصمم من اختيار معمارية نموذج بالحجم والسرعة المناسبين لتطبيقهم. في نهج آخر، طور Collins وKohli طريقة لتدريب النماذج المدمجة المدربة من الصفر. نهجنا لتحديد المعماريات المدمجة مكمل لكلا هذين النهجين.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Singular Value Decomposition (SVD) (تحليل القيم المفردة)
  - Network Pruning (تقليم الشبكة)
  - Sparse matrix (مصفوفة متناثرة)
  - Deep Compression (الضغط العميق)
  - Huffman encoding (ترميز هافمان)
  - Network-in-Network (NiN) (الشبكة داخل الشبكة)
  - Inception architecture (معمارية Inception)
  - Identity mappings (تخطيطات الهوية)
  - Skip connections/shortcuts (اتصالات القفز/الاختصارات)
  - Hyperparameters (المعاملات الفائقة)
  - Bayesian optimization (التحسين البايزي)
  - Depthwise separable convolutions (التفافات قابلة للفصل حسب العمق)
- **Equations:** 0
- **Citations:** Multiple research papers referenced (Denton et al., Han et al., Lin et al., Szegedy et al., Ciresan et al., Snoek et al., Maclaurin et al., Howard et al., Collins and Kohli)
- **Special handling:**
  - Kept architecture names (VGGNet, ResNet, Inception, MobileNets, EIE) as proper nouns
  - Translated technical terms consistently with glossary
  - Maintained formal academic tone for citations

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.87

### Back-Translation Check

The Arabic translation accurately conveys:
- Five main categories of related work (model compression, CNN microarchitecture, CNN macroarchitecture, neural network design space exploration, compact network architectures)
- Key contributions from each cited work
- The relationship between prior work and SqueezeNet's approach
- Technical methods (SVD, pruning, quantization, Huffman encoding)
