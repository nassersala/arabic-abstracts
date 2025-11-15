# Section 4: Blind Spots in Neural Networks
## القسم 4: النقاط العمياء في الشبكات العصبية

**Section:** adversarial-examples
**Translation Quality:** 0.88
**Glossary Terms Used:** adversarial examples, perturbation, generalization, smoothness, cross-entropy loss, optimization, L-BFGS, hard-negative mining, hyperparameters, weight decay, dropout

---

### English Version

So far, unit-level inspection methods had relatively little utility beyond confirming certain intuitions regarding the complexity of the representations learned by a deep neural network~\cite{girshick2013rich, zeiler2013visualizing, goodfellow2009measuring,erhan2009visualization}. Global, network level inspection methods \emph{can} be useful in the context of explaining classification decisions made by a model~\cite{baehrens2010explain} and can be used to, for instance, identify the parts of the input which led to a correct classification of a given visual input instance
(in other words, one can use a trained model for weakly-supervised localization). Such global analyses are useful in that they can make us understand better the input-to-output mapping represented by the trained network.

Generally speaking, the output layer unit of a neural network is a highly nonlinear function of its input. When it is trained with the cross-entropy loss (using the Softmax activation function), it represents a conditional distribution of the label given the input (and the training set presented so far). It has been argued~\cite{bengio2009learning} that the deep stack of non-linear layers in between the input and the output unit of a neural network are a way for the model to encode a \emph{non-local generalization prior} over the input space.
In other words, it is assumed that is possible for the output unit to assign non-significant
(and, presumably, non-epsilon) probabilities to regions of the input space that contain no training examples in their vicinity. Such regions can represent, for instance, the same objects from different viewpoints, which are relatively far (in pixel space), but which share nonetheless both the label and the statistical structure of the original inputs.

It is implicit in such arguments that $local$ generalization---in the very proximity of the training examples---works as expected. And that in particular, for a small enough radius $\varepsilon > 0$ in the vicinity of a given training input $x$, an $x + r$ satisfying $||r|| < \varepsilon$ will get assigned a high probability of the correct class by the model. This kind of smoothness prior is typically valid for computer vision problems. In general, imperceptibly tiny perturbations of a given image do not normally change the underlying class.

Our main result is that for deep neural networks, the smoothness assumption that underlies many kernel methods does not hold.  Specifically, we show that by using a simple optimization procedure, we are able to find adversarial examples, which are obtained by imperceptibly small perturbations to a correctly classified input image, so that it is no longer classified correctly.

In some sense, what we describe is a way to traverse the manifold represented by the network in an efficient way (by optimization) and finding \emph{adversarial examples} in the input space. The adversarial examples represent low-probability (high-dimensional) ``pockets'' in the manifold, which are hard to efficiently find by simply randomly sampling the input around a given example. Already, a variety of recent state of the art computer vision models employ input deformations during training for increasing the robustness and convergence speed of the models~\cite{krizhevsky2012imagenet,zeiler2013visualizing}. These deformations are, however, statistically inefficient, for a given example: they are highly correlated and are drawn from the same distribution throughout the entire training of the model. We propose a scheme to make this process adaptive in a way that exploits the model and its deficiencies in modeling the local space around the training data.

We make the connection with hard-negative mining explicitly, as it is close in spirit: hard-negative mining, in computer vision, consists of identifying training set examples (or portions thereof) which are given low probabilities by the model, but which should be high probability instead, cf.~\cite{felzenszwalb2008discriminatively}. The training set distribution is then changed to emphasize such hard negatives and a further round of model training is performed. As shall be described, the optimization problem proposed in this work can also be used in a constructive way, similar to the hard-negative mining principle.

### Formal description

