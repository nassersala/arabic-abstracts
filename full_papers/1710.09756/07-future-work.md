# Section 7: Future Work
## القسم 7: العمل المستقبلي

**Section:** Future Work
**Translation Quality:** 0.85
**Glossary Terms Used:** compiler optimizations, inlining, type inference, dependent types, multiplicities, borrowing

---

### English Version

**7.1 Controlling program optimisations**

Inlining is a cornerstone of program optimisation, exposing opportunities for many program transformations. Yet not every function can be inlined without negative effects on performance: inlining a function with more than one use sites of the argument may result in duplicating a computation. For example one should avoid the following reduction: (λx → x ++ x) expensive −→ expensive ++ expensive.

Many compilers can discover safe inlining opportunities by analysing source code and determine how many times functions use their arguments. (In GHC it is called the cardinality analysis [Sergey et al. 2014]). A limitation of such an analysis is that it is necessarily heuristic (the problem is undecidable for Haskell). Because inlining is crucial to efficiency, programmers find themselves in the uncomfortable position of relying on a heuristic to obtain efficient programs. Consequently, a small, seemingly innocuous change can prevent a critical inlining opportunity and have rippling catastrophic effects throughout the program. Such unpredictable behaviour justifies the folklore that high-level languages should be abandoned to gain precise control over program efficiency.

A remedy is to use the multiplicity annotations of λq→ as cardinality declarations. Formalising and implementing the integration of multiplicities in the cardinality analysis is left as future work.

**7.2 Extending multiplicities**

For the sake of this article, we use only multiplicities 1 and ω. But in fact λq→ can readily be extended to more, following Ghica and Smith [2014] and McBride [2016]. The general setting for λq→ is an ordered-semiring of multiplicities (with a join operation for type inference). In particular, in order to support dependent types, McBride needs a 0 multiplicity. We may also want to add a multiplicity for affine arguments (i.e. arguments which can be used at most once).

The typing rules are mostly unchanged with the caveat that caseπ must exclude π = 0 (in particular we see that we cannot substitute multiplicity variables by 0). The variable rule becomes:

x :1 A ⩽ Γ
———————
Γ ⊢ x : A

Where the order on contexts is the point-wise extension of the order on multiplicities.

In Sec. 6.3, we have considered the notion of borrowing: delimiting life-time without restricting to linear usage. This seems to be a useful pattern, and we believe it can be encoded as an additional multiplicity as follows: let β be an additional multiplicity with the following characteristics:

• 1 < β < ω
• β + β = 1 + β = 0 + β = 1 + 1 = β

That is, β supports contraction and weakening but is smaller than ω. We can then introduce a value with an explicit lifetime with the following pattern:

borrow :: (T →β Unrestricted a) →β Unrestricted a

The borrow function makes the life-time manifest in the structure of the program. In particular, it is clear that calls within the argument of borrow are not tail: a shortcoming of borrowing that we mentioned in Sec. 6.3.

**7.3 Future industrial applications**

Our own work in an industrial context triggered our efforts to add linear types to GHC. We were originally motivated by precisely typed protocols for complex interactions and by taming GC latencies in distributed systems. But we have since noticed other potential applications of linearity in a variety of other industrial projects.

Streaming I/O. Program inputs and outputs are frequently much larger than the available RAM on any single node. Rather than building complex pipelines with brittle explicit loops copying data piecemeal to spare our precious RAM, one approach is to compose combinators that transform, split and merge data wholemeal but in a streaming fashion. These combinators manipulate first-class streams and guarantee bounded memory usage, as in the below infinitely running echo service:

receive :: Socket → IOStream Msg
send :: Socket → IOStream Msg → IO ()
echo isock osock = send osock (receive isock)

