# Section 3: Convergence
## القسم 3: التقارب

**Section:** convergence
**Translation Quality:** 0.86
**Glossary Terms Used:** formal methods, B method, safety-critical, proof obligations, refinement, certification, compiler

---

### English Version

#### 3 Convergence

We have seen from the previous chapter that B and Event-B have matured over the last decade and are addressing well safety-critical industry topics¹³, at system level, at software level, and at configuration level. However using a formal method is not enough to demonstrate safety. For example, a software can't be SIL4-compliant by itself, even if it is developed with B. The hardware executing it has to be considered, especially its failure modes, and a sound specification at system level has to be elaborated accordingly. A safety demonstration requires a lot of experience, skills, time and energy to complete successfully.

We present in this chapter several new features, linked with B, that are directly contributing to the safety demonstration and that would ease the development and the certification processes of safety-critical systems.

¹³even if re-targeted to address more specific issues

**3.1 Low Cost High Integrity Platform**

LCHIP¹⁴ is a new technology, combining a complete software development environment based on the B language and a secured execution hardware platform, to ease the development of safety critical applications. It relies on several building blocks already used in certified railways products.

LCHIP relies on a software factory that automatically transforms function into binary code that runs on redundant hardware. The starting point is a text-based, B formal model that specifies the function to implement. This model may contain static and dynamic properties that define the functional boundaries of the target software.

This formal specification is then refined automatically into a B implementable model. Transformation rules are applied to the specification to gradually replace abstract variables and substitutions with concrete ones.

The implementable model is then translated using two different chains:
- Translation into C ANSI code, with the C4B Atelier B code generator (instance I1). This C code is then compiled into HEX¹⁵ binary code with an off-the-shelf compiler.
- Translation into MIPS Assembly then to HEX binary code, with a specific compiler developed for this purpose (instance I2). The translation in two steps allows to better debug the translation process as a MIPS assembly instruction corresponds to a HEX line.

¹⁴A short form of Low Cost High Integrity Platform
¹⁵a file format that conveys binary information in ASCII text form. It is commonly used for programming micro-controllers

**Fig. 5:** The safe generation and execution of a function on the double processor.

**3.1.1 Safety** These two different instances I1 and I2 of the same function are then executed in sequence, one after the other, on two PIC32 micro-controllers. Each micro-controller hosts both I1 and I2, so at any time 4 instances of the function are being executed on the micro-controllers. The results obtained by I1 and I2 are first compared locally on each micro-controller then they are compared between micro-controllers by using messages. In case of a divergent behavior (at least one of the four instances exhibits a different behavior), the faulty micro-controller reboots. The sequencer and the safety functions are developed once for all in B by the IDE design team and come along as a library. This way, the safety functions are out of reach of the developers and can't be altered. The safety is based on several features such as the detection of a divergent behavior, the detection of the inability for a processor to execute an instruction properly¹⁶ and the ability to command outputs¹⁷. Memory areas (code, data for the two instances) are also checked (no overlap, no address outside memory range).

¹⁶all instructions are tested regularly against an oracle
¹⁷outputs are read to check if commands are effective, a system not able to change the state of its outputs has to shutdown

**3.1.2 Target software** The execution platform is based on two PIC32 micro-controllers and provides an available power of 100 MIPS. This processing power is sufficient to update 50k interlocking Boolean equations per second, compatible with light-rail signaling requirements. The execution platform can be redesigned seamlessly for any kind of mono-core processor if a higher level of performance is required. Similar secured platforms are operating platform-screen doors in São Paulo L15 metro and in Stockholm City line. The Brazilian one has been recently certified at level SIL3 by CERTIFER on the inopportune opening failure of the doors.

The IDE provides a restricted modeling framework for software where:
- No operating system is used
- Software behavior is cyclic (no parallelism)
- No interruption modifies the software state variables
- Supported types are Boolean and integer types (and arrays of)
- Only bounded-complexity algorithms are supported (the price to pay to keep the refinement and proof process automatic)

