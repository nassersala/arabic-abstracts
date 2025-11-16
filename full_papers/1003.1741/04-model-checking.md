# Section 2.2: Model Checking Techniques for Requirements Validation
## القسم 2.2: تقنيات فحص النماذج للتحقق من صحة المتطلبات

**Section:** model checking techniques
**Translation Quality:** 0.85
**Glossary Terms Used:** satisfiability (الإرضاء), model checking (فحص النماذج), SMT (نظرية الإرضاء بالقياس), bounded model checking (فحص النماذج المحدود), CEGAR (التحسين التجريدي الموجه بالأمثلة المضادة), predicate abstraction (التجريد المحمولي)

---

### English Version

The validation process of the proposed methodology relies on a series of satisfiability checks: consistency checking is performed by solving the satisfiability problem of the conjunction of the formalized requirements; the check that the requirements are not too strict is performed by checking whether the conjunction of the requirements and the scenario's formulas is satisfiable; finally, the check that the requirements are not too weak is performed by checking whether the conjunction of the requirements and the negation of the property is unsatisfiable.

Unfortunately, the satisfiability problem of the chosen language is undecidable. The undecidability comes independently from the combination of temporal and first-order logics, from the combination of the uninterpreted functions and quantifiers, and from the hybrid component of the logic.

Nevertheless, we want to keep such expressiveness in order to faithfully represent the informal requirements in the formal language. Thus, we rely on automatic albeit incomplete satisfiability procedures.

First, we fix a number of objects per class so that it is possible to reduce the formula to equi-satisfiable one free of quantifiers and functional symbols [CRST09]. As described in [CRST08b], we can automatically find a bound on the number of objects for classes under certain restrictions.

Second, we translate the resulting quantifier-free hybrid formula into an equi-satisfiable formula in the classical temporal logic over discrete traces. In this case, we exploit the linearity of the constraints over the derivatives to guarantee the existence of a piecewise-linear solution and to encode the continuity of the continuous variables into quantifier-free constraints.

Third, we compile the resulting formula into a Fair Transition System (FTS) [MP92], whose accepted language is not empty iff the formula is satisfiable. For the compilation we rely on the works described in [CRT08, CRST08b]. We apply infinite-state model checking techniques to verify the language emptiness of the resulting fair transition system. In particular, we used Bounded Model Checking (BMC) [BCCZ99], particularly effective in solving the satisfiable cases and producing short models, and Counterexample-Guided Abstraction Refinement (CEGAR) [CGJ+00], more oriented to prove the unsatisfiability cases.

The language non-emptiness check for the FTS is performed by looking for a lasso-shape trace of length up to a given bound. We encode this trace into an SMT formula using a standard BMC encoding and we submit it to a suitable SMT solver. This procedure is incomplete from two point of views: first, we are performing BMC limiting the number of different transitions in the trace; second, unlike the Boolean case, we cannot guarantee that if there is no lasso-shape trace, there does not exist an infinite trace satisfying the model (since a real variable may be forced to increase forever). Nevertheless, we find the procedure extremely efficient in the framework of requirements validation.

In order to prove the emptiness of the FTS, we use predicate abstraction. We adopt a CEGAR loop, where the abstraction generation and refinement are completely automated. The loop consists of four phases: 1) *abstraction*, where the abstract system is built according to a given set of predicates; the abstract state space is computing by passing to the SMT solver an ALLSAT problem; 2) *verification*, where the non-emptiness of the language of the abstract system is checked; if the language is empty, it can be concluded that also the concrete system has an empty language; otherwise, an infinite trace is produced; the abstract system is finite so that we can used classical model checking techniques; 3) *simulation*: if the verification produces a trace, the simulation checks whether it is realistic by simulating it on the concrete system; if the trace can be simulated in the concrete system, it is reported as a real witness of the satisfiability of the formula; the trace is simulated by checking the satisfiability of the SMT problem; 4) *refinement*: if the simulation cannot find a concrete trace corresponding to the abstract one, the refinement discovers new predicates that, once added to the abstraction, are sufficient to rule out the unrealistic path; also this step is solved with an SMT solver.

---

### النسخة العربية

تعتمد عملية التحقق من الصحة للمنهجية المقترحة على سلسلة من فحوصات الإرضاء: يتم إجراء فحص الاتساق عن طريق حل مشكلة الإرضاء لاقتران المتطلبات الرسمية؛ يتم إجراء الفحص بأن المتطلبات ليست صارمة للغاية عن طريق التحقق مما إذا كان اقتران المتطلبات وصيغ السيناريو قابلاً للإرضاء؛ وأخيرًا، يتم إجراء الفحص بأن المتطلبات ليست ضعيفة جدًا عن طريق التحقق مما إذا كان اقتران المتطلبات ونفي الخاصية غير قابل للإرضاء.

لسوء الحظ، مشكلة الإرضاء للغة المختارة غير قابلة للقرار. يأتي عدم قابلية القرار بشكل مستقل من الجمع بين المنطق الزمني ومنطق الدرجة الأولى، ومن الجمع بين الدوال غير المفسرة والمحددات الكمية، ومن المكون الهجين للمنطق.

