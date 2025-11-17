# Section 6: Conclusion
## القسم 6: الخاتمة

**Section:** conclusion
**Translation Quality:** 0.87
**Glossary Terms Used:** dependent types, property-based testing, type checker, model checking, stateful systems, proof system

---

### English Version

We successfully implemented QuickCheck in Idris2 and demonstrated how it can be extended to generate arbitrary instances of dependent types. We then highlighted how dependent types allow us to model stateful systems, that these models are tricky to get right, and how we can use QuickCheck at the type-level to automatically detect this and help us fix it. Finally, we generalised the type-level framework to support any stateful system, and demonstrated its usefulness by modelling, implementing, and testing a network protocol. Our approach is not a proof system, however it should help prototype specifications and models faster, gaining confidence that the current system is sound, before potentially choosing to model check or to formalise and prove it. We believe that our generalisation is low-friction enough for wider adoption and are excited to see what this may lead to.

## Acknowledgments

We are grateful to the anonymous reviewers who took the time to carefully read through the paper and write detailed and insightful feedback, including ideas for how to improve the code, many of which were incorporated into this final version. We are also grateful for the support of EPSRC grant EP/T007265/1.

---

### النسخة العربية

نجحنا في تطبيق QuickCheck في Idris2 وأظهرنا كيف يمكن توسيعه لتوليد حالات تعسفية من الأنواع التابعة. ثم سلطنا الضوء على كيفية السماح للأنواع التابعة بنمذجة الأنظمة ذات الحالات، وأن هذه النماذج صعبة لتصحيحها، وكيف يمكننا استخدام QuickCheck على مستوى الأنواع لاكتشاف ذلك تلقائياً ومساعدتنا على إصلاحه. أخيراً، عممنا إطار العمل على مستوى الأنواع لدعم أي نظام ذو حالات، وأظهرنا فائدته من خلال نمذجة وتطبيق واختبار بروتوكول شبكة. نهجنا ليس نظام برهان، ومع ذلك يجب أن يساعد في إنشاء نماذج أولية للمواصفات والنماذج بشكل أسرع، واكتساب الثقة بأن النظام الحالي سليم، قبل أن نختار ربما فحص النموذج أو إضفاء الطابع الرسمي عليه وإثباته. نعتقد أن تعميمنا منخفض الاحتكاك بما يكفي للاعتماد على نطاق أوسع ونحن متحمسون لرؤية ما قد يؤدي إليه ذلك.

## شكر وتقدير

نحن ممتنون للمراجعين المجهولين الذين أخذوا الوقت لقراءة الورقة بعناية وكتابة ملاحظات مفصلة وثاقبة، بما في ذلك أفكار لتحسين الشفرة، والتي تم دمج الكثير منها في هذا الإصدار النهائي. نحن ممتنون أيضاً لدعم منحة EPSRC EP/T007265/1.

---

### Translation Notes

- **Key terms:**
  - QuickCheck implementation - تطبيق QuickCheck
  - Arbitrary instances - حالات تعسفية
  - Proof system - نظام برهان
  - Prototype specifications - مواصفات نموذج أولي
  - Low-friction - منخفض الاحتكاك

- **Special handling:** Acknowledgments section, grant reference

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.86
- **Overall section score:** 0.87
