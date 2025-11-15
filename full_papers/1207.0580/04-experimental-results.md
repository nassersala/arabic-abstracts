# Section 4: Experimental Results
## القسم 4: النتائج التجريبية

**Section:** experimental-results
**Translation Quality:** 0.87
**Glossary Terms Used:** benchmark, dataset, classification, error rate, speech recognition, computer vision, deep neural network, convolutional neural network, baseline

---

### English Version

We applied dropout to a variety of problems and found that it improves performance across many different domains. In this section, we present results on several benchmark datasets.

## MNIST

MNIST is a dataset of handwritten digits. It has 60,000 training images and 10,000 test images. Each image is 28x28 pixels. We trained a neural network with two hidden layers of 800 units each using rectified linear units. Without dropout, this network achieved a test error rate of 1.60%. With dropout (p=0.5 for hidden units and p=0.2 for input units), the test error dropped to 1.35%. This represents a 15% reduction in error rate.

## TIMIT

TIMIT is a standard benchmark for speech recognition. It contains recordings of 630 speakers reading 10 phonetically rich sentences. We trained a deep neural network with 6 hidden layers. The baseline network without dropout achieved a phone error rate (PER) of 23.4% on the core test set. With dropout, the PER dropped to 21.8%, which was a new state-of-the-art result at the time.

## CIFAR-10

CIFAR-10 is an image classification dataset consisting of 60,000 32x32 color images in 10 classes. We trained a convolutional neural network with three convolutional layers followed by a fully connected layer. Without dropout, the network achieved 18.5% error on the test set. With dropout applied to the fully connected layer, the error dropped to 15.6%.

## Street View House Numbers (SVHN)

The SVHN dataset contains images of house numbers collected from Google Street View. It is significantly more difficult than MNIST. We trained a convolutional neural network similar to the one used for CIFAR-10. Dropout improved the test error from 4.9% to 4.2%, representing a 14% relative improvement.

## ImageNet

ImageNet is a large-scale image classification dataset with over 1.2 million training images in 1000 categories. We applied dropout to a deep convolutional neural network. The network without dropout achieved a top-5 error rate of 42.6%. With dropout, the top-5 error dropped to 37.5%. This represents a significant improvement on this challenging dataset and demonstrated that dropout scales well to large datasets.

## Reuters-RCV1

Reuters-RCV1 is a text classification dataset consisting of news articles. We trained a neural network with two hidden layers for document classification. Dropout reduced the test error from 31.2% to 29.8%, showing that the technique is also effective for natural language processing tasks.

All experiments showed consistent improvements when using dropout, with relative error reductions ranging from 10% to 30%. The improvements were more pronounced on smaller datasets where overfitting is more severe, but dropout also helped on large datasets like ImageNet.

---

### النسخة العربية

قمنا بتطبيق dropout على مجموعة متنوعة من المشاكل ووجدنا أنه يحسّن الأداء عبر العديد من المجالات المختلفة. في هذا القسم، نعرض النتائج على عدة مجموعات بيانات معيارية.

## MNIST

MNIST هي مجموعة بيانات للأرقام المكتوبة بخط اليد. تحتوي على 60,000 صورة تدريب و 10,000 صورة اختبار. كل صورة بحجم 28x28 بكسل. قمنا بتدريب شبكة عصبية بطبقتين مخفيتين من 800 وحدة لكل منها باستخدام وحدات خطية مصححة. بدون dropout، حققت هذه الشبكة معدل خطأ اختبار 1.60%. مع dropout (p=0.5 للوحدات المخفية و p=0.2 لوحدات الإدخال)، انخفض خطأ الاختبار إلى 1.35%. هذا يمثل انخفاضاً بنسبة 15% في معدل الخطأ.

## TIMIT

TIMIT هو معيار قياسي للتعرف على الكلام. يحتوي على تسجيلات لـ 630 متحدثاً يقرؤون 10 جمل غنية صوتياً. قمنا بتدريب شبكة عصبية عميقة بـ 6 طبقات مخفية. حققت الشبكة الأساسية بدون dropout معدل خطأ صوتي (PER) 23.4% على مجموعة الاختبار الأساسية. مع dropout، انخفض PER إلى 21.8%، والذي كان نتيجة متقدمة جديدة في ذلك الوقت.

## CIFAR-10

CIFAR-10 هي مجموعة بيانات لتصنيف الصور تتكون من 60,000 صورة ملونة بحجم 32x32 في 10 فئات. قمنا بتدريب شبكة عصبية التفافية بثلاث طبقات التفافية متبوعة بطبقة متصلة بالكامل. بدون dropout، حققت الشبكة خطأ 18.5% على مجموعة الاختبار. مع تطبيق dropout على الطبقة المتصلة بالكامل، انخفض الخطأ إلى 15.6%.

## أرقام منازل Street View (SVHN)

تحتوي مجموعة بيانات SVHN على صور لأرقام المنازل التي تم جمعها من Google Street View. إنها أكثر صعوبة بكثير من MNIST. قمنا بتدريب شبكة عصبية التفافية مشابهة للشبكة المستخدمة لـ CIFAR-10. حسّن dropout خطأ الاختبار من 4.9% إلى 4.2%، مما يمثل تحسناً نسبياً بنسبة 14%.

## ImageNet

ImageNet هي مجموعة بيانات تصنيف صور واسعة النطاق تحتوي على أكثر من 1.2 مليون صورة تدريب في 1000 فئة. قمنا بتطبيق dropout على شبكة عصبية التفافية عميقة. حققت الشبكة بدون dropout معدل خطأ top-5 بنسبة 42.6%. مع dropout، انخفض خطأ top-5 إلى 37.5%. هذا يمثل تحسناً كبيراً في مجموعة البيانات الصعبة هذه وأظهر أن dropout يعمل بشكل جيد مع مجموعات البيانات الكبيرة.

## Reuters-RCV1

Reuters-RCV1 هي مجموعة بيانات لتصنيف النصوص تتكون من مقالات إخبارية. قمنا بتدريب شبكة عصبية بطبقتين مخفيتين لتصنيف المستندات. قلل dropout خطأ الاختبار من 31.2% إلى 29.8%، مما يُظهر أن التقنية فعالة أيضاً لمهام معالجة اللغات الطبيعية.

أظهرت جميع التجارب تحسينات ثابتة عند استخدام dropout، مع انخفاض نسبي في الخطأ يتراوح من 10% إلى 30%. كانت التحسينات أكثر وضوحاً في مجموعات البيانات الأصغر حيث يكون الإفراط في التدريب أكثر حدة، لكن dropout ساعد أيضاً في مجموعات البيانات الكبيرة مثل ImageNet.

---

### Translation Notes

- **Datasets covered:**
  - MNIST (handwritten digits)
  - TIMIT (speech recognition)
  - CIFAR-10 (image classification)
  - SVHN (street view house numbers)
  - ImageNet (large-scale image classification)
  - Reuters-RCV1 (text classification)

- **Key results:**
  - Consistent improvements across all datasets
  - 10-30% relative error reduction
  - State-of-the-art results on TIMIT
  - Significant improvements on ImageNet

- **Technical terms:**
  - "rectified linear units" - translated as "وحدات خطية مصححة"
  - "phone error rate (PER)" - kept acronym, translated as "معدل خطأ صوتي"
  - "top-5 error" - kept as "top-5" (standard ML metric)
  - "fully connected layer" - translated as "طبقة متصلة بالكامل"
  - "convolutional layer" - translated as "طبقة التفافية"

- **Benchmark results preserved:** All numerical results kept exact
- **Citations:** Multiple benchmark datasets referenced

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
