# Section 4: Translation
## القسم 4: الترجمة

**Section:** Translation Algorithm
**Translation Quality:** 0.86
**Glossary Terms Used:** translation, transpiling, soundness, inference rules, environment, closure, domain predicate, magic set transformation, lambda abstraction, application, fixpoint

---

### English Version

In this section we explain the core of the translation mechanism. Section 4.1 defines the relation between the translation and the PCF semantics. Section 4.2 introduces some conventions which explain the structure of the resulting program. Finally, Section 4.3 explains the static part of the translation. Section 4.4 defines the translation relation between PCF expressions and the dynamic part of the translation.

#### 4.1 Characterisation of the translation

**Translation relation** The translation is characterised using a relation which we will write as follows:

$$(E, S_1), e \leadsto A, (t, S_2)$$

- $E$ is a mapping from PCF-variables to ASP-terms for at least the free variables in $e$. This works analogously to the environment of the PCF semantics, which was the mapping from PCF-variables to closures.
- $S_1$ is a set of ASP atoms ensuring the ASP-terms in $E$ are safe, and constraints enforcing the ifzero-semantics.
- $e$ is the PCF expression that is translated.
- $A$ is the ASP program consisting of a set of safe ASP rules, this is the program that contains all the helper rules to translate $e$
- $t$ is the ASP term which represents the translation of $e$
- $S_2$ is the set of ASP atoms ensuring that $t$ is safe

It can be unintuitive that there are ASP-terms occurring on both sides of the translation relation. The explanation for this lies in the handling of free variables. The translation relation will be defined structurally, this means that for the translation of a composite term, the translation of its subterms are needed. This implies that when translating the expression $(\lambda x. x)$, the subterm $x$ needs to be translated as well. The translation needs some context to interpret this $x$ and the context of a translation environment will be some information about the parts which are already translated.

A PCF expression corresponds to a single value, but a logic program corresponds to an answer set with a lot of atoms. We need a way to indicate the actual value that is meant with the logic program. The result-predicate is used to indicate the resulting value of the program.

**Definition 2.** The ASP translation of a PCF expression $e$ determined by $\leadsto$ is the ASP program $A$ such that $(\emptyset, \emptyset), e \leadsto A_2, (t, S)$ and $A = A_2 \cup \{\text{result}(t) \text{:-} S\}$.

**Soundness of the translation** PCF inherently works on expressions which evaluate to a particular value, ASP programs define relations. A certain equivalence criterion is needed to validate the translation. For this we use the result-predicate. For ease of defining the correspondence the soundness criterion is restricted to programs with a numeric evaluation.

**Definition 3.** A sound translator for PCF to ASP maps every PCF expression $e$ to an ASP program $A$ with a unique answer set. This answer set contains at most one atom for the result-predicate. If $\emptyset, e \Downarrow n \in \mathbb{N}$, then $\text{result}(n)$ must be an element of the answer set of $A$.

**Claim.** The translation of PCF expressions determined by $\leadsto$ is a sound translator.

In this paper we will not prove this claim. We state it here to give the reader an intuition about the correspondence between a program and its translation.

#### 4.2 Conventions

In the translation, all PCF expressions $e$ correspond to a tuple $(t, S)$ where $t$ is an ASP term and $S$ is a set of ASP bodies. Natural numbers have constants in both PCF and ASP which have a natural correspondence. PCF functions are identified by an ASP term $t_f$, so that for every ASP term $t_x$, the tuple $(Y, \{\text{inter}(t_f, t_x, Y)\})$ denotes the image of the function $t_f$ applied to $t_x$. All functions have infinite domains, and thus the full function cannot be represented in a finite answer set. The domain predicate serves the purpose of making a finite estimate of the relevant parts of the function. If at some point in the evaluation of $e$, the function $t_f$ is applied to the value $t_x$, $\text{domain}(t_f, t_x)$ should be true. The inter-predicate only needs to be defined for the domain of the function, resulting in a finite answer set containing the relevant parts of the interpretation of the function.

Remember that result predicate is used as the predicate determining the final result of the program. So the translation of a PCF expression is an ASP program, defining only 3 predicates:
1. **inter**: determines the interpretation of functions
2. **domain**: determines the (relevant) domain of functions
3. **result**: determines the end result

**Magic Set Transformation** In these conventions a link with the magic set transformations [13] of logic programs appears. The magic set transformation allows us to transform a query, which is traditionally executed top-down, to a program, which can be executed bottom-up. It uses the magic predicates to indicate which subqueries needs to be performed. As explained in Section 3.2, ASP uses a bottom-up grounding process. So, the translation from PCF to ASP also converts a top-down query (the evaluation of PCF) to a bottom-up process (the ASP grounding). The domain-predicate has a function similar to the magic predicates: it indicates for which arguments a function needs to be calculated.

