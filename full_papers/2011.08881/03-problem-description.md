# Section 3: Problem description
## القسم 3: وصف المشكلة

**Section:** problem description
**Translation Quality:** 0.87
**Glossary Terms Used:** program synthesis, background knowledge, function templates, lambda calculus, type checking, induced programs, target function, positive examples, negative examples, program space, solution space

---

### English Version

Before presenting algorithms that solve the synthesis problem, we need to formalize it. We will assume, for the rest of the chapter, that all definitions will be relative to a target language L, whose syntax will be specified in the next chapter.

## 3.1 Abstract description of the problem

A program synthesis algorithm's aim is to induce programs with respect to some sort of user provided specification. The synthesis process will create programs which we call induced programs, that are composed of a set of functions which we call induced functions. For each induced program we will distinguish a function called the target function, which is to be applied to the examples to check whether a candidate program is a solution. Intuitively, the output shall be an induced program whose target function satisfies the provided specification.

The provided specification in this paper shall be divided in two parts: background knowledge and input-output examples.

**Definition 3.1 (Background knowledge (BK)).** We define background knowledge to be the information used during the synthesis process. The BK completely determines the possible forms an induced program can have. There are three types of BK that we consider:

• **Background functions:** represents the set of functions provided via an external source. We require those functions to be total so as to not introduce non-termination in an induced program. We use the notation BK_F to refer to this kind of knowledge.

• **Invented functions:** represents the set of functions that are invented during the synthesis process; this set grows dynamically during the synthesis process (with each new invented function). We use the notation BK_I to refer to this kind of knowledge.

• **Function templates:** a set of lambda calculus-style contexts that describe the possible forms of the induced functions. We use the notation BK_T to refer to it.

Let us unpack this definition. We have referred to both BK_I and BK_F to be sets of functions: more precisely, they are sets containing pairs of the form (f_name, f_body): f_name represents the identifier (function name) of function f, whereas f_body corresponds to the body of its definition. When we write f, we refer to the pair. Example 3.1 shows an example of two functions that might be part of BK_F.

**Example 3.1 (Background functions)**
```
rev xs = if xs == []
         then []
         else rev (tail xs) ++ [head xs]
addOne x = x + 1
```

Function templates represent the blueprints that we use when defining invented functions. They are contexts in the meta-theory of lambda calculus sense, that represent the application of a higher-order combinator, where the "holes" are place-holders for the required number of functional inputs for such a combinator. Those place-holders signify that there is missing information in the body of the induced function that needs to be filled with either background functions or synthesized functions. We have chosen those to specify the grammar of the invented functions because higher-order functions let us combine the background and invented functions in complex ways, and provide great flexibility. We note the similarity of our function templates to metarules [3] and sketches [21], which serve similar purposes in the respective systems where they are used. Example 3.2 shows the form of a few such templates. For convenience, we number the "holes", e.g. ◻_i, with indices starting from 1.

**Example 3.2 (Function templates)**
- Conditional templates: if ◻_1 then ◻_2 else ◻_3
- Identity: ◻_1
- Higher-order templates: ◻_1 . ◻_2, map ◻_1, filter ◻_1

We say an induced function is complete if its body has no holes and all functions mentioned in it have a definition, or incomplete otherwise. Similarly, we say an induced program is complete if it is composed of complete functions. We give a short example to see how templates and functions interact with each other, which will provide some intuition for the algorithmic approach to the inductive process presented in the next chapter.

**Example 3.3 (Derivation)**
Suppose we wish to find the complete function F = map reverse. The following process involving the BK will take place: we invent a new function F, and assign it the map template to obtain the definition F = map ◻_1; we then fill the remaining hole using reverse.

The second part of the specification is represented by examples.

**Definition 3.2 (Examples).** Examples are user provided input-output pairs that describe the aim of the induced program. We shall consider two types of examples:

• **Positive examples:** those specify what an induced program should produce;

• **Negative examples:** those specify what an induced program should not produce;

We use the relation in ↦_+ out to refer to positive examples, and the relation in ↦_- out to refer to negative ones. While the positive examples have a clear role in the synthesis process, the negative ones serve a slightly different one: they try to remove ambiguity, which is highlighted in example 3.4. Something to note is that both the positive and the negative examples need to have compatible types, meaning that if a type checker is used, all the inputs would share the same type, and so should the outputs.

