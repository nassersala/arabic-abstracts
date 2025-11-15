# Section 0: Abstract
## القسم 0: الملخص

**Section:** Abstract
**Translation Quality:** 0.89
**Glossary Terms Used:** monad, proof, proof assistant, termination, functional programming, verification, partiality, free monad, container

---

### English Version

One Monad to Prove Them All is a modern fairy tale about curiosity and perseverance, two important properties of a successful PhD student. We follow the PhD student Mona on her adventure of proving properties about Haskell programs in the proof assistant Coq.

On the one hand, as a PhD student in computer science Mona observes an increasing demand for correct software products. In particular, because of the large amount of existing software, verifying existing software products becomes more important. Verifying programs in the functional programming language Haskell is no exception. On the other hand, Mona is delighted to see that communities in the area of theorem proving are becoming popular. Thus, Mona sets out to learn more about the interactive theorem prover Coq and verifying Haskell programs in Coq.

To prove properties about a Haskell function in Coq, Mona has to translate the function into Coq code. As Coq programs have to be total and Haskell programs are often not, Mona has to model partiality explicitly in Coq. In her quest for a solution Mona finds an ancient manuscript that explains how properties about Haskell functions can be proven in the proof assistant Agda by translating Haskell programs into monadic Agda programs. By instantiating the monadic program with a concrete monad instance the proof can be performed in either a total or a partial setting. Mona discovers that the proposed transformation does not work in Coq due to a restriction in the termination checker. In fact the transformation does not work in Agda anymore as well, as the termination checker in Agda has been improved.

We follow Mona on an educational journey through the land of functional programming where she learns about concepts like free monads and containers as well as basics and restrictions of proof assistants like Coq. These concepts are well-known individually, but their interplay gives rise to a solution for Mona's problem based on the originally proposed monadic transformation that has not been presented before. When Mona starts to test her approach by proving a statement about simple Haskell functions, she realizes that her approach has an additional advantage over the original idea in Agda. Mona's final solution not only works for a specific monad instance but even allows her to prove monad-generic properties. Instead of proving properties over and over again for specific monad instances she is able to prove properties that hold for all monads representable by a container-based instance of the free monad. In order to strengthen her confidence in the practicability of her approach, Mona evaluates her approach in a case study that compares two implementations for queues. In order to share the results with other functional programmers the fairy tale is available as a literate Coq file.

---

### النسخة العربية

موناد واحد لإثباتها جميعاً هي حكاية خرافية حديثة عن الفضول والمثابرة، وهما خاصيتان مهمتان لطالب دكتوراه ناجح. نتابع طالبة الدكتوراه مونا في مغامرتها لإثبات خصائص برامج Haskell باستخدام مساعد البرهان Coq.

من ناحية، كطالبة دكتوراه في علوم الحاسوب تلاحظ مونا طلباً متزايداً على منتجات برمجية صحيحة. وعلى وجه الخصوص، بسبب الكمية الكبيرة من البرمجيات الموجودة، يصبح التحقق من المنتجات البرمجية الموجودة أكثر أهمية. التحقق من البرامج في لغة البرمجة الوظيفية Haskell ليس استثناءً. من ناحية أخرى، تسعد مونا برؤية أن المجتمعات في مجال إثبات النظريات أصبحت شائعة. لذلك، تشرع مونا في تعلم المزيد عن مُثبِّت النظريات التفاعلي Coq والتحقق من برامج Haskell في Coq.

لإثبات خصائص حول دالة Haskell في Coq، يجب على مونا ترجمة الدالة إلى شفرة Coq. نظراً لأن برامج Coq يجب أن تكون كاملة وبرامج Haskell غالباً ما لا تكون كذلك، يجب على مونا نمذجة الجزئية بشكل صريح في Coq. في سعيها للحصول على حل تجد مونا مخطوطة قديمة تشرح كيف يمكن إثبات خصائص دوال Haskell في مساعد البرهان Agda من خلال ترجمة برامج Haskell إلى برامج Agda موناديّة. من خلال تحديد نموذج موناد محدد، يمكن إجراء البرهان في إعداد كامل أو جزئي. تكتشف مونا أن التحويل المقترح لا يعمل في Coq بسبب قيد في مدقق الإنهاء. في الواقع، التحويل لم يعد يعمل في Agda أيضاً، حيث تم تحسين مدقق الإنهاء في Agda.

نتابع مونا في رحلة تعليمية عبر أرض البرمجة الوظيفية حيث تتعلم عن مفاهيم مثل الموناد الحر والحاويات بالإضافة إلى أساسيات وقيود مساعدي البرهان مثل Coq. هذه المفاهيم معروفة بشكل فردي، لكن تفاعلها يؤدي إلى حل لمشكلة مونا استناداً إلى التحويل الموناديّ المقترح في الأصل والذي لم يتم تقديمه من قبل. عندما تبدأ مونا في اختبار نهجها من خلال إثبات عبارة حول دوال Haskell بسيطة، تدرك أن نهجها له ميزة إضافية على الفكرة الأصلية في Agda. حل مونا النهائي لا يعمل فقط لنموذج موناد محدد ولكنه يسمح لها حتى بإثبات خصائص عامة للموناد. بدلاً من إثبات الخصائص مراراً وتكراراً لنماذج موناد محددة، فهي قادرة على إثبات خصائص تنطبق على جميع الموناد القابلة للتمثيل بنموذج قائم على الحاويات من الموناد الحر. من أجل تعزيز ثقتها في قابلية تطبيق نهجها، تقيّم مونا نهجها في دراسة حالة تقارن تطبيقين لقوائم الانتظار. من أجل مشاركة النتائج مع مبرمجين وظيفيين آخرين، الحكاية الخرافية متاحة كملف Coq أدبي.

---

### Translation Notes

- **Key Terms:**
  - "monad" → "موناد" (transliterated as it's a technical term)
  - "proof assistant" → "مساعد البرهان"
  - "partiality" → "الجزئية"
  - "termination checker" → "مدقق الإنهاء"
  - "free monad" → "الموناد الحر"
  - "container" → "حاوية"
  - "literate Coq file" → "ملف Coq أدبي" (literate programming style)

- **Narrative Style:** The abstract maintains the fairy tale framing ("modern fairy tale", "ancient manuscript", "educational journey") which adds an engaging educational dimension to the technical content.

- **Technical Accuracy:** The translation preserves all technical details about the transformation from Haskell to Coq, the problem with termination checkers, and the solution using free monads and containers.

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.92
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.89
