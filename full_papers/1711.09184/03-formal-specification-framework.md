# Section III: Formal Specification Framework
## القسم الثالث: إطار المواصفات الرسمية

**Section:** formal-specification-framework
**Translation Quality:** 0.87
**Glossary Terms Used:** formal specification (المواصفات الرسمية), schema (مخطط), state transition (انتقال الحالة), Z language (لغة Z), predicate (المسند)

---

### English Version

In this section, we present formal specification models for the smart grid components. In our study, we consider four different entities in a smart grid system. These entities are: appliance, solar, turbine, and storage devices. Each entity has different states as well as associated events that cause state transitions. In table I, summary of each object, states and events are given.

**TABLE I: Smart grid components, their states and events**

| Object | States | Events |
|--------|--------|--------|
| Appliance | Disconnected | Unplugged |
| | Connected | Plugged-in, not in-use |
| | Running | In use |
| Turbine | Not running | No wind |
| | Slow running | Slow wind |
| | Fast running | Fast wind |
| Solar | No energy generation | Night time |
| | Partial energy generation | Day, cloudy |
| | Full energy generation | Day, sunny |
| Storage | Charging | Store energy |
| | Discharging | Consume energy |
| | Not-in-use | remove storage |

#### A. Smart appliance

An appliance object has three distinct states along with events associated with states. As we can see in figure 1, Whenever an unplugged event occurs, the appliance enters in the disconnected state. By plugged-in event, the appliance enters in the connected state. And whenever an in-use event occurs, the appliance remains in the running state.

Next, we present formal specification for an appliance object.

A free type "APPLIANCESTATE" is used to represent different states of an appliance that are disconnected, connected and running.

```
[APPLIANCESTATE] == {disconnected; connected; running}
```

Next, we define an appliance schema that contains "appState" variable of type "APPLIANCESTATE". The value of "appState" can be either disconnected, connected or running.

```
Appliance
    appState: APPLIANCESTATE
```

As we have defined appliance state and appliance schema. Now we can move towards operational schemas.

First, we start by presenting initialization schema named as InitAppliance. In this schema, we declare "Appliance" schema as a variable. In predicate section, we say that on initialization, the state of an appliance must be equal to disconnected.

```
InitAppliance
    Appliance
    appState = disconnected
```

As the plugged-in event occurs, the state of an appliance becomes connected. To show this transition, we define an operational schema called PluggedInAppliance. In the schema, the changing state of an appliance is shown by a delta sign (Δ). In predicate, we say that the state of an appliance is changed from disconnected to the connected state.

```
PluggedInAppliance
    ΔAppliance
    appState = disconnected
    appState' = connected
```

The state of an appliance is also changing whenever an in-use event occurs. Then the appliance remains in a running state. This transition is shown by defining InUseAppliance. Here, again we declare the changing state of an appliance with a delta sign. In predicate, first an appliance must be in the connected state, then we say that the state changes to the running state.

```
InUseAppliance
    ΔAppliance
    appState = connected
    appState' = running
```

As we noted before, when an unplugged event occurs, an appliance goes to the disconnected state. This transition is shown by another schema called UnPluggedAppliance. In the predicate section, we can see that the state of an appliance changes from connected to the disconnected state.

```
UnPluggedAppliance
    ΔAppliance
    appState = connected
    appState' = disconnected
```

An appliance can be in connected but not in use state. This operation is shown by introducing another schema called NotInUseAppliance.

```
NotInUseAppliance
    ΔAppliance
    appState = running
    appState' = connected
```

There can be some scenario in which a schema can be success or there may some error. To understanding the success and error conditions of schemas, we present free type definitions in the form of table II. In the given table, for each schema we define the success and failure conditions.

**TABLE II: Success and error outcomes of the schemas for an appliance entity**

| Schema | Pre-condition for success | Condition for error |
|--------|---------------------------|---------------------|
| PluggedInAppliance | Appliance is disconnected (appState = disconnected) | Already connected (appState = connected) |
| InUseAppliance | Appliance is connected (appState = connected) | Already in running state (appState = running) |
| UnPluggedAppliance | Appliance is connected (appState = connected) | Already in disconnected state (appState = disconnected) |
| NotInUseAppliance | Appliance is running (appState = running) | Already not in not running state (appState ≠ running) |

