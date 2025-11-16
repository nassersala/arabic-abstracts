# Section 6: Conclusions
## القسم 6: الخاتمة

**Section:** conclusion
**Translation Quality:** 0.88
**Glossary Terms Used:** monad, functional programming, call-by-value, call-by-name, call-by-need, evaluation strategy, category theory, computational comonad

---

### English Version

We presented an alternative translation from purely functional code to monadic form. Previously, this required choosing either the *call-by-name* or the *call-by-value* translation and the translated code had different structure and different types in both cases. Our translation abstracts the evaluation strategy into a function *malias* that can be implemented separately providing the required evaluation strategy.

Our translation is not limited to the above two evaluation strategies. Most interestingly, we show that certain monads can be automatically turned into an extended version that supports the *call-by-need* strategy. This answers part of an interesting open problem posed by Wadler. The approach has other interesting applications -- it makes it possible to write code that is parameterized by the evaluation strategy and it allows implementing a *parallel call-by-need* strategy for certain monads.

Finally, we presented the theoretical foundations of our approach using a model described in terms of category theory. We extended the monad structure with an additional operation based on *computational comonads*, which were previously used to give intensional semantics of computations. In our setting, the operation specifies the evaluation order. The categorical model specifies laws about *malias* and we proved that the laws hold for *call-by-value* and *call-by-name* strategies.

**Acknowledgements.** The author is grateful to Sebastian Fischer, Dominic Orchard and Alan Mycroft for inspiring comments and discussion, and to the latter two for proofreading the paper. We are also grateful to anonymous referees for detailed comments and to Paul Blain Levy for shepherding of the paper. The work has been partly supported by EPSRC and through the Cambridge CHESS scheme.

---

### النسخة العربية

قدمنا ترجمة بديلة من الشفرة الوظيفية النقية إلى صيغة موناد. سابقاً، تطلب هذا اختيار إما ترجمة *استدعاء بالاسم* أو *استدعاء بالقيمة* وكان للشفرة المترجمة بنية وأنواع مختلفة في كلتا الحالتين. تجرد ترجمتنا استراتيجية التقييم في دالة *malias* التي يمكن تطبيقها بشكل منفصل لتوفير استراتيجية التقييم المطلوبة.

ترجمتنا ليست محدودة باستراتيجيتي التقييم المذكورتين أعلاه. والأكثر إثارة للاهتمام، نُظهر أن بعض الموناد يمكن تحويلها تلقائياً إلى نسخة موسعة تدعم استراتيجية *استدعاء بالحاجة*. هذا يجيب على جزء من مشكلة مفتوحة مثيرة للاهتمام طرحها Wadler. للنهج تطبيقات مثيرة أخرى -- فهو يجعل من الممكن كتابة شفرة مُعَلّمة باستراتيجية التقييم ويسمح بتطبيق استراتيجية *استدعاء بالحاجة الموازية* لموناد معينة.

أخيراً، قدمنا الأسس النظرية لنهجنا باستخدام نموذج موصوف بمصطلحات نظرية التصنيف. وسّعنا بنية الموناد بعملية إضافية بناءً على *الكوموناد الحوسبية*، التي استُخدمت سابقاً لإعطاء دلاليات كثافية للحسابات. في سياقنا، تحدد العملية ترتيب التقييم. يحدد النموذج الفئوي القوانين حول *malias* وأثبتنا أن القوانين تحقق لاستراتيجيات *استدعاء بالقيمة* و*استدعاء بالاسم*.

**شكر وتقدير.** يشكر المؤلف Sebastian Fischer و Dominic Orchard و Alan Mycroft على التعليقات والمناقشات الملهمة، والأخيرين على مراجعة البحث. نحن ممتنون أيضاً للمحكمين المجهولين على التعليقات التفصيلية ولـ Paul Blain Levy على رعاية البحث. تم دعم العمل جزئياً من قبل EPSRC ومن خلال مخطط Cambridge CHESS.

---

### Translation Notes

- **Key contributions summarized:**
  1. Alternative translation abstracting evaluation strategy
  2. Support for call-by-need in certain monads
  3. Parameterization by evaluation strategy
  4. Categorical theoretical foundations
- **Acknowledgements:** Preserved names and institutions
- **Special handling:**
  - EPSRC and Cambridge CHESS kept as proper nouns
  - Names of researchers kept in English

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.89
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88

### Back-Translation Check

First paragraph back-translates to: "We presented an alternative translation from pure functional code to monad form. Previously, this required choosing either *call-by-name* or *call-by-value* translation and the translated code had different structure and types in both cases. Our translation abstracts the evaluation strategy in a *malias* function that can be implemented separately to provide the required evaluation strategy."
