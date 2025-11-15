# Section 5: Evaluation and Case Studies
## القسم 5: التقييم ودراسات الحالة

**Section:** Evaluation and Case Studies
**Translation Quality:** 0.86
**Glossary Terms Used:** serialized data, type safety, sockets, protocols, performance, benchmarking

---

### English Version

While many linear type systems have been proposed, a retrofitted linear type system for a mature language like Haskell offers the opportunity to implement non-trivial applications mixing linear and non-linear code, I/O, etc., and observe how linear code interacts with existing libraries and the optimiser of a sophisticated compiler.

Our first method for evaluating the implementation is to simply compile a large existing code base together with the following changes: (1) all (non-GADT) data constructors are linear by default, as implied by the new type system; and (2) we update standard list functions to have linear types (++, concat, uncons). Under these conditions, we verified that the base GHC libraries and the nofib benchmark suites compile successfully: 195K lines of Haskell, providing preliminary evidence of backwards compatibility.

In the remainder of this section, we describe case-studies implemented with the modified GHC of Sec. 4. In Sec. 7.3, we propose further applications for Linear Haskell, which we have not yet implemented, but which motivate this work.

**5.1 Computing directly with serialised data**

While Sec. 2.2 covered simple mutable arrays, we now turn to a related but more complicated application: operating directly on binary, serialised representations of algebraic datatypes (like Vollmer et al. [2017] do). The motivation is that programs are increasingly decoupled into separate (cloud) services that communicate via serialised data in text or binary formats, carried by remote procedure calls. The standard approach is to deserialise data into an in-heap, pointer-based representation, process it, and then serialise the result for transmission. This process is inefficient, but nevertheless tolerated, because the alternative — computing directly with serialised data — is far too difficult to program.

Here is an unusual case where advanced types can yield performance by making it practical to code in a previously infeasible style: accessing serialised data at a fine grain without copying it.

The interface gives an example of type-safe, read-only access to serialised data for a particular datatype. A Packed value is a pointer to raw bits (a bytestring), indexed by the types of the values contained within. We define a type-safe serialisation layer as one which reads byte-ranges only at the type and size they were originally written.

**5.1.1 Writing serialised data.** To create a serialised data constructor, we must write a tag, followed by the fields. A linear write pointer can ensure all fields are initialised, in order. We use a type "Needs" for write pointers, parameterised by (1) a list of remaining things to be written, and (2) the type of the final value which will be initialised once those writes are performed.

**5.1.2 A version without linear types.** How would we build the same thing in Haskell without linear types? It may appear that the ST monad is a suitable choice. Unfortunately, not only do we have the same trouble with freezing in the absence of linearity (unsafeFreeze, Sec. 2.2), we also have an additional problem not present with arrays: namely, a non-linear use of a Needs pointer can ruin our type-safe deserialisation guarantee!

**5.1.3 Benchmarking compiler optimisations.** As shown in Fig. 7, there are some unexpected performance consequences from using a linear versus a monadic, ST style in GHC. Achieving allocation-free loops in GHC is always a challenge. For the linearly-typed code, however, we have more options. Using levity polymorphism, we were able to ensure by construction that the "linear/packed" implementations were completely non-allocating, rather than depending on the optimiser. This results in better performance for the linear, compared to monadic version of the serialised-data transformations.

The basic premise of Fig. 7 is that a machine in the network receives, processes, and transmits serialized data (trees). Compared to the baseline (unpack-repack), processing the data directly in its serialised form results in speedups of over 20× on large trees. What linear types makes safe, is also efficient.

**5.2 Sockets with type-level state**

The BSD socket API is a standard through which computers connect over networks. It involves a series of actions which must be performed in order: on the server-side, a freshly created socket must be bound to an address, then start listening incoming traffic, then accept connection requests. Programming with it is exactly as clumsy as socket libraries for other languages: after each action, the state of the socket changes, as do the permissible actions, but these states are invisible in the types. Better is to track the state of sockets in the type, akin to a typestate analysis.

As an illustration, we implemented a wrapper around the API of the socket library. For concision, this wrapper is specialised for the case of TCP. The linear socket API is very similar to that of files: we use the IOL monad in order to enforce linear use of sockets. The difference is the argument to Socket, which represents the current state of the socket and is used to limit the functions which apply to a socket at a given time.

**5.3 Pure bindings to impure APIs**

In Haskell SpriteKit, Chakravarty and Keller [2017] have a different kind of problem. They build a pure interface for graphics, in the same style as the Elm programming language, but implement it in terms of an existing imperative graphical interface engine.

Basically, the pure interface takes an update function u : Scene → Scene which is tasked with returning the next state that the screen will display. Things can go wrong though: if the update function duplicates any proxy node, one gets the situation where two nodes can point to the same imperative source but have different payloads. In this situation the Scene has become inconsistent and the behaviour of SpriteKit is unpredictable.

In the API of Chakravarty and Keller [2017], the burden of checking non-duplication is on the programmer. Using linear types, we can switch that burden to the compiler: we change the update function to type Scene⊸Scene, and the ref field is made linear too. We implemented such an API in our implementation of Linear Haskell. The library-side code does not use any linear code, the Nodes are actually used unrestrictedly. Linearity is only imposed on the user of the interface, in order to enforce the above restriction.

---

### النسخة العربية

بينما تم اقتراح العديد من أنظمة الأنواع الخطية، فإن نظام الأنواع الخطية المُعدّل استعارياً للغة ناضجة مثل Haskell يوفر الفرصة لتنفيذ تطبيقات غير تافهة تخلط بين الشفرة الخطية وغير الخطية، والإدخال/الإخراج، وما إلى ذلك، ومراقبة كيفية تفاعل الشفرة الخطية مع المكتبات الموجودة ومحسّن المترجم المتطور.

