# Section 3: The Railway Signalling Domain
## القسم 3: مجال إشارات السكك الحديدية

**Section:** railway-domain
**Translation Quality:** 0.86
**Glossary Terms Used:** domain engineering (هندسة المجال), track plan (مخطط المسار), route (مسار), interlocking (التشابك), movement authority (سلطة الحركة), domain specific language (لغة خاصة بالمجال), UML (يو إم إل), narrative (السرد)

---

### English Version

**Introduction**

We now introduce the railway signalling domain. We discuss the main elements of this domain and present an established DSL by Bjørner that captures it. Here, we first present the narrative before discussing the UML class diagram.

**3.1 Background: Industrial Practice in the Railway Domain**

In industry, companies such as our industrial partner, Invensys Rail, undertake domain engineering with the aim to "describe all concepts, components and properties within the railway domain". This modelling, for example, includes features such as rail topology (the basic graph underlying the railway), dimensions (e.g., where tracks are with regards to reference points, the length of tracks, etc), and signalling (routes, speed restrictions etc.). Common across all these layers is the notion of a *track plan* as a term to describe layouts of junctions and stations. Track plans combine topological information and the conceptual abstraction of routes, which determine the use of a rail layout.

An example track plan is shown in Figure 4. The intended operation of the train station shown in Figure 4 is: (1) trains enter at X using track LA1, they then proceed across point P1 towards the upper line to platform PLAT1 (i.e. taking route RX1); (2) alternatively, they pass over point P1 towards the lower line and proceed to platform PLAT2 (i.e. taking route RX2); (3) trains from platform PLAT1 can then pass back the lower line using point P2 and exit the station through track LA2 (i.e. taking route R1Y); (4) finally, trains from platform PLAT2 can pass across point P2 and exit the station through track LA2 (i.e. taking route R2Y).

Such a track plan is usually paired with a set of control and release tables to form a scheme plan -- see Figure 4. A scheme plan details the conditions required for route availability. The operational setting and unsetting of points and routes is controlled by an interlocking which is implemented based on this scheme plan.

The control table prescribes that a given route can be used when all tracks in the "clear" column are not occupied by a train, and the points in the "normal" and "reverse" columns are set to those positions. The example control table prescribes that route RX1 can be assigned to a train when units LA1, P1, and PLAT1 are unoccupied and point P1 is in its reverse position, that is, allowing trains to travel to the top line of Figure 4. We note that the track plan in Figure 4 is uni-directional and that if it were bi-directional, there would be routes corresponding to the opposite direction of travel. The rules for these routes would also share tracks with the current rules, stopping the possibility of routes in opposite directions being used at the same time.

The interlocking also allocates so called locks on points to particular route requests. These locks ensure that the point remains locked in position. Such locks are then released according to the information in the release table. For example, the first row of the release table states that for route RX1 the point P1 can be released by the point itself becoming clear. Releasing of these locks allows the corresponding points to be used within another route. Notice, that for a point which splits two routes, i.e. point P1, the lock on the point can be released by the point itself. However, for points that merge two routes, i.e. point P2, there is the added safety check that the point can only be released after the shared parts of the routes are cleared, i.e. track LA2.

Finally, the last element in the dynamic operation of railways is that of train movements. Above, we have described how access to certain routes is granted, and areas of tracks can be released. This follows conventional railway signalling. However, the newer ETCS standard builds on this conventional signalling with the notion of a movement authority. A movement authority can be thought of as an area of railway for which a train can be granted access to travel along. For example, a train may be granted access to move along units LA1 and P1 in Figure 4. The assignment of movement authorities is given by the following narratives:

**N1 -- Extension:** Initially, no train has a movement authority. A request can be made for a train to travel along a particular route. If the route is available (as dictated by the control table) then the train's movement authority can be extended to include the route. The movement authority for a train can contain multiple routes.

**N2 -- Release:** As a train travels it releases regions of railway from its movement authority according to the release table for that route.

Such movement authorities allow the example run illustrated in Figure 5. In the beginning, at time 0, there is no train in the system. At time 1, train A has been detected by track circuit LA1. Train A travels to platform PLAT1 where it resides until it has been overtaken by train B. Train A then travels further and leaves the system. This run illustrates that train A releases the use of point P1 before it exits the full route RX1. This allows for train B to use route RX2 whilst the end of route RX1 is still in use by train A.

**Discussion of Safety Properties**