The whole process, starting from the B model and finishing with the software running on the hardware platform, is expected to be fully automatic with the integration of the results obtained from some R&D projects¹⁸. In addition several in-house projects have helped to optimize the automatic refinement process by improving the refinement engine and by defining a subset of the B language, Simple B.

¹⁸to implement automatic refinement (ANR-RIMEL) and improve automatic proof performances (ANR-BWARE)

**3.1.3 Research and development** LCHIP [12] is developed by the eponymous French R&D project. It is aimed at allowing any engineer to develop a function by using its usual Domain Specific Language and to obtain this function running safely on a hardware platform. With the automatic development process, the B formal method will remain "behind the curtain" in order to avoid expert transactions.

As the safety demonstration doesn't require any specific feature for the input B model, it could be handwritten or the by-product of a translation process. So several DSL are planned to be supported at once (relays schematic, grafcet) based on an Open API (Bxml). The translation from relays schematic is being studied for the French Railways with a strong focus on the feedback between DSL and B: in case of unproven B proof obligations, it is mandatory to exhibit its source in the DSL model.

The project reuses a number of building blocks such as the C4B¹⁹ C code generator extended to support PIC memory model, and the B to Hex binary file in-house compiler supporting PIC32.

The IDE will be based on Atelier B 5.0, providing a simplified process-oriented GUI. A first starter kit, containing the IDE and the execution platform, will be publicly released by the end of 2017.

¹⁹Atelier B C code generator

**3.2 Proof Support Advances**

**3.2.1 Proof Support in Atelier B** A formal development demands that different aspects are verified using a mathematical proof. To this end, Atelier B produces automatically a number of proof obligations (POs). To assist the user in discharging POs, Atelier B has included a theorem prover since its inception. This "historical" theorem prover is an inference engine and an (extensible) rule database. It has been certified in the railway domain by expert review of both the inference engine and a core rule base. The architecture of the theorem prover is such that it can be used interactively, or automatically, at different force levels.

The user applies the theorem prover in batch to all the proof obligations, and is then left with a number of open POs. The remaining POs can be classified in three categories: valid, the theorem prover being unable to find the proof; unprovable, because the rule database is essentially incomplete; unprovable, because the user made a mistake in the formal development.

The top priority of the user is to ensure that there is no mistake, i.e., there is no PO of the last category. Visually inspecting the POs is often enough to detect most such errors, although there are also trickier mistakes that are only uncovered in the course of an interactive proof.

The user has then to discharge the unproved POs by interactive proof, and this is the most time-consuming task in a formal development. The prover of Atelier-B supports a number of commands to develop interactive proofs: hypotheses selection, case split, quantifier instantiation, equality rewriting, rule application, etc. A proof script is successful when the proof obligation has been shown valid. Once a script is successful, it is saved in the project database, and can be applied to other proof obligations. Actually, a script is often successful for more than one PO. To improve scripting capabilities and efficiency, the language has been enriched with pattern-matching constructs that enable more general proofs. However, we feel that the interactive proof process should be improved so that the user would only need to address "interesting" goals and sub-goals that require some human insight.

Since the specification language of the B method is undecidable, the user is allowed to write new rules to be taken into account by the inference engine. The risk of introducing inconsistencies is mitigated by two measures. The first measure consists in the inclusion of an alternative prover, based on tableaux, that is able to prove some of the rules automatically. The second measure applies to those rules that could not be proved automatically. It consists in the user writing a textual proof in natural language, that is then subject to validation by a third-party.

In the past year, Atelier B support for PO verification has been improved with two different tools, addressing this issue at different levels:
- **iapa** (Interface to Automatic Proof Agents) for batch processing of POs;
- **drudges** of the theorem prover for rapid processing of sub-goals in the interactive prover.

They are presented in turn in the following.

