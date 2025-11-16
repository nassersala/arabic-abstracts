# Section 9: Conclusion
## القسم 9: الخاتمة

**Section:** Conclusion
**Translation Quality:** 0.87
**Glossary Terms Used:** formal methods (الأساليب الرسمية), formal verification (التحقق الرسمي), specification (مواصفة), requirements (متطلبات), safety-critical (حرجة من حيث السلامة)

---

### English Version

During analysis several smaller deficiencies were discovered in the low-level requirements. The formalization of natural language requirements into ACSL is an excellent tool to "debug" specifications and to improve their quality. Moreover, the formalization helps to achieve many of the DO-178C objectives related to LLR.

At this time of writing, we recommend to use ACSL and Frama-C only in highly safety critical applications and even there only in areas that need extra scrutiny. And even so, the team must be supported by an experienced consultant for both tool and method who can provide immediate assistance in case specification or verification problems occur. We also suggest to collect and publish a set of specification patterns or best practices similar to those for Z [17, 19].

If formal specification is used, then additional rules must be added to the software design and coding standards in order to facilitate formal verification. Such rules would include the reduction of the call hierarchy, the reduction of internal state where possible and the increase of parameter passing as main method of data flow. The decision to use ACSL for specification and verification will shape the software design and coding practice.

Since formal methods have made their way into aviation standards and guidelines it is to be expected that they will be mandated in certain areas in the future, if not by the certification authorities, then by major aerospace companies like Airbus and Dassault. Since the WP plugin did not fully implement the ACSL language standard at the time of the experiment, we also recommend to observe the further development and to repeat this study in one or two years.

---

### النسخة العربية

خلال التحليل، تم اكتشاف عدة أوجه قصور أصغر في المتطلبات منخفضة المستوى. إن الصياغة الرسمية لمتطلبات اللغة الطبيعية في ACSL هي أداة ممتازة "لتصحيح أخطاء" المواصفات وتحسين جودتها. علاوة على ذلك، تساعد الصياغة الرسمية في تحقيق العديد من أهداف DO-178C المتعلقة بالمتطلبات منخفضة المستوى.

في وقت كتابة هذا، نوصي باستخدام ACSL و Frama-C فقط في التطبيقات شديدة الحرجة من حيث السلامة وحتى هناك فقط في المجالات التي تحتاج إلى فحص إضافي. وحتى في هذه الحالة، يجب أن يحظى الفريق بدعم من مستشار ذي خبرة لكل من الأداة والطريقة يمكنه تقديم مساعدة فورية في حالة حدوث مشاكل في المواصفة أو التحقق. نقترح أيضاً جمع ونشر مجموعة من أنماط المواصفات أو أفضل الممارسات المشابهة لتلك الخاصة بـ Z [17، 19].

إذا تم استخدام المواصفة الرسمية، فيجب إضافة قواعد إضافية إلى معايير تصميم وترميز البرمجيات من أجل تسهيل التحقق الرسمي. ستشمل هذه القواعد تقليل التسلسل الهرمي للاستدعاءات، وتقليل الحالة الداخلية حيثما أمكن، وزيادة تمرير المعاملات كطريقة رئيسية لتدفق البيانات. سيشكل قرار استخدام ACSL للمواصفة والتحقق ممارسة تصميم وترميز البرمجيات.

بما أن الأساليب الرسمية شقت طريقها إلى معايير وإرشادات الطيران، فمن المتوقع أن يتم فرضها في مجالات معينة في المستقبل، إن لم يكن من قبل سلطات الاعتماد، فمن قبل شركات الفضاء الجوي الكبرى مثل Airbus و Dassault. نظراً لأن إضافة WP لم تنفذ معيار لغة ACSL بالكامل في وقت التجربة، نوصي أيضاً بمراقبة التطور الإضافي وتكرار هذه الدراسة في سنة أو سنتين.

---

### Translation Notes

- **Key Terms:**
  - Deficiencies: أوجه قصور
  - Debug: تصحيح أخطاء
  - Extra scrutiny: فحص إضافي
  - Experienced consultant: مستشار ذي خبرة
  - Immediate assistance: مساعدة فورية
  - Specification patterns: أنماط المواصفات
  - Best practices: أفضل الممارسات
  - Design standards: معايير التصميم
  - Coding standards: معايير الترميز
  - Call hierarchy: التسلسل الهرمي للاستدعاءات
  - Internal state: الحالة الداخلية
  - Parameter passing: تمرير المعاملات
  - Data flow: تدفق البيانات
  - Aviation standards: معايير الطيران
  - Certification authorities: سلطات الاعتماد
  - Aerospace companies: شركات الفضاء الجوي

- **Citations:** [17], [19]

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-Translation Sample (First Paragraph)

"During the analysis, several smaller deficiencies were discovered in the low-level requirements. The formal formulation of natural language requirements in ACSL is an excellent tool for 'debugging' specifications and improving their quality. Moreover, the formal formulation helps achieve many of the DO-178C objectives related to low-level requirements."

**Back-translation Assessment:** Excellent - preserves all key information and technical meaning.
