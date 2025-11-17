# Section 6: Evaluation
## القسم 6: التقييم

**Section:** evaluation
**Translation Quality:** 0.87
**Glossary Terms Used:** FPGA, benchmarks, latency, throughput, power consumption, resource utilization, LUTs, FFs, DSP, BRAMs, speedup, MNIST, encryption, decryption, DMA, Ethernet, GuardML

---

### English Version

## VI. EVALUATION

### A. Evaluation Setup

We evaluate HHEML on a Xilinx PYNQ-Z2 FPGA platform equipped with a dual-core ARM Cortex-A9 PS and 650 MHz programmable logic fabric. The client-side accelerator is clocked at 100 MHz, while the server-side computation runs the GuardML framework on an Intel i7-10750H CPU (2.6 GHz) with 16 GB RAM. All hardware designs are synthesized using Vivado 2022.1 with default timing constraints, and DMA drivers are implemented in PYNQ Python APIs for PS–PL data transfer. For all FPGA-based experiments, we use MNIST as the primary dataset (28×28 images), encoded into 784-word plaintext blocks (32-bit words).

The baseline comparison includes:
1) Pasta on Edge – the original FPGA implementation of the Pasta cipher, representing the prior state-of-the-art HHE hardware module without pipelining optimization.
2) GuardML (software) – a pure software implementation of HHE for PPML inference, representative of typical hybrid homomorphic approaches deployed on CPUs.

### B. Results

Table I summarizes the hardware resource utilization and runtime comparison between HHEML and Pasta on Edge. Our design achieves nearly a 2× speedup for end-to-end MNIST encryption while maintaining comparable resource usage on the PYNQ-Z2 device. This improvement stems from introducing a second XOF module that enables parallel keystream generation, effectively reducing the number of permutation rounds required per input batch. Although the addition of an extra XOF module slightly increases logic utilization, the overall power consumption remains comparable to the original design, which was primarily evaluated in an ASIC setting. We argue that this represents a favorable trade-off between performance and resource cost. Furthermore, compared to modern CPU-based PPML solutions deployed on high-power desktop systems (typically consuming 300W or more), our FPGA-based implementation demonstrates significantly lower power requirements while delivering competitive performance.

Table II further quantifies the benefit of the two-XOF pipeline: large plaintext blocks (e.g., MNIST samples) that require 47 rounds under the single-XOF design are reduced to 24 rounds, effectively doubling throughput without algorithmic changes to the Pasta cipher. This optimization is particularly beneficial for machine learning workloads that process high-dimensional input vectors.

Table III evaluates end-to-end latency, including PS–PL DMA transfers and Ethernet communication overhead. Compared to GuardML's software pipeline, HHEML reduces client-side runtime from hundreds of milliseconds to single-digit milliseconds, yielding a >50× latency improvement for LAN deployments. The server-side runtime remains identical since our system reuses GuardML's FHE evaluation stack, but overall system latency drops significantly due to hardware acceleration of symmetric encryption.

Table IV reports the breakdown of end-to-end runtime for the MNIST dataset when using GuardML's software implementation versus the proposed HHEML hardware-accelerated design. The client-side processing time is significantly reduced from 356 ms to 6.5 ms due to offloading symmetric encryption to the FPGA, eliminating the high computational cost of software-based Pasta encryption. The server-side decomposition and homomorphic evaluation phases remain unchanged, as HHEML reuses the same GuardML FHE processing stack. These results highlight that the main performance bottleneck in hybrid homomorphic encryption pipelines resides on the client side, and that hardware acceleration can substantially improve overall responsiveness of privacy-preserving machine learning without requiring modifications to the server-side inference framework.

Overall, HHEML demonstrates that FPGA-based pipelining of Pasta significantly improves the practicality of HHE for PPML. Compared to both software-only frameworks and prior FPGA implementations, our design achieves lower latency, and higher throughput while preserving end-to-end cryptographic security.

---

### النسخة العربية

## VI. التقييم

### أ. إعداد التقييم

