# Section 4: Experiments
## القسم 4: التجارب

**Section:** experiments
**Translation Quality:** 0.87
**Glossary Terms Used:** segmentation, benchmark, training, annotation, data augmentation, accuracy, IoU (Intersection over Union), GPU

---

### English Version

We demonstrate the application of the u-net to three different segmentation tasks. The first task is the segmentation of neuronal structures in electron microscopic recordings. An example of the data set and our obtained segmentation is displayed in Figure 2. We provide the full result as Supplementary Material. The data set is provided by the EM segmentation challenge [14] that was started at ISBI 2012 and is still open for new contributions. The training data is a set of 30 images (512x512 pixels) from serial section transmission electron microscopy of the Drosophila first instar larva ventral nerve cord (VNC). Each image comes with a corresponding fully annotated ground truth segmentation map for cells (white) and membranes (black). The test set is publicly available, but its segmentation maps are kept secret. An evaluation can be obtained by sending the predicted membrane probability map to the organizers. The evaluation is done by thresholding the map at 10 different levels and computation of the "warping error", the "Rand error" and the "pixel error" [14].

Our network (average over 7 rotated versions of the input data) achieves without any further pre- or postprocessing a warping error of 0.0003529 (the new best score, see Table 1) and a rand-error of 0.0382.

This is significantly better than the sliding-window convolutional network result by Ciresan et al. [2], whose best submission had a warping error of 0.000420 and a rand error of 0.0504. In terms of rand error the only better performing algorithms on this data set use highly data set specific post-processing methods applied to the probability map of Ciresan et al. [2].

We also applied the u-net to a cell segmentation task in light microscopic images. This segmenation task is part of the ISBI cell tracking challenge 2014 and 2015 [11,13]. The first data set "PhC-U373"1 contains Glioblastoma-astrocytoma U373 cells on a polyacrylamide substrate recorded by phase contrast microscopy (see Figure 4a,b and Supp. Material). It contains 35 partially annotated training images. Here we achieve an average IOU ("intersection over union") of 92%, which is significantly better than the second best algorithm with 83% (see Table 2). The second data set "DIC-HeLa"2 are HeLa cells on a flat glass recorded by differential interference contrast (DIC) microscopy (see Supp. Material). It contains 20 partially annotated training images. Here we achieve an average IOU of 77.5% which is significantly better than the second best algorithm with 46%.

---

### النسخة العربية

نُظهر تطبيق شبكة U-Net على ثلاث مهام تجزئة مختلفة. المهمة الأولى هي تجزئة البنى العصبية في تسجيلات المجهر الإلكتروني. يتم عرض مثال على مجموعة البيانات والتجزئة التي حصلنا عليها في الشكل 2. نقدم النتيجة الكاملة كمواد تكميلية. يتم توفير مجموعة البيانات بواسطة تحدي تجزئة المجهر الإلكتروني [14] الذي بدأ في ISBI 2012 ولا يزال مفتوحاً للمساهمات الجديدة. بيانات التدريب هي مجموعة من 30 صورة (512×512 بكسل) من المجهر الإلكتروني النافذ للمقطع المتسلسل للحبل العصبي البطني (VNC) ليرقة Drosophila من الطور الأول. تأتي كل صورة مع خريطة تجزئة حقيقة أرضية موسومة بالكامل مقابلة للخلايا (أبيض) والأغشية (أسود). مجموعة الاختبار متاحة للجمهور، لكن خرائط التجزئة الخاصة بها يتم الاحتفاظ بها سرية. يمكن الحصول على تقييم عن طريق إرسال خريطة احتمالية الغشاء المتوقعة إلى المنظمين. يتم التقييم عن طريق عتبة الخريطة عند 10 مستويات مختلفة وحساب "خطأ الالتواء" و"خطأ راند" و"خطأ البكسل" [14].

تحقق شبكتنا (متوسط 7 إصدارات مدورة من بيانات المدخل) دون أي معالجة مسبقة أو لاحقة إضافية خطأ التواء قدره 0.0003529 (أفضل نتيجة جديدة، انظر الجدول 1) وخطأ راند قدره 0.0382.

هذا أفضل بكثير من نتيجة الشبكة الالتفافية بنافذة منزلقة من Ciresan وآخرون [2]، الذين كان لديهم أفضل تقديم بخطأ التواء قدره 0.000420 وخطأ راند قدره 0.0504. من حيث خطأ راند، الخوارزميات الوحيدة الأفضل أداءً على مجموعة البيانات هذه تستخدم طرق معالجة لاحقة خاصة بمجموعة البيانات للغاية مطبقة على خريطة الاحتمالية من Ciresan وآخرون [2].

طبقنا أيضاً شبكة U-Net على مهمة تجزئة الخلايا في صور المجهر الضوئي. هذه مهمة التجزئة جزء من تحدي تتبع الخلايا ISBI 2014 و 2015 [11,13]. مجموعة البيانات الأولى "PhC-U373" تحتوي على خلايا Glioblastoma-astrocytoma U373 على ركيزة بولي أكريلاميد مسجلة بواسطة مجهر التباين الطوري (انظر الشكل 4a,b والمواد التكميلية). تحتوي على 35 صورة تدريب موسومة جزئياً. هنا نحقق متوسط IOU ("التقاطع على الاتحاد") بنسبة 92٪، وهو أفضل بكثير من ثاني أفضل خوارزمية بنسبة 83٪ (انظر الجدول 2). مجموعة البيانات الثانية "DIC-HeLa" هي خلايا HeLa على زجاج مسطح مسجلة بواسطة مجهر التباين التفاضلي (DIC) (انظر المواد التكميلية). تحتوي على 20 صورة تدريب موسومة جزئياً. هنا نحقق متوسط IOU بنسبة 77.5٪ وهو أفضل بكثير من ثاني أفضل خوارزمية بنسبة 46٪.

---

### Translation Notes

- **Figures referenced:** Figure 2, Figure 4a, Figure 4b
- **Key terms introduced:** warping error, Rand error, pixel error, IOU (Intersection over Union), phase contrast microscopy, differential interference contrast microscopy, ground truth segmentation
- **Equations:** None, but numerical results and error metrics
- **Citations:** [2], [11], [13], [14]
- **Special handling:**
  - Dataset names preserved: PhC-U373, DIC-HeLa, Drosophila, VNC
  - Specific numerical results preserved: 0.0003529, 0.0382, 92%, 83%, 77.5%, 46%
  - Technical biological terms: Glioblastoma-astrocytoma, HeLa cells, polyacrylamide substrate

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
