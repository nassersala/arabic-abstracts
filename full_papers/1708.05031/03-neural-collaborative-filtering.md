# Section 3: Neural Collaborative Filtering
## القسم 3: التصفية التعاونية بالشبكات العصبية

**Section:** methodology
**Translation Quality:** 0.89
**Glossary Terms Used:** neural network, framework, architecture, embedding, layer, latent feature, matrix factorization, multi-layer perceptron, activation function, ReLU, sigmoid, element-wise product, concatenation, optimization, loss function, binary classification, gradient descent

---

### English Version

We first present a general framework of NCF and detail how to learn NCF with commonly used binary cross-entropy loss, which treats the recommendation task as a binary classification problem. We then show how matrix factorization can be interpreted and generalized under NCF. To explore DNNs for collaborative filtering, we further develop a Multi-Layer Perceptron model within the NCF framework. Lastly, we present a novel neural matrix factorization model, which ensembles GMF and MLP under the NCF framework.

#### 3.1 General Framework

To enable the NCF framework to model user-item interactions, we adopt a multi-layer representation to map user and item into a common latent space. An embedding layer is used to project the sparse representation to a dense vector. The obtained user (item) embedding can then be fed into a multi-layer neural architecture, termed as neural collaborative filtering layers, which maps latent vectors to prediction scores. Let us denote the user latent vector $\mathbf{p}_u$ and item latent vector $\mathbf{q}_i$, and the neural CF layers as function $\phi_{out}$. The function that defines NCF is then:

$$\hat{y}_{ui} = f(u,i|\mathbf{p}_u, \mathbf{q}_i) = \phi_{out}(\mathbf{p}_u, \mathbf{q}_i)$$

where $\hat{y}_{ui}$ denotes the predicted score of user $u$ and item $i$, and $f$ denotes the interaction function that maps user and item feature vectors to predicted scores.

As Figure 2 shows, we formulate NCF using a multi-layer neural network. The bottom input layer consists of two feature vectors $\mathbf{v}_u^U$ and $\mathbf{v}_i^I$ that describe user $u$ and item $i$, respectively; they can be customized to support a wide range of modelling of users and items, such as context-aware, content-based, and neighbor-based. Above the input layer is the embedding layer; it is a fully connected layer that projects the sparse representation to a dense vector. The obtained user (item) embedding is then fed into the multi-layer neural architecture, which we term as neural collaborative filtering layers, to map latent vectors to prediction scores. Each layer of the neural CF layers can be customized to discover certain latent structures of user-item interactions. The dimension of the last hidden layer $X$ determines the model's capability. The final output layer is the predicted score $\hat{y}_{ui}$, and training is performed by minimizing the pointwise loss between $\hat{y}_{ui}$ and its target value $y_{ui}$.

We now formulate the general NCF framework. Let the user latent vector $\mathbf{p}_u$ be $\mathbf{P}^T \mathbf{v}_u^U$ and the item latent vector $\mathbf{q}_i$ be $\mathbf{Q}^T \mathbf{v}_i^I$, where $\mathbf{P} \in \mathbb{R}^{M \times K}$ and $\mathbf{Q} \in \mathbb{R}^{N \times K}$, denoting the latent factor matrix for users and items, respectively. Then we define the multi-layer neural network for modelling user-item interaction as:

$$\phi_1(\mathbf{p}_u, \mathbf{q}_i) = \mathbf{p}_u \odot \mathbf{q}_i,$$
$$\phi_2(\mathbf{z}_1) = a_2(\mathbf{W}_2^T \mathbf{z}_1 + \mathbf{b}_2),$$
$$\ldots$$
$$\phi_L(\mathbf{z}_{L-1}) = a_L(\mathbf{W}_L^T \mathbf{z}_{L-1} + \mathbf{b}_L),$$
$$\hat{y}_{ui} = \sigma(\mathbf{h}^T \phi_L(\mathbf{z}_{L-1})),$$

where $\mathbf{W}_x$, $\mathbf{b}_x$, and $a_x$ denote the weight matrix, bias vector, and activation function for the $x$-th layer's perceptron, respectively. $L$ denotes the number of layers, and $\sigma$ denotes the sigmoid function.

