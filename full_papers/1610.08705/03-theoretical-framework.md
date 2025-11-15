# Section 3: Theoretical Framework
## القسم 3: الإطار النظري

**Section:** theoretical-framework
**Translation Quality:** 0.85
**Glossary Terms Used:** pipeline, hazard, performance, optimization, floating point, architecture, throughput, latency, workload, processor

---

### English Version

In the initial part of this section, we revisit theory presented in [9], [10], and [19]. Latter we extend theory for domain customized architectures by considering workload characterization. The total time $T$ for the pipeline of the processor can be given by

$$T = T_{BZ} + T_{NBZ}$$
(1)

where $T_{BZ}$, and $T_{NBZ}$ represent busy and non-busy time respectively. Typically, $T_{BZ}$ is when pipeline is busy while $T_{NBZ}$ is when pipeline is stalled due one of the hazards. From [19], ratio of total time $T$ to the total number of instructions $N_I$ is given by

$$\frac{T}{N_I} = (t_o + \frac{\gamma N_H t_p}{N_I}) + (\frac{t_p}{p}) + (\frac{\gamma N_H t_o p}{N_I})$$
(2)

In equation 2, $t_p$ is the total logic delay of the processor, $p$ is the number of pipeline stages in the design, $t_o$ is the latch overhead for the technology, $N_I$ is total number of instructions, $N_H$ is total number of pipeline hazards, and $\gamma = \frac{1}{N_H}\sum^{N_H} \beta_h$ where $\beta_h$ is the fraction of the total pipeline delay encountered by each particular hazard.

In equation 2, the first term is independent of pipeline depth; the second term varies inversely with $p$; and the last term varies linearly with $p$. To obtain minimum at particular value of $p$, equation 2 can be differentiated and equated to 0. That will give

$$p_{opt}^2 = \frac{N_I t_p}{\gamma N_H t_o}$$
(3)

Few observations about optimum pipeline depth can be made from equation 3. As $t_o$ which is latch overhead decreases with lowering node of technology, optimum pipeline depth increases. Lower the hazards in the workload the pipeline depth increases. As $\gamma$ which is fraction of the pipeline that hazards stall decreases, the optimum pipeline depth increases.

We extend this theory for BLAS and LAPACK through workload characterization where we consider characteristics of the specific workload to arrive at an optimum pipeline depth of different operations in encountered in the workload. To extend theoretical frame work, we consider analytical pipeline model presented in [10] that encompasses several pipes namely fixed point unit pipe, load-store pipe, and branch pipe. We extend the theoretical model presented in [10] and incorporate a floating point pipe as shown in figure 1.

**Figure 1: Pipeline Model**

As shown in the figure 1, the model has four pipes: fixed point, floating point, load store, and branch. Since, in BLAS and LAPACK, the operations are floating point in nature and the operations encountered are multiply, addition, division, and square root, we further divide floating point unit pipeline into multiplier pipe, adder pipe, divide pipe, and square root pipelines. Our objective is to arrive at an optimum pipeline depth of these floating point hardware units. The types of arithmetic instructions encountered in BLAS and LAPACK can be given by a set $K = \{M, A, S, D\}$ where $M$, $A$, $S$, and $D$ are for multiplication, adder, square root and divider instructions respectively. The total number of instructions in a routine of BLAS and/or LAPACK is given by

$$N_I = \sum_K N_i^I \text{ where } i \in K$$
(4)

Similarly, total number of hazards are given by

$$N_H = \sum_K N_i^H \text{ where } i \in K$$
(5)

To arrive at an optimum pipeline depth of the each individual pipes shown in the figure 1, we can replace $N_I$ and $N_H$ by corresponding pipe parameters. From equation 2, Time per Instruction (TPI) is given by

$$TPI = \sum_K \frac{T_i}{N_i^I} \text{ where } i \in K$$
(6)

where $T_i = (t_o + \frac{\gamma N_i^H t_p}{N_i^I}) + (\frac{t_p}{p}) + (\frac{\gamma N_i^H t_o p}{N_i^I}), i \in K$. $T_M$, $T_A$, $T_D$, and $T_S$ are the total execution times for multiplier, adder, divider, and square root pipelines for an instruction stream. Parameter $t_o$ is technology dependent and not dependent on the type of the instruction. Equation 3 can be modified as

