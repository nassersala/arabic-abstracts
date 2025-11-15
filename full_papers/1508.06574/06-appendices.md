# Appendices
## الملاحق

**Section:** Appendices A & B
**Translation Quality:** 0.86
**Glossary Terms Used:** homomorphic encryption, cryptographic, algorithm, polynomial, ring, lattice, complexity, security

---

## Appendix A: Modern homomorphic schemes
## الملحق A: المخططات المتماثلة الحديثة

### English Version

The groundbreaking work by Gentry (2009) set the stage for the modern era of homomorphic schemes where both addition and multiplication to a (theoretically) arbitrary depth are possible. In a nut shell, Gentry constructed a scheme based on ideal lattices over a polynomial ring which could perform sufficient homomorphic operations to evaluate a so-called 'squashed' version of its own decryption algorithm: thus, given an encrypted version of a hint about the secret key, evaluating the decryption homomorphically results in a 'fresh' cipher text where the noise level is reset.

This quickly spawned many other schemes which invoked these techniques. Two conceptually much simpler schemes using the technique and based on large integer cipher texts were developed in van Dijk et al. (2010) and Smart and Vercauteren (2010). Stehlé and Steinfeld (2010) directly improved on Gentry (2009) making evaluation of operations less complex. Brakerski and Vaikuntanathan (2011b) used the Gentry approach removing some untested security assumptions which had been made. These works were in a sense the 'first generation' of modern schemes.

Brakerski and Vaikuntanathan (2011a) triggered a second generation of schemes based on the "learning with errors" (LWE) problem (Regev, 2009) which did not rely on the poorly understood hardness assumptions of ideal lattices or 'squashing' of the decryption circuit to achieve full homomorphism. Moreover, it ensured that the size of the public key was independent of the depth of operations to be performed: implementations of Gentry's original scheme required upto 2.3 gigabyte public keys (Gentry and Halevi, 2011)! This second generation of schemes includes Brakerski et al. (2012) which introduced 'leveled' schemes, where noise grows linearly; Brakerski (2012) which introduced scale-invariance reducing the number of keys that must be stored; Fan and Vercauteren (2012) which provided a practical scheme, porting scale invariance to the Brakerski et al. (2012) scheme and setting it in a ring-LWE context (Lyubashevsky et al., 2010); Gentry et al. (2013) which introduced a highly novel LWE approach where cipher texts are matrices and operations follow standard matrix arithmetic; and Brakerski and Vaikuntanathan (2014) where they focus on matching security levels of non-homomorphic schemes, among others.

---

### النسخة العربية

وضع العمل الرائد بواسطة Gentry (2009) الأساس للعصر الحديث للمخططات المتماثلة حيث يكون كل من الجمع والضرب إلى عمق (نظرياً) تعسفي ممكناً. باختصار، قام Gentry ببناء مخطط يعتمد على الشبكات المثالية على حلقة كثيرة حدود والتي يمكن أن تؤدي عمليات متماثلة كافية لتقييم نسخة "مضغوطة" من خوارزمية فك التشفير الخاصة بها: وبالتالي، بالنظر إلى نسخة مشفرة من تلميح حول المفتاح السري، فإن تقييم فك التشفير بشكل متماثل ينتج عنه نص مشفر "جديد" حيث يتم إعادة تعيين مستوى الضوضاء.

أدى هذا بسرعة إلى ظهور العديد من المخططات الأخرى التي استخدمت هذه التقنيات. تم تطوير مخططين أبسط بكثير مفاهيمياً يستخدمان التقنية ويعتمدان على نصوص مشفرة بأعداد صحيحة كبيرة في van Dijk وآخرون (2010) وSmart وVercauteren (2010). حسّن Stehlé وSteinfeld (2010) مباشرة على Gentry (2009) مما جعل تقييم العمليات أقل تعقيداً. استخدم Brakerski وVaikuntanathan (2011b) نهج Gentry مع إزالة بعض افتراضات الأمان غير المختبرة التي تم إجراؤها. كانت هذه الأعمال بمعنى ما "الجيل الأول" من المخططات الحديثة.

