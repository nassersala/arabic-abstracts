# Section 2.1: B for Software
## القسم 2.1: B للبرمجيات

**Section:** modeling - software
**Translation Quality:** 0.87
**Glossary Terms Used:** formal methods, B method, safety-critical, proof obligations, abstraction, refinement, validation, implementation

---

### English Version

#### 2.1 B for Software

The B Method was introduced in the late 80's to correctly design safe software. The main idea was to avoid introducing errors by proving the software while being built, instead of trying to find errors with testing after the software was produced.

Promoted and supported by RATP, B and Atelier B¹ have been successfully applied to the industry of transportation, through metros automatic pilots installed worldwide. Paris Meteor line 14 driverless metro is the first reference application with over 110,000 lines of B models, translated into 86,000 lines of Ada. No bugs were detected after the proof was completed, neither at the functional validation, at the integration validation, and at the on-site testing, nor since the beginning of the metro line operation (October 1998).

For years, Alstom Transportation Systems and Siemens Transportation Systems (representing a major part of the worldwide metro market) have been the two main actors in the development of B safety-critical software. Both companies have a product based strategy and reuse as much as possible existing B models for future metros. As an example, the Alstom Urbalis 400 CBTC (Radio communication based train control) equips more than 100 metros in the world, representing 1250 km of lines and 25% of the CBTC market.

**2.1.1 Structure and metrics** For such applications, B modeling is used for safety critical functions for both track-side (zone controller, interlocking) and on-board (automatic train pilot or ATP) software. The interlocking part has to avoid having two trains on the same track section. It computes boolean equations that represent the tracks status as seen from diverse sensors. The automatic pilot is mainly in charge of triggering the emergency brake in case of over-speed. It requires several functions such as the localization (where is the train?) that involve several graph-based algorithms, and the energy control which computes the braking curve of the train, based on the geometry of the tracks (in particular the positive and negative slopes). Data types used are: integer for the energy control, booleans for the interlocking and tables of integer for the tracks.

¹the tool implementing the B method

A typical ATP software model is made of one top-level function executed every cycle.

**Fig. 1:** Example of a non-deterministic post-condition of a function

The specification of this function (see figure 1) is non-deterministic and is expressed as a large "variables become such as" substitution. The specification of the function, contained in the post-condition, is sufficiently abstract and different from the implementation² to avoid to prove the copy-paste from the specification to the implementation. This implementation imports 55 components. The complete B project is made of 233 machines (50 kloc³), 46 intermediate refinements (6 kloc) and 213 implementations (45 kloc), as well the handwritten code for non-safety critical parts (110 kloc). It also contains 3000 definitions reused among several components. 23,000 proof obligations are generated, 83% of these of proved automatically, the remaining 17% requires interactive proof. 3000 mathematical rules were added to ease the proof process, 85% of these are proved automatically, the remaining 15% requires human manual proof.

To date, the biggest B software is a XML compiler enabling the execution of safety critical embedded applications by an interpreter. More than 300,000 lines of Ada code are generated from B models, for this SIL4 T3-compliant (EN50128) program⁴. 300,000 lines do not represent the limit of the method as no bottleneck has been met until now. So the method is likely to scale up to larger, non-threaded software. At the other end of the scale, with platform screen doors controllers less demanding in term of computation, smaller applications are generated for both programmable logic controllers (PLC) and PIC32 microcontrollers, with a maximum of 64 KB in memory per software.

²which contains the algorithm (statements, operation calls)
³thousands lines of code
⁴T3 means that the tool is able to generate a (faulty) binary program and as such requires a special attention in the safety process

**2.1.2 Organization and acceptance** Since 1998, Atelier B has been slightly improved in order to obtain proven software more quickly:
- proof obligations (PO) contain traceability information (which parts of the B models have been used to obtain a PO), helping to better locate modeling errors and to improve modeling style
- a model editor allowing to navigate models (abstraction, refinement) and operations (caller, callee)
- a model editor merging model and proof (see figure 2) by displaying the number of proof obligations associated to any line of a B model, its current proof status (fully proved or not) and the body of the related proof obligations.
- a framework to automatically prove and review user added mathematical proof rules, that generates a report for the safety case.

From a human point-of-view, usual organization requires a local guru acting as a technical referee (usually - but not necessarily - a PhD) and a team of software engineers able to handle abstraction. Introductory B courses (B language, projects with B) and close support during the first months have been enough to set up development teams. The forthcoming MOOC on B⁵ and a dedicated YouTube channel for Atelier B practitioners would speed up the learning process.

⁵https://moocs.imd.ufrn.br

**Fig. 2:** Text-based model editor combining proof information with modeling

