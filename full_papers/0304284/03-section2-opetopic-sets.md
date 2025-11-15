# Section 2: Opetopic Sets
## القسم 2: المجموعات الأوبتوبية

**Section:** main results
**Translation Quality:** 0.85
**Glossary Terms Used:** category (فئة), presheaf (حزمة أمامية), functor (دالة تصنيفية), morphism (تشاكل), multicategory (تعدد فئوي), equivalence (تكافؤ), opetope (أوبتوب), pullback (سحب عكسي), colimit (حد استقرائي)

---

### English Version

In this section we examine the theory of opetopic sets. We begin by following through our modifications to the opetopic theory to include the theory of opetopic sets. We then use results of [12] to prove that the category of opetopic sets is indeed equivalent to the category of presheaves on O, the category of opetopes defined in Section 1. This is the main result of this work.

Recall that, by the equivalences proved in the [6] and [5], we have equivalent categories of opetopes, multitopes and Leinster opetopes. So we may define equivalent categories of opetopic sets by taking presheaves on any of these three categories. In the following definitions, although the opetopes we consider are the 'symmetric multicategory' kind, the concrete description of an opetopic set is not precisely as a presheaf on the category of these opetopes. The sets given in the data are indexed not by opetopes themselves but by isomorphism classes of opetopes; so at first sight this resembles a presheaf on the category of Leinster opetopes. However, we do not pursue this matter here, since the equivalences proved in our earlier work are sufficient for the purposes of this article.

We adopt this presentation in order to avoid naming the same cells repeatedly according to the symmetries; that is, we do not keep copies of cells that are isomorphic by the symmetries.

#### 2.1 Definitions

In [3], weak n-categories are defined as opetopic sets satisfying certain universality conditions. However, opetopic sets are defined using only symmetric multicategories with a set of objects; in the light of the results of our earlier work, we seek a definition using symmetric multicategories with a category of objects. The definitions we give here are those given in [3] but with modifications as demanded by the results of our previous work.

The underlying data for an opetopic n-category are given by an opetopic set. Recall that, in [3], given a symmetric multicategory Q a Q-opetopic set X is given by, for each k ≥ 0, a symmetric multicategory Q(k) and a set X(k) over o(Q(k)), where

Q(0) = Q
and Q(k + 1) = Q(k)_{X(k)}^+.

An opetopic set is then an I-opetopic set, where I is the symmetric multicategory with one object and one (identity) arrow.

The idea is that the category of opetopic sets should be equivalent to the presheaf category

[Opetope^{op}, Set].

To prove this we use [12], Theorem 5.26, in the case V = Set. A functor

Opetope^{op} −→ Set

may be considered as assigning to each opetope a set of 'labels'.

Recall that for each k, ℂ(k) is equivalent to a discrete category. So it is sufficient to specify 'labels' for each isomorphism class of opetopes.

Recall ([6]) that we call a symmetric multicategory Q tidy if it is freely symmetric with a category of objects ℂ equivalent to a discrete category. Throughout this section we say 'Q has object-category ℂ equivalent to S discrete' to mean that S is the set of isomorphism classes of ℂ, so ℂ is equipped with a morphism ℂ ∼−→ S. We begin by defining the construction used for 'labelling' as discussed above. The idea is to give a set of labels as a set over the isomorphism classes of objects of Q, and then to 'attach' the labels using the following pullback construction.

**Definition 2.1** Let Q be a tidy symmetric multicategory with category of objects ℂ equivalent to S discrete. Given a set X over S, that is, equipped with a function f : X −→ S, we define the pullback multicategory Q_X as follows.

• **Objects:** o(Q_X) is given by the pullback

[Pullback diagram]

X → ℂ
↓   ↓
S → S

Observe that the morphism on the left is an equivalence, so o(Q_X) is equivalent to X discrete. Write h for this morphism.

• **Arrows:** given objects a₁,... a_k,a ∈ o(Q_X) we have

Q_X(a₁,... ,a_k; a) ≅ Q(fh(a₁),... ,fh(a_k); fh(a)).

• Composition, identities and symmetric action are then inherited from Q.

We observe immediately that since Q is tidy, Q_X is tidy. Also note that if Q is object-discrete this definition corresponds to the definition of pullback symmetric multicategory given in [3].

We are now ready to describe the construction of opetopic sets.

**Definition 2.2** Let Q be a tidy symmetric multicategory with object-category ℂ equivalent to S discrete. A Q-opetopic set X is defined recursively as a set X(0) over S together with a Q_{X}^+-opetopic set X₁.

So a Q-opetopic set consists of, for each k ≥ 0:

• a tidy symmetric multicategory Q(k) with object-category ℂ(k) equivalent to S(k) discrete

• a set X(k) and function X(k) →f_k S(k)

