# Section 5: Spectral Analysis of Unstability
## القسم 5: التحليل الطيفي لعدم الاستقرار

**Section:** spectral-analysis
**Translation Quality:** 0.85
**Glossary Terms Used:** perturbation, Lipschitz constant, operator norm, singular value, convolutional layer, fully connected layer, max-pooling, rectified layer, Fourier transform, regularization

---

### English Version

The previous section showed examples
of deep networks resulting from
purely supervised training
which are unstable with respect to a peculiar
form of small perturbations.
Independently of their generalisation properties across
networks and training sets, the adversarial examples
show that there exist small additive perturbations of the input (in Euclidean sense)
that produce large perturbations at the output of the last layer.
This section describes a simple procedure to
measure and control the additive stability of the network
by measuring the spectrum of each rectified layer.

Mathematically, if $\phi(x)$ denotes the output of a network
of $K$ layers corresponding to input $x$ and trained parameters $W$,
we write
$$\phi(x) = \phi_K( \phi_{K-1}( \dots \phi_1(x; W_1) ; W_2 )\dots ; W_K)~,$$
where $\phi_k$ denotes the operator mapping layer $k-1$ to layer $k$.
The unstability of $\phi(x)$ can be explained by inspecting the upper Lipschitz constant
of each layer $k=1\dots K$, defined as the constant $L_k>0$ such that
$$\forall\, x,\,r~,~ \| \phi_k(x; W_k) - \phi_k(x+r; W_k) \| \leq L_k \| r \|~.$$
The resulting network thus satsifies $\| \phi(x) - \phi(x+r) \| \leq L \| r \|$, with
$L = \prod_{k=1}^K L_k$.

A half-rectified layer (both convolutional or fully connected) is defined by the mapping
$\phi_k(x; W_k,b_k) = \max(0, W_k x+b_k)$.
Let $\|W \|$ denote the operator norm of $W$ (i.e., its largest singular value).
Since the non-linearity $\rho(x) = \max(0,x)$ is contractive, i.e. satisfies
$\| \rho(x) - \rho(x+r) \| \leq \| r\|~$ for all $x,r$;  it follows that
 $$ \| \phi_k(x; W_k) - \phi_k(x+r; W_k) \| = \| \max(0,W_k x + b_k) - \max(0,W_k (x+r) + b_k) \| \leq \| W_k r \| \leq \|W_k \| \| r\|~,$$
 and hence $L_k \leq \|W_k\|$.
On the other hand, a max-pooling layer $\phi_k$ is contractive:
$$\forall\, x\,,\,r\,,~\| \phi_k(x) - \phi_k(x+r) \| \leq \| r\| ~,$$
since its Jacobian is a projection onto a subset of the input coordinates
and hence does not expand the gradients.
Finally, if $\phi_k$ is a contrast-normalization layer
$$\phi_k(x) = \frac{x}{\Big( \epsilon + \|x \|^2 \Big)^\gamma}~,$$
one can verify that
$$\forall\, x\,,\,r\,,~\| \phi_k(x) - \phi_k(x+r) \| \leq  \epsilon^{-\gamma} \| r\| $$
for $\gamma \in [0.5,1]$, which corresponds to most common operating
regimes.

It results that a conservative measure of the
unstability of the network can be obtained by simply computing
the operator norm of each fully connected and convolutional layer.
The fully connected case is trivial since the norm is directly given
by the largest singular value of the fully connected matrix.
Let us describe the convolutional case.
If $W$ denotes a generic $4$-tensor, implementing a convolutional layer with
$C$ input features, $D$ output features, support $N\times N$ and spatial stride $\Delta$,
$$W x = \left\{  \sum_{c=1}^C x_c \star w_{c,d} (n_1 \Delta, n_2 \Delta) \, ; d=1\,\dots,D\right\}~,$$
where $x_c$ denotes the $c$-th input feature image,
and $w_{c,d}$ is the spatial kernel corresponding to input feature $c$ and output feature $d$,
by applying Parseval's formula we obtain that
its operator norm is given by
\begin{equation}
\label{convbound}
\| W \| = \sup_{\xi \in [0,N \Delta^{-1})^2} \| A(\xi) \| ~,
\end{equation}
where $A(\xi)$ is a $D \times (C \cdot \Delta^{2})$ matrix whose rows are
$$\forall~d=1\dots D~,~A(\xi)_d =  \Big(\Delta^{-2}  \widehat{w_{c,d}}(\xi+ l \cdot N \cdot \Delta^{-1}) \,;\, c=1\dots C\, ,\, l=(0\dots \Delta-1)^2 \Big)~,$$
and $\widehat{w_{c,d}}$ is the 2-D Fourier transform of $w_{c,d}$:
$$\widehat{w_{c,d}}(\xi) = \sum_{u \in [0,N)^2} w_{c,d}(u) e^{- 2 \pi i (u \cdot \xi) / N^2}~.$$

