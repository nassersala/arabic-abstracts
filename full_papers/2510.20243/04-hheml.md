# Section 4: HHEML
## القسم 4: HHEML

**Section:** hheml
**Translation Quality:** 0.87
**Glossary Terms Used:** FPGA, processing system, programmable logic, AXI-Stream, DMA, FIFO, Pasta cipher, GuardML, encryption, decryption, ciphertext, plaintext, hardware accelerator, pipeline, datapath

---

### English Version

## IV. HHEML

### A. System Overview

The proposed HHEML framework, shown in Fig. 2, is composed of two tightly integrated parts: a client implemented on a PYNQ-Z2 FPGA and a server executing the GuardML-based homomorphic evaluation stack. On the client, the Programmable Logic (PL) contains a hardware accelerator derived from the Pasta on Edge design and extended to support full hybrid homomorphic encryption. Key generation, symmetric encryption, and decryption are performed entirely in hardware within a unified pipeline, removing dependence on software for latency-sensitive cryptographic operations. The Processing System (PS) handles high-level orchestration, including configuration and data scheduling, and communicates with the PL via an AXI4-Stream interface with DMA support for bulk data transfers, while control and status information are exchanged through AXI-Lite.

The processing workflow starts with plaintext inputs, such as feature vectors from edge ML applications, collected by the PS and transferred to the PL accelerator. Using the Pasta cipher, the PL rapidly encrypts the data, generating ciphertexts that are directly compatible with subsequent transformation into fully homomorphic encryption (FHE) form. These ciphertexts are sent to the server through an Ethernet link, where GuardML converts them into FHE ciphertexts and performs encrypted inference on the target model. The evaluated results are then re-encoded as symmetric ciphertexts, transmitted back to the client, and decrypted in hardware to produce the final predictions.

A key architectural feature of HHEML is the use of a pipelined datapath in the PL accelerator. By reorganizing keystream generation and data masking operations, the hardware can process multiple input blocks in parallel, minimizing latency for large datasets such as batched image inputs. This improvement enhances client-side performance while maintaining seamless integration with the GuardML software stack.

Fig. 3 provides an overview of this end-to-end workflow, illustrating data movement from initial plaintext capture on the client, through hardware-based encryption and network transmission, to server-side FHE evaluation, and finally secure decryption on the FPGA client.

### B. Modules in HHEML

The HHEML framework operates primarily on the client side, instantiated as a tightly coupled Processing System (PS) and Programmable Logic (PL) design on the PYNQ-Z2 FPGA platform. The PL hosts a hardware implementation of the Pasta cipher based on the Pasta-4 specification, extended to support both encryption and decryption within a single, reusable AXI-Stream interface. Internally, the PL contains separate encryption and decryption modules that share common data pathways and utilize FIFOs for input and output staging, allowing seamless streaming of large data batches. A custom-designed AXI-Stream wrapper orchestrates data movement, dividing incoming plaintext or ciphertext streams into 17-word packets (32 bits each) per encryption round before injecting them into the cipher core. The same wrapper handles output staging, ensuring results are packetized and returned to the PS efficiently. Key generation and all cryptographic computations are fully implemented within the PL, allowing end-to-end symmetric processing to be completed in hardware without software intervention.

The PS in HHEML serves as the control and coordination layer. Its role is limited to configuring DMA channels, issuing start and stop commands, and supervising data flow between the host software and the hardware accelerator. It does not perform any cryptographic or preprocessing tasks, relying entirely on the PL for key scheduling, keystream generation, and encryption or decryption. Communication between PS and PL is handled via an AXI4-Stream interface combined with DMA for high-throughput data transfer, while control and status signals are managed through a lightweight AXI-Lite interface. Once data encryption is complete, the resulting ciphertexts, together with their symmetric encryption keys (protected under the SE scheme), are transmitted to the server through a single Ethernet link, where they are transformed into FHE ciphertexts and processed within the GuardML inference pipeline.

This modular hardware-software partitioning enables a clear separation of responsibilities: the PL delivers high-performance, hardware-accelerated encryption and decryption with complete key management, while the PS maintains minimal control overhead. Such a design reduces latency on the client side and provides a scalable foundation for hybrid homomorphic encryption in privacy-preserving machine learning applications.

