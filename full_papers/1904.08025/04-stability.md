# Section 4: Controlled Error Growth by Closed-loop Stability
## القسم 4: نمو الخطأ المتحكم فيه بواسطة استقرار الحلقة المغلقة

**Section:** results/analysis
**Translation Quality:** 0.85
**Glossary Terms Used:** stability, closed-loop, error growth, bounded, asymptotically stable, disturbance, control performance

---

### English Version

As mentioned previously, the growth of the error in the ciphertext $\mathbf{x}[t]$ is of major concern in this section. We have to suppress its growth not to go unbounded.

Actually, the source of error growth is the arithmetic operations in (17). To see both the message and the error in the state $\mathbf{x}[t]$, let us decrypt the dynamics (17) with the secret key $\mathbf{s}$ except the rounding operation; i.e., we define

$$\xi[t] := \frac{(\mathbf{x}[t] \cdot \mathbf{s}) \mod q}{L} \in \mathbb{R}^n$$

so that $\text{Dec}(\mathbf{x}[t]) = \lfloor \xi[t] \rceil$, and see the evolution of $\xi$-system over real-valued signals, which in turn is equivalent to the operation of (17). According to the homomorphic property (11), the $\xi$-system is derived as

$$\xi[t+1] = F\xi[t] + \bar{G}\left(\bar{y}[t] + \frac{e_y[t]}{L}\right) + \frac{\Delta(\mathbf{F}, \mathbf{x}[t])}{L} + \frac{\Delta(\mathbf{G}, \mathbf{y}[t])}{L}$$
$$=: F\xi[t] + \bar{G}\bar{y}[t] + \Delta_1[t], \quad \xi[0] = \bar{x}[0] + \frac{e_{x}[0]}{L},$$

$$\bar{u}'[t] = \bar{H}\xi[t] + \bar{J}\left(\bar{y}[t] + \frac{e_y[t]}{L}\right) + \frac{\Delta(\mathbf{H}, \mathbf{x}[t])}{L} + \frac{\Delta(\mathbf{J}, \mathbf{y}[t])}{L}$$
$$=: \bar{H}\xi[t] + \bar{J}\bar{y}[t] + \Delta_2[t],$$
(18)

in which $e_y[t]$ and $e_{x}[0]$ are the errors injected to the encryptions $\mathbf{y}[t]$ and $\mathbf{x}[0]$, respectively, $\Delta(\mathbf{F}, \mathbf{x}[t])$, $\Delta(\mathbf{G}, \mathbf{y}[t])$, $\Delta(\mathbf{H}, \mathbf{x}[t])$, and $\Delta(\mathbf{J}, \mathbf{y}[t])$ are the errors caused by ciphertext multiplication, which are defined as the same as in (11), and $\bar{u}'[t]$ is defined as $\bar{u}'[t] := ((\mathbf{u}[t] \cdot \mathbf{s}) \mod q)/L$ so that $\text{Dec}(\mathbf{u}[t]) = \lfloor \bar{u}'[t] \rceil$.

For the comparison with the quantized controller (15), the first observation is that if there is no error injected to ciphertexts $\mathbf{y}[t]$, $\mathbf{x}[0]$, and $\{\mathbf{F}, \mathbf{G}, \mathbf{H}, \mathbf{J}\}$ so that $\Delta_1[t]$, $\Delta_2[t]$, and $e_{x}[0]$ are all zero, the operation of (18) is exactly the same way as the operation of (15). Then, with the control perspective, the signals $\Delta_1[t]$ and $\Delta_2[t]$ can be understood as external disturbances injected to the feedback loop, and the quantity $e_{x}[0]$ can be regarded as perturbation of the initial condition (see Fig. 2). Here, the sizes of $\Delta_1[t]$, $\Delta_2[t]$, and $e_{x}[0]$ can be made arbitrarily small by increasing the parameter $L$ for the encryption. This is because $\|e_y[t]/L\|_\infty$ and $\|e_{x}[0]/L\|_\infty$ are less than $r/(2L)$, and the disturbance caused by multiplication of $\{\mathbf{x}[t], \mathbf{y}[t]\}$ by $\{\mathbf{F}, \mathbf{G}, \mathbf{H}, \mathbf{J}\}$ can also be made arbitrary small with the choice of $L$; for example, as seen in (11), the size of signal $\Delta(\mathbf{F}, \mathbf{x}[t])/L$ is bounded as

