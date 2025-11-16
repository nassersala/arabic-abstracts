# Section 1: Introduction
## القسم 1: المقدمة

**Section:** Introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** formal methods (الأساليب الرسمية), formal verification (التحقق الرسمي), automated theorem prover (مُثبِت نظريات آلي), safety-critical (حرجة من حيث السلامة), certification (اعتماد), avionics (إلكترونيات الطيران), development process (عملية التطوير)

---

### English Version

Recent advances in automated theorem provers have brought formal methods from purely academic exercises close to industrial use. Airborne software has early been recognized as a suitable candidate for the application of formal methods [14, 21]. Airbus, for example, has examined the formal method Caveat to replace unit tests [15]. Since Airbus is a trend setter in the avionics industry at least in Europe, one can expect the obligation to use formal methods for the development of highly safety critical airborne software in future. Moreover, standard organizations start to incorporate formal methods into their regulations as one can already see with the formal methods supplement DO-333 [12] of the new version of the avionics software certification guidelines, DO-178C [11]. Another well-known example is the Common Criteria for Information Technology Security Evaluation that demand the use of formal methods for the highest Evaluation Assurance Levels EAL 6 and EAL 7 [9]. It is probably safe to assume that more and more development standards will mandate the application of formal methods in the future. This will force also small and medium enterprises (SME) that develop safety critical software to consider the adoption of formal methods in the long run.

ESG as a medium sized company that develops airborne system solutions has therefore launched a small experimental study to examine if formal verification can be integrated into its development processes for airborne software, and to identify the prerequisites for an adoption of formal methods in future DO-178C compliant software projects.

In Germany, the Verisoft XT project [6] examined the application of formal methods in an industrial context. ESG participated in a work package of that project that examined the application of formal methods in the avionics domain [7]. This experimental study is a continuation of ESG's work in that project.

ACSL is an acronym for "ANSI C Specification Language" provided for the open source tool platform Frama-C [2, 10]. It is a behavioral specification language that can express properties of C source code including pre-conditions and post-conditions of C functions using first order logic. The ACSL specifications are provided as annotations to the source code. The WP plug-in of the framework allows a deductive verification of the source code against the formal annotations in ACSL [3].

DO-178C defines Low-Level Requirements (LLR) as software requirements from which source code can be directly implemented without further information. In the software projects we have been involved in, these requirements were natural language annotations to the subroutines or function declarations provided by the interfaces of the software modules. It is therefore natural to consider ACSL as a candidate to formally express the low-level requirements.

Several so-called DO-178C objectives are associated with low-level requirements that must be fulfilled for acceptance of the software by certification authorities. One such objective is the verifiability of low-level requirements. This objective is indeed achieved when a formal notation is used. Another objective is the compliance of the source code with the low-level requirements, which is usually shown by code review. These time consuming reviews may be replaced by automated formal verification. Blasum et al [7] discuss these and other DO-178C objectives for the formal methods of the Verisoft XT project.

The major goal of the study was to check if formal notations can be used in a real project to formally express real world low level requirements, i.e. to see if a certain formal method is fit for use in industrial practice in general and for ESG in particular. A secondary goal was to examine if available tools can verify such annotated code and even be able to find bugs not yet discovered by testing, which would prove one of the claimed advantages of formal methods over testing.

The first step was to establish criteria which a formal notation and its supporting tools should meet in order to be ready for industrial use in an SME setting. In a second step, we selected a function from a real avionics project and formalized the natural language specifications of the associated C functions into ACSL specifications. It was in this step that we encountered the first obstacles although the selected function was rather trivial.

These obstacles are, in our view, quite typical for embedded real-time programming. The problems were solved with support of Frama-C experts via the Frama-C mailing list. However, the solutions are not fully satisfactory which may be inherent to the approach, as it will be discussed later.

In a next step, we attempted to verify the source code against the ACSL specification while instrumenting the source code with assertions in order to guide the prover. Not all verification attempts were successful. We were only able to explain some of the failed attempts before running out of time. In a final step, we compared our experience in using tool and method against the formerly established criteria.

---

### النسخة العربية

