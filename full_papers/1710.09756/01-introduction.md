# Section 1: Introduction
## القسم 1: المقدمة

**Section:** Introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** linear types, functional programming, compiler, type system, higher-order, polymorphism, ownership typing, uniqueness typing

---

### English Version

Despite their obvious promise, and a huge research literature, linear type systems have not made it into mainstream programming languages, even though linearity has inspired uniqueness typing in Clean, and ownership typing in Rust. We take up this challenge by extending Haskell with linear types. Our design supports many applications for linear types, but we focus on two particular use-cases. First, safe update-in-place for mutable structures, such as arrays; and second, enforcing access protocols for external APIs, such as files, sockets, channels and other resources. Our particular contributions are these:

• We describe an extension to Haskell for linear types, dubbed Linear Haskell, using two extended examples (Sec. 2.1-Sec. 2.3). The extension is non-invasive: existing programs continue to typecheck, and existing datatypes can be used as-is even in linear parts of the program. The key to this non-invasiveness is that, in contrast to most other approaches, we focus on linearity on the function arrow rather than linearity in the kinds (Sec. 6.1).

• Every function arrow can be declared linear, including those of constructor types. This results in datatypes which can store both linear values, in addition to unrestricted ones (Sec. 2.4-2.5).

• A benefit of linearity-on-the-arrow is that it naturally supports linearity polymorphism (Sec. 2.6). This contributes to a smooth extension of Haskell by allowing many existing functions (map, compose, etc) to be given more general types, so they can work uniformly in both linear and non-linear code.

• We formalise our system in a small, statically-typed core calculus that exhibits all these features (Sec. 3). It enjoys the usual properties of progress and preservation.

• We have implemented a prototype of the system as a modest extension to GHC (Sec. 4), which substantiates our claim of non-invasiveness. We use this prototype to implement case-study applications (Sec. 5). Our prototype performs linearity inference, but a systematic treatment of type inference for linearity in our system remains open.

Retrofits often involve compromise and ad-hoc choices, but in fact we have found that, as well as fitting into Haskell, our design holds together in its own right. We hope that it may perhaps serve as a template for similar work in other languages. There is a rich literature on linear type systems, as we discuss in a long related work section (Sec. 6).

---

### النسخة العربية

على الرغم من الوعد الواضح للأنواع الخطية، والأدبيات البحثية الضخمة حولها، إلا أن أنظمة الأنواع الخطية لم تدخل إلى لغات البرمجة السائدة، على الرغم من أن الخطية ألهمت كتابة الفردية (uniqueness typing) في Clean، وكتابة الملكية (ownership typing) في Rust. نتصدى لهذا التحدي من خلال توسيع Haskell بالأنواع الخطية. يدعم تصميمنا العديد من تطبيقات الأنواع الخطية، لكننا نركز على حالتي استخدام معينتين. أولاً، التحديث الآمن في المكان للبنى القابلة للتغيير، مثل المصفوفات؛ وثانياً، فرض بروتوكولات الوصول لواجهات برمجة التطبيقات الخارجية، مثل الملفات والمقابس والقنوات والموارد الأخرى. مساهماتنا المحددة هي كما يلي:

• نصف امتداداً لـ Haskell للأنواع الخطية، يُطلق عليه Haskell الخطي، باستخدام مثالين موسعين (القسم 2.1-القسم 2.3). الامتداد غير تدخلي: تستمر البرامج الموجودة في اجتياز فحص الأنواع، ويمكن استخدام أنواع البيانات الموجودة كما هي حتى في الأجزاء الخطية من البرنامج. مفتاح عدم التدخل هذا هو أننا، على عكس معظم الأساليب الأخرى، نركز على الخطية في سهم الدالة بدلاً من الخطية في الأنواع (القسم 6.1).

• يمكن الإعلان عن كل سهم دالة على أنه خطي، بما في ذلك أسهم أنواع المُنشئات. ينتج عن هذا أنواع بيانات يمكنها تخزين القيم الخطية، بالإضافة إلى القيم غير المقيدة (القسم 2.4-2.5).

• فائدة الخطية على السهم هي أنها تدعم بشكل طبيعي تعددية الخطية (linearity polymorphism) (القسم 2.6). يساهم هذا في توسيع سلس لـ Haskell من خلال السماح للعديد من الدوال الموجودة (map، compose، إلخ) بإعطائها أنواعاً أكثر عمومية، بحيث يمكنها العمل بشكل موحد في كل من الشفرة الخطية وغير الخطية.

• نضفي الطابع الرسمي على نظامنا في حساب أساسي صغير مكتوب بشكل ثابت يعرض كل هذه الميزات (القسم 3). يتمتع بالخصائص المعتادة للتقدم والحفاظ.

• قمنا بتنفيذ نموذج أولي للنظام كامتداد متواضع لـ GHC (القسم 4)، والذي يدعم ادعاءنا بعدم التدخل. نستخدم هذا النموذج الأولي لتنفيذ تطبيقات دراسة حالة (القسم 5). يقوم نموذجنا الأولي بإجراء استدلال الخطية، لكن المعالجة المنهجية لاستدلال الأنواع للخطية في نظامنا لا تزال مفتوحة.

غالباً ما تتضمن التحديثات الاستعارية (Retrofits) التسوية والاختيارات المخصصة، ولكننا وجدنا في الواقع أنه، بالإضافة إلى ملاءمة Haskell، فإن تصميمنا متماسك في حد ذاته. نأمل أن يكون بمثابة قالب لأعمال مماثلة في لغات أخرى. هناك أدبيات غنية حول أنظمة الأنواع الخطية، كما نناقش في قسم العمل ذي الصلة الطويل (القسم 6).

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:**
  - Linear types (الأنواع الخطية)
  - Linear Haskell (Haskell الخطي)
  - Linearity on the arrow (الخطية على السهم)
  - Linearity polymorphism (تعددية الخطية)
  - Update-in-place (التحديث في المكان)
  - Access protocols (بروتوكولات الوصول)
  - Uniqueness typing (كتابة الفردية)
  - Ownership typing (كتابة الملكية)
- **Citations:** References to sections 2-6
- **Special handling:** Bullet points maintained in both versions

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.86
- **Overall section score:** 0.87
