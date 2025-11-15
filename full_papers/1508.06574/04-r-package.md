# Section 4: HomomorphicEncryption R package
## القسم 4: حزمة R للتشفير المتماثل

**Section:** HomomorphicEncryption R package
**Translation Quality:** 0.87
**Glossary Terms Used:** homomorphic encryption, implementation, library, algorithm, software, cipher text, encryption, decryption, CPU, parallelism

---

### English Version

For statistics researchers to be able to use homomorphic encryption techniques, an easy to use yet high performance library in a high level language which is popular in the community is necessary. An R language (R Core Team, 2014) package providing such an implementation is a contribution of our work.

The HomomorphicEncryption R package (Aslett, 2014) provides an easy to use interface to begin developing and testing statistical methods in a homomorphic environment. The package has been developed to be extensible, so that as new schemes are researched by cryptographers they can be made available for use by statistics researchers with minimal additional effort. The package has a small number of generic functions for which different cryptographic backends can be used. The underlying implementation is mostly in high performance C and C++ (Eddelbuettel et al., 2011), with many of the operations setup to utilise multi-core parallelism via multithreading (Allaire et al., 2014) without requiring any end-user intervention.

The first generic cryptographic function is `pars`. The first argument to this function designates which cryptographic backend to use and allows the user to override any of the default parameters of that scheme (for example, $d$, $q$, $t$ and $\sigma$ of Section 2.3). Related to this, there is the alternative method of specifying parameters via the function `parsHelp`. This allows users to instead specify a desired minimal security level in bits and a minimal depth of multiplications required, and then computes values for $d$, $q$, $t$ and $\sigma$ which will satisfy these requirements with high probability, by automatically optimising established bounds from the literature (Lepoint and Naehrig, 2014; Lindner and Peikert, 2011)

The second generic cryptographic function is `keygen`, whose sole argument is a parameter object as returned by `pars` or `parsHelp`. `keygen` then generates a list containing public (`$pk`) and private (`$sk`) keys, along with any scheme dependent keys (such as relinearisation keys in the case of Fan and Vercauteren (2012)), which correspond to the homomorphic scheme designated by the parameter object. At this point, the parameter object is absorbed into the keys so that it doesn't need to be used for any other functions.

The third generic cryptographic function is `enc`. This requires simply the public key (as returned in the `$pk` list element from `keygen`) and the integer message to be encrypted. It then returns a cipher text encrypted under the scheme to which the public key corresponds. Crucially, the ease of use begins to become very apparent here, with `enc` overloaded to enable encryption of not just individual integers, but also vectors and matrices of integers defined in R. The structure of the vectors and matrices are preserved and the encryption process is fully multithreaded across all available CPU cores automatically.

The final generic cryptographic function is `dec`. Similarly, this requires simply the private key, as returned in the `$sk` list element from `keygen`, and the (scalar/vector/matrix) cipher text to be decrypted. It then returns the original message. Note that the structure of vector or matrix cipher texts is correctly preserved throughout.

The real simplicity becomes evident when manipulating the cipher texts. All the standard arithmetic functions (`+`, `-`, `*`) work as expected, implementing for example the cyclotomic polynomial ring algebra of the FandV scheme transparently. Moreover, vectors can be formed in the usual R manner using `c` (or extracted from the diagonal of matrix cipher texts with `diag`), element wise arithmetic can be performed on those vectors (with automatic multithreaded parallelism) and there is support for all the standard vector functions, such as `length`, `sum`, `prod` and `%*%` for inner products, just as one would conventionally use with unencrypted vectors in R. Indeed, such functionality extends to matrices, with formation of diagonal matrices via `diag` from cipher text vectors, element wise arithmetic and full matrix multiplication using the usual `%*%` R operator (again, automatically fully parallelised). Matrices also support the usual matrix functions (`dim`, `length`, `t`, etc). The package automatically dispatches these operations to the correct backend cryptographic routines to perform the corresponding cipher text space operations transparently, returning cipher text result objects which can be used in further operations or decrypted.

The following is the simplest possible instructive example. Examining the contents of `k`, `c1`, etc will show the encryption detail:

```r
library(HomomorphicEncryption)
p <- pars("FandV")
k <- keygen(p)
c1 <- enc(k$pk, c(42, 34))
c2 <- enc(k$pk, c(7, 5))
cres1 <- c1 + c2
cres2 <- c1 * c2
cres1[1]
dec(k$sk, cres1)
dec(k$sk, cres2)
```

Note that indexing into vectors and matrices as provided by R via the usual `[]` notation is fully supported, including assignment.

We hope this provides a distinctly easy-to-use software implementation in arguably the most popular high level language in use among data scientists today, including automatic help for encryption scheme parameter selection to aid non-cryptographers. Moreover, given the computational burden of homomorphic schemes, the transparent multithreaded parallelism automatically across all CPU cores in all available scenarios (encryption, decryption and arithmetic with vectors/matrices) enables focus to be on the subject matter questions.

At present, the scheme of Fan and Vercauteren (2012) (described in Section 2.3) has been implemented, making use of FLINT (Hart, 2010) for certain polynomial operations and GMP (Granlund and the GMP development team, 2012) for high performance arbitrary precision arithmetic. Backends for further homomorphic encryption schemes may be added in the future.

Table 1 provides indicative timings for common operations using the default parameters of the package (which match the default parameters suggested in Fan and Vercauteren, 2012).

**Table 1:** Timings (in seconds; average of 100 repetitions) for operations on cipher texts using the HomomorphicEncryption package. All timings performed on an Amazon EC2 c4.8xlarge instance for reproducibility. S represents a scalar, V a vector of size 100 and M a matrix of size 10 × 10.

| scalar operations | | vector operations | | matrix operations | |
|-------------------|-------|-------------------|-------|-------------------|-------|
| S+S | 0.003 | V+V | 0.58 | M+M | 0.87 |
| S*S | 0.084 | V*V | 1.59 | M*M | 8.49 |
| | | V%*%V | 1.59 | M%*%M | 10.21 |

---

### النسخة العربية

لكي يتمكن باحثو الإحصاء من استخدام تقنيات التشفير المتماثل، من الضروري وجود مكتبة سهلة الاستخدام وعالية الأداء بلغة عالية المستوى شائعة في المجتمع. حزمة لغة R (R Core Team، 2014) توفر مثل هذا التطبيق هي مساهمة من عملنا.

توفر حزمة R للتشفير المتماثل HomomorphicEncryption (Aslett، 2014) واجهة سهلة الاستخدام للبدء في تطوير واختبار الأساليب الإحصائية في بيئة متماثلة. تم تطوير الحزمة لتكون قابلة للتوسيع، بحيث عندما يبحث علماء التشفير في مخططات جديدة، يمكن جعلها متاحة للاستخدام من قبل باحثي الإحصاء بأقل جهد إضافي. تحتوي الحزمة على عدد صغير من الدوال العامة التي يمكن استخدام خلفيات تشفيرية مختلفة لها. التطبيق الأساسي معظمه في C وC++ عالية الأداء (Eddelbuettel وآخرون، 2011)، مع إعداد العديد من العمليات للاستفادة من التوازي متعدد النواة عبر تعدد الخيوط (Allaire وآخرون، 2014) دون الحاجة إلى أي تدخل من المستخدم النهائي.

الدالة التشفيرية العامة الأولى هي `pars`. يحدد الوسيط الأول لهذه الدالة الخلفية التشفيرية المراد استخدامها ويسمح للمستخدم بتجاوز أي من المعلمات الافتراضية لذلك المخطط (على سبيل المثال، $d$ و $q$ و $t$ و $\sigma$ من القسم 2.3). المتعلق بهذا، هناك طريقة بديلة لتحديد المعلمات عبر الدالة `parsHelp`. يسمح هذا للمستخدمين بدلاً من ذلك بتحديد مستوى أمان أدنى مرغوب بالبتات وعمق أدنى للضرب المطلوب، ثم يحسب القيم لـ $d$ و $q$ و $t$ و $\sigma$ التي ستحقق هذه المتطلبات باحتمالية عالية، من خلال تحسين الحدود المثبتة من الأدبيات تلقائياً (Lepoint وNaehrig، 2014؛ Lindner وPeikert، 2011).

