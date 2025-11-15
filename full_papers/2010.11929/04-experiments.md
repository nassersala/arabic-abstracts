# Section 4: Experiments
## القسم 4: التجارب

**Section:** experiments
**Translation Quality:** 0.86
**Glossary Terms Used:** pre-training, fine-tuning, dataset, benchmark, image classification, transformer, convolutional neural network, transfer learning, self-supervised learning, accuracy, optimization, scaling

---

### English Version

#### 4.1 Setup

**Datasets.** We use ILSVRC-2012 ImageNet dataset with 1k classes and 1.3M images for training. We also use the larger ImageNet-21k dataset with 21k classes and 14M images, and the JFT dataset with 18k classes and approximately 303M high-resolution images. We transfer the models trained on these datasets to several benchmark tasks: ImageNet on the original validation labels and the cleaned-up ReaL labels, CIFAR-10/100, Oxford-IIIT Pets, and Oxford Flowers-102. For these datasets, we use the splits defined in Appendix B. We also evaluate on the VTAB classification suite with 19 tasks divided into three groups: Natural (tasks like Pets, CIFAR), Specialized (medical and satellite imagery), and Structured (tasks requiring geometric understanding like localization).

**Model Variants.** We base ViT configurations on those used for BERT and use the following notation: "ViT-L/16" means the "Large" variant with 16×16 input patch size. The baseline ViT configurations are: ViT-Base (ViT-B): 12 layers, 768 hidden dimension, 12 attention heads, 86M parameters; ViT-Large (ViT-L): 24 layers, 1024 hidden dimension, 16 heads, 307M parameters; ViT-Huge (ViT-H): 32 layers, 1280 hidden dimension, 16 heads, 632M parameters. We compare against state-of-the-art CNN baselines, in particular ResNet-based Big Transfer (BiT) and EfficientNet-based Noisy Student. We use ResNets with Group Normalization (GN) and standardized convolutions to improve transfer performance.

**Training & Fine-tuning.** We train all models using Adam optimizer with β₁ = 0.9, β₂ = 0.999, a batch size of 4096 and apply a high weight decay of 0.1, which we found to be useful for transfer of all models. We use a linear learning rate warmup and decay. For fine-tuning we use SGD with momentum, batch size 512, for all models. For ImageNet results we fine-tune at higher resolution: 512 for ViT-L/16 and 518 for ViT-H/14, and also use Polyak averaging with a factor of 0.9999.

**Metrics.** We report results through fine-tuning accuracy and few-shot accuracy. For few-shot, we solve a regularized least-squares regression problem that maps frozen representations of images to target vectors containing one hot labels for the corresponding image. This formulation allows us to solve in closed form and compute few-shot accuracies very quickly.

#### 4.2 Comparison to State of the Art

We compare Vision Transformer against state-of-the-art models on popular image classification benchmarks. We first compare to the Big Transfer (BiT) models which use large ResNets trained on ImageNet-21k and JFT-300M. The second baseline is Noisy Student, which is trained on JFT-300M using semi-supervised learning with extra unlabeled ImageNet data.

Table 2 shows the results. The best ViT model, ViT-H/14, pre-trained on JFT-300M, outperforms all prior work on all tested datasets while requiring substantially less computational resources to pre-train. Specifically, ViT-H/14 achieves 88.55% top-1 accuracy on ImageNet, 90.72% on ImageNet ReaL, 94.55% on CIFAR-100, and 77.63% average on the 19-task VTAB suite.

Comparing to BiT, the ViT-L/16 model pre-trained on JFT-300M outperforms BiT-L (which is a ResNet152x4) on all tasks, while taking substantially fewer resources to train. The smaller ViT-L/16 model pre-trained on ImageNet-21k performs well on most datasets too. It requires only 8 TPU cores and takes approximately 30 days to train.

Figure 5 performs a comparison in the performance-compute space. Vision Transformers dominate ResNets on the performance/compute trade-off. ViT uses approximately 2-4x less compute to attain the same performance.

#### 4.3 Pre-training Data Requirements

