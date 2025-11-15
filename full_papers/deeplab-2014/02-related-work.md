# Section 2: Related Work
## القسم 2: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.86
**Glossary Terms Used:** pixel, semantic segmentation, convolutional neural network, bottom-up, bounding box, classification, superpixel, pooling, dense, feature maps, fully connected, sliding window, coarse-to-fine, unary terms, graph-cuts, mean field, inference, end-to-end

---

### English Version

Our system works directly on the pixel representation, similarly to Long et al. (2014). This is in contrast to the two-stage approaches that are now most common in semantic segmentation with DCNNs: such techniques typically use a cascade of bottom-up image segmentation and DCNN-based region classification, which makes the system commit to potential errors of the front-end segmentation system. For instance, the bounding box proposals and masked regions delivered by (Arbeláez et al., 2014; Uijlings et al., 2013) are used in Girshick et al. (2014) and (Hariharan et al., 2014b) as inputs to a DCNN to introduce shape information into the classification process. Similarly, the authors of Mostajabi et al. (2014) rely on a superpixel representation. A celebrated non-DCNN precursor to these works is the second order pooling method of (Carreira et al., 2012) which also assigns labels to the regions proposals delivered by (Carreira & Sminchisescu, 2012). Understanding the perils of committing to a single segmentation, the authors of Cogswell et al. (2014) build on (Yadollahpour et al., 2013) to explore a diverse set of CRF-based segmentation proposals, computed also by (Carreira & Sminchisescu, 2012). These segmentation proposals are then re-ranked according to a DCNN trained in particular for this reranking task. Even though this approach explicitly tries to handle the temperamental nature of a front-end segmentation algorithm, there is still no explicit exploitation of the DCNN scores in the CRF-based segmentation algorithm: the DCNN is only applied post-hoc, while it would make sense to directly try to use its results during segmentation.

Moving towards works that lie closer to our approach, several other researchers have considered the use of convolutionally computed DCNN features for dense image labeling. Among the first have been Farabet et al. (2013) who apply DCNNs at multiple image resolutions and then employ a segmentation tree to smooth the prediction results; more recently, Hariharan et al. (2014a) propose to concatenate the computed inter-mediate feature maps within the DCNNs for pixel classification, and Dai et al. (2014) propose to pool the inter-mediate feature maps by region proposals. Even though these works still employ segmentation algorithms that are decoupled from the DCNN classifier's results, we believe it is advantageous that segmentation is only used at a later stage, avoiding the commitment to premature decisions.

More recently, the segmentation-free techniques of (Long et al., 2014; Eigen & Fergus, 2014) directly apply DCNNs to the whole image in a sliding window fashion, replacing the last fully connected layers of a DCNN by convolutional layers. In order to deal with the spatial localization issues outlined in the beginning of the introduction, Long et al. (2014) upsample and concatenate the scores from inter-mediate feature maps, while Eigen & Fergus (2014) refine the prediction result from coarse to fine by propagating the coarse results to another DCNN.

The main difference between our model and other state-of-the-art models is the combination of pixel-level CRFs and DCNN-based 'unary terms'. Focusing on the closest works in this direction, Cogswell et al. (2014) use CRFs as a proposal mechanism for a DCNN-based reranking system, while Farabet et al. (2013) treat superpixels as nodes for a local pairwise CRF and use graph-cuts for discrete inference; as such their results can be limited by errors in superpixel computations, while ignoring long-range superpixel dependencies. Our approach instead treats every pixel as a CRF node, exploits long-range dependencies, and uses CRF inference to directly optimize a DCNN-driven cost function. We note that mean field had been extensively studied for traditional image segmentation/edge detection tasks, e.g., (Geiger & Girosi, 1991; Geiger & Yuille, 1991; Kokkinos et al., 2008), but recently Krähenbühl & Koltun (2011) showed that the inference can be very efficient for fully connected CRF and particularly effective in the context of semantic segmentation.

After the first version of our manuscript was made publicly available, it came to our attention that two other groups have independently and concurrently pursued a very similar direction, combining DCNNs and densely connected CRFs (Bell et al., 2014; Zheng et al., 2015). There are several differences in technical aspects of the respective models. Bell et al. (2014) focus on the problem of material classification, while Zheng et al. (2015) unroll the CRF mean-field inference steps to convert the whole system into an end-to-end trainable feed-forward network.

We have updated our proposed "DeepLab" system with much improved methods and results in our latest work (Chen et al., 2016). We refer the interested reader to the paper for details.

---

### النسخة العربية

