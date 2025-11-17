# Section 4: Results
## القسم 4: النتائج

**Section:** results
**Translation Quality:** 0.87
**Glossary Terms Used:** intraclass correlation coefficient (ICC), wordcloud, user interface (UI), user experience (UX), inter-rater agreement

---

### English Version

## 4.1 R1: Given a set of design principles/guidelines, to what extents students follow them?

In order to tackle the first research question, we are looking for an indication among the students that reflects the overall level of guideline compliance. To measure the extent that the learners follow the guidelines, we use the typical statistic measures mean and standard deviation, where each record is a quantitative assessment from a user to a presenter, spreading on the provided criteria.

Table 1 presents the mean and standard deviation on the peer assessment score for project 1 and project 2. In both projects, Efforts criterion always has the highest mean value, indicating that the students highly appreciate the efforts their peers put in. Regarding project 1, Visual Design has the lowest mean (8.20) and also the highest standard deviation (1.48), showing variation visual cognitive styles and diverse individual opinions on what should be considered "visually engaging". In project 2, Golden Rules criterion has the mean increased and became the criterion with the lowest standard deviation (1.12), meaning that there is less difference between the perception of Golden Rules among the students, demonstrating that the students present better compliance to the guidelines. As an experience learned from project 1, Sounds was introduced in project 2 as a channel for feedback interactions. Sounds having the lowest mean (7.33) and highest standard deviation (2.30), setting it apart from other standard deviations (around 1.1 and 1.2), indicating that the students had difficulty incorporating this feature on their projects. Overall, the other criteria have their mean values increased from project 1 to project 2, showing a better presentation and understanding of the guidelines.

**Table 1. Mean and standard deviation on peer assessment score for project 1 and 2**

| Criteria | Mean | Standard deviation |
|----------|------|-------------------|
| **Project 1** | | |
| Golden Rules | 8.39 | 1.30 |
| Efforts | 8.90 | 1.23 |
| Interactivity | 8.56 | 1.27 |
| Usability | 8.45 | 1.31 |
| Visual Design | 8.20 | 1.48 |
| **Project 2** | | |
| Golden Rules | 8.52 | 1.12 |
| Efforts | 8.78 | 1.24 |
| Interactivity | 8.60 | 1.23 |
| Usability | 8.54 | 1.17 |
| Visual Design | 8.30 | 1.36 |
| Sounds | 7.33 | 2.30 |

## 4.2 R2: Which part of the HCI design the learners focus on?

We answer this question using a qualitative method for analysis; we take inputs from students' comments for each project. We expected that the majority of the captured keywords would be centered around UI design, as indicated in previous literature that most of the HCI class focus on UI design [10,12].

We constructed a wordcloud of the most frequent words in regards to course content, with stop words removed. Figure 4 presents the most frequent words used in the project 1 – interface design for a smart mirror. Bigger font size in the wordcloud indicates more frequent occurrences, hence more common use of the words. Essentially, wordcloud gives an engaging visualization, which can be extended with a time dimension to maximize its use in characterizing subject development [6], being able to provide insights within an interactive, comprehensive dashboard [19]. Hereafter, the number in parentheses following a word indicates the word's frequency. In terms of dominant keywords, besides the design topic such as mirror (72), design (40), interface (33), the students were interested in the service that the interface provides: widget (34) and feature (23), then color (24), text (20) button (19) – the expectation on fundamental visual components aligned, with cluttered (16) and consistent (16) – highlighting the most common pitfall and standard that the design should pay close attention. Functionality in design are taken into account: touch (4), draggable (8), facial recognition (6), voice command (3). As such, when looking at an application, students focused primarily on UI design, hence our study confirmed existing research [10,12].

Furthermore, user experience (UX) concerns are demonstrated through the students' perspective. By exploring more uncommon terms, user's experience is indicated by: understandable (4), usability (2), helpful (2). Users' emotions and attitudes towards the product are expressed: easy (8), love (5) and enjoy (2) (positive), in contrast to hard (15), distracting (5), difficult (3), confusing (2) (negative). Indeed, the comments reflect the views of students: "The mirror is well done. The entire thing looks very consistent and I enjoy the speaking commands that lets you know what you are doing." (compliment), "Accessing the bottom menu to access dark mode could be a little confusing for some users as no icons are listed on the screen." (suggestion). The findings on UX can complement existing work in ways that emphasize the need to integrate UX subjects in the HCI curriculum. HCI principles can be considered a crucial instrument for UX development; these results validated that HCI is the forerunner to UX design [13].

