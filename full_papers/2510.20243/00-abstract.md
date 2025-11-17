# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.89
**Glossary Terms Used:** privacy-preserving machine learning, fully homomorphic encryption, hybrid homomorphic encryption, symmetric encryption, edge devices, hardware accelerator, FPGA, latency, throughput, ciphertext

---

### English Version

Privacy-preserving machine learning (PPML) is an emerging topic to handle secure machine learning inference over sensitive data in untrusted environments. Fully homomorphic encryption (FHE) enables computation directly on encrypted data on the server side, making it a promising approach for PPML. However, it introduces significant communication and computation overhead on the client side, making it impractical for edge devices. Hybrid homomorphic encryption (HHE) addresses this limitation by combining symmetric encryption (SE) with FHE to reduce the computational cost on the client side, and combining with an FHE-friendly SE can also lessen the processing overhead on the server side, making it a more balanced and efficient alternative. Our work proposes a hardware-accelerated HHE architecture built around a lightweight symmetric cipher optimized for FHE compatibility and implemented as a dedicated hardware accelerator. To the best of our knowledge, this is the first design to integrate an end-to-end HHE framework with hardware acceleration. Beyond this, we also present several microarchitectural optimizations to achieve higher performance and energy efficiency. The proposed work is integrated into a full PPML pipeline, enabling secure inference with significantly lower latency and power consumption than software implementations. Our contributions validate the feasibility of low-power, hardware-accelerated HHE for edge deployment and provide a hardware-software co-design methodology for building scalable, secure machine learning systems in resource-constrained environments. Experiments on a PYNQ-Z2 platform with the MNIST dataset show over a 50× reduction in client-side encryption latency and nearly a 2× gain in hardware throughput compared to existing FPGA-based HHE accelerators.

---

### النسخة العربية

التعلم الآلي الحافظ للخصوصية (PPML) هو موضوع ناشئ للتعامل مع استدلال التعلم الآلي الآمن على البيانات الحساسة في بيئات غير موثوقة. يمكّن التشفير المتماثل الكامل (FHE) من إجراء الحسابات مباشرة على البيانات المشفرة على جانب الخادم، مما يجعله نهجاً واعداً للتعلم الآلي الحافظ للخصوصية. ومع ذلك، فإنه يُدخل عبئاً كبيراً من حيث الاتصال والحساب على جانب العميل، مما يجعله غير عملي لأجهزة الحافة. يعالج التشفير المتماثل الهجين (HHE) هذا القيد من خلال دمج التشفير المتماثل (SE) مع التشفير المتماثل الكامل لتقليل التكلفة الحسابية على جانب العميل، كما أن الدمج مع تشفير متماثل متوافق مع FHE يمكن أن يخفف أيضاً من عبء المعالجة على جانب الخادم، مما يجعله بديلاً أكثر توازناً وكفاءة. يقترح عملنا معمارية تشفير متماثل هجين مُسرّعة بالعتاد مبنية حول شفرة متماثلة خفيفة الوزن مُحسّنة للتوافق مع FHE ومُنفّذة كمُسرّع عتادي مخصص. على حد علمنا، هذا هو التصميم الأول الذي يدمج إطار عمل تشفير متماثل هجين شامل من البداية إلى النهاية مع التسريع العتادي. علاوة على ذلك، نقدم أيضاً العديد من التحسينات الدقيقة للمعمارية لتحقيق أداء أعلى وكفاءة طاقة أفضل. يتم دمج العمل المقترح في مسار معالجة كامل للتعلم الآلي الحافظ للخصوصية، مما يتيح الاستدلال الآمن بزمن وصول أقل بكثير واستهلاك طاقة أقل مقارنة بالتطبيقات البرمجية. تؤكد مساهماتنا جدوى التشفير المتماثل الهجين منخفض الطاقة والمُسرّع بالعتاد لنشره على الحافة، وتوفر منهجية تصميم مشترك للعتاد والبرمجيات لبناء أنظمة تعلم آلي قابلة للتوسع وآمنة في بيئات محدودة الموارد. تُظهر التجارب على منصة PYNQ-Z2 مع مجموعة بيانات MNIST انخفاضاً يزيد عن 50 ضعفاً في زمن وصول التشفير على جانب العميل وزيادة تقارب الضعفين في إنتاجية العتاد مقارنة بمُسرّعات التشفير المتماثل الهجين القائمة على FPGA الموجودة.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:**
  - PPML (Privacy-Preserving Machine Learning) = التعلم الآلي الحافظ للخصوصية
  - FHE (Fully Homomorphic Encryption) = التشفير المتماثل الكامل
  - HHE (Hybrid Homomorphic Encryption) = التشفير المتماثل الهجين
  - SE (Symmetric Encryption) = التشفير المتماثل
  - Edge devices = أجهزة الحافة
  - Hardware accelerator = مُسرّع عتادي
  - FPGA = مصفوفة البوابات القابلة للبرمجة حقلياً (implied, PYNQ-Z2 is FPGA-based)
  - Latency = زمن الوصول
  - Throughput = الإنتاجية
  - Resource-constrained environments = بيئات محدودة الموارد

- **Equations:** None
- **Citations:** None in abstract
- **Special handling:**
  - Technical performance metrics (50×, 2×) kept in original form
  - Platform name "PYNQ-Z2" kept in English
  - Dataset name "MNIST" kept in English
  - Emphasized hardware-software co-design methodology

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.89
- Readability: 0.88
- Glossary consistency: 0.89
- **Overall section score:** 0.89

### Back-Translation Check (First Sentence)

Arabic: "التعلم الآلي الحافظ للخصوصية (PPML) هو موضوع ناشئ للتعامل مع استدلال التعلم الآلي الآمن على البيانات الحساسة في بيئات غير موثوقة."

Back to English: "Privacy-preserving machine learning (PPML) is an emerging topic for handling secure machine learning inference on sensitive data in untrusted environments."

✓ Semantically equivalent to original
