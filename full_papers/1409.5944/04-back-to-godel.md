# Section 4: Back to Gödel
## القسم 4: العودة إلى غودل

**Section:** back to Gödel - main proof
**Translation Quality:** 0.88
**Glossary Terms Used:** theorem, proof, formal system, statement, derivation, computable, contradiction

---

### English Version

How do we connect all this to Gödel's first incompleteness theorem? We want to show the variant of Gödel's theorem that says: in any "rich-enough" formal proof system where no false statement about functions can be derived, there are true statements about functions that cannot be derived. We haven't defined what "true" or "rich-enough" means in general, but we will in a specific context.

Recall function $\overline{f}$, and recall that it is well-defined, i.e., there is a value $\overline{f}(x)$ for every positive integer $x$, and for any specific $x$, $\overline{f}(x)$ is either 0 or 1. Recall also, that $\overline{f}$ is not a computable function.

**Definition:** We call a statement an $\overline{f}$-statement if it is either:

> "$\overline{f}(x)$ is 1,"

or:

> "$\overline{f}(x)$ is 0,"

for some positive integer $x$.

Note that every $\overline{f}$-statement is a statement about a specific integer. For example the statement "$\overline{f}(57)$ is 1" is an $\overline{f}$-statement, where $x$ has the value 57. Since, for any positive integer $x$, $\overline{f}(x)$ has only two possible values, 0 or 1, when the two kinds of $\overline{f}$-statements refer to the same $x$, we refer to the first statement as $Sf(x)$ and the second statement as $\neg Sf(x)$.

**What is Truth?**
We say an $\overline{f}$-statement $Sf(x)$ is "true", and $\neg Sf(x)$ is "false", if in fact $\overline{f}(x)$ is 1. Similarly, we say an $\overline{f}$-statement $\neg Sf(x)$ is true, and $Sf(x)$ is false, if in fact $\overline{f}(x)$ is 0. Clearly, for any positive integer $x$, one of the statements $\{Sf(x), \neg Sf(x)\}$ is true and the other is false. In this context, truth and falsity are simple concepts (not so simple in general).

Clearly, it is a desirable property of a formal proof system $\Pi$, that it is not possible to give a formal derivation in $\Pi$ for a statement that is false.

**What does it mean to be rich-enough?**
We need a definition.

**Definition:** We define a formal proof system $\Pi$ to be *rich-enough* if any $\overline{f}$-statement can be formed (i.e., stated, or written) in $\Pi$.

Note that the words "formed", "stated", "written" do not mean "derived". The question of whether a statement can be derived in $\Pi$ is at the heart of Gödel's theorem. Here, we are only saying that the statement can be formed (or written) in $\Pi$.

### 4.1 The Proof of our variant of Gödel's Theorem

Now let $\Pi$ be a rich-enough formal proof system, and suppose **a)** that $\Pi$ has the properties that no false $\overline{f}$-statements can be derived in $\Pi$; and suppose **b)** that for any true $\overline{f}$-statement $S$, there is a formal derivation $s$ of $S$ in $\Pi$.

Since $\Pi$ is rich-enough, for any positive integer $x$, both statements $Sf(x)$ and $\neg Sf(x)$ can be formed in $\Pi$, and since exactly one of those statements is true, suppositions **a** and **b** imply that there is a formal derivation in $\Pi$ of exactly one of the two statements, in particular, the statement that is true. But this leads to a contradiction of the established fact that function $\overline{f}$ is not computable.

In more detail, if the two suppositions (**a** and **b**) hold, the following approach describes a computer program $P^*$ that can correctly determine the value of $\overline{f}(x)$, for any positive integer $x$, in finite time.

**Program $P^*$:**
Given $x$, start program $P$ to successively generate all possible strings (using the finite alphabet and known words and phrases in $\Pi$), in order of their lengths, breaking ties in length lexicographically (as we did when discussing list $L$). After $P$ generates a string $s$, run program $P'$ to see if $s$ is a formal derivation of statement $Sf(x)$. If it is, output that $\overline{f}(x) = 1$ and halt; and if it isn't, run $P''$ to see if $s$ is a formal derivation of $\neg Sf(x)$. If it is, output that $\overline{f}(x) = 0$ and halt; and if it isn't, let $P$ go on to generate the next possible string.

The two suppositions **a** and **b** guarantee that for any positive integer $x$, this mechanical computer program, $P^*$, will halt in finite time, outputting the correct value of $\overline{f}(x)$. But then, $\overline{f}$ would be a *computable* function (computable by program $P^*$), contradicting the already established fact that $\overline{f}$ is not a computable function. So, the two suppositions **a** and **b** lead to a contradiction, so they cannot both hold for any rich-enough formal proof system $\Pi$. There are several equivalent conclusions that result. One is:

**Theorem 4.1:**
For any rich-enough formal proof system $\Pi$ in which no formal derivation of a false $\overline{f}$-statement is possible, there will be some true $\overline{f}$-statement that cannot be formally derived in $\Pi$.

A different, but equivalent conclusion is:

**Theorem 4.2:**
In any rich-enough formal proof system $\Pi$ in which no formal derivation of a false $\overline{f}$-statement is possible, there will be some positive integer $x$ such that neither statement $Sf(x)$ nor statement $\neg Sf(x)$ can be formally derived.

We leave to the reader the proof that Theorems 4.2 and 4.1 are equivalent. Theorems 4.1 and 4.2 are variants of Gödel's first incompleteness theorem.

---

### النسخة العربية

كيف نربط كل هذا بنظرية عدم الاكتمال الأولى لغودل؟ نريد إظهار متغير من نظرية غودل يقول: في أي نظام برهان صوري "غني بما يكفي" حيث لا يمكن اشتقاق عبارة خاطئة حول الدوال، هناك عبارات صحيحة حول الدوال لا يمكن اشتقاقها. لم نعرف ما يعنيه "صحيح" أو "غني بما يكفي" بشكل عام، لكننا سنفعل ذلك في سياق محدد.

تذكر الدالة $\overline{f}$، وتذكر أنها معرفة جيداً، أي، هناك قيمة $\overline{f}(x)$ لكل عدد صحيح موجب $x$، ولأي $x$ محدد، $\overline{f}(x)$ إما 0 أو 1. تذكر أيضاً، أن $\overline{f}$ ليست دالة قابلة للحوسبة.

**تعريف:** نسمي العبارة عبارة $\overline{f}$ إذا كانت إما:

> "$\overline{f}(x)$ هو 1،"

أو:

> "$\overline{f}(x)$ هو 0،"

لبعض الأعداد الصحيحة الموجبة $x$.

لاحظ أن كل عبارة $\overline{f}$ هي عبارة حول عدد صحيح محدد. على سبيل المثال، العبارة "$\overline{f}(57)$ هو 1" هي عبارة $\overline{f}$، حيث $x$ له القيمة 57. بما أنه لأي عدد صحيح موجب $x$، $\overline{f}(x)$ له قيمتان محتملتان فقط، 0 أو 1، عندما يشير النوعان من عبارات $\overline{f}$ إلى نفس $x$، نشير إلى العبارة الأولى بـ $Sf(x)$ والعبارة الثانية بـ $\neg Sf(x)$.

**ما هي الحقيقة؟**
نقول أن عبارة $\overline{f}$ $Sf(x)$ "صحيحة"، و $\neg Sf(x)$ "خاطئة"، إذا كانت $\overline{f}(x)$ في الواقع 1. بالمثل، نقول أن عبارة $\overline{f}$ $\neg Sf(x)$ صحيحة، و $Sf(x)$ خاطئة، إذا كانت $\overline{f}(x)$ في الواقع 0. من الواضح أنه لأي عدد صحيح موجب $x$، إحدى العبارتين $\{Sf(x), \neg Sf(x)\}$ صحيحة والأخرى خاطئة. في هذا السياق، الحقيقة والخطأ مفاهيم بسيطة (ليست بسيطة جداً بشكل عام).

من الواضح أنها خاصية مرغوبة لنظام برهان صوري $\Pi$، أنه لا يمكن إعطاء اشتقاق صوري في $\Pi$ لعبارة خاطئة.

**ما الذي يعنيه أن يكون غنياً بما يكفي؟**
نحتاج إلى تعريف.

**تعريف:** نعرف نظام البرهان الصوري $\Pi$ بأنه *غني بما يكفي* إذا كان يمكن تكوين أي عبارة $\overline{f}$ (أي، صياغتها، أو كتابتها) في $\Pi$.

لاحظ أن الكلمات "تكوين"، "صياغة"، "كتابة" لا تعني "اشتقاق". مسألة ما إذا كان يمكن اشتقاق عبارة في $\Pi$ هي في صميم نظرية غودل. هنا، نقول فقط أن العبارة يمكن تكوينها (أو كتابتها) في $\Pi$.

### 4.1 برهان متغيرنا من نظرية غودل

