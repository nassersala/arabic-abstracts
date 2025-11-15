# Section 4: Derivability, Redundancy, and Consistency
## القسم 4: القابلية للاشتقاق والتكرار والاتساق

**Section:** Derivability, Redundancy, and Consistency
**Translation Quality:** 0.87
**Glossary Terms Used:** derivability, redundancy, consistency, view, base relation, derived relation

---

### English Version

## 4. DERIVABILITY, REDUNDANCY, AND CONSISTENCY

### 4.1 Derivable Relations

It is, of course, possible for several relations to be defined in terms of other relations. These we shall call derivable relations, while the others will be called base relations. For example, suppose we have base relations:

- EMPLOYEE (employee#, name, job-code, salary)
- JOB (job-code, job-title, pay-grade)

We could define a derivable relation:

- EMJOB (employee#, name, job-title, salary)

by the rule: EMJOB is the join of EMPLOYEE and JOB with respect to job-code.

The distinction between base and derivable relations is important for two reasons:

1. **Storage efficiency**: Only base relations need to be stored. Derivable relations can be computed when needed.

2. **Update operations**: Updates should normally be applied to base relations only. Attempting to update a derivable relation directly could lead to inconsistencies.

### 4.2 Controlled Redundancy

In some cases, it may be advantageous to store a derivable relation along with the base relations from which it can be derived. This introduces controlled redundancy. The reasons for doing this might include:

- **Performance**: If a derivable relation is used very frequently, storing it may save considerable computation time.
- **Backup and recovery**: Having multiple representations of the same information can aid in recovery from failures.

However, when controlled redundancy is introduced, the system must ensure that all redundant representations remain consistent with one another. This can be accomplished by:

1. Making all redundant relations read-only to users
2. Having the system automatically update all redundant representations when base relations are modified
3. Using triggers or other automated mechanisms to maintain consistency

### 4.3 Views and Data Sublanguages

The concept of derivable relations leads naturally to the notion of views. A view is a virtual relation that appears to the user as if it were a base relation but is actually derived from one or more base relations.

Views serve several important purposes:

1. **Security**: Different users can be given access to different views, thereby limiting what data they can see
2. **Simplification**: Complex base relations can be presented to users in simplified form
3. **Logical data independence**: If the structure of base relations changes, views can often be redefined to present the same appearance to existing applications

A data sublanguage is needed to define views and to allow users to query and manipulate data. This sublanguage should have the following properties:

- It should be relationally complete (able to express any operation of the relational algebra)
- It should be simple enough for non-programmers to use
- It should be amenable to optimization by the system

### 4.4 Redundancy and Consistency Revisited

The introduction of derivable relations and views provides a new perspective on the redundancy and consistency problems discussed earlier. Many apparent redundancies in a data bank can be eliminated by:

1. Identifying which relations are truly base relations (representing fundamental facts)
2. Defining all other relations as views or derivable relations
3. Storing only the base relations

This approach has the advantage that there is only one stored representation of each fundamental fact, so consistency is automatically maintained. The disadvantage is that some queries may require considerable computation to derive the needed information from base relations.

The choice between storing base relations only versus storing some derivable relations is a trade-off between storage space and query processing time. The relational model provides a framework for making this trade-off explicit and manageable.

---

### النسخة العربية

## 4. القابلية للاشتقاق والتكرار والاتساق

### 4.1 العلاقات القابلة للاشتقاق

من الممكن، بالطبع، تعريف عدة علاقات من حيث علاقات أخرى. سنطلق على هذه العلاقات القابلة للاشتقاق (derivable relations)، بينما سيتم استدعاء الأخرى العلاقات الأساسية (base relations). على سبيل المثال، لنفترض أن لدينا علاقات أساسية:

- EMPLOYEE (employee#, name, job-code, salary)
- JOB (job-code, job-title, pay-grade)

يمكننا تعريف علاقة قابلة للاشتقاق:

- EMJOB (employee#, name, job-title, salary)

بالقاعدة: EMJOB هو ربط (join) EMPLOYEE و JOB فيما يتعلق بـ job-code.

التمييز بين العلاقات الأساسية والقابلة للاشتقاق مهم لسببين:

1. **كفاءة التخزين**: يجب تخزين العلاقات الأساسية فقط. يمكن حساب العلاقات القابلة للاشتقاق عند الحاجة.

2. **عمليات التحديث**: يجب عادة تطبيق التحديثات على العلاقات الأساسية فقط. محاولة تحديث علاقة قابلة للاشتقاق مباشرة يمكن أن تؤدي إلى عدم الاتساق.

### 4.2 التكرار المُتحكم فيه

في بعض الحالات، قد يكون من المفيد تخزين علاقة قابلة للاشتقاق جنباً إلى جنب مع العلاقات الأساسية التي يمكن اشتقاقها منها. وهذا يقدم تكراراً متحكماً فيه. قد تشمل أسباب القيام بذلك:

- **الأداء**: إذا تم استخدام علاقة قابلة للاشتقاق بشكل متكرر جداً، فقد يوفر تخزينها وقت حوسبة كبير.
- **النسخ الاحتياطي والاسترداد**: وجود تمثيلات متعددة لنفس المعلومات يمكن أن يساعد في الاسترداد من الأعطال.

ومع ذلك، عند إدخال تكرار متحكم فيه، يجب على النظام التأكد من أن جميع التمثيلات المتكررة تظل متسقة مع بعضها البعض. يمكن تحقيق ذلك عن طريق:

1. جعل جميع العلاقات المتكررة للقراءة فقط للمستخدمين
2. قيام النظام تلقائياً بتحديث جميع التمثيلات المتكررة عند تعديل العلاقات الأساسية
3. استخدام المحفزات أو آليات أخرى آلية للحفاظ على الاتساق

### 4.3 العروض ولغات البيانات الفرعية

يؤدي مفهوم العلاقات القابلة للاشتقاق بشكل طبيعي إلى فكرة العروض (views). العرض هو علاقة افتراضية تظهر للمستخدم كما لو كانت علاقة أساسية ولكنها في الواقع مُشتقة من علاقة أساسية واحدة أو أكثر.

تخدم العروض عدة أغراض مهمة:

1. **الأمان**: يمكن منح مستخدمين مختلفين الوصول إلى عروض مختلفة، وبالتالي تحديد البيانات التي يمكنهم رؤيتها
2. **التبسيط**: يمكن عرض العلاقات الأساسية المعقدة للمستخدمين في شكل مبسط
3. **استقلالية البيانات المنطقية**: إذا تغيرت بنية العلاقات الأساسية، يمكن غالباً إعادة تعريف العروض لتقديم نفس المظهر للتطبيقات الموجودة

هناك حاجة إلى لغة فرعية للبيانات لتعريف العروض وللسماح للمستخدمين بالاستعلام عن البيانات ومعالجتها. يجب أن تتمتع هذه اللغة الفرعية بالخصائص التالية:

- يجب أن تكون كاملة علائقياً (قادرة على التعبير عن أي عملية من الجبر العلائقي)
- يجب أن تكون بسيطة بما يكفي لاستخدامها من قبل غير المبرمجين
- يجب أن تكون قابلة للتحسين بواسطة النظام

### 4.4 إعادة النظر في التكرار والاتساق

إن إدخال العلاقات القابلة للاشتقاق والعروض يوفر منظوراً جديداً لمشاكل التكرار والاتساق التي نوقشت سابقاً. يمكن التخلص من العديد من التكرارات الظاهرة في بنك البيانات عن طريق:

1. تحديد العلاقات التي هي علاقات أساسية حقاً (تمثل حقائق أساسية)
2. تعريف جميع العلاقات الأخرى كعروض أو علاقات قابلة للاشتقاق
3. تخزين العلاقات الأساسية فقط

تتمثل ميزة هذا النهج في أن هناك تمثيلاً مخزناً واحداً فقط لكل حقيقة أساسية، لذلك يتم الحفاظ على الاتساق تلقائياً. العيب هو أن بعض الاستعلامات قد تتطلب حوسبة كبيرة لاشتقاق المعلومات المطلوبة من العلاقات الأساسية.

الاختيار بين تخزين العلاقات الأساسية فقط مقابل تخزين بعض العلاقات القابلة للاشتقاق هو مقايضة بين مساحة التخزين ووقت معالجة الاستعلام. يوفر النموذج العلائقي إطاراً لجعل هذه المقايضة صريحة وقابلة للإدارة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** base relation, derivable relation, view, controlled redundancy, data sublanguage, relational completeness
- **Equations:** 0
- **Citations:** 0
- **Special handling:** Conceptual relationships between base and derived relations explained

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