أدت التطورات الحديثة في مُثبِتات النظريات الآلية إلى نقل الأساليب الرسمية من كونها مجرد تمارين أكاديمية بحتة إلى قربها من الاستخدام الصناعي. تم الاعتراف مبكراً بالبرمجيات المحمولة جواً كمرشح مناسب لتطبيق الأساليب الرسمية [14، 21]. على سبيل المثال، فحصت شركة Airbus الأسلوب الرسمي Caveat لاستبدال اختبارات الوحدات [15]. وبما أن Airbus تُعد رائدة في صناعة إلكترونيات الطيران على الأقل في أوروبا، يمكن توقع إلزامية استخدام الأساليب الرسمية لتطوير البرمجيات المحمولة جواً شديدة الحرجة من حيث السلامة في المستقبل. علاوة على ذلك، بدأت المنظمات المعيارية في إدراج الأساليب الرسمية في لوائحها كما يمكن ملاحظة ذلك بالفعل في الملحق الخاص بالأساليب الرسمية DO-333 [12] من الإصدار الجديد لإرشادات اعتماد برمجيات إلكترونيات الطيران، DO-178C [11]. مثال آخر معروف هو المعايير المشتركة لتقييم أمن تكنولوجيا المعلومات التي تتطلب استخدام الأساليب الرسمية لأعلى مستويات ضمان التقييم EAL 6 و EAL 7 [9]. من المحتمل أن يكون من الآمن افتراض أن المزيد والمزيد من معايير التطوير ستفرض تطبيق الأساليب الرسمية في المستقبل. وهذا سيجبر أيضاً الشركات الصغيرة والمتوسطة التي تطور برمجيات حرجة من حيث السلامة على النظر في اعتماد الأساليب الرسمية على المدى الطويل.

لذلك أطلقت شركة ESG، كشركة متوسطة الحجم تطور حلول الأنظمة المحمولة جواً، دراسة تجريبية صغيرة لفحص ما إذا كان يمكن دمج التحقق الرسمي في عمليات تطويرها للبرمجيات المحمولة جواً، ولتحديد المتطلبات الأساسية لاعتماد الأساليب الرسمية في مشاريع البرمجيات المتوافقة مع DO-178C في المستقبل.

في ألمانيا، فحص مشروع Verisoft XT [6] تطبيق الأساليب الرسمية في سياق صناعي. شاركت ESG في حزمة عمل من ذلك المشروع فحصت تطبيق الأساليب الرسمية في مجال إلكترونيات الطيران [7]. هذه الدراسة التجريبية هي استمرار لعمل ESG في ذلك المشروع.

ACSL هو اختصار لـ "ANSI C Specification Language" (لغة مواصفات ANSI C) المتوفرة لمنصة الأدوات مفتوحة المصدر Frama-C [2، 10]. إنها لغة مواصفات سلوكية يمكنها التعبير عن خصائص شفرة C المصدرية بما في ذلك الشروط المسبقة والشروط اللاحقة لدوال C باستخدام منطق الرتبة الأولى. يتم توفير مواصفات ACSL كتعليقات توضيحية للشفرة المصدرية. تسمح إضافة WP للإطار بالتحقق الاستنتاجي من الشفرة المصدرية مقابل التعليقات التوضيحية الرسمية في ACSL [3].

يُعرِّف DO-178C المتطلبات منخفضة المستوى (LLR) على أنها متطلبات البرمجيات التي يمكن تنفيذ الشفرة المصدرية منها مباشرة دون مزيد من المعلومات. في مشاريع البرمجيات التي شاركنا فيها، كانت هذه المتطلبات عبارة عن تعليقات توضيحية باللغة الطبيعية للإجراءات الفرعية أو إعلانات الدوال المقدمة من واجهات وحدات البرمجيات. لذلك من الطبيعي اعتبار ACSL كمرشح للتعبير رسمياً عن المتطلبات منخفضة المستوى.

ترتبط عدة أهداف ما يسمى بأهداف DO-178C بالمتطلبات منخفضة المستوى التي يجب الوفاء بها لقبول البرمجيات من قبل سلطات الاعتماد. أحد هذه الأهداف هو إمكانية التحقق من المتطلبات منخفضة المستوى. ويتحقق هذا الهدف بالفعل عند استخدام تدوين رسمي. هدف آخر هو امتثال الشفرة المصدرية للمتطلبات منخفضة المستوى، والذي يتم إظهاره عادةً بمراجعة الشفرة. يمكن استبدال هذه المراجعات المستهلكة للوقت بالتحقق الرسمي الآلي. يناقش Blasum وآخرون [7] هذه الأهداف وأهداف DO-178C الأخرى للأساليب الرسمية في مشروع Verisoft XT.

