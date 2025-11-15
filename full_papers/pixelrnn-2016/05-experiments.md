# Section 5: Experiments
## القسم 5: التجارب

**Section:** experiments
**Translation Quality:** 0.88
**Glossary Terms Used:** log-likelihood, evaluation, training, discrete distribution, residual connections, receptive field, benchmark

---

### English Version

## 5 Experiments

### 5.1 Evaluation

The researchers evaluate models using log-likelihood from discrete distributions. They note that continuous and discrete models are directly comparable when uniform noise is added to pixel values during training. For MNIST, results are reported in nats (negative log-likelihood). For CIFAR-10 and ImageNet, measurements use bits per dimension, calculated by normalizing total discrete log-likelihood by image dimensionality. This approach represents the number of bits that a compression scheme based on this model would need for each RGB value.

### 5.2 Training Details

Models were trained on GPUs using Torch. The authors employed RMSProp for parameter updates, finding it provided optimal convergence. Learning rates and batch sizes varied by dataset: smaller batches (16 images) for MNIST and CIFAR-10 helped regularize models, while ImageNet used larger batches (32-64 images) constrained by GPU memory. No preprocessing or data augmentation was applied beyond input scaling and centering. Initial recurrent states were learned during training.

### 5.3 Discrete Softmax Distribution

Using softmax on discrete pixel values outperformed mixture density approaches on continuous values. The Row LSTM with softmax achieved 3.06 bits/dim on CIFAR-10 validation, compared to 3.22 bits/dim using Mixture of Conditional Gaussian Scale Mixtures. The discrete approach offers representational advantages: multimodal distributions without shape priors emerge naturally. Values 0 and 255 receive higher probabilities reflecting their frequency, and no distribution mass falls outside the valid range [0, 255].

### 5.4 Residual Connections

Table 2 demonstrates that residual connections matched skip connection performance on the 12-layer CIFAR-10 Row LSTM (3.07 bits/dim with residual, no skip versus 3.09 bits/dim with skip, no residual). Combined use proved most effective. Table 3 shows performance improvement with network depth up to 12 LSTM layers, with results improving from 3.30 bits/dim (1 layer) to 3.06 bits/dim (12 layers).

### 5.5 MNIST

On binary MNIST, the Diagonal BiLSTM (7 layers, h=16) achieved 79.20 nats, reported as the best result on MNIST so far. This surpassed previous approaches including DRAW (≤80.97 nats) and DARN (≈84.13 nats).

### 5.6 CIFAR-10

The Diagonal BiLSTM performed best (3.00 bits/dim), followed by Row LSTM (3.07) and PixelCNN (3.14). Performance correlated with receptive field size, suggesting that effectively capturing a large receptive field is important for this task.

### 5.7 ImageNet

No published generative model results existed for ImageNet at publication. The authors provide first benchmarks: 32×32 images achieved 3.86 bits/dim (validation), while 64×64 images achieved 3.63 bits/dim. The researchers note ImageNet images are less compressible than CIFAR-10 images due to greater visual variety and sharper downsampling producing less correlated neighboring pixels. Multi-scale conditioning improved visual coherence in 64×64 samples despite similar likelihood scores.

---

### النسخة العربية

## 5 التجارب

### 5.1 التقييم

يقيّم الباحثون النماذج باستخدام اللوغاريتم الاحتمالي من التوزيعات المنفصلة. يلاحظون أن النماذج المستمرة والمنفصلة قابلة للمقارنة مباشرة عند إضافة ضوضاء موحدة إلى قيم البكسل أثناء التدريب. بالنسبة لـ MNIST، يتم الإبلاغ عن النتائج بوحدة النات (اللوغاريتم الاحتمالي السلبي). بالنسبة لـ CIFAR-10 و ImageNet، تستخدم القياسات البتات لكل بُعد، محسوبة بتطبيع إجمالي اللوغاريتم الاحتمالي المنفصل بأبعاد الصورة. يمثل هذا النهج عدد البتات التي سيحتاجها مخطط ضغط قائم على هذا النموذج لكل قيمة RGB.