In railway signalling, many different safety properties have been considered. For example, on the concrete level of an interlocking, one may want to check the concrete property that "Signal x only shows green when route y is free to use". Alternatively, when checking the design of a scheme plan, Moller et al. check that the control table ensures collision-freedom (excluding two trains occupying the same track). Our aim differs slightly, as we consider the assignment of movement authorities which is outlined by the ETCS standard. Therefore we verify that "overlapping movement authorities are not assigned at the same time".

Such a property is at a higher level of abstraction than the properties mentioned previously. However, as movement authorities are extended depending on the rules of the control table, we do in fact cover the property of collision freedom under the assumption that trains are well behaved. That is, if trains stay within their given movement authority, and movement authorities are proven to never overlap, then we know two trains cannot occupy the same track unit.

**3.2 Background: Bjørner's DSL Adapted for ETCS**

The process of identifying, classifying and precisely defining the elements of a domain has been coined as "Domain Engineering" by Bjørner. Bjørner gives such a classification, i.e., DSL, for the railway domain using a narrative which we introduce as a running example.

Figure 1 shows part of the UML class diagram for Bjørner's DSL. A railway is a "Net", built from "Station(s)" that are connected via "Line(s)". A station can have a complex structure, including "Tracks", "Switch Points" (also called points) and "Linear Units". "Tracks" and "Lines" can only contain "Linear Units". All "Unit(s)" are attached together via "Connector(s)". Along with defining these concepts, Bjørner stipulates various well-formedness conditions on such a model, for example, "No two distinct lines and/or stations share units." or "Every line of a net is connected to exactly two, distinct stations".

Bjørner's approach contains the necessary terms to describe the track plan in Figure 4. The whole track plan forms a *station*. This *station* contains all elements such as *switch points* P1 and P2 along with *linear units* LA1, PLAT1, PLAT2, and LA2, and *connectors* c1, c2, ..., c8 for connecting these units. From this point on, we only consider the elements of Bjørner's DSL that we require for modelling track plans we are interested in. Therefore, some of the conditions stipulated by Bjørner do not apply. For example, the track plan given in Figure 4 is open ended. Hence, axioms regarding closed networks, such as the condition "all nets must contain two stations" (leaving no open lines), do not apply to our models.

Bjørner's DSL gains dynamics by attaching a state to each unit. Each unit can be in one of several *states* at a given time. A state is represented using a set of paths, where a path is a pair of distinct connectors (c,c'). A path expresses that a train is allowed to move along a given unit from connector c to connector c'. To combine a unit and a path across it, Bjørner introduces *unit path pairs* by forming pairs from units and paths across them. These paths allow one to describe which direction along a unit a train is allowed to travel. Trains are not an explicit part of Bjørner's DSL. Instead, Bjørner describes the concept of a "Route", which is a dynamic "window" around a train. Concretely, routes are lists of connected units and paths through them. For example, the route from X to PLAT1 of Figure 4 would be captured as the list [(LA1,(c1,c2)), (P1,(c2,c3)), (PLAT1,(c3,c4))]. Bjørner stipulates that a route can be dynamically changed over time using a movement function that, for a given time, gives the set of assigned routes. This movement function extends or shrinks a route by adding or removing units at one or both of its ends. Train movements are modelled using this function.

Finally, Bjørner has formalised his narrative in (the algebraic part of) RSL. Here we adopt the CASL specification language rather than RSL. Our formalisation follows in great part Bjørner's modelling, however, we utilise the CASL features of predicates, subsorting, and structuring in order to obtain a more readable specification text. Our choice of CASL is also due to the greater level of proof support that is available for CASL in the form of the HETS environment, and the institutional base for HETS which allows us to describe how to implement a comorphism from UML class diagrams to CASL in Section 4.2. Overall, the CASL models we present capture the narrative in a similar manner to the RSL models presented by Bjørner.

---

### النسخة العربية

**مقدمة**

نقدم الآن مجال إشارات السكك الحديدية. نناقش العناصر الرئيسية لهذا المجال ونقدم لغة خاصة بالمجال راسخة من قبل Bjørner تلتقطه. هنا، نقدم أولاً السرد قبل مناقشة مخطط فئات UML.

**3.1 خلفية: الممارسة الصناعية في مجال السكك الحديدية**