The Vision Transformer performs well when pre-trained on large datasets. But how critical is the dataset size? We train ViT models on datasets of increasing size: ImageNet, ImageNet-21k, and JFT-300M, and evaluate transfer performance.

Figure 3 shows the results. When pre-trained on the smallest dataset (ImageNet), models with lower computational cost perform better. Specifically, ViT-B/32 outperforms ViT-B/16, and ViT-L models underperform ViT-B models. This result is somewhat expected: Vision Transformers do not have the inductive biases built into CNNs (translation equivariance and locality), so they need more data to learn these patterns.

However, when moving to the larger datasets ImageNet-21k and JFT-300M, the trends reverse. ViT-L models outperform ViT-B models, and smaller patch sizes lead to better performance. This suggests that with sufficient pre-training data, Vision Transformers can learn the relevant patterns and surpass models with stronger inductive biases.

We also compare the performance of ViT and ResNet at various dataset sizes. On smaller datasets, ResNets outperform Vision Transformers. Vision Transformers overfit more than ResNets with comparable computational cost on smaller datasets. However, for larger datasets (ImageNet-21k and above), ViT overtakes ResNets.

#### 4.4 Scaling Study

We perform a controlled study of transfer performance as we scale the model and dataset. Figure 4 shows this analysis. We train multiple ViT models with different computational budgets and compare to ResNets and hybrid models. All models are trained for approximately 7 epochs, ensuring that compute is dominated by training and not evaluation.

Vision Transformers dominate ResNets on the performance/compute trade-off. Hybrid models, which use a ResNet feature extractor followed by a Transformer, show a small improvement over pure ViT at smaller computational budgets, but the gap closes as we scale up. This suggests that the convolutional inductive bias is helpful when computational resources are limited, but becomes less important with scale.

#### 4.5 Inspecting Vision Transformer

To understand how Vision Transformer processes images, we analyze the learned representations. First, we visualize the learned position embeddings (Figure 6). Position embeddings learn to encode spatial position: closer patches have more similar position embeddings, and the similarity structure shows a clear 2D spatial pattern.

We also analyze the attention patterns across layers (Figure 7). Some attention heads attend to most of the image already in the lowest layers, showing that the ability to integrate information globally is used by the model. In deeper layers, attention becomes increasingly focused and specialized. We compute the mean attention distance (in image space) for each attention head at each layer. This "attention distance" is analogous to receptive field size in CNNs. We find that some heads attend to distant regions even in the lowest layers, while attention distance increases through the network for other heads, similar to how receptive fields grow in CNNs.

#### 4.6 Self-supervision

Transformers show impressive performance on NLP tasks when pre-trained using self-supervised learning. Motivated by this success, we explore masked patch prediction for self-supervised pre-training of ViT, analogous to masked language modeling in BERT.

We train a ViT-B/16 model with masked patch prediction on ImageNet. We corrupt 50% of patch tokens by replacing them with a learned [MASK] embedding (80% of the time), a random patch (10% of the time), or leaving them unchanged (10% of the time). We then predict the 3-bit, mean color (i.e., one of 512 colors) of the masked patches.

Table 4 shows that self-supervised pre-training on ImageNet yields 79.9% accuracy on ImageNet classification after fine-tuning, which is 2% better than training from scratch, but still 4% behind supervised pre-training on ImageNet. We conclude that self-supervised pre-training for ViT is promising but leaves a gap compared to large-scale supervised pre-training. Exploring other self-supervised pre-training methods, such as contrastive methods, is an interesting future direction.

---

### النسخة العربية

#### 4.1 الإعداد

**مجموعات البيانات.** نستخدم مجموعة بيانات ImageNet من ILSVRC-2012 التي تحتوي على 1000 فئة و1.3 مليون صورة للتدريب. نستخدم أيضاً مجموعة بيانات ImageNet-21k الأكبر التي تحتوي على 21 ألف فئة و14 مليون صورة، ومجموعة بيانات JFT التي تحتوي على 18 ألف فئة وحوالي 303 مليون صورة عالية الدقة. ننقل النماذج المدربة على هذه المجموعات إلى عدة مهام معيارية: ImageNet على تسميات التحقق الأصلية والتسميات النظيفة ReaL، وCIFAR-10/100، وOxford-IIIT Pets، وOxford Flowers-102. لهذه المجموعات، نستخدم التقسيمات المحددة في الملحق B. نقيّم أيضاً على مجموعة تصنيف VTAB التي تحتوي على 19 مهمة مقسمة إلى ثلاث مجموعات: طبيعية (مهام مثل Pets وCIFAR)، ومتخصصة (صور طبية وصور الأقمار الصناعية)، ومنظمة (مهام تتطلب فهماً هندسياً مثل التحديد الموضعي).

