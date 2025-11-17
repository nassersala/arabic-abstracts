# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** formal methods (الأساليب الرسمية), software engineering (هندسة البرمجيات), computer science (علوم الحاسوب), software quality (جودة البرمجيات), curricula (مناهج)

---

### English Version

The greatest contribution that universities make to industrial practices is through releasing legions of graduates every year. When properly equipped with a scholarly education, these graduates challenge established processes and pave the way for new approaches. In the increasingly-digital world we live in, the scope for this is arguably greatest in the software industry, particularly given that the public perception–and indeed the reality–is that software is inherently unreliable.

Advances in digital technology take place at an astronomical rate, unfettered by regulations which would hinder progress in other scientific endeavours. There are generally few established principles in place to ensure that new software systems are as reliable as, say, a new vaccine. Software engineers demonstrate success in their company by releasing systems which, for almost all intents and purposes, appear to work. Because of the benefits these advances offer society, the public are generally accepting of – and, indeed, used to – software failures. This situation persists in spite of the fact that computer science and software engineering research has developed a multitude of design principles which could help to improve software quality [Bar11]. It has been over half a century since Robert Floyd's seminal paper [Flo67] set out the means by which computer programs could be analysed to determine their functional correctness, and formal methods for developing correct software have been steadily devised and refined ever since. The typical computer science or software engineering graduate, however, leaves university with little or no knowledge of formal methods, and even a dislike for whatever formal methods they have encountered in their studies. Thus, rather than opening doors for formal methods in (software) industry, university education seems to have a detrimental effect.

Due to their ubiquity, software failures are overlooked by society as they tend to result in nothing more serious than delays and frustrations. We accept as mere inconvenience when a software failure results in a delayed train or an out-of-order cash machine or a need to repeatedly enter details into a website. However, the problems of systems failures become more serious (costly, deadly, invasive) as automatic control systems find their way into virtually every aspect of our daily lives. This increasing reliance on computer systems makes it essential to develop and maintain software in which the possibility, and probability, of hazardous errors is minimised. Formal methods offer cost-efficient means to achieve the required high degree of software quality.

A major reason that students (and, in turn, software engineers) have a negative attitude towards formal methods is that these are not introduced with due care during the early stages of higher education. Left to the theoretical computer science professor, such courses often start with fearful terms like state machine, logical inference, mathematical semantics, etc., without providing elementary explanations of the basic notions which relate these to the practice of software development. In their defence, formal methods professors often find it difficult to deliver the subject due to students' scepticism [Zhu20], which arises from the generally limited or non-existent exposure to formal methods in the rest of the curriculum. Boute [Bou09] and Sekerinski [Sek06] observe that limited references from other subjects and isolated use are the main factors leading to students' low opinion. Even worse, students perceive formal methods to be unsuitable for actual software engineering [BDK+06] or even an "additional burden" [BLA+09].

In this white paper we analyse what hinders a successful formal methods education, and make constructive suggestions about how to change the situation. We are convinced that such changes are a prerequisite for formal methods to become widely accepted in industry. We analyse the current situation of formal methods teaching and explore ways which we think will be engaging for students and practitioners alike. Our vision is that formal methods can be taught in such a way that both students and lecturers will enjoy formal methods teaching.

This white paper is the result of a collective effort by authors and participants at the 1st International Workshop "Formal Methods – Fun for Everybody", which was held in Bergen, Norway, 2-3 December 2019. At the workshop, there were several discussion sessions. Based on these, the two lead authors devised a paper outline, which was subsequently "populated" with text snippets written by all authors. The resulting draft was carefully edited, and agreed upon by all authors. By its very nature, this white paper offers a spectrum of opinions, in particular in the personal statements. What unites us are the following beliefs:

- Current software engineering practices fail to deliver dependable software.
- Formal methods are capable of improving this situation, and are beneficial and cost-effective for mainstream software development.
- Education in formal methods is key to progress things.
- Education in formal methods needs to be transformed.

In Section 2, we analyse the challenges in teaching formal methods. In Section 3, we collect ideas about how to teach formal methods – the fun way. In Section 4, we discuss how to increase the visibility of formal methods throughout the curriculum. In Section 5, we suggest a syllabus for a compulsory formal methods course. Finally, we discuss how to assess such teaching efforts in Section 6, before making concluding remarks in Section 7.

