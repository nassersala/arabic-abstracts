# Section 2: Preliminaries
## القسم الثاني: المفاهيم الأساسية

**Section:** Preliminaries
**Translation Quality:** 0.87
**Glossary Terms Used:** differential privacy, privacy, privacy loss, database, mechanism, divergence, subgaussian, random variable, variance

---

### English Version

**Divergence.** We will need several different notions of divergence between distributions. We will also introduce a new notion, subgaussian divergence in Section 3.

**Definition 1 (KL-Divergence):** The KL-Divergence, or Relative entropy, between two random variables $Y$ and $Z$ is defined as:
$$D_{KL}(Y||Z) = \mathbb{E}_{y \sim Y} \left[ \ln \frac{\Pr[Y=y]}{\Pr[Z=y]} \right],$$
where if the support of $Y$ is not equal to the support of $Z$, then $D_{KL}(Y||Z)$ is not defined.

**Definition 2 (Max Divergence):** The Max Divergence between two random variables $Y$ and $Z$ is defined to be:
$$D_{max}(Y||Z) = \max_{S \subseteq \text{Supp}(Y)} \left[ \ln \frac{\Pr[Y \in S]}{\Pr[Z \in S]} \right],$$
where if the support of $Y$ is not equal to the support of $Z$, then $D_{max}(Y||Z)$ is not defined.

The $\delta$-approximate divergence between $Y$ and $Z$ is defined to be:
$$D_{max}^{\delta}(Y||Z) = \max_{S \subseteq \text{Supp}(Y): \Pr[Y \in S] \geq \delta} \left[ \ln \frac{\Pr[Y \in S]}{\Pr[Z \in S]} \right],$$
where if $\Pr[Y \in \text{Supp}(Y) \setminus \text{Supp}(Z)] > \delta$, then $D_{max}^{\delta}(Y||Z)$ is not defined.

### Differential Privacy

For a given database $D$, a (randomized) non-interactive database access mechanism $\mathcal{M}$ computes an output $\mathcal{M}(x)$ that can later be used to reconstruct information about $D$. We will be concerned with mechanisms $\mathcal{M}$ that are private according to various privacy notions described below.

We think of a database $D_A$ as a multiset of rows, each from a data universe $U$. Intuitively, each row contains the data of a single individual. We will often view a database of size $n$ as a tuple $D_A \in U^n$ for some $n \in \mathbb{N}$ (the number of individuals whose data is in the database). We treat $n$ as public information throughout.

We say databases $D_A, D_B$ are adjacent if they differ only in one row, meaning that we can obtain one from the other by deleting one row and adding another. I.e. databases are adjacent if they are of the same size and their edit distance is 1. To handle worst case pairs of databases, our probabilities will be over the random choices made by the privacy mechanism.

**Definition 3 ($(\varepsilon,0)$-Differential Privacy):** A randomized algorithm $\mathcal{M}$ is $\varepsilon$-differentially private if for all pairs of adjacent databases $D_A, D_B$, and for all sets $S \subseteq \text{Range}(\mathcal{M}(D_A)) \cup \text{Range}(\mathcal{M}(D_B))$
$$\Pr[\mathcal{M}(D_A) \in S] \leq e^{\varepsilon} \cdot \Pr[\mathcal{M}(D_B) \in S],$$
where the probabilities are over algorithm $\mathcal{M}$'s coins. Or alternatively: $$D_{max}(\mathcal{M}(D_A)||\mathcal{M}(D_B)), D_{max}(\mathcal{M}(D_B)||\mathcal{M}(D_A)) \leq \varepsilon$$

**Definition 4 ($(\varepsilon, \delta)$-Differential Privacy):** A randomized algorithm $\mathcal{M}$ gives $(\varepsilon,\delta)$-differential privacy if for all pairs of adjacent databases $D_A$ and $D_B$ and all $S \subseteq \text{Range}(\mathcal{M})$
$$ \Pr[\mathcal{M}(D_A) \in S]  \le   e^\varepsilon \cdot \Pr[\mathcal{M}(D_B) \in S] + \delta, $$
where the probabilities are over the coin flips of the algorithm $\mathcal{M}$. Or alternatively: $$D_{max}^{\delta}(\mathcal{M}(D_A)||\mathcal{M}(D_B)), D_{max}^{\delta}(\mathcal{M}(D_B)||\mathcal{M}(D_A)) \leq \varepsilon$$