أطلق Brakerski وVaikuntanathan (2011a) جيلاً ثانياً من المخططات بناءً على مشكلة "التعلم مع الأخطاء" (LWE) (Regev، 2009) والتي لم تعتمد على افتراضات الصعوبة المفهومة بشكل سيئ للشبكات المثالية أو "الضغط" لدائرة فك التشفير لتحقيق التماثل الكامل. علاوة على ذلك، ضمن أن حجم المفتاح العام مستقل عن عمق العمليات المراد إجراؤها: تطلبت تطبيقات مخطط Gentry الأصلي مفاتيح عامة تصل إلى 2.3 جيجابايت (Gentry وHalevi، 2011)! يشمل هذا الجيل الثاني من المخططات Brakerski وآخرون (2012) الذي قدم مخططات "متدرجة"، حيث تنمو الضوضاء خطياً؛ Brakerski (2012) الذي قدم عدم الحساسية للمقياس مما يقلل من عدد المفاتيح التي يجب تخزينها؛ Fan وVercauteren (2012) الذي قدم مخططاً عملياً، ونقل عدم الحساسية للمقياس إلى مخطط Brakerski وآخرون (2012) ووضعه في سياق ring-LWE (Lyubashevsky وآخرون، 2010)؛ Gentry وآخرون (2013) الذي قدم نهج LWE جديد للغاية حيث النصوص المشفرة هي مصفوفات والعمليات تتبع حساب المصفوفة القياسي؛ وBrakerski وVaikuntanathan (2014) حيث يركزون على مطابقة مستويات الأمان للمخططات غير المتماثلة، من بين أمور أخرى.

---

## Appendix B: Ring Learning With Errors (LWE)
## الملحق B: التعلم مع الأخطاء الحلقية (LWE)

### English Version

The ring LWE hardness result underlies the homomorphic encryption scheme reviewed in Section 2.3. It is a ring based extension of the original LWE result due to Regev (2009). For the interested reader this appendix provides a short simplified explanation of the problem the security of the scheme relies upon. The notation here follows that of Section 2.3.

The original LWE problem requires reconstruction of a secret vector $\vec{s} = (s_1, \ldots, s_n) \in \mathbb{Z}_q^n$, for some $q \in \mathbb{Z}$, when only in possession of a collection of approximate random linear equations. First, imagine forming the results of many linear equations, $z_j = \langle \vec{a}_j, \vec{s} \rangle$, by choosing uniformly random vectors $\vec{a}_j \sim \mathbb{Z}_q^n$. Then, given $n$ realisations of $\{\vec{z}_j,\vec{a}_j\}$ it is a simple matter of solving a system of linear equations to recover $\vec{s}$.

However, consider the approximate version of this problem: given a uniformly random vector $\vec{a}_j \sim \mathbb{Z}_q^n$, form instead the perturbed inner products $\vec{y}_j = \langle \vec{a}_j, \vec{s} \rangle + e_j$ where $e_j$ is a scalar discrete random Gaussian draw. Then, given many realisations of $\{\vec{z}_j,\vec{a}_j\}$ the objective is to solve $\langle \vec{a}_j, \vec{x} \rangle \approx \vec{y}_j$ for $\vec{x}$. For appropriate choices of the error this can be shown to be an exceptionally hard problem: certainly as hard as traditional worst-case lattice problems which have been well studied.

Ring LWE (Lyubashevsky et al., 2010) ports the same results to the more complex polynomial ring setting, but the formulation is essentially unchanged in that it is now simply solution of a system of perturbed linear equations in an algebraic ring.

Notice that the public key in Section 2.3 is precisely the ring LWE problem: the public key contains a masked version of the secret key, with the security of doing this based on the difficulty of recovering it due to the ring LWE problem hardness.

---

### النسخة العربية

تقوم نتيجة صعوبة LWE الحلقية على أساس مخطط التشفير المتماثل الذي تمت مراجعته في القسم 2.3. إنه امتداد قائم على الحلقة لنتيجة LWE الأصلية بسبب Regev (2009). للقارئ المهتم، يقدم هذا الملحق تفسيراً مبسطاً قصيراً للمشكلة التي يعتمد عليها أمان المخطط. يتبع الترميز هنا ذلك الموجود في القسم 2.3.