#### 4.3 Static Preamble

The translation of any PCF expression consists of a dynamic part and a static part. The static part ensures that the interpretation of the $\text{succ}$, $\text{pred}$ and $\text{fix}$ builtins is taken care of. The dynamic part is produced by the translation algorithm and takes care of the actual PCF expression. The static part is the same for every translation and can be seen in Listing 2.

**Listing 2:** Static preamble of the ASP translation

```
1  inter((pred, X), X-1) :- domain(pred, X), X > 0.
2  inter((succ, X), X+1) :- domain(succ, X).
3  inter((fix, F), Y) :- domain(fix, F), inter((F, f(F)), Y).
4  inter((f(F), X), Y) :- domain(f(F), X), inter((F, f(F)), FIX),
                          inter((FIX, X), Y).
5  domain(F, f(F)) :- domain(fix, F).
6  domain(FIX, X) :- domain(f(F), X), inter((F, f(F)), FIX).
```

The first two lines of the static part ensure the right translation of the $\text{pred}$ and $\text{succ}$ terms. E.g. the PCF-term $\text{succ}$ correctly corresponds to the ASP tuple $(\text{succ}, \{\})$ according to the conventions defined in Section 4.2. For instance, if somewhere the PCF-term $\text{succ } 0$ needs to be evaluated. The term will translate to $(Y, \{\text{inter}((\text{succ}, 0), Y)\})$ which will result in $Y$ being equal to 1 in the answer set.

Just like $\text{pred}$ and $\text{succ}$, the PCF- and ASP-term of $\text{fix}$ are the same. But the required rules in the preamble are more complex. A naive translation could look like this:
```
inter((fix, F), Z) :- inter((fix, F), Y), inter((F, Y), Z).
```
This rule most closely represents $\text{fix } f = f \, (\text{fix } f)$, but in the stable semantics this equation is not correctly represented by the above rule. Instead, an intermediate term $f(F)$ is introduced to symbolically represent the fixpoint of $F$ in ASP. Now we are able to write the fixpoint as the function $F$ applied to the symbolic function $f(F)$ as can be seen on line 3. If the fixpoint is a function, we need to be able to apply it to arguments. Line 4 serves this purpose: to apply $X$ to a fixpoint of a function, you can apply $F$ to this fixpoint (to ensure we do not have the symbolic representation) and then apply $X$ to the result. Finally, lines 5 and 6 ensure that the function applications performed in lines 3 and 4 are all well-defined through the domain predicates.

#### 4.4 Translation Algorithm

In this section we present the translation algorithm as a definition for the translation relation $\leadsto$ using inference rules. Sometimes new ASP constants or variables are needed in the translation. We suppose there is some global supply of those. We use the notation $\text{head} \leftarrow B$ for the ASP rule where head is the head atom and $B$ is the set of body atoms.

**Scoping** When translating an expression, the free variables in this expression need to be filled in. As we translate nested expressions level per level, we need to pass these values along the expression tree. For this reason, we do not just associate an identifier with a function but a tuple containing an identifier and the current scope. The current scope is a tupling of the full codomain of the translation environment $E$. We will refer to it as $\text{scope}_E$.

**Builtins (numbers, pred, succ, fix)**
$$\frac{}{(E, S), b \leadsto \emptyset, (b, S)}$$
Builtins are relatively easy to translate. The hard work is taken care of by the static preamble described in Section 4.3. A builtin produces no new ASP rules and is translated by itself. Safety is however taken into account, not for the scoping of variables, but for the handling of the if-zero constraints.

**Variable**
$$\frac{}{(E, S), x \leadsto \emptyset, (E[x], S)}$$
The algorithm carries around a mapping that represents how variables should be translated. This makes translating it a simple variable easy: just look it up in the mapping and combine it with the required safety.

**Application**
$$\frac{(E, S), e_1 \leadsto A_1, (t_1, B_1) \quad (E, S), e_2 \leadsto A_2, (t_2, B_2)}{(E, S), e_1 \, e_2 \leadsto A_1 \cup A_2 \cup \text{rule}_{\text{domain}}, (X, \text{body}_{\text{inter}} \cup B_1 \cup B_2)}$$
where:
- $X$ = a new ASP variable
- $\text{rule}_{\text{domain}} = \{\text{domain}(t_1, t_2) \leftarrow B_1 \cup B_2\}$
- $\text{body}_{\text{inter}} = \{\text{inter}((t_1, t_2), X)\}$

Applications are translated by independently translating the two subexpressions. The produced ASP programs need to be combined, with the additional rule that $t_2$ should be added to the domain of the function $t_1$. To obtain the resulting value, we use the inter-predicate according to the conventions explained in Section 4.2.

