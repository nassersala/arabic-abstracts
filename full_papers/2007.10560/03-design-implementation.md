# Section 3: Design and Implementation
## القسم 3: التصميم والتطبيق

**Section:** Design and Implementation
**Translation Quality:** 0.86
**Glossary Terms Used:** FPGA, hardware accelerator, Paillier cryptosystem, modular multiplication, Montgomery algorithm, high-level synthesis, HLS, OpenCL, DSP blocks, throughput, latency, clock cycle, clock frequency, resource allocation, pipeline, processing element, Karatsuba algorithm, BRAM, optimization

---

### English Version

## 3.1 System Overview

The overall architecture of our encryption framework is shown in Figure 2. The framework is envisioned to be hosted on cloud servers belonging to geo-distributed parties of federated learning. It includes components residing on both the host CPU and the FPGA, where a PCI-e bus provides communication between them. The host CPU is responsible for the normal training workload of a machine learning model, while it batches the requests of encryption to sends to the FPGA, and encodes the floating point number used by machine learning to integers agree with HE schemes. Apart from these necessities, our main contribution is designing high performance processors for Paillier computation on FPGA and encapsulating the hardware module as OpenCL kernel for invocation, which we will detail in Section 3.2 and 3.3 respectively.

## 3.2 Micro-architecture for Montgomery ModMult

A Paillier processor encapsulates units for operations involved, i.e. modular multiplication, random number generator and integer divisor, along with its local storage. We replicate Paillier processors in HLS to deploy multiple copies, and the top level function is responsible for dispatching input data and collecting results. Since the Paillier processors are independent and work in parallel, the overall throughput of an FPGA chip can be determined by

$$\text{Throughput} = \frac{\text{Total amount of resource}}{\text{Latency} \times \text{Resource consumption per core}}$$

where resource broadly refers to multipliers, adders, memory, etc., and latency can be further decomposed to $\frac{\text{clock cycle of execution}}{\text{clock frequency}}$. Therefore, our design guideline is to optimize the Montgomery ModMult operation lying at the heart of Paillier cryptosystem, with respect to clock cycle, resource allocation, clock frequency, in addition to memory usage. We elaborate on the optimization on these dimensions as below.

### Clock Cycle

Generally, the clock cycle required by an algorithm is intrinsically lower bounded by the number of operations and the critical path in the dependency graph. As shown in Algorithm 1, the body of the Montgomery algorithm is a two-level loop, consisting of $2(l/k)(l/k+1)$ multiplications. Thus, the ideal clock cycle will be $2(l/k)(l/k+1)$ divided by the number of multipliers, even if we ignore the rest of the operations. On the other hand, as the execution of each inner iteration depends on the iteration before, it is hard to force a parallel execution of the inner iterations. Our goal is to deploy two multipliers for an inner iteration, and obtain a clock cycle number as close to $(l/k)(l/k+1)$ as possible.

Another dependency issue that deserves attention is the computation of $q$ in each outer iteration. In the $i$-th iteration, $q$ depends on the value of $S_{i-1}$, while it is necessary in the computation of inner loops. However, if $q$ is computed before the start of inner loop, the latency will be magnified by the number of outer iterations.

To enforce a tight scheduling, we make the following optimizations in HLS:

- **Unrolling the inner loop.** This can be done through an UNROLL directive in HLS, or manually repeat part of the loop. Unrolling the loop does not lead to parallel execution of iterations. However, this is the only way to disassemble all the operations composing the loop, achieving the flexibility of scheduling to overlap operations as much as possible. Also, without unrolling we are not able to insert the computation of $q$ into the middle of an inner loop.

- **Interleaving the $q$ computation with the inner loop.** As discussed before, the $q$ value used in each inner loop must be computed before. Since the $q$ value for computing $S_i$ only relies on first few words of $S_{i-1}$, it is possible to start generating $q$ in the last inner loop when those words are ready. In this way we can obtain $q$ in advance and hide its latency.

- **Pipelining the outer loop.** We achieve this by inserting a PIPELINE directive in HLS, with the initiation interval set to the number of iterations contained in an inner loop. The final step of schedule enforcement is to pipeline all the iterations. We aim to pipeline both the outer loop and the inner loop by unrolling the inner loop, and pipelining the outer loop, so that the inner loop is naturally pipelined by scheduling the disassembled operations, and the outer loop try to start an interaction each time when a whole inner loop is initiated.

