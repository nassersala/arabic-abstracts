# Section 6: The Entropy Formula
## القسم 6: صيغة الإنتروبيا

**Section:** Mathematical Derivation
**Translation Quality:** 0.89
**Glossary Terms Used:** entropy (إنتروبيا), Shannon Entropy (إنتروبيا شانون), probability (احتمال), logarithm (لوغاريتم)

---

### English Version

Now, to understand the entropy formula, let us write down the three probabilities in the above example (section 5) for the occurrences of a, b, and c as follows:
 p(a) = 0.5  = 2/4
 p(b) = 0.25 = 1/4
 p(c) = 0.25 = 1/4

The key thing to notice here is that we have written p(a) as 2/4 and not 1/2, thus ensuring that all the three probabilities have the same denominator. Writing it this way leads us to an interpretation of the Entropy formula.

When p(x==c)=1/4 (i.e., p(c)), the numerator 1 and denominator 4 say that the value 'c' is taken on once in 4 times, which means there might be up to 3 other values that the variable can take on at other times (i.e., when it does not take on the value c). In which case, there are 4 values altogether and we will need the following number of bits to represent them all:
 log₂(4) = log₂(1/p) bits = 2 bits

So, 'c' will need 2 bits to be represented as distinct from those other values.

To represent the one 'b', we will similarly need log₂(4) = 2 bits.

For 'a', we can interpret p(a) = 2/4 as the value 'a' being taken on twice in four times. Or, we can now say that of the 4 values the variable can take on, two are 'a's, one is 'b', and one is 'c'. Now, to represent the two 'a's among the four values, we don't need two different storage representations, as the two 'a's are the same. So, from the overall number of bits required to represent the two 'a's of the variable, we can deduct log₂(2) bits, since presumably those log₂(2) bits were meant to differentiate the two 'a's which are actually identical. Thus, to represent 'a', we will need:
 log₂(4) – log₂(2) = 1 bit

Now, to determine the overall amount of storage required for the variable, we simply add up the above storage requirements (for the different individual values of the variable) in proportion to their frequencies of occurrence:
 'a' occurs half the time and needs 1 bit: 0.5*1
 'b' occurs a quarter of the time and needs 2 bits: 0.25*2
 'c' occurs a quarter of the time and needs 2 bits: 0.25*2
 In total, we need 0.5*1 + 0.25*2 + 0.25*2  = 1.5 bits

But, this is exactly Shannon's formula [1] for Entropy!
 Shannon Entropy  E = -∑ᵢ(p(i)×log₂(p(i)))

Note that the minus sign takes care of the fact that p(i) is a fraction. For example, for 'a',
 -p(a)×log₂(p(a)) = -{0.5*log₂(2/4)} = -{0.5*[log(2)–log(4)]} = +{0.5*[log(4)–log(2)]} = 0.5*1  !!

Thus, entropy is a direct measure of the number of bits needed to store the information in a variable, as opposed to its raw data. Thus, entropy is a direct measure of the "amount of information" in a variable.

---

### النسخة العربية

الآن، لفهم صيغة الإنتروبيا، دعونا نكتب الاحتمالات الثلاثة في المثال أعلاه (القسم 5) لحدوث a و b و c على النحو التالي:
 p(a) = 0.5  = 2/4
 p(b) = 0.25 = 1/4
 p(c) = 0.25 = 1/4

الشيء الأساسي الذي يجب ملاحظته هنا هو أننا كتبنا p(a) على أنها 2/4 وليس 1/2، وبالتالي ضمنا أن جميع الاحتمالات الثلاثة لها نفس المقام. كتابتها بهذه الطريقة تقودنا إلى تفسير صيغة الإنتروبيا.

