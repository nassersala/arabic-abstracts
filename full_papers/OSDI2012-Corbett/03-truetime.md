# Section 3: TrueTime
## القسم 3: TrueTime

**Section:** truetime
**Translation Quality:** 0.89
**Glossary Terms Used:** API (واجهة برمجة التطبيقات), uncertainty (عدم اليقين), GPS (نظام تحديد المواقع العالمي), atomic clocks (الساعات الذرية), daemon (عفريت/خدمة), synchronization (المزامنة), clock drift (انحراف الساعة)

---

### English Version

This section describes the TrueTime API and sketches its implementation. We leave most of the details for another paper: our goal is to demonstrate the power of having such an API. Table 1 lists the methods of the API. TrueTime explicitly represents time as a TTinterval, which is an interval with bounded time uncertainty (unlike standard time interfaces that give clients no notion of uncertainty). The endpoints of a TTinterval are of type TTstamp. The TT.now() method returns a TTinterval that is guaranteed to contain the absolute time during which TT.now() was invoked. The time epoch is analogous to UNIX time with leap-second smearing. Define the instantaneous error bound as ε, which is half of the interval's width, and the average error bound as ε̄.

**Table 1: TrueTime API**

| Method | Returns |
|--------|---------|
| TT.now() | TTinterval: [earliest, latest] |
| TT.after(t) | true if t has definitely passed |
| TT.before(t) | true if t has definitely not arrived |

The argument t is of type TTstamp.

The TT.after() and TT.before() methods are convenience wrappers around TT.now(). Denote the absolute time of an event e by the function t_abs(e). In more formal terms, TrueTime guarantees that for an invocation tt = TT.now(), tt.earliest ≤ t_abs(e_now) ≤ tt.latest, where e_now is the invocation event.

The underlying time references used by TrueTime are GPS and atomic clocks. TrueTime uses two forms of time reference because they have different failure modes. GPS reference-source vulnerabilities include antenna and receiver failures, local radio interference, correlated failures (e.g., design faults such as incorrect leap-second handling and spoofing), and GPS system outages. Atomic clocks can fail in ways uncorrelated to GPS and each other, and over long periods of time can drift significantly due to frequency error.

TrueTime is implemented by a set of time master machines per datacenter and a timeslave daemon per machine. The majority of masters have GPS receivers with dedicated antennas; these masters are separated physically to reduce the effects of antenna failures, radio interference, and spoofing. The remaining masters (which we refer to as Armageddon masters) are equipped with atomic clocks. An atomic clock is not that expensive: the cost of an Armageddon master is of the same order as that of a GPS master. All masters' time references are regularly compared against each other. Each master also cross-checks the rate at which its reference advances time against its own local clock, and evicts itself if there is substantial divergence. Between synchronizations, Armageddon masters advertise a slowly increasing time uncertainty that is derived from conservatively applied worst-case clock drift. GPS masters advertise uncertainty that is typically close to zero.

Every daemon polls a variety of masters [29] to reduce vulnerability to errors from any one master. Some are GPS masters chosen from nearby datacenters; the rest are GPS masters from farther datacenters, as well as some Armageddon masters. Daemons apply a variant of Marzullo's algorithm [27] to detect and reject liars, and synchronize the local machine clocks to the non-liars. To protect against broken local clocks, machines that exhibit frequency excursions larger than the worst-case bound derived from component specifications and operating environment are evicted.

Between synchronizations, a daemon advertises a slowly increasing time uncertainty. ε is derived from conservatively applied worst-case local clock drift. ε also depends on time-master uncertainty and communication delay to the time masters. In our production environment, ε is typically a sawtooth function of time, varying from about 1 to 7 ms over each poll interval. ε̄ is therefore 4 ms most of the time. The daemon's poll interval is currently 30 seconds, and the current applied drift rate is set at 200 microseconds/second, which together account for the sawtooth bounds from 0 to 6 ms. The remaining 1 ms comes from the communication delay to the time masters. Excursions from this sawtooth are possible in the presence of failures. For example, occasional time-master unavailability can cause datacenter-wide increases in ε. Similarly, overloaded machines and network links can result in occasional localized ε spikes.

