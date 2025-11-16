# Section 4: Intersegment Linking and Addressing
## القسم 4: الربط والعنونة بين المقاطع

**Section:** intersegment-linking
**Translation Quality:** 0.86
**Glossary Terms Used:** dynamic linking, pure procedure, segment, linkage section, symbolic name, path name, reference name, symbol table, link data, stack segment, frame

---

### English Version

The ability of many users to share access to procedure and data information, and the power of being able to construct complex procedures by building on the work of others are two prime desiderata of multiprocess computer systems. The potential value of these features to the advancement of computer applications should not be underestimated. The design of a system around the notion of a generalized, location-independent address is an essential ingredient in meeting these objectives. It remains to show how the sharing of data and procedure segments, and the building of programs out of component procedure segments can be implemented within the framework of the Multics addressing mechanisms just described. In particular we must show how references to external data (and procedure) segments occurring within a shared procedure segment can be correctly interpreted for each of possibly many processes running concurrently.

#### Requirements

Necessary properties of a satisfactory intersegment addressing arrangement include the following:

1. **Procedure segments must be pure**, that is, their execution must not cause a single word of their content to be modified.

   Pure procedure is a recognized requirement for general sharing of procedure information.

2. **It must be possible for a process to call a routine by its symbolic name without having made prior arrangements for its use.**

   This means that the subroutine (which could invoke in turn an arbitrarily large collection of other procedures) must be able to provide space for its data, must be able to reference any needed data object, and must be able to call on further routines that may be unknown to its caller.

3. **Segments of a procedure must be invariant to the recompilation of other segments.**

   This requirement has the following implication: The values of identifiers that denote addresses within a segment which may change with recompilation must not appear in the content of any other segment.

#### Making a segment known

Meeting condition (1) requires that a segment be callable by a process even if no position in the descriptor segment of the process has been reserved for the segment. Hence a mechanism is provided in the system for assigning a position in the descriptor segment (a segment number) when the process first makes reference to the segment by means of its symbolic name. We call this operation making the segment **known** to the process. Once a segment is known, the process may reference it by its segment number.

The pattern of descriptor segment assignment will be different for each process. Therefore it is not possible, in general, for the system to assign a unique segment number to a shared routine or data object. This fact is a major consideration in the design of the linking mechanism. In the following paragraphs we describe a scheme for implementing the linkage of segments that meets the requirements stated above.

It is worth emphasizing that this discussion has nothing to do with the memory management problem that the supervisor faces in deciding where in the storage hierarchy information should reside. All information involved in the linkage mechanism is, as will be seen, referenced by generalized addresses which are made effective by the mechanisms described earlier. The fact that pages of the segments referred to in the following discussion may be in or out of main memory at the time a process requires access to them, is irrelevant.

#### Linkage data

Before a segment becomes known to a process the segment may only be referenced by means of a symbolic **path name** [2] which permanently identifies the segment within the directory structure. Since the segment number used to reference a particular segment is process dependent, segment numbers may not appear internally in pure procedure code. For this reason, a segment is identified within a procedure segment by a symbolic **segment reference name**. Before a procedure can complete an external segment reference, the reference name must be translated into a path name by means of a directory searching algorithm and the desired segment made known to the process. Once the segment has become known to the process, we wish to substitute the efficient addressing mechanism based on the generalized address for the time-consuming operation of searching the directory structure.

Consider a procedure segment P that makes reference to a word at location x within data segment D, as illustrated in Figure 9. In assembly language this would be written as

`OPR <D>|[x]`

The angle brackets indicate that the enclosed character string is the reference name of some segment. This name will be used to search the directory structure the first time segment P is referenced by a process. The square brackets indicate that the enclosed character string is a symbolic address within an external segment.

**Figure 9:** An intersegment reference by procedure P. (Shows procedure P with linkage section and data segment D)