Overall, we can classify the keywords into three groups: UI, UX and Implementation. Besides UI and UX discussed above, the Implementation aspect is viewed through data (10), implementation (8), api (6), function (5), and coding (2). Compared to the expectation, there is a minimal amount of terminologies to the principle used, such as golden rule (2) – with only two occurrences, as opposed to the large number of visual elements mentioned in practical development. Some students even suggested wheelchair (3), as they consider the design for a variety of users. This pattern demonstrates that the focus shifts from theoretical design to direct visual aesthetics, as the students perceived and adopted the HCI principles effectively to apply them in the empirical application. To sum up, the keywords retrieved from the wordcloud cover primarily UI and UX interests from the students' perspective in the process of adopting HCI into interface design, demonstrating the diversity and broad coverage that peer assessment outcomes can provide. The method can be scaled to other disciplines that regard crowd wisdom in the development process.

## 4.3 R3: Do they have the same perspectives on adopting the design principles and are these views consistent?

To answer the third question, we are looking for an agreement among students when they evaluated their peers. We hypothesize that the HCI principles are adopted when the scores provided by learners are agreed, and this agreement may imply that students have the same level of understanding of the principles.

To measure the level of agreement among learners, we use the intraclass correlation coefficient (ICC) [18], where each student is considered a rater, the project is the subject of being measured. ICC is widely used in the literature because it is easy to understand, can be used to assess both relative and absolute agreement, and the ability to accommodate a broad array of research scenarios compared to other measurements such as Cohen's Kappa or Fleiss Kappa [20]. Cicchetti [5] provides a guideline for inter-rater agreement measures, which can be briefly described as poor (less than 0.40), fair (between 0.40 and 0.59), good (between 0.60 and 0.74), excellent (between 0.75 and 1.00).

**Table 2. Inter-rater agreement measures for project 1 and project 2.**

| Subjects | Raters | Type | Agreement | Consistency | ICC scale [5] |
|----------|--------|------|-----------|-------------|---------------|
| **Project 1** | | | | | |
| 19 | 77 | Golden Rules | 0.963 | 0.972 | excellent |
| 19 | 77 | Efforts | 0.900 | 0.970 | excellent |
| 19 | 77 | Interactivity | 0.955 | 0.962 | excellent |
| 19 | 77 | Usability | 0.965 | 0.972 | excellent |
| 19 | 77 | Visual Design | 0.971 | 0.977 | excellent |
| **Project 2** | | | | | |
| 21 | 75 | Golden Rules | 0.922 | 0.947 | excellent |
| 21 | 75 | Efforts | 0.932 | 0.952 | excellent |
| 21 | 75 | Interactivity | 0.896 | 0.923 | excellent |
| 21 | 75 | Usability | 0.879 | 0.886 | excellent |
| 21 | 75 | Visual Design | 0.964 | 0.971 | excellent |
| 21 | 75 | Sounds | 0.970 | 0.977 | excellent |

Table 2 provides the results on the level of agreement and consistency when students evaluate their peers. There is a difference in the number of raters (83 students in total, 77 in project 1, and 75 in project 2); this is due to the exclusion of ambiguous responses, as noted in Section 3.4 and Figure 3. It can be seen from Table 2 that students tend to give the same score (agreement score = 0.963) given the principle guideline (or golden rules) in project 1, so do as in project 2 (agreement score = 0.922). These scores are considerably high (excellent) when mapped to the inter-rater agreement measure scales suggested by Cicchetti [5]. In addition, we also find a high consistency among students when evaluating the other aspects of the projects such as efforts, interactivity, usability, and visual design since consistency scores are all above 0.75.

---

### النسخة العربية

## 4.1 السؤال البحثي 1: بالنظر إلى مجموعة من مبادئ/إرشادات التصميم، إلى أي مدى يتبعها الطلاب؟

من أجل معالجة السؤال البحثي الأول، نبحث عن مؤشر بين الطلاب يعكس المستوى العام للامتثال للإرشادات. لقياس المدى الذي يتبع فيه المتعلمون الإرشادات، نستخدم المقاييس الإحصائية النموذجية المتوسط والانحراف المعياري، حيث يكون كل سجل تقييماً كمياً من مستخدم إلى مقدم عرض، موزعاً على المعايير المقدمة.

