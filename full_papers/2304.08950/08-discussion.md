# Section 8: Discussion
## القسم 8: المناقشة

**Section:** discussion
**Translation Quality:** 0.86
**Glossary Terms Used:** formal methods, formal verification, specification, model checking, counterexample, refinement

---

### English Version

In this section, we discuss the findings of the two user study phases following the research questions and points to be investigated (cf. Section 5.1).

**8.1 RQ1 – Challenges in Identifying Inconsistent Specifications**

Research question RQ1 gathers challenges in identifying inconsistent formal specifications that are introduced during the refinement of a system.

**Understanding formal notations is difficult for engineers.** Formal methods may play a crucial role on the left-hand side of the V-model (Weber 2009), where systems engineers and safety manager/engineers are mainly involved, to avoid major flaws in early design decisions. In our user survey Phase 1, 20 of 41 participants are system engineers and safety managers/engineers (Section 6.1.3). The majority of them perceives understanding of formal notations as hard to some degree (cf. Section 6.2). Additionally, we noticed that the complexity of understanding depends on years of experience in using formal methods. Results further show that introducing formal methods to engineering teams with little experience in formal methods is challenging.

**Identifying inconsistent specifications is difficult for engineers.** Results in Section 6.3 clearly show that a majority of Phase 1 participants perceive the identification and understanding of inconsistent specifications as hard to some degree and that it consumes significant time. Results are similar for maintaining and verifying the refinement consistency (Section 6.4).

Qualitative statements by the participants note that identifying and understanding of inconsistent specifications highly depends on the size of the system and the number of its requirements. These statements emphasize the question whether the usage of formal methods for industrial system and at industrial scale is possible. For example, the automobile sector is now developing systems that are quickly expanding in size and complexity as a result of highly automated driving. System and requirements are not only complex but also frequently changing, for instance, due to security demands.

Our initial expectation was that more of our participants perform manual inspections/reviews rather than using automated tools like model checkers, simulators, and reasoners in their development projects. However, on the contrary, a majority of participants use model checkers (Section 6.3.5). Even though a majority uses automated tools like model checkers, a majority still answers that the identification and understanding of inconsistent specifications are hard. A reason for this might be the complexity of verification tools and their generated results, raising the need to make them more user-friendly to be used by engineers without having in-depth knowledge of formal methods.

**8.2 RQ2 – Benefit of Formal Methods to Development Processes**

RQ2 gathers insights on whether the identification of inconsistent specifications and usage of formal methods are beneficial to real-world development processes.

**Using formal methods can make the system safer.** Functionalities of automotive systems increase expeditiously, resulting in more (safety) requirements to avoid any unintended behavior. Thus, performing safety analysis early on the left-hand side of the V-model (Weber 2009) is crucial to help reducing the number of errors identified later during the validation. A majority of participants agrees that formal verification can make the system safer and be a benefit to the functional safety (cf. Section 6.5 and Section 6.6). Although a majority of the participants have a positive opinion on using formal verification, based on the qualitative answers from the participants, there is a discussion whether formal verification is usable and scalable to real-world systems. Specifically, a majority participants indicate that the usage of formal methods could be improved by making formal notations easier to understand (cf. Section 6.6.2).

**Identifying inconsistent specifications is beneficial in real-world development processes.** Eliciting requirements, refining requirements, and developing system architectures are the initial steps in the V-model (Weber 2009). Thus, requirement elicitation and refinement of those requirements are crucial as they serve as a basis for further system development and safety analysis. Errors and inconsistencies introduced in these early phases, identified only in later development stages, become costly and may lead to catastrophic events. There is a high possibility that most safety-critical errors are identified late during the validation phase in industry (Pohl and Rupp 2011). Therefore, to identify errors in the requirements during the initial stages performing manual reviews (e.g., inspections) does not seem to be sufficient or an efficient approach. This motivates the usage of automated methods like formal verification and simulation to help identifying errors in requirements and overcoming challenges of manual reviews.

**8.3 RQ3 – Easing the Use of Formal Methods**

Insights for RQ3 are drawn from Phase 2, the one-group pretest-posttest experiment. RQ3 gathers insights whether engineers prefer to use formal methods (model checkers particularly) if the difficulty for understanding verification results to identify inconsistent specifications is reduced, in particular with the counterexample explanation approach.

**The counterexample explanation approach eases the comprehension when compared to the interpretation of the raw model checker output.** Six of 13 participants of the one-group pretest-posttest experiment answer that they understand the verification result generated by the model checker for the airbag system (Section 7.4). Our initial hypothesis was that by proving an additional user-friendly counterexample explanation, it would be easier for engineers to understand the error as well as that it can ease the usage of formal methods among engineers. The results discussed in Section 7.4 support this hypothesis, as a stark majority of 12 of 13 participants prefer the counterexample explanation compared to understanding the model checker output. In summary, improving the usability and understandability aspects of formal notations can promote the use of formal methods.

