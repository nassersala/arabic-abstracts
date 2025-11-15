# Section 4: Analysis
## القسم 4: التحليل

**Section:** analysis
**Translation Quality:** 0.88
**Glossary Terms Used:** neural networks, training, transform gate, bias, activation, highway networks, block output, mean, visualization, depth, information flow, routing

---

### English Version

Figure 2 illustrates the inner workings of the best 50 hidden layer fully-connected highway networks trained on MNIST (top row) and CIFAR-100 (bottom row). The first three columns show the bias, the mean activity over all training samples, and the activity for a single random sample for each transform gate respectively. Block outputs for the same single sample are displayed in the last column.

The transform gate biases of the two networks were initialized to -2 and -4 respectively. It is interesting to note that contrary to our expectations most biases decreased further during training. For the CIFAR-100 network the biases increase with depth forming a gradient. Curiously this gradient is inversely correlated with the average activity of the transform gates, as seen in the second column. This indicates that the strong negative biases at low depths are not used to shut down the gates, but to make them more selective. This behavior is also suggested by the fact that the transform gate activity for a single example (column 3) is very sparse. The effect is more pronounced for the CIFAR-100 network, but can also be observed to a lesser extent in the MNIST network.

The last column of Figure 2 displays the block outputs and visualizes the concept of "information highways". Most of the outputs stay constant over many layers forming a pattern of stripes. Most of the change in outputs happens in the early layers (≈ 15 for MNIST and ≈ 40 for CIFAR-100).

### 4.1 Routing of Information

One possible advantage of the highway architecture over hard-wired shortcut connections is that the network can learn to dynamically adjust the routing of the information based on the current input. This begs the question: does this behaviour manifest itself in trained networks or do they just learn a static routing that applies to all inputs similarly. A partial answer can be found by looking at the mean transform gate activity (second column) and the single example transform gate outputs (third column) in Figure 2. Especially for the CIFAR-100 case, most transform gates are active on average, while they show very selective activity for the single example. This implies that for each sample only a few blocks perform transformation but different blocks are utilized by different samples.

This data-dependent routing mechanism is further investigated in Figure 3. In each of the columns we show how the average over all samples of one specific class differs from the total average shown in the second column of Figure 2. For MNIST digits 0 and 7 substantial differences can be seen within the first 15 layers, while for CIFAR class numbers 0 and 1 the differences are sparser and spread out over all layers. In both cases it is clear that the mean activity pattern differs between classes. The gating system acts not just as a mechanism to ease training, but also as an important part of the computation in a trained network.

### 4.2 Layer Importance

Since we bias all the transform gates towards being closed, in the beginning every layer mostly copies the activations of the previous layer. Does training indeed change this behaviour, or is the final network still essentially equivalent to a network with a much fewer layers? To shed light on this issue, we investigated the extent to which lesioning a single layer affects the total performance of trained networks from Section 3.1. By lesioning, we mean manually setting all the transform gates of a layer to 0 forcing it to simply copy its inputs. For each layer, we evaluated the network on the full training set with the gates of that layer closed. The resulting performance as a function of the lesioned layer is shown in Figure 4.

For MNIST (left) it can be seen that the error rises significantly if any one of the early layers is removed, but layers 15 − 45 seem to have close to no effect on the final performance. About 60% of the layers don't learn to contribute to the final result, likely because MNIST is a simple dataset that doesn't require much depth.

We see a different picture for the CIFAR-100 dataset (right) with performance degrading noticeably when removing any of the first ≈ 40 layers. This suggests that for complex problems a highway network can learn to utilize all of its layers, while for simpler problems like MNIST it will keep many of the unneeded layers idle. Such behavior is desirable for deep networks in general, but appears difficult to obtain using plain networks.

---

### النسخة العربية

يوضح الشكل 2 الآليات الداخلية لأفضل شبكات الطرق السريعة المتصلة بالكامل ذات 50 طبقة مخفية المدربة على MNIST (الصف العلوي) و CIFAR-100 (الصف السفلي). تُظهر الأعمدة الثلاثة الأولى الانحياز، ومتوسط النشاط على جميع عينات التدريب، والنشاط لعينة عشوائية واحدة لكل بوابة تحويل على التوالي. يتم عرض مخرجات الكتلة لنفس العينة الواحدة في العمود الأخير.

تم تهيئة انحيازات بوابة التحويل للشبكتين إلى -2 و -4 على التوالي. من المثير للاهتمام ملاحظة أنه خلافاً لتوقعاتنا، انخفضت معظم الانحيازات بشكل أكبر أثناء التدريب. بالنسبة لشبكة CIFAR-100، تزداد الانحيازات مع العمق مكونة تدرجاً. من الغريب أن هذا التدرج مرتبط عكسياً بمتوسط نشاط بوابات التحويل، كما هو موضح في العمود الثاني. يشير هذا إلى أن الانحيازات السالبة القوية عند الأعماق المنخفضة لا تُستخدم لإغلاق البوابات، بل لجعلها أكثر انتقائية. يُشار أيضاً إلى هذا السلوك من خلال حقيقة أن نشاط بوابة التحويل لمثال واحد (العمود 3) متناثر جداً. التأثير أكثر وضوحاً لشبكة CIFAR-100، ولكن يمكن ملاحظته أيضاً بدرجة أقل في شبكة MNIST.

