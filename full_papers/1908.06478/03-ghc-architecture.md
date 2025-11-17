# Section 3: GHC Architecture
## القسم 3: معمارية GHC

**Section:** ghc-architecture
**Translation Quality:** 0.87
**Glossary Terms Used:** compiler, compilation pipeline, intermediate representation, optimization, type system, functional programming

---

### English Version

In this section, we provide a basic summary of the compilation pipeline used within GHC, depicted in Figure 1. The original Haskell code is first parsed into an abstract syntax tree, which is then type-checked. It is then desugared and translated to GHC Core, a lazy functional language based on System F. At this point, the compiler will apply most of its code optimizations. Afterwards, the code is translated to STG, a subset of GHC Core minus certain type information which is not needed anymore after this point. It is then translated into a low-level imperative language called Cmm, before one of several different backends can be used to translate it into Assembler and, finally, the finished binary.

**Figure 1:** Basic overview of the GHC compilation pipeline. Based on a graphic in [4].

```
Parse tree → Desugar → Core → STGify → STG → CodeGen → Cmm → [LLVM backend / C backend / NCG]
                                                                     ↓           ↓         ↓
                                                                  LLVM IR      C       Assembly
                                                                     ↓           ↓
                                                                   LLVM        GCC
                                                                     ↓
                                                                 Assembly
```

For our analysis, we will be looking at GHC Core, as it is the most similar to the JVFH language. Additionally, the other intermediate languages used by GHC Core have a number of drawbacks that make them unsuitable for our analysis:

The syntax of the parse tree is a considerably more redundant than that of GHC Core; In fact, the type used in GHC to represent a Core expression consists of only 10 different constructors [1], while the Haskell syntax is represented by around 50 different constructors [2]. While it is possible to implement a type system on the parse tree, it is tedious and does not provide any advantage for our purpose. Additionally, most of the compiler optimizations are applied only after the translation to GHC Core. It is preferable to analyze this optimized code, as it is more representative of the final compiled binary.

The STG code is unsuitable for our purpose, because it lacks certain type information such as type abstraction and application. As GHC Core is an extension to System F and STG is a subset of Core missing type information, we assume that the undecidability of type inference in System F [15] also applies to STG; This is not an issue for the compiler, as type checking has already completed at this point and the compiler does not need the discarded type information anymore. However, as our analysis is based on a type system, this information is essential to us in fully supporting the language, particularly polymorphism. While our current implementation does not support polymorphism yet and therefore may also work on STG, choosing STG over Core would severely hamper any future work on supporting the full language.

Finally, Cmm and any of the languages used thereafter are strict imperative languages. Thus, they are unsuitable for an adaption of the JVFH type system, which is designed around a lazy functional language. Analyzing these languages may be feasible, but this would require a completely different approach.

The GHC compiler has an API for custom plugins that can be used to interact with the compilation pipeline. Plugins can be implemented by writing a Haskell module that exports variables with specific names and specific types, and they can be used by calling GHC with specific command line arguments. [3, 14]

---

### النسخة العربية

في هذا القسم، نقدم ملخصاً أساسياً لخط الترجمة المستخدم داخل GHC، الموضح في الشكل 1. يتم أولاً تحليل شفرة Haskell الأصلية إلى شجرة صياغة تجريدية، والتي يتم بعد ذلك فحص أنواعها. ثم يتم إزالة السكر منها وترجمتها إلى GHC Core، وهي لغة وظيفية كسولة مبنية على System F. في هذه المرحلة، سيطبق المترجم معظم تحسينات الشفرة الخاصة به. بعد ذلك، يتم ترجمة الشفرة إلى STG، وهي مجموعة فرعية من GHC Core ناقص معلومات أنواع معينة لم تعد مطلوبة بعد هذه النقطة. ثم يتم ترجمتها إلى لغة أمرية منخفضة المستوى تسمى Cmm، قبل أن يتم استخدام إحدى عدة واجهات خلفية مختلفة لترجمتها إلى المُجمِّع (Assembler) وأخيراً، الملف الثنائي النهائي.

**الشكل 1:** نظرة عامة أساسية على خط ترجمة GHC. بناءً على رسم في [4].

```
شجرة التحليل → إزالة السكر → Core → STGify → STG → CodeGen → Cmm → [LLVM backend / C backend / NCG]
                                                                              ↓           ↓         ↓
                                                                          LLVM IR      C       Assembly
                                                                              ↓           ↓
                                                                            LLVM        GCC
                                                                              ↓
                                                                          Assembly
```

بالنسبة لتحليلنا، سننظر في GHC Core، حيث إنها الأكثر تشابهاً مع لغة JVFH. بالإضافة إلى ذلك، فإن اللغات الوسيطة الأخرى المستخدمة بواسطة GHC Core لها عدد من العيوب التي تجعلها غير مناسبة لتحليلنا:

