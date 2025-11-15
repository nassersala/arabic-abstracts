# Section 14: Gradients and Duality
## القسم 14: التدرجات والازدواجية

**Section:** Gradients and Duality
**Translation Quality:** 0.86
**Glossary Terms Used:** gradient, optimization, automatic differentiation, linear map, vector space

---

### English Version

Gradients and Duality

As a special case of reverse-mode automatic differentiation, let's consider its use to compute gradients, i.e., derivatives of functions with a scalar codomain, as with gradient-based optimization.

Given a vector space $A$ over a scalar field $s$, the dual of $A$ is $A \multimap s$, i.e., the linear maps to the underlying field [Lang, 1987]. This dual space is also a vector space, and when $A$ has finite dimension, it is isomorphic to its dual. In particular, every linear map in $A \multimap s$ has the form $dot \, u$ for some $u :: A$, where $dot$ is the curried dot product:

```haskell
class HasDot s u where dot :: u -> (u ⊸ s)

instance HasDot R R where dot = scale
instance (HasDot s a, HasDot s b) => HasDot s (a × b) where
    dot (u, v) = dot u ⊕ dot v
```

The $Cont_r^k$ construction from Section 12 works for any type/object $r$, so let's take $r$ to be the scalar field $s$. The internal representation of $Cont_s^k \, a \, b$ is $(b \multimap s) \to (a \multimap s)$, which is isomorphic to $b \to a$. Call this representation the dual (or "opposite") of $k$:

```haskell
newtype Dual k a b = Dual (b `k` a)
```

To construct dual representations of (generalized) linear maps, it suffices to convert from $Cont_s^k$ to $Dual \, k$ by a functor we will now derive.

Note that the instances exactly dualize a computation, reversing sequential compositions and swapping corresponding Cartesian and Cocartesian operations. From a matrix perspective, duality is transposition, turning an $m \times n$ matrix into an $n \times m$ matrix. Note, however, that $Dual \, k$ involves no actual matrix computations unless $k$ does.

---

### النسخة العربية

التدرجات والازدواجية

كحالة خاصة من التفاضل الآلي ذي النمط العكسي، لنفكر في استخدامه لحساب التدرجات، أي مشتقات الدوال ذات المجال المشترك القياسي، كما في التحسين القائم على التدرج.

بالنظر إلى فضاء متجه $A$ على حقل قياسي $s$، فإن مزدوج $A$ هو $A \multimap s$، أي الخرائط الخطية للحقل الأساسي [Lang, 1987]. هذا الفضاء المزدوج هو أيضاً فضاء متجه، وعندما يكون لـ $A$ بُعد محدود، فإنه متماثل الشكل مع مزدوجه. على وجه الخصوص، كل خريطة خطية في $A \multimap s$ لها الشكل $dot \, u$ لبعض $u :: A$، حيث $dot$ هو الضرب النقطي المكرر:

```haskell
class HasDot s u where dot :: u -> (u ⊸ s)

instance HasDot R R where dot = scale
instance (HasDot s a, HasDot s b) => HasDot s (a × b) where
    dot (u, v) = dot u ⊕ dot v
```

بناء $Cont_r^k$ من القسم 12 يعمل لأي نوع/كائن $r$، لذا لنأخذ $r$ ليكون الحقل القياسي $s$. التمثيل الداخلي لـ $Cont_s^k \, a \, b$ هو $(b \multimap s) \to (a \multimap s)$، وهو متماثل الشكل مع $b \to a$. نسمي هذا التمثيل المزدوج (أو "المعاكس") لـ $k$:

```haskell
newtype Dual k a b = Dual (b `k` a)
```

لبناء تمثيلات مزدوجة للخرائط الخطية (المعممة)، يكفي التحويل من $Cont_s^k$ إلى $Dual \, k$ بواسطة دالة فئوية سنشتقها الآن.

لاحظ أن النسخ تُزدوج حساباً بالضبط، معكسةً التراكيب المتسلسلة ومبادلةً العمليات الديكارتية والمشتركة الديكارتية المقابلة. من منظور المصفوفة، الازدواجية هي التبديل، تحويل مصفوفة $m \times n$ إلى مصفوفة $n \times m$. لاحظ، مع ذلك، أن $Dual \, k$ لا يتضمن حسابات مصفوفة فعلية ما لم يفعل $k$ ذلك.

---

### Translation Notes

- **Key terms:** dual space, gradient, scalar field, dot product, transposition
- **Code examples:** Haskell type class definitions
- **Citations:** [Lang 1987]
- **Special handling:** Mathematical duality concepts; matrix-free computations

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
