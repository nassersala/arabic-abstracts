# Section 8: Reflection on Industrial Collaboration
## القسم 8: تأمل في التعاون الصناعي

**Section:** reflection
**Translation Quality:** 0.86
**Glossary Terms Used:** formal methods (الأساليب الرسمية), verification (التحقق), interlocking (التشابك), scheme plan (مخطط الخطة), graphical editor (محرر رسومي), automated verification (التحقق الآلي)

---

### English Version

Since 2007, the Railway Verification Group at Swansea University Computer Science has been working in collaboration with Invensys Rail. The group is supported by eight academics. It adopts formal techniques to railway systems. This setup has led to a rich process of information exchange, by mutual visits and internships, as well as regular meetings. Out of this collaboration, there have been several successful research projects covering research into verification of interlocking programs, the verification of scheme plan designs, and capacity analysis. These projects have involved many specification formalisms including propositional logic, CSP, Timed CSP, CSP-B, Scade, CASL and Agda. Here, it appears that operational based models such as the one we have provided in CASL are easier for railway engineers to follow and understand.

The methodology outlined in this paper has also been successfully applied to the Invensys Rail Data Model, see [citation] for full details. In this context, the DSL definition is provided by Invensys Rail in the form of UML class diagrams with accompanying narrative. This DSL definition has been completely designed by Invensys Rail without our support. Hence, developing the informal DSL that is used as a starting point for our methodology is clearly a task that can be undertaken purely within industry. With regards to the formalisation of the DSL in CASL, this step was performed in a cyclic manner. Namely, the computer scientists would suggest a formalisation at a meeting with Invensys Rail, and then feedback would be provided on the formalisation. This process was repeated until both groups were happy with the resulting formalisation. Verification support (in terms of supporting lemmas) was then developed purely by the computer scientists at Swansea. As this step does not alter the DSL, the engineers were happy with the approach.

Finally, the graphical front end to the OnTrack tool provides a view to scheme plans that is of the same nature as representations used within Invensys Rail. The railway engineers have seen the verification process we propose and are confident that they could follow it thanks to the automated nature of the process. They have expressed an interest in the extension of OnTrack to allow for importing and exporting of models using an industrial format such as the XLDL (XML Layout Description Language) format used by Invensys Rail. This would allow the toolset to be more easily integrated within current development processes at Invensys Rail. We note that even though Invensys Rail believe technologies such as the OnTrack toolset will improve their development processes, due to concerns around the integrity of automated verification tools, quality assurance of a scheme plan design will, in the near future, still rely upon traditional testing and inspection. Here, tool qualification is the issue: our tools are not yet "proven-in-use", i.e., there is no experience from previous industrial safety-critical projects suggesting that our tools are "correct"; alternatively, our tools are not yet certified by a designated authority.

Finally, it remains future work to perform a systematic evaluation into how usable the presented verification is for railway engineers. To do this, one could carry out a pilot project. This would involve thorough time measurement and documentation for all activities that our approach incurs including installing, using, and integrating OnTrack into the development process. Reflecting upon these results would allow us to check if our approach is indeed feasible. On the management level, such a pilot project would then have to be evaluated as to whether it is an improvement with respect to current practice. It should be both more effective, in that it allows one to achieve better results than current practice, and more efficient, i.e., it should offer a better cost/result ratio.

---

### النسخة العربية

منذ عام 2007، تعمل مجموعة التحقق من السكك الحديدية في قسم علوم الحاسوب بجامعة سوانزي بالتعاون مع Invensys Rail. تدعم المجموعة ثمانية أكاديميين. تعتمد التقنيات الرسمية لأنظمة السكك الحديدية. أدى هذا الإعداد إلى عملية غنية لتبادل المعلومات، من خلال الزيارات المتبادلة والتدريب الداخلي، وكذلك الاجتماعات المنتظمة. من هذا التعاون، كانت هناك عدة مشاريع بحثية ناجحة تغطي البحث في التحقق من برامج التشابك، والتحقق من تصميمات مخططات الخطط، وتحليل السعة. شملت هذه المشاريع العديد من الشكليات للمواصفات بما في ذلك المنطق القضوي، وCSP، وTimed CSP، وCSP-B، وScade، وCASL، وAgda. هنا، يبدو أن النماذج القائمة على التشغيل مثل تلك التي قدمناها في CASL أسهل لمهندسي السكك الحديدية للمتابعة والفهم.