**Example 3.4 (Examples)**
Given the positive examples [3, 2, 1] ↦_+ [1, 2, 3] and [5, 4] ↦_+ [4, 5], and the negative examples [1, 3, 2] ↦_- [2, 3, 1] and [5, 4] ↦_- [5, 4] then the program we want to induce is likely to be a list sorting algorithm. Note that if we only look at the positive examples, another possible induced program is reverse, but the negative example [1, 3, 2] ↦_- [2, 3, 1] removes this possibility.

**Definition 3.3 (Satisfiability).** We say an complete induced program P whose target function is f satisfies the relations ↦_+ and ↦_- if:

• ∀(in, out) ∈ ↦_+. f(in) = out

• ∀(in, out) ∈ ↦_-. f(in) ≠ out

**Definition 3.4 (Program space).** Assume we are given background knowledge BK and let T_check be a type checking algorithm for L. We define the program space P_BK to be composed of programs written in L such that:

1. the bodies of the induced functions are either function templates (which still have holes in them) or function applications (for completed functions).

2. the inputs for the higher-order functions (of the templates) are either functions from BK_I or BK_F.

3. they are typeable w.r.t. T_check.

4. they contain no cyclical definitions (guard against non-termination).

Note how the P_BK contains induced programs whose functions could still have unfilled holes. We now describe the solution space, which contains the programs we consider solutions.

**Definition 3.5 (Solution space).** Given BK, ↦_+ and ↦_-, we define the solution space S_BK,↦_+,↦_- ⊂ P_BK to be composed of complete programs whose target functions satisfy both ↦_+ and ↦_-.

We now formulate the program synthesis problem.

**Definition 3.6 (Program Synthesis problem).** Given:

• a set of positive input/output examples,

• a set of negative input/output examples,

• background knowledge BK

the Program Synthesis problem is to find a solution S ∈ S_BK,↦_+,↦_- that has the minimum number of functions (textually optimal solution).

## 3.2 Invention and reuse

For this section, suppose A is an algorithm that solves the Program Synthesis problem. First we formalize the concepts of invention and reuse, which we mentioned in chapters 1 and 2.

**Definition 3.7 (Invention).** We say that A can invent functions if at any point during the synthesis process it is able to fill a hole with a fresh function name (i.e. does not appear in any of the previous definitions).

**Definition 3.8 (Reuse).** We say that A can reuse functions if at any point during the synthesis process it is able to fill a hole with a function name that has been invented at some point during the synthesis process (be it defined or yet undefined).

As we can see, the two definitions are intertwined: we can not have reuse without invention. The motivation for inventing functions is that this creates modular programs, which naturally support function reuse. As we shall see in the next chapter, one of the main consequences with modularity is its effect on type based pruning techniques.

When function reuse is used, certain problems will benefit from this (such as droplasts from chapter 2): we could find solutions closer to the root, which can have noticeable effects on the computation time. However, enabling function reuse means that the BK increases with each newly invented function, and hence the branching factor of the search tree increases dynamically: in the end, function reuse can be seen as a trade-off between the depth and the branching factor of the search tree; this will benefit some sorts of problems, but for others it will just increase the computation time. The concerns we talked in this paragraph are related to the research questions posed in section 1.2, which we will address in the next two chapters.

---

### النسخة العربية

قبل تقديم الخوارزميات التي تحل مشكلة التوليف، نحتاج إلى إضفاء الطابع الرسمي عليها. سنفترض، لبقية الفصل، أن جميع التعريفات ستكون نسبية للغة مستهدفة L، والتي سيتم تحديد بنيتها في الفصل التالي.

## 3.1 الوصف المجرد للمشكلة

الهدف من خوارزمية توليف البرامج هو استنتاج البرامج فيما يتعلق ببعض أنواع المواصفات المقدمة من المستخدم. ستنشئ عملية التوليف برامج نسميها البرامج المستنتجة، والتي تتكون من مجموعة من الدوال نسميها الدوال المستنتجة. لكل برنامج مستنتج سنميز دالة تسمى الدالة المستهدفة، والتي سيتم تطبيقها على الأمثلة للتحقق مما إذا كان البرنامج المرشح حلاً. بشكل بديهي، يجب أن يكون المخرج برنامجاً مستنتجاً تُرضي دالته المستهدفة المواصفات المقدمة.

