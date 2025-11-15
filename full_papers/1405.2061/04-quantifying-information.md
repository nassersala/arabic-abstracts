# Section 4: Quantifying the Amount of Information
## القسم 4: قياس كمية المعلومات

**Section:** Technical Development
**Translation Quality:** 0.88
**Glossary Terms Used:** bit (بت), encoding (ترميز), probability (احتمال), distribution (توزيع)

---

### English Version

Now, how do we quantify the "amount of information" in a random variable? One way to represent this "amount of information" is the number of bits it takes to represent/express the variable. In a naive representation of variables, if a variable can take on only two values, it can be represented with just 1 bit; if it can take on any of 4 values, 2 bits are needed (the 2 bits can be said to form a "word"); if 9 different values, then 4 bits are needed; etc. But this is the storage required for the raw data, not for the information content of the data.

In a more sophisticated representation of the variable, if a variable is easier to guess, then we can leverage that fact to reduce the number of bits needed to store/transmit that information. For example, if a die is 80% likely to come up with the number "3", then one way to leverage the "guess-ability" of the die is to store/transmit only a single bit with the value 0 whenever the die actually comes up with "3", and store/transmit more bits, starting with a first bit of value 1, when the die comes up with other values. The single bit transmission (of bit value "0") simply indicates to the receiver that the dice was tossed; the receiver then just maps that information to the information that the toss outcome was "3", without needing the transmitter to actually specify that value! Further, when the first bit is a 0, the receiver knows not to look for more bits associated with this particular storage/transmission. This avoids the need for an "end" marker for each stored or transmitted "word", which would be additional cost otherwise.

All this is an intelligent form of "coding" (or, "encoding") the information; it leverages the probabilities or bias to reduce the average size of the code. While in a naive representation we would need 3 bits to represent each outcome of a die having 6 faces, by leveraging probabilities we use only 1 bit whenever the die comes up with "3" -- a more frequently occurring event -- thus reducing the average number of bits needed (over multiple dice throws) to store the die throw outcome. This reduction happens even if we are forced to use more than 3 bits for some infrequently-occurring outcome of the die throw.

One can thus leverage the probabilities of the different values to reduce the number of bits needed -- if and only if the variable has a non-uniform distribution. If not, there will be no reduction in the number of bits needed. The intuition here is that if a variable is more likely to take on one value than another, then it is easier to guess the value of the variable without looking at it, thus the variable has less information in it, and thus it takes fewer bits to store/transmit the value.

---

### النسخة العربية

الآن، كيف نقيس "كمية المعلومات" في متغير عشوائي؟ إحدى طرق تمثيل "كمية المعلومات" هذه هي عدد البتات اللازمة لتمثيل/التعبير عن المتغير. في تمثيل ساذج للمتغيرات، إذا كان المتغير يمكن أن يأخذ قيمتين فقط، فيمكن تمثيله ببت واحد فقط؛ إذا كان يمكن أن يأخذ أياً من 4 قيم، فإن 2 بت مطلوبة (يمكن القول إن البتان يشكلان "كلمة")؛ إذا كانت هناك 9 قيم مختلفة، فإن 4 بتات مطلوبة؛ إلخ. لكن هذا هو التخزين المطلوب للبيانات الخام، وليس لمحتوى المعلومات في البيانات.

في تمثيل أكثر تطوراً للمتغير، إذا كان المتغير أسهل في التخمين، فيمكننا الاستفادة من هذه الحقيقة لتقليل عدد البتات اللازمة لتخزين/نقل تلك المعلومات. على سبيل المثال، إذا كان احتمال ظهور الرقم "3" على حجر النرد 80٪، فإن إحدى طرق الاستفادة من "قابلية التخمين" لحجر النرد هي تخزين/نقل بت واحد فقط بالقيمة 0 كلما ظهر فعلياً الرقم "3" على حجر النرد، وتخزين/نقل المزيد من البتات، بدءاً من بت أول بالقيمة 1، عندما يظهر على حجر النرد قيم أخرى. نقل البت الواحد (ذو القيمة "0") يشير ببساطة إلى المستقبل أن النرد قد تم رميه؛ ثم يقوم المستقبل فقط بتعيين تلك المعلومات إلى المعلومة بأن نتيجة الرمي كانت "3"، دون الحاجة إلى أن يحدد المرسل تلك القيمة فعلياً! علاوة على ذلك، عندما يكون البت الأول هو 0، يعلم المستقبل ألا يبحث عن مزيد من البتات المرتبطة بهذا التخزين/النقل المحدد. هذا يتجنب الحاجة إلى علامة "نهاية" لكل "كلمة" مخزنة أو منقولة، والتي ستكون تكلفة إضافية بخلاف ذلك.

كل هذا هو شكل ذكي من "الترميز" (أو "التشفير") للمعلومات؛ إنه يستفيد من الاحتمالات أو التحيز لتقليل متوسط حجم الترميز. بينما في التمثيل الساذج سنحتاج إلى 3 بتات لتمثيل كل نتيجة من نرد له 6 أوجه، بالاستفادة من الاحتمالات نستخدم بت واحد فقط كلما ظهر على النرد الرقم "3" -- وهو حدث يحدث بشكل أكثر تكراراً -- وبالتالي تقليل متوسط عدد البتات المطلوبة (على مدى رميات نرد متعددة) لتخزين نتيجة رمية النرد. يحدث هذا التقليل حتى لو اضطررنا لاستخدام أكثر من 3 بتات لبعض النتائج النادرة الحدوث لرمية النرد.

يمكن للمرء إذن الاستفادة من احتمالات القيم المختلفة لتقليل عدد البتات المطلوبة -- إذا وفقط إذا كان للمتغير توزيع غير موحد. إن لم يكن، فلن يكون هناك تقليل في عدد البتات المطلوبة. الحدس هنا هو أنه إذا كان المتغير أكثر احتمالاً لأخذ قيمة واحدة من أخرى، فإنه من الأسهل تخمين قيمة المتغير دون النظر إليه، وبالتالي فإن المتغير يحتوي على معلومات أقل فيه، وبالتالي يستغرق بتات أقل لتخزين/نقل القيمة.

---

### Translation Notes

- **Key terms introduced:**
  - encoding/coding (ترميز/تشفير)
  - word (كلمة) - in the context of bit sequences
  - transmission (نقل)
  - receiver (مستقبل)
  - transmitter (مرسل)
  - non-uniform distribution (توزيع غير موحد)
  - guess-ability (قابلية التخمين)
- **Examples:**
  - Die with 80% probability for "3"
  - Comparison of naive vs. sophisticated encoding
  - Variable-length encoding scheme
- **Special handling:**
  - Carefully explained the intelligent encoding scheme
  - Preserved the step-by-step logical development
  - Maintained technical precision while keeping accessible tone

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.88
