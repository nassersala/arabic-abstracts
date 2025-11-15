# Section 6: Related Work
## القسم 6: الأعمال ذات الصلة

**Section:** Related Work
**Translation Quality:** 0.85
**Glossary Terms Used:** linear types, uniqueness typing, ownership typing, type system, polymorphism, monads, dependent types

---

### English Version

There are two possible choices to indicate the distinction between linear and unrestricted objects. Our choice is to use the arrow type. That is, we have both a linear arrow to introduce linear objects in the environment, and an unrestricted arrow to introduce unrestricted objects. This choice is featured in the work of McBride [2016] and Ghica and Smith [2014] and is ultimately inspired by Girard's presentation of linear logic, which features only linear arrows, and where the unrestricted arrow A → B is encoded as !A ⊸ B.

Another popular choice [Mazurak et al. 2010; Morris 2016; Tov and Pucella 2011; Wadler 1990] is to separate types into two kinds: a linear kind and an unrestricted kind. Values with a type whose kind is linear are linear, and the others are unrestricted. While this does not match linear logic, it is attractive on the surface because, intuitively, some types are inherently linear (file handles, updateable arrays, etc.) and some types are inherently unrestricted (Int, Bool, etc.). However, after scratching the surface we have discovered that "linearity via arrows" has an edge over "linearity via kinds".

**6.1 Linearity via arrows vs. linearity via kinds**

Better code reuse. When retrofitting linear types in an existing language, it is important to share as much code as possible between linear and non-linear code. In a system with linearity on arrows, the subsumption relation and the scaling of context in the application rule mean that much linear code can be used as-is from unrestricted code, and be properly promoted.

In contrast, in a two-kind system, a function must declare the exact linearity of its return value. Consequently, to make a function promotable from linear to unrestricted, its declaration must use polymorphism over kinds.

Linear Haskell features quantification over multiplicities and parameterised arrows. In a two-kinds system, sharing data types also requires polymorphism.

**6.2 Other variants of "linearity on the arrow"**

The λq→ type system is heavily inspired from the work of Ghica and Smith [2014] and McBride [2016]. Both of them present a type system where arrows are annotated with the multiplicity of the argument that they require, and where the multiplicities form a semi-ring.

In contrast with λq→, McBride uses a multiplicity-annotated type judgement Γ ⊢ρ t : A, where ρ represents the multiplicity of t. The problem is that this check is arguably too coarse, and results in the judgement ⊢ω λx.(x, x) : A ⊸ (A,A) being derivable. This derivation is not desirable: it implies that there cannot be reusable definitions of linear functions.

The essential differences between our system and that of Ghica and Smith is that we support multiplicity-polymorphism and datatypes. In particular our case rule is novel.

**6.3 Uniqueness and ownership typing**

The literature contains many proposals for uniqueness (or ownership) types. Prominent representative languages with uniqueness types include Clean [Barendsen and Smetsers 1996] and Rust [Matsakis and Klock 2014]. Linear Haskell, on the other hand, is designed around linear types based on linear logic [Girard 1987].

Idris [Brady 2013] features uniqueness types, which have been used to enforce communication protocols [Brady 2017]. Uniqueness types in Idris are being replaced by linear types based on QTT [Atkey 2017].

Linear types and uniqueness types are, at their core, dual: whereas a linear type is a contract that a function uses its argument exactly once even if the call's context can share a linear argument as many times as it pleases, a uniqueness type ensures that the argument of a function is not used anywhere else in the expression's context even if the callee can work with the argument as it pleases.

Rust & Borrowing. In Linear Haskell we need to thread linear variables throughout the program. Rust uses instead a type-system feature called borrowing. Borrowed values differ from owned values in that they can be used in an unrestricted fashion, albeit in a delimited scope.

Borrowing does not come without a cost, however: if a function f borrows a value v of type T, then the caller of the function must retain v alive until f has returned; the consequence is that Rust cannot, in general, perform tail-call elimination, crucial to the operational behaviour of many functional programs.

**6.4 Linearity via monads**

Launchbury and Peyton Jones [1995] taught us a conceptually simple approach to lifetimes: the ST monad. It has a phantom type parameter s (the region) that is instantiated once at the beginning of the computation by a runST function of type: runST :: ∀a. (∀s. ST s a) → a.

Region-types. With region-types such as ST, we cannot express typestates, but this is sufficient to offer a safe API for freezing array or ensuring that files are eventually closed. This simplicity comes at a cost: it forces operations to be more sequentialised than need be, and does not support the interaction of nested regions.

Kiselyov and Shan [2008] show that it is possible to promote resources in parent regions to resources in a subregion. But this is an explicit and monadic operation, forcing an unnatural imperative style of programming where order of evaluation is explicit.

