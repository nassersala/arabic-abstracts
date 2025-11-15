# Section 2: Model Architectures
## القسم 2: معماريات النماذج

**Section:** model-architectures
**Translation Quality:** 0.87
**Glossary Terms Used:** neural network, architecture, feedforward, recurrent, hidden layer, activation function, softmax, projection layer, embedding, computational complexity, continuous bag-of-words, skip-gram

---

### English Version

Many different types of models were proposed for estimating continuous representations of words, including the well-known Latent Semantic Analysis (LSA) and Latent Dirichlet Allocation (LDA). In this paper, we focus on distributed representations of words learned by neural networks, as it was previously shown that they perform significantly better than LSA for preserving linear regularities among words [20, 31]; LDA moreover becomes computationally very expensive on large data sets.

#### 2.1 Feedforward Neural Net Language Model (NNLM)

The probabilistic feedforward neural network language model has been proposed in [1]. It has been shown that the neural network language model achieves better performance than the widely used N-gram models. The NNLM architecture consists of input, projection, hidden and output layers. At the input layer, N previous words are encoded using 1-of-V coding, where V is the size of the vocabulary. The input layer is then projected to a projection layer P that has dimensionality N × D, using a shared projection matrix. As only N inputs are active at any given time, composition of the projection layer is a relatively cheap operation.

The NNLM architecture becomes complex for computation between the projection and the hidden layer, as values in the projection layer are dense. For a common choice of N = 10, the size of the projection layer (P) might be 500 to 2000, while the hidden layer size H is typically 500 to 1000 units. Moreover, the hidden layer is used to compute probability distribution over all the words in the vocabulary, resulting in an output layer with dimensionality V. Thus, the computational complexity per each training example is

$$Q = N × D + N × D × H + H × V$$

where the dominating term is $H × V$. However, several practical solutions were proposed for avoiding it; either using hierarchical versions of the softmax [25, 23, 18], or avoiding normalized models completely by using models that are not normalized during training [4, 9]. With binary tree representations of the vocabulary, the number of output units that need to be evaluated can go down to around $\log_2(V)$. Thus, most of the complexity is caused by the term $N × D × H$.

#### 2.2 Recurrent Neural Net Language Model (RNNLM)

Recurrent neural network based language model has been proposed to overcome certain limitations of the feedforward NNLM, such as the need to specify the context length (the order N), and because theoretically RNNs can efficiently represent more complex patterns than the shallow neural networks [15, 2]. The RNN model does not have a projection layer; only input, hidden and output layer. What is special for this type of model is the recurrent matrix that connects hidden layer to itself, using time-delayed connections. This allows the recurrent model to form some kind of short term memory, as information from the past can be represented by the hidden layer state that gets updated based on the current input and the state of the hidden layer in the previous time step.

The complexity per training example of the RNN model is

$$Q = H × H + H × V$$

where the word representations D have the same dimensionality as the hidden layer H. Again, the term $H × V$ can be efficiently reduced to $H × \log_2(V)$ by using hierarchical softmax. Most of the complexity then comes from $H × H$.

#### 2.3 Parallel Training of Neural Networks

To train models on huge data sets, we have implemented several models on top of a large-scale distributed framework called DistBelief [6], including the feedforward NNLM and the new models proposed in this paper. The framework allows us to run multiple replicas of the same model in parallel, and each replica synchronizes its gradient updates through a centralized server that keeps all the parameters. For this parallel training, we use mini-batch asynchronous gradient descent with an adaptive learning rate procedure called Adagrad [7]. Under this framework, it is common to use one hundred or more model replicas, each using many CPU cores at different machines in a data center.

#### 2.4 New Log-linear Models

In this section, we propose two new model architectures for learning distributed representations of words that try to minimize computational complexity. The main observation from the previous section was that most of the complexity is caused by the non-linear hidden layer in the model. While this is what makes neural networks so attractive, we decided to explore simpler models that might not be able to represent the data as precisely as neural networks, but can possibly be trained on much more data efficiently.

The new architectures directly follow those proposed in our earlier work [13, 14], where it was found that neural network language model can be successfully trained in two steps: first, continuous word vectors are learned using simple model, and then the N-gram NNLM is trained on top of these distributed representations of words. While there has been later substantial amount of work that focuses on learning word vectors, we consider the approach proposed in [13] to be the simplest one. Note that related models have been proposed also much earlier [16, 26].

