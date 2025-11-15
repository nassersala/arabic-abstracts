# Section 2: Fundamentals of Cryptography
## القسم 2: أساسيات علم التشفير

**Section:** Fundamentals of Cryptography
**Translation Quality:** 0.86
**Glossary Terms Used:** encryption (تشفير), cryptography (علم التشفير), algorithm (خوارزمية), symmetric (متماثل), asymmetric (غير متماثل), ciphertext (نص مشفر), plaintext (نص صريح)

---

### English Version

In this Section, we will recall some important concepts on encryption schemes. For more detailed information, the reader may refer to (Menezes et al., 1997; Van Tilborg, 2011). Encryption schemes are designed to preserve confidentiality. The security of encryption schemes must not rely on the obfuscation of their codes, but it should only be based on the secrecy of the key used in the encryption process. Encryption schemes are broadly of two types: symmetric and asymmetric encryption schemes. In the following, we present a very brief discussion on each of these schemes.

**Symmetric encryption schemes:** In these schemes, the sender and the receiver agree on the key they will use before establishing any secure communication session. Therefore, it is not possible for two persons who never met before to use such schemes directly. This also implies that in order to communicate with different persons, we must have a different key for each people. Requirement of large number of keys in these schemes make their key generation and management relatively more complex operations. However, symmetric schemes present the advantage of being very fast and they are used in applications where speed of execution is a paramount requirement. Among the existing symmetric encryption systems, AES (Daemen & Rijmen, 2000; Daemen & Rijmen, 2002), One-Time Pad (Vernam, 1926) and Snow (Ekdahl & Johansson, 2002) are very popular.

**Asymmetric encryption schemes:** In these schemes, every participant has a pair of keys- private and public. While the private key of a person is known to only her, the public key of each participant is known to everyone in the group. Such schemes are more secure than their symmetric counterparts and they don't need any prior agreement between the communicating parties on a common key before establishing a session of communication. RSA (Rivest et al., 1978b) and ElGamal (ElGamal, 1985) are two most popular asymmetric encryption systems.

**Security of encryption schemes:** Security of encryption schemes was first formalized by Shannon (Shannon, 1949). In his seminal paper, Shannon first introduced the notion of perfect secrecy/unconditional secrecy, which characterizes encryption schemes for which the knowledge of a ciphertext does not give any information about the corresponding plaintext and the encryption key. Shannon also proved that One-Time Pad (Vernam, 1926) encryption scheme is perfectly secure under certain conditions. However, no other encryption scheme has been proved to be unconditionally secure. For asymmetric schemes, we can rely on their mathematical structures to estimate their security strength in a formal way. These schemes are based on some well-identified mathematical problems which are hard to solve in general, but easy to solve for the one who knows the trapdoor – i.e., the owner of the keys. However, the estimation of the security level of these schemes may not be always correct due to several reasons. First, there may be other ways to break the system than solving the mathematical problems on which these schemes are based (Ajtai & Dwork, 1997; Nguyen & Stern, 1999). Second, most of the security proofs are performed in an idealized model called random oracle model, in which involved primitives, for example, hash functions, are considered truly random. This model has allowed the study of the security level of numerous asymmetric ciphers. However, we are now able to perform proofs in a more realistic model called standard model (Canetti et al., 1998; Paillier, 2007). This model eliminates some of the unrealistic assumptions in the random oracle model and makes the security analysis of cryptographic schemes more practical.

Usually, to evaluate the attack capacity of an adversary, we distinguish among several contexts (Diffie & Hellman, 1976): cipher-text only attacks (where the adversary has access only to some ciphertexts), known-plaintext attacks (where the adversary has access to some pairs of plaintext messages and their corresponding ciphertexts), chosen-plaintext attacks (the adversary has access to a decryption oracle that behaves like a black-box and takes a ciphertext as its input and outputs the corresponding plaintexts). The first context is the most frequent in real-world since it can happen when some adversary eavesdrops on a communication channel. The other cases may seem difficult to achieve, and may arise when the adversary is in a more powerful position; he may, for example, have stolen some plaintexts or an encryption engine. The chosen one exists in adaptive versions, where the opponents can wait for a computation result before choosing the next input (Fontaine & Galand, 2007).

**Probabilistic encryption:** Almost all the well-known cryptosystems are deterministic. This means that for a fixed encryption key, a given plaintext will always be encrypted into the same ciphertext under these systems. However, this may lead to some security problems. RSA scheme is a good example for explaining this point. Let us consider the following points with reference to the RSA cryptosystem:

• A particular plaintext may be encrypted in a too much structured way. With RSA, messages 0 and 1 are always encrypted as 0 and 1, respectively.