where

Q(0) = Q
and Q(k + 1) = Q(k)_{X(k)}^+.

We refer to X₁ as the underlying Q(k)_{X(k)}^+-opetopic set of X.

We now define morphisms of opetopic sets. Suppose we have opetopic sets X and X' with notation as above, together with a morphism of symmetric multicategories

F : Q −→ Q'

and a function

F₀ : X(0) −→ X'(0)

such that the following diagram commutes

[Commutative diagram]

This induces a morphism

Q_{X(0)} −→ Q'_{X'(0)}

and so a morphism

Q_{X(0)}^+ −→ Q'_{X'(0)}^+.

We make the following definition.

**Definition 2.3** A morphism of Q-opetopic sets

F : X −→ X'

is given by:

• an underlying morphism of symmetric multicategories and function F₀ as above

• a morphism X₁ −→ X'₁ of their underlying opetopic sets, whose underlying morphism is induced as above.

So F consists of

• a morphism Q −→ Q'

• for each k ≥ 0 a function F_k : X(k) −→ X'(k) such that the following diagram commutes

[Commutative diagram]

where the map on the right hand side is induced as appropriate.

Note that the above notation for a Q-opetopic set X and morphism F will be used throughout this section, unless otherwise specified.

**Definition 2.4** An opetopic set is an I-opetopic set. A morphism of opetopic sets is a morphism of I-opetopic sets. We write **OSet** for the category of opetopic sets and their morphisms.

Eventually, a weak n-category is defined as an opetopic set with certain properties. The idea is that k-cells have underlying shapes given by the objects of I^{k+}. These are 'unlabelled' cells. To make these into fully labelled k-cells, we first give labels to the 0-cells, via the function X(0) −→ S(0), and then to 1-cells via X(1) −→ S(1), and so on. This idea may be captured in the following 'schematic' diagram.

[Large diagram showing the labelling process]

Bearing in mind our modified definitions, we use the Baez-Dolan terminology as follows.

**Definitions 2.5**

• A **k-dimensional cell** (or **k-cell**) is an element of X(k) (i.e. an isomorphism class of objects of Q(k)_{X(k)}).

• A **k-frame** is an isomorphism class of objects of Q(k) (i.e. an isomorphism class of arrows of Q(k − 1)_{X(k−1)}).

• A **k-opening** is an isomorphism class of arrows of Q(k −1), for k ≥ 1.

So a k-opening may acquire (k − 1)-cell labels and become a k-frame, which may itself acquire a label and become a k-cell. We refer to such a cell and frame as being in the original k-opening.

On objects, the above schematic diagram becomes:

[Detailed diagram showing progression from opetopes to cells]

Horizontal arrows represent the process of labelling, as shown; vertical arrows represent the process of 'moving up' dimensions. Starting with a k-opetope, we have from right to left the progressive labelling of 0-cells, 1-cells, and so on, to form a k-cell at the far left, the final stages being:

k-opening → k-frame → k-cell

A k-opening acquires labels as an arrow of Q(k − 1), becoming a k-frame as an arrow of Q(k − 1)_{X(k−1)}. That is, it has (k − 1)-cells as its source and a (k − 1)-cell as its target.

**Definition 2.6** A **k-niche** is a k-opening (i.e. arrow of Q(k − 1)) together with labels for its source only.

We may represent these notions as follows. Let f be an arrow of Q(k−1), so f specifies a k-opening which we might represent as

[Diagram of k-opening]

Then a niche in f is represented by

[Diagram of k-niche with labeled source]

where a₁,... a_r are 'valid' labels for the source elements of f; a k-frame is represented by

[Diagram of k-frame]

where a is a 'valid' label for the target of f. Finally a k-cell is represented by

[Diagram of k-cell]

Since all symmetric multicategories in question are tidy, we may in each case represent the same isomorphism class by any symmetric variant of the above diagrams. Also, we refer to k-cells as labelling k-opetopes, rather than isomorphism classes of k-opetopes.

#### 2.2 OSet is a presheaf category

In this section we prove the main result of this work, that the category of opetopic sets is a presheaf category, and moreover, that it is equivalent to the presheaf category

[O^{op}, Set].

To prove this we use [12], Theorem 5.26, in the case V = Set. This theorem is as follows.

**Theorem 2.7** Let ℂ be a V-category. In order that ℂ be equivalent to [ℰ^{op}, V] for some small category ℰ it is necessary and sufficient that ℂ be cocomplete, and that there be a set of small-projective objects in ℂ constituting a strong generator for ℂ.

We see from the proof of this theorem that if E is such a set and ℰ is the full subcategory of ℂ whose objects are the elements of E, then

ℂ ≃ [ℰ^{op}, V].

