---
# Learning Transferable Visual Models From Natural Language Supervision
## تعلم نماذج بصرية قابلة للنقل من الإشراف باللغة الطبيعية

**arXiv ID:** 2103.00020
**Authors:** Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, Ilya Sutskever
**Year:** 2021
**Categories:** cs.CV (Computer Vision and Pattern Recognition), cs.LG (Machine Learning)
**Translation Quality:** 0.96
**Glossary Terms Used:** computer vision, state-of-the-art, training, pretraining, dataset, natural language, downstream task, performance, benchmark, accuracy, baseline, pretrained, representation, supervised learning, caption, zero-shot transfer, geo-localization, fine-grained, labeled data, scalable, raw text, image-text pair, visual concept, transfer

### English Abstract
State-of-the-art computer vision systems are trained to predict a fixed set of predetermined object categories. This restricted form of supervision limits their generality and usability since additional labeled data is needed to specify any other visual concept. Learning directly from raw text about images is a promising alternative which leverages a much broader source of supervision. We demonstrate that the simple pre-training task of predicting which caption goes with which image is an efficient and scalable way to learn SOTA image representations from scratch on a dataset of 400 million (image, text) pairs collected from the internet. After pre-training, natural language is used to reference learned visual concepts (or describe new ones) enabling zero-shot transfer of the model to downstream tasks. We study the performance of this approach by benchmarking on over 30 different existing computer vision datasets, spanning tasks such as OCR, action recognition in videos, geo-localization, and many types of fine-grained object classification. The model transfers non-trivially to most tasks and is often competitive with a fully supervised baseline without the need for any dataset specific training. For instance, we match the accuracy of the original ResNet-50 on ImageNet zero-shot without needing to use any of the 1.28 million training examples it was trained on. We release our code and pre-trained model weights at https://github.com/OpenAI/CLIP.

### الملخص العربي
تُدرَّب أنظمة الرؤية الحاسوبية المتقدمة للتنبؤ بمجموعة ثابتة من فئات الأجسام المحددة مسبقاً. يحد هذا الشكل المقيد من الإشراف من عموميتها وقابلية استخدامها حيث تكون هناك حاجة إلى بيانات موسومة إضافية لتحديد أي مفهوم بصري آخر. يُعد التعلم مباشرة من النص الخام حول الصور بديلاً واعداً يستفيد من مصدر إشراف أوسع بكثير. نُظهر أن مهمة التدريب المسبق البسيطة المتمثلة في التنبؤ بأي تسمية نصية تتطابق مع أي صورة هي طريقة فعالة وقابلة للتوسع لتعلم تمثيلات صور متقدمة من الصفر على مجموعة بيانات تحتوي على 400 مليون زوج (صورة، نص) مجمعة من الإنترنت. بعد التدريب المسبق، تُستخدم اللغة الطبيعية للإشارة إلى المفاهيم البصرية المتعلمة (أو وصف مفاهيم جديدة) مما يمكّن النقل بدون أمثلة للنموذج إلى المهام النهائية. ندرس أداء هذا النهج من خلال قياس الأداء على أكثر من 30 مجموعة بيانات مختلفة موجودة للرؤية الحاسوبية، تغطي مهام مثل التعرف الضوئي على الحروف، والتعرف على الأفعال في مقاطع الفيديو، والتوطين الجغرافي، والعديد من أنواع التصنيف الدقيق للأجسام. ينتقل النموذج بشكل ملموس إلى معظم المهام وغالباً ما يكون منافساً لخط الأساس الموجه بالكامل دون الحاجة إلى أي تدريب محدد لمجموعة البيانات. على سبيل المثال، نطابق دقة ResNet-50 الأصلي على ImageNet بدون أمثلة دون الحاجة إلى استخدام أي من 1.28 مليون مثال تدريبي التي تم تدريبه عليها. ننشر شفرتنا البرمجية وأوزان النموذج المدرب مسبقاً.

### Back-Translation (Validation)
State-of-the-art computer vision systems are trained to predict a fixed set of predetermined object categories. This restricted form of supervision limits their generality and usability as additional labeled data is needed to specify any other visual concept. Learning directly from raw text about images is a promising alternative that leverages a much broader source of supervision. We show that the simple pre-training task of predicting which text caption matches which image is an efficient and scalable method to learn state-of-the-art image representations from scratch on a dataset containing 400 million (image, text) pairs collected from the internet. After pre-training, natural language is used to reference learned visual concepts (or describe new ones) enabling zero-shot transfer of the model to downstream tasks. We study the performance of this approach by benchmarking performance on over 30 different existing computer vision datasets, covering tasks such as optical character recognition, action recognition in videos, geographic localization, and many types of fine-grained object classification. The model transfers substantially to most tasks and is often competitive with a fully supervised baseline without the need for any dataset-specific training. For example, we match the accuracy of the original ResNet-50 on ImageNet zero-shot without needing to use any of the 1.28 million training examples it was trained on. We release our code and pre-trained model weights.

### Translation Metrics
- Iterations: 3
- Final Score: 0.96
- Quality: High
- Semantic Equivalence: 0.97
- Technical Accuracy: 0.98
- Completeness: 1.0
- Coherence: 0.95
- Glossary Consistency: 0.98

### Notes
This translation represents the seminal CLIP (Contrastive Language-Image Pre-training) paper from OpenAI, which introduced a revolutionary approach to learning visual representations through natural language supervision. The model's ability to perform zero-shot transfer to various computer vision tasks without task-specific training has had significant impact on the field of multimodal AI.

Key technical terms translated:
- Zero-shot transfer: النقل بدون أمثلة
- Visual concept: مفهوم بصري
- Caption: تسمية نصية
- Geo-localization: التوطين الجغرافي
- Fine-grained classification: التصنيف الدقيق

---
