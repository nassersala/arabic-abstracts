# Section 5: MaxCut on 3-Regular Graphs
## القسم 5: القطع الأعظمي على الرسوم البيانية المنتظمة ثلاثياً

**Section:** experimental-results
**Translation Quality:** 0.87
**Glossary Terms Used:** 3-regular graph, MaxCut, QAOA, approximation ratio, isolated triangle, crossed square, subgraph, classical algorithm

---

### English Version

We now look at how the Quantum Approximate Optimization Algorithm, the QAOA, performs on MaxCut on (connected) 3-regular graphs. The approximation ratio is C(z), where z is the output of the quantum algorithm, divided by the maximum of C. We first show that for p = 1, the worst case approximation ratio that the quantum algorithm produces is 0.6924.

Suppose a 3-regular graph with n vertices (and accordingly 3n/2 edges) contains T "isolated triangles" and S "crossed squares", which are subgraphs of the form,

[Diagram showing isolated triangle and crossed square configurations]

The dotted lines indicate edges that leave the isolated triangle and the crossed square. To say that the triangle is isolated is to say that the 3 edges that leave the triangle end on distinct vertices. If the two edges that leave the crossed square are in fact the same edge, then we have a 4 vertex disconnected 3-regular graph. For this special case (the only case where the analysis below does not apply) the approximation ratio is actually higher than 0.6924. In general, $3T + 4S \leq n$ because no isolated triangle and crossed square can share a vertex.

Return to the edge sum in $F_1(γ, β)$ of equation (13). For each crossed square there is one edge $⟨jk⟩$ for which $g(j, k)$ is the first type displayed in (18). Call this subgraph type $g_4$ because it has 4 vertices. In each crossed square there are 4 edges that give rise to subgraphs of the second type displayed in (18). We call this subgraph type $g_5$ because it has 5 vertices. All 3 of the edges in any isolated triangle have subgraph type $g_5$, so there are $4S + 3T$ edges with subgraph type $g_5$. The remaining edges in the graph all have a subgraph type like the third one displayed in (18) and we call this subgraph type $g_6$. There are $(3n/2 - 5S - 3T)$ of these so we have

$$F_1(γ, β) = S f_{g_4}(γ, β) + (4S + 3T) f_{g_5}(γ, β) + \left(\frac{3n}{2} - 5S - 3T\right) f_{g_6}(γ, β)$$

The maximum of $F_1$ is a function of n, S, and T,

$$M_1(n, S, T) = \max_{γ,β} F_1(γ, β)$$

Given any 3 regular graph it is straightforward to count S and T. Then using a classical computer it is straightforward to calculate $M_1(n, S, T)$. Running a quantum computer with the maximizing angles γ and β will produce the state $|γ, β⟩$ which is then measured in the computational basis. With order $n \log n$ repetitions a string will be found whose cut value is very near or larger than $M_1(n, S, T)$.

To get the approximation ratio we need to know the best cut that can be obtained for the input graph. This is not just a function of S and T. However a graph with S crossed squares and T isolated triangles must have at least one unsatisfied edge per crossed square and one unsatisfied edge per isolated triangle so the number of satisfied edges is $\leq (3n/2 - S - T)$. This means that for any graph characterized by n, S and T the quantum algorithm will produce an approximation ratio that is at least

$$\frac{M_1(n, S, T)}{(3n/2 - S - T)}$$

It is convenient to scale out n from the top and bottom of (34). Note that $M_1/n$ which comes from $F_1/n$ depends only on $S/n \equiv s$ and $T/n \equiv t$. So we can write (34) as

$$\frac{M_1(1, s, t)}{(3/2 - s - t)}$$

where $s, t \geq 0$ and $4s + 3t \leq 1$. It is straightforward to numerically evaluate (35) and we find that it achieves its minimum value at $s = t = 0$ and the value is 0.6924. So we know that on any 3-regular graph, the QAOA will always produce a cut whose size is at least 0.6924 times the size of the optimal cut. This p = 1 result on 3-regular graphs is not as good as known classical algorithms [1].