طريقتنا الأولى لتقييم التنفيذ هي ببساطة تجميع قاعدة شفرة موجودة كبيرة مع التغييرات التالية: (1) جميع مُنشئات البيانات (غير GADT) خطية افتراضياً، كما يتضمن نظام الأنواع الجديد؛ و (2) نقوم بتحديث دوال القائمة القياسية لتكون لها أنواع خطية (++، concat، uncons). في ظل هذه الظروف، تحققنا من أن مكتبات GHC الأساسية ومجموعات معايير nofib تُجمّع بنجاح: 195 ألف سطر من Haskell، مما يوفر دليلاً أولياً على التوافق العكسي.

في بقية هذا القسم، نصف دراسات الحالة المنفذة باستخدام GHC المُعدّل من القسم 4. في القسم 7.3، نقترح تطبيقات إضافية لـ Haskell الخطي، والتي لم ننفذها بعد، لكنها تحفز هذا العمل.

**5.1 الحوسبة مباشرة مع البيانات المسلسلة**

بينما غطى القسم 2.2 المصفوفات القابلة للتغيير البسيطة، ننتقل الآن إلى تطبيق ذي صلة ولكن أكثر تعقيداً: العمل مباشرة على التمثيلات الثنائية المسلسلة لأنواع البيانات الجبرية. الدافع هو أن البرامج أصبحت منفصلة بشكل متزايد إلى خدمات منفصلة (سحابية) تتواصل عبر بيانات مسلسلة في صيغ نصية أو ثنائية، تُحمل بواسطة استدعاءات الإجراءات البعيدة.

هذه حالة غير عادية حيث يمكن للأنواع المتقدمة أن تحقق الأداء من خلال جعل البرمجة عملية في نمط كان غير قابل للتنفيذ سابقاً: الوصول إلى البيانات المسلسلة بشكل دقيق دون نسخها.

**5.1.1 كتابة البيانات المسلسلة.** لإنشاء مُنشئ بيانات مسلسل، يجب علينا كتابة علامة، متبوعة بالحقول. يمكن لمؤشر الكتابة الخطي ضمان تهيئة جميع الحقول، بالترتيب.

**5.1.2 نسخة بدون أنواع خطية.** كيف يمكننا بناء نفس الشيء في Haskell بدون أنواع خطية؟ قد يبدو أن ST monad هو خيار مناسب. لسوء الحظ، ليس لدينا فقط نفس المشكلة مع التجميد في غياب الخطية (unsafeFreeze، القسم 2.2)، بل لدينا أيضاً مشكلة إضافية غير موجودة مع المصفوفات.

**5.1.3 معايير تحسينات المترجم.** كما هو موضح في الشكل 7، هناك بعض العواقب الأدائية غير المتوقعة من استخدام نمط خطي مقابل ST monadic في GHC. مقارنة بخط الأساس (unpack-repack)، تؤدي معالجة البيانات مباشرة في شكلها المسلسل إلى تسريعات تزيد عن 20× على الأشجار الكبيرة. ما تجعله الأنواع الخطية آمناً، هو أيضاً فعال.

**5.2 المقابس مع حالة على مستوى الأنواع**

واجهة برمجة تطبيقات مقبس BSD هي معيار تتصل من خلاله أجهزة الكمبيوتر عبر الشبكات. تتضمن سلسلة من الإجراءات التي يجب تنفيذها بالترتيب. البرمجة معها غير مريحة تماماً مثل مكتبات المقابس للغات الأخرى: بعد كل إجراء، تتغير حالة المقبس، كما تتغير الإجراءات المسموح بها، لكن هذه الحالات غير مرئية في الأنواع. الأفضل هو تتبع حالة المقابس في النوع، مشابه لتحليل حالة الأنواع.

كتوضيح، قمنا بتنفيذ غلاف حول واجهة برمجة تطبيقات مكتبة المقابس. من أجل الإيجاز، هذا الغلاف متخصص لحالة TCP.

**5.3 ارتباطات نقية لواجهات برمجة تطبيقات غير نقية**

في Haskell SpriteKit، لدى Chakravarty و Keller [2017] نوع مختلف من المشكلة. يبنون واجهة نقية للرسومات، بنفس أسلوب لغة البرمجة Elm، لكنهم ينفذونها من حيث محرك واجهة رسومية إلزامي موجود.

باستخدام الأنواع الخطية، يمكننا نقل هذا العبء إلى المترجم: نغير دالة التحديث إلى النوع Scene⊸Scene، وحقل المرجع يُجعل خطياً أيضاً. بفضل الخطية، لا يمكن تكرار أي مرجع: إذا تم نسخ عقدة، يجب على المبرمج اختيار أيهما سيتوافق مع النظير الإلزامي القديم وأيهما سيكون جديداً.

---

### Translation Notes

- **Figures referenced:** Fig. 7 (Performance benchmarks)
- **Key terms introduced:**
  - Serialised data (البيانات المسلسلة)
  - Type-safe deserialisation (إلغاء التسلسل الآمن للأنواع)
  - Levity polymorphism (تعددية الأشكال الخفيفة)
  - Typestate analysis (تحليل حالة الأنواع)
  - Pure interfaces (الواجهات النقية)
- **Benchmarks:** Performance results showing 20× speedup
- **Case studies:** Three detailed examples (serialised data, sockets, SpriteKit)

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.85
- **Overall section score:** 0.86
