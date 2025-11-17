# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** machine learning, privacy-preserving, fully homomorphic encryption, differential privacy, garbled circuits, secure multi-party computation, ciphertext, edge devices, IoT, hybrid homomorphic encryption, symmetric encryption, FPGA, computational overhead

---

### English Version

Contemporary machine learning (ML) workloads often involve handling sensitive datasets, such as personal health information, biometric authentication data, confidential business analytics, and sensitive financial records [1], [2]. The delivery of ML as a cloud-based or remote inference service necessitates transferring raw data inputs, intermediate representations, or model parameters beyond the direct control of the original data custodians. This inherently poses substantial risks, ranging from accidental exposure to intentional misuse [3], [4]. To effectively mitigate these concerns, the research community has increasingly concentrated efforts on privacy-preserving machine learning (PPML) [5], [6], a field dedicated to maintaining data confidentiality while preserving the full functionality of ML algorithms.

Privacy-preserving machine learning (PPML) encompasses several prominent techniques, notably fully homomorphic encryption (FHE) [1], [7], differential privacy (DP), and secure multi-party computation based on garbled circuits (GC) [4]. Among these methods, FHE is distinguished by its robust security model, enabling arbitrary computations directly on encrypted data without any intermediate decryption [5], [6]. In a typical FHE-based PPML workflow, the client locally encrypts sensitive input data before transmitting the ciphertexts to an untrusted computation server. This server performs inference or training entirely within the encrypted domain, returning encrypted results that can only be decrypted by the client, who exclusively holds the corresponding secret key.

Compared to alternative PPML methods, FHE provides end-to-end cryptographic security without compromising data accuracy or necessitating intensive communication [7]. In contrast, DP ensures privacy through calibrated statistical noise injection, inherently sacrificing precision [6]. Likewise, GC-based methods require frequent interactions among multiple parties, thus limiting practicality in scenarios characterized by unreliable or slow network connections [4]. Conversely, FHE-based solutions are inherently non-interactive, involve only a single communication exchange per computation task, and demonstrate robustness under conditions of high latency or intermittent connectivity [1], [2]. These advantages make FHE particularly well-suited to Internet-of-Things (IoT) deployments, where devices often face resource limitations, heterogeneity, and unstable connections while simultaneously requiring rigorous data privacy protection [8].

Although FHE stands out among existing PPML methods in IoT scenarios, its practical deployment remains challenging. Prominent FHE schemes, such as Brakerski-Gentry-Vaikuntanathan (BGV), Brakerski/Fan-Vercauteren (BFV), Cheon-Kim-Kim-Song (CKKS), Fully Homomorphic Encryption over the Torus (FHEW), and Torus Fully Homomorphic Encryption (TFHE) [5], typically involve significant computational overhead and extensive memory usage. Each critical phase, including plaintext encoding, encryption, and homomorphic evaluation, demands substantial computational resources, and ciphertexts impose orders-of-magnitude overhead compared to conventional symmetric encryption. While recent advances in algorithms and optimized implementations have progressively improved the performance of FHE schemes [9]–[12], the inherent complexity continues to be prohibitive for ultra-low-power IoT devices that possess limited computational capability, constrained memory, and strict energy budgets [13].

To address these practical challenges, hybrid homomorphic encryption (HHE) has emerged as a promising alternative [14]–[17]. The HHE-based PPML system model is shown in Fig. 1. HHE integrates efficient symmetric encryption methods, typically lightweight block ciphers, with the algebraically rich capabilities of FHE. This strategic combination enables end-to-end secure computation while significantly reducing ciphertext expansion and computational overhead [8], [18]. Consequently, HHE is particularly advantageous for edge computing scenarios, where performance, bandwidth, and energy constraints must be carefully balanced against rigorous data privacy requirements [19], [20].

In light of the limitations associated with classical FHE in edge computing scenarios, we propose HHEML, a hardware accelerated framework for HHE tailored to PPML on resource constrained devices. Built upon the Pasta encryption scheme [14], [19], which combines symmetric encryption with homomorphic compatibility, HHEML is designed to reduce latency and energy consumption at the client side. To further alleviate communication overhead between software and hardware components, we implement a streamlined data transfer pipeline that leverages processing system to programmable logic (PS to PL) communication and a lightweight Ethernet-based protocol for exchanging encrypted data with a remote server.

