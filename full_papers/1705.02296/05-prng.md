# Section 5: Pseudo Random Number Generator
## القسم 5: مولد الأرقام شبه العشوائية

**Section:** technical foundation for random number generation
**Translation Quality:** 0.86
**Glossary Terms Used:** PRNG (مولد أرقام شبه عشوائية), internal state (حالة داخلية), random seed (بذرة عشوائية), polynomial function (دالة متعددة الحدود), adversary (خصم), projection (إسقاط), axiom (بديهية), soundness (صحة)

---

### English Version

**Section V: PSEUDO RANDOM NUMBER GENERATOR**

A PRNG uses an internal state, which is updated at each call, and outputs a pseudo random number. This can be modeled by a function G taking the internal state as input, and outputting a pair with the new internal state and the generated pseudo random number (retrieved using the projections πS and πo). Besides, a function initS is used to initialized the internal state with a random seed (which can be hard-coded in the tag).

**Definition 5 (PRNG):** A PRNG is a tuple of polynomial functions (G, initS) such that for every PPT adversary A and for every n, the following quantity is negligible in η:

|Pr (r ∈ {0, 1}^η : A(πo(s0), ..., πo(sn)) = 1) −
 Pr (r0, ..., rn ∈ {0, 1}^η : A(r0, ..., rn) = 1)|

where s0 = G(initS(r, 1^η)) and for all 0 ≤ i < n, si+1 = G(πS(si)).

This can be translated in the logic by the PRNGn axioms:

πo(s0), ..., πo(sn) ∼ n0, ..., nn

where s0 ≡ G(initS(n)) and ∀0 ≤ i < n, si+1 ≡ G(πS(si)).

**Proposition 5:** The (PRNGn)n axioms are sound in any computational model Mc where (G, initS) is interpreted as a PRNG.

The soundness is an immediate consequence of Definition 5.

For each protocol where a strict separation exists between the cryptographic material used for random number generation and the other primitives (e.g. encryption keys), pseudo random numbers generated using a PRNG can be abstracted as random numbers using the following proposition:

**Proposition 6:** For every names n,(ni)i≤n and contexts u0, ..., un that do not contain these names, the following formula is derivable using the axioms in Figure 1 and PRNGn:

u0[πo(s0)], ..., un[πo(sn)] ∼ u0[n0], ..., un[nn]

where s0 ≡ G(initS(n)) and ∀0 ≤ i < n, si+1 ≡ G(πS(si)).

**Remark 4 (Forward Secrecy):** We did not study forward secrecy of RFID protocols, but this could easily be done. The standard forward secrecy assumption on a PRNG states that leaking the internal state πS(sn) of the PRNG (e.g. with a physical attack on the RFID chip) does not allow the adversary to gain any information about the previously generated names (πo(si))i≤n. This could be expressed in the logic using, for example, the following formula:

πo(s0), ..., πo(sn), πS(sn) ∼ n0, ..., nn, πS(sn)

where s0 ≡ G(initS(n)) and ∀0 ≤ i < n, si+1 ≡ G(πS(si)).

**Key Result:** This section justifies the abstraction used in earlier sections where we assumed names nR, nT are randomly generated. In practice, due to limited computing capabilities of RFID tags, they must be implemented using a cryptographic PRNG. Proposition 6 shows that we can safely abstract pseudo-random numbers as random numbers, provided:
1. The PRNG satisfies the standard security definition
2. The random seed is never used for any other purpose
3. There is strict separation between cryptographic material for random generation and other primitives

---

### النسخة العربية

**القسم V: مولد الأرقام شبه العشوائية**

يستخدم مولد الأرقام شبه العشوائية (PRNG) حالة داخلية، تُحدَّث عند كل استدعاء، ويُخرج رقماً شبه عشوائي. يمكن نمذجة هذا بدالة G تأخذ الحالة الداخلية كمدخل، وتُخرج زوجاً مع الحالة الداخلية الجديدة والرقم شبه العشوائي المولد (يُسترجع باستخدام الإسقاطين πS و πo). بالإضافة إلى ذلك، تُستخدم دالة initS لتهيئة الحالة الداخلية ببذرة عشوائية (يمكن أن تكون مشفرة بشكل ثابت في الوسم).