Since by requirement (3) we wish segment P to be invariant to recompilation of D, only the symbolic address [x] may appear in P. Furthermore, we wish to delay the evaluation of [x] until a reference to it is actually made in the running of a process.

The following problem arises: Initially process α in executing procedure P may reference <D>|[x] only by symbolic segment name and symbolic external address. After segment D has been made known to process α, and a first reference has been effected, we wish to make further references by the generalized address d#α|x. The question is: How can we make the transition from symbolic reference to generalized addressing without altering the content of segment P?

It should be clear that a change must be made **some** place that can effect the change in addressing mechanism. Further, the data that is changed must participate in **every** reference to the information. We will call the information that is altered in value to make this transition the **link data** for linking segment P to symbolic addresses <D>|[x] in process α. The collection of link data for all external references originating in segment P is called the **linkage section** of procedure P.

Link data is private data of its process because whether P is linked to D|x for process α is entirely independent of whether the same is true for any other process. Therefore, whenever a procedure segment is made known to a process a copy of the procedure's linkage section is made as a segment within that process. In certain cases the linkage sections of several procedures are combined into a single linkage segment private to the process.

#### Linking

Figure 10 shows segments P, D and the linkage section Lα for P in process α. To implement reference to D|x from within segment P will require two references by generalized address: one to access the pertinent link data in Lα, and one to fetch the word addressed in segment D. Realization of this minimum number of references implies use of the indirect addressing feature of the processor. Thus the link data for an established link will be an indirect word pair containing the generalized address D#α|x (Figure 11a). Before the link is established, an attempt by a process of computation α to reference D|x through the link must lead to a trap of the process and transfer of control to the system routines that will establish the link and continue operation of the process. For this purpose a special form of indirect word pair is used which causes the desired trap. In Figure 11b this is indicated by the code **ft** in the addressing mode field of the pair. The segment number and word number fields of the indirect word can then be used to inform supervisory routines of the place to look to find the symbolic address <D>|[x] associated with the link. This address must be translated into a generalized address to establish the link. The operation of changing the link data to establish a link is called **linking**.

**Figure 10:** Linkage of P to D|x for process α. (Shows procedure P, linkage section Lα, and data segment D)

**Figure 11:** States of the link data. (Shows two states: (a) established link with its code, (b) unestablished link with ft code)

It is desirable to keep the procedure segment P self-contained if at all possible. Consequently the symbolic address <D>|[x] pointed to by the un-established link should be part of the procedure segment P. Two look-up operations are required on the part of supervisory routines to establish the link. The symbolic reference name D must be associated with a specific segment through a search in the directory structure, and this segment must be made known to the process if a segment number has not already been assigned.

The word number corresponding to the symbolic word name x must also be determined. The set of associations between symbolic word names and word numbers for a segment is its **symbol table** and is part of the segment. Thus, in our example, a list of word numbers corresponding to symbolic word names that may appear in references to segment D from other segments is included as part of segment D at a standard position known to the system. This list is searched by a system routine to find the word number required to establish a link.

#### The link pointer

A remaining question is: How does a process produce the generalized address L#α|w required to access the link data? One might suppose that word address w could be fixed permanently at the time procedure segment P was created. This is not possible because the set of segments required by each process that might share use of procedure P will in general be unrelated: If the linkage sections of several procedures were placed in a single segment, assigning a fixed position to a link for all processes would produce intolerable conflicts. On the other hand, the code by which an intersegment reference is represented in segment P must be fixed and identical for all computations to meet the pure procedure constraint. Any data that allows different addresses to be formed from fixed code must reside in processor registers. By this argument we see the necessity of associating a linkage pointer with each process. The **linkage pointer** is a generalized address that resides in a dedicated base register (designated **lp**). As shown in Figure 12, it is the origin L#α|s of the portion of a linkage segment that contains the links for intersegment references made from the segment being executed.

References to external segments are coded relative to the link pointer and have the form shown in Figure 12. The displacement k is determined by the coding of P and is invariant with respect to the process using P.

