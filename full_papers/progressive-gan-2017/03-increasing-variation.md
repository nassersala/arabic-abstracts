# Section 3: Increasing Variation Using Minibatch Standard Deviation
## القسم 3: زيادة التنوع باستخدام الانحراف المعياري للدفعة الصغيرة

**Section:** Methodology - Increasing Variation
**Translation Quality:** 0.86
**Glossary Terms Used:** generator (المولد), discriminator (المميز), mode collapse (انهيار الأنماط), minibatch (دفعة صغيرة), standard deviation (الانحراف المعياري), latent code (رمز كامن), feature map (خريطة ميزات), variation (تنوع), diversity (تنوع)

---

### English Version

GANs have a tendency to capture only a subset of the variation found in training data, and Salimans et al. (2016) suggest "minibatch discrimination" as a solution. They compute feature statistics not only from individual images but also across the minibatch, thus encouraging the minibatches of generated and training images to show similar statistics. This is implemented by adding a minibatch layer towards the end of the discriminator, where the layer learns a large tensor to project the input activations into an array of statistics.

We simplify this approach drastically while also improving the variation. Our simplified solution has neither learnable parameters nor new hyperparameters. We first compute the standard deviation for each feature in each spatial location over the minibatch. We then average these estimates over all features and spatial locations to arrive at a single value. We replicate the value and concatenate it to all spatial locations and over the minibatch, yielding one additional (constant) feature map. This layer could be inserted anywhere in the discriminator, but we have found it to work best towards the end (see Appendix A.1 for details).

Intuitively, this layer provides the discriminator with information about the variation in the minibatch. If the generator produces images with little variation, the discriminator can use this information to penalize it. This encourages the generator to produce more diverse outputs.

**Mathematical formulation.** Let $x \\in \\mathbb{R}^{N \\times C \\times H \\times W}$ be the input to the minibatch standard deviation layer, where N is the minibatch size, C is the number of feature maps, and H, W are the height and width. We compute:

$$f(x) = \\frac{1}{CHW} \\sum_{c=1}^{C} \\sum_{h=1}^{H} \\sum_{w=1}^{W} \\sqrt{\\frac{1}{N} \\sum_{n=1}^{N} (x_{n,c,h,w} - \\mu_{c,h,w})^2 + \\epsilon}$$

where $\\mu_{c,h,w} = \\frac{1}{N} \\sum_{n=1}^{N} x_{n,c,h,w}$ is the mean, and $\\epsilon = 10^{-8}$ is a small constant for numerical stability. The scalar value $f(x)$ is then replicated to create an additional feature map that is concatenated to the input.

This approach is significantly simpler than the original minibatch discrimination, as it has no learnable parameters and requires only a single scalar summary statistic. Despite its simplicity, we found it to be highly effective at increasing variation in the generated images.

**Connection to diversity.** By providing the discriminator with information about the variation within a minibatch, we give it the ability to recognize when the generator is producing insufficiently diverse outputs. This creates pressure for the generator to increase diversity, helping to prevent mode collapse and encouraging the exploration of the full data distribution.

---

### النسخة العربية

تميل شبكات GAN إلى التقاط جزء فقط من التنوع الموجود في بيانات التدريب، ويقترح Salimans وآخرون (2016) "التمييز بين الدفعات الصغيرة" كحل. يحسبون إحصائيات الميزات ليس فقط من الصور الفردية ولكن أيضاً عبر الدفعة الصغيرة، وبالتالي تشجيع الدفعات الصغيرة من الصور المولدة وصور التدريب على إظهار إحصائيات مماثلة. يتم تنفيذ هذا بإضافة طبقة دفعة صغيرة نحو نهاية المميز، حيث تتعلم الطبقة موتراً كبيراً لإسقاط التفعيلات المدخلة في مصفوفة من الإحصائيات.

نبسط هذا النهج بشكل كبير مع تحسين التنوع أيضاً. حلنا المبسط ليس له معاملات قابلة للتعلم ولا معاملات فائقة جديدة. نحسب أولاً الانحراف المعياري لكل ميزة في كل موقع مكاني عبر الدفعة الصغيرة. ثم نحسب متوسط هذه التقديرات عبر جميع الميزات والمواقع المكانية للوصول إلى قيمة واحدة. نكرر القيمة ونربطها بجميع المواقع المكانية وعبر الدفعة الصغيرة، مما ينتج خريطة ميزات إضافية واحدة (ثابتة). يمكن إدراج هذه الطبقة في أي مكان في المميز، لكننا وجدنا أنها تعمل بشكل أفضل نحو النهاية (انظر الملحق A.1 للتفاصيل).

بشكل حدسي، توفر هذه الطبقة للمميز معلومات حول التنوع في الدفعة الصغيرة. إذا أنتج المولد صوراً بتنوع قليل، يمكن للمميز استخدام هذه المعلومات لمعاقبته. يشجع هذا المولد على إنتاج مخرجات أكثر تنوعاً.

**الصياغة الرياضية.** لنفترض أن $x \\in \\mathbb{R}^{N \\times C \\times H \\times W}$ هو المدخل إلى طبقة الانحراف المعياري للدفعة الصغيرة، حيث N هو حجم الدفعة الصغيرة، وC هو عدد خرائط الميزات، وH، W هما الارتفاع والعرض. نحسب:

$$f(x) = \\frac{1}{CHW} \\sum_{c=1}^{C} \\sum_{h=1}^{H} \\sum_{w=1}^{W} \\sqrt{\\frac{1}{N} \\sum_{n=1}^{N} (x_{n,c,h,w} - \\mu_{c,h,w})^2 + \\epsilon}$$

حيث $\\mu_{c,h,w} = \\frac{1}{N} \\sum_{n=1}^{N} x_{n,c,h,w}$ هو المتوسط، و$\\epsilon = 10^{-8}$ هو ثابت صغير للاستقرار العددي. ثم يتم تكرار القيمة العددية $f(x)$ لإنشاء خريطة ميزات إضافية يتم ربطها بالمدخل.

هذا النهج أبسط بكثير من التمييز الأصلي بين الدفعات الصغيرة، حيث أنه ليس له معاملات قابلة للتعلم ويتطلب فقط إحصاءً موجزاً عددياً واحداً. على الرغم من بساطته، وجدنا أنه فعال للغاية في زيادة التنوع في الصور المولدة.

**العلاقة بالتنوع.** من خلال تزويد المميز بمعلومات حول التنوع داخل الدفعة الصغيرة، نمنحه القدرة على التعرف عندما ينتج المولد مخرجات غير متنوعة بشكل كافٍ. يخلق هذا ضغطاً على المولد لزيادة التنوع، مما يساعد على منع انهيار الأنماط وتشجيع استكشاف التوزيع الكامل للبيانات.

---

### Translation Notes

- **Figures referenced:** Reference to Appendix A.1
- **Key terms introduced:**
  - Minibatch discrimination (التمييز بين الدفعات الصغيرة)
  - Minibatch standard deviation (الانحراف المعياري للدفعة الصغيرة)
  - Feature statistics (إحصائيات الميزات)
  - Feature map (خريطة ميزات)
  - Spatial location (موقع مكاني)
  - Numerical stability (الاستقرار العددي)
  - Summary statistic (إحصاء موجز)
- **Equations:** 1 main equation for computing minibatch standard deviation
- **Citations:** Reference to Salimans et al. (2016)
- **Special handling:**
  - Mathematical equations preserved in LaTeX format with proper notation
  - Greek letters (μ, ε) kept in original form
  - Mathematical symbols and notation maintained
  - Subscript notation preserved

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.85
- **Overall section score:** 0.86
