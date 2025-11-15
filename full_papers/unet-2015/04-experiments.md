# Section 4: Experiments
## القسم 4: التجارب

**Section:** experiments
**Translation Quality:** 0.87
**Glossary Terms Used:** segmentation, neuronal structures, electron microscopic, training images, ground truth, biomedical, cell tracking, phase contrast microscopy, DIC, test set, evaluation, membrane, warping error, Rand error, pixel error, IOU (intersection over union)

---

### English Version

We demonstrate the application of the u-net to three different segmentation tasks. The first task is the segmentation of neuronal structures in electron microscopic recordings. An example of the data set and our obtained segmentation is displayed in Figure 2. We provide the full result as Supplementary Material. The data set is provided by the EM segmentation challenge [em-segmentation-webpage] that was started at ISBI 2012 and is still open for new contributions. The training data is a set of 30 images (512x512 pixels) from serial section transmission electron microscopy of the Drosophila first instar larva ventral nerve cord (VNC). Each image comes with a corresponding fully annotated ground truth segmentation map for cells (white) and membranes (black). The test set is publicly available, but its segmentation maps are kept secret. An evaluation can be obtained by sending the predicted membrane probability map to the organizers. The evaluation is done by thresholding the map at 10 different levels and computation of the "warping error", the "Rand error" and the "pixel error" [em-segmentation-webpage].

The u-net (averaged over 7 rotated versions of the input data) achieves without any further pre- or postprocessing a warping error of 0.0003529 (the new best score, see Table 1) and a rand-error of 0.0382.

**Table 1: Ranking on the EM segmentation challenge [em-segmentation-webpage] (march 6th, 2015), sorted by warping error.**

| Rank | Group name | Warping Error | Rand Error | Pixel Error |
|------|------------|---------------|------------|-------------|
| | ** human values ** | 0.000005 | 0.0021 | 0.0010 |
| 1. | u-net | **0.000353** | 0.0382 | 0.0611 |
| 2. | DIVE-SCI | 0.000355 | 0.0305 | 0.0584 |
| 3. | IDSIA [schmidhuber12deepneural] | 0.000420 | 0.0504 | 0.0613 |
| 4. | DIVE | 0.000430 | 0.0545 | **0.0582** |
| ⋮ | | | | |
| 10. | IDSIA-SCI | 0.000653 | **0.0189** | 0.1027 |

This is significantly better than the sliding-window convolutional network result by Ciresan et al. [schmidhuber12deepneural], whose best submission had a warping error of 0.000420 and a rand error of 0.0504. In terms of rand error the only better performing algorithms on this data set use highly data set specific post-processing methods applied to the probability map of Ciresan et al. [schmidhuber12deepneural].

We also applied the u-net to a cell segmentation task in light microscopic images. This segmentation task is part of the ISBI cell tracking challenge 2014 and 2015 [Maska2014, cell-tracking-webpage]. The first data set "PhC-U373" contains Glioblastoma-astrocytoma U373 cells on a polyacrylimide substrate recorded by phase contrast microscopy (see Figure 4a,b and Supp. Material). It contains 35 partially annotated training images. Here we achieve an average IOU ("intersection over union") of 92%, which is significantly better than the second best algorithm with 83% (see Table 2).

**Table 2: Segmentation results (IOU) on the ISBI cell tracking challenge 2015.**

| Name | PhC-U373 | DIC-HeLa |
|------|----------|----------|
| IMCB-SG (2014) | 0.2669 | 0.2935 |
| KTH-SE (2014) | 0.7953 | 0.4607 |
| HOUS-US (2014) | 0.5323 | - |
| second-best 2015 | 0.83 | 0.46 |
| u-net (2015) | **0.9203** | **0.7756** |

The second data set "DIC-HeLa" are HeLa cells on a flat glass recorded by differential interference contrast (DIC) microscopy (see Figure 3, Figure 4c,d and Supp. Material). It contains 20 partially annotated training images. Here we achieve an average IOU of 77.5% which is significantly better than the second best algorithm with 46%.

---