The first contribution of this work is the development of an end-to-end hardware acceleration framework compatible with FHE, implemented on the PYNQ-Z2 FPGA [19]. The system includes a dedicated module for symmetric encryption, such as Advanced Encryption Standard (AES) [9], a high bandwidth PS to PL AXI interface, and a communication layer based on Ethernet for transferring ciphertexts. This configuration allows for efficient data encryption at the edge, followed by secure transformation into FHE ciphertext for remote inference or training.

The second contribution targets the server-side cost of transforming symmetric encryption ciphertexts into FHE format. To address this, we adopt the Pasta cipher [14], which preserves algebraic structure during encryption and is optimized for homomorphic applications. We develop a custom hardware module to offload these operations from the server software, thereby improving transformation efficiency and reducing overall processing delay in the PPML pipeline [8].

The third contribution is the integration of HHEML into a complete PPML inference pipeline and a detailed evaluation of its performance. We validate the system on representative benchmarks and demonstrate substantial improvements in throughput and power efficiency when compared with software-only FHE baselines [1], [2], [8]. These results underscore the feasibility and impact of hardware accelerated HHE in real world edge computing environments [20].

The main contributions of this work are summarized as follows:
• The design of an FPGA-based HHE acceleration framework that integrates symmetric encryption and FHE compatibility for edge devices.
• A hardware implementation of the Pasta cipher for efficient ciphertext transformation at the server side.
• A system-level evaluation within a PPML pipeline, demonstrating improved throughput and energy efficiency over conventional approaches.

---

### النسخة العربية

غالباً ما تتضمن أحمال عمل التعلم الآلي (ML) المعاصرة التعامل مع مجموعات بيانات حساسة، مثل المعلومات الصحية الشخصية، وبيانات المصادقة البيومترية، والتحليلات التجارية السرية، والسجلات المالية الحساسة [1]، [2]. يتطلب تقديم التعلم الآلي كخدمة سحابية أو خدمة استدلال عن بُعد نقل مدخلات البيانات الأولية، أو التمثيلات الوسيطة، أو معاملات النموذج خارج السيطرة المباشرة للقائمين على البيانات الأصليين. وهذا يشكل بطبيعته مخاطر كبيرة، تتراوح من التعرض العرضي إلى سوء الاستخدام المتعمد [3]، [4]. للتخفيف من هذه المخاوف بشكل فعال، ركز مجتمع البحث بشكل متزايد الجهود على التعلم الآلي الحافظ للخصوصية (PPML) [5]، [6]، وهو مجال مكرس للحفاظ على سرية البيانات مع الحفاظ على الوظائف الكاملة لخوارزميات التعلم الآلي.

يشمل التعلم الآلي الحافظ للخصوصية (PPML) العديد من التقنيات البارزة، ولا سيما التشفير المتماثل الكامل (FHE) [1]، [7]، والخصوصية التفاضلية (DP)، والحساب متعدد الأطراف الآمن القائم على الدوائر المشوشة (GC) [4]. من بين هذه الطرق، يتميز التشفير المتماثل الكامل بنموذج أمان قوي، مما يتيح إجراء حسابات تعسفية مباشرة على البيانات المشفرة دون أي فك تشفير وسيط [5]، [6]. في مسار عمل نموذجي للتعلم الآلي الحافظ للخصوصية القائم على FHE، يقوم العميل بتشفير البيانات الحساسة المدخلة محلياً قبل إرسال النصوص المشفرة إلى خادم حساب غير موثوق. يقوم هذا الخادم بتنفيذ الاستدلال أو التدريب بالكامل ضمن النطاق المشفر، ويعيد النتائج المشفرة التي لا يمكن فك تشفيرها إلا من قبل العميل، الذي يحتفظ حصرياً بالمفتاح السري المقابل.

