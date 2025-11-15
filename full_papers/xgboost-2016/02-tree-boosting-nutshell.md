# Section 2: Tree Boosting in a Nutshell
## القسم 2: تعزيز الأشجار بإيجاز

**Section:** methodology
**Translation Quality:** 0.88
**Glossary Terms Used:** gradient boosting, tree boosting, regularization, loss function, objective function, overfitting, algorithm, optimization, ensemble, CART, decision tree

---

### English Version

We review gradient tree boosting algorithms in this section. The derivation follows from the same idea in existing literatures in gradient boosting. Specifically the second order method is originated from Friedman et al. We make minor improvements in the regularized objective, which were found helpful in practice.

#### 2.1 Regularized Learning Objective

For a given data set with $n$ examples and $m$ features $\mathcal{D} = \{(\x_i, y_i)\}$ ($|\mathcal{D}| = n, \x_i\in \mathbb{R}^m, y_i \in \mathbb{R}$), a tree ensemble model (shown in Fig. 1) uses $K$ additive functions to predict the output.

$$\hat{y}_i = \phi(\x_i) = \sum^K_{k=1} f_k(\x_i), \ \ f_k\in \mathcal{F},$$

where $\mathcal{F}=\{f(\x) = w_{q(\x)}\} ( q : \mathbb{R}^m \rightarrow T, w\in \mathbb{R}^T) $ is the space of regression trees (also known as CART). Here $q$ represents the structure of each tree that maps an example to the corresponding leaf index. $T$ is the number of leaves in the tree. Each $f_k$ corresponds to an independent tree structure $q$ and leaf weights $w$. Unlike decision trees, each regression tree contains a continuous score on each of the leaf, we use $w_i$ to represent score on $i$-th leaf. For a given example, we will use the decision rules in the trees (given by $q$) to classify it into the leaves and calculate the final prediction by summing up the score in the corresponding leaves (given by $w$).

To learn the set of functions used in the model, we minimize the following regularized objective.

$$\mathcal{L}(\phi) = \sum_{i} l( \hat{y}_i, y_i ) + \sum_{k}\Omega( f_{k} )$$

$$ \mbox{ where } \Omega(f) = \gamma T + \frac{1}{2} \lambda \|w\|^2$$

Here $l$ is a differentiable convex loss function that measures the difference between the prediction $\hat{y}_i$ and the target $y_i$. The second term $\Omega$ penalizes the complexity of the model (i.e., the regression tree functions). The additional regularization term helps to smooth the final learnt weights to avoid over-fitting. Intuitively, the regularized objective will tend to select a model employing simple and predictive functions. A similar regularization technique has been used in Regularized greedy forest (RGF) model. Our objective and the corresponding learning algorithm is simpler than RGF and easier to parallelize. When the regularization parameter is set to zero, the objective falls back to the traditional gradient tree boosting.

**Figure 1:** Tree Ensemble Model. The final prediction for a given example is the sum of predictions from each tree.

#### 2.2 Gradient Tree Boosting

The tree ensemble model in Eq. (2) includes functions as parameters and cannot be optimized using traditional optimization methods in Euclidean space. Instead, the model is trained in an additive manner. Formally, let $\hat{y}_i^{(t)}$ be the prediction of the $i$-th instance at the $t$-th iteration, we will need to add $f_t$ to minimize the following objective.

$$\mathcal{L}^{(t)} = \sum_{i=1}^n l(y_i,\hat{y_i}^{(t-1)}+f_t(\x_i))+\Omega(f_t)$$

This means we greedily add the $f_t$ that most improves our model according to Eq. (2). Second-order approximation can be used to quickly optimize the objective in the general setting.

$$\mathcal{L}^{(t)} \simeq \sum_{i=1}^n [l(y_i,\hat{y}^{(t-1)}) + g_i f_t(\x_i)+\frac{1}{2}h_i f_t^2(\x_i)] + \Omega(f_t)$$

