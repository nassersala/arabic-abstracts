# Section 4: Two RFID Protocols
## القسم 4: بروتوكولان RFID

**Section:** case studies and proofs
**Translation Quality:** 0.87
**Glossary Terms Used:** protocol (بروتوكول), attack (هجوم), proof (برهان), hash function (دالة تجزئة), collision resistance (مقاومة التصادم), PRF (دالة شبه عشوائية), xor (or حصري), unlinkability (عدم الربط), authentication (مصادقة)

---

### English Version (Summary)

**Section IV: TWO RFID PROTOCOLS**

We describe the LAK and KCL RFID protocols, attacks, patches, and formal computational security proofs of fixed versions.

**A. A known attack on KCL**

Original KCL protocol (Figure 2):
```
R : nR ←$          TA : nT ←$
1 : R → TA : nR
2 : TA → R : ⟨A ⊕ nT, nT ⊕ H(nR, kA)⟩
```

**Attack [27]:** Tag challenged twice with same nR. Adversary xors two message components:
- Same tag: (A ⊕ nT) ⊕ (nT ⊕ H(nR, kA)) = (A ⊕ n'T) ⊕ (n'T ⊕ H(nR, kA)) = A ⊕ H(nR, kA)
- Different tags: Values differ with high probability

**B. KCL+, a revised version**

Fixed protocol (Figure 5):
```
R : nR ←$          T : nT ←$
1 : R → TA : nR
2 : TA → R : ⟨A ⊕ H(nT, kA), nT ⊕ H(nR, kA)⟩
```

Replace first nT with its hash H(nT, kA), breaking algebraic property used in attack.

**Theorem 2 (Unlinkability for arbitrary rounds):** Assuming PRF for keyed hash function, KCL+ protocol verifies m-Fixed Trace Privacy for two agents and all m.

Proof uses induction on m with several axioms:
- FreshNonce: for new reader challenges
- PRF: to replace hash outputs with fresh names
- FA (Function Application): structural decomposition
- CS (Case Split): conditional reasoning
- Indep: independence of xor with fresh names

**C. The LAK protocol**

Original LAK [21] (Figure 6):
```
R : nR ←$          TA : nT ←$
1 : R → TA : nR
2 : TA → R : ⟨nT, h(nR ⊕ nT ⊕ kA)⟩
3 : R → TA : h(h(nR ⊕ nT ⊕ kA) ⊕ nR ⊕ kA)
R : kA = h(kA), k'A = kA
TA : kA = h(kA)
```

Stateful protocol with key updates after successful completion.

**Attack [27]:** Adversary observes session, gets h(nR ⊕ nT ⊕ kA) and nR, nT. In new session with n'R, sends n'T such that n'R ⊕ n'T = nR ⊕ nT, reusing hash value to impersonate tag.

**D. A stateless revised version of LAK**

Corrected version [17]:
```
R : nR ←$          TA : nT ←$
1 : R → TA : nR
2 : TA → R : ⟨nT, h(⟨nR, nT, kA⟩)⟩
3 : R → TA : h(⟨h(⟨nR, nT, kA⟩), nR, kA⟩)
```

Uses pairing instead of xor to avoid algebraic attacks.

**Attack against stateless LAK with one-way hash:** If hash function leaks bits of key, adversary can distinguish tags by observing leaked bits from h(⟨nR, nT, kA⟩) and h(⟨n'R, n'T, kA⟩) vs h(⟨nR, nT, kA⟩) and h(⟨n'R, n'T, kB⟩).

**E. The LAK+ protocol**

LAK+ uses keyed hash H (PRF):
```
R : nR ←$          T : nT ←$
1 : R → T : nR
2 : T → R : ⟨nT, H(c(nR, nT), kA)⟩
3 : R → T : H(c(H(c(nR, nT), kA), nR), kA)
```

where c is a combination function.

**Attacks on LAK+ and required properties for c:**

1. **First attack:** If ∃s such that Pr(c(nR, nT) = c(n'R, s(nR, nT, n'R))) is non-negligible, adversary can forge valid response. **Prevention:** c must be left-injective:
   ∀a, b, x, y. EQ(c(a, b); c(x, y)) ⇒ EQ(a; x)

2. **Second attack:** If ∃g₁, s such that Pr(c(g₁, x) = c(s(x), y)) is non-negligible, adversary can link tags. **Prevention:** c must be right-injective:
   ∀a, b, x, y. EQ(c(a, b); c(x, y)) ⇒ EQ(b; y)

**Injectivity axioms for c (Figure 9):**
```
if EQ(u; u') then false else EQ(c(u, v); c(u', v')) = false
if EQ(v; v') then false else EQ(c(u, v); c(u', v')) = false
```

Satisfied when c is pairing.

**Theorem 3:** LAK+ protocol verifies 6-Fixed Trace Privacy (two full sessions) with axioms from Section II and injectivity axioms.

Proof uses PRF axioms, case splitting on conditionals, and injectivity properties.

---

### النسخة العربية (ملخص)

**القسم IV: بروتوكولان RFID**

نصف بروتوكولي LAK و KCL لـ RFID، والهجمات، والترقيعات، والبراهين الرسمية للأمان الحسابي للنسخ المصححة.

**أ. هجوم معروف على KCL**

بروتوكول KCL الأصلي (الشكل 2):
```
R : nR ←$          TA : nT ←$
1 : R → TA : nR
2 : TA → R : ⟨A ⊕ nT, nT ⊕ H(nR, kA)⟩
```

