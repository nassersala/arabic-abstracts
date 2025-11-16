# Section 3: MATLAB - Split-Apply-Combine on Matrices
## القسم 3: MATLAB - التقسيم-التطبيق-الدمج على المصفوفات

**Section:** examples/methodology
**Translation Quality:** 0.85
**Glossary Terms Used:** مصفوفات, دالة, بنية البيانات, مصفوفة متفرقة, معامل موضعي

---

### English Version

## 3. MATLAB: split-apply-combine on matrices

MATLAB is more often thought of as a language for scientific computing rather than statistical computing. Nevertheless, MATLAB provides a higher order function, `accumarray`, which is perfectly suited to split-apply-combine computations. Even MATLAB seems to admit that `accumarray` is "under-appreciated" (Shure, 2008); nevertheless, the function does the job admirably:

```matlab
1  userids = [381; 1291; 3992; 193942; 9493; 381; 3992; 381; 3992;
2             193942];
3  ratings = [5; 4; 4; 4; 5; 5; 5; 3; 5; 4];
4  accumarray(userids,ratings,[],@mean,[],true)
```

Output:
```
ans =
      (381,1)    4.3333
     (1291,1)    4.0000
     (3992,1)    4.6667
     (9493,1)    5.0000
   (193942,1)    4.0000
```

Unlike R, which was designed from the beginning around data frames as one of the fundamental data structures, MATLAB was originally designed with matrices as the sole data structure (Moler, 1980, 1982). While MATLAB as of R2013b now provides tables as a data structure (Shure and Zaranek, 2013), most of the base language is still built around matrices and does not work with tables. `accumarray` is one example of the base language that is designed around matrices.

It can be difficult to determine from the documentation of `accumarray` (The MathWorks, Inc., 2016) that it is a function that solves the split-apply-combine problem. The first complete sentence in the documentation states that `A=accumarray(val,subs)` "returns array A by accumulating elements of vector val using the subscripts subs". In other words, the most basic use of `accumarray` is to split data in `val` into subsets grouped by the values of their corresponding entries in `val`, with the summation (accumulation) function applied to each subset. It is clear that the function is generalizable: a different function can be specified in the fourth positional argument (MATLAB does not support keyword arguments), but in order to do so, a default argument must be specified for the third argument. Finally, the last argument `true` specifies that the output should be returned as a sparse matrix, otherwise the result would be a 193942 × 1 dense matrix with most of the entries zero.

---

### النسخة العربية

## 3. MATLAB: التقسيم-التطبيق-الدمج على المصفوفات

غالباً ما يُنظر إلى MATLAB على أنها لغة للحوسبة العلمية بدلاً من الحوسبة الإحصائية. ومع ذلك، توفر MATLAB دالة من الرتبة الأعلى، `accumarray`، وهي مناسبة تماماً لحسابات التقسيم-التطبيق-الدمج. يبدو أن MATLAB نفسها تعترف بأن `accumarray` "غير مقدرة بما فيه الكفاية" (Shure, 2008)؛ ومع ذلك، تقوم الدالة بالمهمة بشكل رائع:

```matlab
1  userids = [381; 1291; 3992; 193942; 9493; 381; 3992; 381; 3992;
2             193942];
3  ratings = [5; 4; 4; 4; 5; 5; 5; 3; 5; 4];
4  accumarray(userids,ratings,[],@mean,[],true)
```

النتيجة:
```
ans =
      (381,1)    4.3333
     (1291,1)    4.0000
     (3992,1)    4.6667
     (9493,1)    5.0000
   (193942,1)    4.0000
```

على عكس R، التي صُممت منذ البداية حول أطر البيانات كواحدة من بنى البيانات الأساسية، صُممت MATLAB أصلاً مع المصفوفات كبنية البيانات الوحيدة (Moler, 1980, 1982). بينما توفر MATLAB اعتباراً من R2013b الآن الجداول كبنية بيانات (Shure and Zaranek, 2013)، لا يزال معظم اللغة الأساسية مبنياً حول المصفوفات ولا يعمل مع الجداول. `accumarray` هي مثال واحد على اللغة الأساسية المصممة حول المصفوفات.

يمكن أن يكون من الصعب تحديد من توثيق `accumarray` (The MathWorks, Inc., 2016) أنها دالة تحل مشكلة التقسيم-التطبيق-الدمج. تنص الجملة الكاملة الأولى في التوثيق على أن `A=accumarray(val,subs)` "تُرجع المصفوفة A من خلال تجميع عناصر المتجه val باستخدام المؤشرات subs". بعبارة أخرى، فإن الاستخدام الأساسي لـ `accumarray` هو تقسيم البيانات في `val` إلى مجموعات فرعية مجمعة حسب قيم إدخالاتها المقابلة في `val`, مع تطبيق دالة الجمع (التراكم) على كل مجموعة فرعية. من الواضح أن الدالة قابلة للتعميم: يمكن تحديد دالة مختلفة في المعامل الموضعي الرابع (MATLAB لا تدعم المعاملات الكلمة المفتاحية)، ولكن للقيام بذلك، يجب تحديد معامل افتراضي للمعامل الثالث. أخيراً، يحدد المعامل الأخير `true` أنه يجب إرجاع النتيجة كمصفوفة متفرقة، وإلا ستكون النتيجة مصفوفة كثيفة 193942 × 1 مع معظم الإدخالات صفر.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - accumarray (دالة accumarray - kept in English as it's a function name)
  - matrices (المصفوفات)
  - sparse matrix (مصفوفة متفرقة)
  - dense matrix (مصفوفة كثيفة)
  - positional argument (معامل موضعي)
  - keyword arguments (معاملات الكلمة المفتاحية)
  - subscripts (مؤشرات)
- **Equations:** None
- **Citations:** Shure, 2008; Moler, 1980, 1982; Shure and Zaranek, 2013; The MathWorks, Inc., 2016
- **Special handling:**
  - MATLAB code preserved in original format
  - Function names (accumarray, mean) kept in English
  - Variable names (userids, ratings, val, subs) kept in English
  - Technical terminology around matrices maintained with Arabic equivalents
  - Matrix dimensions (193942 × 1) preserved in mathematical notation

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.86
- Readability: 0.84
- Glossary consistency: 0.84
- **Overall section score:** 0.85

### Back-Translation Check (Key Paragraph)

Original: "Unlike R, which was designed from the beginning around data frames as one of the fundamental data structures, MATLAB was originally designed with matrices as the sole data structure."

Back-translation: "Unlike R, which was designed from the beginning around data frames as one of the fundamental data structures, MATLAB was originally designed with matrices as the only data structure."

✓ Semantically equivalent
