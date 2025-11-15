# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.93
**Glossary Terms Used:** neural networks (شبكة عصبية), machine learning (تعلم الآلة), adversarial examples (أمثلة خصامية), robustness (متانة), security (أمان), attack (هجوم), defense (دفاع), distillation (تقطير), algorithm (خوارزمية)

---

### English Version

Neural networks provide state-of-the-art results for most machine learning tasks. Unfortunately, neural networks are vulnerable to adversarial examples: given an input x and any target classification t, it is possible to find a new input x' that is similar to x but classified as t. This makes it difficult to apply neural networks in security-critical areas.

Defensive distillation is a recently proposed approach that can take an arbitrary neural network, and increase its robustness, reducing the success rate of current attacks' ability to find adversarial examples from 95% to 0.5%. In this paper, we demonstrate that defensive distillation does not significantly increase the robustness of neural networks by introducing three new attack algorithms that are successful on both distilled and undistilled neural networks with 100% probability. Our attacks are tailored to three distance metrics used previously in the literature, and when compared to previous adversarial example generation algorithms, our attacks are often much more effective (and never worse). Furthermore, we propose using high-confidence adversarial examples in a simple transferability test we show can also be used to break defensive distillation.

We hope our attacks will be used as a benchmark in future defense attempts to create neural networks that resist adversarial examples.

---

### النسخة العربية

توفر الشبكات العصبية نتائج متقدمة لمعظم مهام تعلم الآلة. للأسف، الشبكات العصبية عرضة للأمثلة الخصامية: بإعطاء مدخل x وأي تصنيف مستهدف t، من الممكن إيجاد مدخل جديد x' مشابه لـ x ولكن يصنف كـ t. هذا يجعل من الصعب تطبيق الشبكات العصبية في المجالات الحرجة للأمان.

التقطير الدفاعي هو نهج مقترح مؤخراً يمكنه أخذ أي شبكة عصبية وزيادة متانتها، مما يقلل معدل نجاح قدرة الهجمات الحالية على إيجاد أمثلة خصامية من 95% إلى 0.5%. في هذا البحث، نوضح أن التقطير الدفاعي لا يزيد بشكل كبير من متانة الشبكات العصبية من خلال تقديم ثلاث خوارزميات هجوم جديدة ناجحة على كل من الشبكات العصبية المقطرة وغير المقطرة باحتمالية 100%. هجماتنا مصممة لثلاثة مقاييس مسافة مستخدمة سابقاً في الأدبيات، وعند مقارنتها بخوارزميات توليد الأمثلة الخصامية السابقة، غالباً ما تكون هجماتنا أكثر فعالية (وليست أسوأ أبداً). علاوة على ذلك، نقترح استخدام أمثلة خصامية عالية الثقة في اختبار قابلية النقل البسيط الذي نظهر أنه يمكن استخدامه أيضاً لكسر التقطير الدفاعي.

نأمل أن تُستخدم هجماتنا كمعيار في محاولات الدفاع المستقبلية لإنشاء شبكات عصبية تقاوم الأمثلة الخصامية.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** adversarial examples, defensive distillation, robustness, attack algorithms
- **Equations:** None
- **Citations:** None in abstract
- **Special handling:** Distance metrics (L₀, L₂, L∞) mentioned in full paper

### Quality Metrics

- Semantic equivalence: 0.95
- Technical accuracy: 0.94
- Readability: 0.92
- Glossary consistency: 0.91
- **Overall section score:** 0.93

**Source:** Copied from /home/user/arabic-abstracts/translations/1608.04644.md
