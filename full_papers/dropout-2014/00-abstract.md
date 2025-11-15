# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.92
**Glossary Terms Used:** neural network, overfitting, dropout, regularization, training, test, co-adaptation, feature detector

---

### English Version

When a large feedforward neural network is trained on a small training set, it typically performs poorly on held-out test data. This "overfitting" is greatly reduced by randomly omitting half of the feature detectors on each training case. This prevents complex co-adaptations in which a feature detector is only helpful in the context of several other specific feature detectors. Instead, each neuron learns to detect a feature that is generally helpful for producing the correct answer given the combinatorially large variety of internal contexts in which it must operate. Random "dropout" gives big improvements on many benchmark tasks and sets new records for speech and object recognition.

Deep neural nets with a large number of parameters are very powerful machine learning systems. However, overfitting is a serious problem in such networks. Large networks are also slow to use, making it difficult to deal with overfitting by combining the predictions of many different large neural nets at test time. Dropout is a technique for addressing this problem. The key idea is to randomly drop units (along with their connections) from the neural network during training. This prevents units from co-adapting too much. During training, dropout samples from an exponential number of different "thinned" networks. At test time, it is easy to approximate the effect of averaging the predictions of all these thinned networks by simply using a single unthinned network that has smaller weights. This significantly reduces overfitting and gives major improvements over other regularization methods. We show that dropout improves the performance of neural networks on supervised learning tasks in vision, speech recognition, document classification and computational biology, obtaining state-of-the-art results on many benchmark data sets.

---

### النسخة العربية

عندما يتم تدريب شبكة عصبية أمامية كبيرة على مجموعة تدريب صغيرة، فإنها عادةً ما تحقق أداءً ضعيفاً على بيانات الاختبار المحجوبة. يتم تقليل هذا "الإفراط في التدريب" بشكل كبير عن طريق حذف نصف كاشفات الميزات بشكل عشوائي في كل حالة تدريب. يمنع هذا التكيفات المشتركة المعقدة التي يكون فيها كاشف الميزات مفيداً فقط في سياق العديد من كاشفات الميزات المحددة الأخرى. بدلاً من ذلك، تتعلم كل خلية عصبية اكتشاف ميزة مفيدة بشكل عام لإنتاج الإجابة الصحيحة بالنظر إلى التنوع الكبير تجميعياً للسياقات الداخلية التي يجب أن تعمل فيها. يعطي "dropout" العشوائي تحسينات كبيرة في العديد من المهام المعيارية ويحقق أرقاماً قياسية جديدة في التعرف على الكلام والأشياء.

الشبكات العصبية العميقة التي تحتوي على عدد كبير من المعاملات هي أنظمة تعلم آلي قوية جداً. ومع ذلك، يعد الإفراط في التدريب مشكلة خطيرة في مثل هذه الشبكات. الشبكات الكبيرة أيضاً بطيئة في الاستخدام، مما يجعل من الصعب التعامل مع الإفراط في التدريب عن طريق دمج تنبؤات العديد من الشبكات العصبية الكبيرة المختلفة في وقت الاختبار. Dropout هي تقنية لمعالجة هذه المشكلة. الفكرة الرئيسية هي حذف الوحدات (جنباً إلى جنب مع اتصالاتها) بشكل عشوائي من الشبكة العصبية أثناء التدريب. يمنع هذا الوحدات من التكيف المشترك بشكل مفرط. أثناء التدريب، يأخذ dropout عينات من عدد أسي من الشبكات "المخففة" المختلفة. في وقت الاختبار، من السهل تقريب تأثير حساب متوسط تنبؤات كل هذه الشبكات المخففة ببساطة باستخدام شبكة واحدة غير مخففة لها أوزان أصغر. يقلل هذا بشكل كبير من الإفراط في التدريب ويعطي تحسينات كبيرة مقارنة بطرق التنظيم الأخرى. نُظهر أن dropout يحسن أداء الشبكات العصبية في مهام التعلم الخاضع للإشراف في الرؤية الحاسوبية، والتعرف على الكلام، وتصنيف المستندات، والبيولوجيا الحسابية، ويحقق نتائج متقدمة على العديد من مجموعات البيانات المعيارية.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:** dropout, overfitting, co-adaptation, feature detector, thinned networks, regularization
- **Equations:** None
- **Citations:** None
- **Special handling:** The term "dropout" is kept in English as it's a technical term that has been widely adopted in the Arabic ML community

### Quality Metrics

- Semantic equivalence: 0.93
- Technical accuracy: 0.95
- Readability: 0.90
- Glossary consistency: 0.90
- **Overall section score:** 0.92
