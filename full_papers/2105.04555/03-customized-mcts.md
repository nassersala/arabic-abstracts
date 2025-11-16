# Section 3: Customized MCTS for Autotuning Loop Transformation Pragmas
## القسم 3: MCTS المخصص للضبط التلقائي لتوجيهات pragma لتحويل الحلقات

**Section:** methodology
**Translation Quality:** 0.86
**Glossary Terms Used:** MCTS, autotuning, reward function, exploration, exploitation, moving average, random walk, restart mechanism, transfer learning, quantile, reinforcement

---

### English Version

Although MCTS is designed to explore the treelike search space, the vanilla version cannot be applied directly to our autotuning problem. First, there is no concept of playing a game for optimizing loop transformation directives. While the reward is trivial in a game setting with a win or loss, MCTS for autotuning problems requires careful reward engineering. Second, the vanilla MCTS is not efficient if a good solution, a high-performing configuration in our case, is located deep in the tree. Assume that we have a kernel where there are numerous configurations with one directive located at the first depth of the tree. However, the best configuration requires more than one directive. As the pure MCTS expands a node one by one from the root, it requires many iterations to reach the best configuration located deep in the tree. Third, there is no limit on the number of loop transformations to form a configuration (node), which means a terminal node is unknown. In this case the algorithm needs to determine when to stop to form a configuration. Fourth, the vanilla MCTS can end up with a poor local solution.

To circumvent these issues, we developed a customized MCTS for autotuning loop transformation pragmas. Our method consists of two phases: random exploration of configurations at different depths to find promising regions, followed by targeted exploitation of the promising regions. A restart strategy is applied to MCTS to avoid being stuck in a local solution. MCTS repeats the exploration and exploitation after each restart so that configurations at different depths can be searched. Moreover, it leverages the search history after the restart by transferring the high- and low-performing configurations for reinforcement.

**3.1 Moving average reward function**

We design our reward function such that an evaluated configuration (sequence of pragams applied to the unoptimized code) at each iteration leads to a win and a loss. To this end, we introduce a utility function that measures the performance of the configuration and a target function $T$ to determine a win or a loss over its performance. We use the utility function that computes the speedup of a configuration $c$ over an unoptimized code located on the root $c_0$.

The target is computed by using the $m$-moving average, defined as follows:

$$U_c = \frac{\text{execution time of } c_0}{\text{execution time of } c}$$

$$T_c(m) = \text{movavg}(T_{c-1}, \frac{1}{m}\sum_{i=c-m+1}^{c}U_i)$$

at iteration $c$, and the reward function is

$$r_c = \begin{cases}
r_{\text{penalty}} & \text{if } \neg c \\
1 & \text{if } U_c > T_c \\
0 & \text{otherwise}
\end{cases}$$

where $\neg c$ denotes a failure program rejected by the compiler and $r_{\text{penalty}}$ is a negative constant. This reward function progressively increases the ability of MCTS to find configurations whose performances are better than the average performances of the last $m$ configurations.

**3.2 Random walk to learn depth**

Since the depth of the tree is unbounded, MCTS cannot stop at a terminal node in a given iteration. Therefore, learning at what depth to stop is an additional complexity that we have to address in dealing with the autotuning problem.

To that end, we incorporate a random walk search within MCTS to explore configurations at different depths and to find the best depth to terminate the search for each iteration. This is achieved as follows. First, we perform $n$ number of random walks each with randomly generated depth sampled uniformly between 1 and $d_{\max}$. Each random walk is a configuration that corresponds to a sequence of pragmas. We compute their performances by applying them on the unoptimized code and running them on the target hardware. The depth of the configuration with the best performance then is selected as the termination depth for MCTS. We use the random walk not only for learning the depth but also for exploration. The performance values from the evaluation are used to compute the reward and backpropagation.

**3.3 Restart mechanism to avoid getting stuck in a local solution**

