# Section 9: Related Work and Conclusion
## القسم 9: الأعمال ذات الصلة والخلاصة

**Section:** related-work-and-conclusion
**Translation Quality:** 0.86
**Glossary Terms Used:** JIT compiler, dynamic compilation, selective dynamic compilation, binary translator, hardware optimizer, trace cache, native-to-native optimization

---

### English Version

## 9. Related Work

In focusing on native-to-native runtime optimization, Dynamo is a fundamentally different approach from past work on dynamic compilation. Just-in-time compilers delay all compilation until runtime [6][11][10]. Selective dynamic compilation [1][9][23][13][22][26][16][24] is a staged form of compilation that restricts dynamic compilation to selected portions of code identified by user annotations or source language extensions. In these cases, the static compiler prepares the dynamic compilation process as much as possible by generating templates that are instantiated at run-time by a specialized dynamic compiler. These generate profile data during the initial run via emulation, and perform background translation together with optimization of hot spots based on the profile data. The benefit of the profile-based optimization is only available during subsequent runs of the program and the initial profile-collecting run may suffer from worsened performance.

In contrast to both just-in-time and selective dynamic compilation, Dynamo separates the task of compilation, which occurs prior to execution, from dynamic optimization, which occurs entirely at runtime and without requiring user assistance. Dynamo's input is an already compiled native instruction stream, that is re-optimized to exploit performance opportunities that manifest themselves at runtime.

A lot of work has been done on dynamic translation as a technique for non-native system emulation [8][30][5][31][12][17]. The idea is to lower emulation overhead by caching native code translations of frequently interpreted regions. Unlike such binary translators, Dynamo is not concerned with translation. The Dynamo approach does however allow one to couple a fast lightweight translator that emits native code to Dynamo, which then becomes a backend optimizer.

There are several implementations of offline binary translators that also perform native code optimization [7][29]. Hardware solutions for a limited form of runtime code optimization are now commonplace in modern superscalar microprocessors [21][25][19]. The optimization unit is a fixed size instruction window, with the optimization logic operating on the critical execution path. The Trace Cache is another hardware alternative that can be extended to do superscalar-like optimization off the critical path [27][15]. Dynamo offers the potential for a purely software alternative, which could allow it to be tailored to specific application domains, and cooperate with the compiler or JIT in ways that hardware dynamic optimizers cannot.

## 10. Conclusion

Dynamo is a novel performance delivery mechanism. It complements the compiler's traditional strength as a static performance improvement tool by providing a dynamic optimization capability. In contrast to other approaches to dynamic optimization, Dynamo works transparently, requiring no user intervention. This fact allows Dynamo to be bundled with a computer system, and shipped as a client-side performance delivery mechanism, whose activation does not depend on the ISVs (independent software vendors) in the way that traditional compiler optimizations do.

This paper demonstrates that it is possible to engineer a practical software dynamic optimizer that provides a significant performance benefit even on highly optimized executables produced by a static compiler. The key is to focus the optimization effort on opportunities that are likely to manifest themselves only at runtime, and hence those that a static compiler might miss.

We are currently investigating applications of Dynamo's dynamic optimization technology in many different areas. One of the directions we are exploring is to export an API to the application program, so that a "Dynamo-aware" application can use the underlying system in interesting ways. This might be useful for example to implement a very low-overhead profiler, or a JIT compiler. From Dynamo's perspective, user and/or compiler hints provided via this API might allow it to perform more comprehensive optimizations that go beyond the scope of individual traces. Finally, we are also looking at the problem of transparent de-optimization at runtime.

---

### النسخة العربية

## 9. الأعمال ذات الصلة

من خلال التركيز على التحسين الأصلي إلى الأصلي في وقت التشغيل، دينامو هو نهج مختلف بشكل أساسي عن الأعمال السابقة على الترجمة الديناميكية. مترجمات JIT تؤخر كل الترجمة حتى وقت التشغيل [6][11][10]. الترجمة الديناميكية الانتقائية [1][9][23][13][22][26][16][24] هي شكل مرحلي من الترجمة يقيد الترجمة الديناميكية بأجزاء مختارة من الشيفرة محددة بواسطة تعليقات توضيحية من المستخدم أو امتدادات لغة المصدر. في هذه الحالات، يعد المترجم الساكن عملية الترجمة الديناميكية قدر الإمكان بتوليد قوالب يتم إنشاء نسخ منها في وقت التشغيل بواسطة مترجم ديناميكي متخصص. هذه تولِّد بيانات ملف التعريف أثناء التشغيل الأولي عبر المحاكاة، وتجري ترجمة خلفية مع تحسين النقاط الساخنة استناداً إلى بيانات ملف التعريف. فائدة التحسين القائم على ملف التعريف متاحة فقط أثناء التشغيلات اللاحقة للبرنامج وقد يعاني تشغيل جمع ملف التعريف الأولي من أداء أسوأ.

