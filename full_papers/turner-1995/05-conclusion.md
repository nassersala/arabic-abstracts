# Section 5: Observations and Concluding Remarks
## القسم 5: ملاحظات وتعليقات ختامية

**Section:** conclusion
**Translation Quality:** 0.87
**Glossary Terms Used:** functional programming, data, codata, type system, termination, Turing completeness, halting problem

---

### English Version

I have outlined an elementary discipline of strong (or total) functional programming, in which we have both finite data and (potentially) infinite codata, which we keep separate from each other by a minor variant of the Hindley Milner type discipline. There are syntactic restrictions on recursion and corecursion which ensure well-foundation for the former, and finite progress for the latter, and simple proof rules for both data and codata.

Although the particular syntactic discipline proposed may be too restrictive (particularly in the forms of corecursion it permits - further research is required here) I would like to argue that the distinction between data and codata is very helpful to a clean discipline of functional programming, and gives us a better teaching vehicle, and perhaps a better vehicle for production programming also (because of the greater freedom of choice for the implementor).

A question we postponed from section 2 is whether we ought to be willing to give up Turing completeness. Anyone who has taken a course in theory of computation will be familiar with the following result, which is a corollary of the Halting Theorem.

**Theorem:** For any language in which all programs terminate, there are always-terminating programs which cannot be written in it - among these are the interpreter for the language itself.

So if we call our proposed language for strong functional programming, L, an interpreter for L in L cannot be written. Does this really matter? I can see two arguments which suggest this might in fact be something to which we could accommodate ourselves quite easily

1) We will have a hierarchy of languages, of ascending power, each of which can express the interpreters of those below it. For example if our language L has a first order type system, we can easily add some second order features to get a language L2, in which we can write the interpreter for L, and so on up. Constructive type theory, with its hierarchy of universes, is like this, for example.

2) There is no such theoretical obstacle to our writing a compiler for L in L, which is of far greater practical importance.

**Summary**

There is a dichotomy in language design, because of the halting problem. For our programming discipline we are forced to choose between

A) **Security** - a language in which all programs are known to terminate.

B) **Universality** - a language in which we can write
  (i) all terminating programs
  (ii) silly programs which fail to terminate

and, given an arbitrary program we cannot in general say if it is (i) or (ii).

Four decades ago, at the beginning of electronic computing, we chose (B). It may be time to reconsider this decision.

---

### النسخة العربية

لقد حددت انضباطاً أولياً للبرمجة الوظيفية القوية (أو الكلية)، حيث لدينا كل من البيانات المحدودة والبيانات المشتركة (اللانهائية محتملاً)، التي نحتفظ بها منفصلة عن بعضها البعض من خلال متغير طفيف من انضباط نوع Hindley Milner. هناك قيود تركيبية على التكرار والتكرار المشترك تضمن التأسيس الجيد للأول، والتقدم المحدود للأخير، وقواعد إثبات بسيطة لكل من البيانات والبيانات المشتركة.

على الرغم من أن الانضباط التركيبي المعين المقترح قد يكون مقيداً جداً (خاصة في أشكال التكرار المشترك التي يسمح بها - هناك حاجة إلى مزيد من البحث هنا) أود أن أجادل بأن التمييز بين البيانات والبيانات المشتركة مفيد جداً لانضباط نظيف للبرمجة الوظيفية، ويعطينا وسيلة تدريس أفضل، وربما وسيلة أفضل للبرمجة الإنتاجية أيضاً (بسبب حرية الاختيار الأكبر للمُنفِّذ).

سؤال أجلناه من القسم 2 هو ما إذا كان يجب أن نكون على استعداد للتخلي عن اكتمال تورينج. أي شخص أخذ دورة في نظرية الحساب سيكون على دراية بالنتيجة التالية، وهي نتيجة طبيعية لنظرية التوقف.

**نظرية:** لأي لغة تنتهي فيها جميع البرامج، هناك برامج منتهية دائماً لا يمكن كتابتها فيها - من بينها مفسر اللغة نفسها.

لذا إذا أطلقنا على لغتنا المقترحة للبرمجة الوظيفية القوية اسم L، فلا يمكن كتابة مفسر لـ L في L. هل هذا مهم حقاً؟ يمكنني رؤية حجتين تشيران إلى أن هذا قد يكون في الواقع شيئاً يمكننا أن نتكيف معه بسهولة تامة

1) سيكون لدينا تسلسل هرمي من اللغات، ذات قوة متصاعدة، يمكن لكل منها التعبير عن مفسرات تلك التي تحتها. على سبيل المثال، إذا كانت لغتنا L لها نظام نوع من الدرجة الأولى، يمكننا بسهولة إضافة بعض ميزات الدرجة الثانية للحصول على لغة L2، التي يمكننا فيها كتابة مفسر لـ L، وهكذا. نظرية الأنواع البنائية، مع تسلسلها الهرمي من الأكوان، مثل هذا، على سبيل المثال.

2) لا يوجد مثل هذا العائق النظري لكتابة مترجم لـ L في L، وهو ذو أهمية عملية أكبر بكثير.

**ملخص**

هناك ثنائية في تصميم اللغة، بسبب مشكلة التوقف. لانضباطنا البرمجي، نُجبَر على الاختيار بين

A) **الأمان** - لغة تُعرف فيها جميع البرامج بأنها تنتهي.

B) **العمومية** - لغة يمكننا فيها كتابة
  (i) جميع البرامج المنتهية
  (ii) برامج سخيفة تفشل في الإنهاء

وبإعطاء برنامج تعسفي، لا يمكننا بشكل عام القول ما إذا كان (i) أو (ii).

قبل أربعة عقود، في بداية الحوسبة الإلكترونية، اخترنا (B). قد يكون الوقت قد حان لإعادة النظر في هذا القرار.

---

### Translation Notes

- **Key terms introduced:**
  - Hindley Milner type discipline (انضباط نوع Hindley Milner)
  - well-foundation (تأسيس جيد)
  - finite progress (تقدم محدود)
  - Turing completeness (اكتمال تورينج)
  - Halting Theorem (نظرية التوقف)
  - hierarchy of languages (تسلسل هرمي من اللغات)
  - hierarchy of universes (تسلسل هرمي من الأكوان)
  - security vs universality (الأمان مقابل العمومية)
  - halting problem (مشكلة التوقف)
- **Central argument:** The dichotomy between security (guaranteed termination) and universality (Turing completeness)
- **Historical perspective:** Suggests reconsidering the 40-year-old choice of universality over security
- **Citations:** None in this section
- **Special handling:** Two-choice dichotomy (A/B) formatted with clear emphasis

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.87
- Glossary consistency: 0.87
- **Overall section score:** 0.87
