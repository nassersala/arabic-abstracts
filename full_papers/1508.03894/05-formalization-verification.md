# Section 5: Formalization and Verification of LLR
## القسم 5: الصياغة الرسمية والتحقق من المتطلبات منخفضة المستوى

**Section:** Formalization and Verification of LLR
**Translation Quality:** 0.86
**Glossary Terms Used:** formalization (الصياغة الرسمية), verification (التحقق), specification (مواصفة), proof (برهان), requirements (متطلبات)

---

### English Version

The analysis approach is the same for all functions: at first, the original specification of the C function is formalized using ACSL behavior specifications. In a subsequent step, verification of the source code is attempted to show by proof that the implementation follows the specification. This is actually an iterative approach which often needs adding instrumentation (assertions, loop invariants) to the source code.

To illustrate the approach, we use the most simple function cbit_set_work_cond that simply writes to a module variable, i.e. a persistent variable only known within the module cbit. This variable is used in other parts of the program but is read and write protected by setter and getter functions.

The update of the state variable is guarded – the function takes a new value of the working condition as a parameter new_cond and writes that to the module variable WorkCondition unless this module variable has been set previously. The only exception is the special parameter value NCD_NO_COMMAND that can overwrite all settings. A natural language formulation of the low level requirements would read as follows:

1. If the value of the input parameter new_cond is equal to NCD_NO_COMMAND, then the module variable WorkCondition is set to this value NCD_NO_COMMAND.

2. If the current content of the module variable WorkCondition is equal to NCD_IDLE_EMIT, the module variable WorkCondition is set to the value of the input parameter new_cond.

3. If the value of the module variable WorkCondition is not equal to NCD_IDLE_EMIT and the value of the input parameter new_cond is not equal to NCD_NO_COMMAND, then the current value of WorkCondition is not changed.

The attempt to formalize these LLR into ACSL encounters the first obstacle: the internal module variable – a static variable of file scope – is not visible in the header file where the formalized specification is located. The solution was to introduce a ghost variable that represents the internal data, which in effect is uncovering the internal variable, i.e. turning parts of the module inside out. The ghost variable for the internal state is located in the header file:

```c
//@ ghost uint16_t gWorkCond = NCD_IDLE_EMIT ;
```

The behavioral specification, i.e. the translation of the LLR above, is now straight forward:

```c
/*@
@ behavior NoCommand:
@ assumes new_cond == NCD_NO_COMMAND ;
@ ensures gWorkCond == new_cond;
@ behavior ModifyWC:
@ assumes gWorkCond == NCD_IDLE_EMIT ;
@ assumes new_cond != NCD_NO_COMMAND ;
@ ensures gWorkCond == new_cond;
@ behavior KeepWC:
@ assumes (( gWorkCond != NCD_IDLE_EMIT ) &&
@ (new_cond != NCD_NO_COMMAND ));
@ ensures gWorkCond == \old( gWorkCond );
@ complete behaviors ;
@ disjoint behaviors ;
@*/
void cbit_set_work_cond ( uint16_t new_cond);
```

The three behavior specifications above directly correspond to the natural language requirements so that they could be replaced by the formalized requirements. The behavior clause can be named as shown in the example which facilitates traceability to higher level requirements, an objective that is strongly emphasized in aviation standards. The assumes clauses represent the conditional part of the natural language requirements and are evaluated at the beginning of the execution of the function. Moreover, with complete and disjoint clauses one can automatically verify completeness and consistency of the formal specification.

Note that assigns clauses have been omitted from the specification above although this is discouraged by the ACSL reference manual ([4], section 2.3.5). However, adding assigns clauses generates verification conditions that cannot be proved. This is due to the fact that the function modifies a state variable of file scope (WorkCondition) which cannot be listed in the assigns clause because it is not visible there. Several solutions for this problem are under discussion on the tool's mailing list at this time of writing.

For the verification, the ghost state variable must be aligned with the internal module variable using assertions, as shown below:

```c
void cbit_set_work_cond ( uint16_t new_cond )
{
//@ assert gWorkCond == WorkCondition ;
if (( WorkCondition == NCD_IDLE_EMIT ) || ( new_cond == NCD_NO_COMMAND) )
{
WorkCondition = new_cond ;
//@ ghost gWorkCond = WorkCondition ;
}
}
```

The assertion in line 3 is necessary to inform the prover that the internal state is always equal to the ghost state. It is not possible to prove it.