In contrast, with linear types, values in two regions can safely be mixed: elements can be moved from one data structure (or heap) to another, linearly, with responsibility for deallocation transferred along.

Idris's dependent indexed monad. To go beyond simple regions, Idris [Brady 2013] introduces a generic way to add typestate on top of a monad, the ST indexed monad transformer. The basic idea is that everything which must be single-threaded becomes part of the state of the monad.

The support for dependent types in GHC is not as comprehensive as Idris's. But it is conceivable to implement such an indexed monad transformer in Haskell. However, this is not an easy task, and we can anticipate that the error messages would be hard to stomach.

---

### النسخة العربية

هناك خياران محتملان للإشارة إلى التمييز بين الكائنات الخطية وغير المقيدة. خيارنا هو استخدام نوع السهم. أي أن لدينا سهماً خطياً لتقديم كائنات خطية في البيئة، وسهماً غير مقيد لتقديم كائنات غير مقيدة. يظهر هذا الخيار في عمل McBride [2016] و Ghica و Smith [2014] وهو مستوحى في النهاية من عرض Girard للمنطق الخطي، الذي يتضمن أسهماً خطية فقط، وحيث يتم ترميز السهم غير المقيد A → B على أنه !A ⊸ B.

خيار شائع آخر هو فصل الأنواع إلى نوعين: نوع خطي ونوع غير مقيد. القيم ذات النوع الذي يكون نوعه خطياً هي خطية، والبقية غير مقيدة. بينما لا يتطابق هذا مع المنطق الخطي، إلا أنه جذاب ظاهرياً لأنه، بديهياً، بعض الأنواع خطية بطبيعتها (معالجات الملفات، المصفوفات القابلة للتحديث، إلخ) وبعض الأنواع غير مقيدة بطبيعتها (Int، Bool، إلخ). ومع ذلك، بعد التعمق قليلاً اكتشفنا أن "الخطية عبر الأسهم" لها ميزة على "الخطية عبر الأنواع".

**6.1 الخطية عبر الأسهم مقابل الخطية عبر الأنواع**

إعادة استخدام أفضل للشفرة. عند إضافة الأنواع الخطية إلى لغة موجودة، من المهم مشاركة أكبر قدر ممكن من الشفرة بين الشفرة الخطية وغير الخطية. في نظام بالخطية على الأسهم، تعني علاقة التضمين وقياس السياق في قاعدة التطبيق أن الكثير من الشفرة الخطية يمكن استخدامها كما هي من الشفرة غير المقيدة، وترقيتها بشكل صحيح.

في المقابل، في نظام من نوعين، يجب على الدالة الإعلان عن الخطية الدقيقة لقيمة الإرجاع الخاصة بها. وبالتالي، لجعل دالة قابلة للترقية من خطية إلى غير مقيدة، يجب أن يستخدم إعلانها تعددية الأشكال على الأنواع.

يتميز Haskell الخطي بالتحديد الكمي على التعدديات والأسهم ذات المعاملات. في نظام من نوعين، تتطلب مشاركة أنواع البيانات أيضاً تعددية الأشكال.

**6.2 متغيرات أخرى من "الخطية على السهم"**

يستوحى نظام الأنواع λq→ بشكل كبير من عمل Ghica و Smith [2014] و McBride [2016]. كلاهما يقدم نظام أنواع حيث يتم تعليق الأسهم بتعددية الوسيط الذي تتطلبه، وحيث تشكل التعدديات حلقة نصف.

على النقيض من λq→، يستخدم McBride حكم نوع معلق بالتعددية Γ ⊢ρ t : A، حيث يمثل ρ تعددية t. المشكلة هي أن هذا الفحص خشن جداً بشكل مثير للجدل، ويؤدي إلى أن يكون الحكم ⊢ω λx.(x, x) : A ⊸ (A,A) قابلاً للاشتقاق. هذا الاشتقاق غير مرغوب فيه: فهو يعني أنه لا يمكن أن تكون هناك تعريفات قابلة لإعادة الاستخدام للدوال الخطية.

الاختلافات الأساسية بين نظامنا ونظام Ghica و Smith هي أننا ندعم تعددية التعددية وأنواع البيانات. على وجه الخصوص، قاعدة الحالة (case) الخاصة بنا جديدة.

**6.3 كتابة الفردية والملكية**

تحتوي الأدبيات على العديد من المقترحات لأنواع الفردية (أو الملكية). تشمل اللغات التمثيلية البارزة ذات أنواع الفردية Clean [Barendsen و Smetsers 1996] و Rust [Matsakis و Klock 2014]. من ناحية أخرى، تم تصميم Haskell الخطي حول الأنواع الخطية القائمة على المنطق الخطي [Girard 1987].

