# Section 8: Applicative State Transition (AST) Systems
## القسم 8: أنظمة الانتقال الحالي التطبيقية (أنظمة AST)

**Section:** ast-systems
**Translation Quality:** 0.86
**Glossary Terms Used:** state, state transition, applicative, functional programming, history

---

### English Version

While FP and FFP systems are purely functional (no state), many practical problems require managing state. AST (Applicative State Transition) systems show how to incorporate state into functional programming without losing mathematical tractability.

## 8.1 The Need for State

Some applications inherently involve state:

1. **Interactive systems**: User interfaces, operating systems
2. **Simulation**: Systems that evolve over time
3. **Databases**: Current state of stored data
4. **I/O**: Reading and writing external data

Pure functional programs cannot model these directly because they have no notion of "current state" or "changing values." AST systems provide a solution.

## 8.2 AST System Structure

An AST system consists of:

1. **A state space S**: Set of all possible states
2. **An input set I**: Set of all possible inputs
3. **A state transition function δ: S × I → S**
4. **An output function ω: S → O**
5. **An initial state s₀ ∈ S**

The key insight: The state transition function δ is **applicative** (functional) even though it models state transitions.

## 8.3 How AST Systems Work

An AST system operates as follows:

1. Start with initial state s₀
2. Receive input i₁
3. Compute new state: s₁ = δ(s₀, i₁)
4. Produce output: o₁ = ω(s₁)
5. Receive input i₂
6. Compute new state: s₂ = δ(s₁, i₂)
7. And so on...

The sequence of states is: s₀, s₁, s₂, s₃, ...

The sequence of outputs is: ω(s₀), ω(s₁), ω(s₂), ω(s₃), ...

## 8.4 Functional State Transitions

The crucial difference from von Neumann languages:

**Von Neumann approach:**
- State is a mutable global variable
- Assignment destructively updates state
- Old state values are lost
- Difficult to reason about

**AST approach:**
- Each state is an immutable value
- Transition function computes new state from old state
- Old states can be retained (history)
- Can reason about state transitions mathematically

Example: A simple counter AST system:
```
S = integers (state is a counter value)
I = {INC, DEC, RESET} (inputs are commands)
s₀ = 0 (initial state is zero)

δ(s, INC) = s + 1
δ(s, DEC) = s - 1
δ(s, RESET) = 0

ω(s) = s (output is current counter value)
```

## 8.5 History-Sensitive Functions

Because states are values that persist, AST systems can access the entire history:

**State with history:**
```
S = sequences of previous states
Current state = <s₀, s₁, ..., sₙ>
```

**Transition function with history:**
```
δ(<s₀, ..., sₙ>, i) = <s₀, ..., sₙ, new_state>

Where new_state depends on <s₀, ..., sₙ> and i
```

**History-sensitive operations:**
- **Undo**: Return to previous state
- **Replay**: Re-execute from earlier state
- **Analysis**: Examine pattern of state changes
- **Debugging**: Inspect complete execution trace

Example: Text editor with undo:
```
S = sequences of document versions
I = {INSERT(text), DELETE(n), UNDO, ...}

δ(<d₁, ..., dₙ>, INSERT(t)) = <d₁, ..., dₙ, insert(dₙ, t)>
δ(<d₁, ..., dₙ>, UNDO) = <d₁, ..., dₙ₋₁>
```

## 8.6 AST Systems vs. Von Neumann Programs

| Aspect | Von Neumann | AST Systems |
|--------|-------------|-------------|
| State | Mutable global | Immutable values |
| History | Lost | Preserved (optional) |
| Time travel | Impossible | Natural (undo/redo) |
| Reasoning | Difficult | Mathematical |
| Composition | Problematic | Well-defined |
| Parallelism | Difficult | Easier |

## 8.7 Composing AST Systems

AST systems can be composed to build larger systems:

**Sequential composition:**
```
System A: SA × I → SA
System B: SB × SA → SB

Combined: <SA, SB> × I → <SA, SB>
Where: δ_combined(<sa, sb>, i) = <δA(sa, i), δB(sb, δA(sa, i))>
```

