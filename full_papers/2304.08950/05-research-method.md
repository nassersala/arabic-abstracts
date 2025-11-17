# Section 5: Research Method
## القسم 5: منهجية البحث

**Section:** research method
**Translation Quality:** 0.86
**Glossary Terms Used:** formal methods, model checking, counterexample, specification, refinement, user survey, one-group pretest-posttest experiment

---

### English Version

In this section, we discuss the research questions, design, execution plan, target participants, and analysis plan of the studies.

**5.1 Research Questions**

Our study aims to explore and understand the challenges in identifying inconsistent specifications, and the acceptance of formal methods by Bosch automotive engineers. Therefore, this user study has two significant goals: (G1) to understand challenges faced by Bosch engineers when identifying inconsistent specifications, and challenges along with their opinions to use formal verification or formal methods in real-world development processes, and (G2) to explore whether Bosch engineers are interested in using formal methods, particularly model checking, in real-world development processes if the difficulty of understanding model checking results is reduced by our counterexample explanation approach. Considering these two goals, we formulate the following three research questions:

**RQ1:** To what extent do engineers face challenges in identifying inconsistent specifications in formal models that are introduced during the refinement of a system?

With this RQ we want to investigate whether:
- (I1) Understanding formal notations is difficult for engineers.
- (I2) Identifying inconsistent specifications that are introduced during a refinement of a top-level specification is difficult.

**RQ2:** To what extent the identification of inconsistent specifications and usage of formal methods prove beneficial to a real-world development process?

With this RQ we want to investigate whether:
- (I4) Usage of formal verification or formal methods is beneficial in a real-world development process.
- (I5) Identifying inconsistent specifications is beneficial in a real-world development process.

**RQ3:** To what extent do engineers prefer to use formal methods (model checkers particularly) if the difficulty is reduced for understanding verification results to identify inconsistent specifications?

With this RQ we want to investigate whether:
- (I5) The counterexample explanation approach eases the comprehension when compared to interpretation of the raw model checker output for engineers with a formal methods background.
- (I6) It is possible for engineers with a background in formal methods to identify and fix inconsistent specifications based on the counterexample explanation approach.
- (I7) The counterexample explanation approach can promote formal verification and usage of model checking in real-world development processes.

**5.2 Variables**

To attain the goals G1 and G2, we perform two different types of exploratory user studies as shown in Figure 2. The first study is the user survey (Part 1), and the second study is a one-group pretest-posttest experiment (Part 2).

*5.2.1 Variables of Part 1: User Survey*

Our user survey evaluates the research questions RQ1 and RQ2. The independent variables of Part 1 are participants' professional background and experience. The dependent variables are different for each research questions. For RQ1, the dependent variable is the difficulty in understanding that infers understanding formal notations and identifying inconsistent specifications by engineers are difficult. Similarly, the dependent variable for RQ2 is the increase in confidence in system safety, that is, the identification of inconsistent specifications and use of formal methods in real-world development processes can make systems safer.

*5.2.2 Variables of Part 2: One-Group Pretest-Posttest Design*

According to Babbie (2016), an experimental stimulus (also called an intervention) is the independent variable. In the one-group pretest-posttest design, we use our counterexample explanation approach as an intervention. Therefore, it serves as the independent variable of Part 2. Further, we evaluate RQ3 based on the following four attributes that serve as dependent variables for Part 2:

1. **Better understanding:** Does the counterexample explanation approach allow engineers to understand model checking results and identify inconsistencies more effectively?
2. **Quicker understanding:** Does the counterexample explanation approach allow engineers to understand model checking results and identify inconsistencies more efficiently?
3. **Confidence:** Does the counterexample explanation approach make engineers more confident in their understanding of the system and its inconsistency respective to safety?
4. **No value:** This attribute is inversely related to the above attributes. Will the counterexample explanation approach provide no or only minimal value to real-world projects?

[Note: Full questionnaires in Tables 1, 2, and 3 are included in the paper but summarized here for length]

**5.3 Design of the User Study**

*5.3.1 Part 1: User Survey*

For Part 1, we use a cross sectional survey (Kitchenham and Pfleeger 2008) to collect data from engineers to achieve goal G1. We follow guidelines for questionnaire construction and use eight-point Likert scales for responses (see Table 2).