عندما p(x==c)=1/4 (أي p(c))، فإن البسط 1 والمقام 4 يقولان أن القيمة 'c' تُأخذ مرة واحدة من كل 4 مرات، مما يعني أنه قد يكون هناك ما يصل إلى 3 قيم أخرى يمكن للمتغير أن يأخذها في أوقات أخرى (أي عندما لا يأخذ القيمة c). في هذه الحالة، هناك 4 قيم إجمالاً وسنحتاج إلى العدد التالي من البتات لتمثيلها جميعاً:
 log₂(4) = log₂(1/p) بتات = 2 بت

إذن، ستحتاج 'c' إلى 2 بت لتُمثل كمتميزة عن تلك القيم الأخرى.

لتمثيل 'b' الواحدة، سنحتاج بالمثل إلى log₂(4) = 2 بت.

بالنسبة لـ 'a'، يمكننا تفسير p(a) = 2/4 على أن القيمة 'a' تُأخذ مرتين من كل أربع مرات. أو، يمكننا الآن أن نقول أنه من بين القيم الأربع التي يمكن للمتغير أن يأخذها، اثنتان هما 'a'، وواحدة هي 'b'، وواحدة هي 'c'. الآن، لتمثيل 'a' المزدوجة بين القيم الأربع، لا نحتاج إلى تمثيلي تخزين مختلفين، حيث أن 'a' الاثنتين هما نفس الشيء. لذلك، من إجمالي عدد البتات المطلوبة لتمثيل 'a' المزدوجة للمتغير، يمكننا خصم log₂(2) بت، حيث أن تلك log₂(2) بت كانت من المفترض أن تميز بين 'a' الاثنتين اللتين هما في الواقع متطابقتان. وبالتالي، لتمثيل 'a'، سنحتاج إلى:
 log₂(4) – log₂(2) = 1 بت

الآن، لتحديد الكمية الإجمالية للتخزين المطلوبة للمتغير، نجمع ببساطة متطلبات التخزين أعلاه (للقيم الفردية المختلفة للمتغير) بما يتناسب مع تكرارات حدوثها:
 'a' تحدث نصف الوقت وتحتاج إلى 1 بت: 0.5×1
 'b' تحدث ربع الوقت وتحتاج إلى 2 بت: 0.25×2
 'c' تحدث ربع الوقت وتحتاج إلى 2 بت: 0.25×2
 في المجموع، نحتاج إلى 0.5×1 + 0.25×2 + 0.25×2  = 1.5 بت

لكن، هذه بالضبط هي صيغة شانون [1] للإنتروبيا!
 إنتروبيا شانون  E = -∑ᵢ(p(i)×log₂(p(i)))

لاحظ أن الإشارة السالبة تعتني بحقيقة أن p(i) هو كسر. على سبيل المثال، بالنسبة لـ 'a'،
 -p(a)×log₂(p(a)) = -{0.5×log₂(2/4)} = -{0.5×[log(2)–log(4)]} = +{0.5×[log(4)–log(2)]} = 0.5×1  !!

وبالتالي، فإن الإنتروبيا هي مقياس مباشر لعدد البتات اللازمة لتخزين المعلومات في متغير، على عكس بياناته الخام. وبالتالي، فإن الإنتروبيا هي مقياس مباشر لـ "كمية المعلومات" في متغير.

---

### Translation Notes

- **Key terms introduced:**
  - Shannon Entropy formula (صيغة إنتروبيا شانون)
  - logarithm (لوغاريتم)
  - numerator (بسط)
  - denominator (مقام)
  - fraction (كسر)
  - summation (∑ᵢ)
- **Mathematical formulas:**
  - Shannon Entropy: $E = -\sum_i(p(i) \times \log_2(p(i)))$
  - Logarithm properties preserved
  - Step-by-step derivation maintained
- **Special handling:**
  - Preserved all mathematical notation exactly
  - Maintained the logical flow of the derivation
  - Kept exclamation marks to show the "aha moment"
  - Ensured subscript notation (log₂) is clear
- **Equations:**
  - Multiple logarithmic calculations
  - Probability calculations
  - Algebraic manipulations

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.92
- Readability: 0.87
- Glossary consistency: 0.89
- **Overall section score:** 0.89
