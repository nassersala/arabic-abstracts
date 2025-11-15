# Section 2: Related Work
## القسم 2: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.87
**Glossary Terms Used:** convolutional neural networks, accuracy, efficiency, architecture, depth, width, resolution, neural architecture search, automated, computational cost, parameters

---

### English Version

**ConvNet Accuracy:** Since AlexNet won the 2012 ImageNet competition, ConvNets have become increasingly more accurate by going bigger: while the 2014 ImageNet winner GoogleNet achieves 74.8% top-1 accuracy with about 6.8M parameters, the 2017 ImageNet winner SENet achieves 82.7% top-1 accuracy with 145M parameters. Recently, GPipe further pushes the state-of-the-art ImageNet top-1 validation accuracy to 84.3% using 557M parameters: it is so big that it can only be trained with a specialized pipeline parallelism library by partitioning the network and spreading each part to a different accelerator. While these models are mainly designed for ImageNet, recent studies have shown better ImageNet models also perform better across a variety of transfer learning datasets, and across different computer vision tasks such as object detection. Although higher accuracy is critical for many applications, we have already hit the hardware memory limit, and thus further accuracy gain needs better efficiency.

**ConvNet Efficiency:** Deep ConvNets are often over-parameterized. Model compression is a common way to reduce model size by trading accuracy for efficiency. As mobile phones become ubiquitous, it is also common to handcraft efficient mobile-size ConvNets, such as SqueezeNets, MobileNets, and ShuffleNets. Recently, neural architecture search becomes popular in designing efficient mobile-size ConvNets, and achieves even better efficiency than hand-crafted mobile ConvNets by extensively tuning the network width, depth, convolution kernel types and sizes. However, it is unclear how to apply these techniques for larger models that have much larger design space and much more expensive tuning cost. In this paper, we aim to study model efficiency for super large ConvNets that surpass state-of-the-art accuracy. To achieve this goal, we resort to model scaling.

**Model Scaling:** There are many ways to scale a ConvNet for different resource constraints: ResNet can be scaled down (e.g., ResNet-18) or up (e.g., ResNet-200) by adjusting network depth (#layers), while WideResNet and MobileNets can be scaled by network width (#channels). It is also well-recognized that bigger input image size will help accuracy with the overhead of more FLOPS. Although prior studies have shown that network depth and width are both important for ConvNets' expressive power, it still remains an open question of how to effectively scale a ConvNet to achieve better efficiency and accuracy. Our work systematically and empirically studies ConvNet scaling for all three dimensions of network width, depth, and resolutions.

---

### النسخة العربية

**دقة الشبكات الالتفافية:** منذ أن فاز AlexNet بمسابقة ImageNet لعام 2012، أصبحت الشبكات الالتفافية أكثر دقة بشكل متزايد من خلال أن تصبح أكبر: بينما حقق الفائز بـ ImageNet لعام 2014 وهو GoogleNet دقة 74.8% في أفضل 1 مع حوالي 6.8 مليون معامل، حقق الفائز بـ ImageNet لعام 2017 وهو SENet دقة 82.7% في أفضل 1 مع 145 مليون معامل. مؤخراً، دفع GPipe دقة التحقق من أفضل 1 على ImageNet المتقدمة إلى 84.3% باستخدام 557 مليون معامل: إنه كبير جداً لدرجة أنه لا يمكن تدريبه إلا باستخدام مكتبة متخصصة للتوازي الأنبوبي من خلال تقسيم الشبكة ونشر كل جزء على مسرّع مختلف. بينما تم تصميم هذه النماذج بشكل أساسي لـ ImageNet، أظهرت الدراسات الحديثة أن نماذج ImageNet الأفضل تؤدي أيضاً بشكل أفضل عبر مجموعة متنوعة من مجموعات بيانات التعلم بالنقل، وعبر مهام رؤية حاسوبية مختلفة مثل كشف الكائنات. على الرغم من أن الدقة الأعلى أمر بالغ الأهمية للعديد من التطبيقات، فقد وصلنا بالفعل إلى حد ذاكرة الأجهزة، وبالتالي فإن المزيد من تحسين الدقة يحتاج إلى كفاءة أفضل.

**كفاءة الشبكات الالتفافية:** غالباً ما تكون الشبكات الالتفافية العميقة معاملاتها زائدة. ضغط النموذج هو طريقة شائعة لتقليل حجم النموذج عن طريق مقايضة الدقة بالكفاءة. نظراً لأن الهواتف المحمولة أصبحت موجودة في كل مكان، فمن الشائع أيضاً صياغة شبكات التفافية فعالة بحجم الهاتف المحمول يدوياً، مثل SqueezeNets وMobileNets وShuffleNets. مؤخراً، أصبح البحث عن معمارية عصبية شائعاً في تصميم شبكات التفافية فعالة بحجم الهاتف المحمول، ويحقق كفاءة أفضل من الشبكات الالتفافية المحمولة المصنوعة يدوياً من خلال ضبط عرض الشبكة وعمقها وأنواع نواة الالتفاف وأحجامها على نطاق واسع. ومع ذلك، فمن غير الواضح كيفية تطبيق هذه التقنيات على نماذج أكبر لها مساحة تصميم أكبر بكثير وتكلفة ضبط أكثر تكلفة بكثير. في هذه الورقة، نهدف إلى دراسة كفاءة النموذج للشبكات الالتفافية الكبيرة للغاية التي تتجاوز الدقة المتقدمة. لتحقيق هذا الهدف، نلجأ إلى توسيع النموذج.

**توسيع النموذج:** هناك العديد من الطرق لتوسيع الشبكة الالتفافية لقيود الموارد المختلفة: يمكن تصغير ResNet (على سبيل المثال، ResNet-18) أو تكبيرها (على سبيل المثال، ResNet-200) عن طريق تعديل عمق الشبكة (عدد الطبقات)، بينما يمكن توسيع WideResNet وMobileNets من خلال عرض الشبكة (عدد القنوات). من المعترف به جيداً أيضاً أن حجم صورة الإدخال الأكبر سيساعد في الدقة مع تكلفة إضافية من المزيد من FLOPS. على الرغم من أن الدراسات السابقة أظهرت أن عمق الشبكة وعرضها كلاهما مهمان للقوة التعبيرية للشبكات الالتفافية، لا يزال من الأسئلة المفتوحة كيفية توسيع الشبكة الالتفافية بشكل فعال لتحقيق كفاءة ودقة أفضل. يدرس عملنا بشكل منهجي وتجريبي توسيع الشبكة الالتفافية لجميع الأبعاد الثلاثة لعرض الشبكة وعمقها ودقة الوضوح.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** Pipeline parallelism, model compression, over-parameterized, transfer learning, FLOPS, expressive power
- **Equations:** 0
- **Citations:** AlexNet, GoogleNet, SENet, GPipe, SqueezeNets, MobileNets, ShuffleNets, ResNet, WideResNet
- **Special handling:** All model and architecture names kept in English as per convention

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-Translation (Key Paragraph)

"There are many ways to scale a convolutional network for different resource constraints: ResNet can be scaled down (for example, ResNet-18) or scaled up (for example, ResNet-200) by adjusting the network depth (number of layers), while WideResNet and MobileNets can be scaled through network width (number of channels). It is also well recognized that larger input image size will help with accuracy at the additional cost of more FLOPS. Although previous studies have shown that both network depth and width are important for the expressive power of convolutional networks, it remains an open question how to effectively scale a convolutional network to achieve better efficiency and accuracy."
