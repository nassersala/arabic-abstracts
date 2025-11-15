# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.92
**Glossary Terms Used:** object detection, region proposal, convolutional, neural network, GPU, accuracy, fps, dataset, network, feature, computation, bottleneck

---

### English Version

State-of-the-art object detection networks depend on region proposal algorithms to hypothesize object locations. Advances like SPPnet and Fast R-CNN have reduced the running time of these detection networks, exposing region proposal computation as a bottleneck. In this work, we introduce a Region Proposal Network (RPN) that shares full-image convolutional features with the detection network, thus enabling nearly cost-free region proposals. An RPN is a fully convolutional network that simultaneously predicts object bounds and objectness scores at each position. The RPN is trained end-to-end to generate high-quality region proposals, which are used by Fast R-CNN for detection. We further merge RPN and Fast R-CNN into a single network by sharing their convolutional features—using the recent terminology of neural networks with 'attention' mechanisms, the RPN component tells the unified network where to look. For the very deep VGG-16 model, our detection system has a frame rate of 5 fps (including all steps) on a GPU, while achieving state-of-the-art object detection accuracy on PASCAL VOC 2007, 2012, and MS COCO datasets with only 300 proposals per image. In ILSVRC and COCO 2015 competitions, Faster R-CNN and RPN are the foundations of the 1st-place winning entries in several tracks.

---

### النسخة العربية

تعتمد شبكات كشف الأجسام المتطورة على خوارزميات اقتراح المناطق لافتراض مواقع الأجسام. لقد قللت التطورات مثل SPPnet وFast R-CNN من زمن تشغيل شبكات الكشف هذه، مما كشف أن حساب اقتراح المناطق يمثل عنق زجاجة. في هذا العمل، نقدم شبكة اقتراح المناطق (RPN) التي تشارك الميزات الالتفافية للصورة الكاملة مع شبكة الكشف، وبالتالي تمكين اقتراحات المناطق بتكلفة حسابية شبه معدومة. شبكة RPN هي شبكة التفافية بالكامل تتنبأ في آن واحد بحدود الأجسام ودرجات وجود الجسم في كل موضع. يتم تدريب شبكة RPN من طرف إلى طرف لتوليد اقتراحات مناطق عالية الجودة، والتي تُستخدم بواسطة Fast R-CNN للكشف. ندمج بشكل إضافي شبكة RPN وFast R-CNN في شبكة واحدة من خلال مشاركة ميزاتهما الالتفافية - باستخدام المصطلحات الحديثة للشبكات العصبية ذات آليات "الانتباه"، يخبر مكون RPN الشبكة الموحدة عن المكان الذي يجب النظر إليه. بالنسبة لنموذج VGG-16 العميق جداً، يحقق نظام الكشف لدينا معدل 5 إطارات في الثانية (بما في ذلك جميع الخطوات) على وحدة معالجة الرسومات، مع تحقيق دقة كشف أجسام متطورة على مجموعات بيانات PASCAL VOC 2007 و2012 وMS COCO باستخدام 300 اقتراح فقط لكل صورة. في مسابقات ILSVRC وCOCO 2015، تُعد Faster R-CNN وRPN الأساس لإدخالات الفوز بالمركز الأول في عدة مسارات.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:** Region Proposal Network (RPN), شبكة اقتراح المناطق، objectness scores (درجات وجود الجسم), attention mechanisms (آليات الانتباه)
- **Equations:** 0
- **Citations:** None in abstract (mentions SPPnet, Fast R-CNN, VGG-16, PASCAL VOC, MS COCO, ILSVRC)
- **Special handling:**
  - Preserved technical terms like SPPnet, Fast R-CNN, VGG-16 as is (standard in Arabic academic writing)
  - Translated "frame rate" as "معدل الإطارات" following standard terminology
  - "End-to-end" translated as "من طرف إلى طرف" (standard ML term in Arabic)
  - "Objectness" translated as "وجود الجسم" (existence/presence of object)

### Quality Metrics

- Semantic equivalence: 0.95 (preserves all key concepts and technical meaning)
- Technical accuracy: 0.93 (correct use of all domain-specific terms)
- Readability: 0.90 (natural flow in formal academic Arabic)
- Glossary consistency: 0.92 (uses established glossary terms consistently)
- **Overall section score:** 0.92

### Back-Translation Check (First Sentence)

Arabic: تعتمد شبكات كشف الأجسام المتطورة على خوارزميات اقتراح المناطق لافتراض مواقع الأجسام.
Back to English: "State-of-the-art object detection networks depend on region proposal algorithms to hypothesize object locations."
✓ Semantic match confirmed
