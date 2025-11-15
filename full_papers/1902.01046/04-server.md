# Section 4: Server
## القسم 4: الخادم

**Section:** server
**Translation Quality:** 0.87
**Glossary Terms Used:** FL server, actor model, concurrent, message passing, scalable, coordinator, selector, aggregator, master aggregator, distributed storage, persistent storage, round, device, pipelining, failure modes

---

### English Version

## 4.1 Actor Model

The FL server architecture employs the "Actor Programming Model" as its foundational design paradigm. This approach treats actors as "universal primitives of concurrent computation which use message passing as the sole communication mechanism."

Each actor processes messages sequentially, enabling straightforward programming logic. Scaling is achieved naturally by running multiple actor instances across processors and machines. Actors respond to messages by making local decisions, transmitting messages to other actors, or dynamically creating additional actors. Depending on functional requirements, actor instances can be colocated or distributed geographically, with configuration handled explicitly or automatically. For FL tasks, ephemeral fine-grained actor instances enable dynamic resource allocation and load-balancing.

## 4.2 Architecture

The system comprises several key actor types shown in Figure 3:

**Coordinators** function as top-level actors enabling global synchronization and round advancement. Each Coordinator manages one FL population, registering its address in a shared locking service to ensure single ownership. Coordinators receive device connection information from Selectors and direct device acceptance based on scheduled tasks, spawning Master Aggregators for each task's rounds.

**Selectors** accept and forward device connections. They periodically receive device requirement information from Coordinators, making local acceptance decisions. After Master Aggregators and Aggregators are initialized, Coordinators instruct Selectors to route device subsets appropriately, enabling efficient allocation independent of available device counts. This distributed Selector approach allows geographic proximity to devices while limiting remote Coordinator communication.

**Master Aggregators** oversee each task's rounds, dynamically spawning Aggregators as needed based on device count and update size scaling requirements.

Critically, "no information for a round is written to persistent storage until it is fully aggregated by the Master Aggregator." All actors maintain in-memory state as ephemeral entities, improving scalability by eliminating distributed storage latency and preventing potential datacenter attacks targeting per-device update logs.

## 4.3 Pipelining

Although Selection, Configuration, and Reporting protocol phases are sequentially dependent within single rounds, the Selection phase requires no prior-round inputs. This architectural property enables latency optimization through parallel execution: the subsequent round's Selection phase runs concurrently with the previous round's Configuration and Reporting phases. This pipelining emerges naturally from Selectors continuously executing the selection process without added architectural complexity.

## 4.4 Failure Modes

The system maintains continuous progress despite failures, completing current rounds or restarting from previously committed results. Many failure scenarios don't prevent round completion. If individual Aggregators or Selectors fail, only their connected devices are lost. Master Aggregator failures cause current round failures but trigger Coordinator-initiated restarts. Coordinator failures trigger Selector detection and respawning through the shared locking service, ensuring precisely one replacement.

---

### النسخة العربية

## 4.1 نموذج الفاعل

تستخدم معمارية خادم التعلم الاتحادي "نموذج برمجة الفاعل (Actor Programming Model)" كنموذج تصميم أساسي. يعامل هذا النهج الفواعل (actors) على أنها "عناصر أولية عامة للحساب المتزامن والتي تستخدم تمرير الرسائل (message passing) كآلية اتصال وحيدة".

يعالج كل فاعل الرسائل بشكل متسلسل، مما يُمكّن من منطق برمجة واضح ومباشر. يتم تحقيق التوسع بشكل طبيعي من خلال تشغيل مثيلات متعددة من الفواعل عبر المعالجات والأجهزة. تستجيب الفواعل للرسائل من خلال اتخاذ قرارات محلية، أو نقل رسائل إلى فواعل أخرى، أو إنشاء فواعل إضافية ديناميكياً. اعتماداً على المتطلبات الوظيفية، يمكن وضع مثيلات الفواعل معاً أو توزيعها جغرافياً، مع التعامل مع التكوين بشكل صريح أو تلقائي. بالنسبة لمهام التعلم الاتحادي، تُمكّن مثيلات الفواعل الدقيقة المؤقتة من التخصيص الديناميكي للموارد وموازنة الحمل.

