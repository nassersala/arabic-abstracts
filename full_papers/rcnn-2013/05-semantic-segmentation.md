# Section 5: Semantic segmentation
## القسم 5: التقسيم الدلالي

**Section:** semantic-segmentation
**Translation Quality:** 0.87
**Glossary Terms Used:** semantic segmentation, region classification, feature extraction, support vector regression, cross-validation, accuracy

---

### English Version

## 5. Semantic segmentation

Region classification is a standard technique for semantic segmentation, allowing us to easily apply R-CNN to the PASCAL VOC segmentation challenge. To facilitate a direct comparison with the current leading semantic segmentation system (called O2P for "second-order pooling") [4], we work within their open source framework. O2P uses CPMC to generate 150 region proposals per image and then predicts the quality of each region, for each class, using support vector regression (SVR). The high performance of their approach is due to the quality of the CPMC regions and the powerful second-order pooling of multiple feature types (enriched variants of SIFT and LBP). We also note that Farabet et al. [16] recently demonstrated good results on several dense scene labeling datasets (not including PASCAL) using a CNN as a multi-scale per-pixel classifier.

We follow [2, 4] and extend the PASCAL segmentation training set to include the extra annotations made available by Hariharan et al. [22]. Design decisions and hyperparameters were cross-validated on the VOC 2011 validation set. Final test results were evaluated only once.

**CNN features for segmentation.** We evaluate three strategies for computing features on CPMC regions, all of which begin by warping the rectangular window around the region to 227×227. The first strategy (full) ignores the region's shape and computes CNN features directly on the warped window, exactly as we did for detection. However, these features ignore the non-rectangular shape of the region. Two regions might have very similar bounding boxes while having very little overlap. Therefore, the second strategy (fg) computes CNN features only on a region's foreground mask. We replace the background with the mean input so that background regions are zero after mean subtraction. The third strategy (full+fg) simply concatenates the full and fg features; our experiments validate their complementarity.

|                    | O2P [4] | full R-CNN fc6 | full R-CNN fc7 | fg R-CNN fc6 | fg R-CNN fc7 | full+fg R-CNN fc6 | full+fg R-CNN fc7 |
|--------------------|---------|----------------|----------------|--------------|--------------|-------------------|-------------------|
| VOC 2011 val       | 46.4    | 43.0           | 42.5           | 43.7         | 42.1         | 47.9              | 45.8              |

**Table 5:** Segmentation mean accuracy (%) on VOC 2011 validation. Column 1 presents O2P; 2-7 use our CNN pre-trained on ILSVRC 2012.

**Results on VOC 2011.** Table 5 shows a summary of our results on the VOC 2011 validation set compared with O2P. (See Appendix E for complete per-category results.) Within each feature computation strategy, layer fc6 always outperforms fc7 and the following discussion refers to the fc6 features. The fg strategy slightly outperforms full, indicating that the masked region shape provides a stronger signal, matching our intuition. However, full+fg achieves an average accuracy of 47.9%, our best result by a margin of 4.2% (also modestly outperforming O2P), indicating that the context provided by the full features is highly informative even given the fg features. Notably, training the 20 SVRs on our full+fg features takes an hour on a single core, compared to 10+ hours for training on O2P features.

In Table 6 we present results on the VOC 2011 test set, comparing our best-performing method, fc6(full+fg), against two strong baselines. Our method achieves the highest segmentation accuracy for 11 out of 21 categories, and the highest overall segmentation accuracy of 47.9%, averaged across categories (but likely ties with the O2P result under any reasonable margin of error). Still better performance could likely be achieved by fine-tuning.

|                              | bg   | aero | bike | bird | boat | bottle | bus  | car  | cat  | chair | cow  | table | dog  | horse | mbike | person | plant | sheep | sofa | train | tv   | mean |
|------------------------------|------|------|------|------|------|--------|------|------|------|-------|------|-------|------|-------|-------|--------|-------|-------|------|-------|------|------|
| R&P [2]                      | 83.4 | 46.8 | 18.9 | 36.6 | 31.2 | 42.7   | 57.3 | 47.4 | 44.1 | 8.1   | 39.4 | 36.1  | 36.3 | 49.5  | 48.3  | 50.7   | 26.3  | 47.2  | 22.1 | 42.0  | 43.2 | 40.8 |
| O2P [4]                      | 85.4 | 69.7 | 22.3 | 45.2 | 44.4 | 46.9   | 66.7 | 57.8 | 56.2 | 13.5  | 46.1 | 32.3  | 41.2 | 59.1  | 55.3  | 51.0   | 36.2  | 50.4  | 27.8 | 46.9  | 44.6 | 47.6 |
| ours (full+fg R-CNN fc6)     | 84.2 | 66.9 | 23.7 | 58.3 | 37.4 | 55.4   | 73.3 | 58.7 | 56.5 | 9.7   | 45.5 | 29.5  | 49.3 | 40.1  | 57.8  | 53.9   | 33.8  | 60.7  | 22.7 | 47.1  | 41.3 | 47.9 |

