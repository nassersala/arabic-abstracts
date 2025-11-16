# Section 4: Random Differential Privacy
## القسم 4: الخصوصية التفاضلية العشوائية

**Section:** random-differential-privacy
**Translation Quality:** 0.88
**Glossary Terms Used:** random differential privacy, differential privacy, distribution, database, privacy, algorithm, composition

---

### English Version

In random differential privacy (RDP) we view the data $X = (X_1, \ldots, X_n)$ as random draws from an unknown distribution $P$. This is certainly the case in statistical sampling and of course it is the usual assumption in most learning theory. Let us denote the observed values of the random variables $X = (X_1, \ldots, X_n)$ by $x = (x_1, \ldots, x_n)$. Recall that under DP, $Q(Z \in B|x_1, \ldots, x_n)$ is not strongly affected if we replace some value $x_i$ with another value $x'_i$. We continue to restrict to the case in which, $Q(Z \in B|x_1, \ldots, x_n)$ is invariant to permutations of $(x_1, \ldots, x_n)$. Thus we may restate DP by saying that $Q(Z \in B|x_1, \ldots, x_n)$ is not strongly affected if we replace $x_n$ by some other arbitrary value $x'_n$. In RDP, we require instead that the distribution $Q_n(\cdot|x_1, \ldots, x_n)$ is not strongly affected if we replace $x_n$ by some new $x'_n$ which is also randomly drawn from $P$.

**Definition 1** ($(\alpha, \gamma)$-Random Differential Privacy). We say that a randomized algorithm $Q_n$ is $(\alpha, \gamma)$-Randomly Differentially Private when:

$$\mathbb{P}\left( \forall B \subseteq \mathcal{Z}, e^{-\alpha} \leq \frac{Q_n(Z \in B|X)}{Q_n(Z \in B|X')} \leq e^{\alpha} \right) \geq 1 - \gamma$$

where
$$X = (X_1, \ldots, X_{n-1}, X_n), \quad X' = (X_1, \ldots, X_{n-1}, X_{n+1})$$

(i.e., $X \sim X'$), and the probability is with respect to the $n+1$-fold product measure $P^{n+1}$ on the space $\mathcal{X}^{n+1}$, that is, $X_1, \ldots, X_{n+1} \stackrel{\text{iid}}{\sim} P$.

We also give the "random" analog of the $(\alpha, \delta)$-Differential Privacy:

**Definition 2** ($(\alpha, \eta, \gamma)$-Random Differential Privacy). We say that a randomized algorithm $Q_n$ is $(\alpha, \eta, \gamma)$-Randomly Differentially Private when:

$$\mathbb{P}(\forall B \subseteq \mathcal{Z}, Q_n(Z \in B|X) \leq e^{\alpha}Q_n(Z \in B|X') + \eta(n)) \geq 1 - \gamma$$

where $\eta$ is negligible (i.e., decreasing faster than any inverse polynomial).

We note that [12] also consider a probabilistic relaxation of DP. However, their relaxation is quite different than the one considered here. Namely, their relaxation bounds the probability that the differential privacy criteria is not met, but where the probability is taken with respect to the randomized algorithm itself. Our relaxation takes the probability with respect to the generation of the data itself. The following result is clear from the definition of random differential privacy.

**Proposition 4.1.** $(\alpha, \gamma)$-RDP is a strict relaxation of $\alpha$-DP. That is, if $Q_n$ is DP then it is also RDP. However, there are RDP procedures that are not DP.

**Remark 3.** Although an $\alpha$-DP procedure fulfils the requirement of $(\alpha, 0)$-RDP, the converse is not true. The reason is that the latter requires that the condition (that the ratio of densities be bounded) holds almost everywhere with respect to the unknown measure, whereas DP require that this condition holds uniformly everywhere in the space.

We next show an important property of the definition, namely, that RDP algorithms may be composed to give other RDP algorithms with different constants. The analogous composition property for DP was considered to be important because it allowed rapid development of techniques which release multiple statistics, as well as techniques which allow interactive access to the data.

**Proposition 4.2** (Composition). Suppose $Q, Q'$ are distributions over $\mathcal{Z}, \mathcal{Z}'$ which are $(\alpha, \gamma)$-RDP and $(\alpha', \gamma')$-RDP respectively. The following distribution $C$ over $\mathcal{Z} \times \mathcal{Z}'$ is $(\alpha + \alpha', \gamma + \gamma')$-RDP:

$$C(Z, Z'|X) = Q(Z|X) \cdot Q'(Z'|X).$$

This result is simply an application of the union bound combined with the standard composition property of differential privacy. As an example, suppose it is required to release $k$ different statistics of some data sample. If each one is released via a $(\alpha/k, \gamma/k)$-RDP procedure, then the overall release of all $k$ statistics together achieves $(\alpha, \gamma)$-RDP. A similar result holds for the composition of $(\alpha, \delta, \gamma)$-RDP releases.

---

### النسخة العربية

في الخصوصية التفاضلية العشوائية (RDP) نعتبر البيانات $X = (X_1, \ldots, X_n)$ عمليات سحب عشوائية من توزيع غير معروف $P$. هذا بالتأكيد هو الحال في أخذ العينات الإحصائية وبالطبع هو الافتراض المعتاد في معظم نظرية التعلم. دعنا نرمز للقيم الملاحظة للمتغيرات العشوائية $X = (X_1, \ldots, X_n)$ بـ $x = (x_1, \ldots, x_n)$. تذكر أنه في ظل DP، فإن $Q(Z \in B|x_1, \ldots, x_n)$ لا تتأثر بشكل قوي إذا استبدلنا بعض القيمة $x_i$ بقيمة أخرى $x'_i$. نستمر في التقييد بالحالة التي يكون فيها $Q(Z \in B|x_1, \ldots, x_n)$ ثابتاً بالنسبة لتبديلات $(x_1, \ldots, x_n)$. وبالتالي يمكننا إعادة صياغة DP بقول أن $Q(Z \in B|x_1, \ldots, x_n)$ لا تتأثر بشكل قوي إذا استبدلنا $x_n$ ببعض القيمة التعسفية الأخرى $x'_n$. في RDP، نتطلب بدلاً من ذلك أن التوزيع $Q_n(\cdot|x_1, \ldots, x_n)$ لا يتأثر بشكل قوي إذا استبدلنا $x_n$ بـ $x'_n$ جديد يتم سحبه أيضاً عشوائياً من $P$.

**التعريف 1** (الخصوصية التفاضلية العشوائية $(\alpha, \gamma)$). نقول إن خوارزمية عشوائية $Q_n$ هي خاصة تفاضلياً عشوائياً $(\alpha, \gamma)$ عندما:

$$\mathbb{P}\left( \forall B \subseteq \mathcal{Z}, e^{-\alpha} \leq \frac{Q_n(Z \in B|X)}{Q_n(Z \in B|X')} \leq e^{\alpha} \right) \geq 1 - \gamma$$

حيث
$$X = (X_1, \ldots, X_{n-1}, X_n), \quad X' = (X_1, \ldots, X_{n-1}, X_{n+1})$$

(أي $X \sim X'$)، والاحتمال هو بالنسبة للقياس الضربي $n+1$ $P^{n+1}$ على الفضاء $\mathcal{X}^{n+1}$، أي $X_1, \ldots, X_{n+1} \stackrel{\text{iid}}{\sim} P$.

نعطي أيضاً النظير "العشوائي" للخصوصية التفاضلية $(\alpha, \delta)$:

**التعريف 2** (الخصوصية التفاضلية العشوائية $(\alpha, \eta, \gamma)$). نقول إن خوارزمية عشوائية $Q_n$ هي خاصة تفاضلياً عشوائياً $(\alpha, \eta, \gamma)$ عندما:

$$\mathbb{P}(\forall B \subseteq \mathcal{Z}, Q_n(Z \in B|X) \leq e^{\alpha}Q_n(Z \in B|X') + \eta(n)) \geq 1 - \gamma$$

حيث $\eta$ ضئيلة (أي تتناقص أسرع من أي كثيرة حدود معكوسة).

نلاحظ أن [12] يأخذون في الاعتبار أيضاً إرخاءً احتمالياً لـ DP. ومع ذلك، فإن إرخاءهم مختلف تماماً عن الإرخاء المعتبر هنا. أي أن إرخاءهم يحدد الاحتمال بأن معايير الخصوصية التفاضلية لا تتحقق، ولكن حيث يؤخذ الاحتمال بالنسبة للخوارزمية العشوائية نفسها. إرخاؤنا يأخذ الاحتمال بالنسبة لتوليد البيانات نفسها. النتيجة التالية واضحة من تعريف الخصوصية التفاضلية العشوائية.

**القضية 4.1.** RDP $(\alpha, \gamma)$ هو إرخاء صارم لـ $\alpha$-DP. أي، إذا كان $Q_n$ هو DP فهو أيضاً RDP. ومع ذلك، هناك إجراءات RDP ليست DP.

**ملاحظة 3.** على الرغم من أن إجراء $\alpha$-DP يحقق متطلب $(\alpha, 0)$-RDP، فإن العكس غير صحيح. السبب هو أن الأخير يتطلب أن الشرط (أن نسبة الكثافات محدودة) يحمل في كل مكان تقريباً بالنسبة للقياس غير المعروف، بينما DP يتطلب أن هذا الشرط يحمل بشكل موحد في كل مكان في الفضاء.

نُظهر بعد ذلك خاصية مهمة للتعريف، وهي أنه يمكن تركيب خوارزميات RDP لإعطاء خوارزميات RDP أخرى بثوابت مختلفة. كانت خاصية التركيب المماثلة لـ DP تُعتبر مهمة لأنها سمحت بالتطوير السريع للتقنيات التي تصدر إحصاءات متعددة، بالإضافة إلى التقنيات التي تسمح بالوصول التفاعلي إلى البيانات.

**القضية 4.2** (التركيب). لنفترض أن $Q, Q'$ توزيعان على $\mathcal{Z}, \mathcal{Z}'$ وهما $(\alpha, \gamma)$-RDP و $(\alpha', \gamma')$-RDP على التوالي. التوزيع التالي $C$ على $\mathcal{Z} \times \mathcal{Z}'$ هو $(\alpha + \alpha', \gamma + \gamma')$-RDP:

$$C(Z, Z'|X) = Q(Z|X) \cdot Q'(Z'|X).$$

هذه النتيجة هي ببساطة تطبيق لحد الاتحاد مع خاصية التركيب القياسية للخصوصية التفاضلية. كمثال، لنفترض أنه مطلوب إصدار $k$ إحصاءات مختلفة لعينة بيانات ما. إذا تم إصدار كل واحدة عبر إجراء $(\alpha/k, \gamma/k)$-RDP، فإن الإصدار الكلي لجميع الإحصاءات $k$ معاً يحقق $(\alpha, \gamma)$-RDP. نتيجة مماثلة تحمل لتركيب إصدارات $(\alpha, \delta, \gamma)$-RDP.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** random differential privacy (RDP), product measure, iid (independent and identically distributed), composition property, union bound
- **Equations:** 5 main equations with definitions and properties
- **Citations:** [12]
- **Special handling:** Mathematical definitions with probability theory; comparison between RDP and standard DP

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.88
- Readability: 0.88
- Glossary consistency: 0.88
- **Overall section score:** 0.88