مقارنة بطرق التعلم الآلي الحافظ للخصوصية البديلة، يوفر التشفير المتماثل الكامل أماناً تشفيرياً شاملاً من البداية إلى النهاية دون المساس بدقة البيانات أو الحاجة إلى اتصال مكثف [7]. في المقابل، تضمن الخصوصية التفاضلية الخصوصية من خلال حقن ضوضاء إحصائية معايرة، مما يضحي بطبيعته بالدقة [6]. وبالمثل، تتطلب الطرق القائمة على الدوائر المشوشة تفاعلات متكررة بين أطراف متعددة، وبالتالي تحد من العملية في السيناريوهات التي تتميز باتصالات شبكة غير موثوقة أو بطيئة [4]. على العكس من ذلك، فإن الحلول القائمة على التشفير المتماثل الكامل غير تفاعلية بطبيعتها، وتتضمن تبادل اتصال واحد فقط لكل مهمة حساب، وتظهر قوة في ظروف زمن الوصول المرتفع أو الاتصال المتقطع [1]، [2]. تجعل هذه المزايا التشفير المتماثل الكامل مناسباً بشكل خاص لعمليات نشر إنترنت الأشياء (IoT)، حيث غالباً ما تواجه الأجهزة قيود الموارد، وعدم التجانس، والاتصالات غير المستقرة بينما تتطلب في الوقت نفسه حماية صارمة لخصوصية البيانات [8].

على الرغم من أن التشفير المتماثل الكامل يبرز بين طرق التعلم الآلي الحافظ للخصوصية الموجودة في سيناريوهات إنترنت الأشياء، إلا أن نشره العملي يظل صعباً. تتضمن مخططات التشفير المتماثل الكامل البارزة، مثل Brakerski-Gentry-Vaikuntanathan (BGV)، وBrakerski/Fan-Vercauteren (BFV)، وCheon-Kim-Kim-Song (CKKS)، والتشفير المتماثل الكامل على الطارة (FHEW)، والتشفير المتماثل الكامل للطارة (TFHE) [5]، عادةً عبئاً حسابياً كبيراً واستخداماً واسعاً للذاكرة. تتطلب كل مرحلة حرجة، بما في ذلك ترميز النص العادي، والتشفير، والتقييم المتماثل، موارد حسابية كبيرة، وتفرض النصوص المشفرة عبئاً يفوق بعدة مرات التشفير المتماثل التقليدي. في حين أن التطورات الحديثة في الخوارزميات والتطبيقات المُحسّنة قد حسّنت تدريجياً أداء مخططات التشفير المتماثل الكامل [9]–[12]، فإن التعقيد الكامن يستمر في أن يكون محظوراً لأجهزة إنترنت الأشياء منخفضة الطاقة للغاية التي تمتلك قدرة حسابية محدودة، وذاكرة مقيدة، وميزانيات طاقة صارمة [13].

لمعالجة هذه التحديات العملية، ظهر التشفير المتماثل الهجين (HHE) كبديل واعد [14]–[17]. يظهر نموذج نظام التعلم الآلي الحافظ للخصوصية القائم على HHE في الشكل 1. يدمج التشفير المتماثل الهجين طرق التشفير المتماثل الفعالة، عادةً الشفرات الكتلية خفيفة الوزن، مع القدرات الجبرية الغنية للتشفير المتماثل الكامل. يمكّن هذا المزيج الاستراتيجي من الحساب الآمن الشامل من البداية إلى النهاية مع تقليل توسع النص المشفر والعبء الحسابي بشكل كبير [8]، [18]. وبالتالي، فإن التشفير المتماثل الهجين مفيد بشكل خاص لسيناريوهات الحوسبة على الحافة، حيث يجب موازنة الأداء وعرض النطاق الترددي وقيود الطاقة بعناية مقابل متطلبات خصوصية البيانات الصارمة [19]، [20].

في ضوء القيود المرتبطة بالتشفير المتماثل الكامل الكلاسيكي في سيناريوهات الحوسبة على الحافة، نقترح HHEML، وهو إطار عمل مُسرّع بالعتاد للتشفير المتماثل الهجين مصمم للتعلم الآلي الحافظ للخصوصية على الأجهزة محدودة الموارد. بناءً على مخطط تشفير Pasta [14]، [19]، الذي يجمع بين التشفير المتماثل والتوافق المتماثل، تم تصميم HHEML لتقليل زمن الوصول واستهلاك الطاقة على جانب العميل. لتخفيف عبء الاتصال بشكل أكبر بين مكونات البرمجيات والعتاد، نطبق مسار نقل بيانات مبسط يستفيد من اتصال نظام المعالجة إلى المنطق القابل للبرمجة (PS إلى PL) وبروتوكول خفيف الوزن قائم على Ethernet لتبادل البيانات المشفرة مع خادم عن بُعد.

