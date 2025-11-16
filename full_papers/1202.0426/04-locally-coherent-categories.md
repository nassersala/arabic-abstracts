# Section 4: Locally coherent additive categories
## القسم 4: الفئات الجمعية المتماسكة موضعياً

**Section:** technical-results-applications
**Translation Quality:** 0.86
**Glossary Terms Used:** locally coherent, Grothendieck category, coherent morphism, classifying topos, Ind-completion, adjoint pair

---

### English Version (Key Content Summary)

**Section Overview:**
This section develops the connection between ABEX and COH (the 2-category of locally coherent Grothendieck categories and coherent morphisms), providing an additive analogue of concepts from topos theory including classifying toposes and points.

**Main Definitions:**
- An object A is **finitely presented** if (A,-): A→Ab commutes with direct limits
- A is **coherent** if it is finitely presented and each finitely generated subobject is finitely presented
- An abelian category G is **locally coherent** if it has a generating set of coherent objects
- A **coherent morphism** f: G→H is an adjoint pair (f*,f*) where f* is exact and preserves coherent objects
- The **Ind-completion** Ind(A) is the free extension of A to a category with direct limits

**Theorem 4.1 (Fundamental Correspondence):**
- If A is skeletally small abelian, then Lex(A^op,Ab) ≃ Flat-A ≃ Ind(A) is a locally coherent Grothendieck category G with G_fp ≃ A
- If G is locally coherent Grothendieck, then G_fp is abelian and G ≃ Lex((G_fp)^op,Ab)

**Special case:** Mod-R is locally coherent iff R is right coherent.

**Structure of Coherent Morphisms:**
A morphism f: G→H in COH consists of:
- f*: H→G (right adjoint)
- f*: G→H (left adjoint, exact, preserves coherent objects)
- Adjunction (f*,f*) with f*H_fp ⊆ G_fp

**Lemma 4.2 (2-arrows):** For adjoint pairs f = (f*,f*) and g = (g*,g*) from G to H, there is a natural bijection between natural transformations τ*: f*→g* and τ*: g*→f* that commutes with composition.

**Theorem 4.3 (Anti-Equivalence):** There is a natural anti-equivalence of 2-categories between COH and ABEX.

**Proposition 4.4 (Correspondence on Morphisms):**
- From ABEX to COH: f_0 ∈ Ex(A,B) maps to coherent morphism f = (f*,f*): Ind(B)→Ind(A) where:
  - f*: Lex(B^op,Ab)→Lex(A^op,Ab) is precomposition with f_0^op
  - f* = Ind(f_0)
- From COH to ABEX: (f*,f*): H→G maps to f*↾G_fp

**Section 4.1 - The Additive Version of the Classifying Topos:**

Develops the additive analogue of the classifying topos construction from topos theory. For a skeletally small abelian category A:
- The category Lex(A^op,Ab) plays the role of the classifying topos
- Flat-A ≃ Ind(A) is the additive version
- Connections to the Yoneda embedding and finitely presented objects

**Key Results:**
- The Yoneda embedding A→Flat-A is full and faithful
- The image consists precisely of the finitely presented objects
- Universal property: exact functors from A correspond to coherent morphisms from Flat-A

**Section 4.2 - Points of Locally Coherent Categories:**

**Definition:** A **point** of a locally coherent category G is a coherent morphism p: Ab→G (where Ab is the category of abelian groups viewed as a locally coherent Grothendieck category).

**Theorem 4.5:** Points of G = Ind(A) correspond to exact functors A→Ab, hence to objects of the definable category Ex(A,Ab).

**Main Results:**
- The set of points of G has natural structure related to the Ziegler spectrum
- Points reflect the model-theoretic structure of the definable category
- Connection between geometric (topos-theoretic) and algebraic perspectives

**Geometric vs Algebraic Viewpoints:**
The section demonstrates how locally coherent categories provide a bridge between:
- Topos theory (geometric morphisms, points, classifying toposes)
- Representation theory (module categories, exact functors)
- Model theory (definable categories, pure-injectives)

---

### النسخة العربية (ملخص المحتوى الرئيسي)

**نظرة عامة على القسم:**
يطور هذا القسم الارتباط بين ABEX و COH (الفئة الثنائية لفئات غروتنديك المتماسكة موضعياً والتشاكلات المتماسكة)، موفراً نظيراً جمعياً للمفاهيم من نظرية التوبوسات بما في ذلك التوبوسات المصنفة والنقاط.

**التعريفات الرئيسية:**
- الشيء A **مقدم بشكل منته** إذا كانت (A,-): A→Ab تتبادل مع الحدود المباشرة
- A **متماسك** إذا كان مقدماً بشكل منته وكل شيء فرعي مولد بشكل منته هو مقدم بشكل منته
- الفئة الأبيلية G **متماسكة موضعياً** إذا كان لديها مجموعة مولدة من الأشياء المتماسكة
- **التشاكل المتماسك** f: G→H هو زوج مساعد (f*,f*) حيث f* تام ويحفظ الأشياء المتماسكة
- **إكمال Ind** لـ Ind(A) هو الامتداد الحر لـ A إلى فئة ذات حدود مباشرة

