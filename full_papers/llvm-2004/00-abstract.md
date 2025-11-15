---
# LLVM: A Compilation Framework for Lifelong Program Analysis & Transformation
## LLVM: إطار عمل للترجمة من أجل التحليل والتحويل مدى حياة البرنامج

**Authors:** Chris Lattner, Vikram Adve
**Year:** 2004
**Publication:** International Symposium on Code Generation and Optimization (CGO 2004)
**Pages:** 75-86
**Translation Quality:** 0.91
**Glossary Terms Used:** compiler, framework, analysis, transformation, architecture, algorithm

### English Abstract
This paper describes LLVM (Low Level Virtual Machine), a compiler framework designed to support transparent, life-long program analysis and transformation for arbitrary programs, by providing high-level information to compiler transformations at compile-time, link-time, run-time, and in idle time between runs. LLVM defines a common, low-level code representation in Static Single Assignment (SSA) form, with several novel features: a simple, language-independent type-system that exposes the primitives commonly used to implement high-level language features; an instruction for typed address arithmetic; and a simple mechanism that can be used to implement the exception handling features of high-level languages (and setjmp/longjmp in C) uniformly and efficiently. The LLVM compiler framework and code representation together provide a combination of key capabilities that are important for practical, lifelong analysis and transformation of programs. To our knowledge, no existing compilation approach provides all these capabilities.

### الملخص العربي
تصف هذه الورقة LLVM (الآلة الافتراضية منخفضة المستوى)، وهو إطار عمل مترجم مصمم لدعم التحليل والتحويل الشفاف مدى الحياة للبرامج التعسفية، من خلال توفير معلومات عالية المستوى لتحويلات المترجم في وقت الترجمة ووقت الربط ووقت التشغيل وفي وقت الخمول بين التشغيلات. يحدد LLVM تمثيل كود مشترك منخفض المستوى في شكل الإسناد الثابت الفردي (SSA)، مع عدة ميزات جديدة: نظام أنواع بسيط مستقل عن اللغة يكشف العناصر الأولية المستخدمة عادةً لتنفيذ ميزات اللغات عالية المستوى؛ تعليمة للحساب الحسابي المكتوب للعناوين؛ وآلية بسيطة يمكن استخدامها لتنفيذ ميزات معالجة الاستثناءات للغات عالية المستوى (و setjmp/longjmp في لغة C) بشكل موحد وفعال. يوفر إطار عمل المترجم LLVM وتمثيل الكود معاً مجموعة من القدرات الرئيسية المهمة للتحليل والتحويل العملي مدى الحياة للبرامج. وفقاً لمعرفتنا، لا يوفر أي نهج ترجمة موجود جميع هذه القدرات.

### Back-Translation (Validation)
This paper describes LLVM (Low Level Virtual Machine), a compiler framework designed to support transparent, lifelong analysis and transformation for arbitrary programs, by providing high-level information to compiler transformations at compile-time, link-time, run-time, and in idle time between runs. LLVM defines a common low-level code representation in Static Single Assignment (SSA) form, with several novel features: a simple language-independent type system that exposes primitives commonly used to implement high-level language features; an instruction for typed address arithmetic; and a simple mechanism that can be used to implement exception handling features of high-level languages (and setjmp/longjmp in C) uniformly and efficiently. The LLVM compiler framework and code representation together provide a set of key capabilities important for practical lifelong analysis and transformation of programs. To our knowledge, no existing compilation approach provides all these capabilities.

### Translation Metrics
- Iterations: 1
- Final Score: 0.91
- Quality: High
- Key Technical Terms: compiler framework (إطار عمل مترجم), program analysis (تحليل البرنامج), transformation (تحويل), compile-time (وقت الترجمة), link-time (وقت الربط), run-time (وقت التشغيل), code representation (تمثيل الكود), Static Single Assignment (إسناد ثابت فردي), type-system (نظام الأنواع), exception handling (معالجة الاستثناءات)

### Historical Significance
LLVM, introduced in 2004, has become one of the most widely used compiler infrastructures in the world. It powers Clang (C/C++ compiler), Swift, Rust, and many other languages. Apple, Google, and countless other companies use LLVM in production. Its modular design and powerful optimization framework revolutionized compiler construction and made it possible to build high-quality compilers with significantly less effort than traditional approaches.
---