We prove the following propositions; the idea is to "realise" each isomorphism class of opetopes as an opetopic set; the set of these opetopic sets constitutes a strong generator as required.

**Proposition 2.8** **OSet** is cocomplete.

**Proposition 2.9** There is a full and faithful functor

G : O −→ **OSet**.

**Proposition 2.10** Let α ∈ O. Then G(α) is small-projective in **OSet**.

**Proposition 2.11** Let

E = ⨿{G(α) | α ∈ O} ⊆ **OSet**.

Then E is a strongly generating set for **OSet**.

**Corollary 2.12** **OSet** is a presheaf category.

**Corollary 2.13**

**OSet** ≃ [O^{op}, Set].

**Proof of Proposition 2.8.** Consider a diagram

D : I −→ **OSet**

where I is a small category. We seek to construct a limit Z for D; the set of cells of Z of shape α is given by a colimit of the sets of cells of shape α in each D(I).

We construct an opetopic set Z as follows. For each k ≥ 0, Z(k) is a colimit in **Set**:

Z(k) = ∫^{I∈I} D(I)(k).

Now for each k we need to give a function

F(k) : Z(k) −→ o(Q(k))

where

Q(k) = Q(k − 1)_{Z(k−1)}^+
Q(0) = I.

That is, for each α ∈ Z(k) we need to give its frame. Now