المساهمة الأولى لهذا العمل هي تطوير إطار عمل تسريع عتادي شامل من البداية إلى النهاية متوافق مع التشفير المتماثل الكامل، مُنفّذ على FPGA من نوع PYNQ-Z2 [19]. يتضمن النظام وحدة مخصصة للتشفير المتماثل، مثل معيار التشفير المتقدم (AES) [9]، وواجهة AXI عالية النطاق الترددي من PS إلى PL، وطبقة اتصال قائمة على Ethernet لنقل النصوص المشفرة. يسمح هذا التكوين بتشفير بيانات فعال على الحافة، يليه تحويل آمن إلى نص مشفر FHE للاستدلال أو التدريب عن بُعد.

تستهدف المساهمة الثانية تكلفة جانب الخادم لتحويل نصوص التشفير المتماثل إلى صيغة التشفير المتماثل الكامل. لمعالجة هذا، نعتمد شفرة Pasta [14]، التي تحافظ على البنية الجبرية أثناء التشفير ومُحسّنة للتطبيقات المتماثلة. نطور وحدة عتادية مخصصة لتفريغ هذه العمليات من برمجيات الخادم، وبالتالي تحسين كفاءة التحويل وتقليل تأخير المعالجة الإجمالي في مسار معالجة التعلم الآلي الحافظ للخصوصية [8].

المساهمة الثالثة هي دمج HHEML في مسار استدلال كامل للتعلم الآلي الحافظ للخصوصية وتقييم مفصل لأدائه. نتحقق من صحة النظام على معايير تمثيلية ونوضح تحسينات كبيرة في الإنتاجية وكفاءة الطاقة عند المقارنة مع خطوط أساس للتشفير المتماثل الكامل البرمجية فقط [1]، [2]، [8]. تؤكد هذه النتائج جدوى وتأثير التشفير المتماثل الهجين المُسرّع بالعتاد في بيئات الحوسبة على الحافة في العالم الحقيقي [20].

يمكن تلخيص المساهمات الرئيسية لهذا العمل على النحو التالي:
• تصميم إطار عمل تسريع للتشفير المتماثل الهجين قائم على FPGA يدمج التشفير المتماثل والتوافق مع التشفير المتماثل الكامل لأجهزة الحافة.
• تطبيق عتادي لشفرة Pasta لتحويل فعال للنص المشفر على جانب الخادم.
• تقييم على مستوى النظام ضمن مسار معالجة للتعلم الآلي الحافظ للخصوصية، يوضح إنتاجية محسّنة وكفاءة طاقة أعلى مقارنة بالنهج التقليدية.

---

### Translation Notes

- **Figures referenced:** Fig. 1 (HHE-based PPML system model)
- **Key terms introduced:**
  - PPML (Privacy-Preserving Machine Learning) = التعلم الآلي الحافظ للخصوصية
  - FHE schemes: BGV, BFV, CKKS, FHEW, TFHE (kept as acronyms)
  - Differential Privacy (DP) = الخصوصية التفاضلية
  - Garbled Circuits (GC) = الدوائر المشوشة
  - IoT (Internet of Things) = إنترنت الأشياء
  - HHE (Hybrid Homomorphic Encryption) = التشفير المتماثل الهجين
  - Pasta cipher = شفرة Pasta (proper name kept)
  - PYNQ-Z2 FPGA = FPGA من نوع PYNQ-Z2
  - PS to PL = نظام المعالجة إلى المنطق القابل للبرمجة
  - AES (Advanced Encryption Standard) = معيار التشفير المتقدم
  - AXI interface = واجهة AXI (technical term kept)

- **Equations:** None
- **Citations:** [1]-[20] referenced throughout
- **Special handling:**
  - Technical acronyms (BGV, BFV, CKKS, FHEW, TFHE) kept in English
  - Platform names (PYNQ-Z2, Ethernet) kept in English
  - Proper names (Pasta, Brakerski, Gentry, etc.) kept in English
  - Three main contributions formatted as bullet points

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88

### Back-Translation Check (Opening Paragraph)

Arabic: "غالباً ما تتضمن أحمال عمل التعلم الآلي (ML) المعاصرة التعامل مع مجموعات بيانات حساسة، مثل المعلومات الصحية الشخصية، وبيانات المصادقة البيومترية..."

Back to English: "Contemporary machine learning (ML) workloads often involve dealing with sensitive datasets, such as personal health information, biometric authentication data..."

✓ Semantically equivalent to original
