# Section 1: Introduction - Each Decade Has Its Own Programming Languages and Linguistic Relativity
## القسم 1: المقدمة - لكل عقد لغات البرمجة الخاصة به والنسبية اللغوية

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** لغات البرمجة, الحوسبة الإحصائية, تجريدات, تعبيرية, بنية البيانات, مصفوفات, عادات لغوية

---

### English Version

## 1. Each decade has its own programming languages

Each discipline has its own favorite languages: applied mathematics has MATLAB, web applications have JavaScript, and high-performance computing still uses Fortran, accompanied by Python (Jones et al., 2001) and even Tcl (Phillips et al., 2014). Statistical computing, of course, is associated strongly with R. Yet the boundaries of these seemingly absolute fiefdoms in the kingdom of computing turn out to be surprisingly malleable on the time scale of decades. Statistical computing came to prominence with PL/I in the 70s, APL in the 80s, and XLISP-STAT in the 90s before the relatively modern advent of S and R (de Leeuw, 2005). In truth, programming languages come and go beyond the time scale of single years or even PhD studentships.

So what makes a programming language suitable for the demands of a scientific discipline like statistical computing? Discussing pros and cons of different languages can get bogged down in absolutist statements about what "can" and "cannot" be done in a language. On some level such statements are absurd, given that all sufficiently complicated programming languages are Turing complete, and therefore have the same computational power in the sense of Turing equivalence. Thus anything that can be done in one Turing-complete language must be doable in another Turing-complete language. Instead, the answer to the question of suitability must necessarily be ensconced in "softer" concepts about ease of use and expressiveness, concepts that are hard to define precisely but are nonetheless responsible for shaping the adoption of programming languages.

This paper explores how the suitability of programming languages is related to expressiveness: what abstractions exist in a given programming language that map onto ideas that a programmer would want to implement? Closely related is the notion of idiomaticness: would an experienced programmer in a particular language recognize and accept a given piece of code as "idiomatic"?

## 1.1 Linguistic relativity and programming languages

To discuss the suitability of programming languages, I will borrow notions from the study of human languages, linguistics. In particular, I will adopt the controversial concept of linguistic relativity (Gumperz and Levinson, 1996), or the Sapir–Whorf hypothesis (Brown, 1976), and argue that the idea that (human) languages determine or even constrain cognition has its relevance to computer languages and programming.

Some of the original writings of Sapir and Whorf seem particularly relevant to the discussion. Here are some choice quotations:

> Human beings do not live in the objective world alone,[...] but are very much at the mercy of the particular language which has become the medium of expression for their society [...] [T]he 'real world' is to a large extent unconsciously built up on the language habits of the group. (Sapir, 1929)

Sapir wrote about human languages, in particular contrasting native American languages like Hopi against Occidental languages like English. Nevertheless, programmers would immediately recognize these words about "language habits" as echoing a parallel worldview in computer languages, being themselves human constructs designed to abstract away unwanted, low level machine details. Some examples of these programming language habits may include:

- "Always put data in a data frame"
- "Never write for loops; vectorize your code to gain performance."

Some "language habits" can be as banal as choosing between 0- or 1-based indexing, leading to notoriously unproductive flame wars. Others are more subtle. For example, MATLAB treats vectors like column matrices, and therefore allow operations on one-dimensional objects like v[(2,1)] indexing with two numbers, which are disallowed in many other languages like C. We can trace the different indexing behaviors back to different mathematical starting points—whereas most languages treat vectors as one-dimensional arrays, i.e. "flat" sequences of numbers, MATLAB by virtue of treating most objects like matrices, assumes that vectors by default are column vectors, and therefore behave just matrices with one column.

The fact that such discussions of language habits tend to be emotionally charged is also not a coincidence. Whorf wrote:

> [E]very person [...] carries through life certain naïve but deeply rooted ideas about talking and its relation to thinking. Because of their firm connection with speech habits that have become unconscious and automatic, these notions tend to be intolerant of opposition. (Whorf, 1956b)

Replace "talking" with "writing code", and the analogy between speech and computer programs could hardly be plainer. An experienced programmer, practically by definition, internalizes the boilerplate and design patterns in code as "unconscious and automatic" idioms to be regurgitated on demand (preferably with an editor or IDE that helps reinforce these idioms automatically). To the fluent Java programmer, wrapping everything in a class must be second nature, just as the R user is accustomed to seeing data in a data frame, or whitespace sensitivity to the Pythonista. Allowing for code as a generalization of speech, one could argue that Whorf's observation predicted the very phenomenon of flame wars over programming language design!

In the rest of this paper, I will make use of another insight from Whorf:

> Through [linguistic knowledge], the world as seen from the diverse viewpoints of other social groups, that we have thought of as alien, becomes intelligible in new terms. Alienness turns into a new and often clarifying way of looking at things. (Whorf, 1956a)