The WP plugin generates a verification condition for every assertion. The verification conditions are similar to test cases in traditional verification so that a verification condition that cannot be proved is identical to a test case that has failed. Therefore, justification is needed for the assertion in line 3 to fulfill objective FM2 of table FM.C-7 of DO-333 that demands that formal analysis results are correct and discrepancies are explained.

Representing internal state with a ghost variable is not optimal as indicated above. The function cbit_set_work_cond and its counterpart cbit_get_work_cond would have been better specified by using algebraic specification techniques in the way it is shown in [8] for the stack example. The approach described there transforms the axioms into additional, ACSL annotated C code. This essentially means that C code is used as low level requirements which is not acceptable. The inclusion of algebraic specification techniques into ACSL would probably be the most elegant solution for this problem.

---

### النسخة العربية

نهج التحليل هو نفسه لجميع الدوال: في البداية، يتم صياغة المواصفة الأصلية لدالة C رسمياً باستخدام مواصفات السلوك في ACSL. في خطوة لاحقة، يتم محاولة التحقق من الشفرة المصدرية لإظهار بالبرهان أن التنفيذ يتبع المواصفة. هذا في الواقع نهج تكراري غالباً ما يحتاج إلى إضافة أدوات قياس (تأكيدات، ثوابت الحلقات) إلى الشفرة المصدرية.

لتوضيح النهج، نستخدم الدالة الأبسط cbit_set_work_cond التي تكتب ببساطة إلى متغير وحدة، أي متغير ثابت معروف فقط داخل الوحدة cbit. يُستخدم هذا المتغير في أجزاء أخرى من البرنامج ولكنه محمي للقراءة والكتابة بواسطة دوال تعيين وجلب.

تحديث متغير الحالة محمي - تأخذ الدالة قيمة جديدة لحالة التشغيل كمعامل new_cond وتكتبها إلى متغير الوحدة WorkCondition ما لم يكن متغير الوحدة هذا قد تم تعيينه مسبقاً. الاستثناء الوحيد هو قيمة المعامل الخاصة NCD_NO_COMMAND التي يمكنها الكتابة فوق جميع الإعدادات. صياغة اللغة الطبيعية للمتطلبات منخفضة المستوى ستكون كما يلي:

1. إذا كانت قيمة معامل الإدخال new_cond تساوي NCD_NO_COMMAND، فإن متغير الوحدة WorkCondition يتم تعيينه لهذه القيمة NCD_NO_COMMAND.

2. إذا كان المحتوى الحالي لمتغير الوحدة WorkCondition يساوي NCD_IDLE_EMIT، فإن متغير الوحدة WorkCondition يتم تعيينه لقيمة معامل الإدخال new_cond.

3. إذا لم تكن قيمة متغير الوحدة WorkCondition تساوي NCD_IDLE_EMIT وقيمة معامل الإدخال new_cond لا تساوي NCD_NO_COMMAND، فإن القيمة الحالية لـ WorkCondition لا تتغير.

محاولة صياغة هذه المتطلبات منخفضة المستوى رسمياً في ACSL تواجه العقبة الأولى: متغير الوحدة الداخلي - وهو متغير ثابت ذو نطاق ملف - غير مرئي في ملف الرأسية حيث توجد المواصفة المُصاغة رسمياً. كان الحل هو إدخال متغير شبح يمثل البيانات الداخلية، والذي في الواقع يكشف عن المتغير الداخلي، أي قلب أجزاء من الوحدة من الداخل إلى الخارج. يقع المتغير الشبح للحالة الداخلية في ملف الرأسية:

```c
//@ ghost uint16_t gWorkCond = NCD_IDLE_EMIT ;
```

مواصفة السلوك، أي ترجمة المتطلبات منخفضة المستوى أعلاه، مباشرة الآن:

```c
/*@
@ behavior NoCommand:
@ assumes new_cond == NCD_NO_COMMAND ;
@ ensures gWorkCond == new_cond;
@ behavior ModifyWC:
@ assumes gWorkCond == NCD_IDLE_EMIT ;
@ assumes new_cond != NCD_NO_COMMAND ;
@ ensures gWorkCond == new_cond;
@ behavior KeepWC:
@ assumes (( gWorkCond != NCD_IDLE_EMIT ) &&
@ (new_cond != NCD_NO_COMMAND ));
@ ensures gWorkCond == \old( gWorkCond );
@ complete behaviors ;
@ disjoint behaviors ;
@*/
void cbit_set_work_cond ( uint16_t new_cond);
```

