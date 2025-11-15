# Section 2: Newtonian Mechanics
## القسم 2: الميكانيكا النيوتونية

**Section:** newtonian-mechanics
**Translation Quality:** 0.86
**Glossary Terms Used:** types, functions, higher-order functions, type classes, data type, state space, vector, differential equation, numerical method, acceleration

---

### English Version

## 2 Newtonian Mechanics

Newton's second law, Fnet = ma, appears deceptively simple. Coupled with the natural tendency in a first physics course to focus on problems that are easily and analytically solvable, the structure of Newtonian mechanics usually gets missed.

We take a state-based approach to Newtonian mechanics. The state of a single particle is given by its position and its velocity (or, equivalently, its momentum). States of rigid bodies (able to rotate) and of multiple particles or bodies require more information. In any case, the state is characterized by a type; initial conditions for the problem are specified by a value of that type.

### 2.1 Vectors

Three-dimensional vectors play a central role in Newtonian mechanics. They are used to describe velocity, acceleration, force, and momentum.

We define a data type for three-dimensional vectors.¹

```haskell
data Vec = Vec { xComp :: Double
               , yComp :: Double
               , zComp :: Double }
```

In the Physics 261 course, we introduce vectors in two stages. In stage 1, we introduce functions that apply only to the Vec data type, giving these operations easily digestible type signatures that clearly express their purpose. These type signatures are shown in Table 1. Some of the operators in Table 1 are provided for convenience; for example we provide a scalar multiplication operator (*^) in which the scalar goes on the left and the vector on the right, as well as an alternative version (^*) in which the arguments are flipped. This redundancy matches the operators in Conal Elliott's vector-space package[1].

Later in the course, around the time we want to write a numerical integrator that can work with both scalars and vectors, we introduce stage 2 in our description of vectors. In stage 2, we keep the Vec data type, but redefine the functions that act on it to belong to type classes from the vector-space package[1] that can accommodate numbers as well as Vecs. The cost of this abstraction is that the type signatures of these functions are now more difficult to read, and require an understanding of type classes. The stage 2 type signatures are shown in Table 2.

¹ Most of the code presented in this paper can be found in the learn-physics package[9].

**Table 1:** Functions for working with vectors, stage 1. In stage 1, all of the functions for working with vectors have concrete types. This makes their type signatures easier for students to read and reason about.

| Function | Description | Type |
|----------|-------------|------|
| (^+^) | vector addition | Vec -> Vec -> Vec |
| (^-^) | vector subtraction | Vec -> Vec -> Vec |
| (*^) | scalar multiplication | Double -> Vec -> Vec |
| (^*) | scalar multiplication | Vec -> Double -> Vec |
| (^/) | scalar division | Vec -> Double -> Vec |
| (<.>) | dot product | Vec -> Vec -> Double |
| (><) | cross product | Vec -> Vec -> Vec |
| magnitude | magnitude | Vec -> Double |
| zeroV | zero vector | Vec |
| iHat | unit vector | Vec |
| negateV | vector negation | Vec -> Vec |
| vec | vector construction | Double -> Double -> Double -> Vec |
| xComp | vector component | Vec -> Double |
| sumV | vector sum | [Vec] -> Vec |

**Table 2:** Functions for working with vectors, stage 2. In stage 2, we want to be able to write code, such as a numerical integrator, that can work with numbers or vectors. The type classes are defined in Conal Elliott's vector-space package[1].

| Function | Description | Type |
|----------|-------------|------|
| (^+^) | vector addition | AdditiveGroup v => v -> v -> v |
| (^-^) | vector subtraction | AdditiveGroup v => v -> v -> v |
| (*^) | scalar multiplication | VectorSpace v => Scalar v -> v -> v |
| (^*) | scalar multiplication | VectorSpace v => v -> Scalar v -> v |
| (^/) | scalar division | (VectorSpace v, Fractional (Scalar v)) => v -> Scalar v -> v |
| (<.>) | dot product | InnerSpace v => v -> v -> Scalar v |
| magnitude | magnitude | (InnerSpace v, Floating (Scalar v)) => v -> Scalar v |
| zeroV | zero vector | AdditiveGroup v => v |
| negateV | vector negation | AdditiveGroup v => v -> v |
| sumV | vector sum | (Foldable f, AdditiveGroup v) => f v -> v |

### 2.2 Single-particle mechanics