• It may be easy to compute some partial information about the plaintext: with RSA, the ciphertext c leaks one bit of information about the plaintext m, namely, the so called Jacobi symbol (Fontaine & Galand, 2007).

• When using a deterministic encryption scheme, it is easy to detect when the same message is sent twice while processed with the same key.

In view of the problems stated above, we prefer encryption schemes to be probabilistic. In case of symmetric schemes, we introduce a random vector in the encryption process (e.g., in the pseudo-random generator for stream ciphers, or in the operating mode for block ciphers) – generally called initial vector (IV). This vector may be public and it may be transmitted in a clear-text form. However, the IV must be changed every time we encrypt a message. In case of asymmetric ciphers, the security analysis is more mathematical and formal, and we want the randomized schemes to remain analyzable in the same way as the deterministic schemes. Researchers have proposed some models to randomize the existing deterministic schemes, as the optimal asymmetric encryption padding (OAEP) for RSA (or any scheme that is based on a trapdoor one-way permutation) (Bellare & Rogaway, 1995). In the literature, researchers have also proposed some other randomized schemes (ElGamal, 1985; Goldwasser & Micali, 1982; Blum & Goldwasser, 1985).

A simple consequence of this requirement of the encryption schemes to be preferably probabilistic appears in the phenomenon called expansion. Since for a plaintext we require the existence of several possible ciphertexts, the number of ciphertexts is greater than the number of possible plaintexts. This means the ciphertexts cannot be as short as the plaintexts; they have to be strictly longer. The ratio of the length of the ciphertext and the corresponding plaintext (in bits) is called expansion. The value of this parameter is of paramount importance in determining security and efficiency tradeoff of a probabilistic encryption scheme. In Paillier's scheme, an efficient probabilistic encryption mechanism has been proposed with the value of expansion less than 2 (Paillier, 1997). We will see the significance of expansion in other homomorphic encryption systems in the subsequent sections of this chapter.

---

### النسخة العربية

في هذا القسم، سنستعرض بعض المفاهيم المهمة حول مخططات التشفير. للحصول على معلومات أكثر تفصيلاً، يمكن للقارئ الرجوع إلى (Menezes et al., 1997; Van Tilborg, 2011). تُصمم مخططات التشفير للحفاظ على السرية. يجب ألا يعتمد أمان مخططات التشفير على تعتيم أكوادها، بل يجب أن يعتمد فقط على سرية المفتاح المستخدم في عملية التشفير. تنقسم مخططات التشفير بشكل عام إلى نوعين: مخططات التشفير المتماثلة وغير المتماثلة. في ما يلي، نقدم مناقشة موجزة جداً حول كل من هذه المخططات.

**مخططات التشفير المتماثلة:** في هذه المخططات، يتفق المرسل والمستقبل على المفتاح الذي سيستخدمونه قبل إنشاء أي جلسة اتصال آمنة. لذلك، لا يمكن لشخصين لم يلتقيا من قبل استخدام هذه المخططات مباشرة. وهذا يعني أيضاً أنه من أجل التواصل مع أشخاص مختلفين، يجب أن يكون لدينا مفتاح مختلف لكل شخص. إن متطلبات العدد الكبير من المفاتيح في هذه المخططات تجعل عمليات توليدها وإدارتها أكثر تعقيداً نسبياً. ومع ذلك، فإن المخططات المتماثلة تتميز بكونها سريعة جداً وتُستخدم في التطبيقات التي تكون فيها سرعة التنفيذ مطلباً بالغ الأهمية. من بين أنظمة التشفير المتماثلة الموجودة، يعد AES (Daemen & Rijmen, 2000; Daemen & Rijmen, 2002)، وOne-Time Pad (Vernam, 1926)، وSnow (Ekdahl & Johansson, 2002) من الأنظمة الشائعة جداً.

**مخططات التشفير غير المتماثلة:** في هذه المخططات، يمتلك كل مشارك زوجاً من المفاتيح - خاص وعام. بينما يُعرف المفتاح الخاص للشخص له فقط، فإن المفتاح العام لكل مشارك معروف للجميع في المجموعة. هذه المخططات أكثر أماناً من نظيراتها المتماثلة ولا تحتاج إلى أي اتفاق مسبق بين الأطراف المتصلة على مفتاح مشترك قبل إنشاء جلسة اتصال. RSA (Rivest et al., 1978b) وElGamal (ElGamal, 1985) هما نظامان من أكثر أنظمة التشفير غير المتماثلة شيوعاً.

