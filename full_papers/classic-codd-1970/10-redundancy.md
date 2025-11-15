# Section 10: Redundancy
## القسم 10: التكرار

**Section:** Redundancy
**Translation Quality:** 0.86
**Glossary Terms Used:** redundancy, normalization, update anomaly, insertion anomaly, deletion anomaly, lossless decomposition

---

### English Version

## 10. REDUNDANCY

### 10.1 The Problem of Redundancy

Redundancy occurs when the same fact is represented in multiple places in a data base. While some redundancy may be deliberate (for backup or performance), uncontrolled redundancy leads to serious problems:

**Update anomalies**: If a redundantly stored fact must be updated, all copies must be changed. If some copies are updated and others are not, the data base becomes inconsistent.

**Insertion anomalies**: It may be impossible to record certain facts without recording other, unrelated facts. For example, if employee and department information are stored together, we cannot record information about a new department until we hire an employee for that department.

**Deletion anomalies**: Deleting certain data may cause loss of other, independent facts. For example, if we delete the last employee in a department, we may lose all information about that department.

### 10.2 Normalization as a Solution

The process of normalization is designed to eliminate redundancy by organizing data into well-structured relations. The normal forms provide a hierarchy of increasingly stringent conditions:

**First Normal Form (1NF)**: All domains are simple (atomic). No repeating groups or nested relations.

**Second Normal Form (2NF)**: In 1NF, and every non-key attribute is fully functionally dependent on the entire primary key (not on just part of it).

**Third Normal Form (3NF)**: In 2NF, and every non-key attribute is non-transitively dependent on the primary key (no dependencies between non-key attributes).

Higher normal forms (BCNF, 4NF, 5NF) impose even stronger conditions, addressing more subtle forms of redundancy and dependency.

### 10.3 Decomposition

To achieve a desired normal form, relations often must be decomposed—split into two or more relations. A key requirement is that the decomposition be lossless: it must be possible to reconstruct the original relation by joining the decomposed relations.

For example, consider a relation:
```
EMPLOYEE-DEPT (employee#, employee-name, dept#, dept-name, dept-location)
```

This has redundancy because department information is repeated for each employee in that department. It can be decomposed into:
```
EMPLOYEE (employee#, employee-name, dept#)
DEPARTMENT (dept#, dept-name, dept-location)
```

The original relation can be reconstructed by joining these two relations on dept#.

### 10.4 Trade-offs

While normalization reduces redundancy and eliminates anomalies, it has costs:

**Join cost**: Queries that need data from multiple normalized relations require join operations, which can be expensive.

**Complexity**: A highly normalized schema may have many relations, making the data base structure more complex to understand and manage.

In practice, database designers must balance these considerations. Sometimes controlled denormalization is used to improve performance, accepting some redundancy in exchange for reduced query complexity.

### 10.5 The Role of Constraints

Even with well-normalized relations, certain constraints must be enforced to maintain consistency:

**Domain constraints**: Ensuring that attribute values come from the appropriate domains

**Key constraints**: Ensuring that primary key values are unique and non-null

**Referential integrity**: Ensuring that foreign key values match primary key values in referenced relations

The relational model provides a framework for expressing these constraints formally, and a relational DBMS should enforce them automatically.

---

### النسخة العربية

## 10. التكرار

### 10.1 مشكلة التكرار

يحدث التكرار عندما يتم تمثيل نفس الحقيقة في أماكن متعددة في قاعدة البيانات. في حين أن بعض التكرار قد يكون متعمداً (للنسخ الاحتياطي أو الأداء)، فإن التكرار غير المضبوط يؤدي إلى مشاكل خطيرة:

**شذوذات التحديث**: إذا كان يجب تحديث حقيقة مخزنة بشكل متكرر، فيجب تغيير جميع النسخ. إذا تم تحديث بعض النسخ ولم يتم تحديث البعض الآخر، تصبح قاعدة البيانات غير متسقة.

**شذوذات الإدراج**: قد يكون من المستحيل تسجيل حقائق معينة دون تسجيل حقائق أخرى غير ذات صلة. على سبيل المثال، إذا تم تخزين معلومات الموظفين والأقسام معاً، فلا يمكننا تسجيل معلومات حول قسم جديد حتى نوظف موظفاً لذلك القسم.

