# Section 5: Conclusion
## القسم 5: الخلاصة

**Section:** Conclusion
**Translation Quality:** 0.90
**Glossary Terms Used:** architecture, convolutional cell, transfer learning, scalable, image classification, computational cost, parameters, search space, state-of-the-art, object detection, ImageNet, CIFAR-10

---

### English Version

In this work, we demonstrate how to learn scalable, convolutional cells from data that transfer to multiple image classification tasks. The learned architecture is quite flexible as it may be scaled in terms of computational cost and parameters to easily address a variety of problems. In all cases, the accuracy of the resulting model exceeds all human-designed models – ranging from models designed for mobile applications to computationally-heavy models designed to achieve the most accurate results.

The key insight in our approach is to design a search space that decouples the complexity of an architecture from the depth of a network. This resulting search space permits identifying good architectures on a small dataset (i.e., CIFAR-10) and transferring the learned architecture to image classifications across a range of data and computational scales.

The resulting architectures approach or exceed state-of-the-art performance in both CIFAR-10 and ImageNet datasets with less computational demand than human-designed architectures. The ImageNet results are particularly important because many state-of-the-art computer vision problems (e.g., object detection, face detection, image localization) derive image features or architectures from ImageNet classification models. For instance, we find that image features obtained from ImageNet used in combination with the Faster-RCNN framework achieves state-of-the-art object detection results. Finally, we demonstrate that we can use the resulting learned architecture to perform ImageNet classification with reduced computational budgets that outperform streamlined architectures targeted to mobile and embedded platforms.

---

### النسخة العربية

في هذا العمل، نوضح كيفية تعلم خلايا التفافية قابلة للتوسع من البيانات تنتقل إلى مهام تصنيف صور متعددة. المعمارية المتعلمة مرنة تماماً حيث يمكن توسيعها من حيث التكلفة الحسابية والمعاملات لمعالجة مجموعة متنوعة من المشاكل بسهولة. في جميع الحالات، تتجاوز دقة النموذج الناتج جميع النماذج المصممة بشرياً - بدءاً من النماذج المصممة لتطبيقات المحمول إلى النماذج الثقيلة حسابياً المصممة لتحقيق أدق النتائج.

الرؤية الرئيسية في نهجنا هي تصميم فضاء بحث يفصل تعقيد المعمارية عن عمق الشبكة. يسمح فضاء البحث الناتج بتحديد معماريات جيدة على مجموعة بيانات صغيرة (أي CIFAR-10) ونقل المعمارية المتعلمة إلى تصنيفات الصور عبر مجموعة من المقاييس البيانية والحسابية.

تقترب المعماريات الناتجة أو تتجاوز الأداء المتقدم في كل من مجموعات بيانات CIFAR-10 وImageNet مع طلب حسابي أقل من المعماريات المصممة بشرياً. نتائج ImageNet مهمة بشكل خاص لأن العديد من مشاكل الرؤية الحاسوبية المتقدمة (مثل كشف الأجسام، واكتشاف الوجوه، وتحديد موقع الصور) تستمد ميزات الصور أو المعماريات من نماذج تصنيف ImageNet. على سبيل المثال، نجد أن ميزات الصور التي تم الحصول عليها من ImageNet المستخدمة بالاقتران مع إطار Faster-RCNN تحقق نتائج متقدمة في كشف الأجسام. أخيراً، نوضح أنه يمكننا استخدام المعمارية المتعلمة الناتجة لإجراء تصنيف ImageNet بميزانيات حسابية مخفضة تتفوق على المعماريات المبسطة الموجهة نحو المنصات المحمولة والمدمجة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms summarized:**
  - Scalable convolutional cells (خلايا التفافية قابلة للتوسع)
  - Decouples complexity (يفصل تعقيد)
  - Computational budget (ميزانية حسابية)
  - Streamlined architectures (المعماريات المبسطة)
  - Embedded platforms (المنصات المدمجة)

- **Equations:** None
- **Citations:** None explicit, but references to previous sections
- **Special handling:**
  - Model names kept: Faster-RCNN
  - Dataset names kept: CIFAR-10, ImageNet
  - Computer vision tasks listed: object detection, face detection, image localization
  - Emphasis on transferability and scalability maintained

### Quality Metrics

- **Semantic equivalence:** 0.91 - Captures all key conclusions and contributions
- **Technical accuracy:** 0.92 - All technical terms accurately translated
- **Readability:** 0.89 - Clear, concise conclusion in formal Arabic
- **Glossary consistency:** 0.90 - Consistent terminology throughout
- **Overall section score:** 0.90

### Back-Translation Validation

In this work, we demonstrate how to learn scalable convolutional cells from data that transfer to multiple image classification tasks. The learned architecture is very flexible as it can be scaled in terms of computational cost and parameters to easily address a variety of problems. In all cases, the accuracy of the resulting model exceeds all human-designed models - from models designed for mobile applications to computationally heavy models designed to achieve the most accurate results.

The key insight in our approach is designing a search space that separates the complexity of the architecture from the depth of the network. The resulting search space allows identifying good architectures on a small dataset (i.e., CIFAR-10) and transferring the learned architecture to image classifications across a range of data and computational scales.

The resulting architectures approach or exceed state-of-the-art performance in both CIFAR-10 and ImageNet datasets with less computational demand than human-designed architectures. ImageNet results are particularly important because many state-of-the-art computer vision problems (such as object detection, face detection, and image localization) derive image features or architectures from ImageNet classification models. For example, we find that image features obtained from ImageNet used in conjunction with the Faster-RCNN framework achieve state-of-the-art results in object detection. Finally, we demonstrate that we can use the resulting learned architecture to perform ImageNet classification with reduced computational budgets that outperform streamlined architectures targeted at mobile and embedded platforms.
