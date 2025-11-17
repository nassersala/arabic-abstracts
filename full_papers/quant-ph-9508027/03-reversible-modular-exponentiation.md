# Section 3: Reversible Logic and Modular Exponentiation
## القسم 3: المنطق القابل للعكس والأس النمطي

**Section:** reversible-logic-modular-exponentiation
**Translation Quality:** 0.86
**Glossary Terms Used:** reversible computation, quantum gate, Toffoli gate, Fredkin gate, modular exponentiation, algorithm, polynomial time, gate array, unitary transformation, quantum computer, Bennett's method, Schönhage-Strassen algorithm

---

### English Version

The definition of quantum gate arrays gives rise to completely reversible computation. That is, knowing the quantum state on the wires leading out of a gate tells uniquely what the quantum state must have been on the wires leading into that gate. This is a reflection of the fact that, despite the macroscopic arrow of time, the laws of physics appear to be completely reversible. This would seem to imply that anything built with the laws of physics must be completely reversible; however, classical computers get around this fact by dissipating energy and thus making their computations thermodynamically irreversible. This appears impossible to do for quantum computers because superpositions of quantum states need to be maintained throughout the computation. Thus, quantum computers necessarily have to use reversible computation. This imposes extra costs when doing classical computations on a quantum computer, as is sometimes necessary in subroutines of quantum computations.

Because of the reversibility of quantum computation, a deterministic computation is performable on a quantum computer only if it is reversible. Luckily, it has already been shown that any deterministic computation can be made reversible [Lecerf 1963, Bennett 1973]. In fact, reversible classical gate arrays have been studied. Much like the result that any classical computation can be done using NAND gates, there are also universal gates for reversible computation. Two of these are Toffoli gates [Toffoli 1980] and Fredkin gates [Fredkin and Toffoli 1982]; these are illustrated in Table 3.1.

The Toffoli gate is just a controlled controlled NOT, i.e., the last bit is negated if and only if the first two bits are 1. In a Toffoli gate, if the third input bit is set to 1, then the third output bit is the NAND of the first two input bits. Since NAND is a universal gate for classical gate arrays, this shows that the Toffoli gate is universal. In a Fredkin gate, the last two bits are swapped if the first bit is 0, and left untouched if the first bit is 1. For a Fredkin gate, if the third input bit is set to 0, the second output bit is the AND of the first two input bits; and if the last two input bits are set to 0 and 1 respectively, the second output bit is the NOT of the first input bit. Thus, both AND and NOT gates are realizable using Fredkin gates, showing that the Fredkin gate is universal.

From results on reversible computation [Lecerf 1963, Bennett 1973], we can compute any polynomial time function $F(x)$ as long as we keep the input $x$ in the computer. We do this by adapting the method for computing the function $F$ non-reversibly. These results can easily be extended to work for gate arrays [Toffoli 1980, Fredkin and Toffoli 1982]. When AND, OR or NOT gates are changed to Fredkin or Toffoli gates, one obtains both additional input bits, which must be preset to specified values, and additional output bits, which contain the information needed to reverse the computation. While the additional input bits do not present difficulties in designing quantum computers, the additional output bits do, because unless they are all reset to 0, they will affect the interference patterns in quantum computation. Bennett's method for resetting these bits to 0 is shown in the top half of Table 3.2. A non-reversible gate array may thus be turned into a reversible gate array as follows. First, duplicate the input bits as many times as necessary (since each input bit could be used more than once by the gate array). Next, keeping one copy of the input around, use Toffoli and Fredkin gates to simulate non-reversible gates, putting the extra output bits into the RECORD register. These extra output bits preserve enough of a record of the operations to enable the computation of the gate array to be reversed. Once the output $F(x)$ has been computed, copy it into a register that has been preset to zero, and then undo the computation to erase both the first OUTPUT register and the RECORD register.

To erase $x$ and replace it with $F(x)$, in addition to a polynomial-time algorithm for $F$, we also need a polynomial-time algorithm for computing $x$ from $F(x)$; i.e., we need that $F$ is one-to-one and that both $F$ and $F^{-1}$ are polynomial-time computable. The method for this computation is given in the whole of Table 3.2. There are two stages to this computation. The first is the same as before, taking $x$ to $(x, F(x))$. For the second stage, shown in the bottom half of Table 3.2, note that if we have a method to compute $F^{-1}$ non-reversibly in polynomial time, we can use the same technique to reversibly map $F(x)$ to $(F(x), F^{-1}(F(x))) = (F(x), x)$. However, since this is a reversible computation, we can reverse it to go from $(x, F(x))$ to $F(x)$. Put together, these two pieces take $x$ to $F(x)$.

