# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** convolutional neural networks, accuracy, efficiency, model scaling, architecture, depth, width, resolution, neural architecture search, baseline, parameters, computational cost

---

### English Version

Scaling up ConvNets is widely used to achieve better accuracy. For example, ResNet can be scaled up from ResNet-18 to ResNet-200 by using more layers; Recently, GPipe achieved 84.3% ImageNet top-1 accuracy by scaling up a baseline model four times larger. However, the process of scaling up ConvNets has never been well understood and there are currently many ways to do it. The most common way is to scale up ConvNets by their depth or width. Another less common, but increasingly popular, method is to scale up models by image resolution. In previous work, it is common to scale only one of the three dimensions – depth, width, and resolution. Though it is possible to scale two or three dimensions arbitrarily, arbitrary scaling requires tedious manual tuning and still often yields sub-optimal accuracy and efficiency.

In this paper, we want to study and rethink the process of scaling up ConvNets. In particular, we investigate the central question: is there a principled method to scale up ConvNets that can achieve better accuracy and efficiency? Our empirical study shows that it is critical to balance all dimensions of network width/depth/resolution, and surprisingly such balance can be achieved by simply scaling each of them with constant ratio. Based on this observation, we propose a simple yet effective compound scaling method. Unlike conventional practice that arbitrary scales these factors, our method uniformly scales network width, depth, and resolution with a set of fixed scaling coefficients. For example, if we want to use 2^N times more computational resources, then we can simply increase the network depth by α^N, width by β^N, and image size by γ^N, where α, β, γ are constant coefficients determined by a small grid search on the original small model. Figure 1 illustrates the difference between our scaling method and conventional methods.

Intuitively, the compound scaling method makes sense because if the input image is bigger, then the network needs more layers to increase the receptive field and more channels to capture more fine-grained patterns on the bigger image. In fact, previous theoretical and empirical results both show that there is a certain relationship between network width and depth, but to our best knowledge, we are the first to empirically quantify the relationship among all three dimensions of network width, depth, and resolution.

We demonstrate that our scaling method works well on existing MobileNets and ResNet. Notably, the effectiveness of model scaling heavily depends on the baseline network; to go even further, we use neural architecture search to develop a new baseline network, and scale it up to obtain a family of models, called EfficientNets. Figure 2 summarizes the ImageNet performance, where our EfficientNets significantly outperform other ConvNets. In particular, our EfficientNet-B7 surpasses the best existing GPipe accuracy, but using 8.4x fewer parameters and running 6.1x faster on inference. Compared to the widely used ResNet-50, our EfficientNet-B4 improves the top-1 accuracy from 76.3% to 83.0% (+6.7%) with similar FLOPS. Besides ImageNet, EfficientNets also transfer well and achieve state-of-the-art accuracy on 5 out of 8 widely used datasets, while reducing parameters by up to 21x than existing ConvNets.

---

### النسخة العربية

يُستخدم توسيع الشبكات الالتفافية (ConvNets) على نطاق واسع لتحقيق دقة أفضل. على سبيل المثال، يمكن توسيع ResNet من ResNet-18 إلى ResNet-200 باستخدام المزيد من الطبقات؛ مؤخراً، حقق GPipe دقة 84.3% في أفضل 1 على ImageNet من خلال توسيع نموذج خط الأساس بمقدار أربعة أضعاف حجمه. ومع ذلك، لم تتم دراسة عملية توسيع الشبكات الالتفافية بشكل جيد أبداً وتوجد حالياً العديد من الطرق للقيام بذلك. الطريقة الأكثر شيوعاً هي توسيع الشبكات الالتفافية من خلال عمقها أو عرضها. هناك طريقة أخرى أقل شيوعاً، لكنها تزداد شعبية، وهي توسيع النماذج من خلال دقة وضوح الصورة. في الأعمال السابقة، من الشائع توسيع بُعد واحد فقط من الأبعاد الثلاثة - العمق والعرض ودقة الوضوح. على الرغم من أنه من الممكن توسيع بُعدين أو ثلاثة أبعاد بشكل تعسفي، إلا أن التوسيع التعسفي يتطلب ضبطاً يدوياً مملاً وغالباً ما يؤدي إلى دقة وكفاءة دون المستوى الأمثل.

