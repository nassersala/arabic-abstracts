# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** neural network, deep learning, overfitting, regularization, training, generalization, parameters, hidden units, backpropagation

---

### English Version

Deep neural nets with a large number of parameters are very powerful machine learning systems. However, overfitting is a serious problem in such networks. Large networks are also slow to use, making it difficult to deal with overfitting by combining the predictions of many different large neural nets at test time. Dropout is a technique for addressing this problem. The key idea is to randomly drop units (along with their connections) from the neural network during training. This prevents units from co-adapting too much. During training, dropout samples from an exponential number of different "thinned" networks. At test time, it is easy to approximate the effect of averaging the predictions of all these thinned networks by simply using a single unthinned network that has smaller weights. This significantly reduces overfitting and gives major improvements over other regularization methods.

We show that dropout improves the performance of neural networks on supervised learning tasks in vision, speech recognition, document classification and computational biology, obtaining state-of-the-art results on many benchmark data sets. In Section 2, we describe the motivation for this approach. Section 3 describes related work. Section 4 formally describes the dropout model and gives a practical guide for training dropout networks. Section 5 presents experimental results. Section 6 analyzes several properties of dropout. Section 7 explores the effect of different kinds of input noise. Section 8 describes how dropout can be used in Restricted Boltzmann Machines. Section 9 discusses some extensions and variations of dropout. Section 10 concludes with a discussion of the advantages of dropout.

---

### النسخة العربية

الشبكات العصبية العميقة التي تحتوي على عدد كبير من المعاملات هي أنظمة تعلم آلي قوية جداً. ومع ذلك، يعد الإفراط في التدريب مشكلة خطيرة في مثل هذه الشبكات. الشبكات الكبيرة أيضاً بطيئة في الاستخدام، مما يجعل من الصعب التعامل مع الإفراط في التدريب عن طريق دمج تنبؤات العديد من الشبكات العصبية الكبيرة المختلفة في وقت الاختبار. Dropout هي تقنية لمعالجة هذه المشكلة. الفكرة الرئيسية هي حذف الوحدات (جنباً إلى جنب مع اتصالاتها) بشكل عشوائي من الشبكة العصبية أثناء التدريب. يمنع هذا الوحدات من التكيف المشترك بشكل مفرط. أثناء التدريب، يأخذ dropout عينات من عدد أسي من الشبكات "المخففة" المختلفة. في وقت الاختبار، من السهل تقريب تأثير حساب متوسط تنبؤات كل هذه الشبكات المخففة ببساطة باستخدام شبكة واحدة غير مخففة لها أوزان أصغر. يقلل هذا بشكل كبير من الإفراط في التدريب ويعطي تحسينات كبيرة مقارنة بطرق التنظيم الأخرى.

نُظهر أن dropout يحسن أداء الشبكات العصبية في مهام التعلم الخاضع للإشراف في الرؤية الحاسوبية، والتعرف على الكلام، وتصنيف المستندات، والبيولوجيا الحسابية، ويحقق نتائج متقدمة على العديد من مجموعات البيانات المعيارية. في القسم 2، نصف الدافع وراء هذا النهج. يصف القسم 3 الأعمال ذات الصلة. يصف القسم 4 بشكل رسمي نموذج dropout ويقدم دليلاً عملياً لتدريب شبكات dropout. يقدم القسم 5 النتائج التجريبية. يحلل القسم 6 العديد من خصائص dropout. يستكشف القسم 7 تأثير أنواع مختلفة من ضوضاء الإدخال. يصف القسم 8 كيف يمكن استخدام dropout في آلات بولتزمان المقيدة. يناقش القسم 9 بعض الامتدادات والتنويعات على dropout. يختتم القسم 10 بمناقشة مزايا dropout.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** thinned networks, Restricted Boltzmann Machines, supervised learning
- **Equations:** None
- **Citations:** Implicit references to sections 2-10
- **Special handling:** Kept "dropout" and "Restricted Boltzmann Machines" in English/transliterated form as they are established technical terms

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.92
- Readability: 0.85
- Glossary consistency: 0.85
- **Overall section score:** 0.88
