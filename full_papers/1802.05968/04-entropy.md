# Section 4: Information and Entropy
## القسم 4: المعلومات والإنتروبيا

**Section:** core-theory
**Translation Quality:** 0.88
**Glossary Terms Used:** entropy, Shannon information, surprisal, random variable, probability distribution

---

### English Version

Consider a coin which lands heads up 90% of the time (i.e. $p(x_h) = 0.9$). When this coin is flipped, we expect it to land heads up ($x = x_h$), so when it does so we are less surprised than when it lands tails up ($x = x_t$). The more improbable a particular outcome is, the more surprised we are to observe it. If we use logarithms to the base 2 then the Shannon information or surprisal of each outcome is measured in bits (see Figure 3a)

$$\text{Shannon information} = \log \frac{1}{p(x_h)} \text{ bits,}$$ (1)

which is often expressed as: information = $-\log p(x_h)$ bits.

**Entropy is Average Shannon Information.** We can represent the outcome of a coin flip as the random variable $x$, such that a head is $x = x_h$ and a tail is $x = x_t$. In practice, we are not usually interested in the surprise of a particular value of a random variable, but we are interested in how much surprise, on average, is associated with the entire set of possible values. The average surprise of a variable $x$ is defined by its probability distribution $p(x)$, and is called the entropy of $p(x)$, represented as $H(x)$.

**The Entropy of a Fair Coin.** The average amount of surprise about the possible outcomes of a coin flip can be found as follows. If a coin is fair or unbiased then $p(x_h) = p(x_t) = 0.5$ then the Shannon information gained when a head or a tail is observed is $\log 1/0.5 = 1$ bit, so the average Shannon information gained after each coin flip is also 1 bit. Because entropy is defined as average Shannon information, the entropy of a fair coin is $H(x) = 1$ bit.

**The Entropy of an Unfair (Biased) Coin.** If a coin is biased such that the probability of a head is $p(x_h) = 0.9$ then it is easy to predict the result of each coin flip (i.e. with 90% accuracy if we predict a head for each flip). If the outcome is a head then the amount of Shannon information gained is $\log(1/0.9) = 0.15$ bits. But if the outcome is a tail then the amount of Shannon information gained is $\log(1/0.1) = 3.32$ bits. Notice that more information is associated with the more surprising outcome. Given that the proportion of flips that yield a head is $p(x_h)$, and that the proportion of flips that yield a tail is $p(x_t)$ (where $p(x_h) + p(x_t) = 1$), the average surprise is

$$H(x) = p(x_h) \log \frac{1}{p(x_h)} + p(x_t) \log \frac{1}{p(x_t)},$$  (2)

which comes to $H(x) = 0.469$ bits, as in Figure 3b. If we define a tail as $x_1 = x_t$ and a head as $x_2 = x_h$ then Equation 2 can be written as

$$H(x) = \sum_{i=1}^{2} p(x_i) \log \frac{1}{p(x_i)} \text{ bits.}$$ (3)

More generally, a random variable $x$ with a probability distribution $p(x) = \{p(x_1), \ldots, p(x_m)\}$ has an entropy of

$$H(x) = \sum_{i=1}^{m} p(x_i) \log \frac{1}{p(x_i)} \text{ bits.}$$ (4)

The reason this definition matters is because Shannon's source coding theorem (see Section 7) guarantees that each value of the variable $x$ can be represented with an average of (just over) $H(x)$ binary digits. However, if the values of consecutive values of a random variable are not independent then each value is more predictable, and therefore less surprising, which reduces the information-carrying capability (i.e. entropy) of the variable. This is why it is important to specify whether or not consecutive variable values are independent.

**Interpreting Entropy.** If $H(x) = 1$ bit then the variable $x$ could be used to represent $m = 2^{H(x)}$ or 2 equiprobable values. Similarly, if $H(x) = 0.469$ bits then the variable $x$ could be used to represent $m = 2^{0.469}$ or 1.38 equiprobable values; as if we had a die with 1.38 sides. At first sight, this seems like an odd statement. Nevertheless, translating entropy into an equivalent number of equiprobable values serves as an intuitive guide for the amount of information represented by a variable.

