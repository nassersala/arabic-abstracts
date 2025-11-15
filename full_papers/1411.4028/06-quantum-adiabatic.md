# Section 6: Relation to the Quantum Adiabatic Algorithm
## القسم 6: العلاقة بالخوارزمية الكمومية الأديباتية

**Section:** discussion
**Translation Quality:** 0.86
**Glossary Terms Used:** Quantum Adiabatic Algorithm (QAA), optimization, Hamiltonian, eigenstate, Perron-Frobenius theorem, Trotterization, overlap, approximation ratio

---

### English Version

We are focused on finding a good approximate solution to an optimization problem whereas the Quantum Adiabatic Algorithm, QAA [2], is designed to find the optimal solution and will do so if the run time is long enough. Consider the time dependent Hamiltonian $H(t) = (1 - t/T)B + (t/T)C$. Note that the state $|s⟩$ is the highest energy eigenstate of B and we are seeking a high energy eigenstate of C. Starting in $|s⟩$ we could run the quantum adiabatic algorithm and if the run time T were long enough we would find the highest energy eigenstate of C. Because B has only non-negative off-diagonal elements, the Perron-Frobenius theorem implies that the difference in energies between the top state and the one below is greater than 0 for all $t < T$, so for sufficiently large T success is assured. A Trotterized approximation to the evolution consists of an alternation of the operators $U(C, γ)$ and $U(B, β)$ where the sum of the angles is the total run time. For a good approximation we want each γ and β to be small and for success we want a long run time so together these force p to be large. In other words, we can always find a p and a set of angles γ, β that make $F_p(γ, β)$ as close to $M_p$ as desired. With (9), this proves the assertion of (10).

The previous discussion shows that we can get a good approximate solution to an optimization problem by making p sufficiently large, perhaps exponentially large in n. But the QAA works by producing a state with a large overlap with the optimal string. In this sense (10), although correct, may be misleading. In fact on the ring of disagrees the state produced at p = 1, which gives a 3/4 approximation ratio, has an exponentially small overlap with the optimal strings.

We also know an example where the QAA fails and the QAOA succeeds. In this example (actually a minimization) the objective function is symmetric in the n bits and therefore depends only on the Hamming weight. The objective function is plotted in figure 1 of reference [3]. Since the beginning Hamiltonian is also symmetric the evolution takes place in a subspace of dimension $n + 1$ with a basis of states $|w⟩$ indexed by the Hamming weight. The example can be simulated and analyzed for large n. For subexponential run times, the QAA is trapped in a false minimum at $w = n$. The QAOA can be similarly simulated and analyzed. For large n, even with p = 1, there are values of $γ_1$ and $β_1$ such that the final state is concentrated near the true minimum at $w = 0$.

The Quantum Approximate Optimization Algorithm has the key feature that as p increases the approximation improves. We contrast this to the performance of the QAA. For realizations of the QAA there is a total run time T that also appears in the instantaneous Hamiltonian, $H(t) = \tilde{H}(t/T)$. We start in the ground state of $\tilde{H}(0)$ seeking the ground state of $\tilde{H}(1)$. As T goes to infinity the overlap of the evolved state with the desired state goes to 1. However the success probability is generally not a monotonic function of T. See figure 2 of reference [4] for an extreme example where the success probability is plotted as a function of T for a particular 20 qubit instance of Max2Sat. The probability rises and then drops dramatically, and the ultimate rise for large T is not seen for times that can be reasonably simulated. It may well be advantageous in designing strategies for the QAOA to use the fact that the approximation improves as p increases.

---

### النسخة العربية

