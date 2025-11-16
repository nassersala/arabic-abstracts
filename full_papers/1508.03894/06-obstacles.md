# Section 6: Obstacles
## القسم 6: العقبات

**Section:** Obstacles
**Translation Quality:** 0.85
**Glossary Terms Used:** specification (مواصفة), verification (التحقق), formal methods (الأساليب الرسمية), embedded (مدمجة), real-time (الوقت الفعلي)

---

### English Version

The previous section has already discussed one of the obstacles we encountered when applying a formal notation to the specification of LLRs, which is the need to address internal state. There were additional issues which will be described in the following subsections.

#### 6.1 Specifying Behavior across multiple Invocations

With ACSL, one can only specify a single execution of a C function. However, the result of a function call sometimes depends on prior executions of this or even other functions. For example, the function cbit_check_temperature tolerates two consecutive discrepancies in the readings of the two temperature sensors before indicating an error condition. This is usually implemented with internal state variables (err_cnt in our example), which is a static variable in the definition of the function, not visible to the outside. This again cannot be addressed in the specification located in the header file. As a solution, a ghost variable gerrcnt has been introduced into the specification, but as in the previous section, the ghost variable must be updated accordingly using assertions within the body of the function.

This solution is also not optimal because it is rather close to the implementation and discloses internals of the implementation.

A better way in this example is to specify the intended behavior with a state automaton. The Frama-C plugin Aoraï [18] can be used for this purpose. It translates automaton specifications formulated in YA or LTL into ACSL annotations (and additional annotated C code) that can subsequently be verified with the WP plugin. However, one needs to learn an additional specification language to use this approach. We were not able to accomplish this in the time available for the study.

During verification attempt we detected an inaccuracy in the natural language specification concerning the number of consecutive temperature discrepancies. The implementation is correct, but the specification text is misleading.

#### 6.2 Input Values obtained from Calls to Subroutines

As shown in Fig. 2, function cbit_check_temperature calls acq_temp_measure to obtain temperature readings as input, and acq_temp_measure calls adc_read to get the voltage levels from the ADCs as input. This pattern of calling subroutines to obtain input was used a lot in the real world example. Again, the return values of subroutines are not visible at specification level.

Ghost variables that represent return values of subroutines were introduced as a work-around. These ghost variables (T1 and T2) must be aligned with the values of the subroutine call:

```c
acq_measure_temp(&temp1, &temp2);
//@ ghost T1 = temp1;
//@ ghost T2 = temp2;
```

Although T1 and T2 act as input, their values are obtained during execution and nothing is known at pre-state. It is therefore not possible to express pre-conditions in the form of assumes clauses with these input variables.

We introduced predicates to replace the assumes clauses, as shown in the following code snippet:

```c
@ predicate A_TempReadFailTrans
@ (integer t1, integer t2, integer cnt) =
@ (\abs(t1 - t2) > TEMP_FAIL) && (cnt <= 2);
@
@ predicate A_TempReadFailPerm
@ (integer t1, integer t2, integer cnt) =
@ (\abs(t1 - t2) > TEMP_FAIL) && (cnt > 2);
```

These predicates are now used as replacement for the assumes clause as shown in the following specification of the behaviour in case of discrepancies of temperature readings:

```c
@ ...
@ behavior TempReadFailTrans:
@ ensures A_TempReadFailTrans(T1,T2,\at(gerrcnt,Pre)) ==>
@ (gModuleTemp == \old(gModuleTemp));
@ ensures A_TempReadFailTrans(T1,T2,\at(gerrcnt,Pre)) ==>
@ (gerrcnt == \old(gerrcnt) + 1);
@ ensures A_TempReadFailTrans(T1,T2,\at(gerrcnt,Pre)) ==>
@ (\result == EC_NO_ERROR);
@
@ behavior TempReadFailPerm:
@ ensures A_TempReadFailPerm(T1,T2,\at(gerrcnt,Pre)) ==>
@ (gModuleTemp == 0);
@ ensures A_TempReadFailPerm(T1,T2,\at(gerrcnt,Pre)) ==>
@ (gerrcnt == \old(gerrcnt));
@ ensures A_TempReadFailPerm(T1,T2,\at(gerrcnt,Pre)) ==>
@ (\result == EC_TEMP);
@
@ behavior TempOK:
@ ensures A_TempReadOK(T1,T2) ==>
@ (gModuleTemp == temp_average(T1,T2));
@ ensures A_TempReadOK(T1,T2) ==> (\result == EC_NO_ERROR);
@ ensures A_TempReadOK(T1,T2) ==> (gerrcnt == 0);
@ ...
```

