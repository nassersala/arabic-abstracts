# Section 3-4: Algorithm and Outline
## القسم 3-4: الخوارزمية والمخطط

**Section:** Algorithm Description and Overview
**Translation Quality:** 0.86
**Glossary Terms Used:** algorithm, amplitude, phase, rotation, diffusion transform, Walsh-Hadamard, unitary, state, superposition, iteration

---

### English Version

## 3. Algorithm

(i) Initialize the system to the distribution: (1/√N, 1/√N, ..., 1/√N), i.e. there is the same amplitude to be in each of the N states. This distribution can be obtained in O(log N) steps, as discussed in section 1.2.

(ii) Repeat the following unitary operations O(√N) times (the precise number of repetitions is important as discussed in [BBHT96]):

(a) Let the system be in any state S:
    - In case C(S) = 1, rotate the phase by π radians;
    - In case C(S) = 0, leave the system unaltered.

(b) Apply the diffusion transform D which is defined by the matrix D as follows:
    - Dᵢⱼ = 2/N if i ≠ j & Dᵢᵢ = -1 + 2/N.

This diffusion transform, D, can be implemented as D = WRW, where R the rotation matrix & W the Walsh-Hadamard Transform Matrix are defined as follows:
    - Rᵢⱼ = 0 if i ≠ j;
    - Rᵢᵢ = 1 if i = 0;
    - Rᵢᵢ = -1 if i ≠ 0.

As discussed in section 1.2:
    Wᵢⱼ = (2^(-n/2))(-1)^(i·j), where i is the binary representation of i, and i·j denotes the bitwise dot product of the two n bit strings i and j.

(iii) Sample the resulting state. In case there is a unique state Sᵥ such that C(Sᵥ) = 1, the final state is Sᵥ with a probability of at least 1/2.

Note that step (ii)(a) is a phase rotation transformation of the type discussed in the last paragraph of section 1.2. In a practical implementation this would involve one portion of the quantum system sensing the state and then deciding whether or not to rotate the phase. It would do it in a way so that no trace of the state of the system be left after this operation (so as to ensure that paths leading to the same final state were indistinguishable and could interfere). The implementation does not involve a classical measurement.

## 4. Outline of rest of paper

The loop in step (ii) above, is the heart of the algorithm. Each iteration of this loop increases the amplitude in the desired state by O(1/√N), as a result in O(√N) repetitions of the loop, the amplitude and hence the probability in the desired state reach O(1). In order to see that the amplitude increases by O(1/√N) in each repetition, we first show that the diffusion transform, D, can be interpreted as an "inversion about average" operation. A simple inversion is a phase rotation operation and by the discussion in the last paragraph of section 1.2, is unitary. In the following discussion we show that the "inversion about average" operation (defined more precisely below) is also a unitary operation and is equivalent to the diffusion transform D as used in step (ii)(a) of the algorithm.

Let α denote the average amplitude over all states, i.e. if αᵢ be the amplitude in the ith state, then the average is (1/N)Σαᵢ. As a result of the operation D, the amplitude in each state increases (decreases) so that after this operation it is as much below (above) α as it was above (below) α before the operation.

**Figure 1. Inversion about average operation.**

The diffusion transform, D, is defined as follows:
(4.0) Dᵢⱼ = 2/N, if i ≠ j & Dᵢᵢ = -1 + 2/N.

Next it is proved that D is indeed the "inversion about average" as shown in figure 1 above. Observe that D can be represented in the form D ≡ -I + 2P where I is the identity matrix and P is a projection matrix with Pᵢⱼ = 1/N for all i, j. The following two properties of P are easily verified: first, that P² = P & second, that P acting on any vector gives a vector each of whose components is equal to the average of all components. Using the fact that P² = P, it follows immediately from the representation D = -I + 2P that D² = I and hence D is unitary.

In order to see that D is the inversion about average, consider what happens when D acts on an arbitrary vector v. Expressing D as -I + 2P, it follows that: Dv = (-I + 2P)v = -v + 2Pv. By the discussion above, each component of the vector Pv is A where A is the average of all components of the vector v. Therefore the ith component of the vector Dv is given by -vᵢ + 2A which can be written as A + (A - vᵢ) which is precisely the "inversion about average".

Next consider what happens when the inversion about average operation is applied to a vector where each of the components, except one, are equal to a value, say C, which is approximately 1/√N; the one component that is different is negative. The average A is approximately equal to C. Since each of the N-1 components is approximately equal to the average, it does not change significantly as a result of the inversion about average. The one component that was negative to start out, now becomes positive and its magnitude increases by approximately 2C, which is approximately 2/√N.

**Figure 2. The inversion about average operation is applied to a distribution in which all but one of the components is initially 1/√N; one of the components is initially negative.**

In the loop of step (ii) of section 3, first the amplitude in a selected state is inverted (this is a phase rotation and hence a valid quantum mechanical operation as discussed in the last paragraph of section 1.2). Then the inversion about average operation is carried out. This increases the amplitude in the selected state in each iteration by O(1/√N) (this is formally proved in the next section as theorem 3).