**Privacy Loss as a Random Variable.** Consider running an algorithm $\mathcal{M}$ on a pair of databases $x,y$. For an outcome $o$, the privacy loss on $o$ is the log-ratio of its probability when $\mathcal{M}$ is run on each database:
$$\mathcal{L}_{(\mathcal{M}(D_A)||\mathcal{M}(D_B))}^{(o)} = \ln \frac{\Pr[\mathcal{M}(D_A)=o]}{\Pr[\mathcal{M}(D_B)=o]} .$$

CDP delves more deeply into the privacy loss random variable: this real-valued random variable measures the privacy loss ensuing when algorithm $\mathcal{M}$ is run on $D_A$ (as opposed to $D_B$). It is sampled by taking $y \sim \mathcal{M}(D_A)$ and outputting $\mathcal{L}_{(\mathcal{M}(D_A)||\mathcal{M}(D_B))}^{(o)}$. This random variable can take positive or negative values. For $(\varepsilon,0)$-differentially private algorithms, its magnitude is always bounded by $\varepsilon$. For $(\varepsilon,\delta)$-differentially private algorithms, with all but $\delta$ probability the magnitude is bounded by $\varepsilon$.

### Subgaussian Random Variables

Subgaussian random variables were introduced by Kahane. A subgaussian random variable is one for which there is a positive real number $\sigma > 0$ s.t. the moment generating function is always smaller than the moment generating function of a Gaussian with standard deviation $\sigma$ and expectation 0. In this section we briefly review the definition and basic lemmata from the literature.

**Definition 5 (Subgaussian Random Variable):** A random variable $X$ is $\sigma$-subgaussian for a constant $\sigma > 0$ if:
$$\forall \lambda \in \mathbb{R}: \mathbb{E}[e^{\lambda \cdot X}] \leq e^{\frac{\lambda^2 \cdot \sigma^2}{2}}$$

We say that $X$ is subgaussian if there exists $\sigma \geq 0$ s.t. $X$ is $\sigma$-subgaussian. For a subgaussian random variable $X$, the subgaussian standard of $X$ is:
$$\tau(X) = \inf \{\sigma \geq 0: \text{$X$ is $\sigma$-subgaussian} \}$$

**Remarks.** An immediate consequence of Definition 5 is that an $\sigma$-subgaussian random variable has expectation 0, and variance bounded by $\sigma^2$ (see Fact 1). Note also that the gaussian distribution with expectation 0 and standard deviation $\sigma$ is $\sigma$-subgaussian. There are also known bounds on the higher moments of subgaussian random variables (see Fact 2).

**Lemma 1 (Subgaussian Concentration):** If $X$ is $\sigma$-subgaussian for $\sigma > 0$, then:
$$\Pr[X \geq t \cdot \sigma] \leq  e^{-t^2/2}, \qquad \Pr[X \leq -t \cdot \sigma]  \leq  e^{-t^2/2}$$

**Proof:** For every $\lambda > 0$ and $t > 0$:
$$\Pr[X \geq t \cdot \sigma] = \Pr[e^{\lambda \cdot X} \geq e^{\lambda \cdot t \cdot \sigma}] \leq e^{-\lambda \cdot t \cdot \sigma} \cdot \mathbb{E}[e^{\lambda \cdot X}] \leq e^{\frac{\lambda^2 \cdot \sigma^2}{2} - \lambda \cdot t \cdot \sigma}$$
where the first equality is obtained by taking an exponential of all arguments, the second (in)equality is by Markov, and this is by the properties of the subgaussian random variable $X$. The right-hand side is minimized when $\lambda = t/\sigma$, and thus we get that:
$$\Pr[X \geq t \cdot \sigma] \leq e^{-t^2/2}$$
The proof that $\Pr[X \leq -t \cdot \sigma] \leq e^{-t^2/2}$ is similar. □

**Fact 1 (Subgaussian Variance):** The variance of any $\tau$-subgaussian random variable $Y$ is bounded by $\text{Var}(Y) \leq \tau^2$.

**Fact 2 (Subgaussian Moments):** For any $\tau$-subgaussian random variable $Y$, and integer $k$, the $k$-th moment is bounded by:
$$\mathbb{E}[Y^{k}] \leq \left( (\lceil k/2 \rceil !) \cdot 2^{\lceil k/2 \rceil + 1} \cdot \tau^{k} \right)$$

**Lemma 2 (Sum of Subgaussians):** Let $X_1,\ldots,X_k$ be (jointly distributed) real-valued random variables such that for every $i \in [k]$, and for every $(x_1,\ldots,x_{i-1}) \in \text{Supp}(X_1,\ldots,X_{k-1})$, it holds that the random variable $(X_i|X_1=x_1,\ldots,X_{i-1}=x_{i-1})$ is $\sigma_i$-subgaussian. Then the random variable $\sum_{i \in [k]} X_i$ is $\sigma$-subgaussian, where $\sigma = \sqrt{\sum_{i \in [k]} \sigma_i^2}$.