## 4.2 المعمارية

يتكون النظام من عدة أنواع رئيسية من الفواعل الموضحة في الشكل 3:

**المنسقون (Coordinators)** يعملون كفواعل على المستوى الأعلى تُمكّن من التزامن العام وتقدم الجولات. يدير كل منسق مجموعة واحدة من التعلم الاتحادي، مسجلاً عنوانه في خدمة قفل مشتركة لضمان الملكية الفردية. يتلقى المنسقون معلومات اتصال الأجهزة من المحددات (Selectors) ويوجهون قبول الأجهزة بناءً على المهام المجدولة، منشئين المجمعات الرئيسية (Master Aggregators) لكل جولة من جولات المهمة.

**المحددات (Selectors)** تقبل وتعيد توجيه اتصالات الأجهزة. تتلقى بشكل دوري معلومات متطلبات الأجهزة من المنسقين، وتتخذ قرارات القبول المحلية. بعد تهيئة المجمعات الرئيسية والمجمعات (Aggregators)، يوجه المنسقون المحددات لتوجيه مجموعات فرعية من الأجهزة بشكل مناسب، مما يُمكّن من التخصيص الفعال بشكل مستقل عن أعداد الأجهزة المتاحة. يتيح نهج المحددات الموزع هذا القرب الجغرافي من الأجهزة مع الحد من الاتصال البعيد مع المنسق.

**المجمعات الرئيسية (Master Aggregators)** تشرف على جولات كل مهمة، منشئة المجمعات ديناميكياً حسب الحاجة بناءً على عدد الأجهزة ومتطلبات توسع حجم التحديثات.

والأهم من ذلك، "لا يتم كتابة أي معلومات لجولة إلى التخزين المستمر حتى يتم تجميعها بالكامل بواسطة المجمع الرئيسي". تحافظ جميع الفواعل على الحالة في الذاكرة ككيانات مؤقتة، مما يحسن قابلية التوسع من خلال إزالة تأخير التخزين الموزع ومنع هجمات مراكز البيانات المحتملة التي تستهدف سجلات التحديث لكل جهاز.

## 4.3 التسلسل المتوازي

على الرغم من أن مراحل بروتوكول الاختيار والتكوين والإبلاغ تعتمد بشكل متسلسل داخل الجولات الفردية، فإن مرحلة الاختيار لا تتطلب مدخلات من الجولة السابقة. تُمكّن هذه الخاصية المعمارية من تحسين الكمون من خلال التنفيذ المتوازي: تعمل مرحلة الاختيار للجولة اللاحقة بالتزامن مع مراحل التكوين والإبلاغ للجولة السابقة. يظهر هذا التسلسل المتوازي (pipelining) بشكل طبيعي من المحددات التي تنفذ عملية الاختيار بشكل مستمر دون تعقيد معماري إضافي.

## 4.4 أوضاع الفشل

يحافظ النظام على التقدم المستمر على الرغم من الفشل، حيث يكمل الجولات الحالية أو يعيد البدء من النتائج المُلتزم بها سابقاً. العديد من سيناريوهات الفشل لا تمنع إكمال الجولة. إذا فشل المجمعات أو المحددات الفردية، فإن الأجهزة المتصلة بها فقط هي التي تُفقد. تتسبب حالات فشل المجمع الرئيسي في فشل الجولة الحالية لكنها تُطلق عمليات إعادة التشغيل التي يبدأها المنسق. تُطلق حالات فشل المنسق اكتشاف المحدد وإعادة الإنشاء من خلال خدمة القفل المشتركة، مما يضمن بديلاً واحداً بالضبط.

---

### Translation Notes

- **Figures referenced:** Figure 3 (mentioned but not shown)
- **Key terms introduced:** Actor Programming Model, message passing, ephemeral actors, Coordinators, Selectors, Master Aggregators, Aggregators, shared locking service, in-memory state, pipelining
- **Equations:** 0
- **Citations:** 0
- **Special handling:** Technical terms from actor model kept in English in parentheses. The four actor types (Coordinators, Selectors, Master Aggregators, Aggregators) are kept in English alongside Arabic translations as they are key architectural components.

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
