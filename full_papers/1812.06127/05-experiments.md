# Section 5: Experiments
## القسم 5: التجارب

**Section:** experiments
**Translation Quality:** 0.87
**Glossary Terms Used:** dataset, federated learning, heterogeneous, convergence, hyperparameter, training, MNIST, LSTM, SGD, proximal term, statistical heterogeneity, systems heterogeneity

---

### English Version

## 5.1 Experimental Details

The researchers evaluated FedProx using diverse tasks, models, and real-world federated datasets. They created synthetic data following a setup similar to prior work, imposing heterogeneity among devices to characterize statistical heterogeneity precisely. For synthetic datasets, device k generates samples according to a softmax model where parameters vary by device through normal distributions controlled by parameters α and β.

Four real datasets were employed:
- **MNIST**: 1,000 devices with 69,035 samples distributed so each device has only two digits
- **FEMNIST**: 200 devices with 18,345 samples across 62 classes
- **Sent140**: 772 devices with sentiment analysis using LSTM classifiers
- **Shakespeare**: 143 devices performing next-character prediction

The implementation used TensorFlow with SGD as the local solver for both methods. Rather than the probabilistic device sampling in the algorithms, they employed uniform device sampling and then averaged the updates with weights proportional to the number of local data points, matching McMahan et al.'s original proposal.

For hyperparameter selection, researchers tuned learning rates on FedAvg without systems heterogeneity, then applied identical settings across all experiments on each dataset. They fixed K=10 selected devices per round.

## 5.2 Systems Heterogeneity: Tolerating Partial Work

This section simulates federated settings with varying system heterogeneity by assigning variable local work amounts to different devices based on a global clock cycle.

The experimental design forced devices to perform fewer than E epochs chosen uniformly at random between [1, E] in 0%, 50%, and 90% of cases respectively. FedAvg dropped these stragglers; FedProx incorporated partial updates.

Results demonstrated that systems heterogeneity has negative effects on convergence, and larger heterogeneity results in worse convergence for FedAvg. However, allowing for variable amounts of work (FedProx, μ=0) is beneficial and leads to more stable and faster convergence. Setting μ>0 further improved performance across all datasets tested.

## 5.3 Statistical Heterogeneity: Proximal Term

### 5.3.1 Effects of Statistical Heterogeneity

Using four synthetic datasets without systems heterogeneity, researchers showed convergence degrades as data become more heterogeneous. Notably, while setting μ>0 may slow convergence for IID data, it proved particularly useful in heterogeneous settings.

### 5.3.2 Effects of μ>0

The proximal parameter μ provides an alternative to manually tuning local epochs E. The researchers demonstrated that appropriate μ can increase the stability for unstable methods and can force divergent methods to converge across all tested datasets.

For selecting μ, they tuned from {0.001, 0.01, 0.1, 1}. They also proposed a simple heuristic: increase μ by 0.1 whenever the loss increases and decreases it by 0.1 whenever the loss decreases for 5 consecutive rounds. This adaptive approach showed competitive empirical performance.

### 5.3.3 Dissimilarity Measurement and Divergence

The bounded dissimilarity metric captured real-world statistical heterogeneity. Tracking variance of gradients per device revealed that smaller dissimilarity indicates better convergence, which can be enforced by setting μ appropriately. This validation confirms the theoretical assumptions matched practical behavior on both synthetic and real federated datasets.

---

### النسخة العربية

## 5.1 تفاصيل التجارب

قيّم الباحثون FedProx باستخدام مهام ونماذج ومجموعات بيانات اتحادية متنوعة من العالم الحقيقي. أنشأوا بيانات اصطناعية تتبع إعدادًا مشابهًا للعمل السابق، مما يفرض عدم التجانس بين الأجهزة لتوصيف عدم التجانس الإحصائي بدقة. بالنسبة لمجموعات البيانات الاصطناعية، يولد الجهاز k عينات وفقًا لنموذج softmax حيث تختلف المعاملات حسب الجهاز من خلال التوزيعات الطبيعية المتحكم فيها بواسطة المعاملات α و β.

تم استخدام أربع مجموعات بيانات حقيقية:
- **MNIST**: 1,000 جهاز مع 69,035 عينة موزعة بحيث يحتوي كل جهاز على رقمين فقط
- **FEMNIST**: 200 جهاز مع 18,345 عينة عبر 62 فئة
- **Sent140**: 772 جهاز مع تحليل المشاعر باستخدام مصنفات LSTM
- **Shakespeare**: 143 جهاز يؤدي التنبؤ بالحرف التالي

