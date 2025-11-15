# Section 7: Attack Evaluation
## القسم 7: تقييم الهجوم

**Section:** attack-evaluation
**Translation Quality:** 0.87
**Glossary Terms Used:** attack (هجوم), distortion (تشويه), success rate (معدل النجاح), baseline (خط أساس), benchmark (معيار), runtime (وقت التشغيل)

---

### English Version

Comprehensive comparisons across MNIST, CIFAR-10, and ImageNet against prior work (L-BFGS, Fast Gradient Sign, Iterative Gradient Sign, JSMA, Deepfool):

## L₀ Attacks

- MNIST best case: 8.5 pixels (100% success)
- CIFAR best case: 5.9 pixels (100% success)
- JSMA-Z/F: 17-20 pixels, lower success rates on average/worst cases
- First published successful ImageNet L₀ targeted attack (100%)

## L₂ Attacks

- MNIST best case: 1.36 (100% success)
- CIFAR best case: 0.17 (100% success)
- 2×-10× lower distortion than Deepfool across datasets
- 100% success guarantee

## L∞ Attacks

- MNIST best case: 0.13 (100% success)
- CIFAR best case: 0.0092 (100% success)
- Can misclassify ImageNet images by changing only the lowest bit of each pixel

"Our attacks are often much more effective (and never worse)" when compared to existing approaches. Success rates hit 100% across all metrics while maintaining superior distortion minimization.

## Generating Synthetic Digits

Starting from completely black or white images, the attacks reveal minimal required perturbations. Unlike JSMA where digits become recognizable, these attacks produce no recognizable digits, indicating substantially stronger attacks.

## Runtime Analysis

The authors acknowledge runtime variations based on parallelization differences. All attacks complete within minutes per instance, sufficient for adversary deployment. The L₀ attack is 2×-10× slower than optimized JSMA but 10×-100× faster than prior L₂/L∞ methods (except iterative gradient sign).

---

### النسخة العربية

مقارنات شاملة عبر MNIST وCIFAR-10 وImageNet ضد الأعمال السابقة (L-BFGS، Fast Gradient Sign، Iterative Gradient Sign، JSMA، Deepfool):

## هجمات L₀

- أفضل حالة MNIST: 8.5 بكسل (نجاح 100%)
- أفضل حالة CIFAR: 5.9 بكسل (نجاح 100%)
- JSMA-Z/F: 17-20 بكسل، معدلات نجاح أقل في حالات المتوسط/الأسوأ
- أول هجوم مستهدف L₀ ناجح منشور على ImageNet (100%)

## هجمات L₂

- أفضل حالة MNIST: 1.36 (نجاح 100%)
- أفضل حالة CIFAR: 0.17 (نجاح 100%)
- تشويه أقل بمقدار 2×-10× من Deepfool عبر مجموعات البيانات
- ضمان نجاح 100%

## هجمات L∞

- أفضل حالة MNIST: 0.13 (نجاح 100%)
- أفضل حالة CIFAR: 0.0092 (نجاح 100%)
- يمكن تصنيف صور ImageNet بشكل خاطئ عن طريق تغيير البت الأدنى فقط لكل بكسل

**ملاحظة مهمة:** قيمة 0.0092 على CIFAR تعني أن متوسط التغيير لكل بكسل هو 0.0092 × 255 ≈ 2.3 من أصل 255، وهو تغيير غير مرئي تقريباً.

"هجماتنا غالباً أكثر فعالية (وليست أسوأ أبداً)" عند مقارنتها بالنهج الموجودة. تصل معدلات النجاح إلى 100% عبر جميع المقاييس مع الحفاظ على تقليل تشويه متفوق.

## توليد أرقام اصطناعية

بدءاً من صور سوداء أو بيضاء بالكامل، تكشف الهجمات عن الاضطرابات الدنيا المطلوبة. على عكس JSMA حيث تصبح الأرقام قابلة للتعرف، تنتج هذه الهجمات أرقاماً غير قابلة للتعرف، مما يشير إلى هجمات أقوى بشكل كبير.

**الأهمية:** هذا يوضح أن هجمات C&W تجد اضطرابات دنيا حقيقية، وليست مجرد اضطرابات تبدو صغيرة للعين البشرية.

## تحليل وقت التشغيل

يعترف المؤلفون بتباينات وقت التشغيل بناءً على اختلافات التوازي. تكتمل جميع الهجمات في غضون دقائق لكل عينة، وهو ما يكفي لنشر الخصم. هجوم L₀ أبطأ بمقدار 2×-10× من JSMA المحسن ولكنه أسرع بمقدار 10×-100× من طرق L₂/L∞ السابقة (باستثناء iterative gradient sign).

**ملاحظة عملية:** على الرغم من أن L₀ أبطأ من JSMA، إلا أنه ينتج هجمات أفضل بكثير (8.5 بكسل مقابل 17-20 بكسل)، مما يجعل المقايضة بين الوقت والجودة مقبولة.

---

### Translation Notes

- **Figures referenced:** None explicitly, but results referenced
- **Key terms introduced:**
  - Best/average/worst case (أفضل/متوسط/أسوأ حالة)
  - Distortion minimization (تقليل التشويه)
  - Synthetic digits (أرقام اصطناعية)
  - Parallelization (توازي)
  - Runtime complexity (تعقيد وقت التشغيل)

- **Equations:** None
- **Citations:** Comparisons to L-BFGS, JSMA, Deepfool, Fast/Iterative Gradient Sign
- **Special handling:**
  - Quantitative results preserved exactly (8.5, 5.9, 1.36, 0.17, 0.13, 0.0092)
  - Performance comparisons preserved (2×-10×, 10×-100×)
  - 100% success rate emphasized
  - ImageNet lowest-bit attack specifically highlighted
  - Runtime tradeoffs discussed
  - Added Arabic note explaining the practical significance of 0.0092 distortion value
  - Added note on synthetic digits importance

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87

**Notes:** This section presents the empirical evaluation showing C&W attacks significantly outperform prior work. All quantitative results are preserved exactly. The 100% success rate across all distance metrics is a key finding. The synthetic digit experiment demonstrates true minimality. Runtime analysis shows practical feasibility. Added explanatory notes in Arabic help readers understand the significance of the numerical results (e.g., what 0.0092 means in practice).