The above discussion shows that computations can be made reversible for only a constant factor cost in time, but the above method uses as much space as it does time. If the classical computation requires much less space than time, then making it reversible in this manner will result in a large increase in the space required. There are methods that do not use as much space, but use more time, to make computations reversible [Bennett 1989, Levine and Sherman 1990]. While there is no general method that does not cause an increase in either space or time, specific algorithms can sometimes be made reversible without paying a large penalty in either space or time; at the end of this section we will show how to do this for modular exponentiation, which is a subroutine necessary for quantum factoring.

**Modular Exponentiation**

The bottleneck in the quantum factoring algorithm; i.e., the piece of the factoring algorithm that consumes the most time and space, is modular exponentiation. The modular exponentiation problem is, given $n$, $x$, and $r$, find $x^r \pmod{n}$.

The best classical method for doing this is to repeatedly square $x \pmod{n}$ to get $x^{2^i} \pmod{n}$ for $i \leq \log_2 r$, and then multiply a subset of these powers $\pmod{n}$ to get $x^r \pmod{n}$. If we are working with $l$-bit numbers, this requires $O(l)$ squarings and multiplications of $l$-bit numbers $\pmod{n}$. Asymptotically, the best classical result for gate arrays for multiplication is the Schönhage–Strassen algorithm [Schönhage and Strassen 1971, Knuth 1981, Schönhage 1982]. This gives a gate array for integer multiplication that uses $O(l \log l \log \log l)$ gates to multiply two $l$-bit numbers. Thus, asymptotically, modular exponentiation requires $O(l^2 \log l \log \log l)$ time. Making this reversible would naïvely cost the same amount in space; however, one can reuse the space used in the repeated squaring part of the algorithm, and thus reduce the amount of space needed to essentially that required for multiplying two $l$-bit numbers; one simple method for reducing this space (although not the most versatile one) will be given later in this section. Thus, modular exponentiation can be done in $O(l^2 \log l \log \log l)$ time and $O(l \log l \log \log l)$ space.

While the Schönhage–Strassen algorithm is the best multiplication algorithm discovered to date for large $l$, it does not scale well for small $l$. For small numbers, the best gate arrays for multiplication essentially use elementary-school longhand multiplication in binary. This method requires $O(l^2)$ time to multiply two $l$-bit numbers, and thus modular exponentiation requires $O(l^3)$ time with this method. These gate arrays can be made reversible, however, using only $O(l)$ space.

We will now give the method for constructing a reversible gate array that takes only $O(l)$ space and $O(l^3)$ time to compute $(a, x^a \pmod{n})$ from $a$, where $a$, $x$, and $n$ are $l$-bit numbers. The basic building block used is a gate array that takes $b$ as input and outputs $b + c \pmod{n}$. Note that here $b$ is the gate array's input but $c$ and $n$ are built into the structure of the gate array. Since addition $\pmod{n}$ is computable in $O(\log n)$ time classically, this reversible gate array can be made with only $O(\log n)$ gates and $O(\log n)$ work bits using the techniques explained earlier in this section.

The technique we use for computing $x^a \pmod{n}$ is essentially the same as the classical method. First, by repeated squaring we compute $x^{2^i} \pmod{n}$ for all $i < l$. Then, to obtain $x^a \pmod{n}$ we multiply the powers $x^{2^i} \pmod{n}$ where $2^i$ appears in the binary expansion of $a$. In our algorithm for factoring $n$, we only need to compute $x^a \pmod{n}$ where $a$ is in a superposition of states, but $x$ is some fixed integer. This makes things much easier, because we can use a reversible gate array where $a$ is treated as input, but where $x$ and $n$ are built into the structure of the gate array. Thus, we can use the algorithm described by the following pseudocode; here, $a_i$ represents the $i$-th bit of $a$ in binary, where the bits are indexed from right to left and the rightmost bit of $a$ is $a_0$.

```
power := 1
for i = 0 to l-1
    if (a_i == 1) then
        power := power * x^(2^i) (mod n)
    endif
endfor
```

The variable $a$ is left unchanged by the code and $x^a \pmod{n}$ is output as the variable `power`. Thus, this code takes the pair of values $(a, 1)$ to $(a, x^a \pmod{n})$.

