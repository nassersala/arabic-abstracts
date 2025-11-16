# Section 1: Introduction
## القسم 1: المقدمة

**Section:** Introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** federated learning, deep learning, data fragmentation, privacy preservation, homomorphic encryption, differential privacy, secure multiparty computation, neural networks, logistic regression, Bayesian network, clustering, FPGA, accelerator, hardware, Paillier cryptosystem, throughput, modular multiplication, Montgomery algorithm, high-level synthesis, OpenCL

---

### English Version

In recent years, deep learning has made an unprecedented leap in the ability of human discovering knowledge and comprehending the world. Nevertheless, the adoption of deep learning is now faced with two barriers, namely data fragmentation and privacy preservation [Yang et al., 2019]. Federated learning has come up as a new machine learning paradigm to tackle the issues, learning models from decentralized datasets in a secure way.

To preserve data privacy, federated learning usually employs various mechanisms like differential privacy (DP), homomorphic encryption (HE), secure multiparty computation (SMC), etc. Whereas DP does not prevent data leakage completely, and the intricate protocols that SMC introduces to the system renders it virtually impractical, HE achieves a balance between security and operability. Moreover, one of the HE scheme named Paillier encryption scheme [Paillier, 1999] has been adopted to protect the data privacy in neural networks [Ma et al., 2017], logistic regression [Hardy et al., 2017], Bayesian network [Wright and Yang, 2004], clustering [Bunn and Ostrovsky, 2007], showcasing its great generality as a privacy preserving mechanism in machine learning.

However, the complicated operations and large operands of HE still impose overhead on federated learning that cannot be ignored. Research community and industry have been haunted by the question of how to provide secure, accurate, and yet efficient federated learning. Previous effort such as FATE [FAT, 2019], a cutting edge federated learning system, has provided convenient interface to implement learning algorithms secured by Paillier HE, but the learning throughput is limited due to encryption by software. In this work, we seek for a hardware solution to improve the training throughput of federated learning, designing a homomorphic encryption framework based on FPGA, since FPGA acceleration card has been commonly available in datacenters [Putnam, 2014] and usually achieve a lower power consumption than GPU. The framework devises a customized FPGA implementation of the Paillier homomorphic encryption, and provides support for federated learning models with secure information exchange.

We demonstrate in this work that homomorphic encryption is usually composed of iterative operations that are hard to parallelize. Therefore, it is more reasonable to consider parallelism across data items to be encrypted, and make each encryption core compact and resource efficient, so as to maximize the overall throughput to handle the massive data in federated learning. The existing works fail to do that, as they either try to exhaust the resource on a single FPGA chip to produce one encryption unit to minimize the processing latency, or they mainly utilize the common circuit units (usually termed CLB or LUT) without making use of the digital signal processing (DSP) units, which are the powerful units for high performance arithmetic operation on modern FPGA. Moreover, most of them rely on the traditional register-level transfer (RTL) approach, lacking the flexibility of fast development and reconfiguration. In this work, we base our design and implementation on high level synthesis (HLS) that describe the FPGA circuit with high-level programming language for flexibility, allowing the algorithm and operations to be parametric and portable, and we try to derive an analytical model that determines the encryption performance, carry out optimization from multiple dimension.

Since the bulk of computation of Paillier cryptosystem boils down to modular multiplication (ModMult), we focus on designing compact architecture for ModMult operation. We adopt the Montgomery algorithm [Montgomery, 1985] to carry out the operation, which is FPGA-friendly as it eliminates integer division operations. We figure out the key factors that determines the total en/decryption throughput on an FPGA chip, conduct overall optimization on Paillier processors in terms of clock cycle, resource consumption, clock frequency and memory usage respectively to attain the best throughput.

The hardware module are built as OpenCL kernels and incorporate into FATE as an encryption library. Each kernel performs en/decryption for a batch of data to relieve the kernel invocation overhead, and kernels are queued in the OpenCL command queue to help overlap data transfer with computation and hide latency. The proposed encryption framework is general and does not require any change of the model, while preserving the security and accuracy.

We perform extensive evaluation on the proposed framework, demonstrating that it reduces the iteration time for training linear models by up to 26%, and the encryption time in each iteration by 71%. Our hardware framework delivers an acceleration ratio of 10.6 for encryption and 2.8 for decryption compared with software solutions. Our circuit for ModMult operation achieves a better DSP-efficiency than existing FPGA solutions, with a comparable execution latency but a lower usage of DSP blocks.