صياغة شجرة التحليل أكثر تكراراً بكثير من تلك الخاصة بـ GHC Core؛ في الواقع، يتكون النوع المستخدم في GHC لتمثيل تعبير Core من 10 منشئات مختلفة فقط [1]، بينما يتم تمثيل صياغة Haskell بحوالي 50 منشئاً مختلفاً [2]. في حين أنه من الممكن تنفيذ نظام أنواع على شجرة التحليل، إلا أن ذلك مُمِل ولا يوفر أي ميزة لهدفنا. بالإضافة إلى ذلك، يتم تطبيق معظم تحسينات المترجم فقط بعد الترجمة إلى GHC Core. من الأفضل تحليل هذه الشفرة المُحسَّنة، حيث إنها أكثر تمثيلاً للملف الثنائي المترجم النهائي.

شفرة STG غير مناسبة لهدفنا، لأنها تفتقر إلى معلومات أنواع معينة مثل تجريد الأنواع وتطبيقها. نظراً لأن GHC Core هو امتداد لـ System F وأن STG هي مجموعة فرعية من Core تفتقد معلومات الأنواع، نفترض أن عدم القابلية للبت في استنتاج الأنواع في System F [15] ينطبق أيضاً على STG؛ هذا ليس مشكلة للمترجم، حيث تم بالفعل إكمال فحص الأنواع في هذه المرحلة ولا يحتاج المترجم إلى معلومات الأنواع المُهمَلة بعد الآن. ومع ذلك، نظراً لأن تحليلنا يعتمد على نظام أنواع، فإن هذه المعلومات ضرورية لنا في دعم اللغة بالكامل، لا سيما تعدد الأشكال. بينما لا يدعم تطبيقنا الحالي تعدد الأشكال حتى الآن وبالتالي قد يعمل أيضاً على STG، فإن اختيار STG على Core سيعيق بشدة أي عمل مستقبلي على دعم اللغة الكاملة.

أخيراً، Cmm وأي من اللغات المستخدمة بعد ذلك هي لغات أمرية صارمة. وبالتالي، فهي غير مناسبة لتكييف نظام أنواع JVFH، الذي صُمم حول لغة وظيفية كسولة. قد يكون تحليل هذه اللغات ممكناً، ولكن ذلك سيتطلب نهجاً مختلفاً تماماً.

يحتوي مترجم GHC على واجهة برمجة تطبيقات للإضافات المخصصة التي يمكن استخدامها للتفاعل مع خط الترجمة. يمكن تنفيذ الإضافات من خلال كتابة وحدة Haskell تُصدّر متغيرات بأسماء محددة وأنواع محددة، ويمكن استخدامها عن طريق استدعاء GHC مع معاملات سطر أوامر محددة. [3, 14]

---

### Translation Notes

- **Figures referenced:** Figure 1 (GHC compilation pipeline diagram)
- **Key terms introduced:**
  - abstract syntax tree (شجرة صياغة تجريدية)
  - type-checked (فحص الأنواع)
  - desugared (إزالة السكر)
  - System F (نظام F)
  - code optimizations (تحسينات الشفرة)
  - low-level imperative language (لغة أمرية منخفضة المستوى)
  - assembler (المُجمِّع)
  - binary (ملف ثنائي)
  - constructors (منشئات)
  - type abstraction (تجريد الأنواع)
  - type inference (استنتاج الأنواع)
  - undecidability (عدم القابلية للبت)
  - polymorphism (تعدد الأشكال)
  - plugin API (واجهة برمجة التطبيقات للإضافات)
- **Equations:** None
- **Citations:** [1, 2, 3, 4, 14, 15]
- **Special handling:**
  - Technical terms like "GHC Core", "STG", "Cmm", "LLVM" kept in English as they are proper names
  - "desugaring" translated as "إزالة السكر" (removing sugar) - a standard translation in Arabic CS literature

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-Translation (First & Last Paragraphs)

**First paragraph:** In this section, we provide a basic summary of the compilation pipeline used within GHC, shown in Figure 1. First, the original Haskell code is parsed into an abstract syntax tree, which is then type-checked. Then it is desugared and translated to GHC Core, a lazy functional language built on System F. At this stage, the compiler will apply most of its code optimizations. After that, the code is translated to STG, a subset of GHC Core minus certain type information that is no longer needed after this point. Then it is translated into a low-level imperative language called Cmm, before one of several different backends is used to translate it to Assembler and finally, the final binary file.

**Last paragraph:** The GHC compiler has an API for custom plugins that can be used to interact with the compilation pipeline. Plugins can be implemented by writing a Haskell module that exports variables with specific names and specific types, and they can be used by calling GHC with specific command line parameters. [3, 14]