This pseudocode can easily be turned into a gate array; the only hard part of this is the fourth line, where we multiply the variable `power` by $x^{2^i} \pmod{n}$; to do this we need to use a fairly complicated gate array as a subroutine. Recall that $x^{2^i} \pmod{n}$ can be computed classically and then built into the structure of the gate array. Thus, to implement this line, we need a reversible gate array that takes $b$ as input and gives $bc \pmod{n}$ as output, where the structure of the gate array can depend on $c$ and $n$. Of course, this step can only be reversible if $\gcd(c, n) = 1$, i.e., if $c$ and $n$ have no common factors, as otherwise two distinct values of $b$ will be mapped to the same value of $bc \pmod{n}$; this case is fortunately all we need for the factoring algorithm. We will show how to build this gate array in two stages. The first stage is directly analogous to exponentiation by repeated multiplication; we obtain multiplication from repeated addition $\pmod{n}$. Pseudocode for this stage is as follows:

```
result := 0
for i = 0 to l-1
    if (b_i == 1) then
        result := result + 2^i c (mod n)
    endif
endfor
```

Again, $2^i c \pmod{n}$ can be precomputed and built into the structure of the gate array.

The above pseudocode takes $b$ as input, and gives $(b, bc \pmod{n})$ as output. To get the desired result, we now need to erase $b$. Recall that $\gcd(c, n) = 1$, so there is a $c^{-1} \pmod{n}$ with $c c^{-1} \equiv 1 \pmod{n}$. Multiplication by this $c^{-1}$ could be used to reversibly take $bc \pmod{n}$ to $(bc \pmod{n}, bcc^{-1} \pmod{n}) = (bc \pmod{n}, b)$. This is just the reverse of the operation we want, and since we are working with reversible computing, we can turn this operation around to erase $b$. The pseudocode for this follows:

```
for i = 0 to l-1
    if (result_i == 1) then
        b := b - 2^i c^(-1) (mod n)
    endif
endfor
```

As before, `result_i` is the $i$-th bit of `result`.

Note that at this stage of the computation, $b$ should be 0. However, we did not set $b$ directly to zero, as this would not have been a reversible operation and thus impossible on a quantum computer, but instead we did a relatively complicated sequence of operations which ended with $b = 0$ and which in fact depended on multiplication being a group $\pmod{n}$. At this point, then, we could do something somewhat sneaky: we could measure $b$ to see if it actually is 0. If it is not, we know that there has been an error somewhere in the quantum computation, i.e., that the results are worthless and we should stop the computer and start over again. However, if we do find that $b$ is 0, then we know (because we just observed it) that it is now exactly 0. This measurement thus may bring the quantum computation back on track in that any amplitude that $b$ had for being non-zero has been eliminated. Further, because the probability that we observe a state is proportional to the square of the amplitude of that state, depending on the error model, doing the modular exponentiation and measuring $b$ every time that we know that it should be 0 may have a higher probability of overall success than the same computation done without the repeated measurements of $b$; this is the quantum watchdog (or quantum Zeno) effect [Peres 1993]. The argument above does not actually show that repeated measurement of $b$ is indeed beneficial, because there is a cost (in time, if nothing else) of measuring $b$. Before this is implemented, then, it should be checked with analysis or experiment that the benefit of such measurements exceeds their cost. However, I believe that partial measurements such as this one are a promising way of trying to stabilize quantum computations.

Currently, Schönhage–Strassen is the algorithm of choice for multiplying very large numbers, and longhand multiplication is the algorithm of choice for small numbers. There are also multiplication algorithms which have efficiencies between these two algorithms, and which are the best algorithms to use for intermediate length numbers [Karatsuba and Ofman 1962, Knuth 1981, Schönhage et al. 1994]. It is not clear which algorithms are best for which size numbers. While this may be known to some extent for classical computation [Schönhage et al. 1994], using data on which algorithms work better on classical computers could be misleading for two reasons: First, classical computers need not be reversible, and the cost of making an algorithm reversible depends on the algorithm. Second, existing computers generally have multiplication for 32- or 64-bit numbers built into their hardware, and this will increase the optimal changeover points to asymptotically faster algorithms; further, some multiplication algorithms can take better advantage of this hardwired multiplication than others. Thus, in order to program quantum computers most efficiently, work needs to be done on the best way of implementing elementary arithmetic operations on quantum computers. One tantalizing fact is that the Schönhage–Strassen fast multiplication algorithm uses the fast Fourier transform, which is also the basis for all the fast algorithms on quantum computers discovered to date; it is tempting to speculate that integer multiplication itself might be speeded up by a quantum algorithm; if possible, this would result in a somewhat faster asymptotic bound for factoring on a quantum computer, and indeed could even make breaking RSA on a quantum computer asymptotically faster than encrypting with RSA on a classical computer.

---

### النسخة العربية

