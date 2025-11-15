# Section 7: Growth and Restructuring
## القسم 7: النمو وإعادة الهيكلة

**Section:** Growth and Restructuring
**Translation Quality:** 0.86
**Glossary Terms Used:** data independence, schema evolution, restructuring, migration, backward compatibility

---

### English Version

## 7. GROWTH AND RESTRUCTURING

One of the principal objectives of the relational approach to data organization is to permit the data base to grow and change its structure without requiring modification of existing application programs. This objective stems from the recognition that large shared data banks have a long lifetime, during which:

1. The types of information stored in the data bank grow and change
2. The relationships among data items become more complex
3. New applications are developed that make unexpected demands on the data
4. Performance requirements change

### 7.1 Types of Growth

Several types of growth can occur in a data bank:

**Extension of domains**: New values may be added to existing domains. For example, a new job code might be added to the set of valid job codes. This type of growth is the easiest to accommodate and normally requires no change to the data base structure.

**Addition of new attributes**: New attributes may be added to existing relations. For example, we might add a "hire-date" attribute to an employee relation. This can be accomplished by extending the relation with additional columns. Applications that do not need the new attribute can ignore it.

**Creation of new relations**: Entirely new relations may be added to the data base to represent new types of entities or relationships. This is necessary when the data bank's scope expands to cover new subject areas.

**Changes to existing structures**: Sometimes the structure of existing relations must be changed. For example, a relation might need to be decomposed into two relations to eliminate redundancy or to improve performance.

### 7.2 Data Independence and Growth

The relational model supports data independence in two important ways:

**Logical data independence**: Applications can be insulated from changes in the logical structure of the data. For example, if a relation is decomposed into two relations, a view can be defined that reconstructs the original relation, allowing existing applications to continue working unchanged.

**Physical data independence**: Applications are insulated from changes in how the data is physically stored and accessed. Changes in indexing, clustering, or storage structures do not affect application programs, which access data only through the relational interface.

### 7.3 Restructuring Operations

When restructuring a data base, several operations may be needed:

**Decomposition**: A relation may be split into two or more relations. This is typically done to achieve a higher normal form or to separate frequently-accessed data from infrequently-accessed data.

**Composition**: Two or more relations may be combined into a single relation. This might be done if the decomposition was too fine-grained or if access patterns have changed.

**Attribute migration**: Attributes may be moved from one relation to another. This requires careful handling of functional dependencies to maintain consistency.

**Renaming**: Relations or attributes may be renamed for clarity. While this seems simple, it can affect many programs if not handled through views.

### 7.4 Managing Change

To manage structural changes effectively, the data base system should provide:

1. **View mechanism**: As discussed earlier, views allow the same logical structure to be presented to applications even when the underlying base relations change.

2. **Catalog or data dictionary**: Information about the data base structure should itself be stored in relational form, allowing it to be queried and modified using the same operations that apply to ordinary data.

3. **Migration tools**: Utilities should be provided to help transform data from old structures to new ones, checking constraints and preserving consistency.

4. **Version control**: Some mechanism is needed to manage concurrent access to the data base while restructuring is in progress.

The relational model, by separating logical and physical data organization, provides a solid foundation for managing the growth and evolution of large shared data banks.

---

### النسخة العربية

## 7. النمو وإعادة الهيكلة

أحد الأهداف الرئيسية للنهج العلائقي لتنظيم البيانات هو السماح لقاعدة البيانات بالنمو وتغيير بنيتها دون الحاجة إلى تعديل برامج التطبيقات الموجودة. ينبع هذا الهدف من الاعتراف بأن بنوك البيانات المشتركة الكبيرة لها عمر طويل، يحدث خلاله:

1. تنمو أنواع المعلومات المخزنة في بنك البيانات وتتغير
2. تصبح العلاقات بين عناصر البيانات أكثر تعقيداً
3. يتم تطوير تطبيقات جديدة تفرض متطلبات غير متوقعة على البيانات
4. تتغير متطلبات الأداء

### 7.1 أنواع النمو

يمكن أن تحدث عدة أنواع من النمو في بنك البيانات:

**توسيع النطاقات**: قد تتم إضافة قيم جديدة إلى النطاقات الموجودة. على سبيل المثال، قد تتم إضافة رمز وظيفي جديد إلى مجموعة رموز الوظائف الصالحة. هذا النوع من النمو هو الأسهل للاستيعاب ولا يتطلب عادة أي تغيير في بنية قاعدة البيانات.