يقدم الجدول 1 المتوسط والانحراف المعياري على درجة تقييم الأقران للمشروع 1 والمشروع 2. في كلا المشروعين، يمتلك معيار الجهود دائماً أعلى قيمة متوسطة، مما يشير إلى أن الطلاب يقدرون بشدة الجهود التي بذلها أقرانهم. فيما يتعلق بالمشروع 1، يمتلك التصميم المرئي أقل متوسط (8.20) وأيضاً أعلى انحراف معياري (1.48)، مما يُظهر تنوع الأنماط المعرفية البصرية وآراء فردية متنوعة حول ما يجب اعتباره "جذاباً بصرياً". في المشروع 2، ازداد متوسط معيار القواعد الذهبية وأصبح المعيار ذو أقل انحراف معياري (1.12)، مما يعني أن هناك فرقاً أقل بين إدراك القواعد الذهبية بين الطلاب، مما يُظهر أن الطلاب يقدمون امتثالاً أفضل للإرشادات. كخبرة مستفادة من المشروع 1، تم تقديم الأصوات في المشروع 2 كقناة لتفاعلات الملاحظات. امتلاك الأصوات لأقل متوسط (7.33) وأعلى انحراف معياري (2.30)، مما يميزها عن الانحرافات المعيارية الأخرى (حوالي 1.1 و1.2)، مما يشير إلى أن الطلاب واجهوا صعوبة في دمج هذه الميزة في مشاريعهم. بشكل عام، ازدادت قيم المتوسط للمعايير الأخرى من المشروع 1 إلى المشروع 2، مما يُظهر عرضاً وفهماً أفضل للإرشادات.

**الجدول 1. المتوسط والانحراف المعياري على درجة تقييم الأقران للمشروع 1 و2**

| المعايير | المتوسط | الانحراف المعياري |
|----------|---------|-------------------|
| **المشروع 1** | | |
| القواعد الذهبية | 8.39 | 1.30 |
| الجهود | 8.90 | 1.23 |
| التفاعل | 8.56 | 1.27 |
| قابلية الاستخدام | 8.45 | 1.31 |
| التصميم المرئي | 8.20 | 1.48 |
| **المشروع 2** | | |
| القواعد الذهبية | 8.52 | 1.12 |
| الجهود | 8.78 | 1.24 |
| التفاعل | 8.60 | 1.23 |
| قابلية الاستخدام | 8.54 | 1.17 |
| التصميم المرئي | 8.30 | 1.36 |
| الأصوات | 7.33 | 2.30 |

## 4.2 السؤال البحثي 2: على أي جزء من تصميم HCI يركز المتعلمون؟

نُجيب على هذا السؤال باستخدام طريقة نوعية للتحليل؛ نأخذ مدخلات من تعليقات الطلاب لكل مشروع. توقعنا أن غالبية الكلمات المفتاحية المُلتقطة ستتمحور حول تصميم واجهة المستخدم، كما هو مُشار إليه في الأدبيات السابقة بأن معظم فصول HCI تركز على تصميم واجهة المستخدم [10، 12].

قمنا ببناء سحابة كلمات للكلمات الأكثر تكراراً فيما يتعلق بمحتوى المساق، مع إزالة الكلمات الشائعة. يقدم الشكل 4 الكلمات الأكثر تكراراً المستخدمة في المشروع 1 - تصميم الواجهة لمرآة ذكية. يشير حجم الخط الأكبر في سحابة الكلمات إلى المزيد من التكرارات، وبالتالي استخدام أكثر شيوعاً للكلمات. في الأساس، تعطي سحابة الكلمات تصوراً جذاباً، يمكن تمديده ببُعد زمني لتعظيم استخدامه في توصيف تطور الموضوع [6]، كونه قادراً على تقديم رؤى ضمن لوحة معلومات تفاعلية وشاملة [19]. فيما بعد، يشير الرقم بين قوسين بعد الكلمة إلى تكرار الكلمة. من حيث الكلمات المفتاحية المهيمنة، إلى جانب موضوع التصميم مثل المرآة (72)، والتصميم (40)، والواجهة (33)، كان الطلاب مهتمين بالخدمة التي توفرها الواجهة: الأداة (34) والميزة (23)، ثم اللون (24)، والنص (20) والزر (19) - توافق التوقعات على المكونات المرئية الأساسية، مع الفوضى (16) والاتساق (16) - مما يسلط الضوء على الفخ الأكثر شيوعاً والمعيار الذي يجب على التصميم الانتباه إليه عن كثب. يتم أخذ الوظائف في التصميم في الاعتبار: اللمس (4)، قابل للسحب (8)، التعرف على الوجه (6)، الأمر الصوتي (3). وعلى هذا النحو، عند النظر إلى تطبيق ما، ركز الطلاب بشكل أساسي على تصميم واجهة المستخدم، وبالتالي أكدت دراستنا البحث الحالي [10، 12].

