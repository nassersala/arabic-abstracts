# Section 3: Modular Resource Management
## القسم 3: الإدارة النمطية للموارد

**Section:** modular-resource-management
**Translation Quality:** 0.87
**Glossary Terms Used:** ticket transfer, ticket inflation, ticket currency, compensation ticket, modular resource management, resource rights, RPC, priority inversion, priority inheritance, trust boundary, exchange rate, quantum

---

### English Version

The explicit representation of resource rights as lottery tickets provides a convenient substrate for modular resource management. Tickets can be used to insulate the resource management policies of independent modules, because each ticket probabilistically guarantees its owner the right to a worst-case resource consumption rate. Since lottery tickets abstractly encapsulate resource rights, they can also be treated as first-class objects that may be transferred in messages.

This section presents basic techniques for implementing resource management policies with lottery tickets. Detailed examples are presented in Section 5.

## 3.1 Ticket Transfers

*Ticket transfers* are explicit transfers of tickets from one client to another. Ticket transfers can be used in any situation where a client blocks due to some dependency. For example, when a client needs to block pending a reply from an RPC, it can temporarily transfer its tickets to the server on which it is waiting. This idea also conveniently solves the conventional priority inversion problem in a manner similar to priority inheritance [Sha90]. Clients also have the ability to divide ticket transfers across multiple servers on which they may be waiting.

## 3.2 Ticket Inflation

*Ticket inflation* is an alternative to explicit ticket transfers in which a client can escalate its resource rights by creating more lottery tickets. In general, such inflation should be disallowed, since it violates desirable modularity and load insulation properties. For example, a single client could easily monopolize a resource by creating a large number of lottery tickets. However, ticket inflation can be very useful among mutually trusting clients; inflation and deflation can be used to adjust resource allocations without explicit communication.

## 3.3 Ticket Currencies

In general, resource management abstraction barriers are desirable across logical trust boundaries. Lottery scheduling can easily be extended to express resource rights in units that are local to each group of mutually trusting clients. A unique *currency* is used to denominate tickets within each trust boundary. Each currency is backed, or funded, by tickets that are denominated in more primitive currencies. Currency relationships may form an arbitrary acyclic graph, such as a hierarchy of currencies. The effects of inflation can be locally contained by maintaining an exchange rate between each local currency and a base currency that is conserved. The currency abstraction is useful for flexibly naming, sharing, and protecting resource rights. For example, an access control list associated with a currency could specify which principals have permission to inflate it by creating new tickets.

## 3.4 Compensation Tickets

A client which consumes only a fraction $f$ of its allocated resource quantum can be granted a *compensation ticket* that inflates its value by $1/f$ until the client starts its next quantum. This ensures that each client's resource consumption, equal to $f$ times its per-lottery win probability $p$, is adjusted by $1/f$ to match its allocated share $p$. Without compensation tickets, a client that does not consume its entire allocated quantum would receive less than its entitled share of the processor.

---

### النسخة العربية

يوفر التمثيل الصريح لحقوق الموارد كتذاكر يانصيب ركيزة ملائمة للإدارة النمطية للموارد. يمكن استخدام التذاكر لعزل سياسات إدارة الموارد للوحدات المستقلة، لأن كل تذكرة تضمن احتمالياً لمالكها الحق في معدل استهلاك موارد في أسوأ الحالات. نظراً لأن تذاكر اليانصيب تغلف بشكل مجرد حقوق الموارد، يمكن أيضاً معاملتها ككائنات من الدرجة الأولى قد تُنقل في الرسائل.

يقدم هذا القسم تقنيات أساسية لتطبيق سياسات إدارة الموارد باستخدام تذاكر اليانصيب. تُقدم أمثلة تفصيلية في القسم 5.

## 3.1 نقل التذاكر

*نقل التذاكر* هو نقل صريح للتذاكر من عميل إلى آخر. يمكن استخدام نقل التذاكر في أي موقف يُحظر فيه العميل بسبب تبعية ما. على سبيل المثال، عندما يحتاج عميل إلى الحظر في انتظار رد من استدعاء إجرائي بعيد (RPC)، يمكنه نقل تذاكره مؤقتاً إلى الخادم الذي ينتظره. تحل هذه الفكرة أيضاً بشكل ملائم مشكلة انعكاس الأولوية التقليدية بطريقة مماثلة لوراثة الأولوية [Sha90]. لدى العملاء أيضاً القدرة على تقسيم نقل التذاكر عبر خوادم متعددة قد يكونون في انتظارها.

## 3.2 تضخم التذاكر

*تضخم التذاكر* هو بديل لنقل التذاكر الصريح حيث يمكن للعميل تصعيد حقوق موارده عن طريق إنشاء المزيد من تذاكر اليانصيب. بشكل عام، يجب عدم السماح بمثل هذا التضخم، حيث إنه ينتهك خصائص النمطية وعزل الحمل المرغوبة. على سبيل المثال، يمكن لعميل واحد بسهولة احتكار مورد عن طريق إنشاء عدد كبير من تذاكر اليانصيب. ومع ذلك، يمكن أن يكون تضخم التذاكر مفيداً جداً بين العملاء الموثوقين المتبادلين؛ يمكن استخدام التضخم والانكماش لتعديل تخصيصات الموارد دون اتصال صريح.

## 3.3 عملات التذاكر

بشكل عام، حواجز تجريد إدارة الموارد مرغوبة عبر حدود الثقة المنطقية. يمكن بسهولة توسيع الجدولة اليانصيبية للتعبير عن حقوق الموارد بوحدات محلية لكل مجموعة من العملاء الموثوقين المتبادلين. تُستخدم *عملة* فريدة لتسمية التذاكر ضمن كل حد ثقة. تُدعم كل عملة، أو تُمول، بتذاكر مسماة بعملات أكثر بدائية. قد تشكل علاقات العملات رسماً بيانياً لا دورياً تعسفياً، مثل تسلسل هرمي من العملات. يمكن احتواء تأثيرات التضخم محلياً عن طريق الحفاظ على سعر صرف بين كل عملة محلية وعملة أساسية محفوظة. يُعد تجريد العملة مفيداً لتسمية حقوق الموارد ومشاركتها وحمايتها بمرونة. على سبيل المثال، يمكن لقائمة التحكم في الوصول المرتبطة بعملة أن تحدد الأصول التي لديها إذن لتضخيمها عن طريق إنشاء تذاكر جديدة.

## 3.4 تذاكر التعويض

يمكن منح عميل يستهلك فقط كسراً $f$ من كم موارده المخصص *تذكرة تعويض* تضخم قيمته بمقدار $1/f$ حتى يبدأ العميل كمه التالي. هذا يضمن أن استهلاك موارد كل عميل، المساوي لـ $f$ مضروباً في احتمالية فوزه لكل يانصيب $p$، يتم تعديله بمقدار $1/f$ ليتطابق مع حصته المخصصة $p$. بدون تذاكر التعويض، سيحصل العميل الذي لا يستهلك كمه المخصص بالكامل على أقل من حصته المستحقة من المعالج.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - ticket transfer: نقل التذاكر
  - ticket inflation: تضخم التذاكر
  - ticket currency: عملة التذاكر
  - compensation ticket: تذكرة تعويض
  - trust boundary: حد الثقة
  - exchange rate: سعر صرف
  - priority inversion: انعكاس الأولوية
  - priority inheritance: وراثة الأولوية
  - first-class objects: كائنات من الدرجة الأولى
- **Equations:** Mathematical expressions for compensation (f, 1/f, p)
- **Citations:** [Sha90]
- **Special handling:** Mathematical notation preserved with Arabic context

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
