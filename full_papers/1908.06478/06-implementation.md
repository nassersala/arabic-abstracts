# Section 6: Implementation
## القسم 6: التطبيق

**Section:** implementation
**Translation Quality:** 0.86
**Glossary Terms Used:** compiler, analysis, type system, constraint solver, linear program, optimization

---

### English Version

The architecture of our tool is shown in Figure 8. We initiate the analysis by calling the GHC compiler on a given Haskell module. After the code was compiled to GHC Core, it is then fetched by our GHC plugin and passed to the actual analysis. Note that this Core "program" is actually a list of variable bindings; However, we can convert this list into a single expression by simply nesting let and letrec expressions. This allows us to generate an initial typing judgment, or "constraint", which needs to be proven.

**Figure 8:** Outline of the architecture of our analysis

```
.hs file → GHC compiler → GHC plugin → Core program → initial typing judgment
                                                             ↓
           LP ← LP solver ← typing with value annotations ← type system
                                  ↑
                    typing with variable annotations
                                  ↑
                              judgments
```

A constraint solver is used to apply the appropriate type rules to each judgment, and to keep track of the judgments that already have been or still need to be proven. Using a central "control unit" for managing derived judgments like this has several advantages; For example, this allows us to print a trace when we encounter a typing error, or to output the full derivation tree after the analysis has completed. This can be used as an evidence to support the correctness of the analysis result, or as a tool for debugging.

In most cases, there is no ambiguousness regarding which inference rule to apply on any given judgment; However, structural type rules are an exception, as any of them may be applied to any typing judgment. For our implementation, we therefore need to find a way to make these rule applications deterministic. A naive solution for this problem is to apply every structural once to every generated typing judgment before applying the next syntax-driven type rule. However, this needlessly increases the size of the derivation tree, as most of these rule applications would not add anything to the strength of our type system.

Instead we reused the same heuristics as described in section "4.5 Experimental Results" of the original paper on JVFH. [9] For example, consider the PREPAY rule, which allows us to prepay the cost of a variable in the context. This is used to simulate the fact that thunks are evaluated at most once, even when they are referenced multiple times in an expression. According to Jost et al., it suffices to apply this rule once whenever a new variable is inserted into the context of a typing judgment. In our system, this applies to the ABS_GC, LETREC_GC, LET_GC and CASEALG_GC rules. Note that the CASELIT_GC also introduces a new variable, but its thunk cost is always zero, so prepaying would be redundant.

For the most part, we found the given heuristics to be sufficient, with one exception: In the CASEALG_GC and CASELIT_GC rules, the number of resources remaining after evaluating the scrutinee is also used as the number of resources available before evaluating the respective cases. However, for most scrutinees, our type system will set this number to a low value which generally does not suffice for evaluating the cases. Therefore, we found it necessary to apply the RELAX rule to the scrutinee judgment. This allows us to artificially increase the number of resources available both before and after the evaluation by any value as needed. The intuition is that these additional resources are not used during the evaluation of the scrutinee; Therefore, they are available before its evaluation and also remain available afterwards.

In addition to the syntax-driven type rules mentioned in the previous section, we also had to hardcode the types of some specific variables. Most notably, these include operations on primitive types such as Int# or Float#. Usually, variables simply resolve to actual Haskell code, which we could analyze to derive an annotated type and an LP over its annotations. However, primitive operators do not correspond to any Haskell code; Instead, they are detected by the GHC compiler and translated into an appropriate opcode for the target machine of the compilation. Since these operators are hard-coded into the compiler, we also need to hard-code them into our analysis. We introduce an additional cost constant K_prim which is used for every execution of a primitive operation.

We also hard-coded several other variables from the Prelude, including dictionaries and operators on boxed primitive types such as Int and Float. This is a temporary solution introduced only because our implementation currently does not support multi-module programs yet. In the future, references to other modules – including the Prelude – should automatically be detected and handled correctly, rendering this workaround obsolete.

Finally, for solving the linear program we make use of glpk-hs, which previously was also used in the implementation of the JVFH type system. This package provides Haskell bindings for the GNU Linear Programming Kit. However, we have introduced an additional abstraction layer, so the use of this library is transparent to the majority of our code. Thus, it should be possible to replace the LP solver without much effort if required.

---

### النسخة العربية