**3.2.2 iapa** The iapa extension for Atelier B gives access to a number of third-party provers to discharge POs [5]. In iapa, POs are not translated directly to the input format of these provers; instead the translation targets the format of a program verification platform that plays here the role of a gateway to such automatic provers, namely Why3 [3]. Each PO thus includes a prelude where the logic of the B expression language is formalized in Why3 [14]. The axiomatization of the B operators in Why3 has been fine tuned based on an industrial benchmark, resulting in significant improvement of the automatic proving capabilities in Atelier B on that benchmark [6].

**Fig. 6:** An annotated screenshot of iapa

As the proof obligations are produced automatically, they include all the hypotheses that are in scope at the point the PO is concerned about. It is often the case that the validity of the goal only depends on a small number of such hypotheses. However, at times, provers are not able to identify these relevant hypotheses and end up lost in the proof search space.

In order to address this issue, iapa includes a hypotheses selection functionality, where the user can identify a subset of the hypotheses, and only this subset is included in the proof obligation that is translated to Why3 and eventually processed by the provers. This functionality is available both through a graphical, point-and-click, interface and through a command line language. Subsets of hypotheses can be created according to the presence of some identifier or set of identifiers, then added to the proof obligation. Of course iapa also provides a function to extract a set of free identifiers from the goal or from some subset of hypotheses. These functionalities are built upon two kinds of entities that the user can create and manipulate: contexts (subsets of hypotheses) and lexicons (subsets of identifiers). Full details are available in [5]; iapa is part of Atelier B starting from version 4.5.

**3.2.3 Drudges of the interactive prover** The motivation for this functionality was born out of the feeling of frustration that the user of the interactive prover sometimes feels when she is faced with a seemingly trivial sub-goal, yet single command is able to discharge it. An example of such situation is when the current goal can be shown to be a consequence of the hypotheses using the theory of equality and propositional reasoning, but the terms involved are large or contain operators that get the automatic prover lost.

**Fig. 7:** Interface to the drudges in the window of the interactive prover

A general rule is that the less proficient the proof engine, the more efficient it is. So the rationale of the drudges of the interactive prover is to use automatic provers for simpler logics that are able to produce not only the result of the validity check, but also information on how they have reached their conclusion, and this information is then processed to produce guidance for the automatic prover of Atelier B.

**Fig. 8:** State after the successful completion of the drudges: with a single click, a new rule has been created (right panel) and applied (left panel) automatically, discharging the goal.

Candidate drudges are provers that are either proof producing, or at least able to generate a so-called unsat core, i.e. a subset of the hypotheses that are actually used in the proof. Such functions have been standardized through at least two initiatives: TPTP [16] and SMT [1]. The drudges currently in the latter category only (veriT [4] and Z3 [7]), as they implement the unsat core functionality. Given the unsat core, a proof rule for the Atelier B prover can be produced automatically, compiled and applied to the current goal. The drudges are available as a single click on a new button in the tool bar of the interactive prover (see figure 7). If the drudges are successful, the current goal is automatically discharged and the proof rule is added to the rule base of the component (see figure 8).

---

### النسخة العربية

#### 3 التقارب

لقد رأينا من الفصل السابق أن B و Event-B قد نضجا خلال العقد الماضي ويعالجان بشكل جيد موضوعات الصناعة الحرجة من حيث السلامة¹³، على مستوى النظام، وعلى مستوى البرمجيات، وعلى مستوى التكوين. ومع ذلك، فإن استخدام أسلوب رسمي ليس كافياً لإثبات السلامة. على سبيل المثال، لا يمكن أن تكون البرمجيات متوافقة مع SIL4 بحد ذاتها، حتى لو تم تطويرها بـ B. يجب أخذ الأجهزة التي تنفذها في الاعتبار، خاصة أوضاع الفشل الخاصة بها، ويجب وضع مواصفة سليمة على مستوى النظام وفقاً لذلك. يتطلب إثبات السلامة الكثير من الخبرة والمهارات والوقت والطاقة لإتمامه بنجاح.

