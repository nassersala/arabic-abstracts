# Abstract
## الملخص

**Section:** abstract
**Translation Quality:** 0.92
**Glossary Terms Used:** neural network, convolutional, training, overfitting, dropout, dataset, architecture, image classification

---

### English Version

We trained a large, deep convolutional neural network to classify the 1.2 million high-resolution images in the ImageNet LSVRC-2010 contest into the 1000 different classes. On the test data, we achieved top-1 and top-5 error rates of 37.5% and 17.0% which is considerably better than the previous state-of-the-art. The neural network, which has 60 million parameters and 650,000 neurons, consists of five convolutional layers, some of which are followed by max-pooling layers, and three fully-connected layers with a final 1000-way softmax. To make training faster, we used non-saturating neurons and a very efficient GPU implementation of the convolution operation. To reduce overfitting in the fully-connected layers we employed a recently-developed regularization method called "dropout" that proved to be very effective. We also entered a variant of this model in the ILSVRC-2012 competition and achieved a winning top-5 test error rate of 15.3%, compared to 26.2% achieved by the second-best entry.

---

### النسخة العربية

قمنا بتدريب شبكة عصبية التفافية كبيرة وعميقة لتصنيف 1.2 مليون صورة عالية الدقة في مسابقة ImageNet LSVRC-2010 إلى 1000 فئة مختلفة. على بيانات الاختبار، حققنا معدلات خطأ top-1 وtop-5 بنسبة 37.5% و17.0% وهو ما يعد أفضل بكثير من أحدث النتائج السابقة. تتكون الشبكة العصبية، التي تحتوي على 60 مليون معامل و650,000 عصبون، من خمس طبقات التفافية، بعضها متبوع بطبقات تجميع أعظمي (max-pooling)، وثلاث طبقات متصلة بالكامل مع طبقة softmax نهائية ذات 1000 مخرج. لجعل التدريب أسرع، استخدمنا عصبونات غير مشبعة (non-saturating neurons) وتطبيق GPU فعال جداً لعملية الالتفاف. لتقليل الإفراط في التدريب في الطبقات المتصلة بالكامل، استخدمنا طريقة تنظيم تم تطويرها مؤخراً تسمى "dropout" أثبتت فعاليتها الكبيرة. كما شاركنا بنسخة من هذا النموذج في مسابقة ILSVRC-2012 وحققنا معدل خطأ اختبار top-5 فائز بنسبة 15.3%، مقارنة بنسبة 26.2% التي حققها صاحب المركز الثاني.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:**
  - convolutional neural network (الشبكة العصبية الالتفافية)
  - max-pooling (تجميع أعظمي)
  - non-saturating neurons (عصبونات غير مشبعة)
  - dropout (dropout - kept as is, common practice)
  - softmax (softmax - kept as is, standard term)
  - fully-connected layers (طبقات متصلة بالكامل)
- **Equations:** None
- **Citations:** None
- **Special handling:**
  - Numerical data preserved exactly
  - Technical terms like "top-1" and "top-5" kept in English as they are standard metrics
  - ImageNet LSVRC competition names kept in English

### Quality Metrics

- Semantic equivalence: 0.93
- Technical accuracy: 0.95
- Readability: 0.90
- Glossary consistency: 0.90
- **Overall section score:** 0.92

### Back-Translation Check

Key sentence back-translated:
Arabic: "قمنا بتدريب شبكة عصبية التفافية كبيرة وعميقة لتصنيف 1.2 مليون صورة عالية الدقة..."
Back to English: "We trained a large and deep convolutional neural network to classify 1.2 million high-resolution images..."
✓ Semantic match confirmed