#### B. Wind turbine system

A wind turbine object has three distinct states named as turbine not running, turbine slow running, and turbine fast running. There are also different events associated with each state that causes a state transition. In figure 2 we can see that when there is no wind, the turbine enters in the "Turbine not running" state. When there is slow wind, turbine runs slowly. And if there is fast wind, the turbine is running fast.

Next, we present formal specification for a turbine object.

First, we start by defining a free type "TURBINESTATE" set. This set comprises of a turbine different states that are "turbineNotRunning, turbineSlowRunning, and turbineFastRunning".

```
[TURBINESTATE] == {turbineNotRunning; turbineSlowRunning; turbineFastRunning}
```

Now, we define a wind turbine system schema by presenting WindTurbine. This schema consists of a variable "trbState" of type TURBINESTATE. The value of this variable can be either "turbineNotRunning", "turbineSlowRunning", or "turbineFastRunning".

```
WindTurbine
    trbState: TURBINESTATE
```

As we have defined turbine's states and turbine's schema, now we move to operational schemas.

First, we start by initializing a turbine entity by presenting InitTurbine schema. In the schema, first, we call the WindTurbine schema. Then in the predicate, we say that the initial state of a turbine must be equal to "turbineNotRunning" state.

```
InitTurbine
    WindTurbine
    trbState = turbineNotRunning
```

As we noted in the state diagram when during slow wind, the state of a turbine becomes "turbineSlowRunning". This transition is shown by defining SlowWind schema. In the schema, we call the WindTurbine schema with a delta sign. In predicate, we say that the state of a turbine is changing from "turbineNotRunning" to the "turbineSlowRunning".

```
SlowWind
    ΔWindTurbine
    trbState = turbineNotRunning
    trbState' = turbineSlowRunning
```

In case of fast wind, a turbine runs fast. To show this process, we present another schema called FastWind. In the schema, again we call WindTurbine schema with a delta sign. In predicate, we say that the state of a turbine changes from slow to fast running.

```
FastWind
    ΔWindTurbine
    trbState = turbineSlowRunning
    trbState' = turbineFastRunning
```

A turbine's state also changes to not running when there is no wind. This transition is shown by introducing NoWind schema. The schema shows that a turbine's state is changed from slow running to not running state.

```
NoWind
    ΔWindTurbine
    trbState = turbineSlowRunning
    trbState' = turbineNotRunning
```

The schemas of the turbine entity can be success or fail when errors occur. So to understand the success and error conditions of each turbine's schemas, we present free type definitions in table III.

**TABLE III: Success and error outcomes of the schemas for a wind turbine entity**

| Schema | Pre-condition for success | Condition for error |
|--------|---------------------------|---------------------|
| SlowWind | Turbine not running (trbState = notRunning) | Already in slow running state (trbState = turbineSlowRunning) |
| FastWind | Turbine is running slowly (trbState = turbineSlowRunning) | Already in Fast running state (trbState = turbineFastRunning) |
| NoWind | Turbine is running slowly (trbState = turbineSlowRunning) | Already in not running state (trbState = turbineNotRunning) |

#### C. Solar system

A solar object has three distinct states named as "no energy generation, partial energy generation, and full energy generation". There are also different events associated with each state that causes a state transition. The states and it's associated events have shown in the figure 3. Next, we present formal specification for a solar object.

First, we begin by introducing a free type "SOLARSTATE" that is used for presenting different states of a solar entity. This set comprises of "noEnergyGeneration, partialEnergyGeneration, and fullEnergyGeneration" states.

```
[SOLARSTATE] == {noEnergyGeneration; partialEnergyGeneration; fullEnergyGeneration}
```

Here, we present a solar system by introducing SolarPanel schema. The schema takes a variable "slrState" of type SOLARSTATE. The value of this variable can be either "noEnergyGeneration", "partialEnergyGeneration" or "fullEnergyGeneration".

```
SolarPanel
    slrState: SOLARSTATE
```

As we have defined solar state and schema, now we move towards the operational schemas.

The initialization process is shown by presenting InitSolar schema. First, the schema calls the SolarPanel schema in the declaration part. In predicate, we defined that the state of a solar is "noEnergyGeneration" at the initial time.

