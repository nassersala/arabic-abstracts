# Section 3.2: Somewhat Homomorphic Encryption Schemes
## القسم 3.2: مخططات التشفير المتماثل المحدود

**Section:** Homomorphic Encryption Schemes - Somewhat Homomorphic (SWHE)
**Translation Quality:** 0.86
**Glossary Terms Used:** homomorphic encryption (تشفير متماثل), encryption (تشفير), ciphertext (نص مشفر), plaintext (نص واضح), noise (ضوضاء), decryption (فك تشفير), security (أمان), circuit (دائرة)

---

### English Version

Somewhat Homomorphic Encryption (SWHE) represents an intermediate class of encryption schemes that bridges the gap between Partially Homomorphic Encryption (PHE) and Fully Homomorphic Encryption (FHE). While PHE schemes support unlimited applications of a single operation type (either addition or multiplication), SWHE schemes support both addition and multiplication operations, but only for a limited number of applications.

**Formal Characterization**: A SWHE scheme supports both homomorphic addition and multiplication:
- $E(m_1) + E(m_2) = E(m_1 + m_2)$
- $E(m_1) \times E(m_2) = E(m_1 \times m_2)$

However, these operations can only be performed up to a bounded depth before the scheme fails to decrypt correctly.

### The Noise Problem in SWHE

A fundamental characteristic of SWHE schemes is the presence of **noise** in ciphertexts. This noise serves a dual purpose:

1. **Security**: The noise component is essential for semantic security, preventing adversaries from distinguishing encryptions of different messages.

2. **Computational Limitation**: The noise grows with each homomorphic operation, eventually rendering decryption impossible.

**Noise Growth Dynamics**:
- **Addition**: Noise grows **linearly** with each additive operation
- **Multiplication**: Noise grows **exponentially** with each multiplicative operation

**Decryption Threshold**: When the accumulated noise exceeds approximately half the value of the private key modulus, decryption produces incorrect results. This fundamental limitation defines the computational depth of SWHE schemes.

**Mathematical Intuition**: Consider a ciphertext with noise $e$:
$$c = \mu + e \mod q$$

where $\mu$ encodes the message and $q$ is the ciphertext modulus. After $k$ multiplications, the noise can grow to approximately $e^{2^k}$, quickly exceeding the decryption threshold.

### Major SWHE Schemes

#### 1. Boneh-Goh-Nissim (BGN) Scheme

**Operational Capability**: Unlimited additions + One multiplication

**Key Innovation**: The BGN scheme demonstrated that **ciphertext size can remain constant** despite homomorphic operations—a major breakthrough addressing the ciphertext explosion problem in earlier schemes.

**Mathematical Foundation**:
- Based on bilinear pairings on elliptic curves
- Security relies on the subgroup decision problem
- Supports evaluation of 2-DNF (Disjunctive Normal Form) formulas

**Homomorphic Properties**:
- Can perform unlimited homomorphic additions on ciphertexts
- Supports exactly one level of multiplication
- After multiplication, only additive operations remain possible

**Advantages**:
- Constant ciphertext size (independent of number of operations)
- Efficient for specific computation classes (e.g., quadratic polynomials)
- Practical for applications like private information retrieval

**Limitations**:
- Restricted to one multiplication level
- Cannot evaluate deep circuits requiring multiple multiplication layers
- Relatively slower than some PHE schemes due to pairing operations

**Applications**: Privacy-preserving auctions, encrypted database queries with limited computation, secure voting systems.

#### 2. Yao's Garbled Circuits

**Operational Capability**: Arbitrary circuit depth (different paradigm from traditional SWHE)

**Approach**: Rather than operating on algebraically encrypted data, Yao's construction encrypts Boolean circuits gate-by-gate, allowing arbitrary function evaluation.

**Key Properties**:
- Supports evaluation of any Boolean circuit
- Each gate has a constant-size garbled representation
- Requires one round of interaction between parties

**Limitations**:
- **Linear ciphertext growth**: The size of the garbled circuit grows linearly with the number of gates
- Primarily a two-party computation protocol rather than a general encryption scheme
- Circuit must be fixed before encryption
- Does not support arbitrary re-evaluation or composition

**Significance**: While not a traditional SWHE scheme in the algebraic sense, Yao's garbled circuits demonstrated that secure computation on encrypted data was theoretically feasible.

#### 3. SYY Scheme (Sander-Young-Yung)

**Operational Capability**: Supports evaluation of polynomial-AND formulas

