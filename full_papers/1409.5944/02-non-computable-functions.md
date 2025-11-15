# Section 2: There are Non-Computable Functions
## القسم 2: توجد دوال غير قابلة للحوسبة

**Section:** non-computable functions
**Translation Quality:** 0.89
**Glossary Terms Used:** function, computable, algorithm, program, proof

---

### English Version

We start with a discussion of computable and non-computable functions.

**Definition:** We use $Q$ to denote all functions from the positive integers to $\{0,1\}$. That is, if $f$ is in $Q$, then for any positive integer $x$, $f(x)$ is either 0 or 1.

Note that since a function in $Q$ is defined on *all* positive integers, the number of functions in $Q$ is infinite.

**Definition:** Define a function $f$ in $Q$ to be *computable* if there is a finite-sized computer program (in Python, for example) that executes on a computer (a MacBook Pro running Snow Leopard, for example) that computes function $f$. That is, given *any* positive integer $x$, the program finishes in finite time and correctly spits out the value $f(x)$.

**Definition:** Let $A$ be the set of functions in $Q$ that are computable.

Note that the number of functions in $A$ is infinite. For example, the function $f(7) = 1$ and $f(x) = 0$ for all $x \neq 7$ is a computable function, and we can create a similar computable function for any positive integer, in place of 7. So, since there are an infinite number of positive integers, there are an infinite number of computable functions.

**Theorem 2.1:** There are functions in $Q$ that are not computable. That is, $A \subset Q$.

**Proof:** In this proof we would like to talk about an *ordering* (or an ordered list) of all functions in $A$, rather than just the *set* $A$. It might seem self-evident that such an ordering should exist, and so one might think we could just assert that it does. But issues of ordering are subtle; there are unsettled questions about which properties are sufficient to guarantee that an ordering exists. So, we want to be careful and fully establish that an ordering of the functions in $A$ does exist.

**An ordering Exists:**
First, choose a computer language and consider a program in that language. Each line in a program has some end-of-line symbol, so we can concatenate the lines together into a single long string. Therefore, we think of a program in that computer language as a single string written using some finite alphabet.

Now, since $A$ consists of the computable functions in $Q$, for each function $f \in A$, there is some computer program $P_f$ (in the chosen computer language) that computes $f$. Program $P_f$ (considered as a single string) has some finite length. We can, conceptually, order the strings representing the programs that compute the functions in $A$ into a list $L$ in *order* of the lengths of the strings. To make the ordering perfectly precise, when there are strings of the same length, we order those strings lexicographically (i.e., the way they would be *alphabetically* ordered in a dictionary). So, each *program* that computes a function in $A$ has a *well-defined* position in $L$. Then, since each function in $A$ is computed by some program in the ordered list $L$, $L$ also defines an ordered list, which we call $L'$, containing all the functions in $A$.

A function $f$ in $A$ might be computed by different computer programs, so $f$ might appear in $L'$ more than once. If that occurs, we could, conceptually, remove all but the *first* occurrence of $f$ in $L'$, resulting in an ordering of the functions in $A$, as desired. We will see that it will not harm anything if $f$ is computed by more than one program in $L$, and hence appears in $L'$ more than once. The only point that will matter is that there is some ordered listing $L'$ of the functions in $A$ that includes every function in $A$.