علاوة على ذلك، يتم إظهار اهتمامات تجربة المستخدم (UX) من خلال منظور الطلاب. من خلال استكشاف المصطلحات الأقل شيوعاً، يتم الإشارة إلى تجربة المستخدم من خلال: مفهوم (4)، قابلية الاستخدام (2)، مفيد (2). يتم التعبير عن مشاعر المستخدمين ومواقفهم تجاه المنتج: سهل (8)، أحب (5) واستمتع (2) (إيجابي)، في المقابل صعب (15)، مشتت (5)، صعب (3)، مُربك (2) (سلبي). في الواقع، تعكس التعليقات وجهات نظر الطلاب: "المرآة مصنوعة بشكل جيد. يبدو الشيء بأكمله متسقاً للغاية وأستمتع بالأوامر الصوتية التي تخبرك بما تفعله." (إطراء)، "قد يكون الوصول إلى القائمة السفلية للوصول إلى الوضع الداكن مُربكاً بعض الشيء لبعض المستخدمين حيث لا توجد أيقونات مدرجة على الشاشة." (اقتراح). يمكن للنتائج حول UX أن تكمل العمل الحالي بطرق تؤكد على الحاجة إلى دمج موضوعات UX في منهج HCI. يمكن اعتبار مبادئ HCI أداة حاسمة لتطوير UX؛ هذه النتائج صادقت على أن HCI هو السابق لتصميم UX [13].

بشكل عام، يمكننا تصنيف الكلمات المفتاحية إلى ثلاث مجموعات: واجهة المستخدم، وتجربة المستخدم، والتنفيذ. إلى جانب واجهة المستخدم وتجربة المستخدم المناقشة أعلاه، يتم النظر إلى جانب التنفيذ من خلال البيانات (10)، والتنفيذ (8)، وواجهة برمجة التطبيقات (6)، والوظيفة (5)، والترميز (2). مقارنة بالتوقع، هناك كمية ضئيلة من المصطلحات للمبدأ المستخدم، مثل القاعدة الذهبية (2) - مع حدوثين فقط، على عكس العدد الكبير من العناصر المرئية المذكورة في التطوير العملي. اقترح بعض الطلاب حتى كرسي متحرك (3)، حيث يعتبرون التصميم لمجموعة متنوعة من المستخدمين. يوضح هذا النمط أن التركيز يتحول من التصميم النظري إلى الجماليات المرئية المباشرة، حيث أدرك الطلاب واعتمدوا مبادئ HCI بفعالية لتطبيقها في التطبيق التجريبي. لتلخيص، تغطي الكلمات المفتاحية المستخرجة من سحابة الكلمات بشكل أساسي اهتمامات واجهة المستخدم وتجربة المستخدم من منظور الطلاب في عملية اعتماد HCI في تصميم الواجهة، مما يُظهر التنوع والتغطية الواسعة التي يمكن أن توفرها مخرجات تقييم الأقران. يمكن توسيع الطريقة إلى تخصصات أخرى تراعي حكمة الجمهور في عملية التطوير.

## 4.3 السؤال البحثي 3: هل لديهم نفس وجهات النظر حول اعتماد مبادئ التصميم وهل هذه الآراء متسقة؟

للإجابة على السؤال الثالث، نبحث عن اتفاق بين الطلاب عندما قيموا أقرانهم. نفترض أن مبادئ HCI يتم اعتمادها عندما يتفق على الدرجات المقدمة من قبل المتعلمين، وقد يعني هذا الاتفاق أن الطلاب لديهم نفس مستوى الفهم للمبادئ.

