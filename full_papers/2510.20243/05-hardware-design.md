# Section 5: Detail Hardware Design and Optimizations
## القسم 5: تصميم العتاد المفصل والتحسينات

**Section:** hardware-design-optimizations
**Translation Quality:** 0.86
**Glossary Terms Used:** FPGA, ASIC, baseline, XOF, SHAKE, AXI-Stream, FIFO, DMA, Ethernet, pipeline, throughput, latency, round counter, encryption, decryption, data transfer

---

### English Version

## V. DETAIL HARDWARE DESIGN AND OPTIMIZATIONS

The hardware implementation of HHEML consists of several core components derived from the Pasta on Edge design, which serves as our baseline cryptoprocessor architecture for hybrid homomorphic encryption. Leveraging this foundation, we introduce an optimized pipelined permutation pipeline tailored for privacy-preserving machine learning workloads.

### A. Baseline Hardware Flow

We adopt the Pasta-4 specification from the original Pasta on Edge framework, which implements key generation, keystream expansion, and data masking fully in hardware. In their design, a single SHAKE-based XOF module generates the pseudorandom stream used to mask plaintext inputs in 17-word blocks per encryption round (each word 32 bits). An AXI-Stream wrapper orchestrates the flow of data into and out of the Pasta core, while internal FIFOs stage input and output data to balance throughput. This architecture delivers a symmetric encryption accelerator that achieves significant speedups—on the order of 40× to over 100×—compared to CPU baselines on both FPGA and ASIC platforms.

### B. Processing System Design

The Processing System (PS) in HHEML fulfills two essential roles: hardware control and network communication. On the control side, the PS configures DMA engines, issues start and stop signals to the Programmable Logic (PL), and monitors the status of encryption or decryption operations. This lightweight management approach minimizes PS computational overhead while allowing the PL to handle all cryptographic tasks autonomously.

In addition to local control, the PS maintains the communication interface between the FPGA-based client and the remote server. An Ethernet controller integrated into the PS stack manages data transfers over the network, transmitting encrypted feature vectors and their associated symmetric encryption keys (protected under the SE scheme) to the server for transformation into fully homomorphic ciphertexts. The same interface handles receiving the processed results after FHE evaluation, which are then passed to the PL for final decryption.

### C. Programmable Logic Model

Within the PL, the hardware implements the Pasta-4 cipher core following the baseline design, including the SHAKE128-based XOF and the permutation-based masking engine. Input and output FIFOs buffer plain/cipher text streams to accommodate batch transfers via AXI-Stream, preserving high throughput even when transient stalls occur. Both encryption and decryption modules share the same AXI-Stream wrapper and FIFO interface, simplifying control logic and reuse of buffers. A centralized round counter ensures correct sequencing of XOF rounds and block alignment throughout the pipeline.

### D. Data Transfer

Data movement between PS and PL is handled via AXI4-Stream interfaces linked to DMA controllers, enabling high-throughput packet transfers. Incoming plaintext data is streamed into PL in contiguous blocks, buffered in the input FIFO and then consumed by the Pasta core. Processed ciphertext is similarly queued in the output FIFO and transferred back to PS. This DMA-based, FIFO-buffered design minimizes PS-side data staging and avoids processing stalls, even during large ML workloads such as batch-encryption of image datasets.

### E. Pipeline Optimization

Building on the baseline, HHEML introduces a two-XOF module pipeline to greatly improve throughput for large data encryption. The entire design is shown in Fig. 4. In contrast to the single-module design in Pasta on Edge, our architecture replicates the SHAKE128 XOF block, allowing parallel mask generation over interleaved data streams. A centralized scheduler (round counter) dynamically assigns input words to one of two XOF modules in alternating fashion, driving both units concurrently. This architectural enhancement effectively halves the number of encryption rounds required for large inputs (e.g., MNIST images), reducing latency even though the fundamental core logic remains unchanged.

Such pipelining allows simultaneous execution of independent keystream generation tasks, leveraging parallelism to boost throughput without altering the core permutation logic. Importantly, because both XOF modules share the same seed and round schedule, synchronization remains straightforward via the centralized control logic. While the detailed synthesis results and resource trade-offs will be discussed in Section VI, the design preserves correctness by maintaining ordered output and eliminating data interleaving artifacts.

