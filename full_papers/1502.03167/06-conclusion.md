# Section 6: Conclusion
## القسم 6: الخلاصة

**Section:** conclusion
**Translation Quality:** 0.88
**Glossary Terms Used:** batch normalization, internal covariate shift, training, deep neural networks, normalization, learning rate, generalization

---

### English Version

We have presented a novel mechanism for dramatically accelerating the training of deep networks. It is based on the premise that covariate shift, which is known to complicate the training of machine learning systems, also applies to sub-networks and layers, and removing it from internal activations of the network may aid in training. Our proposed method draws its power from normalizing activations, and from incorporating this normalization in the network architecture itself. Our method adds only two extra parameters per activation, and in doing so preserves the representation ability of the network. We presented an algorithm for constructing, training, and performing inference with batch-normalized networks. In our experiments, we demonstrated that Batch Normalization can accelerate training by reducing the number of training steps. Furthermore, we showed that Batch Normalization acts as a regularizer, reducing or even eliminating the need for Dropout.

We applied Batch Normalization to the state-of-the-art image classification model, and showed that we can match its performance using only 7% of the training steps, and can further exceed its accuracy by a substantial margin. Using an ensemble of such models trained with Batch Normalization, we achieve top-5 error rate that improves upon the best known results on ImageNet classification.

Importantly, Batch Normalization achieves the same accuracy as the original model, but does so significantly faster. By using higher learning rates, removing Dropout, and applying other modifications enabled by Batch Normalization, we have been able to improve upon the best published results. This opens up the possibility of achieving state-of-the-art accuracy in a fraction of the time previously required.

Batch Normalization brings us closer to achieving the desirable property that training and testing behavior of deep networks match. Since the normalization is integral to the model architecture, BN provides the benefits both during training and at test time. As our experiments demonstrate, the test accuracy can be significantly improved by properly training the network with Batch Normalization.

In future work, we plan to investigate the effect of Batch Normalization applied to Recurrent Neural Networks (Pascanu et al., 2013), where the internal covariate shift and the vanishing or exploding gradients may be especially severe, and which would allow us to more thoroughly test the hypothesis of internal covariate shift. We also plan to investigate whether Batch Normalization can help with domain adaptation, in scenarios where the training and the test data come from different distributions. Finally, we believe that further theoretical analysis of the algorithm will allow us to better understand its properties and to develop even more effective normalization techniques.

---

### النسخة العربية

قدمنا آلية جديدة لتسريع تدريب الشبكات العميقة بشكل كبير. تستند إلى فرضية أن التحول التبايني، المعروف بتعقيد تدريب أنظمة التعلم الآلي، ينطبق أيضاً على الشبكات الفرعية والطبقات، وإزالته من التنشيطات الداخلية للشبكة قد يساعد في التدريب. تستمد طريقتنا المقترحة قوتها من تطبيع التنشيطات، ومن دمج هذا التطبيع في معمارية الشبكة نفسها. تضيف طريقتنا معاملين إضافيين فقط لكل تنشيط، وبذلك تحافظ على قدرة التمثيل للشبكة. قدمنا خوارزمية لبناء وتدريب وإجراء الاستدلال مع الشبكات المطبعة بالحزمة. في تجاربنا، أثبتنا أن تطبيع الحزمة يمكن أن يسرّع التدريب من خلال تقليل عدد خطوات التدريب. علاوة على ذلك، أظهرنا أن تطبيع الحزمة يعمل كمنظم، مما يقلل أو حتى يلغي الحاجة إلى الإسقاط (Dropout).

طبقنا تطبيع الحزمة على نموذج تصنيف الصور المتقدم، وأظهرنا أنه يمكننا مطابقة أدائه باستخدام 7٪ فقط من خطوات التدريب، ويمكننا أيضاً تجاوز دقته بهامش كبير. باستخدام مجموعة من هذه النماذج المدربة مع تطبيع الحزمة، نحقق معدل خطأ أفضل 5 يحسّن أفضل النتائج المعروفة في تصنيف ImageNet.

الأهم من ذلك، يحقق تطبيع الحزمة نفس دقة النموذج الأصلي، لكنه يفعل ذلك بشكل أسرع بكثير. باستخدام معدلات تعلم أعلى، وإزالة Dropout، وتطبيق تعديلات أخرى ممكّنة بواسطة تطبيع الحزمة، تمكنا من التحسين على أفضل النتائج المنشورة. هذا يفتح إمكانية تحقيق دقة متقدمة في جزء صغير من الوقت المطلوب سابقاً.

يقربنا تطبيع الحزمة من تحقيق الخاصية المرغوبة المتمثلة في تطابق سلوك التدريب والاختبار للشبكات العميقة. نظراً لأن التطبيع جزء لا يتجزأ من معمارية النموذج، يوفر BN الفوائد أثناء التدريب وفي وقت الاختبار. كما توضح تجاربنا، يمكن تحسين دقة الاختبار بشكل كبير من خلال تدريب الشبكة بشكل صحيح مع تطبيع الحزمة.

في العمل المستقبلي، نخطط للتحقيق في تأثير تطبيع الحزمة المطبق على الشبكات العصبية المتكررة (Pascanu et al., 2013)، حيث قد يكون التحول التبايني الداخلي والتدرجات المتلاشية أو المنفجرة شديدة بشكل خاص، والتي ستسمح لنا باختبار فرضية التحول التبايني الداخلي بشكل أكثر شمولاً. نخطط أيضاً للتحقيق فيما إذا كان تطبيع الحزمة يمكن أن يساعد في تكيف المجال، في السيناريوهات التي تأتي فيها بيانات التدريب والاختبار من توزيعات مختلفة. أخيراً، نعتقد أن مزيداً من التحليل النظري للخوارزمية سيسمح لنا بفهم خصائصها بشكل أفضل وتطوير تقنيات تطبيع أكثر فعالية.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Recurrent Neural Networks (الشبكات العصبية المتكررة)
  - Domain adaptation (تكيف المجال)
  - Test time (وقت الاختبار)
  - Representation ability (قدرة التمثيل)
  - State-of-the-art (متقدم/حديث)
- **Equations:** None
- **Citations:** Pascanu et al., 2013
- **Special handling:** Future work directions translated with appropriate technical terminology

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
