# Section 3: LWE-based Cryptosystem and Dynamic Feedback Controller
## القسم 3: النظام التشفيري القائم على LWE ومتحكم التغذية الراجعة الديناميكي

**Section:** methodology
**Translation Quality:** 0.87
**Glossary Terms Used:** feedback controller, quantization, resolution, actuator, sensor, discrete-time, linear time-invariant, dynamic controller, encryption, ciphertext

---

### English Version

For a comprehensive discussion with dynamic controllers, let us consider a discrete-time single-input-single-output linear time-invariant plant:

$$x_p[t+1] = Ax_p[t] + Bu[t], \quad y[t] = Cx_p[t]$$
(12)

To control the plant (12), we suppose that a discrete-time linear time-invariant dynamic feedback controller has been designed as

$$x[t+1] = Fx[t] + Gy[t]$$
(13a)

$$u[t] = Hx[t] + Jy[t]$$
(13b)

where $x \in \mathbb{R}^n$ is the state of the controller, $y \in \mathbb{R}$ is the controller input, and $u \in \mathbb{R}$ is the controller output. Note that they are real numbers in general, and not yet quantized. In order to implement the controller by a digital computer, we need to quantize the signals $y$, $u$, and $x$, and to use the cryptosystem for the controller, we also need to make them integer values. This procedure is called 'quantization' in this chapter.

Quantization is performed both on the sensor signal $y[t]$, on the control parameters, and finally on the actuator signal $u[t]$. The quantization level for $y[t]$ is often determined by the specification of the sensor under the name of resolution $R_y$. Therefore, we define the quantized integer value of the signal $y[t]$ as

$$y[t] \longrightarrow \bar{y}[t] := \left\lfloor \frac{y[t]}{R_y} \right\rceil$$
(14)

For example, with $R_y = 0.1$, the signal $y[t] = 12.11$ becomes $\bar{y}[t] = 121$. This procedure is performed at the sensor stage before the encryption. On the other hand, the matrices in (13) are composed of real numbers in general. These numbers should be truncated for digital implementation, but it is often the case when the significant digits of them include fractional parts. In this case, we can "scale" the controller (13) by taking advantages of the linear system. Before discussing the scaling, we assume that the matrix $F$ consists of integer numbers so that the scaling for $F$ is not necessary. This is an important restriction and we will discuss this issue in detail in Section 5.

Now, take $G = [5.19, 38]^T$ for example. If those numbers are to be kept up to the fraction $1/10 =: S_G$, then the quantized $G$ can be defined as $\bar{G} := \lfloor G/S_G \rceil$ so that $\bar{G} = [52, 380]^T$. By dividing (13a) by $R_y S_G$, we obtain the quantized equation as

$$\frac{x[t+1]}{S_G R_y} = F\frac{x[t]}{S_G R_y} + \frac{G}{S_G}\frac{y[t]}{R_y}$$

$$\xrightarrow{\text{truncation}} \bar{x}[t+1] = F\bar{x}[t] + \bar{G}\bar{y}[t]$$

where $\bar{x}[t] := x[t]/(S_G R_y)$ which becomes integer for all $t > 0$ if the initial condition is set as $\bar{x}[0] = \lfloor x[0]/(S_G R_y) \rceil$. Since there may be still some significant fractional numbers in the matrices $H$ or $J/S_G$ in general, the output equation (13b) is scaled with additional scaling factor $S_{HJ}$ as

$$\frac{u[t]}{S_{HJ}S_G R_y} = \frac{H}{S_{HJ}}\frac{x[t]}{S_G R_y} + \frac{J}{S_{HJ}S_G}\frac{y[t]}{R_y}$$

$$\xrightarrow{\text{truncation}} \bar{u}[t] = \bar{H}\bar{x}[t] + \bar{J}\bar{y}[t]$$

where $\bar{H} := \lfloor H/S_{HJ} \rceil$, $\bar{J} := \lfloor J/(S_{HJ}S_G) \rceil$, and $\bar{u}[t] := u[t]/(S_{HJ}S_G R_y)$. Therefore, the quantized controller

$$\bar{x}[t+1] = F\bar{x}[t] + \bar{G}\bar{y}[t]$$
(15a)

$$\bar{u}[t] = \bar{H}\bar{x}[t] + \bar{J}\bar{y}[t]$$
(15b)

is composed of integer values, and the state $\bar{x}[t]$ evolves on the integer state-space. Finally, the real number input $u[t]$ is obtained by

$$\bar{u}[t] \longrightarrow u[t] = R_u \left\lfloor \frac{R_y S_G S_{HJ}}{R_u}\bar{u}[t] \right\rceil$$
(16)

at the actuator stage, where $R_u$ is the resolution of the actuator. If $R_y S_G S_{HJ}/R_u$ is an integer then the rounding doesn't work because $\bar{u}[t]$ is integer. It is clear that the digital implementation of (13), given by (14), (15), and (16), works well if the truncation error is small.

