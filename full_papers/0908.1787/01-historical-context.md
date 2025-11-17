# Section 1: Historical Context
## القسم 1: السياق التاريخي

**Section:** Introduction - Historical Context
**Translation Quality:** 0.87
**Glossary Terms Used:** quantum theory, Hilbert space, quantum logic, quantum entanglement, quantum non-locality, EPR paradox, quantum measurement, monoidal categories, linear logic, category theory, computational process

---

### English Version

With John von Neumann's "Mathematische Grundlagen der Quantenmechanik", published in 1932 [1], quantum theory reached maturity, now having been provided with a rigourous mathematical underpinning. Three year later something remarkable happened. John von Neumann wrote in a letter to the renowned American mathematician Garrett Birkhoff the following:

> I would like to make a confession which may seem immoral: I do not believe absolutely in Hilbert space no more – sic [2, 3]

In other words, merely three years after completing something that is in many ways the most successful formalism physics has ever known, both in terms of experimental predictions, technological applications, and conceptual challenges, its creator denounced his own brainchild. However, today, more than 70 years later, we still teach John von Neumann's Hilbert space formalism to our students. People did try to come up with alternative formalisms, by relying on physically motivated mathematical structures other than Hilbert spaces. For example, in 1936 Birkhoff and von Neumann proposed so-called 'quantum logic' [4]. But quantum logic's disciples failed to convince the wider physics community of this approach's virtues. There are similar alternative approaches due to Ludwig, Mackie, Jauch-Piron, and Foulis-Randall [5], but neither of these have made it into mainstream physics, nor is there any compelling evidence of their virtue.

Today, more than 70 years later, we meanwhile did learn many new things. For example, we discovered new things about the quantum world and its potential for applications:

• During the previous century, a vast amount of the ongoing discourse on quantum foundations challenged in some way or another the validity of quantum theory. The source of this was the community's inability to craft a satisfactory worldview in the light of the following:
  - *Quantum non-locality*, or, the EPR paradox, that is: Compound quantum systems which may be far apart exhibit certain correlations that cannot be explained as having been established in the past when the two systems were in close proximity. Rather, the correlations can only be explained as being instantaneously created over a large distance, hence 'non-locality'. But remarkably, these correlations are so delicate that this process does not involve instantaneous transmission of information, and hence does not violate Einstein's theory of relativity.
  - The *quantum measurement problem*, that is: There is no good explanation of what causes the wavefunction to collapse, and, there is no good explanation of the non-determinism in quantum measurements. The latter turns out to be closely related to quantum non-locality.

  We refer the reader to [6, 7] for more details on these issues. Many took these 'paradoxes' or 'quantum weirdness' to be tokens of the fact that there is something fundamentally wrong with quantum theory. But this position that quantum theory is in some way or another 'wrong' seems to be increasingly hard to maintain. Not only have there been impressive experiments which assert quantum theory in all of its aspects, but also, several new quantum phenomena have been observed, which radically alter the way in which we need think about nature, and which raise new kinds of conceptual challenges. Examples of experimentally established new phenomena are quantum teleportation [8], which we explain in detail below, and quantum key exchange [9], for which we refer the reader to [10]. In particular, the field of quantum information has emerged from embracing 'quantum weirdness', not as a bug, but as a feature!

• Within this quantum informatic endeavour we are becoming increasingly conscious of how central the particular behaviour of compound systems is to quantum theory. One nowadays refers to this as the existence of quantum entanglement. It is when compound quantum systems are in these entangled states that the non-local correlations can occur. The first to point at the key role of quantum entanglement within quantum theory was Schrödinger in 1935 [11]. Most of the new phenomena discovered in the quantum information era crucially rely on quantum entanglement. But this key role of quantum entanglement is completely ignored within the proposed alternatives to the Hilbert space formalism to which we referred above. The key concepts of those approaches solely apply to individual quantum systems, and, it is a recognised soft spot of these approaches that they weren't able to reproduce entanglement in a canonical manner. In hindsight, this is not that surprising. Neither the physical evidence nor the appropriate mathematical tools were available (yet) to establish a new formalism for quantum theory in which quantum entanglement plays the leading role.

But today, more than 70 years later, this situation has changed, which brings us to other important recent developments. These did not take place in physics, but in other areas of science:

