# Section 2: Recursive Functions of Symbolic Expressions
## القسم 2: الدوال العودية للتعبيرات الرمزية

**Section:** recursive-functions
**Translation Quality:** 0.88
**Glossary Terms Used:** recursive, function, symbolic, computation, formalism, lambda calculus, computable function, definition

---

### English Version

We shall first define a class of symbolic expressions in terms of ordered pairs and lists. Then we shall define five elementary functions and predicates, and build from these, by composition, conditional expressions, and recursive definitions, an extensive class of functions of symbolic expressions. We shall show that these functions are computable in an automatic sense and discuss their use in computations with symbolic expressions.

**Recursive Function Definitions**

A function is said to be recursively defined if its definition refers to the function being defined. Such definitions are common in mathematics. For example, the factorial function can be defined recursively as:

$$n! = \begin{cases} 1 & \text{if } n = 0 \\ n \times (n-1)! & \text{if } n > 0 \end{cases}$$

The power of recursive definitions lies in their ability to define infinite processes with finite expressions. In traditional programming languages, recursion was often avoided in favor of iteration due to efficiency concerns. However, for symbolic computation and artificial intelligence applications, recursive definitions are more natural and expressive.

**Connection to Lambda Calculus**

The theoretical foundation for our system rests on Church's lambda calculus. In lambda calculus, functions are first-class objects that can be manipulated like any other data. A lambda expression has the form:

$$\lambda[[x]; E]$$

where $x$ is a variable and $E$ is an expression that may contain $x$. This denotes a function of one argument $x$ whose value is computed by evaluating $E$.

For example, $\lambda[[x]; x^2]$ denotes the squaring function. The application of this function to an argument $a$ is written as:

$$(\lambda[[x]; x^2])[a]$$

and evaluates to $a^2$.

**Properties of Recursive Functions**

1. **Composability:** Recursive functions can be combined to form more complex functions.

2. **Termination:** A recursive function must have a base case that does not involve recursion, ensuring termination.

3. **Well-foundedness:** Each recursive call must make progress toward the base case.

4. **Expressive Power:** Recursive functions can express all computable functions (Church-Turing thesis).

**Symbolic vs. Numerical Computation**

Traditional computing focused on numerical computation, where data are numbers and operations are arithmetic. In contrast, symbolic computation deals with arbitrary symbolic expressions that may represent:
- Mathematical formulas
- Logical propositions
- Data structures
- Programs themselves

The key insight of LISP is that both programs and data can be represented uniformly as symbolic expressions, enabling programs that manipulate other programs.

---

### النسخة العربية

سنقوم أولاً بتعريف فئة من التعبيرات الرمزية بدلالة الأزواج المرتبة والقوائم. ثم سنعرف خمس دوال وعبارات شرطية أولية، ونبني منها، عن طريق التركيب والتعبيرات الشرطية والتعريفات العودية، فئة واسعة من دوال التعبيرات الرمزية. سنُظهر أن هذه الدوال قابلة للحوسبة بمعنى آلي ونناقش استخدامها في الحسابات مع التعبيرات الرمزية.

**تعريفات الدوال العودية**

يُقال إن دالة معرفة بشكل عودي إذا كان تعريفها يشير إلى الدالة نفسها التي يتم تعريفها. مثل هذه التعريفات شائعة في الرياضيات. على سبيل المثال، يمكن تعريف دالة المضروب (factorial) بشكل عودي كما يلي:

$$n! = \begin{cases} 1 & \text{إذا كان } n = 0 \\ n \times (n-1)! & \text{إذا كان } n > 0 \end{cases}$$

تكمن قوة التعريفات العودية في قدرتها على تعريف عمليات لا نهائية بتعبيرات منتهية. في لغات البرمجة التقليدية، كان يتم تجنب العودية غالباً لصالح التكرار بسبب مخاوف الكفاءة. ومع ذلك، بالنسبة لتطبيقات الحساب الرمزي والذكاء الاصطناعي، تكون التعريفات العودية أكثر طبيعية وتعبيراً.

**الارتباط بحساب لامبدا**

يستند الأساس النظري لنظامنا على حساب لامبدا لتشرش (Church's lambda calculus). في حساب لامبدا، الدوال هي كائنات من الدرجة الأولى يمكن معالجتها مثل أي بيانات أخرى. تعبير لامبدا له الشكل:

$$\lambda[[x]; E]$$

حيث $x$ هو متغير و $E$ هو تعبير قد يحتوي على $x$. يدل هذا على دالة من معامل واحد $x$ تُحسب قيمتها بتقييم $E$.

على سبيل المثال، $\lambda[[x]; x^2]$ يدل على دالة التربيع. يُكتب تطبيق هذه الدالة على معامل $a$ كما يلي:

$$(\lambda[[x]; x^2])[a]$$

ويتم تقييمه إلى $a^2$.

**خصائص الدوال العودية**

1. **قابلية التركيب (Composability):** يمكن دمج الدوال العودية لتشكيل دوال أكثر تعقيداً.

2. **الإنهاء (Termination):** يجب أن تحتوي الدالة العودية على حالة أساسية لا تتضمن العودية، مما يضمن الإنهاء.

3. **التأسيس الجيد (Well-foundedness):** يجب أن تحرز كل نداء عودي تقدماً نحو الحالة الأساسية.

4. **القوة التعبيرية (Expressive Power):** يمكن للدوال العودية التعبير عن جميع الدوال القابلة للحوسبة (أطروحة تشرش-تورينغ).

**الحساب الرمزي مقابل الحساب العددي**

ركزت الحوسبة التقليدية على الحساب العددي، حيث البيانات أرقام والعمليات حسابية. في المقابل، يتعامل الحساب الرمزي مع تعبيرات رمزية عشوائية قد تمثل:
- الصيغ الرياضية
- القضايا المنطقية
- بنى البيانات
- البرامج نفسها

الفكرة الرئيسية لـ LISP هي أنه يمكن تمثيل كل من البرامج والبيانات بشكل موحد كتعبيرات رمزية، مما يمكّن البرامج التي تعالج برامج أخرى.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** recursive definition, lambda calculus, Church's lambda calculus, symbolic expression, computable function, Church-Turing thesis, base case, termination, composability
- **Equations:** 2 mathematical equations (factorial definition, lambda notation)
- **Citations:** Implicit reference to Church's lambda calculus
- **Special handling:**
  - Lambda notation preserved: $\lambda[[x]; E]$
  - Mathematical equations kept in LaTeX format with Arabic context
  - Technical terms (Composability, Termination, etc.) given in both languages
  - "Church-Turing thesis" translated as "أطروحة تشرش-تورينغ"
  - Factorial example used to illustrate recursion

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.87
- **Overall section score:** 0.88
