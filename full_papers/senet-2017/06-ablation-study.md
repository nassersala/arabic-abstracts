# Section 6: Ablation Study
## القسم 6: دراسة الإزالة التدريجية

**Section:** ablation-study
**Translation Quality:** 0.89
**Glossary Terms Used:** reduction ratio, global average pooling, excitation, sigmoid activation, ReLU, tanh, computational efficiency, parameters, top-1 error, top-5 error

---

### English Version

#### 6.1 Reduction Ratio

The reduction ratio *r* controls the capacity and computational efficiency of SE blocks. Testing values from 2 to 32 on SE-ResNet-50:

- **r=16** provides optimal balance: 22.28% top-1 error, 6.03% top-5 error
- **r=2** achieves lowest error (22.29%) but increases parameters to 45.7M
- **r=32** degrades performance (22.72% top-1) while reducing parameters to 26.9M

Finding: "performance is robust to a range of reduction ratios," with r=16 offering practical efficiency.

#### 6.2 Squeeze Operator

Comparing global average pooling versus global max pooling:

- **Average pooling**: 22.28% top-1, 6.03% top-5 (selected)
- **Max pooling**: 22.57% top-1, 6.09% top-5

Result: Average pooling achieves marginally better performance while remaining computationally efficient.

#### 6.3 Excitation Operator

Testing alternative non-linearities for the gating mechanism:

- **Sigmoid**: 22.28% top-1, 6.03% top-5 (optimal)
- **Tanh**: 23.00% top-1, 6.38% top-5
- **ReLU**: 23.47% top-1, 6.98% top-5 (substantially worse)

Key insight: "careful construction of the excitation operator is important" for effectiveness.

#### 6.4 Different Stages

Progressively adding SE blocks to ResNet-50 stages:

- Stage 2 only: 23.03% top-1
- Stage 3 only: 23.04% top-1
- Stage 4 only: 22.68% top-1
- All stages: 22.28% top-1

Finding: SE block benefits are complementary across network depth; gains accumulate effectively.

#### 6.5 Integration Strategy

Four placement strategies tested:

- **SE (proposed)**: 22.28% top-1
- **SE-PRE**: 22.23% top-1
- **SE-Identity**: 22.20% top-1
- **SE-POST**: 22.78% top-1 (performance drops significantly)

Result: "performance improvements are fairly robust" when SE blocks apply before branch aggregation, but placement after summation reduces effectiveness.

#### Additional Finding

SE blocks positioned at the 3×3 convolutional layer within residual units achieve comparable accuracy (22.48% top-1) with reduced parameters (25.8M vs. 28.1M), demonstrating efficiency optimization potential.

---

### النسخة العربية

#### 6.1 نسبة التخفيض

تتحكم نسبة التخفيض *r* في سعة وكفاءة الحسابات لكتل SE. اختبار قيم من 2 إلى 32 على SE-ResNet-50:

- **r=16** توفر التوازن الأمثل: خطأ أعلى-1 بنسبة 22.28٪، خطأ أعلى-5 بنسبة 6.03٪
- **r=2** تحقق أقل خطأ (22.29٪) لكن تزيد المعاملات إلى 45.7 مليون
- **r=32** تُضعف الأداء (22.72٪ أعلى-1) بينما تقلل المعاملات إلى 26.9 مليون

الاستنتاج: "الأداء قوي عبر نطاق من نسب التخفيض"، مع r=16 التي توفر الكفاءة العملية.

#### 6.2 معامل الضغط

مقارنة التجميع المتوسط الشامل مقابل التجميع الأقصى الشامل:

- **التجميع المتوسط**: 22.28٪ أعلى-1، 6.03٪ أعلى-5 (المختار)
- **التجميع الأقصى**: 22.57٪ أعلى-1، 6.09٪ أعلى-5

النتيجة: التجميع المتوسط يحقق أداءً أفضل بشكل طفيف مع البقاء فعالاً حسابياً.

#### 6.3 معامل الإثارة

اختبار بدائل اللاخطية لآلية البوابة:

- **Sigmoid**: 22.28٪ أعلى-1، 6.03٪ أعلى-5 (الأمثل)
- **Tanh**: 23.00٪ أعلى-1، 6.38٪ أعلى-5
- **ReLU**: 23.47٪ أعلى-1، 6.98٪ أعلى-5 (أسوأ بكثير)

الفكرة الرئيسية: "البناء الدقيق لمعامل الإثارة مهم" للفعالية.

#### 6.4 المراحل المختلفة

إضافة كتل SE تدريجياً إلى مراحل ResNet-50:

- المرحلة 2 فقط: 23.03٪ أعلى-1
- المرحلة 3 فقط: 23.04٪ أعلى-1
- المرحلة 4 فقط: 22.68٪ أعلى-1
- جميع المراحل: 22.28٪ أعلى-1

الاستنتاج: فوائد كتل SE متكاملة عبر عمق الشبكة؛ تتراكم المكاسب بفعالية.

#### 6.5 استراتيجية التكامل

اختبار أربع استراتيجيات موضع:

- **SE (المقترح)**: 22.28٪ أعلى-1
- **SE-PRE**: 22.23٪ أعلى-1
- **SE-Identity**: 22.20٪ أعلى-1
- **SE-POST**: 22.78٪ أعلى-1 (ينخفض الأداء بشكل كبير)

النتيجة: "تحسينات الأداء قوية إلى حد ما" عندما تُطبق كتل SE قبل تجميع الفروع، لكن الموضع بعد الجمع يقلل الفعالية.

#### اكتشاف إضافي

كتل SE الموضوعة في الطبقة الالتفافية 3×3 ضمن وحدات متبقية تحقق دقة مماثلة (22.48٪ أعلى-1) مع معاملات مخفضة (25.8 مليون مقابل 28.1 مليون)، مما يُظهر إمكانية تحسين الكفاءة.

---

### Translation Notes

- **Figures referenced:** Likely includes tables/figures showing ablation results
- **Key terms introduced:**
  - Reduction ratio → نسبة التخفيض
  - Global average pooling → التجميع المتوسط الشامل
  - Global max pooling → التجميع الأقصى الشامل
  - Squeeze operator → معامل الضغط
  - Excitation operator → معامل الإثارة
  - Non-linearity → اللاخطية
  - Gating mechanism → آلية البوابة
  - Sigmoid → Sigmoid (kept as standard function name)
  - Tanh → Tanh (kept as standard function name)
  - ReLU → ReLU (kept as standard abbreviation)
  - Integration strategy → استراتيجية التكامل
  - Branch aggregation → تجميع الفروع
  - SE-PRE, SE-POST, SE-Identity → (kept as variant names)
  - Residual units → وحدات متبقية
  - Complementary → متكاملة

- **Equations:** None (numerical results only)
- **Key findings:**
  1. r=16 is optimal reduction ratio
  2. Average pooling > max pooling
  3. Sigmoid > tanh > ReLU for excitation
  4. Benefits accumulate across stages
  5. Placement before summation is critical

- **Numerical results preserved:**
  - Various error rates for different configurations
  - Parameter counts (45.7M, 26.9M, 25.8M, 28.1M)
  - All top-1 and top-5 error percentages

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.91
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.89