The state of a single particle in three dimensions can be specified by giving the particle's position and the particle's velocity. It is convenient to include the current time as part of the state as well; this allows the inclusion of time-dependent forces that may act on the particle. It is also convenient to work with the displacement from some chosen origin, rather than working directly with position, because position is not a vector (it makes no sense to add positions), but displacement is a vector. The state of our system of one particle can then be expressed as follows.

```haskell
type Time         = Double
type Displacement = Vec
type Velocity     = Vec
type State        = (Time, Displacement, Velocity)
```

The state of a particle changes based on the local forces that act on it. We would like to express this idea with a function `Double -> State -> State` that takes a short time interval and updates the state accordingly.

What information is needed to know how to update the state? We need to know the forces that act on the particle; from the net force on the particle and the mass of the particle, Newton's second law allows us to calculate the acceleration of the particle. The key information is contained in what we call an AccelerationFunction.

```haskell
type AccelerationFunction = State -> Vec
```

With an AccelerationFunction, we have specified a system of first-order differential equations; the rate of change of displacement is given by velocity, and the rate of change of velocity is given by acceleration. Using the Euler method to solve the differential equation, we arrive at the following function. (We start with the Euler method because it is the simplest and most intuitive to understand.)

```haskell
eulerStep :: AccelerationFunction -> Double -> State -> State
eulerStep a dt (t,r,v) = (t',r',v')
  where
    t' = t + dt
    r' = r ^+^ v ^* dt
    v' = v ^+^ a(t,r,v) ^* dt
```

To define any particular one-particle problem, we have only to specify the appropriate acceleration function. For a satellite orbiting a fixed Earth, for example, we have the following function to produce the satellite's acceleration from the current state of the satellite.

```haskell
satellite :: AccelerationFunction
satellite (t,r,v) = 6.67e-11 * 5.98e24 / magnitude r ^ 2 *^ u
  where
    u = negateV r ^/ magnitude r
```

Here, the universal gravitational constant and the mass of Earth are expressed numerically in SI units. We see the inverse square law for universal gravity. The unit vector u points from the satellite toward the Earth. (The negation is because the displacement vector r points from the Earth to the satellite.) Notice that while the state consists of time, displacement, and velocity, the force and acceleration in this problem depend only on displacement, and not on time or velocity.

Another one-particle problem is the damped, driven, harmonic oscillator. The particle in this situation is subject to three forces—a spring force, a damping force, and a driving force. An acceleration function for this situation could be written as follows.

```haskell
dampedDrivenOsc :: Double  -- damping constant
                -> Double  -- drive amplitude
                -> Double  -- drive frequency
                -> AccelerationFunction
dampedDrivenOsc beta driveAmp omega (t,r,v)
  = (forceDamp ^+^ forceDrive ^+^ forceSpring) ^/ mass
  where
    forceDamp   = (-beta) *^ v
    forceDrive  = driveAmp * cos (omega * t) *^ iHat
    forceSpring = (-k) *^ r
    mass        = 1
    k           = 1  -- spring constant
```

Here we have decided to commit to numeric values for some of the parameters, such as the mass and spring constant, while passing others as parameters to the function dampedDrivenOsc. Note that the net force for the damped, driven, harmonic oscillator depends on time, displacement, and velocity. The driving force is in the x direction.

We can obtain a solution as an infinite list of State values by iterating the eulerStep function we defined above. Shown here is a related function eulerCromerStep which uses the Euler-Cromer method (see, for example [3]), an improved version of the Euler method.

```haskell
solution :: AccelerationFunction -> Double -> State -> [State]
solution a dt = iterate (eulerCromerStep a dt)

states :: [State]
states = solution (dampedDrivenOsc 0 1 0.7) 0.01
                  (0, vec 1 0 0, vec 0 0 0)
```

Once in possession of a list of States, we can pick out relevant data for plotting or animation. For example, here is a function to form a list of pairs of times and x components of displacement, to make a plot of x vs. t.

```haskell
txPairs :: [State] -> [(Double,Double)]
txPairs sts = [(t, xComp r) | (t,r,v) <- sts]
```

Any single-particle problem in three dimensions can be treated in a similar way. The specification of a particular situation consists in writing an AccelerationFunction, as we did above for satellite motion and for the damped, driven, harmonic oscillator.

### 2.3 Beyond a single-particle state space

We want to study problems in mechanics that go beyond a single particle in three dimensions. For such problems, our first task is to decide on an appropriate type to characterize the state of our system. For a system of multiple particles, one choice is to pair the current time with a list of displacement-velocity pairs (one pair for each particle).

