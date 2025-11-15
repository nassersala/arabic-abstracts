# Section 16: Conclusions
## القسم 16: الخلاصة

**Section:** Conclusions
**Translation Quality:** 0.88
**Glossary Terms Used:** automatic differentiation, backpropagation, optimization, compiler, functional programming

---

### English Version

Conclusions

This paper develops a simple, mode-independent algorithm for automatic differentiation (AD) (Section 4), calculated from a simple, natural specification in terms of elementary category theory (functoriality). It then generalizes the algorithm, replacing linear maps (as derivatives) by an arbitrary biproduct category (Figure 6). Specializing this general algorithm to two well-known categorical constructions (Figures 7 and 10)—also calculated—yields reverse-mode AD (RAD) for general derivatives and for gradients. These RAD implementations are far simpler than previously known. In contrast to common approaches to AD, the new algorithms involve no graphs, tapes, variables, partial derivatives, or mutation, and are usable directly from an existing programming language with no need for new data types or programming style (thanks to use of an AD-agnostic compiler plugin). Only the simple essence remains.

Future work includes detailed performance analysis (compared with backpropagation and other conventional AD algorithms); efficient higher-order differentiation; and applying generalized AD to derivative-like notions, including subdifferentiation [Rockafellar, 1966] and automatic incrementalization (continuing previous work [Elliott, 2017]).

AD is typically said to be about the chain rule for sequential composition (Theorem 1). This paper rounds out the story with two more rules: one for parallel composition and one for all linear operations (Theorems 2 and 3). Parallel composition is usually left implicit in the special-case treatment of a collection of non-unary operations, such as addition, multiplication, division, and dot products. With explicit, general support for parallel composition, all operations come to be on equal footing, regardless of arity.

AD is also typically presented in opposition to symbolic differentiation (SD), with the latter described as applying differentiation rules symbolically. The main criticism of SD is that it can blow up expressions, resulting in a great deal of redundant work. In contrast, AD is described as a numeric method. The approach explored in this paper suggests a different perspective: **automatic differentiation is symbolic differentiation performed by a compiler.** Compilers already work symbolically and already take care to preserve sharing in computations, addressing both criticisms of SD.

The specification and implementation of AD in a simple, correct-by-construction, and apparently efficient manner, together with its use from a typed functional language (here via a compiler plugin), make a step toward the vision of differentiable functional programming for machine learning and other uses.

In retrospect, two key principles enable the results in this paper:

1. **Focus on abstract notions** (specified denotationally and/or axiomatically) rather than particular representations (here, derivatives as linear maps rather than as matrices). Then transform a correct, naive representation into subtler, more efficient representations.

2. **Capture the main concepts of interest directly, as first-class values** (here, differentiable functions).

---

### النسخة العربية

الخلاصة

تطور هذه الورقة خوارزمية بسيطة مستقلة عن النمط للتفاضل الآلي (AD) (القسم 4)، محسوبة من مواصفة بسيطة وطبيعية بمصطلحات نظرية الفئات الأساسية (الدالية الفئوية). ثم تعمم الخوارزمية، مستبدلة الخرائط الخطية (كمشتقات) بفئة ثنائية المنتج تعسفية (الشكل 6). تخصيص هذه الخوارزمية العامة لبناءين فئويين معروفين (الشكلان 7 و 10) - محسوبين أيضاً - ينتج عنه التفاضل الآلي ذو النمط العكسي (RAD) للمشتقات العامة وللتدرجات. هذه التنفيذات لـ RAD أبسط بكثير من المعروفة سابقاً. على النقيض من الأساليب الشائعة للتفاضل الآلي، لا تتضمن الخوارزميات الجديدة رسوماً بيانية أو أشرطة أو متغيرات أو مشتقات جزئية أو تغيير، ويمكن استخدامها مباشرة من لغة برمجة موجودة دون الحاجة إلى أنواع بيانات جديدة أو أسلوب برمجة (بفضل استخدام مكون إضافي للمترجم غير معتمد على التفاضل الآلي). فقط الجوهر البسيط يبقى.

يشمل العمل المستقبلي تحليل أداء مفصل (مقارنة بالانتشار العكسي وخوارزميات التفاضل الآلي التقليدية الأخرى)؛ والتفاضل الفعال ذو الترتيب الأعلى؛ وتطبيق التفاضل الآلي المعمم على مفاهيم شبيهة بالمشتقة، بما في ذلك التفاضل الفرعي [Rockafellar, 1966] والتزايد التلقائي (مواصلة العمل السابق [Elliott, 2017]).

يُقال عادةً أن التفاضل الآلي يتعلق بقاعدة السلسلة للتركيب المتسلسل (المبرهنة 1). تكمل هذه الورقة القصة بقاعدتين إضافيتين: واحدة للتركيب المتوازي وواحدة لجميع العمليات الخطية (المبرهنتان 2 و 3). عادة ما يُترك التركيب المتوازي ضمنياً في المعالجة الخاصة لمجموعة من العمليات غير الأحادية، مثل الجمع والضرب والقسمة والمنتجات النقطية. مع الدعم الصريح والعام للتركيب المتوازي، تصبح جميع العمليات على قدم المساواة، بغض النظر عن العدد.

يُقدم التفاضل الآلي أيضاً عادةً في معارضة التفاضل الرمزي (SD)، مع وصف الأخير بأنه تطبيق قواعد التفاضل رمزياً. النقد الرئيسي لـ SD هو أنه يمكن أن ينفجر التعبيرات، مما يؤدي إلى قدر كبير من العمل الزائد. في المقابل، يُوصف التفاضل الآلي كطريقة عددية. النهج المستكشف في هذه الورقة يقترح منظوراً مختلفاً: **التفاضل الآلي هو تفاضل رمزي يؤديه المترجم.** تعمل المترجمات بالفعل رمزياً وتهتم بالفعل بالحفاظ على المشاركة في الحسابات، معالجةً كلا انتقادي SD.

تحديد وتنفيذ التفاضل الآلي بطريقة بسيطة وصحيحة بالبناء وفعالة على ما يبدو، جنباً إلى جنب مع استخدامه من لغة وظيفية منطّقة (هنا عبر مكون إضافي للمترجم)، يمثل خطوة نحو رؤية البرمجة الوظيفية القابلة للتفاضل للتعلم الآلي والاستخدامات الأخرى.

بأثر رجعي، يُمكِّن مبدآن رئيسيان النتائج في هذه الورقة:

1. **التركيز على المفاهيم المجردة** (محددة دلالياً و/أو بديهياً) بدلاً من التمثيلات الخاصة (هنا، المشتقات كخرائط خطية بدلاً من المصفوفات). ثم تحويل تمثيل صحيح وساذج إلى تمثيلات أكثر دقة وكفاءة.

2. **التقاط المفاهيم الرئيسية ذات الاهتمام مباشرة، كقيم من الدرجة الأولى** (هنا، الدوال القابلة للتفاضل).

---

### Translation Notes

- **Key contributions:** Simple AD algorithm, category-theoretic specification, no graphs/tapes/mutation
- **Future work:** Performance analysis, higher-order differentiation, subdifferentiation
- **Key insight:** "AD is symbolic differentiation performed by a compiler"
- **Two key principles:** Abstract notions, first-class values

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