### 5.2 تفاصيل التدريب

تم تدريب النماذج على وحدات معالجة الرسومات باستخدام Torch. استخدم المؤلفون RMSProp لتحديثات المعاملات، ووجدوا أنه يوفر تقارباً مثالياً. تختلف معدلات التعلم وأحجام الدفعات حسب مجموعة البيانات: ساعدت الدفعات الأصغر (16 صورة) لـ MNIST و CIFAR-10 على تنظيم النماذج، بينما استخدم ImageNet دفعات أكبر (32-64 صورة) مقيدة بذاكرة وحدة معالجة الرسومات. لم يتم تطبيق أي معالجة مسبقة أو زيادة بيانات بخلاف قياس الإدخال والتمركز. تم تعلم الحالات التكرارية الأولية أثناء التدريب.

### 5.3 توزيع Softmax المنفصل

تفوق استخدام softmax على قيم البكسل المنفصلة على مناهج كثافة المزيج على القيم المستمرة. حقق صف LSTM مع softmax 3.06 بت/بُعد على تحقق CIFAR-10، مقارنة بـ 3.22 بت/بُعد باستخدام خليط مزيجات القياس الغوسية الشرطية. يوفر النهج المنفصل مزايا تمثيلية: تظهر التوزيعات متعددة الأنماط دون افتراضات مسبقة حول الشكل بشكل طبيعي. تتلقى القيم 0 و 255 احتمالات أعلى تعكس تكرارها، ولا تقع كتلة التوزيع خارج النطاق الصالح [0، 255].

### 5.4 الاتصالات المتبقية

يوضح الجدول 2 أن الاتصالات المتبقية طابقت أداء اتصالات التخطي على صف LSTM من 12 طبقة CIFAR-10 (3.07 بت/بُعد مع المتبقي، بدون تخطي مقابل 3.09 بت/بُعد مع التخطي، بدون متبقي). أثبت الاستخدام المشترك أنه الأكثر فعالية. يُظهر الجدول 3 تحسن الأداء مع عمق الشبكة حتى 12 طبقة LSTM، مع تحسن النتائج من 3.30 بت/بُعد (طبقة واحدة) إلى 3.06 بت/بُعد (12 طبقة).

### 5.5 MNIST

على MNIST الثنائي، حققت القطرية BiLSTM (7 طبقات، h=16) 79.20 نات، تم الإبلاغ عنها كأفضل نتيجة على MNIST حتى الآن. تجاوز هذا المناهج السابقة بما في ذلك DRAW (≤80.97 نات) و DARN (≈84.13 نات).

### 5.6 CIFAR-10

أداء القطرية BiLSTM الأفضل (3.00 بت/بُعد)، تليها صف LSTM (3.07) و PixelCNN (3.14). ارتبط الأداء بحجم مجال الاستقبال، مما يشير إلى أن التقاط مجال استقبال كبير بشكل فعال أمر مهم لهذه المهمة.

### 5.7 ImageNet

لم تكن هناك نتائج نموذج توليدي منشورة لـ ImageNet عند النشر. يوفر المؤلفون المعايير المرجعية الأولى: حققت صور 32×32 3.86 بت/بُعد (التحقق)، بينما حققت صور 64×64 3.63 بت/بُعد. يلاحظ الباحثون أن صور ImageNet أقل قابلية للضغط من صور CIFAR-10 بسبب التنوع البصري الأكبر وإعادة العينات الأكثر حدة التي تنتج بكسلات مجاورة أقل ارتباطاً. حسّن التكييف متعدد المقاييس التماسك البصري في عينات 64×64 على الرغم من درجات الاحتمالية المماثلة.

---

### Translation Notes

- **Figures referenced:** Table 2, Table 3 (referenced but not reproduced)
- **Key terms introduced:** bits per dimension, nats, RMSProp, mixture density, multimodal distributions
- **Equations:** None
- **Citations:** References to DRAW and DARN models
- **Special handling:** Technical terms like "bits/dim" and "nats" kept with Arabic explanation. Dataset names kept in English.

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.88
