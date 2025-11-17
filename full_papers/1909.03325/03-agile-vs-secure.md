# Section 3: Agile versus Secure
## القسم 3: التطوير الرشيق مقابل الأمان

**Section:** agile-vs-secure
**Translation Quality:** 0.86
**Glossary Terms Used:** Agile Development (التطوير الرشيق), security (الأمن), safety-critical (حرج من حيث السلامة), non-functional requirement (متطلب غير وظيفي)

---

### English Version

"Agile Development" [6] is a major theme in software development. Mark Zuckerberg can be said to have taken this theme to the extreme in 2009.

> "Move fast and break things" is Mark's prime directive to his developers and team. "Unless you are breaking stuff," he says, "you are not moving fast enough." [9]

In both safety-critical and security-conscious programming, "breaking things" comes with a very high price. Aeroplanes can't be uncrashed, and data can't be unleaked.

The problems with using "Agile" methods in security are well-documented, at practitioner level, e.g. a recent "Security + Agile = FAIL" presentation [38], in many theoretical analyses as well as the interview-based research in [3] for small teams and [29] for large multi-team projects. Both mention team expertise in security as a significant problem.

[3] The overall security in a project depends on the security expertise of the individuals, either on the customer or developer side. This corresponds to the agile value of "individuals and interaction over processes and tools" [6, Value 1].

[29] The interviewees generally agree that more could be done to provide security education and training to employees. Without prompting, several interviewees mentioned training as an important factor for increasing security awareness and expertise.

It is very hard to take security seriously in this setting.

[3] security "is only of interest [to the customer] when money-aspects are concerned".

[29] One Test Manager articulated his team view that "security is not currently seen as part of working software, it only costs extra time and it doesn't provide functionality". With less focus on providing extensive (security) documentation typical for agile, ineffective knowledge sharing between security officers and agile team members is especially problematic.

[64] "Security is often referred to as a NFR [non-functional requirement] in that it is expected to be included as part of high quality code development, but is rarely listed as an explicit requirement. As a result, developers prioritise security below more-visible functional requirements or even easy-to-measure activities such as closing bug tracking tickets."

It would be tempting to conclude that "Agile" and "Secure" are, or at least are close to being, mutually contradictory. But there has been some analysis of the same apparent contradiction in the safety-critical industry [15]. Other than "Embedded Systems" [15, §3.6], this analysis of the problems is fairly close to the practitioner view in [38], and we could reasonably ask what lessons could be carried across.

---

### النسخة العربية

يُعد "التطوير الرشيق" [6] موضوعاً رئيسياً في تطوير البرمجيات. يمكن القول إن مارك زوكربيرغ أخذ هذا الموضوع إلى أقصى الحدود في عام 2009.

> "تحرك بسرعة واكسر الأشياء" هو التوجيه الأساسي لمارك إلى مطوريه وفريقه. "ما لم تكن تكسر الأشياء"، كما يقول، "فأنت لا تتحرك بسرعة كافية." [9]

في كل من البرمجة الحرجة من حيث السلامة والبرمجة الواعية بالأمن، يأتي "كسر الأشياء" بثمن باهظ للغاية. لا يمكن إلغاء تحطم الطائرات، ولا يمكن إلغاء تسريب البيانات.

المشاكل المتعلقة باستخدام الأساليب "الرشيقة" في الأمن موثقة جيداً، على مستوى الممارسين، مثل عرض تقديمي حديث بعنوان "الأمن + الرشاقة = فشل" [38]، في العديد من التحليلات النظرية بالإضافة إلى البحث القائم على المقابلات في [3] للفرق الصغيرة و [29] للمشاريع متعددة الفرق الكبيرة. يذكر كلاهما خبرة الفريق في الأمن كمشكلة كبيرة.

[3] يعتمد الأمن الشامل في المشروع على خبرة الأفراد في الأمن، سواء على جانب العميل أو المطور. وهذا يتوافق مع قيمة الرشاقة المتمثلة في "الأفراد والتفاعل فوق العمليات والأدوات" [6، القيمة 1].

[29] يتفق المستجوبون عموماً على أنه يمكن فعل المزيد لتوفير التعليم والتدريب الأمني للموظفين. دون مطالبة، ذكر العديد من المستجوبين التدريب كعامل مهم لزيادة الوعي الأمني والخبرة.

من الصعب جداً أخذ الأمن على محمل الجد في هذا السياق.

[3] الأمن "محل اهتمام [للعميل] فقط عندما تكون الجوانب المالية معنية".

[29] عبّر أحد مديري الاختبار عن رأي فريقه بأن "الأمن لا يُنظر إليه حالياً كجزء من البرمجيات العاملة، بل يكلف وقتاً إضافياً فقط ولا يوفر وظائف". مع التركيز الأقل على توفير التوثيق الشامل (الأمني) النموذجي للرشاقة، فإن مشاركة المعرفة غير الفعالة بين مسؤولي الأمن وأعضاء الفريق الرشيق إشكالية بشكل خاص.

[64] "غالباً ما يُشار إلى الأمن باعتباره NFR [متطلب غير وظيفي] من حيث أنه من المتوقع تضمينه كجزء من تطوير كود عالي الجودة، لكن نادراً ما يتم إدراجه كمتطلب صريح. ونتيجة لذلك، يعطي المطورون الأولوية للأمن أقل من المتطلبات الوظيفية الأكثر وضوحاً أو حتى الأنشطة سهلة القياس مثل إغلاق تذاكر تتبع الأخطاء."

سيكون من المغري الاستنتاج أن "الرشاقة" و"الأمان" متناقضان بشكل متبادل، أو على الأقل قريبان من ذلك. لكن كان هناك بعض التحليل لنفس التناقض الظاهر في الصناعة الحرجة من حيث السلامة [15]. بخلاف "الأنظمة المدمجة" [15، §3.6]، فإن هذا التحليل للمشاكل قريب جداً من وجهة نظر الممارسين في [38]، ويمكننا بشكل معقول أن نسأل عن الدروس التي يمكن نقلها.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** Agile Development, safety-critical programming, non-functional requirement (NFR), security awareness, knowledge sharing
- **Equations:** 0
- **Citations:** [3], [6], [9], [15], [29], [38], [64]
- **Special handling:** Mark Zuckerberg's quote preserved; references to interview-based research findings included verbatim; "Move fast and break things" famous quote kept in context

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
