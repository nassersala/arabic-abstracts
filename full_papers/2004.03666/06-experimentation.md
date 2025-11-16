# Section 6: Experimentation Evaluation
## القسم 6: تقييم التجربة

**Section:** experimentation
**Translation Quality:** 0.87
**Glossary Terms Used:** validation (التحقق), performance (الأداء), error detection (كشف الأخطاء), counterexample (مثال مضاد), simulation (محاكاة), scalability (قابلية التوسع)

---

### English Version

**6.1 Experiment Overview**

The objective of our experiment was to validate our approach to reducing complex system models to computationally tractable formal state specifications through application of a set of well-defined component archetypes. We determined success by whether we could run formal analysis on the generated state model and that a result found for a success or error discovery assertion in a SLICED model would also manifest in the Virtual ADAPT Simulink model.

**6.2 Application of SLICED to ADAPT**

**Core ADAPT Components**

Virtual ADAPT identifies 97 of its high-level Simulink subsystems as "ADAPT Components," many of which have specified fault conditions. These components fit into several categories: batteries, inverters, load banks, loads, circuit breakers, relays, and sensors.

Aside from loadbanks and sensors, each component is taken to be a state machine with its states and transitions straightforwardly deduced from each type's well-defined fault modes and inferred functionality. Additionally, this abstraction hides the detail associated with the electrical power transfer by describing component's electric states with discrete notions of power supply and consumption.

SLICED is concerned with behavioral interfaces. We identified 52 of the 602 "SubSystem" blocks in the top 6 levels of Virtual ADAPT as having modelable behavioral interfaces (we identified an additional 2 at the 7th level). We determined the applicability of blocks via inspection of their names and uses in ADAPT, for example by identifying any block of type "SubSystem" with a name containing "battery" as behaving according to the Battery behavior prototype.

Using the 52 identified blocks, we generated a NuSMV specification including definitions of each of our re-usable component archetypes, as well as variables defining each of the 52 blocks according to their determined archetype. We implemented connections between the blocks using additional variables internal to each type definition. Figure 5 shows all of these components and their connections.

ADAPT provides connections describing both voltage and amperage on wires between components. In creating the NuSMV representation we combined these connections into a single "draw" connection representing a unitless measure of power consumption. As with our other design abstractions, this choice results in a loss of fidelity but maintains the capacity to reason about the system in terms of relative supply and demand.

**6.3 Results**

**6.3.1 Performance Results**

**Test Platform**

We ran our example analysis on a 64 bit Windows 10 laptop with 24GB of RAM and an Intel i7 CPU running at 2.5 GHz. We used NuSMV version 2.6.0. We measured performance of the NuSMV execution using the PowerShell Measure-Command cmdlet.

We added a simple assertion to the state model, asserting that the draw on Battery1 would be less than one.

```
LTLSPEC G(Battery1.draw < 1)
```

**Nominal Analysis**

Analysis of the generated FSM with no performance improvements applied was computationally intractable, yielding no results after 12 hours.

**Actuator Removal**

We performed several analyses of reduced models, each time starting with the full SLICED-generated model and applying a reduction or adaptation. First, we removed 12 actuators and their associated relays, as shown in Figure 6. Analysis of this model took 3 minutes 8 seconds.

**Battery Subsystem Removal**

Second, we removed Battery2 and all of the 2-prefixed components, as shown in Figure 7. Analysis of this configuration took 8 minutes 34 seconds.

**Smaller Actuator Removal**

Third, we removed eight actuators and relays, as shown in Figure 8. Analysis of this configuration took 5 hours 25 minutes 59 seconds.

**Actuator Subsystem Collapse**

As discussed in Subsubsection 4.1.1 we merged the relays and actuators in two subsystems into abstractions representing only the possible power consumption of the subsystem (see Figure 9). Analysis of this configuration took 26 minutes 51 seconds. This result is of particular note because this reduction did not constitute a reduction in problem scope (as did the other reductions), yet it made the overall problem computationally tractable.

