# Section 10: Eliminating Explicit Sequencing
## القسم 10: إزالة التسلسل الصريح

**Section:** eliminating-sequencing
**Translation Quality:** 0.87
**Glossary Terms Used:** expressions, conditional expressions, functional programming, ALGOL, explicit sequencing

---

### English Version

There is a game sometimes played with ALGOL 60 programs--rewriting them so as to avoid using labels and go to statements. It is part of a more embracing game--reducing the extent to which the program conveys its information by explicit sequencing. Roughly speaking this amounts to using fewer and larger statements. The game's significance lies in that it frequently produces a more "transparent" program--easier to understand, debug, modify and incorporate into a larger program.

The author does not argue the case against explicit sequencing here. Instead he takes as point of departure the observation that the user of any programming language is frequently presented with a choice between using explicit sequencing or some alternative feature of the language. Furthermore languages vary greatly in the alternatives they offer. For example, our game is greatly facilitated by ALGOL 60's conditional statements and conditional expressions. So the question considered here is: What other such features are there? This question is considered because, not surprisingly, it turns out that an emphasis on describing things in terms of other things leads to the same kind of requirements as an emphasis against explicit sequencing.

Though ALGOL 60 is comparatively favorable to this activity, it shares with most other current languages certain deficiencies that severely limit how far the game can go. The author's experiments suggest that two of the most needed features are:

• Treat a listing of expressions as a special case of the class of expressions, especially in the arms of a conditional expression, and in defining a function.

• Treat argument lists as a special case of lists. So a triadic function can have its arguments supplied by a conditional whose arms are 3-listings, or by application of a function that produces a 3-list. A similar situation arises when a 3-listing occurs as a definee. (Even LISP trips up here, over lists of length one.)

To clarify their practical use, here are some of the steps by which many a conventional ALGOL 60 or PL/1 program can be transformed into an ISWIM program that exploits ISWIM's nonimperative features.

(1) Rewrite the program so as to use two-dimensional layout and arrows to illuminate the explicit sequencing, i.e., as a flowchart with algebraic steps. Rearrange this to achieve the least confusing network of arrows.

(2) Apply the following changes repeatedly wherever they are applicable:

(a) Replace a string of independent assignments by one multiple assignment.

(b) Replace an assignment having purely local significance by a where-clause.

(c) Replace procedures by type-procedures (possibly with multiple type), and procedure statements by assignment statements.

(d) Replace conditional jumps by conditional statements having bigger arms.

(e) Replace a branch whose arms have assignees in common by an assignment with conditional right-hand side.

(f) Replace a join by two calls for a procedure.

It should be observed that translating into ISWIM does not force such rearrangements; it merely facilitates them.

One interesting observation is that the most recalcitrant uses of explicit sequencing appear to be associated with success/failure situations and the action needed on failure.

Section 2 discussed adding 'where' to a conventional programming language. Theory and experiment both support the opposite approach, that taken in LISP, of adding imperative features to a basically nonimperative language. One big advantage is that the resulting language will have a nonimperative subset.

The special claim of ISWIM is that it grafts procedural notions onto a purely functional base without disturbing many of the desirable properties. The underlying ideas have been presented in [2]. This paper can do no more than begin the task of explaining their practical significance.

---

### النسخة العربية

هناك لعبة تُلعب أحياناً مع برامج ALGOL 60--إعادة كتابتها لتجنب استخدام التسميات وعبارات go to. إنها جزء من لعبة أكثر شمولاً--تقليل المدى الذي ينقل فيه البرنامج معلوماته عن طريق التسلسل الصريح. بشكل تقريبي، يعادل هذا استخدام عبارات أقل وأكبر. تكمن أهمية اللعبة في أنها كثيراً ما تنتج برنامجاً أكثر "شفافية"--أسهل للفهم والتصحيح والتعديل والدمج في برنامج أكبر.

لا يجادل المؤلف ضد التسلسل الصريح هنا. بدلاً من ذلك، يأخذ كنقطة انطلاق الملاحظة أن مستخدم أي لغة برمجة غالباً ما يُقدم له خيار بين استخدام التسلسل الصريح أو بعض الميزات البديلة للغة. علاوة على ذلك، تختلف اللغات بشكل كبير في البدائل التي تقدمها. على سبيل المثال، يتم تسهيل لعبتنا بشكل كبير من خلال العبارات الشرطية والتعبيرات الشرطية في ALGOL 60. لذا فإن السؤال المطروح هنا هو: ما هي الميزات الأخرى من هذا القبيل؟ يتم النظر في هذا السؤال لأنه، ليس من المستغرب، يتبين أن التركيز على وصف الأشياء من حيث أشياء أخرى يؤدي إلى نفس نوع المتطلبات التي يؤدي إليها التركيز ضد التسلسل الصريح.