**Dicing With Entropy.** [Content continues with dice example, Table 1, etc.]

**Entropy and Uncertainty.** Entropy is a measure of uncertainty. When our uncertainty is reduced, we gain information, so information and entropy are two sides of the same coin. However, information has a rather subtle interpretation, which can easily lead to confusion.

Average information shares the same definition as entropy, but whether we call a given quantity information or entropy depends on whether it is being given to us or taken away. For example, if a variable has high entropy then our initial uncertainty about the value of that variable is large and is, by definition, exactly equal to its entropy. If we are told the value of that variable then, on average, we have been given information equal to the uncertainty (entropy) we had about its value. Thus, receiving an amount of information is equivalent to having exactly the same amount of entropy (uncertainty) taken away.

---

### النسخة العربية

فكر في عملة تهبط على الوجه في 90% من الوقت (أي $p(x_h) = 0.9$). عندما يتم قذف هذه العملة، نتوقع أن تهبط على الوجه ($x = x_h$)، لذلك عندما تفعل ذلك نكون أقل مفاجأة مما لو هبطت على الكتابة ($x = x_t$). كلما كانت نتيجة معينة أقل احتمالاً، زادت مفاجأتنا بملاحظتها. إذا استخدمنا اللوغاريتمات للأساس 2 فإن معلومات شانون أو المفاجأة لكل نتيجة تُقاس بالبتات (انظر الشكل 3أ)

$$\text{معلومات شانون} = \log \frac{1}{p(x_h)} \text{ بتات،}$$ (1)

والتي غالباً ما تُعبر على النحو التالي: المعلومات = $-\log p(x_h)$ بتات.

**الإنتروبيا هي متوسط معلومات شانون.** يمكننا تمثيل نتيجة قذف عملة كمتغير عشوائي $x$، بحيث يكون الوجه هو $x = x_h$ والكتابة هي $x = x_t$. في الممارسة العملية، لسنا مهتمين عادة بمفاجأة قيمة معينة لمتغير عشوائي، ولكننا مهتمون بمقدار المفاجأة، في المتوسط، المرتبطة بمجموعة القيم المحتملة بأكملها. يتم تعريف متوسط المفاجأة لمتغير $x$ بواسطة توزيع احتماله $p(x)$، ويُسمى إنتروبيا $p(x)$، ويُمثل بـ $H(x)$.

**إنتروبيا العملة العادلة.** يمكن إيجاد متوسط كمية المفاجأة حول النتائج المحتملة لقذف عملة على النحو التالي. إذا كانت العملة عادلة أو غير متحيزة حيث $p(x_h) = p(x_t) = 0.5$ فإن معلومات شانون المكتسبة عند ملاحظة وجه أو كتابة هي $\log 1/0.5 = 1$ بتة، لذلك متوسط معلومات شانون المكتسبة بعد كل قذف للعملة هو أيضاً 1 بتة. نظراً لأن الإنتروبيا معرفة كمتوسط معلومات شانون، فإن إنتروبيا العملة العادلة هي $H(x) = 1$ بتة.

**إنتروبيا العملة غير العادلة (المتحيزة).** إذا كانت العملة متحيزة بحيث يكون احتمال الوجه $p(x_h) = 0.9$ فمن السهل التنبؤ بنتيجة كل قذف للعملة (أي بدقة 90% إذا تنبأنا بوجه لكل قذف). إذا كانت النتيجة وجهاً فإن كمية معلومات شانون المكتسبة هي $\log(1/0.9) = 0.15$ بتة. ولكن إذا كانت النتيجة كتابة فإن كمية معلومات شانون المكتسبة هي $\log(1/0.1) = 3.32$ بتة. لاحظ أن معلومات أكثر ترتبط بالنتيجة الأكثر مفاجأة. بالنظر إلى أن نسبة القذفات التي تعطي وجهاً هي $p(x_h)$، وأن نسبة القذفات التي تعطي كتابة هي $p(x_t)$ (حيث $p(x_h) + p(x_t) = 1$)، فإن متوسط المفاجأة هو

