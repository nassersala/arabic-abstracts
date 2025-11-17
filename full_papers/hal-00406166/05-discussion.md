# Section 4: Discussion
## القسم 4: المناقشة

**Section:** discussion
**Translation Quality:** 0.87
**Glossary Terms Used:** implementation, hash function, register, correction, collision, Gaussian distribution, Central Limit Theorem, optimality, complexity

---

### English Version

We offer here final reflections concerning an implementation of the HYPERLOGLOG algorithm (Figures 3, 4, and 5) as well as some surrounding complexity considerations.

## The HYPERLOGLOG program

A program meant to cope with most practical usage conditions is described in Figure 3. In comparison to the algorithm of Figure 2, one modification regarding initialization and two final corrections to the estimates are introduced.

**(i) Initialization of registers.** In the algorithm of Figure 2, registers are initialized at -∞. This has the advantage of leading to expressions of the average-case that are comparatively simple: see Equations (4) and (5). However, a consequence is that the estimate E returned by the algorithm assumes the value 0 as soon as one of the registers has been left untouched, that is, as soon as one of the m substreams is empty. Given known fact regarding the coupon collector problem, this means that we should expect E = 0 when n ≪ m log m, so that the algorithm errs badly for small cardinalities.

In the program of Figure 3, we have changed the initialization of registers to 0. The conclusions of Theorem 1, regarding the asymptotically unbiased character of the estimate, are still applicable to the program, since all substreams are nonempty with an overwhelming probability, as soon as n ≫ m log m. The advantage of the modification is that we can now get usable estimates even when n is a small multiple of m (this fact can be furthermore confirmed by Poisson approximations). The estimates provided by the program for very small values of n (say, n ≈ a constant or n ≈ m) can then be effectively corrected, as we explain next.

**(ii) Small range corrections.** For the HYPERLOGLOG program (including the modification of (i) above, regarding register initialization), extensive simulations demonstrate that the asymptotic regime is practically attained (without essentially affecting the nominal error of 1.04/√m and without detectable bias) at the cardinality value n = 5m/2, when m ≥ 16. In contrast, for n < 5m/2, nonlinear distortions start appearing—on the extreme side, the raw algorithm with registers initialized to 0 will invariably return the estimate α_m m ≈ 0.7m when n = 0 (!). Thus, corrections must be brought to the estimate, when E (i.e., n) is comparatively small with respect to m.

The solution comes from probabilistic properties of random allocations, as already exploited by the HITCOUNTING algorithm of Whang et al. [24], whose analysis is discussed in [9, Sec. 4.3]. Say n balls are thrown at random into m bins. Then, as it is well-known, the number of empty bins is about me^{-ρ}, where ρ := n/m. Thus, upon observing V empty bins amongst a total of m, one may legitimately expect ρ to be close to log(m/V), that is, n must be close to m log(m/V). (The quality of this estimate can be precisely analysed, since exact and asymptotic forms are known for the mean, variance, and distribution of V; see, e.g., [21].) Here the bins are the ones associated to the m "submultisets", and one knows that a bin j is empty from the fact that its corresponding register M[j] has preserved its initial value 0. This correction is incorporated in the program of Figure 3.

**(iii) Large range corrections.** For cardinalities in the range 1::N, with N of the order of 10^9, hashing over at least L = 32 bits should be used (2^32 ≈ 4 × 10^9). However, when the cardinality n approaches (or perhaps even exceeds) 2^L, then hashing collisions become more and more likely. For a randomly chosen hash function, this effect can be modelled by a balls and bins model of the type described in the previous paragraph, with now 2^L replacing m. In other words, the quantity E of HYPERLOGLOG estimates the number of different hashed values, which is with high probability, about 2^L(1 - e^{-ρ}), where ρ = n/2^L. The inversion of that relation then gives us the approximate equation n ≈ -2^L log(1 - E/2^L), which is the one used in the program.

