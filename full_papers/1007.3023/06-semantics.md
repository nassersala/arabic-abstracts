# Section 6: Semantics of Mini Babel-17
## القسم 6: دلالات Mini Babel-17

**Section:** semantics
**Translation Quality:** 0.85
**Glossary Terms Used:** operational semantics, interpreter, datatype, environment, evaluation function, reference cell

---

### English Version

In this section we define an operational semantics for Mini Babel-17 by building a Mini Babel-17 interpreter written in Standard ML¹.

First we represent the grammar of Mini Babel-17 as SML datatypes:

```sml
datatype block = Block of statement list
and statement =
    SVal of identifier * expression
  | SAssign of identifier * expression
  | SYield of expression
  | SIf of simple_expression * block * block
  | SWhile of simple_expression * block
  | SFor of identifier * simple_expression * block
  | SBlock of block
and expression =
    ESimple of simple_expression
  | EBlock of statement
and simple_expression =
    EInt of int | EBool of bool | EId of identifier
  | EFun of identifier * expression
  | EBinOp of (value * value -> value) *
              expression * expression
and identifier = Id of string
```

Note that function application, multiplication, comparison and so on are all described via the EBinOp constructor by providing a suitable parameter of type `value * value -> value`. The type value represents all values that can be the result of evaluating a Mini Babel-17 program:

```sml
datatype value = VBool of bool | VInt of int
               | VFun of value -> value
               | VList of value list
```

Mini Babel-17 wants to be both purely functional and structured; the most important ingredients of a purely functional program are expressions; the most important ingredients of an SP program are blocks and statements. This dilemma is resolved by treating statements as special expressions.

The interpreter defines the following evaluation functions:

```sml
eval_b  : environment -> block -> environment * value list
eval_st : environment -> statement -> environment * value list
eval_e  : environment -> expression -> value
eval_se : environment -> simple_expression -> value
```

The evaluation of blocks and statements yields lists of values instead of single values, the block

```
begin yield 1; yield 2; 3 end
```

for example evaluates to `[1, 2, 3]`.

Consider the following Mini Babel-17 program:

```
val x = 0
begin x = 1; x end * begin val x = x + 2; x end
```

It does not obey the linear scoping rules of Mini Babel-17 because x is not in linear scope in the val-assign-statement `x = 1`. In such a situation, the exception Illformed is raised during evaluation. Furthermore, an exception TypeError is raised when for example the condition of an if-statement evaluates to a list instead of a boolean. Note by the way that the program

```
val x = 0
begin val x = 1; x end * begin val x = x + 2; x end
```

is perfectly fine and evaluates to 2.

What does the environment look like? It is actually split into two parts, one part for those identifiers that have linear scope, and one part for identifiers that don't. The nonlinear part is a mapping from identifiers to values, the linear part a mapping from identifiers to reference cells of values. Both parts can be described by the polymorphic type 'a idmap:

```sml
type idmap = (string * 'a) list
fun lookup [] = raise Illformed
  | lookup ((t, x):: r) (Id s) =
      if t = s then x else lookup r (Id s)
fun remove [] = []
  | remove ((t,x):: r) (Id s) =
      if t = s then r else remove r (Id s)
fun insert m ((Id s), x) = (s,x)::(remove m (Id s))
```

The type of environments is then introduced as follows:

```sml
type environment = value idmap * (value ref) idmap
fun deref [] = []
  | deref ((s, vr):: m) = ((s,!vr)::(deref m))
fun freeze (nonlinear, linear) = (nonlinear@(deref linear), [])
fun bind (nonlinear, linear) (id,value) =
  (remove nonlinear id, insert linear (id, ref value))
fun rebind (env as (_, linear)) (id, value) =
  (lookup linear id := value; env)
```

Note that `bind` returns a new environment, and `rebind` returns the same environment with a mutated linear part. The function `freeze` turns all mutable linear bindings into immutable nonlinear ones.

Now we can give the definition of all evaluation functions:

```sml
fun eval_b env (Block []) = (env, [])
  | eval_b env (Block (s :: r)) =
      let
        val (env', values_s) = eval_st env s
        val (env'', values_r) = eval_b env' (Block r)
      in (env'', values_s @ values_r) end
and eval_nestedb env b =
      let
        val (_, values) = eval_b env b
      in (env, values) end
and eval_st env (SVal (id, e)) =
      let
        val value = eval_e env e
      in (bind env (id, value), []) end
  | eval_st env (SAssign (id, e)) =
      let
        val value = eval_e env e
      in (rebind env (id, value), []) end
  | eval_st env (SYield e) =
      let
        val value = eval_e env e
      in (env, [value]) end
  | eval_st env (SBlock b) = eval_nestedb env b
  | eval_st env (SIf (cond, yes, no)) =
      (case eval_se env cond of
         VBool true => eval_nestedb env yes
       | VBool false => eval_nestedb env no
       | _ => raise TypeError)
  | eval_st env (loop as SWhile (cond, body)) =
      (case eval_se env cond of
         VBool true =>
           let
             val (_, values_1) = eval_b env body
             val (_, values_2) = eval_st env loop
           in (env, values_1 @ values_2) end
       | VBool false => (env, [])
       | _ => raise TypeError)
  | eval_st env (SFor (id, list, body)) =
      (case eval_se env list of
         VList L => eval_for env id body L
       | _ => raise TypeError)
and eval_for env id body [] = (env, [])
  | eval_for env id body (x::xs) =
      let
        val (_, values_1) = eval_b (bind env (id,x)) body
        val (_, values_2) = eval_for env id body xs
      in (env, values_1@values_2) end
and eval_e env (ESimple se) = eval_se env se
  | eval_e env (EBlock s) =
      (case eval_b env (Block [s]) of
         (_, [a]) => a
       | (_, L) => VList L)
and eval_se env se = eval_simple (freeze env) se
and eval_simple env (EInt i) = VInt i
  | eval_simple env (EBool b) = VBool b
  | eval_simple env (EBinOp (f, a, b)) =
      f (eval_e env a, eval_e env b)
  | eval_simple (nonlinear, _) (EId id) =
      lookup nonlinear id
  | eval_simple env (EFun (id, body)) =
      VFun (fn value =>
              eval_e (bind env (id, value)) body)
```

Here is the evaluation function that computes the meaning of a Mini Babel-17 program, i.e. of a block:

```sml
eval : block -> value
fun eval prog = snd (eval_e ([], []) (EBlock (SBlock prog)))
```

It is straightforward how to extract from above evaluation functions a well-formedness criterion such that if a Mini Babel-17 program is statically checked to be well-formed according to that criterion, no Illformed exception will be raised during the evaluation of the program:

```sml
val VALUE = VInt 0
fun check_b env (Block []) = env
  | check_b env (Block (s :: r)) =
      check_b (check_st env s) (Block r)
and check_st env (SVal (id, e)) =
      (check_e env e; bind env (id, VALUE))
  | check_st env (SAssign (id, e)) =
      (check_e env e; rebind env (id, VALUE))
  | check_st env (SYield e) = (check_e env e; env)
  | check_st env (SBlock b) = (check_b env b; env)
  | check_st env (SIf (cond, yes, no)) =
      (check_se env cond;
       check_b env yes; check_b env no; env)
  | check_st env (loop as SWhile (cond, body)) =
      (check_se env cond; check_b env body; env)
  | check_st env (SFor (id, list, body)) =
      (check_se env list;
       check_b (bind env (id, VALUE)) body; env)
and check_e env (ESimple se) = check_se env se
  | check_e env (EBlock s) =
      (check_b env (Block [s]); ())
and check_se env se = check_simple (freeze env) se
and check_simple env (EInt i) = ()
  | check_simple env (EBool b) = ()
  | check_simple env (EBinOp (f, a, b)) =
      (check_e env a; check_e env b)
  | check_simple (nonlinear, _) (EId id) =
      (lookup nonlinear id; ())
  | check_simple env (EFun (id, body)) =
      check_e (bind env (id, VALUE)) body
fun check prog = check_e ([], []) (EBlock (SBlock prog))
```

The function `check` terminates because it is basically defined via primitive recursion on the structure of the program. Furthermore, the set of calls to `lookup` generated during an execution of `check prog` is clearly a superset of the set of calls to `lookup` generated during the execution of `eval prog`. Therefore, if `check prog` does not raise an exception Illformed, then neither will `eval prog`.

---

¹ The original SML sources of the interpreter and all Mini Babel-17 programs of this paper are available online [8].

---

### النسخة العربية

في هذا القسم نعرّف دلالات تشغيلية لـ Mini Babel-17 عن طريق بناء مفسر Mini Babel-17 مكتوب بـ Standard ML¹.

أولاً نمثل قواعد Mini Babel-17 كأنواع بيانات SML:

```sml
datatype block = Block of statement list
and statement =
    SVal of identifier * expression
  | SAssign of identifier * expression
  | SYield of expression
  | SIf of simple_expression * block * block
  | SWhile of simple_expression * block
  | SFor of identifier * simple_expression * block
  | SBlock of block
and expression =
    ESimple of simple_expression
  | EBlock of statement
and simple_expression =
    EInt of int | EBool of bool | EId of identifier
  | EFun of identifier * expression
  | EBinOp of (value * value -> value) *
              expression * expression
and identifier = Id of string
```

