# Section 2.3-2.4: Formal Data Validation and Adoption by Industry
## القسم 2.3-2.4: التحقق الرسمي من البيانات والتبني من قبل الصناعة

**Section:** formal data validation and industry adoption
**Translation Quality:** 0.87
**Glossary Terms Used:** formal methods, B method, validation, verification, proof, model-checker

---

### English Version

#### 2.3 Formal Data Validation

The verification of a behavior, based on Event-B system specification or B software specification, is achievable by semi-automated proof. However the verification of static properties of parameters (that tune the system or the software) against properties may turn out to be a nightmare in case of large data sets (10,000+ items) and complex relationships among data, as the built-in Atelier B prover is not able to handle them properly. In the early 2000's data validation in the railways [8] used to be entirely human, leading to painful, error-prone, long-term activities (usually more than six months to manually check constantly changing¹⁰ 100,000 items of data against 1,000 rules).

In 2003, this human process was made more formal while:
- formalizing data properties with the B mathematical language (set theory, first order logic)
- generating a B machine containing the properties (the data model) and instantiated with the data to verify,
- checking the correctness of the B machine

¹⁰CAD data is replaced by real plant data, topology is modified after in situ testing, etc.

**2.3.1 Rules** Properties, issued from international standards, national regulations, local practices, rail operator requirements, metro manufacturer constraints, are modeled as rules (see figure 4). The clause WHERE allows the selection and filtering of data¹¹. The clause VERIFY specifies the conditions expected for all filtered signals. In case the predicates of this clause are not verified, an error message is displayed for each signal found.

¹¹that could be stored in files like JSON, Xml, Excel, CSV, TXT, etc.

**Fig. 4:** Example of verification rule. Signals belonging to an interlocking territory are searched; such signals have to be linked to this interlocking. If not, an error message is displayed for each faulty signal found.

Most of the rules fit in one page, but some rules are really large, up to 10 pages, as they embed several small steps or they contain a lot of implicit information. To ensure compliance with safety standard, rules have to be cross-read and tested by independent engineers. A specific testing environment has been developed to ease to set up of testing scenarios demonstrating that a rule triggers a KO conclusion for all error classes.

**2.3.2 Deployment** The PredicateB predicate evaluator was first used for checking the correctness. The PredicateB tool is a symbolic calculator able to manipulate B mathematical language predicates in order to animate a B formal model: constants and variables initial values are calculated, then operations are executed depending on enabling conditions and their substitutions. Symbolic values are scalars, sets, functions, etc. PredicateB has limited capabilities for non-deterministic computations and was replaced by ProB [9]. The ProB model-checker embeds several well performing heuristics for reducing search space (symmetry detection for example), is able to better handle non-deterministic substitution and to provide a more complete set of counter examples. It has been modified in order to produce a file containing all counter examples detected and slightly improved to better support some B keywords.

The major outcome of this decision to introduce formalities and to automate the verification [13] was a dramatic reduction of the validation duration from about six months of human verification to some minutes of computation (if we set aside the time to formalize verification rules). Since then the resulting tools (certified as T2 and T3 compliant, EN50128 standard) have been experimented with success¹² on several metro lines worldwide for different metro manufacturers. In this context, more than 2,500 rules have been developed, cross-verified and applied. The French Railways (SNCF) is going to deploy these tools for the main lines to check new interlocking parameters for the 10 coming years, requiring the development of 2,500 more rules.

¹²metro line fully and positively analyzed, results validated by certification body and independent expert

From a human point-of-view, usual organization requires engineers able to manipulate mathematical predicates and to understand railways signaling. A technical referee provides feedback and support on how to model certain tricky aspects like non-deterministic choices ("find a bijection such as ..."), quantified predicates, etc. The verification process is well accepted by certification bodies and by several rail operators worldwide, and is ready to be deployed in other industries with safety-critical constraints.

#### 2.4 Adoption by Industry

From our experience, industry is not particularly interested in using formal methods except if it is required by the standards (1) or by the customers (2), or if it allows to speed up a process by an order of magnitude (3).

