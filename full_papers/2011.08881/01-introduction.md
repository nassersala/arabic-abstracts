# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.89
**Glossary Terms Used:** inductive programming, functional programming, program synthesis, machine learning, algorithm, type-based pruning, deductive programming, inductive logic programming, end-user programming

---

### English Version

## 1.1 Inductive programming

Inductive programming (IP) [8] - also known as program synthesis or example based learning - is a field that lies at the intersection of several computer science topics (machine learning, artificial intelligence, algorithm design) and is a form of automatic programming. IP, as opposed to deductive programming [15] (another automatic programming approach, where one starts with a full specification of the target program) tackles the problem starting with an incomplete specification and tries to generalize that into a program. Usually, that incomplete specification is represented by examples, so we can informally define inductive programming to be the process of creating programs from examples using a limited amount of background information - we shall call this process the program synthesis problem [20]. We give an example of what an IP system might produce, given a task:

**Example 1.1**
Input: The definitions of map and increment and the examples f ([1, 2, 3]) = [2, 3, 4] and f ([5, 6]) = [6, 7]).
Output: The definition f = map increment.

One of the key challenges of IP (and what makes it attractive) is the need to learn from small numbers of training examples, which mostly rules out statistical machine learning approaches, such as SVMS and neural networks.

**Figure 1.1: Flash fill in action**

This can clearly create problems: if the examples are not representative enough, we might not get the program we expect.

As noted in the survey by Gulwani et al [8], one of the main areas of research in IP has been end-user programming. More often than not, an application will be used by a non-programmer, and hence that user will probably not be able to write scripts that make interacting with that application easier. IP tries to offer a solution to that problem: the user could supply a (small) amount of information, such as a list of examples that describe the task, and an IP system could generate a small script that automates the task. Perhaps one of the most noteworthy applications of this idea is in the MS Excel plug-in Flash Fill [7]. Its task is to induce a program that generalizes some spreadsheet related operation, while only being given a few examples - usage of Flash Fill can be seen in figure 1.1.

## 1.2 Motivation

Two main areas of research in IP are inductive functional programming (IFP, which we will focus on in this paper) and inductive logic programming (ILP). The idea of function invention in the IFP context is not new, and indeed some systems use it, such as IGOR 2 and λ2. In informal terms, function invention mimics the way humans write programs: instead of writing a long one-line program, we break the bigger program into auxiliary functions that can be used to build a modular (equivalent) program.

In this context, we have asked the question of whether another program writing technique could be useful for inductive programming: reusing the functions that we have already invented. By reuse we mean that once a function has been invented, it can then be used in the definition of another function. While some ILP systems have explored the idea of reusing functions (such as Metagol and Hexmil [2] and to a lesser extent DILP [5] and ILASP [14]), function reuse and its benefits (if any) have not really been explored in the IFP context, as noted by Cropper [1]. When investigating the existing systems with invention capabilities, we have observed that the way the invention process is conducted makes reuse practically impossible. Moreover, even though predicate invention and reuse have been claimed as useful (at least in the ILP context [18]), to our knowledge there has been no work that empirically demonstrates that it is, nor any work discussing when it may be useful. To address those limitations, in this work we are interesting in the following research questions:

**Q1** Can function reuse improve learning performance (find programs faster)?

**Q2** What impact does modularity have on pruning techniques, especially type based ones?

**Q3** What impact does the grammar of the synthesized programs have on function reuse?

**Q4** What classes of problems benefit from it; that is, can we describe the kinds of programs where function reuse is useful?

## 1.3 Contributions

In this paper, we make the following contributions:

• We provide a formal framework to describe IFP approaches that solve the program synthesis problem by creating modular programs and that can exploit function reuse.

• Given this formal framework, we create two algorithms that solve the synthesis problem. One of them uses type based pruning to speed up the searching process, but uses a restrictive grammar; we have proven that for general grammars, this algorithm (which uses a "natural" type inference based pruning approach) loses completeness (which in particular greatly hinders function reuse). The second algorithm does not use type based pruning and works with general grammars, but we propose a way in which this might be achieved.

• Our experimental work has provided positive results, which shed light on the usefulness of reuse in the IFP context; for example, we have shown that reuse can decrease the size of the synthesized programs and hence reduce the overall computation time (in some cases dramatically). Through experimentation, we have also distinguished two classes of problems for which reuse is important: AI planning problems and problems concerned with nested data structures (we have focused on lists).

## 1.4 Structure of the report

The rest of the paper is structured as follows:

• **chapter 2:** Presents background on inductive programming, function invention and reuse, and a variety of other systems.

• **chapter 3:** Presents a formal framework for describing the program synthesis problem and formalizes function reuse.

• **chapter 4:** Presents two algorithms that attempt to solve the program synthesis problem, in light of the description presented in chapter 3.

• **chapter 5:** Explores the role of function reuse through experimentation and contains a variety of experiments that validate our hypothesis; we also explore the various use cases of function reuse.

• **chapter 6:** Presents the conclusions, limitations, possible extensions of the project.

---

### النسخة العربية

## 1.1 البرمجة الاستقرائية