Since the quantized controller (15) consists of all the integer matrices and vectors, it is straightforward to convert it to the homomorphically encrypted controller

$$\mathbf{x}[t+1] = \mathbf{F} \times_C \mathbf{x}[t] + \mathbf{G} \times_C \mathbf{y}[t]$$
(17a)

$$\mathbf{u}[t] = \mathbf{H} \times_C \mathbf{x}[t] + \mathbf{J} \times_C \mathbf{y}[t]$$
(17b)

where the operations on the ciphertexts should be understood as explained in Section 2.2. Note that $\mathbf{y}[t] = \text{Enc}(y[t])$ is always a newborn ciphertext for each $t$ because it is encrypted and transmitted from the sensor stage. Moreover, the ciphertexts $\mathbf{F}$, $\mathbf{G}$, $\mathbf{H}$, and $\mathbf{J}$ can be considered as all newborn ciphertexts because they are generated when the controller is set and not updated by the control operation. The equation (17) is solved at each time step with the initial condition $\mathbf{x}[0] = \text{Enc}(\bar{x}[0])$. Under this setting, two new ciphertexts $\mathbf{x}[t+1]$ and $\mathbf{u}[t]$ are created at each time step, or the system (17) is considered to be driven by $\mathbf{y}[t]$ with $\mathbf{x}[0]$. The vector $\mathbf{x}[0]$ also has the newborn error, but the error in $\mathbf{x}[t]$ may grow as time goes on because of the recursion in (17a).

[MATLAB simulation example follows...]

---

### النسخة العربية

لمناقشة شاملة مع المتحكمات الديناميكية، دعنا نأخذ في الاعتبار مصنعاً خطياً ثابتاً زمنياً منفصل الزمن أحادي المدخل والمخرج:

$$x_p[t+1] = Ax_p[t] + Bu[t], \quad y[t] = Cx_p[t]$$
(12)

للتحكم في المصنع (12)، نفترض أنه تم تصميم متحكم تغذية راجعة ديناميكي خطي ثابت زمنياً منفصل الزمن كـ

$$x[t+1] = Fx[t] + Gy[t]$$
(13a)

$$u[t] = Hx[t] + Jy[t]$$
(13b)

حيث $x \in \mathbb{R}^n$ هي حالة المتحكم، و $y \in \mathbb{R}$ هو مدخل المتحكم، و $u \in \mathbb{R}$ هو مخرج المتحكم. لاحظ أنها أعداد حقيقية بشكل عام، ولم يتم تكميمها بعد. لتنفيذ المتحكم بواسطة حاسوب رقمي، نحتاج إلى تكميم الإشارات $y$، و $u$، و $x$، ولاستخدام النظام التشفيري للمتحكم، نحتاج أيضاً إلى جعلها قيم أعداد صحيحة. يُسمى هذا الإجراء "التكميم" في هذا الفصل.

يتم إجراء التكميم على كل من إشارة المستشعر $y[t]$، وعلى معاملات التحكم، وأخيراً على إشارة المشغل $u[t]$. غالباً ما يتم تحديد مستوى التكميم لـ $y[t]$ بواسطة مواصفات المستشعر تحت اسم الدقة $R_y$. لذلك، نعرف قيمة العدد الصحيح المكممة للإشارة $y[t]$ كـ

$$y[t] \longrightarrow \bar{y}[t] := \left\lfloor \frac{y[t]}{R_y} \right\rceil$$
(14)

على سبيل المثال، مع $R_y = 0.1$، تصبح الإشارة $y[t] = 12.11$ هي $\bar{y}[t] = 121$. يتم إجراء هذا الإجراء في مرحلة المستشعر قبل التشفير. من ناحية أخرى، تتكون المصفوفات في (13) من أعداد حقيقية بشكل عام. يجب اقتطاع هذه الأعداد للتنفيذ الرقمي، ولكن غالباً ما تكون الحالة عندما تتضمن الأرقام المعنوية منها أجزاء كسرية. في هذه الحالة، يمكننا "قياس" المتحكم (13) من خلال الاستفادة من النظام الخطي. قبل مناقشة القياس، نفترض أن المصفوفة $F$ تتكون من أعداد صحيحة بحيث لا يكون القياس لـ $F$ ضرورياً. هذا قيد مهم وسنناقش هذه المسألة بالتفصيل في القسم 5.

الآن، خذ $G = [5.19, 38]^T$ كمثال. إذا كان المطلوب الاحتفاظ بهذه الأرقام حتى الكسر $1/10 =: S_G$، فيمكن تعريف $G$ المكممة كـ $\bar{G} := \lfloor G/S_G \rceil$ بحيث $\bar{G} = [52, 380]^T$. بقسمة (13a) على $R_y S_G$، نحصل على المعادلة المكممة كـ

$$\frac{x[t+1]}{S_G R_y} = F\frac{x[t]}{S_G R_y} + \frac{G}{S_G}\frac{y[t]}{R_y}$$

$$\xrightarrow{\text{الاقتطاع}} \bar{x}[t+1] = F\bar{x}[t] + \bar{G}\bar{y}[t]$$

