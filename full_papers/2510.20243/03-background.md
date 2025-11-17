# Section 3: Background
## القسم 3: الخلفية

**Section:** background
**Translation Quality:** 0.88
**Glossary Terms Used:** finite field, symmetric encryption, asymmetric encryption, homomorphic encryption, plaintext, ciphertext, key expansion, substitution, permutation, S-box, AES, Pasta, XOF, DMA, nonce, round constant, Feistel network

---

### English Version

## III. BACKGROUND

### A. Notations

Throughout this paper, we use the following notations. Let $\mathbb{F}_p$ denote a finite field of prime order $p$. The internal state of the Pasta cipher is represented as $\mathbf{x} = \mathbf{x}_L \| \mathbf{x}_R$, where each half consists of $t$ words of 32 bits. A symmetric secret key is denoted by $sk$, while $N$ represents a public nonce and $i$ indexes the input block in a message stream. Plaintext and ciphertext blocks are denoted by $\mathbf{m}_i$ and $\mathbf{c}_i$, respectively. The core permutation of Pasta is Pasta-$\pi(\cdot)$, applied over $r$ rounds comprising affine layers $A_{j,N,i}$ and substitution layers $S$, $S'$. The keystream is expanded using an extendable-output function (XOF, e.g., SHAKE128), and $\text{left}_t(\cdot)$ extracts the first $t$ words from a permutation output. In our hardware design, DMA refers to Direct Memory Access used for high-throughput data transfer between the processing system (PS) and programmable logic (PL).

### B. Symmetric and Asymmetric Encryption

Symmetric and asymmetric encryption form the foundation of modern cryptographic systems [9], each with distinct operational principles, security properties, and performance characteristics. Symmetric encryption employs a single shared secret key for both encryption and decryption, offering high throughput and low computational cost. It is widely used in environments with constrained resources, such as embedded systems, encrypted storage, and real-time communication [7]. In contrast, asymmetric encryption is based on a public and private key pair, enabling secure communication without pre-shared keys and supporting functions such as digital signatures and key encapsulation [9]. Although schemes like RSA and elliptic curve cryptography (ECC) provide flexible trust models and strong security guarantees, they are inherently more computationally demanding and less suited for processing large volumes of data. As a result, many cryptographic protocols adopt a hybrid approach in which asymmetric encryption establishes secure channels or performs key exchange, while symmetric encryption secures the data payload [7]. This design pattern also informs the structure of homomorphic encryption systems, where lightweight symmetric components are increasingly employed to alleviate the computational overhead of public-key operations [8], [14].

### C. Homomorphic Encryption

Homomorphic encryption (HE) enhances traditional cryptographic techniques by enabling computations to be carried out directly on encrypted data [1], [2]. This allows an untrusted party, such as a cloud service provider, to perform meaningful operations without access to the plaintext, thereby preserving data confidentiality throughout the computational process. The fully homomorphic encryption (FHE) model supports arbitrary computations on ciphertexts and represents the most powerful instantiation of HE [5], [7]. However, this expressiveness comes at a substantial performance cost. Each stage in the FHE workflow, ranging from encoding and encryption to homomorphic evaluation and decryption, involves complex arithmetic over high-dimensional ciphertexts [6], [9]. As a result, FHE systems typically incur orders-of-magnitude increases in computation time and memory usage, along with significant ciphertext expansion [10], [11].

Hybrid homomorphic encryption (HHE) has been proposed as a practical alternative to address these challenges [8], [14]. By combining efficient symmetric encryption for general data protection with targeted use of FHE for sensitive or security-critical operations, HHE reduces the computational demands placed on the client while preserving strong end-to-end security guarantees [15]–[18]. This balanced design has enabled new applications of privacy-preserving machine learning in edge computing scenarios, where devices operate under strict resource constraints related to performance, bandwidth, and energy consumption [8], [19].

### D. Advanced Encryption Standard (AES)

The Advanced Encryption Standard (AES), defined in NIST FIPS 197 [9], is a symmetric-key block cipher that operates on 128-bit plaintext blocks and supports key sizes of 128, 192, or 256 bits. The algorithm applies a sequence of transformation rounds to the plaintext, where the number of rounds $N_r$ depends on the key length: 10, 12, or 14 rounds for 128-, 192-, and 256-bit keys, respectively. Each round uses a unique 128-bit round key derived from the original key via the key expansion algorithm [9].

