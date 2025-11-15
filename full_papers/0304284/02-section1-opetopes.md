# Section 1: The category of opetopes
## القسم 1: فئة الأوبتوبات

**Section:** methodology/construction
**Translation Quality:** 0.86
**Glossary Terms Used:** category (فئة), opetope (أوبتوب), morphism (تشاكل), functor (دالة تصنيفية), object (كائن), bijection (تقابل), isomorphism (تشاكل), graph (رسم بياني)

---

### English Version

In this section we give an explicit construction of the category **Opetope** of opetopes. This construction will enable us, in Section 2, to prove that the category of opetopic sets is in fact a presheaf category.

We begin with a brief account of the trees used to construct higher-dimensional opetopes from lower-dimensional ones; we refer the reader to [4] for the full account, with proofs and examples.

#### 1.1 Informal description of trees

Recall the trees introduced in [6] to describe the morphisms of a slice multicategory. These are 'labelled combed trees' with ordered nodes. In fact, we will first consider the unlabelled version of such trees, since the labelled version follows easily. For example the following is a tree:

[Tree diagram with nodes numbered 1-5]

Explicitly, a tree T = (T,ρ,τ) consists of

i) A planar tree T

ii) A permutation ρ ∈ Sₗ where l = number of leaves of T

iii) A bijection τ : {nodes of T} −→ {1, 2,... ,k} where k = number of nodes of T; equivalently an ordering on the nodes of T.

Note that there is a 'null tree' with no nodes [single vertical line].

#### 1.2 Formal description of trees

In this section we give a formal description of the above trees, characterising them as connected graphs with no closed loops (in the conventional sense of 'graph'). This will enable us, in Section 1.4, to determine which faces of faces are identified in an opetope.

Note that the material in this section is presented fully in [4]. It enables us to express a tree as a Kelly-Mac Lane graph; it also enables us to show that all allowable Kelly-Mac Lane graphs of the correct shape arise in this way.

We consider a tree with k nodes N₁,... ,Nₖ where Nᵢ has mᵢ inputs and one output. Let N be a node with (∑ᵢ mᵢ) − k + 1 inputs; N will be used to represent the leaves and root of the tree.

Then a tree is given by a bijection

⨿ᵢ {inputs of Nᵢ} ⨿ {output of N} −→ ⨿ᵢ {output of Nᵢ} ⨿ {inputs of N}

since each input of a node is either connected to a unique output of another node, or it is a leaf, that is, input of N. Similarly each output of a node is either attached to an input of another node, or it is the root, that is, output of N.

We express this formally as follows.

**Lemma 1.1** Let T be a tree with nodes N₁,... ,Nₖ, where Nᵢ has inputs {xᵢ₁,... ,xᵢₘᵢ} and output xᵢ. Let N be a node with inputs {z₁,... ,zₗ} and output z, with

l = (∑ᵏᵢ₌₁ mᵢ) − k + 1.

Then T is given by a bijection

α : ⨿ᵢ {xᵢ₁,... ,xᵢₘᵢ} ⨿ {z} −→ ⨿ᵢ {xᵢ} ⨿ {z₁,... ,zₗ}.

For the converse, every such bijection gives a graph, but it is not necessarily a tree. We need to ensure that the resulting graph has no closed loops; the use of the 'formal' node N then ensures connectedness. We express this formally as follows.

**Lemma 1.2** Let N₁,... ,Nₖ,N be nodes where Nᵢ has inputs {xᵢ₁,... ,xᵢₘᵢ} and output xᵢ, and N has inputs {z₁,... ,zₗ} and output z, with l = (∑ᵏᵢ₌₁ mᵢ) − k + 1. Let α be a bijection

⨿ᵢ {xᵢ₁,... ,xᵢₘᵢ} ⨿ {z} −→ ⨿ᵢ {xᵢ} ⨿ {z₁,... ,zₗ}.

Then α defines a graph with nodes N₁,... ,Nₖ.

**Lemma 1.3** Let α be a graph as above. Then α has a closed loop if and only if there is a non-empty sequence of indices

{t₁,... ,tₙ} ⊆ {1,... ,k}

such that for each 2 ≤ j ≤ n

α(xₜⱼ bⱼ) = xₜⱼ₋₁

