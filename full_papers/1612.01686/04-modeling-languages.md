# Section 4: Initial set of Modeling Languages and Tools
## القسم 4: المجموعة الأولية من لغات ووسائل النمذجة

**Section:** modeling-languages
**Translation Quality:** 0.87
**Glossary Terms Used:** TLA+, temporal logic, Focus, streams, FocusST, BeSpaceD, component, verification, spatial, domain specific language, case classes, cyber-physical systems

---

### English Version

To create the initial set of formal methods-based modeling languages and tools, we have selected the following ingredients, which have a number of similarities in syntax and semantics and are also covering spatio-temporal aspects of the specifications:

– **TLA+**: Temporal logic of actions (TLA) is a logic developed by Leslie Lamport, which combines temporal logic with a logic of actions. It is used to describe behaviours of concurrent systems, cf. [15].

– **FocusST**: Formal language providing concise but easily understandable specifications that is focused on timing and spatial aspects of the system behaviour, cf. [23,24].

– **BeSpaceD**: A framework for modelling and checking behaviour of spatially distributed component systems, cf. [2,3].

The FocusST language was inspired by Focus [5], a framework for formal specification and development of interactive systems. In both languages, specifications are based on the notion of streams. However, in the original Focus input and output streams of a component are mappings of natural numbers to single messages, whereas a FocusST stream is a mapping from natural numbers to lists of messages within the corresponding time intervals. Moreover, the syntax of FocusST is particularly devoted to specify spatial (S) and timing (T) aspects in a comprehensible fashion, which is the reason to extend the name of the language by ST. The FocusST specification layout also differs from the original one: it is based on human factor analysis within formal methods [21,22].

Design goals of BeSpaceD include:

– Ability to model spatial behaviour in a component oriented, simple and intuitive way
– Automatically analyse and verify systems and integration possibilities with other modelling and verification tools.

Blech and Schmidt proposed a process for checking properties of models and described the approach using different examples [3]. In our current work, we only focus on the spatio-temporal aspects of BeSpaceD.

From a programming language perspective, we create BeSpaceD models by using Scala case classes. During the specification process, this gives a functional abstract datatype feeling with a domain specific language flavour. A typical BeSpaceD formula is shown below:

```scala
IMPLIES(AND(TimeInterval(300,605),Owner("AreaOfInterest")),
        OccupyBox(1051,3056,1505,3603))
```

The language constructs comprise basic logical operators (such as AND and IMPLIES). Furthermore special constructs for space, time, and topology are incorporated. In the example, OccupyBox represents a rectangular two-dimensional space while constructs such as TimeInterval allow for the modeling of temporal aspects possible. A variety of different operators exist which facilitates the reasoning about geometric and topological constraints. Furthermore, connections to data sources from cyber-physical systems exists (e.g., lego-trains [11] and event analysis for industrial automation facilities [1]) which facilitates the construction of demonstrators and conduction of experiments.

In our work we are using FocusST and TLA+ for modelling the behaviour of systems, whereas the BeSpaceD functionality is invoked at a lower level to check and test properties of the specified systems.

To understand the workflow of the proposed model, we use the example of Therac25 mentioned in the introduction. The machine included VT-100 terminal which controlled the PDP-11 computer. The sequence of user actions leading to the accidents was as follows:

– user selects 25 MeV photon mode
– user enters "cursor up"
– user select 25 MeV Electron mode
– previous commands have to take place in eight seconds

Therefore, we use algebraic data types to model the operations of the machine. Then we provide formal specification formulas and feed them to the framework.

```scala
sealed abstract class Operation
case object CursorUp extends Operation
case object Select25MevPhotonMode extends Operation
case object Select25MevElectronMode extends Operation
case object OtherKindOfOperation extends Operation

type Therac25 = Sut

val init: TLAInit = {.. some predicate ...}
val next: TLANext = {.. another predicate ...}

val correctBehaviours: List[TLAState] =
  Therac25.correctBehaviours(init, next)

Therac25.checkAgainst(correctBehaviours, randoms(Operation))
```