**Proof:** The proof is by induction over $k$. The base case $k=1$ is immediate. For $k > 1$, for any $\lambda \in \mathbb{R}$, we have:
$$\mathbb{E}[e^{\lambda \cdot  \sum_{i \in [k]} X_i} ] = \mathbb{E}_{(x_1,\ldots,x_{k-1})} \left[ \mathbb{E}_{X_k} [e^{\lambda \cdot  \sum_{i \in [k]} X_i} | X_1=x_1,\ldots,X_{k-1}=x_{k-1}] \right]$$
$$= \mathbb{E}_{(x_1,\ldots,x_{k-1})} \left[ e^{\lambda \cdot \sum_{i \in [k-1]} x_i } \cdot \mathbb{E}_{X_k} [e^{\lambda \cdot  X_k} | X_1=x_1,\ldots,X_{k-1}=x_{k-1}] \right]$$
$$\leq \mathbb{E}_{(x_1,\ldots,x_{k-1})} \left[ e^{\lambda \cdot \sum_{i \in [k-1]} x_i } \cdot e^{\frac{\lambda^2 \cdot \sigma_k^2}{2}} \right] = e^{\frac{\lambda^2 \cdot \sigma_k^2}{2}} \cdot \mathbb{E}[e^{\lambda \cdot  \sum_{i \in [k-1]} X_i} ]$$
$$\leq  e^{\frac{\lambda^2 \cdot \sigma_k^2}{2}} \cdot  e^{\frac{\lambda^2 \cdot \sum_{i \in [k-1]} \sigma_i^2}{2}} = e^{\frac{\lambda^2 \cdot \sum_{i \in [k]} \sigma_i^2}{2}}$$
where the last inequality is by the induction hypothesis. □

The following technical Lemma about the products of (jointly distributed) random variables, one of which is exponential in a subgaussian, will be used extensively in proving group privacy:

**Lemma 3 (Expected Product with Exponential in Subgaussian):** Let $X$ and $Y$ be jointly distributed random variables, where $Y$ is $\sigma$-Subgaussian for $\tau \leq 1/3$. Then:
$$\mathbb{E}[X \cdot e^Y] \leq \mathbb{E}[X] + \sqrt{\mathbb{E}[X^2]} \cdot (\tau + 3\tau^2) \leq \mathbb{E}[X] + (\sqrt{\text{Var}(X)} + \mathbb{E}[X]) \cdot (\tau + 3\tau^2)$$

**Proof:** Taking the Taylor expansion of $e^Y$ we have:
$$\mathbb{E}[X \cdot e^Y] = \mathbb{E}\left[X \cdot \left( 1 + Y + \sum_{k=2}^{\infty} \frac{Y^k}{k!} \right) \right] = \mathbb{E}[X] + \mathbb{E}[X \cdot Y] + \mathbb{E}\left[X \cdot \left(\sum_{k=2}^{\infty} \frac{Y^k}{k!} \right) \right]$$

By the Cauchy-Schwartz inequality:
$$\mathbb{E}[X \cdot Y] \leq \sqrt{\mathbb{E}[X^2]} \cdot \sqrt{\mathbb{E}[Y^2]} \leq  \sqrt{\mathbb{E}[X^2]} \cdot \tau$$
where the last inequality uses the fact that for a $\sigma$-subgaussian RV $Y$, $\text{Var}(Y) \leq \tau^2$ (Fact 1), and that $\sqrt{a + b} \leq \sqrt{a} + \sqrt{b}$ (for any $a,b \geq 0$). To bound the last summand, we use linearity of the expectation and Cauchy-Schwartz:
$$\mathbb{E}\left[X \cdot \left(\sum_{k=2}^{\infty} \frac{Y^k}{k!} \right) \right] = \sum_{k=2}^{\infty} \left( \mathbb{E}\left[X \cdot \frac{Y^k}{k!} \right] \right) \leq \sum_{k=2}^{\infty} \sqrt{\mathbb{E}[X^2]} \cdot \sqrt{\mathbb{E}\left[ \frac{Y^{2k}}{(k!)^2} \right]}$$
$$= \sqrt{\mathbb{E}[X^2]} \cdot \sum_{k=2}^{\infty} \sqrt{\mathbb{E}\left[ \frac{Y^{2k}}{(k!)^2} \right]}$$