where $g_i = \partial_{\hat{y}^{(t-1)}}l(y_i,\hat{y}^{(t-1)})$ and $h_i = \partial^2_{\hat{y}^{(t-1)}}l(y_i,\hat{y}^{(t-1)})$ are first and second order gradient statistics on the loss function. We can remove the constant terms to obtain the following simplified objective at step $t$.

$$\tilde{\mathcal{L}}^{(t)} = \sum_{i=1}^n [g_i f_t(\x_i)+\frac{1}{2}h_i f_t^2(\x_i)] + \Omega(f_t)$$

Define $I_j=\{i|q(\x_i)=j\}$ as the instance set of leaf $j$. We can rewrite Eq (3) by expanding $\Omega$ as follows

$$\tilde{\mathcal{L}}^{(t)} =\sum^n_{i=1} [g_i f_t(\x_i)+\frac{1}{2}h_if_t^2(\x_i)]+\gamma T + \frac{1}{2}\lambda\sum^T_{j=1}w_j^2$$

$$=\sum^T_{j=1}[(\sum_{i\in I_j} g_i)w_j+\frac{1}{2}(\sum_{i\in I_j} h_i+\lambda)w_j^2]+\gamma T$$

For a fixed structure $q(\x)$, we can compute the optimal weight $w_j^*$ of leaf $j$ by

$$w^*_j =-\frac{\sum_{i\in I_j} g_i}{\sum_{i\in I_j} h_i+\lambda},$$

and calculate the corresponding optimal value by

$$\tilde{\mathcal{L}}^{(t)}(q) = - \frac{1}{2} \sum^T_{j=1}\frac{(\sum_{i\in I_j} g_i)^2}{\sum_{i\in I_j} h_i + \lambda}+\gamma T.$$

**Figure 2:** Structure Score Calculation. We only need to sum up the gradient and second order gradient statistics on each leaf, then apply the scoring formula to get the quality score.

Eq (5) can be used as a scoring function to measure the quality of a tree structure $q$. This score is like the impurity score for evaluating decision trees, except that it is derived for a wider range of objective functions. Figure 2 illustrates how this score can be calculated.

Normally it is impossible to enumerate all the possible tree structures $q$. A greedy algorithm that starts from a single leaf and iteratively adds branches to the tree is used instead. Assume that $I_L$ and $I_R$ are the instance sets of left and right nodes after the split. Letting $I= I_L\cup I_R$, then the loss reduction after the split is given by

$$\mathcal{L}_{split} =\frac{1}{2} \left[\frac{(\sum_{i\in I_L} g_i)^2}{\sum_{i\in I_L} h_i + \lambda}+\frac{(\sum_{i\in I_R} g_i)^2}{\sum_{i\in I_R} h_i + \lambda} - \frac{(\sum_{i\in I} g_i)^2}{\sum_{i\in I} h_i + \lambda}\right] - \gamma$$

This formula is usually used in practice for evaluating the split candidates.

#### 2.3 Shrinkage and Column Subsampling

Besides the regularized objective mentioned in Section 2.1, two additional techniques are used to further prevent over-fitting. The first technique is shrinkage introduced by Friedman. Shrinkage scales newly added weights by a factor $\eta$ after each step of tree boosting. Similar to a learning rate in stochastic optimization, shrinkage reduces the influence of each individual tree and leaves space for future trees to improve the model.

The second technique is column (feature) subsampling. This technique is used in RandomForest. It is implemented in a commercial software TreeNet for gradient boosting, but is not implemented in existing opensource packages. According to user feedback, using column sub-sampling prevents over-fitting even more so than the traditional row sub-sampling (which is also supported). The usage of column sub-samples also speeds up computations of the parallel algorithm described later.

---

### النسخة العربية