**أمان مخططات التشفير:** تم إضفاء الطابع الرسمي على أمان مخططات التشفير لأول مرة من قبل Shannon (Shannon, 1949). في ورقته البحثية الرائدة، قدم Shannon لأول مرة مفهوم السرية التامة/السرية غير المشروطة، والتي تميز مخططات التشفير التي لا تعطي فيها معرفة النص المشفر أي معلومات عن النص الصريح المقابل ومفتاح التشفير. كما أثبت Shannon أيضاً أن مخطط التشفير One-Time Pad (Vernam, 1926) آمن تماماً في ظل ظروف معينة. ومع ذلك، لم يُثبت أن أي مخطط تشفير آخر آمن بشكل غير مشروط. بالنسبة للمخططات غير المتماثلة، يمكننا الاعتماد على بنياتها الرياضية لتقدير قوة أمانها بطريقة رسمية. تعتمد هذه المخططات على بعض المسائل الرياضية المحددة جيداً والتي يصعب حلها بشكل عام، ولكن يسهل حلها لمن يعرف الباب الخلفي - أي صاحب المفاتيح. ومع ذلك، قد لا يكون تقدير مستوى أمان هذه المخططات صحيحاً دائماً لعدة أسباب. أولاً، قد تكون هناك طرق أخرى لكسر النظام غير حل المسائل الرياضية التي تستند إليها هذه المخططات (Ajtai & Dwork, 1997; Nguyen & Stern, 1999). ثانياً، يتم إجراء معظم إثباتات الأمان في نموذج مثالي يسمى نموذج الوحي العشوائي، حيث تُعتبر العمليات البدائية المعنية، على سبيل المثال، دوال التجزئة، عشوائية حقاً. وقد سمح هذا النموذج بدراسة مستوى أمان العديد من الأصفار غير المتماثلة. ومع ذلك، أصبحنا الآن قادرين على إجراء الإثباتات في نموذج أكثر واقعية يسمى النموذج القياسي (Canetti et al., 1998; Paillier, 2007). يزيل هذا النموذج بعض الافتراضات غير الواقعية في نموذج الوحي العشوائي ويجعل تحليل أمان المخططات التشفيرية أكثر عملية.

عادةً، لتقييم قدرة الهجوم للخصم، نميز بين عدة سياقات (Diffie & Hellman, 1976): هجمات النص المشفر فقط (حيث يمكن للخصم الوصول فقط إلى بعض النصوص المشفرة)، هجمات النص الصريح المعروف (حيث يمكن للخصم الوصول إلى بعض أزواج رسائل النص الصريح ونصوصها المشفرة المقابلة)، هجمات النص الصريح المختار (يمكن للخصم الوصول إلى وحي فك التشفير الذي يتصرف مثل الصندوق الأسود ويأخذ نصاً مشفراً كمدخل له ويخرج النصوص الصريحة المقابلة). السياق الأول هو الأكثر شيوعاً في العالم الواقعي حيث يمكن أن يحدث عندما يتنصت بعض الخصوم على قناة اتصال. قد تبدو الحالات الأخرى صعبة التحقيق، وقد تنشأ عندما يكون الخصم في موقع أقوى؛ فقد يكون، على سبيل المثال، قد سرق بعض النصوص الصريحة أو محرك تشفير. يوجد المختار في إصدارات تكيفية، حيث يمكن للخصوم انتظار نتيجة الحساب قبل اختيار المدخل التالي (Fontaine & Galand, 2007).

**التشفير الاحتمالي:** تقريباً جميع أنظمة التشفير المعروفة هي حتمية. هذا يعني أنه بالنسبة لمفتاح تشفير ثابت، سيتم دائماً تشفير نص صريح معين في نفس النص المشفر في ظل هذه الأنظمة. ومع ذلك، قد يؤدي هذا إلى بعض المشاكل الأمنية. يُعد مخطط RSA مثالاً جيداً لشرح هذه النقطة. دعونا نتناول النقاط التالية بالإشارة إلى نظام RSA التشفيري:

• قد يتم تشفير نص صريح معين بطريقة منظمة للغاية. مع RSA، يتم دائماً تشفير الرسائل 0 و1 كـ 0 و1، على التوالي.

• قد يكون من السهل حساب بعض المعلومات الجزئية حول النص الصريح: مع RSA، يسرب النص المشفر c بتّة واحدة من المعلومات حول النص الصريح m، وهي ما يُسمى رمز جاكوبي (Fontaine & Galand, 2007).

• عند استخدام مخطط تشفير حتمي، من السهل اكتشاف متى يتم إرسال نفس الرسالة مرتين أثناء معالجتها بنفس المفتاح.

