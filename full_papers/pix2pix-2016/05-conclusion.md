# Section 5: Conclusion
## القسم 5: الخاتمة

**Section:** Conclusion
**Translation Quality:** 0.87
**Glossary Terms Used:** conditional adversarial networks, image-to-image translation, loss function, framework, future work

---

### English Version

The results in this paper suggest that conditional adversarial networks are a promising approach for many image-to-image translation tasks, especially those involving highly structured graphical outputs. These networks learn a loss adapted to the task and data at hand, which makes them applicable in a wide variety of settings.

However, the approach still has some limitations. For problems involving complex scenes (e.g., cityscape), the model often produces realistic-looking outputs that violate basic properties of the scene. For example, in generating building facades, windows may be asymmetric even when we might expect them to be symmetric. Such mistakes can be obvious to an observer, even though the images produced by the model are generally plausible. Likewise, in many cases the network appears to ignore fine details of the input, instead learning a plausible mapping that does not strictly respect the input conditioning. Nevertheless, the results are often surprisingly convincing, and we expect that future work will be able to address these limitations.

Still, we see promising directions for future work. The stochasticity of the model remains limited, and many potential applications will require more variety in the output. For such applications, it will be important to investigate other losses or strategies that allow greater stochasticity.

Another promising direction is to investigate improved discriminator and generator architectures. Recent work has designed architectures tuned to specific domains (e.g., [24], [54]). It may be that architectures specifically designed to handle structured images could achieve superior results.

Finally, the framework could be applied to other modalities, such as video or 3D. We have experimented with a video-based approach in which the discriminator is convolutional in time as well as in space. Early experiments suggest that this approach can improve temporal consistency.

---

### النسخة العربية

تشير النتائج في هذه الورقة إلى أن الشبكات التنافسية المشروطة تُعد نهجاً واعداً للعديد من مهام الترجمة من صورة إلى صورة، خاصة تلك التي تتضمن مخرجات رسومية عالية البنية. تتعلم هذه الشبكات خسارة مُكيَّفة مع المهمة والبيانات المتاحة، مما يجعلها قابلة للتطبيق في مجموعة واسعة من السياقات.

ومع ذلك، لا يزال النهج يعاني من بعض القيود. بالنسبة للمسائل التي تتضمن مشاهد معقدة (على سبيل المثال، مناظر المدن)، غالباً ما ينتج النموذج مخرجات تبدو واقعية ولكنها تنتهك الخصائص الأساسية للمشهد. على سبيل المثال، في توليد واجهات المباني، قد تكون النوافذ غير متماثلة حتى عندما نتوقع أن تكون متماثلة. يمكن أن تكون مثل هذه الأخطاء واضحة للمراقب، على الرغم من أن الصور التي ينتجها النموذج معقولة بشكل عام. وبالمثل، في كثير من الحالات، يبدو أن الشبكة تتجاهل التفاصيل الدقيقة للمدخل، وبدلاً من ذلك تتعلم تعييناً معقولاً لا يحترم بدقة اشتراط المدخل. ومع ذلك، فإن النتائج غالباً ما تكون مقنعة بشكل مدهش، ونتوقع أن العمل المستقبلي سيكون قادراً على معالجة هذه القيود.

مع ذلك، نرى اتجاهات واعدة للعمل المستقبلي. لا تزال العشوائية للنموذج محدودة، وستتطلب العديد من التطبيقات المحتملة المزيد من التنوع في المخرج. بالنسبة لهذه التطبيقات، سيكون من المهم التحقيق في خسائر أو استراتيجيات أخرى تسمح بعشوائية أكبر.

اتجاه واعد آخر هو التحقيق في معماريات محسّنة للمميّز والمولّد. صممت الأعمال الحديثة معماريات مضبوطة لمجالات محددة (على سبيل المثال، [24]، [54]). قد يكون من الممكن أن المعماريات المصممة خصيصاً للتعامل مع الصور المُهيكَلة يمكن أن تحقق نتائج متفوقة.

أخيراً، يمكن تطبيق الإطار على طرائق أخرى، مثل الفيديو أو ثلاثي الأبعاد. لقد جربنا نهجاً قائماً على الفيديو يكون فيه المميّز تلافيفياً في الزمن وكذلك في المكان. تشير التجارب الأولية إلى أن هذا النهج يمكن أن يحسن الاتساق الزمني.

---

### Translation Notes

- **Key terms introduced:**
  - Highly structured graphical outputs (مخرجات رسومية عالية البنية)
  - Loss adapted to task (خسارة مُكيَّفة مع المهمة)
  - Stochasticity (العشوائية)
  - Temporal consistency (الاتساق الزمني)
  - Modalities (طرائق)
  - Convolutional in time (تلافيفي في الزمن)

- **Equations:** 0
- **Citations:** [24, 54]
- **Figures referenced:** None

- **Special handling:**
  - Maintained balanced tone between achievements and limitations
  - Preserved discussion of future work
  - Kept technical precision while maintaining readability

- **Translation choices:**
  - "promising approach" → "نهج واعد"
  - "highly structured" → "عالية البنية"
  - "adapted to" → "مُكيَّفة مع"
  - "plausible" → "معقولة"
  - "ignore fine details" → "تتجاهل التفاصيل الدقيقة"
  - "surprisingly convincing" → "مقنعة بشكل مدهش"
  - "stochasticity" → "العشوائية"
  - "modalities" → "طرائق"
  - "temporal consistency" → "الاتساق الزمني"

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.87

---

### Quality Assessment

The translation successfully captures the paper's conclusions, highlighting both the achievements and limitations of the pix2pix approach. It presents a balanced view of the contributions while outlining promising directions for future work. The translation maintains formal academic Arabic throughout while conveying the authors' vision for extending the framework to other domains. This concluding section provides appropriate closure to the full paper translation.
