# Section 5: Experimental Setup and Results
## القسم 5: الإعداد التجريبي والنتائج

**Section:** experimental-results
**Translation Quality:** 0.87
**Glossary Terms Used:** processing element, floating point, pipeline, simulation, synthesis, performance, power, area, memory, register file, instruction decoder

---

### English Version

**Figure 11: Experimental Setup**

Experimental setup is shown in figure 11. As shown in the figure 11, we have a Processing Element (PE) and an Auxiliary Processing Element (APE) where PE has compute resources and load/store operations are handled by APE. PE consists of different floating point operations like multiplier, adder, square root, and divider, a small register file, an instruction memory, and an instruction decoder, and APE consists of two small instruction memories, corresponding instruction decoders, and a Local Memory (LM). The operation of PE and APE can be described as follows:

**Step 1:** Load data from upper level of memory to LM in APE

**Step 2:** Load data from LM to Register File

**Step 3:** Perform computations in the PE and store results back in the Register File

**Step 4:** Store results back from Register File to LM

**Step 5:** Store final result to the upper level of memory

As shown in the figure 11, the pipeline depths of the floating point arithmetic units are kept variable. Usually, it is not possible vary pipeline stages of the floating point unit in RTL. For simulation purpose, we use Bluespec System Verilog (BSV) that lets us incorporation of C program along with RTL registers to mimic the different number of pipeline stages for different floating point operations. The simulation environment also becomes non-synthesizable due to presence of floating point operation written in C. For simulation results, we report Cycles-per-Instructions (CPI) for varying number of pipeline stages for adder and multiplier for *matrix-matrix* multiplication, QR factorization, and LU factorization as shown in figure 12. It can be observed in the figure 12 that our simulation results corroborate to our theoretical curve observed in section 3.

**Figure 12: CPI in Matrix Multiplication, QR factorization, and LU factorization with Varying Number of Pipeline Stages in Adder and Multiplier for a Matrix of Size 100 × 100**

**Figure 13: CPI in QR factorization, and LU factorization with Varying Number of Pipeline Stages in Square root and Divider for a Matrix of Size 100 × 100**

For synthesis, we use enhanced version of PE where we attach 4 multipliers and 3 adders in a reconfigurable way to enhance the performance of the PE. Table 1 presents comparison between LAP-PE and PE. It can be observed from the table 1 that PE has more area and consumes more power. This is mainly because of SRAM and DOT4 instruction. If we take GFlops/mm² and GFlops/W as a performance measure as shown in table 2 then at 1.81 GHz, LAP-PE attains 19.92 GFlops/mm² while PE attains 42.09 GFlops/mm². Similarly, at 0.20 GHz, LAP-PE attains 2.37 GFlops/mm² while PE attains 5.09 GFlops/mm².

Similarly, at 1.81 GHz, LAP-PE attains 29.7 GFlops/W while PE attains 28.281 GFlops/W. At 0.95 GHz, LAP-PE attains 46.4 GFlops/W while in PE it is 48.54 GFlops/W. At 0.2 GHz, LAP-PE achieves 51.1 GFlops/W while PE achieves 84.84 GFlops/W.

It can be concluded from above observations that PE performs better than LAP-PE at lower frequencies. This is mainly because lower power consumed by double precision floating point operations at low frequencies.

**TABLE 1: Comparison between LAP-PE and PE at Different Frequencies with 16KBytes of dual-ported SRAM with double precision floating point arithmetic**

| Architecture | Speed (GHz) | Area (mm²) | Memory (mW) | FMAC (mW) | PE (mW) |
|--------------|------------|------------|-------------|-----------|---------|
| LAP-PE | 1.81 | 0.181 | 13.25 | 105.5 | 118.7 |
| LAP-PE | 0.95 | 0.174 | 6.95 | 31.0 | 38.0 |
| LAP-PE | 0.33 | 0.167 | 2.41 | 6.0 | 8.4 |
| LAP-PE | 0.20 | 0.169 | 1.46 | 3.4 | 4.8 |
| PE | 1.81 | 0.301 | 26.50 | 422 | 448.5 |
| PE | 0.95 | 0.28 | 13.90 | 124 | 137.9 |
| PE | 0.33 | 0.273 | 4.82 | 24 | 28.82 |
| PE | 0.20 | 0.275 | 2.92 | 13.6 | 16.5 |

