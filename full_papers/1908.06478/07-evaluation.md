# Section 7: Evaluation
## القسم 7: التقييم

**Section:** evaluation
**Translation Quality:** 0.86
**Glossary Terms Used:** analysis, type system, compiler, optimization, linear program

---

### English Version

Our implementation can analyze a substantial subset of Haskell. For example, consider the following simple Haskell module, which contains examples of several concepts that are common to Haskell, but nonexistent in JVFH, such as list comprehension and function applications with non-variable arguments:

```haskell
module Example where
import Prelude hiding (map, repeat)

repeat x = xs where xs = x : xs
map f xs = [f x | x <- xs]
it = map (+1) $ repeat 1 :: [Int]
```

When applied to this module, our analysis will successfully generate the following typing for the variable it:

```
⊢^9_1 it : µX. {[] : (0, []) | (:) : (0, [T³(Int), T⁰(X)])}
```

This means that evaluating this expression to weak head normal form will induce a onetime cost of 9 allocations at most, and up to 3 more allocations for each list node accessed. Furthermore, accessing any of the list elements will also evoke one additional allocation.

For comparison, consider the following translation of the previous code to JVFH:

```
let repeat = \x -> letcons xs = Cons(x,xs) in xs
in let map = \f xt -> match xt with
                Nil() -> letcons r = Nil() in r
              | Cons(x,xs) -> let y = f x
                              in let ys = map f xs
                              in letcons r = Cons(y,ys)
                              in r
in let one = 1
in let ones = repeat one
in let inc = \x -> let r = one + x in r
in let it = map inc ones
in it
```

From this expression, the original JVFH analysis will infer the following typing:

```
⊢^10_0 it : µX. {[] : (0, []) | (:) : (0, [T¹(Int), T³(X)])}
```

Note that the typing is similar, but not identical. The specific values used as type annotations may differ, due to differences in how the code is represented in JVFH and GHC Core, respectively; and the LP solver also has some freedom in how values are assigned to variables.

This result is typical of most comparisons between JVFH and Haskell analyses. As we have not formally proven the correctness of our adapted system, we used JVFH analysis results as a basis for testing the viability of our own analysis. For this purpose, we translated several JVFH example programs published as part of a JVFH online demo¹ to Haskell. We then ran our analysis on this code and compared our results to those from the online demo. While we obtained similar results in most cases, there were a few noteworthy cases where our results were entirely different.

One of these is the following code which is a simplified version of the "list fusion" example from the online demo. For brevity, we will only provide our Haskell translation of the code:

```haskell
map1 f [] = []
map1 f (x:xs) = f x : map1 f xs

map2 f [] = []
map2 f (x:xs) = f x : map2 f xs

lhs f g xs = map1 f $ map2 g xs
```

Note that we provide duplicate definitions of the map function for each usage within the lhs function. This is a workaround commonly used in the JVFH examples, which allows us to assign different types with different annotations to each usage of the function. Using this trick, the original JVFH version of the code above can be analyzed without any issues. However, when we attempt to analyze our Haskell translation, the GHC compiler detects this duplication and removes it, replacing all references to map2 with map1. As a result, our analysis of the lhs function will generate an unsolvable linear program and then fail. This is beyond our control, as we can only edit the Haskell code, and the translation to GHC Core is left entirely to the compiler.

However, this property also facilitated the discovery and elimination of an issue with a type rule that had previously been considered sound. We found this issue while analyzing the following definition of the Fibonacci sequence:

```haskell
zipWith f (x:xs) (y:ys) = f x y : zipWith f xs ys
fibs = 0 : 1 : zipWith (+) fibs fibs' where (_:fibs') = fibs
```

Initially, our analysis erroneously was able to derive a constant cost for this sequence, meaning that it would be possible to fully evaluate the entire infinite list. We have previously detailed the cause and our fix of this issue in our discussion of the LETREC_GC type rule in section 5. However, this issue was exposed only because GHC translated our Haskell code to Core using letrec for mutual recursion; The original JVFH version of this code did not contain any letand expressions – which is the JVFH equivalent of letrec – and therefore the erroneous type rule was not triggered during analysis. However, we were able to reproduce this error in the JVFH analysis by manually translating the Core code to JVFH, proving that this is an issue with the original rule, and not with our own implementation. While our fix causes the analysis of this Fibonacci code to fail due to an unsolvable linear program, this is preferable over returning an incorrect analysis result.