**متغيرات النموذج.** نبني تكوينات ViT على تلك المستخدمة لـ BERT ونستخدم الترميز التالي: "ViT-L/16" يعني المتغير "الكبير" بحجم رقعة مدخل 16×16. تكوينات ViT الأساسية هي: ViT-Base (ViT-B): 12 طبقة، 768 بُعد مخفي، 12 رأس انتباه، 86 مليون معامل؛ ViT-Large (ViT-L): 24 طبقة، 1024 بُعد مخفي، 16 رأس، 307 مليون معامل؛ ViT-Huge (ViT-H): 32 طبقة، 1280 بُعد مخفي، 16 رأس، 632 مليون معامل. نقارن مع خطوط الأساس للشبكات العصبية الالتفافية الأحدث والأفضل، وخاصة Big Transfer (BiT) القائمة على ResNet وNoisy Student القائمة على EfficientNet. نستخدم شبكات ResNet مع التطبيع الجماعي (GN) والالتفافات الموحدة لتحسين أداء النقل.

**التدريب والضبط الدقيق.** ندرب جميع النماذج باستخدام محسن Adam مع β₁ = 0.9، β₂ = 0.999، وحجم دفعة 4096، ونطبق تراجع وزن عالي قدره 0.1، والذي وجدنا أنه مفيد لنقل جميع النماذج. نستخدم إحماء معدل تعلم خطي وتراجع. للضبط الدقيق نستخدم SGD مع الزخم، وحجم دفعة 512، لجميع النماذج. لنتائج ImageNet، نقوم بالضبط الدقيق بدقة أعلى: 512 لـ ViT-L/16 و518 لـ ViT-H/14، ونستخدم أيضاً متوسط Polyak بمعامل 0.9999.

**المقاييس.** نبلغ عن النتائج من خلال دقة الضبط الدقيق ودقة التعلم بلقطات قليلة. للتعلم بلقطات قليلة، نحل مسألة انحدار المربعات الصغرى المنظمة التي تربط التمثيلات المجمدة للصور بمتجهات مستهدفة تحتوي على تسميات واحدة ساخنة للصورة المقابلة. تسمح لنا هذه الصيغة بالحل في شكل مغلق وحساب دقة التعلم بلقطات قليلة بسرعة كبيرة.

#### 4.2 المقارنة مع الأحدث والأفضل

نقارن محول الرؤية مع النماذج الأحدث والأفضل على معايير تصنيف الصور الشائعة. نقارن أولاً مع نماذج Big Transfer (BiT) التي تستخدم شبكات ResNet كبيرة مدربة على ImageNet-21k وJFT-300M. خط الأساس الثاني هو Noisy Student، الذي يُدرب على JFT-300M باستخدام التعلم شبه الخاضع للإشراف مع بيانات ImageNet إضافية غير مسماة.

يُظهر الجدول 2 النتائج. أفضل نموذج ViT، وهو ViT-H/14، المدرب مسبقاً على JFT-300M، يتفوق على جميع الأعمال السابقة في جميع مجموعات البيانات المختبرة بينما يتطلب موارد حسابية أقل بكثير للتدريب المسبق. على وجه الخصوص، يحقق ViT-H/14 دقة 88.55% على ImageNet (top-1)، و90.72% على ImageNet ReaL، و94.55% على CIFAR-100، و77.63% كمتوسط على مجموعة VTAB المكونة من 19 مهمة.

