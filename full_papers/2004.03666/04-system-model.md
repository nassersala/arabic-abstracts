# Section 4: System Model
## القسم 4: نموذج النظام

**Section:** system-model
**Translation Quality:** 0.87
**Glossary Terms Used:** compositional (تركيبي), state machine (آلة حالة), finite automata (آليات محدودة), deterministic (حتمي), powerset construction (بناء مجموعة القوى), formal specification (مواصفة رسمية), Kripke structure (بنية كريبكي), assertion (تأكيد)

---

### English Version

SLICED takes a compositional approach to state modeling, requiring that the user provide state machine specifications for each component that describe its behavior as manifest at its logical boundary. Applied to a Simulink model, this means the user treats individual blocks (e.g., a battery) as black boxes, describing their behavior only in terms of what goes in to the component and what comes out.

For the ADAPT example application of SLICED, we defined five types of components, each with behavior specified at their boundary. Doing so enabled us to abstract the inner complexity of the components, losing model fidelity but enabling formal analysis. Listing 1 shows an example of a SLICED module abstracting the Simulink specification shown in Figure 3. The states listed in Listing 1 are taken from a secondary specification provided by NASA with the ADAPT model.

**Listing 1: Battery module specified in NuSMV**

```
MODULE Battery(output1, output2, capacity)
VAR
  state: {nominal, dead, underRepair};
DEFINE
  supplyingPower := (state = nominal);
  draw := (output1.draw + output1.draw);
ASSIGN
  init(state) := nominal;

  next(state) := case
    (draw > capacity) : dead;
    ((state = dead) & (draw = 0)) : underRepair;
    ((state = underRepair) & (draw = 0)) : nominal;
    TRUE : state;
  esac;
```

SLICED combines these state specifications with global system configuration (such as processor schedules, message routing, or intercomponent dependencies) to create a composite state machine (this data flow is shown in Figure 4).

**Definition 3.** A composite state machine is a deterministic finite automata formed from the powerset construction of independent component state machines and system configuration.

By limiting the scope of each component's state machine to its behavioral interface, SLICED can minimize the effective state space that it must analyze. The limited scope of each component's state machine reduces the risk required to reconfigure an integrated system design, for example by adding or removing components as shown in Subsubsection 6.3.1, because the connections between components are well defined and clearly specified. A naive deterministic finite automata construction from multiple state machines results in the powerset construction of all of their component states, as described in Definition 3. Our definition of the composite state machine is similar to the Interface Featured Time Automata described by Cledou et al. [12].

A core element of the SLICED hypothesis is that discretized events in a system model can yield results that are useful for a real system. Use of a discrete clock enables us to model timed automata (strictly, ordered automata) where assumptions about the duration of events can be applied. A further branch of study, the application of statistical methods to timed automata, is beyond the scope of this paper.

**Approaches to Finite State Machine Generation**

There are several potential levels of fidelity in translation of an electrical systems model (such as Virtual ADAPT) to a formal specification. All of these approaches treat individual components as black boxes and construct a formal specification as an assembly of black-box modeled components. Each level adds fidelity to the black box models, progressively them from "black" to "white."

1. **State only translation:** Make no assumptions about the relationships between components. Model component states only as expressed verbatim in the source model.

2. **State and connection translation:** Assume that error states propagate along communication paths described in the source model. Assume some source model states are "good" and some are "bad" and that good and bad state properties propagate (e.g., if a component is in a bad state, anything connected to it is also in a bad state).

3. **State and connection translation with directionality:** Same as State and Connection Translation, but assume directionality in connections can be determined from the source model (that is, bad component state only propagates to downstream components.) This assumes that cycles are allowed, but that connections are directed.

4. **State and connection translation with directionality and discrete signals:** Instead of treating connections as binary on/off, treat connections as capable of holding one of a fixed set of values (e.g., value from 0...9).

5. **Discrete models of component behavior:** Model the internals of each component in the model, discretizing and bounding the values but otherwise fully translating its behavior to a formal specification.

**SLICED Pseudocode**

SLICED employs approach 4, State and connection translation with directionality and discrete signals. This is in contrast with the higher-fidelity translation presented by Meenakshi et al. [19]. The SLICED implementation is similar for most modeling languages (prior implementations have used AADL and SysML). The SLICED implementation for ADAPT and Simulink is as follows:

1. Iterate over all elements in the simulink model (using the library org.conqat.lib.simulink) in a depth-first search.
2. For each leaf block, identify the archetype of the block (e.g., relay, battery, junction). Create a new MODULE in SMV for that block using a standard prototype.
   a. The ADAPT Simulink model does not define component archetypes, so we relied on component naming conventions to differentiate components. For future work an AADL model of ADAPT could enable stronger semantic consistency in component definitions.
