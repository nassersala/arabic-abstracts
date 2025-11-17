# Section 8: Discussion and Conclusions
## القسم ٨: المناقشة والاستنتاجات

**Section:** discussion-conclusion
**Translation Quality:** 0.87
**Glossary Terms Used:** real-time, radiance field, rendering, training, optimization, 3D Gaussians, volumetric, rasterization, GPU, CUDA, performance, mesh reconstruction, surface representation

---

### English Version

## 8 DISCUSSION AND CONCLUSIONS

We have presented the first approach that truly allows real-time, high-quality radiance field rendering, in a wide variety of scenes and capture styles, while requiring training times competitive with the fastest previous methods.

Our choice of a 3D Gaussian primitive preserves properties of volumetric rendering for optimization while directly allowing fast splat-based rasterization. Our work demonstrates that – contrary to widely accepted opinion – a continuous representation is not strictly necessary to allow fast and high-quality radiance field training.

The majority (∼80%) of our training time is spent in Python code, since we built our solution in PyTorch to allow our method to be easily used by others. Only the rasterization routine is implemented as optimized CUDA kernels. We expect that porting the remaining optimization entirely to CUDA, as e.g., done in InstantNGP [Müller et al. 2022], could enable significant further speedup for applications where performance is essential.

We also demonstrated the importance of building on real-time rendering principles, exploiting the power of the GPU and speed of software rasterization pipeline architecture. These design choices are the key to performance both for training and real-time rendering, providing a competitive edge in performance over previous volumetric ray-marching.

It would be interesting to see if our Gaussians can be used to perform mesh reconstructions of the captured scene. Aside from practical implications given the widespread use of meshes, this would allow us to better understand where our method stands exactly in the continuum between volumetric and surface representations.

In conclusion, we have presented the first real-time rendering solution for radiance fields, with rendering quality that matches the best expensive previous methods, with training times competitive with the fastest existing solutions.

---

### النسخة العربية

## ٨ المناقشة والاستنتاجات

قدمنا النهج الأول الذي يسمح حقاً بتقديم حقول الإشعاع في الوقت الفعلي بجودة عالية، في مجموعة واسعة من المشاهد وأنماط الالتقاط، مع طلب أوقات تدريب منافسة لأسرع الطرق السابقة.

يحافظ اختيارنا للوحدة الأولية الغاوسية ثلاثية الأبعاد على خصائص التقديم الحجمي للتحسين بينما يسمح مباشرة بالتنقيط السريع القائم على التناثر. يوضح عملنا أنه - على عكس الرأي المقبول على نطاق واسع - ليس التمثيل المستمر ضرورياً بشكل صارم للسماح بتدريب سريع وعالي الجودة لحقول الإشعاع.

تُنفق غالبية (~٨٠٪) من وقت تدريبنا في شفرة Python، لأننا بنينا حلنا في PyTorch للسماح لطريقتنا بأن يستخدمها الآخرون بسهولة. يتم تنفيذ روتين التنقيط فقط كنوى CUDA مُحسَّنة. نتوقع أن نقل التحسين المتبقي بالكامل إلى CUDA، كما هو الحال على سبيل المثال في InstantNGP [Müller et al. 2022]، يمكن أن يتيح تسريعاً إضافياً كبيراً للتطبيقات حيث يكون الأداء ضرورياً.

أوضحنا أيضاً أهمية البناء على مبادئ التقديم في الوقت الفعلي، واستغلال قوة GPU وسرعة معمارية خط التنقيط البرمجي. هذه الخيارات التصميمية هي المفتاح للأداء لكل من التدريب والتقديم في الوقت الفعلي، مما يوفر ميزة تنافسية في الأداء على التتبع الشعاعي الحجمي السابق.

سيكون من المثير للاهتمام معرفة ما إذا كان يمكن استخدام غاوسياتنا لإجراء إعادة بناء شبكي للمشهد الملتقط. بصرف النظر عن الآثار العملية نظراً للاستخدام الواسع للشبكات، سيسمح لنا ذلك بفهم أفضل لموقع طريقتنا بالضبط في الاستمرارية بين التمثيلات الحجمية والسطحية.

في الختام، قدمنا حل التقديم الأول في الوقت الفعلي لحقول الإشعاع، بجودة تقديم تطابق أفضل الطرق السابقة المكلفة، مع أوقات تدريب منافسة لأسرع الحلول الموجودة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Continuum (استمرارية)
  - Surface representations (التمثيلات السطحية)
  - Mesh reconstruction (إعادة البناء الشبكي)
  - Competitive edge (ميزة تنافسية)
  - Pipeline architecture (معمارية خط)

- **Equations:** None
- **Citations:** [Müller et al. 2022]

- **Special handling:**
  - Percentage (~80%) maintained
  - Acknowledgments section not translated (references only)
  - Future work discussion included

### Quality Metrics

- **Semantic equivalence:** 0.88
- **Technical accuracy:** 0.87
- **Readability:** 0.87
- **Glossary consistency:** 0.86
- **Overall section score:** 0.87

### Back-Translation

We presented the first approach that truly allows real-time rendering of radiance fields with high quality, in a wide variety of scenes and capture styles, with training times competitive with the fastest previous methods.

Our choice of 3D Gaussian primitive preserves the properties of volumetric rendering for optimization while directly allowing fast rasterization based on splatting. Our work demonstrates that - contrary to widely accepted opinion - continuous representation is not strictly necessary to allow fast and high-quality training of radiance fields.

The majority (~80%) of our training time is spent in Python code, because we built our solution in PyTorch to allow our method to be easily used by others. Only the rasterization routine is implemented as optimized CUDA kernels. We expect that transferring the remaining optimization entirely to CUDA, as is the case for example in InstantNGP [Müller et al. 2022], could enable significant additional speedup for applications where performance is essential.

We also demonstrated the importance of building on real-time rendering principles, and exploiting GPU power and the speed of software rasterization pipeline architecture. These design choices are the key to performance for both training and real-time rendering, providing a competitive advantage in performance over previous volumetric ray tracing.

It would be interesting to know if our Gaussians can be used to perform mesh reconstruction of the captured scene. Apart from the practical implications given the wide use of meshes, this would allow us to better understand the exact position of our method in the continuum between volumetric and surface representations.

In conclusion, we presented the first real-time rendering solution for radiance fields, with rendering quality matching the best expensive previous methods, with training times competitive with the fastest existing solutions.

**Assessment:** The back-translation accurately preserves the discussion points, conclusions, and future work suggestions with high fidelity.