for some 1 ≤ bⱼ ≤ mⱼ, and

α(xₜ₁b₁) = xₜₙ

for some 1 ≤ b₁ ≤ m₁.

**Corollary 1.4** A tree with nodes N₁,... ,Nₖ is precisely a bijection α as in Lemma 1.2, such that there is no sequence of indices as in Lemma 1.3.

#### 1.3 Labelled trees

For the construction of opetopes we require the 'labelled' version of the trees presented in Section 1.1. A tree labelled in a category C is a tree as above, with each edge labelled by a morphism of C considered to be pointing 'down' towards the root.

**Proposition 1.5** Let N₁,... ,Nₖ,N be nodes where Nᵢ has inputs

{xᵢ₁,... ,xᵢₘᵢ}

and output xᵢ, and N has inputs {z₁,... ,zₗ} and output z, with

l = (∑ᵏᵢ₌₁ mᵢ) − k + 1.

Then a labelled tree with these nodes is given by a bijection

α : ⨿ᵢ {xᵢ₁,... ,xᵢₘᵢ} ⨿ {z} −→ ⨿ᵢ {xᵢ} ⨿ {z₁,... ,zₗ}

satisfying the conditions as above, together with, for each

y ∈ ⨿ᵢ {xᵢ₁,... ,xᵢₘᵢ} ⨿ {z}

a morphism f ∈ C giving the label of the edge joining y and α(y). Then y is considered to be labelled by the object cod(f) and α(y) by the object dom(f).

**Proof.** Follows immediately from Corollary 1.4 and the definition. □

#### 1.4 The category of opetopes

In our earlier work ([6]) we constructed for each k ≥ 0 the category ℂₖ of k-opetopes. We now construct a category **Opetope** = O of opetopes of all dimensions whose morphisms are, essentially, face maps. Each category ℂₖ is to be a full subcategory of **Opetope**, and there are no morphisms from an opetope to one of lower dimension.

We construct the category **Opetope** = O as follows. Write 𝒪ₖ = ℂₖ.

For the objects:
ob O = ⨿ₖ≥₀ 𝒪ₖ.

The morphisms of O are given by generators and relations as follows.

**• Generators**

1) For each morphism f : α −→ β ∈ 𝒪ₖ there is a morphism
   f : α −→ β ∈ O.

2) Let k ≥ 1 and consider α ∈ 𝒪ₖ = o(Iᵏ⁺) = elt(I⁽ᵏ⁻¹⁾⁺). Write
   α ∈ I⁽ᵏ⁻¹⁾⁺(x₁,... ,xₘ; x). Then for each 1 ≤ i ≤ m there is a morphism
   sᵢ: xᵢ −→ α ∈ O
   and there is also a morphism
   t : x −→ α ∈ O.

We write Gₖ for the set of all generating morphisms of this kind.

Before giving the relations on these morphisms we make the following observation about morphisms in 𝒪ₖ. Consider

α ∈ I⁽ᵏ⁻¹⁾⁺(x₁,... ,xₘ; x)
β ∈ I⁽ᵏ⁻¹⁾⁺(y₁,... ,yₘ; y)

A morphism α →ᵍ β ∈ 𝒪ₖ is given by a permutation σ and morphisms

xᵢ →fᵢ yσ(i)
x →f y ∈ 𝒪ₖ₋₁

So for each face map γ there is a unique 'restriction' of g to the specified face, giving a morphism γg of (k − 1)-opetopes.

Note that, to specify a morphism in the category F𝒪ₖ₋₁ᵒᵖ × 𝒪ₖ₋₁ the morphisms fᵢ above should be in the direction yσ(i) −→ xᵢ, but since these are all unique isomorphisms the direction does not matter; the convention above helps the notation. We now give the relations on the above generating morphisms.

**• Relations**

1) For any morphism
   α →ᵍ β ∈ 𝒪ₖ
   and face map
   xᵢ →sᵢ α

   the following diagrams commute

   [Commutative diagrams showing face map restrictions]

   We write these generally as

   [Generic commutative diagram]

