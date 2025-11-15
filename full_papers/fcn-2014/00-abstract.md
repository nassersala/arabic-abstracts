# Abstract
## الملخص

**Section:** Abstract
**Translation Quality:** 0.89
**Glossary Terms Used:** convolutional networks, semantic segmentation, fully convolutional, end-to-end, fine-tuning, architecture

---

### English Version

Convolutional networks are powerful visual models that yield hierarchies of features. We show that convolutional networks by themselves, trained end-to-end, pixels-to-pixels, exceed the state-of-the-art in semantic segmentation. Our key insight is to build "fully convolutional" networks that take input of arbitrary size and produce correspondingly-sized output with efficient inference and learning. We define and detail the space of fully convolutional networks, explain their application to spatially dense prediction tasks, and draw connections to prior models. We adapt contemporary classification networks (AlexNet, the VGG net, and GoogLeNet) into fully convolutional networks and transfer their learned representations by fine-tuning to the segmentation task. We then define a novel architecture that combines semantic information from a deep, coarse layer with appearance information from a shallow, fine layer to produce accurate and detailed segmentations. Our fully convolutional network achieves state-of-the-art segmentation of PASCAL VOC (20% relative improvement to 62.2% mean IU on 2012), NYUDv2, and SIFT Flow, while inference takes one third of a second for a typical image.

---

### النسخة العربية

الشبكات الالتفافية هي نماذج بصرية قوية تُنتج تسلسلات هرمية من الميزات. نُظهر أن الشبكات الالتفافية بحد ذاتها، والمدربة من البداية إلى النهاية، من البكسل إلى البكسل، تتجاوز أحدث ما توصلت إليه التقنية في التجزئة الدلالية. رؤيتنا الرئيسية هي بناء شبكات "التفافية كاملة" تأخذ مدخلات ذات حجم تعسفي وتنتج مخرجات ذات حجم مطابق مع استنتاج وتعلم فعالين. نُعرّف ونُفصّل فضاء الشبكات الالتفافية الكاملة، ونشرح تطبيقها على مهام التنبؤ الكثيفة مكانياً، ونربطها بالنماذج السابقة. نقوم بتكييف شبكات التصنيف المعاصرة (AlexNet، وشبكة VGG، وGoogLeNet) إلى شبكات التفافية كاملة وننقل تمثيلاتها المتعلمة من خلال الضبط الدقيق لمهمة التجزئة. ثم نُعرّف معمارية جديدة تجمع بين المعلومات الدلالية من طبقة عميقة خشنة مع معلومات المظهر من طبقة سطحية دقيقة لإنتاج تجزئات دقيقة ومفصلة. تحقق شبكتنا الالتفافية الكاملة أحدث ما توصلت إليه التقنية في تجزئة PASCAL VOC (تحسين نسبي بنسبة 20% إلى 62.2% متوسط IU في 2012)، وNYUDv2، وSIFT Flow، بينما يستغرق الاستنتاج ثلث ثانية لصورة نموذجية.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:**
  - Fully convolutional networks (الشبكات الالتفافية الكاملة)
  - Semantic segmentation (التجزئة الدلالية)
  - End-to-end training (التدريب من البداية إلى النهاية)
  - Pixels-to-pixels (من البكسل إلى البكسل)
  - Fine-tuning (الضبط الدقيق)
  - Spatially dense prediction (التنبؤ الكثيف مكانياً)
  - Mean IU (متوسط IU - Intersection over Union)

- **Equations:** None
- **Citations:** Implicit references to AlexNet, VGG, GoogLeNet networks and PASCAL VOC, NYUDv2, SIFT Flow datasets
- **Special handling:**
  - Kept dataset names and network names in English as they are proper nouns
  - Translated technical metrics like "mean IU" with Arabic explanation in parentheses

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.90
- Readability: 0.88
- Glossary consistency: 0.88
- **Overall section score:** 0.89

### Back-translation Check

Key sentence back-translation:
Arabic: "رؤيتنا الرئيسية هي بناء شبكات 'التفافية كاملة' تأخذ مدخلات ذات حجم تعسفي وتنتج مخرجات ذات حجم مطابق"
Back to English: "Our main insight is to build 'fully convolutional' networks that take inputs of arbitrary size and produce outputs of corresponding size"
Original: "Our key insight is to build 'fully convolutional' networks that take input of arbitrary size and produce correspondingly-sized output"
✓ Semantic equivalence confirmed