---

### النسخة العربية

يصف هذا القسم واجهة برمجة تطبيقات TrueTime ويرسم ملامح تنفيذها. نترك معظم التفاصيل لورقة بحثية أخرى: هدفنا هو إظهار قوة امتلاك مثل هذه الواجهة. يسرد الجدول 1 طرق الواجهة. يمثل TrueTime الوقت صراحةً كـ TTinterval، وهو فترة زمنية ذات عدم يقين زمني محدود (على عكس واجهات الوقت القياسية التي لا تعطي العملاء أي فكرة عن عدم اليقين). نقاط نهاية TTinterval من نوع TTstamp. تعيد طريقة TT.now() قيمة TTinterval مضمونة أن تحتوي على الوقت المطلق الذي تم خلاله استدعاء TT.now(). حقبة الوقت مماثلة لوقت UNIX مع توزيع الثانية الكبيسة. عرّف حد الخطأ اللحظي بـ ε، وهو نصف عرض الفترة، ومتوسط حد الخطأ بـ ε̄.

**الجدول 1: واجهة برمجة تطبيقات TrueTime**

| الطريقة | القيمة المُرجعة |
|---------|-----------------|
| TT.now() | TTinterval: [earliest, latest] |
| TT.after(t) | true إذا كان t قد مر بالتأكيد |
| TT.before(t) | true إذا كان t لم يصل بعد بالتأكيد |

المعامل t من نوع TTstamp.

طريقتا TT.after() و TT.before() هما غلافات ملائمة حول TT.now(). دع t_abs(e) يدل على الوقت المطلق لحدث e. بمصطلحات أكثر رسمية، يضمن TrueTime أنه لاستدعاء tt = TT.now()، فإن tt.earliest ≤ t_abs(e_now) ≤ tt.latest، حيث e_now هو حدث الاستدعاء.

مراجع الوقت الأساسية المستخدمة بواسطة TrueTime هي GPS والساعات الذرية. يستخدم TrueTime شكلين من مراجع الوقت لأن لديهما أنماط فشل مختلفة. تشمل نقاط ضعف مصدر مرجع GPS فشل الهوائي والمستقبل، والتداخل اللاسلكي المحلي، والأعطال المترابطة (مثل عيوب التصميم كمعالجة الثانية الكبيسة غير الصحيحة والانتحال)، وانقطاعات نظام GPS. يمكن أن تفشل الساعات الذرية بطرق غير مترابطة مع GPS ومع بعضها البعض، وعلى مدى فترات زمنية طويلة يمكن أن تنحرف بشكل كبير بسبب خطأ التردد.

يتم تنفيذ TrueTime بواسطة مجموعة من آلات سيد الوقت (time master) لكل مركز بيانات وعفريت عبد الوقت (timeslave daemon) لكل آلة. تحتوي غالبية الأسياد على مستقبلات GPS بهوائيات مخصصة؛ يتم فصل هذه الأسياد فيزيائياً لتقليل تأثيرات فشل الهوائيات والتداخل اللاسلكي والانتحال. الأسياد المتبقية (التي نشير إليها باسم أسياد أرماجيدون Armageddon masters) مجهزة بالساعات الذرية. الساعة الذرية ليست باهظة الثمن: تكلفة سيد أرماجيدون من نفس رتبة تكلفة سيد GPS. تتم مقارنة مراجع الوقت لجميع الأسياد بانتظام مع بعضها البعض. يقوم كل سيد أيضاً بالتحقق المتقاطع من المعدل الذي يتقدم به مرجعه الوقت مقابل ساعته المحلية الخاصة، ويطرد نفسه إذا كان هناك اختلاف كبير. بين عمليات المزامنة، تعلن أسياد أرماجيدون عن عدم يقين زمني يتزايد ببطء مشتق من انحراف الساعة في أسوأ الحالات المطبق بشكل متحفظ. تعلن أسياد GPS عن عدم يقين يكون عادةً قريباً من الصفر.

