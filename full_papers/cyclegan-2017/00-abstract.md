# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.92
**Glossary Terms Used:** image-to-image translation, mapping, adversarial loss, cycle consistency, domain, generative adversarial networks

---

### English Version

Image-to-image translation is a class of vision and graphics problems where the goal is to learn the mapping between an input image and an output image using a training set of aligned image pairs. However, for many tasks, paired training data will not be available. We present an approach for learning to translate an image from a source domain X to a target domain Y in the absence of paired examples. Our goal is to learn a mapping G: X → Y such that the distribution of images from G(X) is indistinguishable from the distribution Y using an adversarial loss. Because this mapping is highly under-constrained, we couple it with an inverse mapping F: Y → X and introduce a cycle consistency loss to enforce F(G(X)) ≈ X (and vice versa). Qualitative results are presented on several tasks where paired training data does not exist, including collection style transfer, object transfiguration, season transfer, photo enhancement, etc. Quantitative comparisons against several prior methods demonstrate the superiority of our approach.

---

### النسخة العربية

الترجمة من صورة إلى صورة هي فئة من مسائل الرؤية الحاسوبية والرسومات حيث يكمن الهدف في تعلم التخطيط بين صورة مدخلة وصورة مخرجة باستخدام مجموعة تدريب من أزواج الصور المحاذاة. ومع ذلك، بالنسبة للعديد من المهام، لن تكون بيانات التدريب المقترنة متاحة. نقدم نهجاً لتعلم ترجمة صورة من مجال مصدر X إلى مجال هدف Y في غياب الأمثلة المقترنة. هدفنا هو تعلم تخطيط G: X → Y بحيث يكون توزيع الصور من G(X) غير قابل للتمييز عن التوزيع Y باستخدام خسارة تنافسية خصامية. ونظراً لأن هذا التخطيط يعاني من قيود ناقصة بشكل كبير، فإننا نقرنه بتخطيط عكسي F: Y → X ونقدم خسارة اتساق دوري لفرض F(G(X)) ≈ X (والعكس صحيح). يتم تقديم نتائج نوعية على عدة مهام حيث لا توجد بيانات تدريب مقترنة، بما في ذلك نقل نمط المجموعة، وتحويل الكائنات، ونقل المواسم، وتحسين الصور، وغيرها. تُظهر المقارنات الكمية مع عدة طرق سابقة تفوق نهجنا.

---

### Translation Notes

- **Figures referenced:** Figure 1 (implicitly referenced in the context)
- **Key terms introduced:**
  - image-to-image translation (الترجمة من صورة إلى صورة)
  - paired training data (بيانات التدريب المقترنة)
  - cycle consistency loss (خسارة الاتساق الدوري)
  - adversarial loss (خسارة تنافسية خصامية)
  - domain (مجال)
  - mapping (تخطيط)
  - style transfer (نقل النمط)
  - object transfiguration (تحويل الكائنات)

- **Equations:** 2 mappings (G: X → Y and F: Y → X)
- **Citations:** None in abstract
- **Special handling:**
  - Mathematical notation preserved: G: X → Y, F: Y → X, F(G(X)) ≈ X
  - "adversarial loss" translated as "خسارة تنافسية خصامية" (combining both competitive and adversarial aspects)
  - "cycle consistency" as "الاتساق الدوري" (circular/cyclic consistency)
  - "under-constrained" as "يعاني من قيود ناقصة" (has insufficient constraints)

### Quality Metrics

- **Semantic equivalence:** 0.93 - All key concepts accurately conveyed
- **Technical accuracy:** 0.95 - Mathematical notation and technical terms preserved correctly
- **Readability:** 0.90 - Natural Arabic flow while maintaining technical precision
- **Glossary consistency:** 0.90 - Consistent use of established terms, introduced new specialized terms
- **Overall section score:** 0.92

### Back-Translation Check (First Sentence)

**Arabic:** الترجمة من صورة إلى صورة هي فئة من مسائل الرؤية الحاسوبية والرسومات حيث يكمن الهدف في تعلم التخطيط بين صورة مدخلة وصورة مخرجة باستخدام مجموعة تدريب من أزواج الصور المحاذاة.

**Back to English:** Image-to-image translation is a category of computer vision and graphics problems where the goal lies in learning the mapping between an input image and an output image using a training set of aligned image pairs.

**Assessment:** ✅ Semantically equivalent, preserves all key information