2) Faces are identified where composition occurs: consider θ ∈ 𝒪ₖ where k ≥ 2. Recall that θ is constructed as an arrow of a slice multicategory, so is given by a labelled tree, with nodes labelled by its (k − 1)-faces, and edges labelled by object-morphisms, that is, morphisms of 𝒪ₖ₋₂.

   So by the formal description of trees (Section 1.2), θ is a certain bijection, and the elements that are in bijection with each other are the (k − 2)-faces of the (k − 1)-faces of θ; they are given by composable pairs of face maps of the second kind above. That is, the node labels are given by face maps α →γ θ and then the inputs and outputs of those are given by pairs

   x →γ₁ α →γ₂ θ

   where γ₂ ∈ Gₖ and γ₁ ∈ Gₖ₋₁. Now, if

   x →γ₁ α →γ₂ θ
   and y →γ₃ β →γ₄ θ

   correspond under the bijection, there must be a unique object-morphism

   f : x −→ y

   labelling the relevant edge of the tree. Then for the composites in O we have the relation: the following diagram commutes

   [Commutative diagram showing face identification]

3) Composition in 𝒪ₖ is respected, that is, if g ∘ f = h ∈ 𝒪ₖ then g ∘ f = h ∈ O.

4) Identities in 𝒪ₖ are respected, that is, given any morphism x →γ α ∈ O we have γ ∘ 1ₓ = γ.

Note that only the relation (2) is concerned with the identification of faces with one another; the other relations are merely dealing with isomorphic copies of opetopes.

We immediately check that the above relations have not identified any morphisms of 𝒪ₖ.

**Lemma 1.6** Each 𝒪ₖ is a full subcategory of O.

**Proof.** Clear from definitions. □

We now check that the above relations have not identified any (k − 1)-faces of k-opetopes.

**Proposition 1.7** Let x ∈ 𝒪ₖ₋₁, α ∈ 𝒪ₖ and γ₁,γ₂ ∈ Gₖ with

γ₁, γ₂ : x −→ α

Then γ₁ = γ₂ ∈ O =⇒ γ₁ = γ₂ ∈ Gₖ.

We prove this by expressing all morphisms from (k − 1)-opetopes to k-opetopes in the following "normal form"; this is a simple exercise in term rewriting (see [11]).

**Lemma 1.8** Let x ∈ 𝒪ₖ₋₁, α ∈ O. Then a morphism

x −→ α ∈ O

is uniquely represented by

x →γ α

or a pair

x →f y →γ α

where f ∈ 𝒪ₖ₋₁ and γ ∈ Gₖ.

**Proof.** Any map x −→ α is represented by terms of the form

x →f₁ x₁ →f₂ · · · →fₘ xₘ →γ α₁ →g₁ · · · →gⱼ₋₁ αⱼ →gⱼ α

where each fᵢ ∈ 𝒪ₖ₋₁ and each gᵣ ∈ 𝒪ₖ. Equalities are generated by equalities in components of the following forms:

1) γ → g → = γg → γ′ →
2) f → f′ → = f′ ∘ f → ∈ 𝒪ₖ₋₁
3) g → g′ → = g′ ∘ g → ∈ 𝒪ₖ
4) 1 → γ → = γ →

where γ ∈ Gₖ and γg and γ′ are as defined above. That is, equalities in terms are generated by equations t = t′ where t′ is obtained from t by replacing a component of t of a left hand form above, with the form in the right hand side, or vice versa.

We now orient the equations in the term rewriting style in the direction =⇒ from left to right in the above equations. We then show two obvious properties:

1) Any reduction of t by =⇒ terminates in at most 2j + m steps.

2) If we have

   [Diamond diagram showing confluence]

   then there exists t′′′ with

   [Diamond diagram with dotted arrows]

   where the dotted arrows indicate a chain of equations (in this case of length at most 2).

The first part is clear from the definitions; for the second part the only non-trivial case is for a component of the form

γ → g₁ → g₂ →.

This reduces uniquely to

γ(g₂ ∘ g₁) → γ′ →

since 'restriction' is unique, as discussed earlier.

It follows that, for any terms t and s, t = s if and only if t and s reduce to the same normal form as above. □

**Proof of Proposition 1.7.** γ₁ and γ₂ are in normal form. □

---

### النسخة العربية