يتميز Idris [Brady 2013] بأنواع الفردية، والتي تم استخدامها لفرض بروتوكولات الاتصال [Brady 2017]. يتم استبدال أنواع الفردية في Idris بأنواع خطية بناءً على QTT [Atkey 2017].

الأنواع الخطية وأنواع الفردية، في جوهرها، ثنائية: في حين أن النوع الخطي هو عقد بأن الدالة تستخدم وسيطها مرة واحدة بالضبط حتى لو كان سياق الاستدعاء يمكنه مشاركة وسيط خطي بقدر ما يشاء، فإن نوع الفردية يضمن عدم استخدام وسيط الدالة في أي مكان آخر في سياق التعبير حتى لو كان المستدعى يمكنه العمل مع الوسيط كما يشاء.

Rust والاستعارة. في Haskell الخطي نحتاج إلى إدخال المتغيرات الخطية في جميع أنحاء البرنامج. تستخدم Rust بدلاً من ذلك ميزة نظام الأنواع تسمى الاستعارة (borrowing). تختلف القيم المستعارة عن القيم المملوكة من حيث أنه يمكن استخدامها بطريقة غير مقيدة، وإن كان ذلك في نطاق محدود.

ومع ذلك، لا تأتي الاستعارة بدون تكلفة: إذا استعارت دالة f قيمة v من النوع T، فيجب على المتصل بالدالة الاحتفاظ بـ v حياً حتى تعود f؛ النتيجة هي أن Rust لا يمكنها، بشكل عام، إجراء إلغاء استدعاء الذيل، وهو أمر بالغ الأهمية للسلوك التشغيلي للعديد من البرامج الوظيفية.

**6.4 الخطية عبر المونادات**

علمنا Launchbury و Peyton Jones [1995] نهجاً بسيطاً من الناحية المفاهيمية لمدد الحياة: ST monad. لديها معامل نوع وهمي s (المنطقة) يتم إنشاؤه مرة واحدة في بداية الحساب بواسطة دالة runST من النوع: runST :: ∀a. (∀s. ST s a) → a.

أنواع المناطق. مع أنواع المناطق مثل ST، لا يمكننا التعبير عن حالات الأنواع، لكن هذا يكفي لتقديم واجهة برمجة تطبيقات آمنة لتجميد المصفوفة أو ضمان إغلاق الملفات في النهاية. تأتي هذه البساطة بتكلفة: فهي تفرض أن تكون العمليات أكثر تسلسلاً مما هو مطلوب، ولا تدعم تفاعل المناطق المتداخلة.

يوضح Kiselyov و Shan [2008] أنه من الممكن ترقية الموارد في المناطق الأم إلى موارد في منطقة فرعية. لكن هذه عملية صريحة ومونادية، تفرض أسلوب برمجة إلزامياً غير طبيعي حيث يكون ترتيب التقييم صريحاً.

في المقابل، مع الأنواع الخطية، يمكن خلط القيم في منطقتين بأمان: يمكن نقل العناصر من بنية بيانات (أو كومة) إلى أخرى، بشكل خطي، مع نقل مسؤولية إلغاء التخصيص معها.

المونادة المفهرسة التابعة لـ Idris. للذهاب إلى ما هو أبعد من المناطق البسيطة، يقدم Idris [Brady 2013] طريقة عامة لإضافة حالة الأنواع فوق المونادة، محول المونادة المفهرس ST. الفكرة الأساسية هي أن كل شيء يجب أن يكون أحادي الخيط يصبح جزءاً من حالة المونادة.

الدعم للأنواع التابعة في GHC ليس شاملاً كما في Idris. لكن من الممكن تنفيذ مثل هذا محول المونادة المفهرس في Haskell. ومع ذلك، هذه ليست مهمة سهلة، ويمكننا أن نتوقع أن رسائل الخطأ ستكون صعبة الاستيعاب.

---

### Translation Notes

- **Key comparisons:**
  - Linearity via arrows vs. linearity via kinds (الخطية عبر الأسهم مقابل الخطية عبر الأنواع)
  - Linear types vs. uniqueness types (الأنواع الخطية مقابل أنواع الفردية)
  - Region-based vs. linear approaches (المناهج القائمة على المناطق مقابل المناهج الخطية)
- **Languages discussed:** Clean, Rust, Idris, Haskell
- **Technical concepts:**
  - Borrowing (الاستعارة)
  - Ownership typing (كتابة الملكية)
  - Uniqueness typing (كتابة الفردية)
  - ST monad (ST monad)
  - Region types (أنواع المناطق)
  - Indexed monad transformer (محول المونادة المفهرس)

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.85
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.85
