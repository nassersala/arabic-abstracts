# Section 1: Introduction
## القسم 1: المقدمة

**Section:** Introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** artificial intelligence, neural network, machine learning, deep learning, program synthesis, gradient descent, supervised learning, inductive program synthesis, search techniques, framework

---

### English Version

A dream of artificial intelligence is to build systems that can write computer programs. Recently, there has been much interest in program-like neural network models (Graves et al., 2014; Weston et al., 2015; Kurach et al., 2015; Joulin & Mikolov, 2015; Grefenstette et al., 2015; Sukhbaatar et al., 2015; Neelakantan et al., 2016; Kaiser & Sutskever, 2016; Reed & de Freitas, 2016; Zaremba et al., 2016; Graves et al., 2016), but none of these can write programs; that is, they do not generate human-readable source code. Only very recently, Riedel et al. (2016); Bunel et al. (2016); Gaunt et al. (2016) explored the use of gradient descent to induce source code from input-output examples via differentiable interpreters, and Ling et al. (2016) explored the generation of source code from unstructured text descriptions. However, Gaunt et al. (2016) showed that differentiable interpreter-based program induction is inferior to discrete search-based techniques used by the programming languages community. We are then left with the question of how to make progress on program induction using machine learning techniques.

In this work, we propose two main ideas: (1) learn to induce programs; that is, use a corpus of program induction problems to learn strategies that generalize across problems, and (2) integrate neural network architectures with search-based techniques rather than replace them.

In more detail, we can contrast our approach to existing work on differentiable interpreters. In differentiable interpreters, the idea is to define a differentiable mapping from source code and inputs to outputs. After observing inputs and outputs, gradient descent can be used to search for a program that matches the input-output examples. This approach leverages gradient-based optimization, which has proven powerful for training neural networks, but each synthesis problem is still solved independently—solving many synthesis problems does not help to solve the next problem.

We argue that machine learning can provide significant value towards solving Inductive Program Synthesis (IPS) by re-casting the problem as a big data problem. We show that training a neural network on a large number of generated IPS problems to predict cues from the problem description can help a search-based technique. In this work, we focus on predicting an order on the program space and show how to use it to guide search-based techniques that are common in the programming languages community. This approach has three desirable properties: first, we transform a difficult search problem into a supervised learning problem; second, we soften the effect of failures of the neural network by searching over program space rather than relying on a single prediction; and third, the neural network's predictions are used to guide existing program synthesis systems, allowing us to use and improve on the best solvers from the programming languages community. Empirically, we show orders-of-magnitude improvements over optimized standard search techniques and a Recurrent Neural Network-based approach to the problem.

In summary, we define and instantiate a framework for using deep learning for program synthesis problems like ones appearing on programming competition websites. Our concrete contributions are:

1. defining a programming language that is expressive enough to include real-world programming problems while being high-level enough to be predictable from input-output examples;

2. models for mapping sets of input-output examples to program properties; and

3. experiments that show an order of magnitude speedup over standard program synthesis techniques, which makes this approach feasible for solving problems of similar difficulty as the simplest problems that appear on programming competition websites.

---

### النسخة العربية

يتمثل حلم الذكاء الاصطناعي في بناء أنظمة قادرة على كتابة برامج الحاسوب. في الآونة الأخيرة، كان هناك اهتمام كبير بنماذج الشبكات العصبية الشبيهة بالبرامج (Graves وآخرون، 2014؛ Weston وآخرون، 2015؛ Kurach وآخرون، 2015؛ Joulin و Mikolov، 2015؛ Grefenstette وآخرون، 2015؛ Sukhbaatar وآخرون، 2015؛ Neelakantan وآخرون، 2016؛ Kaiser و Sutskever، 2016؛ Reed و de Freitas، 2016؛ Zaremba وآخرون، 2016؛ Graves وآخرون، 2016)، ولكن لا يستطيع أي من هذه النماذج كتابة برامج؛ أي أنها لا تولد كود مصدري قابل للقراءة البشرية. ومؤخراً فقط، استكشف Riedel وآخرون (2016)؛ Bunel وآخرون (2016)؛ Gaunt وآخرون (2016) استخدام الانحدار التدرجي لاستقراء الكود المصدري من أمثلة الإدخال والإخراج عبر مفسرات قابلة للاشتقاق، واستكشف Ling وآخرون (2016) توليد الكود المصدري من أوصاف نصية غير منظمة. ومع ذلك، أظهر Gaunt وآخرون (2016) أن استقراء البرامج القائم على المفسرات القابلة للاشتقاق أدنى من التقنيات القائمة على البحث المنفصل المستخدمة من قبل مجتمع لغات البرمجة. وبالتالي نُترك مع سؤال حول كيفية إحراز تقدم في استقراء البرامج باستخدام تقنيات تعلم الآلة.

