# Section 2: Related Work
## القسم 2: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.86
**Glossary Terms Used:** ConvNet, accuracy, efficiency, model compression, neural architecture search, mobile, scaling, depth, width, resolution, FLOPS

---

### English Version

**ConvNet Accuracy:** Since AlexNet (Krizhevsky et al., 2012) won the 2012 ImageNet competition, ConvNets have become increasingly more accurate by going bigger: while the 2014 ImageNet winner GoogleNet (Szegedy et al., 2015) achieves 74.8% top-1 accuracy with about 6.8M parameters, the 2017 ImageNet winner SENet (Hu et al., 2018) achieves 82.7% top-1 accuracy with 145M parameters. Recently, GPipe (Huang et al., 2018) further pushes the state-of-the-art ImageNet top-1 validation accuracy to 84.3% using 557M parameters: it is so big that it can only be trained with a specialized pipeline parallelism library by partitioning the network and spreading each part to a different accelerator. While these models are mainly designed for ImageNet, recent studies have shown better ImageNet models also perform better across a variety of transfer learning datasets (Kornblith et al., 2019), and other computer vision tasks such as object detection (He et al., 2016; Tan et al., 2019). Although higher accuracy is critical for many applications, we have already hit the hardware memory limit, and thus further accuracy gain needs better efficiency.

**ConvNet Efficiency:** Deep ConvNets are often over-parameterized. Model compression (Han et al., 2016; He et al., 2018; Yang et al., 2018) is a common way to reduce model size by trading accuracy for efficiency. As mobile phones become ubiquitous, it is also common to hand-craft efficient mobile-size ConvNets, such as SqueezeNets (Iandola et al., 2016; Gholami et al., 2018), MobileNets (Howard et al., 2017; Sandler et al., 2018), and ShuffleNets (Zhang et al., 2018; Ma et al., 2018). Recently, neural architecture search becomes increasingly popular in designing efficient mobile-size ConvNets (Tan et al., 2019; Cai et al., 2019), and achieves even better efficiency than hand-crafted mobile ConvNets by extensively tuning the network width, depth, convolution kernel types and sizes. However, it is unclear how to apply these techniques for larger models that have much larger design space and much more expensive tuning cost. In this paper, we aim to study model efficiency for super large ConvNets that surpass state-of-the-art accuracy. To achieve this goal, we resort to model scaling.

