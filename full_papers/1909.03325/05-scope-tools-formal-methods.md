# Section 5: The Scope of Tools and Formal Methods
## القسم 5: نطاق الأدوات والأساليب الرسمية

**Section:** scope-tools-formal-methods
**Translation Quality:** 0.86
**Glossary Terms Used:** formal methods (الأساليب الرسمية), static verification (التحقق الساكن), taint analysis (تحليل التلويث), memory corruption (فساد الذاكرة), sandboxing (العزل), filtering (التصفية)

---

### English Version

There is a substantial range of tools, and degrees of formality, and [15, §6] is probably correct in saying "We doubt theres a one-size-fits-all approach". At one extreme, there are the humble, but still surprisingly effective, lint and its equivalents, looking, essentially, for dangerous or dubious, though legal, syntax.

**5.1 Ada and SPARK**

At the other extreme, there are languages, such as the SPARK Ada subset [17] designed with verification in mind and heavily employed in the safety-critical sector such as railways and air traffic control, which can also be deployed for demanding secure applications, such as an RFC4108-compliant [31] secure download system for embedded systems [16].

**5.2 C/C++**

There is, however, a large middle ground between these two extremes. Even if the application is required to be in C or C++, there is a lot to be said for sticking to a safer (even if not provably safe) subset of the language and associated libraries, such as eschewing strcpy in favour of strncpy. This can often be enforced by static verification tools. We note that Google's "Zero Day" project reports [26] that 68% of all such zero-day exploits (i.e. exploits discovered in the wild first) were caused by memory corruption errors, and Microsoft report a very similar story [68].

There is a good survey of such subsets and standards in [14, Appendix F]. As that notes, the ISO standard for secure C coding [34] has the unusual (for this middle ground) but important concept of "taint analysis" (as in [40]): input data should be considered "tainted" until it has been sanitised. This is particularly important for network-oriented applications, where it is natural for the programmer to believe that the other party is behaving correctly (see Heartbleed above).

**5.3 Java**

Closer to the SPARK Ada end of the spectrum we find Safety-Critical Java [13]. The author does not have enough experience with this to comment directly. However, the Java ecosystem (Stack Overflow etc.) is far from security-aware [44]. The fact that an application is in Java doesn't mean it's free from security coding errors: see [25] for a recent example.

There is a static analysis security tool for Java described in [40]. As with [34], this has "taint analysis" as its major feature, and at the time it spotted some significant-seeming problems.

**5.4 JavaScript**

JavaScript is a particular problem for Security. There are some verification tools, e.g. GATEKEEPER as described in [27]. However, even if it were possible to guarantee a particular piece of stand-alone JavaScript, that is not how the current paradigm operates. As [45] writes:

> Much of the power of modern Web comes from the ability of a Web page to combine content and JavaScript code from disparate servers on the same page. While the ability to create such mash-ups is attractive for both the user and the developer because of extra functionality, code inclusion effectively opens the hosting site up for attacks and poor programming practices within every JavaScript library or API it chooses to use.

Though not explicit in this statement, an additional weakness is that this combination is dynamic. The obvious solution would be some kind of sandboxing of the external resources relied upon, but the nature of JavaScript makes this difficult. [41] describe one such sandboxing, but it only works for a subset of JavaScript and relies on a combination of filtering, rewriting and wrapping to guarantee security. That it can do so at all is a remarkable feat of formal methods, given that previous attempts such as Facebook's FBJS have subtle flaws [42], and that the formal semantics of JavaScript being relied upon are very much a piece of reverse engineering.

In fact the dynamic loading from multiple sites is often not good for performance, and web performance engineers recommend tools to bundle the pages: this could usefully be combined with the sort of protection described by [41].

An alternative solution is used by Google, who are introducing a form of taint analysis into Chrome [36] through run-time typing. When enabled, this means that the 60+ dangerous DOM API functions can only be called with arguments whose type is that emitted by TrustedTypes functions. Google expects that these functions would be manually verified, but this does open the door to formal verification of certain security policies in what is currently a very challenging environment for formal methods. We note the complex interaction between the server and the client.

---

### النسخة العربية

هناك نطاق كبير من الأدوات، ودرجات من الرسمية، و [15، §6] ربما صحيح في قوله "نشك في وجود نهج واحد يناسب الجميع". في أحد الطرفين، توجد أدوات lint المتواضعة، ولكن الفعالة بشكل مدهش، ومعادلاتها، التي تبحث، في الأساس، عن بناء جملة خطير أو مشكوك فيه، وإن كان قانونياً.

**5.1 Ada و SPARK**

في الطرف الآخر، توجد لغات، مثل مجموعة فرعية SPARK Ada [17] المصممة مع وضع التحقق في الاعتبار والمستخدمة بكثافة في القطاع الحرج من حيث السلامة مثل السكك الحديدية ومراقبة الحركة الجوية، والتي يمكن أيضاً نشرها للتطبيقات الآمنة الصعبة، مثل نظام التنزيل الآمن المتوافق مع RFC4108 [31] للأنظمة المدمجة [16].

**5.2 C/C++**