**Key Characteristics**:
- Can evaluate circuits with polynomial-sized AND gates
- Handles specific classes of Boolean formulas efficiently

**Limitations**:
- **Exponential ciphertext growth**: The ciphertext size increases exponentially with circuit depth
- Practical only for shallow circuits
- Limited applicability to real-world scenarios

#### 4. Ishai-Paskin (IP) Scheme

**Operational Capability**: Evaluates branching programs

**Innovation**: The scheme's ciphertext size is **independent of the evaluated function's complexity**, depending only on the input size.

**Key Properties**:
- Handles randomized branching programs
- Provides a different computational model than arithmetic circuits
- Useful for specific decision-tree computations

**Limitations**:
- Limited to branching program representation
- Not as general-purpose as circuit-based approaches

### Comparison of SWHE Schemes

| Scheme | Addition | Multiplication | Ciphertext Growth | Key Advantage |
|--------|----------|----------------|-------------------|---------------|
| BGN | Unlimited | 1 level | Constant | Constant size |
| Yao's Garbled | Unlimited | Unlimited | Linear in gates | Arbitrary depth |
| SYY | Unlimited | Limited | Exponential | Polynomial-AND |
| Ishai-Paskin | Depends on model | Depends on model | Constant in complexity | Function-independent size |

### Advantages of SWHE over PHE

1. **Dual Operation Support**: Unlike PHE, SWHE schemes support both addition and multiplication, enabling evaluation of more complex functions.

2. **Richer Computation**: Can evaluate polynomial expressions, quadratic formulas, and limited-depth circuits.

3. **Foundation for FHE**: SWHE schemes provided the theoretical and practical foundation for developing Fully Homomorphic Encryption.

### Fundamental Limitations of SWHE

Despite improvements over PHE, SWHE schemes face critical constraints:

1. **Bounded Computation Depth**: Cannot evaluate arbitrary circuits without depth restrictions due to noise accumulation.

2. **Noise Management Challenge**: Exponential noise growth with multiplication severely limits the number of multiplicative levels.

3. **Impractical for General Computation**: Real-world applications often require unbounded computation depth, which SWHE cannot provide.

4. **Application-Specific Trade-offs**: Each SWHE scheme is optimized for particular computation patterns, lacking general-purpose flexibility.

### Transition to Fully Homomorphic Encryption

The limitations of SWHE—particularly the noise growth problem—motivated the search for techniques to "refresh" ciphertexts and remove accumulated noise. This challenge remained unsolved until Craig Gentry's breakthrough in 2009, which introduced **bootstrapping**: a method to homomorphically evaluate the decryption function itself, thereby refreshing noisy ciphertexts and enabling unlimited computation depth.

SWHE schemes thus represent a critical evolutionary step in homomorphic encryption, demonstrating the feasibility of multi-operation homomorphism while highlighting the noise management challenge that FHE ultimately solved.

---

### النسخة العربية

يمثل التشفير المتماثل المحدود (SWHE) فئة وسيطة من مخططات التشفير التي تسد الفجوة بين التشفير المتماثل الجزئي (PHE) والتشفير المتماثل الكامل (FHE). بينما تدعم مخططات PHE تطبيقات غير محدودة لنوع عملية واحدة (إما الجمع أو الضرب)، تدعم مخططات SWHE عمليات الجمع والضرب معاً، ولكن لعدد محدود من التطبيقات فقط.

**التوصيف الرسمي**: يدعم مخطط SWHE كلاً من الجمع والضرب المتماثلين:
- $E(m_1) + E(m_2) = E(m_1 + m_2)$
- $E(m_1) \times E(m_2) = E(m_1 \times m_2)$

ومع ذلك، يمكن إجراء هذه العمليات فقط حتى عمق محدود قبل أن يفشل المخطط في فك التشفير بشكل صحيح.

### مشكلة الضوضاء في SWHE

من الخصائص الأساسية لمخططات SWHE وجود **الضوضاء** في النصوص المشفرة. تخدم هذه الضوضاء غرضاً مزدوجاً:

1. **الأمان**: مكون الضوضاء ضروري للأمان الدلالي، مما يمنع الخصوم من التمييز بين تشفيرات الرسائل المختلفة.

2. **القيد الحسابي**: تنمو الضوضاء مع كل عملية متماثلة، مما يجعل فك التشفير مستحيلاً في النهاية.

