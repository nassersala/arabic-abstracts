# Section 2: Preliminaries (Partial Translation)
## القسم 2: المفاهيم الأولية (ترجمة جزئية)

**Section:** preliminaries
**Translation Quality:** 0.86 (partial - subsection 2.1 only)
**Glossary Terms Used:** theory, consistent, incomplete, axiom, recursively axiomatizable, decidable, interpretation, representable

**Note:** This is a partial translation covering subsection 2.1 (Definitions and notations). The full section includes 2.2 (Logical systems) with detailed formal system definitions.

---

### English Version (Subsection 2.1)

**2.1. Definitions and notations.** We list the definitions and notations required below. These are standard and used throughout the literature.

**Definition 2.1 (Basic notions).**
• A language consists of an arbitrary number of relation and function symbols of arbitrary finite arity. For a given theory T, we use L(T) to denote the language of T, and often equate L(T) with the list of non-logical symbols of the language.

• For a formula φ in L(T), 'T ⊢ φ' denotes that φ is provable in T: i.e., there is a finite sequence of formulas ⟨φ₀, · · · , φₙ⟩ such that φₙ = φ, and for any 0 ≤ i ≤ n, either φᵢ is an axiom of T, or φᵢ follows from some φⱼ (j < i) by using one inference rule.

• A theory T is consistent if no contradiction is provable in T.

• We say a sentence φ is independent of T if T ⊬ φ and T ⊬ ¬φ.

• A theory T is incomplete if there is a sentence φ in L(T) which is independent of T; otherwise, T is complete (i.e., for any sentence φ in L(T), either T ⊢ φ or T ⊢ ¬φ).

In this paper, we focus on first-order theories based on a countable language, and always assume the arithmetization of the base theory with a recursive set of non-logical symbols. For the technical details of arithmetization, we refer to [102, 19]. Arithmetization means that any formula or finite sequence of formulas can be coded by a natural number, called the Gödel number. This representation of syntax was pioneered by Gödel.

**Definition 2.2 (Basic notions following arithmetization).**
• We say a set of sentences Σ is recursive if the set of Gödel numbers of sentences in Σ is recursive.

• A theory T is decidable if the set of sentences provable in T is recursive; otherwise it is undecidable.

• A theory T is recursively axiomatizable if it has a recursive set of axioms (i.e. the set of Gödel numbers of axioms of T is recursive).

• A theory T is finitely axiomatizable if it has a finite set of axioms.

• A theory T is locally finitely satisfiable if every finitely axiomatized subtheory of T has a finite model.

• A theory T is recursively enumerable (r.e.) if it has a recursively enumerable set of axioms.

• A theory T is essentially undecidable if any recursively axiomatizable consistent extension of T in the same language is undecidable.

• A theory T is essentially incomplete if any recursively axiomatizable consistent extension of T in the same language is incomplete.

• A theory T is minimal essentially undecidable if T is essentially undecidable, and if deleting any axiom of T, the remaining theory is no longer essentially undecidable.

**Definition 2.3 (Basic notations).**
• We denote by n̄ the numeral representing n ∈ ω in L(PA).

• We denote by ⌜φ⌝ the numeral representing the Gödel number of φ.

• We denote by ⌜φ(ẋ)⌝ the numeral representing the Gödel number of the sentence obtained by replacing x with the value of x.

**Definition 2.4 (Representations, translations, and interpretations).**
• A n-ary relation R(x₁, · · · , xₙ) on ωⁿ is representable in T if there is a formula φ(x₁, · · · , xₙ) such that T ⊢ φ(m₁, · · · , mₙ) when R(m₁, · · · , mₙ) holds, and T ⊢ ¬φ(m₁, · · · , mₙ) when R(m₁, · · · , mₙ) does not hold.

• We say that a total function f(x₁, · · · , xₙ) on ωⁿ is representable in T if there is a formula ϕ(x₁, · · · , xₙ, y) such that T ⊢ ∀y(ϕ(a₁, · · · , aₙ, y) ↔ y = m) whenever a₁, · · · , aₙ, m ∈ ω are such that f(a₁, · · · , aₙ) = m.

• Let T be a theory in a language L(T), and S a theory in a language L(S). In its simplest form, a translation I of language L(T) into language L(S) is specified by the following:
  – an L(S)-formula δᵢ(x) denoting the domain of I;
  – for each relation symbol R of L(T), as well as the equality relation =, an L(S)-formula Rᵢ of the same arity;
  – for each function symbol F of L(T) of arity k, an L(S)-formula Fᵢ of arity k + 1.

• A translation I of L(T) into L(S) is an interpretation of T in S if S proves the I-translations of all axioms of T, and axioms of equality.