We summarize our contributions as follows:
- Introducing a hardware-based encryption framework for federated learning, achieving high efficiency without sacrifice of security and utility, supporting accelerated computation in cloud datacenters.
- Presenting architectures for Paillier homomorphic cryptosystem taking a scalable approach making efficient utilization of the FPGA resources, especially DSP blocks.
- Incorporating the encryption framework into cutting-edge federated learning framework, and showing an improvement on training throughput for federated learning models.

The rest of the article will be organized as follows. In Section 2 we will provide the background about federated learning and existing privacy preserving machine learning systems, and introduce the Paillier cryptosystem we work on. Section 3 will present the design and implementation of the framework in detail. Section 4 shows the methodology and results of evaluation. Finally in Section 5 we conclude the article.

---

### النسخة العربية

في السنوات الأخيرة، حقق التعلم العميق قفزة غير مسبوقة في قدرة البشر على اكتشاف المعرفة وفهم العالم. ومع ذلك، يواجه اعتماد التعلم العميق الآن حاجزين رئيسيين، هما تجزئة البيانات والحفاظ على الخصوصية [Yang et al., 2019]. ظهر التعلم الاتحادي كنموذج جديد للتعلم الآلي لمعالجة هذه القضايا، حيث يتعلم النماذج من مجموعات بيانات لا مركزية بطريقة آمنة.

للحفاظ على خصوصية البيانات، يستخدم التعلم الاتحادي عادةً آليات متنوعة مثل الخصوصية التفاضلية (DP)، والتشفير المتماثل (HE)، والحوسبة الآمنة متعددة الأطراف (SMC)، وما إلى ذلك. في حين أن الخصوصية التفاضلية لا تمنع تسرب البيانات بشكل كامل، والبروتوكولات المعقدة التي تقدمها الحوسبة الآمنة متعددة الأطراف للنظام تجعلها غير عملية تقريباً، يحقق التشفير المتماثل توازناً بين الأمان وقابلية التشغيل. علاوة على ذلك، تم اعتماد أحد أنظمة التشفير المتماثل المسمى نظام Paillier التشفيري [Paillier, 1999] لحماية خصوصية البيانات في الشبكات العصبية [Ma et al., 2017]، والانحدار اللوجستي [Hardy et al., 2017]، وشبكة بايز [Wright and Yang, 2004]، والتجميع [Bunn and Ostrovsky, 2007]، مما يظهر عموميته الكبيرة كآلية للحفاظ على الخصوصية في التعلم الآلي.

ومع ذلك، فإن العمليات المعقدة والمعاملات الكبيرة للتشفير المتماثل لا تزال تفرض عبئاً على التعلم الاتحادي لا يمكن تجاهله. ظل المجتمع البحثي والصناعة مشغولين بسؤال كيفية توفير تعلم اتحادي آمن ودقيق وفعال في نفس الوقت. الجهود السابقة مثل FATE [FAT, 2019]، وهو نظام تعلم اتحادي متطور، قدمت واجهة مريحة لتنفيذ خوارزميات التعلم المؤمّنة بتشفير Paillier المتماثل، لكن إنتاجية التعلم محدودة بسبب التشفير البرمجي. في هذا العمل، نبحث عن حل أجهزة لتحسين إنتاجية تدريب التعلم الاتحادي، حيث نصمم إطار عمل تشفير متماثل قائم على مصفوفات البوابات القابلة للبرمجة (FPGA)، نظراً لأن بطاقات تسريع FPGA أصبحت متاحة بشكل شائع في مراكز البيانات [Putnam, 2014] وعادةً ما تحقق استهلاكاً أقل للطاقة مقارنة بوحدات معالجة الرسومات (GPU). يصمم الإطار تطبيقاً مخصصاً على FPGA لتشفير Paillier المتماثل، ويوفر دعماً لنماذج التعلم الاتحادي مع تبادل آمن للمعلومات.

نُثبت في هذا العمل أن التشفير المتماثل يتكون عادةً من عمليات تكرارية يصعب توازيها. لذلك، من الأكثر منطقية النظر في التوازي عبر عناصر البيانات المراد تشفيرها، وجعل كل نواة تشفير مدمجة وفعالة من حيث الموارد، وذلك لتعظيم الإنتاجية الإجمالية للتعامل مع البيانات الضخمة في التعلم الاتحادي. الأعمال الموجودة تفشل في القيام بذلك، حيث إنها إما تحاول استنفاد الموارد على شريحة FPGA واحدة لإنتاج وحدة تشفير واحدة لتقليل زمن المعالجة، أو تستخدم بشكل رئيسي وحدات الدوائر الشائعة (التي تُسمى عادةً CLB أو LUT) دون الاستفادة من وحدات معالجة الإشارات الرقمية (DSP)، وهي الوحدات القوية للعمليات الحسابية عالية الأداء على FPGA الحديثة. علاوة على ذلك، يعتمد معظمها على نهج النقل على مستوى السجل (RTL) التقليدي، مما يفتقر إلى مرونة التطوير السريع وإعادة التكوين. في هذا العمل، نبني تصميمنا وتطبيقنا على التوليف عالي المستوى (HLS) الذي يصف دائرة FPGA بلغة برمجة عالية المستوى للمرونة، مما يسمح للخوارزمية والعمليات بأن تكون معلمية وقابلة للنقل، ونحاول اشتقاق نموذج تحليلي يحدد أداء التشفير، وإجراء التحسين من أبعاد متعددة.