Regarding registers, their values a priori range in the interval 0::L+1-log₂ m. With hashed values of 32 bits, this means that 5 bits ("short bytes") are sufficient to store registers (of course, standard 8-bit bytes can also be used in some implementations). Regarding the quality of results returned, we expect the values of the estimate returned to be approximately Gaussian, due to an averaging effect and the Central Limit Theorem: this property is indeed well supported by the simulations of Figure 4 (bottom). Accordingly:

**Let σ = 1.04/√m represent the standard error; the estimates provided by HYPERLOGLOG are expected to be within σ, 2σ, 3σ of the exact count in respectively 65%, 95%, 99% of all the cases.**

In practice, the HYPERLOGLOG program is quite efficient: like the standard LOGLOG of [10] or MINCOUNT of [16], its running time is dominated by the computation of the hash function, so that it is only three to four times slower than a plain scan of the data (e.g., by the Unix command "wc -l", which merely counts end-of-lines).

## Optimality considerations

The near-optimality expressed by our title results from the combination of two facts.

**(i)** Clearly, maintaining ε-approximate counts till a range of N necessitates Ω(log log N) bits. Indeed, the cardinalities should be located in an exponential scale,

$$1, (1+ε), (1+ε)^2, ..., (1+ε)^L = N,$$

which comprises log_{(1+ε)} N intervals, necessitating at least log₂ log_{(1+ε)} N bits of information to be represented.

**(ii)** For a wide class of algorithms based on order statistics, Chassaing and Gérin [6] have shown that the best achievable accuracy is bounded from below by a quantity close to 1/√m. Our algorithm, which can be viewed as maintaining approximate order statistics, is, on the basis of this result only about 4% off the information-theoretic optimum of the Chassaing-Gérin class, while using memory units that are typically 3 to 5 times shorter.

As a final summary, the algorithm proves to be easy to code and efficient, being even nearly optimal under certain criteria. On "real-life" data, it appears to be in excellent agreement with the theoretical analysis, a fact recently verified by extensive tests (see Figure 5 for a sample) conducted by Pranav Kashyap, whose contribution is here gratefully acknowledged. The program can be applied to very diverse collections of data (only a "good" hash function is needed), and, once duly equipped with corrections, it can smoothly cope with a wide range of cardinalities—from very small to very large. In addition, it parallelizes or distributes optimally and can be adapted to the "sliding window" usage [7].

All in all, HYPERLOGLOG is highly practical, versatile, and it conforms well to what analysis predicts.

---

**Program HYPERLOGLOG** (input M: multiset of items from domain D)

Let h: D → {0,1}^32 hash data from D to binary 32-bit words.
Let ρ(s) be the position of the leftmost 1-bit of s: e.g., ρ(1···) = 1; ρ(0001···) = 4; ρ(0^K···) = K+1.
Define α₁₆ = 0.673; α₃₂ = 0.697; α₆₄ = 0.709; α_m = 0.7213/(1+1.079/m) for m ≥ 128.

```
assume m = 2^b with b ∈ [4::16].
initialize a collection of m registers, M[1], ..., M[m], to 0;
for v ∈ M do
    set x := h(v);
    set j = 1 + ⟨x₁x₂...x_b⟩₂;  {the binary address determined by the first b bits of x}
    set w := x_{b+1}x_{b+2}...;
    set M[j] := max(M[j], ρ(w));
compute E := α_m m² (∑_{j=1}^m 2^{-M[j]})^{-1};  {the "raw" HyperLogLog estimate}
if E ≤ 5m/2 then
    let V be the number of registers equal to 0;
    if V ≠ 0 then set E* := m log(m/V) else set E* := E;  {small range correction}
if E ∈ ]5m/2, 1/30 × 2^32] then
    set E* := E;  {intermediate range—no correction}
if E > 1/30 × 2^32 then
    set E* := -2^32 log(1 - E/2^32);  {large range correction}
return cardinality estimate E* with typical relative error 1.04/√m.
```

**Figure 3:** The HYPERLOGLOG Program dimensioned for maximal cardinalities in the range [0::10^9] and for common "practical" values m = 2^4, ..., 2^16.

---

### النسخة العربية

