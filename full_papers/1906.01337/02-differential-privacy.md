# Section 2: Differential Privacy / القسم 2: الخصوصية التفاضلية

**Section:** 2. Differential Privacy
**Arabic Translation:** 2. الخصوصية التفاضلية
**Quality Score:** 0.93
**Source:** Translated from paper.pdf pages 5-9

---

## English

In this chapter we recap the original DP definition with its basic properties, define how definitions can related to each other and introduce our dimensions along which DP can be modified.

Let T denote an arbitrary set of possible records. We typically use t to denote the records themselves. A dataset is a finite indexed family of records. We denote by D space of possible datasets, individuals datasets are typically called D, D', D₁ or D₂. The indices of a dataset are typically called i and j, with D(i) referring to the i-th record of a dataset D. We denote by D₋ᵢ the dataset D whose i-th record has been removed.

Let O denote an arbitrary set of possible outputs; outputs are typically called O, and sets of outputs called S. A mechanism is a randomized function which takes a dataset as input and returns an output. Mechanisms are typically called M while M(D) is usually a random variable.

Probability distributions on T are called π, probability distribution on D are called θ, and family of probability distributions on D are called Θ. Given some property φ, let M(D)|D∼θ,φ denote the random variable corresponding to the output of M(D), when D is drawn from a distribution θ conditioned on φ.

Table 1 summarizes the notations used throughout the paper.

**2.1 The original version**

The first DP mechanism, randomized response, was proposed in 1965, and data privacy definitions that are a property of a mechanism and not of the output dataset were already proposed in as early as 2003. However, DP and the related notion of ε-indistinguishability were first formally defined in 2006.

**Definition 1 (ε-indistinguishability).** Two random variables A and B are ε-indistinguishable, denoted A ≈ε B, if for all measurable sets X of possible events:
P[A ∈ X] ≤ eᵉ · P[B ∈ X] and P[B ∈ X] ≤ eᵉ · P[A ∈ X].

Informally, A and B are ε-indistinguishable if their distributions are "close". This notion originates from the cryptographic notion of indistinguishability. A similar notion, (1, ε)-privacy, was defined in [CM06], where (1 + ε) used in place of eᵉ, and it was also called log-ratio distance in [HMSS19].

The notion of ε-indistinguishability is then used to define differential privacy.

**Definition 2 (ε-differential privacy).** A privacy mechanism M is ε-differential private (or ε-DP) if for all datasets D₁ and D₂ that differ only in one record, M(D₁) ≈ε M(D₂).

**Mechanisms**

Besides the random response mechanism (which returns the true value with probability p and returns a random value otherwise) in general there are three places where noise can be injected to guarantee DP: it can be added to the input, to the output, and directly to the mechanism. For instance, in machine learning context input (e.g., [PAE+16]) and output (e.g., [PTB19]) pertubation are equivalent with sanitizing the dataset before and the predictions after the training respectively. Concerning mechanism pertubation, there are various techniques, such as loss function perturbation (e.g., [CMS11]), and gradient perturbation (e.g., [ACG+16]), which insert noise to the model objective and update respectively.

