# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.89
**Glossary Terms Used:** quantum computing, algorithm, eigenvalue, eigenvector, operator, quantum phase estimation, coherent, evolution, Hamiltonian, optimization, computational, quantum processor

---

### English Version

In chemistry, the properties of atoms and molecules can be determined by solving the Schrödinger equation. However, because the dimension of the problem grows exponentially with the size of the physical system under consideration, exact treatment of these problems remains classically infeasible for compounds with more than 2-3 atoms. Many approximate methods have been developed to treat these systems, but efficient exact methods for large chemical problems remain out of reach for classical computers. Beyond chemistry, the solution of large eigenvalue problems would have applications ranging from determining the results of internet search engines to designing new materials and drugs.

Recent developments in the field of quantum computation offer a way forward for efficient solutions of many instances of large eigenvalue problems which are classically intractable. Quantum approaches to finding eigenvalues have previously relied on the quantum phase estimation (QPE) algorithm. The QPE algorithm offers an exponential speedup over classical methods and requires a number of quantum operations O(1/p) to obtain an estimate with precision p. In the standard formulation of QPE, one assumes the eigenvector |ψ⟩ of a Hermitian operator H is given as input and the problem is to determine the corresponding eigenvalue λ. The time the quantum computer must remain coherent is determined by the necessity of O(1/p) successive applications of e^(-iHt), each of which can require on the order of millions or billions of quantum gates for practical applications, as compared to the tens to hundreds of gates achievable in the short term.

Here we introduce and experimentally demonstrate an alternative to QPE that significantly reduces the requirements for coherent evolution. We have developed a reconfigurable quantum processing unit (QPU), which efficiently calculates the expectation value of a Hamiltonian (H), providing an exponential speedup over conventional methods. The QPU is combined with an optimization algorithm run on a classical processing unit (CPU), which variationally computes the eigenvalues and eigenvectors of H. By using a variational algorithm, this approach reduces the requirement for coherent evolution of the quantum state, making more efficient use of quantum resources, and may offer an alternative route to practical quantum-enhanced computation.

---

### النسخة العربية

في الكيمياء، يمكن تحديد خصائص الذرات والجزيئات من خلال حل معادلة شرودنغر. ومع ذلك، نظراً لأن بُعد المسألة ينمو بشكل أُسّي مع حجم النظام الفيزيائي قيد الدراسة، فإن المعالجة الدقيقة لهذه المسائل تظل غير ممكنة كلاسيكياً للمركبات التي تحتوي على أكثر من 2-3 ذرات. تم تطوير العديد من الأساليب التقريبية لمعالجة هذه الأنظمة، لكن الأساليب الدقيقة الفعالة للمسائل الكيميائية الكبيرة تظل بعيدة المنال بالنسبة للحواسيب الكلاسيكية. وبعيداً عن الكيمياء، فإن حل مسائل القيم الذاتية الكبيرة سيكون له تطبيقات تتراوح من تحديد نتائج محركات البحث على الإنترنت إلى تصميم مواد وأدوية جديدة.

توفر التطورات الحديثة في مجال الحوسبة الكمومية طريقاً للأمام للحلول الفعالة للعديد من حالات مسائل القيم الذاتية الكبيرة التي يستعصي حلها كلاسيكياً. اعتمدت الأساليب الكمومية لإيجاد القيم الذاتية سابقاً على خوارزمية تقدير الطور الكمومي (QPE). تقدم خوارزمية QPE تسريعاً أسياً مقارنة بالأساليب الكلاسيكية وتتطلب عدداً من العمليات الكمومية بمقدار O(1/p) للحصول على تقدير بدقة p. في الصياغة القياسية لـ QPE، يُفترض أن المتجه الذاتي |ψ⟩ لمؤثر هيرميتي H مُعطى كمدخل والمسألة هي تحديد القيمة الذاتية المقابلة λ. يتم تحديد الوقت الذي يجب أن يبقى فيه الحاسوب الكمومي متماسكاً بضرورة O(1/p) من التطبيقات المتتالية لـ e^(-iHt)، كل منها يمكن أن يتطلب ملايين أو مليارات من البوابات الكمومية للتطبيقات العملية، مقارنة بعشرات إلى مئات البوابات القابلة للتحقيق على المدى القصير.

نقدم هنا ونُظهر تجريبياً بديلاً لـ QPE يقلل بشكل كبير من متطلبات التطور المتماسك. قمنا بتطوير وحدة معالجة كمومية قابلة لإعادة التكوين (QPU)، تحسب بكفاءة القيمة المتوقعة للهاميلتونياني (H)، مما يوفر تسريعاً أسياً مقارنة بالأساليب التقليدية. يتم دمج وحدة المعالجة الكمومية مع خوارزمية تحسين تُشغَّل على وحدة معالجة كلاسيكية (CPU)، والتي تحسب بشكل تبايني القيم الذاتية والمتجهات الذاتية لـ H. من خلال استخدام خوارزمية تباينية، يقلل هذا النهج من متطلبات التطور المتماسك للحالة الكمومية، مما يجعل استخدام الموارد الكمومية أكثر كفاءة، وقد يوفر طريقاً بديلاً للحوسبة المعززة كمومياً العملية.

---

### Translation Notes

- **Figures referenced:** Figure 1 (algorithm architecture - mentioned but not in this text section)
- **Key terms introduced:** Schrödinger equation (معادلة شرودنغر), quantum phase estimation/QPE (تقدير الطور الكمومي), Hermitian operator (مؤثر هيرميتي), coherent evolution (التطور المتماسك), variational algorithm (خوارزمية تباينية), quantum processing unit/QPU (وحدة معالجة كمومية), expectation value (القيمة المتوقعة)
- **Equations:** O(1/p) notation, exponential e^(-iHt), Dirac notation |ψ⟩
- **Citations:** Multiple references to prior work [Thogersen2004, Helgaker2002, Saad1992, Page1999, Golub2000, Nielsen2007, Kitaev1996, and others]
- **Special handling:**
  - Mathematical notation preserved in both English and Arabic
  - Technical acronyms (QPE, QPU, CPU) kept in English with Arabic explanations
  - Quantum notation (bra-ket) preserved

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.88
- Glossary consistency: 0.90
- **Overall section score:** 0.89