```haskell
type SystemState = (Time, [(Displacement, Velocity)])
```

This type has the advantage that it works for any number of particles (and the disadvantage that Haskell's type system will not warn us if our code erroneously changes the length of the particle list). For the SystemState above, the crucial information needed to update the state is a list of particle accelerations. Taking the place of AccelerationFunction, then, is SystemAccFunc, which provides an acceleration for each of the particles as a function of the system state. We also generalize our eulerStep or eulerCromerStep numerical method to handle the new system state.

```haskell
type SystemAccFunc = SystemState -> [Vec]

eulerCromerSystemStep :: SystemAccFunc -> Double -> SystemState -> SystemState
eulerCromerSystemStep a dt (t,rvs) = (t + dt,rvs')
  where
    as       = a (t,rvs)
    (rs,vs)  = unzip rvs
    rs'      = zipWith (^+^) rs (map (^* dt) vs')
    vs'      = zipWith (^+^) vs (map (^* dt) as)
    rvs'     = zip rs' vs'
```

Using techniques like this, we simulate in the course a system consisting of the Sun, Earth, and Moon mutually interacting by universal gravitation. Increasing the number of particles to about 100, we also model an elastic vibration as a collection of point masses with nearest-neighbor Hooke's-law spring interactions.[2, 4] A physical pendulum is another problem we study, where the state is best expressed with an angle and an angular velocity for the pendulum in its rotation about a fixed pivot.

### 2.4 Uncoupling the numerical solution method

There are many numerical methods that one can use to solve a differential equation. In the exposition above, we have applied the Euler method (or the Euler-Cromer method) in the same function that effectively sets up the differential equation to be solved. This has some advantage for students who have not yet studied differential equations; the Euler method is particularly easy to read and understand.

Nevertheless, it would be conceptually cleaner to separate the construction of the differential equation from its solution with a particular numerical method. Moreover, there is nothing approximate in the construction of the differential equation from the forces that are present in a given physical situation, while numerical solution methods are invariably approximate. In fact, a clean separation can be made. Although we have never had time to address this issue in the course, it is a desirable way to organize our thinking, and extends the theme of exposing the structure of Newtonian mechanics.

We can define a type class StateSpace for data types that can serve as the state of a physical system. This type class is a bit more general than the VectorSpace class, because we want data types for position, which is not a vector, to be able to be part of the state. If state is an instance of StateSpace, there is an associated data type Diff state that represents the vector space of time derivatives of the state space. The StateSpace type class is a modification of the AffineSpace type class[1], in which the scalars of the associated vector space are required to be instances of Fractional.

A differential equation is then simply a function from the state space to its linearization giving the time derivatives of each of the dependent variables in the state.

```haskell
type DifferentialEquation state = state -> Diff state
```

For example, for the single-particle State that we defined earlier, we must specify the time derivatives of time, displacement, and velocity. This is easily done in terms of our AccelerationFunction.

```haskell
oneParticleDiffEq :: AccelerationFunction -> DifferentialEquation State
oneParticleDiffEq a (t, r, v) = (1, v, a(t, r, v))
```

An evolution method is a way of approximating the state after advancing a finite interval in the independent variable (time) from a given state.

```haskell
type EvolutionMethod state
  = DifferentialEquation state  -- ^ differential equation
  -> Scalar (Diff state)        -- ^ time interval
  -> state                      -- ^ initial state
  -> state                      -- ^ evolved state
```

The Euler method is the simplest evolution method.

```haskell
eulerMethod :: StateSpace state => EvolutionMethod state
eulerMethod de dt st = st .+^ de st ^* dt
```

Here the operator (.+^) is borrowed from AffineSpace to represent shifting a point in the state space by a vector from the associated vector space. Other evolution methods, such as a Runge-Kutta method, can now be easily plugged in.

To obtain a full solution, we define two more type synonyms, and a function to form an iterative solution.

```haskell
type InitialValueProblem state = (DifferentialEquation state, state)
type SolutionMethod state = InitialValueProblem state -> [state]

stepSolution :: EvolutionMethod state
             -> Scalar (Diff state)  -- time interval
             -> SolutionMethod state
stepSolution ev dt (de, ic) = iterate (ev de dt) ic
```

An initial value problem is a differential equation along with an initial state. A (numerical) solution method is a way of converting an initial value problem into a list of states (a solution). The infinite list states of state values that we obtained above would now be formed as follows.

```haskell
states' :: [State]
states' = stepSolution eulerMethod 0.01
            ( oneParticleDiffEq (dampedDrivenOsc 0 1 0.7)
            , (0, vec 1 0 0, vec 0 0 0) )
```

### 2.5 Mechanics summary

We summarize our state space view of mechanics by giving a three-step process for analyzing a physical situation.

1. Choose a type to represent the state space for the problem. This involves a choice of which quantities to pay attention to, but it does not require a knowledge of the nature of the forces that are acting.

2. Describe how the state changes in time. Newton's second law (and possibly also Newton's third law) is at the heart of this description.