**It is possible for engineers to identify and fix inconsistent specifications based on the counterexample explanation approach.** With the raw model checker output, only five of 13 participants identify either fully or partially correct the inconsistent specifications. While with the counterexample explanation, nine of 13 participants were able to identify the complete set of inconsistent specifications and also correctly explained the reason of the inconsistency by understanding the explanation. This strongly shows that a counterexample explanation can indeed improve the error comprehension and providing such an explanation can promote the use of formal methods among engineers.

**The counterexample explanation approach can promote formal verification and usage of model checking in real-world development processes.** From the collected responses, a majority of participants have a positive opinion as a counterexample explanation could support maintaining refinement consistency, could be usable in real-world development process, and could be used while using formal methods (cf. Section 7.8). A major challenge mentioned by the participants is that tools currently used in their projects do not support integrating the proposed counterexample explanation approach. This shows that integrating the existing verification tools with industrial tools needs to be one of the prime focus to improve the usage of formal methods.

---

### النسخة العربية

في هذا القسم، نناقش نتائج مرحلتي دراسة المستخدمين وفقاً لأسئلة البحث والنقاط المراد التحقق منها (راجع القسم 5.1).

**8.1 RQ1 – التحديات في تحديد المواصفات غير المتسقة**

يجمع السؤال البحثي RQ1 التحديات في تحديد المواصفات الرسمية غير المتسقة التي يتم إدخالها أثناء تحسين النظام.

**فهم التدوينات الرسمية صعب بالنسبة للمهندسين.** قد تلعب الأساليب الرسمية دوراً حاسماً على الجانب الأيسر من نموذج V (ويبر 2009)، حيث يشارك بشكل أساسي مهندسو الأنظمة ومديرو/مهندسو السلامة، لتجنب العيوب الرئيسية في قرارات التصميم المبكرة. في مسح المستخدمين المرحلة 1، 20 من 41 مشاركاً هم مهندسو أنظمة ومديرو/مهندسو سلامة (القسم 6.1.3). تدرك غالبيتهم فهم التدوينات الرسمية على أنه صعب إلى حد ما (راجع القسم 6.2). بالإضافة إلى ذلك، لاحظنا أن تعقيد الفهم يعتمد على سنوات الخبرة في استخدام الأساليب الرسمية. تُظهر النتائج أيضاً أن تقديم الأساليب الرسمية لفرق الهندسة ذات الخبرة القليلة في الأساليب الرسمية يُعد تحدياً.

**تحديد المواصفات غير المتسقة صعب بالنسبة للمهندسين.** تُظهر النتائج في القسم 6.3 بوضوح أن غالبية المشاركين في المرحلة 1 يدركون تحديد وفهم المواصفات غير المتسقة على أنه صعب إلى حد ما وأنه يستهلك وقتاً كبيراً. النتائج مماثلة للحفاظ على اتساق التحسين والتحقق منه (القسم 6.4).

تشير البيانات النوعية من المشاركين إلى أن تحديد وفهم المواصفات غير المتسقة يعتمد بشكل كبير على حجم النظام وعدد متطلباته. تؤكد هذه البيانات على السؤال حول ما إذا كان استخدام الأساليب الرسمية للأنظمة الصناعية وعلى المستوى الصناعي ممكناً. على سبيل المثال، يطور قطاع السيارات الآن أنظمة تتوسع بسرعة في الحجم والتعقيد نتيجة للقيادة الآلية العالية. الأنظمة والمتطلبات ليست معقدة فحسب، بل تتغير أيضاً بشكل متكرر، على سبيل المثال، بسبب متطلبات الأمان.

كان توقعنا الأولي أن المزيد من مشاركينا يقومون بعمليات فحص/مراجعات يدوية بدلاً من استخدام أدوات آلية مثل فاحصات النماذج، والمحاكيات، والمُستدلات في مشاريع التطوير الخاصة بهم. ومع ذلك، على العكس من ذلك، تستخدم غالبية المشاركين فاحصات النماذج (القسم 6.3.5). على الرغم من أن الغالبية تستخدم أدوات آلية مثل فاحصات النماذج، لا تزال الغالبية تجيب بأن تحديد وفهم المواصفات غير المتسقة صعب. قد يكون السبب في ذلك تعقيد أدوات التحقق ونتائجها المُنتَجة، مما يثير الحاجة إلى جعلها أكثر سهولة في الاستخدام لاستخدامها من قبل المهندسين دون الحاجة إلى معرفة متعمقة بالأساليب الرسمية.

**8.2 RQ2 – فائدة الأساليب الرسمية لعمليات التطوير**

يجمع RQ2 رؤى حول ما إذا كان تحديد المواصفات غير المتسقة واستخدام الأساليب الرسمية مفيدين لعمليات التطوير الواقعية.

