# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** differential privacy, database, privacy, algorithm, accuracy, minimax, histogram, sensitivity, sparse

---

### English Version

Differential privacy (DP) ([8]) is a type of privacy guarantee that has become quite popular in the computer science literature. The advantage of differential privacy is that it gives a strong and mathematically rigorous guarantee. The disadvantage is that the strong privacy guarantee often comes at the expense of the statistical utility of the released information. We propose a weaker notion of privacy, called "random differential privacy" (RDP), under which it is possible to achieve better accuracy.

The privacy guarantee provided by RDP represents a radical weakening of the ordinary differential privacy. This could be a cause for concern for those who want very strong privacy guarantees. Indeed, we are not suggesting the RDP should replace ordinary differential privacy. However, as we shall show in this paper (and has been observed many times in the past), differential privacy can lead to large information losses in some cases (see e.g., [9]). Thus, we feel there is great value in exploring weakened versions of differential privacy. In other words, we are proposing a new privacy definition as a way of exploring the privacy/accuracy tradeoff.

We begin by introducing ordinary differential privacy and setting up some notation. We then explore the lower limits for accuracy of differentially private techniques in the context of histograms. We introduce a concept which parallels minimaxity in statistics, and identify the minimax risk for a differentially private histogram. We describe an important subset of these minimax differentially private histograms which we show to have risk which is uniformly lower bounded at a rate which is linear in the dimension of the histogram. We then introduce our proposed relaxation to differential privacy, under which our technique enjoys the same minimax risk, but with a lower bound which depends only on the size of the support of the histogram (namely, the number of nonzero cells). Thus we show that in the context of sparse histograms, the relaxation allows for a strictly better data release. We also demonstrate some important properties of our relaxation, such as an analog of the composition lemma.

---

### النسخة العربية

الخصوصية التفاضلية (DP) ([8]) هي نوع من ضمانات الخصوصية التي أصبحت شائعة جداً في أدبيات علوم الحاسوب. تكمن ميزة الخصوصية التفاضلية في أنها تقدم ضماناً قوياً ودقيقاً رياضياً. أما العيب فهو أن ضمان الخصوصية القوي غالباً ما يأتي على حساب المنفعة الإحصائية للمعلومات المُصدَرة. نقترح مفهوماً أضعف للخصوصية، يُسمى "الخصوصية التفاضلية العشوائية" (RDP)، والذي يمكن من خلاله تحقيق دقة أفضل.

إن ضمان الخصوصية الذي توفره RDP يمثل إضعافاً جذرياً للخصوصية التفاضلية العادية. قد يكون هذا مدعاة للقلق لأولئك الذين يريدون ضمانات خصوصية قوية جداً. في الواقع، نحن لا نقترح أن تحل RDP محل الخصوصية التفاضلية العادية. ومع ذلك، كما سنُظهر في هذه الورقة (وكما لوحظ مرات عديدة في الماضي)، يمكن أن تؤدي الخصوصية التفاضلية إلى خسائر كبيرة في المعلومات في بعض الحالات (انظر على سبيل المثال [9]). لذلك، نشعر أن هناك قيمة كبيرة في استكشاف نسخ مُضعَفة من الخصوصية التفاضلية. بعبارة أخرى، نقترح تعريفاً جديداً للخصوصية كوسيلة لاستكشاف المقايضة بين الخصوصية والدقة.

نبدأ بتقديم الخصوصية التفاضلية العادية ووضع بعض الترميزات. ثم نستكشف الحدود الدنيا لدقة التقنيات الخاصة تفاضلياً في سياق الرسوم البيانية الهيستوغرامية. نقدم مفهوماً يوازي المينيماكس في الإحصاء، ونحدد مخاطر المينيماكس للرسم البياني الهيستوغرامي الخاص تفاضلياً. نصف مجموعة فرعية مهمة من هذه الرسوم البيانية الهيستوغرامية الخاصة تفاضلياً والتي نُظهر أن لها مخاطر محدودة من الأسفل بشكل موحد بمعدل خطي في بُعد الرسم البياني الهيستوغرامي. ثم نقدم الإرخاء المقترح للخصوصية التفاضلية، حيث تتمتع تقنيتنا بنفس مخاطر المينيماكس، ولكن مع حد أدنى يعتمد فقط على حجم الدعم للرسم البياني الهيستوغرامي (أي عدد الخلايا غير الصفرية). وبالتالي نُظهر أنه في سياق الرسوم البيانية الهيستوغرامية المتناثرة، يسمح الإرخاء بإصدار بيانات أفضل بشكل صارم. كما نوضح بعض الخصائص المهمة لإرخائنا، مثل نظير لمبرهنة التركيب.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** differential privacy (DP), random differential privacy (RDP), minimax risk, privacy/accuracy tradeoff, sparse histograms, composition lemma
- **Equations:** None
- **Citations:** [8], [9]
- **Special handling:** Technical terminology for privacy concepts; mathematical terms like "minimax" kept with Arabic explanation

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.88
- Readability: 0.88
- Glossary consistency: 0.88
- **Overall section score:** 0.88