• Firstly, not many might be aware of the enormous effort that has been made by the computer science community to understand the mathematical structure of general processes, and in particular, the way in which they interact, how different configurations of interacting processes might result in the same overall process, and similar fairly abstract questions. An accurate description of how concurrent processes precisely interact turns out to be far more delicate than one would imagine at first. Key to solving these problems are appropriate mathematical means for describing these processes, usually referred to as their semantics. The research area of computer science semantics has produced a vast amount of new mathematical structures which enable us to design high-level programming languages. You may ask, why do we need these high-level programming languages? Well, because otherwise there wouldn't be internet, there wouldn't be operating systems for your Mac or PC, there wouldn't be mobile phone networks, and there wouldn't be secure electronic payment mechanisms, simply because these systems are so complicated that getting things right wouldn't be possible without relying on the programming paradigms present in high-level programming languages such as abstraction, modularity, compositionality, computational types, and many others.

• These developments in computer science went hand-in-hand with developments in proof theory, that is, the study of the structure of mathematical proofs. In fact, the study of interacting programs is in a certain sense 'isomorphic' to the study of interacting proofs – what this 'certain sense' is should become clear to the reader after reading the remainder of this paper. The subject of proof theory encompasses the subject of logic: while logic aims to establish whether one can derive a conclusion given certain premises in 'yes/no'-terms, in proof theory one is also interested in how one establishes that something is either true or false. In other words, the process of proving things becomes an explicit part of the subject, and of particular interest is how certain 'ugly' proofs can be transformed in 'nicer' ones. In the late 1980's proof theoreticians became interested in how many times one uses (they say 'consume') a certain premise within proofs. To obtain a clear view on this they needed to strip logic from:
  - its implicit ability to clone premises. This implicit ability to clone premises was made explicit as a logical rule by Gentzen in 1934 [12]. Concretely, 'clone A within context Γ' translates symbolically as A, Γ ⊢ A, A, Γ where the symbol ⊢ stands for 'entails'.
  - its implicit ability to delete premises, cf. 'delete A within context Γ' means A, Γ ⊢ Γ.

  Stripping logic from these two rules gave rise to Girard's linear logic [13]. Now, in quantum information theory we also have a no-cloning principle and a no-deleting principle:
  - The *no-cloning theorem*, discovered in 1982 [14, 15], states that there is no physical operation which produces a copy of an arbitrary unknown quantum state. Explicitly, there is no physical operation f such that for any |ψ⟩ we have f(|ψ⟩ ⊗ |0⟩) = |ψ⟩ ⊗ |ψ⟩. The the fact that |ψ⟩ is unknown is crucial here, since otherwise we could just prepare a copy of |ψ⟩. Although this fact was only discovered 25 years ago, its proof is extremely simple [16].
  - The *no-deleting theorem* discovered in 2000 [17] requires a slightly more subtle formulation.

  One may wonder whether there is a connection between the logical and the physical no-cloning and no-deleting laws. In particular, the above indicates that maybe this new 'linear logic' might be more of a 'quantum logic' than the original 'Birkhoff-von Neumann quantum logic' which according to most logicians wasn't even a 'logic'. Another important new feature of linear logic was the fact that it had a manifestly geometrical aspect to it, which translated in purely diagrammatic characterisations of linear logic proofs and of proof transformations [18]. These proof diagrams look very similar to those that you will encounter in this paper [19].

• There exists an algebraic structure which captures interacting computational processes as well as linear logic, namely monoidal categories. Monoidal categories are a particular kind of categories. Initially, categories were introduced as a meta-theory for mathematical structures [20], which enables one to import results of one area of mathematics into another. Its consequently highly abstract nature earned it the not all too flattering name 'generalised abstract nonsense'. Nonetheless, categories, and monoidal categories in particular, meanwhile play an important role in several areas of mathematical physics, e.g. in a variety of approaches to quantum field theory, in statistical physics, and in several proposals for a theory of quantum gravity. Important mathematical areas such as knot theory are also naturally described in terms of monoidal categories. But for us their highly successful use in logic and computer science is more relevant. In those areas category theory is very established e.g. at Oxford University Computing Laboratory we offer it to our undergraduates. To pass from categories in computer science to categories in physics, the following substitution will start the ball rolling:

  'computational process' ↦ 'physical process'.