**Figure 12:** Addressing the link data. (Shows how linkage pointer lp and displacement k are used to form generalized address to link data)

#### Procedure Call and Return

The coding used to transfer control to a sub-procedure and the subsequent return of control must meet the requirements of programming generality. In particular, no assumptions may be made regarding the detailed coding of either the calling or called procedure other than those aspects uniformly established by convention. Conventions for four aspects of subroutine calling are relatively familiar:

1. Transmission of arguments

2. Arranging for return of control

3. Saving and restoring processor state

4. Allocating private storage for the called procedure.

Item (4) is necessary in Multics because of the pure procedure requirement, and the generality requirement which forbids prior arrangement of a called procedure's storage needs. This private storage is supplied by associating the **stack segment** with each process in which a **frame** of private storage is reserved at each procedure call. The frame is released upon return of control. This mechanism is implemented by the stack pointer (designated **sp**) which is the generalized address of the stack frame origin for the procedure in operation. The use of the stack segment makes every procedure in Multics automatically recursive by associating separate stack frames with successive entries into the same procedure. Due to the pure procedure requirement, only fixed arguments that do not depend on segment numbers may appear in procedure segments. Pointers and variable arguments must be placed in the stack segment, the linkage segment, or elsewhere. So that the language designer may have his choice of implementation, the argument pointer (designated **ap**) is at procedure entry the generalized address of the list of arguments for the called procedure.

In addition to these conventional requirements, the method of dynamic linking just described introduces one new problem: When process α, in executing procedure P, transfers control to procedure Q, the value of linkage pointer must be changed to the generalized address of the linkage section for procedure Q. Since the new value of the linkage pointer contains a segment number, it is private data of process α and cannot be placed in segment P or Q.

This problem requires a somewhat modified form of intersegment linkage from that used for data references. Since it is desirable that the machine code necessary to load the linkage pointer for a procedure segment be associated with that segment, the following solution was adopted. For each external entry point within a procedure segment two additional instructions are placed in the procedure's linkage section at compilation time. The first instruction loads the linkage pointer with the appropriate value at procedure entry, and the second instruction transfers control to the entry point in the called procedure segment. Thus in establishing the link for an external procedure call, the generalized indirect address placed in the calling procedure's link data points to the corresponding instruction pair in the linkage section of the procedure being called. When control passes to the linkage segment during an external procedure call, the segment number portion of the desired linkage pointer is easily obtained from the procedure base register, since the process is now executing in the desired linkage segment.

Figure 13 depicts the linkage mechanism required for an external procedure call from procedure P to segment Q at entry point e. The solid lines indicate the individual steps taken through indirect addresses while the dashed lines indicate resulting flow of control.

**Figure 13:** Linkage mechanism for procedure entry. (Shows procedure P, linkage sections, and procedure Q with arrows indicating control flow)

In executing a call to an external procedure, the caller's machine conditions, including the procedure base register and program counter, are saved in the stack segment by the caller. Return from the called procedure can thus be effected by simply restoring the caller's machine conditions from the stack segment.

---

### النسخة العربية

إن قدرة العديد من المستخدمين على مشاركة الوصول إلى معلومات الإجراءات والبيانات، وقوة القدرة على بناء إجراءات معقدة بالبناء على عمل الآخرين هما من الرغبات الأساسية لأنظمة الحاسوب متعددة العمليات. يجب عدم التقليل من القيمة المحتملة لهذه الميزات لتقدم تطبيقات الحاسوب. إن تصميم نظام حول فكرة العنوان المعمم المستقل عن الموقع هو عنصر أساسي في تحقيق هذه الأهداف. يبقى أن نُظهر كيف يمكن تنفيذ مشاركة مقاطع البيانات والإجراءات، وبناء البرامج من مقاطع إجراءات مكونة ضمن إطار آليات العنونة في مَلتِكس التي وُصفت للتو. على وجه الخصوص يجب أن نُظهر كيف يمكن تفسير المراجع لمقاطع البيانات (والإجراءات) الخارجية التي تحدث داخل مقطع إجراء مشترك بشكل صحيح لكل من العديد من العمليات التي قد تعمل بشكل متزامن.

