# Section 3: Current Methods
## القسم 3: الأساليب الحالية

**Section:** Current Methods (Encrypted Statistics, Implementations)
**Translation Quality:** 0.88
**Glossary Terms Used:** homomorphic encryption, machine learning, statistical, algorithm, implementation, cryptographic, binary, classification, regression, library, software

---

### English Version

There are two aspects which, from the perspective of a statistician, are important to review: prior work on encrypted statistics algorithms and existing software implementations for making use of homomorphic encryption schemes.

In this section, both aspects are surveyed before the software tools documented in this paper are covered in Section 4.

## 3.1 Encrypted statistics

In the recent years, some work has emerged on statistical methods for homomorphically encrypted data.

Graepel et al. (2012) proposed algorithms for binary classification, namely secure versions of the Linear Means and Fisher's Linear Discriminant classifiers. The algorithms are rewritten in such a way that divisions are avoided but the original score function (needed for classification) is computable up to a constant. Because some operations have no counterpart in the encryption framework (like division and comparison), some of the computation is done offline by the client after decrypting results returned by the cloud. For instance, in binary classification $y \in \{-1, 1\}$ with Linear Means, the class label is computed in this way as the sign of a score function. To represent real numbers as integers, the authors propose a rescaling approach which approximates real numbers with rational numbers (integer numerator and denominator) and then clears denominators by multiplying all numbers by an appropriate factor and rounding the result to the nearest integer. Approximation accuracy can be controlled in this way.

Wu and Haven (2012) extended previous work on encrypted statistics (Lauter et al., 2011), namely the computation of mean and covariance in a multivariate scenario, using the same technique of returning separate encrypted numerators and denominators. Additionally, they also mention the possibility of implementing (and indeed implement) low-dimension linear regression ($d \leq 5$) by using Cramer's rule to invert the matrix $X^T X$ which is required to obtain the ordinary least squares estimates of the regression parameters $\hat{\beta} = (X^T X)^{-1}X^T Y$. Because Cramer's rule also involves a division by the determinant of $X^T X$, the computation can not be completely performed homomorphically and must be finished offline by the client who assembles the division factors post-decryption. Apart from the computational issues caused by division, there are additional problems here, the most important being the complexity of Cramer's rule: for a problem with dimension $d$, the computation of the determinant has multiplicative depth $d - 1$ and requires $O(d!)$ multiplications. Allied to this comes the computation of the adjoint matrix, having similarly substantial computational complexity. The restriction is twofold: firstly, in the multiplicative depth of operations; and secondly, in the computational costs of these operations. Whereas the second restriction implies possible intractability of high-dimensional linear regression, the first restriction affects correctness of decryption and so should be regarded as more serious.

Lauter et al. (2014) observed that it is possible to analyse genomic data in a privacy-preserving framework and provide some examples of algorithms in statistical genetics which are implementable under the restrictions of homomorphic encryption, including the Cochran–Armitage trend test, the expectation–maximisation algorithm and measures of goodness-of-fit and linkage disequilibrium. The main issue in implementing these methods under the homomorphic encryption framework is that divisions are not possible. The solution proposed is to write the statistics in terms of the two factors involved in a division (dividend/numerator and divisor/denominator), compute these homomorphically and send them back to the client, who decrypts each factor and performs the division offline. For complex problems where divisions can not be grouped (by combining dividends and divisors), there will be a higher number of cipher texts being passed to the client, which increases communication costs and, more importantly, may compromise privacy since more information is contained in less processed cipher texts.

Another class of privacy-preserving statistical methods has been proposed for predictive purposes: an algorithm is trained offline (say, a regression model) and the corresponding predictive model (the parameters in the regression model, $\beta$) encrypted. For prediction tasks, covariates are encrypted and sent to the server, where computations take place (e.g., the computation of the regression model predictor, $X_{i\cdot}\beta$) and are then returned to the client for decryption (and potentially further transformation, as would be the case for generalised linear models). Examples of these include logistic regression (Bos et al., 2013) and hidden Markov models (Pathak et al., 2011).

Crucially, in all these current methods, existing algorithms are simply refactored to run homomorphically rather than developing novel approaches to approximate otherwise currently intractable statistical techniques.

## 3.2 Implementations

