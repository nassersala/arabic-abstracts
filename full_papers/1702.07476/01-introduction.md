# Section 1: Introduction
## القسم 1: مقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** differential privacy, privacy, mechanism, composition, privacy loss, privacy budget, Gaussian mechanism, Laplace mechanism

---

### English Version

Differential privacy, introduced by Dwork et al. [1], has been embraced by multiple research communities as a commonly accepted notion of privacy for algorithms on statistical databases. As applications of differential privacy begin to emerge, practical concerns of tracking and communicating privacy guarantees are coming to the fore.

Informally, differential privacy bounds a shift in the output distribution of a randomized algorithm that can be induced by a small change in its input. The standard definition of ε-differential privacy puts a multiplicative upper bound on the worst-case change in the distribution's density.

Several relaxations of differential privacy explored other measures of closeness between two distributions. The most common such relaxation, the (ε, δ) definition, has been a method of choice for expressing privacy guarantees of a variety of differentially private algorithms, especially those that rely on the Gaussian additive noise mechanism or whose analysis follows from composition theorems. The additive δ parameter allows suppressing the long tails of the mechanism's distribution where pure ε-differential privacy guarantees may not hold.

Compared to the standard definition, (ε, δ)-differential privacy offers asymptotically smaller cumulative loss under composition and allows greater flexibility in the selection of privacy-preserving mechanisms.

Despite its notable advantages and numerous applications, the definition of (ε, δ)-differential privacy is an imperfect fit for its two most common use cases: the Gaussian mechanism and a composition rule. We briefly sketch them here and elaborate on these points in the next section.

The first application of (ε, δ)-differential privacy was the analysis of the Gaussian noise mechanism [2]. In contrast with the Laplace mechanism, whose privacy guarantee is characterized tightly and accurately by ε-differential privacy, a single Gaussian mechanism satisfies a curve of (ε(δ), δ)-differential privacy definitions. Picking any one point on this curve leaves out important information about the mechanism's actual behavior.

The second common use of (ε, δ)-differential privacy is due to applications of advanced composition theorems. The central feature of ε-differential privacy is that it is closed under composition; moreover, the ε parameters of composed mechanisms simply add up, which motivates the concept of a privacy budget. By relaxing the guarantee to (ε, δ)-differential privacy, advanced composition allows tighter analyses for compositions of (pure) differentially private mechanisms. Iterating this process, however, quickly leads to a combinatorial explosion of parameters, as each application of an advanced composition theorem leads to a wide selection of possibilities for (ε(δ), δ)-differentially private guarantees.

In part to address the shortcomings of (ε, δ)-differential privacy, several recent works, surveyed in the next section, explored the use of higher-order moments as a way of bounding the tails of the privacy loss variable.

Inspired by these theoretical results and their applications, we propose Rényi differential privacy as a natural relaxation of differential privacy that is well-suited for expressing guarantees of privacy-preserving algorithms and for composition of heterogeneous mechanisms. Compared to (ε, δ)-differential privacy, Rényi differential privacy is a strictly stronger privacy definition. It offers an operationally convenient and quantitatively accurate way of tracking cumulative privacy loss throughout execution of a standalone differentially private mechanism and across many such mechanisms. Most significantly, Rényi differential privacy allows combining the intuitive and appealing concept of a privacy budget with application of advanced composition theorems.

The paper presents a self-contained exposition of the new definition, unifying current literature and demonstrating its applications. The organization of the paper is as follows. Section II reviews the standard definition of differential privacy, its (ε, δ) relaxation and its most common uses. Section III introduces the definition of Rényi differential privacy and proves its basic properties that parallel those of ε-differential privacy, summarizing the results in Table I. Section IV demonstrates a reduction from Rényi differential privacy to (ε, δ)-differential privacy, followed by a proof of an advanced composition theorem in Section V. Section VI applies Rényi differential privacy to analysis of several basic mechanisms: randomized response for predicates, Laplace and Gaussian (see Table II for a brief summary). Section VII discusses assessment of risk due to application of a Rényi differentially private mechanism and use of Rényi differential privacy as a privacy loss tracking tool. Section VIII concludes with open questions.

---

### النسخة العربية

تم تقديم الخصوصية التفاضلية من قبل Dwork وآخرين [1]، وقد تبنتها مجتمعات بحثية متعددة كمفهوم مقبول عمومًا للخصوصية للخوارزميات على قواعد البيانات الإحصائية. مع بدء ظهور تطبيقات الخصوصية التفاضلية، تبرز المخاوف العملية لتتبع وإيصال ضمانات الخصوصية إلى الواجهة.

بشكل غير رسمي، تحد الخصوصية التفاضلية من التحول في توزيع مخرجات خوارزمية عشوائية يمكن أن ينتج عن تغيير صغير في مدخلاتها. يضع التعريف القياسي للخصوصية التفاضلية ε حدًا أعلى تضاعفيًا على التغيير في أسوأ الحالات في كثافة التوزيع.

استكشفت عدة تخفيفات للخصوصية التفاضلية مقاييس أخرى للقرب بين توزيعين. التخفيف الأكثر شيوعًا، تعريف (ε, δ)، كان طريقة الاختيار للتعبير عن ضمانات الخصوصية لمجموعة متنوعة من الخوارزميات الخاصة تفاضليًا، خاصة تلك التي تعتمد على آلية الضوضاء الجمعية الغاوسية أو التي يتبع تحليلها من نظريات التركيب. يسمح معامل δ الجمعي بقمع الذيول الطويلة لتوزيع الآلية حيث قد لا تصمد ضمانات الخصوصية التفاضلية النقية ε.