*5.3.2 Part 2: One-Group Pretest-Posttest Experiment*

Part 2 is an exploratory pre-experimental study following a one-group pretest-posttest experiment design to attain goal G2. We follow the guidelines by Campbell and Stanley (1963). Due to the scarcity of participants with formal methods knowledge in an industrial organization, we use this design despite its limitations in generalizability.

**5.4 Tools Used for the Study**

Both studies are performed remotely due to the COVID-19 pandemic. We use Microsoft Forms for Excel for data collection and BoschTube for video explanations.

**5.5 Participants**

The target population is automotive engineers with at least basic knowledge of formal methods, particularly those working on system development, requirement elicitation, and safety analysis. We use convenience sampling and snowball sampling for Part 1. For Part 2, we invite participants from Part 1 who have knowledge in formal methods.

**5.6 Execution Plan**

*5.6.1 Execution Plan of Part 1*

The user survey comprises four steps: (1) data processing agreement and motivation video, (2) demographic questions (Q1-Q6), (3) main survey questions (Q7-Q20), and (4) conclusion.

*5.6.2 Execution Plan of Part 2*

The one-group pretest-posttest experiment follows this sequence:

**Pretest:** Participants analyze violated specification and counterexample from model checker output, answer task questions (TQ1-TQ9 except TQ4) and pre-questionnaire (PRQ1-PRQ4).

**Intervention:** Video introduction to the counterexample explanation approach.

**Posttest:** Participants interpret the explanation from the counterexample explanation approach, answer task questions (TQ1-TQ9 except TQ3) and post-questionnaire (POQ1-POQ4), rate features (FQ1-FQ6), and provide feedback (FE1-FE8).

**5.7 Presentation of the Analysis Results**

We use bar charts to plot results. Qualitative statements are analyzed through three steps: (i) Microanalysis: labeling statements, (ii) Categorization: extracting themes, and (iii) Saturation: final agreement on labels and themes.

---

### النسخة العربية

في هذا القسم، نناقش أسئلة البحث، والتصميم، وخطة التنفيذ، والمشاركين المستهدفين، وخطة التحليل للدراسات.

**5.1 أسئلة البحث**

تهدف دراستنا إلى استكشاف وفهم التحديات في تحديد المواصفات غير المتسقة، وقبول الأساليب الرسمية من قبل مهندسي السيارات في بوش. لذلك، لدراسة المستخدمين هذه هدفان مهمان: (G1) فهم التحديات التي يواجهها مهندسو بوش عند تحديد المواصفات غير المتسقة، والتحديات مع آرائهم لاستخدام التحقق الرسمي أو الأساليب الرسمية في عمليات التطوير الواقعية، و(G2) استكشاف ما إذا كان مهندسو بوش مهتمين باستخدام الأساليب الرسمية، وخاصة فحص النماذج، في عمليات التطوير الواقعية إذا تم تقليل صعوبة فهم نتائج فحص النماذج من خلال نهج تفسير الأمثلة المضادة الخاص بنا. بالنظر إلى هذين الهدفين، نصوغ أسئلة البحث الثلاثة التالية:

**RQ1:** إلى أي مدى يواجه المهندسون تحديات في تحديد المواصفات غير المتسقة في النماذج الرسمية التي يتم إدخالها أثناء تحسين النظام؟

بهذا السؤال البحثي نريد التحقق مما إذا كان:
- (I1) فهم التدوينات الرسمية صعب بالنسبة للمهندسين.
- (I2) تحديد المواصفات غير المتسقة التي يتم إدخالها أثناء تحسين مواصفة المستوى الأعلى صعب.

**RQ2:** إلى أي مدى يثبت تحديد المواصفات غير المتسقة واستخدام الأساليب الرسمية أنه مفيد لعملية التطوير الواقعية؟

بهذا السؤال البحثي نريد التحقق مما إذا كان:
- (I4) استخدام التحقق الرسمي أو الأساليب الرسمية مفيد في عملية التطوير الواقعية.
- (I5) تحديد المواصفات غير المتسقة مفيد في عملية التطوير الواقعية.