3. Give an initial state for the system. Now we can make graphs or animations.

---

### النسخة العربية

## 2 الميكانيكا النيوتونية

يبدو قانون نيوتن الثاني، Fnet = ma، بسيطاً بشكل خادع. إلى جانب الميل الطبيعي في مقرر الفيزياء الأول للتركيز على المسائل القابلة للحل بسهولة وتحليلياً، عادة ما تُفقد بنية الميكانيكا النيوتونية.

نتبنى منهجاً قائماً على الحالة للميكانيكا النيوتونية. تُعطى حالة جسيم واحد من خلال موضعه وسرعته (أو، بالمثل، زخمه). تتطلب حالات الأجسام الصلبة (القادرة على الدوران) وحالات الجسيمات أو الأجسام المتعددة مزيداً من المعلومات. في جميع الأحوال، تتميز الحالة بنوع؛ وتُحدد الشروط الأولية للمسألة بقيمة من ذلك النوع.

### 2.1 المتجهات

تلعب المتجهات ثلاثية الأبعاد دوراً محورياً في الميكانيكا النيوتونية. تُستخدم لوصف السرعة، والتسارع، والقوة، والزخم.

نعرّف نوع بيانات للمتجهات ثلاثية الأبعاد.¹

```haskell
data Vec = Vec { xComp :: Double
               , yComp :: Double
               , zComp :: Double }
```

في مقرر الفيزياء 261، نقدم المتجهات على مرحلتين. في المرحلة 1، نقدم دوال تنطبق فقط على نوع البيانات Vec، مما يعطي هذه العمليات توقيعات أنواع سهلة الاستيعاب تعبر بوضوح عن غرضها. توقيعات الأنواع هذه موضحة في الجدول 1. بعض المعاملات في الجدول 1 مُقدمة للراحة؛ على سبيل المثال نوفر معامل ضرب قياسي (*^) حيث يذهب القياس على اليسار والمتجه على اليمين، بالإضافة إلى نسخة بديلة (^*) حيث يتم قلب المعاملات. هذا التكرار يطابق المعاملات في حزمة vector-space لكونال إليوت [1].

في وقت لاحق من المقرر، في الوقت الذي نريد فيه كتابة مُكامل رقمي يمكنه العمل مع كل من القياسات والمتجهات، نقدم المرحلة 2 في وصفنا للمتجهات. في المرحلة 2، نحتفظ بنوع البيانات Vec، لكننا نعيد تعريف الدوال التي تعمل عليه لتنتمي إلى فئات الأنواع من حزمة vector-space [1] التي يمكنها استيعاب الأرقام وكذلك Vecs. تكلفة هذا التجريد هي أن توقيعات الأنواع لهذه الدوال أصبحت الآن أكثر صعوبة في القراءة، وتتطلب فهماً لفئات الأنواع. توقيعات المرحلة 2 موضحة في الجدول 2.

¹ يمكن العثور على معظم الشفرة المقدمة في هذا البحث في حزمة learn-physics [9].

**الجدول 1:** الدوال للعمل مع المتجهات، المرحلة 1. في المرحلة 1، جميع الدوال للعمل مع المتجهات لها أنواع محددة. وهذا يجعل توقيعات أنواعها أسهل للطلاب للقراءة والاستنتاج.

| الدالة | الوصف | النوع |
|----------|-------------|------|
| (^+^) | جمع المتجهات | Vec -> Vec -> Vec |
| (^-^) | طرح المتجهات | Vec -> Vec -> Vec |
| (*^) | الضرب القياسي | Double -> Vec -> Vec |
| (^*) | الضرب القياسي | Vec -> Double -> Vec |
| (^/) | القسمة القياسية | Vec -> Double -> Vec |
| (<.>) | الضرب النقطي | Vec -> Vec -> Double |
| (><) | الضرب الاتجاهي | Vec -> Vec -> Vec |
| magnitude | المقدار | Vec -> Double |
| zeroV | المتجه الصفري | Vec |
| iHat | متجه الوحدة | Vec |
| negateV | نفي المتجه | Vec -> Vec |
| vec | إنشاء متجه | Double -> Double -> Double -> Vec |
| xComp | مكون المتجه | Vec -> Double |
| sumV | مجموع المتجهات | [Vec] -> Vec |

