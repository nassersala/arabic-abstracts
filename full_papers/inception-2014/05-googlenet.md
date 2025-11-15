# Section 5: GoogLeNet
## القسم 5: GoogLeNet

**Section:** GoogLeNet
**Translation Quality:** 0.87
**Glossary Terms Used:** architecture, convolution, pooling, inception module, classifier, auxiliary classifier, regularization, gradient, overfitting, average pooling

---

### English Version

By "GoogLeNet" we denote a particular incarnation of the Inception architecture used in our submission for ILSVRC14. We also used one additional modification to the network motivated by computer memory considerations – the beneficial effect of which turned out to be marginal. The details of the architecture are summarized in Table 1.

All the convolutions, including those inside the Inception modules, use rectified linear activation. The size of the receptive field in our network is 224×224 taking RGB color channels with mean subtraction. "#3×3 reduce" and "#5×5 reduce" stands for the number of 1×1 filters in the reduction layer used before the 3×3 and 5×5 convolutions. One can see the number of 1×1 filters in the projection layer after the built-in max-pooling in the pool proj column. All these reduction/projection layers use rectified linear activation as well.

The network was designed with computational efficiency and practicality in mind, so that inference can be run on individual devices including even those with limited computational resources, especially with low-memory footprint. The network is 22 layers deep when counting only layers with parameters (or 27 layers if we also count pooling). The overall number of layers (independent building blocks) used for the construction of the network is about 100. The exact number depends on the machine learning infrastructure system used. The use of average pooling before the classifier is based on [12], although our implementation differs in that we use an extra linear layer. This enables adapting and fine-tuning our networks for other label sets easily, but it is mostly convenience and we don't expect it to have a major effect. It was found that a move from fully connected layers to average pooling improved the top-1 accuracy by about 0.6%, however the use of dropout remained essential even after removing the fully connected layers.

Given the relatively large depth of the network, the ability to propagate gradients back through all the layers in an effective manner was a concern. One interesting insight is that the strong performance of relatively shallower networks on this task suggests that the features produced by the layers in the middle of the network should be very discriminative. By adding auxiliary classifiers connected to these intermediate layers, we would expect to encourage discrimination in the lower stages in the classifier, increase the gradient signal that gets propagated back, and provide additional regularization. These classifiers take the form of smaller convolutional networks put on top of the output of the Inception (4a) and (4d) modules. During training, their loss gets added to the total loss of the network with a discount weight (the losses of the auxiliary classifiers were weighted by 0.3). At inference time, these auxiliary networks are discarded.

The exact structure of the extra network on the side, including the auxiliary classifier, is as follows:
- An average pooling layer with 5×5 filter size and stride 3, resulting in an 4×4×512 output for the (4a), and 4×4×528 for the (4d) stage.
- A 1×1 convolution with 128 filters for dimension reduction and rectified linear activation.
- A fully connected layer with 1024 units and rectified linear activation.
- A dropout layer with 70% ratio of dropped outputs.
- A linear layer with softmax loss as the classifier (predicting the same 1000 classes as the main classifier, but removed at inference time).

A schematic depiction of the resulting network is in Figure 3. We refer interested parties to the supplementary material or [18] for the actual code that produces our described architecture.

---

### النسخة العربية

بـ "GoogLeNet" نشير إلى تجسيد معين لمعمارية Inception المستخدمة في تقديمنا لـ ILSVRC14. استخدمنا أيضاً تعديلاً إضافياً واحداً على الشبكة مدفوعاً باعتبارات ذاكرة الحاسوب - واتضح أن التأثير المفيد كان هامشياً. تفاصيل المعمارية ملخصة في الجدول 1.

تستخدم جميع الالتفافات، بما في ذلك تلك الموجودة داخل وحدات Inception، التنشيط الخطي المقوّم. حجم مجال الاستقبال في شبكتنا هو 224×224 مع أخذ قنوات ألوان RGB مع طرح المتوسط. "#3×3 reduce" و"#5×5 reduce" يمثلان عدد المرشحات 1×1 في طبقة التخفيض المستخدمة قبل الالتفافات 3×3 و5×5. يمكن للمرء رؤية عدد المرشحات 1×1 في طبقة الإسقاط بعد التجميع الأقصى المدمج في عمود pool proj. تستخدم جميع طبقات التخفيض/الإسقاط هذه التنشيط الخطي المقوّم أيضاً.

