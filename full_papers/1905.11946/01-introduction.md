# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** scaling, ConvNets, accuracy, depth, width, resolution, compound scaling, baseline, neural architecture search, efficiency, state-of-the-art, inference, parameters, FLOPS

---

### English Version

Scaling up ConvNets is widely used to achieve better accuracy. For example, ResNet (He et al., 2016) can be scaled up from ResNet-18 to ResNet-200 by using more layers; Recently, GPipe (Huang et al., 2018) achieved 84.3% ImageNet top-1 accuracy by scaling up a baseline model four time larger. However, the process of scaling up ConvNets has never been well understood and there are currently many ways to do it. The most common way is to scale up ConvNets by their depth (He et al., 2016) or width (Zagoruyko & Komodakis, 2016). Another less common, but increasingly popular, method is to scale up models by image resolution (Huang et al., 2018). In previous work, it is common to scale only one of the three dimensions – depth, width, and image size. Though it is possible to scale two or three dimensions arbitrarily, arbitrary scaling requires tedious manual tuning and still often yields sub-optimal accuracy and efficiency.

In this paper, we want to study and rethink the process of scaling up ConvNets. In particular, we investigate the central question: is there a principled method to scale up ConvNets that can achieve better accuracy and efficiency? Our empirical study shows that it is critical to balance all dimensions of network width/depth/resolution, and surprisingly such balance can be achieved by simply scaling each of them with constant ratio. Based on this observation, we propose a simple yet effective compound scaling method. Unlike conventional practice that arbitrary scales these factors, our method uniformly scales network width, depth, and resolution with a set of fixed scaling coefficients. For example, if we want to use 2^N times more computational resources, then we can simply increase the network depth by α^N, width by β^N, and image size by γ^N, where α, β, γ are constant coefficients determined by a small grid search on the original small model. Figure 2 illustrates the difference between our scaling method and conventional methods.

Intuitively, the compound scaling method makes sense because if the input image is bigger, then the network needs more layers to increase the receptive field and more channels to capture more fine-grained patterns on the bigger image. In fact, previous theoretical (Raghu et al., 2017; Lu et al., 2018) and empirical results (Zagoruyko & Komodakis, 2016) both show that there exists certain relationship between network width and depth, but to our best knowledge, we are the first to empirically quantify the relationship among all three dimensions of network width, depth, and resolution.

We demonstrate that our scaling method work well on existing MobileNets (Howard et al., 2017; Sandler et al., 2018) and ResNet (He et al., 2016). Notably, the effectiveness of model scaling heavily depends on the baseline network; to go even further, we use neural architecture search (Zoph & Le, 2017; Tan et al., 2019) to develop a new baseline network, and scale it up to obtain a family of models, called EfficientNets. Figure 1 summarizes the ImageNet performance, where our EfficientNets significantly outperform other ConvNets. In particular, our EfficientNet-B7 surpasses the best existing GPipe accuracy (Huang et al., 2018), but using 8.4x fewer parameters and running 6.1x faster on inference. Compared to the widely used ResNet-50 (He et al., 2016), our EfficientNet-B4 improves the top-1 accuracy from 76.3% to 83.0% (+6.7%) with similar FLOPS. Besides ImageNet, EfficientNets also transfer well and achieve state-of-the-art accuracy on 5 out of 8 widely used datasets, while reducing parameters by up to 21x than existing ConvNets.

---

### النسخة العربية

يُستخدم توسيع الشبكات الالتفافية (ConvNets) على نطاق واسع لتحقيق دقة أفضل. على سبيل المثال، يمكن توسيع ResNet (He et al., 2016) من ResNet-18 إلى ResNet-200 باستخدام المزيد من الطبقات؛ في الآونة الأخيرة، حقق GPipe (Huang et al., 2018) دقة 84.3% في أفضل 1 على ImageNet من خلال توسيع نموذج خط أساس بمقدار أربعة أضعاف. ومع ذلك، لم تتم دراسة عملية توسيع الشبكات الالتفافية بشكل جيد أبداً وهناك حالياً العديد من الطرق للقيام بذلك. الطريقة الأكثر شيوعاً هي توسيع الشبكات الالتفافية من حيث العمق (He et al., 2016) أو العرض (Zagoruyko & Komodakis, 2016). هناك طريقة أخرى أقل شيوعاً، لكنها تزداد شعبية، وهي توسيع النماذج من خلال دقة وضوح الصورة (Huang et al., 2018). في الأعمال السابقة، من الشائع توسيع بُعد واحد فقط من الأبعاد الثلاثة - العمق، أو العرض، أو حجم الصورة. على الرغم من أنه من الممكن توسيع بُعدين أو ثلاثة أبعاد بشكل تعسفي، إلا أن التوسيع التعسفي يتطلب ضبطاً يدوياً مُرهقاً ولا يزال غالباً ما ينتج عنه دقة وكفاءة دون المستوى الأمثل.

