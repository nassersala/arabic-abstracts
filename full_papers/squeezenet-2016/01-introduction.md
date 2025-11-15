# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** deep neural networks (الشبكات العصبية العميقة), convolutional neural networks (الشبكات العصبية الالتفافية), accuracy (دقة), model compression (ضغط النموذج), distributed training (تدريب موزع), autonomous vehicle (مركبة ذاتية القيادة), FPGA (مصفوفات البوابات القابلة للبرمجة), bandwidth (نطاق ترددي), architecture (معمارية), parameters (معاملات)

---

### English Version

Much of the recent research on deep convolutional neural networks (CNNs) has focused on increasing accuracy on computer vision datasets. For a given accuracy level, there typically exist multiple CNN architectures that achieve that accuracy level. Given equivalent accuracy, a CNN architecture with fewer parameters has several advantages:

**More efficient distributed training.** Communication among servers is the limiting factor to the scalability of distributed DNN training. For distributed data-parallel training, communication overhead is directly proportional to the number of parameters in the model. In short, small models train faster due to requiring less communication.

**Less overhead when exporting new models to clients.** For autonomous driving, companies such as Tesla periodically copy new models from their servers to customers' cars. This practice is often referred to as an over-the-air update. Consumer Reports has found that a Tesla Model S can consume almost 4GB of cellular data per month for model and map updates. Smaller models require less communication, making frequent updates more feasible.

**Feasible FPGA and embedded deployment.** FPGAs often have less than 10MB of on-chip memory and no off-chip memory or storage. For inference, a sufficiently small model could be stored directly on the FPGA instead of being bottlenecked by memory bandwidth, while video frames stream through the FPGA in real time. Further, when deploying DNNs on Application-Specific Integrated Circuits (ASICs), a sufficiently small model could be stored directly on-chip, and smaller models may enable the ASIC to fit on a smaller die.

As you can see, there are several advantages of smaller CNN architectures. With this in mind, we focus directly on the problem of identifying a CNN architecture with fewer parameters but equivalent accuracy compared to a well-known model. We have discovered such an architecture, which we call SqueezeNet. In addition, we present our analysis of design strategies that led to the development of SqueezeNet.

The rest of the paper is organized as follows. In Section 2, we review the related work. Then, in Sections 3 and 4, we describe and evaluate the SqueezeNet architecture. After that, we turn our attention to understanding how CNN architectural design choices impact model size and accuracy. We organize our discussion into three topics: CNN microarchitecture (per-layer architectural decisions), CNN macroarchitecture (high-level organization of layers), and the effect of model compression. In Section 5, we do a design space exploration of SqueezeNet microarchitecture design decisions, such as the size and quantity of filters per layer. In Section 6, we evaluate the impact of CNN macroarchitecture, as applied to SqueezeNet; in particular, we explore the effect of modules inspired by the Residual Network (ResNet) architecture. Finally, in Section 7, we conclude with key insights and directions for future work.

---

### النسخة العربية

ركز جزء كبير من الأبحاث الحديثة حول الشبكات العصبية الالتفافية العميقة على زيادة الدقة في مجموعات بيانات الرؤية الحاسوبية. ولمستوى دقة معين، توجد عادةً معماريات متعددة للشبكات العصبية الالتفافية تحقق ذلك المستوى من الدقة. ومع تساوي الدقة، فإن معمارية الشبكة العصبية الالتفافية ذات المعاملات الأقل لها العديد من المزايا:

**تدريب موزع أكثر كفاءة.** يعد الاتصال بين الخوادم العامل المحدد لقابلية التوسع في تدريب الشبكات العصبية العميقة الموزعة. بالنسبة للتدريب الموزع المتوازي للبيانات، يكون عبء الاتصال متناسباً بشكل مباشر مع عدد المعاملات في النموذج. باختصار، النماذج الصغيرة تتدرب بشكل أسرع نظراً لاحتياجها إلى اتصال أقل.

**عبء أقل عند تصدير النماذج الجديدة إلى العملاء.** في مجال القيادة الذاتية، تقوم شركات مثل Tesla بشكل دوري بنسخ النماذج الجديدة من خوادمها إلى سيارات العملاء. يشار إلى هذه الممارسة غالباً بالتحديث عبر الهواء. وجدت مجلة Consumer Reports أن سيارة Tesla Model S يمكن أن تستهلك ما يقارب 4 جيجابايت من البيانات الخلوية شهرياً لتحديثات النماذج والخرائط. النماذج الأصغر حجماً تتطلب اتصالاً أقل، مما يجعل التحديثات المتكررة أكثر قابلية للتطبيق.

