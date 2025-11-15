# Abstract
## الملخص

**Section:** abstract
**Translation Quality:** 0.89
**Glossary Terms Used:** convolutional neural network, image segmentation, semantic, object detection, image classification, probabilistic, conditional random fields, accuracy, GPU, object segmentation, dense, boundary

---

### English Version

Deep Convolutional Neural Networks (DCNNs) have recently shown state of the art performance in high level vision tasks, such as image classification and object detection. This work brings together methods from DCNNs and probabilistic graphical models for addressing the task of pixel-level classification (also called "semantic image segmentation"). We show that responses at the final layer of DCNNs are not sufficiently localized for accurate object segmentation. This is due to the very invariance properties that make DCNNs good for high level tasks. We overcome this poor localization property of deep networks by combining the responses at the final DCNN layer with a fully connected Conditional Random Field (CRF). Qualitatively, our "DeepLab" system is able to localize segment boundaries at a level of accuracy which is beyond previous methods. Quantitatively, our method sets the new state-of-art at the PASCAL VOC-2012 semantic image segmentation task, reaching 71.6% IOU accuracy in the test set. We show how these results can be obtained efficiently: Careful network re-purposing and a novel application of the 'hole' algorithm from the wavelet community allow dense computation of neural net responses at 8 frames per second on a modern GPU.

---

### النسخة العربية

أظهرت الشبكات العصبية الالتفافية العميقة (DCNNs) مؤخراً أداءً متقدماً في مهام الرؤية عالية المستوى، مثل تصنيف الصور وكشف الأجسام. يجمع هذا العمل بين أساليب الشبكات العصبية الالتفافية العميقة والنماذج البيانية الاحتمالية لمعالجة مهمة التصنيف على مستوى البكسل (والتي تُسمى أيضاً "التقسيم الدلالي للصور"). نوضح أن استجابات الطبقة النهائية للشبكات العصبية الالتفافية العميقة ليست موضعية بشكل كافٍ لتجزئة الأجسام بدقة. يرجع ذلك إلى خصائص الثبات ذاتها التي تجعل الشبكات العصبية الالتفافية العميقة جيدة للمهام عالية المستوى. نتغلب على خاصية التوضيع الضعيفة هذه للشبكات العميقة من خلال دمج استجابات الطبقة النهائية للشبكة العصبية الالتفافية العميقة مع حقل عشوائي شرطي (CRF) مترابط بالكامل. نوعياً، يستطيع نظامنا "DeepLab" توضيع حدود التقسيم بمستوى دقة يتجاوز الطرق السابقة. كمياً، تحدد طريقتنا أحدث مستوى متقدم في مهمة التقسيم الدلالي للصور PASCAL VOC-2012، محققةً دقة 71.6% في مقياس IOU على مجموعة الاختبار. نوضح كيف يمكن الحصول على هذه النتائج بكفاءة: إعادة توظيف دقيقة للشبكة وتطبيق جديد لخوارزمية "الثقوب" من مجتمع المويجات يتيحان حساباً كثيفاً لاستجابات الشبكة العصبية بمعدل 8 إطارات في الثانية على وحدة معالجة رسومات حديثة.

---

### Translation Notes

- **Key terms introduced:**
  - Deep Convolutional Neural Networks (DCNNs): الشبكات العصبية الالتفافية العميقة
  - Semantic image segmentation: التقسيم الدلالي للصور
  - Pixel-level classification: التصنيف على مستوى البكسل
  - Conditional Random Field (CRF): الحقول العشوائية الشرطية / حقل عشوائي شرطي
  - Localization: التوضيع / توضيع
  - Invariance properties: خصائص الثبات
  - IOU (Intersection over Union): IOU (kept as acronym - standard metric)
  - Hole algorithm: خوارزمية "الثقوب"
  - Wavelet: المويجات
  - Dense computation: حساب كثيف

- **Dataset/Benchmark referenced:** PASCAL VOC-2012
- **Performance metric:** 71.6% IOU accuracy
- **Throughput:** 8 frames per second (8 إطارات في الثانية)
- **Special terms:** "DeepLab" kept in English as it's a proper name

### Quality Metrics

- **Semantic equivalence:** 0.90 - All key concepts accurately conveyed
- **Technical accuracy:** 0.89 - Terminology consistent with glossary and domain standards
- **Readability:** 0.88 - Flows naturally in formal academic Arabic
- **Glossary consistency:** 0.90 - Used established terms from glossary

**Overall section score:** 0.89

### Back-Translation Check (First and Last Sentences)

**Original (first):** "Deep Convolutional Neural Networks (DCNNs) have recently shown state of the art performance in high level vision tasks, such as image classification and object detection."

**Back-translation:** "Deep Convolutional Neural Networks (DCNNs) recently demonstrated advanced performance in high-level vision tasks, such as image classification and object detection."

✅ **Semantic match:** Excellent - conveys the same meaning

**Original (last):** "Careful network re-purposing and a novel application of the 'hole' algorithm from the wavelet community allow dense computation of neural net responses at 8 frames per second on a modern GPU."

**Back-translation:** "Careful network repurposing and a novel application of the 'hole' algorithm from the wavelet community enable dense computation of neural network responses at a rate of 8 frames per second on a modern GPU."

✅ **Semantic match:** Excellent - accurately preserves technical details and meaning