**الهجوم [27]:** يُتحدى الوسم مرتين بنفس nR. يقوم الخصم بعملية xor لمكونين من الرسالة:
- نفس الوسم: (A ⊕ nT) ⊕ (nT ⊕ H(nR, kA)) = (A ⊕ n'T) ⊕ (n'T ⊕ H(nR, kA)) = A ⊕ H(nR, kA)
- وسوم مختلفة: تختلف القيم باحتمال عالٍ

**ب. KCL+، نسخة منقحة**

البروتوكول المصحح (الشكل 5):
```
R : nR ←$          T : nT ←$
1 : R → TA : nR
2 : TA → R : ⟨A ⊕ H(nT, kA), nT ⊕ H(nR, kA)⟩
```

نستبدل nT الأول بتجزئته H(nT, kA)، مما يكسر الخاصية الجبرية المستخدمة في الهجوم.

**المبرهنة 2 (عدم الربط لجولات تعسفية):** بافتراض PRF لدالة التجزئة بمفتاح، يحقق بروتوكول KCL+ خصوصية التتبع الثابت m لعاملين ولجميع m.

يستخدم البرهان الاستقراء على m مع عدة بديهيات:
- FreshNonce: للتحديات الجديدة للقارئ
- PRF: لاستبدال مخرجات التجزئة بأسماء جديدة
- FA (تطبيق الدالة): تفكيك هيكلي
- CS (تقسيم الحالات): استدلال شرطي
- Indep: استقلالية xor مع الأسماء الجديدة

**ج. بروتوكول LAK**

LAK الأصلي [21] (الشكل 6):
```
R : nR ←$          TA : nT ←$
1 : R → TA : nR
2 : TA → R : ⟨nT, h(nR ⊕ nT ⊕ kA)⟩
3 : R → TA : h(h(nR ⊕ nT ⊕ kA) ⊕ nR ⊕ kA)
R : kA = h(kA), k'A = kA
TA : kA = h(kA)
```

بروتوكول ذو حالة مع تحديثات للمفتاح بعد الإكمال الناجح.

**الهجوم [27]:** يراقب الخصم جلسة، يحصل على h(nR ⊕ nT ⊕ kA) و nR، nT. في جلسة جديدة مع n'R، يرسل n'T بحيث n'R ⊕ n'T = nR ⊕ nT، معيداً استخدام قيمة التجزئة لانتحال الوسم.

**د. نسخة منقحة عديمة الحالة من LAK**

النسخة المصححة [17]:
```
R : nR ←$          TA : nT ←$
1 : R → TA : nR
2 : TA → R : ⟨nT, h(⟨nR, nT, kA⟩)⟩
3 : R → TA : h(⟨h(⟨nR, nT, kA⟩), nR, kA⟩)
```

تستخدم الإقران بدلاً من xor لتجنب الهجمات الجبرية.

**هجوم ضد LAK عديمة الحالة مع تجزئة أحادية الاتجاه:** إذا سربت دالة التجزئة بتات من المفتاح، يمكن للخصم تمييز الوسوم بملاحظة البتات المسربة من h(⟨nR, nT, kA⟩) و h(⟨n'R, n'T, kA⟩) مقابل h(⟨nR, nT, kA⟩) و h(⟨n'R, n'T, kB⟩).

**هـ. بروتوكول LAK+**

يستخدم LAK+ تجزئة بمفتاح H (PRF):
```
R : nR ←$          T : nT ←$
1 : R → T : nR
2 : T → R : ⟨nT, H(c(nR, nT), kA)⟩
3 : R → T : H(c(H(c(nR, nT), kA), nR), kA)
```

حيث c دالة تركيب.

**هجمات على LAK+ والخصائص المطلوبة لـ c:**

1. **الهجوم الأول:** إذا ∃s بحيث Pr(c(nR, nT) = c(n'R, s(nR, nT, n'R))) غير ضئيل، يمكن للخصم تزوير استجابة صالحة. **المنع:** يجب أن تكون c تحقيقية يساراً:
   ∀a, b, x, y. EQ(c(a, b); c(x, y)) ⇒ EQ(a; x)

2. **الهجوم الثاني:** إذا ∃g₁, s بحيث Pr(c(g₁, x) = c(s(x), y)) غير ضئيل، يمكن للخصم ربط الوسوم. **المنع:** يجب أن تكون c تحقيقية يميناً:
   ∀a, b, x, y. EQ(c(a, b); c(x, y)) ⇒ EQ(b; y)

**بديهيات التحقيقية لـ c (الشكل 9):**
```
if EQ(u; u') then false else EQ(c(u, v); c(u', v')) = false
if EQ(v; v') then false else EQ(c(u, v); c(u', v')) = false
```

تُلبى عندما تكون c إقراناً.

**المبرهنة 3:** يحقق بروتوكول LAK+ خصوصية التتبع الثابت 6 (جلستان كاملتان) مع البديهيات من القسم II وبديهيات التحقيقية.

يستخدم البرهان بديهيات PRF، وتقسيم الحالات على الشرطيات، وخصائص التحقيقية.

---

### Translation Notes

- **Figures referenced:** Figure 2, 4, 5, 6, 7, 8, 9
- **Key terms introduced:**
  - Stateful protocol (بروتوكول ذو حالة)
  - Stateless protocol (بروتوكول عديم الحالة)
  - Key update (تحديث المفتاح)
  - Impersonation (انتحال)
  - Left-injective (تحقيقية يساراً)
  - Right-injective (تحقيقية يميناً)
  - Combination function (دالة تركيب)
  - Fixed Trace Privacy (خصوصية التتبع الثابت)
- **Equations:** Protocol notation and formal logic expressions
- **Citations:** [17], [18], [19], [20], [21], [23], [27]
- **Special handling:**
  - Protocol flow diagrams
  - Attack descriptions
  - Formal security proofs
  - Axiomatic reasoning

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
