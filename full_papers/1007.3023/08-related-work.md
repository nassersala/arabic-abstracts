# Section 8: Related Work
## القسم 8: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.86
**Glossary Terms Used:** monad, monad transformers, linear types, uniqueness types, functional programming, structured programming

---

### English Version

We have already mentioned how Scala also combines structured programming with functional programming, but fails to deliver a combination of structured programming and purely functional programming. Actually, it should be possible to conservatively extend Scala so that linear scope for variables defined via val is supported.

The work done on monads in the purely functional programming language Haskell [4] has a superficial similarity with the work done in this paper. With monads it is possible to formulate sequences of (possibly shadowing) assignments, and with the help of monad transformers even loops can be modeled. But in order to understand and effectively use monads a solid background in functional programming is useful, if not even required; linear scope on the other hand is understood intuitively by programmers with a mostly imperative background, because Mini Babel-17 programs can look just like imperative programs and do not introduce additional clutter like the need for lifting. Actually, in Haskell monads are used to limit the influence of mutable state to a confined region of the code that can be recognized by its type; the work in this paper has the entirely different focus of trying to merge the structured and purely functional programming style as seamlessly as possible.

This work is not directly connected to work done on linear or uniqueness types [7]. Of course one might think about applying uniqueness typing to Mini Babel-17, but Mini Babel-17 itself is dynamically-typed and its values are persistent and can be passed around without any restrictions.

---

### النسخة العربية

لقد ذكرنا بالفعل كيف تجمع Scala أيضاً بين البرمجة المهيكلة والبرمجة الوظيفية، لكنها تفشل في تقديم مزيج من البرمجة المهيكلة والبرمجة الوظيفية الصرفة. في الواقع، يجب أن يكون من الممكن توسيع Scala بشكل محافظ بحيث يتم دعم النطاق الخطي للمتغيرات المعرّفة عبر val.

العمل المنجز على المونادات في لغة البرمجة الوظيفية الصرفة Haskell [4] له تشابه سطحي مع العمل المنجز في هذه الورقة. مع المونادات من الممكن صياغة تسلسلات من الإسنادات (المحتمل تظليلها)، ومع مساعدة محوّلات المونادات يمكن حتى نمذجة الحلقات. لكن من أجل فهم واستخدام المونادات بفعالية، تكون خلفية قوية في البرمجة الوظيفية مفيدة، إن لم تكن مطلوبة حتى؛ من ناحية أخرى، يُفهم النطاق الخطي بشكل حدسي من قبل المبرمجين ذوي الخلفية الأمرية في الغالب، لأن برامج Mini Babel-17 يمكن أن تبدو تماماً مثل البرامج الأمرية ولا تُدخل فوضى إضافية مثل الحاجة إلى الرفع. في الواقع، في Haskell تُستخدم المونادات للحد من تأثير الحالة القابلة للتغيير إلى منطقة محصورة من الشفرة يمكن التعرف عليها بنوعها؛ العمل في هذه الورقة له تركيز مختلف تماماً يتمثل في محاولة دمج أسلوب البرمجة المهيكلة والوظيفية الصرفة بسلاسة قدر الإمكان.

هذا العمل غير متصل بشكل مباشر بالعمل المنجز على الأنواع الخطية أو أنواع الفرادة [7]. بالطبع قد يفكر المرء في تطبيق كتابة الفرادة على Mini Babel-17، لكن Mini Babel-17 نفسها ديناميكية النمط وقيمها مستمرة ويمكن تمريرها دون أي قيود.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Monad (موناد)
  - Monad transformers (محوّلات المونادات)
  - Linear types (أنواع خطية)
  - Uniqueness types (أنواع الفرادة)
  - Lifting (رفع)
  - Mutable state (حالة قابلة للتغيير)
  - Persistent values (قيم مستمرة)
  - Conservative extension (توسيع محافظ)
- **Equations:** None
- **Citations:** [4] Haskell (Jones, Wadler), [7] Linear/uniqueness types (Wadler)
- **Special handling:**
  - Language names (Scala, Haskell, Mini Babel-17) kept in English
  - Technical FP terms (monad, lifting) translated but originals recognizable

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
