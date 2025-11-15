# Section 5: Conclusions
## القسم 5: الخلاصة

**Section:** conclusions
**Translation Quality:** 0.88
**Glossary Terms Used:** functional programming, dependent types, type-level functions, property-based testing, theorem proving, rewriting rules, parallelism, compiler optimization

---

### English Version

In this paper, we have demonstrated how we can adopt the methods developed in the area of functional programming to build a computer algebra system. Some of these methods are also applicable in imperative languages.

In Section 2, we presented a type-system strong enough to detect algebraic errors at compile-time. For example, our system can distinguish number of variables of polynomial rings at type-level thanks to dependent types. It also enables us to automatically generate casting functions and we saw how their overhead can be reduced using rewriting rules. As for type-systems for a computer algebra system, there are several existing works [18, 23]. However, these systems are not safe enough for discriminating variable arity at type-level and don't make use of rewriting rules.

In Section 3, we successfully applied the method of property-based testing for verification of the implementation, which is lightweight compared to the existing theorem-prover based approach [2, 24]. Although property-based testing is not as rigorous as theorem proving, it is lightweight and can be applied to algorithms not yet proven to be valid or terminate and available also for imperative languages.

We have seen that, in Section 4, other features of Haskell, such as higher-order polymorphism, parallelism and laziness, can also be easily applied to computer algebra by actual examples. Even though they are shown as fragments of code, we expect them to be convincing.

Since some of the methods in this paper, such as dependent types or property-based testing, are not limited to the functional paradigm, it might be interesting to investigate their applicability in the imperative settings.

From the viewpoint of efficiency, there are much to be done. For example, efficiency of our current F₄ implementation is far inferior to that of the naïve Buchberger algorithm, and other algorithms are far much slower than state-of-the-art implementations such as Singular. To optimise implementations, we can make more use of Rewriting Rules and efficient data structures. Also, the parallelism must undoubtedly play an important role. Fortunately, there are plenty of the parallel computation functionalities in Haskell, such as Regular Parallel Arrays [16] and parallel package [22], and another book by Marlow [21] on general topics in parallelism in Haskell. Also, there is an existing work by Lobachev et al. [20] on parallel symbolic computation in Eden, a dialect of Haskell with parallelism support. Although Eden is retired, the methods introduced there might be helpful.

#### Acknowledgements

The author would like to thank my supervisor, Prof. Akira Terui, for discussions, and to anonymous reviewers for helpful comments. This research is supported by Grant-in-Aid for JSPS Research Fellow Number 17J00479, and partially by Grants-in-Aid for Scientific Research 16K05035. This is a pre-print of an article published in "Computer Algebra in Scientific Computing" (2018). The final authenticated version is available online at: https://doi.org/10.1007/978-3-319-99639-4

---

### النسخة العربية

في هذه الورقة، أوضحنا كيف يمكننا اعتماد الأساليب المطورة في مجال البرمجة الوظيفية لبناء نظام جبر حاسوبي. بعض هذه الأساليب قابلة للتطبيق أيضاً في اللغات الإلزامية.

في القسم 2، قدمنا نظام أنواع قوي بما يكفي لاكتشاف الأخطاء الجبرية في وقت الترجمة. على سبيل المثال، يمكن لنظامنا التمييز بين عدد متغيرات حلقات كثيرات الحدود على مستوى الأنواع بفضل الأنواع التابعة. كما يمكننا من إنشاء دوال التحويل تلقائياً ورأينا كيف يمكن تقليل النفقات العامة الخاصة بها باستخدام قواعد إعادة الكتابة. فيما يتعلق بأنظمة الأنواع لنظام جبر حاسوبي، هناك العديد من الأعمال الموجودة [18، 23]. ومع ذلك، فإن هذه الأنظمة ليست آمنة بما فيه الكفاية للتمييز بين عدد المتغيرات على مستوى الأنواع ولا تستفيد من قواعد إعادة الكتابة.

في القسم 3، طبقنا بنجاح طريقة الاختبار القائم على الخصائص للتحقق من التطبيق، وهي خفيفة الوزن مقارنة بالنهج القائم على مُثبت النظرية الموجود [2، 24]. على الرغم من أن الاختبار القائم على الخصائص ليس صارماً مثل إثبات النظرية، إلا أنه خفيف الوزن ويمكن تطبيقه على الخوارزميات التي لم يتم إثبات صحتها أو انتهائها بعد ومتاح أيضاً للغات الإلزامية.

رأينا في القسم 4 أنه يمكن أيضاً تطبيق ميزات أخرى لـ Haskell، مثل تعدد الأشكال من الرتبة العليا والتوازي والكسل، بسهولة على الجبر الحاسوبي من خلال أمثلة فعلية. على الرغم من أنها معروضة كأجزاء من الشفرة، إلا أننا نتوقع أن تكون مقنعة.

نظراً لأن بعض الأساليب في هذه الورقة، مثل الأنواع التابعة أو الاختبار القائم على الخصائص، ليست محدودة بالنموذج الوظيفي، فقد يكون من المثير للاهتمام دراسة قابليتها للتطبيق في الإعدادات الإلزامية.

من وجهة نظر الكفاءة، هناك الكثير مما يجب القيام به. على سبيل المثال، كفاءة تطبيق F₄ الحالي الخاص بنا أقل بكثير من كفاءة خوارزمية Buchberger الساذجة، والخوارزميات الأخرى أبطأ بكثير من التطبيقات الحديثة مثل Singular. لتحسين التطبيقات، يمكننا الاستفادة بشكل أكبر من قواعد إعادة الكتابة وبنى البيانات الفعالة. أيضاً، يجب أن يلعب التوازي دوراً مهماً بلا شك. لحسن الحظ، هناك الكثير من وظائف الحوسبة المتوازية في Haskell، مثل Regular Parallel Arrays [16] وحزمة parallel [22]، وكتاب آخر لـ Marlow [21] عن موضوعات عامة في التوازي في Haskell. أيضاً، هناك عمل موجود لـ Lobachev وآخرون [20] حول الحوسبة الرمزية المتوازية في Eden، وهي لهجة من Haskell مع دعم التوازي. على الرغم من أن Eden قد تم إيقافها، إلا أن الأساليب المُقدمة هناك قد تكون مفيدة.

#### شكر وتقدير

يود المؤلف أن يشكر مشرفي، البروفيسور Akira Terui، على المناقشات، والمراجعين المجهولين على التعليقات المفيدة. هذا البحث مدعوم من قبل Grant-in-Aid لزميل أبحاث JSPS رقم 17J00479، وجزئياً من قبل Grants-in-Aid للبحث العلمي 16K05035. هذه نسخة ما قبل الطباعة من مقال منشور في "Computer Algebra in Scientific Computing" (2018). النسخة النهائية الموثقة متاحة عبر الإنترنت على: https://doi.org/10.1007/978-3-319-99639-4

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** naïve algorithm (الخوارزمية الساذجة), state-of-the-art (حديثة), dialect (لهجة)
- **Equations:** 0
- **Citations:** [2, 16, 18, 20, 21, 22, 23, 24]
- **Special handling:**
  - Acknowledgements section fully translated
  - Grant numbers and DOI preserved as is
  - Names of people and institutions kept in English
  - Book and publication titles maintained in English
  - Technical system names unchanged

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