نقدم في هذا الفصل عدة ميزات جديدة، مرتبطة بـ B، تساهم بشكل مباشر في إثبات السلامة والتي من شأنها تسهيل عمليات التطوير والاعتماد للأنظمة الحرجة من حيث السلامة.

¹³حتى لو تم إعادة توجيهها لمعالجة قضايا أكثر تحديداً

**3.1 منصة التكامل العالي منخفضة التكلفة**

LCHIP¹⁴ هي تقنية جديدة، تجمع بين بيئة تطوير برمجيات كاملة قائمة على لغة B ومنصة أجهزة تنفيذ آمنة، لتسهيل تطوير التطبيقات الحرجة من حيث السلامة. تعتمد على عدة كتل بناء مستخدمة بالفعل في منتجات السكك الحديدية المعتمدة.

تعتمد LCHIP على مصنع برمجيات يحول تلقائياً الدالة إلى كود ثنائي يعمل على أجهزة متكررة. نقطة البداية هي نموذج B رسمي نصي يحدد الدالة المراد تطبيقها. قد يحتوي هذا النموذج على خصائص ثابتة وديناميكية تحدد الحدود الوظيفية للبرمجيات المستهدفة.

ثم يتم تنقيح هذه المواصفة الرسمية تلقائياً إلى نموذج B قابل للتطبيق. يتم تطبيق قواعد التحويل على المواصفة لاستبدال المتغيرات والاستبدالات المجردة تدريجياً بأخرى ملموسة.

ثم تتم ترجمة النموذج القابل للتطبيق باستخدام سلسلتين مختلفتين:
- الترجمة إلى كود C ANSI، مع مولد كود C4B Atelier B (النسخة I1). ثم يتم تجميع كود C هذا إلى كود ثنائي HEX¹⁵ باستخدام مُجمّع جاهز.
- الترجمة إلى MIPS Assembly ثم إلى كود ثنائي HEX، مع مُجمّع محدد تم تطويره لهذا الغرض (النسخة I2). تسمح الترجمة في خطوتين بتصحيح أخطاء عملية الترجمة بشكل أفضل حيث أن تعليمة MIPS assembly تتوافق مع سطر HEX.

¹⁴الشكل المختصر لـ Low Cost High Integrity Platform (منصة التكامل العالي منخفضة التكلفة)
¹⁵تنسيق ملف ينقل المعلومات الثنائية في شكل نص ASCII. يُستخدم عادة لبرمجة المتحكمات الدقيقة

**الشكل 5:** التوليد والتنفيذ الآمنان لدالة على المعالج المزدوج.

**3.1.1 السلامة** يتم بعد ذلك تنفيذ هاتين النسختين المختلفتين I1 و I2 من نفس الدالة بالتسلسل، واحدة تلو الأخرى، على متحكمين دقيقين PIC32. يستضيف كل متحكم دقيق كلاً من I1 و I2، بحيث يتم تنفيذ 4 نُسخ من الدالة في أي وقت على المتحكمات الدقيقة. تتم مقارنة النتائج التي تم الحصول عليها من I1 و I2 أولاً محلياً على كل متحكم دقيق ثم تتم مقارنتها بين المتحكمات الدقيقة باستخدام الرسائل. في حالة السلوك المتباين (تُظهر واحدة على الأقل من النُسخ الأربع سلوكاً مختلفاً)، يُعيد المتحكم الدقيق المعيب التشغيل. يتم تطوير المُسلسِل ووظائف السلامة مرة واحدة للجميع في B من قبل فريق تصميم IDE وتأتي كمكتبة. بهذه الطريقة، وظائف السلامة بعيدة عن متناول المطورين ولا يمكن تغييرها. تعتمد السلامة على عدة ميزات مثل اكتشاف السلوك المتباين، واكتشاف عدم قدرة المعالج على تنفيذ تعليمة بشكل صحيح¹⁶ والقدرة على التحكم في المخرجات¹⁷. يتم أيضاً التحقق من مناطق الذاكرة (الكود، البيانات للنسختين) (لا تداخل، لا عنوان خارج نطاق الذاكرة).

