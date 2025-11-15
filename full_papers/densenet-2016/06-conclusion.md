# Section 6: Conclusion
## القسم 6: الخلاصة

**Section:** Conclusion
**Translation Quality:** 0.90
**Glossary Terms Used:** convolutional network architecture (معمارية الشبكة التلافيفية), Dense Convolutional Network (الشبكة التلافيفية الكثيفة), DenseNet, direct connections (اتصالات مباشرة), feature-map (خريطة ميزات), optimization (تحسين), accuracy (دقة), parameters (معاملات), state-of-the-art (أحدث ما توصل إليه العلم), datasets (مجموعات البيانات), performance degradation (تدهور الأداء), overfitting (الإفراط في التكيف), identity mappings (تخطيطات الهوية), deep supervision (إشراف عميق), diversified depth (عمق متنوع), feature reuse (إعادة استخدام الميزات), compact (مدمج), feature redundancy (تكرار الميزات), computer vision (رؤية حاسوبية), convolutional features (ميزات تلافيفية), hyperparameters (معاملات فائقة), learning rate schedules (جداول معدل التعلم)

---

### English Version

We proposed a new convolutional network architecture, which we refer to as Dense Convolutional Network (DenseNet). It introduces direct connections between any two layers with the same feature-map size. We showed that DenseNets scale naturally to hundreds of layers, while exhibiting no optimization difficulties. In our experiments, DenseNets tend to yield consistent improvement in accuracy with growing number of parameters, without any signs of performance degradation or overfitting. Under multiple settings, it achieved state-of-the-art results across several highly competitive datasets. Moreover, DenseNets require substantially fewer parameters and less computation to achieve state-of-the-art performances. Because we adopted hyperparameter settings optimized for residual networks in our study, we believe that further gains in accuracy of DenseNets may be obtained by more detailed tuning of hyperparameters and learning rate schedules.

Whilst following a simple connectivity rule, DenseNets naturally integrate the properties of identity mappings, deep supervision, and diversified depth. They allow feature reuse throughout the networks and can consequently learn more compact and, according to our experiments, more accurate models. Because of their compact internal representations and reduced feature redundancy, DenseNets may be good feature extractors for various computer vision tasks that build on convolutional features, e.g., [4, 5]. We plan to study such feature transfer with DenseNets in future work.

---

### النسخة العربية

اقترحنا معمارية جديدة للشبكة التلافيفية، نشير إليها باسم الشبكة التلافيفية الكثيفة (DenseNet). تُدخل اتصالات مباشرة بين أي طبقتين لهما نفس حجم خريطة الميزات. أظهرنا أن شبكات DenseNets تتوسع بشكل طبيعي إلى مئات الطبقات، دون إظهار أي صعوبات في التحسين. في تجاربنا، تميل شبكات DenseNets إلى تحقيق تحسين ثابت في الدقة مع زيادة عدد المعاملات، دون أي علامات على تدهور الأداء أو الإفراط في التكيف. في إعدادات متعددة، حققت نتائج أحدث ما توصل إليه العلم عبر العديد من مجموعات البيانات التنافسية للغاية. علاوة على ذلك، تتطلب شبكات DenseNets معاملات أقل بكثير وحسابات أقل لتحقيق أداء أحدث ما توصل إليه العلم. نظراً لأننا اعتمدنا إعدادات المعاملات الفائقة المحسّنة للشبكات المتبقية في دراستنا، نعتقد أنه يمكن الحصول على مكاسب إضافية في دقة شبكات DenseNets من خلال ضبط أكثر تفصيلاً للمعاملات الفائقة وجداول معدل التعلم.

بينما تتبع قاعدة اتصال بسيطة، تدمج شبكات DenseNets بشكل طبيعي خصائص تخطيطات الهوية والإشراف العميق والعمق المتنوع. إنها تسمح بإعادة استخدام الميزات في جميع أنحاء الشبكات ويمكنها بالتالي تعلم نماذج أكثر إدماجاً، ووفقاً لتجاربنا، أكثر دقة. بسبب تمثيلاتها الداخلية المدمجة وتقليل تكرار الميزات، قد تكون شبكات DenseNets مستخرجات ميزات جيدة لمختلف مهام الرؤية الحاسوبية التي تعتمد على الميزات التلافيفية، على سبيل المثال، [4، 5]. نخطط لدراسة نقل الميزات هذا مع شبكات DenseNets في الأعمال المستقبلية.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** None new (summary of previously introduced concepts)
- **Equations:** None
- **Citations:** [4, 5] (future work references)
- **Special handling:** Conclusion summarizes main contributions and future directions

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.93
- Readability: 0.88
- Glossary consistency: 0.90
- **Overall section score:** 0.90

### Back-translation Check

Main contribution: "تُدخل اتصالات مباشرة بين أي طبقتين لهما نفس حجم خريطة الميزات" → "Introduces direct connections between any two layers with the same feature-map size" - accurately preserves the core innovation.

Future work: "نخطط لدراسة نقل الميزات هذا مع شبكات DenseNets في الأعمال المستقبلية" → "We plan to study such feature transfer with DenseNets in future work" - correctly maintains research direction.
