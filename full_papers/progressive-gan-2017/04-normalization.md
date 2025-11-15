# Section 4: Normalization in Generator and Discriminator
## القسم 4: التطبيع في المولد والمميز

**Section:** Methodology - Normalization
**Translation Quality:** 0.87
**Glossary Terms Used:** generator (المولد), discriminator (المميز), normalization (تطبيع), training (تدريب), stability (استقرار), feature vector (متجه ميزات), gradient (تدرج), batch normalization (تطبيع الدفعة), weights (أوزان), activation (تفعيل)

---

### English Version

GAN training is known to be sensitive to the magnitudes of the activations and gradients. To address this, we employ several normalization techniques in both the generator and the discriminator.

**4.1 Equalized Learning Rate**

We deviate from the current trend of careful weight initialization and instead use a trivial N(0,1) initialization and then explicitly scale the weights at runtime. To be precise, we set $\\hat{w}_i = w_i/c$, where $w_i$ are the weights and $c$ is the per-layer normalization constant from He's initializer (He et al., 2015). The benefit of this approach is that the dynamic range of the weights is the same for all layers and does not depend on the layer topology.

This ensures that parameter updates have the same relative magnitude regardless of the layer. In other words, we are effectively using a learning rate that is equalized across all layers. This simple modification has a subtle but important effect on the training dynamics. Typically, when using adaptive optimizers like Adam (Kingma & Ba, 2015), the learning rate is adapted per-parameter based on the magnitude of recent gradients. Our equalization ensures that these adaptations happen on the same scale across all parameters.

**4.2 Pixelwise Feature Vector Normalization in Generator**

To disallow the scenario where the magnitudes in the generator and discriminator spiral out of control as a result of competition, we normalize the feature vector in each pixel to unit length in the generator after each convolutional layer. We use a variant of "local response normalization" (Krizhevsky et al., 2012), but without the parameters that require tuning:

$$b_{x,y} = a_{x,y} / \\sqrt{\\frac{1}{N} \\sum_{j=0}^{N-1} (a_{x,y}^j)^2 + \\epsilon}$$

where $\\epsilon = 10^{-8}$, N is the number of feature maps, and $a_{x,y}$ and $b_{x,y}$ denote the original and normalized feature vector in pixel (x,y), respectively.

This constrains the signal magnitude but does not impose any constraints on the overall statistics of the activations. We find this to be a useful way to prevent the escalation of signal magnitudes in the generator. Similar to minibatch standard deviation, this technique has no learnable parameters and adds negligible computational cost.

**4.3 Implementation Details**

Our normalization approach differs from batch normalization in several ways:

1. **No learned parameters:** Unlike batch normalization, which learns scale and bias parameters, our normalization techniques have no learnable parameters.

2. **No batch statistics:** We do not compute or track running statistics across batches. Each pixel is normalized independently based on its feature vector.

3. **Applied per-pixel:** The normalization is applied to each spatial location independently, rather than globally across the batch.

These design choices make our approach simpler and more stable. We found that batch normalization can sometimes interfere with the adversarial dynamics of GAN training, whereas our simpler approach works reliably across different settings.

**Benefits of normalization.** The combination of equalized learning rate and pixelwise normalization provides several benefits:

1. **Improved stability:** By controlling the magnitude of activations and ensuring balanced learning across layers, we significantly improve training stability.

2. **Prevention of signal explosion:** The pixelwise normalization prevents the common problem where signal magnitudes grow uncontrollably during training.

3. **Faster convergence:** Equalized learning rate ensures that all parameters are updated with similar relative magnitudes, leading to more efficient optimization.

These normalization techniques, combined with progressive growing, form the foundation of our stable and high-quality GAN training methodology.

---

### النسخة العربية

من المعروف أن تدريب شبكات GAN حساس لمقادير التفعيلات والتدرجات. لمعالجة هذا، نستخدم عدة تقنيات تطبيع في كل من المولد والمميز.

**4.1 معدل التعلم المتساوي**

ننحرف عن الاتجاه الحالي للتهيئة الدقيقة للأوزان ونستخدم بدلاً من ذلك تهيئة بسيطة N(0,1) ثم نقوم صراحة بقياس الأوزان في وقت التشغيل. لنكون دقيقين، نحدد $\\hat{w}_i = w_i/c$، حيث $w_i$ هي الأوزان وc هو ثابت التطبيع لكل طبقة من مُهيئ He (He et al., 2015). فائدة هذا النهج هي أن النطاق الديناميكي للأوزان هو نفسه لجميع الطبقات ولا يعتمد على طوبولوجيا الطبقة.

