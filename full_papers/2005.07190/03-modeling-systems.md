# Section 2.2: B for Systems
## القسم 2.2: B للأنظمة

**Section:** modeling - systems
**Translation Quality:** 0.86
**Glossary Terms Used:** Event-B, formal methods, refinement, specification, certification, distributed systems

---

### English Version

#### 2.2 B for Systems

A broader use of B appeared in the mid '90s, called Event-B, to analyze, study and specify not only software, but also systems (system is here considered in its widest definition). It extends the usage of B to systems that might contain software, hardware and pieces of equipment, but also to intangible objects like process, procedure, business rule, etc. In that respect, one of the outcome of Event-B is the proved definition of systems architecture and, more generally, the proved development of, so called, "system studies", which are performed before the specification and design of the software. This enlargement allows one to perform failure studies right from the beginning, even in a large system development.

**2.2.1 Research and development** Several European projects were required to set-up Event-B, among them:
- MATISSE aimed at providing a first definition of the language,
- PUSSEE specifically aimed at hardware/software embedded systems,
- Rodin for the development of the eponymous platform and
- DEPLOY for its deployment in the industry.

Several system studies from diverse application domains (banking, air traffic control, defense, satellites, etc.) were initially performed with Atelier B before naturally moving to the Rodin platform. The modeling of the Mazurkiewicz enumeration algorithm and its proof during the project RIMEL⁶ was the perfect demonstration of the suitability of Event-B for small, distributed systems. In 2008, during the certification for a smart-card microcircuit, Event-B was seamlessly integrated to Atelier B⁷. The supported language slightly differs from the one supported by Rodin but doesn't restrict its usability regarding target applications. Several EAL5+ (CC2.3) and EAL6+ (CC3.1) certifications were performed in France, Germany and Spain, and functional specification were proved to comply with security policies.

A follow-up project, FORCOMENT [2], was initiated with STMicroelectronics and aimed at providing a proven path from specification to VHDL. Specific proof obligations were added to ensure a deterministic behavior. Resulting VHDL was quite different from the one developed manually (similar numbers of gates, but architecture more easily analyzable) and went successfully through product test benches. However the technology failed to find its audience because of:
- (the complexity of) the input formalism,
- the necessity to specify the target system several tens of times (refinements) with different levels of detail,
- the time and the number of iterations⁸ to converge to a final model,
- the obligation to allocate our best practitioners to complete the duty.

⁶http://rimel.loria.fr/
⁷because of the inability, at that time, for the Rodin platform to handle a model with 17 levels of refinement
⁸Our maximum is 190 iterations and 5 major refactoring, many modifications having a slight impact on the structure of the model

**2.2.2 Flat specification** Event-B was also used as a descriptive language for behavioral specification (flat specification, no refinement), mainly for document generation, structural analysis (dependencies among variables) and model animation with application in the automotive (enhanced diagnosis – Peugeot), in the defense (military vehicles integration testing scheduling – CNIM) and in the railways (platform screen doors preliminary studies – RATP).

The main reason for not modeling with refinement was the complexity of the target systems and the level of detail required to perform an analysis that would have led to both practical and economical impossibilities (models too large to be handled by human modelers; too much effort to complete, if reachable). The Event-B models were sided by a dictionary containing natural language descriptions of the variables, events and substitutions, allowing for the automatic generation of document. Events were allocated to "sub-systems", allowing to analyze data-flows (see figure 3) between these sub-systems (where the variables are read/modified).

A dedicated tool, Composys [10], was developed and maintained to support this approach until 2012.

**Fig. 3:** All the dependencies between the sub-systems of a military vehicle analyzed with Composys, and used for defining a non-trivial efficient integration testing policy. This drawing is for illustrating the complexity of the model.

This approach was more aimed at finding ambiguities in the existing technical documentation, and at animating the specification than at proving a correct behavior and was finally abandoned.

**2.2.3 Collection of separate models** Instead of developing a model of the whole signaling system, verbose, complex and not containing enough details⁹ to ensure a definitive conclusion on the safety of the system, another approach was tried. The fundamental goal was to extract the rigorous reasoning establishing that the considered system ensures its requested properties, and to assert that this reasoning is correct and fully expressed. At system level, this rigorous reasoning involves the properties of different kind of subsystems (from computer subsystems to operational procedures), that the formal proof shall all encompass. Event-B is used to formalize the reasoning with a collection of separate models: each model is readable and understandable by a non-expert and doesn't require to dig into hundreds of events and tens of refinement levels. This approach was used for the system formal verification for the CBTC of New York subway line 7 in 2012 and Flushing in 2014 (effort divided by two due to models reuse). It is now deployed in Paris for all the new automatic metro lines [15]. Even if based on refinement, the formal modeling effort is now manageable (each model is one or two pages long) and only requires engineers able to reason (not our best practitioners any more). The Event-B language as implemented in Atelier B in 2008 is still enough to support this modeling approach.