في هذا القسم نُقدم بناءً صريحاً لفئة الأوبتوبات **Opetope**. سيمكننا هذا البناء، في القسم 2، من إثبات أن فئة المجموعات الأوبتوبية هي في الواقع فئة حزم أمامية.

نبدأ بعرض موجز للأشجار المستخدمة لبناء أوبتوبات ذات أبعاد أعلى من أوبتوبات ذات أبعاد أدنى؛ نحيل القارئ إلى [4] للعرض الكامل، مع البراهين والأمثلة.

#### 1.1 وصف غير رسمي للأشجار

تذكر الأشجار المقدمة في [6] لوصف تشاكلات تعدد فئوي مشرّح. هذه هي 'أشجار ممشطة موسومة' مع عُقد مرتبة. في الواقع، سننظر أولاً في النسخة غير الموسومة من هذه الأشجار، حيث أن النسخة الموسومة تتبع بسهولة. على سبيل المثال، ما يلي شجرة:

[رسم شجرة مع عُقد مرقمة 1-5]

بشكل صريح، شجرة T = (T,ρ,τ) تتكون من

i) شجرة مستوية T

ii) تبديل ρ ∈ Sₗ حيث l = عدد أوراق T

iii) تقابل τ : {عُقد T} −→ {1, 2,... ,k} حيث k = عدد عُقد T؛ أو بما يعادل ترتيب على عُقد T.

لاحظ أن هناك 'شجرة خالية' بدون عُقد [خط عمودي واحد].

#### 1.2 وصف رسمي للأشجار

في هذا القسم نعطي وصفاً رسمياً للأشجار أعلاه، ونميزها كرسوم بيانية متصلة بدون حلقات مغلقة (بالمعنى التقليدي لـ 'رسم بياني'). سيمكننا هذا، في القسم 1.4، من تحديد أي وجوه من الوجوه يتم تحديدها في أوبتوب.

لاحظ أن المادة في هذا القسم مقدمة بالكامل في [4]. تمكننا من التعبير عن شجرة كرسم بياني لكيلي-ماك لين؛ كما تمكننا من إظهار أن جميع رسوم كيلي-ماك لين المسموح بها من الشكل الصحيح تنشأ بهذه الطريقة.

نعتبر شجرة بها k عُقدة N₁,... ,Nₖ حيث Nᵢ لها mᵢ مدخلات ومخرج واحد. لتكن N عُقدة بها (∑ᵢ mᵢ) − k + 1 مدخلات؛ ستُستخدم N لتمثيل الأوراق والجذر للشجرة.

ثم الشجرة معطاة بتقابل

⨿ᵢ {مدخلات Nᵢ} ⨿ {مخرج N} −→ ⨿ᵢ {مخرج Nᵢ} ⨿ {مدخلات N}

حيث أن كل مدخل لعُقدة إما متصل بمخرج فريد لعُقدة أخرى، أو هو ورقة، أي مدخل لـ N. وبالمثل كل مخرج لعُقدة إما مرفق بمدخل عُقدة أخرى، أو هو الجذر، أي مخرج N.

نعبر عن هذا رسمياً كما يلي.

**المبرهنة 1.1** لتكن T شجرة مع عُقد N₁,... ,Nₖ، حيث Nᵢ لها مدخلات {xᵢ₁,... ,xᵢₘᵢ} ومخرج xᵢ. لتكن N عُقدة مع مدخلات {z₁,... ,zₗ} ومخرج z، مع

l = (∑ᵏᵢ₌₁ mᵢ) − k + 1.

ثم T معطاة بتقابل

α : ⨿ᵢ {xᵢ₁,... ,xᵢₘᵢ} ⨿ {z} −→ ⨿ᵢ {xᵢ} ⨿ {z₁,... ,zₗ}.

للعكس، كل تقابل من هذا القبيل يعطي رسماً بيانياً، لكنه ليس بالضرورة شجرة. نحتاج إلى التأكد من أن الرسم البياني الناتج ليس له حلقات مغلقة؛ استخدام العُقدة 'الرسمية' N يضمن بعد ذلك الاتصال. نعبر عن هذا رسمياً كما يلي.