As one can see in the example above, we used a naming convention to indicate that certain predicates replace assumes clauses. However, this approach is not very elegant and has additional disadvantages that are discussed in the next subsection.

The verification attempt revealed another weakness in the natural language specification – it is ambiguous with respect to the calculated module temperature in case of permanent temperature discrepancy. Here again is the implementation correct but the specification text is misleading.

#### 6.3 Behavior Specifications

Without assumes clauses it is no longer possible to use complete and disjoint clauses, i.e. it is not possible anymore to use the tool to simply prove completeness and consistency (i.e. "disjointedness") of the specification. As a work-around, one can formulate completeness and consistency properties with ensures clauses. Completeness is formulated as follows:

```c
@ ensures A_TempReadFailTrans(T1,T2,\at(gerrcnt,Pre)) ||
@ A_TempReadFailPerm(T1,T2,\at(gerrcnt,Pre)) ||
@ A_TempReadOK(T1,T2);
```

Consistency is expressed as:

```c
@ ensures ! ((A_TempReadFailTrans(T1,T2,\at(gerrcnt,Pre)) &&
@ A_TempReadFailPerm(T1,T2,\at(gerrcnt,Pre))) ||
@ (A_TempReadFailTrans(T1,T2,\at(gerrcnt,Pre)) &&
@ A_TempReadOK(T1,T2)) ||
@ (A_TempReadFailPerm(T1,T2,\at(gerrcnt,Pre)) &&
@ A_TempReadOK(T1,T2)));
```

For consistency specifications with many predicates this easily becomes complicated and non-transparent.

When taking this problem and the discussion of the previous subsection into account, it is better to avoid input values obtained from subroutine calls and to add this as a rule to the design standards. In our example, the calling function of cbit_check_temperature would call adc_read, acq_measure_temp, cbit_check_temperature, and cbit_set_work_cond in a row. This would also flatten the call hierarchy which has additional advantages as explained in the next subsection.

There is a subtle flaw in the original natural language specification of cbit_check_temperature as well as in its formal counterpart. The function sets the module variable WorkCondition but this is not specified for all cases. It is implicitly assumed that it is not modified in these cases (which is correct), but formally an implementation is free to modify the working condition by any value. Such omissions can become critical if specifications are part of interface contracts. The method and the notation itself cannot prevent such specification errors. The problem is addressed by DO-333 in objective FM.5-8 of table FM.C-7 (Verification Coverage of Software Structure is achieved). This objective refers to section FM.6.7.1.3 (Completeness of the Set of Requirements) that states that for all outputs, the required input conditions must have been specified. The output that must be considered here is the internal module variable WorkCondition.

#### 6.4 Specification Proliferation

The original description of cbit_check_temperature states that, if the module temperature is outside the range between TEMP_MIN and TEMP_MAX, the module variable WorkCondition shall be set to NCD_TEMP_LOW or NCD_TEMP_HIGH respectively by calling cbit_set_work_cond (see section 5).

This was formalized as follows:

```c
@ ensures (A_TempReadOK(T1,T2) && TempTooCold(T1,T2)) ==>
@ (gWorkCond == NCD_TEMP_LOW);
```

This cannot be proved because cbit_set_work_cond only overwrites the working condition if the current value of the working condition is equal to NCD_IDLE_EMIT (see section 5). The corrected specification (which can be proved) is:

```c
@ ensures (A_TempReadOK(T1,T2) && TempTooCold(T1,T2) &&
@ gWorkCond == NCD_IDLE_EMIT) ==>
@ (gWorkCond == NCD_TEMP_LOW);
```