```
InitSolar
    SolarPanel
    slrState = noEnergyGeneration
```

As we know that when there is a cloud at daytime, then the solar generates partial energy. During this time period, the solar remains in a partial energy generation state. This process is shown by introducing DayAndCloudy schema. In the schema, the changing state of a solar is shown by a delta sign. In predicate, it shows that the state of solar changes from no generation to the partial generation.

```
DayAndCloudy
    ΔSolarPanel
    slrState = noEnergyGeneration
    slrState' = partialEnergyGeneration
```

In case of the sunny day, a solar remains in a full generation state. This process is shown by defining DayAndSunny schema. Here, we again define the changing state of a solar with delta sign. In predicate, we say that the state of solar changes from partial to full energy generation.

```
DayAndSunny
    ΔSolarPanel
    slrState = partialEnergyGeneration
    slrState' = fullEnergyGeneration
```

As we know that a solar does not generate any energy during night time. At this time period, solar remains in a no generation state. Here, we present another schema called "Night". In the schema, we say that the current state of a solar can be partial or full energy generation. Then we change solar state to the no energy generation state.

```
Night
    ΔSolarPanel
    slrState = partialEnergyGeneration ∨ fullEnergyGeneration
    slrState' = noEnergyGeneration
```

The success and failure conditions for the solar's schemas is summarized in table IV.

**TABLE IV: Success and error outcomes of the schemas for a solar entity**

| Schema | Pre-condition for success | Condition for error |
|--------|---------------------------|---------------------|
| DayAndCloudy | Solar is in no generation state (slrState = noGeneration) | Already in partial generation state (slrState = partialEnergyGeneration) |
| DayAndSunny | Solar is in partial state (slrState = partialEnergyGeneration) | Already in full generation state (slrState = fullEnergyGeneration) |
| Night | Solar is in partial or full state (slrState = PartialEnergyGeneration ∨ fullEnergyGeneration) | Already in no generation state (slrState = noEnergyGeneration) |

#### D. Storage system

A storage device also has different states as well as events that cause the transition of states. As we can see in the figure 4 that there are three states named as "charging, discharging, and not in use" of a storage object. When a store energy or battery low event occurs, the storage enters in the charging state. In case of energy consumption, the state of storage becomes discharging, In case remove event, the state of storage becomes not in use.

Next, we present formal specification for a storage system.

First, we start by defining a free type STORAGESTATE set that comprises of different state of a storage device.

```
[STORAGESTATE] == {charging; discharging; notInUse}
```

Here, we define a storage system schema. In the schema, we declare a variable "strState" of type STORAGESTATE that has any single value from the storage state set.

```
StorageDevice
    strState: STORAGESTATE
```

As we have defined storage state and system schema. Now, we move towards operational schema.

First, we start by introducing an initialization schema called InitStorage. This schema calls the StorageDevice schema as a variable. In predicate, it shows that the state of a storage is "notInUse" at the initial time.

```
InitStorage
    StorageDevice
    strState = notInUse
```

As we noted before, when a store energy event occurs, a storage goes to the charging state. This process is shown by StoreEnergy schema. The changing of a storage is shown by a delta sign. In predicate, it shows that the current state of a storage is "notInUse" which is changed to the "charging" state.

```
StoreEnergy
    ΔStorageDevice
    strState = notInUse
    strState' = charging
```

We also know that when a consume energy event occurs, a storage device goes to the discharging state. This process is shown by presenting ConsumeEnergy schema. In the schema, we can see that the state of a storage changes from charging to the discharging state.

```
ConsumeEnergy
    ΔStorageDevice
    strState = charging
    strState' = discharging
```

A storage can also enter in the charging state whenever the storage state is low. This process is presented by means of BatteryLow schema.

```
BatteryLow
    ΔStorageDevice
    strState = discharging
    strState' = charging
```

When a storage is removed from the system, then it goes to the "notInUse" state. This process is shown by introducing another schema called RemoveStorage. In the schema, we can see a storage can be in either charging or discharging state. Then it's state changes to the "notInUse" state.

```
RemoveStorage
    ΔStorageDevice
    strState = charging ∨ discharging
    strState' = notInUse
```