**الجدول 2:** الدوال للعمل مع المتجهات، المرحلة 2. في المرحلة 2، نريد أن نكون قادرين على كتابة شفرة، مثل مُكامل رقمي، يمكنه العمل مع الأرقام أو المتجهات. فئات الأنواع معرّفة في حزمة vector-space لكونال إليوت [1].

| الدالة | الوصف | النوع |
|----------|-------------|------|
| (^+^) | جمع المتجهات | AdditiveGroup v => v -> v -> v |
| (^-^) | طرح المتجهات | AdditiveGroup v => v -> v -> v |
| (*^) | الضرب القياسي | VectorSpace v => Scalar v -> v -> v |
| (^*) | الضرب القياسي | VectorSpace v => v -> Scalar v -> v |
| (^/) | القسمة القياسية | (VectorSpace v, Fractional (Scalar v)) => v -> Scalar v -> v |
| (<.>) | الضرب النقطي | InnerSpace v => v -> v -> Scalar v |
| magnitude | المقدار | (InnerSpace v, Floating (Scalar v)) => v -> Scalar v |
| zeroV | المتجه الصفري | AdditiveGroup v => v |
| negateV | نفي المتجه | AdditiveGroup v => v -> v |
| sumV | مجموع المتجهات | (Foldable f, AdditiveGroup v) => f v -> v |

### 2.2 ميكانيكا الجسيم الواحد

يمكن تحديد حالة جسيم واحد في ثلاثة أبعاد من خلال إعطاء موضع الجسيم وسرعة الجسيم. من المريح تضمين الوقت الحالي كجزء من الحالة أيضاً؛ هذا يسمح بتضمين القوى المعتمدة على الوقت التي قد تؤثر على الجسيم. من المريح أيضاً العمل مع الإزاحة من أصل مختار، بدلاً من العمل مباشرة مع الموضع، لأن الموضع ليس متجهاً (لا معنى لجمع المواضع)، لكن الإزاحة متجه. يمكن بعد ذلك التعبير عن حالة نظامنا لجسيم واحد على النحو التالي.

```haskell
type Time         = Double
type Displacement = Vec
type Velocity     = Vec
type State        = (Time, Displacement, Velocity)
```

تتغير حالة الجسيم بناءً على القوى المحلية التي تؤثر عليه. نود التعبير عن هذه الفكرة بدالة `Double -> State -> State` تأخذ فترة زمنية قصيرة وتُحدث الحالة وفقاً لذلك.

ما هي المعلومات المطلوبة لمعرفة كيفية تحديث الحالة؟ نحتاج إلى معرفة القوى التي تؤثر على الجسيم؛ من القوة الصافية على الجسيم وكتلة الجسيم، يسمح لنا قانون نيوتن الثاني بحساب تسارع الجسيم. المعلومات الرئيسية موجودة فيما نسميه دالة التسارع (AccelerationFunction).

```haskell
type AccelerationFunction = State -> Vec
```

مع دالة التسارع، حددنا نظاماً من المعادلات التفاضلية من الدرجة الأولى؛ معدل تغير الإزاحة يُعطى بالسرعة، ومعدل تغير السرعة يُعطى بالتسارع. باستخدام طريقة أويلر لحل المعادلة التفاضلية، نصل إلى الدالة التالية. (نبدأ بطريقة أويلر لأنها الأبسط والأكثر بديهية للفهم.)

```haskell
eulerStep :: AccelerationFunction -> Double -> State -> State
eulerStep a dt (t,r,v) = (t',r',v')
  where
    t' = t + dt
    r' = r ^+^ v ^* dt
    v' = v ^+^ a(t,r,v) ^* dt
```

لتعريف أي مسألة جسيم واحد معينة، علينا فقط تحديد دالة التسارع المناسبة. بالنسبة لقمر صناعي يدور حول الأرض الثابتة، على سبيل المثال، لدينا الدالة التالية لإنتاج تسارع القمر الصناعي من الحالة الحالية للقمر الصناعي.

```haskell
satellite :: AccelerationFunction
satellite (t,r,v) = 6.67e-11 * 5.98e24 / magnitude r ^ 2 *^ u
  where
    u = negateV r ^/ magnitude r
```

