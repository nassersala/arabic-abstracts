---
# Communication-Efficient Learning of Deep Networks from Decentralized Data
## التعلم الفعّال اتصالياً للشبكات العميقة من البيانات اللامركزية

**arXiv ID:** 1602.05629
**Authors:** H. Brendan McMahan, Eider Moore, Daniel Ramage, Seth Hampson, Blaise Agüera y Arcas
**Year:** 2016
**Categories:** cs.LG
**Translation Quality:** 0.88
**Glossary Terms Used:** federated learning (تعلم اتحادي), training (التدريب), deep networks (شبكات عميقة), distributed (موزع), model (نموذج), privacy (خصوصية), architecture (معمارية)

### English Abstract
Modern mobile devices have access to a wealth of data suitable for learning models, which in turn can greatly improve the user experience on the device. For example, language models can improve speech recognition and text entry, and image models can automatically select good photos. However, this rich data is often privacy sensitive, large in quantity, or both, which may preclude logging to the data center and training there using conventional approaches. We advocate an alternative that leaves the training data distributed on the mobile devices, and learns a shared model by aggregating locally-computed updates. We term this decentralized approach Federated Learning.

We present a practical method for the federated learning of deep networks based on iterative model averaging, and conduct an extensive empirical evaluation, considering five different model architectures and four datasets. These experiments demonstrate the approach is robust to the unbalanced and non-IID data distributions that are a defining characteristic of this setting. Communication costs are the principal constraint, and we show a reduction in required communication rounds by 10-100x as compared to synchronized stochastic gradient descent.

### الملخص العربي
تمتلك الأجهزة المحمولة الحديثة إمكانية الوصول إلى ثروة من البيانات المناسبة لتعلم النماذج، والتي يمكن بدورها تحسين تجربة المستخدم على الجهاز بشكل كبير. على سبيل المثال، يمكن لنماذج اللغة تحسين التعرف على الكلام وإدخال النص، ويمكن لنماذج الصور اختيار الصور الجيدة تلقائياً. ومع ذلك، فإن هذه البيانات الغنية غالباً ما تكون حساسة للخصوصية، أو كبيرة الكمية، أو كليهما، مما قد يمنع تسجيلها في مركز البيانات والتدريب هناك باستخدام الأساليب التقليدية. نحن ندعو إلى بديل يترك بيانات التدريب موزعة على الأجهزة المحمولة، ويتعلم نموذجاً مشتركاً من خلال تجميع التحديثات المحسوبة محلياً. نطلق على هذا النهج اللامركزي اسم التعلم الاتحادي.

نقدم طريقة عملية للتعلم الاتحادي للشبكات العميقة بناءً على متوسط النموذج التكراري، ونجري تقييماً تجريبياً موسعاً، مع النظر في خمس معماريات مختلفة للنموذج وأربع مجموعات بيانات. توضح هذه التجارب أن النهج قوي تجاه توزيعات البيانات غير المتوازنة وغير المستقلة والموزعة بشكل متطابق والتي تعتبر خاصية محددة لهذا الإعداد. تكاليف الاتصال هي القيد الرئيسي، ونظهر انخفاضاً في جولات الاتصال المطلوبة بمقدار 10-100 ضعف مقارنة بالانحدار التدرجي العشوائي المتزامن.

### Back-Translation (Validation)
Modern mobile devices have access to a wealth of data suitable for learning models, which in turn can greatly improve the user experience on the device. For example, language models can improve speech recognition and text entry, and image models can automatically select good photos. However, this rich data is often privacy-sensitive, or large in quantity, or both, which may prevent logging it to the data center and training there using traditional methods. We advocate an alternative that leaves training data distributed on mobile devices, and learns a shared model through aggregating locally computed updates. We call this decentralized approach Federated Learning.

We present a practical method for federated learning of deep networks based on iterative model averaging, and conduct an extensive empirical evaluation, considering five different model architectures and four datasets. These experiments demonstrate that the approach is robust toward unbalanced and non-independent identically distributed data distributions which are a defining characteristic of this setting. Communication costs are the main constraint, and we show a reduction in required communication rounds by 10-100 times compared to synchronized stochastic gradient descent.

### Translation Metrics
- Iterations: 1
- Final Score: 0.88
- Quality: High
---