يؤدي تعريف مصفوفات البوابات الكمومية إلى حوسبة قابلة للعكس بالكامل. أي أن معرفة الحالة الكمومية على الأسلاك الخارجة من بوابة تخبرنا بشكل فريد بما يجب أن تكون عليه الحالة الكمومية على الأسلاك الداخلة إلى تلك البوابة. هذا انعكاس لحقيقة أنه، على الرغم من سهم الزمن الماكروسكوبي، فإن قوانين الفيزياء تبدو قابلة للعكس بالكامل. قد يبدو هذا يعني ضمناً أن أي شيء مبني بقوانين الفيزياء يجب أن يكون قابلاً للعكس بالكامل؛ ومع ذلك، تتجاوز الحواسيب الكلاسيكية هذه الحقيقة عن طريق تبديد الطاقة وبالتالي جعل حساباتها غير قابلة للعكس ترموديناميكياً. يبدو أن هذا مستحيل القيام به للحواسيب الكمومية لأن تراكبات الحالات الكمومية يجب أن تُحافظ عليها طوال الحساب. وبالتالي، يجب على الحواسيب الكمومية بالضرورة استخدام الحوسبة القابلة للعكس. هذا يفرض تكاليف إضافية عند إجراء حسابات كلاسيكية على حاسوب كمومي، كما هو ضروري أحياناً في روتينات فرعية للحسابات الكمومية.

بسبب قابلية العكس للحوسبة الكمومية، يمكن تنفيذ حساب حتمي على حاسوب كمومي فقط إذا كان قابلاً للعكس. لحسن الحظ، تم بالفعل إظهار أن أي حساب حتمي يمكن جعله قابلاً للعكس [Lecerf 1963، Bennett 1973]. في الواقع، تمت دراسة مصفوفات البوابات الكلاسيكية القابلة للعكس. تماماً مثل النتيجة القائلة بأن أي حساب كلاسيكي يمكن إجراؤه باستخدام بوابات NAND، هناك أيضاً بوابات شاملة للحوسبة القابلة للعكس. اثنان من هذه البوابات هما بوابات توفولي [Toffoli 1980] وبوابات فريدكين [Fredkin و Toffoli 1982]؛ وهي موضحة في الجدول 3.1.

بوابة توفولي هي فقط NOT متحكم به مزدوج، أي أن البت الأخير يُنفى إذا وفقط إذا كان البتان الأولان 1. في بوابة توفولي، إذا تم ضبط بت الإدخال الثالث على 1، فإن بت الإخراج الثالث هو NAND للبتين الأولين من الإدخال. نظراً لأن NAND هي بوابة شاملة لمصفوفات البوابات الكلاسيكية، فهذا يُظهر أن بوابة توفولي شاملة. في بوابة فريدكين، يتم تبديل البتين الأخيرين إذا كان البت الأول 0، ويُتركان دون تغيير إذا كان البت الأول 1. لبوابة فريدكين، إذا تم ضبط بت الإدخال الثالث على 0، فإن بت الإخراج الثاني هو AND للبتين الأولين من الإدخال؛ وإذا تم ضبط بتي الإدخال الأخيرين على 0 و 1 على التوالي، فإن بت الإخراج الثاني هو NOT لبت الإدخال الأول. وبالتالي، فإن كلاً من بوابات AND و NOT قابلة للتحقيق باستخدام بوابات فريدكين، مما يُظهر أن بوابة فريدكين شاملة.

من نتائج الحوسبة القابلة للعكس [Lecerf 1963، Bennett 1973]، يمكننا حساب أي دالة زمن متعدد حدود $F(x)$ طالما احتفظنا بالمدخل $x$ في الحاسوب. نقوم بذلك عن طريق تكييف الطريقة لحساب الدالة $F$ بشكل غير قابل للعكس. يمكن بسهولة توسيع هذه النتائج لتعمل لمصفوفات البوابات [Toffoli 1980، Fredkin و Toffoli 1982]. عندما تتغير بوابات AND أو OR أو NOT إلى بوابات فريدكين أو توفولي، يحصل المرء على كل من بتات إدخال إضافية، يجب أن تُضبط مسبقاً على قيم محددة، وبتات إخراج إضافية، تحتوي على المعلومات اللازمة لعكس الحساب. بينما بتات الإدخال الإضافية لا تمثل صعوبات في تصميم الحواسيب الكمومية، فإن بتات الإخراج الإضافية تفعل ذلك، لأنه ما لم يتم إعادة ضبطها جميعاً على 0، فإنها ستؤثر على أنماط التداخل في الحوسبة الكمومية. طريقة بينيت لإعادة ضبط هذه البتات إلى 0 معروضة في النصف العلوي من الجدول 3.2. وبالتالي، يمكن تحويل مصفوفة بوابات غير قابلة للعكس إلى مصفوفة بوابات قابلة للعكس على النحو التالي. أولاً، قم بتكرار بتات الإدخال بقدر ما هو ضروري (نظراً لأن كل بت إدخال يمكن استخدامه أكثر من مرة بواسطة مصفوفة البوابات). بعد ذلك، مع الاحتفاظ بنسخة واحدة من المدخل، استخدم بوابات توفولي وفريدكين لمحاكاة البوابات غير القابلة للعكس، ووضع بتات الإخراج الإضافية في سجل RECORD. هذه البتات الإضافية للإخراج تحتفظ بما يكفي من سجل للعمليات لتمكين عكس حساب مصفوفة البوابات. بمجرد حساب الإخراج $F(x)$، انسخه إلى سجل تم ضبطه مسبقاً على صفر، ثم تراجع عن الحساب لمسح كل من سجل OUTPUT الأول وسجل RECORD.

