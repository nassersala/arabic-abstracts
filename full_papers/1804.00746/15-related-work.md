# Section 15: Related Work
## القسم 15: الأعمال ذات الصلة

**Section:** Related Work
**Translation Quality:** 0.85
**Glossary Terms Used:** automatic differentiation, backpropagation, functional programming, compiler

---

### English Version

Related Work

The literature on automatic differentiation is vast, beginning with forward mode [Wengert, 1964] and later reverse mode [Speelpenning, 1980; Rall, 1981], with many developments since [Griewank, 1989; Griewank and Walther, 2008]. While most techniques and uses of AD have been directed at imperative programming, there are also variations for functional programs [Karczmarczuk, 1999, 2000, 2001; Pearlmutter and Siskind, 2007, 2008; Elliott, 2009]. The work in this paper differs in being phrased at the level of functions/morphisms and specified by functoriality, without any mention or manipulation of graphs or other syntactic representations. Moreover, the specifications in this paper are simple enough that the various forms of AD presented can be calculated into being [Bird and de Moor, 1996; Oliveira, 2018], and so are correct by construction.

Pearlmutter and Siskind [2008] make the following observation:

> In this context, reverse-mode AD refers to a particular construction in which the primal data-flow graph is transformed to construct an adjoint graph that computes the sensitivity values. In the adjoint, the direction of the data-flow edges are reversed; addition nodes are replaced by fanout nodes; fanout nodes are replaced by addition nodes; and other nodes are replaced by multiplication by their linearizations.

The Cont and Dual category transformers described in Sections 12 and 13 explain this "adjoint graph" construction without involving graphs. Data-flow edge reversal corresponds to the reversal of $(◦)$ (from Category), while fanout and addition correspond to $dup$ and $jam$ (from Cartesian and Cocartesian respectively), which are mutually dual.

The categorical approach in this paper also makes fanout easily apparent, as occurrences of $dup$, which are produced during translation from Haskell to categorical form [Elliott, 2017].

---

### النسخة العربية

الأعمال ذات الصلة

أدبيات التفاضل الآلي واسعة، بدءاً من النمط الأمامي [Wengert, 1964] ولاحقاً النمط العكسي [Speelpenning, 1980; Rall, 1981]، مع العديد من التطورات منذ ذلك الحين [Griewank, 1989; Griewank and Walther, 2008]. بينما كانت معظم تقنيات واستخدامات التفاضل الآلي موجهة نحو البرمجة الأمرية، هناك أيضاً أشكال متنوعة للبرامج الوظيفية [Karczmarczuk, 1999, 2000, 2001; Pearlmutter and Siskind, 2007, 2008; Elliott, 2009]. يختلف العمل في هذه الورقة في صياغته على مستوى الدوال/التشاكلات ومحدد بالدالية الفئوية، دون أي ذكر أو معالجة للرسوم البيانية أو التمثيلات النحوية الأخرى. علاوة على ذلك، فإن المواصفات في هذه الورقة بسيطة بما يكفي بحيث يمكن حساب الأشكال المختلفة من التفاضل الآلي المقدمة إلى الوجود [Bird and de Moor, 1996; Oliveira, 2018]، وبالتالي فهي صحيحة بالبناء.

يقدم بيرلماتر وسيسكيند [2008] الملاحظة التالية:

> في هذا السياق، يشير التفاضل الآلي ذو النمط العكسي إلى بناء معين يتم فيه تحويل الرسم البياني لتدفق البيانات الأولي لبناء رسم بياني مساعد يحسب قيم الحساسية. في المساعد، يتم عكس اتجاه حواف تدفق البيانات؛ يتم استبدال عُقد الجمع بعُقد التوزيع؛ يتم استبدال عُقد التوزيع بعُقد الجمع؛ ويتم استبدال العُقد الأخرى بالضرب بتخطيطاتها.

محولات الفئة Cont و Dual الموصوفة في الأقسام 12 و 13 تشرح هذا البناء "للرسم البياني المساعد" دون إشراك الرسوم البيانية. عكس حافة تدفق البيانات يتوافق مع عكس $(◦)$ (من Category)، بينما التوزيع والجمع يتوافقان مع $dup$ و $jam$ (من Cartesian و Cocartesian على التوالي)، وهما مزدوجان متبادلان.

النهج الفئوي في هذه الورقة يجعل أيضاً التوزيع واضحاً بسهولة، كحدوث لـ $dup$، التي يتم إنتاجها أثناء الترجمة من Haskell إلى الشكل الفئوي [Elliott, 2017].

---

### Translation Notes

- **Key terms:** forward mode, reverse mode, imperative programming, categorical approach
- **Citations:** 11 references to AD literature
- **Special handling:** Block quote preserved; comparison with prior work

### Quality Metrics

- **Overall section score:** 0.85
