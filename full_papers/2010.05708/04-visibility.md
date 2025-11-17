# Section 4: Increasing Visibility of Formal Methods Throughout the Curriculum
## القسم 4: زيادة رؤية الأساليب الرسمية عبر المنهج

**Section:** visibility
**Translation Quality:** 0.85
**Glossary Terms Used:** formal methods (الأساليب الرسمية), curriculum (المنهج), computer science (علوم الحاسوب), software engineering (هندسة البرمجيات), quality assurance (ضمان الجودة)

---

### English Version (Summary)

In common computer science and software engineering curricula, formal methods play a minor role. There are at most one or two specialized courses focusing on teaching formal methods. Often, these courses are only weakly linked to the rest of the curriculum.

Formal methods fail to link to the current hot topics in computer science and software engineering, both in teaching and research. In consequence, even students with considerable interest in software engineering are drawn towards courses such as data science, machine learning or artificial intelligence. However, now that artificial intelligence and machine learning techniques find their way into safety critical systems (such as autonomous cars), correctness considerations become more important every day.

An ideal integration of formal methods into a computer science or software engineering curriculum should first and foremost strive to present formal methods as a quality assurance tool to be used in other areas, be it embedded systems engineering or machine learning. This first contact to formal methods would aim at teaching usage scenarios as well as techniques and how they are to be deployed.

The 2013 "Curriculum Guidelines for Undergraduate Degree Programs in Computer Science" [ACM13] lists 18 "Knowledge Areas". Suggestions for formal method units in some areas include:

- **AL-Algorithms and Complexity:** formal verification of algorithms; model checking algorithms.
- **DS-Discrete Structures:** logic, modelling, semantic foundations of formal methods.
- **HCI-Human-Computer Interaction:** mode confusion problems; formal analysis of user dialogs; cognitive models.
- **IAS-Information Assurance and Security:** formal analysis of security protocols.
- **NC-Networking and Communication:** protocol verification.
- **OS-Operating Systems:** parallel modelling; scheduling.
- **PL-Programming Languages:** semantics of programming languages; program correctness; compiler correctness.

---

### النسخة العربية

في المناهج الشائعة لعلوم الحاسوب وهندسة البرمجيات، تلعب الأساليب الرسمية دوراً ثانوياً. هناك على الأكثر مقرر أو مقرران متخصصان يركزان على تدريس الأساليب الرسمية. في كثير من الأحيان، ترتبط هذه المقررات بشكل ضعيف ببقية المنهج.

تفشل الأساليب الرسمية في الارتباط بالموضوعات الساخنة الحالية في علوم الحاسوب وهندسة البرمجيات، سواء في التدريس أو البحث. ونتيجة لذلك، حتى الطلاب الذين لديهم اهتمام كبير بهندسة البرمجيات ينجذبون نحو مقررات مثل علم البيانات أو التعلم الآلي أو الذكاء الاصطناعي. ومع ذلك، الآن بعد أن وجدت تقنيات الذكاء الاصطناعي والتعلم الآلي طريقها إلى الأنظمة الحرجة من حيث السلامة (مثل السيارات ذاتية القيادة)، أصبحت اعتبارات الصحة أكثر أهمية كل يوم.

طبيعة "الفائز يأخذ كل شيء" لصناعة البرمجيات اليوم (حيث يفوز منتج/خدمة واحدة في كل فئة بشكل أساسي ويحقق مليارات، بينما تتلاشى الحلول الأخرى، على سبيل المثال، فيسبوك لوسائل التواصل الاجتماعي؛ جوجل لمحركات البحث؛ إيباي للمزادات عبر الإنترنت؛ زوم للمناقشات/التدريس/الاجتماعات عبر الإنترنت) تبرر الاستثمار المسبق في جودة النظام. نلاحظ أن الشركات الكبرى مثل جوجل [SvGJ+15] وفيسبوك [DFLO19] وأمازون [NRZ+15] تقوم جميعها بذلك، لكن هذا لم ينتقل بعد إلى ممارسات التوظيف الخاصة بها، أو إلى تصورات الطلاب حول ما يحتاجونه للحصول على وظيفة لدى هؤلاء أرباب العمل المفضلين.

