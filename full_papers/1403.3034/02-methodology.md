# Section 2: A Methodology for Encapsulating Formal Methods within DSLs
## القسم 2: منهجية لتغليف الأساليب الرسمية ضمن اللغات الخاصة بالمجال

**Section:** methodology
**Translation Quality:** 0.87
**Glossary Terms Used:** domain specific languages (لغات خاصة بالمجال), formal methods (الأساليب الرسمية), UML (يو إم إل), verification (التحقق), modelling (النمذجة), scalability (قابلية التوسع), algebraic specification (المواصفات الجبرية), faithful modelling (النمذجة الأمينة), accessibility (إمكانية الوصول)

---

### English Version

**Introduction**

We begin by introducing the topic of domain specific languages (DSLs), paying particular attention to the common industrial representation used to formulate such languages in terms of UML class diagrams accompanied by a narrative. For such industrial DSLs, we then develop our methodology in a detailed step-by-step manner.

**2.1 Background: Domain Specific Languages (DSLs)**

Throughout all areas of science, one can find approaches that are general in principle or specific to the task at hand. A general approach gives a solution to several problems of a similar manner. Whereas a specific approach often solves problems in a more comprehensive manner, but can be applied to significantly less problems. In computer science, the differences are exemplified by general purpose languages (GPLs) and domain specific languages (DSLs) respectively.

Domain specific languages (DSLs) are languages that have been designed and tailored for a specific application domain. DSLs aim to abstract away technical details of computer science from the user, allowing them to create programs or specifications without having to be an expert programmer or specifier. Examples of DSLs include the well known Backus Naur Form or the commonly used HTML markup language. Considering HTML, it is designed explicitly with webpage creation in mind. It has specific features such as *elements*, *tags* and *attributes* that allow the specification of structure within a web page. The advantages of having these domain specific features are apparent as HTML has become the de facto standard for webpage creation thanks to its expressiveness and to its ease of application. When we speak of expressiveness in the context of DSLs, we refer to the question of how easy it is for a user to describe the objects they desire. Expressiveness can often be explored by considering how intuitive various language constructs are. This idea forms a main theme throughout this work.

**DSLs Formulated using UML Class Diagrams and Narrative**

UML Class Diagrams are industrially accepted for modelling a variety of systems across numerous domains. Often they are used to describe all elements and relationships occurring within a domain. As such, a UML Class Diagram can be thought of as describing a DSL. Many tools and frameworks actually use UML class diagrams as a starting point for the description of a DSL. A typical example of such an endeavour is given by the Data Model of our research partner Invensys Rail. It aims to describe all elements within the railway domain.

The UML diagram in Figure 1 captures Bjørner's railway DSL that we will use as a running example. It illustrates many of the features of class diagrams:

- **Classes**, represented by a box, e.g. *Net*, *Unit*, *Station* etc. These represent concepts from the railway domain.
- **Properties**, listed inside a class, e.g. *id : UID* in the class *Net* expresses that all *Net*s have an identifier of type *UID*.
- **Generalisations**, represented by an unfilled arrow head, e.g. *Point* and *Linear* are generalisations of *Unit*.
- **Associations**, represented by a line connecting two classes, e.g. the *has* link between *Unit* and *Connector*. These can have direction, and also multiplicities associated with them. The multiplicities on the *has* association between *Unit* and *Connector* can be read as: "One *Unit* has two or more connectors".
- **Compositions**, represented by a filled diamond, e.g. the *hasLine* composition for *Net* and *Line*, tell us that one class "is made up of" another class. In a similar fashion to associations, compositions can also have multiplicities.
- **Operations** are also represented inside a class, e.g. the *isOpen* operation of type *Boolean* inside the *Route* class.

As UML class diagrams only capture static system aspects, we make the realistic assumption that the class diagram is accompanied with some narrative. Obviously, such a narrative can give explanations on the static structure of the class diagram. Its main purpose, however, is to describe the dynamic system aspects. For many domains such a narrative is present in the form of standard literature. An example of this is Kerr's narrative for the railway domain. Kerr describes, for instance, how a signal changes using the following narrative: *"a repeater signal shows yellow if its parent signal is showing red"*. Further examples of narrative are N1 and N2 in Section 3.

UML class diagrams and narratives can be linked via the stereotype **dynamic**. This annotation indicates that the labelled class diagram element is related to the dynamic nature of the system. The manner in which change happens is described in the narrative. In Figure 1, e.g., the relation *stateAt* is marked to be of dynamic nature, i.e., to change over time. Section 3 provides the narrative how this state change happens.