Even though MCTS is known to find a relatively good solution, it can get trapped in a local solution [44]. Moreover, the random walk method to learn the depth can exacerbate this issue because the depth once fixed cannot be changed. Specifically, if the random walk did not find a good value for the depth, then MCTS is forced to search with that depth value.

To address these issues, we adopt a restart mechanism, where we detect the convergence to a local solution and restart MCTS with a new random walk. This cycle repeats until a computational budget is exhausted. The convergence of the search is identified if there is no improvement in the target value or the algorithm terminates at the same configuration for more than a threshold.

Since the restart mechanism erases the memory of the MCTS, it cannot leverage what it has seen in the past. To avoid this issue, we transfer information from the search history as soon as a new restart is performed. At each restart, we consider all the configurations evaluated by the MCTS by speedup with respect to the evaluated code. We compute lower and upper quantiles of the speedup distribution given by $q\%$ and $100-q\%$, where $q$ is a user-defined parameter. For example, when $q$ is set to 5, the lower and upper quantiles are 5% and 95%, respectively. We take configurations with speedup above $100-q\%$ and reinforce the path with the positive reward. Similarly, we take the configurations with speedup below $q\%$ and reinforce the path with the negative reward. It is not guaranteed that all of the pragmas from the lower quantile lead to poor performance. For example, a good pragma can be included in both lower and upper quantiles. Therefore, we penalize the lower quantile configurations that do not share any common pragmas with the configurations that belong to the upper quantile.

**Algorithm 1: Customized MCTS**

```
Input: d_max, budgets for search, convergence settings, and q
while stopping criterion not met do
    while no convergence is detected do
        d ← RandomWalk(d_max)
        Transfer(q)
        c ← MCTS(d)
    end while
end while
```

Algorithm 1 shows the pseudo-code of the customized MCTS method. The outer while loop (lines 2–8) runs until the stopping criterion is met. Typically, this is a wall-clock time or a total number of evaluations allowed. The inner while loop (lines 3–7) comprises a random walk to find the depth $d$ (RandomWalk($d_{\max}$)), transfer of configurations from lower and upper quantiles for negative and positive reinforcement (Transfer($q$)), and MCTS with the depth $d$ (MCTS($d$)). Note that the transfer and the random walk are independent of each other and the order in which they are performed does not matter.

---

### النسخة العربية

على الرغم من أن MCTS مصمم لاستكشاف فضاء البحث الشجري، إلا أن الإصدار الأساسي لا يمكن تطبيقه مباشرة على مشكلة الضبط التلقائي الخاصة بنا. أولاً، لا يوجد مفهوم للعب لعبة لتحسين توجيهات تحويل الحلقات. بينما تكون المكافأة بسيطة في إعداد لعبة بفوز أو خسارة، يتطلب MCTS لمشاكل الضبط التلقائي هندسة مكافأة دقيقة. ثانياً، MCTS الأساسي ليس فعالاً إذا كان الحل الجيد، وهو تكوين عالي الأداء في حالتنا، موجوداً في عمق الشجرة. افترض أن لدينا نواة حيث توجد تكوينات عديدة بتوجيه واحد موجودة في العمق الأول من الشجرة. ومع ذلك، يتطلب التكوين الأفضل أكثر من توجيه واحد. بما أن MCTS النقي يوسع عقدة واحدة تلو الأخرى من الجذر، فإنه يتطلب العديد من التكرارات للوصول إلى التكوين الأفضل الموجود في عمق الشجرة. ثالثاً، لا يوجد حد لعدد تحويلات الحلقات لتكوين تكوين (عقدة)، مما يعني أن العقدة الطرفية غير معروفة. في هذه الحالة يحتاج الخوارزمية إلى تحديد متى تتوقف لتكوين تكوين. رابعاً، يمكن أن ينتهي MCTS الأساسي بحل محلي ضعيف.

