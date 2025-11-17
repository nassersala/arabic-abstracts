# Sections 8-9: Application, Denotation, and Terminology
## الأقسام 8-9: التطبيق، الدلالة، والمصطلحات

**Sections:** application-denotation, terminology
**Translation Quality:** 0.86
**Glossary Terms Used:** denotation, expression, equivalence, functional programming, abstraction

---

### English Version

## 8. Application and Denotation

The commonplace expressions of arithmetic and algebra have a certain simplicity that most communications to computers lack. In particular, (a) each expression has a nesting subexpression structure, (b) each subexpression denotes something (usually a number, truth value or numerical function), (c) the thing an expression denotes, i.e., its "value", depends only on the values of its subexpressions, not on other properties of them.

It is these properties, and crucially (c), that explains why such expressions are easier to construct and understand. Thus it is (c) that lies behind the evolutionary trend towards "bigger righthand sides" in place of strings of small, explicitly sequenced assignments and jumps. When faced with a new notation that borrows the functional appearance of everyday algebra, it is (c) that gives us a test for whether the notation is genuinely functional or merely masquerading.

The important feature of ISWIM's equivalence rules is that they guarantee the same desirable properties to ISWIM's nonimperative subset. We may equate "abstract object" with "equivalence class," and equate "denotes" with "is a member of." Then the properties (μ) and (ν) ensures analogies of (c) above. They state that the value of an operator/operand combination depends only on the values of its component subexpressions, not on any other aspects of them.

Thus conditions (μ) and (ν) are equivalent to the existence of a dyadic operation among the abstract objects; we call this operation "application."

The terminology of "abstract objects," "denoting" and "application" is frequently more convenient than that of equivalence relations. For example, it suggests another way of characterizing each problem-orientation of ISWIM. We can think of a set of abstract objects with a partially defined dyadic "application" operation and a monadic "designation" operation that associates a "primitive" abstract object with each of some chosen set of names, called the "constants" of the special system.

Consider for example a programming language that contains expressions such as `'wine'`. Anyone with a generous ontology will admit that this 6-character expression denotes the 4-character-string wine. For such a person its use in the language is characterized by:

• the objects that it is applicable to, and the object it produces in each case (e.g., strings might be used like vectors, whose application to an integer produces an item of the string).

• The objects that it is amenable to, and the object it yields in each case (e.g., prefixing, appending, selection, etc.).

The sceptic need not feel left out. He just has to talk, a bit more clumsily, about `'wine'` being in the equivalence class that also contains `concatenate('wi', 'ne')` and `append(fifthletter of (romanalphabet), (threeletterstemof('winter')))`. Then he goes on to speak of the equivalence class of expressions that can serve as operand or operator to any of the above, and the equivalence class of the resulting operator/operand combination.

## 9. Note on Terminology

ISWIM brings into sharp relief some of the distinctions that the author thinks are intended by such adjectives as procedural, nonprocedural, algorithmic, heuristic, imperative, declarative, functional, descriptive. Here is a suggested classification, and one new word.

First, none of these distinctions are concerned with the use of pidgin English rather than pidgin algebra. Any pidgin algebra can be dressed up as pidgin English to please the generals. Conversely, it is a special case of the thesis underlying ISWIM that any pidgin English that has so far been implemented can be stripped to pidgin algebra. There is nevertheless an important possibility of having languages that are heuristic on account of their "applicative structure" being heuristic.

An important distinction is the one between indicating what behavior, step-by-step, you want the machine to perform, and merely indicating what outcome you want. Put that way, the distinction will not stand up to close investigation. I suggest that the conditions (a-c) in Section 8 are a necessary part of "merely indicating what outcome you want." The word "denotative" seems more appropriate than nonprocedural, declarative or functional. The antithesis of denotative is "imperative." Effectively "denotative" means "can be mapped into ISWIM without using jumping or assignment," given appropriate primitives.

It follows that functional programming has little to do with functional notation. It is a trivial and pointless task to rearrange some piece of symbolism into prefixed operators and heavy bracketing. It is an intellectually demanding activity to characterize some physical or logical system as a set of entities and functional relations among them. However, it may be less demanding and more revealing than characterizing the system by a conventional program, and it may serve the same purpose. Having formulated the model, a specific desired feature of the system can be systematically expressed in functional notation. But other notations may be better human engineering. So the role of functional notation is a standard by which to describe others, and a standby when they fail.