نقدم هنا تأملات نهائية بخصوص تنفيذ خوارزمية HYPERLOGLOG (الأشكال 3، 4، و 5) بالإضافة إلى بعض الاعتبارات المتعلقة بالتعقيد المحيط.

## برنامج HYPERLOGLOG

يُوصف في الشكل 3 برنامج يهدف إلى التعامل مع معظم ظروف الاستخدام العملية. بالمقارنة مع خوارزمية الشكل 2، يتم تقديم تعديل واحد يتعلق بالتهيئة وتصحيحين نهائيين للتقديرات.

**(i) تهيئة السجلات.** في خوارزمية الشكل 2، يتم تهيئة السجلات عند -∞. لهذا ميزة أنه يؤدي إلى تعبيرات للحالة المتوسطة بسيطة نسبياً: انظر المعادلات (4) و (5). ومع ذلك، فإن النتيجة هي أن التقدير E الذي ترجعه الخوارزمية يفترض القيمة 0 بمجرد ترك أحد السجلات دون مساس، أي بمجرد أن يكون أحد التدفقات الفرعية m فارغاً. نظراً للحقيقة المعروفة فيما يتعلق بمشكلة جامع القسائم، فإن هذا يعني أنه يجب أن نتوقع E = 0 عندما n ≪ m log m، بحيث تخطئ الخوارزمية بشكل سيئ للعدديات الصغيرة.

في برنامج الشكل 3، غيرنا تهيئة السجلات إلى 0. استنتاجات النظرية 1، فيما يتعلق بالطابع غير المنحاز بشكل مقارب للتقدير، لا تزال قابلة للتطبيق على البرنامج، نظراً لأن جميع التدفقات الفرعية غير فارغة باحتمال كبير، بمجرد أن n ≫ m log m. ميزة التعديل هي أنه يمكننا الآن الحصول على تقديرات قابلة للاستخدام حتى عندما تكون n مضاعفاً صغيراً لـ m (يمكن تأكيد هذه الحقيقة أيضاً من خلال تقريبات بواسون). يمكن حينئذ تصحيح التقديرات التي يوفرها البرنامج لقيم صغيرة جداً من n (مثل، n ≈ ثابت أو n ≈ m) بشكل فعال، كما نشرح بعد ذلك.

**(ii) تصحيحات النطاق الصغير.** بالنسبة لبرنامج HYPERLOGLOG (بما في ذلك التعديل في (i) أعلاه، فيما يتعلق بتهيئة السجل)، توضح المحاكاة المكثفة أن النظام المقارب يتم الوصول إليه عملياً (دون التأثير بشكل أساسي على الخطأ الاسمي البالغ 1.04/√m ودون انحياز قابل للكشف) عند قيمة العددية n = 5m/2، عندما m ≥ 16. في المقابل، بالنسبة لـ n < 5m/2، تبدأ التشوهات غير الخطية في الظهور—على الجانب المتطرف، ستعيد الخوارزمية الخام مع السجلات المهيأة إلى 0 دائماً التقدير α_m m ≈ 0.7m عندما n = 0 (!). وبالتالي، يجب تطبيق التصحيحات على التقدير، عندما يكون E (أي n) صغيراً نسبياً بالنسبة لـ m.

يأتي الحل من الخصائص الاحتمالية للتخصيصات العشوائية، كما تم استغلالها بالفعل بواسطة خوارزمية HITCOUNTING لـ Whang وآخرون [24]، والتي تمت مناقشة تحليلها في [9، القسم 4.3]. لنفترض أن n كرات تُرمى بشكل عشوائي في m صندوق. ثم، كما هو معروف جيداً، فإن عدد الصناديق الفارغة يكون حوالي me^{-ρ}، حيث ρ := n/m. وبالتالي، عند ملاحظة V صناديق فارغة من إجمالي m، يمكن للمرء أن يتوقع بشكل مشروع أن يكون ρ قريباً من log(m/V)، أي يجب أن يكون n قريباً من m log(m/V). (يمكن تحليل جودة هذا التقدير بدقة، نظراً لأن الأشكال الدقيقة والمقاربة معروفة للمتوسط والتباين والتوزيع لـ V؛ انظر، على سبيل المثال، [21].) هنا الصناديق هي تلك المرتبطة بـ m "مجموعات فرعية متعددة"، ويعرف المرء أن صندوقاً j فارغ من حقيقة أن سجله المقابل M[j] قد حافظ على قيمته الأولية 0. يتم دمج هذا التصحيح في برنامج الشكل 3.

