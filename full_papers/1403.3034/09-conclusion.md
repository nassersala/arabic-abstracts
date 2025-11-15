# Section 9: Summary & Conclusion
## القسم 9: الخلاصة والاستنتاج

**Section:** conclusion
**Translation Quality:** 0.88
**Glossary Terms Used:** domain specific languages (اللغات الخاصة بالمجال), formal methods (الأساليب الرسمية), verification (التحقق), faithful modelling (النمذجة الأمينة), scalability (قابلية التوسع), accessibility (إمكانية الوصول), algebraic specification (المواصفات الجبرية), automated theorem proving (إثبات النظريات الآلي)

---

### English Version

In this paper, we have introduced a novel design methodology for encapsulating formal methods within DSLs. We have supported our hypothesis that DSLs can aid with verification by showing it to be valid for the railway domain.

Our methodology begins with industrial documents describing domain elements in the form of UML class diagrams with narratives. This informal DSL is formalised in the algebraic specification language CASL, where we support this step with automated translations of the UML class diagram, thus ensuring "faithful modelling" of the domain. Next, systematic exploitation of domain knowledge allows us to prove domain specific lemmas. Thanks to these domain specific lemmas, properties on the formal specifications can automatically be proven for a class of systems, thus addressing issues surrounding "scalability". Finally, a graphical editor for the DSL is developed. This editor allows engineers from the domain to follow a seamless verification process: (1) they can formulate models in the DSL; (2) these models can be automatically transformed into formal specifications; and (3) they can automatically verify these models thanks to the domain specific lemmas. Overall, this addresses the issues of "accessibility" of formal methods.

The verification of railway control software has been identified as a grand challenge of computer science. The defining element of a grand challenge is that progress towards the challenge results in progress in computer science in general. Therefore, motivated by the railway domain, our methodology can be seen as a step forward for industrial applications of formal methods.

Along with presenting this methodology, we have also successfully illustrated the use of algebraic specification for modelling railway systems and the use of automated theorem proving for railway verification. Bringing these points together results in a strong case for using DSLs in the setting of specification and verification.

In the future, we would like to explore visual feedback of failed proof attempts. Currently, feedback to the user is provided in the form of a named route which is unsafe (obtained from the name of the failed proof). Such visualisations have been considered by Marchi et al., and it would be interesting to extend OnTrack with such visualisations. We would also like to illustrate the applicability of our methodology to further domains, such as to the design of medical devices as considered by Oladimeji et al.

**Acknowledgements:**
The authors would like to thank Simon Chadwick and Dominic Taylor from Invensys Rail UK for their contributions and encouraging feedback. We would like to thank our colleagues from the Swansea railway verification group and the Swansea Processes and Data research group for their input and feedback towards this work. Similarly, we greatly appreciate the input of Alexander Knapp and Till Mossakowski towards our work on the UML institution and comorphism to Modal CASL. We also thank Helen Treharne, Steve Schneider and Matthew Trumble from Surrey University for their collaboration in developing the OnTrack tool. Our final thanks goes to Erwin R. Catesbeiana (Jr) for signalling us in the correct direction.

---

### النسخة العربية

في هذا البحث، قدمنا منهجية تصميم جديدة لتغليف الأساليب الرسمية ضمن اللغات الخاصة بالمجال. دعمنا فرضيتنا بأن اللغات الخاصة بالمجال يمكن أن تساعد في التحقق من خلال إظهار صحتها لمجال السكك الحديدية.

