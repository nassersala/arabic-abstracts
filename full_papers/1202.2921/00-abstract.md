# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.88
**Glossary Terms Used:** monad, functional programming, call-by-value, call-by-name, call-by-need, evaluation strategy, computational comonad

---

### English Version

Monads have become a powerful tool for structuring effectful computations in functional programming, because they make the order of effects explicit. When translating pure code to a monadic version, we need to specify evaluation order explicitly. Two standard translations give *call-by-value* and *call-by-name* semantics. The resulting programs have different structure and types, which makes revisiting the choice difficult.

In this paper, we translate pure code to monadic using an additional operation *malias* that abstracts out the evaluation strategy. The *malias* operation is based on *computational comonads*; we use a categorical framework to specify the laws that are required to hold about the operation.

For any monad, we show implementations of *malias* that give *call-by-value* and *call-by-name* semantics. Although we do not give *call-by-need* semantics for *all* monads, we show how to turn certain monads into an extended monad with *call-by-need* semantics, which partly answers an open question. Moreover, using our unified translation, it is possible to change the evaluation strategy of functional code translated to the monadic form without changing its structure or types.

---

### النسخة العربية

أصبحت الموناد أداة قوية لهيكلة الحسابات ذات الآثار الجانبية في البرمجة الوظيفية، لأنها تجعل ترتيب الآثار صريحاً. عند ترجمة الشفرة النقية إلى نسخة موناد، نحتاج إلى تحديد ترتيب التقييم بشكل صريح. تعطي الترجمتان القياسيتان دلاليات *استدعاء بالقيمة* و*استدعاء بالاسم*. تمتلك البرامج الناتجة بنية وأنواع مختلفة، مما يجعل إعادة النظر في الاختيار أمراً صعباً.

في هذا البحث، نترجم الشفرة النقية إلى صيغة موناد باستخدام عملية إضافية *malias* تجرد استراتيجية التقييم. تستند عملية *malias* إلى *الكوموناد الحوسبية* (computational comonads)؛ ونستخدم إطار عمل فئوي لتحديد القوانين المطلوب أن تحققها العملية.

لأي موناد، نُظهر تطبيقات *malias* تعطي دلاليات *استدعاء بالقيمة* و*استدعاء بالاسم*. على الرغم من أننا لا نعطي دلاليات *استدعاء بالحاجة* لـ*جميع* الموناد، نُظهر كيفية تحويل موناد معينة إلى موناد موسّعة بدلاليات *استدعاء بالحاجة*، مما يجيب جزئياً على سؤال مفتوح. علاوة على ذلك، باستخدام ترجمتنا الموحدة، من الممكن تغيير استراتيجية التقييم للشفرة الوظيفية المترجمة إلى الصيغة الموناد دون تغيير بنيتها أو أنواعها.

---

### Translation Notes

- **Key terms introduced:** malias (operation name kept in English as it's a specific technical term introduced in the paper), computational comonads (الكوموناد الحوسبية)
- **Technical accuracy:** The translation preserves the nuance between "all monads" vs "certain monads" when discussing call-by-need semantics
- **Special handling:** The term "malias" is kept in English as it's a coined term specific to this paper and not a general concept

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.90
- Readability: 0.85
- Glossary consistency: 0.88
- **Overall section score:** 0.88

### Back-Translation Check

The Arabic translates back to: "Monads have become a powerful tool for structuring computations with side effects in functional programming, as they make the order of effects explicit. When translating pure code to a monad version, we need to specify the evaluation order explicitly. The two standard translations give *call-by-value* and *call-by-name* semantics. The resulting programs have different structure and types, making reconsideration of the choice difficult. In this paper, we translate pure code to monad form using an additional *malias* operation that abstracts the evaluation strategy. The *malias* operation is based on *computational comonads*; we use a categorical framework to specify the laws required to be satisfied by the operation. For any monad, we show *malias* implementations that give *call-by-value* and *call-by-name* semantics. Although we do not give *call-by-need* semantics for *all* monads, we show how to convert certain monads to an extended monad with *call-by-need* semantics, partially answering an open question. Moreover, using our unified translation, it is possible to change the evaluation strategy of functional code translated to monad form without changing its structure or types."
