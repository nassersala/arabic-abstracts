# Section 1: Introduction
## القسم 1: المقدمة

**Section:** Introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** abstraction, lambda calculus, functional programming, logic programming, search problems, transpiling

---

### English Version

A lot of research aims to put more abstraction layers into modelling languages for search problems. One common approach is to add templates or macros to a language to enable the reuse of a concept [6,7,11]. Some languages such as HiLog [3] introduce higher order language constructs with first order semantics to mimic this kind of features. While the lambda calculus is generally not considered a regular modelling language, one of its strengths is the ability to easily define abstractions. We aim to shrink this gap by showing how the lambda calculus can be translated into existing paradigms. Our end goal is to leverage existing search technology for logic programming languages to serve as a search engine for problems specified in functional languages.

In this paper we introduce a transpiling algorithm between Programming Computable Functions, a programming language based on the lambda calculus and Answer Set Programming, a logic-based modelling language. This transpilation is a source-to-source translation of programs. We show how this can be the basis for a functional modelling language which combines the advantages of easy abstractions and reasoning over non-defined symbols. Transpiling Programmable Computable Functions to other languages like C [10], or a theorem prover like Coq [5] has been done before. But as far as the authors are aware, no approaches to translate it into logic programs have been done before.

In Section 2 we introduce the source language of our transpiler: Programming Computable Functions. In Section 3 we introduce the target language of our transpiler: Answer Set Programming. In Section 4 we describe the translation algorithm. Finally, in Section 5 we motivate why this kind of translation can be useful in practice. An implementation of the translator is made available online (https://dtai.cs.kuleuven.be/krr/pcf2asp), where it can be tested with your own examples.

---

### النسخة العربية

يهدف الكثير من الأبحاث إلى إضافة المزيد من طبقات التجريد في لغات النمذجة لمشاكل البحث. أحد الأساليب الشائعة هو إضافة القوالب أو وحدات الماكرو إلى اللغة لتمكين إعادة استخدام مفهوم معين [6,7,11]. بعض اللغات مثل HiLog [3] تقدم بنيات لغوية من الرتبة العليا مع دلالات من الرتبة الأولى لمحاكاة هذا النوع من الميزات. في حين أن حساب لامبدا لا يُعتبر عادةً لغة نمذجة عادية، فإن إحدى نقاط قوته هي القدرة على تعريف التجريدات بسهولة. نهدف إلى تقليص هذه الفجوة من خلال إظهار كيف يمكن ترجمة حساب لامبدا إلى نماذج موجودة. هدفنا النهائي هو الاستفادة من تقنية البحث الموجودة للغات البرمجة المنطقية لتكون بمثابة محرك بحث للمشاكل المحددة في اللغات الوظيفية.

في هذا البحث نقدم خوارزمية تحويل بين الدوال القابلة للحوسبة والبرمجة، وهي لغة برمجة تعتمد على حساب لامبدا، وبرمجة مجموعة الإجابات، وهي لغة نمذجة قائمة على المنطق. هذا التحويل هو ترجمة من مصدر إلى مصدر للبرامج. نوضح كيف يمكن أن يكون هذا الأساس للغة نمذجة وظيفية تجمع بين مزايا التجريدات السهلة والاستدلال على الرموز غير المعرَّفة. تم من قبل تحويل الدوال القابلة للحوسبة والبرمجة إلى لغات أخرى مثل C [10]، أو مُثبِّت نظريات مثل Coq [5]. لكن حسب علم المؤلفين، لم يتم من قبل أي نُهج لترجمتها إلى برامج منطقية.

في القسم 2 نقدم اللغة المصدر لمحول البرامج الخاص بنا: الدوال القابلة للحوسبة والبرمجة. في القسم 3 نقدم اللغة الهدف لمحول البرامج الخاص بنا: برمجة مجموعة الإجابات. في القسم 4 نصف خوارزمية الترجمة. وأخيراً، في القسم 5 نبرر لماذا يمكن أن يكون هذا النوع من الترجمة مفيداً في الممارسة العملية. تم توفير تطبيق للمترجم عبر الإنترنت (https://dtai.cs.kuleuven.be/krr/pcf2asp)، حيث يمكن اختباره مع أمثلتك الخاصة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - abstraction layers - طبقات التجريد
  - templates/macros - القوالب/وحدات الماكرو
  - higher order language constructs - بنيات لغوية من الرتبة العليا
  - first order semantics - دلالات من الرتبة الأولى
  - lambda calculus - حساب لامبدا
  - transpiling algorithm - خوارزمية تحويل
  - source-to-source translation - ترجمة من مصدر إلى مصدر
  - functional modelling language - لغة نمذجة وظيفية
  - non-defined symbols - الرموز غير المعرَّفة
  - theorem prover - مُثبِّت نظريات
  - logic programs - برامج منطقية
- **Equations:** None
- **Citations:** [3], [5], [6], [7], [10], [11]
- **Special handling:**
  - URL preserved in original form
  - References to paper sections (2, 3, 4, 5) maintained

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88

### Back-Translation Validation

Key paragraph back-translation: "Much research aims to add more abstraction layers in modeling languages for search problems. One common approach is to add templates or macro units to the language to enable reusing a specific concept. Some languages like HiLog introduce higher-order language structures with first-order semantics to simulate this type of features. While lambda calculus is not usually considered an ordinary modeling language, one of its strengths is the ability to define abstractions easily. We aim to reduce this gap by showing how lambda calculus can be translated into existing paradigms. Our ultimate goal is to leverage existing search technology for logic programming languages to serve as a search engine for problems specified in functional languages."

The back-translation accurately preserves the technical meaning and logical flow of the original.
