# Section 2: What's a Derivative?
## القسم 2: ما هي المشتقة؟

**Section:** What's a Derivative?
**Translation Quality:** 0.87
**Glossary Terms Used:** derivative, automatic differentiation, linear map, vector space, Jacobian, Hessian

---

### English Version

What's a Derivative?

Since automatic differentiation (AD) has to do with computing derivatives, let's begin by considering what derivatives are. If your introductory calculus class was like mine, you learned that the derivative $f' x$ of a function $f :: \mathbb{R} \to \mathbb{R}$ at a point $x$ (in the domain of $f$) is a number, defined as follows:

$$f' x = \lim_{\varepsilon \to 0} \frac{f(x + \varepsilon) - f x}{\varepsilon} \tag{1}$$

That is, $f' x$ tells us how fast $f$ is scaling input changes at $x$.

How well does this definition hold up beyond functions of type $\mathbb{R} \to \mathbb{R}$? It will do fine with complex numbers ($\mathbb{C} \to \mathbb{C}$), where division is also defined. Extending to $\mathbb{R} \to \mathbb{R}^n$ also works if we interpret the ratio as dividing a vector (in $\mathbb{R}^n$) by a scalar in the usual way. When we extend to $\mathbb{R}^m \to \mathbb{R}^n$ (or even $\mathbb{R}^m \to \mathbb{R}$), however, this definition no longer makes sense, as it would rely on dividing by a vector $\varepsilon :: \mathbb{R}^m$.

This difficulty of differentiation with non-scalar domains is usually addressed with the notion of "partial derivatives" with respect to the $m$ scalar components of the domain $\mathbb{R}^m$, often written "$\partial f/\partial x_j$" for $j \in \{1, \ldots, m\}$. When the codomain $\mathbb{R}^n$ is also non-scalar (i.e., $n > 1$), we have a matrix $J$ (the Jacobian), with $J_{ij} = \partial f_i/\partial x_j$ for $i \in \{1, \ldots, n\}$, where each $f_i$ projects out the $i$-th scalar value from the result of $f$.

So far, we've seen that the derivative of a function could be a single number (for $\mathbb{R} \to \mathbb{R}$), or a vector (for $\mathbb{R} \to \mathbb{R}^n$), or a matrix (for $\mathbb{R}^m \to \mathbb{R}^n$). Moreover, each of these situations has an accompanying chain rule, which says how to differentiate the composition of two functions. Where the scalar chain rule involves multiplying two scalar derivatives, the vector chain rule involves "multiplying" two matrices $A$ and $B$ (the Jacobians), defined as follows:

$$(A \cdot B)_{ij} = \sum_{k=1}^m A_{ik} \cdot B_{kj}$$

Since one can think of scalars as a special case of vectors, and scalar multiplication as a special case of matrix multiplication, perhaps we've reached the needed generality. When we turn our attention to higher derivatives (which are derivatives of derivatives), however, the situation gets more complicated, and we need yet higher-dimensional representations, with correspondingly more complex chain rules.

Fortunately, there is a single, elegant generalization of differentiation with a correspondingly simple chain rule. First, reword Definition 1 above as follows:

$$\lim_{\varepsilon \to 0} \frac{f(x + \varepsilon) - f x}{\varepsilon} - f' x = 0$$

Equivalently,

