# Section 5: Conclusion
## القسم 5: الخاتمة

**Section:** Conclusion
**Translation Quality:** 0.88
**Glossary Terms Used:** training, deep neural networks, internal covariate shift, normalization, convergence, learning rate, accuracy, ImageNet

---

### English Version

We have presented a novel mechanism for dramatically accelerating the training of deep networks. It is based on the premise that covariate shift, which is known to complicate the training of machine learning systems, also applies to sub-networks and layers, and removing it from internal activations of the network may aid in training. Our proposed method draws its power from normalizing activations, and from incorporating this normalization in the network architecture itself. Our method adds only two extra parameters per activation, and in doing so preserves the representation ability of the network. We have presented an algorithm for constructing, training, and performing inference with batch-normalized networks. The resulting networks can be trained with saturating nonlinearities, are more tolerant to increased training rates, and often do not require Dropout for regularization.

Merely adding Batch Normalization to a state-of-the-art image classification model yields a substantial speedup in training. By further increasing the learning rates, removing Dropout, and applying other modifications afforded by Batch Normalization, we reach the previous state of the art with only a small fraction of training steps – and then beat the state of the art in single-network image classification. Furthermore, by combining multiple models trained with Batch Normalization, we perform better than the best known system on ImageNet, by a significant margin.

Interestingly, our method bears similarity to the standardization layer of, but with crucial differences. The goal of Batch Normalization is to achieve a stable distribution of activation values throughout training, and in our experiments we apply it before the nonlinearity since that is where matching the first and second moments is more likely to result in a stable distribution. On the contrary, standardizes the layer output, which in our experience may lead to explosion of activations. We are currently investigating whether Batch Normalization can be beneficial for other forms of networks, such as recurrent neural networks and the generative models used in unsupervised learning, and whether it can help the deeper networks that are used for other challenging tasks.

---

### النسخة العربية

قدمنا آلية جديدة لتسريع تدريب الشبكات العميقة بشكل كبير. تستند إلى فرضية أن تحول التباين، المعروف بتعقيد تدريب أنظمة التعلم الآلي، ينطبق أيضاً على الشبكات الفرعية والطبقات، وأن إزالته من التفعيلات الداخلية للشبكة قد يساعد في التدريب. تستمد طريقتنا المقترحة قوتها من تطبيع التفعيلات، ومن دمج هذا التطبيع في معمارية الشبكة نفسها. تضيف طريقتنا معاملين إضافيين فقط لكل تفعيل، وبذلك تحافظ على قدرة التمثيل للشبكة. قدمنا خوارزمية لبناء وتدريب وإجراء الاستدلال مع الشبكات المُطبّعة بالحزمة. يمكن تدريب الشبكات الناتجة باستخدام لاخطيات مشبعة، وهي أكثر تحملاً لمعدلات التدريب المتزايدة، وغالباً لا تتطلب Dropout للتنظيم.

إن مجرد إضافة تطبيع الحزمة إلى نموذج تصنيف صور متقدم يؤدي إلى تسريع كبير في التدريب. بزيادة معدلات التعلم، وإزالة Dropout، وتطبيق تعديلات أخرى يوفرها تطبيع الحزمة، نصل إلى الحالة السابقة من الفن بجزء صغير فقط من خطوات التدريب - ثم نتفوق على الحالة الحالية من الفن في تصنيف الصور بشبكة واحدة. علاوة على ذلك، من خلال الجمع بين نماذج متعددة مُدربة بتطبيع الحزمة، نؤدي بشكل أفضل من أفضل نظام معروف على ImageNet، بهامش كبير.

من المثير للاهتمام، أن طريقتنا تحمل تشابهاً مع طبقة التوحيد القياسي لـ، ولكن مع اختلافات حاسمة. الهدف من تطبيع الحزمة هو تحقيق توزيع مستقر لقيم التفعيل طوال التدريب، وفي تجاربنا نطبقه قبل اللاخطية نظراً لأن هذا هو المكان الذي من المرجح أن تؤدي فيه مطابقة العزوم الأولى والثانية إلى توزيع مستقر. على العكس من ذلك، يوحد مخرج الطبقة، والذي في تجربتنا قد يؤدي إلى انفجار التفعيلات. نحن نحقق حالياً فيما إذا كان تطبيع الحزمة يمكن أن يكون مفيداً لأشكال أخرى من الشبكات، مثل الشبكات العصبية المتكررة والنماذج التوليدية المستخدمة في التعلم غير الخاضع للإشراف، وما إذا كان يمكن أن يساعد الشبكات الأعمق المستخدمة في مهام أخرى صعبة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - State of the art (الحالة الحالية من الفن / المتقدم)
  - Representation ability (قدرة التمثيل)
  - Standardization layer (طبقة التوحيد القياسي)
  - First and second moments (العزوم الأولى والثانية)
  - Recurrent neural networks (الشبكات العصبية المتكررة)
  - Generative models (النماذج التوليدية)
  - Unsupervised learning (التعلم غير الخاضع للإشراف)
- **Equations:** None
- **Citations:** Reference to prior work on standardization
- **Special handling:**
  - Future research directions mentioned
  - Comparison with related work
  - Summary of contributions

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.88
- Glossary consistency: 0.87
- **Overall section score:** 0.88