نقيّم HHEML على منصة FPGA من نوع Xilinx PYNQ-Z2 مجهزة بنظام معالجة ARM Cortex-A9 ثنائي النواة وبنية منطق قابلة للبرمجة بتردد 650 ميجاهرتز. يعمل المُسرّع على جانب العميل بساعة 100 ميجاهرتز، بينما يشغل الحساب على جانب الخادم إطار عمل GuardML على معالج Intel i7-10750H (2.6 جيجاهرتز) مع ذاكرة وصول عشوائي 16 جيجابايت. يتم تصنيع جميع تصاميم العتاد باستخدام Vivado 2022.1 مع قيود توقيت افتراضية، ويتم تنفيذ برامج تشغيل DMA في واجهات برمجة تطبيقات PYNQ Python لنقل البيانات بين PS وPL. لجميع التجارب القائمة على FPGA، نستخدم MNIST كمجموعة بيانات أولية (صور 28×28)، مشفرة في كتل نص عادي من 784 كلمة (كلمات 32-بت).

تشمل مقارنة خط الأساس:
1) Pasta on Edge - التطبيق الأصلي على FPGA لشفرة Pasta، ممثلاً لوحدة عتاد التشفير المتماثل الهجين الأحدث السابقة دون تحسين المسار المتدفق.
2) GuardML (برمجي) - تطبيق برمجي بحت للتشفير المتماثل الهجين للاستدلال في التعلم الآلي الحافظ للخصوصية، ممثلاً للنهج المتماثلة الهجينة النموذجية المنشورة على وحدات المعالجة المركزية.

### ب. النتائج

يلخص الجدول الأول استخدام موارد العتاد ومقارنة وقت التشغيل بين HHEML وPasta on Edge. يحقق تصميمنا تسريعاً يقارب الضعفين لتشفير MNIST الشامل من البداية إلى النهاية مع الحفاظ على استخدام موارد قابل للمقارنة على جهاز PYNQ-Z2. ينبع هذا التحسين من إدخال وحدة XOF ثانية تتيح توليد تدفق مفاتيح متوازٍ، مما يقلل بشكل فعال عدد جولات التبديل المطلوبة لكل دفعة إدخال. على الرغم من أن إضافة وحدة XOF إضافية تزيد قليلاً من استخدام المنطق، فإن استهلاك الطاقة الإجمالي يظل قابلاً للمقارنة مع التصميم الأصلي، الذي تم تقييمه في المقام الأول في إعداد ASIC. نجادل بأن هذا يمثل مقايضة مواتية بين الأداء وتكلفة الموارد. علاوة على ذلك، مقارنة بحلول التعلم الآلي الحافظ للخصوصية الحديثة القائمة على CPU المنشورة على أنظمة سطح المكتب عالية الطاقة (تستهلك عادةً 300 واط أو أكثر)، يوضح تطبيقنا القائم على FPGA متطلبات طاقة أقل بكثير مع تقديم أداء تنافسي.

يحدد الجدول الثاني بشكل أكبر فائدة مسار XOF الثنائي: كتل النص العادي الكبيرة (مثل عينات MNIST) التي تتطلب 47 جولة في ظل تصميم XOF الأحادي يتم تقليلها إلى 24 جولة، مما يضاعف الإنتاجية بشكل فعال دون تغييرات خوارزمية على شفرة Pasta. هذا التحسين مفيد بشكل خاص لأحمال عمل التعلم الآلي التي تعالج متجهات إدخال عالية الأبعاد.

يقيّم الجدول الثالث زمن الوصول الشامل من البداية إلى النهاية، بما في ذلك عمليات نقل DMA بين PS وPL وعبء اتصال Ethernet. مقارنة بمسار GuardML البرمجي، يقلل HHEML وقت التشغيل على جانب العميل من مئات المللي ثانية إلى مللي ثانية أحادية الرقم، مما ينتج تحسيناً في زمن الوصول يزيد عن 50 ضعفاً لعمليات النشر على LAN. يظل وقت التشغيل على جانب الخادم متطابقاً لأن نظامنا يعيد استخدام مجموعة تقييم التشفير المتماثل الكامل لـ GuardML، ولكن زمن وصول النظام الإجمالي ينخفض بشكل كبير بسبب التسريع العتادي للتشفير المتماثل.