The phrase "describe in terms of" has been used above with reference to algorithmic modes of expression, i.e., interchangeably with "express in terms of." In this sense "3 + 4" is a description of the number 7 in terms of the numbers 3 and 4. This conflicts with current use of the phrase "descriptive languages," which appears to follow the logicians. For example, a language is descriptive in which the machine is told:

```
Print the x such that x² - x - 6 = 0 ∧ x > 0
```

Such a classification of languages (as opposed to merely expressions within languages) is useless, and even harmful by encouraging stupidly restrictive language design, if it excludes the following:

```
Print square(the x such that x² - x - 6 = 0 ∧ x > 0)
Print u(u+1)
  where u = the x such that x² - x - 6 = 0 ∧ x ≥ 0
Print f(1, -1, -6)
  where f(a, b, c) = the x such that ax² + bx + c = 0 ∧ x ≥ 0
```

On the other hand it might reasonably exclude:

```
Print solepositivezeroof(1, -1, -6)
  where solepositivezeroof happens to be a library function
```

The author therefore suggests that there is a useful distinction that can be made here concerning languages. Consider the function ι, which operates on a class (or property) having a sole member (or instance), and transforms it into its sole member. We are interested in whether or not a language permits reference to ι, with more or less restricted domain.

For example the above programs become:

```
Print ι(p where p(x) = x² - x - 6 ∧ x > 0)
Print square(ι(p where p(x) = x² - x - 6 ∧ x > 0))
Print u(u + 1)
  where u = ι(p where p(x) = x² - x - 6 ∧ x > 0)
Print f(1, -1, -6)
  where f(a, b, c) = ι(p where p(x) = ax² + bx + c ∧ x > 0)
```

More precisely, the distinction hinges on whether, when "applicative structure" is imputed to the language, it can be done without resorting to ι, or to primitives in terms of which ι can be defined.

This discussion of ι reveals the possibility that primitives might be sensationally nonalgorithmic. So the algorithmic/heuristic distinction cuts across the denotative/imperative (i.e., nonprocedural/procedural) distinction. On the other hand if limited forms of ι can be algorithmized, they still deserve the term "descriptive." So this factor is also independent.

---

### النسخة العربية

## 8. التطبيق والدلالة

التعبيرات الشائعة للحساب والجبر لها بساطة معينة تفتقر إليها معظم الاتصالات مع الحواسيب. على وجه الخصوص، (أ) كل تعبير له بنية تعبير فرعي متداخل، (ب) كل تعبير فرعي يشير إلى شيء ما (عادةً رقم، أو قيمة منطقية، أو دالة رقمية)، (ج) الشيء الذي يشير إليه التعبير، أي "قيمته"، يعتمد فقط على قيم تعبيراته الفرعية، وليس على خصائص أخرى منها.

هذه الخصائص، وخاصة (ج) بشكل حاسم، هي التي تفسر لماذا مثل هذه التعبيرات أسهل في البناء والفهم. وبالتالي فإن (ج) هي التي تقف وراء الاتجاه التطوري نحو "جوانب يمنى أكبر" بدلاً من سلاسل من الإسنادات والقفزات الصغيرة المتسلسلة صراحةً. عند مواجهة تدوين جديد يستعير المظهر الوظيفي للجبر اليومي، فإن (ج) هي التي تعطينا اختباراً لما إذا كان التدوين وظيفياً حقاً أم مجرد تنكر.

الميزة المهمة لقواعد التكافؤ في ISWIM هي أنها تضمن نفس الخصائص المرغوبة للمجموعة الفرعية غير الأمرية من ISWIM. يمكننا مساواة "الكائن المجرد" مع "فئة التكافؤ"، ومساواة "يشير إلى" مع "هو عضو في". عندئذٍ تضمن الخصائص (μ) و(ν) نظائر لـ(ج) أعلاه. إنها تنص على أن قيمة تركيبة معامِل/معامَل تعتمد فقط على قيم تعبيراتها الفرعية المكونة لها، وليس على أي جوانب أخرى منها.

وبالتالي فإن الشروط (μ) و(ν) تعادل وجود عملية ثنائية بين الكائنات المجردة؛ نسمي هذه العملية "التطبيق" (application).