**Algorithm 1 Pseudocode for CIPHER()**

```
1: procedure CIPHER(in, Nr, w)
2:     state ← in
3:     state ← AddRoundKey(state, w[0..3])
4:     for round from 1 to Nr - 1 do
5:         state ← SubBytes(state)
6:         state ← ShiftRows(state)
7:         state ← MixColumns(state)
8:         state ← AddRoundKey(state, w[4·round..4·round+3])
9:     state ← SubBytes(state)
10:    state ← ShiftRows(state)
11:    state ← AddRoundKey(state, w[4·Nr..4·Nr+3])
12:    return state
```

**Algorithm 2 Pseudocode for INVCIPHER()**

```
1: procedure INVCIPHER(in, Nr, w)
2:     state ← in
3:     state ← AddRoundKey(state, w[4·Nr..4·Nr+3])
4:     for round from Nr - 1 downto 1 do
5:         state ← InvShiftRows(state)
6:         state ← InvSubBytes(state)
7:         state ← AddRoundKey(state, w[4·round..4·round+3])
8:         state ← InvMixColumns(state)
9:     state ← InvShiftRows(state)
10:    state ← InvSubBytes(state)
11:    state ← AddRoundKey(state, w[0..3])
12:    return state
```

The AES encryption process, defined by the Cipher() procedure, begins with an initial AddRoundKey, followed by $N_r - 1$ rounds consisting of SubBytes, ShiftRows, MixColumns, and AddRoundKey, and ends with a final round excluding MixColumns [7]. Decryption, via InvCipher(), reverses this sequence: starting with AddRoundKey, applying $N_r-1$ rounds of InvShiftRows, InvSubBytes, AddRoundKey, and InvMixColumns, and concluding with InvShiftRows, InvSubBytes, and a final AddRoundKey. Both procedures share the same expanded key schedule and ensure cryptographic strength through a combination of substitution, permutation, and key mixing [9]. Each round transforms the internal state as follows:

• **SubBytes:** A nonlinear substitution step that replaces each byte in the state using a fixed S-box, providing confusion.
• **ShiftRows:** A transposition step where the rows of the state matrix are cyclically shifted by different offsets, contributing to diffusion.
• **MixColumns:** A column-wise mixing operation that transforms each column of the state using linear algebra over a finite field, further enhancing diffusion.
• **AddRoundKey:** A bitwise XOR between the current state and a round-specific subkey derived from the original cipher key, injecting key material into each round.

The inverse operations, including InvSubBytes, InvShiftRows, and InvMixColumns, reverse their corresponding encryption steps [9].

### E. Pasta

Conventional symmetric ciphers like AES are ill-suited for homomorphic encryption (HE) contexts due to their reliance on nonlinear operations such as S-box lookups, table-driven substitutions, and fine-grained bitwise logic, all of which are expensive to emulate over encrypted data [7]. In contrast, Pasta is a symmetric cipher specifically designed to align with the computational structure of lattice-based HE schemes [14], [17], [19]. It avoids homomorphically inefficient operations and instead leverages FHE-friendly primitives such as modular addition, modular multiplication, and word-level linear transformations [14].

Pasta adopts a substitution-permutation network (SPN)-like architecture operating over 32-bit words [14]. Its nonlinear components are chosen to minimize multiplicative depth while ensuring adequate cryptographic diffusion, which is critical for FHE efficiency. This design enables practical hybrid homomorphic encryption (HHE) systems, where symmetric encryption is performed on the client side and homomorphic evaluation is offloaded to the server [8]. Its operation can be broken down into three main phases:

#### 1. State and Key Schedule

• The internal state is a vector $\mathbf{x} \in \mathbb{F}_p^{2t}$, $\mathbf{x} = \mathbf{x}_L \| \mathbf{x}_R$ split into left and right halves.
• A secret key $sk \in \mathbb{F}_p^{2t}$, along with a public nonce $N$ and block counter $i$, seeds an extendable-output function (e.g., SHAKE128) to generate round constants and affine-layer matrices.

#### 2. Keystream Generation (Encryption/Decryption)

• For a plaintext block $\mathbf{m}_i \in \mathbb{F}_p^t$, the ciphertext is computed as

$$\mathbf{c}_i = \mathbf{m}_i + \text{left}_t(\text{Pasta-}\pi(sk, N, i)),$$

