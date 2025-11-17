# Section 2: Background and related work
## القسم 2: الخلفية والأعمال ذات الصلة

**Section:** background and related work
**Translation Quality:** 0.88
**Glossary Terms Used:** inductive programming, inductive functional programming, inductive logic programming, machine learning, artificial intelligence, cognitive science, algorithm, analytical approach, generate-and-test approach, genetic programming, type pruning, higher-order functions, background knowledge, meta-interpretative learning

---

### English Version

In the previous chapter, we have informally introduced the concept of inductive programming (IP), presented its relevance and showcased our ideas. In this chapter, we first provide the reader with more background on IP (areas of research, approaches) and then switch to literature review, showing different IP systems and their relevance to ours. We finish the chapter by talking about the idea of function invention and reuse.

## 2.1 Background on IP

IP has been around for almost half a century, with a lot of systems trying to tackle the problem of finding programs from examples. It is a subject that is placed at the crossroad between cognitive sciences, artificial intelligence, algorithm design and software development [13]. An interesting fact to note is that IP is a machine learning problem (learning from data) and moreover, in recent years it has gained attention because of the inherent transparency of its approach to learning, as opposed to the black box nature of statistical/neuronal approaches, as noted by Schmid [19].

IP has two main research areas, as noted by Gulwani et al. [8]:

• **Inductive functional programming (IFP):** IFP focuses on the synthesis of functional programs, typically used to create programs that manipulate data structures.

• **Inductive logical programming (ILP):** ILP started as research on induction in a logical context [8], generally used for learning AI tasks. It's aim is to construct a hypothesis (logic programs) h which explain examples E in terms of some background knowledge B [17].

As highlighted in the review by Kitzelmann [13], there have been two main approaches to inductive programming (for both IFP and ILP):

• **analytical approach:** Its aim is to exploit features in the input-output examples; the first systematic attempt was done by Summers' THESIS [23] system in 1977. He observed that using a few basic primitives and a fixed program grammar, a restricted class of recursive LISP programs that satisfy a set of input-output examples can be induced. Because of the inherent restrictiveness of the primitives, the analytical approach saw little innovation in the following decade, but systems like IGOR1, IGOR2 [11] have built on Summers' work. The analytical approach is also found in ILP, a well known example being Muggleton's Progol [16].

• **generate-and-test approach (GAT):** In GAT, examples are not used to actually construct the programs, but rather to test streams of possible programs, selected on some criteria from the program space. Compared to the analytical approach, GAT tends to be the more expressive approach, at the cost of higher computational time. Indeed, the ADATE system, a GAT system that uses genetic programming techniques to create programs, is one of the most powerful IP system with regards to expressivity [13]. Another well known GAT system is Katayama's Magic Haskeller [12], which uses type directed search and higher-order functions as background knowledge. Usually, to compensate for the fact that the program space is very big, most GAT systems will include some sort of pruning that discards undesirable programs.

## 2.2 Related work

We now present three systems that helped us develop our ideas and contrast them with our work.

### 2.2.1 Metagol

Metagol [2] is an ILP system that induces Prolog programs. It uses an idea called MIL, or meta-interpretative learning, to learn logic programs from examples. It uses three forms of background information:

• **compiled background knowledge (CBK):** those are small, first order Prolog programs that are deductively proven by the Prolog interpreter.

• **interpreted background knowledge (IBK):** this is represented by higher-order formulas that are proven with the aid of a meta-interpreter (since Prolog does not allow clauses with higher-order predicates as variables); for example, we could describe map/3 using the following two clauses:
  map([], [], F) :- and map([A|As], [B|Bs], F) :- F(A, B), map(As, Bs, F).

• **metarules:** those are rules that enforce the form (grammar) of the induced program's clauses; an example would be P(a, b) :- Q(a, c), R(c, b), where upper case letters are existentially quantified variables (they will be replaced with CBK or IBK).

