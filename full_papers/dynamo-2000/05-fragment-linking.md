# Section 5: Fragment Linking
## القسم 5: ربط الأجزاء

**Section:** fragment-linking
**Translation Quality:** 0.87
**Glossary Terms Used:** fragment linking, exit stub, compensation block, fragment cache, branch patching, working set

---

### English Version

After the fragment code is emitted into the fragment cache, the new fragment is linked to other fragments already in the fragment cache. Linking involves patching a fragment exit branch so that its taken target is the entry point of another fragment, instead of to its exit stub.

As an example, suppose the trace BDGIJE in Figure 3 (a) now becomes hot (B is a valid start-of-trace by our definition, when it is entered via an exit from the earlier hot trace ACDGHJE). Figure 4 illustrates the linking that occurs after the fragment corresponding to the BDGIJE trace is emitted into the fragment cache. Linked branches are shown as dark arrows, and their original unlinked versions are indicated as dashed light arrows.

Fragment linking is essential for performance, because it prevents expensive exits from the fragment cache back to the Dynamo interpreter. In our prototype implementation on the PA-8000 for example, disabling fragment linking results in an order of magnitude slowdown (by an average factor of 40 for the SpecInt95 benchmarks).

Fragment linking also provides an opportunity for removing redundant compensation code from the source fragment involved in the link. Recall that the trace optimizer sinks on-trace redundancies into compensation blocks, so that these instructions are only executed when control exits the fragment along a particular path (see Section 4.2). Fragment A in Figure 5 illustrates such a case, where the assignment to r5 shown in the compensation block (thick border) was originally in the first block before it was sunk into its compensation block. As part of the linkage information that is kept at each fragment exit stub (the shaded boxes in Figure 5), a mask of on-trace redundant register assignments along that particular fragment exit is maintained. In Figure 5, this mask would be kept in the exit stub corresponding to the compensation block, and bit 5 of the mask would be set. A similar mask of killed register assignments at the top of every fragment is also maintained as part of the Dynamo internal data structure that keeps fragment-related information. At link-time, if a register appears in both masks, the instruction that last defined it in the source fragment's compensation block is dead and can be removed. This is illustrated in Figure 5, where the assignment to r5 in Fragment A's compensation block can be deleted because r5 is defined before being used on entry to Fragment B.

While the advantages of linking are clear, it also has some disadvantages that impact other parts of the Dynamo system. For instance, linking makes the removal of individual fragments from the fragment cache expensive, because all incoming branches into a fragment must be unlinked first. Linking also makes it difficult to relocate fragments in the fragment cache memory after they have been emitted. This might be useful for instance to do periodic de-fragmentation of the fragment cache memory.

---

### النسخة العربية

بعد بث شيفرة الجزء في ذاكرة الأجزاء المؤقتة، يُربَط الجزء الجديد بأجزاء أخرى موجودة بالفعل في ذاكرة الأجزاء المؤقتة. يتضمن الربط تصحيح تفريع خروج الجزء بحيث يكون هدفه المأخوذ هو نقطة دخول جزء آخر، بدلاً من عقب خروجه.

كمثال، لنفترض أن الأثر BDGIJE في الشكل 3 (a) أصبح الآن ساخناً (B هي بداية أثر صالحة حسب تعريفنا، عندما يُدخَل عبر خروج من الأثر الساخن السابق ACDGHJE). يوضح الشكل 4 الربط الذي يحدث بعد بث الجزء المقابل لأثر BDGIJE في ذاكرة الأجزاء المؤقتة. تُظهَر التفريعات المربوطة كأسهم داكنة، وتُشار إلى نسخها الأصلية غير المربوطة كأسهم فاتحة منقطة.

ربط الأجزاء ضروري للأداء، لأنه يمنع المخارج المكلفة من ذاكرة الأجزاء المؤقتة إلى مفسِّر دينامو. في تطبيق نموذجنا الأولي على PA-8000 على سبيل المثال، يؤدي تعطيل ربط الأجزاء إلى تباطؤ بترتيب من الحجم (بمتوسط عامل 40 لمعايير SpecInt95).

يوفر ربط الأجزاء أيضاً فرصة لإزالة شيفرة التعويض الزائدة من الجزء المصدر المشارك في الربط. تذكر أن محسِّن الأثر يُغرِق التكرارات على الأثر في كتل تعويض، بحيث تُنفَّذ هذه التعليمات فقط عندما يخرج التحكم من الجزء على طول مسار معين (انظر القسم 4.2). يوضح الجزء A في الشكل 5 مثل هذه الحالة، حيث كان الإسناد إلى r5 الموضح في كتلة التعويض (الحدود السميكة) في الكتلة الأولى أصلاً قبل إغراقه في كتلة التعويض الخاصة به. كجزء من معلومات الربط المحفوظة في كل عقب خروج جزء (المربعات المظللة في الشكل 5)، يُحتفَظ بقناع إسنادات السجلات الزائدة على الأثر على طول خروج الجزء المعين ذلك. في الشكل 5، سيُحفَظ هذا القناع في عقب الخروج المقابل لكتلة التعويض، وسيُعيَّن البت 5 من القناع. يُحتفَظ أيضاً بقناع مماثل لإسنادات السجلات المقتولة في أعلى كل جزء كجزء من بنية البيانات الداخلية لدينامو التي تحتفظ بمعلومات متعلقة بالجزء. في وقت الربط، إذا ظهر سجل في كلا القناعين، فإن التعليمة التي عرَّفته أخيراً في كتلة التعويض للجزء المصدر ميتة ويمكن إزالتها. يوضح هذا في الشكل 5، حيث يمكن حذف الإسناد إلى r5 في كتلة التعويض للجزء A لأن r5 مُعرَّف قبل استخدامه عند الدخول إلى الجزء B.

بينما مزايا الربط واضحة، فإن له أيضاً بعض العيوب التي تؤثر على أجزاء أخرى من نظام دينامو. على سبيل المثال، يجعل الربط إزالة الأجزاء الفردية من ذاكرة الأجزاء المؤقتة مكلفة، لأن جميع التفريعات الواردة إلى جزء يجب فك ربطها أولاً. يجعل الربط أيضاً من الصعب إعادة تموضع الأجزاء في ذاكرة الأجزاء المؤقتة بعد بثها. قد يكون هذا مفيداً على سبيل المثال للقيام بإزالة تجزئة دورية لذاكرة الأجزاء المؤقتة.

---

### Translation Notes

- **Figures referenced:** Figure 3(a), Figure 4 (fragment linking example), Figure 5 (link-time optimization)
- **Key terms introduced:** branch patching, link-time optimization, register mask, dead code elimination, compensation block
- **Performance impact:** 40x slowdown without fragment linking on SpecInt95
- **Technical details:** Register assignment masks, dead code detection at link time
- **Trade-offs:** Benefits (performance) vs. costs (difficulty of fragment removal/relocation)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