Table \ref{bounds} shows the upper Lipschitz bounds computed from the ImageNet deep
convolutional network of \cite{krizhevsky2012imagenet}, using (\ref{convbound}).
 It shows that instabilities can appear as soon as in the first
convolutional layer.

These results are consistent with the exsitence of blind spots
constructed in the previous section, but they don't attempt to explain why
these examples generalize across different hyperparameters or training sets.
We emphasize that we compute upper bounds:
large bounds do not automatically translate into existence of adversarial examples;
however, small bounds guarantee that no such examples can appear.
This suggests a simple regularization of the parameters,
consisting in penalizing each upper Lipschitz bound,
which might help improve the generalisation error of the networks.

---

### النسخة العربية

أظهر القسم السابق أمثلة للشبكات العميقة الناتجة عن التدريب الخاضع للإشراف البحت والتي تكون غير مستقرة فيما يتعلق بشكل غريب من الاضطرابات الصغيرة. بشكل مستقل عن خصائص التعميم الخاصة بها عبر الشبكات ومجموعات التدريب، تُظهر الأمثلة الخصامية أنه توجد اضطرابات إضافية صغيرة للإدخال (بالمعنى الإقليدي) تنتج اضطرابات كبيرة في الإخراج للطبقة الأخيرة. يصف هذا القسم إجراءً بسيطاً لقياس والتحكم في الاستقرار الإضافي للشبكة من خلال قياس الطيف لكل طبقة مُصححة.

رياضياً، إذا كان $\phi(x)$ يشير إلى إخراج شبكة من $K$ طبقات تتوافق مع الإدخال $x$ والمعاملات المدربة $W$، نكتب
$$\phi(x) = \phi_K( \phi_{K-1}( \dots \phi_1(x; W_1) ; W_2 )\dots ; W_K)~,$$
حيث $\phi_k$ يشير إلى المشغل الذي يُعيِّن الطبقة $k-1$ إلى الطبقة $k$. يمكن تفسير عدم استقرار $\phi(x)$ من خلال فحص ثابت ليبشيتز العلوي لكل طبقة $k=1\dots K$، المعرَّف على أنه الثابت $L_k>0$ بحيث
$$\forall\, x,\,r~,~ \| \phi_k(x; W_k) - \phi_k(x+r; W_k) \| \leq L_k \| r \|~.$$
وبالتالي تحقق الشبكة الناتجة $\| \phi(x) - \phi(x+r) \| \leq L \| r \|$، مع $L = \prod_{k=1}^K L_k$.

تُعرَّف الطبقة نصف المُصححة (سواء كانت التفافية أو متصلة بالكامل) بالتعيين $\phi_k(x; W_k,b_k) = \max(0, W_k x+b_k)$. لنفرض أن $\|W \|$ تشير إلى معيار المشغل لـ $W$ (أي أكبر قيمة مفردة له). نظراً لأن عدم الخطية $\rho(x) = \max(0,x)$ انكماشي، أي يحقق $\| \rho(x) - \rho(x+r) \| \leq \| r\|~$ لجميع $x,r$؛ يتبع ذلك أن
 $$ \| \phi_k(x; W_k) - \phi_k(x+r; W_k) \| = \| \max(0,W_k x + b_k) - \max(0,W_k (x+r) + b_k) \| \leq \| W_k r \| \leq \|W_k \| \| r\|~,$$
 وبالتالي $L_k \leq \|W_k\|$.
من ناحية أخرى، فإن طبقة max-pooling $\phi_k$ انكماشية:
$$\forall\, x\,,\,r\,,~\| \phi_k(x) - \phi_k(x+r) \| \leq \| r\| ~,$$
نظراً لأن مصفوفة جاكوبيان الخاصة بها هي إسقاط على مجموعة فرعية من إحداثيات الإدخال وبالتالي لا توسع التدرجات.
أخيراً، إذا كانت $\phi_k$ طبقة تطبيع التباين
$$\phi_k(x) = \frac{x}{\Big( \epsilon + \|x \|^2 \Big)^\gamma}~,$$
يمكن للمرء التحقق من أن
$$\forall\, x\,,\,r\,,~\| \phi_k(x) - \phi_k(x+r) \| \leq  \epsilon^{-\gamma} \| r\| $$
لـ $\gamma \in [0.5,1]$، والذي يتوافق مع معظم أنظمة التشغيل الشائعة.