**Example 8.** The rule below shows how the application rule can be used to translate the successor of 1. The static part of the translation ensures that the inter-relation for $\text{succ}$ is interpreted correctly so that in any solution, the $X$ gets evaluated to 2.

$$\frac{\frac{}{(\emptyset, \emptyset), \text{succ} \leadsto \emptyset, (\text{succ}, \emptyset)} \quad \frac{}{(\emptyset, \emptyset), 1 \leadsto \emptyset, (1, \emptyset)}}{(\emptyset, \emptyset), \text{succ } 1 \leadsto \{\text{domain}(\text{succ}, 1)\}, (X, \text{inter}((\text{succ}, 1), X))}$$

**Lambda**
$$\frac{(E \cup (x, X), S \cup \text{body}_{\text{domain}}), e \leadsto A, (t, B)}{(E, S), \lambda x. e \leadsto A \cup \text{rule}_{\text{inter}}, ((l, \text{scope}_E), S)}$$
where:
- $X$ = a new ASP variable
- $l$ = a new ASP constant
- $\text{rule}_{\text{inter}} = \{\text{inter}(((l, \text{scope}_E), X), t) \leftarrow B\}$
- $\text{body}_{\text{domain}} = \{\text{domain}((l, \text{scope}_E), X)\}$

Lambda expressions bring a new variable into scope, so they modify the $(E, S)$-environment before recursively translating the body of the expression. The freshly scoped variable needs to be put into the scoping function $E$, for this we assign it a new ASP variable ($X$ in the rule). This variable should have a finite range, we invent a new name for our function ($l$ in the rule) and use the domain predicate to restrict $X$ to the domain of the function. The resulting translation $(t, B)$ represents the image of the function, so the rule $\text{rule}_{\text{inter}}$ is added to couple the representation of the function to its interpretation.

**Example 9.** $(\emptyset, \emptyset), (\lambda x. 2) \leadsto \{\text{inter}(((l, ()), X), 2) \leftarrow \text{domain}((l, ()), X)\}, ((l, ()), \emptyset)$

This can be read as follows: The translation of the constant function to 2 in an empty environment is represented by the constant $(l, ())$. The interpretation of $(l, ())$ when applied to any term $X$ in the domain of $(l, ())$ is 2.

**If zero-then-else**
$$\frac{(E, S), e_{\text{ifz}} \leadsto A_{\text{ifz}}, (t_{\text{ifz}}, B_{\text{ifz}}) \quad (E, B_{\text{ifz}} \cup \{t_{\text{ifz}} = 0\}), e_{\text{then}} \leadsto A_{\text{then}}, (t_{\text{then}}, B_{\text{then}}) \quad (E, B_{\text{ifz}} \cup \{t_{\text{ifz}} \neq 0\}), e_{\text{else}} \leadsto A_{\text{else}}, (t_{\text{else}}, B_{\text{else}})}{(E, S), \text{if } e_{\text{ifz}} \text{ then } e_{\text{then}} \text{ else } e_{\text{else}} \leadsto A_{\text{ite}} \cup \text{rule}_{\text{ite}}, (X, S \cup \text{body}_{\text{ite}})}$$
where:
- $X$ = a new ASP variable
- $\text{ite}$ = a new ASP constant
- $\text{rule}_{\text{ite}} = \{\text{inter}((\text{ite}, \text{scope}_E), t_{\text{then}}) \leftarrow B_{\text{then}}, \text{inter}((\text{ite}, \text{scope}_E), t_{\text{else}}) \leftarrow B_{\text{else}}\}$
- $\text{body}_{\text{ite}} = \{\text{inter}((\text{ite}, \text{scope}_E), X)\}$
- $A_{\text{ite}} = A_{\text{ifz}} \cup A_{\text{then}} \cup A_{\text{else}}$

If zero expressions are translated using the translations of its three subexpressions. But we need to alter the safety to ensure that the "then"-part is only evaluated if the "if"-part is 0 (and the analog for the "else" part). To construct the value of the full expression we define an intermediate symbol ($\text{ite}$ in the rule) to represent the union of the "then" and the "else" part. Because the extra safety ($= 0, \neq 0$) is mutually exclusive, only one of those terms will have a denotation, so the interpretation of $\text{ite}$ will be unique.

**Example 10.** The translation of $(\lambda x. \text{ifz } x \text{ then succ else pred}) \, 2 \, 4$ is visible in Listing 3. The static part is omitted. Lines 1 and 2 are result of the if zero-then-else translation. Line 3 is the result of the lambda translation. Lines 4 and 5 are the result of the application. And in line 6 the end result can be seen. This rule can be read as follows: Let $X_2$ be the application of the function to 2. Let $X_3$ be application of $X_2$ to 4. The final result is $X_3$.