**2.2 Contribution: The Design Steps of our Methodology**

To achieve a faithful, scalable and accessible modelling and verification procedure, we present a new methodology that encapsulates formal methods within a DSL. This results in a tool based framework for verification.

Considering Figure 2, the encapsulation process we propose is undertaken by a team comprising of computer scientists working in close collaboration with experts from the domain. Here, the close working relationship ensures the resulting domain modelling is faithful. The following steps are involved in the process:

**M1: Formalising (Industrial) DSLs**

The starting point for our methodology is an informal domain description in the form of UML Class Diagrams and accompanying narrative. From such UML class diagrams, names, relations, and multiplicity constraints can be automatically extracted and translated into a formal specification in Modal CASL. We suggest and support a particular automatic translation (see Section 4.2). Next, domain experts and computer scientists extend the resulting formal Modal CASL specification with a modelling of the narrative that captures dynamics. This is possible as Modal CASL allows the description of state changes in terms of modal operators. Here, we also encode proof goals for verification. Then, for the sake of better proof support, we apply an existing automatic translation from Modal CASL to CASL. Overall, starting from an existing DSL and involving domain experts ensures a faithful formalisation of the selected domain concepts.

**M2: DSL Analysis for Verification Support**

The result of Step M1, the formalisation of the DSL, is a loose CASL specification. The logical closure of this specification, i.e., all theorems that one can prove from this CASL specification, is what we call the implicitly encoded "domain knowledge" of the DSL. We make (part of) this domain knowledge explicit in the form of lemmas that allow one to refactor any proof goals into equivalent ones that are expressed on the right level of granularity. Naturally, there cannot be a universal solution to finding such domain specific lemmas. However, in our experience, for all DSLs we have considered, such lemmas have existed, follow from knowledge of the domain experts, and allow refactoring. We discuss such lemmas in Section 5 and show that these lemmas allow for scalable verification based on ideas that are often inherent to the domain. Overall, this step enables scalability of the verification approach.

**M3: Graphical Tool Support**

DSLs are often accompanied by a development framework. For this we make use of the *Graphical Modelling Framework*, GMF. GMF provides the infrastructure to create, from a UML class diagram, a Java based graphical editor. Using GMF, domain experts and computer scientists create such a graphical tooling environment for the DSL. This allows for native graphical representations of domain elements. Such an editor is open (via Epsilon) to extension with model transformations. Such transformations allow for the graphical models produced by the editor to be translated to CASL specifications. These specifications can be enriched with the domain knowledge developed in Step M2. We illustrate this approach in Section 6, giving details of the OnTrack Toolset for the railway domain. The result of this step is a tool for generation of formal models that is readily usable by engineers from the domain under consideration.

**Addressing the Issues**

Overall, our methodology addresses the issues we started with: faithful modelling is achieved thanks to starting with an informal description and forming a formal specification in a close working relationship between the domain experts and computer scientists; scalability of the verification procedure is achieved thanks to the property supporting domain specific lemmas; accessibility to modelling and verification of systems is achieved thanks to graphical tooling incorporating domain specific concepts and constructs.

**2.3 Contribution: The Resulting Verification Process**

The result of applying our methodology is a toolset accommodating the verification process illustrated in Figure 3. This process is undertaken purely by the engineers in the domain. It follows three main steps:

**V1: Model Development Based on the Informal DSL**

The first (optional) step within industry is to outline or specify a design informally. This step should be undertaken using the vocabulary outlined within the informal DSL.

**V2: Graphical Modelling**

Next, the domain engineer can encode their design using the graphical editor. Once encoded, the engineer can automatically produce formal specifications ready for verification. As the graphical editor contains constructs that are from the informal DSL, training and learning costs are minimal.

**V3: Verification**

Finally, the formal specifications can be verified using (for CASL) the Heterogeneous Toolset, HETS. Due to the domain specific lemmas developed during the design process, verification is automated and "Push Button".

---

### النسخة العربية

**مقدمة**

نبدأ بتقديم موضوع اللغات الخاصة بالمجال (DSLs)، مع إيلاء اهتمام خاص للتمثيل الصناعي الشائع المستخدم لصياغة هذه اللغات من حيث مخططات فئات UML مصحوبة بسرد. بالنسبة لهذه اللغات الخاصة بالمجال الصناعية، نطور بعد ذلك منهجيتنا بطريقة تفصيلية خطوة بخطوة.

**2.1 خلفية: اللغات الخاصة بالمجال (DSLs)**

