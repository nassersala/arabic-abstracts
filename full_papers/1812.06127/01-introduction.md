# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.89
**Glossary Terms Used:** federated learning, distributed learning, optimization, heterogeneous, systems heterogeneity, statistical heterogeneity, privacy, differential privacy, convergence, stochastic gradient descent, framework

---

### English Version

Federated learning represents an emerging computational paradigm for distributing machine learning model training across networks of remote devices. While distributed optimization has been extensively studied in machine learning contexts, federated environments present two distinguishing obstacles: substantial variability in device system characteristics (systems heterogeneity) and non-uniform data distributions across the network (statistical heterogeneity).

The authors identify privacy as a third key consideration in federated settings, though this work primarily addresses the first two challenges. Standard privacy-preserving approaches including differential privacy and secure multiparty communication can be naturally integrated with the proposed methods, given that the framework involves only lightweight algorithmic modifications to existing approaches.

#### Local Updating Approaches

Addressing heterogeneity and communication constraints, optimization methods permitting local updating with limited device participation have gained prominence. FedAvg (McMahan et al., 2017) has become the predominant optimization method in federated contexts. This iterative approach involves: (1) devices performing E epochs of stochastic gradient descent locally on K selected devices, then (2) communicating model updates to a central server for averaging.

#### Limitations of Existing Methods

Despite empirical success, FedAvg inadequately addresses heterogeneity challenges. From a systems perspective, it prevents devices from performing variable local work based on their constraints—instead, devices failing to complete E epochs within specified timeframes are simply disconnected. Statistically, FedAvg demonstrates empirical divergence with non-identically distributed data, yet lacks convergence guarantees to characterize its behavior in realistic heterogeneous scenarios.

#### Proposed Solution: FedProx

The authors propose FedProx, addressing both heterogeneity forms theoretically and empirically. A critical insight involves recognizing interactions between systems and statistical heterogeneity: dropping stragglers or incorporating incomplete information from constrained devices implicitly amplifies statistical heterogeneity, potentially damaging convergence. The solution incorporates a proximal term in the objective, enabling the server to systematically account for heterogeneity-related partial information.

These modifications enable convergence guarantees for heterogeneous, non-identically distributed data while respecting device-level systems constraints. Empirically, FedProx demonstrates substantially more stable convergence than FedAvg—improving absolute test accuracy by an average of 22% in highly heterogeneous environments.

The paper proceeds through background discussion, methodological presentation, theoretical convergence analysis, and comprehensive empirical evaluation across synthetic and real-world federated datasets.

---

### النسخة العربية

يمثل التعلم الاتحادي نموذجًا حسابيًا ناشئًا لتوزيع تدريب نماذج التعلم الآلي عبر شبكات من الأجهزة البعيدة. بينما تمت دراسة التحسين الموزع على نطاق واسع في سياقات التعلم الآلي، تقدم البيئات الاتحادية عقبتين مميزتين: التباين الكبير في خصائص أنظمة الأجهزة (عدم التجانس في الأنظمة) والتوزيعات غير المنتظمة للبيانات عبر الشبكة (عدم التجانس الإحصائي).

يحدد المؤلفون الخصوصية كاعتبار رئيسي ثالث في الإعدادات الاتحادية، على الرغم من أن هذا العمل يعالج بشكل أساسي التحديين الأولين. يمكن دمج الأساليب القياسية للحفاظ على الخصوصية بما في ذلك الخصوصية التفاضلية والاتصال الآمن متعدد الأطراف بشكل طبيعي مع الطرق المقترحة، نظرًا لأن إطار العمل يتضمن فقط تعديلات خوارزمية خفيفة الوزن على الأساليب الموجودة.

#### أساليب التحديث المحلي

لمعالجة عدم التجانس وقيود الاتصال، اكتسبت طرق التحسين التي تسمح بالتحديث المحلي مع مشاركة محدودة للأجهزة أهمية بارزة. أصبح FedAvg (McMahan et al., 2017) طريقة التحسين السائدة في السياقات الاتحادية. يتضمن هذا النهج التكراري: (1) قيام الأجهزة بتنفيذ E من حقب الانحدار التدرجي العشوائي محليًا على K من الأجهزة المختارة، ثم (2) إرسال تحديثات النموذج إلى خادم مركزي للحساب المتوسط.

#### قيود الأساليب الموجودة

على الرغم من النجاح التجريبي، لا يعالج FedAvg بشكل كافٍ تحديات عدم التجانس. من منظور الأنظمة، يمنع الأجهزة من أداء عمل محلي متغير بناءً على قيودها - بدلاً من ذلك، يتم ببساطة فصل الأجهزة التي تفشل في إكمال E من الحقب ضمن أطر زمنية محددة. من الناحية الإحصائية، يُظهر FedAvg تباعدًا تجريبيًا مع البيانات الموزعة بشكل غير متطابق، ومع ذلك يفتقر إلى ضمانات التقارب لتوصيف سلوكه في السيناريوهات غير المتجانسة الواقعية.

#### الحل المقترح: FedProx

يقترح المؤلفون FedProx، الذي يعالج كلا شكلي عدم التجانس نظريًا وتجريبيًا. تتضمن الرؤية الحاسمة التعرف على التفاعلات بين عدم التجانس في الأنظمة وعدم التجانس الإحصائي: إسقاط الأجهزة المتأخرة أو دمج المعلومات غير الكاملة من الأجهزة المقيدة يضخم ضمنيًا عدم التجانس الإحصائي، مما قد يضر بالتقارب. يتضمن الحل حدًا قريبيًا (proximal term) في الهدف، مما يمكّن الخادم من المحاسبة بشكل منهجي عن المعلومات الجزئية المتعلقة بعدم التجانس.

تمكّن هذه التعديلات من ضمانات التقارب للبيانات غير المتجانسة والموزعة بشكل غير متطابق مع احترام قيود الأنظمة على مستوى الجهاز. تجريبيًا، يُظهر FedProx تقاربًا أكثر استقرارًا بشكل كبير من FedAvg - مما يحسن دقة الاختبار المطلقة بمعدل 22% في المتوسط في البيئات شديدة عدم التجانس.

تتقدم الورقة من خلال مناقشة الخلفية، وعرض المنهجية، وتحليل التقارب النظري، والتقييم التجريبي الشامل عبر مجموعات البيانات الاتحادية الاصطناعية والواقعية.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - systems heterogeneity (عدم التجانس في الأنظمة)
  - statistical heterogeneity (عدم التجانس الإحصائي)
  - proximal term (حد قريبي)
  - stragglers (الأجهزة المتأخرة)
  - local updating (التحديث المحلي)
- **Equations:** None in this section
- **Citations:** McMahan et al., 2017 (FedAvg paper)
- **Special handling:**
  - FedAvg and FedProx kept as proper names
  - Technical terms like "epochs" kept in transliterated form with Arabic explanation

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.89
- Readability: 0.88
- Glossary consistency: 0.89
- **Overall section score:** 0.89