$$\left\|\frac{\Delta(\mathbf{F}, \mathbf{x}[t])}{L}\right\|_\infty \leq \frac{1}{L}\sum_{j=1}^n \left\| \begin{bmatrix} D(\mathbf{x}_j[t]) \cdot \mathbf{e}_{F_{1,j}} \\ D(\mathbf{x}_j[t]) \cdot \mathbf{e}_{F_{2,j}} \\ \vdots \\ D(\mathbf{x}_j[t]) \cdot \mathbf{e}_{F_{n,j}} \end{bmatrix} \right\|_\infty \leq \frac{9nr\log q}{2L} = \frac{9nr(\log p + \log L)}{2L}.$$

Now, in terms of the error growth problem of the controller state, the difference $\xi[t] - \bar{x}[t]$ corresponds to the error of our concern. One might expect that the size of $\xi[t] - \bar{x}[t]$ can be made arbitrarily small by increasing $L$, but it is not true due to the rounding operations in the sensor and actuator; for example, if the difference $\xi[t] - \bar{x}[t]$ is so small that the difference of actuator inputs is less than the size of input resolution, it is truncated and the difference is not compensated in the closed-loop stability. As a result, the error eventually grows up to the resolution range, but is controlled not to grow more than that. Therefore, the damage of the message in the ciphertexts $\mathbf{x}[t]$ is inevitable, but it can be limited up to the last a few digits. Motivated by this fact, one may intentionally enhance the resolutions by a few more digits in order to preserve the significant figures. In this way, as long as the injected errors $\Delta_1[t]$, $\Delta_2[t]$, and $e_{x}[0]/L$ are sufficiently small, the error (i.e., the difference $\xi[t] - \bar{x}[t]$) is controlled not to grow unbounded by the closed-loop stability. See a simulation result in Fig. 3.

In the rest of this section, we analyze the control performance in terms of the encryption as well as the quantization. The detailed quantitative analysis is omitted but can be found in [12]. For this, let us recall that $\text{Dec}(\mathbf{u}[t]) = \lfloor \bar{u}' \rceil$. This leads to, by (16),

$$u = R_u \left\lfloor \frac{R_y S_G S_{HJ}}{R_u} \lfloor \bar{u}' \rceil \right\rceil = R_y S_G S_{HJ} \bar{u}' + \Delta_{\text{Dec}} + \Delta_u$$

where

$$\Delta_{\text{Dec}} := R_y S_G S_{HJ} (\lfloor \bar{u}' \rceil - \bar{u}'), \quad \Delta_u := R_u \left\lfloor \frac{R_y S_G S_{HJ}}{R_u} \lfloor \bar{u}' \rceil \right\rceil - R_y S_G S_{HJ} \lfloor \bar{u}' \rceil$$

in which, $\Delta_{\text{Dec}}$ implies the error caused by the rounding in the decryption, and $\Delta_u$ implies the error by the quantization of the input stage. Now, for the sake of simplicity, let us assume that $G = S_G\bar{G}$, $H = S_{HJ}\bar{H}$, and $J = S_{HJ}S_G\bar{J}$, which means there is no error due to the scaling of the matrices. By defining $\xi' := R_y S_G \xi$, we obtain from (18) that

$$R_y S_G S_{HJ} \bar{u}' = H\xi' + Jy + J\Delta_y + R_y S_G S_{HJ}\Delta_2 \quad \text{where } \Delta_y := R_y \left\lfloor \frac{y}{R_y} \right\rceil - y$$

in which, $\Delta_y$ is the error caused by the quantization at the sensor stage. Putting together, the closed-loop system of the plant (12) and the controller (18) is equivalently described by

