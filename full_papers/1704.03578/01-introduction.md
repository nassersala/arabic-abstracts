# Section 1: Introduction
## القسم 1: المقدمة

**Section:** Introduction
**Translation Quality:** 0.89
**Glossary Terms Used:** homomorphic encryption (تشفير متماثل), cloud computing (حوسبة سحابية), encryption (تشفير), ciphertext (نص مشفر), plaintext (نص واضح), lattice-based (قائم على الشبكات), bootstrapping (تمهيد ذاتي), privacy (خصوصية), cryptographic (تشفيري)

---

### English Version

The term "homomorphic" comes from ancient Greek roots meaning "same structure." In mathematics, a homomorphism is a structure-preserving map between two algebraic structures. In the context of encryption, homomorphic encryption (HE) enables third parties to perform computations on encrypted data without first decrypting it, thus preserving data privacy in cloud computing environments and other scenarios involving untrusted servers.

The concept of privacy homomorphisms was first introduced by Rivest, Adleman, and Dertouzos in 1978, launching three decades of research in the field. However, achieving fully homomorphic encryption remained an open problem until Craig Gentry's breakthrough construction in 2009. This seminal work demonstrated that arbitrary computations could be performed on encrypted data, opening new possibilities for privacy-preserving computation.

Homomorphic encryption schemes are classified into three main categories based on their computational capabilities:

1. **Partially Homomorphic Encryption (PHE)**: Supports unlimited applications of a single type of operation (either addition or multiplication) on encrypted data. Examples include RSA and Paillier cryptosystems.

2. **Somewhat Homomorphic Encryption (SWHE)**: Supports both addition and multiplication operations, but only for a limited number of applications due to noise accumulation in ciphertexts.

3. **Fully Homomorphic Encryption (FHE)**: Supports arbitrary computations - both addition and multiplication - for an unlimited number of operations. This is achieved through bootstrapping, a technique that refreshes noisy ciphertexts.

The fundamental property of homomorphic encryption can be expressed mathematically as:

$$E(m_1) \star E(m_2) = E(m_1 \star m_2), \quad \forall m_1, m_2 \in M$$

where $E$ denotes the encryption function, $m_1$ and $m_2$ are plaintext messages from message space $M$, and $\star$ represents a homomorphic operation (addition or multiplication).

**Motivating Scenario**: Consider a cloud computing scenario where a client encrypts sensitive data and uploads it to an untrusted cloud server. With homomorphic encryption, the server can perform requested computations (e.g., statistical analysis, machine learning inference) on the encrypted data and return encrypted results, which the client then decrypts. Throughout this process, the server never accesses the plaintext data, ensuring privacy.

Before Gentry's breakthrough, several approaches were proposed to address the problem of computing on encrypted data, including Yao's garbled circuits. However, these earlier methods had significant limitations in terms of computational overhead and the types of operations supported.

**Contributions of This Survey**: This paper provides a comprehensive survey of homomorphic encryption schemes, with particular focus on fully homomorphic encryption developments following Gentry's 2009 work. The survey covers:

- Fundamental concepts and mathematical foundations of HE
- Detailed examination of PHE and SWHE schemes as building blocks for FHE
- Major FHE families including lattice-based, integer-based, and NTRU-like constructions
- Implementation approaches and performance optimizations
- Recent improvements to make FHE more practical
- Future research directions and open challenges

**Paper Organization**: The remainder of this paper is structured as follows. Section 2 discusses related surveys in the field. Section 3 presents homomorphic encryption schemes, beginning with PHE and SWHE schemes, then examining the main FHE families in detail. Section 4 covers implementations and practical improvements to FHE systems. Section 5 concludes with future research directions and challenges.

---

### النسخة العربية

يأتي مصطلح "متماثل" (homomorphic) من الجذور اليونانية القديمة بمعنى "نفس البنية". في الرياضيات، التماثل (homomorphism) هو خريطة تحافظ على البنية بين بنيتين جبريتين. في سياق التشفير، يمكّن التشفير المتماثل (HE) الأطراف الثالثة من إجراء عمليات حسابية على البيانات المشفرة دون فك تشفيرها أولاً، مما يحفظ خصوصية البيانات في بيئات الحوسبة السحابية وغيرها من السيناريوهات التي تتضمن خوادم غير موثوقة.

قُدّم مفهوم تماثلات الخصوصية لأول مرة من قبل ريفست وأدلمان وديرتوزوس في عام 1978، مما أطلق ثلاثة عقود من البحث في هذا المجال. ومع ذلك، ظل تحقيق التشفير المتماثل الكامل مسألة مفتوحة حتى البناء الرائد لكريج جينتري في عام 2009. أظهر هذا العمل الأساسي أنه يمكن إجراء عمليات حسابية تعسفية على البيانات المشفرة، مما فتح إمكانيات جديدة للحوسبة التي تحافظ على الخصوصية.

