# Section 2: Related Work
## القسم 2: الأعمال ذات الصلة

**Section:** Related Work
**Translation Quality:** 0.88
**Glossary Terms Used:** deep learning (تعلم عميق), embedding (التضمين), convolutional neural network (الشبكة العصبية الالتفافية), dimensionality reduction (تقليل الأبعاد), classification (تصنيف)

---

### English Version

Similarly to other recent works which employ deep networks, our approach is a purely data driven method which learns its representation directly from the pixels of the face. Rather than using engineered features, we use a large dataset of labelled faces to attain the appropriate invariances to pose, illumination, and other variational conditions.

In this paper we explore two different deep network architectures that have been recently used to great success in the computer vision community. Both are deep convolutional networks. The first architecture is based on the Zeiler&Fergus model which consists of multiple interleaved layers of convolutions, non-linear activations, local response normalization, and max pooling layers. We additionally add several 1×1×d convolution layers inspired by the work of Lin et al. The second architecture is based on the Inception model of Szegedy et al. which was recently used as the winning approach for ImageNet 2014.

There is a vast corpus of face verification and recognition works. Reviewing it is outside the scope of this paper so we will only briefly discuss the most relevant recent work.

The works of Bromley et al., Chopra et al., and Hadsell et al. use a loss function that tries to project the faces of the same person onto nearby points while increasing the distance between different people. Similar to our approach they use a deep network to learn the embedding space directly; however, they use a contrastive loss in a Siamese architecture which limits them to comparing pairs of images. In contrast, our approach uses triplets of images which allows for more robust training and the enforcement of a margin between the positive and negative pairs.

Zhenyao et al. use a similar loss function to learn an ensemble of models and achieves competitive results on LFW using a larger network. However they use PCA to reduce the dimensionality and do not explore the trade-offs between accuracy and compactness as we do. Hu et al. propose an alternative triplet loss which enforces an absolute distance constraint instead of a margin constraint. This can lead to collapsed models in the early stages of training. The benefit of a margin-based loss is that correct orderings are enforced even when the absolute distances are small or large.

---

### النسخة العربية

بشكل مشابه للأعمال الحديثة الأخرى التي توظف الشبكات العميقة، فإن نهجنا هو طريقة مدفوعة بالبيانات بحتة تتعلم تمثيلها مباشرة من بكسلات الوجه. بدلاً من استخدام ميزات مهندسة، نستخدم مجموعة بيانات كبيرة من الوجوه الموسومة لتحقيق الثوابت المناسبة للوضعية والإضاءة والظروف المتغيرة الأخرى.

في هذا البحث نستكشف معماريتين مختلفتين للشبكات العميقة استخدمتا مؤخراً بنجاح كبير في مجتمع الرؤية الحاسوبية. كلاهما شبكات عصبية التفافية عميقة. المعمارية الأولى تعتمد على نموذج Zeiler&Fergus الذي يتكون من طبقات متشابكة متعددة من الالتفافات والتفعيلات غير الخطية وتطبيع الاستجابة المحلية وطبقات التجميع الأقصى. نضيف أيضاً عدة طبقات التفاف 1×1×d مستوحاة من عمل Lin وآخرين. المعمارية الثانية تعتمد على نموذج Inception من Szegedy وآخرين والذي استخدم مؤخراً كنهج فائز في ImageNet 2014.

هناك مجموعة ضخمة من أعمال التحقق من الوجوه والتعرف عليها. مراجعتها خارج نطاق هذا البحث لذا سنناقش فقط بإيجاز الأعمال الحديثة الأكثر صلة.

تستخدم أعمال Bromley وآخرين، و Chopra وآخرين، و Hadsell وآخرين دالة خسارة تحاول إسقاط وجوه الشخص نفسه على نقاط قريبة مع زيادة المسافة بين الأشخاص المختلفين. بشكل مشابه لنهجنا، يستخدمون شبكة عميقة لتعلم فضاء التضمين مباشرة؛ ومع ذلك، يستخدمون خسارة تباينية في معمارية سيامية (Siamese) تحد منهم لمقارنة أزواج من الصور. في المقابل، يستخدم نهجنا ثلاثيات من الصور مما يسمح بتدريب أكثر قوة وفرض هامش بين الأزواج الإيجابية والسلبية.

يستخدم Zhenyao وآخرون دالة خسارة مشابهة لتعلم مجموعة من النماذج ويحققون نتائج تنافسية على LFW باستخدام شبكة أكبر. ومع ذلك، يستخدمون تحليل المكونات الأساسية (PCA) لتقليل الأبعاد ولا يستكشفون المفاضلات بين الدقة والإيجاز كما نفعل. يقترح Hu وآخرون خسارة ثلاثية بديلة تفرض قيد مسافة مطلق بدلاً من قيد هامش. يمكن أن يؤدي هذا إلى نماذج منهارة في المراحل المبكرة من التدريب. فائدة الخسارة القائمة على الهامش هي أن الترتيبات الصحيحة تُفرض حتى عندما تكون المسافات المطلقة صغيرة أو كبيرة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Siamese architecture (معمارية سيامية)
  - Contrastive loss (خسارة تباينية)
  - Margin-based loss (الخسارة القائمة على الهامش)
  - Zeiler&Fergus model (نموذج Zeiler&Fergus - kept in English)
  - Inception model (نموذج Inception - kept in English)
  - Local response normalization (تطبيع الاستجابة المحلية)
  - Max pooling (التجميع الأقصى)
  - PCA - Principal Component Analysis (تحليل المكونات الأساسية)
- **Equations:** None
- **Citations:** Multiple author names kept in English (Bromley, Chopra, Hadsell, Zhenyao, Hu, Lin, Szegedy)
- **Special handling:**
  - Model names kept in English (Zeiler&Fergus, Inception)
  - Dataset name kept in English: ImageNet, LFW
  - Technical architecture terms translated

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.90
- Readability: 0.86
- Glossary consistency: 0.86
- **Overall section score:** 0.88
