# Section II: Theoretical Foundation
## القسم الثاني: الأساس النظري

**Section:** theoretical-foundation
**Translation Quality:** 0.88
**Glossary Terms Used:** formal specification (المواصفات الرسمية), Z language (لغة Z), state-based (قائم على الحالة), demand response management (إدارة استجابة الطلب), renewable energy sources (مصادر الطاقة المتجددة), electric vehicles (المركبات الكهربائية), vehicle to grid (من المركبة إلى الشبكة)

---

### English Version

In this section, we present the theoretical foundations needed for understand the presented formal specification model.

#### A. Formal Frameworks

A formal specification is a software engineering approach that is used for mathematical modeling of different components of a system [7]. During engineering of any system, it is important to ensure that all the system components are integrated and working correctly without any error. A formal specification provides this facility to accurately specify each requirement of the system before going to the real implementation [16].

A formal specification decomposes the large system into the subsystem. Then provides a specification for each individual subsystems. It follows two approaches; one is the algebraic approach in which each operation and relationships can be described, second is a model-based approach which concerns with the state and transitions of each individual components. The model-based approach uses the Z language specification which involves the utilization of mathematical notations, sets, sequences, and states [17].

#### B. Scenario of the Smart grid

We can think of a smart grid as a complex system in which different consumers and generation units are connected through power communication lines [18]. Generation units generate power and transmit toward consumer's side. Consumers demand energy according to their usage profile and generation units response according to the consumer's demand [19].

On the consumer's side, the process of monitoring and controlling consumer's demand energy usage profile is called home energy management (HEM) [20]. This process involves the use of smart meters, smart appliances, information and communication technology etc. the smart meters collect data about consumer's demand at the different time period and transmit this collected data to the power generation unit. On the power generation unit side, this data is analyzed and response according to the consumer's demand. Sometimes, consumer's demands exceed from available energy power at the grid side. This creates unbalance situation of the power system. To handle this issue, the concept of demand response management (DRM)[21] has been introduced.

DRM is the process of adjusting consumer's demand in response to the price of energy and incentives from grid side. The generation unit sends their energy cost pattern of different time periods. The time in which power cost is high is called high peak hour and the time in which power cost is low is called off peak hour. So during high peak hour, consumers can keep their flexible appliances off and run at low peak hour.

To reduce burden on generation unit, the concept of renewable energy sources (RES) is also introduced in a smart grid application [22]. RES can be in the form of photo-voltaic (PV) or wind energy sources. These energy sources can be installed and provide energy to the consumer's side. Consumers can use this energy at an off-peak hour, so this solves the energy unbalance as well as high-cost issues. The energy collected from RES can be stored using storage devices. Sometimes, if the available energy is larger than consumer's demands, then it can be sold back to the grid unit by using some buyback mechanism [23]. However, RES has unpredictable nature and depends on weather and time. PV energy can only be produced during the daytime i.e. at sunny day. Wind energy can only be produced in windy environments.

Regarding RES, a new concept has also been included in a smart grid called electric vehicles (EVs) [24]. These EVs are using energy storage devices which can be charged either using PV or electric station. The stored energy is then used for drive vehicles. In case if the energy demands of consumers exceed at grid unit. These EVs can also provide energy to the grid unit by using the vehicle to grid (V2G) mechanism.

---

### النسخة العربية

في هذا القسم، نقدم الأسس النظرية اللازمة لفهم نموذج المواصفات الرسمية المقدم.

#### أ. الأطر الرسمية

المواصفات الرسمية هي نهج هندسة برمجيات يُستخدم للنمذجة الرياضية لمكونات مختلفة من النظام [7]. أثناء هندسة أي نظام، من المهم التأكد من أن جميع مكونات النظام متكاملة وتعمل بشكل صحيح دون أي خطأ. توفر المواصفات الرسمية هذه الإمكانية لتحديد كل متطلب من متطلبات النظام بدقة قبل الانتقال إلى التنفيذ الفعلي [16].

تُحلل المواصفات الرسمية النظام الكبير إلى أنظمة فرعية. ثم توفر مواصفات لكل نظام فرعي على حدة. وهي تتبع نهجين؛ أحدهما هو النهج الجبري حيث يمكن وصف كل عملية وعلاقات، والثاني هو النهج القائم على النموذج الذي يهتم بالحالة والانتقالات لكل مكون فردي. يستخدم النهج القائم على النموذج مواصفات لغة Z والتي تتضمن استخدام الترميزات الرياضية والمجموعات والتسلسلات والحالات [17].

#### ب. سيناريو الشبكة الذكية