استخدم التنفيذ TensorFlow مع SGD كحلال محلي لكلا الطريقتين. بدلاً من أخذ عينات الأجهزة الاحتمالية في الخوارزميات، استخدموا أخذ عينات الأجهزة الموحدة ثم حساب متوسط التحديثات مع أوزان متناسبة مع عدد نقاط البيانات المحلية، مطابقة الاقتراح الأصلي لـ McMahan et al.

لاختيار المعاملات الفائقة، ضبط الباحثون معدلات التعلم على FedAvg دون عدم التجانس في الأنظمة، ثم طبقوا إعدادات متطابقة عبر جميع التجارب على كل مجموعة بيانات. ثبتوا K=10 أجهزة مختارة لكل جولة.

## 5.2 عدم التجانس في الأنظمة: تحمل العمل الجزئي

يحاكي هذا القسم إعدادات اتحادية مع عدم تجانس متفاوت في الأنظمة من خلال تعيين كميات عمل محلية متغيرة لأجهزة مختلفة بناءً على دورة ساعة عامة.

أجبر التصميم التجريبي الأجهزة على أداء أقل من E من الحقب المختارة بشكل عشوائي موحد بين [1, E] في 0% و 50% و 90% من الحالات على التوالي. أسقط FedAvg هذه الأجهزة المتأخرة؛ دمج FedProx التحديثات الجزئية.

أظهرت النتائج أن عدم التجانس في الأنظمة له تأثيرات سلبية على التقارب، وعدم التجانس الأكبر يؤدي إلى تقارب أسوأ لـ FedAvg. ومع ذلك، فإن السماح بكميات متغيرة من العمل (FedProx، μ=0) مفيد ويؤدي إلى تقارب أكثر استقرارًا وأسرع. أدى تعيين μ>0 إلى تحسين الأداء بشكل أكبر عبر جميع مجموعات البيانات المختبرة.

## 5.3 عدم التجانس الإحصائي: الحد القريبي

### 5.3.1 تأثيرات عدم التجانس الإحصائي

باستخدام أربع مجموعات بيانات اصطناعية دون عدم تجانس في الأنظمة، أظهر الباحثون أن التقارب يتدهور مع زيادة عدم تجانس البيانات. والجدير بالذكر، بينما قد يبطئ تعيين μ>0 التقارب لبيانات IID، فقد أثبت أنه مفيد بشكل خاص في الإعدادات غير المتجانسة.

### 5.3.2 تأثيرات μ>0

يوفر المعامل القريبي μ بديلاً للضبط اليدوي للحقب المحلية E. أظهر الباحثون أن μ المناسب يمكن أن يزيد الاستقرار للطرق غير المستقرة ويمكن أن يجبر الطرق المتباعدة على التقارب عبر جميع مجموعات البيانات المختبرة.

لاختيار μ، قاموا بالضبط من {0.001، 0.01، 0.1، 1}. اقترحوا أيضًا استدلاليًا بسيطًا: زيادة μ بمقدار 0.1 كلما زادت الخسارة وتخفيضها بمقدار 0.1 كلما انخفضت الخسارة لـ 5 جولات متتالية. أظهر هذا النهج التكيفي أداءً تجريبيًا تنافسيًا.

### 5.3.3 قياس التباين والتباعد

التقط مقياس التباين المحدود عدم التجانس الإحصائي في العالم الحقيقي. كشف تتبع تباين التدرجات لكل جهاز أن التباين الأصغر يشير إلى تقارب أفضل، والذي يمكن فرضه من خلال تعيين μ بشكل مناسب. يؤكد هذا التحقق أن الافتراضات النظرية تطابق السلوك العملي على كل من مجموعات البيانات الاتحادية الاصطناعية والحقيقية.

---

### Translation Notes

- **Figures referenced:** Figure 1 (mentioned but not shown in text)
- **Key terms introduced:**
  - synthetic data (بيانات اصطناعية)
  - softmax model (نموذج softmax)
  - uniform device sampling (أخذ عينات الأجهزة الموحدة)
  - global clock cycle (دورة ساعة عامة)
  - stragglers (الأجهزة المتأخرة)
  - partial updates (التحديثات الجزئية)
  - adaptive heuristic (استدلالي تكيفي)
  - consecutive rounds (جولات متتالية)
  - gradient variance (تباين التدرجات)
- **Equations:** None explicitly shown
- **Citations:** McMahan et al.
- **Special handling:**
  - Dataset names (MNIST, FEMNIST, Sent140, Shakespeare) kept in English
  - Framework name TensorFlow kept as-is
  - Parameter values and ranges preserved exactly
  - Percentages (0%, 50%, 90%) maintained as-is

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
