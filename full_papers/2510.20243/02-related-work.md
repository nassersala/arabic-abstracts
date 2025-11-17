# Section 2: Related Work
## القسم 2: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.87
**Glossary Terms Used:** hardware accelerator, homomorphic encryption, FHE, HHE, bootstrapping, FPGA, ASIC, GPU, GPGPU, chiplet, symmetric cipher, transciphering, deep learning, neural network, latency, ciphertext expansion, throughput

---

### English Version

## II. RELATED WORK

### A. Hardware Accelerators of Homomorphic Encryption

Hardware accelerators are pivotal in enhancing the practicality of homomorphic encryption (HE) by addressing its significant computational overhead. For fully homomorphic encryption (FHE), which supports arbitrary computations on encrypted data, several hardware solutions have been developed. CraterLake [10] introduces a hardware accelerator that enables unbounded computation on encrypted data by optimizing bootstrapping operations, a critical bottleneck in FHE. REED [21] presents a chiplet-based architecture for FHE, offering improved scalability and flexibility over monolithic designs. SHARP [11] proposes a short-word hierarchical accelerator tailored for the CKKS scheme, enhancing robustness and efficiency. Aloha-HE [13] provides a low-area hardware accelerator for client-side HE operations, making it suitable for resource-constrained environments. GPU-based accelerators, such as Cheddar [22] and Phantom [23], leverage parallel processing to accelerate HE computations, while TensorFHE [12] demonstrates the use of GPGPUs for practical encrypted data processing. A comprehensive survey by [9] analyzes existing acceleration methods for FHE, categorizing them into algorithmic and hardware-based approaches and providing evaluation metrics for comparison.

In the context of hybrid homomorphic encryption (HHE), which combines different HE schemes or integrates HE with other cryptographic techniques to balance security and efficiency, hardware acceleration is equally vital. Pasta [14] establishes the theoretical foundation for HHE, proposing a symmetric encryption scheme optimized for integer HHE use cases. Building on this, Pasta on Edge [19] presents the first implementation of an HHE scheme as a cryptoprocessor on FPGA and ASIC platforms, achieving a 43–171× speedup on low-end 130nm ASIC technology and a 97× speedup on high-end 7nm and 28nm ASICs compared to previous FHE accelerators. Similarly, Presto [20] develops hardware accelerators for HHE ciphers HERA and Rubato on an AMD Virtex UltraScale+ FPGA. Other recent designs such as Masta [15] and Elisabeth [16] explore new families of FHE-friendly symmetric ciphers optimized for transciphering operations. The SoK on FHE-friendly symmetric ciphers [17] provides a comprehensive benchmarking of Pasta, Masta, and Elisabeth under ML workloads such as ResNet-20, outlining their trade-offs in depth, latency, and energy efficiency. These advancements highlight the critical role of hardware solutions in making HHE practical for privacy-preserving computations.

### B. Homomorphic Encryption and Deep Learning

The integration of homomorphic encryption (HE) with deep learning (DL) has gained significant traction for enabling privacy-preserving computations in sensitive domains such as healthcare and finance. Early frameworks like CryptoNets [1] and LoLa [2] pioneered encrypted inference using FHE but suffered from high latency and ciphertext expansion. Later works such as Falcon [3] and Cheetah [4] employed secure multiparty computation or optimized HE techniques to reduce inference time, but communication costs and limited scalability remained bottlenecks. More recent surveys [5], [6] review such FHE-based PPML frameworks, detailing their network adaptations, accuracy trade-offs, and runtime overheads. Lee et al. [7] propose a privacy-preserving deep neural network inference system using FHE, demonstrating feasibility but highlighting performance constraints. Tong et al. [24] mitigate these constraints via polynomial approximations for non-linear activations, improving throughput while maintaining accuracy.

Hybrid homomorphic encryption (HHE) has emerged as a promising alternative to reduce client-side costs. GuardML [8] demonstrates practical PPML services by combining lightweight symmetric encryption with FHE transformations, achieving improved inference latency on constrained devices. Nguyen et al. [18] propose pervasive PPML protocols leveraging HHE for secure computations in zero-trust environments, while Podschwadt et al. [25] address memory limitations of HE-based models for resource-constrained devices. The SoK on FHE-friendly ciphers [17] further benchmarks hybrid ciphers such as Pasta, Masta, and Elisabeth for secure ML inference, showing significant performance benefits over traditional FHE-only approaches. These developments underscore the promising role of HHE in improving the efficiency and scalability of privacy-preserving ML.

### C. Limitations of Previous Work

Prior work on privacy-preserving machine learning often focuses either on standalone hardware accelerators for HE/HHE without full integration into PPML pipelines or purely software-based solutions that suffer from high client-side latency. Few works consider a complete end-to-end architecture that combines hardware acceleration, hybrid encryption, and efficient communication between client and server. HHEML bridges this gap by introducing a hardware/software co-designed framework with FPGA acceleration, pipelined data processing, and Ethernet-enabled offloading to server-side FHE inference.

