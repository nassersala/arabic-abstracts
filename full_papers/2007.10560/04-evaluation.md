# Section 4: Evaluation
## القسم 4: التقييم

**Section:** Evaluation
**Translation Quality:** 0.87
**Glossary Terms Used:** FPGA, modular multiplication, Montgomery algorithm, Paillier cryptosystem, DSP, throughput, encryption, decryption, federated learning, logistic regression, linear regression, benchmark, performance, optimization, hardware accelerator, multicore processor

---

### English Version

We conduct experiments aiming to perform an extensive evaluation on the proposed encryption framework. We first perform a microscopic examination, comparing the implementation of Paillier algorithm and ModMult operation with software solutions and existing FPGA designs. Then we study its improvement on the overall performance of training process of federated learning. The training tasks are carried out on the open-sourced version of the FATE machine learning framework. We choose two linear models, and adopt Kaggle datasets on breast cancer¹ and motor temperature² and partition the datasets vertically.

We attempt to answer the following questions empirically with the evaluation experiments:
- How do the Paillier processors perform, especially for the ModMult operation, in terms of throughput and resource-efficiency?
- How does the hardware framework compare with software solutions of Paillier cryptosystem in terms of en/decryption throughput?
- How much does the framework affect the training throughput of federated learning with respect to different models or algorithms?

¹https://www.kaggle.com/uciml/breast-cancer-wisconsin-data
²https://www.kaggle.com/wkirgsn/electric-motor-temperature

**Table 1:** Comparison of ModMult operation

| Implementation | Area (slice) | DSP | Clock frequency (MHz) | Execution time (μs) | Throughput per DSP (op/s) |
|----------------|--------------|-----|----------------------|---------------------|---------------------------|
| This work | 483 | 9 | 500 | 8.81 | 12626 |
| [San and At, 2014] | 567 | 13 | 490 | 8.64 | 8903 |
| [Song et al., 2010] | 180 | 1 | 447 | 135.4 | 7385 |
| [Huang et al., 2011] | 9268 | NA | 129 | 18.70 | NA |

Given the broad adoption of the ModMult operation, many implementation has been proposed by researchers, and we compare ours with them in Table 1. Since we are targeting datacenter acceleration chips and applications, the DSP efficiency is a key factor evaluating an implementation. Comparing with the state of the art solution [San and At, 2014], our ModMult module delivers a close latency but uses fewer DSPs due to our precise limit on resource usage. The authors of [Song et al., 2010] proposes an implementation using only one DSP and one block RAM. However, without employing the Karatsuba algorithm, their version turns out to be less efficient than ours. [Huang et al., 2011] gives an implementation using circuit elements entirely without DSP, and it shows that an such a ModMult module consumes much area and limits the clock frequency, and hence not recommendable. Moreover, most of existing solutions are based on register-transfer level (RTL) that describes the circuit directly, but lacks the flexibility of parametrizing and reusing the ModMult module as our HLS version does.

To evaluate the effectiveness of the scheduling of ModMult operation, we compare the number of execution clock cycles with the theoretically ideal clock cycle, given as $T = (l/k)(l/k+1)$ (Section 3). As shown in Figure 6, for different sizes of operands, our implementation keeps no more than 10% higher than the ideal. The gap is mainly due to pipeline stages, time for initialization and data transfer.

To investigate the performance of FPGA and software solution, we compare the framework with PHE, a popular Paillier library, as shown in Figure 8 and 9. We can see that for a 1024-bit public key, our framework delivers an acceleration ratio of 10.62 and 2.76 for encryption and decryption, respectively. We also compare FPGA with a multicore processor using libpaillier library, as shown in Figure 7. It shows that an FPGA effectively outperforms a multicore CPU and is advisable to be used in accelerating computational intensive applications.

Additionally, we test the modified FATE with linear models and the breast and motor datasets. We train a logistic regression and a linear regression model on the two datasets respectively for 10 iterations, and record the timing. Figure 10 and Figure 11 show the training iteration time and the encryption time in each iteration respectively. It demonstrates that for linear models, our framework reduce the training iteration time by up to 26%, and the encryption time during one iteration by 71.2%.

**Figure 6:** Number of execution clock cycles of ModMult operation
- Shows comparison between "Our impl." and "Ideal" for operand lengths from 1000 to 4500 bits
- Our implementation maintains close to ideal performance (within 10%)

**Figure 7:** Throughput of FPGA and multicore processor
- Compares encryption and decryption throughput for 1 core, 2 cores, 8 cores, and FPGA
- FPGA shows superior performance over multicore CPU

