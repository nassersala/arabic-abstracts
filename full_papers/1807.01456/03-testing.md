# Section 3: Lightweight Correctness: Property-based Testing
## القسم 3: الصحة الخفيفة الوزن: الاختبار القائم على الخصائص

**Section:** property-based-testing
**Translation Quality:** 0.88
**Glossary Terms Used:** property-based testing, formal methods, formal verification, correctness, algorithm, specification, theorem proving

---

### English Version

#### 3.1 Property-based testing introduced

In this section, we will address the correctness issue, in a top-down, or lightweight manner. Especially, we apply the method of property-based testing [1] to verify the correctness of our implementation. The idea is that one specifies the formal properties that the implemented algorithms and types must satisfy, and checks if they hold by testing them against randomly or exhaustively generated inputs. Although it is not as rigorous as a theorem proving, it still gives a guarantee of the correctness at high assurance, after repeating tests time after time.

**Code 5** presents the example specifications for algebraic programs. In Lines 1 through 4, `prop_division` states that the implementation of Q must satisfy the axioms of division ring. The `prop_passesSTest` function demand the result of `calcGroebnerBasis` to pass the S-test. The tester accepts the specifications above, generates a specified number of inputs (default: 100) and tests against them. If all the inputs satisfy the specifications, it successfully halts; otherwise, it reports counterexamples, which is useful while debugging.

#### 3.2 Discussion

There are several libraries for property-based testing adopting different strategies to generate inputs. For example, QuickCheck [1] generates inputs randomly, while SmallCheck [26] exhaustively enumerates inputs in the depth-increasing order. Even though there are other implementations of property-based testers in languages other than Haskell [11], it does not seem that it is applied in existing systems, such as Singular [9], JAS or DoCon.

By its generative nature, property-based testing has several drawbacks and pitfalls. First, evidently, it cannot assure the validity as rigorously as the formal theorem proving, unless the input space is finite. There are several pieces of research that combine formal theorem proving and computational algebra to rigorously certify correctness of implementations (for example, [24, 2]). These first formalise the theory of Gröbner basis in the constructive type-theory. Then, execute them within the host theorem proving language, or extract the program into other languages. However, by its nature, this approach requires everything to be proven formally. It is not so easy a task to prove the correctness of every part of a program, even with help from automatic provers. Even if one manages to finish the proof of the validity of some algorithm, when one wants to optimise it afterwards, then one must prove the "equivalence" or validity of that optimisation. Moreover, it is sometimes the case that the validity, or even termination, of the algorithm remains unknown when it is implemented; e.g. the correctness and termination of Faugère's F₅ [6] are proven very recently [25]. Furthermore, there is an obvious restriction that we can extract programs only into the languages supported by the theorem prover. We consider these conditions too restrictive, and decided to adopt theorem proving only in trivial arity arithmetic.

Secondly, if the algorithm has a bad time complexity, property-based tests can easily explode. Specifically, since Gröbner bases have double-exponential worst time complexity, randomly generated input can take much time to be processed. One might reduce the burden by combining randomised and enumerative generation strategies carefully, but there is still a possibility that there are small inputs which take much time. To avoid such a circumstance, one can reduce the number of inputs, however it also reduces the assurance of validity.

Finally, they are not so good at treating existential properties. Although SmallCheck provides the existential quantifier in its vocabulary, it just tries to find solutions up to a prescribed depth. If solutions are relatively "larger" than its inputs, this results in false-negative failures. For example, one can write the following specification that demands each element of the result of `calcGroebnerBasis` to be a member of the original ideal, however it does not work as expected.

In the above, `dot i g` denotes the "dot-product". As a workaround, we currently combine inter-process communication with property-based testing. More specifically, we invoke a reliable existing implementation, such as SINGULAR, inside the spec as follows. Thus, if the existential property in question is decidable and has an existing reliable implementation, then it might be better to call it inside specifications.

---

### النسخة العربية

#### 3.1 مقدمة للاختبار القائم على الخصائص

في هذا القسم، سنتناول مسألة الصحة، بطريقة من أعلى إلى أسفل، أو خفيفة الوزن. على وجه الخصوص، نطبق طريقة الاختبار القائم على الخصائص [1] للتحقق من صحة تطبيقنا. الفكرة هي أن المرء يحدد الخصائص الرسمية التي يجب أن تفي بها الخوارزميات والأنواع المُنفذة، ويتحقق مما إذا كانت صحيحة عن طريق اختبارها ضد مدخلات مُولدة عشوائياً أو بشكل شامل. على الرغم من أنه ليس صارماً كإثبات النظرية، إلا أنه لا يزال يعطي ضماناً للصحة بضمان عالٍ، بعد تكرار الاختبارات مراراً وتكراراً.

يقدم **الكود 5** مواصفات أمثلة للبرامج الجبرية. في الأسطر 1 حتى 4، تنص `prop_division` على أن تطبيق Q يجب أن يفي ببديهيات حلقة القسمة. تتطلب دالة `prop_passesSTest` أن تمر نتيجة `calcGroebnerBasis` باختبار S. يقبل المختبر المواصفات أعلاه، ويولد عدداً محدداً من المدخلات (افتراضياً: 100) ويختبرها. إذا كانت جميع المدخلات تفي بالمواصفات، فإنه يتوقف بنجاح؛ وإلا، فإنه يبلغ عن الأمثلة المضادة، وهو أمر مفيد أثناء التصحيح.