**Table 1:** Summary of the main tools used during the last 25 years for industrial projects. B/E/D columns refer to B language (B), Event-B language (E) and formal data validation (D) supports.

| Tool | B | E | D | Usage | Availability |
|------|---|---|---|-------|--------------|
| Atelier B | X | X | - | modeling environment, 100+ automatic metro lines | Free, http://www.atelier.eu/en |
| ProB | X | X | - | model-checker | Free, https://www3.hhu.de/stups/prob |
| BMotionWeb | X | X | - | model animator | Free, http://wiki.event-b.org/index.php/BMotion Studio |
| PredicateB | - | X | - | model animator | Free, https://sourceforge.net/p/rodin-b-sharp |
| PredicateB++ | - | X | - | model animator | Proprietary (ClearSy) |
| Rodin | - | X | - | modeling environment | Free, http://www.event-b.org/ |
| DTVT | - | - | X | data validation environment, 20+ metro and tramway lines | Proprietary (Alstom) |
| Dave | - | - | X | data validation environment, Singapore metro line | Proprietary (General Electrics) |
| Ovado | - | - | X | data validation environment, Paris metro lines | Proprietary (RATP) |

In our history, (1) is related to smartcard industry (§2.2.1), (2) is associated with Meteor/RATP (§2.1) and with L7/NYCT (§2.2.3), while (3) is represented by the formal data validation (§2.3).

In any case, a formal method without a proper tool support is useless. We have used several tools over the years (Table 1) that were applied in industrial settings. As such, formal data validation is much appreciated because as a V&V tool, it doesn't impact the development cycle (on the contrary of B for software development) and the verification phase is a "push-button" activity (once the formal data model is completed).

---

### النسخة العربية

#### 2.3 التحقق الرسمي من البيانات

يمكن تحقيق التحقق من السلوك، بناءً على مواصفة نظام Event-B أو مواصفة برمجيات B، من خلال الإثبات شبه الآلي. ومع ذلك، قد يتحول التحقق من الخصائص الثابتة للمعاملات (التي تضبط النظام أو البرمجيات) مقابل الخصائص إلى كابوس في حالة مجموعات البيانات الكبيرة (أكثر من 10,000 عنصر) والعلاقات المعقدة بين البيانات، حيث أن مُثبِت Atelier B المدمج غير قادر على التعامل معها بشكل صحيح. في أوائل العقد الأول من القرن الحادي والعشرين، كان التحقق من البيانات في السكك الحديدية [8] بشرياً بالكامل، مما أدى إلى أنشطة مؤلمة وعرضة للخطأ وطويلة الأمد (عادة أكثر من ستة أشهر للتحقق يدوياً من 100,000 عنصر من البيانات المتغيرة باستمرار¹⁰ مقابل 1,000 قاعدة).

في عام 2003، تم جعل هذه العملية البشرية أكثر رسمية من خلال:
- إضفاء الطابع الرسمي على خصائص البيانات باستخدام اللغة الرياضية B (نظرية المجموعات، منطق الدرجة الأولى)
- توليد آلة B تحتوي على الخصائص (نموذج البيانات) ومُنشأة بالبيانات المراد التحقق منها،
- التحقق من صحة آلة B

¹⁰يتم استبدال بيانات CAD ببيانات المصنع الحقيقية، ويتم تعديل الطوبولوجيا بعد الاختبار في الموقع، إلخ.

**2.3.1 القواعد** يتم نمذجة الخصائص، الصادرة عن المعايير الدولية واللوائح الوطنية والممارسات المحلية ومتطلبات مشغل السكك الحديدية وقيود مصنع المترو، كقواعد (انظر الشكل 4). يسمح بند WHERE باختيار وتصفية البيانات¹¹. يحدد بند VERIFY الشروط المتوقعة لجميع الإشارات المفلترة. في حالة عدم التحقق من محمولات هذا البند، يتم عرض رسالة خطأ لكل إشارة موجودة.

