# Section 4: Experiments
## القسم 4: التجارب

**Section:** experiments
**Translation Quality:** 0.86
**Glossary Terms Used:** MNIST, dataset, distortion, rotation, translation, scale, affine, projective, thin plate spline, convolutional, fully-connected, baseline, error rate, SGD, cross-entropy, loss function, benchmark, ImageNet, classification, accuracy, attention, parallel

---

### English Version

## 4.1 Distorted MNIST

The researchers evaluated spatial transformer networks on MNIST data with various distortions: rotation (R), rotation/scale/translation (RTS), projective transformation (P), and elastic warping (E).

**Setup:** Networks compared included fully-connected (FCN) and convolutional (CNN) baselines, plus spatial transformer variants (ST-FCN and ST-CNN). The spatial transformers employed different transformation functions: affine, projective, and 16-point thin plate spline (TPS). All models had approximately the same number of parameters and used identical training schemes with SGD and multinomial cross-entropy loss.

**Key Results:** ST-CNN models consistently outperformed baselines. For RTS distortions, ST-CNN achieved 0.5-0.6% error versus 0.8% for CNN. On 60×60 translated MNIST with clutter, ST-FCN achieved 2.0% error and ST-CNN achieved 1.7% error, compared to 3.5% for CNN baseline.

The thin plate spline transformation proved most powerful, effectively reshaping the input into a prototype instance for elastic distortions. Networks learned to transform inputs to a canonical upright pose matching the training data mean.

## 4.2 Street View House Numbers

This section tested spatial transformer networks on real-world multi-digit house number recognition using the SVHN dataset (~200k images with 1-5 digits per image).

**Experimental Design:** Following established protocols, researchers used 64×64 pixel crops and additional 128×128 pixel crops with more background. They created a baseline character sequence CNN with 11 hidden layers and five independent softmax classifiers for variable-length digit sequences.

Two ST variants were developed: ST-CNN Single (one spatial transformer before initial convolution) and ST-CNN Multi (spatial transformers before first four convolutional layers). The ST-CNN Multi approach allowed deeper spatial transformers to predict a transformation based on richer features.

**Performance Metrics:** ST-CNN Single achieved 3.7% error (64px) and 3.9% error (128px). ST-CNN Multi reached state-of-the-art with 3.6% error (64px) and 3.9% error (128px), surpassing previous best of 3.9% at 64px. Notably, performance remained stable on 128×128 images where competing methods degraded. The ST-CNN Multi was only 6% slower (forward and backward pass) than the CNN.

## 4.3 Fine-Grained Classification

Researchers applied multiple parallel spatial transformers to fine-grained bird classification using the CUB-200-2011 dataset (6k training, 5.8k test images across 200 bird species).

**Architecture:** The baseline used an Inception architecture with batch normalization pre-trained on ImageNet, achieving 82.3% accuracy. The ST-CNN employed 2 or 4 parallel spatial transformers parameterized for attention, sampling 224×224 crops from input images. Each crop was processed by separate Inception streams, with outputs concatenated and classified via a 200-way softmax layer.

**Results:** ST-CNN with 4 parallel transformers achieved 84.1% accuracy, improving baseline by 1.8%. Visualizations revealed interesting learned behaviors: one transformer detected bird heads while another focused on body regions, demonstrating part detectors discovered in a data-driven manner without any additional supervision. Using 448px resolution inputs showed no performance degradation due to downsampling after transformations.

---

### النسخة العربية

## 4.1 MNIST المشوَّه

قيّم الباحثون شبكات المحوّل المكاني على بيانات MNIST مع تشوهات مختلفة: الدوران (R)، والدوران/التحجيم/الإزاحة (RTS)، والتحويل الإسقاطي (P)، والالتواء المرن (E).

**الإعداد:** شملت الشبكات المقارنة خطوط أساس متصلة بالكامل (FCN) والتفافية (CNN)، بالإضافة إلى متغيرات المحوّل المكاني (ST-FCN وST-CNN). استخدمت المحوّلات المكانية دوال تحويل مختلفة: أفينية، وإسقاطية، وشريحة صفيحة رقيقة بـ16 نقطة (TPS). كان لجميع النماذج عدد متقارب من المعاملات واستخدمت نفس مخططات التدريب مع SGD وخسارة الإنتروبيا المتقاطعة متعددة الحدود.

