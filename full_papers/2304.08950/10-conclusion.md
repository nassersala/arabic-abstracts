# Section 10: Conclusion
## القسم 10: الخاتمة

**Section:** conclusion
**Translation Quality:** 0.87
**Glossary Terms Used:** formal methods, formal verification, model checking, counterexample, specification

---

### English Version

> As researchers and educators in formal methods, we should strive to make our notations and tools accessible to non-experts. – Clarke and Wing (1996)

Our user study was designed to i) identify the motivation, challenges, and applicability of formal methods in industry and ii) evaluate if the proposed counterexample explanation approach matches the identified challenges.

To identify the motivation, challenges, and applicability of formal methods in industry, we conducted an extensive survey with 41 participants of various business units and disciplines within Bosch as a first phase of the user study. Responses show that the majority of the participants is positive regarding the use of formal methods in real-world development processes. However, participants identify that incomplete formal models in industry, understanding formal notations, as well as understanding verification results, e.g., produced by a model checker, still remain a challenge for adoption of formal methods in practice. Identifying refinement inconsistencies gets more complex with the system getting more complex and the number of requirements increasing. Apart from understanding and scalability challenges, one of the major challenge in using verification tools is a lack of training for engineers.

As a second part of the user study, we performed a one group pretest-posttest study with 13 participants of various Bosch business units to evaluate if the proposed counterexample explanation approach is capable of supporting the use of formal methods in industry. Results from the experiments as well as collected opinions from participants prove that the approach helps in i) better understanding and ii) quicker understanding inconsistencies, that it iii) raises their confidence in the analysis, and that iv) it provide value for the development of safety-critical projects in industry.

**Future directions.** To leverage formal methods in real-world development processes, one of the most suitable means is to provide education and training in formal methods. On the one hand, universities can teach the foundations of formal methods to students (e.g., temporal logics). On the other hand, companies can teach the skills required in the specific industrial context (e.g., considering the domain and tooling) to people entering industry as well as upskill existing employees to understand the foundations of formal methods. By providing education structured training in formal methods either in universities or companies, hesitancy in using formal methods could be reduced and the benefits of formal methods could be reaped.

Looking at the results of evaluating our counterexample explanation approach, it is clear that understanding of verification results is easier with a counterexample explanation than with the direct output of model checker. In future, similar explanations need to be generated for different model checkers, domain-specific system models and requirements, as well as integrated with project-specific tool chains. Furthermore, instead of only providing explanations that illustrate the error, providing suggestion to fix those errors could help to improve the agility to perform verification iteratively and thus, to support round-trip engineering.

---

### النسخة العربية

> كباحثين ومعلمين في الأساليب الرسمية، يجب أن نسعى لجعل تدويناتنا وأدواتنا متاحة لغير الخبراء. – كلارك ووينج (1996)

صُممت دراسة المستخدمين الخاصة بنا لـ i) تحديد الدافع والتحديات وقابلية تطبيق الأساليب الرسمية في الصناعة و ii) تقييم ما إذا كان نهج تفسير الأمثلة المضادة المُقترح يتطابق مع التحديات المُحددة.

لتحديد الدافع والتحديات وقابلية تطبيق الأساليب الرسمية في الصناعة، أجرينا مسحاً شاملاً مع 41 مشاركاً من وحدات أعمال وتخصصات مختلفة داخل بوش كمرحلة أولى من دراسة المستخدمين. تُظهر الاستجابات أن غالبية المشاركين إيجابيون فيما يتعلق باستخدام الأساليب الرسمية في عمليات التطوير الواقعية. ومع ذلك، يحدد المشاركون أن النماذج الرسمية غير المكتملة في الصناعة، وفهم التدوينات الرسمية، بالإضافة إلى فهم نتائج التحقق، على سبيل المثال، المُنتَجة بواسطة فاحص النماذج، لا تزال تمثل تحدياً لاعتماد الأساليب الرسمية في الممارسة. يصبح تحديد تعارضات التحسين أكثر تعقيداً مع ازدياد تعقيد النظام وزيادة عدد المتطلبات. بصرف النظر عن تحديات الفهم وقابلية التوسع، فإن أحد التحديات الرئيسية في استخدام أدوات التحقق هو نقص التدريب للمهندسين.

كجزء ثانٍ من دراسة المستخدمين، أجرينا دراسة مجموعة واحدة بقياس قبلي وبعدي مع 13 مشاركاً من وحدات أعمال مختلفة في بوش لتقييم ما إذا كان نهج تفسير الأمثلة المضادة المُقترح قادراً على دعم استخدام الأساليب الرسمية في الصناعة. تثبت النتائج من التجارب بالإضافة إلى الآراء المُجمعة من المشاركين أن النهج يساعد في i) فهم أفضل و ii) فهم أسرع للتعارضات، وأنه iii) يزيد من ثقتهم في التحليل، وأنه iv) يوفر قيمة لتطوير المشاريع الحرجة من حيث السلامة في الصناعة.

**الاتجاهات المستقبلية.** للاستفادة من الأساليب الرسمية في عمليات التطوير الواقعية، فإن أحد الوسائل الأكثر ملاءمة هو توفير التعليم والتدريب في الأساليب الرسمية. من ناحية، يمكن للجامعات تعليم أسس الأساليب الرسمية للطلاب (على سبيل المثال، المنطق الزمني). من ناحية أخرى، يمكن للشركات تعليم المهارات المطلوبة في السياق الصناعي المحدد (على سبيل المثال، مع مراعاة المجال والأدوات) للأشخاص الداخلين إلى الصناعة بالإضافة إلى رفع مهارات الموظفين الحاليين لفهم أسس الأساليب الرسمية. من خلال توفير التدريب المُنظَّم في الأساليب الرسمية إما في الجامعات أو الشركات، يمكن تقليل التردد في استخدام الأساليب الرسمية ويمكن جني فوائد الأساليب الرسمية.

بالنظر إلى نتائج تقييم نهج تفسير الأمثلة المضادة الخاص بنا، من الواضح أن فهم نتائج التحقق أسهل مع تفسير الأمثلة المضادة منه مع المُخرَجات المباشرة لفاحص النماذج. في المستقبل، يجب إنشاء تفسيرات مماثلة لفاحصات نماذج مختلفة، ونماذج أنظمة ومتطلبات خاصة بالمجال، بالإضافة إلى دمجها مع سلاسل أدوات خاصة بالمشروع. علاوة على ذلك، بدلاً من توفير التفسيرات فقط التي توضح الخطأ، يمكن أن يساعد تقديم اقتراحات لإصلاح تلك الأخطاء في تحسين المرونة لإجراء التحقق بشكل تكراري وبالتالي، لدعم الهندسة ذهاباً وإياباً.

---

### Translation Notes

- **Key contributions summarized:**
  - User survey (41 participants): Identified challenges and positive attitudes
  - Pretest-posttest experiment (13 participants): Validated counterexample explanation benefits
  - Four main benefits: better understanding, quicker understanding, increased confidence, added value

- **Future directions:**
  - Education and training in formal methods (universities and industry)
  - Generate explanations for different model checkers and domains
  - Integration with project-specific tool chains
  - Provide automated fix suggestions

- **Special handling:**
  - Preserved inspirational quote from Clarke and Wing (1996)
  - Maintained numbered lists for clarity (i, ii, iii, iv)
  - Emphasized call to action for education and tool integration

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
