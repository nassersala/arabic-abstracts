# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.91
**Glossary Terms Used:** deep networks, training, annotated, data augmentation, architecture, convolutional network, segmentation, image, GPU, implementation, biomedical

---

### English Version

There is large consent that successful training of deep networks requires many thousand annotated training samples. In this paper, we present a network and training strategy that relies on the strong use of data augmentation to use the available annotated samples more efficiently. The architecture consists of a contracting path to capture context and a symmetric expanding path that enables precise localization. We show that such a network can be trained end-to-end from very few images and outperforms the prior best method (a sliding-window convolutional network) on the ISBI challenge for segmentation of neuronal structures in electron microscopic stacks. Using the same network trained on transmitted light microscopy images (phase contrast and DIC) we won the ISBI cell tracking challenge 2015 in these categories by a large margin. Moreover, the network is fast. Segmentation of a 512x512 image takes less than a second on a recent GPU. The full implementation (based on Caffe) and the trained networks are available at http://lmb.informatik.uni-freiburg.de/people/ronneber/u-net.

---

### النسخة العربية

هناك إجماع واسع على أن التدريب الناجح للشبكات العميقة يتطلب عدة آلاف من عينات التدريب الموسومة. في هذه الورقة، نقدم شبكة واستراتيجية تدريب تعتمد على الاستخدام القوي لزيادة البيانات لاستخدام العينات الموسومة المتاحة بكفاءة أكبر. تتكون المعمارية من مسار انقباضي لالتقاط السياق ومسار توسعي متماثل يمكّن من التحديد الموضعي الدقيق. نُظهر أن مثل هذه الشبكة يمكن تدريبها من البداية للنهاية من عدد قليل جداً من الصور وتتفوق على أفضل طريقة سابقة (شبكة التفافية بنافذة منزلقة) في تحدي ISBI لتجزئة البنى العصبية في حزم المجهر الإلكتروني. باستخدام نفس الشبكة المدربة على صور المجهر الضوئي المنقول (التباين الطوري وDIC) فزنا بتحدي تتبع الخلايا ISBI 2015 في هذه الفئات بهامش كبير. علاوة على ذلك، الشبكة سريعة. تستغرق تجزئة صورة 512×512 أقل من ثانية على وحدة معالجة رسومات حديثة. التطبيق الكامل (القائم على Caffe) والشبكات المدربة متاحة على الموقع المذكور.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** U-Net architecture, contracting path, expanding path, ISBI challenge, data augmentation
- **Equations:** None
- **Citations:** References to ISBI challenges and Caffe framework
- **Special handling:** Preserved technical terms like "end-to-end", "DIC", "ISBI"

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.91
- Readability: 0.90
- Glossary consistency: 0.91
- **Overall section score:** 0.91