I will present a simple, stereotypical data science task and show how solutions may be implemented in different computer languages, not all of which may necessarily be familiar to the reader or the typical user of statistical computing. This side-by-side comparison of the familiar and unfamiliar will hopefully aid to highlight similarities and differences between the abstractions expressed within the codes.

---

### النسخة العربية

## 1. لكل عقد لغات البرمجة الخاصة به

لكل تخصص لغاته المفضلة: الرياضيات التطبيقية لديها MATLAB، وتطبيقات الويب لديها JavaScript، والحوسبة عالية الأداء لا تزال تستخدم Fortran، مصحوبة بـ Python (Jones et al., 2001) وحتى Tcl (Phillips et al., 2014). الحوسبة الإحصائية، بالطبع، ترتبط بقوة بـ R. ومع ذلك، فإن حدود هذه الإقطاعيات التي تبدو مطلقة في مملكة الحوسبة تتضح أنها مرنة بشكل مدهش على مقياس زمني من العقود. برزت الحوسبة الإحصائية مع PL/I في السبعينيات، وAPL في الثمانينيات، وXLISP-STAT في التسعينيات قبل ظهور S وR الحديثين نسبياً (de Leeuw, 2005). في الحقيقة، تأتي لغات البرمجة وتذهب خارج النطاق الزمني للسنوات الفردية أو حتى فترات دراسة الدكتوراه.

إذاً ما الذي يجعل لغة البرمجة مناسبة لمتطلبات تخصص علمي مثل الحوسبة الإحصائية؟ يمكن أن تتعثر مناقشة إيجابيات وسلبيات اللغات المختلفة في تصريحات مطلقة حول ما "يمكن" و"لا يمكن" القيام به في لغة ما. على مستوى معين، مثل هذه التصريحات سخيفة، نظراً لأن جميع لغات البرمجة المعقدة بما فيه الكفاية هي مكتملة وفقاً لتورينج، وبالتالي لديها نفس القوة الحسابية بمعنى تكافؤ تورينج. وبالتالي، فإن أي شيء يمكن القيام به في لغة واحدة مكتملة وفقاً لتورينج يجب أن يكون قابلاً للتنفيذ في لغة أخرى مكتملة وفقاً لتورينج. بدلاً من ذلك، يجب أن تكون الإجابة على سؤال الملاءمة متضمنة بالضرورة في مفاهيم "أكثر نعومة" حول سهولة الاستخدام والتعبيرية، وهي مفاهيم يصعب تعريفها بدقة ولكنها مع ذلك مسؤولة عن تشكيل اعتماد لغات البرمجة.

تستكشف هذه الورقة كيف ترتبط ملاءمة لغات البرمجة بالتعبيرية: ما هي التجريدات الموجودة في لغة برمجة معينة والتي تتوافق مع الأفكار التي يريد المبرمج تنفيذها؟ يرتبط ارتباطاً وثيقاً بذلك مفهوم الاصطلاحية: هل سيتعرف مبرمج متمرس في لغة معينة على قطعة من الشفرة ويقبلها باعتبارها "اصطلاحية"؟

## 1.1 النسبية اللغوية ولغات البرمجة

لمناقشة ملاءمة لغات البرمجة، سأستعير مفاهيم من دراسة اللغات البشرية، أي علم اللغة. على وجه الخصوص، سأتبنى المفهوم المثير للجدل للنسبية اللغوية (Gumperz and Levinson, 1996)، أو فرضية سابير-وورف (Brown, 1976)، وأؤكد أن فكرة أن اللغات (البشرية) تحدد أو حتى تقيد الإدراك لها صلة بلغات الحاسوب والبرمجة.

يبدو أن بعض كتابات سابير ووورف الأصلية ذات صلة خاصة بالمناقشة. فيما يلي بعض الاقتباسات المختارة:

> لا يعيش البشر في العالم الموضوعي وحده، [...] بل هم تحت رحمة اللغة المعينة التي أصبحت وسيلة التعبير لمجتمعهم [...] [إ]ن "العالم الحقيقي" يُبنى إلى حد كبير بشكل غير واعٍ على عادات اللغة للمجموعة. (Sapir, 1929)

كتب سابير عن اللغات البشرية، وعلى وجه الخصوص مقارنة اللغات الأمريكية الأصلية مثل الهوبي مع اللغات الغربية مثل الإنجليزية. ومع ذلك، سيتعرف المبرمجون على الفور على هذه الكلمات حول "عادات اللغة" باعتبارها تعكس رؤية عالمية موازية في لغات الحاسوب، كونها نفسها بنى بشرية مصممة للتجريد بعيداً عن التفاصيل الآلية غير المرغوب فيها ذات المستوى المنخفض. قد تشمل بعض الأمثلة على عادات لغة البرمجة هذه:

- "ضع البيانات دائماً في إطار بيانات"
- "لا تكتب حلقات for أبداً؛ استخدم المتجهات في شفرتك للحصول على الأداء."

