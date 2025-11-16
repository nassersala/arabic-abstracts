# Section 8: Results
## القسم 8: النتائج

**Section:** Results
**Translation Quality:** 0.86
**Glossary Terms Used:** formal methods (الأساليب الرسمية), formal verification (التحقق الرسمي), specification (مواصفة), formal logic (المنطق الرسمي)

---

### English Version

This section matches the experience made in conducting this experiment against the criteria established in section 2.

**Familiarity with Notation and Method.** We had some exposure to formal methods from past experience with algebraic specifications and with the formal notation Z ([16]) as well as his participation in the research project Verisoft XT, but did not have working knowledge of ACSL and the Frama-C tool suite.

The ACSL notation is quite close to the C programming language syntax, a couple of additional language constructs must be familiarized. However, even the simple example that had been chosen for this study required some more sophisticated concepts such as ghost variables, logic functions, axioms and labels. As a consequence, the specifications are not simple to read for the untrained.

One particular difficulty is to find the correct and most efficient loop invariant, which however is a common problem to formal proof.

It should be noted that the amount of instrumentation in form of assertions and loop invariants is in the same order of magnitude as the size of the source code, or even exceeds it. This is to be expected and in line with DO-178 objectives where all source code must be traceable to requirements.

**Complexity of the Formal Language.** The language is very close to C syntax and is therefore familiar to C programmers. However, for more sophisticated specification tasks, the available ACSL constructs need a much deeper knowledge. Some specification tasks require learning of additional languages (e.g. YA or LTL for Aoraï).

**Training.** We are only aware of training sessions at conferences, and of courses and project consultancy that had been offered by the Fraunhofer FOKUS institute. Also the recently founded company TrustinSoft offers consultancy for Frama-C.

**Information Sources.** A few online resources are available, mostly tutorials and papers. The most efficient source of information is the Frama-C mailing list, accessible via the Frama-C Website [13] where the members of the Frama-C community provide fast and accurate advice.

**Tool Maturity.** We had difficulties installing the tool set on our Linux distribution (Archlinux 3.14.4-1) and on Cygwin over Microsoft Windows 7. With assistance of the tools mailing list and the forum of the Linux distribution we managed to install a command line version of Frama-C with the WP plugin and the Alt-Ergo proof engine on the Linux system. Although problems early on in the tool's usage can have detrimental effects on an organization's acceptance of the tool, this is considered a minor problem.

The WP plugin should be extended to include all ACSL features and support of mathematical functions.

**User Guidance provided by Tool.** The tool, even the command line version, highlights the goals that cannot be proved. It is possible to record the verification conditions that the tool generates. However, these are formulated in an intermediate language as input to the prover which is quite different to the C or even ACSL syntax. Analysis of verification conditions requires deep knowledge of automated prover technologies.

We were not able to prove all generated proof obligations and could not explain all discrepancies in the time that was allocated for this study. It may be possible that the Frama-C GUI together with interactive provers provide more debugging support – which we could not test due to the aforementioned installation problems.

---

### النسخة العربية

يطابق هذا القسم الخبرة المكتسبة في إجراء هذه التجربة مع المعايير المحددة في القسم 2.

**الإلمام بالتدوين والطريقة.** كان لدينا بعض الخبرة في الأساليب الرسمية من التجربة السابقة مع المواصفات الجبرية ومع التدوين الرسمي Z ([16]) بالإضافة إلى مشاركته في المشروع البحثي Verisoft XT، لكن لم تكن لدينا معرفة عملية بـ ACSL ومجموعة أدوات Frama-C.

تدوين ACSL قريب جداً من بناء جملة لغة البرمجة C، يجب التعرف على بضعة تركيبات لغة إضافية. ومع ذلك، فإن حتى المثال البسيط الذي تم اختياره لهذه الدراسة تطلب بعض المفاهيم الأكثر تطوراً مثل متغيرات الشبح والدوال المنطقية والبديهيات والتسميات. ونتيجة لذلك، فإن المواصفات ليست بسيطة القراءة لغير المدربين.

إحدى الصعوبات الخاصة هي إيجاد ثابت الحلقة الصحيح والأكثر كفاءة، والذي مع ذلك هو مشكلة شائعة للبرهان الرسمي.