### النسخة العربية

نُظهر تطبيق يونت على ثلاث مهام تجزئة مختلفة. المهمة الأولى هي تجزئة البنى العصبية في التسجيلات المجهرية الإلكترونية. يُعرض مثال على مجموعة البيانات والتجزئة التي حصلنا عليها في الشكل 2. نقدم النتيجة الكاملة كمادة تكميلية. يتم توفير مجموعة البيانات من قبل تحدي تجزئة المجهر الإلكتروني [em-segmentation-webpage] الذي بدأ في ISBI 2012 ولا يزال مفتوحاً لمساهمات جديدة. بيانات التدريب هي مجموعة من 30 صورة (512×512 بكسل) من المجهر الإلكتروني النافذ للمقاطع المتسلسلة للحبل العصبي البطني (VNC) ليرقة ذبابة الفاكهة في الطور الأول. تأتي كل صورة مع خريطة تجزئة حقيقة أرضية موسومة بالكامل للخلايا (أبيض) والأغشية (أسود). مجموعة الاختبار متاحة للجمهور، لكن خرائط التجزئة الخاصة بها تُحفظ سرية. يمكن الحصول على تقييم عن طريق إرسال خريطة احتمالية الغشاء المتنبأ بها إلى المنظمين. يتم التقييم عن طريق تعتيب الخريطة عند 10 مستويات مختلفة وحساب "خطأ الالتواء"، و"خطأ راند" و"خطأ البكسل" [em-segmentation-webpage].

يحقق يونت (متوسط على 7 إصدارات مدورة من بيانات المدخل) بدون أي معالجة مسبقة أو لاحقة إضافية خطأ التواء قدره 0.0003529 (أفضل درجة جديدة، انظر الجدول 1) وخطأ راند قدره 0.0382.

**الجدول 1: الترتيب في تحدي تجزئة المجهر الإلكتروني [em-segmentation-webpage] (6 مارس 2015)، مرتب حسب خطأ الالتواء.**

| الترتيب | اسم المجموعة | خطأ الالتواء | خطأ راند | خطأ البكسل |
|---------|--------------|--------------|----------|-----------|
| | ** قيم بشرية ** | 0.000005 | 0.0021 | 0.0010 |
| 1. | u-net | **0.000353** | 0.0382 | 0.0611 |
| 2. | DIVE-SCI | 0.000355 | 0.0305 | 0.0584 |
| 3. | IDSIA [schmidhuber12deepneural] | 0.000420 | 0.0504 | 0.0613 |
| 4. | DIVE | 0.000430 | 0.0545 | **0.0582** |
| ⋮ | | | | |
| 10. | IDSIA-SCI | 0.000653 | **0.0189** | 0.1027 |

هذا أفضل بكثير من نتيجة الشبكة الالتفافية ذات النافذة المنزلقة من قبل Ciresan وزملائه [schmidhuber12deepneural]، التي كان لأفضل تقديم لها خطأ التواء قدره 0.000420 وخطأ راند قدره 0.0504. من حيث خطأ راند، فإن الخوارزميات الوحيدة ذات الأداء الأفضل على مجموعة البيانات هذه تستخدم طرق معالجة لاحقة خاصة جداً بمجموعة البيانات مطبقة على خريطة الاحتمالية من Ciresan وزملائه [schmidhuber12deepneural].

قمنا أيضاً بتطبيق يونت على مهمة تجزئة الخلايا في صور المجهر الضوئي. هذه مهمة التجزئة هي جزء من تحدي تتبع الخلايا ISBI 2014 و2015 [Maska2014, cell-tracking-webpage]. تحتوي مجموعة البيانات الأولى "PhC-U373" على خلايا ورم أرومي دبقي-نجمي U373 على ركيزة بولي أكريلاميد مسجلة بواسطة مجهر التباين الطوري (انظر الشكل 4a,b والمادة التكميلية). تحتوي على 35 صورة تدريب موسومة جزئياً. هنا نحقق متوسط IOU ("التقاطع على الاتحاد") بنسبة 92٪، وهو أفضل بكثير من ثاني أفضل خوارزمية بنسبة 83٪ (انظر الجدول 2).

