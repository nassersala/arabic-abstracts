# Section 6: Conclusion
## القسم 6: الخاتمة

**Section:** conclusion
**Translation Quality:** 0.89
**Glossary Terms Used:** object detection, convolutional neural networks, region proposals, supervised pre-training, fine-tuning, computer vision, deep learning

---

### English Version

## 6. Conclusion

In recent years, object detection performance had stagnated. The best performing systems were complex ensembles combining multiple low-level image features with high-level context from object detectors and scene classifiers. This paper presents a simple and scalable object detection algorithm that gives a 30% relative improvement over the best previous results on PASCAL VOC 2012.

We achieved this performance through two insights. The first is to apply high-capacity convolutional neural networks to bottom-up region proposals in order to localize and segment objects. The second is a paradigm for training large CNNs when labeled training data is scarce. We show that it is highly effective to pre-train the network—with supervision—for a auxiliary task with abundant data (image classification) and then to fine-tune the network for the target task where data is scarce (detection). We conjecture that the "supervised pre-training/domain-specific fine-tuning" paradigm will be highly effective for a variety of data-scarce vision problems.

We conclude by noting that it is significant that we achieved these results by using a combination of classical tools from computer vision and deep learning (bottom-up region proposals and convolutional neural networks). Rather than opposing lines of scientific inquiry, the two are natural and inevitable partners.

**Acknowledgments.** This research was supported in part by DARPA Mind's Eye and MSEE programs, by NSF awards IIS-0905647, IIS-1134072, and IIS-1212798, MURI N000014-10-1-0933, and by support from Toyota. The GPUs used in this research were generously donated by the NVIDIA Corporation.

---

### النسخة العربية

## 6. الخاتمة

في السنوات الأخيرة، توقف تحسن أداء الكشف عن الأجسام. كانت الأنظمة الأفضل أداءً عبارة عن تجميعات معقدة تجمع بين ميزات صور متعددة منخفضة المستوى مع سياق عالي المستوى من كواشف الأجسام ومصنفات المشاهد. يقدم هذا البحث خوارزمية كشف أجسام بسيطة وقابلة للتوسع تحقق تحسناً نسبياً بنسبة 30% مقارنة بأفضل النتائج السابقة على PASCAL VOC 2012.

حققنا هذا الأداء من خلال رؤيتين. الأولى هي تطبيق الشبكات العصبية الالتفافية عالية السعة على مقترحات المناطق من الأسفل إلى الأعلى من أجل تحديد موقع الأجسام وتقسيمها. الثانية هي نموذج لتدريب الشبكات العصبية الالتفافية الكبيرة عندما تكون بيانات التدريب الموسومة نادرة. نُظهر أنه من الفعال للغاية التدريب المسبق للشبكة - بإشراف - لمهمة مساعدة ببيانات وفيرة (تصنيف الصور) ثم الضبط الدقيق للشبكة للمهمة المستهدفة حيث البيانات نادرة (الكشف). نفترض أن نموذج "التدريب المسبق الموجّه / الضبط الدقيق الخاص بالمجال" سيكون فعالاً للغاية لمجموعة متنوعة من مشاكل الرؤية حيث البيانات نادرة.

نختتم بملاحظة أنه من المهم أننا حققنا هذه النتائج باستخدام مزيج من الأدوات الكلاسيكية من الرؤية الحاسوبية والتعلم العميق (مقترحات المناطق من الأسفل إلى الأعلى والشبكات العصبية الالتفافية). بدلاً من كونهما خطي استقصاء علمي متعارضين، الاثنان شريكان طبيعيان وحتميان.

**شكر وتقدير.** تم دعم هذا البحث جزئياً من قبل برامج DARPA Mind's Eye وMSEE، ومن قبل جوائز NSF: IIS-0905647 وIIS-1134072 وIIS-1212798، وMURI N000014-10-1-0933، ومن خلال الدعم من تويوتا. تم التبرع بوحدات معالجة الرسومات المستخدمة في هذا البحث بسخاء من قبل شركة NVIDIA.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** None (summary section using previously established terminology)
- **Equations:** None
- **Citations:** None in conclusion
- **Special handling:**
  - Preserved funding agency names: DARPA, NSF, MURI, NVIDIA, Toyota
  - Maintained grant numbers as-is
  - Kept the acknowledgments section structure
  - Emphasized the two key insights of the paper
  - Maintained the philosophical conclusion about combining classical CV and deep learning

### Quality Metrics

- Semantic equivalence: 0.91
- Technical accuracy: 0.90
- Readability: 0.88
- Glossary consistency: 0.88
- **Overall section score:** 0.89