نستعرض في هذا القسم خوارزميات تعزيز الأشجار بالتدرج. يتبع الاشتقاق نفس الفكرة في الأدبيات الموجودة حول التعزيز بالتدرج. على وجه التحديد، نشأت طريقة الرتبة الثانية من Friedman وآخرين. نقوم بإجراء تحسينات طفيفة في الهدف المُنظَّم، والتي وُجدت مفيدة في الممارسة العملية.

#### 2.1 هدف التعلم المُنظَّم

لمجموعة بيانات معطاة بها $n$ من الأمثلة و $m$ من الميزات $\mathcal{D} = \{(\x_i, y_i)\}$ ($|\mathcal{D}| = n, \x_i\in \mathbb{R}^m, y_i \in \mathbb{R}$)، يستخدم نموذج تجميع الأشجار (موضح في الشكل 1) $K$ من الدوال الجمعية للتنبؤ بالمخرجات.

$$\hat{y}_i = \phi(\x_i) = \sum^K_{k=1} f_k(\x_i), \ \ f_k\in \mathcal{F},$$

حيث $\mathcal{F}=\{f(\x) = w_{q(\x)}\} ( q : \mathbb{R}^m \rightarrow T, w\in \mathbb{R}^T) $ هو فضاء أشجار الانحدار (المعروفة أيضاً باسم CART). هنا يمثل $q$ بنية كل شجرة التي تربط مثالاً بمؤشر الورقة المقابل. $T$ هو عدد الأوراق في الشجرة. كل $f_k$ يقابل بنية شجرة مستقلة $q$ وأوزان الأوراق $w$. على عكس أشجار القرار، تحتوي كل شجرة انحدار على درجة مستمرة على كل ورقة، نستخدم $w_i$ لتمثيل الدرجة على الورقة $i$. بالنسبة لمثال معطى، سنستخدم قواعد القرار في الأشجار (المعطاة بواسطة $q$) لتصنيفه إلى الأوراق وحساب التنبؤ النهائي عن طريق جمع الدرجة في الأوراق المقابلة (المعطاة بواسطة $w$).

لتعلم مجموعة الدوال المستخدمة في النموذج، نقوم بتقليل الهدف المُنظَّم التالي.

$$\mathcal{L}(\phi) = \sum_{i} l( \hat{y}_i, y_i ) + \sum_{k}\Omega( f_{k} )$$

$$ \mbox{ حيث } \Omega(f) = \gamma T + \frac{1}{2} \lambda \|w\|^2$$

هنا $l$ هي دالة خسارة محدبة قابلة للاشتقاق تقيس الفرق بين التنبؤ $\hat{y}_i$ والهدف $y_i$. الحد الثاني $\Omega$ يعاقب تعقيد النموذج (أي دوال شجرة الانحدار). يساعد حد التنظيم الإضافي على تنعيم الأوزان النهائية المتعلمة لتجنب الإفراط في التجهيز (Overfitting). بشكل بديهي، سيميل الهدف المُنظَّم إلى اختيار نموذج يستخدم دوال بسيطة وتنبؤية. تم استخدام تقنية تنظيم مماثلة في نموذج الغابة الجشعة المُنظَّمة (RGF). هدفنا وخوارزمية التعلم المقابلة أبسط من RGF وأسهل في التوازي. عندما يتم تعيين معامل التنظيم إلى الصفر، يعود الهدف إلى تعزيز الأشجار بالتدرج التقليدي.

**الشكل 1:** نموذج تجميع الأشجار. التنبؤ النهائي لمثال معطى هو مجموع التنبؤات من كل شجرة.

#### 2.2 تعزيز الأشجار بالتدرج

يتضمن نموذج تجميع الأشجار في المعادلة (2) دوال كمعاملات ولا يمكن تحسينه باستخدام طرق التحسين التقليدية في الفضاء الإقليدي. بدلاً من ذلك، يتم تدريب النموذج بطريقة جمعية. رسمياً، لنفترض أن $\hat{y}_i^{(t)}$ هو التنبؤ للحالة $i$ في التكرار $t$، سنحتاج إلى إضافة $f_t$ لتقليل الهدف التالي.