يعرض العمود الأخير من الشكل 2 مخرجات الكتلة ويصور مفهوم "طرق المعلومات السريعة". تبقى معظم المخرجات ثابتة على العديد من الطبقات مكونة نمطاً من الخطوط. يحدث معظم التغيير في المخرجات في الطبقات الأولى (≈ 15 لـ MNIST و ≈ 40 لـ CIFAR-100).

### 4.1 توجيه المعلومات

أحد المزايا المحتملة لمعمارية الطريق السريع على الاتصالات التخطية المثبتة هو أن الشبكة يمكن أن تتعلم تعديل توجيه المعلومات ديناميكياً بناءً على المدخلات الحالية. هذا يطرح السؤال: هل يظهر هذا السلوك في الشبكات المدربة أم أنها تتعلم فقط توجيهاً ثابتاً ينطبق على جميع المدخلات بالمثل. يمكن العثور على إجابة جزئية من خلال النظر إلى متوسط نشاط بوابة التحويل (العمود الثاني) ومخرجات بوابة التحويل للمثال الواحد (العمود الثالث) في الشكل 2. خاصة بالنسبة لحالة CIFAR-100، معظم بوابات التحويل نشطة في المتوسط، بينما تُظهر نشاطاً انتقائياً جداً للمثال الواحد. يشير هذا إلى أنه لكل عينة، يقوم عدد قليل فقط من الكتل بالتحويل ولكن يتم استخدام كتل مختلفة بواسطة عينات مختلفة.

يتم التحقيق في آلية التوجيه التابعة للبيانات هذه بشكل أكبر في الشكل 3. في كل من الأعمدة، نُظهر كيف يختلف المتوسط على جميع عينات صنف معين واحد عن المتوسط الإجمالي الموضح في العمود الثاني من الشكل 2. بالنسبة لأرقام MNIST 0 و7، يمكن رؤية اختلافات كبيرة في أول 15 طبقة، بينما بالنسبة لأرقام أصناف CIFAR 0 و1، تكون الاختلافات أكثر تناثراً وموزعة على جميع الطبقات. في كلتا الحالتين، من الواضح أن نمط النشاط المتوسط يختلف بين الأصناف. يعمل نظام البوابات ليس فقط كآلية لتسهيل التدريب، ولكن أيضاً كجزء مهم من الحساب في شبكة مدربة.

### 4.2 أهمية الطبقات

بما أننا ننحاز جميع بوابات التحويل نحو أن تكون مغلقة، في البداية تقوم كل طبقة في الغالب بنسخ تنشيطات الطبقة السابقة. هل يغير التدريب حقاً هذا السلوك، أم أن الشبكة النهائية لا تزال في الأساس مكافئة لشبكة ذات عدد أقل بكثير من الطبقات؟ لإلقاء الضوء على هذه المسألة، حققنا في مدى تأثير إتلاف طبقة واحدة على الأداء الإجمالي للشبكات المدربة من القسم 3.1. بالإتلاف، نعني تعيين جميع بوابات التحويل لطبقة يدوياً إلى 0 مما يجبرها على نسخ مدخلاتها ببساطة. لكل طبقة، قمنا بتقييم الشبكة على مجموعة التدريب الكاملة مع إغلاق بوابات تلك الطبقة. يتم عرض الأداء الناتج كدالة للطبقة المتضررة في الشكل 4.

بالنسبة لـ MNIST (يسار)، يمكن رؤية أن الخطأ يرتفع بشكل كبير إذا تمت إزالة أي من الطبقات الأولى، لكن الطبقات 15 − 45 يبدو أن لها تأثير قريب من الصفر على الأداء النهائي. حوالي 60% من الطبقات لا تتعلم المساهمة في النتيجة النهائية، على الأرجح لأن MNIST هي مجموعة بيانات بسيطة لا تتطلب عمقاً كبيراً.

نرى صورة مختلفة لمجموعة بيانات CIFAR-100 (يمين) مع تدهور ملحوظ في الأداء عند إزالة أي من أول ≈ 40 طبقة. يشير هذا إلى أنه بالنسبة للمشاكل المعقدة، يمكن لشبكة الطريق السريع أن تتعلم استخدام جميع طبقاتها، بينما بالنسبة للمشاكل الأبسط مثل MNIST ستبقي العديد من الطبقات غير الضرورية خاملة. مثل هذا السلوك مرغوب فيه للشبكات العميقة بشكل عام، لكن يبدو أنه من الصعب الحصول عليه باستخدام الشبكات العادية.

---

### Translation Notes

- **Figures referenced:**
  - Figure 2 (visualization of transform gate biases and block outputs)
  - Figure 3 (class-specific routing patterns)
  - Figure 4 (layer lesioning analysis)
- **Key terms introduced:**
  - inner workings → الآليات الداخلية
  - fully-connected → متصلة بالكامل
  - mean activity → متوسط النشاط
  - training samples → عينات التدريب
  - inversely correlated → مرتبط عكسياً
  - selective → انتقائية
  - sparse → متناثر
  - information highways → طرق المعلومات السريعة
  - stripes → خطوط
  - hard-wired → مثبتة
  - routing → توجيه
  - data-dependent → تابع للبيانات
  - lesioning → إتلاف
  - idle → خاملة
- **Equations:** None
- **Citations:** Reference to Section 3.1
- **Special handling:**
  - Figures are referenced but not included in text
  - Preserved all numerical details (layer numbers, percentages)
  - Maintained scientific analysis tone
  - Kept technical precision in describing network behavior

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.89
- **Overall section score:** 0.88