#### المتطلبات

تتضمن الخصائص الضرورية لترتيب عنونة مُرضٍ بين المقاطع ما يلي:

1. **يجب أن تكون مقاطع الإجراءات نقية**، أي أن تنفيذها يجب ألا يتسبب في تعديل كلمة واحدة من محتواها.

   الإجراء النقي متطلب معترف به للمشاركة العامة لمعلومات الإجراءات.

2. **يجب أن يكون من الممكن للعملية استدعاء روتين باسمه الرمزي دون إجراء ترتيبات مسبقة لاستخدامه.**

   هذا يعني أن الروتين الفرعي (الذي يمكن أن يستدعي بدوره مجموعة كبيرة بشكل تعسفي من الإجراءات الأخرى) يجب أن يكون قادراً على توفير مساحة لبياناته، ويجب أن يكون قادراً على الإشارة إلى أي كائن بيانات مطلوب، ويجب أن يكون قادراً على استدعاء روتينات أخرى قد تكون غير معروفة لاستدعائه.

3. **يجب أن تكون مقاطع الإجراء ثابتة لإعادة التصريف للمقاطع الأخرى.**

   هذا المتطلب له التضمين التالي: قيم المعرفات التي تدل على عناوين داخل مقطع والتي قد تتغير مع إعادة التصريف يجب ألا تظهر في محتوى أي مقطع آخر.

#### جعل المقطع معروفاً

يتطلب استيفاء الشرط (1) أن يكون المقطع قابلاً للاستدعاء بواسطة عملية حتى إذا لم يتم حجز موضع في مقطع الواصف للعملية للمقطع. وبالتالي يتم توفير آلية في النظام لتعيين موضع في مقطع الواصف (رقم مقطع) عندما تقوم العملية بإجراء إشارة أولى إلى المقطع عن طريق اسمه الرمزي. نسمي هذه العملية جعل المقطع **معروفاً** للعملية. بمجرد أن يكون المقطع معروفاً، قد تشير العملية إليه برقم مقطعه.

سيكون نمط تعيين مقطع الواصف مختلفاً لكل عملية. لذلك ليس من الممكن، بشكل عام، للنظام تعيين رقم مقطع فريد لروتين مشترك أو كائن بيانات. هذه الحقيقة هي اعتبار رئيسي في تصميم آلية الربط. في الفقرات التالية نصف مخططاً لتنفيذ ربط المقاطع الذي يلبي المتطلبات المذكورة أعلاه.

من الجدير بالتأكيد أن هذه المناقشة ليس لها علاقة بمشكلة إدارة الذاكرة التي يواجهها المشرف في تحديد مكان وجود المعلومات في التسلسل الهرمي للتخزين. جميع المعلومات المشاركة في آلية الربط، كما سيُرى، يُشار إليها بالعناوين المعممة التي تُجعل فعالة بواسطة الآليات الموضحة سابقاً. حقيقة أن صفحات المقاطع المشار إليها في المناقشة التالية قد تكون داخل أو خارج الذاكرة الرئيسية في الوقت الذي تتطلب فيه العملية الوصول إليها، غير ذات صلة.

#### بيانات الربط