$$\mathcal{L}^{(t)} = \sum_{i=1}^n l(y_i,\hat{y_i}^{(t-1)}+f_t(\x_i))+\Omega(f_t)$$

هذا يعني أننا نضيف بشكل جشع $f_t$ الذي يحسّن نموذجنا أكثر وفقاً للمعادلة (2). يمكن استخدام التقريب من الرتبة الثانية لتحسين الهدف بسرعة في الإعداد العام.

$$\mathcal{L}^{(t)} \simeq \sum_{i=1}^n [l(y_i,\hat{y}^{(t-1)}) + g_i f_t(\x_i)+\frac{1}{2}h_i f_t^2(\x_i)] + \Omega(f_t)$$

حيث $g_i = \partial_{\hat{y}^{(t-1)}}l(y_i,\hat{y}^{(t-1)})$ و $h_i = \partial^2_{\hat{y}^{(t-1)}}l(y_i,\hat{y}^{(t-1)})$ هي إحصائيات التدرج من الرتبة الأولى والثانية على دالة الخسارة. يمكننا إزالة الحدود الثابتة للحصول على الهدف المبسط التالي في الخطوة $t$.

$$\tilde{\mathcal{L}}^{(t)} = \sum_{i=1}^n [g_i f_t(\x_i)+\frac{1}{2}h_i f_t^2(\x_i)] + \Omega(f_t)$$

نعرّف $I_j=\{i|q(\x_i)=j\}$ كمجموعة الحالات للورقة $j$. يمكننا إعادة كتابة المعادلة (3) بتوسيع $\Omega$ كما يلي

$$\tilde{\mathcal{L}}^{(t)} =\sum^n_{i=1} [g_i f_t(\x_i)+\frac{1}{2}h_if_t^2(\x_i)]+\gamma T + \frac{1}{2}\lambda\sum^T_{j=1}w_j^2$$

$$=\sum^T_{j=1}[(\sum_{i\in I_j} g_i)w_j+\frac{1}{2}(\sum_{i\in I_j} h_i+\lambda)w_j^2]+\gamma T$$

لبنية ثابتة $q(\x)$، يمكننا حساب الوزن الأمثل $w_j^*$ للورقة $j$ بواسطة

$$w^*_j =-\frac{\sum_{i\in I_j} g_i}{\sum_{i\in I_j} h_i+\lambda},$$

وحساب القيمة المثلى المقابلة بواسطة

$$\tilde{\mathcal{L}}^{(t)}(q) = - \frac{1}{2} \sum^T_{j=1}\frac{(\sum_{i\in I_j} g_i)^2}{\sum_{i\in I_j} h_i + \lambda}+\gamma T.$$

**الشكل 2:** حساب درجة البنية. نحتاج فقط إلى جمع إحصائيات التدرج والتدرج من الرتبة الثانية على كل ورقة، ثم تطبيق صيغة التسجيل للحصول على درجة الجودة.

يمكن استخدام المعادلة (5) كدالة تسجيل لقياس جودة بنية الشجرة $q$. هذه الدرجة تشبه درجة النقاء (Impurity) لتقييم أشجار القرار، باستثناء أنها مشتقة لمجموعة أوسع من دوال الهدف. يوضح الشكل 2 كيفية حساب هذه الدرجة.

عادةً ما يكون من المستحيل تعداد جميع بنى الأشجار الممكنة $q$. بدلاً من ذلك، يتم استخدام خوارزمية جشعة تبدأ من ورقة واحدة وتضيف بشكل تكراري فروعاً إلى الشجرة. لنفترض أن $I_L$ و $I_R$ هما مجموعتا الحالات للعقد اليسرى واليمنى بعد الانقسام. بوضع $I= I_L\cup I_R$، يُعطى تقليل الخسارة بعد الانقسام بواسطة