**شذوذات الحذف**: قد يؤدي حذف بيانات معينة إلى فقدان حقائق أخرى مستقلة. على سبيل المثال، إذا حذفنا آخر موظف في قسم، فقد نفقد جميع المعلومات حول ذلك القسم.

### 10.2 التطبيع كحل

تم تصميم عملية التطبيع (normalization) للقضاء على التكرار من خلال تنظيم البيانات في علاقات جيدة البنية. توفر الأشكال الطبيعية تسلسلاً هرمياً من الشروط الأكثر صرامة:

**الشكل الطبيعي الأول (1NF)**: جميع النطاقات بسيطة (ذرية). لا توجد مجموعات متكررة أو علاقات متداخلة.

**الشكل الطبيعي الثاني (2NF)**: في 1NF، وكل خاصية غير مفتاح تعتمد وظيفياً بالكامل على المفتاح الأولي بأكمله (وليس على جزء منه فقط).

**الشكل الطبيعي الثالث (3NF)**: في 2NF، وكل خاصية غير مفتاح تعتمد بشكل غير متعدي على المفتاح الأولي (لا توجد تبعيات بين الخصائص غير المفتاح).

تفرض الأشكال الطبيعية الأعلى (BCNF، 4NF، 5NF) شروطاً أقوى، معالجة أشكال أكثر دقة من التكرار والتبعية.

### 10.3 التحليل

لتحقيق شكل طبيعي مرغوب، يجب غالباً تحليل العلاقات - تقسيمها إلى علاقتين أو أكثر. المتطلب الرئيسي هو أن يكون التحليل بدون فقدان: يجب أن يكون من الممكن إعادة بناء العلاقة الأصلية من خلال ربط العلاقات المُحللة.

على سبيل المثال، لنأخذ العلاقة:
```
EMPLOYEE-DEPT (employee#, employee-name, dept#, dept-name, dept-location)
```

هذا يحتوي على تكرار لأن معلومات القسم تتكرر لكل موظف في ذلك القسم. يمكن تحليلها إلى:
```
EMPLOYEE (employee#, employee-name, dept#)
DEPARTMENT (dept#, dept-name, dept-location)
```

يمكن إعادة بناء العلاقة الأصلية من خلال ربط هاتين العلاقتين على dept#.

### 10.4 المقايضات

في حين أن التطبيع يقلل من التكرار ويزيل الشذوذات، إلا أن له تكاليف:

**تكلفة الربط**: تتطلب الاستعلامات التي تحتاج إلى بيانات من علاقات مُطبّعة متعددة عمليات ربط، والتي يمكن أن تكون مكلفة.

**التعقيد**: قد يحتوي المخطط المُطبّع بشكل كبير على العديد من العلاقات، مما يجعل بنية قاعدة البيانات أكثر تعقيداً للفهم والإدارة.

في الممارسة العملية، يجب على مصممي قواعد البيانات موازنة هذه الاعتبارات. في بعض الأحيان يتم استخدام إلغاء التطبيع المُتحكم فيه لتحسين الأداء، وقبول بعض التكرار مقابل تقليل تعقيد الاستعلام.

### 10.5 دور القيود

حتى مع العلاقات المُطبّعة جيداً، يجب فرض قيود معينة للحفاظ على الاتساق:

**قيود النطاق**: التأكد من أن قيم الخصائص تأتي من النطاقات المناسبة

**قيود المفتاح**: التأكد من أن قيم المفتاح الأولي فريدة وغير فارغة

**سلامة المراجع**: التأكد من أن قيم المفتاح الخارجي تتطابق مع قيم المفتاح الأولي في العلاقات المشار إليها

يوفر النموذج العلائقي إطاراً للتعبير عن هذه القيود رسمياً، ويجب أن يفرضها نظام إدارة قواعد البيانات العلائقية تلقائياً.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** update anomaly, insertion anomaly, deletion anomaly, first normal form (1NF), second normal form (2NF), third normal form (3NF), BCNF, 4NF, 5NF, lossless decomposition, referential integrity, denormalization
- **Equations:** 0
- **Citations:** 0
- **Special handling:** Examples of normalization and decomposition provided

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.89
- Readability: 0.85
- Glossary consistency: 0.83
- **Overall section score:** 0.86