$$p_{opt_i}^2 = \frac{N_i^I t_{p_i}}{\gamma_i N_i^H t_o} \text{ where } i \in K$$
(7)

In equation 7, $p_M$, $p_A$, $p_D$, and $p_S$ is the total number of pipeline stages in multiplier, adder, divider, and square root hardware units respectively. Similarly, $\gamma_M$, $\gamma_A$, $\gamma_D$, and $\gamma_S$ are the total pipeline delay for each pipeline averaged over total number of hazards for each pipe. From [19], $\gamma = \frac{1}{N_H}\sum^{N_H} \beta_h$ where $\beta_h$ is fraction of total pipeline delay encountered by each particular hazard.

In general, in absence of workload characterization, we can vary different parameters like $\gamma$, $N_I$, $N_H$, and $p$ in equation 2 and comment on effect of different parameters on the time $T$.

**Figure 2: TPI for Different Sizes of Workload for 2, 4, 6, and 8 (keeping $\frac{N_H}{N_I}$ = 0.1, 0.01, and 0.001)**

In figure 2, it can be observed that for a fixed number of pipeline stages $p$, as the problem size increases, the TPI saturates. For example, $p = 2$ and $\frac{N_H}{N_I}$ = 0.1, 0.01, and 0.001 then TPI saturates at instruction count of $10 \times 10^5$ in the workload. This is mainly because smaller pipelines require large number of instruction to saturate and approach lower bound of TPI. It can also be observed in the figure 2 that for relatively larger pipelines (for $p = 4, 6$, and 8) attained TPI progressively increases. This is mainly because of increased operating frequency of the pipeline stages.

Effect on TPI of varying pipeline depth for a particular workload with varying hazards is shown in figure 3. It can be observed in the figure 3 that as we increase pipeline depth, TPI decreases and optimum is achieved. Beyond optimum, a linear increase in the TPI is observed. It can also be observed that the theoretical curve presented in 3 is fairly flat around optimum leaving considerable scope in choosing best design point for the optimum pipeline depth.

**Figure 3: TPI for Different Pipeline Stages $p$ and Varying Workload (keeping $\frac{N_H}{N_I}$ = 0.1, 0.01, 0.001, 0.2, 0.4, 0.6, and 0.8)**

Effect of varying $\gamma$ and pipeline stages $p$ on TPI is shown in figure 4. It can be observed in the figure 4 that for a smaller values of $\gamma$, optimum achieved in the theoretical curve is around 4 and as we increase value of $\gamma$, a deeper pipeline becomes optimum pipeline. From the figures 2, 3, and 4, we can make following remarks:

**Figure 4: TPI for Different Pipeline Stages $p$ and $\gamma$ = 0.1, 0.2, 0.4, 0.6, and 0.8**

**Remark 1:** Pipeline will saturate as we increase the size of the workload. Higher the ratio $\frac{N_H}{N_I}$, worse TPI is attained for small size of workloads.

**Remark 2:** Higher the ratio $\frac{N_H}{N_I}$, shallow the optimum pipeline depth for the workload. It is better to have less number of pipeline stages if workload contains large number of hazards. For large number of hazards, if pipeline stages are higher than the optimum pipeline stages then the TPI attained deteriorates significantly as shown by red line (for $\frac{N_H}{N_I}$ = 0.8) in the figure 3

**Remark 3:** Parameter $\gamma$ that solely depends on the total number of hazards $N_H$ and $\beta_h$ which is fraction of the total pipeline delay encountered by each particular hazard plays an important role in determination of optimum pipeline depth. For large value of $\gamma$, if the pipeline stages are more than 20 and increased further, TPI deteriorates significantly as shown by blue line in the figure 4. For small value of $\gamma$, even if the number of pipeline stages are increased beyond optimum number, the increase in TPI is observed minimal

Based on the observations from the theoretical curves in the figures 2, 3, and 4, we can establish that it is important to characterize workloads of the domain of interest to arrive at an optimum pipeline depth of the different operations encountered in the computations pertaining to the domain.

---

### النسخة العربية