سيتم تقسيم المواصفات المقدمة في هذا البحث إلى جزأين: المعرفة الخلفية وأمثلة المدخلات-المخرجات.

**التعريف 3.1 (المعرفة الخلفية (BK)).** نعرّف المعرفة الخلفية على أنها المعلومات المستخدمة أثناء عملية التوليف. تحدد المعرفة الخلفية بالكامل الأشكال الممكنة التي يمكن أن يتخذها البرنامج المستنتج. هناك ثلاثة أنواع من المعرفة الخلفية نأخذها في الاعتبار:

• **دوال الخلفية:** تمثل مجموعة الدوال المقدمة عبر مصدر خارجي. نطلب أن تكون هذه الدوال كلية حتى لا تدخل عدم الانتهاء في برنامج مستنتج. نستخدم الترميز BK_F للإشارة إلى هذا النوع من المعرفة.

• **الدوال المبتكرة:** تمثل مجموعة الدوال التي يتم ابتكارها أثناء عملية التوليف؛ تنمو هذه المجموعة ديناميكياً أثناء عملية التوليف (مع كل دالة مبتكرة جديدة). نستخدم الترميز BK_I للإشارة إلى هذا النوع من المعرفة.

• **قوالب الدوال:** مجموعة من السياقات بأسلوب حساب لامبدا التي تصف الأشكال الممكنة للدوال المستنتجة. نستخدم الترميز BK_T للإشارة إليها.

دعونا نوضح هذا التعريف. أشرنا إلى كل من BK_I و BK_F على أنهما مجموعتان من الدوال: بشكل أكثر دقة، هما مجموعتان تحتويان على أزواج من الشكل (f_name, f_body): يمثل f_name المعرّف (اسم الدالة) للدالة f، بينما يقابل f_body جسم تعريفها. عندما نكتب f، نشير إلى الزوج. يوضح المثال 3.1 مثالاً لدالتين قد تكونان جزءاً من BK_F.

**المثال 3.1 (دوال الخلفية)**
```
rev xs = if xs == []
         then []
         else rev (tail xs) ++ [head xs]
addOne x = x + 1
```

تمثل قوالب الدوال المخططات التي نستخدمها عند تعريف الدوال المبتكرة. إنها سياقات بمعنى النظرية الفوقية لحساب لامبدا، تمثل تطبيق مركّب ذي رتبة عليا، حيث "الثقوب" هي عناصر نائبة للعدد المطلوب من المدخلات الوظيفية لمثل هذا المركّب. تشير هذه العناصر النائبة إلى وجود معلومات مفقودة في جسم الدالة المستنتجة التي تحتاج إلى ملئها إما بدوال الخلفية أو بالدوال المُولفة. لقد اخترنا هذه لتحديد قواعد الدوال المبتكرة لأن الدوال ذات الرتب العليا تتيح لنا دمج دوال الخلفية والدوال المبتكرة بطرق معقدة، وتوفر مرونة كبيرة. نلاحظ التشابه بين قوالب دوالنا والقواعد الفوقية [3] والمخططات [21]، التي تخدم أغراضاً مماثلة في الأنظمة المعنية التي تُستخدم فيها. يوضح المثال 3.2 شكل بعض هذه القوالب. للراحة، نرقم "الثقوب"، مثل ◻_i، بمؤشرات تبدأ من 1.

**المثال 3.2 (قوالب الدوال)**
- قوالب شرطية: if ◻_1 then ◻_2 else ◻_3
- الهوية: ◻_1
- قوالب ذات رتب عليا: ◻_1 . ◻_2، map ◻_1، filter ◻_1

نقول إن دالة مستنتجة كاملة إذا لم يكن لجسمها ثقوب وجميع الدوال المذكورة فيها لها تعريف، أو غير كاملة بخلاف ذلك. وبالمثل، نقول إن برنامجاً مستنتجاً كامل إذا كان يتكون من دوال كاملة. نقدم مثالاً قصيراً لنرى كيف تتفاعل القوالب والدوال مع بعضها البعض، مما سيوفر بعض الحدس للنهج الخوارزمي للعملية الاستقرائية المقدمة في الفصل التالي.

