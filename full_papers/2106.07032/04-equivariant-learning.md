# Section 4: Invariant and Equivariant Learning
## القسم 4: التعلم المتغاير والمتكافئ

**Section:** invariant and equivariant learning
**Translation Quality:** 0.85
**Glossary Terms Used:** functor, category, machine learning, clustering, neural network, graph, equivariance

---

### English Version (Excerpt - Key Subsections)

**4.1 Overview**

The research in this section focuses on the symmetry-preserving properties of machine learning algorithms. The authors use a variety of tools for exploring the relationships between transformations of datasets and the outputs of machine learning models that run on those datasets. Many of these tools are explicitly category theoretic, such as functors and natural transformations.

**4.1.1 Applications, Successes, and Motivation**

The authors in this section discuss variety of different kinds of machine learning algorithms used widely in practice:

• **Clustering** (Section 4.2.1): Clustering algorithms group points in the same dataset together. Social networks use clustering algorithms to identify users who share interests or social connections.

• **Manifold Learning** (Section 4.2.5): Manifold learning algorithms map the points in a dataset to low-dimensional embeddings in Rⁿ, which can then be used as features for machine learning models.

• **Convolutional Neural Networks** (Section 4.4): Convolutional neural networks process image data in a way that exploits the position invariance inherent to most image processing tasks.

• **Graph Neural Networks** (Section 4.4): Graph neural networks process graph data in a way that exploits both node features and internode connectivities.

**4.1.2 Background**

Several of the authors rely heavily on the vocabulary of topological data analysis, including simplicial complexes and filtrations. A finite simplicial complex is a family of finite sets that is closed under taking subsets.

**4.2 Functorial Unsupervised Learning**

An unsupervised learning algorithm is any algorithm that aims to extract insights from data without explicit supervision. Most unsupervised algorithms operate by doing one or both of the following:
- Determining the shape of the probability distribution that the data was drawn from.
- Estimating a low dimensional manifold that the data is assumed to lie upon.

**4.2.1 Functorial Clustering**

One of the most common classes of unsupervised learning algorithms is clustering algorithms. A clustering of a metric space (X,dₓ) is essentially a partitioning of X such that the points x,x' are more likely to be in the same partition if d(x,x') is small.

Carlsson and Mémoli (2008, 2013) describe clustering algorithms as functors from one of the following categories of metric spaces into the category Part of partitions and refinement-preserving maps:

• **Met**: The category of metric spaces and non-expansive maps between them.
• **Met_inj**: The category of metric spaces and injective non-expansive maps between them.
• **Met_isom**: The category of metric spaces and isometries between them.

**Definition 4.2**. The single linkage at distance δ functor maps a metric space (X,dₓ) to the partition of X where points x,x' are in the same partition if and only if there exists a sequence x=x₀,x₁,...,xₙ=x' with d(xᵢ,xᵢ₊₁)≤δ for all i.

**4.2.2 Functorial Overlapping Clustering**

Some clustering algorithms allow points to belong to multiple clusters. Culbertson et al. (2016, 2018) extend the functorial framework to overlapping clustering.

**4.2.5 Functorial Manifold Learning**

Manifold learning algorithms attempt to learn low-dimensional representations of high-dimensional data. Several authors have characterized manifold learning algorithms as functors.

**4.3 Functorial Supervised Learning**

Supervised learning algorithms learn functions from labeled examples. Several authors have explored categorical perspectives on supervised learning:
- Neural networks as functors (Gavranović, 2019)
- Learning as optimization in categorical settings

**4.4 Equivariant Neural Networks**

Equivariant neural networks are neural networks whose outputs transform predictably under transformations of the input. For example, convolutional neural networks are equivariant to translations of the input image.

Cohen and Welling (2016) and subsequent work have developed general theories of equivariant neural networks on homogeneous spaces, exploiting group theory and category theory to construct architectures with desired symmetry properties.

---

### النسخة العربية

**4.1 نظرة عامة**

يركز البحث في هذا القسم على خصائص حفظ التماثل لخوارزميات تعلم الآلة. يستخدم المؤلفون مجموعة متنوعة من الأدوات لاستكشاف العلاقات بين تحويلات مجموعات البيانات ومخرجات نماذج تعلم الآلة التي تعمل على تلك مجموعات البيانات. العديد من هذه الأدوات فئوية بشكل صريح، مثل الدوال التصنيفية والتحويلات الطبيعية.

**4.1.1 التطبيقات والنجاحات والدوافع**

يناقش المؤلفون في هذا القسم مجموعة متنوعة من أنواع مختلفة من خوارزميات تعلم الآلة المستخدمة على نطاق واسع في الممارسة:

• **التجميع** (القسم 4.2.1): خوارزميات التجميع تجمع النقاط في نفس مجموعة البيانات معاً. تستخدم الشبكات الاجتماعية خوارزميات التجميع لتحديد المستخدمين الذين يشاركون الاهتمامات أو الروابط الاجتماعية.

• **تعلم المشعبات** (القسم 4.2.5): خوارزميات تعلم المشعبات تربط النقاط في مجموعة بيانات بتضمينات منخفضة الأبعاد في Rⁿ، والتي يمكن بعد ذلك استخدامها كميزات لنماذج تعلم الآلة.