في الجزء الأول من هذا القسم، نعيد النظر في النظرية المقدمة في [9] و[10] و[19]. لاحقاً نوسع النظرية للمعماريات المخصصة للمجال من خلال اعتبار توصيف حمل العمل. يمكن إعطاء الوقت الإجمالي $T$ لخط أنابيب المعالج بواسطة

$$T = T_{BZ} + T_{NBZ}$$
(1)

حيث $T_{BZ}$ و $T_{NBZ}$ يمثلان الوقت المشغول وغير المشغول على التوالي. عادةً، $T_{BZ}$ هو عندما يكون خط الأنابيب مشغولاً بينما $T_{NBZ}$ هو عندما يتوقف خط الأنابيب بسبب أحد المخاطر. من [19]، نسبة الوقت الإجمالي $T$ إلى إجمالي عدد التعليمات $N_I$ تُعطى بواسطة

$$\frac{T}{N_I} = (t_o + \frac{\gamma N_H t_p}{N_I}) + (\frac{t_p}{p}) + (\frac{\gamma N_H t_o p}{N_I})$$
(2)

في المعادلة 2، $t_p$ هو التأخير المنطقي الإجمالي للمعالج، $p$ هو عدد مراحل خط الأنابيب في التصميم، $t_o$ هو الحمل الزائد للمزلاج للتكنولوجيا، $N_I$ هو إجمالي عدد التعليمات، $N_H$ هو إجمالي عدد مخاطر خط الأنابيب، و $\gamma = \frac{1}{N_H}\sum^{N_H} \beta_h$ حيث $\beta_h$ هو جزء من التأخير الإجمالي لخط الأنابيب الذي يواجهه كل خطر معين.

في المعادلة 2، الحد الأول مستقل عن عمق خط الأنابيب؛ يتغير الحد الثاني عكسياً مع $p$؛ ويتغير الحد الأخير خطياً مع $p$. للحصول على الحد الأدنى عند قيمة معينة من $p$، يمكن تفاضل المعادلة 2 ومساواتها بـ 0. سيعطي ذلك

$$p_{opt}^2 = \frac{N_I t_p}{\gamma N_H t_o}$$
(3)

يمكن عمل بعض الملاحظات حول عمق خط الأنابيب الأمثل من المعادلة 3. مع انخفاض $t_o$ وهو الحمل الزائد للمزلاج مع خفض عقدة التكنولوجيا، يزداد عمق خط الأنابيب الأمثل. كلما انخفضت المخاطر في حمل العمل، يزداد عمق خط الأنابيب. مع انخفاض $\gamma$ وهو جزء من خط الأنابيب الذي توقفه المخاطر، يزداد عمق خط الأنابيب الأمثل.

نوسع هذه النظرية لـ BLAS و LAPACK من خلال توصيف حمل العمل حيث نعتبر خصائص حمل العمل المحدد للوصول إلى عمق خط أنابيب أمثل للعمليات المختلفة التي تُواجه في حمل العمل. لتوسيع الإطار النظري، نعتبر نموذج خط الأنابيب التحليلي المقدم في [10] الذي يشمل عدة خطوط أنابيب وهي خط أنابيب وحدة النقطة الثابتة وخط أنابيب التحميل والتخزين وخط أنابيب التفريع. نوسع النموذج النظري المقدم في [10] وندمج خط أنابيب النقطة العائمة كما هو موضح في الشكل 1.

**الشكل 1: نموذج خط الأنابيب**

كما هو موضح في الشكل 1، يحتوي النموذج على أربعة خطوط أنابيب: النقطة الثابتة والنقطة العائمة والتحميل والتخزين والتفريع. نظراً لأن العمليات في BLAS و LAPACK هي ذات طبيعة النقطة العائمة والعمليات التي تُواجه هي الضرب والجمع والقسمة والجذر التربيعي، نقسم خط أنابيب وحدة النقطة العائمة بشكل أكبر إلى خط أنابيب المضارب وخط أنابيب الجامع وخط أنابيب القسمة وخطوط أنابيب الجذر التربيعي. هدفنا هو الوصول إلى عمق خط أنابيب أمثل لوحدات الأجهزة للنقطة العائمة هذه. يمكن إعطاء أنواع تعليمات الحساب التي تُواجه في BLAS و LAPACK بواسطة مجموعة $K = \{M, A, S, D\}$ حيث $M$ و $A$ و $S$ و $D$ للضرب والجمع والجذر التربيعي وتعليمات القسمة على التوالي. يُعطى إجمالي عدد التعليمات في برنامج BLAS و/أو LAPACK بواسطة