**Listing 3:** Translation of $(\lambda x. \text{ifz } x \text{ then succ else pred}) \, 2 \, 4$

```
1  inter((ite1, (X0)), succ) :- domain((l0, ()), X0), X0 = 0.
2  inter((ite1, (X0)), pred) :- domain((l0, ()), X0), X0 <> 0.
3  inter(((l0, ()), X0), X1) :- domain((l0, ()), X0), inter((ite1, (X0)), X1).
4  domain((l0, ()), 2).
5  domain(X2, 4) :- inter(((l0, ()), 2), X2).
6  result(X3) :- inter(((l0, ()), 2), X2), inter((X2, 4), X3).
   % omitted static part visible in Listing 2
```

#### 4.5 Optimisations

The translation algorithm which is given in the previous section is not an optimal translation. A lot of optimisations are possible, for instance, not all variables in scope need to be present in $\text{scope}_E$, only the ones which are actually used in the subexpression. Applying such optimisations can significantly reduce the size of the grounding of the ASP program. The possibilities here are very interesting research topics, but are considered out of scope for this paper.

#### 4.6 Implementation

An implementation was made in Kotlin. The runtime uses Clingo [9] to run the resulting ASP files, but the resulting specifications could be used with any ASP-Core-2 [2] compliant system. On https://dtai.cs.kuleuven.be/krr/pcf2asp you can find a tool on which you can try out the translation. A few example PCF formulas are provided, but you can ask for translations of arbitrary PCF formulas and see their corresponding answer set.

---

### النسخة العربية

في هذا القسم نشرح جوهر آلية الترجمة. القسم 4.1 يعرّف العلاقة بين الترجمة ودلالات PCF. القسم 4.2 يقدم بعض الاصطلاحات التي تشرح بنية البرنامج الناتج. وأخيراً، القسم 4.3 يشرح الجزء الثابت من الترجمة. القسم 4.4 يعرّف علاقة الترجمة بين تعبيرات PCF والجزء الديناميكي من الترجمة.

#### 4.1 توصيف الترجمة

**علاقة الترجمة** يتم توصيف الترجمة باستخدام علاقة سنكتبها كما يلي:

$$(E, S_1), e \leadsto A, (t, S_2)$$

- $E$ هو تعيين من متغيرات PCF إلى حدود ASP على الأقل للمتغيرات الحرة في $e$. يعمل هذا بشكل مماثل لبيئة دلالات PCF، والتي كانت التعيين من متغيرات PCF إلى الإغلاقات.
- $S_1$ هي مجموعة من ذرات ASP تضمن أن حدود ASP في $E$ آمنة، وقيود تطبق دلالات ifzero.
- $e$ هو تعبير PCF الذي يتم ترجمته.
- $A$ هو برنامج ASP يتكون من مجموعة من قواعد ASP الآمنة، هذا هو البرنامج الذي يحتوي على جميع القواعد المساعدة لترجمة $e$
- $t$ هو حد ASP الذي يمثل ترجمة $e$
- $S_2$ هي مجموعة ذرات ASP التي تضمن أن $t$ آمن

قد يكون من غير البديهي وجود حدود ASP على كلا جانبي علاقة الترجمة. التفسير لهذا يكمن في معالجة المتغيرات الحرة. سيتم تعريف علاقة الترجمة بنيوياً، هذا يعني أنه لترجمة حد مركب، نحتاج إلى ترجمة حدوده الفرعية. هذا يعني أنه عند ترجمة التعبير $(\lambda x. x)$، يحتاج الحد الفرعي $x$ إلى الترجمة أيضاً. تحتاج الترجمة إلى بعض السياق لتفسير هذا $x$ وسياق بيئة الترجمة سيكون بعض المعلومات حول الأجزاء التي تمت ترجمتها بالفعل.

تعبير PCF يتوافق مع قيمة واحدة، لكن برنامج منطقي يتوافق مع مجموعة إجابات مع الكثير من الذرات. نحتاج إلى طريقة للإشارة إلى القيمة الفعلية المقصودة بالبرنامج المنطقي. يُستخدم محمول النتيجة للإشارة إلى القيمة الناتجة من البرنامج.

**تعريف 2.** ترجمة ASP لتعبير PCF $e$ المحددة بواسطة $\leadsto$ هي برنامج ASP $A$ بحيث $(\emptyset, \emptyset), e \leadsto A_2, (t, S)$ و $A = A_2 \cup \{\text{result}(t) \text{:-} S\}$.

**سلامة الترجمة** PCF بطبيعته يعمل على تعبيرات تُقيّم إلى قيمة معينة، برامج ASP تعرّف علاقات. معيار تكافؤ معين مطلوب للتحقق من صحة الترجمة. لهذا نستخدم محمول النتيجة. لسهولة تعريف المطابقة يقتصر معيار السلامة على البرامج ذات التقييم الرقمي.

