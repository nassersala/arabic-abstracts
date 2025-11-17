# Section 3: Materials and Methods
## القسم 3: المواد والطرق

**Section:** materials-methods
**Translation Quality:** 0.86
**Glossary Terms Used:** studio-based learning, project-based learning, peer assessment, Likert scale, Virtual Reality (VR), Augmented Reality (AR)

---

### English Version

## 3.1 Teaching method and activities

The main goal of our study is to investigate the adoption of HCI design principles in the classroom setting from the learners' perspective. It is a daunting task for instructors to justify the adoption level due to variations in visual cognitive styles. For example, teachers may like bright and high contrast design, whereas students prefer a colorful dashboard. Thus, a teaching method and assessment should be carefully designed to help motivate and engage students and adequately reflect their performance level. Literature work has proposed several teaching methods [3], such as inquiry-based learning, situated-based learning, project-based learning, and studio-based learning. As such, we chose the studio-based learning approach due to its characteristics, encompassed our critical factors. These characteristics can be laid out as follows:

- Students should be engaged in project-based assignments (C1).
- Student learning outcomes should be iteratively assessed in formal and informal fashion through design critiques (C2).
- Students are required to engage in critiquing the work of their peers (C3).
- Design critiques should revolve around the artifacts typically created by the domains (C4).

Based on the above criteria, we divided the entire course work into four main activities spanning over 16-week long, including 1) Introduction to HCI, 2) Homework assignment, 3) Projects engagement: Throughout the course, students were actively involved in two projects (characteristic C1), and 4) Evaluation and design critiques: In each assignment/projects both instructors and students were engaged for evaluations (characteristics C2, C4), this process not only helps to avoid bias in the results but also allows learners to reflect their learning for justifying their peers (characteristic C3). The assignment's purpose is to give students some practice in the design of everyday things. In the first project, we incorporated the problem-based learning method on the problem extended from the assignment. The second project had a different approach by adapting the computational thinking-based method, where students can explore a real-life problem and then solve it on their own.

## 3.2 Participants

The present study was conducted with university students enrolled in the Human-Computer Interaction course in computer science. There was a total of 83 students, of which 62 students are undergraduate, 13 masters, and eight doctoral students. There were 64 males and 19 females.

## 3.3 Assessment tool

Aalberg and Lors [1] indicated that 'the lack of technology support for peer assessment is one likely cause for the lack of systematic use in education.' To address these issues, many assessment tools have been introduced [8,9,21]. However, no such a comprehensive tool enables instructors to carry out a new task that has not been presented. Particularly, in our study, the evaluation requires features such as instant feedback, timing control, list preview, or even 3D objects embedded applications. We developed a standalone tool to facilitate peer evaluation and data collection, supporting multiple application types, including webpage, web-based VR, and AR. The tool is expected to serve these goals:

- G1 From the presenter's perspective: Each presenter (group or individual) demonstrates their interface design within their session. The presenter can see the feedback and evaluation visualization within their session.
- G2 From the audience's perspective: The audience can give comments and evaluations for the current design presented [9]. Authentication for the in-class audience is necessary for input validity.
- G3 The system presents online, instant evaluation from the audience (anonymously) to the presenter without interrupting the presentation.

