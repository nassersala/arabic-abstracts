# Section 1: Introduction
## القسم 1: المقدمة

**Section:** Introduction (Background, Search Problems, Quantum Algorithms)
**Translation Quality:** 0.87
**Glossary Terms Used:** quantum computer, algorithm, classical computer, quantum mechanics, factorization, polynomial, database, search, SAT problem, NP-complete, probability, amplitude, superposition, unitary, Walsh-Hadamard transformation, phase

---

### English Version

## 1. Introduction

### 1.0 Background

Quantum mechanical computers were proposed in the early 1980's [Benioff80] and in many respects, shown to be at least as powerful as classical computers - an important but not surprising result, since classical computers, at the deepest level, ultimately follow the laws of quantum mechanics. The description of quantum mechanical computers was formalized in the late 80's and early 90's [Deutsch85] [BB94] [BV93] [Yao93] and they were shown to be more powerful than classical computers on various specialized problems. In early 1994, [Shor94] demonstrated that a quantum mechanical computer could efficiently solve a well-known problem for which there was no known efficient algorithm using classical computers. This is the problem of integer factorization, i.e. finding the factors of a given integer N, in a time which is polynomial in log N.

This paper applies quantum computing to a mundane problem in information processing and presents an algorithm that is significantly faster than any classical algorithm can be. The problem is this: there is an unsorted database containing N items out of which just one item satisfies a given condition - that one item has to be retrieved. Once an item is examined, it is possible to tell whether or not it satisfies the condition in one step. However, there does not exist any sorting on the database that would aid its selection. The most efficient classical algorithm for this is to examine the items in the database one by one. If an item satisfies the required condition stop; if it does not, keep track of this item so that it is not examined again. It is easily seen that this algorithm will need to look at an average of N/2 items before finding the desired item.

### 1.1 Search Problems in Computer Science

Even in theoretical computer science, the typical problem can be looked at as that of examining a number of different possibilities to see which, if any, of them satisfy a given condition. This is analogous to the search problem stated in the summary above, except that usually there exists some structure to the problem, i.e some sorting does exist on the database. Most interesting problems are concerned with the effect of this structure on the speed of the algorithm. For example the SAT problem asks whether it is possible to find any combination of n binary variables that satisfies a certain set of clauses C, the crucial issue in NP-completeness is whether it is possible to solve it in time polynomial in n. In this case there are N=2^n possible combinations which have to be searched for any that satisfy the specified property and the question is whether we can do that in a time which is polynomial in log N, i.e. O(n^k). Thus if it were possible to reduce the number of steps to a finite power of log N (instead of O(√N) as in this paper), it would yield a polynomial time algorithm for NP-complete problems.

In view of the fundamental nature of the search problem in both theoretical and applied computer science, it is natural to ask - how fast can the basic identification problem be solved without assuming anything about the structure of the problem? It is generally assumed that this limit is O(N) since there are N items to be examined and a classical algorithm will clearly take O(N) steps. However, quantum mechanical systems can simultaneously be in multiple Schrodinger cat states and carry out multiple tasks at the same time. This paper presents an O(√N) step algorithm for the search problem.

There is a matching lower bound on how fast the desired item can be identified. [BBBV96] show in their paper that in order to identify the desired element, without any information about the structure of the database, a quantum mechanical system will need at least Ω(√N) steps. Since the number of steps required by the algorithm of this paper is O(√N), it is within a constant factor of the fastest possible quantum mechanical algorithm.

### 1.2 Quantum Mechanical Algorithms

A good starting point to think of quantum mechanical algorithms is probabilistic algorithms [BV93] (e.g. simulated annealing). In these algorithms, instead of having the system in a specified state, it is in a distribution over various states with a certain probability of being in each state. At each step, there is a certain probability of making a transition from one state to another. The evolution of the system is obtained by premultiplying this probability vector (that describes the distribution of probabilities over various states) by a state transition matrix. Knowing the initial distribution and the state transition matrix, it is possible in principle to calculate the distribution at any instant in time.