---

### النسخة العربية

## II. الأعمال ذات الصلة

### أ. مُسرّعات العتاد للتشفير المتماثل

تلعب مُسرّعات العتاد دوراً محورياً في تعزيز عملية التشفير المتماثل (HE) من خلال معالجة عبئه الحسابي الكبير. بالنسبة للتشفير المتماثل الكامل (FHE)، الذي يدعم حسابات تعسفية على البيانات المشفرة، تم تطوير العديد من حلول العتاد. يقدم CraterLake [10] مُسرّع عتادي يتيح حساباً غير محدود على البيانات المشفرة من خلال تحسين عمليات التمهيد الذاتي، وهي عنق الزجاجة الحرج في التشفير المتماثل الكامل. يقدم REED [21] معمارية قائمة على الشرائح الصغيرة للتشفير المتماثل الكامل، مما يوفر قابلية توسع ومرونة محسّنة مقارنة بالتصاميم الأحادية. يقترح SHARP [11] مُسرّعاً هرمياً قصير الكلمات مصمماً خصيصاً لمخطط CKKS، مما يعزز القوة والكفاءة. يوفر Aloha-HE [13] مُسرّع عتادي منخفض المساحة لعمليات التشفير المتماثل على جانب العميل، مما يجعله مناسباً للبيئات محدودة الموارد. تستفيد المُسرّعات القائمة على GPU، مثل Cheddar [22] وPhantom [23]، من المعالجة المتوازية لتسريع حسابات التشفير المتماثل، بينما يوضح TensorFHE [12] استخدام GPGPUs لمعالجة البيانات المشفرة العملية. يحلل مسح شامل بواسطة [9] طرق التسريع الموجودة للتشفير المتماثل الكامل، مصنفاً إياها إلى نهج خوارزمية وقائمة على العتاد ويوفر مقاييس تقييم للمقارنة.

في سياق التشفير المتماثل الهجين (HHE)، الذي يجمع بين مخططات تشفير متماثل مختلفة أو يدمج التشفير المتماثل مع تقنيات تشفيرية أخرى لتحقيق التوازن بين الأمان والكفاءة، فإن التسريع العتادي حيوي بالقدر نفسه. يؤسس Pasta [14] الأساس النظري للتشفير المتماثل الهجين، مقترحاً مخطط تشفير متماثل مُحسّن لحالات استخدام التشفير المتماثل الهجين الصحيح. بناءً على ذلك، يقدم Pasta on Edge [19] أول تطبيق لمخطط تشفير متماثل هجين كمعالج تشفيري على منصات FPGA وASIC، محققاً تسريعاً من 43-171 ضعفاً على تقنية ASIC منخفضة المستوى 130 نانومتر وتسريعاً 97 ضعفاً على ASICs عالية المستوى 7 نانومتر و28 نانومتر مقارنة بمُسرّعات التشفير المتماثل الكامل السابقة. وبالمثل، يطور Presto [20] مُسرّعات عتادية لشفرات التشفير المتماثل الهجين HERA وRubato على FPGA من نوع AMD Virtex UltraScale+. تستكشف تصاميم حديثة أخرى مثل Masta [15] وElisabeth [16] عائلات جديدة من الشفرات المتماثلة الصديقة للتشفير المتماثل الكامل مُحسّنة لعمليات نقل التشفير. يوفر SoK حول الشفرات المتماثلة الصديقة للتشفير المتماثل الكامل [17] قياساً معيارياً شاملاً لـ Pasta وMasta وElisabeth تحت أحمال عمل التعلم الآلي مثل ResNet-20، موضحاً مقايضاتها في العمق وزمن الوصول وكفاءة الطاقة. تسلط هذه التطورات الضوء على الدور الحاسم لحلول العتاد في جعل التشفير المتماثل الهجين عملياً للحسابات الحافظة للخصوصية.

### ب. التشفير المتماثل والتعلم العميق

