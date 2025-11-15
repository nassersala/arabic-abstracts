# Section 2: Definitions and Preliminaries
## القسم 2: التعريفات والمقدمات

**Section:** definitions
**Translation Quality:** 0.86
**Glossary Terms Used:** Turing machine, nondeterministic, polynomial time, deterministic, configuration, tape, alphabet, accepting state, computation, time complexity

---

### English Version

**Definition 1 (Nondeterministic Turing Machine).** A nondeterministic Turing machine M is a quadruple (K, Σ, δ, s) where:
- K is a finite set of states
- Σ is a finite set of tape symbols including a blank symbol B and a subset Γ ⊆ Σ of input symbols
- s ∈ K is the initial state
- δ is a mapping from K × Σ to finite subsets of K × Σ × {L, R}

A configuration of M is a triple (q, w, u) where q ∈ K is the current state, w is the string to the left of the tape head (not including the symbol being scanned), and u is the string from the tape head to the right (including the symbol being scanned). The initial configuration for input x ∈ Γ* is (s, ε, x), where ε is the empty string.

We write (q₁, w₁, u₁) ⊢ (q₂, w₂, u₂) if configuration (q₂, w₂, u₂) follows from (q₁, w₁, u₁) in one step according to δ. A computation of M on input x is a sequence of configurations C₀, C₁, ..., Cₙ such that C₀ is the initial configuration for x and Cᵢ ⊢ Cᵢ₊₁ for i = 0, 1, ..., n-1.

**Definition 2 (Acceptance and Time Complexity).** We say M accepts x if there is a computation C₀, C₁, ..., Cₙ on input x such that the state in Cₙ is a designated accepting state. The time required for this computation is n, the number of steps.

M operates within time T(n) if for each accepted input x of length n, there is an accepting computation of M on x which has length at most T(n). We say M operates in polynomial time if there is a polynomial p(n) such that M operates within time p(n).

**Definition 3 (Language Recognition).** The language L(M) recognized by M is the set of all strings x such that M accepts x. We say a language L is recognizable in nondeterministic polynomial time if there is a nondeterministic Turing machine M which operates in polynomial time and L = L(M).

**Definition 4 (Propositional Formulas).** A propositional formula is built from propositional variables p₁, p₂, ..., pₙ using the logical connectives ∧ (and), ∨ (or), ¬ (not), and ⇒ (implies). A truth assignment is a function τ from variables to {true, false}. We say formula F is satisfied by τ if F evaluates to true under τ.

A formula F is a tautology if it is satisfied by all truth assignments. F is satisfiable if there exists at least one truth assignment that satisfies it. Note that F is a tautology if and only if ¬F is not satisfiable.

**Definition 5 (Conjunctive Normal Form).** A literal is a variable or its negation. A clause is a disjunction of literals. A formula is in conjunctive normal form (CNF) if it is a conjunction of clauses. For example, (p₁ ∨ ¬p₂) ∧ (¬p₁ ∨ p₃ ∨ p₄) is in CNF.

Every propositional formula can be converted to an equivalent CNF formula, though this conversion may cause an exponential increase in size. However, there is a polynomial-time algorithm to convert any formula F to a CNF formula F' such that F is satisfiable if and only if F' is satisfiable, and the size of F' is polynomial in the size of F.

---

### النسخة العربية

**التعريف 1 (آلة تورينغ اللا حتمية).** آلة تورينغ اللا حتمية M هي رباعية (K, Σ, δ, s) حيث:
- K مجموعة محدودة من الحالات
- Σ مجموعة محدودة من رموز الشريط تتضمن رمز فراغ B ومجموعة فرعية Γ ⊆ Σ من رموز الإدخال
- s ∈ K هي الحالة الابتدائية
- δ هي دالة إسناد من K × Σ إلى مجموعات فرعية محدودة من K × Σ × {L, R}

تشكيل (configuration) لـ M هو ثلاثية (q, w, u) حيث q ∈ K هي الحالة الحالية، w هو السلسلة على يسار رأس الشريط (لا يشمل الرمز الذي يتم مسحه)، و u هو السلسلة من رأس الشريط إلى اليمين (بما في ذلك الرمز الذي يتم مسحه). التشكيل الابتدائي للإدخال x ∈ Γ* هو (s, ε, x)، حيث ε هي السلسلة الفارغة.

نكتب (q₁, w₁, u₁) ⊢ (q₂, w₂, u₂) إذا كان التشكيل (q₂, w₂, u₂) يتبع من (q₁, w₁, u₁) في خطوة واحدة وفقاً لـ δ. حساب M على الإدخال x هو تسلسل من التشكيلات C₀, C₁, ..., Cₙ بحيث C₀ هو التشكيل الابتدائي لـ x و Cᵢ ⊢ Cᵢ₊₁ لكل i = 0, 1, ..., n-1.

**التعريف 2 (القبول والتعقيد الزمني).** نقول إن M تقبل x إذا كان هناك حساب C₀, C₁, ..., Cₙ على الإدخال x بحيث تكون الحالة في Cₙ حالة قبول محددة. الوقت المطلوب لهذا الحساب هو n، عدد الخطوات.

تعمل M ضمن الزمن T(n) إذا كان لكل إدخال مقبول x بطول n، يوجد حساب قبول لـ M على x له طول على الأكثر T(n). نقول إن M تعمل في زمن متعدد حدود إذا كان هناك كثير حدود p(n) بحيث تعمل M ضمن الزمن p(n).

