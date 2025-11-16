# Section 8: Example
## القسم 8: مثال

**Section:** example
**Translation Quality:** 0.87
**Glossary Terms Used:** random differential privacy, differential privacy, histogram, accuracy, loss function, simulation

---

### English Version

We present two examples in which the RDP technique and the DP techniques are compared on synthetic histogram data. In the first example the histogram has $k = 25$ bins, all but two of which are empty and $n = 500$ points fall in to the other two. Figure 1(a) shows the original data as well as the sanitized data due to differential privacy and RDP. Figure 1(b) shows the distribution of $L_1$ loss from 100 simulations of both approaches. We see that the risk of the RDP histogram is typically much lower than that of the DP histogram, which occasionally has risk in excess of 0.5 (recall that the maximum possible loss is 2 in the case that the original and sanitized histograms had completely disjoint support).

We present an analogous two dimensional example in figure 2. Here the histogram has $k = 400$ bins in which all but 16 are empty. In this example we see that the RDP technique has uniformly better loss than the DP technique.

---

### النسخة العربية

نقدم مثالين يتم فيهما مقارنة تقنية RDP وتقنيات DP على بيانات رسوم بيانية هيستوغرامية اصطناعية. في المثال الأول، يحتوي الرسم البياني الهيستوغرامي على $k = 25$ حاوية، كلها فارغة باستثناء اثنتين وتقع $n = 500$ نقطة في الاثنتين الأخريين. يُظهر الشكل 1(a) البيانات الأصلية بالإضافة إلى البيانات المعقمة بسبب الخصوصية التفاضلية و RDP. يُظهر الشكل 1(b) توزيع خسارة $L_1$ من 100 محاكاة لكلا النهجين. نرى أن مخاطر الرسم البياني الهيستوغرامي RDP عادة أقل بكثير من تلك الخاصة بالرسم البياني الهيستوغرامي DP، والتي لديها أحياناً مخاطر تزيد عن 0.5 (تذكر أن الحد الأقصى للخسارة الممكنة هو 2 في حالة أن الرسوم البيانية الهيستوغرامية الأصلية والمعقمة كان لها دعم منفصل تماماً).

نقدم مثالاً ثنائي الأبعاد مماثلاً في الشكل 2. هنا يحتوي الرسم البياني الهيستوغرامي على $k = 400$ حاوية جميعها فارغة باستثناء 16. في هذا المثال نرى أن تقنية RDP لديها خسارة أفضل بشكل موحد من تقنية DP.

---

### Translation Notes

- **Figures referenced:** Figure 1(a), Figure 1(b), Figure 2
- **Key terms introduced:** synthetic data, sanitized data, simulation, disjoint support
- **Equations:** None (empirical results)
- **Citations:** None
- **Special handling:** Description of experimental results with figures

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.87
- Readability: 0.87
- Glossary consistency: 0.87
- **Overall section score:** 0.87