للتحايل على هذه المشاكل، طورنا MCTS مخصصاً للضبط التلقائي لتوجيهات pragma لتحويل الحلقات. تتكون طريقتنا من مرحلتين: استكشاف عشوائي للتكوينات على أعماق مختلفة لإيجاد مناطق واعدة، يليه استغلال موجه للمناطق الواعدة. يتم تطبيق استراتيجية إعادة تشغيل على MCTS لتجنب الانحصار في حل محلي. يكرر MCTS الاستكشاف والاستغلال بعد كل إعادة تشغيل بحيث يمكن البحث في التكوينات على أعماق مختلفة. علاوة على ذلك، يستفيد من تاريخ البحث بعد إعادة التشغيل من خلال نقل التكوينات عالية ومنخفضة الأداء للتعزيز.

**3.1 دالة مكافأة المتوسط المتحرك**

نصمم دالة المكافأة الخاصة بنا بحيث يؤدي تكوين مُقيَّم (تسلسل من pragmas مطبق على الشفرة غير المحسنة) في كل تكرار إلى فوز وخسارة. لهذه الغاية، نقدم دالة منفعة تقيس أداء التكوين ودالة هدف $T$ لتحديد فوز أو خسارة على أدائه. نستخدم دالة المنفعة التي تحسب تسريع تكوين $c$ على شفرة غير محسنة موجودة على الجذر $c_0$.

يتم حساب الهدف باستخدام المتوسط المتحرك $m$، المعرف على النحو التالي:

$$U_c = \frac{\text{وقت تنفيذ } c_0}{\text{وقت تنفيذ } c}$$

$$T_c(m) = \text{movavg}(T_{c-1}, \frac{1}{m}\sum_{i=c-m+1}^{c}U_i)$$

في التكرار $c$، ودالة المكافأة هي

$$r_c = \begin{cases}
r_{\text{penalty}} & \text{إذا } \neg c \\
1 & \text{إذا } U_c > T_c \\
0 & \text{خلاف ذلك}
\end{cases}$$

حيث $\neg c$ يشير إلى برنامج فاشل رفضه المترجم و$r_{\text{penalty}}$ ثابت سالب. تزيد دالة المكافأة هذه تدريجياً من قدرة MCTS على إيجاد تكوينات تكون أداءاتها أفضل من متوسط أداءات آخر $m$ تكوينات.

**3.2 سير عشوائي لتعلم العمق**

بما أن عمق الشجرة غير محدود، لا يمكن لـ MCTS التوقف عند عقدة طرفية في تكرار معين. لذلك، فإن تعلم العمق الذي يجب التوقف عنده هو تعقيد إضافي يجب علينا معالجته في التعامل مع مشكلة الضبط التلقائي.

لهذه الغاية، ندمج بحث سير عشوائي ضمن MCTS لاستكشاف التكوينات على أعماق مختلفة ولإيجاد أفضل عمق لإنهاء البحث لكل تكرار. يتم تحقيق ذلك على النحو التالي. أولاً، ننفذ $n$ عدداً من السيرات العشوائية كل منها بعمق مُولَّد عشوائياً تم أخذ عينات منه بشكل موحد بين 1 و$d_{\max}$. كل سير عشوائي هو تكوين يتوافق مع تسلسل من pragmas. نحسب أداءاتها من خلال تطبيقها على الشفرة غير المحسنة وتشغيلها على العتاد المستهدف. يتم بعد ذلك اختيار عمق التكوين ذي الأداء الأفضل كعمق إنهاء لـ MCTS. نستخدم السير العشوائي ليس فقط لتعلم العمق ولكن أيضاً للاستكشاف. تُستخدم قيم الأداء من التقييم لحساب المكافأة والانتشار العكسي.

**3.3 آلية إعادة التشغيل لتجنب الانحصار في حل محلي**

على الرغم من أن MCTS معروف بإيجاد حل جيد نسبياً، إلا أنه يمكن أن ينحصر في حل محلي [44]. علاوة على ذلك، يمكن أن تؤدي طريقة السير العشوائي لتعلم العمق إلى تفاقم هذه المشكلة لأن العمق بمجرد تثبيته لا يمكن تغييره. على وجه التحديد، إذا لم يجد السير العشوائي قيمة جيدة للعمق، فإن MCTS مجبر على البحث بقيمة العمق تلك.

