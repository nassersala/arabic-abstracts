# Section 9: Threats to Validity
## القسم 9: التهديدات للصلاحية

**Section:** threats to validity
**Translation Quality:** 0.87
**Glossary Terms Used:** formal methods, model checking, user survey, one-group pretest-posttest experiment

---

### English Version

In this section, we discuss threats that might jeopardize the validity of our study results as well as on measures we take to reduce these threats. We consider threats to validity as discussed by Wohlin et al. (2012), Kitchenham and Pfleeger (2008), and Campbell and Stanley (1963). In the following, we structure them according to construct, internal, and external validity.

**Construct validity.** The prime threats to construct validity are related to the completeness of the questionnaire and in phrasing questions in a way that is understood by all participants in the same way. To mitigate these threats, we have considered the following steps in our research method: (i) we incorporated feedback from two senior engineers having background in formal methods and model checking, (ii) we incorporated feedback regarding unbiased questions from a psychologist, and (iii) we performed a pilot test with five research engineers to check for completeness and understandability.

**Internal validity.** The critical internal threat to be considered for the user survey is the selection of participants. Since we followed snowball sampling for the participant selection, there could be a possibility of several participants working in the same project, which could bias the final result. Therefore, we considered at most first four participants from each project and neglected further project members.

We consider threats to internal validity listed by Campbell and Stanley (1963) for the pretest-posttest experiment. To mitigate the history and maturation threats, we performed the posttest experiment within fifteen days following the pretest experiment. The most severe threats to be considered in this experimental design are testing and instrumentation. Those threats arise because participants get overwhelmed with the intervention including the fact that we have developed the counterexample explanation approach. Consequently, participants could answer more positively in the posttest experiment than the actual value due to the intervention. To mitigate these threats, participants conduct the study anonymously and we explicitly emphasized to the participants that the obtained study results would serve as a reference in the future to use our counterexample explanation approach for real-world projects at Bosch. Additionally, to avoid overwhelmed responses and accept only valid responses, we have added the task questions TQ1–TQ9 (Table 3); And the response is accepted as valid only if the participant attempted to answer at least some part of these questions.

Further, to reduce biasing between the pretest and posttest experiment, the use case of an airbag system (a toy example) used in the pretest is significantly less complex than the use case of the Bosch EPS system used in the posttest. However, to adjust the difficulty level of the systems used for the experiment, we used feedback from the pilot study with five research engineers. Basically, adjustment of difficulty is done by increasing or decreasing the number of components and size of the specifications which have to be understood by the participants.

Finally, another internal threat is to present the model checker's raw output with the inconsistent specification highlighted by us to the participants in the pretest. This could bias the participants' opinions that the model checker's output included the highlighted parts is easier to interpret than it actually is in practice where the highlighted parts are not available. As such, we can rather expect larger benefits of our counterexample explanation approach in practice than we observed it in the one-group pretest-posttest experiment.

**External validity.** To avoid polluting results, we do not force the participants to select an option from an answer scale for every question. For example, the participants could choose the option "No Opinion", which supports in achieving actual results. However, the participants have the choice to enter a reason as a qualitative statement if they do not want to select any option. One of the severe drawbacks of the one-group pretest-posttest experiment is its generalization. However, the benefit of our study is that we used a real-world EPS system for the posttest experiment, and the participants are professional engineers who work on real-world automotive projects at Bosch.

---

### النسخة العربية

في هذا القسم، نناقش التهديدات التي قد تُعرّض صلاحية نتائج دراستنا للخطر بالإضافة إلى التدابير التي نتخذها لتقليل هذه التهديدات. نأخذ في الاعتبار التهديدات للصلاحية كما ناقشها Wohlin وآخرون (2012)، وKitchenham وPfleeger (2008)، وCampbell وStanley (1963). فيما يلي، نُنظمها وفقاً للصلاحية البنائية والداخلية والخارجية.

**الصلاحية البنائية.** التهديدات الرئيسية للصلاحية البنائية تتعلق بكمال الاستبيان وفي صياغة الأسئلة بطريقة يفهمها جميع المشاركين بنفس الطريقة. للتخفيف من هذه التهديدات، اعتبرنا الخطوات التالية في منهجية البحث الخاصة بنا: (i) أدمجنا ملاحظات من اثنين من المهندسين الكبار ذوي الخلفية في الأساليب الرسمية وفحص النماذج، (ii) أدمجنا ملاحظات حول الأسئلة غير المُتحيّزة من طبيب نفسي، و(iii) أجرينا اختباراً تجريبياً مع خمسة مهندسي بحث للتحقق من الكمال والقابلية للفهم.