**المبرهنة 1.2** لتكن N₁,... ,Nₖ,N عُقداً حيث Nᵢ لها مدخلات {xᵢ₁,... ,xᵢₘᵢ} ومخرج xᵢ، وN لها مدخلات {z₁,... ,zₗ} ومخرج z، مع l = (∑ᵏᵢ₌₁ mᵢ) − k + 1. ليكن α تقابلاً

⨿ᵢ {xᵢ₁,... ,xᵢₘᵢ} ⨿ {z} −→ ⨿ᵢ {xᵢ} ⨿ {z₁,... ,zₗ}.

ثم α يُعرِّف رسماً بيانياً مع عُقد N₁,... ,Nₖ.

**المبرهنة 1.3** ليكن α رسماً بيانياً كما أعلاه. ثم α له حلقة مغلقة إذا وفقط إذا كانت هناك متتالية غير فارغة من الفهارس

{t₁,... ,tₙ} ⊆ {1,... ,k}

بحيث لكل 2 ≤ j ≤ n

α(xₜⱼ bⱼ) = xₜⱼ₋₁

لبعض 1 ≤ bⱼ ≤ mⱼ، و

α(xₜ₁b₁) = xₜₙ

لبعض 1 ≤ b₁ ≤ m₁.

**النتيجة 1.4** الشجرة مع عُقد N₁,... ,Nₖ هي بالضبط تقابل α كما في المبرهنة 1.2، بحيث لا توجد متتالية من الفهارس كما في المبرهنة 1.3.

#### 1.3 الأشجار الموسومة

لبناء الأوبتوبات نحتاج النسخة 'الموسومة' من الأشجار المقدمة في القسم 1.1. الشجرة الموسومة في فئة C هي شجرة كما أعلاه، مع وسم كل حافة بتشاكل من C يُعتبر يشير 'لأسفل' نحو الجذر.

**القضية 1.5** لتكن N₁,... ,Nₖ,N عُقداً حيث Nᵢ لها مدخلات

{xᵢ₁,... ,xᵢₘᵢ}

ومخرج xᵢ، وN لها مدخلات {z₁,... ,zₗ} ومخرج z، مع

l = (∑ᵏᵢ₌₁ mᵢ) − k + 1.

ثم الشجرة الموسومة مع هذه العُقد معطاة بتقابل

α : ⨿ᵢ {xᵢ₁,... ,xᵢₘᵢ} ⨿ {z} −→ ⨿ᵢ {xᵢ} ⨿ {z₁,... ,zₗ}

يُحقق الشروط أعلاه، مع، لكل

y ∈ ⨿ᵢ {xᵢ₁,... ,xᵢₘᵢ} ⨿ {z}

تشاكل f ∈ C يعطي وسم الحافة التي تربط y وα(y). ثم y يُعتبر موسوماً بالكائن cod(f) وα(y) بالكائن dom(f).

**البرهان.** يتبع مباشرة من النتيجة 1.4 والتعريف. □

#### 1.4 فئة الأوبتوبات

في عملنا السابق ([6]) بنينا لكل k ≥ 0 فئة ℂₖ من k-أوبتوبات. نبني الآن فئة **Opetope** = O من الأوبتوبات من جميع الأبعاد التي تشاكلاتها، بشكل أساسي، دوال الوجوه. كل فئة ℂₖ ستكون فئة جزئية كاملة من **Opetope**، ولا توجد تشاكلات من أوبتوب إلى واحد من بُعد أدنى.

نبني فئة **Opetope** = O كما يلي. نكتب 𝒪ₖ = ℂₖ.

للكائنات:
ob O = ⨿ₖ≥₀ 𝒪ₖ.

تُعطى تشاكلات O بمولدات وعلاقات كما يلي.

**• المولدات**

1) لكل تشاكل f : α −→ β ∈ 𝒪ₖ يوجد تشاكل
   f : α −→ β ∈ O.

2) ليكن k ≥ 1 ونعتبر α ∈ 𝒪ₖ = o(Iᵏ⁺) = elt(I⁽ᵏ⁻¹⁾⁺). نكتب
   α ∈ I⁽ᵏ⁻¹⁾⁺(x₁,... ,xₘ; x). ثم لكل 1 ≤ i ≤ m يوجد تشاكل
   sᵢ: xᵢ −→ α ∈ O
   ويوجد أيضاً تشاكل
   t : x −→ α ∈ O.