**إضافة خصائص جديدة**: قد تتم إضافة خصائص جديدة إلى العلاقات الموجودة. على سبيل المثال، قد نضيف خاصية "تاريخ التوظيف" إلى علاقة الموظفين. يمكن تحقيق ذلك من خلال توسيع العلاقة بأعمدة إضافية. يمكن للتطبيقات التي لا تحتاج إلى الخاصية الجديدة تجاهلها.

**إنشاء علاقات جديدة**: قد تتم إضافة علاقات جديدة تماماً إلى قاعدة البيانات لتمثيل أنواع جديدة من الكيانات أو العلاقات. هذا ضروري عندما يتوسع نطاق بنك البيانات ليغطي مجالات موضوعية جديدة.

**تغييرات في البنى الموجودة**: في بعض الأحيان يجب تغيير بنية العلاقات الموجودة. على سبيل المثال، قد تحتاج علاقة إلى تحليلها إلى علاقتين للتخلص من التكرار أو لتحسين الأداء.

### 7.2 استقلالية البيانات والنمو

يدعم النموذج العلائقي استقلالية البيانات بطريقتين مهمتين:

**استقلالية البيانات المنطقية**: يمكن عزل التطبيقات عن التغييرات في البنية المنطقية للبيانات. على سبيل المثال، إذا تم تحليل علاقة إلى علاقتين، يمكن تعريف عرض (view) يعيد بناء العلاقة الأصلية، مما يسمح للتطبيقات الموجودة بالاستمرار في العمل دون تغيير.

**استقلالية البيانات الفيزيائية**: يتم عزل التطبيقات عن التغييرات في كيفية تخزين البيانات والوصول إليها فيزيائياً. لا تؤثر التغييرات في الفهرسة أو التجميع أو بنى التخزين على برامج التطبيقات، التي تصل إلى البيانات فقط من خلال الواجهة العلائقية.

### 7.3 عمليات إعادة الهيكلة

عند إعادة هيكلة قاعدة بيانات، قد تكون هناك حاجة إلى عدة عمليات:

**التحليل**: قد يتم تقسيم علاقة إلى علاقتين أو أكثر. يتم ذلك عادة لتحقيق شكل طبيعي أعلى أو لفصل البيانات التي يتم الوصول إليها بشكل متكرر عن البيانات التي يتم الوصول إليها بشكل غير متكرر.

**التركيب**: قد يتم دمج علاقتين أو أكثر في علاقة واحدة. قد يتم ذلك إذا كان التحليل دقيقاً للغاية أو إذا تغيرت أنماط الوصول.

**ترحيل الخصائص**: قد يتم نقل الخصائص من علاقة إلى أخرى. يتطلب ذلك معالجة دقيقة للتبعيات الوظيفية للحفاظ على الاتساق.

**إعادة التسمية**: قد تتم إعادة تسمية العلاقات أو الخصائص من أجل الوضوح. بينما يبدو هذا بسيطاً، يمكن أن يؤثر على العديد من البرامج إذا لم تتم معالجته من خلال العروض.

### 7.4 إدارة التغيير

لإدارة التغييرات الهيكلية بفعالية، يجب أن يوفر نظام قاعدة البيانات:

1. **آلية العروض**: كما نوقش سابقاً، تسمح العروض بتقديم نفس البنية المنطقية للتطبيقات حتى عندما تتغير العلاقات الأساسية.

2. **الفهرس أو قاموس البيانات**: يجب تخزين المعلومات حول بنية قاعدة البيانات نفسها في شكل علائقي، مما يسمح بالاستعلام عنها وتعديلها باستخدام نفس العمليات التي تنطبق على البيانات العادية.

3. **أدوات الترحيل**: يجب توفير أدوات مساعدة للمساعدة في تحويل البيانات من البنى القديمة إلى الجديدة، مع فحص القيود والحفاظ على الاتساق.

4. **التحكم في الإصدار**: هناك حاجة إلى آلية ما لإدارة الوصول المتزامن إلى قاعدة البيانات أثناء إعادة الهيكلة.

يوفر النموذج العلائقي، من خلال فصل تنظيم البيانات المنطقية والفيزيائية، أساساً متيناً لإدارة نمو وتطور بنوك البيانات المشتركة الكبيرة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** data independence, logical data independence, physical data independence, schema evolution, decomposition, composition, attribute migration, data dictionary, catalog
- **Equations:** 0
- **Citations:** 0
- **Special handling:** Conceptual discussion of database evolution and change management

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.89
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86