**(iii) تصحيحات النطاق الكبير.** بالنسبة للعدديات في النطاق 1::N، مع N من رتبة 10^9، يجب استخدام التجزئة على الأقل L = 32 بت (2^32 ≈ 4 × 10^9). ومع ذلك، عندما تقترب العددية n (أو ربما حتى تتجاوز) 2^L، تصبح تصادمات التجزئة أكثر احتمالاً. بالنسبة لدالة تجزئة مختارة عشوائياً، يمكن نمذجة هذا التأثير بنموذج كرات وصناديق من النوع الموصوف في الفقرة السابقة، مع 2^L الآن تحل محل m. بعبارة أخرى، تقدر كمية E لـ HYPERLOGLOG عدد القيم المجزأة المختلفة، والتي تكون باحتمال عالٍ، حوالي 2^L(1 - e^{-ρ})، حيث ρ = n/2^L. عكس تلك العلاقة يعطينا حينئذ المعادلة التقريبية n ≈ -2^L log(1 - E/2^L)، وهي المستخدمة في البرنامج.

فيما يتعلق بالسجلات، تتراوح قيمها a priori في الفترة 0::L+1-log₂ m. مع القيم المجزأة بـ 32 بت، هذا يعني أن 5 بتات ("بايتات قصيرة") كافية لتخزين السجلات (بالطبع، يمكن أيضاً استخدام البايتات القياسية 8 بت في بعض التطبيقات). فيما يتعلق بجودة النتائج المعادة، نتوقع أن تكون قيم التقدير المعاد تقريباً غاوسية، بسبب تأثير المتوسط ونظرية الحد المركزي: هذه الخاصية مدعومة بالفعل بشكل جيد من خلال محاكاة الشكل 4 (أسفل). وفقاً لذلك:

**دع σ = 1.04/√m يمثل الخطأ المعياري؛ من المتوقع أن تكون التقديرات التي يوفرها HYPERLOGLOG ضمن σ، 2σ، 3σ من العد الدقيق في 65%، 95%، 99% من جميع الحالات على التوالي.**

في الممارسة العملية، برنامج HYPERLOGLOG فعال للغاية: مثل LOGLOG القياسي لـ [10] أو MINCOUNT لـ [16]، يهيمن على وقت تشغيله حساب دالة التجزئة، بحيث يكون أبطأ بثلاث إلى أربع مرات فقط من المسح البسيط للبيانات (على سبيل المثال، بأمر Unix "wc -l"، الذي يحسب فقط نهايات الأسطر).

## اعتبارات الأمثلية

تنتج الأمثلية شبه الكاملة المعبر عنها بعنواننا من مزيج من حقيقتين.

**(i)** من الواضح أن الحفاظ على عدادات تقريبية ε حتى نطاق N يتطلب Ω(log log N) بت. في الواقع، يجب أن تكون العدديات موجودة على مقياس أسي،

$$1, (1+ε), (1+ε)^2, ..., (1+ε)^L = N,$$

والتي تتضمن log_{(1+ε)} N فترة، تتطلب على الأقل log₂ log_{(1+ε)} N بت من المعلومات لتمثيلها.

**(ii)** بالنسبة لفئة واسعة من الخوارزميات القائمة على إحصاءات الترتيب، أظهر Chassaing و Gérin [6] أن أفضل دقة قابلة للتحقيق محدودة من الأسفل بكمية قريبة من 1/√m. خوارزميتنا، التي يمكن اعتبارها الحفاظ على إحصاءات ترتيب تقريبية، على أساس هذه النتيجة فقط بعيدة حوالي 4% عن الأمثل النظري للمعلومات لفئة Chassaing-Gérin، بينما تستخدم وحدات ذاكرة أقصر عادةً بمقدار 3 إلى 5 مرات.