By combining the Pasta on Edge baseline with this pipelined XOF architecture, HHEML achieves significantly higher encryption throughput with minimal overhead in PL resource use, making it well-suited for PPML tasks on edge devices.

---

### النسخة العربية

## V. تصميم العتاد المفصل والتحسينات

يتكون التطبيق العتادي لـ HHEML من عدة مكونات أساسية مشتقة من تصميم Pasta on Edge، الذي يعمل كمعمارية معالج تشفيري أساسية للتشفير المتماثل الهجين. بالاستفادة من هذا الأساس، نقدم مسار تبديل متدفق مُحسّن مصمم خصيصاً لأحمال عمل التعلم الآلي الحافظ للخصوصية.

### أ. تدفق العتاد الأساسي

نعتمد مواصفات Pasta-4 من إطار عمل Pasta on Edge الأصلي، الذي ينفذ توليد المفاتيح، وتوسيع تدفق المفاتيح، وإخفاء البيانات بالكامل في العتاد. في تصميمهم، تولد وحدة XOF واحدة قائمة على SHAKE التدفق الزائف العشوائي المستخدم لإخفاء مدخلات النص العادي في كتل من 17 كلمة لكل جولة تشفير (كل كلمة 32 بت). يُنسق غلاف AXI-Stream تدفق البيانات داخل وخارج نواة Pasta، بينما تنظم FIFOs الداخلية بيانات الإدخال والإخراج لتحقيق التوازن في الإنتاجية. توفر هذه المعمارية مُسرّع تشفير متماثل يحقق تسريعات كبيرة - بمقدار 40 ضعفاً إلى أكثر من 100 ضعف - مقارنة بخطوط الأساس على CPU على منصات FPGA وASIC.

### ب. تصميم نظام المعالجة

يؤدي نظام المعالجة (PS) في HHEML دورين أساسيين: التحكم في العتاد والاتصال بالشبكة. على جانب التحكم، يقوم PS بتكوين محركات DMA، وإصدار إشارات البدء والإيقاف للمنطق القابل للبرمجة (PL)، ومراقبة حالة عمليات التشفير أو فك التشفير. يقلل نهج الإدارة الخفيف الوزن هذا من العبء الحسابي لـ PS بينما يسمح لـ PL بالتعامل مع جميع المهام التشفيرية بشكل مستقل.

بالإضافة إلى التحكم المحلي، يحافظ PS على واجهة الاتصال بين العميل القائم على FPGA والخادم البعيد. يدير متحكم Ethernet متكامل في مجموعة PS عمليات نقل البيانات عبر الشبكة، وإرسال متجهات الميزات المشفرة ومفاتيح التشفير المتماثل المرتبطة بها (المحمية تحت مخطط SE) إلى الخادم للتحويل إلى نصوص مشفرة متماثلة كاملة. تتعامل نفس الواجهة مع استقبال النتائج المعالجة بعد تقييم FHE، والتي تُمرر بعد ذلك إلى PL لفك التشفير النهائي.

### ج. نموذج المنطق القابل للبرمجة

داخل PL، ينفذ العتاد نواة شفرة Pasta-4 وفقاً للتصميم الأساسي، بما في ذلك XOF القائم على SHAKE128 ومحرك الإخفاء القائم على التبديل. تخزن FIFOs الإدخال والإخراج تدفقات النص العادي / المشفر مؤقتاً لاستيعاب عمليات النقل الدفعي عبر AXI-Stream، مع الحفاظ على إنتاجية عالية حتى عند حدوث توقفات مؤقتة. تشترك وحدات التشفير وفك التشفير في نفس غلاف AXI-Stream وواجهة FIFO، مما يبسط منطق التحكم وإعادة استخدام المخازن المؤقتة. يضمن عداد جولة مركزي تسلسلاً صحيحاً لجولات XOF ومحاذاة الكتل في جميع أنحاء المسار.

### د. نقل البيانات

