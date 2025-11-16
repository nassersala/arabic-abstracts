# Section 2: Established Formal Methods
## القسم 2: الأساليب الرسمية الراسخة

**Section:** Background / Established Formal Methods
**Translation Quality:** 0.87
**Glossary Terms Used:** formal methods, formal verification, abstract interpretation, avionic software, certification, soundness, static analysis, model checking, theorem proving

---

### English Version

## 2. Established Formal Methods and Safety-Critical Systems

Formal methods have a rich history spanning several decades of research and industrial application. They encompass a range of mathematical techniques for specifying, developing, and verifying systems to ensure they meet their requirements. In safety-critical domains—where failures can lead to loss of life, environmental damage, or significant economic impact—formal methods have become indispensable tools in certification processes.

### 2.1 Overview of Formal Methods

Formal methods can be broadly categorized into several families of techniques:

**Model Checking** systematically explores all possible states of a system model to verify that specified properties hold. While powerful for finite-state systems, model checking faces state explosion problems that limit scalability to large systems.

**Theorem Proving** uses interactive or automated proof assistants to construct mathematical proofs of system correctness. This approach offers maximum generality and precision but typically requires significant expert effort and does not scale automatically.

**Static Analysis** examines program code without executing it, using techniques from programming language theory to infer properties about runtime behavior. Static analysis methods vary in their precision-performance tradeoffs, with abstract interpretation providing a particularly successful framework.

### 2.2 Abstract Interpretation

Abstract interpretation, introduced by Patrick and Radhia Cousot in 1977, provides a theoretical framework for sound approximation of program semantics. The key insight is to execute programs not with concrete values but with abstract values representing sets of possible concrete values.

An **abstract domain** defines:
- A set of abstract values (e.g., intervals for representing sets of numbers)
- Abstract operations that safely overapproximate concrete operations
- Abstraction and concretization functions connecting concrete and abstract semantics

The fundamental soundness guarantee of abstract interpretation ensures that if the analysis proves a property in the abstract domain, that property holds for all possible concrete executions. This makes abstract interpretation particularly suitable for safety-critical verification.

For example, to verify that a variable `x` never exceeds 100, an interval abstract domain might track that `x ∈ [0, 100]`. If this invariant is maintained throughout the analysis, we have a sound proof that `x ≤ 100` in all executions.

Abstract interpretation's key advantage is scalability: by trading precision for performance through carefully designed abstract domains, it can handle large industrial programs. The tradeoff is that overapproximation may lead to false alarms—the analysis may report potential violations that cannot actually occur.

### 2.3 Formal Methods in Avionic Software

The aviation industry represents a mature application domain for formal methods, driven by stringent safety requirements. Aircraft software must be certified according to standards such as DO-178C (Software Considerations in Airborne Systems and Equipment Certification), which defines development and verification processes based on criticality levels.

For the most critical software (Level A - software whose failure could cause catastrophic consequences), DO-178C mandates extensive verification activities including:
- Requirements-based testing
- Structural coverage analysis
- Formal methods (encouraged but not strictly required)

Major aircraft manufacturers and suppliers increasingly use abstract interpretation tools such as Astrée and Polyspace to verify absence of runtime errors (division by zero, buffer overflows, arithmetic overflows) in flight control software. These tools have successfully analyzed programs with hundreds of thousands of lines of code, proving absence of specified error classes with zero false alarms—a remarkable achievement demonstrating the maturity of abstract interpretation technology.

Other formal methods applications in avionics include:
- **Model checking** for verifying state machines in control logic
- **Formal specification languages** like SCADE for designing certified systems
- **Theorem proving** for verifying critical algorithms

### 2.4 The Golden Standard for ML Verification

The success of formal methods in avionic software establishes high expectations for ML verification:

1. **Complete Automation**: Analysis should run automatically without requiring expert intervention or manual proof construction.

2. **Scalability**: Tools must handle industrial-scale systems with millions of lines of code (or millions of neural network parameters).

3. **Zero False Alarms**: For adoption in certification, tools should eliminate false positives through careful tuning, even if this requires domain-specific customization.

4. **Sound Guarantees**: Verification must provide mathematical certainty, not statistical confidence—a proven property must hold for all possible inputs.

5. **Integration**: Formal methods must integrate into existing development workflows and toolchains.

