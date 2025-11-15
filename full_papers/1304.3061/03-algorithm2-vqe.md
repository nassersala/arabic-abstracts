# Section 3: Algorithm 2 - Quantum Variational Eigensolver
## القسم 3: الخوارزمية 2 - الحلّال التبايني للقيم الذاتية الكمومية

**Section:** algorithm-2-vqe
**Translation Quality:** 0.88
**Glossary Terms Used:** algorithm, ground state, eigenstate, eigenvalue, eigenvector, wavefunction, adiabatic evolution, variational, optimization, ansatz, unitary coupled cluster, Hartree-Fock, quantum chemistry

---

### English Version

**Algorithm 2: Quantum variational eigensolver**

The procedure outlined above replaces the long coherent evolution required by QPE by many short coherent evolutions. In both QPE and Algorithm 1 we require a good approximation to the ground state wavefunction to compute the ground state eigenvalue and we now consider this problem. Previous approaches have proposed to prepare ground states by adiabatic evolution, or by the quantum metropolis algorithm. Unfortunately both of these require long coherent evolution.

Algorithm 2 is a variational method to prepare the eigenstate and, by exploiting Algorithm 1, requires short coherent evolution. Algorithm 1 and 2 and their relationship are shown in Fig. 1 and detailed in the Appendix.

It is well known that the eigenvalue problem for an observable represented by an operator H can be restated as a variational problem on the Rayleigh-Ritz quotient, such that the eigenvector |ψ⟩ corresponding to the lowest eigenvalue is the |ψ⟩ that minimizes:

$$\frac{\langle\psi|H|\psi\rangle}{\langle\psi|\psi\rangle}$$

By varying the experimental parameters in the preparation of |ψ⟩ and computing the Rayleigh-Ritz quotient using Algorithm 1 as a subroutine in a classical minimization, one may prepare unknown eigenvectors. At the termination of the algorithm, a simple prescription for the reconstruction of the eigenvector is stored in the final set of experimental parameters that define |ψ⟩.

If a quantum state is characterized by an exponentially large number of parameters, it cannot be prepared with a polynomial number of operations. The set of efficiently preparable states are therefore characterized by polynomially many parameters, and we choose a particular set of ansatz states of this type. Under these conditions, a classical search algorithm on the experimental parameters which define |ψ⟩, needs only explore a polynomial number of dimensions—a requirement for the search to be efficient.

One example of a quantum state parametrized by a polynomial number of parameters is the unitary coupled cluster ansatz:

$$|\Psi\rangle = e^{T - T^\dagger} |\Phi\rangle_{ref}$$

where T is the cluster operator (defined in the Appendix) and |Φ⟩_ref is some reference state, normally taken to be the Hartree-Fock ground state. There is currently no known efficient classical algorithm based on these ansatz states. However, non-unitary coupled cluster ansatz is sometimes referred to as the "gold standard of quantum chemistry" as it is the standard of accuracy to which other methods in quantum chemistry are often compared. The unitary version of this ansatz is thought to yield superior results to even this "gold standard". Details of efficient construction of the unitary coupled cluster state using a quantum device are given in the Appendix.

---

### النسخة العربية

**الخوارزمية 2: الحلّال التبايني للقيم الذاتية الكمومية**

يستبدل الإجراء الموضح أعلاه التطور المتماسك الطويل المطلوب بواسطة QPE بالعديد من التطورات المتماسكة القصيرة. في كل من QPE والخوارزمية 1، نحتاج إلى تقريب جيد للدالة الموجية للحالة الأساسية لحساب القيمة الذاتية للحالة الأساسية ونعتبر الآن هذه المشكلة. اقترحت الأساليب السابقة تحضير الحالات الأساسية من خلال التطور الأدياباتي، أو من خلال خوارزمية ميتروبوليس الكمومية. لسوء الحظ، يتطلب كلاهما تطوراً متماسكاً طويلاً.

الخوارزمية 2 هي طريقة تباينية لتحضير الحالة الذاتية، ومن خلال استغلال الخوارزمية 1، تتطلب تطوراً متماسكاً قصيراً. يتم عرض الخوارزميتين 1 و2 وعلاقتهما في الشكل 1 ويتم تفصيلهما في الملحق.