##### 2.4.1 Continuous Bag-of-Words Model

The first proposed architecture is similar to the feedforward NNLM, where the non-linear hidden layer is removed and the projection layer is shared for all words (not just the projection matrix); thus all words get projected into the same position (their vectors are averaged). We call this architecture a bag-of-words model as the order of words in the history does not influence the projection. Furthermore, we also use words from the future; we have obtained the best performance on the task introduced in the next section by building a log-linear classifier with four future and four history words at the input, where the training criterion is to correctly classify the current (middle) word. Training complexity is then

$$Q = N × D + D × \log_2(V)$$

We denote this model further as CBOW, as unlike standard bag-of-words model, it uses continuous distributed representation of the context. The model architecture is shown at Figure 1.

##### 2.4.2 Continuous Skip-gram Model

The second architecture is similar to CBOW, but instead of predicting the current word based on the context, it tries to maximize classification of a word based on another word in the same sentence. More precisely, we use each current word as an input to a log-linear classifier with continuous projection layer, and predict words within a certain range before and after the current word. We found that increasing the range improves quality of the resulting word vectors, but it also increases the computational complexity. Since the more distant words are usually less related to the current word than those close to it, we give less weight to the distant words by sampling less from those words in our training examples.

The training complexity of this architecture is proportional to

$$Q = C × (D + D × \log_2(V))$$

where C is the maximum distance of the words. Thus, if we choose C = 5, then for each training word we will select randomly a number R in range $\langle 1; C \rangle$, and then use R words from history and R words from the future of the current word as correct labels. This will require us to do $R × 2$ word classifications, with the current word as input, and each of the $R + R$ words as output. In the following experiments, we use C = 10.

---

### النسخة العربية

تم اقتراح العديد من الأنواع المختلفة من النماذج لتقدير التمثيلات المستمرة للكلمات، بما في ذلك تحليل الدلالة الكامنة (LSA) المعروف وتخصيص ديريشليه الكامن (LDA). في هذه الورقة، نركز على التمثيلات الموزعة للكلمات المتعلمة بواسطة الشبكات العصبية، حيث تم إظهار سابقاً أنها تؤدي بشكل أفضل بكثير من LSA للحفاظ على الانتظامات الخطية بين الكلمات [20، 31]؛ علاوة على ذلك، يصبح LDA مكلفاً حسابياً للغاية على مجموعات البيانات الكبيرة.

#### 2.1 نموذج اللغة العصبي بالتغذية الأمامية (NNLM)

تم اقتراح نموذج اللغة العصبي الاحتمالي بالتغذية الأمامية في [1]. وقد ثبت أن نموذج اللغة العصبي يحقق أداءً أفضل من نماذج N-gram المستخدمة على نطاق واسع. تتكون معمارية NNLM من طبقات الإدخال والإسقاط والمخفية والإخراج. في طبقة الإدخال، يتم ترميز N من الكلمات السابقة باستخدام ترميز 1-من-V، حيث V هو حجم المفردات. ثم يتم إسقاط طبقة الإدخال إلى طبقة إسقاط P ذات أبعاد N × D، باستخدام مصفوفة إسقاط مشتركة. نظراً لأن N من المدخلات فقط تكون نشطة في أي وقت معين، فإن تكوين طبقة الإسقاط هو عملية رخيصة نسبياً.

تصبح معمارية NNLM معقدة للحساب بين طبقة الإسقاط والطبقة المخفية، حيث أن القيم في طبقة الإسقاط كثيفة. للاختيار الشائع N = 10، قد يكون حجم طبقة الإسقاط (P) من 500 إلى 2000، بينما يكون حجم الطبقة المخفية H عادةً من 500 إلى 1000 وحدة. علاوة على ذلك، تُستخدم الطبقة المخفية لحساب توزيع الاحتمالات على جميع الكلمات في المفردات، مما يؤدي إلى طبقة إخراج بأبعاد V. وبالتالي، فإن التعقيد الحسابي لكل مثال تدريب هو

$$Q = N × D + N × D × H + H × V$$

حيث الحد المهيمن هو $H × V$. ومع ذلك، تم اقتراح العديد من الحلول العملية لتجنبه؛ إما باستخدام إصدارات هرمية من softmax [25، 23، 18]، أو تجنب النماذج المطبعة تماماً باستخدام نماذج غير مطبعة أثناء التدريب [4، 9]. مع تمثيلات الشجرة الثنائية للمفردات، يمكن أن ينخفض عدد وحدات الإخراج التي يجب تقييمها إلى حوالي $\log_2(V)$. وبالتالي، فإن معظم التعقيد ناتج عن الحد $N × D × H$.