Using the fact that for any $\tau$-subgaussian distribution $Y$, the $2k$-th moment $\mathbb{E}[Y^{2k}]$ is bounded by $(k!) \cdot 2^{k+1} \cdot \tau^{2k}$ (see Fact 2), we conclude from the above that for $\tau < 1$:
$$\mathbb{E}\left[X \cdot \left(\sum_{k=2}^{\infty} \frac{Y^k}{k!} \right) \right] \leq \sqrt{\mathbb{E}[X^2]} \cdot \sum_{k=2}^{\infty} \sqrt{\frac{(k!) \cdot 2^{k+1} \cdot \tau^{2k}}{(k!)^2}}$$
$$= \sqrt{\mathbb{E}[X^2]} \cdot  \sum_{k=2}^{\infty} \sqrt{ \frac{2^{k+1} \cdot \tau^{2k}}{(k!)} } \leq \sqrt{\mathbb{E}[X^2]} \cdot \sum_{k=2}^{\infty} \sqrt{4\tau^{2k}}$$
$$= \sqrt{\mathbb{E}[X^2]} \cdot 2\tau^2 \cdot \sum_{k=0}^{\infty} \tau^k = \sqrt{\mathbb{E}[X^2]} \cdot \frac{2\tau^2}{1- \tau}$$

Putting together the inequalities, we conclude that for $\tau \leq 1/2$:
$$\mathbb{E}[X \cdot e^Y] \leq  \mathbb{E}[X] + \sqrt{\mathbb{E}[X^2]} \cdot \tau + \sqrt{\mathbb{E}[X^2]} \cdot \frac{2\tau^2}{1- \tau}$$
$$= \mathbb{E}[X] + \sqrt{\mathbb{E}[X^2]} \cdot \left( \tau + \frac{2\tau^2}{1-\tau} \right) \leq  \mathbb{E}[X] + \sqrt{\mathbb{E}[X^2]} \cdot (\tau + 3\tau^2)$$
$$\leq  \mathbb{E}[X] + (\sqrt{\text{Var}(X)} + \mathbb{E}[X]) \cdot (\tau + 3\tau^2)$$
where the next-to-last inequality holds whenever $\tau \leq 1/3$, and the last inequality is because $\sqrt{\mathbb{E}[X^2]} \leq \sqrt{\text{Var}(X)} + \mathbb{E}[X]$ (because $\sqrt{a+b} \leq \sqrt{a} + \sqrt{b}$ for any $a,b>0$). □

---

### النسخة العربية

**التباعد.** سنحتاج إلى عدة مفاهيم مختلفة للتباعد بين التوزيعات. سنقدم أيضاً مفهوماً جديداً، التباعد التحت-غاوسي (subgaussian divergence) في القسم 3.

**التعريف 1 (تباعد KL):** تباعد KL، أو الإنتروبيا النسبية، بين متغيرين عشوائيين $Y$ و $Z$ يُعرَّف بأنه:
$$D_{KL}(Y||Z) = \mathbb{E}_{y \sim Y} \left[ \ln \frac{\Pr[Y=y]}{\Pr[Z=y]} \right],$$
حيث إذا لم يكن مجال $Y$ مساوياً لمجال $Z$، فإن $D_{KL}(Y||Z)$ غير معرَّف.

**التعريف 2 (التباعد الأقصى):** التباعد الأقصى بين متغيرين عشوائيين $Y$ و $Z$ يُعرَّف بأنه:
$$D_{max}(Y||Z) = \max_{S \subseteq \text{Supp}(Y)} \left[ \ln \frac{\Pr[Y \in S]}{\Pr[Z \in S]} \right],$$
حيث إذا لم يكن مجال $Y$ مساوياً لمجال $Z$، فإن $D_{max}(Y||Z)$ غير معرَّف.

التباعد التقريبي بمقدار $\delta$ بين $Y$ و $Z$ يُعرَّف بأنه:
$$D_{max}^{\delta}(Y||Z) = \max_{S \subseteq \text{Supp}(Y): \Pr[Y \in S] \geq \delta} \left[ \ln \frac{\Pr[Y \in S]}{\Pr[Z \in S]} \right],$$
حيث إذا كان $\Pr[Y \in \text{Supp}(Y) \setminus \text{Supp}(Z)] > \delta$، فإن $D_{max}^{\delta}(Y||Z)$ غير معرَّف.

### الخصوصية التفاضلية

بالنسبة لقاعدة بيانات معينة $D$، آلية الوصول إلى قاعدة البيانات (العشوائية) غير التفاعلية $\mathcal{M}$ تحسب مخرجاً $\mathcal{M}(x)$ يمكن استخدامه لاحقاً لإعادة بناء معلومات حول $D$. سنهتم بالآليات $\mathcal{M}$ التي تكون خاصة وفقاً لمفاهيم الخصوصية المختلفة الموصوفة أدناه.

