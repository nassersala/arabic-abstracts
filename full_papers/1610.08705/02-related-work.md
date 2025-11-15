# Section 2: Related Work
## القسم 2: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.86
**Glossary Terms Used:** pipeline, cache, performance, processor, benchmark, simulator, floating point, architecture, optimization, power

---

### English Version

There is a significant theoretical and experimental work done in the recent past that establishes relation between pipeline depth of a microprocessor and cache size [9][10].

In [9], authors have presented interesting work that focuses on improving processor performance by having deeper pipeline considering Intel Pentium 4 as a baseline case. Relation between processor performance, pipeline depth, and cache size is established for several benchmarks. The paper presents simulator based experimental results. It is concluded that with 100% increase in the performance in the Pentium 4 like processors, performance improvement of 35-90% can be attained. A major shortcoming of the work presented in [9] is that the work presents interesting empirical results and does not establish succinct theory for predicting performance by varying pipeline depth and cache size.

In [10], authors have presented an analytical model that derives optimal pipeline depth as a function of power and performance for a superscalar processor. The model is validated using a cycle accurate simulator of a contemporary superscalar processor. Authors in [10] build on the base case presented in [18] where it is shown that for $s_i$ pipeline stages, if $t_i$ is the latch free time to complete the operation in pipe $i$, then in the scenario where all the pipe stages operate at same frequency, $\frac{t_i}{s_i} = \frac{t_j}{s_j}, \forall i, j$. If $c_i$ is latch overhead in $i^{th}$ pipeline stage than time per stage of pipe $i$ is $T_i = \frac{t_i}{s_i} + c_i, \forall i$. In case of absence of pipeline stalls, throughput of such a machine would be $G = \sum_{i=1}^{k}(\frac{1}{T_i})$, where $k$ is number of pipe stages in the pipeline. In [10], authors have extended this baseline model to incorporate pipeline stalls. The work presented in [10] becomes one of the starting point for the work presented in this paper.

In [19], authors have analyzed trade-off between greater throughput in deeper pipeline and penalty due to hazards in deeper pipeline. Sensitivity in Cycles-per-Instruction and cycle time are considered as parameters to arrive at optimum pipeline depth. It is shown that the total time can be modeled as a sum busy and non busy time of the pipeline considering pipeline hazards as a parameter. Simulation is performed for 35 different types of workloads and it is clearly shown that the optimum pipeline depth varies between 13 to 35 for these workloads. Such a revelation gives us motivation to work further on a class of workloads for the workload specific (or domain specific) accelerator. The theoretical framework presented in [19] forms foundation of our theoretical framework and the framework presented in [19] is revisited in the prelude of section 3.

Theoretical framework presented in [20] is continuation of the theoretical framework presented in [19]. In [20], authors have optimized pipeline for power and performance considering 55 workloads. The problem of optimum pipeline depth is well studied by considering parameters like dynamic power increase, clock gating, and leakage power in [20].

In [21], authors have presented several floating point unit architecture extensions to accelerate matrix factorizations. The work presented in [21] is interesting and through several extension to the floating point unit architecture, significant performance improvement over baseline accelerator is achieved. The limitation of the work presented in [21] is lack of theoretical framework that helps to decide the architectural parameters. The work presented in [21] serves as a major benchmark for the work presented in this paper.

In this paper, we have considered several theoretical and experimental framework as a motivation and/or baseline for our theoretical framework. We dwell on the idea of arriving at optimum pipeline depth for the domain customized accelerator. We perform analysis of the workload which is BLAS and LAPACK in this case and based on that we arrive at optimum pipeline depth of multiplier, adder, square root, and divider for the accelerator. Number of independent operations in the Directed Acyclic Graphs (DAGs) of the several routines BLAS and LAPACK are considered as parameters for floating point unit co-design for domain specific accelerator.

---

### النسخة العربية

هناك عمل نظري وتجريبي كبير تم إنجازه في الماضي القريب يؤسس علاقة بين عمق خط الأنابيب للمعالج الدقيق وحجم الذاكرة المخبئية [9][10].

في [9]، قدم المؤلفون عملاً مثيراً للاهتمام يركز على تحسين أداء المعالج من خلال خط أنابيب أعمق مع اعتبار Intel Pentium 4 كحالة أساسية. تم إنشاء علاقة بين أداء المعالج وعمق خط الأنابيب وحجم الذاكرة المخبئية لعدة معايير. تقدم الورقة نتائج تجريبية قائمة على المحاكي. تم استنتاج أنه مع زيادة بنسبة 100% في الأداء في معالجات مماثلة لـ Pentium 4، يمكن تحقيق تحسين في الأداء بنسبة 35-90%. يتمثل القصور الرئيسي في العمل المقدم في [9] في أن العمل يقدم نتائج تجريبية مثيرة للاهتمام ولا ينشئ نظرية موجزة للتنبؤ بالأداء من خلال تغيير عمق خط الأنابيب وحجم الذاكرة المخبئية.

