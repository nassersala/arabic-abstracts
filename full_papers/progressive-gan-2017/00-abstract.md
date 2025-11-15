# Section 0: Abstract
## القسم 0: الملخص

**Section:** Abstract
**Translation Quality:** 0.90
**Glossary Terms Used:** generative adversarial networks (شبكات خصامية توليدية), generator (المولد), discriminator (المميز), training (تدريب), resolution (دقة), layers (طبقات), quality (جودة), variation (تنوع), metric (معيار)

---

### English Version

We describe a new training methodology for generative adversarial networks. The key idea is to grow both the generator and discriminator progressively: starting from a low resolution, we add new layers that model increasingly fine details as training progresses. This both speeds the training up and greatly stabilizes it, allowing us to produce images of unprecedented quality, e.g., CelebA images at 1024². We also propose a simple way to increase the variation in generated images, and achieve a record inception score of 8.80 in unsupervised CIFAR10. Additionally, we describe several implementation details that are important for discouraging unhealthy competition between the generator and discriminator. Finally, we suggest a new metric for evaluating GAN results, both in terms of image quality and variation. As an additional contribution, we construct a higher-quality version of the CelebA dataset.

---

### النسخة العربية

نقدم منهجية تدريب جديدة للشبكات الخصامية التوليدية. الفكرة الأساسية هي تنمية كل من المولد والمميز بشكل تدريجي: بدءاً من دقة منخفضة، نضيف طبقات جديدة تنمذج تفاصيل دقيقة بشكل متزايد مع تقدم التدريب. يؤدي هذا إلى تسريع التدريب وتحقيق استقرار كبير له، مما يسمح لنا بإنتاج صور ذات جودة غير مسبوقة، على سبيل المثال، صور CelebA بدقة 1024². كما نقترح طريقة بسيطة لزيادة التنوع في الصور المولدة، ونحقق درجة inception قياسية بلغت 8.80 على مجموعة بيانات CIFAR10 غير الخاضعة للإشراف. بالإضافة إلى ذلك، نصف العديد من تفاصيل التنفيذ المهمة لتثبيط المنافسة غير الصحية بين المولد والمميز. وأخيراً، نقترح معياراً جديداً لتقييم نتائج شبكات GAN، من حيث جودة الصورة والتنوع على حد سواء. كمساهمة إضافية، نقوم ببناء نسخة عالية الجودة من مجموعة بيانات CelebA.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:**
  - Progressive growing (النمو التدريجي)
  - Generative adversarial networks/GANs (الشبكات الخصامية التوليدية)
  - Generator (المولد)
  - Discriminator (المميز)
  - Inception score (درجة inception)
  - CelebA-HQ dataset (مجموعة بيانات CelebA-HQ)
- **Equations:** None in abstract
- **Citations:** Implicit reference to CIFAR10 and CelebA datasets
- **Special handling:** Kept "CelebA" and "CIFAR10" as proper nouns; "inception score" partially transliterated as it's a standard metric name

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.90
- Readability: 0.88
- Glossary consistency: 0.90
- **Overall section score:** 0.90