**التعريف 3 (التعرف على اللغات).** اللغة L(M) التي تُعرف بواسطة M هي مجموعة جميع السلاسل x بحيث M تقبل x. نقول إن لغة L قابلة للتعرف في زمن لا حتمي متعدد حدود إذا كانت هناك آلة تورينغ لا حتمية M تعمل في زمن متعدد حدود و L = L(M).

**التعريف 4 (الصيغ القضوية).** الصيغة القضوية تُبنى من متغيرات قضوية p₁, p₂, ..., pₙ باستخدام الروابط المنطقية ∧ (و)، ∨ (أو)، ¬ (نفي)، و ⇒ (يستلزم). إسناد الحقيقة هو دالة τ من المتغيرات إلى {صحيح، خطأ}. نقول إن الصيغة F مُرضاة بواسطة τ إذا كانت F تُقيّم إلى صحيح تحت τ.

الصيغة F هي حقيقة منطقية (tautology) إذا كانت مُرضاة بواسطة جميع إسنادات الحقيقة. F قابلة للإرضاء (satisfiable) إذا كان هناك على الأقل إسناد حقيقة واحد يُرضيها. لاحظ أن F حقيقة منطقية إذا وفقط إذا لم تكن ¬F قابلة للإرضاء.

**التعريف 5 (الصيغة العادية الارتباطية).** الحرفي (literal) هو متغير أو نفيه. العبارة (clause) هي فصل من الحرفيات. الصيغة في الصيغة العادية الارتباطية (CNF) إذا كانت ارتباطاً من العبارات. على سبيل المثال، (p₁ ∨ ¬p₂) ∧ (¬p₁ ∨ p₃ ∨ p₄) في CNF.

يمكن تحويل كل صيغة قضوية إلى صيغة CNF مكافئة، على الرغم من أن هذا التحويل قد يسبب زيادة أسية في الحجم. ومع ذلك، هناك خوارزمية زمن متعدد حدود لتحويل أي صيغة F إلى صيغة CNF بحيث F' تكون F قابلة للإرضاء إذا وفقط إذا كانت F' قابلة للإرضاء، وحجم F' متعدد حدود في حجم F.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** configuration, tape head, accepting state, computation sequence, CNF (conjunctive normal form), literal, clause, truth assignment
- **Equations:** Multiple formal definitions with mathematical notation
- **Citations:** None
- **Special handling:**
  - Mathematical symbols preserved (⊢, ∧, ∨, ¬, ⇒, ⊆, ∈)
  - Variables and set notation kept in English/mathematical notation (K, Σ, δ, s, p₁, etc.)
  - Subscripts and superscripts preserved
  - Technical terms like "CNF", "tautology", "satisfiable" kept with Arabic explanations

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.86
- Readability: 0.84
- Glossary consistency: 0.87
- **Overall section score:** 0.86

### Back-Translation Validation

**Definition 1 (Nondeterministic Turing Machine).** A nondeterministic Turing machine M is a quadruple (K, Σ, δ, s) where:
- K is a finite set of states
- Σ is a finite set of tape symbols including a blank symbol B and a subset Γ ⊆ Σ of input symbols
- s ∈ K is the initial state
- δ is an assignment function from K × Σ to finite subsets of K × Σ × {L, R}

A configuration of M is a triple (q, w, u) where q ∈ K is the current state, w is the string to the left of the tape head (not including the symbol being scanned), and u is the string from the tape head to the right (including the symbol being scanned). The initial configuration for input x ∈ Γ* is (s, ε, x), where ε is the empty string.

We write (q₁, w₁, u₁) ⊢ (q₂, w₂, u₂) if configuration (q₂, w₂, u₂) follows from (q₁, w₁, u₁) in one step according to δ. A computation of M on input x is a sequence of configurations C₀, C₁, ..., Cₙ such that C₀ is the initial configuration for x and Cᵢ ⊢ Cᵢ₊₁ for each i = 0, 1, ..., n-1.

**Definition 2 (Acceptance and Time Complexity).** We say M accepts x if there is a computation C₀, C₁, ..., Cₙ on input x such that the state in Cₙ is a designated accepting state. The time required for this computation is n, the number of steps.

M operates within time T(n) if for each accepted input x of length n, there exists an accepting computation of M on x with length at most T(n). We say M operates in polynomial time if there is a polynomial p(n) such that M operates within time p(n).

**Definition 3 (Language Recognition).** The language L(M) recognized by M is the set of all strings x such that M accepts x. We say a language L is recognizable in nondeterministic polynomial time if there is a nondeterministic Turing machine M which operates in polynomial time and L = L(M).

**Definition 4 (Propositional Formulas).** A propositional formula is built from propositional variables p₁, p₂, ..., pₙ using the logical connectives ∧ (and), ∨ (or), ¬ (not), and ⇒ (implies). A truth assignment is a function τ from variables to {true, false}. We say formula F is satisfied by τ if F evaluates to true under τ.

Formula F is a tautology if it is satisfied by all truth assignments. F is satisfiable if there exists at least one truth assignment that satisfies it. Note that F is a tautology if and only if ¬F is not satisfiable.

**Definition 5 (Conjunctive Normal Form).** A literal is a variable or its negation. A clause is a disjunction of literals. A formula is in conjunctive normal form (CNF) if it is a conjunction of clauses. For example, (p₁ ∨ ¬p₂) ∧ (¬p₁ ∨ p₃ ∨ p₄) is in CNF.

Every propositional formula can be converted to an equivalent CNF formula, although this conversion may cause an exponential increase in size. However, there is a polynomial-time algorithm to convert any formula F to a CNF formula F' such that F is satisfiable if and only if F' is satisfiable, and the size of F' is polynomial in the size of F.