The way the hypothesis search works is as follows: try to prove the required atom using CBK; if that fails, fetch a metarule, and try to fill in the existentially quantified variables; continue until a valid hypothesis (one that satisfies the examples) is found. Something to note here is that Metagol generates new examples: if we select the map metarule, based on the existing examples we can infer a set of derived examples that the functional argument of map must satisfy. This technique is used to prune incorrect programs from an early stage. All this process is wrapped in a depth-bounded search, so as to ensure the shortest program is found.

Our paper has started as an experiment to see whether ideas from Metagol could be transferred to a functional setting; hence, in the next chapters we use similar terminology, especially around metarules and background knowledge. We will also use depth-bounded search in our algorithm, for similar reasons to Metagol.

### 2.2.2 Magic Haskeller

Katayama's Magic Haskeller [12] is a GAT approach that uses type pruning and exhaustive search over the program space. Katayama argues that type pruning makes the search space manageable. One of the main innovation of the system was the usage of higher-order functions, which speeds up the searching process and helps simplify the output programs (which are chains of function applications). Our system differs in the fact that our programs are modular, which allow for function reuse. One of Magic Haskeller's limitations is the inability to provide user supplied background knowledge. The implementation of our algorithms enable a user to experiment with the background functions in a programmatic manner, and we also make it fairly easy to change the grammar of the programs.

### 2.2.3 λ2

λ2 [6] is an IFP system which combines GAT and analytical methods: the search is similar to Magic Haskeller, in the way that it uses higher order functions and explores the program space using type pruning, but differs in the fact that programs have a nested form (think of where clauses in Haskell) and uses an example propagation pruning method, similar to Metagol. However, such an approach does not allow function reuse, since an inner function can't use an "ancestor" function in its definition (possible infinite loop). Our paper tries to address this, exploring the possibility of creating non-nested programs and hence allowing function reuse.

## 2.3 Invention and reuse

Generally, most IP approaches tend to disregard the extra knowledge found during the synthesis process as another form of background knowledge. In fact, systems like λ2 and Magic Haskeller make this impossible because of how the search is conducted. Some systems, like Igor 2 do have a limited form of it, but it is very restrictive and does not allow function reuse in a general sense. This usually stems from what grammars the induced programs use. One of our main interests has been the usefulness of function reuse by allowing a modular (through function invention) way of generating programs (that is, we create "standalone" functions that can then be pieced together like a puzzle). For example, consider the drop lasts problem: given a non-empty list of lists, remove the last element of the outer list as well as the last elements of all the inner ones. Example 2.1 shows a possible program that was synthesized using only invention. However, if function reuse is enabled, example 2.2 shows how we can synthesize a simpler program, which we would expect to reduce the searching time.

**Example 2.1 (droplasts - only invention)**
```
target = f1 . f2
f1 = f2 . f4
f2 = reverse . f3
f3 = map reverse
f4 = tail . f5
f5 = map tail
```

**Example 2.2 (droplasts - invention + reuse)**
Note how f1 is reused to create a shorter program.
```
target = f1 . f2
f2 = map f1
f1 = reverse . f3
f3 = tail . reverse
```

An interesting questions when considering function reuse is what kind of programs benefit from it, which we explore in chapter 5, but we will now move to formalizing the program synthesis problem.

---

### النسخة العربية

في الفصل السابق، قدمنا بشكل غير رسمي مفهوم البرمجة الاستقرائية (IP)، وعرضنا أهميتها وأبرزنا أفكارنا. في هذا الفصل، نوفر أولاً للقارئ المزيد من الخلفية عن البرمجة الاستقرائية (مجالات البحث، النُهج) ثم ننتقل إلى مراجعة الأدبيات، نعرض أنظمة البرمجة الاستقرائية المختلفة وصلتها بنظامنا. ننهي الفصل بالحديث عن فكرة ابتكار الدوال وإعادة استخدامها.

## 2.1 الخلفية عن البرمجة الاستقرائية