**تعريف 3.** المترجم السليم من PCF إلى ASP يعيّن كل تعبير PCF $e$ إلى برنامج ASP $A$ مع مجموعة إجابات فريدة. تحتوي مجموعة الإجابات هذه على ذرة واحدة على الأكثر لمحمول النتيجة. إذا كان $\emptyset, e \Downarrow n \in \mathbb{N}$، فيجب أن يكون $\text{result}(n)$ عنصراً من مجموعة إجابات $A$.

**ادعاء.** ترجمة تعبيرات PCF المحددة بواسطة $\leadsto$ هي مترجم سليم.

في هذا البحث لن نثبت هذا الادعاء. نذكره هنا لإعطاء القارئ حدساً حول المطابقة بين البرنامج وترجمته.

#### 4.2 الاصطلاحات

في الترجمة، جميع تعبيرات PCF $e$ تتوافق مع مجموعة ثنائية $(t, S)$ حيث $t$ هو حد ASP و $S$ هي مجموعة من أجسام ASP. الأعداد الطبيعية لها ثوابت في كل من PCF و ASP التي لها مطابقة طبيعية. دوال PCF يتم تعريفها بحد ASP $t_f$، بحيث لكل حد ASP $t_x$، المجموعة الثنائية $(Y, \{\text{inter}(t_f, t_x, Y)\})$ تدل على صورة الدالة $t_f$ المطبقة على $t_x$. جميع الدوال لها نطاقات لا نهائية، وبالتالي لا يمكن تمثيل الدالة الكاملة في مجموعة إجابات محدودة. محمول النطاق يخدم غرض عمل تقدير محدود للأجزاء ذات الصلة من الدالة. إذا في أي نقطة في تقييم $e$، تم تطبيق الدالة $t_f$ على القيمة $t_x$، يجب أن يكون $\text{domain}(t_f, t_x)$ صحيحاً. محمول inter يحتاج فقط إلى التعريف لنطاق الدالة، مما ينتج عنه مجموعة إجابات محدودة تحتوي على الأجزاء ذات الصلة من تفسير الدالة.

تذكر أن محمول النتيجة يُستخدم كمحمول يحدد النتيجة النهائية للبرنامج. لذا فإن ترجمة تعبير PCF هي برنامج ASP، يعرّف 3 محمولات فقط:
1. **inter**: يحدد تفسير الدوال
2. **domain**: يحدد النطاق (ذي الصلة) للدوال
3. **result**: يحدد النتيجة النهائية

**تحويل المجموعة السحرية** في هذه الاصطلاحات يظهر رابط مع تحويلات المجموعة السحرية [13] للبرامج المنطقية. يسمح لنا تحويل المجموعة السحرية بتحويل استعلام، يُنفذ تقليدياً من الأعلى إلى الأسفل، إلى برنامج، يمكن تنفيذه من الأسفل إلى الأعلى. يستخدم المحمولات السحرية للإشارة إلى الاستعلامات الفرعية التي يجب تنفيذها. كما هو موضح في القسم 3.2، يستخدم ASP عملية تأريض من الأسفل إلى الأعلى. لذا، فإن الترجمة من PCF إلى ASP تحول أيضاً استعلاماً من الأعلى إلى الأسفل (تقييم PCF) إلى عملية من الأسفل إلى الأعلى (تأريض ASP). محمول النطاق له وظيفة مماثلة للمحمولات السحرية: يشير إلى الوسائط التي يجب حساب الدالة لها.

#### 4.3 المقدمة الثابتة

ترجمة أي تعبير PCF تتكون من جزء ديناميكي وجزء ثابت. الجزء الثابت يضمن أن تفسير الدوال المدمجة $\text{succ}$ و $\text{pred}$ و $\text{fix}$ يتم التعامل معه. الجزء الديناميكي يتم إنتاجه بواسطة خوارزمية الترجمة ويتعامل مع تعبير PCF الفعلي. الجزء الثابت هو نفسه لكل ترجمة ويمكن رؤيته في القائمة 2.

**القائمة 2:** المقدمة الثابتة لترجمة ASP

```
1  inter((pred, X), X-1) :- domain(pred, X), X > 0.
2  inter((succ, X), X+1) :- domain(succ, X).
3  inter((fix, F), Y) :- domain(fix, F), inter((F, f(F)), Y).
4  inter((f(F), X), Y) :- domain(f(F), X), inter((F, f(F)), FIX),
                          inter((FIX, X), Y).
5  domain(F, f(F)) :- domain(fix, F).
6  domain(FIX, X) :- domain(f(F), X), inter((F, f(F)), FIX).
```

