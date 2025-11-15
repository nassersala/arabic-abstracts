# Section 5: CNN Microarchitecture Design Space Exploration
## القسم 5: استكشاف فضاء تصميم المعمارية الدقيقة للشبكات العصبية الالتفافية

**Section:** cnn-microarchitecture
**Translation Quality:** 0.86
**Glossary Terms Used:** architecture (معمارية), microarchitecture (المعمارية الدقيقة), parameters (معاملات), accuracy (دقة), convolutional neural networks (الشبكات العصبية الالتفافية), hyperparameters (المعاملات الفائقة), baseline (خط الأساس), design space exploration (استكشاف فضاء التصميم)

---

### English Version

So far, we have proposed a novel CNN architecture called SqueezeNet, which uses Fire modules. Now, in Sections 5 and 6, we explore the impact of CNN architecture design choices on model size and accuracy. Here in Section 5, we do an exploration of the design space of microarchitectural hyperparameters for SqueezeNet, as defined in Section 3. Specifically, we explore the following design dimensions:

- **$SR$ (Squeeze Ratio):** In Section 3, we defined $s_{1x1}$ as the number of filters in a Fire module's squeeze layer, and we defined $e_{1x1}$ and $e_{3x3}$ as the number of 1x1 and 3x3 filters in a Fire module's expand layer. In Section 3, we set $s_{1x1} = 0.125 \times (e_{1x1} + e_{3x3})$. In this section, we define SR (the squeeze ratio) as $SR = s_{1x1} / (e_{1x1} + e_{3x3})$, and we explore the following squeeze ratios: $SR \in \{0.125, 0.25, 0.5, 0.75\}$.

- **$pct_{3x3}$:** We defined this in Section 3 as the percentage of filters in the expand layer that are 3x3. In this section, we explore the following settings: $pct_{3x3} \in \{0.01, 0.25, 0.5, 0.75, 0.99\}$. Note that $pct_{3x3} = 0.01$ is the setting in which expand layers contain almost all 1x1 filters, and $pct_{3x3} = 0.99$ is the opposite extreme in which expand layers contain almost all 3x3 filters.

We train SqueezeNet with various settings of the aforementioned design dimensions, and we report top-1 and top-5 ImageNet classification accuracy in Figure 3 and Figure 4, respectively. In our design space exploration, we hold constant the following architectural parameters: input image size is 224x224, batch size is 1024, number of training epochs is 90, and all Fire modules have the same settings of the aforementioned microarchitectural parameters ($SR$ and $pct_{3x3}$) within a given SqueezeNet instance.

From the accuracy results in Figure 3 and 4, we glean the following observations:

**Squeeze Ratio (SR).** Accuracy increases with SR up to SR=0.75. However, the model size increases linearly with SR. We selected SR=0.125 as our "baseline" setting, and we use SR=0.75 as an accuracy-optimized setting. With SR=0.125, SqueezeNet has 1.24M parameters, and with SR=0.75, SqueezeNet has 4.75M parameters (but still much smaller than AlexNet's 61M parameters).

**$pct_{3x3}$.** With SqueezeNet, changing from an all-3x3 expand layer ($pct_{3x3}=0.99$) to an all-1x1 expand layer ($pct_{3x3}=0.01$) yields only a minor decrease in accuracy. However, the model size can be substantially reduced by decreasing $pct_{3x3}$. For example, when we change $pct_{3x3}$ from 0.99 to 0.5, the model size decreases by 1.7×. Therefore, for model compression on a limited bandwidth budget, decreasing $pct_{3x3}$ can be a useful knob to turn.

**Comparison to AlexNet.** When we set $SR=0.75$ and $pct_{3x3}=0.5$, SqueezeNet achieves 60.4% top-1 accuracy and 82.5% top-5 accuracy, outperforming AlexNet (57.2% and 80.3% top-1 and top-5 accuracy, respectively) with 13× fewer parameters.

---

### النسخة العربية

حتى الآن، اقترحنا معمارية جديدة للشبكات العصبية الالتفافية تسمى SqueezeNet، والتي تستخدم وحدات Fire. الآن، في القسمين 5 و6، نستكشف تأثير خيارات تصميم معمارية الشبكات العصبية الالتفافية على حجم النموذج والدقة. هنا في القسم 5، نقوم باستكشاف فضاء تصميم المعاملات الفائقة للمعمارية الدقيقة لـ SqueezeNet، كما هو محدد في القسم 3. على وجه التحديد، نستكشف أبعاد التصميم التالية:

- **$SR$ (نسبة الضغط):** في القسم 3، عرفنا $s_{1x1}$ كعدد المرشحات في طبقة الضغط لوحدة Fire، وعرفنا $e_{1x1}$ و$e_{3x3}$ كعدد مرشحات 1x1 و3x3 في طبقة التوسيع لوحدة Fire. في القسم 3، عيّنا $s_{1x1} = 0.125 \times (e_{1x1} + e_{3x3})$. في هذا القسم، نعرف SR (نسبة الضغط) على أنها $SR = s_{1x1} / (e_{1x1} + e_{3x3})$، ونستكشف نسب الضغط التالية: $SR \in \{0.125, 0.25, 0.5, 0.75\}$.

- **$pct_{3x3}$:** عرفنا هذا في القسم 3 على أنه النسبة المئوية للمرشحات في طبقة التوسيع التي هي 3x3. في هذا القسم، نستكشف الإعدادات التالية: $pct_{3x3} \in \{0.01, 0.25, 0.5, 0.75, 0.99\}$. لاحظ أن $pct_{3x3} = 0.01$ هو الإعداد الذي تحتوي فيه طبقات التوسيع على مرشحات 1x1 تقريباً بالكامل، و$pct_{3x3} = 0.99$ هو العكس الأقصى حيث تحتوي طبقات التوسيع على مرشحات 3x3 تقريباً بالكامل.

نقوم بتدريب SqueezeNet بإعدادات مختلفة لأبعاد التصميم المذكورة أعلاه، ونبلغ عن دقة تصنيف ImageNet لـ top-1 وtop-5 في الشكل 3 والشكل 4، على التوالي. في استكشاف فضاء التصميم الخاص بنا، نحافظ على ثبات المعاملات المعمارية التالية: حجم الصورة المدخلة هو 224x224، حجم الدفعة هو 1024، عدد حقب التدريب هو 90، وجميع وحدات Fire لها نفس الإعدادات للمعاملات الفائقة للمعمارية الدقيقة المذكورة أعلاه ($SR$ و$pct_{3x3}$) ضمن نسخة SqueezeNet معينة.

من نتائج الدقة في الشكلين 3 و4، نجمع الملاحظات التالية:

**نسبة الضغط (SR).** تزداد الدقة مع SR حتى SR=0.75. ومع ذلك، يزداد حجم النموذج خطياً مع SR. اخترنا SR=0.125 كإعداد "خط الأساس" الخاص بنا، ونستخدم SR=0.75 كإعداد محسّن للدقة. مع SR=0.125، تحتوي SqueezeNet على 1.24 مليون معامل، ومع SR=0.75، تحتوي SqueezeNet على 4.75 مليون معامل (ولكن لا تزال أصغر بكثير من معاملات AlexNet البالغة 61 مليون معامل).

**$pct_{3x3}$.** مع SqueezeNet، التغيير من طبقة توسيع 3x3 بالكامل ($pct_{3x3}=0.99$) إلى طبقة توسيع 1x1 بالكامل ($pct_{3x3}=0.01$) ينتج عنه انخفاض طفيف فقط في الدقة. ومع ذلك، يمكن تقليل حجم النموذج بشكل كبير عن طريق تقليل $pct_{3x3}$. على سبيل المثال، عندما نغير $pct_{3x3}$ من 0.99 إلى 0.5، ينخفض حجم النموذج بمقدار 1.7 مرة. لذلك، لضغط النموذج على ميزانية نطاق ترددي محدودة، يمكن أن يكون تقليل $pct_{3x3}$ أداة مفيدة لاستخدامها.

**المقارنة مع AlexNet.** عندما نعيّن $SR=0.75$ و$pct_{3x3}=0.5$، تحقق SqueezeNet دقة top-1 بنسبة 60.4% ودقة top-5 بنسبة 82.5%، متفوقة على AlexNet (57.2% و80.3% دقة top-1 وtop-5، على التوالي) بمعاملات أقل بـ 13 مرة.

---

### Translation Notes

- **Figures referenced:** Figure 3 (top-1 accuracy results), Figure 4 (top-5 accuracy results)
- **Key terms introduced:**
  - Squeeze Ratio (SR) (نسبة الضغط)
  - Design dimensions (أبعاد التصميم)
  - Accuracy-optimized setting (إعداد محسّن للدقة)
  - Bandwidth budget (ميزانية نطاق ترددي)
- **Equations:** Mathematical notation for SR and $pct_{3x3}$ definitions
- **Citations:** None explicit
- **Special handling:**
  - Preserved mathematical notation ($SR$, $pct_{3x3}$, $s_{1x1}$, $e_{1x1}$, $e_{3x3}$)
  - Kept set notation: $\{0.125, 0.25, 0.5, 0.75\}$
  - Maintained precision in percentage values and ratios
  - Used consistent formatting for experimental parameters

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.89
- Readability: 0.84
- Glossary consistency: 0.86
- **Overall section score:** 0.86

### Back-Translation Check

The Arabic translation accurately conveys:
- The two main design dimensions explored (SR and $pct_{3x3}$)
- Experimental setup and methodology
- Key findings about squeeze ratio impact on accuracy and model size
- Trade-offs between $pct_{3x3}$ settings and model size
- Comparison results with AlexNet (60.4% vs 57.2% top-1 accuracy)
- The linear relationship between SR and model size