Let $f_i$ denote the function in $A$ that appears in position $i$ in $L'$; that is, $f_i$ is computed by the $i$'th program in $L$. (Remember that lists $L$ and $T$ are only conceptual; we don't actually build them--we only have to imagine them for the sake of the proof). Next, consider a table $T$ with one column for each positive integer, and one row for each program in $L$; and associate the function $f_i$ with row $i$ of $T$. Then set the value of cell $T(i,x)$ to $f_i(x)$. See Table 1.

**Function $\overline{f}$:**
Next, we define the function $\overline{f}$ from the positive integers to $\{0,1\}$ as $\overline{f}(i) = 1 - f_i(i)$. For example, based on the functions in Table 1, $\overline{f}(1) = 0$; $\overline{f}(2) = 1$; $\overline{f}(3) = 1$; $\overline{f}(4) = 0$; $\overline{f}(5) = 1$.

Note that in the definition of $\overline{f}(i)$, the same integer $i$ is used both to identify the function $f_i$ in $A$, and as the input value to $f_i$ and to $\overline{f}$. Hence the values for $\overline{f}$ are determined from the values along the main *diagonal* of table $T$. Note also that $\overline{f}$ changes 0 to 1, and changes 1 to 0. So, the values of function $\overline{f}$ are the *opposite* of the values along the main diagonal of Table $T$. Clearly, function $\overline{f}$ is in $Q$.

Now we ask: Is $\overline{f}$ a computable function?

The answer is no for the following reason. If $\overline{f}$ were a computable function, then there would be some row $i^*$ in $T$ such that $\overline{f}(x) = f_{i^*}(x)$ for every positive integer $x$. For example, maybe $i^*$ is 57. But $\overline{f}(57) = 1 - f_{57}(57) \neq f_{57}(57)$, so $\overline{f}$ can't be $f_{57}$. More generally, $\overline{f}(i^*) = 1 - f_{i^*}(i^*)$, so $\overline{f}$ and $f_{i^*}$ differ at least for one input value (namely $i^*$), so $\overline{f} \neq f_{i^*}$. Hence, there is no row in $T$ corresponding to $\overline{f}$, and so $\overline{f}$ is not in set $A$. So $\overline{f}$ is *not* computable---it is in $Q$, but not in $A$. ∎

---

### النسخة العربية

نبدأ بمناقشة الدوال القابلة للحوسبة والدوال غير القابلة للحوسبة.

**تعريف:** نستخدم $Q$ للإشارة إلى جميع الدوال من الأعداد الصحيحة الموجبة إلى $\{0,1\}$. أي، إذا كانت $f$ في $Q$، فإنه لأي عدد صحيح موجب $x$، تكون $f(x)$ إما 0 أو 1.

لاحظ أنه بما أن الدالة في $Q$ معرفة على *جميع* الأعداد الصحيحة الموجبة، فإن عدد الدوال في $Q$ لانهائي.

**تعريف:** نعرّف الدالة $f$ في $Q$ بأنها *قابلة للحوسبة* إذا كان هناك برنامج حاسوبي محدود الحجم (في Python، على سبيل المثال) يُنفذ على حاسوب (MacBook Pro يعمل بنظام Snow Leopard، على سبيل المثال) يحسب الدالة $f$. أي، بالنظر إلى *أي* عدد صحيح موجب $x$، ينتهي البرنامج في وقت محدود ويخرج بشكل صحيح القيمة $f(x)$.

**تعريف:** لتكن $A$ مجموعة الدوال في $Q$ التي هي قابلة للحوسبة.

لاحظ أن عدد الدوال في $A$ لانهائي. على سبيل المثال، الدالة $f(7) = 1$ و $f(x) = 0$ لجميع $x \neq 7$ هي دالة قابلة للحوسبة، ويمكننا إنشاء دالة قابلة للحوسبة مماثلة لأي عدد صحيح موجب، بدلاً من 7. لذلك، بما أن هناك عدداً لانهائياً من الأعداد الصحيحة الموجبة، فهناك عدد لانهائي من الدوال القابلة للحوسبة.

**نظرية 2.1:** توجد دوال في $Q$ غير قابلة للحوسبة. أي، $A \subset Q$.

**برهان:** في هذا البرهان نود التحدث عن *ترتيب* (أو قائمة مرتبة) لجميع الدوال في $A$، بدلاً من مجرد *المجموعة* $A$. قد يبدو من البديهي أن مثل هذا الترتيب يجب أن يكون موجوداً، وبالتالي قد يعتقد المرء أنه يمكننا فقط التأكيد على وجوده. لكن مسائل الترتيب دقيقة؛ هناك أسئلة غير محسومة حول الخصائص الكافية لضمان وجود ترتيب. لذلك، نريد أن نكون حذرين وأن نثبت بالكامل أن ترتيباً للدوال في $A$ موجود بالفعل.

**وجود الترتيب:**
أولاً، اختر لغة برمجة وافترض برنامجاً بتلك اللغة. كل سطر في البرنامج له رمز نهاية سطر ما، لذلك يمكننا دمج الأسطر معاً في سلسلة نصية طويلة واحدة. لذلك، نفكر في البرنامج بتلك اللغة البرمجية على أنه سلسلة نصية واحدة مكتوبة باستخدام أبجدية محدودة ما.

الآن، بما أن $A$ تتكون من الدوال القابلة للحوسبة في $Q$، فإنه لكل دالة $f \in A$، هناك برنامج حاسوبي $P_f$ (باللغة البرمجية المختارة) يحسب $f$. البرنامج $P_f$ (المعتبر كسلسلة نصية واحدة) له طول محدود. يمكننا، نظرياً، ترتيب السلاسل النصية التي تمثل البرامج التي تحسب الدوال في $A$ في قائمة $L$ حسب *ترتيب* أطوال السلاسل النصية. لجعل الترتيب دقيقاً تماماً، عندما تكون هناك سلاسل نصية بنفس الطول، نرتب تلك السلاسل النصية معجمياً (أي، بالطريقة التي سيتم بها ترتيبها *أبجدياً* في قاموس). لذلك، كل *برنامج* يحسب دالة في $A$ له موضع *محدد جيداً* في $L$. بعد ذلك، بما أن كل دالة في $A$ يتم حسابها بواسطة برنامج ما في القائمة المرتبة $L$، فإن $L$ تحدد أيضاً قائمة مرتبة، نسميها $L'$، تحتوي على جميع الدوال في $A$.

قد تُحسب الدالة $f$ في $A$ بواسطة برامج حاسوبية مختلفة، لذلك قد تظهر $f$ في $L'$ أكثر من مرة. إذا حدث ذلك، يمكننا، نظرياً، إزالة جميع التكرارات ماعدا *الظهور الأول* لـ $f$ في $L'$، مما ينتج عنه ترتيب للدوال في $A$، كما هو مطلوب. سنرى أنه لن يضر أي شيء إذا تم حساب $f$ بواسطة أكثر من برنامج واحد في $L$، وبالتالي تظهر في $L'$ أكثر من مرة. النقطة الوحيدة التي ستهم هي أن هناك قائمة مرتبة $L'$ للدوال في $A$ تتضمن كل دالة في $A$.

لتكن $f_i$ تشير إلى الدالة في $A$ التي تظهر في الموضع $i$ في $L'$؛ أي، $f_i$ يتم حسابها بواسطة البرنامج رقم $i$ في $L$. (تذكر أن القوائم $L$ و $T$ مفاهيمية فقط؛ نحن لا نبنيها فعلياً--نحتاج فقط إلى تخيلها من أجل البرهان). بعد ذلك، افترض جدولاً $T$ بعمود واحد لكل عدد صحيح موجب، وصف واحد لكل برنامج في $L$؛ وربط الدالة $f_i$ بالصف $i$ من $T$. ثم عيّن قيمة الخلية $T(i,x)$ إلى $f_i(x)$. انظر الجدول 1.

**الدالة $\overline{f}$:**
بعد ذلك، نعرف الدالة $\overline{f}$ من الأعداد الصحيحة الموجبة إلى $\{0,1\}$ على أنها $\overline{f}(i) = 1 - f_i(i)$. على سبيل المثال، بناءً على الدوال في الجدول 1، $\overline{f}(1) = 0$؛ $\overline{f}(2) = 1$؛ $\overline{f}(3) = 1$؛ $\overline{f}(4) = 0$؛ $\overline{f}(5) = 1$.

لاحظ أنه في تعريف $\overline{f}(i)$، يتم استخدام نفس العدد الصحيح $i$ لتحديد الدالة $f_i$ في $A$، وكقيمة مدخلة لـ $f_i$ ولـ $\overline{f}$. وبالتالي يتم تحديد قيم $\overline{f}$ من القيم على طول *القطر* الرئيسي للجدول $T$. لاحظ أيضاً أن $\overline{f}$ تغير 0 إلى 1، وتغير 1 إلى 0. لذلك، قيم الدالة $\overline{f}$ هي *عكس* القيم على طول القطر الرئيسي للجدول $T$. من الواضح أن الدالة $\overline{f}$ موجودة في $Q$.

الآن نسأل: هل $\overline{f}$ دالة قابلة للحوسبة؟

الجواب هو لا للسبب التالي. إذا كانت $\overline{f}$ دالة قابلة للحوسبة، فسيكون هناك صف $i^*$ في $T$ بحيث $\overline{f}(x) = f_{i^*}(x)$ لكل عدد صحيح موجب $x$. على سبيل المثال، ربما $i^*$ هو 57. لكن $\overline{f}(57) = 1 - f_{57}(57) \neq f_{57}(57)$، لذلك لا يمكن أن تكون $\overline{f}$ هي $f_{57}$. بشكل أعم، $\overline{f}(i^*) = 1 - f_{i^*}(i^*)$، لذلك $\overline{f}$ و $f_{i^*}$ تختلفان على الأقل لقيمة مدخلة واحدة (وهي $i^*$)، لذلك $\overline{f} \neq f_{i^*}$. وبالتالي، لا يوجد صف في $T$ يطابق $\overline{f}$، وبالتالي $\overline{f}$ ليست في المجموعة $A$. إذن $\overline{f}$ *ليست* قابلة للحوسبة---هي في $Q$، لكن ليست في $A$. ∎

---

### Translation Notes

- **Figures referenced:** Table 1 (الجدول 1)
- **Key terms introduced:** computable function (دالة قابلة للحوسبة), ordering (ترتيب), lexicographic order (ترتيب معجمي), diagonal (القطر), positive integer (عدد صحيح موجب)
- **Equations:** Multiple mathematical expressions and the main diagonal argument
- **Citations:** 0
- **Special handling:** Mathematical notation preserved in LaTeX format; the diagonal argument is central to the proof

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.88
- Glossary consistency: 0.89
- **Overall section score:** 0.89
