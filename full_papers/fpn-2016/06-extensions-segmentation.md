# Section 6: Extensions: Segmentation Proposals
## القسم 6: التوسعات: مقترحات التجزئة

**Section:** extensions-segmentation
**Translation Quality:** 0.87
**Glossary Terms Used:** segmentation, instance segmentation, feature pyramid, object detection, mask, proposals, MLP, fully convolutional, inference

---

### English Version

Our method is a generic pyramid representation and can be used in applications other than object detection. In this section we use FPNs to generate segmentation proposals, following the DeepMask/SharpMask framework [27, 28].

DeepMask/SharpMask were trained on image crops for predicting instance segments and object/non-object scores. At inference time, these models are run convolutionally to generate dense proposals in an image. To generate segments at multiple scales, image pyramids are necessary [27, 28].

It is easy to adapt FPN to generate mask proposals. We use a fully convolutional setup for both training and inference. We construct our feature pyramid as in Sec. 5.1 and set d = 128. On top of each level of the feature pyramid, we apply a small 5×5 MLP to predict 14×14 masks and object scores in a fully convolutional fashion, see Fig. 4. Additionally, motivated by the use of 2 scales per octave in the image pyramid of [27, 28], we use a second MLP of input size 7×7 to handle half octaves. The two MLPs play a similar role as anchors in RPN. The architecture is trained end-to-end; full implementation details are given in the appendix.

**6.1. Segmentation Proposal Results**

Results are shown in Table 6. We report segment AR and segment AR on small, medium, and large objects, always for 1000 proposals. Our baseline FPN model with a single 5×5 MLP achieves an AR of 43.4. Switching to a slightly larger 7×7 MLP leaves accuracy largely unchanged. Using both MLPs together increases accuracy to 45.7 AR. Increasing mask output size from 14×14 to 28×28 increases AR another point (larger sizes begin to degrade accuracy). Finally, doubling the training iterations increases AR to 48.1.

We also report comparisons to DeepMask [27], SharpMask [28], and InstanceFCN [4], the previous state of the art methods in mask proposal generation. We outperform the accuracy of these approaches by over 8.3 points AR. In particular, we nearly double the accuracy on small objects.

Existing mask proposal methods [27, 28, 4] are based on densely sampled image pyramids (e.g., scaled by 2{-2:0.5:1} in [27, 28]), making them computationally expensive. Our approach, based on FPNs, is substantially faster (our models run at 6 to 7 FPS). These results demonstrate that our model is a generic feature extractor and can replace image pyramids for other multi-scale detection problems.

On the test-dev set, our method increases over the existing best results by 0.5 points of AP (36.2 vs. 35.7) and 3.4 points of AP@0.5 (59.1 vs. 55.7). It is worth noting that our method does not rely on image pyramids and only uses a single input image scale, but still has outstanding AP on small-scale objects. This could only be achieved by high-resolution image inputs with previous methods.

Moreover, our method does not exploit many popular improvements, such as iterative regression [9], hard negative mining [35], context modeling [16], stronger data augmentation [22], etc. These improvements are complementary to FPNs and should boost accuracy further.

Recently, FPN has enabled new top results in all tracks of the COCO competition, including detection, instance segmentation, and keypoint estimation. See [14] for details.

---

### النسخة العربية

طريقتنا هي تمثيل هرمي عام ويمكن استخدامها في تطبيقات غير الكشف عن الأشياء. في هذا القسم نستخدم شبكات FPN لتوليد مقترحات التجزئة، متبعين إطار DeepMask/SharpMask [27، 28].

تم تدريب DeepMask/SharpMask على قصاصات الصور للتنبؤ بقطاعات المثيل ودرجات شيء/غير شيء. في وقت الاستنتاج، يتم تشغيل هذه النماذج بشكل التفافي لتوليد مقترحات كثيفة في الصورة. لتوليد قطاعات على مقاييس متعددة، تكون أهرام الصور ضرورية [27، 28].

من السهل تكييف FPN لتوليد مقترحات القناع. نستخدم إعدادًا التفافيًا بالكامل لكل من التدريب والاستنتاج. نبني هرم السمات الخاص بنا كما في القسم 5.1 ونضع d = 128. فوق كل مستوى من هرم السمات، نطبق شبكة MLP صغيرة 5×5 للتنبؤ بأقنعة 14×14 ودرجات الأشياء بطريقة التفافية بالكامل، انظر الشكل 4. بالإضافة إلى ذلك، بدافع من استخدام مقياسين لكل أوكتاف في هرم الصورة في [27، 28]، نستخدم شبكة MLP ثانية بحجم إدخال 7×7 للتعامل مع نصف الأوكتافات. تلعب شبكتا MLP دورًا مشابهًا للمراسي في RPN. يتم تدريب المعمارية من البداية إلى النهاية؛ تُعطى تفاصيل التنفيذ الكاملة في الملحق.

