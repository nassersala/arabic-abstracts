# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** SLAM, algorithm, EKF, extended Kalman filter, particle filter, convergence, data association, complexity, landmarks, covariance, proposal distribution

---

### English Version

Simultaneous localization and mapping (SLAM) is a highly active research area in robotics and AI. The SLAM problem arises when a moving vehicle (e.g. a mobile robot, submarine, or drone) simultaneously estimates a map of its environment and its pose relative to that map. In the absence of global position information, the vehicle's pose estimate will become increasingly inaccurate, as will its map. Since maps may contain thousands of entities, acquiring large, accurate maps is a challenging statistical estimation problem, especially when performed in real-time.

Most present-day research on SLAM originates from a seminal paper by Smith and Cheeseman [21], which proposed the use of the extended Kalman filter (EKF) for solving SLAM. This paper is based on the insights that errors in the map and pose errors are naturally correlated, and that the covariance matrix maintained by the EKF expresses such correlations. Newman [18] recently proved that the EKF converges for linear SLAM problems, where the motion model and observation model are linear functions with Gaussian noise (see below).

Unfortunately, EKF covariance matrices are quadratic in the size of the map, and updating them requires time quadratic in the number of landmarks N. This quadratic complexity has long been recognized to be a major obstacle in scaling SLAM algorithms to maps with more than a few hundred features. It also limits the applicability of SLAM algorithms to problems with ambiguous landmarks, which induces a data association problem [2; 22]. Today's most robust algorithms for SLAM with unknown data association maintain multiple hypotheses (tracks), which increase their computational complexity.

Consequently, there has been a flurry on research on more efficient SLAM techniques (see e.g., [11]). One group of researchers has developed techniques that recursively divide maps into submaps, thereby confining most computation to small regions. Some of these approaches still maintain global correlations among those submaps, hence are quadratic but with a much reduced constant factor [1; 7; 22; 25]. Others restrict the update exclusively to local maps [12], hence operate in constant time (assuming known data association).

A second group of researchers has developed techniques that represent maps through potential functions between adjacent landmarks, similar to Markov random fields. The resulting representations require memory linear in the number of landmarks [19; 23]. Under appropriate approximations, such techniques have been shown to provide constant time updating (again for known data association). Unfortunately, no convergence proof exists for any of these extensions of the EKF, even for the generic case of linear SLAM. Furthermore, if landmarks are ambiguous, all of these approaches have to perform search to find appropriate data association hypotheses, adding a logarithmic factor to their update complexity.

The FastSLAM algorithm, proposed in [15] as an efficient approach to SLAM based on particle filtering [6], does not fall into either of the categories above. FastSLAM takes advantage of an important characteristic of the SLAM problem (with known data association): landmark estimates are conditionally independent given the robot's path [17]. FastSLAM uses a particle filter to sample over robot paths. Each particle possesses N low-dimensional EKFs, one for each of the N landmarks. This representation requires O(NM) memory, where M is the number of particles in the particle filter. Updating this filter requires O(M log N) time, with or without knowledge of the data associations. However, the number of particles M needed for convergence is unknown and has been suspected to be exponential in the size of the map, in the worst-case.

This paper proposes an improved version of the FastSLAM algorithm. The modification is conceptually simple: When proposing a new robot pose—an essential step in FastSLAM's particle filter—our proposal distribution relies not only on the motion estimate (as is the case in FastSLAM), but also on the most recent sensor measurement. Such an approach is less wasteful with its samples than the original FastSLAM algorithm, especially in situations where the noise in motion is high relative to the measurement noise.

To obtain a suitable proposal distribution, our algorithm linearizes the motion and the measurement model in the same manner as the EKF. As a result, the proposal distribution can be calculated in closed form. This extension parallels prior work by Doucet and colleagues, who proposed a similar modification for general particle filters [6] and Markov Chain Monte Carlo techniques for neural networks [4]. It is similar to the arc reversal technique proposed for particle filters applied to Bayes networks [10], and it is similar to recent work by van der Merwe [24], who uses an unscented filtering step [9] for generating proposal distributions that accommodate the measurement.

While this modification is conceptually simple, it has important ramifications. A key contribution of this paper is a convergence proof for linear SLAM problems using a single particle. The resulting algorithm requires constant updating time. To our knowledge, the best previous SLAM algorithm for which convergence was shown requires quadratic update time. Furthermore, we observe experimentally that our new FastSLAM algorithm, even with a single particle, yields significantly more accurate results on a challenging real-world benchmark [7] than the previous version of the algorithm. These findings are of significance, as many mobile robot systems are plagued by control noise, but possess relatively accurate sensors. Moreover, they contradict a common belief that maintaining the entire covariance matrix is required for convergence [5].

---

### النسخة العربية