يستعلم كل عفريت مجموعة متنوعة من الأسياد [29] لتقليل التعرض للأخطاء من أي سيد واحد. بعضها أسياد GPS مختارة من مراكز بيانات قريبة؛ والباقي أسياد GPS من مراكز بيانات أبعد، بالإضافة إلى بعض أسياد أرماجيدون. تطبق العفاريت نوعاً مختلفاً من خوارزمية مارزولو [27] للكشف عن الكاذبين ورفضهم، وتزامن ساعات الآلات المحلية مع غير الكاذبين. للحماية من الساعات المحلية المعطلة، يتم طرد الآلات التي تظهر انحرافات تردد أكبر من حد أسوأ حالة المشتق من مواصفات المكونات وبيئة التشغيل.

بين عمليات المزامنة، يعلن عفريت عن عدم يقين زمني يتزايد ببطء. يُشتق ε من انحراف الساعة المحلية في أسوأ الحالات المطبق بشكل متحفظ. يعتمد ε أيضاً على عدم يقين سيد الوقت وتأخير الاتصال بأسياد الوقت. في بيئة الإنتاج لدينا، عادةً ما يكون ε دالة منشارية للوقت، تتراوح من حوالي 1 إلى 7 ميللي ثانية على مدى كل فترة استقصاء. لذلك فإن ε̄ يكون 4 ميللي ثانية في معظم الوقت. فترة استقصاء العفريت حالياً 30 ثانية، ومعدل الانحراف المطبق الحالي مضبوط على 200 ميكروثانية/ثانية، وهو ما يفسر معاً حدود المنشار من 0 إلى 6 ميللي ثانية. تأتي الـ 1 ميللي ثانية المتبقية من تأخير الاتصال بأسياد الوقت. الانحرافات عن هذا المنشار ممكنة في وجود الأعطال. على سبيل المثال، يمكن أن يتسبب عدم توفر سيد الوقت العرضي في زيادات على مستوى مركز البيانات في ε. وبالمثل، يمكن أن تؤدي الآلات المثقلة بالحمل وروابط الشبكة إلى ارتفاعات محلية عرضية في ε.

---

### Translation Notes

- **Figures referenced:** None
- **Tables referenced:** Table 1 (TrueTime API), Table 2 mentioned at end
- **Key terms introduced:**
  - TrueTime API (واجهة برمجة تطبيقات TrueTime)
  - TTinterval (فترة TT)
  - TTstamp (طابع TT)
  - Bounded uncertainty (عدم اليقين المحدود)
  - Time master (سيد الوقت)
  - Timeslave daemon (عفريت عبد الوقت)
  - Armageddon masters (أسياد أرماجيدون)
  - Leap-second smearing (توزيع الثانية الكبيسة)
  - Clock drift (انحراف الساعة)
  - Sawtooth function (دالة منشارية)
  - Marzullo's algorithm (خوارزمية مارزولو)
  - Frequency excursions (انحرافات التردد)
- **Equations:**
  - tt.earliest ≤ t_abs(e_now) ≤ tt.latest
  - ε (epsilon) for instantaneous error bound
  - ε̄ (epsilon bar) for average error bound
- **Citations:** [27], [29]
- **Special handling:**
  - Method names kept in English: TT.now(), TT.after(), TT.before()
  - Technical terms: GPS, UNIX kept in English
  - "Armageddon masters" kept in English as it's a specific system name
  - Mathematical symbols preserved: ε, ε̄, ≤

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.94
- Readability: 0.86
- Glossary consistency: 0.95
- **Overall section score:** 0.89