**6.1. نتائج مقترحات التجزئة**

تُظهر النتائج في الجدول 6. نُبلغ عن AR للقطاع و AR للقطاع على الأشياء الصغيرة والمتوسطة والكبيرة، دائمًا لـ 1000 مقترح. يحقق نموذج FPN الأساسي الخاص بنا مع شبكة MLP واحدة 5×5 AR قدره 43.4. التبديل إلى شبكة MLP أكبر قليلاً 7×7 يترك الدقة دون تغيير إلى حد كبير. استخدام كلا شبكتي MLP معًا يزيد الدقة إلى 45.7 AR. زيادة حجم إخراج القناع من 14×14 إلى 28×28 يزيد AR نقطة أخرى (الأحجام الأكبر تبدأ في تدهور الدقة). أخيرًا، مضاعفة تكرارات التدريب يزيد AR إلى 48.1.

نُبلغ أيضًا عن مقارنات مع DeepMask [27]، SharpMask [28]، و InstanceFCN [4]، الطرق السابقة للحالة الحديثة في توليد مقترحات القناع. نتفوق على دقة هذه النهج بأكثر من 8.3 نقطة AR. على وجه الخصوص، نضاعف تقريبًا الدقة على الأشياء الصغيرة.

تعتمد طرق مقترحات القناع الموجودة [27، 28، 4] على أهرام صور كثيفة العينات (على سبيل المثال، بمقياس 2{-2:0.5:1} في [27، 28])، مما يجعلها مكلفة حسابيًا. نهجنا، القائم على شبكات FPN، أسرع بكثير (تعمل نماذجنا بمعدل 6 إلى 7 إطارات في الثانية). تُظهر هذه النتائج أن نموذجنا هو مستخرج سمات عام ويمكن أن يحل محل أهرام الصور لمشاكل الكشف متعددة النطاقات الأخرى.

في مجموعة test-dev، تزيد طريقتنا عن أفضل النتائج الموجودة بمقدار 0.5 نقطة من AP (36.2 مقابل 35.7) و 3.4 نقطة من AP@0.5 (59.1 مقابل 55.7). يجدر الإشارة إلى أن طريقتنا لا تعتمد على أهرام الصور وتستخدم فقط مقياس صورة إدخال واحد، ولكنها لا تزال تتمتع بـ AP متميز على الأشياء صغيرة المقياس. هذا لا يمكن تحقيقه إلا بمدخلات صور عالية الدقة مع الطرق السابقة.

علاوة على ذلك، لا تستغل طريقتنا العديد من التحسينات الشائعة، مثل الانحدار التكراري [9]، والتعدين السلبي الصعب [35]، ونمذجة السياق [16]، وزيادة البيانات الأقوى [22]، وما إلى ذلك. هذه التحسينات مكملة لشبكات FPN ويجب أن تعزز الدقة بشكل أكبر.

مؤخرًا، مكّنت FPN نتائج جديدة رائدة في جميع مسارات مسابقة COCO، بما في ذلك الكشف، والتجزئة حسب المثيل، وتقدير النقاط الرئيسية. انظر [14] للتفاصيل.

---

### Translation Notes

- **Figures referenced:** Figure 4
- **Tables referenced:** Table 6
- **Key terms introduced:**
  - segmentation proposals: مقترحات التجزئة
  - instance segments: قطاعات المثيل
  - mask proposals: مقترحات القناع
  - fully convolutional: التفافي بالكامل
  - half octaves: نصف الأوكتافات
  - mask output: إخراج القناع
  - iterative regression: الانحدار التكراري
  - hard negative mining: التعدين السلبي الصعب
  - context modeling: نمذجة السياق
  - data augmentation: زيادة البيانات
  - keypoint estimation: تقدير النقاط الرئيسية
- **Equations:** 0
- **Citations:** References to [4, 9, 14, 16, 22, 27, 28, 35]
- **Special handling:**
  - Technical names kept in English: DeepMask, SharpMask, InstanceFCN, MLP
  - FPS (frames per second) kept as English abbreviation
  - Mathematical notation like "5×5", "7×7", "14×14", "28×28" kept as is

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.91
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87

### Back-Translation Check

Key phrases verified:
- "مقترحات التجزئة" → Segmentation proposals ✓
- "قطاعات المثيل" → Instance segments ✓
- "مقترحات القناع" → Mask proposals ✓
- "التفافي بالكامل" → Fully convolutional ✓
- "نصف الأوكتافات" → Half octaves ✓
- "التعدين السلبي الصعب" → Hard negative mining ✓
