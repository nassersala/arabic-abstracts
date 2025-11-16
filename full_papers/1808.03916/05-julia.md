# Section 5: Julia - Flexibility of Idioms
## القسم 5: Julia - مرونة التعابير الاصطلاحية

**Section:** examples/methodology
**Translation Quality:** 0.87
**Glossary Terms Used:** لغة برمجة, أداء, إطار البيانات, حلقات for, تجريدات, تحسين

---

### English Version

## 5. Julia: flexibility of idioms

The last language I will consider here is Julia, a general-purpose programming language that was originally designed for technical computing (Bezanson, 2015)². Julia is a language that is easy for both compilers and programmers to understand, in the sense that it is a high level dynamic language with language constructs that facilitate compiler analysis and generation of efficient code.

The result of Julia's careful design for expressiveness and performance allows for the different solutions above for the split-apply-combine problem to all be expressible in the same language. The solution to split-apply-combine in R/dplyr derives its performance from an underlying implementation of dplyr in C++ (via Rcpp). In contrast, all the Julia solutions in this section are written in pure Julia. The result is that Julia users can also be Julia developers without necessarily having to learn another language to work on the underlying implementation which does all the heavy lifting. Another advantage is that Julia users can experiment with different idioms and data structures without being confined to just those that have well-optimized implementations, and enjoy reasonable performance in many cases.

For example, the DataFrames.jl package provides two different spellings for the R/dplyr approach:

```julia
1  using DataFrames
2  df = DataFrame(
3      userids=[381, 1291, 3992, 193942, 9494, 381, 3992, 381, 3992,
4               193942], ratings=[5, 4, 4, 4, 5, 5, 5, 3, 5, 4]);
5  by(df, :userids, df->mean(df[:ratings])) #Same as next line
6  aggregate(df, :userids, mean)
```

Output:
```
5×2 DataFrames.DataFrame
│ Row │ userids │ ratings_mean │
├─────┼─────────┼──────────────┤
│ 1   │ 381     │ 4.33333      │
│ 2   │ 1291    │ 4.0          │
│ 3   │ 3992    │ 4.66667      │
│ 4   │ 9494    │ 5.0          │
│ 5   │ 193942  │ 4.0          │
```

The solution to split-apply-combine in R/dplyr derives its performance from an underlying implementation of dplyr in C++ (via Rcpp). In contrast, the Julia solutions are written in pure Julia. The result is that Julia users can also be Julia developers without necessarily having to learn another language to work on the underlying implementation which does all the heavy lifting. Another advantage is that Julia users can experiment with different idioms and data structures without being confined to just those that have well-optimized implementations, and enjoy reasonable performance in many cases.

For example, a user who is unfamiliar with data frames and may prefer instead an array-based solution may choose to implement an APL-style solution using a simple list comprehension:

```julia
7  userids=[381, 1291, 3992, 193942, 9494, 381, 3992, 381, 3992,
8           193942]
9  ratings=[5, 4, 4, 4, 5, 5, 5, 3, 5, 4]
10 [(u, mean(ratings[userids.==u])) for u in unique(userids)]
```

Output:
```
5-element Array{Tuple{Any,Any},1}:
 (381,4.333333333333333)
 (1291,4.0)
 (3992,4.666666666666667)
 (193942,4.0)
 (9494,5.0)
```

The list comprehension approach is simple and concise, if not particularly fast. Nevertheless, the ability to rewrite a solution multiple different way in Julia allows for Julia users to experiment with different approaches in order to find one with the most acceptable performance. For example, a Julia user may choose to rewrite the list comprehension solution by writing out for loops explicitly, something that is discouraged in all the other languages discussed here (which promote the "vectorize your code" habit). One such implementation example might look like the following:

```julia
11 counts = []
12 uuserids=[]
13 uratings=[]
14 for i in eachindex(userids)
15     j = findfirst(uuserids, userids[i])
16     if j==0 #not found
17         push!(uuserids, userids[i])
18         push!(uratings, ratings[i])
19         push!(counts, 1)
20     else #already seen
21         uratings[j] += ratings[i]
22         counts[j] += 1
23     end
24 end
25 [uuserids uratings./counts]
```

Output:
```
5x2 Array{Any,2}:
 381    4.33333
 1291   4.0
 3992   4.66667
 193942 4.0
 9494   5.0
```

Finally, a Julia user may later recognize this code as implementing the split-apply-combine idiom and choose to refactor this code into a reusable function akin to accumarray. In fact, accumarray itself can be implemented in Julia with just a few lines of code:

```julia
26 function accumarray{Tk,Tv}(
27     subs::AbstractArray{Tk}, val::AbstractArray{Tv},
28     func=sum, fillval=zero(Tv)
29     ; sz=maximum(subs,1), issparse=false)
30
31     counts = Dict{Vector{Tk},Vector{Tv}}()
32     for i = 1:size(subs, 1)
33         counts[subs[i, :]] = #split
34             Tv[get(counts,subs[i, :], Tv[]); val[i...]]
35     end
36
37     A = issparse ? spzeros(sz...) : fill(fillval, sz...) #combine
38     for (key, val) in counts
39         A[key...]= func(val) #apply
40     end
41     return A
42 end
```

Thus even though accumarray does not exist in the base Julia library, an experienced user can, without much difficulty, refactor a previous solution into a part that implements the general purpose accumarray function. Having multiple options gives Julia users the possibility of choosing the best trade-off between development time and actual execution time when deployed on large data sets.

---

²All the Julia code presented here is written for version 0.5.0.

---

### النسخة العربية

## 5. Julia: مرونة التعابير الاصطلاحية

اللغة الأخيرة التي سأنظر فيها هنا هي Julia، وهي لغة برمجة للأغراض العامة صُممت في الأصل للحوسبة التقنية (Bezanson, 2015)². Julia هي لغة سهلة الفهم لكل من المترجمات والمبرمجين، بمعنى أنها لغة ديناميكية عالية المستوى مع بنى لغوية تسهل تحليل المترجم وتوليد شفرة فعالة.

تسمح نتيجة التصميم الدقيق لـ Julia للتعبيرية والأداء بالتعبير عن جميع الحلول المختلفة أعلاه لمشكلة التقسيم-التطبيق-الدمج في نفس اللغة. يستمد حل التقسيم-التطبيق-الدمج في R/dplyr أداءه من تطبيق أساسي لـ dplyr في C++ (عبر Rcpp). في المقابل، جميع حلول Julia في هذا القسم مكتوبة بلغة Julia الخالصة. والنتيجة هي أن مستخدمي Julia يمكن أن يكونوا أيضاً مطوري Julia دون الحاجة بالضرورة إلى تعلم لغة أخرى للعمل على التطبيق الأساسي الذي يقوم بكل العمل الشاق. ميزة أخرى هي أن مستخدمي Julia يمكنهم التجربة مع تعابير اصطلاحية وبنى بيانات مختلفة دون أن يكونوا محصورين فقط في تلك التي لديها تطبيقات محسّنة جيداً، والتمتع بأداء معقول في كثير من الحالات.

على سبيل المثال، توفر حزمة DataFrames.jl صياغتين مختلفتين لنهج R/dplyr:

```julia
1  using DataFrames
2  df = DataFrame(
3      userids=[381, 1291, 3992, 193942, 9494, 381, 3992, 381, 3992,
4               193942], ratings=[5, 4, 4, 4, 5, 5, 5, 3, 5, 4]);
5  by(df, :userids, df->mean(df[:ratings])) #Same as next line
6  aggregate(df, :userids, mean)
```

النتيجة:
```
5×2 DataFrames.DataFrame
│ Row │ userids │ ratings_mean │
├─────┼─────────┼──────────────┤
│ 1   │ 381     │ 4.33333      │
│ 2   │ 1291    │ 4.0          │
│ 3   │ 3992    │ 4.66667      │
│ 4   │ 9494    │ 5.0          │
│ 5   │ 193942  │ 4.0          │
```

يستمد حل التقسيم-التطبيق-الدمج في R/dplyr أداءه من تطبيق أساسي لـ dplyr في C++ (عبر Rcpp). في المقابل، حلول Julia مكتوبة بلغة Julia الخالصة. والنتيجة هي أن مستخدمي Julia يمكن أن يكونوا أيضاً مطوري Julia دون الحاجة بالضرورة إلى تعلم لغة أخرى للعمل على التطبيق الأساسي الذي يقوم بكل العمل الشاق. ميزة أخرى هي أن مستخدمي Julia يمكنهم التجربة مع تعابير اصطلاحية وبنى بيانات مختلفة دون أن يكونوا محصورين فقط في تلك التي لديها تطبيقات محسّنة جيداً، والتمتع بأداء معقول في كثير من الحالات.

على سبيل المثال، قد يختار مستخدم غير مألوف بأطر البيانات وقد يفضل بدلاً من ذلك حلاً قائماً على المصفوفات تنفيذ حل على نمط APL باستخدام فهم قائمة بسيط:

```julia
7  userids=[381, 1291, 3992, 193942, 9494, 381, 3992, 381, 3992,
8           193942]
9  ratings=[5, 4, 4, 4, 5, 5, 5, 3, 5, 4]
10 [(u, mean(ratings[userids.==u])) for u in unique(userids)]
```

