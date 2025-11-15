# Section 1: Introduction
## القسم 1: المقدمة

**Section:** Introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** convolutional networks, semantic segmentation, classification, deep learning, end-to-end, fine-tuning, architecture

---

### English Version

Convolutional networks are driving advances in recognition. Convnets are not only improving for whole-image classification [20, 21, 31], but also making progress on local tasks with structured output. These include advances in bounding box object detection [30, 12, 17], part and keypoint prediction [42, 26], and local correspondence [27, 8].

The natural next step in the progression from coarse to fine inference is to make a prediction at every pixel. Prior approaches have used convnets for semantic segmentation [28, 2, 9, 30, 14, 11], in which each pixel is labeled with the class of its enclosing object or region, but with shortcomings that this work addresses.

We show that a fully convolutional network (FCN) trained end-to-end, pixels-to-pixels on semantic segmentation exceeds the state-of-the-art without further machinery. To our knowledge, this is the first work to train FCNs end-to-end (1) for pixelwise prediction and (2) from supervised pre-training. Fully convolutional versions of existing networks predict dense outputs from arbitrary-sized inputs. Both learning and inference are performed whole-image-at-a-time by dense feedforward computation and backpropagation. In-network upsampling layers enable pixelwise prediction and learning in nets with subsampled pooling.

This method is efficient, both asymptotically and absolutely, and precludes the need for the complications in other approaches. Patchwise training is common [28, 2, 9, 30, 14, 11], but lacks the efficiency of fully convolutional training. Our approach does not make use of pre- and post-processing complications, including superpixels [9, 17], proposals [17, 14], or post-hoc refinement by random fields or local classifiers [9, 17]. Our model transfers recent success in classification [20, 31, 30] to dense prediction by reinterpreting classification nets as fully convolutional and fine-tuning from their learned representations. In contrast, previous works have applied small convnets without supervised pre-training [9, 28, 27].

Semantic segmentation faces an inherent tension between semantics and location: global information resolves what while local information resolves where. Deep feature hierarchies encode location and semantics in a nonlinear local-to-global pyramid. We define a novel "skip" architecture to combine deep, coarse, semantic information and shallow, fine, appearance information (see Figure 3). In the next section we review related work on deep classification nets, FCNs, and recent approaches to semantic segmentation using convnets. The following sections explain FCN design and dense prediction tradeoffs, introduce our architecture with in-network upsampling and multilayer combinations, and describe our experimental framework. Finally, we demonstrate state-of-the-art results on PASCAL VOC 2011-12, NYUDv2, and SIFT Flow.

---

### النسخة العربية

الشبكات الالتفافية تقود التقدم في التعرف البصري. لا تتحسن الشبكات الالتفافية فقط في تصنيف الصور الكاملة [20، 21، 31]، بل تحقق أيضاً تقدماً في المهام الموضعية ذات المخرجات المُنظَّمة. يشمل ذلك التقدم في كشف الأجسام باستخدام صناديق التحديد [30، 12، 17]، والتنبؤ بالأجزاء والنقاط المفصلية [42، 26]، والتوافق الموضعي [27، 8].

الخطوة الطبيعية التالية في التدرج من الاستنتاج الخشن إلى الدقيق هي إجراء تنبؤ عند كل بكسل. استخدمت الأساليب السابقة الشبكات الالتفافية للتجزئة الدلالية [28، 2، 9، 30، 14، 11]، حيث يتم تصنيف كل بكسل بفئة الكائن أو المنطقة المحيطة به، ولكن مع قصور يعالجه هذا العمل.

نُظهر أن الشبكة الالتفافية الكاملة (FCN) المدربة من البداية إلى النهاية، من البكسل إلى البكسل، على التجزئة الدلالية تتجاوز أحدث ما توصلت إليه التقنية دون آليات إضافية. على حد علمنا، هذا هو العمل الأول لتدريب شبكات FCN من البداية إلى النهاية (1) للتنبؤ على مستوى البكسل و(2) من التدريب المسبق الخاضع للإشراف. النسخ الالتفافية الكاملة من الشبكات الموجودة تتنبأ بمخرجات كثيفة من مدخلات ذات أحجام تعسفية. يتم إجراء كل من التعلم والاستنتاج على الصورة الكاملة دفعة واحدة من خلال الحساب الأمامي الكثيف والانتشار العكسي. طبقات الرفع الداخلية في الشبكة تمكن التنبؤ والتعلم على مستوى البكسل في الشبكات ذات التجميع بالعينات الفرعية.