However, reifying sequences of IO actions (socket reads) in this way runs the risk that effects might be duplicated inadvertently. In the above example, we wouldn't want to inadvertently hand over the receive stream to multiple consumers, or the abstraction of wholemeal I/O programming would be broken, because neither consumer would ultimately see the same values from the stream. If say one consumer reads in the stream first, the second consumer would see an empty stream — not what the first consumer saw. We have seen this very error several times in industrial projects, where the symptoms are bugs whose root cause are painful to track down. A linear type discipline would prevent such bugs.

Programming foreign heaps. Complex projects with large teams invariably involve a mix of programming languages. Reusing legacy code is often much cheaper than reimplementing it. A key to successful interoperation between languages is performance. If all code lives in the same address space, then data need not be copied as it flows from function to function implemented in multiple programming languages. Trouble is, language A needs to tell language B what objects in language A's heap still have live references in the call stack of language B to avoid too eager garbage collection.

For instance, users of inline-java call the JVM from Haskell via the JNI. The JVM implicitly creates so-called local references any time we request a Java object from the JVM. The references count as GC roots that prevent eager garbage collection. For performance, local references have a restricted scope: they are purely thread-local and never survive the call frame in which they were created. Both restrictions to their use can be enforced with linear types.

Remote direct memory access. Section 5.1 is an example of an API requiring destination-passing style. This style often appears in performance-sensitive contexts. One notable example from our industrial experience is RDMA (Remote Direct Memory Access), which enables machines in high-performance clusters to copy data from the address space in one process to that of a remote process directly, bypassing the kernel and even the CPU, thereby avoiding any unneeded copy in the process.

One could treat a remote memory location as a low-level resource, to be accessed using an imperative API. Using linear types, one can instead treat it as a high-level value which can be written to directly (but exactly once). Using linear types the compiler can ensure that, as soon as the writing operation is complete, the destination computer is notified.

---

### النسخة العربية

**7.1 التحكم في تحسينات البرنامج**

الإدراج (Inlining) هو حجر الزاوية في تحسين البرنامج، حيث يكشف عن فرص للعديد من تحويلات البرنامج. ومع ذلك، لا يمكن إدراج كل دالة دون تأثيرات سلبية على الأداء: قد يؤدي إدراج دالة بأكثر من موقع استخدام واحد للوسيط إلى تكرار عملية حسابية. على سبيل المثال، يجب تجنب الاختزال التالي: (λx → x ++ x) expensive −→ expensive ++ expensive.

يمكن للعديد من المترجمات اكتشاف فرص الإدراج الآمنة من خلال تحليل الشفرة المصدرية وتحديد عدد المرات التي تستخدم فيها الدوال وسائطها. (في GHC يُطلق عليها تحليل العددية [Sergey et al. 2014]). القيد على مثل هذا التحليل هو أنه بالضرورة إرشادي (المشكلة غير قابلة للحل لـ Haskell). نظراً لأن الإدراج بالغ الأهمية للكفاءة، يجد المبرمجون أنفسهم في موقف غير مريح من الاعتماد على إرشادي للحصول على برامج فعالة. وبالتالي، يمكن لتغيير صغير يبدو غير ضار أن يمنع فرصة إدراج حرجة ويكون له تأثيرات كارثية متموجة في جميع أنحاء البرنامج. مثل هذا السلوك غير المتوقع يبرر المعرفة الشائعة بأنه يجب التخلي عن اللغات عالية المستوى للحصول على تحكم دقيق في كفاءة البرنامج.

الحل هو استخدام تعليقات التعددية في λq→ كإعلانات عددية. ترك إضفاء الطابع الرسمي وتنفيذ دمج التعدديات في تحليل العددية كعمل مستقبلي.

**7.2 توسيع التعدديات**

