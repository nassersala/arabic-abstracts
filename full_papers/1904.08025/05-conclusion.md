# Section 5: Conclusion and Need for Integer System Matrix
## القسم 5: الخاتمة والحاجة إلى مصفوفة نظام صحيحة

**Section:** conclusion
**Translation Quality:** 0.86
**Glossary Terms Used:** homomorphic encryption, dynamic feedback controller, integer system matrix, PID controller, FIR filter, pole-zero cancellation, steady-state error

---

### English Version

In this chapter, with the use of fully homomorphic encryption, we have seen a method as well as an illustrative example to implement a dynamic feedback controller over encrypted data. Exploiting both additively and multiplicatively homomorphic properties of LWE-based scheme, all the operations in the controller are performed over encrypted parameters and signals. Once the designed controller (13) is converted to the dynamical system (15) over integer, it can be directly encrypted as (17). From the nature of fully homomorphic encryption schemes, the error injected to the encryption $\mathbf{y}[t]$ may be accumulated in the controller state $\mathbf{x}[t]$ under the recursive state update and may affect the message. However, from the control perspective, it has been seen that the effect of error is controlled and suppressed by the stability of the closed-loop system.

For the concluding remark, let us revisit that the encryption scheme for the dynamic controller (13) is based on the assumption that all entries of the system matrix $F$ are integers. To see the necessity of this assumption, let us suppose the matrix $F$ consists of non-integer real numbers. One may attempt the scaling of $F$ as $\lfloor F/S_F \rceil$ with the scaling factor $1/S_F > 1$ in order to keep the fractional part of $F$, but this scaling is hopeless because it results in recursive multiplication by $1/S_F$ for each update of the controller. Indeed, for this case, it can be checked that the state $\bar{x}[t]$ of the quantized controller (15a) is multiplied by $\lfloor F/S_F \rceil$ (instead of $F$) for each time step, so (15a) should be remodeled as the form

$$\bar{x}[t+1] = \left\lfloor \frac{F}{S_F} \right\rceil \bar{x}[t] + \left\lfloor \frac{G}{S_F^{t+1} S_G} \right\rceil \bar{y}[t]$$
(19)

with the relation $\bar{x}[t] = x[t]/(S_F^t S_G R_y)$. However, encryption of (19) is hopeless, because in this case the message of the encrypted state is unbounded due to the term $1/S_F^t$. It will lose its value when it eventually go beyond the bound $\pm p/2$ of the plaintext space $[p]$ represented as (1), unless the state is reset to eliminate the accumulated scaling factor.

This problem, which is from the constraint that encrypted variables can be multiplied by scaled real numbers only a finite number of times, is in fact one of the main difficulties of encrypting dynamic controllers having non-integer system matrix. In this respect, one may find potential benefits of using proportional-integral-derivative (PID) controllers or finite-impulse-response (FIR) filters for the design of encrypted control system, because they can be realized with the matrix $F$ being integer as follows:

• Given an FIR filter written as $C(z) = \sum_{i=0}^n b_{n-i}z^{-i}$, and the dynamic feedback controller can be realized as