**Parallel composition:**
```
System A: SA × IA → SA
System B: SB × IB → SB

Combined: <SA, SB> × <IA, IB> → <SA, SB>
Where: δ_combined(<sa, sb>, <ia, ib>) = <δA(sa, ia), δB(sb, ib)>
```

This compositional structure is much cleaner than composing imperative programs with shared mutable state.

## 8.8 Example: File System AST

A simplified file system as an AST system:

```
S = sets of (filename, content) pairs
I = {READ(f), WRITE(f, data), DELETE(f), ...}

δ(s, READ(f)) = s (no state change)
δ(s, WRITE(f, data)) = s ∪ {(f, data)} (add or update file)
δ(s, DELETE(f)) = s \ {(f, _)} (remove file)

ω(s) = s (entire file system state)
```

This functional view makes it easy to reason about:
- Crash recovery (restore to previous state)
- Transactions (atomic state transitions)
- Concurrent access (compose independent transitions)
- Versioning (keep historical states)

## 8.9 Implementing AST Systems

AST systems can be implemented efficiently:

**Persistent data structures:**
- Share structure between states
- Only store differences
- O(log n) access and update

**Lazy evaluation:**
- Don't compute states until needed
- Share computation between similar states

**Garbage collection:**
- Discard old states when no longer referenced
- Retain only active states and those needed for undo

## 8.10 Advantages of AST Approach

1. **Mathematical tractability**: State transitions are functions
2. **Compositionality**: Systems compose cleanly
3. **History**: Can access previous states
4. **Debugging**: Complete execution trace
5. **Testing**: Easier to test pure functions
6. **Concurrency**: No shared mutable state
7. **Reasoning**: Can prove properties about state evolution

## 8.11 Relation to Modern Functional Programming

AST systems anticipate modern functional approaches to state:

- **Monads** in Haskell (encapsulate state transformations)
- **Redux** in React (functional state management)
- **Event sourcing** (persist state transitions, not just state)
- **Persistent data structures** (efficient immutable data)
- **Transactional memory** (atomic state updates)

The AST approach shows that state and functional programming are not incompatible - you can have both mathematical properties and practical state management.

## 8.12 Significance

AST systems demonstrate that:

1. **State can be functional**: Transitions as pure functions
2. **History is valuable**: Previous states are first-class values
3. **Composition works**: State systems compose mathematically
4. **Practical**: Can model real systems (OS, DB, UI, etc.)
5. **Complete**: Functional programming is not limited to pure computations

AST systems complete the picture: functional programming can handle the full range of computing tasks, from pure mathematics to stateful interactive systems.

---

### النسخة العربية

بينما أنظمة FP و FFP وظيفية بحتة (بدون حالة)، تتطلب العديد من المشاكل العملية إدارة الحالة. توضح أنظمة AST (الانتقال الحالي التطبيقية) كيفية دمج الحالة في البرمجة الوظيفية دون فقدان قابلية المعالجة الرياضية.

## 8.1 الحاجة إلى الحالة

بعض التطبيقات تتضمن الحالة بطبيعتها:

1. **الأنظمة التفاعلية**: واجهات المستخدم، أنظمة التشغيل
2. **المحاكاة**: أنظمة تتطور مع الوقت
3. **قواعد البيانات**: الحالة الحالية للبيانات المخزنة
4. **الإدخال/الإخراج**: قراءة وكتابة بيانات خارجية

لا يمكن للبرامج الوظيفية النقية نمذجة هذه مباشرة لأنها ليس لديها مفهوم "الحالة الحالية" أو "القيم المتغيرة." توفر أنظمة AST حلاً.

## 8.2 بنية نظام AST

يتكون نظام AST من:

1. **فضاء حالة S**: مجموعة جميع الحالات الممكنة
2. **مجموعة مدخلات I**: مجموعة جميع المدخلات الممكنة
3. **دالة انتقال حالة δ: S × I → S**
4. **دالة إخراج ω: S → O**
5. **حالة أولية s₀ ∈ S**

الرؤية الرئيسية: دالة انتقال الحالة δ **تطبيقية** (وظيفية) حتى وإن كانت تنمذج انتقالات الحالة.

## 8.3 كيف تعمل أنظمة AST

يعمل نظام AST كما يلي:

1. ابدأ بالحالة الأولية s₀
2. استقبل المدخل i₁
3. احسب الحالة الجديدة: s₁ = δ(s₀, i₁)
4. أنتج الإخراج: o₁ = ω(s₁)
5. استقبل المدخل i₂
6. احسب الحالة الجديدة: s₂ = δ(s₁, i₂)
7. وهكذا...

متتالية الحالات هي: s₀, s₁, s₂, s₃, ...

متتالية الإخراجات هي: ω(s₀), ω(s₁), ω(s₂), ω(s₃), ...

## 8.4 انتقالات الحالة الوظيفية

الفرق الحاسم من لغات فون نيومان:

**نهج فون نيومان:**
- الحالة متغير عام قابل للتغيير
- الإسناد يحدّث الحالة بشكل تدميري
- قيم الحالة القديمة تُفقد
- صعب الاستدلال حولها

**نهج AST:**
- كل حالة قيمة غير قابلة للتغيير
- دالة الانتقال تحسب حالة جديدة من حالة قديمة
- الحالات القديمة يمكن الاحتفاظ بها (التاريخ)
- يمكن الاستدلال حول انتقالات الحالة رياضياً

مثال: نظام AST عداد بسيط:
```
S = أعداد صحيحة (الحالة هي قيمة العداد)
I = {INC, DEC, RESET} (المدخلات هي أوامر)
s₀ = 0 (الحالة الأولية هي صفر)

δ(s, INC) = s + 1
δ(s, DEC) = s - 1
δ(s, RESET) = 0

ω(s) = s (الإخراج هو قيمة العداد الحالية)
```

## 8.5 الدوال الحساسة للتاريخ

لأن الحالات قيم مستمرة، يمكن لأنظمة AST الوصول إلى التاريخ الكامل:

**حالة مع التاريخ:**
```
S = متتاليات من الحالات السابقة
الحالة الحالية = <s₀, s₁, ..., sₙ>
```

**دالة انتقال مع التاريخ:**
```
δ(<s₀, ..., sₙ>, i) = <s₀, ..., sₙ, new_state>

حيث new_state يعتمد على <s₀, ..., sₙ> و i
```

**عمليات حساسة للتاريخ:**
- **التراجع**: العودة إلى حالة سابقة
- **إعادة التشغيل**: إعادة التنفيذ من حالة سابقة
- **التحليل**: فحص نمط تغيرات الحالة
- **التصحيح**: فحص أثر التنفيذ الكامل

مثال: محرر نصوص مع التراجع:
```
S = متتاليات من إصدارات المستند
I = {INSERT(text), DELETE(n), UNDO, ...}

δ(<d₁, ..., dₙ>, INSERT(t)) = <d₁, ..., dₙ, insert(dₙ, t)>
δ(<d₁, ..., dₙ>, UNDO) = <d₁, ..., dₙ₋₁>
```

## 8.6 أنظمة AST مقابل برامج فون نيومان

| الجانب | فون نيومان | أنظمة AST |
|--------|-------------|-------------|
| الحالة | عامة قابلة للتغيير | قيم غير قابلة للتغيير |
| التاريخ | مفقود | محفوظ (اختياري) |
| السفر عبر الزمن | مستحيل | طبيعي (تراجع/إعادة) |
| الاستدلال | صعب | رياضي |
| التركيب | إشكالي | محدد جيداً |
| التوازي | صعب | أسهل |

## 8.7 تركيب أنظمة AST

يمكن تركيب أنظمة AST لبناء أنظمة أكبر:

**التركيب التسلسلي:**
```
النظام A: SA × I → SA
النظام B: SB × SA → SB

المدمج: <SA, SB> × I → <SA, SB>
حيث: δ_combined(<sa, sb>, i) = <δA(sa, i), δB(sb, δA(sa, i))>
```

**التركيب الموازي:**
```
النظام A: SA × IA → SA
النظام B: SB × IB → SB

المدمج: <SA, SB> × <IA, IB> → <SA, SB>
حيث: δ_combined(<sa, sb>, <ia, ib>) = <δA(sa, ia), δB(sb, ib)>
```

هذه البنية التركيبية أنظف بكثير من تركيب برامج أمرية مع حالة مشتركة قابلة للتغيير.