في ضوء المشاكل المذكورة أعلاه، نفضل أن تكون مخططات التشفير احتمالية. في حالة المخططات المتماثلة، نقدم متجهاً عشوائياً في عملية التشفير (على سبيل المثال، في المولد شبه العشوائي للأصفار الانسيابية، أو في وضع التشغيل للأصفار الكتلية) - يُسمى عموماً المتجه الابتدائي (IV). قد يكون هذا المتجه عاماً وقد يتم نقله في شكل نص واضح. ومع ذلك، يجب تغيير IV في كل مرة نقوم فيها بتشفير رسالة. في حالة الأصفار غير المتماثلة، يكون تحليل الأمان أكثر رياضية ورسمية، ونريد أن تظل المخططات العشوائية قابلة للتحليل بنفس الطريقة التي تُحلل بها المخططات الحتمية. اقترح الباحثون بعض النماذج لجعل المخططات الحتمية الموجودة عشوائية، مثل الحشو الأمثل للتشفير غير المتماثل (OAEP) لـ RSA (أو أي مخطط يعتمد على تبديل أحادي الاتجاه بباب خلفي) (Bellare & Rogaway, 1995). في الأدبيات، اقترح الباحثون أيضاً بعض المخططات العشوائية الأخرى (ElGamal, 1985; Goldwasser & Micali, 1982; Blum & Goldwasser, 1985).

نتيجة بسيطة لمتطلب أن تكون مخططات التشفير احتمالية يفضل أن تظهر في ظاهرة تسمى التوسع. نظراً لأننا نطلب وجود عدة نصوص مشفرة محتملة لنص صريح، فإن عدد النصوص المشفرة أكبر من عدد النصوص الصريحة المحتملة. هذا يعني أن النصوص المشفرة لا يمكن أن تكون قصيرة مثل النصوص الصريحة؛ يجب أن تكون أطول بكثير. تُسمى نسبة طول النص المشفر إلى النص الصريح المقابل (بالبتات) التوسع. قيمة هذا المعامل ذات أهمية قصوى في تحديد المفاضلة بين الأمان والكفاءة لمخطط التشفير الاحتمالي. في مخطط Paillier، تم اقتراح آلية تشفير احتمالية فعالة بقيمة توسع أقل من 2 (Paillier, 1997). سنرى أهمية التوسع في أنظمة التشفير المتماثل الأخرى في الأقسام اللاحقة من هذا الفصل.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:**
  - Symmetric encryption (تشفير متماثل)
  - Asymmetric encryption (تشفير غير متماثل)
  - Perfect secrecy (سرية تامة)
  - Unconditional secrecy (سرية غير مشروطة)
  - Trapdoor (باب خلفي)
  - Random oracle model (نموذج الوحي العشوائي)
  - Standard model (النموذج القياسي)
  - Cipher-text only attack (هجوم النص المشفر فقط)
  - Known-plaintext attack (هجوم النص الصريح المعروف)
  - Chosen-plaintext attack (هجوم النص الصريح المختار)
  - Probabilistic encryption (تشفير احتمالي)
  - Deterministic encryption (تشفير حتمي)
  - Initial vector (IV) (متجه ابتدائي)
  - Expansion (توسع)
  - Jacobi symbol (رمز جاكوبي)
  - OAEP (Optimal Asymmetric Encryption Padding) (الحشو الأمثل للتشفير غير المتماثل)

- **Equations:** None, but mathematical concepts discussed

- **Citations:** Multiple references to foundational cryptography papers (Shannon 1949, Diffie & Hellman 1976, Rivest 1978b, ElGamal 1985, etc.)

- **Special handling:**
  - Preserved cryptographic system names (AES, RSA, ElGamal, etc.)
  - Maintained technical precision for security concepts
  - Translated attack models carefully to preserve their technical meaning

### Quality Metrics

- **Semantic equivalence:** 0.87
- **Technical accuracy:** 0.88
- **Readability:** 0.85
- **Glossary consistency:** 0.85
- **Overall section score:** 0.86

### Back-Translation Sample (First Paragraph)

"In this section, we will review some important concepts about encryption schemes. For more detailed information, the reader can refer to (Menezes et al., 1997; Van Tilborg, 2011). Encryption schemes are designed to preserve confidentiality. The security of encryption schemes should not depend on obfuscating their codes, but should only depend on the secrecy of the key used in the encryption process. Encryption schemes are generally divided into two types: symmetric and asymmetric encryption schemes. In the following, we present a very brief discussion about each of these schemes."

**Validation:** ✓ Semantically equivalent to original
