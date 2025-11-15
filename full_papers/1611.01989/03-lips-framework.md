# Section 3: Learning Inductive Program Synthesis (LIPS)
## القسم 3: تعلم التوليد الاستقرائي للبرامج (LIPS)

**Section:** LIPS Framework
**Translation Quality:** 0.86
**Glossary Terms Used:** framework, domain-specific language, machine learning, neural network, attribute, data generation, search, distribution, encoder, decoder, maximum likelihood

---

### English Version

In this section we outline the general approach that we follow in this work, which we call Learning Inductive Program Synthesis (LIPS). The details of our instantiation of LIPS appear in Sect. 4. The components of LIPS are (1) a DSL specification, (2) a data-generation procedure, (3) a machine learning model that maps from input-output examples to program attributes, and (4) a search procedure that searches program space in an order guided by the model from (3). The framework is related to the formulation of Menon et al. (2013); the relationship and key differences are discussed in Sect. 6.

**(1) DSL and Attributes.** The choice of DSL is important in LIPS, just as it is in any program synthesis system. It should be expressive enough to capture the problems that we wish to solve, but restricted as much as possible to limit the difficulty of the search. In LIPS we additionally specify an attribute function A that maps programs P of the DSL to finite attribute vectors a = A(P). (Attribute vectors of different programs need not have equal length.) Attributes serve as the link between the machine learning and the search component of LIPS: the machine learning model predicts a distribution q(a | E), where E is the set of input-output examples, and the search procedure aims to search over programs P as ordered by q(A(P) | E). Thus an attribute is useful if it is both predictable from input-output examples, and if conditioning on its value significantly reduces the effective size of the search space.

Possible attributes are the (perhaps position-dependent) presence or absence of high-level functions (e.g., does the program contain or end in a call to SORT). Other possible attributes include control flow templates (e.g., the number of loops and conditionals). In the extreme case, one may set A to the identity function, in which case the attribute is equivalent to the program; however, in our experiments we find that performance is improved by choosing a more abstract attribute function.

**(2) Data Generation.** Step 2 is to generate a dataset ((P^(n), a^(n), E^(n)))_{n=1}^N of programs P^(n) in the chosen DSL, their attributes a^(n), and accompanying input-output examples E^(n). Different approaches are possible, ranging from enumerating valid programs in the DSL and pruning, to training a more sophisticated generative model of programs in the DSL. The key in the LIPS formulation is to ensure that it is feasible to generate a large dataset (ideally millions of programs).

**(3) Machine Learning Model.** The machine learning problem is to learn a distribution of attributes given input-output examples, q(a | E). There is freedom to explore a large space of models, so long as the input component can encode E, and the output is a proper distribution over attributes (e.g., if attributes are a fixed-size binary vector, then a neural network with independent sigmoid outputs is appropriate; if attributes are variable size, then a recurrent neural network output could be used). Attributes are observed at training time, so training can use a maximum likelihood objective.

**(4) Search.** The aim of the search component is to interface with an existing solver, using the predicted q(a | E) to guide the search. We describe specific approaches in the next section.

---

### النسخة العربية

في هذا القسم نحدد النهج العام الذي نتبعه في هذا العمل، والذي نسميه تعلم التوليد الاستقرائي للبرامج (Learning Inductive Program Synthesis - LIPS). تفاصيل تجسيدنا لـ LIPS تظهر في القسم 4. مكونات LIPS هي (1) مواصفات اللغة الخاصة بالمجال، (2) إجراء توليد البيانات، (3) نموذج تعلم آلة يعيّن من أمثلة الإدخال والإخراج إلى خصائص البرامج، و (4) إجراء بحث يبحث في فضاء البرامج بترتيب موجه بواسطة النموذج من (3). الإطار مرتبط بصياغة Menon وآخرون (2013)؛ العلاقة والاختلافات الرئيسية مناقشة في القسم 6.