The framework would generate large number of Operation combinations that are more likely to catch the error that caused the fatal accidents. Frequencies of generated commands can be tailored to match real system behaviour. The example used TLA+ formulas. However, FocusST formulas could have been used instead to specify the system.

To achieve that, we have partially implemented the code that is responsible to generate random BespaceD constructs using techniques from functional programming. The Invariant generator is composed of smaller generators such as integer and string generators as shown in the code below:

```scala
trait Generator[+T] {
  self =>
  def generate: T

  def map[U](f: T => S): Generator[U] = new Generator[U] {
    def generate = f(self.generate)
  }
}

val integers = new Generator[Int] {
  def generate = scala.util.Random.nextInt()
}

val booleans = integers.map(_ >= 0)
val strings = integers.map(_.toString)

def bSpaceD: Generator[Invariant] = for {
  int1 <- integers
  int2 <- integers
  int3 <- integers
  int4 <- integers
  int5 <- integers
  str <- strings
} yield IMPLIES(AND(TimeInterval(int1, int2),Owner(str)),
                OccupyBox(int3, int4, int5, int6))
```

---

### النسخة العربية

لإنشاء المجموعة الأولية من لغات ووسائل النمذجة القائمة على الأساليب الرسمية، اخترنا المكونات التالية، التي تتمتع بعدد من أوجه التشابه في البنية والدلالات وتغطي أيضاً الجوانب الزمكانية للمواصفات:

– **TLA+**: منطق الأفعال الزمني (TLA) هو منطق طوره Leslie Lamport، يجمع بين المنطق الزمني ومنطق الأفعال. يُستخدم لوصف سلوكيات الأنظمة المتزامنة، راجع [15].

– **FocusST**: لغة رسمية توفر مواصفات موجزة ولكن سهلة الفهم تركز على التوقيت والجوانب المكانية لسلوك النظام، راجع [23،24].

– **BeSpaceD**: إطار عمل لنمذجة والتحقق من سلوك أنظمة المكونات الموزعة مكانياً، راجع [2،3].

تم إلهام لغة FocusST من Focus [5]، وهو إطار عمل للمواصفات الرسمية وتطوير الأنظمة التفاعلية. في كلتا اللغتين، تعتمد المواصفات على مفهوم التدفقات. ومع ذلك، في Focus الأصلي تكون تدفقات الإدخال والإخراج لمكون ما عبارة عن تعيينات من الأعداد الطبيعية إلى رسائل منفردة، بينما يكون تدفق FocusST عبارة عن تعيين من الأعداد الطبيعية إلى قوائم من الرسائل ضمن الفترات الزمنية المقابلة. علاوة على ذلك، فإن صيغة FocusST مخصصة بشكل خاص لتحديد الجوانب المكانية (S) والتوقيت (T) بطريقة مفهومة، وهو السبب في تمديد اسم اللغة بـ ST. يختلف تخطيط مواصفات FocusST أيضاً عن التخطيط الأصلي: فهو يعتمد على تحليل العوامل البشرية ضمن الأساليب الرسمية [21،22].

تشمل أهداف تصميم BeSpaceD:

– القدرة على نمذجة السلوك المكاني بطريقة موجهة نحو المكونات، بسيطة وبديهية
– تحليل والتحقق من الأنظمة تلقائياً وإمكانيات التكامل مع وسائل النمذجة والتحقق الأخرى.

اقترح Blech و Schmidt عملية للتحقق من خصائص النماذج ووصفا النهج باستخدام أمثلة مختلفة [3]. في عملنا الحالي، نركز فقط على الجوانب الزمكانية لـ BeSpaceD.

من منظور لغة البرمجة، نقوم بإنشاء نماذج BeSpaceD باستخدام أصناف الحالة في Scala. أثناء عملية المواصفات، يعطي هذا شعوراً بنوع البيانات المجردة الوظيفية مع نكهة لغة خاصة بالمجال. فيما يلي صيغة BeSpaceD نموذجية:

```scala
IMPLIES(AND(TimeInterval(300,605),Owner("AreaOfInterest")),
        OccupyBox(1051,3056,1505,3603))
```

