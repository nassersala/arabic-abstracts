# Section 3: Syntax of Mini Babel-17
## القسم 3: بنية Mini Babel-17 النحوية

**Section:** syntax
**Translation Quality:** 0.86
**Glossary Terms Used:** statement, expression, identifier, function, block, syntax

---

### English Version

Babel-17 [8] is a new dynamically-typed programming language in the making which is being developed by the author of this paper. One of its main features is that it combines purely functional programming and structured programming, building on the key observation that shadowing is purely functional. For illustration purposes we use a simplified version of a subset of Babel-17, which we call Mini Babel-17, as a proposal of how a purely functional structured programming language could look like. An implementation of Mini Babel-17 is available at [9].

A block in Mini Babel-17 is a sequence of statements:

```
block → statement₁
        ...
        statementₙ
```

Several statements within a single line are separated via semicolons. There are seven kinds of statements:

```
statement → val-statement
          | assign-statement
          | yield-statement
          | if-statement
          | while-statement
          | for-statement
          | block-statement

val-statement → val identifier = expression
val-assign-statement → identifier = expression
yield-statement → yield expression
if-statement → if simple-expression then block else block end
while-statement → while simple-expression do block end
for-statement → for identifier in simple-expression do block end
block-statement → begin block end
```

If the last statement of a block is a yield-statement, then the yield keyword may be dropped in that statement.

A simple-expression is an expression like it can be found in most other functional languages, i.e. it can be an integer, a boolean, an identifier, an anonymous function, function application, or some operation on expressions like function application, multiplication or comparison:

```
simple-expression →
    integer | boolean | identifier
  | identifier => expression
  | expression₁ expression₂
  | expression₁ * expression₂
  | expression₁ == expression₂
  ...
```

An expression is either a simple-expression or a statement:

```
expression → simple-expression
           | if-statement
           | while-statement
           | for-statement
           | block-statement
```

---

### النسخة العربية

Babel-17 [8] هي لغة برمجة جديدة ديناميكية النمط قيد التطوير من قبل مؤلف هذه الورقة. إحدى ميزاتها الرئيسية هي أنها تجمع بين البرمجة الوظيفية الصرفة والبرمجة المهيكلة، بناءً على الملاحظة الأساسية بأن التظليل وظيفي صرف. لأغراض التوضيح نستخدم نسخة مبسطة من مجموعة فرعية من Babel-17، والتي نسميها Mini Babel-17، كاقتراح لكيف يمكن أن تبدو لغة برمجة منظمة وظيفية صرفة. تتوفر تنفيذ لـ Mini Babel-17 على [9].

الكتلة في Mini Babel-17 هي تسلسل من العبارات:

```
block → statement₁
        ...
        statementₙ
```

يتم فصل عدة عبارات ضمن سطر واحد عبر الفواصل المنقوطة. هناك سبعة أنواع من العبارات:

```
statement → val-statement
          | assign-statement
          | yield-statement
          | if-statement
          | while-statement
          | for-statement
          | block-statement

val-statement → val identifier = expression
val-assign-statement → identifier = expression
yield-statement → yield expression
if-statement → if simple-expression then block else block end
while-statement → while simple-expression do block end
for-statement → for identifier in simple-expression do block end
block-statement → begin block end
```

إذا كانت العبارة الأخيرة من الكتلة هي yield-statement، فيمكن إسقاط الكلمة المفتاحية yield في تلك العبارة.

التعبير البسيط (simple-expression) هو تعبير كما يمكن العثور عليه في معظم اللغات الوظيفية الأخرى، أي يمكن أن يكون عدداً صحيحاً، أو قيمة منطقية، أو معرفاً، أو دالة مجهولة، أو تطبيق دالة، أو بعض العمليات على التعبيرات مثل تطبيق الدالة أو الضرب أو المقارنة:

```
simple-expression →
    integer | boolean | identifier
  | identifier => expression
  | expression₁ expression₂
  | expression₁ * expression₂
  | expression₁ == expression₂
  ...
```

التعبير إما أن يكون تعبيراً بسيطاً أو عبارة:

```
expression → simple-expression
           | if-statement
           | while-statement
           | for-statement
           | block-statement
```

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Block (كتلة)
  - Statement (عبارة)
  - Expression (تعبير)
  - Simple-expression (تعبير بسيط)
  - Identifier (معرّف)
  - Anonymous function (دالة مجهولة)
  - Function application (تطبيق دالة)
  - Dynamically-typed (ديناميكية النمط)
- **Equations:** Grammar production rules (BNF notation)
- **Citations:** [8] Babel-17, [9] Mini Babel-17 implementation
- **Special handling:**
  - Grammar notation preserved in English (BNF)
  - Keywords (val, yield, if, then, else, end, while, do, for, in, begin) kept in English
  - Subscripts preserved in mathematical notation

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
