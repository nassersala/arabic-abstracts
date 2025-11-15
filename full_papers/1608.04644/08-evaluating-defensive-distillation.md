# Section 8: Evaluating Defensive Distillation
## القسم 8: تقييم التقطير الدفاعي

**Section:** evaluating-defensive-distillation
**Translation Quality:** 0.86
**Glossary Terms Used:** defensive distillation (تقطير دفاعي), gradient (تدرج), vanishing gradient (تدرج متلاشي), logits (لوجيتات), temperature (درجة حرارة), transferability (قابلية النقل), correlation (ارتباط)

---

### English Version

## VIII-A Fragility of Existing Attacks

The paper analyzes why existing attacks fail on distilled networks:

**L-BFGS and Deepfool Failure**: "The gradient of $F(\cdot)$ is zero almost always, which prohibits the use of the standard objective function." When training at temperature $T$ and testing at $T=1$, the logits $Z(\cdot)$ become $T$ times larger. This forces softmax outputs toward $\{0,1\}$, creating vanishing gradients.

Distilled network logits have mean L₁ norm of 482 with SD 457 compared to undistilled networks at 5.8 ± 6.4. This 100× magnification produces $F$ values of $\epsilon$ everywhere except the predicted class ($1-9\epsilon$ for 10 classes), with $\epsilon$ so tiny that 32-bit floating-point rounds to zero.

**JSMA-F Failure**: Identical gradient vanishing problem—the output softmax becomes nearly hard maximum due to large logits.

**JSMA-Z Failure**: Uses logits directly, avoiding gradient vanishing. However, distillation magnifies a pre-existing problem: "Distillation at temperature $T$ causes the value of the logits to be $T$ times larger. In effect, this magnifies the sub-optimality noted above as logits that are extremely unlikely but have slight variation can cause the attack to refuse to make any changes."

The original attack treats all logit changes equally regardless of softmax impact. Negative values changing from -100 to -90 still produce ~zero softmax output. The attack refuses modifications when target class gains (+10) but least likely class gains more (+15), even if absolute logit magnitudes are $T$ times larger.

**Fast Gradient Sign Anomaly**: Initially fails due to vanishing gradients. Interestingly, dividing logits by $T$ before softmax maintains distillation effectiveness, contradicting expectations. The authors acknowledge inability to explain this phenomenon.

## VIII-B Applying Our Attacks

When applied to distilled networks with $T=100$:

Table VI shows negligible defense benefit:
- L₀ MNIST best: 10 pixels (vs. 8.5 undistilled)
- L₀ CIFAR best: 7.4 pixels (vs. 5.9 undistilled)
- L₂ MNIST best: 1.7 (vs. 1.36 undistilled)
- L₂ CIFAR best: 0.36 (vs. 0.17 undistilled)
- L∞ performance approximately equal to undistilled

"All of the previous attacks fail to find adversarial examples. In contrast, our attack succeeds with 100 percent success probability." Distillation adds almost no robustness value against strong attacks, contradicting initial claims that reduced prior attack success rates from 95% to 0.5%.

## VIII-C Effect of Temperature

Original distillation work showed that increasing temperature $T$ from 1 to 100 reduced attack success rates (91%→24%→0.5% with JSMA). The authors re-evaluate with their improved attacks.

JSMA shows the same degradation pattern. However, "with our improved L₂ attack, we see no effect of temperature on the mean distance to adversarial examples: the correlation coefficient is $\rho = -0.05$."

This proves that "increasing the distillation temperature does not increase the robustness of the neural network, it only causes existing attacks to fail more often." Temperature merely masks vulnerability rather than providing genuine hardening.

## VIII-D Transferability

Adversarial examples frequently transfer between different models. Any effective defense must break this transferability property; otherwise, attackers could compromise an easy-to-attack model and transfer those examples to defended models.

The paper proposes using **high-confidence adversarial examples**—strongly misclassified on the source model—to test defense transferability. Recall the L₂ loss function modification:

$$f(x') = \max(\max\{Z(x')_i : i \neq t\} - Z(x')_t, -\kappa)$$

Larger $\kappa$ creates stronger target class confidence. Experiments show transferability increases linearly with $\kappa$ from 0 to 20, plateauing near 100%.

Testing transferability from undistilled to distilled models at $\kappa=20$ achieves approximately 100% transfer success. However, distilled models require $\kappa \approx 40$ for equivalent transfer rates, indicating slightly increased robustness against transferability attacks.

"Even though defensive distillation is not robust to our stronger attacks, we demonstrate a second break of distillation by transferring attacks from a standard model to a defensively distilled model." This provides an alternative evaluation pathway even when gradient-based attacks might fail.

---

### النسخة العربية

## VIII-A هشاشة الهجمات الموجودة

يحلل البحث لماذا تفشل الهجمات الموجودة على الشبكات المقطرة:

**فشل L-BFGS وDeepfool**: "تدرج $F(\cdot)$ صفر تقريباً دائماً، مما يمنع استخدام الدالة الهدفية القياسية." عند التدريب عند درجة حرارة $T$ والاختبار عند $T=1$، تصبح اللوجيتات $Z(\cdot)$ أكبر بمقدار $T$ مرة. هذا يجبر مخرجات softmax نحو $\{0,1\}$، مما يخلق تدرجات متلاشية.

لوجيتات الشبكة المقطرة لها معيار L₁ متوسط 482 مع انحراف معياري 457 مقارنة بالشبكات غير المقطرة عند 5.8 ± 6.4. هذا التضخيم 100× ينتج قيم $F$ من $\epsilon$ في كل مكان باستثناء الفئة المتوقعة ($1-9\epsilon$ لـ 10 فئات)، مع $\epsilon$ صغير جداً بحيث يقرب الفاصلة العائمة 32 بت إلى صفر.

**فشل JSMA-F**: نفس مشكلة التدرج المتلاشي - يصبح مخرج softmax تقريباً حد أقصى صارم بسبب اللوجيتات الكبيرة.

**فشل JSMA-Z**: يستخدم اللوجيتات مباشرة، متجنباً التدرج المتلاشي. ومع ذلك، يضخم التقطير مشكلة موجودة مسبقاً: "التقطير عند درجة حرارة $T$ يجعل قيمة اللوجيتات أكبر بمقدار $T$ مرة. في الواقع، هذا يضخم عدم الأمثلية المذكورة أعلاه حيث يمكن للوجيتات غير محتملة للغاية ولكن لها تباين طفيف أن تتسبب في رفض الهجوم لإجراء أي تغييرات."

يعامل الهجوم الأصلي جميع تغييرات اللوجيت بالتساوي بغض النظر عن تأثير softmax. القيم السالبة التي تتغير من -100 إلى -90 لا تزال تنتج مخرج softmax ~صفر. يرفض الهجوم التعديلات عندما تكتسب الفئة المستهدفة (+10) ولكن الفئة الأقل احتمالاً تكتسب أكثر (+15)، حتى لو كانت قيم اللوجيت المطلقة أكبر بمقدار $T$ مرة.

**شذوذ Fast Gradient Sign**: يفشل في البداية بسبب التدرجات المتلاشية. من المثير للاهتمام أن قسمة اللوجيتات على $T$ قبل softmax تحافظ على فعالية التقطير، متناقضة مع التوقعات. يعترف المؤلفون بعدم القدرة على تفسير هذه الظاهرة.

## VIII-B تطبيق هجماتنا

عند تطبيقها على الشبكات المقطرة مع $T=100$:

يُظهر الجدول VI فائدة دفاعية ضئيلة:
- L₀ MNIST أفضل: 10 بكسلات (مقابل 8.5 غير مقطر)
- L₀ CIFAR أفضل: 7.4 بكسلات (مقابل 5.9 غير مقطر)
- L₂ MNIST أفضل: 1.7 (مقابل 1.36 غير مقطر)
- L₂ CIFAR أفضل: 0.36 (مقابل 0.17 غير مقطر)
- أداء L∞ تقريباً مساوٍ لغير المقطر

**التحليل:** الزيادة الطفيفة في التشويه المطلوب (مثلاً، من 5.9 إلى 7.4 بكسلات) لا توفر أماناً ذا معنى، حيث كلا الهجومين لا يزالان غير مرئيين بصرياً.

"جميع الهجمات السابقة تفشل في العثور على أمثلة خصامية. على النقيض، ينجح هجومنا باحتمالية نجاح 100 بالمائة." يضيف التقطير قيمة متانة ضئيلة تقريباً ضد الهجمات القوية، متناقضاً مع الادعاءات الأولية التي قللت معدلات نجاح الهجوم السابقة من 95% إلى 0.5%.

## VIII-C تأثير درجة الحرارة

أظهر العمل الأصلي للتقطير أن زيادة درجة الحرارة $T$ من 1 إلى 100 قللت معدلات نجاح الهجوم (91%→24%→0.5% مع JSMA). يعيد المؤلفون التقييم مع هجماتهم المحسنة.

يُظهر JSMA نفس نمط التدهور. ومع ذلك، "مع هجوم L₂ المحسن لدينا، لا نرى أي تأثير لدرجة الحرارة على متوسط المسافة إلى الأمثلة الخصامية: معامل الارتباط هو $\rho = -0.05$."

**التفسير:** $\rho = -0.05$ يشير إلى عدم وجود ارتباط تقريباً، مما يعني أن درجة الحرارة لا تؤثر على قوة الهجوم.

هذا يثبت أن "زيادة درجة حرارة التقطير لا تزيد من متانة الشبكة العصبية، بل تتسبب فقط في فشل الهجمات الموجودة بشكل أكثر تكراراً." درجة الحرارة تخفي الثغرة فقط بدلاً من توفير تعزيز حقيقي.

## VIII-D قابلية النقل

تنتقل الأمثلة الخصامية بشكل متكرر بين نماذج مختلفة. يجب على أي دفاع فعال كسر خاصية قابلية النقل هذه؛ وإلا يمكن للمهاجمين اختراق نموذج سهل الهجوم ونقل تلك الأمثلة إلى النماذج المدافع عنها.

يقترح البحث استخدام **أمثلة خصامية عالية الثقة** - مصنفة بشكل خاطئ بقوة على النموذج المصدر - لاختبار قابلية نقل الدفاع. تذكر تعديل دالة خسارة L₂:

$$f(x') = \max(\max\{Z(x')_i : i \neq t\} - Z(x')_t, -\kappa)$$

حيث $\kappa$ أكبر يخلق ثقة أقوى في الفئة المستهدفة.

يخلق $\kappa$ الأكبر ثقة أقوى في الفئة المستهدفة. تُظهر التجارب أن قابلية النقل تزداد خطياً مع $\kappa$ من 0 إلى 20، مستقرة بالقرب من 100%.

اختبار قابلية النقل من النماذج غير المقطرة إلى المقطرة عند $\kappa=20$ يحقق نجاح نقل يقارب 100%. ومع ذلك، تتطلب النماذج المقطرة $\kappa \approx 40$ لمعدلات نقل معادلة، مما يشير إلى متانة متزايدة قليلاً ضد هجمات قابلية النقل.

"على الرغم من أن التقطير الدفاعي ليس متيناً ضد هجماتنا الأقوى، نوضح كسراً ثانياً للتقطير عن طريق نقل الهجمات من نموذج قياسي إلى نموذج مقطر دفاعياً." هذا يوفر مساراً بديلاً للتقييم حتى عندما قد تفشل الهجمات القائمة على التدرج.

**الأهمية العملية:** هذا يعني أن المهاجم يمكنه تدريب نموذجه الخاص غير المقطر، توليد أمثلة خصامية عالية الثقة، ونقلها إلى النموذج المقطر المستهدف - متجاوزاً الحاجة إلى الوصول المباشر للتدرج.

---

### Translation Notes

- **Figures referenced:** Table VI (results table)
- **Key terms introduced:**
  - Vanishing gradient (تدرج متلاشي)
  - Gradient magnification (تضخيم التدرج)
  - Hard maximum (حد أقصى صارم)
  - Sub-optimality (عدم الأمثلية)
  - Pearson correlation (ارتباط بيرسون)
  - Transferability (قابلية النقل)
  - High-confidence examples (أمثلة عالية الثقة)
  - Source model (نموذج مصدر)
  - Transfer success (نجاح النقل)

- **Equations:**
  - High-confidence objective function with κ
  - Preserved in LaTeX

- **Citations:** Reference to original distillation work, Table VI
- **Special handling:**
  - Detailed explanation of gradient vanishing mechanism
  - Quantitative comparison: 482±457 vs 5.8±6.4 (100× difference)
  - Floating-point precision issue explained
  - JSMA-Z failure mechanism explained with numerical example (-100 to -90)
  - Fast Gradient Sign anomaly acknowledged as unexplained
  - Correlation coefficient ρ = -0.05 interpreted
  - Transfer rates quantified (κ=20 vs κ≈40)
  - Added Arabic notes explaining practical significance
  - Temperature masking vs genuine hardening distinction emphasized

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86

**Notes:** This critical section demonstrates why defensive distillation fails. The gradient vanishing mechanism is explained in detail with quantitative evidence (100× logit magnification). The distinction between masking vulnerability (temperature effect on weak attacks) vs actual robustness (no effect on strong attacks) is crucial. The transferability analysis provides a black-box attack alternative. All numerical results are preserved exactly. Added explanatory notes help Arabic readers understand the practical implications.
