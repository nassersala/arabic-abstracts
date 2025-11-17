# Section 4: Compiler Implementation
## القسم 4: تنفيذ المترجم

**Section:** compiler-implementation
**Translation Quality:** 0.86
**Glossary Terms Used:** grammar, parser, lexer, expression, function declaration, parse tree

---

### English Version

The following subset of Haskell grammar is part of HTCC compiler code. Here, functions are divided into declarations (dcFun) and definitions (dFun):

```
PROG : STAT+;
STAT : dcFun;

dcFun : ID '::' formalType('->')* NL+ dFun;

expr : expr op = ('*'|'/')(DIGIT|expr)
      |expr op = ('.&.'|'.||.')(DIGIT|expr)
      |expr op = ('+'|'−')(DIGIT|expr)
      |('xor' expr DIGIT)
      |('shiftL' expr DIGIT)
      |('shiftR' expr DIGIT)
      |mPassing(mPassing)*
      |expr mPassing
      |ID*
```

According to the proposed grammar an expression (expr) has multiple meanings that captures the definition of the function. expr can be any arithmetic or logic operation between two or more variables. In addition, an expression expr can call other functions that take place at mPassing node. Figure 7 demonstrates the parse tree of the following function:

```haskell
f :: Int → Int
f x = x + 3
```

A subset of the lexer grammar is as following:

```
ID : [a-zA-Z]+ [0-9]*;
NL : '\r'? '\n';
ARROW : '->' | '→';
WS : [\t]+ → SKIP;
DIGIT : [0-9]+;
COMMENT : '--' .*? '\r'? '\n' → SKIP;
```

---

### النسخة العربية

المجموعة الفرعية التالية من قواعد Haskell هي جزء من كود مترجم HTCC. هنا، يتم تقسيم الدوال إلى تصريحات (dcFun) وتعريفات (dFun):

```
PROG : STAT+;
STAT : dcFun;

dcFun : ID '::' formalType('->')* NL+ dFun;

expr : expr op = ('*'|'/')(DIGIT|expr)
      |expr op = ('.&.'|'.||.')(DIGIT|expr)
      |expr op = ('+'|'−')(DIGIT|expr)
      |('xor' expr DIGIT)
      |('shiftL' expr DIGIT)
      |('shiftR' expr DIGIT)
      |mPassing(mPassing)*
      |expr mPassing
      |ID*
```

وفقاً للقواعد المقترحة، فإن التعبير (expr) له معانٍ متعددة تلتقط تعريف الدالة. يمكن أن يكون expr أي عملية حسابية أو منطقية بين متغيرين أو أكثر. بالإضافة إلى ذلك، يمكن للتعبير expr استدعاء دوال أخرى تحدث عند عقدة mPassing. يوضح الشكل 7 شجرة التحليل للدالة التالية:

```haskell
f :: Int → Int
f x = x + 3
```

مجموعة فرعية من قواعد المحلل المعجمي كما يلي:

```
ID : [a-zA-Z]+ [0-9]*;
NL : '\r'? '\n';
ARROW : '->' | '→';
WS : [\t]+ → SKIP;
DIGIT : [0-9]+;
COMMENT : '--' .*? '\r'? '\n' → SKIP;
```

---

### Translation Notes

- **Figures referenced:** Figure 7 (The parse tree of function f)
- **Key terms introduced:** dcFun, dFun, mPassing, expr, PROG, STAT
- **Equations:** 0
- **Citations:** 0
- **Special handling:**
  - Grammar specifications kept in English (standard practice)
  - Code examples kept in original format
  - Technical notation preserved (::, ->, |, etc.)

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.85
- **Overall section score:** 0.86

### Back-Translation Check (Key Paragraph)

According to the proposed grammar, an expression (expr) has multiple meanings that capture the definition of the function. expr can be any arithmetic or logical operation between two or more variables. Additionally, an expression expr can call other functions that occur at the mPassing node. Figure 7 demonstrates the parse tree of the following function.

**Quality Assessment:** The back-translation accurately conveys the technical content (0.86).
