# Section 3: Related Work
## القسم 3: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.86
**Glossary Terms Used:** regularization, neural network, ensemble, bagging, boosting, overfitting, weight decay, early stopping, L1 regularization, L2 regularization, model averaging

---

### English Version

Dropout is a way of regularizing neural networks by adding noise to the hidden units. There are several other ways of introducing noise into neural networks that have been studied extensively.

**Regularization Methods:** The most common way to regularize neural networks is by using weight decay (L2 regularization) or weight elimination (L1 regularization). These methods penalize large weights and encourage the network to keep the weights small. Early stopping is another popular regularization technique where training is stopped when performance on a validation set starts getting worse. Adding Gaussian noise to the inputs of a neural network is also a common way to regularize.

**Model Combination:** Combining predictions from multiple models is one of the most reliable ways to improve performance. Bagging (Breiman, 1994) involves training different models on different subsets of the data and averaging their predictions. Boosting (Freund and Schapire, 1997) trains models sequentially, with each new model focusing on the examples that previous models got wrong. Bayesian model averaging involves combining predictions from all possible parameter settings, weighted by their posterior probability.

**Random Forests:** Random forests (Breiman, 2001) are a way of bagging decision trees. Each tree is trained on a different random subset of the data, and at each node, a random subset of the features is considered for splitting. This randomness prevents overfitting and makes the trees more robust. Dropout can be seen as a way of doing something similar for neural networks.

**Denoising Autoencoders:** Vincent et al. (2008, 2010) showed that adding noise to the inputs of an autoencoder and training it to reconstruct the clean inputs helps the autoencoder learn useful representations. This is related to dropout in that both involve adding noise during training.

**Marginalized Dropout:** Dropout can be seen as a way of training an exponential number of neural networks with shared weights. Wang and Manning (2013) showed that for linear models, it is possible to analytically marginalize out the dropout noise, which gives a closed-form solution. However, for non-linear networks, marginalization is intractable.

---

### النسخة العربية

Dropout هي طريقة لتنظيم الشبكات العصبية عن طريق إضافة الضوضاء إلى الوحدات المخفية. هناك عدة طرق أخرى لإدخال الضوضاء في الشبكات العصبية التي تمت دراستها على نطاق واسع.

**طرق التنظيم:** الطريقة الأكثر شيوعاً لتنظيم الشبكات العصبية هي باستخدام تضاؤل الوزن (تنظيم L2) أو إزالة الوزن (تنظيم L1). تعاقب هذه الطرق الأوزان الكبيرة وتشجع الشبكة على إبقاء الأوزان صغيرة. الإيقاف المبكر هو تقنية تنظيم شائعة أخرى حيث يتم إيقاف التدريب عندما يبدأ الأداء على مجموعة التحقق في التدهور. إضافة ضوضاء غاوسية إلى مدخلات الشبكة العصبية هي أيضاً طريقة شائعة للتنظيم.

**دمج النماذج:** يعد الجمع بين التنبؤات من نماذج متعددة من أكثر الطرق موثوقية لتحسين الأداء. يتضمن التجميع (Breiman, 1994) تدريب نماذج مختلفة على مجموعات فرعية مختلفة من البيانات وحساب متوسط تنبؤاتها. يدرب التعزيز (Freund and Schapire, 1997) النماذج بشكل تسلسلي، حيث يركز كل نموذج جديد على الأمثلة التي أخطأت فيها النماذج السابقة. يتضمن حساب المتوسط البايزي للنماذج الجمع بين التنبؤات من جميع إعدادات المعاملات الممكنة، مرجحة حسب احتمالها اللاحق.

**الغابات العشوائية:** الغابات العشوائية (Breiman, 2001) هي طريقة لتجميع أشجار القرار. يتم تدريب كل شجرة على مجموعة فرعية عشوائية مختلفة من البيانات، وفي كل عقدة، يتم النظر في مجموعة فرعية عشوائية من الميزات للتقسيم. تمنع هذه العشوائية الإفراط في التدريب وتجعل الأشجار أكثر قوة. يمكن النظر إلى dropout على أنه طريقة للقيام بشيء مماثل للشبكات العصبية.

**المشفرات التلقائية لإزالة الضوضاء:** أظهر Vincent et al. (2008, 2010) أن إضافة الضوضاء إلى مدخلات المشفر التلقائي وتدريبه على إعادة بناء المدخلات النظيفة يساعد المشفر التلقائي على تعلم تمثيلات مفيدة. هذا مرتبط بـ dropout من حيث أن كليهما يتضمن إضافة الضوضاء أثناء التدريب.

**Dropout الهامشي:** يمكن النظر إلى dropout على أنه طريقة لتدريب عدد أسي من الشبكات العصبية بأوزان مشتركة. أظهر Wang and Manning (2013) أنه بالنسبة للنماذج الخطية، من الممكن تهميش ضوضاء dropout تحليلياً، مما يعطي حلاً مغلق الشكل. ومع ذلك، بالنسبة للشبكات غير الخطية، فإن التهميش غير قابل للحل.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** weight decay, early stopping, bagging, boosting, random forests, denoising autoencoders, marginalization
- **Equations:** None
- **Citations:** Breiman (1994, 2001), Freund and Schapire (1997), Vincent et al. (2008, 2010), Wang and Manning (2013)
- **Special handling:**
  - "L1" and "L2 regularization" kept as technical terms
  - "Bagging", "boosting", "dropout" kept in English as established ML terms
  - Citations kept in original format

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.90
- Readability: 0.83
- Glossary consistency: 0.85
- **Overall section score:** 0.86