لمسح $x$ واستبداله بـ $F(x)$، بالإضافة إلى خوارزمية زمن متعدد حدود لـ $F$، نحتاج أيضاً إلى خوارزمية زمن متعدد حدود لحساب $x$ من $F(x)$؛ أي نحتاج إلى أن تكون $F$ واحد لواحد وأن يكون كل من $F$ و $F^{-1}$ قابلين للحساب في زمن متعدد حدود. طريقة هذا الحساب معطاة في الجدول 3.2 بأكمله. هناك مرحلتان لهذا الحساب. الأولى هي نفسها كما كانت من قبل، تأخذ $x$ إلى $(x, F(x))$. للمرحلة الثانية، الموضحة في النصف السفلي من الجدول 3.2، لاحظ أنه إذا كان لدينا طريقة لحساب $F^{-1}$ بشكل غير قابل للعكس في زمن متعدد حدود، فيمكننا استخدام نفس التقنية لرسم $F(x)$ بشكل قابل للعكس إلى $(F(x), F^{-1}(F(x))) = (F(x), x)$. ومع ذلك، نظراً لأن هذا حساب قابل للعكس، يمكننا عكسه للانتقال من $(x, F(x))$ إلى $F(x)$. معاً، هاتان القطعتان تأخذان $x$ إلى $F(x)$.

المناقشة أعلاه تُظهر أن الحسابات يمكن جعلها قابلة للعكس بتكلفة عامل ثابت فقط في الزمن، لكن الطريقة أعلاه تستخدم من المساحة بقدر ما تستخدم من الزمن. إذا كان الحساب الكلاسيكي يتطلب مساحة أقل بكثير من الزمن، فإن جعله قابلاً للعكس بهذه الطريقة سيؤدي إلى زيادة كبيرة في المساحة المطلوبة. هناك طرق لا تستخدم مساحة كبيرة، ولكنها تستخدم زمناً أكثر، لجعل الحسابات قابلة للعكس [Bennett 1989، Levine و Sherman 1990]. بينما لا توجد طريقة عامة لا تسبب زيادة في المساحة أو الزمن، يمكن أحياناً جعل خوارزميات محددة قابلة للعكس دون دفع غرامة كبيرة في المساحة أو الزمن؛ في نهاية هذا القسم سنُظهر كيفية القيام بذلك للأس النمطي، وهو روتين فرعي ضروري للتحليل الكمومي إلى عوامل.

**الأس النمطي**

الاختناق في خوارزمية التحليل الكمومي إلى عوامل؛ أي الجزء من خوارزمية التحليل إلى عوامل الذي يستهلك أكبر قدر من الزمن والمساحة، هو الأس النمطي. مسألة الأس النمطي هي، بالنظر إلى $n$ و $x$ و $r$، إيجاد $x^r \pmod{n}$.

أفضل طريقة كلاسيكية للقيام بذلك هي تربيع $x \pmod{n}$ بشكل متكرر للحصول على $x^{2^i} \pmod{n}$ لـ $i \leq \log_2 r$، ثم ضرب مجموعة فرعية من هذه القوى $\pmod{n}$ للحصول على $x^r \pmod{n}$. إذا كنا نعمل مع أرقام $l$-بت، فهذا يتطلب $O(l)$ من عمليات التربيع والضرب لأرقام $l$-بت $\pmod{n}$. تقاربياً، أفضل نتيجة كلاسيكية لمصفوفات البوابات للضرب هي خوارزمية Schönhage-Strassen [Schönhage و Strassen 1971، Knuth 1981، Schönhage 1982]. هذا يعطي مصفوفة بوابات لضرب الأعداد الصحيحة تستخدم $O(l \log l \log \log l)$ من البوابات لضرب رقمين $l$-بت. وبالتالي، تقاربياً، يتطلب الأس النمطي $O(l^2 \log l \log \log l)$ زمناً. جعل هذا قابلاً للعكس سيكلف بسذاجة نفس الكمية في المساحة؛ ومع ذلك، يمكن للمرء إعادة استخدام المساحة المستخدمة في جزء التربيع المتكرر من الخوارزمية، وبالتالي تقليل كمية المساحة المطلوبة إلى ما هو مطلوب بشكل أساسي لضرب رقمين $l$-بت؛ سيتم إعطاء طريقة بسيطة واحدة لتقليل هذه المساحة (على الرغم من أنها ليست الأكثر مرونة) لاحقاً في هذا القسم. وبالتالي، يمكن إجراء الأس النمطي في $O(l^2 \log l \log \log l)$ زمناً و $O(l \log l \log \log l)$ مساحة.