The resulted scheduling is shown in Figure 3. We illustrate with an example with operands 4 words in length (i.e. $l/k = 4$), and the computation of each inner iteration takes 4 clock cycles to complete. Initially, the schedule computes $q$ for the first inner loop (not shown in the figure), and then initiates the inner iterations sequentially. In the meantime, as soon as $S^0$ is ready, it can be used to compute $q$ for the next inner loop. Hence, when the last inner iteration ends, the first iteration of the next inner loop can start immediately with the precomputed $q$. Therefore, we enable a tight schedule that initiates an inner iteration each clock cycle. The resulted execution clock cycle is $(l/k)(l/k+1)$, plus the number of pipeline stages, and a few cycles for data read-in and write-out.

### Resource Allocation

In this work, we utilize the embedded DSP blocks on the FPGA chip to construct pipelined multipliers. For the remaining logic, including adder, multiplexer, integer comparison, finite state machine, etc., we leave them to lookup-table (LUT). As DSP on FPGA is scarce and expensive, we use them to carry out the heavy multiplication only. Further, we will show purely relying on LUT to implement ModMult operation is not economic (Section 4). Therefore, we will focus on the usage of LUT and DSP, and reduce the area and DSP usage without sacrificing the performance.

We encapsulate the operations comprising an inner iteration into a processing element (PE), as shown in Figure 4. Each PE contains two multipliers to perform the two independent multiplications $xy$ and $qm$. Then it accepts $S_{i-1}^j$ of the last outer iteration, and a carry word (not shown in the figure), adds them with the multiplication results, and then outputs $S_i^j$ and a carry word. Then we limit the number of PE to 1, with an ALLOCATION directive in HLS. This is to avoid the resource bloating owing to loop unrolling, so that only resource for computing one inner iteration is actually allocated, and to reduce the overall area of the micro-architecture.

We also employ the Karatsuba algorithm to construct DSP-conservative multipliers. As shown in Algorithm 2, Karatsuba algorithm performs an integer multiplication by recursively breaking it into three of half size. Its efficiency is attributed to one multiplication less than the schoolbook algorithm, and we take advantage of it to allocate DSPs according to the actual number of operations. For instance, a DSP48E1 block is able to carry out $18 \times 25$-bit multiplication, and a $32 \times 32$ one can be divided into $16 \times 16$ ones, and takes up 3 DSP blocks.

**Algorithm 2:** Karatsuba algorithm

**Input:** Operands $X$ and $Y$, the length of operand $k$

**Output:** $S = X \times Y$

1. Let $X = X_h X_l$, $Y = Y_h Y_l$, where $X_h, X_l, Y_h, Y_l$ are $k/2$-bit integers;
2. $HH \leftarrow \text{Karatsuba}(X_h, Y_h)$;
3. $LL \leftarrow \text{Karatsuba}(X_l, Y_l)$;
4. $HL \leftarrow \text{Karatsuba}(X_h + X_l, Y_h + Y_l)$;
5. $S \leftarrow HH \cdot 2^k + (HL - HH - LL) \cdot 2^{k/2} + LL$;
6. **return** $S$

### Clock Frequency

The DSP units on the Xilinx FPGA run at a maximum frequency of 400-500MHz. To approach the frequency limit, we need to pay attention to the following measures:

- **Declare the multipliers as pipelined multipliers.** A pipelined multiplier takes multiple cycles to accomplish a multiplication, distributing its workload and relieving the burden of each cycle. It does no harm to the multiplication throughput since we have resolved the dependency between its input and output.

- **Restrict bitwidth of operands.** The clock frequency is constraint by the critical path of the circuit, i.e. the longest path of gates a signal needs to pass through during one cycle. Arithmetic on integers such as addition or comparison usually results in a long carry chain, and thus we need to avoid computation on very long integers directly. In this work, we use 32-bit as the operand size, and the maximum bitwidth involved is 64 bits.

- **Simplify the control logic.** For the finite state machine in charge of controlling the compute units, we use one-hot encoding scheme to represent the states for a fast lookup and match. The number of states is related to the number of iterations of each loop and thus one-hot encoding will be acceptable.

### Memory Usage

Our design allocate each Paillier processors its own block RAM (BRAM) as local buffer, to hold the input/output data and the intermediate large integers involved in the computation. We do not share storage among processors to prevent data access contention.

