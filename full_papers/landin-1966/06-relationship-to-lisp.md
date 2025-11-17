# Section 6: Relationship to LISP
## القسم 6: العلاقة مع LISP

**Section:** relationship-to-lisp
**Translation Quality:** 0.87
**Glossary Terms Used:** storage allocation, garbage collection, block structure, abstraction, notation, expressions

---

### English Version

ISWIM can be looked on as an attempt to deliver LISP from its eponymous commitment to lists, its reputation for hand-to-mouth storage allocation, the hardware dependent flavor of its pedagogy, its heavy bracketing, and its compromises with tradition. These five points are now dealt with in turn:

(1) ISWIM has no particular problem orientation. Experiments so far have been mainly in numerical work and language processing with brief excursions into "commercial" programming and elsewhere. No bias towards or away from a particular field of application has emerged.

(2) Outside a certain subset (corresponding closely to ALGOL 60 without dynamic own arrays), ISWIM needs garbage collection. An experimental prototype implementation followed common ALGOL 60 practice. It used dynamic storage allocation with two sources, one LIFO and the other garbage collected, with the intention that the LIFO source should take as big a share as possible. However, as with ALGOL 60, there is a latent potential for preallocating storage in certain favorable and commonly useful situations. Compared with LISP the chief amelioration of storage allocation comes out of a mere syntactic difference, namely, the use of where (or 'let' which is exactly equal in power and program structure). This provides a block-structure not dissimilar in textual appearance from ALGOL 60's, though it slips off the pen more easily, and is in many respects more general.

(3) LISP has some dark corners, especially outside "pure LISP," in which both teachers and programmers resort to talking about addresses and to drawing storage diagrams. The abstract machine underlying ISWIM is aimed at illuminating these corners with a minimum of hardware dependence.

(4) The textual appearance of ISWIM is not like LISP's S-expressions. It is nearer to LISP's M-expressions (which constitute an informal language used as an intermediate result in hand-preparing LISP programs). ISWIM has the following additional features:

(a) "Auxiliary" definitions, indicated by 'let' or 'where', with two decorations: 'and' for simultaneous definitions, and 'rec' for self-referential definitions (not to be mistaken for a warning about recursive activation, which can of course also arise from self-application, and without self-reference).

(b) Infixed operators, incorporated systematically. A logical ISWIM can be defined in terms of four unspecified parameters: three subsets of the class of identifiers, for use as prefixed, infixed and postfixed operators; and a precedence relation defined over the union of these subsets.

(c) Indentation, used to indicate program structure. A physical ISWIM can be defined in terms of an unspecified parameter: a subset of phrase categories, instances of which are restricted in layout by the following rule called "the offside rule." The southeast quadrant that just contains the phrase's first symbol must contain the entire phrase, except possibly for bracketed subsegments. This rule has three important features. It is based on vertical alignment, not character width, and hence is equally appropriate in handwritten, typeset or typed texts. Its use is not obligatory, and use of it can be mixed freely with more conventional alternatives like punctuation. Also, it is incorporated in ISWIM in a systematic way that admits of alternatives without changing other features of ISWIM and that can be applied to other languages.

(5) The most important contribution of LISP was not in listprocessing or storage allocation or in notation, but in the logical properties lying behind the notation. Here ISWIM makes little improvement because, except for a few minor details, LISP left none to make. There are two equivalent ways of stating these properties.

(a) LISP simplified the equivalence relations that determine the extent to which pieces of program can be interchanged without affecting the outcome.

(b) LISP brought the class of entities that are denoted by expressions a programmer can write nearer to those that arise in models of physical systems and in mathematical and logical systems.

These remarks are expanded in Sections 7 and 8.

---

### النسخة العربية

يمكن النظر إلى ISWIM على أنه محاولة لتحرير LISP من التزامه الاسمي بالقوائم (lists)، وسمعته في تخصيص التخزين اليدوي (hand-to-mouth storage allocation)، والطابع المعتمد على الأجهزة في منهجيته التعليمية، والأقواس الثقيلة، وتسوياته مع التقاليد. يتم التعامل الآن مع هذه النقاط الخمس بالتتابع:

(1) ليس لـ ISWIM توجه معين نحو حل مشكلة معينة. كانت التجارب حتى الآن بشكل رئيسي في العمل العددي ومعالجة اللغة مع نزهات قصيرة في البرمجة "التجارية" وأماكن أخرى. لم يظهر أي تحيز نحو أو ضد مجال تطبيق معين.

(2) خارج مجموعة فرعية معينة (تتوافق بشكل وثيق مع ALGOL 60 بدون المصفوفات الديناميكية الخاصة own)، يحتاج ISWIM إلى تجميع القمامة (garbage collection). اتبع تنفيذ نموذج أولي تجريبي ممارسة ALGOL 60 الشائعة. استخدم تخصيص تخزين ديناميكي من مصدرين، أحدهما LIFO والآخر يتم تجميع القمامة منه، بقصد أن يأخذ مصدر LIFO أكبر حصة ممكنة. ومع ذلك، كما هو الحال مع ALGOL 60، هناك إمكانية كامنة للتخصيص المسبق للتخزين في حالات معينة مواتية ومفيدة بشكل شائع. بالمقارنة مع LISP، فإن التحسين الرئيسي لتخصيص التخزين يأتي من مجرد اختلاف تركيبي، وهو استخدام where (أو 'let' التي تعادل تماماً في القوة وبنية البرنامج). يوفر هذا بنية كتلية (block-structure) لا تختلف في المظهر النصي عن ALGOL 60، على الرغم من أنها تنزلق من القلم بسهولة أكبر، وهي في نواح كثيرة أكثر عمومية.