نتيجة لذلك، يجب أن يسعى التكامل المثالي للأساليب الرسمية في منهج علوم الحاسوب أو هندسة البرمجيات أولاً وقبل كل شيء إلى تقديم الأساليب الرسمية كأداة لضمان الجودة لاستخدامها في مجالات أخرى، سواء كانت هندسة الأنظمة المدمجة أو التعلم الآلي. سيهدف هذا الاتصال الأول بالأساليب الرسمية إلى تدريس سيناريوهات الاستخدام وكذلك التقنيات وكيفية نشرها.

نحن نعتقد أن إظهار فائدة الأساليب الرسمية من خلال مناقشة التطبيقات على مجالات أخرى سيحقق هدفين. أولاً، يضمن اعتبار جودة الشفرة ووظائف النظام أمراً حاسماً. علاوة على ذلك، قد يثير هذا الاتصال الأولي بالأساليب الرسمية اهتماماً في تطويرها وتحسينها. يمكن أن يكون كلا الموضوعين بعد ذلك جزءاً من مقررات مخصصة في الأساليب الرسمية.

بينما سيكون مثل هذا النهج "العرضي" مثالياً، فإنه سيتطلب من الزملاء أن يكونوا راغبين وقادرين على تدريس وحدات صغيرة حول الأساليب الرسمية. قد يكون هذا افتراضاً غير واقعي. قد يكون تنظيم "جلسات ضيوف" من خبراء الأساليب الرسمية طريقة للمضي قدماً.

للحصول على قبول لزيادة رؤية الأساليب الرسمية في منهج الجامعة، نحتاج إلى إقناع زملائنا أولاً وقبل كل شيء. في النهاية، هم من يقررون ما إذا كان/كيف/كم يجب أن يحتوي منهج الجامعة على الأساليب الرسمية. هناك منافسة كبيرة على الأماكن في المنهج بين التخصصات/المجالات المختلفة.

تسرد "إرشادات المناهج لبرامج الدرجات الجامعية في علوم الحاسوب" لعام 2013 [ACM13] 18 "مجال معرفة". في ما يلي، نقدم عدداً من الاقتراحات لوحدات الأساليب الرسمية في بعض هذه المجالات:

- **AL-الخوارزميات والتعقيد:** التحقق الرسمي من الخوارزميات؛ خوارزميات فحص النماذج.
- **DS-البنى المنفصلة:** المنطق، النمذجة، الأسس الدلالية للأساليب الرسمية.
- **HCI-التفاعل بين الإنسان والحاسوب:** مشاكل الخلط بين الأنماط؛ التحليل الرسمي لحوارات المستخدم؛ النماذج المعرفية.
- **IAS-ضمان المعلومات والأمن:** التحليل الرسمي لبروتوكولات الأمن.
- **IM-إدارة المعلومات:** تحديد وتحليل كل من الصحة والأداء لأنظمة التخزين السحابي.
- **NC-الشبكات والاتصالات:** التحقق من البروتوكولات.
- **OS-أنظمة التشغيل:** النمذجة المتوازية؛ الجدولة.
- **PBD-التطوير القائم على المنصة:** التطوير الرسمي القائم على النماذج.
- **PD-الحوسبة المتوازية والموزعة:** حسابات العمليات؛ شبكات بتري.
- **PL-لغات البرمجة:** كيفية تحليل البرمجيات المكتوبة في نموذج برمجة معين؛ صحة المترجم؛ دلالات لغات البرمجة؛ صحة البرنامج.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms:** curriculum (المنهج), knowledge areas (مجالات المعرفة), quality assurance (ضمان الجودة), safety-critical systems (الأنظمة الحرجة من حيث السلامة), autonomous cars (السيارات ذاتية القيادة), protocol verification (التحقق من البروتوكولات)
- **Citations:** [ACM13], [SvGJ+15], [DFLO19], [NRZ+15]

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.84
- Glossary consistency: 0.83
- **Overall section score:** 0.85