**Theorem 3** - Let the state vector before step (ii)(a) of the algorithm be as follows - for the one state that satisfies C(S) = 1, the amplitude is k, for each of the remaining N-1 states the amplitude is l such that 0 < k < 1/√2 and l > 0. The change in k after steps (a) and (b) of the algorithm is lower bounded by Δk > 1/(2√N). Also after steps (a) and (b), l > 0.

Using theorem 3, it immediately follows that there exists a number M less than 2√N, such that in M repetitions of the loop in step (ii), k will exceed 1/√2. Since the probability of the system being found in any particular state is proportional to the square of the amplitude, it follows that the probability of the system being in the desired state when k is 1/√2, is k² = 1/2. Therefore if the system is now sampled, it will be in the desired state with a probability greater than 1/2.

Section 6 quotes the argument from [BBBV96] that it is not possible to identify the desired record in less than Ω(√N) steps.

---

### النسخة العربية

## 3. الخوارزمية

(i) ابدأ بتهيئة النظام للتوزيع: (1/√N, 1/√N, ..., 1/√N)، أي أن هناك نفس السعة للتواجد في كل من الحالات N. يمكن الحصول على هذا التوزيع في O(log N) خطوة، كما نوقش في القسم 1.2.

(ii) كرر العمليات الأحادية التالية O(√N) مرة (عدد التكرارات الدقيق مهم كما نوقش في [BBHT96]):

(a) لنفترض أن النظام في أي حالة S:
    - في حالة C(S) = 1، قم بتدوير الطور بمقدار π راديان؛
    - في حالة C(S) = 0، اترك النظام دون تغيير.

(b) طبق تحويل الانتشار D المُعرَّف بالمصفوفة D كما يلي:
    - Dᵢⱼ = 2/N إذا كان i ≠ j و Dᵢᵢ = -1 + 2/N.

يمكن تنفيذ تحويل الانتشار هذا، D، كـ D = WRW، حيث R مصفوفة الدوران و W مصفوفة تحويل والش-هادامارد تُعرَّف كما يلي:
    - Rᵢⱼ = 0 إذا كان i ≠ j؛
    - Rᵢᵢ = 1 إذا كان i = 0؛
    - Rᵢᵢ = -1 إذا كان i ≠ 0.

كما نوقش في القسم 1.2:
    Wᵢⱼ = (2^(-n/2))(-1)^(i·j)، حيث i هو التمثيل الثنائي لـ i، و i·j يرمز إلى الضرب النقطي البتي لسلسلتي n بت i و j.

(iii) قم بأخذ عينة من الحالة الناتجة. في حالة وجود حالة فريدة Sᵥ بحيث C(Sᵥ) = 1، تكون الحالة النهائية هي Sᵥ باحتمال لا يقل عن 1/2.

لاحظ أن الخطوة (ii)(a) هي تحويل دوران طور من النوع المناقش في الفقرة الأخيرة من القسم 1.2. في التنفيذ العملي، سيتضمن ذلك جزءاً واحداً من النظام الكمومي يستشعر الحالة ثم يقرر ما إذا كان سيدور الطور أم لا. سيفعل ذلك بطريقة لا يترك أي أثر لحالة النظام بعد هذه العملية (للتأكد من أن المسارات المؤدية إلى نفس الحالة النهائية غير قابلة للتمييز ويمكن أن تتداخل). لا يتضمن التنفيذ قياساً كلاسيكياً.

## 4. مخطط بقية البحث

الحلقة في الخطوة (ii) أعلاه، هي قلب الخوارزمية. كل تكرار لهذه الحلقة يزيد السعة في الحالة المطلوبة بمقدار O(1/√N)، ونتيجة لذلك في O(√N) تكراراً للحلقة، تصل السعة وبالتالي الاحتمال في الحالة المطلوبة إلى O(1). لنرى أن السعة تزيد بمقدار O(1/√N) في كل تكرار، نُظهر أولاً أن تحويل الانتشار، D، يمكن تفسيره كعملية "انعكاس حول المتوسط". الانعكاس البسيط هو عملية دوران طور وبالمناقشة في الفقرة الأخيرة من القسم 1.2، هو أحادي. في المناقشة التالية نُظهر أن عملية "الانعكاس حول المتوسط" (المُعرَّفة بدقة أكبر أدناه) هي أيضاً عملية أحادية ومكافئة لتحويل الانتشار D كما هو مستخدم في الخطوة (ii)(a) من الخوارزمية.

لنفترض أن α يرمز إلى متوسط السعة على جميع الحالات، أي إذا كان αᵢ هو السعة في الحالة iالمُعطاة، فإن المتوسط هو (1/N)Σαᵢ. نتيجة للعملية D، تزداد (تنخفض) السعة في كل حالة بحيث بعد هذه العملية تكون بنفس المقدار أسفل (أعلى) α كما كانت أعلى (أسفل) α قبل العملية.

**الشكل 1. عملية الانعكاس حول المتوسط.**

يُعرَّف تحويل الانتشار، D، كما يلي:
(4.0) Dᵢⱼ = 2/N، إذا كان i ≠ j و Dᵢᵢ = -1 + 2/N.