---

### النسخة العربية

تتمثل أعظم مساهمة تقدمها الجامعات للممارسات الصناعية في إطلاق أفواج من الخريجين كل عام. عندما يتم تجهيز هؤلاء الخريجين بشكل صحيح بتعليم علمي، فإنهم يتحدون العمليات القائمة ويمهدون الطريق لنُهج جديدة. في العالم المتزايد الرقمنة الذي نعيش فيه، يمكن القول إن نطاق ذلك هو الأعظم في صناعة البرمجيات، لا سيما بالنظر إلى أن التصور العام - والواقع بالفعل - هو أن البرمجيات غير موثوقة بطبيعتها.

تحدث التطورات في التكنولوجيا الرقمية بمعدل فلكي، دون قيود من اللوائح التي قد تعيق التقدم في المساعي العلمية الأخرى. لا توجد بشكل عام سوى مبادئ قليلة راسخة لضمان أن الأنظمة البرمجية الجديدة موثوقة مثل، على سبيل المثال، لقاح جديد. يُظهر مهندسو البرمجيات النجاح في شركاتهم من خلال إطلاق أنظمة تبدو، لجميع النوايا والأغراض تقريباً، أنها تعمل. نظراً للفوائد التي تقدمها هذه التطورات للمجتمع، فإن الجمهور يقبل بشكل عام - وبالفعل، اعتاد على - فشل البرمجيات. يستمر هذا الوضع على الرغم من حقيقة أن البحث في علوم الحاسوب وهندسة البرمجيات قد طور العديد من مبادئ التصميم التي يمكن أن تساعد في تحسين جودة البرمجيات [Bar11]. لقد مضى أكثر من نصف قرن منذ أن وضعت ورقة روبرت فلويد الرائدة [Flo67] الوسائل التي يمكن من خلالها تحليل البرامج الحاسوبية لتحديد صحتها الوظيفية، وقد تم ابتكار وتحسين الأساليب الرسمية لتطوير البرمجيات الصحيحة بشكل مطرد منذ ذلك الحين. ومع ذلك، يغادر خريج علوم الحاسوب أو هندسة البرمجيات النموذجي الجامعة بمعرفة قليلة أو معدومة بالأساليب الرسمية، بل وحتى بكره لأي أساليب رسمية واجهها في دراسته. وبالتالي، بدلاً من فتح الأبواب للأساليب الرسمية في صناعة (البرمجيات)، يبدو أن التعليم الجامعي له تأثير ضار.

نظراً لانتشارها في كل مكان، يتم تجاهل فشل البرمجيات من قبل المجتمع لأنها تميل إلى عدم التسبب في شيء أكثر خطورة من التأخيرات والإحباطات. نقبل كمجرد إزعاج عندما يؤدي فشل برمجي إلى تأخير قطار أو خروج جهاز صراف آلي عن الخدمة أو الحاجة إلى إدخال التفاصيل بشكل متكرر في موقع ويب. ومع ذلك، تصبح مشكلات فشل الأنظمة أكثر خطورة (مكلفة، مميتة، تدخلية) حيث تجد أنظمة التحكم الآلي طريقها إلى كل جانب من جوانب حياتنا اليومية تقريباً. هذا الاعتماد المتزايد على أنظمة الحاسوب يجعل من الضروري تطوير وصيانة البرمجيات التي يتم فيها تقليل إمكانية واحتمالية الأخطاء الخطرة. توفر الأساليب الرسمية وسائل فعالة من حيث التكلفة لتحقيق الدرجة العالية المطلوبة من جودة البرمجيات.

