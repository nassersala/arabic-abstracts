# Section 5: Evaluation & Further Work
## القسم 5: التقييم والعمل المستقبلي

**Section:** evaluation
**Translation Quality:** 0.85
**Glossary Terms Used:** domain specific language, type checker, model checking, temporal logic, performance

---

### English Version

The types, state transitions, and Traceable implementation for ARQ come to around 30 lines of code, in contrast to the nearly 80 we had to write just for the supports for the ATM in section 3.3.2. These are tricky lines of code — weaving the state in the types and making sure the trace generation follows the correct sequence — so having them in a generalised form saves us from the risk of incorrectly reimplementing them, in addition to also saving us a lot of tedious work.

It could be argued that most DSLs are simple enough to manually reason about. However, as we have seen, seemingly trivial DSLs like the one for the ATM are easy to get wrong and this mistake can remain undetected for years. For more involved use cases like network protocols, resource management, or concurrency, where the host type system is leveraged to provide certain desirable guarantees for the target domain [7,13,14,16,25,28], the risk of the DSL accidentally introducing subtle inconsistencies and unintended behaviour, is likely to be much higher, weakening the goal of eliminating certain bugs by using a stricter host language. Combined with the ubiquity of stateful systems, we therefore believe that our approach is worthwhile and intend to model and test more advanced protocols in the future.

Throughout the paper, all the traces have had seemingly magic numbers as their bound. The numbers were determined partially on reasoning: it is possible to get a good estimate of the depth needed by taking the number of transitions in the ISM, deciding on an upper bound for when the system should be in the desired state, and multiplying this by the number of transitions (or the number of states) in the system. Should the properties fail, they can be examined to either reveal a valid error case, possibly a fault in the generators, or a false positive caused by the model (as happened in [32]). For true positives the depth can be doubled until they pass, at which point a binary search can be used to find the smallest valid bound. We believe this to be part of the confidence building: the programmers can increase the bound until they are confident in their typed models, or they can decide that the current bound is sufficient. In our experience, this is not a hindrance, as the properties fail quickly, thereby quickly finding the initial upper bound.

The type-level PBT for the ARQ model takes around 3.5 seconds on a reasonably modern laptop¹. While this may seem slow, it is worth remembering that the type checker is doing a lot of work. It is solving interface constraints, unifying values, running a PRNG, and doing equality checks for non-trivial types at least 100 times. The Idris2 type checker is currently the main bottleneck to our approach and presents many interesting research questions in terms of how to speed up the elaboration process, when to expand and inline certain functions and datatypes, and how much information to keep around in the type checker and elaborator.

In the future, we plan to examine and implement increasingly more advanced systems. ARQ with Sliding Window [33] would be a nice extension to the ARQ example, as it improves the throughput of the protocol and presents some new challenges for the state function: how do we best model the packet window's movements? Pick and Place machines used for automatic placement of surface mounted components [1], file systems [18], and protocols with crash-stop failures [4], are all stateful systems which will present interesting modelling challenges as well as provide us with more performance and usability data. Additionally, it will be interesting to explore what kind of properties we can check. Linear Temporal Logic (LTL) and Computation Tree Logic (CTL) are used extensively in model checking [23,24], and there is recent work by O'Connor and Wickström on combining LTL with PBT for use in testing Graphical User Interfaces (GUIs) [35]. As such, it will be interesting to see how big the overlap might be between our approach and what model checkers can express and verify.

All the code used in this paper is publicly available at:
https://github.com/CodingCellist/tyde-24-code

**Footnote:**
¹ x86_64 Intel Core i7-8750H @ 2.20GHz, boosting to ~4.08GHz, with 32GiB of SODIMM DDR4 RAM @ 2667MT/s

---

### النسخة العربية

تصل أنواع، وانتقالات الحالة، وتطبيق Traceable لـ ARQ إلى حوالي 30 سطراً من الشفرة، بالمقارنة مع ما يقرب من 80 سطراً كان علينا كتابتها فقط لدعم الصراف الآلي في القسم 3.3.2. هذه أسطر شفرة صعبة — نسج الحالة في الأنواع والتأكد من أن توليد الأثر يتبع التسلسل الصحيح — لذا فإن وجودها في شكل معمم يوفر علينا خطر إعادة تطبيقها بشكل غير صحيح، بالإضافة إلى توفير الكثير من العمل المضجر.

يمكن القول بأن معظم لغات المجال المحددة بسيطة بما يكفي للتفكير فيها يدوياً. ومع ذلك، كما رأينا، فإن لغات المجال المحددة التي تبدو تافهة مثل تلك الخاصة بالصراف الآلي سهلة الخطأ ويمكن أن يظل هذا الخطأ غير مكتشف لسنوات. بالنسبة لحالات الاستخدام الأكثر تعقيداً مثل بروتوكولات الشبكة، أو إدارة الموارد، أو التزامن، حيث يتم الاستفادة من نظام أنواع المضيف لتوفير ضمانات معينة مرغوبة للمجال المستهدف [7,13,14,16,25,28]، فإن خطر قيام لغة المجال المحددة بإدخال تناقضات خفية وسلوك غير مقصود عن طريق الخطأ، من المحتمل أن يكون أعلى بكثير، مما يضعف هدف القضاء على أخطاء معينة باستخدام لغة مضيف أكثر صرامة. جنباً إلى جنب مع انتشار الأنظمة ذات الحالات، نعتقد لذلك أن نهجنا يستحق العناء ونعتزم نمذجة واختبار بروتوكولات أكثر تقدماً في المستقبل.

