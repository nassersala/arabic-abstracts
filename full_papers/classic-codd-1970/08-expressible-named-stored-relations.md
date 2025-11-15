# Section 8: Expressible, Named, and Stored Relations
## القسم 8: العلاقات القابلة للتعبير والمسماة والمخزنة

**Section:** Expressible, Named, and Stored Relations
**Translation Quality:** 0.86
**Glossary Terms Used:** expressible relation, named relation, stored relation, materialized view, virtual relation

---

### English Version

## 8. EXPRESSIBLE, NAMED, AND STORED RELATIONS

### 8.1 Three Categories of Relations

In a relational data base system, we can distinguish among three categories of relations:

**Expressible relations**: These are all relations that can be expressed using the operations of the relational algebra (or relational calculus) applied to the base relations. This is an infinite set—new relations can always be created by applying operations to existing ones.

**Named relations**: These are expressible relations that have been given names and are known to the system. Named relations include all base relations and all defined views. The set of named relations is typically much smaller than the set of expressible relations.

**Stored relations**: These are named relations that are actually stored in the data base. Typically, all base relations are stored, and some derived relations (materialized views) may also be stored for performance reasons.

### 8.2 Expressibility and Completeness

The concept of expressible relations is closely tied to the notion of relational completeness discussed earlier. A relationally complete language allows users to express any relation that can be defined in terms of the relational algebra.

However, there are limits to what can be expressed in pure relational algebra. Queries involving:
- Transitive closure (e.g., "find all supervisory chains")
- Aggregation (e.g., "count the employees in each department")
- General recursion

...generally require extensions to the basic relational algebra. Most practical query languages provide such extensions while maintaining the spirit of the relational approach.

### 8.3 Named Relations and the Data Sublanguage

Named relations serve several purposes:

1. **Defining the schema**: The collection of base relation names defines the logical structure of the data base
2. **Providing views**: Named derived relations (views) give users simplified or customized perspectives on the data
3. **Enabling reuse**: Complex queries can be saved as named relations and reused
4. **Supporting access control**: Permissions can be granted on individual named relations

The data sublanguage must provide facilities for:
- Defining new named relations (both base and derived)
- Querying named relations
- Updating base relations
- Dropping relations that are no longer needed

### 8.4 Storage Considerations

The decision of which relations to store is a performance optimization issue. Factors to consider include:

**Storage cost**: Storing derived relations uses additional disk space. This must be balanced against the computation cost of deriving the relation when needed.

**Update cost**: If a stored derived relation depends on base relations that are frequently updated, maintaining consistency becomes expensive.

**Query patterns**: Relations that are queried very frequently are good candidates for storage, especially if they are expensive to compute.

**System complexity**: Maintaining stored derived relations adds complexity to the data base system. The system must ensure that all stored representations remain consistent.

### 8.5 Materialized Views

A materialized view is a named derived relation that is actually stored in the data base. When the base relations change, the materialized view may need to be updated. Several strategies exist:

- **Immediate update**: The view is updated as soon as any base relation changes
- **Deferred update**: The view is marked as needing refresh and is updated later
- **Incremental update**: Only the changes are computed and applied to the view
- **Complete recomputation**: The entire view is recomputed from scratch

The choice of strategy depends on the update and query frequencies, the complexity of the view definition, and system resources.

---

### النسخة العربية

## 8. العلاقات القابلة للتعبير والمسماة والمخزنة

### 8.1 ثلاث فئات من العلاقات

في نظام قاعدة بيانات علائقية، يمكننا التمييز بين ثلاث فئات من العلاقات:

**العلاقات القابلة للتعبير**: هذه هي جميع العلاقات التي يمكن التعبير عنها باستخدام عمليات الجبر العلائقي (أو حساب التفاضل والتكامل العلائقي) المطبقة على العلاقات الأساسية. هذه مجموعة لا نهائية - يمكن دائماً إنشاء علاقات جديدة من خلال تطبيق العمليات على العلاقات الموجودة.

**العلاقات المسماة**: هذه هي العلاقات القابلة للتعبير التي تم إعطاؤها أسماء ومعروفة للنظام. تتضمن العلاقات المسماة جميع العلاقات الأساسية وجميع العروض المحددة. عادة ما تكون مجموعة العلاقات المسماة أصغر بكثير من مجموعة العلاقات القابلة للتعبير.