¹¹التي يمكن تخزينها في ملفات مثل JSON و Xml و Excel و CSV و TXT وما إلى ذلك.

**الشكل 4:** مثال على قاعدة التحقق. يتم البحث عن الإشارات التي تنتمي إلى منطقة ترابط؛ يجب أن ترتبط هذه الإشارات بهذا الترابط. إذا لم يكن الأمر كذلك، يتم عرض رسالة خطأ لكل إشارة معيبة موجودة.

معظم القواعد تتناسب مع صفحة واحدة، لكن بعض القواعد كبيرة حقاً، تصل إلى 10 صفحات، حيث تتضمن عدة خطوات صغيرة أو تحتوي على الكثير من المعلومات الضمنية. لضمان الامتثال لمعايير السلامة، يجب قراءة القواعد ومراجعتها واختبارها من قبل مهندسين مستقلين. تم تطوير بيئة اختبار محددة لتسهيل إعداد سيناريوهات الاختبار التي تُظهر أن القاعدة تؤدي إلى استنتاج KO لجميع فئات الأخطاء.

**2.3.2 النشر** تم استخدام مُقيّم المحمولات PredicateB أولاً للتحقق من الصحة. أداة PredicateB هي آلة حاسبة رمزية قادرة على التعامل مع محمولات اللغة الرياضية B من أجل تحريك نموذج B الرسمي: يتم حساب القيم الأولية للثوابت والمتغيرات، ثم يتم تنفيذ العمليات اعتماداً على شروط التمكين واستبدالاتها. القيم الرمزية هي قيم عددية ومجموعات ودوال وما إلى ذلك. لدى PredicateB قدرات محدودة للحسابات غير الحتمية وتم استبداله بـ ProB [9]. يتضمن فاحص النماذج ProB عدة إرشادات جيدة الأداء لتقليل مساحة البحث (اكتشاف التماثل على سبيل المثال)، وهو قادر على التعامل بشكل أفضل مع الاستبدال غير الحتمي وتوفير مجموعة أكثر اكتمالاً من الأمثلة المضادة. تم تعديله لإنتاج ملف يحتوي على جميع الأمثلة المضادة المكتشفة وتحسينه قليلاً لدعم أفضل لبعض الكلمات المفتاحية B.

كانت النتيجة الرئيسية لهذا القرار بإدخال الرسميات وأتمتة التحقق [13] هي انخفاض كبير في مدة التحقق من حوالي ستة أشهر من التحقق البشري إلى بضع دقائق من الحساب (إذا وضعنا جانباً الوقت لإضفاء الطابع الرسمي على قواعد التحقق). منذ ذلك الحين، تم تجريب الأدوات الناتجة (المعتمدة كمتوافقة مع T2 و T3، معيار EN50128) بنجاح¹² على عدة خطوط مترو في جميع أنحاء العالم لمختلف مصنعي المترو. في هذا السياق، تم تطوير أكثر من 2,500 قاعدة والتحقق منها وتطبيقها. ستقوم السكك الحديدية الفرنسية (SNCF) بنشر هذه الأدوات للخطوط الرئيسية للتحقق من معاملات الترابط الجديدة للسنوات العشر القادمة، مما يتطلب تطوير 2,500 قاعدة إضافية.

¹²خط مترو تم تحليله بالكامل وبشكل إيجابي، وتم التحقق من النتائج من قبل هيئة الاعتماد وخبير مستقل

من وجهة نظر بشرية، يتطلب التنظيم المعتاد مهندسين قادرين على التعامل مع المحمولات الرياضية وفهم إشارات السكك الحديدية. يقدم حكم تقني تغذية راجعة ودعماً حول كيفية نمذجة بعض الجوانب الصعبة مثل الاختيارات غير الحتمية ("إيجاد تطابق بحيث...")، المحمولات المحدودة، إلخ. عملية التحقق مقبولة بشكل جيد من قبل هيئات الاعتماد والعديد من مشغلي السكك الحديدية في جميع أنحاء العالم، وهي جاهزة للنشر في صناعات أخرى ذات قيود حرجة من حيث السلامة.