Just like classical probabilistic algorithms, quantum mechanical algorithms work with a probability distribution over various states. However, unlike classical systems, the probability vector does not completely describe the system. In order to completely describe the system we need the amplitude in each state which is a complex number. The evolution of the system is obtained by premultiplying this amplitude vector (that describes the distribution of amplitudes over various states) by a transition matrix, the entries of which are complex in general. The probabilities in any state are given by the square of the absolute values of the amplitude in that state. It can be shown that in order to conserve probabilities, the state transition matrix has to be unitary [BV93].

The machinery of quantum mechanical algorithms is illustrated by discussing the three operations that are needed in the algorithm of this paper. The first is the creation of a configuration in which the amplitude of the system being in any of the 2^n basic states of the system is equal; the second is the Walsh-Hadamard transformation operation and the third the selective rotation of different states.

A basic operation in quantum computing is that of a "fair coin flip" performed on a single bit whose states are 0 and 1 [Simon94]. This operation is represented by the following matrix: M = (1/√2)[[1, 1], [1, -1]]. A bit in the state 0 is transformed into a superposition in the two states: (1/√2, 1/√2). Similarly a bit in the state 1 is transformed into (1/√2, -1/√2), i.e. the magnitude of the amplitude in each state is 1/√2 but the phase of the amplitude in the state 1 is inverted. The phase does not have an analog in classical probabilistic algorithms. It comes about in quantum mechanics since the amplitudes are in general complex. In a system in which the states are described by n bits (it has 2^n possible states) we can perform the transformation M on each bit independently in sequence thus changing the state of the system. The state transition matrix representing this operation will be of dimension 2^n × 2^n. In case the initial configuration was the configuration with all n bits in the first state, the resultant configuration will have an identical amplitude of 1/√(2^n) in each of the 2^n states. This is a way of creating a distribution with the same amplitude in all 2^n states.

Next consider the case when the starting state is another one of the 2^n states, i.e. a state described by an n bit binary string with some 0s and some 1s. The result of performing the transformation M on each bit will be a superposition of states described by all possible n bit binary strings with amplitude of each state having a magnitude equal to 1/√(2^n) and sign either + or -. To deduce the sign, observe that from the definition of the matrix M, i.e. M = (1/√2)[[1, 1], [1, -1]], the phase of the resulting configuration is changed when a bit that was previously a 1 remains a 1 after the transformation is performed. Hence if x be the n-bit binary string describing the starting state and y the n-bit binary string describing the resulting string, the sign of the amplitude of y is determined by the parity of the bitwise dot product of x and y, i.e. (-1)^(x·y). This transformation is referred to as the Walsh-Hadamard transformation [DJ92]. This operation (or a closely related operation called the Fourier Transformation) is one of the things that makes quantum mechanical algorithms more powerful than classical algorithms and forms the basis for most significant quantum mechanical algorithms.

The third transformation that we will need is the selective rotation of the phase of the amplitude in certain states. The transformation describing this for a 4 state system is of the form: diag(e^(iφ₁), e^(iφ₂), e^(iφ₃), e^(iφ₄)), where φ₁, φ₂, φ₃, φ₄ are arbitrary real numbers and i = √(-1). Note that, unlike the Walsh-Hadamard transformation and other state transition matrices, the probability in each state stays the same since the square of the absolute value of the amplitude in each state stays the same.

---

### النسخة العربية

## 1. المقدمة

### 1.0 الخلفية

