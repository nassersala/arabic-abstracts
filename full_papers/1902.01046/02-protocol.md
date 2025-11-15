# Section 2: Protocol
## القسم 2: البروتوكول

**Section:** protocol
**Translation Quality:** 0.87
**Glossary Terms Used:** federated learning, mobile devices, cloud, server, TensorFlow, model, checkpoint, aggregation, federated averaging, device, global model, dataset, round, protocol

---

### English Version

## 2.1 Basic Notions

The federated learning system involves two primary participants: mobile devices (Android phones) and a cloud-based FL server. When devices become available, they announce their readiness to the server for a specific FL population—a globally unique identifier for a particular learning task or application.

From thousands of devices signaling availability within a time window, "the server selects a subset of typically a few hundred which are invited to work on a specific FL task." This server-device rendezvous is termed a round, during which devices maintain connection.

The server communicates via an FL plan, which includes "a TensorFlow graph and instructions for how to execute it." Devices receive the current global model parameters through an FL checkpoint—essentially serialized TensorFlow session state. Each participant performs local computation using its dataset, then returns updates as an FL checkpoint to the server for aggregation.

## 2.2 Phases

The protocol advances the global model through three distinct phases per round:

**Selection:** Devices meeting eligibility criteria (charging, connected to unmetered networks) check in via bidirectional stream. "The server selects a subset of connected devices based on certain goals like the optimal number of participating devices (typically a few hundred devices participate in each round)." Unselected devices receive reconnection instructions.

**Configuration:** The server configures based on aggregation mechanisms and transmits the FL plan and global model checkpoint to selected devices.

**Reporting:** "The server waits for the participating devices to report updates. As updates are received, the server aggregates them using Federated Averaging." Straggler devices that miss deadlines are ignored. Configuration parameters spawn flexible time windows, with round success depending on meeting minimum device thresholds.

## 2.3 Pace Steering

Pace steering regulates device connection patterns through a simple flow control mechanism: "the server suggesting to the device the optimum time window to reconnect." For small populations, it ensures simultaneous connections for security and progress. For large populations, "pace steering is used to randomize device check-in times, avoiding the 'thundering herd' problem," while scheduling necessary participation without excess.

The system accounts for diurnal device availability oscillations, adjusting time windows to minimize peak-hour activity while maintaining performance.

---

### النسخة العربية

## 2.1 المفاهيم الأساسية

يتضمن نظام التعلم الاتحادي مشاركَيْن رئيسيَيْن: الأجهزة المحمولة (هواتف Android) وخادم التعلم الاتحادي القائم على السحابة. عندما تصبح الأجهزة متاحة، تعلن عن استعدادها للخادم لمجموعة تعلم اتحادي محددة - وهو معرّف فريد عالمياً لمهمة تعلم أو تطبيق معين.

من بين آلاف الأجهزة التي تُشير إلى توفرها ضمن نافذة زمنية، "يختار الخادم مجموعة فرعية تضم عادةً بضع مئات من الأجهزة التي تُدعى للعمل على مهمة تعلم اتحادي محددة". يُطلق على هذا اللقاء بين الخادم والأجهزة اسم جولة (round)، والتي تحافظ الأجهزة خلالها على الاتصال.

يتواصل الخادم عبر خطة التعلم الاتحادي (FL plan)، والتي تتضمن "رسماً بيانياً لـ TensorFlow وتعليمات حول كيفية تنفيذه". تتلقى الأجهزة معاملات النموذج العام الحالي من خلال نقطة تحقق التعلم الاتحادي (FL checkpoint) - وهي بشكل أساسي حالة جلسة TensorFlow المتسلسلة. يقوم كل مشارك بإجراء حساب محلي باستخدام مجموعة بياناته، ثم يعيد التحديثات كنقطة تحقق للتعلم الاتحادي إلى الخادم للتجميع.

## 2.2 المراحل

يُقدّم البروتوكول النموذج العام من خلال ثلاث مراحل متميزة لكل جولة:

**الاختيار (Selection):** الأجهزة التي تستوفي معايير الأهلية (قيد الشحن، متصلة بشبكات غير محدودة) تسجّل الدخول عبر تدفق ثنائي الاتجاه. "يختار الخادم مجموعة فرعية من الأجهزة المتصلة بناءً على أهداف معينة مثل العدد الأمثل للأجهزة المشاركة (عادةً ما يشارك بضع مئات من الأجهزة في كل جولة)". تتلقى الأجهزة غير المختارة تعليمات إعادة الاتصال.

**التكوين (Configuration):** يقوم الخادم بالتكوين بناءً على آليات التجميع وينقل خطة التعلم الاتحادي ونقطة تحقق النموذج العام إلى الأجهزة المختارة.

**الإبلاغ (Reporting):** "ينتظر الخادم أن تُبلغ الأجهزة المشاركة عن التحديثات. مع استلام التحديثات، يقوم الخادم بتجميعها باستخدام المتوسط الاتحادي (Federated Averaging)". يتم تجاهل الأجهزة المتأخرة التي تفوت المواعيد النهائية. تُنشئ معاملات التكوين نوافذ زمنية مرنة، حيث يعتمد نجاح الجولة على تلبية الحد الأدنى من عتبات الأجهزة.

## 2.3 توجيه الوتيرة

يُنظّم توجيه الوتيرة (Pace Steering) أنماط اتصال الأجهزة من خلال آلية بسيطة للتحكم في التدفق: "يقترح الخادم على الجهاز النافذة الزمنية المثلى لإعادة الاتصال". بالنسبة للمجموعات الصغيرة، يضمن الاتصالات المتزامنة للأمان والتقدم. بالنسبة للمجموعات الكبيرة، "يُستخدم توجيه الوتيرة لجعل أوقات تسجيل دخول الأجهزة عشوائية، متجنباً مشكلة 'القطيع الهادر' (thundering herd)"، مع جدولة المشاركة الضرورية دون فائض.

يأخذ النظام في الاعتبار تذبذبات توفر الأجهزة اليومية، مع تعديل النوافذ الزمنية لتقليل النشاط في ساعات الذروة مع الحفاظ على الأداء.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** FL population, round, FL plan, FL checkpoint, pace steering, selection phase, configuration phase, reporting phase, thundering herd problem
- **Equations:** 0
- **Citations:** 0
- **Special handling:** Technical terms like "FL plan", "FL checkpoint", "pace steering", and "thundering herd" are translated with English terms kept in parentheses for clarity. The three phases (Selection, Configuration, Reporting) are kept in English alongside Arabic translations as they are key technical terms.

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