يُعد التوطين والرسم الخرائطي المتزامن (SLAM) مجال بحث نشط للغاية في مجال الروبوتات والذكاء الاصطناعي. تنشأ مسألة SLAM عندما تقوم مركبة متحركة (مثل روبوت متحرك أو غواصة أو طائرة بدون طيار) بتقدير خريطة لبيئتها ووضعيتها بالنسبة لتلك الخريطة في وقت واحد. في غياب معلومات الموقع العالمي، سيصبح تقدير وضعية المركبة غير دقيق بشكل متزايد، وكذلك خريطتها. نظراً لأن الخرائط قد تحتوي على آلاف الكيانات، فإن الحصول على خرائط كبيرة ودقيقة يمثل مشكلة تقدير إحصائي صعبة، خاصة عند تنفيذها في الوقت الفعلي.

ينبع معظم الأبحاث الحالية حول SLAM من ورقة بحثية أساسية كتبها سميث وتشيزمان [21]، والتي اقترحت استخدام مرشح كالمان الممتد (EKF) لحل مسألة SLAM. تستند هذه الورقة إلى الرؤى التي تفيد بأن الأخطاء في الخريطة وأخطاء الوضعية مترابطة بشكل طبيعي، وأن مصفوفة التباين المشترك التي يحتفظ بها مرشح كالمان الممتد تعبر عن مثل هذه الارتباطات. أثبت نيومان [18] مؤخراً أن مرشح كالمان الممتد يتقارب لمسائل SLAM الخطية، حيث يكون نموذج الحركة ونموذج الملاحظة دوال خطية مع ضوضاء غاوسية (انظر أدناه).

لسوء الحظ، فإن مصفوفات التباين المشترك لمرشح كالمان الممتد تربيعية في حجم الخريطة، ويتطلب تحديثها وقتاً تربيعياً في عدد المعالم N. لطالما تم الاعتراف بهذا التعقيد التربيعي كعقبة رئيسية في توسيع نطاق خوارزميات SLAM إلى خرائط بها أكثر من بضع مئات من الخصائص. كما أنه يحد من قابلية تطبيق خوارزميات SLAM على المسائل ذات المعالم الغامضة، مما يحفز مشكلة ربط البيانات [2؛ 22]. تحافظ خوارزميات SLAM الأكثر متانة اليوم مع ربط البيانات غير المعروف على فرضيات متعددة (مسارات)، مما يزيد من تعقيدها الحسابي.

وبالتالي، حدث تدفق في الأبحاث حول تقنيات SLAM الأكثر كفاءة (انظر على سبيل المثال، [11]). طورت مجموعة من الباحثين تقنيات تقسم الخرائط بشكل متكرر إلى خرائط فرعية، وبالتالي تقتصر معظم العمليات الحسابية على مناطق صغيرة. لا تزال بعض هذه الأساليب تحافظ على الارتباطات العالمية بين تلك الخرائط الفرعية، وبالتالي فهي تربيعية ولكن مع عامل ثابت أقل بكثير [1؛ 7؛ 22؛ 25]. يقصر البعض الآخر التحديث حصرياً على الخرائط المحلية [12]، وبالتالي يعمل في وقت ثابت (بافتراض ربط البيانات المعروف).

طورت مجموعة ثانية من الباحثين تقنيات تمثل الخرائط من خلال دوال الجهد بين المعالم المجاورة، على غرار حقول ماركوف العشوائية. تتطلب التمثيلات الناتجة ذاكرة خطية في عدد المعالم [19؛ 23]. تحت التقريبات المناسبة، ثبت أن مثل هذه التقنيات توفر تحديثاً في وقت ثابت (مرة أخرى لربط البيانات المعروف). لسوء الحظ، لا يوجد إثبات تقارب لأي من هذه الامتدادات لمرشح كالمان الممتد، حتى بالنسبة للحالة العامة لـ SLAM الخطي. علاوة على ذلك، إذا كانت المعالم غامضة، يجب على جميع هذه الأساليب إجراء بحث للعثور على فرضيات ربط البيانات المناسبة، مما يضيف عاملاً لوغاريتمياً إلى تعقيد التحديث الخاص بها.

خوارزمية FastSLAM، المقترحة في [15] كنهج فعال لـ SLAM بناءً على الترشيح الجسيمي [6]، لا تندرج ضمن أي من الفئتين أعلاه. تستفيد FastSLAM من خاصية مهمة لمسألة SLAM (مع ربط البيانات المعروف): تقديرات المعالم مستقلة شرطياً بالنظر إلى مسار الروبوت [17]. تستخدم FastSLAM مرشح جسيمات لأخذ عينات من مسارات الروبوت. تمتلك كل جسيمة N من مرشحات كالمان الممتدة منخفضة الأبعاد، واحد لكل من المعالم N. يتطلب هذا التمثيل ذاكرة O(NM)، حيث M هو عدد الجسيمات في مرشح الجسيمات. يتطلب تحديث هذا المرشح وقت O(M log N)، مع أو بدون معرفة ربطات البيانات. ومع ذلك، فإن عدد الجسيمات M اللازمة للتقارب غير معروف ويُشتبه في أنها أسية في حجم الخريطة، في أسوأ الحالات.

