# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** runtime, lazy programming language, memory usage, type system, resource analysis, compiler, intermediate representation

---

### English Version

It can be difficult to estimate the runtime costs of a program written in a lazy programming language. For example, consider the following two versions of a "repeat" function, which returns an infinite list with a given element:

```haskell
repeat x = let xs = x : xs in xs
it = repeat 1 :: [Int]

repeat' x = x : repeat' x
it' = repeat' 1 :: [Int]
```

To a novice, it may not be obvious that the memory usage of this function is constant for the first version and linear for the second version. To assist in detecting these differences, we want to automatically generate annotated types such as the following:

```
it : µX. {[] : (0, []) | (:) : (0, [T⁰(Int), T⁰(X)])}
it' : µX. {[] : (0, []) | (:) : (0, [T⁰(Int), T²(X)])}
```

In these types, the second field of the (:) constructor is wrapped in a thunk type that is annotated with costs 0 and 2, respectively. These values represent additional costs – in this case, memory allocations – that arise from accessing subsequent nodes of the linked list. As this cost is 0 in the type of the first version, this means that no additional allocations will take place and the list therefore requires constant space. For the second version, the value is greater than 0, indicating linear costs.

In this paper, we describe our implementation of a tool that can derive these annotated types automatically. Given a Haskell module, our tool will use the GHC compiler to parse the code and translate it into an intermediate representation which is more easy to analyze. We then apply our own custom type-based system on each expression to derive an annotated typing which depicts an upper bound on the number of resources required for evaluation. Depending on the cost model used, this can be used to approximate memory usage or runtime duration, for example.

This paper is a summary of the master's thesis "Implementation of an Automated Amortized Analysis on GHC Core as Compiler Plugin". [12] Note that sections of this paper may be similar or identical to that thesis.

---

### النسخة العربية

قد يكون من الصعب تقدير تكاليف وقت التشغيل لبرنامج مكتوب بلغة برمجة كسولة. على سبيل المثال، لننظر إلى النسختين التاليتين من دالة "repeat" التي تُرجع قائمة لا نهائية تحتوي على عنصر معين:

```haskell
repeat x = let xs = x : xs in xs
it = repeat 1 :: [Int]

repeat' x = x : repeat' x
it' = repeat' 1 :: [Int]
```

قد لا يكون واضحاً للمبتدئ أن استخدام الذاكرة لهذه الدالة ثابت للنسخة الأولى وخطي للنسخة الثانية. للمساعدة في اكتشاف هذه الفروقات، نريد توليد أنواع مُعلّمة تلقائياً مثل التالية:

```
it : µX. {[] : (0, []) | (:) : (0, [T⁰(Int), T⁰(X)])}
it' : µX. {[] : (0, []) | (:) : (0, [T⁰(Int), T²(X)])}
```

في هذه الأنواع، يتم تغليف الحقل الثاني من المُنشئ (:) في نوع ثانك (thunk) مُعلّم بتكاليف 0 و 2 على التوالي. تمثل هذه القيم تكاليف إضافية - في هذه الحالة، تخصيصات الذاكرة - التي تنشأ من الوصول إلى العقد اللاحقة في القائمة المترابطة. نظراً لأن هذه التكلفة تساوي 0 في نوع النسخة الأولى، فهذا يعني أنه لن تحدث تخصيصات إضافية وبالتالي تتطلب القائمة مساحة ثابتة. بالنسبة للنسخة الثانية، القيمة أكبر من 0، مما يشير إلى تكاليف خطية.

في هذه الورقة، نصف تطبيقنا لأداة يمكنها اشتقاق هذه الأنواع المُعلّمة تلقائياً. بالنظر إلى وحدة Haskell، ستستخدم أداتنا مترجم GHC لتحليل الشفرة وترجمتها إلى تمثيل وسيط أسهل للتحليل. ثم نطبق نظامنا المخصص القائم على الأنواع على كل تعبير لاشتقاق نوع مُعلّم يُظهر حداً أعلى على عدد الموارد المطلوبة للتقييم. اعتماداً على نموذج التكلفة المستخدم، يمكن استخدام ذلك لتقريب استخدام الذاكرة أو مدة وقت التشغيل، على سبيل المثال.

هذه الورقة هي ملخص لرسالة الماجستير "تطبيق تحليل مطفأ آلي على GHC Core كإضافة للمترجم". [12] لاحظ أن أقساماً من هذه الورقة قد تكون مشابهة أو متطابقة مع تلك الرسالة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - lazy programming language (لغة برمجة كسولة)
  - infinite list (قائمة لا نهائية)
  - annotated types (أنواع مُعلّمة)
  - thunk type (نوع ثانك)
  - memory allocations (تخصيصات الذاكرة)
  - linked list (قائمة مترابطة)
  - intermediate representation (تمثيل وسيط)
  - cost model (نموذج التكلفة)
- **Equations:** Type annotations with µX notation
- **Citations:** [12]
- **Special handling:**
  - Code examples kept in English (Haskell syntax)
  - Mathematical type notation preserved
  - "thunk" kept in transliteration as it's a specialized technical term

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-Translation (First & Last Paragraphs)

**First paragraph:** It may be difficult to estimate runtime costs for a program written in a lazy programming language. For example, let's look at the following two versions of a "repeat" function that returns an infinite list containing a given element:

**Last paragraph:** This paper is a summary of the master's thesis "Implementation of an Automated Amortized Analysis on GHC Core as Compiler Plugin". [12] Note that sections of this paper may be similar or identical to that thesis.