تتوافق مواصفات السلوك الثلاث أعلاه مباشرة مع متطلبات اللغة الطبيعية بحيث يمكن استبدالها بالمتطلبات المُصاغة رسمياً. يمكن تسمية بند السلوك كما هو موضح في المثال مما يسهل التتبع للمتطلبات الأعلى مستوى، وهو هدف يتم التأكيد عليه بشدة في معايير الطيران. تمثل بنود assumes الجزء الشرطي من متطلبات اللغة الطبيعية ويتم تقييمها في بداية تنفيذ الدالة. علاوة على ذلك، مع بنود complete وdisjoint يمكن للمرء التحقق تلقائياً من اكتمال واتساق المواصفة الرسمية.

لاحظ أن بنود assigns تم حذفها من المواصفة أعلاه على الرغم من أن هذا غير مستحسن في دليل مرجع ACSL ([4]، القسم 2.3.5). ومع ذلك، فإن إضافة بنود assigns تولد شروط تحقق لا يمكن إثباتها. هذا بسبب حقيقة أن الدالة تعدل متغير حالة ذو نطاق ملف (WorkCondition) والذي لا يمكن إدراجه في بند assigns لأنه غير مرئي هناك. عدة حلول لهذه المشكلة قيد المناقشة على القائمة البريدية للأداة في وقت كتابة هذا.

للتحقق، يجب محاذاة متغير الحالة الشبح مع متغير الوحدة الداخلي باستخدام التأكيدات، كما هو موضح أدناه:

```c
void cbit_set_work_cond ( uint16_t new_cond )
{
//@ assert gWorkCond == WorkCondition ;
if (( WorkCondition == NCD_IDLE_EMIT ) || ( new_cond == NCD_NO_COMMAND) )
{
WorkCondition = new_cond ;
//@ ghost gWorkCond = WorkCondition ;
}
}
```

التأكيد في السطر 3 ضروري لإبلاغ المُثبِت بأن الحالة الداخلية تساوي دائماً حالة الشبح. لا يمكن إثبات ذلك.

تولد إضافة WP شرط تحقق لكل تأكيد. شروط التحقق مشابهة لحالات الاختبار في التحقق التقليدي بحيث أن شرط التحقق الذي لا يمكن إثباته مطابق لحالة اختبار فشلت. لذلك، هناك حاجة لتبرير التأكيد في السطر 3 لتحقيق الهدف FM2 من الجدول FM.C-7 من DO-333 الذي يتطلب أن تكون نتائج التحليل الرسمي صحيحة ويتم شرح التناقضات.

تمثيل الحالة الداخلية بمتغير شبح ليس مثالياً كما هو مشار إليه أعلاه. كان من الأفضل تحديد الدالة cbit_set_work_cond ونظيرتها cbit_get_work_cond باستخدام تقنيات المواصفات الجبرية بالطريقة الموضحة في [8] لمثال المكدس. النهج الموصوف هناك يحول البديهيات إلى شفرة C إضافية مُعلَّق عليها بـ ACSL. هذا يعني بشكل أساسي أن شفرة C تُستخدم كمتطلبات منخفضة المستوى وهو أمر غير مقبول. إن إدراج تقنيات المواصفات الجبرية في ACSL سيكون على الأرجح الحل الأكثر أناقة لهذه المشكلة.

---

### Translation Notes

- **Key Terms:**
  - Behavioral specification: مواصفة السلوك
  - Iterative approach: نهج تكراري
  - Instrumentation: أدوات قياس
  - Assertions: تأكيدات
  - Loop invariants: ثوابت الحلقات
  - Module variable: متغير وحدة
  - Persistent variable: متغير ثابت
  - Setter and getter functions: دوال تعيين وجلب
  - State variable: متغير الحالة
  - Ghost variable: متغير شبح
  - File scope: نطاق ملف
  - Header file: ملف رأسية
  - Traceability: التتبع
  - Completeness: اكتمال
  - Consistency: اتساق
  - Verification condition: شرط تحقق
  - Algebraic specification: المواصفات الجبرية

- **Code Examples:** Multiple C and ACSL code snippets preserved in English
- **Citations:** [4], [8]

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