في الصناعة، تقوم الشركات مثل شريكنا الصناعي، Invensys Rail، بهندسة المجال بهدف "وصف جميع المفاهيم والمكونات والخصائص ضمن مجال السكك الحديدية". تتضمن هذه النمذجة، على سبيل المثال، ميزات مثل طوبولوجيا السكة (الرسم البياني الأساسي الكامن وراء السكة الحديدية)، والأبعاد (مثل موقع المسارات فيما يتعلق بنقاط المرجع، وطول المسارات، وما إلى ذلك)، والإشارات (المسارات، وقيود السرعة، وما إلى ذلك). المشترك عبر جميع هذه الطبقات هو مفهوم *مخطط المسار* كمصطلح لوصف تخطيطات التقاطعات والمحطات. تجمع مخططات المسار بين المعلومات الطوبولوجية والتجريد المفاهيمي للمسارات، والتي تحدد استخدام تخطيط السكة.

يظهر مثال على مخطط المسار في الشكل 4. التشغيل المقصود لمحطة القطار الموضحة في الشكل 4 هو: (1) تدخل القطارات عند X باستخدام المسار LA1، ثم تتابع عبر النقطة P1 نحو الخط العلوي إلى الرصيف PLAT1 (أي باتخاذ المسار RX1)؛ (2) بدلاً من ذلك، تمر فوق النقطة P1 نحو الخط السفلي وتتابع إلى الرصيف PLAT2 (أي باتخاذ المسار RX2)؛ (3) يمكن للقطارات من الرصيف PLAT1 بعد ذلك أن تعود إلى الخط السفلي باستخدام النقطة P2 والخروج من المحطة عبر المسار LA2 (أي باتخاذ المسار R1Y)؛ (4) أخيرًا، يمكن للقطارات من الرصيف PLAT2 أن تمر عبر النقطة P2 والخروج من المحطة عبر المسار LA2 (أي باتخاذ المسار R2Y).

عادةً ما يتم إقران مخطط المسار هذا مع مجموعة من جداول التحكم والإفراج لتشكيل مخطط الخطة -- انظر الشكل 4. يوضح مخطط الخطة الشروط المطلوبة لتوفر المسار. يتم التحكم في الإعداد التشغيلي وإلغاء إعداد النقاط والمسارات بواسطة التشابك الذي يتم تنفيذه بناءً على مخطط الخطة هذا.

يحدد جدول التحكم أنه يمكن استخدام مسار معين عندما لا تكون جميع المسارات في عمود "واضح" مشغولة بواسطة قطار، ويتم تعيين النقاط في أعمدة "عادي" و "عكسي" إلى تلك المواضع. يحدد جدول التحكم في المثال أنه يمكن تعيين المسار RX1 لقطار عندما تكون الوحدات LA1 و P1 و PLAT1 غير مشغولة وتكون النقطة P1 في وضعها العكسي، أي السماح للقطارات بالسفر إلى الخط العلوي من الشكل 4. نلاحظ أن مخطط المسار في الشكل 4 أحادي الاتجاه وأنه إذا كان ثنائي الاتجاه، فستكون هناك مسارات تقابل الاتجاه المعاكس للسفر. ستشارك القواعد لهذه المسارات أيضًا المسارات مع القواعد الحالية، مما يوقف إمكانية استخدام المسارات في اتجاهات معاكسة في نفس الوقت.

يخصص التشابك أيضًا ما يسمى بالأقفال على النقاط لطلبات مسار معينة. تضمن هذه الأقفال بقاء النقطة مقفلة في مكانها. يتم بعد ذلك إطلاق مثل هذه الأقفال وفقًا للمعلومات الواردة في جدول الإفراج. على سبيل المثال، ينص الصف الأول من جدول الإفراج على أنه بالنسبة للمسار RX1، يمكن إطلاق النقطة P1 من خلال النقطة نفسها التي تصبح واضحة. إطلاق هذه الأقفال يسمح باستخدام النقاط المقابلة ضمن مسار آخر. لاحظ أنه بالنسبة للنقطة التي تقسم مسارين، أي النقطة P1، يمكن إطلاق القفل على النقطة بواسطة النقطة نفسها. ومع ذلك، بالنسبة للنقاط التي تدمج مسارين، أي النقطة P2، هناك فحص أمان إضافي بأنه لا يمكن إطلاق النقطة إلا بعد تطهير الأجزاء المشتركة من المسارات، أي المسار LA2.

أخيرًا، العنصر الأخير في التشغيل الديناميكي للسكك الحديدية هو حركات القطار. أعلاه، وصفنا كيفية منح الوصول إلى مسارات معينة، ويمكن إطلاق مناطق من المسارات. هذا يتبع إشارات السكك الحديدية التقليدية. ومع ذلك، يبني معيار ETCS الأحدث على هذه الإشارات التقليدية بمفهوم سلطة الحركة. يمكن اعتبار سلطة الحركة منطقة من السكة الحديدية يمكن منح القطار الوصول إليها للسفر على طولها. على سبيل المثال، قد يُمنح القطار إمكانية الوصول للتحرك على طول الوحدات LA1 و P1 في الشكل 4. يتم إعطاء تعيين سلطات الحركة بالسردات التالية:

**N1 -- التمديد:** في البداية، لا يوجد لدى أي قطار سلطة حركة. يمكن تقديم طلب لقطار للسفر على طول مسار معين. إذا كان المسار متاحًا (كما تمليه جدول التحكم) فيمكن تمديد سلطة حركة القطار لتشمل المسار. يمكن أن تحتوي سلطة الحركة للقطار على مسارات متعددة.

**N2 -- الإفراج:** عندما يسافر القطار، فإنه يطلق مناطق من السكة الحديدية من سلطة حركته وفقًا لجدول الإفراج لذلك المسار.

تسمح سلطات الحركة هذه بالتشغيل المثال الموضح في الشكل 5. في البداية، في الوقت 0، لا يوجد قطار في النظام. في الوقت 1، تم اكتشاف القطار A بواسطة دائرة المسار LA1. يسافر القطار A إلى الرصيف PLAT1 حيث يقيم حتى يتم تجاوزه بواسطة القطار B. ثم يسافر القطار A أبعد من ذلك ويغادر النظام. يوضح هذا التشغيل أن القطار A يطلق استخدام النقطة P1 قبل أن يخرج من المسار الكامل RX1. هذا يسمح للقطار B باستخدام المسار RX2 بينما لا يزال القطار A يستخدم نهاية المسار RX1.

**مناقشة خصائص السلامة**

في إشارات السكك الحديدية، تم النظر في العديد من خصائص السلامة المختلفة. على سبيل المثال، على المستوى الملموس للتشابك، قد يرغب المرء في التحقق من الخاصية الملموسة بأن "الإشارة x تظهر اللون الأخضر فقط عندما يكون المسار y حرًا للاستخدام". بدلاً من ذلك، عند فحص تصميم مخطط الخطة، يتحقق Moller وآخرون من أن جدول التحكم يضمن الخلو من التصادم (باستثناء قطارين يشغلان نفس المسار). يختلف هدفنا قليلاً، حيث نعتبر تعيين سلطات الحركة المحددة في معيار ETCS. لذلك نتحقق من أن "سلطات الحركة المتداخلة لا يتم تعيينها في نفس الوقت".

مثل هذه الخاصية على مستوى أعلى من التجريد من الخصائص المذكورة سابقًا. ومع ذلك، نظرًا لأن سلطات الحركة تمتد اعتمادًا على قواعد جدول التحكم، فإننا في الواقع نغطي خاصية الخلو من التصادم تحت افتراض أن القطارات تتصرف بشكل جيد. أي، إذا بقيت القطارات ضمن سلطة حركتها المعطاة، وثبت أن سلطات الحركة لا تتداخل أبدًا، فإننا نعلم أن قطارين لا يمكنهما احتلال نفس وحدة المسار.

**3.2 خلفية: لغة Bjørner الخاصة بالمجال المُكيّفة لـ ETCS**

تمت صياغة عملية تحديد وتصنيف وتعريف عناصر المجال بدقة على أنها "هندسة المجال" من قبل Bjørner. يعطي Bjørner مثل هذا التصنيف، أي لغة خاصة بالمجال، لمجال السكك الحديدية باستخدام سرد نقدمه كمثال تشغيلي.

يظهر الشكل 1 جزءًا من مخطط فئات UML للغة Bjørner الخاصة بالمجال. السكة الحديدية هي "شبكة"، مبنية من "محطة (محطات)" متصلة عبر "خط (خطوط)". يمكن أن يكون للمحطة بنية معقدة، بما في ذلك "المسارات"، و "نقاط التبديل" (تسمى أيضًا النقاط) و "الوحدات الخطية". يمكن أن تحتوي "المسارات" و "الخطوط" فقط على "وحدات خطية". يتم ربط جميع "الوحدات" معًا عبر "الموصلات". إلى جانب تعريف هذه المفاهيم، ينص Bjørner على شروط التشكيل الجيد المختلفة على مثل هذا النموذج، على سبيل المثال، "لا يوجد خطان و/أو محطتان متميزتان تشتركان في الوحدات." أو "كل خط من الشبكة متصل بمحطتين متميزتين بالضبط".