السبب الرئيسي لامتلاك الطلاب (وبالتالي مهندسي البرمجيات) موقفاً سلبياً تجاه الأساليب الرسمية هو أن هذه الأساليب لا يتم تقديمها بالعناية الواجبة خلال المراحل المبكرة من التعليم العالي. عند تركها لأستاذ علوم الحاسوب النظرية، غالباً ما تبدأ هذه المقررات بمصطلحات مخيفة مثل آلة الحالة، والاستدلال المنطقي، والدلالات الرياضية، إلخ، دون تقديم تفسيرات أولية للمفاهيم الأساسية التي تربط هذه بممارسة تطوير البرمجيات. دفاعاً عنهم، غالباً ما يجد أساتذة الأساليب الرسمية صعوبة في تقديم الموضوع بسبب شكوك الطلاب [Zhu20]، والتي تنشأ من التعرض المحدود أو المعدوم للأساليب الرسمية في بقية المنهج. يلاحظ بوت [Bou09] وسيكيرينسكي [Sek06] أن المراجع المحدودة من المواد الأخرى والاستخدام المعزول هما العاملان الرئيسيان اللذان يؤديان إلى رأي الطلاب المتدني. والأسوأ من ذلك، أن الطلاب ينظرون إلى الأساليب الرسمية على أنها غير مناسبة لهندسة البرمجيات الفعلية [BDK+06] أو حتى "عبء إضافي" [BLA+09].

في هذه الورقة البيضاء، نحلل ما يعيق التعليم الناجح للأساليب الرسمية، ونقدم اقتراحات بناءة حول كيفية تغيير الوضع. نحن مقتنعون بأن مثل هذه التغييرات شرط أساسي لقبول الأساليب الرسمية على نطاق واسع في الصناعة. نحلل الوضع الحالي لتدريس الأساليب الرسمية ونستكشف طرقاً نعتقد أنها ستكون جذابة للطلاب والممارسين على حد سواء. رؤيتنا هي أن الأساليب الرسمية يمكن تدريسها بطريقة تجعل كلاً من الطلاب والمحاضرين يستمتعون بتدريس الأساليب الرسمية.

هذه الورقة البيضاء هي نتيجة جهد جماعي من قبل المؤلفين والمشاركين في ورشة العمل الدولية الأولى "الأساليب الرسمية - متعة للجميع"، التي عُقدت في بيرغن، النرويج، في الفترة من 2-3 ديسمبر 2019. في ورشة العمل، كانت هناك عدة جلسات نقاش. بناءً على ذلك، ابتكر المؤلفان الرئيسيان مخططاً للورقة، والذي تم لاحقاً "ملؤه" بمقتطفات نصية كتبها جميع المؤلفين. تم تحرير المسودة الناتجة بعناية، وتم الاتفاق عليها من قبل جميع المؤلفين. بطبيعتها، تقدم هذه الورقة البيضاء مجموعة من الآراء، لا سيما في البيانات الشخصية. ما يوحدنا هو المعتقدات التالية:

- تفشل ممارسات هندسة البرمجيات الحالية في تقديم برمجيات موثوقة.
- الأساليب الرسمية قادرة على تحسين هذا الوضع، وهي مفيدة وفعالة من حيث التكلفة لتطوير البرمجيات السائدة.
- التعليم في الأساليب الرسمية هو مفتاح التقدم.
- التعليم في الأساليب الرسمية يحتاج إلى التحول.

في القسم 2، نحلل التحديات في تدريس الأساليب الرسمية. في القسم 3، نجمع أفكاراً حول كيفية تدريس الأساليب الرسمية - بالطريقة الممتعة. في القسم 4، نناقش كيفية زيادة رؤية الأساليب الرسمية عبر المنهج. في القسم 5، نقترح منهجاً لمقرر إلزامي في الأساليب الرسمية. أخيراً، نناقش كيفية تقييم جهود التدريس هذه في القسم 6، قبل تقديم ملاحظات ختامية في القسم 7.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** white paper (ورقة بيضاء), formal methods (الأساليب الرسمية), functional correctness (الصحة الوظيفية), state machine (آلة الحالة), logical inference (الاستدلال المنطقي), mathematical semantics (الدلالات الرياضية)
- **Equations:** None
- **Citations:** [Bar11], [Flo67], [Zhu20], [Bou09], [Sek06], [BDK+06], [BLA+09]
- **Special handling:** Reference to Robert Floyd's seminal 1967 paper on program correctness

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.89
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88

### Back-Translation (Key Paragraph)

Arabic to English (first paragraph): "The greatest contribution that universities provide to industrial practices is through releasing cohorts of graduates each year. When these graduates are properly equipped with scientific education, they challenge existing processes and pave the way for new approaches. In the increasingly digitalized world we live in, it can be said that the scope of this is greatest in the software industry, particularly considering that the general perception - and reality indeed - is that software is inherently unreliable."

**Validation:** Excellent semantic preservation with accurate technical terminology and proper academic tone.
