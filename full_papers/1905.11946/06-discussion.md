# Section 6: Discussion
## القسم 6: المناقشة

**Section:** discussion
**Translation Quality:** 0.87
**Glossary Terms Used:** compound scaling, EfficientNet, accuracy, FLOPS, baseline, class activation map (CAM), scaling method, depth, width, resolution

---

### English Version

To disentangle the contribution of our proposed scaling method from the EfficientNet architecture, Figure 8 compares the ImageNet performance of different scaling methods for the same EfficientNet-B0 baseline network. In general, all scaling methods improve accuracy with the cost of more FLOPS, but our compound scaling method can further improve accuracy, by up to 2.5%, than other single-dimension scaling methods, suggesting the importance of our proposed compound scaling.

**Figure 8. Scaling Up EfficientNet-B0 with Different Methods.**

In order to further understand why our compound scaling method is better than others, Figure 7 compares the class activation map (Zhou et al., 2016) for a few representative models with different scaling methods. All these models are scaled from the same baseline, and their statistics are shown in Table 7. Images are randomly picked from ImageNet validation set. As shown in the figure, the model with compound scaling tends to focus on more relevant regions with more object details, while other models are either lack of object details or unable to capture all objects in the images.

**Table 7. Scaled Models Used in Figure 7.**

| Model | FLOPS | Top-1 Acc. |
|-------|-------|------------|
| Baseline model (EfficientNet-B0) | 0.4B | 77.3% |
| Scale model by depth (d=4) | 1.8B | 79.0% |
| Scale model by width (w=2) | 1.8B | 78.9% |
| Scale model by resolution (r=2) | 1.9B | 79.1% |
| Compound Scale (d=1.4, w=1.2, r=1.3) | 1.8B | 81.1% |

---

### النسخة العربية

لفصل مساهمة طريقة التوسيع المقترحة عن معمارية EfficientNet، يقارن الشكل 8 أداء ImageNet لطرق التوسيع المختلفة لنفس شبكة خط الأساس EfficientNet-B0. بشكل عام، تحسن جميع طرق التوسيع الدقة بتكلفة المزيد من FLOPS، لكن طريقة التوسيع المركب الخاصة بنا يمكن أن تحسن الدقة بشكل أكبر، بما يصل إلى 2.5%، من طرق التوسيع أحادية البُعد الأخرى، مما يشير إلى أهمية التوسيع المركب المقترح.

**الشكل 8. توسيع EfficientNet-B0 بطرق مختلفة.**

من أجل فهم أفضل لسبب كون طريقة التوسيع المركب الخاصة بنا أفضل من الطرق الأخرى، يقارن الشكل 7 خريطة تنشيط الفئة (Zhou et al., 2016) لعدد قليل من النماذج التمثيلية بطرق توسيع مختلفة. تم توسيع جميع هذه النماذج من نفس خط الأساس، وتُظهر إحصائياتها في الجدول 7. تم اختيار الصور بشكل عشوائي من مجموعة التحقق من ImageNet. كما هو موضح في الشكل، يميل النموذج ذو التوسيع المركب إلى التركيز على المناطق الأكثر صلة مع المزيد من تفاصيل الشيء، بينما تفتقر النماذج الأخرى إما إلى تفاصيل الشيء أو غير قادرة على التقاط جميع الأشياء في الصور.

**الجدول 7. النماذج الموسعة المستخدمة في الشكل 7.**

| النموذج | FLOPS | دقة أفضل 1 |
|-------|-------|------------|
| النموذج الأساسي (EfficientNet-B0) | 0.4B | 77.3% |
| توسيع النموذج بالعمق (d=4) | 1.8B | 79.0% |
| توسيع النموذج بالعرض (w=2) | 1.8B | 78.9% |
| توسيع النموذج بدقة الوضوح (r=2) | 1.9B | 79.1% |
| التوسيع المركب (d=1.4, w=1.2, r=1.3) | 1.8B | 81.1% |

---

### Translation Notes

- **Figures referenced:** Figure 7 (Class Activation Maps), Figure 8 (Scaling comparison)
- **Tables referenced:** Table 7 (Model statistics)
- **Key terms introduced:** class activation map (خريطة تنشيط الفئة), disentangle (فصل), object details (تفاصيل الشيء), relevant regions (المناطق الأكثر صلة)
- **Equations:** None
- **Citations:** Reference to Zhou et al., 2016 for CAM
- **Special handling:** Discussion of visual analysis (CAM); comparison of scaling methods

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