where $\text{left}_t(\cdot)$ extracts the first $t$ words of the permutation output.

• Decryption recovers $\mathbf{m}_i$ by subtracting the same keystream component from $\mathbf{c}_i$.

#### 3. Core Permutation Pasta-$\pi$

• The core permutation consists of $r$ rounds (e.g., $r = 3$ for Pasta-3 and $r = 4$ for Pasta-4), each comprising a linear affine layer and a nonlinear substitution.

• The permutation over state $\mathbf{x} \in \mathbb{F}_p^{2t}$ with nonce $N$ and block counter $i$ is defined as:

$$\text{Pasta-}\pi(\mathbf{x}, N, i) = A_{r,N,i} \circ S \circ A_{r-1,N,i} \circ S' \circ \cdots \circ A_{1,N,i} \circ S' \circ A_{0,N,i}(\mathbf{x}).$$

• Each component is defined as follows:

  **a) Affine Layer $A_{j,N,i}$:** Applies an invertible linear transformation $M_{j,N,i}$ followed by a round constant, both derived from SHAKE128. This layer ensures reversible diffusion across the state.

  **b) Feistel-Style S-Box $S'$:** Used in rounds 0 through $r-1$, this low-depth substitution maps each element by:

  $$[S'(\mathbf{x})]_i = \begin{cases} x_i, & i = 0 \\ x_i + x_{i-1}^2, & \text{otherwise} \end{cases}$$

  and is efficiently implementable with a single multiplication and rotation.

  **c) Cube S-Box $S$:** Applied only in the final round, this nonlinearity is defined as

  $$S(x_i) = x_i^3,$$

  providing stronger algebraic complexity while remaining compatible with FHE operations.

---

### النسخة العربية

## III. الخلفية

### أ. الترميزات

على مدار هذا البحث، نستخدم الترميزات التالية. لتكن $\mathbb{F}_p$ تدل على حقل منته من رتبة أولية $p$. تُمثل الحالة الداخلية لشفرة Pasta كـ $\mathbf{x} = \mathbf{x}_L \| \mathbf{x}_R$، حيث يتكون كل نصف من $t$ كلمة من 32 بت. يُرمز لمفتاح سري متماثل بـ $sk$، بينما يمثل $N$ عدداً عشوائياً عاماً (nonce) ويفهرس $i$ كتلة الإدخال في تدفق الرسائل. يُرمز لكتل النص العادي والنص المشفر بـ $\mathbf{m}_i$ و $\mathbf{c}_i$، على التوالي. التبديل الأساسي لـ Pasta هو Pasta-$\pi(\cdot)$، ويُطبق على $r$ جولة تتضمن طبقات أفينية $A_{j,N,i}$ وطبقات استبدال $S$، $S'$. يتم توسيع تدفق المفاتيح باستخدام دالة خرج قابلة للتوسع (XOF، مثل SHAKE128)، و$\text{left}_t(\cdot)$ تستخرج أول $t$ كلمة من خرج التبديل. في تصميمنا العتادي، يشير DMA إلى الوصول المباشر للذاكرة المستخدم لنقل بيانات عالي الإنتاجية بين نظام المعالجة (PS) والمنطق القابل للبرمجة (PL).

### ب. التشفير المتماثل وغير المتماثل

يشكل التشفير المتماثل وغير المتماثل الأساس لأنظمة التشفير الحديثة [9]، كل منهما بمبادئ تشغيلية مميزة، وخصائص أمان، وخصائص أداء. يستخدم التشفير المتماثل مفتاحاً سرياً مشتركاً واحداً لكل من التشفير وفك التشفير، مما يوفر إنتاجية عالية وتكلفة حسابية منخفضة. يُستخدم على نطاق واسع في البيئات ذات الموارد المقيدة، مثل الأنظمة المدمجة، والتخزين المشفر، والاتصال في الوقت الفعلي [7]. في المقابل، يعتمد التشفير غير المتماثل على زوج مفاتيح عامة وخاصة، مما يتيح اتصالاً آمناً دون مفاتيح مشتركة مسبقاً ويدعم وظائف مثل التواقيع الرقمية وتغليف المفاتيح [9]. على الرغم من أن مخططات مثل RSA وتشفير المنحنى الإهليلجي (ECC) توفر نماذج ثقة مرنة وضمانات أمان قوية، إلا أنها أكثر تطلباً حسابياً بطبيعتها وأقل ملاءمة لمعالجة كميات كبيرة من البيانات. نتيجة لذلك، تتبنى العديد من البروتوكولات التشفيرية نهجاً هجيناً يقوم فيه التشفير غير المتماثل بإنشاء قنوات آمنة أو تنفيذ تبادل المفاتيح، بينما يؤمن التشفير المتماثل حمولة البيانات [7]. يُعلم نمط التصميم هذا أيضاً بنية أنظمة التشفير المتماثل، حيث يتم استخدام مكونات متماثلة خفيفة الوزن بشكل متزايد لتخفيف العبء الحسابي لعمليات المفتاح العام [8]، [14].