البرمجة الاستقرائية موجودة منذ ما يقرب من نصف قرن، مع العديد من الأنظمة التي تحاول معالجة مشكلة إيجاد البرامج من الأمثلة. إنه موضوع يقع عند تقاطع العلوم المعرفية، والذكاء الاصطناعي، وتصميم الخوارزميات، وتطوير البرمجيات [13]. حقيقة مثيرة للاهتمام يجب ملاحظتها هي أن البرمجة الاستقرائية هي مشكلة تعلم آلي (التعلم من البيانات) وعلاوة على ذلك، في السنوات الأخيرة اكتسبت اهتماماً بسبب الشفافية الكامنة في نهجها للتعلم، على عكس طبيعة الصندوق الأسود للنهج الإحصائية/العصبونية، كما لاحظ Schmid [19].

للبرمجة الاستقرائية مجالان رئيسيان للبحث، كما لاحظ Gulwani وآخرون [8]:

• **البرمجة الوظيفية الاستقرائية (IFP):** تركز البرمجة الوظيفية الاستقرائية على توليف البرامج الوظيفية، التي تُستخدم عادة لإنشاء برامج تتعامل مع بنى البيانات.

• **البرمجة المنطقية الاستقرائية (ILP):** بدأت البرمجة المنطقية الاستقرائية كبحث عن الاستقراء في سياق منطقي [8]، وتُستخدم عموماً لتعلم مهام الذكاء الاصطناعي. هدفها هو بناء فرضية (برامج منطقية) h تشرح الأمثلة E من حيث بعض المعرفة الخلفية B [17].

كما سُلط الضوء عليه في المراجعة التي أجراها Kitzelmann [13]، كان هناك نهجان رئيسيان للبرمجة الاستقرائية (لكل من البرمجة الوظيفية الاستقرائية والبرمجة المنطقية الاستقرائية):

• **النهج التحليلي:** هدفه هو استغلال الميزات في أمثلة المدخلات-المخرجات؛ تمت المحاولة المنهجية الأولى من قبل نظام THESIS لـ Summers [23] في عام 1977. لاحظ أنه باستخدام عدد قليل من العناصر الأساسية وقواعد برنامج ثابتة، يمكن استنتاج فئة مقيدة من برامج LISP التكرارية التي ترضي مجموعة من أمثلة المدخلات-المخرجات. بسبب القيود الكامنة في العناصر الأساسية، شهد النهج التحليلي ابتكاراً ضئيلاً في العقد التالي، لكن أنظمة مثل IGOR1 و IGOR2 [11] بنت على عمل Summers. يوجد النهج التحليلي أيضاً في البرمجة المنطقية الاستقرائية، ومثال معروف هو Progol لـ Muggleton [16].

• **نهج التوليد والاختبار (GAT):** في نهج التوليد والاختبار، لا تُستخدم الأمثلة فعلياً لبناء البرامج، بل لاختبار سلاسل من البرامج المحتملة، المختارة بناءً على بعض المعايير من فضاء البرامج. مقارنةً بالنهج التحليلي، يميل نهج التوليد والاختبار إلى أن يكون النهج الأكثر تعبيراً، بتكلفة وقت حسابي أعلى. في الواقع، نظام ADATE، وهو نظام توليد واختبار يستخدم تقنيات البرمجة الجينية لإنشاء البرامج، هو أحد أقوى أنظمة البرمجة الاستقرائية من حيث التعبيرية [13]. نظام آخر معروف من نهج التوليد والاختبار هو Magic Haskeller لـ Katayama [12]، والذي يستخدم البحث الموجه بالأنواع والدوال ذات الرتب العليا كمعرفة خلفية. عادة، للتعويض عن حقيقة أن فضاء البرامج كبير جداً، فإن معظم أنظمة التوليد والاختبار ستتضمن نوعاً من التقليم الذي يتجاهل البرامج غير المرغوب فيها.

## 2.2 الأعمال ذات الصلة

نقدم الآن ثلاثة أنظمة ساعدتنا في تطوير أفكارنا ونقارنها بعملنا.

### 2.2.1 Metagol

Metagol [2] هو نظام برمجة منطقية استقرائية يستنتج برامج Prolog. يستخدم فكرة تسمى MIL، أو التعلم بالتفسير الفوقي، لتعلم البرامج المنطقية من الأمثلة. يستخدم ثلاثة أشكال من المعلومات الخلفية:

• **المعرفة الخلفية المترجمة (CBK):** هي برامج Prolog صغيرة من الرتبة الأولى تُثبت بشكل استنتاجي بواسطة مفسر Prolog.

• **المعرفة الخلفية المفسرة (IBK):** يتم تمثيلها بصيغ ذات رتب عليا تُثبت بمساعدة مفسر فوقي (حيث لا يسمح Prolog بالجمل ذات المحمولات ذات الرتب العليا كمتغيرات)؛ على سبيل المثال، يمكننا وصف map/3 باستخدام الجملتين التاليتين:
  map([], [], F) :- و map([A|As], [B|Bs], F) :- F(A, B), map(As, Bs, F).

• **القواعد الفوقية:** هي قواعد تفرض شكل (قواعد) جمل البرنامج المستنتج؛ مثال على ذلك سيكون P(a, b) :- Q(a, c), R(c, b)، حيث الحروف الكبيرة هي متغيرات محددة وجودياً (سيتم استبدالها بـ CBK أو IBK).

الطريقة التي يعمل بها بحث الفرضية هي كما يلي: محاولة إثبات الذرة المطلوبة باستخدام CBK؛ إذا فشل ذلك، جلب قاعدة فوقية، ومحاولة ملء المتغيرات المحددة وجودياً؛ الاستمرار حتى يتم العثور على فرضية صالحة (واحدة ترضي الأمثلة). شيء يجب ملاحظته هنا هو أن Metagol يولد أمثلة جديدة: إذا اخترنا القاعدة الفوقية map، بناءً على الأمثلة الموجودة يمكننا استنتاج مجموعة من الأمثلة المشتقة التي يجب أن ترضيها الوسيطة الوظيفية لـ map. تُستخدم هذه التقنية لتقليم البرامج غير الصحيحة من مرحلة مبكرة. كل هذه العملية ملفوفة في بحث محدود العمق، وذلك لضمان العثور على أقصر برنامج.

بدأ بحثنا كتجربة لمعرفة ما إذا كان يمكن نقل أفكار من Metagol إلى إطار وظيفي؛ ومن ثم، في الفصول القادمة نستخدم مصطلحات مماثلة، خاصة حول القواعد الفوقية والمعرفة الخلفية. سنستخدم أيضاً البحث محدود العمق في خوارزميتنا، لأسباب مماثلة لـ Metagol.

### 2.2.2 Magic Haskeller

Magic Haskeller لـ Katayama [12] هو نهج توليد واختبار يستخدم التقليم على أساس الأنواع والبحث الشامل في فضاء البرامج. يجادل Katayama بأن التقليم على أساس الأنواع يجعل فضاء البحث قابلاً للإدارة. كان أحد الابتكارات الرئيسية للنظام هو استخدام الدوال ذات الرتب العليا، مما يسرع عملية البحث ويساعد في تبسيط برامج المخرجات (وهي سلاسل من تطبيقات الدوال). يختلف نظامنا في حقيقة أن برامجنا نمطية، مما يسمح بإعادة استخدام الدوال. أحد قيود Magic Haskeller هو عدم القدرة على توفير معرفة خلفية يوفرها المستخدم. يتيح تنفيذ خوارزمياتنا للمستخدم التجربة مع الدوال الخلفية بطريقة برمجية، كما نجعل من السهل نسبياً تغيير قواعد البرامج.

### 2.2.3 λ2

λ2 [6] هو نظام برمجة وظيفية استقرائية يجمع بين أساليب التوليد والاختبار والأساليب التحليلية: البحث مشابه لـ Magic Haskeller، من حيث أنه يستخدم دوال ذات رتب عليا ويستكشف فضاء البرامج باستخدام التقليم على أساس الأنواع، لكنه يختلف في حقيقة أن البرامج لها شكل متداخل (فكر في جمل where في Haskell) ويستخدم طريقة تقليم بنشر الأمثلة، مشابهة لـ Metagol. ومع ذلك، لا يسمح مثل هذا النهج بإعادة استخدام الدوال، لأن الدالة الداخلية لا يمكنها استخدام دالة "سلف" في تعريفها (حلقة لا نهائية محتملة). يحاول بحثنا معالجة هذا، استكشاف إمكانية إنشاء برامج غير متداخلة وبالتالي السماح بإعادة استخدام الدوال.

