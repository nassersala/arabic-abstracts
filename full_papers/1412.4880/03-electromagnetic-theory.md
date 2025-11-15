# Section 3: Electromagnetic Theory
## القسم 3: النظرية الكهرومغناطيسية

**Section:** electromagnetic-theory
**Translation Quality:** 0.87
**Glossary Terms Used:** vector field, scalar field, curve, type synonym, higher-order functions, line integral, charge distribution, current

---

### English Version

## 3 Electromagnetic Theory

One type of problem that occurs in electromagnetic theory is the calculation of electric and magnetic fields produced by charge and current distributions.

### 3.1 Electric field produced by a continuous charge distribution

The electric field at position $\vec{r}$ produced by a charge distributed over a curve C is

$$\vec{E}(\vec{r}) = \frac{1}{4\pi\epsilon_0} \int_C \frac{\lambda(\vec{r}')(\vec{r} - \vec{r}')}{|\vec{r} - \vec{r}'|^3} dl',$$ (1)

where $\lambda(\vec{r}')$ is the linear charge density at $\vec{r}'$ and $\epsilon_0$ is a constant called the permittivity of free space.

Unlike in mechanics, where the simple expression of Newton's second law hides the complexity of the situation, here the notation is daunting. One issue in particular that the notation hides from the beginning student is that in order to calculate the electric field, we need to have (1) a curve C describing where the charge is, and (2) a charge density λ, and that is all.

Since curves are important in a number of places in electromagnetic theory, we define a data type for curves.

```haskell
data Curve = Curve { curveFunc          :: Double -> Position
                   , startingCurveParam :: Double
                   , endingCurveParam   :: Double }
```

A Curve is a parametrized curve along with starting and ending parameters. The parametrized curve is expressed here in terms of a Position data type, defined similarly to Vec, but without the vector operations.

Here are some example curves.

```haskell
circularLoop :: Double -> Curve
circularLoop radius
  = Curve (\t -> cart (radius * cos t)
                      (radius * sin t)
                      0
          ) 0 (2*pi)

line :: Double -> Curve
line l = Curve (\t -> cart 0 0 t) (-l/2) (l/2)
```

The function cart produces a Position by giving Cartesian coordinates.

Equipped with our Curve data type, we next need a way to integrate over a curve. A line integral can have either a scalar or vector integrand (to calculate electric field, we'll use a vector integrand, but to calculate electric potential, we would use a scalar integrand).

$$\int_C f(\vec{r}')dl'$$ or $$\int_C \vec{F}(\vec{r}')dl'$$

We use type synonyms to describe what a scalar field is and what a vector field is.

```haskell
type ScalarField = Position -> Double
type VectorField = Position -> Vec
type Field v     = Position -> v
```

A scalar field is an assignment of a scalar (number) to each position in space. A vector field is an assignment of a vector to each position in space. We also want to be able to refer to a field that could be either a scalar field or a vector field, so we define Field v.

I usually ask students to write a simple numerical integrator using the trapezoidal rule, to get a sense for what is required. Then, I ask them to use code that I have written to integrate over a curve. We use a general purpose line integral with the following type.

```haskell
simpleLineIntegral
  :: (InnerSpace v, Scalar v ~ Double)
  => Int        -- ^ number of intervals
  -> Field v    -- ^ scalar or vector field
  -> Curve      -- ^ curve to integrate over
  -> v          -- ^ scalar or vector result
```

The integrator works by chopping the curve into a number to intervals, evaluating the field on each interval, multiplying each value by the length of its interval, and summing.

Now we can calculate the electric field (1) of a one-dimensional charge distribution.

```haskell
eFieldFromLineCharge
  :: ScalarField  -- ^ linear charge density lambda
  -> Curve        -- ^ geometry of the line charge
  -> VectorField  -- ^ electric field (in V/m)
eFieldFromLineCharge lambda c r
  = k *^ simpleLineIntegral 1000 integrand c
  where
    k = 9e9  -- 1 / (4 * pi * epsilon0)
    integrand r' = lambda r' *^ d ^/ magnitude d ** 3
      where
        d = displacement r' r
```

Notice how types and higher-order functions are an essential aspect of this definition. The types ScalarField and VectorField are themselves functions, one used as input and one used as output of the eFieldFromLineCharge function. The Curve type, like Vec and Position, is used to package information that, from the perspective of physics, rightfully belongs together. Also note how the type signature describes that the charge density λ and the curve C are the only inputs necessary to make the calculation.

### 3.2 Magnetic field produced by a current-carrying wire

Let us take the example of the magnetic field produced by a current-carrying wire. We will allow the wire to be of any shape, and to carry any amount of current. We wish to calculate the magnetic field produced by the wire. The magnetic field at position $\vec{r}$ produced by a current I flowing along a curve C is given by the Biot-Savart law.

$$\vec{B}(\vec{r}) = \frac{\mu_0 I}{4\pi} \int_C \frac{d\vec{l}' \times (\vec{r} - \vec{r}')}{|\vec{r} - \vec{r}'|^3}$$ (2)

To implement the Biot-Savart law, it is useful to have a general purpose "crossed line integral".

$$\int_C \vec{F}(\vec{r}') \times d\vec{l}'$$

```haskell
-- | Calculates integral vf x dl over curve.
crossedLineIntegral
  :: Int          -- ^ number of intervals
  -> VectorField  -- ^ vector field
  -> Curve        -- ^ curve to integrate over
  -> Vec          -- ^ vector result
```

Do we really need a new integrator for the crossed line integral? Can we not write

$$\int_C \vec{F}(\vec{r}') \times d\vec{l}' = \int_C \vec{F}(\vec{r}') \times \hat{t}dl'$$

where $\hat{t}$ is a unit tangent to the curve, and use our previous integrator, applying the cross product in the integrand? That is a possibility, but I did not want to burden the user with supplying tangent vectors along the curve. Part of the motivation for the functions which calculate electric and magnetic fields is to show how little is required to make the calculation.

Here is an implementation of the Biot-Savart law (2).

```haskell
bFieldFromLineCurrent
  :: Current      -- ^ current (in Amps)
  -> Curve        -- ^ geometry of the line current
  -> VectorField  -- ^ magnetic field (in Tesla)
bFieldFromLineCurrent i c r
  = k *^ crossedLineIntegral 1000 integrand c
  where
    k = 1e-7  -- mu0 / (4 * pi)
    integrand r' = (-i) *^ d ^/ magnitude d ** 3
      where
        d = displacement r' r
```

Here, Current is a synonym for Double.

```haskell
type Current = Double
```

The minus sign prefixing the current in the integrand is because the crossed line integral performs the cross product in the opposite order from the Biot-Savart law. The magnetic field produced by a circular current loop is a great problem for numerical investigation; despite the symmetry, the magnetic field from a circular loop is not analytically calculable (except on the axis of symmetry). Finally, note how the type signature shows that a current I and a curve C are all the information needed to calculate magnetic field.

---

### النسخة العربية

## 3 النظرية الكهرومغناطيسية

أحد أنواع المسائل التي تحدث في النظرية الكهرومغناطيسية هو حساب الحقول الكهربائية والمغناطيسية الناتجة عن توزيعات الشحنة والتيار.

### 3.1 الحقل الكهربائي الناتج عن توزيع شحنة مستمر

الحقل الكهربائي عند الموضع $\vec{r}$ الناتج عن شحنة موزعة على منحنى C هو

$$\vec{E}(\vec{r}) = \frac{1}{4\pi\epsilon_0} \int_C \frac{\lambda(\vec{r}')(\vec{r} - \vec{r}')}{|\vec{r} - \vec{r}'|^3} dl',$$ (1)

حيث $\lambda(\vec{r}')$ هي كثافة الشحنة الخطية عند $\vec{r}'$ و $\epsilon_0$ هو ثابت يُسمى السماحية الكهربائية للفراغ.

على عكس الميكانيكا، حيث التعبير البسيط لقانون نيوتن الثاني يخفي تعقيد الحالة، هنا الترميز مخيف. مسألة واحدة على وجه الخصوص يخفيها الترميز عن الطالب المبتدئ هي أنه من أجل حساب الحقل الكهربائي، نحتاج إلى (1) منحنى C يصف مكان الشحنة، و(2) كثافة شحنة λ، وهذا كل شيء.

نظراً لأن المنحنيات مهمة في عدد من الأماكن في النظرية الكهرومغناطيسية، نعرّف نوع بيانات للمنحنيات.

```haskell
data Curve = Curve { curveFunc          :: Double -> Position
                   , startingCurveParam :: Double
                   , endingCurveParam   :: Double }
```

المنحنى (Curve) هو منحنى مُعَلَّم مع معاملات البداية والنهاية. يُعبر عن المنحنى المُعَلَّم هنا من حيث نوع بيانات الموضع (Position)، معرّف بشكل مشابه لـ Vec، لكن بدون عمليات المتجه.

إليك بعض الأمثلة على المنحنيات.

```haskell
circularLoop :: Double -> Curve
circularLoop radius
  = Curve (\t -> cart (radius * cos t)
                      (radius * sin t)
                      0
          ) 0 (2*pi)

line :: Double -> Curve
line l = Curve (\t -> cart 0 0 t) (-l/2) (l/2)
```

الدالة cart تنتج موضعاً (Position) بإعطاء الإحداثيات الديكارتية.

مجهزين بنوع بيانات المنحنى، نحتاج بعد ذلك إلى طريقة للتكامل على منحنى. يمكن أن يكون للتكامل الخطي إما دالة تكامل قياسية أو متجهية (لحساب الحقل الكهربائي، سنستخدم دالة تكامل متجهية، لكن لحساب الجهد الكهربائي، سنستخدم دالة تكامل قياسية).

$$\int_C f(\vec{r}')dl'$$ أو $$\int_C \vec{F}(\vec{r}')dl'$$

نستخدم مترادفات الأنواع لوصف ما هو الحقل القياسي وما هو الحقل المتجهي.

```haskell
type ScalarField = Position -> Double
type VectorField = Position -> Vec
type Field v     = Position -> v
```

الحقل القياسي (ScalarField) هو تخصيص قياس (رقم) لكل موضع في الفضاء. الحقل المتجهي (VectorField) هو تخصيص متجه لكل موضع في الفضاء. نريد أيضاً أن نكون قادرين على الإشارة إلى حقل يمكن أن يكون إما حقلاً قياسياً أو حقلاً متجهياً، لذلك نعرّف Field v.

عادة ما أطلب من الطلاب كتابة مُكامل رقمي بسيط باستخدام قاعدة شبه المنحرف، للحصول على فكرة عما هو مطلوب. ثم، أطلب منهم استخدام شفرة كتبتها للتكامل على منحنى. نستخدم تكاملاً خطياً عام الأغراض بالنوع التالي.

```haskell
simpleLineIntegral
  :: (InnerSpace v, Scalar v ~ Double)
  => Int        -- ^ عدد الفترات
  -> Field v    -- ^ حقل قياسي أو متجهي
  -> Curve      -- ^ المنحنى للتكامل عليه
  -> v          -- ^ نتيجة قياسية أو متجهية
```

يعمل المُكامل من خلال تقطيع المنحنى إلى عدد من الفترات، وتقييم الحقل على كل فترة، وضرب كل قيمة بطول فترتها، والجمع.

الآن يمكننا حساب الحقل الكهربائي (1) لتوزيع شحنة أحادي البُعد.

```haskell
eFieldFromLineCharge
  :: ScalarField  -- ^ كثافة الشحنة الخطية lambda
  -> Curve        -- ^ هندسة الشحنة الخطية
  -> VectorField  -- ^ الحقل الكهربائي (بالفولت/متر)
eFieldFromLineCharge lambda c r
  = k *^ simpleLineIntegral 1000 integrand c
  where
    k = 9e9  -- 1 / (4 * pi * epsilon0)
    integrand r' = lambda r' *^ d ^/ magnitude d ** 3
      where
        d = displacement r' r
```

لاحظ كيف أن الأنواع والدوال من الرتبة العليا هي جانب أساسي من هذا التعريف. الأنواع ScalarField و VectorField هي نفسها دوال، واحدة تُستخدم كإدخال وواحدة تُستخدم كإخراج لدالة eFieldFromLineCharge. نوع Curve، مثل Vec و Position، يُستخدم لتغليف المعلومات التي، من منظور الفيزياء، تنتمي بحق معاً. لاحظ أيضاً كيف يصف توقيع النوع أن كثافة الشحنة λ والمنحنى C هما المدخلات الوحيدة اللازمة لإجراء الحساب.

### 3.2 الحقل المغناطيسي الناتج عن سلك يحمل تياراً

لنأخذ مثال الحقل المغناطيسي الناتج عن سلك يحمل تياراً. سنسمح للسلك بأن يكون من أي شكل، وأن يحمل أي كمية من التيار. نريد حساب الحقل المغناطيسي الناتج عن السلك. الحقل المغناطيسي عند الموضع $\vec{r}$ الناتج عن تيار I يتدفق على طول منحنى C يُعطى بقانون بيوت-سافارت.

$$\vec{B}(\vec{r}) = \frac{\mu_0 I}{4\pi} \int_C \frac{d\vec{l}' \times (\vec{r} - \vec{r}')}{|\vec{r} - \vec{r}'|^3}$$ (2)

لتنفيذ قانون بيوت-سافارت، من المفيد أن يكون لدينا "تكامل خطي متقاطع" عام الأغراض.

$$\int_C \vec{F}(\vec{r}') \times d\vec{l}'$$

```haskell
-- | يحسب التكامل vf x dl على المنحنى.
crossedLineIntegral
  :: Int          -- ^ عدد الفترات
  -> VectorField  -- ^ حقل متجهي
  -> Curve        -- ^ المنحنى للتكامل عليه
  -> Vec          -- ^ نتيجة متجهية
```

هل نحتاج حقاً إلى مُكامل جديد للتكامل الخطي المتقاطع؟ ألا يمكننا كتابة

$$\int_C \vec{F}(\vec{r}') \times d\vec{l}' = \int_C \vec{F}(\vec{r}') \times \hat{t}dl'$$

حيث $\hat{t}$ هو مماس وحدة للمنحنى، واستخدام مُكاملنا السابق، بتطبيق الضرب الاتجاهي في دالة التكامل؟ هذا احتمال، لكنني لم أرد أن أثقل كاهل المستخدم بتوفير متجهات المماس على طول المنحنى. جزء من الدافع للدوال التي تحسب الحقول الكهربائية والمغناطيسية هو إظهار مدى قلة ما هو مطلوب لإجراء الحساب.

إليك تنفيذ لقانون بيوت-سافارت (2).

```haskell
bFieldFromLineCurrent
  :: Current      -- ^ التيار (بالأمبير)
  -> Curve        -- ^ هندسة التيار الخطي
  -> VectorField  -- ^ الحقل المغناطيسي (بالتسلا)
bFieldFromLineCurrent i c r
  = k *^ crossedLineIntegral 1000 integrand c
  where
    k = 1e-7  -- mu0 / (4 * pi)
    integrand r' = (-i) *^ d ^/ magnitude d ** 3
      where
        d = displacement r' r
```

هنا، Current هو مترادف لـ Double.

```haskell
type Current = Double
```

علامة الطرح التي تسبق التيار في دالة التكامل لأن التكامل الخطي المتقاطع ينفذ الضرب الاتجاهي بالترتيب المعاكس لقانون بيوت-سافارت. الحقل المغناطيسي الناتج عن حلقة تيار دائرية هو مسألة رائعة للبحث الرقمي؛ على الرغم من التماثل، فإن الحقل المغناطيسي من حلقة دائرية غير قابل للحساب تحليلياً (باستثناء محور التماثل). أخيراً، لاحظ كيف يُظهر توقيع النوع أن التيار I والمنحنى C هما كل المعلومات اللازمة لحساب الحقل المغناطيسي.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - electromagnetic theory (النظرية الكهرومغناطيسية)
  - electric field (الحقل الكهربائي)
  - magnetic field (الحقل المغناطيسي)
  - charge distribution (توزيع الشحنة)
  - current (التيار)
  - scalar field (الحقل القياسي)
  - vector field (الحقل المتجهي)
  - line integral (التكامل الخطي)
  - curve (منحنى)
  - parametrized curve (منحنى مُعَلَّم)
  - permittivity (السماحية الكهربائية)
  - Biot-Savart law (قانون بيوت-سافارت)
  - cross product (الضرب الاتجاهي)
  - trapezoidal rule (قاعدة شبه المنحرف)
- **Equations:**
  - Electric field equation (1)
  - Biot-Savart law (2)
  - Line integral expressions
- **Citations:** [1]
- **Special handling:**
  - All Haskell code preserved in English
  - Mathematical equations in LaTeX preserved
  - Type signatures maintained
  - Function names kept in English
  - Added Arabic comments in code blocks
  - Physics constants (ε₀, μ₀) maintained in standard notation
  - Units (V/m, Tesla, Amps) kept in English (standard practice)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-Translation Check (Key Paragraphs)

**First paragraph back-translation:**
"One of the types of problems that occur in electromagnetic theory is calculating the electric and magnetic fields resulting from charge and current distributions."

**Key technical paragraph back-translation:**
"Notice how types and higher-order functions are a fundamental aspect of this definition. The types ScalarField and VectorField are themselves functions, one used as input and one used as output of the eFieldFromLineCharge function. The Curve type, like Vec and Position, is used to wrap information that, from a physics perspective, rightfully belongs together. Also note how the type signature describes that charge density λ and curve C are the only inputs necessary to perform the calculation."

**Validation:** Back-translations accurately preserve the technical content and pedagogical intent. The translation maintains the balance between physics concepts and programming constructs.