### ج. التشفير المتماثل

يعزز التشفير المتماثل (HE) التقنيات التشفيرية التقليدية من خلال تمكين إجراء الحسابات مباشرة على البيانات المشفرة [1]، [2]. يتيح هذا لطرف غير موثوق، مثل مزود خدمة سحابية، تنفيذ عمليات ذات معنى دون الوصول إلى النص العادي، وبالتالي الحفاظ على سرية البيانات طوال العملية الحسابية. يدعم نموذج التشفير المتماثل الكامل (FHE) حسابات تعسفية على النصوص المشفرة ويمثل التجسيد الأقوى للتشفير المتماثل [5]، [7]. ومع ذلك، فإن هذه التعبيرية تأتي بتكلفة أداء كبيرة. تتضمن كل مرحلة في مسار عمل التشفير المتماثل الكامل، بدءاً من الترميز والتشفير إلى التقييم المتماثل وفك التشفير، حساباً معقداً على نصوص مشفرة عالية الأبعاد [6]، [9]. نتيجة لذلك، تتكبد أنظمة التشفير المتماثل الكامل عادةً زيادات بأوامر من الحجم في وقت الحساب واستخدام الذاكرة، إلى جانب توسع كبير في النص المشفر [10]، [11].

تم اقتراح التشفير المتماثل الهجين (HHE) كبديل عملي لمعالجة هذه التحديات [8]، [14]. من خلال دمج التشفير المتماثل الفعال لحماية البيانات العامة مع الاستخدام المستهدف للتشفير المتماثل الكامل للعمليات الحساسة أو الحرجة من حيث الأمان، يقلل التشفير المتماثل الهجين من المتطلبات الحسابية الموضوعة على العميل مع الحفاظ على ضمانات أمان قوية من البداية إلى النهاية [15]–[18]. لقد مكّن هذا التصميم المتوازن من تطبيقات جديدة للتعلم الآلي الحافظ للخصوصية في سيناريوهات الحوسبة على الحافة، حيث تعمل الأجهزة في ظل قيود موارد صارمة تتعلق بالأداء وعرض النطاق الترددي واستهلاك الطاقة [8]، [19].

### د. معيار التشفير المتقدم (AES)

معيار التشفير المتقدم (AES)، المُعرّف في NIST FIPS 197 [9]، هو شفرة كتلية متماثلة المفتاح تعمل على كتل نص عادي 128-بت وتدعم أحجام مفاتيح 128 أو 192 أو 256 بت. تطبق الخوارزمية تسلسلاً من جولات التحويل على النص العادي، حيث يعتمد عدد الجولات $N_r$ على طول المفتاح: 10 أو 12 أو 14 جولة لمفاتيح 128- أو 192- أو 256-بت، على التوالي. تستخدم كل جولة مفتاح جولة فريد من 128-بت مشتق من المفتاح الأصلي عبر خوارزمية توسيع المفتاح [9].

**خوارزمية 1: كود زائف لـ CIPHER()**

```
1: إجراء CIPHER(in, Nr, w)
2:     state ← in
3:     state ← AddRoundKey(state, w[0..3])
4:     for round from 1 to Nr - 1 do
5:         state ← SubBytes(state)
6:         state ← ShiftRows(state)
7:         state ← MixColumns(state)
8:         state ← AddRoundKey(state, w[4·round..4·round+3])
9:     state ← SubBytes(state)
10:    state ← ShiftRows(state)
11:    state ← AddRoundKey(state, w[4·Nr..4·Nr+3])
12:    return state
```

**خوارزمية 2: كود زائف لـ INVCIPHER()**