البرمجة الاستقرائية (IP) [8] - المعروفة أيضاً باسم توليف البرامج أو التعلم القائم على الأمثلة - هي مجال يقع عند تقاطع العديد من موضوعات علوم الحاسوب (التعلم الآلي، الذكاء الاصطناعي، تصميم الخوارزميات) وهي شكل من أشكال البرمجة الآلية. على النقيض من البرمجة الاستنتاجية [15] (وهي نهج برمجة آلي آخر، حيث يبدأ المرء بمواصفات كاملة للبرنامج المستهدف)، تتعامل البرمجة الاستقرائية مع المشكلة بدءاً من مواصفات غير كاملة وتحاول تعميمها إلى برنامج. عادة، يتم تمثيل هذه المواصفات غير الكاملة بأمثلة، لذا يمكننا تعريف البرمجة الاستقرائية بشكل غير رسمي على أنها عملية إنشاء برامج من الأمثلة باستخدام كمية محدودة من المعلومات الخلفية - سنسمي هذه العملية مشكلة توليف البرامج [20]. نقدم مثالاً على ما قد ينتجه نظام البرمجة الاستقرائية، في ظل مهمة معينة:

**مثال 1.1**
المدخل: تعريفات map و increment والأمثلة f ([1, 2, 3]) = [2, 3, 4] و f ([5, 6]) = [6, 7]).
المخرج: التعريف f = map increment.

أحد التحديات الرئيسية للبرمجة الاستقرائية (وما يجعلها جذابة) هو الحاجة إلى التعلم من أعداد صغيرة من أمثلة التدريب، مما يستبعد إلى حد كبير أساليب التعلم الآلي الإحصائي، مثل SVMS والشبكات العصبية.

**الشكل 1.1: Flash Fill أثناء العمل**

يمكن أن يخلق هذا مشاكل بوضوح: إذا لم تكن الأمثلة ممثلة بما فيه الكفاية، فقد لا نحصل على البرنامج الذي نتوقعه.

كما لوحظ في المسح الذي أجراه Gulwani وآخرون [8], كان أحد المجالات الرئيسية للبحث في البرمجة الاستقرائية هو برمجة المستخدم النهائي. في أغلب الأحيان، سيتم استخدام التطبيق من قبل شخص غير مبرمج، وبالتالي من المحتمل ألا يتمكن هذا المستخدم من كتابة نصوص برمجية تجعل التفاعل مع هذا التطبيق أسهل. تحاول البرمجة الاستقرائية تقديم حل لتلك المشكلة: يمكن للمستخدم تقديم كمية (صغيرة) من المعلومات، مثل قائمة من الأمثلة التي تصف المهمة، ويمكن لنظام البرمجة الاستقرائية إنشاء نص برمجي صغير يؤتمت المهمة. ربما يكون أحد أبرز تطبيقات هذه الفكرة في إضافة MS Excel المسماة Flash Fill [7]. مهمتها هي استنتاج برنامج يعمم بعض العمليات المتعلقة بجداول البيانات، مع إعطائه بضعة أمثلة فقط - يمكن رؤية استخدام Flash Fill في الشكل 1.1.

## 1.2 الدافع

هناك مجالان رئيسيان للبحث في البرمجة الاستقرائية هما البرمجة الوظيفية الاستقرائية (IFP، والتي سنركز عليها في هذا البحث) والبرمجة المنطقية الاستقرائية (ILP). فكرة ابتكار الدوال في سياق البرمجة الوظيفية الاستقرائية ليست جديدة، وبالفعل تستخدمها بعض الأنظمة، مثل IGOR 2 و λ2. بعبارات غير رسمية، يحاكي ابتكار الدوال الطريقة التي يكتب بها البشر البرامج: بدلاً من كتابة برنامج طويل من سطر واحد، نقوم بتقسيم البرنامج الأكبر إلى دوال مساعدة يمكن استخدامها لبناء برنامج نمطي (مكافئ).

في هذا السياق، طرحنا السؤال عما إذا كانت تقنية كتابة برامج أخرى يمكن أن تكون مفيدة للبرمجة الاستقرائية: إعادة استخدام الدوال التي سبق لنا ابتكارها. بإعادة الاستخدام نعني أنه بمجرد ابتكار دالة، يمكن بعد ذلك استخدامها في تعريف دالة أخرى. في حين استكشفت بعض أنظمة البرمجة المنطقية الاستقرائية فكرة إعادة استخدام الدوال (مثل Metagol و Hexmil [2] وبدرجة أقل DILP [5] و ILASP [14])، لم يتم استكشاف إعادة استخدام الدوال وفوائدها (إن وجدت) حقاً في سياق البرمجة الوظيفية الاستقرائية، كما لاحظ Cropper [1]. عند التحقيق في الأنظمة الموجودة التي لديها قدرات الابتكار، لاحظنا أن الطريقة التي يتم بها إجراء عملية الابتكار تجعل إعادة الاستخدام مستحيلة عملياً. علاوة على ذلك، على الرغم من الادعاء بأن ابتكار المحمولات وإعادة استخدامها مفيد (على الأقل في سياق البرمجة المنطقية الاستقرائية [18])، لا نعلم وجود أي عمل يُظهر تجريبياً أن الأمر كذلك، ولا أي عمل يناقش متى قد يكون مفيداً. لمعالجة تلك القيود، نحن مهتمون في هذا العمل بأسئلة البحث التالية:

**س1** هل يمكن لإعادة استخدام الدوال تحسين أداء التعلم (إيجاد البرامج بشكل أسرع)؟

**س2** ما هو تأثير النمطية على تقنيات التقليم، وخاصة تلك القائمة على الأنواع؟

**س3** ما هو تأثير قواعد البرامج المُولفة على إعادة استخدام الدوال؟

**س4** ما هي فئات المشاكل التي تستفيد منها؛ أي، هل يمكننا وصف أنواع البرامج التي تكون فيها إعادة استخدام الدوال مفيدة؟

## 1.3 المساهمات

في هذا البحث، نقدم المساهمات التالية:

• نوفر إطاراً رسمياً لوصف نُهج البرمجة الوظيفية الاستقرائية التي تحل مشكلة توليف البرامج من خلال إنشاء برامج نمطية ويمكنها استغلال إعادة استخدام الدوال.

• بالنظر إلى هذا الإطار الرسمي، ننشئ خوارزميتين تحلان مشكلة التوليف. إحداهما تستخدم التقليم القائم على الأنواع لتسريع عملية البحث، لكنها تستخدم قواعد مقيدة؛ لقد أثبتنا أنه بالنسبة للقواعد العامة، تفقد هذه الخوارزمية (التي تستخدم نهج تقليم "طبيعي" قائم على استنتاج الأنواع) الاكتمال (مما يعيق بشكل كبير إعادة استخدام الدوال بشكل خاص). الخوارزمية الثانية لا تستخدم التقليم القائم على الأنواع وتعمل مع القواعد العامة، لكننا نقترح طريقة يمكن من خلالها تحقيق ذلك.

• قدم عملنا التجريبي نتائج إيجابية، تلقي الضوء على فائدة إعادة الاستخدام في سياق البرمجة الوظيفية الاستقرائية؛ على سبيل المثال، أظهرنا أن إعادة الاستخدام يمكن أن تقلل من حجم البرامج المُولفة وبالتالي تقلل من وقت الحساب الإجمالي (في بعض الحالات بشكل كبير). من خلال التجريب، ميزنا أيضاً بين فئتين من المشاكل التي تكون إعادة الاستخدام مهمة بالنسبة لها: مشاكل تخطيط الذكاء الاصطناعي والمشاكل المتعلقة ببنى البيانات المتداخلة (ركزنا على القوائم).

## 1.4 هيكل التقرير

يتم تنظيم باقي البحث على النحو التالي:

• **الفصل 2:** يقدم خلفية عن البرمجة الاستقرائية، وابتكار الدوال وإعادة استخدامها، ومجموعة متنوعة من الأنظمة الأخرى.

• **الفصل 3:** يقدم إطاراً رسمياً لوصف مشكلة توليف البرامج ويضفي الطابع الرسمي على إعادة استخدام الدوال.

• **الفصل 4:** يقدم خوارزميتين تحاولان حل مشكلة توليف البرامج، في ضوء الوصف المقدم في الفصل 3.

• **الفصل 5:** يستكشف دور إعادة استخدام الدوال من خلال التجريب ويحتوي على مجموعة متنوعة من التجارب التي تتحقق من صحة فرضيتنا؛ كما نستكشف حالات الاستخدام المختلفة لإعادة استخدام الدوال.

• **الفصل 6:** يقدم الاستنتاجات والقيود والإضافات الممكنة للمشروع.

---

### Translation Notes

- **Figures referenced:** Figure 1.1 (Flash Fill in action)
- **Key terms introduced:** Inductive programming (IP), program synthesis, example-based learning, deductive programming, inductive functional programming (IFP), inductive logic programming (ILP), function invention, function reuse, end-user programming, Flash Fill, modularity, type-based pruning
- **Equations:** None
- **Citations:** [1], [2], [5], [7], [8], [14], [15], [18], [20]
- **Special handling:**
  - System names kept in English (IGOR 2, λ2, Metagol, Hexmil, DILP, ILASP, Flash Fill)
  - Function names in Example 1.1 kept in English (map, increment, f)
  - Research questions Q1-Q4 maintained clear formatting

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.91
- Readability: 0.88
- Glossary consistency: 0.88
- **Overall section score:** 0.89

### Back-Translation Validation

Key paragraph back-translation (section 1.2, paragraph 2):
"In this context, we asked the question of whether another programming technique could be useful for inductive programming: reusing functions that we have already invented. By reuse we mean that once a function has been invented, it can then be used in the definition of another function. While some ILP systems have explored the idea of reusing functions (such as Metagol and Hexmil [2] and to a lesser extent DILP [5] and ILASP [14]), function reuse and its benefits (if any) have not really been explored in the context of inductive functional programming, as noted by Cropper [1]."

**Validation Score:** 0.89 - Strong semantic preservation with excellent technical accuracy