نفكر في قاعدة البيانات $D_A$ كمجموعة متعددة من الصفوف، كل منها من فضاء بيانات $U$. بديهياً، كل صف يحتوي على بيانات فرد واحد. غالباً ما سننظر إلى قاعدة بيانات بحجم $n$ كمجموعة مرتبة $D_A \in U^n$ لبعض $n \in \mathbb{N}$ (عدد الأفراد الذين بياناتهم في قاعدة البيانات). نعامل $n$ كمعلومة عامة في كل مكان.

نقول أن قواعد البيانات $D_A, D_B$ متجاورة إذا اختلفت في صف واحد فقط، بمعنى أنه يمكننا الحصول على إحداهما من الأخرى بحذف صف واحد وإضافة آخر. أي أن قواعد البيانات متجاورة إذا كانت من نفس الحجم ومسافة التحرير بينهما تساوي 1. للتعامل مع أسوأ الحالات لأزواج قواعد البيانات، ستكون احتمالاتنا على الخيارات العشوائية التي تتخذها آلية الخصوصية.

**التعريف 3 (الخصوصية التفاضلية $(\varepsilon,0)$):** الخوارزمية العشوائية $\mathcal{M}$ محافظة على الخصوصية التفاضلية $\varepsilon$ إذا كان لجميع أزواج قواعد البيانات المتجاورة $D_A, D_B$، ولجميع المجموعات $S \subseteq \text{Range}(\mathcal{M}(D_A)) \cup \text{Range}(\mathcal{M}(D_B))$
$$\Pr[\mathcal{M}(D_A) \in S] \leq e^{\varepsilon} \cdot \Pr[\mathcal{M}(D_B) \in S],$$
حيث الاحتمالات على عملات الخوارزمية $\mathcal{M}$. أو بدلاً من ذلك: $$D_{max}(\mathcal{M}(D_A)||\mathcal{M}(D_B)), D_{max}(\mathcal{M}(D_B)||\mathcal{M}(D_A)) \leq \varepsilon$$

**التعريف 4 (الخصوصية التفاضلية $(\varepsilon, \delta)$):** الخوارزمية العشوائية $\mathcal{M}$ تعطي خصوصية تفاضلية $(\varepsilon,\delta)$ إذا كان لجميع أزواج قواعد البيانات المتجاورة $D_A$ و $D_B$ ولجميع $S \subseteq \text{Range}(\mathcal{M})$
$$ \Pr[\mathcal{M}(D_A) \in S]  \le   e^\varepsilon \cdot \Pr[\mathcal{M}(D_B) \in S] + \delta, $$
حيث الاحتمالات على رميات العملة للخوارزمية $\mathcal{M}$. أو بدلاً من ذلك: $$D_{max}^{\delta}(\mathcal{M}(D_A)||\mathcal{M}(D_B)), D_{max}^{\delta}(\mathcal{M}(D_B)||\mathcal{M}(D_A)) \leq \varepsilon$$

**خسارة الخصوصية كمتغير عشوائي.** لنأخذ في الاعتبار تشغيل خوارزمية $\mathcal{M}$ على زوج من قواعد البيانات $x,y$. بالنسبة لنتيجة $o$، فإن خسارة الخصوصية على $o$ هي نسبة اللوغاريتم لاحتماليتها عند تشغيل $\mathcal{M}$ على كل قاعدة بيانات:
$$\mathcal{L}_{(\mathcal{M}(D_A)||\mathcal{M}(D_B))}^{(o)} = \ln \frac{\Pr[\mathcal{M}(D_A)=o]}{\Pr[\mathcal{M}(D_B)=o]} .$$

الخصوصية التفاضلية المركزة تتعمق أكثر في متغير خسارة الخصوصية العشوائي: هذا المتغير العشوائي ذو القيمة الحقيقية يقيس خسارة الخصوصية الناتجة عند تشغيل الخوارزمية $\mathcal{M}$ على $D_A$ (مقابل $D_B$). يتم أخذ عينة منه عن طريق أخذ $y \sim \mathcal{M}(D_A)$ وإخراج $\mathcal{L}_{(\mathcal{M}(D_A)||\mathcal{M}(D_B))}^{(o)}$. هذا المتغير العشوائي يمكن أن يأخذ قيماً موجبة أو سالبة. بالنسبة للخوارزميات المحافظة على الخصوصية التفاضلية $(\varepsilon,0)$، فإن مقداره محدود دائماً بـ $\varepsilon$. بالنسبة للخوارزميات المحافظة على الخصوصية التفاضلية $(\varepsilon,\delta)$، باستثناء احتمال $\delta$ فإن المقدار محدود بـ $\varepsilon$.

