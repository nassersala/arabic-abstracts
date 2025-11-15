# Section 3: Consistency
## القسم 3: الاتساق

**Section:** Consistency
**Translation Quality:** 0.86
**Glossary Terms Used:** consistency, redundancy, data integrity, constraint, database

---

### English Version

## 3. CONSISTENCY

Two types of inconsistency are discussed in this section: those which can arise when the data bank is specifically set up or changed, and those which can develop during normal operations. Both types involve redundancy, but redundancy of different kinds.

### 3.1 Domain Constraints

If a relation has a domain which is supposed to be a subset of some other set, it is essential that this inclusion relationship be maintained. For example, suppose a parts relation includes a supplier number attribute, and a supplier relation exists with supplier number as the primary key. Then the values of supplier number appearing in the parts relation should be included in the set of values of supplier number appearing in the supplier relation. This is an example of what we shall call a domain constraint.

More generally, suppose we have two or more relations $R_1, R_2, \ldots, R_m$ and suppose that the $i$th domain of $R_1$ is constrained to be a subset of the $j$th domain of $R_2$. We can express this constraint formally as:

$$\pi_i(R_1) \subseteq \pi_j(R_2)$$

where $\pi_i$ denotes projection on the $i$th domain.

Enforcing domain constraints becomes necessary whenever insertions or deletions are made. When a new tuple is inserted into $R_1$, the system should check that the $i$th component of this tuple belongs to $\pi_j(R_2)$. Similarly, when a tuple is deleted from $R_2$, the system should check that the $j$th component of this tuple does not appear in $\pi_i(R_1)$ (or else appropriate action must be taken with respect to the dependent tuples in $R_1$).

### 3.2 Time-Varying Relations

In many applications, relations vary with time. At any instant there is a current value of each relation, and stored with this value are usually one or more past values. The problem of maintaining consistency is complicated by the presence of such time-varying relations.

Suppose, for example, that we have a relation giving the current salary of each employee and another relation giving the history of salary changes. It is essential that these two relations be consistent with one another. Specifically, the current salary in the first relation should be the same as the most recent salary in the history relation.

The usual approach to this problem is to insist that all updates be made through controlled procedures. The relational approach suggests an alternative: namely, that one of these redundant relations should be derivable from the other. In the example just given, the current salary relation could be derived from the salary history relation by taking, for each employee, the salary associated with the most recent date.

### 3.3 Interdependencies

Many organizations need to maintain data which is subject to various interdependencies. These interdependencies may take the form of functional dependencies or, more generally, multivalued dependencies.

A functional dependency exists when, for a given value of one attribute (or combination of attributes), there is exactly one corresponding value of another attribute. For example, in an employee relation, there is a functional dependency of salary on employee number (assuming each employee has exactly one current salary).

Multivalued dependencies are more complex and involve situations where, for a given value of one attribute, there may be a specific set of values of another attribute. The relational model provides a mathematical framework for expressing and enforcing such dependencies.

---

### النسخة العربية

## 3. الاتساق

يُناقش نوعان من عدم الاتساق في هذا القسم: تلك التي يمكن أن تنشأ عند إعداد بنك البيانات أو تغييره بشكل خاص، وتلك التي يمكن أن تتطور أثناء العمليات العادية. كلا النوعين يتضمنان التكرار، ولكن تكراراً من أنواع مختلفة.

### 3.1 قيود النطاق

إذا كانت العلاقة تحتوي على نطاق يُفترض أن يكون مجموعة فرعية من مجموعة أخرى، فمن الضروري الحفاظ على علاقة الاحتواء هذه. على سبيل المثال، لنفترض أن علاقة الأجزاء تتضمن خاصية رقم المورد، وتوجد علاقة الموردين مع رقم المورد كمفتاح أولي. عندئذٍ يجب أن تُدرج قيم رقم المورد التي تظهر في علاقة الأجزاء في مجموعة قيم رقم المورد التي تظهر في علاقة الموردين. هذا مثال على ما سنطلق عليه قيد النطاق (domain constraint).