**المبرهنة 4.1 (المطابقة الأساسية):**
- إذا كانت A أبيلية صغيرة هيكلياً، فإن Lex(A^op,Ab) ≃ Flat-A ≃ Ind(A) فئة غروتنديك متماسكة موضعياً G مع G_fp ≃ A
- إذا كانت G غروتنديك متماسكة موضعياً، فإن G_fp أبيلية و G ≃ Lex((G_fp)^op,Ab)

**حالة خاصة:** Mod-R متماسكة موضعياً إذا وفقط إذا كانت R متماسكة يميناً.

**بنية التشاكلات المتماسكة:**
التشاكل f: G→H في COH يتكون من:
- f*: H→G (المساعد الأيمن)
- f*: G→H (المساعد الأيسر، تام، يحفظ الأشياء المتماسكة)
- الاقتران (f*,f*) مع f*H_fp ⊆ G_fp

**اللمة 4.2 (الأسهم الثنائية):** للأزواج المساعدة f = (f*,f*) و g = (g*,g*) من G إلى H، يوجد تقابل ثنائي طبيعي بين التحويلات الطبيعية τ*: f*→g* و τ*: g*→f* يتبادل مع التركيب.

**المبرهنة 4.3 (التكافؤ العكسي):** يوجد تكافؤ عكسي طبيعي للفئات الثنائية بين COH و ABEX.

**القضية 4.4 (المطابقة على التشاكلات):**
- من ABEX إلى COH: f_0 ∈ Ex(A,B) يُصور إلى تشاكل متماسك f = (f*,f*): Ind(B)→Ind(A) حيث:
  - f*: Lex(B^op,Ab)→Lex(A^op,Ab) هو تركيب مسبق مع f_0^op
  - f* = Ind(f_0)
- من COH إلى ABEX: (f*,f*): H→G يُصور إلى f*↾G_fp

**القسم 4.1 - النسخة الجمعية من التوبوس المصنف:**

يطور النظير الجمعي لبناء التوبوس المصنف من نظرية التوبوسات. لفئة أبيلية صغيرة هيكلياً A:
- الفئة Lex(A^op,Ab) تلعب دور التوبوس المصنف
- Flat-A ≃ Ind(A) هي النسخة الجمعية
- ارتباطات بتضمين يونيدا والأشياء المقدمة بشكل منته

**النتائج الرئيسية:**
- تضمين يونيدا A→Flat-A كامل وأمين
- الصورة تتكون بالضبط من الأشياء المقدمة بشكل منته
- الخاصية الشمولية: الدوال التصنيفية التامة من A تطابق التشاكلات المتماسكة من Flat-A

**القسم 4.2 - نقاط الفئات المتماسكة موضعياً:**

**التعريف:** **النقطة** للفئة المتماسكة موضعياً G هي تشاكل متماسك p: Ab→G (حيث Ab فئة الزمر الأبيلية يُنظر إليها كفئة غروتنديك متماسكة موضعياً).

**المبرهنة 4.5:** نقاط G = Ind(A) تطابق الدوال التصنيفية التامة A→Ab، وبالتالي أشياء الفئة القابلة للتعريف Ex(A,Ab).

**النتائج الرئيسية:**
- مجموعة نقاط G لها بنية طبيعية مرتبطة بطيف زيغلر
- النقاط تعكس البنية النظرية النموذجية للفئة القابلة للتعريف
- الارتباط بين المنظورات الهندسية (نظرية التوبوسات) والجبرية

**وجهات النظر الهندسية مقابل الجبرية:**
يُظهر القسم كيف توفر الفئات المتماسكة موضعياً جسراً بين:
- نظرية التوبوسات (التشاكلات الهندسية، النقاط، التوبوسات المصنفة)
- نظرية التمثيل (فئات الوحدات، الدوال التصنيفية التامة)
- نظرية النماذج (الفئات القابلة للتعريف، الأشياء القابلة للحقن النقي)

---

### Translation Notes

- **Key Theorems Covered:** 4.1, 4.3, 4.4, 4.5
- **Subsections:** 4.1 (Classifying topos analogue), 4.2 (Points of categories)
- **Mathematical Concepts:** Locally coherent categories, Grothendieck categories, coherent morphisms, Ind-completion, classifying toposes, points, adjoint pairs
- **Connections:** Bridges topos theory, representation theory, and model theory
- **Technical Depth:** Advanced category theory with geometric and algebraic perspectives
- **Citations:** [3], [12], [17], [26], [27], [28], [30], [36], [37], [43], [45], [48]
- **Note:** Comprehensive summary of 10-page final section

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86

### Back-Translation Sample (Theorem 4.1)

If A is a structurally small abelian category, then Lex(A^op,Ab) ≃ Flat-A ≃ Ind(A) is a locally coherent Grothendieck category G with G_fp ≃ A. If G is a locally coherent Grothendieck category, then G_fp is abelian and G ≃ Lex((G_fp)^op,Ab).