في جميع مجالات العلوم، يمكن للمرء أن يجد نُهجًا عامة من حيث المبدأ أو خاصة بالمهمة المطروحة. يقدم النهج العام حلاً لعدة مشاكل بطريقة مماثلة. بينما غالبًا ما يحل النهج الخاص المشاكل بطريقة أكثر شمولاً، ولكن يمكن تطبيقه على عدد أقل بكثير من المشاكل. في علوم الحاسوب، تتجلى الاختلافات من خلال اللغات ذات الأغراض العامة (GPLs) واللغات الخاصة بالمجال (DSLs) على التوالي.

اللغات الخاصة بالمجال (DSLs) هي لغات تم تصميمها وتخصيصها لمجال تطبيق محدد. تهدف اللغات الخاصة بالمجال إلى تجريد التفاصيل التقنية لعلوم الحاسوب عن المستخدم، مما يسمح له بإنشاء برامج أو مواصفات دون الحاجة إلى أن يكون مبرمجًا أو محددًا خبيرًا. تشمل أمثلة اللغات الخاصة بالمجال نموذج باكوس-ناور (Backus Naur Form) المعروف أو لغة ترميز HTML الشائعة الاستخدام. بالنظر إلى HTML، فهي مصممة صراحةً مع وضع إنشاء صفحات الويب في الاعتبار. لديها ميزات محددة مثل *العناصر*، و*الوسوم* و*السمات* التي تسمح بتحديد البنية داخل صفحة الويب. مزايا امتلاك هذه الميزات الخاصة بالمجال واضحة حيث أصبحت HTML المعيار الفعلي لإنشاء صفحات الويب بفضل تعبيريتها وسهولة تطبيقها. عندما نتحدث عن التعبيرية في سياق اللغات الخاصة بالمجال، فإننا نشير إلى سؤال مدى سهولة وصف المستخدم للكائنات التي يرغب فيها. يمكن غالبًا استكشاف التعبيرية من خلال النظر في مدى سهولة استخدام بنيات اللغة المختلفة. تشكل هذه الفكرة موضوعًا رئيسيًا في جميع أنحاء هذا العمل.

**اللغات الخاصة بالمجال المصاغة باستخدام مخططات فئات UML والسرد**

مخططات فئات UML مقبولة صناعيًا لنمذجة مجموعة متنوعة من الأنظمة عبر العديد من المجالات. غالبًا ما تُستخدم لوصف جميع العناصر والعلاقات التي تحدث داخل المجال. على هذا النحو، يمكن اعتبار مخطط فئات UML وصفًا للغة خاصة بالمجال. تستخدم العديد من الأدوات والأطر في الواقع مخططات فئات UML كنقطة انطلاق لوصف لغة خاصة بالمجال. مثال نموذجي على مثل هذا الجهد هو نموذج البيانات لشريك البحث لدينا Invensys Rail. يهدف إلى وصف جميع العناصر في مجال السكك الحديدية.

يوضح مخطط UML في الشكل 1 لغة السكك الحديدية الخاصة بالمجال لـ Bjørner والتي سنستخدمها كمثال تشغيلي. يوضح العديد من ميزات مخططات الفئات:

- **الفئات**، ممثلة بمربع، مثل *Net*، *Unit*، *Station* إلخ. تمثل هذه المفاهيم من مجال السكك الحديدية.
- **الخصائص**، المدرجة داخل فئة، مثل *id : UID* في الفئة *Net* تعبر عن أن جميع *Net*s لديها معرف من نوع *UID*.
- **التعميمات**، ممثلة برأس سهم غير مملوء، مثل *Point* و *Linear* هما تعميمات لـ *Unit*.
- **الارتباطات**، ممثلة بخط يربط بين فئتين، مثل رابط *has* بين *Unit* و *Connector*. يمكن أن يكون لها اتجاه، وأيضًا تعددية مرتبطة بها. يمكن قراءة التعددية على ارتباط *has* بين *Unit* و *Connector* على النحو التالي: "وحدة واحدة *Unit* لها موصلان أو أكثر".
- **التركيبات**، ممثلة بماسة مملوءة، مثل تركيب *hasLine* لـ *Net* و *Line*، تخبرنا أن فئة واحدة "مكونة من" فئة أخرى. بطريقة مماثلة للارتباطات، يمكن أن يكون للتركيبات أيضًا تعددية.
- **العمليات** ممثلة أيضًا داخل فئة، مثل عملية *isOpen* من نوع *Boolean* داخل فئة *Route*.