من أجل هذا المقال، نستخدم فقط التعدديات 1 و ω. لكن في الواقع يمكن توسيع λq→ بسهولة إلى المزيد، باتباع Ghica و Smith [2014] و McBride [2016]. الإعداد العام لـ λq→ هو حلقة نصف مرتبة من التعدديات (مع عملية اتحاد لاستدلال الأنواع). على وجه الخصوص، من أجل دعم الأنواع التابعة، يحتاج McBride إلى تعددية 0. قد نرغب أيضاً في إضافة تعددية للوسائط الأفينية (أي الوسائط التي يمكن استخدامها على الأكثر مرة واحدة).

قواعد الكتابة دون تغيير في الغالب مع التحذير من أن caseπ يجب أن يستبعد π = 0 (على وجه الخصوص نرى أننا لا يمكننا استبدال متغيرات التعددية بـ 0). تصبح قاعدة المتغير:

x :1 A ⩽ Γ
———————
Γ ⊢ x : A

حيث الترتيب على السياقات هو التمديد النقطي للترتيب على التعدديات.

في القسم 6.3، اعتبرنا مفهوم الاستعارة (borrowing): تحديد مدة الحياة دون التقييد بالاستخدام الخطي. يبدو أن هذا نمط مفيد، ونعتقد أنه يمكن ترميزه كتعددية إضافية على النحو التالي: دع β تكون تعددية إضافية بالخصائص التالية:

• 1 < β < ω
• β + β = 1 + β = 0 + β = 1 + 1 = β

أي أن β تدعم الانكماش والإضعاف ولكنها أصغر من ω. يمكننا بعد ذلك تقديم قيمة بمدة حياة صريحة بالنمط التالي:

borrow :: (T →β Unrestricted a) →β Unrestricted a

تجعل دالة borrow مدة الحياة واضحة في بنية البرنامج. على وجه الخصوص، من الواضح أن الاستدعاءات داخل وسيط borrow ليست ذيلية: قصور في الاستعارة ذكرناه في القسم 6.3.

**7.3 التطبيقات الصناعية المستقبلية**

أدى عملنا في سياق صناعي إلى إطلاق جهودنا لإضافة الأنواع الخطية إلى GHC. كانت دوافعنا في الأصل هي البروتوكولات المكتوبة بدقة للتفاعلات المعقدة وترويض زمن الانتقال لجامع القمامة في الأنظمة الموزعة. لكننا لاحظنا منذ ذلك الحين تطبيقات محتملة أخرى للخطية في مجموعة متنوعة من المشاريع الصناعية الأخرى.

الإدخال/الإخراج الانسيابي (Streaming I/O). إن مدخلات ومخرجات البرنامج في كثير من الأحيان أكبر بكثير من ذاكرة الوصول العشوائي المتاحة على أي عقدة واحدة. بدلاً من بناء خطوط أنابيب معقدة بحلقات صريحة هشة تنسخ البيانات على دفعات لتوفير ذاكرة الوصول العشوائي الثمينة، يتمثل أحد الأساليب في تكوين مجمعات تحول وتقسم وتدمج البيانات بالكامل ولكن بطريقة انسيابية. تتعامل هذه المجمعات مع التدفقات من الدرجة الأولى وتضمن استخدام ذاكرة محدود، كما في خدمة الصدى التي تعمل إلى ما لا نهاية أدناه:

receive :: Socket → IOStream Msg
send :: Socket → IOStream Msg → IO ()
echo isock osock = send osock (receive isock)

ومع ذلك، فإن تجسيد تسلسلات إجراءات الإدخال/الإخراج (قراءات المقبس) بهذه الطريقة يحمل خطر تكرار التأثيرات عن غير قصد. في المثال أعلاه، لن نرغب في تسليم تدفق الاستقبال (receive stream) إلى مستهلكين متعددين عن غير قصد، أو سينكسر تجريد برمجة الإدخال/الإخراج الكامل، لأن أياً من المستهلكين لن يرى في النهاية نفس القيم من التدفق. إذا قرأ أحد المستهلكين التدفق أولاً، فسيرى المستهلك الثاني تدفقاً فارغاً — وليس ما رآه المستهلك الأول. لقد رأينا هذا الخطأ بالذات عدة مرات في المشاريع الصناعية، حيث الأعراض هي أخطاء يصعب تتبع سببها الجذري. سيمنع نظام الأنواع الخطي مثل هذه الأخطاء.