#### 2.2 نموذج اللغة العصبي المتكرر (RNNLM)

تم اقتراح نموذج اللغة القائم على الشبكة العصبية المتكررة للتغلب على قيود معينة في NNLM بالتغذية الأمامية، مثل الحاجة إلى تحديد طول السياق (الترتيب N)، ولأن الشبكات العصبية المتكررة نظرياً يمكنها تمثيل أنماط أكثر تعقيداً بكفاءة من الشبكات العصبية الضحلة [15، 2]. لا يحتوي نموذج RNN على طبقة إسقاط؛ فقط طبقات الإدخال والمخفية والإخراج. ما يميز هذا النوع من النماذج هو المصفوفة المتكررة التي تربط الطبقة المخفية بنفسها، باستخدام اتصالات متأخرة زمنياً. يسمح هذا للنموذج المتكرر بتشكيل نوع من الذاكرة قصيرة المدى، حيث يمكن تمثيل المعلومات من الماضي بواسطة حالة الطبقة المخفية التي يتم تحديثها بناءً على الإدخال الحالي وحالة الطبقة المخفية في الخطوة الزمنية السابقة.

التعقيد لكل مثال تدريب لنموذج RNN هو

$$Q = H × H + H × V$$

حيث تمثيلات الكلمات D لها نفس أبعاد الطبقة المخفية H. مرة أخرى، يمكن تقليل الحد $H × V$ بكفاءة إلى $H × \log_2(V)$ باستخدام softmax الهرمي. معظم التعقيد يأتي من $H × H$.

#### 2.3 التدريب المتوازي للشبكات العصبية

لتدريب النماذج على مجموعات بيانات ضخمة، قمنا بتنفيذ عدة نماذج على إطار عمل موزع واسع النطاق يسمى DistBelief [6]، بما في ذلك NNLM بالتغذية الأمامية والنماذج الجديدة المقترحة في هذه الورقة. يسمح لنا إطار العمل بتشغيل نسخ متعددة من نفس النموذج بالتوازي، وكل نسخة تزامن تحديثات التدرج الخاصة بها من خلال خادم مركزي يحتفظ بجميع المعاملات. لهذا التدريب المتوازي، نستخدم الانحدار التدرجي اللامتزامن بالدفعات الصغيرة مع إجراء معدل تعلم تكيفي يسمى Adagrad [7]. في ظل هذا الإطار، من الشائع استخدام مائة نسخة من النموذج أو أكثر، كل منها يستخدم العديد من نوى المعالجة المركزية على أجهزة مختلفة في مركز البيانات.

#### 2.4 نماذج لوغاريتمية خطية جديدة

في هذا القسم، نقترح معماريتين نموذجيتين جديدتين لتعلم التمثيلات الموزعة للكلمات التي تحاول تقليل التعقيد الحسابي. الملاحظة الرئيسية من القسم السابق كانت أن معظم التعقيد ناتج عن الطبقة المخفية غير الخطية في النموذج. في حين أن هذا هو ما يجعل الشبكات العصبية جذابة للغاية، قررنا استكشاف نماذج أبسط قد لا تكون قادرة على تمثيل البيانات بدقة مثل الشبكات العصبية، ولكن يمكن تدريبها بكفاءة على بيانات أكثر بكثير.

تتبع المعماريات الجديدة مباشرة تلك المقترحة في عملنا السابق [13، 14]، حيث تم اكتشاف أن نموذج اللغة العصبي يمكن تدريبه بنجاح على خطوتين: أولاً، يتم تعلم متجهات الكلمات المستمرة باستخدام نموذج بسيط، ثم يتم تدريب NNLM من نوع N-gram على هذه التمثيلات الموزعة للكلمات. في حين كان هناك قدر كبير من العمل اللاحق الذي يركز على تعلم متجهات الكلمات، نعتبر النهج المقترح في [13] الأبسط. لاحظ أن النماذج ذات الصلة تم اقتراحها أيضاً في وقت مبكر [16، 26].

##### 2.4.1 نموذج الكيس المستمر للكلمات