نظرًا لأن مخططات فئات UML تلتقط فقط جوانب النظام الثابتة، فإننا نفترض افتراضًا واقعيًا أن مخطط الفئات مصحوب ببعض السرد. من الواضح أن مثل هذا السرد يمكن أن يعطي تفسيرات حول البنية الثابتة لمخطط الفئات. ومع ذلك، فإن هدفه الرئيسي هو وصف جوانب النظام الديناميكية. بالنسبة للعديد من المجالات، يكون هذا السرد موجودًا في شكل أدبيات قياسية. مثال على ذلك هو سرد Kerr لمجال السكك الحديدية. يصف Kerr، على سبيل المثال، كيف تتغير الإشارة باستخدام السرد التالي: *"إشارة المكرر تظهر باللون الأصفر إذا كانت إشارتها الأم تظهر باللون الأحمر"*. أمثلة أخرى من السرد هي N1 و N2 في القسم 3.

يمكن ربط مخططات فئات UML والسردات عبر النمط **ديناميكي**. يشير هذا التعليق التوضيحي إلى أن عنصر مخطط الفئات المُعنون مرتبط بالطبيعة الديناميكية للنظام. يتم وصف الطريقة التي يحدث بها التغيير في السرد. في الشكل 1، على سبيل المثال، العلاقة *stateAt* موسومة بأنها ذات طبيعة ديناميكية، أي تتغير بمرور الوقت. يقدم القسم 3 السرد حول كيفية حدوث تغيير الحالة هذا.

**2.2 المساهمة: خطوات التصميم لمنهجيتنا**

لتحقيق إجراء نمذجة وتحقق أمين وقابل للتوسع ويمكن الوصول إليه، نقدم منهجية جديدة تغلف الأساليب الرسمية ضمن لغة خاصة بالمجال. ينتج عن ذلك إطار عمل قائم على الأدوات للتحقق.

بالنظر إلى الشكل 2، يتم تنفيذ عملية التغليف التي نقترحها من قبل فريق يتألف من علماء الحاسوب يعملون بتعاون وثيق مع خبراء من المجال. هنا، تضمن علاقة العمل الوثيقة أن تكون نمذجة المجال الناتجة أمينة. الخطوات التالية متضمنة في العملية:

**M1: صياغة اللغات الخاصة بالمجال (الصناعية) رسميًا**

نقطة البداية لمنهجيتنا هي وصف المجال غير الرسمي في شكل مخططات فئات UML وسرد مصاحب. من مخططات فئات UML هذه، يمكن استخراج الأسماء والعلاقات وقيود التعددية تلقائيًا وترجمتها إلى مواصفات رسمية في Modal CASL. نقترح وندعم ترجمة تلقائية معينة (انظر القسم 4.2). بعد ذلك، يوسع خبراء المجال وعلماء الحاسوب مواصفات Modal CASL الرسمية الناتجة بنمذجة للسرد الذي يلتقط الديناميكيات. هذا ممكن لأن Modal CASL يسمح بوصف تغييرات الحالة من حيث العوامل الموديولية. هنا، نقوم أيضًا بتشفير أهداف الإثبات للتحقق. ثم، من أجل دعم أفضل للإثبات، نطبق ترجمة تلقائية موجودة من Modal CASL إلى CASL. بشكل عام، فإن البدء من لغة خاصة بالمجال موجودة وإشراك خبراء المجال يضمن صياغة رسمية أمينة لمفاهيم المجال المحددة.

**M2: تحليل اللغة الخاصة بالمجال لدعم التحقق**

نتيجة الخطوة M1، صياغة اللغة الخاصة بالمجال رسميًا، هي مواصفات CASL فضفاضة. الإغلاق المنطقي لهذه المواصفات، أي جميع النظريات التي يمكن للمرء إثباتها من مواصفات CASL هذه، هو ما نسميه "معرفة المجال" المشفرة ضمنيًا للغة الخاصة بالمجال. نجعل (جزءًا من) معرفة المجال هذه صريحة في شكل لمّات تسمح للمرء بإعادة صياغة أي أهداف إثبات إلى أهداف مكافئة يتم التعبير عنها على المستوى الصحيح من التفصيل. بطبيعة الحال، لا يمكن أن يكون هناك حل عالمي للعثور على مثل هذه اللمّات الخاصة بالمجال. ومع ذلك، في تجربتنا، بالنسبة لجميع اللغات الخاصة بالمجال التي نظرنا فيها، وُجدت مثل هذه اللمّات، وتتبع من معرفة خبراء المجال، وتسمح بإعادة الصياغة. نناقش مثل هذه اللمّات في القسم 5 ونظهر أن هذه اللمّات تسمح بالتحقق القابل للتوسع بناءً على أفكار غالبًا ما تكون كامنة في المجال. بشكل عام، تمكن هذه الخطوة من قابلية توسع نهج التحقق.