السطران الأولان من الجزء الثابت يضمنان الترجمة الصحيحة لحدود $\text{pred}$ و $\text{succ}$. على سبيل المثال، حد PCF $\text{succ}$ يتوافق بشكل صحيح مع مجموعة ASP الثنائية $(\text{succ}, \{\})$ وفقاً للاصطلاحات المحددة في القسم 4.2. على سبيل المثال، إذا في مكان ما حد PCF $\text{succ } 0$ يحتاج إلى التقييم. سيترجم الحد إلى $(Y, \{\text{inter}((\text{succ}, 0), Y)\})$ والذي سينتج عنه $Y$ يساوي 1 في مجموعة الإجابات.

تماماً مثل $\text{pred}$ و $\text{succ}$، حدا PCF و ASP لـ $\text{fix}$ هما نفسهما. لكن القواعد المطلوبة في المقدمة أكثر تعقيداً. الترجمة الساذجة يمكن أن تبدو كما يلي:
```
inter((fix, F), Z) :- inter((fix, F), Y), inter((F, Y), Z).
```
هذه القاعدة تمثل بشكل أقرب $\text{fix } f = f \, (\text{fix } f)$، لكن في الدلالات المستقرة هذه المعادلة لا يتم تمثيلها بشكل صحيح بواسطة القاعدة أعلاه. بدلاً من ذلك، يتم تقديم حد وسيط $f(F)$ لتمثيل النقطة الثابتة لـ $F$ بشكل رمزي في ASP. الآن يمكننا كتابة النقطة الثابتة كدالة $F$ مطبقة على الدالة الرمزية $f(F)$ كما يمكن رؤيته في السطر 3. إذا كانت النقطة الثابتة دالة، نحتاج إلى أن نكون قادرين على تطبيقها على الوسائط. السطر 4 يخدم هذا الغرض: لتطبيق $X$ على نقطة ثابتة لدالة، يمكنك تطبيق $F$ على هذه النقطة الثابتة (للتأكد من أننا لا نملك التمثيل الرمزي) ثم تطبيق $X$ على النتيجة. وأخيراً، السطران 5 و 6 يضمنان أن تطبيقات الدوال المنفذة في السطرين 3 و 4 جميعها محددة بشكل جيد من خلال محمولات النطاق.

#### 4.4 خوارزمية الترجمة

في هذا القسم نقدم خوارزمية الترجمة كتعريف لعلاقة الترجمة $\leadsto$ باستخدام قواعد الاستنتاج. أحياناً تكون ثوابت أو متغيرات ASP جديدة مطلوبة في الترجمة. نفترض أن هناك مخزوناً عالمياً من تلك. نستخدم الترميز $\text{head} \leftarrow B$ لقاعدة ASP حيث head هي ذرة الرأس و $B$ هي مجموعة ذرات الجسم.

**النطاقية** عند ترجمة تعبير، المتغيرات الحرة في هذا التعبير تحتاج إلى الملء. بما أننا نترجم التعبيرات المتداخلة مستوى تلو الآخر، نحتاج إلى تمرير هذه القيم على طول شجرة التعبير. لهذا السبب، لا نربط فقط معرّفاً بدالة ولكن مجموعة ثنائية تحتوي على معرّف والنطاق الحالي. النطاق الحالي هو تجميع للنطاق المشترك الكامل لبيئة الترجمة $E$. سنشير إليه بـ $\text{scope}_E$.

**الدوال المدمجة (أرقام، pred، succ، fix)**
$$\frac{}{(E, S), b \leadsto \emptyset, (b, S)}$$
الدوال المدمجة سهلة نسبياً للترجمة. العمل الشاق يتم التعامل معه بواسطة المقدمة الثابتة الموصوفة في القسم 4.3. دالة مدمجة لا تنتج قواعد ASP جديدة وتترجم بنفسها. الأمان مع ذلك يؤخذ في الاعتبار، ليس لنطاقية المتغيرات، ولكن للتعامل مع قيود if-zero.

**المتغير**
$$\frac{}{(E, S), x \leadsto \emptyset, (E[x], S)}$$
الخوارزمية تحمل حولها تعييناً يمثل كيف يجب ترجمة المتغيرات. هذا يجعل ترجمة متغير بسيط سهلة: فقط ابحث عنه في التعيين واجمعه مع الأمان المطلوب.

**التطبيق**
$$\frac{(E, S), e_1 \leadsto A_1, (t_1, B_1) \quad (E, S), e_2 \leadsto A_2, (t_2, B_2)}{(E, S), e_1 \, e_2 \leadsto A_1 \cup A_2 \cup \text{rule}_{\text{domain}}, (X, \text{body}_{\text{inter}} \cup B_1 \cup B_2)}$$
حيث:
- $X$ = متغير ASP جديد
- $\text{rule}_{\text{domain}} = \{\text{domain}(t_1, t_2) \leftarrow B_1 \cup B_2\}$
- $\text{body}_{\text{inter}} = \{\text{inter}((t_1, t_2), X)\}$

