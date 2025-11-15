# Section 5: Operations on Relations
## القسم 5: العمليات على العلاقات

**Section:** Operations on Relations
**Translation Quality:** 0.89
**Glossary Terms Used:** projection, selection, join, union, intersection, difference, product, relational algebra

---

### English Version

## 5. OPERATIONS ON RELATIONS

The relational algebra is a collection of operations on relations. Each operation takes one or more relations as operands and produces a relation as its result. This closure property is important—it means that the output of one operation can serve as input to another.

### 5.1 Projection

The projection operation, denoted $\pi$, is used to select certain columns from a relation. If $R$ is a relation of degree $n$ and $i_1, i_2, \ldots, i_m$ are integers between 1 and $n$, then:

$$\pi_{i_1, i_2, \ldots, i_m}(R)$$

is the relation of degree $m$ obtained from $R$ by selecting the columns in positions $i_1, i_2, \ldots, i_m$. Duplicate tuples, if any, are removed from the result.

For example, if we have the employee relation shown earlier, then $\pi_{employee, salary}(EMPLOYEE)$ would give us a relation showing just the employee numbers and salaries.

### 5.2 Selection (Restriction)

The selection operation, denoted $\sigma$, is used to select certain rows from a relation based on some condition. If $R$ is a relation and $\phi$ is a condition (involving the attributes of $R$), then:

$$\sigma_\phi(R)$$

is the relation consisting of all tuples in $R$ which satisfy condition $\phi$.

For example, $\sigma_{salary > 13000}(EMPLOYEE)$ would give us all employees with salaries greater than 13000.

### 5.3 Join

The join operation combines related tuples from two relations into single tuples. There are several varieties of join, but the natural join is most important.

If $R$ and $S$ are relations with a common domain, the natural join $R * S$ consists of all combinations of tuples from $R$ and $S$ which agree on their common attributes.

More formally, suppose $R$ has attributes $A_1, A_2, \ldots, A_n, C_1, \ldots, C_k$ and $S$ has attributes $C_1, \ldots, C_k, B_1, \ldots, B_m$, where $C_1, \ldots, C_k$ are the common attributes. Then $R * S$ has attributes $A_1, \ldots, A_n, C_1, \ldots, C_k, B_1, \ldots, B_m$ and consists of all tuples $(a_1, \ldots, a_n, c_1, \ldots, c_k, b_1, \ldots, b_m)$ such that $(a_1, \ldots, a_n, c_1, \ldots, c_k) \in R$ and $(c_1, \ldots, c_k, b_1, \ldots, b_m) \in S$.

### 5.4 Union, Intersection, and Difference

These are the standard set operations applied to relations. For relations $R$ and $S$ with identical attributes:

- **Union** ($R \cup S$): Contains all tuples in $R$ or $S$ or both
- **Intersection** ($R \cap S$): Contains all tuples in both $R$ and $S$
- **Difference** ($R - S$): Contains all tuples in $R$ but not in $S$

These operations require that $R$ and $S$ be union-compatible, meaning they have the same degree and corresponding attributes have the same domains.

### 5.5 Product

The Cartesian product $R \times S$ of relations $R$ and $S$ is the set of all possible combinations of tuples from $R$ and $S$. If $R$ has degree $m$ and $S$ has degree $n$, then $R \times S$ has degree $m + n$.

The product operation is less frequently used directly, as the join operation is usually more appropriate. However, the product is theoretically important and can be used to define other operations.

### 5.6 Division

The division operation is useful for queries involving "for all" conditions. If $R$ has attributes $A_1, \ldots, A_n, B_1, \ldots, B_m$ and $S$ has attributes $B_1, \ldots, B_m$, then $R \div S$ is the relation with attributes $A_1, \ldots, A_n$ consisting of all tuples $(a_1, \ldots, a_n)$ such that for every tuple $(b_1, \ldots, b_m)$ in $S$, the tuple $(a_1, \ldots, a_n, b_1, \ldots, b_m)$ appears in $R$.

### 5.7 Completeness

A query language is said to be relationally complete if it is at least as powerful as the relational algebra—that is, if every query expressible in the relational algebra can be expressed in the language. This notion of completeness provides a standard for evaluating data sublanguages.

It is important to note that relational completeness does not mean the language can express every conceivable query. For example, queries involving transitive closure (such as "find all ancestors") generally cannot be expressed in pure relational algebra. However, relational completeness does provide a reasonable baseline of functionality.

---

### النسخة العربية

## 5. العمليات على العلاقات

الجبر العلائقي هو مجموعة من العمليات على العلاقات. تأخذ كل عملية علاقة واحدة أو أكثر كمعاملات وتنتج علاقة كنتيجة لها. خاصية الانغلاق هذه مهمة - فهي تعني أن مخرجات عملية واحدة يمكن أن تكون بمثابة مدخلات لعملية أخرى.

### 5.1 الإسقاط

عملية الإسقاط (projection)، المشار إليها بـ $\pi$، تُستخدم لتحديد أعمدة معينة من علاقة. إذا كانت $R$ علاقة من الدرجة $n$ و $i_1, i_2, \ldots, i_m$ أعداد صحيحة بين 1 و $n$، فإن:

$$\pi_{i_1, i_2, \ldots, i_m}(R)$$

هي العلاقة من الدرجة $m$ التي يتم الحصول عليها من $R$ عن طريق تحديد الأعمدة في المواضع $i_1, i_2, \ldots, i_m$. تتم إزالة الصفوف المكررة، إن وُجدت، من النتيجة.

