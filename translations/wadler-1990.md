---
# Comprehending Monads
## استيعاب الموناد

**Paper ID:** wadler-1990
**Author:** Philip Wadler
**Year:** 1990
**Published in:** Proceedings of the 1990 ACM Conference on LISP and Functional Programming, pp. 61-78
**Later published in:** Mathematical Structures in Computer Science, Vol. 2, Issue 4, 1992, pp. 461-493
**Translation Quality:** 0.91
**Glossary Terms Used:** monad, functional programming, list comprehension, category theory, state, exception handling, parser, continuation

### English Abstract
Category theorists invented monads in the 1960's to express concisely certain aspects of universal algebra. Functional programmers invented list comprehensions in the 1970's to express concisely certain programs involving lists. This paper shows how list comprehensions may be generalised to an arbitrary monad, and how the resulting programming feature can express concisely in a pure functional language some programs that manipulate state, handle exceptions, parse text, or invoke continuations. A new solution to the old problem of destructive array update is also presented. No knowledge of category theory is assumed.

### الملخص العربي
ابتكر منظرو الفئات الموناد في الستينيات للتعبير بإيجاز عن جوانب معينة من الجبر الشامل. ابتكر مبرمجو اللغات الوظيفية استيعابات القوائم في السبعينيات للتعبير بإيجاز عن برامج معينة تتضمن القوائم. توضح هذه الورقة كيف يمكن تعميم استيعابات القوائم إلى موناد تعسفي، وكيف يمكن للخاصية البرمجية الناتجة أن تعبر بإيجاز في لغة وظيفية نقية عن بعض البرامج التي تتعامل مع الحالة، أو تعالج الاستثناءات، أو تحلل النصوص، أو تستدعي الاستمرارات. يُقدم أيضاً حل جديد لمشكلة قديمة تتعلق بتحديث المصفوفات المدمر. لا يُفترض أي معرفة بنظرية الفئات.

### Back-Translation (Validation)
Category theorists invented monads in the sixties to express concisely certain aspects of universal algebra. Functional language programmers invented list comprehensions in the seventies to express concisely certain programs involving lists. This paper shows how list comprehensions can be generalized to an arbitrary monad, and how the resulting programming feature can express concisely in a pure functional language some programs that deal with state, handle exceptions, parse texts, or invoke continuations. A new solution is also presented for an old problem related to destructive array updates. No knowledge of category theory is assumed.

### Translation Metrics
- Iterations: 1
- Final Score: 0.91
- Quality: High
- Semantic Equivalence: Excellent
- Technical Accuracy: Excellent
- Completeness: Complete
- Coherence: Excellent

### Notes
This influential paper connects monads from category theory with the familiar concept of list comprehensions, showing how to generalize comprehensions to arbitrary monads. It demonstrates that monadic notation provides an elegant way to express effectful computations in pure functional languages. The paper made monads accessible to functional programmers by avoiding categorical jargon and focusing on practical programming applications. It also introduced a monadic solution to the array update problem.
---