Z(k) = `_{I∈I} D(I)(k) / ∼

where ∼ is the equivalence relation generated by

D(u)(α_{I'}) ∼ α_I for all u : I −→ I' ∈ I
and α_I ∈ D(I)(k).

So α ∈ Z(k) is of the form [α_I] for some α_I ∈ D(I)(k) where [α_I] denotes the equivalence class of α_I with respect to ∼.

Now suppose the frame of α_I in D(I) is

(β₁,... ,β_j) ? −→ β

where β_i,β ∈ D(I)(k − 1) label some k-opetope x. We set the frame of [α_I] to be

([β₁],... ,[β_j]) ? −→ [β]

labelling the same opetope x. This is well-defined since a morphism of opetopic sets preserves frames of cells, so the frame of D(u)(α_I) is

(D(u)(β₁),... ,D(u)(β_j)) ? −→ D(u)(β)

also labelling k-opetope x. It follows from the universal properties of the colimits in **Set** that Z is a colimit for D, with coprojections induced from those in **Set**. Then, since **Set** is cocomplete, **OSet** is cocomplete. □

**Proof of Proposition 2.9.** Let α be a k-opetope. We express α as an opetopic set G(α) = α̂ as follows, using the usual notation for an opetopic set. The idea is that the m-cells are given by the m-faces of α.

For each m ≥ 0 set

X(m) = {[(x,f)] | x ∈ O_m and x →f α ∈ O
where [ ] denotes isomorphism class in O/α}.

So in particular we have

X(k) = {[(α, 1)]}

and for all m > k, X(m) = ∅. It remains to specify the frame of [(x,f)].

The frame is an object of

Q(m) = Q(m − 1)_{X(m−1)}^+

so an arrow of

Q(m − 2)_{X(m−2)}^+

labelled with elements of X(m − 1). Now such an arrow is a configuration for composing arrows of Q(m − 2)_{X(m−2)}; for the frame as above, this is given by the opetope x as a labelled tree. Then the (m − 1)-cell labels are given as follows. Write

x : y₁,... ,y_j −→ y

say, and so we have for each i a morphism

y_i −→ x

and a morphism

y −→ x ∈ O.

Then the labels in X(m − 1) are given by

[y_i −→ x →f α] ∈ X(m − 1)

and

[y −→ x →f α] ∈ X(m − 1).

Now, given a morphism

h : α −→ β ∈ O

we define

ĥ : α̂ −→ β̂ ∈ **OSet**

by

[(x,f)] ↦ [(x,h ◦ f)]

which is well-defined since if (x,f) ≅ (x',f') then (x,hf) ≅ (x',hf') in O/α. This is clearly a morphism of opetopic sets.

Observe that any morphism α̂ −→ β̂ must be of this form since the faces of α must be preserved. Moreover, if ĥ = ĝ then certainly [(α,h)] = [(α,g)]. But this gives (α,h) = (α,g) since there is a unique morphism α −→ α ∈ O namely the identity. So G is full and faithful as required. □

**Proof of Proposition 2.10.** For any α ∈ O_k we show that α̂ is small-projective, that is that the functor

ψ = **OSet**(α̂, −) : **OSet** −→ **Set**

preserves small colimits. First observe that for any opetopic set X

ψ(X) = **OSet**(α̂,X) ≅ {k-cells in X whose underlying k-opetope is α}
⊆ X(k)

and the action on a morphism F : X −→ Y is given by

ψ(F) = **OSet**(α̂,F) : **OSet**(α̂,X) −→ **OSet**(α̂,Y)
x ↦ F(x).

So ψ is the 'restriction' to the set of cells of shape α. This clearly preserves colimits since the cells of shape α in the colimit are given by a colimit of the sets cells of shape α in the original diagram. □

**Proof of Proposition 2.11.** First note that

α̂ = β̂ ⟺ α ≅ β ∈ O

so

E ≅ ⨿_k S_k

where for each k, S_k is the set of k-dimensional Leinster opetopes. Since each S_k is a set it follows that E is a set.

We need to show that, given a morphism of opetopic sets F : X −→ Y, we have

**OSet**(α̂,F) is an isomorphism for all α̂ ⟹ F is an isomorphism.

Now, we have seen above that

**OSet**(α̂,X) ≅ {cells of X of shape α}

so

**OSet**(α̂,F) = F|_α = F restricted to cells of shape α.

So

**OSet**(α̂,F) is an isomorphism for all α̂
⟺ F|_α is an isomorphism for all α ∈ O
⟺ F is an isomorphism.

□

**Proof of Corollary 2.12.** Follows from Propositions 2.8, 2.9, 2.10, 2.11 and [12] Theorem 5.26. □

**Proof of Corollary 2.13.** Let ℰ be the full subcategory of **OSet** whose objects are those of E. Since G is full and faithful, ℰ is the image of G and we have

O ≃ ℰ

and hence

**OSet** ≃ [ℰ^{op}, **Set**] ≃ [O^{op}, **Set**].

□

---

### النسخة العربية

في هذا القسم نفحص نظرية المجموعات الأوبتوبية. نبدأ بمتابعة تعديلاتنا على النظرية الأوبتوبية لتضمين نظرية المجموعات الأوبتوبية. ثم نستخدم نتائج [12] لإثبات أن فئة المجموعات الأوبتوبية مكافئة بالفعل لفئة الحزم الأمامية على O، فئة الأوبتوبات المعرفة في القسم 1. هذه هي النتيجة الرئيسية لهذا العمل.

تذكر أنه بالتكافؤات المثبتة في [6] و[5]، لدينا فئات مكافئة من الأوبتوبات والمالتيتوبات وأوبتوبات لينستر. لذا يمكننا تعريف فئات مكافئة من المجموعات الأوبتوبية بأخذ الحزم الأمامية على أي من هذه الفئات الثلاث. في التعريفات التالية، على الرغم من أن الأوبتوبات التي نعتبرها هي من نوع 'تعدد فئوي متماثل'، فإن الوصف المحدد لمجموعة أوبتوبية ليس بالضبط كحزمة أمامية على فئة هذه الأوبتوبات. المجموعات المعطاة في البيانات مفهرسة ليس بالأوبتوبات نفسها بل بأصناف تشاكل الأوبتوبات؛ لذا للوهلة الأولى يشبه هذا حزمة أمامية على فئة أوبتوبات لينستر. ومع ذلك، لا نتابع هذه المسألة هنا، حيث أن التكافؤات المثبتة في عملنا السابق كافية لأغراض هذا المقال.

نعتمد هذا العرض لتجنب تسمية نفس الخلايا بشكل متكرر وفقاً للتماثلات؛ أي أننا لا نحتفظ بنسخ من الخلايا المتشاكلة بالتماثلات.

#### 2.1 التعريفات

في [3]، تُعرَّف فئات n الضعيفة كمجموعات أوبتوبية تحقق شروط شمولية معينة. ومع ذلك، تُعرَّف المجموعات الأوبتوبية باستخدام تعدد فئوي متماثل فقط مع مجموعة من الكائنات؛ في ضوء نتائج عملنا السابق، نسعى لتعريف باستخدام تعدد فئوي متماثل مع فئة من الكائنات. التعريفات التي نقدمها هنا هي تلك المعطاة في [3] لكن مع تعديلات كما تتطلب نتائج عملنا السابق.

البيانات الأساسية لفئة n أوبتوبية معطاة بمجموعة أوبتوبية. تذكر أنه في [3]، بإعطاء تعدد فئوي متماثل Q، مجموعة Q-أوبتوبية X معطاة بـ، لكل k ≥ 0، تعدد فئوي متماثل Q(k) ومجموعة X(k) على o(Q(k))، حيث

Q(0) = Q
و Q(k + 1) = Q(k)_{X(k)}^+.

المجموعة الأوبتوبية هي إذن مجموعة I-أوبتوبية، حيث I هو التعدد الفئوي المتماثل مع كائن واحد وسهم واحد (متطابق).

الفكرة هي أن فئة المجموعات الأوبتوبية يجب أن تكون مكافئة لفئة الحزم الأمامية

[Opetope^{op}, Set].

لإثبات هذا نستخدم [12]، النظرية 5.26، في الحالة V = Set. الدالة التصنيفية

Opetope^{op} −→ Set

يمكن اعتبارها تخصيص مجموعة من 'الوسوم' لكل أوبتوب.

تذكر أنه لكل k، ℂ(k) مكافئة لفئة منفصلة. لذا يكفي تحديد 'وسوم' لكل صنف تشاكل من الأوبتوبات.

تذكر ([6]) أننا نسمي تعدداً فئوياً متماثلاً Q مرتباً إذا كان متماثلاً حراً مع فئة من الكائنات ℂ مكافئة لفئة منفصلة. في جميع أنحاء هذا القسم نقول 'Q له فئة-كائنات ℂ مكافئة لـ S منفصلة' لنعني أن S هي مجموعة أصناف تشاكل ℂ، لذا ℂ مجهزة بتشاكل ℂ ∼−→ S. نبدأ بتعريف البناء المستخدم للـ 'وسم' كما نوقش أعلاه. الفكرة هي إعطاء مجموعة من الوسوم كمجموعة على أصناف تشاكل كائنات Q، ثم 'إرفاق' الوسوم باستخدام بناء السحب العكسي التالي.

**التعريف 2.1** ليكن Q تعدداً فئوياً متماثلاً مرتباً مع فئة من الكائنات ℂ مكافئة لـ S منفصلة. بإعطاء مجموعة X على S، أي مجهزة بدالة f : X −→ S، نعرف التعدد الفئوي للسحب العكسي Q_X كما يلي.

• **الكائنات:** o(Q_X) معطى بالسحب العكسي

[مخطط السحب العكسي]

لاحظ أن التشاكل على اليسار تكافؤ، لذا o(Q_X) مكافئ لـ X منفصلة. نكتب h لهذا التشاكل.

• **الأسهم:** بإعطاء كائنات a₁,... a_k,a ∈ o(Q_X) لدينا

Q_X(a₁,... ,a_k; a) ≅ Q(fh(a₁),... ,fh(a_k); fh(a)).

• التركيب والمتطابقات والفعل المتماثل موروثة بعد ذلك من Q.

نلاحظ مباشرة أنه بما أن Q مرتب، Q_X مرتب. لاحظ أيضاً أنه إذا كان Q كائن-منفصل فإن هذا التعريف يتوافق مع تعريف التعدد الفئوي المتماثل للسحب العكسي المعطى في [3].

نحن الآن جاهزون لوصف بناء المجموعات الأوبتوبية.

**التعريف 2.2** ليكن Q تعدداً فئوياً متماثلاً مرتباً مع فئة-كائنات ℂ مكافئة لـ S منفصلة. مجموعة Q-أوبتوبية X معرفة بشكل استقرائي كمجموعة X(0) على S مع مجموعة Q_{X}^+-أوبتوبية X₁.

لذا مجموعة Q-أوبتوبية تتكون من، لكل k ≥ 0:

• تعدد فئوي متماثل مرتب Q(k) مع فئة-كائنات ℂ(k) مكافئة لـ S(k) منفصلة

• مجموعة X(k) ودالة X(k) →f_k S(k)

حيث

Q(0) = Q
و Q(k + 1) = Q(k)_{X(k)}^+.

نشير إلى X₁ كالمجموعة Q(k)_{X(k)}^+-الأوبتوبية الأساسية لـ X.

نعرف الآن تشاكلات المجموعات الأوبتوبية. لنفترض أن لدينا مجموعات أوبتوبية X وX' بالترميز أعلاه، مع تشاكل من التعدد الفئوي المتماثل

F : Q −→ Q'

ودالة

F₀ : X(0) −→ X'(0)

بحيث المخطط التالي يُبدّل

[مخطط تبديلي]

هذا يحث تشاكلاً

Q_{X(0)} −→ Q'_{X'(0)}

ولذا تشاكلاً

Q_{X(0)}^+ −→ Q'_{X'(0)}^+.

نقدم التعريف التالي.

**التعريف 2.3** تشاكل المجموعات Q-الأوبتوبية

F : X −→ X'

معطى بـ:

• تشاكل أساسي من التعدد الفئوي المتماثل ودالة F₀ كما أعلاه

• تشاكل X₁ −→ X'₁ من مجموعاتها الأوبتوبية الأساسية، الذي تشاكله الأساسي محث كما أعلاه.

لذا F يتكون من

• تشاكل Q −→ Q'

• لكل k ≥ 0 دالة F_k : X(k) −→ X'(k) بحيث المخطط التالي يُبدّل

[مخطط تبديلي]

حيث الدالة على اليد اليمنى محثة بشكل مناسب.

لاحظ أن الترميز أعلاه لمجموعة Q-أوبتوبية X وتشاكل F سيُستخدم في جميع أنحاء هذا القسم، ما لم يُحدد خلاف ذلك.

**التعريف 2.4** المجموعة الأوبتوبية هي مجموعة I-أوبتوبية. تشاكل المجموعات الأوبتوبية هو تشاكل المجموعات I-الأوبتوبية. نكتب **OSet** لفئة المجموعات الأوبتوبية وتشاكلاتها.

في النهاية، تُعرَّف فئة n ضعيفة كمجموعة أوبتوبية بخصائص معينة. الفكرة هي أن k-خلايا لها أشكال أساسية معطاة بكائنات I^{k+}. هذه خلايا 'غير موسومة'. لجعل هذه خلايا k موسومة بالكامل، نعطي أولاً وسوماً للـ 0-خلايا، عبر الدالة X(0) −→ S(0)، ثم لـ 1-خلايا عبر X(1) −→ S(1)، وهكذا. يمكن التعبير عن هذه الفكرة بالمخطط 'التخطيطي' التالي.

[مخطط كبير يُظهر عملية الوسم]

مع مراعاة تعريفاتنا المعدلة، نستخدم مصطلحات باييز-دولان كما يلي.

**التعريفات 2.5**

• **خلية k-بُعدية** (أو **k-خلية**) هي عنصر من X(k) (أي صنف تشاكل من كائنات Q(k)_{X(k)}).

• **k-إطار** هو صنف تشاكل من كائنات Q(k) (أي صنف تشاكل من أسهم Q(k − 1)_{X(k−1)}).

• **k-فتحة** هو صنف تشاكل من أسهم Q(k −1)، لـ k ≥ 1.

لذا k-فتحة قد تكتسب وسوم (k − 1)-خلية وتصبح k-إطار، الذي قد يكتسب هو نفسه وسماً ويصبح k-خلية. نشير إلى هذه الخلية والإطار كونهما في k-الفتحة الأصلية.

على الكائنات، المخطط التخطيطي أعلاه يصبح:

[مخطط مفصل يُظهر التقدم من الأوبتوبات إلى الخلايا]

الأسهم الأفقية تمثل عملية الوسم، كما هو موضح؛ الأسهم العمودية تمثل عملية 'الصعود' في الأبعاد. بدءاً من k-أوبتوب، لدينا من اليمين إلى اليسار الوسم التدريجي لـ 0-خلايا، 1-خلايا، وهكذا، لتشكيل k-خلية في أقصى اليسار، المراحل النهائية هي:

k-فتحة → k-إطار → k-خلية

k-فتحة تكتسب وسوماً كسهم من Q(k − 1)، لتصبح k-إطار كسهم من Q(k − 1)_{X(k−1)}. أي أنها لها (k − 1)-خلايا كمصدرها و(k − 1)-خلية كهدفها.

**التعريف 2.6** **k-حافة** هي k-فتحة (أي سهم من Q(k − 1)) مع وسوم لمصدرها فقط.

يمكننا تمثيل هذه المفاهيم كما يلي. لتكن f سهم من Q(k−1)، لذا f تحدد k-فتحة التي قد نمثلها كـ

[مخطط k-فتحة]

ثم حافة في f ممثلة بـ

[مخطط k-حافة مع مصدر موسوم]

حيث a₁,... a_r وسوم 'صالحة' لعناصر مصدر f؛ k-إطار ممثل بـ

[مخطط k-إطار]

حيث a وسم 'صالح' لهدف f. أخيراً k-خلية ممثلة بـ

[مخطط k-خلية]

نظراً لأن جميع التعدد الفئوي المتماثل المعني مرتب، يمكننا في كل حالة تمثيل نفس صنف التشاكل بأي متغير متماثل من المخططات أعلاه. أيضاً، نشير إلى k-خلايا كوسم لـ k-أوبتوبات، بدلاً من أصناف تشاكل k-أوبتوبات.

#### 2.2 OSet فئة حزم أمامية

في هذا القسم نُثبت النتيجة الرئيسية لهذا العمل، أن فئة المجموعات الأوبتوبية فئة حزم أمامية، وعلاوة على ذلك، أنها مكافئة لفئة الحزم الأمامية

[O^{op}, Set].

لإثبات هذا نستخدم [12]، النظرية 5.26، في الحالة V = Set. هذه النظرية كما يلي.

**النظرية 2.7** لتكن ℂ فئة V. لكي تكون ℂ مكافئة لـ [ℰ^{op}, V] لبعض الفئة الصغيرة ℰ من الضروري والكافي أن تكون ℂ مكتملة استقرائياً، وأن يكون هناك مجموعة من الكائنات صغيرة-إسقاطية في ℂ تشكل مولداً قوياً لـ ℂ.

نرى من برهان هذه النظرية أنه إذا كان E هذه المجموعة وℰ هي الفئة الجزئية الكاملة من ℂ التي كائناتها عناصر E، ثم

ℂ ≃ [ℰ^{op}, V].

نُثبت القضايا التالية؛ الفكرة هي "تحقيق" كل صنف تشاكل من الأوبتوبات كمجموعة أوبتوبية؛ مجموعة هذه المجموعات الأوبتوبية تشكل مولداً قوياً كما هو مطلوب.

**القضية 2.8** **OSet** مكتملة استقرائياً.

**القضية 2.9** يوجد دالة تصنيفية كاملة وموثوقة

G : O −→ **OSet**.

**القضية 2.10** ليكن α ∈ O. ثم G(α) صغيرة-إسقاطية في **OSet**.

**القضية 2.11** لتكن

E = ⨿{G(α) | α ∈ O} ⊆ **OSet**.

ثم E مجموعة مولدة قوياً لـ **OSet**.

**النتيجة 2.12** **OSet** فئة حزم أمامية.

**النتيجة 2.13**

**OSet** ≃ [O^{op}, Set].

**برهان القضية 2.8.** نعتبر مخططاً

D : I −→ **OSet**

حيث I فئة صغيرة. نسعى لبناء حد استقرائي Z لـ D؛ مجموعة خلايا Z من شكل α معطاة بحد استقرائي من مجموعات خلايا شكل α في كل D(I).

نبني مجموعة أوبتوبية Z كما يلي. لكل k ≥ 0، Z(k) حد استقرائي في **Set**:

Z(k) = ∫^{I∈I} D(I)(k).

الآن لكل k نحتاج لإعطاء دالة

F(k) : Z(k) −→ o(Q(k))

حيث

Q(k) = Q(k − 1)_{Z(k−1)}^+
Q(0) = I.

أي لكل α ∈ Z(k) نحتاج لإعطاء إطاره. الآن

Z(k) = `_{I∈I} D(I)(k) / ∼

