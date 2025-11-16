# Section 8: Conclusion
## القسم 8: الخاتمة

**Section:** conclusion
**Translation Quality:** 0.88
**Glossary Terms Used:** assurance case (حالة ضمان), formal methods (الأساليب الرسمية), verification (التحقق), ontology (أنطولوجيا), cyber-physical systems (الأنظمة السيبرانية الفيزيائية)

---

### English Version

We have presented Isabelle/SACM, a framework for mechanised assurance cases. We showed how SACM is embedded into Isabelle as an ontology, and provided an interactive assurance language that generates valid instances. We applied it to the production of part of the Tokeneer security case, including verification of one of the security functional requirements, and embedded these results into a mechanised assurance argument. Of a particular note, Isabelle/SACM enforce the usage of the formal ontological links which represent the relationships between the assurance arguments and their claims, a feature we inherit from Isabelle/DOF. Isabelle/SACM also combines features from Isabelle/HOL, Isabelle/DOF and SACM which results in a framework that allows the integration of formal methods and argument-based safety assurance cases.

In future work, we will consider the integration of assurance case pattern execution [9] into our framework, which facilitate their production. We will also complete the mechanisation of the TIS security case, including verification of the other five SFRs. In parallel with this, we are developing our verification framework, Isabelle/UTP [14] to support a variety of notations used in software engineering. We recently demonstrated formal verification facilities for a statechart-like notation [12], and are also working towards tools to support hybrid dynamical languages [13] like Modelica and Simulink. Our overarching goal is a comprehensive assurance framework supported by a variety of integrated formal methods in order to approach complex certification tasks for cyber-physical systems and autonomous robots.

---

### النسخة العربية

قدمنا Isabelle/SACM، إطاراً لحالات الضمان الآلية. أظهرنا كيف يتم تضمين SACM في Isabelle كأنطولوجيا، ووفرنا لغة ضمان تفاعلية تولد مثيلات صالحة. طبقناها على إنتاج جزء من حالة أمان Tokeneer، بما في ذلك التحقق من أحد متطلبات الأمان الوظيفية، وضمننا هذه النتائج في حجة ضمان مؤتمتة. من الجدير بالذكر على وجه الخصوص، يفرض Isabelle/SACM استخدام الروابط الأنطولوجية الرسمية التي تمثل العلاقات بين حجج الضمان وادعاءاتها، وهي ميزة نرثها من Isabelle/DOF. يجمع Isabelle/SACM أيضاً ميزات من Isabelle/HOL و Isabelle/DOF و SACM مما ينتج عنه إطار يسمح بتكامل الأساليب الرسمية وحالات ضمان السلامة القائمة على الحجج.

في العمل المستقبلي، سننظر في تكامل تنفيذ نمط حالة الضمان [9] في إطارنا، الذي يسهل إنتاجها. سنكمل أيضاً أتمتة حالة أمان TIS، بما في ذلك التحقق من SFRs الخمسة الأخرى. بالتوازي مع ذلك، نقوم بتطوير إطار التحقق الخاص بنا، Isabelle/UTP [14] لدعم مجموعة متنوعة من التدوينات المستخدمة في هندسة البرمجيات. أظهرنا مؤخراً مرافق التحقق الرسمي لتدوين شبيه بمخطط الحالات [12]، ونعمل أيضاً نحو أدوات لدعم اللغات الديناميكية الهجينة [13] مثل Modelica و Simulink. هدفنا الشامل هو إطار ضمان شامل مدعوم بمجموعة متنوعة من الأساليب الرسمية المتكاملة من أجل التعامل مع مهام الاعتماد المعقدة للأنظمة السيبرانية الفيزيائية والروبوتات المستقلة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Assurance case pattern execution (تنفيذ نمط حالة الضمان)
  - Statechart notation (تدوين مخطط الحالات)
  - Hybrid dynamical languages (اللغات الديناميكية الهجينة)
  - Modelica
  - Simulink
  - Autonomous robots (الروبوتات المستقلة)
- **Equations:** 0
- **Citations:** [9,12,13,14]
- **Special handling:**
  - System/language names (Modelica, Simulink) kept in English
  - Framework names (Isabelle/SACM, Isabelle/UTP, Isabelle/DOF, Isabelle/HOL) kept in English

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
