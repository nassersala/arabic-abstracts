# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** category, fibration, type theory, indexed, contextual category, model category, pullback, Π-types, identity types, extension types, pushouts, localization, quasicategories

---

### English Version

Indexed categories were defined in [10] (see also [6, B1]). We defined an analogue of this notion using the language of indexed type theories which were defined in [5] as certain algebraic theories. A contextually indexed contextual category is a model of such a theory. We will show how to construct such a model from a category with fibrations and some additional structure. Our construction is based on constructions from [12, 8] which were defined for ordinary type theory.

We use the local universes construction to make constructions stable under substitution and reindexing. To get an unstable interpretation, we use the notion of a type-theoretic semi-fibration category. This is a category with fibrations with additional structure which allows us to interpret unit types, Σ-types, and identity types. We do not require that all objects of a type-theoretic semi-fibration category are fibrant and we also do not require right properness. The reason is that right properness implies that corresponding contextually indexed category is locally Cartesian closed and we want to work with models which are not. Without right properness we cannot require all objects to be fibrant since we need to work with objects of the form Πp(q), where p and q are fibrations, and such an object is fibrant only if the category is right proper.

We also show how to construct extension types, products, and stable and unstable colimits. Extension types were defined in [11]. They generalize Π-types and identity types. We use them to give a description of pushouts and other higher inductive types which is based on constructions from [7]. To construct unstable pushouts (and other colimits), we need to modify this argument. We proved in [5] that the existence of pushouts in the empty context implies the existence of unstable pushouts. A minor modification of the construction from [7] gives us pushouts in the empty context.

We will prove that localizations of model categories are closed under identity types. This implies that if identity types are extensional in a model category, then they are also extensional in its localizations. This gives us many examples of contextually indexed contextual categories with finite limits since extensionality of identity types implies the existence of equalizers as was proved in [5].

Finally, we give one example of a type-theoretic semi-fibration category: namely, the category of simplicial sets with the Joyal model structure. We will show that it gives rise to a locally small Cartesian closed contextually indexed contextual category with dependent limits and colimits. To prove that it is Cartesian closed and has pushouts in the empty context, we define a functor G : sSet → sSet. Every edge in a simplicial set of the form G(X) is invertible. This implies that if X is a quasicategory, then G(X) is a Kan complex. In general, G(X) might not be a Kan complex, but it has many useful properties of Kan complexes. For example, every categorical fibration of the form Y → G(X) is a Cartesian fibration and every map of the form G(Y) → G(X) factors into a categorical trivial cofibration followed by a Kan fibration.

The paper is organized as follows. In section 2, we define contextually indexed contextual categories and show how to construct such categories from categories with fibrations. In section 3, we define type-theoretic semi-fibration categories and prove that corresponding contextually indexed contextual categories have unit types, Σ-types, and identity types. In section 4, we discuss extension types. In section 5, we construct dependent coproducts, pushouts, binary coproducts, and initial types. In section 6, we show that localizations of model categories are closed under identity types. In section 7, we discuss the contextually indexed contextual category constructed from quasicategories.

---

### النسخة العربية

تم تعريف الفئات المفهرسة في [10] (انظر أيضاً [6, B1]). عرّفنا نظيراً لهذا المفهوم باستخدام لغة نظريات الأنواع المفهرسة التي تم تعريفها في [5] كنظريات جبرية معينة. الفئة السياقية المفهرسة سياقياً هي نموذج لمثل هذه النظرية. سنُظهر كيفية بناء مثل هذا النموذج من فئة مع ألياف وبعض البنية الإضافية. يعتمد بناؤنا على بنى من [12, 8] تم تعريفها لنظرية الأنواع العادية.

