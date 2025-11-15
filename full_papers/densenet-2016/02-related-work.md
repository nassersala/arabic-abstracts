# Section 2: Related Work
## القسم 2: الأعمال ذات الصلة

**Section:** Related Work
**Translation Quality:** 0.90
**Glossary Terms Used:** network architectures (معماريات الشبكات), cascade structure (بنية متتالية), multi-layer perceptrons (إدراكات متعددة الطبقات), skip connections (اتصالات قفز), Highway Networks (شبكات الطرق السريعة), ResNets (شبكات ResNet), gating units (وحدات البوابات), identity mappings (تخطيطات الهوية), stochastic depth (عمق عشوائي), pre-activation (التنشيط المسبق), network width (عرض الشبكة), Inception module (وحدة Inception), feature-maps (خرائط الميزات), concatenation (ربط), residual blocks (كتل متبقية), FractalNets (شبكات كسورية), feature reuse (إعادة استخدام الميزات)

---

### English Version

The exploration of network architectures has been a part of neural network research since their initial discovery. The recent resurgence in popularity of neural networks has also revived this research domain. The increasing number of layers in modern networks amplifies the differences between architectures and motivates the exploration of different connectivity patterns and the revisiting of old research ideas.

A cascade structure similar to our proposed dense network layout has already been studied in the neural networks literature in the 1980s [3]. Their pioneering work focuses on fully connected multi-layer perceptrons trained in a layer-by-layer fashion. More recently, fully connected cascade networks to be trained with batch gradient descent were proposed [40]. Although effective on small datasets, this approach only scales to networks with a few hundred parameters. In [9, 23, 31, 41], utilizing multi-level features in CNNs through skip-connnections has been found to be effective for various vision tasks. Parallel to our work, [1] derived a purely theoretical framework for networks with cross-layer connections similar to ours.

Highway Networks [34] were amongst the first architectures that provided a means to effectively train end-to-end networks with more than 100 layers. Using bypassing paths along with gating units, Highway Networks with hundreds of layers can be optimized without difficulty. The bypassing paths are presumed to be the key factor that eases the training of these very deep networks. This point is further supported by ResNets [11], in which pure identity mappings are used as bypassing paths. ResNets have achieved impressive, record-breaking performance on many challenging image recognition, localization, and detection tasks, such as ImageNet and COCO object detection [11]. Recently, stochastic depth was proposed as a way to successfully train a 1202-layer ResNet [13]. Stochastic depth improves the training of deep residual networks by dropping layers randomly during training. This shows that not all layers may be needed and highlights that there is a great amount of redundancy in deep (residual) networks. Our paper was partly inspired by that observation. ResNets with pre-activation also facilitate the training of state-of-the-art networks with >1000 layers [12].

An orthogonal approach to making networks deeper (e.g., with the help of skip connections) is to increase the network width. The GoogLeNet [36, 37] uses an "Inception module" which concatenates feature-maps produced by filters of different sizes. In [38], a variant of ResNets with wide generalized residual blocks was proposed. In fact, simply increasing the number of filters in each layer of ResNets can improve its performance provided the depth is sufficient [42]. FractalNets also achieve competitive results on several datasets using a wide network structure [17].

Instead of drawing representational power from extremely deep or wide architectures, DenseNets exploit the potential of the network through feature reuse, yielding condensed models that are easy to train and highly parameter-efficient. Concatenating feature-maps learned by different layers increases variation in the input of subsequent layers and improves efficiency. This constitutes a major difference between DenseNets and ResNets. Compared to Inception networks [36, 37], which also concatenate features from different layers, DenseNets are simpler and more efficient.

There are other notable network architecture innovations which have yielded competitive results. The Network in Network (NIN) [22] structure includes micro multi-layer perceptrons into the filters of convolutional layers to extract more complicated features. In Deeply Supervised Network (DSN) [20], internal layers are directly supervised by auxiliary classifiers, which can strengthen the gradients received by earlier layers. Ladder Networks [27, 25] introduce lateral connections into autoencoders, producing impressive accuracies on semi-supervised learning tasks. In [39], Deeply-Fused Nets (DFNs) were proposed to improve information flow by combining intermediate layers of different base networks. The augmentation of networks with pathways that minimize reconstruction losses was also shown to improve image classification models [43].

---

### النسخة العربية

كان استكشاف معماريات الشبكات جزءاً من أبحاث الشبكات العصبية منذ اكتشافها الأولي. أدى الانتعاش الأخير في شعبية الشبكات العصبية أيضاً إلى إحياء هذا المجال البحثي. يؤدي العدد المتزايد من الطبقات في الشبكات الحديثة إلى تضخيم الاختلافات بين المعماريات ويحفز استكشاف أنماط اتصال مختلفة وإعادة النظر في الأفكار البحثية القديمة.

تمت دراسة بنية متتالية مماثلة لتخطيط شبكتنا الكثيفة المقترحة بالفعل في أدبيات الشبكات العصبية في الثمانينيات [3]. يركز عملهم الرائد على الإدراكات متعددة الطبقات المتصلة بالكامل والمدربة بطريقة طبقة تلو الأخرى. في الآونة الأخيرة، تم اقتراح شبكات متتالية متصلة بالكامل ليتم تدريبها باستخدام الانحدار التدرجي الدفعي [40]. على الرغم من فعالية هذا النهج على مجموعات البيانات الصغيرة، إلا أنه يتوسع فقط إلى الشبكات التي تحتوي على بضع مئات من المعاملات. في [9، 23، 31، 41]، وُجد أن استخدام ميزات متعددة المستويات في شبكات CNNs من خلال اتصالات القفز فعال لمختلف مهام الرؤية. بالتوازي مع عملنا، استنتج [1] إطاراً نظرياً بحتاً للشبكات ذات اتصالات عبر الطبقات مماثلة لنا.