نكتب Gₖ لمجموعة جميع التشاكلات المولدة من هذا النوع.

قبل إعطاء العلاقات على هذه التشاكلات نُجري الملاحظة التالية حول التشاكلات في 𝒪ₖ. نعتبر

α ∈ I⁽ᵏ⁻¹⁾⁺(x₁,... ,xₘ; x)
β ∈ I⁽ᵏ⁻¹⁾⁺(y₁,... ,yₘ; y)

التشاكل α →ᵍ β ∈ 𝒪ₖ معطى بتبديل σ وتشاكلات

xᵢ →fᵢ yσ(i)
x →f y ∈ 𝒪ₖ₋₁

لذا لكل دالة وجه γ يوجد 'تقييد' فريد لـ g على الوجه المحدد، يعطي تشاكل γg من (k − 1)-أوبتوبات.

لاحظ أنه لتحديد تشاكل في فئة F𝒪ₖ₋₁ᵒᵖ × 𝒪ₖ₋₁ يجب أن تكون التشاكلات fᵢ أعلاه في الاتجاه yσ(i) −→ xᵢ، لكن نظراً لأن هذه كلها تشاكلات فريدة، الاتجاه لا يهم؛ الاتفاقية أعلاه تساعد الترميز. نعطي الآن العلاقات على التشاكلات المولدة أعلاه.

**• العلاقات**

1) لأي تشاكل
   α →ᵍ β ∈ 𝒪ₖ
   ودالة وجه
   xᵢ →sᵢ α

   المخططات التالية تُبدّل

   [مخططات تبديلية تُظهر تقييدات دوال الوجوه]

   نكتب هذه بشكل عام كـ

   [مخطط تبديلي عام]

2) تُحدَّد الوجوه حيث يحدث التركيب: نعتبر θ ∈ 𝒪ₖ حيث k ≥ 2. تذكر أن θ مبني كسهم من تعدد فئوي مشرّح، لذا معطى بشجرة موسومة، مع عُقد موسومة بوجوهه (k − 1)، وحواف موسومة بتشاكلات كائنات، أي تشاكلات 𝒪ₖ₋₂.

   لذا بالوصف الرسمي للأشجار (القسم 1.2)، θ هو تقابل معين، والعناصر التي في تقابل مع بعضها البعض هي وجوه (k − 2) لوجوه (k − 1) لـ θ؛ معطاة بأزواج قابلة للتركيب من دوال الوجوه من النوع الثاني أعلاه. أي أن وسوم العُقد معطاة بدوال الوجوه α →γ θ ثم المدخلات والمخرجات لتلك معطاة بأزواج

   x →γ₁ α →γ₂ θ

   حيث γ₂ ∈ Gₖ وγ₁ ∈ Gₖ₋₁. الآن، إذا

   x →γ₁ α →γ₂ θ
   و y →γ₃ β →γ₄ θ

   تتوافقان تحت التقابل، يجب أن يكون هناك تشاكل كائن فريد

   f : x −→ y

   يوسم الحافة ذات الصلة من الشجرة. ثم للمركبات في O لدينا العلاقة: المخطط التالي يُبدّل

   [مخطط تبديلي يُظهر تحديد الوجوه]

3) التركيب في 𝒪ₖ محترم، أي إذا g ∘ f = h ∈ 𝒪ₖ ثم g ∘ f = h ∈ O.

4) المتطابقات في 𝒪ₖ محترمة، أي لأي تشاكل x →γ α ∈ O لدينا γ ∘ 1ₓ = γ.

لاحظ أن العلاقة (2) فقط معنية بتحديد الوجوه مع بعضها البعض؛ العلاقات الأخرى تتعامل فقط مع نسخ متشاكلة من الأوبتوبات.

نتحقق مباشرة من أن العلاقات أعلاه لم تحدد أي تشاكلات من 𝒪ₖ.

**المبرهنة 1.6** كل 𝒪ₖ فئة جزئية كاملة من O.

**البرهان.** واضح من التعريفات. □

نتحقق الآن من أن العلاقات أعلاه لم تحدد أي وجوه (k − 1) من k-أوبتوبات.