نحن نركز على إيجاد حل تقريبي جيد لمسألة تحسين بينما الخوارزمية الكمومية الأديباتية، QAA [2]، مصممة لإيجاد الحل الأمثل وستفعل ذلك إذا كان وقت التشغيل طويلاً بما فيه الكفاية. لنفكر في الهاميلتونية المعتمدة على الزمن $H(t) = (1 - t/T)B + (t/T)C$. لاحظ أن الحالة $|s⟩$ هي الحالة الذاتية ذات الطاقة الأعلى لـ B ونحن نبحث عن حالة ذاتية ذات طاقة عالية لـ C. بدءاً من $|s⟩$ يمكننا تشغيل الخوارزمية الكمومية الأديباتية وإذا كان وقت التشغيل T طويلاً بما فيه الكفاية فسنجد الحالة الذاتية ذات الطاقة الأعلى لـ C. لأن B لها فقط عناصر خارج قطرية غير سالبة، فإن مبرهنة بيرون-فروبينيوس تعني أن الفرق في الطاقات بين الحالة العليا والتي تحتها أكبر من 0 لجميع $t < T$، لذا فإن النجاح مضمون لقيمة T كبيرة بما فيه الكفاية. التقريب المُتروتَر للتطور يتكون من تناوب المؤثرات $U(C, γ)$ و $U(B, β)$ حيث مجموع الزوايا هو وقت التشغيل الإجمالي. للحصول على تقريب جيد نريد أن يكون كل من γ و β صغيراً وللنجاح نريد وقت تشغيل طويل لذا معاً هذه تفرض أن تكون p كبيرة. بعبارة أخرى، يمكننا دائماً إيجاد p ومجموعة من الزوايا γ, β التي تجعل $F_p(γ, β)$ قريباً من $M_p$ كما نريد. مع (9)، هذا يثبت التأكيد في (10).

تُظهر المناقشة السابقة أنه يمكننا الحصول على حل تقريبي جيد لمسألة تحسين بجعل p كبيراً بما فيه الكفاية، ربما كبيراً أسياً في n. لكن QAA تعمل بإنتاج حالة لها تداخل كبير مع السلسلة الأمثل. بهذا المعنى، فإن (10)، رغم صحتها، قد تكون مضللة. في الواقع على حلقة عدم الاتفاقات فإن الحالة المنتجة عند p = 1، التي تعطي نسبة تقريب 3/4، لها تداخل صغير أسياً مع السلاسل الأمثل.

نعرف أيضاً مثالاً حيث تفشل QAA وتنجح QAOA. في هذا المثال (في الواقع تصغير) فإن الدالة الهدفية متماثلة في البتات n وبالتالي تعتمد فقط على وزن هامينج. الدالة الهدفية مرسومة في الشكل 1 من المرجع [3]. بما أن الهاميلتونية البدائية متماثلة أيضاً فإن التطور يحدث في فضاء جزئي ببُعد $n + 1$ مع أساس من الحالات $|w⟩$ مفهرسة بوزن هامينج. يمكن محاكاة المثال وتحليله لقيم n كبيرة. لأوقات تشغيل تحت أسية، فإن QAA محاصرة في حد أدنى زائف عند $w = n$. يمكن محاكاة QAOA وتحليلها بالمثل. لقيم n كبيرة، حتى مع p = 1، توجد قيم لـ $γ_1$ و $β_1$ بحيث تكون الحالة النهائية متركزة بالقرب من الحد الأدنى الحقيقي عند $w = 0$.

تتميز خوارزمية التحسين التقريبي الكمومية بأن التقريب يتحسن مع زيادة p. نقارن هذا بأداء QAA. لتحققات QAA يوجد وقت تشغيل إجمالي T يظهر أيضاً في الهاميلتونية اللحظية، $H(t) = \tilde{H}(t/T)$. نبدأ في الحالة الأرضية لـ $\tilde{H}(0)$ ونبحث عن الحالة الأرضية لـ $\tilde{H}(1)$. مع ذهاب T إلى ما لا نهاية فإن تداخل الحالة المتطورة مع الحالة المطلوبة يذهب إلى 1. لكن احتمالية النجاح عموماً ليست دالة رتيبة لـ T. انظر الشكل 2 من المرجع [4] لمثال متطرف حيث يُرسم احتمال النجاح كدالة لـ T لمثال معين من 20 كيوبت لـ Max2Sat. يرتفع الاحتمال ثم ينخفض بشكل كبير، والارتفاع النهائي لقيم T الكبيرة لا يُرى لأوقات يمكن محاكاتها بشكل معقول. قد يكون من المفيد جداً في تصميم استراتيجيات لـ QAOA استخدام حقيقة أن التقريب يتحسن مع زيادة p.

---

### Translation Notes

- **Figures referenced:** Figure 1 and Figure 2 from references [3] and [4]
- **Key terms introduced:** Quantum Adiabatic Algorithm (الخوارزمية الكمومية الأديباتية), Hamming weight (وزن هامينج), Perron-Frobenius theorem (مبرهنة بيرون-فروبينيوس), Trotterization (التروتر), overlap (تداخل), monotonic function (دالة رتيبة)
- **Equations:** Time-dependent Hamiltonian formulations
- **Citations:** References [2], [3], and [4]
- **Special handling:** Comparison between QAOA and QAA; discussion of advantages and limitations

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.86
