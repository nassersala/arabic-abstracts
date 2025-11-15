# Section 1: Introduction
## القسم 1: المقدمة

**Section:** Introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** database, data structure, data independence, hierarchical, network, relational, model, query, application

---

### English Version

## 1. INTRODUCTION

This paper is concerned with the application of elementary relation theory to systems which provide shared access to large banks of formatted data. Except for a paper by Childs [1], the principal application of relations to data systems has been to deductive question-answering systems. Levien and Maron [2] provide numerous references to work in this area.

In contrast, the problems treated here are those of data independence—the independence of application programs and terminal activities from growth in data types and changes in data representation—and certain kinds of data inconsistency which are expected to become troublesome even in nondeductive systems.

In order to set the stage for our discussion of the relational model, we shall first describe in greater detail the problems—especially those of data independence and consistency—which have motivated this work. As we shall see, there are several kinds of independence.

### 1.1 Data Independence

A serious problem with existing data systems is that the application programs which access the data are dependent not only on the logical structure of the data they access, but also upon the following details:
1. The ordering of the data as stored in the computer;
2. The indexing;
3. The access paths.

Any one of these may be changed for a variety of reasons such as performance improvement. If the data is physically stored in a different order, if a new index is added, or if an access path is changed, all the application programs which formerly worked must be changed. This is an extremely expensive proposition.

A second and rather serious problem arises from the fact that most data access languages are dependent upon the conceptual model of the data. If the conceptual model changes—if the way the users think about the data changes—then the data access language itself must change.

The provision of data independence is a principal goal of relational model of data.

### 1.2 Consistency

The problems of consistency are closely related to those of redundancy. In many large data banks, redundancy is both prevalent and unavoidable. While deliberate redundancy in data has the advantage that it makes the system more resilient (since data is not lost when one file is damaged), there are several disadvantages:
1. It takes more storage space;
2. It takes more time to update redundantly stored data;
3. If not all the redundant data is updated at the same time, the system becomes inconsistent.

The third point is of particular interest. Because of the cost in time and storage space to update redundantly stored data, such updates are often deferred. This means that during the interval between updates the data bank contains some information which is out of date.

The relational model provides a means of describing data with its natural structure only—that is, without superimposing any additional structure for machine representation purposes. Accordingly, it provides a basis for a high level data language which will yield maximal independence between programs on the one hand and machine representation and organization of data on the other.

---

### النسخة العربية

## 1. المقدمة

تتعلق هذه الورقة بتطبيق نظرية العلاقات الأولية على الأنظمة التي توفر وصولاً مشتركاً إلى بنوك كبيرة من البيانات المنسقة. باستثناء ورقة تشايلدز [1]، كان التطبيق الرئيسي للعلاقات على أنظمة البيانات في أنظمة الإجابة على الأسئلة الاستنتاجية. يقدم ليفين ومارون [2] مراجع عديدة للأعمال في هذا المجال.

على النقيض من ذلك، فإن المشاكل التي يتم التعامل معها هنا هي مشاكل استقلالية البيانات - استقلالية برامج التطبيقات وأنشطة الطرفيات عن النمو في أنواع البيانات والتغييرات في تمثيل البيانات - وأنواع معينة من عدم اتساق البيانات التي من المتوقع أن تصبح مزعجة حتى في الأنظمة غير الاستنتاجية.

من أجل تهيئة المسرح لمناقشتنا للنموذج العلائقي، سنقوم أولاً بوصف المشاكل بمزيد من التفصيل - وخاصة تلك المتعلقة باستقلالية البيانات والاتساق - التي حفزت هذا العمل. كما سنرى، هناك عدة أنواع من الاستقلالية.

### 1.1 استقلالية البيانات

تتمثل المشكلة الخطيرة في أنظمة البيانات الموجودة في أن برامج التطبيقات التي تصل إلى البيانات تعتمد ليس فقط على البنية المنطقية للبيانات التي تصل إليها، ولكن أيضاً على التفاصيل التالية:
1. ترتيب البيانات كما هي مخزنة في الحاسوب؛
2. الفهرسة؛
3. مسارات الوصول.

يمكن تغيير أي من هذه العناصر لأسباب متنوعة مثل تحسين الأداء. إذا تم تخزين البيانات فعلياً بترتيب مختلف، أو إذا تمت إضافة فهرس جديد، أو إذا تم تغيير مسار الوصول، فيجب تغيير جميع برامج التطبيقات التي كانت تعمل سابقاً. هذا مقترح مكلف للغاية.

تنشأ المشكلة الثانية والخطيرة إلى حد ما من حقيقة أن معظم لغات الوصول إلى البيانات تعتمد على النموذج المفاهيمي للبيانات. إذا تغير النموذج المفاهيمي - إذا تغيرت الطريقة التي يفكر بها المستخدمون في البيانات - فيجب أن تتغير لغة الوصول إلى البيانات نفسها.

يُعد توفير استقلالية البيانات هدفاً رئيسياً للنموذج العلائقي للبيانات.

### 1.2 الاتساق

ترتبط مشاكل الاتساق ارتباطاً وثيقاً بمشاكل التكرار. في العديد من بنوك البيانات الكبيرة، يكون التكرار سائداً ولا مفر منه. في حين أن التكرار المتعمد في البيانات له ميزة أنه يجعل النظام أكثر مرونة (نظراً لأن البيانات لا تُفقد عند تلف ملف واحد)، إلا أن هناك عدة عيوب:
1. يستهلك مساحة تخزين أكبر؛
2. يستغرق وقتاً أطول لتحديث البيانات المخزنة بشكل متكرر؛
3. إذا لم يتم تحديث جميع البيانات المتكررة في نفس الوقت، يصبح النظام غير متسق.

النقطة الثالثة ذات أهمية خاصة. بسبب التكلفة في الوقت ومساحة التخزين لتحديث البيانات المخزنة بشكل متكرر، غالباً ما يتم تأجيل هذه التحديثات. وهذا يعني أنه خلال الفترة الفاصلة بين التحديثات، يحتوي بنك البيانات على بعض المعلومات التي أصبحت قديمة.

يوفر النموذج العلائقي وسيلة لوصف البيانات ببنيتها الطبيعية فقط - أي دون فرض أي بنية إضافية لأغراض التمثيل الآلي. وبناءً عليه، فإنه يوفر أساساً للغة بيانات عالية المستوى التي ستحقق أقصى استقلالية بين البرامج من جهة وتمثيل البيانات وتنظيمها في الآلة من جهة أخرى.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** data independence, consistency, redundancy, relational model, access paths, indexing
- **Equations:** 0
- **Citations:** [1] Childs, [2] Levien and Maron
- **Special handling:** Technical database terminology preserved with Arabic equivalents

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