**TABLE 2: Comparison of LAP-PE and PE**

| Speed | LAP-PE (GFlops/mm²) | LAP-PE (GFlops/W) | PE (GFlops/mm²) | PE (GFlops/W) |
|-------|---------------------|-------------------|-----------------|---------------|
| 1.81 | 19.92 | 29.7 | 42.09 | 28.24 |
| 0.95 | 10.92 | 46.4 | 23.75 | 48.54 |
| 0.33 | 3.95 | 57.8 | 8.46 | 82.5 |
| 0.2 | 2.37 | 51.1 | 5.09 | 84.84 |

---

### النسخة العربية

**الشكل 11: الإعداد التجريبي**

يُظهر الإعداد التجريبي في الشكل 11. كما هو موضح في الشكل 11، لدينا عنصر معالجة (PE) وعنصر معالجة مساعد (APE) حيث يحتوي PE على موارد الحوسبة ويتم التعامل مع عمليات التحميل/التخزين بواسطة APE. يتكون PE من عمليات النقطة العائمة المختلفة مثل المضارب والجامع والجذر التربيعي والمقسم، وملف سجل صغير، وذاكرة تعليمات، وفك تشفير تعليمات، ويتكون APE من ذاكرتي تعليمات صغيرتين، وفك تشفير تعليمات مقابلة، وذاكرة محلية (LM). يمكن وصف عملية PE و APE كما يلي:

**الخطوة 1:** تحميل البيانات من المستوى الأعلى للذاكرة إلى LM في APE

**الخطوة 2:** تحميل البيانات من LM إلى ملف السجل

**الخطوة 3:** إجراء الحسابات في PE وتخزين النتائج مرة أخرى في ملف السجل

**الخطوة 4:** تخزين النتائج مرة أخرى من ملف السجل إلى LM

**الخطوة 5:** تخزين النتيجة النهائية في المستوى الأعلى للذاكرة

كما هو موضح في الشكل 11، يتم الاحتفاظ بأعماق خطوط الأنابيب لوحدات الحساب بالنقطة العائمة متغيرة. عادةً، لا يمكن تغيير مراحل خط الأنابيب لوحدة النقطة العائمة في RTL. لأغراض المحاكاة، نستخدم Bluespec System Verilog (BSV) الذي يسمح لنا بدمج برنامج C مع سجلات RTL لمحاكاة العدد المختلف من مراحل خط الأنابيب لعمليات النقطة العائمة المختلفة. تصبح بيئة المحاكاة أيضاً غير قابلة للتوليف بسبب وجود عملية النقطة العائمة المكتوبة بـ C. بالنسبة لنتائج المحاكاة، نبلغ عن الدورات لكل تعليمة (CPI) لعدد متفاوت من مراحل خط الأنابيب للجامع والمضارب لـ *ضرب المصفوفة بالمصفوفة* وتحليل QR وتحليل LU كما هو موضح في الشكل 12. يمكن ملاحظة في الشكل 12 أن نتائج المحاكاة لدينا تؤكد المنحنى النظري الذي لوحظ في القسم 3.

**الشكل 12: CPI في ضرب المصفوفات وتحليل QR وتحليل LU مع عدد متفاوت من مراحل خط الأنابيب في الجامع والمضارب لمصفوفة بحجم 100 × 100**

**الشكل 13: CPI في تحليل QR وتحليل LU مع عدد متفاوت من مراحل خط الأنابيب في الجذر التربيعي والمقسم لمصفوفة بحجم 100 × 100**