Once we find ourselves in the world of monoidal categories, language becomes purely diagrammatical. Structuralism becomes picturalism, ... It are the monoidal categories which underpin linear logic that provide it with its diagrammatic proof theory. Physicist friendly introductions to monoidal categories are [21, 22, 23, 24, 25, 26]. These are ordered by increasing level of technicality. A very pedestrian introduction to category theory is Lawvere and Schanuel's Conceptual Mathematics [27]. Standard textbooks on category theory such as [28] are unfortunately mostly directed at pure mathematicians, what makes them somewhat inappropriate for physicists.

All these developments together justify a new attempt for a 'better' formalism for quantum theory, say quantum logic mark II. We are not saying that there is something wrong with the (current) predictions of quantum theory, but that the way in which we obtain these isn't great.

---

### النسخة العربية

مع كتاب جون فون نويمان "Mathematische Grundlagen der Quantenmechanik" (الأسس الرياضية لميكانيكا الكم)، الذي نُشر عام 1932 [1]، بلغت نظرية الكم نضجها، حيث تم تزويدها الآن بأساس رياضي صارم. بعد ثلاث سنوات حدث شيء ملحوظ. كتب جون فون نويمان في رسالة إلى عالم الرياضيات الأمريكي الشهير غاريت بيركهوف ما يلي:

> أود أن أعترف اعترافاً قد يبدو غير أخلاقي: لم أعد أؤمن مطلقاً بفضاء هيلبرت بعد الآن [كذا] [2، 3]

بعبارة أخرى، بعد ثلاث سنوات فقط من إكمال شيء يُعد بعدة طرق الصياغة الشكلية الأكثر نجاحاً التي عرفها الفيزياء على الإطلاق، سواء من حيث التنبؤات التجريبية أو التطبيقات التكنولوجية أو التحديات المفاهيمية، تنصّل مبتكرها من إبداعه. ومع ذلك، اليوم، بعد أكثر من 70 عاماً، لا نزال ندرّس صياغة فضاء هيلبرت الشكلية التي وضعها جون فون نويمان لطلابنا. حاول الناس بالفعل ابتكار صياغات شكلية بديلة، بالاعتماد على بنى رياضية محفزة فيزيائياً غير فضاءات هيلبرت. على سبيل المثال، في عام 1936 اقترح بيركهوف وفون نويمان ما يسمى "المنطق الكمومي" [4]. لكن أتباع المنطق الكمومي فشلوا في إقناع مجتمع الفيزياء الأوسع بفضائل هذا النهج. هناك مناهج بديلة مماثلة بسبب لودفيغ، وماكي، وجوش-بيرون، وفوليس-راندال [5]، لكن لم يصل أي منها إلى الفيزياء السائدة، ولا يوجد أي دليل مقنع على فضيلتها.

اليوم، بعد أكثر من 70 عاماً، تعلمنا بالفعل أشياء جديدة كثيرة. على سبيل المثال، اكتشفنا أشياء جديدة عن العالم الكمومي وإمكاناته للتطبيقات:

