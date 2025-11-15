# Section 3: Rules for Differentiation
## القسم 3: قواعد التفاضل

**Section:** Rules for Differentiation
**Translation Quality:** 0.86
**Glossary Terms Used:** derivative, linear map, sequential composition, parallel composition, chain rule

---

### English Version

Rules for Differentiation

**3.1 Sequential Composition**

With the shift to linear maps, there is one general chain rule, having a lovely form, namely that the derivative of a composition is a composition of the derivatives [Spivak, 1965, Theorem 2-2]:

**Theorem 1 (compose/"chain" rule)**

$$D(g \circ f) a = D g (f a) \circ D f a$$

If $f :: a \to b$ and $g :: b \to c$, then $D f a :: a \multimap b$, and $D g (f a) :: b \multimap c$, so both sides of this equation have type $a \multimap c$.

Strictly speaking, Theorem 1 is not a compositional recipe for differentiating sequential compositions, i.e., it is not the case $D(g \circ f)$ can be constructed solely from $D g$ and $D f$. Instead, it also needs $f$ itself. Fortunately, there is a simple way to restore compositionality. Instead of constructing just the derivative of a function $f$, suppose we augment $f$ with its derivative:

$$D'_+ :: (a \to b) \to ((a \to b) \times (a \to (a \multimap b))) \text{ -- first try}$$
$$D'_+ f = (f, D f)$$

As desired, this altered specification is compositional:

$$D'_+ (g \circ f) = (g \circ f, D(g \circ f)) \text{ -- definition of } D'_+$$
$$= (g \circ f, \lambda a \to D g (f a) \circ D f a) \text{ -- Theorem 1}$$

Note that $D'_+ (g \circ f)$ is assembled entirely from components of $D'_+ g$ and $D'_+ f$, which is to say from $g$, $D g$, $f$, and $D f$. Writing out $g \circ f$ as $\lambda a \to g (f a)$ underscores that the two parts of $D'_+ (g \circ f) a$ both involve $f a$. Computing these parts independently thus requires redundant work. Moreover, the chain rule itself requires applying a function and its derivative (namely $f$ and $D f$) to the same $a$. Since the chain rule gets applied recursively to nested compositions, this redundant work multiplies greatly, resulting in an impractically expensive algorithm.

Fortunately, this efficiency problem is easily fixed. Instead of pairing $f$ and $D f$, combine them:

$$D_+ :: (a \to b) \to (a \to b \times (a \multimap b)) \text{ -- better!}$$
$$D_+ f a = (f a, D f a)$$

Combining $f$ and $D f$ into a single function in this way enables us to eliminate the redundant computation of $f a$ in $D_+ (g \circ f) a$, as follows:

**Corollary 1.1** (Proved in Appendix C.1) $D_+$ is (efficiently) compositional with respect to $(\circ)$. Specifically,

$$D_+ (g \circ f) a = \text{let } \{(b, f') = D_+ f a; (c, g') = D_+ g b\} \text{ in } (c, g' \circ f')$$

**3.2 Parallel Composition**

The chain rule, telling how to differentiate sequential compositions, gets a lot of attention in calculus classes and in automatic and symbolic differentiation. There are other important ways to combine functions, however, and examining them yields additional helpful tools. Another operation $(\times)$ (pronounced "cross") combines two functions in parallel [Gibbons, 2002]:

$$(\times) :: (a \to c) \to (b \to d) \to (a \times b \to c \times d)$$
$$f \times g = \lambda(a, b) \to (f a, g b)$$

While the derivative of a sequential composition is a sequential composition of derivatives, the derivative of a parallel composition is a parallel composition of the derivatives [Spivak, 1965, variant of Theorem 2-3 (3)]:

**Theorem 2 (cross rule)**

$$D(f \times g) (a, b) = D f a \times D g b$$

If $f :: a \to c$ and $g :: b \to d$, then $D f a :: a \multimap c$ and $D g b :: b \multimap d$, so both sides of this equation have type $a \times b \multimap c \times d$.