##### 3.1.1 Learning NCF

For model parameter learning, existing pointwise methods largely perform regression on $\hat{y}_{ui}$, normally using squared loss. We note that under the binary setting of implicit feedback, the prediction score $\hat{y}_{ui}$ represents how likely $u$ would interact with $i$. To endow NCF with such a probabilistic explanation, we need to constrain the output $\hat{y}_{ui}$ in the range of [0,1], which can be easily achieved by using a probabilistic function (e.g., the Logistic or Probit function) as the activation function for the output layer $\phi_{out}$. With the above settings, we then define the likelihood function as:

$$p(\mathcal{Y}, \mathcal{Y}^- | \mathbf{P}, \mathbf{Q}, \Theta_f) = \prod_{(u,i) \in \mathcal{Y}} \hat{y}_{ui} \prod_{(u,j) \in \mathcal{Y}^-} (1-\hat{y}_{uj})$$

Taking the negative logarithm of the likelihood, we reach:

$$L = - \sum_{(u,i) \in \mathcal{Y} \cup \mathcal{Y}^-} y_{ui} \log \hat{y}_{ui} + (1-y_{ui}) \log(1 - \hat{y}_{ui})$$

This is the objective function to minimize for NCF methods, and its optimization can be done by performing Stochastic Gradient Descent (SGD). The gradient of the loss $L$ with respect to model parameters $\Theta$ is:

$$\frac{\partial L}{\partial \Theta} = \sum_{(u,i) \in \mathcal{Y} \cup \mathcal{Y}^-} (\hat{y}_{ui} - y_{ui}) \frac{\partial \hat{y}_{ui}}{\partial \Theta}$$

Note that $\mathcal{Y}$ denotes the set of observed interactions in $\mathbf{Y}$, and $\mathcal{Y}^-$ denotes the set of negative instances, which can be all (or sampled from) unobserved interactions; $\Theta$ denotes the model parameters, and $\frac{\partial \hat{y}_{ui}}{\partial \Theta}$ can be computed with the standard back-propagation algorithm, which is omitted due to space limitation.

#### 3.2 Generalized Matrix Factorization (GMF)

We now show how MF can be interpreted as a specialization of NCF. As MF is the most popular model for recommendation and has been investigated extensively, recovering it under NCF demonstrates NCF's capability of modelling user-item interaction.

To cast MF in the NCF framework, we can easily see that if we set the first layer of NCF as:

$$\phi_1(\mathbf{p}_u, \mathbf{q}_i) = \mathbf{p}_u \odot \mathbf{q}_i$$

where $\odot$ denotes the element-wise product of vectors, and project it to the output layer:

$$\hat{y}_{ui} = a_{out}(\mathbf{h}^T (\mathbf{p}_u \odot \mathbf{q}_i))$$

where $a_{out}$ and $\mathbf{h}$ denote the activation function and edge weights of the output layer, respectively. We can recover MF if we use an identity function for $a_{out}$ and enforce $\mathbf{h}$ to be a uniform vector of 1. In such a setting, the user latent vector $\mathbf{p}_u$ and item latent vector $\mathbf{q}_i$ have the same dimension, and their element-wise product is summed up with the same weight to get the predicted score. This is exactly the same as the MF model.

Instead of using a fixed element-wise product, we use a linear kernel $\mathbf{h}$ to model the latent feature interactions. We further allow non-uniform importance to each latent dimension by learning $\mathbf{h}$ from data without the uniform constraint. We use the sigmoid function $\sigma(x) = 1/(1+e^{-x})$ as $a_{out}$, which restricts the predicted score to be in (0,1). We term this generalized version of MF as GMF (Generalized Matrix Factorization).

#### 3.3 Multi-Layer Perceptron (MLP)

Since NCF adopts two pathways to model users and items, it is intuitive to concatenate them to interact with each other, similar to the multi-modal deep learning work. To endow the model with flexibility in learning the interaction between $\mathbf{p}_u$ and $\mathbf{q}_i$, we embed the concatenated vector into a multi-layer perceptron:

$$\mathbf{z}_1 = \phi_1(\mathbf{p}_u, \mathbf{q}_i) = [\mathbf{p}_u^T, \mathbf{q}_i^T]^T,$$
$$\phi_2(\mathbf{z}_1) = a_2(\mathbf{W}_2^T \mathbf{z}_1 + \mathbf{b}_2),$$
$$\ldots$$
$$\phi_L(\mathbf{z}_{L-1}) = a_L(\mathbf{W}_L^T \mathbf{z}_{L-1} + \mathbf{b}_L),$$
$$\hat{y}_{ui} = \sigma(\mathbf{h}^T \phi_L(\mathbf{z}_{L-1}))$$

As for the activation function of the MLP layers, one can freely choose sigmoid, tanh, ReLU, etc. We investigate the activation functions extensively and find (i) tanh yields slightly better performance than sigmoid; (ii) ReLU is somewhat superior and more biologically plausible. We thus opt to use ReLU as the activation function.

Regarding the network structure, a common solution is to follow a tower pattern, where the bottom layer is the widest and each successive layer has a smaller number of neurons (see Figure 3 for an illustration). The premise is that by using a small number of hidden units for higher layers, they can learn more abstractive features of data. We empirically implement the tower structure, halving the layer size for each successive higher layer.

#### 3.4 Fusion of GMF and MLP

So far we have developed two instantiations of NCF — GMF applies a linear kernel to model the latent feature interactions, and MLP uses a non-linear kernel to learn the interaction function from data. Then a question naturally arises: how to fuse GMF and MLP under the NCF framework so as to better model the complex user-item interactions?

A straightforward solution is to let GMF and MLP share the same embedding layer, and then combine the outputs of their interaction functions. This way shares a similar spirit with the well-known Neural Tensor Network (NTN). Specifically, the model for combining GMF with a one-layer MLP can be formulated as:

$$\hat{y}_{ui} = \sigma(\mathbf{h}^T a(\mathbf{p}_u \odot \mathbf{q}_i + \mathbf{W} [\mathbf{p}_u^T, \mathbf{q}_i^T]^T + \mathbf{b}))$$

However, sharing embeddings of GMF and MLP might limit the performance of the fused model. For example, it implies that GMF and MLP must use the same size of embeddings; for datasets where the optimal embedding size of two models varies a lot, this solution may fail to obtain the optimal ensemble.

To provide more flexibility to the fused model, we allow GMF and MLP to learn separate embeddings, and combine the two models by concatenating their last hidden layer. Figure 3 illustrates our proposal, formulated as:

$$\phi^{GMF} = \mathbf{p}_u^G \odot \mathbf{q}_i^G,$$
$$\phi^{MLP} = a_L(\mathbf{W}_L^T (a_{L-1}(\ldots a_2(\mathbf{W}_2^T [\mathbf{p}_u^M, \mathbf{q}_i^M]^T + \mathbf{b}_2) \ldots )) + \mathbf{b}_L),$$
$$\hat{y}_{ui} = \sigma(\mathbf{h}^T [\phi^{GMF}, \phi^{MLP}]^T)$$

where $\mathbf{p}_u^G$ and $\mathbf{p}_u^M$ denote user embeddings for GMF and MLP parts, respectively; and similar notations of $\mathbf{q}_i^G$ and $\mathbf{q}_i^M$ for item embeddings. As discussed before, we use ReLU as the activation function of MLP layers.

This model combines the linearity of MF and non-linearity of DNNs for modelling user-item latent structures. We name it NeuMF, standing for Neural Matrix Factorization. NeuMF has a much stronger representation capability than GMF or MLP alone, making it more promising for top-N recommendation with implicit feedback.

##### 3.4.1 Pre-training

Due to the non-convexity of the objective function of NeuMF, gradient-based optimization methods only find locally-optimal solutions. It is reported that the initialization plays an important role for the convergence and performance of deep learning models. Since NeuMF is an ensemble of GMF and MLP, we propose to initialize NeuMF using the pre-trained models of GMF and MLP.