### المتغيرات العشوائية التحت-غاوسية

المتغيرات العشوائية التحت-غاوسية قدمها Kahane. المتغير العشوائي التحت-غاوسي هو ذاك الذي يوجد له عدد حقيقي موجب $\sigma > 0$ بحيث أن دالة التوليد العزمية دائماً أصغر من دالة التوليد العزمية لتوزيع غاوسي بانحراف معياري $\sigma$ وقيمة متوقعة 0. في هذا القسم نراجع بإيجاز التعريف والمبرهنات الأساسية من الأدبيات.

**التعريف 5 (المتغير العشوائي التحت-غاوسي):** المتغير العشوائي $X$ هو تحت-غاوسي بمعيار $\sigma$ لثابت $\sigma > 0$ إذا كان:
$$\forall \lambda \in \mathbb{R}: \mathbb{E}[e^{\lambda \cdot X}] \leq e^{\frac{\lambda^2 \cdot \sigma^2}{2}}$$

نقول أن $X$ تحت-غاوسي إذا وُجد $\sigma \geq 0$ بحيث أن $X$ تحت-غاوسي بمعيار $\sigma$. بالنسبة لمتغير عشوائي تحت-غاوسي $X$، فإن المعيار التحت-غاوسي لـ $X$ هو:
$$\tau(X) = \inf \{\sigma \geq 0: \text{$X$ تحت-غاوسي بمعيار $\sigma$} \}$$

**ملاحظات.** نتيجة مباشرة للتعريف 5 هي أن المتغير العشوائي التحت-غاوسي بمعيار $\sigma$ له قيمة متوقعة 0، وتباين محدود بـ $\sigma^2$ (انظر الحقيقة 1). لاحظ أيضاً أن التوزيع الغاوسي بقيمة متوقعة 0 وانحراف معياري $\sigma$ هو تحت-غاوسي بمعيار $\sigma$. توجد أيضاً حدود معروفة على العزوم الأعلى للمتغيرات العشوائية التحت-غاوسية (انظر الحقيقة 2).

**المبرهنة 1 (التركيز التحت-غاوسي):** إذا كان $X$ تحت-غاوسياً بمعيار $\sigma$ لـ $\sigma > 0$، فإن:
$$\Pr[X \geq t \cdot \sigma] \leq  e^{-t^2/2}, \qquad \Pr[X \leq -t \cdot \sigma]  \leq  e^{-t^2/2}$$

**البرهان:** لكل $\lambda > 0$ و $t > 0$:
$$\Pr[X \geq t \cdot \sigma] = \Pr[e^{\lambda \cdot X} \geq e^{\lambda \cdot t \cdot \sigma}] \leq e^{-\lambda \cdot t \cdot \sigma} \cdot \mathbb{E}[e^{\lambda \cdot X}] \leq e^{\frac{\lambda^2 \cdot \sigma^2}{2} - \lambda \cdot t \cdot \sigma}$$
حيث يتم الحصول على المساواة الأولى بأخذ الأس لجميع المتغيرات، والمساواة (عدم المساواة) الثانية بمتباينة ماركوف، وهذا بخصائص المتغير العشوائي التحت-غاوسي $X$. الطرف الأيمن يصل إلى الحد الأدنى عندما $\lambda = t/\sigma$، وبالتالي نحصل على:
$$\Pr[X \geq t \cdot \sigma] \leq e^{-t^2/2}$$
البرهان على أن $\Pr[X \leq -t \cdot \sigma] \leq e^{-t^2/2}$ مشابه. □

**الحقيقة 1 (التباين التحت-غاوسي):** تباين أي متغير عشوائي تحت-غاوسي بمعيار $\tau$ محدود بـ $\text{Var}(Y) \leq \tau^2$.

**الحقيقة 2 (العزوم التحت-غاوسية):** بالنسبة لأي متغير عشوائي تحت-غاوسي بمعيار $\tau$، وعدد صحيح $k$، فإن العزم الـ $k$ محدود بـ:
$$\mathbb{E}[Y^{k}] \leq \left( (\lceil k/2 \rceil !) \cdot 2^{\lceil k/2 \rceil + 1} \cdot \tau^{k} \right)$$

**المبرهنة 2 (مجموع المتغيرات التحت-غاوسية):** لتكن $X_1,\ldots,X_k$ متغيرات عشوائية ذات قيم حقيقية (موزعة بشكل مشترك) بحيث أنه لكل $i \in [k]$، ولكل $(x_1,\ldots,x_{i-1}) \in \text{Supp}(X_1,\ldots,X_{k-1})$، يكون المتغير العشوائي $(X_i|X_1=x_1,\ldots,X_{i-1}=x_{i-1})$ تحت-غاوسياً بمعيار $\sigma_i$. عندئذٍ المتغير العشوائي $\sum_{i \in [k]} X_i$ هو تحت-غاوسي بمعيار $\sigma$، حيث $\sigma = \sqrt{\sum_{i \in [k]} \sigma_i^2}$.