The schemas of the storage devices can be success and may be there some errors at the execution time. So there is also need to define the success and error criteria for schemas. Here, in table V, we summarized all success and failure conditions of the storage's schemas.

**TABLE V: Success and error outcomes of the schemas for a storage entity**

| Schema | Pre-condition for success | Condition for error |
|--------|---------------------------|---------------------|
| StoreEnergy | Storage is in not-in use (strState = notInUse) | Already in charging state (strState = charging) |
| ConsumeEnergy | Storage is in charging state (strState = charging) | Already in discharging state (strState = discharging) |
| BatteryLow | Storage is in discharging state (strState = discharging) | Already in charging state (strState = charging) |
| RemoveStorage | Storage is in charging or discharging state (strState = discharging ∨ charging) | Already in not-in-use state (strState = notInUse) |

---

### النسخة العربية

في هذا القسم، نقدم نماذج المواصفات الرسمية لمكونات الشبكة الذكية. في دراستنا، نأخذ في الاعتبار أربعة كيانات مختلفة في نظام الشبكة الذكية. هذه الكيانات هي: الجهاز، والألواح الشمسية، والتوربين، وأجهزة التخزين. كل كيان له حالات مختلفة بالإضافة إلى أحداث مرتبطة تسبب انتقالات الحالة. في الجدول I، يتم تقديم ملخص لكل كائن وحالاته وأحداثه.

**الجدول I: مكونات الشبكة الذكية وحالاتها وأحداثها**

| الكائن | الحالات | الأحداث |
|--------|---------|---------|
| الجهاز | غير متصل | فصل الاتصال |
| | متصل | توصيل، غير قيد الاستخدام |
| | قيد التشغيل | قيد الاستخدام |
| التوربين | غير قيد التشغيل | لا توجد رياح |
| | تشغيل بطيء | رياح بطيئة |
| | تشغيل سريع | رياح سريعة |
| الألواح الشمسية | لا توليد للطاقة | وقت الليل |
| | توليد طاقة جزئي | نهار، غائم |
| | توليد طاقة كامل | نهار، مشمس |
| التخزين | قيد الشحن | تخزين الطاقة |
| | قيد التفريغ | استهلاك الطاقة |
| | غير مستخدم | إزالة التخزين |

#### أ. الجهاز الذكي

كائن الجهاز له ثلاث حالات مميزة إلى جانب الأحداث المرتبطة بالحالات. كما يمكننا أن نرى في الشكل 1، عندما يحدث حدث فصل الاتصال، يدخل الجهاز في حالة غير متصل. من خلال حدث التوصيل، يدخل الجهاز في الحالة المتصلة. وكلما حدث حدث قيد الاستخدام، يبقى الجهاز في حالة التشغيل.

بعد ذلك، نقدم المواصفات الرسمية لكائن الجهاز.

يُستخدم نوع حر "APPLIANCESTATE" لتمثيل حالات مختلفة للجهاز وهي غير متصل، متصل، وقيد التشغيل.

```
[APPLIANCESTATE] == {disconnected; connected; running}
```

بعد ذلك، نعرّف مخطط الجهاز الذي يحتوي على متغير "appState" من نوع "APPLIANCESTATE". يمكن أن تكون قيمة "appState" إما غير متصل أو متصل أو قيد التشغيل.

```
Appliance
    appState: APPLIANCESTATE
```

بما أننا عرّفنا حالة الجهاز ومخطط الجهاز، الآن يمكننا الانتقال نحو المخططات التشغيلية.

أولاً، نبدأ بتقديم مخطط التهيئة المسمى InitAppliance. في هذا المخطط، نعلن عن مخطط "Appliance" كمتغير. في قسم المسند، نقول إنه عند التهيئة، يجب أن تكون حالة الجهاز مساوية لغير متصل.

```
InitAppliance
    Appliance
    appState = disconnected
```

عند حدوث حدث التوصيل، تصبح حالة الجهاز متصلة. لإظهار هذا الانتقال، نعرّف مخططاً تشغيلياً يُسمى PluggedInAppliance. في المخطط، يتم عرض حالة الجهاز المتغيرة بعلامة دلتا (Δ). في المسند، نقول إن حالة الجهاز تتغير من غير متصل إلى الحالة المتصلة.