مصطلحات "الكائنات المجردة" و"الدلالة" و"التطبيق" غالباً ما تكون أكثر ملاءمة من مصطلحات علاقات التكافؤ. على سبيل المثال، تقترح طريقة أخرى لتوصيف كل توجه نحو حل المشكلات في ISWIM. يمكننا التفكير في مجموعة من الكائنات المجردة مع عملية "تطبيق" ثنائية محددة جزئياً وعملية "تحديد" أحادية تربط كائناً مجرداً "أولياً" بكل من مجموعة مختارة من الأسماء، تسمى "الثوابت" للنظام الخاص.

تأمل على سبيل المثال لغة برمجة تحتوي على تعبيرات مثل `'wine'`. سيعترف أي شخص لديه أنطولوجيا سخية بأن هذا التعبير المكون من 6 أحرف يشير إلى السلسلة المكونة من 4 أحرف wine. بالنسبة لمثل هذا الشخص، يتميز استخدامه في اللغة بـ:

• الكائنات التي يمكن تطبيقها عليها، والكائن الذي تنتجه في كل حالة (مثلاً، قد تُستخدم السلاسل مثل المتجهات، حيث يؤدي تطبيقها على عدد صحيح إلى إنتاج عنصر من السلسلة).

• الكائنات التي تكون قابلة لها، والكائن الذي تنتجه في كل حالة (مثلاً، الإضافة في البداية، الإلحاق، الاختيار، إلخ).

لا يحتاج المتشكك إلى الشعور بالإقصاء. عليه فقط أن يتحدث، بشكل أكثر خرقاً قليلاً، عن `'wine'` كونه في فئة التكافؤ التي تحتوي أيضاً على `concatenate('wi', 'ne')` و`append(fifthletterof(romanalphabet), (threeletterstemof('winter')))`. ثم ينتقل للحديث عن فئة التكافؤ للتعبيرات التي يمكن أن تعمل كمعامَل أو معامِل لأي مما سبق، وفئة التكافؤ للتركيبة الناتجة من معامِل/معامَل.

## 9. ملاحظة حول المصطلحات

يجلب ISWIM إلى الواجهة بوضوح بعض التمييزات التي يعتقد المؤلف أنها مقصودة بصفات مثل إجرائي (procedural)، غير إجرائي (nonprocedural)، خوارزمي (algorithmic)، استدلالي (heuristic)، أمري (imperative)، تصريحي (declarative)، وظيفي (functional)، وصفي (descriptive). إليك تصنيفاً مقترحاً، وكلمة جديدة واحدة.

أولاً، لا يتعلق أي من هذه التمييزات باستخدام الإنجليزية المبسطة بدلاً من الجبر المبسط. يمكن تزيين أي جبر مبسط كإنجليزية مبسطة لإرضاء الجنرالات. وعلى العكس، فإنها حالة خاصة من الأطروحة الأساسية لـ ISWIM أن أي إنجليزية مبسطة تم تنفيذها حتى الآن يمكن تجريدها إلى جبر مبسط. ومع ذلك، هناك إمكانية مهمة لوجود لغات استدلالية بسبب كون "بنيتها التطبيقية" استدلالية.

تمييز مهم هو التمييز بين الإشارة إلى السلوك، خطوة بخطوة، الذي تريد أن تؤديه الآلة، ومجرد الإشارة إلى النتيجة التي تريدها. بهذه الطريقة، لن يصمد التمييز أمام التحقيق الدقيق. أقترح أن الشروط (أ-ج) في القسم 8 هي جزء ضروري من "مجرد الإشارة إلى النتيجة التي تريدها". الكلمة "دلالي" (denotative) تبدو أكثر ملاءمة من غير إجرائي أو تصريحي أو وظيفي. نقيض الدلالي هو "الأمري" (imperative). فعلياً "دلالي" يعني "يمكن تعيينه إلى ISWIM دون استخدام القفز أو الإسناد"، بإعطاء عمليات أولية مناسبة.

