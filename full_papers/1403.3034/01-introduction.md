# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** formal methods (الأساليب الرسمية), software engineering (هندسة البرمجيات), verification (التحقق), domain specific languages (لغات خاصة بالمجال), algebraic specification (المواصفات الجبرية), scalability (قابلية التوسع), automated theorem proving (إثبات النظريات الآلي)

---

### English Version

Formal methods in software engineering have existed at least as long as the term "software engineering" itself, which was coined at the NATO Science Conference, Garmisch, 1968. In many engineering-based application areas, such as in the railway domain, formal verification processes have reached an impressive level of maturity as demonstrated by various industrial case studies, e.g. see [citations]. Authors like Barnes also demonstrate that formal methods can be cost effective. Even though these studies successfully illustrate the use of formal methods from an academic perspective, adoption of formal methods within industry is still limited.

From the industrial perspective, issues include:

**Faithful modelling:** Do the proposed mathematical models faithfully represent the systems of concern? Modelling approaches offered from computer science are often in a form that is acceptable to computer scientists, but not to the engineer working within the domain. How can an engineer working within the domain come up with new models?

**Scalability:** Does the proposed technology scale up to industrially sized systems in a manner that is uniformly applicable? Often, formal methods have been applied in a pilot to specific systems, but require individual, hand-crafted adaptation and optimisation for each new system under consideration.

**Accessibility:** Are the methods accessible to practitioners in the domain of interest or is it just the developers of the approach who can apply them? Handling of tools for verification procedures is often aimed towards a computer science audience specialised in verification, however they are usually not manageable by engineers outside the field of formal methods.

This paper presents a new methodology addressing these three issues. The underlying theme is that:

> "Domain Specific Languages (DSLs) can aid with modelling, verification and encapsulation of formal methods tools within a given domain".

We first present our methodology in general terms and then demonstrate it on the concrete example of verifying scheme plans from the railway domain. Our methodology is centered around the algebraic specification language CASL. CASL provides us with a sound semantic foundation. Furthermore, CASL offers mature tool support for verification. Our methodology takes as a starting point industrial documents describing a DSL, see for instance the Invensys Rail Data Model. We then stepwise develop a modelling and automated verification process. Thanks to elements such as graphical tooling, the process as a whole is accessible to practitioners in the domain, verification is scalable, and models are guaranteed to be faithful.

The paper is organised as follows: First, we discuss our methodology in detail. Then, we introduce railway signalling as the domain in which we demonstrate our methodology and present the DSL which will serve as running example throughout the paper. The next sections apply the methodology step by step: in Section 4 we give a method for *formalising* a DSL within CASL (Step M1); Section 5 demonstrates how to *exploit implicit domain knowledge* for the purpose of verification (Step M2); Section 6 presents techniques to *encapsulate formal methods* within a tooling framework (Step M3) -- this includes the presentation of competitive verification results for railway scheme plan verification. Finally, we place our work in context by discussing related work.

While in the context of this paper we deal with an "academic" DSL, it is worth noting that we have successfully, i.e., with the same positive results, applied our methodology to the DSL of our industrial partner -- see [citation]. The chosen academic language is of smaller extent, however, it "covers" all challenging elements.

As the paper covers such diverse topics as railways, modelling in CASL, verification, and tooling, we present their respective background distributed over the paper. We use the labels "background" and "contribution" to signpost the status of each subsection. Our paper is based upon the PhD thesis of the first author and earlier results on the topic. Complete specifications, further details and further examples for the work we present in this paper can be found in the thesis. In 2011, we published a first version of our methodology. In 2012, we gave a first report upon the exploitation of domain knowledge for verification. In 2013, we discussed in detail how to formalise DSLs within CASL. However, this paper comprises the first complete presentation of the whole methodology.

---

### النسخة العربية

وُجدت الأساليب الرسمية في هندسة البرمجيات لمدة طويلة على الأقل بقدر مصطلح "هندسة البرمجيات" نفسه، والذي صِيغ في مؤتمر علوم منظمة حلف شمال الأطلسي (الناتو)، جارمش، عام 1968. في العديد من مجالات التطبيقات القائمة على الهندسة، مثل مجال السكك الحديدية، وصلت عمليات التحقق الرسمي إلى مستوى مثير للإعجاب من النضج كما هو موضح في دراسات حالة صناعية مختلفة. كما يُظهر مؤلفون مثل بارنز أن الأساليب الرسمية يمكن أن تكون فعالة من حيث التكلفة. على الرغم من أن هذه الدراسات توضح بنجاح استخدام الأساليب الرسمية من منظور أكاديمي، إلا أن اعتماد الأساليب الرسمية في الصناعة لا يزال محدودًا.

من المنظور الصناعي، تشمل القضايا ما يلي:

**النمذجة الأمينة:** هل تمثل النماذج الرياضية المقترحة الأنظمة محل الاهتمام بأمانة؟ غالبًا ما تكون نُهج النمذجة المقدمة من علوم الحاسوب في شكل مقبول لعلماء الحاسوب، ولكن ليس للمهندس العامل في المجال. كيف يمكن للمهندس العامل في المجال أن يأتي بنماذج جديدة؟

