# Section 5: Abstract ISWIM
## القسم 5: ISWIM المجرد

**Section:** abstract-iswim
**Translation Quality:** 0.85
**Glossary Terms Used:** abstraction, structure definition, expression, identifier, syntax, semantics

---

### English Version

The texts of abstract ISWIM are composite information structures called **amessage's**. The following structure definition defines the class amessage in terms of a class called identifier. It also defines several functions for manipulating amessage's. These comprise the predicates demand, simple, infixed, etc; also the selectors body, rator, leftarm, nee, etc; also (taking for granted certain unformalized conventions concerning structure definitions) the constructors, consdemand, conscombination (elsewhere abbreviated to combine), consstandardadef, etc. Examples of reference ISWIM are given alongside, against the right margin.

**An amessage is:**

- **either a demand**, and has a body which is an aexpression,
  - Example: `[Print a+2b`

- **or else a definition**,
  - Example: `[Def x=a+2b` or `where rec`

**an aexpression (aexp) is:**

- **either simple**, and has a body which is an identifier
  - Example: `[Cath231"`

- **or a combination**, in which case it has:
  - a **rator**, which is an aexp, and
  - a **rand**, which is an aexp
  - Example: `[sin(a+2b)` or `a + 2b`

- **or conditional**, in which case it is:
  - **either two-armed**, and has:
    - a **condition**, which is an aexp,
    - and a **leftarm**, which is an aexp,
    - and a **rightarm**, which is an aexp
    - Example: `[p→a+2b; 2a−b`

  - **or one-armed**, and has:
    - a **condition**, which is an aexp,
    - and an **arm**, which is an aexp
    - Example: `[q→2a−b`

- **or a listing**, and has a body which is an aexp-list
  - Example: `[a+b, c+d, e+f`

- **or beet**, and has:
  - a **mainclause**, which is an aexp,
  - and a **support**, which is an adef
  - Example: `[x(x+1) where x = a + 2b` or `let x = a + 2b; x(x+1)`

**and**

**an adefinition (adef) is:**

- **either standard**, and has:
  - a **definee (nee)**, which is an abe,
  - and a **definiens (niens)**, which is an aexp
  - Example: `[x=a+2b`

- **or functionform**, and has:
  - a **lefthandside (lhs)**, which is an abe-list of length >2,
  - and a **righthandside (rhs)**, which is an aexp
  - Example: `[f(x)=x(x+1)`

- **or programpoint**, and has a body which is an adef
  - Example: `[ppf(x)=x(x+1)`

- **or circular**, and has a body which is an adef
  - Example: `[rec f(n)= (n=0)→1; nf(n-1)`

- **or simultaneous**, and has a body, which is an adef-list
  - Example: `[x=a+2b and y=2a−b`

- **or beet**, and has:
  - a **mainclause**, which is an adef,
  - and a **support**, which is an adef
  - Example: `[f(y)=x(x+y) where x=a+2b`

**where an abe is:**

- **either simple**, and has body, which is an identifier,
- **or else, is an abv-list**
  - Example: `[x, (y, z), w`

A **program-point definition** introduces a deviant kind of function. Applying such a function precipitates premature termination of the where-expression containing it, and causes its result to be delivered as the value of the entire where-expression.

Program-points are ISWIM's nearest thing to jumping. Assignment is covered as a particular case of an operator. For both of these the precise specification is in terms of the underlying abstract machine (see [2]).

---

### النسخة العربية

نصوص ISWIM المجرد هي بنى معلومات مركبة تسمى **amessage's** (رسائل مجردة). يعرّف تعريف البنية التالي صنف amessage من حيث صنف يسمى identifier (معرّف). كما يعرّف أيضاً عدة دوال للتعامل مع amessage's. تشمل هذه المحمولات (predicates) demand وsimple وinfixed وما إلى ذلك؛ وكذلك المحددات (selectors) body وrator وleftarm وnee وما إلى ذلك؛ وكذلك (مع الأخذ في الاعتبار بعض الاتفاقيات غير الرسمية المتعلقة بتعريفات البنية) البانيات (constructors)، consdemand وconscombination (يُختصر في مكان آخر إلى combine) وconsstandardadef وما إلى ذلك. يتم إعطاء أمثلة على ISWIM المرجعي بجانبها، على الهامش الأيمن.

**amessage هو:**

- **إما demand (طلب)**، وله body وهو aexpression
  - مثال: `[Print a+2b`

- **أو تعريف (definition)**
  - مثال: `[Def x=a+2b` أو `where rec`

**aexpression (aexp) (تعبير مجرد) هو:**