كان الهدف الرئيسي للدراسة هو التحقق مما إذا كان يمكن استخدام التدوينات الرسمية في مشروع حقيقي للتعبير رسمياً عن متطلبات العالم الواقعي منخفضة المستوى، أي لمعرفة ما إذا كان أسلوب رسمي معين مناسب للاستخدام في الممارسة الصناعية بشكل عام ولشركة ESG بشكل خاص. كان الهدف الثانوي هو فحص ما إذا كانت الأدوات المتاحة يمكنها التحقق من مثل هذه الشفرة المُعلَّقة توضيحياً وحتى القدرة على اكتشاف أخطاء لم يتم اكتشافها بعد بواسطة الاختبار، مما سيثبت إحدى المزايا المزعومة للأساليب الرسمية على الاختبار.

كانت الخطوة الأولى هي إنشاء معايير يجب أن يستوفيها التدوين الرسمي وأدوات دعمه من أجل أن يكون جاهزاً للاستخدام الصناعي في بيئة الشركات الصغيرة والمتوسطة. في خطوة ثانية، اخترنا دالة من مشروع إلكترونيات طيران حقيقي وصغنا رسمياً المواصفات باللغة الطبيعية لدوال C المرتبطة في مواصفات ACSL. كان في هذه الخطوة أننا واجهنا العقبات الأولى على الرغم من أن الدالة المختارة كانت بسيطة نوعاً ما.

هذه العقبات، في رأينا، نموذجية تماماً للبرمجة المدمجة في الوقت الفعلي. تم حل المشاكل بدعم من خبراء Frama-C عبر القائمة البريدية لـ Frama-C. ومع ذلك، فإن الحلول ليست مرضية تماماً مما قد يكون متأصلاً في النهج، كما سيتم مناقشته لاحقاً.

في خطوة تالية، حاولنا التحقق من الشفرة المصدرية مقابل مواصفة ACSL مع إضافة أدوات تأكيد للشفرة المصدرية من أجل توجيه المُثبِت. لم تكن كل محاولات التحقق ناجحة. تمكنا فقط من تفسير بعض المحاولات الفاشلة قبل نفاد الوقت. في خطوة أخيرة، قارنا تجربتنا في استخدام الأداة والطريقة مقابل المعايير المحددة سابقاً.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Automated theorem prover: مُثبِت نظريات آلي
  - Unit tests: اختبارات الوحدات
  - Trend setter: رائدة
  - Certification authorities: سلطات الاعتماد
  - Behavioral specification language: لغة مواصفات سلوكية
  - Pre-conditions: الشروط المسبقة
  - Post-conditions: الشروط اللاحقة
  - First order logic: منطق الرتبة الأولى
  - Annotations: تعليقات توضيحية
  - Deductive verification: التحقق الاستنتاجي
  - Low-Level Requirements (LLR): المتطلبات منخفضة المستوى
  - Code review: مراجعة الشفرة
  - Assertions: تأكيدات / أدوات تأكيد

- **Equations:** None
- **Citations:** [2], [3], [6], [7], [9], [10], [11], [12], [14], [15], [21]
- **Special handling:**
  - Company and project names kept in English (Airbus, Caveat, Verisoft XT, ESG)
  - Tool names kept in English (ACSL, Frama-C, WP plugin)
  - Standard names kept in English (DO-178C, DO-333, EAL 6, EAL 7)
  - Footnote 1 from page 2: "Ironically, the failed proof attempts that we were not able to explain were those where the prover timed out." - This is a humorous observation noted but not included in main translation

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-Translation Sample (First Paragraph)

"Recent developments in automated theorem provers led to moving formal methods from being mere pure academic exercises to their proximity to industrial use. Airborne software was recognized early as a suitable candidate for applying formal methods [14, 21]. For example, Airbus company examined the formal method Caveat to replace unit tests [15]. Since Airbus is considered a pioneer in the avionics industry at least in Europe, one can expect the obligation to use formal methods for developing highly safety-critical airborne software in the future."

**Back-translation Assessment:** Excellent semantic preservation with minor stylistic variations.
