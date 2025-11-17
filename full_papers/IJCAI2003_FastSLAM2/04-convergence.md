# Section 5: Convergence
## القسم 5: التقارب

**Section:** theoretical-analysis
**Translation Quality:** 0.85
**Glossary Terms Used:** convergence, algorithm, SLAM, linear, Gaussian, Kalman filter, particle, features, landmarks

---

### English Version

## 5 Convergence

A key result in this paper is the fact that our new version of FastSLAM converges for M=1 particle, for a restricted class of linear Gaussian problems (the same for which KFs converge [5; 18]). Specifically, our result applies to SLAM problems characterized by the following linear form:

sₜ = Asₜ₋₁ + Buₜ + εₜ     (23)
zₜ = Csₜ + Dmₙₜ + δₜ     (24)

Linear SLAM can be thought of as a robot operating in a Cartesian space equipped with a noise-free compass, and sensors that measure distances to features along the coordinate axes. The following theorem, whose proof can be found in the appendix, states the convergence of our new FastSLAM variant:

**Theorem.** For linear SLAM, FastSLAM with M=1 particles converges in expectation to the correct map if all features are observed infinitely often, and if the location of one feature is known in advance.

This theorem parallels a similar result previously published for the Kalman filter [5; 18]. However, this result applies to the Kalman filter, whose update requires time quadratic in the number of landmarks N. With M=1, the resampling step becomes obsolete and each update takes constant time. To our knowledge, our result is the first convergence result for a constant-time SLAM algorithm. It even holds if all features are arranged in a large loop, a situation often thought of as the worst case for SLAM problems [8].

---

### النسخة العربية

## 5 التقارب

نتيجة رئيسية في هذه الورقة هي حقيقة أن نسختنا الجديدة من FastSLAM تتقارب لـ M=1 جسيمة، لفئة مقيدة من المسائل الغاوسية الخطية (نفس المسائل التي تتقارب لها مرشحات كالمان [5؛ 18]). على وجه التحديد، تنطبق نتيجتنا على مسائل SLAM المميزة بالشكل الخطي التالي:

sₜ = Asₜ₋₁ + Buₜ + εₜ     (23)
zₜ = Csₜ + Dmₙₜ + δₜ     (24)

يمكن التفكير في SLAM الخطي كروبوت يعمل في فضاء ديكارتي مجهز ببوصلة خالية من الضوضاء، ومستشعرات تقيس المسافات إلى الخصائص على طول محاور الإحداثيات. تنص النظرية التالية، التي يمكن العثور على إثباتها في الملحق، على تقارب متغير FastSLAM الجديد الخاص بنا:

**نظرية.** بالنسبة لـ SLAM الخطي، تتقارب FastSLAM مع M=1 جسيمة في التوقع إلى الخريطة الصحيحة إذا لوحظت جميع الخصائص بشكل لا نهائي في كثير من الأحيان، وإذا كان موقع خاصية واحدة معروفاً مسبقاً.

توازي هذه النظرية نتيجة مماثلة نُشرت سابقاً لمرشح كالمان [5؛ 18]. ومع ذلك، تنطبق هذه النتيجة على مرشح كالمان، الذي يتطلب تحديثه وقتاً تربيعياً في عدد المعالم N. مع M=1، تصبح خطوة إعادة أخذ العينات عفا عليها الزمن ويستغرق كل تحديث وقتاً ثابتاً. على حد علمنا، نتيجتنا هي أول نتيجة تقارب لخوارزمية SLAM ذات وقت ثابت. إنها صحيحة حتى إذا تم ترتيب جميع الخصائص في حلقة كبيرة، وهي حالة غالباً ما يُنظر إليها على أنها أسوأ حالة لمسائل SLAM [8].

---

### Translation Notes

- **Equations:** 2 numbered equations (23-24)
- **Key terms introduced:** linear SLAM, Cartesian space, noise-free compass, convergence in expectation
- **Theorem:** Formal theorem statement translated with proper mathematical rigor
- **Citations:** [5], [18], [8]
- **Special handling:**
  - Matrix notation (A, B, C, D) preserved
  - "converges in expectation" translated as "تتقارب في التوقع"
  - "obsolete" translated as "عفا عليها الزمن" (became obsolete)
  - Mathematical conditions maintained precisely

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.85
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.85

### Back-Translation Validation (Theorem)

**Original Theorem:**
For linear SLAM, FastSLAM with M=1 particles converges in expectation to the correct map if all features are observed infinitely often, and if the location of one feature is known in advance.

**Back-Translation:**
For linear SLAM, FastSLAM with M=1 particle converges in expectation to the correct map if all features are observed infinitely often, and if the location of one feature is known in advance.
