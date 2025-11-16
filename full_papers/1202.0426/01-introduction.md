# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** category, 2-category, abelian, functor, exact functor, definable, coherent, morphism, algebraic, model theory

---

### English Version

This paper is about three 2-categories which sit at an intersection of algebra, model theory and geometry (the last in the broad sense).

One of these categories, ABEX, has for its objects the skeletally small abelian categories and for its morphisms the exact functors; another, DEF, is the category of definable additive categories and interpretation functors; the third is the category, COH, of locally coherent Grothendieck categories and coherent morphisms. In each case the 2-arrows are just the natural transformations. The (anti-)equivalences between these were described in [45], which builds on [43] and [30], and are recalled below (see also [34] and [25] for analogous results). Here these categories and their connections are explored further.

I have tried to include enough explanation of background to make the paper accessible to a variety of readers; for more details one should consult the various references cited. I will use [42] as a convenient reference since it gathers together much of what I will need but [23], [29], [43] also contain much of that.

Throughout this paper, categories are, by default, preadditive, functor means additive functor, (A,B) will denote the category of additive functors from the (usually skeletally small) preadditive category A to the (usually at least additive) category B, Ab will denote the category of abelian groups, Mod-A will be an alternative notation for (A^op, Ab) (where op denotes the opposite of a category) - it is the category of right A-modules - and A-Mod = (A,Ab) will denote the category of left A-modules. The full subcategory of finitely presented modules is denoted by mod-A. We write PREADD for the 2-category of preadditive categories (additive functors and natural transformations). We scarcely distinguish between a skeletally small category and a small version of it (i.e. a category to which it is equivalent but which has just a set of objects).

Now we show how the three 2-categories are related, then give a quick summary of what is in each section.

**Theorem 1.1.** [45, 2.3 and comments following] There is a diagram of equivalences and anti-equivalences between ABEX, COH and DEF as follows.

ABEX ≃^op ↔ DEF
   ↓≃        ↑≃
  COH  ←→  COH

Explicitly:
A = fun(D) = G_fp
D = Abs(G) = Ex(A,Ab)
G = Flat-A = Fun(D)

We will need the details of these (anti-)equivalences, so here they are.

**From ABEX to DEF:** to a skeletally small abelian category A we associate the definable category Ex(A,Ab) - the full subcategory of A-Mod on those functors which are exact; to an exact functor F:A→B, we associate the functor F*: Ex(B,Ab)→Ex(A,Ab) which is just precomposition with F.

**From DEF to ABEX:** to a definable category D we associate the category, fun(D) = (D,Ab)^{→∏}, of functors from D which commute with direct limits and direct products (we write fun-R in the case that D = Mod-R); to an interpretation functor, that is, a functor I:C→D which commutes with direct products and direct limits, we associate the functor I^0: fun(D)→fun(C) which is precomposition with I.

**Between ABEX and COH (on objects):** to a locally coherent Grothendieck category G we assign its full subcategory, G_fp, of finitely presented objects; in the other direction, to a skeletally small abelian category A we assign the category Lex(A^op,Ab) of left exact functors on A^op, thus right exact functors on A, so this includes the representable functors (-,A) for A∈A. This is a locally coherent Grothendieck category and the image of A under the just-mentioned Yoneda embedding A↦(-,A) is equivalent to the full subcategory of finitely presented objects (see 4.1, also for the identifications Lex(A^op,Ab)≃Flat-A≃Ind(A)).

**Between ABEX and COH (on morphisms):** from a morphism f∈Ex(A,B) we define the coherent morphism (see Section 4) (f*,f*): H = Ind(B)→Ind(A) = G which has f*: H = Lex(B^op,Ab)→Lex(A^op,Ab) = G just precomposition with f^op and has f* = Ind(f). In the other direction we take a coherent morphism (f*,f*) to the restriction of the left adjoint, f*, to the finitely presented objects of G.

The as-yet-unexplained notation Abs(G) refers to the full subcategory of absolutely pure (or fp-injective) objects of G - those objects G such that Ext^1(G_fp,G) = 0.

The next result, which is not difficult to show (or see [44]), is one instance of this picture. By A(R) we denote the smallest abelian (not necessarily full) subcategory of Mod-R which contains mod-R (see [45,§6], also Section 2.4 below). By ⟨X⟩ we denote the smallest definable subcategory of Mod-R containing X.