يحتوي نهج Bjørner على المصطلحات الضرورية لوصف مخطط المسار في الشكل 4. يشكل مخطط المسار بأكمله *محطة*. تحتوي هذه *المحطة* على جميع العناصر مثل *نقاط التبديل* P1 و P2 إلى جانب *الوحدات الخطية* LA1 و PLAT1 و PLAT2 و LA2، و *الموصلات* c1 و c2 و ... و c8 لربط هذه الوحدات. من هذه النقطة فصاعدًا، نعتبر فقط عناصر لغة Bjørner الخاصة بالمجال التي نحتاجها لنمذجة مخططات المسار التي نهتم بها. لذلك، بعض الشروط التي نص عليها Bjørner لا تنطبق. على سبيل المثال، مخطط المسار المعطى في الشكل 4 مفتوح النهاية. وبالتالي، فإن البديهيات المتعلقة بالشبكات المغلقة، مثل الشرط "يجب أن تحتوي جميع الشبكات على محطتين" (لا تترك خطوطًا مفتوحة)، لا تنطبق على نماذجنا.

تكتسب لغة Bjørner الخاصة بالمجال ديناميكية من خلال إرفاق حالة بكل وحدة. يمكن أن تكون كل وحدة في واحدة من عدة *حالات* في وقت معين. يتم تمثيل الحالة باستخدام مجموعة من المسارات، حيث المسار هو زوج من الموصلات المتميزة (c,c'). يعبر المسار عن أن القطار مسموح له بالتحرك على طول وحدة معينة من الموصل c إلى الموصل c'. لدمج وحدة ومسار عبرها، يقدم Bjørner *أزواج مسار الوحدة* من خلال تكوين أزواج من الوحدات والمسارات عبرها. تسمح هذه المسارات بوصف الاتجاه الذي يسمح للقطار بالسفر على طول الوحدة. القطارات ليست جزءًا صريحًا من لغة Bjørner الخاصة بالمجال. بدلاً من ذلك، يصف Bjørner مفهوم "المسار"، وهو "نافذة" ديناميكية حول القطار. بشكل ملموس، المسارات هي قوائم من الوحدات المتصلة والمسارات من خلالها. على سبيل المثال، سيتم التقاط المسار من X إلى PLAT1 من الشكل 4 على أنه القائمة [(LA1,(c1,c2)), (P1,(c2,c3)), (PLAT1,(c3,c4))]. ينص Bjørner على أنه يمكن تغيير المسار ديناميكيًا بمرور الوقت باستخدام دالة حركة تعطي، لوقت معين، مجموعة المسارات المعينة. تمتد دالة الحركة هذه أو تقلص المسار عن طريق إضافة أو إزالة الوحدات في أحد طرفيه أو كليهما. يتم نمذجة حركات القطار باستخدام هذه الدالة.

أخيرًا، قام Bjørner بصياغة سرده رسميًا في (الجزء الجبري من) RSL. هنا نعتمد لغة مواصفات CASL بدلاً من RSL. تتبع صياغتنا الرسمية إلى حد كبير نمذجة Bjørner، ومع ذلك، نستخدم ميزات CASL من المحمولات، والتصنيف الفرعي، والهيكلة من أجل الحصول على نص مواصفات أكثر قابلية للقراءة. يرجع اختيارنا لـ CASL أيضًا إلى المستوى الأكبر من دعم الإثبات المتاح لـ CASL في شكل بيئة HETS، والقاعدة المؤسسية لـ HETS التي تسمح لنا بوصف كيفية تنفيذ كوموفيزم من مخططات فئات UML إلى CASL في القسم 4.2. بشكل عام، تلتقط نماذج CASL التي نقدمها السرد بطريقة مماثلة لنماذج RSL المقدمة من قبل Bjørner.

---

### Translation Notes

- **Figures referenced:** Figure 1 (Bjørner's UML diagram), Figure 4 (track plan with control/release tables), Figure 5 (time/position diagram)
- **Key terms introduced:**
  - Track plan (مخطط المسار)
  - Scheme plan (مخطط الخطة)
  - Interlocking (التشابك)
  - Control table (جدول التحكم)
  - Release table (جدول الإفراج)
  - Movement authority (سلطة الحركة)
  - ETCS (ETCS)
  - RSL (RSL)
  - Unit path pairs (أزواج مسار الوحدة)
  - Domain engineering (هندسة المجال)
- **Railway-specific terminology:** Points, connectors, linear units, routes, stations, nets, lines
- **Special handling:**
  - Railway technical concepts preserved with Arabic translations
  - ETCS and RSL kept as acronyms
  - Narratives N1 and N2 clearly marked
  - Safety property discussion maintained

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