**M3: دعم الأدوات الرسومية**

غالبًا ما تكون اللغات الخاصة بالمجال مصحوبة بإطار تطوير. لهذا نستخدم *إطار النمذجة الرسومية*، GMF. يوفر GMF البنية التحتية لإنشاء، من مخطط فئات UML، محرر رسومي قائم على Java. باستخدام GMF، ينشئ خبراء المجال وعلماء الحاسوب مثل هذه البيئة الأدواتية الرسومية للغة الخاصة بالمجال. هذا يسمح بتمثيلات رسومية أصلية لعناصر المجال. مثل هذا المحرر مفتوح (عبر Epsilon) للتوسع مع تحويلات النماذج. تسمح مثل هذه التحويلات بترجمة النماذج الرسومية التي ينتجها المحرر إلى مواصفات CASL. يمكن إثراء هذه المواصفات بمعرفة المجال المطورة في الخطوة M2. نوضح هذا النهج في القسم 6، مع إعطاء تفاصيل مجموعة أدوات OnTrack لمجال السكك الحديدية. نتيجة هذه الخطوة هي أداة لتوليد النماذج الرسمية التي يمكن للمهندسين من المجال قيد النظر استخدامها بسهولة.

**معالجة القضايا**

بشكل عام، تعالج منهجيتنا القضايا التي بدأنا بها: يتم تحقيق النمذجة الأمينة بفضل البدء بوصف غير رسمي وتشكيل مواصفات رسمية في علاقة عمل وثيقة بين خبراء المجال وعلماء الحاسوب؛ يتم تحقيق قابلية توسع إجراء التحقق بفضل اللمّات الخاصة بالمجال الداعمة للخصائص؛ يتم تحقيق إمكانية الوصول إلى نمذجة وتحقق الأنظمة بفضل الأدوات الرسومية التي تدمج المفاهيم والبنيات الخاصة بالمجال.

**2.3 المساهمة: عملية التحقق الناتجة**

نتيجة تطبيق منهجيتنا هي مجموعة أدوات تستوعب عملية التحقق الموضحة في الشكل 3. يتم تنفيذ هذه العملية بشكل حصري من قبل المهندسين في المجال. تتبع ثلاث خطوات رئيسية:

**V1: تطوير النموذج بناءً على اللغة الخاصة بالمجال غير الرسمية**

الخطوة الأولى (الاختيارية) في الصناعة هي تحديد أو تحديد تصميم بشكل غير رسمي. يجب القيام بهذه الخطوة باستخدام المفردات المحددة في اللغة الخاصة بالمجال غير الرسمية.

**V2: النمذجة الرسومية**

بعد ذلك، يمكن لمهندس المجال تشفير تصميمه باستخدام المحرر الرسومي. بمجرد التشفير، يمكن للمهندس إنتاج مواصفات رسمية تلقائيًا جاهزة للتحقق. نظرًا لأن المحرر الرسومي يحتوي على بنيات من اللغة الخاصة بالمجال غير الرسمية، فإن تكاليف التدريب والتعلم ضئيلة.

**V3: التحقق**

أخيرًا، يمكن التحقق من المواصفات الرسمية باستخدام (لـ CASL) مجموعة الأدوات غير المتجانسة، HETS. بسبب اللمّات الخاصة بالمجال المطورة أثناء عملية التصميم، فإن التحقق آلي و"بضغطة زر".

---

### Translation Notes

- **Figures referenced:** Figure 1 (Bjørner's DSL UML diagram), Figure 2 (methodology process), Figure 3 (verification process)
- **Key terms introduced:**
  - Domain Specific Languages (اللغات الخاصة بالمجال)
  - General Purpose Languages (اللغات ذات الأغراض العامة)
  - UML Class Diagrams (مخططات فئات UML)
  - Modal CASL (Modal CASL)
  - CASL (CASL)
  - GMF (إطار النمذجة الرسومية)
  - HETS (مجموعة الأدوات غير المتجانسة)
  - Domain knowledge (معرفة المجال)
  - Lemmas (لمّات)
- **Technical concepts:** Class diagrams components (classes, properties, generalisations, associations, compositions, operations), narrative, verification process
- **Special handling:** Three-step methodology (M1, M2, M3) and three-step verification process (V1, V2, V3) clearly delineated

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