The most widely used distributions the noise is sampled from are Laplace, Gauss, and Exponential. Using the first and last makes any underlying mechanism to satisfy ε-DP for continious and discrete cases, however, they could result in large added noise. On the contrary, the middle distribution decrease the probability of such events significantly, but the obtained differential privacy guarantee is weaker (i.e. (ε, δ)-DP, introduced in Section 3.

**2.2 Dimensions**

Variants and extensions of differential privacy modify the original definition in various ways. To establish a comprehensive taxonomy, a natural approach is to partition them into categories, depending on which aspect of the definition they change. Unfortunately, this approach fails for privacy definitions, many of which modify several aspects at once, so it is impossible to have a categorization such that every definition falls neatly into only one category.

The approach we take is to define dimensions along which the original definition can be modified. Each variant or extension of DP can be seen as a point in a multidimensional space, where each coordinate corresponds to one possible way of changing the definition along a particular dimension. To make this representation possible, our dimensions need to satisfy two properties:

- **Mutual compatibility**: definitions that vary along different dimensions can be combined to form a new, meaningful definition.
- **Inner exclusivity**: definitions in the same dimension cannot be combined to form a new, meaningful definition (but they can be pairwise comparable).

In addition, each dimension should be motivatable: there should be an intuitive explanation of what it means to modify DP along each dimension. Moreover, each possible choice within a dimension should be similarly understandable, to allow new practitioners to determine quickly which kind of definition they should use or study, depending on their use case.

We introduce our dimensions by reformulating the guarantee offered by DP, highlighting aspects that have been modified by its variants or extensions. Each dimension is attributed a letter, and we note the dimension letter corresponding to each highlight. This formulation considers the point of view of an attacker, trying to find out some sensitive information about some input data using the output of a mechanism.

**An attacker with perfect background knowledge (B) and unbounded computation power (C) is unable (R) to distinguish (F) anything about an individual (N), uniformly across users (V) even in the worst-case scenario (Q).**

This informal definition of DP with the seven highlighted aspects give us seven distinct dimensions. We denote each one by a letter and summarize them in Table 2. Each is introduced in its corresponding section.

Note that the interpretation of DP is subject to some debate. In [TSD20], authors summarize this debate, and show that DP can be interpreted under two possible lenses: it can be seen as an associative property, or as a causal property. The difference between the two interpretations is particularly clear when one supposes that the input dataset is modeled as being generated by a probability distribution.

- In the **associative view**, this probability distribution is conditioned upon the value of one record. If the distribution has correlations, this change can affect other records as well.
- In the **causal view**, the dataset is first generated, and the value of one record is then changed before computing the result of the mechanism.

While the causal view does not require any additional assumption to capture the intuition behind DP, the associative view requires that either all records are independent in the original probability distribution (the independence assumption), or the adversary must know all data points except one (the strong adversary assumption, which we picked in the reformulation above).

These considerations can have a significant impact on DP variants and extensions, either leading to distinct variants that attempt to capture the same intuition, or to the same variant being interpreted in different ways.

**2.3 Properties**

In this section, we introduce three main properties of differential privacy, that we then check against variants and extensions of DP listed in this work.

**Privacy Axioms**

Two important properties of data privacy notions are called privacy axioms, proposed in [KL10, KL12]. These are not axioms in a sense that they assumed to be true; rather, they are consistency checks: properties that, if not satisfied by a data privacy definition, indicate a flaw in the definition.

**Definition 3 (Privacy axioms).**

1. **Post-processing** (or transformation invariance): A privacy definition Def satisfies the post-processing axiom if, for any mechanism M satisfying Def and any probabilistic function f, the mechanism D → f(M(D)) also satisfies Def.

2. **Convexity** (or privacy axiom of choice): A privacy definition Def satisfies the convexity axiom if, for any two mechanisms M₁ and M₂ satisfying Def, the mechanism M defined by M(D) = M₁(D) with probability p and M(D) = M₂(D) with probability 1 − p also satisfies Def.

Most differential privacy variants and extensions, including the original definition of DP, satisfy these axioms, although some do not. We highlighted these in Table 3 in Section 10.

**Composition**

A third important property is one of differential privacy's main strengths: composability. It guarantees that the output of two mechanisms satisfying a privacy definition still satisfies the definition, typically with a change in parameters. There are several types of composition: parallel composition, sequential composition, and adaptive composition. We introduce the first two below.

**Theorem (Parallel composition).** Let M₁ be a ε₁-differentially private mechanism, and M₂ a ε₂-differentially private mechanism. For any dataset D, let D₁ and D₂ be the result of an operation that separates records in two disjoint datasets. Then the mechanism M defined by M(D) = (M₁(D₁),M₂(D₂)) is max(ε₁, ε₂)-differentially private.

This property allows us to build locally differentially private mechanisms, in which a central server can compute global statistics without accessing the raw data from each user. In this work, we focus on sequential composition, which we simply call composition.

**Theorem (Sequential composition).** Let M₁ be a ε₁-differentially private mechanism, and M₂ a ε₂-differentially private mechanism. Then the mechanism M defined by M(D) = (M₁(D),M₂(D)) is (ε₁ + ε₂)-differentially private.

This theorem stays true if M₂ depends on the value of M₁(D): this variant is called adaptative composition. This latter property allows to quantify the gain of information over time of an attacker interacting with a differentially private query engine.

In this work, we only consider sequential composition, in the more abstract form formalized below.

**Definition 4 (Composability).** A privacy definition Def with parameter α is composable if for any two mechanisms M₁ and M₂ satisfying respectively α₁-Def and α₂-Def, the mechanism M(D) = (M₁(D),M₂(D)) satisfies α-Def for some (non-trivial) α.

**2.4 Relations between definitions**

When learning about a new data privacy notion, it is often useful to know what are the known relations between this notion and other definitions. However, definitions have parameters that often have different meanings, and whose value is not directly comparable. To capture extensions, when a definition can be seen as a special case of another, we introduce the following definition.

**Definition 5 (Extensions).** Let α-Def₁ and β-Def₂ be data privacy definitions. We say that Def₁ is extended by Def₂, and denote is as Def₁ ⊂ Def₂, if for all α, there is a value of β such that α-Def₁ is identical to β-Def₂.

Concerning variants, to claim that a definition is stronger than another, we adopt the concept of ordering established in [CY16] using α and β as tuples, encoding multiple parameters. Note that we slightly changed the original definition as that only required the second condition to hold, which would classify any extension as a stronger variant.

**Definition 6 (Relative strength of privacy definitions).** Let α-Def₁ and β-Def₂ be data privacy definitions. We say that Def₁ is stronger than Def₂, and denote it Def₁ ≻ Def₂, if:

1. for all α, there is a β such that α-Def₁ ⟹ β-Def₂;
2. for all β, there is an α such that α-Def₁ ⟹ β-Def₂.

If Def₁ is both stronger than and weaker than Def₂, we say that the two definitions are equivalent, and denote it Def₁ ∼ Def₂.

Relative strength implies a partial ordering on the space of possible definitions. On the other hand, if two definitions are equivalent, this does not mean that they are equal: they could be only equal up to a change in parameters. Both relations are reflexive and transitive; and we define the symmetric counterpart of these relations as well (i.e., ≺ and ⊃). Moreover, for brevity, we combine these two concepts in a single notation: if Def₁ ⊂ Def₂ and Def₁ ≻ Def₂, we say that Def₂ is a weaker extension of Def₁, and denote it Def₁ ⊂≺ Def₂.

A summarizing table is presented at the end of this work, where for each definition, we also highlight its dimensions and its relation to other notions. In Table 3, we also specify whether these notions satisfy the privacy axioms and the composability property (✓: yes, ✗: no, ?: currently unknown); in Section 10 we either provide a reference or a novel proof for each of these claims.

---

## Arabic / العربية

في هذا الفصل نستعرض التعريف الأصلي للخصوصية التفاضلية مع خصائصه الأساسية، ونحدد كيف يمكن أن ترتبط التعريفات ببعضها البعض ونقدم أبعادنا التي يمكن على طولها تعديل الخصوصية التفاضلية.

لتكن T مجموعة عشوائية من السجلات الممكنة. نستخدم عادةً t للإشارة إلى السجلات نفسها. مجموعة البيانات هي عائلة محدودة ومفهرسة من السجلات. نشير بـ D إلى مساحة مجموعات البيانات الممكنة، وتسمى مجموعات البيانات الفردية عادةً D أو D' أو D₁ أو D₂. تسمى فهارس مجموعة البيانات عادةً i و j، حيث يشير D(i) إلى السجل i-th من مجموعة البيانات D. نشير بـ D₋ᵢ إلى مجموعة البيانات D التي تم إزالة سجلها i-th.

لتكن O مجموعة عشوائية من المخرجات الممكنة؛ تسمى المخرجات عادةً O، ومجموعات المخرجات تسمى S. الآلية هي دالة عشوائية تأخذ مجموعة بيانات كمدخل وتعيد مخرجاً. تسمى الآليات عادةً M بينما M(D) عادةً ما يكون متغيراً عشوائياً.

تسمى توزيعات الاحتمالات على T بـ π، وتوزيع الاحتمالات على D يسمى θ، وعائلة توزيعات الاحتمالات على D تسمى Θ. بالنظر إلى خاصية ما φ، دع M(D)|D∼θ,φ تشير إلى المتغير العشوائي المقابل لمخرجات M(D)، عندما يتم سحب D من توزيع θ مشروط بـ φ.

يلخص الجدول 1 الترميزات المستخدمة في جميع أنحاء البحث.

**2.1 النسخة الأصلية**

تم اقتراح أول آلية للخصوصية التفاضلية، الاستجابة العشوائية، في عام 1965، وتم اقتراح تعريفات خصوصية البيانات التي هي خاصية للآلية وليست لمجموعة البيانات الناتجة في وقت مبكر من عام 2003. ومع ذلك، تم تعريف الخصوصية التفاضلية والمفهوم ذي الصلة لعدم التمييز-ε رسمياً لأول مرة في عام 2006.

**التعريف 1 (عدم التمييز-ε).** يكون المتغيران العشوائيان A و B غير قابلين للتمييز-ε، ويُرمز له A ≈ε B، إذا كان لجميع المجموعات القابلة للقياس X من الأحداث الممكنة:
P[A ∈ X] ≤ eᵉ · P[B ∈ X] و P[B ∈ X] ≤ eᵉ · P[A ∈ X].

بشكل غير رسمي، A و B غير قابلين للتمييز-ε إذا كانت توزيعاتهما "قريبة". ينشأ هذا المفهوم من المفهوم التشفيري لعدم التمييز. تم تعريف مفهوم مماثل، (1, ε)-خصوصية، في [CM06]، حيث يتم استخدام (1 + ε) بدلاً من eᵉ، وتم تسميته أيضاً بمسافة نسبة اللوغاريتم في [HMSS19].

ثم يُستخدم مفهوم عدم التمييز-ε لتعريف الخصوصية التفاضلية.

**التعريف 2 (الخصوصية التفاضلية-ε).** تكون آلية الخصوصية M خاصة تفاضلياً-ε (أو ε-DP) إذا كان لجميع مجموعات البيانات D₁ و D₂ التي تختلف فقط في سجل واحد، M(D₁) ≈ε M(D₂).

**الآليات**

إلى جانب آلية الاستجابة العشوائية (التي تعيد القيمة الحقيقية باحتمال p وتعيد قيمة عشوائية خلاف ذلك)، بشكل عام هناك ثلاثة أماكن حيث يمكن حقن الضوضاء لضمان الخصوصية التفاضلية: يمكن إضافتها إلى المدخل، أو إلى المخرج، أو مباشرة إلى الآلية. على سبيل المثال، في سياق التعلم الآلي، الاضطراب في المدخل (على سبيل المثال، [PAE+16]) والمخرج (على سبيل المثال، [PTB19]) يعادل تعقيم مجموعة البيانات قبل وبعد التدريب على التوالي. فيما يتعلق باضطراب الآلية، هناك تقنيات مختلفة، مثل اضطراب دالة الخسارة (على سبيل المثال، [CMS11])، واضطراب التدرج (على سبيل المثال، [ACG+16])، التي تُدخل ضوضاء إلى هدف النموذج والتحديث على التوالي.

التوزيعات الأكثر استخداماً التي يتم أخذ عينات الضوضاء منها هي لابلاس وغاوس والأسية. استخدام الأول والأخير يجعل أي آلية أساسية تحقق ε-DP للحالات المستمرة والمنفصلة، ومع ذلك، يمكن أن ينتج عنها ضوضاء مضافة كبيرة. على العكس من ذلك، يقلل التوزيع الأوسط من احتمالية مثل هذه الأحداث بشكل كبير، لكن ضمان الخصوصية التفاضلية المحصل عليه أضعف (أي (ε, δ)-DP، الذي سيتم تقديمه في القسم 3).

**2.2 الأبعاد**

تقوم متغيرات وإضافات الخصوصية التفاضلية بتعديل التعريف الأصلي بطرق مختلفة. لإنشاء تصنيف شامل، النهج الطبيعي هو تقسيمها إلى فئات، اعتماداً على الجانب الذي تغيره من التعريف. لسوء الحظ، يفشل هذا النهج بالنسبة لتعريفات الخصوصية، حيث أن العديد منها تعدل عدة جوانب في وقت واحد، لذلك من المستحيل الحصول على تصنيف بحيث يقع كل تعريف بدقة في فئة واحدة فقط.

النهج الذي نتبعه هو تحديد الأبعاد التي يمكن على طولها تعديل التعريف الأصلي. يمكن رؤية كل متغير أو إضافة للخصوصية التفاضلية كنقطة في فضاء متعدد الأبعاد، حيث يتوافق كل إحداثي مع طريقة ممكنة واحدة لتغيير التعريف على طول بُعد معين. لجعل هذا التمثيل ممكناً، يجب أن تلبي أبعادنا خاصيتين:

- **التوافق المتبادل**: يمكن دمج التعريفات التي تختلف على طول أبعاد مختلفة لتشكيل تعريف جديد وذي معنى.
- **الحصرية الداخلية**: لا يمكن دمج التعريفات في نفس البُعد لتشكيل تعريف جديد وذي معنى (لكن يمكن مقارنتها على أزواج).

بالإضافة إلى ذلك، يجب أن يكون كل بُعد قابلاً للتحفيز: يجب أن يكون هناك تفسير بديهي لما يعنيه تعديل الخصوصية التفاضلية على طول كل بُعد. علاوة على ذلك، يجب أن يكون كل خيار ممكن ضمن بُعد قابلاً للفهم بالمثل، للسماح للممارسين الجدد بتحديد نوع التعريف الذي يجب عليهم استخدامه أو دراسته بسرعة، اعتماداً على حالة الاستخدام الخاصة بهم.

نقدم أبعادنا من خلال إعادة صياغة الضمان الذي تقدمه الخصوصية التفاضلية، مع تسليط الضوء على الجوانب التي تم تعديلها بواسطة متغيراتها أو إضافاتها. يُنسب لكل بُعد حرف، ونلاحظ حرف البُعد المقابل لكل تسليط ضوء. تأخذ هذه الصياغة في الاعتبار وجهة نظر المهاجم، الذي يحاول معرفة بعض المعلومات الحساسة حول بعض بيانات الإدخال باستخدام مخرجات الآلية.

**المهاجم الذي لديه معرفة خلفية كاملة (B) وقوة حسابية غير محدودة (C) غير قادر (R) على التمييز (F) بين أي شيء عن فرد (N)، بشكل موحد عبر المستخدمين (V) حتى في السيناريو الأسوأ (Q).**

يعطينا هذا التعريف غير الرسمي للخصوصية التفاضلية مع الجوانب السبعة المميزة سبعة أبعاد متميزة. نشير إلى كل واحد بحرف ونلخصها في الجدول 2. يتم تقديم كل منها في القسم المقابل له.

لاحظ أن تفسير الخصوصية التفاضلية يخضع لبعض النقاش. في [TSD20]، يلخص المؤلفون هذا النقاش، ويظهرون أن الخصوصية التفاضلية يمكن تفسيرها تحت عدستين محتملتين: يمكن رؤيتها كخاصية ترابطية، أو كخاصية سببية. الفرق بين التفسيرين واضح بشكل خاص عندما يفترض المرء أن مجموعة بيانات الإدخال يتم نمذجتها على أنها تم إنشاؤها بواسطة توزيع احتمالي.

- في **النظرة الترابطية**، يتم تكييف توزيع الاحتمالات هذا على قيمة سجل واحد. إذا كان للتوزيع ارتباطات، فإن هذا التغيير يمكن أن يؤثر على السجلات الأخرى أيضاً.
- في **النظرة السببية**، يتم أولاً إنشاء مجموعة البيانات، ثم يتم تغيير قيمة سجل واحد قبل حساب نتيجة الآلية.

بينما لا تتطلب النظرة السببية أي افتراض إضافي لالتقاط الحدس وراء الخصوصية التفاضلية، تتطلب النظرة الترابطية إما أن تكون جميع السجلات مستقلة في توزيع الاحتمالات الأصلي (افتراض الاستقلالية)، أو يجب على الخصم معرفة جميع نقاط البيانات باستثناء واحدة (افتراض الخصم القوي، الذي اخترناه في إعادة الصياغة أعلاه).

يمكن أن يكون لهذه الاعتبارات تأثير كبير على متغيرات وإضافات الخصوصية التفاضلية، إما أن تؤدي إلى متغيرات متميزة تحاول التقاط نفس الحدس، أو إلى تفسير نفس المتغير بطرق مختلفة.

**2.3 الخصائص**

في هذا القسم، نقدم ثلاث خصائص رئيسية للخصوصية التفاضلية، التي نتحقق منها بعد ذلك ضد متغيرات وإضافات الخصوصية التفاضلية المدرجة في هذا العمل.

**بديهيات الخصوصية**

تسمى خاصيتان مهمتان لمفاهيم خصوصية البيانات ببديهيات الخصوصية، المقترحة في [KL10, KL12]. هذه ليست بديهيات بمعنى أنه يُفترض أن تكون صحيحة؛ بل هي فحوصات اتساق: خصائص، إذا لم يتم استيفاؤها بواسطة تعريف خصوصية البيانات، تشير إلى عيب في التعريف.

**التعريف 3 (بديهيات الخصوصية).**

1. **المعالجة اللاحقة** (أو ثبات التحويل): يلبي تعريف الخصوصية Def بديهية المعالجة اللاحقة إذا، لأي آلية M تلبي Def وأي دالة احتمالية f، فإن الآلية D → f(M(D)) تلبي أيضاً Def.

2. **التحدب** (أو بديهية اختيار الخصوصية): يلبي تعريف الخصوصية Def بديهية التحدب إذا، لأي آليتين M₁ و M₂ تلبيان Def، فإن الآلية M المحددة بـ M(D) = M₁(D) باحتمال p و M(D) = M₂(D) باحتمال 1 − p تلبي أيضاً Def.

تلبي معظم متغيرات وإضافات الخصوصية التفاضلية، بما في ذلك التعريف الأصلي للخصوصية التفاضلية، هذه البديهيات، على الرغم من أن بعضها لا يفعل ذلك. سلطنا الضوء على هذه في الجدول 3 في القسم 10.

**التركيب**

الخاصية الثالثة المهمة هي أحد نقاط القوة الرئيسية للخصوصية التفاضلية: قابلية التركيب. تضمن أن مخرجات آليتين تلبيان تعريف خصوصية لا تزال تلبي التعريف، عادةً مع تغيير في المعاملات. هناك عدة أنواع من التركيب: التركيب المتوازي، والتركيب التسلسلي، والتركيب التكيفي. نقدم الأولين أدناه.

**نظرية (التركيب المتوازي).** لتكن M₁ آلية خاصة تفاضلياً-ε₁، و M₂ آلية خاصة تفاضلياً-ε₂. لأي مجموعة بيانات D، لتكن D₁ و D₂ نتيجة عملية تفصل السجلات إلى مجموعتي بيانات منفصلتين. عندئذٍ تكون الآلية M المحددة بـ M(D) = (M₁(D₁),M₂(D₂)) خاصة تفاضلياً-max(ε₁, ε₂).

تسمح هذه الخاصية لنا ببناء آليات خاصة تفاضلياً محلياً، حيث يمكن لخادم مركزي حساب إحصائيات عامة دون الوصول إلى البيانات الخام من كل مستخدم. في هذا العمل، نركز على التركيب التسلسلي، الذي نسميه ببساطة التركيب.

**نظرية (التركيب التسلسلي).** لتكن M₁ آلية خاصة تفاضلياً-ε₁، و M₂ آلية خاصة تفاضلياً-ε₂. عندئذٍ تكون الآلية M المحددة بـ M(D) = (M₁(D),M₂(D)) خاصة تفاضلياً-(ε₁ + ε₂).

تظل هذه النظرية صحيحة إذا كانت M₂ تعتمد على قيمة M₁(D): يسمى هذا المتغير التركيب التكيفي. تسمح هذه الخاصية الأخيرة بقياس كسب المعلومات بمرور الوقت لمهاجم يتفاعل مع محرك استعلام خاص تفاضلياً.

في هذا العمل، نعتبر فقط التركيب التسلسلي، في الشكل الأكثر تجريداً المُشكَّل أدناه.

**التعريف 4 (قابلية التركيب).** يكون تعريف الخصوصية Def بمعامل α قابلاً للتركيب إذا كان لأي آليتين M₁ و M₂ تلبيان α₁-Def و α₂-Def على التوالي، فإن الآلية M(D) = (M₁(D),M₂(D)) تلبي α-Def لبعض α (غير تافه).

**2.4 العلاقات بين التعريفات**

عند التعرف على مفهوم خصوصية بيانات جديد، غالباً ما يكون من المفيد معرفة ما هي العلاقات المعروفة بين هذا المفهوم والتعريفات الأخرى. ومع ذلك، التعريفات لها معاملات غالباً ما يكون لها معانٍ مختلفة، وقيمتها غير قابلة للمقارنة مباشرة. للالتقاط الإضافات، عندما يمكن رؤية تعريف كحالة خاصة من آخر، نقدم التعريف التالي.

**التعريف 5 (الإضافات).** لتكن α-Def₁ و β-Def₂ تعريفات خصوصية بيانات. نقول إن Def₁ يتم توسيعه بواسطة Def₂، ونشير إليه كـ Def₁ ⊂ Def₂، إذا كان لجميع α، هناك قيمة β بحيث α-Def₁ مطابق لـ β-Def₂.

فيما يتعلق بالمتغيرات، للادعاء بأن تعريفاً أقوى من آخر، نعتمد مفهوم الترتيب المُنشأ في [CY16] باستخدام α و β كمجموعات، لترميز معاملات متعددة. لاحظ أننا قمنا بتغيير التعريف الأصلي قليلاً حيث أن ذلك يتطلب فقط الشرط الثاني للاحتفاظ به، مما قد يصنف أي إضافة كمتغير أقوى.

**التعريف 6 (القوة النسبية لتعريفات الخصوصية).** لتكن α-Def₁ و β-Def₂ تعريفات خصوصية بيانات. نقول إن Def₁ أقوى من Def₂، ونشير إليه Def₁ ≻ Def₂، إذا:

1. لجميع α، هناك β بحيث α-Def₁ ⟹ β-Def₂;
2. لجميع β، هناك α بحيث α-Def₁ ⟹ β-Def₂.

إذا كان Def₁ أقوى من وأضعف من Def₂، نقول إن التعريفين متكافئان، ونشير إليه Def₁ ∼ Def₂.

تشير القوة النسبية إلى ترتيب جزئي على مساحة التعريفات الممكنة. من ناحية أخرى، إذا كان تعريفان متكافئين، فهذا لا يعني أنهما متساويان: يمكن أن يكونا متساويين فقط حتى تغيير في المعاملات. كلتا العلاقتين انعكاسية ومتعدية؛ ونحدد النظير المتماثل لهذه العلاقات أيضاً (أي، ≺ و ⊃). علاوة على ذلك، من أجل الإيجاز، نجمع هذين المفهومين في ترميز واحد: إذا كان Def₁ ⊂ Def₂ و Def₁ ≻ Def₂، نقول إن Def₂ هي إضافة أضعف لـ Def₁، ونشير إليها Def₁ ⊂≺ Def₂.

يتم عرض جدول ملخص في نهاية هذا العمل، حيث نسلط الضوء أيضاً لكل تعريف على أبعاده وعلاقته بالمفاهيم الأخرى. في الجدول 3، نحدد أيضاً ما إذا كانت هذه المفاهيم تلبي بديهيات الخصوصية وخاصية قابلية التركيب (✓: نعم، ✗: لا، ?: غير معروف حالياً)؛ في القسم 10 نقدم إما مرجعاً أو برهاناً جديداً لكل من هذه الادعاءات.

---

## Back-Translation (Validation)

In this chapter we review the original DP definition with its basic properties, define how definitions can be related to each other and present our dimensions along which DP can be modified.

Let T be an arbitrary set of possible records. We typically use t to refer to the records themselves. A dataset is a finite indexed family of records. We denote by D the space of possible datasets, individual datasets are typically called D, D', D₁ or D₂. The indices of a dataset are typically called i and j, where D(i) refers to the i-th record of dataset D. We denote by D₋ᵢ the dataset D whose i-th record has been removed.

Let O be an arbitrary set of possible outputs; outputs are typically called O, and sets of outputs are called S. A mechanism is a randomized function that takes a dataset as input and returns an output. Mechanisms are typically called M while M(D) is usually a random variable.

Probability distributions on T are called π, probability distribution on D is called θ, and family of probability distributions on D are called Θ. Given some property φ, let M(D)|D∼θ,φ denote the random variable corresponding to the output of M(D), when D is drawn from a distribution θ conditioned on φ.

Table 1 summarizes the notations used throughout the paper.

**2.1 The Original Version**

The first mechanism for differential privacy, randomized response, was proposed in 1965, and data privacy definitions that are a property of the mechanism and not of the resulting dataset were proposed as early as 2003. However, differential privacy and the related concept of ε-indistinguishability were formally defined for the first time in 2006.

**Definition 1 (ε-indistinguishability).** Two random variables A and B are ε-indistinguishable, denoted A ≈ε B, if for all measurable sets X of possible events:
P[A ∈ X] ≤ eᵉ · P[B ∈ X] and P[B ∈ X] ≤ eᵉ · P[A ∈ X].

Informally, A and B are ε-indistinguishable if their distributions are "close". This concept originates from the cryptographic concept of indistinguishability. A similar concept, (1, ε)-privacy, was defined in [CM06], where (1 + ε) is used instead of eᵉ, and it was also called logarithm ratio distance in [HMSS19].

The concept of ε-indistinguishability is then used to define differential privacy.

**Definition 2 (ε-differential privacy).** A privacy mechanism M is ε-differentially private (or ε-DP) if for all datasets D₁ and D₂ that differ only in one record, M(D₁) ≈ε M(D₂).

**Mechanisms**

Besides the randomized response mechanism (which returns the true value with probability p and returns a random value otherwise), in general there are three places where noise can be injected to ensure differential privacy: it can be added to the input, to the output, or directly to the mechanism. For example, in the machine learning context, input perturbation (e.g., [PAE+16]) and output (e.g., [PTB19]) are equivalent to sanitizing the dataset before and after training respectively. Regarding mechanism perturbation, there are various techniques, such as loss function perturbation (e.g., [CMS11]), and gradient perturbation (e.g., [ACG+16]), which insert noise into the model objective and update respectively.

The most widely used distributions from which noise is sampled are Laplace, Gauss, and Exponential. Using the first and last makes any underlying mechanism satisfy ε-DP for continuous and discrete cases, however, they can result in large added noise. Conversely, the middle distribution significantly decreases the probability of such events, but the obtained differential privacy guarantee is weaker (i.e. (ε, δ)-DP, which will be presented in Section 3).

**2.2 Dimensions**

Variants and extensions of differential privacy modify the original definition in various ways. To create a comprehensive taxonomy, the natural approach is to divide them into categories, depending on which aspect they change from the definition. Unfortunately, this approach fails for privacy definitions, since many of them modify several aspects at once, so it is impossible to get a categorization such that each definition falls precisely into only one category.

The approach we follow is to determine the dimensions along which the original definition can be modified. Each variant or extension of differential privacy can be viewed as a point in multidimensional space, where each coordinate corresponds to one possible way to change the definition along a certain dimension. To make this representation possible, our dimensions must satisfy two properties:

- **Mutual compatibility**: definitions that vary along different dimensions can be combined to form a new and meaningful definition.
- **Inner exclusivity**: definitions in the same dimension cannot be combined to form a new and meaningful definition (but can be compared in pairs).

Additionally, each dimension should be motivatable: there should be an intuitive explanation of what it means to modify differential privacy along each dimension. Moreover, each possible choice within a dimension should be similarly understandable, to allow new practitioners to determine which type of definition they should use or study quickly, depending on their use case.

We present our dimensions by reformulating the guarantee provided by differential privacy, highlighting the aspects that have been modified by its variants or extensions. Each dimension is assigned a letter, and we note the dimension letter corresponding to each highlight. This formulation considers the attacker's point of view, who tries to find out some sensitive information about some input data using the mechanism's outputs.

**An attacker who has complete background knowledge (B) and unlimited computational power (C) is unable (R) to distinguish (F) anything about an individual (N), uniformly across users (V) even in the worst scenario (Q).**

This informal definition of differential privacy with the seven distinguished aspects gives us seven distinct dimensions. We denote each one by a letter and summarize them in Table 2. Each is presented in its corresponding section.

Note that the interpretation of differential privacy is subject to some debate. In [TSD20], the authors summarize this debate and show that differential privacy can be interpreted under two possible lenses: it can be seen as an associative property, or as a causal property. The difference between the two interpretations is especially clear when one assumes that the input dataset is modeled as being generated by a probability distribution.

- In the **associative view**, this probability distribution is conditioned on the value of one record. If the distribution has correlations, this change can affect other records as well.
- In the **causal view**, the dataset is first generated, and then the value of one record is changed before calculating the mechanism's result.

While the causal view does not require any additional assumption to capture the intuition behind differential privacy, the associative view requires that either all records are independent in the original probability distribution (the independence assumption), or the adversary must know all data points except one (the strong adversary assumption, which we chose in the reformulation above).

These considerations can have a significant impact on differential privacy variants and extensions, either leading to distinct variants that attempt to capture the same intuition, or to interpreting the same variant in different ways.

**2.3 Properties**

In this section, we present three main properties of differential privacy, which we then verify against the variants and extensions of differential privacy listed in this work.

**Privacy Axioms**

Two important properties of data privacy concepts are called privacy axioms, proposed in [KL10, KL12]. These are not axioms in the sense that they are assumed to be true; rather, they are consistency checks: properties that, if not satisfied by a data privacy definition, indicate a flaw in the definition.

**Definition 3 (Privacy axioms).**

1. **Post-processing** (or transformation invariance): A privacy definition Def satisfies the post-processing axiom if, for any mechanism M that satisfies Def and any probabilistic function f, the mechanism D → f(M(D)) also satisfies Def.

2. **Convexity** (or privacy choice axiom): A privacy definition Def satisfies the convexity axiom if, for any two mechanisms M₁ and M₂ that satisfy Def, the mechanism M defined by M(D) = M₁(D) with probability p and M(D) = M₂(D) with probability 1 − p also satisfies Def.

Most variants and extensions of differential privacy, including the original definition of differential privacy, satisfy these axioms, although some do not. We highlighted these in Table 3 in Section 10.

**Composition**

The third important property is one of the main strengths of differential privacy: composability. It ensures that the outputs of two mechanisms that satisfy a privacy definition still satisfy the definition, usually with a change in parameters. There are several types of composition: parallel composition, sequential composition, and adaptive composition. We present the first two below.

**Theorem (Parallel composition).** Let M₁ be a ε₁-differentially private mechanism, and M₂ a ε₂-differentially private mechanism. For any dataset D, let D₁ and D₂ be the result of an operation that separates records into two disjoint datasets. Then the mechanism M defined by M(D) = (M₁(D₁),M₂(D₂)) is max(ε₁, ε₂)-differentially private.

This property allows us to build locally differentially private mechanisms, where a central server can compute general statistics without accessing raw data from each user. In this work, we focus on sequential composition, which we simply call composition.

**Theorem (Sequential composition).** Let M₁ be a ε₁-differentially private mechanism, and M₂ a ε₂-differentially private mechanism. Then the mechanism M defined by M(D) = (M₁(D),M₂(D)) is (ε₁ + ε₂)-differentially private.

This theorem remains true if M₂ depends on the value of M₁(D): this variant is called adaptive composition. This last property allows quantifying the gain of information over time for an attacker interacting with a differentially private query engine.

In this work, we only consider sequential composition, in the more abstract form formalized below.

**Definition 4 (Composability).** A privacy definition Def with parameter α is composable if for any two mechanisms M₁ and M₂ that satisfy α₁-Def and α₂-Def respectively, the mechanism M(D) = (M₁(D),M₂(D)) satisfies α-Def for some (non-trivial) α.

**2.4 Relations between Definitions**

When learning about a new data privacy concept, it is often useful to know what the known relations are between this concept and other definitions. However, definitions have parameters that often have different meanings, and whose value is not directly comparable. To capture extensions, when a definition can be viewed as a special case of another, we present the following definition.

**Definition 5 (Extensions).** Let α-Def₁ and β-Def₂ be data privacy definitions. We say that Def₁ is extended by Def₂, and denote it as Def₁ ⊂ Def₂, if for all α, there is a value β such that α-Def₁ is identical to β-Def₂.

Regarding variants, to claim that a definition is stronger than another, we adopt the ordering concept established in [CY16] using α and β as tuples, to encode multiple parameters. Note that we slightly changed the original definition as it only required the second condition to hold, which could classify any extension as a stronger variant.

**Definition 6 (Relative strength of privacy definitions).** Let α-Def₁ and β-Def₂ be data privacy definitions. We say that Def₁ is stronger than Def₂, and denote it Def₁ ≻ Def₂, if:

1. for all α, there is a β such that α-Def₁ ⟹ β-Def₂;
2. for all β, there is an α such that α-Def₁ ⟹ β-Def₂.

If Def₁ is both stronger than and weaker than Def₂, we say the two definitions are equivalent, and denote it Def₁ ∼ Def₂.

Relative strength indicates a partial ordering on the space of possible definitions. On the other hand, if two definitions are equivalent, this does not mean they are equal: they could only be equal up to a change in parameters. Both relations are reflexive and transitive; and we define the symmetric counterpart of these relations as well (i.e., ≺ and ⊃). Moreover, for brevity, we combine these two concepts in one notation: if Def₁ ⊂ Def₂ and Def₁ ≻ Def₂, we say that Def₂ is a weaker extension of Def₁, and denote it Def₁ ⊂≺ Def₂.

A summary table is presented at the end of this work, where we also highlight for each definition its dimensions and its relation to other concepts. In Table 3, we also specify whether these concepts satisfy the privacy axioms and composability property (✓: yes, ✗: no, ?: currently unknown); in Section 10 we provide either a reference or a new proof for each of these claims.

---

## Glossary Terms Used

- differential privacy → الخصوصية التفاضلية
- privacy → خصوصية
- data privacy → خصوصية البيانات
- definition → تعريف
- mechanism → آلية
- dataset → مجموعة البيانات
- record → سجل
- output → مخرج
- indistinguishability → عدم التمييز
- random variable → متغير عشوائي
- distribution → توزيع
- probability → احتمال
- randomized response → الاستجابة العشوائية
- noise → ضوضاء
- perturbation → اضطراب
- dimension → بُعد
- variant → متغير
- extension → إضافة
- taxonomy → تصنيف
- mutual compatibility → التوافق المتبادل
- inner exclusivity → الحصرية الداخلية
- attacker → مهاجم
- background knowledge → معرفة خلفية
- computational power → قوة حسابية
- associative → ترابطية
- causal → سببية
- privacy axioms → بديهيات الخصوصية
- post-processing → المعالجة اللاحقة
- convexity → التحدب
- composition → التركيب
- parallel composition → التركيب المتوازي
- sequential composition → التركيب التسلسلي
- adaptive composition → التركيب التكيفي
- composability → قابلية التركيب
- stronger → أقوى
- weaker → أضعف
- equivalent → متكافئ