¹ The JVFH online demo is available at: http://kashmir.dcc.fc.up.pt/cgi/lazy.cgi

---

### النسخة العربية

يمكن لتطبيقنا تحليل مجموعة فرعية كبيرة من Haskell. على سبيل المثال، لننظر إلى وحدة Haskell البسيطة التالية، والتي تحتوي على أمثلة لعدة مفاهيم شائعة في Haskell، ولكنها غير موجودة في JVFH، مثل استيعاب القوائم وتطبيقات الدوال مع معاملات غير متغيرة:

```haskell
module Example where
import Prelude hiding (map, repeat)

repeat x = xs where xs = x : xs
map f xs = [f x | x <- xs]
it = map (+1) $ repeat 1 :: [Int]
```

عند تطبيق هذه الوحدة، سينجح تحليلنا في توليد التنميط التالي للمتغير it:

```
⊢^9_1 it : µX. {[] : (0, []) | (:) : (0, [T³(Int), T⁰(X)])}
```

هذا يعني أن تقييم هذا التعبير إلى الشكل الطبيعي الضعيف للرأس سيؤدي إلى تكلفة لمرة واحدة قدرها 9 تخصيصات على الأكثر، وما يصل إلى 3 تخصيصات إضافية لكل عقدة قائمة يتم الوصول إليها. علاوة على ذلك، سيؤدي الوصول إلى أي من عناصر القائمة أيضاً إلى استدعاء تخصيص إضافي واحد.

للمقارنة، لننظر إلى الترجمة التالية للشفرة السابقة إلى JVFH:

```
let repeat = \x -> letcons xs = Cons(x,xs) in xs
in let map = \f xt -> match xt with
                Nil() -> letcons r = Nil() in r
              | Cons(x,xs) -> let y = f x
                              in let ys = map f xs
                              in letcons r = Cons(y,ys)
                              in r
in let one = 1
in let ones = repeat one
in let inc = \x -> let r = one + x in r
in let it = map inc ones
in it
```

من هذا التعبير، سيستنتج تحليل JVFH الأصلي التنميط التالي:

```
⊢^10_0 it : µX. {[] : (0, []) | (:) : (0, [T¹(Int), T³(X)])}
```

لاحظ أن التنميط متشابه، ولكن ليس متطابقاً. قد تختلف القيم المحددة المستخدمة كتعليمات أنواع، بسبب الاختلافات في كيفية تمثيل الشفرة في JVFH و GHC Core على التوالي؛ ولدى حلّال البرمجة الخطية أيضاً بعض الحرية في كيفية تعيين القيم للمتغيرات.

هذه النتيجة نموذجية لمعظم المقارنات بين تحليلات JVFH و Haskell. نظراً لأننا لم نثبت رسمياً صحة نظامنا المكيّف، فقد استخدمنا نتائج تحليل JVFH كأساس لاختبار جدوى تحليلنا الخاص. لهذا الغرض، ترجمنا عدة برامج أمثلة JVFH منشورة كجزء من عرض توضيحي عبر الإنترنت لـ JVFH¹ إلى Haskell. ثم قمنا بتشغيل تحليلنا على هذه الشفرة وقارنا نتائجنا بتلك من العرض التوضيحي عبر الإنترنت. بينما حصلنا على نتائج مماثلة في معظم الحالات، كانت هناك بعض الحالات الجديرة بالملاحظة حيث كانت نتائجنا مختلفة تماماً.

إحدى هذه الحالات هي الشفرة التالية وهي نسخة مبسطة من مثال "دمج القوائم" من العرض التوضيحي عبر الإنترنت. للإيجاز، سنقدم فقط ترجمة Haskell الخاصة بنا للشفرة:

```haskell
map1 f [] = []
map1 f (x:xs) = f x : map1 f xs

map2 f [] = []
map2 f (x:xs) = f x : map2 f xs

lhs f g xs = map1 f $ map2 g xs
```

