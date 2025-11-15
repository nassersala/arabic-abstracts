# Section 7: Related Work
## القسم 7: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.87
**Glossary Terms Used:** domain specific language (لغة خاصة بالمجال), verification (التحقق), model-driven engineering (الهندسة المدفوعة بالنماذج), automated verification (التحقق الآلي), formal methods (الأساليب الرسمية), bounded model checking (فحص النماذج المحدود)

---

### English Version

At this point, we reflect on other DSL based approaches for railway verification, commenting on how they differ to our presented methodology.

The Railway Control Systems Domain language (RCSD) is a DSL for railway control systems developed by Kirsten Mewes. RCSD is motivated by model-driven engineering approaches to system design. The language uses common domain notation for its concrete syntax and incorporates knowledge from domain engineers about the domain into its static and dynamic semantics. Mewes also considers the topic of testing models created in DSL. Here, domain specific constraints are included into the models ensuring that validation checks for correct functionality can be tested at the model level, before any software is been developed. Mewes' work focuses on the design of RCSD. In contrast, we leave the design of the DSL to the domain engineer and focus on capturing domain knowledge that can be exploited for automatic verification.

Work by Haxthausen and Peleska has also explored the development of a domain specific framework for automated construction and verification of railway control systems. Their framework consists of a three tiered approach: the top layer is a DSL for use by domain engineers to specify railway control systems; the second tier is model generation: A generator automatically produces the model of a control program based on the specification given by the design engineer. Bounded model checking can then be performed to establish various safety properties over such programs; the third tier allows actual code to be automatically generated and verified to ensure certain properties are maintained throughout process. Differing to our work, this framework is specifically developed for the railway domain and tied to a specific DSL. In this paper, we provide a generic and systematic methodology, where the railway domain serves for illustration.

Finally, the SafeCap toolset provides a tooling platform that supports reasoning about railway capacity whilst ensuring system safety. It is based upon the SafeCap DSL, which captures track topology, route and path definitions and signalling rules. Overall, the toolset allows signalling engineers to design stations and junctions, to check their safety and to evaluate the potential improvements in capacity. Again, the SafeCap approach is bound to a specific DSL, where the design of the DSL is tailored to the underlying verification technology (Event B). This differs from our aim to decouple the DSL from the formal specification language, in turn allowing tooling environments to be very openly extendable.

---

### النسخة العربية

في هذه النقطة، نتأمل في نُهج أخرى قائمة على اللغات الخاصة بالمجال للتحقق من السكك الحديدية، معلقين على كيفية اختلافها عن منهجيتنا المقدمة.

لغة مجال أنظمة التحكم في السكك الحديدية (RCSD) هي لغة خاصة بالمجال لأنظمة التحكم في السكك الحديدية طورتها Kirsten Mewes. تُحفَّز RCSD بنُهج الهندسة المدفوعة بالنماذج لتصميم الأنظمة. تستخدم اللغة الترميز الشائع للمجال لبناءها الملموس وتدمج المعرفة من مهندسي المجال حول المجال في دلالاتها الثابتة والديناميكية. تنظر Mewes أيضًا في موضوع اختبار النماذج المُنشأة في اللغة الخاصة بالمجال. هنا، يتم تضمين القيود الخاصة بالمجال في النماذج لضمان إمكانية اختبار فحوصات التحقق من الصحة للوظيفة الصحيحة على مستوى النموذج، قبل تطوير أي برنامج. يركز عمل Mewes على تصميم RCSD. في المقابل، نترك تصميم اللغة الخاصة بالمجال لمهندس المجال ونركز على التقاط معرفة المجال التي يمكن استغلالها للتحقق التلقائي.

استكشف عمل Haxthausen و Peleska أيضًا تطوير إطار عمل خاص بالمجال للبناء الآلي والتحقق من أنظمة التحكم في السكك الحديدية. يتكون إطار عملهم من نهج ثلاثي الطبقات: الطبقة العليا هي لغة خاصة بالمجال لاستخدامها من قبل مهندسي المجال لتحديد أنظمة التحكم في السكك الحديدية؛ الطبقة الثانية هي توليد النموذج: يُنتج المولد تلقائيًا نموذج برنامج التحكم بناءً على المواصفات المقدمة من قبل مهندس التصميم. يمكن بعد ذلك إجراء فحص النماذج المحدود لإنشاء خصائص السلامة المختلفة على مثل هذه البرامج؛ تسمح الطبقة الثالثة بتوليد الشفرة الفعلية تلقائيًا والتحقق منها لضمان الحفاظ على خصائص معينة طوال العملية. على عكس عملنا، تم تطوير هذا الإطار خصيصًا لمجال السكك الحديدية ومرتبط بلغة خاصة بالمجال محددة. في هذا البحث، نقدم منهجية عامة ومنهجية، حيث يعمل مجال السكك الحديدية للتوضيح.

أخيرًا، توفر مجموعة أدوات SafeCap منصة أدوات تدعم الاستدلال حول سعة السكك الحديدية مع ضمان سلامة النظام. تستند إلى لغة SafeCap الخاصة بالمجال، والتي تلتقط طوبولوجيا المسار، وتعريفات المسار والطريق، وقواعد الإشارات. بشكل عام، تسمح مجموعة الأدوات لمهندسي الإشارات بتصميم المحطات والتقاطعات، والتحقق من سلامتها، وتقييم التحسينات المحتملة في السعة. مرة أخرى، يرتبط نهج SafeCap بلغة خاصة بالمجال محددة، حيث يتم تصميم اللغة الخاصة بالمجال لتناسب تقنية التحقق الأساسية (Event B). يختلف هذا عن هدفنا في فصل اللغة الخاصة بالمجال عن لغة المواصفات الرسمية، مما يسمح بدوره ببيئات الأدوات القابلة للتوسع بشكل مفتوح للغاية.

---

### Translation Notes

- **Key systems/tools mentioned:**
  - RCSD (Railway Control Systems Domain language)
  - SafeCap toolset
  - Event B
  - Framework by Haxthausen and Peleska
- **Key comparison points:**
  - DSL design approach
  - Domain knowledge capture
  - Generic vs. domain-specific methodology
  - Coupling/decoupling of DSL and verification technology
- **Citations:** Multiple references to related research work

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