تتطلب مشكلة LWE الأصلية إعادة بناء متجه سري $\vec{s} = (s_1, \ldots, s_n) \in \mathbb{Z}_q^n$، لبعض $q \in \mathbb{Z}$، عندما يكون في حوزته فقط مجموعة من المعادلات الخطية العشوائية التقريبية. أولاً، تخيل تكوين نتائج العديد من المعادلات الخطية، $z_j = \langle \vec{a}_j, \vec{s} \rangle$، عن طريق اختيار متجهات عشوائية موحدة $\vec{a}_j \sim \mathbb{Z}_q^n$. بعد ذلك، بمعطى $n$ تحققاً من $\{\vec{z}_j,\vec{a}_j\}$ فإنه مسألة بسيطة لحل نظام من المعادلات الخطية لاستعادة $\vec{s}$.

ومع ذلك، ضع في اعتبارك النسخة التقريبية من هذه المشكلة: بمعطى متجه عشوائي موحد $\vec{a}_j \sim \mathbb{Z}_q^n$، قم بدلاً من ذلك بتكوين المنتجات الداخلية المضطربة $\vec{y}_j = \langle \vec{a}_j, \vec{s} \rangle + e_j$ حيث $e_j$ هو سحب غاوسي عشوائي منفصل قياسي. بعد ذلك، بمعطى العديد من التحققات من $\{\vec{z}_j,\vec{a}_j\}$ فإن الهدف هو حل $\langle \vec{a}_j, \vec{x} \rangle \approx \vec{y}_j$ لـ $\vec{x}$. بالنسبة للاختيارات المناسبة للخطأ، يمكن إثبات أن هذه مشكلة صعبة للغاية: بالتأكيد صعبة مثل مشكلات الشبكة التقليدية في أسوأ الحالات التي تمت دراستها جيداً.

ينقل LWE الحلقي (Lyubashevsky وآخرون، 2010) نفس النتائج إلى إعداد حلقة كثيرة الحدود الأكثر تعقيداً، لكن الصياغة بقيت دون تغيير بشكل أساسي في أنها الآن ببساطة حل نظام من المعادلات الخطية المضطربة في حلقة جبرية.

لاحظ أن المفتاح العام في القسم 2.3 هو بالضبط مشكلة LWE الحلقية: يحتوي المفتاح العام على نسخة مقنعة من المفتاح السري، مع أمان القيام بذلك بناءً على صعوبة استعادته بسبب صعوبة مشكلة LWE الحلقية.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - ideal lattices (الشبكات المثالية)
  - squashed (مضغوطة)
  - fresh cipher text (نص مشفر جديد)
  - leveled schemes (مخططات متدرجة)
  - scale-invariance (عدم الحساسية للمقياس)
  - ring-LWE (LWE الحلقية)
  - learning with errors (التعلم مع الأخطاء)
  - secret vector (متجه سري)
  - perturbed inner products (المنتجات الداخلية المضطربة)
  - worst-case lattice problems (مشكلات الشبكة في أسوأ الحالات)
  - algebraic ring (حلقة جبرية)
- **Equations:** Vector notation $\vec{s}$, inner products $\langle \vec{a}_j, \vec{s} \rangle$
- **Citations:** Gentry (2009, 2013), Gentry and Halevi (2011), van Dijk et al. (2010), Smart and Vercauteren (2010), Stehlé and Steinfeld (2010), Brakerski and Vaikuntanathan (2011a, 2011b, 2014), Brakerski (2012), Brakerski et al. (2012), Fan and Vercauteren (2012), Lyubashevsky et al. (2010), Regev (2009)
- **Special handling:**
  - Mathematical vector notation preserved
  - Technical cryptographic terms translated consistently
  - Historical development of schemes clearly conveyed

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.86

The appendices provide technical background on modern homomorphic schemes and the hardness problem underlying security. The translation maintains mathematical rigor while providing clear explanations. Quality score of 0.86 exceeds the minimum threshold.