The B software development process is now well-oiled, accepted by certification bodies and several rail operators worldwide. Without being formally developed, Atelier B 3.6 was used for METEOR in 1998 while Atelier B 4.2/4.3 is used for Alstom Urbalis 400/500 product line. Atelier B 4.2 is at the core of the SIL4 certificate obtained for the platform screen-doors controller installed in 2017 in Stockholm (line Citybanan).

---

### النسخة العربية

#### 2.1 B للبرمجيات

تم تقديم أسلوب B في أواخر الثمانينيات لتصميم البرمجيات الآمنة بشكل صحيح. كانت الفكرة الرئيسية هي تجنب إدخال الأخطاء من خلال إثبات البرمجيات أثناء بنائها، بدلاً من محاولة إيجاد الأخطاء بالاختبار بعد إنتاج البرمجيات.

بدعم وترويج من RATP، تم تطبيق B و Atelier B¹ بنجاح في صناعة النقل، من خلال الطيارين الآليين للمترو المثبتة في جميع أنحاء العالم. يعد مترو باريس Meteor الخط 14 بدون سائق التطبيق المرجعي الأول مع أكثر من 110,000 سطر من نماذج B، مترجمة إلى 86,000 سطر من Ada. لم يتم اكتشاف أي أخطاء بعد اكتمال الإثبات، لا في التحقق من الصحة الوظيفية، ولا في التحقق من التكامل، ولا في الاختبار في الموقع، ولا منذ بداية تشغيل خط المترو (أكتوبر 1998).

لسنوات عديدة، كانت أنظمة Alstom Transportation و Siemens Transportation Systems (التي تمثل جزءاً كبيراً من سوق المترو العالمي) الفاعلَين الرئيسيَّين في تطوير برمجيات B الحرجة من حيث السلامة. تتبع كلتا الشركتين استراتيجية قائمة على المنتج وتعيد استخدام نماذج B الموجودة قدر الإمكان للمترو المستقبلي. كمثال، يُجهز Alstom Urbalis 400 CBTC (التحكم في القطارات القائم على الاتصال الراديوي) أكثر من 100 مترو في العالم، يمثل 1250 كم من الخطوط و25% من سوق CBTC.

**2.1.1 البنية والمقاييس** في مثل هذه التطبيقات، تُستخدم نمذجة B للوظائف الحرجة من حيث السلامة لكل من البرمجيات الجانبية للمسار (متحكم المنطقة، الترابط) والبرمجيات على متن القطار (الطيار الآلي للقطار أو ATP). يجب على جزء الترابط تجنب وجود قطارين على نفس قسم المسار. يحسب معادلات منطقية تمثل حالة المسارات كما تُرى من مستشعرات متنوعة. الطيار الآلي مسؤول بشكل رئيسي عن تفعيل الفرامل الطارئة في حالة السرعة الزائدة. يتطلب عدة وظائف مثل التحديد الموضعي (أين يوجد القطار؟) التي تتضمن عدة خوارزميات قائمة على الرسوم البيانية، والتحكم في الطاقة الذي يحسب منحنى الفرملة للقطار، بناءً على هندسة المسارات (خاصة المنحدرات الموجبة والسالبة). أنواع البيانات المستخدمة هي: الأعداد الصحيحة للتحكم في الطاقة، والقيم المنطقية للترابط، وجداول الأعداد الصحيحة للمسارات.

¹الأداة التي تنفذ أسلوب B

يتكون نموذج برمجيات ATP النموذجي من دالة واحدة على المستوى الأعلى يتم تنفيذها في كل دورة.

**الشكل 1:** مثال على شرط لاحق غير حتمي لدالة

مواصفة هذه الدالة (انظر الشكل 1) غير حتمية ويتم التعبير عنها كاستبدال كبير من نوع "المتغيرات تصبح بحيث". مواصفة الدالة، الموجودة في الشرط اللاحق، مجردة بما يكفي ومختلفة عن التطبيق² لتجنب إثبات النسخ واللصق من المواصفة إلى التطبيق. يستورد هذا التطبيق 55 مكوناً. يتكون مشروع B الكامل من 233 آلة (50 ألف سطر³)، و46 تنقيحاً وسيطاً (6 آلاف سطر) و213 تطبيقاً (45 ألف سطر)، بالإضافة إلى الكود المكتوب يدوياً للأجزاء غير الحرجة من حيث السلامة (110 ألف سطر). يحتوي أيضاً على 3000 تعريف مُعاد استخدامها بين عدة مكونات. يتم توليد 23,000 التزام إثبات، 83% منها تُثبَت تلقائياً، والنسبة المتبقية 17% تتطلب إثباتاً تفاعلياً. تم إضافة 3000 قاعدة رياضية لتسهيل عملية الإثبات، 85% منها تُثبَت تلقائياً، والنسبة المتبقية 15% تتطلب إثباتاً يدوياً بشرياً.