It is possible to analyze the performance of the QAOA for p = 2 on 3-regular graphs. However it is more complicated then the p = 1 case and we will just show partial results. The subgraph type with the most qubits is this tree with 14 vertices:

[Diagram showing tree structure with 14 vertices]

Numerically maximizing (24) with g given by (36) yields 0.7559. Consider a 3-regular graph on n vertices with o(n) pentagons, squares and triangles. Then all but o(n) edges have (36) as their subgraph type. The QAOA at p = 2 cannot detect whether the graph is bipartite, that is, completely satisfiable, or contains many odd loops of length 7 or longer. If the graph is bipartite the approximation ratio is 0.7559 in the limit of large n. If the graph contains many odd loops (length 7 or more), the approximation ratio will be higher.

---

### النسخة العربية

ننظر الآن إلى كيفية أداء خوارزمية التحسين التقريبي الكمومية، QAOA، على مسألة القطع الأعظمي على الرسوم البيانية المنتظمة ثلاثياً (المتصلة). نسبة التقريب هي C(z)، حيث z هي مخرجات الخوارزمية الكمومية، مقسومة على القيمة العظمى لـ C. نبيّن أولاً أنه لـ p = 1، فإن أسوأ حالة لنسبة التقريب التي تنتجها الخوارزمية الكمومية هي 0.6924.

لنفترض أن رسماً بيانياً منتظماً ثلاثياً بـ n رأساً (وبالتالي 3n/2 حافة) يحتوي على T "مثلثات معزولة" و S "مربعات متقاطعة"، وهي رسوم بيانية فرعية من الشكل:

[رسم تخطيطي يظهر تكوينات المثلث المعزول والمربع المتقاطع]

تشير الخطوط المنقطة إلى الحواف التي تغادر المثلث المعزول والمربع المتقاطع. القول بأن المثلث معزول يعني أن الحواف الثلاث التي تغادر المثلث تنتهي عند رؤوس متمايزة. إذا كانت الحافتان اللتان تغادران المربع المتقاطع هما في الواقع نفس الحافة، فلدينا رسم بياني منتظم ثلاثياً منفصل بـ 4 رؤوس. لهذه الحالة الخاصة (الحالة الوحيدة التي لا ينطبق فيها التحليل أدناه) فإن نسبة التقريب أعلى في الواقع من 0.6924. بشكل عام، $3T + 4S \leq n$ لأن أي مثلث معزول ومربع متقاطع لا يمكنهما مشاركة رأس.

لنعد إلى مجموع الحواف في $F_1(γ, β)$ من المعادلة (13). لكل مربع متقاطع توجد حافة واحدة $⟨jk⟩$ حيث $g(j, k)$ هو النوع الأول المعروض في (18). نسمي هذا النوع من الرسم البياني الفرعي $g_4$ لأنه يحتوي على 4 رؤوس. في كل مربع متقاطع توجد 4 حواف تعطي رسوماً بيانية فرعية من النوع الثاني المعروض في (18). نسمي هذا النوع من الرسم البياني الفرعي $g_5$ لأنه يحتوي على 5 رؤوس. جميع الحواف الثلاث في أي مثلث معزول لها نوع الرسم البياني الفرعي $g_5$، لذا يوجد $4S + 3T$ حافة من نوع الرسم البياني الفرعي $g_5$. الحواف المتبقية في الرسم البياني جميعها لها نوع رسم بياني فرعي مثل النوع الثالث المعروض في (18) ونسمي هذا النوع من الرسم البياني الفرعي $g_6$. يوجد $(3n/2 - 5S - 3T)$ منها لذا لدينا:

$$F_1(γ, β) = S f_{g_4}(γ, β) + (4S + 3T) f_{g_5}(γ, β) + \left(\frac{3n}{2} - 5S - 3T\right) f_{g_6}(γ, β)$$

القيمة العظمى لـ $F_1$ هي دالة لـ n و S و T:

$$M_1(n, S, T) = \max_{γ,β} F_1(γ, β)$$

