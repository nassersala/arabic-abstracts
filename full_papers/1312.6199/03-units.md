# Section 3: Units of $\phi(x)$
## القسم 3: وحدات $\phi(x)$

**Section:** units-analysis
**Translation Quality:** 0.86
**Glossary Terms Used:** feature extraction, activation, hidden unit, semantic, basis vector, random direction, convolutional neural network, natural basis

---

### English Version

Traditional computer vision systems rely on feature extraction:
often a single feature is easily interpretable, e.g. a histogram of colors, or quantized local derivatives. This allows one to
inspect the individual coordinates of the feature space, and link them back to meaningful variations in the input domain.
Similar reasoning was used in previous work that attempted to analyze neural networks that were applied to computer vision problems.
These works interpret an activation of a hidden unit as
a meaningful feature. They look for input images which maximize the activation value of this single feature~\cite{girshick2013rich, zeiler2013visualizing, goodfellow2009measuring,erhan2009visualization}.

The aforementioned technique can be formally stated as visual inspection of images $x'$, which satisfy (or are close to maximum attainable value):
\begin{align*}
	x' = \argmax_{x \in \mathcal{I}} \langle \phi(x), e_i \rangle
\end{align*}
where $\mathcal{I}$ is a held-out set of images from the data distribution that the network
was not trained on and $e_i$ is the natural basis vector associated with the $i$-th hidden unit.

Our experiments show that any random direction $v \in \mathbb{R}^n$ gives rise to similarly interpretable
semantic properties. More formally, we find that images $x'$ are semantically related to each
other, for many $x'$ such that
\begin{align*}
	x' = \argmax_{x \in \mathcal{I}} \langle \phi(x), v \rangle
\end{align*}

This suggests that the natural basis is not better than a random basis for inspecting the properties of $\phi(x)$. This puts into question the notion that neural networks disentangle variation factors across coordinates.

First, we evaluated the above claim using a convolutional neural network trained on MNIST.
We used the MNIST test set for $\mathcal{I}$.
Figure \ref{fig:natural}
shows images that maximize the activations in the natural basis, and Figure \ref{fig:random} shows images
that maximize the activation in random directions. In both cases the resulting images share many high-level similarities.

Next, we repeated our experiment on an AlexNet, where we used the validation set as $\mathcal{I}$. Figures \ref{fig:natural_imagenet} and \ref{fig:random_imagenet} compare the natural basis to the random basis on the trained network. The rows appear to be semantically meaningful for both the single unit and the combination of units.

Although such analysis gives insight on the capacity of $\phi$ to generate invariance on a particular subset of the input
distribution, it does not explain the behavior on the rest of its domain. We shall see in the next section that $\phi$ has
counterintuitive properties in the neighbourhood of almost every point form data distribution.

---

### النسخة العربية

تعتمد أنظمة الرؤية الحاسوبية التقليدية على استخراج الميزات: غالباً ما تكون ميزة واحدة قابلة للتفسير بسهولة، على سبيل المثال رسم بياني للألوان، أو المشتقات المحلية المكممة. هذا يسمح للمرء بفحص الإحداثيات الفردية لفضاء الميزات، وربطها مرة أخرى بالتغيرات ذات المعنى في مجال الإدخال. تم استخدام استدلال مماثل في الأعمال السابقة التي حاولت تحليل الشبكات العصبية التي تم تطبيقها على مشاكل الرؤية الحاسوبية. تفسر هذه الأعمال تنشيط وحدة مخفية على أنه ميزة ذات معنى. يبحثون عن صور إدخال تُعظِّم قيمة تنشيط هذه الميزة الواحدة~\cite{girshick2013rich, zeiler2013visualizing, goodfellow2009measuring,erhan2009visualization}.

يمكن صياغة التقنية المذكورة أعلاه بشكل رسمي على أنها فحص بصري للصور $x'$، التي تحقق (أو قريبة من القيمة القصوى القابلة للتحقيق):
\begin{align*}
	x' = \argmax_{x \in \mathcal{I}} \langle \phi(x), e_i \rangle
\end{align*}
حيث $\mathcal{I}$ هي مجموعة محجوزة من الصور من توزيع البيانات التي لم يتم تدريب الشبكة عليها و $e_i$ هو متجه الأساس الطبيعي المرتبط بالوحدة المخفية $i$.

تُظهر تجاربنا أن أي اتجاه عشوائي $v \in \mathbb{R}^n$ يؤدي إلى خصائص دلالية قابلة للتفسير بشكل مماثل. بشكل أكثر رسمية، نجد أن الصور $x'$ مرتبطة دلالياً ببعضها البعض، للكثير من $x'$ بحيث
\begin{align*}
	x' = \argmax_{x \in \mathcal{I}} \langle \phi(x), v \rangle
\end{align*}

هذا يشير إلى أن الأساس الطبيعي ليس أفضل من أساس عشوائي لفحص خصائص $\phi(x)$. هذا يضع موضع تساؤل فكرة أن الشبكات العصبية تفصل عوامل التباين عبر الإحداثيات.

أولاً، قمنا بتقييم الادعاء أعلاه باستخدام شبكة عصبية التفافية مدربة على MNIST. استخدمنا مجموعة اختبار MNIST لـ $\mathcal{I}$. يُظهر الشكل \ref{fig:natural} صوراً تُعظِّم التنشيطات في الأساس الطبيعي، ويُظهر الشكل \ref{fig:random} صوراً تُعظِّم التنشيط في الاتجاهات العشوائية. في كلتا الحالتين، تتشارك الصور الناتجة العديد من أوجه التشابه عالية المستوى.

بعد ذلك، كررنا تجربتنا على AlexNet، حيث استخدمنا مجموعة التحقق كـ $\mathcal{I}$. تقارن الأشكال \ref{fig:natural_imagenet} و \ref{fig:random_imagenet} الأساس الطبيعي بالأساس العشوائي على الشبكة المدربة. تبدو الصفوف ذات معنى دلالي لكل من الوحدة الواحدة ومزيج الوحدات.

على الرغم من أن مثل هذا التحليل يعطي نظرة ثاقبة على قدرة $\phi$ على توليد الثبات على مجموعة فرعية معينة من توزيع الإدخال، فإنه لا يفسر السلوك على بقية مجاله. سنرى في القسم التالي أن $\phi$ لديه خصائص متناقضة في جوار كل نقطة تقريباً من توزيع البيانات.

---

### Translation Notes

- **Figures referenced:**
  - Figure \ref{fig:natural}: MNIST images maximizing natural basis activations
  - Figure \ref{fig:random}: MNIST images maximizing random direction activations
  - Figure \ref{fig:natural_imagenet}: ImageNet images with natural basis
  - Figure \ref{fig:random_imagenet}: ImageNet images with random basis
- **Key terms introduced:**
  - feature extraction (استخراج الميزات)
  - feature space (فضاء الميزات)
  - natural basis (أساس طبيعي)
  - random direction (اتجاه عشوائي)
  - basis vector (متجه الأساس)
  - held-out set (مجموعة محجوزة)
  - validation set (مجموعة التحقق)
  - invariance (الثبات)
- **Equations:** 2 optimization equations using argmax
- **Citations:** 4 references to visualization and analysis methods
- **Special handling:**
  - Preserved mathematical notation: $\argmax$, $\langle \phi(x), e_i \rangle$ (inner product)
  - Maintained Greek letter $\phi$ for representation function
  - Kept figure references as \ref{} for LaTeX compatibility

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.84
- Glossary consistency: 0.86
- **Overall section score:** 0.86