هذه الطريقة فعالة، بشكل مقارب ومطلق على حد سواء، وتستبعد الحاجة إلى التعقيدات في الأساليب الأخرى. التدريب القائم على الرقع شائع [28، 2، 9، 30، 14، 11]، لكنه يفتقر إلى كفاءة التدريب الالتفافي الكامل. لا يستخدم نهجنا تعقيدات المعالجة المسبقة واللاحقة، بما في ذلك البكسلات الفائقة [9، 17]، أو المقترحات [17، 14]، أو التحسين اللاحق بواسطة الحقول العشوائية أو المصنفات الموضعية [9، 17]. ينقل نموذجنا النجاح الأخير في التصنيف [20، 31، 30] إلى التنبؤ الكثيف من خلال إعادة تفسير شبكات التصنيف على أنها التفافية كاملة والضبط الدقيق من تمثيلاتها المتعلمة. على النقيض من ذلك، طبقت الأعمال السابقة شبكات التفافية صغيرة دون تدريب مسبق خاضع للإشراف [9، 28، 27].

تواجه التجزئة الدلالية توتراً جوهرياً بين الدلالات والموقع: المعلومات العامة تحل ما هو الشيء بينما المعلومات الموضعية تحل أين هو. التسلسلات الهرمية للميزات العميقة تشفر الموقع والدلالات في هرم لا خطي من الموضعي إلى العام. نعرّف معمارية "التخطي" الجديدة للجمع بين المعلومات الدلالية العميقة الخشنة ومعلومات المظهر السطحية الدقيقة (انظر الشكل 3). في القسم التالي، نستعرض الأعمال ذات الصلة حول شبكات التصنيف العميقة، وشبكات FCN، والأساليب الحديثة للتجزئة الدلالية باستخدام الشبكات الالتفافية. الأقسام التالية تشرح تصميم FCN والمقايضات في التنبؤ الكثيف، وتقدم معماريتنا مع الرفع الداخلي في الشبكة والتركيبات متعددة الطبقات، وتصف إطار عملنا التجريبي. أخيراً، نظهر نتائج أحدث ما توصلت إليه التقنية على PASCAL VOC 2011-12، وNYUDv2، وSIFT Flow.

---

### Translation Notes

- **Figures referenced:** Figure 3 (skip architecture)
- **Key terms introduced:**
  - Fully convolutional network - FCN (الشبكة الالتفافية الكاملة)
  - Pixelwise prediction (التنبؤ على مستوى البكسل)
  - Dense feedforward computation (الحساب الأمامي الكثيف)
  - In-network upsampling (الرفع الداخلي في الشبكة)
  - Subsampled pooling (التجميع بالعينات الفرعية)
  - Patchwise training (التدريب القائم على الرقع)
  - Skip architecture (معمارية التخطي)
  - Dense prediction (التنبؤ الكثيف)

- **Equations:** None
- **Citations:** Multiple references [2, 8, 9, 11, 12, 14, 17, 20, 21, 26, 27, 28, 30, 31, 42]
- **Special handling:**
  - Kept dataset names (PASCAL VOC, NYUDv2, SIFT Flow) in English
  - Maintained reference numbers in brackets as in original
  - Translated technical concepts while preserving their precise meaning

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88

### Back-translation Check

Key sentence:
Arabic: "نُظهر أن الشبكة الالتفافية الكاملة (FCN) المدربة من البداية إلى النهاية، من البكسل إلى البكسل، على التجزئة الدلالية تتجاوز أحدث ما توصلت إليه التقنية دون آليات إضافية"
Back: "We show that a fully convolutional network (FCN) trained end-to-end, pixel-to-pixel, on semantic segmentation surpasses state-of-the-art without additional mechanisms"
Original: "We show that a fully convolutional network (FCN) trained end-to-end, pixels-to-pixels on semantic segmentation exceeds the state-of-the-art without further machinery"
✓ Semantic equivalence confirmed
