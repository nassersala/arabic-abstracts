# Section 2: Background
## القسم 2: الخلفية

**Section:** background
**Translation Quality:** 0.88
**Glossary Terms Used:** neural networks (شبكة عصبية), adversarial examples (أمثلة خصامية), defensive distillation (تقطير دفاعي), white-box (صندوق أبيض), black-box (صندوق أسود), activation function (دالة التنشيط), softmax, gradient (تدرج), optimization (تحسين), logits (اللوجيتات)

---

### English Version

## II-A Threat Model

The paper assumes white-box access where attackers possess complete network knowledge including architecture and parameters. This conservative assumption reflects practical realities: "prior work has shown it is possible to train a substitute model given black-box access to a target model, and by attacking the substitute model, we can then transfer these attacks to the target model."

Applications vulnerable to adversarial examples span self-driving vehicles, malware classification, speech recognition, and drone systems. The key question becomes determining required distortion levels across different domains using appropriate distance metrics.

## II-B Neural Networks and Notation

Networks are formalized as functions $F(x) = y$ mapping inputs to outputs through composed layers. The softmax function produces probability distributions: $y_i$ represents the probability that input $x$ belongs to class $i$, with $C(x) = \arg\max_i F(x)_i$ assigning the predicted label.

Notation distinguishes $F(x)$ (full network with softmax) from $Z(x)$ (logits—outputs before softmax). Networks typically consist of stacked layers where $F_i(x) = \sigma(\theta_i \cdot x) + \hat{\theta}_i$, with $\sigma$ denoting activation functions (ReLU used predominantly).

## II-C Adversarial Examples

An adversarial example $x'$ satisfies $C(x') = t$ where $t \neq C^*(x)$, yet remains close to original input $x$ under some distance metric. The paper examines three attack types:

- **Average Case**: Target randomly selected incorrect class
- **Best Case**: Attack all incorrect classes, report easiest
- **Worst Case**: Attack all incorrect classes, report hardest

## II-D Distance Metrics

Three $L_p$ norms quantify similarity:

**L₀ Distance**: Counts modified coordinates. "The L₀ distance corresponds to the number of pixels that have been altered in an image." Papernot et al. argue this metric best captures defensive distillation's security claims.

**L₂ Distance**: Euclidean (root-mean-square) distance between vectors, used in initial adversarial example work.

**L∞ Distance**: Maximum coordinate change. "For images, we can imagine there is a maximum budget, and each pixel is allowed to be changed by up to this limit, with no limit on the number of pixels that are modified."

## II-E Defensive Distillation

Distillation trains networks on soft labels from teacher networks. The process uses temperature-adjusted softmax during training:

$$\text{softmax}(x,T)_i = \frac{e^{x_i/T}}{\sum_j e^{x_j/T}}$$

Four-step procedure:
1. Train teacher with temperature $T$
2. Generate soft labels using teacher at temperature $T$
3. Train distilled network on soft labels at temperature $T$
4. Evaluate distilled network at temperature 1

Theory suggests preventing overfitting to training data's adversarial blind spots. However, adversarial examples likely stem from local linearity rather than blind spots, suggesting distillation should not improve robustness.

## II-F Organization

The paper progresses from surveying existing attacks (L-BFGS, Fast Gradient Sign, JSMA, Deepfool) to proposing superior alternatives, then evaluating them against defensive distillation.

---

### النسخة العربية

## II-A نموذج التهديد

يفترض البحث وصول الصندوق الأبيض حيث يمتلك المهاجمون معرفة كاملة بالشبكة بما في ذلك المعمارية والمعاملات. يعكس هذا الافتراض المحافظ الواقع العملي: "أظهر العمل السابق أنه من الممكن تدريب نموذج بديل بالنظر إلى وصول الصندوق الأسود إلى النموذج المستهدف، وبمهاجمة النموذج البديل، يمكننا بعد ذلك نقل هذه الهجمات إلى النموذج المستهدف."

تشمل التطبيقات المعرضة للأمثلة الخصامية المركبات ذاتية القيادة وتصنيف البرمجيات الخبيثة والتعرف على الكلام وأنظمة الطائرات بدون طيار. يصبح السؤال الرئيسي هو تحديد مستويات التشويه المطلوبة عبر المجالات المختلفة باستخدام مقاييس المسافة المناسبة.

## II-B الشبكات العصبية والترميز

يتم صياغة الشبكات كدوال $F(x) = y$ تربط المدخلات بالمخرجات من خلال طبقات مركبة. تنتج دالة softmax توزيعات احتمالية: يمثل $y_i$ احتمالية أن المدخل $x$ ينتمي إلى الفئة $i$، مع $C(x) = \arg\max_i F(x)_i$ التي تعين التسمية المتوقعة.