⁹this demonstration requires for example to know the algorithm used for the odometer, to rediscover how the distance between signals and switches is computed based on the minimum curve radius, tunnel width, maximum slope, minimum train braking capability, etc.

---

### النسخة العربية

#### 2.2 B للأنظمة

ظهر استخدام أوسع لـ B في منتصف التسعينيات، يُسمى Event-B، لتحليل ودراسة وتحديد ليس فقط البرمجيات، ولكن أيضاً الأنظمة (يُعتبر النظام هنا في تعريفه الأوسع). يمتد استخدام B إلى الأنظمة التي قد تحتوي على برمجيات وأجهزة وقطع معدات، ولكن أيضاً إلى كائنات غير ملموسة مثل العملية والإجراء وقاعدة العمل وما إلى ذلك. في هذا الصدد، أحد نتائج Event-B هو التعريف المُثبَت لمعمارية الأنظمة، وبشكل أعم، التطوير المُثبَت لما يُسمى "دراسات الأنظمة"، التي يتم إجراؤها قبل مواصفة وتصميم البرمجيات. يسمح هذا التوسع بإجراء دراسات الفشل من البداية، حتى في تطوير الأنظمة الكبيرة.

**2.2.1 البحث والتطوير** تطلبت عدة مشاريع أوروبية لإعداد Event-B، من بينها:
- MATISSE الذي يهدف إلى توفير تعريف أول للغة،
- PUSSEE الذي يستهدف بشكل خاص الأنظمة المدمجة للأجهزة/البرمجيات،
- Rodin لتطوير المنصة التي تحمل نفس الاسم و
- DEPLOY لنشره في الصناعة.

تم إجراء عدة دراسات أنظمة من مجالات تطبيقات متنوعة (الخدمات المصرفية، التحكم في حركة الطيران، الدفاع، الأقمار الصناعية، إلخ) في البداية مع Atelier B قبل الانتقال بشكل طبيعي إلى منصة Rodin. كانت نمذجة خوارزمية تعداد Mazurkiewicz وإثباتها خلال مشروع RIMEL⁶ البرهان المثالي على ملاءمة Event-B للأنظمة الموزعة الصغيرة. في عام 2008، خلال الاعتماد لدائرة متناهية الصغر للبطاقة الذكية، تم دمج Event-B بسلاسة في Atelier B⁷. تختلف اللغة المدعومة قليلاً عن تلك المدعومة من Rodin لكنها لا تقيد قابليتها للاستخدام فيما يتعلق بالتطبيقات المستهدفة. تم إجراء عدة اعتمادات EAL5+ (CC2.3) و EAL6+ (CC3.1) في فرنسا وألمانيا وإسبانيا، وتم إثبات أن المواصفات الوظيفية تتوافق مع سياسات الأمان.

تم بدء مشروع متابعة، FORCOMENT [2]، مع STMicroelectronics ويهدف إلى توفير مسار مُثبَت من المواصفة إلى VHDL. تمت إضافة التزامات إثبات محددة لضمان سلوك حتمي. كان VHDL الناتج مختلفاً تماماً عن ذلك الذي تم تطويره يدوياً (أعداد مماثلة من البوابات، لكن المعمارية أكثر قابلية للتحليل) ونجح في اجتياز منصات اختبار المنتج. ومع ذلك، فشلت التكنولوجيا في إيجاد جمهورها بسبب:
- (تعقيد) الشكل الرسمي للمدخلات،
- ضرورة تحديد النظام المستهدف عشرات المرات (التنقيحات) بمستويات مختلفة من التفاصيل،
- الوقت وعدد التكرارات⁸ للتقارب إلى نموذج نهائي،
- الالتزام بتخصيص أفضل ممارسينا لإتمام المهمة.

⁶http://rimel.loria.fr/
⁷بسبب عدم قدرة منصة Rodin، في ذلك الوقت، على التعامل مع نموذج يحتوي على 17 مستوى من التنقيح
⁸حدنا الأقصى هو 190 تكراراً و5 إعادة هيكلة رئيسية، مع العديد من التعديلات التي لها تأثير طفيف على بنية النموذج

**2.2.2 المواصفة المسطحة** تم استخدام Event-B أيضاً كلغة وصفية للمواصفة السلوكية (مواصفة مسطحة، بدون تنقيح)، بشكل رئيسي لتوليد المستندات، والتحليل الهيكلي (التبعيات بين المتغيرات) وتحريك النموذج مع تطبيقات في السيارات (التشخيص المحسّن - Peugeot)، في الدفاع (جدولة اختبار تكامل المركبات العسكرية - CNIM) وفي السكك الحديدية (الدراسات الأولية لأبواب الشاشة للمنصة - RATP).