**الجدول 2: نتائج التجزئة (IOU) في تحدي تتبع الخلايا ISBI 2015.**

| الاسم | PhC-U373 | DIC-HeLa |
|------|----------|----------|
| IMCB-SG (2014) | 0.2669 | 0.2935 |
| KTH-SE (2014) | 0.7953 | 0.4607 |
| HOUS-US (2014) | 0.5323 | - |
| second-best 2015 | 0.83 | 0.46 |
| u-net (2015) | **0.9203** | **0.7756** |

مجموعة البيانات الثانية "DIC-HeLa" هي خلايا HeLa على زجاج مسطح مسجلة بواسطة مجهر التباين التداخلي التفاضلي (DIC) (انظر الشكل 3، والشكل 4c,d والمادة التكميلية). تحتوي على 20 صورة تدريب موسومة جزئياً. هنا نحقق متوسط IOU بنسبة 77.5٪ وهو أفضل بكثير من ثاني أفضل خوارزمية بنسبة 46٪.

---

### Translation Notes

- **Figures referenced:**
  - Figure 2: Overlap-tile strategy example (EM segmentation)
  - Figure 3: HeLa cells ground truth
  - Figure 4a,b: PhC-U373 segmentation results
  - Figure 4c,d: DIC-HeLa segmentation results
- **Tables included:**
  - Table 1: EM segmentation challenge rankings (6 entries shown)
  - Table 2: ISBI cell tracking challenge results (5 entries)
- **Key terms introduced:**
  - Electron microscopic recordings (التسجيلات المجهرية الإلكترونية)
  - Serial section transmission electron microscopy (المجهر الإلكتروني النافذ للمقاطع المتسلسلة)
  - Drosophila (ذبابة الفاكهة)
  - Ventral nerve cord (VNC) (الحبل العصبي البطني)
  - Warping error (خطأ الالتواء)
  - Rand error (خطأ راند)
  - Pixel error (خطأ البكسل)
  - Thresholding (تعتيب)
  - Phase contrast microscopy (مجهر التباين الطوري)
  - Differential interference contrast (DIC) (التباين التداخلي التفاضلي)
  - Glioblastoma-astrocytoma (ورم أرومي دبقي-نجمي)
  - Polyacrylimide substrate (ركيزة بولي أكريلاميد)
  - Intersection over union (IOU) (التقاطع على الاتحاد)
  - HeLa cells (خلايا HeLa - kept as proper name)
- **Equations:** None in this section
- **Citations:** Multiple references
  - [em-segmentation-webpage]
  - [schmidhuber12deepneural]
  - [Maska2014, cell-tracking-webpage]
- **Special handling:**
  - Preserved all numerical results exactly
  - Kept dataset names in English (PhC-U373, DIC-HeLa)
  - Kept team/group names in English (DIVE-SCI, IDSIA, etc.)
  - Kept "IOU" as abbreviation with Arabic translation
  - Preserved table structures with Arabic headers
  - Used bold for best results as in original
  - Footnote references preserved

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.86
- **Overall section score:** 0.87

### Back-Translation Check

First paragraph back-translation:
Arabic → English: "We demonstrate the application of U-net to three different segmentation tasks. The first task is segmentation of neuronal structures in electron microscopic recordings. An example of the dataset and the segmentation we obtained is shown in Figure 2. We provide the complete result as supplementary material."
Original: "We demonstrate the application of the u-net to three different segmentation tasks. The first task is the segmentation of neuronal structures in electron microscopic recordings. An example of the data set and our obtained segmentation is displayed in Figure 2. We provide the full result as Supplementary Material."
✓ Semantically equivalent

Results description back-translation:
Arabic → English: "U-net (averaged over 7 rotated versions of the input data) achieves without any additional pre- or post-processing a warping error of 0.0003529 (new best score, see Table 1) and a Rand error of 0.0382."
✓ Semantically equivalent with exact numerical preservation
