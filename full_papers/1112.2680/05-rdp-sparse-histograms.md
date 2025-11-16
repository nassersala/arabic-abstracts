# Section 5: RDP Sparse Histograms
## القسم 5: الرسوم البيانية الهيستوغرامية المتناثرة لـ RDP

**Section:** rdp-sparse-histograms
**Translation Quality:** 0.87
**Glossary Terms Used:** random differential privacy, histogram, sparse, accuracy, Laplace distribution, risk, algorithm

---

### English Version

We first give a technique for the release of a histogram which works well in the case of a sparse histogram, and which satisfies the $(\alpha, \gamma)$-Random Differential Privacy. We then compare the accuracy of this method to a lower bound on the accuracy of a $\alpha$-Differentially Private approach.

The basic idea is to not add any noise to cells with low counts. This results in partitioning the space into two blocks and releasing a noise-free histogram in one block, and use a differentially private histogram in the other. The partition will depend on the data itself. For a sample $x_1, \ldots, x_n$, we denote: $S = S(x_1, \ldots, x_n) = \{j : \theta_j = 0\}$. Then we consider the release mechanism:

$$z_j = \begin{cases} \theta_j & j \in S \text{ and } 2k \leq \gamma n \\ \theta_j + \frac{2}{n\alpha}L & \text{o/w} \end{cases}$$

**Proposition 5.1.** The random vector $Z = (z_1, \ldots, z_k)$ as defined in (5) satisfies the $(\alpha, \gamma)$-RDP.

In demonstrating RDP, we take the sample $x_1, \ldots, x_n, x_{n+1}$ and denote: $S = S(x_1, \ldots, x_n)$ and $S' = S(x_1, \ldots, x_{n-1}, x_{n+1})$. We consider the output distribution of our method when applied to each of the neighboring samples. The event that the ratio of densities fail to meet the requisite bound is a subset of the event where either $x_{n+1} \in S$ or $x_n \in S'$, and when $2k \leq \gamma n$. In the complement of this event then the partitions are the same, and the differing samples both fall within the block which receives the Laplace noise, so the DP condition is achieved. In demonstrating the RDP, we simply bound the probability of the aforementioned event, conditional on the order statistics.

*Proof of proposition 5.1.* In the interest of space let the vector of order statistics be denoted $T = (x_{(1)}, \ldots, x_{(n+1)})$. Let $S^*(x_1, \ldots, x_n, x_{n+1}) = \{j : \sum_{i=1}^{n+1} \mathbf{1}\{x_i = j\} \leq 1\}$. We have that $S, S' \subseteq S^*$. We thus have

