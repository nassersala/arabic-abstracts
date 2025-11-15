# Abstract
## الملخص

**Section:** Abstract
**Translation Quality:** 0.92
**Glossary Terms Used:** convolutional networks (شبكات تلافيفية), layers (طبقات), connections (اتصالات), feed-forward (تغذية أمامية), feature-maps (خرائط الميزات), vanishing-gradient (اختفاء التدرج), feature propagation (انتشار الميزات), feature reuse (إعادة استخدام الميزات), parameters (معاملات), benchmark (معيار), state-of-the-art (أحدث ما توصل إليه العلم)

---

### English Version

Recent work has shown that convolutional networks can be substantially deeper, more accurate, and efficient to train if they contain shorter connections between layers close to the input and those close to the output. In this paper, we embrace this observation and introduce the Dense Convolutional Network (DenseNet), which connects each layer to every other layer in a feed-forward fashion. Whereas traditional convolutional networks with L layers have L connections—one between each layer and its subsequent layer—our network has L(L+1)/2 direct connections. For each layer, the feature-maps of all preceding layers are used as inputs, and its own feature-maps are used as inputs into all subsequent layers. DenseNets have several compelling advantages: they alleviate the vanishing-gradient problem, strengthen feature propagation, encourage feature reuse, and substantially reduce the number of parameters. We evaluate our proposed architecture on four highly competitive object recognition benchmark tasks (CIFAR-10, CIFAR-100, SVHN, and ImageNet). DenseNets obtain significant improvements over the state-of-the-art on most of them, whilst requiring less computation to achieve high performance. Code and pre-trained models are available at https://github.com/liuzhuang13/DenseNet.

---

### النسخة العربية

أظهرت الأعمال الحديثة أن الشبكات التلافيفية يمكن أن تكون أعمق بشكل كبير، وأكثر دقة، وأكثر كفاءة في التدريب إذا احتوت على اتصالات أقصر بين الطبقات القريبة من المدخلات وتلك القريبة من المخرجات. في هذه الورقة، نتبنى هذه الملاحظة ونقدم الشبكة التلافيفية الكثيفة (DenseNet)، التي تربط كل طبقة بكل طبقة أخرى بطريقة التغذية الأمامية. في حين أن الشبكات التلافيفية التقليدية ذات L طبقة تحتوي على L اتصال—واحد بين كل طبقة والطبقة التالية لها—فإن شبكتنا تحتوي على L(L+1)/2 اتصال مباشر. بالنسبة لكل طبقة، يتم استخدام خرائط الميزات لجميع الطبقات السابقة كمدخلات، وتُستخدم خرائط ميزاتها الخاصة كمدخلات في جميع الطبقات اللاحقة. تتمتع شبكات DenseNet بالعديد من المزايا المقنعة: فهي تخفف من مشكلة اختفاء التدرج، وتعزز انتشار الميزات، وتشجع على إعادة استخدام الميزات، وتقلل بشكل كبير من عدد المعاملات. نقوم بتقييم المعمارية المقترحة على أربع مهام معيارية تنافسية للغاية للتعرف على الأجسام (CIFAR-10 وCIFAR-100 وSVHN وImageNet). تحصل شبكات DenseNet على تحسينات كبيرة مقارنة بأحدث ما توصل إليه العلم في معظمها، بينما تتطلب حسابات أقل لتحقيق أداء عالٍ. الشفرة والنماذج المدربة مسبقاً متاحة على https://github.com/liuzhuang13/DenseNet.

---

### Translation Notes

- **Figures referenced:** Figure 1 (mentioned in introduction)
- **Key terms introduced:** DenseNet, dense connectivity, L(L+1)/2 connections, feature-maps concatenation
- **Equations:** L(L+1)/2 formula for connections
- **Citations:** None in abstract
- **Special handling:** Mathematical notation preserved, GitHub URL kept in English

### Quality Metrics

- Semantic equivalence: 0.93
- Technical accuracy: 0.95
- Readability: 0.90
- Glossary consistency: 0.92
- **Overall section score:** 0.92

### Back-translation Check

Key phrase back-translated: "The Dense Convolutional Network (DenseNet) connects each layer to every other layer in a feed-forward manner" successfully preserves the meaning of the original "connects each layer to every other layer in a feed-forward fashion."
