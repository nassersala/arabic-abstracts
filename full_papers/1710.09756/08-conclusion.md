# Section 8: Conclusion
## القسم 8: الخلاصة

**Section:** Conclusion
**Translation Quality:** 0.87
**Glossary Terms Used:** linear types, type system, backwards compatibility, compiler, pure functions, lazy evaluation

---

### English Version

This article demonstrates how an existing lazy language, such as Haskell, can be extended with linear types, without compromising the language, in the sense that:

• existing programs are valid in the extended language without modification,
• such programs retain the same operational semantics, and in particular
• the performance of existing programs is not affected,
• yet existing library functions can be reused to serve the objectives of resource-sensitive programs with simple changes to their types, and no code duplication.

In other words: regular Haskell comes first. Additionally, first-order linearly typed functions and data structures are usable directly from regular Haskell code. In such a setting their semantics is that of the same code with linearity erased.

Linear Haskell was engineered as an unintrusive design, making it tractable to integrate to an existing, mature compiler with a large ecosystem. We have developed a prototype implementation extending GHC with multiplicities. As we hoped, this design integrates well in GHC.

Even though we change only GHC's type system, we found that the compiler and runtime already had the features necessary for unboxed, off-heap, and in-place data structures. That is, GHC has the low-level compiler primitives and FFI support to implement, for example, mutable arrays, mutable cursors into serialised data, or off-heap foreign data structures without garbage collection. These features could be used before this work, but their correct use put some burden-of-proof on the programmers. Linearity unlocks these capabilities for safe, compiler-checked use, within pure code.

---

### النسخة العربية

يوضح هذا المقال كيف يمكن توسيع لغة كسولة موجودة، مثل Haskell، بالأنواع الخطية، دون المساس باللغة، بمعنى أن:

• البرامج الموجودة صالحة في اللغة الموسعة دون تعديل،
• تحتفظ هذه البرامج بنفس الدلالات التشغيلية، وعلى وجه الخصوص
• لا يتأثر أداء البرامج الموجودة،
• ومع ذلك يمكن إعادة استخدام دوال المكتبة الموجودة لخدمة أهداف البرامج الحساسة للموارد بتغييرات بسيطة على أنواعها، ودون تكرار الشفرة.

بعبارة أخرى: Haskell العادي يأتي أولاً. بالإضافة إلى ذلك، فإن الدوال وبنى البيانات المكتوبة خطياً من الدرجة الأولى قابلة للاستخدام مباشرة من شفرة Haskell العادية. في مثل هذا الإعداد، تكون دلالاتها هي دلالات نفس الشفرة مع محو الخطية.

تم تصميم Haskell الخطي كتصميم غير تدخلي، مما يجعل من الممكن دمجه في مترجم ناضج موجود بنظام بيئي كبير. لقد طورنا نموذجاً أولياً يمدد GHC بالتعدديات. كما كنا نأمل، يندمج هذا التصميم بشكل جيد في GHC.

على الرغم من أننا نغير نظام الأنواع في GHC فقط، وجدنا أن المترجم ووقت التشغيل لديهما بالفعل الميزات اللازمة لبنى البيانات غير المعبأة وخارج الكومة والتحديث في المكان. أي أن GHC لديه الأوليات منخفضة المستوى للمترجم ودعم FFI لتنفيذ، على سبيل المثال، المصفوفات القابلة للتغيير، والمؤشرات القابلة للتغيير في البيانات المسلسلة، أو بنى البيانات الأجنبية خارج الكومة بدون جمع القمامة. كان من الممكن استخدام هذه الميزات قبل هذا العمل، لكن استخدامها الصحيح وضع بعض عبء الإثبات على المبرمجين. تفتح الخطية هذه القدرات للاستخدام الآمن الذي يفحصه المترجم، داخل الشفرة النقية.

---

### Translation Notes

- **Key achievements:**
  - Backwards compatibility (التوافق العكسي)
  - Non-invasive design (تصميم غير تدخلي)
  - Preservation of semantics (الحفاظ على الدلالات)
  - Unlocking safe low-level features (فتح الميزات منخفضة المستوى الآمنة)
- **Technical highlights:**
  - Type system extension only (امتداد نظام الأنواع فقط)
  - Compiler-checked safety (السلامة التي يفحصها المترجم)
  - Pure code with mutability (شفرة نقية مع القابلية للتغيير)
- **Main message:** Linear types integrate seamlessly into Haskell while preserving all existing code

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