**Proposition 1.2.** If R is any skeletally small preadditive category then
Ex(A(R)^op,Ab)≃⟨Abs-R⟩.
If R is right coherent, so Abs-R is a definable subcategory of Mod-R, then
Ex((mod-R)^op,Ab)≃Abs-R.

Note the duality which applies to the whole picture described above. It is obvious for ABEX, on which it is the 2-category equivalence which takes each abelian category to its opposite. It follows that there is a corresponding self-equivalence on each of the other two categories (which will be described in the relevant section). In the context of the model theory of definable subcategories of module categories this duality was found first for pp formulas, and termed elementary duality ([39]) then extended to the category of pp-pairs and the Ziegler spectrum in [22]. In an algebraic form it is in [5] and [21].

For instance, the dual to the result above is the following.

**Proposition 1.3.** If R is any skeletally small preadditive category then
Ex(A(R),Ab)≃⟨R-Flat⟩.
If R is right coherent, so A(R) = mod-R and R-Flat is a definable subcategory of R-Mod, then
Ex(mod-R,Ab)≃R-Flat.

In Section 2 we identify the finitely presented objects of ABEX as the finite type localisations of free abelian categories of finitely presented rings and we show that every small abelian category is a direct limit - "directed colimit" in the more category-theoretic terminology - of such categories. Since ABEX also has directed colimits in a suitable 2-category sense we could therefore say that ABEX is finitely accessible (in some 2-category sense). We show that ABEX has pullbacks and also characterise the monomorphisms (and say a little about the epimorphisms) of this category.

The main result of Section 3 is that the structure of DEF - arrows and 2-arrows as well as the objects - is essentially determined by the full subcategories of pure-injective objects. We also show that if A is skeletally small abelian then Ex(A,D) is definable for any definable Grothendieck (so, 3.6, locally finitely presented) category D (not just when D=Ab).

Section 4 is devoted to developing an additive version of things (coherent morphisms, classifying toposes, points) that are familiar in the context of toposes. The parallel is well-known but we develop it further here as part of the larger additive picture.

---

### النسخة العربية

تدور هذه الورقة حول ثلاث فئات ثنائية تقع عند تقاطع الجبر ونظرية النماذج والهندسة (الأخيرة بالمعنى الواسع).

إحدى هذه الفئات، ABEX، لها كأشياء الفئات الأبيلية الصغيرة هيكلياً وكتشاكلات الدوال التصنيفية التامة؛ والأخرى، DEF، هي فئة الفئات الجمعية القابلة للتعريف ودوال التفسير؛ والثالثة هي الفئة، COH، من فئات غروتنديك المتماسكة موضعياً والتشاكلات المتماسكة. في كل حالة، الأسهم الثنائية هي فقط التحويلات الطبيعية. التكافؤات (العكسية) بين هذه الفئات تم وصفها في [45]، والتي تبني على [43] و [30]، ويتم استرجاعها أدناه (انظر أيضاً [34] و [25] لنتائج مماثلة). هنا يتم استكشاف هذه الفئات وارتباطاتها بشكل أعمق.

لقد حاولت تضمين شرح كافٍ للخلفية لجعل الورقة قابلة للوصول لمجموعة متنوعة من القراء؛ للحصول على مزيد من التفاصيل، يجب استشارة المراجع المختلفة المذكورة. سأستخدم [42] كمرجع مناسب لأنه يجمع الكثير مما سأحتاجه، لكن [23] و [29] و [43] تحتوي أيضاً على الكثير من ذلك.

في جميع أنحاء هذه الورقة، الفئات هي، بشكل افتراضي، جمعية أولية، والدالة التصنيفية تعني دالة تصنيفية جمعية، (A,B) سيشير إلى فئة الدوال التصنيفية الجمعية من الفئة الجمعية الأولية (عادة صغيرة هيكلياً) A إلى الفئة (عادة جمعية على الأقل) B، Ab ستشير إلى فئة الزمر الأبيلية، Mod-A ستكون تدويناً بديلاً لـ (A^op, Ab) (حيث op تشير إلى عكس الفئة) - وهي فئة وحدات A اليمنى - و A-Mod = (A,Ab) ستشير إلى فئة وحدات A اليسرى. الفئة الفرعية الكاملة للوحدات المقدمة بشكل منته تُشار إليها بـ mod-A. نكتب PREADD للفئة الثنائية للفئات الجمعية الأولية (الدوال التصنيفية الجمعية والتحويلات الطبيعية). نحن بالكاد نميز بين فئة صغيرة هيكلياً ونسخة صغيرة منها (أي فئة مكافئة لها ولكن لها مجموعة من الأشياء فقط).