**استخدام الأساليب الرسمية يمكن أن يجعل النظام أكثر أماناً.** تزداد وظائف أنظمة السيارات بسرعة، مما يؤدي إلى المزيد من متطلبات (السلامة) لتجنب أي سلوك غير مقصود. وبالتالي، فإن إجراء تحليل السلامة في وقت مبكر على الجانب الأيسر من نموذج V (ويبر 2009) أمر بالغ الأهمية للمساعدة في تقليل عدد الأخطاء المُحددة لاحقاً أثناء التحقق من الصحة. توافق غالبية المشاركين على أن التحقق الرسمي يمكن أن يجعل النظام أكثر أماناً ويكون فائدة للسلامة الوظيفية (راجع القسمين 6.5 و6.6).

**تحديد المواصفات غير المتسقة مفيد في عمليات التطوير الواقعية.** استخلاص المتطلبات، وتحسين المتطلبات، وتطوير معماريات الأنظمة هي الخطوات الأولية في نموذج V (ويبر 2009). وبالتالي، فإن استخلاص المتطلبات وتحسين تلك المتطلبات أمر بالغ الأهمية لأنها تعمل كأساس لمزيد من تطوير الأنظمة وتحليل السلامة. الأخطاء والتعارضات المُدخَلة في هذه المراحل المبكرة، والمُحددة فقط في مراحل التطوير اللاحقة، تصبح مكلفة وقد تؤدي إلى أحداث كارثية. هناك احتمال كبير أن يتم تحديد معظم أخطاء السلامة الحرجة في وقت متأخر أثناء مرحلة التحقق من الصحة في الصناعة (بول وروب 2011).

**8.3 RQ3 – تسهيل استخدام الأساليب الرسمية**

يتم استخلاص الرؤى لـ RQ3 من المرحلة 2، تجربة المجموعة الواحدة بقياس قبلي وبعدي. يجمع RQ3 رؤى حول ما إذا كان المهندسون يفضلون استخدام الأساليب الرسمية (فاحصات النماذج على وجه الخصوص) إذا تم تقليل صعوبة فهم نتائج التحقق لتحديد المواصفات غير المتسقة، وخاصة مع نهج تفسير الأمثلة المضادة.

**نهج تفسير الأمثلة المضادة يسهل الفهم مقارنة بتفسير المُخرَجات الخام لفاحص النماذج.** أجاب ستة من 13 مشاركاً في تجربة المجموعة الواحدة بقياس قبلي وبعدي أنهم يفهمون نتيجة التحقق المُنتَجة بواسطة فاحص النماذج لنظام الوسادة الهوائية (القسم 7.4). كانت فرضيتنا الأولية أنه بإثبات تفسير إضافي سهل الاستخدام للأمثلة المضادة، سيكون من الأسهل للمهندسين فهم الخطأ وكذلك أنه يمكن أن يسهل استخدام الأساليب الرسمية بين المهندسين. تدعم النتائج المناقشة في القسم 7.4 هذه الفرضية، حيث تفضل الغالبية الساحقة من 12 من 13 مشاركاً تفسير الأمثلة المضادة مقارنة بفهم مُخرَجات فاحص النماذج.

**من الممكن للمهندسين تحديد وإصلاح المواصفات غير المتسقة بناءً على نهج تفسير الأمثلة المضادة.** مع المُخرَجات الخام لفاحص النماذج، يحدد خمسة فقط من 13 مشاركاً المواصفات غير المتسقة بشكل كامل أو جزئي صحيح. بينما مع تفسير الأمثلة المضادة، تمكن تسعة من 13 مشاركاً من تحديد المجموعة الكاملة من المواصفات غير المتسقة وشرح سبب التعارض بشكل صحيح من خلال فهم التفسير. يُظهر هذا بقوة أن تفسير الأمثلة المضادة يمكن أن يحسن بالفعل فهم الأخطاء وأن توفير مثل هذا التفسير يمكن أن يعزز استخدام الأساليب الرسمية بين المهندسين.

**نهج تفسير الأمثلة المضادة يمكن أن يعزز التحقق الرسمي واستخدام فحص النماذج في عمليات التطوير الواقعية.** من الاستجابات المجمعة، لدى غالبية المشاركين رأي إيجابي حيث يمكن لتفسير الأمثلة المضادة دعم الحفاظ على اتساق التحسين، ويمكن أن يكون قابلاً للاستخدام في عملية التطوير الواقعية (راجع القسم 7.8). التحدي الرئيسي الذي ذكره المشاركون هو أن الأدوات المُستخدمة حالياً في مشاريعهم لا تدعم دمج نهج تفسير الأمثلة المضادة المُقترح. يُظهر هذا أن دمج أدوات التحقق الموجودة مع الأدوات الصناعية يحتاج إلى أن يكون أحد التركيزات الأساسية لتحسين استخدام الأساليب الرسمية.

---

### Translation Notes

- **Key findings:**
  - Understanding formal notations and identifying inconsistencies are major challenges
  - Majority believe formal methods make systems safer
  - Counterexample explanation significantly improves comprehension (5/13 → 9/13 correct)
  - Integration with industrial tools is a key barrier

- **Special handling:**
  - Preserved V-model references (software development lifecycle model)
  - Maintained research question linkage (RQ1, RQ2, RQ3)
  - Kept section cross-references intact

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