قبل أن يصبح المقطع معروفاً للعملية، قد يُشار إلى المقطع فقط عن طريق **اسم المسار** الرمزي [2] الذي يحدد المقطع بشكل دائم داخل بنية الدليل. نظراً لأن رقم المقطع المستخدم للإشارة إلى مقطع معين يعتمد على العملية، فإن أرقام المقاطع قد لا تظهر داخلياً في كود الإجراء النقي. لهذا السبب، يتم تحديد المقطع داخل مقطع إجراء باسم **اسم مرجع المقطع** الرمزي. قبل أن يتمكن الإجراء من إكمال مرجع مقطع خارجي، يجب ترجمة اسم المرجع إلى اسم مسار عن طريق خوارزمية بحث الدليل ويجب جعل المقطع المطلوب معروفاً للعملية. بمجرد أن يصبح المقطع معروفاً للعملية، نرغب في استبدال آلية العنونة الفعالة القائمة على العنوان المعمم بعملية البحث المستهلكة للوقت في بنية الدليل.

لنعتبر مقطع إجراء P الذي يشير إلى كلمة في الموقع x داخل مقطع البيانات D، كما هو موضح في الشكل 9. في لغة التجميع سيُكتب هذا كـ

`OPR <D>|[x]`

تشير الأقواس الزاوية إلى أن السلسلة النصية المرفقة هي اسم المرجع لبعض المقاطع. سيُستخدم هذا الاسم للبحث في بنية الدليل في المرة الأولى التي يُشار فيها إلى المقطع P بواسطة عملية. تشير الأقواس المربعة إلى أن السلسلة النصية المرفقة هي عنوان رمزي داخل مقطع خارجي.

**الشكل 9:** إشارة بين المقاطع بواسطة الإجراء P. (يُظهر الإجراء P مع قسم الربط ومقطع البيانات D)

نظراً لأننا نرغب بالمتطلب (3) في أن يكون المقطع P ثابتاً لإعادة تصريف D، فقد يظهر فقط العنوان الرمزي [x] في P. علاوة على ذلك، نرغب في تأخير تقييم [x] حتى يتم إجراء إشارة إليه فعلياً في تشغيل العملية.

تنشأ المشكلة التالية: في البداية قد تشير العملية α في تنفيذ الإجراء P إلى <D>|[x] فقط باسم المقطع الرمزي والعنوان الخارجي الرمزي. بعد جعل المقطع D معروفاً للعملية α، وبعد إجراء إشارة أولى، نرغب في إجراء مراجع أخرى بالعنوان المعمم d#α|x. السؤال هو: كيف يمكننا إجراء الانتقال من الإشارة الرمزية إلى العنونة المعممة دون تغيير محتوى المقطع P؟

يجب أن يكون واضحاً أن التغيير يجب أن يتم في **مكان ما** يمكن أن يؤثر على التغيير في آلية العنونة. علاوة على ذلك، يجب أن تشارك البيانات التي تم تغييرها في **كل** إشارة إلى المعلومات. سنسمي المعلومات التي تم تغيير قيمتها لإجراء هذا الانتقال **بيانات الربط** لربط المقطع P بالعناوين الرمزية <D>|[x] في العملية α. يُسمى مجموعة بيانات الربط لجميع المراجع الخارجية الناشئة في المقطع P **قسم الربط** للإجراء P.

بيانات الربط هي بيانات خاصة لعمليتها لأن ما إذا كان P مرتبطاً بـ D|x للعملية α مستقل تماماً عما إذا كان نفس الشيء صحيحاً لأي عملية أخرى. لذلك، كلما أصبح مقطع إجراء معروفاً لعملية، يتم عمل نسخة من قسم الربط للإجراء كمقطع داخل تلك العملية. في حالات معينة، يتم دمج أقسام الربط لعدة إجراءات في مقطع ربط واحد خاص بالعملية.

#### الربط

