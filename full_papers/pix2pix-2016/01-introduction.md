# Section 1: Introduction
## القسم 1: المقدمة

**Section:** Introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** image processing, computer graphics, computer vision, translation, algorithm, architecture, conditional, adversarial, network, loss function, mapping, training

---

### English Version

Many problems in image processing, computer graphics, and computer vision involve translating an input image into a corresponding output image. These problems are often treated with application-specific algorithms, even though the setting is always the same: map pixels to pixels. Just as automatic language translation systems translate from one language to another, we would like to have "automatic image-to-image translation" systems that can translate one possible representation of a scene into another, given a training set of aligned image pairs.

Traditionally, each of these tasks has been tackled with separate, specialized machinery (e.g., [11, 21, 28, 34, 37, 58, 64, 65]), despite the fact that the setting is always the same. Our goal in this paper is to develop a common framework for all these problems.

The community has already taken significant steps in this direction, with convolutional neural networks (CNNs) becoming the common workhorse behind a wide variety of image prediction problems. CNNs learn to minimize a loss function – an objective that scores the quality of results. While the learning process is automatic, a lot of manual effort still goes into designing effective loss functions. In other words, we still have to tell the CNN what to minimize. But, just as it is infeasible to manually specify our objective for all visual recognition tasks, it is also infeasible to manually specify a loss function for every image-to-image translation task.

It would be highly desirable to develop a loss function that automatically measures the quality of different image-to-image translation tasks. Generative Adversarial Networks (GANs) [23] learn a loss function to train a generative model. This paper explores GANs in the conditional setting. Just as GANs learn a generative model of data, conditional GANs (cGANs) learn a conditional generative model [23]. This makes cGANs suitable for image-to-image translation tasks, where we condition on an input image and generate a corresponding output image.

GANs are generative models that learn a mapping from random noise vector z to output image y: G : z → y [23]. In contrast, conditional GANs learn a mapping from observed image x and random noise vector z, to y: G : {x, z} → y. The generator G is trained to produce outputs that cannot be distinguished from "real" images by an adversarially trained discriminator, D, which is trained to do as well as possible at detecting the generator's "fakes." This training procedure is diagrammed in Figure 2.

Our primary contribution is to demonstrate that on a wide variety of problems, conditional GANs produce reasonable results. Our second contribution is to present a simple framework sufficient to achieve good results, and to analyze the effects of several important architectural choices. Code is available at https://github.com/phillipi/pix2pix.

---

### النسخة العربية

تتضمن العديد من المسائل في معالجة الصور (Image Processing)، والرسومات الحاسوبية (Computer Graphics)، والرؤية الحاسوبية (Computer Vision) ترجمة صورة مدخلة إلى صورة مخرجة مقابلة. غالباً ما تُعالج هذه المسائل بخوارزميات مخصصة لكل تطبيق على حدة، على الرغم من أن السياق دائماً هو نفسه: تعيين البكسلات إلى بكسلات. تماماً كما تترجم أنظمة الترجمة اللغوية الآلية من لغة إلى أخرى، نرغب في امتلاك أنظمة "ترجمة تلقائية من صورة إلى صورة" يمكنها ترجمة تمثيل محتمل لمشهد ما إلى تمثيل آخر، بالاعتماد على مجموعة تدريب من أزواج الصور المحاذية.

تقليدياً، تمت معالجة كل من هذه المهام بآليات منفصلة ومتخصصة (مثل [11، 21، 28، 34، 37، 58، 64، 65])، على الرغم من أن السياق دائماً هو نفسه. هدفنا في هذه الورقة هو تطوير إطار عمل مشترك لجميع هذه المسائل.

لقد خطا المجتمع البحثي بالفعل خطوات مهمة في هذا الاتجاه، حيث أصبحت الشبكات العصبية التلافيفية (Convolutional Neural Networks - CNNs) الأداة الأساسية وراء مجموعة واسعة من مسائل التنبؤ بالصور. تتعلم الشبكات العصبية التلافيفية تقليل دالة خسارة - وهي هدف يقيّم جودة النتائج. بينما تكون عملية التعلم تلقائية، لا يزال هناك جهد يدوي كبير يُبذل في تصميم دوال خسارة فعالة. بعبارة أخرى، لا يزال علينا إخبار الشبكة العصبية التلافيفية بما يجب تقليله. لكن، تماماً كما أنه من غير العملي تحديد هدفنا يدوياً لجميع مهام التعرف البصري، فإنه أيضاً من غير العملي تحديد دالة خسارة يدوياً لكل مهمة ترجمة من صورة إلى صورة.