بالمقارنة مع BiT، فإن نموذج ViT-L/16 المدرب مسبقاً على JFT-300M يتفوق على BiT-L (وهو ResNet152x4) في جميع المهام، بينما يستغرق موارد أقل بكثير للتدريب. نموذج ViT-L/16 الأصغر المدرب مسبقاً على ImageNet-21k يؤدي بشكل جيد على معظم مجموعات البيانات أيضاً. يتطلب 8 نوى TPU فقط ويستغرق حوالي 30 يوماً للتدريب.

يُجري الشكل 5 مقارنة في فضاء الأداء-الحساب. تهيمن محولات الرؤية على شبكات ResNet في المقايضة بين الأداء والحساب. يستخدم ViT حوالي 2-4 مرات حساب أقل للوصول إلى نفس الأداء.

#### 4.3 متطلبات بيانات التدريب المسبق

يؤدي محول الرؤية بشكل جيد عند التدريب المسبق على مجموعات بيانات كبيرة. لكن ما مدى أهمية حجم مجموعة البيانات؟ ندرب نماذج ViT على مجموعات بيانات متزايدة الحجم: ImageNet وImageNet-21k وJFT-300M، ونقيّم أداء النقل.

يُظهر الشكل 3 النتائج. عند التدريب المسبق على أصغر مجموعة بيانات (ImageNet)، تؤدي النماذج ذات التكلفة الحسابية الأقل بشكل أفضل. على وجه الخصوص، يتفوق ViT-B/32 على ViT-B/16، وتؤدي نماذج ViT-L أداءً أقل من نماذج ViT-B. هذه النتيجة متوقعة إلى حد ما: لا تحتوي محولات الرؤية على الانحيازات الاستقرائية المدمجة في الشبكات العصبية الالتفافية (ثبات الإزاحة والمحلية)، لذا تحتاج إلى المزيد من البيانات لتعلم هذه الأنماط.

ومع ذلك، عند الانتقال إلى مجموعات البيانات الأكبر ImageNet-21k وJFT-300M، تنعكس الاتجاهات. تتفوق نماذج ViT-L على نماذج ViT-B، وتؤدي أحجام الرقع الأصغر إلى أداء أفضل. يشير هذا إلى أنه مع بيانات تدريب مسبق كافية، يمكن لمحولات الرؤية تعلم الأنماط ذات الصلة وتجاوز النماذج ذات الانحيازات الاستقرائية الأقوى.

نقارن أيضاً أداء ViT وResNet عند أحجام مختلفة من مجموعات البيانات. في مجموعات البيانات الأصغر، تتفوق شبكات ResNet على محولات الرؤية. تعاني محولات الرؤية من الإفراط في التخصيص أكثر من شبكات ResNet بتكلفة حسابية مماثلة على مجموعات البيانات الأصغر. ومع ذلك، بالنسبة لمجموعات البيانات الأكبر (ImageNet-21k وما فوق)، يتفوق ViT على ResNets.

#### 4.4 دراسة التوسع

نُجري دراسة منضبطة لأداء النقل مع توسيع نطاق النموذج ومجموعة البيانات. يُظهر الشكل 4 هذا التحليل. ندرب نماذج ViT متعددة بميزانيات حسابية مختلفة ونقارنها بشبكات ResNet والنماذج الهجينة. يتم تدريب جميع النماذج لحوالي 7 حقب، مما يضمن أن الحساب يهيمن عليه التدريب وليس التقييم.

تهيمن محولات الرؤية على شبكات ResNet في المقايضة بين الأداء والحساب. تُظهر النماذج الهجينة، التي تستخدم مستخرج خصائص ResNet متبوعاً بمحول، تحسناً طفيفاً على ViT النقي عند ميزانيات حسابية أصغر، لكن الفجوة تنغلق مع التوسع. يشير هذا إلى أن الانحياز الاستقرائي الالتفافي مفيد عندما تكون الموارد الحسابية محدودة، لكنه يصبح أقل أهمية مع التوسع.

#### 4.5 فحص محول الرؤية

