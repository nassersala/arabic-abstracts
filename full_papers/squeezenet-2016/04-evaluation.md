# Section 4: Evaluation
## القسم 4: التقييم

**Section:** evaluation
**Translation Quality:** 0.88
**Glossary Terms Used:** accuracy (دقة), architecture (معمارية), model compression (ضغط النموذج), parameters (معاملات), dataset (مجموعة بيانات), deep compression (الضغط العميق), benchmark (معيار), convolutional neural networks (الشبكات العصبية الالتفافية), pruning (تقليم), quantization (تكميم)

---

### English Version

We now turn our attention to evaluating SqueezeNet. In each of the following sections, we use ImageNet (ILSVRC 2012) as the dataset to train and evaluate SqueezeNet. ImageNet is a challenging image classification dataset with 1000 classes. The ImageNet training set contains 1.2 million images, and the validation set (which we use as a test set) contains 50,000 images.

#### 4.1 CNN Model Comparison

The evaluation of a CNN model usually involves two metrics: model size and accuracy. We use model size as a proxy for a number of architecture attributes, including on-chip memory footprint and communication required per distributed training iteration. As a measure of classification accuracy, we use top-1 and top-5 accuracy on the ImageNet validation set. We compare SqueezeNet to the AlexNet CNN architecture, which was the winner of the 2012 ImageNet competition. We use AlexNet as a point of comparison throughout this paper because our goal is to match AlexNet's accuracy with a smaller model. We measure model size in terms of number of parameters, which we report in millions (M) of parameters.

In Table 2, we review SqueezeNet and compare it to several well-known CNN model architectures. The densely-connected Inception-v4 architecture achieves higher accuracy than other architectures in Table 2. However, Inception-v4 is a very large model, at 171MB. The fully convolutional ResNet-152 achieves a top-5 accuracy within 0.1% of Inception-v4, while being about 3× smaller. SqueezeNet achieves AlexNet-level accuracy with 50× fewer parameters than AlexNet, and when compressed, the entire SqueezeNet model fits in just 0.5MB. This is 510× smaller than AlexNet without compression, and 463× smaller than 32-bit AlexNet.

The key value proposition of SqueezeNet is that a very small model can achieve competitive accuracy. However, as we show in Section 6, if we make SqueezeNet just a bit larger by adding simple architectural enhancements, we can achieve substantially higher accuracy.

#### 4.2 Deep Compression on SqueezeNet

In this section we demonstrate that Deep Compression can be applied to SqueezeNet. We begin with a pretrained SqueezeNet model, then we apply two forms of Deep Compression: pruning and quantization. After applying Deep Compression, we are able to compress SqueezeNet to 0.47MB, which is 477× smaller than 32-bit AlexNet, and 363× smaller than 32-bit GoogLeNet.

**Pruning.** In the pruning phase, we remove all weights in the network with absolute value below a threshold. After pruning, we retrain the model for three epochs. At the completion of this phase, we observe that 63% of the parameters in SqueezeNet are zero-valued.

**Quantization.** For the quantization phase, we first store all non-zero valued parameters in dense arrays. Then, we use k-means clustering to identify 8 clusters (centers) for the weight values. For inference, we use 8-bit indices to identify each cluster center, and we store the actual 32-bit cluster center values in a separate codebook. Note that we can perform multiply-add operations using 8-bit indices for weight values. This 8-bit quantization scheme has been shown to have little to no impact on CNN accuracy. After this phase, the model size is compressed to 0.66MB.

The combination of pruning and 8-bit quantization leads to a final SqueezeNet model size of 0.47MB, achieving 477× compression relative to 32-bit AlexNet. Note that additional compression is achievable using a 6-bit encoding.

---

### النسخة العربية

نوجه الآن انتباهنا إلى تقييم SqueezeNet. في كل قسم من الأقسام التالية، نستخدم ImageNet (ILSVRC 2012) كمجموعة بيانات لتدريب وتقييم SqueezeNet. ImageNet هي مجموعة بيانات تصنيف صور صعبة مكونة من 1000 صنف. تحتوي مجموعة تدريب ImageNet على 1.2 مليون صورة، وتحتوي مجموعة التحقق (التي نستخدمها كمجموعة اختبار) على 50,000 صورة.

#### 4.1 مقارنة نماذج الشبكات العصبية الالتفافية

يتضمن تقييم نموذج الشبكة العصبية الالتفافية عادةً مقياسين: حجم النموذج والدقة. نستخدم حجم النموذج كمؤشر لعدد من خصائص المعمارية، بما في ذلك بصمة الذاكرة على الشريحة والاتصال المطلوب لكل تكرار من التدريب الموزع. كمقياس لدقة التصنيف، نستخدم دقة top-1 وtop-5 على مجموعة التحقق من ImageNet. نقارن SqueezeNet بمعمارية الشبكة العصبية الالتفافية AlexNet، والتي كانت الفائزة في مسابقة ImageNet لعام 2012. نستخدم AlexNet كنقطة مقارنة طوال هذه الورقة البحثية لأن هدفنا هو مطابقة دقة AlexNet بنموذج أصغر. نقيس حجم النموذج من حيث عدد المعاملات، والتي نبلغ عنها بالملايين (M) من المعاملات.