ومع ذلك، نريد الحفاظ على هذه القوة التعبيرية من أجل تمثيل المتطلبات غير الرسمية بدقة في اللغة الرسمية. وبالتالي، نعتمد على إجراءات إرضاء تلقائية وإن كانت غير مكتملة.

أولاً، نحدد عددًا من الكائنات لكل فئة بحيث يكون من الممكن تقليص الصيغة إلى صيغة متساوية الإرضاء خالية من المحددات الكمية والرموز الوظيفية [CRST09]. كما هو موضح في [CRST08b]، يمكننا العثور تلقائيًا على حد لعدد الكائنات للفئات في ظل قيود معينة.

ثانيًا، نترجم الصيغة الهجينة الخالية من المحددات الكمية الناتجة إلى صيغة متساوية الإرضاء في المنطق الزمني الكلاسيكي على التتبعات المنفصلة. في هذه الحالة، نستغل خطية القيود على المشتقات لضمان وجود حل خطي متعدد الأجزاء ولترميز استمرارية المتغيرات المستمرة في قيود خالية من المحددات الكمية.

ثالثًا، نترجم الصيغة الناتجة إلى نظام انتقال عادل (FTS) [MP92]، الذي لا تكون لغته المقبولة فارغة إلا إذا كانت الصيغة قابلة للإرضاء. للترجمة نعتمد على الأعمال الموصوفة في [CRT08، CRST08b]. نطبق تقنيات فحص النماذج ذات الحالات اللانهائية للتحقق من فراغ اللغة لنظام الانتقال العادل الناتج. على وجه الخصوص، استخدمنا فحص النماذج المحدود (BMC) [BCCZ99]، الفعال بشكل خاص في حل الحالات القابلة للإرضاء وإنتاج نماذج قصيرة، والتحسين التجريدي الموجه بالأمثلة المضادة (CEGAR) [CGJ+00]، الموجه أكثر لإثبات حالات عدم الإرضاء.

يتم إجراء فحص عدم فراغ اللغة لنظام FTS عن طريق البحث عن تتبع على شكل حلقة بطول يصل إلى حد معين. نرمز هذا التتبع إلى صيغة SMT باستخدام ترميز BMC قياسي ونقدمه إلى محلل SMT مناسب. هذا الإجراء غير مكتمل من وجهتي نظر: أولاً، نقوم بإجراء BMC مع تحديد عدد الانتقالات المختلفة في التتبع؛ ثانيًا، على عكس الحالة البولية، لا يمكننا ضمان أنه إذا لم يكن هناك تتبع على شكل حلقة، فلا يوجد تتبع لانهائي يرضي النموذج (نظرًا لأن متغيرًا حقيقيًا قد يُجبر على الزيادة إلى الأبد). ومع ذلك، نجد الإجراء فعالاً للغاية في إطار التحقق من صحة المتطلبات.

من أجل إثبات فراغ FTS، نستخدم التجريد المحمولي. نعتمد حلقة CEGAR، حيث يكون توليد التجريد والتحسين مؤتمتين بالكامل. تتكون الحلقة من أربع مراحل: 1) *التجريد*، حيث يتم بناء النظام المجرد وفقًا لمجموعة محمولات معينة؛ يتم حساب فضاء الحالة المجرد بتمرير مشكلة ALLSAT إلى محلل SMT؛ 2) *التحقق*، حيث يتم فحص عدم فراغ لغة النظام المجرد؛ إذا كانت اللغة فارغة، يمكن الاستنتاج أن النظام الفعلي أيضًا له لغة فارغة؛ وإلا، يتم إنتاج تتبع لانهائي؛ النظام المجرد محدود بحيث يمكننا استخدام تقنيات فحص النماذج الكلاسيكية؛ 3) *المحاكاة*: إذا أنتج التحقق تتبعًا، تتحقق المحاكاة مما إذا كان واقعيًا بمحاكاته على النظام الفعلي؛ إذا أمكن محاكاة التتبع في النظام الفعلي، يتم الإبلاغ عنه كشاهد حقيقي على إرضاء الصيغة؛ يتم محاكاة التتبع بفحص إرضاء مشكلة SMT؛ 4) *التحسين*: إذا لم تتمكن المحاكاة من العثور على تتبع فعلي مقابل للتتبع المجرد، يكتشف التحسين محمولات جديدة بحيث، بمجرد إضافتها إلى التجريد، تكون كافية لاستبعاد المسار غير الواقعي؛ يتم حل هذه الخطوة أيضًا باستخدام محلل SMT.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** satisfiability (الإرضاء), undecidable (غير قابل للقرار), equi-satisfiable (متساوي الإرضاء), Fair Transition System/FTS (نظام الانتقال العادل), Bounded Model Checking/BMC (فحص النماذج المحدود), CEGAR (التحسين التجريدي الموجه بالأمثلة المضادة), lasso-shape trace (تتبع على شكل حلقة), predicate abstraction (التجريد المحمولي), ALLSAT problem (مشكلة ALLSAT)
- **Equations:** 0
- **Citations:** 7 references (CRST09, CRST08b, MP92, CRT08, BCCZ99, CGJ+00)
- **Special handling:** Technical acronyms (FTS, BMC, CEGAR, SMT, ALLSAT) explained with Arabic translations

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.85
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.85