```
PluggedInAppliance
    ΔAppliance
    appState = disconnected
    appState' = connected
```

تتغير حالة الجهاز أيضاً عندما يحدث حدث قيد الاستخدام. ثم يبقى الجهاز في حالة التشغيل. يتم عرض هذا الانتقال من خلال تعريف InUseAppliance. هنا، مرة أخرى نعلن عن حالة الجهاز المتغيرة بعلامة دلتا. في المسند، أولاً يجب أن يكون الجهاز في الحالة المتصلة، ثم نقول إن الحالة تتغير إلى حالة التشغيل.

```
InUseAppliance
    ΔAppliance
    appState = connected
    appState' = running
```

كما ذكرنا من قبل، عندما يحدث حدث فصل الاتصال، يذهب الجهاز إلى الحالة غير المتصلة. يتم عرض هذا الانتقال من خلال مخطط آخر يُسمى UnPluggedAppliance. في قسم المسند، يمكننا أن نرى أن حالة الجهاز تتغير من متصل إلى الحالة غير المتصلة.

```
UnPluggedAppliance
    ΔAppliance
    appState = connected
    appState' = disconnected
```

يمكن أن يكون الجهاز في حالة متصل ولكن غير قيد الاستخدام. يتم عرض هذه العملية من خلال تقديم مخطط آخر يُسمى NotInUseAppliance.

```
NotInUseAppliance
    ΔAppliance
    appState = running
    appState' = connected
```

يمكن أن يكون هناك بعض السيناريو الذي يمكن فيه أن ينجح المخطط أو قد يكون هناك خطأ ما. لفهم شروط النجاح والخطأ للمخططات، نقدم تعريفات النوع الحر في شكل جدول II. في الجدول المعطى، لكل مخطط نعرف شروط النجاح والفشل.

**الجدول II: نتائج النجاح والخطأ للمخططات لكيان الجهاز**

| المخطط | الشرط المسبق للنجاح | شرط الخطأ |
|--------|---------------------|-----------|
| PluggedInAppliance | الجهاز غير متصل (appState = disconnected) | متصل بالفعل (appState = connected) |
| InUseAppliance | الجهاز متصل (appState = connected) | في حالة التشغيل بالفعل (appState = running) |
| UnPluggedAppliance | الجهاز متصل (appState = connected) | في الحالة غير المتصلة بالفعل (appState = disconnected) |
| NotInUseAppliance | الجهاز قيد التشغيل (appState = running) | ليس في حالة التشغيل بالفعل (appState ≠ running) |

#### ب. نظام توربينات الرياح

كائن توربينات الرياح له ثلاث حالات مميزة تُسمى التوربين غير قيد التشغيل، التوربين قيد التشغيل البطيء، والتوربين قيد التشغيل السريع. هناك أيضاً أحداث مختلفة مرتبطة بكل حالة تسبب انتقال الحالة. في الشكل 2 يمكننا أن نرى أنه عندما لا توجد رياح، يدخل التوربين في حالة "التوربين غير قيد التشغيل". عندما تكون هناك رياح بطيئة، يعمل التوربين ببطء. وإذا كانت هناك رياح سريعة، فإن التوربين يعمل بسرعة.

بعد ذلك، نقدم المواصفات الرسمية لكائن التوربين.

أولاً، نبدأ بتعريف مجموعة النوع الحر "TURBINESTATE". تتكون هذه المجموعة من حالات مختلفة للتوربين وهي "turbineNotRunning، turbineSlowRunning، وturbineFastRunning".

```
[TURBINESTATE] == {turbineNotRunning; turbineSlowRunning; turbineFastRunning}
```

الآن، نعرّف مخطط نظام توربينات الرياح من خلال تقديم WindTurbine. يتكون هذا المخطط من متغير "trbState" من نوع TURBINESTATE. يمكن أن تكون قيمة هذا المتغير إما "turbineNotRunning" أو "turbineSlowRunning" أو "turbineFastRunning".

```
WindTurbine
    trbState: TURBINESTATE
```

بما أننا عرّفنا حالات التوربين ومخطط التوربين، الآن ننتقل إلى المخططات التشغيلية.