$$x_p[t+1] = Ax_p[t] + B(H\xi'[t] + JCx_p[t])$$
$$+ \{B(J\Delta_y[t] + R_y S_G S_{HJ}\Delta_2[t] + \Delta_{\text{Dec}}[t] + \Delta_u[t])\}$$

$$\xi'[t+1] = F\xi'[t] + GCx_p[t] + \{G\Delta_y[t] + S_G S_{HJ}\Delta_1[t]\}$$

with the initial condition of the controller is set to be

$$\xi'[0] = x[0] + \left\{R_y S_G \left\lfloor \frac{x[0]}{R_y S_G} \right\rceil - x[0] + \frac{R_y S_G e_{x}[0]}{L}\right\}$$

where $x[0]$ is the initial condition of (13). Note that all the braced terms (i.e., errors) can be made arbitrarily small with sufficiently small $R_y$ and $R_u$ and with sufficiently large $L$. Moreover, with all these errors being zero, the above system is nothing but the closed-loop system of the plant (12) and the controller (13), which is supposed to be asymptotically stable. Therefore, it is seen that the control performance with the encrypted controller (17) can be made arbitrarily close to the nominal control performance with the linear controller (13).

---

### النسخة العربية

كما ذُكر سابقاً، نمو الخطأ في النص المشفر $\mathbf{x}[t]$ هو الشاغل الرئيسي في هذا القسم. يجب علينا قمع نموه حتى لا يصبح غير محدود.

في الواقع، مصدر نمو الخطأ هو العمليات الحسابية في (17). لرؤية كل من الرسالة والخطأ في الحالة $\mathbf{x}[t]$، دعنا نفك تشفير الديناميكيات (17) باستخدام المفتاح السري $\mathbf{s}$ باستثناء عملية التقريب؛ أي، نعرف

$$\xi[t] := \frac{(\mathbf{x}[t] \cdot \mathbf{s}) \mod q}{L} \in \mathbb{R}^n$$

بحيث $\text{Dec}(\mathbf{x}[t]) = \lfloor \xi[t] \rceil$، ونرى تطور نظام $\xi$ على الإشارات ذات القيم الحقيقية، والذي بدوره يعادل عملية (17). وفقاً للخاصية المتماثلة (11)، يُشتق نظام $\xi$ كـ

$$\xi[t+1] = F\xi[t] + \bar{G}\left(\bar{y}[t] + \frac{e_y[t]}{L}\right) + \frac{\Delta(\mathbf{F}, \mathbf{x}[t])}{L} + \frac{\Delta(\mathbf{G}, \mathbf{y}[t])}{L}$$
$$=: F\xi[t] + \bar{G}\bar{y}[t] + \Delta_1[t], \quad \xi[0] = \bar{x}[0] + \frac{e_{x}[0]}{L},$$

$$\bar{u}'[t] = \bar{H}\xi[t] + \bar{J}\left(\bar{y}[t] + \frac{e_y[t]}{L}\right) + \frac{\Delta(\mathbf{H}, \mathbf{x}[t])}{L} + \frac{\Delta(\mathbf{J}, \mathbf{y}[t])}{L}$$
$$=: \bar{H}\xi[t] + \bar{J}\bar{y}[t] + \Delta_2[t],$$
(18)

حيث $e_y[t]$ و $e_{x}[0]$ هما الأخطاء المحقونة في التشفيرات $\mathbf{y}[t]$ و $\mathbf{x}[0]$، على التوالي، و $\Delta(\mathbf{F}, \mathbf{x}[t])$ و $\Delta(\mathbf{G}, \mathbf{y}[t])$ و $\Delta(\mathbf{H}, \mathbf{x}[t])$ و $\Delta(\mathbf{J}, \mathbf{y}[t])$ هي الأخطاء الناتجة عن ضرب النص المشفر، والتي تُعرّف بنفس الطريقة كما في (11)، و $\bar{u}'[t]$ يُعرّف كـ $\bar{u}'[t] := ((\mathbf{u}[t] \cdot \mathbf{s}) \mod q)/L$ بحيث $\text{Dec}(\mathbf{u}[t]) = \lfloor \bar{u}'[t] \rceil$.

للمقارنة مع المتحكم المكمم (15)، الملاحظة الأولى هي أنه إذا لم يكن هناك خطأ محقون في النصوص المشفرة $\mathbf{y}[t]$ و $\mathbf{x}[0]$ و $\{\mathbf{F}, \mathbf{G}, \mathbf{H}, \mathbf{J}\}$ بحيث $\Delta_1[t]$ و $\Delta_2[t]$ و $e_{x}[0]$ كلها صفر، فإن عملية (18) هي بالضبط نفس الطريقة التي تعمل بها عملية (15). إذن، من منظور التحكم، يمكن فهم الإشارات $\Delta_1[t]$ و $\Delta_2[t]$ على أنها اضطرابات خارجية محقونة في حلقة التغذية الراجعة، ويمكن اعتبار الكمية $e_{x}[0]$ على أنها اضطراب الشرط الابتدائي (انظر الشكل 2). هنا، يمكن جعل أحجام $\Delta_1[t]$ و $\Delta_2[t]$ و $e_{x}[0]$ صغيرة تعسفياً بزيادة المعامل $L$ للتشفير. هذا لأن $\|e_y[t]/L\|_\infty$ و $\|e_{x}[0]/L\|_\infty$ أقل من $r/(2L)$، ويمكن أيضاً جعل الاضطراب الناتج عن ضرب $\{\mathbf{x}[t], \mathbf{y}[t]\}$ بـ $\{\mathbf{F}, \mathbf{G}, \mathbf{H}, \mathbf{J}\}$ صغيراً تعسفياً مع اختيار $L$؛ على سبيل المثال، كما هو موضح في (11)، حجم الإشارة $\Delta(\mathbf{F}, \mathbf{x}[t])/L$ محدود كـ

$$\left\|\frac{\Delta(\mathbf{F}, \mathbf{x}[t])}{L}\right\|_\infty \leq \frac{1}{L}\sum_{j=1}^n \left\| \begin{bmatrix} D(\mathbf{x}_j[t]) \cdot \mathbf{e}_{F_{1,j}} \\ D(\mathbf{x}_j[t]) \cdot \mathbf{e}_{F_{2,j}} \\ \vdots \\ D(\mathbf{x}_j[t]) \cdot \mathbf{e}_{F_{n,j}} \end{bmatrix} \right\|_\infty \leq \frac{9nr\log q}{2L} = \frac{9nr(\log p + \log L)}{2L}.$$

الآن، من حيث مشكلة نمو الخطأ لحالة المتحكم، يتوافق الفرق $\xi[t] - \bar{x}[t]$ مع الخطأ الذي يثير قلقنا. قد يتوقع المرء أن حجم $\xi[t] - \bar{x}[t]$ يمكن جعله صغيراً تعسفياً بزيادة $L$، ولكن هذا ليس صحيحاً بسبب عمليات التقريب في المستشعر والمشغل؛ على سبيل المثال، إذا كان الفرق $\xi[t] - \bar{x}[t]$ صغيراً جداً بحيث يكون الفرق في مدخلات المشغل أقل من حجم دقة المدخل، فإنه يتم اقتطاعه ولا يتم تعويض الفرق في استقرار الحلقة المغلقة. نتيجة لذلك، ينمو الخطأ في النهاية حتى نطاق الدقة، لكنه يتحكم فيه حتى لا ينمو أكثر من ذلك. لذلك، الضرر للرسالة في النصوص المشفرة $\mathbf{x}[t]$ أمر لا مفر منه، لكن يمكن تحديده حتى آخر بضعة أرقام. بدافع من هذه الحقيقة، قد يعزز المرء عمداً الدقة ببضعة أرقام إضافية من أجل الحفاظ على الأرقام المعنوية. بهذه الطريقة، طالما أن الأخطاء المحقونة $\Delta_1[t]$ و $\Delta_2[t]$ و $e_{x}[0]/L$ صغيرة بما فيه الكفاية، يتم التحكم في الخطأ (أي، الفرق $\xi[t] - \bar{x}[t]$) حتى لا ينمو بشكل غير محدود بواسطة استقرار الحلقة المغلقة. انظر نتيجة المحاكاة في الشكل 3.

في بقية هذا القسم، نحلل أداء التحكم من حيث التشفير وكذلك التكميم. تم حذف التحليل الكمي التفصيلي ولكن يمكن العثور عليه في [12]. لهذا، دعنا نتذكر أن $\text{Dec}(\mathbf{u}[t]) = \lfloor \bar{u}' \rceil$. يؤدي هذا إلى، بواسطة (16)،

$$u = R_u \left\lfloor \frac{R_y S_G S_{HJ}}{R_u} \lfloor \bar{u}' \rceil \right\rceil = R_y S_G S_{HJ} \bar{u}' + \Delta_{\text{Dec}} + \Delta_u$$

حيث

$$\Delta_{\text{Dec}} := R_y S_G S_{HJ} (\lfloor \bar{u}' \rceil - \bar{u}'), \quad \Delta_u := R_u \left\lfloor \frac{R_y S_G S_{HJ}}{R_u} \lfloor \bar{u}' \rceil \right\rceil - R_y S_G S_{HJ} \lfloor \bar{u}' \rceil$$

حيث، $\Delta_{\text{Dec}}$ يعني الخطأ الناتج عن التقريب في فك التشفير، و $\Delta_u$ يعني الخطأ الناتج عن تكميم مرحلة المدخل. الآن، من أجل البساطة، دعنا نفترض أن $G = S_G\bar{G}$ و $H = S_{HJ}\bar{H}$ و $J = S_{HJ}S_G\bar{J}$، مما يعني عدم وجود خطأ بسبب قياس المصفوفات. بتعريف $\xi' := R_y S_G \xi$، نحصل من (18) على

$$R_y S_G S_{HJ} \bar{u}' = H\xi' + Jy + J\Delta_y + R_y S_G S_{HJ}\Delta_2 \quad \text{حيث } \Delta_y := R_y \left\lfloor \frac{y}{R_y} \right\rceil - y$$

حيث، $\Delta_y$ هو الخطأ الناتج عن التكميم في مرحلة المستشعر. بتجميعها معاً، يوصف النظام ذو الحلقة المغلقة للمصنع (12) والمتحكم (18) بشكل مكافئ بـ

$$x_p[t+1] = Ax_p[t] + B(H\xi'[t] + JCx_p[t])$$
$$+ \{B(J\Delta_y[t] + R_y S_G S_{HJ}\Delta_2[t] + \Delta_{\text{Dec}}[t] + \Delta_u[t])\}$$

$$\xi'[t+1] = F\xi'[t] + GCx_p[t] + \{G\Delta_y[t] + S_G S_{HJ}\Delta_1[t]\}$$

مع تعيين الشرط الابتدائي للمتحكم ليكون

$$\xi'[0] = x[0] + \left\{R_y S_G \left\lfloor \frac{x[0]}{R_y S_G} \right\rceil - x[0] + \frac{R_y S_G e_{x}[0]}{L}\right\}$$

حيث $x[0]$ هو الشرط الابتدائي لـ (13). لاحظ أن جميع المصطلحات بين الأقواس (أي، الأخطاء) يمكن جعلها صغيرة تعسفياً مع $R_y$ و $R_u$ صغيرة بما فيه الكفاية ومع $L$ كبير بما فيه الكفاية. علاوة على ذلك، مع كون جميع هذه الأخطاء صفراً، النظام أعلاه ليس سوى النظام ذو الحلقة المغلقة للمصنع (12) والمتحكم (13)، والذي من المفترض أن يكون مستقراً تقاربياً. لذلك، يُرى أن أداء التحكم مع المتحكم المشفر (17) يمكن جعله قريباً تعسفياً من أداء التحكم الاسمي مع المتحكم الخطي (13).

---

### Translation Notes

- **Figures referenced:** Figure 2 (closed-loop system diagram), Figure 3 (error simulation)
- **Key concepts:** Closed-loop stability (استقرار الحلقة المغلقة), error bounds (حدود الخطأ), disturbance rejection (رفض الاضطراب), asymptotic stability (استقرار تقاربي)
- **Mathematical analysis:** Detailed stability analysis with quantization and encryption errors
- **Citations:** Reference [12] cited
- **Special handling:** Complex matrix/vector equations preserved

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.85
- Readability: 0.84
- Glossary consistency: 0.84
- **Overall section score:** 0.85