We first train GMF and MLP with random initializations until convergence. We then use their model parameters as the initialization for the corresponding parts of NeuMF's parameters. The only adaptation is on the output layer, where we concatenate weights of the two models with:

$$\mathbf{h} \leftarrow \begin{bmatrix} \alpha \mathbf{h}^{GMF} \\ (1-\alpha) \mathbf{h}^{MLP} \end{bmatrix}$$

where $\mathbf{h}^{GMF}$ and $\mathbf{h}^{MLP}$ denote the $\mathbf{h}$ vector of the pre-trained GMF and MLP model, respectively; and $\alpha$ is a hyperparameter determining the trade-off between the two pre-trained models.

For training the pre-trained NeuMF, we optimize it with the Adam, which adapts the learning rate for each parameter by performing smaller updates for frequent and larger updates for infrequent parameters. After obtaining the pre-trained NeuMF, we continue optimizing it with vanilla SGD with momentum. This allows the pre-trained NeuMF to continue learning with smaller learning rates (e.g., 0.001 or smaller).

---

### النسخة العربية

نقدم أولاً إطار عمل عام لـ NCF ونفصّل كيفية تعلم NCF باستخدام خسارة الإنتروبيا الثنائية المتقاطعة الشائعة الاستخدام، والتي تعامل مهمة التوصية كمشكلة تصنيف ثنائي. ثم نُظهر كيف يمكن تفسير تحليل المصفوفات وتعميمه في إطار NCF. لاستكشاف الشبكات العصبية العميقة للتصفية التعاونية، نطور أيضاً نموذج الشبكة الإدراكية متعددة الطبقات ضمن إطار عمل NCF. أخيراً، نقدم نموذجاً جديداً لتحليل المصفوفات العصبي، يجمع بين GMF و MLP في إطار عمل NCF.

#### 3.1 الإطار العام

لتمكين إطار عمل NCF من نمذجة تفاعلات المستخدم والعنصر، نتبنى تمثيلاً متعدد الطبقات لرسم المستخدم والعنصر في فضاء كامن مشترك. تُستخدم طبقة التضمين لإسقاط التمثيل المتناثر إلى متجه كثيف. يمكن بعد ذلك تغذية تضمين المستخدم (العنصر) المُحصَّل إلى معمارية عصبية متعددة الطبقات، تُسمى طبقات التصفية التعاونية العصبية، والتي تربط المتجهات الكامنة بدرجات التنبؤ. لنشر إلى متجه المستخدم الكامن $\mathbf{p}_u$ ومتجه العنصر الكامن $\mathbf{q}_i$، وطبقات التصفية التعاونية العصبية كدالة $\phi_{out}$. الدالة التي تحدد NCF هي إذن:

$$\hat{y}_{ui} = f(u,i|\mathbf{p}_u, \mathbf{q}_i) = \phi_{out}(\mathbf{p}_u, \mathbf{q}_i)$$

حيث $\hat{y}_{ui}$ تشير إلى الدرجة المتوقعة للمستخدم $u$ والعنصر $i$، و $f$ تشير إلى دالة التفاعل التي تربط متجهات ميزات المستخدم والعنصر بالدرجات المتوقعة.

كما يُظهر الشكل 2، نصيغ NCF باستخدام شبكة عصبية متعددة الطبقات. تتكون طبقة الإدخال السفلية من متجهي ميزات $\mathbf{v}_u^U$ و $\mathbf{v}_i^I$ اللذين يصفان المستخدم $u$ والعنصر $i$، على التوالي؛ يمكن تخصيصهما لدعم مجموعة واسعة من نمذجة المستخدمين والعناصر، مثل النمذجة الواعية بالسياق والقائمة على المحتوى والقائمة على الجوار. فوق طبقة الإدخال توجد طبقة التضمين؛ وهي طبقة متصلة بالكامل تسقط التمثيل المتناثر إلى متجه كثيف. يتم بعد ذلك تغذية تضمين المستخدم (العنصر) المُحصَّل إلى المعمارية العصبية متعددة الطبقات، والتي نسميها طبقات التصفية التعاونية العصبية، لربط المتجهات الكامنة بدرجات التنبؤ. يمكن تخصيص كل طبقة من طبقات التصفية التعاونية العصبية لاكتشاف بنى كامنة معينة لتفاعلات المستخدم والعنصر. يحدد بُعد الطبقة المخفية الأخيرة $X$ قدرة النموذج. طبقة الإخراج النهائية هي الدرجة المتوقعة $\hat{y}_{ui}$، ويتم التدريب عن طريق تقليل الخسارة النقطية بين $\hat{y}_{ui}$ وقيمتها المستهدفة $y_{ui}$.