$$N_I = \sum_K N_i^I \text{ حيث } i \in K$$
(4)

بالمثل، يُعطى إجمالي عدد المخاطر بواسطة

$$N_H = \sum_K N_i^H \text{ حيث } i \in K$$
(5)

للوصول إلى عمق خط أنابيب أمثل لكل خط أنابيب فردي موضح في الشكل 1، يمكننا استبدال $N_I$ و $N_H$ بمعاملات خط الأنابيب المقابلة. من المعادلة 2، يُعطى الوقت لكل تعليمة (TPI) بواسطة

$$TPI = \sum_K \frac{T_i}{N_i^I} \text{ حيث } i \in K$$
(6)

حيث $T_i = (t_o + \frac{\gamma N_i^H t_p}{N_i^I}) + (\frac{t_p}{p}) + (\frac{\gamma N_i^H t_o p}{N_i^I}), i \in K$. $T_M$ و $T_A$ و $T_D$ و $T_S$ هي أوقات التنفيذ الإجمالية لخطوط أنابيب المضارب والجامع والمقسم والجذر التربيعي لتدفق التعليمات. المعامل $t_o$ يعتمد على التكنولوجيا ولا يعتمد على نوع التعليمة. يمكن تعديل المعادلة 3 كـ

$$p_{opt_i}^2 = \frac{N_i^I t_{p_i}}{\gamma_i N_i^H t_o} \text{ حيث } i \in K$$
(7)

في المعادلة 7، $p_M$ و $p_A$ و $p_D$ و $p_S$ هو إجمالي عدد مراحل خط الأنابيب في وحدات الأجهزة للمضارب والجامع والمقسم والجذر التربيعي على التوالي. بالمثل، $\gamma_M$ و $\gamma_A$ و $\gamma_D$ و $\gamma_S$ هي التأخير الإجمالي لخط الأنابيب لكل خط أنابيب متوسط على إجمالي عدد المخاطر لكل خط أنابيب. من [19]، $\gamma = \frac{1}{N_H}\sum^{N_H} \beta_h$ حيث $\beta_h$ هو جزء من التأخير الإجمالي لخط الأنابيب الذي يواجهه كل خطر معين.

بشكل عام، في غياب توصيف حمل العمل، يمكننا تغيير معاملات مختلفة مثل $\gamma$ و $N_I$ و $N_H$ و $p$ في المعادلة 2 والتعليق على تأثير المعاملات المختلفة على الوقت $T$.

**الشكل 2: TPI لأحجام مختلفة من حمل العمل لـ 2 و 4 و 6 و 8 (مع الحفاظ على $\frac{N_H}{N_I}$ = 0.1 و 0.01 و 0.001)**

في الشكل 2، يمكن ملاحظة أنه لعدد ثابت من مراحل خط الأنابيب $p$، مع زيادة حجم المشكلة، يتشبع TPI. على سبيل المثال، $p = 2$ و $\frac{N_H}{N_I}$ = 0.1 و 0.01 و 0.001 ثم يتشبع TPI عند عدد التعليمات $10 \times 10^5$ في حمل العمل. هذا يرجع بشكل أساسي إلى أن خطوط الأنابيب الأصغر تتطلب عدداً كبيراً من التعليمات للتشبع والاقتراب من الحد الأدنى لـ TPI. يمكن أيضاً ملاحظة في الشكل 2 أن خطوط الأنابيب الأكبر نسبياً (لـ $p = 4, 6$، و 8) تزيد TPI المحققة تدريجياً. هذا يرجع بشكل أساسي إلى زيادة تردد التشغيل لمراحل خط الأنابيب.

