# Section 3: Device
## القسم 3: الجهاز

**Section:** device
**Translation Quality:** 0.86
**Glossary Terms Used:** federated learning, Android, device, model training, evaluation, API, FL runtime, example store, database, encryption, server, FL plan, job scheduler, metrics, multi-tenancy, attestation, data poisoning

---

### English Version

## Overview

This section describes the software architecture for devices participating in federated learning, focusing on the Android implementation. The architectural choices are platform-agnostic and applicable broadly.

## Core Responsibilities

The device's primary responsibility involves maintaining a repository of locally collected data for model training and evaluation. Applications must implement an API to make their data available to the FL runtime through an example store. A typical example store might be an SQLite database recording user interactions, such as suggested actions and their acceptance rates.

Applications should limit storage footprint and automatically remove old data after designated expiration periods. The paper recommends following best practices for on-device data security, including encryption at rest using platform-recommended methods.

## Control Flow

When the FL server provides a task, the FL runtime accesses the appropriate example store to compute model updates or evaluate model quality. The control flow consists of four steps:

**Programmatic Configuration**: Applications configure the FL runtime by providing an FL population name and registering example stores. This schedules a periodic job using Android's JobScheduler. Crucially, the runtime requests job invocation only when "the phone is idle, charging, and connected to an unmetered network such as WiFi." The runtime aborts and frees resources if these conditions change.

**Job Invocation**: Upon scheduler invocation in a separate process, the runtime contacts the FL server to announce readiness for the population. The server either returns an FL plan or suggests a reconnection time.

**Task Execution**: Selected devices receive the FL plan, query the example store for requested data, and compute model updates and metrics.

**Reporting**: The runtime reports updates and metrics to the server and cleans up temporary resources.

FL plans can encode evaluation tasks computing quality metrics from held-out data, analogous to validation in data center training.

## Architecture Flexibility

The design enables the FL runtime to run within the application or in a centralized service hosted in another app. Communication between application, runtime, and example store uses Android's AIDL IPC mechanism, functioning both within single apps and across apps.

## Multi-Tenancy

The implementation provides multi-tenant architecture, supporting training of multiple FL populations in the same app or service. This allows coordination between multiple training activities, preventing device overload from simultaneous training sessions.

## Attestation

Devices participate anonymously, excluding user identity authentication. To protect against attacks from non-genuine devices, the system uses "Android's remote attestation mechanism," which ensures only genuine devices and applications participate and provides protection against data poisoning via compromised devices. The paper notes that other forms of model manipulation—such as content farms using uncompromised phones—remain unaddressed in their scope.

---

### النسخة العربية

## نظرة عامة

يصف هذا القسم معمارية البرمجيات للأجهزة المشاركة في التعلم الاتحادي، مع التركيز على تطبيق Android. الخيارات المعمارية مستقلة عن المنصة وقابلة للتطبيق على نطاق واسع.

## المسؤوليات الأساسية

تتضمن المسؤولية الأساسية للجهاز الحفاظ على مستودع للبيانات المجمعة محلياً لتدريب النموذج وتقييمه. يجب على التطبيقات تنفيذ واجهة برمجة تطبيقات (API) لإتاحة بياناتها لبيئة تشغيل التعلم الاتحادي (FL runtime) من خلال مخزن أمثلة (example store). قد يكون مخزن الأمثلة النموذجي قاعدة بيانات SQLite تسجل تفاعلات المستخدم، مثل الإجراءات المقترحة ومعدلات قبولها.

يجب على التطبيقات تقييد البصمة التخزينية وإزالة البيانات القديمة تلقائياً بعد فترات انتهاء صلاحية محددة. يوصي البحث باتباع أفضل الممارسات لأمان البيانات على الجهاز، بما في ذلك التشفير أثناء التخزين باستخدام الطرق الموصى بها من المنصة.

## تدفق التحكم

عندما يوفر خادم التعلم الاتحادي مهمة، تصل بيئة تشغيل التعلم الاتحادي إلى مخزن الأمثلة المناسب لحساب تحديثات النموذج أو تقييم جودة النموذج. يتكون تدفق التحكم من أربع خطوات:

**التكوين البرمجي (Programmatic Configuration)**: تقوم التطبيقات بتكوين بيئة تشغيل التعلم الاتحادي من خلال توفير اسم مجموعة التعلم الاتحادي وتسجيل مخازن الأمثلة. يؤدي هذا إلى جدولة مهمة دورية باستخدام JobScheduler في Android. والأهم من ذلك، تطلب بيئة التشغيل استدعاء المهمة فقط عندما "يكون الهاتف في وضع الخمول، قيد الشحن، ومتصل بشبكة غير محدودة مثل WiFi". تقوم بيئة التشغيل بالإيقاف وتحرير الموارد إذا تغيرت هذه الشروط.

**استدعاء المهمة (Job Invocation)**: عند استدعاء المجدول في عملية منفصلة، تتصل بيئة التشغيل بخادم التعلم الاتحادي للإعلان عن الاستعداد للمجموعة. يعيد الخادم إما خطة التعلم الاتحادي أو يقترح وقت إعادة الاتصال.

**تنفيذ المهمة (Task Execution)**: تتلقى الأجهزة المختارة خطة التعلم الاتحادي، وتستعلم عن مخزن الأمثلة للحصول على البيانات المطلوبة، وتحسب تحديثات النموذج والمقاييس.

**الإبلاغ (Reporting)**: تُبلغ بيئة التشغيل عن التحديثات والمقاييس إلى الخادم وتنظف الموارد المؤقتة.

يمكن لخطط التعلم الاتحادي تشفير مهام التقييم التي تحسب مقاييس الجودة من البيانات المستبعدة، بشكل مماثل للتحقق في تدريب مراكز البيانات.

## مرونة المعمارية

يُمكّن التصميم بيئة تشغيل التعلم الاتحادي من العمل داخل التطبيق أو في خدمة مركزية مستضافة في تطبيق آخر. يستخدم الاتصال بين التطبيق وبيئة التشغيل ومخزن الأمثلة آلية AIDL IPC في Android، والتي تعمل داخل التطبيقات الفردية وعبر التطبيقات.

## تعدد المستأجرين

يوفر التنفيذ معمارية متعددة المستأجرين (multi-tenant)، تدعم تدريب مجموعات متعددة من التعلم الاتحادي في نفس التطبيق أو الخدمة. يتيح ذلك التنسيق بين أنشطة التدريب المتعددة، مما يمنع التحميل الزائد على الجهاز من جلسات التدريب المتزامنة.

## المصادقة

تشارك الأجهزة بشكل مجهول، باستثناء مصادقة هوية المستخدم. للحماية من الهجمات من الأجهزة غير الحقيقية، يستخدم النظام "آلية المصادقة عن بُعد في Android (remote attestation mechanism)"، والتي تضمن مشاركة الأجهزة والتطبيقات الحقيقية فقط وتوفر الحماية ضد تسميم البيانات (data poisoning) عبر الأجهزة المخترقة. يشير البحث إلى أن أشكال أخرى من التلاعب بالنموذج - مثل مزارع المحتوى التي تستخدم هواتف غير مخترقة - تظل غير معالجة في نطاقهم.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** FL runtime, example store, JobScheduler, AIDL IPC, multi-tenant architecture, remote attestation, data poisoning
- **Equations:** 0
- **Citations:** 0
- **Special handling:** Technical Android-specific terms like "JobScheduler", "AIDL IPC", and "remote attestation" are kept in English with Arabic explanations. The four control flow steps are labeled in both English and Arabic.

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86