الآن نبين كيف ترتبط الفئات الثنائية الثلاث، ثم نعطي ملخصاً سريعاً لما هو موجود في كل قسم.

**المبرهنة 1.1.** [45، 2.3 والتعليقات التالية] يوجد مخطط للتكافؤات والتكافؤات العكسية بين ABEX و COH و DEF كما يلي.

ABEX ≃^op ↔ DEF
   ↓≃        ↑≃
  COH  ←→  COH

بشكل صريح:
A = fun(D) = G_fp
D = Abs(G) = Ex(A,Ab)
G = Flat-A = Fun(D)

سنحتاج إلى تفاصيل هذه التكافؤات (العكسية)، لذا إليها.

**من ABEX إلى DEF:** لفئة أبيلية صغيرة هيكلياً A نربط الفئة القابلة للتعريف Ex(A,Ab) - الفئة الفرعية الكاملة من A-Mod على تلك الدوال التصنيفية التي هي تامة؛ لدالة تصنيفية تامة F:A→B، نربط الدالة التصنيفية F*: Ex(B,Ab)→Ex(A,Ab) التي هي فقط تركيب مسبق مع F.

**من DEF إلى ABEX:** لفئة قابلة للتعريف D نربط الفئة، fun(D) = (D,Ab)^{→∏}، من الدوال التصنيفية من D التي تتبادل مع الحدود المباشرة والجداءات المباشرة (نكتب fun-R في الحالة التي D = Mod-R)؛ لدالة تفسير، أي دالة تصنيفية I:C→D التي تتبادل مع الجداءات المباشرة والحدود المباشرة، نربط الدالة التصنيفية I^0: fun(D)→fun(C) التي هي تركيب مسبق مع I.

**بين ABEX و COH (على الأشياء):** لفئة غروتنديك متماسكة موضعياً G نخصص فئتها الفرعية الكاملة، G_fp، من الأشياء المقدمة بشكل منته؛ في الاتجاه الآخر، لفئة أبيلية صغيرة هيكلياً A نخصص الفئة Lex(A^op,Ab) من الدوال التصنيفية التامة يساراً على A^op، وبالتالي الدوال التصنيفية التامة يميناً على A، لذا يتضمن هذا الدوال التصنيفية القابلة للتمثيل (-,A) لـ A∈A. هذه فئة غروتنديك متماسكة موضعياً وصورة A تحت تضمين يونيدا المذكور للتو A↦(-,A) مكافئة للفئة الفرعية الكاملة من الأشياء المقدمة بشكل منته (انظر 4.1، أيضاً للمطابقات Lex(A^op,Ab)≃Flat-A≃Ind(A)).

**بين ABEX و COH (على التشاكلات):** من تشاكل f∈Ex(A,B) نعرف التشاكل المتماسك (انظر القسم 4) (f*,f*): H = Ind(B)→Ind(A) = G الذي له f*: H = Lex(B^op,Ab)→Lex(A^op,Ab) = G فقط تركيب مسبق مع f^op وله f* = Ind(f). في الاتجاه الآخر، نأخذ تشاكلاً متماسكاً (f*,f*) إلى تقييد المساعد الأيسر، f*، على الأشياء المقدمة بشكل منته من G.

يشير الترميز الذي لم يتم شرحه بعد Abs(G) إلى الفئة الفرعية الكاملة من الأشياء النقية تماماً (أو قابلة للحقن fp) من G - تلك الأشياء G بحيث Ext^1(G_fp,G) = 0.

النتيجة التالية، التي ليس من الصعب إظهارها (أو انظر [44])، هي مثال واحد على هذه الصورة. بـ A(R) نشير إلى أصغر فئة فرعية أبيلية (ليست بالضرورة كاملة) من Mod-R التي تحتوي على mod-R (انظر [45,§6]، أيضاً القسم 2.4 أدناه). بـ ⟨X⟩ نشير إلى أصغر فئة فرعية قابلة للتعريف من Mod-R تحتوي على X.

**القضية 1.2.** إذا كانت R أي فئة جمعية أولية صغيرة هيكلياً فإن
Ex(A(R)^op,Ab)≃⟨Abs-R⟩.
إذا كانت R متماسكة يميناً، بحيث Abs-R فئة فرعية قابلة للتعريف من Mod-R، فإن
Ex((mod-R)^op,Ab)≃Abs-R.