**نشر قابل للتطبيق على مصفوفات البوابات القابلة للبرمجة والأنظمة المدمجة.** غالباً ما تحتوي مصفوفات البوابات القابلة للبرمجة على أقل من 10 ميجابايت من الذاكرة على الشريحة وبدون ذاكرة أو تخزين خارج الشريحة. للاستدلال، يمكن تخزين نموذج صغير بما فيه الكفاية مباشرة على مصفوفة البوابات القابلة للبرمجة بدلاً من أن تصبح عنق الزجاجة بسبب نطاق ترددي الذاكرة، بينما تتدفق إطارات الفيديو عبر مصفوفة البوابات القابلة للبرمجة في الوقت الفعلي. علاوة على ذلك، عند نشر الشبكات العصبية العميقة على الدوائر المتكاملة الخاصة بالتطبيقات (ASICs)، يمكن تخزين نموذج صغير بما فيه الكفاية مباشرة على الشريحة، وقد تمكّن النماذج الأصغر حجماً الدائرة المتكاملة الخاصة بالتطبيقات من الاحتواء على شريحة أصغر.

كما ترون، هناك العديد من المزايا لمعماريات الشبكات العصبية الالتفافية الأصغر حجماً. مع وضع ذلك في الاعتبار، نركز بشكل مباشر على مشكلة تحديد معمارية شبكة عصبية التفافية بمعاملات أقل ولكن بدقة مكافئة مقارنة بنموذج معروف. لقد اكتشفنا مثل هذه المعمارية، والتي نسميها SqueezeNet. بالإضافة إلى ذلك، نقدم تحليلنا لاستراتيجيات التصميم التي أدت إلى تطوير SqueezeNet.

تم تنظيم بقية الورقة البحثية على النحو التالي. في القسم 2، نستعرض الأعمال ذات الصلة. ثم، في القسمين 3 و 4، نصف ونقيّم معمارية SqueezeNet. بعد ذلك، نحول انتباهنا إلى فهم كيفية تأثير خيارات التصميم المعماري للشبكات العصبية الالتفافية على حجم النموذج ودقته. نقوم بتنظيم نقاشنا في ثلاثة مواضيع: المعمارية الدقيقة للشبكات العصبية الالتفافية (القرارات المعمارية لكل طبقة)، والمعمارية الكلية للشبكات العصبية الالتفافية (التنظيم عالي المستوى للطبقات)، وتأثير ضغط النموذج. في القسم 5، نقوم باستكشاف فضاء التصميم لقرارات المعمارية الدقيقة لـ SqueezeNet، مثل حجم وكمية المرشحات لكل طبقة. في القسم 6، نقيّم تأثير المعمارية الكلية للشبكات العصبية الالتفافية، كما هو مطبق على SqueezeNet؛ وعلى وجه الخصوص، نستكشف تأثير الوحدات المستوحاة من معمارية الشبكة المتبقية (ResNet). أخيراً، في القسم 7، نختتم بالرؤى الأساسية والاتجاهات للعمل المستقبلي.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Over-the-air update (التحديث عبر الهواء)
  - Data-parallel training (التدريب المتوازي للبيانات)
  - On-chip memory (الذاكرة على الشريحة)
  - Application-Specific Integrated Circuits (ASICs) (الدوائر المتكاملة الخاصة بالتطبيقات)
  - Microarchitecture (المعمارية الدقيقة)
  - Macroarchitecture (المعمارية الكلية)
- **Equations:** 0
- **Citations:** Implicit references to Tesla, Consumer Reports, ResNet
- **Special handling:**
  - Kept proper nouns like "Tesla", "Consumer Reports" in English
  - Translated "over-the-air update" as "التحديث عبر الهواء" (update through the air)
  - Translated "ASIC" fully on first use, kept acronym in parentheses
  - Used formal academic tone throughout

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.91
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.88

### Back-Translation Check

The Arabic translation accurately conveys:
- The three main advantages of smaller models (distributed training, client updates, FPGA deployment)
- The paper's focus on finding efficient architectures with equivalent accuracy
- The organization and structure of the paper's subsequent sections
- Technical details about memory constraints and deployment scenarios