يُظهر تأثير تغيير عمق خط الأنابيب على TPI لحمل عمل معين مع مخاطر متفاوتة في الشكل 3. يمكن ملاحظة في الشكل 3 أنه مع زيادة عمق خط الأنابيب، ينخفض TPI ويتم تحقيق الأمثل. بعد الأمثل، يُلاحظ زيادة خطية في TPI. يمكن أيضاً ملاحظة أن المنحنى النظري المقدم في 3 مسطح إلى حد ما حول الأمثل مما يترك مجالاً كبيراً لاختيار أفضل نقطة تصميم لعمق خط الأنابيب الأمثل.

**الشكل 3: TPI لمراحل خط أنابيب مختلفة $p$ وحمل عمل متفاوت (مع الحفاظ على $\frac{N_H}{N_I}$ = 0.1 و 0.01 و 0.001 و 0.2 و 0.4 و 0.6 و 0.8)**

يُظهر تأثير تغيير $\gamma$ ومراحل خط الأنابيب $p$ على TPI في الشكل 4. يمكن ملاحظة في الشكل 4 أنه لقيم أصغر من $\gamma$، الأمثل المحقق في المنحنى النظري حوالي 4 ومع زيادة قيمة $\gamma$، يصبح خط أنابيب أعمق هو خط الأنابيب الأمثل. من الأشكال 2 و 3 و 4، يمكننا عمل الملاحظات التالية:

**الشكل 4: TPI لمراحل خط أنابيب مختلفة $p$ و $\gamma$ = 0.1 و 0.2 و 0.4 و 0.6 و 0.8**

**ملاحظة 1:** سيتشبع خط الأنابيب مع زيادة حجم حمل العمل. كلما زادت نسبة $\frac{N_H}{N_I}$، كان TPI المحقق أسوأ لأحمال العمل الصغيرة.

**ملاحظة 2:** كلما زادت نسبة $\frac{N_H}{N_I}$، كان عمق خط الأنابيب الأمثل أقل لحمل العمل. من الأفضل أن يكون لديك عدد أقل من مراحل خط الأنابيب إذا كان حمل العمل يحتوي على عدد كبير من المخاطر. بالنسبة لعدد كبير من المخاطر، إذا كانت مراحل خط الأنابيب أعلى من مراحل خط الأنابيب الأمثل، فإن TPI المحقق يتدهور بشكل كبير كما هو موضح بالخط الأحمر (لـ $\frac{N_H}{N_I}$ = 0.8) في الشكل 3

**ملاحظة 3:** المعامل $\gamma$ الذي يعتمد فقط على إجمالي عدد المخاطر $N_H$ و $\beta_h$ وهو جزء من التأخير الإجمالي لخط الأنابيب الذي يواجهه كل خطر معين يلعب دوراً مهماً في تحديد عمق خط الأنابيب الأمثل. بالنسبة لقيمة كبيرة من $\gamma$، إذا كانت مراحل خط الأنابيب أكثر من 20 وزادت بشكل أكبر، يتدهور TPI بشكل كبير كما هو موضح بالخط الأزرق في الشكل 4. بالنسبة لقيمة صغيرة من $\gamma$، حتى لو زاد عدد مراحل خط الأنابيب بعد العدد الأمثل، فإن الزيادة الملاحظة في TPI تكون ضئيلة

بناءً على الملاحظات من المنحنيات النظرية في الأشكال 2 و 3 و 4، يمكننا أن نثبت أنه من المهم توصيف أحمال العمل لمجال الاهتمام للوصول إلى عمق خط أنابيب أمثل للعمليات المختلفة التي تُواجه في الحسابات المتعلقة بالمجال.

---

### Translation Notes

- **Figures referenced:** Figure 1 (Pipeline Model), Figure 2 (TPI for Different Workload Sizes), Figure 3 (TPI for Different Pipeline Stages), Figure 4 (TPI for Different $\gamma$ values)
- **Key terms introduced:** TPI (Time per Instruction), busy time, non-busy time, latch overhead, pipeline hazards, pipeline stages
- **Equations:** 7 equations (equations 1-7)
- **Citations:** [9], [10], [19] referenced
- **Special handling:** All mathematical equations preserved in LaTeX; Three remarks (Remark 1, 2, 3) translated; Figure descriptions maintained

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.87
- Readability: 0.84
- Glossary consistency: 0.83
- **Overall section score:** 0.85