لاحظ الثنائية التي تنطبق على الصورة الكاملة الموصوفة أعلاه. إنها واضحة لـ ABEX، والتي عليها يكون التكافؤ للفئة الثنائية هو الذي يأخذ كل فئة أبيلية إلى عكسها. يتبع من ذلك أن هناك تكافؤاً ذاتياً مقابلاً على كل من الفئتين الأخريين (والذي سيتم وصفه في القسم ذي الصلة). في سياق نظرية النماذج للفئات الفرعية القابلة للتعريف من فئات الوحدات، تم العثور على هذه الثنائية أولاً لصيغ pp، وأطلق عليها الثنائية الأساسية ([39]) ثم تم توسيعها إلى فئة أزواج pp وطيف زيغلر في [22]. في شكل جبري، موجودة في [5] و [21].

على سبيل المثال، الثنائي للنتيجة أعلاه هو التالي.

**القضية 1.3.** إذا كانت R أي فئة جمعية أولية صغيرة هيكلياً فإن
Ex(A(R),Ab)≃⟨R-Flat⟩.
إذا كانت R متماسكة يميناً، بحيث A(R) = mod-R و R-Flat فئة فرعية قابلة للتعريف من R-Mod، فإن
Ex(mod-R,Ab)≃R-Flat.

في القسم 2 نحدد الأشياء المقدمة بشكل منته من ABEX كموضعات النوع المنته للفئات الأبيلية الحرة للحلقات المقدمة بشكل منته ونبين أن كل فئة أبيلية صغيرة هي حد مباشر - "حد مشترك موجه" في المصطلحات الأكثر نظرية فئوية - لمثل هذه الفئات. بما أن ABEX لديها أيضاً حدود مشتركة موجهة بمعنى فئة ثنائية مناسب، يمكننا بالتالي أن نقول إن ABEX قابلة للوصول بشكل منته (بمعنى فئة ثنائية ما). نبين أن ABEX لديها سحوبات ونميز أيضاً التشاكلات الأحادية (ونقول قليلاً عن التشاكلات التامة) لهذه الفئة.

النتيجة الرئيسية للقسم 3 هي أن بنية DEF - الأسهم والأسهم الثنائية بالإضافة إلى الأشياء - يتم تحديدها بشكل أساسي بواسطة الفئات الفرعية الكاملة من الأشياء القابلة للحقن النقي. نبين أيضاً أنه إذا كانت A أبيلية صغيرة هيكلياً فإن Ex(A,D) قابلة للتعريف لأي فئة غروتنديك قابلة للتعريف (وبالتالي، 3.6، مقدمة موضعياً بشكل منته) D (وليس فقط عندما D=Ab).

القسم 4 مخصص لتطوير نسخة جمعية من الأشياء (التشاكلات المتماسكة، التوبوسات المصنفة، النقاط) التي هي مألوفة في سياق التوبوسات. التوازي معروف جيداً لكننا نطوره أكثر هنا كجزء من الصورة الجمعية الأكبر.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** ABEX, DEF, COH, exact functor, definable category, interpretation functor, locally coherent Grothendieck category, coherent morphism, preadditive category, Yoneda embedding, absolutely pure objects, fp-injective
- **Equations:** Several categorical equivalences and isomorphisms
- **Citations:** [5], [21], [22], [23], [25], [29], [30], [34], [39], [42], [43], [44], [45]
- **Special handling:**
  - Mathematical notation preserved (superscripts, subscripts, arrows)
  - Category names kept in English (ABEX, DEF, COH, PREADD)
  - Technical terms like "mod-A", "Mod-A", "A-Mod" kept in original form
  - Theorem and Proposition numbering maintained

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.87

### Back-Translation Sample (First Paragraph)

This paper revolves around three 2-categories located at the intersection of algebra, model theory, and geometry (the latter in the broad sense).

One of these categories, ABEX, has as objects the structurally small abelian categories and as morphisms the exact functors; another, DEF, is the category of definable additive categories and interpretation functors; and the third is the category, COH, of locally coherent Grothendieck categories and coherent morphisms. In each case, the 2-arrows are just the natural transformations. The (anti-)equivalences between these categories were described in [45], which builds on [43] and [30], and are recalled below (see also [34] and [25] for analogous results). Here these categories and their connections are explored more deeply.