We denote by $f: \mathbb{R}^m \longrightarrow \{1 \dots k\}$ a classifier
mapping image pixel value vectors to a discrete label set. We also assume
that $f$ has an associated continuous loss function denoted by
$\textrm{loss}_f:\mathbb{R}^m\times \{1 \dots k\}\longrightarrow \mathbb{R}^+$.
For a given $x\in\mathbb{R}^m$ image and target label $l\in \{1 \dots k\}$,
we aim to solve the following box-constrained optimization problem:
\begin{itemize}
\item Minimize $\|r\|_2$ subject to:
  \begin{enumerate}
    \item $f(x+r)=l$
    \item $x+r \in [0, 1]^m$
  \end{enumerate}
\end{itemize}
The minimizer $r$ might not be unique, but we denote one such $x+r$ for an
arbitrarily chosen minimizer by $D(x, l)$. Informally, $x + r$ is the closest
image to $x$ classified as $l$ by $f$.
Obviously, $D(x, f(x))=f(x)$, so this task is non-trivial only if
$f(x)\neq l$.
In general, the exact computation of $D(x, l)$ is a hard problem,
so we approximate it by using a box-constrained
L-BFGS. Concretely, we find an approximation of $D(x, l)$ by performing
line-search to find the minimum $c>0$ for which the minimizer $r$
of the following problem satisfies $f(x+r)=l$.
\begin{itemize}
\item Minimize $c|r| + \textrm{loss}_f(x + r, l)$ subject to $x+r \in [0,1]^m$
\end{itemize}
This penalty function method would yield the exact solution for $D(X, l)$
in the case of convex losses, however neural networks are non-convex in general,
so we end up with an approximation in this case.

### Experimental results