**النتائج الرئيسية:** تفوقت نماذج ST-CNN باستمرار على خطوط الأساس. بالنسبة لتشوهات RTS، حقق ST-CNN خطأ 0.5-0.6% مقابل 0.8% لـCNN. على MNIST المزاح 60×60 مع الفوضى، حقق ST-FCN خطأ 2.0% وحقق ST-CNN خطأ 1.7%، مقارنة بـ3.5% لخط الأساس CNN.

أثبت تحويل شريحة الصفيحة الرقيقة أنه الأقوى، حيث أعاد تشكيل الإدخال بفعالية إلى نموذج أولي للتشوهات المرنة. تعلمت الشبكات تحويل المدخلات إلى وضعية قائمة معيارية تطابق متوسط بيانات التدريب.

## 4.2 أرقام منازل ستريت فيو

اختبر هذا القسم شبكات المحوّل المكاني على التعرف على أرقام المنازل متعددة الأرقام في العالم الحقيقي باستخدام مجموعة بيانات SVHN (~200 ألف صورة مع 1-5 أرقام لكل صورة).

**التصميم التجريبي:** باتباع البروتوكولات المعمول بها، استخدم الباحثون قصاصات بكسل 64×64 وقصاصات بكسل 128×128 إضافية مع خلفية أكثر. أنشأوا شبكة CNN أساسية لتسلسل الأحرف بـ11 طبقة مخفية وخمسة مصنفات softmax مستقلة لتسلسلات الأرقام متغيرة الطول.

تم تطوير متغيرين من ST: ST-CNN أحادي (محوّل مكاني واحد قبل الالتفاف الأولي) وST-CNN متعدد (محوّلات مكانية قبل أول أربع طبقات التفافية). سمح نهج ST-CNN المتعدد للمحوّلات المكانية الأعمق بالتنبؤ بتحويل بناءً على ميزات أغنى.

**مقاييس الأداء:** حقق ST-CNN الأحادي خطأ 3.7% (64 بكسل) و3.9% (128 بكسل). وصل ST-CNN المتعدد إلى الحالة المتقدمة بخطأ 3.6% (64 بكسل) و3.9% (128 بكسل)، متجاوزاً الأفضل السابق البالغ 3.9% عند 64 بكسل. والجدير بالذكر أن الأداء ظل مستقراً على صور 128×128 حيث تدهورت الطرق المنافسة. كان ST-CNN المتعدد أبطأ بنسبة 6% فقط (مرور أمامي وخلفي) من CNN.

## 4.3 التصنيف الدقيق

طبق الباحثون محوّلات مكانية متوازية متعددة على تصنيف الطيور الدقيق باستخدام مجموعة بيانات CUB-200-2011 (6 آلاف صورة تدريب، 5.8 آلاف صورة اختبار عبر 200 نوع من الطيور).

**المعمارية:** استخدم خط الأساس معمارية Inception مع تطبيع الدفعات مُدرَّبة مسبقاً على ImageNet، محققةً دقة 82.3%. استخدم ST-CNN محوّلين أو 4 محوّلات مكانية متوازية ذات معاملات للانتباه، تأخذ عينات قصاصات 224×224 من صور الإدخال. تمت معالجة كل قصاصة بواسطة تدفقات Inception منفصلة، مع ربط المخرجات وتصنيفها عبر طبقة softmax بـ200 اتجاه.

**النتائج:** حقق ST-CNN مع 4 محوّلات متوازية دقة 84.1%، محسناً خط الأساس بنسبة 1.8%. كشفت التصورات عن سلوكيات مُتعلَّمة مثيرة للاهتمام: اكتشف محوّل واحد رؤوس الطيور بينما ركز آخر على مناطق الجسم، مما يُظهر كاشفات أجزاء مكتشفة بطريقة مدفوعة بالبيانات دون أي إشراف إضافي. أظهر استخدام مدخلات بدقة 448 بكسل عدم تدهور الأداء بسبب أخذ عينات أقل بعد التحويلات.

---

### Translation Notes