من المعروف أن مسألة القيمة الذاتية لمشاهَد ممثل بمؤثر H يمكن إعادة صياغتها كمسألة تباينية على حاصل رايلي-ريتز، بحيث أن المتجه الذاتي |ψ⟩ المقابل لأدنى قيمة ذاتية هو |ψ⟩ الذي يقلل:

$$\frac{\langle\psi|H|\psi\rangle}{\langle\psi|\psi\rangle}$$

من خلال تغيير المعاملات التجريبية في تحضير |ψ⟩ وحساب حاصل رايلي-ريتز باستخدام الخوارزمية 1 كإجراء فرعي في تقليل كلاسيكي، يمكن للمرء تحضير متجهات ذاتية غير معروفة. عند انتهاء الخوارزمية، يتم تخزين وصفة بسيطة لإعادة بناء المتجه الذاتي في المجموعة النهائية من المعاملات التجريبية التي تعرّف |ψ⟩.

إذا كانت حالة كمومية تتميز بعدد أسي كبير من المعاملات، فلا يمكن تحضيرها بعدد كثير حدود من العمليات. لذلك فإن مجموعة الحالات القابلة للتحضير بكفاءة تتميز بعدد كثير حدود من المعاملات، ونختار مجموعة معينة من حالات الأنزاتز من هذا النوع. في ظل هذه الظروف، تحتاج خوارزمية بحث كلاسيكية على المعاملات التجريبية التي تعرّف |ψ⟩ فقط إلى استكشاف عدد كثير حدود من الأبعاد - وهو شرط لكي يكون البحث فعالاً.

أحد الأمثلة على حالة كمومية مُعَلمَّة بعدد كثير حدود من المعاملات هو أنزاتز الكتلة المقترنة الوحدوية:

$$|\Psi\rangle = e^{T - T^\dagger} |\Phi\rangle_{ref}$$

حيث T هو مؤثر الكتلة (مُعرَّف في الملحق) و|Φ⟩_ref هي حالة مرجعية ما، تُأخذ عادة على أنها الحالة الأساسية لهارتري-فوك. لا توجد حالياً خوارزمية كلاسيكية فعالة معروفة تستند إلى حالات الأنزاتز هذه. ومع ذلك، يُشار أحياناً إلى أنزاتز الكتلة المقترنة غير الوحدوية باسم "المعيار الذهبي للكيمياء الكمومية" لأنها معيار الدقة الذي غالباً ما تُقارن به الأساليب الأخرى في الكيمياء الكمومية. يُعتقد أن النسخة الوحدوية من هذا الأنزاتز تُنتج نتائج متفوقة حتى على هذا "المعيار الذهبي". تُعطى تفاصيل البناء الفعال لحالة الكتلة المقترنة الوحدوية باستخدام جهاز كمومي في الملحق.

---

### Translation Notes

- **Figures referenced:**
  - Figure 1 (algorithm architecture)
  - Figure 3 (ground state optimization for He-H+)
- **Key terms introduced:**
  - Rayleigh-Ritz quotient (حاصل رايلي-ريتز)
  - Adiabatic evolution (التطور الأدياباتي)
  - Quantum Metropolis algorithm (خوارزمية ميتروبوليس الكمومية)
  - Ansatz/ans\"atze (أنزاتز - kept as transliteration, common in quantum chemistry)
  - Unitary coupled cluster (الكتلة المقترنة الوحدوية)
  - Cluster operator (مؤثر الكتلة)
  - Hartree-Fock (هارتري-فوك)
  - Gold standard (المعيار الذهبي)
  - Tangle (التشابك - measure of entanglement)
- **Equations:**
  - Rayleigh-Ritz quotient formula
  - Unitary coupled cluster ansatz formula
- **Citations:** References to Aspuru:2005, Yung03012012, Rayleigh:1870, Ritz:1908, Bartlett:2006, Yung:2013
- **Special handling:**
  - Proper names (Rayleigh, Ritz, Hartree, Fock) kept in English with Arabic transliteration
  - "Ansatz" kept as transliteration - standard practice in quantum chemistry literature
  - Mathematical expressions preserved exactly

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.87
- Glossary consistency: 0.89
- **Overall section score:** 0.88