As will be clear from Section 2.3, many homomorphic schemes can be non-trivial to implement. Some public implementations are releases of software which was written for a specific paper, whilst there are a small number of libraries or packages enabling reuse. Most libraries or packages commonly interfaces in low-level languages such as C/C++. A very compact single C file library implementing Gentry (2010) is 'libfhe' (Minar, 2010). This implementation is based on a binary scheme, but has routines to allow encryption of integers by base-2 decomposing, encrypting each binary digit separately and then implementing binary adder arithmetic (so that even addition will involve cipher text multiplications). There is no bootstrapping implementation and at time of writing there have been no apparent updates since 2010.

'Scarab' (Perl et al., 2011) is another low-level C library, implementing instead another integer cipher text space scheme by Smart and Vercauteren (2010). This implementation allows only encryption of a binary message, although as well as providing addition (XOR) and multiplication (AND), there are full and half adders provided offering carry in and carry out or just carry out, respectively. A bootstrapping routine is also provided. There have not been additional updates in some time.

Another low level implementation, 'HELib' (Halevi and Shoup, 2014b), provides a C++ library implementing Brakerski et al. (2012), one of the early second generation of schemes (see Appendix A). It incorporates some very useful optimisations, including the work of Smart and Vercauteren (2014), which enables single-instruction multiple-data (SIMD) parallelism by packing multiple values in a single cipher text. This is under active development at the time of writing and appears the most comprehensive implementation of a modern scheme currently available. Details of the algorithms used are available in preprint (Halevi and Shoup, 2014a).

Finally, there was a recent comparison of two schemes, Fan and Vercauteren (2012) and Bos et al. (2013), in Lepoint and Naehrig (2014) which provided the C++ software used (Lepoint, 2014). Although not in the explicit form of a library it could be possible to transform this into a C++ library for the two schemes.

---

### النسخة العربية

هناك جانبان مهمان للمراجعة من منظور الإحصائي: العمل السابق على خوارزميات الإحصاء المشفرة والتطبيقات البرمجية الموجودة لاستخدام مخططات التشفير المتماثل.

في هذا القسم، يتم استعراض كلا الجانبين قبل تغطية أدوات البرمجيات الموثقة في هذه الورقة في القسم 4.

## 3.1 الإحصاء المشفر

في السنوات الأخيرة، ظهر بعض العمل على الأساليب الإحصائية للبيانات المشفرة بشكل متماثل.

اقترح Graepel وآخرون (2012) خوارزميات للتصنيف الثنائي، وهي إصدارات آمنة من مصنفات الوسائط الخطية ومميز فيشر الخطي. تم إعادة كتابة الخوارزميات بطريقة يتم فيها تجنب القسمة لكن يمكن حساب دالة النقاط الأصلية (المطلوبة للتصنيف) حتى ثابت. نظراً لأن بعض العمليات ليس لها نظير في إطار التشفير (مثل القسمة والمقارنة)، يتم إجراء بعض الحسابات دون اتصال بواسطة العميل بعد فك تشفير النتائج المعادة من السحابة. على سبيل المثال، في التصنيف الثنائي $y \in \{-1, 1\}$ مع الوسائط الخطية، يتم حساب تسمية الصنف بهذه الطريقة كإشارة لدالة النقاط. لتمثيل الأعداد الحقيقية كأعداد صحيحة، يقترح المؤلفون نهج إعادة قياس يقرب الأعداد الحقيقية بأعداد نسبية (بسط ومقام عدد صحيح) ثم يزيل المقامات عن طريق ضرب جميع الأعداد في عامل مناسب وتقريب النتيجة إلى أقرب عدد صحيح. يمكن التحكم في دقة التقريب بهذه الطريقة.

