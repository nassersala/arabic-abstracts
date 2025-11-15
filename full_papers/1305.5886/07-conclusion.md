# Section 7: Conclusion and Future Trends
## القسم 7: الخلاصة والاتجاهات المستقبلية

**Section:** Conclusion and Future Trends
**Translation Quality:** 0.88
**Glossary Terms Used:** homomorphic encryption (تشفير متماثل), fully homomorphic encryption (تشفير متماثل كامل), lattice (شبكة بلورية)

---

### English Version

The study of fully homomorphic encryption has led to a number of new and exciting concepts and questions, as well as a powerful tool-kit to address them. We conclude the chapter by discussing a number of research directions related to the domain of fully homomorphic encryption and more generally, on the problem of computing on encrypted data.

**Applications of fully homomorphic encryption:** While Gentry's original construction was considered as being infeasible for practical deployments, recent constructions and implementation efforts have drastically improved the efficiency of fully homomorphic encryption (Vaikuntanathan, 2011). The initial implementation efforts focused on Gentry's original scheme and its variants (Smart & Vercauteren, 2010; Smart & Vercauteren, 2012; Coron et al., 2011; Gentry & Halevi, 2011), which seemed to pose rather inherent efficiency bottlenecks. Later implementations leverage the recent algorithmic advances (Brakerski & Vaikuntanathan, 2011; Brakerski et al., 2011; Brakerski & Vaikuntanathan, 2011a) that result in asymptotically better fully homomorphic encryption systems, as well as new algebraic mechanisms to improve the overall efficiency of these schemes (Naehrig et al., 2011; Gentry et al., 2012; Smart & Vercauteren, 2012).

**Non-malleability and homomorphic encryption:** Homomorphism and non-malleability are two orthogonal properties of an encryption scheme. Homomorphic encryption schemes permit anyone to transform an encryption of a message m into an encryption of f(m) for non-trivial functions f. Non-malleable encryption, on the other hand, prevents precisely this sort of thing- it requires that no adversary be able to transform an encryption of m into an encryption of any related message. Essentially, what we need is a combination of both the properties that selectively permit homomorphic computations (Vaikuntanathan, 2011). This implies that the evaluator should be able to homomorphically compute any function from some pre-specified class $F_{hom}$; however, she should not be able to transform an encryption of m into an encryption of f(m) for which $f \\notin F_{hom}$ does not hold good (i.e., f does not belong to $F_{hom}$). The natural question that arises is: whether we can control what is being (homomorphically) computed?

Answering this question turns out to be tricky. Boneh, Segev and Waters (Boneh et al., 2011) propose the notion of targeted malleability – a possible formalization of such a requirement as well as formal constructions of such encryption schemes. Their encryption scheme is based on a strong knowledge of exponent-type assumption that allows iterative evaluation of at most t functions, where t is a suitably determined and pre-specified constant. Improving their construction as well as the underlying complexity assumptions is an important open problem (Vaikuntanathan, 2011).

It is also interesting to extend the definition of non-malleability to allow for chosen cipher-text attacks. As an example, we consider the problem that involves implementing an encrypted targeted advertisement system that generates advertisements depending on the contents of a user's e-mail. Since the e-mail is stored in an encrypted form with the user's public key, the e-mail server performs a homomorphic evaluation and computes an encrypted advertisement to be sent back to the user. The user decrypts it, performs an action depending on what she sees. If the advertisement is relevant, she might choose to click on it; otherwise, she simply discards it. However, if the e-mail server is aware to this information, namely whether the user clicked on the advertisement or not, it can use this as a restricted decryption oracle to break the security of the user's encryption scheme and possibly even recover her secret key. Such attacks are ubiquitous whenever we compute on encrypted data, almost to the point that CCA security seems inevitable. Yet, it is easy to see that chosen ciphertext (CCA2-secure) homomorphic encryption schemes cannot exist. Therefore, an appropriate security definition and constructions that achieve the definition is in demand.