على سبيل المثال، إذا كان لدينا علاقة الموظفين الموضحة سابقاً، فإن $\pi_{employee, salary}(EMPLOYEE)$ ستعطينا علاقة تظهر فقط أرقام الموظفين والرواتب.

### 5.2 التحديد (التقييد)

عملية التحديد (selection)، المشار إليها بـ $\sigma$، تُستخدم لتحديد صفوف معينة من علاقة بناءً على شرط ما. إذا كانت $R$ علاقة و $\phi$ شرط (يتضمن خصائص $R$)، فإن:

$$\sigma_\phi(R)$$

هي العلاقة التي تتكون من جميع الصفوف في $R$ التي تفي بالشرط $\phi$.

على سبيل المثال، $\sigma_{salary > 13000}(EMPLOYEE)$ ستعطينا جميع الموظفين ذوي الرواتب الأكبر من 13000.

### 5.3 الربط

تجمع عملية الربط (join) الصفوف المرتبطة من علاقتين في صفوف مفردة. هناك عدة أنواع من الربط، ولكن الربط الطبيعي (natural join) هو الأكثر أهمية.

إذا كانت $R$ و $S$ علاقتين بنطاق مشترك، فإن الربط الطبيعي $R * S$ يتكون من جميع تركيبات الصفوف من $R$ و $S$ التي تتفق على خصائصها المشتركة.

بشكل أكثر رسمية، لنفترض أن $R$ لها الخصائص $A_1, A_2, \ldots, A_n, C_1, \ldots, C_k$ و $S$ لها الخصائص $C_1, \ldots, C_k, B_1, \ldots, B_m$، حيث $C_1, \ldots, C_k$ هي الخصائص المشتركة. عندئذٍ $R * S$ لها الخصائص $A_1, \ldots, A_n, C_1, \ldots, C_k, B_1, \ldots, B_m$ وتتكون من جميع الصفوف $(a_1, \ldots, a_n, c_1, \ldots, c_k, b_1, \ldots, b_m)$ بحيث $(a_1, \ldots, a_n, c_1, \ldots, c_k) \in R$ و $(c_1, \ldots, c_k, b_1, \ldots, b_m) \in S$.

### 5.4 الاتحاد والتقاطع والفرق

هذه هي عمليات المجموعات القياسية المطبقة على العلاقات. بالنسبة للعلاقات $R$ و $S$ ذات الخصائص المتطابقة:

- **الاتحاد** ($R \cup S$): يحتوي على جميع الصفوف في $R$ أو $S$ أو كليهما
- **التقاطع** ($R \cap S$): يحتوي على جميع الصفوف في كل من $R$ و $S$
- **الفرق** ($R - S$): يحتوي على جميع الصفوف في $R$ وليس في $S$

تتطلب هذه العمليات أن تكون $R$ و $S$ متوافقتين للاتحاد، مما يعني أن لهما نفس الدرجة والخصائص المقابلة لها نفس النطاقات.

### 5.5 الجداء

الجداء الديكارتي $R \times S$ للعلاقات $R$ و $S$ هو مجموعة جميع التركيبات الممكنة من صفوف $R$ و $S$. إذا كانت $R$ من الدرجة $m$ و $S$ من الدرجة $n$، فإن $R \times S$ من الدرجة $m + n$.

نادراً ما تُستخدم عملية الجداء بشكل مباشر، حيث أن عملية الربط عادة ما تكون أكثر ملاءمة. ومع ذلك، فإن الجداء مهم من الناحية النظرية ويمكن استخدامه لتعريف عمليات أخرى.

### 5.6 القسمة

عملية القسمة (division) مفيدة للاستعلامات التي تتضمن شروط "لجميع". إذا كانت $R$ لها الخصائص $A_1, \ldots, A_n, B_1, \ldots, B_m$ و $S$ لها الخصائص $B_1, \ldots, B_m$، فإن $R \div S$ هي العلاقة ذات الخصائص $A_1, \ldots, A_n$ التي تتكون من جميع الصفوف $(a_1, \ldots, a_n)$ بحيث لكل صف $(b_1, \ldots, b_m)$ في $S$، يظهر الصف $(a_1, \ldots, a_n, b_1, \ldots, b_m)$ في $R$.

### 5.7 الاكتمال

يُقال إن لغة الاستعلام كاملة علائقياً إذا كانت على الأقل بنفس قوة الجبر العلائقي - أي إذا كان كل استعلام يمكن التعبير عنه في الجبر العلائقي يمكن التعبير عنه في اللغة. يوفر مفهوم الاكتمال هذا معياراً لتقييم اللغات الفرعية للبيانات.

من المهم ملاحظة أن الاكتمال العلائقي لا يعني أن اللغة يمكنها التعبير عن كل استعلام يمكن تصوره. على سبيل المثال، الاستعلامات التي تتضمن الإغلاق المتعدي (transitive closure) (مثل "العثور على جميع الأسلاف") بشكل عام لا يمكن التعبير عنها في الجبر العلائقي النقي. ومع ذلك، فإن الاكتمال العلائقي يوفر خط أساس معقول من الوظائف.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** projection, selection, join, union, intersection, difference, product, division, relational algebra, relational completeness, transitive closure
- **Equations:** 7 (relational algebra operations)
- **Citations:** 0
- **Special handling:** Mathematical notation for relational algebra operations preserved

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.92
- Readability: 0.88
- Glossary consistency: 0.86
- **Overall section score:** 0.89
