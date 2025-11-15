# Section 5: Examples
## القسم 5: أمثلة

**Section:** Examples
**Translation Quality:** 0.86
**Glossary Terms Used:** automatic differentiation, compiler, derivative, linear map

---

### English Version

Examples

Let's now look at some AD examples, to which we will return later in the paper:

```haskell
sqr :: Num a => a -> a
sqr a = a · a

magSqr :: Num a => a × a -> a
magSqr (a, b) = sqr a + sqr b

cosSinProd :: Floating a => a × a -> a × a
cosSinProd (x, y) = (cos z, sin z) where z = x · y
```

A compiler plugin converts these definitions to categorical vocabulary [Elliott, 2017]:

```haskell
sqr = mulC ◦ (id ▵ id)
magSqr = addC ◦ (mulC ◦ (exl ▵ exl) ▵ mulC ◦ (exr ▵ exr))
cosSinProd = (cosC ▵ sinC) ◦ mulC
```

To visualize computations before differentiation, we can interpret these categorical expressions in a category of graphs [Elliott, 2017, Section 7], with the results rendered in Figures 2 and 3. To see the differentiable versions, interpret these same expressions in the category of differentiable functions (D from Section 4.1), remove the D constructors to reveal the function representation, convert these functions to categorical form as well, and finally interpret the result in the graph category. The results are rendered in Figures 4 and 5. Some remarks:

- The derivatives are (linear) functions, as depicted in boxes.
- Work is shared between the function's result (sometimes called the "primal") and its derivative in Figure 5.
- The graphs shown here are used solely for visualizing functions before and after differentiation, playing no role in the programming interface or in the implementation of differentiation.

---

### النسخة العربية

أمثلة

لننظر الآن في بعض أمثلة التفاضل الآلي، التي سنعود إليها لاحقاً في الورقة:

```haskell
sqr :: Num a => a -> a
sqr a = a · a

magSqr :: Num a => a × a -> a
magSqr (a, b) = sqr a + sqr b

cosSinProd :: Floating a => a × a -> a × a
cosSinProd (x, y) = (cos z, sin z) where z = x · y
```

يحول مكون إضافي للمترجم هذه التعريفات إلى مفردات فئوية [Elliott, 2017]:

```haskell
sqr = mulC ◦ (id ▵ id)
magSqr = addC ◦ (mulC ◦ (exl ▵ exl) ▵ mulC ◦ (exr ▵ exr))
cosSinProd = (cosC ▵ sinC) ◦ mulC
```

لتصور الحسابات قبل التفاضل، يمكننا تفسير هذه التعبيرات الفئوية في فئة من الرسوم البيانية [Elliott, 2017, Section 7]، مع عرض النتائج في الشكلين 2 و 3. لرؤية النسخ القابلة للتفاضل، فسر هذه التعبيرات نفسها في فئة الدوال القابلة للتفاضل (D من القسم 4.1)، أزل منشئات D للكشف عن تمثيل الدالة، حول هذه الدوال إلى شكل فئوي أيضاً، وأخيراً فسر النتيجة في فئة الرسم البياني. تظهر النتائج في الشكلين 4 و 5. بعض الملاحظات:

- المشتقات هي دوال (خطية)، كما هو موضح في الصناديق.
- يتم مشاركة العمل بين نتيجة الدالة (تسمى أحياناً "الأولية") ومشتقتها في الشكل 5.
- الرسوم البيانية المعروضة هنا تُستخدم فقط لتصور الدوال قبل وبعد التفاضل، ولا تلعب أي دور في واجهة البرمجة أو في تنفيذ التفاضل.

---

### Translation Notes

- **Figures referenced:** Figures 2, 3, 4, 5 (visualization of computations and derivatives)
- **Key terms:** compiler plugin, categorical vocabulary, primal, derivative functions
- **Code examples:** 3 Haskell function definitions with categorical transformations
- **Citations:** [Elliott 2017]

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