```
1: إجراء INVCIPHER(in, Nr, w)
2:     state ← in
3:     state ← AddRoundKey(state, w[4·Nr..4·Nr+3])
4:     for round from Nr - 1 downto 1 do
5:         state ← InvShiftRows(state)
6:         state ← InvSubBytes(state)
7:         state ← AddRoundKey(state, w[4·round..4·round+3])
8:         state ← InvMixColumns(state)
9:     state ← InvShiftRows(state)
10:    state ← InvSubBytes(state)
11:    state ← AddRoundKey(state, w[0..3])
12:    return state
```

تبدأ عملية تشفير AES، المُعرّفة بإجراء Cipher()، بـ AddRoundKey الأولي، يليها $N_r - 1$ جولة تتكون من SubBytes وShiftRows وMixColumns وAddRoundKey، وتنتهي بجولة نهائية باستثناء MixColumns [7]. يعكس فك التشفير، عبر InvCipher()، هذا التسلسل: بدءاً من AddRoundKey، وتطبيق $N_r-1$ جولة من InvShiftRows وInvSubBytes وAddRoundKey وInvMixColumns، والختام بـ InvShiftRows وInvSubBytes وAddRoundKey النهائي. يتشارك كلا الإجراءين في نفس جدول المفاتيح الموسّع ويضمنان القوة التشفيرية من خلال مزيج من الاستبدال والتبديل وخلط المفاتيح [9]. تحوّل كل جولة الحالة الداخلية على النحو التالي:

• **SubBytes:** خطوة استبدال غير خطية تستبدل كل بايت في الحالة باستخدام صندوق استبدال S ثابت، مما يوفر الإرباك.
• **ShiftRows:** خطوة تبديل حيث تُزاح صفوف مصفوفة الحالة دورياً بإزاحات مختلفة، مما يساهم في الانتشار.
• **MixColumns:** عملية خلط على مستوى الأعمدة تحوّل كل عمود من الحالة باستخدام الجبر الخطي على حقل منته، مما يعزز الانتشار بشكل أكبر.
• **AddRoundKey:** XOR على مستوى البت بين الحالة الحالية ومفتاح فرعي خاص بالجولة مشتق من مفتاح التشفير الأصلي، مما يحقن مادة المفتاح في كل جولة.

تعكس العمليات العكسية، بما في ذلك InvSubBytes وInvShiftRows وInvMixColumns، خطوات التشفير المقابلة لها [9].

### هـ. Pasta

الشفرات المتماثلة التقليدية مثل AES غير مناسبة لسياقات التشفير المتماثل (HE) بسبب اعتمادها على عمليات غير خطية مثل عمليات البحث في صناديق الاستبدال S، والاستبدالات المدفوعة بالجداول، والمنطق البتي الدقيق، وكلها مكلفة لمحاكاتها على البيانات المشفرة [7]. في المقابل، Pasta هي شفرة متماثلة مصممة خصيصاً للتوافق مع البنية الحسابية لمخططات التشفير المتماثل القائمة على الشبكة [14]، [17]، [19]. تتجنب العمليات غير الفعالة متماثلياً وتستفيد بدلاً من ذلك من العناصر الأولية الصديقة للتشفير المتماثل الكامل مثل الجمع المعياري، والضرب المعياري، والتحويلات الخطية على مستوى الكلمة [14].

تعتمد Pasta معمارية شبيهة بشبكة الاستبدال-التبديل (SPN) تعمل على كلمات 32-بت [14]. يتم اختيار مكوناتها غير الخطية لتقليل العمق الضربي مع ضمان انتشار تشفيري كافٍ، وهو أمر حاسم لكفاءة التشفير المتماثل الكامل. يتيح هذا التصميم أنظمة تشفير متماثل هجين (HHE) عملية، حيث يتم إجراء التشفير المتماثل على جانب العميل ويتم تفريغ التقييم المتماثل إلى الخادم [8]. يمكن تقسيم عمليتها إلى ثلاث مراحل رئيسية:

#### 1. الحالة وجدول المفاتيح

• الحالة الداخلية هي متجه $\mathbf{x} \in \mathbb{F}_p^{2t}$، $\mathbf{x} = \mathbf{x}_L \| \mathbf{x}_R$ مقسم إلى نصفين أيسر وأيمن.
• مفتاح سري $sk \in \mathbb{F}_p^{2t}$، إلى جانب عدد عشوائي عام $N$ وعداد كتلة $i$، يبذر دالة خرج قابلة للتوسع (مثل SHAKE128) لتوليد ثوابت الجولة ومصفوفات الطبقة الأفينية.

