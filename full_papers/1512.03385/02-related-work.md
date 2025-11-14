# Section 2: Related Work
## القسم 2: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.86
**Glossary Terms Used:** residual representations, vector quantization, dictionary, image retrieval, classification, Partial Differential Equations (PDEs), Multigrid method, hierarchical basis preconditioning, optimization, shortcut connections, multi-layer perceptrons (MLPs), vanishing/exploding gradients, highway networks, gating functions, parameters

---

### English Version

**Residual Representations.** In image recognition, VLAD [18] is a representation that encodes by the residual vectors with respect to a dictionary, and Fisher Vector [30] can be formulated as a probabilistic version [18] of VLAD. Both of them are powerful shallow representations for image retrieval and classification [4, 48]. For vector quantization, encoding residual vectors [17] is shown to be more effective than encoding original vectors.

In low-level vision and computer graphics, for solving Partial Differential Equations (PDEs), the widely used Multigrid method [3] reformulates the system as subproblems at multiple scales, where each subproblem is responsible for the residual solution between a coarser and a finer scale. An alternative to Multigrid is hierarchical basis preconditioning [45, 46], which relies on variables that represent residual vectors between two scales. It has been shown [3, 45, 46] that these solvers converge much faster than standard solvers that are unaware of the residual nature of the solutions. These methods suggest that a good reformulation or preconditioning can simplify the optimization.

**Shortcut Connections.** Practices and theories that lead to shortcut connections [2, 34, 49] have been studied for a long time. An early practice of training multi-layer perceptrons (MLPs) is to add a linear layer connected from the network input to the output [34, 49]. In [44, 24], a few intermediate layers are directly connected to auxiliary classifiers for addressing vanishing/exploding gradients. The papers of [39, 38, 31, 47] propose methods for centering layer responses, gradients, and propagated errors, implemented by shortcut connections. In [44], an "inception" layer is composed of a shortcut branch and a few deeper branches.

Concurrent with our work, "highway networks" [42, 43] present shortcut connections with gating functions [15]. These gates are data-dependent and have parameters, in contrast to our identity shortcuts that are parameter-free. When a gated shortcut is "closed" (approaching zero), the layers in highway networks represent non-residual functions. On the contrary, our formulation always learns residual functions; our identity shortcuts are never closed, and all information is always passed through, with additional residual functions to be learned. In addition, highway networks have not demonstrated accuracy gains with extremely increased depth (e.g., over 100 layers).

---

### النسخة العربية

**التمثيلات المتبقية.** في التعرف على الصور، VLAD [18] هو تمثيل يقوم بالترميز باستخدام المتجهات المتبقية بالنسبة إلى قاموس، ويمكن صياغة متجه فيشر [30] كنسخة احتمالية [18] من VLAD. كلاهما عبارة عن تمثيلات ضحلة قوية لاسترجاع وتصنيف الصور [4, 48]. بالنسبة للتكميم المتجهي، ثبت أن ترميز المتجهات المتبقية [17] أكثر فعالية من ترميز المتجهات الأصلية.

في الرؤية منخفضة المستوى ورسومات الحاسوب، لحل المعادلات التفاضلية الجزئية (PDEs)، تعيد طريقة Multigrid المستخدمة على نطاق واسع [3] صياغة النظام كمسائل فرعية على مقاييس متعددة، حيث تكون كل مسألة فرعية مسؤولة عن الحل المتبقي بين مقياس أخشن وآخر أدق. البديل لـ Multigrid هو التهيئة المسبقة للأساس الهرمي [45, 46]، التي تعتمد على متغيرات تمثل المتجهات المتبقية بين مقياسين. تم إثبات [3, 45, 46] أن هذه المحللات تتقارب بشكل أسرع بكثير من المحللات القياسية التي لا تدرك الطبيعة المتبقية للحلول. تشير هذه الطرق إلى أن إعادة الصياغة الجيدة أو التهيئة المسبقة يمكن أن تبسط التحسين.

**اتصالات الاختصار.** تمت دراسة الممارسات والنظريات التي تؤدي إلى اتصالات الاختصار [2, 34, 49] لفترة طويلة. كانت الممارسة المبكرة لتدريب الشبكات الإدراكية متعددة الطبقات (MLPs) هي إضافة طبقة خطية متصلة من مدخل الشبكة إلى المخرج [34, 49]. في [44, 24]، تتصل بعض الطبقات الوسيطة مباشرة بمصنفات مساعدة لمعالجة تلاشي/انفجار التدرجات. تقترح الأوراق [39, 38, 31, 47] طرقاً لتمركز استجابات الطبقات والتدرجات والأخطاء المنتشرة، والتي يتم تنفيذها بواسطة اتصالات الاختصار. في [44]، تتكون طبقة "inception" من فرع اختصار وبضعة فروع أعمق.

بالتزامن مع عملنا، تقدم "شبكات الطرق السريعة" (highway networks) [42, 43] اتصالات اختصار مع دوال بوابية [15]. هذه البوابات تعتمد على البيانات ولها معاملات، على النقيض من اختصارات الهوية الخاصة بنا التي لا تحتوي على معاملات. عندما تكون بوابة الاختصار "مغلقة" (تقترب من الصفر)، تمثل الطبقات في شبكات الطرق السريعة دوال غير متبقية. على العكس من ذلك، صيغتنا تتعلم دائماً دوال متبقية؛ اختصارات الهوية الخاصة بنا لا تُغلق أبداً، وتمر جميع المعلومات دائماً، مع دوال متبقية إضافية لتعلمها. بالإضافة إلى ذلك، لم تُظهر شبكات الطرق السريعة مكاسب في الدقة مع العمق المتزايد بشكل كبير (مثل أكثر من 100 طبقة).

---

### Translation Notes

- **Key concepts discussed:**
  - Prior work on residual representations (VLAD, Fisher Vector)
  - Mathematical methods using residuals (Multigrid, hierarchical basis preconditioning)
  - History of shortcut connections in neural networks
  - Comparison with highway networks

- **Key terms introduced:**
  - residual representations (التمثيلات المتبقية)
  - vector quantization (التكميم المتجهي)
  - dictionary (قاموس)
  - image retrieval (استرجاع الصور)
  - Partial Differential Equations (PDEs) (المعادلات التفاضلية الجزئية)
  - Multigrid method (طريقة Multigrid)
  - hierarchical basis preconditioning (التهيئة المسبقة للأساس الهرمي)
  - multi-layer perceptrons (MLPs) (الشبكات الإدراكية متعددة الطبقات)
  - auxiliary classifiers (مصنفات مساعدة)
  - highway networks (شبكات الطرق السريعة)
  - gating functions (دوال بوابية)
  - parameter-free (لا تحتوي على معاملات)
  - inception layer (طبقة inception)

- **Important comparisons:**
  - ResNet vs Highway Networks: Identity shortcuts (parameter-free) vs gated shortcuts (with parameters)
  - ResNet always learns residual functions; Highway Networks can represent non-residual functions when gates close
  - ResNet demonstrates gains with 100+ layers; Highway Networks do not

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