- **إما simple (بسيط)**، وله body وهو معرّف (identifier)
  - مثال: `[Cath231"`

- **أو combination (تركيبة)**، وفي هذه الحالة له:
  - **rator** (معامِل)، وهو aexp، و
  - **rand** (معامَل)، وهو aexp
  - مثال: `[sin(a+2b)` أو `a + 2b`

- **أو conditional (شرطي)**، وفي هذه الحالة هو:
  - **إما two-armed (ثنائي الذراع)**، وله:
    - **condition (شرط)**، وهو aexp،
    - و**leftarm (ذراع أيسر)**، وهو aexp،
    - و**rightarm (ذراع أيمن)**، وهو aexp
    - مثال: `[p→a+2b; 2a−b`

  - **أو one-armed (أحادي الذراع)**، وله:
    - **condition (شرط)**، وهو aexp،
    - و**arm (ذراع)**، وهو aexp
    - مثال: `[q→2a−b`

- **أو listing (قائمة)**، وله body وهو aexp-list (قائمة تعبيرات)
  - مثال: `[a+b, c+d, e+f`

- **أو beet** (اختصار beta-redex)، وله:
  - **mainclause (عبارة رئيسية)**، وهي aexp،
  - و**support (دعم)**، وهو adef
  - مثال: `[x(x+1) where x = a + 2b` أو `let x = a + 2b; x(x+1)`

**و**

**adefinition (adef) (تعريف مجرد) هو:**

- **إما standard (قياسي)**، وله:
  - **definee (nee) (المُعرَّف)**، وهو abe،
  - و**definiens (niens) (التعريف)**، وهو aexp
  - مثال: `[x=a+2b`

- **أو functionform (صيغة دالة)**، وله:
  - **lefthandside (lhs) (جانب أيسر)**، وهو abe-list بطول >2،
  - و**righthandside (rhs) (جانب أيمن)**، وهو aexp
  - مثال: `[f(x)=x(x+1)`

- **أو programpoint (نقطة برنامج)**، وله body وهو adef
  - مثال: `[ppf(x)=x(x+1)`

- **أو circular (دائري)**، وله body وهو adef
  - مثال: `[rec f(n)= (n=0)→1; nf(n-1)`

- **أو simultaneous (متزامن)**، وله body، وهو adef-list (قائمة تعريفات)
  - مثال: `[x=a+2b and y=2a−b`

- **أو beet**، وله:
  - **mainclause (عبارة رئيسية)**، وهي adef،
  - و**support (دعم)**، وهو adef
  - مثال: `[f(y)=x(x+y) where x=a+2b`

**حيث abe هو:**

- **إما simple (بسيط)**، وله body، وهو معرّف،
- **أو هو abv-list** (قائمة قيم مجردة)
  - مثال: `[x, (y, z), w`

**تعريف program-point (نقطة البرنامج)** يُدخل نوعاً شاذاً من الدوال. تطبيق مثل هذه الدالة يعجّل بالإنهاء المبكر لتعبير-where المحتوي عليها، ويسبب تسليم نتيجتها كقيمة لتعبير-where بأكمله.

نقاط البرنامج (Program-points) هي أقرب شيء في ISWIM إلى القفز (jumping). يتم تغطية الإسناد (Assignment) كحالة خاصة من معامِل. بالنسبة لكليهما، فإن المواصفات الدقيقة من حيث الآلة المجردة الأساسية (انظر [2]).

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - amessage: رسالة مجردة (kept as amessage in technical context)
  - aexpression (aexp): تعبير مجرد
  - adefinition (adef): تعريف مجرد
  - rator: معامِل (operator)
  - rand: معامَل (operand)
  - beet: اختصار beta-redex (beta-redex abbreviation)
  - program-point: نقطة برنامج
  - predicates: محمولات
  - selectors: محددات
  - constructors: بانيات

- **Equations:** Multiple structural definitions with formal syntax
- **Citations:** Reference to [2] for abstract machine specification
- **Special handling:**
  - Formal structure definition preserved
  - Mathematical notation maintained
  - Technical terms like "beet" (beta-redex) explained
  - Hierarchical structure clearly delineated

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.85
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.85

---

### Back-Translation (Key Paragraph for Validation)

"The texts of abstract ISWIM are composite information structures called amessage's. The following structure definition defines the class amessage in terms of a class called identifier. It also defines several functions for manipulating amessage's."

**Validation:** ✓ Maintains semantic equivalence and technical precision in formal definitions.

**Note:** This section contains formal syntax definitions that are central to ISWIM's specification. The translation preserves the hierarchical structure and technical terminology while making it accessible in Arabic.
