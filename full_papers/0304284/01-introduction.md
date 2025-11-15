# Section: Introduction
## القسم: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** category (فئة), opetope (أوبتوب), presheaf (حزمة أمامية), functor (دالة تصنيفية), morphism (تشاكل), multicategory (تعدد فئوي), equivalence (تكافؤ), isomorphic (متشاكل)

---

### English Version

In [3], Baez and Dolan give a definition of weak n-category in which the underlying shapes of cells are 'opetopes' and the underlying data is given by 'opetopic sets'. The idea is that opetopic sets should be presheaves over the category of opetopes. However Baez and Dolan do not explicitly construct the category of opetopes, so opetopic sets are defined directly instead. A relationship between this category of opetopic sets and a category of presheaves is alluded to but not proved.

The main result of this paper is that the category of opetopic sets is equivalent to the category of presheaves over the category of opetopes. However, we do not use the opetopic definitions exactly as given in [3] but continue to use the modifications given in our earlier work ([6], [5]). In these papers we use a generalisation along lines which the original authors began, but chose to abandon for reasons which are unclear. This generalisation enables us, in [6], to exhibit a relationship with the work of Hermida, Makkai and Power ([7]) and, in [5], with the work of Leinster ([13]). Given these useful results, we continue to study the modified theory in this work.

We begin, in Section 1 by giving an explicit construction of the category of opetopes. The idea is as follows. In [6] we constructed, for each k ≥ 0, a category ℂₖ of k-opetopes. For the category **Opetope** of opetopes of all dimensions, each category ℂₖ should be a full subcategory of **Opetope**; furthermore there should be 'face maps' exhibiting the constituent m-opetopes, or 'faces' of a k-opetope, for m ≤ k. We refer to the m-opetope faces as m-faces. Note that there are no degeneracy maps.

The (k − 1)-faces of a k-opetope α should be the (k − 1)-opetopes of its source and target; these should all be distinct. Then each of these faces has its own (k − 2)-faces, but all these (k − 2)-opetopes should not necessarily be considered as distinct (k − 2)-faces in α. For α is a configuration for composing its (k − 1)-faces at their (k − 2)-faces, so the (k − 2)-faces should be identified with one another at places where composition is to occur. That is, the composite face maps from these (k−2)-opetopes to α should therefore be equal. Some further details are then required to deal with isomorphic copies of opetopes.

Recall that a 'configuration' for composing (k −1)-opetopes is expressed as a tree (see [6]) whose nodes are labelled by the (k−1)-opetopes in question, with the edges giving their inputs and outputs. So composition occurs along each edge of the tree, via an object-morphism label, and thus the tree tells us which (k − 1)-opetopes are identified.

In order to express this more precisely, we first give a more formal description of trees (Section 1.2). In fact, this leads to an abstract description of trees as certain Kelly-Mac Lane graphs; this is the subject of [4]. The results of Section 1.2 thus arise as preliminary results in [4] and we refer the reader to this paper for the full account and proofs.

In Section 2, we examine the theory of opetopic sets. We begin by following through our modifications to the opetopic theory to include the theory of opetopic sets. (Our previous work has only dealt with the theory of opetopes.) We then use results of [12] to prove that the category of opetopic sets is indeed equivalent to the category of presheaves on O, the category of opetopes defined in Section 1. This is the main result of this work.

Finally, a comment is due on the notion of 'multitope' as defined in [7]. In this work, Hermida, Makkai and Power begin a definition of n-category explicitly analogous to that of [3], the analogous concepts being 'multitopes' and 'multitopic sets'. In [6] we prove that 'opetopes and multitopes are the same up to isomorphism', that is, for each k ≥ 0 the category of k-opetopes is equivalent to the (discrete) category of k-multitopes. In [7], Hermida, Makkai and Power do go on to give an explicit definition of the analogous category **Multitope**, of multitopes. Given the above equivalences, and assuming the underlying idea is the same, this would be equivalent to the category **Opetope**, but we do not attempt to prove it in this work.

**Terminology**

i) Since we are concerned chiefly with weak n-categories, we follow Baez and Dolan ([3]) and omit the word 'weak' unless emphasis is required; we refer to strict n-categories as 'strict n-categories'.

ii) We use the term 'weak n-functor' for an n-functor where functoriality holds up to coherent isomorphisms, and 'lax' functor when the constraints are not necessarily invertible.

iii) In [3] Baez and Dolan use the terms 'operad' and 'types' where we use 'multicategory' and 'objects'; the latter terminology is more consistent with Leinster's use of 'operad' to describe a multicategory whose 'objects-object' is 1.