في [10]، قدم المؤلفون نموذجاً تحليلياً يستمد عمق خط الأنابيب الأمثل كدالة للطاقة والأداء لمعالج فائق القياسية. يتم التحقق من صحة النموذج باستخدام محاكي دقيق للدورات لمعالج فائق القياسية معاصر. يبني المؤلفون في [10] على الحالة الأساسية المقدمة في [18] حيث يُظهر أنه لمراحل خط الأنابيب $s_i$، إذا كان $t_i$ هو الوقت الخالي من المزلاج لإكمال العملية في خط الأنابيب $i$، فإنه في السيناريو حيث تعمل جميع مراحل خط الأنابيب بنفس التردد، $\frac{t_i}{s_i} = \frac{t_j}{s_j}, \forall i, j$. إذا كان $c_i$ هو الحمل الزائد للمزلاج في المرحلة $i$ من خط الأنابيب، فإن الوقت لكل مرحلة من خط الأنابيب $i$ هو $T_i = \frac{t_i}{s_i} + c_i, \forall i$. في حالة عدم وجود توقفات في خط الأنابيب، فإن معدل الإنتاجية لمثل هذه الآلة سيكون $G = \sum_{i=1}^{k}(\frac{1}{T_i})$، حيث $k$ هو عدد مراحل خط الأنابيب في خط الأنابيب. في [10]، قام المؤلفون بتوسيع هذا النموذج الأساسي لدمج توقفات خط الأنابيب. يصبح العمل المقدم في [10] أحد نقاط البداية للعمل المقدم في هذه الورقة.

في [19]، حلل المؤلفون المفاضلة بين معدل إنتاجية أكبر في خط أنابيب أعمق والعقوبة بسبب المخاطر في خط أنابيب أعمق. تُعتبر الحساسية في الدورات لكل تعليمة ووقت الدورة معاملات للوصول إلى عمق خط الأنابيب الأمثل. يُظهر أنه يمكن نمذجة الوقت الإجمالي كمجموع الوقت المشغول وغير المشغول لخط الأنابيب مع اعتبار مخاطر خط الأنابيب كمعامل. تم إجراء المحاكاة لـ 35 نوعاً مختلفاً من أحمال العمل ويُظهر بوضوح أن عمق خط الأنابيب الأمثل يتراوح بين 13 إلى 35 لأحمال العمل هذه. يعطينا مثل هذا الكشف دافعاً للعمل أكثر على فئة من أحمال العمل لمسرّع خاص بحمل العمل (أو خاص بالمجال). يشكل الإطار النظري المقدم في [19] أساس إطارنا النظري ويتم إعادة النظر في الإطار المقدم في [19] في مقدمة القسم 3.

الإطار النظري المقدم في [20] هو استمرار للإطار النظري المقدم في [19]. في [20]، قام المؤلفون بتحسين خط الأنابيب للطاقة والأداء مع اعتبار 55 حمل عمل. تمت دراسة مشكلة عمق خط الأنابيب الأمثل جيداً من خلال اعتبار معاملات مثل زيادة الطاقة الديناميكية وبوابات الساعة وطاقة التسرب في [20].

في [21]، قدم المؤلفون العديد من امتدادات معمارية وحدة النقطة العائمة لتسريع تحليل المصفوفات. العمل المقدم في [21] مثير للاهتمام ومن خلال العديد من الامتدادات لمعمارية وحدة النقطة العائمة، تم تحقيق تحسين كبير في الأداء مقارنة بالمسرّع الأساسي. يتمثل قيد العمل المقدم في [21] في الافتقار إلى إطار نظري يساعد في تحديد المعاملات المعمارية. يعمل العمل المقدم في [21] كمعيار رئيسي للعمل المقدم في هذه الورقة.

في هذه الورقة، اعتبرنا العديد من الأطر النظرية والتجريبية كدافع و/أو خط أساس لإطارنا النظري. نتعمق في فكرة الوصول إلى عمق خط الأنابيب الأمثل للمسرّع المخصص للمجال. نقوم بإجراء تحليل لحمل العمل وهو BLAS و LAPACK في هذه الحالة وبناءً على ذلك نصل إلى عمق خط الأنابيب الأمثل للمضارب والجامع والجذر التربيعي والمقسم للمسرّع. يُعتبر عدد العمليات المستقلة في الرسوم البيانية غير الدورية الموجهة (DAGs) للعديد من برامج BLAS و LAPACK معاملات للتصميم المشترك لوحدة النقطة العائمة للمسرّع الخاص بالمجال.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** Cycles-per-Instruction (CPI), cycle accurate simulator, pipeline stalls, throughput, Directed Acyclic Graphs (DAGs), latch overhead, clock gating
- **Equations:** 3 equations referenced in text ($\frac{t_i}{s_i} = \frac{t_j}{s_j}$, $T_i = \frac{t_i}{s_i} + c_i$, $G = \sum_{i=1}^{k}(\frac{1}{T_i})$)
- **Citations:** [9], [10], [18], [19], [20], [21] referenced
- **Special handling:** Mathematical notation preserved in LaTeX format; Intel Pentium 4 kept in English

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86