النتيجة:
```
5-element Array{Tuple{Any,Any},1}:
 (381,4.333333333333333)
 (1291,4.0)
 (3992,4.666666666666667)
 (193942,4.0)
 (9494,5.0)
```

نهج فهم القائمة بسيط وموجز، إن لم يكن سريعاً بشكل خاص. ومع ذلك، فإن القدرة على إعادة كتابة حل بطرق مختلفة متعددة في Julia تسمح لمستخدمي Julia بالتجربة مع مناهج مختلفة من أجل العثور على واحدة ذات أداء أكثر قبولاً. على سبيل المثال، قد يختار مستخدم Julia إعادة كتابة حل فهم القائمة عن طريق كتابة حلقات for بشكل صريح، وهو شيء محبط في جميع اللغات الأخرى التي تمت مناقشتها هنا (والتي تروج لعادة "استخدام المتجهات في شفرتك"). قد يبدو أحد أمثلة التطبيق كالتالي:

```julia
11 counts = []
12 uuserids=[]
13 uratings=[]
14 for i in eachindex(userids)
15     j = findfirst(uuserids, userids[i])
16     if j==0 #not found
17         push!(uuserids, userids[i])
18         push!(uratings, ratings[i])
19         push!(counts, 1)
20     else #already seen
21         uratings[j] += ratings[i]
22         counts[j] += 1
23     end
24 end
25 [uuserids uratings./counts]
```

النتيجة:
```
5x2 Array{Any,2}:
 381    4.33333
 1291   4.0
 3992   4.66667
 193942 4.0
 9494   5.0
```

أخيراً، قد يتعرف مستخدم Julia لاحقاً على هذه الشفرة كتنفيذ للتعبير الاصطلاحي للتقسيم-التطبيق-الدمج ويختار إعادة هيكلة هذه الشفرة إلى دالة قابلة لإعادة الاستخدام مشابهة لـ accumarray. في الواقع، يمكن تنفيذ accumarray نفسها في Julia بعدد قليل فقط من أسطر الشفرة:

```julia
26 function accumarray{Tk,Tv}(
27     subs::AbstractArray{Tk}, val::AbstractArray{Tv},
28     func=sum, fillval=zero(Tv)
29     ; sz=maximum(subs,1), issparse=false)
30
31     counts = Dict{Vector{Tk},Vector{Tv}}()
32     for i = 1:size(subs, 1)
33         counts[subs[i, :]] = #split
34             Tv[get(counts,subs[i, :], Tv[]); val[i...]]
35     end
36
37     A = issparse ? spzeros(sz...) : fill(fillval, sz...) #combine
38     for (key, val) in counts
39         A[key...]= func(val) #apply
40     end
41     return A
42 end
```

وبالتالي، حتى لو لم تكن accumarray موجودة في مكتبة Julia الأساسية، يمكن لمستخدم متمرس، دون صعوبة كبيرة، إعادة هيكلة حل سابق إلى جزء ينفذ دالة accumarray للأغراض العامة. إن وجود خيارات متعددة يمنح مستخدمي Julia إمكانية اختيار أفضل مقايضة بين وقت التطوير ووقت التنفيذ الفعلي عند النشر على مجموعات بيانات كبيرة.

---

²جميع شفرات Julia المقدمة هنا مكتوبة للإصدار 0.5.0.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - general-purpose (للأغراض العامة)
  - technical computing (الحوسبة التقنية)
  - dynamic language (لغة ديناميكية)
  - compiler analysis (تحليل المترجم)
  - list comprehension (فهم القائمة)
  - for loops (حلقات for)
  - refactor (إعادة هيكلة)
  - trade-off (مقايضة)
- **Equations:** None
- **Citations:** Bezanson, 2015
- **Special handling:**
  - All Julia code preserved in original format
  - Function names (by, aggregate, mean, unique, findfirst, push!, etc.) kept in English
  - Package names (DataFrames.jl, Rcpp) kept in English
  - Comments in code kept in English
  - Technical terms explained with Arabic equivalents
  - Comparison with R/dplyr and C++ implementation highlighted

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.86
- **Overall section score:** 0.87

### Back-Translation Check (Key Paragraph)

Original: "The result of Julia's careful design for expressiveness and performance allows for the different solutions above for the split-apply-combine problem to all be expressible in the same language."

Back-translation: "The result of Julia's careful design for expressiveness and performance allows all the different solutions above for the split-apply-combine problem to be expressed in the same language."

✓ Semantically equivalent
