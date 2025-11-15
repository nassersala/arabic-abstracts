# Section 8: Conclusion
## القسم 8: الخاتمة

**Section:** conclusion
**Translation Quality:** 0.88
**Glossary Terms Used:** quantum algorithm, combinatorial optimization, objective function, computational basis, classical preprocessing, quantum circuit

---

### English Version

We introduced a quantum algorithm for approximate combinatorial optimization that depends on an integer parameter p. The input is an n bit instance with an objective function C that is the sum of m local terms. The goal is to find a string z for which C(z) is close to C's global maximum. In the basic algorithm, each call to the quantum computer uses a set of 2p angles (γ, β) and produces the state

$$|γ, β⟩ = U(B, β_p) U(C, γ_p) \cdots U(B, β_1) U(C, γ_1) |s⟩$$

This is followed by a measurement in the computational basis yielding a string z with an associated value C(z). Repeated calls to the quantum computer will yield a good estimate of

$$F_p(γ, β) = ⟨γ, β| C |γ, β⟩$$

Running the algorithm requires a strategy for a picking a sequence of sets of angles with the goal of making $F_p$ as big as possible. We give several possible strategies for finding a good set of angles.

In section II we focused on fixed p and the case where each bit is in no more than a fixed number of clauses. In this case there is an efficient classical algorithm that determines the best set of angles which is then fed to the quantum computer. Here the quantum computer is run with only the best set of angles. Note that the "efficient" classical algorithm which evaluates (25) using (24) could require space doubly exponential in p.

An alternative to using a classical preprocessor to find the best angles is to make repeated calls to the quantum computer with different sets of angles. One strategy, when p does not grow with n is to put a fine grid on the compact set $[0, 2π]^p × [0, π]^p$ where the number of points is only polynomial in n and m. This works because the function $F_p$ does not have peaks that are so narrow that they are not seen by the grid.

The QAOA can be run on a quantum computer with p growing with n as long as there is a strategy for choosing sets of angles. Perhaps for some combinatorial optimization problem, good angles can be discovered in advance. Or the quantum computer can be called to evaluate $F_p(γ, β)$, the expectation of C in the state $|γ, β⟩$. This call can be used as a subroutine by a classical algorithm that seeks the maximum of the smooth function $F_p(γ, β)$.

We hope that either p fixed or growing slowly with n will be enough to have this quantum algorithm be of use in finding solutions to combinatorial search problems beyond what classical algorithms can achieve.

---

### النسخة العربية

قدمنا خوارزمية كمومية للتحسين التجميعي التقريبي تعتمد على معامل صحيح p. المدخل هو مثال n بت بدالة هدفية C هي مجموع m حداً موضعياً. الهدف هو إيجاد سلسلة z بحيث يكون C(z) قريباً من القيمة العظمى العامة لـ C. في الخوارزمية الأساسية، تستخدم كل استدعاء للحاسوب الكمومي مجموعة من 2p زاوية (γ, β) وتنتج الحالة:

$$|γ, β⟩ = U(B, β_p) U(C, γ_p) \cdots U(B, β_1) U(C, γ_1) |s⟩$$

يتبع هذا قياس في الأساس الحسابي ينتج سلسلة z بقيمة مرتبطة C(z). ستنتج استدعاءات متكررة للحاسوب الكمومي تقديراً جيداً لـ:

$$F_p(γ, β) = ⟨γ, β| C |γ, β⟩$$

يتطلب تشغيل الخوارزمية استراتيجية لاختيار تسلسل من مجموعات الزوايا بهدف جعل $F_p$ كبيرة قدر الإمكان. نقدم عدة استراتيجيات ممكنة لإيجاد مجموعة جيدة من الزوايا.

في القسم II ركزنا على p الثابت والحالة التي يكون فيها كل بت في ما لا يزيد عن عدد ثابت من الجمل. في هذه الحالة توجد خوارزمية تقليدية فعالة تحدد أفضل مجموعة من الزوايا التي تُغذى بعد ذلك إلى الحاسوب الكمومي. هنا يُشغَّل الحاسوب الكمومي بأفضل مجموعة من الزوايا فقط. لاحظ أن الخوارزمية التقليدية "الفعالة" التي تحسب (25) باستخدام (24) قد تتطلب مساحة أسية مضاعفة في p.

بديل لاستخدام معالج مسبق تقليدي لإيجاد أفضل الزوايا هو إجراء استدعاءات متكررة للحاسوب الكمومي بمجموعات مختلفة من الزوايا. إحدى الاستراتيجيات، عندما لا ينمو p مع n، هي وضع شبكة دقيقة على المجموعة المدمجة $[0, 2π]^p × [0, π]^p$ حيث عدد النقاط متعدد حدود فقط في n و m. هذا يعمل لأن الدالة $F_p$ ليس لها قمم ضيقة جداً بحيث لا تُرى بالشبكة.

يمكن تشغيل QAOA على حاسوب كمومي مع p ينمو مع n طالما توجد استراتيجية لاختيار مجموعات الزوايا. ربما لبعض مسائل التحسين التجميعي، يمكن اكتشاف زوايا جيدة مسبقاً. أو يمكن استدعاء الحاسوب الكمومي لحساب $F_p(γ, β)$، توقع C في الحالة $|γ, β⟩$. يمكن استخدام هذا الاستدعاء كبرنامج فرعي بواسطة خوارزمية تقليدية تبحث عن القيمة العظمى للدالة الناعمة $F_p(γ, β)$.

نأمل أن يكون p ثابتاً أو ينمو ببطء مع n كافياً لجعل هذه الخوارزمية الكمومية مفيدة في إيجاد حلول لمسائل البحث التجميعي بما يتجاوز ما يمكن أن تحققه الخوارزميات التقليدية.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** smooth function (دالة ناعمة), compact set (مجموعة مدمجة), polynomial (متعدد حدود)
- **Equations:** 2 key equations summarizing the algorithm
- **Citations:** Reference to Section II
- **Special handling:** Summary of main contributions; discussion of strategies; future outlook

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.88
- Glossary consistency: 0.87
- **Overall section score:** 0.88
