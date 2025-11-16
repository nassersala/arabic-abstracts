# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** safety-critical systems, formal model, software development life-cycle, formal methods, property-based testing, temporal, verification, testing

---

### English Version

Safety-critical systems, e.g., in the automotive domain (Kuhnel and Spichkova, 2007), become more and more software-intensive with every year. While specifying such systems, a precise formal model, i.e., a mathematical model at some level of abstraction, might be essential to eliminate ambiguity and to detect possible errors early in the software development life-cycle (SDL). Also, in most cases the system properties have to be analysed in relation to the time, thus, verification/testing of the temporal aspects is crucial.

To achieve the integration of formal models into SDL, the development process should be human-oriented. Thus, aspects of human factors engineering should be taken into account, cf. (Spichkova et al., 2015). Moreover, using Formal Methods (FMs) can be beneficial while developing not only safety-critical systems, but also web services, cf. (Newcombe et al., 2015). FMs were successfully applied to design and analyse systems since many years, cf. (Bowen and Hinchey, 1995; Yu et al., 1999). Despite all the advantages of FMs, software engineers are not keen to include them into the software development process. This problem was discussed 15-20 years ago, e.g., in (Hinchey, 2003). This problem is still unsolved now. Lack of readability and usability is one of the reasons for very limited use of FMs in industrial projects (Zamansky et al., 2016). However, in some cases even simply implementable improvements can make an FM more readable and understandable, cf. (Spichkova, 2012).

In many cases, FMs require huge amount of training, as they use a very specific syntax that is unreadable for novices. In general, testing approaches are perceived by practitioners as more appropriate for a real-life development process. However, they are usually comfortable with concepts from property-based testing (PBT), which require a little bit of mathematical thinking. PBT approach allows to use randomly generated test cases based on properties to test systems against their specifications.

To led programmers in formulating and testing properties of programs, Claessen and Hughes introduced a tool named QuickCheck that is focusing on Haskell programming language. They demonstrated that QuickCheck allowed them to discover hundreds of bugs, e.g., DropBox file sharing service (Claessen and Hughes, 2011; Hughes, 2010). In its first edition, QuickCheck was proposed as a testing framework for testing only functional programs. However, recent development in the area of PBT incorporates the statefulness of systems. That provides functionality for the testing of state-ful systems as well as for testing programs written in imperative languages, e.g., C (Gerdes et al., 2015; Hughes, 2010).

We propose to apply PBT on top of temporal formal models. This might help software engineers to understand temporal formal models (which describe the state of a system in every discrete time point), as the FM constructs will be expressed in terms of system code. This might contribute to the understandability of FMs indirectly, and allow software engineers to make use of the advantages of FMs. To achieve this goal, we suggest to translate the core time-based constructs of an FM to the BeSpaceD extension of the Scala programming language, specified in (Blech and Schmidt, 2014). This allows us to have an executable Scala code that corresponds to the formal model, as well as to perform PBT of the models functionality. To model temporal properties of the systems, in the current work we focus on two formal languages, Temporal logic of actions (TLA+) and FOCUSST. TLA+ combines temporal logic with a logic of actions, and is used to describe behaviours of concurrent systems, cf. (Lamport, 1994; Lamport, 1993). FOCUSST is a formal language providing concise but easily understandable specifications that is focused on timing and spatial aspects of the system behaviour (Spichkova et al., 2014; Spichkova, 2007).

To implement the proposed ideas, we selected Scala programming language, as on the PBT level this allows us to apply an extension to ScalaCheck library. Early ideas of this approach was presented at Software Technologies: Applications and Foundations Conference, cf. (Alzahrani et al., 2016). In this paper we go further and discuss the developed framework and how it can be applies to TLA+ and FOCUSST. This approach is based on a completed Minor Master Thesis of the first author.

---

### النسخة العربية

تصبح الأنظمة الحرجة للسلامة، على سبيل المثال، في مجال السيارات (Kuhnel and Spichkova, 2007)، أكثر كثافة من حيث البرمجيات مع كل عام. عند تحديد مواصفات مثل هذه الأنظمة، قد يكون النموذج الرسمي الدقيق، أي نموذج رياضي عند مستوى معين من التجريد، ضرورياً للقضاء على الغموض ولاكتشاف الأخطاء المحتملة في وقت مبكر من دورة حياة تطوير البرمجيات (SDL). أيضاً، في معظم الحالات يجب تحليل خصائص النظام فيما يتعلق بالوقت، وبالتالي فإن التحقق/الاختبار من الجوانب الزمنية أمر حاسم.