$$x[t+1] = \begin{bmatrix} 0 & \cdots & 0 & 0 \\ 1 & \cdots & 0 & 0 \\ \vdots & \ddots & \vdots & \vdots \\ 0 & \cdots & 1 & 0 \end{bmatrix} x[t] + \begin{bmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{bmatrix} y[t], \quad u[t] = \begin{bmatrix} b_{n-1} & \cdots & b_1 & b_0 \end{bmatrix} x[t] + b_n y[t].$$

• A discrete PID controller in the parallel form is given by

$$C(z) = k_p + \frac{k_i T_s}{z-1} + \frac{k_d}{T_s} \frac{N_d}{N_d + \frac{T_s}{z-1}}$$

where $k_p$, $k_i$, and $k_d$ are the proportional, integral, and derivative gains, respectively, $T_s$ is the sampling time, and $N_d \in \mathbb{N}$ is the parameter for the derivative filter. This controller can be realized as

$$x[t+1] = \begin{bmatrix} 2-N_d & N_d-1 \\ 1 & 0 \end{bmatrix} x[t] + \begin{bmatrix} 1 \\ 0 \end{bmatrix} y[t], \quad u[t] = \begin{bmatrix} b_1 & b_0 \end{bmatrix} x[t] + b_2 y[t]$$

where $b_1 = k_i T_s - k_d N_d^2/T_s$, $b_0 = k_i T_s N_d - k_i T_s + k_d N_d^2/T_s$, and $b_2 = k_p + k_d N_d/T_s$.

Another idea of approximating the effect of non-integer real numbers of $F$ has been presented in [13] by using stable pole-zero cancellation. However, it was done at the cost of increased steady-state error in control performance. Further research is called for in this direction.

**Acknowledgement**

The authors are grateful to Prof. Jung Hee Cheon and Dr. Yongsoo Song, Department of Mathematical Sciences, Seoul National University, for helpful discussions. This work was supported by National Research Foundation of Korea (NRF) grant funded by the Korea government (Ministry of Science and ICT) (No. NRF-2017R1E1A1A03070342).

---

### النسخة العربية

في هذا الفصل، مع استخدام التشفير المتماثل الكامل، رأينا طريقة بالإضافة إلى مثال توضيحي لتنفيذ متحكم تغذية راجعة ديناميكي على بيانات مشفرة. باستغلال كل من الخصائص المتماثلة الجمعية والضربية للمخطط القائم على LWE، يتم إجراء جميع العمليات في المتحكم على المعاملات والإشارات المشفرة. بمجرد تحويل المتحكم المصمم (13) إلى النظام الديناميكي (15) على الأعداد الصحيحة، يمكن تشفيره مباشرة كـ (17). من طبيعة مخططات التشفير المتماثلة الكاملة، قد يتراكم الخطأ المحقون في التشفير $\mathbf{y}[t]$ في حالة المتحكم $\mathbf{x}[t]$ تحت تحديث الحالة العودي وقد يؤثر على الرسالة. ومع ذلك، من منظور التحكم، رُئي أن تأثير الخطأ يتم التحكم فيه وقمعه بواسطة استقرار النظام ذو الحلقة المغلقة.

للملاحظة الختامية، دعنا نعيد النظر في أن مخطط التشفير للمتحكم الديناميكي (13) يعتمد على افتراض أن جميع عناصر مصفوفة النظام $F$ هي أعداد صحيحة. لرؤية ضرورة هذا الافتراض، دعنا نفترض أن المصفوفة $F$ تتكون من أعداد حقيقية غير صحيحة. قد يحاول المرء قياس $F$ كـ $\lfloor F/S_F \rceil$ مع عامل القياس $1/S_F > 1$ من أجل الاحتفاظ بالجزء الكسري من $F$، ولكن هذا القياس ميؤوس منه لأنه يؤدي إلى ضرب عودي بـ $1/S_F$ لكل تحديث للمتحكم. في الواقع، لهذه الحالة، يمكن التحقق من أن الحالة $\bar{x}[t]$ للمتحكم المكمم (15a) تُضرب بـ $\lfloor F/S_F \rceil$ (بدلاً من $F$) لكل خطوة زمنية، لذا يجب إعادة نمذجة (15a) كالشكل

$$\bar{x}[t+1] = \left\lfloor \frac{F}{S_F} \right\rceil \bar{x}[t] + \left\lfloor \frac{G}{S_F^{t+1} S_G} \right\rceil \bar{y}[t]$$
(19)

مع العلاقة $\bar{x}[t] = x[t]/(S_F^t S_G R_y)$. ومع ذلك، تشفير (19) ميؤوس منه، لأن في هذه الحالة رسالة الحالة المشفرة غير محدودة بسبب المصطلح $1/S_F^t$. ستفقد قيمتها عندما تتجاوز في النهاية الحد $\pm p/2$ من فضاء النص الواضح $[p]$ الممثل كـ (1)، ما لم يتم إعادة تعيين الحالة للتخلص من عامل القياس المتراكم.

هذه المشكلة، التي تنشأ من القيد بأن المتغيرات المشفرة يمكن ضربها بأعداد حقيقية مقاسة عدداً محدوداً فقط من المرات، هي في الواقع إحدى الصعوبات الرئيسية لتشفير المتحكمات الديناميكية التي لها مصفوفة نظام غير صحيحة. في هذا الصدد، قد يجد المرء فوائد محتملة لاستخدام متحكمات تناسبية-تكاملية-تفاضلية (PID) أو مرشحات استجابة نبضية محدودة (FIR) لتصميم نظام التحكم المشفر، لأنه يمكن تحقيقها مع كون المصفوفة $F$ عدداً صحيحاً كما يلي:

• بالنظر إلى مرشح FIR مكتوب كـ $C(z) = \sum_{i=0}^n b_{n-i}z^{-i}$، يمكن تحقيق متحكم التغذية الراجعة الديناميكي كـ

$$x[t+1] = \begin{bmatrix} 0 & \cdots & 0 & 0 \\ 1 & \cdots & 0 & 0 \\ \vdots & \ddots & \vdots & \vdots \\ 0 & \cdots & 1 & 0 \end{bmatrix} x[t] + \begin{bmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{bmatrix} y[t], \quad u[t] = \begin{bmatrix} b_{n-1} & \cdots & b_1 & b_0 \end{bmatrix} x[t] + b_n y[t].$$

• يُعطى متحكم PID منفصل في الشكل الموازي بواسطة

$$C(z) = k_p + \frac{k_i T_s}{z-1} + \frac{k_d}{T_s} \frac{N_d}{N_d + \frac{T_s}{z-1}}$$

حيث $k_p$ و $k_i$ و $k_d$ هي الكسوب التناسبية والتكاملية والتفاضلية، على التوالي، و $T_s$ هو وقت العينة، و $N_d \in \mathbb{N}$ هو معامل المرشح التفاضلي. يمكن تحقيق هذا المتحكم كـ

$$x[t+1] = \begin{bmatrix} 2-N_d & N_d-1 \\ 1 & 0 \end{bmatrix} x[t] + \begin{bmatrix} 1 \\ 0 \end{bmatrix} y[t], \quad u[t] = \begin{bmatrix} b_1 & b_0 \end{bmatrix} x[t] + b_2 y[t]$$

حيث $b_1 = k_i T_s - k_d N_d^2/T_s$، و $b_0 = k_i T_s N_d - k_i T_s + k_d N_d^2/T_s$، و $b_2 = k_p + k_d N_d/T_s$.

تم تقديم فكرة أخرى لتقريب تأثير الأعداد الحقيقية غير الصحيحة لـ $F$ في [13] باستخدام إلغاء القطب-الصفر المستقر. ومع ذلك، تم ذلك على حساب زيادة خطأ الحالة المستقرة في أداء التحكم. هناك حاجة لمزيد من البحث في هذا الاتجاه.

**الشكر والتقدير**

يشعر المؤلفون بالامتنان للبروفيسور جونغ هي تشون والدكتور يونغسو سونغ، قسم العلوم الرياضية، جامعة سيول الوطنية، على المناقشات المفيدة. تم دعم هذا العمل بمنحة من مؤسسة البحوث الوطنية الكورية (NRF) الممولة من حكومة كوريا (وزارة العلوم وتكنولوجيا المعلومات والاتصالات) (رقم NRF-2017R1E1A1A03070342).

---

### Translation Notes

- **Key concepts:** Integer system matrix (مصفوفة نظام صحيحة), scaling factor accumulation (تراكم عامل القياس), PID controller (متحكم PID), FIR filter (مرشح FIR), pole-zero cancellation (إلغاء القطب-الصفر)
- **Equations:** 2 mathematical equations and 2 matrix realizations
- **Future research:** Identified limitation and potential solutions
- **Citations:** Reference [13] cited
- **Acknowledgements:** Funding information preserved

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.85
- **Overall section score:** 0.86