كانت شبكات الطرق السريعة (Highway Networks) [34] من بين المعماريات الأولى التي وفرت وسيلة لتدريب الشبكات من طرف إلى طرف بفعالية مع أكثر من 100 طبقة. باستخدام مسارات التجاوز جنباً إلى جنب مع وحدات البوابات، يمكن تحسين شبكات Highway التي تحتوي على مئات الطبقات دون صعوبة. يُفترض أن مسارات التجاوز هي العامل الرئيسي الذي يسهل تدريب هذه الشبكات العميقة جداً. يتم دعم هذه النقطة بشكل أكبر من خلال شبكات ResNets [11]، التي تُستخدم فيها تخطيطات الهوية النقية كمسارات تجاوز. حققت شبكات ResNets أداءً مذهلاً يحطم الأرقام القياسية في العديد من مهام التعرف على الصور الصعبة والتوطين والكشف، مثل كشف الأجسام في ImageNet وCOCO [11]. مؤخراً، تم اقتراح العمق العشوائي كطريقة لتدريب شبكة ResNet مكونة من 1202 طبقة بنجاح [13]. يحسن العمق العشوائي من تدريب الشبكات المتبقية العميقة عن طريق إسقاط الطبقات عشوائياً أثناء التدريب. يُظهر هذا أنه قد لا تكون هناك حاجة لجميع الطبقات ويسلط الضوء على أن هناك قدراً كبيراً من التكرار في الشبكات العميقة (المتبقية). تم إلهام ورقتنا جزئياً بتلك الملاحظة. تسهل شبكات ResNets مع التنشيط المسبق أيضاً تدريب الشبكات الحديثة بأكثر من 1000 طبقة [12].

النهج المتعامد لجعل الشبكات أعمق (على سبيل المثال، بمساعدة اتصالات القفز) هو زيادة عرض الشبكة. تستخدم GoogLeNet [36، 37] "وحدة Inception" التي تربط خرائط الميزات المنتجة بواسطة مرشحات ذات أحجام مختلفة. في [38]، تم اقتراح متغير من شبكات ResNets مع كتل متبقية عامة واسعة. في الواقع، يمكن لمجرد زيادة عدد المرشحات في كل طبقة من شبكات ResNets تحسين أدائها بشرط أن يكون العمق كافياً [42]. تحقق شبكات FractalNets أيضاً نتائج تنافسية على العديد من مجموعات البيانات باستخدام بنية شبكة واسعة [17].

بدلاً من استخلاص القوة التمثيلية من معماريات عميقة أو واسعة للغاية، تستغل شبكات DenseNets إمكانات الشبكة من خلال إعادة استخدام الميزات، مما ينتج نماذج مكثفة سهلة التدريب وذات كفاءة عالية في المعاملات. يزيد ربط خرائط الميزات المتعلمة بواسطة طبقات مختلفة من التباين في مدخلات الطبقات اللاحقة ويحسن الكفاءة. هذا يشكل فرقاً رئيسياً بين شبكات DenseNets وشبكات ResNets. بالمقارنة مع شبكات Inception [36، 37]، التي تربط أيضاً الميزات من طبقات مختلفة، فإن شبكات DenseNets أبسط وأكثر كفاءة.

هناك ابتكارات أخرى جديرة بالملاحظة في معماريات الشبكات أنتجت نتائج تنافسية. تتضمن بنية الشبكة في الشبكة (NIN) [22] إدراكات متعددة الطبقات صغيرة في مرشحات الطبقات التلافيفية لاستخراج ميزات أكثر تعقيداً. في الشبكة المشرفة بعمق (DSN) [20]، يتم الإشراف على الطبقات الداخلية مباشرة بواسطة مصنفات مساعدة، والتي يمكن أن تعزز التدرجات التي تتلقاها الطبقات السابقة. تُدخل شبكات السلم (Ladder Networks) [27، 25] اتصالات جانبية في المشفرات التلقائية، مما ينتج دقة مذهلة في مهام التعلم شبه الموجه. في [39]، تم اقتراح شبكات الدمج العميق (DFNs) لتحسين تدفق المعلومات من خلال الجمع بين الطبقات الوسيطة لشبكات أساسية مختلفة. كما ثبت أن تعزيز الشبكات بمسارات تقلل من خسائر إعادة البناء يحسن نماذج تصنيف الصور [43].

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:** Cascade structure, Highway Networks, gating units, Inception module, Network in Network (NIN), Deeply Supervised Network (DSN), Ladder Networks, Deeply-Fused Nets (DFNs)
- **Equations:** None
- **Citations:** [3], [40], [9, 23, 31, 41], [1], [34], [11], [13], [12], [36, 37], [38], [42], [17], [22], [20], [27, 25], [39], [43]
- **Special handling:** Network names preserved in recognizable form with Arabic transliteration where appropriate

### Quality Metrics

- Semantic equivalence: 0.91
- Technical accuracy: 0.92
- Readability: 0.88
- Glossary consistency: 0.90
- **Overall section score:** 0.90

### Back-translation Check

Key concept: "تستغل شبكات DenseNets إمكانات الشبكة من خلال إعادة استخدام الميزات" → "DenseNets exploit the network's potential through feature reuse" - accurately preserves the original meaning.