**الصلاحية الداخلية.** التهديد الداخلي الحرج الذي يجب مراعاته لمسح المستخدمين هو اختيار المشاركين. نظراً لأننا اتبعنا أخذ عينات كرة الثلج لاختيار المشاركين، يمكن أن يكون هناك احتمال لعدة مشاركين يعملون في نفس المشروع، مما قد يُحيّز النتيجة النهائية. لذلك، اعتبرنا على الأكثر أول أربعة مشاركين من كل مشروع وأهملنا أعضاء المشروع الإضافيين.

نأخذ في الاعتبار التهديدات للصلاحية الداخلية المُدرَجة بواسطة Campbell وStanley (1963) لتجربة القياس القبلي والبعدي. للتخفيف من تهديدات التاريخ والنضج، أجرينا تجربة القياس البعدي في غضون خمسة عشر يوماً بعد تجربة القياس القبلي. التهديدات الأكثر خطورة التي يجب مراعاتها في هذا التصميم التجريبي هي الاختبار والأدوات. تنشأ هذه التهديدات لأن المشاركين يُغمَرون بالتدخل بما في ذلك حقيقة أننا طورنا نهج تفسير الأمثلة المضادة. وبالتالي، يمكن للمشاركين الإجابة بشكل أكثر إيجابية في تجربة القياس البعدي من القيمة الفعلية بسبب التدخل. للتخفيف من هذه التهديدات، يُجري المشاركون الدراسة بشكل مجهول وأكدنا صراحة للمشاركين أن نتائج الدراسة المُحصلة ستعمل كمرجع في المستقبل لاستخدام نهج تفسير الأمثلة المضادة الخاص بنا لمشاريع واقعية في بوش. بالإضافة إلى ذلك، لتجنب الاستجابات المُغمَرة وقبول الاستجابات الصحيحة فقط، أضفنا أسئلة المهمة TQ1-TQ9 (الجدول 3)؛ ويتم قبول الاستجابة كصحيحة فقط إذا حاول المشارك الإجابة على جزء واحد على الأقل من هذه الأسئلة.

علاوة على ذلك، لتقليل التحيّز بين تجربة القياس القبلي والبعدي، فإن حالة استخدام نظام الوسادة الهوائية (مثال لعبة) المُستخدَم في القياس القبلي أقل تعقيداً بشكل كبير من حالة استخدام نظام EPS من بوش المُستخدَم في القياس البعدي. ومع ذلك، لضبط مستوى صعوبة الأنظمة المُستخدَمة في التجربة، استخدمنا ملاحظات من الدراسة التجريبية مع خمسة مهندسي بحث. بشكل أساسي، يتم ضبط الصعوبة من خلال زيادة أو تقليل عدد المكونات وحجم المواصفات التي يجب أن يفهمها المشاركون.

أخيراً، التهديد الداخلي الآخر هو تقديم المُخرَجات الخام لفاحص النماذج مع المواصفة غير المتسقة المُبرَزة من قبلنا للمشاركين في القياس القبلي. قد يؤدي هذا إلى تحيّز آراء المشاركين بأن مُخرَجات فاحص النماذج المتضمنة الأجزاء المُبرَزة أسهل في التفسير مما هي عليه بالفعل في الممارسة حيث الأجزاء المُبرَزة غير متوفرة. على هذا النحو، يمكننا بالأحرى توقع فوائد أكبر لنهج تفسير الأمثلة المضادة الخاص بنا في الممارسة مما لاحظناه في تجربة المجموعة الواحدة بقياس قبلي وبعدي.

**الصلاحية الخارجية.** لتجنب تلويث النتائج، لا نُجبر المشاركين على اختيار خيار من مقياس الإجابة لكل سؤال. على سبيل المثال، يمكن للمشاركين اختيار خيار "لا رأي"، مما يدعم في تحقيق النتائج الفعلية. ومع ذلك، لدى المشاركين الخيار لإدخال سبب كبيان نوعي إذا لم يرغبوا في اختيار أي خيار. أحد العيوب الشديدة لتجربة المجموعة الواحدة بقياس قبلي وبعدي هو تعميمها. ومع ذلك، فإن فائدة دراستنا هي أننا استخدمنا نظام EPS واقعي لتجربة القياس البعدي، والمشاركون هم مهندسون محترفون يعملون على مشاريع سيارات واقعية في بوش.

---

### Translation Notes

- **Key threats identified:**
  - Construct validity: questionnaire completeness and phrasing
  - Internal validity: participant selection bias, testing/instrumentation effects
  - External validity: generalization limitations

- **Mitigation measures:**
  - Pilot testing with 5 engineers
  - Feedback from psychologist for unbiased questions
  - Limit to 4 participants per project
  - Anonymous participation
  - Real-world use case (EPS system) for ecological validity

- **Special handling:**
  - Preserved methodological terminology (snowball sampling, pretest-posttest)
  - Maintained reference to Campbell and Stanley (1963) threat taxonomy
  - Kept task question references (TQ1-TQ9)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