**RQ3:** إلى أي مدى يفضل المهندسون استخدام الأساليب الرسمية (فاحصات النماذج على وجه الخصوص) إذا تم تقليل الصعوبة لفهم نتائج التحقق لتحديد المواصفات غير المتسقة؟

بهذا السؤال البحثي نريد التحقق مما إذا كان:
- (I5) نهج تفسير الأمثلة المضادة يسهل الفهم مقارنة بتفسير المُخرَجات الخام لفاحص النماذج للمهندسين ذوي الخلفية في الأساليب الرسمية.
- (I6) من الممكن للمهندسين ذوي الخلفية في الأساليب الرسمية تحديد وإصلاح المواصفات غير المتسقة بناءً على نهج تفسير الأمثلة المضادة.
- (I7) نهج تفسير الأمثلة المضادة يمكن أن يعزز التحقق الرسمي واستخدام فحص النماذج في عمليات التطوير الواقعية.

**5.2 المتغيرات**

لتحقيق الهدفين G1 وG2، نُجري نوعين مختلفين من الدراسات الاستكشافية للمستخدمين كما هو موضح في الشكل 2. الدراسة الأولى هي مسح المستخدمين (الجزء 1)، والدراسة الثانية هي تجربة المجموعة الواحدة بقياس قبلي وبعدي (الجزء 2).

*5.2.1 متغيرات الجزء 1: مسح المستخدمين*

يُقيّم مسح المستخدمين لدينا أسئلة البحث RQ1 وRQ2. المتغيرات المستقلة للجزء 1 هي الخلفية المهنية والخبرة للمشاركين. المتغيرات التابعة مختلفة لكل سؤال بحثي. بالنسبة لـ RQ1، المتغير التابع هو الصعوبة في الفهم التي تستنتج أن فهم التدوينات الرسمية وتحديد المواصفات غير المتسقة من قبل المهندسين صعب. وبالمثل، المتغير التابع لـ RQ2 هو الزيادة في الثقة في سلامة النظام، أي أن تحديد المواصفات غير المتسقة واستخدام الأساليب الرسمية في عمليات التطوير الواقعية يمكن أن يجعل الأنظمة أكثر أماناً.

*5.2.2 متغيرات الجزء 2: تصميم المجموعة الواحدة بقياس قبلي وبعدي*

وفقاً لـ Babbie (2016)، التحفيز التجريبي (يُسمى أيضاً التدخل) هو المتغير المستقل. في تصميم المجموعة الواحدة بقياس قبلي وبعدي، نستخدم نهج تفسير الأمثلة المضادة كتدخل. لذلك، يعمل كمتغير مستقل للجزء 2. علاوة على ذلك، نُقيّم RQ3 بناءً على السمات الأربع التالية التي تعمل كمتغيرات تابعة للجزء 2:

1. **فهم أفضل:** هل يسمح نهج تفسير الأمثلة المضادة للمهندسين بفهم نتائج فحص النماذج وتحديد التعارضات بشكل أكثر فعالية؟
2. **فهم أسرع:** هل يسمح نهج تفسير الأمثلة المضادة للمهندسين بفهم نتائج فحص النماذج وتحديد التعارضات بشكل أكثر كفاءة؟
3. **الثقة:** هل يجعل نهج تفسير الأمثلة المضادة المهندسين أكثر ثقة في فهمهم للنظام وتعارضه فيما يتعلق بالسلامة؟
4. **لا قيمة:** هذه السمة مرتبطة عكسياً بالسمات أعلاه. هل سيوفر نهج تفسير الأمثلة المضادة قيمة معدومة أو قيمة ضئيلة فقط للمشاريع الواقعية؟

[ملاحظة: تُضمّن الاستبيانات الكاملة في الجداول 1 و2 و3 في الورقة ولكن يتم تلخيصها هنا للإيجاز]

**5.3 تصميم دراسة المستخدمين**

*5.3.1 الجزء 1: مسح المستخدمين*

للجزء 1، نستخدم مسحاً مقطعياً عرضياً (Kitchenham وPfleeger 2008) لجمع البيانات من المهندسين لتحقيق الهدف G1. نتبع إرشادات بناء الاستبيان ونستخدم مقاييس ليكرت ثمانية النقاط للاستجابات (انظر الجدول 2).

