# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** programming languages, application, abstraction, functional programming, semantics

---

### English Version

Most programming languages are partly a way of expressing things in terms of other things and partly a basic set of given things. The facilities for the one activity are usually called its assignment, control, and declaration features, the facilities for the other its data structure and operators or data descriptions and basic processes. This paper is mainly concerned with the former.

The applicability of a programming language is largely determined by the range of concepts that can be expressed in it and by the smoothness with which it can be done. The existing range of languages reflects this. Some are oriented to list manipulation and some to matrix operations, some to numerical calculation and some to symbol manipulation. One language provides good sorting routines, another good string-handling.

A particular task may be easy to express in one language but hard in another. The paper introduces a family of languages that is intended to express a particularly wide range of concepts in a uniform way. The intent is to provide a framework that can span different application areas by allowing users to coin names for their own operations and entities and to express functional relationships between them.

The framework provided by these languages is called ISWIM, an acronym standing for "If you See What I Mean." ISWIM is not a single language but a family of languages with common underlying semantics. It attempts to combine the advantages of many existing languages while avoiding their incompatibilities.

The paper proposes that the design of a programming language can be divided into two independent aspects: the choice of how programs appear when written (their syntax or "surface structure"), and the choice of what kinds of things the programs can refer to (their semantics or "abstract entities"). This separation allows different "dialects" of ISWIM to share a common semantic core while having different syntactic presentations suited to different users or application domains.

---

### النسخة العربية

معظم لغات البرمجة هي جزئياً وسيلة للتعبير عن الأشياء من خلال أشياء أخرى، وجزئياً مجموعة أساسية من الأشياء المعطاة. عادة ما تُسمى التسهيلات للنشاط الأول بميزات الإسناد والتحكم والإعلان، بينما تُسمى التسهيلات للنشاط الآخر ببنية البيانات والمعاملات أو أوصاف البيانات والعمليات الأساسية. يهتم هذا البحث بشكل أساسي بالأول.

تتحدد قابلية تطبيق لغة البرمجة إلى حد كبير بنطاق المفاهيم التي يمكن التعبير عنها فيها وبمدى سلاسة القيام بذلك. يعكس النطاق الحالي للغات هذا الأمر. فبعضها موجه نحو معالجة القوائم والبعض الآخر نحو عمليات المصفوفات، وبعضها نحو الحساب العددي والبعض الآخر نحو معالجة الرموز. توفر إحدى اللغات إجراءات فرز جيدة، بينما توفر أخرى معالجة جيدة للسلاسل النصية.

قد تكون مهمة معينة سهلة التعبير في لغة واحدة ولكنها صعبة في لغة أخرى. يقدم البحث عائلة من اللغات تهدف إلى التعبير عن نطاق واسع بشكل خاص من المفاهيم بطريقة موحدة. الهدف هو توفير إطار عمل يمكن أن يغطي مجالات تطبيق مختلفة من خلال السماح للمستخدمين بابتكار أسماء لعملياتهم وكياناتهم الخاصة والتعبير عن العلاقات الوظيفية بينها.

يُسمى الإطار الذي توفره هذه اللغات ISWIM، وهو اختصار لعبارة "If you See What I Mean" (إذا كنت ترى ما أعنيه). ISWIM ليست لغة واحدة بل عائلة من اللغات ذات دلالات أساسية مشتركة. تحاول الجمع بين مزايا العديد من اللغات الموجودة مع تجنب عدم توافقها.

يقترح البحث أن تصميم لغة البرمجة يمكن تقسيمه إلى جانبين مستقلين: اختيار كيفية ظهور البرامج عند كتابتها (بنيتها التركيبية أو "البنية السطحية")، واختيار أنواع الأشياء التي يمكن للبرامج الإشارة إليها (دلالاتها أو "الكيانات المجردة"). يسمح هذا الفصل لـ "لهجات" مختلفة من ISWIM بمشاركة نواة دلالية مشتركة مع الحصول على عروض تركيبية مختلفة تناسب مستخدمين مختلفين أو مجالات تطبيق مختلفة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - assignment, control, and declaration features (ميزات الإسناد والتحكم والإعلان)
  - data structure and operators (بنية البيانات والمعاملات)
  - ISWIM (يبقى كما هو - اختصار)
  - surface structure (البنية السطحية)
  - semantic core (النواة الدلالية)
- **Equations:** None
- **Citations:** None in this section
- **Special handling:** The acronym ISWIM is kept in English as it's a proper name

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