الدالة التشفيرية العامة الثانية هي `keygen`، والوسيط الوحيد لها هو كائن معلمة كما يتم إرجاعه بواسطة `pars` أو `parsHelp`. ثم يولد `keygen` قائمة تحتوي على مفاتيح عامة (`$pk`) وخاصة (`$sk`)، جنباً إلى جنب مع أي مفاتيح تعتمد على المخطط (مثل مفاتيح إعادة الخطية في حالة Fan وVercauteren (2012))، والتي تتوافق مع المخطط المتماثل المحدد بواسطة كائن المعلمة. في هذه المرحلة، يتم امتصاص كائن المعلمة في المفاتيح بحيث لا حاجة لاستخدامه لأي دوال أخرى.

الدالة التشفيرية العامة الثالثة هي `enc`. يتطلب هذا ببساطة المفتاح العام (كما تم إرجاعه في عنصر القائمة `$pk` من `keygen`) ورسالة العدد الصحيح المراد تشفيرها. ثم تعيد نصاً مشفراً مشفراً تحت المخطط الذي يتوافق معه المفتاح العام. بشكل حاسم، تبدأ سهولة الاستخدام في أن تصبح واضحة جداً هنا، مع `enc` محمل بشكل زائد لتمكين تشفير ليس فقط الأعداد الصحيحة الفردية، ولكن أيضاً المتجهات والمصفوفات من الأعداد الصحيحة المحددة في R. يتم الحفاظ على بنية المتجهات والمصفوفات وعملية التشفير متعددة الخيوط بالكامل عبر جميع نوى وحدة المعالجة المركزية المتاحة تلقائياً.

الدالة التشفيرية العامة النهائية هي `dec`. وبالمثل، يتطلب هذا ببساطة المفتاح الخاص، كما تم إرجاعه في عنصر القائمة `$sk` من `keygen`، والنص المشفر (القياسي/المتجه/المصفوفة) المراد فك تشفيره. ثم تعيد الرسالة الأصلية. لاحظ أن بنية نصوص مشفرة المتجه أو المصفوفة محفوظة بشكل صحيح طوال الوقت.

تصبح البساطة الحقيقية واضحة عند التعامل مع النصوص المشفرة. جميع الدوال الحسابية القياسية (`+` و `-` و `*`) تعمل كما هو متوقع، وتطبق على سبيل المثال الجبر الحلقي لكثيرة الحدود الحلقية لمخطط FandV بشكل شفاف. علاوة على ذلك، يمكن تكوين المتجهات بالطريقة المعتادة في R باستخدام `c` (أو استخراجها من قطر النصوص المشفرة للمصفوفة باستخدام `diag`)، ويمكن إجراء حساب عنصري على تلك المتجهات (مع التوازي متعدد الخيوط التلقائي) وهناك دعم لجميع دوال المتجهات القياسية، مثل `length` و `sum` و `prod` و `%*%` للمنتجات الداخلية، تماماً كما يستخدمها المرء تقليدياً مع المتجهات غير المشفرة في R. في الواقع، تمتد هذه الوظيفة إلى المصفوفات، مع تكوين المصفوفات القطرية عبر `diag` من متجهات النص المشفر، والحساب العنصري وضرب المصفوفة الكامل باستخدام عامل R المعتاد `%*%` (مرة أخرى، بالتوازي الكامل تلقائياً). تدعم المصفوفات أيضاً دوال المصفوفة المعتادة (`dim` و `length` و `t`، إلخ). ترسل الحزمة هذه العمليات تلقائياً إلى إجراءات الخلفية التشفيرية الصحيحة لأداء عمليات فضاء النص المشفر المقابلة بشكل شفاف، وإرجاع كائنات نتيجة النص المشفر التي يمكن استخدامها في عمليات أخرى أو فك تشفيرها.

فيما يلي أبسط مثال تعليمي ممكن. فحص محتويات `k` و `c1`، إلخ سيظهر تفاصيل التشفير:

```r
library(HomomorphicEncryption)
p <- pars("FandV")
k <- keygen(p)
c1 <- enc(k$pk, c(42, 34))
c2 <- enc(k$pk, c(7, 5))
cres1 <- c1 + c2
cres2 <- c1 * c2
cres1[1]
dec(k$sk, cres1)
dec(k$sk, cres2)
```

لاحظ أن الفهرسة في المتجهات والمصفوفات كما توفرها R عبر ترميز `[]` المعتاد مدعومة بالكامل، بما في ذلك التعيين.

نأمل أن يوفر هذا تطبيقاً برمجياً سهل الاستخدام بشكل مميز في يمكن القول أنها اللغة عالية المستوى الأكثر شعبية قيد الاستخدام بين علماء البيانات اليوم، بما في ذلك المساعدة التلقائية لاختيار معلمة مخطط التشفير لمساعدة غير علماء التشفير. علاوة على ذلك، نظراً للعبء الحسابي للمخططات المتماثلة، فإن التوازي متعدد الخيوط الشفاف تلقائياً عبر جميع نوى وحدة المعالجة المركزية في جميع السيناريوهات المتاحة (التشفير وفك التشفير والحساب مع المتجهات/المصفوفات) يمكّن من التركيز على أسئلة الموضوع.

في الوقت الحالي، تم تطبيق مخطط Fan وVercauteren (2012) (الموصوف في القسم 2.3)، مع استخدام FLINT (Hart، 2010) لعمليات كثيرة حدود معينة وGMP (Granlund وفريق تطوير GMP، 2012) للحساب عالي الأداء ذو الدقة التعسفية. يمكن إضافة خلفيات لمخططات التشفير المتماثل الأخرى في المستقبل.

يوفر الجدول 1 توقيتات إرشادية للعمليات الشائعة باستخدام المعلمات الافتراضية للحزمة (التي تطابق المعلمات الافتراضية المقترحة في Fan وVercauteren، 2012).

**الجدول 1:** التوقيتات (بالثواني؛ متوسط 100 تكرار) للعمليات على النصوص المشفرة باستخدام حزمة HomomorphicEncryption. تم إجراء جميع التوقيتات على مثيل Amazon EC2 c4.8xlarge من أجل القابلية للتكرار. S يمثل قياسي، V متجه بحجم 100 وM مصفوفة بحجم 10 × 10.

| العمليات القياسية | | عمليات المتجهات | | عمليات المصفوفات | |
|-------------------|-------|-------------------|-------|-------------------|-------|
| S+S | 0.003 | V+V | 0.58 | M+M | 0.87 |
| S*S | 0.084 | V*V | 1.59 | M*M | 8.49 |
| | | V%*%V | 1.59 | M%*%M | 10.21 |

---

### Translation Notes

- **Figures referenced:** Table 1 (performance timings)
- **Key terms introduced:**
  - R package (حزمة R)
  - high performance (عالي الأداء)
  - extensible (قابلة للتوسيع)
  - backend (خلفية)
  - multithreading (تعدد الخيوط)
  - multi-core parallelism (التوازي متعدد النواة)
  - generic function (دالة عامة)
  - parameter object (كائن معلمة)
  - public key (مفتاح عام)
  - private key (مفتاح خاص)
  - overloaded (محمل بشكل زائد)
  - inner product (منتج داخلي)
  - element wise (عنصري)
- **Equations:** None
- **Citations:** R Core Team (2014), Aslett (2014), Eddelbuettel et al. (2011), Allaire et al. (2014), Lepoint and Naehrig (2014), Lindner and Peikert (2011), Fan and Vercauteren (2012), Hart (2010), Granlund and the GMP development team (2012)
- **Special handling:**
  - R code preserved in original form (programming language)
  - Function names preserved (pars, keygen, enc, dec, etc.)
  - R operators preserved (+, -, *, %*%, [], etc.)
  - Performance table translated with structure preserved

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87

This section describes the software contribution of the paper. The translation preserves all code examples and technical details while providing clear Arabic explanations. Quality score of 0.87 exceeds the minimum threshold.