**البرهان:** البرهان بالاستقراء على $k$. الحالة الأساسية $k=1$ واضحة مباشرة. بالنسبة لـ $k > 1$، لأي $\lambda \in \mathbb{R}$، لدينا:
$$\mathbb{E}[e^{\lambda \cdot  \sum_{i \in [k]} X_i} ] = \mathbb{E}_{(x_1,\ldots,x_{k-1})} \left[ \mathbb{E}_{X_k} [e^{\lambda \cdot  \sum_{i \in [k]} X_i} | X_1=x_1,\ldots,X_{k-1}=x_{k-1}] \right]$$
$$= \mathbb{E}_{(x_1,\ldots,x_{k-1})} \left[ e^{\lambda \cdot \sum_{i \in [k-1]} x_i } \cdot \mathbb{E}_{X_k} [e^{\lambda \cdot  X_k} | X_1=x_1,\ldots,X_{k-1}=x_{k-1}] \right]$$
$$\leq \mathbb{E}_{(x_1,\ldots,x_{k-1})} \left[ e^{\lambda \cdot \sum_{i \in [k-1]} x_i } \cdot e^{\frac{\lambda^2 \cdot \sigma_k^2}{2}} \right] = e^{\frac{\lambda^2 \cdot \sigma_k^2}{2}} \cdot \mathbb{E}[e^{\lambda \cdot  \sum_{i \in [k-1]} X_i} ]$$
$$\leq  e^{\frac{\lambda^2 \cdot \sigma_k^2}{2}} \cdot  e^{\frac{\lambda^2 \cdot \sum_{i \in [k-1]} \sigma_i^2}{2}} = e^{\frac{\lambda^2 \cdot \sum_{i \in [k]} \sigma_i^2}{2}}$$
حيث عدم المساواة الأخيرة بفرضية الاستقراء. □

المبرهنة التقنية التالية حول حاصل ضرب المتغيرات العشوائية (الموزعة بشكل مشترك)، أحدها أسي في متغير تحت-غاوسي، ستُستخدم على نطاق واسع في إثبات خصوصية المجموعة:

**المبرهنة 3 (القيمة المتوقعة لحاصل الضرب مع الأسي في التحت-غاوسي):** لتكن $X$ و $Y$ متغيرين عشوائيين موزعين بشكل مشترك، حيث $Y$ تحت-غاوسي بمعيار $\sigma$ لـ $\tau \leq 1/3$. عندئذٍ:
$$\mathbb{E}[X \cdot e^Y] \leq \mathbb{E}[X] + \sqrt{\mathbb{E}[X^2]} \cdot (\tau + 3\tau^2) \leq \mathbb{E}[X] + (\sqrt{\text{Var}(X)} + \mathbb{E}[X]) \cdot (\tau + 3\tau^2)$$

**البرهان:** بأخذ تطوير تايلور لـ $e^Y$ لدينا:
$$\mathbb{E}[X \cdot e^Y] = \mathbb{E}\left[X \cdot \left( 1 + Y + \sum_{k=2}^{\infty} \frac{Y^k}{k!} \right) \right] = \mathbb{E}[X] + \mathbb{E}[X \cdot Y] + \mathbb{E}\left[X \cdot \left(\sum_{k=2}^{\infty} \frac{Y^k}{k!} \right) \right]$$

بمتباينة كوشي-شوارتز:
$$\mathbb{E}[X \cdot Y] \leq \sqrt{\mathbb{E}[X^2]} \cdot \sqrt{\mathbb{E}[Y^2]} \leq  \sqrt{\mathbb{E}[X^2]} \cdot \tau$$
حيث عدم المساواة الأخيرة تستخدم حقيقة أنه بالنسبة لمتغير عشوائي تحت-غاوسي بمعيار $\sigma$ $Y$، فإن $\text{Var}(Y) \leq \tau^2$ (الحقيقة 1)، وأن $\sqrt{a + b} \leq \sqrt{a} + \sqrt{b}$ (لأي $a,b \geq 0$). لتحديد الحد للمجموع الأخير، نستخدم خطية القيمة المتوقعة وكوشي-شوارتز:
$$\mathbb{E}\left[X \cdot \left(\sum_{k=2}^{\infty} \frac{Y^k}{k!} \right) \right] = \sum_{k=2}^{\infty} \left( \mathbb{E}\left[X \cdot \frac{Y^k}{k!} \right] \right) \leq \sum_{k=2}^{\infty} \sqrt{\mathbb{E}[X^2]} \cdot \sqrt{\mathbb{E}\left[ \frac{Y^{2k}}{(k!)^2} \right]}$$
$$= \sqrt{\mathbb{E}[X^2]} \cdot \sum_{k=2}^{\infty} \sqrt{\mathbb{E}\left[ \frac{Y^{2k}}{(k!)^2} \right]}$$