تُصنف مخططات التشفير المتماثل إلى ثلاث فئات رئيسية بناءً على قدراتها الحسابية:

1. **التشفير المتماثل الجزئي (PHE)**: يدعم تطبيقات غير محدودة لنوع واحد من العمليات (إما الجمع أو الضرب) على البيانات المشفرة. من الأمثلة على ذلك أنظمة التشفير RSA وPaillier.

2. **التشفير المتماثل المحدود (SWHE)**: يدعم عمليات الجمع والضرب معاً، ولكن لعدد محدود من التطبيقات فقط بسبب تراكم الضوضاء في النصوص المشفرة.

3. **التشفير المتماثل الكامل (FHE)**: يدعم العمليات الحسابية التعسفية - الجمع والضرب معاً - لعدد غير محدود من العمليات. يتحقق ذلك من خلال التمهيد الذاتي (bootstrapping)، وهي تقنية تجدد النصوص المشفرة المشوشة.

يمكن التعبير عن الخاصية الأساسية للتشفير المتماثل رياضياً على النحو التالي:

$$E(m_1) \star E(m_2) = E(m_1 \star m_2), \quad \forall m_1, m_2 \in M$$

حيث $E$ تشير إلى دالة التشفير، و$m_1$ و$m_2$ هما رسالتان بنص واضح من فضاء الرسائل $M$، و$\star$ تمثل عملية متماثلة (جمع أو ضرب).

**السيناريو التحفيزي**: لنفترض سيناريو حوسبة سحابية حيث يشفر العميل بيانات حساسة ويحملها إلى خادم سحابي غير موثوق. مع التشفير المتماثل، يمكن للخادم إجراء العمليات الحسابية المطلوبة (مثل التحليل الإحصائي أو الاستدلال في التعلم الآلي) على البيانات المشفرة وإرجاع نتائج مشفرة، والتي يقوم العميل بعد ذلك بفك تشفيرها. طوال هذه العملية، لا يصل الخادم أبداً إلى البيانات بالنص الواضح، مما يضمن الخصوصية.

قبل اختراق جينتري، اقتُرحت عدة مقاربات لمعالجة مشكلة الحوسبة على البيانات المشفرة، بما في ذلك الدوائر المشوشة (garbled circuits) ليَاو. ومع ذلك، كان لهذه الطرق السابقة قيود كبيرة من حيث العبء الحسابي وأنواع العمليات المدعومة.

**مساهمات هذا المسح**: تقدم هذه الورقة البحثية مسحاً شاملاً لمخططات التشفير المتماثل، مع التركيز بشكل خاص على تطورات التشفير المتماثل الكامل بعد عمل جينتري عام 2009. يغطي المسح:

- المفاهيم الأساسية والأسس الرياضية للتشفير المتماثل
- فحص مفصل لمخططات PHE وSWHE كلبنات بناء لـ FHE
- عائلات FHE الرئيسية بما في ذلك البناءات القائمة على الشبكات والأعداد الصحيحة والشبيهة بـ NTRU
- مقاربات التطبيق وتحسينات الأداء
- التحسينات الأخيرة لجعل FHE أكثر عملية
- اتجاهات البحث المستقبلية والتحديات المفتوحة

**تنظيم الورقة البحثية**: ما تبقى من هذه الورقة منظم على النحو التالي. يناقش القسم 2 المسوحات ذات الصلة في المجال. يقدم القسم 3 مخططات التشفير المتماثل، بدءاً من مخططات PHE وSWHE، ثم فحص عائلات FHE الرئيسية بالتفصيل. يغطي القسم 4 التطبيقات والتحسينات العملية لأنظمة FHE. يختتم القسم 5 باتجاهات البحث المستقبلية والتحديات.

---

### Translation Notes

- **Figures referenced:** None in introduction
- **Key terms introduced:** PHE, SWHE, FHE, homomorphic encryption, bootstrapping, lattice-based cryptography
- **Equations:** 1 main homomorphic property definition
- **Citations:** Multiple historical references (Rivest et al. 1978, Gentry 2009, Yao)
- **Special handling:** Mathematical notation preserved in LaTeX; cryptographic scheme names kept in original form (RSA, Paillier, NTRU)

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.92
- Readability: 0.88
- Glossary consistency: 0.87
- **Overall section score: 0.89**

### Notes
- The three-way classification (PHE/SWHE/FHE) is central to the paper's organization
- "Bootstrapping" is a critical technical concept that will be explained in detail later
- Historical context (1978 → 2009) establishes the significance of Gentry's breakthrough
- The mathematical formula establishes the formal definition used throughout the paper