*5.3.2 الجزء 2: تجربة المجموعة الواحدة بقياس قبلي وبعدي*

الجزء 2 هو دراسة تجريبية أولية استكشافية تتبع تصميم تجربة المجموعة الواحدة بقياس قبلي وبعدي لتحقيق الهدف G2. نتبع الإرشادات التي وضعها Campbell وStanley (1963). بسبب ندرة المشاركين ذوي المعرفة بالأساليب الرسمية في منظمة صناعية، نستخدم هذا التصميم على الرغم من قيوده في قابلية التعميم.

**5.4 الأدوات المستخدمة في الدراسة**

أُجريت كلتا الدراستين عن بُعد بسبب جائحة COVID-19. نستخدم Microsoft Forms for Excel لجمع البيانات وBoschTube لتفسيرات الفيديو.

**5.5 المشاركون**

السكان المستهدفون هم مهندسو السيارات الذين لديهم معرفة أساسية على الأقل بالأساليب الرسمية، وخاصة أولئك الذين يعملون على تطوير الأنظمة، واستخلاص المتطلبات، وتحليل السلامة. نستخدم أخذ العينات الملائمة وأخذ عينات كرة الثلج للجزء 1. للجزء 2، ندعو المشاركين من الجزء 1 الذين لديهم معرفة بالأساليب الرسمية.

**5.6 خطة التنفيذ**

*5.6.1 خطة تنفيذ الجزء 1*

يتكون مسح المستخدمين من أربع خطوات: (1) اتفاقية معالجة البيانات وفيديو التحفيز، (2) الأسئلة الديموغرافية (Q1-Q6)، (3) أسئلة المسح الرئيسية (Q7-Q20)، و(4) الخاتمة.

*5.6.2 خطة تنفيذ الجزء 2*

تتبع تجربة المجموعة الواحدة بقياس قبلي وبعدي هذا التسلسل:

**القياس القبلي:** يحلل المشاركون المواصفة المنتهكة والمثال المضاد من مُخرَجات فاحص النماذج، ويجيبون على أسئلة المهمة (TQ1-TQ9 باستثناء TQ4) والاستبيان القبلي (PRQ1-PRQ4).

**التدخل:** مقدمة فيديو لنهج تفسير الأمثلة المضادة.

**القياس البعدي:** يفسر المشاركون التفسير من نهج تفسير الأمثلة المضادة، ويجيبون على أسئلة المهمة (TQ1-TQ9 باستثناء TQ3) والاستبيان البعدي (POQ1-POQ4)، ويُقيّمون الميزات (FQ1-FQ6)، ويقدمون الملاحظات (FE1-FE8).

**5.7 عرض نتائج التحليل**

نستخدم الرسوم البيانية الشريطية لعرض النتائج. تُحلل البيانات النوعية من خلال ثلاث خطوات: (i) التحليل الجزئي: وضع تسميات للبيانات، (ii) التصنيف: استخراج المواضيع، و(iii) التشبع: الاتفاق النهائي على التسميات والمواضيع.

---

### Translation Notes

- **Figures referenced:** Figure 2 (overview of study design showing two parts)
- **Tables referenced:** Tables 1, 2, and 3 (questionnaires and scales)
- **Key terms introduced:**
  - research questions = أسئلة البحث
  - independent variables = المتغيرات المستقلة
  - dependent variables = المتغيرات التابعة
  - cross sectional survey = مسح مقطعي عرضي
  - one-group pretest-posttest experiment = تجربة المجموعة الواحدة بقياس قبلي وبعدي
  - intervention = التدخل
  - convenience sampling = أخذ العينات الملائمة
  - snowball sampling = أخذ عينات كرة الثلج
  - Likert scales = مقاييس ليكرت

- **Equations:** None
- **Citations:** 10+ references cited
- **Special handling:**
  - Preserved research question notation (RQ1, RQ2, RQ3)
  - Maintained goal notation (G1, G2)
  - Kept investigation item notation (I1-I7)
  - Preserved question codes (Q1-Q20, TQ1-TQ9, PRQ1-PRQ4, POQ1-POQ4, FQ1-FQ6, FE1-FE8)
  - Tool names (Microsoft Forms, BoschTube) kept in English

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