This result will serve as a motivating factor for future research in performance-oriented composition of FSM and model checking problem specification based on traditional engineering models.

**6.4 Validation**

**6.4.1 Error Detection**

As described in Subsection 4.2, we generate assertions on the model based on component archetypes. For example, for breaker CircuitBreakerEY162 we generate an assertion that CircuitBreakerEY162 will remain connected (a safety assertion), as shown in Listing 6.

```
LTLSPEC G(CircuitBreakerEY166.state = connected)
```

The SLICED model was useful in fault determination. For example, it was discovered that sufficient power draw through CircuitBreakerEY162 could cause it to trip and become disconnected, as shown in the counter example in Listing 7.

```
-- specification G CircuitBreakerEY162.state = connected is false
-- as demonstrated by the following execution sequence
Trace Description: LTL Counterexample
Trace Type: Counterexample
-> State: 1.1 <-
CircuitBreakerEY162.state = connected
CircuitBreakerEY162.supplyingPower = TRUE
-> State: 1.2 <-
BankOne.draw = 11
CircuitBreakerEY162.draw = 11
-> State: 1.3 <-
CircuitBreakerEY162.state = broken
```

**Validation with Simulink**

The Virtual ADAPT model is designed to allow user injection of error into the model. The objective of SLICED is to find errors in the design as specified (without injection of specific errors), so to validate SLICED and Virtual ADAPT we manually introduced errors into the Virtual ADAPT model specification (instead of injecting them at runtime).

We replicated the example detection of a circuit breaker tripping on excessive load by changing an actuator's parameters in Virtual ADAPT to increase its power consumption (as described by the counterexample generated by NuSMV). Figure 10 shows a screenshot of Simulink's data viewer tracking the power draw from the actuator (ComputerPower:1) and the state of the circuitbreaker (CircuitBreakerEY162:3). Note that the state of the circuit breaker changes from connected (1) to disconnected (0) shortly after the increase in power consumption from the actuator.

**6.4.2 Fault Mitigation**

**Methodology**

To exercise SLICED as a mechanism for generating error correction plans with ADAPT, we first used SLICED to generate a baseline ADAPT NuSMV specification, then removed some components to make it computationally tractable (as described in Subsubsection 6.3.1). Next, we manually modified that specification to set the initial state of a given component to an error state, for example by initializing Battery2 as dead.

Next, we specified an assertion claiming that "there is no way to return the system to a good state" such as the assertion in Listing 9.

```
-- NuSMV LTL assertion claiming that there is no future
-- state in which all of the listed
-- actuators are nominal and battery 1 is in a nominal state
-- with a power draw of two or less.
LTLSPEC G(
  NEMO.state != nominal |
  L1H.state != nominal |
  DCLoadBox.state != nominal |
  Load2G.state != nominal |
  Battery1.state != nominal |
  Battery1.draw > 2)
```

Finally, we ran NuSMV on the modified model. If a repair plan was possible, NuSMV generated a sequence of steps that could be taken by the user (recall that user-actionable operations are specified as non-deterministic in our model, so NuSMV can vary them at will to generate plan).

We determined that our use of NuSMV discovered repair plans that were valid in the context of the SLICED-generated FSM (that is, they were legal sequences of transitions), but that our generated FSM did not facilitate constraints on the plan discovery so that other desired system constraints are maintained throughout execution of the plan. This meant that we could generate viable repair plans for simple problems (e.g., turn a switch back on), but that attempts to generate multi-step plans were often met with technically valid but practically infeasible results, such as rapidly switching relays on and off.

---

### النسخة العربية

**6.1 نظرة عامة على التجربة**