لاحظ أن تطبيق الدالة، والضرب، والمقارنة وما إلى ذلك كلها موصوفة عبر المُنشئ EBinOp من خلال توفير معامل مناسب من النوع `value * value -> value`. النوع value يمثل جميع القيم التي يمكن أن تكون نتيجة تقييم برنامج Mini Babel-17:

```sml
datatype value = VBool of bool | VInt of int
               | VFun of value -> value
               | VList of value list
```

Mini Babel-17 تريد أن تكون وظيفية صرفة ومهيكلة في آن واحد؛ المكونات الأكثر أهمية لبرنامج وظيفي صرف هي التعبيرات؛ والمكونات الأكثر أهمية لبرنامج برمجة مهيكلة هي الكتل والعبارات. تُحل هذه المعضلة بمعاملة العبارات كتعبيرات خاصة.

يعرّف المفسر دوال التقييم التالية:

```sml
eval_b  : environment -> block -> environment * value list
eval_st : environment -> statement -> environment * value list
eval_e  : environment -> expression -> value
eval_se : environment -> simple_expression -> value
```

تقييم الكتل والعبارات يُنتج قوائم من القيم بدلاً من قيم مفردة، الكتلة

```
begin yield 1; yield 2; 3 end
```

على سبيل المثال تُقيّم إلى `[1, 2, 3]`.

اعتبر برنامج Mini Babel-17 التالي:

```
val x = 0
begin x = 1; x end * begin val x = x + 2; x end
```

إنه لا يطيع قواعد النطاق الخطي لـ Mini Babel-17 لأن x ليس في نطاق خطي في عبارة الإسناد val `x = 1`. في مثل هذا الموقف، يُثار الاستثناء Illformed أثناء التقييم. علاوة على ذلك، يُثار استثناء TypeError عندما، على سبيل المثال، يُقيّم شرط عبارة if إلى قائمة بدلاً من قيمة منطقية. لاحظ بالمناسبة أن البرنامج

```
val x = 0
begin val x = 1; x end * begin val x = x + 2; x end
```

صحيح تماماً ويُقيّم إلى 2.

كيف تبدو البيئة؟ إنها في الواقع مقسمة إلى جزأين، جزء واحد للمعرّفات التي لها نطاق خطي، وجزء واحد للمعرّفات التي ليس لها ذلك. الجزء غير الخطي هو تعيين من المعرّفات إلى القيم، الجزء الخطي هو تعيين من المعرّفات إلى خلايا مرجعية من القيم. يمكن وصف كلا الجزأين بالنوع متعدد الأشكال 'a idmap:

```sml
type idmap = (string * 'a) list
fun lookup [] = raise Illformed
  | lookup ((t, x):: r) (Id s) =
      if t = s then x else lookup r (Id s)
fun remove [] = []
  | remove ((t,x):: r) (Id s) =
      if t = s then r else remove r (Id s)
fun insert m ((Id s), x) = (s,x)::(remove m (Id s))
```

نوع البيئات يُقدّم حينئذٍ على النحو التالي:

```sml
type environment = value idmap * (value ref) idmap
fun deref [] = []
  | deref ((s, vr):: m) = ((s,!vr)::(deref m))
fun freeze (nonlinear, linear) = (nonlinear@(deref linear), [])
fun bind (nonlinear, linear) (id,value) =
  (remove nonlinear id, insert linear (id, ref value))
fun rebind (env as (_, linear)) (id, value) =
  (lookup linear id := value; env)
```

لاحظ أن `bind` تُعيد بيئة جديدة، و `rebind` تُعيد نفس البيئة مع جزء خطي متحول. الدالة `freeze` تحول جميع الارتباطات الخطية القابلة للتغيير إلى ارتباطات غير خطية غير قابلة للتغيير.

الآن يمكننا إعطاء تعريف جميع دوال التقييم:

```sml
fun eval_b env (Block []) = (env, [])
  | eval_b env (Block (s :: r)) =
      let
        val (env', values_s) = eval_st env s
        val (env'', values_r) = eval_b env' (Block r)
      in (env'', values_s @ values_r) end
and eval_nestedb env b =
      let
        val (_, values) = eval_b env b
      in (env, values) end
and eval_st env (SVal (id, e)) =
      let
        val value = eval_e env e
      in (bind env (id, value), []) end
  | eval_st env (SAssign (id, e)) =
      let
        val value = eval_e env e
      in (rebind env (id, value), []) end
  | eval_st env (SYield e) =
      let
        val value = eval_e env e
      in (env, [value]) end
  | eval_st env (SBlock b) = eval_nestedb env b
  | eval_st env (SIf (cond, yes, no)) =
      (case eval_se env cond of
         VBool true => eval_nestedb env yes
       | VBool false => eval_nestedb env no
       | _ => raise TypeError)
  | eval_st env (loop as SWhile (cond, body)) =
      (case eval_se env cond of
         VBool true =>
           let
             val (_, values_1) = eval_b env body
             val (_, values_2) = eval_st env loop
           in (env, values_1 @ values_2) end
       | VBool false => (env, [])
       | _ => raise TypeError)
  | eval_st env (SFor (id, list, body)) =
      (case eval_se env list of
         VList L => eval_for env id body L
       | _ => raise TypeError)
and eval_for env id body [] = (env, [])
  | eval_for env id body (x::xs) =
      let
        val (_, values_1) = eval_b (bind env (id,x)) body
        val (_, values_2) = eval_for env id body xs
      in (env, values_1@values_2) end
and eval_e env (ESimple se) = eval_se env se
  | eval_e env (EBlock s) =
      (case eval_b env (Block [s]) of
         (_, [a]) => a
       | (_, L) => VList L)
and eval_se env se = eval_simple (freeze env) se
and eval_simple env (EInt i) = VInt i
  | eval_simple env (EBool b) = VBool b
  | eval_simple env (EBinOp (f, a, b)) =
      f (eval_e env a, eval_e env b)
  | eval_simple (nonlinear, _) (EId id) =
      lookup nonlinear id
  | eval_simple env (EFun (id, body)) =
      VFun (fn value =>
              eval_e (bind env (id, value)) body)
```

فيما يلي دالة التقييم التي تحسب معنى برنامج Mini Babel-17، أي كتلة:

```sml
eval : block -> value
fun eval prog = snd (eval_e ([], []) (EBlock (SBlock prog)))
```

من المباشر كيفية استخراج معيار حسن التشكل من دوال التقييم أعلاه بحيث إذا تم فحص برنامج Mini Babel-17 بشكل ثابت ليكون حسن التشكل وفقاً لهذا المعيار، لن يُثار أي استثناء Illformed أثناء تقييم البرنامج:

```sml
val VALUE = VInt 0
fun check_b env (Block []) = env
  | check_b env (Block (s :: r)) =
      check_b (check_st env s) (Block r)
and check_st env (SVal (id, e)) =
      (check_e env e; bind env (id, VALUE))
  | check_st env (SAssign (id, e)) =
      (check_e env e; rebind env (id, VALUE))
  | check_st env (SYield e) = (check_e env e; env)
  | check_st env (SBlock b) = (check_b env b; env)
  | check_st env (SIf (cond, yes, no)) =
      (check_se env cond;
       check_b env yes; check_b env no; env)
  | check_st env (loop as SWhile (cond, body)) =
      (check_se env cond; check_b env body; env)
  | check_st env (SFor (id, list, body)) =
      (check_se env list;
       check_b (bind env (id, VALUE)) body; env)
and check_e env (ESimple se) = check_se env se
  | check_e env (EBlock s) =
      (check_b env (Block [s]); ())
and check_se env se = check_simple (freeze env) se
and check_simple env (EInt i) = ()
  | check_simple env (EBool b) = ()
  | check_simple env (EBinOp (f, a, b)) =
      (check_e env a; check_e env b)
  | check_simple (nonlinear, _) (EId id) =
      (lookup nonlinear id; ())
  | check_simple env (EFun (id, body)) =
      check_e (bind env (id, VALUE)) body
fun check prog = check_e ([], []) (EBlock (SBlock prog))
```

الدالة `check` تنتهي لأنها معرّفة أساساً عبر العودية البدائية على بنية البرنامج. علاوة على ذلك، مجموعة الاستدعاءات لـ `lookup` المُولّدة أثناء تنفيذ `check prog` هي بوضوح مجموعة شاملة لمجموعة الاستدعاءات لـ `lookup` المُولّدة أثناء تنفيذ `eval prog`. لذلك، إذا لم يُثِر `check prog` استثناءً Illformed، فلن يُثيره `eval prog` أيضاً.

---

¹ شفرات SML الأصلية للمفسر وجميع برامج Mini Babel-17 في هذه الورقة متاحة على الإنترنت [8].

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Operational semantics (دلالات تشغيلية)
  - Interpreter (مفسر)
  - Datatype (نوع بيانات)
  - Environment (بيئة)
  - Evaluation function (دالة تقييم)
  - Reference cell (خلية مرجعية)
  - Well-formedness (حسن التشكل)
  - Primitive recursion (العودية البدائية)
  - Polymorphic type (نوع متعدد الأشكال)
- **Equations:** Type signatures in SML
- **Citations:** [8] Babel-17 (source code available online)
- **Special handling:**
  - All SML code blocks preserved exactly as in original
  - Function names and keywords in code kept in English
  - Comments and descriptions translated to Arabic

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.85
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.85
