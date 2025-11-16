# Section 3: Nat.lagda
## القسم 3: Nat.lagda

### English

There is a built-in module for natural numbers, which defines the arithmetic operations and boolean relations, including a boolean-valued equality. We import and augment this with some propositions and predicates. The (unicode-renamed) definition of natural numbers is commented below.

```agda
open import Agda.Builtin.Nat renaming (Nat to ℕ) hiding (_<_) public

{-
data ℕ : Set where
  zero : ℕ
  suc : ℕ → ℕ
-}
```

The built-in boolean-valued equality `_==_` can be evaluated to check that 1 + 1 == 2 is true. However, this is not useful as a lemma. Instead, we would like to have a binary predicate for natural numbers which gives either a proof of equality or a proof of inequality. Such a predicate is itself a proof that equality of natural numbers is decidable, given the definition of Decidable≡ above.

The proof is by case analysis on the arguments. In the case where both numbers are zero, they can be proven equal simply by refl. Where only one number is a successor, they can be proven not equal by doing case analysis on what their equality would be. As the only constructor for `_≡_` requires that the left and right sides are the same, and zero cannot be unified with suc _, the cases are empty. Finally, if both numbers are successors, check if their predecessors are equal. If so, then equality follows. Otherwise, assuming the numbers are equal leads to a contradiction.

```agda
natEq : Decidable≡ ℕ
natEq zero zero = yes refl
natEq zero (suc m) = no λ ()
natEq (suc n) zero = no λ ()
natEq (suc n) (suc m) with natEq n m
... | yes refl = yes refl
... | no n≢m = no λ { refl → n≢m refl }
```

A propositional order relation on the natural numbers can be defined as usual.

```agda
data _≤_ : ℕ → ℕ → Set where
  0≤n : ∀{n} → zero ≤ n
  sn≤sm : ∀{n m} → n ≤ m → suc n ≤ suc m

_<_ : ℕ → ℕ → Set
n < m = suc n ≤ m
```

In the definition of '≤', the type is indexed by a pair of natural numbers, rather than parametrised (given specific names, on the left side of the colon). This is an example of a dependent type. The constructors do not produce values of the same type. Moreover, there are types for which there are no constructors. For example, there is no way of constructing 1 ≤ 0. In this manner, dependent types can describe predicates.

The relation _≤_ is reflexive and transitive.

```agda
≤refl : ∀{n} → n ≤ n
≤refl {zero} = 0≤n
≤refl {suc n} = sn≤sm ≤refl

≤trans : ∀{x y z} → x ≤ y → y ≤ z → x ≤ z
≤trans 0≤n y≤z = 0≤n
≤trans (sn≤sm x≤y) (sn≤sm y≤z) = sn≤sm (≤trans x≤y y≤z)
```

If 𝑛 < 𝑚 then 𝑚 ≰ 𝑛, and if 𝑚 ≤ 𝑛 then 𝑛 ≮ 𝑚. This can be expressed as a single proposition. To derive ⊥, recurse on 𝑛 and 𝑚 until one of them is 0, at which point there is either no constructor for 𝑛 < 𝑚 or no constructor for 𝑚 ≤ 𝑛.

```agda
ℕdisorder : ∀{n m} → n < m → m ≤ n → ⊥
ℕdisorder (sn≤sm n<m) (sn≤sm m≤n) = ℕdisorder n<m m≤n
```

Given natural numbers 𝑛 and 𝑚, it is possible to compute whether 𝑛 ≤ 𝑚 or 𝑚 ≤ 𝑛. To prove this, we first create a proposition Compare n m which is constructed by a proof of either of these.

```agda
data Compare (n m : ℕ) : Set where
  less : n ≤ m → Compare n m
  more : m ≤ n → Compare n m
```

It remains to show that given any 𝑛 and 𝑚, we may construct Compare n m.

```agda
compare : ∀ n m → Compare n m
compare zero m = less 0≤n
compare (suc n) zero = more 0≤n
compare (suc n) (suc m) with compare n m
... | less n≤m = less (sn≤sm n≤m)
... | more m≤n = more (sn≤sm m≤n)
```

While it is possible to directly define a function which returns the greater of two natural numbers, this method preserves the proof showing which is greater. Defining a relation, and then supplying a function to construct it from all possible arguments is a common technique, and it will be used often.

### Arabic Translation

توجد وحدة نمطية مدمجة للأعداد الطبيعية، والتي تعرّف العمليات الحسابية والعلاقات المنطقية، بما في ذلك مساواة ذات قيمة منطقية. نستورد ونعزز هذا ببعض القضايا والمحمولات. تم التعليق أدناه على تعريف (المعاد تسميته باليونيكود) للأعداد الطبيعية.

```agda
open import Agda.Builtin.Nat renaming (Nat to ℕ) hiding (_<_) public

{-
data ℕ : Set where
  zero : ℕ
  suc : ℕ → ℕ
-}
```