تم اقتراح الحواسيب الكمومية في أوائل الثمانينيات [Benioff80] وأُظهر من نواحٍ عديدة أنها على الأقل بنفس قوة الحواسيب الكلاسيكية - وهي نتيجة مهمة لكنها ليست مفاجئة، حيث أن الحواسيب الكلاسيكية، على أعمق مستوى، تتبع في نهاية المطاف قوانين ميكانيكا الكم. تم إضفاء الطابع الرسمي على وصف الحواسيب الكمومية في أواخر الثمانينيات وأوائل التسعينيات [Deutsch85] [BB94] [BV93] [Yao93] وأُظهر أنها أقوى من الحواسيب الكلاسيكية في مشاكل متخصصة مختلفة. في أوائل عام 1994، أثبت [Shor94] أن الحاسوب الكمومي يمكنه حل مشكلة معروفة بكفاءة لم تكن هناك خوارزمية فعّالة معروفة لها باستخدام الحواسيب الكلاسيكية. هذه هي مشكلة تحليل الأعداد الصحيحة إلى عوامل أولية، أي إيجاد عوامل عدد صحيح معطى N، في وقت متعدد الحدود بالنسبة لـ log N.

يطبق هذا البحث الحوسبة الكمومية على مشكلة عادية في معالجة المعلومات ويقدم خوارزمية أسرع بكثير من أي خوارزمية كلاسيكية يمكن أن تكون. المشكلة هي: توجد قاعدة بيانات غير مرتبة تحتوي على N عنصراً، عنصر واحد فقط منها يحقق شرطاً معيناً - يجب استرجاع ذلك العنصر الوحيد. بمجرد فحص عنصر، يمكن معرفة ما إذا كان يحقق الشرط أم لا في خطوة واحدة. ومع ذلك، لا يوجد أي ترتيب على قاعدة البيانات من شأنه أن يساعد في اختياره. الخوارزمية الكلاسيكية الأكثر كفاءة لهذا هي فحص العناصر في قاعدة البيانات واحداً تلو الآخر. إذا حقق عنصر الشرط المطلوب توقف؛ وإذا لم يحققه، احتفظ بتتبع هذا العنصر حتى لا يتم فحصه مرة أخرى. من السهل رؤية أن هذه الخوارزمية ستحتاج إلى النظر في متوسط N/2 عنصراً قبل العثور على العنصر المطلوب.

### 1.1 مشاكل البحث في علوم الحاسوب

حتى في علوم الحاسوب النظرية، يمكن النظر إلى المشكلة النموذجية على أنها فحص عدد من الاحتمالات المختلفة لمعرفة أي منها، إن وُجد، يحقق شرطاً معيناً. هذا مماثل لمشكلة البحث المذكورة في الملخص أعلاه، إلا أنه عادة ما يوجد بعض البنية للمشكلة، أي يوجد بعض الترتيب في قاعدة البيانات. معظم المشاكل المثيرة للاهتمام تتعلق بتأثير هذه البنية على سرعة الخوارزمية. على سبيل المثال، تسأل مشكلة SAT عما إذا كان من الممكن العثور على أي تركيبة من n متغيراً ثنائياً تحقق مجموعة معينة من الشروط C، والقضية الحاسمة في اكتمال NP هي ما إذا كان من الممكن حلها في وقت متعدد الحدود بالنسبة لـ n. في هذه الحالة هناك N=2^n تركيبة محتملة يجب البحث فيها عن أي منها يحقق الخاصية المحددة والسؤال هو ما إذا كان يمكننا القيام بذلك في وقت متعدد الحدود بالنسبة لـ log N، أي O(n^k). لذلك إذا كان من الممكن تقليل عدد الخطوات إلى قوة منتهية من log N (بدلاً من O(√N) كما في هذا البحث)، فسيؤدي ذلك إلى خوارزمية بوقت متعدد الحدود لمشاكل اكتمال NP.

في ضوء الطبيعة الأساسية لمشكلة البحث في كل من علوم الحاسوب النظرية والتطبيقية، من الطبيعي أن نسأل - ما مدى سرعة حل مشكلة التحديد الأساسية دون افتراض أي شيء عن بنية المشكلة؟ يُفترض عموماً أن هذا الحد هو O(N) حيث أن هناك N عنصراً يجب فحصها وستستغرق الخوارزمية الكلاسيكية بوضوح O(N) خطوة. ومع ذلك، يمكن للأنظمة الكمومية أن تكون في وقت واحد في حالات قطة شرودنجر متعددة وتنفيذ مهام متعددة في نفس الوقت. يقدم هذا البحث خوارزمية بـ O(√N) خطوة لمشكلة البحث.