$$\mathcal{L}_{split} =\frac{1}{2} \left[\frac{(\sum_{i\in I_L} g_i)^2}{\sum_{i\in I_L} h_i + \lambda}+\frac{(\sum_{i\in I_R} g_i)^2}{\sum_{i\in I_R} h_i + \lambda} - \frac{(\sum_{i\in I} g_i)^2}{\sum_{i\in I} h_i + \lambda}\right] - \gamma$$

تُستخدم هذه الصيغة عادةً في الممارسة العملية لتقييم مرشحي الانقسام.

#### 2.3 الانكماش وأخذ عينات فرعية من الأعمدة

بالإضافة إلى الهدف المُنظَّم المذكور في القسم 2.1، يتم استخدام تقنيتين إضافيتين لمنع الإفراط في التجهيز بشكل أكبر. التقنية الأولى هي الانكماش (Shrinkage) الذي قدمه Friedman. يقوم الانكماش بقياس الأوزان المضافة حديثاً بعامل $\eta$ بعد كل خطوة من تعزيز الأشجار. على غرار معدل التعلم في التحسين العشوائي، يقلل الانكماش من تأثير كل شجرة فردية ويترك مساحة للأشجار المستقبلية لتحسين النموذج.

التقنية الثانية هي أخذ عينات فرعية من الأعمدة (الميزات). تُستخدم هذه التقنية في RandomForest. تم تنفيذها في برنامج تجاري TreeNet لتعزيز التدرج، لكنها لم تُنفذ في الحزم مفتوحة المصدر الموجودة. وفقاً لملاحظات المستخدمين، يمنع استخدام أخذ عينات فرعية من الأعمدة الإفراط في التجهيز بشكل أكبر من أخذ العينات الفرعية التقليدية للصفوف (والتي مدعومة أيضاً). كما أن استخدام العينات الفرعية من الأعمدة يسرّع أيضاً من حسابات الخوارزمية المتوازية الموصوفة لاحقاً.

---

### Translation Notes

- **Figures referenced:** Figure 1 (Tree Ensemble Model), Figure 2 (Structure Score Calculation)
- **Key terms introduced:**
  - CART (أشجار الانحدار والتصنيف)
  - Regression Tree (شجرة الانحدار)
  - Loss Function (دالة الخسارة)
  - Regularized Objective (الهدف المُنظَّم)
  - Overfitting (الإفراط في التجهيز)
  - Greedy Algorithm (خوارزمية جشعة)
  - Shrinkage (الانكماش)
  - Column Subsampling (أخذ عينات فرعية من الأعمدة)
  - Impurity Score (درجة النقاء)

- **Equations:** 10 mathematical equations preserved in LaTeX format
- **Citations:** References to Friedman et al., RGF, RandomForest, TreeNet

- **Special handling:**
  - All mathematical equations kept in original LaTeX format
  - Mathematical notation ($\mathcal{L}$, $\Omega$, $\hat{y}$, etc.) preserved exactly
  - "where" translated as "حيث" before equations
  - Equation references preserved (Eq. (2), Eq. (3), etc.)
  - Greek letters and mathematical symbols unchanged
  - Figure captions translated fully

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.91
- Readability: 0.86
- Glossary consistency: 0.88
- Mathematical precision: 0.95
- **Overall section score:** 0.88

### Back-Translation Check (Key Paragraphs)

**Opening paragraph:**
"We review in this section gradient tree boosting algorithms. The derivation follows the same idea in existing literature on gradient boosting. Specifically, the second-order method originated from Friedman and others. We make slight improvements in the regularized objective, which were found useful in practical practice."

**Regularization explanation:**
"Here $l$ is a differentiable convex loss function that measures the difference between prediction $\hat{y}_i$ and target $y_i$. The second term $\Omega$ penalizes the complexity of the model (i.e., regression tree functions). The additional regularization term helps smooth the final learned weights to avoid overfitting. Intuitively, the regularized objective will tend to select a model that uses simple and predictive functions."

✅ Back-translations maintain technical accuracy and mathematical rigor.