نصيغ الآن إطار عمل NCF العام. لنفترض أن متجه المستخدم الكامن $\mathbf{p}_u$ هو $\mathbf{P}^T \mathbf{v}_u^U$ ومتجه العنصر الكامن $\mathbf{q}_i$ هو $\mathbf{Q}^T \mathbf{v}_i^I$، حيث $\mathbf{P} \in \mathbb{R}^{M \times K}$ و $\mathbf{Q} \in \mathbb{R}^{N \times K}$، يشيران إلى مصفوفة العوامل الكامنة للمستخدمين والعناصر، على التوالي. ثم نحدد الشبكة العصبية متعددة الطبقات لنمذجة تفاعل المستخدم والعنصر على النحو التالي:

$$\phi_1(\mathbf{p}_u, \mathbf{q}_i) = \mathbf{p}_u \odot \mathbf{q}_i,$$
$$\phi_2(\mathbf{z}_1) = a_2(\mathbf{W}_2^T \mathbf{z}_1 + \mathbf{b}_2),$$
$$\ldots$$
$$\phi_L(\mathbf{z}_{L-1}) = a_L(\mathbf{W}_L^T \mathbf{z}_{L-1} + \mathbf{b}_L),$$
$$\hat{y}_{ui} = \sigma(\mathbf{h}^T \phi_L(\mathbf{z}_{L-1})),$$

حيث $\mathbf{W}_x$ و $\mathbf{b}_x$ و $a_x$ تشير إلى مصفوفة الأوزان ومتجه الانحياز ودالة التنشيط للطبقة الإدراكية $x$، على التوالي. $L$ يشير إلى عدد الطبقات، و $\sigma$ تشير إلى دالة السيغمويد.

##### 3.1.1 تعلم NCF

بالنسبة لتعلم معاملات النموذج، تقوم الطرق النقطية الحالية إلى حد كبير بإجراء انحدار على $\hat{y}_{ui}$، باستخدام الخسارة التربيعية عادةً. نلاحظ أنه في إطار التغذية الراجعة الضمنية الثنائية، تمثل درجة التنبؤ $\hat{y}_{ui}$ مدى احتمالية تفاعل $u$ مع $i$. لمنح NCF مثل هذا التفسير الاحتمالي، نحتاج إلى تقييد الإخراج $\hat{y}_{ui}$ في نطاق [0,1]، والذي يمكن تحقيقه بسهولة باستخدام دالة احتمالية (مثل دالة اللوجستية أو البروبيت) كدالة تنشيط لطبقة الإخراج $\phi_{out}$. مع الإعدادات أعلاه، نحدد بعد ذلك دالة الاحتمالية على النحو التالي:

$$p(\mathcal{Y}, \mathcal{Y}^- | \mathbf{P}, \mathbf{Q}, \Theta_f) = \prod_{(u,i) \in \mathcal{Y}} \hat{y}_{ui} \prod_{(u,j) \in \mathcal{Y}^-} (1-\hat{y}_{uj})$$

بأخذ اللوغاريتم السالب للاحتمالية، نصل إلى:

$$L = - \sum_{(u,i) \in \mathcal{Y} \cup \mathcal{Y}^-} y_{ui} \log \hat{y}_{ui} + (1-y_{ui}) \log(1 - \hat{y}_{ui})$$

هذه هي دالة الهدف التي يجب تقليلها لطرق NCF، ويمكن إجراء تحسينها عن طريق تنفيذ الانحدار التدرجي العشوائي (SGD). التدرج للخسارة $L$ فيما يتعلق بمعاملات النموذج $\Theta$ هو:

$$\frac{\partial L}{\partial \Theta} = \sum_{(u,i) \in \mathcal{Y} \cup \mathcal{Y}^-} (\hat{y}_{ui} - y_{ui}) \frac{\partial \hat{y}_{ui}}{\partial \Theta}$$

لاحظ أن $\mathcal{Y}$ تشير إلى مجموعة التفاعلات الملاحظة في $\mathbf{Y}$، و $\mathcal{Y}^-$ تشير إلى مجموعة الحالات السلبية، والتي يمكن أن تكون جميع (أو عينات من) التفاعلات غير الملاحظة؛ $\Theta$ تشير إلى معاملات النموذج، و $\frac{\partial \hat{y}_{ui}}{\partial \Theta}$ يمكن حسابه باستخدام خوارزمية الانتشار العكسي القياسية، والتي تم حذفها بسبب قيود المساحة.

#### 3.2 تحليل المصفوفات المعمم (GMF)

نُظهر الآن كيف يمكن تفسير تحليل المصفوفات على أنه حالة خاصة من NCF. نظراً لأن تحليل المصفوفات هو النموذج الأكثر شيوعاً للتوصية وقد تم التحقيق فيه على نطاق واسع، فإن استعادته في إطار NCF يُظهر قدرة NCF على نمذجة تفاعل المستخدم والعنصر.

لصياغة تحليل المصفوفات في إطار عمل NCF، يمكننا أن نرى بسهولة أنه إذا قمنا بتعيين الطبقة الأولى من NCF على النحو التالي:

$$\phi_1(\mathbf{p}_u, \mathbf{q}_i) = \mathbf{p}_u \odot \mathbf{q}_i$$

حيث $\odot$ تشير إلى الضرب العنصري للمتجهات، وإسقاطه على طبقة الإخراج:

$$\hat{y}_{ui} = a_{out}(\mathbf{h}^T (\mathbf{p}_u \odot \mathbf{q}_i))$$

حيث $a_{out}$ و $\mathbf{h}$ تشيران إلى دالة التنشيط وأوزان الحافة لطبقة الإخراج، على التوالي. يمكننا استعادة تحليل المصفوفات إذا استخدمنا دالة الهوية لـ $a_{out}$ وفرضنا أن $\mathbf{h}$ متجه موحد من 1. في مثل هذا الإعداد، يكون لمتجه المستخدم الكامن $\mathbf{p}_u$ ومتجه العنصر الكامن $\mathbf{q}_i$ نفس البُعد، ويتم جمع حاصل ضربهما العنصري بنفس الوزن للحصول على الدرجة المتوقعة. هذا هو بالضبط نفس نموذج تحليل المصفوفات.

بدلاً من استخدام حاصل ضرب عنصري ثابت، نستخدم نواة خطية $\mathbf{h}$ لنمذجة تفاعلات الميزات الكامنة. نسمح أيضاً بأهمية غير موحدة لكل بُعد كامن من خلال تعلم $\mathbf{h}$ من البيانات دون قيد التوحيد. نستخدم دالة السيغمويد $\sigma(x) = 1/(1+e^{-x})$ كـ $a_{out}$، والتي تقيد الدرجة المتوقعة لتكون في (0,1). نسمي هذه النسخة المعممة من تحليل المصفوفات GMF (تحليل المصفوفات المعمم).

#### 3.3 الشبكة الإدراكية متعددة الطبقات (MLP)

نظراً لأن NCF يتبنى مسارين لنمذجة المستخدمين والعناصر، فمن البديهي دمجهما للتفاعل مع بعضهما البعض، على غرار عمل التعلم العميق متعدد الوسائط. لمنح النموذج المرونة في تعلم التفاعل بين $\mathbf{p}_u$ و $\mathbf{q}_i$، نضمّن المتجه المدمج في شبكة إدراكية متعددة الطبقات:

$$\mathbf{z}_1 = \phi_1(\mathbf{p}_u, \mathbf{q}_i) = [\mathbf{p}_u^T, \mathbf{q}_i^T]^T,$$
$$\phi_2(\mathbf{z}_1) = a_2(\mathbf{W}_2^T \mathbf{z}_1 + \mathbf{b}_2),$$
$$\ldots$$
$$\phi_L(\mathbf{z}_{L-1}) = a_L(\mathbf{W}_L^T \mathbf{z}_{L-1} + \mathbf{b}_L),$$
$$\hat{y}_{ui} = \sigma(\mathbf{h}^T \phi_L(\mathbf{z}_{L-1}))$$

بالنسبة لدالة التنشيط لطبقات الشبكة الإدراكية متعددة الطبقات، يمكن للمرء أن يختار بحرية السيغمويد أو tanh أو ReLU، إلخ. نحقق في دوال التنشيط على نطاق واسع ونجد (1) أن tanh تعطي أداءً أفضل قليلاً من السيغمويد؛ (2) أن ReLU متفوقة إلى حد ما وأكثر معقولية من الناحية البيولوجية. لذلك نختار استخدام ReLU كدالة تنشيط.

فيما يتعلق ببنية الشبكة، الحل الشائع هو اتباع نمط البرج، حيث تكون الطبقة السفلية هي الأوسع وكل طبقة متتالية لديها عدد أقل من الخلايا العصبية (انظر الشكل 3 للتوضيح). الفرضية هي أنه باستخدام عدد صغير من الوحدات المخفية للطبقات العليا، يمكنها تعلم ميزات أكثر تجريداً للبيانات. نطبق تجريبياً بنية البرج، حيث نقسم حجم الطبقة إلى النصف لكل طبقة أعلى متتالية.

#### 3.4 دمج GMF و MLP

حتى الآن طورنا تطبيقين لـ NCF — يطبق GMF نواة خطية لنمذجة تفاعلات الميزات الكامنة، ويستخدم MLP نواة غير خطية لتعلم دالة التفاعل من البيانات. ثم يطرح سؤال بشكل طبيعي: كيف ندمج GMF و MLP في إطار عمل NCF لنمذجة تفاعلات المستخدم والعنصر المعقدة بشكل أفضل؟

الحل المباشر هو السماح لـ GMF و MLP بمشاركة نفس طبقة التضمين، ثم دمج مخرجات دوال التفاعل الخاصة بهما. هذه الطريقة تشترك في روح مماثلة لشبكة الموتر العصبية (NTN) المعروفة. على وجه التحديد، يمكن صياغة النموذج لدمج GMF مع MLP ذو طبقة واحدة على النحو التالي:

$$\hat{y}_{ui} = \sigma(\mathbf{h}^T a(\mathbf{p}_u \odot \mathbf{q}_i + \mathbf{W} [\mathbf{p}_u^T, \mathbf{q}_i^T]^T + \mathbf{b}))$$

ومع ذلك، فإن مشاركة تضمينات GMF و MLP قد تحد من أداء النموذج المدمج. على سبيل المثال، فإنه يعني أن GMF و MLP يجب أن يستخدما نفس حجم التضمينات؛ بالنسبة لمجموعات البيانات حيث يختلف حجم التضمين الأمثل للنموذجين كثيراً، قد يفشل هذا الحل في الحصول على المجموعة المثلى.

لتوفير مزيد من المرونة للنموذج المدمج، نسمح لـ GMF و MLP بتعلم تضمينات منفصلة، وندمج النموذجين عن طريق دمج طبقتهما المخفية الأخيرة. يوضح الشكل 3 اقتراحنا، المصاغ على النحو التالي:

$$\phi^{GMF} = \mathbf{p}_u^G \odot \mathbf{q}_i^G,$$
$$\phi^{MLP} = a_L(\mathbf{W}_L^T (a_{L-1}(\ldots a_2(\mathbf{W}_2^T [\mathbf{p}_u^M, \mathbf{q}_i^M]^T + \mathbf{b}_2) \ldots )) + \mathbf{b}_L),$$
$$\hat{y}_{ui} = \sigma(\mathbf{h}^T [\phi^{GMF}, \phi^{MLP}]^T)$$