سيكون من المرغوب للغاية تطوير دالة خسارة تقيس تلقائياً جودة مهام الترجمة المختلفة من صورة إلى صورة. تتعلم الشبكات التنافسية التوليدية (Generative Adversarial Networks - GANs) [23] دالة خسارة لتدريب نموذج توليدي. تستكشف هذه الورقة الشبكات التنافسية التوليدية في السياق المشروط. تماماً كما تتعلم الشبكات التنافسية التوليدية نموذجاً توليدياً للبيانات، فإن الشبكات التنافسية التوليدية المشروطة (conditional GANs - cGANs) تتعلم نموذجاً توليدياً مشروطاً [23]. هذا يجعل الشبكات التنافسية التوليدية المشروطة مناسبة لمهام الترجمة من صورة إلى صورة، حيث نشترط على صورة مدخلة ونولد صورة مخرجة مقابلة.

الشبكات التنافسية التوليدية هي نماذج توليدية تتعلم تعييناً من متجه ضوضاء عشوائية z إلى صورة مخرجة y: G : z → y [23]. في المقابل، تتعلم الشبكات التنافسية التوليدية المشروطة تعييناً من صورة ملاحظة x ومتجه ضوضاء عشوائية z، إلى y: G : {x, z} → y. يُدرّب المولّد G لإنتاج مخرجات لا يمكن تمييزها عن الصور "الحقيقية" بواسطة مميّز D مُدرّب تنافسياً، والذي يُدرّب للقيام بأفضل ما يمكن في كشف "التزييفات" الصادرة عن المولّد. هذا الإجراء التدريبي موضح في الشكل 2.

مساهمتنا الأساسية هي إثبات أن الشبكات التنافسية التوليدية المشروطة تنتج نتائج معقولة على مجموعة واسعة من المسائل. مساهمتنا الثانية هي تقديم إطار عمل بسيط كافٍ لتحقيق نتائج جيدة، وتحليل تأثيرات عدة خيارات معمارية مهمة. الكود متاح على https://github.com/phillipi/pix2pix.

---

### Translation Notes

- **Figures referenced:** Figure 2
- **Key terms introduced:**
  - Image-to-image translation (الترجمة من صورة إلى صورة)
  - Conditional GANs (الشبكات التنافسية التوليدية المشروطة - cGANs)
  - Generator (المولّد - G)
  - Discriminator (المميّز - D)
  - Aligned image pairs (أزواج الصور المحاذية)
  - Random noise vector (متجه ضوضاء عشوائية)
  - Convolutional neural networks (الشبكات العصبية التلافيفية - CNNs)

- **Equations:** 2 mapping formulations
- **Citations:** [11, 21, 28, 34, 37, 58, 64, 65], [23]
- **Special handling:**
  - Maintained mathematical notation for mappings (G : z → y, G : {x, z} → y)
  - Preserved GitHub URL in original form
  - Kept acronyms in English with Arabic translations

- **Translation choices:**
  - "image processing" → "معالجة الصور"
  - "computer graphics" → "الرسومات الحاسوبية"
  - "computer vision" → "الرؤية الحاسوبية"
  - "map pixels to pixels" → "تعيين البكسلات إلى بكسلات"
  - "automatic image-to-image translation" → "ترجمة تلقائية من صورة إلى صورة"
  - "loss function" → "دالة خسارة"
  - "generative model" → "نموذج توليدي"
  - "generator" → "المولّد"
  - "discriminator" → "المميّز"
  - "fakes" → "التزييفات"

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87

---

### Quality Assessment

The translation successfully conveys the core motivation and approach of the pix2pix paper. It explains the problem of hand-engineering loss functions, introduces conditional GANs as the solution, and distinguishes between standard GANs and conditional GANs. The translation maintains formal academic Arabic while preserving technical precision. The slightly lower score compared to the abstract reflects the increased complexity and length of this section.