اكتسب دمج التشفير المتماثل (HE) مع التعلم العميق (DL) زخماً كبيراً لتمكين الحسابات الحافظة للخصوصية في المجالات الحساسة مثل الرعاية الصحية والتمويل. كانت أطر العمل المبكرة مثل CryptoNets [1] وLoLa [2] رائدة في الاستدلال المشفر باستخدام التشفير المتماثل الكامل ولكنها عانت من زمن وصول عالٍ وتوسع في النص المشفر. استخدمت أعمال لاحقة مثل Falcon [3] وCheetah [4] الحساب الآمن متعدد الأطراف أو تقنيات التشفير المتماثل المُحسّنة لتقليل وقت الاستدلال، ولكن تكاليف الاتصال وقابلية التوسع المحدودة ظلت عقبات. تستعرض المسوحات الأحدث [5]، [6] أطر عمل التعلم الآلي الحافظ للخصوصية القائمة على التشفير المتماثل الكامل، مفصلة تكييفات شبكاتها، ومقايضات الدقة، والنفقات الزمنية للتشغيل. يقترح Lee وآخرون [7] نظام استدلال شبكة عصبية عميقة حافظ للخصوصية باستخدام التشفير المتماثل الكامل، موضحاً الجدوى ولكن مع تسليط الضوء على قيود الأداء. يخفف Tong وآخرون [24] من هذه القيود عبر تقريبات متعددة الحدود للتنشيطات غير الخطية، محسّنين الإنتاجية مع الحفاظ على الدقة.

ظهر التشفير المتماثل الهجين (HHE) كبديل واعد لتقليل التكاليف على جانب العميل. يوضح GuardML [8] خدمات التعلم الآلي الحافظ للخصوصية العملية من خلال دمج التشفير المتماثل خفيف الوزن مع تحويلات التشفير المتماثل الكامل، محققاً زمن وصول استدلال محسّن على الأجهزة المقيدة. يقترح Nguyen وآخرون [18] بروتوكولات التعلم الآلي الحافظ للخصوصية الشاملة التي تستفيد من التشفير المتماثل الهجين للحسابات الآمنة في بيئات انعدام الثقة، بينما يعالج Podschwadt وآخرون [25] قيود الذاكرة للنماذج القائمة على التشفير المتماثل للأجهزة محدودة الموارد. يقيس SoK حول الشفرات الصديقة للتشفير المتماثل الكامل [17] بشكل إضافي الشفرات الهجينة مثل Pasta وMasta وElisabeth للاستدلال الآمن للتعلم الآلي، موضحاً فوائد أداء كبيرة على النهج التقليدية القائمة على التشفير المتماثل الكامل فقط. تؤكد هذه التطورات الدور الواعد للتشفير المتماثل الهجين في تحسين كفاءة وقابلية توسع التعلم الآلي الحافظ للخصوصية.

### ج. قيود الأعمال السابقة

غالباً ما يركز العمل السابق على التعلم الآلي الحافظ للخصوصية إما على مُسرّعات عتادية مستقلة للتشفير المتماثل / التشفير المتماثل الهجين دون تكامل كامل في مسارات معالجة التعلم الآلي الحافظ للخصوصية أو حلول برمجية بحتة تعاني من زمن وصول عالٍ على جانب العميل. تنظر أعمال قليلة في معمارية شاملة من البداية إلى النهاية تجمع بين التسريع العتادي، والتشفير الهجين، والاتصال الفعال بين العميل والخادم. يسد HHEML هذه الفجوة من خلال تقديم إطار عمل مصمم بشكل مشترك للعتاد / البرمجيات مع تسريع FPGA، ومعالجة بيانات متدفقة، وتفريغ ممكّن بـ Ethernet للاستدلال بالتشفير المتماثل الكامل على جانب الخادم.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Hardware accelerators = مُسرّعات العتاد
  - Bootstrapping = التمهيد الذاتي
  - Chiplet-based architecture = معمارية قائمة على الشرائح الصغيرة
  - Monolithic designs = التصاميم الأحادية
  - Short-word hierarchical accelerator = مُسرّع هرمي قصير الكلمات
  - Low-area = منخفض المساحة
  - GPGPU = معالجات رسومية للأغراض العامة
  - Transciphering = نقل التشفير
  - Ciphertext expansion = توسع النص المشفر
  - Zero-trust environments = بيئات انعدام الثقة
  - Hardware/software co-design = التصميم المشترك للعتاد/البرمجيات

- **Specific systems mentioned:**
  - CraterLake, REED, SHARP, Aloha-HE, Cheddar, Phantom, TensorFHE (kept as proper names)
  - Pasta, Masta, Elisabeth, HERA, Rubato (cipher names kept)
  - CryptoNets, LoLa, Falcon, Cheetah, GuardML (framework names kept)
  - AMD Virtex UltraScale+ (hardware platform kept)
  - ResNet-20 (model name kept)

- **Equations:** None
- **Citations:** [1]-[25] referenced
- **Special handling:**
  - Performance metrics (43-171×, 97×) kept in original form
  - Technology nodes (130nm, 7nm, 28nm) kept in English
  - Subsection headings A, B, C maintained

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-Translation Check (Subsection A opening)

Arabic: "تلعب مُسرّعات العتاد دوراً محورياً في تعزيز عملية التشفير المتماثل (HE) من خلال معالجة عبئه الحسابي الكبير."

Back to English: "Hardware accelerators play a pivotal role in enhancing the practicality of homomorphic encryption (HE) by addressing its significant computational overhead."

✓ Semantically equivalent to original