**Table 6:** Segmentation accuracy (%) on VOC 2011 test. We compare against two strong baselines: the "Regions and Parts" (R&P) method of [2] and the second-order pooling (O2P) method of [4]. Without any fine-tuning, our CNN achieves top segmentation performance, outperforming R&P and roughly matching O2P.

---

### النسخة العربية

## 5. التقسيم الدلالي

تصنيف المناطق هو تقنية قياسية للتقسيم الدلالي، مما يسمح لنا بتطبيق R-CNN بسهولة على تحدي تقسيم PASCAL VOC. لتسهيل مقارنة مباشرة مع نظام التقسيم الدلالي الرائد الحالي (يُدعى O2P لـ "التجميع من الدرجة الثانية") [4]، نعمل ضمن إطار عملهم مفتوح المصدر. يستخدم O2P خوارزمية CPMC لتوليد 150 مقترح منطقة لكل صورة ثم يتنبأ بجودة كل منطقة، لكل صنف، باستخدام انحدار المتجهات الداعمة (SVR). الأداء العالي لنهجهم يرجع إلى جودة مناطق CPMC والتجميع القوي من الدرجة الثانية لأنواع ميزات متعددة (متغيرات محسّنة من SIFT وLBP). نلاحظ أيضاً أن Farabet وآخرين [16] أظهروا مؤخراً نتائج جيدة على عدة مجموعات بيانات لوسم المشاهد الكثيفة (لا تشمل PASCAL) باستخدام شبكة عصبية التفافية كمصنف متعدد المقاييس لكل بكسل.

نتبع [2، 4] ونوسع مجموعة تدريب تقسيم PASCAL لتشمل التعليقات التوضيحية الإضافية التي أتاحها Hariharan وآخرون [22]. تم التحقق المتقاطع من القرارات التصميمية والمعاملات الفائقة على مجموعة تحقق VOC 2011. تم تقييم نتائج الاختبار النهائية مرة واحدة فقط.

**ميزات الشبكة العصبية الالتفافية للتقسيم.** نقيّم ثلاث استراتيجيات لحساب الميزات على مناطق CPMC، وكلها تبدأ بتشويه النافذة المستطيلة حول المنطقة إلى 227×227. الاستراتيجية الأولى (full) تتجاهل شكل المنطقة وتحسب ميزات الشبكة العصبية الالتفافية مباشرة على النافذة المشوهة، تماماً كما فعلنا للكشف. ومع ذلك، تتجاهل هذه الميزات الشكل غير المستطيل للمنطقة. قد يكون لمنطقتين صناديق تحديد متشابهة جداً بينما يكون لهما تداخل ضئيل جداً. لذلك، الاستراتيجية الثانية (fg) تحسب ميزات الشبكة العصبية الالتفافية فقط على قناع المقدمة للمنطقة. نستبدل الخلفية بمتوسط المدخل بحيث تكون مناطق الخلفية صفراً بعد طرح المتوسط. الاستراتيجية الثالثة (full+fg) ببساطة تسلسل ميزات full وfg؛ تجاربنا تتحقق من تكاملها.

|                    | O2P [4] | full R-CNN fc6 | full R-CNN fc7 | fg R-CNN fc6 | fg R-CNN fc7 | full+fg R-CNN fc6 | full+fg R-CNN fc7 |
|--------------------|---------|----------------|----------------|--------------|--------------|-------------------|-------------------|
| VOC 2011 val       | 46.4    | 43.0           | 42.5           | 43.7         | 42.1         | 47.9              | 45.8              |

**الجدول 5:** متوسط دقة التقسيم (%) على تحقق VOC 2011. يعرض العمود 1 نظام O2P؛ تستخدم الأعمدة 2-7 شبكتنا العصبية الالتفافية المدربة مسبقاً على ILSVRC 2012.