للتوليف، نستخدم نسخة محسنة من PE حيث نربط 4 مضاربات و 3 جوامع بطريقة قابلة لإعادة التكوين لتعزيز أداء PE. يقدم الجدول 1 مقارنة بين LAP-PE و PE. يمكن ملاحظة من الجدول 1 أن PE لديه مساحة أكبر ويستهلك طاقة أكثر. هذا يرجع بشكل أساسي إلى SRAM وتعليمة DOT4. إذا أخذنا GFlops/mm² و GFlops/W كمقياس للأداء كما هو موضح في الجدول 2، فعند 1.81 GHz، يحقق LAP-PE 19.92 GFlops/mm² بينما يحقق PE 42.09 GFlops/mm². بالمثل، عند 0.20 GHz، يحقق LAP-PE 2.37 GFlops/mm² بينما يحقق PE 5.09 GFlops/mm².

بالمثل، عند 1.81 GHz، يحقق LAP-PE 29.7 GFlops/W بينما يحقق PE 28.281 GFlops/W. عند 0.95 GHz، يحقق LAP-PE 46.4 GFlops/W بينما في PE يكون 48.54 GFlops/W. عند 0.2 GHz، يحقق LAP-PE 51.1 GFlops/W بينما يحقق PE 84.84 GFlops/W.

يمكن استنتاج من الملاحظات أعلاه أن PE يؤدي أفضل من LAP-PE عند الترددات المنخفضة. هذا يرجع بشكل أساسي إلى استهلاك طاقة أقل من قبل عمليات النقطة العائمة ذات الدقة المزدوجة عند الترددات المنخفضة.

**الجدول 1: مقارنة بين LAP-PE و PE عند ترددات مختلفة مع 16 كيلوبايت من SRAM ثنائي المنفذ مع حساب النقطة العائمة ذات الدقة المزدوجة**

| المعمارية | السرعة (GHz) | المساحة (mm²) | الذاكرة (mW) | FMAC (mW) | PE (mW) |
|-----------|-------------|--------------|--------------|-----------|---------|
| LAP-PE | 1.81 | 0.181 | 13.25 | 105.5 | 118.7 |
| LAP-PE | 0.95 | 0.174 | 6.95 | 31.0 | 38.0 |
| LAP-PE | 0.33 | 0.167 | 2.41 | 6.0 | 8.4 |
| LAP-PE | 0.20 | 0.169 | 1.46 | 3.4 | 4.8 |
| PE | 1.81 | 0.301 | 26.50 | 422 | 448.5 |
| PE | 0.95 | 0.28 | 13.90 | 124 | 137.9 |
| PE | 0.33 | 0.273 | 4.82 | 24 | 28.82 |
| PE | 0.20 | 0.275 | 2.92 | 13.6 | 16.5 |

**الجدول 2: مقارنة LAP-PE و PE**

| السرعة | LAP-PE (GFlops/mm²) | LAP-PE (GFlops/W) | PE (GFlops/mm²) | PE (GFlops/W) |
|--------|---------------------|-------------------|-----------------|---------------|
| 1.81 | 19.92 | 29.7 | 42.09 | 28.24 |
| 0.95 | 10.92 | 46.4 | 23.75 | 48.54 |
| 0.33 | 3.95 | 57.8 | 8.46 | 82.5 |
| 0.2 | 2.37 | 51.1 | 5.09 | 84.84 |

---

### Translation Notes

- **Figures referenced:** Figure 11 (Experimental Setup), Figure 12 (CPI in Matrix Multiplication and Factorizations), Figure 13 (CPI in Factorizations with Square root and Divider)
- **Tables referenced:** Table 1 (Comparison between LAP-PE and PE at Different Frequencies), Table 2 (Comparison of LAP-PE and PE)
- **Key terms introduced:** Processing Element (PE), Auxiliary Processing Element (APE), Local Memory (LM), Register File, Instruction Decoder, Bluespec System Verilog (BSV), RTL, CPI (Cycles-per-Instruction), SRAM, FMAC (Fused Multiply-Accumulate)
- **Equations:** None
- **Citations:** None directly in this section
- **Special handling:** Technical acronyms maintained (PE, APE, LM, BSV, RTL, SRAM, FMAC, DOT4); Performance metrics preserved (GFlops/mm², GFlops/W); All numerical data in tables maintained

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
