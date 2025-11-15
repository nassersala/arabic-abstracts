# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.92
**Glossary Terms Used:** federated learning, distributed learning, optimization, heterogeneous, convergence, dataset, test accuracy, framework, accuracy, distributed system, network, algorithm, parameter

---

### English Version

Federated Learning is a distributed learning paradigm with two key challenges that differentiate it from traditional distributed optimization: (1) significant variability in terms of the systems characteristics on each device in the network (systems heterogeneity), and (2) non-identically distributed data across the network (statistical heterogeneity). In this work, we introduce a framework, FedProx, to tackle heterogeneity in federated networks. FedProx can be viewed as a generalization and re-parametrization of FedAvg, the current state-of-the-art method for federated learning. While this re-parameterization makes only minor modifications to the method itself, these modifications have important ramifications both in theory and in practice. Theoretically, we provide convergence guarantees for our framework when learning over data from non-identical distributions (statistical heterogeneity), and while adhering to device-level systems constraints by allowing each participating device to perform a variable amount of work (systems heterogeneity). Practically, we demonstrate that FedProx allows for more robust convergence than FedAvg across a suite of realistic federated datasets. In particular, in highly heterogeneous settings, FedProx demonstrates significantly more stable and accurate convergence behavior relative to FedAvg---improving absolute test accuracy by 22% on average.

---

### النسخة العربية

التعلم الاتحادي هو نموذج تعلم موزع يتميز بتحديين رئيسيين يميزانه عن التحسين الموزع التقليدي: (1) التباين الكبير في خصائص الأنظمة على كل جهاز في الشبكة (عدم التجانس في الأنظمة)، و(2) البيانات الموزعة بشكل غير متطابق عبر الشبكة (عدم التجانس الإحصائي). في هذا العمل، نقدم إطار عمل يسمى FedProx لمعالجة عدم التجانس في الشبكات الاتحادية. يمكن اعتبار FedProx بمثابة تعميم وإعادة بارمترة لـ FedAvg، وهي الطريقة الحالية الأكثر تقدمًا للتعلم الاتحادي. في حين أن إعادة البارمترة هذه تجري تعديلات طفيفة فقط على الطريقة نفسها، فإن هذه التعديلات لها تداعيات مهمة من الناحية النظرية والعملية. من الناحية النظرية، نقدم ضمانات التقارب لإطار عملنا عند التعلم من البيانات ذات التوزيعات غير المتطابقة (عدم التجانس الإحصائي)، ومع الالتزام بقيود الأنظمة على مستوى الجهاز من خلال السماح لكل جهاز مشارك بأداء كمية متغيرة من العمل (عدم التجانس في الأنظمة). من الناحية العملية، نوضح أن FedProx يسمح بتقارب أكثر قوة من FedAvg عبر مجموعة من مجموعات البيانات الاتحادية الواقعية. على وجه الخصوص، في الإعدادات شديدة عدم التجانس، يُظهر FedProx سلوك تقارب أكثر استقرارًا ودقة بشكل ملحوظ مقارنة بـ FedAvg - مما يحسن دقة الاختبار المطلقة بنسبة 22% في المتوسط.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** federated learning (التعلم الاتحادي), systems heterogeneity (عدم التجانس في الأنظمة), statistical heterogeneity (عدم التجانس الإحصائي), FedProx, FedAvg, convergence (التقارب)
- **Equations:** None
- **Citations:** None
- **Special handling:** Algorithm names FedProx and FedAvg kept in English as they are proper names

### Quality Metrics

- Semantic equivalence: 0.93
- Technical accuracy: 0.92
- Readability: 0.92
- Glossary consistency: 0.91
- **Overall section score:** 0.92