كان الهدف من تجربتنا هو التحقق من نهجنا لتقليل نماذج الأنظمة المعقدة إلى مواصفات حالة رسمية قابلة للمعالجة حسابياً من خلال تطبيق مجموعة من الأنماط الأساسية للمكونات المحددة جيداً. حددنا النجاح بما إذا كان بإمكاننا تشغيل تحليل رسمي على نموذج الحالة المولد وأن النتيجة الموجودة لنجاح أو تأكيد اكتشاف خطأ في نموذج SLICED ستظهر أيضاً في نموذج Virtual ADAPT Simulink.

**6.2 تطبيق SLICED على ADAPT**

**مكونات ADAPT الأساسية**

يحدد Virtual ADAPT 97 من أنظمته الفرعية عالية المستوى في Simulink كـ "مكونات ADAPT"، والعديد منها لديه حالات أعطال محددة. تتناسب هذه المكونات مع عدة فئات: البطاريات، والعاكسات، وبنوك الحمل، والأحمال، وقواطع الدوائر، والمرحلات، وأجهزة الاستشعار.

بصرف النظر عن بنوك الحمل وأجهزة الاستشعار، يُعتبر كل مكون آلة حالة مع حالاتها وانتقالاتها المستنتجة بشكل مباشر من أوضاع الأعطال المحددة جيداً لكل نوع والوظيفة المستنتجة. بالإضافة إلى ذلك، يخفي هذا التجريد التفاصيل المرتبطة بنقل الطاقة الكهربائية من خلال وصف الحالات الكهربائية للمكون بمفاهيم منفصلة لتوفير واستهلاك الطاقة.

تهتم SLICED بالواجهات السلوكية. حددنا 52 من كتل "SubSystem" الـ 602 في أعلى 6 مستويات من Virtual ADAPT على أنها تحتوي على واجهات سلوكية قابلة للنمذجة (حددنا 2 إضافية في المستوى السابع). حددنا قابلية تطبيق الكتل عن طريق فحص أسمائها واستخداماتها في ADAPT، على سبيل المثال من خلال تحديد أي كتلة من النوع "SubSystem" باسم يحتوي على "battery" على أنها تتصرف وفقاً لنموذج سلوك البطارية.

باستخدام الكتل الـ 52 المحددة، ولدنا مواصفة NuSMV بما في ذلك تعريفات كل من أنماطنا الأساسية للمكونات القابلة لإعادة الاستخدام، بالإضافة إلى المتغيرات التي تحدد كل من الكتل الـ 52 وفقاً لنمطها الأساسي المحدد. قمنا بتنفيذ الاتصالات بين الكتل باستخدام متغيرات إضافية داخلية لكل تعريف نوع. يُظهر الشكل 5 جميع هذه المكونات واتصالاتها.

يوفر ADAPT اتصالات تصف كلاً من الجهد والتيار على الأسلاك بين المكونات. في إنشاء تمثيل NuSMV، جمعنا هذه الاتصالات في اتصال "draw" واحد يمثل مقياساً بدون وحدة لاستهلاك الطاقة. كما هو الحال مع تجريداتنا التصميمية الأخرى، يؤدي هذا الاختيار إلى فقدان الدقة ولكنه يحافظ على القدرة على الاستدلال حول النظام من حيث العرض والطلب النسبي.

**6.3 النتائج**

**6.3.1 نتائج الأداء**

**منصة الاختبار**

قمنا بتشغيل تحليلنا النموذجي على جهاز كمبيوتر محمول بنظام Windows 10 بسعة 64 بت مع 24 جيجابايت من ذاكرة الوصول العشوائي ومعالج Intel i7 يعمل بسرعة 2.5 جيجاهرتز. استخدمنا NuSMV الإصدار 2.6.0. قمنا بقياس أداء تنفيذ NuSMV باستخدام cmdlet PowerShell Measure-Command.

أضفنا تأكيداً بسيطاً إلى نموذج الحالة، مؤكدين أن السحب على Battery1 سيكون أقل من واحد.

```
LTLSPEC G(Battery1.draw < 1)
```

**التحليل الاسمي**

كان تحليل آلة الحالة المحدودة المولدة بدون تطبيق تحسينات الأداء غير قابل للمعالجة حسابياً، ولم يسفر عن أي نتائج بعد 12 ساعة.