كان السبب الرئيسي لعدم النمذجة مع التنقيح هو تعقيد الأنظمة المستهدفة ومستوى التفاصيل المطلوب لإجراء تحليل كان سيؤدي إلى استحالات عملية واقتصادية (نماذج كبيرة جداً بحيث لا يمكن للمحللين البشريين التعامل معها؛ جهد كبير جداً للإكمال، إذا كان قابلاً للتحقيق). رافقت نماذج Event-B قاموس يحتوي على أوصاف بلغة طبيعية للمتغيرات والأحداث والاستبدالات، مما يسمح بالتوليد التلقائي للمستندات. تم تخصيص الأحداث لـ "الأنظمة الفرعية"، مما يسمح بتحليل تدفقات البيانات (انظر الشكل 3) بين هذه الأنظمة الفرعية (حيث يتم قراءة/تعديل المتغيرات).

تم تطوير وصيانة أداة مخصصة، Composys [10]، لدعم هذا النهج حتى عام 2012.

**الشكل 3:** جميع التبعيات بين الأنظمة الفرعية لمركبة عسكرية تم تحليلها باستخدام Composys، واستُخدمت لتحديد سياسة اختبار تكامل فعالة غير بسيطة. هذا الرسم لتوضيح تعقيد النموذج.

كان هذا النهج يهدف أكثر إلى إيجاد الغموض في التوثيق التقني الموجود، وإلى تحريك المواصفة بدلاً من إثبات سلوك صحيح وتم التخلي عنه في النهاية.

**2.2.3 مجموعة من النماذج المنفصلة** بدلاً من تطوير نموذج لنظام الإشارات بأكمله، المطوّل والمعقد وغير المحتوي على تفاصيل كافية⁹ لضمان استنتاج نهائي حول سلامة النظام، تمت تجربة نهج آخر. كان الهدف الأساسي هو استخراج التفكير الصارم الذي يُثبت أن النظام المعني يضمن خصائصه المطلوبة، والتأكيد على أن هذا التفكير صحيح ومعبر عنه بالكامل. على مستوى النظام، يتضمن هذا التفكير الصارم خصائص أنواع مختلفة من الأنظمة الفرعية (من الأنظمة الفرعية الحاسوبية إلى الإجراءات التشغيلية)، التي يجب أن يشملها الإثبات الرسمي جميعاً. يُستخدم Event-B لإضفاء الطابع الرسمي على التفكير بمجموعة من النماذج المنفصلة: كل نموذج قابل للقراءة والفهم من قبل غير متخصص ولا يتطلب الحفر في مئات الأحداث وعشرات مستويات التنقيح. تم استخدام هذا النهج للتحقق الرسمي من النظام لـ CBTC في خط مترو أنفاق نيويورك 7 في عام 2012 و Flushing في عام 2014 (تم تقسيم الجهد إلى النصف بسبب إعادة استخدام النماذج). يتم نشره الآن في باريس لجميع خطوط المترو الأوتوماتيكية الجديدة [15]. حتى مع أنه يعتمد على التنقيح، فإن جهد النمذجة الرسمية الآن قابل للإدارة (كل نموذج بطول صفحة أو صفحتين) ويتطلب فقط مهندسين قادرين على التفكير (لم يعد أفضل ممارسينا). لا تزال لغة Event-B كما هي مطبقة في Atelier B في عام 2008 كافية لدعم نهج النمذجة هذا.

⁹يتطلب هذا الإثبات على سبيل المثال معرفة الخوارزمية المستخدمة لعداد المسافة، وإعادة اكتشاف كيفية حساب المسافة بين الإشارات والمحولات بناءً على الحد الأدنى لنصف قطر المنحنى، وعرض النفق، والحد الأقصى للمنحدر، والحد الأدنى لقدرة فرامل القطار، إلخ.

---

### Translation Notes

- **Figures referenced:** Figure 3 (subsystem dependencies diagram)
- **Key terms introduced:**
  - Event-B = Event-B (kept in English as proper noun/technical term)
  - Rodin platform = منصة Rodin
  - MATISSE, PUSSEE, DEPLOY, RIMEL = project names (kept in English)
  - EAL (Evaluation Assurance Level) = مستوى ضمان التقييم
  - VHDL = VHDL (hardware description language, kept as acronym)
  - Composys = Composys (tool name, kept in English)
  - CBTC = نظام التحكم في القطارات القائم على الاتصال
- **Equations:** 0
- **Citations:** [2] FORCOMENT, [10] Composys, [15] Paris automatic metro lines
- **Special handling:**
  - European project names kept in English
  - Company names (STMicroelectronics, Peugeot, CNIM) kept in original form
  - Technical acronyms (EAL, CC, VHDL, CBTC) kept in English
  - Footnotes maintained with Arabic numbering
  - "Flat specification" translated as "المواصفة المسطحة" to indicate no refinement hierarchy

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