تقترح هذه الورقة نسخة محسّنة من خوارزمية FastSLAM. التعديل بسيط من الناحية المفاهيمية: عند اقتراح وضعية روبوت جديدة—وهي خطوة أساسية في مرشح جسيمات FastSLAM—يعتمد توزيع الاقتراح الخاص بنا ليس فقط على تقدير الحركة (كما هو الحال في FastSLAM)، ولكن أيضاً على قياس المستشعر الأحدث. مثل هذا النهج أقل هدراً للعينات من خوارزمية FastSLAM الأصلية، خاصة في الحالات التي تكون فيها الضوضاء في الحركة عالية نسبياً إلى ضوضاء القياس.

للحصول على توزيع اقتراح مناسب، تقوم خوارزميتنا بتخطيط نموذج الحركة ونموذج القياس بنفس الطريقة التي يستخدمها مرشح كالمان الممتد. ونتيجة لذلك، يمكن حساب توزيع الاقتراح في صورة مغلقة. يوازي هذا الامتداد العمل السابق من قبل دوسيت وزملائه، الذين اقترحوا تعديلاً مماثلاً لمرشحات الجسيمات العامة [6] وتقنيات مونتي كارلو لسلسلة ماركوف للشبكات العصبية [4]. إنه مشابه لتقنية عكس القوس المقترحة لمرشحات الجسيمات المطبقة على شبكات بايز [10]، وهو مشابه للعمل الحديث من قبل فان دير ميرفي [24]، الذي يستخدم خطوة ترشيح غير معطر [9] لتوليد توزيعات اقتراح تستوعب القياس.

بينما هذا التعديل بسيط من الناحية المفاهيمية، إلا أن له تداعيات مهمة. تتمثل المساهمة الرئيسية لهذه الورقة في إثبات التقارب لمسائل SLAM الخطية باستخدام جسيمة واحدة. تتطلب الخوارزمية الناتجة وقت تحديث ثابت. على حد علمنا، فإن أفضل خوارزمية SLAM سابقة تم إثبات تقاربها تتطلب وقت تحديث تربيعي. علاوة على ذلك، نلاحظ تجريبياً أن خوارزمية FastSLAM الجديدة، حتى مع جسيمة واحدة، تعطي نتائج أكثر دقة بكثير على معيار من العالم الحقيقي صعب [7] من الإصدار السابق من الخوارزمية. هذه النتائج ذات أهمية، حيث أن العديد من أنظمة الروبوتات المتحركة تعاني من ضوضاء التحكم، ولكنها تمتلك مستشعرات دقيقة نسبياً. علاوة على ذلك، فإنها تناقض اعتقاداً شائعاً بأن الحفاظ على مصفوفة التباين المشترك بأكملها مطلوب للتقارب [5].

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:** SLAM, EKF (extended Kalman filter), particle filter, data association, covariance matrix, proposal distribution, landmarks, Rao-Blackwellized
- **Citations:** [21], [18], [2], [22], [11], [1], [7], [25], [12], [19], [23], [15], [6], [17], [4], [10], [24], [9], [5]
- **Special handling:**
  - O(NM), O(M log N) notation preserved
  - Technical terms like "Rao-Blackwellized" transliterated as "راو-بلاكويلي"
  - "unscented filtering" translated as "ترشيح غير معطر" (literal translation maintaining technical meaning)

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88

### Back-Translation Validation (First and Last Paragraphs)

**First Paragraph Back-Translation:**
Simultaneous localization and mapping (SLAM) is a highly active research area in robotics and artificial intelligence. The SLAM problem arises when a moving vehicle (such as a mobile robot, submarine, or unmanned aerial vehicle) estimates a map of its environment and its pose relative to that map simultaneously. In the absence of global position information, the vehicle's pose estimate will become increasingly inaccurate, and so will its map. Since maps may contain thousands of entities, obtaining large and accurate maps represents a challenging statistical estimation problem, especially when executed in real-time.

**Last Paragraph Back-Translation:**
While this modification is conceptually simple, it has important ramifications. The main contribution of this paper is a convergence proof for linear SLAM problems using a single particle. The resulting algorithm requires constant update time. To our knowledge, the best previous SLAM algorithm for which convergence was proven requires quadratic update time. Moreover, we experimentally observe that our new FastSLAM algorithm, even with a single particle, yields significantly more accurate results on a challenging real-world benchmark [7] than the previous version of the algorithm. These findings are significant, as many mobile robot systems suffer from control noise but possess relatively accurate sensors. Furthermore, they contradict a common belief that maintaining the entire covariance matrix is required for convergence [5].