$$\mathbb{P}(x_n \in S' \text{ or } x_{n+1} \in S|T) \leq \mathbb{P}(x_n \in S^* \text{ or } x_{n+1} \in S^*|T).$$

The latter probability is just the fraction of ways in which the order statistics may be rearranged so that $x_n, x_{n+1}$ fall within $S^*$. Due to the condition $2k \leq \gamma n$, we have $|S^*| \leq k \leq \frac{\gamma n}{2}$. Therefore the number of rearrangements having at least one of $x_n$ or $x_{n+1}$ in $S^*$ is bounded above

$$\mathbb{P}(x_n \in S^* \text{ or } x_{n+1} \in S^*|T) \leq \frac{2|S^*|}{n+1} < \gamma.$$

Therefore

$$\mathbb{P}(x_n \in S' \text{ or } x_{n+1} \in S) \leq \int_{\mathcal{X}^{n+1}} \mathbb{P}(x_n \in S' \text{ or } x_{n+1} \in S|T)dP(T) \leq \int_{\mathcal{X}^{n+1}} \mathbb{P}(x_n \in S^* \text{ or } x_{n+1} \in S^*|T)dP(T)$$
$$< \gamma \int_{\mathcal{X}^{n+1}} dP(T) = \gamma.$$

Finally:

$$\mathbb{P}\left( \forall Z \subseteq \mathcal{Z}, e^{-\alpha} \leq \frac{Q_n(Z|X)}{Q_n(Z|X')} \leq e^{\alpha} \right) = 1 - \mathbb{P}(x_n \in S' \text{ or } x_{n+1} \in S) > 1 - \gamma.$$

□

## 5.1 Accuracy

Here we show that $\delta(z)$ from (2) is close to $\theta$ even when the histogram is sparse.

**Theorem 5.2.** Suppose that $2k \leq \gamma n$. Let $\theta^n(x_1, \ldots, x_n) = (\theta_1, \ldots, \theta_r, 0, \ldots, 0)$ for some $1 \leq r < k$. Then $||\theta - \delta(z)||_1 = O_P(r/\alpha n)$.

*Proof.* Let $L_1, \ldots, L_r \sim \text{Laplace}$. Let $E$ be the event that $L_j > -\frac{n\alpha}{2}\theta_j$ for all $1 \leq j \leq r$. Then $E$ holds, except on a set of exponentially small probability. Suppose $E$ holds. Let $W = \sum_{j=1}^r L_j = O_P(r)$. For $1 \leq j \leq r$,

$$z_j = \theta_j + \frac{2L_j}{n\alpha}$$

For $j > r$, $z_j = \theta_j = 0$. Hence $||z - \theta||_1 = O_P(r/\alpha n)$. Furthermore $||\delta(z) - z||_1 \leq \frac{r}{n} \leq \frac{r}{\alpha n}$. Hence via the triangle inequality we have, $||\delta(z) - \theta||_1 = O_P(r/\alpha n)$. □

We thus have a technique for which the risk is uniformly bounded above by $O(k/\alpha n)$ as with the DP technique, and which also enjoys the coordinate-wise upper bound on the risk. However in this regime, the risk is no longer uniformly lower bounded with a rate linear in $k$, since the upper bound is linear in $r$ in the case of sparse vectors.

---

### النسخة العربية

نقدم أولاً تقنية لإصدار رسم بياني هيستوغرامي تعمل بشكل جيد في حالة الرسم البياني الهيستوغرامي المتناثر، والتي تحقق الخصوصية التفاضلية العشوائية $(\alpha, \gamma)$. ثم نقارن دقة هذه الطريقة بالحد الأدنى لدقة نهج خاص تفاضلياً $\alpha$.

الفكرة الأساسية هي عدم إضافة أي ضوضاء إلى الخلايا ذات العدادات المنخفضة. ينتج عن هذا تقسيم الفضاء إلى كتلتين وإصدار رسم بياني هيستوغرامي خالٍ من الضوضاء في كتلة واحدة، واستخدام رسم بياني هيستوغرامي خاص تفاضلياً في الأخرى. سيعتمد التقسيم على البيانات نفسها. لعينة $x_1, \ldots, x_n$، نرمز: $S = S(x_1, \ldots, x_n) = \{j : \theta_j = 0\}$. ثم نأخذ في الاعتبار آلية الإصدار:

$$z_j = \begin{cases} \theta_j & j \in S \text{ و } 2k \leq \gamma n \\ \theta_j + \frac{2}{n\alpha}L & \text{خلاف ذلك} \end{cases}$$

**القضية 5.1.** المتجه العشوائي $Z = (z_1, \ldots, z_k)$ كما هو معرف في (5) يحقق $(\alpha, \gamma)$-RDP.

في إثبات RDP، نأخذ العينة $x_1, \ldots, x_n, x_{n+1}$ ونرمز: $S = S(x_1, \ldots, x_n)$ و $S' = S(x_1, \ldots, x_{n-1}, x_{n+1})$. نأخذ في الاعتبار توزيع المخرجات لطريقتنا عند تطبيقها على كل من العينات المتجاورة. الحدث الذي تفشل فيه نسبة الكثافات في تلبية الحد المطلوب هو مجموعة فرعية من الحدث حيث إما $x_{n+1} \in S$ أو $x_n \in S'$، وعندما $2k \leq \gamma n$. في مكمل هذا الحدث تكون التقسيمات هي نفسها، وكلتا العينتين المختلفتين تقعان ضمن الكتلة التي تتلقى ضوضاء لابلاس، لذا يتحقق شرط DP. في إثبات RDP، نحدد ببساطة احتمال الحدث المذكور أعلاه، مشروطاً بإحصاءات الترتيب.

*برهان القضية 5.1.* من أجل المساحة، ليكن متجه إحصاءات الترتيب مرموزاً بـ $T = (x_{(1)}, \ldots, x_{(n+1)})$. لتكن $S^*(x_1, \ldots, x_n, x_{n+1}) = \{j : \sum_{i=1}^{n+1} \mathbf{1}\{x_i = j\} \leq 1\}$. لدينا $S, S' \subseteq S^*$. وبالتالي لدينا

$$\mathbb{P}(x_n \in S' \text{ أو } x_{n+1} \in S|T) \leq \mathbb{P}(x_n \in S^* \text{ أو } x_{n+1} \in S^*|T).$$

الاحتمال الأخير هو فقط كسر الطرق التي يمكن بها إعادة ترتيب إحصاءات الترتيب بحيث يقع $x_n, x_{n+1}$ ضمن $S^*$. نظراً للشرط $2k \leq \gamma n$، لدينا $|S^*| \leq k \leq \frac{\gamma n}{2}$. لذلك فإن عدد إعادات الترتيب التي لها واحد على الأقل من $x_n$ أو $x_{n+1}$ في $S^*$ محدود من الأعلى

$$\mathbb{P}(x_n \in S^* \text{ أو } x_{n+1} \in S^*|T) \leq \frac{2|S^*|}{n+1} < \gamma.$$

لذلك

$$\mathbb{P}(x_n \in S' \text{ أو } x_{n+1} \in S) \leq \int_{\mathcal{X}^{n+1}} \mathbb{P}(x_n \in S' \text{ أو } x_{n+1} \in S|T)dP(T) \leq \int_{\mathcal{X}^{n+1}} \mathbb{P}(x_n \in S^* \text{ أو } x_{n+1} \in S^*|T)dP(T)$$
$$< \gamma \int_{\mathcal{X}^{n+1}} dP(T) = \gamma.$$

أخيراً:

$$\mathbb{P}\left( \forall Z \subseteq \mathcal{Z}, e^{-\alpha} \leq \frac{Q_n(Z|X)}{Q_n(Z|X')} \leq e^{\alpha} \right) = 1 - \mathbb{P}(x_n \in S' \text{ أو } x_{n+1} \in S) > 1 - \gamma.$$

□

## 5.1 الدقة

نُظهر هنا أن $\delta(z)$ من (2) قريبة من $\theta$ حتى عندما يكون الرسم البياني الهيستوغرامي متناثراً.

**المبرهنة 5.2.** لنفترض أن $2k \leq \gamma n$. لتكن $\theta^n(x_1, \ldots, x_n) = (\theta_1, \ldots, \theta_r, 0, \ldots, 0)$ لبعض $1 \leq r < k$. عندئذ $||\theta - \delta(z)||_1 = O_P(r/\alpha n)$.

*البرهان.* لتكن $L_1, \ldots, L_r \sim \text{Laplace}$. ليكن $E$ الحدث بأن $L_j > -\frac{n\alpha}{2}\theta_j$ لجميع $1 \leq j \leq r$. عندئذ $E$ يحمل، باستثناء مجموعة ذات احتمال أسي صغير. لنفترض أن $E$ يحمل. ليكن $W = \sum_{j=1}^r L_j = O_P(r)$. لـ $1 \leq j \leq r$،

$$z_j = \theta_j + \frac{2L_j}{n\alpha}$$

لـ $j > r$، $z_j = \theta_j = 0$. ومن ثم $||z - \theta||_1 = O_P(r/\alpha n)$. علاوة على ذلك $||\delta(z) - z||_1 \leq \frac{r}{n} \leq \frac{r}{\alpha n}$. ومن ثم عبر متباينة المثلث لدينا، $||\delta(z) - \theta||_1 = O_P(r/\alpha n)$. □

وبالتالي لدينا تقنية تكون فيها المخاطر محدودة من الأعلى بشكل موحد بـ $O(k/\alpha n)$ كما هو الحال مع تقنية DP، والتي تتمتع أيضاً بالحد الأعلى للمخاطر على مستوى الإحداثيات. ومع ذلك في هذا النظام، لم تعد المخاطر محدودة من الأسفل بشكل موحد بمعدل خطي في $k$، لأن الحد الأعلى خطي في $r$ في حالة المتجهات المتناثرة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** sparse histogram, order statistics, Laplace noise, triangle inequality, exponentially small probability
- **Equations:** 8 equations including proof steps
- **Citations:** None
- **Special handling:** Mathematical proofs with probability bounds; O_P notation for stochastic order

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.87
- Readability: 0.87
- Glossary consistency: 0.87
- **Overall section score:** 0.87
