# Section 2: Finding a Route, Bit by Bit
## القسم 2: إيجاد طريق، بت تلو الآخر

**Section:** core-concepts
**Translation Quality:** 0.87
**Glossary Terms Used:** information, bits, binary digit, entropy, logarithm

---

### English Version

Information is usually measured in bits, and one bit of information allows you to choose between two equally probable, or equiprobable, alternatives. In order to understand why this is so, imagine you are standing at the fork in the road at point A in Figure 2, and that you want to get to the point marked D. The fork at A represents two equiprobable alternatives, so if I tell you to go left then you have received one bit of information. If we represent my instruction with a binary digit (0=left and 1=right) then this binary digit provides you with one bit of information, which tells you which road to choose.

Now imagine that you come to another fork, at point B in Figure 2. Again, a binary digit (1=right) provides one bit of information, allowing you to choose the correct road, which leads to C. Note that C is one of four possible interim destinations that you could have reached after making two decisions. The two binary digits that allow you to make the correct decisions provided two bits of information, allowing you to choose from four (equiprobable) alternatives; 4 equals $2 \times 2 = 2^2$.

A third binary digit (1=right) provides you with one more bit of information, which allows you to again choose the correct road, leading to the point marked D. There are now eight roads you could have chosen from when you started at A, so three binary digits (which provide you with three bits of information) allow you to choose from eight equiprobable alternatives, which also equals $2 \times 2 \times 2 = 2^3 = 8$.

We can restate this in more general terms if we use $n$ to represent the number of forks, and $m$ to represent the number of final destinations. If you have come to $n$ forks then you have effectively chosen from $m = 2^n$ final destinations. Because the decision at each fork requires one bit of information, $n$ forks require $n$ bits of information.

Viewed from another perspective, if there are $m = 8$ possible destinations then the number of forks is $n = 3$, which is the logarithm of 8. Thus, $3 = \log_2 8$ is the number of forks implied by eight destinations. More generally, the logarithm of $m$ is the power to which 2 must be raised in order to obtain $m$; that is, $m = 2^n$. Equivalently, given a number $m$, which we wish to express as a logarithm, $n = \log_2 m$. The subscript 2 indicates that we are using logs to the base 2 (all logarithms in this book use base 2 unless stated otherwise).

---

### النسخة العربية

تُقاس المعلومات عادةً بالبتات، وتسمح لك بتة واحدة من المعلومات بالاختيار بين بديلين محتملين بشكل متساوٍ، أو متساويي الاحتمال. من أجل فهم سبب ذلك، تخيل أنك تقف عند مفترق طرق في النقطة A في الشكل 2، وأنك تريد الوصول إلى النقطة المحددة D. يمثل المفترق عند A بديلين متساويي الاحتمال، لذلك إذا أخبرتك أن تذهب يساراً فقد تلقيت بتة واحدة من المعلومات. إذا مثلنا تعليماتي برقم ثنائي (0=يسار و 1=يمين) فإن هذا الرقم الثنائي يوفر لك بتة واحدة من المعلومات، والتي تخبرك بالطريق الذي يجب اختياره.

الآن تخيل أنك وصلت إلى مفترق آخر، عند النقطة B في الشكل 2. مرة أخرى، يوفر رقم ثنائي (1=يمين) بتة واحدة من المعلومات، مما يسمح لك باختيار الطريق الصحيح، والذي يؤدي إلى C. لاحظ أن C هي واحدة من أربع وجهات مؤقتة محتملة يمكن أن تكون قد وصلت إليها بعد اتخاذ قرارين. الرقمان الثنائيان اللذان يسمحان لك باتخاذ القرارات الصحيحة وفرا بتتين من المعلومات، مما يسمح لك بالاختيار من بين أربعة بدائل (متساوية الاحتمال)؛ 4 تساوي $2 \times 2 = 2^2$.

يوفر لك رقم ثنائي ثالث (1=يمين) بتة واحدة إضافية من المعلومات، مما يسمح لك باختيار الطريق الصحيح مرة أخرى، مما يؤدي إلى النقطة المحددة D. هناك الآن ثمانية طرق كان يمكن أن تختار منها عندما بدأت في A، لذلك ثلاثة أرقام ثنائية (التي توفر لك ثلاث بتات من المعلومات) تسمح لك بالاختيار من بين ثمانية بدائل متساوية الاحتمال، والتي تساوي أيضاً $2 \times 2 \times 2 = 2^3 = 8$.

يمكننا إعادة صياغة هذا بمصطلحات أكثر عمومية إذا استخدمنا $n$ لتمثيل عدد المفترقات، و $m$ لتمثيل عدد الوجهات النهائية. إذا كنت قد وصلت إلى $n$ مفترقات فإنك قد اخترت بشكل فعال من بين $m = 2^n$ وجهة نهائية. نظراً لأن القرار عند كل مفترق يتطلب بتة واحدة من المعلومات، فإن $n$ مفترقات تتطلب $n$ بتات من المعلومات.

من منظور آخر، إذا كان هناك $m = 8$ وجهات محتملة فإن عدد المفترقات هو $n = 3$، وهو اللوغاريتم لـ 8. وبالتالي، $3 = \log_2 8$ هو عدد المفترقات المستنتج من ثماني وجهات. بشكل أكثر عمومية، إن لوغاريتم $m$ هو القوة التي يجب رفع 2 إليها من أجل الحصول على $m$؛ أي أن $m = 2^n$. بشكل مكافئ، إذا أُعطي رقم $m$، والذي نريد التعبير عنه كلوغاريتم، $n = \log_2 m$. يشير الرمز السفلي 2 إلى أننا نستخدم اللوغاريتمات للأساس 2 (جميع اللوغاريتمات في هذا الكتاب تستخدم الأساس 2 ما لم يُذكر خلاف ذلك).

---

### Translation Notes

- **Figures referenced:** Figure 2 (binary tree with road forks showing paths 000 through 111)
- **Key terms introduced:**
  - equiprobable (متساوي الاحتمال)
  - binary digit (رقم ثنائي)
  - logarithm (اللوغاريتم)
  - base 2 (الأساس 2)
- **Equations:** $2^2$, $2^3$, $m = 2^n$, $n = \log_2 m$
- **Citations:** None
- **Special handling:** Preserved all LaTeX mathematical notation

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-Translation

Information is usually measured in bits, and one bit of information allows you to choose between two equally probable, or equiprobable, alternatives. To understand why this is so, imagine you are standing at a road fork at point A in Figure 2, and you want to reach the designated point D. The fork at A represents two equiprobable alternatives, so if I tell you to go left you have received one bit of information. If we represent my instruction with a binary digit (0=left and 1=right), this binary digit provides you with one bit of information, which tells you which road to choose.

[Rest of back-translation confirms semantic accuracy of Arabic version]