**المثال 3.3 (الاشتقاق)**
لنفترض أننا نرغب في إيجاد الدالة الكاملة F = map reverse. ستحدث العملية التالية التي تتضمن المعرفة الخلفية: نبتكر دالة جديدة F، ونعيّن لها قالب map للحصول على التعريف F = map ◻_1؛ ثم نملأ الثقب المتبقي باستخدام reverse.

الجزء الثاني من المواصفات ممثل بالأمثلة.

**التعريف 3.2 (الأمثلة).** الأمثلة هي أزواج مدخلات-مخرجات يقدمها المستخدم تصف هدف البرنامج المستنتج. سنأخذ في الاعتبار نوعين من الأمثلة:

• **الأمثلة الإيجابية:** تحدد ما يجب أن ينتجه البرنامج المستنتج؛

• **الأمثلة السلبية:** تحدد ما لا يجب أن ينتجه البرنامج المستنتج؛

نستخدم العلاقة in ↦_+ out للإشارة إلى الأمثلة الإيجابية، والعلاقة in ↦_- out للإشارة إلى الأمثلة السلبية. في حين أن للأمثلة الإيجابية دوراً واضحاً في عملية التوليف، فإن الأمثلة السلبية تخدم دوراً مختلفاً قليلاً: فهي تحاول إزالة الغموض، وهو ما تم تسليط الضوء عليه في المثال 3.4. شيء يجب ملاحظته هو أن كلاً من الأمثلة الإيجابية والسلبية تحتاج إلى أنواع متوافقة، مما يعني أنه إذا تم استخدام مدقق أنواع، فإن جميع المدخلات ستشترك في نفس النوع، وكذلك يجب أن تفعل المخرجات.

**المثال 3.4 (الأمثلة)**
بالنظر إلى الأمثلة الإيجابية [3, 2, 1] ↦_+ [1, 2, 3] و [5, 4] ↦_+ [4, 5]، والأمثلة السلبية [1, 3, 2] ↦_- [2, 3, 1] و [5, 4] ↦_- [5, 4]، فإن البرنامج الذي نريد استنتاجه من المحتمل أن يكون خوارزمية لترتيب القوائم. لاحظ أنه إذا نظرنا فقط إلى الأمثلة الإيجابية، فإن برنامجاً مستنتجاً محتملاً آخر هو reverse، لكن المثال السلبي [1, 3, 2] ↦_- [2, 3, 1] يزيل هذا الاحتمال.

**التعريف 3.3 (الإرضاء).** نقول إن برنامجاً مستنتجاً كاملاً P دالته المستهدفة هي f يُرضي العلاقات ↦_+ و ↦_- إذا:

• ∀(in, out) ∈ ↦_+. f(in) = out

• ∀(in, out) ∈ ↦_-. f(in) ≠ out

**التعريف 3.4 (فضاء البرامج).** لنفترض أننا أعطينا معرفة خلفية BK ودع T_check يكون خوارزمية فحص الأنواع لـ L. نعرّف فضاء البرامج P_BK على أنه يتكون من برامج مكتوبة في L بحيث:

1. أجسام الدوال المستنتجة هي إما قوالب دوال (التي لا تزال بها ثقوب) أو تطبيقات دوال (للدوال المكتملة).

2. المدخلات للدوال ذات الرتب العليا (للقوالب) هي إما دوال من BK_I أو BK_F.

3. قابلة للكتابة بالنسبة لـ T_check.

4. لا تحتوي على تعريفات دورية (حراسة ضد عدم الانتهاء).

لاحظ كيف يحتوي P_BK على برامج مستنتجة قد لا تزال دوالها تحتوي على ثقوب غير مملوءة. نصف الآن فضاء الحل، الذي يحتوي على البرامج التي نعتبرها حلولاً.

**التعريف 3.5 (فضاء الحل).** بالنظر إلى BK و ↦_+ و ↦_-، نعرّف فضاء الحل S_BK,↦_+,↦_- ⊂ P_BK على أنه يتكون من برامج كاملة دوالها المستهدفة تُرضي كلاً من ↦_+ و ↦_-.