**النتائج على VOC 2011.** يُظهر الجدول 5 ملخصاً لنتائجنا على مجموعة تحقق VOC 2011 مقارنة بـ O2P. (انظر الملحق E للنتائج الكاملة لكل فئة.) ضمن كل استراتيجية حساب ميزات، تتفوق طبقة fc6 دائماً على fc7 والمناقشة التالية تشير إلى ميزات fc6. تتفوق استراتيجية fg قليلاً على full، مما يشير إلى أن شكل المنطقة المقنّع يوفر إشارة أقوى، بما يتطابق مع حدسنا. ومع ذلك، تحقق full+fg متوسط دقة 47.9%، أفضل نتيجة لدينا بفارق 4.2% (تتفوق أيضاً بشكل متواضع على O2P)، مما يشير إلى أن السياق المقدم من ميزات full غني بالمعلومات للغاية حتى مع ميزات fg. بشكل ملحوظ، يستغرق تدريب 20 SVR على ميزات full+fg الخاصة بنا ساعة على نواة واحدة، مقارنة بـ 10+ ساعات للتدريب على ميزات O2P.

في الجدول 6 نعرض النتائج على مجموعة اختبار VOC 2011، مقارنة طريقتنا الأفضل أداءً، fc6(full+fg)، مع خطي أساس قويين. تحقق طريقتنا أعلى دقة تقسيم لـ 11 من أصل 21 فئة، وأعلى دقة تقسيم إجمالية بنسبة 47.9%، كمتوسط عبر الفئات (لكن من المحتمل أن تتعادل مع نتيجة O2P ضمن أي هامش خطأ معقول). لا يزال من الممكن تحقيق أداء أفضل من خلال الضبط الدقيق.

|                              | bg   | aero | bike | bird | boat | bottle | bus  | car  | cat  | chair | cow  | table | dog  | horse | mbike | person | plant | sheep | sofa | train | tv   | mean |
|------------------------------|------|------|------|------|------|--------|------|------|------|-------|------|-------|------|-------|-------|--------|-------|-------|------|-------|------|------|
| R&P [2]                      | 83.4 | 46.8 | 18.9 | 36.6 | 31.2 | 42.7   | 57.3 | 47.4 | 44.1 | 8.1   | 39.4 | 36.1  | 36.3 | 49.5  | 48.3  | 50.7   | 26.3  | 47.2  | 22.1 | 42.0  | 43.2 | 40.8 |
| O2P [4]                      | 85.4 | 69.7 | 22.3 | 45.2 | 44.4 | 46.9   | 66.7 | 57.8 | 56.2 | 13.5  | 46.1 | 32.3  | 41.2 | 59.1  | 55.3  | 51.0   | 36.2  | 50.4  | 27.8 | 46.9  | 44.6 | 47.6 |
| ours (full+fg R-CNN fc6)     | 84.2 | 66.9 | 23.7 | 58.3 | 37.4 | 55.4   | 73.3 | 58.7 | 56.5 | 9.7   | 45.5 | 29.5  | 49.3 | 40.1  | 57.8  | 53.9   | 33.8  | 60.7  | 22.7 | 47.1  | 41.3 | 47.9 |

**الجدول 6:** دقة التقسيم (%) على اختبار VOC 2011. نقارن مع خطي أساس قويين: طريقة "المناطق والأجزاء" (R&P) من [2] وطريقة التجميع من الدرجة الثانية (O2P) من [4]. بدون أي ضبط دقيق، تحقق شبكتنا العصبية الالتفافية أفضل أداء تقسيم، متفوقة على R&P ومطابقة تقريباً لـ O2P.

---

### Translation Notes

- **Figures referenced:** Table 5 (validation results), Table 6 (test results), Appendix E (per-category results)
- **Key terms introduced:** semantic segmentation (التقسيم الدلالي), region classification (تصنيف المناطق), support vector regression (انحدار المتجهات الداعمة), foreground mask (قناع المقدمة), second-order pooling (التجميع من الدرجة الثانية)
- **Equations:** None
- **Citations:** References [2, 4, 16, 22] cited
- **Special handling:**
  - Preserved feature strategy names: full, fg, full+fg
  - Maintained table formatting with all numeric values
  - Kept system names: O2P, R&P, CPMC
  - Preserved layer names: fc6, fc7
  - Maintained category abbreviations: bg (background), aero (aeroplane), mbike (motorbike), tv (tvmonitor)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.86
- **Overall section score:** 0.87