**القضية 1.7** ليكن x ∈ 𝒪ₖ₋₁، α ∈ 𝒪ₖ وγ₁,γ₂ ∈ Gₖ مع

γ₁, γ₂ : x −→ α

ثم γ₁ = γ₂ ∈ O =⇒ γ₁ = γ₂ ∈ Gₖ.

نُثبت هذا بالتعبير عن جميع التشاكلات من (k − 1)-أوبتوبات إلى k-أوبتوبات في "الصيغة الطبيعية" التالية؛ هذا تمرين بسيط في إعادة كتابة المصطلحات (انظر [11]).

**المبرهنة 1.8** ليكن x ∈ 𝒪ₖ₋₁، α ∈ O. ثم التشاكل

x −→ α ∈ O

ممثل بشكل فريد بـ

x →γ α

أو زوج

x →f y →γ α

حيث f ∈ 𝒪ₖ₋₁ وγ ∈ Gₖ.

**البرهان.** أي دالة x −→ α ممثلة بمصطلحات من الشكل

x →f₁ x₁ →f₂ · · · →fₘ xₘ →γ α₁ →g₁ · · · →gⱼ₋₁ αⱼ →gⱼ α

حيث كل fᵢ ∈ 𝒪ₖ₋₁ وكل gᵣ ∈ 𝒪ₖ. التساويات مولدة بتساويات في مكونات من الأشكال التالية:

1) γ → g → = γg → γ′ →
2) f → f′ → = f′ ∘ f → ∈ 𝒪ₖ₋₁
3) g → g′ → = g′ ∘ g → ∈ 𝒪ₖ
4) 1 → γ → = γ →

حيث γ ∈ Gₖ وγg وγ′ كما عُرِّفا أعلاه. أي أن التساويات في المصطلحات مولدة بمعادلات t = t′ حيث t′ محصول عليه من t باستبدال مكون من t من شكل يد يسرى أعلاه، بالشكل في اليد اليمنى، أو العكس.

نوجه الآن المعادلات بأسلوب إعادة كتابة المصطلحات في الاتجاه =⇒ من اليسار إلى اليمين في المعادلات أعلاه. ثم نُظهر خاصيتين واضحتين:

1) أي اختزال لـ t بـ =⇒ ينتهي في 2j + m خطوة على الأكثر.

2) إذا كان لدينا

   [مخطط ماسي يُظهر الالتقاء]

   ثم يوجد t′′′ مع

   [مخطط ماسي مع أسهم منقطة]

   حيث الأسهم المنقطة تشير إلى سلسلة من المعادلات (في هذه الحالة من طول 2 على الأكثر).

الجزء الأول واضح من التعريفات؛ للجزء الثاني الحالة غير التافهة الوحيدة هي لمكون من الشكل

γ → g₁ → g₂ →.

هذا يختزل بشكل فريد إلى

γ(g₂ ∘ g₁) → γ′ →

حيث أن 'التقييد' فريد، كما نوقش سابقاً.

يتبع أنه لأي مصطلحات t وs، t = s إذا وفقط إذا اختُزل t وs إلى نفس الصيغة الطبيعية أعلاه. □

**برهان القضية 1.7.** γ₁ وγ₂ في صيغة طبيعية. □

---

### Translation Notes

- **Figures referenced:** Tree diagrams (described textually), commutative diagrams
- **Key terms introduced:** planar tree (شجرة مستوية), permutation (تبديل), bijection (تقابل), Kelly-Mac Lane graph (رسم بياني لكيلي-ماك لين), face map (دالة وجه), degeneracy map (دالة تدهور), full subcategory (فئة جزئية كاملة), generators (مولدات), relations (علاقات), normal form (صيغة طبيعية), term rewriting (إعادة كتابة المصطلحات), confluence (التقاء)
- **Equations:** Multiple mathematical equations and formulas preserved
- **Citations:** [4], [6], [11]
- **Special handling:**
  - All mathematical notation preserved exactly (∑, ⨿, ∈, ≥, ∘, etc.)
  - Lemmas, Propositions, Corollaries numbered as in original
  - Proof structures maintained with البرهان and □ for end of proof
  - Commutative diagrams described textually

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.86