iv) In [7] Hermida, Makkai and Power use the term 'multitope' for the objects constructed in analogy with the 'opetopes' of [3]. This is intended to reflect the fact that opetopes are constructed using operads but multitopes using multicategories, a distinction that we have removed by using the term 'multicategory' in both cases. However, we continue to use the term 'opetope' and furthermore, use it in general to refer to the analogous objects constructed in each of the three theories. Note also that Leinster uses the term 'opetope' to describe objects which are analogous but not a priori the same; we refer to these as 'Leinster opetopes' if clarification is needed.

v) We regard sets as sets or discrete categories with no notational distinction.

**Acknowledgements**

This work was supported by a PhD grant from EPSRC. I would like to thank Martin Hyland and Tom Leinster for their support and guidance.

---

### النسخة العربية

في [3]، يُقدم باييز ودولان تعريفاً لفئة n الضعيفة حيث تكون الأشكال الأساسية للخلايا هي 'أوبتوبات' والبيانات الأساسية مُعطاة بواسطة 'المجموعات الأوبتوبية'. الفكرة هي أن المجموعات الأوبتوبية يجب أن تكون حزماً أمامية على فئة الأوبتوبات. ومع ذلك، لم يبنِ باييز ودولان صراحةً فئة الأوبتوبات، لذا تُعرَّف المجموعات الأوبتوبية مباشرةً بدلاً من ذلك. تُلمَّح إلى علاقة بين هذه الفئة من المجموعات الأوبتوبية وفئة من الحزم الأمامية لكن دون إثبات.

النتيجة الرئيسية لهذه الورقة هي أن فئة المجموعات الأوبتوبية مكافئة لفئة الحزم الأمامية على فئة الأوبتوبات. ومع ذلك، لا نستخدم التعريفات الأوبتوبية كما هي مُعطاة في [3] بالضبط، بل نستمر في استخدام التعديلات المُقدمة في أعمالنا السابقة ([6]، [5]). في هذه الأوراق نستخدم تعميماً على الخطوط التي بدأها المؤلفون الأصليون، لكنهم اختاروا التخلي عنها لأسباب غير واضحة. يمكِّننا هذا التعميم، في [6]، من إظهار علاقة مع عمل هيرميدا وماكاي وباور ([7]) وفي [5]، مع عمل لينستر ([13]). بالنظر إلى هذه النتائج المفيدة، نستمر في دراسة النظرية المعدلة في هذا العمل.

نبدأ، في القسم 1، بإعطاء بناء صريح لفئة الأوبتوبات. الفكرة كما يلي. في [6] بنينا، لكل k ≥ 0، فئة ℂₖ من k-أوبتوبات. بالنسبة لفئة **Opetope** من الأوبتوبات من جميع الأبعاد، يجب أن تكون كل فئة ℂₖ فئة جزئية كاملة من **Opetope**؛ علاوة على ذلك، يجب أن تكون هناك 'دوال الوجوه' التي تُظهر m-أوبتوبات المكونة، أو 'وجوه' k-أوبتوب، لـ m ≤ k. نشير إلى وجوه m-أوبتوب بـ m-وجوه. لاحظ أنه لا توجد دوال تدهور.

يجب أن تكون الوجوه (k − 1) لـ k-أوبتوب α هي (k − 1)-أوبتوبات مصدره وهدفه؛ يجب أن تكون هذه كلها مميزة. ثم كل من هذه الوجوه له وجوهه (k − 2) الخاصة، لكن جميع هذه (k − 2)-أوبتوبات لا يجب بالضرورة اعتبارها وجوه (k − 2) مميزة في α. لأن α هو تكوين لتركيب وجوهه (k − 1) عند وجوههم (k − 2)، لذا يجب تحديد وجوه (k − 2) مع بعضها البعض في الأماكن التي سيحدث فيها التركيب. أي أن دوال الوجوه المركبة من هذه (k−2)-أوبتوبات إلى α يجب أن تكون متساوية. بعض التفاصيل الإضافية مطلوبة بعد ذلك للتعامل مع النسخ المتشاكلة من الأوبتوبات.

تذكر أن 'التكوين' لتركيب (k −1)-أوبتوبات يُعبَّر عنه كشجرة (انظر [6]) تُوسَم عُقدها بـ (k−1)-أوبتوبات المعنية، مع إعطاء الحواف مدخلاتها ومخرجاتها. لذا يحدث التركيب على طول كل حافة من الشجرة، عبر علامة كائن-تشاكل، وبالتالي تخبرنا الشجرة بأي (k − 1)-أوبتوبات يتم تحديدها.

من أجل التعبير عن هذا بشكل أكثر دقة، نعطي أولاً وصفاً أكثر رسمية للأشجار (القسم 1.2). في الواقع، يؤدي هذا إلى وصف تجريدي للأشجار كرسوم بيانية معينة لكيلي-ماك لين؛ هذا هو موضوع [4]. وبالتالي فإن نتائج القسم 1.2 تنشأ كنتائج تمهيدية في [4] ونحيل القارئ إلى هذه الورقة للحساب الكامل والبراهين.