3. As the search ascends toward the root, continue creating MODULES for each block that has a corresponding archetype.
4. For each line contained in each block, add input or output parameters to the appropriate modules based on the start and end points of each line. This step is similar to the process of creating Reo connectors described in [12].
5. For each line that traverses multiple blocks, follow the line until a SLICED-abstracted component is found. When the SLICED-abstracted component is found, add it as an input or an output parameter as described in the previous step.

**4.1 Subsystem Merging**

An additional performance improvement strategy employed by SLICED is problem reduction based on effective communication. In software state analysis, SLICED uses intercomponent communication configuration to limit the size of the composite state machine by excluding composite states that are not reachable using a given communication configuration, similar to the "port linking" approach described by Cledou et al. [12]. As with Cledou et al., we treat all signals uniformly (that is, in a hardware model a component's power draw is treated as a form of communication with the component supplying the power). SLICED uses a strategy similar to Shannon's expansion to reduce the complexity of hardware model FSMs [17]. This paper focuses on the latter, as it is most applicable to the ADAPT model.

**4.1.1 Subsystem Merging in ADAPT**

In the ADAPT model there are four banks of actuators, two with two actuators and two with six actuators. Using our actuator module definition (Listing 2), this results in 16 total actuators, each with 3 states, increasing our effective state space by a factor of 3^16. However, inspection of the model shows that the effective communication between each bank of actuators and the batteries and relays all goes through a single connection (e.g., the breaker EY166 in Figure 5). The result is that there are a considerable numbers of composite states of the actuators that can be discarded a priori by collapsing the state space of six actuators into a single effective actuator state, shown in Listing 3, whose states are limited to the available effective states of the subsystem. In the case of the breaker, EY166, there are 3^6 possible states when the subsystem is considered naively, but there are only 13 effective states of its interaction with other components (each actuator can draw 0, 1, or 2 units of power. There are 6 actuators, so power consumption of 0..12 is possible (thus drawlimit is set to 12 in Listing 3).

**Listing 2: Actuator module specified in NuSMV**

```
MODULE Actuator(input)
VAR
  state: {nominal, nopower, faultyResistance};
DEFINE
  draw := case
    (!(input.supplyingPower) | (state = nopower)) : 0;
    (state = nominal) : 1;
    (state = faultyResistance) : 2;
  esac;
ASSIGN
  init(state) := nominal;
```

**Listing 3: Merged Actuator module specified in NuSMV**

```
MODULE MergedActuator(input, drawlimit)
VAR
  draw : 0..drawlimit;
```

**4.1.2 Subsystem Merging Formalism**

In terms of Shannon's expansion, we divide the system problem into two sub-problems at the boundary of the connection between the system and the parent system. This divide is possible because of the compositional structure of the FSM. Subsystems that interact only at the subsystem boundary (abstracting their inner components) must define functions that aggregate their internal state (such as the addition of power consumption described in Subsubsection 4.1.1). Dependencies between components are modeled as shared variables in the FSM. For example, the power draw of an actuator is represented as an integer variable that is shared with upstream relays, breakers, or power supplies. This approach to reduced subsystem representation is similar to the Cone of Influence (COI) feature of NuSMV, however COI only eliminates variables not reachable from a given assertion [10]. BMC analysis of the state model may likely have taken advantage of this feature of the model and is an opportunity for future study.

Any resulting error trace (for example, an error when the total draw is 10) can serve as input to a follow-up sub-analysis on the decomposed subsystem. The error trace for the top level error will give us the value on the communication channel between the top level system and the sub-system, which we then use to generate a second assertion, this time on the sub-system. Because the only interaction between the sub-system and the top level system is through the aggregation component, we can be confident that none of the 3^6 - 13 state combinations in the sub-system could have altered our top level assessment.

**4.2 Assertion Generation**

SLICED deals with two classes of assertions over the same problem space, both are classical applications of temporal logical applied by generation from conventional engineering models. First, SLICED generates error discovery assertions, which are assertions for which a counterexample indicates a system specification error. Error discovery assertions include those asserting that the system will not enter a bad state from a good state (safety) or that some expected state will eventually occur (liveness). SLICED can also generate path discovery assertions, which are assertions that the system will not enter a good state from a bad state. The former is useful for detecting potential system error conditions. The latter is useful for generating plans to restore a safe system state if a bad state has occurred.

**Definition 4.** An Error Discovery Assertion defines a condition to be avoided, such as "the system shall never enter an unsafe state." A "solution" found by the solver for an error discovery assertion indicates an error in the design.

**Definition 5.** A Path Discovery Assertion defines a condition to be reached if possible. A "solution" found by the solver for a path discovery assertion indicates a plan for return to a good state.

**Safety and Liveness Assertion Generation**

Failure assertions include both safety assertions (describing things that should not happen) and liveness assertions (describing things that should happen). SLICED generates assertions using information provided by the source model describing the expected states of each component. For example, when dealing with software components SLICED generates liveness assertions for periodic threads that must always reach a final state. Similarly, if the source model definition of a component describes an error state, SLICED generates a safety assertion that the error state will never be reached.

When evaluating timing properties, SLICED uses a cyclic clock, incrementing one tick for each step taken in the state machine evaluation. Ticks are represented at the Greatest Common Denominator (GCD) of timing properties of the design (e.g., for a system which expresses performance deadlines at a granularity of one millisecond, sliced uses one millisecond for a tick). SLICED uses a cyclic clock because all variables in a FSM must be finite. The maximum value of the clock is determined by the hyperperiod of all periodic elements in the source model (e.g., if the source model has threads with periods of 100, 200, and 300ms, SLICED will use a 600ms clock cycle). When the source model provides deadlines for performance, SLICED evaluates the component states against its cyclic clock.

For connections between components, SLICED treats each connection as a discrete variable or as a property of an existing variable. For connections with capacity constraints, SLICED treats the connection as a counting semaphore and creates assertions that restrict the number of messages it can contain according to its upper bound.

**Path Discovery Assertion Generation**

To generate a path discovery assertion, SLICED expresses the initial (failed) state of the system in a FSM with its initial state set to include one or more errors. The FSM differs from that used to evaluate error discovery assertions because it leaves user actions specified as non-deterministic, in effect letting the solver take on the role of the user to manipulate the system at-will. In the FSM a user action is a is a transition whose guard relies on a user input event (e.g., flipping of a switch) where the source of that event is external to the modeled system. SLICED then generates an assertion describing the negation of the desired state, including both the original faulty component and of all of the other components in the system.

**4.2.1 SLICED Formalism**

For each component in the source model, we generate a state machine ψ. Using actions A on or between these components as specified in the source model (e.g., as connections), we assemble a composite state machine Ψ.

**State machine semantics**

The formal semantics of a state machine in SLICED are a 6-tuple ψ = (S, A, T ⊆ S × A × S, s₀ ∈ S, E ⊆ S, d ∈ S).

- A—is a set of events, or Actions,
- S—is a set of states for the component,
- T ⊆ S × A × S—is the set of labeled transitions,
- s₀ ∈ S—is a designated initial state,
- E ⊆ S—is a distinguished set of error states.

We use a shorthand for transitions of S, writing s →ᵃ s' for an element t ∈ T.

**Composite State Machine**

The composite state machine is built from both the behavioral model associated with each component and connections between them. The composite state machine is the analytic core of SLICED and describes the behavior of the entire system.

Formally, the composite state machine is a timed Büchi automaton built by viewing each component as running independently with the addition of a global clock. In the case of ADAPT, which does not have specific timing constraints used by SLICED, SLICED assumes events happen in discrete time steps. Transitions between states are inter-component connections, supporting human-in-the-loop state changes through non-determinism. For example, user-settable relays have non-deterministic open and closed state transitions to account for user actions. Using powerset construction, we can build a Deterministic Finite Automata (DFA) to model the behavior of the entire system [23]. In the context of a Simulink model, a transition is an event that changes the significant state of a component as defined by its component archetype. The naïve powerset construction is exponentially larger than the Nondeterministic Finite Automata (NFA) for any individual component.

Formally, given a collection of input n behavioral state machines ψ₁, ··· ψₙ, using a common data model A, denoted ψⁱ = (Sⁱ, A, Tⁱ ⊆ Sⁱ × A × Sⁱ, sⁱ₀ ∈ S, Eⁱ ⊆ S, d ∈ S), the composite state machine is constructed as:

Ψ = (⊕ψᵢ) ⊕ A꜀
  c = a clock
  T = {(···, s, ···) →ᵃ (···, s', ···) for s →ᵃ s' a transition of Sⁱ and S a time slice of Sᵢ}
  s₀ = (s¹₀, s²₀, ..., sⁿ₀, S₀) ∈ Ψ

**State Space Size**

The full state space of the naïve composite state machine for a model the scale of ADAPT is combinatorially large, making it impractical to analyze. By using component abstractions with simplified behavior specifications, SLICED dramatically reduces the size of the relevant state space.

We achieve further reduction in the state space size by using subsystem aggregation functions table to collapse large subsystem state spaces for top-level system analysis, then expand them to generate detailed traces for particular conditions.

---

### النسخة العربية

تتخذ SLICED نهجاً تركيبياً لنمذجة الحالة، مما يتطلب من المستخدم توفير مواصفات آلة حالة لكل مكون تصف سلوكه كما يظهر عند حدودهالمنطقية. عند تطبيقها على نموذج Simulink، يعني هذا أن المستخدم يتعامل مع الكتل الفردية (على سبيل المثال، البطارية) كصناديق سوداء، ويصف سلوكها فقط من حيث ما يدخل إلى المكون وما يخرج منه.

بالنسبة لتطبيق ADAPT النموذجي لـ SLICED، قمنا بتحديد خمسة أنواع من المكونات، كل منها مع سلوك محدد عند حدودها. مكّننا ذلك من تجريد التعقيد الداخلي للمكونات، مما أدى إلى فقدان دقة النموذج ولكن تمكين التحليل الرسمي. يُظهر القائمة 1 مثالاً على وحدة SLICED تجرد مواصفة Simulink الموضحة في الشكل 3. الحالات المدرجة في القائمة 1 مأخوذة من مواصفة ثانوية قدمتها ناسا مع نموذج ADAPT.

**القائمة 1: وحدة البطارية المحددة في NuSMV**

```
MODULE Battery(output1, output2, capacity)
VAR
  state: {nominal, dead, underRepair};
DEFINE
  supplyingPower := (state = nominal);
  draw := (output1.draw + output1.draw);
ASSIGN
  init(state) := nominal;

  next(state) := case
    (draw > capacity) : dead;
    ((state = dead) & (draw = 0)) : underRepair;
    ((state = underRepair) & (draw = 0)) : nominal;
    TRUE : state;
  esac;
```

تجمع SLICED مواصفات الحالة هذه مع تكوين النظام العام (مثل جداول المعالج، أو توجيه الرسائل، أو التبعيات بين المكونات) لإنشاء آلة حالة مركبة (يظهر تدفق البيانات هذا في الشكل 4).

**التعريف 3.** آلة الحالة المركبة هي آلية محدودة حتمية تتكون من بناء مجموعة القوى لآلات حالة المكونات المستقلة وتكوين النظام.

من خلال تحديد نطاق آلة حالة كل مكون إلى واجهته السلوكية، يمكن لـ SLICED تقليل فضاء الحالة الفعال الذي يجب تحليله. يقلل النطاق المحدود لآلة حالة كل مكون من المخاطر المطلوبة لإعادة تكوين تصميم نظام متكامل، على سبيل المثال عن طريق إضافة أو إزالة المكونات كما هو موضح في القسم الفرعي 6.3.1، لأن الاتصالات بين المكونات محددة جيداً ومحددة بوضوح. ينتج عن بناء آلية محدودة حتمية ساذجة من آلات حالة متعددة بناء مجموعة القوى لجميع حالات مكوناتها، كما هو موضح في التعريف 3. تعريفنا لآلة الحالة المركبة مماثل لآليات الوقت المميزة بالواجهة الموصوفة من قبل Cledou وآخرين [12].

عنصر أساسي في فرضية SLICED هو أن الأحداث المنفصلة في نموذج النظام يمكن أن تسفر عن نتائج مفيدة لنظام حقيقي. يمكّننا استخدام ساعة منفصلة من نمذجة آليات موقوتة (على وجه الدقة، آليات مرتبة) حيث يمكن تطبيق افتراضات حول مدة الأحداث. فرع آخر من الدراسة، تطبيق الأساليب الإحصائية على الآليات الموقوتة، يتجاوز نطاق هذه الورقة.

**نُهُج توليد آلة الحالة المحدودة**

هناك عدة مستويات محتملة من الدقة في ترجمة نموذج أنظمة كهربائية (مثل Virtual ADAPT) إلى مواصفة رسمية. تعامل جميع هذه النُهُج المكونات الفردية كصناديق سوداء وتبني مواصفة رسمية كتجميع للمكونات المنمذجة بصناديق سوداء. يضيف كل مستوى دقة إلى نماذج الصندوق الأسود، مما يحولها تدريجياً من "أسود" إلى "أبيض".

1. **ترجمة الحالة فقط:** لا تضع افتراضات حول العلاقات بين المكونات. نموذج حالات المكونات فقط كما هو معبر عنه حرفياً في النموذج المصدر.

2. **ترجمة الحالة والاتصال:** افترض أن حالات الخطأ تنتشر على طول مسارات الاتصال الموصوفة في النموذج المصدر. افترض أن بعض حالات النموذج المصدر "جيدة" وبعضها "سيئة" وأن خصائص الحالة الجيدة والسيئة تنتشر (على سبيل المثال، إذا كان المكون في حالة سيئة، فإن أي شيء متصل به يكون أيضاً في حالة سيئة).

3. **ترجمة الحالة والاتصال مع الاتجاهية:** مماثل لترجمة الحالة والاتصال، ولكن افترض أنه يمكن تحديد الاتجاهية في الاتصالات من النموذج المصدر (أي أن حالة المكون السيئة تنتشر فقط إلى المكونات اللاحقة). يفترض هذا أن الدورات مسموحة، ولكن الاتصالات موجهة.

4. **ترجمة الحالة والاتصال مع الاتجاهية والإشارات المنفصلة:** بدلاً من معاملة الاتصالات على أنها ثنائية تشغيل/إيقاف، عامل الاتصالات على أنها قادرة على حمل واحدة من مجموعة ثابتة من القيم (على سبيل المثال، قيمة من 0...9).

5. **نماذج منفصلة لسلوك المكونات:** نموذج الأجزاء الداخلية لكل مكون في النموذج، وتفكيك وتحديد القيم ولكن ترجمة سلوكها بالكامل إلى مواصفة رسمية.

**كود SLICED الزائف**

توظف SLICED النهج 4، ترجمة الحالة والاتصال مع الاتجاهية والإشارات المنفصلة. هذا على النقيض من الترجمة ذات الدقة الأعلى المقدمة من قبل Meenakshi وآخرين [19]. تنفيذ SLICED مماثل لمعظم لغات النمذجة (استخدمت التنفيذات السابقة AADL و SysML). تنفيذ SLICED لـ ADAPT و Simulink كما يلي:

1. التكرار عبر جميع العناصر في نموذج simulink (باستخدام المكتبة org.conqat.lib.simulink) في بحث بالعمق أولاً.
2. لكل كتلة ورقة، حدد النمط الأساسي للكتلة (على سبيل المثال، مرحل، بطارية، تقاطع). أنشئ MODULE جديدة في SMV لتلك الكتلة باستخدام نموذج أولي قياسي.
   أ. نموذج ADAPT Simulink لا يحدد الأنماط الأساسية للمكونات، لذلك اعتمدنا على اتفاقيات تسمية المكونات لتمييز المكونات. للعمل المستقبلي، يمكن لنموذج AADL لـ ADAPT تمكين اتساق دلالي أقوى في تعريفات المكونات.
3. عندما يصعد البحث نحو الجذر، استمر في إنشاء MODULES لكل كتلة لها نمط أساسي مقابل.
4. لكل خط موجود في كل كتلة، أضف معاملات إدخال أو إخراج إلى الوحدات النمطية المناسبة بناءً على نقاط البداية والنهاية لكل خط. هذه الخطوة مماثلة لعملية إنشاء موصلات Reo الموصوفة في [12].
5. لكل خط يجتاز كتل متعددة، اتبع الخط حتى يتم العثور على مكون مجرد بواسطة SLICED. عندما يتم العثور على المكون المجرد بواسطة SLICED، أضفه كمعامل إدخال أو إخراج كما هو موضح في الخطوة السابقة.

**4.1 دمج الأنظمة الفرعية**

استراتيجية تحسين أداء إضافية توظفها SLICED هي تقليل المسألة بناءً على الاتصال الفعال. في تحليل حالة البرمجيات، تستخدم SLICED تكوين الاتصال بين المكونات لتحديد حجم آلة الحالة المركبة من خلال استبعاد الحالات المركبة غير القابلة للوصول باستخدام تكوين اتصال معين، مماثل لنهج "ربط المنفذ" الموصوف من قبل Cledou وآخرين [12]. كما هو الحال مع Cledou وآخرين، نتعامل مع جميع الإشارات بشكل موحد (أي في نموذج أجهزة، يُعامل استهلاك طاقة المكون كشكل من أشكال الاتصال مع المكون الذي يوفر الطاقة). تستخدم SLICED استراتيجية مماثلة لتوسع شانون لتقليل تعقيد آلات الحالة المحدودة لنموذج الأجهزة [17]. تركز هذه الورقة على الأخير، لأنه الأكثر قابلية للتطبيق على نموذج ADAPT.

**4.1.1 دمج الأنظمة الفرعية في ADAPT**

في نموذج ADAPT هناك أربعة بنوك من المشغلات، اثنان مع اثنين من المشغلات واثنان مع ستة مشغلات. باستخدام تعريف وحدة المشغل (القائمة 2)، ينتج عن هذا 16 مشغلاً إجمالياً، كل منها مع 3 حالات، مما يزيد فضاء الحالة الفعال لدينا بمعامل 3^16. ومع ذلك، يُظهر فحص النموذج أن الاتصال الفعال بين كل بنك من المشغلات والبطاريات والمرحلات يمر كله عبر اتصال واحد (على سبيل المثال، القاطع EY166 في الشكل 5). النتيجة هي أن هناك أعداداً كبيرة من الحالات المركبة للمشغلات يمكن التخلص منها مسبقاً عن طريق طي فضاء حالة ستة مشغلات إلى حالة مشغل فعالة واحدة، موضحة في القائمة 3، والتي تقتصر حالاتها على الحالات الفعالة المتاحة للنظام الفرعي. في حالة القاطع، EY166، هناك 3^6 حالة ممكنة عندما يتم اعتبار النظام الفرعي بشكل ساذج، ولكن هناك فقط 13 حالة فعالة لتفاعله مع المكونات الأخرى (يمكن لكل مشغل استهلاك 0 أو 1 أو 2 وحدة من الطاقة. هناك 6 مشغلات، لذا فإن استهلاك الطاقة من 0..12 ممكن (وبالتالي يتم تعيين drawlimit إلى 12 في القائمة 3).

**القائمة 2: وحدة المشغل المحددة في NuSMV**

```
MODULE Actuator(input)
VAR
  state: {nominal, nopower, faultyResistance};
DEFINE
  draw := case
    (!(input.supplyingPower) | (state = nopower)) : 0;
    (state = nominal) : 1;
    (state = faultyResistance) : 2;
  esac;
ASSIGN
  init(state) := nominal;
```

**القائمة 3: وحدة المشغل المدمجة المحددة في NuSMV**

```
MODULE MergedActuator(input, drawlimit)
VAR
  draw : 0..drawlimit;
```

**4.1.2 شكلية دمج الأنظمة الفرعية**

من حيث توسع شانون، نقسم مسألة النظام إلى مسألتين فرعيتين عند حدود الاتصال بين النظام والنظام الأب. هذا التقسيم ممكن بسبب البنية التركيبية لآلة الحالة المحدودة. يجب على الأنظمة الفرعية التي تتفاعل فقط عند حدود النظام الفرعي (تجريد مكوناتها الداخلية) تحديد دوال تجمع حالتها الداخلية (مثل إضافة استهلاك الطاقة الموضحة في القسم الفرعي 4.1.1). يتم نمذجة التبعيات بين المكونات كمتغيرات مشتركة في آلة الحالة المحدودة. على سبيل المثال، يتم تمثيل استهلاك طاقة المشغل كمتغير عدد صحيح يتم مشاركته مع المرحلات أو القواطع أو مصادر الطاقة الأولية. هذا النهج لتمثيل النظام الفرعي المختزل مماثل لميزة مخروط التأثير (COI) في NuSMV، ومع ذلك فإن COI يزيل فقط المتغيرات غير القابلة للوصول من تأكيد معين [10]. قد يكون تحليل BMC لنموذج الحالة قد استفاد من هذه الميزة من النموذج وهو فرصة للدراسة المستقبلية.

يمكن لأي أثر خطأ ناتج (على سبيل المثال، خطأ عندما يكون إجمالي السحب 10) أن يعمل كمدخل لتحليل فرعي متابعة على النظام الفرعي المحلل. سيعطينا أثر الخطأ للخطأ على المستوى الأعلى القيمة على قناة الاتصال بين نظام المستوى الأعلى والنظام الفرعي، والتي نستخدمها بعد ذلك لتوليد تأكيد ثانٍ، هذه المرة على النظام الفرعي. لأن التفاعل الوحيد بين النظام الفرعي ونظام المستوى الأعلى هو من خلال مكون التجميع، يمكننا أن نكون واثقين من أن أياً من تركيبات الحالة 3^6 - 13 في النظام الفرعي لم يكن بإمكانها تغيير تقييمنا على المستوى الأعلى.

**4.2 توليد التأكيدات**

تتعامل SLICED مع فئتين من التأكيدات على نفس فضاء المسألة، وكلاهما من التطبيقات الكلاسيكية للمنطق الزمني المطبق من خلال التوليد من نماذج الهندسة التقليدية. أولاً، تولد SLICED تأكيدات اكتشاف الأخطاء، وهي تأكيدات يشير فيها مثال مضاد إلى خطأ في مواصفة النظام. تشمل تأكيدات اكتشاف الأخطاء تلك التي تؤكد أن النظام لن يدخل حالة سيئة من حالة جيدة (سلامة) أو أن بعض الحالة المتوقعة ستحدث في النهاية (حيوية). يمكن لـ SLICED أيضاً توليد تأكيدات اكتشاف المسار، وهي تأكيدات بأن النظام لن يدخل حالة جيدة من حالة سيئة. الأول مفيد للكشف عن حالات خطأ النظام المحتملة. الأخير مفيد لتوليد خطط لاستعادة حالة نظام آمنة إذا حدثت حالة سيئة.

**التعريف 4.** تأكيد اكتشاف الخطأ يحدد حالة يجب تجنبها، مثل "يجب على النظام ألا يدخل أبداً حالة غير آمنة". يشير "حل" وجده الحلال لتأكيد اكتشاف الخطأ إلى خطأ في التصميم.

**التعريف 5.** تأكيد اكتشاف المسار يحدد حالة يجب الوصول إليها إن أمكن. يشير "حل" وجده الحلال لتأكيد اكتشاف المسار إلى خطة للعودة إلى حالة جيدة.

**توليد تأكيدات السلامة والحيوية**

تشمل تأكيدات الفشل كلاً من تأكيدات السلامة (وصف الأشياء التي يجب ألا تحدث) وتأكيدات الحيوية (وصف الأشياء التي يجب أن تحدث). تولد SLICED التأكيدات باستخدام المعلومات المقدمة من النموذج المصدر الذي يصف الحالات المتوقعة لكل مكون. على سبيل المثال، عند التعامل مع مكونات البرمجيات، تولد SLICED تأكيدات حيوية للخيوط الدورية التي يجب أن تصل دائماً إلى حالة نهائية. وبالمثل، إذا كان تعريف النموذج المصدر لمكون يصف حالة خطأ، تولد SLICED تأكيد سلامة بأن حالة الخطأ لن يتم الوصول إليها أبداً.

عند تقييم خصائص التوقيت، تستخدم SLICED ساعة دورية، تزيد علامة واحدة لكل خطوة مأخوذة في تقييم آلة الحالة. يتم تمثيل العلامات عند القاسم المشترك الأكبر (GCD) لخصائص التوقيت للتصميم (على سبيل المثال، لنظام يعبر عن المواعيد النهائية للأداء بدقة ميلي ثانية واحدة، تستخدم SLICED ميلي ثانية واحدة لعلامة). تستخدم SLICED ساعة دورية لأن جميع المتغيرات في آلة حالة محدودة يجب أن تكون محدودة. يتم تحديد القيمة القصوى للساعة من خلال الفترة الفائقة لجميع العناصر الدورية في النموذج المصدر (على سبيل المثال، إذا كان النموذج المصدر يحتوي على خيوط بفترات 100 و 200 و 300 ميلي ثانية، ستستخدم SLICED دورة ساعة 600 ميلي ثانية). عندما يوفر النموذج المصدر المواعيد النهائية للأداء، تقيم SLICED حالات المكون مقابل ساعتها الدورية.

للاتصالات بين المكونات، تتعامل SLICED مع كل اتصال كمتغير منفصل أو كخاصية لمتغير موجود. للاتصالات ذات قيود السعة، تتعامل SLICED مع الاتصال كسيمافور عداد وتنشئ تأكيدات تقيد عدد الرسائل التي يمكن أن يحتويها وفقاً لحده الأعلى.

**توليد تأكيدات اكتشاف المسار**

لتوليد تأكيد اكتشاف المسار، تعبر SLICED عن الحالة الأولية (الفاشلة) للنظام في آلة حالة محدودة مع تعيين حالتها الأولية لتشمل خطأً واحداً أو أكثر. تختلف آلة الحالة المحدودة عن تلك المستخدمة لتقييم تأكيدات اكتشاف الأخطاء لأنها تترك إجراءات المستخدم محددة على أنها غير حتمية، مما يتيح فعلياً للحلال أن يتولى دور المستخدم للتلاعب بالنظام كما يشاء. في آلة الحالة المحدودة، فعل المستخدم هو انتقال يعتمد حارسه على حدث إدخال مستخدم (على سبيل المثال، قلب مفتاح) حيث مصدر هذا الحدث خارجي للنظام المنمذج. تولد SLICED بعد ذلك تأكيداً يصف نفي الحالة المرغوبة، بما في ذلك كل من المكون المعطوب الأصلي وجميع المكونات الأخرى في النظام.

**4.2.1 شكلية SLICED**

لكل مكون في النموذج المصدر، نولد آلة حالة ψ. باستخدام الأفعال A على أو بين هذه المكونات كما هو محدد في النموذج المصدر (على سبيل المثال، كاتصالات)، نجمع آلة حالة مركبة Ψ.

**دلالات آلة الحالة**

الدلالات الرسمية لآلة حالة في SLICED هي 6-tuple ψ = (S, A, T ⊆ S × A × S, s₀ ∈ S, E ⊆ S, d ∈ S).

- A—هي مجموعة من الأحداث، أو الأفعال،
- S—هي مجموعة من الحالات للمكون،
- T ⊆ S × A × S—هي مجموعة الانتقالات الموسومة،
- s₀ ∈ S—هي حالة أولية محددة،
- E ⊆ S—هي مجموعة متميزة من حالات الخطأ.

نستخدم اختصاراً للانتقالات من S، كتابة s →ᵃ s' لعنصر t ∈ T.

**آلة الحالة المركبة**

تُبنى آلة الحالة المركبة من كل من النموذج السلوكي المرتبط بكل مكون والاتصالات بينها. آلة الحالة المركبة هي النواة التحليلية لـ SLICED وتصف سلوك النظام بأكمله.

رسمياً، آلة الحالة المركبة هي آلية بوخي موقوتة مبنية من خلال عرض كل مكون كمشغل بشكل مستقل مع إضافة ساعة عامة. في حالة ADAPT، التي ليس لديها قيود توقيت محددة تستخدمها SLICED، تفترض SLICED أن الأحداث تحدث في خطوات زمنية منفصلة. الانتقالات بين الحالات هي اتصالات بين المكونات، تدعم تغييرات الحالة بمشاركة الإنسان من خلال عدم الحتمية. على سبيل المثال، المرحلات القابلة للتعيين من قبل المستخدم لديها انتقالات حالة مفتوحة ومغلقة غير حتمية لمراعاة إجراءات المستخدم. باستخدام بناء مجموعة القوى، يمكننا بناء آلية محدودة حتمية (DFA) لنمذجة سلوك النظام بأكمله [23]. في سياق نموذج Simulink، الانتقال هو حدث يغير الحالة المهمة لمكون كما هو محدد بواسطة نمطه الأساسي. بناء مجموعة القوى الساذج أكبر بشكل أسي من الآلية المحدودة غير الحتمية (NFA) لأي مكون فردي.

رسمياً، بالنظر إلى مجموعة من n آلات حالة سلوكية إدخال ψ₁، ··· ψₙ، باستخدام نموذج بيانات مشترك A، محددة ψⁱ = (Sⁱ, A, Tⁱ ⊆ Sⁱ × A × Sⁱ, sⁱ₀ ∈ S, Eⁱ ⊆ S, d ∈ S)، يتم بناء آلة الحالة المركبة كـ:

Ψ = (⊕ψᵢ) ⊕ A꜀
  c = ساعة
  T = {(···, s, ···) →ᵃ (···, s', ···) لـ s →ᵃ s' انتقال من Sⁱ و S شريحة زمنية من Sᵢ}
  s₀ = (s¹₀, s²₀, ..., sⁿ₀, S₀) ∈ Ψ

**حجم فضاء الحالة**

فضاء الحالة الكامل لآلة الحالة المركبة الساذجة لنموذج بحجم ADAPT كبير تجميعياً، مما يجعل تحليله غير عملي. باستخدام تجريدات المكونات مع مواصفات السلوك المبسطة، تقلل SLICED بشكل كبير من حجم فضاء الحالة ذي الصلة.

نحقق مزيداً من التخفيض في حجم فضاء الحالة باستخدام جدول دوال تجميع الأنظمة الفرعية لطي فضاءات حالة الأنظمة الفرعية الكبيرة للتحليل على مستوى النظام الأعلى، ثم توسيعها لتوليد آثار مفصلة لشروط معينة.

---

### Translation Notes

- **Figures referenced:** Figure 3 (Battery in ADAPT model), Figure 4 (SLICED architecture), Figure 5 (ADAPT components)
- **Key terms introduced:**
  - Compositional approach - نهج تركيبي
  - Black box - صندوق أسود
  - Composite state machine - آلة حالة مركبة
  - Deterministic finite automata - آلية محدودة حتمية
  - Powerset construction - بناء مجموعة القوى
  - Kripke structure - بنية كريبكي
  - Büchi automaton - آلية بوخي
  - Shannon's expansion - توسع شانون
  - Cone of Influence (COI) - مخروط التأثير
  - Error discovery assertion - تأكيد اكتشاف الخطأ
  - Path discovery assertion - تأكيد اكتشاف المسار
  - Safety assertion - تأكيد السلامة
  - Liveness assertion - تأكيد الحيوية
  - Cyclic clock - ساعة دورية
  - Greatest Common Denominator (GCD) - القاسم المشترك الأكبر
  - Hyperperiod - الفترة الفائقة
- **Equations:** Multiple formal definitions and mathematical notation
- **Citations:** [10], [12], [17], [19], [23]
- **Special handling:**
  - Code listings kept in English (industry standard)
  - Mathematical notation preserved
  - Formal definitions numbered and formatted

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.84
- Glossary consistency: 0.87
- **Overall section score:** 0.87