في جميع أنحاء الورقة، كانت جميع الآثار لها أرقام سحرية على ما يبدو كحدودها. تم تحديد الأرقام جزئياً بناءً على التفكير: من الممكن الحصول على تقدير جيد للعمق المطلوب بأخذ عدد الانتقالات في موناد الحالة المفهرسة، والقرار بشأن حد أعلى لوقت يجب أن يكون فيه النظام في الحالة المطلوبة، وضرب هذا في عدد الانتقالات (أو عدد الحالات) في النظام. في حالة فشل الخصائص، يمكن فحصها إما للكشف عن حالة خطأ صالحة، أو ربما خطأ في المولدات، أو إيجابية خاطئة ناتجة عن النموذج (كما حدث في [32]). بالنسبة للإيجابيات الحقيقية، يمكن مضاعفة العمق حتى تمر، وعند هذه النقطة يمكن استخدام البحث الثنائي للعثور على أصغر حد صالح. نعتقد أن هذا جزء من بناء الثقة: يمكن للمبرمجين زيادة الحد حتى يثقوا في نماذجهم المكتوبة، أو يمكنهم أن يقرروا أن الحد الحالي كافٍ. في تجربتنا، هذا ليس عائقاً، حيث تفشل الخصائص بسرعة، وبالتالي تجد الحد الأعلى الأولي بسرعة.

يستغرق الاختبار القائم على الخصائص على مستوى الأنواع لنموذج ARQ حوالي 3.5 ثانية على جهاز كمبيوتر محمول حديث بشكل معقول¹. على الرغم من أن هذا قد يبدو بطيئاً، إلا أنه يجدر التذكير بأن مدقق الأنواع يقوم بالكثير من العمل. إنه يحل قيود الواجهة، ويوحد القيم، ويشغل PRNG، ويقوم بفحوصات المساواة للأنواع غير التافهة 100 مرة على الأقل. مدقق أنواع Idris2 هو حالياً العائق الرئيسي لنهجنا ويقدم العديد من أسئلة البحث المثيرة للاهتمام من حيث كيفية تسريع عملية التفصيل، ومتى يتم توسيع ودمج دوال وأنواع بيانات معينة، وكمية المعلومات التي يجب الاحتفاظ بها في مدقق الأنواع والمفصّل.

في المستقبل، نخطط لفحص وتطبيق أنظمة متقدمة بشكل متزايد. ARQ مع النافذة المنزلقة [33] سيكون امتداداً جيداً لمثال ARQ، حيث يحسن من إنتاجية البروتوكول ويقدم بعض التحديات الجديدة لدالة الحالة: كيف ننمذج حركات نافذة الحزم بشكل أفضل؟ آلات الالتقاط والوضع المستخدمة للوضع التلقائي للمكونات المثبتة على السطح [1]، وأنظمة الملفات [18]، والبروتوكولات مع أعطال التوقف الفجائي [4]، كلها أنظمة ذات حالات ستقدم تحديات نمذجة مثيرة للاهتمام بالإضافة إلى تزويدنا ببيانات أكثر عن الأداء وسهولة الاستخدام. بالإضافة إلى ذلك، سيكون من المثير للاهتمام استكشاف نوع الخصائص التي يمكننا التحقق منها. يتم استخدام منطق الزمن الخطي (LTL) ومنطق شجرة الحساب (CTL) على نطاق واسع في فحص النماذج [23,24]، وهناك عمل حديث من O'Connor و Wickström حول الجمع بين LTL و PBT للاستخدام في اختبار واجهات المستخدم الرسومية (GUIs) [35]. على هذا النحو، سيكون من المثير للاهتمام رؤية مدى التداخل الكبير بين نهجنا وما يمكن لمدققي النماذج التعبير عنه والتحقق منه.

جميع الشفرة المستخدمة في هذه الورقة متاحة للعامة على:
https://github.com/CodingCellist/tyde-24-code

**حاشية:**
¹ x86_64 Intel Core i7-8750H @ 2.20GHz، مع تعزيز إلى ~4.08GHz، مع 32GiB من SODIMM DDR4 RAM @ 2667MT/s

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Domain Specific Language (DSL) - لغة مجال محددة
  - Linear Temporal Logic (LTL) - منطق الزمن الخطي
  - Computation Tree Logic (CTL) - منطق شجرة الحساب
  - Graphical User Interface (GUI) - واجهة المستخدم الرسومية
  - Sliding Window - نافذة منزلقة
  - Binary search - بحث ثنائي
  - Elaboration - تفصيل

- **Equations:** None
- **Code blocks:** 1 URL reference
- **Citations:** [1,4,7,13,14,16,18,23,24,25,28,32,33,35]
- **Special handling:** Performance metrics, future work discussion

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.85
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.85