يُظهر الشكل 10 المقاطع P و D وقسم الربط Lα لـ P في العملية α. لتنفيذ الإشارة إلى D|x من داخل المقطع P سيتطلب مرجعين بالعنوان المعمم: واحد للوصول إلى بيانات الربط ذات الصلة في Lα، وواحد لجلب الكلمة المعنونة في المقطع D. يعني تحقيق هذا العدد الأدنى من المراجع استخدام ميزة العنونة غير المباشرة للمعالج. وبالتالي فإن بيانات الربط لرابط منشأ ستكون زوج كلمات غير مباشر يحتوي على العنوان المعمم D#α|x (الشكل 11a). قبل إنشاء الرابط، يجب أن تؤدي محاولة العملية للحساب α للإشارة إلى D|x من خلال الرابط إلى احتجاز العملية ونقل التحكم إلى روتينات النظام التي ستنشئ الرابط وتستمر في تشغيل العملية. لهذا الغرض، يتم استخدام شكل خاص من زوج الكلمات غير المباشر الذي يسبب الاحتجاز المطلوب. في الشكل 11b يُشار إلى هذا بالكود **ft** في حقل نمط العنونة للزوج. يمكن بعد ذلك استخدام حقول رقم المقطع ورقم الكلمة للكلمة غير المباشرة لإبلاغ الروتينات الإشرافية بالمكان الذي يجب البحث فيه للعثور على العنوان الرمزي <D>|[x] المرتبط بالرابط. يجب ترجمة هذا العنوان إلى عنوان معمم لإنشاء الرابط. تُسمى عملية تغيير بيانات الربط لإنشاء رابط **الربط**.

**الشكل 10:** ربط P بـ D|x للعملية α. (يُظهر الإجراء P، وقسم الربط Lα، ومقطع البيانات D)

**الشكل 11:** حالات بيانات الربط. (يُظهر حالتين: (a) رابط منشأ بكود its، (b) رابط غير منشأ بكود ft)

من المرغوب الحفاظ على مقطع الإجراء P مستقلاً قدر الإمكان. وبالتالي يجب أن يكون العنوان الرمزي <D>|[x] الذي يُشير إليه الرابط غير المنشأ جزءاً من مقطع الإجراء P. تتطلب عمليتا بحث من جانب الروتينات الإشرافية لإنشاء الرابط. يجب ربط اسم المرجع الرمزي D بمقطع معين من خلال بحث في بنية الدليل، ويجب جعل هذا المقطع معروفاً للعملية إذا لم يتم بالفعل تعيين رقم مقطع.

يجب أيضاً تحديد رقم الكلمة المقابل لاسم الكلمة الرمزي x. مجموعة الارتباطات بين أسماء الكلمات الرمزية وأرقام الكلمات للمقطع هي **جدول الرموز** الخاص به وهو جزء من المقطع. وبالتالي، في مثالنا، يتم تضمين قائمة من أرقام الكلمات المقابلة لأسماء الكلمات الرمزية التي قد تظهر في الإشارات إلى المقطع D من مقاطع أخرى كجزء من المقطع D في موضع قياسي معروف للنظام. يتم البحث في هذه القائمة بواسطة روتين نظام للعثور على رقم الكلمة المطلوب لإنشاء رابط.

#### مؤشر الربط

السؤال المتبقي هو: كيف تنتج العملية العنوان المعمم L#α|w المطلوب للوصول إلى بيانات الربط؟ قد يُفترض أن عنوان الكلمة w يمكن أن يكون ثابتاً بشكل دائم في الوقت الذي تم فيه إنشاء مقطع الإجراء P. هذا غير ممكن لأن مجموعة المقاطع المطلوبة من قبل كل عملية قد تشارك في استخدام الإجراء P ستكون بشكل عام غير مرتبطة: إذا تم وضع أقسام الربط لعدة إجراءات في مقطع واحد، فإن تعيين موضع ثابت لرابط لجميع العمليات سينتج تضاربات لا يمكن تحملها. من ناحية أخرى، يجب أن يكون الكود الذي يتم به تمثيل إشارة بين المقاطع في المقطع P ثابتاً ومتطابقاً لجميع الحسابات لتلبية قيد الإجراء النقي. يجب أن توجد أي بيانات تسمح بتكوين عناوين مختلفة من كود ثابت في سجلات المعالج. من خلال هذه الحجة نرى ضرورة ربط مؤشر الربط بكل عملية. **مؤشر الربط** هو عنوان معمم يوجد في سجل قاعدة مخصص (مُعيَّن **lp**). كما هو موضح في الشكل 12، إنه الأصل L#α|s من الجزء من مقطع الربط الذي يحتوي على الروابط لمراجع بين المقاطع المُجراة من المقطع الذي يتم تنفيذه.