قام Wu وHaven (2012) بتوسيع العمل السابق على الإحصاء المشفر (Lauter وآخرون، 2011)، وهو حساب المتوسط والتباين المشترك في سيناريو متعدد المتغيرات، باستخدام نفس تقنية إرجاع بسطات ومقامات مشفرة منفصلة. بالإضافة إلى ذلك، يذكرون أيضاً إمكانية تطبيق (وفي الواقع ينفذون) الانحدار الخطي منخفض البعد ($d \leq 5$) باستخدام قاعدة كرامر لعكس المصفوفة $X^T X$ المطلوبة للحصول على تقديرات المربعات الصغرى العادية لمعاملات الانحدار $\hat{\beta} = (X^T X)^{-1}X^T Y$. نظراً لأن قاعدة كرامر تتضمن أيضاً قسمة على محدد $X^T X$، لا يمكن إجراء الحساب بالكامل بشكل متماثل ويجب إنهاؤه دون اتصال بواسطة العميل الذي يجمع عوامل القسمة بعد فك التشفير. بصرف النظر عن المشكلات الحسابية الناجمة عن القسمة، هناك مشكلات إضافية هنا، أهمها تعقيد قاعدة كرامر: لمشكلة ذات بعد $d$، يحتوي حساب المحدد على عمق ضربي $d - 1$ ويتطلب $O(d!)$ عمليات ضرب. مرتبط بهذا يأتي حساب المصفوفة المرافقة، ذات التعقيد الحسابي الكبير المماثل. القيد مزدوج: أولاً، في العمق الضربي للعمليات؛ وثانياً، في التكاليف الحسابية لهذه العمليات. بينما يعني القيد الثاني عدم قابلية التطبيق المحتملة للانحدار الخطي عالي البعد، فإن القيد الأول يؤثر على صحة فك التشفير وبالتالي يجب اعتباره أكثر خطورة.

لاحظ Lauter وآخرون (2014) أنه من الممكن تحليل البيانات الجينومية في إطار يحافظ على الخصوصية وتقديم بعض الأمثلة على الخوارزميات في الإحصاء الوراثي التي يمكن تطبيقها تحت قيود التشفير المتماثل، بما في ذلك اختبار الاتجاه Cochran-Armitage، وخوارزمية التوقع-التعظيم، ومقاييس جودة الملاءمة وعدم التوازن الارتباطي. المشكلة الرئيسية في تطبيق هذه الأساليب تحت إطار التشفير المتماثل هي أن القسمة غير ممكنة. الحل المقترح هو كتابة الإحصائيات من حيث العاملين المشاركين في القسمة (المقسوم/البسط والمقسوم عليه/المقام)، وحساب هذه بشكل متماثل وإرسالها مرة أخرى إلى العميل، الذي يفك تشفير كل عامل ويجري القسمة دون اتصال. بالنسبة للمشكلات المعقدة حيث لا يمكن تجميع القسمة (عن طريق دمج المقسومات والمقسومات عليها)، سيكون هناك عدد أكبر من النصوص المشفرة التي يتم تمريرها إلى العميل، مما يزيد من تكاليف الاتصال، والأهم من ذلك، قد يعرض الخصوصية للخطر نظراً لأن المزيد من المعلومات موجودة في نصوص مشفرة أقل معالجة.

تم اقتراح فئة أخرى من الأساليب الإحصائية التي تحافظ على الخصوصية لأغراض التنبؤ: يتم تدريب خوارزمية دون اتصال (لنقل، نموذج انحدار) ويتم تشفير نموذج التنبؤ المقابل (المعاملات في نموذج الانحدار، $\beta$). بالنسبة لمهام التنبؤ، يتم تشفير المتغيرات المصاحبة وإرسالها إلى الخادم، حيث تجري الحسابات (على سبيل المثال، حساب متنبئ نموذج الانحدار، $X_{i\cdot}\beta$) ثم يتم إرجاعها إلى العميل لفك التشفير (وربما المزيد من التحويل، كما سيكون الحال بالنسبة للنماذج الخطية المعممة). تتضمن أمثلة هذه الانحدار اللوجستي (Bos وآخرون، 2013) ونماذج ماركوف المخفية (Pathak وآخرون، 2011).

بشكل حاسم، في جميع هذه الأساليب الحالية، يتم ببساطة إعادة هيكلة الخوارزميات الموجودة للعمل بشكل متماثل بدلاً من تطوير أساليب جديدة لتقريب التقنيات الإحصائية التي يتعذر معالجتها حالياً.

## 3.2 التطبيقات

كما سيكون واضحاً من القسم 2.3، يمكن أن تكون العديد من المخططات المتماثلة غير تافهة للتطبيق. بعض التطبيقات العامة هي إصدارات من البرمجيات التي تم كتابتها لورقة معينة، بينما يوجد عدد صغير من المكتبات أو الحزم التي تمكن من إعادة الاستخدام. معظم المكتبات أو الحزم عادةً ما تتصل بلغات منخفضة المستوى مثل C/C++. مكتبة ملف C واحد مدمجة جداً تطبق Gentry (2010) هي 'libfhe' (Minar، 2010). يعتمد هذا التطبيق على مخطط ثنائي، ولكن لديه إجراءات للسماح بتشفير الأعداد الصحيحة عن طريق التحليل بالأساس 2، وتشفير كل رقم ثنائي على حدة ثم تنفيذ حساب الجامع الثنائي (بحيث حتى الجمع سيتضمن عمليات ضرب النص المشفر). لا يوجد تطبيق التمهيد وفي وقت الكتابة لم تكن هناك تحديثات واضحة منذ 2010.