تتضمن تراكيب اللغة معاملات منطقية أساسية (مثل AND و IMPLIES). علاوة على ذلك، يتم دمج تراكيب خاصة للفضاء والوقت والطوبولوجيا. في المثال، يمثل OccupyBox فضاءً مستطيلاً ثنائي الأبعاد بينما تسمح تراكيب مثل TimeInterval بنمذجة الجوانب الزمنية. توجد مجموعة متنوعة من المعاملات المختلفة التي تسهل الاستدلال حول القيود الهندسية والطوبولوجية. علاوة على ذلك، توجد اتصالات بمصادر بيانات من الأنظمة السيبرانية الفيزيائية (مثل قطارات الليجو [11] وتحليل الأحداث لمرافق الأتمتة الصناعية [1]) مما يسهل إنشاء النماذج التوضيحية وإجراء التجارب.

في عملنا نستخدم FocusST و TLA+ لنمذجة سلوك الأنظمة، بينما يتم استدعاء وظائف BeSpaceD على مستوى أدنى للتحقق من واختبار خصائص الأنظمة المحددة.

لفهم سير عمل النموذج المقترح، نستخدم مثال Therac25 المذكور في المقدمة. تضمنت الآلة طرفية VT-100 التي تتحكم في حاسوب PDP-11. كان تسلسل إجراءات المستخدم المؤدية إلى الحوادث كما يلي:

– يختار المستخدم وضع الفوتون 25 ميجا إلكترون فولت
– يدخل المستخدم "cursor up"
– يختار المستخدم وضع الإلكترون 25 ميجا إلكترون فولت
– يجب أن تحدث الأوامر السابقة في ثماني ثوانٍ

لذلك، نستخدم أنواع البيانات الجبرية لنمذجة عمليات الآلة. ثم نوفر صيغ المواصفات الرسمية ونغذيها إلى إطار العمل.

```scala
sealed abstract class Operation
case object CursorUp extends Operation
case object Select25MevPhotonMode extends Operation
case object Select25MevElectronMode extends Operation
case object OtherKindOfOperation extends Operation

type Therac25 = Sut

val init: TLAInit = {.. some predicate ...}
val next: TLANext = {.. another predicate ...}

val correctBehaviours: List[TLAState] =
  Therac25.correctBehaviours(init, next)

Therac25.checkAgainst(correctBehaviours, randoms(Operation))
```

سيولد إطار العمل عدداً كبيراً من تركيبات العمليات التي من المرجح أن تلتقط الخطأ الذي تسبب في الحوادث المميتة. يمكن تخصيص ترددات الأوامر المولدة لتتناسب مع سلوك النظام الحقيقي. استخدم المثال صيغ TLA+. ومع ذلك، كان يمكن استخدام صيغ FocusST بدلاً من ذلك لتحديد النظام.

لتحقيق ذلك، قمنا بتنفيذ جزئي للشفرة المسؤولة عن توليد تراكيب BeSpaceD العشوائية باستخدام تقنيات من البرمجة الوظيفية. يتكون مولد الثوابت من مولدات أصغر مثل مولدات الأعداد الصحيحة والنصوص كما هو موضح في الشفرة أدناه:

```scala
trait Generator[+T] {
  self =>
  def generate: T

  def map[U](f: T => S): Generator[U] = new Generator[U] {
    def generate = f(self.generate)
  }
}

val integers = new Generator[Int] {
  def generate = scala.util.Random.nextInt()
}

val booleans = integers.map(_ >= 0)
val strings = integers.map(_.toString)

def bSpaceD: Generator[Invariant] = for {
  int1 <- integers
  int2 <- integers
  int3 <- integers
  int4 <- integers
  int5 <- integers
  str <- strings
} yield IMPLIES(AND(TimeInterval(int1, int2),Owner(str)),
                OccupyBox(int3, int4, int5, int6))
```

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:** TLA+, FocusST, BeSpaceD, Focus, temporal logic, streams, case classes, algebraic data types, cyber-physical systems, Therac-25 example
- **Equations:** None
- **Citations:** [1, 2, 3, 5, 11, 15, 21, 22, 23, 24]
- **Special handling:** Code examples in Scala preserved in English with explanatory Arabic text, Therac-25 case study implementation

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