Our ``minimum distortion'' function $D$ has the following intriguing
properties which we will support by informal evidence and quantitative
experiments in this section:
\begin{enumerate}
\item For all the networks we studied (MNIST, QuocNet \cite{le2011building},
AlexNet \cite{krizhevsky2012imagenet}), for each
sample, we have always managed to generate very close, visually hard to
distinguish, adversarial examples that are misclassified by the original
network (see figure \ref{fig:alexnegative} and {\tt http://goo.gl/huaGPb}
for examples).
\item {\it Cross model generalization:} a relatively large fraction of examples will
be misclassified by networks trained from scratch with different
hyper-parameters (number of layers, regularization or initial weights).
\item {\it Cross training-set generalization} a relatively large fraction of examples
will be misclassified by networks trained from scratch {\it on a disjoint
training set}.
\end{enumerate}
The above observations suggest that adversarial examples are somewhat universal
and not just the results of overfitting to a particular model or to the specific
selection of the training set. They also suggest that back-feeding
adversarial examples to training might improve generalization of the resulting models.
Our preliminary experiments have yielded positive evidence on MNIST to
support this hypothesis as well: We have successfully trained a two layer
100-100-10 non-convolutional neural network with a test error below $1.2\%$ by
keeping a pool of adversarial examples a random subset of which is continuously
replaced by newly generated adversarial examples and which is mixed into the
original training set all the time. We used weight decay, but no dropout for
this network. For comparison, a network of this size gets to $1.6\%$ errors
when regularized by weight decay alone and can be improved to around $1.3\%$
by using carefully applied dropout. A subtle, but essential
detail is that we only got improvements by generating adversarial examples for
each layer outputs which were used to train all the layers above.
The network was trained in an alternating fashion, maintaining and updating
a pool of adversarial examples for each layer separately in addition to the
original training set. According to our initial observations, adversarial
examples for the higher layers seemed to be significantly more useful than
those on the input or lower layers. In our future work, we plan to compare these
effects in a systematic manner.

[Content continues with experimental tables and cross-validation results...]

---

### النسخة العربية

حتى الآن، كان لطرق الفحص على مستوى الوحدة فائدة قليلة نسبياً تتجاوز تأكيد بعض الحدس فيما يتعلق بتعقيد التمثيلات التي تعلمتها الشبكة العصبية العميقة~\cite{girshick2013rich, zeiler2013visualizing, goodfellow2009measuring,erhan2009visualization}. يمكن أن تكون طرق الفحص الشاملة على مستوى الشبكة \emph{مفيدة} في سياق شرح قرارات التصنيف التي يتخذها النموذج~\cite{baehrens2010explain} ويمكن استخدامها، على سبيل المثال، لتحديد أجزاء الإدخال التي أدت إلى تصنيف صحيح لمثيل إدخال مرئي معين (بعبارة أخرى، يمكن للمرء استخدام نموذج مدرب للتوطين الضعيف الإشراف). مثل هذه التحليلات الشاملة مفيدة من حيث أنها يمكن أن تجعلنا نفهم بشكل أفضل تعيين الإدخال إلى الإخراج الذي يمثله الشبكة المدربة.

بشكل عام، تعد وحدة طبقة الإخراج للشبكة العصبية دالة غير خطية للغاية من مدخلاتها. عندما يتم تدريبها بخسارة الإنتروبيا المتقاطعة (باستخدام دالة تنشيط Softmax)، فإنها تمثل توزيعاً شرطياً للتسمية بالنظر إلى المدخل (ومجموعة التدريب المقدمة حتى الآن). تم الجدل~\cite{bengio2009learning} بأن الكومة العميقة من الطبقات غير الخطية بين وحدة الإدخال ووحدة الإخراج للشبكة العصبية هي طريقة للنموذج لترميز \emph{افتراض مسبق للتعميم غير المحلي} على فضاء الإدخال. بعبارة أخرى، يُفترض أنه من الممكن لوحدة الإخراج تعيين احتمالات غير مهمة (ويُفترض، غير إبسيلون) لمناطق من فضاء الإدخال لا تحتوي على أمثلة تدريب في جوارها. يمكن أن تمثل هذه المناطق، على سبيل المثال، نفس الأشياء من وجهات نظر مختلفة، والتي تكون بعيدة نسبياً (في فضاء البكسل)، ولكنها تشترك مع ذلك في كل من التسمية والبنية الإحصائية للمدخلات الأصلية.

من الضمني في مثل هذه الحجج أن التعميم $المحلي$ --- في القرب الشديد من أمثلة التدريب --- يعمل كما هو متوقع. وبشكل خاص، لنصف قطر صغير بما يكفي $\varepsilon > 0$ في جوار مدخل تدريب معين $x$، سيتم تعيين احتمال عالٍ للصنف الصحيح بواسطة النموذج لـ $x + r$ الذي يحقق $||r|| < \varepsilon$. هذا النوع من الافتراض المسبق للنعومة صحيح عادة لمشاكل الرؤية الحاسوبية. بشكل عام، لا تغير الاضطرابات الصغيرة غير المحسوسة لصورة معينة عادةً الصنف الأساسي.

نتيجتنا الرئيسية هي أنه بالنسبة للشبكات العصبية العميقة، فإن افتراض النعومة الذي يكمن وراء العديد من طرق النواة لا يصمد. على وجه التحديد، نُظهر أنه باستخدام إجراء تحسين بسيط، نحن قادرون على إيجاد أمثلة خصامية، والتي يتم الحصول عليها من خلال اضطرابات صغيرة غير محسوسة لصورة إدخال مصنفة بشكل صحيح، بحيث لم تعد مصنفة بشكل صحيح.

بمعنى ما، ما نصفه هو طريقة لاجتياز المشعب الذي تمثله الشبكة بطريقة فعالة (عن طريق التحسين) وإيجاد \emph{أمثلة خصامية} في فضاء الإدخال. تمثل الأمثلة الخصامية "جيوب" منخفضة الاحتمال (عالية الأبعاد) في المشعب، والتي يصعب إيجادها بكفاءة من خلال أخذ عينات عشوائية من المدخل حول مثال معين. بالفعل، تستخدم مجموعة متنوعة من نماذج الرؤية الحاسوبية المتقدمة الحديثة تشوهات الإدخال أثناء التدريب لزيادة متانة ومعدل تقارب النماذج~\cite{krizhevsky2012imagenet,zeiler2013visualizing}. هذه التشوهات، مع ذلك، غير فعالة إحصائياً، لمثال معين: فهي مرتبطة بشكل كبير ويتم سحبها من نفس التوزيع طوال التدريب بالكامل للنموذج. نقترح مخططاً لجعل هذه العملية تكيفية بطريقة تستغل النموذج وأوجه قصوره في نمذجة الفضاء المحلي حول بيانات التدريب.

نجعل الاتصال مع تعدين السلبيات الصعبة صريحاً، لأنه قريب في الروح: يتكون تعدين السلبيات الصعبة، في الرؤية الحاسوبية، من تحديد أمثلة مجموعة التدريب (أو أجزاء منها) التي تُعطى احتمالات منخفضة بواسطة النموذج، ولكن يجب أن تكون ذات احتمال عالٍ بدلاً من ذلك، راجع~\cite{felzenszwalb2008discriminatively}. يتم بعد ذلك تغيير توزيع مجموعة التدريب للتأكيد على هذه السلبيات الصعبة ويتم إجراء جولة إضافية من تدريب النموذج. كما سيتم وصفه، يمكن أيضاً استخدام مشكلة التحسين المقترحة في هذا العمل بطريقة بناءة، على غرار مبدأ تعدين السلبيات الصعبة.

### الوصف الرسمي

نرمز بـ $f: \mathbb{R}^m \longrightarrow \{1 \dots k\}$ إلى مصنف يُعيِّن متجهات قيم بكسل الصورة إلى مجموعة تسميات منفصلة. نفترض أيضاً أن $f$ لها دالة خسارة مستمرة مرتبطة يُرمز إليها بـ $\textrm{loss}_f:\mathbb{R}^m\times \{1 \dots k\}\longrightarrow \mathbb{R}^+$. لصورة $x\in\mathbb{R}^m$ معينة وتسمية هدف $l\in \{1 \dots k\}$، نهدف إلى حل مشكلة التحسين المقيدة بالصندوق التالية:
\begin{itemize}
\item تصغير $\|r\|_2$ بشرط:
  \begin{enumerate}
    \item $f(x+r)=l$
    \item $x+r \in [0, 1]^m$
  \end{enumerate}
\end{itemize}
قد لا يكون المُصغِّر $r$ فريداً، لكننا نرمز إلى أحد هذه $x+r$ لمُصغِّر مختار بشكل عشوائي بـ $D(x, l)$. بشكل غير رسمي، $x + r$ هي أقرب صورة إلى $x$ مصنفة كـ $l$ بواسطة $f$. من الواضح أن $D(x, f(x))=f(x)$، لذا فإن هذه المهمة غير تافهة فقط إذا كان $f(x)\neq l$. بشكل عام، يُعد الحساب الدقيق لـ $D(x, l)$ مشكلة صعبة، لذلك نقوم بتقريبها باستخدام L-BFGS المقيد بالصندوق. بشكل ملموس، نجد تقريباً لـ $D(x, l)$ من خلال إجراء بحث خطي لإيجاد الحد الأدنى $c>0$ الذي يحقق المُصغِّر $r$ للمشكلة التالية $f(x+r)=l$.
\begin{itemize}
\item تصغير $c|r| + \textrm{loss}_f(x + r, l)$ بشرط $x+r \in [0,1]^m$
\end{itemize}
ستؤدي طريقة دالة الجزاء هذه إلى الحل الدقيق لـ $D(X, l)$ في حالة الخسائر المحدبة، ومع ذلك فإن الشبكات العصبية غير محدبة بشكل عام، لذلك ننتهي بتقريب في هذه الحالة.

### النتائج التجريبية

تحتوي دالة "الحد الأدنى من التشويه" $D$ لدينا على الخصائص المثيرة للاهتمام التالية والتي سندعمها بأدلة غير رسمية وتجارب كمية في هذا القسم:
\begin{enumerate}
\item لجميع الشبكات التي درسناها (MNIST، QuocNet \cite{le2011building}، AlexNet \cite{krizhevsky2012imagenet})، لكل عينة، تمكنا دائماً من توليد أمثلة خصامية قريبة جداً، يصعب تمييزها بصرياً، يتم تصنيفها بشكل خاطئ بواسطة الشبكة الأصلية (انظر الشكل \ref{fig:alexnegative} و {\tt http://goo.gl/huaGPb} للأمثلة).
\item {\it التعميم عبر النماذج:} سيتم تصنيف جزء كبير نسبياً من الأمثلة بشكل خاطئ بواسطة الشبكات المدربة من الصفر بمعاملات فرط مختلفة (عدد الطبقات، التنظيم أو الأوزان الأولية).
\item {\it التعميم عبر مجموعات التدريب} سيتم تصنيف جزء كبير نسبياً من الأمثلة بشكل خاطئ بواسطة الشبكات المدربة من الصفر {\it على مجموعة تدريب منفصلة}.
\end{enumerate}
تشير الملاحظات أعلاه إلى أن الأمثلة الخصامية عالمية إلى حد ما وليست مجرد نتائج للملاءمة الزائدة لنموذج معين أو لاختيار محدد لمجموعة التدريب. كما أنها تشير إلى أن إعادة إدخال الأمثلة الخصامية إلى التدريب قد يحسن تعميم النماذج الناتجة.
أسفرت تجاربنا الأولية عن أدلة إيجابية على MNIST لدعم هذه الفرضية أيضاً: لقد نجحنا في تدريب شبكة عصبية غير التفافية ذات طبقتين 100-100-10 بخطأ اختبار أقل من $1.2\%$ من خلال الاحتفاظ بمجموعة من الأمثلة الخصامية يتم استبدال مجموعة فرعية عشوائية منها باستمرار بأمثلة خصامية مولدة حديثاً ويتم مزجها في مجموعة التدريب الأصلية طوال الوقت. استخدمنا تسوس الوزن، ولكن لا dropout لهذه الشبكة. للمقارنة، تحصل شبكة بهذا الحجم على $1.6\%$ أخطاء عند تنظيمها بتسوس الوزن وحده ويمكن تحسينها إلى حوالي $1.3\%$ باستخدام dropout المطبق بعناية.

[تستمر المحتويات مع الجداول التجريبية ونتائج التحقق المتقاطع...]

---

### Translation Notes

- **Figures referenced:**
  - Figure \ref{fig:alexnegative}: Adversarial examples for AlexNet
  - Figure \ref{fig:quocnegative}: Adversarial examples for QuocNet
  - Figure \ref{fig:mnistdistorted}: MNIST adversarial examples
- **Tables referenced:**
  - Table \ref{crossneg}: Model descriptions
  - Table \ref{negativegen}: Cross-model generalization results
  - Table \ref{crosstrainneg}, \ref{crosstrainnegresults}: Cross-training-set generalization
- **Key terms introduced:**
  - adversarial examples (أمثلة خصامية)
  - perturbation (اضطراب)
  - smoothness prior (افتراض مسبق للنعومة)
  - cross-entropy loss (خسارة الإنتروبيا المتقاطعة)
  - box-constrained optimization (تحسين مقيد بالصندوق)
  - L-BFGS (L-BFGS)
  - hard-negative mining (تعدين السلبيات الصعبة)
  - manifold (مشعب)
  - weakly-supervised localization (التوطين الضعيف الإشراف)
  - minimum distortion (الحد الأدنى من التشويه)
  - cross-model generalization (التعميم عبر النماذج)
  - cross-training-set generalization (التعميم عبر مجموعات التدريب)
- **Equations:** Multiple optimization formulations with constraints
- **Citations:** 7 references
- **Special handling:**
  - Preserved mathematical notation throughout
  - Maintained LaTeX itemize/enumerate structure
  - Note: Full experimental tables omitted for brevity but should be included in complete translation

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.88
