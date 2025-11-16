# Section 5: Related work
## القسم 5: الأعمال ذات الصلة

**Section:** related work
**Translation Quality:** 0.86
**Glossary Terms Used:** monad, comonad, evaluation strategy, call-by-need, call-by-value, call-by-name, functional programming, applicative functor

---

### English Version

Most of the work that directly influenced this work has been discussed throughout the paper. Most importantly, the question of translating pure code to a monadic version with *call-by-need* semantics was posed by Wadler. To our knowledge, this question has not been answered before, but there is various work that either uses similar structures or considers evaluation strategies from different perspectives.

**Monads with aliasing.** Numerous monads have independently introduced an operation of type `m a -> m (m a)`. The `eagerly` combinator of the Orc monad causes computation to run in parallel, effectively implementing the *parallel call-by-need* evaluation strategy. The only law that relates `eagerly` to operations of a monad is too restrictive to allow the *call-by-value* semantics.

A monad for purely functional lazy non-deterministic programming uses a similar combinator `share` to make monadic (non-deterministic) computations lazy. However, the *call-by-value* strategy is inefficient and the *call-by-name* strategy is incorrect, because choosing a different value each time a non-deterministic computation is accessed means that *generate and test* pattern does not work.

The `share` operation is described together with the laws that should hold. The *HNF* law is similar to our *computationality*. However, the *Ignore* law specifies that the `share` operation should not be strict (ruling out our *call-by-value* implementation of *malias*). A related paper discusses where `share` needs to be inserted when translating lazy non-deterministic programs to a monadic form. The results may be directly applicable to make our translation more efficient by inserting *malias* only when required.

**Abstract computations and comonads.** In this paper, we extended monads with one component of a comonadic structure. Although less widespread than monads, comonads are also useful for capturing abstract computations in functional programming. They have been used for dataflow programming, array programming, environment passing, and more. In general, comonads can be used to describe context-dependent computations, where `cojoin` (natural transformation δ) duplicates the context. In our work, the corresponding operation *malias* splits the context (effects) in a particular way between two computations.

We only considered basic monadic computations, but it would be interesting to see how *malias* interacts with other abstract notions of computations, such as *applicative functors*, *arrows* or additive monads (the `MonadPlus` type-class). The monad for lazy non-deterministic programming, mentioned earlier, implements `MonadPlus` and may thus provide interesting insights.

**Evaluation strategies.** One of the key results of this paper is a monadic translation from purely functional code to a monadic version that has the *call-by-need* semantics. We achieve that using the monad transformer for adding state.

In the absence of effects, *call-by-need* is equivalent to *call-by-name*, but it has been described formally as a version of λ-calculus by Ariola and Felleisen. This allows equational reasoning about computations and it could be used to show that our encoding directly corresponds to *call-by-need*, similarly to proofs for other strategies. The semantics has been also described using an environment that models caching, which closely corresponds to our actual implementation.

Considering the two basic evaluation strategies, Wadler shows that *call-by-name* is dual to *call-by-value*. We find this curious as the two definitions of *malias* in our work are, in some sense, also dual or symmetric as they associate all effects with the inner or the outer monad of the type `m (m a)`. Furthermore, the duality between *call-by-name* and *call-by-value* can be viewed from a logical perspective thanks to the Curry-Howard correspondence. We believe that finding a similar logical perspective for our generalized strategy may be an interesting future work.

Finally, the work presented in this work unifies monadic *call-by-name* and *call-by-value*. In a non-monadic setting, a similar goal is achieved by the *call-by-push-value* calculus. The calculus is more fine-grained and strictly separates *values* and *computations*. Using these mechanisms, it is possible to encode both *call-by-name* and *call-by-value*. It may be interesting to consider whether our computations parameterized over evaluation strategy could be encoded in *call-by-push-value*.

---

### النسخة العربية

تمت مناقشة معظم الأعمال التي أثرت بشكل مباشر على هذا العمل في جميع أنحاء البحث. والأهم من ذلك، أن سؤال ترجمة الشفرة النقية إلى نسخة موناد بدلاليات *استدعاء بالحاجة* طُرح من قبل Wadler. على حد علمنا، لم تتم الإجابة على هذا السؤال من قبل، ولكن هناك أعمال متنوعة إما تستخدم بنى مماثلة أو تنظر في استراتيجيات التقييم من وجهات نظر مختلفة.

**الموناد مع الأسماء المستعارة.** قدمت العديد من الموناد بشكل مستقل عملية من نوع `m a -> m (m a)`. يتسبب المجمّع `eagerly` لموناد Orc في تشغيل الحساب بالتوازي، منفذاً بشكل فعال استراتيجية التقييم *استدعاء بالحاجة الموازية*. القانون الوحيد الذي يربط `eagerly` بعمليات موناد مقيد للغاية ولا يسمح بدلاليات *استدعاء بالقيمة*.

تستخدم موناد للبرمجة اللاحتمية الكسولة النقية مجمّعاً مماثلاً `share` لجعل حسابات الموناد (اللاحتمية) كسولة. ومع ذلك، فإن استراتيجية *استدعاء بالقيمة* غير فعالة واستراتيجية *استدعاء بالاسم* غير صحيحة، لأن اختيار قيمة مختلفة في كل مرة يتم فيها الوصول إلى حساب لاحتمي يعني أن نمط *التوليد والاختبار* لا يعمل.