في القسم 2، نفحص نظرية المجموعات الأوبتوبية. نبدأ بمتابعة تعديلاتنا على النظرية الأوبتوبية لتضمين نظرية المجموعات الأوبتوبية. (تعاملت أعمالنا السابقة فقط مع نظرية الأوبتوبات.) ثم نستخدم نتائج [12] لإثبات أن فئة المجموعات الأوبتوبية مكافئة بالفعل لفئة الحزم الأمامية على O، فئة الأوبتوبات المعرفة في القسم 1. هذه هي النتيجة الرئيسية لهذا العمل.

أخيراً، يستحق التعليق على مفهوم 'المالتيتوب' كما هو معرَّف في [7]. في هذا العمل، يبدأ هيرميدا وماكاي وباور تعريفاً لفئة n مماثلاً صراحةً لتعريف [3]، مع كون المفاهيم المماثلة 'مالتيتوبات' و'المجموعات المالتيتوبية'. في [6] نُثبت أن 'الأوبتوبات والمالتيتوبات متطابقة حتى التشاكل'، أي أنه لكل k ≥ 0، فئة k-أوبتوبات مكافئة لفئة (المنفصلة) من k-مالتيتوبات. في [7]، يستمر هيرميدا وماكاي وباور في إعطاء تعريف صريح للفئة المماثلة **Multitope**، من المالتيتوبات. بالنظر إلى التكافؤات أعلاه، وبافتراض أن الفكرة الأساسية هي نفسها، سيكون هذا مكافئاً لفئة **Opetope**، لكننا لا نحاول إثبات ذلك في هذا العمل.

**المصطلحات**

i) نظراً لأننا نهتم بشكل أساسي بفئات n الضعيفة، نتبع باييز ودولان ([3]) ونحذف كلمة 'ضعيفة' ما لم يُطلب التأكيد؛ نشير إلى فئات n الصارمة بـ 'فئات n صارمة'.

ii) نستخدم مصطلح 'دالة تصنيفية n ضعيفة' لدالة تصنيفية n حيث تنطبق الدالية حتى التشاكلات المتماسكة، و'دالة ضعيفة لاكس' عندما لا تكون القيود قابلة للعكس بالضرورة.

iii) في [3] يستخدم باييز ودولان مصطلحي 'أوبيراد' و'أنواع' حيث نستخدم 'تعدد فئوي' و'كائنات'؛ المصطلحات الأخيرة أكثر اتساقاً مع استخدام لينستر لـ 'أوبيراد' لوصف تعدد فئوي يكون 'كائن-الكائنات' فيه هو 1.

iv) في [7] يستخدم هيرميدا وماكاي وباور مصطلح 'مالتيتوب' للكائنات المبنية بالقياس مع 'أوبتوبات' [3]. هذا يهدف إلى عكس حقيقة أن الأوبتوبات تُبنى باستخدام أوبيرادات لكن المالتيتوبات باستخدام تعدد فئوي، وهو تمييز قمنا بإزالته باستخدام مصطلح 'تعدد فئوي' في كلتا الحالتين. ومع ذلك، نستمر في استخدام مصطلح 'أوبتوب' وعلاوة على ذلك، نستخدمه بشكل عام للإشارة إلى الكائنات المماثلة المبنية في كل من النظريات الثلاث. لاحظ أيضاً أن لينستر يستخدم مصطلح 'أوبتوب' لوصف كائنات مماثلة لكن ليست بالضرورة نفسها؛ نشير إلى هذه بـ 'أوبتوبات لينستر' إذا كانت هناك حاجة للتوضيح.

v) نعتبر المجموعات كمجموعات أو فئات منفصلة بدون تمييز في الترميز.

**شكر وتقدير**

تم دعم هذا العمل بمنحة دكتوراه من EPSRC. أود أن أشكر مارتن هايلاند وتوم لينستر على دعمهم وتوجيههم.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** weak n-category (فئة n ضعيفة), opetopic sets (المجموعات الأوبتوبية), face maps (دوال الوجوه), degeneracy maps (دوال تدهور), multitope (مالتيتوب), Kelly-Mac Lane graphs (رسوم بيانية لكيلي-ماك لين)
- **Equations:** 0
- **Citations:** Multiple references to works [3], [4], [5], [6], [7], [12], [13]
- **Special handling:**
  - Category names kept in English as proper nouns (Opetope, Multitope)
  - Mathematical notation preserved (k ≥ 0, ℂₖ, etc.)
  - Reference numbers preserved as in original

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87
