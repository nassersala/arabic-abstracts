# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** model checking (فحص النماذج), formal methods (الأساليب الرسمية), finite state machine (آلة الحالة المحدودة), temporal logic (منطق زمني), symbolic model checking (فحص النماذج الرمزي), Binary Decision Diagram (مخطط القرار الثنائي), Bounded Model Checking (فحص النماذج المحدود), AADL, SysML, Simulink

---

### English Version

Formal methods for system verification, particularly via model checking have been in use since the 1980s. A common use of model checking is to create a representation of the system under analysis as a Finite State Machine (FSM) with assertions to be verified written in temporal logic. A model checker is then used to evaluate the FSM against the temporal logic assertions, providing counterexamples for any assertions for which an exception exists. Several strategies have been developed for representing and exploring finite state machines, notably symbolic model checking, which represents sets of states as Boolean functions. Exploration of these functions can be accomplished via Binary Decision Diagram (BDD) manipulation, which treats the state model exploration as a graph traversal, or by Bounded Model Checking (BMC), which treats bounded length executions of the state model as a SATISFIABILITY (SAT) problems.

A detailed survey of the practice of model checking is beyond the scope of this paper (See [5] for an overview). However, a theme in model checking methodologies encountered by the authors is the need to translate or adapt one's system design to an FSM with temporal logic assertions. Many such system designs are already written as conventional engineering models (e.g., AADL, SysML, Simulink). The SLICED methodology outlined in this paper provides a framework for generation of an FSM and associated assertions from conventional engineering models, as well as recommendations for addressing scalability concerns associated with the analysis of large engineering models.

**Background**

SLICED originated as an analysis methodology for generating FSM and temporal logic assertions from Architecture Analysis and Design Language (AADL). AADL is a language for describing embedded software systems in semantically precise terms [1]. SLICED has subsequently evolved to also include generation of FSMs and temporal logic assertions from SysML and Simulink. SLICED relies on well-defined component archetypes to generate standardized behavior FSM for individual system components that can be assembled into a composite FSM (see Definition 1).

**Definition 1.** A component's *significant states* are states that affect or are affected by other components. In the context of SLICED, a component's *behavior* is a specification of its significant states, how external events affect its active significant state, and how its significant states or transitions between significant states affect other components.

Advanced Diagnostic and Prognostic Testbed (ADAPT) is a testbed for evaluating electrical systems and injecting faults in a controlled manner. ADAPT consists of a power supply, batteries, sensors, and actuators. ADAPT has several hundred components [20]. NASA created Virtual ADAPT to provide a digital equivalent of ADAPT. Virtual ADAPT is a Simulink model of the majority of ADAPT [21].

We exercise the SLICED methodology using the symbolic model checker NuSMV. NuSMV provides the ability to specify Modules, which are collections of variables and transitions analogous to subcomponents in a system design [11].

**Scope**

This paper describes the SLICED methodology and how it applies to the Virtual ADAPT source model. We provide examples of the generated FSM as specified in the Symbolic Model Verification (SMV) language. We provide performance metrics generated from running the NuSMV solver on our generated FSM. We conclude with recommendations for future research.

---

### النسخة العربية

تم استخدام الأساليب الرسمية للتحقق من الأنظمة، وخاصة عبر فحص النماذج، منذ ثمانينيات القرن الماضي. من الاستخدامات الشائعة لفحص النماذج إنشاء تمثيل للنظام قيد التحليل كآلة حالة محدودة (FSM) مع تأكيدات يتم التحقق منها مكتوبة بمنطق زمني. يتم بعد ذلك استخدام فاحص النماذج لتقييم آلة الحالة المحدودة مقابل تأكيدات المنطق الزمني، مما يوفر أمثلة مضادة لأي تأكيدات يوجد لها استثناء. تم تطوير عدة استراتيجيات لتمثيل واستكشاف آلات الحالة المحدودة، وخاصة فحص النماذج الرمزي، الذي يمثل مجموعات من الحالات كدوال منطقية. يمكن تحقيق استكشاف هذه الدوال عبر معالجة مخطط القرار الثنائي (BDD)، الذي يتعامل مع استكشاف نموذج الحالة كاجتياز رسم بياني، أو عن طريق فحص النماذج المحدود (BMC)، الذي يتعامل مع عمليات التنفيذ محدودة الطول لنموذج الحالة كمسائل إشباع (SAT).