يتم التعامل مع حركة البيانات بين PS وPL عبر واجهات AXI4-Stream المرتبطة بمتحكمات DMA، مما يتيح نقل حزم عالي الإنتاجية. يتم بث بيانات النص العادي الواردة إلى PL في كتل متجاورة، مخزنة مؤقتاً في FIFO الإدخال ثم تستهلكها نواة Pasta. يتم تخزين النص المشفر المعالج بالمثل في FIFO الإخراج ونقله مرة أخرى إلى PS. يقلل هذا التصميم القائم على DMA والمخزن مؤقتاً بـ FIFO من تنظيم البيانات على جانب PS ويتجنب توقفات المعالجة، حتى أثناء أحمال عمل التعلم الآلي الكبيرة مثل التشفير الدفعي لمجموعات بيانات الصور.

### هـ. تحسين المسار المتدفق

بناءً على الأساس، يقدم HHEML مساراً من وحدتي XOF لتحسين الإنتاجية بشكل كبير لتشفير البيانات الكبيرة. يظهر التصميم الكامل في الشكل 4. على النقيض من التصميم أحادي الوحدة في Pasta on Edge، تكرر معماريتنا كتلة XOF من SHAKE128، مما يتيح توليد أقنعة متوازية على تدفقات بيانات متشابكة. يخصص جدول مركزي (عداد جولة) كلمات الإدخال بشكل ديناميكي إلى واحدة من وحدتي XOF بطريقة متناوبة، مما يقود كلا الوحدتين بشكل متزامن. يقلل هذا التحسين المعماري بشكل فعال عدد جولات التشفير المطلوبة للمدخلات الكبيرة (مثل صور MNIST) إلى النصف، مما يقلل زمن الوصول حتى لو ظل منطق النواة الأساسي دون تغيير.

يسمح هذا التدفق بالتنفيذ المتزامن لمهام توليد تدفق المفاتيح المستقلة، مستفيداً من التوازي لتعزيز الإنتاجية دون تغيير منطق التبديل الأساسي. والأهم من ذلك، نظراً لأن كلتا وحدتي XOF تشتركان في نفس البذرة وجدول الجولات، يظل التزامن واضحاً عبر منطق التحكم المركزي. في حين سيتم مناقشة نتائج التركيب المفصلة والمقايضات في الموارد في القسم السادس، يحافظ التصميم على الصحة من خلال الحفاظ على إخراج مرتب والقضاء على تحف تشابك البيانات.

من خلال دمج خط الأساس Pasta on Edge مع معمارية XOF المتدفقة هذه، يحقق HHEML إنتاجية تشفير أعلى بكثير مع الحد الأدنى من العبء في استخدام موارد PL، مما يجعله مناسباً تماماً لمهام التعلم الآلي الحافظ للخصوصية على أجهزة الحافة.

---

### Translation Notes

- **Figures referenced:** Fig. 4 (XOF pipeline design)
- **Key terms introduced:**
  - Baseline = خط الأساس
  - Cryptoprocessor = معالج تشفيري
  - Pipelined permutation = تبديل متدفق
  - SHAKE-based XOF = XOF القائم على SHAKE
  - Pseudorandom stream = تدفق زائف عشوائي
  - Data masking = إخفاء البيانات
  - Speedups = تسريعات
  - Ethernet controller = متحكم Ethernet
  - Masking engine = محرك الإخفاء
  - Buffer = مخزن مؤقت
  - Transient stalls = توقفات مؤقتة
  - Round counter = عداد جولة
  - Block alignment = محاذاة الكتل
  - Contiguous blocks = كتل متجاورة
  - Packet transfers = نقل حزم
  - Batch-encryption = تشفير دفعي
  - Two-XOF module pipeline = مسار من وحدتي XOF
  - Interleaved data streams = تدفقات بيانات متشابكة
  - Centralized scheduler = جدول مركزي
  - Data interleaving artifacts = تحف تشابك البيانات

- **Equations:** None
- **Citations:** References to Section VI
- **Special handling:**
  - Technical terms (SHAKE128, AXI-Stream, FIFO, DMA) kept where appropriate
  - Performance metrics (40×, 100×, halves) kept in original form
  - Subsection headings A through E maintained
  - Word size (17-word blocks, 32 bits) kept in original

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86

### Back-Translation Check (Pipeline Optimization opening)

Arabic: "بناءً على الأساس، يقدم HHEML مساراً من وحدتي XOF لتحسين الإنتاجية بشكل كبير لتشفير البيانات الكبيرة."

Back to English: "Building on the baseline, HHEML introduces a two-XOF module pipeline to significantly improve throughput for large data encryption."

✓ Semantically equivalent to original