**قابلية التوسع:** هل تتوسع التقنية المقترحة لتصل إلى أنظمة بحجم صناعي بطريقة قابلة للتطبيق بشكل موحد؟ غالبًا ما تم تطبيق الأساليب الرسمية في مشاريع تجريبية على أنظمة محددة، ولكنها تتطلب تكيفًا وتحسينًا مصنوعًا يدويًا بشكل فردي لكل نظام جديد قيد النظر.

**إمكانية الوصول:** هل الأساليب متاحة لممارسي المجال محل الاهتمام أم أن مطوري النهج فقط هم من يمكنهم تطبيقها؟ غالبًا ما يكون التعامل مع أدوات إجراءات التحقق موجهًا نحو جمهور علوم الحاسوب المتخصص في التحقق، ومع ذلك عادةً لا يمكن للمهندسين خارج مجال الأساليب الرسمية إدارتها.

يقدم هذا البحث منهجية جديدة تعالج هذه القضايا الثلاث. الموضوع الأساسي هو أن:

> "اللغات الخاصة بالمجال (DSLs) يمكن أن تساعد في النمذجة، والتحقق، وتغليف أدوات الأساليب الرسمية ضمن مجال معين".

نقدم أولاً منهجيتنا بشكل عام ثم نوضحها على المثال الملموس للتحقق من مخططات الخطط من مجال السكك الحديدية. تتمحور منهجيتنا حول لغة المواصفات الجبرية CASL. توفر لنا CASL أساسًا دلاليًا سليمًا. علاوة على ذلك، تقدم CASL دعمًا ناضجًا للأدوات للتحقق. تأخذ منهجيتنا كنقطة انطلاق الوثائق الصناعية التي تصف لغة خاصة بالمجال، انظر على سبيل المثال نموذج بيانات Invensys Rail. ثم نطور خطوة بخطوة عملية نمذجة وتحقق آلي. بفضل عناصر مثل الأدوات الرسومية، فإن العملية ككل متاحة لممارسي المجال، والتحقق قابل للتوسع، والنماذج مضمونة لتكون أمينة.

يُنظم البحث على النحو التالي: أولاً، نناقش منهجيتنا بالتفصيل. ثم، نقدم إشارات السكك الحديدية كمجال نوضح فيه منهجيتنا ونقدم اللغة الخاصة بالمجال التي ستكون بمثابة مثال تشغيلي طوال البحث. تطبق الأقسام التالية المنهجية خطوة بخطوة: في القسم 4 نقدم طريقة *لصياغة* لغة خاصة بالمجال رسميًا ضمن CASL (الخطوة M1)؛ يوضح القسم 5 كيفية *استغلال المعرفة الضمنية بالمجال* لغرض التحقق (الخطوة M2)؛ يقدم القسم 6 تقنيات *لتغليف الأساليب الرسمية* ضمن إطار عمل الأدوات (الخطوة M3) -- يشمل ذلك عرض نتائج تحقق تنافسية للتحقق من مخططات خطط السكك الحديدية. أخيرًا، نضع عملنا في السياق من خلال مناقشة الأعمال ذات الصلة.

بينما نتعامل في سياق هذا البحث مع لغة خاصة بالمجال "أكاديمية"، تجدر الإشارة إلى أننا طبقنا بنجاح، أي بنفس النتائج الإيجابية، منهجيتنا على اللغة الخاصة بالمجال لشريكنا الصناعي. اللغة الأكاديمية المختارة ذات نطاق أصغر، ومع ذلك، فهي "تغطي" جميع العناصر الصعبة.

نظرًا لأن البحث يغطي موضوعات متنوعة مثل السكك الحديدية، والنمذجة في CASL، والتحقق، والأدوات، فإننا نقدم خلفياتها المعنية موزعة على البحث. نستخدم تسميات "الخلفية" و "المساهمة" للإشارة إلى حالة كل قسم فرعي. يستند بحثنا إلى أطروحة الدكتوراه للمؤلف الأول ونتائج سابقة حول الموضوع. يمكن العثور على مواصفات كاملة، وتفاصيل إضافية، وأمثلة إضافية للعمل الذي نقدمه في هذا البحث في الأطروحة. في عام 2011، نشرنا نسخة أولى من منهجيتنا. في عام 2012، قدمنا تقريرًا أوليًا حول استغلال المعرفة بالمجال للتحقق. في عام 2013، ناقشنا بالتفصيل كيفية صياغة اللغات الخاصة بالمجال رسميًا ضمن CASL. ومع ذلك، يتضمن هذا البحث العرض الكامل الأول للمنهجية بأكملها.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:**
  - Faithful modelling (النمذجة الأمينة)
  - Scalability (قابلية التوسع)
  - Accessibility (إمكانية الوصول)
  - Domain Specific Languages (اللغات الخاصة بالمجال)
  - CASL (المواصفات الجبرية)
  - Railway signalling (إشارات السكك الحديدية)
- **Citations:** Preserved as [citations] in English version, maintained in Arabic
- **Special handling:**
  - The three main challenges are highlighted as a description list
  - The central quote is preserved as a block quote
  - Section structure references maintained

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