كملخص نهائي، تثبت الخوارزمية أنها سهلة الترميز وفعالة، بل وشبه مثالية تحت معايير معينة. على البيانات "الواقعية"، يبدو أنها في اتفاق ممتاز مع التحليل النظري، وهي حقيقة تم التحقق منها مؤخراً من خلال اختبارات مكثفة (انظر الشكل 5 للعينة) أجراها Pranav Kashyap، الذي يُشكر مساهمته هنا بامتنان. يمكن تطبيق البرنامج على مجموعات بيانات متنوعة جداً (يلزم فقط دالة تجزئة "جيدة")، وبمجرد تجهيزه بالتصحيحات المناسبة، يمكنه التعامل بسلاسة مع مجموعة واسعة من العدديات—من الصغيرة جداً إلى الكبيرة جداً. بالإضافة إلى ذلك، يتوازى أو يوزع بشكل مثالي ويمكن تكييفه لاستخدام "النافذة المنزلقة" [7].

في المجمل، HYPERLOGLOG عملي للغاية ومتعدد الاستخدامات، ويتوافق بشكل جيد مع ما يتنبأ به التحليل.

---

**برنامج HYPERLOGLOG** (مدخل M: مجموعة متعددة من العناصر من المجال D)

دع h: D → {0,1}^32 تجزأ البيانات من D إلى كلمات ثنائية 32 بت.
دع ρ(s) يكون موضع البت 1 الأيسر من s: مثلاً، ρ(1···) = 1؛ ρ(0001···) = 4؛ ρ(0^K···) = K+1.
عرّف α₁₆ = 0.673؛ α₃₂ = 0.697؛ α₆₄ = 0.709؛ α_m = 0.7213/(1+1.079/m) لـ m ≥ 128.

```
افترض m = 2^b مع b ∈ [4::16].
ابدأ مجموعة من m سجل، M[1]، ...، M[m]، بـ 0;
for v ∈ M do
    اجعل x := h(v);
    اجعل j = 1 + ⟨x₁x₂...x_b⟩₂;  {العنوان الثنائي المحدد بواسطة أول b بت من x}
    اجعل w := x_{b+1}x_{b+2}...;
    اجعل M[j] := max(M[j], ρ(w));
احسب E := α_m m² (∑_{j=1}^m 2^{-M[j]})^{-1};  {تقدير HyperLogLog "الخام"}
if E ≤ 5m/2 then
    دع V يكون عدد السجلات المساوية لـ 0;
    if V ≠ 0 then اجعل E* := m log(m/V) else اجعل E* := E;  {تصحيح النطاق الصغير}
if E ∈ ]5m/2, 1/30 × 2^32] then
    اجعل E* := E;  {النطاق المتوسط—لا تصحيح}
if E > 1/30 × 2^32 then
    اجعل E* := -2^32 log(1 - E/2^32);  {تصحيح النطاق الكبير}
أرجع تقدير العددية E* مع خطأ نسبي نموذجي 1.04/√m.
```

**الشكل 3:** برنامج HYPERLOGLOG المُحدّد للعدديات القصوى في النطاق [0::10^9] ولقيم "عملية" شائعة m = 2^4، ...، 2^16.

---

### Translation Notes

- **Figures referenced:** Figures 3, 4, 5 (algorithm pseudocode, simulation results, real-world tests)
- **Key terms introduced:** coupon collector problem (مشكلة جامع القسائم), hash collision (تصادم التجزئة), Gaussian distribution (توزيع غاوسي), short byte (بايت قصير), sliding window (نافذة منزلقة)
- **Equations:** Program pseudocode with range corrections
- **Citations:** [6, 7, 9, 10, 16, 21, 24]
- **Special handling:** Practical implementation details, parameter tuning, real-world performance analysis

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.85
- Glossary consistency: 0.85
- **Overall section score:** 0.87