ينتج عن ذلك أنه يمكن الحصول على قياس محافظ لعدم استقرار الشبكة من خلال حساب معيار المشغل لكل طبقة متصلة بالكامل والتفافية ببساطة. حالة الاتصال الكامل تافهة نظراً لأن المعيار يُعطى مباشرة بأكبر قيمة مفردة للمصفوفة المتصلة بالكامل. دعونا نصف الحالة الالتفافية.
إذا كان $W$ يشير إلى موتر $4$ عام، يُنفذ طبقة التفافية مع $C$ ميزات إدخال، $D$ ميزات إخراج، دعم $N\times N$ وخطوة مكانية $\Delta$،
$$W x = \left\{  \sum_{c=1}^C x_c \star w_{c,d} (n_1 \Delta, n_2 \Delta) \, ; d=1\,\dots,D\right\}~,$$
حيث $x_c$ يشير إلى صورة ميزة الإدخال $c$، و $w_{c,d}$ هو النواة المكانية المقابلة لميزة الإدخال $c$ وميزة الإخراج $d$، من خلال تطبيق صيغة بارسيفال نحصل على أن معيار المشغل الخاص بها معطى بواسطة
\begin{equation}
\label{convbound}
\| W \| = \sup_{\xi \in [0,N \Delta^{-1})^2} \| A(\xi) \| ~,
\end{equation}
حيث $A(\xi)$ هي مصفوفة $D \times (C \cdot \Delta^{2})$ صفوفها هي
$$\forall~d=1\dots D~,~A(\xi)_d =  \Big(\Delta^{-2}  \widehat{w_{c,d}}(\xi+ l \cdot N \cdot \Delta^{-1}) \,;\, c=1\dots C\, ,\, l=(0\dots \Delta-1)^2 \Big)~,$$
و $\widehat{w_{c,d}}$ هو تحويل فورييه ثنائي الأبعاد لـ $w_{c,d}$:
$$\widehat{w_{c,d}}(\xi) = \sum_{u \in [0,N)^2} w_{c,d}(u) e^{- 2 \pi i (u \cdot \xi) / N^2}~.$$

يُظهر الجدول \ref{bounds} حدود ليبشيتز العليا المحسوبة من شبكة ImageNet العميقة الالتفافية في \cite{krizhevsky2012imagenet}، باستخدام (\ref{convbound}). يُظهر أن عدم الاستقرار يمكن أن يظهر في وقت مبكر في الطبقة الالتفافية الأولى.

هذه النتائج متسقة مع وجود النقاط العمياء المبنية في القسم السابق، لكنها لا تحاول شرح سبب تعميم هذه الأمثلة عبر معاملات فرط أو مجموعات تدريب مختلفة. نؤكد أننا نحسب الحدود العليا: الحدود الكبيرة لا تُترجم تلقائياً إلى وجود أمثلة خصامية؛ ومع ذلك، فإن الحدود الصغيرة تضمن عدم ظهور مثل هذه الأمثلة. هذا يقترح تنظيماً بسيطاً للمعاملات، يتكون من معاقبة كل حد ليبشيتز علوي، والذي قد يساعد في تحسين خطأ التعميم للشبكات.

---

### Translation Notes

- **Tables referenced:**
  - Table \ref{bounds}: Frame bounds of each rectified layer from AlexNet
- **Key terms introduced:**
  - Lipschitz constant (ثابت ليبشيتز)
  - operator norm (معيار المشغل)
  - singular value (قيمة مفردة)
  - half-rectified layer (طبقة نصف مُصححة)
  - contractive (انكماشي)
  - max-pooling layer (طبقة max-pooling)
  - Jacobian (مصفوفة جاكوبيان)
  - contrast-normalization (تطبيع التباين)
  - Fourier transform (تحويل فورييه)
  - Parseval's formula (صيغة بارسيفال)
  - spatial kernel (النواة المكانية)
  - 4-tensor (موتر 4)
  - spatial stride (خطوة مكانية)
  - frame bounds (حدود الإطار)
- **Equations:** Multiple mathematical derivations for Lipschitz bounds
- **Citations:** 1 reference to AlexNet
- **Special handling:**
  - Preserved all mathematical notation and Greek letters
  - Maintained equation numbering with \label{convbound}
  - Kept technical terms like max-pooling and ReLU untranslated where appropriate
  - Complex mathematical expressions preserved exactly

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.88
- Readability: 0.82
- Glossary consistency: 0.85
- **Overall section score:** 0.85