حتى الآن، أكبر برنامج B هو مُجمِّع XML يمكّن من تنفيذ التطبيقات المدمجة الحرجة من حيث السلامة بواسطة مفسر. يتم توليد أكثر من 300,000 سطر من كود Ada من نماذج B، لهذا البرنامج المتوافق مع SIL4 T3 (EN50128)⁴. لا تمثل 300,000 سطر حد الأسلوب حيث لم يتم مواجهة أي عنق زجاجة حتى الآن. لذا من المرجح أن يتوسع الأسلوب إلى برمجيات أكبر وغير متعددة الخيوط. في الطرف الآخر من النطاق، مع متحكمات أبواب الشاشة للمنصة الأقل تطلباً من حيث الحساب، يتم توليد تطبيقات أصغر لكل من متحكمات المنطق القابلة للبرمجة (PLC) ومتحكمات PIC32 الدقيقة، بحد أقصى 64 كيلوبايت في الذاكرة لكل برنامج.

²الذي يحتوي على الخوارزمية (التعليمات، استدعاءات العمليات)
³آلاف أسطر الكود
⁴T3 يعني أن الأداة قادرة على توليد برنامج ثنائي (معيب) وعلى هذا النحو تتطلب اهتماماً خاصاً في عملية السلامة

**2.1.2 التنظيم والقبول** منذ عام 1998، تم تحسين Atelier B قليلاً للحصول على برمجيات مُثبتة بشكل أسرع:
- تحتوي التزامات الإثبات (PO) على معلومات التتبع (أي أجزاء نماذج B تم استخدامها للحصول على PO)، مما يساعد على تحديد أخطاء النمذجة بشكل أفضل وتحسين أسلوب النمذجة
- محرر نماذج يسمح بالتنقل في النماذج (التجريد، التنقيح) والعمليات (المُستدعي، المُستدعى)
- محرر نماذج يدمج النموذج والإثبات (انظر الشكل 2) من خلال عرض عدد التزامات الإثبات المرتبطة بأي سطر من نموذج B، وحالة الإثبات الحالية له (مُثبَت بالكامل أم لا) ومتن التزامات الإثبات ذات الصلة
- إطار عمل لإثبات ومراجعة قواعد الإثبات الرياضية المضافة من المستخدم تلقائياً، والذي ينشئ تقريراً لحالة السلامة

من وجهة نظر بشرية، يتطلب التنظيم المعتاد وجود خبير محلي يعمل كحكم تقني (عادة - ولكن ليس بالضرورة - حاصل على درجة الدكتوراه) وفريق من مهندسي البرمجيات القادرين على التعامل مع التجريد. كانت دورات B التمهيدية (لغة B، المشاريع مع B) والدعم الوثيق خلال الأشهر الأولى كافية لإعداد فرق التطوير. من شأن دورة MOOC القادمة على B⁵ وقناة YouTube مخصصة لممارسي Atelier B أن تُسرّع عملية التعلم.

⁵https://moocs.imd.ufrn.br

**الشكل 2:** محرر نماذج نصي يجمع معلومات الإثبات مع النمذجة

عملية تطوير برمجيات B الآن محكمة التشغيل، ومقبولة من قبل هيئات الاعتماد والعديد من مشغلي السكك الحديدية في جميع أنحاء العالم. دون أن يتم تطويره رسمياً، تم استخدام Atelier B 3.6 لـ METEOR في عام 1998 بينما يُستخدم Atelier B 4.2/4.3 لخط إنتاج Alstom Urbalis 400/500. يقع Atelier B 4.2 في قلب شهادة SIL4 التي تم الحصول عليها لمتحكم أبواب الشاشة للمنصة المثبت في عام 2017 في ستوكهولم (خط Citybanan).

---

### Translation Notes

- **Figures referenced:** Figure 1 (non-deterministic post-condition), Figure 2 (model editor)
- **Key terms introduced:**
  - Atelier B = أداة تنفذ أسلوب B
  - RATP = هيئة نقل باريس
  - ATP (Automatic Train Pilot) = الطيار الآلي للقطار
  - CBTC = التحكم في القطارات القائم على الاتصال الراديوي
  - PO (Proof Obligations) = التزامات الإثبات
  - kloc = آلاف أسطر الكود
  - SIL4 = مستوى تكامل السلامة 4
  - PLC = متحكمات المنطق القابلة للبرمجة
- **Equations:** 0
- **Citations:** References to RATP, Alstom, Siemens, EN50128 standard
- **Special handling:**
  - Company names (RATP, Alstom, Siemens) kept in English
  - Tool names (Atelier B) kept in English as proper nouns
  - Standards (SIL4, EN50128) kept as acronyms
  - Technical metrics preserved (110,000 lines, 300,000 lines, etc.)
  - Footnotes maintained with Arabic numbering

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