يضمن هذا أن تحديثات المعاملات لها نفس المقدار النسبي بغض النظر عن الطبقة. بعبارة أخرى، نستخدم فعلياً معدل تعلم متساوٍ عبر جميع الطبقات. هذا التعديل البسيط له تأثير دقيق ولكنه مهم على ديناميكيات التدريب. عادةً، عند استخدام محسنات تكيفية مثل Adam (Kingma & Ba, 2015)، يتم تكييف معدل التعلم لكل معامل بناءً على مقدار التدرجات الأخيرة. يضمن تساوينا حدوث هذه التكيفات على نفس المقياس عبر جميع المعاملات.

**4.2 تطبيع متجه الميزات لكل بكسل في المولد**

لمنع السيناريو حيث تخرج المقادير في المولد والمميز عن السيطرة نتيجة للمنافسة، نقوم بتطبيع متجه الميزات في كل بكسل إلى طول الوحدة في المولد بعد كل طبقة التفافية. نستخدم نسخة من "تطبيع الاستجابة المحلي" (Krizhevsky et al., 2012)، ولكن بدون المعاملات التي تتطلب ضبطاً:

$$b_{x,y} = a_{x,y} / \\sqrt{\\frac{1}{N} \\sum_{j=0}^{N-1} (a_{x,y}^j)^2 + \\epsilon}$$

حيث $\\epsilon = 10^{-8}$، وN هو عدد خرائط الميزات، و$a_{x,y}$ و$b_{x,y}$ يشيران إلى متجه الميزات الأصلي والمطبع في البكسل (x,y)، على التوالي.

يقيد هذا مقدار الإشارة لكنه لا يفرض أي قيود على الإحصائيات الإجمالية للتفعيلات. نجد أن هذه طريقة مفيدة لمنع تصاعد مقادير الإشارة في المولد. على غرار الانحراف المعياري للدفعة الصغيرة، هذه التقنية ليس لها معاملات قابلة للتعلم وتضيف تكلفة حسابية ضئيلة.

**4.3 تفاصيل التنفيذ**

يختلف نهج التطبيع الخاص بنا عن تطبيع الدفعة في عدة طرق:

1. **لا توجد معاملات متعلمة:** على عكس تطبيع الدفعة، الذي يتعلم معاملات المقياس والانحياز، تقنيات التطبيع الخاصة بنا ليس لها معاملات قابلة للتعلم.

2. **لا توجد إحصائيات دفعة:** لا نحسب أو نتتبع الإحصائيات الجارية عبر الدفعات. يتم تطبيع كل بكسل بشكل مستقل بناءً على متجه ميزاته.

3. **يطبق لكل بكسل:** يتم تطبيق التطبيع على كل موقع مكاني بشكل مستقل، بدلاً من عالمياً عبر الدفعة.

تجعل خيارات التصميم هذه نهجنا أبسط وأكثر استقراراً. وجدنا أن تطبيع الدفعة يمكن أن يتداخل أحياناً مع الديناميكيات الخصامية لتدريب GAN، بينما يعمل نهجنا الأبسط بشكل موثوق عبر إعدادات مختلفة.

**فوائد التطبيع.** يوفر الجمع بين معدل التعلم المتساوي والتطبيع لكل بكسل عدة فوائد:

1. **تحسين الاستقرار:** من خلال التحكم في مقدار التفعيلات وضمان التعلم المتوازن عبر الطبقات، نحسن بشكل كبير استقرار التدريب.

2. **منع انفجار الإشارة:** يمنع التطبيع لكل بكسل المشكلة الشائعة حيث تنمو مقادير الإشارة بشكل لا يمكن السيطرة عليه أثناء التدريب.

3. **تقارب أسرع:** يضمن معدل التعلم المتساوي تحديث جميع المعاملات بمقادير نسبية مماثلة، مما يؤدي إلى تحسين أكثر كفاءة.

تشكل تقنيات التطبيع هذه، جنباً إلى جنب مع النمو التدريجي، أساس منهجية تدريب GAN المستقرة وعالية الجودة الخاصة بنا.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:**
  - Equalized learning rate (معدل التعلم المتساوي)
  - Pixelwise normalization (التطبيع لكل بكسل)
  - Feature vector normalization (تطبيع متجه الميزات)
  - Local response normalization (تطبيع الاستجابة المحلي)
  - He's initializer (مُهيئ He)
  - Dynamic range (النطاق الديناميكي)
  - Signal magnitude (مقدار الإشارة)
  - Adaptive optimizer (محسن تكيفي)
  - Unit length (طول الوحدة)
- **Equations:** 2 equations (weight scaling and pixelwise normalization)
- **Citations:** He et al. (2015), Kingma & Ba (2015) for Adam, Krizhevsky et al. (2012)
- **Special handling:**
  - Mathematical notation preserved in LaTeX
  - N(0,1) kept as standard notation for normal distribution
  - Greek letter ε kept in original form
  - Technical terms consistently translated according to glossary

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.86
- **Overall section score:** 0.87