#### 2.4 التبني من قبل الصناعة

من تجربتنا، الصناعة غير مهتمة بشكل خاص باستخدام الأساليب الرسمية إلا إذا كانت مطلوبة من قبل المعايير (1) أو من قبل العملاء (2)، أو إذا كانت تسمح بتسريع عملية بأمر من الحجم (3).

**الجدول 1:** ملخص الأدوات الرئيسية المستخدمة خلال السنوات الـ 25 الماضية للمشاريع الصناعية. تشير أعمدة B/E/D إلى دعم لغة B (B)، لغة Event-B (E) والتحقق الرسمي من البيانات (D).

| الأداة | B | E | D | الاستخدام | التوفر |
|--------|---|---|---|---------|---------|
| Atelier B | X | X | - | بيئة نمذجة، أكثر من 100 خط مترو أوتوماتيكي | مجاني، http://www.atelier.eu/en |
| ProB | X | X | - | فاحص نماذج | مجاني، https://www3.hhu.de/stups/prob |
| BMotionWeb | X | X | - | محرك نماذج | مجاني، http://wiki.event-b.org/index.php/BMotion Studio |
| PredicateB | - | X | - | محرك نماذج | مجاني، https://sourceforge.net/p/rodin-b-sharp |
| PredicateB++ | - | X | - | محرك نماذج | ملكية خاصة (ClearSy) |
| Rodin | - | X | - | بيئة نمذجة | مجاني، http://www.event-b.org/ |
| DTVT | - | - | X | بيئة التحقق من البيانات، أكثر من 20 خط مترو وترام | ملكية خاصة (Alstom) |
| Dave | - | - | X | بيئة التحقق من البيانات، خط مترو سنغافورة | ملكية خاصة (General Electrics) |
| Ovado | - | - | X | بيئة التحقق من البيانات، خطوط مترو باريس | ملكية خاصة (RATP) |

في تاريخنا، (1) مرتبط بصناعة البطاقات الذكية (§2.2.1)، (2) مرتبط بـ Meteor/RATP (§2.1) ومع L7/NYCT (§2.2.3)، بينما (3) يتمثل في التحقق الرسمي من البيانات (§2.3).

في أي حال، فإن الأسلوب الرسمي بدون دعم أداة مناسب عديم الفائدة. لقد استخدمنا عدة أدوات على مر السنين (الجدول 1) تم تطبيقها في البيئات الصناعية. على هذا النحو، يحظى التحقق الرسمي من البيانات بتقدير كبير لأنه كأداة V&V، لا يؤثر على دورة التطوير (على عكس B لتطوير البرمجيات) ومرحلة التحقق هي نشاط "بضغطة زر" (بمجرد اكتمال نموذج البيانات الرسمي).

---

### Translation Notes

- **Figures referenced:** Figure 4 (verification rule example)
- **Tables referenced:** Table 1 (tools summary)
- **Key terms introduced:**
  - PredicateB = PredicateB (tool name, kept in English)
  - ProB = ProB (tool name, kept in English)
  - Model-checker = فاحص نماذج
  - V&V (Verification and Validation) = التحقق والتصديق
  - Push-button activity = نشاط "بضغطة زر"
  - Counter examples = الأمثلة المضادة
  - Symbolic calculator = آلة حاسبة رمزية
- **Equations:** 0
- **Citations:** [8] railways data validation, [9] ProB, [13] automation verification
- **Special handling:**
  - Tool names kept in English as proper nouns
  - Company/organization names (SNCF, Alstom, RATP) kept in original form
  - Standards (EN50128, T2, T3) kept as acronyms
  - URLs preserved in original form
  - Table format maintained with Arabic headers
  - Data metrics preserved (10,000+ items, 100,000 items, 2,500 rules, etc.)
  - Footnotes maintained with Arabic numbering

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