¹⁶يتم اختبار جميع التعليمات بانتظام مقابل أوراكل
¹⁷تتم قراءة المخرجات للتحقق من فعالية الأوامر، يجب إيقاف النظام غير القادر على تغيير حالة مخرجاته

**3.1.2 البرمجيات المستهدفة** تعتمد منصة التنفيذ على متحكمين دقيقين PIC32 وتوفر قوة متاحة تبلغ 100 MIPS. هذه القوة المعالجة كافية لتحديث 50 ألف معادلة منطقية للترابط في الثانية، متوافقة مع متطلبات إشارات السكك الحديدية الخفيفة. يمكن إعادة تصميم منصة التنفيذ بسلاسة لأي نوع من المعالجات أحادية النواة إذا كان مطلوباً مستوى أعلى من الأداء. تعمل منصات مؤمنة مماثلة على أبواب الشاشة للمنصة في مترو ساو باولو L15 وفي خط مدينة ستوكهولم. تم اعتماد المنصة البرازيلية مؤخراً على مستوى SIL3 من قبل CERTIFER على فشل الفتح غير المناسب للأبواب.

توفر IDE إطار نمذجة مقيد للبرمجيات حيث:
- لا يُستخدم نظام تشغيل
- سلوك البرمجيات دوري (لا توازي)
- لا يُعدل أي انقطاع متغيرات حالة البرمجيات
- الأنواع المدعومة هي الأنواع المنطقية والأعداد الصحيحة (ومصفوفاتها)
- فقط الخوارزميات ذات التعقيد المحدود مدعومة (الثمن الذي يُدفع للحفاظ على عملية التنقيح والإثبات تلقائية)

من المتوقع أن تكون العملية بأكملها، بدءاً من نموذج B وانتهاءً بالبرمجيات التي تعمل على منصة الأجهزة، تلقائية بالكامل مع دمج النتائج التي تم الحصول عليها من بعض مشاريع البحث والتطوير¹⁸. بالإضافة إلى ذلك، ساعدت عدة مشاريع داخلية في تحسين عملية التنقيح التلقائي من خلال تحسين محرك التنقيح وتعريف مجموعة فرعية من لغة B، Simple B.

¹⁸لتطبيق التنقيح التلقائي (ANR-RIMEL) وتحسين أداء الإثبات التلقائي (ANR-BWARE)

**3.1.3 البحث والتطوير** تم تطوير LCHIP [12] من قبل مشروع البحث والتطوير الفرنسي الذي يحمل نفس الاسم. يهدف إلى السماح لأي مهندس بتطوير دالة باستخدام لغته الخاصة بالنطاق المعتادة والحصول على هذه الدالة تعمل بأمان على منصة أجهزة. مع عملية التطوير التلقائي، سيبقى الأسلوب الرسمي B "خلف الستار" لتجنب المعاملات الخبيرة.

نظراً لأن إثبات السلامة لا يتطلب أي ميزة محددة لنموذج B المُدخل، يمكن أن يكون مكتوباً يدوياً أو نتيجة ثانوية لعملية ترجمة. لذا من المخطط دعم عدة DSL دفعة واحدة (مخطط المرحلات، grafcet) بناءً على Open API (Bxml). تتم دراسة الترجمة من مخطط المرحلات للسكك الحديدية الفرنسية مع تركيز قوي على التغذية الراجعة بين DSL و B: في حالة التزامات إثبات B غير المُثبتة، من الإلزامي إظهار مصدرها في نموذج DSL.

يعيد المشروع استخدام عدد من كتل البناء مثل مولد كود C4B¹⁹ C الممتد لدعم نموذج ذاكرة PIC، ومُجمّع الملف الثنائي من B إلى Hex الداخلي الذي يدعم PIC32.