لتحقيق دمج النماذج الرسمية في دورة حياة تطوير البرمجيات، يجب أن تكون عملية التطوير موجهة نحو الإنسان. وبالتالي، ينبغي أخذ جوانب هندسة العوامل البشرية في الاعتبار، راجع (Spichkova et al., 2015). علاوة على ذلك، يمكن أن يكون استخدام الأساليب الرسمية (FMs) مفيداً أثناء تطوير ليس فقط الأنظمة الحرجة للسلامة، ولكن أيضاً خدمات الويب، راجع (Newcombe et al., 2015). تم تطبيق الأساليب الرسمية بنجاح لتصميم وتحليل الأنظمة منذ سنوات عديدة، راجع (Bowen and Hinchey, 1995; Yu et al., 1999). على الرغم من جميع مزايا الأساليب الرسمية، فإن مهندسي البرمجيات ليسوا حريصين على إدراجها في عملية تطوير البرمجيات. تمت مناقشة هذه المشكلة قبل 15-20 عاماً، على سبيل المثال، في (Hinchey, 2003). هذه المشكلة لا تزال غير محلولة الآن. يعد نقص القابلية للقراءة وسهولة الاستخدام أحد أسباب الاستخدام المحدود جداً للأساليب الرسمية في المشاريع الصناعية (Zamansky et al., 2016). ومع ذلك، في بعض الحالات، يمكن حتى للتحسينات البسيطة القابلة للتنفيذ أن تجعل الأسلوب الرسمي أكثر قابلية للقراءة والفهم، راجع (Spichkova, 2012).

في كثير من الحالات، تتطلب الأساليب الرسمية قدراً هائلاً من التدريب، حيث إنها تستخدم بنية نحوية محددة جداً غير قابلة للقراءة بالنسبة للمبتدئين. بشكل عام، يُنظر إلى نهج الاختبار من قبل الممارسين على أنه أكثر ملاءمة لعملية التطوير الواقعية. ومع ذلك، فهم عادة مرتاحون لمفاهيم الاختبار القائم على الخصائص (PBT)، والتي تتطلب القليل من التفكير الرياضي. يسمح نهج الاختبار القائم على الخصائص باستخدام حالات اختبار مُولّدة عشوائياً استناداً إلى الخصائص لاختبار الأنظمة مقابل مواصفاتها.

لقيادة المبرمجين في صياغة واختبار خصائص البرامج، قدم Claessen و Hughes أداة تسمى QuickCheck التي تركز على لغة البرمجة Haskell. لقد أظهروا أن QuickCheck سمح لهم باكتشاف مئات الأخطاء، على سبيل المثال، خدمة مشاركة الملفات DropBox (Claessen and Hughes, 2011; Hughes, 2010). في طبعته الأولى، تم اقتراح QuickCheck كإطار عمل اختبار لاختبار البرامج الوظيفية فقط. ومع ذلك، فإن التطوير الأخير في مجال الاختبار القائم على الخصائص يدمج حالية الأنظمة. وهذا يوفر وظيفة لاختبار الأنظمة الحالية وكذلك لاختبار البرامج المكتوبة بلغات حتمية، على سبيل المثال، C (Gerdes et al., 2015; Hughes, 2010).

نقترح تطبيق الاختبار القائم على الخصائص على النماذج الرسمية الزمنية. قد يساعد هذا مهندسي البرمجيات على فهم النماذج الرسمية الزمنية (التي تصف حالة النظام في كل نقطة زمنية منفصلة)، حيث سيتم التعبير عن بنى الأسلوب الرسمي من حيث شفرة النظام. قد يساهم هذا في قابلية الفهم للأساليب الرسمية بشكل غير مباشر، ويسمح لمهندسي البرمجيات بالاستفادة من مزايا الأساليب الرسمية. لتحقيق هذا الهدف، نقترح ترجمة البنى الأساسية القائمة على الوقت لأسلوب رسمي إلى امتداد BeSpaceD للغة البرمجة Scala، المحددة في (Blech and Schmidt, 2014). هذا يسمح لنا بالحصول على شفرة Scala قابلة للتنفيذ تتوافق مع النموذج الرسمي، وكذلك لإجراء الاختبار القائم على الخصائص لوظيفة النموذج. لنمذجة الخصائص الزمنية للأنظمة، نركز في العمل الحالي على لغتين رسميتين، منطق الأفعال الزمني (TLA+) و FOCUSST. يجمع TLA+ بين المنطق الزمني ومنطق الأفعال، ويُستخدم لوصف سلوكيات الأنظمة المتزامنة، راجع (Lamport, 1994; Lamport, 1993). FOCUSST هي لغة رسمية توفر مواصفات موجزة ولكنها سهلة الفهم تركز على الجوانب الزمنية والمكانية لسلوك النظام (Spichkova et al., 2014; Spichkova, 2007).

لتنفيذ الأفكار المقترحة، اخترنا لغة البرمجة Scala، حيث على مستوى الاختبار القائم على الخصائص يسمح لنا هذا بتطبيق امتداد لمكتبة ScalaCheck. تم تقديم الأفكار المبكرة لهذا النهج في مؤتمر تقنيات البرمجيات: التطبيقات والأسس، راجع (Alzahrani et al., 2016). في هذه الورقة نذهب أبعد من ذلك ونناقش إطار العمل المطور وكيف يمكن تطبيقه على TLA+ و FOCUSST. يعتمد هذا النهج على أطروحة ماجستير ثانوية مكتملة للمؤلف الأول.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** Safety-critical systems, formal models, SDL (Software Development Life-cycle), Formal Methods (FMs), QuickCheck, TLA+, FOCUSST, BeSpaceD, Scala, ScalaCheck
- **Equations:** 0
- **Citations:** 15 references cited
- **Special handling:**
  - Technical acronyms kept: SDL, FMs, PBT
  - Tool names kept as-is: QuickCheck, ScalaCheck, DropBox
  - Language names kept as-is: TLA+, FOCUSST, BeSpaceD, Scala, Haskell, C
  - Author names in citations kept in English

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