نستخدم بناء الأكوان المحلية لجعل البنى مستقرة تحت التعويض وإعادة الفهرسة. للحصول على تفسير غير مستقر، نستخدم مفهوم فئة شبه الألياف النوعية النظرية. هذه فئة مع ألياف ذات بنية إضافية تسمح لنا بتفسير أنواع الوحدة، وأنواع Σ، وأنواع الهوية. لا نتطلب أن تكون جميع عناصر فئة شبه الألياف النوعية النظرية ليفية، كما لا نتطلب الصحة اليمنى. السبب هو أن الصحة اليمنى تعني أن الفئة المفهرسة سياقياً المقابلة مغلقة ديكارتياً محلياً ونريد العمل مع نماذج ليست كذلك. بدون الصحة اليمنى لا يمكننا أن نتطلب أن تكون جميع العناصر ليفية لأننا نحتاج للعمل مع عناصر من الشكل Πp(q)، حيث p و q أليا، ومثل هذا العنصر ليفي فقط إذا كانت الفئة صحيحة يمنياً.

نُظهر أيضاً كيفية بناء أنواع التمديد، والجدءات، والحدود المشتركة المستقرة وغير المستقرة. تم تعريف أنواع التمديد في [11]. إنها تُعمم أنواع Π وأنواع الهوية. نستخدمها لإعطاء وصف للدفعات وأنواع حثية عليا أخرى يعتمد على بنى من [7]. لبناء الدفعات غير المستقرة (والحدود المشتركة الأخرى)، نحتاج لتعديل هذه الحجة. أثبتنا في [5] أن وجود الدفعات في السياق الفارغ يعني وجود الدفعات غير المستقرة. تعديل طفيف للبناء من [7] يعطينا الدفعات في السياق الفارغ.

سنُثبت أن توطينات الفئات النموذجية مغلقة تحت أنواع الهوية. هذا يعني أنه إذا كانت أنواع الهوية امتدادية في فئة نموذجية، فإنها أيضاً امتدادية في توطيناتها. هذا يعطينا أمثلة عديدة على الفئات السياقية المفهرسة سياقياً ذات الحدود المنتهية حيث أن امتدادية أنواع الهوية تعني وجود المعادِلات كما تم إثباته في [5].

أخيراً، نعطي مثالاً واحداً على فئة شبه ألياف نوعية نظرية: وهي فئة المجموعات البسيطة مع بنية نموذج جويال. سنُظهر أنها تُنتج فئة سياقية مفهرسة سياقياً ديكارتية مغلقة محلياً صغيرة مع حدود وحدود مشتركة معتمدة. لإثبات أنها ديكارتية مغلقة ولديها دفعات في السياق الفارغ، نُعرِّف دالة G : sSet → sSet. كل حافة في مجموعة بسيطة من الشكل G(X) قابلة للعكس. هذا يعني أنه إذا كانت X فئة شبه، فإن G(X) مُركب كان. بشكل عام، قد لا يكون G(X) مُركب كان، لكن له خصائص مفيدة كثيرة من مركبات كان. على سبيل المثال، كل ليف فئوي من الشكل Y → G(X) هو ليف ديكارتي وكل خريطة من الشكل G(Y) → G(X) تتحلل إلى ليف مشترك تافه فئوي متبوعاً بليف كان.

الورقة منظمة كما يلي. في القسم 2، نُعرِّف الفئات السياقية المفهرسة سياقياً ونُظهر كيفية بناء مثل هذه الفئات من فئات مع ألياف. في القسم 3، نُعرِّف فئات شبه الألياف النوعية النظرية ونُثبت أن الفئات السياقية المفهرسة سياقياً المقابلة لها أنواع وحدة، وأنواع Σ، وأنواع هوية. في القسم 4، نناقش أنواع التمديد. في القسم 5، نبني الجداءات المشتركة المعتمدة، والدفعات، والجداءات المشتركة الثنائية، والأنواع الأولية. في القسم 6، نُظهر أن توطينات الفئات النموذجية مغلقة تحت أنواع الهوية. في القسم 7، نناقش الفئة السياقية المفهرسة سياقياً المبنية من الفئات الشبه.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** local universes, type-theoretic semi-fibration category, right properness, extension types, stable/unstable colimits, localizations, Joyal model structure, quasicategories, Kan complex
- **Equations:** 0
- **Citations:** References to [5], [6], [7], [8], [10], [11], [12]
- **Special handling:** Technical category theory and type theory terminology

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