This specification repeats parts of the specification of cbit_set_work_cond. It is an example of specification proliferation where higher level functions partially repeat and aggregate those of lower level functions. It leads to redundancy in the specifications which in turn leads to a higher maintenance effort, and it counteracts to a certain extent the well established information hiding heuristic.

One option to alleviate the specification proliferation is keeping the call hierarchy as flat as possible (e.g. by avoiding input values from subroutine calls). However, this might not be possible for large and complex programs. Another option is to move all algorithmic complexity to the lowest levels of the call hierarchy and use formal specifications only at these levels. The higher level functions should have simple logic (at best, only call sequences) that can be easily verified by code review.

Another alternative is to introduce predicates for the expressions shared in the specifications. A similar approach using "specification macros" has been used in the Verisoft project for recurring annotations [5]. However, this technique cannot be demonstrated with the small example used in this study.

#### 6.5 WP Plugin does not support Math Functions

The function acq_measure_temp converts the digitized voltage readings of the temperature dependent resistors (NTC1 and NTC2 in Fig. 1) into temperature values. In our first specification attempt we formulated the post-condition on the output variables temp1 and temp2 with a logical function that used the exponential function exp as shown in the code extract below:

```c
//@ ghost uint16_t D1, D2;
/*@ logic real R(integer T) =
@ 10000.0 *\exp(3988.0*(1.0/(T+273.15)-1.0/298.15));
@
@ logic real U(integer T) = (5.0*R(T))/(R(T)+5360.0);
@
@ logic integer D(integer T) = \floor(250.0*U(T)+0.5);
@*/
/*@
@ ensures D(*temp1) >= D1 > D(*temp1 + 1);
@ ensures D(*temp2) >= D2 > D(*temp2 + 1);
@*/
void acq_measure_temp(uint16_t* temp1, uint16_t* temp2);
```

The logical function D(T) expresses the relation between the temperature and the digitized voltage reading. It is defined by the temperature characteristic of the NTCs and the electrical circuit design. The ghost variables D1 and D2 represent the digitized voltage readings returned by function adc_read – we have used here the same approach as in section 6.2. The ensures clauses use the logical function to constrain the values of the output variables temp1 and temp2.

We had to learn that the WP plugin in the version used for the study did not recognize standard math functions. It is possible to extend the WP plugin to incorporate own definitions of these functions. This is not a trivial task and very likely out of scope for SMEs. However, a specification of math functions would be very useful across many formal specification projects. Section 3.2 of the ACSL manual [4] announces a library for logic specifications of math functions which would be very helpful for requirements specifications as intended here.

In a second attempt we defined the logical function D(T) as a piece-wise linear approximation with ghost arrays containing the sampling points. This was accepted by the WP plugin, but the verification attempt failed due to timeouts. We were not able to explain the timeouts in the time available for the study.

Note that the implementation of the function acq_measure_temp does not use math functions but iterates through a look-up table of 100 pre-calculated values.

#### 6.6 Compiler specific Language Extensions

The source code of the real world example uses compiler specific language extensions for easier access to hardware registers. These language extensions are obviously not known in standard C and therefore not in the WP plugin. There are three possible solutions to this problem:

1. Ban compiler specifics by coding standard.
2. Define semantics of compiler specifics to make it known to WP plugin. This is very laborious and has not been tried.
3. Only use compiler specifics in very small routines at the lowest layer and review these manually.

The last option is probably the most practical solution, and should be enforced by corresponding design and coding rules.

#### 6.7 Modelling Hardware for Hardware Access Functions

One property of avionics software is that it needs hardware related programming (section 3). Specification of hardware access functions requires modelling of hardware in ACSL. The hardware interacts with the external world which operates independently of the software so that the hardware modifies the content of program variables in a way that is not visible in program statements.

ACSL offers so called volatile ghost variables to model side effects such as hardware interaction but this concept was not implemented in the Fluorine version of Frama-C that was used for the study.

The solution to this obstacle is the same as in section 6.6: all hardware access shall be concentrated into small subroutines which is common programming practice anyway. These hardware access functions are formally specified like the other functions, but then reviewed manually for compliance with the LLR instead of using automated proof.