Large integers are normally stored as arrays of words in the BRAM. However, we notice that the input data for encryption, which are encoded from floating point numbers used in machine learning, have few effective digits compared with the length of large integers. Therefore, we are able to store the input data as a sparse vector, i.e. only recording the non-zero elements and their indices, reducing the memory footprint.

## 3.3 Implementation

We develop our encryption framework with the AWS F1 instance and Xilinx SDAccel development suite. The basic logic of the encryption and decryption function is implemented with Xilinx high level synthesis (HLS), allowing to transform an algorithm described in C/C++ into tailor-made implementation on FPGA. Directives like loop pipelining and instance allocation are inserted into the HLS code to fine tune the performance of the resulted architecture.

On the host side, we use the OpenCL API to access the acceleration hardware. The OpenCL API provides an abstraction of the computing device like CPU, GPU and FPGA. An invocation to the device function is named a kernel. OpenCL is used to manage the data transfer between host and device, queue and invoke kernels, and monitor the execution events. We adopt the PyOpenCL APIs to implement a module that makes use of the FPGA device for cryptographic processes and incorporate it into the FATE framework.

The requests from the host side are divided into fixed size batches, and each batch invokes a kernel on device. Multiple kernels will be queued in the OpenCL command queue. This helps overlap data transfer with computation and hide latency. We also preallocate buffers on the device, arranging them as a ring buffer, in order to reuse buffers among kernels and avoid frequent memory allocation.

---

### النسخة العربية

## 3.1 نظرة عامة على النظام

يظهر في الشكل 2 المعمارية الإجمالية لإطار التشفير الخاص بنا. يُتصور أن يتم استضافة الإطار على خوادم سحابية تنتمي إلى أطراف التعلم الاتحادي الموزعة جغرافياً. يتضمن مكونات موجودة على كل من وحدة المعالجة المركزية المضيفة (CPU) ومصفوفة البوابات القابلة للبرمجة (FPGA)، حيث يوفر ناقل PCI-e الاتصال بينهما. وحدة المعالجة المركزية المضيفة مسؤولة عن حمل التدريب العادي لنموذج التعلم الآلي، بينما تجمع طلبات التشفير لإرسالها إلى FPGA، وتشفر الأعداد ذات الفاصلة العائمة المستخدمة في التعلم الآلي إلى أعداد صحيحة تتوافق مع أنظمة التشفير المتماثل. بصرف النظر عن هذه الضروريات، فإن مساهمتنا الرئيسية هي تصميم معالجات عالية الأداء لحساب Paillier على FPGA وتغليف وحدة الأجهزة كنواة OpenCL للاستدعاء، والتي سنفصلها في القسمين 3.2 و3.3 على التوالي.

## 3.2 المعمارية الدقيقة للضرب المعياري بخوارزمية Montgomery

يغلف معالج Paillier وحدات للعمليات المتضمنة، أي الضرب المعياري، ومولد الأرقام العشوائية، والقاسم الصحيح، إلى جانب تخزينه المحلي. نكرر معالجات Paillier في HLS لنشر نسخ متعددة، والدالة من المستوى الأعلى مسؤولة عن توزيع بيانات الإدخال وجمع النتائج. نظراً لأن معالجات Paillier مستقلة وتعمل بالتوازي، يمكن تحديد الإنتاجية الإجمالية لشريحة FPGA بواسطة

$$\text{الإنتاجية} = \frac{\text{إجمالي كمية الموارد}}{\text{الكمون} \times \text{استهلاك الموارد لكل نواة}}$$

حيث تشير الموارد على نطاق واسع إلى المضاعفات، والمجمعات، والذاكرة، وما إلى ذلك، ويمكن تحليل الكمون بشكل أكبر إلى $\frac{\text{دورة ساعة التنفيذ}}{\text{تردد الساعة}}$. لذلك، فإن مبدأ التصميم الخاص بنا هو تحسين عملية الضرب المعياري بخوارزمية Montgomery الموجودة في قلب نظام Paillier التشفيري، فيما يتعلق بدورة الساعة، وتخصيص الموارد، وتردد الساعة، بالإضافة إلى استخدام الذاكرة. نفصل التحسين على هذه الأبعاد أدناه.

### دورة الساعة