على الرغم من أن ALGOL 60 مؤاتٍ نسبياً لهذا النشاط، إلا أنه يشترك مع معظم اللغات الحالية الأخرى في أوجه قصور معينة تحد بشدة من مدى إمكانية اللعبة. تشير تجارب المؤلف إلى أن اثنتين من أكثر الميزات المطلوبة هي:

• معاملة قائمة التعبيرات كحالة خاصة من فئة التعبيرات، خاصة في ذراعي التعبير الشرطي، وفي تعريف دالة.

• معاملة قوائم الوسائط كحالة خاصة من القوائم. لذا يمكن أن يكون للدالة الثلاثية وسائطها مقدمة من شرطي أذرعه قوائم-3، أو بتطبيق دالة تنتج قائمة-3. تنشأ حالة مماثلة عندما تحدث قائمة-3 كمُعرَّف. (حتى LISP يتعثر هنا، على القوائم ذات الطول واحد.)

لتوضيح استخدامها العملي، إليك بعض الخطوات التي يمكن من خلالها تحويل العديد من برامج ALGOL 60 أو PL/1 التقليدية إلى برنامج ISWIM يستغل ميزات ISWIM غير الأمرية.

(1) أعد كتابة البرنامج بحيث يستخدم تخطيطاً ثنائي الأبعاد وأسهماً لإلقاء الضوء على التسلسل الصريح، أي كمخطط انسيابي بخطوات جبرية. أعد ترتيب هذا لتحقيق أقل شبكة مربكة من الأسهم.

(2) طبق التغييرات التالية بشكل متكرر حيثما كانت قابلة للتطبيق:

(أ) استبدل سلسلة من الإسنادات المستقلة بإسناد متعدد واحد.

(ب) استبدل إسناداً ذا أهمية محلية بحتة بعبارة-where.

(ج) استبدل الإجراءات بإجراءات النوع (ربما مع نوع متعدد)، وعبارات الإجراءات بعبارات الإسناد.

(د) استبدل القفزات الشرطية بعبارات شرطية ذات أذرع أكبر.

(هـ) استبدل فرعاً أذرعه لها مُسندات مشتركة بإسناد بجانب أيمن شرطي.

(و) استبدل اتحاداً باستدعاءين لإجراء.

ينبغي ملاحظة أن الترجمة إلى ISWIM لا تفرض مثل هذه الإعادات الترتيب؛ إنها تسهلها فقط.

ملاحظة مثيرة للاهتمام هي أن أكثر استخدامات التسلسل الصريح عناداً يبدو أنها مرتبطة بحالات النجاح/الفشل والإجراء المطلوب عند الفشل.

ناقش القسم 2 إضافة 'where' إلى لغة برمجة تقليدية. تدعم النظرية والتجربة معاً النهج المعاكس، الذي تم اتخاذه في LISP، وهو إضافة ميزات أمرية إلى لغة غير أمرية بشكل أساسي. ميزة كبيرة واحدة هي أن اللغة الناتجة ستكون لها مجموعة فرعية غير أمرية.

الادعاء الخاص بـ ISWIM هو أنه يطعّم المفاهيم الإجرائية على قاعدة وظيفية بحتة دون إزعاج العديد من الخصائص المرغوبة. تم تقديم الأفكار الأساسية في [2]. لا يمكن لهذه الورقة أن تفعل أكثر من البدء في مهمة شرح أهميتها العملية.

---

### Translation Notes

- **Key terms introduced:**
  - explicit sequencing: التسلسل الصريح
  - transparent program: برنامج شفاف
  - conditional statements: العبارات الشرطية
  - multiple assignment: إسناد متعدد
  - where-clause: عبارة-where
  - nonimperative features: ميزات غير أمرية

- **Equations:** None
- **Citations:** Reference to Section 2, reference to [2]
- **Special handling:**
  - Transformation steps clearly enumerated
  - Comparison with ALGOL 60 and LISP maintained
  - Practical programming guidance preserved

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87

---

### Back-Translation (Key Paragraph for Validation)

"There is a game sometimes played with ALGOL 60 programs--rewriting them so as to avoid using labels and go to statements. It is part of a more embracing game--reducing the extent to which the program conveys its information by explicit sequencing. The game's significance lies in that it frequently produces a more 'transparent' program--easier to understand, debug, modify and incorporate into a larger program."

**Validation:** ✓ Maintains semantic equivalence and practical programming advice.

**Note:** This section provides practical guidance on transforming imperative programs into functional ones, demonstrating ISWIM's practical value beyond theoretical considerations.