هنا، يتم التعبير عن ثابت الجاذبية العالمي وكتلة الأرض عددياً بوحدات SI. نرى قانون التربيع العكسي للجاذبية العالمية. متجه الوحدة u يشير من القمر الصناعي نحو الأرض. (النفي لأن متجه الإزاحة r يشير من الأرض إلى القمر الصناعي.) لاحظ أنه بينما تتكون الحالة من الوقت والإزاحة والسرعة، تعتمد القوة والتسارع في هذه المسألة على الإزاحة فقط، وليس على الوقت أو السرعة.

مسألة جسيم واحد أخرى هي المذبذب التوافقي المخمد المُدار. الجسيم في هذه الحالة يخضع لثلاث قوى - قوة زنبرك، وقوة تخميد، وقوة إدارة. يمكن كتابة دالة تسارع لهذه الحالة على النحو التالي.

```haskell
dampedDrivenOsc :: Double  -- ثابت التخميد
                -> Double  -- سعة الإدارة
                -> Double  -- تردد الإدارة
                -> AccelerationFunction
dampedDrivenOsc beta driveAmp omega (t,r,v)
  = (forceDamp ^+^ forceDrive ^+^ forceSpring) ^/ mass
  where
    forceDamp   = (-beta) *^ v
    forceDrive  = driveAmp * cos (omega * t) *^ iHat
    forceSpring = (-k) *^ r
    mass        = 1
    k           = 1  -- ثابت الزنبرك
```

هنا قررنا الالتزام بقيم عددية لبعض المعاملات، مثل الكتلة وثابت الزنبرك، بينما نمرر معاملات أخرى كمعاملات للدالة dampedDrivenOsc. لاحظ أن القوة الصافية للمذبذب التوافقي المخمد المُدار تعتمد على الوقت والإزاحة والسرعة. قوة الإدارة في اتجاه x.

يمكننا الحصول على حل كقائمة لانهائية من قيم الحالة (State) من خلال تكرار دالة eulerStep التي عرفناها أعلاه. الموضح هنا هو دالة ذات صلة eulerCromerStep التي تستخدم طريقة أويلر-كرومر (انظر، على سبيل المثال [3])، نسخة محسنة من طريقة أويلر.

```haskell
solution :: AccelerationFunction -> Double -> State -> [State]
solution a dt = iterate (eulerCromerStep a dt)

states :: [State]
states = solution (dampedDrivenOsc 0 1 0.7) 0.01
                  (0, vec 1 0 0, vec 0 0 0)
```

بمجرد امتلاك قائمة من الحالات، يمكننا اختيار البيانات ذات الصلة للرسم أو الرسوم المتحركة. على سبيل المثال، إليك دالة لتشكيل قائمة من أزواج الأوقات ومكونات x للإزاحة، لإنشاء رسم بياني لـ x مقابل t.

```haskell
txPairs :: [State] -> [(Double,Double)]
txPairs sts = [(t, xComp r) | (t,r,v) <- sts]
```

يمكن معالجة أي مسألة جسيم واحد في ثلاثة أبعاد بطريقة مماثلة. يتكون تحديد حالة معينة من كتابة دالة تسارع (AccelerationFunction)، كما فعلنا أعلاه لحركة القمر الصناعي وللمذبذب التوافقي المخمد المُدار.

### 2.3 ما وراء فضاء حالة الجسيم الواحد

نريد دراسة مسائل في الميكانيكا تتجاوز جسيماً واحداً في ثلاثة أبعاد. بالنسبة لهذه المسائل، مهمتنا الأولى هي تحديد نوع مناسب لتوصيف حالة نظامنا. بالنسبة لنظام من جسيمات متعددة، أحد الخيارات هو إقران الوقت الحالي بقائمة من أزواج الإزاحة-السرعة (زوج واحد لكل جسيم).

```haskell
type SystemState = (Time, [(Displacement, Velocity)])
```

لهذا النوع ميزة أنه يعمل مع أي عدد من الجسيمات (وعيب أن نظام أنواع Haskell لن يحذرنا إذا غيرت شفرتنا خطأً طول قائمة الجسيمات). بالنسبة لـ SystemState أعلاه، المعلومات الحاسمة اللازمة لتحديث الحالة هي قائمة بتسارعات الجسيمات. لتحل محل AccelerationFunction، إذن، SystemAccFunc، الذي يوفر تسارعاً لكل من الجسيمات كدالة لحالة النظام. نُعمم أيضاً طريقتنا الرقمية eulerStep أو eulerCromerStep للتعامل مع حالة النظام الجديد.