This standard sets a high bar for ML verification research. While neural networks differ fundamentally from traditional software, the aerospace industry's successful application of formal methods demonstrates that rigorous verification of complex critical systems is achievable. The question is whether similar success can be replicated for machine learning systems.

The following sections examine attempts to meet this challenge, surveying verification techniques specifically developed for neural networks and other ML methods.

---

### النسخة العربية

## 2. الأساليب الرسمية الراسخة والأنظمة الحرجة من حيث السلامة

للأساليب الرسمية تاريخ غني يمتد عبر عدة عقود من البحث والتطبيق الصناعي. تشمل مجموعة من التقنيات الرياضية لتحديد وتطوير والتحقق من الأنظمة لضمان تلبيتها لمتطلباتها. في المجالات الحرجة من حيث السلامة—حيث يمكن أن تؤدي الإخفاقات إلى فقدان الأرواح أو الضرر البيئي أو التأثير الاقتصادي الكبير—أصبحت الأساليب الرسمية أدوات لا غنى عنها في عمليات الاعتماد.

### 2.1 نظرة عامة على الأساليب الرسمية

يمكن تصنيف الأساليب الرسمية على نطاق واسع إلى عدة عائلات من التقنيات:

**فحص النماذج** يستكشف بشكل منهجي جميع الحالات الممكنة لنموذج النظام للتحقق من أن الخصائص المحددة صحيحة. بينما يكون قوياً للأنظمة ذات الحالة المحدودة، يواجه فحص النماذج مشاكل انفجار الحالات التي تحد من قابلية التوسع للأنظمة الكبيرة.

**إثبات النظريات** يستخدم مساعدي الإثبات التفاعليين أو الآليين لبناء براهين رياضية لصحة النظام. يوفر هذا النهج أقصى قدر من العمومية والدقة ولكنه يتطلب عادة جهداً كبيراً من الخبراء ولا يتوسع تلقائياً.

**التحليل الثابت** يفحص كود البرنامج دون تنفيذه، باستخدام تقنيات من نظرية لغات البرمجة لاستنتاج الخصائص حول سلوك وقت التشغيل. تختلف أساليب التحليل الثابت في مقايضاتها بين الدقة والأداء، مع توفير التفسير المجرد إطاراً ناجحاً بشكل خاص.

### 2.2 التفسير المجرد

يوفر التفسير المجرد، الذي قدمه باتريك ورادية كوزو في عام 1977، إطاراً نظرياً للتقريب السليم لدلالات البرنامج. الفكرة الرئيسية هي تنفيذ البرامج ليس بقيم محددة ولكن بقيم مجردة تمثل مجموعات من القيم المحددة الممكنة.

يحدد **النطاق المجرد**:
- مجموعة من القيم المجردة (على سبيل المثال، الفترات لتمثيل مجموعات الأرقام)
- العمليات المجردة التي تقرب بأمان العمليات المحددة بشكل زائد
- دوال التجريد والتجسيد التي تربط الدلالات المحددة والمجردة

يضمن ضمان السلامة المنطقية الأساسي للتفسير المجرد أنه إذا أثبت التحليل خاصية في النطاق المجرد، فإن هذه الخاصية تنطبق على جميع التنفيذات المحددة الممكنة. وهذا يجعل التفسير المجرد مناسباً بشكل خاص للتحقق الحرج من حيث السلامة.

على سبيل المثال، للتحقق من أن متغير `x` لا يتجاوز أبداً 100، قد يتتبع نطاق الفترة المجردة أن `x ∈ [0, 100]`. إذا تم الحفاظ على هذا الثابت طوال التحليل، فلدينا إثبات سليم على أن `x ≤ 100` في جميع التنفيذات.

الميزة الرئيسية للتفسير المجرد هي قابلية التوسع: من خلال تبادل الدقة بالأداء من خلال نطاقات مجردة مصممة بعناية، يمكنه التعامل مع البرامج الصناعية الكبيرة. المقايضة هي أن التقريب الزائد قد يؤدي إلى إنذارات كاذبة—قد يبلغ التحليل عن انتهاكات محتملة لا يمكن أن تحدث فعلياً.

### 2.3 الأساليب الرسمية في برمجيات الطيران

تمثل صناعة الطيران مجال تطبيق ناضج للأساليب الرسمية، مدفوعاً بمتطلبات السلامة الصارمة. يجب اعتماد برامج الطائرات وفقاً لمعايير مثل DO-178C (اعتبارات البرمجيات في أنظمة ومعدات الطيران)، والتي تحدد عمليات التطوير والتحقق بناءً على مستويات الحرج.