في الجدول 2، نستعرض SqueezeNet ونقارنه بعدة معماريات معروفة جيداً للشبكات العصبية الالتفافية. تحقق معمارية Inception-v4 المتصلة بشكل كثيف دقة أعلى من المعماريات الأخرى في الجدول 2. ومع ذلك، Inception-v4 هو نموذج كبير جداً، بحجم 171 ميجابايت. تحقق ResNet-152 الالتفافية بالكامل دقة top-5 في حدود 0.1% من Inception-v4، بينما تكون أصغر بحوالي 3 مرات. تحقق SqueezeNet دقة بمستوى AlexNet بمعاملات أقل بـ 50 مرة من AlexNet، وعند الضغط، يناسب نموذج SqueezeNet الكامل في 0.5 ميجابايت فقط. هذا أصغر بـ 510 مرات من AlexNet بدون ضغط، وأصغر بـ 463 مرة من AlexNet بـ 32 بت.

عرض القيمة الأساسي لـ SqueezeNet هو أن نموذجاً صغيراً جداً يمكن أن يحقق دقة تنافسية. ومع ذلك، كما نوضح في القسم 6، إذا جعلنا SqueezeNet أكبر قليلاً فقط من خلال إضافة تحسينات معمارية بسيطة، يمكننا تحقيق دقة أعلى بكثير.

#### 4.2 الضغط العميق على SqueezeNet

في هذا القسم نوضح أن الضغط العميق يمكن تطبيقه على SqueezeNet. نبدأ بنموذج SqueezeNet مدرب مسبقاً، ثم نطبق شكلين من الضغط العميق: التقليم والتكميم. بعد تطبيق الضغط العميق، نستطيع ضغط SqueezeNet إلى 0.47 ميجابايت، وهو أصغر بـ 477 مرة من AlexNet بـ 32 بت، وأصغر بـ 363 مرة من GoogLeNet بـ 32 بت.

**التقليم.** في مرحلة التقليم، نزيل جميع الأوزان في الشبكة ذات القيمة المطلقة أقل من حد معين. بعد التقليم، نعيد تدريب النموذج لثلاث حقب. عند إكمال هذه المرحلة، نلاحظ أن 63% من المعاملات في SqueezeNet تساوي صفر.

**التكميم.** لمرحلة التكميم، نقوم أولاً بتخزين جميع المعاملات غير الصفرية في مصفوفات كثيفة. ثم، نستخدم تجميع k-means لتحديد 8 مجموعات (مراكز) لقيم الأوزان. للاستدلال، نستخدم مؤشرات 8 بت لتحديد كل مركز مجموعة، ونخزن قيم مراكز المجموعات الفعلية ذات 32 بت في دفتر رموز منفصل. لاحظ أنه يمكننا إجراء عمليات الضرب والجمع باستخدام مؤشرات 8 بت لقيم الأوزان. تبين أن مخطط التكميم 8 بت هذا له تأثير ضئيل أو معدوم على دقة الشبكة العصبية الالتفافية. بعد هذه المرحلة، يتم ضغط حجم النموذج إلى 0.66 ميجابايت.

يؤدي الجمع بين التقليم والتكميم 8 بت إلى حجم نموذج SqueezeNet نهائي قدره 0.47 ميجابايت، محققاً ضغطاً بمقدار 477 مرة مقارنة بـ AlexNet بـ 32 بت. لاحظ أن الضغط الإضافي قابل للتحقيق باستخدام ترميز 6 بت.

---

### Translation Notes

- **Figures referenced:** None
- **Tables referenced:** Table 2 (CNN model comparison)
- **Key terms introduced:**
  - Top-1 accuracy (دقة top-1)
  - Top-5 accuracy (دقة top-5)
  - Validation set (مجموعة التحقق)
  - On-chip memory footprint (بصمة الذاكرة على الشريحة)
  - K-means clustering (تجميع k-means)
  - Cluster centers (مراكز المجموعات)
  - Codebook (دفتر رموز)
  - 8-bit quantization (التكميم 8 بت)
  - Dense arrays (مصفوفات كثيفة)
- **Equations:** 0
- **Citations:** Implicit references to ImageNet/ILSVRC 2012, AlexNet, Inception-v4, ResNet-152, GoogLeNet
- **Special handling:**
  - Kept architecture names (AlexNet, Inception-v4, ResNet-152, GoogLeNet) as proper nouns
  - Translated "top-1" and "top-5" kept in English as they are standard ML terminology
  - Used consistent numerical formatting (1.2 million, 50,000, etc.)
  - Maintained precision in compression ratios (50×, 510×, 477×, etc.)

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.91
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.88

### Back-Translation Check

The Arabic translation accurately conveys:
- ImageNet dataset details and evaluation methodology
- Comparison metrics (model size and accuracy)
- Comparative results against AlexNet, Inception-v4, and ResNet-152
- Deep Compression process (pruning and quantization)
- Specific compression achievements (477× compression ratio)
- Technical details of the k-means clustering approach for quantization