أولاً، نبدأ بتهيئة كيان التوربين من خلال تقديم مخطط InitTurbine. في المخطط، أولاً، نستدعي مخطط WindTurbine. ثم في المسند، نقول إن الحالة الأولية للتوربين يجب أن تكون مساوية لحالة "turbineNotRunning".

```
InitTurbine
    WindTurbine
    trbState = turbineNotRunning
```

كما لاحظنا في مخطط الحالة عندما تكون هناك رياح بطيئة، تصبح حالة التوربين "turbineSlowRunning". يتم عرض هذا الانتقال من خلال تعريف مخطط SlowWind. في المخطط، نستدعي مخطط WindTurbine بعلامة دلتا. في المسند، نقول إن حالة التوربين تتغير من "turbineNotRunning" إلى "turbineSlowRunning".

```
SlowWind
    ΔWindTurbine
    trbState = turbineNotRunning
    trbState' = turbineSlowRunning
```

في حالة الرياح السريعة، يعمل التوربين بسرعة. لإظهار هذه العملية، نقدم مخططاً آخر يُسمى FastWind. في المخطط، مرة أخرى نستدعي مخطط WindTurbine بعلامة دلتا. في المسند، نقول إن حالة التوربين تتغير من التشغيل البطيء إلى التشغيل السريع.

```
FastWind
    ΔWindTurbine
    trbState = turbineSlowRunning
    trbState' = turbineFastRunning
```

تتغير حالة التوربين أيضاً إلى غير قيد التشغيل عندما لا توجد رياح. يتم عرض هذا الانتقال من خلال تقديم مخطط NoWind. يُظهر المخطط أن حالة التوربين تتغير من التشغيل البطيء إلى حالة عدم التشغيل.

```
NoWind
    ΔWindTurbine
    trbState = turbineSlowRunning
    trbState' = turbineNotRunning
```

يمكن أن تنجح مخططات كيان التوربين أو تفشل عند حدوث أخطاء. لذلك لفهم شروط النجاح والخطأ لكل مخططات التوربين، نقدم تعريفات النوع الحر في الجدول III.

**الجدول III: نتائج النجاح والخطأ للمخططات لكيان توربينات الرياح**

| المخطط | الشرط المسبق للنجاح | شرط الخطأ |
|--------|---------------------|-----------|
| SlowWind | التوربين غير قيد التشغيل (trbState = notRunning) | في حالة التشغيل البطيء بالفعل (trbState = turbineSlowRunning) |
| FastWind | التوربين يعمل ببطء (trbState = turbineSlowRunning) | في حالة التشغيل السريع بالفعل (trbState = turbineFastRunning) |
| NoWind | التوربين يعمل ببطء (trbState = turbineSlowRunning) | في حالة عدم التشغيل بالفعل (trbState = turbineNotRunning) |

#### ج. نظام الألواح الشمسية

كائن الألواح الشمسية له ثلاث حالات مميزة تُسمى "لا توليد للطاقة، توليد طاقة جزئي، وتوليد طاقة كامل". هناك أيضاً أحداث مختلفة مرتبطة بكل حالة تسبب انتقال الحالة. تم عرض الحالات وأحداثها المرتبطة في الشكل 3. بعد ذلك، نقدم المواصفات الرسمية لكائن الألواح الشمسية.

أولاً، نبدأ بتقديم نوع حر "SOLARSTATE" الذي يُستخدم لتقديم حالات مختلفة لكيان الألواح الشمسية. تتكون هذه المجموعة من حالات "noEnergyGeneration، partialEnergyGeneration، وfullEnergyGeneration".

```
[SOLARSTATE] == {noEnergyGeneration; partialEnergyGeneration; fullEnergyGeneration}
```

هنا، نقدم نظام الألواح الشمسية من خلال تقديم مخطط SolarPanel. يأخذ المخطط متغير "slrState" من نوع SOLARSTATE. يمكن أن تكون قيمة هذا المتغير إما "noEnergyGeneration" أو "partialEnergyGeneration" أو "fullEnergyGeneration".

```
SolarPanel
    slrState: SOLARSTATE
```

بما أننا عرّفنا حالة الألواح الشمسية والمخطط، الآن ننتقل نحو المخططات التشغيلية.

