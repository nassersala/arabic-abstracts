# Section 2: Everything is an Array
## القسم 2: كل شيء هو مصفوفة

**Section:** arrays-and-basics
**Translation Quality:** 0.86
**Glossary Terms Used:** مصفوفة, رتبة, شكل, ذرة, متجه, مصفوفة مستطيلة, خلية, إطار

---

### English Version

In rank-polymorphic languages such as Remora, all values are arrays. That is, every Remora expression evaluates to an array. An array is a collection of data arranged in a hyper-rectangle of some given dimensionality. Every array comes with its constituent elements, and a shape. Array elements come from a separate universe of atoms; typical atoms are numbers, characters, booleans and functions. Permitting arrays of functions means that Remora is a higher-order functional language.

For example, consider a matrix that has two rows and three columns of integers:
```
7 1 2
2 0 5
```

We say that this matrix has rank 2—that is, it has two dimensions or axes of indexing—and shape [2, 3]. The shape of an array is a sequence (or, equivalently, list or vector) giving its dimensions.

As another example, suppose we have collected rainfall data showing the monthly rainfall for twelve months of the year, across fifteen years of data collection, for all fifty states of the USA. We could collect this data as a numeric array RF of rank 3 and shape [50, 15, 12].

In principle, we could pull out the rainfall for April (month 3) of year 6 for the state of Georgia (state #9) by indexing into the array with the appropriate indices: RF[9,6,3]. But well-written programs in rank-polymorphic languages do not operate on individual elements of arrays; as we'll see, programs operate on entire arrays. So indexing is, in fact, something upon which we frown.²

The rank of a scalar array is 0 and its shape is the empty vector [ ]. Note that:

• The rank of an array is also the length of its shape, which is maintained in the case of scalar values.

• Multiplying together the numbers in the shape of an array tells us how many atoms the array contains. For example, the shape of our rainfall-data array is [50, 15, 12], so the array contains 50 × 15 × 12 = 9000 elements.

² It's not impossible to do: as we'll see in a later section (page 30), Remora does have an indexing operator that works in a data-parallel way. It's best to think of indexing in Remora as a fairly heavyweight communications operation that permits programmers to shuffle entire collections of data, not as a means of accessing array elements one-at-a-time.

As a boundary case, consider the scalar array whose only element is the number 17. The shape vector for a scalar array is the empty vector [ ]; multiplying all the elements of the empty vector together produces 1, which is, indeed, the number of elements contained by a scalar array.

In Remora, a language with a LISP-like s-expression syntax, the primitive notation for writing a literal array is the array form, that gives the shape of the array followed by its elements listed in row-major order. So our two example arrays, above, along with the scalar 17, could be written in Remora as the constant expressions:

```scheme
(array [2 3] 7 1 2 2 0 5)  ; Our 2x3 example matrix
(array [50 15 12]          ; Rainfall data
       8 14 10 10 ...)     ; 9,000 elements here
(array [] 17)              ; The scalar value seventeen
```

Note that Remora's basic s-expression syntax uses square brackets as well as parentheses; these are notationally distinct. Note, also, the LISP comment syntax: all text from a semicolon to the end of a line is ignored.

Array-producing expressions can be assembled into larger arrays with the frame form:
```scheme
(frame [d1 ...] e1 ...)
```

The first subform of a frame expression is a shape or list of dimensions [d1 ... dn]. This is followed by as many expressions as the product of the di; these must all produce arrays of identical shape [d′1 ... d′m]. Once these expressions have been evaluated, their result arrays are assembled together to produce a final array of rank n + m and shape [d1 ... dn d′1 ... d′m].

For example, the following code defines v to be a 3-element vector, and m to be a two-row, three-column matrix whose two rows are each identical to v:

```scheme
(define v (array [3] 8 1 7))  ; Shape [3]
(define m (frame [2] v v))    ; Shape [2 3]
```

Note the distinctions between the array and frame forms. The array form is for writing down array constants, that is, literal arrays; its subforms are literal atoms. The frame form causes run-time computation to occur: we evaluate the expressions that are its subforms to produce arrays that are then "plugged into" position in the given frame to make a larger, result array.

Now that we've introduced the array and frame forms, we'll hide them from view at every turn by means of some convenient syntactic sugar:

• First, whenever an atom (that is, an array element) literal a appears in a syntactic context where we expect an expression³, it is taken to be a scalar array—that is, it is treated as shorthand for (array [] a).

• Second, whenever a sequence of expressions occurs surrounded by square brackets in an expression context, it is treated as a frame form for a vector frame. That is, the expression [e1 ... en] is treated as shorthand for (frame [n] e1 ... en).

• Finally, a frame whose component expressions are all array literals is, itself, collapsed to a single array term.

³ Remember: all expressions produce arrays.

Thus we could write the scalar array 17 as expression 17, and the vector of the first five primes as expression [2 3 5 7 11]; our original example array could be written as:

```scheme
[[7 1 2]      ; A 2x3 matrix
 [2 0 5]]
```

This is exactly equivalent to the array-literal expression:
```scheme
(array [2 3] 7 1 2 2 0 5)
```

Likewise, we could write the truth table for i xor j xor k, using 0 for false and 1 for true, as the rank-3 array:

```scheme
;;; A 2x2x2 array
[[[0 1]   ; i=0 plane / j=0 row
  [1 0]]  ; i=0 plane / j=1 row

 [[1 0]   ; i=1 plane / j=0 row
  [0 1]]] ; i=1 plane / j=1 row
```

When using the square-bracket notation, the shape of the array is determined from the nesting structure of the expression. It's not allowed for two brother elements in a square-bracket array expression to have different shapes; they must match. Thus, the following "ragged" matrix is not a legal expression, as it doesn't have a well-defined shape:

```scheme
[[7 1 2]
 [9 5]      ; Illegal -- row too short!
 [2 0 5]]
```

As we'll see later (page 43), there is a mechanism in Remora called a "box," that permits programmers to make ragged arrays, but we'll ignore this for now.

**Functions operate on "cells" of input**

In Remora, every function is defined to operate on arguments of a given rank and produce a result of a given rank; these are called the cells of the function application. For example, the addition operator + operates on two arguments, each of which is a scalar, that is, of rank 0.

```scheme
(+ 3 4)
⇒ 7
(+ 2 8)
⇒ 10
```

In this example, and the examples to come, we'll show code and the result expressions it produces, in an "interactive" style, as if we were presenting Remora expressions and definitions to an interpreter: the input Remora expression will be indented, and the value produced will displayed, flush left, on the following line.

As further examples, we could have a dot-product function dot-prod that operates on two arguments of rank 1; or a polynomial evaluation function poly-eval that operates on a vector (rank 1) giving the coefficients of a polynomial, and a scalar (rank 0) giving the x value where we are evaluating the polynomial:

```scheme
(dot-product [2 0 1] [1 2 3])
⇒ 5
;; Evaluate 2 + 0x - 3x^2 at x=1
(poly-eval [2 0 -3] 1)
⇒ -1
```

The argument ranks of a function are part of its static definition; when we define our own functions, we must specify them. We do this by tagging each parameter to the function with its rank. So, both x and y inputs to the diff-square function below are specified as being of rank 0:

```scheme
(define (diff-square [x 0] [y 0])
  (- (* x x)
     (* y y)))

(diff-square 5 3)
⇒ 16
```

---

### النسخة العربية

في اللغات متعددة الأشكال حسب الرتبة مثل Remora، جميع القيم هي مصفوفات. أي أن كل تعبير في Remora يُقيّم إلى مصفوفة. المصفوفة هي مجموعة من البيانات مرتبة في مستطيل فائق ذي بعد معين. كل مصفوفة تأتي مع عناصرها المكونة، وشكل. عناصر المصفوفة تأتي من عالم منفصل من الذرات؛ الذرات النموذجية هي الأرقام والحروف والقيم المنطقية والدوال. السماح بمصفوفات الدوال يعني أن Remora هي لغة وظيفية عالية المستوى.

على سبيل المثال، لنفكر في مصفوفة مستطيلة لها صفان وثلاثة أعمدة من الأعداد الصحيحة:
```
7 1 2
2 0 5
```

نقول أن هذه المصفوفة المستطيلة لها رتبة 2—أي أن لها بعدين أو محورين للفهرسة—وشكل [2, 3]. شكل المصفوفة هو تسلسل (أو، بالمثل، قائمة أو متجه) يعطي أبعادها.

كمثال آخر، لنفترض أننا جمعنا بيانات هطول الأمطار توضح هطول الأمطار الشهري لاثني عشر شهراً من السنة، عبر خمسة عشر عاماً من جمع البيانات، لجميع الولايات الخمسين في الولايات المتحدة الأمريكية. يمكننا جمع هذه البيانات كمصفوفة رقمية RF ذات رتبة 3 وشكل [50, 15, 12].

من حيث المبدأ، يمكننا استخراج هطول الأمطار لشهر أبريل (الشهر 3) من السنة 6 لولاية جورجيا (الولاية #9) بالفهرسة في المصفوفة بالمؤشرات المناسبة: RF[9,6,3]. لكن البرامج المكتوبة بشكل جيد في اللغات متعددة الأشكال حسب الرتبة لا تعمل على العناصر الفردية للمصفوفات؛ كما سنرى، تعمل البرامج على مصفوفات كاملة. لذا فإن الفهرسة هي، في الواقع، شيء نعارضه.²

رتبة المصفوفة العددية هي 0 وشكلها هو المتجه الفارغ [ ]. لاحظ أن:

• رتبة المصفوفة هي أيضاً طول شكلها، والذي يتم الحفاظ عليه في حالة القيم العددية.

• ضرب الأرقام في شكل المصفوفة معاً يخبرنا بعدد الذرات التي تحتويها المصفوفة. على سبيل المثال، شكل مصفوفة بيانات هطول الأمطار لدينا هو [50, 15, 12]، لذا تحتوي المصفوفة على 50 × 15 × 12 = 9000 عنصر.

² ليس من المستحيل القيام بذلك: كما سنرى في قسم لاحق (صفحة 30)، لدى Remora عامل فهرسة يعمل بطريقة متوازية للبيانات. من الأفضل التفكير في الفهرسة في Remora كعملية اتصال ثقيلة إلى حد ما تسمح للمبرمجين بخلط مجموعات كاملة من البيانات، وليس كوسيلة للوصول إلى عناصر المصفوفة واحداً تلو الآخر.

كحالة حدية، لنفكر في المصفوفة العددية التي عنصرها الوحيد هو الرقم 17. متجه الشكل للمصفوفة العددية هو المتجه الفارغ [ ]؛ ضرب جميع عناصر المتجه الفارغ معاً ينتج 1، وهو بالفعل عدد العناصر الموجودة في المصفوفة العددية.

في Remora، وهي لغة ذات صياغة تعبير-s شبيهة بـ LISP، الترميز الأساسي لكتابة مصفوفة حرفية هو شكل المصفوفة، الذي يعطي شكل المصفوفة متبوعاً بعناصرها المدرجة بترتيب الصف الرئيسي. لذا يمكن كتابة مصفوفتي المثال لدينا، أعلاه، مع العدد 17، في Remora كتعبيرات ثابتة:

```scheme
(array [2 3] 7 1 2 2 0 5)  ; مصفوفتنا المستطيلة 2x3
(array [50 15 12]          ; بيانات هطول الأمطار
       8 14 10 10 ...)     ; 9,000 عنصر هنا
(array [] 17)              ; القيمة العددية سبعة عشر
```

لاحظ أن صياغة التعبير-s الأساسية في Remora تستخدم الأقواس المربعة بالإضافة إلى الأقواس؛ هذه مميزة ترميزياً. لاحظ أيضاً صياغة التعليقات في LISP: كل النص من فاصلة منقوطة إلى نهاية السطر يتم تجاهله.

يمكن تجميع التعبيرات المنتجة للمصفوفات في مصفوفات أكبر باستخدام شكل الإطار:
```scheme
(frame [d1 ...] e1 ...)
```

الشكل الفرعي الأول لتعبير الإطار هو شكل أو قائمة بالأبعاد [d1 ... dn]. يتبع ذلك عدد من التعبيرات يساوي حاصل ضرب di؛ يجب أن تنتج هذه جميعها مصفوفات بشكل متطابق [d′1 ... d′m]. بمجرد تقييم هذه التعبيرات، يتم تجميع مصفوفات النتائج معاً لإنتاج مصفوفة نهائية ذات رتبة n + m وشكل [d1 ... dn d′1 ... d′m].

على سبيل المثال، يحدد الكود التالي v ليكون متجهاً من 3 عناصر، وm لتكون مصفوفة مستطيلة من صفين وثلاثة أعمدة يكون صفاها متطابقين مع v:

```scheme
(define v (array [3] 8 1 7))  ; الشكل [3]
(define m (frame [2] v v))    ; الشكل [2 3]
```

لاحظ الفروق بين أشكال المصفوفة والإطار. شكل المصفوفة هو لكتابة ثوابت المصفوفة، أي المصفوفات الحرفية؛ أشكالها الفرعية هي ذرات حرفية. شكل الإطار يتسبب في حدوث الحساب في وقت التشغيل: نقوم بتقييم التعبيرات التي هي أشكالها الفرعية لإنتاج مصفوفات يتم بعد ذلك "توصيلها" في موضع في الإطار المعطى لصنع مصفوفة نتيجة أكبر.

الآن بعد أن قدمنا أشكال المصفوفة والإطار، سنخفيها عن الأنظار في كل منعطف بوسائل بعض السكر النحوي المناسب:

• أولاً، عندما يظهر ذرة حرفية a (أي عنصر مصفوفة) في سياق نحوي حيث نتوقع تعبيراً³، يُعتبر مصفوفة عددية—أي يُعامل كاختصار لـ (array [] a).

• ثانياً، عندما يحدث تسلسل من التعبيرات محاط بأقواس مربعة في سياق تعبير، يُعامل كشكل إطار لإطار متجه. أي أن التعبير [e1 ... en] يُعامل كاختصار لـ (frame [n] e1 ... en).

• أخيراً، الإطار الذي تكون تعبيرات مكوناته جميعها حرفيات مصفوفة، يتم طيه إلى مصطلح مصفوفة واحد.

³ تذكر: جميع التعبيرات تنتج مصفوفات.

وبالتالي يمكننا كتابة المصفوفة العددية 17 كتعبير 17، ومتجه الأعداد الأولية الخمسة الأولى كتعبير [2 3 5 7 11]؛ يمكن كتابة مصفوفة مثالنا الأصلي كـ:

```scheme
[[7 1 2]      ; مصفوفة مستطيلة 2x3
 [2 0 5]]
```

هذا مكافئ تماماً لتعبير المصفوفة الحرفية:
```scheme
(array [2 3] 7 1 2 2 0 5)
```

بالمثل، يمكننا كتابة جدول الحقيقة لـ i xor j xor k، باستخدام 0 للخطأ و1 للصواب، كمصفوفة رتبة-3:

```scheme
;;; مصفوفة 2x2x2
[[[0 1]   ; i=0 plane / j=0 row
  [1 0]]  ; i=0 plane / j=1 row

 [[1 0]   ; i=1 plane / j=0 row
  [0 1]]] ; i=1 plane / j=1 row
```

عند استخدام ترميز الأقواس المربعة، يتم تحديد شكل المصفوفة من بنية التداخل للتعبير. غير مسموح لعنصرين شقيقين في تعبير مصفوفة بأقواس مربعة أن يكون لهما أشكال مختلفة؛ يجب أن تتطابق. وبالتالي، فإن المصفوفة المستطيلة "المسننة" التالية ليست تعبيراً قانونياً، لأنها لا تحتوي على شكل محدد جيداً:

```scheme
[[7 1 2]
 [9 5]      ; غير قانوني -- الصف قصير جداً!
 [2 0 5]]
```

كما سنرى لاحقاً (صفحة 43)، هناك آلية في Remora تسمى "الصندوق"، تسمح للمبرمجين بصنع مصفوفات مسننة، لكننا سنتجاهل هذا الآن.

**الدوال تعمل على "خلايا" من المدخلات**

في Remora، يتم تعريف كل دالة للعمل على معاملات ذات رتبة معينة وإنتاج نتيجة ذات رتبة معينة؛ تسمى هذه خلايا تطبيق الدالة. على سبيل المثال، عامل الجمع + يعمل على معاملين، كل منهما عددي، أي من رتبة 0.

```scheme
(+ 3 4)
⇒ 7
(+ 2 8)
⇒ 10
```

في هذا المثال، والأمثلة القادمة، سنعرض الكود والتعبيرات الناتجة التي ينتجها، بأسلوب "تفاعلي"، كما لو كنا نقدم تعبيرات وتعريفات Remora لمفسر: سيتم إزاحة تعبير Remora المدخل، وستُعرض القيمة المنتجة، محاذية لليسار، على السطر التالي.

كأمثلة إضافية، يمكن أن يكون لدينا دالة حاصل ضرب نقطي dot-prod تعمل على معاملين من رتبة 1؛ أو دالة تقييم كثيرات الحدود poly-eval تعمل على متجه (رتبة 1) يعطي معاملات كثيرة حدود، وعدد (رتبة 0) يعطي قيمة x حيث نقوم بتقييم كثيرة الحدود:

```scheme
(dot-product [2 0 1] [1 2 3])
⇒ 5
;; تقييم 2 + 0x - 3x^2 عند x=1
(poly-eval [2 0 -3] 1)
⇒ -1
```

رتب معاملات الدالة هي جزء من تعريفها الثابت؛ عندما نحدد دوالنا الخاصة، يجب علينا تحديدها. نفعل ذلك بوسم كل معامل للدالة برتبته. لذا، كل من مدخلات x وy لدالة diff-square أدناه محددة على أنها من رتبة 0:

```scheme
(define (diff-square [x 0] [y 0])
  (- (* x x)
     (* y y)))

(diff-square 5 3)
⇒ 16
```

---

### Translation Notes

- **Key terms introduced:**
  - array (مصفوفة)
  - rank (رتبة)
  - shape (شكل)
  - atom (ذرة)
  - scalar (عددي/قيمة عددية)
  - vector (متجه)
  - matrix (مصفوفة مستطيلة)
  - frame (إطار)
  - cell (خلية)
  - hyper-rectangle (مستطيل فائق)

- **Code examples:** Preserved in original English format (standard practice)
- **Comments:** Translated to Arabic while keeping code syntax intact
- **Mathematical notation:** Preserved (e.g., 50 × 15 × 12)
- **Footnotes:** Maintained with same numbering

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.86

### Back-Translation (Key Paragraphs)

In rank-polymorphic languages like Remora, all values are arrays. That is, every expression in Remora evaluates to an array. An array is a collection of data arranged in a hyper-rectangle of a specific dimension. Each array comes with its constituent elements, and a shape. Array elements come from a separate universe of atoms; typical atoms are numbers, letters, boolean values, and functions. Allowing arrays of functions means that Remora is a higher-order functional language.

In Remora, each function is defined to operate on parameters of a specific rank and produce a result of a specific rank; these are called the cells of the function application. For example, the addition operator + operates on two parameters, each scalar, i.e., of rank 0.
