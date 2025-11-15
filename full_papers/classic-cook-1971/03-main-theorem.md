# Section 3: Main Theorem and Proof
## القسم 3: النظرية الرئيسية والبرهان

**Section:** main-theorem
**Translation Quality:** 0.88
**Glossary Terms Used:** polynomial time, nondeterministic, Turing machine, tautology, satisfiability, reduction, CNF, computational complexity, proof

---

### English Version

**Theorem 1 (Cook's Theorem).** Let L be a language recognized by some nondeterministic Turing machine M in polynomial time. Then there exists a polynomial time-computable function f such that for each string x:
- x ∈ L if and only if f(x) is a satisfiable propositional formula in CNF

Furthermore, the size of f(x) is bounded by a polynomial in the size of x.

**Proof Sketch.** Given a nondeterministic Turing machine M that operates in time p(n) for some polynomial p, and an input x of length n, we construct a formula F that is satisfiable if and only if M accepts x.

The key idea is to use propositional variables to encode the computation of M on x. We introduce variables:
- Qᵢ,ₜ: true if M is in state qᵢ at time t
- Tⱼ,ₜ,ₛ: true if tape cell j contains symbol s at time t
- Hⱼ,ₜ: true if the tape head is at position j at time t

The time runs from 0 to p(n), and the tape positions run from 0 to p(n) (since M can visit at most p(n) cells in p(n) steps). The total number of variables is O(p(n)²).

The formula F is a conjunction of clauses expressing:

1. **Initial configuration**: At time 0, M is in the initial state s, the tape head is at position 0, and the tape contains the input x:
   $$F_{init} = Q_{s,0} \wedge H_{0,0} \wedge \bigwedge_{j=0}^{n-1} T_{j,0,x_j} \wedge \bigwedge_{j=n}^{p(n)} T_{j,0,B}$$

2. **Uniqueness**: At each time t, exactly one state is active, exactly one tape position contains the head, and each cell contains exactly one symbol. These constraints can be expressed as CNF clauses of size O(p(n)²).

3. **Transition validity**: For each time t < p(n) and each position j, if the machine is in state qᵢ, the head is at position j, and cell j contains symbol s, then the next configuration must be consistent with one of the transitions in δ(qᵢ, s). This gives clauses of the form:
   $$(Q_{i,t} \wedge H_{j,t} \wedge T_{j,t,s}) \Rightarrow \bigvee_{(q',s',d) \in \delta(q_i,s)} (Q_{q',t+1} \wedge T_{j,t+1,s'} \wedge H_{j+d,t+1})$$
   where d ∈ {-1, +1} represents left or right movement.

4. **Non-head cells unchanged**: If the head is not at position j at time t, then cell j has the same symbol at time t+1:
   $$\neg H_{j,t} \Rightarrow (T_{j,t,s} \Leftrightarrow T_{j,t+1,s})$$

5. **Acceptance**: At some time t ≤ p(n), the machine is in an accepting state:
   $$F_{accept} = \bigvee_{t=0}^{p(n)} \bigvee_{q \in Q_{accept}} Q_{q,t}$$

The complete formula is:
$$F = F_{init} \wedge F_{unique} \wedge F_{trans} \wedge F_{preserve} \wedge F_{accept}$$

Each of these components can be expressed in CNF with at most O(p(n)²) clauses, each of constant size (after introducing auxiliary variables if necessary). Therefore, the total size of F is polynomial in n.

**Correctness:** If M accepts x, then there is an accepting computation, and we can set the variables according to this computation to satisfy F. Conversely, if F is satisfiable, then any satisfying assignment corresponds to a valid accepting computation of M on x.

**Corollary 1.** The satisfiability problem for CNF formulas (SAT) is NP-complete. That is:
1. SAT is in NP (can be solved by a nondeterministic polynomial-time Turing machine)
2. Every language in NP can be reduced to SAT in polynomial time

**Proof.** (1) is obvious: guess a truth assignment and verify it satisfies the formula in polynomial time. (2) follows from Theorem 1.

**Corollary 2.** The tautology problem (determining if a formula is true under all truth assignments) is co-NP-complete.

**Proof.** A formula F is a tautology if and only if ¬F is not satisfiable. The reduction follows by negation.

---

### النسخة العربية

**النظرية 1 (نظرية كوك).** لتكن L لغة يتم التعرف عليها بواسطة بعض آلات تورينغ اللا حتمية M في زمن متعدد حدود. إذن توجد دالة f قابلة للحوسبة في زمن متعدد حدود بحيث لكل سلسلة x:
- x ∈ L إذا وفقط إذا كانت f(x) صيغة قضوية قابلة للإرضاء في CNF

علاوة على ذلك، حجم f(x) محدود بكثير حدود في حجم x.

**ملخص البرهان.** بالنظر إلى آلة تورينغ لا حتمية M تعمل في الزمن p(n) لبعض كثيرات الحدود p، وإدخال x بطول n، نُنشئ صيغة F قابلة للإرضاء إذا وفقط إذا كانت M تقبل x.

الفكرة الأساسية هي استخدام متغيرات قضوية لتشفير حساب M على x. نُقدم المتغيرات:
- Qᵢ,ₜ: صحيح إذا كانت M في الحالة qᵢ عند الزمن t
- Tⱼ,ₜ,ₛ: صحيح إذا كانت خلية الشريط j تحتوي على الرمز s عند الزمن t
- Hⱼ,ₜ: صحيح إذا كان رأس الشريط في الموضع j عند الزمن t

يمتد الزمن من 0 إلى p(n)، وتمتد مواضع الشريط من 0 إلى p(n) (نظراً لأن M يمكن أن تزور على الأكثر p(n) خلية في p(n) خطوة). العدد الإجمالي للمتغيرات هو O(p(n)²).

الصيغة F هي ارتباط من العبارات التي تعبر عن:

1. **التشكيل الابتدائي**: عند الزمن 0، M في الحالة الابتدائية s، رأس الشريط في الموضع 0، والشريط يحتوي على الإدخال x:
   $$F_{init} = Q_{s,0} \wedge H_{0,0} \wedge \bigwedge_{j=0}^{n-1} T_{j,0,x_j} \wedge \bigwedge_{j=n}^{p(n)} T_{j,0,B}$$

2. **التفرد**: عند كل زمن t، حالة واحدة بالضبط نشطة، موضع شريط واحد بالضبط يحتوي على الرأس، وكل خلية تحتوي على رمز واحد بالضبط. يمكن التعبير عن هذه القيود كعبارات CNF بحجم O(p(n)²).

3. **صحة الانتقال**: لكل زمن t < p(n) وكل موضع j، إذا كانت الآلة في الحالة qᵢ، والرأس في الموضع j، والخلية j تحتوي على الرمز s، فيجب أن يكون التشكيل التالي متسقاً مع أحد الانتقالات في δ(qᵢ, s). هذا يعطي عبارات من الشكل:
   $$(Q_{i,t} \wedge H_{j,t} \wedge T_{j,t,s}) \Rightarrow \bigvee_{(q',s',d) \in \delta(q_i,s)} (Q_{q',t+1} \wedge T_{j,t+1,s'} \wedge H_{j+d,t+1})$$
   حيث d ∈ {-1, +1} يمثل الحركة لليسار أو اليمين.

4. **الخلايا غير الرأسية دون تغيير**: إذا لم يكن الرأس في الموضع j عند الزمن t، فإن الخلية j لها نفس الرمز عند الزمن t+1:
   $$\neg H_{j,t} \Rightarrow (T_{j,t,s} \Leftrightarrow T_{j,t+1,s})$$

5. **القبول**: عند بعض الزمن t ≤ p(n)، الآلة في حالة قبول:
   $$F_{accept} = \bigvee_{t=0}^{p(n)} \bigvee_{q \in Q_{accept}} Q_{q,t}$$

الصيغة الكاملة هي:
$$F = F_{init} \wedge F_{unique} \wedge F_{trans} \wedge F_{preserve} \wedge F_{accept}$$

يمكن التعبير عن كل من هذه المكونات في CNF مع على الأكثر O(p(n)²) عبارة، كل منها بحجم ثابت (بعد إدخال متغيرات مساعدة إذا لزم الأمر). لذلك، الحجم الإجمالي لـ F متعدد حدود في n.

**الصحة:** إذا كانت M تقبل x، فهناك حساب قبول، ويمكننا تعيين المتغيرات وفقاً لهذا الحساب لإرضاء F. وبالعكس، إذا كانت F قابلة للإرضاء، فإن أي إسناد مُرضٍ يتوافق مع حساب قبول صحيح لـ M على x.

**النتيجة 1.** مسألة الإرضاء لصيغ CNF (SAT) مكتملة بالنسبة لـ NP. أي:
1. SAT في NP (يمكن حلها بواسطة آلة تورينغ لا حتمية في زمن متعدد حدود)
2. كل لغة في NP يمكن اختزالها إلى SAT في زمن متعدد حدود

**البرهان.** (1) واضح: خمّن إسناد حقيقة وتحقق من أنه يُرضي الصيغة في زمن متعدد حدود. (2) يتبع من النظرية 1.

**النتيجة 2.** مسألة الحقيقة المنطقية (تحديد ما إذا كانت الصيغة صحيحة تحت جميع إسنادات الحقيقة) مكتملة بالنسبة لـ co-NP.

**البرهان.** الصيغة F حقيقة منطقية إذا وفقط إذا لم تكن ¬F قابلة للإرضاء. الاختزال يتبع بالنفي.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** encoding, CNF clauses, configuration encoding, NP-complete, co-NP-complete, polynomial reduction
- **Equations:** 6 major formulas with logical connectives
- **Citations:** None
- **Special handling:**
  - Complex mathematical formulas preserved with all symbols
  - Subscripts and logical operators maintained
  - Proof structure carefully translated
  - Big-O notation preserved
  - Corollaries translated with full mathematical rigor

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.89
- **Overall section score:** 0.88

### Back-Translation Validation

**Theorem 1 (Cook's Theorem).** Let L be a language recognized by some nondeterministic Turing machine M in polynomial time. Then there exists a function f computable in polynomial time such that for each string x:
- x ∈ L if and only if f(x) is a satisfiable propositional formula in CNF

Furthermore, the size of f(x) is bounded by a polynomial in the size of x.

**Proof Summary.** Given a nondeterministic Turing machine M operating in time p(n) for some polynomial p, and an input x of length n, we construct a formula F that is satisfiable if and only if M accepts x.

The basic idea is to use propositional variables to encode the computation of M on x. We introduce variables:
- Qᵢ,ₜ: true if M is in state qᵢ at time t
- Tⱼ,ₜ,ₛ: true if tape cell j contains symbol s at time t
- Hⱼ,ₜ: true if the tape head is at position j at time t

Time extends from 0 to p(n), and tape positions extend from 0 to p(n) (since M can visit at most p(n) cells in p(n) steps). The total number of variables is O(p(n)²).

Formula F is a conjunction of clauses expressing:

1. **Initial configuration**: At time 0, M is in initial state s, the tape head is at position 0, and the tape contains input x
2. **Uniqueness**: At each time t, exactly one state is active, exactly one tape position contains the head, and each cell contains exactly one symbol
3. **Transition validity**: For each time t < p(n) and each position j, if the machine is in state qᵢ, the head is at position j, and cell j contains symbol s, then the next configuration must be consistent with one of the transitions in δ(qᵢ, s)
4. **Non-head cells unchanged**: If the head is not at position j at time t, then cell j has the same symbol at time t+1
5. **Acceptance**: At some time t ≤ p(n), the machine is in an accepting state

Each of these components can be expressed in CNF with at most O(p(n)²) clauses, each of constant size (after introducing auxiliary variables if necessary). Therefore, the total size of F is polynomial in n.

**Correctness:** If M accepts x, there is an accepting computation, and we can assign variables according to this computation to satisfy F. Conversely, if F is satisfiable, any satisfying assignment corresponds to a valid accepting computation of M on x.

**Corollary 1.** The satisfiability problem for CNF formulas (SAT) is NP-complete. That is:
1. SAT is in NP (can be solved by a nondeterministic polynomial-time Turing machine)
2. Every language in NP can be reduced to SAT in polynomial time

**Proof.** (1) is obvious: guess a truth assignment and verify it satisfies the formula in polynomial time. (2) follows from Theorem 1.

**Corollary 2.** The tautology problem (determining if a formula is true under all truth assignments) is co-NP-complete.

**Proof.** Formula F is a tautology if and only if ¬F is not satisfiable. The reduction follows by negation.
