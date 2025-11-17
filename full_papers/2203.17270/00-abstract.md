# Section 0: Abstract
## القسم 0: الملخص

**Section:** Abstract
**Translation Quality:** 0.94
**Glossary Terms Used:** autonomous driving (القيادة الذاتية), 3D detection (كشف ثلاثي الأبعاد), transformer (محول), bird's-eye-view (منظور عين الطائر), attention mechanism (آلية الانتباه), cross-attention (الانتباه المتقاطع), query (استعلام), features (ميزات), views (رؤى), self-attention (الانتباه الذاتي), representation (تمثيل), benchmark (معيار), performance (أداء), object detection (كشف الأجسام), velocity estimation (تقدير السرعة), LiDAR (ليدار), spatiotemporal (زمكاني)

---

### English Version

3D visual perception tasks, including 3D detection and map segmentation based on multi-camera images, are essential for autonomous driving systems. In this work, we present a new framework termed BEVFormer, which learns unified BEV representations with spatiotemporal transformers to support multiple autonomous driving perception tasks. In a nutshell, BEVFormer exploits both spatial and temporal information by interacting with spatial and temporal space through predefined grid-shaped BEV queries. To aggregate spatial information, we design spatial cross-attention that each BEV query extracts the spatial features from the regions of interest across camera views. For temporal information, we propose temporal self-attention to recurrently fuse the history BEV information. Our approach achieves the new state-of-the-art 56.9% in terms of NDS metric on the nuScenes test set, which is 9.0 points higher than previous best arts and on par with the performance of LiDAR-based baselines. We further show that BEVFormer remarkably improves the accuracy of velocity estimation and recall of objects under low visibility conditions. The code is available at https://github.com/zhiqi-li/BEVFormer.

---

### النسخة العربية

تُعد مهام الإدراك البصري ثلاثي الأبعاد، بما في ذلك الكشف ثلاثي الأبعاد وتقسيم الخرائط القائمة على صور الكاميرات المتعددة، ضرورية لأنظمة القيادة الذاتية. في هذا العمل، نقدم إطار عمل جديد يُسمى BEVFormer، والذي يتعلم تمثيلات BEV موحدة باستخدام المحولات الزمكانية لدعم مهام الإدراك المتعددة للقيادة الذاتية. باختصار، يستغل BEVFormer كلاً من المعلومات المكانية والزمنية من خلال التفاعل مع الفضاء المكاني والزمني عبر استعلامات BEV محددة مسبقاً على شكل شبكة. لتجميع المعلومات المكانية، نُصمم انتباهاً متقاطعاً مكانياً حيث يستخرج كل استعلام BEV الميزات المكانية من مناطق الاهتمام عبر رؤى الكاميرات المختلفة. أما بالنسبة للمعلومات الزمنية، فنقترح انتباهاً ذاتياً زمنياً لدمج معلومات BEV التاريخية بشكل متكرر. يحقق نهجنا أحدث مستوى من الأداء بنسبة 56.9% من حيث معيار NDS على مجموعة اختبار nuScenes، وهو أعلى بـ 9.0 نقاط من أفضل الأساليب السابقة ومماثل لأداء الخطوط الأساسية القائمة على الليدار. نُظهر أيضاً أن BEVFormer يُحسّن بشكل ملحوظ دقة تقدير السرعة واستدعاء الأجسام في ظروف الرؤية المنخفضة. الكود متاح على https://github.com/zhiqi-li/BEVFormer.

---

### Translation Notes

- **Figures referenced:** Figure 1 (main architecture diagram)
- **Key terms introduced:** BEV (Bird's-Eye-View), spatiotemporal transformers, spatial cross-attention, temporal self-attention, NDS metric, nuScenes
- **Equations:** None in abstract
- **Citations:** nuScenes benchmark mentioned
- **Special handling:** GitHub URL preserved in both versions

### Quality Metrics

- Semantic equivalence: 0.94
- Technical accuracy: 0.95
- Readability: 0.93
- Glossary consistency: 0.95
- **Overall section score:** 0.94