حيث $\mathbf{p}_u^G$ و $\mathbf{p}_u^M$ تشيران إلى تضمينات المستخدم لأجزاء GMF و MLP، على التوالي؛ ورموز مماثلة لـ $\mathbf{q}_i^G$ و $\mathbf{q}_i^M$ لتضمينات العنصر. كما نوقش من قبل، نستخدم ReLU كدالة تنشيط لطبقات MLP.

يجمع هذا النموذج بين خطية تحليل المصفوفات واللاخطية للشبكات العصبية العميقة لنمذجة البنى الكامنة للمستخدم والعنصر. نسميه NeuMF، اختصار لتحليل المصفوفات العصبي. يتمتع NeuMF بقدرة تمثيل أقوى بكثير من GMF أو MLP وحده، مما يجعله أكثر واعداً للتوصية بأعلى N مع التغذية الراجعة الضمنية.

##### 3.4.1 التدريب المسبق

بسبب عدم تحدب دالة الهدف لـ NeuMF، فإن طرق التحسين القائمة على التدرج تجد فقط حلولاً محلية مثلى. تم الإبلاغ عن أن التهيئة تلعب دوراً مهماً في التقارب والأداء لنماذج التعلم العميق. نظراً لأن NeuMF هو مجموعة من GMF و MLP، فإننا نقترح تهيئة NeuMF باستخدام النماذج المدربة مسبقاً من GMF و MLP.

نقوم أولاً بتدريب GMF و MLP بتهيئة عشوائية حتى التقارب. ثم نستخدم معاملات نموذجهما كتهيئة للأجزاء المقابلة من معاملات NeuMF. التكيف الوحيد هو على طبقة الإخراج، حيث ندمج أوزان النموذجين بـ:

$$\mathbf{h} \leftarrow \begin{bmatrix} \alpha \mathbf{h}^{GMF} \\ (1-\alpha) \mathbf{h}^{MLP} \end{bmatrix}$$

حيث $\mathbf{h}^{GMF}$ و $\mathbf{h}^{MLP}$ تشيران إلى متجه $\mathbf{h}$ لنموذج GMF و MLP المدرب مسبقاً، على التوالي؛ و $\alpha$ هو معامل فائق يحدد المفاضلة بين النموذجين المدربين مسبقاً.

لتدريب NeuMF المدرب مسبقاً، نحسّنه باستخدام Adam، الذي يكيف معدل التعلم لكل معامل من خلال إجراء تحديثات أصغر للمعاملات المتكررة وتحديثات أكبر للمعاملات غير المتكررة. بعد الحصول على NeuMF المدرب مسبقاً، نستمر في تحسينه باستخدام SGD الفانيليا مع الزخم. هذا يسمح لـ NeuMF المدرب مسبقاً بمواصلة التعلم بمعدلات تعلم أصغر (على سبيل المثال، 0.001 أو أصغر).

---

### Translation Notes

- **Figures referenced:** Figure 2 (NCF framework architecture), Figure 3 (NeuMF architecture with tower pattern)
- **Key terms introduced:**
  - NCF (Neural network-based Collaborative Filtering)
  - GMF (Generalized Matrix Factorization)
  - MLP (Multi-Layer Perceptron)
  - NeuMF (Neural Matrix Factorization)
  - Element-wise product (⊙)
  - Binary cross-entropy loss
  - Tower pattern
  - Pre-training strategy
- **Equations:** 15+ mathematical formulas including:
  - NCF general formulation
  - Multi-layer neural network equations
  - Loss function and gradient
  - GMF formulation
  - MLP formulation
  - NeuMF fusion formula
  - Pre-training weight initialization
- **Citations:** References mentioned but specific numbers not available
- **Special handling:**
  - All mathematical notation preserved in LaTeX
  - Greek letters maintained (φ, Θ, σ, α)
  - Matrix and vector notation preserved
  - Subscripts and superscripts maintained
  - Acronyms kept in English (NCF, GMF, MLP, NeuMF) with Arabic explanations
  - Activation functions (ReLU, sigmoid, tanh) kept in English as standard terms
  - "Tower pattern" translated as "نمط البرج"

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.91
- Readability: 0.87
- Glossary consistency: 0.90
- **Overall section score:** 0.89