**(1) اللغة الخاصة بالمجال والخصائص.** اختيار اللغة الخاصة بالمجال مهم في LIPS، تماماً كما هو الحال في أي نظام توليد برامج. يجب أن تكون تعبيرية بما يكفي لالتقاط المشاكل التي نرغب في حلها، ولكن مقيدة قدر الإمكان للحد من صعوبة البحث. في LIPS نحدد بالإضافة إلى ذلك دالة خاصية A التي تعيّن البرامج P من اللغة الخاصة بالمجال إلى متجهات خصائص محدودة a = A(P). (متجهات الخصائص للبرامج المختلفة لا يجب أن تكون بنفس الطول.) تعمل الخصائص كرابط بين تعلم الآلة ومكون البحث في LIPS: يتنبأ نموذج تعلم الآلة بتوزيع q(a | E)، حيث E هي مجموعة أمثلة الإدخال والإخراج، ويهدف إجراء البحث إلى البحث عبر البرامج P مرتبة بواسطة q(A(P) | E). وبالتالي فإن الخاصية مفيدة إذا كانت قابلة للتنبؤ من أمثلة الإدخال والإخراج، وإذا كان التكييف على قيمتها يقلل بشكل كبير من الحجم الفعال لفضاء البحث.

الخصائص الممكنة هي وجود أو غياب الدوال عالية المستوى (ربما تعتمد على الموقع) (على سبيل المثال، هل يحتوي البرنامج أو ينتهي بدعوة إلى SORT). تشمل الخصائص الممكنة الأخرى قوالب تدفق التحكم (على سبيل المثال، عدد الحلقات والشرطيات). في الحالة القصوى، قد يتم تعيين A إلى دالة الهوية، وفي هذه الحالة تكون الخاصية مكافئة للبرنامج؛ ومع ذلك، في تجاربنا نجد أن الأداء يتحسن باختيار دالة خاصية أكثر تجريداً.

**(2) توليد البيانات.** الخطوة 2 هي توليد مجموعة بيانات ((P^(n), a^(n), E^(n)))_{n=1}^N من البرامج P^(n) في اللغة الخاصة بالمجال المختارة، وخصائصها a^(n)، وأمثلة الإدخال والإخراج المصاحبة E^(n). النهج المختلفة ممكنة، تتراوح من تعداد البرامج الصالحة في اللغة الخاصة بالمجال والتقليم، إلى تدريب نموذج توليدي أكثر تطوراً للبرامج في اللغة الخاصة بالمجال. المفتاح في صياغة LIPS هو التأكد من أنه من الممكن توليد مجموعة بيانات كبيرة (من الناحية المثالية ملايين البرامج).

**(3) نموذج تعلم الآلة.** مشكلة تعلم الآلة هي تعلم توزيع الخصائص بالنظر إلى أمثلة الإدخال والإخراج، q(a | E). هناك حرية لاستكشاف مساحة كبيرة من النماذج، طالما أن مكون الإدخال يمكنه ترميز E، والمخرج هو توزيع مناسب على الخصائص (على سبيل المثال، إذا كانت الخصائص متجه ثنائي ذو حجم ثابت، فإن شبكة عصبية بمخرجات سيجمويد مستقلة مناسبة؛ إذا كانت الخصائص بحجم متغير، فيمكن استخدام مخرج شبكة عصبية متكررة). يتم ملاحظة الخصائص في وقت التدريب، لذلك يمكن للتدريب استخدام هدف أقصى احتمالية.

**(4) البحث.** الهدف من مكون البحث هو الواجهة مع حلال موجود، باستخدام q(a | E) المتنبأ به لتوجيه البحث. نصف النهج المحددة في القسم التالي.

---

### Translation Notes

- **Key terms introduced:**
  - Learning Inductive Program Synthesis (LIPS) = تعلم التوليد الاستقرائي للبرامج
  - attribute function = دالة الخاصية
  - attribute vector = متجه الخصائص
  - distribution = توزيع
  - data generation = توليد البيانات
  - maximum likelihood = أقصى احتمالية
  - sigmoid = سيجمويد (kept in transliteration as technical term)
  - identity function = دالة الهوية
  - control flow = تدفق التحكم

- **Mathematical notation:** Preserved all mathematical formulas (a = A(P), q(a | E), q(A(P) | E), etc.)
- **Citations:** Reference to Menon et al. (2013)
- **Special handling:** Framework name LIPS kept as acronym with Arabic expansion

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