يتم عرض عملية التهيئة من خلال تقديم مخطط InitSolar. أولاً، يستدعي المخطط مخطط SolarPanel في جزء الإعلان. في المسند، عرّفنا أن حالة الألواح الشمسية هي "noEnergyGeneration" في الوقت الأولي.

```
InitSolar
    SolarPanel
    slrState = noEnergyGeneration
```

كما نعلم أنه عندما يكون هناك غيوم في وقت النهار، فإن الألواح الشمسية تولد طاقة جزئية. خلال هذه الفترة الزمنية، تبقى الألواح الشمسية في حالة توليد طاقة جزئي. يتم عرض هذه العملية من خلال تقديم مخطط DayAndCloudy. في المخطط، يتم عرض حالة الألواح الشمسية المتغيرة بعلامة دلتا. في المسند، يُظهر أن حالة الألواح الشمسية تتغير من عدم التوليد إلى التوليد الجزئي.

```
DayAndCloudy
    ΔSolarPanel
    slrState = noEnergyGeneration
    slrState' = partialEnergyGeneration
```

في حالة اليوم المشمس، تبقى الألواح الشمسية في حالة التوليد الكامل. يتم عرض هذه العملية من خلال تعريف مخطط DayAndSunny. هنا، مرة أخرى نعرّف حالة الألواح الشمسية المتغيرة بعلامة دلتا. في المسند، نقول إن حالة الألواح الشمسية تتغير من التوليد الجزئي إلى توليد الطاقة الكامل.

```
DayAndSunny
    ΔSolarPanel
    slrState = partialEnergyGeneration
    slrState' = fullEnergyGeneration
```

كما نعلم أن الألواح الشمسية لا تولد أي طاقة خلال وقت الليل. في هذه الفترة الزمنية، تبقى الألواح الشمسية في حالة عدم التوليد. هنا، نقدم مخططاً آخر يُسمى "Night". في المخطط، نقول إن الحالة الحالية للألواح الشمسية يمكن أن تكون توليد طاقة جزئي أو كامل. ثم نغير حالة الألواح الشمسية إلى حالة عدم توليد الطاقة.

```
Night
    ΔSolarPanel
    slrState = partialEnergyGeneration ∨ fullEnergyGeneration
    slrState' = noEnergyGeneration
```

يتم تلخيص شروط النجاح والفشل لمخططات الألواح الشمسية في الجدول IV.

**الجدول IV: نتائج النجاح والخطأ للمخططات لكيان الألواح الشمسية**

| المخطط | الشرط المسبق للنجاح | شرط الخطأ |
|--------|---------------------|-----------|
| DayAndCloudy | الألواح الشمسية في حالة عدم التوليد (slrState = noGeneration) | في حالة التوليد الجزئي بالفعل (slrState = partialEnergyGeneration) |
| DayAndSunny | الألواح الشمسية في حالة جزئية (slrState = partialEnergyGeneration) | في حالة التوليد الكامل بالفعل (slrState = fullEnergyGeneration) |
| Night | الألواح الشمسية في حالة جزئية أو كاملة (slrState = PartialEnergyGeneration ∨ fullEnergyGeneration) | في حالة عدم التوليد بالفعل (slrState = noEnergyGeneration) |

#### د. نظام التخزين

جهاز التخزين له أيضاً حالات مختلفة بالإضافة إلى أحداث تسبب انتقال الحالات. كما يمكننا أن نرى في الشكل 4 أن هناك ثلاث حالات تُسمى "الشحن، التفريغ، وغير مستخدم" لكائن التخزين. عندما يحدث حدث تخزين الطاقة أو حدث انخفاض البطارية، يدخل التخزين في حالة الشحن. في حالة استهلاك الطاقة، تصبح حالة التخزين تفريغ، في حالة حدث الإزالة، تصبح حالة التخزين غير مستخدم.

بعد ذلك، نقدم المواصفات الرسمية لنظام التخزين.

أولاً، نبدأ بتعريف مجموعة النوع الحر STORAGESTATE التي تتكون من حالة مختلفة لجهاز التخزين.

```
[STORAGESTATE] == {charging; discharging; notInUse}
```

