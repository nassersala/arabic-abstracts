# Section 5: Evaluation
## القسم 5: التقييم

**Section:** evaluation
**Translation Quality:** 0.86
**Glossary Terms Used:** robotics, API, Future, specification, TLA+, FocusST, formula, validation

---

### English Version

The evaluation is based on a case study that involves robotics that are installed in the Virtual Experiences Lab (VXLab) at RMIT University, Australia.

**Figure 2. Interacting with robots from the VXLab at RMIT**

[Image shows researchers working with robotic arms through multiple display screens in a control room]

The implemented model will be installed in the robotic arms or simulations of them. For instance, assuming the existence of the function `initialisePosition(): Future[Position]` which is responsible to move a robotic arm to an initial position. The Future data type is used because moving arms takes long time and we need to verify the final position the arm reached after the API call. However, since `initialisePosition()` is just returning the initial position, it will return instantly. The framework will call this API function and simultaneously check whether it is in accordance to the specified state. Failing tests for the intended framework might indicate:

– Failure in the software of the system under test. This is one of the benefits of property based testing. The found error may have never been discovered otherwise.
– Wrong specification. The system under test may have been wrongly under-specified. In this case, the engineer might change the formulas to reflect system required properties.

Therefore, the input to the framework is formal-methods formulas and the output is the correct behaviours specified by these formulas. The formulas are written in host programming language (Scala in this research). For example, the initial state for the aforementioned robotic example would be specified as follows:

```scala
val position: TLAVariable = TLAVariable("Y")
val init: TLAInit = position
```

For this simple example (the next formula has been omitted for simplicity), the only possible correct behaviour for this specification formula is that position should equal to "Y". The framework will then check whether the position was indeed "Y" after the call to `initialisePosition()`, otherwise, it reports an error.

**Table 1. Evaluating cases with TLA+ Init Formulas**

| API Code | Init Formula | Result | Error? |
|----------|--------------|--------|--------|
| initialisePosition() | TLAVariable("Y") | "Y" | No |
| initialisePosition() | TLAVariable("Y") | "K" | Yes |
| moveToQ() | TLAVariable("Q") | "Q" | Yes |
| moveToR() | TLAVariable("Q") | "M" | Yes |

Table 1 shows some examples for the evaluation of the intended framework using TLA+ formula (FocusST evaluation will follow similar pattern). The first call to `initialisePosition()` is correctly specified and the actual result reflects the specification (assuming arm initial position is "Y"), as a result, it is regarded as a successful case. The second call to `initialisePosition()` is different from the actual position, therefore, its was reported as an error. Although the result is expected for the call to `moveToQ()` in the third case, the framework reports an error because the specification is not correct (the arm can not logically move to its current position). Finally, `moveToR` is reported as error because the actual result (reached position) is not correct. The result column is calculated by getting the value from the Future datatype that each API call returns through onComplete callback as follows:

```scala
initialisePosition() onComplete {
  case Success(position) => println(position)
  case Failure(t) => println("An error has occured: " + t.getMessage)
}
```

---

### النسخة العربية

يعتمد التقييم على دراسة حالة تتضمن الروبوتات المثبتة في مختبر التجارب الافتراضية (VXLab) في جامعة RMIT، أستراليا.

**الشكل 2. التفاعل مع الروبوتات من VXLab في RMIT**

[تُظهر الصورة باحثين يعملون مع أذرع روبوتية من خلال شاشات عرض متعددة في غرفة التحكم]

سيتم تثبيت النموذج المنفذ في الأذرع الروبوتية أو محاكاتها. على سبيل المثال، بافتراض وجود الدالة `initialisePosition(): Future[Position]` المسؤولة عن نقل ذراع روبوتية إلى موضع أولي. يُستخدم نوع البيانات Future لأن تحريك الأذرع يستغرق وقتاً طويلاً ونحتاج إلى التحقق من الموضع النهائي الذي وصل إليه الذراع بعد استدعاء واجهة برمجة التطبيقات. ومع ذلك، نظراً لأن `initialisePosition()` تعيد فقط الموضع الأولي، فستعود على الفور. سيستدعي إطار العمل دالة واجهة برمجة التطبيقات هذه ويتحقق في وقت واحد مما إذا كانت متوافقة مع الحالة المحددة. قد تشير الاختبارات الفاشلة لإطار العمل المقصود إلى:

– فشل في برمجيات النظام قيد الاختبار. هذه واحدة من فوائد الاختبار القائم على الخصائص. قد لا يتم اكتشاف الخطأ الموجود أبداً بطريقة أخرى.
– مواصفات خاطئة. قد يكون النظام قيد الاختبار قد تم تحديد مواصفاته بشكل خاطئ. في هذه الحالة، قد يغير المهندس الصيغ لتعكس خصائص النظام المطلوبة.

لذلك، فإن المدخل إلى إطار العمل هو صيغ الأساليب الرسمية والمخرج هو السلوكيات الصحيحة المحددة بواسطة هذه الصيغ. تُكتب الصيغ في لغة البرمجة المضيفة (Scala في هذا البحث). على سبيل المثال، سيتم تحديد الحالة الأولية لمثال الروبوت المذكور أعلاه على النحو التالي:

```scala
val position: TLAVariable = TLAVariable("Y")
val init: TLAInit = position
```

بالنسبة لهذا المثال البسيط (تم حذف الصيغة التالية للبساطة)، فإن السلوك الصحيح الوحيد الممكن لصيغة المواصفات هذه هو أن الموضع يجب أن يساوي "Y". سيتحقق إطار العمل بعد ذلك مما إذا كان الموضع فعلاً "Y" بعد استدعاء `initialisePosition()`، وإلا فإنه يبلغ عن خطأ.

**الجدول 1. تقييم الحالات باستخدام صيغ TLA+ الأولية**

| شفرة واجهة برمجة التطبيقات | صيغة الحالة الأولية | النتيجة | خطأ؟ |
|----------|--------------|--------|--------|
| initialisePosition() | TLAVariable("Y") | "Y" | لا |
| initialisePosition() | TLAVariable("Y") | "K" | نعم |
| moveToQ() | TLAVariable("Q") | "Q" | نعم |
| moveToR() | TLAVariable("Q") | "M" | نعم |

يوضح الجدول 1 بعض الأمثلة لتقييم إطار العمل المقصود باستخدام صيغة TLA+ (سيتبع تقييم FocusST نمطاً مشابهاً). يتم تحديد الاستدعاء الأول لـ `initialisePosition()` بشكل صحيح وتعكس النتيجة الفعلية المواصفات (بافتراض أن موضع الذراع الأولي هو "Y")، ونتيجة لذلك، يُعتبر حالة ناجحة. يختلف الاستدعاء الثاني لـ `initialisePosition()` عن الموضع الفعلي، لذلك تم الإبلاغ عنه كخطأ. على الرغم من أن النتيجة متوقعة لاستدعاء `moveToQ()` في الحالة الثالثة، يبلغ إطار العمل عن خطأ لأن المواصفات غير صحيحة (لا يمكن للذراع منطقياً التحرك إلى موضعه الحالي). أخيراً، يتم الإبلاغ عن `moveToR` كخطأ لأن النتيجة الفعلية (الموضع الذي تم الوصول إليه) غير صحيحة. يتم حساب عمود النتيجة من خلال الحصول على القيمة من نوع البيانات Future الذي يعيده كل استدعاء لواجهة برمجة التطبيقات من خلال استدعاء onComplete على النحو التالي:

```scala
initialisePosition() onComplete {
  case Success(position) => println(position)
  case Failure(t) => println("An error has occured: " + t.getMessage)
}
```

---

### Translation Notes

- **Figures referenced:** Figure 2 (VXLab robotics setup)
- **Key terms introduced:** VXLab, Future datatype, robotic arms, onComplete callback, under-specified
- **Equations:** None
- **Citations:** None in this section
- **Special handling:** Table 1 with evaluation cases, code examples for Scala Future handling

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