• خلال القرن الماضي، تحدى قدر هائل من الخطاب المستمر حول أسس الكم بطريقة أو بأخرى صلاحية نظرية الكم. كان مصدر ذلك عدم قدرة المجتمع على صياغة رؤية مرضية للعالم في ضوء ما يلي:
  - *عدم المحلية الكمومية*، أو مفارقة EPR، أي: الأنظمة الكمومية المركبة التي قد تكون متباعدة تُظهر ارتباطات معينة لا يمكن تفسيرها على أنها تم إنشاؤها في الماضي عندما كان النظامان على مقربة. بل يمكن تفسير الارتباطات فقط على أنها تُنشأ بشكل آني عبر مسافة كبيرة، ومن هنا "عدم المحلية". لكن من الملحوظ أن هذه الارتباطات دقيقة جداً بحيث لا تتضمن هذه العملية نقل آني للمعلومات، وبالتالي لا تنتهك نظرية النسبية لأينشتاين.
  - *مشكلة القياس الكمومي*، أي: لا يوجد تفسير جيد لما يسبب انهيار الدالة الموجية، ولا يوجد تفسير جيد لعدم الحتمية في القياسات الكمومية. يتضح أن الأخير مرتبط ارتباطاً وثيقاً بعدم المحلية الكمومية.

  نحيل القارئ إلى [6، 7] لمزيد من التفاصيل حول هذه القضايا. اعتبر الكثيرون هذه "المفارقات" أو "الغرابة الكمومية" رموزاً لحقيقة أن هناك خطأ أساسي في نظرية الكم. لكن هذا الموقف القائل بأن نظرية الكم "خاطئة" بطريقة أو بأخرى يبدو أنه أصبح من الصعب الحفاظ عليه بشكل متزايد. ليس فقط كانت هناك تجارب مثيرة للإعجاب تؤكد نظرية الكم في جميع جوانبها، بل أيضاً، تم رصد عدة ظواهر كمومية جديدة، تغير بشكل جذري الطريقة التي نحتاج إلى التفكير بها حول الطبيعة، وتثير أنواعاً جديدة من التحديات المفاهيمية. أمثلة على الظواهر الجديدة المثبتة تجريبياً هي النقل الآني الكمومي [8]، الذي نشرحه بالتفصيل أدناه، وتبادل المفاتيح الكمومية [9]، والتي نحيل القارئ إليها في [10]. على وجه الخصوص، ظهر مجال المعلومات الكمومية من احتضان "الغرابة الكمومية"، ليس كعلة، بل كميزة!

• ضمن هذا المسعى المعلوماتي الكمومي أصبحنا ندرك بشكل متزايد مدى مركزية السلوك الخاص للأنظمة المركبة في نظرية الكم. يشير المرء في الوقت الحاضر إلى هذا باعتباره وجود التشابك الكمومي. عندما تكون الأنظمة الكمومية المركبة في هذه الحالات المتشابكة يمكن أن تحدث الارتباطات غير المحلية. كان أول من أشار إلى الدور الرئيسي للتشابك الكمومي ضمن نظرية الكم هو شرودنغر في عام 1935 [11]. تعتمد معظم الظواهر الجديدة المكتشفة في عصر المعلومات الكمومية بشكل حاسم على التشابك الكمومي. لكن هذا الدور الرئيسي للتشابك الكمومي يتم تجاهله تماماً ضمن البدائل المقترحة لصياغة فضاء هيلبرت الشكلية التي أشرنا إليها أعلاه. المفاهيم الرئيسية لتلك المناهج تنطبق فقط على الأنظمة الكمومية الفردية، وهي نقطة ضعف معترف بها في هذه المناهج أنها لم تكن قادرة على إعادة إنتاج التشابك بطريقة قانونية. بالنظر إلى الوراء، هذا ليس مفاجئاً للغاية. لم تكن الأدلة الفيزيائية ولا الأدوات الرياضية المناسبة متاحة (بعد) لإنشاء صياغة شكلية جديدة لنظرية الكم يلعب فيها التشابك الكمومي الدور الرائد.

لكن اليوم، بعد أكثر من 70 عاماً، تغير هذا الوضع، مما يقودنا إلى تطورات حديثة مهمة أخرى. لم تحدث هذه في الفيزياء، بل في مجالات أخرى من العلوم:

• أولاً، قد لا يكون الكثيرون على علم بالجهد الهائل الذي بذله مجتمع علوم الحاسوب لفهم البنية الرياضية للعمليات العامة، وبشكل خاص، الطريقة التي تتفاعل بها، وكيف يمكن أن تؤدي تكوينات مختلفة من العمليات المتفاعلة إلى نفس العملية الإجمالية، وأسئلة مجردة مماثلة إلى حد ما. يتضح أن الوصف الدقيق لكيفية تفاعل العمليات المتزامنة بالضبط أكثر دقة بكثير مما يتخيله المرء في البداية. المفتاح لحل هذه المشاكل هو الوسائل الرياضية المناسبة لوصف هذه العمليات، والتي يشار إليها عادة باسم دلالاتها. أنتجت مجال بحث دلالات علوم الحاسوب كماً هائلاً من البنى الرياضية الجديدة التي تمكننا من تصميم لغات برمجة عالية المستوى. قد تسأل، لماذا نحتاج إلى هذه اللغات البرمجية عالية المستوى؟ حسناً، لأنه بخلاف ذلك لن يكون هناك إنترنت، ولن تكون هناك أنظمة تشغيل لجهاز Mac أو PC الخاص بك، ولن تكون هناك شبكات هاتف محمول، ولن تكون هناك آليات دفع إلكترونية آمنة، ببساطة لأن هذه الأنظمة معقدة للغاية بحيث لن يكون من الممكن إنجاز الأمور بشكل صحيح دون الاعتماد على نماذج البرمجة الموجودة في لغات البرمجة عالية المستوى مثل التجريد، والوحدات، والتركيبية، والأنواع الحسابية، وغيرها الكثير.

