# Section 11: Shannon's Noisy Channel Coding Theorem
## القسم 11: نظرية الترميز للقناة المشوشة لشانون

**Section:** noisy-channel-theorem
**Translation Quality:** 0.88
**Glossary Terms Used:** channel capacity, error-correcting codes, mutual information, equivocation

---

### English Version

All practical communication channels are noisy. To take a trivial example, the voice signal coming out of a telephone is not a perfect copy of the speaker's voice signal, because various electrical components introduce spurious bits of noise into the telephone system.

As we have seen, the effects of noise can be reduced by using error correcting codes. These codes reduce errors, but they also reduce the rate at which information is communicated. More generally, any method which reduces the effects of noise also reduces the rate at which information can be communicated. Taking this line of reasoning to its logical conclusion seems to imply that the only way to communicate information with zero error is to reduce the effective rate of information transmission to zero, and in Shannon's day this was widely believed to be true. But Shannon proved that information can be communicated, with vanishingly small error, at a rate which is limited only by the channel capacity.

Now we give Shannon's fundamental theorem for a discrete channel with noise, also known as the second fundamental coding theorem, and as Shannon's noisy channel coding theorem[2]:

> Let a discrete channel have the capacity $C$ and a discrete source the entropy per second $H$. If $H \leq C$ there exists a coding system such that the output of the source can be transmitted over the channel with an arbitrarily small frequency of errors (or an arbitrarily small equivocation). If $H \geq C$ it is possible to encode the source so that the equivocation is less than $H - C + \epsilon$ where $\epsilon$ is arbitrarily small. There is no method of encoding which gives an equivocation less than $H - C$.

(The word 'equivocation' means the average uncertainty that remains regarding the value of the input after the output is observed, i.e. the conditional entropy $H(X|Y)$). In essence, Shannon's theorem states that it is possible to use a communication channel to communicate information with a low error rate $\epsilon$ (epsilon), at a rate arbitrarily close to the channel capacity of $C$ bits/s, but it is not possible to communicate information at a rate greater than $C$ bits/s.

The capacity of a noisy channel is defined as

$$C = \max_{p(x)} I(x, y)$$ (17)
$$= \max_{p(x)} [H(y) - H(y|x)] \text{ bits.}$$ (18)

If there is no noise (i.e. if $H(y|x) = 0$) then this reduces to Equation 10, which is the capacity of a noiseless channel. The data processing inequality states that, no matter how sophisticated any device is, the amount of information $I(x, y)$ in its output about its input cannot be greater than the amount of information $H(x)$ in the input.

---

### النسخة العربية

جميع قنوات الاتصال العملية مشوشة. لنأخذ مثالاً بسيطاً، إشارة الصوت الخارجة من الهاتف ليست نسخة مثالية من إشارة صوت المتحدث، لأن مكونات كهربائية مختلفة تُدخل بتات زائفة من الضوضاء إلى نظام الهاتف.

كما رأينا، يمكن تقليل آثار الضوضاء باستخدام شفرات تصحيح الأخطاء. تقلل هذه الشفرات من الأخطاء، لكنها تقلل أيضاً من المعدل الذي تُنقل به المعلومات. بشكل أكثر عمومية، أي طريقة تقلل من آثار الضوضاء تقلل أيضاً من المعدل الذي يمكن به نقل المعلومات. إن أخذ هذا الخط من التفكير إلى استنتاجه المنطقي يبدو أنه يعني أن الطريقة الوحيدة لنقل المعلومات بدون خطأ هي تقليل المعدل الفعلي لنقل المعلومات إلى الصفر، وفي أيام شانون كان يُعتقد على نطاق واسع أن هذا صحيح. ولكن شانون أثبت أن المعلومات يمكن نقلها، مع خطأ صغير يتلاشى، بمعدل محدود فقط بسعة القناة.

الآن نعطي النظرية الأساسية لشانون لقناة منفصلة مع ضوضاء، المعروفة أيضاً باسم نظرية الترميز الأساسية الثانية، وباسم نظرية الترميز للقناة المشوشة لشانون[2]:

> لتكن لقناة منفصلة السعة $C$ وللمصدر المنفصل الإنتروبيا في الثانية $H$. إذا كان $H \leq C$ يوجد نظام ترميز بحيث يمكن نقل خرج المصدر عبر القناة بتكرار صغير بشكل تعسفي للأخطاء (أو التباس صغير بشكل تعسفي). إذا كان $H \geq C$ فمن الممكن ترميز المصدر بحيث يكون الالتباس أقل من $H - C + \epsilon$ حيث $\epsilon$ صغير بشكل تعسفي. لا توجد طريقة ترميز تعطي التباساً أقل من $H - C$.

(تعني كلمة "التباس" متوسط عدم اليقين المتبقي فيما يتعلق بقيمة الدخل بعد ملاحظة الخرج، أي الإنتروبيا الشرطية $H(X|Y)$). في جوهرها، تنص نظرية شانون على أنه من الممكن استخدام قناة اتصال لنقل المعلومات بمعدل خطأ منخفض $\epsilon$ (إبسيلون)، بمعدل قريب بشكل تعسفي من سعة القناة $C$ بتات/ث، ولكن ليس من الممكن نقل المعلومات بمعدل أكبر من $C$ بتات/ث.

يتم تعريف سعة قناة مشوشة على النحو التالي

$$C = \max_{p(x)} I(x, y)$$ (17)
$$= \max_{p(x)} [H(y) - H(y|x)] \text{ بتات.}$$ (18)

إذا لم يكن هناك ضوضاء (أي إذا كان $H(y|x) = 0$) فإن هذا يختزل إلى المعادلة 10، وهي سعة قناة خالية من الضوضاء. تنص متباينة معالجة البيانات على أنه بغض النظر عن مدى تطور أي جهاز، فإن كمية المعلومات $I(x, y)$ في خرجه حول دخله لا يمكن أن تكون أكبر من كمية المعلومات $H(x)$ في الدخل.

---

### Quality Metrics
- **Overall section score:** 0.88
