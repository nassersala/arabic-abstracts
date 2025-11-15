# Section 6: Conclusion
## القسم 6: الخاتمة

**Section:** conclusion
**Translation Quality:** 0.87
**Glossary Terms Used:** distributed system, event, causality, logical clock, physical clock, synchronization, anomalous behavior

---

### English Version

We have seen that the concept of "happening before" defines a partial ordering of the events in a distributed system. We have shown how to extend this to a total ordering, and how to use this ordering to solve synchronization problems. The total ordering defined by our algorithm has the property that it orders events in a way that is consistent with the causal structure of the computation.

An interesting aspect of the approach is that no message need contain a statement of the global state. Each process makes its decisions based only upon the information available to it. The correctness of a process's decision depends only upon the ordering of events defined by the relation ⇒, which in turn depends upon the logical clocks. No global state information need be communicated.

We have shown that the logical clocks can be implemented in such a way that they approximate physical time, with a bound on how far apart the different clocks can be. This bound is determined by the communication delay and the rate at which the physical clocks drift.

An anomalous behavior can occur in a distributed system if we rely upon real time ordering. For example, suppose one person makes a telephone call to another and says "I just sent you a message." If the message and phone call travel through two different communication media, the phone call might arrive before the message, leading to an apparent violation of causality. Our algorithm ensures that such anomalies cannot occur if processes use the logical clocks to order events, rather than relying upon real-time information.

The approach described here provides a foundation for designing correct distributed algorithms. By using logical clocks, we can ensure that the system behaves correctly according to the causal ordering of events, independent of the vagaries of message transmission times.

---

### النسخة العربية

لقد رأينا أن مفهوم "حدث قبل" يُعرّف ترتيباً جزئياً للأحداث في نظام موزع. أظهرنا كيفية توسيع هذا إلى ترتيب كامل، وكيفية استخدام هذا الترتيب لحل مسائل التزامن. الترتيب الكامل المُعرَّف بواسطة خوارزميتنا له خاصية أنه يرتب الأحداث بطريقة متسقة مع البنية السببية للحساب.

جانب مثير للاهتمام من هذا النهج هو أنه لا تحتاج أي رسالة إلى احتواء بيان للحالة العامة. كل عملية تتخذ قراراتها بناءً فقط على المعلومات المتاحة لها. تعتمد صحة قرار العملية فقط على ترتيب الأحداث المُعرَّف بواسطة العلاقة ⇒، والذي يعتمد بدوره على الساعات المنطقية. لا حاجة لتوصيل معلومات الحالة العامة.

أظهرنا أن الساعات المنطقية يمكن تنفيذها بطريقة تقارب الوقت الفيزيائي، مع حد أعلى على مدى تباعد الساعات المختلفة عن بعضها. يُحدد هذا الحد بواسطة تأخير الاتصال ومعدل انحراف الساعات الفيزيائية.

يمكن أن يحدث سلوك شاذ في نظام موزع إذا اعتمدنا على ترتيب الوقت الحقيقي. على سبيل المثال، لنفترض أن شخصاً ما أجرى مكالمة هاتفية مع آخر وقال "لقد أرسلت لك للتو رسالة". إذا سافرت الرسالة والمكالمة الهاتفية عبر وسطين اتصال مختلفين، فقد تصل المكالمة الهاتفية قبل الرسالة، مما يؤدي إلى انتهاك ظاهري للسببية. تضمن خوارزميتنا عدم حدوث مثل هذه الحالات الشاذة إذا استخدمت العمليات الساعات المنطقية لترتيب الأحداث، بدلاً من الاعتماد على معلومات الوقت الحقيقي.

يوفر النهج الموصوف هنا أساساً لتصميم خوارزميات موزعة صحيحة. باستخدام الساعات المنطقية، يمكننا ضمان تصرف النظام بشكل صحيح وفقاً للترتيب السببي للأحداث، بشكل مستقل عن تقلبات أوقات نقل الرسائل.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** global state, causal structure, anomalous behavior, real-time ordering
- **Equations:** 0
- **Citations:** 0
- **Special handling:** Telephone call example preserved as concrete illustration of anomalous behavior

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