تم تصميم الشبكة مع الكفاءة الحسابية والعملية في الاعتبار، بحيث يمكن تشغيل الاستدلال على الأجهزة الفردية بما في ذلك حتى تلك ذات الموارد الحسابية المحدودة، خاصة مع بصمة ذاكرة منخفضة. الشبكة بعمق 22 طبقة عند حساب الطبقات ذات المعاملات فقط (أو 27 طبقة إذا قمنا أيضاً بحساب التجميع). العدد الإجمالي للطبقات (الكتل البنائية المستقلة) المستخدمة لبناء الشبكة حوالي 100. يعتمد العدد الدقيق على نظام البنية التحتية للتعلم الآلي المستخدم. يستند استخدام التجميع المتوسط قبل المصنف إلى [12]، على الرغم من أن تطبيقنا يختلف في أننا نستخدم طبقة خطية إضافية. هذا يتيح تكييف وضبط شبكاتنا بشكل دقيق لمجموعات تسميات أخرى بسهولة، لكنه في الغالب للراحة ولا نتوقع أن يكون له تأثير كبير. تبين أن الانتقال من الطبقات المتصلة بالكامل إلى التجميع المتوسط حسّن دقة top-1 بحوالي 0.6٪، ومع ذلك ظل استخدام dropout ضرورياً حتى بعد إزالة الطبقات المتصلة بالكامل.

نظراً للعمق الكبير نسبياً للشبكة، كانت القدرة على نشر التدرجات للخلف عبر جميع الطبقات بطريقة فعالة مصدر قلق. أحد الرؤى المثيرة للاهتمام هو أن الأداء القوي للشبكات الضحلة نسبياً في هذه المهمة يشير إلى أن الميزات التي تنتجها الطبقات في منتصف الشبكة يجب أن تكون تمييزية للغاية. من خلال إضافة مصنفات مساعدة متصلة بهذه الطبقات الوسيطة، نتوقع تشجيع التمييز في المراحل السفلية في المصنف، وزيادة إشارة التدرج التي تنتشر للخلف، وتوفير تنظيم إضافي. تتخذ هذه المصنفات شكل شبكات التفافية أصغر موضوعة فوق مخرجات وحدتي Inception (4a) و(4d). أثناء التدريب، يتم إضافة خسارتها إلى الخسارة الإجمالية للشبكة بوزن خصم (تم ترجيح خسائر المصنفات المساعدة بـ 0.3). في وقت الاستدلال، يتم تجاهل هذه الشبكات المساعدة.

البنية الدقيقة للشبكة الإضافية على الجانب، بما في ذلك المصنف المساعد، هي كما يلي:
- طبقة تجميع متوسط بحجم مرشح 5×5 وخطوة 3، مما ينتج عنه مخرجات 4×4×512 للمرحلة (4a)، و4×4×528 للمرحلة (4d).
- التفاف 1×1 بـ 128 مرشح لتخفيض الأبعاد والتنشيط الخطي المقوّم.
- طبقة متصلة بالكامل بـ 1024 وحدة والتنشيط الخطي المقوّم.
- طبقة dropout بنسبة 70٪ من المخرجات المُسقَطة.
- طبقة خطية مع خسارة softmax كمصنف (تتنبأ بنفس الفئات الـ 1000 مثل المصنف الرئيسي، ولكن تُزال في وقت الاستدلال).

الوصف التخطيطي للشبكة الناتجة موجود في الشكل 3. نحيل الأطراف المهتمة إلى المادة التكميلية أو [18] للحصول على الشفرة الفعلية التي تنتج المعمارية الموصوفة لدينا.

---

### Translation Notes

- **Figures referenced:** Figure 3
- **Tables referenced:** Table 1
- **Key terms introduced:** auxiliary classifier, receptive field, RGB channels, mean subtraction, softmax, inference, gradient propagation, discriminative features
- **Equations:** None
- **Citations:** [12], [18]
- **Special handling:**
  - Kept "GoogLeNet" as proper noun
  - Kept "dropout" and "softmax" as transliterated/English terms (standard in ML)
  - Translated "receptive field" as "مجال الاستقبال"
  - Kept mathematical dimensions like "224×224", "4×4×512" unchanged
  - Translated "auxiliary classifier" as "مصنف مساعد"
  - Kept "top-1 accuracy" with the English term
  - Translated "gradient propagation" as "نشر التدرجات"
  - Translated "discriminative" as "تمييزية"
  - Kept technical column names like "pool proj" in English
  - Translated "inference time" as "وقت الاستدلال"

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