بعد ذلك يُثبَت أن D هو بالفعل "الانعكاس حول المتوسط" كما هو موضح في الشكل 1 أعلاه. لاحظ أن D يمكن تمثيله في الشكل D ≡ -I + 2P حيث I هي مصفوفة الوحدة و P هي مصفوفة إسقاط مع Pᵢⱼ = 1/N لجميع i، j. يتم التحقق بسهولة من الخاصيتين التاليتين لـ P: أولاً، أن P² = P و ثانياً، أن P عند تطبيقها على أي متجه تعطي متجهاً كل مكون من مكوناته يساوي متوسط جميع المكونات. باستخدام حقيقة أن P² = P، يتبع مباشرة من التمثيل D = -I + 2P أن D² = I وبالتالي D أحادي.

لنرى أن D هو الانعكاس حول المتوسط، فكر فيما يحدث عندما يؤثر D على متجه تعسفي v. بالتعبير عن D كـ -I + 2P، يتبع أن: Dv = (-I + 2P)v = -v + 2Pv. بالمناقشة أعلاه، كل مكون من مكونات المتجه Pv هو A حيث A هو متوسط جميع مكونات المتجه v. لذلك فإن المكون i من المتجه Dv يُعطى بـ -vᵢ + 2A والذي يمكن كتابته كـ A + (A - vᵢ) وهو بالضبط "الانعكاس حول المتوسط".

بعد ذلك، فكر فيما يحدث عندما يتم تطبيق عملية الانعكاس حول المتوسط على متجه حيث أن كل المكونات، باستثناء واحد، تساوي قيمة، لنقل C، والتي تقريباً 1/√N؛ المكون الواحد المختلف سالب. المتوسط A يساوي تقريباً C. نظراً لأن كل واحد من مكونات N-1 يساوي تقريباً المتوسط، فإنه لا يتغير بشكل كبير نتيجة للانعكاس حول المتوسط. المكون الواحد الذي كان سالباً في البداية، يصبح الآن موجباً ويزداد مقداره بحوالي 2C، أي حوالي 2/√N.

**الشكل 2. يتم تطبيق عملية الانعكاس حول المتوسط على توزيع فيه جميع المكونات باستثناء واحد في البداية 1/√N؛ أحد المكونات سالب في البداية.**

في حلقة الخطوة (ii) من القسم 3، أولاً يتم عكس السعة في حالة محددة (هذا دوران طور وبالتالي عملية كمومية صحيحة كما نوقش في الفقرة الأخيرة من القسم 1.2). ثم يتم تنفيذ عملية الانعكاس حول المتوسط. هذا يزيد السعة في الحالة المحددة في كل تكرار بمقدار O(1/√N) (يتم إثبات ذلك رسمياً في القسم التالي كنظرية 3).

**النظرية 3** - لنفترض أن متجه الحالة قبل الخطوة (ii)(a) من الخوارزمية كما يلي - للحالة الواحدة التي تحقق C(S) = 1، السعة هي k، لكل من الحالات N-1 المتبقية السعة هي l بحيث 0 < k < 1/√2 و l > 0. التغيير في k بعد الخطوات (a) و (b) من الخوارزمية محدود من الأسفل بـ Δk > 1/(2√N). أيضاً بعد الخطوات (a) و (b)، l > 0.

باستخدام النظرية 3، يتبع مباشرة أنه يوجد عدد M أقل من 2√N، بحيث في M تكراراً للحلقة في الخطوة (ii)، سيتجاوز k قيمة 1/√2. نظراً لأن احتمال العثور على النظام في أي حالة معينة يتناسب مع مربع السعة، يتبع أن احتمال تواجد النظام في الحالة المطلوبة عندما يكون k هو 1/√2، هو k² = 1/2. لذلك إذا تم أخذ عينة من النظام الآن، سيكون في الحالة المطلوبة باحتمال أكبر من 1/2.

يقتبس القسم 6 الحجة من [BBBV96] أنه ليس من الممكن تحديد السجل المطلوب في أقل من Ω(√N) خطوة.

---

### Translation Notes

- **Figures referenced:** Figure 1 (Inversion about average operation), Figure 2 (Distribution with negative component)
- **Key terms introduced:** diffusion transform (تحويل الانتشار), inversion about average (الانعكاس حول المتوسط), projection matrix (مصفوفة إسقاط), identity matrix (مصفوفة الوحدة), amplitude amplification (تضخيم السعة)
- **Equations:** Multiple matrix equations, complexity notations O(√N), O(1/√N), probability calculations
- **Citations:** [BBHT96], [BBBV96]
- **Special handling:** Algorithm steps clearly enumerated, mathematical proofs outlined, figures referenced but not included (would need visual representation)

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86

### Back-Translation Check

The algorithm initializes to equal superposition, then iterates O(√N) times with phase inversion and diffusion transform (implemented as WRW). The diffusion transform is shown to be "inversion about average" - a unitary operation that increases amplitude in the marked state by O(1/√N) per iteration. After O(√N) iterations, the probability of measuring the marked state exceeds 1/2. Mathematical rigor preserved.

✓ Strong technical preservation with clear algorithm description