تتم ترجمة التطبيقات عن طريق ترجمة التعبيرين الفرعيين بشكل مستقل. برامج ASP المنتجة يجب أن تُدمج، مع القاعدة الإضافية بأن $t_2$ يجب أن يُضاف إلى نطاق الدالة $t_1$. للحصول على القيمة الناتجة، نستخدم محمول inter وفقاً للاصطلاحات الموضحة في القسم 4.2.

**مثال 8.** القاعدة أدناه توضح كيف يمكن استخدام قاعدة التطبيق لترجمة خلف 1. الجزء الثابت من الترجمة يضمن أن علاقة inter لـ $\text{succ}$ تُفسر بشكل صحيح بحيث في أي حل، $X$ يُقيّم إلى 2.

$$\frac{\frac{}{(\emptyset, \emptyset), \text{succ} \leadsto \emptyset, (\text{succ}, \emptyset)} \quad \frac{}{(\emptyset, \emptyset), 1 \leadsto \emptyset, (1, \emptyset)}}{(\emptyset, \emptyset), \text{succ } 1 \leadsto \{\text{domain}(\text{succ}, 1)\}, (X, \text{inter}((\text{succ}, 1), X))}$$

**لامبدا**
$$\frac{(E \cup (x, X), S \cup \text{body}_{\text{domain}}), e \leadsto A, (t, B)}{(E, S), \lambda x. e \leadsto A \cup \text{rule}_{\text{inter}}, ((l, \text{scope}_E), S)}$$
حيث:
- $X$ = متغير ASP جديد
- $l$ = ثابت ASP جديد
- $\text{rule}_{\text{inter}} = \{\text{inter}(((l, \text{scope}_E), X), t) \leftarrow B\}$
- $\text{body}_{\text{domain}} = \{\text{domain}((l, \text{scope}_E), X)\}$

تعبيرات لامبدا تجلب متغيراً جديداً إلى النطاق، لذا تعدل بيئة $(E, S)$ قبل ترجمة جسم التعبير بشكل عودي. المتغير المنطوق حديثاً يحتاج إلى وضعه في دالة النطاق $E$، لهذا نعين له متغير ASP جديد ($X$ في القاعدة). يجب أن يكون لهذا المتغير مدى محدود، نبتكر اسماً جديداً لدالتنا ($l$ في القاعدة) ونستخدم محمول النطاق لتقييد $X$ إلى نطاق الدالة. الترجمة الناتجة $(t, B)$ تمثل صورة الدالة، لذا يتم إضافة القاعدة $\text{rule}_{\text{inter}}$ لربط تمثيل الدالة بتفسيرها.

**مثال 9.** $(\emptyset, \emptyset), (\lambda x. 2) \leadsto \{\text{inter}(((l, ()), X), 2) \leftarrow \text{domain}((l, ()), X)\}, ((l, ()), \emptyset)$

يمكن قراءة هذا كما يلي: ترجمة الدالة الثابتة إلى 2 في بيئة فارغة تمثل بالثابت $(l, ())$. تفسير $(l, ())$ عند تطبيقه على أي حد $X$ في نطاق $(l, ())$ هو 2.

**If zero-then-else**
$$\frac{(E, S), e_{\text{ifz}} \leadsto A_{\text{ifz}}, (t_{\text{ifz}}, B_{\text{ifz}}) \quad (E, B_{\text{ifz}} \cup \{t_{\text{ifz}} = 0\}), e_{\text{then}} \leadsto A_{\text{then}}, (t_{\text{then}}, B_{\text{then}}) \quad (E, B_{\text{ifz}} \cup \{t_{\text{ifz}} \neq 0\}), e_{\text{else}} \leadsto A_{\text{else}}, (t_{\text{else}}, B_{\text{else}})}{(E, S), \text{if } e_{\text{ifz}} \text{ then } e_{\text{then}} \text{ else } e_{\text{else}} \leadsto A_{\text{ite}} \cup \text{rule}_{\text{ite}}, (X, S \cup \text{body}_{\text{ite}})}$$
حيث:
- $X$ = متغير ASP جديد
- $\text{ite}$ = ثابت ASP جديد
- $\text{rule}_{\text{ite}} = \{\text{inter}((\text{ite}, \text{scope}_E), t_{\text{then}}) \leftarrow B_{\text{then}}, \text{inter}((\text{ite}, \text{scope}_E), t_{\text{else}}) \leftarrow B_{\text{else}}\}$
- $\text{body}_{\text{ite}} = \{\text{inter}((\text{ite}, \text{scope}_E), X)\}$
- $A_{\text{ite}} = A_{\text{ifz}} \cup A_{\text{then}} \cup A_{\text{else}}$