سيعتمد IDE على Atelier B 5.0، موفراً واجهة مستخدم رسومية موجهة للعمليات مبسطة. ستُطلق أول مجموعة بداية، تحتوي على IDE ومنصة التنفيذ، للجمهور بنهاية عام 2017.

¹⁹مولد كود C من Atelier B

**3.2 تقدم دعم الإثبات**

**3.2.1 دعم الإثبات في Atelier B** يتطلب التطوير الرسمي التحقق من جوانب مختلفة باستخدام إثبات رياضي. لهذه الغاية، ينتج Atelier B تلقائياً عدداً من التزامات الإثبات (POs). لمساعدة المستخدم في إبراء التزامات الإثبات، ضمّن Atelier B مُثبِت نظرية منذ بدايته. هذا المُثبِت "التاريخي" للنظرية هو محرك استدلال وقاعدة بيانات قواعد (قابلة للتوسع). تم اعتماده في مجال السكك الحديدية من خلال مراجعة الخبراء لكل من محرك الاستدلال وقاعدة القواعد الأساسية. معمارية مُثبِت النظرية هي بحيث يمكن استخدامه بشكل تفاعلي، أو تلقائياً، في مستويات قوة مختلفة.

يطبق المستخدم مُثبِت النظرية على دفعات لجميع التزامات الإثبات، ثم يُترك مع عدد من التزامات الإثبات المفتوحة. يمكن تصنيف التزامات الإثبات المتبقية في ثلاث فئات: صالحة، لكن مُثبِت النظرية غير قادر على إيجاد الإثبات؛ غير قابلة للإثبات، لأن قاعدة البيانات للقواعد غير مكتملة بشكل أساسي؛ غير قابلة للإثبات، لأن المستخدم ارتكب خطأ في التطوير الرسمي.

الأولوية القصوى للمستخدم هي التأكد من عدم وجود خطأ، أي عدم وجود التزام إثبات من الفئة الأخيرة. غالباً ما يكون الفحص البصري لالتزامات الإثبات كافياً لاكتشاف معظم هذه الأخطاء، على الرغم من وجود أخطاء أكثر صعوبة لا يتم الكشف عنها إلا أثناء إثبات تفاعلي.

يتعين على المستخدم بعد ذلك إبراء التزامات الإثبات غير المُثبتة من خلال الإثبات التفاعلي، وهذه هي المهمة الأكثر استهلاكاً للوقت في التطوير الرسمي. يدعم مُثبِت Atelier-B عدداً من الأوامر لتطوير إثباتات تفاعلية: اختيار الفرضيات، تقسيم الحالة، إنشاء مثيل للمُحدد الكمي، إعادة كتابة المساواة، تطبيق القاعدة، إلخ. يكون البرنامج النصي للإثبات ناجحاً عندما يتم إظهار صحة التزام الإثبات. بمجرد نجاح البرنامج النصي، يتم حفظه في قاعدة بيانات المشروع، ويمكن تطبيقه على التزامات إثبات أخرى. في الواقع، غالباً ما يكون البرنامج النصي ناجحاً لأكثر من التزام إثبات واحد. لتحسين قدرات البرمجة النصية والكفاءة، تم إثراء اللغة ببُنى مطابقة الأنماط التي تُمكّن من إثباتات أكثر عمومية. ومع ذلك، نشعر أن عملية الإثبات التفاعلي يجب أن تُحسّن بحيث يحتاج المستخدم فقط لمعالجة الأهداف والأهداف الفرعية "المثيرة للاهتمام" التي تتطلب بعض البصيرة البشرية.

نظراً لأن لغة المواصفة لأسلوب B غير قابلة للحسم، يُسمح للمستخدم بكتابة قواعد جديدة ليأخذها محرك الاستدلال في الاعتبار. يتم تخفيف خطر إدخال التناقضات من خلال إجراءين. يتمثل الإجراء الأول في تضمين مُثبِت بديل، يعتمد على الجداول، قادر على إثبات بعض القواعد تلقائياً. ينطبق الإجراء الثاني على تلك القواعد التي لا يمكن إثباتها تلقائياً. يتكون من كتابة المستخدم لإثبات نصي بلغة طبيعية، يخضع بعد ذلك للتحقق من قبل طرف ثالث.