لمعالجة هذه المشاكل، نتبنى آلية إعادة تشغيل، حيث نكتشف التقارب إلى حل محلي ونعيد تشغيل MCTS بسير عشوائي جديد. تتكرر هذه الدورة حتى نفاد الميزانية الحسابية. يتم تحديد تقارب البحث إذا لم يكن هناك تحسن في قيمة الهدف أو أن الخوارزمية تنتهي عند نفس التكوين لأكثر من عتبة.

بما أن آلية إعادة التشغيل تمحو ذاكرة MCTS، فإنها لا يمكنها الاستفادة مما رأته في الماضي. لتجنب هذه المشكلة، ننقل معلومات من تاريخ البحث بمجرد إجراء إعادة تشغيل جديدة. عند كل إعادة تشغيل، نأخذ في الاعتبار جميع التكوينات التي تم تقييمها بواسطة MCTS حسب التسريع فيما يتعلق بالشفرة المُقيَّمة. نحسب الشرائح الربعية السفلى والعليا لتوزيع التسريع المحددة بـ $q\%$ و$100-q\%$، حيث $q$ معامل محدد بواسطة المستخدم. على سبيل المثال، عندما يتم تعيين $q$ إلى 5، تكون الشرائح الربعية السفلى والعليا 5٪ و95٪، على التوالي. نأخذ التكوينات ذات التسريع فوق $100-q\%$ ونعزز المسار بالمكافأة الإيجابية. وبالمثل، نأخذ التكوينات ذات التسريع أدناه $q\%$ ونعزز المسار بالمكافأة السلبية. ليس من المضمون أن جميع pragmas من الشريحة الربعية السفلى تؤدي إلى أداء ضعيف. على سبيل المثال، يمكن تضمين pragma جيدة في كل من الشرائح الربعية السفلى والعليا. لذلك، نعاقب تكوينات الشريحة الربعية السفلى التي لا تشترك في أي pragmas مشتركة مع التكوينات التي تنتمي إلى الشريحة الربعية العليا.

**الخوارزمية 1: MCTS المخصص**

```
المدخلات: d_max، ميزانيات البحث، إعدادات التقارب، وq
while لم يتم استيفاء معيار التوقف do
    while لم يتم اكتشاف تقارب do
        d ← RandomWalk(d_max)
        Transfer(q)
        c ← MCTS(d)
    end while
end while
```

تُظهر الخوارزمية 1 الشفرة الزائفة لطريقة MCTS المخصصة. تعمل حلقة while الخارجية (الأسطر 2-8) حتى يتم استيفاء معيار التوقف. عادة، هذا وقت حائط أو إجمالي عدد التقييمات المسموح بها. تتضمن حلقة while الداخلية (الأسطر 3-7) سيراً عشوائياً لإيجاد العمق $d$ (RandomWalk($d_{\max}$))، ونقل التكوينات من الشرائح الربعية السفلى والعليا للتعزيز السلبي والإيجابي (Transfer($q$))، و MCTS بالعمق $d$ (MCTS($d$)). لاحظ أن النقل والسير العشوائي مستقلان عن بعضهما البعض والترتيب الذي يتم تنفيذهما فيه لا يهم.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:** moving average, utility function, target function, random walk, restart mechanism, transfer learning, quantile, reinforcement
- **Equations:** 3 (utility function, target function, reward function)
- **Algorithms:** Algorithm 1 (Customized MCTS pseudo-code)
- **Citations:** [44]
- **Special handling:**
  - Mathematical formulas kept in LaTeX with Arabic explanations
  - Algorithm pseudo-code kept in English structure with Arabic annotations
  - Technical parameters: $m$ (moving average window), $n$ (number of random walks), $d_{\max}$ (maximum depth), $q$ (quantile parameter)

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86