يمكن أن تكون بعض "عادات اللغة" عادية مثل الاختيار بين الفهرسة القائمة على 0 أو 1، مما يؤدي إلى حروب لفظية غير منتجة بشكل سيء السمعة. البعض الآخر أكثر دقة. على سبيل المثال، تعامل MATLAB المتجهات مثل مصفوفات الأعمدة، وبالتالي تسمح بعمليات على كائنات أحادية البعد مثل v[(2,1)] بفهرسة برقمين، وهو ما لا يُسمح به في العديد من اللغات الأخرى مثل C. يمكننا تتبع سلوكيات الفهرسة المختلفة إلى نقاط انطلاق رياضية مختلفة - في حين أن معظم اللغات تعامل المتجهات كمصفوفات أحادية البعد، أي تسلسلات "مسطحة" من الأرقام، فإن MATLAB بحكم معاملة معظم الكائنات مثل المصفوفات، تفترض أن المتجهات افتراضياً هي متجهات أعمدة، وبالتالي تتصرف تماماً مثل المصفوفات ذات عمود واحد.

إن حقيقة أن مثل هذه المناقشات حول عادات اللغة تميل إلى أن تكون مشحونة عاطفياً ليست مصادفة أيضاً. كتب وورف:

> [ك]ل شخص [...] يحمل طوال حياته أفكاراً معينة ساذجة ولكنها متجذرة بعمق حول التحدث وعلاقته بالتفكير. بسبب ارتباطها القوي بعادات الكلام التي أصبحت غير واعية وتلقائية، فإن هذه المفاهيم تميل إلى عدم التسامح مع المعارضة. (Whorf, 1956b)

استبدل "التحدث" بـ "كتابة الشفرة"، ولا يمكن أن تكون القياس بين الكلام وبرامج الحاسوب أوضح من ذلك. يستوعب المبرمج المتمرس، عملياً بحكم التعريف، الشفرة النمطية وأنماط التصميم في الشفرة كتعابير "غير واعية وتلقائية" يتم إعادة إنتاجها عند الطلب (ويفضل أن يكون ذلك مع محرر أو IDE يساعد في تعزيز هذه التعابير تلقائياً). بالنسبة لمبرمج Java الطليق، يجب أن يكون لف كل شيء في فئة أمراً طبيعياً، تماماً كما اعتاد مستخدم R على رؤية البيانات في إطار بيانات، أو حساسية المسافات البيضاء لمبرمج Python. عند السماح بالشفرة كتعميم للكلام، يمكن للمرء أن يجادل بأن ملاحظة وورف تنبأت بظاهرة الحروب اللفظية حول تصميم لغات البرمجة!

في بقية هذه الورقة، سأستخدم رؤية أخرى من وورف:

> من خلال [المعرفة اللغوية]، يصبح العالم كما يُرى من وجهات نظر متنوعة لمجموعات اجتماعية أخرى، والتي اعتبرناها غريبة، مفهوماً بمصطلحات جديدة. تتحول الغرابة إلى طريقة جديدة وغالباً ما تكون موضحة للنظر إلى الأشياء. (Whorf, 1956a)

سأقدم مهمة علم بيانات بسيطة ونمطية وأوضح كيف يمكن تنفيذ الحلول في لغات حاسوب مختلفة، والتي قد لا تكون جميعها مألوفة بالضرورة للقارئ أو المستخدم النموذجي للحوسبة الإحصائية. ستساعد هذه المقارنة جنباً إلى جنب للمألوف وغير المألوف على تسليط الضوء على أوجه التشابه والاختلاف بين التجريدات المعبر عنها داخل الشفرات.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - linguistic relativity (النسبية اللغوية)
  - Sapir-Whorf hypothesis (فرضية سابير-وورف)
  - expressiveness (التعبيرية)
  - idiomaticness (الاصطلاحية)
  - language habits (عادات اللغة)
  - Turing complete (مكتملة وفقاً لتورينج)
  - abstractions (التجريدات)
- **Equations:** None
- **Citations:** Multiple references to authors (Jones et al., 2001; Phillips et al., 2014; de Leeuw, 2005; Gumperz and Levinson, 1996; Brown, 1976; Sapir, 1929; Whorf, 1956a, 1956b)
- **Special handling:**
  - Programming language names kept in English (MATLAB, JavaScript, Fortran, Python, Tcl, R, PL/I, APL, XLISP-STAT, S, C, Java)
  - Direct quotations from Sapir and Whorf presented with Arabic translations
  - Code examples ("Always put data in a data frame") presented in both English and Arabic

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-Translation Check (Key Paragraph)

Original: "So what makes a programming language suitable for the demands of a scientific discipline like statistical computing? Discussing pros and cons of different languages can get bogged down in absolutist statements about what "can" and "cannot" be done in a language."

Back-translation: "So what makes a programming language suitable for the requirements of a scientific discipline such as statistical computing? Discussion of the pros and cons of different languages can get stuck in absolute statements about what "can" and "cannot" be done in a language."

✓ Semantically equivalent