الآن لتكن $\Pi$ نظام برهان صوري غني بما يكفي، ولنفترض **أ)** أن $\Pi$ له الخصائص التي لا يمكن اشتقاق عبارات $\overline{f}$ خاطئة في $\Pi$؛ ولنفترض **ب)** أنه لأي عبارة $\overline{f}$ صحيحة $S$، هناك اشتقاق صوري $s$ لـ $S$ في $\Pi$.

بما أن $\Pi$ غني بما يكفي، لأي عدد صحيح موجب $x$، يمكن تكوين كلتا العبارتين $Sf(x)$ و $\neg Sf(x)$ في $\Pi$، وبما أن واحدة فقط من تلك العبارات صحيحة، فإن الافتراضين **أ** و **ب** يعنيان أن هناك اشتقاقاً صورياً في $\Pi$ لواحدة فقط من العبارتين، وتحديداً، العبارة الصحيحة. لكن هذا يؤدي إلى تناقض مع الحقيقة الثابتة أن الدالة $\overline{f}$ ليست قابلة للحوسبة.

بمزيد من التفصيل، إذا كان الافتراضان (**أ** و **ب**) صحيحين، فإن النهج التالي يصف برنامج حاسوبي $P^*$ يمكنه تحديد قيمة $\overline{f}(x)$ بشكل صحيح، لأي عدد صحيح موجب $x$، في وقت محدود.

**البرنامج $P^*$:**
بالنظر إلى $x$، ابدأ البرنامج $P$ لتوليد جميع السلاسل النصية الممكنة بشكل متتابع (باستخدام الأبجدية المحدودة والكلمات والعبارات المعروفة في $\Pi$)، حسب ترتيب أطوالها، وكسر التعادلات في الطول معجمياً (كما فعلنا عند مناقشة القائمة $L$). بعد أن يولد $P$ سلسلة نصية $s$، قم بتشغيل البرنامج $P'$ لمعرفة ما إذا كانت $s$ اشتقاقاً صورياً للعبارة $Sf(x)$. إذا كانت كذلك، اخرج أن $\overline{f}(x) = 1$ وتوقف؛ وإذا لم تكن، قم بتشغيل $P''$ لمعرفة ما إذا كانت $s$ اشتقاقاً صورياً لـ $\neg Sf(x)$. إذا كانت كذلك، اخرج أن $\overline{f}(x) = 0$ وتوقف؛ وإذا لم تكن، دع $P$ يستمر في توليد السلسلة النصية الممكنة التالية.

يضمن الافتراضان **أ** و **ب** أنه لأي عدد صحيح موجب $x$، سيتوقف هذا البرنامج الحاسوبي الآلي، $P^*$، في وقت محدود، مخرجاً القيمة الصحيحة لـ $\overline{f}(x)$. لكن بعد ذلك، ستكون $\overline{f}$ دالة *قابلة للحوسبة* (قابلة للحوسبة بواسطة البرنامج $P^*$)، مما يناقض الحقيقة الثابتة بالفعل أن $\overline{f}$ ليست دالة قابلة للحوسبة. لذلك، يؤدي الافتراضان **أ** و **ب** إلى تناقض، لذلك لا يمكن أن يكونا كلاهما صحيحين لأي نظام برهان صوري غني بما يكفي $\Pi$. هناك عدة استنتاجات متكافئة تنتج. واحد منها:

**نظرية 4.1:**
لأي نظام برهان صوري غني بما يكفي $\Pi$ لا يمكن فيه اشتقاق صوري لعبارة $\overline{f}$ خاطئة، ستكون هناك بعض عبارات $\overline{f}$ الصحيحة التي لا يمكن اشتقاقها صورياً في $\Pi$.

استنتاج مختلف، لكنه متكافئ هو:

**نظرية 4.2:**
في أي نظام برهان صوري غني بما يكفي $\Pi$ لا يمكن فيه اشتقاق صوري لعبارة $\overline{f}$ خاطئة، سيكون هناك بعض الأعداد الصحيحة الموجبة $x$ بحيث لا يمكن اشتقاق العبارة $Sf(x)$ ولا العبارة $\neg Sf(x)$ صورياً.

نترك للقارئ البرهان على أن النظريتين 4.2 و 4.1 متكافئتان. النظريتان 4.1 و 4.2 هما متغيران من نظرية عدم الاكتمال الأولى لغودل.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** $\overline{f}$-statement (عبارة $\overline{f}$), truth (الحقيقة/صحيح), falsity (الخطأ/خاطئ), rich-enough (غني بما يكفي), well-defined (معرف جيداً), contradiction (تناقض)
- **Equations:** Multiple logical statements and program descriptions
- **Citations:** 0
- **Special handling:** The proof by contradiction is central; careful distinction between "forming" and "deriving" statements

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