#### 3.2 مناقشة

هناك العديد من المكتبات للاختبار القائم على الخصائص تعتمد استراتيجيات مختلفة لتوليد المدخلات. على سبيل المثال، يولد QuickCheck [1] المدخلات عشوائياً، بينما يُعدد SmallCheck [26] المدخلات بشكل شامل بترتيب متزايد العمق. على الرغم من وجود تطبيقات أخرى لمختبري الخصائص في لغات أخرى غير Haskell [11]، لا يبدو أنها مُطبقة في الأنظمة الموجودة، مثل Singular [9] أو JAS أو DoCon.

بطبيعته التوليدية، يحتوي الاختبار القائم على الخصائص على عدة عيوب ومخاطر. أولاً، من الواضح أنه لا يمكن ضمان الصحة بشكل صارم كإثبات النظرية الرسمي، ما لم يكن فضاء المدخلات محدوداً. هناك عدة أبحاث تجمع بين إثبات النظرية الرسمي والجبر الحاسوبي للتصديق الصارم على صحة التطبيقات (على سبيل المثال، [24، 2]). تقوم هذه أولاً بصياغة نظرية Gröbner basis في نظرية الأنواع البنائية. ثم، تنفذها ضمن لغة إثبات النظرية المضيفة، أو تستخرج البرنامج إلى لغات أخرى. ومع ذلك، بطبيعتها، يتطلب هذا النهج إثبات كل شيء رسمياً. ليست مهمة سهلة إثبات صحة كل جزء من البرنامج، حتى بمساعدة المُثبتات التلقائية. حتى لو تمكن المرء من إنهاء إثبات صحة خوارزمية ما، عندما يريد تحسينها لاحقاً، فيجب عليه إثبات "التكافؤ" أو صحة هذا التحسين. علاوة على ذلك، في بعض الأحيان تظل صحة الخوارزمية، أو حتى انتهاؤها، غير معروفة عند تنفيذها؛ على سبيل المثال تم إثبات صحة وانتهاء F₅ لـ Faugère [6] مؤخراً جداً [25]. علاوة على ذلك، هناك قيد واضح وهو أنه يمكننا استخراج البرامج فقط إلى اللغات المدعومة من قبل مُثبت النظرية. نعتبر هذه الشروط مقيدة للغاية، وقررنا اعتماد إثبات النظرية فقط في حساب عدد المتغيرات البسيط.

ثانياً، إذا كانت الخوارزمية لديها تعقيد زمني سيء، يمكن أن تنفجر اختبارات الخصائص بسهولة. على وجه الخصوص، نظراً لأن قواعد Gröbner لديها تعقيد زمني أسوأ من الأسي المضاعف، يمكن أن تستغرق المدخلات المُولدة عشوائياً وقتاً طويلاً لمعالجتها. قد يقلل المرء العبء عن طريق الجمع بين استراتيجيات التوليد العشوائية والتعدادية بعناية، ولكن لا يزال هناك احتمال وجود مدخلات صغيرة تستغرق وقتاً طويلاً. لتجنب مثل هذا الظرف، يمكن للمرء تقليل عدد المدخلات، ومع ذلك فإنه يقلل أيضاً من ضمان الصحة.

أخيراً، لا تكون جيدة جداً في معاملة الخصائص الوجودية. على الرغم من أن SmallCheck توفر المحدد الوجودي في مفرداتها، إلا أنها تحاول فقط إيجاد حلول حتى عمق مُحدد مسبقاً. إذا كانت الحلول "أكبر" نسبياً من مدخلاتها، فإن هذا يؤدي إلى إخفاقات سلبية خاطئة. على سبيل المثال، يمكن للمرء كتابة المواصفة التالية التي تتطلب أن يكون كل عنصر من نتيجة `calcGroebnerBasis` عضواً في المثالي الأصلي، ومع ذلك فإنها لا تعمل كما هو متوقع.

في ما سبق، يدل `dot i g` على "الضرب النقطي". كحل بديل، نجمع حالياً بين الاتصال بين العمليات والاختبار القائم على الخصائص. بشكل أكثر تحديداً، نستدعي تطبيقاً موثوقاً موجوداً، مثل SINGULAR، داخل المواصفة على النحو التالي. وبالتالي، إذا كانت الخاصية الوجودية المطروحة قابلة للتقرير ولها تطبيق موثوق موجود، فقد يكون من الأفضل استدعاؤها داخل المواصفات.

---

### Translation Notes

- **Figures referenced:** Code 5
- **Key terms introduced:** property-based testing (الاختبار القائم على الخصائص), theorem proving (إثبات النظرية), formal specification (المواصفة الرسمية), counterexample (الأمثلة المضادة), existential quantifier (المحدد الوجودي), dot-product (الضرب النقطي)
- **Equations:** Several code examples preserved
- **Citations:** [1, 2, 6, 9, 11, 24, 25, 26]
- **Special handling:**
  - Code examples preserved in English
  - System names (QuickCheck, SmallCheck, Singular, SINGULAR) kept in English
  - Technical testing terminology translated consistently
  - Mathematical properties and axioms explained in Arabic

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
