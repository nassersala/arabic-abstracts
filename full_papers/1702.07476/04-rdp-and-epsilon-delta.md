# Section 4: RDP and (ε, δ)-DP
## القسم 4: RDP و(ε, δ)-DP

**Section:** methodology
**Translation Quality:** 0.87
**Glossary Terms Used:** Rényi differential privacy, differential privacy, mechanism, privacy loss

---

### English Version

As we observed earlier, the definition of ε-differential privacy coincides with (∞, ε)-RDP. By monotonicity of the Rényi divergence, (∞, ε)-RDP implies (α, ε)-RDP for all finite α.

In turn, an (α, ε)-RDP implies (ε_δ, δ)-differential privacy for any given probability δ > 0.

**Proposition 3 (From RDP to (ε, δ)-DP).** If $f$ is an (α, ε)-RDP mechanism, it also satisfies $(\varepsilon + \frac{\log 1/\delta}{\alpha - 1}, \delta)$-differential privacy for any $0 < \delta < 1$.

**Proof.** Take any two adjacent inputs $D$ and $D'$, and a subset of $f$'s range $S$. To show that $f$ is $(ε', δ)$-differentially private, where $ε' = \varepsilon + \frac{1}{\alpha - 1}\log 1/\delta$, we need to demonstrate that $\Pr[f(D) \in S] \leq e^{\varepsilon'} \Pr[f(D') \in S] + \delta$. In fact, we prove a stronger statement that $\Pr[f(D) \in S] \leq \max(e^{\varepsilon'} \Pr[f(D') \in S], \delta)$.

Recall that by Proposition 10

$$\Pr[f(D) \in S] \leq \{e^{\varepsilon} \Pr[f(D') \in S]\}^{1-1/\alpha}.$$

Denote $\Pr[f(D') \in S]$ by $Q$ and consider two cases.

**Case I.** $e^{\varepsilon} Q > \delta^{\alpha/(\alpha-1)}$. Continuing the above,

$$\Pr[f(D) \in S] \leq \{e^{\varepsilon} Q\}^{1-1/\alpha} = e^{\varepsilon} Q \cdot \{e^{\varepsilon} Q\}^{-1/\alpha}$$

$$\leq e^{\varepsilon} Q \cdot \delta^{-1/(\alpha-1)} = \exp\left(\varepsilon + \frac{\log 1/\delta}{\alpha - 1}\right) \cdot Q.$$

**Case II.** $e^{\varepsilon} Q \leq \delta^{\alpha/(\alpha-1)}$. This case is immediate since

$$\Pr[f(D) \in S] \leq \{e^{\varepsilon} Q\}^{1-1/\alpha} \leq \delta,$$

which completes the proof.

A more detailed comparison between the notions of RDP and (ε, δ)-differential privacy that goes beyond these reductions is deferred to Section VII.

---

### النسخة العربية

كما لاحظنا سابقًا، يتطابق تعريف الخصوصية التفاضلية ε مع (∞, ε)-RDP. من خلال رتابة اختلاف ريني، فإن (∞, ε)-RDP يعني (α, ε)-RDP لجميع α المحدودة.

في المقابل، فإن (α, ε)-RDP يعني خصوصية تفاضلية $(ε_δ, δ)$ لأي احتمالية معطاة δ > 0.

**المقترح 3 (من RDP إلى (ε, δ)-DP).** إذا كانت $f$ آلية (α, ε)-RDP، فإنها تحقق أيضًا خصوصية تفاضلية $(\varepsilon + \frac{\log 1/\delta}{\alpha - 1}, \delta)$ لأي $0 < \delta < 1$.

**البرهان.** خذ أي مدخلين متجاورين $D$ و$D'$، ومجموعة فرعية من نطاق $f$ هي $S$. لإظهار أن $f$ خاصة تفاضليًا $(ε', δ)$، حيث $ε' = \varepsilon + \frac{1}{\alpha - 1}\log 1/\delta$، نحتاج إلى إثبات أن $\Pr[f(D) \in S] \leq e^{\varepsilon'} \Pr[f(D') \in S] + \delta$. في الواقع، نثبت بيانًا أقوى وهو أن $\Pr[f(D) \in S] \leq \max(e^{\varepsilon'} \Pr[f(D') \in S], \delta)$.

تذكر أنه بواسطة المقترح 10

$$\Pr[f(D) \in S] \leq \{e^{\varepsilon} \Pr[f(D') \in S]\}^{1-1/\alpha}.$$

دع $\Pr[f(D') \in S]$ تكون $Q$ وضع في اعتبارك حالتين.

**الحالة الأولى.** $e^{\varepsilon} Q > \delta^{\alpha/(\alpha-1)}$. بالاستمرار في ما سبق،

$$\Pr[f(D) \in S] \leq \{e^{\varepsilon} Q\}^{1-1/\alpha} = e^{\varepsilon} Q \cdot \{e^{\varepsilon} Q\}^{-1/\alpha}$$

$$\leq e^{\varepsilon} Q \cdot \delta^{-1/(\alpha-1)} = \exp\left(\varepsilon + \frac{\log 1/\delta}{\alpha - 1}\right) \cdot Q.$$

**الحالة الثانية.** $e^{\varepsilon} Q \leq \delta^{\alpha/(\alpha-1)}$. هذه الحالة فورية حيث

$$\Pr[f(D) \in S] \leq \{e^{\varepsilon} Q\}^{1-1/\alpha} \leq \delta,$$

مما يكمل البرهان.

تتم المقارنة الأكثر تفصيلاً بين مفاهيم RDP والخصوصية التفاضلية (ε, δ) التي تتجاوز هذه الاختزالات في القسم السابع.

---

### Translation Notes

- **Key terms introduced:** None (all previously introduced)
- **Figures referenced:** None
- **Equations:** Mathematical proof with case analysis
- **Citations:** References to Section VII and Proposition 10
- **Special handling:** Case-by-case proof structure

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