تم أيضًا تطبيق المنهجية الموضحة في هذا البحث بنجاح على نموذج بيانات Invensys Rail، انظر [الاستشهاد] للحصول على التفاصيل الكاملة. في هذا السياق، يتم توفير تعريف اللغة الخاصة بالمجال من قبل Invensys Rail في شكل مخططات فئات UML مع سرد مصاحب. تم تصميم تعريف اللغة الخاصة بالمجال هذا بالكامل من قبل Invensys Rail بدون دعمنا. وبالتالي، فإن تطوير اللغة الخاصة بالمجال غير الرسمية المستخدمة كنقطة انطلاق لمنهجيتنا هي بوضوح مهمة يمكن القيام بها بشكل حصري داخل الصناعة. فيما يتعلق بالصياغة الرسمية للغة الخاصة بالمجال في CASL، تم تنفيذ هذه الخطوة بطريقة دورية. أي، أن علماء الحاسوب كانوا يقترحون صياغة رسمية في اجتماع مع Invensys Rail، ثم يتم تقديم تعليقات على الصياغة الرسمية. تكررت هذه العملية حتى كانت كلتا المجموعتين راضيتين عن الصياغة الرسمية الناتجة. تم بعد ذلك تطوير دعم التحقق (من حيث اللمّات الداعمة) بشكل حصري من قبل علماء الحاسوب في سوانزي. نظرًا لأن هذه الخطوة لا تغير اللغة الخاصة بالمجال، كان المهندسون راضين عن النهج.

أخيرًا، توفر الواجهة الأمامية الرسومية لأداة OnTrack عرضًا لمخططات الخطط من نفس طبيعة التمثيلات المستخدمة داخل Invensys Rail. شاهد مهندسو السكك الحديدية عملية التحقق التي نقترحها وهم واثقون من أنهم يمكنهم متابعتها بفضل الطبيعة الآلية للعملية. أعربوا عن اهتمامهم بتوسيع OnTrack للسماح باستيراد وتصدير النماذج باستخدام تنسيق صناعي مثل تنسيق XLDL (لغة وصف التخطيط XML) المستخدم من قبل Invensys Rail. سيسمح ذلك بدمج مجموعة الأدوات بسهولة أكبر ضمن عمليات التطوير الحالية في Invensys Rail. نلاحظ أنه على الرغم من أن Invensys Rail تعتقد أن التقنيات مثل مجموعة أدوات OnTrack ستحسن عمليات التطوير الخاصة بهم، بسبب المخاوف المتعلقة بسلامة أدوات التحقق الآلي، فإن ضمان الجودة لتصميم مخطط الخطة سيعتمد، في المستقبل القريب، لا يزال على الاختبار والفحص التقليديين. هنا، تأهيل الأداة هو القضية: أدواتنا ليست بعد "مثبتة في الاستخدام"، أي أنه لا توجد خبرة من مشاريع صناعية حرجة للسلامة سابقة تشير إلى أن أدواتنا "صحيحة"؛ بدلاً من ذلك، لم يتم بعد اعتماد أدواتنا من قبل سلطة معينة.

أخيرًا، يبقى العمل المستقبلي لإجراء تقييم منهجي حول مدى قابلية استخدام التحقق المقدم لمهندسي السكك الحديدية. للقيام بذلك، يمكن للمرء تنفيذ مشروع تجريبي. سيتضمن ذلك قياسًا دقيقًا للوقت وتوثيقًا لجميع الأنشطة التي يتكبدها نهجنا بما في ذلك تثبيت واستخدام ودمج OnTrack في عملية التطوير. التأمل في هذه النتائج سيسمح لنا بالتحقق مما إذا كان نهجنا قابلاً للتطبيق بالفعل. على مستوى الإدارة، سيتعين بعد ذلك تقييم مثل هذا المشروع التجريبي لمعرفة ما إذا كان تحسينًا فيما يتعلق بالممارسة الحالية. يجب أن يكون أكثر فعالية، من حيث أنه يسمح بتحقيق نتائج أفضل من الممارسة الحالية، وأكثر كفاءة، أي يجب أن يقدم نسبة أفضل للتكلفة/النتيجة.

---

### Translation Notes

- **Key organizations mentioned:** Swansea University, Invensys Rail
- **Tools/systems referenced:** OnTrack, XLDL, CSP, Timed CSP, CSP-B, Scade, CASL, Agda
- **Main themes:**
  - University-industry collaboration
  - Iterative development process
  - Tool qualification and certification challenges
  - Future evaluation needs
- **Special handling:** Industrial partnership details, tool certification concerns, future work discussion

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
