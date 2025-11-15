# Abstract
## الملخص

**Section:** Abstract
**Translation Quality:** 0.92
**Glossary Terms Used:** embedding (التضمين), face recognition (التعرف على الوجوه), Euclidean space (الفضاء الإقليدي), convolutional neural network (الشبكة العصبية الالتفافية), accuracy (دقة), deep learning (تعلم عميق)

---

### English Version

Despite significant recent advances in the field of face recognition, implementing face verification and recognition efficiently at scale presents serious challenges to current approaches. In this paper we present a system, called FaceNet, that directly learns a mapping from face images to a compact Euclidean space where distances directly correspond to a measure of face similarity. Once this space has been produced, tasks such as face recognition, verification and clustering can be easily implemented using standard techniques with FaceNet embeddings as feature vectors.

Our method uses a deep convolutional network trained to directly optimize the embedding itself, rather than an intermediate bottleneck layer as in previous deep learning approaches. To train, we use triplets of roughly aligned matching / non-matching face patches generated using a novel online triplet mining method. The benefit of our approach is much greater representational efficiency: we achieve state-of-the-art face recognition performance using only 128-bytes per face.

On the widely used Labeled Faces in the Wild (LFW) dataset, our system achieves a new record accuracy of 99.63%. On YouTube Faces DB it achieves 95.12%. Our system cuts the error of the current best result by 30% on both datasets.

---

### النسخة العربية

على الرغم من التقدم الكبير الأخير في مجال التعرف على الوجوه، فإن تنفيذ التحقق من الوجوه والتعرف عليها بكفاءة على نطاق واسع يمثل تحديات جادة للأساليب الحالية. في هذا البحث، نقدم نظاماً يسمى فيس نت (FaceNet)، يتعلم مباشرة تعييناً من صور الوجوه إلى فضاء إقليدي مدمج حيث تتوافق المسافات بشكل مباشر مع قياس تشابه الوجوه. بمجرد إنتاج هذا الفضاء، يمكن تنفيذ مهام مثل التعرف على الوجوه والتحقق منها وتجميعها بسهولة باستخدام تقنيات قياسية مع تضمينات فيس نت كمتجهات ميزات.

تستخدم طريقتنا شبكة عصبية التفافية عميقة مدربة لتحسين التضمين نفسه مباشرة، بدلاً من طبقة اختناق وسيطة كما في أساليب التعلم العميق السابقة. للتدريب، نستخدم ثلاثيات من رقع الوجوه المتطابقة / غير المتطابقة المحاذاة تقريباً والتي تم توليدها باستخدام طريقة جديدة للتعدين الثلاثي على الإنترنت. فائدة نهجنا هي كفاءة تمثيلية أكبر بكثير: نحقق أداءً متطوراً في التعرف على الوجوه باستخدام 128 بايت فقط لكل وجه.

في مجموعة بيانات الوجوه الموسومة في البرية (Labeled Faces in the Wild - LFW) المستخدمة على نطاق واسع، يحقق نظامنا دقة قياسية جديدة تبلغ 99.63%. في قاعدة بيانات يوتيوب للوجوه (YouTube Faces DB) يحقق 95.12%. يخفض نظامنا خطأ أفضل نتيجة حالية بنسبة 30% على كلتا مجموعتي البيانات.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:**
  - FaceNet (kept as فيس نت in Arabic)
  - Euclidean space (الفضاء الإقليدي)
  - embeddings (التضمينات)
  - triplet mining (التعدين الثلاثي)
  - face verification (التحقق من الوجوه)
  - face recognition (التعرف على الوجوه)
- **Equations:** None
- **Citations:** None
- **Special handling:** Dataset names (LFW, YouTube Faces DB) kept in English with Arabic explanation in parentheses

### Quality Metrics

- Semantic equivalence: 0.93
- Technical accuracy: 0.95
- Readability: 0.90
- Glossary consistency: 0.90
- **Overall section score:** 0.92