**إزالة المشغل**

قمنا بإجراء عدة تحليلات للنماذج المختزلة، في كل مرة نبدأ بنموذج SLICED الكامل المولد ونطبق اختزالاً أو تكييفاً. أولاً، أزلنا 12 مشغلاً ومرحلاتها المرتبطة، كما هو موضح في الشكل 6. استغرق تحليل هذا النموذج 3 دقائق و 8 ثوانٍ.

**إزالة النظام الفرعي للبطارية**

ثانياً، أزلنا Battery2 وجميع المكونات ذات البادئة 2، كما هو موضح في الشكل 7. استغرق تحليل هذا التكوين 8 دقائق و 34 ثانية.

**إزالة مشغل أصغر**

ثالثاً، أزلنا ثمانية مشغلات ومرحلات، كما هو موضح في الشكل 8. استغرق تحليل هذا التكوين 5 ساعات و 25 دقيقة و 59 ثانية.

**طي النظام الفرعي للمشغل**

كما نوقش في القسم الفرعي 4.1.1، دمجنا المرحلات والمشغلات في نظامين فرعيين في تجريدات تمثل فقط استهلاك الطاقة الممكن للنظام الفرعي (انظر الشكل 9). استغرق تحليل هذا التكوين 26 دقيقة و 51 ثانية. هذه النتيجة جديرة بالملاحظة بشكل خاص لأن هذا الاختزال لم يشكل اختزالاً في نطاق المسألة (كما فعلت الاختزالات الأخرى)، ومع ذلك جعل المسألة الإجمالية قابلة للمعالجة حسابياً.

ستكون هذه النتيجة عاملاً تحفيزياً للبحث المستقبلي في التركيب الموجه نحو الأداء لآلات الحالة المحدودة ومواصفة مسألة فحص النماذج بناءً على نماذج الهندسة التقليدية.

**6.4 التحقق**

**6.4.1 كشف الأخطاء**

كما هو موضح في القسم الفرعي 4.2، نولد تأكيدات على النموذج بناءً على الأنماط الأساسية للمكونات. على سبيل المثال، بالنسبة للقاطع CircuitBreakerEY162، نولد تأكيداً بأن CircuitBreakerEY162 سيظل متصلاً (تأكيد سلامة)، كما هو موضح في القائمة 6.

```
LTLSPEC G(CircuitBreakerEY166.state = connected)
```

كان نموذج SLICED مفيداً في تحديد الأعطال. على سبيل المثال، تم اكتشاف أن السحب الكافي للطاقة عبر CircuitBreakerEY162 يمكن أن يتسبب في تعثره وانفصاله، كما هو موضح في المثال المضاد في القائمة 7.

```
-- specification G CircuitBreakerEY162.state = connected is false
-- as demonstrated by the following execution sequence
Trace Description: LTL Counterexample
Trace Type: Counterexample
-> State: 1.1 <-
CircuitBreakerEY162.state = connected
CircuitBreakerEY162.supplyingPower = TRUE
-> State: 1.2 <-
BankOne.draw = 11
CircuitBreakerEY162.draw = 11
-> State: 1.3 <-
CircuitBreakerEY162.state = broken
```

**التحقق مع Simulink**

صُمم نموذج Virtual ADAPT للسماح للمستخدم بحقن خطأ في النموذج. هدف SLICED هو العثور على أخطاء في التصميم كما هو محدد (بدون حقن أخطاء محددة)، لذا للتحقق من SLICED و Virtual ADAPT قدمنا يدوياً أخطاء في مواصفة نموذج Virtual ADAPT (بدلاً من حقنها في وقت التشغيل).