بينما خوارزمية Schönhage-Strassen هي أفضل خوارزمية ضرب تم اكتشافها حتى الآن لـ $l$ الكبيرة، فهي لا تتدرج بشكل جيد لـ $l$ الصغيرة. للأرقام الصغيرة، أفضل مصفوفات البوابات للضرب تستخدم بشكل أساسي الضرب اليدوي للمدرسة الابتدائية في النظام الثنائي. هذه الطريقة تتطلب $O(l^2)$ زمناً لضرب رقمين $l$-بت، وبالتالي يتطلب الأس النمطي $O(l^3)$ زمناً مع هذه الطريقة. ومع ذلك، يمكن جعل مصفوفات البوابات هذه قابلة للعكس، باستخدام $O(l)$ مساحة فقط.

سنعطي الآن الطريقة لبناء مصفوفة بوابات قابلة للعكس تأخذ $O(l)$ مساحة فقط و $O(l^3)$ زمناً لحساب $(a, x^a \pmod{n})$ من $a$، حيث $a$ و $x$ و $n$ هي أرقام $l$-بت. الكتلة البنائية الأساسية المستخدمة هي مصفوفة بوابات تأخذ $b$ كمدخل وتخرج $b + c \pmod{n}$. لاحظ أنه هنا $b$ هو مدخل مصفوفة البوابات ولكن $c$ و $n$ مدمجان في بنية مصفوفة البوابات. نظراً لأن الجمع $\pmod{n}$ قابل للحساب في $O(\log n)$ زمناً كلاسيكياً، يمكن إنشاء مصفوفة البوابات القابلة للعكس هذه بـ $O(\log n)$ من البوابات و $O(\log n)$ من بتات العمل فقط باستخدام التقنيات الموضحة سابقاً في هذا القسم.

التقنية التي نستخدمها لحساب $x^a \pmod{n}$ هي بشكل أساسي نفس الطريقة الكلاسيكية. أولاً، عن طريق التربيع المتكرر نحسب $x^{2^i} \pmod{n}$ لكل $i < l$. ثم، للحصول على $x^a \pmod{n}$ نضرب القوى $x^{2^i} \pmod{n}$ حيث يظهر $2^i$ في التوسع الثنائي لـ $a$. في خوارزميتنا لتحليل $n$ إلى عوامل، نحتاج فقط إلى حساب $x^a \pmod{n}$ حيث $a$ في تراكب من الحالات، ولكن $x$ هو عدد صحيح ثابت. هذا يجعل الأمور أسهل بكثير، لأنه يمكننا استخدام مصفوفة بوابات قابلة للعكس حيث يُعامل $a$ كمدخل، ولكن حيث $x$ و $n$ مدمجان في بنية مصفوفة البوابات. وبالتالي، يمكننا استخدام الخوارزمية الموصوفة بالكود الزائف التالي؛ هنا، $a_i$ يمثل البت $i$-ي من $a$ في النظام الثنائي، حيث تُفهرس البتات من اليمين إلى اليسار والبت الأيمن من $a$ هو $a_0$.

```
power := 1
for i = 0 to l-1
    if (a_i == 1) then
        power := power * x^(2^i) (mod n)
    endif
endfor
```

المتغير $a$ يُترك دون تغيير بواسطة الكود و $x^a \pmod{n}$ يُخرج كمتغير `power`. وبالتالي، يأخذ هذا الكود زوج القيم $(a, 1)$ إلى $(a, x^a \pmod{n})$.

