# Section 7: Tools and Workflow
## القسم 7: الأدوات وسير العمل

**Section:** tools-workflow
**Translation Quality:** 0.86
**Glossary Terms Used:** federated learning, model, training, TensorFlow, FL plan, deployment, simulation, hyperparameter, versioning, testing, metrics, device, server, aggregation, Python

---

### English Version

## Overview

The workflow for federated learning presents distinct challenges compared to centralized data training. Model engineers cannot directly inspect individual training examples and must instead work with proxy datasets during development. Additionally, models require compilation into FL plans for server deployment rather than interactive execution.

## 7.1 Modeling and Simulation

Engineers define FL tasks using Python interfaces and TensorFlow functions that map input tensors to output metrics. During development, "model engineers may use sample test data or other proxy data as inputs. When deployed, the inputs will be provided from the on-device example store via the FL runtime."

The modeling infrastructure validates tasks against engineer-provided test data. Proxy data—drawn from different distributions than actual on-device data—enables initial hyperparameter exploration. The system supports "deployment of FL tasks to a simulated FL server and a fleet of cloud jobs emulating devices."

## 7.2 Plan Generation

FL plans are automatically generated from model and configuration specifications. Rather than executing Python directly, "the FL plan's purpose is to describe the desired orchestration independent of Python."

Plans contain two components: a device portion with the TensorFlow graph, data selection criteria, and computation labels, and a server portion encoding aggregation logic. Libraries automatically partition computations between device and server execution.

## 7.3 Versioning, Testing, and Deployment

Deployment requires several conditions: auditable, peer-reviewed code; passing test predicates in simulation; resource consumption within safe ranges; and compatibility across TensorFlow runtime versions.

The infrastructure addresses version challenges through "generating versioned FL plans for each task. Each versioned FL plan is derived from the default (unversioned) FL plan by transforming its computation graph to achieve compatibility with a deployed TensorFlow version."

## 7.4 Metrics

Upon deployment acceptance, "As soon as an FL round closes, that round's aggregated model parameters and metrics are written to the server storage location chosen by the model engineer." Metrics include metadata and statistical summaries, accessible through standard Python data science packages.

---

### النسخة العربية

## نظرة عامة

يقدم سير العمل للتعلم الاتحادي تحديات مميزة مقارنة بتدريب البيانات المركزية. لا يمكن لمهندسي النماذج فحص أمثلة التدريب الفردية بشكل مباشر ويجب عليهم بدلاً من ذلك العمل مع مجموعات بيانات بديلة (proxy datasets) أثناء التطوير. بالإضافة إلى ذلك، تتطلب النماذج الترجمة إلى خطط تعلم اتحادي لنشر الخادم بدلاً من التنفيذ التفاعلي.

## 7.1 النمذجة والمحاكاة

يُعرّف المهندسون مهام التعلم الاتحادي باستخدام واجهات Python ودوال TensorFlow التي تربط الموترات المدخلة بمقاييس المخرجات. أثناء التطوير، "قد يستخدم مهندسو النماذج بيانات اختبار عينة أو بيانات بديلة أخرى كمدخلات. عند النشر، سيتم توفير المدخلات من مخزن الأمثلة على الجهاز عبر بيئة تشغيل التعلم الاتحادي".

تتحقق البنية التحتية للنمذجة من المهام مقابل بيانات الاختبار المقدمة من المهندس. تُمكّن البيانات البديلة - المستمدة من توزيعات مختلفة عن البيانات الفعلية على الجهاز - من الاستكشاف الأولي للمعاملات الفائقة (hyperparameter). يدعم النظام "نشر مهام التعلم الاتحادي على خادم تعلم اتحادي محاكى ومجموعة من مهام السحابة التي تحاكي الأجهزة".

## 7.2 توليد الخطط

يتم توليد خطط التعلم الاتحادي تلقائياً من مواصفات النموذج والتكوين. بدلاً من تنفيذ Python مباشرة، "الغرض من خطة التعلم الاتحادي هو وصف التنسيق المطلوب بشكل مستقل عن Python".

تحتوي الخطط على مكونين: جزء الجهاز مع الرسم البياني لـ TensorFlow ومعايير اختيار البيانات وتسميات الحساب، وجزء الخادم الذي يشفر منطق التجميع. تقوم المكتبات بتقسيم العمليات الحسابية تلقائياً بين تنفيذ الجهاز والخادم.

## 7.3 التحكم في الإصدارات والاختبار والنشر

يتطلب النشر عدة شروط: كود قابل للمراجعة ومُراجَع من الأقران؛ اجتياز محمولات الاختبار في المحاكاة؛ استهلاك الموارد ضمن نطاقات آمنة؛ والتوافق عبر إصدارات بيئة تشغيل TensorFlow.

تعالج البنية التحتية تحديات الإصدار من خلال "توليد خطط تعلم اتحادي ذات إصدارات لكل مهمة. تُشتق كل خطة تعلم اتحادي ذات إصدار من خطة التعلم الاتحادي الافتراضية (بدون إصدار) من خلال تحويل الرسم البياني الحسابي الخاص بها لتحقيق التوافق مع إصدار TensorFlow المنشور".

## 7.4 المقاييس

عند قبول النشر، "بمجرد إغلاق جولة التعلم الاتحادي، تُكتب معاملات النموذج المُجمَّعة والمقاييس لتلك الجولة في موقع تخزين الخادم الذي اختاره مهندس النموذج". تتضمن المقاييس البيانات الوصفية والملخصات الإحصائية، ويمكن الوصول إليها من خلال حزم Python القياسية لعلم البيانات.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** proxy datasets, FL tasks, modeling infrastructure, hyperparameter exploration, plan generation, versioned FL plans, computation graph, peer-reviewed code, test predicates, metadata
- **Equations:** 0
- **Citations:** 0
- **Special handling:** Technical terms like "proxy data", "hyperparameter", "versioned FL plans", and "computation graph" are translated with English equivalents in parentheses where appropriate for clarity.

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86