## 8.8 مثال: نظام ملفات AST

نظام ملفات مبسط كنظام AST:

```
S = مجموعات من أزواج (اسم_ملف, محتوى)
I = {READ(f), WRITE(f, data), DELETE(f), ...}

δ(s, READ(f)) = s (لا تغيير في الحالة)
δ(s, WRITE(f, data)) = s ∪ {(f, data)} (إضافة أو تحديث ملف)
δ(s, DELETE(f)) = s \ {(f, _)} (إزالة ملف)

ω(s) = s (حالة نظام الملفات الكاملة)
```

هذه النظرة الوظيفية تسهل الاستدلال حول:
- استعادة الأعطال (استعادة لحالة سابقة)
- المعاملات (انتقالات حالة ذرية)
- الوصول المتزامن (تركيب انتقالات مستقلة)
- التحكم في الإصدارات (الاحتفاظ بالحالات التاريخية)

## 8.9 تنفيذ أنظمة AST

يمكن تنفيذ أنظمة AST بكفاءة:

**بنى بيانات مستمرة:**
- مشاركة البنية بين الحالات
- تخزين الاختلافات فقط
- وصول وتحديث O(log n)

**التقييم الكسول:**
- لا تحسب الحالات حتى الحاجة
- مشاركة الحساب بين حالات مشابهة

**جمع القمامة:**
- تجاهل الحالات القديمة عند عدم الإشارة إليها
- الاحتفاظ بالحالات النشطة وتلك المطلوبة للتراجع

## 8.10 مزايا نهج AST

1. **قابلية المعالجة الرياضية**: انتقالات الحالة هي دوال
2. **التركيبية**: تتركب الأنظمة بشكل نظيف
3. **التاريخ**: يمكن الوصول إلى الحالات السابقة
4. **التصحيح**: أثر تنفيذ كامل
5. **الاختبار**: أسهل لاختبار دوال نقية
6. **التزامن**: لا حالة مشتركة قابلة للتغيير
7. **الاستدلال**: يمكن إثبات خصائص حول تطور الحالة

## 8.11 العلاقة بالبرمجة الوظيفية الحديثة

تتوقع أنظمة AST النهج الوظيفية الحديثة للحالة:

- **المونادات** في Haskell (تغليف تحويلات الحالة)
- **Redux** في React (إدارة حالة وظيفية)
- **مصادر الأحداث** (الاحتفاظ بانتقالات الحالة، وليس الحالة فقط)
- **بنى البيانات المستمرة** (بيانات غير قابلة للتغيير فعالة)
- **الذاكرة المعاملاتية** (تحديثات حالة ذرية)

يوضح نهج AST أن الحالة والبرمجة الوظيفية ليسا متنافيين - يمكنك الحصول على كل من الخصائص الرياضية وإدارة الحالة العملية.

## 8.12 الأهمية

توضح أنظمة AST أن:

1. **الحالة يمكن أن تكون وظيفية**: الانتقالات كدوال نقية
2. **التاريخ قيّم**: الحالات السابقة قيم من الدرجة الأولى
3. **التركيب يعمل**: أنظمة الحالة تتركب رياضياً
4. **عملي**: يمكن نمذجة أنظمة حقيقية (OS، DB، UI، إلخ)
5. **كامل**: البرمجة الوظيفية ليست محدودة بالحسابات النقية

تكمل أنظمة AST الصورة: يمكن للبرمجة الوظيفية التعامل مع النطاق الكامل لمهام الحوسبة، من الرياضيات النقية إلى الأنظمة التفاعلية الحالية.

---

### Translation Notes

- **Key terms introduced:**
  - AST systems (أنظمة AST)
  - state space (فضاء حالة)
  - state transition function (دالة انتقال حالة)
  - applicative (تطبيقية)
  - history-sensitive (حساس للتاريخ)
  - immutable values (قيم غير قابلة للتغيير)
  - persistent data structures (بنى بيانات مستمرة)
  - event sourcing (مصادر الأحداث)

- **Mathematical notation:** State transition δ, output function ω
- **Code examples:** Counter, file system, text editor
- **Citations:** None
- **Special handling:** Comparison table, formal state transition definitions

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.85
- **Overall section score:** 0.86
