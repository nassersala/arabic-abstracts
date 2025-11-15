# Section 2: Algorithm 1 - Quantum Expectation Estimation
## القسم 2: الخوارزمية 1 - تقدير القيمة المتوقعة الكمومية

**Section:** algorithm-1-expectation-estimation
**Translation Quality:** 0.87
**Glossary Terms Used:** algorithm, quantum system, Hamiltonian, operator, expectation value, Pauli operator, tensor product, complexity, qubit, state, coherence time, polynomial, exponential

---

### English Version

**Algorithm 1: Quantum expectation estimation**

This algorithm computes the expectation value of a given Hamiltonian H for an input state |ψ⟩.

Any Hamiltonian may be written as:

$$H = \sum_{i\alpha} h^i_\alpha \sigma_\alpha^i + \sum_{ij\alpha\beta} h^{ij}_{\alpha \beta} \sigma_\alpha^i \sigma_\beta^j + \ldots$$

for real h where Roman indices identify the subspace on which the operator acts, and Greek indices identify the Pauli operator, e.g., α = x.

By exploiting the linearity of quantum observables, it follows that:

$$\langle H \rangle = \sum_{i\alpha} h^i_\alpha \langle \sigma_\alpha^i \rangle + \sum_{ij\alpha\beta} h^{ij}_{\alpha \beta} \langle \sigma_\alpha^i \sigma_\beta^j \rangle + \ldots$$

We consider Hamiltonians that can be written as a number of terms which is polynomial in the size of the system. This class of Hamiltonians encompasses a wide range of physical systems, including the electronic structure Hamiltonian of quantum chemistry, the quantum Ising Model, the Heisenberg Model, matrices that are well approximated as a sum of n-fold tensor products, and more generally any k-sparse Hamiltonian without evident tensor product structure (see Appendix for details).

Thus the evaluation of ⟨H⟩ reduces to the sum of a polynomial number of expectation values of simple Pauli operators for a quantum state |ψ⟩, multiplied by some real constants. A quantum device can efficiently evaluate the expectation value of a tensor product of an arbitrary number of simple Pauli operators, therefore with an n-qubit state we can efficiently evaluate the expectation value of this 2^n × 2^n Hamiltonian.

One might attempt this using a classical computer by separately optimizing all reduced states corresponding to the desired terms in the Hamiltonian, but this would suffer from the N-representability problem, which is known to be intractable for both classical and quantum computers (it is in the quantum complexity class QMA-Hard). The power of our approach derives from the fact that quantum hardware can store a global quantum state with exponentially fewer resources than required by classical hardware, and as a result the N-representability problem does not arise.

As the expectation value of a tensor product of an arbitrary number of Pauli operators can be measured in constant time and the spectrum of each of these operators is bounded, to obtain an estimate with precision p, our approach incurs a cost of O(|h|²/p²) repetitions.

Thus the total cost of computing the expectation value of a state |ψ⟩ is given by O(|h_max|² M/p²), where M is the number of terms in the decomposition of the Hamiltonian. The advantage of this approach is that the coherence time to make a single measurement after preparing the state is O(1). In essence, we dramatically reduce the coherence time requirement while maintaining an exponential advantage over the classical case, by adding a polynomial number of repetitions with respect to QPE.

---

### النسخة العربية

**الخوارزمية 1: تقدير القيمة المتوقعة الكمومية**

تحسب هذه الخوارزمية القيمة المتوقعة لهاميلتونياني H مُعطى لحالة مدخلة |ψ⟩.

يمكن كتابة أي هاميلتونياني على الشكل:

$$H = \sum_{i\alpha} h^i_\alpha \sigma_\alpha^i + \sum_{ij\alpha\beta} h^{ij}_{\alpha \beta} \sigma_\alpha^i \sigma_\beta^j + \ldots$$

لـ h حقيقية حيث تحدد المؤشرات اللاتينية الفضاء الجزئي الذي يعمل عليه المؤثر، وتحدد المؤشرات اليونانية مؤثر باولي، على سبيل المثال α = x.

من خلال استغلال خطية المشاهدات الكمومية، يتبع أن:

$$\langle H \rangle = \sum_{i\alpha} h^i_\alpha \langle \sigma_\alpha^i \rangle + \sum_{ij\alpha\beta} h^{ij}_{\alpha \beta} \langle \sigma_\alpha^i \sigma_\beta^j \rangle + \ldots$$

نعتبر الهاميلتونيانيات التي يمكن كتابتها كعدد من الحدود تكون كثيرة حدود في حجم النظام. تشمل هذه الفئة من الهاميلتونيانيات مجموعة واسعة من الأنظمة الفيزيائية، بما في ذلك هاميلتونياني البنية الإلكترونية في الكيمياء الكمومية، ونموذج إيسينغ الكمومي، ونموذج هايزنبرغ، والمصفوفات التي يتم تقريبها بشكل جيد كمجموع من الجداءات التنسورية n-أضعاف، وبشكل أعم أي هاميلتونياني k-متناثر دون بنية جداء تنسوري واضحة (انظر الملحق للتفاصيل).

وبالتالي يختزل تقييم ⟨H⟩ إلى مجموع عدد كثير حدود من القيم المتوقعة لمؤثرات باولي البسيطة لحالة كمومية |ψ⟩، مضروبة في بعض الثوابت الحقيقية. يمكن لجهاز كمومي تقييم القيمة المتوقعة للجداء التنسوري لعدد تعسفي من مؤثرات باولي البسيطة بكفاءة، وبالتالي مع حالة n-كيوبت يمكننا تقييم القيمة المتوقعة لهذا الهاميلتونياني 2^n × 2^n بكفاءة.

قد يحاول المرء ذلك باستخدام حاسوب كلاسيكي من خلال التحسين المنفصل لجميع الحالات المختزلة المقابلة للحدود المرغوبة في الهاميلتونياني، لكن هذا سيعاني من مشكلة قابلية التمثيل-N، والتي من المعروف أنها مستعصية على كل من الحواسيب الكلاسيكية والكمومية (فهي في صنف التعقيد الكمومي QMA-Hard). تنبع قوة نهجنا من حقيقة أن الأجهزة الكمومية يمكنها تخزين حالة كمومية شاملة بموارد أقل بشكل أسي مما تتطلبه الأجهزة الكلاسيكية، ونتيجة لذلك لا تظهر مشكلة قابلية التمثيل-N.

نظراً لأن القيمة المتوقعة للجداء التنسوري لعدد تعسفي من مؤثرات باولي يمكن قياسها في وقت ثابت وطيف كل من هذه المؤثرات محدود، للحصول على تقدير بدقة p، يتكبد نهجنا تكلفة O(|h|²/p²) من التكرارات.

وبالتالي فإن التكلفة الإجمالية لحساب القيمة المتوقعة لحالة |ψ⟩ تُعطى بـ O(|h_max|² M/p²)، حيث M هو عدد الحدود في تحليل الهاميلتونياني. ميزة هذا النهج هي أن زمن التماسك لإجراء قياس واحد بعد تحضير الحالة هو O(1). في جوهره، نقلل بشكل كبير من متطلبات زمن التماسك مع الحفاظ على ميزة أسية على الحالة الكلاسيكية، من خلال إضافة عدد كثير حدود من التكرارات فيما يتعلق بـ QPE.

---

### Translation Notes

- **Figures referenced:** Figure 2 (experimental implementation - mentioned in context)
- **Key terms introduced:**
  - Pauli operator (مؤثر باولي)
  - Tensor product (الجداء التنسوري)
  - N-representability problem (مشكلة قابلية التمثيل-N)
  - QMA-Hard (QMA-صعب - quantum complexity class)
  - Ising Model (نموذج إيسينغ)
  - Heisenberg Model (نموذج هايزنبرغ)
  - k-sparse Hamiltonian (هاميلتونياني k-متناثر)
  - Ground state (الحالة الأساسية)
- **Equations:** Multiple mathematical expressions with summation notation, Dirac notation, Big-O notation
- **Citations:** References to Lloyd:2002, Ma:2011, Oseledets:2010, Ortiz:2001, Liu:2007
- **Special handling:**
  - All mathematical notation preserved exactly
  - Complexity class "QMA-Hard" kept in English with transliteration
  - Matrix dimensions (2^n × 2^n) preserved

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87