---

### النسخة العربية

## IV. HHEML

### أ. نظرة عامة على النظام

يتكون إطار عمل HHEML المقترح، الموضح في الشكل 2، من جزأين متكاملين بشكل وثيق: عميل مُنفّذ على FPGA من نوع PYNQ-Z2 وخادم ينفذ مجموعة تقييم متماثل قائمة على GuardML. على جانب العميل، يحتوي المنطق القابل للبرمجة (PL) على مُسرّع عتادي مشتق من تصميم Pasta on Edge وموسّع لدعم التشفير المتماثل الهجين الكامل. يتم تنفيذ توليد المفاتيح، والتشفير المتماثل، وفك التشفير بالكامل في العتاد ضمن مسار موحد، مما يزيل الاعتماد على البرمجيات للعمليات التشفيرية الحساسة لزمن الوصول. يتعامل نظام المعالجة (PS) مع التنسيق عالي المستوى، بما في ذلك التكوين وجدولة البيانات، ويتواصل مع PL عبر واجهة AXI4-Stream مع دعم DMA لنقل البيانات الكبيرة، بينما يتم تبادل معلومات التحكم والحالة من خلال AXI-Lite.

يبدأ مسار عمل المعالجة بمدخلات نص عادي، مثل متجهات الميزات من تطبيقات التعلم الآلي على الحافة، التي يتم جمعها بواسطة PS ونقلها إلى مُسرّع PL. باستخدام شفرة Pasta، يقوم PL بتشفير البيانات بسرعة، مما ينتج نصوصاً مشفرة متوافقة مباشرة مع التحويل اللاحق إلى شكل التشفير المتماثل الكامل (FHE). تُرسل هذه النصوص المشفرة إلى الخادم عبر ارتباط Ethernet، حيث يحولها GuardML إلى نصوص مشفرة FHE ويقوم بإجراء استدلال مشفر على النموذج المستهدف. ثم يتم إعادة ترميز النتائج المُقيّمة كنصوص مشفرة متماثلة، وإرسالها مرة أخرى إلى العميل، وفك تشفيرها في العتاد لإنتاج التنبؤات النهائية.

الميزة المعمارية الرئيسية لـ HHEML هي استخدام مسار بيانات متدفق في مُسرّع PL. من خلال إعادة تنظيم توليد تدفق المفاتيح وعمليات إخفاء البيانات، يمكن للعتاد معالجة كتل إدخال متعددة بالتوازي، مما يقلل زمن الوصول لمجموعات البيانات الكبيرة مثل مدخلات الصور المجمعة. يعزز هذا التحسين الأداء على جانب العميل مع الحفاظ على التكامل السلس مع مجموعة برمجيات GuardML.

يوفر الشكل 3 نظرة عامة على مسار العمل الشامل هذا من البداية إلى النهاية، موضحاً حركة البيانات من التقاط النص العادي الأولي على العميل، عبر التشفير القائم على العتاد ونقل الشبكة، إلى تقييم FHE على جانب الخادم، وأخيراً فك التشفير الآمن على عميل FPGA.

### ب. الوحدات في HHEML

يعمل إطار عمل HHEML بشكل أساسي على جانب العميل، مُجسداً كتصميم نظام معالجة (PS) ومنطق قابل للبرمجة (PL) مترابط بإحكام على منصة FPGA من نوع PYNQ-Z2. يستضيف PL تطبيقاً عتادياً لشفرة Pasta بناءً على مواصفات Pasta-4، موسّعة لدعم كل من التشفير وفك التشفير ضمن واجهة AXI-Stream واحدة قابلة لإعادة الاستخدام. داخلياً، يحتوي PL على وحدات تشفير وفك تشفير منفصلة تشترك في مسارات بيانات مشتركة وتستخدم FIFOs لتنظيم الإدخال والإخراج، مما يسمح ببث سلس لدفعات البيانات الكبيرة. يُنسق غلاف AXI-Stream مصمم خصيصاً حركة البيانات، مقسماً تدفقات النص العادي أو النص المشفر الواردة إلى حزم من 17 كلمة (32 بت لكل منها) لكل جولة تشفير قبل حقنها في نواة التشفير. يتعامل نفس الغلاف مع تنظيم الإخراج، مما يضمن تجميع النتائج وإعادتها إلى PS بكفاءة. يتم تنفيذ توليد المفاتيح وجميع الحسابات التشفيرية بالكامل ضمن PL، مما يسمح بإكمال المعالجة المتماثلة الشاملة من البداية إلى النهاية في العتاد دون تدخل البرمجيات.