```haskell
type SystemAccFunc = SystemState -> [Vec]

eulerCromerSystemStep :: SystemAccFunc -> Double -> SystemState -> SystemState
eulerCromerSystemStep a dt (t,rvs) = (t + dt,rvs')
  where
    as       = a (t,rvs)
    (rs,vs)  = unzip rvs
    rs'      = zipWith (^+^) rs (map (^* dt) vs')
    vs'      = zipWith (^+^) vs (map (^* dt) as)
    rvs'     = zip rs' vs'
```

باستخدام تقنيات مثل هذه، نحاكي في المقرر نظاماً يتكون من الشمس والأرض والقمر يتفاعلون بشكل متبادل بالجاذبية العالمية. بزيادة عدد الجسيمات إلى حوالي 100، نمذج أيضاً اهتزازاً مرناً كمجموعة من الكتل النقطية مع تفاعلات زنبرك قانون هوك للجيران الأقرب. [2، 4] البندول الفيزيائي هو مسألة أخرى ندرسها، حيث يتم التعبير عن الحالة بشكل أفضل بزاوية وسرعة زاوية للبندول في دورانه حول محور ثابت.

### 2.4 فك ارتباط طريقة الحل الرقمي

هناك العديد من الطرق الرقمية التي يمكن للمرء استخدامها لحل معادلة تفاضلية. في العرض أعلاه، طبقنا طريقة أويلر (أو طريقة أويلر-كرومر) في نفس الدالة التي تنشئ بشكل فعال المعادلة التفاضلية المراد حلها. لهذا بعض الميزة للطلاب الذين لم يدرسوا بعد المعادلات التفاضلية؛ طريقة أويلر سهلة القراءة والفهم بشكل خاص.

ومع ذلك، سيكون من الأنظف من الناحية المفاهيمية فصل بناء المعادلة التفاضلية عن حلها بطريقة رقمية معينة. علاوة على ذلك، لا يوجد شيء تقريبي في بناء المعادلة التفاضلية من القوى الموجودة في حالة فيزيائية معينة، بينما طرق الحل الرقمية تقريبية دائماً. في الواقع، يمكن إجراء فصل نظيف. على الرغم من أننا لم يكن لدينا وقت لمعالجة هذه القضية في المقرر، إلا أنها طريقة مرغوبة لتنظيم تفكيرنا، وتوسع موضوع كشف بنية الميكانيكا النيوتونية.

يمكننا تعريف فئة نوع StateSpace لأنواع البيانات التي يمكن أن تعمل كحالة لنظام فيزيائي. فئة النوع هذه أكثر عمومية قليلاً من فئة VectorSpace، لأننا نريد أن تكون أنواع البيانات للموضع، وهو ليس متجهاً، قادرة على أن تكون جزءاً من الحالة. إذا كانت الحالة مثيلاً لـ StateSpace، فهناك نوع بيانات مرتبط Diff state يمثل فضاء المتجه للمشتقات الزمنية لفضاء الحالة. فئة النوع StateSpace هي تعديل لفئة النوع AffineSpace [1]، حيث يُطلب أن تكون القياسات من فضاء المتجه المرتبط مثيلات لـ Fractional.

المعادلة التفاضلية هي ببساطة دالة من فضاء الحالة إلى خطيته التي تعطي المشتقات الزمنية لكل من المتغيرات التابعة في الحالة.

```haskell
type DifferentialEquation state = state -> Diff state
```

على سبيل المثال، بالنسبة للحالة (State) للجسيم الواحد التي عرفناها سابقاً، يجب أن نحدد المشتقات الزمنية للوقت والإزاحة والسرعة. يتم ذلك بسهولة من حيث دالة التسارع لدينا.

```haskell
oneParticleDiffEq :: AccelerationFunction -> DifferentialEquation State
oneParticleDiffEq a (t, r, v) = (1, v, a(t, r, v))
```

طريقة التطور هي طريقة لتقريب الحالة بعد التقدم بفاصل زمني محدود في المتغير المستقل (الوقت) من حالة معينة.

```haskell
type EvolutionMethod state
  = DifferentialEquation state  -- ^ المعادلة التفاضلية
  -> Scalar (Diff state)        -- ^ الفاصل الزمني
  -> state                      -- ^ الحالة الأولية
  -> state                      -- ^ الحالة المتطورة
```