$$H(x) = p(x_h) \log \frac{1}{p(x_h)} + p(x_t) \log \frac{1}{p(x_t)},$$  (2)

والذي يصل إلى $H(x) = 0.469$ بتة، كما في الشكل 3ب. إذا عرّفنا كتابة كـ $x_1 = x_t$ ووجه كـ $x_2 = x_h$ فيمكن كتابة المعادلة 2 على النحو التالي

$$H(x) = \sum_{i=1}^{2} p(x_i) \log \frac{1}{p(x_i)} \text{ بتات.}$$ (3)

بشكل أكثر عمومية، المتغير العشوائي $x$ بتوزيع احتمال $p(x) = \{p(x_1), \ldots, p(x_m)\}$ له إنتروبيا

$$H(x) = \sum_{i=1}^{m} p(x_i) \log \frac{1}{p(x_i)} \text{ بتات.}$$ (4)

السبب في أهمية هذا التعريف هو أن نظرية ترميز المصدر لشانون (انظر القسم 7) تضمن أن كل قيمة من قيم المتغير $x$ يمكن تمثيلها بمتوسط (أكثر قليلاً من) $H(x)$ رقم ثنائي. ومع ذلك، إذا لم تكن قيم القيم المتتالية لمتغير عشوائي مستقلة فإن كل قيمة تكون أكثر قابلية للتنبؤ، وبالتالي أقل مفاجأة، مما يقلل من القدرة على حمل المعلومات (أي الإنتروبيا) للمتغير. لهذا السبب من المهم تحديد ما إذا كانت قيم المتغير المتتالية مستقلة أم لا.

**تفسير الإنتروبيا.** إذا كان $H(x) = 1$ بتة فإن المتغير $x$ يمكن استخدامه لتمثيل $m = 2^{H(x)}$ أو 2 قيمة متساوية الاحتمال. بالمثل، إذا كان $H(x) = 0.469$ بتة فإن المتغير $x$ يمكن استخدامه لتمثيل $m = 2^{0.469}$ أو 1.38 قيمة متساوية الاحتمال؛ كما لو كان لدينا نرد بـ 1.38 وجه. للوهلة الأولى، يبدو هذا بياناً غريباً. ومع ذلك، فإن ترجمة الإنتروبيا إلى عدد مكافئ من القيم متساوية الاحتمال يعمل كدليل بديهي لكمية المعلومات الممثلة بواسطة متغير.

[محتوى مثال النرد والجدول 1 يتبع...]

**الإنتروبيا وعدم اليقين.** الإنتروبيا هي مقياس لعدم اليقين. عندما ينخفض عدم اليقين لدينا، نكتسب معلومات، لذلك المعلومات والإنتروبيا هما وجهان لعملة واحدة. ومع ذلك، فإن للمعلومات تفسيراً دقيقاً إلى حد ما، والذي يمكن أن يؤدي بسهولة إلى الارتباك.

يشارك متوسط المعلومات نفس التعريف كالإنتروبيا، ولكن ما إذا كنا نسمي كمية معينة معلومات أو إنتروبيا يعتمد على ما إذا كان يتم إعطاؤها لنا أو أخذها منا. على سبيل المثال، إذا كان لمتغير إنتروبيا عالية فإن عدم اليقين الأولي لدينا حول قيمة ذلك المتغير كبير ويكون، بحكم التعريف، مساوياً تماماً لإنتروبيته. إذا أُخبرنا بقيمة ذلك المتغير فإننا، في المتوسط، قد أُعطينا معلومات مساوية لعدم اليقين (الإنتروبيا) الذي كان لدينا حول قيمته. وبالتالي، فإن تلقي كمية من المعلومات يعادل أخذ نفس الكمية بالضبط من الإنتروبيا (عدم اليقين).

---

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