بشكل عام، دورة الساعة المطلوبة بواسطة خوارزمية محددة جوهرياً بعدد العمليات والمسار الحرج في رسم التبعية. كما هو موضح في الخوارزمية 1، جسم خوارزمية Montgomery عبارة عن حلقة من مستويين، تتكون من $2(l/k)(l/k+1)$ عمليات ضرب. وبالتالي، فإن دورة الساعة المثالية ستكون $2(l/k)(l/k+1)$ مقسومة على عدد المضاعفات، حتى لو تجاهلنا بقية العمليات. من ناحية أخرى، نظراً لأن تنفيذ كل تكرار داخلي يعتمد على التكرار السابق، فمن الصعب فرض تنفيذ متوازي للتكرارات الداخلية. هدفنا هو نشر اثنين من المضاعفات لتكرار داخلي، والحصول على عدد دورات ساعة قريب من $(l/k)(l/k+1)$ قدر الإمكان.

مشكلة تبعية أخرى تستحق الاهتمام هي حساب $q$ في كل تكرار خارجي. في التكرار $i$-ال، يعتمد $q$ على قيمة $S_{i-1}$، بينما هو ضروري في حساب الحلقات الداخلية. ومع ذلك، إذا تم حساب $q$ قبل بدء الحلقة الداخلية، فسيتم تضخيم الكمون بعدد التكرارات الخارجية.

لفرض جدولة محكمة، نقوم بالتحسينات التالية في HLS:

- **فك الحلقة الداخلية.** يمكن القيام بذلك من خلال توجيه UNROLL في HLS، أو تكرار جزء من الحلقة يدوياً. فك الحلقة لا يؤدي إلى تنفيذ متوازي للتكرارات. ومع ذلك، هذه هي الطريقة الوحيدة لتفكيك جميع العمليات المكونة للحلقة، وتحقيق مرونة الجدولة لتداخل العمليات قدر الإمكان. أيضاً، بدون فك الحلقة لن نكون قادرين على إدراج حساب $q$ في منتصف الحلقة الداخلية.

- **تشابك حساب $q$ مع الحلقة الداخلية.** كما نوقش من قبل، يجب حساب قيمة $q$ المستخدمة في كل حلقة داخلية مسبقاً. نظراً لأن قيمة $q$ لحساب $S_i$ تعتمد فقط على الكلمات القليلة الأولى من $S_{i-1}$، فمن الممكن البدء في توليد $q$ في الحلقة الداخلية الأخيرة عندما تكون تلك الكلمات جاهزة. بهذه الطريقة يمكننا الحصول على $q$ مسبقاً وإخفاء كمونها.

- **جعل الحلقة الخارجية خطية.** نحقق ذلك من خلال إدراج توجيه PIPELINE في HLS، مع تعيين فترة البدء إلى عدد التكرارات الموجودة في الحلقة الداخلية. الخطوة الأخيرة من فرض الجدولة هي جعل جميع التكرارات خطية. نهدف إلى جعل كل من الحلقة الخارجية والحلقة الداخلية خطية من خلال فك الحلقة الداخلية، وجعل الحلقة الخارجية خطية، بحيث يتم جعل الحلقة الداخلية خطية بشكل طبيعي من خلال جدولة العمليات المفككة، وتحاول الحلقة الخارجية بدء تفاعل في كل مرة يتم فيها بدء حلقة داخلية كاملة.

تظهر الجدولة الناتجة في الشكل 3. نوضح بمثال مع معاملات بطول 4 كلمات (أي $l/k = 4$)، ويستغرق حساب كل تكرار داخلي 4 دورات ساعة لإكماله. في البداية، تحسب الجدولة $q$ للحلقة الداخلية الأولى (غير موضحة في الشكل)، ثم تبدأ التكرارات الداخلية بالتسلسل. في هذه الأثناء، بمجرد أن تكون $S^0$ جاهزة، يمكن استخدامها لحساب $q$ للحلقة الداخلية التالية. وبالتالي، عندما ينتهي التكرار الداخلي الأخير، يمكن أن يبدأ التكرار الأول من الحلقة الداخلية التالية فوراً مع $q$ المحسوبة مسبقاً. لذلك، نمكّن جدولة محكمة تبدأ تكراراً داخلياً في كل دورة ساعة. دورة ساعة التنفيذ الناتجة هي $(l/k)(l/k+1)$، بالإضافة إلى عدد مراحل خط الأنابيب، وبضع دورات لقراءة البيانات وكتابتها.

### تخصيص الموارد