**العلاقات المخزنة**: هذه هي العلاقات المسماة المخزنة فعلياً في قاعدة البيانات. عادة، يتم تخزين جميع العلاقات الأساسية، وقد يتم أيضاً تخزين بعض العلاقات المشتقة (العروض المادية) لأسباب تتعلق بالأداء.

### 8.2 القابلية للتعبير والاكتمال

يرتبط مفهوم العلاقات القابلة للتعبير ارتباطاً وثيقاً بمفهوم الاكتمال العلائقي الذي نوقش سابقاً. تسمح اللغة الكاملة علائقياً للمستخدمين بالتعبير عن أي علاقة يمكن تعريفها من حيث الجبر العلائقي.

ومع ذلك، هناك حدود لما يمكن التعبير عنه في الجبر العلائقي النقي. الاستعلامات التي تتضمن:
- الإغلاق المتعدي (على سبيل المثال، "العثور على جميع سلاسل الإشراف")
- التجميع (على سبيل المثال، "عد الموظفين في كل قسم")
- التكرار العام

...تتطلب عموماً امتدادات للجبر العلائقي الأساسي. توفر معظم لغات الاستعلام العملية مثل هذه الامتدادات مع الحفاظ على روح النهج العلائقي.

### 8.3 العلاقات المسماة ولغة البيانات الفرعية

تخدم العلاقات المسماة عدة أغراض:

1. **تعريف المخطط**: تعرّف مجموعة أسماء العلاقات الأساسية البنية المنطقية لقاعدة البيانات
2. **توفير العروض**: تمنح العلاقات المشتقة المسماة (العروض) المستخدمين وجهات نظر مبسطة أو مخصصة على البيانات
3. **تمكين إعادة الاستخدام**: يمكن حفظ الاستعلامات المعقدة كعلاقات مسماة وإعادة استخدامها
4. **دعم التحكم في الوصول**: يمكن منح الأذونات على علاقات مسماة فردية

يجب أن توفر لغة البيانات الفرعية مرافق لـ:
- تعريف علاقات مسماة جديدة (الأساسية والمشتقة)
- الاستعلام عن العلاقات المسماة
- تحديث العلاقات الأساسية
- حذف العلاقات التي لم تعد هناك حاجة إليها

### 8.4 اعتبارات التخزين

قرار العلاقات التي يجب تخزينها هو مسألة تحسين الأداء. العوامل التي يجب مراعاتها تشمل:

**تكلفة التخزين**: يستخدم تخزين العلاقات المشتقة مساحة قرص إضافية. يجب موازنة ذلك مع تكلفة الحوسبة لاشتقاق العلاقة عند الحاجة.

**تكلفة التحديث**: إذا كانت العلاقة المشتقة المخزنة تعتمد على علاقات أساسية يتم تحديثها بشكل متكرر، يصبح الحفاظ على الاتساق مكلفاً.

**أنماط الاستعلام**: العلاقات التي يتم الاستعلام عنها بشكل متكرر جداً هي مرشحة جيدة للتخزين، خاصة إذا كانت مكلفة حسابياً.

**تعقيد النظام**: إن الحفاظ على العلاقات المشتقة المخزنة يضيف تعقيداً إلى نظام قاعدة البيانات. يجب على النظام التأكد من أن جميع التمثيلات المخزنة تظل متسقة.

### 8.5 العروض المادية

العرض المادي (materialized view) هو علاقة مشتقة مسماة مخزنة فعلياً في قاعدة البيانات. عندما تتغير العلاقات الأساسية، قد يحتاج العرض المادي إلى التحديث. توجد عدة استراتيجيات:

- **التحديث الفوري**: يتم تحديث العرض بمجرد تغيير أي علاقة أساسية
- **التحديث المؤجل**: يتم وضع علامة على العرض بأنه يحتاج إلى تحديث ويتم تحديثه لاحقاً
- **التحديث التدريجي**: يتم حساب التغييرات فقط وتطبيقها على العرض
- **إعادة الحساب الكاملة**: يتم إعادة حساب العرض بالكامل من الصفر

يعتمد اختيار الاستراتيجية على ترددات التحديث والاستعلام، وتعقيد تعريف العرض، وموارد النظام.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** expressible relation, named relation, stored relation, materialized view, relational calculus, transitive closure, aggregation, incremental update
- **Equations:** 0
- **Citations:** 0
- **Special handling:** Discussion of different categories of relations and materialization strategies

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.89
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86