• سارت هذه التطورات في علوم الحاسوب جنباً إلى جنب مع التطورات في نظرية البرهان، أي دراسة بنية البراهين الرياضية. في الواقع، دراسة البرامج المتفاعلة "متماثلة" بمعنى معين لدراسة البراهين المتفاعلة - ما هو هذا "المعنى المعين" يجب أن يصبح واضحاً للقارئ بعد قراءة بقية هذا البحث. يشمل موضوع نظرية البرهان موضوع المنطق: بينما يهدف المنطق إلى تحديد ما إذا كان يمكن للمرء استنتاج نتيجة بالنظر إلى مقدمات معينة من حيث "نعم/لا"، في نظرية البرهان يكون المرء مهتماً أيضاً بكيفية تحديد أن شيئاً ما صحيح أو خاطئ. بعبارة أخرى، تصبح عملية إثبات الأشياء جزءاً صريحاً من الموضوع، ومن الاهتمام الخاص كيف يمكن تحويل براهين معينة "قبيحة" إلى براهين "أجمل". في أواخر الثمانينيات أصبح منظرو البرهان مهتمين بعدد المرات التي يستخدم فيها المرء (يقولون "يستهلك") مقدمة معينة ضمن البراهين. للحصول على رؤية واضحة لهذا احتاجوا إلى تجريد المنطق من:
  - قدرته الضمنية على استنساخ المقدمات. تم جعل هذه القدرة الضمنية على استنساخ المقدمات صريحة كقاعدة منطقية بواسطة جنتسن في عام 1934 [12]. بشكل ملموس، "استنساخ A ضمن السياق Γ" يترجم رمزياً كـ A، Γ ⊢ A، A، Γ حيث الرمز ⊢ يعني "يستلزم".
  - قدرته الضمنية على حذف المقدمات، راجع "حذف A ضمن السياق Γ" يعني A، Γ ⊢ Γ.

  أدى تجريد المنطق من هاتين القاعدتين إلى المنطق الخطي لجيرارد [13]. الآن، في نظرية المعلومات الكمومية لدينا أيضاً مبدأ عدم الاستنساخ ومبدأ عدم الحذف:
  - *نظرية عدم الاستنساخ*، المكتشفة في عام 1982 [14، 15]، تنص على أنه لا توجد عملية فيزيائية تنتج نسخة من حالة كمومية مجهولة تعسفية. صراحة، لا توجد عملية فيزيائية f بحيث لأي |ψ⟩ يكون لدينا f(|ψ⟩ ⊗ |0⟩) = |ψ⟩ ⊗ |ψ⟩. حقيقة أن |ψ⟩ مجهولة حاسمة هنا، لأنه بخلاف ذلك يمكننا فقط إعداد نسخة من |ψ⟩. على الرغم من أن هذه الحقيقة اكتُشفت فقط قبل 25 عاماً، إلا أن برهانها بسيط للغاية [16].
  - *نظرية عدم الحذف* المكتشفة في عام 2000 [17] تتطلب صياغة أكثر دقة قليلاً.

  قد يتساءل المرء عما إذا كان هناك اتصال بين قوانين عدم الاستنساخ وعدم الحذف المنطقية والفيزيائية. على وجه الخصوص، يشير ما سبق إلى أنه ربما يكون هذا "المنطق الخطي" الجديد أكثر من "منطق كمومي" من "منطق بيركهوف-فون نويمان الكمومي" الأصلي الذي وفقاً لمعظم المناطقة لم يكن حتى "منطقاً". ميزة جديدة مهمة أخرى للمنطق الخطي كانت حقيقة أن له جانباً هندسياً واضحاً، والذي ترجم إلى توصيفات تخطيطية بحتة لبراهين المنطق الخطي ولتحويلات البرهان [18]. تبدو هذه الرسوم التخطيطية للبرهان مشابهة جداً لتلك التي ستواجهها في هذا البحث [19].