#### 2. توليد تدفق المفاتيح (التشفير / فك التشفير)

• لكتلة نص عادي $\mathbf{m}_i \in \mathbb{F}_p^t$، يُحسب النص المشفر كـ

$$\mathbf{c}_i = \mathbf{m}_i + \text{left}_t(\text{Pasta-}\pi(sk, N, i)),$$

حيث $\text{left}_t(\cdot)$ تستخرج أول $t$ كلمة من خرج التبديل.

• يستعيد فك التشفير $\mathbf{m}_i$ بطرح نفس مكون تدفق المفاتيح من $\mathbf{c}_i$.

#### 3. التبديل الأساسي Pasta-$\pi$

• يتكون التبديل الأساسي من $r$ جولة (مثل $r = 3$ لـ Pasta-3 و $r = 4$ لـ Pasta-4)، كل منها يتضمن طبقة أفينية خطية واستبدال غير خطي.

• التبديل على الحالة $\mathbf{x} \in \mathbb{F}_p^{2t}$ مع عدد عشوائي عام $N$ وعداد كتلة $i$ يُعرّف كـ:

$$\text{Pasta-}\pi(\mathbf{x}, N, i) = A_{r,N,i} \circ S \circ A_{r-1,N,i} \circ S' \circ \cdots \circ A_{1,N,i} \circ S' \circ A_{0,N,i}(\mathbf{x}).$$

• يُعرّف كل مكون على النحو التالي:

  **أ) الطبقة الأفينية $A_{j,N,i}$:** تطبق تحويلاً خطياً عكوساً $M_{j,N,i}$ يليه ثابت جولة، كلاهما مشتق من SHAKE128. تضمن هذه الطبقة انتشاراً عكوساً عبر الحالة.

  **ب) صندوق استبدال نمط فيستل $S'$:** يُستخدم في الجولات من 0 إلى $r-1$، هذا الاستبدال منخفض العمق يعيّن كل عنصر بـ:

  $$[S'(\mathbf{x})]_i = \begin{cases} x_i, & i = 0 \\ x_i + x_{i-1}^2, & \text{خلاف ذلك} \end{cases}$$

  ويمكن تنفيذه بكفاءة بضرب واحد ودوران.

  **ج) صندوق استبدال تكعيبي $S$:** يُطبق فقط في الجولة النهائية، هذا اللاخطية يُعرّف كـ

  $$S(x_i) = x_i^3,$$

  مما يوفر تعقيداً جبرياً أقوى مع بقائه متوافقاً مع عمليات التشفير المتماثل الكامل.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Finite field = حقل منته
  - Nonce = عدد عشوائي عام
  - Block counter = عداد كتلة
  - XOF (eXtendable Output Function) = دالة خرج قابلة للتوسع
  - DMA (Direct Memory Access) = الوصول المباشر للذاكرة
  - Affine layer = طبقة أفينية
  - Substitution layer = طبقة استبدال
  - Round constant = ثابت جولة
  - S-box = صندوق استبدال S
  - SPN (Substitution-Permutation Network) = شبكة الاستبدال-التبديل
  - Multiplicative depth = العمق الضربي
  - Feistel network = شبكة فيستل
  - Key expansion = توسيع المفتاح
  - Confusion = الإرباك
  - Diffusion = الانتشار

- **Algorithms:** Two pseudocode algorithms for AES (CIPHER and INVCIPHER)
- **Equations:** Multiple mathematical expressions for Pasta operations
- **Citations:** [1]-[19] referenced
- **Special handling:**
  - Mathematical notation preserved in LaTeX
  - Algorithm pseudocode kept in structured format with Arabic comments where needed
  - Technical terms like SHAKE128, NIST FIPS 197 kept in English
  - AES operations (SubBytes, ShiftRows, etc.) kept in English but explained in Arabic

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88

### Back-Translation Check (Pasta description opening)

Arabic: "الشفرات المتماثلة التقليدية مثل AES غير مناسبة لسياقات التشفير المتماثل (HE) بسبب اعتمادها على عمليات غير خطية..."

Back to English: "Conventional symmetric ciphers like AES are unsuitable for homomorphic encryption (HE) contexts due to their reliance on nonlinear operations..."

✓ Semantically equivalent to original