يبلغ الجدول الرابع تفصيل وقت التشغيل الشامل من البداية إلى النهاية لمجموعة بيانات MNIST عند استخدام تطبيق GuardML البرمجي مقابل تصميم HHEML المُسرّع بالعتاد المقترح. يتم تقليل وقت المعالجة على جانب العميل بشكل كبير من 356 مللي ثانية إلى 6.5 مللي ثانية بسبب تفريغ التشفير المتماثل إلى FPGA، مما يلغي التكلفة الحسابية العالية للتشفير القائم على Pasta البرمجي. تظل مراحل التحليل على جانب الخادم والتقييم المتماثل دون تغيير، حيث يعيد HHEML استخدام نفس مجموعة معالجة التشفير المتماثل الكامل لـ GuardML. تسلط هذه النتائج الضوء على أن عنق الزجاجة الأساسي للأداء في مسارات التشفير المتماثل الهجين يقع على جانب العميل، وأن التسريع العتادي يمكن أن يحسن بشكل كبير الاستجابة العامة للتعلم الآلي الحافظ للخصوصية دون الحاجة إلى تعديلات على إطار عمل الاستدلال على جانب الخادم.

بشكل عام، يوضح HHEML أن المسار المتدفق القائم على FPGA لـ Pasta يحسن بشكل كبير عملية التشفير المتماثل الهجين للتعلم الآلي الحافظ للخصوصية. مقارنة بكل من الأطر البرمجية فقط والتطبيقات السابقة على FPGA، يحقق تصميمنا زمن وصول أقل، وإنتاجية أعلى مع الحفاظ على الأمان التشفيري الشامل من البداية إلى النهاية.

---

### Translation Notes

- **Figures referenced:** None
- **Tables referenced:**
  - Table I: Implementation Result
  - Table II: Throughput Improvement from Two-XOF Pipeline
  - Table III: End-to-end PPML latency and communication for HHE Encryption
  - Table IV: End-to-end runtime and communication costs on different datasets

- **Key terms introduced:**
  - Evaluation setup = إعداد التقييم
  - Xilinx PYNQ-Z2 = Xilinx PYNQ-Z2 (platform name kept)
  - ARM Cortex-A9 = ARM Cortex-A9 (processor name kept)
  - Programmable logic fabric = بنية منطق قابلة للبرمجة
  - Intel i7-10750H = Intel i7-10750H (processor kept)
  - Vivado 2022.1 = Vivado 2022.1 (software kept)
  - Timing constraints = قيود توقيت
  - Resource utilization = استخدام الموارد
  - Logic utilization = استخدام المنطق
  - ASIC setting = إعداد ASIC
  - Trade-off = مقايضة
  - LAN deployments = عمليات النشر على LAN
  - DMA transfers = عمليات نقل DMA
  - Ethernet communication = اتصال Ethernet
  - Client-side processing = المعالجة على جانب العميل
  - Server-side decomposition = التحليل على جانب الخادم
  - Performance bottleneck = عنق الزجاجة الأساسي للأداء

- **Equations:** None
- **Citations:** References to Tables I-IV
- **Special handling:**
  - Performance metrics (2×, 47 rounds→24 rounds, >50×, 356ms→6.5ms) kept in original form
  - Platform/hardware names (PYNQ-Z2, ARM Cortex-A9, Intel i7-10750H) kept in English
  - Software names (Vivado, GuardML, Pasta) kept in English
  - Dataset name (MNIST) kept in English
  - Technical specifications (100 MHz, 650 MHz, 2.6 GHz, 16 GB RAM) kept in original form
  - Power consumption (300W) kept in original form

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-Translation Check (Results opening)

Arabic: "يلخص الجدول الأول استخدام موارد العتاد ومقارنة وقت التشغيل بين HHEML وPasta on Edge. يحقق تصميمنا تسريعاً يقارب الضعفين لتشفير MNIST الشامل من البداية إلى النهاية..."

Back to English: "Table I summarizes hardware resource utilization and runtime comparison between HHEML and Pasta on Edge. Our design achieves nearly a 2× speedup for end-to-end MNIST encryption..."

✓ Semantically equivalent to original
