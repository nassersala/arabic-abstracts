# Section 4: FedProx Convergence Analysis
## القسم 4: تحليل التقارب لـ FedProx

**Section:** convergence-analysis
**Translation Quality:** 0.86
**Glossary Terms Used:** convergence, dissimilarity, heterogeneous, non-convex, optimization, gradient, stationary point, bounded, algorithm, framework

---

### English Version

## 4.1 Local Dissimilarity

The paper introduces a measure to quantify dissimilarity between devices in federated networks. This metric is essential for proving convergence without assuming identical data distribution across devices.

**Definition 3 (B-local dissimilarity)** states: The local functions $F_k$ are B-locally dissimilar at $w$ if

$$\mathbb{E}_k[\|\nabla F_k(w)\|^2] \leq \|\nabla f(w)\|^2 B^2$$

The authors also define $B(w)$ as the ratio measuring dissimilarity at specific points. Importantly, when all local functions are identical, $B(w)=1$. In federated settings with heterogeneous data, $B>1$ due to sampling discrepancies.

**Assumption 1 (Bounded dissimilarity)** requires: For some $\epsilon>0$, there exists a $B_\epsilon$ such that for all points $w \in \mathcal{S}_\epsilon^c$ where $\|\nabla f(w)\|^2 > \epsilon$, $B(w) \leq B_\epsilon$

This assumption is practical because most machine learning applications don't require solving to highly accurate stationary solutions. The dissimilarity metric captures real-world heterogeneity and correlates with empirical performance.

## 4.2 FedProx Analysis

**Theorem 4** provides convergence guarantees for non-convex functions. Under specified conditions on $\mu$, $K$, and $\gamma$, the method achieves:

$$\mathbb{E}_{S_t}[f(w^{t+1})] \leq f(w^t) - \rho\|\nabla f(w^t)\|^2$$

The proof demonstrates expected objective decrease at each iteration by applying $\gamma$-inexactness definitions and the bounded dissimilarity assumption while accounting for partial device participation.

**Theorem 6** establishes convergence rates. After $T=O(\Delta/(\rho\epsilon))$ iterations, the method achieves approximate stationarity where averaged gradient norms satisfy:

$$\frac{1}{T} \sum_{t=0}^{T-1} \mathbb{E}[\|\nabla f(w^t)\|^2] \leq \epsilon$$

**Corollary 7** specializes results to convex cases with exact minimization, showing convergence with appropriately chosen $\mu$.

**Corollary 9** extends analysis to variable $\gamma$ values across devices and iterations, accommodating systems heterogeneity where different devices perform different amounts of local computation based on resource constraints.

---

### النسخة العربية

## 4.1 التباين المحلي

تقدم الورقة مقياسًا لقياس التباين بين الأجهزة في الشبكات الاتحادية. هذا المقياس ضروري لإثبات التقارب دون افتراض توزيع بيانات متطابق عبر الأجهزة.

**التعريف 3 (التباين المحلي B)** ينص على: الدوال المحلية $F_k$ متباينة محليًا بمقدار B عند $w$ إذا كان

$$\mathbb{E}_k[\|\nabla F_k(w)\|^2] \leq \|\nabla f(w)\|^2 B^2$$

يُعرّف المؤلفون أيضًا $B(w)$ كنسبة تقيس التباين عند نقاط محددة. من المهم أنه عندما تكون جميع الدوال المحلية متطابقة، يكون $B(w)=1$. في الإعدادات الاتحادية مع بيانات غير متجانسة، يكون $B>1$ بسبب اختلافات العينات.

**الافتراض 1 (التباين المحدود)** يتطلب: لبعض $\epsilon>0$، يوجد $B_\epsilon$ بحيث لجميع النقاط $w \in \mathcal{S}_\epsilon^c$ حيث $\|\nabla f(w)\|^2 > \epsilon$، يكون $B(w) \leq B_\epsilon$

هذا الافتراض عملي لأن معظم تطبيقات التعلم الآلي لا تتطلب الحل إلى حلول ثابتة عالية الدقة. يلتقط مقياس التباين عدم التجانس في العالم الحقيقي ويرتبط بالأداء التجريبي.

## 4.2 تحليل FedProx

**النظرية 4** توفر ضمانات التقارب للدوال غير المحدبة. في ظل شروط محددة على $\mu$ و $K$ و $\gamma$، تحقق الطريقة:

$$\mathbb{E}_{S_t}[f(w^{t+1})] \leq f(w^t) - \rho\|\nabla f(w^t)\|^2$$

يوضح الإثبات انخفاض الهدف المتوقع في كل تكرار من خلال تطبيق تعريفات $\gamma$-عدم الدقة وافتراض التباين المحدود مع مراعاة المشاركة الجزئية للأجهزة.

**النظرية 6** تؤسس معدلات التقارب. بعد $T=O(\Delta/(\rho\epsilon))$ من التكرارات، تحقق الطريقة ثباتًا تقريبيًا حيث تحقق معايير التدرج المتوسطة:

$$\frac{1}{T} \sum_{t=0}^{T-1} \mathbb{E}[\|\nabla f(w^t)\|^2] \leq \epsilon$$

**النتيجة 7** تخصص النتائج للحالات المحدبة مع التصغير الدقيق، مما يُظهر التقارب مع $\mu$ المختار بشكل مناسب.

**النتيجة 9** توسع التحليل لقيم $\gamma$ المتغيرة عبر الأجهزة والتكرارات، مما يستوعب عدم التجانس في الأنظمة حيث تؤدي الأجهزة المختلفة كميات مختلفة من الحساب المحلي بناءً على قيود الموارد.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - B-local dissimilarity (التباين المحلي B)
  - bounded dissimilarity (التباين المحدود)
  - stationary point (نقطة ثابتة)
  - approximate stationarity (ثبات تقريبي)
  - expected objective decrease (انخفاض الهدف المتوقع)
  - gradient norm (معيار التدرج)
  - non-convex function (دالة غير محدبة)
- **Equations:** 4 main mathematical expressions
- **Citations:** None directly referenced
- **Special handling:**
  - Mathematical notation preserved exactly in LaTeX
  - Definitions, theorems, assumptions, and corollaries clearly marked
  - Greek letters (ε, ρ, γ, μ) kept as-is in formulas
  - Set notation (∈, ∇, 𝔼, ∑) preserved
  - Big-O notation O(·) maintained

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