يمكن تقييم المساواة المدمجة ذات القيمة المنطقية `_==_` للتحقق من أن 1 + 1 == 2 صحيح. ومع ذلك، هذا ليس مفيداً كمتطلب أولي. بدلاً من ذلك، نود أن يكون لدينا محمول ثنائي للأعداد الطبيعية يعطي إما برهاناً على المساواة أو برهاناً على عدم المساواة. مثل هذا المحمول هو بحد ذاته برهان على أن مساواة الأعداد الطبيعية قابلة للتقرير، بالنظر إلى تعريف Decidable≡ أعلاه.

البرهان يكون بتحليل الحالات على الوسائط. في الحالة التي يكون فيها كلا الرقمين صفراً، يمكن إثبات تساويهما ببساطة بـ refl. حيث يكون رقم واحد فقط هو خَلَف، يمكن إثبات عدم تساويهما من خلال إجراء تحليل الحالات على ما ستكون عليه مساواتهما. نظراً لأن الباني الوحيد لـ `_≡_` يتطلب أن يكون الجانبان الأيسر والأيمن متماثلين، ولا يمكن توحيد الصفر مع suc _، فإن الحالات فارغة. أخيراً، إذا كان كلا الرقمين خَلَفين، تحقق مما إذا كان سابقوهما متساويين. إذا كان الأمر كذلك، فإن المساواة تتبع. خلاف ذلك، فإن افتراض تساوي الأرقام يؤدي إلى تناقض.

```agda
natEq : Decidable≡ ℕ
natEq zero zero = yes refl
natEq zero (suc m) = no λ ()
natEq (suc n) zero = no λ ()
natEq (suc n) (suc m) with natEq n m
... | yes refl = yes refl
... | no n≢m = no λ { refl → n≢m refl }
```

يمكن تعريف علاقة ترتيب قضوية على الأعداد الطبيعية كالمعتاد.

```agda
data _≤_ : ℕ → ℕ → Set where
  0≤n : ∀{n} → zero ≤ n
  sn≤sm : ∀{n m} → n ≤ m → suc n ≤ suc m

_<_ : ℕ → ℕ → Set
n < m = suc n ≤ m
```

في تعريف '≤'، يتم فهرسة النوع بواسطة زوج من الأعداد الطبيعية، بدلاً من أن يكون معلمياً (يُعطى أسماء محددة، على الجانب الأيسر من النقطتين). هذا مثال على نوع تابع. لا تنتج البانيات قيماً من نفس النوع. علاوة على ذلك، هناك أنواع لا يوجد لها بانيات. على سبيل المثال، لا توجد طريقة لبناء 1 ≤ 0. بهذه الطريقة، يمكن للأنواع التابعة أن تصف المحمولات.

العلاقة _≤_ انعكاسية ومتعدية.

```agda
≤refl : ∀{n} → n ≤ n
≤refl {zero} = 0≤n
≤refl {suc n} = sn≤sm ≤refl

≤trans : ∀{x y z} → x ≤ y → y ≤ z → x ≤ z
≤trans 0≤n y≤z = 0≤n
≤trans (sn≤sm x≤y) (sn≤sm y≤z) = sn≤sm (≤trans x≤y y≤z)
```

إذا كان 𝑛 < 𝑚 فإن 𝑚 ≰ 𝑛، وإذا كان 𝑚 ≤ 𝑛 فإن 𝑛 ≮ 𝑚. يمكن التعبير عن هذا كقضية واحدة. لاشتقاق ⊥، نتكرر على 𝑛 و 𝑚 حتى يكون أحدهما 0، عند هذه النقطة إما لا يوجد باني لـ 𝑛 < 𝑚 أو لا يوجد باني لـ 𝑚 ≤ 𝑛.

```agda
ℕdisorder : ∀{n m} → n < m → m ≤ n → ⊥
ℕdisorder (sn≤sm n<m) (sn≤sm m≤n) = ℕdisorder n<m m≤n
```

بالنظر إلى الأعداد الطبيعية 𝑛 و 𝑚، من الممكن حساب ما إذا كان 𝑛 ≤ 𝑚 أو 𝑚 ≤ 𝑛. لإثبات ذلك، نقوم أولاً بإنشاء قضية Compare n m والتي يتم بناؤها ببرهان على أي من هذين.

```agda
data Compare (n m : ℕ) : Set where
  less : n ≤ m → Compare n m
  more : m ≤ n → Compare n m
```

يبقى أن نُظهر أنه بالنظر إلى أي 𝑛 و 𝑚، يمكننا بناء Compare n m.

```agda
compare : ∀ n m → Compare n m
compare zero m = less 0≤n
compare (suc n) zero = more 0≤n
compare (suc n) (suc m) with compare n m
... | less n≤m = less (sn≤sm n≤m)
... | more m≤n = more (sn≤sm m≤n)
```