هناك حد أدنى مطابق لمدى سرعة تحديد العنصر المطلوب. يُظهر [BBBV96] في بحثهم أنه من أجل تحديد العنصر المطلوب، دون أي معلومات عن بنية قاعدة البيانات، سيحتاج النظام الكمومي إلى Ω(√N) خطوة على الأقل. نظراً لأن عدد الخطوات المطلوبة بواسطة خوارزمية هذا البحث هو O(√N)، فهي ضمن عامل ثابت من أسرع خوارزمية كمومية ممكنة.

### 1.2 الخوارزميات الكمومية

نقطة انطلاق جيدة للتفكير في الخوارزميات الكمومية هي الخوارزميات الاحتمالية [BV93] (على سبيل المثال، التلدين المحاكى). في هذه الخوارزميات، بدلاً من أن يكون النظام في حالة محددة، يكون في توزيع على حالات مختلفة مع احتمال معين للتواجد في كل حالة. في كل خطوة، هناك احتمال معين للانتقال من حالة إلى أخرى. يتم الحصول على تطور النظام عن طريق الضرب المسبق لمتجه الاحتمال هذا (الذي يصف توزيع الاحتمالات على الحالات المختلفة) بمصفوفة انتقال الحالة. بمعرفة التوزيع الأولي ومصفوفة انتقال الحالة، من الممكن من حيث المبدأ حساب التوزيع في أي لحظة زمنية.

تماماً مثل الخوارزميات الاحتمالية الكلاسيكية، تعمل الخوارزميات الكمومية مع توزيع احتمالي على حالات مختلفة. ومع ذلك، على عكس الأنظمة الكلاسيكية، لا يصف متجه الاحتمال النظام بشكل كامل. لوصف النظام بشكل كامل نحتاج إلى السعة في كل حالة والتي هي عدد مركب. يتم الحصول على تطور النظام عن طريق الضرب المسبق لمتجه السعة هذا (الذي يصف توزيع السعات على الحالات المختلفة) بمصفوفة انتقال، والتي تكون عناصرها مركبة بشكل عام. تُعطى الاحتمالات في أي حالة بمربع القيم المطلقة للسعة في تلك الحالة. يمكن إثبات أنه من أجل الحفاظ على الاحتمالات، يجب أن تكون مصفوفة انتقال الحالة أحادية [BV93].

يتم توضيح آلية الخوارزميات الكمومية من خلال مناقشة العمليات الثلاث المطلوبة في خوارزمية هذا البحث. الأولى هي إنشاء تكوين تكون فيه سعة تواجد النظام في أي من الحالات الأساسية 2^n للنظام متساوية؛ والثانية هي عملية تحويل والش-هادامارد والثالثة الدوران الانتقائي لحالات مختلفة.

عملية أساسية في الحوسبة الكمومية هي عملية "رمي عملة عادلة" يتم إجراؤها على بت واحد حالاته هي 0 و 1 [Simon94]. يتم تمثيل هذه العملية بالمصفوفة التالية: M = (1/√2)[[1, 1], [1, -1]]. يتم تحويل بت في الحالة 0 إلى تراكب في الحالتين: (1/√2, 1/√2). وبالمثل يتم تحويل بت في الحالة 1 إلى (1/√2, -1/√2)، أي أن مقدار السعة في كل حالة هو 1/√2 ولكن طور السعة في الحالة 1 معكوس. الطور ليس له نظير في الخوارزميات الاحتمالية الكلاسيكية. يأتي في ميكانيكا الكم لأن السعات هي بشكل عام أعداد مركبة. في نظام يتم فيه وصف الحالات بـ n بت (له 2^n حالة محتملة) يمكننا تنفيذ التحويل M على كل بت بشكل مستقل بالتسلسل وبالتالي تغيير حالة النظام. ستكون مصفوفة انتقال الحالة التي تمثل هذه العملية ذات بعد 2^n × 2^n. في حالة كان التكوين الأولي هو التكوين الذي تكون فيه جميع البتات n في الحالة الأولى، سيكون للتكوين الناتج سعة متطابقة قدرها 1/√(2^n) في كل من الحالات 2^n. هذه طريقة لإنشاء توزيع بنفس السعة في جميع الحالات 2^n.