يميز الترميز بين $F(x)$ (الشبكة الكاملة مع softmax) و $Z(x)$ (اللوجيتات - المخرجات قبل softmax). تتكون الشبكات عادةً من طبقات مكدسة حيث $F_i(x) = \sigma(\theta_i \cdot x) + \hat{\theta}_i$، مع $\sigma$ التي تشير إلى دوال التنشيط (يتم استخدام ReLU بشكل رئيسي).

## II-C الأمثلة الخصامية

يحقق المثال الخصامي $x'$ الشرط $C(x') = t$ حيث $t \neq C^*(x)$، ومع ذلك يبقى قريباً من المدخل الأصلي $x$ تحت مقياس مسافة معين. يفحص البحث ثلاثة أنواع من الهجمات:

- **الحالة المتوسطة**: استهداف فئة غير صحيحة مختارة عشوائياً
- **أفضل حالة**: مهاجمة جميع الفئات غير الصحيحة، الإبلاغ عن الأسهل
- **أسوأ حالة**: مهاجمة جميع الفئات غير الصحيحة، الإبلاغ عن الأصعب

## II-D مقاييس المسافة

تقيس ثلاثة معايير $L_p$ التشابه:

**مسافة L₀**: تحسب الإحداثيات المعدلة. "تتوافق مسافة L₀ مع عدد البكسلات التي تم تغييرها في الصورة." يجادل Papernot وآخرون أن هذا المقياس يلتقط بشكل أفضل ادعاءات الأمان للتقطير الدفاعي.

**مسافة L₂**: المسافة الإقليدية (الجذر التربيعي للمتوسط) بين المتجهات، المستخدمة في عمل الأمثلة الخصامية الأولي.

**مسافة L∞**: الحد الأقصى لتغيير الإحداثيات. "بالنسبة للصور، يمكننا تخيل أن هناك ميزانية قصوى، ويسمح بتغيير كل بكسل حتى هذا الحد، مع عدم وجود حد على عدد البكسلات التي يتم تعديلها."

## II-E التقطير الدفاعي

يدرب التقطير الشبكات على تسميات ناعمة من شبكات معلمة. تستخدم العملية softmax المعدلة بدرجة الحرارة أثناء التدريب:

$$\text{softmax}(x,T)_i = \frac{e^{x_i/T}}{\sum_j e^{x_j/T}}$$

حيث $T$ هي معامل درجة الحرارة.

إجراء من أربع خطوات:
1. تدريب المعلم بدرجة حرارة $T$
2. توليد تسميات ناعمة باستخدام المعلم عند درجة حرارة $T$
3. تدريب الشبكة المقطرة على التسميات الناعمة عند درجة حرارة $T$
4. تقييم الشبكة المقطرة عند درجة حرارة 1

تشير النظرية إلى منع الإفراط في التلاؤم مع النقاط العمياء الخصامية لبيانات التدريب. ومع ذلك، من المحتمل أن تنبع الأمثلة الخصامية من الخطية المحلية بدلاً من النقاط العمياء، مما يشير إلى أن التقطير لا ينبغي أن يحسن المتانة.

## II-F التنظيم

يتقدم البحث من مسح الهجمات الموجودة (L-BFGS، Fast Gradient Sign، JSMA، Deepfool) إلى اقتراح بدائل متفوقة، ثم تقييمها ضد التقطير الدفاعي.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - white-box access (وصول الصندوق الأبيض)
  - black-box access (وصول الصندوق الأسود)
  - substitute model (نموذج بديل)
  - logits (اللوجيتات - kept in transliteration as standard in ML)
  - soft labels (تسميات ناعمة)
  - teacher network (شبكة معلمة)
  - temperature parameter (معامل درجة الحرارة)
  - local linearity (الخطية المحلية)

- **Equations:**
  - Softmax with temperature equation preserved in LaTeX
  - Mathematical notation for functions F(x), Z(x), C(x) preserved
  - Distance metric notation L₀, L₂, L∞ preserved

- **Citations:** Papernot et al. referenced
- **Special handling:**
  - "Adversarial blind spots" translated as "النقاط العمياء الخصامية"
  - Technical attack names (L-BFGS, JSMA, Deepfool) kept in English as standard
  - ReLU kept in English (standard abbreviation)

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88

**Notes:** This section contains critical mathematical foundations. All equations are preserved in LaTeX with Arabic explanations added. The threat model and distance metrics are explained clearly for Arabic-speaking security researchers. The translation maintains technical precision while ensuring readability.