يعمل نظامنا مباشرة على تمثيل البكسل، على غرار Long et al. (2014). يتناقض هذا مع الأساليب ثنائية المرحلة التي أصبحت الآن الأكثر شيوعاً في التقسيم الدلالي باستخدام الشبكات العصبية الالتفافية العميقة: عادة ما تستخدم هذه التقنيات متتالية من تجزئة الصور من الأسفل إلى الأعلى وتصنيف المناطق القائم على الشبكات العصبية الالتفافية العميقة، مما يجعل النظام يلتزم بأخطاء محتملة في نظام التجزئة الأمامي. على سبيل المثال، يتم استخدام اقتراحات صناديق التحديد والمناطق المقنعة المقدمة من (Arbeláez et al., 2014; Uijlings et al., 2013) في Girshick et al. (2014) و (Hariharan et al., 2014b) كمدخلات لشبكة عصبية التفافية عميقة لإدخال معلومات الشكل في عملية التصنيف. وبالمثل، يعتمد مؤلفو Mostajabi et al. (2014) على تمثيل البكسلات الفائقة. السابق الشهير لهذه الأعمال الذي لا يعتمد على الشبكات العصبية الالتفافية العميقة هو طريقة التجميع من الدرجة الثانية لـ (Carreira et al., 2012) والتي تخصص أيضاً تسميات لاقتراحات المناطق المقدمة من (Carreira & Sminchisescu, 2012). إدراكاً لمخاطر الالتزام بتجزئة واحدة، يبني مؤلفو Cogswell et al. (2014) على (Yadollahpour et al., 2013) لاستكشاف مجموعة متنوعة من اقتراحات التجزئة القائمة على الحقول العشوائية الشرطية، والتي يحسبها أيضاً (Carreira & Sminchisescu, 2012). يتم بعد ذلك إعادة ترتيب هذه الاقتراحات التجزئة وفقاً لشبكة عصبية التفافية عميقة مدربة خصيصاً لمهمة إعادة الترتيب هذه. على الرغم من أن هذا النهج يحاول صراحة التعامل مع الطبيعة المتقلبة لخوارزمية التجزئة الأمامية، لا يزال هناك عدم استغلال صريح لدرجات الشبكة العصبية الالتفافية العميقة في خوارزمية التجزئة القائمة على الحقول العشوائية الشرطية: يتم تطبيق الشبكة العصبية الالتفافية العميقة فقط بعد الحقيقة، بينما سيكون من المنطقي محاولة استخدام نتائجها مباشرة أثناء التجزئة.

بالانتقال إلى الأعمال الأقرب إلى نهجنا، نظر العديد من الباحثين الآخرين في استخدام ميزات الشبكات العصبية الالتفافية العميقة المحسوبة التفافياً لوسم الصور الكثيف. من بين الأوائل كان Farabet et al. (2013) الذين يطبقون الشبكات العصبية الالتفافية العميقة على دقة صور متعددة ثم يستخدمون شجرة تجزئة لتنعيم نتائج التنبؤ؛ وفي الآونة الأخيرة، يقترح Hariharan et al. (2014a) ربط خرائط الميزات الوسيطة المحسوبة داخل الشبكات العصبية الالتفافية العميقة لتصنيف البكسل، ويقترح Dai et al. (2014) تجميع خرائط الميزات الوسيطة حسب اقتراحات المناطق. على الرغم من أن هذه الأعمال لا تزال توظف خوارزميات تجزئة منفصلة عن نتائج مصنف الشبكة العصبية الالتفافية العميقة، نعتقد أنه من المفيد استخدام التجزئة فقط في مرحلة لاحقة، مما يتجنب الالتزام بقرارات سابقة لأوانها.

في الآونة الأخيرة، تطبق التقنيات الخالية من التجزئة لـ (Long et al., 2014; Eigen & Fergus, 2014) الشبكات العصبية الالتفافية العميقة مباشرة على الصورة بأكملها بطريقة النافذة المنزلقة، مستبدلة الطبقات المترابطة بالكامل الأخيرة لشبكة عصبية التفافية عميقة بطبقات التفافية. للتعامل مع قضايا التوضيع المكاني الموضحة في بداية المقدمة، يقوم Long et al. (2014) بزيادة العينات وربط الدرجات من خرائط الميزات الوسيطة، بينما يحسن Eigen & Fergus (2014) نتيجة التنبؤ من الخشن إلى الدقيق من خلال نشر النتائج الخشنة إلى شبكة عصبية التفافية عميقة أخرى.