• هناك بنية جبرية تلتقط العمليات الحسابية المتفاعلة وكذلك المنطق الخطي، وهي الفئات الأحادية. الفئات الأحادية هي نوع خاص من الفئات. في البداية، تم تقديم الفئات كنظرية فوقية للبنى الرياضية [20]، مما يمكّن المرء من استيراد نتائج منطقة واحدة من الرياضيات إلى أخرى. أكسبت طبيعتها المجردة للغاية الاسم غير المحبب "الهراء المجرد المعمم". ومع ذلك، تلعب الفئات، والفئات الأحادية بشكل خاص، في الوقت نفسه دوراً مهماً في عدة مجالات من الفيزياء الرياضية، على سبيل المثال في مجموعة متنوعة من المناهج لنظرية المجال الكمومي، في الفيزياء الإحصائية، وفي عدة مقترحات لنظرية الجاذبية الكمومية. مجالات رياضية مهمة مثل نظرية العقد موصوفة أيضاً بشكل طبيعي من حيث الفئات الأحادية. لكن بالنسبة لنا، استخدامها الناجح للغاية في المنطق وعلوم الحاسوب أكثر صلة. في تلك المجالات نظرية الفئات راسخة جداً، على سبيل المثال في مختبر الحوسبة بجامعة أكسفورد نقدمها لطلاب البكالوريوس لدينا. للانتقال من الفئات في علوم الحاسوب إلى الفئات في الفيزياء، سيبدأ الاستبدال التالي في تحريك الكرة:

  "عملية حسابية" ↦ "عملية فيزيائية".

بمجرد أن نجد أنفسنا في عالم الفئات الأحادية، تصبح اللغة تخطيطية بحتة. تصبح البنيوية صورية، ... إن الفئات الأحادية هي التي تدعم المنطق الخطي وتوفر له نظرية البرهان التخطيطية. مقدمات ودية للفيزيائيين للفئات الأحادية هي [21، 22، 23، 24، 25، 26]. هذه مرتبة حسب مستوى الفنية المتزايد. مقدمة بسيطة جداً لنظرية الفئات هي "الرياضيات المفاهيمية" لوفير وشانويل [27]. للأسف، الكتب المدرسية القياسية حول نظرية الفئات مثل [28] موجهة في الغالب إلى علماء الرياضيات البحتة، مما يجعلها غير مناسبة إلى حد ما للفيزيائيين.

كل هذه التطورات معاً تبرر محاولة جديدة لصياغة شكلية "أفضل" لنظرية الكم، لنقل منطق كمومي الإصدار الثاني. نحن لا نقول أن هناك خطأ في التنبؤات (الحالية) لنظرية الكم، ولكن الطريقة التي نحصل بها على هذه التنبؤات ليست رائعة.

---

### Translation Notes

- **Hilbert space:** Translated as "فضاء هيلبرت" - standard term
- **Quantum logic:** Translated as "المنطق الكمومي" - established term
- **Quantum entanglement:** Translated as "التشابك الكمومي" - standard physics term
- **EPR paradox:** Kept as EPR in Latin letters as it's a proper name (Einstein-Podolsky-Rosen)
- **Monoidal categories:** Translated as "الفئات الأحادية" following category theory convention
- **Linear logic:** Translated as "المنطق الخطي" - standard logic term
- **No-cloning theorem:** Translated as "نظرية عدم الاستنساخ" - established quantum computing term
- **Proof theory:** Translated as "نظرية البرهان" - mathematical logic term
- **Semantics:** Translated as "دلالات" in computer science context

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.88
- **Overall section score:** 0.87

**Justification:** This section successfully conveys the historical narrative about von Neumann's doubts, the failure of alternative formalisms, and the emergence of category theory from computer science. The technical terminology is handled consistently. The parallel between linear logic's no-cloning/no-deleting and quantum theory's analogous principles is clearly presented. Minor deduction for the complexity of translating some philosophical arguments about "quantum weirdness" and the computer science metaphors.