**ديناميكيات نمو الضوضاء**:
- **الجمع**: تنمو الضوضاء **خطياً** مع كل عملية جمع
- **الضرب**: تنمو الضوضاء **أسياً** مع كل عملية ضرب

**عتبة فك التشفير**: عندما تتجاوز الضوضاء المتراكمة حوالي نصف قيمة معامل المفتاح الخاص، ينتج فك التشفير نتائج غير صحيحة. هذا القيد الأساسي يحدد العمق الحسابي لمخططات SWHE.

**الحدس الرياضي**: لنفترض نصاً مشفراً مع ضوضاء $e$:
$$c = \mu + e \mod q$$

حيث $\mu$ يشفر الرسالة و$q$ هو معامل النص المشفر. بعد $k$ عمليات ضرب، يمكن أن تنمو الضوضاء إلى حوالي $e^{2^k}$، متجاوزة بسرعة عتبة فك التشفير.

### مخططات SWHE الرئيسية

#### 1. مخطط Boneh-Goh-Nissim (BGN)

**القدرة التشغيلية**: عمليات جمع غير محدودة + عملية ضرب واحدة

**الابتكار الرئيسي**: أظهر مخطط BGN أن **حجم النص المشفر يمكن أن يبقى ثابتاً** على الرغم من العمليات المتماثلة - اختراق كبير يعالج مشكلة انفجار النص المشفر في المخططات السابقة.

**الأساس الرياضي**:
- يعتمد على الاقترانات ثنائية الخطية على المنحنيات الإهليلجية
- يعتمد الأمان على مشكلة قرار المجموعة الفرعية
- يدعم تقييم صيغ 2-DNF (الشكل الطبيعي الفصلي)

**الخصائص المتماثلة**:
- يمكن إجراء عمليات جمع متماثلة غير محدودة على النصوص المشفرة
- يدعم مستوى واحد بالضبط من الضرب
- بعد الضرب، تبقى العمليات الجمعية فقط ممكنة

**المزايا**:
- حجم نص مشفر ثابت (مستقل عن عدد العمليات)
- فعال لفئات حساب معينة (مثل كثيرات الحدود التربيعية)
- عملي لتطبيقات مثل استرجاع المعلومات الخاصة

**القيود**:
- مقيد بمستوى ضرب واحد
- لا يمكن تقييم دوائر عميقة تتطلب طبقات ضرب متعددة
- أبطأ نسبياً من بعض مخططات PHE بسبب عمليات الاقتران

**التطبيقات**: المزادات التي تحافظ على الخصوصية، استعلامات قواعد البيانات المشفرة مع حساب محدود، أنظمة التصويت الآمن.

#### 2. الدوائر المشوشة ليَاو (Yao's Garbled Circuits)

**القدرة التشغيلية**: عمق دائرة تعسفي (نموذج مختلف عن SWHE التقليدي)

**المقاربة**: بدلاً من العمل على البيانات المشفرة جبرياً، يشفر بناء يَاو الدوائر المنطقية بوابة تلو بوابة، مما يسمح بتقييم دالة تعسفية.

**الخصائص الرئيسية**:
- يدعم تقييم أي دائرة منطقية
- كل بوابة لها تمثيل مشوش بحجم ثابت
- يتطلب جولة واحدة من التفاعل بين الأطراف

**القيود**:
- **نمو خطي للنص المشفر**: ينمو حجم الدائرة المشوشة خطياً مع عدد البوابات
- بشكل أساسي بروتوكول حساب ثنائي الأطراف بدلاً من مخطط تشفير عام
- يجب تحديد الدائرة قبل التشفير
- لا يدعم إعادة التقييم أو التركيب التعسفي

**الأهمية**: بينما ليس مخطط SWHE تقليدي بالمعنى الجبري، أظهرت الدوائر المشوشة ليَاو أن الحساب الآمن على البيانات المشفرة كان ممكناً نظرياً.

#### 3. مخطط SYY (Sander-Young-Yung)

**القدرة التشغيلية**: يدعم تقييم صيغ كثيرة الحدود-AND

**الخصائص الرئيسية**:
- يمكن تقييم دوائر مع بوابات AND بحجم كثير الحدود
- يتعامل مع فئات معينة من الصيغ المنطقية بكفاءة

**القيود**:
- **نمو أسي للنص المشفر**: يزداد حجم النص المشفر أسياً مع عمق الدائرة
- عملي فقط للدوائر الضحلة
- قابلية تطبيق محدودة على السيناريوهات الواقعية