باستخدام حقيقة أنه بالنسبة لأي توزيع تحت-غاوسي بمعيار $\tau$ $Y$، فإن العزم الـ $2k$ $\mathbb{E}[Y^{2k}]$ محدود بـ $(k!) \cdot 2^{k+1} \cdot \tau^{2k}$ (انظر الحقيقة 2)، نستنتج من أعلاه أنه لـ $\tau < 1$:
$$\mathbb{E}\left[X \cdot \left(\sum_{k=2}^{\infty} \frac{Y^k}{k!} \right) \right] \leq \sqrt{\mathbb{E}[X^2]} \cdot \sum_{k=2}^{\infty} \sqrt{\frac{(k!) \cdot 2^{k+1} \cdot \tau^{2k}}{(k!)^2}}$$
$$= \sqrt{\mathbb{E}[X^2]} \cdot  \sum_{k=2}^{\infty} \sqrt{ \frac{2^{k+1} \cdot \tau^{2k}}{(k!)} } \leq \sqrt{\mathbb{E}[X^2]} \cdot \sum_{k=2}^{\infty} \sqrt{4\tau^{2k}}$$
$$= \sqrt{\mathbb{E}[X^2]} \cdot 2\tau^2 \cdot \sum_{k=0}^{\infty} \tau^k = \sqrt{\mathbb{E}[X^2]} \cdot \frac{2\tau^2}{1- \tau}$$

بجمع المتباينات، نستنتج أنه لـ $\tau \leq 1/2$:
$$\mathbb{E}[X \cdot e^Y] \leq  \mathbb{E}[X] + \sqrt{\mathbb{E}[X^2]} \cdot \tau + \sqrt{\mathbb{E}[X^2]} \cdot \frac{2\tau^2}{1- \tau}$$
$$= \mathbb{E}[X] + \sqrt{\mathbb{E}[X^2]} \cdot \left( \tau + \frac{2\tau^2}{1-\tau} \right) \leq  \mathbb{E}[X] + \sqrt{\mathbb{E}[X^2]} \cdot (\tau + 3\tau^2)$$
$$\leq  \mathbb{E}[X] + (\sqrt{\text{Var}(X)} + \mathbb{E}[X]) \cdot (\tau + 3\tau^2)$$
حيث عدم المساواة قبل الأخيرة تصمد عندما يكون $\tau \leq 1/3$، وعدم المساواة الأخيرة لأن $\sqrt{\mathbb{E}[X^2]} \leq \sqrt{\text{Var}(X)} + \mathbb{E}[X]$ (لأن $\sqrt{a+b} \leq \sqrt{a} + \sqrt{b}$ لأي $a,b>0$). □

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:** KL-divergence, max divergence, approximate divergence, adjacent databases, privacy loss random variable, subgaussian random variable, subgaussian standard, moment generating function
- **Equations:** Extensive mathematical notation with definitions, lemmas, proofs
- **Citations:** Kahane60, DworkMNS06, DworkKMMN06, BuldyginK00, Rivasplata12
- **Special handling:**
  - Three formal definitions for divergence measures
  - Two definitions for differential privacy variants
  - One main definition for subgaussian random variables
  - Three lemmas with complete proofs (Subgaussian Concentration, Sum of Subgaussians, Expected Product)
  - Two facts about subgaussian properties
  - Proof notation and mathematical symbols preserved throughout
  - Conditional probability notation maintained

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.89
- **Overall section score:** 0.87

### Back-Translation Check (Definition 5)

A random variable $X$ is $\sigma$-subgaussian for a constant $\sigma > 0$ if: for all $\lambda \in \mathbb{R}$: $\mathbb{E}[e^{\lambda \cdot X}] \leq e^{\frac{\lambda^2 \cdot \sigma^2}{2}}$. We say that $X$ is subgaussian if there exists $\sigma \geq 0$ such that $X$ is $\sigma$-subgaussian. For a subgaussian random variable $X$, the subgaussian standard of $X$ is: $\tau(X) = \inf \{\sigma \geq 0: \text{$X$ is $\sigma$-subgaussian}\}$

**Back-translation assessment:** Excellent semantic match with original definition.