في هذا العمل، نستخدم كتل DSP المضمنة على شريحة FPGA لبناء مضاعفات خطية. بالنسبة للمنطق المتبقي، بما في ذلك المجمع، ومبدل التعدد، ومقارنة الأعداد الصحيحة، والآلة الحالة المحدودة، وما إلى ذلك، نتركها لجدول البحث (LUT). نظراً لأن DSP على FPGA نادر ومكلف، فإننا نستخدمه لتنفيذ الضرب الثقيل فقط. علاوة على ذلك، سنُظهر أن الاعتماد بشكل كامل على LUT لتنفيذ عملية الضرب المعياري ليس اقتصادياً (القسم 4). لذلك، سنركز على استخدام LUT وDSP، ونقلل من المساحة واستخدام DSP دون التضحية بالأداء.

نغلف العمليات التي تشتمل على تكرار داخلي في عنصر معالجة (PE)، كما هو موضح في الشكل 4. يحتوي كل PE على اثنين من المضاعفات لتنفيذ عمليتي الضرب المستقلتين $xy$ و$qm$. ثم يقبل $S_{i-1}^j$ من التكرار الخارجي الأخير، وكلمة حمل (غير موضحة في الشكل)، ويضيفها مع نتائج الضرب، ثم يخرج $S_i^j$ وكلمة حمل. ثم نحدد عدد PE بـ 1، مع توجيه ALLOCATION في HLS. هذا لتجنب انتفاخ الموارد بسبب فك الحلقة، بحيث يتم تخصيص الموارد فقط لحساب تكرار داخلي واحد فعلياً، ولتقليل المساحة الإجمالية للمعمارية الدقيقة.

نوظف أيضاً خوارزمية Karatsuba لبناء مضاعفات محافظة على DSP. كما هو موضح في الخوارزمية 2، تنفذ خوارزمية Karatsuba ضرب الأعداد الصحيحة من خلال تقسيمه بشكل متكرر إلى ثلاثة بنصف الحجم. تُنسب كفاءتها إلى عملية ضرب واحدة أقل من خوارزمية الكتاب المدرسي، ونستفيد منها لتخصيص DSPs وفقاً لعدد العمليات الفعلية. على سبيل المثال، كتلة DSP48E1 قادرة على تنفيذ ضرب $18 \times 25$-بت، وواحد $32 \times 32$ يمكن تقسيمه إلى $16 \times 16$، ويستهلك 3 كتل DSP.

**الخوارزمية 2:** خوارزمية Karatsuba

**المدخل:** المعاملات $X$ و$Y$، طول المعامل $k$

**المخرج:** $S = X \times Y$

1. دع $X = X_h X_l$، $Y = Y_h Y_l$، حيث $X_h, X_l, Y_h, Y_l$ هي أعداد صحيحة $k/2$-بت؛
2. $HH \leftarrow \text{Karatsuba}(X_h, Y_h)$;
3. $LL \leftarrow \text{Karatsuba}(X_l, Y_l)$;
4. $HL \leftarrow \text{Karatsuba}(X_h + X_l, Y_h + Y_l)$;
5. $S \leftarrow HH \cdot 2^k + (HL - HH - LL) \cdot 2^{k/2} + LL$;
6. **أرجع** $S$

### تردد الساعة

تعمل وحدات DSP على Xilinx FPGA بتردد أقصى يبلغ 400-500 ميجاهرتز. للاقتراب من حد التردد، نحتاج إلى الاهتمام بالإجراءات التالية:

- **الإعلان عن المضاعفات كمضاعفات خطية.** يستغرق المضاعف الخطي دورات متعددة لإنجاز الضرب، موزعاً عبء عمله ومخففاً عبء كل دورة. لا يضر بإنتاجية الضرب نظراً لأننا قد حللنا التبعية بين مدخلاته ومخرجاته.

- **تقييد عرض البت للمعاملات.** يكون تردد الساعة مقيداً بالمسار الحرج للدائرة، أي أطول مسار من البوابات يحتاج الإشارة لتمريرها خلال دورة واحدة. العمليات الحسابية على الأعداد الصحيحة مثل الجمع أو المقارنة عادةً ما تؤدي إلى سلسلة حمل طويلة، وبالتالي نحتاج إلى تجنب الحساب على أعداد صحيحة طويلة جداً مباشرة. في هذا العمل، نستخدم 32-بت كحجم للمعامل، والحد الأقصى لعرض البت المتضمن هو 64 بت.