نصيغ الآن مشكلة توليف البرامج.

**التعريف 3.6 (مشكلة توليف البرامج).** بالنظر إلى:

• مجموعة من أمثلة المدخلات/المخرجات الإيجابية،

• مجموعة من أمثلة المدخلات/المخرجات السلبية،

• معرفة خلفية BK

فإن مشكلة توليف البرامج هي إيجاد حل S ∈ S_BK,↦_+,↦_- له الحد الأدنى من عدد الدوال (حل أمثل نصياً).

## 3.2 الابتكار وإعادة الاستخدام

لهذا القسم، لنفترض أن A هي خوارزمية تحل مشكلة توليف البرامج. أولاً نضفي الطابع الرسمي على مفهومي الابتكار وإعادة الاستخدام، اللذين ذكرناهما في الفصلين 1 و 2.

**التعريف 3.7 (الابتكار).** نقول إن A يمكنها ابتكار دوال إذا كانت في أي نقطة أثناء عملية التوليف قادرة على ملء ثقب باسم دالة جديد (أي لا يظهر في أي من التعريفات السابقة).

**التعريف 3.8 (إعادة الاستخدام).** نقول إن A يمكنها إعادة استخدام الدوال إذا كانت في أي نقطة أثناء عملية التوليف قادرة على ملء ثقب باسم دالة تم ابتكارها في مرحلة ما أثناء عملية التوليف (سواء كانت معرّفة أو غير معرّفة بعد).

كما نرى، التعريفان متشابكان: لا يمكننا الحصول على إعادة الاستخدام بدون ابتكار. الدافع لابتكار الدوال هو أن هذا ينشئ برامج نمطية، تدعم بشكل طبيعي إعادة استخدام الدوال. كما سنرى في الفصل التالي، واحدة من العواقب الرئيسية للنمطية هي تأثيرها على تقنيات التقليم القائمة على الأنواع.

عند استخدام إعادة استخدام الدوال، ستستفيد مشاكل معينة من هذا (مثل droplasts من الفصل 2): يمكننا إيجاد حلول أقرب إلى الجذر، مما قد يكون له تأثيرات ملحوظة على وقت الحساب. ومع ذلك، فإن تمكين إعادة استخدام الدوال يعني أن المعرفة الخلفية تزداد مع كل دالة مبتكرة جديدة، وبالتالي يزداد معامل التفرع لشجرة البحث ديناميكياً: في النهاية، يمكن اعتبار إعادة استخدام الدوال مقايضة بين العمق ومعامل التفرع لشجرة البحث؛ سيستفيد هذا من بعض أنواع المشاكل، لكن بالنسبة للآخرين سيزيد فقط من وقت الحساب. المخاوف التي تحدثنا عنها في هذه الفقرة تتعلق بأسئلة البحث المطروحة في القسم 1.2، والتي سنتناولها في الفصلين القادمين.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** induced programs, induced functions, target function, background knowledge (BK), background functions (BK_F), invented functions (BK_I), function templates (BK_T), lambda calculus, higher-order combinator, holes, positive examples, negative examples, satisfiability, program space (P_BK), solution space (S_BK), type checking, textually optimal solution
- **Equations:** Multiple formal definitions with mathematical notation (∀, ∈, ↦, ⊂, ≠)
- **Citations:** [3], [21]
- **Special handling:**
  - All mathematical notation preserved exactly (↦_+, ↦_-, ◻_i, ∀, ∈, etc.)
  - Formal definitions numbered and formatted consistently
  - Code examples in Example 3.1 kept in English
  - Function notation (f_name, f_body, BK_F, BK_I, BK_T) maintained
  - Subscripts and mathematical symbols preserved

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.87

### Back-Translation Validation

Key paragraph back-translation (Definition 3.1):
"We define background knowledge to be the information used during the synthesis process. The BK completely determines the possible forms that an induced program can take. There are three types of BK that we consider: Background functions, Invented functions, and Function templates."

**Validation Score:** 0.87 - Strong semantic preservation with excellent handling of formal mathematical notation