تُظهر معمارية أداتنا في الشكل 8. نبدأ التحليل عن طريق استدعاء مترجم GHC على وحدة Haskell معطاة. بعد ترجمة الشفرة إلى GHC Core، يتم بعد ذلك جلبها بواسطة إضافة GHC الخاصة بنا وتمريرها إلى التحليل الفعلي. لاحظ أن "برنامج" Core هذا هو في الواقع قائمة من روابط المتغيرات؛ ومع ذلك، يمكننا تحويل هذه القائمة إلى تعبير واحد ببساطة عن طريق تداخل تعبيرات let و letrec. يسمح لنا ذلك بتوليد حكم تنميط أولي، أو "قيد"، يحتاج إلى إثبات.

**الشكل 8:** مخطط معمارية تحليلنا

```
ملف .hs → مترجم GHC → إضافة GHC → برنامج Core → حكم تنميط أولي
                                                        ↓
        LP ← حلّال LP ← تنميط بتعليمات قيم ← نظام الأنواع
                             ↑
                تنميط بتعليمات متغيرات
                             ↑
                         أحكام
```

يُستخدم حلّال قيود لتطبيق قواعد الأنواع المناسبة على كل حكم، ولتتبع الأحكام التي تم إثباتها بالفعل أو لا تزال بحاجة إلى إثبات. استخدام "وحدة تحكم" مركزية لإدارة الأحكام المُشتقة بهذه الطريقة له عدة مزايا؛ على سبيل المثال، يسمح لنا ذلك بطباعة تتبع عندما نواجه خطأ في التنميط، أو إخراج شجرة الاشتقاق الكاملة بعد اكتمال التحليل. يمكن استخدام ذلك كدليل لدعم صحة نتيجة التحليل، أو كأداة للتنقيح.

في معظم الحالات، لا يوجد غموض بشأن قاعدة الاستنتاج التي يجب تطبيقها على أي حكم معين؛ ومع ذلك، فإن قواعد الأنواع الهيكلية استثناء، حيث يمكن تطبيق أي منها على أي حكم تنميط. لذلك، بالنسبة لتطبيقنا، نحتاج إلى إيجاد طريقة لجعل تطبيقات القواعد هذه حتمية. الحل الساذج لهذه المشكلة هو تطبيق كل قاعدة هيكلية مرة واحدة على كل حكم تنميط مُولّد قبل تطبيق قاعدة الأنواع المدفوعة بالصياغة التالية. ومع ذلك، يزيد هذا بلا داعٍ من حجم شجرة الاشتقاق، حيث أن معظم تطبيقات القواعد هذه لن تضيف أي شيء إلى قوة نظام الأنواع لدينا.

بدلاً من ذلك، أعدنا استخدام نفس الإرشادات الموصوفة في القسم "4.5 النتائج التجريبية" من الورقة الأصلية حول JVFH. [9] على سبيل المثال، لننظر إلى قاعدة PREPAY، التي تسمح لنا بالدفع المسبق لتكلفة متغير في السياق. يُستخدم هذا لمحاكاة حقيقة أن الثانكات يتم تقييمها مرة واحدة على الأكثر، حتى عندما يُشار إليها عدة مرات في تعبير. وفقاً لـ Jost وزملائه، يكفي تطبيق هذه القاعدة مرة واحدة كلما تم إدراج متغير جديد في سياق حكم تنميط. في نظامنا، ينطبق هذا على قواعد ABS_GC و LETREC_GC و LET_GC و CASEALG_GC. لاحظ أن CASELIT_GC تُدخل أيضاً متغيراً جديداً، لكن تكلفة الثانك الخاصة به دائماً صفر، لذلك سيكون الدفع المسبق زائداً عن الحاجة.

في معظم الأحيان، وجدنا أن الإرشادات المعطاة كافية، مع استثناء واحد: في قواعد CASEALG_GC و CASELIT_GC، يُستخدم عدد الموارد المتبقية بعد تقييم المفحوص أيضاً كعدد الموارد المتاحة قبل تقييم الحالات المعنية. ومع ذلك، بالنسبة لمعظم المفحوصين، سيضبط نظام الأنواع لدينا هذا العدد على قيمة منخفضة لا تكفي بشكل عام لتقييم الحالات. لذلك، وجدنا أنه من الضروري تطبيق قاعدة RELAX على حكم المفحوص. يسمح لنا ذلك بزيادة عدد الموارد المتاحة بشكل مصطنع قبل التقييم وبعده بأي قيمة حسب الحاجة. الحدس هو أن هذه الموارد الإضافية لا تُستخدم أثناء تقييم المفحوص؛ لذلك، فهي متاحة قبل تقييمه وتبقى متاحة أيضاً بعد ذلك.