يتم ترميز المراجع إلى المقاطع الخارجية نسبة إلى مؤشر الربط ولها الشكل الموضح في الشكل 12. يتم تحديد الإزاحة k بواسطة ترميز P وهي ثابتة فيما يتعلق بالعملية التي تستخدم P.

**الشكل 12:** عنونة بيانات الربط. (يُظهر كيف يُستخدم مؤشر الربط lp والإزاحة k لتكوين عنوان معمم لبيانات الربط)

#### استدعاء الإجراء والعودة

يجب أن يلبي الترميز المستخدم لنقل التحكم إلى إجراء فرعي والعودة اللاحقة للتحكم متطلبات عمومية البرمجة. على وجه الخصوص، لا يمكن وضع افتراضات بشأن الترميز التفصيلي لأي من الإجراءات المُستدعِية أو المُستدعاة بخلاف تلك الجوانب المُنشأة بشكل موحد بالاتفاقية. الاتفاقيات لأربعة جوانب من استدعاء الروتين الفرعي مألوفة نسبياً:

1. نقل الوسيطات

2. الترتيب لعودة التحكم

3. حفظ واستعادة حالة المعالج

4. تخصيص تخزين خاص للإجراء المُستدعى.

البند (4) ضروري في مَلتِكس بسبب متطلب الإجراء النقي، ومتطلب العمومية الذي يمنع الترتيب المسبق لاحتياجات التخزين للإجراء المُستدعى. يتم توفير هذا التخزين الخاص من خلال ربط **مقطع المكدس** بكل عملية حيث يتم حجز **إطار** من التخزين الخاص عند كل استدعاء إجراء. يتم تحرير الإطار عند عودة التحكم. يتم تنفيذ هذه الآلية بواسطة مؤشر المكدس (المُعيَّن **sp**) وهو العنوان المعمم لأصل إطار المكدس للإجراء قيد التشغيل. يجعل استخدام مقطع المكدس كل إجراء في مَلتِكس تكرارياً تلقائياً من خلال ربط إطارات مكدس منفصلة بإدخالات متتالية في نفس الإجراء. بسبب متطلب الإجراء النقي، فإن الوسيطات الثابتة فقط التي لا تعتمد على أرقام المقاطع قد تظهر في مقاطع الإجراءات. يجب وضع المؤشرات والوسيطات المتغيرة في مقطع المكدس، أو مقطع الربط، أو في مكان آخر. بحيث قد يكون لمصمم اللغة اختياره للتنفيذ، فإن مؤشر الوسيطة (المُعيَّن **ap**) عند دخول الإجراء هو العنوان المعمم لقائمة الوسيطات للإجراء المُستدعى.

بالإضافة إلى هذه المتطلبات التقليدية، تقدم طريقة الربط الديناميكي الموصوفة للتو مشكلة جديدة واحدة: عندما تنقل العملية α، في تنفيذ الإجراء P، التحكم إلى الإجراء Q، يجب تغيير قيمة مؤشر الربط إلى العنوان المعمم لقسم الربط للإجراء Q. نظراً لأن القيمة الجديدة لمؤشر الربط تحتوي على رقم مقطع، فهي بيانات خاصة للعملية α ولا يمكن وضعها في المقطع P أو Q.

