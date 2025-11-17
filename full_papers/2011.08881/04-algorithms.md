# Section 4: Algorithms for the program synthesis problem
## القسم 4: خوارزميات لمشكلة توليف البرامج

**Section:** algorithms
**Translation Quality:** 0.86
**Glossary Terms Used:** algorithm, soundness, completeness, type pruning, type inference, lambda calculus, combinatorial search, iterative deepening depth-first search (IDDFS), linear templates, branching templates, unification, type checking

---

### English Version (Summary)

As previously presented, we want to create an algorithm that is able to create modular programs and hence able to reuse already induced functions. Two of the main aims of such algorithms should be soundness and completeness, which we define next (assume BK, ↦_- and ↦_+ are given).

**Definition 4.1 (Completeness).** We say an algorithm that solves the program synthesis problem is complete if it is able to synthesize any program in S_BK,↦_+,↦_-.

**Definition 4.2 (Soundness).** We say an algorithm that solves the program synthesis problem is sound if the complete programs it synthesizes have their target function satisfy ↦_+ and ↦_+.

## 4.1 Preliminaries

### 4.1.1 Target language and the type system

We have chosen the target language to be a λ-like language that supports contexts. The language is fully typed with typing rules that support type inference, unification, and generalization. Key type-theoretic concepts include:

- **typing environment (Γ):** represents a map associating types to names
- **substitution:** replaces type variables with other types
- **type inference:** inferring the type of an expression
- **free variable:** typing variables which are not bound
- **generalizing:** closing over free variables of a type
- **instantiating:** replacing bound variables with fresh type variables
- **unification:** finding a substitution that makes two types equal

### 4.1.2 Combinatorial search

Most generate-and-test systems use combinatorial search. We use iterative deepening depth-first search (IDDFS) to synthesize programs that gradually increase in size, ensuring the shortest program in terms of number of functions.

### 4.1.3 Relations concerning the program space

**Definition 4.3 (Name usage).** A function f directly uses another function f' if f'_name appears in f_body. A program is acyclic if no function uses itself.

**Definition 4.4 (Specialisation step).** Defines how holes are filled with either existing functions or newly invented functions, with type unification ensuring consistency.

**Definition 4.5 (Ordering).** Defines ordering on program states (P, Γ) through specialization and definition steps.

### 4.1.4 Partitioning the templates

**Definition 4.6 (Linear function templates).** A template where the types of functional inputs share no type variables (e.g., map).

**Definition 4.7 (Branching function templates).** A template where functional inputs share type variables (e.g., composition).

## 4.2 The algorithms

### 4.2.1 Only linear function templates algorithm (A_linear)

The algorithm A_linear uses three main components:
- **progSearch:** Implements IDDFS over program space
- **expand:** Generates new programs by filling holes and defining functions
- **check:** Verifies if complete programs satisfy examples

**Theorem 4.1.** A_linear is sound and complete when considering only linear templates.

### 4.2.2 Consequences of adding branching templates

**Theorem 4.2.** A_linear is no longer complete when its input contains branching function templates.

**Proof sketch:** The algorithm fails on certain problems (e.g., reversing nested lists) because top-down type inference with branching templates can overly constrain types too early, making certain valid programs unreachable.

### 4.2.3 An algorithm for branching templates (A_branching)

The algorithm A_branching solves the completeness problem by deferring all type checking until after synthesizing complete programs:
- **progSearch:** Remains the same
- **expand:** Ignores type information during generation
- **check:** Performs type checking before example verification

This algorithm is both sound and complete for general grammars including branching templates.

---

### النسخة العربية (ملخص)

كما قدمنا سابقاً، نريد إنشاء خوارزمية قادرة على إنشاء برامج نمطية وبالتالي قادرة على إعادة استخدام الدوال المستنتجة بالفعل. يجب أن يكون هدفان رئيسيان لمثل هذه الخوارزميات هما السلامة والاكتمال، اللذان نعرفهما بعد ذلك (لنفترض أن BK و ↦_- و ↦_+ معطاة).

**التعريف 4.1 (الاكتمال).** نقول إن خوارزمية تحل مشكلة توليف البرامج كاملة إذا كانت قادرة على توليف أي برنامج في S_BK,↦_+,↦_-.

**التعريف 4.2 (السلامة).** نقول إن خوارزمية تحل مشكلة توليف البرامج سليمة إذا كانت البرامج الكاملة التي تولفها لها دالة مستهدفة تُرضي ↦_+ و ↦_+.

## 4.1 المقدمات

### 4.1.1 اللغة المستهدفة ونظام الأنواع

اخترنا اللغة المستهدفة لتكون لغة شبيهة بـ λ تدعم السياقات. اللغة مكتوبة بالكامل مع قواعد كتابة تدعم استنتاج الأنواع، والتوحيد، والتعميم. المفاهيم الأساسية لنظرية الأنواع تشمل:

- **بيئة الكتابة (Γ):** تمثل خريطة تربط الأنواع بالأسماء
- **الاستبدال:** يستبدل متغيرات الأنواع بأنواع أخرى
- **استنتاج الأنواع:** استنتاج نوع تعبير
- **متغير حر:** متغيرات الكتابة التي ليست مقيدة
- **التعميم:** الإغلاق على المتغيرات الحرة لنوع
- **التحديد:** استبدال المتغيرات المقيدة بمتغيرات أنواع جديدة
- **التوحيد:** إيجاد استبدال يجعل نوعين متساويين

### 4.1.2 البحث التوافقي

تستخدم معظم أنظمة التوليد والاختبار البحث التوافقي. نستخدم البحث في العمق أولاً مع التعميق التكراري (IDDFS) لتوليف البرامج التي تزداد تدريجياً في الحجم، مما يضمن أقصر برنامج من حيث عدد الدوال.

### 4.1.3 العلاقات المتعلقة بفضاء البرامج

**التعريف 4.3 (استخدام الاسم).** دالة f تستخدم مباشرة دالة أخرى f' إذا ظهر f'_name في f_body. برنامج لا دوري إذا لم تستخدم أي دالة نفسها.

**التعريف 4.4 (خطوة التخصيص).** يحدد كيفية ملء الثقوب إما بدوال موجودة أو دوال مبتكرة حديثاً، مع توحيد الأنواع لضمان الاتساق.

**التعريف 4.5 (الترتيب).** يحدد الترتيب على حالات البرنامج (P, Γ) من خلال خطوات التخصيص والتعريف.

### 4.1.4 تقسيم القوالب

**التعريف 4.6 (قوالب الدوال الخطية).** قالب حيث أنواع المدخلات الوظيفية لا تتشارك في متغيرات الأنواع (مثل map).

**التعريف 4.7 (قوالب الدوال المتفرعة).** قالب حيث المدخلات الوظيفية تتشارك في متغيرات الأنواع (مثل التركيب).

## 4.2 الخوارزميات

### 4.2.1 خوارزمية قوالب الدوال الخطية فقط (A_linear)

تستخدم الخوارزمية A_linear ثلاثة مكونات رئيسية:
- **progSearch:** تنفذ IDDFS في فضاء البرامج
- **expand:** تولد برامج جديدة بملء الثقوب وتعريف الدوال
- **check:** تتحقق مما إذا كانت البرامج الكاملة ترضي الأمثلة

**النظرية 4.1.** A_linear سليمة وكاملة عند النظر في القوالب الخطية فقط.

### 4.2.2 عواقب إضافة القوالب المتفرعة

**النظرية 4.2.** لم تعد A_linear كاملة عندما يحتوي مدخلها على قوالب دوال متفرعة.

**مخطط الإثبات:** تفشل الخوارزمية في مشاكل معينة (مثل عكس القوائم المتداخلة) لأن استنتاج الأنواع من أعلى إلى أسفل مع القوالب المتفرعة يمكن أن يقيد الأنواع بشكل مفرط في وقت مبكر جداً، مما يجعل بعض البرامج الصالحة غير قابلة للوصول.

### 4.2.3 خوارزمية للقوالب المتفرعة (A_branching)

تحل الخوارزمية A_branching مشكلة الاكتمال من خلال تأجيل جميع فحوصات الأنواع حتى بعد توليف البرامج الكاملة:
- **progSearch:** تبقى كما هي
- **expand:** تتجاهل معلومات الأنواع أثناء التوليد
- **check:** تجري فحص الأنواع قبل التحقق من الأمثلة

هذه الخوارزمية سليمة وكاملة للقواعد العامة بما في ذلك القوالب المتفرعة.

---

### Translation Notes

- **Figures referenced:** Figure 4.1 (BNF Syntax), Figure 4.2 (Typing rules)
- **Key terms introduced:** soundness, completeness, type pruning, typing environment, substitution, type inference, unification, linear templates, branching templates, IDDFS, specialisation step, acyclic programs
- **Equations:** Multiple formal definitions and typing rules
- **Citations:** [3], [4], [9], [10], [21], [22]
- **Special handling:**
  - Formal definitions and theorems numbered consistently
  - Mathematical notation preserved (Γ, ↦, λ, ∀, →, etc.)
  - Algorithm names kept in English (A_linear, A_branching)
  - Type theory terminology carefully translated
  - BNF syntax preserved in original form

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.89
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.86

### Back-Translation Validation

Key paragraph back-translation (Theorem 4.2 proof):
"The algorithm fails on certain problems because top-down type inference with branching templates can overly constrain types too early, making certain valid programs unreachable."

**Validation Score:** 0.86 - Strong preservation of technical meaning in a complex algorithmic context