بإعطاء أي رسم بياني منتظم ثلاثياً، من المباشر عد S و T. ثم باستخدام حاسوب تقليدي من المباشر حساب $M_1(n, S, T)$. تشغيل حاسوب كمومي بزوايا التعظيم γ و β سينتج الحالة $|γ, β⟩$ التي تُقاس بعد ذلك في الأساس الحسابي. مع تكرارات من رتبة $n \log n$ ستُوجد سلسلة تكون قيمة قطعها قريبة جداً من أو أكبر من $M_1(n, S, T)$.

للحصول على نسبة التقريب نحتاج إلى معرفة أفضل قطع يمكن الحصول عليه للرسم البياني المدخل. هذا ليس مجرد دالة لـ S و T. لكن رسماً بيانياً بـ S مربعات متقاطعة و T مثلثات معزولة يجب أن يكون فيه على الأقل حافة واحدة غير محققة لكل مربع متقاطع وحافة واحدة غير محققة لكل مثلث معزول لذا فإن عدد الحواف المحققة هو $\leq (3n/2 - S - T)$. هذا يعني أنه لأي رسم بياني يتميز بـ n و S و T فإن الخوارزمية الكمومية ستنتج نسبة تقريب على الأقل:

$$\frac{M_1(n, S, T)}{(3n/2 - S - T)}$$

من المناسب استخراج n من البسط والمقام في (34). لاحظ أن $M_1/n$ التي تأتي من $F_1/n$ تعتمد فقط على $S/n \equiv s$ و $T/n \equiv t$. لذا يمكننا كتابة (34) كـ:

$$\frac{M_1(1, s, t)}{(3/2 - s - t)}$$

حيث $s, t \geq 0$ و $4s + 3t \leq 1$. من المباشر حساب (35) عددياً ونجد أنها تحقق قيمتها الدنيا عند $s = t = 0$ والقيمة هي 0.6924. لذا نعلم أنه على أي رسم بياني منتظم ثلاثياً، فإن QAOA ستنتج دائماً قطعاً يكون حجمه على الأقل 0.6924 مرة حجم القطع الأمثل. هذه النتيجة لـ p = 1 على الرسوم البيانية المنتظمة ثلاثياً ليست جيدة مثل الخوارزميات التقليدية المعروفة [1].

من الممكن تحليل أداء QAOA لـ p = 2 على الرسوم البيانية المنتظمة ثلاثياً. لكنها أكثر تعقيداً من حالة p = 1 وسنعرض فقط نتائج جزئية. نوع الرسم البياني الفرعي الذي يحتوي على أكبر عدد من الكيوبتات هو هذه الشجرة بـ 14 رأساً:

[رسم تخطيطي يظهر بنية الشجرة بـ 14 رأساً]

التعظيم العددي لـ (24) مع g المعطاة بـ (36) يعطي 0.7559. لنفكر في رسم بياني منتظم ثلاثياً على n رأساً مع o(n) من الخماسيات والمربعات والمثلثات. حينئذٍ جميع الحواف باستثناء o(n) لها (36) كنوع رسمها البياني الفرعي. لا يمكن لـ QAOA عند p = 2 اكتشاف ما إذا كان الرسم البياني ثنائي الأجزاء، أي قابل للإرضاء بالكامل، أو يحتوي على العديد من الحلقات الفردية بطول 7 أو أكثر. إذا كان الرسم البياني ثنائي الأجزاء فإن نسبة التقريب هي 0.7559 في نهاية n الكبيرة. إذا كان الرسم البياني يحتوي على العديد من الحلقات الفردية (بطول 7 أو أكثر)، فإن نسبة التقريب ستكون أعلى.

---

### Translation Notes

- **Figures referenced:** Diagrams (31) showing isolated triangles and crossed squares, diagram (36) showing tree with 14 vertices
- **Key terms introduced:** isolated triangle (مثلث معزول), crossed square (مربع متقاطع), bipartite (ثنائي الأجزاء), odd loop (حلقة فردية)
- **Equations:** 5 mathematical equations and inequalities
- **Citations:** Reference [1] to classical algorithms paper
- **Special handling:** Graph substructure terminology; worst-case analysis; comparison with classical algorithms

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
