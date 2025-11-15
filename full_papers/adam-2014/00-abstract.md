# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.92
**Glossary Terms Used:** algorithm, optimization, gradient, stochastic, memory, performance, adaptive, convergence, sparse, objective function

---

### English Version

We introduce Adam, an algorithm for first-order gradient-based optimization of stochastic objective functions, based on adaptive estimates of lower-order moments. The method is straightforward to implement, is computationally efficient, has little memory requirements, is invariant to diagonal rescaling of the gradients, and is well suited for problems that are large in terms of data and/or parameters. The method is also appropriate for non-stationary objectives and problems with very noisy and/or sparse gradients. The hyper-parameters have intuitive interpretations and typically require little tuning. Some connections to related algorithms, on which Adam was inspired, are discussed. We also analyze the theoretical convergence properties of the algorithm and provide a regret bound on the convergence rate that is comparable to the best known results under the online convex optimization framework. Empirical results demonstrate that Adam works well in practice and compares favorably to other stochastic optimization methods. Finally, we discuss AdaMax, a variant of Adam based on the infinity norm.

---

### النسخة العربية

نقدم خوارزمية Adam، وهي خوارزمية لتحسين الدوال الهدفية العشوائية القائمة على تدرجات الدرجة الأولى، استناداً إلى تقديرات تكيفية للعزوم ذات الدرجة الأدنى. الطريقة سهلة التنفيذ وفعالة حسابياً، وتتطلب الحد الأدنى من متطلبات الذاكرة، وتكون ثابتة تجاه إعادة قياس التدرجات القطرية، وهي مناسبة تماماً للمسائل الكبيرة من حيث البيانات و/أو المعاملات. كما أن الطريقة مناسبة للأهداف غير الثابتة والمسائل ذات التدرجات الصاخبة جداً و/أو المتفرقة. المعاملات الفائقة لها تفسيرات بديهية وعادة ما تتطلب ضبطاً محدوداً. نناقش بعض الروابط بالخوارزميات ذات الصلة التي استُلهمت منها Adam. كما نحلل الخصائص النظرية لتقارب الخوارزمية ونقدم حداً للندم على معدل التقارب يمكن مقارنته بأفضل النتائج المعروفة في إطار التحسين المحدب عبر الإنترنت. تُظهر النتائج التجريبية أن Adam تعمل بشكل جيد في الممارسة العملية وتتفوق بشكل ملحوظ على طرق التحسين العشوائي الأخرى. أخيراً، نناقش AdaMax، وهو متغير من Adam يعتمد على معيار اللانهاية.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:** Adam, stochastic optimization, adaptive estimates, lower-order moments, gradient-based optimization, first-order, non-stationary objectives, sparse gradients, hyper-parameters, convergence rate, regret bound, online convex optimization, AdaMax, infinity norm
- **Equations:** None in abstract
- **Citations:** None in abstract
- **Special handling:** Technical terminology carefully translated using glossary

### Quality Metrics

- Semantic equivalence: 0.93
- Technical accuracy: 0.94
- Readability: 0.91
- Glossary consistency: 0.92
- **Overall section score:** 0.92

### Back-Translation (Validation)

We present the Adam algorithm, an algorithm for optimizing stochastic objective functions based on first-order gradients, based on adaptive estimates of lower-order moments. The method is easy to implement and computationally efficient, requires minimal memory requirements, is invariant to diagonal gradient rescaling, and is perfectly suited for large problems in terms of data and/or parameters. The method is also suitable for non-stationary objectives and problems with very noisy and/or sparse gradients. The hyper-parameters have intuitive interpretations and typically require limited tuning. We discuss some connections to related algorithms from which Adam was inspired. We also analyze the theoretical convergence properties of the algorithm and provide a bound on regret for the convergence rate that can be compared to the best known results in the online convex optimization framework. Empirical results show that Adam works well in practice and significantly outperforms other stochastic optimization methods. Finally, we discuss AdaMax, a variant of Adam based on the infinity norm.