لاحظ أننا نقدم تعريفات مكررة لدالة map لكل استخدام داخل دالة lhs. هذا حل بديل يُستخدم بشكل شائع في أمثلة JVFH، والذي يسمح لنا بتعيين أنواع مختلفة بتعليمات مختلفة لكل استخدام للدالة. باستخدام هذه الحيلة، يمكن تحليل نسخة JVFH الأصلية من الشفرة أعلاه دون أي مشاكل. ومع ذلك، عندما نحاول تحليل ترجمة Haskell الخاصة بنا، يكتشف مترجم GHC هذا التكرار ويزيله، ويستبدل جميع المراجع إلى map2 بـ map1. نتيجة لذلك، سيولد تحليلنا لدالة lhs برنامجاً خطياً غير قابل للحل ثم يفشل. هذا خارج عن سيطرتنا، حيث يمكننا فقط تحرير شفرة Haskell، وتُترك الترجمة إلى GHC Core بالكامل للمترجم.

ومع ذلك، سهّلت هذه الخاصية أيضاً اكتشاف مشكلة في قاعدة أنواع كان يُعتبر سابقاً أنها صحيحة والقضاء عليها. وجدنا هذه المشكلة أثناء تحليل التعريف التالي لمتتالية فيبوناتشي:

```haskell
zipWith f (x:xs) (y:ys) = f x y : zipWith f xs ys
fibs = 0 : 1 : zipWith (+) fibs fibs' where (_:fibs') = fibs
```

في البداية، تمكن تحليلنا بشكل خاطئ من اشتقاق تكلفة ثابتة لهذه المتتالية، مما يعني أنه سيكون من الممكن تقييم القائمة اللانهائية بأكملها بالكامل. لقد فصّلنا سابقاً السبب وإصلاحنا لهذه المشكلة في مناقشتنا لقاعدة نوع LETREC_GC في القسم 5. ومع ذلك، تم الكشف عن هذه المشكلة فقط لأن GHC ترجم شفرة Haskell الخاصة بنا إلى Core باستخدام letrec للتكرار المتبادل؛ لم تحتوِ نسخة JVFH الأصلية من هذه الشفرة على أي تعبيرات letand - وهي ما يعادل JVFH لـ letrec - وبالتالي لم يتم تشغيل قاعدة النوع الخاطئة أثناء التحليل. ومع ذلك، تمكنا من إعادة إنتاج هذا الخطأ في تحليل JVFH من خلال ترجمة شفرة Core يدوياً إلى JVFH، مما يثبت أن هذه مشكلة في القاعدة الأصلية، وليس في تطبيقنا الخاص. بينما يتسبب إصلاحنا في فشل تحليل شفرة فيبوناتشي هذه بسبب برنامج خطي غير قابل للحل، فإن هذا أفضل من إرجاع نتيجة تحليل غير صحيحة.

¹ العرض التوضيحي عبر الإنترنت لـ JVFH متاح على: http://kashmir.dcc.fc.up.pt/cgi/lazy.cgi

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - list comprehension (استيعاب القوائم)
  - weak head normal form (الشكل الطبيعي الضعيف للرأس)
  - allocations (تخصيصات)
  - list node (عقدة قائمة)
  - list fusion (دمج القوائم)
  - unsolvable linear program (برنامج خطي غير قابل للحل)
  - mutual recursion (التكرار المتبادل)
  - Fibonacci sequence (متتالية فيبوناتشي)
- **Equations:** Type annotations with superscripts
- **Citations:** Reference to JVFH online demo
- **Special handling:**
  - Code examples in Haskell and JVFH kept as is
  - URL to JVFH demo kept in original
  - Footnote notation preserved

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86

### Back-Translation (First & Last Paragraphs)

**First paragraph:** Our implementation can analyze a substantial subset of Haskell. For example, let's look at the following simple Haskell module, which contains examples of several concepts common to Haskell, but nonexistent in JVFH, such as list comprehension and function applications with non-variable arguments:

**Last paragraph:** Initially, our analysis was erroneously able to derive a constant cost for this sequence, meaning that it would be possible to fully evaluate the entire infinite list completely. We have previously detailed the cause and our fix for this problem in our discussion of the LETREC_GC type rule in section 5. However, this problem was exposed only because GHC translated our Haskell code to Core using letrec for mutual recursion; The original JVFH version of this code did not contain any letand expressions - which is the JVFH equivalent of letrec - and therefore the erroneous type rule was not triggered during analysis. However, we were able to reproduce this error in the JVFH analysis by manually translating the Core code to JVFH, proving that this is a problem with the original rule, and not with our own implementation. While our fix causes the analysis of this Fibonacci code to fail due to an unsolvable linear program, this is preferable to returning an incorrect analysis result.
