# Section 1: Introduction/Motivation
## القسم 1: المقدمة والدافع

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** state machine, model checking, type checking, property-based testing, dependent types, embedded domain specific language, formal verification

---

### English Version

Stateful computer systems are ubiquitous. Embedded devices, computer networks and banking systems all involve states and transitions between different states. We can formally verify programs using tools like Spin [30] or Uppaal [5], however these tools rarely scale to real-world code bases due to the State Explosion Problem (although progress is steadily being made) [22–24,26,40]. There are also several testing tools and methodologies one can employ, such as Test-Driven Development — à la JUnit — and Fuzz-testing [29,41], which typically target imperative programming languages.

For functional languages, Property Based Testing (PBT) using QuickCheck [19] has proven widely successful [2,18,20,31,32] and been ported to other languages, both functional and imperative [6,27,36]. Test-driven methods are well understood, but the tests are only as good as the cases which the programmer can think of. On the flip side, model-checking tools require a secondary implementation of the program in the form of a formal model, which opens the verification process up to errors in translation leading to a semantic mismatch between the running code and the verified model [2].

Dependently Typed languages like Agda [8] and Idris [9,12] can be used for "correct by construction" programming, where typically an Embedded Domain Specific Language (eDSL) is constructed to ensure the program is valid by definition [7,13,14,16]. However, well-typed programs can go wrong. Occasionally, this is due to bugs in the type checker [17] or due to problems with how programmers use the language-provided escape hatches [37], but there is also a third, arguably more likely, case: what if the types themselves are subtly incorrect? One could imagine a program requiring that a certain number remain positive but either by habit or by accident, the programmer gives the type Int instead of Nat. This is unlikely to be caught by the type checker, tests, or implementations, as the programmers are likely to carry this assumption in their minds, thereby avoiding including it in both tests and implementation error-checks. Nevertheless, the code modelling the specification has now introduced subtly different permitted states. How can we be sure that the DSL does not accidentally permit an incorrect state or transition?

## 1.1 Contributions

We make the following contributions:

• An implementation of QuickCheck for use with dependent types at compile time.

• A framework for simultaneously specifying, implementing, and testing a stateful model of an Automated Teller Machine (ATM), using QuickCheck to increase confidence in the correctness of all 3 parts.

• We demonstrate the power of the framework by generalising it to stateful programs, both finite and infinite, and evaluate it by implementing an example of a network protocol.

In doing so, we aim to increase confidence in the correctness of the types we use to model stateful systems, using type level testing to help us understand the behaviour of state machines.

---

### النسخة العربية

الأنظمة الحاسوبية ذات الحالات موجودة في كل مكان. الأجهزة المدمجة، وشبكات الحاسوب، والأنظمة المصرفية جميعها تتضمن حالات وانتقالات بين حالات مختلفة. يمكننا التحقق رسمياً من البرامج باستخدام أدوات مثل Spin [30] أو Uppaal [5]، ومع ذلك نادراً ما تتوسع هذه الأدوات لتشمل قواعد الشفرة الواقعية بسبب مشكلة انفجار الحالات (على الرغم من أن التقدم يُحرز بشكل مطرد) [22–24,26,40]. هناك أيضاً العديد من أدوات ومنهجيات الاختبار التي يمكن للمرء استخدامها، مثل التطوير الموجه بالاختبار — على غرار JUnit — واختبار التشويش [29,41]، والتي تستهدف عادةً لغات البرمجة الأمرية.

بالنسبة للغات البرمجة الوظيفية، أثبت الاختبار القائم على الخصائص (PBT) باستخدام QuickCheck [19] نجاحاً واسعاً [2,18,20,31,32] وتم نقله إلى لغات أخرى، سواء وظيفية أو أمرية [6,27,36]. الطرق الموجهة بالاختبار مفهومة جيداً، ولكن الاختبارات جيدة فقط بقدر الحالات التي يمكن للمبرمج التفكير فيها. من الجانب الآخر، تتطلب أدوات فحص النماذج تطبيقاً ثانوياً للبرنامج في شكل نموذج رسمي، مما يفتح عملية التحقق لأخطاء في الترجمة تؤدي إلى عدم تطابق دلالي بين الشفرة المنفذة والنموذج المُتحقق منه [2].

يمكن استخدام اللغات المكتوبة تابعياً مثل Agda [8] و Idris [9,12] للبرمجة "الصحيحة بالبناء"، حيث يتم عادةً بناء لغة مجال محددة مدمجة (eDSL) لضمان أن البرنامج صالح بالتعريف [7,13,14,16]. ومع ذلك، يمكن أن تخطئ البرامج المكتوبة جيداً. في بعض الأحيان، يكون هذا بسبب أخطاء في مدقق الأنواع [17] أو بسبب مشاكل في كيفية استخدام المبرمجين لمنافذ الهروب التي توفرها اللغة [37]، ولكن هناك أيضاً حالة ثالثة، يمكن القول إنها الأكثر احتمالاً: ماذا لو كانت الأنواع نفسها غير صحيحة بشكل خفي؟ يمكن للمرء أن يتخيل برنامجاً يتطلب أن يبقى عدد معين موجباً ولكن إما بالعادة أو بالخطأ، يعطي المبرمج النوع Int بدلاً من Nat. من غير المرجح أن يتم اكتشاف هذا بواسطة مدقق الأنواع أو الاختبارات أو التطبيقات، حيث من المحتمل أن يحمل المبرمجون هذا الافتراض في أذهانهم، وبالتالي يتجنبون تضمينه في كل من الاختبارات وفحوصات أخطاء التطبيق. ومع ذلك، فإن الشفرة التي تنمذج المواصفة قد أدخلت الآن حالات مسموحة مختلفة بشكل خفي. كيف يمكننا التأكد من أن لغة المجال المحددة لا تسمح عن طريق الخطأ بحالة أو انتقال غير صحيح؟

## 1.1 المساهمات

نقدم المساهمات التالية:

• تطبيق لـ QuickCheck للاستخدام مع الأنواع التابعة في وقت الترجمة.

• إطار عمل لتحديد وتطبيق واختبار نموذج حالة لآلة الصراف الآلي (ATM) في نفس الوقت، باستخدام QuickCheck لزيادة الثقة في صحة الأجزاء الثلاثة.

• نوضح قوة إطار العمل من خلال تعميمه على البرامج ذات الحالات، سواء المحدودة أو اللانهائية، ونقيّمه من خلال تطبيق مثال على بروتوكول شبكة.

في القيام بذلك، نهدف إلى زيادة الثقة في صحة الأنواع التي نستخدمها لنمذجة الأنظمة ذات الحالات، باستخدام الاختبار على مستوى الأنواع لمساعدتنا على فهم سلوك آلات الحالة.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:**
  - State Explosion Problem - مشكلة انفجار الحالات
  - Property Based Testing (PBT) - الاختبار القائم على الخصائص
  - Fuzz-testing - اختبار التشويش
  - Embedded Domain Specific Language (eDSL) - لغة مجال محددة مدمجة
  - Correct by construction - صحيح بالبناء
  - Dependent types - الأنواع التابعة
  - Type checker - مدقق الأنواع
  - State machine - آلة الحالة
  - Automated Teller Machine (ATM) - آلة الصراف الآلي

- **Equations:** None
- **Citations:** [2,5,6,7,8,9,12,13,14,16,17,18,19,20,22–24,26,27,29,30,31,32,36,37,40,41]
- **Special handling:** Technical tool names (Spin, Uppaal, QuickCheck, JUnit, Agda, Idris) kept in English

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.86
- **Overall section score:** 0.87
