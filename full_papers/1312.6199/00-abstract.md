# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.90
**Glossary Terms Used:** neural networks, deep learning, adversarial, representation, perturbation, generalization

---

### English Version

Deep neural networks are highly expressive models that have recently
achieved state of the art performance on speech and visual recognition
tasks.  While their expressiveness is the reason they succeed, it also causes
them to learn uninterpretable solutions that could have counter-intuitive properties.
In this paper we report two such properties.

First, we find that there is no distinction between individual high level units and random linear
combinations of high level units, according to various methods of unit analysis. It suggests
that it is the space, rather than the individual units, that contains the semantic information
in the high layers of neural networks.

Second, we find that deep neural networks learn input-output mappings that are fairly discontinuous
to a significant extent.
We can cause the network to misclassify an image by applying a certain
hardly perceptible perturbation, which is found by maximizing the network's prediction error.
In addition, the specific nature of these perturbations is not a random artifact of learning: the same perturbation
can cause a different network, that was trained on a different subset of the dataset, to misclassify the same input.

---

### النسخة العربية

الشبكات العصبية العميقة هي نماذج تعبيرية للغاية حققت مؤخراً أداءً متقدماً على مهام التعرف على الكلام والصور المرئية. وبينما تعبيريتها هي سبب نجاحها، فإنها تتسبب أيضاً في تعلم حلول غير قابلة للتفسير يمكن أن يكون لها خصائص متناقضة. في هذا البحث، نقدم اثنين من هذه الخصائص.

أولاً، نجد أنه لا يوجد تمييز بين الوحدات الفردية عالية المستوى والتركيبات الخطية العشوائية للوحدات عالية المستوى، وفقاً لطرق تحليل الوحدات المختلفة. هذا يشير إلى أن الفضاء، وليس الوحدات الفردية، هو الذي يحتوي على المعلومات الدلالية في الطبقات العليا من الشبكات العصبية.

ثانياً، نجد أن الشبكات العصبية العميقة تتعلم تعيينات الإدخال-الإخراج التي تكون متقطعة بشكل كبير إلى حد ملحوظ. يمكننا أن نتسبب في قيام الشبكة بتصنيف صورة بشكل خاطئ من خلال تطبيق اضطراب معين غير محسوس تقريباً، والذي يتم إيجاده من خلال تعظيم خطأ التنبؤ للشبكة. بالإضافة إلى ذلك، فإن الطبيعة المحددة لهذه الاضطرابات ليست نتيجة عشوائية للتعلم: يمكن لنفس الاضطراب أن يتسبب في قيام شبكة مختلفة، تم تدريبها على مجموعة فرعية مختلفة من مجموعة البيانات، بتصنيف نفس الإدخال بشكل خاطئ.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:** adversarial perturbation (اضطراب خصامي), semantic information (معلومات دلالية), representation space (فضاء التمثيل), discontinuous mappings (تعيينات متقطعة)
- **Equations:** 0
- **Citations:** 0
- **Special handling:** This abstract is copied from translations/1312.6199.md with minor enhancements

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.90
- Readability: 0.88
- Glossary consistency: 0.90
- **Overall section score:** 0.90