حيث ∼ علاقة تكافؤ مولدة بـ

D(u)(α_{I'}) ∼ α_I لجميع u : I −→ I' ∈ I
وα_I ∈ D(I)(k).

لذا α ∈ Z(k) من الشكل [α_I] لبعض α_I ∈ D(I)(k) حيث [α_I] يدل على صنف تكافؤ α_I بالنسبة لـ ∼.

الآن لنفترض أن إطار α_I في D(I) هو

(β₁,... ,β_j) ? −→ β

حيث β_i,β ∈ D(I)(k − 1) توسم بعض k-أوبتوب x. نضع إطار [α_I] ليكون

([β₁],... ,[β_j]) ? −→ [β]

يوسم نفس الأوبتوب x. هذا محدد جيداً حيث أن تشاكل المجموعات الأوبتوبية يحفظ أطر الخلايا، لذا إطار D(u)(α_I) هو

(D(u)(β₁),... ,D(u)(β_j)) ? −→ D(u)(β)

يوسم أيضاً k-أوبتوب x. يتبع من الخصائص الشمولية للحدود الاستقرائية في **Set** أن Z حد استقرائي لـ D، مع إسقاطات مشتركة محثة من تلك في **Set**. ثم، بما أن **Set** مكتملة استقرائياً، **OSet** مكتملة استقرائياً. □

**برهان القضية 2.9.** ليكن α k-أوبتوب. نعبر عن α كمجموعة أوبتوبية G(α) = α̂ كما يلي، باستخدام الترميز المعتاد لمجموعة أوبتوبية. الفكرة هي أن m-خلايا معطاة بـ m-وجوه α.

لكل m ≥ 0 نضع

X(m) = {[(x,f)] | x ∈ O_m وx →f α ∈ O
حيث [ ] يدل على صنف تشاكل في O/α}.

لذا بشكل خاص لدينا

X(k) = {[(α, 1)]}

ولجميع m > k، X(m) = ∅. يبقى تحديد إطار [(x,f)].

الإطار كائن من

Q(m) = Q(m − 1)_{X(m−1)}^+

لذا سهم من

Q(m − 2)_{X(m−2)}^+

موسوم بعناصر من X(m − 1). الآن هذا السهم تكوين لتركيب أسهم Q(m − 2)_{X(m−2)}؛ للإطار كما أعلاه، هذا معطى بالأوبتوب x كشجرة موسومة. ثم وسوم (m − 1)-الخلايا معطاة كما يلي. نكتب

x : y₁,... ,y_j −→ y

قل، ولذا لدينا لكل i تشاكل

y_i −→ x

وتشاكل

y −→ x ∈ O.

ثم الوسوم في X(m − 1) معطاة بـ

[y_i −→ x →f α] ∈ X(m − 1)

و

[y −→ x →f α] ∈ X(m − 1).

الآن، بإعطاء تشاكل

h : α −→ β ∈ O

نعرف

ĥ : α̂ −→ β̂ ∈ **OSet**

بـ

[(x,f)] ↦ [(x,h ◦ f)]

الذي محدد جيداً حيث أنه إذا (x,f) ≅ (x',f') ثم (x,hf) ≅ (x',hf') في O/α. هذا واضح أنه تشاكل مجموعات أوبتوبية.

لاحظ أن أي تشاكل α̂ −→ β̂ يجب أن يكون من هذا الشكل حيث أن وجوه α يجب أن تُحفظ. علاوة على ذلك، إذا ĥ = ĝ ثم بالتأكيد [(α,h)] = [(α,g)]. لكن هذا يعطي (α,h) = (α,g) حيث أن هناك تشاكلاً فريداً α −→ α ∈ O وهو المتطابق. لذا G كاملة وموثوقة كما هو مطلوب. □

**برهان القضية 2.10.** لأي α ∈ O_k نُظهر أن α̂ صغيرة-إسقاطية، أي أن الدالة التصنيفية

ψ = **OSet**(α̂, −) : **OSet** −→ **Set**

تحفظ الحدود الاستقرائية الصغيرة. أولاً لاحظ أنه لأي مجموعة أوبتوبية X

ψ(X) = **OSet**(α̂,X) ≅ {k-خلايا في X التي k-أوبتوبها الأساسي α}
⊆ X(k)

والفعل على تشاكل F : X −→ Y معطى بـ

ψ(F) = **OSet**(α̂,F) : **OSet**(α̂,X) −→ **OSet**(α̂,Y)
x ↦ F(x).

لذا ψ هو 'التقييد' إلى مجموعة خلايا شكل α. هذا يحفظ بوضوح الحدود الاستقرائية حيث أن خلايا شكل α في الحد الاستقرائي معطاة بحد استقرائي من مجموعات خلايا شكل α في المخطط الأصلي. □

**برهان القضية 2.11.** لاحظ أولاً أن

α̂ = β̂ ⟺ α ≅ β ∈ O

لذا

E ≅ ⨿_k S_k

حيث لكل k، S_k مجموعة k-بُعدية من أوبتوبات لينستر. بما أن كل S_k مجموعة يتبع أن E مجموعة.

نحتاج لإظهار أنه بإعطاء تشاكل مجموعات أوبتوبية F : X −→ Y، لدينا

**OSet**(α̂,F) تشاكل لجميع α̂ ⟹ F تشاكل.

الآن، رأينا أعلاه أن

**OSet**(α̂,X) ≅ {خلايا X من شكل α}

لذا

**OSet**(α̂,F) = F|_α = F مقيد لخلايا شكل α.

لذا

**OSet**(α̂,F) تشاكل لجميع α̂
⟺ F|_α تشاكل لجميع α ∈ O
⟺ F تشاكل.

□

**برهان النتيجة 2.12.** يتبع من القضايا 2.8، 2.9، 2.10، 2.11 و[12] النظرية 5.26. □

**برهان النتيجة 2.13.** لتكن ℰ الفئة الجزئية الكاملة من **OSet** التي كائناتها تلك من E. بما أن G كاملة وموثوقة، ℰ هي صورة G ولدينا

O ≃ ℰ

ولذا

**OSet** ≃ [ℰ^{op}, **Set**] ≃ [O^{op}, **Set**].

□

---

### Translation Notes

- **Figures referenced:** Multiple diagrams (pullbacks, commutative diagrams, schematic diagrams)
- **Key terms introduced:** opetopic set (مجموعة أوبتوبية), tidy multicategory (تعدد فئوي مرتب), pullback (سحب عكسي), colimit (حد استقرائي), k-cell (k-خلية), k-frame (k-إطار), k-opening (k-فتحة), k-niche (k-حافة), small-projective (صغيرة-إسقاطية), cocomplete (مكتملة استقرائياً), strong generator (مولد قوي)
- **Equations:** Multiple mathematical formulas and category-theoretic constructions
- **Citations:** [3], [5], [6], [12]
- **Special handling:**
  - Definitions 2.1-2.6 numbered as in original
  - Theorem 2.7 and Propositions 2.8-2.11 preserved
  - Corollaries 2.12-2.13 maintained
  - Proof structures with البرهان and □
  - All category-theoretic notation preserved
  - Diagrams described textually

### Quality Metrics

- Semantic equivalence: 0.85
- Technical accuracy: 0.86
- Readability: 0.84
- Glossary consistency: 0.86
- **Overall section score:** 0.85
