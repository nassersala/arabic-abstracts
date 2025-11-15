# Section 9: Final Comments
## القسم 9: تعليقات ختامية

**Section:** final comments
**Translation Quality:** 0.87
**Glossary Terms Used:** theorem, proof, computability, halting problem

---

### English Version

The exposition here does not follow Gödel's original proof, and while the exposition is my own, the general approach reflects (more and less) the contemporary computer-sciencey way that Gödel's theorem is thought about, i.e., via computability. In coming to this exposition for undergraduates, I must acknowledge the discussion of Gödel's theorems in Scott Aaronson's book *Quantum Computing Since Democritus*, and an exposition shown to me by Christos Papadimitriou. Those are both shorter, aimed at a more advanced audience, and are based on the undecidability of Turing's Halting problem. I also thank David Doty for pointing out an incorrect definition in my first version of this exposition.

Second, I must state again that the variant of Gödel's theorem proved here is weaker than what Gödel originally proved. In this exposition, the formal proof system must be able to express any $\overline{f}$-statement, but Gödel's original proof only requires that the formal system be able to express statements about arithmetic (in fact, statements about arithmetic on integers only using addition and multiplication). This is a more limited domain, implying a stronger theorem. That difference partly explains why a proof of Gödel's original theorem is technically more demanding than the exposition here. Further, Gödel did not just prove the *existence* of a true statement that could not be derived (in any sufficiently rich, sound proof system), he demonstrated a *particular* statement with that property. But, I believe that the moral, cultural, mathematical, and philosophical impact of the variant of Gödels theorem proved here is comparable to that of Gödel's actual first incompleteness theorem. Many modern treatments of Gödel's theorem similarly reflect this view. Of course, some people disagree and insist that anything using the phrase "Gödel's theorem" must actually be the same as what Gödel proved. Although, Gödel did not actually prove what is generally stated as "Gödel's theorem", but only a weaker form of it--which was later strengthened by Rosser to become the classic "Gödel's theorem". Accordingly, some people call it the "Gödel-Rosser theorem".

---

### النسخة العربية

العرض هنا لا يتبع برهان غودل الأصلي، وبينما العرض خاص بي، فإن النهج العام يعكس (بدرجة أكبر أو أقل) الطريقة المعاصرة لعلوم الحاسوب في التفكير في نظرية غودل، أي، عبر القابلية للحوسبة. في الوصول إلى هذا العرض لطلاب المرحلة الجامعية، يجب أن أعترف بمناقشة نظريات غودل في كتاب سكوت آرونسون *الحوسبة الكمومية منذ ديموقريطس*، وعرض أظهره لي كريستوس بابادميتريو. كلاهما أقصر، موجه لجمهور أكثر تقدماً، ويستند إلى عدم قابلية حسم مسألة التوقف عند تورينغ. أشكر أيضاً ديفيد دوتي لإشارته إلى تعريف غير صحيح في النسخة الأولى من هذا العرض.

ثانياً، يجب أن أذكر مرة أخرى أن متغير نظرية غودل المثبت هنا أضعف مما أثبته غودل في الأصل. في هذا العرض، يجب أن يكون نظام البرهان الصوري قادراً على التعبير عن أي عبارة $\overline{f}$، لكن برهان غودل الأصلي يتطلب فقط أن يكون النظام الصوري قادراً على التعبير عن عبارات حول الحساب (في الواقع، عبارات حول الحساب على الأعداد الصحيحة باستخدام الجمع والضرب فقط). هذا مجال أكثر محدودية، مما يعني نظرية أقوى. هذا الاختلاف يفسر جزئياً لماذا برهان نظرية غودل الأصلية أكثر تطلباً تقنياً من العرض هنا. علاوة على ذلك، لم يثبت غودل فقط *وجود* عبارة صحيحة لا يمكن اشتقاقها (في أي نظام برهان غني بما يكفي وسليم)، بل أظهر عبارة *معينة* بتلك الخاصية. لكنني أعتقد أن التأثير الأخلاقي والثقافي والرياضي والفلسفي لمتغير نظرية غودل المثبت هنا قابل للمقارنة بتأثير نظرية عدم الاكتمال الأولى الفعلية لغودل. تعكس العديد من المعالجات الحديثة لنظرية غودل بالمثل هذا الرأي. بالطبع، يختلف بعض الناس ويصرون على أن أي شيء يستخدم عبارة "نظرية غودل" يجب أن يكون فعلياً نفس ما أثبته غودل. على الرغم من أن غودل لم يثبت فعلياً ما يُذكر عموماً على أنه "نظرية غودل"، بل فقط شكل أضعف منها--والذي تم تقويته لاحقاً بواسطة روسر ليصبح "نظرية غودل" الكلاسيكية. وفقاً لذلك، يسميها بعض الناس "نظرية غودل-روسر".

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** Gödel-Rosser theorem (نظرية غودل-روسر), arithmetic (الحساب)
- **Equations:** 0
- **Citations:** References to Scott Aaronson's book "Quantum Computing Since Democritus", Christos Papadimitriou, David Doty, Rosser's work
- **Special handling:** The author's acknowledgments and reflections on the limitations of the proof are preserved

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
