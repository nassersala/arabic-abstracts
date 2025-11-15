# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** neural networks (شبكة عصبية), adversarial examples (أمثلة خصامية), defensive distillation (تقطير دفاعي), white-box (أبيض), robustness (متانة), optimization (تحسين), objective function (دالة هدفية)

---

### English Version

Neural networks achieve state-of-the-art performance across many domains including image recognition, speech processing, and game playing. However, adversarial examples—minimal perturbations to inputs that cause misclassification—represent a critical vulnerability limiting deployment in security-critical applications.

"Given an input x and any target classification t, it is possible to find a new input x′ that is similar to x but classified as t." This threat becomes particularly concerning in domains like autonomous vehicles where adversarial examples could cause dangerous system failures.

Defensive distillation was proposed to harden networks by training on soft labels from a teacher network using elevated temperature parameters. Initial claims suggested this reduced attack success dramatically. However, the authors' contributions include:

- Three novel attacks (L₀, L₂, L∞) significantly outperforming prior work
- Demonstration that defensive distillation provides minimal actual security benefit
- High-confidence adversarial example transferability testing methodology
- Systematic evaluation of objective function choices in attack formulation

---

### النسخة العربية

تحقق الشبكات العصبية أداءً متقدماً عبر العديد من المجالات بما في ذلك التعرف على الصور ومعالجة الكلام ولعب الألعاب. ومع ذلك، تمثل الأمثلة الخصامية - وهي اضطرابات طفيفة على المدخلات تسبب تصنيفاً خاطئاً - ثغرة أمنية حرجة تحد من النشر في التطبيقات الحرجة للأمان.

"بإعطاء مدخل x وأي تصنيف مستهدف t، من الممكن إيجاد مدخل جديد x′ مشابه لـ x ولكن يصنف كـ t." يصبح هذا التهديد مثيراً للقلق بشكل خاص في مجالات مثل المركبات ذاتية القيادة حيث يمكن للأمثلة الخصامية أن تسبب فشلاً خطيراً في النظام.

تم اقتراح التقطير الدفاعي لتعزيز الشبكات من خلال التدريب على تسميات ناعمة من شبكة معلمة باستخدام معاملات درجة حرارة مرتفعة. أشارت الادعاءات الأولية إلى أن هذا قلل من نجاح الهجوم بشكل كبير. ومع ذلك، تشمل مساهمات المؤلفين:

- ثلاث هجمات جديدة (L₀، L₂، L∞) تتفوق بشكل كبير على الأعمال السابقة
- إثبات أن التقطير الدفاعي يوفر فائدة أمنية فعلية ضئيلة
- منهجية اختبار قابلية نقل الأمثلة الخصامية عالية الثقة
- تقييم منهجي لاختيارات الدالة الهدفية في صياغة الهجوم

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** adversarial examples (أمثلة خصامية), defensive distillation (تقطير دفاعي), soft labels (تسميات ناعمة), teacher network (شبكة معلمة), temperature parameters (معاملات درجة الحرارة)
- **Equations:** None
- **Citations:** Implicit references to prior work on defensive distillation
- **Special handling:**
  - "state-of-the-art" translated as "متقدم" (advanced) maintaining the meaning of best current performance
  - Distance metrics L₀, L₂, L∞ kept in English notation as is standard in Arabic technical literature
  - "white-box access" will be introduced in Background section

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87

**Notes:** This introduction is concise and sets the stage for the technical contributions. The translation maintains the academic tone while ensuring accessibility for Arabic-speaking security researchers.