**Fully homomorphic encryption and functional decryption:** Homomorphic encryption schemes permit anyone to evaluate functions on encrypted data, but the evaluators never see any information about the result. It is possible to construct an encryption scheme where a user can compute f(m) from an encryption of a message m, but she should not be able to learn any other information about m (including the intermediate results in the computation of f)? Essentially, the issue boils down to the following question: can we control the information that the evaluator can see? Such an encryption scheme is called a functional encryption scheme. The concept of functional encryption scheme was first introduced by Sahai and Waters (Sahai & Waters, 2005) and subsequently investigated in a number of intriguing works (Katz et al., 2013; Lewko et al., 2010; Boneh et al., 2011; Agrawal et al., 2011). Although the constructions in these propositions work for several interesting families of functions (such as monotone formulas and inner products), construction of a fully functional encryption scheme is still not achieved and remains as an open problem. What we need is a novel and generic encryption system that provides us with fine-grained control over what one can see and access and what one can compute on data to get a desired output.

**Other problems and applications:** Another important open question relates to the assumptions underlying the current fully homomorphic encryption systems. All known fully homomorphic encryption schemes are based on hardness of lattice problems. The natural question that arises - can we construct fully homomorphic from other approaches – say, for example, from number-theoretic assumptions? Can we bring in the issue of the hardness of factoring or discrete logarithms in this problem?

In addition to the scenarios where it is beneficial to keep all data encrypted and to perform computations on encrypted data, fully homomorphic encryption can be gainfully exploited to solve a number of practical problems in cryptography. Two such examples are the problems of verifiably outsourcing computation (Goldwasser et al., 2008; Gennaro et al., 2010; Chung et al., 2010; Applebaum et al., 2010) and constructing short non-interactive zero-knowledge proofs (Gentry, 2009). Some of the applications of fully homomorphic encryption do not require its full power. For example, in private information retrieval (PIR), it is sufficient to have a somewhat homomorphic encryption scheme that is capable of evaluating simple database indexing functions. For this applications, what is needed is an optimized and less functional encryption scheme that is more efficient than a fully homomorphic encryption function. Design of such functions for different application scenarios is also a current hot topic of research.

---

### النسخة العربية

أدت دراسة التشفير المتماثل الكامل إلى عدد من المفاهيم والأسئلة الجديدة والمثيرة، بالإضافة إلى مجموعة أدوات قوية لمعالجتها. نختتم الفصل بمناقشة عدد من الاتجاهات البحثية المتعلقة بمجال التشفير المتماثل الكامل وبشكل أعم، بمشكلة الحوسبة على البيانات المشفرة.

**تطبيقات التشفير المتماثل الكامل:** بينما كان يُعتبر بناء Gentry الأصلي غير قابل للتطبيق في النشر العملي، فإن البناءات الحديثة وجهود التنفيذ حسّنت بشكل كبير كفاءة التشفير المتماثل الكامل (Vaikuntanathan, 2011). ركزت جهود التنفيذ الأولية على مخطط Gentry الأصلي ومتغيراته (Smart & Vercauteren, 2010; Smart & Vercauteren, 2012; Coron et al., 2011; Gentry & Halevi, 2011)، والتي بدا أنها تطرح اختناقات كفاءة متأصلة إلى حد ما. تستفيد التنفيذات اللاحقة من التطورات الخوارزمية الحديثة (Brakerski & Vaikuntanathan, 2011; Brakerski et al., 2011; Brakerski & Vaikuntanathan, 2011a) التي تؤدي إلى أنظمة تشفير متماثل كامل أفضل تقاربياً، بالإضافة إلى آليات جبرية جديدة لتحسين الكفاءة الإجمالية لهذه المخططات (Naehrig et al., 2011; Gentry et al., 2012; Smart & Vercauteren, 2012).