إن مسحاً مفصلاً لممارسة فحص النماذج يتجاوز نطاق هذه الورقة (انظر [5] للحصول على نظرة عامة). ومع ذلك، فإن موضوعاً في منهجيات فحص النماذج واجهه المؤلفون هو الحاجة إلى ترجمة أو تكييف تصميم النظام الخاص بالمرء إلى آلة حالة محدودة مع تأكيدات منطق زمني. العديد من تصاميم الأنظمة هذه مكتوبة بالفعل كنماذج هندسية تقليدية (على سبيل المثال، AADL، SysML، Simulink). توفر منهجية SLICED الموضحة في هذه الورقة إطاراً لتوليد آلة حالة محدودة والتأكيدات المرتبطة بها من نماذج الهندسة التقليدية، بالإضافة إلى توصيات لمعالجة مخاوف قابلية التوسع المرتبطة بتحليل نماذج الهندسة الكبيرة.

**الخلفية**

نشأت SLICED كمنهجية تحليل لتوليد آلات الحالة المحدودة وتأكيدات المنطق الزمني من لغة تحليل وتصميم المعمارية (AADL). AADL هي لغة لوصف أنظمة البرمجيات المدمجة بعبارات دلالية دقيقة [1]. تطورت SLICED لاحقاً لتشمل أيضاً توليد آلات الحالة المحدودة وتأكيدات المنطق الزمني من SysML و Simulink. تعتمد SLICED على أنماط أساسية محددة جيداً للمكونات لتوليد آلات حالة محدودة سلوكية موحدة لمكونات النظام الفردية التي يمكن تجميعها في آلة حالة محدودة مركبة (انظر التعريف 1).

**التعريف 1.** *الحالات المهمة* للمكون هي حالات تؤثر أو تتأثر بمكونات أخرى. في سياق SLICED، *سلوك* المكون هو مواصفة لحالاته المهمة، وكيف تؤثر الأحداث الخارجية على حالته المهمة النشطة، وكيف تؤثر حالاته المهمة أو التحولات بين الحالات المهمة على مكونات أخرى.

منصة الاختبار التشخيصية والتنبؤية المتقدمة (ADAPT) هي منصة اختبار لتقييم الأنظمة الكهربائية وحقن الأعطال بطريقة محكومة. تتكون ADAPT من مصدر طاقة وبطاريات وأجهزة استشعار ومشغلات. تحتوي ADAPT على عدة مئات من المكونات [20]. أنشأت ناسا Virtual ADAPT لتوفير مكافئ رقمي لـ ADAPT. Virtual ADAPT هو نموذج Simulink لمعظم ADAPT [21].

نمارس منهجية SLICED باستخدام فاحص النماذج الرمزي NuSMV. يوفر NuSMV القدرة على تحديد الوحدات النمطية، وهي مجموعات من المتغيرات والتحولات المماثلة للمكونات الفرعية في تصميم النظام [11].

**النطاق**

تصف هذه الورقة منهجية SLICED وكيف تنطبق على نموذج مصدر Virtual ADAPT. نقدم أمثلة على آلة الحالة المحدودة المولدة كما هو محدد في لغة التحقق من النموذج الرمزي (SMV). نقدم مقاييس الأداء الناتجة عن تشغيل حلال NuSMV على آلة الحالة المحدودة المولدة. نختتم بتوصيات للبحث المستقبلي.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Model checking - فحص النماذج
  - Finite State Machine (FSM) - آلة الحالة المحدودة
  - Temporal logic - منطق زمني
  - Symbolic model checking - فحص النماذج الرمزي
  - Binary Decision Diagram (BDD) - مخطط القرار الثنائي
  - Bounded Model Checking (BMC) - فحص النماذج المحدود
  - SATISFIABILITY (SAT) - إشباع
  - Component archetypes - الأنماط الأساسية للمكونات
  - Significant states - الحالات المهمة
  - Composite FSM - آلة حالة محدودة مركبة
  - ADAPT - منصة الاختبار التشخيصية والتنبؤية المتقدمة
  - NuSMV - (kept as proper noun)
- **Equations:** 0
- **Citations:** [1], [5], [11], [20], [21]
- **Special handling:** Proper nouns (AADL, SysML, Simulink, ADAPT, NuSMV) kept in English

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.91
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.88