برمجة الأكوام الأجنبية. تتضمن المشاريع المعقدة ذات الفرق الكبيرة حتماً مزيجاً من لغات البرمجة. غالباً ما تكون إعادة استخدام الشفرة القديمة أرخص بكثير من إعادة تنفيذها. أحد مفاتيح التشغيل البيني الناجح بين اللغات هو الأداء. إذا كانت جميع الشفرات تعيش في نفس مساحة العنوان، فلا حاجة إلى نسخ البيانات أثناء تدفقها من دالة إلى دالة منفذة بلغات برمجة متعددة. المشكلة هي أن اللغة A تحتاج إلى إخبار اللغة B بالكائنات الموجودة في كومة اللغة A التي لا تزال لديها مراجع مباشرة في مكدس استدعاءات اللغة B لتجنب جمع القمامة المفرط في الحماس.

على سبيل المثال، يستدعي مستخدمو inline-java جهاز JVM من Haskell عبر JNI. ينشئ JVM ضمنياً ما يسمى بالمراجع المحلية في أي وقت نطلب فيه كائن Java من JVM. تحسب المراجع كجذور لجامع القمامة التي تمنع جمع القمامة المتحمس. من أجل الأداء، المراجع المحلية لها نطاق مقيد: فهي محلية تماماً للخيط ولا تنجو أبداً من إطار الاستدعاء الذي تم إنشاؤها فيه. يمكن فرض كلا القيدين على استخدامها بالأنواع الخطية.

الوصول المباشر للذاكرة عن بُعد. القسم 5.1 هو مثال على واجهة برمجة تطبيقات تتطلب نمط تمرير الوجهة. يظهر هذا النمط غالباً في السياقات الحساسة للأداء. أحد الأمثلة البارزة من تجربتنا الصناعية هو RDMA (الوصول المباشر للذاكرة عن بُعد)، والذي يمكّن الأجهزة في مجموعات عالية الأداء من نسخ البيانات من مساحة العنوان في عملية واحدة إلى تلك الخاصة بعملية بعيدة مباشرة، متجاوزة النواة وحتى وحدة المعالجة المركزية، وبالتالي تجنب أي نسخة غير ضرورية في العملية.

يمكن للمرء أن يعامل موقع ذاكرة عن بُعد كمورد منخفض المستوى، يتم الوصول إليه باستخدام واجهة برمجة تطبيقات إلزامية. باستخدام الأنواع الخطية، يمكن للمرء بدلاً من ذلك معاملته كقيمة عالية المستوى يمكن الكتابة إليها مباشرة (ولكن مرة واحدة بالضبط). باستخدام الأنواع الخطية، يمكن للمترجم التأكد من أنه بمجرد اكتمال عملية الكتابة، يتم إخطار الكمبيوتر الوجهة.

---

### Translation Notes

- **Key topics:**
  - Compiler optimizations (تحسينات المترجم)
  - Inlining and cardinality analysis (الإدراج وتحليل العددية)
  - Extended multiplicities (التعدديات الموسعة)
  - Borrowing (الاستعارة)
  - Industrial applications (التطبيقات الصناعية)
- **Technical terms:**
  - Streaming I/O (الإدخال/الإخراج الانسيابي)
  - Foreign heaps (الأكوام الأجنبية)
  - RDMA - Remote Direct Memory Access (الوصول المباشر للذاكرة عن بُعد)
  - JVM/JNI references (مراجع JVM/JNI)
  - Destination-passing style (نمط تمرير الوجهة)
- **Future work areas:** Three main categories (optimizations, type extensions, applications)

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.85
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.85