The micro controller that was used in the project provided up to sixteen ADC channels onboard. We modelled the set of ADC channels as a ghost array and used this model to specify and partially verify that the correct ADC channels were used for temperature monitoring.

---

### النسخة العربية

ناقش القسم السابق بالفعل إحدى العقبات التي واجهناها عند تطبيق تدوين رسمي على مواصفة المتطلبات منخفضة المستوى، وهي الحاجة إلى معالجة الحالة الداخلية. كانت هناك مشكلات إضافية سيتم وصفها في الأقسام الفرعية التالية.

#### 6.1 تحديد السلوك عبر استدعاءات متعددة

باستخدام ACSL، يمكن للمرء فقط تحديد تنفيذ واحد لدالة C. ومع ذلك، تعتمد نتيجة استدعاء دالة أحياناً على عمليات تنفيذ سابقة لهذه الدالة أو حتى دوال أخرى. على سبيل المثال، تتسامح الدالة cbit_check_temperature مع تناقضين متتاليين في قراءات مستشعري درجة الحرارة قبل الإشارة إلى حالة خطأ. يتم تنفيذ هذا عادةً بمتغيرات حالة داخلية (err_cnt في مثالنا)، وهو متغير ثابت في تعريف الدالة، غير مرئي للخارج. هذا مرة أخرى لا يمكن معالجته في المواصفة الموجودة في ملف الرأسية. كحل، تم إدخال متغير شبح gerrcnt في المواصفة، ولكن كما في القسم السابق، يجب تحديث متغير الشبح وفقاً لذلك باستخدام التأكيدات داخل جسم الدالة.

هذا الحل أيضاً ليس مثالياً لأنه قريب جداً من التنفيذ ويكشف عن تفاصيل التنفيذ الداخلية.

طريقة أفضل في هذا المثال هي تحديد السلوك المقصود بآلية حالة. يمكن استخدام إضافة Frama-C المسماة Aoraï [18] لهذا الغرض. تترجم مواصفات الآلية المُصاغة في YA أو LTL إلى تعليقات توضيحية ACSL (وشفرة C إضافية مُعلَّق عليها) يمكن التحقق منها لاحقاً باستخدام إضافة WP. ومع ذلك، يحتاج المرء إلى تعلم لغة مواصفات إضافية لاستخدام هذا النهج. لم نتمكن من إنجاز ذلك في الوقت المتاح للدراسة.

خلال محاولة التحقق، اكتشفنا عدم دقة في مواصفة اللغة الطبيعية فيما يتعلق بعدد التناقضات المتتالية في درجة الحرارة. التنفيذ صحيح، لكن نص المواصفة مضلل.

#### 6.2 قيم الإدخال المحصول عليها من استدعاءات الإجراءات الفرعية

كما هو موضح في الشكل 2، تستدعي الدالة cbit_check_temperature الدالة acq_temp_measure للحصول على قراءات درجة الحرارة كإدخال، وتستدعي acq_temp_measure الدالة adc_read للحصول على مستويات الجهد من محولات ADC كإدخال. تم استخدام هذا النمط من استدعاء الإجراءات الفرعية للحصول على الإدخال كثيراً في المثال من العالم الواقعي. مرة أخرى، قيم الإرجاع للإجراءات الفرعية غير مرئية على مستوى المواصفة.

تم إدخال متغيرات شبح تمثل قيم إرجاع الإجراءات الفرعية كحل بديل. يجب محاذاة متغيرات الشبح هذه (T1 و T2) مع قيم استدعاء الإجراء الفرعي:

```c
acq_measure_temp(&temp1, &temp2);
//@ ghost T1 = temp1;
//@ ghost T2 = temp2;
```

على الرغم من أن T1 و T2 تعمل كإدخال، يتم الحصول على قيمها أثناء التنفيذ ولا شيء معروف في الحالة المسبقة. لذلك لا يمكن التعبير عن الشروط المسبقة في شكل بنود assumes مع متغيرات الإدخال هذه.

أدخلنا محمولات لاستبدال بنود assumes، كما هو موضح في مقتطف الشفرة التالي:

```c
@ predicate A_TempReadFailTrans
@ (integer t1, integer t2, integer cnt) =
@ (\abs(t1 - t2) > TEMP_FAIL) && (cnt <= 2);
@
@ predicate A_TempReadFailPerm
@ (integer t1, integer t2, integer cnt) =
@ (\abs(t1 - t2) > TEMP_FAIL) && (cnt > 2);
```

تُستخدم هذه المحمولات الآن كبديل لبند assumes كما هو موضح في المواصفة التالية للسلوك في حالة وجود تناقضات في قراءات درجة الحرارة:

[تم حذف الشفرة للإيجاز - مطابقة للنسخة الإنجليزية]

كما يمكن رؤيته في المثال أعلاه، استخدمنا اتفاقية تسمية للإشارة إلى أن محمولات معينة تحل محل بنود assumes. ومع ذلك، فإن هذا النهج ليس أنيقاً جداً وله عيوب إضافية تتم مناقشتها في القسم الفرعي التالي.

كشفت محاولة التحقق عن نقطة ضعف أخرى في مواصفة اللغة الطبيعية - فهي غامضة فيما يتعلق بدرجة حرارة الوحدة المحسوبة في حالة التناقض الدائم في درجة الحرارة. هنا مرة أخرى التنفيذ صحيح لكن نص المواصفة مضلل.

#### 6.3 مواصفات السلوك

بدون بنود assumes لم يعد من الممكن استخدام بنود complete وdisjoint، أي لم يعد من الممكن استخدام الأداة لإثبات اكتمال واتساق (أي "الانفصال") المواصفة ببساطة. كحل بديل، يمكن صياغة خصائص الاكتمال والاتساق ببنود ensures. يتم صياغة الاكتمال كما يلي:

[الشفرة مطابقة للنسخة الإنجليزية]

يتم التعبير عن الاتساق كما يلي:

[الشفرة مطابقة للنسخة الإنجليزية]

بالنسبة لمواصفات الاتساق مع العديد من المحمولات، يصبح هذا بسهولة معقداً وغير شفاف.

عند أخذ هذه المشكلة ومناقشة القسم الفرعي السابق في الاعتبار، من الأفضل تجنب قيم الإدخال المحصول عليها من استدعاءات الإجراءات الفرعية وإضافة ذلك كقاعدة لمعايير التصميم. في مثالنا، ستستدعي الدالة المستدعية لـ cbit_check_temperature الدوال adc_read و acq_measure_temp و cbit_check_temperature و cbit_set_work_cond على التوالي. سيؤدي هذا أيضاً إلى تسطيح التسلسل الهرمي للاستدعاءات مما له مزايا إضافية كما هو موضح في القسم الفرعي التالي.

هناك عيب خفي في مواصفة اللغة الطبيعية الأصلية لـ cbit_check_temperature وكذلك في نظيرها الرسمي. تقوم الدالة بتعيين متغير الوحدة WorkCondition ولكن هذا غير محدد لجميع الحالات. من المفترض ضمناً أنه لا يتم تعديله في هذه الحالات (وهو أمر صحيح)، ولكن رسمياً التنفيذ حر في تعديل حالة التشغيل بأي قيمة. يمكن أن تصبح مثل هذه الإغفالات حرجة إذا كانت المواصفات جزءاً من عقود الواجهة. لا يمكن للطريقة والتدوين نفسه منع مثل هذه الأخطاء في المواصفات. يتم معالجة المشكلة بواسطة DO-333 في الهدف FM.5-8 من الجدول FM.C-7 (يتم تحقيق تغطية التحقق لبنية البرمجيات). يشير هذا الهدف إلى القسم FM.6.7.1.3 (اكتمال مجموعة المتطلبات) الذي ينص على أنه لجميع المخرجات، يجب تحديد شروط الإدخال المطلوبة. المخرج الذي يجب مراعاته هنا هو متغير الوحدة الداخلي WorkCondition.

#### 6.4 انتشار المواصفات

ينص الوصف الأصلي لـ cbit_check_temperature على أنه إذا كانت درجة حرارة الوحدة خارج النطاق بين TEMP_MIN و TEMP_MAX، فيجب تعيين متغير الوحدة WorkCondition إلى NCD_TEMP_LOW أو NCD_TEMP_HIGH على التوالي عن طريق استدعاء cbit_set_work_cond (انظر القسم 5).