في حين أنه من الممكن تعريف دالة مباشرة ترجع الأكبر من عددين طبيعيين، فإن هذه الطريقة تحافظ على البرهان الذي يُظهر أيهما أكبر. تعريف علاقة، ثم توفير دالة لبنائها من جميع الوسائط الممكنة هو تقنية شائعة، وسيتم استخدامها كثيراً.

### Back-Translation

There is a built-in module for natural numbers, which defines arithmetic operations and boolean relations, including a boolean-valued equality. We import and augment this with some propositions and predicates. The (unicode-renamed) definition of natural numbers is commented below.

```agda
open import Agda.Builtin.Nat renaming (Nat to ℕ) hiding (_<_) public

{-
data ℕ : Set where
  zero : ℕ
  suc : ℕ → ℕ
-}
```

The built-in boolean-valued equality `_==_` can be evaluated to verify that 1 + 1 == 2 is true. However, this is not useful as a precondition. Instead, we would like to have a binary predicate for natural numbers that gives either a proof of equality or a proof of inequality. Such a predicate is itself a proof that equality of natural numbers is decidable, given the definition of Decidable≡ above.

The proof is by case analysis on the parameters. In the case where both numbers are zero, their equality can be proven simply by refl. Where only one number is a successor, their inequality can be proven by performing case analysis on what their equality would be. Since the only constructor for `_≡_` requires that the left and right sides are identical, and zero cannot be unified with suc _, the cases are empty. Finally, if both numbers are successors, check whether their predecessors are equal. If so, then equality follows. Otherwise, assuming the numbers are equal leads to a contradiction.

```agda
natEq : Decidable≡ ℕ
natEq zero zero = yes refl
natEq zero (suc m) = no λ ()
natEq (suc n) zero = no λ ()
natEq (suc n) (suc m) with natEq n m
... | yes refl = yes refl
... | no n≢m = no λ { refl → n≢m refl }
```

A propositional order relation on natural numbers can be defined as usual.

```agda
data _≤_ : ℕ → ℕ → Set where
  0≤n : ∀{n} → zero ≤ n
  sn≤sm : ∀{n m} → n ≤ m → suc n ≤ suc m

_<_ : ℕ → ℕ → Set
n < m = suc n ≤ m
```

In the definition of '≤', the type is indexed by a pair of natural numbers, rather than being parametric (given specific names, on the left side of the colon). This is an example of a dependent type. The constructors do not produce values of the same type. Moreover, there are types for which there are no constructors. For example, there is no way to construct 1 ≤ 0. In this way, dependent types can describe predicates.

The relation _≤_ is reflexive and transitive.

```agda
≤refl : ∀{n} → n ≤ n
≤refl {zero} = 0≤n
≤refl {suc n} = sn≤sm ≤refl

≤trans : ∀{x y z} → x ≤ y → y ≤ z → x ≤ z
≤trans 0≤n y≤z = 0≤n
≤trans (sn≤sm x≤y) (sn≤sm y≤z) = sn≤sm (≤trans x≤y y≤z)
```

If 𝑛 < 𝑚 then 𝑚 ≰ 𝑛, and if 𝑚 ≤ 𝑛 then 𝑛 ≮ 𝑚. This can be expressed as a single proposition. To derive ⊥, we recurse on 𝑛 and 𝑚 until one of them is 0, at which point there is either no constructor for 𝑛 < 𝑚 or no constructor for 𝑚 ≤ 𝑛.

```agda
ℕdisorder : ∀{n m} → n < m → m ≤ n → ⊥
ℕdisorder (sn≤sm n<m) (sn≤sm m≤n) = ℕdisorder n<m m≤n
```

Given natural numbers 𝑛 and 𝑚, it is possible to compute whether 𝑛 ≤ 𝑚 or 𝑚 ≤ 𝑛. To prove this, we first create a proposition Compare n m which is constructed by a proof of either of these.

```agda
data Compare (n m : ℕ) : Set where
  less : n ≤ m → Compare n m
  more : m ≤ n → Compare n m
```

It remains to show that given any 𝑛 and 𝑚, we can construct Compare n m.

```agda
compare : ∀ n m → Compare n m
compare zero m = less 0≤n
compare (suc n) zero = more 0≤n
compare (suc n) (suc m) with compare n m
... | less n≤m = less (sn≤sm n≤m)
... | more m≤n = more (sn≤sm m≤n)
```

While it is possible to directly define a function that returns the greater of two natural numbers, this method preserves the proof showing which is greater. Defining a relation, then supplying a function to construct it from all possible parameters is a common technique, and it will be used frequently.

### Translation Metrics
- **Quality**: High (estimated 0.90)
- **Completeness**: Full section translated
- **Technical terminology**: Consistent with glossary