بعد ذلك، فكر في الحالة التي تكون فيها الحالة الابتدائية واحدة أخرى من الحالات 2^n، أي حالة موصوفة بسلسلة ثنائية من n بت مع بعض الأصفار وبعض الآحاد. ستكون نتيجة تنفيذ التحويل M على كل بت عبارة عن تراكب حالات موصوفة بجميع سلاسل n بت الثنائية الممكنة مع سعة لكل حالة لها مقدار يساوي 1/√(2^n) وإشارة إما + أو -. لاستنتاج الإشارة، لاحظ أنه من تعريف المصفوفة M، أي M = (1/√2)[[1, 1], [1, -1]]، يتغير طور التكوين الناتج عندما يظل البت الذي كان سابقاً 1 كـ 1 بعد تنفيذ التحويل. وبالتالي إذا كان x هو سلسلة n بت الثنائية التي تصف الحالة الابتدائية و y سلسلة n بت الثنائية التي تصف السلسلة الناتجة، فإن إشارة سعة y تُحدد بواسطة تكافؤ الضرب النقطي البتي لـ x و y، أي (-1)^(x·y). يُشار إلى هذا التحويل باسم تحويل والش-هادامارد [DJ92]. هذه العملية (أو عملية وثيقة الصلة تسمى تحويل فورييه) هي واحدة من الأشياء التي تجعل الخوارزميات الكمومية أقوى من الخوارزميات الكلاسيكية وتشكل الأساس لمعظم الخوارزميات الكمومية المهمة.

التحويل الثالث الذي سنحتاجه هو الدوران الانتقائي لطور السعة في حالات معينة. التحويل الذي يصف هذا لنظام من 4 حالات هو من الشكل: diag(e^(iφ₁), e^(iφ₂), e^(iφ₃), e^(iφ₄))، حيث φ₁، φ₂، φ₃، φ₄ هي أعداد حقيقية تعسفية و i = √(-1). لاحظ أنه، على عكس تحويل والش-هادامارد ومصفوفات انتقال الحالة الأخرى، يظل الاحتمال في كل حالة كما هو حيث أن مربع القيمة المطلقة للسعة في كل حالة يظل كما هو.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** quantum computer (حاسوب كمومي), Shor's algorithm (خوارزمية شور), NP-complete (اكتمال NP), Schrodinger cat states (حالات قطة شرودنجر), amplitude (سعة), unitary matrix (مصفوفة أحادية), Walsh-Hadamard transformation (تحويل والش-هادامارد), phase rotation (دوران الطور)
- **Equations:** Multiple complexity notations (O(N), O(√N), Ω(√N)), matrix definitions, complex numbers
- **Citations:** [Benioff80], [Deutsch85], [BB94], [BV93], [Yao93], [Shor94], [BBBV96], [Simon94], [DJ92]
- **Special handling:** Mathematical notation preserved, complex number notation (i = √(-1)), matrix representations

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-Translation Check

The introduction covers quantum computer background from the 1980s-1990s, explains the unstructured database search problem (O(N) classically vs O(√N) quantum), discusses NP-completeness and SAT problems, compares probabilistic and quantum algorithms, and explains three key quantum operations: equal superposition creation, Walsh-Hadamard transformation, and selective phase rotation. All technical concepts are preserved with appropriate mathematical rigor.

✓ Excellent technical preservation with natural Arabic flow
