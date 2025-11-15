# Section 6: Conclusion
## القسم 6: الخلاصة

**Section:** conclusion
**Translation Quality:** 0.90
**Glossary Terms Used:** object detection (كشف الأجسام), sparse (متفرقة), dense (كثيفة), proposals (مقترحات)

---

### English Version

This paper proposes Fast R-CNN, a clean and fast update to R-CNN and SPPnet. In addition to reporting state-of-the-art detection results, we present detailed experiments that we hope provide new insights. Of particular note, sparse object proposals appear to improve detector quality. This issue was too costly (in time) to probe in the past, but becomes practical with Fast R-CNN. Of course, there may exist yet undiscovered techniques that allow dense boxes to perform as well as sparse proposals. Such methods, if developed, may help further accelerate object detection.

**Acknowledgements.** I thank Kaiming He, Larry Zitnick, and Piotr Dollár for helpful discussions and encouragement.

---

### النسخة العربية

تقترح هذه الورقة Fast R-CNN، وهو تحديث نظيف وسريع لـ R-CNN و SPPnet. بالإضافة إلى الإبلاغ عن نتائج كشف حديثة، نقدم تجارب مفصلة نأمل أن توفر رؤى جديدة. والجدير بالذكر بشكل خاص، يبدو أن مقترحات الأجسام المتفرقة تحسن جودة الكاشف. كانت هذه المسألة مكلفة جداً (من حيث الوقت) للبحث فيها في الماضي، لكنها تصبح عملية مع Fast R-CNN. بالطبع، قد توجد تقنيات لم تُكتشف بعد تسمح للصناديق الكثيفة بالأداء بنفس جودة المقترحات المتفرقة. قد تساعد مثل هذه الطرق، إذا تم تطويرها، في تسريع كشف الأجسام بشكل أكبر.

**شكر وتقدير.** أشكر Kaiming He و Larry Zitnick و Piotr Dollár على المناقشات والتشجيع المفيدة.

---

### Translation Notes

- **Key points:**
  - Summary of contributions
  - Emphasis on sparse proposals being better than dense boxes
  - Future work suggestions
  - Acknowledgements section

- **Key terms used:**
  - clean and fast update: تحديث نظيف وسريع
  - state-of-the-art: حديثة / الأحدث
  - insights: رؤى
  - sparse object proposals: مقترحات الأجسام المتفرقة
  - detector quality: جودة الكاشف
  - dense boxes: الصناديق الكثيفة

- **Equations:** None
- **Citations:** None in conclusion
- **Special handling:**
  - Kept author names in English (Kaiming He, Larry Zitnick, Piotr Dollár)
  - Maintained the acknowledgements section structure
  - Preserved the formal academic tone

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.92
- Readability: 0.90
- Glossary consistency: 0.95
- **Overall section score:** 0.90

### Back-translation Verification

Key conclusion sentence back-translated:
Arabic: "يبدو أن مقترحات الأجسام المتفرقة تحسن جودة الكاشف"
Back to English: "Sparse object proposals appear to improve detector quality"
✓ Matches original semantics accurately