## 2.3 الابتكار وإعادة الاستخدام

بشكل عام، تميل معظم نُهج البرمجة الاستقرائية إلى تجاهل المعرفة الإضافية الموجودة أثناء عملية التوليف كشكل آخر من المعرفة الخلفية. في الواقع، أنظمة مثل λ2 و Magic Haskeller تجعل هذا مستحيلاً بسبب كيفية إجراء البحث. بعض الأنظمة، مثل Igor 2 لديها شكل محدود منه، لكنه مقيد للغاية ولا يسمح بإعادة استخدام الدوال بمعنى عام. ينبع هذا عادة من القواعد التي تستخدمها البرامج المستنتجة. كان أحد اهتماماتنا الرئيسية هو فائدة إعادة استخدام الدوال من خلال السماح بطريقة نمطية (من خلال ابتكار الدوال) لتوليد البرامج (أي، ننشئ دوالاً "مستقلة" يمكن بعد ذلك تجميعها معاً مثل الأحجية). على سبيل المثال، لنأخذ مشكلة drop lasts: بالنظر إلى قائمة غير فارغة من القوائم، أزل العنصر الأخير من القائمة الخارجية بالإضافة إلى العناصر الأخيرة من جميع القوائم الداخلية. يوضح المثال 2.1 برنامجاً محتملاً تم توليفه باستخدام الابتكار فقط. ومع ذلك، إذا تم تمكين إعادة استخدام الدوال، يوضح المثال 2.2 كيف يمكننا توليف برنامج أبسط، والذي نتوقع أن يقلل من وقت البحث.

**المثال 2.1 (droplasts - الابتكار فقط)**
```
target = f1 . f2
f1 = f2 . f4
f2 = reverse . f3
f3 = map reverse
f4 = tail . f5
f5 = map tail
```

**المثال 2.2 (droplasts - الابتكار + إعادة الاستخدام)**
لاحظ كيف يتم إعادة استخدام f1 لإنشاء برنامج أقصر.
```
target = f1 . f2
f2 = map f1
f1 = reverse . f3
f3 = tail . reverse
```

سؤال مثير للاهتمام عند النظر في إعادة استخدام الدوال هو ما نوع البرامج التي تستفيد منه، والذي نستكشفه في الفصل 5، لكننا سننتقل الآن إلى إضفاء الطابع الرسمي على مشكلة توليف البرامج.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** Meta-interpretative learning (MIL), compiled background knowledge (CBK), interpreted background knowledge (IBK), metarules, depth-bounded search, type pruning, exhaustive search, example propagation, nested programs, modular programs
- **Equations:** None
- **Citations:** [2], [5], [6], [8], [11], [12], [13], [14], [16], [17], [19], [23]
- **Special handling:**
  - System names kept in English (Metagol, Magic Haskeller, λ2, IGOR, Progol, THESIS, ADATE, DILP, ILASP, Hexmil)
  - Prolog code examples kept in original format
  - Example 2.1 and 2.2 function definitions kept in English
  - Technical acronyms maintained (IFP, ILP, IP, GAT, MIL, CBK, IBK)

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.87
- **Overall section score:** 0.88

### Back-Translation Validation

Key paragraph back-translation (section 2.3, paragraph 1):
"Generally, most inductive programming approaches tend to disregard the extra knowledge found during the synthesis process as another form of background knowledge. In fact, systems like λ2 and Magic Haskeller make this impossible because of how the search is conducted. Some systems, like Igor 2 do have a limited form of it, but it is very restrictive and does not allow function reuse in a general sense."

**Validation Score:** 0.88 - Excellent preservation of technical meaning and context