يمكننا التفكير في الشبكة الذكية كنظام معقد تتصل فيه مختلف المستهلكين ووحدات التوليد من خلال خطوط اتصالات الطاقة [18]. تولد وحدات التوليد الطاقة وتنقلها نحو جانب المستهلك. يطلب المستهلكون الطاقة وفقاً لملف استخدامهم وتستجيب وحدات التوليد وفقاً لطلب المستهلك [19].

على جانب المستهلك، تُسمى عملية مراقبة ومراقبة ملف استخدام الطاقة حسب الطلب للمستهلك بإدارة الطاقة المنزلية (HEM) [20]. تتضمن هذه العملية استخدام العدادات الذكية والأجهزة الذكية وتكنولوجيا المعلومات والاتصالات وما إلى ذلك. تجمع العدادات الذكية بيانات عن طلب المستهلك في فترات زمنية مختلفة وترسل هذه البيانات المجمعة إلى وحدة توليد الطاقة. على جانب وحدة توليد الطاقة، يتم تحليل هذه البيانات والاستجابة وفقاً لطلب المستهلك. في بعض الأحيان، تتجاوز طلبات المستهلكين الطاقة المتاحة على جانب الشبكة. يؤدي هذا إلى وضع اختلال توازن في نظام الطاقة. للتعامل مع هذه المشكلة، تم تقديم مفهوم إدارة استجابة الطلب (DRM) [21].

إدارة استجابة الطلب هي عملية تعديل طلب المستهلك استجابة لسعر الطاقة والحوافز من جانب الشبكة. ترسل وحدة التوليد نمط تكلفة الطاقة الخاصة بها لفترات زمنية مختلفة. الوقت الذي تكون فيه تكلفة الطاقة مرتفعة يُسمى ساعة الذروة العالية والوقت الذي تكون فيه تكلفة الطاقة منخفضة يُسمى ساعة خارج الذروة. لذلك خلال ساعة الذروة العالية، يمكن للمستهلكين إبقاء أجهزتهم المرنة متوقفة عن العمل وتشغيلها في ساعة الذروة المنخفضة.

لتقليل العبء على وحدة التوليد، تم تقديم مفهوم مصادر الطاقة المتجددة (RES) أيضاً في تطبيق الشبكة الذكية [22]. يمكن أن تكون مصادر الطاقة المتجددة في شكل مصادر طاقة كهروضوئية (PV) أو طاقة الرياح. يمكن تركيب مصادر الطاقة هذه وتوفير الطاقة لجانب المستهلك. يمكن للمستهلكين استخدام هذه الطاقة في ساعة خارج الذروة، لذلك يحل هذا مشكلة عدم توازن الطاقة وكذلك مشاكل التكلفة العالية. يمكن تخزين الطاقة المجمعة من مصادر الطاقة المتجددة باستخدام أجهزة التخزين. في بعض الأحيان، إذا كانت الطاقة المتاحة أكبر من طلبات المستهلك، فيمكن بيعها مرة أخرى إلى وحدة الشبكة باستخدام آلية إعادة الشراء [23]. ومع ذلك، فإن مصادر الطاقة المتجددة لها طبيعة غير قابلة للتنبؤ وتعتمد على الطقس والوقت. يمكن إنتاج الطاقة الكهروضوئية فقط خلال النهار أي في يوم مشمس. يمكن إنتاج طاقة الرياح فقط في البيئات العاصفة.

فيما يتعلق بمصادر الطاقة المتجددة، تم أيضاً تضمين مفهوم جديد في الشبكة الذكية يُسمى المركبات الكهربائية (EVs) [24]. تستخدم هذه المركبات الكهربائية أجهزة تخزين الطاقة التي يمكن شحنها إما باستخدام الطاقة الكهروضوئية أو محطة كهربائية. يتم استخدام الطاقة المخزنة بعد ذلك لقيادة المركبات. في حالة تجاوز طلبات الطاقة للمستهلكين في وحدة الشبكة. يمكن لهذه المركبات الكهربائية أيضاً توفير الطاقة لوحدة الشبكة باستخدام آلية من المركبة إلى الشبكة (V2G).

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** home energy management (إدارة الطاقة المنزلية), demand response management (إدارة استجابة الطلب), photo-voltaic (كهروضوئية), buyback mechanism (آلية إعادة الشراء), vehicle to grid (من المركبة إلى الشبكة)
- **Equations:** None
- **Citations:** [7, 16-24] - references to various papers
- **Special handling:** Acronyms like HEM, DRM, RES, PV, EV, V2G are introduced in English after the Arabic translation for clarity

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