قمنا بتكرار مثال الكشف عن قاطع دائرة يتعثر على حمل زائد من خلال تغيير معاملات المشغل في Virtual ADAPT لزيادة استهلاك الطاقة الخاص به (كما هو موضح بواسطة المثال المضاد الذي ولده NuSMV). يُظهر الشكل 10 لقطة شاشة لعارض بيانات Simulink يتتبع سحب الطاقة من المشغل (ComputerPower:1) وحالة القاطع (CircuitBreakerEY162:3). لاحظ أن حالة القاطع تتغير من متصل (1) إلى منفصل (0) بعد فترة وجيزة من زيادة استهلاك الطاقة من المشغل.

**6.4.2 تخفيف الأعطال**

**المنهجية**

لممارسة SLICED كآلية لتوليد خطط تصحيح الأخطاء مع ADAPT، استخدمنا أولاً SLICED لتوليد مواصفة ADAPT NuSMV الأساسية، ثم أزلنا بعض المكونات لجعلها قابلة للمعالجة حسابياً (كما هو موضح في القسم الفرعي 6.3.1). بعد ذلك، قمنا يدوياً بتعديل تلك المواصفة لتعيين الحالة الأولية لمكون معين إلى حالة خطأ، على سبيل المثال عن طريق تهيئة Battery2 كميت.

بعد ذلك، حددنا تأكيداً يدعي أن "لا توجد طريقة لإعادة النظام إلى حالة جيدة" مثل التأكيد في القائمة 9.

```
-- NuSMV LTL assertion claiming that there is no future
-- state in which all of the listed
-- actuators are nominal and battery 1 is in a nominal state
-- with a power draw of two or less.
LTLSPEC G(
  NEMO.state != nominal |
  L1H.state != nominal |
  DCLoadBox.state != nominal |
  Load2G.state != nominal |
  Battery1.state != nominal |
  Battery1.draw > 2)
```

أخيراً، قمنا بتشغيل NuSMV على النموذج المعدل. إذا كانت خطة الإصلاح ممكنة، ولد NuSMV تسلسلاً من الخطوات التي يمكن أن يتخذها المستخدم (تذكر أن العمليات القابلة للتنفيذ من قبل المستخدم محددة على أنها غير حتمية في نموذجنا، لذا يمكن لـ NuSMV تغييرها كما يشاء لتوليد الخطة).

حددنا أن استخدامنا لـ NuSMV اكتشف خطط إصلاح كانت صالحة في سياق آلة الحالة المحدودة المولدة بواسطة SLICED (أي أنها كانت تسلسلات قانونية من الانتقالات)، ولكن آلة الحالة المحدودة المولدة لدينا لم تسهل القيود على اكتشاف الخطة بحيث يتم الحفاظ على قيود النظام المرغوبة الأخرى طوال تنفيذ الخطة. يعني هذا أنه يمكننا توليد خطط إصلاح قابلة للتطبيق لمشاكل بسيطة (على سبيل المثال، إعادة تشغيل مفتاح)، ولكن المحاولات لتوليد خطط متعددة الخطوات كانت غالباً ما تُواجه بنتائج صالحة تقنياً ولكن غير قابلة للتطبيق عملياً، مثل تبديل المرحلات بسرعة.

---

### Translation Notes

- **Figures referenced:** Figure 5, Figure 6, Figure 7, Figure 8, Figure 9, Figure 10
- **Key terms introduced:**
  - Validation - التحقق
  - Computationally tractable - قابل للمعالجة حسابياً
  - Component archetypes - الأنماط الأساسية للمكونات
  - Behavioral interfaces - الواجهات السلوكية
  - Circuit breaker - القاطع
  - Power consumption - استهلاك الطاقة
  - Counterexample - مثال مضاد
  - Error injection - حقن الأخطاء
  - Repair plan - خطة إصلاح
  - Subsystem collapse - طي النظام الفرعي
- **Equations:** 0
- **Citations:** None directly in this section
- **Special handling:**
  - Code listings and assertions kept in English
  - Performance timing results kept as-is
  - Figure numbers preserved
  - Component names (CircuitBreakerEY162, Battery1, etc.) kept in English

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
