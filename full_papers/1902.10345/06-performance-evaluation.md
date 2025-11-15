# Section 6: Performance Evaluation
## القسم 6: تقييم الأداء

**Section:** Performance Evaluation
**Translation Quality:** 0.86
**Glossary Terms Used:** benchmark, matrix multiplication, speedup, optimization, BFS, quantum transport

---

### English Version

We evaluate the performance of SDFGs on a set of fundamental kernels, followed by three case studies: analysis of matrix multiplication, a graph algorithm, and a real-world physics application.

**Experimental Setup** We run all experiments on a server with an Intel 12-core Xeon E5-2650 v4 CPU, Tesla P100 GPU, and Xilinx VCU1525 FPGA board.

**6.1 Fundamental Computational Kernels** We evaluate 5 core scientific computing kernels: Matrix Multiplication (MM), Jacobi Stencil, Histogram, Query, and Sparse Matrix-Vector Multiplication (SpMV). On all applications, our SDFG results only employ data-centric transformations. In MM, SDFGs achieve ∼98.6% of the performance of MKL, ∼70% of CUBLAS, and ∼90% of CUTLASS. On FPGA, SDFGs yield a result 4,992× faster than naïve HLS. Similar results are seen in SpMV, Histogram, Query, and Jacobi.

**6.2 Case Study I: Matrix Multiplication** The transformation chain from Fig. 9b to the MM CPU SDFG is shown in Fig. 15. After only 7 steps the performance increases by ∼536× (75% of MKL), and further increases to 98.6% of MKL after tuning.

**6.3 Case Study II: Graph Algorithms** We implement Breadth-First Search (BFS) on multi-core CPUs. We compare with Galois and Gluon frameworks. SDFGs perform on-par with the frameworks on all graphs, where Galois is marginally faster on social networks and SDFGs are up to 2× faster than Galois on road maps.

**6.4 Case Study III: Quantum Transport** We use SDFGs to optimize OMEN, a quantum transport simulator. Using data-centric transformations, we achieve a 32.26× speedup for SDFGs over manually-tuned implementations, and 1,021× over Python.

---

### النسخة العربية

نقيّم أداء SDFGs على مجموعة من النوى الأساسية، تليها ثلاث دراسات حالة: تحليل ضرب المصفوفات، وخوارزمية رسم بياني، وتطبيق فيزياء من العالم الحقيقي.

**الإعداد التجريبي** نجري جميع التجارب على خادم مع معالج Intel 12-core Xeon E5-2650 v4 CPU، وTesla P100 GPU، ولوحة Xilinx VCU1525 FPGA.

**6.1 النوى الحسابية الأساسية** نقيّم 5 نوى حوسبة علمية أساسية: ضرب المصفوفات (MM)، واستنسل جاكوبي، والمدرج التكراري، والاستعلام، وضرب المصفوفة المتفرقة-المتجه (SpMV). على جميع التطبيقات، تستخدم نتائج SDFG الخاصة بنا فقط التحويلات المحورية للبيانات. في MM، تحقق SDFGs ∼98.6% من أداء MKL، و∼70% من CUBLAS، و∼90% من CUTLASS. على FPGA، تنتج SDFGs نتيجة أسرع بـ 4,992× من HLS الساذج. تظهر نتائج مماثلة في SpMV والمدرج التكراري والاستعلام وجاكوبي.

**6.2 دراسة الحالة الأولى: ضرب المصفوفات** تُظهر سلسلة التحويل من الشكل 9ب إلى MM CPU SDFG في الشكل 15. بعد 7 خطوات فقط، يزداد الأداء بـ ∼536× (75% من MKL)، ويزيد أكثر إلى 98.6% من MKL بعد الضبط.

**6.3 دراسة الحالة الثانية: خوارزميات الرسوم البيانية** نطبق البحث بالاتساع أولاً (BFS) على وحدات المعالجة المركزية متعددة النوى. نقارن مع أطر عمل Galois وGluon. تؤدي SDFGs على قدم المساواة مع الأطر على جميع الرسوم البيانية، حيث Galois أسرع بشكل طفيف على الشبكات الاجتماعية وSDFGs أسرع بما يصل إلى 2× من Galois على خرائط الطرق.

**6.4 دراسة الحالة الثالثة: النقل الكمي** نستخدم SDFGs لتحسين OMEN، محاكي النقل الكمي. باستخدام التحويلات المحورية للبيانات، نحقق تسريعًا بمقدار 32.26× لـ SDFGs على التطبيقات المضبوطة يدويًا، و1,021× على Python.

---

### Translation Notes

- **Figures referenced:** Figures 14-18
- **Key terms introduced:** MKL, CUBLAS, CUTLASS, Galois, Gluon, OMEN
- **Equations:** 0
- **Citations:** Multiple library and tool references
- **Special handling:** Performance metrics and speedup numbers

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