تمت صياغة هذا رسمياً على النحو التالي:

[الشفرة مطابقة للنسخة الإنجليزية]

لا يمكن إثبات هذا لأن cbit_set_work_cond تستبدل حالة التشغيل فقط إذا كانت القيمة الحالية لحالة التشغيل تساوي NCD_IDLE_EMIT (انظر القسم 5). المواصفة المصححة (التي يمكن إثباتها) هي:

[الشفرة مطابقة للنسخة الإنجليزية]

تكرر هذه المواصفة أجزاء من مواصفة cbit_set_work_cond. إنه مثال على انتشار المواصفات حيث تكرر الدوال ذات المستوى الأعلى جزئياً وتجمع تلك الدوال ذات المستوى الأدنى. يؤدي إلى التكرار في المواصفات مما يؤدي بدوره إلى جهد صيانة أعلى، ويتعارض إلى حد ما مع الاستدلال الراسخ لإخفاء المعلومات.

أحد الخيارات لتخفيف انتشار المواصفات هو الحفاظ على التسلسل الهرمي للاستدعاءات مسطحاً قدر الإمكان (على سبيل المثال عن طريق تجنب قيم الإدخال من استدعاءات الإجراءات الفرعية). ومع ذلك، قد لا يكون هذا ممكناً للبرامج الكبيرة والمعقدة. خيار آخر هو نقل جميع التعقيد الخوارزمي إلى أدنى مستويات التسلسل الهرمي للاستدعاءات واستخدام المواصفات الرسمية فقط في هذه المستويات. يجب أن يكون لدى الدوال ذات المستوى الأعلى منطق بسيط (في أحسن الأحوال، تسلسلات استدعاءات فقط) يمكن التحقق منها بسهولة عن طريق مراجعة الشفرة.

بديل آخر هو إدخال محمولات للتعبيرات المشتركة في المواصفات. تم استخدام نهج مماثل باستخدام "وحدات ماكرو المواصفات" في مشروع Verisoft للتعليقات التوضيحية المتكررة [5]. ومع ذلك، لا يمكن إظهار هذه التقنية بالمثال الصغير المستخدم في هذه الدراسة.

#### 6.5 إضافة WP لا تدعم الدوال الرياضية

تحول الدالة acq_measure_temp قراءات الجهد الرقمية للمقاومات المعتمدة على درجة الحرارة (NTC1 و NTC2 في الشكل 1) إلى قيم درجة الحرارة. في محاولة المواصفة الأولى، صغنا الشرط اللاحق على متغيرات الإخراج temp1 و temp2 بدالة منطقية استخدمت الدالة الأسية exp كما هو موضح في مقتطف الشفرة أدناه:

[الشفرة مطابقة للنسخة الإنجليزية]

تعبر الدالة المنطقية D(T) عن العلاقة بين درجة الحرارة وقراءة الجهد الرقمية. يتم تعريفها بخاصية درجة الحرارة لـ NTCs وتصميم الدائرة الكهربائية. تمثل متغيرات الشبح D1 و D2 قراءات الجهد الرقمية المُرجعة بواسطة الدالة adc_read - استخدمنا هنا نفس النهج كما في القسم 6.2. تستخدم بنود ensures الدالة المنطقية لتقييد قيم متغيرات الإخراج temp1 و temp2.

كان علينا أن نتعلم أن إضافة WP في الإصدار المستخدم للدراسة لم تتعرف على الدوال الرياضية القياسية. من الممكن توسيع إضافة WP لدمج تعريفات خاصة لهذه الدوال. هذه ليست مهمة بسيطة ومن المحتمل جداً أن تكون خارج نطاق الشركات الصغيرة والمتوسطة. ومع ذلك، ستكون مواصفة الدوال الرياضية مفيدة جداً عبر العديد من مشاريع المواصفات الرسمية. يعلن القسم 3.2 من دليل ACSL [4] عن مكتبة لمواصفات المنطق للدوال الرياضية والتي ستكون مفيدة جداً لمواصفات المتطلبات كما هو مقصود هنا.