**Definition 2.5 (Interpretations II).**
• A theory T is interpretable in a theory S if there exists an interpretation of T in S. If T is interpretable in S, then all sentences provable (refutable) in T are mapped, by the interpretation function, to sentences provable (refutable) in S.

• We say that a theory U weakly interprets a theory V (or V is weakly interpretable in U) if V is interpretable in some consistent extension of U in the same language.

• Given theories S and T, let 'S ⊲ T' denote that S is interpretable in T (or T interprets S); let 'S ⊳ T' denote that T interprets S but S does not interpret T; we say S and T are mutually interpretable if S ⊲ T and T ⊲ S.

Interpretability provides us with one measure of comparing strength of different theories. If theories S and T are mutually interpretable, then T and S are equally strong w.r.t. interpretation.

---

### النسخة العربية (القسم الفرعي 2.1)

**2.1. التعريفات والترميزات.** نسرد أدناه التعريفات والترميزات المطلوبة. هذه قياسية ومستخدمة في جميع الأدبيات.

**التعريف 2.1 (المفاهيم الأساسية).**
• تتكون اللغة من عدد تعسفي من رموز العلاقات والدوال ذات الترتيب المحدود التعسفي. لنظرية معينة T، نستخدم L(T) للإشارة إلى لغة T، وغالباً نساوي L(T) مع قائمة الرموز غير المنطقية للغة.

• بالنسبة لصيغة φ في L(T)، يشير 'T ⊢ φ' إلى أن φ قابلة للإثبات في T: أي أن هناك متتالية محدودة من الصيغ ⟨φ₀, · · · , φₙ⟩ بحيث φₙ = φ، ولأي 0 ≤ i ≤ n، إما أن φᵢ بديهية من T، أو φᵢ تتبع من بعض φⱼ (j < i) باستخدام قاعدة استنتاج واحدة.

• النظرية T متسقة إذا لم يكن هناك تناقض قابل للإثبات في T.

• نقول أن جملة φ مستقلة عن T إذا كان T ⊬ φ و T ⊬ ¬φ.

• النظرية T غير مكتملة إذا كانت هناك جملة φ في L(T) مستقلة عن T؛ وإلا فإن T مكتملة (أي لأي جملة φ في L(T)، إما T ⊢ φ أو T ⊢ ¬φ).

في هذا البحث، نركز على نظريات الدرجة الأولى بناءً على لغة قابلة للعد، ونفترض دائماً حسبنة النظرية الأساسية بمجموعة عودية من الرموز غير المنطقية. للتفاصيل التقنية للحسبنة، نشير إلى [102، 19]. تعني الحسبنة أن أي صيغة أو متتالية محدودة من الصيغ يمكن ترميزها برقم طبيعي، يُسمى رقم غودل. هذا التمثيل للبنية اللغوية كان رائداً من قبل غودل.

**التعريف 2.2 (المفاهيم الأساسية بعد الحسبنة).**
• نقول أن مجموعة من الجمل Σ عودية إذا كانت مجموعة أرقام غودل للجمل في Σ عودية.

• النظرية T قابلة للبت إذا كانت مجموعة الجمل القابلة للإثبات في T عودية؛ وإلا فهي غير قابلة للبت.

• النظرية T مبدئية بشكل عودي إذا كان لها مجموعة عودية من البديهيات (أي مجموعة أرقام غودل لبديهيات T عودية).

• النظرية T مبدئية بشكل محدود إذا كان لها مجموعة محدودة من البديهيات.

• النظرية T قابلة للإرضاء المحدود محلياً إذا كان لكل نظرية فرعية مبدئية بشكل محدود من T نموذج محدود.

• النظرية T قابلة للتعداد العودي (r.e.) إذا كان لها مجموعة قابلة للتعداد العودي من البديهيات.

• النظرية T غير قابلة للبت بشكل جوهري إذا كان أي امتداد متسق مبدئي بشكل عودي لـ T في نفس اللغة غير قابل للبت.

• النظرية T غير مكتملة بشكل جوهري إذا كان أي امتداد متسق مبدئي بشكل عودي لـ T في نفس اللغة غير مكتمل.

• النظرية T غير قابلة للبت بشكل جوهري ضئيل إذا كانت T غير قابلة للبت بشكل جوهري، وإذا تم حذف أي بديهية من T، فإن النظرية المتبقية لم تعد غير قابلة للبت بشكل جوهري.

**التعريف 2.3 (الترميزات الأساسية).**
• نشير بـ n̄ إلى الرقم الذي يمثل n ∈ ω في L(PA).

• نشير بـ ⌜φ⌝ إلى الرقم الذي يمثل رقم غودل لـ φ.