Theorem 2 gives us what we need to construct $D_+ (f \times g)$ compositionally:

**Corollary 2.1** (Proved in Appendix C.2) $D_+$ is compositional with respect to $(\times)$. Specifically,

$$D_+ (f \times g) (a, b) = \text{let } \{(c, f') = D_+ f a; (d, g') = D_+ g b\} \text{ in } ((c, d), f' \times g')$$

An important point left implicit in the discussion above is that sequential and parallel composition preserve linearity. This property is what makes it meaningful to use these forms to combine derivatives, i.e., linear maps, as we've done above.

**3.3 Linear Functions**

A function $f$ is said to be linear when it distributes over (preserves the structure of) vector addition and scalar multiplication, i.e.,

$$f(a + a') = f a + f a'$$
$$f(s \cdot a) = s \cdot f a$$

In addition to Theorems 1 and 2, we will want one more broadly useful rule, namely that the derivative of every linear function is itself, everywhere [Spivak, 1965, Theorem 2-3 (2)]:

**Theorem 3 (linear rule)** For all linear functions $f$, $D f a = f$.

This statement may sound surprising at first, but less so when we recall that the $D f a$ is a local linear approximation of $f$ at $a$, so we're simply saying that linear functions are their own perfect linear approximations.

For example, consider the function $id = \lambda a \to a$. Theorem 3 says that $D \, id \, a = id$. When expressed via typical representations of linear maps, this property may be expressed as saying that $D \, id \, a$ is the number one or is an identity matrix (with ones on the diagonal and zeros elsewhere). Likewise, consider the (linear) function $fst (a, b) = a$, for which Theorem 3 says $D \, fst (a, b) = fst$. This property, when expressed via typical representations of linear maps, would appear as saying that $D \, fst \, a$ comprises the partial derivatives one and zero if $a, b :: \mathbb{R}$. More generally, if $a :: \mathbb{R}^m$ and $b :: \mathbb{R}^n$, then the Jacobian matrix representation has shape $m \times (m + n)$ (i.e., $m$ rows and $m + n$ columns) and is formed by the horizontal juxtaposition of an $m \times m$ identity matrix on the left with an $m \times n$ zero matrix on the right. This $m \times (m + n)$ matrix, however, represents $fst :: \mathbb{R}^m \times \mathbb{R}^n \multimap \mathbb{R}^m$. Note how much simpler it is to say $D \, fst (a, b) = fst$, and with no loss of precision!

Given Theorem 3, we can construct $D_+ f$ for all linear $f$:

**Corollary 3.1** For all linear functions $f$, $D_+ f = \lambda a \to (f a, f)$. (Proof: immediate from the $D_+$ definition and Theorem 3.)

---

### النسخة العربية

قواعد التفاضل

**3.1 التركيب المتسلسل**

مع التحول إلى الخرائط الخطية، هناك قاعدة سلسلة عامة واحدة، لها شكل جميل، وهي أن مشتقة تركيب هي تركيب المشتقات [Spivak, 1965, Theorem 2-2]:

**المبرهنة 1 (قاعدة التركيب/"السلسلة")**

$$D(g \circ f) a = D g (f a) \circ D f a$$

إذا كانت $f :: a \to b$ و $g :: b \to c$، فإن $D f a :: a \multimap b$، و $D g (f a) :: b \multimap c$، لذا فإن كلا طرفي هذه المعادلة لهما النوع $a \multimap c$.

بالمعنى الدقيق، المبرهنة 1 ليست وصفة تركيبية لتفاضل التراكيب المتسلسلة، أي أنه ليس الحال أن $D(g \circ f)$ يمكن بناؤه فقط من $D g$ و $D f$. بدلاً من ذلك، يحتاج أيضاً إلى $f$ نفسها. لحسن الحظ، هناك طريقة بسيطة لاستعادة التركيبية. بدلاً من بناء مشتقة دالة $f$ فقط، لنفترض أننا نعزز $f$ بمشتقتها:

$$D'_+ :: (a \to b) \to ((a \to b) \times (a \to (a \multimap b))) \text{ -- محاولة أولى}$$
$$D'_+ f = (f, D f)$$

كما هو مطلوب، هذه المواصفة المعدلة تركيبية:

$$D'_+ (g \circ f) = (g \circ f, D(g \circ f)) \text{ -- تعريف } D'_+$$
$$= (g \circ f, \lambda a \to D g (f a) \circ D f a) \text{ -- المبرهنة 1}$$

لاحظ أن $D'_+ (g \circ f)$ مُجمّع بالكامل من مكونات $D'_+ g$ و $D'_+ f$، أي من $g$ و $D g$ و $f$ و $D f$. كتابة $g \circ f$ كـ $\lambda a \to g (f a)$ تؤكد أن الجزءين من $D'_+ (g \circ f) a$ كلاهما يتضمنان $f a$. وبالتالي فإن حساب هذين الجزءين بشكل مستقل يتطلب عملاً زائداً. علاوة على ذلك، تتطلب قاعدة السلسلة نفسها تطبيق دالة ومشتقتها (وهي $f$ و $D f$) على نفس $a$. نظراً لأن قاعدة السلسلة يتم تطبيقها بشكل متكرر على تراكيب متداخلة، فإن هذا العمل الزائد يتضاعف بشكل كبير، مما ينتج عنه خوارزمية باهظة التكلفة بشكل غير عملي.

لحسن الحظ، يتم إصلاح مشكلة الكفاءة هذه بسهولة. بدلاً من إقران $f$ و $D f$، قم بدمجهما:

$$D_+ :: (a \to b) \to (a \to b \times (a \multimap b)) \text{ -- أفضل!}$$
$$D_+ f a = (f a, D f a)$$

دمج $f$ و $D f$ في دالة واحدة بهذه الطريقة يمكّننا من التخلص من الحساب الزائد لـ $f a$ في $D_+ (g \circ f) a$، على النحو التالي:

**النتيجة 1.1** (مبرهنة في الملحق C.1) $D_+$ تركيبية (بكفاءة) فيما يتعلق بـ $(\circ)$. على وجه التحديد،

$$D_+ (g \circ f) a = \text{let } \{(b, f') = D_+ f a; (c, g') = D_+ g b\} \text{ in } (c, g' \circ f')$$

**3.2 التركيب المتوازي**

تحظى قاعدة السلسلة، التي تخبرنا كيفية تفاضل التراكيب المتسلسلة، بالكثير من الاهتمام في صفوف الحساب التفاضلي وفي التفاضل الآلي والرمزي. ومع ذلك، هناك طرق مهمة أخرى لدمج الدوال، وفحصها ينتج أدوات إضافية مفيدة. عملية أخرى $(\times)$ (تُنطق "cross") تجمع دالتين بالتوازي [Gibbons, 2002]:

$$(\times) :: (a \to c) \to (b \to d) \to (a \times b \to c \times d)$$
$$f \times g = \lambda(a, b) \to (f a, g b)$$

بينما مشتقة تركيب متسلسل هي تركيب متسلسل للمشتقات، فإن مشتقة تركيب متواز هي تركيب متواز للمشتقات [Spivak, 1965, variant of Theorem 2-3 (3)]:

**المبرهنة 2 (قاعدة الضرب المتقاطع)**

$$D(f \times g) (a, b) = D f a \times D g b$$

إذا كانت $f :: a \to c$ و $g :: b \to d$، فإن $D f a :: a \multimap c$ و $D g b :: b \multimap d$، لذا فإن كلا طرفي هذه المعادلة لهما النوع $a \times b \multimap c \times d$.

المبرهنة 2 تعطينا ما نحتاجه لبناء $D_+ (f \times g)$ بشكل تركيبي:

**النتيجة 2.1** (مبرهنة في الملحق C.2) $D_+$ تركيبية فيما يتعلق بـ $(\times)$. على وجه التحديد،

$$D_+ (f \times g) (a, b) = \text{let } \{(c, f') = D_+ f a; (d, g') = D_+ g b\} \text{ in } ((c, d), f' \times g')$$

نقطة مهمة تُركت ضمنية في المناقشة أعلاه هي أن التركيب المتسلسل والمتوازي يحفظان الخطية. هذه الخاصية هي ما يجعل من المنطقي استخدام هذه الأشكال لدمج المشتقات، أي الخرائط الخطية، كما فعلنا أعلاه.

**3.3 الدوال الخطية**

يُقال أن دالة $f$ خطية عندما توزع على (تحفظ بنية) جمع المتجهات والضرب القياسي، أي،

$$f(a + a') = f a + f a'$$
$$f(s \cdot a) = s \cdot f a$$

بالإضافة إلى المبرهنتين 1 و 2، سنريد قاعدة أخرى مفيدة على نطاق واسع، وهي أن مشتقة كل دالة خطية هي نفسها، في كل مكان [Spivak, 1965, Theorem 2-3 (2)]:

**المبرهنة 3 (قاعدة الخطية)** لجميع الدوال الخطية $f$، $D f a = f$.

قد يبدو هذا البيان مفاجئاً في البداية، ولكن أقل عندما نتذكر أن $D f a$ هو تقريب خطي محلي لـ $f$ عند $a$، لذا نقول ببساطة أن الدوال الخطية هي تقريباتها الخطية المثالية الخاصة بها.

على سبيل المثال، ضع في اعتبارك الدالة $id = \lambda a \to a$. تقول المبرهنة 3 أن $D \, id \, a = id$. عند التعبير عنها عبر التمثيلات النموذجية للخرائط الخطية، يمكن التعبير عن هذه الخاصية بالقول إن $D \, id \, a$ هو الرقم واحد أو هو مصفوفة الهوية (مع آحاد على القطر وأصفار في أماكن أخرى). وبالمثل، ضع في اعتبارك الدالة (الخطية) $fst (a, b) = a$، التي تقول المبرهنة 3 من أجلها $D \, fst (a, b) = fst$. هذه الخاصية، عند التعبير عنها عبر التمثيلات النموذجية للخرائط الخطية، ستظهر على أنها تقول إن $D \, fst \, a$ تتكون من المشتقات الجزئية واحد وصفر إذا كانت $a, b :: \mathbb{R}$. بشكل أعم، إذا كانت $a :: \mathbb{R}^m$ و $b :: \mathbb{R}^n$، فإن تمثيل مصفوفة اليعقوبي له شكل $m \times (m + n)$ (أي $m$ صف و $m + n$ عمود) ويتكون من التجاور الأفقي لمصفوفة هوية $m \times m$ على اليسار مع مصفوفة صفرية $m \times n$ على اليمين. ومع ذلك، فإن مصفوفة $m \times (m + n)$ هذه تمثل $fst :: \mathbb{R}^m \times \mathbb{R}^n \multimap \mathbb{R}^m$. لاحظ مدى البساطة في قول $D \, fst (a, b) = fst$، ودون فقدان الدقة!

بالنظر إلى المبرهنة 3، يمكننا بناء $D_+ f$ لجميع $f$ الخطية:

**النتيجة 3.1** لجميع الدوال الخطية $f$، $D_+ f = \lambda a \to (f a, f)$. (البرهان: مباشر من تعريف $D_+$ والمبرهنة 3.)

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:** sequential composition, parallel composition, chain rule, cross rule, linear rule, compositionality, Jacobian matrix, identity matrix
- **Equations:** Multiple theorems and corollaries with formal mathematical statements
- **Citations:** 2 references [Spivak 1965, Gibbons 2002]
- **Special handling:** Three major theorems and three corollaries; Haskell type signatures preserved; mathematical notation in LaTeX

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86

### Back-Translation Validation

Key theorem (Theorem 1):

"مشتقة تركيب هي تركيب المشتقات"

Back-translates to: "The derivative of a composition is a composition of the derivatives"

This accurately captures the essence of the chain rule.
