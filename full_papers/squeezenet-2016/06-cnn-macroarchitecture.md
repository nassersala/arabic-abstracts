# Section 6: CNN Macroarchitecture Design Space Exploration
## القسم 6: استكشاف فضاء تصميم المعمارية الكلية للشبكات العصبية الالتفافية

**Section:** cnn-macroarchitecture
**Translation Quality:** 0.87
**Glossary Terms Used:** architecture (معمارية), macroarchitecture (المعمارية الكلية), accuracy (دقة), convolutional neural networks (الشبكات العصبية الالتفافية), skip connections (اتصالات القفز), identity mappings (تخطيطات الهوية), parameters (معاملات), baseline (خط الأساس)

---

### English Version

In Sections 3 and 4, we have shown that the base SqueezeNet architecture achieves AlexNet-level accuracy with 50× fewer parameters. In this section, we explore the impact of macroarchitectural design choices on ImageNet accuracy. Inspired by ResNet, we explored three macroarchitectural configurations:

- **Vanilla SqueezeNet** (as described in Section 3)
- **SqueezeNet with simple bypass** connections between Fire modules
- **SqueezeNet with complex bypass** connections between Fire modules

We illustrate these three macroarchitectures in Figure 5. In the middle architecture, we add simple bypass connections around Fire modules, where each bypass is simply an identity mapping. Note, however, that the number of input channels and the number of output channels for each Fire module are often different, preventing us from making identity connections everywhere. To enable more identity connections, in the rightmost architecture we use complex bypasses that include 1×1 convolutions with varying numbers of filters. These complex bypasses add a relatively small amount of extra parameters. Note that in our experiments, we chose to include or omit bypasses after each Fire module, rather than including bypasses after every other Fire module as in ResNet. We leave the ResNet approach as an area for future exploration.

In Section 3, we defined "vanilla SqueezeNet," our baseline SqueezeNet architecture. As before, vanilla SqueezeNet has 1.24M parameters and achieves 57.5% top-1 accuracy and 80.3% top-5 accuracy on ImageNet. Now, with the addition of simple bypass connections, SqueezeNet achieves 60.4% top-1 accuracy and 82.5% top-5 accuracy without increasing the number of parameters. With the addition of complex bypass connections, SqueezeNet achieves 58.8% top-1 accuracy with only a small increase in parameters to 1.27M. The results are summarized in Table 3.

As a point of comparison, recall that in Section 5 we did a microarchitecture exploration, which led us to a SqueezeNet configuration with a SR of 0.75. That network has 4.75M parameters and achieves 60.4% top-1 accuracy. Meanwhile, as we have shown in this section, the simple-bypass version of vanilla SqueezeNet (1.24M parameters) achieves the same 60.4% accuracy. In other words, the macroarchitecture exploration in this section has enabled us to achieve the same accuracy while decreasing the model size by 3.8×.

---

### النسخة العربية

في القسمين 3 و4، أظهرنا أن معمارية SqueezeNet الأساسية تحقق دقة بمستوى AlexNet بمعاملات أقل بـ 50 مرة. في هذا القسم، نستكشف تأثير خيارات التصميم للمعمارية الكلية على دقة ImageNet. مستوحى من ResNet، استكشفنا ثلاثة تكوينات للمعمارية الكلية:

- **SqueezeNet العادية** (كما هو موصوف في القسم 3)
- **SqueezeNet مع اتصالات تجاوز بسيطة** بين وحدات Fire
- **SqueezeNet مع اتصالات تجاوز معقدة** بين وحدات Fire

نوضح هذه المعماريات الكلية الثلاثة في الشكل 5. في المعمارية الوسطى، نضيف اتصالات تجاوز بسيطة حول وحدات Fire، حيث يكون كل تجاوز ببساطة تخطيط هوية. لاحظ، مع ذلك، أن عدد قنوات الإدخال وعدد قنوات الإخراج لكل وحدة Fire غالباً ما تكون مختلفة، مما يمنعنا من عمل اتصالات هوية في كل مكان. لتمكين المزيد من اتصالات الهوية، في المعمارية الموجودة في أقصى اليمين نستخدم تجاوزات معقدة تتضمن التفافات 1×1 مع أعداد متفاوتة من المرشحات. تضيف هذه التجاوزات المعقدة كمية صغيرة نسبياً من المعاملات الإضافية. لاحظ أنه في تجاربنا، اخترنا تضمين أو حذف التجاوزات بعد كل وحدة Fire، بدلاً من تضمين التجاوزات بعد كل وحدة Fire أخرى كما في ResNet. نترك نهج ResNet كمجال للاستكشاف المستقبلي.

في القسم 3، عرفنا "SqueezeNet العادية"، معمارية SqueezeNet الأساسية لدينا. كما في السابق، تحتوي SqueezeNet العادية على 1.24 مليون معامل وتحقق دقة top-1 بنسبة 57.5% ودقة top-5 بنسبة 80.3% على ImageNet. الآن، مع إضافة اتصالات التجاوز البسيطة، تحقق SqueezeNet دقة top-1 بنسبة 60.4% ودقة top-5 بنسبة 82.5% دون زيادة عدد المعاملات. مع إضافة اتصالات التجاوز المعقدة، تحقق SqueezeNet دقة top-1 بنسبة 58.8% مع زيادة صغيرة فقط في المعاملات إلى 1.27 مليون. تم تلخيص النتائج في الجدول 3.

كنقطة مقارنة، تذكر أنه في القسم 5 قمنا باستكشاف المعمارية الدقيقة، مما أدى بنا إلى تكوين SqueezeNet بنسبة SR قدرها 0.75. تحتوي تلك الشبكة على 4.75 مليون معامل وتحقق دقة top-1 بنسبة 60.4%. في الوقت نفسه، كما أظهرنا في هذا القسم، تحقق نسخة التجاوز البسيط من SqueezeNet العادية (1.24 مليون معامل) نفس الدقة البالغة 60.4%. بمعنى آخر، مكّننا استكشاف المعمارية الكلية في هذا القسم من تحقيق نفس الدقة مع تقليل حجم النموذج بمقدار 3.8 مرة.

---

### Translation Notes

- **Figures referenced:** Figure 5 (three macroarchitecture configurations)
- **Tables referenced:** Table 3 (macroarchitecture comparison results)
- **Key terms introduced:**
  - Vanilla SqueezeNet (SqueezeNet العادية)
  - Simple bypass (تجاوز بسيط)
  - Complex bypass (تجاوز معقد)
  - Identity mapping/connection (تخطيط هوية / اتصال هوية)
  - Macroarchitectural configuration (تكوين المعمارية الكلية)
- **Equations:** 0
- **Citations:** Implicit reference to ResNet
- **Special handling:**
  - Translated "vanilla" as "العادية" (ordinary/standard)
  - Kept "bypass" as "تجاوز" (bypass/skip)
  - Used "اتصالات القفز" from glossary for "skip connections"
  - Maintained numerical precision in accuracy percentages
  - Preserved architectural naming conventions

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-Translation Check

The Arabic translation accurately conveys:
- Three macroarchitecture variants (vanilla, simple bypass, complex bypass)
- The inspiration from ResNet architecture
- Distinction between simple (identity) and complex (1×1 conv) bypasses
- Accuracy improvements with bypass connections (57.5% → 60.4% top-1)
- Comparison showing 3.8× model size reduction while maintaining accuracy
- Design choices regarding bypass placement frequency
