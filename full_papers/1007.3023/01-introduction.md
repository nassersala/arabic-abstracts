# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** purely functional programming, side effects, parallel, structured programming, imperative programming, functional programming

---

### English Version

Purely functional programming (PFP) has a chance of becoming very popular for the simple reason that we now have laptops with four cores and more. The promise of PFP is that because there are no side-effects, no destructive updates, and no shared mutable state, partitioning a program into pieces that run in parallel becomes straightforward.

Another consequence of the freedom from impure language constructs is that reasoning about program correctness, both formally and informally, becomes much easier in PFP languages than in, say, imperative languages. Therefore it is not surprising that PFP is popular within the theorem proving community. For example, the source code of the interactive theorem proving assistant Isabelle [10] is mostly written in a purely functional style. Outside of such specialty communities though, PFP clearly has not reached the mainstream yet.

A programming paradigm that pervades today's mainstream is Dijkstra's structured programming [2] (SP). Most young programmers even do not know the term structured programming anymore, but anyway still construct their object-oriented programs out of building blocks like if-branches and while-loops.

Interestingly, the PFP community largely rejects SP because it smells of side-effects, destructive updates, and mutable state, just the things a purely functional programmer wants to avoid. As an example, let us examine the Isabelle (version 2009-2) source code. Discounting blank lines, it consists of about 140000 lines of Standard ML [5] (SML) code. Yet, only ten of those lines use the while keyword of SML! Furthermore, five out of those ten lines are part of Isabelle's system level code, and a further three lines stem from the author of this paper trying to circumvent missing tail-recursion optimization. The reason for this sparse use of while is clear: in order to use while in SML one must also use reference cells which are the embodiment of the small amount of impurity still left in SML.

The easiest way to make PFP more mainstream might be to make SP, which already is part of the mainstream, an integral part of PFP! This is what this paper is about. Our central tool for such a unification of PFP and SP is the notion of linear scope. Linear scope makes heavy use of shadowing, therefore we first look at shadowing and its treatment in other languages that draw on functional programming, like Erlang and Scala. We then present the syntax of a toy language called Mini Babel-17 to prepare a proper playground for the introduction of linear scope. First we concentrate on how linear scope interacts with the sequencing and nesting of statements. From there the extension to conditionals and loops is straightforward. Finally we give a formal semantics for Mini Babel-17 and hence also for linear scope.

---

### النسخة العربية

للبرمجة الوظيفية الصرفة (PFP) فرصة لتصبح شائعة جداً للسبب البسيط المتمثل في أن لدينا الآن حواسيب محمولة بأربعة أنوية ومزيد. الوعد الذي تقدمه البرمجة الوظيفية الصرفة هو أنه لعدم وجود آثار جانبية، ولا تحديثات مدمرة، ولا حالة قابلة للتغيير مشتركة، يصبح تقسيم البرنامج إلى أجزاء تعمل بالتوازي أمراً مباشراً.

نتيجة أخرى للتحرر من البنيات اللغوية غير الصرفة هي أن الاستدلال على صحة البرنامج، سواء بشكل صوري أو غير صوري، يصبح أسهل بكثير في لغات البرمجة الوظيفية الصرفة منه في، لنقل، اللغات الأمرية. لذلك ليس من المفاجئ أن تكون البرمجة الوظيفية الصرفة شائعة داخل مجتمع إثبات النظريات. على سبيل المثال، الشفرة المصدرية لمساعد إثبات النظريات التفاعلي Isabelle [10] مكتوبة في الغالب بأسلوب وظيفي صرف. ومع ذلك، خارج مثل هذه المجتمعات المتخصصة، لم تصل البرمجة الوظيفية الصرفة بوضوح إلى التيار السائد بعد.

نموذج برمجة يسود التيار السائد اليوم هو البرمجة المهيكلة لدايكسترا [2] (SP). معظم المبرمجين الشباب لا يعرفون حتى مصطلح البرمجة المهيكلة بعد الآن، لكنهم على أي حال لا يزالون يبنون برامجهم الكائنية التوجه من لبنات البناء مثل تفرعات if وحلقات while.

ومن المثير للاهتمام أن مجتمع البرمجة الوظيفية الصرفة يرفض البرمجة المهيكلة إلى حد كبير لأنها تنم عن آثار جانبية، وتحديثات مدمرة، وحالة قابلة للتغيير، وهي بالضبط الأشياء التي يريد المبرمج الوظيفي الصرف تجنبها. كمثال، دعونا نفحص الشفرة المصدرية لـ Isabelle (الإصدار 2009-2). مع استبعاد الأسطر الفارغة، تتكون من حوالي 140000 سطر من شفرة Standard ML [5] (SML). ومع ذلك، فإن عشرة فقط من تلك الأسطر تستخدم الكلمة المفتاحية while من SML! علاوة على ذلك، خمسة من تلك الأسطر العشرة هي جزء من شفرة المستوى النظامي لـ Isabelle، وثلاثة أسطر أخرى تأتي من مؤلف هذه الورقة في محاولة للالتفاف على غياب تحسين استدعاء الذيل. السبب في هذا الاستخدام المتناثر لـ while واضح: من أجل استخدام while في SML يجب أن يستخدم المرء أيضاً خلايا مرجعية والتي هي تجسيد للقدر الصغير من عدم الصرافة المتبقي في SML.

قد تكون أسهل طريقة لجعل البرمجة الوظيفية الصرفة أكثر انتشاراً في التيار السائد هي جعل البرمجة المهيكلة، التي هي بالفعل جزء من التيار السائد، جزءاً لا يتجزأ من البرمجة الوظيفية الصرفة! هذا هو موضوع هذه الورقة. أداتنا المركزية لمثل هذا التوحيد بين البرمجة الوظيفية الصرفة والبرمجة المهيكلة هي مفهوم النطاق الخطي. يستخدم النطاق الخطي بكثافة التظليل، لذلك ننظر أولاً في التظليل ومعالجته في لغات أخرى تستمد من البرمجة الوظيفية، مثل Erlang و Scala. ثم نقدم بنية نحوية للغة لعبة تسمى Mini Babel-17 لإعداد ساحة لعب مناسبة لتقديم النطاق الخطي. نركز أولاً على كيفية تفاعل النطاق الخطي مع التسلسل والتداخل للعبارات. ومن هناك يكون التوسع إلى الشرطيات والحلقات مباشراً. وأخيراً نعطي دلالات صورية لـ Mini Babel-17 وبالتالي أيضاً للنطاق الخطي.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Purely functional programming (البرمجة الوظيفية الصرفة)
  - Side effects (آثار جانبية)
  - Destructive updates (تحديثات مدمرة)
  - Mutable state (حالة قابلة للتغيير)
  - Structured programming (البرمجة المهيكلة)
  - Linear scope (النطاق الخطي)
  - Shadowing (التظليل)
  - Tail-recursion optimization (تحسين استدعاء الذيل)
  - Reference cells (خلايا مرجعية)
- **Equations:** None
- **Citations:** [2] Dijkstra's structured programming, [5] Standard ML, [10] Isabelle
- **Special handling:**
  - Code keywords kept in English (while, if, etc.)
  - Programming language names kept in English (SML, Erlang, Scala, Mini Babel-17)

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
