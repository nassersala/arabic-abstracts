# Section 2: Relational Model and Normal Form
## القسم 2: النموذج العلائقي والشكل الطبيعي

**Section:** Relational Model and Normal Form
**Translation Quality:** 0.88
**Glossary Terms Used:** relation, domain, tuple, attribute, primary key, foreign key, normal form, normalization

---

### English Version

## 2. RELATIONAL MODEL AND NORMAL FORM

### 2.1 Terminology

The term relation is used here in its mathematical sense. Given sets $S_1, S_2, \ldots, S_n$ (not necessarily distinct), $R$ is a relation on these $n$ sets if it is a set of $n$-tuples each of which has its first element from $S_1$, its second element from $S_2$, and so on. We shall refer to $S_j$ as the $j$th domain of $R$. As defined above, $R$ is said to have degree $n$. Relations of degree 1 are often called unary, degree 2 binary, degree 3 ternary, and degree $n$ $n$-ary.

For expository reasons, we shall frequently make use of an array representation of relations, but it must be remembered that this particular representation is not an essential part of the relational view being expounded. An $n$-ary relation can be represented by a two-dimensional column-homogeneous array in which the entries in any given column are elements of a common domain. The ordering of rows is immaterial, and the columns are identified by an assigned name which indicates the role played by entries in that column. The column names are called attributes of the relation.

Consider the following example of a relation of degree 5 and cardinality 4:

```
employee  | job-code | job-title        | location | salary
----------|----------|------------------|----------|--------
Jones     | 260      | Programmer       | New York | 12000
Smith     | 261      | Analyst          | New York | 14000
Robinson  | 262      | Systems Analyst  | Boston   | 15000
Green     | 260      | Programmer       | Chicago  | 11000
```

The column headings are attributes. The rows correspond to tuples of the relation.

### 2.2 Normal Form

A relation whose domains are simple (non-decomposable) is said to be normalized, or equivalently, in normal form. We are concerned initially with normalized relations because they free the users of a data bank from certain problems (such as the need for sophisticated algorithms to locate information).

Suppose a relation $R$ is normalized and has an attribute $A$ whose values are required to be unique (that is, no two distinct tuples of $R$ have a common value for $A$). Then we call $A$ a primary key for $R$. A relation may have more than one primary key. In the example above, employee is the primary key.

Some relations have the property that they can be decomposed into other relations in such a way that the original relation can be recovered by taking combinations (joins) of the decomposed relations. When this can be done, we say that the original relation is in a higher normal form. Higher normal forms are defined to remove various forms of redundancy and anomalies in data.

### 2.3 Composition of Relations

A binary relation which associates every element in its first domain with exactly one element in its second domain is called a function. A function from domain $D_1$ to domain $D_2$ is usually denoted $f: D_1 \rightarrow D_2$.

When we have two relations $R$ and $S$ such that some domain of $R$ (say the $i$th) is equal to some domain of $S$ (say the $j$th), we may form the composition $R \circ S$ (pronounced "$R$ composed with $S$"). This composition is achieved by matching up (or joining) tuples of $R$ with tuples of $S$ whenever the $i$th component of an $R$-tuple equals the $j$th component of an $S$-tuple. The resulting tuples have all the components of both $R$-tuples and $S$-tuples with one of the duplicate matching components removed.

### 2.4 Keys

Suppose we have a collection of relations and we wish to organize the data in such a way that we can locate any piece of information starting from a minimal amount of given information. To do this efficiently, we need to designate certain attributes as keys.

A primary key for a relation is a combination of attributes with the property that, at every instant of time, no two distinct tuples have identical values for the attributes in the combination. If a relation has more than one primary key, one may be designated the principal primary key.

A foreign key is a set of attributes in one relation whose values are required to match values of the primary key in another relation. Foreign keys provide the mechanism for creating links between relations in the relational model.

---

### النسخة العربية

## 2. النموذج العلائقي والشكل الطبيعي

### 2.1 المصطلحات

يُستخدم مصطلح العلاقة هنا بمعناه الرياضي. إذا أُعطيت المجموعات $S_1, S_2, \ldots, S_n$ (ليست بالضرورة متمايزة)، فإن $R$ هي علاقة على هذه المجموعات الـ $n$ إذا كانت مجموعة من $n$-صفوف (tuples) يحتوي كل منها على عنصره الأول من $S_1$، وعنصره الثاني من $S_2$، وهكذا. سنشير إلى $S_j$ باعتبارها النطاق (domain) الـ $j$ للعلاقة $R$. كما هو محدد أعلاه، يُقال إن $R$ لها درجة $n$. غالباً ما تُسمى العلاقات من الدرجة 1 أحادية (unary)، والدرجة 2 ثنائية (binary)، والدرجة 3 ثلاثية (ternary)، والدرجة $n$ $n$-ارية.