$$\lim_{\varepsilon \to 0} \frac{f(x + \varepsilon) - (f x + \varepsilon \cdot f' x)}{\varepsilon} = 0$$

Notice that $f' x$ is used to linearly transform $\varepsilon$. Next, generalize this condition to say that $f' x$ is a linear map such that

$$\lim_{\varepsilon \to 0} \frac{\|f(x + \varepsilon) - (f x + f' x \, \varepsilon)\|}{\|\varepsilon\|} = 0.$$

In other words, $f' x$ is a local linear approximation of $f$ at $x$. When an $f' x$ satisfying this condition exists, it is indeed unique [Spivak, 1965, chapter 2].

The derivative of a function $f :: a \to b$ at some value in $a$ is thus not a number, vector, matrix, or higher-dimensional variant, but rather a linear map (also called "linear transformation") from $a$ to $b$, which we will write as "$a \multimap b$". The numbers, vectors, matrices, etc mentioned above are all different representations of linear maps; and the various forms of "multiplication" appearing in their associated chain rules are all implementations of linear map composition for those representations. Here, $a$ and $b$ must be vector spaces that share a common underlying field. Written as a Haskell-style type signature (but omitting vector space constraints),

$$D :: (a \to b) \to (a \to (a \multimap b))$$

From the type of $D$, it follows that differentiating twice has the following type:

$$D^2 = D \circ D :: (a \to b) \to (a \to (a \multimap a \multimap b))$$

The type $a \multimap a \multimap b$ is a linear map that yields a linear map, which is the curried form of a bilinear map. Likewise, differentiating $k$ times yields a $k$-linear map curried $k - 1$ times. For instance, the Hessian matrix $H$ corresponds to the second derivative of a function $f :: \mathbb{R}^m \to \mathbb{R}$, having $m$ rows and $m$ columns (and satisfying the symmetry condition $H_{i,j} \equiv H_{j,i}$).

---

### النسخة العربية

ما هي المشتقة؟

بما أن التفاضل الآلي (AD) يتعلق بحساب المشتقات، فلنبدأ بالنظر في ماهية المشتقات. إذا كانت صف الحساب التفاضلي التمهيدي الخاص بك مثل صفّي، فقد تعلمت أن مشتقة $f' x$ لدالة $f :: \mathbb{R} \to \mathbb{R}$ عند نقطة $x$ (في مجال $f$) هي عدد، معرّف على النحو التالي:

$$f' x = \lim_{\varepsilon \to 0} \frac{f(x + \varepsilon) - f x}{\varepsilon} \tag{1}$$

أي أن $f' x$ تخبرنا بمدى سرعة تحجيم $f$ لتغيرات المدخلات عند $x$.

إلى أي مدى يصمد هذا التعريف بما يتجاوز الدوال من النوع $\mathbb{R} \to \mathbb{R}$؟ سيعمل بشكل جيد مع الأعداد المركبة ($\mathbb{C} \to \mathbb{C}$)، حيث القسمة معرّفة أيضاً. التوسع إلى $\mathbb{R} \to \mathbb{R}^n$ يعمل أيضاً إذا فسرنا النسبة على أنها قسمة متجه (في $\mathbb{R}^n$) على عدد قياسي بالطريقة المعتادة. عندما نوسّع إلى $\mathbb{R}^m \to \mathbb{R}^n$ (أو حتى $\mathbb{R}^m \to \mathbb{R}$)، ومع ذلك، لم يعد هذا التعريف منطقياً، لأنه سيعتمد على القسمة على متجه $\varepsilon :: \mathbb{R}^m$.

عادةً ما يتم معالجة صعوبة التفاضل مع المجالات غير القياسية بمفهوم "المشتقات الجزئية" فيما يتعلق بالمكونات القياسية الـ $m$ للمجال $\mathbb{R}^m$، وغالباً ما تُكتب "$\partial f/\partial x_j$" لـ $j \in \{1, \ldots, m\}$. عندما يكون المجال المشترك $\mathbb{R}^n$ أيضاً غير قياسي (أي $n > 1$)، يكون لدينا مصفوفة $J$ (اليعقوبي)، مع $J_{ij} = \partial f_i/\partial x_j$ لـ $i \in \{1, \ldots, n\}$، حيث كل $f_i$ تُسقط القيمة القياسية الـ $i$ من نتيجة $f$.

حتى الآن، رأينا أن مشتقة دالة يمكن أن تكون رقماً واحداً (لـ $\mathbb{R} \to \mathbb{R}$)، أو متجهاً (لـ $\mathbb{R} \to \mathbb{R}^n$)، أو مصفوفة (لـ $\mathbb{R}^m \to \mathbb{R}^n$). علاوة على ذلك، كل من هذه الحالات لها قاعدة سلسلة مصاحبة، والتي تخبرنا كيفية تفاضل تركيب دالتين. حيث تتضمن قاعدة السلسلة القياسية ضرب مشتقتين قياسيتين، تتضمن قاعدة السلسلة المتجهة "ضرب" مصفوفتين $A$ و $B$ (اليعقوبيات)، معرّفة على النحو التالي:

$$(A \cdot B)_{ij} = \sum_{k=1}^m A_{ik} \cdot B_{kj}$$

بما أنه يمكن للمرء التفكير في القيم القياسية كحالة خاصة من المتجهات، وضرب القيم القياسية كحالة خاصة من ضرب المصفوفات، فربما وصلنا إلى العمومية المطلوبة. عندما نحول انتباهنا إلى المشتقات الأعلى (وهي مشتقات المشتقات)، ومع ذلك، يصبح الوضع أكثر تعقيداً، ونحتاج إلى تمثيلات ذات أبعاد أعلى، مع قواعد سلسلة أكثر تعقيداً.

لحسن الحظ، هناك تعميم واحد أنيق للتفاضل مع قاعدة سلسلة بسيطة مقابلة. أولاً، أعد صياغة التعريف 1 أعلاه على النحو التالي:

$$\lim_{\varepsilon \to 0} \frac{f(x + \varepsilon) - f x}{\varepsilon} - f' x = 0$$

بشكل مكافئ،

$$\lim_{\varepsilon \to 0} \frac{f(x + \varepsilon) - (f x + \varepsilon \cdot f' x)}{\varepsilon} = 0$$

لاحظ أن $f' x$ تُستخدم لتحويل $\varepsilon$ خطياً. بعد ذلك، عمم هذا الشرط ليقول أن $f' x$ هي خريطة خطية بحيث

$$\lim_{\varepsilon \to 0} \frac{\|f(x + \varepsilon) - (f x + f' x \, \varepsilon)\|}{\|\varepsilon\|} = 0.$$

بعبارة أخرى، $f' x$ هي تقريب خطي محلي لـ $f$ عند $x$. عندما توجد $f' x$ تحقق هذا الشرط، فهي بالفعل فريدة [Spivak, 1965, chapter 2].

وبالتالي، فإن مشتقة دالة $f :: a \to b$ عند قيمة ما في $a$ ليست رقماً أو متجهاً أو مصفوفة أو متغيراً ذا أبعاد أعلى، بل هي خريطة خطية (تسمى أيضاً "تحويل خطي") من $a$ إلى $b$، والتي سنكتبها على أنها "$a \multimap b$". الأرقام والمتجهات والمصفوفات وغيرها المذكورة أعلاه هي جميعها تمثيلات مختلفة للخرائط الخطية؛ والأشكال المختلفة من "الضرب" التي تظهر في قواعد السلسلة المرتبطة بها هي جميعها تنفيذات لتركيب الخرائط الخطية لتلك التمثيلات. هنا، يجب أن تكون $a$ و $b$ فضاءات متجهة تشترك في حقل أساسي مشترك. مكتوبة كتوقيع نوع بأسلوب Haskell (لكن مع حذف قيود الفضاء المتجه)،

$$D :: (a \to b) \to (a \to (a \multimap b))$$

من نوع $D$، يتبع أن التفاضل مرتين له النوع التالي:

$$D^2 = D \circ D :: (a \to b) \to (a \to (a \multimap a \multimap b))$$

النوع $a \multimap a \multimap b$ هو خريطة خطية تنتج خريطة خطية، وهو الشكل المكرر لخريطة ثنائية الخطية. وبالمثل، التفاضل $k$ مرات ينتج خريطة $k$-خطية مكررة $k - 1$ مرة. على سبيل المثال، مصفوفة هيسيان $H$ تتوافق مع المشتقة الثانية لدالة $f :: \mathbb{R}^m \to \mathbb{R}$، التي لها $m$ صف و $m$ عمود (وتحقق شرط التناظر $H_{i,j} \equiv H_{j,i}$).

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:** derivative, linear map, Jacobian matrix, Hessian matrix, partial derivatives, bilinear map, vector space
- **Equations:** 7 major equations including the limit definition of derivative, matrix multiplication, and generalized derivative
- **Citations:** 1 reference [Spivak, 1965]
- **Special handling:** Mathematical notation preserved in LaTeX format; type signatures in Haskell notation kept; the linear map arrow symbol "$\multimap$" used to distinguish from function arrow "$\to$"

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-Translation Validation

Key paragraph (final paragraph about derivatives as linear maps):

"وبالتالي، فإن مشتقة دالة $f :: a \to b$ عند قيمة ما في $a$ ليست رقماً أو متجهاً... بل هي خريطة خطية..."

Back-translates to: "Thus, the derivative of a function $f :: a \to b$ at some value in $a$ is not a number, vector, or matrix, but rather is a linear map (also called 'linear transformation') from $a$ to $b$..."

This accurately preserves the key insight that derivatives are fundamentally linear maps rather than just numbers or matrices.