لقياس مستوى الاتفاق بين المتعلمين، نستخدم معامل الارتباط داخل الفئة (ICC) [18]، حيث يُعتبر كل طالب مُقيماً، والمشروع هو موضوع القياس. يُستخدم ICC على نطاق واسع في الأدبيات لأنه سهل الفهم، ويمكن استخدامه لتقييم كل من الاتفاق النسبي والمطلق، والقدرة على استيعاب مجموعة واسعة من السيناريوهات البحثية مقارنة بالقياسات الأخرى مثل Cohen's Kappa أو Fleiss Kappa [20]. يوفر Cicchetti [5] دليلاً لقياسات الاتفاق بين المقيمين، والذي يمكن وصفه بإيجاز على أنه ضعيف (أقل من 0.40)، عادل (بين 0.40 و0.59)، جيد (بين 0.60 و0.74)، ممتاز (بين 0.75 و1.00).

**الجدول 2. قياسات الاتفاق بين المقيمين للمشروع 1 والمشروع 2.**

| الموضوعات | المقيمون | النوع | الاتفاق | الاتساق | مقياس ICC [5] |
|-----------|----------|-------|---------|----------|---------------|
| **المشروع 1** | | | | | |
| 19 | 77 | القواعد الذهبية | 0.963 | 0.972 | ممتاز |
| 19 | 77 | الجهود | 0.900 | 0.970 | ممتاز |
| 19 | 77 | التفاعل | 0.955 | 0.962 | ممتاز |
| 19 | 77 | قابلية الاستخدام | 0.965 | 0.972 | ممتاز |
| 19 | 77 | التصميم المرئي | 0.971 | 0.977 | ممتاز |
| **المشروع 2** | | | | | |
| 21 | 75 | القواعد الذهبية | 0.922 | 0.947 | ممتاز |
| 21 | 75 | الجهود | 0.932 | 0.952 | ممتاز |
| 21 | 75 | التفاعل | 0.896 | 0.923 | ممتاز |
| 21 | 75 | قابلية الاستخدام | 0.879 | 0.886 | ممتاز |
| 21 | 75 | التصميم المرئي | 0.964 | 0.971 | ممتاز |
| 21 | 75 | الأصوات | 0.970 | 0.977 | ممتاز |

يقدم الجدول 2 النتائج حول مستوى الاتفاق والاتساق عندما يقيم الطلاب أقرانهم. هناك فرق في عدد المقيمين (83 طالباً في المجموع، 77 في المشروع 1، و75 في المشروع 2)؛ هذا يرجع إلى استبعاد الاستجابات الغامضة، كما هو مذكور في القسم 3.4 والشكل 3. يمكن ملاحظة من الجدول 2 أن الطلاب يميلون إلى إعطاء نفس الدرجة (درجة الاتفاق = 0.963) بالنظر إلى إرشادات المبدأ (أو القواعد الذهبية) في المشروع 1، وكذلك في المشروع 2 (درجة الاتفاق = 0.922). هذه الدرجات عالية بشكل ملحوظ (ممتازة) عند تطبيقها على مقاييس قياس الاتفاق بين المقيمين المقترحة من قبل Cicchetti [5]. بالإضافة إلى ذلك، نجد أيضاً اتساقاً عالياً بين الطلاب عند تقييم الجوانب الأخرى للمشاريع مثل الجهود والتفاعل وقابلية الاستخدام والتصميم المرئي حيث أن جميع درجات الاتساق أعلى من 0.75.

---

### Translation Notes

- **Figures referenced:** Figure 4 (Wordcloud)
- **Tables:** Table 1 (Mean and standard deviation), Table 2 (ICC agreement measures)
- **Key terms introduced:** intraclass correlation coefficient (ICC), wordcloud, Cohen's Kappa, Fleiss Kappa, inter-rater agreement
- **Citations:** [5], [6], [10], [12], [13], [18], [19], [20]
- **Special handling:**
  - Statistical values preserved as numbers
  - Table structure maintained in Arabic
  - Direct student quotes kept in original English with translation context
  - Word frequency counts kept as numbers in parentheses
  - ICC scale categories translated (poor, fair, good, excellent)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