يعمل PS في HHEML كطبقة التحكم والتنسيق. يقتصر دوره على تكوين قنوات DMA، وإصدار أوامر البدء والإيقاف، والإشراف على تدفق البيانات بين برمجيات المضيف والمُسرّع العتادي. لا يقوم بأي مهام تشفيرية أو معالجة مسبقة، معتمداً بالكامل على PL لجدولة المفاتيح، وتوليد تدفق المفاتيح، والتشفير أو فك التشفير. يتم التعامل مع الاتصال بين PS وPL عبر واجهة AXI4-Stream مدمجة مع DMA لنقل بيانات عالي الإنتاجية، بينما تُدار إشارات التحكم والحالة من خلال واجهة AXI-Lite خفيفة الوزن. بمجرد اكتمال تشفير البيانات، تُرسل النصوص المشفرة الناتجة، مع مفاتيح التشفير المتماثل الخاصة بها (محمية تحت مخطط SE)، إلى الخادم عبر ارتباط Ethernet واحد، حيث يتم تحويلها إلى نصوص مشفرة FHE ومعالجتها ضمن مسار استدلال GuardML.

يتيح هذا التقسيم المعياري للعتاد والبرمجيات فصلاً واضحاً للمسؤوليات: يقدم PL تشفيراً وفك تشفير عالي الأداء ومُسرّع بالعتاد مع إدارة كاملة للمفاتيح، بينما يحافظ PS على عبء تحكم ضئيل. يقلل هذا التصميم من زمن الوصول على جانب العميل ويوفر أساساً قابلاً للتوسع للتشفير المتماثل الهجين في تطبيقات التعلم الآلي الحافظ للخصوصية.

---

### Translation Notes

- **Figures referenced:** Fig. 2 (HHEML System Overview), Fig. 3 (HHEML Workflow)
- **Key terms introduced:**
  - PYNQ-Z2 FPGA = FPGA من نوع PYNQ-Z2
  - Processing System (PS) = نظام المعالجة
  - Programmable Logic (PL) = المنطق القابل للبرمجة
  - AXI4-Stream = واجهة AXI4-Stream (technical interface kept)
  - AXI-Lite = واجهة AXI-Lite (technical interface kept)
  - DMA (Direct Memory Access) = DMA (الوصول المباشر للذاكرة)
  - FIFO = FIFO (First-In-First-Out buffer)
  - Ethernet link = ارتباط Ethernet
  - GuardML = GuardML (framework name kept)
  - Pipelined datapath = مسار بيانات متدفق
  - Keystream generation = توليد تدفق المفاتيح
  - Data masking = إخفاء البيانات
  - Hardware-software partitioning = التقسيم المعياري للعتاد والبرمجيات
  - Control overhead = عبء تحكم

- **Equations:** None
- **Citations:** None in this section
- **Special handling:**
  - Technical interface names (AXI4-Stream, AXI-Lite) kept in English
  - System names (PYNQ-Z2, GuardML, Pasta) kept in English
  - Packet size (17-word, 32 bits) kept in original form
  - Subsection headings A, B maintained

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-Translation Check (System Overview opening)

Arabic: "يتكون إطار عمل HHEML المقترح، الموضح في الشكل 2، من جزأين متكاملين بشكل وثيق: عميل مُنفّذ على FPGA من نوع PYNQ-Z2 وخادم ينفذ مجموعة تقييم متماثل قائمة على GuardML."

Back to English: "The proposed HHEML framework, shown in Fig. 2, consists of two tightly integrated parts: a client implemented on a PYNQ-Z2 FPGA and a server executing a homomorphic evaluation stack based on GuardML."

✓ Semantically equivalent to original