يمكن بسهولة تحويل هذا الكود الزائف إلى مصفوفة بوابات؛ الجزء الصعب الوحيد من هذا هو السطر الرابع، حيث نضرب المتغير `power` بـ $x^{2^i} \pmod{n}$؛ للقيام بذلك نحتاج إلى استخدام مصفوفة بوابات معقدة إلى حد ما كروتين فرعي. تذكر أن $x^{2^i} \pmod{n}$ يمكن حسابه كلاسيكياً ثم دمجه في بنية مصفوفة البوابات. وبالتالي، لتنفيذ هذا السطر، نحتاج إلى مصفوفة بوابات قابلة للعكس تأخذ $b$ كمدخل وتعطي $bc \pmod{n}$ كإخراج، حيث يمكن أن تعتمد بنية مصفوفة البوابات على $c$ و $n$. بالطبع، يمكن أن تكون هذه الخطوة قابلة للعكس فقط إذا كان $\gcd(c, n) = 1$، أي إذا لم يكن لدى $c$ و $n$ عوامل مشتركة، وإلا فإن قيمتين مختلفتين من $b$ ستُخرجان إلى نفس قيمة $bc \pmod{n}$؛ هذه الحالة لحسن الحظ هي كل ما نحتاجه لخوارزمية التحليل إلى عوامل. سنُظهر كيفية بناء مصفوفة البوابات هذه في مرحلتين. المرحلة الأولى مماثلة مباشرة للأس عن طريق الضرب المتكرر؛ نحصل على الضرب من الجمع المتكرر $\pmod{n}$. الكود الزائف لهذه المرحلة هو كما يلي:

```
result := 0
for i = 0 to l-1
    if (b_i == 1) then
        result := result + 2^i c (mod n)
    endif
endfor
```

مرة أخرى، يمكن حساب $2^i c \pmod{n}$ مسبقاً ودمجه في بنية مصفوفة البوابات.

الكود الزائف أعلاه يأخذ $b$ كمدخل، ويعطي $(b, bc \pmod{n})$ كإخراج. للحصول على النتيجة المطلوبة، نحتاج الآن إلى مسح $b$. تذكر أن $\gcd(c, n) = 1$، لذلك يوجد $c^{-1} \pmod{n}$ مع $c c^{-1} \equiv 1 \pmod{n}$. يمكن استخدام الضرب بهذا $c^{-1}$ لأخذ $bc \pmod{n}$ بشكل قابل للعكس إلى $(bc \pmod{n}, bcc^{-1} \pmod{n}) = (bc \pmod{n}, b)$. هذا هو فقط عكس العملية التي نريدها، ونظراً لأننا نعمل مع الحوسبة القابلة للعكس، يمكننا تحويل هذه العملية لمسح $b$. الكود الزائف لهذا يتبع:

```
for i = 0 to l-1
    if (result_i == 1) then
        b := b - 2^i c^(-1) (mod n)
    endif
endfor
```

كما كان من قبل، `result_i` هو البت $i$-ي من `result`.

لاحظ أنه في هذه المرحلة من الحساب، يجب أن يكون $b$ هو 0. ومع ذلك، لم نضبط $b$ مباشرة على صفر، لأن هذا لن يكون عملية قابلة للعكس وبالتالي مستحيلة على حاسوب كمومي، ولكن بدلاً من ذلك قمنا بسلسلة معقدة نسبياً من العمليات التي انتهت بـ $b = 0$ والتي اعتمدت في الواقع على كون الضرب مجموعة $\pmod{n}$. في هذه المرحلة، إذن، يمكننا القيام بشيء ماكر إلى حد ما: يمكننا قياس $b$ لمعرفة ما إذا كان بالفعل 0. إذا لم يكن كذلك، فنحن نعلم أن هناك خطأً في مكان ما في الحساب الكمومي، أي أن النتائج لا قيمة لها ويجب علينا إيقاف الحاسوب والبدء من جديد. ومع ذلك، إذا وجدنا أن $b$ هو 0، فنحن نعلم (لأننا لاحظناه للتو) أنه الآن بالضبط 0. قد يعيد هذا القياس الحساب الكمومي إلى المسار الصحيح بمعنى أن أي سعة كان لدى $b$ لكونه غير صفر قد تم القضاء عليها. علاوة على ذلك، لأن احتمالية أن نلاحظ حالة تتناسب مع مربع سعة تلك الحالة، اعتماداً على نموذج الخطأ، فإن إجراء الأس النمطي وقياس $b$ في كل مرة نعرف فيها أنه يجب أن يكون 0 قد يكون له احتمالية أعلى للنجاح الإجمالي من نفس الحساب الذي يتم بدون القياسات المتكررة لـ $b$؛ هذا هو تأثير المراقبة الكمومية (أو تأثير زينو الكمومي) [Peres 1993]. الحجة أعلاه لا تُظهر فعلياً أن القياس المتكرر لـ $b$ مفيد بالفعل، لأن هناك تكلفة (في الزمن، إن لم يكن هناك شيء آخر) لقياس $b$. قبل تنفيذ هذا، إذن، يجب التحقق بالتحليل أو التجربة من أن فائدة مثل هذه القياسات تتجاوز تكلفتها. ومع ذلك، أعتقد أن القياسات الجزئية مثل هذه واحدة طريقة واعدة لمحاولة تثبيت الحسابات الكمومية.