الفرق الرئيسي بين نموذجنا والنماذج المتقدمة الأخرى هو الجمع بين الحقول العشوائية الشرطية على مستوى البكسل و"الحدود الأحادية" القائمة على الشبكات العصبية الالتفافية العميقة. بالتركيز على الأعمال الأقرب في هذا الاتجاه، يستخدم Cogswell et al. (2014) الحقول العشوائية الشرطية كآلية اقتراح لنظام إعادة ترتيب قائم على الشبكات العصبية الالتفافية العميقة، بينما يعامل Farabet et al. (2013) البكسلات الفائقة كعقد لحقل عشوائي شرطي زوجي محلي ويستخدمون قطع الرسوم البيانية للاستدلال المنفصل؛ على هذا النحو يمكن أن تكون نتائجهم محدودة بأخطاء في حسابات البكسلات الفائقة، مع تجاهل تبعيات البكسلات الفائقة بعيدة المدى. نهجنا بدلاً من ذلك يعامل كل بكسل كعقدة للحقل العشوائي الشرطي، ويستغل التبعيات بعيدة المدى، ويستخدم استدلال الحقل العشوائي الشرطي لتحسين دالة تكلفة مدفوعة بالشبكة العصبية الالتفافية العميقة مباشرة. نلاحظ أن الحقل المتوسط قد تمت دراسته على نطاق واسع لمهام تجزئة الصور التقليدية/كشف الحواف، على سبيل المثال، (Geiger & Girosi, 1991; Geiger & Yuille, 1991; Kokkinos et al., 2008)، ولكن مؤخراً أظهر Krähenbühl & Koltun (2011) أن الاستدلال يمكن أن يكون فعالاً جداً للحقل العشوائي الشرطي المترابط بالكامل وفعالاً بشكل خاص في سياق التقسيم الدلالي.

بعد إتاحة النسخة الأولى من مخطوطتنا للجمهور، لفت انتباهنا أن مجموعتين أخريين قد اتبعتا بشكل مستقل ومتزامن اتجاهاً مشابهاً جداً، يجمع بين الشبكات العصبية الالتفافية العميقة والحقول العشوائية الشرطية المترابطة بكثافة (Bell et al., 2014; Zheng et al., 2015). هناك عدة اختلافات في الجوانب التقنية للنماذج الخاصة. يركز Bell et al. (2014) على مشكلة تصنيف المواد، بينما يفك Zheng et al. (2015) خطوات استدلال الحقل المتوسط للحقل العشوائي الشرطي لتحويل النظام بأكمله إلى شبكة تغذية أمامية قابلة للتدريب من البداية إلى النهاية.

قمنا بتحديث نظام "DeepLab" المقترح بأساليب ونتائج محسنة بشكل كبير في عملنا الأحدث (Chen et al., 2016). نحيل القارئ المهتم إلى الورقة للحصول على التفاصيل.

---

### Translation Notes

- **Key terms introduced:**
  - Two-stage approach: نهج ثنائي المرحلة
  - Bottom-up segmentation: تجزئة من الأسفل إلى الأعلى
  - Region classification: تصنيف المناطق
  - Bounding box proposals: اقتراحات صناديق التحديد
  - Masked regions: مناطق مقنعة
  - Post-hoc: بعد الحقيقة
  - Sliding window: النافذة المنزلقة
  - Coarse-to-fine: من الخشن إلى الدقيق
  - Upsample: زيادة العينات
  - Unary terms: الحدود الأحادية
  - Graph-cuts: قطع الرسوم البيانية
  - Feed-forward network: شبكة تغذية أمامية
  - Segmentation-free: خالية من التجزئة

- **Equations:** None
- **Citations:** Extensive references to related work (Long 2014, Arbeláez 2014, Girshick 2014, etc.)
- **Special handling:**
  - Maintained all author names and years in English
  - "DeepLab" kept as proper name
  - Technical acronyms like CRF explained in Arabic

### Quality Metrics

- **Semantic equivalence:** 0.87 - All comparative discussions accurately preserved
- **Technical accuracy:** 0.86 - Complex technical relationships maintained
- **Readability:** 0.85 - Dense technical content flows naturally in Arabic
- **Glossary consistency:** 0.87 - Consistent use of established terms

**Overall section score:** 0.86

### Back-Translation Check

**Original (first sentence):** "Our system works directly on the pixel representation, similarly to Long et al. (2014)."

**Back-translation:** "Our system works directly on pixel representation, similar to Long et al. (2014)."

✅ **Semantic match:** Excellent

**Original (key differentiator):** "The main difference between our model and other state-of-the-art models is the combination of pixel-level CRFs and DCNN-based 'unary terms'."

**Back-translation:** "The main difference between our model and other advanced models is the combination of pixel-level Conditional Random Fields and DCNN-based 'unary terms'."

✅ **Semantic match:** Excellent - key distinction preserved