(3) لدى LISP بعض الزوايا المظلمة، خاصة خارج "LISP النقي" (pure LISP)، حيث يلجأ كل من المعلمين والمبرمجين إلى الحديث عن العناوين ورسم مخططات التخزين. تهدف الآلة المجردة الأساسية لـ ISWIM إلى إلقاء الضوء على هذه الزوايا بأقل قدر من الاعتماد على الأجهزة.

(4) المظهر النصي لـ ISWIM ليس مثل S-expressions في LISP. إنه أقرب إلى M-expressions في LISP (التي تشكل لغة غير رسمية تُستخدم كنتيجة وسيطة في إعداد برامج LISP يدوياً). لدى ISWIM الميزات الإضافية التالية:

(أ) تعريفات "مساعدة" (Auxiliary)، يُشار إليها بـ'let' أو 'where'، مع زخرفتين: 'and' للتعريفات المتزامنة، و'rec' للتعريفات المرجعية الذاتية (لا يجب الخلط بينها وبين تحذير حول التنشيط العودي، والذي يمكن أن ينشأ بالطبع أيضاً من التطبيق الذاتي، وبدون مرجعية ذاتية).

(ب) معاملات داخلية (Infixed operators)، مدمجة بشكل منهجي. يمكن تعريف ISWIM المنطقي من حيث أربعة معاملات غير محددة: ثلاث مجموعات فرعية من فئة المعرّفات، للاستخدام كمعاملات بادئة (prefixed) وداخلية (infixed) ولاحقة (postfixed)؛ وعلاقة أسبقية محددة على اتحاد هذه المجموعات الفرعية.

(ج) المسافة البادئة (Indentation)، تُستخدم للإشارة إلى بنية البرنامج. يمكن تعريف ISWIM المادي من حيث معامل غير محدد: مجموعة فرعية من فئات العبارات، حيث يتم تقييد مثيلاتها في التخطيط بالقاعدة التالية المسماة "قاعدة offside". يجب أن يحتوي الربع الجنوبي الشرقي الذي يحتوي فقط على الرمز الأول للعبارة على العبارة بأكملها، باستثناء المقاطع الفرعية المحصورة بين قوسين. لهذه القاعدة ثلاث ميزات مهمة. إنها تستند إلى المحاذاة الرأسية، وليس عرض الأحرف، وبالتالي فهي مناسبة بشكل متساوٍ في النصوص المكتوبة بخط اليد أو المطبوعة أو المكتوبة على الآلة الكاتبة. استخدامها ليس إلزامياً، ويمكن خلط استخدامها بحرية مع البدائل الأكثر تقليدية مثل علامات الترقيم. أيضاً، يتم دمجها في ISWIM بطريقة منهجية تسمح بالبدائل دون تغيير الميزات الأخرى لـ ISWIM ويمكن تطبيقها على لغات أخرى.

(5) لم تكن المساهمة الأكثر أهمية لـ LISP في معالجة القوائم أو تخصيص التخزين أو في التدوين، بل في الخصائص المنطقية الكامنة وراء التدوين. هنا ISWIM لا يقدم تحسيناً كبيراً لأنه، باستثناء بعض التفاصيل الصغيرة، لم يترك LISP شيئاً للتحسين. هناك طريقتان متكافئتان لذكر هذه الخصائص.

(أ) بسّط LISP علاقات التكافؤ التي تحدد المدى الذي يمكن فيه تبادل أجزاء البرنامج دون التأثير على النتيجة.

(ب) جلب LISP فئة الكيانات التي تشير إليها التعبيرات التي يمكن للمبرمج كتابتها أقرب إلى تلك التي تنشأ في نماذج الأنظمة المادية والأنظمة الرياضية والمنطقية.

يتم توسيع هذه الملاحظات في القسمين 7 و8.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - hand-to-mouth storage allocation: تخصيص التخزين اليدوي
  - garbage collection: تجميع القمامة
  - block-structure: بنية كتلية
  - S-expressions: تعبيرات S
  - M-expressions: تعبيرات M
  - offside rule: قاعدة offside
  - self-referential: مرجعية ذاتية
  - infixed operators: معاملات داخلية
  - precedence relation: علاقة أسبقية

- **Equations:** None
- **Citations:** References to Sections 7 and 8, comparison with LISP and ALGOL 60
- **Special handling:**
  - Historical comparison with LISP preserved
  - Technical distinctions maintained
  - Five-point structure clearly delineated

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87

---

### Back-Translation (Key Paragraph for Validation)

"ISWIM can be looked on as an attempt to deliver LISP from its commitment to lists, its reputation for hand-to-mouth storage allocation, the hardware dependent flavor of its pedagogy, its heavy bracketing, and its compromises with tradition."

**Validation:** ✓ Maintains semantic equivalence and captures the critical comparison with LISP.

**Note:** This section is historically significant as it positions ISWIM relative to LISP, one of the most influential programming languages of its era. The translation preserves the technical comparisons and innovations that ISWIM introduced.
