# Section 6: Interdependencies
## القسم 6: الترابطات

**Section:** Interdependencies
**Translation Quality:** 0.85
**Glossary Terms Used:** functional dependency, multivalued dependency, join dependency, normalization

---

### English Version

## 6. INTERDEPENDENCIES

### 6.1 Functional Dependencies

A functional dependency is a constraint between two sets of attributes in a relation. We say that attribute set $Y$ is functionally dependent on attribute set $X$ (written $X \rightarrow Y$) if, whenever two tuples agree on their $X$ values, they must also agree on their $Y$ values.

For example, in an employee relation, salary is functionally dependent on employee number: if two tuples have the same employee number, they must have the same salary (assuming each employee has only one current salary).

Functional dependencies are important because:

1. They help identify keys: if $X \rightarrow \{all\ attributes\}$, then $X$ is a superkey
2. They reveal redundancy: if $X \rightarrow Y$ but $X$ is not a key, then the $Y$ values are redundantly stored
3. They guide normalization: functional dependencies determine what normal form a relation is in

### 6.2 Multivalued Dependencies

Multivalued dependencies are more complex than functional dependencies. A multivalued dependency exists when the presence of one attribute value determines a set of values for another attribute, independent of other attributes.

Formally, we say that $Y$ is multivalued dependent on $X$ (written $X \twoheadrightarrow Y$) if, for any two tuples that agree on $X$, we can swap their $Y$ values to produce two new tuples that must also be in the relation.

For example, suppose an employee can work on multiple projects and speak multiple languages. If we represent this in a single relation EMPLOYEE-PROJECT-LANGUAGE, we have multivalued dependencies: employee $\twoheadrightarrow$ project and employee $\twoheadrightarrow$ language. These are independent: the projects an employee works on have nothing to do with the languages they speak.

### 6.3 Join Dependencies

A join dependency is a generalization of multivalued dependencies. A relation $R$ satisfies a join dependency if it can be decomposed into relations $R_1, R_2, \ldots, R_n$ such that $R = R_1 * R_2 * \cdots * R_n$ (where $*$ denotes natural join).

Join dependencies are important for understanding when a relation can be decomposed without loss of information. They play a key role in defining higher normal forms.

### 6.4 Implications of Dependencies

Dependencies have implications—new dependencies can be derived from existing ones. The theory of dependency implication is important for:

- Database design: determining what dependencies hold
- Query optimization: using dependencies to simplify queries
- Integrity checking: verifying that updates preserve dependencies

Armstrong's axioms provide a complete set of inference rules for functional dependencies:

1. **Reflexivity**: If $Y \subseteq X$, then $X \rightarrow Y$
2. **Augmentation**: If $X \rightarrow Y$, then $XZ \rightarrow YZ$
3. **Transitivity**: If $X \rightarrow Y$ and $Y \rightarrow Z$, then $X \rightarrow Z$

From these basic rules, many other useful rules can be derived, such as the union and decomposition rules.

---

### النسخة العربية

## 6. الترابطات

### 6.1 التبعيات الوظيفية

التبعية الوظيفية (functional dependency) هي قيد بين مجموعتين من الخصائص في علاقة. نقول إن مجموعة الخصائص $Y$ تعتمد وظيفياً على مجموعة الخصائص $X$ (تُكتب $X \rightarrow Y$) إذا، كلما اتفق صفان على قيم $X$ الخاصة بهما، يجب أن يتفقا أيضاً على قيم $Y$ الخاصة بهما.

على سبيل المثال، في علاقة الموظفين، يعتمد الراتب وظيفياً على رقم الموظف: إذا كان لصفين نفس رقم الموظف، فيجب أن يكون لهما نفس الراتب (بافتراض أن كل موظف لديه راتب حالي واحد فقط).

التبعيات الوظيفية مهمة لأنها:

1. تساعد في تحديد المفاتيح: إذا كان $X \rightarrow \{جميع\ الخصائص\}$، فإن $X$ هو مفتاح فائق (superkey)
2. تكشف عن التكرار: إذا كان $X \rightarrow Y$ ولكن $X$ ليس مفتاحاً، فإن قيم $Y$ مخزنة بشكل متكرر
3. توجه التطبيع: تحدد التبعيات الوظيفية أي شكل طبيعي تكون العلاقة فيه

### 6.2 التبعيات متعددة القيم

التبعيات متعددة القيم (multivalued dependencies) أكثر تعقيداً من التبعيات الوظيفية. يوجد تبعية متعددة القيم عندما يحدد وجود قيمة خاصية واحدة مجموعة من القيم لخاصية أخرى، بشكل مستقل عن الخصائص الأخرى.

رسمياً، نقول إن $Y$ تعتمد متعدد القيم على $X$ (تُكتب $X \twoheadrightarrow Y$) إذا، لأي صفين يتفقان على $X$، يمكننا تبديل قيم $Y$ الخاصة بهما لإنتاج صفين جديدين يجب أن يكونا أيضاً في العلاقة.

على سبيل المثال، لنفترض أن موظفاً يمكنه العمل على مشاريع متعددة والتحدث بلغات متعددة. إذا مثلنا ذلك في علاقة واحدة EMPLOYEE-PROJECT-LANGUAGE، فلدينا تبعيات متعددة القيم: employee $\twoheadrightarrow$ project و employee $\twoheadrightarrow$ language. هذه مستقلة: المشاريع التي يعمل عليها الموظف لا علاقة لها باللغات التي يتحدث بها.

### 6.3 تبعيات الربط

تبعية الربط (join dependency) هي تعميم للتبعيات متعددة القيم. تفي العلاقة $R$ بتبعية ربط إذا كان يمكن تحليلها إلى علاقات $R_1, R_2, \ldots, R_n$ بحيث $R = R_1 * R_2 * \cdots * R_n$ (حيث $*$ يشير إلى الربط الطبيعي).

تبعيات الربط مهمة لفهم متى يمكن تحليل علاقة دون فقدان المعلومات. تلعب دوراً رئيسياً في تعريف الأشكال الطبيعية الأعلى.

### 6.4 انعكاسات التبعيات

التبعيات لها انعكاسات - يمكن اشتقاق تبعيات جديدة من التبعيات الموجودة. نظرية انعكاس التبعية مهمة لـ:

- تصميم قواعد البيانات: تحديد التبعيات التي تحتفظ بها
- تحسين الاستعلام: استخدام التبعيات لتبسيط الاستعلامات
- فحص السلامة: التحقق من أن التحديثات تحافظ على التبعيات

توفر بديهيات أرمسترونغ (Armstrong's axioms) مجموعة كاملة من قواعد الاستدلال للتبعيات الوظيفية:

1. **الانعكاسية**: إذا كان $Y \subseteq X$، فإن $X \rightarrow Y$
2. **التوسيع**: إذا كان $X \rightarrow Y$، فإن $XZ \rightarrow YZ$
3. **التعدية**: إذا كان $X \rightarrow Y$ و $Y \rightarrow Z$، فإن $X \rightarrow Z$

من هذه القواعد الأساسية، يمكن اشتقاق العديد من القواعد المفيدة الأخرى، مثل قواعد الاتحاد والتحليل.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** functional dependency, multivalued dependency, join dependency, superkey, Armstrong's axioms, reflexivity, augmentation, transitivity
- **Equations:** 4 (dependency notation)
- **Citations:** 0
- **Special handling:** Mathematical notation for dependencies preserved

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.88
- Readability: 0.84
- Glossary consistency: 0.82
- **Overall section score:** 0.85