يتم وصف عملية `share` مع القوانين التي يجب أن تحققها. قانون *HNF* مماثل لقانون *الحوسبية* لدينا. ومع ذلك، يحدد قانون *Ignore* أن عملية `share` يجب ألا تكون صارمة (مما يستبعد تطبيق *استدعاء بالقيمة* لدينا لـ *malias*). يناقش بحث ذو صلة مكان إدراج `share` عند ترجمة البرامج اللاحتمية الكسولة إلى صيغة موناد. قد تكون النتائج قابلة للتطبيق مباشرة لجعل ترجمتنا أكثر كفاءة من خلال إدراج *malias* فقط عند الحاجة.

**الحسابات المجردة والكوموناد.** في هذا البحث، وسّعنا الموناد بمكون واحد من بنية كوموناد. على الرغم من أنها أقل انتشاراً من الموناد، فإن الكوموناد مفيدة أيضاً لالتقاط الحسابات المجردة في البرمجة الوظيفية. لقد استُخدمت للبرمجة بتدفق البيانات، والبرمجة بالمصفوفات، وتمرير البيئة، والمزيد. بشكل عام، يمكن استخدام الكوموناد لوصف الحسابات المعتمدة على السياق، حيث `cojoin` (التحويل الطبيعي δ) يضاعف السياق. في عملنا، العملية المقابلة *malias* تقسم السياق (الآثار) بطريقة معينة بين حسابين.

نظرنا فقط في حسابات الموناد الأساسية، لكن سيكون من المثير للاهتمام معرفة كيف يتفاعل *malias* مع مفاهيم الحسابات المجردة الأخرى، مثل *الدوال التصنيفية التطبيقية* (applicative functors)، أو *الأسهم* (arrows)، أو الموناد الجمعية (صنف النوع `MonadPlus`). الموناد للبرمجة اللاحتمية الكسولة، المذكورة سابقاً، تطبق `MonadPlus` وبالتالي قد توفر رؤى مثيرة للاهتمام.

**استراتيجيات التقييم.** أحد النتائج الرئيسية لهذا البحث هو ترجمة موناد من شفرة وظيفية نقية إلى نسخة موناد لها دلاليات *استدعاء بالحاجة*. نحقق ذلك باستخدام محول الموناد لإضافة الحالة.

في غياب الآثار، *استدعاء بالحاجة* يكافئ *استدعاء بالاسم*، لكنه وُصف رسمياً كنسخة من حساب λ من قبل Ariola و Felleisen. هذا يسمح بالاستدلال المعادلي حول الحسابات ويمكن استخدامه لإظهار أن ترميزنا يتوافق مباشرة مع *استدعاء بالحاجة*، بشكل مماثل للإثباتات لاستراتيجيات أخرى. وُصفت الدلاليات أيضاً باستخدام بيئة تنمذج التخزين المؤقت، مما يتوافق بشكل وثيق مع تطبيقنا الفعلي.

بالنظر إلى استراتيجيتي التقييم الأساسيتين، يُظهر Wadler أن *استدعاء بالاسم* مزدوج لـ *استدعاء بالقيمة*. نجد هذا مثيراً للفضول حيث أن تعريفي *malias* في عملنا، بمعنى ما، مزدوجان أو متماثلان أيضاً حيث يربطان جميع الآثار بالموناد الداخلية أو الخارجية من النوع `m (m a)`. علاوة على ذلك، يمكن النظر إلى الازدواجية بين *استدعاء بالاسم* و*استدعاء بالقيمة* من منظور منطقي بفضل مطابقة Curry-Howard. نعتقد أن إيجاد منظور منطقي مماثل لاستراتيجيتنا المعممة قد يكون عملاً مستقبلياً مثيراً للاهتمام.

أخيراً، يوحد العمل المقدم في هذا البحث *استدعاء بالاسم* و*استدعاء بالقيمة* الموناد. في سياق غير موناد، يتحقق هدف مماثل من خلال حساب *call-by-push-value*. الحساب أكثر دقة ويفصل بشكل صارم بين *القيم* و*الحسابات*. باستخدام هذه الآليات، من الممكن ترميز كل من *استدعاء بالاسم* و*استدعاء بالقيمة*. قد يكون من المثير للاهتمام النظر فيما إذا كان يمكن ترميز حساباتنا المعلمة على استراتيجية التقييم في *call-by-push-value*.

---

### Translation Notes

- **Key topics:** Monads with aliasing operations, comonads in functional programming, evaluation strategies research
- **Citations:** Wadler, Orc monad, Ariola and Felleisen, Curry-Howard correspondence, call-by-push-value calculus
- **Related concepts:** `share` operation, `eagerly` combinator, applicative functors, arrows, MonadPlus
- **Special handling:**
  - Technical term names kept in English where appropriate (Orc, HNF, Ignore, MonadPlus, Curry-Howard)
  - "call-by-push-value" kept in English as it's a specific calculus name

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.85
- **Overall section score:** 0.86