في هذه الورقة، نريد دراسة وإعادة التفكير في عملية توسيع الشبكات الالتفافية. على وجه الخصوص، نبحث في السؤال المركزي: هل توجد طريقة منهجية لتوسيع الشبكات الالتفافية يمكن أن تحقق دقة وكفاءة أفضل؟ تُظهر دراستنا التجريبية أنه من الضروري موازنة جميع أبعاد عرض/عمق/دقة وضوح الشبكة، ومن المفاجئ أن هذا التوازن يمكن تحقيقه ببساطة من خلال توسيع كل منها بنسبة ثابتة. بناءً على هذه الملاحظة، نقترح طريقة توسيع مركب بسيطة لكنها فعالة. على عكس الممارسة التقليدية التي توسع هذه العوامل بشكل تعسفي، فإن طريقتنا توسع عرض الشبكة وعمقها ودقة الوضوح بشكل موحد بمجموعة من معاملات التوسيع الثابتة. على سبيل المثال، إذا أردنا استخدام 2^N أضعاف الموارد الحسابية، فيمكننا ببساطة زيادة عمق الشبكة بمقدار α^N، والعرض بمقدار β^N، وحجم الصورة بمقدار γ^N، حيث α وβ وγ هي معاملات ثابتة يتم تحديدها من خلال بحث شبكي صغير على النموذج الصغير الأصلي. يوضح الشكل 2 الفرق بين طريقة التوسيع الخاصة بنا والطرق التقليدية.

بشكل بديهي، طريقة التوسيع المركب منطقية لأنه إذا كانت الصورة المُدخلة أكبر، فإن الشبكة تحتاج إلى المزيد من الطبقات لزيادة مجال الاستقبال والمزيد من القنوات لالتقاط أنماط أكثر دقة على الصورة الأكبر. في الواقع، تُظهر كل من النتائج النظرية السابقة (Raghu et al., 2017; Lu et al., 2018) والنتائج التجريبية (Zagoruyko & Komodakis, 2016) أن هناك علاقة معينة بين عرض الشبكة وعمقها، ولكن على حد علمنا، نحن الأوائل الذين يقيسون تجريبياً العلاقة بين جميع الأبعاد الثلاثة لعرض الشبكة وعمقها ودقة الوضوح.

نوضح أن طريقة التوسيع الخاصة بنا تعمل بشكل جيد على MobileNets الموجودة (Howard et al., 2017; Sandler et al., 2018) وResNet (He et al., 2016). والجدير بالذكر أن فعالية توسيع النموذج تعتمد بشكل كبير على شبكة خط الأساس؛ للذهاب أبعد من ذلك، نستخدم البحث عن معمارية عصبية (Zoph & Le, 2017; Tan et al., 2019) لتطوير شبكة خط أساس جديدة، وتوسيعها للحصول على عائلة من النماذج، تسمى EfficientNets. يلخص الشكل 1 أداء ImageNet، حيث تتفوق EfficientNets الخاصة بنا بشكل كبير على الشبكات الالتفافية الأخرى. على وجه الخصوص، يتجاوز EfficientNet-B7 الخاص بنا أفضل دقة GPipe الموجودة (Huang et al., 2018)، لكن باستخدام معاملات أقل بمقدار 8.4 مرة وعمل أسرع بمقدار 6.1 مرة في الاستنتاج. بالمقارنة مع ResNet-50 المُستخدم على نطاق واسع (He et al., 2016)، يحسن EfficientNet-B4 الخاص بنا دقة أفضل 1 من 76.3% إلى 83.0% (+6.7%) مع FLOPS مماثلة. إلى جانب ImageNet، تنتقل EfficientNets أيضاً بشكل جيد وتحقق دقة متقدمة على 5 من أصل 8 مجموعات بيانات مستخدمة على نطاق واسع، بينما تقلل المعاملات بما يصل إلى 21 مرة من الشبكات الالتفافية الموجودة.

---

### Translation Notes

- **Figures referenced:** Figure 1, Figure 2
- **Key terms introduced:** compound scaling method (طريقة التوسيع المركب), receptive field (مجال الاستقبال), grid search (بحث شبكي), scaling coefficients (معاملات التوسيع)
- **Equations:** Mathematical notation for scaling (2^N, α^N, β^N, γ^N)
- **Citations:** Multiple references to prior work (ResNet, GPipe, MobileNets)
- **Special handling:** Kept model names in English; preserved mathematical notation

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