'Scarab' (Perl وآخرون، 2011) هي مكتبة C أخرى منخفضة المستوى، تنفذ بدلاً من ذلك مخططاً آخر لفضاء النص المشفر للأعداد الصحيحة بواسطة Smart وVercauteren (2010). يسمح هذا التطبيق فقط بتشفير رسالة ثنائية، على الرغم من أنه بالإضافة إلى توفير الجمع (XOR) والضرب (AND)، هناك جوامع كاملة ونصفية توفر حمل داخل وحمل خارج أو حمل خارج فقط، على التوالي. يتم أيضاً توفير إجراء التمهيد. لم تكن هناك تحديثات إضافية لبعض الوقت.

تطبيق آخر منخفض المستوى، 'HELib' (Halevi وShoup، 2014b)، يوفر مكتبة C++ تطبق Brakerski وآخرون (2012)، أحد الجيل الثاني المبكر من المخططات (انظر الملحق A). يتضمن بعض التحسينات المفيدة للغاية، بما في ذلك عمل Smart وVercauteren (2014)، الذي يمكّن التوازي ذي البيانات المتعددة للتعليمات الواحدة (SIMD) عن طريق تعبئة قيم متعددة في نص مشفر واحد. هذا قيد التطوير النشط في وقت الكتابة ويبدو أنه التطبيق الأكثر شمولاً لمخطط حديث متاح حالياً. تفاصيل الخوارزميات المستخدمة متاحة في النشرة الأولية (Halevi وShoup، 2014a).

أخيراً، كانت هناك مقارنة حديثة لمخططين، Fan وVercauteren (2012) وBos وآخرون (2013)، في Lepoint وNaehrig (2014) والتي وفرت برمجيات C++ المستخدمة (Lepoint، 2014). على الرغم من أنها ليست في شكل صريح لمكتبة، يمكن أن يكون من الممكن تحويل هذا إلى مكتبة C++ للمخططين.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - encrypted statistics (الإحصاء المشفر)
  - binary classification (التصنيف الثنائي)
  - Linear Means (الوسائط الخطية)
  - Fisher's Linear Discriminant (مميز فيشر الخطي)
  - Cramer's rule (قاعدة كرامر)
  - linear regression (الانحدار الخطي)
  - ordinary least squares (المربعات الصغرى العادية)
  - adjoint matrix (المصفوفة المرافقة)
  - genomic data (البيانات الجينومية)
  - Cochran-Armitage trend test (اختبار الاتجاه Cochran-Armitage)
  - expectation-maximisation (التوقع-التعظيم)
  - goodness-of-fit (جودة الملاءمة)
  - linkage disequilibrium (عدم التوازن الارتباطي)
  - logistic regression (الانحدار اللوجستي)
  - hidden Markov models (نماذج ماركوف المخفية)
  - library (مكتبة)
  - bootstrapping (التمهيد)
  - SIMD (بيانات متعددة للتعليمات الواحدة)
- **Equations:** Several mathematical expressions including $\hat{\beta} = (X^T X)^{-1}X^T Y$, $X_{i\cdot}\beta$
- **Citations:** Graepel et al. (2012), Wu and Haven (2012), Lauter et al. (2011, 2014), Bos et al. (2013), Pathak et al. (2011), Minar (2010), Perl et al. (2011), Smart and Vercauteren (2010, 2014), Halevi and Shoup (2014a, 2014b), Brakerski et al. (2012), Fan and Vercauteren (2012), Lepoint and Naehrig (2014), Lepoint (2014)
- **Special handling:**
  - Statistical terminology accurately translated
  - Software library names preserved in original form
  - Mathematical notation preserved

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.89
- **Overall section score:** 0.88

This section reviews existing work on encrypted statistics and software implementations. The translation maintains technical accuracy while clearly conveying the state of the field. Quality score of 0.88 exceeds the minimum threshold.