في العام الماضي، تم تحسين دعم Atelier B للتحقق من التزامات الإثبات بأداتين مختلفتين، تعالجان هذه القضية على مستويات مختلفة:
- **iapa** (واجهة وكلاء الإثبات التلقائيين) لمعالجة الدفعات من التزامات الإثبات؛
- **drudges** من مُثبِت النظرية لمعالجة سريعة للأهداف الفرعية في المُثبِت التفاعلي.

يتم عرضها بالتناوب في ما يلي.

**3.2.2 iapa** توفر امتداد iapa لـ Atelier B الوصول إلى عدد من مُثبِتات الطرف الثالث لإبراء التزامات الإثبات [5]. في iapa، لا تُترجم التزامات الإثبات مباشرة إلى تنسيق الإدخال لهذه المُثبِتات؛ بدلاً من ذلك تستهدف الترجمة تنسيق منصة التحقق من البرامج التي تلعب هنا دور بوابة إلى مثل هذه المُثبِتات التلقائية، وهي Why3 [3]. وبالتالي، يتضمن كل التزام إثبات مقدمة حيث يتم إضفاء الطابع الرسمي على منطق لغة التعبير B في Why3 [14]. تم ضبط بديهيات عوامل B في Why3 بدقة بناءً على معيار مرجعي صناعي، مما أدى إلى تحسن كبير في قدرات الإثبات التلقائي في Atelier B على هذا المعيار المرجعي [6].

**الشكل 6:** لقطة شاشة مُعلّقة لـ iapa

نظراً لأن التزامات الإثبات يتم إنتاجها تلقائياً، فإنها تتضمن جميع الفرضيات التي تكون في النطاق عند النقطة التي يهتم بها التزام الإثبات. غالباً ما تكون صحة الهدف تعتمد فقط على عدد صغير من هذه الفرضيات. ومع ذلك، في بعض الأحيان، لا تستطيع المُثبِتات تحديد هذه الفرضيات ذات الصلة وينتهي بها الأمر تائهة في مساحة بحث الإثبات.

من أجل معالجة هذه القضية، يتضمن iapa وظيفة اختيار الفرضيات، حيث يمكن للمستخدم تحديد مجموعة فرعية من الفرضيات، وفقط هذه المجموعة الفرعية يتم تضمينها في التزام الإثبات الذي يُترجم إلى Why3 ويتم معالجته في النهاية من قبل المُثبِتات. هذه الوظيفة متاحة من خلال واجهة رسومية بالنقر والإشارة ومن خلال لغة سطر الأوامر. يمكن إنشاء مجموعات فرعية من الفرضيات وفقاً لوجود معرّف معين أو مجموعة من المعرفات، ثم إضافتها إلى التزام الإثبات. بالطبع، يوفر iapa أيضاً دالة لاستخراج مجموعة من المعرفات الحرة من الهدف أو من بعض المجموعات الفرعية من الفرضيات. هذه الوظائف مبنية على نوعين من الكيانات التي يمكن للمستخدم إنشاؤها والتعامل معها: السياقات (مجموعات فرعية من الفرضيات) والمعاجم (مجموعات فرعية من المعرفات). التفاصيل الكاملة متاحة في [5]؛ iapa جزء من Atelier B ابتداءً من الإصدار 4.5.

**3.2.3 Drudges للمُثبِت التفاعلي** ولد الدافع لهذه الوظيفة من الشعور بالإحباط الذي يشعر به مستخدم المُثبِت التفاعلي أحياناً عندما يواجه هدفاً فرعياً يبدو بسيطاً، لكن لا يستطيع أمر واحد إبراءه. مثال على هذا الموقف هو عندما يمكن إظهار أن الهدف الحالي نتيجة للفرضيات باستخدام نظرية المساواة والمنطق القضوي، لكن المصطلحات المتضمنة كبيرة أو تحتوي على عوامل تجعل المُثبِت التلقائي يتوه.