**Figure 8:** Encryption Throughput Compared with Software
- Compares "PHE(CPU)" vs "Ours" for public key sizes 1024, 2048, 3072 bits
- Shows significant improvement with FPGA implementation

**Figure 9:** Decryption Throughput Compared with Software
- Compares "PHE(CPU)" vs "Ours" for public key sizes 1024, 2048, 3072 bits
- Demonstrates acceleration in decryption operations

**Figure 10:** Improvement on Iteration Time
- Compares "Vanilla FATE" vs "Ours" for Logistic regression and Linear regression
- Shows up to 26% reduction in iteration time

**Figure 11:** Improvement on Encryption Time Per Iteration
- Compares "Vanilla FATE" vs "Ours" for Logistic regression and Linear regression
- Shows 71.2% reduction in encryption time

---

### النسخة العربية

نجري تجارب تهدف إلى إجراء تقييم شامل على إطار التشفير المقترح. نقوم أولاً بإجراء فحص مجهري، مقارنة تطبيق خوارزمية Paillier وعملية الضرب المعياري مع الحلول البرمجية وتصاميم FPGA الموجودة. ثم ندرس تحسينها على الأداء العام لعملية تدريب التعلم الاتحادي. يتم تنفيذ مهام التدريب على النسخة مفتوحة المصدر من إطار عمل التعلم الآلي FATE. نختار نموذجين خطيين، ونعتمد مجموعات بيانات Kaggle عن سرطان الثدي¹ ودرجة حرارة المحرك² ونقسم مجموعات البيانات عمودياً.

نحاول الإجابة على الأسئلة التالية تجريبياً من خلال تجارب التقييم:
- كيف تؤدي معالجات Paillier، خاصة لعملية الضرب المعياري، من حيث الإنتاجية وكفاءة الموارد؟
- كيف يقارن إطار الأجهزة مع الحلول البرمجية لنظام Paillier التشفيري من حيث إنتاجية التشفير/فك التشفير؟
- ما مقدار تأثير الإطار على إنتاجية تدريب التعلم الاتحادي فيما يتعلق بالنماذج أو الخوارزميات المختلفة؟

¹https://www.kaggle.com/uciml/breast-cancer-wisconsin-data
²https://www.kaggle.com/wkirgsn/electric-motor-temperature

**الجدول 1:** مقارنة عملية الضرب المعياري

| التطبيق | المساحة (شريحة) | DSP | تردد الساعة (ميجاهرتز) | زمن التنفيذ (ميكروثانية) | الإنتاجية لكل DSP (عملية/ثانية) |
|---------|------------------|-----|------------------------|---------------------------|----------------------------------|
| هذا العمل | 483 | 9 | 500 | 8.81 | 12626 |
| [San and At, 2014] | 567 | 13 | 490 | 8.64 | 8903 |
| [Song et al., 2010] | 180 | 1 | 447 | 135.4 | 7385 |
| [Huang et al., 2011] | 9268 | غ/م | 129 | 18.70 | غ/م |

نظراً للاعتماد الواسع لعملية الضرب المعياري، اقترح العديد من الباحثين تطبيقات، ونقارن تطبيقنا معها في الجدول 1. نظراً لأننا نستهدف شرائح تسريع مراكز البيانات والتطبيقات، فإن كفاءة DSP هي عامل رئيسي لتقييم التطبيق. بالمقارنة مع الحل الحديث [San and At, 2014]، توفر وحدة الضرب المعياري الخاصة بنا كموناً قريباً ولكنها تستخدم عدداً أقل من DSP بسبب الحد الدقيق على استخدام الموارد. يقترح مؤلفو [Song et al., 2010] تطبيقاً يستخدم DSP واحد فقط وذاكرة RAM كتلية واحدة. ومع ذلك، بدون استخدام خوارزمية Karatsuba، تبين أن نسختهم أقل كفاءة من نسختنا. يقدم [Huang et al., 2011] تطبيقاً يستخدم عناصر الدائرة بالكامل بدون DSP، ويُظهر أن مثل هذه الوحدة للضرب المعياري تستهلك مساحة كبيرة وتحد من تردد الساعة، وبالتالي غير موصى به. علاوة على ذلك، تعتمد معظم الحلول الموجودة على مستوى النقل على السجل (RTL) الذي يصف الدائرة مباشرة، لكنه يفتقر إلى مرونة معاملة وإعادة استخدام وحدة الضرب المعياري كما تفعل نسخة HLS الخاصة بنا.

