# Section 9: Operational Profile
## القسم 9: الملف التشغيلي

**Section:** operational-profile
**Translation Quality:** 0.86
**Glossary Terms Used:** federated learning, device, population, active devices, participation, eligibility criteria, pace steering, dropout, round, server, selection, diurnal patterns

---

### English Version

This section presents an overview of key operational metrics from the deployed federated learning system operating on production workloads for over a year, with additional details in Appendix A.

**System Scale and Population**

The system currently handles "a cumulative FL population size of approximately 10M daily active devices, spanning several different applications." The design aims to scale elastically with population sizes potentially reaching billions.

**Device Participation Patterns**

At any given time, device availability is constrained by eligibility criteria and pace steering mechanisms. The system observes "up to 10k devices are participating simultaneously," with substantial temporal variation. Device participation shows strong diurnal patterns, as "devices are more likely idle and charging at night," resulting in "a 4×4\\times difference between low and high numbers of participating devices over a 24 hours period for a US-centric population."

**Selection and Dropout Rates**

Research by McMahan et al. indicates that "receiving updates from a few hundred devices per FL round is sufficient." The system observes that "on average the portion of devices that drop out due to computation errors, network failures, or changes in eligibility varies between 6% and 10%." To compensate, "the server typically selects 130% of the target number of devices to initially participate."

This section emphasizes that performance metrics vary significantly based on device characteristics, network conditions, model sizes, and computational complexity—reflecting real-world deployment variability.

---

### النسخة العربية

يقدم هذا القسم نظرة عامة على المقاييس التشغيلية الرئيسية من نظام التعلم الاتحادي المنشور الذي يعمل على أحمال عمل إنتاجية لأكثر من عام، مع تفاصيل إضافية في الملحق A.

**حجم النظام والمجموعة**

يتعامل النظام حالياً مع "حجم مجموعة تعلم اتحادي تراكمي يبلغ حوالي 10 ملايين جهاز نشط يومياً، يمتد عبر عدة تطبيقات مختلفة". يهدف التصميم إلى التوسع بشكل مرن مع أحجام مجموعات قد تصل إلى المليارات.

**أنماط مشاركة الأجهزة**

في أي وقت معين، يكون توفر الأجهزة مقيداً بمعايير الأهلية وآليات توجيه الوتيرة. يلاحظ النظام "ما يصل إلى 10 آلاف جهاز يشاركون في نفس الوقت"، مع تباين زمني كبير. تُظهر مشاركة الأجهزة أنماطاً يومية قوية، حيث "من المرجح أن تكون الأجهزة في وضع الخمول وقيد الشحن في الليل"، مما يؤدي إلى "فرق 4× بين الأعداد المنخفضة والعالية للأجهزة المشاركة على مدار فترة 24 ساعة لمجموعة تتمحور حول الولايات المتحدة".

**معدلات الاختيار والانقطاع**

تشير الأبحاث التي أجراها McMahan وآخرون إلى أن "تلقي التحديثات من بضع مئات من الأجهزة لكل جولة تعلم اتحادي يكفي". يلاحظ النظام أن "في المتوسط، يتراوح جزء الأجهزة التي تنقطع بسبب أخطاء الحساب أو حالات فشل الشبكة أو التغييرات في الأهلية بين 6٪ و 10٪". للتعويض، "عادةً ما يختار الخادم 130٪ من العدد المستهدف من الأجهزة للمشاركة في البداية".

يؤكد هذا القسم أن مقاييس الأداء تختلف بشكل كبير بناءً على خصائص الأجهزة وظروف الشبكة وأحجام النماذج والتعقيد الحسابي - مما يعكس تباين النشر في العالم الواقعي.

---

### Translation Notes

- **Figures referenced:** Appendix A (referenced but not shown)
- **Key terms introduced:** daily active devices, cumulative FL population, elastic scaling, eligibility criteria, temporal variation, diurnal patterns, dropout rates, target number
- **Equations:** 1 (4× difference mentioned in text)
- **Citations:** McMahan et al. (implicit reference)
- **Special handling:** Numeric values (10M, 10k, 6%-10%, 130%) kept in original format. The 4× symbol kept as is since it's a mathematical notation. "US-centric population" translated while keeping geographic reference clear.

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86