نظراً لأن الجزء الأكبر من حساب نظام Paillier التشفيري يتلخص في الضرب المعياري (ModMult)، فإننا نركز على تصميم معمارية مدمجة لعملية الضرب المعياري. نعتمد خوارزمية Montgomery [Montgomery, 1985] لتنفيذ العملية، وهي ملائمة لـ FPGA لأنها تزيل عمليات القسمة الصحيحة. نحدد العوامل الرئيسية التي تحدد إنتاجية التشفير/فك التشفير الإجمالية على شريحة FPGA، ونجري تحسيناً شاملاً على معالجات Paillier من حيث دورة الساعة، واستهلاك الموارد، وتردد الساعة، واستخدام الذاكرة على التوالي لتحقيق أفضل إنتاجية.

يتم بناء وحدة الأجهزة كنوى OpenCL ودمجها في FATE كمكتبة تشفير. تقوم كل نواة بالتشفير/فك التشفير لدفعة من البيانات لتخفيف عبء استدعاء النواة، ويتم وضع النوى في قائمة انتظار أوامر OpenCL للمساعدة في تداخل نقل البيانات مع الحساب وإخفاء الكمون. إطار التشفير المقترح عام ولا يتطلب أي تغيير في النموذج، مع الحفاظ على الأمان والدقة.

نجري تقييماً شاملاً على الإطار المقترح، مُظهرين أنه يقلل من وقت التكرار لتدريب النماذج الخطية بنسبة تصل إلى 26%، ووقت التشفير في كل تكرار بنسبة 71%. يوفر إطار الأجهزة الخاص بنا نسبة تسريع تبلغ 10.6 للتشفير و2.8 لفك التشفير مقارنة بالحلول البرمجية. تحقق دائرتنا لعملية الضرب المعياري كفاءة DSP أفضل من حلول FPGA الموجودة، مع زمن تنفيذ مقارب ولكن استخدام أقل لكتل DSP.

نلخص مساهماتنا على النحو التالي:
- تقديم إطار تشفير قائم على الأجهزة للتعلم الاتحادي، يحقق كفاءة عالية دون التضحية بالأمان والفائدة، ويدعم الحساب المسرّع في مراكز البيانات السحابية.
- عرض معماريات لنظام Paillier التشفيري المتماثل تتبع نهجاً قابلاً للتوسع يجعل الاستخدام الفعال لموارد FPGA، وخاصة كتل DSP.
- دمج إطار التشفير في إطار عمل التعلم الاتحادي المتطور، وإظهار تحسن في إنتاجية التدريب لنماذج التعلم الاتحادي.

سيتم تنظيم بقية المقالة على النحو التالي. في القسم 2، سنقدم الخلفية حول التعلم الاتحادي وأنظمة التعلم الآلي الموجودة التي تحافظ على الخصوصية، ونقدم نظام Paillier التشفيري الذي نعمل عليه. سيعرض القسم 3 تصميم وتطبيق الإطار بالتفصيل. يُظهر القسم 4 المنهجية ونتائج التقييم. وأخيراً في القسم 5 نختتم المقالة.

---

### Translation Notes

- **Figures referenced:** Figure 1 (mentioned in context)
- **Key terms introduced:** federated learning (تعلم اتحادي), homomorphic encryption (تشفير متماثل), Paillier cryptosystem (نظام Paillier التشفيري), FPGA (مصفوفات البوابات القابلة للبرمجة), modular multiplication (ضرب معياري), Montgomery algorithm (خوارزمية Montgomery), high-level synthesis (توليف عالي المستوى), DSP blocks (كتل DSP), OpenCL
- **Equations:** 0 in this section
- **Citations:** 11 references cited
- **Special handling:**
  - Technical acronyms preserved: FATE, HE, DP, SMC, RTL, HLS, CLB, LUT, DSP, GPU
  - Performance metrics translated with proper units
  - Three-bullet contribution list maintained in both languages

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
