# Section 2: Background and Terminology
## القسم 2: الخلفية والمصطلحات

**Section:** background
**Translation Quality:** 0.88
**Glossary Terms Used:** formal methods, model checking, specification, temporal logic, counterexample, Kripke structure, Linear Temporal Logic (LTL), theorem provers, refinement, contract-based design

---

### English Version

In this section, we introduce the background and terminology of formal methods, model checking, contract-based design, which are relevant for our studies.

**Formal methods.** By formal methods we refer to models, e.g., SysML (Friedenthal et al. 2014), and Kripke structures used as input to verification tools (McMillan 1999), formal specifications of requirements, e.g., expressed in natural language-like statements using property specification patterns (Dwyer et al. 1999), or directly in a temporal logic such as Linear Temporal Logic (LTL) (Pnueli 1977), and to automated tools to perform the verification. Examples of such tools are model checkers, e.g., NuSMV (Cimatti et al. 2000), theorem provers, e.g., Isabelle (Paulson 1994), and solvers, e.g., Z3 (de Moura and Bjørner 2008).

**Model checking.** Considering the verification as a model checking problem, a specification is expressed in a temporal logic (φ) and a system is modeled as a Kripke structure (K). Both are the input for a model checker. The model checker verifies whether the given system model (K) satisfies the given property or specification (φ), that is, K ⊨ φ (Baier and Katoen 2008; Clarke et al. 2018a). If φ is not satisfied by K, the model checker generates a counterexample describing an execution path in K that leads from the initial system state to a state that violates φ, where each state consists of system variables with their values. Based on the counterexample, a user can manually localize the fault in K that causes the violation of φ.

**Contract-based design.** Contract-based design (CBD) (Cimatti and Tonetta 2012; Kaiser et al. 2015) supports the automated verification of refinement consistency and correctness. In CBD, model checking is used to identify whether the top-level requirements of a system are consistently refined along the refinement of the system to components. Each component of a system is associated with a contract that precisely specifies the expected behavior of the component by assumptions, and the provided behavior by guarantees. If a component is refined to sub-components, its contract is also refined and assigned to its sub-components. Thus, all of the sub-components should satisfy the expected behavior of the parent component. This corresponds to the correctness of the refined contracts and can be verified by model checking, which is known as the refinement check (Cimatti and Tonetta 2012).

---

### النسخة العربية

في هذا القسم، نقدم الخلفية والمصطلحات الخاصة بالأساليب الرسمية، وفحص النماذج، والتصميم القائم على العقود، والتي تُعد ذات صلة بدراساتنا.

**الأساليب الرسمية.** بالأساليب الرسمية نشير إلى النماذج، مثل SysML (فريدنثال وآخرون 2014)، وبُنى كريبكي المُستخدمة كمدخلات لأدوات التحقق (ماكميلان 1999)، والمواصفات الرسمية للمتطلبات، على سبيل المثال، المُعبر عنها في عبارات تشبه اللغة الطبيعية باستخدام أنماط مواصفات الخصائص (دواير وآخرون 1999)، أو مباشرة في منطق زمني مثل المنطق الزمني الخطي (LTL) (بنويلي 1977)، وإلى الأدوات الآلية لإجراء التحقق. أمثلة على هذه الأدوات هي فاحصات النماذج، مثل NuSMV (سيماتي وآخرون 2000)، ومُبرهنات النظريات، مثل Isabelle (بولسون 1994)، والحلالات، مثل Z3 (دي مورا وبيورنر 2008).

**فحص النماذج.** باعتبار التحقق مسألة فحص نماذج، يتم التعبير عن المواصفة في منطق زمني (φ) ويتم نمذجة النظام كبنية كريبكي (K). كلاهما يُعد مدخلاً لفاحص النماذج. يتحقق فاحص النماذج مما إذا كان نموذج النظام المُعطى (K) يُحقق الخاصية أو المواصفة المُعطاة (φ)، أي K ⊨ φ (باير وكاتوين 2008؛ كلارك وآخرون 2018a). إذا لم يُحقق K المواصفة φ، يولد فاحص النماذج مثالاً مضاداً يصف مساراً تنفيذياً في K يؤدي من حالة النظام الأولية إلى حالة تنتهك φ، حيث تتكون كل حالة من متغيرات النظام بقيمها. بناءً على المثال المضاد، يمكن للمستخدم تحديد الخلل يدوياً في K الذي يتسبب في انتهاك φ.

**التصميم القائم على العقود.** التصميم القائم على العقود (CBD) (سيماتي وتونيتا 2012؛ كايزر وآخرون 2015) يدعم التحقق الآلي من اتساق التحسين والصحة. في CBD، يُستخدم فحص النماذج لتحديد ما إذا كانت المتطلبات على المستوى الأعلى للنظام مُحسّنة بشكل متسق على طول تحسين النظام إلى مكونات. كل مكون من مكونات النظام مرتبط بعقد يحدد بدقة السلوك المتوقع للمكون من خلال الافتراضات، والسلوك المُقدم من خلال الضمانات. إذا تم تحسين مكون إلى مكونات فرعية، فإن عقده يُحسّن أيضاً ويُعيّن لمكوناته الفرعية. وبالتالي، يجب أن تُحقق جميع المكونات الفرعية السلوك المتوقع للمكون الأب. وهذا يتوافق مع صحة العقود المُحسّنة ويمكن التحقق منها بواسطة فحص النماذج، والذي يُعرف بفحص التحسين (سيماتي وتونيتا 2012).

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - SysML = SysML (نموذج لغة الأنظمة)
  - Kripke structure = بنية كريبكي
  - property specification patterns = أنماط مواصفات الخصائص
  - Linear Temporal Logic (LTL) = المنطق الزمني الخطي
  - theorem provers = مُبرهنات النظريات
  - solvers = الحلالات
  - Contract-based design (CBD) = التصميم القائم على العقود
  - assumptions = الافتراضات
  - guarantees = الضمانات
  - refinement check = فحص التحسين
  - execution path = مسار تنفيذي

- **Equations:** K ⊨ φ (satisfaction relation preserved in Arabic)
- **Citations:** 10 references cited
- **Special handling:**
  - Preserved formal notation (K, φ, ⊨) as used in formal methods literature
  - Tool names (NuSMV, Isabelle, Z3, SysML) kept in English as is standard practice
  - Maintained precise technical definitions critical for formal methods

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.88