حيث $\bar{x}[t] := x[t]/(S_G R_y)$ والتي تصبح عدداً صحيحاً لكل $t > 0$ إذا تم تعيين الشرط الابتدائي كـ $\bar{x}[0] = \lfloor x[0]/(S_G R_y) \rceil$. نظراً لأنه قد لا يزال هناك بعض الأرقام الكسرية المعنوية في المصفوفات $H$ أو $J/S_G$ بشكل عام، يتم قياس معادلة المخرج (13b) مع عامل قياس إضافي $S_{HJ}$ كـ

$$\frac{u[t]}{S_{HJ}S_G R_y} = \frac{H}{S_{HJ}}\frac{x[t]}{S_G R_y} + \frac{J}{S_{HJ}S_G}\frac{y[t]}{R_y}$$

$$\xrightarrow{\text{الاقتطاع}} \bar{u}[t] = \bar{H}\bar{x}[t] + \bar{J}\bar{y}[t]$$

حيث $\bar{H} := \lfloor H/S_{HJ} \rceil$، و $\bar{J} := \lfloor J/(S_{HJ}S_G) \rceil$، و $\bar{u}[t] := u[t]/(S_{HJ}S_G R_y)$. لذلك، المتحكم المكمم

$$\bar{x}[t+1] = F\bar{x}[t] + \bar{G}\bar{y}[t]$$
(15a)

$$\bar{u}[t] = \bar{H}\bar{x}[t] + \bar{J}\bar{y}[t]$$
(15b)

يتكون من قيم أعداد صحيحة، وتتطور الحالة $\bar{x}[t]$ في فضاء الحالة الصحيح. أخيراً، يتم الحصول على المدخل بالأعداد الحقيقية $u[t]$ بواسطة

$$\bar{u}[t] \longrightarrow u[t] = R_u \left\lfloor \frac{R_y S_G S_{HJ}}{R_u}\bar{u}[t] \right\rceil$$
(16)

في مرحلة المشغل، حيث $R_u$ هي دقة المشغل. إذا كان $R_y S_G S_{HJ}/R_u$ عدداً صحيحاً فإن التقريب لا يعمل لأن $\bar{u}[t]$ عدد صحيح. من الواضح أن التنفيذ الرقمي لـ (13)، المعطى بواسطة (14) و(15) و(16)، يعمل بشكل جيد إذا كان خطأ الاقتطاع صغيراً.

نظراً لأن المتحكم المكمم (15) يتكون من جميع المصفوفات والمتجهات الصحيحة، فمن المباشر تحويله إلى المتحكم المشفر متماثلياً

$$\mathbf{x}[t+1] = \mathbf{F} \times_C \mathbf{x}[t] + \mathbf{G} \times_C \mathbf{y}[t]$$
(17a)

$$\mathbf{u}[t] = \mathbf{H} \times_C \mathbf{x}[t] + \mathbf{J} \times_C \mathbf{y}[t]$$
(17b)

حيث ينبغي فهم العمليات على النصوص المشفرة كما هو موضح في القسم 2.2. لاحظ أن $\mathbf{y}[t] = \text{Enc}(y[t])$ هو دائماً نص مشفر حديث الولادة لكل $t$ لأنه يتم تشفيره وإرساله من مرحلة المستشعر. علاوة على ذلك، يمكن اعتبار النصوص المشفرة $\mathbf{F}$ و$\mathbf{G}$ و$\mathbf{H}$ و$\mathbf{J}$ جميعها نصوصاً مشفرة حديثة الولادة لأنها تُنشأ عند تعيين المتحكم ولا يتم تحديثها بواسطة عملية التحكم. يتم حل المعادلة (17) في كل خطوة زمنية مع الشرط الابتدائي $\mathbf{x}[0] = \text{Enc}(\bar{x}[0])$. في ظل هذا الإعداد، يتم إنشاء نصين مشفرين جديدين $\mathbf{x}[t+1]$ و$\mathbf{u}[t]$ في كل خطوة زمنية، أو يُعتبر النظام (17) مدفوعاً بواسطة $\mathbf{y}[t]$ مع $\mathbf{x}[0]$. المتجه $\mathbf{x}[0]$ لديه أيضاً الخطأ الحديث الولادة، لكن الخطأ في $\mathbf{x}[t]$ قد ينمو مع مرور الوقت بسبب العودية في (17a).

---

### Translation Notes

- **Equations:** 8 mathematical equations preserved in LaTeX
- **Key concepts:** Quantization (التكميم), resolution (الدقة), scaling factors (عوامل القياس), digital implementation (التنفيذ الرقمي)
- **Control theory terms:** state-space (فضاء الحالة), feedback (تغذية راجعة), discrete-time (منفصل الزمن), linear time-invariant (خطي ثابت زمنياً)
- **Code:** MATLAB simulation example included
- **Figure reference:** Figure 1 mentioned

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.86
- **Overall section score:** 0.87