**عدم القابلية للتطويع والتشفير المتماثل:** التماثل وعدم القابلية للتطويع هما خاصيتان متعامدتان لمخطط التشفير. تسمح مخططات التشفير المتماثل لأي شخص بتحويل تشفير رسالة m إلى تشفير f(m) لدوال غير تافهة f. من ناحية أخرى، يمنع التشفير غير القابل للتطويع هذا النوع من الأشياء بالضبط - فهو يتطلب ألا يتمكن أي خصم من تحويل تشفير m إلى تشفير أي رسالة ذات صلة. في الأساس، ما نحتاجه هو مزيج من كلتا الخاصيتين اللتين تسمحان بشكل انتقائي بالحسابات المتماثلة (Vaikuntanathan, 2011). هذا يعني أن المُقيّم يجب أن يكون قادراً على حساب أي دالة بشكل متماثل من فئة محددة مسبقاً $F_{hom}$؛ ومع ذلك، يجب ألا تتمكن من تحويل تشفير m إلى تشفير f(m) حيث $f \\notin F_{hom}$ لا يصح (أي أن f لا تنتمي إلى $F_{hom}$). السؤال الطبيعي الذي يطرح نفسه هو: هل يمكننا التحكم فيما يتم حسابه (بشكل متماثل)؟

اتضح أن الإجابة على هذا السؤال صعبة. يقترح Boneh و Segev و Waters (Boneh et al., 2011) مفهوم القابلية للتطويع الموجه - وهو إضفاء طابع رسمي محتمل لمثل هذا المتطلب بالإضافة إلى بناءات رسمية لمثل هذه المخططات التشفيرية. يعتمد مخطط التشفير الخاص بهم على افتراض قوي من نوع معرفة الأس الذي يسمح بالتقييم التكراري لما لا يزيد عن t دالة، حيث t ثابت محدد ومحدد مسبقاً بشكل مناسب. يُعد تحسين بنائهم بالإضافة إلى افتراضات التعقيد الأساسية مشكلة مفتوحة مهمة (Vaikuntanathan, 2011).

من المثير للاهتمام أيضاً توسيع تعريف عدم القابلية للتطويع للسماح بهجمات النص المشفر المختار. كمثال، نأخذ بعين الاعتبار المشكلة التي تتضمن تنفيذ نظام إعلانات مستهدف مشفر يولد إعلانات اعتماداً على محتويات البريد الإلكتروني للمستخدم. نظراً لأن البريد الإلكتروني مخزن بشكل مشفر بمفتاح المستخدم العام، يقوم خادم البريد الإلكتروني بإجراء تقييم متماثل ويحسب إعلاناً مشفراً لإرساله مرة أخرى إلى المستخدم. يقوم المستخدم بفك تشفيره، ويؤدي إجراءً اعتماداً على ما يراه. إذا كان الإعلان ذا صلة، فقد تختار النقر عليه؛ وإلا فإنها ببساطة تتجاهله. ومع ذلك، إذا كان خادم البريد الإلكتروني على علم بهذه المعلومات، أي ما إذا كان المستخدم قد نقر على الإعلان أم لا، فيمكنه استخدام هذا كوحي فك تشفير مقيد لكسر أمان مخطط التشفير الخاص بالمستخدم وربما حتى استعادة مفتاحها السري. مثل هذه الهجمات منتشرة في كل مكان عندما نحسب على البيانات المشفرة، تقريباً إلى درجة أن أمان CCA يبدو حتمياً. ومع ذلك، من السهل أن نرى أن مخططات التشفير المتماثل للنص المشفر المختار (الآمنة بـ CCA2) لا يمكن أن توجد. لذلك، فإن تعريف أمان مناسب وبناءات تحقق التعريف مطلوبة.