لأسباب توضيحية، سنستخدم بشكل متكرر تمثيلاً مصفوفياً للعلاقات، ولكن يجب أن نتذكر أن هذا التمثيل المحدد ليس جزءاً أساسياً من الرؤية العلائقية التي يتم شرحها. يمكن تمثيل العلاقة $n$-ارية بواسطة مصفوفة ثنائية الأبعاد متجانسة الأعمدة حيث تكون الإدخالات في أي عمود معين عناصر من نطاق مشترك. ترتيب الصفوف غير مهم، ويتم تحديد الأعمدة بواسطة اسم مخصص يشير إلى الدور الذي تلعبه الإدخالات في ذلك العمود. تُسمى أسماء الأعمدة خصائص (attributes) العلاقة.

لنأخذ المثال التالي لعلاقة من الدرجة 5 والعددية (cardinality) 4:

```
employee  | job-code | job-title        | location | salary
----------|----------|------------------|----------|--------
Jones     | 260      | Programmer       | New York | 12000
Smith     | 261      | Analyst          | New York | 14000
Robinson  | 262      | Systems Analyst  | Boston   | 15000
Green     | 260      | Programmer       | Chicago  | 11000
```

عناوين الأعمدة هي الخصائص. تتوافق الصفوف مع صفوف (tuples) العلاقة.

### 2.2 الشكل الطبيعي

يُقال إن العلاقة التي نطاقاتها بسيطة (غير قابلة للتحليل) مُطبّعة (normalized)، أو بالتساوي، في الشكل الطبيعي (normal form). نحن معنيون في البداية بالعلاقات المُطبّعة لأنها تحرر مستخدمي بنك البيانات من مشاكل معينة (مثل الحاجة إلى خوارزميات متطورة لتحديد موقع المعلومات).

لنفترض أن العلاقة $R$ مُطبّعة ولها خاصية $A$ يُطلب أن تكون قيمها فريدة (أي لا يوجد صفان متمايزان في $R$ لهما قيمة مشتركة لـ $A$). عندئذٍ نسمي $A$ مفتاحاً أولياً (primary key) للعلاقة $R$. قد تحتوي العلاقة على أكثر من مفتاح أولي واحد. في المثال أعلاه، employee هو المفتاح الأولي.

بعض العلاقات لها خاصية أنه يمكن تحليلها إلى علاقات أخرى بطريقة يمكن من خلالها استرداد العلاقة الأصلية من خلال أخذ تركيبات (ربط - joins) للعلاقات المُحللة. عندما يمكن القيام بذلك، نقول إن العلاقة الأصلية في شكل طبيعي أعلى. يتم تعريف الأشكال الطبيعية الأعلى لإزالة أشكال مختلفة من التكرار والشذوذات في البيانات.

### 2.3 تركيب العلاقات

العلاقة الثنائية التي تربط كل عنصر في نطاقها الأول بعنصر واحد بالضبط في نطاقها الثاني تُسمى دالة. عادة ما يُرمز للدالة من النطاق $D_1$ إلى النطاق $D_2$ بالرمز $f: D_1 \rightarrow D_2$.

عندما يكون لدينا علاقتان $R$ و $S$ بحيث يكون بعض نطاق $R$ (لنقل الـ $i$-th) مساوياً لبعض نطاق $S$ (لنقل الـ $j$-th)، يمكننا تشكيل التركيب $R \circ S$ (يُنطق "$R$ المُركّب مع $S$"). يتم تحقيق هذا التركيب عن طريق مطابقة (أو ربط) صفوف $R$ مع صفوف $S$ كلما كان المكون الـ $i$-th من صف $R$ يساوي المكون الـ $j$-th من صف $S$. تحتوي الصفوف الناتجة على جميع مكونات كل من صفوف $R$ وصفوف $S$ مع إزالة أحد المكونات المتطابقة المكررة.

### 2.4 المفاتيح

لنفترض أن لدينا مجموعة من العلاقات ونريد تنظيم البيانات بطريقة تمكننا من تحديد موقع أي جزء من المعلومات بدءاً من حد أدنى من المعلومات المعطاة. للقيام بذلك بكفاءة، نحتاج إلى تعيين خصائص معينة كمفاتيح.

المفتاح الأولي للعلاقة هو مجموعة من الخصائص بخاصية أنه، في كل لحظة زمنية، لا يوجد صفان متمايزان لهما قيم متطابقة للخصائص في التركيبة. إذا كان للعلاقة أكثر من مفتاح أولي واحد، فقد يتم تعيين أحدها كالمفتاح الأولي الرئيسي.

المفتاح الخارجي (foreign key) هو مجموعة من الخصائص في علاقة واحدة يُطلب أن تتطابق قيمها مع قيم المفتاح الأولي في علاقة أخرى. توفر المفاتيح الخارجية الآلية لإنشاء روابط بين العلاقات في النموذج العلائقي.

---

### Translation Notes

- **Figures referenced:** One table example (employee relation)
- **Key terms introduced:** relation, domain, tuple, attribute, primary key, foreign key, normal form, cardinality, degree, composition, join
- **Equations:** Mathematical notation for relations, functions, and set theory
- **Citations:** 0
- **Special handling:** Mathematical notation preserved in LaTeX format, table structure maintained

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.91
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88