بالنسبة للبرمجيات الأكثر أهمية (المستوى A - البرمجيات التي يمكن أن يتسبب فشلها في عواقب كارثية)، تفرض DO-178C أنشطة تحقق واسعة النطاق بما في ذلك:
- الاختبار القائم على المتطلبات
- تحليل التغطية الهيكلية
- الأساليب الرسمية (مشجعة ولكن غير مطلوبة بشكل صارم)

يستخدم كبار مصنعي الطائرات والموردين بشكل متزايد أدوات التفسير المجرد مثل Astrée و Polyspace للتحقق من عدم وجود أخطاء وقت التشغيل (القسمة على صفر، فيضانات المخزن المؤقت، فيضانات حسابية) في برامج التحكم في الطيران. نجحت هذه الأدوات في تحليل البرامج التي تحتوي على مئات الآلاف من أسطر الكود، مما أثبت عدم وجود فئات خطأ محددة بدون إنذارات كاذبة—إنجاز ملحوظ يوضح نضج تكنولوجيا التفسير المجرد.

تشمل تطبيقات الأساليب الرسمية الأخرى في الطيران:
- **فحص النماذج** للتحقق من آلات الحالة في منطق التحكم
- **لغات المواصفات الرسمية** مثل SCADE لتصميم الأنظمة المعتمدة
- **إثبات النظريات** للتحقق من الخوارزميات الحرجة

### 2.4 المعيار الذهبي للتحقق من تعلم الآلة

يضع نجاح الأساليب الرسمية في برمجيات الطيران توقعات عالية للتحقق من تعلم الآلة:

1. **الأتمتة الكاملة**: يجب أن يعمل التحليل تلقائياً دون الحاجة إلى تدخل خبير أو بناء إثبات يدوي.

2. **قابلية التوسع**: يجب أن تتعامل الأدوات مع الأنظمة على نطاق صناعي بملايين الأسطر من التعليمات البرمجية (أو ملايين معاملات الشبكة العصبية).

3. **صفر إنذارات كاذبة**: للاعتماد في الاعتماد، يجب أن تقضي الأدوات على الإيجابيات الكاذبة من خلال الضبط الدقيق، حتى لو تطلب ذلك تخصيصاً خاصاً بالمجال.

4. **ضمانات سليمة**: يجب أن يوفر التحقق اليقين الرياضي، وليس الثقة الإحصائية—يجب أن تنطبق الخاصية المثبتة على جميع المدخلات الممكنة.

5. **التكامل**: يجب أن تتكامل الأساليب الرسمية في سير عمل التطوير وسلاسل الأدوات الحالية.

يضع هذا المعيار معياراً عالياً لأبحاث التحقق من تعلم الآلة. بينما تختلف الشبكات العصبية بشكل أساسي عن البرمجيات التقليدية، فإن التطبيق الناجح لصناعة الطيران للأساليب الرسمية يوضح أن التحقق الصارم من الأنظمة الحرجة المعقدة قابل للتحقيق. السؤال هو ما إذا كان يمكن تكرار نجاح مماثل لأنظمة تعلم الآلة.

تفحص الأقسام التالية محاولات مواجهة هذا التحدي، مستعرضة تقنيات التحقق المطورة خصيصاً للشبكات العصبية وأساليب تعلم الآلة الأخرى.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Model checking (فحص النماذج)
  - Theorem proving (إثبات النظريات)
  - Static analysis (التحليل الثابت)
  - Abstract domain (النطاق المجرد)
  - Overapproximation (التقريب الزائد)
  - DO-178C (standard name kept)
  - Astrée, Polyspace (tool names kept)
  - SCADE (language name kept)
  - False alarms (إنذارات كاذبة)
- **Equations:** Set notation: x ∈ [0, 100], x ≤ 100
- **Citations:** Historical reference to Cousot 1977
- **Special handling:** Maintained technical precision for formal methods terminology

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.85
- Glossary consistency: 0.88
- **Overall section score:** 0.87

### Back-Translation Check (Key Paragraph)

Arabic → English: "Abstract interpretation provides a theoretical framework for sound approximation of program semantics. The key idea is to execute programs not with concrete values but with abstract values representing sets of possible concrete values."

✓ Semantically equivalent to original