**التشفير المتماثل الكامل وفك التشفير الوظيفي:** تسمح مخططات التشفير المتماثل لأي شخص بتقييم الدوال على البيانات المشفرة، لكن المُقيّمين لا يرون أي معلومات حول النتيجة أبداً. هل من الممكن بناء مخطط تشفير حيث يمكن للمستخدم حساب f(m) من تشفير رسالة m، لكن لا يجب أن تتمكن من تعلم أي معلومات أخرى حول m (بما في ذلك النتائج الوسيطة في حساب f)؟ في الأساس، تتلخص المسألة في السؤال التالي: هل يمكننا التحكم في المعلومات التي يمكن للمُقيّم رؤيتها؟ يُسمى مثل هذا المخطط التشفيري مخطط تشفير وظيفي. تم تقديم مفهوم مخطط التشفير الوظيفي لأول مرة من قبل Sahai و Waters (Sahai & Waters, 2005) وتم التحقيق فيه لاحقاً في عدد من الأعمال المثيرة للاهتمام (Katz et al., 2013; Lewko et al., 2010; Boneh et al., 2011; Agrawal et al., 2011). على الرغم من أن البناءات في هذه المقترحات تعمل لعدة عائلات مثيرة للاهتمام من الدوال (مثل الصيغ الأحادية والجداءات الداخلية)، إلا أن بناء مخطط تشفير وظيفي كامل لم يتحقق بعد ويظل مشكلة مفتوحة. ما نحتاجه هو نظام تشفير جديد وعام يوفر لنا تحكماً دقيقاً فيما يمكن للمرء رؤيته والوصول إليه وما يمكن للمرء حسابه على البيانات للحصول على ناتج مرغوب.

**مشاكل وتطبيقات أخرى:** سؤال مفتوح مهم آخر يتعلق بالافتراضات الكامنة وراء أنظمة التشفير المتماثل الكامل الحالية. جميع مخططات التشفير المتماثل الكامل المعروفة تعتمد على صلابة مسائل الشبكات البلورية. السؤال الطبيعي الذي يطرح نفسه - هل يمكننا بناء تشفير متماثل كامل من مناهج أخرى - على سبيل المثال، من افتراضات نظرية الأعداد؟ هل يمكننا إدخال مسألة صلابة التحليل إلى عوامل أو اللوغاريتمات المنفصلة في هذه المشكلة؟

بالإضافة إلى السيناريوهات التي يكون فيها من المفيد إبقاء جميع البيانات مشفرة وإجراء حسابات على البيانات المشفرة، يمكن استغلال التشفير المتماثل الكامل بشكل مفيد لحل عدد من المشاكل العملية في علم التشفير. مثالان على ذلك هما مشاكل الحوسبة الخارجية القابلة للتحقق (Goldwasser et al., 2008; Gennaro et al., 2010; Chung et al., 2010; Applebaum et al., 2010) وبناء إثباتات معرفة صفرية قصيرة غير تفاعلية (Gentry, 2009). بعض تطبيقات التشفير المتماثل الكامل لا تتطلب قوته الكاملة. على سبيل المثال، في استرجاع المعلومات الخاصة (PIR)، يكفي الحصول على مخطط تشفير متماثل إلى حد ما قادر على تقييم دوال فهرسة قاعدة بيانات بسيطة. لهذه التطبيقات، ما هو مطلوب هو مخطط تشفير محسّن وأقل وظيفية يكون أكثر كفاءة من دالة التشفير المتماثل الكامل. يُعد تصميم مثل هذه الدوال لسيناريوهات التطبيق المختلفة أيضاً موضوعاً ساخناً للبحث الحالي.

---

### Translation Notes

- **Key terms introduced:**
  - Non-malleability (عدم قابلية للتطويع)
  - Targeted malleability (قابلية للتطويع موجه)
  - Functional encryption (تشفير وظيفي)
  - CCA security (أمان CCA)
  - Chosen ciphertext attack (هجوم النص المشفر المختار)
  - Private information retrieval (استرجاع معلومات خاصة)
  - Verifiably outsourcing computation (حوسبة خارجية قابلة للتحقق)

- **Future research directions:**
  - Improving efficiency of FHE implementations
  - Combining homomorphism with non-malleability
  - Functional encryption schemes
  - Alternative mathematical foundations beyond lattices
  - Optimized schemes for specific applications

- **Open problems highlighted:**
  - Controlling homomorphic computations
  - Security definitions for CCA-secure homomorphic encryption
  - Fully functional encryption construction
  - Non-lattice-based FHE schemes

### Quality Metrics

- **Semantic equivalence:** 0.89
- **Technical accuracy:** 0.90
- **Readability:** 0.86
- **Glossary consistency:** 0.87
- **Overall section score:** 0.88

**Validation:** ✓ Comprehensive coverage of future research directions with clear identification of open problems