هنا، نعرّف مخطط نظام التخزين. في المخطط، نعلن عن متغير "strState" من نوع STORAGESTATE الذي له قيمة واحدة من مجموعة حالة التخزين.

```
StorageDevice
    strState: STORAGESTATE
```

بما أننا عرّفنا حالة التخزين ومخطط النظام، الآن، ننتقل نحو المخطط التشغيلي.

أولاً، نبدأ بتقديم مخطط تهيئة يُسمى InitStorage. يستدعي هذا المخطط مخطط StorageDevice كمتغير. في المسند، يُظهر أن حالة التخزين هي "notInUse" في الوقت الأولي.

```
InitStorage
    StorageDevice
    strState = notInUse
```

كما لاحظنا من قبل، عندما يحدث حدث تخزين الطاقة، يذهب التخزين إلى حالة الشحن. يتم عرض هذه العملية من خلال مخطط StoreEnergy. يتم عرض تغيير التخزين بعلامة دلتا. في المسند، يُظهر أن الحالة الحالية للتخزين هي "notInUse" والتي تتغير إلى حالة "charging".

```
StoreEnergy
    ΔStorageDevice
    strState = notInUse
    strState' = charging
```

نعلم أيضاً أنه عندما يحدث حدث استهلاك الطاقة، يذهب جهاز التخزين إلى حالة التفريغ. يتم عرض هذه العملية من خلال تقديم مخطط ConsumeEnergy. في المخطط، يمكننا أن نرى أن حالة التخزين تتغير من الشحن إلى حالة التفريغ.

```
ConsumeEnergy
    ΔStorageDevice
    strState = charging
    strState' = discharging
```

يمكن للتخزين أيضاً الدخول في حالة الشحن عندما تكون حالة التخزين منخفضة. يتم تقديم هذه العملية بواسطة مخطط BatteryLow.

```
BatteryLow
    ΔStorageDevice
    strState = discharging
    strState' = charging
```

عندما تتم إزالة التخزين من النظام، فإنه يذهب إلى حالة "notInUse". يتم عرض هذه العملية من خلال تقديم مخطط آخر يُسمى RemoveStorage. في المخطط، يمكننا أن نرى أن التخزين يمكن أن يكون في حالة الشحن أو التفريغ. ثم تتغير حالته إلى حالة "notInUse".

```
RemoveStorage
    ΔStorageDevice
    strState = charging ∨ discharging
    strState' = notInUse
```

يمكن أن تنجح مخططات أجهزة التخزين وقد تكون هناك بعض الأخطاء في وقت التنفيذ. لذلك هناك أيضاً حاجة لتعريف معايير النجاح والخطأ للمخططات. هنا، في الجدول V، لخصنا جميع شروط النجاح والفشل لمخططات التخزين.

**الجدول V: نتائج النجاح والخطأ للمخططات لكيان التخزين**

| المخطط | الشرط المسبق للنجاح | شرط الخطأ |
|--------|---------------------|-----------|
| StoreEnergy | التخزين في حالة عدم الاستخدام (strState = notInUse) | في حالة الشحن بالفعل (strState = charging) |
| ConsumeEnergy | التخزين في حالة الشحن (strState = charging) | في حالة التفريغ بالفعل (strState = discharging) |
| BatteryLow | التخزين في حالة التفريغ (strState = discharging) | في حالة الشحن بالفعل (strState = charging) |
| RemoveStorage | التخزين في حالة الشحن أو التفريغ (strState = discharging ∨ charging) | في حالة عدم الاستخدام بالفعل (strState = notInUse) |

---

### Translation Notes

- **Figures referenced:** Figure 1 (Appliance lifetime), Figure 2 (Wind turbine lifetime), Figure 3 (Solar lifetime), Figure 4 (Storage lifetime)
- **Key terms introduced:** schema (مخطط), predicate (المسند), delta sign (علامة دلتا), state transition (انتقال الحالة), free type (نوع حر), operational schema (مخطط تشغيلي)
- **Equations:** Z specification notation preserved in English (standard practice for formal methods)
- **Citations:** None in this section
- **Special handling:** All Z specification code blocks are kept in original English as this is the standard practice for formal specifications. The explanatory text around the specifications is translated to Arabic.

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