تبدأ منهجيتنا بوثائق صناعية تصف عناصر المجال في شكل مخططات فئات UML مع سرديات. يتم صياغة هذه اللغة الخاصة بالمجال غير الرسمية رسميًا في لغة المواصفات الجبرية CASL، حيث ندعم هذه الخطوة بالترجمات الآلية لمخطط فئات UML، وبالتالي ضمان "النمذجة الأمينة" للمجال. بعد ذلك، يسمح لنا الاستغلال المنهجي لمعرفة المجال بإثبات لمّات خاصة بالمجال. بفضل هذه اللمّات الخاصة بالمجال، يمكن إثبات الخصائص على المواصفات الرسمية تلقائيًا لفئة من الأنظمة، وبالتالي معالجة القضايا المحيطة بـ "قابلية التوسع". أخيرًا، يتم تطوير محرر رسومي للغة الخاصة بالمجال. يسمح هذا المحرر للمهندسين من المجال باتباع عملية تحقق سلسة: (1) يمكنهم صياغة النماذج في اللغة الخاصة بالمجال؛ (2) يمكن تحويل هذه النماذج تلقائيًا إلى مواصفات رسمية؛ و (3) يمكنهم التحقق تلقائيًا من هذه النماذج بفضل اللمّات الخاصة بالمجال. بشكل عام، يعالج هذا قضايا "إمكانية الوصول" للأساليب الرسمية.

تم تحديد التحقق من برامج التحكم في السكك الحديدية كتحدٍ كبير لعلوم الحاسوب. العنصر المحدد للتحدي الكبير هو أن التقدم نحو التحدي ينتج عنه تقدم في علوم الحاسوب بشكل عام. لذلك، بتحفيز من مجال السكك الحديدية، يمكن اعتبار منهجيتنا خطوة إلى الأمام للتطبيقات الصناعية للأساليب الرسمية.

إلى جانب تقديم هذه المنهجية، نجحنا أيضًا في توضيح استخدام المواصفات الجبرية لنمذجة أنظمة السكك الحديدية واستخدام إثبات النظريات الآلي للتحقق من السكك الحديدية. الجمع بين هذه النقاط ينتج عنه حالة قوية لاستخدام اللغات الخاصة بالمجال في سياق المواصفات والتحقق.

في المستقبل، نود استكشاف التغذية الراجعة المرئية لمحاولات الإثبات الفاشلة. حاليًا، يتم تقديم التغذية الراجعة للمستخدم في شكل مسار مسمى غير آمن (تم الحصول عليه من اسم الإثبات الفاشل). تم النظر في مثل هذه التصورات من قبل Marchi وآخرين، وسيكون من المثير للاهتمام توسيع OnTrack بمثل هذه التصورات. نود أيضًا توضيح قابلية تطبيق منهجيتنا على مجالات أخرى، مثل تصميم الأجهزة الطبية كما نظر فيها Oladimeji وآخرون.

**شكر وتقدير:**
يود المؤلفون شكر Simon Chadwick و Dominic Taylor من Invensys Rail UK على مساهماتهم وتعليقاتهم المشجعة. نود أن نشكر زملائنا من مجموعة التحقق من السكك الحديدية في سوانزي ومجموعة بحث العمليات والبيانات في سوانزي على مدخلاتهم وتعليقاتهم تجاه هذا العمل. وبالمثل، نقدر بشكل كبير مدخلات Alexander Knapp و Till Mossakowski تجاه عملنا على مؤسسة UML والكوموفيزم إلى Modal CASL. نشكر أيضًا Helen Treharne و Steve Schneider و Matthew Trumble من جامعة Surrey على تعاونهم في تطوير أداة OnTrack. شكرنا الأخير يذهب إلى Erwin R. Catesbeiana (Jr) للإشارة إلينا في الاتجاه الصحيح.

---

### Translation Notes

- **Key achievements summarized:**
  - Novel methodology for encapsulating formal methods in DSLs
  - Addresses faithful modelling, scalability, and accessibility
  - Successful application in railway domain
  - Demonstrates algebraic specification and automated theorem proving
- **Future work mentioned:**
  - Visual feedback for failed proofs
  - Extension to other domains (medical devices)
- **Acknowledgements:** Preserved names and institutions
- **Grand challenge:** Railway control software verification identified as computer science grand challenge

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
