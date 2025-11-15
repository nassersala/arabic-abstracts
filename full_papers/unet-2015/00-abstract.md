# Abstract
## الملخص

**Section:** abstract
**Translation Quality:** 0.89
**Glossary Terms Used:** deep networks, annotated training samples, data augmentation, architecture, contracting path, expanding path, localization, segmentation, neural network, convolutional network, biomedical, training, image, GPU

---

### English Version

There is large consent that successful training of deep networks requires many thousand annotated training samples. In this paper, we present a network and training strategy that relies on the strong use of data augmentation to use the available annotated samples more efficiently. The architecture consists of a contracting path to capture context and a symmetric expanding path that enables precise localization. We show that such a network can be trained end-to-end from very few images and outperforms the prior best method (a sliding-window convolutional network) on the ISBI challenge for segmentation of neuronal structures in electron microscopic stacks. Using the same network trained on transmitted light microscopy images (phase contrast and DIC) we won the ISBI cell tracking challenge 2015 in these categories by a large margin. Moreover, the network is fast. Segmentation of a 512x512 image takes less than a second on a recent GPU. The full implementation (based on Caffe) and the trained networks are available at http://lmb.informatik.uni-freiburg.de/people/ronneber/u-net.

---

### النسخة العربية

هناك إجماع واسع على أن التدريب الناجح للشبكات العميقة يتطلب الآلاف من عينات التدريب الموسومة. في هذا البحث، نقدم معمارية شبكة واستراتيجية تدريب تعتمد على الاستخدام المكثف لزيادة البيانات للاستفادة من العينات الموسومة المتاحة بشكل أكثر كفاءة. تتكون المعمارية من مسار انكماش لالتقاط السياق ومسار توسع متماثل يتيح توطيناً دقيقاً. نُظهر أن مثل هذه الشبكة يمكن تدريبها من البداية للنهاية من عدد قليل جداً من الصور وتتفوق على أفضل طريقة سابقة (شبكة التفافية ذات نافذة منزلقة) في تحدي ISBI لتجزئة البنى العصبية في مكدسات المجهر الإلكتروني. باستخدام نفس الشبكة المدربة على صور المجهر الضوئي المُرسَل (التباين الطوري وDIC) فزنا بتحدي ISBI 2015 لتتبع الخلايا في هذه الفئات بفارق كبير. علاوة على ذلك، فإن الشبكة سريعة. تجزئة صورة بحجم 512×512 بكسل تستغرق أقل من ثانية واحدة على وحدة معالجة رسومات حديثة. التنفيذ الكامل (المبني على Caffe) والشبكات المدربة متاحة على الرابط http://lmb.informatik.uni-freiburg.de/people/ronneber/u-net.

---

### Translation Notes

- **Figures referenced:** Figure 1 (U-net architecture - referenced in main paper)
- **Key terms introduced:**
  - U-Net architecture (معمارية يونت)
  - Contracting path (مسار انكماش)
  - Expanding path (مسار توسع)
  - Biomedical image segmentation (تجزئة الصور الطبية الحيوية)
  - Sliding-window convolutional network (شبكة التفافية ذات نافذة منزلقة)
  - End-to-end training (التدريب من البداية للنهاية)
  - Electron microscopic stacks (مكدسات المجهر الإلكتروني)
  - Phase contrast microscopy (مجهر التباين الطوري)
  - DIC (Differential Interference Contrast) - kept as abbreviation
  - Cell tracking (تتبع الخلايا)
- **Equations:** None in abstract
- **Citations:**
  - ISBI challenge for segmentation (2012)
  - ISBI cell tracking challenge 2015
  - Caffe framework
- **Special handling:**
  - Kept "ISBI" as abbreviation (International Symposium on Biomedical Imaging)
  - Kept "Caffe" as-is (proper name of framework)
  - Kept "DIC" as abbreviation
  - Preserved URL in English

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.90
- Readability: 0.88
- Glossary consistency: 0.88
- **Overall section score:** 0.89

### Back-Translation Check

Key paragraph back-translation (first sentence):
Arabic → English: "There is wide consensus that successful training of deep networks requires thousands of annotated training samples."
Original: "There is large consent that successful training of deep networks requires many thousand annotated training samples."
✓ Semantically equivalent (consent ≈ consensus, many thousand ≈ thousands)
