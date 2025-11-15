# Section 3: Concentration
## القسم 3: التركيز

**Section:** analysis
**Translation Quality:** 0.87
**Glossary Terms Used:** regular graph, MaxCut, variance, standard deviation, distribution, probability, concentration

---

### English Version

Still using MaxCut on regular graphs as our example, it is useful to get information about the spread of C measured in the state $|γ, β⟩$. If v is fixed and p is fixed (or grows slowly with n) the distribution of C(z) is actually concentrated near its mean. To see this, calculate

$$⟨γ, β| C^2 |γ, β⟩ - ⟨γ, β| C |γ, β⟩^2$$

$$= \sum_{⟨jk⟩, ⟨j'k'⟩} \left[⟨s|U^†(C, γ_1) \cdots U^†(B, β_p) C_{⟨jk⟩} C_{⟨j'k'⟩} U(B, β_p) \cdots U(C, γ_1)|s⟩\right.$$

$$\left.- ⟨s|U^†(C, γ_1) \cdots U^†(B, β_p) C_{⟨jk⟩} U(B, β_p) \cdots U(C, γ_1)|s⟩ \cdot ⟨s|U^†(C, γ_1) \cdots U^†(B, β_p) C_{⟨j'k'⟩} U(B, β_p) \cdots U(C, γ_1)|s⟩\right]$$

If the subgraphs $g(j, k)$ and $g(j', k')$ do not involve any common qubits, the summand in (28) will be 0. The subgraphs $g(j, k)$ and $g(j', k')$ will have no common qubits as long as there is no path in the instance graph from $⟨jk⟩$ to $⟨j'k'⟩$ of length 2p + 1 or shorter. From (26) with p replaced by 2p + 1 we see that for each $⟨jk⟩$ there are at most

$$2\left[\frac{(v-1)^{2p+2} - 1}{(v-1) - 1}\right]$$

edges $⟨j'k'⟩$ which could contribute to the sum in (28) (or 4p + 4 if v = 2) and therefore

$$⟨γ, β| C^2 |γ, β⟩ - ⟨γ, β| C |γ, β⟩^2 \leq 2\left[\frac{(v-1)^{2p+2} - 1}{(v-1) - 1}\right] \cdot m$$

since each summand is at most 1 in norm. For v and p fixed we see that the standard deviation of C(z) is at most of order $\sqrt{m}$. This implies that the sample mean of order $m^2$ values of C(z) will be within 1 of $F_p(γ, β)$ with probability $1 - \frac{1}{m}$. The concentration of the distribution of C(z) also means that there is only a small probability that the algorithm will produce strings with C(z) much bigger than $F_p(γ, β)$.

---

### النسخة العربية

لا نزال نستخدم مسألة القطع الأعظمي على الرسوم البيانية المنتظمة كمثالنا، ومن المفيد الحصول على معلومات حول انتشار C المقاسة في الحالة $|γ, β⟩$. إذا كان v ثابتاً و p ثابتاً (أو ينمو ببطء مع n)، فإن توزيع C(z) في الواقع متركز بالقرب من متوسطه. لنرى ذلك، لنحسب:

$$⟨γ, β| C^2 |γ, β⟩ - ⟨γ, β| C |γ, β⟩^2$$

$$= \sum_{⟨jk⟩, ⟨j'k'⟩} \left[⟨s|U^†(C, γ_1) \cdots U^†(B, β_p) C_{⟨jk⟩} C_{⟨j'k'⟩} U(B, β_p) \cdots U(C, γ_1)|s⟩\right.$$

$$\left.- ⟨s|U^†(C, γ_1) \cdots U^†(B, β_p) C_{⟨jk⟩} U(B, β_p) \cdots U(C, γ_1)|s⟩ \cdot ⟨s|U^†(C, γ_1) \cdots U^†(B, β_p) C_{⟨j'k'⟩} U(B, β_p) \cdots U(C, γ_1)|s⟩\right]$$

إذا لم تكن الرسوم البيانية الفرعية $g(j, k)$ و $g(j', k')$ تشمل أي كيوبتات مشتركة، فإن المجموع في (28) سيكون 0. لن يكون للرسوم البيانية الفرعية $g(j, k)$ و $g(j', k')$ كيوبتات مشتركة طالما لا يوجد مسار في الرسم البياني المثالي من $⟨jk⟩$ إلى $⟨j'k'⟩$ بطول 2p + 1 أو أقصر. من (26) مع استبدال p بـ 2p + 1 نرى أنه لكل $⟨jk⟩$ يوجد على الأكثر:

$$2\left[\frac{(v-1)^{2p+2} - 1}{(v-1) - 1}\right]$$

حواف $⟨j'k'⟩$ التي يمكن أن تساهم في المجموع في (28) (أو 4p + 4 إذا كان v = 2) وبالتالي:

$$⟨γ, β| C^2 |γ, β⟩ - ⟨γ, β| C |γ, β⟩^2 \leq 2\left[\frac{(v-1)^{2p+2} - 1}{(v-1) - 1}\right] \cdot m$$

بما أن كل مجموع على الأكثر 1 في المعيار. لقيم v و p ثابتة نرى أن الانحراف المعياري لـ C(z) على الأكثر من رتبة $\sqrt{m}$. هذا يعني أن متوسط العينة من رتبة $m^2$ من قيم C(z) سيكون ضمن 1 من $F_p(γ, β)$ باحتمالية $1 - \frac{1}{m}$. تركيز توزيع C(z) يعني أيضاً أن هناك احتمالية صغيرة فقط أن تنتج الخوارزمية سلاسل بقيمة C(z) أكبر بكثير من $F_p(γ, β)$.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** concentration (التركيز), variance (التباين), standard deviation (الانحراف المعياري), sample mean (متوسط العينة)
- **Equations:** 5 mathematical equations preserved in LaTeX format
- **Citations:** References to equation (26) from previous section
- **Special handling:** Statistical terminology; variance calculation; probabilistic bounds

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.87