**التعريف 5 (PRNG):** مولد الأرقام شبه العشوائية هو ثنائي من الدوال متعددة الحدود (G, initS) بحيث لكل خصم PPT وهو A ولكل n، الكمية التالية ضئيلة في η:

|Pr (r ∈ {0, 1}^η : A(πo(s0), ..., πo(sn)) = 1) −
 Pr (r0, ..., rn ∈ {0, 1}^η : A(r0, ..., rn) = 1)|

حيث s0 = G(initS(r, 1^η)) ولجميع 0 ≤ i < n، si+1 = G(πS(si)).

يمكن ترجمة هذا في المنطق ببديهيات PRNGn:

πo(s0), ..., πo(sn) ∼ n0, ..., nn

حيث s0 ≡ G(initS(n)) و ∀0 ≤ i < n، si+1 ≡ G(πS(si)).

**القضية 5:** بديهيات (PRNGn)n صحيحة في أي نموذج حسابي Mc حيث يُفسر (G, initS) كمولد أرقام شبه عشوائية.

الصحة نتيجة مباشرة للتعريف 5.

لكل بروتوكول يوجد فيه فصل صارم بين المواد التشفيرية المستخدمة لتوليد الأرقام العشوائية والبدائل الأخرى (مثل مفاتيح التشفير)، يمكن تجريد الأرقام شبه العشوائية المولدة باستخدام مولد الأرقام شبه العشوائية كأرقام عشوائية باستخدام القضية التالية:

**القضية 6:** لكل أسماء n,(ni)i≤n وسياقات u0, ..., un لا تحتوي على هذه الأسماء، الصيغة التالية قابلة للاشتقاق باستخدام البديهيات في الشكل 1 و PRNGn:

u0[πo(s0)], ..., un[πo(sn)] ∼ u0[n0], ..., un[nn]

حيث s0 ≡ G(initS(n)) و ∀0 ≤ i < n، si+1 ≡ G(πS(si)).

**ملاحظة 4 (السرية الأمامية):** لم ندرس السرية الأمامية لبروتوكولات RFID، لكن يمكن القيام بذلك بسهولة. ينص افتراض السرية الأمامية القياسي على مولد الأرقام شبه العشوائية على أن تسريب الحالة الداخلية πS(sn) لمولد الأرقام شبه العشوائية (مثلاً بهجوم مادي على شريحة RFID) لا يسمح للخصم بالحصول على أي معلومات حول الأسماء المولدة مسبقاً (πo(si))i≤n. يمكن التعبير عن هذا في المنطق باستخدام، على سبيل المثال، الصيغة التالية:

πo(s0), ..., πo(sn), πS(sn) ∼ n0, ..., nn, πS(sn)

حيث s0 ≡ G(initS(n)) و ∀0 ≤ i < n، si+1 ≡ G(πS(si)).

**النتيجة الرئيسية:** يبرر هذا القسم التجريد المستخدم في الأقسام السابقة حيث افترضنا أن الأسماء nR، nT مولدة عشوائياً. عملياً، بسبب قدرات الحوسبة المحدودة لوسوم RFID، يجب تنفيذها باستخدام مولد أرقام شبه عشوائية تشفيري. توضح القضية 6 أنه يمكننا تجريد الأرقام شبه العشوائية بأمان كأرقام عشوائية، بشرط:
1. يلبي مولد الأرقام شبه العشوائية التعريف الأمني القياسي
2. لا تُستخدم البذرة العشوائية أبداً لأي غرض آخر
3. يوجد فصل صارم بين المواد التشفيرية للتوليد العشوائي والبدائل الأخرى

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - PRNG (مولد أرقام شبه عشوائية)
  - Internal state (حالة داخلية)
  - Random seed (بذرة عشوائية)
  - Forward secrecy (سرية أمامية)
  - Physical attack (هجوم مادي)
  - Strict separation (فصل صارم)
  - Abstraction (تجريد)
- **Equations:** Definition 5 with probability expressions
- **Citations:** None
- **Special handling:**
  - Formal definition with quantifiers
  - Probability expressions
  - Logical derivation
  - Security assumption formalization

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