ومع ذلك، هناك أرضية وسطى كبيرة بين هذين الطرفين. حتى لو كان التطبيق مطلوباً أن يكون بلغة C أو C++، هناك الكثير مما يمكن قوله للالتزام بمجموعة فرعية أكثر أماناً (حتى لو لم تكن آمنة بشكل قابل للإثبات) من اللغة والمكتبات المرتبطة بها، مثل تجنب strcpy لصالح strncpy. يمكن غالباً فرض ذلك بواسطة أدوات التحقق الساكن. نلاحظ أن مشروع "Zero Day" من Google يذكر [26] أن 68٪ من جميع استغلالات اليوم الصفري هذه (أي الاستغلالات المكتشفة في البرية أولاً) كانت بسبب أخطاء فساد الذاكرة، وتذكر Microsoft قصة مماثلة جداً [68].

هناك مسح جيد لهذه المجموعات الفرعية والمعايير في [14، الملحق F]. كما تلاحظ ذلك، فإن معيار ISO للبرمجة الآمنة بلغة C [34] له مفهوم غير عادي (لهذه الأرضية الوسطى) ولكنه مهم وهو "تحليل التلويث" (كما في [40]): يجب اعتبار بيانات الإدخال "ملوثة" حتى يتم تعقيمها. هذا مهم بشكل خاص للتطبيقات الموجهة للشبكات، حيث من الطبيعي للمبرمج أن يعتقد أن الطرف الآخر يتصرف بشكل صحيح (انظر Heartbleed أعلاه).

**5.3 Java**

أقرب إلى طرف SPARK Ada من الطيف نجد Java الحرجة من حيث السلامة [13]. ليس لدى المؤلف خبرة كافية مع هذا للتعليق مباشرة. ومع ذلك، فإن نظام Java البيئي (Stack Overflow وما إلى ذلك) بعيد عن الوعي الأمني [44]. حقيقة أن التطبيق بلغة Java لا تعني أنه خالٍ من أخطاء البرمجة الأمنية: انظر [25] لمثال حديث.

هناك أداة تحليل ساكن للأمان لـ Java موصوفة في [40]. كما هو الحال مع [34]، فإن "تحليل التلويث" هو ميزتها الرئيسية، وفي ذلك الوقت اكتشفت بعض المشاكل التي تبدو كبيرة.

**5.4 JavaScript**

JavaScript مشكلة خاصة للأمن. هناك بعض أدوات التحقق، مثل GATEKEEPER كما هو موصوف في [27]. ومع ذلك، حتى لو كان من الممكن ضمان قطعة معينة من JavaScript المستقلة، فهذه ليست الطريقة التي يعمل بها النموذج الحالي. كما تكتب [45]:

> الكثير من قوة الويب الحديث يأتي من قدرة صفحة الويب على الجمع بين المحتوى وكود JavaScript من خوادم متباينة على نفس الصفحة. في حين أن القدرة على إنشاء مثل هذه المزج جذابة لكل من المستخدم والمطور بسبب الوظائف الإضافية، فإن تضمين الكود يفتح فعلياً الموقع المضيف للهجمات وممارسات البرمجة السيئة ضمن كل مكتبة JavaScript أو API يختار استخدامها.

على الرغم من عدم وضوح ذلك في هذا البيان، فإن نقطة ضعف إضافية هي أن هذا الجمع ديناميكي. سيكون الحل الواضح نوعاً من العزل للموارد الخارجية المعتمد عليها، لكن طبيعة JavaScript تجعل هذا صعباً. [41] تصف أحد هذه العزل، لكنه يعمل فقط لمجموعة فرعية من JavaScript ويعتمد على مزيج من التصفية وإعادة الكتابة والتغليف لضمان الأمان. أن تتمكن من القيام بذلك على الإطلاق هو إنجاز رائع للأساليب الرسمية، بالنظر إلى أن المحاولات السابقة مثل FBJS من Facebook لديها عيوب دقيقة [42]، وأن الدلالات الرسمية لـ JavaScript المعتمد عليها هي إلى حد كبير قطعة من الهندسة العكسية.

في الواقع، التحميل الديناميكي من مواقع متعددة غالباً ليس جيداً للأداء، ويوصي مهندسو أداء الويب بأدوات لتجميع الصفحات: يمكن الجمع بين هذا بشكل مفيد مع نوع الحماية الموصوفة بواسطة [41].

يتم استخدام حل بديل من قبل Google، التي تقدم شكلاً من أشكال تحليل التلويث في Chrome [36] من خلال الكتابة في وقت التشغيل. عند تمكين ذلك، هذا يعني أن الوظائف الخطرة لـ DOM API البالغ عددها أكثر من 60 يمكن استدعاؤها فقط بمعاملات من النوع الصادر من وظائف TrustedTypes. تتوقع Google أن يتم التحقق من هذه الوظائف يدوياً، لكن هذا يفتح الباب للتحقق الرسمي من سياسات أمنية معينة في ما هو حالياً بيئة صعبة للغاية للأساليب الرسمية. نلاحظ التفاعل المعقد بين الخادم والعميل.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** SPARK Ada, safety-critical sector, zero-day exploits, memory corruption, taint analysis, Safety-Critical Java, JavaScript mash-ups, sandboxing, filtering/rewriting/wrapping, DOM API, TrustedTypes
- **Equations:** 0
- **Citations:** [13], [14], [16], [17], [25], [26], [27], [31], [34], [36], [40], [41], [42], [44], [45], [68]
- **Special handling:** Programming language names (Ada, SPARK, C, C++, Java, JavaScript) kept in English; function names (strcpy, strncpy) preserved; technical terms like GATEKEEPER, FBJS, TrustedTypes, DOM API kept in English as proper names; percentages and statistics (68%, 60+) preserved

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
