# Section 2: Related Work
## القسم 2: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.86
**Glossary Terms Used:** architecture, efficient model design, group convolution, channel shuffle, model acceleration, pruning, compression, quantization, knowledge distillation, neural architecture search

---

### English Version

**Efficient Model Designs.** The last few years have seen the success of deep neural networks in computer vision tasks [17, 28, 33], in which model designs play an important role. The recent trend in designing high-quality architectures leans toward increasing depth and width, such as GoogleNet [33], VGGNet [29], ResNet [8, 9], and more recently DenseNet [11] and ResNeXt [40]. There are some works that focus on efficient model designs, such as GoogLeNet [33] that employs the inception module to reduce the number of parameters, SqueezeNet [15] that uses bottleneck approach to design a very compact architecture achieving AlexNet level accuracy (~57.5% top-1 error) with 1.25M parameters, ResNet [8] that uses a stack of simple bottleneck modules to achieve remarkable results, and more recently SENet [10] that adds channel-wise attention layers to improve performance with modest computation cost. However, all these works are not specifically designed for running on mobile platforms or with very small complexity constraints.

**Group Convolution.** The concept of group convolution, which was first introduced in AlexNet [17] for distributing the model over two GPUs, has been well demonstrated its effectiveness in ResNeXt [40]. Depthwise separable convolution proposed in Xception [3] generalizes the ideas of separable convolutions in Inception series [34, 33]. Recently, MobileNet [12] utilizes the depthwise separable convolutions and gains state-of-the-art results among lightweight deep models. Our work generalizes group convolution and depthwise separable convolution in a novel way.

**Channel Shuffle Operation.** To the best of our knowledge, the idea of channel shuffle operation has been rarely discussed in previous works on efficient model design. In cuda-convnet [18], a "random sparse convolution" layer is supported, which is equivalent to random channel shuffle followed by a group convolution layer. Such "random shuffle" operation has different purpose and been rarely exploited later. Very recently, another concurrent work [41] also adopts this idea for a two-stage convolution. However, [41] did not specially investigate the effectiveness of channel shuffle itself and its usage in tiny model design which is our focus.

**Model Acceleration.** This direction aims to accelerate inference while preserving pre-trained models without modifying them. Pruning network connections [5, 6] or channels [38] reduces redundant connections in a pre-trained model while maintaining performance. Quantization [31, 37, 42] and factorization [19, 20, 16, 22] are proposed in literature to reduce redundancy in calculations to speed up inference. Without modifying the parameters, optimized convolution algorithms implemented via FFT [24, 26] and other methods [2] decrease time consumption in practice. Distilling [7] transfers knowledge from large models into small ones, which makes training small networks easier.

---

### النسخة العربية

**تصميمات النماذج الفعالة.** شهدت السنوات القليلة الماضية نجاح الشبكات العصبية العميقة في مهام الرؤية الحاسوبية [17, 28, 33]، حيث تلعب تصميمات النماذج دوراً مهماً. يميل الاتجاه الحديث في تصميم معماريات عالية الجودة نحو زيادة العمق والعرض، مثل GoogleNet [33] و VGGNet [29] و ResNet [8, 9]، وفي الآونة الأخيرة DenseNet [11] و ResNeXt [40]. هناك بعض الأعمال التي تركز على تصميمات النماذج الفعالة، مثل GoogLeNet [33] التي توظف وحدة الاستهلال (inception module) لتقليل عدد المعاملات، وSqueezeNet [15] التي تستخدم نهج عنق الزجاجة لتصميم معمارية مدمجة جداً تحقق دقة مستوى AlexNet (~57.5% خطأ top-1) بمعاملات قدرها 1.25 مليون، وResNet [8] التي تستخدم مكدساً من وحدات عنق الزجاجة البسيطة لتحقيق نتائج رائعة، وفي الآونة الأخيرة SENet [10] التي تضيف طبقات انتباه على مستوى القنوات لتحسين الأداء بتكلفة حسابية متواضعة. ومع ذلك، جميع هذه الأعمال ليست مصممة خصيصاً للعمل على المنصات المحمولة أو مع قيود تعقيد صغيرة جداً.