- **Figures referenced:** Implicit references to experimental result figures and visualizations
- **Key terms introduced:**
  - Distorted MNIST (MNIST المشوَّه)
  - Elastic warping (الالتواء المرن)
  - Thin plate spline (شريحة الصفيحة الرقيقة)
  - Clutter (الفوضى)
  - Street View House Numbers (أرقام منازل ستريت فيو)
  - Multi-digit recognition (التعرف متعدد الأرقام)
  - Fine-grained classification (التصنيف الدقيق)
  - Part detectors (كاشفات الأجزاء)
  - Batch normalization (تطبيع الدفعات)
  - Inception architecture (معمارية Inception)

- **Equations:** 0
- **Citations:** Multiple (dataset references, prior work comparisons)
- **Special handling:**
  - Dataset names kept in English (MNIST, SVHN, CUB-200-2011, ImageNet)
  - Percentage values and accuracy metrics preserved exactly
  - "Canonical upright pose" translated as "وضعية قائمة معيارية"
  - "Data-driven manner" translated as "بطريقة مدفوعة بالبيانات"
  - "Forward and backward pass" translated as "مرور أمامي وخلفي"
  - Architecture names kept in English (FCN, CNN, ST-CNN, Inception)

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86

### Back-Translation

## 4.1 Distorted MNIST

Researchers evaluated spatial transformer networks on MNIST data with various distortions: rotation (R), rotation/scaling/translation (RTS), projective transformation (P), and elastic warping (E).

**Setup:** Compared networks included fully-connected (FCN) and convolutional (CNN) baselines, in addition to spatial transformer variants (ST-FCN and ST-CNN). Spatial transformers used different transformation functions: affine, projective, and 16-point thin plate spline (TPS). All models had approximately the same number of parameters and used the same training schemes with SGD and multinomial cross-entropy loss.

**Key Results:** ST-CNN models consistently outperformed baselines. For RTS distortions, ST-CNN achieved 0.5-0.6% error versus 0.8% for CNN. On translated 60×60 MNIST with clutter, ST-FCN achieved 2.0% error and ST-CNN achieved 1.7% error, compared to 3.5% for CNN baseline.

Thin plate spline transformation proved most powerful, effectively reshaping the input into a prototype for elastic distortions. Networks learned to transform inputs to a canonical upright pose matching the training data mean.

## 4.2 Street View House Numbers

This section tested spatial transformer networks on multi-digit house number recognition in the real world using the SVHN dataset (~200k images with 1-5 digits per image).

**Experimental Design:** Following established protocols, researchers used 64×64 pixel crops and additional 128×128 pixel crops with more background. They created a baseline CNN for character sequences with 11 hidden layers and five independent softmax classifiers for variable-length digit sequences.

Two ST variants were developed: ST-CNN Single (one spatial transformer before initial convolution) and ST-CNN Multi (spatial transformers before first four convolutional layers). The ST-CNN Multi approach allowed deeper spatial transformers to predict transformation based on richer features.

**Performance Metrics:** ST-CNN Single achieved 3.7% error (64 pixels) and 3.9% (128 pixels). ST-CNN Multi reached state-of-the-art with 3.6% error (64 pixels) and 3.9% (128 pixels), surpassing previous best of 3.9% at 64 pixels. Notably, performance remained stable on 128×128 images where competing methods degraded. ST-CNN Multi was only 6% slower (forward and backward pass) than CNN.

## 4.3 Fine-Grained Classification

Researchers applied multiple parallel spatial transformers to fine-grained bird classification using the CUB-200-2011 dataset (6k training images, 5.8k test images across 200 bird species).

**Architecture:** Baseline used Inception architecture with batch normalization pre-trained on ImageNet, achieving 82.3% accuracy. ST-CNN used 2 or 4 parallel spatial transformers parameterized for attention, sampling 224×224 crops from input images. Each crop was processed by separate Inception streams, with outputs concatenated and classified via 200-way softmax layer.

**Results:** ST-CNN with 4 parallel transformers achieved 84.1% accuracy, improving baseline by 1.8%. Visualizations revealed interesting learned behaviors: one transformer detected bird heads while another focused on body regions, demonstrating part detectors discovered in a data-driven manner without additional supervision. Using 448-pixel resolution inputs showed no performance degradation due to downsampling after transformations.