المعمارية الأولى المقترحة مماثلة لـ NNLM بالتغذية الأمامية، حيث يتم إزالة الطبقة المخفية غير الخطية ومشاركة طبقة الإسقاط لجميع الكلمات (وليس فقط مصفوفة الإسقاط)؛ وبالتالي يتم إسقاط جميع الكلمات إلى نفس الموضع (يتم حساب متوسط متجهاتها). نسمي هذه المعمارية نموذج كيس الكلمات لأن ترتيب الكلمات في السياق لا يؤثر على الإسقاط. علاوة على ذلك، نستخدم أيضاً كلمات من المستقبل؛ لقد حصلنا على أفضل أداء في المهمة المقدمة في القسم التالي من خلال بناء مصنف لوغاريتمي خطي مع أربع كلمات مستقبلية وأربع كلمات من السياق في المدخل، حيث معيار التدريب هو تصنيف الكلمة الحالية (الوسطى) بشكل صحيح. التعقيد التدريبي هو

$$Q = N × D + D × \log_2(V)$$

نشير إلى هذا النموذج فيما يلي باسم CBOW، حيث أنه على عكس نموذج كيس الكلمات القياسي، يستخدم التمثيل الموزع المستمر للسياق. تظهر معمارية النموذج في الشكل 1.

##### 2.4.2 نموذج Skip-gram المستمر

المعمارية الثانية مماثلة لـ CBOW، ولكن بدلاً من التنبؤ بالكلمة الحالية بناءً على السياق، فإنها تحاول تعظيم تصنيف كلمة بناءً على كلمة أخرى في نفس الجملة. بشكل أدق، نستخدم كل كلمة حالية كمدخل لمصنف لوغاريتمي خطي مع طبقة إسقاط مستمرة، ونتنبأ بالكلمات ضمن نطاق معين قبل وبعد الكلمة الحالية. وجدنا أن زيادة النطاق يحسن جودة متجهات الكلمات الناتجة، ولكنه يزيد أيضاً من التعقيد الحسابي. نظراً لأن الكلمات البعيدة عادةً ما تكون أقل صلة بالكلمة الحالية من تلك القريبة منها، فإننا نعطي وزناً أقل للكلمات البعيدة من خلال أخذ عينات أقل من هذه الكلمات في أمثلة التدريب الخاصة بنا.

التعقيد التدريبي لهذه المعمارية يتناسب مع

$$Q = C × (D + D × \log_2(V))$$

حيث C هو الحد الأقصى لمسافة الكلمات. وبالتالي، إذا اخترنا C = 5، فسنختار عشوائياً لكل كلمة تدريب رقماً R في النطاق $\langle 1; C \rangle$، ثم نستخدم R كلمات من السياق و R كلمات من المستقبل للكلمة الحالية كعلامات صحيحة. سيتطلب هذا منا القيام بـ $R × 2$ تصنيف للكلمات، مع الكلمة الحالية كمدخل، وكل من الـ $R + R$ كلمات كمخرج. في التجارب التالية، نستخدم C = 10.

---

### Translation Notes

- **Figures referenced:** Figure 1
- **Key terms introduced:** NNLM, RNNLM, CBOW (Continuous Bag-of-Words), Skip-gram, projection layer, hierarchical softmax, distributed representations, log-linear models, DistBelief, Adagrad
- **Equations:** 5 mathematical complexity formulas
- **Citations:** [1], [20, 31], [25, 23, 18], [4, 9], [15, 2], [6], [7], [13, 14], [16, 26]
- **Special handling:** Mathematical equations preserved exactly in LaTeX format; technical architecture descriptions require precise translation

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.87

### Back-Translation (Validation)

Many different types of models have been proposed for estimating continuous representations of words, including the well-known Latent Semantic Analysis (LSA) and Latent Dirichlet Allocation (LDA). In this paper, we focus on distributed representations of words learned by neural networks, as it has been previously shown that they perform significantly better than LSA in preserving linear regularities between words [20, 31]; moreover, LDA becomes computationally very expensive on large datasets.

The first proposed architecture is similar to feedforward NNLM, where the non-linear hidden layer is removed and the projection layer is shared for all words (not just the projection matrix); thus all words are projected to the same position (their vectors are averaged). We call this architecture a bag-of-words model because the order of words in the context does not affect the projection.

The second architecture is similar to CBOW, but instead of predicting the current word based on context, it tries to maximize the classification of a word based on another word in the same sentence.