تتم ترجمة تعبيرات if zero باستخدام ترجمات تعبيراتها الفرعية الثلاثة. لكن نحتاج إلى تغيير الأمان للتأكد من أن جزء "then" يُقيّم فقط إذا كان جزء "if" يساوي 0 (والمثيل لجزء "else"). لبناء قيمة التعبير الكامل نعرّف رمزاً وسيطاً ($\text{ite}$ في القاعدة) لتمثيل اتحاد جزء "then" وجزء "else". لأن الأمان الإضافي ($= 0, \neq 0$) متعارض متبادل، واحد فقط من هذه الحدود سيكون له دلالة، لذا سيكون تفسير $\text{ite}$ فريداً.

**مثال 10.** ترجمة $(\lambda x. \text{ifz } x \text{ then succ else pred}) \, 2 \, 4$ مرئية في القائمة 3. الجزء الثابت محذوف. السطران 1 و 2 هما نتيجة ترجمة if zero-then-else. السطر 3 هو نتيجة ترجمة لامبدا. السطران 4 و 5 هما نتيجة التطبيق. وفي السطر 6 يمكن رؤية النتيجة النهائية. يمكن قراءة هذه القاعدة كما يلي: دع $X_2$ يكون تطبيق الدالة على 2. دع $X_3$ يكون تطبيق $X_2$ على 4. النتيجة النهائية هي $X_3$.

**القائمة 3:** ترجمة $(\lambda x. \text{ifz } x \text{ then succ else pred}) \, 2 \, 4$

```
1  inter((ite1, (X0)), succ) :- domain((l0, ()), X0), X0 = 0.
2  inter((ite1, (X0)), pred) :- domain((l0, ()), X0), X0 <> 0.
3  inter(((l0, ()), X0), X1) :- domain((l0, ()), X0), inter((ite1, (X0)), X1).
4  domain((l0, ()), 2).
5  domain(X2, 4) :- inter(((l0, ()), 2), X2).
6  result(X3) :- inter(((l0, ()), 2), X2), inter((X2, 4), X3).
   % الجزء الثابت المحذوف مرئي في القائمة 2
```

#### 4.5 التحسينات

خوارزمية الترجمة المعطاة في القسم السابق ليست ترجمة مثلى. الكثير من التحسينات ممكنة، على سبيل المثال، ليس كل المتغيرات في النطاق تحتاج إلى الوجود في $\text{scope}_E$، فقط تلك المستخدمة فعلياً في التعبير الفرعي. تطبيق هذه التحسينات يمكن أن يقلل بشكل كبير من حجم تأريض برنامج ASP. الإمكانيات هنا هي موضوعات بحثية مثيرة جداً للاهتمام، لكنها تُعتبر خارج نطاق هذا البحث.

#### 4.6 التطبيق

تم إنشاء تطبيق في Kotlin. وقت التشغيل يستخدم Clingo [9] لتشغيل ملفات ASP الناتجة، لكن المواصفات الناتجة يمكن استخدامها مع أي نظام متوافق مع ASP-Core-2 [2]. على https://dtai.cs.kuleuven.be/krr/pcf2asp يمكنك العثور على أداة يمكنك من خلالها تجربة الترجمة. يتم توفير بعض صيغ PCF المثالية، لكن يمكنك طلب ترجمات لصيغ PCF تعسفية ورؤية مجموعة إجاباتها المقابلة.

---

### Translation Notes

- **Figures referenced:** Listing 2, Listing 3 (code examples)
- **Key terms introduced:**
  - translation relation - علاقة الترجمة
  - soundness - سلامة
  - result-predicate - محمول النتيجة
  - inter-predicate - محمول inter
  - domain-predicate - محمول النطاق
  - magic set transformation - تحويل المجموعة السحرية
  - static preamble - المقدمة الثابتة
  - scoping - النطاقية
  - builtins - الدوال المدمجة
  - fixpoint - النقطة الثابتة
- **Equations:** Extensive use of inference rules and mathematical notation
- **Citations:** [2], [9], [13]
- **Special handling:**
  - Multiple code listings with ASP syntax preserved
  - Complex inference rules with proper LaTeX formatting
  - Translation relation notation $\leadsto$ preserved
  - Examples numbered consistently

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86

### Back-Translation Validation

Key paragraph: "In this section we explain the core of the translation mechanism. Section 4.1 defines the relationship between the translation and PCF semantics. Section 4.2 introduces some conventions that explain the structure of the resulting program. Finally, Section 4.3 explains the static part of the translation. Section 4.4 defines the translation relation between PCF expressions and the dynamic part of the translation."

The back-translation accurately captures the technical content and structure of this complex section.
