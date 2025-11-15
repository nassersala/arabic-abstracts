# Section 8: Shannon's Source Coding Theorem
## القسم 8: نظرية ترميز المصدر لشانون

**Section:** source-coding-theorem
**Translation Quality:** 0.87
**Glossary Terms Used:** source coding theorem, entropy, channel capacity, encoding, binary digits

---

### English Version

Shannon's source coding theorem, described below, applies only to noiseless channels. This theorem is really about re-packaging (encoding) data before it is transmitted, so that, when it is transmitted, every datum conveys as much information as possible. This theorem is highly relevant to the biological information processing because it defines definite limits to how efficiently sensory data can be re-packaged. We consider the source coding theorem using binary digits below, but the logic of the argument applies equally well to any channel inputs.

Given that a binary digit can convey a maximum of one bit of information, a noiseless channel which communicates $R$ binary digits per second can communicate information at the rate of up to $R$ bits/s. Because the capacity $C$ is the maximum rate at which it can communicate information from input to output, it follows that the capacity of a noiseless channel is numerically equal to the number $R$ of binary digits communicated per second. However, if each binary digit carries less than one bit (e.g. if consecutive output values are correlated) then the channel communicates information at a lower rate $R < C$.

Now that we are familiar with the core concepts of information theory, we can quote Shannon's source coding theorem in full. This is also known as Shannon's fundamental theorem for a discrete noiseless channel, and as the first fundamental coding theorem.

> Let a source have entropy $H$ (bits per symbol) and a channel have a capacity $C$ (bits per second). Then it is possible to encode the output of the source in such a way as to transmit at the average rate $C/H - \epsilon$ symbols per second over the channel where $\epsilon$ is arbitrarily small. It is not possible to transmit at an average rate greater than $C/H$ [symbols/s].
>
> Shannon and Weaver, 1949[2].
> [Text in square brackets has been added by the author.]

Recalling the example of the sum of two dice, a naive encoding would require 3.46 ($\log 11$) binary digits to represent the sum of each throw. However, Shannon's source coding theorem guarantees that an encoding exists such that an average of (just over) 3.27 (i.e. $\log 9.65$) binary digits per value of $s$ will suffice (the phrase 'just over' is an informal interpretation of Shannon's more precise phrase 'arbitrarily close to').

This encoding process yields inputs with a specific distribution $p(x)$, where there are implicit constraints on the form of $p(x)$ (e.g. power constraints). The shape of the distribution $p(x)$ places an upper limit on the entropy $H(x)$, and therefore on the maximum information that each input can carry. Thus, the capacity of a noiseless channel is defined in terms of the particular distribution $p(x)$ which maximises the amount of information per input

$$C = \max_{p(x)} H(x) \text{ bits per input.}$$ (10)

This states that channel capacity $C$ is achieved by the distribution $p(x)$ which makes $H(x)$ as large as possible (see Section 6).

---

### النسخة العربية

نظرية ترميز المصدر لشانون، الموصوفة أدناه، تنطبق فقط على القنوات الخالية من الضوضاء. هذه النظرية تتعلق حقاً بإعادة تعبئة (ترميز) البيانات قبل نقلها، بحيث عند نقلها، ينقل كل بيان أكبر قدر ممكن من المعلومات. هذه النظرية ذات صلة كبيرة بمعالجة المعلومات البيولوجية لأنها تحدد حدوداً واضحة لمدى كفاءة إعادة تعبئة البيانات الحسية. نعتبر نظرية ترميز المصدر باستخدام الأرقام الثنائية أدناه، ولكن منطق الحجة ينطبق بشكل متساوٍ على أي مدخلات قناة.

بالنظر إلى أن رقماً ثنائياً يمكن أن ينقل حداً أقصى من بتة واحدة من المعلومات، فإن قناة خالية من الضوضاء تنقل $R$ رقماً ثنائياً في الثانية يمكنها نقل معلومات بمعدل يصل إلى $R$ بتة/ث. نظراً لأن السعة $C$ هي المعدل الأقصى الذي يمكنها به نقل المعلومات من الدخل إلى الخرج، يتبع أن سعة قناة خالية من الضوضاء تساوي عددياً العدد $R$ من الأرقام الثنائية المنقولة في الثانية. ومع ذلك، إذا كان كل رقم ثنائي يحمل أقل من بتة واحدة (على سبيل المثال إذا كانت قيم الخرج المتتالية مترابطة) فإن القناة تنقل معلومات بمعدل أقل $R < C$.

الآن بعد أن أصبحنا على دراية بالمفاهيم الأساسية لنظرية المعلومات، يمكننا اقتباس نظرية ترميز المصدر لشانون بالكامل. يُعرف هذا أيضاً باسم النظرية الأساسية لشانون لقناة منفصلة خالية من الضوضاء، وباسم نظرية الترميز الأساسية الأولى.

> لتكن للمصدر إنتروبيا $H$ (بتات لكل رمز) وللقناة سعة $C$ (بتات في الثانية). عندئذ من الممكن ترميز خرج المصدر بطريقة تنقل بمعدل متوسط $C/H - \epsilon$ رمزاً في الثانية عبر القناة حيث $\epsilon$ صغير بشكل تعسفي. ليس من الممكن النقل بمعدل متوسط أكبر من $C/H$ [رموز/ث].
>
> شانون وويفر، 1949[2].
> [تم إضافة النص بين الأقواس المربعة من قبل المؤلف.]

باستذكار مثال مجموع نردين، فإن ترميزاً ساذجاً سيتطلب 3.46 ($\log 11$) رقماً ثنائياً لتمثيل مجموع كل رمية. ومع ذلك، تضمن نظرية ترميز المصدر لشانون أن ترميزاً موجود بحيث يكفي متوسط (أكثر قليلاً من) 3.27 (أي $\log 9.65$) رقماً ثنائياً لكل قيمة من $s$ (عبارة 'أكثر قليلاً' هي تفسير غير رسمي لعبارة شانون الأكثر دقة 'قريب بشكل تعسفي').

تنتج عملية الترميز هذه مدخلات بتوزيع محدد $p(x)$، حيث توجد قيود ضمنية على شكل $p(x)$ (مثل قيود الطاقة). يضع شكل التوزيع $p(x)$ حداً أعلى على الإنتروبيا $H(x)$، وبالتالي على الحد الأقصى للمعلومات التي يمكن لكل دخل حملها. وبالتالي، يتم تعريف سعة قناة خالية من الضوضاء من حيث التوزيع المحدد $p(x)$ الذي يزيد من كمية المعلومات لكل دخل

$$C = \max_{p(x)} H(x) \text{ بتات لكل دخل.}$$ (10)

ينص هذا على أن سعة القناة $C$ تتحقق بواسطة التوزيع $p(x)$ الذي يجعل $H(x)$ كبيرة قدر الإمكان (انظر القسم 6).

---

### Quality Metrics
- **Overall section score:** 0.87
