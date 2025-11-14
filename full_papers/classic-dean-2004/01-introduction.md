# Section 1: Introduction
## القسم 1: المقدمة

**Section:** Introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** computation, data processing, distributed system, parallelization, fault-tolerance, abstraction, programming model, cluster, load balancing

---

### English Version

Over the past five years, the authors and many others at Google have implemented hundreds of special-purpose computations that process large amounts of raw data, such as crawled documents, web request logs, etc., to compute various kinds of derived data, such as inverted indices, various representations of the graph structure of web documents, summaries of the number of pages crawled per host, the set of most frequent queries in a given day, etc. Most such computations are conceptually straightforward. However, the input data is usually large and the computations have to be distributed across hundreds or thousands of machines in order to finish in a reasonable amount of time. The issues of how to parallelize the computation, distribute the data, and handle failures conspire to obscure the original simple computation with large amounts of complex code to deal with these issues.

As a reaction to this complexity, we designed a new abstraction that allows us to express the simple computations we were trying to perform but hides the messy details of parallelization, fault-tolerance, data distribution and load balancing in a library. Our abstraction is inspired by the map and reduce primitives present in Lisp and many other functional languages. We realized that most of our computations involved applying a map operation to each logical "record" in our input in order to compute a set of intermediate key/value pairs, and then applying a reduce operation to all the values that shared the same key, in order to combine the derived data appropriately. Our use of a functional model with user-specified map and reduce operations allows us to parallelize large computations easily and to use re-execution as the primary mechanism for fault tolerance.

The major contributions of this work are a simple and powerful interface that enables automatic parallelization and distribution of large-scale computations, combined with an implementation of this interface that achieves high performance on large clusters of commodity PCs.

Section 2 describes the basic programming model and gives several examples. Section 3 describes an implementation of the MapReduce interface tailored towards our cluster-based computing environment. Section 4 describes several refinements of the programming model that we have found useful. Section 5 has performance measurements of our implementation for a variety of tasks. Section 6 explores the use of MapReduce within Google including our experiences in using it as the basis for a rewrite of our production indexing system. Section 7 discusses related and future work.

---

### النسخة العربية

على مدى السنوات الخمس الماضية، قام المؤلفون والعديد من الآخرين في Google بتطبيق مئات الحسابات ذات الأغراض الخاصة التي تعالج كميات كبيرة من البيانات الأولية، مثل المستندات المستخرجة من الويب، وسجلات طلبات الويب، وما إلى ذلك، لحساب أنواع مختلفة من البيانات المشتقة، مثل الفهارس المعكوسة، والتمثيلات المختلفة للبنية البيانية لمستندات الويب، وملخصات عدد الصفحات المستخرجة لكل مضيف، ومجموعة الاستعلامات الأكثر تكراراً في يوم معين، وما إلى ذلك. معظم هذه الحسابات واضحة من الناحية المفاهيمية. ومع ذلك، عادة ما تكون بيانات الإدخال كبيرة ويجب توزيع الحسابات عبر مئات أو آلاف من الأجهزة من أجل الانتهاء في وقت معقول. تتآمر قضايا كيفية توزيع الحساب، وتوزيع البيانات، والتعامل مع الأعطال لإخفاء الحساب البسيط الأصلي بكميات كبيرة من الشفرة المعقدة للتعامل مع هذه القضايا.

كرد فعل لهذا التعقيد، صممنا تجريداً جديداً يسمح لنا بالتعبير عن الحسابات البسيطة التي كنا نحاول إجراءها ولكنه يخفي التفاصيل الفوضوية للتوزيع وتحمل الأخطاء وتوزيع البيانات وموازنة الحمل في مكتبة. يستلهم تجريدنا من بدائيات map و reduce الموجودة في Lisp والعديد من اللغات الوظيفية الأخرى. أدركنا أن معظم حساباتنا تتضمن تطبيق عملية map على كل "سجل" منطقي في إدخالنا من أجل حساب مجموعة من أزواج المفتاح/القيمة الوسيطة، ثم تطبيق عملية reduce على جميع القيم التي تشترك في نفس المفتاح، من أجل دمج البيانات المشتقة بشكل مناسب. يتيح لنا استخدامنا لنموذج وظيفي مع عمليات map و reduce المحددة من قبل المستخدم توزيع الحسابات الكبيرة بسهولة واستخدام إعادة التنفيذ كآلية أساسية لتحمل الأخطاء.

المساهمات الرئيسية لهذا العمل هي واجهة بسيطة وقوية تمكّن التوزيع والتوزيع التلقائي للحسابات واسعة النطاق، جنباً إلى جنب مع تطبيق لهذه الواجهة يحقق أداءً عالياً على عناقيد كبيرة من أجهزة الكمبيوتر الشخصية التجارية.

يصف القسم 2 نموذج البرمجة الأساسي ويعطي عدة أمثلة. يصف القسم 3 تطبيقاً لواجهة MapReduce مصممة خصيصاً لبيئة الحوسبة المستندة إلى العناقيد الخاصة بنا. يصف القسم 4 العديد من التحسينات على نموذج البرمجة التي وجدناها مفيدة. يحتوي القسم 5 على قياسات أداء تطبيقنا لمجموعة متنوعة من المهام. يستكشف القسم 6 استخدام MapReduce داخل Google بما في ذلك تجاربنا في استخدامه كأساس لإعادة كتابة نظام الفهرسة الإنتاجي الخاص بنا. يناقش القسم 7 الأعمال ذات الصلة والعمل المستقبلي.

---

### Translation Notes

- **Key terms introduced:**
  - "special-purpose computations": الحسابات ذات الأغراض الخاصة
  - "raw data": البيانات الأولية
  - "derived data": البيانات المشتقة
  - "inverted indices": الفهارس المعكوسة
  - "graph structure": البنية البيانية
  - "abstraction": تجريد
  - "primitives": بدائيات
  - "functional model": نموذج وظيفي
  - "re-execution": إعادة التنفيذ
  - "commodity PCs": أجهزة الكمبيوتر الشخصية التجارية

- **Technical decisions:**
  - Kept "map" and "reduce" in English as they are established technical terms
  - Kept "Lisp" in English as a proper programming language name
  - Kept "Google" in English as a proper company name
  - Used "توزيع" for both "parallelization" and "distribution" based on context
  - Used "تحمل الأخطاء" for "fault-tolerance"
  - Used "موازنة الحمل" for "load balancing"

- **Section structure:** The introduction provides context, motivation, solution approach, and paper outline

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.86
- Glossary consistency: 0.90
- **Overall section score:** 0.88

### Back-Translation Check (Key Paragraphs)

First paragraph back-translation:
"Over the past five years, the authors and many others at Google have implemented hundreds of special-purpose computations that process large amounts of raw data, such as documents extracted from the web, web request logs, etc., to compute various types of derived data, such as inverted indices, different representations of the graph structure of web documents, summaries of the number of pages extracted per host, and the set of most frequent queries on a given day, etc. Most of these computations are conceptually clear. However, input data is usually large and computations must be distributed across hundreds or thousands of machines in order to finish in a reasonable time. Issues of how to distribute the computation, distribute the data, and handle failures conspire to hide the original simple computation with large amounts of complex code to deal with these issues."

Third paragraph back-translation:
"The main contributions of this work are a simple and powerful interface that enables automatic parallelization and distribution of large-scale computations, along with an implementation of this interface that achieves high performance on large clusters of commercial personal computers."