على النقيض من كل من الترجمة في الوقت المناسب والترجمة الديناميكية الانتقائية، يفصل دينامو مهمة الترجمة، التي تحدث قبل التنفيذ، عن التحسين الديناميكي، الذي يحدث بالكامل في وقت التشغيل ودون الحاجة إلى مساعدة المستخدم. مدخل دينامو هو تسلسل تعليمات أصلية مُترجَم بالفعل، يُعاد تحسينه لاستغلال فرص الأداء التي تظهر في وقت التشغيل.

تم إنجاز الكثير من العمل على الترجمة الديناميكية كتقنية لمحاكاة النظام غير الأصلي [8][30][5][31][12][17]. الفكرة هي تقليل تكلفة المحاكاة عن طريق تخزين ترجمات الشيفرة الأصلية مؤقتاً للمناطق المفسَّرة بشكل متكرر. على عكس مثل هذه المترجمات الثنائية، دينامو لا يهتم بالترجمة. ومع ذلك، فإن نهج دينامو يسمح بربط مترجم سريع وخفيف الوزن يبث شيفرة أصلية لدينامو، والذي يصبح بعد ذلك محسِّناً خلفياً.

هناك العديد من تطبيقات المترجمات الثنائية غير المتصلة التي تجري أيضاً تحسين الشيفرة الأصلية [7][29]. أصبحت الحلول العتادية لشكل محدود من تحسين الشيفرة في وقت التشغيل شائعة الآن في المعالجات الدقيقة الفائقة التدرج الحديثة [21][25][19]. وحدة التحسين هي نافذة تعليمات بحجم ثابت، مع منطق التحسين الذي يعمل على مسار التنفيذ الحرج. ذاكرة الأثر المؤقتة (Trace Cache) هي بديل عتادي آخر يمكن تمديده للقيام بتحسين شبيه بالفائق التدرج خارج المسار الحرج [27][15]. يقدم دينامو إمكانية لبديل برمجي بحت، والذي يمكن أن يسمح بتخصيصه لمجالات تطبيقات محددة، والتعاون مع المترجم أو JIT بطرق لا تستطيع المحسِّنات الديناميكية العتادية القيام بها.

## 10. الخلاصة

دينامو آلية جديدة لتوصيل الأداء. يكمل قوة المترجم التقليدية كأداة تحسين أداء ساكنة من خلال توفير قدرة تحسين ديناميكية. على عكس النهج الأخرى للتحسين الديناميكي، يعمل دينامو بشكل شفاف، دون الحاجة إلى تدخل المستخدم. تسمح هذه الحقيقة بتجميع دينامو مع نظام حاسوب، وشحنه كآلية توصيل أداء من جانب العميل، حيث تفعيله لا يعتمد على موردي البرمجيات المستقلين (ISVs) بالطريقة التي تعتمد بها تحسينات المترجم التقليدية.

تُظهِر هذه الورقة أنه من الممكن هندسة محسِّن ديناميكي برمجي عملي يوفر فائدة أداء كبيرة حتى على الملفات التنفيذية المحسَّنة بشكل كبير والمنتَجة بواسطة مترجم ساكن. المفتاح هو التركيز على جهد التحسين على الفرص التي من المحتمل أن تظهر فقط في وقت التشغيل، وبالتالي تلك التي قد يفوتها المترجم الساكن.

نحن نحقق حالياً في تطبيقات تقنية التحسين الديناميكي لدينامو في العديد من المجالات المختلفة. أحد الاتجاهات التي نستكشفها هو تصدير واجهة برمجة تطبيقات إلى برنامج التطبيق، بحيث يمكن لتطبيق "واعٍ بدينامو" استخدام النظام الأساسي بطرق مثيرة للاهتمام. قد يكون هذا مفيداً على سبيل المثال لتطبيق محلل أداء منخفض التكلفة للغاية، أو مترجم JIT. من منظور دينامو، قد تسمح التلميحات من المستخدم و/أو المترجم المقدمة عبر واجهة برمجة التطبيقات هذه بإجراء تحسينات أكثر شمولاً تتجاوز نطاق الآثار الفردية. أخيراً، ننظر أيضاً في مشكلة إزالة التحسين الشفافة في وقت التشغيل.

---

### Translation Notes

- **Key comparisons:** JIT vs. selective dynamic compilation vs. Dynamo's approach
- **Related systems:** Binary translators, hardware optimizers, Trace Cache
- **Future directions:** API for Dynamo-aware applications, transparent de-optimization
- **Core contribution:** Native-to-native optimization without user intervention
- **References:** Multiple citations to related work [1]-[31]

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