طريقة أويلر هي أبسط طريقة تطور.

```haskell
eulerMethod :: StateSpace state => EvolutionMethod state
eulerMethod de dt st = st .+^ de st ^* dt
```

هنا المعامل (.+^) مستعار من AffineSpace لتمثيل إزاحة نقطة في فضاء الحالة بواسطة متجه من فضاء المتجه المرتبط. طرق التطور الأخرى، مثل طريقة رونج-كوتا، يمكن الآن توصيلها بسهولة.

للحصول على حل كامل، نعرّف مترادفي نوع إضافيين، ودالة لتشكيل حل تكراري.

```haskell
type InitialValueProblem state = (DifferentialEquation state, state)
type SolutionMethod state = InitialValueProblem state -> [state]

stepSolution :: EvolutionMethod state
             -> Scalar (Diff state)  -- الفاصل الزمني
             -> SolutionMethod state
stepSolution ev dt (de, ic) = iterate (ev de dt) ic
```

مسألة القيمة الأولية هي معادلة تفاضلية إلى جانب حالة أولية. طريقة الحل (الرقمية) هي طريقة لتحويل مسألة القيمة الأولية إلى قائمة من الحالات (حل). القائمة اللانهائية states من قيم الحالة التي حصلنا عليها أعلاه ستتشكل الآن على النحو التالي.

```haskell
states' :: [State]
states' = stepSolution eulerMethod 0.01
            ( oneParticleDiffEq (dampedDrivenOsc 0 1 0.7)
            , (0, vec 1 0 0, vec 0 0 0) )
```

### 2.5 ملخص الميكانيكا

نلخص رؤيتنا لفضاء الحالة للميكانيكا من خلال إعطاء عملية من ثلاث خطوات لتحليل حالة فيزيائية.

1. اختر نوعاً لتمثيل فضاء الحالة للمسألة. يتضمن هذا اختيار الكميات التي يجب الانتباه إليها، لكنه لا يتطلب معرفة بطبيعة القوى التي تؤثر.

2. صِف كيف تتغير الحالة في الوقت. قانون نيوتن الثاني (وربما أيضاً قانون نيوتن الثالث) هو في صميم هذا الوصف.

3. أعطِ حالة أولية للنظام. الآن يمكننا إنشاء رسوم بيانية أو رسوم متحركة.

---

### Translation Notes

- **Figures referenced:** Table 1, Table 2
- **Key terms introduced:**
  - state-based approach (منهج قائم على الحالة)
  - state space (فضاء الحالة)
  - displacement (إزاحة)
  - velocity (سرعة)
  - acceleration function (دالة التسارع)
  - differential equation (معادلة تفاضلية)
  - Euler method (طريقة أويلر)
  - numerical integrator (مُكامل رقمي)
  - type class (فئة نوع)
  - evolution method (طريقة التطور)
  - initial value problem (مسألة القيمة الأولية)
- **Equations:** Newton's second law (Fnet = ma), gravitational force equation, damped driven oscillator
- **Citations:** [1], [2], [3], [4], [9]
- **Special handling:**
  - All Haskell code preserved in English
  - Mathematical notation preserved
  - Type signatures maintained in original form
  - Function names kept in English (standard practice)
  - Added Arabic comments in code blocks for clarity
  - Physics terminology translated using standard Arabic physics terms
  - SI units maintained in English

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86

### Back-Translation Check (Opening and Closing Paragraphs)

**Opening paragraph back-translation:**
"Newton's second law, Fnet = ma, appears deceptively simple. Alongside the natural tendency in the first physics course to focus on problems that are easily and analytically solvable, the structure of Newtonian mechanics is usually lost. We adopt a state-based approach to Newtonian mechanics. The state of a single particle is given by its position and velocity (or, similarly, its momentum). States of rigid bodies (capable of rotation) and states of multiple particles or bodies require more information. In all cases, the state is characterized by a type; and the initial conditions for the problem are specified by a value of that type."

**Closing paragraph back-translation:**
"We summarize our vision of state space for mechanics by giving a three-step process for analyzing a physical situation. 1. Choose a type to represent the state space for the problem. This includes choosing the quantities to pay attention to, but does not require knowledge of the nature of the acting forces. 2. Describe how the state changes in time. Newton's second law (and perhaps also Newton's third law) is at the core of this description. 3. Give an initial state for the system. Now we can create graphs or animations."

**Validation:** Both back-translations preserve the original meaning with high accuracy. The technical content and pedagogical flow are maintained.