بشكل أكثر عمومية، لنفترض أن لدينا علاقتين أو أكثر $R_1, R_2, \ldots, R_m$ ولنفترض أن النطاق الـ $i$-th من $R_1$ مقيد بأن يكون مجموعة فرعية من النطاق الـ $j$-th من $R_2$. يمكننا التعبير عن هذا القيد رسمياً على النحو التالي:

$$\pi_i(R_1) \subseteq \pi_j(R_2)$$

حيث $\pi_i$ يشير إلى الإسقاط على النطاق الـ $i$-th.

يصبح فرض قيود النطاق ضرورياً عند إجراء إدراجات أو حذف. عندما يتم إدراج صف جديد في $R_1$، يجب على النظام التحقق من أن المكون الـ $i$-th من هذا الصف ينتمي إلى $\pi_j(R_2)$. وبالمثل، عند حذف صف من $R_2$، يجب على النظام التحقق من أن المكون الـ $j$-th من هذا الصف لا يظهر في $\pi_i(R_1)$ (أو يجب اتخاذ إجراء مناسب فيما يتعلق بالصفوف التابعة في $R_1$).

### 3.2 العلاقات المتغيرة بمرور الوقت

في العديد من التطبيقات، تتغير العلاقات مع مرور الوقت. في أي لحظة، هناك قيمة حالية لكل علاقة، ومخزنة مع هذه القيمة عادة واحدة أو أكثر من القيم السابقة. تُعقّد مشكلة الحفاظ على الاتساق بوجود مثل هذه العلاقات المتغيرة بمرور الوقت.

لنفترض، على سبيل المثال، أن لدينا علاقة تعطي الراتب الحالي لكل موظف وعلاقة أخرى تعطي تاريخ تغييرات الرواتب. من الضروري أن تكون هاتان العلاقتان متسقتين مع بعضهما البعض. على وجه التحديد، يجب أن يكون الراتب الحالي في العلاقة الأولى هو نفس الراتب الأحدث في علاقة التاريخ.

النهج المعتاد لهذه المشكلة هو الإصرار على أن جميع التحديثات تتم من خلال إجراءات خاضعة للرقابة. يقترح النهج العلائقي بديلاً: وهو أن إحدى هذه العلاقات المتكررة يجب أن تكون قابلة للاشتقاق من الأخرى. في المثال المذكور للتو، يمكن اشتقاق علاقة الراتب الحالي من علاقة تاريخ الرواتب عن طريق أخذ، لكل موظف، الراتب المرتبط بالتاريخ الأحدث.

### 3.3 الترابطات

تحتاج العديد من المنظمات إلى الحفاظ على بيانات خاضعة لترابطات مختلفة. قد تتخذ هذه الترابطات شكل التبعيات الوظيفية (functional dependencies) أو، بشكل أكثر عمومية، التبعيات متعددة القيم (multivalued dependencies).

يوجد تبعية وظيفية عندما، لقيمة معينة لخاصية واحدة (أو مجموعة من الخصائص)، يكون هناك قيمة مقابلة واحدة بالضبط لخاصية أخرى. على سبيل المثال، في علاقة الموظفين، يوجد تبعية وظيفية للراتب على رقم الموظف (بافتراض أن كل موظف لديه راتب حالي واحد بالضبط).

التبعيات متعددة القيم أكثر تعقيداً وتتضمن حالات حيث، لقيمة معينة لخاصية واحدة، قد تكون هناك مجموعة محددة من قيم خاصية أخرى. يوفر النموذج العلائقي إطاراً رياضياً للتعبير عن هذه التبعيات وفرضها.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** domain constraint, functional dependency, multivalued dependency, projection, time-varying relations
- **Equations:** 1 (subset constraint using projection)
- **Citations:** 0
- **Special handling:** Mathematical notation for projection and subset operations preserved

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.89
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86