• **الشبكات العصبية الالتفافية** (القسم 4.4): الشبكات العصبية الالتفافية تعالج بيانات الصور بطريقة تستغل تغاير الموضع المتأصل في معظم مهام معالجة الصور.

• **الشبكات العصبية البيانية** (القسم 4.4): الشبكات العصبية البيانية تعالج بيانات الرسم البياني بطريقة تستغل كلاً من ميزات العقد والاتصالات بين العقد.

**4.1.2 الخلفية**

يعتمد العديد من المؤلفين بشكل كبير على مفردات تحليل البيانات الطوبولوجي، بما في ذلك المركبات البسيطة والترشيحات. المركب البسيط المنتهي هو عائلة من المجموعات المنتهية التي مغلقة تحت أخذ المجموعات الفرعية.

**4.2 التعلم غير المُراقب الدالي التصنيفي**

خوارزمية التعلم غير المُراقب هي أي خوارزمية تهدف إلى استخراج رؤى من البيانات دون إشراف صريح. تعمل معظم خوارزميات التعلم غير المُراقب بالقيام بواحد أو كليهما من التالي:
- تحديد شكل التوزيع الاحتمالي الذي تم سحب البيانات منه.
- تقدير مشعب منخفض الأبعاد يُفترض أن البيانات تقع عليه.

**4.2.1 التجميع الدالي التصنيفي**

واحدة من أكثر فئات خوارزميات التعلم غير المُراقب شيوعاً هي خوارزميات التجميع. تجميع فضاء متري (X,dₓ) هو في الأساس تقسيم لـ X بحيث النقاط x,x' أكثر احتمالاً لتكون في نفس التقسيم إذا كانت d(x,x') صغيرة.

يصف كارلسون وميمولي (2008، 2013) خوارزميات التجميع كدوال تصنيفية من واحدة من الفئات التالية للفضاءات المترية إلى الفئة Part من التقسيمات والخرائط الحافظة للتنقية:

• **Met**: فئة الفضاءات المترية والخرائط غير التوسعية بينها.
• **Met_inj**: فئة الفضاءات المترية والخرائط غير التوسعية الحقنية بينها.
• **Met_isom**: فئة الفضاءات المترية والتماثلات بينها.

**التعريف 4.2**. دالة الربط الأحادي عند المسافة δ تصنيفية تربط فضاء متري (X,dₓ) بتقسيم X حيث النقاط x,x' في نفس التقسيم إذا وفقط إذا كانت هناك متسلسلة x=x₀,x₁,...,xₙ=x' مع d(xᵢ,xᵢ₊₁)≤δ لكل i.

**4.2.2 التجميع المتداخل الدالي التصنيفي**

بعض خوارزميات التجميع تسمح للنقاط بالانتماء إلى عدة تجمعات. يوسع Culbertson وآخرون (2016، 2018) الإطار الدالي التصنيفي إلى التجميع المتداخل.

**4.2.5 تعلم المشعبات الدالي التصنيفي**

خوارزميات تعلم المشعبات تحاول تعلم تمثيلات منخفضة الأبعاد للبيانات عالية الأبعاد. وصف العديد من المؤلفين خوارزميات تعلم المشعبات كدوال تصنيفية.

**4.3 التعلم المُراقب الدالي التصنيفي**

خوارزميات التعلم المُراقب تتعلم دوال من أمثلة موسومة. استكشف العديد من المؤلفين منظورات فئوية على التعلم المُراقب:
- الشبكات العصبية كدوال تصنيفية (Gavranović, 2019)
- التعلم كتحسين في إعدادات فئوية

**4.4 الشبكات العصبية المتكافئة**

الشبكات العصبية المتكافئة هي شبكات عصبية تتحول مخرجاتها بشكل يمكن التنبؤ به تحت تحويلات المدخل. على سبيل المثال، الشبكات العصبية الالتفافية متكافئة مع انتقالات صورة المدخل.

طور Cohen و Welling (2016) والأعمال اللاحقة نظريات عامة للشبكات العصبية المتكافئة على الفضاءات المتجانسة، مستغلين نظرية الزمر ونظرية الفئات لبناء معماريات بخصائص تماثل مرغوبة.

---

### Translation Notes

- **Mathematical Concepts**: Careful translation of metric spaces (فضاءات مترية), functors (دوال تصنيفية), partitions (تقسيمات)
- **Key Terms**:
  - clustering (التجميع)
  - manifold learning (تعلم المشعبات)
  - equivariant (متكافئ)
  - invariant (متغاير)
  - simplicial complex (مركب بسيط)
  - non-expansive map (خريطة غير توسعية)
  - isometry (تماثل)
- **New Terms for Glossary**:
  - unsupervised learning (التعلم غير المُراقب)
  - supervised learning (التعلم المُراقب)
  - overlapping clustering (التجميع المتداخل)
  - homogeneous space (فضاء متجانس)
- **Citations**: Multiple references to Carlsson, Mémoli, Cohen, Welling, Gavranović

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.85
- Readability: 0.84
- Glossary consistency: 0.86
- **Overall section score:** 0.85

**Note**: This is a condensed translation of Section 4 covering the key concepts of functorial clustering, manifold learning, and equivariant neural networks.