لتقييم فعالية جدولة عملية الضرب المعياري، نقارن عدد دورات ساعة التنفيذ مع دورة الساعة المثالية نظرياً، المعطاة بـ $T = (l/k)(l/k+1)$ (القسم 3). كما هو موضح في الشكل 6، لأحجام مختلفة من المعاملات، يحافظ تطبيقنا على أن لا يكون أعلى من 10% من المثالي. الفجوة ترجع بشكل رئيسي إلى مراحل خط الأنابيب، والوقت للتهيئة ونقل البيانات.

للتحقيق في أداء FPGA والحل البرمجي، نقارن الإطار مع PHE، مكتبة Paillier الشائعة، كما هو موضح في الشكلين 8 و9. يمكننا أن نرى أنه لمفتاح عام بحجم 1024-بت، يوفر إطارنا نسبة تسريع تبلغ 10.62 و2.76 للتشفير وفك التشفير، على التوالي. نقارن أيضاً FPGA مع معالج متعدد النوى باستخدام مكتبة libpaillier، كما هو موضح في الشكل 7. يُظهر أن FPGA يتفوق بشكل فعال على وحدة المعالجة المركزية متعددة النوى ويُنصح باستخدامه في تسريع التطبيقات المكثفة حسابياً.

بالإضافة إلى ذلك، نختبر FATE المعدل مع النماذج الخطية ومجموعات بيانات الثدي والمحرك. نُدرب نموذج انحدار لوجستي ونموذج انحدار خطي على مجموعتي البيانات على التوالي لـ 10 تكرارات، ونسجل التوقيت. يُظهر الشكل 10 والشكل 11 وقت تكرار التدريب ووقت التشفير في كل تكرار على التوالي. يُثبت أنه للنماذج الخطية، يقلل إطارنا من وقت تكرار التدريب بنسبة تصل إلى 26%، ووقت التشفير خلال تكرار واحد بنسبة 71.2%.

**الشكل 6:** عدد دورات ساعة التنفيذ لعملية الضرب المعياري
- يُظهر مقارنة بين "تطبيقنا" و"المثالي" لأطوال معاملات من 1000 إلى 4500 بت
- يحافظ تطبيقنا على أداء قريب من المثالي (ضمن 10%)

**الشكل 7:** إنتاجية FPGA والمعالج متعدد النوى
- يقارن إنتاجية التشفير وفك التشفير لـ 1 نواة، 2 نواة، 8 نوى، وFPGA
- يُظهر FPGA أداءً متفوقاً على وحدة المعالجة المركزية متعددة النوى

**الشكل 8:** إنتاجية التشفير مقارنة بالبرمجيات
- يقارن "PHE(CPU)" مقابل "تطبيقنا" لأحجام مفاتيح عامة 1024، 2048، 3072 بت
- يُظهر تحسناً كبيراً مع تطبيق FPGA

**الشكل 9:** إنتاجية فك التشفير مقارنة بالبرمجيات
- يقارن "PHE(CPU)" مقابل "تطبيقنا" لأحجام مفاتيح عامة 1024، 2048، 3072 بت
- يُثبت التسريع في عمليات فك التشفير

**الشكل 10:** التحسين في وقت التكرار
- يقارن "FATE الأصلي" مقابل "تطبيقنا" للانحدار اللوجستي والانحدار الخطي
- يُظهر انخفاضاً يصل إلى 26% في وقت التكرار

**الشكل 11:** التحسين في وقت التشفير لكل تكرار
- يقارن "FATE الأصلي" مقابل "تطبيقنا" للانحدار اللوجستي والانحدار الخطي
- يُظهر انخفاضاً بنسبة 71.2% في وقت التشفير

---

### Translation Notes

- **Tables referenced:** Table 1 (ModMult operation comparison)
- **Figures referenced:** Figures 6-11 (performance comparisons and evaluations)
- **Key terms introduced:**
  - Throughput per DSP: الإنتاجية لكل DSP
  - Execution time: زمن التنفيذ
  - Acceleration ratio: نسبة تسريع
  - Vanilla FATE: FATE الأصلي
  - Multicore processor: معالج متعدد النوى
- **Datasets:** Kaggle breast cancer and motor temperature datasets
- **Performance metrics:**
  - 10.62x encryption speedup
  - 2.76x decryption speedup
  - 26% iteration time reduction
  - 71.2% encryption time reduction
- **Citations:** 3 references cited ([San and At, 2014], [Song et al., 2010], [Huang et al., 2011])
- **Special handling:**
  - Table 1 formatted with Arabic headers while preserving numeric data
  - Figure descriptions maintained in both languages
  - Performance percentages and ratios preserved accurately
  - URLs for datasets kept in English

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