لفهم كيف يعالج محول الرؤية الصور، نحلل التمثيلات المتعلمة. أولاً، نتصور تضمينات الموضع المتعلمة (الشكل 6). تتعلم تضمينات الموضع ترميز الموضع المكاني: الرقع الأقرب لديها تضمينات موضع أكثر تشابهاً، وتُظهر بنية التشابه نمطاً مكانياً ثنائي البعد واضحاً.

نحلل أيضاً أنماط الانتباه عبر الطبقات (الشكل 7). تنتبه بعض رؤوس الانتباه إلى معظم الصورة بالفعل في الطبقات الأدنى، مما يُظهر أن القدرة على دمج المعلومات عالمياً تُستخدم بواسطة النموذج. في الطبقات الأعمق، يصبح الانتباه أكثر تركيزاً وتخصصاً. نحسب متوسط مسافة الانتباه (في فضاء الصورة) لكل رأس انتباه في كل طبقة. "مسافة الانتباه" هذه مماثلة لحجم المجال المستقبِل في الشبكات العصبية الالتفافية. نجد أن بعض الرؤوس تنتبه إلى مناطق بعيدة حتى في الطبقات الأدنى، بينما تزداد مسافة الانتباه عبر الشبكة للرؤوس الأخرى، مشابهة لكيفية نمو المجالات المستقبِلة في الشبكات العصبية الالتفافية.

#### 4.6 الإشراف الذاتي

تُظهر المحولات أداءً مذهلاً في مهام معالجة اللغة الطبيعية عند التدريب المسبق باستخدام التعلم ذاتي الإشراف. متحفزين بهذا النجاح، نستكشف التنبؤ بالرقعة المقنعة للتدريب المسبق ذاتي الإشراف لـ ViT، مماثلاً لنمذجة اللغة المقنعة في BERT.

ندرب نموذج ViT-B/16 مع التنبؤ بالرقعة المقنعة على ImageNet. نشوه 50% من رموز الرقع عن طريق استبدالها بتضمين [MASK] متعلم (80% من الوقت)، أو رقعة عشوائية (10% من الوقت)، أو تركها دون تغيير (10% من الوقت). ثم نتنبأ باللون الوسطي بـ 3 بت (أي واحد من 512 لون) للرقع المقنعة.

يُظهر الجدول 4 أن التدريب المسبق ذاتي الإشراف على ImageNet يحقق دقة 79.9% على تصنيف ImageNet بعد الضبط الدقيق، وهو أفضل بـ 2% من التدريب من الصفر، لكنه لا يزال أقل بـ 4% من التدريب المسبق الخاضع للإشراف على ImageNet. نستنتج أن التدريب المسبق ذاتي الإشراف لـ ViT واعد لكنه يترك فجوة مقارنة بالتدريب المسبق الخاضع للإشراف واسع النطاق. استكشاف طرق أخرى للتدريب المسبق ذاتي الإشراف، مثل الطرق المتناقضة، هو اتجاه مستقبلي مثير للاهتمام.

---

### Translation Notes

- **Figures referenced:** Figures 3, 4, 5, 6, 7
- **Tables referenced:** Tables 2, 4
- **Key terms introduced:** few-shot learning (التعلم بلقطات قليلة), Polyak averaging (متوسط Polyak), attention distance (مسافة الانتباه), masked patch prediction (التنبؤ بالرقعة المقنعة), receptive field (المجال المستقبِل)
- **Equations:** Multiple numerical results and performance metrics
- **Citations:** 10+ references cited
- **Special handling:** Preserved all dataset names, model variant names (ViT-B/16, etc.), and numerical performance metrics exactly

### Back-Translation (Key Paragraph from 4.3)

**Pre-training data requirements paragraph:**
"When pre-trained on the smallest dataset (ImageNet), models with lower computational cost perform better. Specifically, ViT-B/32 outperforms ViT-B/16, and ViT-L models perform worse than ViT-B models. This result is somewhat expected: Vision Transformers do not contain the inductive biases built into CNNs (translation invariance and locality), so they need more data to learn these patterns. However, when moving to larger datasets ImageNet-21k and JFT-300M, the trends reverse. ViT-L models outperform ViT-B models, and smaller patch sizes lead to better performance."

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.85
- **Overall section score:** 0.86