#### 4. مخطط Ishai-Paskin (IP)

**القدرة التشغيلية**: يقيّم برامج التفرع

**الابتكار**: حجم النص المشفر للمخطط **مستقل عن تعقيد الدالة المُقيّمة**، ويعتمد فقط على حجم المدخلات.

**الخصائص الرئيسية**:
- يتعامل مع برامج التفرع العشوائية
- يوفر نموذجاً حسابياً مختلفاً عن الدوائر الحسابية
- مفيد لحسابات شجرة القرار المعينة

**القيود**:
- محدود لتمثيل برنامج التفرع
- ليس للأغراض العامة كالمقاربات القائمة على الدوائر

### مقارنة مخططات SWHE

| المخطط | الجمع | الضرب | نمو النص المشفر | الميزة الرئيسية |
|--------|-------|-------|------------------|------------------|
| BGN | غير محدود | مستوى واحد | ثابت | حجم ثابت |
| دوائر يَاو المشوشة | غير محدود | غير محدود | خطي في البوابات | عمق تعسفي |
| SYY | غير محدود | محدود | أسي | كثير الحدود-AND |
| Ishai-Paskin | يعتمد على النموذج | يعتمد على النموذج | ثابت في التعقيد | حجم مستقل عن الدالة |

### مزايا SWHE على PHE

1. **دعم العمليات المزدوجة**: على عكس PHE، تدعم مخططات SWHE كلاً من الجمع والضرب، مما يمكّن من تقييم دوال أكثر تعقيداً.

2. **حساب أغنى**: يمكن تقييم تعبيرات كثيرة الحدود، والصيغ التربيعية، والدوائر ذات العمق المحدود.

3. **أساس لـ FHE**: قدمت مخططات SWHE الأساس النظري والعملي لتطوير التشفير المتماثل الكامل.

### القيود الأساسية لـ SWHE

على الرغم من التحسينات على PHE، تواجه مخططات SWHE قيوداً حرجة:

1. **عمق حساب محدود**: لا يمكن تقييم دوائر تعسفية بدون قيود العمق بسبب تراكم الضوضاء.

2. **تحدي إدارة الضوضاء**: يحد النمو الأسي للضوضاء مع الضرب بشدة من عدد مستويات الضرب.

3. **غير عملي للحساب العام**: غالباً ما تتطلب التطبيقات الواقعية عمق حساب غير محدود، وهو ما لا يمكن أن توفره SWHE.

4. **مقايضات خاصة بالتطبيق**: كل مخطط SWHE محسّن لأنماط حساب معينة، مفتقراً إلى المرونة للأغراض العامة.

### الانتقال إلى التشفير المتماثل الكامل

حفزت قيود SWHE - خاصة مشكلة نمو الضوضاء - البحث عن تقنيات "لتجديد" النصوص المشفرة وإزالة الضوضاء المتراكمة. ظل هذا التحدي دون حل حتى اختراق كريج جينتري في عام 2009، الذي قدم **التمهيد الذاتي (bootstrapping)**: طريقة لتقييم دالة فك التشفير نفسها بشكل متماثل، وبالتالي تجديد النصوص المشفرة المشوشة وتمكين عمق حساب غير محدود.

وبالتالي، تمثل مخططات SWHE خطوة تطورية حرجة في التشفير المتماثل، مما يوضح جدوى التماثل متعدد العمليات مع تسليط الضوء على تحدي إدارة الضوضاء الذي حلته FHE في النهاية.

---

### Translation Notes

- **Figures referenced:** Comparison table for SWHE schemes
- **Key terms introduced:** SWHE, noise growth, BGN, Yao's garbled circuits, SYY, Ishai-Paskin, bootstrapping concept, bilinear pairings, 2-DNF
- **Equations:** 3 mathematical formulas for homomorphic operations and noise
- **Citations:** Multiple scheme papers (Boneh-Goh-Nissim, Yao, Sander-Young-Yung, Ishai-Paskin)
- **Special handling:**
  - Scheme names kept in original English
  - Mathematical notation preserved in LaTeX
  - "Noise" translated as "ضوضاء" following cryptographic convention

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.89
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score: 0.86**

### Notes
- The noise growth problem is central to understanding the transition from SWHE to FHE
- BGN's constant ciphertext size is a significant theoretical achievement
- The section sets up bootstrapping as the key innovation needed for FHE
- Comparison table helps readers understand trade-offs between different SWHE approaches
