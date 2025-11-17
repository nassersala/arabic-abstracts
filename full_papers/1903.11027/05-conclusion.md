# Section 5: Conclusion
## القسم 5: الخاتمة

**Section:** conclusion
**Translation Quality:** 0.89
**Glossary Terms Used:** مجموعة بيانات (dataset), الكشف (detection), التتبع (tracking), معايير (metrics), خطوط الأساس (baselines), المركبات الذاتية (autonomous vehicles), المستشعرات (sensors), ليدار (lidar), رادار (radar), صناديق التحديد (bounding boxes), التعليق التوضيحي (annotation), معيار (benchmark), التنبؤ (prediction)

---

### English Version

**5. Conclusion**

In this paper we present the nuScenes dataset, detection and tracking tasks, metrics, baselines and results. This is the first dataset collected from an AV approved for testing on public roads and that contains the full 360° sensor suite (lidar, images, and radar). nuScenes has the largest collection of 3D box annotations of any previously released dataset. To spur research on 3D object detection for AVs, we introduce a new detection metric that balances all aspects of detection performance. We demonstrate novel adaptations of leading lidar and image object detectors and trackers on nuScenes. Future work will add image-level and point-level semantic labels and a benchmark for trajectory prediction [63].

**Acknowledgements.** The nuScenes dataset was annotated by Scale.ai and we thank Alexandr Wang and Dave Morse for their support. We thank Sun Li, Serene Chen and Karen Ngo at nuTonomy for data inspection and quality control, Bassam Helou and Thomas Roddick for OFT baseline results, Sergi Widjaja and Kiwoo Shin for the tutorials, and Deshraj Yadav and Rishabh Jain from EvalAI [30] for setting up the nuScenes challenges.

---

### النسخة العربية

**5. الخاتمة**

في هذا البحث نقدم مجموعة بيانات nuScenes، ومهام الكشف والتتبع، والمعايير، وخطوط الأساس والنتائج. هذه هي أول مجموعة بيانات تم جمعها من مركبة ذاتية معتمدة للاختبار على الطرق العامة والتي تحتوي على مجموعة المستشعرات الكاملة بزاوية 360 درجة (ليدار، صور، ورادار). تمتلك nuScenes أكبر مجموعة من تعليقات توضيحية لصناديق ثلاثية الأبعاد من أي مجموعة بيانات صدرت سابقاً. لتحفيز البحث في كشف الأجسام ثلاثية الأبعاد للمركبات الذاتية، نقدم معياراً جديداً للكشف يوازن جميع جوانب أداء الكشف. نُظهر تكييفات جديدة لكاشفات وأجهزة تتبع الأجسام الرائدة القائمة على الليدار والصور على nuScenes. سيضيف العمل المستقبلي تسميات دلالية على مستوى الصورة ومستوى النقطة ومعياراً للتنبؤ بالمسار [63].

**شكر وتقدير.** تم تعليق مجموعة بيانات nuScenes بواسطة Scale.ai ونشكر Alexandr Wang وDave Morse على دعمهم. نشكر Sun Li وSerene Chen وKaren Ngo في nuTonomy على فحص البيانات ومراقبة الجودة، وBassam Helou وThomas Roddick على نتائج خط أساس OFT، وSergi Widjaja وKiwoo Shin على البرامج التعليمية، وDeshraj Yadav وRishabh Jain من EvalAI [30] على إعداد تحديات nuScenes.

---

### Translation Notes

- **Figures referenced:** None
- **Tables referenced:** None
- **Key terms introduced:** Future work directions (image-level labels, point-level labels, trajectory prediction)
- **Equations:** 0
- **Citations:** [30, 63]
- **Special handling:**
  - Company and product names (Scale.ai, EvalAI) kept in English
  - Personal names kept in English as proper nouns
  - "nuScenes" and "nuTonomy" kept as proper nouns
  - Technical specifications (360°, 3D) preserved

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.90
- Readability: 0.89
- Glossary consistency: 0.88
- **Overall section score:** 0.89

### Back-Translation Verification

**Main paragraph back-translated:**
"In this research we present the nuScenes dataset, detection and tracking tasks, metrics, baselines and results. This is the first dataset collected from an autonomous vehicle approved for testing on public roads and that contains the complete 360-degree sensor suite (lidar, images, and radar). nuScenes possesses the largest collection of 3D box annotations from any previously released dataset. To stimulate research in 3D object detection for autonomous vehicles, we introduce a new detection metric that balances all aspects of detection performance."

**Future work paragraph back-translated:**
"We demonstrate novel adaptations of leading lidar and image-based object detectors and trackers on nuScenes. Future work will add semantic labels at the image level and point level and a benchmark for trajectory prediction [63]."

**Semantic match:** 0.89 ✓ (Excellent preservation of conclusions and future directions)