**User Interface** Figure 1 describes our web presentation system according to three perspectives. Panel A shows the presenter list (student names and group members' images have been customized for demonstration purposes). This view allows the instructors to manage students' turn to present, each group has two thumbnail images for sketch and final design, indicating the development process. Panel B is the presenter's view with live comments on the right-hand side, updated on-the-fly. The average scores and evaluation are updated live in the presenter's view – visualized in an interactive, dynamic chart. Panel C is the audience's view for providing scores and feedback on the presenting project.

Each presentation is given a bounded time window for demonstration and discussion. The system automatically switches to the next presentation when the current session is over, renewing both Panel B and C interfaces. During the presentation, the clock timer in the two panels are synchronized, and the assessment and comments submitted from Panel C are updated live on Panel B. Questions for peer assessment consist of seven 10-point Likert scale questions (which ranged from "strongly disagree(1)" to "strongly agree(10)") and one open-ended question. The criteria for scoring are as follows.

- Q1, Does the interface follow the Golden rules and principle in design [22]?
- Q2, Usability: The ease of use of the interface [24].
- Q3, Visual appealing: Is the design visually engaging for the users [23]?
- Q4, Interactivity: To what extent does the interface provide user interactions [23]?
- Q5, Soundness: The quality and proper use of the audio from the application [23].
- Q6, Efforts: Does the group provide enough effort for the work?
- Q7, Teamwork: Is the work equally distributed to team members?

## 3.4 Assignment and Project outputs

There were a total of 126 visual interaction designs as assignment and project outcomes, including 82 sketches from the assignment, 21 problem-based designs, and 22 computational thinking based solutions. Figure 2 presents some selected work corresponding to the assignment, project 1, project 2, respectively.

Previous work showed that there was some ambiguity in the results when students gave scores to their peers. Part of the issue is that they wanted to be 'nice' or aimed to get the job done. To alleviate these issues, unusual score patterns will be excluded, and evaluators (students) will be notified anonymously through their alias names. Examples of good grading and inadequate grading are presented in Figure 3. Good grading is illustrated via the diversity in assessment outcome among different criteria, opposite to inadequate examples.

---

### النسخة العربية

## 3.1 طريقة التدريس والأنشطة

الهدف الرئيسي من دراستنا هو التحقيق في اعتماد مبادئ تصميم HCI في بيئة الفصل الدراسي من منظور المتعلمين. إنها مهمة شاقة للمدرسين لتبرير مستوى الاعتماد بسبب الاختلافات في الأنماط المعرفية البصرية. على سبيل المثال، قد يفضل المعلمون التصميم الساطع والعالي التباين، بينما يفضل الطلاب لوحة معلومات ملونة. وبالتالي، يجب تصميم طريقة التدريس والتقييم بعناية للمساعدة في تحفيز ومشاركة الطلاب وعكس مستوى أدائهم بشكل كافٍ. اقترحت الأعمال الأدبية عدة طرق تدريس [3]، مثل التعلم القائم على الاستقصاء، والتعلم القائم على المواقف، والتعلم القائم على المشاريع، والتعلم القائم على الاستوديو. على هذا النحو، اخترنا نهج التعلم القائم على الاستوديو بسبب خصائصه التي تشمل عواملنا الحرجة. يمكن تحديد هذه الخصائص على النحو التالي:

- يجب أن ينخرط الطلاب في مهام قائمة على المشاريع (C1).
- يجب تقييم مخرجات تعلم الطلاب بشكل تكراري بطريقة رسمية وغير رسمية من خلال نقد التصميم (C2).
- يُطلب من الطلاب الانخراط في نقد أعمال أقرانهم (C3).
- يجب أن يدور نقد التصميم حول المنتجات التي يتم إنشاؤها عادةً في المجالات (C4).

بناءً على المعايير أعلاه، قسمنا العمل الكامل للمساق إلى أربعة أنشطة رئيسية تمتد على مدى 16 أسبوعاً، بما في ذلك 1) مقدمة إلى HCI، 2) واجب منزلي، 3) الانخراط في المشاريع: طوال المساق، شارك الطلاب بنشاط في مشروعين (الخاصية C1)، و4) التقييم ونقد التصميم: في كل مهمة/مشروع، انخرط كل من المدرسين والطلاب في التقييمات (الخصائص C2، C4)، هذه العملية لا تساعد فقط على تجنب التحيز في النتائج ولكن أيضاً تسمح للمتعلمين بالتفكير في تعلمهم لتبرير أقرانهم (الخاصية C3). الغرض من المهمة هو إعطاء الطلاب بعض الممارسة في تصميم الأشياء اليومية. في المشروع الأول، أدمجنا طريقة التعلم القائم على المشاكل على المشكلة الممتدة من المهمة. كان للمشروع الثاني نهج مختلف من خلال تكييف طريقة قائمة على التفكير الحاسوبي، حيث يمكن للطلاب استكشاف مشكلة من الحياة الواقعية ثم حلها بأنفسهم.

## 3.2 المشاركون

تم إجراء الدراسة الحالية مع طلاب الجامعة المسجلين في مساق التفاعل بين الإنسان والحاسوب في علوم الحاسوب. كان هناك إجمالي 83 طالباً، منهم 62 طالباً جامعياً، و13 من طلاب الماجستير، وثمانية طلاب دكتوراه. كان هناك 64 ذكراً و19 أنثى.

## 3.3 أداة التقييم

أشار Aalberg و Lors [1] إلى أن "عدم وجود دعم تقني لتقييم الأقران هو أحد الأسباب المحتملة لعدم الاستخدام المنهجي في التعليم". لمعالجة هذه المشاكل، تم تقديم العديد من أدوات التقييم [8، 9، 21]. ومع ذلك، لا توجد أداة شاملة تمكن المدرسين من تنفيذ مهمة جديدة لم يتم تقديمها. على وجه الخصوص، في دراستنا، يتطلب التقييم ميزات مثل الملاحظات الفورية، والتحكم في التوقيت، ومعاينة القائمة، أو حتى تطبيقات الكائنات ثلاثية الأبعاد المضمنة. قمنا بتطوير أداة مستقلة لتسهيل تقييم الأقران وجمع البيانات، تدعم أنواعاً متعددة من التطبيقات، بما في ذلك صفحة الويب، و VR القائم على الويب، و AR. من المتوقع أن تخدم الأداة هذه الأهداف:

- G1 من منظور مقدم العرض: يُظهر كل مقدم عرض (مجموعة أو فرد) تصميم واجهته ضمن جلسته. يمكن لمقدم العرض رؤية الملاحظات وتصور التقييم ضمن جلسته.
- G2 من منظور الجمهور: يمكن للجمهور تقديم تعليقات وتقييمات للتصميم الحالي المقدم [9]. المصادقة للجمهور داخل الفصل ضرورية لصحة المدخلات.
- G3 يقدم النظام تقييماً فورياً عبر الإنترنت من الجمهور (بشكل مجهول) إلى مقدم العرض دون مقاطعة العرض.

**واجهة المستخدم** يصف الشكل 1 نظام العرض التقديمي عبر الويب الخاص بنا وفقاً لثلاث وجهات نظر. تُظهر اللوحة A قائمة مقدمي العروض (تم تخصيص أسماء الطلاب وصور أعضاء المجموعة لأغراض العرض التوضيحي). تسمح هذه المشاهدة للمدرسين بإدارة دور الطلاب للتقديم، ولكل مجموعة صورتان مصغرتان للرسم التخطيطي والتصميم النهائي، مما يشير إلى عملية التطوير. اللوحة B هي عرض مقدم العرض مع التعليقات المباشرة على الجانب الأيمن، محدثة فورياً. يتم تحديث متوسط الدرجات والتقييم مباشرة في عرض مقدم العرض - مصوّر في مخطط تفاعلي ديناميكي. اللوحة C هي عرض الجمهور لتقديم الدرجات والملاحظات على المشروع المقدم.

يُمنح كل عرض تقديمي نافذة زمنية محدودة للعرض التوضيحي والمناقشة. يتحول النظام تلقائياً إلى العرض التقديمي التالي عند انتهاء الجلسة الحالية، مع تجديد واجهات اللوحة B و C. أثناء العرض التقديمي، يتم مزامنة مؤقت الساعة في اللوحتين، ويتم تحديث التقييم والتعليقات المقدمة من اللوحة C مباشرة على اللوحة B. تتكون أسئلة تقييم الأقران من سبعة أسئلة على مقياس ليكرت من 10 نقاط (تتراوح من "لا أوافق بشدة (1)" إلى "أوافق بشدة (10)") وسؤال مفتوح واحد. معايير التسجيل هي كما يلي:

- Q1، هل تتبع الواجهة القواعد والمبادئ الذهبية في التصميم [22]؟
- Q2، قابلية الاستخدام: سهولة استخدام الواجهة [24].
- Q3، الجاذبية البصرية: هل التصميم جذاب بصرياً للمستخدمين [23]؟
- Q4، التفاعل: إلى أي مدى توفر الواجهة تفاعلات المستخدم [23]؟
- Q5، الصوت: جودة واستخدام الصوت بشكل صحيح من التطبيق [23].
- Q6، الجهود: هل قدمت المجموعة جهداً كافياً للعمل؟
- Q7، العمل الجماعي: هل يتم توزيع العمل بالتساوي على أعضاء الفريق؟

## 3.4 مخرجات المهام والمشاريع

كان هناك إجمالي 126 تصميم تفاعل مرئي كمخرجات للمهام والمشاريع، بما في ذلك 82 رسماً تخطيطياً من المهمة، و21 تصميماً قائماً على المشاكل، و22 حلاً قائماً على التفكير الحاسوبي. يقدم الشكل 2 بعض الأعمال المختارة المقابلة للمهمة، المشروع 1، المشروع 2، على التوالي.

أظهرت الأعمال السابقة أن هناك بعض الغموض في النتائج عندما أعطى الطلاب درجات لأقرانهم. جزء من المشكلة هو أنهم أرادوا أن يكونوا "لطيفين" أو يهدفون إلى إنجاز العمل. للتخفيف من هذه المشاكل، سيتم استبعاد أنماط الدرجات غير العادية، وسيتم إخطار المقيمين (الطلاب) بشكل مجهول من خلال أسمائهم المستعارة. يتم تقديم أمثلة على التقييم الجيد والتقييم غير الكافي في الشكل 3. يتم توضيح التقييم الجيد من خلال التنوع في نتائج التقييم بين المعايير المختلفة، عكس الأمثلة غير الكافية.

---

### Translation Notes

- **Figures referenced:** Figure 1 (User interface panels A, B, C), Figure 2 (Assignment and project outputs), Figure 3 (Grading examples)
- **Key terms introduced:** studio-based learning, design critiques, computational thinking, Likert scale, peer assessment
- **Citations:** [1], [3], [8], [9], [21], [22], [23], [24]
- **Equations:** None
- **Special handling:**
  - Characteristics labeled C1-C4 kept as is
  - Goals labeled G1-G3 kept as is
  - Questions Q1-Q7 kept as is
  - Panel labels A, B, C kept in English
  - Likert scale range kept in original format

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