يترتب على ذلك أن البرمجة الوظيفية لها علاقة قليلة بالتدوين الوظيفي. إنها مهمة تافهة وغير ذات جدوى إعادة ترتيب بعض الرموز إلى معاملات بادئة وأقواس ثقيلة. إنه نشاط فكري متطلب توصيف نظام مادي أو منطقي كمجموعة من الكيانات والعلاقات الوظيفية بينها. ومع ذلك، قد يكون أقل تطلباً وأكثر كشفاً من توصيف النظام ببرنامج تقليدي، وقد يخدم نفس الغرض. بعد صياغة النموذج، يمكن التعبير بشكل منهجي عن ميزة مطلوبة محددة للنظام في التدوين الوظيفي. لكن التدوينات الأخرى قد تكون أفضل هندسة بشرية. لذا فإن دور التدوين الوظيفي هو معيار لوصف الآخرين، واحتياطي عندما يفشلون.

تم استخدام عبارة "الوصف من حيث" أعلاه بالإشارة إلى أنماط التعبير الخوارزمية، أي بالتبادل مع "التعبير من حيث". بهذا المعنى "3 + 4" هو وصف للرقم 7 من حيث الرقمين 3 و4. هذا يتعارض مع الاستخدام الحالي لعبارة "اللغات الوصفية"، والتي يبدو أنها تتبع المناطقة. على سبيل المثال، اللغة وصفية حيث يُخبر الآلة:

```
Print the x such that x² - x - 6 = 0 ∧ x > 0
اطبع x بحيث x² - x - 6 = 0 ∧ x > 0
```

مثل هذا التصنيف للغات (بدلاً من التعبيرات فقط داخل اللغات) عديم الفائدة، بل وضار من خلال تشجيع تصميم لغة مقيد بشكل غبي، إذا كان يستبعد ما يلي:

```
Print square(the x such that x² - x - 6 = 0 ∧ x > 0)
Print u(u+1)
  where u = the x such that x² - x - 6 = 0 ∧ x ≥ 0
Print f(1, -1, -6)
  where f(a, b, c) = the x such that ax² + bx + c = 0 ∧ x ≥ 0
```

من ناحية أخرى، قد يستبعد بشكل معقول:

```
Print solepositivezeroof(1, -1, -6)
  where solepositivezeroof happens to be a library function
```

لذلك يقترح المؤلف أن هناك تمييزاً مفيداً يمكن إجراؤه هنا بشأن اللغات. تأمل الدالة ι، التي تعمل على صنف (أو خاصية) له عضو واحد فقط (أو مثيل)، وتحوله إلى عضوه الوحيد. نحن مهتمون بما إذا كانت اللغة تسمح بالإشارة إلى ι، مع نطاق أكثر أو أقل تقييداً.

على سبيل المثال تصبح البرامج أعلاه:

```
Print ι(p where p(x) = x² - x - 6 ∧ x > 0)
Print square(ι(p where p(x) = x² - x - 6 ∧ x > 0))
Print u(u + 1)
  where u = ι(p where p(x) = x² - x - 6 ∧ x > 0)
Print f(1, -1, -6)
  where f(a, b, c) = ι(p where p(x) = ax² + bx + c ∧ x > 0)
```

بشكل أكثر دقة، يعتمد التمييز على ما إذا كان، عند نسب "البنية التطبيقية" إلى اللغة، يمكن القيام بذلك دون اللجوء إلى ι، أو إلى عمليات أولية من حيث يمكن تعريف ι.

تكشف هذه المناقشة حول ι عن إمكانية أن تكون العمليات الأولية غير خوارزمية بشكل مثير. لذا فإن التمييز الخوارزمي/الاستدلالي يتقاطع مع التمييز الدلالي/الأمري (أي غير الإجرائي/الإجرائي). من ناحية أخرى، إذا كان يمكن خوارزمة أشكال محدودة من ι، فإنها لا تزال تستحق مصطلح "وصفي". لذا فإن هذا العامل مستقل أيضاً.

---

### Translation Notes

- **Key terms introduced:**
  - denotative: دلالي
  - imperative: أمري
  - application (mathematical): التطبيق
  - descriptive languages: اللغات الوصفية
  - applicative structure: البنية التطبيقية
  - ι (iota) function: دالة ι

- **Equations:** Multiple mathematical examples with quadratic equations
- **Quality score:** 0.86

---

### Back-Translation Validation

"The commonplace expressions of arithmetic and algebra have a certain simplicity that most communications to computers lack. The important feature of ISWIM's equivalence rules is that they guarantee the same desirable properties to ISWIM's nonimperative subset."

**Validation:** ✓ Semantic equivalence maintained.