حالياً، Schönhage-Strassen هي الخوارزمية المفضلة لضرب أرقام كبيرة جداً، والضرب اليدوي هو الخوارزمية المفضلة للأرقام الصغيرة. هناك أيضاً خوارزميات ضرب ذات كفاءات بين هاتين الخوارزميتين، وهي أفضل الخوارزميات للاستخدام لأرقام ذات طول متوسط [Karatsuba و Ofman 1962، Knuth 1981، Schönhage et al. 1994]. ليس من الواضح أي الخوارزميات هي الأفضل لأي أحجام أرقام. بينما قد يُعرف هذا إلى حد ما للحوسبة الكلاسيكية [Schönhage et al. 1994]، فإن استخدام البيانات حول أي الخوارزميات تعمل بشكل أفضل على الحواسيب الكلاسيكية قد يكون مضللاً لسببين: أولاً، الحواسيب الكلاسيكية لا يلزم أن تكون قابلة للعكس، وتكلفة جعل خوارزمية قابلة للعكس تعتمد على الخوارزمية. ثانياً، الحواسيب الموجودة عموماً لديها ضرب لأرقام 32 أو 64 بت مدمج في عتادها، وهذا سيزيد نقاط التبديل الأمثل إلى خوارزميات أسرع تقاربياً؛ علاوة على ذلك، بعض خوارزميات الضرب يمكن أن تستفيد بشكل أفضل من هذا الضرب المدمج من غيرها. وبالتالي، من أجل برمجة الحواسيب الكمومية بكفاءة أكبر، يجب القيام بعمل على أفضل طريقة لتنفيذ العمليات الحسابية الأساسية على الحواسيب الكمومية. حقيقة واحدة مثيرة هي أن خوارزمية الضرب السريع Schönhage-Strassen تستخدم تحويل فورييه السريع، وهو أيضاً الأساس لجميع الخوارزميات السريعة على الحواسيب الكمومية المكتشفة حتى الآن؛ من المغري التكهن بأن ضرب الأعداد الصحيحة نفسه قد يتم تسريعه بواسطة خوارزمية كمومية؛ إذا كان ذلك ممكناً، فإن هذا سيؤدي إلى حد تقاربي أسرع إلى حد ما للتحليل إلى عوامل على حاسوب كمومي، وفي الواقع يمكن أن يجعل كسر RSA على حاسوب كمومي أسرع تقاربياً من التشفير بـ RSA على حاسوب كلاسيكي.

---

### Translation Notes

- **Key terms introduced:**
  - Reversible computation (حوسبة قابلة للعكس)
  - Thermodynamically irreversible (غير قابل للعكس ترموديناميكياً)
  - Toffoli gate (بوابة توفولي)
  - Fredkin gate (بوابة فريدكين)
  - Modular exponentiation (الأس النمطي)
  - Bennett's method (طريقة بينيت)
  - Quantum Zeno effect (تأثير زينو الكمومي)
  - Schönhage–Strassen algorithm (خوارزمية Schönhage-Strassen)

- **Tables:** 2 (Table 3.1 - Toffoli and Fredkin gates truth tables, Table 3.2 - Bennett's method)
- **Pseudocode:** 4 code blocks
- **Complexity notations:** Extensive use of O-notation for time and space complexity

- **Special handling:**
  - Pseudocode blocks preserved in original form
  - Mathematical complexity notation preserved
  - Discussion of classical vs. quantum computation trade-offs
  - Detailed algorithmic descriptions maintained

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86

### Back-Translation (Opening Paragraph)

The definition of quantum gate arrays leads to completely reversible computation. That is, knowing the quantum state on the wires exiting from a gate tells us uniquely what the quantum state must have been on the wires entering that gate. This is a reflection of the fact that, despite the macroscopic arrow of time, the laws of physics appear to be completely reversible. This might seem to imply that anything built with the laws of physics must be completely reversible; however, classical computers overcome this fact by dissipating energy and thus making their computations thermodynamically irreversible. This appears impossible to do for quantum computers because superpositions of quantum states must be maintained throughout the computation. Therefore, quantum computers must necessarily use reversible computation. This imposes additional costs when performing classical computations on a quantum computer, as is sometimes necessary in subroutines of quantum computations.

**Validation:** Back-translation preserves the technical reasoning and physical concepts. Quality maintained at 0.86/1.0.