تتطلب هذه المشكلة شكلاً معدلاً إلى حد ما من الربط بين المقاطع عن ذلك المستخدم لمراجع البيانات. نظراً لأنه من المرغوب أن يكون كود الآلة الضروري لتحميل مؤشر الربط لمقطع إجراء مرتبطاً بذلك المقطع، فقد تم اعتماد الحل التالي. لكل نقطة دخول خارجية داخل مقطع إجراء، يتم وضع تعليمتين إضافيتين في قسم الربط للإجراء في وقت التصريف. تقوم التعليمة الأولى بتحميل مؤشر الربط بالقيمة المناسبة عند دخول الإجراء، وتنقل التعليمة الثانية التحكم إلى نقطة الدخول في مقطع الإجراء المُستدعى. وبالتالي في إنشاء الرابط لاستدعاء إجراء خارجي، يشير العنوان غير المباشر المعمم الموضوع في بيانات الربط للإجراء المُستدعِي إلى زوج التعليمات المقابل في قسم الربط للإجراء المُستدعى. عندما ينتقل التحكم إلى مقطع الربط أثناء استدعاء إجراء خارجي، يتم الحصول بسهولة على جزء رقم المقطع من مؤشر الربط المطلوب من سجل قاعدة الإجراء، حيث أن العملية تنفذ الآن في مقطع الربط المطلوب.

يصور الشكل 13 آلية الربط المطلوبة لاستدعاء إجراء خارجي من الإجراء P إلى المقطع Q عند نقطة الدخول e. تشير الخطوط الصلبة إلى الخطوات الفردية المتخذة من خلال العناوين غير المباشرة بينما تشير الخطوط المتقطعة إلى تدفق التحكم الناتج.

**الشكل 13:** آلية الربط لدخول الإجراء. (يُظهر الإجراء P، وأقسام الربط، والإجراء Q مع أسهم تشير إلى تدفق التحكم)

في تنفيذ استدعاء إجراء خارجي، يتم حفظ ظروف آلة المُستدعِي، بما في ذلك سجل قاعدة الإجراء وعداد البرنامج، في مقطع المكدس بواسطة المُستدعِي. يمكن بالتالي تنفيذ العودة من الإجراء المُستدعى ببساطة عن طريق استعادة ظروف آلة المُستدعِي من مقطع المكدس.

---

### Translation Notes

- **Figures referenced:** Figures 9, 10, 11, 12, 13
- **Key terms introduced:**
  - Dynamic linking (الربط الديناميكي)
  - Pure procedure (إجراء نقي)
  - Path name (اسم المسار)
  - Segment reference name (اسم مرجع المقطع)
  - Link data (بيانات الربط)
  - Linkage section (قسم الربط)
  - Symbol table (جدول الرموز)
  - Linkage pointer (مؤشر الربط)
  - Stack segment (مقطع المكدس)
  - Stack frame (إطار المكدس)
  - Argument pointer (مؤشر الوسيطة)
  - External entry point (نقطة دخول خارجية)
- **Equations:** None
- **Citations:** Reference [2]
- **Special handling:**
  - Three numbered requirements for intersegment addressing
  - Four numbered aspects of subroutine calling conventions
  - Complex explanation of dynamic linking mechanism
  - Assembly language example: `OPR <D>|[x]`

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.84
- Glossary consistency: 0.86
- **Overall section score:** 0.86

### Back-Translation Check

The ability of many users to share access to procedure and data information, and the power to construct complex procedures by building on the work of others are two fundamental desires of multi-process computer systems. The potential value of these features for the advancement of computer applications should not be underestimated. The design of a system around the idea of a generalized, location-independent address is a fundamental element in achieving these goals.

Link data is private data of its process because whether P is linked to D|x for process α is entirely independent of whether the same is true for any other process. Therefore, whenever a procedure segment becomes known to a process, a copy of the procedure's linkage section is made as a segment within that process.

The linkage pointer is a generalized address that resides in a dedicated base register (designated lp). As shown in Figure 12, it is the origin L#α|s of the portion of a linkage segment that contains the links for intersegment references made from the segment being executed.

**Validation:** ✓ Back-translation accurately preserves the complex concepts of dynamic linking, linkage sections, and the mechanism for procedure calls.