- **تبسيط منطق التحكم.** بالنسبة لآلة الحالة المحدودة المسؤولة عن التحكم في وحدات الحساب، نستخدم نظام ترميز واحد-ساخن لتمثيل الحالات للبحث والمطابقة السريعة. يتعلق عدد الحالات بعدد تكرارات كل حلقة، وبالتالي سيكون ترميز واحد-ساخن مقبولاً.

### استخدام الذاكرة

يخصص تصميمنا لكل معالج Paillier ذاكرة RAM الكتلية الخاصة به (BRAM) كمخزن مؤقت محلي، لحمل بيانات الإدخال/الإخراج والأعداد الصحيحة الكبيرة الوسيطة المتضمنة في الحساب. لا نشارك التخزين بين المعالجات لمنع تنازع الوصول إلى البيانات.

يتم تخزين الأعداد الصحيحة الكبيرة عادةً كمصفوفات من الكلمات في BRAM. ومع ذلك، نلاحظ أن بيانات الإدخال للتشفير، والتي يتم ترميزها من أعداد الفاصلة العائمة المستخدمة في التعلم الآلي، لديها أرقام فعالة قليلة مقارنة بطول الأعداد الصحيحة الكبيرة. لذلك، نحن قادرون على تخزين بيانات الإدخال كمتجه متناثر، أي تسجيل العناصر غير الصفرية ومؤشراتها فقط، مما يقلل من بصمة الذاكرة.

## 3.3 التطبيق

نطور إطار التشفير الخاص بنا باستخدام نسخة AWS F1 ومجموعة تطوير Xilinx SDAccel. يتم تنفيذ المنطق الأساسي لوظيفة التشفير وفك التشفير باستخدام التوليف عالي المستوى Xilinx (HLS)، مما يسمح بتحويل خوارزمية موصوفة في C/C++ إلى تطبيق مخصص على FPGA. يتم إدراج توجيهات مثل جعل الحلقة خطية وتخصيص النسخ في شفرة HLS لضبط أداء المعمارية الناتجة بدقة.

على جانب المضيف، نستخدم واجهة برمجة تطبيقات OpenCL للوصول إلى أجهزة التسريع. توفر واجهة برمجة تطبيقات OpenCL تجريداً لجهاز الحوسبة مثل CPU وGPU وFPGA. يُسمى الاستدعاء لوظيفة الجهاز نواة. يُستخدم OpenCL لإدارة نقل البيانات بين المضيف والجهاز، وقائمة انتظار واستدعاء النوى، ومراقبة أحداث التنفيذ. نعتمد واجهات برمجة تطبيقات PyOpenCL لتنفيذ وحدة تستفيد من جهاز FPGA للعمليات التشفيرية ودمجها في إطار عمل FATE.

يتم تقسيم الطلبات من جانب المضيف إلى دفعات بحجم ثابت، وكل دفعة تستدعي نواة على الجهاز. سيتم وضع نوى متعددة في قائمة انتظار أوامر OpenCL. يساعد هذا على تداخل نقل البيانات مع الحساب وإخفاء الكمون. نخصص أيضاً مخازن مؤقتة على الجهاز مسبقاً، ونرتبها كمخزن مؤقت حلقي، من أجل إعادة استخدام المخازن المؤقتة بين النوى وتجنب تخصيص الذاكرة المتكرر.

---

### Translation Notes

- **Figures referenced:** Figure 2 (System Architecture), Figure 3 (Pipeline Execution), Figure 4 (Processing Element), Figure 5 (Kernel Queueing)
- **Key terms introduced:**
  - Processing Element (PE): عنصر معالجة
  - Karatsuba algorithm: خوارزمية Karatsuba
  - One-hot encoding: ترميز واحد-ساخن
  - Ring buffer: مخزن مؤقت حلقي
  - Sparse vector: متجه متناثر
  - Critical path: المسار الحرج
  - Carry chain: سلسلة حمل
  - BRAM (Block RAM): ذاكرة RAM الكتلية
- **Algorithms:** Algorithm 2 (Karatsuba Algorithm)
- **Equations:**
  - Throughput formula
  - Ideal clock cycle calculations
  - Karatsuba decomposition
- **Citations:** 2 references (Montgomery 1985, Putnam 2014)
- **Special handling:**
  - HLS directives preserved in English: UNROLL, PIPELINE, ALLOCATION
  - Technical specifications maintained: DSP48E1, PCI-e, AWS F1
  - Code-related terms kept in English where appropriate

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.86