في هذا العمل، نقترح فكرتين رئيسيتين: (1) تعلم كيفية استقراء البرامج؛ أي استخدام مدونة من مشاكل استقراء البرامج لتعلم استراتيجيات تعمم عبر المشاكل، و (2) دمج معماريات الشبكات العصبية مع التقنيات القائمة على البحث بدلاً من استبدالها.

وبشكل أكثر تفصيلاً، يمكننا مقارنة نهجنا بالأعمال الموجودة على المفسرات القابلة للاشتقاق. في المفسرات القابلة للاشتقاق، الفكرة هي تحديد تعيين قابل للاشتقاق من الكود المصدري والمدخلات إلى المخرجات. بعد ملاحظة المدخلات والمخرجات، يمكن استخدام الانحدار التدرجي للبحث عن برنامج يطابق أمثلة الإدخال والإخراج. يستفيد هذا النهج من التحسين القائم على التدرج، والذي أثبت قوته في تدريب الشبكات العصبية، لكن كل مشكلة توليد لا تزال تُحل بشكل مستقل - حل العديد من مشاكل التوليد لا يساعد في حل المشكلة التالية.

نحن نجادل بأن تعلم الآلة يمكن أن يوفر قيمة كبيرة نحو حل مشكلة التوليد الاستقرائي للبرامج (Inductive Program Synthesis - IPS) من خلال إعادة صياغة المشكلة كمشكلة بيانات ضخمة. نُظهر أن تدريب شبكة عصبية على عدد كبير من مشاكل IPS المولدة للتنبؤ بإشارات من وصف المشكلة يمكن أن يساعد تقنية قائمة على البحث. في هذا العمل، نركز على التنبؤ بترتيب على فضاء البرامج ونُظهر كيفية استخدامه لتوجيه التقنيات القائمة على البحث الشائعة في مجتمع لغات البرمجة. يتمتع هذا النهج بثلاث خصائص مرغوبة: أولاً، نحوّل مشكلة بحث صعبة إلى مشكلة تعلم موجه؛ ثانياً، نخفف من تأثير إخفاقات الشبكة العصبية من خلال البحث عبر فضاء البرامج بدلاً من الاعتماد على تنبؤ واحد؛ وثالثاً، تُستخدم تنبؤات الشبكة العصبية لتوجيه أنظمة توليد البرامج الموجودة، مما يسمح لنا باستخدام وتحسين أفضل الحلالات من مجتمع لغات البرمجة. تجريبياً، نُظهر تحسينات بمقدار رتب من الحجم مقارنة بتقنيات البحث القياسية المحسنة ونهج قائم على الشبكة العصبية المتكررة.

باختصار، نحدد ونجسد إطار عمل لاستخدام التعلم العميق لمشاكل توليد البرامج مثل تلك الظاهرة على مواقع مسابقات البرمجة. مساهماتنا الملموسة هي:

1. تعريف لغة برمجة تعبيرية بما يكفي لتشمل مشاكل برمجة من العالم الحقيقي بينما تكون عالية المستوى بما يكفي لتكون قابلة للتنبؤ من أمثلة الإدخال والإخراج؛

2. نماذج لتعيين مجموعات من أمثلة الإدخال والإخراج إلى خصائص البرامج؛ و

3. تجارب تُظهر تسريعاً بمقدار رتبة من الحجم مقارنة بتقنيات توليد البرامج القياسية، مما يجعل هذا النهج قابلاً للتطبيق لحل مشاكل بصعوبة مماثلة لأبسط المشاكل التي تظهر على مواقع مسابقات البرمجة.

---

### Translation Notes

- **Key terms introduced:**
  - Inductive Program Synthesis (IPS) = التوليد الاستقرائي للبرامج
  - differentiable interpreter = مفسر قابل للاشتقاق
  - gradient descent = الانحدار التدرجي
  - supervised learning = التعلم الموجه
  - program space = فضاء البرامج
  - search-based techniques = التقنيات القائمة على البحث

- **Citations:** Multiple references cited (Graves et al., Weston et al., Riedel et al., etc.)
- **Special handling:** Preserved all citations in original format; maintained the numbered list structure

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.89
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