في هذه الورقة، نريد دراسة وإعادة التفكير في عملية توسيع الشبكات الالتفافية. على وجه الخصوص، نحقق في السؤال المحوري: هل توجد طريقة منهجية لتوسيع الشبكات الالتفافية يمكن أن تحقق دقة وكفاءة أفضل؟ تُظهر دراستنا التجريبية أنه من الأهمية بمكان موازنة جميع أبعاد عرض الشبكة وعمقها ودقة وضوحها، ومن المدهش أن هذا التوازن يمكن تحقيقه ببساطة عن طريق توسيع كل منها بنسبة ثابتة. بناءً على هذه الملاحظة، نقترح طريقة توسيع مركبة بسيطة لكنها فعالة. على عكس الممارسة التقليدية التي توسع هذه العوامل بشكل تعسفي، فإن طريقتنا توسع عرض الشبكة وعمقها ودقة وضوحها بشكل موحد باستخدام مجموعة من معاملات التوسيع الثابتة. على سبيل المثال، إذا أردنا استخدام موارد حسابية أكثر بمقدار 2^N مرة، فيمكننا ببساطة زيادة عمق الشبكة بمقدار α^N، والعرض بمقدار β^N، وحجم الصورة بمقدار γ^N، حيث α وβ وγ معاملات ثابتة يتم تحديدها من خلال بحث شبكي صغير على النموذج الصغير الأصلي. يوضح الشكل 1 الفرق بين طريقة التوسيع الخاصة بنا والطرق التقليدية.

بشكل بديهي، فإن طريقة التوسيع المركب منطقية لأنه إذا كانت صورة الإدخال أكبر، فإن الشبكة تحتاج إلى المزيد من الطبقات لزيادة الحقل الاستقبالي والمزيد من القنوات لالتقاط أنماط أكثر دقة على الصورة الأكبر. في الواقع، تُظهر النتائج النظرية والتجريبية السابقة وجود علاقة معينة بين عرض الشبكة وعمقها، ولكن على حد علمنا، نحن الأوائل في قياس العلاقة تجريبياً بين جميع الأبعاد الثلاثة لعرض الشبكة وعمقها ودقة وضوحها.

نوضح أن طريقة التوسيع الخاصة بنا تعمل بشكل جيد على MobileNets وResNet الموجودة. والجدير بالذكر أن فعالية توسيع النموذج تعتمد بشكل كبير على شبكة خط الأساس؛ للذهاب أبعد من ذلك، نستخدم البحث عن معمارية عصبية لتطوير شبكة خط أساس جديدة، ونوسعها للحصول على عائلة من النماذج، تسمى EfficientNets. يلخص الشكل 2 أداء ImageNet، حيث تتفوق EfficientNets بشكل كبير على الشبكات الالتفافية الأخرى. على وجه الخصوص، يتجاوز EfficientNet-B7 أفضل دقة لـ GPipe الموجودة، ولكن باستخدام معاملات أقل بمقدار 8.4 مرة ويعمل أسرع بمقدار 6.1 مرة في الاستنتاج. بالمقارنة مع ResNet-50 المستخدم على نطاق واسع، يحسن EfficientNet-B4 دقة أفضل 1 من 76.3% إلى 83.0% (+6.7%) مع FLOPS مماثلة. إلى جانب ImageNet، تنتقل EfficientNets أيضاً بشكل جيد وتحقق دقة متقدمة على 5 من أصل 8 مجموعات بيانات مستخدمة على نطاق واسع، مع تقليل المعاملات بما يصل إلى 21 مرة مقارنة بالشبكات الالتفافية الموجودة.

---

### Translation Notes

- **Figures referenced:** Figure 1 (scaling method comparison), Figure 2 (ImageNet performance)
- **Key terms introduced:** Compound scaling, receptive field, grid search, FLOPS
- **Equations:** Mathematical notation for scaling (2^N, α^N, β^N, γ^N)
- **Citations:** References to ResNet, GPipe, MobileNets
- **Special handling:** Model names and technical acronyms kept in English

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88

### Back-Translation (Key Paragraph)

"In this paper, we want to study and rethink the process of scaling up convolutional networks. Specifically, we investigate the central question: is there a systematic method to scale up convolutional networks that can achieve better accuracy and efficiency? Our empirical study shows that it is critically important to balance all dimensions of network width, depth, and resolution, and surprisingly this balance can be achieved simply by scaling each of them with a constant ratio."
