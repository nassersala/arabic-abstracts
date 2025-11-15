# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** deep learning, convolutional neural networks, architecture, computational complexity, feature map channels, accuracy, mobile devices, model efficiency

---

### English Version

Building deeper and larger convolutional neural networks (CNNs) is a primary trend for solving major visual recognition tasks [23, 13, 8, 29]. The most accurate CNNs usually have hundreds of layers and thousands of channels [9, 34, 28, 40], thus requiring computation at billions of FLOPs. This report examines the opposite extreme: pursuing the best accuracy in very limited computational budgets at tens or hundreds of MFLOPs, focusing on common mobile platforms such as drones, robots, and smartphones. Note that many existing works [16, 22, 43, 42, 7, 27] focus on pruning, compressing, or low-bit representing a "basic" network architecture. Here we aim to explore a highly efficient basic architecture specially designed for our desired computing ranges.

We notice that state-of-the-art basic architectures such as Xception [3] and ResNeXt [40] become less efficient in extremely small networks because of the costly dense 1×1 convolutions. We propose using pointwise group convolutions to reduce computation complexity of 1×1 convolutions. To overcome the side effects brought by group convolutions, we come up with a novel channel shuffle operation to help the information flowing across feature channels. Based on the two techniques, we build a highly efficient architecture called ShuffleNet. Compared with popular structures like [25, 20], for a given complexity budget, our ShuffleNet allows more feature map channels, which helps to encode more information and is especially critical to the performance of very small networks.

We evaluate our models on the challenging ImageNet classification [4, 28] and MS COCO object detection [21] tasks. A series of controlled experiments shows the effectiveness of our design principles and the superiority of our architecture. Compared with the state-of-the-art architecture MobileNet [12], our ShuffleNet achieves superior performance by a significant margin under the same computational complexity, e.g. absolute 7.8% better ImageNet top-1 error at 40 MFLOPs level.

---

### النسخة العربية

يُعد بناء شبكات عصبية التفافية (CNNs) أعمق وأكبر الاتجاه الرئيسي لحل مهام التعرف البصري الرئيسية [23, 13, 8, 29]. عادةً ما تحتوي الشبكات العصبية الالتفافية الأكثر دقة على مئات الطبقات وآلاف القنوات [9, 34, 28, 40]، وبالتالي تتطلب حسابات بمليارات من عمليات النقطة العائمة (FLOPs). يدرس هذا البحث الطرف المعاكس: السعي لتحقيق أفضل دقة ضمن ميزانيات حسابية محدودة جداً تقدر بعشرات أو مئات من ميجا عمليات النقطة العائمة (MFLOPs)، مع التركيز على المنصات المحمولة الشائعة مثل الطائرات بدون طيار والروبوتات والهواتف الذكية. تجدر الإشارة إلى أن العديد من الأعمال الموجودة [16, 22, 43, 42, 7, 27] تركز على تقليم أو ضغط أو تمثيل "الأساسية" بعدد محدود من البتات. هنا نهدف إلى استكشاف معمارية أساسية فائقة الكفاءة مصممة خصيصاً للنطاقات الحسابية المطلوبة.

نلاحظ أن المعماريات الأساسية الحديثة مثل Xception [3] و ResNeXt [40] تصبح أقل كفاءة في الشبكات الصغيرة جداً بسبب الالتفافات الكثيفة المكلفة ذات الحجم 1×1. نقترح استخدام الالتفافات النقطية المجموعية لتقليل التعقيد الحسابي للالتفافات 1×1. للتغلب على الآثار الجانبية الناتجة عن الالتفافات المجموعية، نقدم عملية خلط القنوات الجديدة للمساعدة في تدفق المعلومات عبر قنوات الميزات. بناءً على هاتين التقنيتين، نبني معمارية فائقة الكفاءة تُسمى ShuffleNet. بالمقارنة مع الهياكل الشائعة مثل [25, 20]، ولميزانية تعقيد معينة، تسمح شبكة ShuffleNet الخاصة بنا بمزيد من قنوات خرائط الميزات، مما يساعد على ترميز المزيد من المعلومات وهو أمر بالغ الأهمية بشكل خاص لأداء الشبكات الصغيرة جداً.

نقوم بتقييم نماذجنا على مهمتي تصنيف ImageNet الصعبة [4, 28] وكشف الأجسام MS COCO [21]. تُظهر سلسلة من التجارب الخاضعة للرقابة فعالية مبادئ التصميم الخاصة بنا وتفوق معماريتنا. بالمقارنة مع المعمارية الحديثة MobileNet [12]، تحقق شبكة ShuffleNet الخاصة بنا أداءً متفوقاً بهامش كبير تحت نفس التعقيد الحسابي، على سبيل المثال خطأ top-1 على ImageNet أفضل بنسبة 7.8% مطلقة عند مستوى 40 ميجا عملية فاصلة عائمة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - CNNs (الشبكات العصبية الالتفافية)
  - FLOPs (عمليات النقطة العائمة)
  - MFLOPs (ميجا عمليات النقطة العائمة)
  - Pointwise group convolutions (الالتفافات النقطية المجموعية)
  - Channel shuffle (خلط القنوات)
  - Feature map channels (قنوات خرائط الميزات)
  - Dense 1×1 convolutions (الالتفافات الكثيفة 1×1)

- **Equations:** 0
- **Citations:** Multiple references [23, 13, 8, 29, 9, 34, 28, 40, 16, 22, 43, 42, 7, 27, 3, 25, 20, 4, 21, 12]
- **Special handling:**
  - Kept architecture names in English (Xception, ResNeXt, MobileNet, ShuffleNet)
  - Translated the concept while maintaining technical precision
  - Preserved citation numbers as-is

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87

### Back-translation Check (Key Paragraph)

First paragraph Arabic translation back to English:
"Building deeper and larger CNNs is the main direction for solving major visual recognition tasks. The most accurate CNNs typically contain hundreds of layers and thousands of channels, thus requiring computations in the billions of floating point operations (FLOPs). This research examines the opposite end: seeking to achieve the best accuracy within very limited computational budgets estimated at tens or hundreds of mega floating point operations (MFLOPs)..."

✓ Semantically equivalent to original