**الشكل 7:** واجهة drudges في نافذة المُثبِت التفاعلي

قاعدة عامة هي أنه كلما كان محرك الإثبات أقل كفاءة، كلما كان أكثر فعالية. لذا فإن المنطق وراء drudges للمُثبِت التفاعلي هو استخدام مُثبِتات تلقائية لمنطقيات أبسط قادرة على إنتاج ليس فقط نتيجة فحص الصحة، ولكن أيضاً معلومات حول كيفية توصلهم إلى استنتاجهم، ويتم بعد ذلك معالجة هذه المعلومات لإنتاج إرشادات للمُثبِت التلقائي لـ Atelier B.

**الشكل 8:** الحالة بعد الإكمال الناجح لـ drudges: بنقرة واحدة، تم إنشاء قاعدة جديدة (اللوحة اليمنى) وتطبيقها (اللوحة اليسرى) تلقائياً، وإبراء الهدف.

المُثبِتات المرشحة لـ drudges هي مُثبِتات إما منتجة للإثبات، أو على الأقل قادرة على توليد ما يسمى unsat core، أي مجموعة فرعية من الفرضيات التي تُستخدم فعلياً في الإثبات. تم توحيد مثل هذه الوظائف من خلال مبادرتين على الأقل: TPTP [16] و SMT [1]. توجد drudges حالياً في الفئة الأخيرة فقط (veriT [4] و Z3 [7])، حيث تطبق وظيفة unsat core. بالنظر إلى unsat core، يمكن إنتاج قاعدة إثبات لمُثبِت Atelier B تلقائياً، وتجميعها وتطبيقها على الهدف الحالي. تتوفر drudges بنقرة واحدة على زر جديد في شريط الأدوات للمُثبِت التفاعلي (انظر الشكل 7). إذا نجحت drudges، يتم إبراء الهدف الحالي تلقائياً وتُضاف قاعدة الإثبات إلى قاعدة قواعد المكون (انظر الشكل 8).

---

### Translation Notes

- **Figures referenced:** Figure 5 (double processor execution), Figure 6 (iapa screenshot), Figure 7 (drudges interface), Figure 8 (drudges completion)
- **Key terms introduced:**
  - LCHIP = LCHIP (Low Cost High Integrity Platform)
  - IDE = بيئة التطوير المتكاملة
  - PIC32 = PIC32 (microcontroller family, kept as acronym)
  - MIPS = MIPS (processor architecture, kept as acronym)
  - HEX = HEX (file format, kept as acronym)
  - DSL (Domain Specific Language) = لغة خاصة بالنطاق
  - iapa = iapa (Interface to Automatic Proof Agents)
  - Why3 = Why3 (verification platform)
  - drudges = drudges (proof assistance tool)
  - unsat core = unsat core (unsatisfiable core)
  - SMT = SMT (Satisfiability Modulo Theories)
  - TPTP = TPTP (Thousands of Problems for Theorem Provers)
- **Equations:** 0
- **Citations:** [3] Why3, [4] veriT, [5] iapa details, [6] benchmark improvement, [7] Z3, [12] LCHIP, [14] B formalization in Why3, [16] TPTP, [1] SMT
- **Special handling:**
  - Technical acronyms (LCHIP, PIC32, MIPS, HEX, DSL, SMT, TPTP) kept in English
  - Tool and system names (Atelier B, Why3, iapa, veriT, Z3) kept in original form
  - Project names (ANR-RIMEL, ANR-BWARE) kept as acronyms
  - City/location names (São Paulo, Stockholm) kept in original form with proper Arabic transliteration where applicable
  - Technical metrics preserved (100 MIPS, 50k equations, etc.)
  - Footnotes maintained with Arabic numbering
  - "Simple B" kept as proper noun for the B language subset

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