تجدر الإشارة إلى أن كمية الأدوات في شكل تأكيدات وثوابت حلقات من نفس حجم الشفرة المصدرية، أو حتى تتجاوزها. هذا متوقع ومتوافق مع أهداف DO-178 حيث يجب أن تكون جميع الشفرة المصدرية قابلة للتتبع إلى المتطلبات.

**تعقيد اللغة الرسمية.** اللغة قريبة جداً من بناء جملة C وبالتالي فهي مألوفة لمبرمجي C. ومع ذلك، بالنسبة لمهام المواصفات الأكثر تطوراً، تحتاج تركيبات ACSL المتاحة إلى معرفة أعمق بكثير. تتطلب بعض مهام المواصفات تعلم لغات إضافية (على سبيل المثال YA أو LTL لـ Aoraï).

**التدريب.** نحن على علم فقط بجلسات التدريب في المؤتمرات، والدورات والاستشارات المشروعية التي قدمها معهد Fraunhofer FOKUS. كما تقدم شركة TrustinSoft التي تأسست مؤخراً استشارات لـ Frama-C.

**مصادر المعلومات.** تتوفر بعض الموارد عبر الإنترنت، معظمها برامج تعليمية وأوراق بحثية. المصدر الأكثر كفاءة للمعلومات هو القائمة البريدية لـ Frama-C، يمكن الوصول إليها عبر موقع Frama-C [13] حيث يقدم أعضاء مجتمع Frama-C نصائح سريعة ودقيقة.

**نضج الأداة.** واجهنا صعوبات في تثبيت مجموعة الأدوات على توزيعة Linux الخاصة بنا (Archlinux 3.14.4-1) وعلى Cygwin فوق Microsoft Windows 7. بمساعدة القائمة البريدية للأدوات ومنتدى توزيعة Linux تمكنا من تثبيت نسخة سطر الأوامر من Frama-C مع إضافة WP ومحرك البرهان Alt-Ergo على نظام Linux. على الرغم من أن المشاكل في وقت مبكر من استخدام الأداة يمكن أن يكون لها تأثيرات ضارة على قبول المنظمة للأداة، إلا أن هذا يُعتبر مشكلة بسيطة.

يجب توسيع إضافة WP لتشمل جميع ميزات ACSL ودعم الدوال الرياضية.

**التوجيه المقدم من الأداة للمستخدم.** تسلط الأداة، حتى نسخة سطر الأوامر، الضوء على الأهداف التي لا يمكن إثباتها. من الممكن تسجيل شروط التحقق التي تولدها الأداة. ومع ذلك، يتم صياغة هذه في لغة وسيطة كإدخال للمُثبِت والتي تختلف تماماً عن بناء جملة C أو حتى ACSL. يتطلب تحليل شروط التحقق معرفة عميقة بتقنيات المُثبِت الآلي.

لم نتمكن من إثبات جميع التزامات البرهان المُولدة ولم نتمكن من تفسير جميع التناقضات في الوقت المخصص لهذه الدراسة. قد يكون من الممكن أن واجهة Frama-C الرسومية مع المُثبِتات التفاعلية توفر المزيد من دعم تصحيح الأخطاء - والذي لم نتمكن من اختباره بسبب مشاكل التثبيت المذكورة أعلاه.

---

### Translation Notes

- **Key Terms:**
  - Algebraic specifications: المواصفات الجبرية
  - Ghost variables: متغيرات الشبح
  - Logic functions: الدوال المنطقية
  - Axioms: البديهيات
  - Labels: التسميات
  - Loop invariant: ثابت الحلقة
  - Instrumentation: الأدوات / أدوات القياس
  - Traceability: التتبع
  - Mailing list: القائمة البريدية
  - Command line version: نسخة سطر الأوامر
  - Proof engine: محرك البرهان
  - Tool maturity: نضج الأداة
  - User guidance: التوجيه للمستخدم
  - Intermediate language: لغة وسيطة
  - Interactive provers: المُثبِتات التفاعلية
  - Debugging support: دعم تصحيح الأخطاء

- **Citations:** [13], [16]

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
