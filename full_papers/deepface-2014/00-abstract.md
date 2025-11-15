# Abstract
## الملخص

**Section:** abstract
**Translation Quality:** 0.92
**Glossary Terms Used:** deep neural network, face recognition, convolutional layers, locally connected, alignment, classifier, accuracy, dataset

---

### English Version

In modern face recognition, the conventional pipeline consists of four stages: detect ⇒ align ⇒ represent ⇒ classify. We revisit both the alignment step and the representation step by employing explicit 3D face modeling in order to apply a piecewise affine transformation, and derive a face representation from a nine-layer deep neural network. This deep network involves more than 120 million parameters using several locally connected layers without weight sharing, rather than the standard convolutional layers. Thus we trained it on the largest facial dataset to-date, an identity labeled dataset of four million facial images belonging to more than 4,000 identities. The learned representations coupling the accurate model-based alignment with the large facial database generalize remarkably well to faces in unconstrained environments, even with a simple classifier. Our method reaches an accuracy of 97.35% on the Labeled Faces in the Wild (LFW) dataset, reducing the error of the current state of the art by more than 27%, closely approaching human-level performance.

---

### النسخة العربية

في التعرف على الوجوه الحديث، يتكون خط الأنابيب التقليدي من أربع مراحل: الكشف ⇒ المحاذاة ⇒ التمثيل ⇒ التصنيف. نعيد النظر في كل من خطوة المحاذاة وخطوة التمثيل من خلال استخدام نمذجة صريحة ثلاثية الأبعاد للوجه بهدف تطبيق تحويل أفيني متعدد القطع، ونستخرج تمثيلاً للوجه من شبكة عصبية عميقة ذات تسع طبقات. تتضمن هذه الشبكة العميقة أكثر من 120 مليون معامل باستخدام عدة طبقات محلية الاتصال بدون مشاركة الأوزان، بدلاً من الطبقات الالتفافية القياسية. وبالتالي قمنا بتدريبها على أكبر مجموعة بيانات للوجوه حتى الآن، وهي مجموعة بيانات مُسمَّاة بالهويات تحتوي على أربعة ملايين صورة وجه تنتمي إلى أكثر من 4,000 هوية. تتعمم التمثيلات المتعلمة التي تجمع بين المحاذاة الدقيقة القائمة على النموذج وقاعدة البيانات الكبيرة للوجوه بشكل ملحوظ على الوجوه في البيئات غير المقيدة، حتى مع مصنف بسيط. تصل طريقتنا إلى دقة 97.35% على مجموعة بيانات Labeled Faces in the Wild (LFW)، مما يقلل الخطأ في أحدث التقنيات الحالية بأكثر من 27%، مقتربين بشكل وثيق من الأداء البشري.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:**
  - Face recognition pipeline (خط أنابيب التعرف على الوجوه)
  - 3D face modeling (نمذجة ثلاثية الأبعاد للوجه)
  - Piecewise affine transformation (تحويل أفيني متعدد القطع)
  - Locally connected layers (طبقات محلية الاتصال)
  - Weight sharing (مشاركة الأوزان)
  - Unconstrained environments (البيئات غير المقيدة)
  - State of the art (أحدث التقنيات)
  - Human-level performance (الأداء البشري)
- **Equations:** None
- **Citations:** None explicit (mentions LFW dataset)
- **Special handling:**
  - Kept "LFW" acronym with translation
  - Preserved arrow symbols (⇒) in pipeline description
  - Maintained specific numbers (97.35%, 27%, 120 million, 4 million, 4,000)

### Quality Metrics

- **Semantic equivalence:** 0.92
- **Technical accuracy:** 0.93
- **Readability:** 0.91
- **Glossary consistency:** 0.92
- **Overall section score:** 0.92

### Back-translation Check

Key sentence back-translated to English:
"نعيد النظر في كل من خطوة المحاذاة وخطوة التمثيل من خلال استخدام نمذجة صريحة ثلاثية الأبعاد للوجه"
→ "We revisit both the alignment step and the representation step through using explicit 3D modeling of the face"
✓ Semantically equivalent to original