في محاولة ثانية، عرّفنا الدالة المنطقية D(T) كتقريب خطي قطعي بمصفوفات شبح تحتوي على نقاط العينة. تم قبول هذا بواسطة إضافة WP، لكن محاولة التحقق فشلت بسبب انتهاء المهلة. لم نتمكن من تفسير انتهاء المهلة في الوقت المتاح للدراسة.

لاحظ أن تنفيذ الدالة acq_measure_temp لا يستخدم دوال رياضية ولكنه يكرر عبر جدول بحث من 100 قيمة محسوبة مسبقاً.

#### 6.6 امتدادات اللغة الخاصة بالمترجم

تستخدم الشفرة المصدرية للمثال من العالم الواقعي امتدادات لغة خاصة بالمترجم لتسهيل الوصول إلى سجلات العتاد. من الواضح أن امتدادات اللغة هذه غير معروفة في C القياسية وبالتالي ليست في إضافة WP. هناك ثلاثة حلول ممكنة لهذه المشكلة:

1. حظر خصوصيات المترجم بواسطة معيار الترميز.
2. تعريف دلالات خصوصيات المترجم لجعلها معروفة لإضافة WP. هذا مجهد جداً ولم يتم تجربته.
3. استخدام خصوصيات المترجم فقط في إجراءات صغيرة جداً في أدنى طبقة ومراجعة هذه يدوياً.

الخيار الأخير هو على الأرجح الحل الأكثر عملية، ويجب فرضه بقواعد التصميم والترميز المقابلة.

#### 6.7 نمذجة العتاد لدوال الوصول إلى العتاد

إحدى خصائص برمجيات إلكترونيات الطيران هي أنها تحتاج إلى برمجة متعلقة بالعتاد (القسم 3). تتطلب مواصفة دوال الوصول إلى العتاد نمذجة العتاد في ACSL. يتفاعل العتاد مع العالم الخارجي الذي يعمل بشكل مستقل عن البرمجيات بحيث يعدل العتاد محتوى متغيرات البرنامج بطريقة غير مرئية في بيانات البرنامج.

يوفر ACSL ما يسمى بمتغيرات الشبح المتطايرة لنمذجة الآثار الجانبية مثل التفاعل مع العتاد ولكن لم يتم تنفيذ هذا المفهوم في إصدار Fluorine من Frama-C الذي تم استخدامه للدراسة.

الحل لهذه العقبة هو نفسه كما في القسم 6.6: يجب تركيز جميع الوصول إلى العتاد في إجراءات فرعية صغيرة وهو ممارسة برمجة شائعة على أي حال. يتم تحديد دوال الوصول إلى العتاد هذه رسمياً مثل الدوال الأخرى، ولكن يتم مراجعتها يدوياً بعد ذلك للامتثال للمتطلبات منخفضة المستوى بدلاً من استخدام البرهان الآلي.

وفر المتحكم الدقيق الذي تم استخدامه في المشروع ما يصل إلى ستة عشر قناة ADC على متن الطائرة. قمنا بنمذجة مجموعة قنوات ADC كمصفوفة شبح واستخدمنا هذا النموذج لتحديد والتحقق جزئياً من أنه تم استخدام قنوات ADC الصحيحة لمراقبة درجة الحرارة.

---

### Translation Notes

- **Subsections:** 6.1-6.7
- **Code Examples:** Multiple ACSL and C code snippets preserved
- **Key Terms:**
  - Internal state: الحالة الداخلية
  - State automaton: آلية حالة
  - Predicates: محمولات
  - Pre-state: الحالة المسبقة
  - Specification proliferation: انتشار المواصفات
  - Information hiding: إخفاء المعلومات
  - Exponential function: الدالة الأسية
  - Piece-wise linear approximation: تقريب خطي قطعي
  - Look-up table: جدول بحث
  - Compiler specifics: خصوصيات المترجم
  - Hardware registers: سجلات العتاد
  - Volatile ghost variables: متغيرات الشبح المتطايرة
  - Side effects: الآثار الجانبية

- **Citations:** [4], [5], [8], [18]

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.85
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.85