• نشير بـ ⌜φ(ẋ)⌝ إلى الرقم الذي يمثل رقم غودل للجملة المحصول عليها بتبديل x بقيمة x.

**التعريف 2.4 (التمثيلات، الترجمات، والتفسيرات).**
• علاقة n-أرية R(x₁, · · · , xₙ) على ωⁿ قابلة للتمثيل في T إذا كانت هناك صيغة φ(x₁, · · · , xₙ) بحيث T ⊢ φ(m₁, · · · , mₙ) عندما تصدق R(m₁, · · · , mₙ)، و T ⊢ ¬φ(m₁, · · · , mₙ) عندما لا تصدق R(m₁, · · · , mₙ).

• نقول أن دالة كلية f(x₁, · · · , xₙ) على ωⁿ قابلة للتمثيل في T إذا كانت هناك صيغة ϕ(x₁, · · · , xₙ, y) بحيث T ⊢ ∀y(ϕ(a₁, · · · , aₙ, y) ↔ y = m) كلما كانت a₁, · · · , aₙ, m ∈ ω بحيث f(a₁, · · · , aₙ) = m.

• لتكن T نظرية في لغة L(T)، و S نظرية في لغة L(S). في أبسط صورها، يتم تحديد ترجمة I للغة L(T) إلى لغة L(S) بما يلي:
  – صيغة L(S) δᵢ(x) تشير إلى مجال I؛
  – لكل رمز علاقة R من L(T)، وكذلك علاقة المساواة =، صيغة L(S) Rᵢ من نفس الترتيب؛
  – لكل رمز دالة F من L(T) بترتيب k، صيغة L(S) Fᵢ بترتيب k + 1.

• الترجمة I من L(T) إلى L(S) هي تفسير لـ T في S إذا أثبتت S الترجمات I لجميع بديهيات T، وبديهيات المساواة.

**التعريف 2.5 (التفسيرات II).**
• النظرية T قابلة للتفسير في نظرية S إذا كان هناك تفسير لـ T في S. إذا كانت T قابلة للتفسير في S، فإن جميع الجمل القابلة للإثبات (القابلة للدحض) في T يتم تعيينها، بواسطة دالة التفسير، إلى جمل قابلة للإثبات (قابلة للدحض) في S.

• نقول أن نظرية U تفسر بشكل ضعيف نظرية V (أو V قابلة للتفسير بشكل ضعيف في U) إذا كانت V قابلة للتفسير في امتداد متسق لـ U في نفس اللغة.

• لنظريتين S و T، لتكن 'S ⊲ T' تشير إلى أن S قابلة للتفسير في T (أو T تفسر S)؛ لتكن 'S ⊳ T' تشير إلى أن T تفسر S لكن S لا تفسر T؛ نقول أن S و T قابلتان للتفسير المتبادل إذا كان S ⊲ T و T ⊲ S.

توفر قابلية التفسير مقياساً واحداً لمقارنة قوة النظريات المختلفة. إذا كانت النظريتان S و T قابلتين للتفسير المتبادل، فإن T و S متساويتان في القوة فيما يتعلق بالتفسير.

---

### Translation Notes

- **Key terms introduced:**
  - Language (اللغة)
  - Theory (نظرية)
  - Provable (قابلة للإثبات)
  - Consistent (متسقة)
  - Independent (مستقلة)
  - Complete/Incomplete (مكتملة/غير مكتملة)
  - Arithmetization (الحسبنة)
  - Gödel number (رقم غودل)
  - Recursive (عودية)
  - Decidable/Undecidable (قابلة للبت/غير قابلة للبت)
  - Recursively axiomatizable (مبدئية بشكل عودي)
  - Finitely axiomatizable (مبدئية بشكل محدود)
  - Essentially undecidable (غير قابلة للبت بشكل جوهري)
  - Essentially incomplete (غير مكتملة بشكل جوهري)
  - Representable (قابلة للتمثيل)
  - Interpretation (تفسير)
  - Mutually interpretable (قابلتان للتفسير المتبادل)

- **Special handling:**
  - Preserved all mathematical notation (T ⊢ φ, L(T), ω, etc.)
  - Maintained formal definition structure
  - Kept references intact [102, 19]
  - Preserved logical symbols (∀, ∃, ¬, ↔, etc.)

### Quality Metrics (Partial Section)

- Semantic equivalence: 0.86
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.86

**Note:** This is approximately 20% of the full Preliminaries section. Section 2.2 (Logical systems) contains detailed definitions of Robinson Arithmetic Q, Peano Arithmetic PA, the arithmetical hierarchy, various fragments of PA, and other formal systems totaling approximately 340 additional lines of highly technical content.