**Model Scaling:** There are many ways to scale a ConvNet for different resource constraints: ResNet (He et al., 2016) can be scaled down (e.g., ResNet-18) or up (e.g., ResNet-200) by adjusting network depth (#layers), while WideResNet (Zagoruyko & Komodakis, 2016) and MobileNets (Howard et al., 2017) can be scaled by network width (#channels). It is also well-recognized that bigger input image size will help accuracy with the overhead of more FLOPS. Although prior studies (Raghu et al., 2017; Lin & Jegelka, 2018; Sharir & Shashua, 2018; Lu et al., 2018) have shown that network depth and width are both important for ConvNets' expressive power, it still remains an open question of how to effectively scale a ConvNet to achieve better efficiency and accuracy. Our work systematically and empirically studies ConvNet scaling for all three dimensions of network width, depth, and resolutions.

---

### النسخة العربية

**دقة الشبكات الالتفافية:** منذ أن فاز AlexNet (Krizhevsky et al., 2012) بمسابقة ImageNet لعام 2012، أصبحت الشبكات الالتفافية أكثر دقة بشكل متزايد من خلال التكبير: بينما حقق الفائز في ImageNet لعام 2014 وهو GoogleNet (Szegedy et al., 2015) دقة 74.8% في أفضل 1 مع حوالي 6.8 مليون معامل، حقق الفائز في ImageNet لعام 2017 وهو SENet (Hu et al., 2018) دقة 82.7% في أفضل 1 مع 145 مليون معامل. مؤخراً، دفع GPipe (Huang et al., 2018) دقة التحقق في أفضل 1 على ImageNet المتقدمة إلى 84.3% باستخدام 557 مليون معامل: إنه كبير جداً لدرجة أنه لا يمكن تدريبه إلا باستخدام مكتبة متخصصة للتوازي الأنبوبي من خلال تقسيم الشبكة ونشر كل جزء على مسرّع مختلف. بينما تم تصميم هذه النماذج بشكل رئيسي لـ ImageNet، أظهرت الدراسات الحديثة أن نماذج ImageNet الأفضل تؤدي أيضاً بشكل أفضل عبر مجموعة متنوعة من مجموعات بيانات التعلم بالنقل (Kornblith et al., 2019)، ومهام رؤية الحاسوب الأخرى مثل كشف الأشياء (He et al., 2016; Tan et al., 2019). على الرغم من أن الدقة الأعلى حاسمة للعديد من التطبيقات، فقد وصلنا بالفعل إلى حد ذاكرة الأجهزة، وبالتالي فإن تحقيق مزيد من الدقة يحتاج إلى كفاءة أفضل.

**كفاءة الشبكات الالتفافية:** غالباً ما تكون الشبكات الالتفافية العميقة مُفرطة في المعاملات. ضغط النموذج (Han et al., 2016; He et al., 2018; Yang et al., 2018) هو طريقة شائعة لتقليل حجم النموذج من خلال المقايضة بين الدقة والكفاءة. مع انتشار الهواتف المحمولة في كل مكان، من الشائع أيضاً صياغة شبكات التفافية فعالة بحجم الهاتف المحمول يدوياً، مثل SqueezeNets (Iandola et al., 2016; Gholami et al., 2018)، وMobileNets (Howard et al., 2017; Sandler et al., 2018)، وShuffleNets (Zhang et al., 2018; Ma et al., 2018). مؤخراً، أصبح البحث عن معمارية عصبية شائعاً بشكل متزايد في تصميم شبكات التفافية فعالة بحجم الهاتف المحمول (Tan et al., 2019; Cai et al., 2019)، ويحقق كفاءة أفضل من الشبكات الالتفافية المحمولة المصنوعة يدوياً من خلال الضبط الموسع لعرض الشبكة وعمقها وأنواع وأحجام نواة الالتفاف. ومع ذلك، من غير الواضح كيفية تطبيق هذه التقنيات على النماذج الأكبر التي لديها مساحة تصميم أكبر بكثير وتكلفة ضبط أكثر تكلفة بكثير. في هذه الورقة، نهدف إلى دراسة كفاءة النموذج للشبكات الالتفافية الفائقة الكبر التي تتجاوز الدقة المتقدمة. لتحقيق هذا الهدف، نلجأ إلى توسيع النموذج.

**توسيع النموذج:** هناك العديد من الطرق لتوسيع شبكة التفافية لقيود موارد مختلفة: يمكن تقليص ResNet (He et al., 2016) (مثل ResNet-18) أو توسيعه (مثل ResNet-200) عن طريق تعديل عمق الشبكة (عدد الطبقات)، بينما يمكن توسيع WideResNet (Zagoruyko & Komodakis, 2016) وMobileNets (Howard et al., 2017) من خلال عرض الشبكة (عدد القنوات). من المعترف به جيداً أيضاً أن حجم صورة المُدخلات الأكبر سيساعد في الدقة مع تكلفة إضافية من FLOPS أكثر. على الرغم من أن الدراسات السابقة (Raghu et al., 2017; Lin & Jegelka, 2018; Sharir & Shashua, 2018; Lu et al., 2018) قد أظهرت أن عمق الشبكة وعرضها مهمان لقدرة الشبكات الالتفافية على التعبير، لا يزال السؤال مفتوحاً حول كيفية توسيع شبكة التفافية بفعالية لتحقيق كفاءة ودقة أفضل. يدرس عملنا توسيع الشبكات الالتفافية بشكل منهجي وتجريبي لجميع الأبعاد الثلاثة لعرض الشبكة وعمقها ودقة الوضوح.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** over-parameterized (مُفرطة في المعاملات), model compression (ضغط النموذج), pipeline parallelism (التوازي الأنبوبي), expressive power (قدرة على التعبير), hand-craft (صياغة يدوياً)
- **Equations:** None
- **Citations:** Extensive references to prior work in three subsections
- **Special handling:** Organized into three subsections (ConvNet Accuracy, ConvNet Efficiency, Model Scaling)

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