**الالتفاف المجموعي.** تم توضيح فعالية مفهوم الالتفاف المجموعي، الذي تم تقديمه لأول مرة في AlexNet [17] لتوزيع النموذج على وحدتي معالجة رسومات، بشكل جيد في ResNeXt [40]. يعمم الالتفاف الفصلي العميق (depthwise separable convolution) المقترح في Xception [3] أفكار الالتفافات القابلة للفصل في سلسلة Inception [34, 33]. مؤخراً، تستخدم MobileNet [12] الالتفافات الفصلية العميقة وتحقق نتائج حديثة بين النماذج العميقة خفيفة الوزن. يعمم عملنا الالتفاف المجموعي والالتفاف الفصلي العميق بطريقة جديدة.

**عملية خلط القنوات.** على حد علمنا، نادراً ما تمت مناقشة فكرة عملية خلط القنوات في الأعمال السابقة حول تصميم النماذج الفعالة. في cuda-convnet [18]، يتم دعم طبقة "الالتفاف المتفرق العشوائي" (random sparse convolution)، والتي تعادل خلط القنوات العشوائي يليها طبقة التفاف مجموعي. مثل هذه العملية "الخلط العشوائي" لها غرض مختلف ونادراً ما تم استغلالها لاحقاً. في الآونة الأخيرة جداً، يتبنى عمل متزامن آخر [41] هذه الفكرة أيضاً للالتفاف ذي المرحلتين. ومع ذلك، لم يدرس [41] على وجه التحديد فعالية خلط القنوات نفسها واستخدامها في تصميم النماذج الصغيرة وهو محور تركيزنا.

**تسريع النماذج.** يهدف هذا الاتجاه إلى تسريع الاستدلال مع الحفاظ على النماذج المدربة مسبقاً دون تعديلها. يقلل تقليم اتصالات الشبكة [5, 6] أو القنوات [38] من الاتصالات الزائدة في نموذج مدرب مسبقاً مع الحفاظ على الأداء. تم اقتراح التكميم [31, 37, 42] والتحليل إلى عوامل [19, 20, 16, 22] في الأدبيات لتقليل التكرار في الحسابات لتسريع الاستدلال. دون تعديل المعاملات، تقلل خوارزميات الالتفاف المحسنة المنفذة عبر FFT [24, 26] وطرق أخرى [2] من استهلاك الوقت في الممارسة العملية. ينقل التقطير [7] المعرفة من النماذج الكبيرة إلى الصغيرة، مما يجعل تدريب الشبكات الصغيرة أسهل.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Efficient model design (تصميمات النماذج الفعالة)
  - Inception module (وحدة الاستهلال)
  - Bottleneck approach (نهج عنق الزجاجة)
  - Channel-wise attention (انتباه على مستوى القنوات)
  - Group convolution (الالتفاف المجموعي)
  - Depthwise separable convolution (الالتفاف الفصلي العميق)
  - Channel shuffle (خلط القنوات)
  - Pruning (تقليم)
  - Quantization (تكميم)
  - Factorization (تحليل إلى عوامل)
  - Knowledge distilling (تقطير المعرفة)

- **Equations:** 0
- **Citations:** Multiple references throughout [17, 28, 33, 29, 8, 9, 11, 40, 15, 10, 3, 34, 12, 18, 41, 5, 6, 38, 31, 37, 42, 19, 20, 16, 22, 24, 26, 2, 7]
- **Special handling:**
  - Kept architecture names in English (GoogleNet, VGGNet, ResNet, DenseNet, ResNeXt, GoogLeNet, SqueezeNet, AlexNet, SENet, Xception, MobileNet)
  - Translated technical concepts while maintaining precision
  - Preserved subsection headers with bold formatting

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.84
- Glossary consistency: 0.86
- **Overall section score:** 0.86

### Back-translation Check (Key Sentence)

Arabic: "يعمم عملنا الالتفاف المجموعي والالتفاف الفصلي العميق بطريقة جديدة"
Back to English: "Our work generalizes group convolution and depthwise separable convolution in a novel way"
✓ Semantically equivalent to original
