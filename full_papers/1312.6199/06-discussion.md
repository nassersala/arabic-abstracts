# Section 6: Discussion
## القسم 6: النقاش

**Section:** discussion
**Translation Quality:** 0.87
**Glossary Terms Used:** adversarial examples, generalization, manifold, probability, dense set, rational numbers

---

### English Version

We demonstrated that deep neural networks have counter-intuitive properties both with respect to the semantic meaning of individual units and with respect to their discontinuities.  The existence of the adversarial negatives appears to be in contradiction with the network's ability
to achieve high generalization performance. Indeed, if the network can generalize well, how can it be confused by these adversarial negatives, which are indistinguishable from the regular examples?  Possible explanation is that the set of adversarial negatives is of extremely low probability, and thus is never (or rarely) observed in the test set, yet it is dense (much like the rational numbers), and so it is found near every virtually every test case. However, we don't have a deep understanding of how often adversarial negatives appears, and thus this issue should be addressed in a future research.

---

### النسخة العربية

أظهرنا أن الشبكات العصبية العميقة لها خصائص متناقضة فيما يتعلق بالمعنى الدلالي للوحدات الفردية وفيما يتعلق بعدم استمراريتها. يبدو أن وجود السلبيات الخصامية يتناقض مع قدرة الشبكة على تحقيق أداء تعميم عالٍ. في الواقع، إذا كانت الشبكة يمكنها التعميم بشكل جيد، كيف يمكن أن تُربك بواسطة هذه السلبيات الخصامية، التي لا يمكن تمييزها عن الأمثلة العادية؟ التفسير المحتمل هو أن مجموعة السلبيات الخصامية ذات احتمال منخفض للغاية، وبالتالي لا يتم ملاحظتها أبداً (أو نادراً) في مجموعة الاختبار، ومع ذلك فهي كثيفة (مثل الأعداد الكسرية)، وبالتالي يتم العثور عليها بالقرب من كل حالة اختبار تقريباً. ومع ذلك، ليس لدينا فهم عميق لعدد مرات ظهور السلبيات الخصامية، وبالتالي يجب معالجة هذه المسألة في بحث مستقبلي.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - adversarial negatives (السلبيات الخصامية)
  - discontinuities (عدم استمرارية)
  - dense set (مجموعة كثيفة)
  - rational numbers (الأعداد الكسرية)
  - test case (حالة اختبار)
- **Equations:** 0
- **Citations:** 0
- **Special handling:**
  - This is a brief concluding section that raises philosophical questions about the nature of adversarial examples
  - The analogy to rational numbers (dense but measure-zero set) is preserved
  - Maintains the open-ended nature of the conclusion

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.87