بالإضافة إلى قواعد الأنواع المدفوعة بالصياغة المذكورة في القسم السابق، اضطررنا أيضاً إلى ترميز أنواع بعض المتغيرات المحددة بشكل ثابت. والأبرز من ذلك، تشمل هذه العمليات على الأنواع البدائية مثل Int# أو Float#. عادةً، تحل المتغيرات ببساطة إلى شفرة Haskell فعلية، والتي يمكننا تحليلها لاشتقاق نوع مُعلّم وبرنامج خطي على تعليماته. ومع ذلك، لا تتوافق المعاملات البدائية مع أي شفرة Haskell؛ بدلاً من ذلك، يتم اكتشافها بواسطة مترجم GHC وترجمتها إلى رمز عملية مناسب للآلة المستهدفة للترجمة. نظراً لأن هذه المعاملات مُرمّزة بشكل ثابت في المترجم، فنحن بحاجة أيضاً إلى ترميزها بشكل ثابت في تحليلنا. نُدخل ثابت تكلفة إضافي K_prim يُستخدم لكل تنفيذ لعملية بدائية.

قمنا أيضاً بترميز عدة متغيرات أخرى من Prelude بشكل ثابت، بما في ذلك القواميس والمعاملات على الأنواع البدائية المُعلّبة مثل Int و Float. هذا حل مؤقت تم إدخاله فقط لأن تطبيقنا لا يدعم حالياً البرامج متعددة الوحدات بعد. في المستقبل، يجب اكتشاف المراجع إلى الوحدات الأخرى - بما في ذلك Prelude - والتعامل معها بشكل صحيح تلقائياً، مما يجعل هذا الحل البديل عفا عليه الزمن.

أخيراً، لحل البرنامج الخطي نستخدم glpk-hs، والتي تم استخدامها سابقاً أيضاً في تطبيق نظام أنواع JVFH. توفر هذه الحزمة روابط Haskell لمجموعة أدوات البرمجة الخطية GNU. ومع ذلك، قمنا بإدخال طبقة تجريد إضافية، بحيث يكون استخدام هذه المكتبة شفافاً لمعظم شفرتنا. وبالتالي، يجب أن يكون من الممكن استبدال حلّال البرمجة الخطية دون بذل الكثير من الجهد إذا لزم الأمر.

---

### Translation Notes

- **Figures referenced:** Figure 8 (Architecture diagram)
- **Key terms introduced:**
  - constraint solver (حلّال قيود)
  - control unit (وحدة تحكم)
  - derivation tree (شجرة الاشتقاق)
  - debugging (التنقيح)
  - inference rule (قاعدة الاستنتاج)
  - deterministic (حتمية)
  - heuristics (إرشادات)
  - prepay (الدفع المسبق)
  - opcode (رمز عملية)
  - boxed primitive types (أنواع بدائية مُعلّبة)
  - multi-module programs (برامج متعددة الوحدات)
  - abstraction layer (طبقة تجريد)
- **Equations:** None
- **Citations:** [9]
- **Special handling:**
  - Figure 8 diagram translated with Arabic labels
  - Technical package names (glpk-hs, GNU Linear Programming Kit) kept in English
  - Cost constant notation (K_prim) preserved

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86

### Back-Translation (First & Last Paragraphs)

**First paragraph:** The architecture of our tool is shown in Figure 8. We start the analysis by calling the GHC compiler on a given Haskell module. After compiling the code to GHC Core, it is then fetched by our GHC plugin and passed to the actual analysis. Note that this Core "program" is actually a list of variable bindings; however, we can convert this list into a single expression simply by nesting let and letrec expressions. This allows us to generate an initial typing judgment, or "constraint", that needs to be proven.

**Last paragraph:** Finally, for solving the linear program we use glpk-hs, which was also previously used in the implementation of the JVFH type system. This package provides Haskell bindings for the GNU Linear Programming Kit. However, we have introduced an additional abstraction layer, so the use of this library is transparent to most of our code. Therefore, it should be possible to replace the LP solver without expending much effort if necessary.