بالمقارنة مع التعريف القياسي، توفر الخصوصية التفاضلية (ε, δ) خسارة تراكمية أصغر تدريجيًا تحت التركيب وتسمح بمرونة أكبر في اختيار آليات الحفاظ على الخصوصية.

على الرغم من مزاياها الملحوظة والتطبيقات العديدة، فإن تعريف الخصوصية التفاضلية (ε, δ) ليس مناسبًا بشكل مثالي لحالتي الاستخدام الأكثر شيوعًا: آلية غاوس وقاعدة التركيب. نحدد هذه الحالات بإيجاز هنا ونوضح هذه النقاط في القسم التالي.

كان التطبيق الأول للخصوصية التفاضلية (ε, δ) هو تحليل آلية الضوضاء الغاوسية [2]. على النقيض من آلية لابلاس، التي يتم توصيف ضمان الخصوصية الخاص بها بإحكام ودقة من خلال الخصوصية التفاضلية ε، فإن آلية غاوس واحدة تحقق منحنى من تعريفات الخصوصية التفاضلية (ε(δ), δ). إن اختيار أي نقطة واحدة على هذا المنحنى يترك معلومات مهمة حول السلوك الفعلي للآلية.

الاستخدام الثاني الشائع للخصوصية التفاضلية (ε, δ) يرجع إلى تطبيقات نظريات التركيب المتقدمة. الميزة المركزية للخصوصية التفاضلية ε هي أنها مغلقة تحت التركيب؛ علاوة على ذلك، فإن معاملات ε للآليات المركبة تجمع ببساطة، مما يحفز مفهوم ميزانية الخصوصية. من خلال تخفيف الضمان إلى الخصوصية التفاضلية (ε, δ)، يسمح التركيب المتقدم بتحليلات أكثر إحكامًا لتركيبات الآليات الخاصة تفاضليًا (النقية). ومع ذلك، فإن تكرار هذه العملية يؤدي بسرعة إلى انفجار تجميعي في المعاملات، حيث يؤدي كل تطبيق لنظرية تركيب متقدمة إلى مجموعة واسعة من الاحتمالات لضمانات الخصوصية التفاضلية (ε(δ), δ).

جزئيًا لمعالجة أوجه القصور في الخصوصية التفاضلية (ε, δ)، استكشفت العديد من الأعمال الحديثة، التي تم استعراضها في القسم التالي، استخدام العزوم ذات الرتب الأعلى كوسيلة لتحديد ذيول متغير خسارة الخصوصية.

مستوحين من هذه النتائج النظرية وتطبيقاتها، نقترح الخصوصية التفاضلية لريني كتخفيف طبيعي للخصوصية التفاضلية مناسب تمامًا للتعبير عن ضمانات خوارزميات الحفاظ على الخصوصية ولتركيب الآليات غير المتجانسة. بالمقارنة مع الخصوصية التفاضلية (ε, δ)، فإن الخصوصية التفاضلية لريني هي تعريف خصوصية أقوى بشكل صارم. إنها توفر طريقة ملائمة تشغيليًا ودقيقة كميًا لتتبع خسارة الخصوصية التراكمية طوال تنفيذ آلية خاصة تفاضليًا مستقلة وعبر العديد من هذه الآليات. الأهم من ذلك، تسمح الخصوصية التفاضلية لريني بدمج مفهوم ميزانية الخصوصية البديهي والجذاب مع تطبيق نظريات التركيب المتقدمة.

تقدم الورقة عرضًا مكتفيًا ذاتيًا للتعريف الجديد، مع توحيد الأدبيات الحالية وإظهار تطبيقاته. تنظيم الورقة كما يلي. يراجع القسم الثاني التعريف القياسي للخصوصية التفاضلية، وتخفيف (ε, δ) الخاص به واستخداماته الأكثر شيوعًا. يقدم القسم الثالث تعريف الخصوصية التفاضلية لريني ويثبت خصائصها الأساسية التي توازي تلك الخاصة بالخصوصية التفاضلية ε، مع تلخيص النتائج في الجدول الأول. يوضح القسم الرابع اختزالًا من الخصوصية التفاضلية لريني إلى الخصوصية التفاضلية (ε, δ)، يليه برهان نظرية تركيب متقدمة في القسم الخامس. يطبق القسم السادس الخصوصية التفاضلية لريني على تحليل العديد من الآليات الأساسية: الاستجابة العشوائية للمحمولات، ولابلاس وغاوس (انظر الجدول الثاني للحصول على ملخص موجز). يناقش القسم السابع تقييم المخاطر بسبب تطبيق آلية خاصة تفاضليًا لريني واستخدام الخصوصية التفاضلية لريني كأداة لتتبع خسارة الخصوصية. يختتم القسم الثامن بأسئلة مفتوحة.

---

### Translation Notes

- **Key terms introduced:**
  - Rényi differential privacy (الخصوصية التفاضلية لريني)
  - privacy budget (ميزانية الخصوصية)
  - Gaussian mechanism (آلية غاوس)
  - Laplace mechanism (آلية لابلاس)
  - advanced composition theorems (نظريات التركيب المتقدمة)
  - higher-order moments (العزوم ذات الرتب الأعلى)
  - privacy loss variable (متغير خسارة الخصوصية)
  - heterogeneous mechanisms (آليات غير متجانسة)
  - randomized response (الاستجابة العشوائية)

- **Figures referenced:** None in this section
- **Equations:** None in this section
- **Citations:** [1], [2]
- **Special handling:** Technical terminology requires precise translation to maintain mathematical rigor

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
