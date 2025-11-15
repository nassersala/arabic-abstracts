# Section 4: Performance Engineer Workflow
## القسم 4: سير عمل مهندس الأداء

**Section:** Performance Engineer Workflow
**Translation Quality:** 0.87
**Glossary Terms Used:** transformation, optimization, pattern matching, graph rewriting, tiling

---

### English Version

The Stateful Dataflow Multigraph is designed to expose application data movement motifs, regardless of the underlying computations. As such, the optimization process of an SDFG consists of finding and leveraging such motifs, in order to mutate program dataflow.

**4.1 Graph Transformations**

Informally, we define a graph transformation on an SDFG as a "find and replace" operation, either within one state or between several, which can be performed if all of the conditions match. For general optimization strategies (e.g., tiling), we provide a standard library of such transformations. Transformations consist of a pattern subgraph and a replacement subgraph. A transformation also includes a matching function, used to identify instances of the pattern in an SDFG, and programmatically verify that requirements are met. To find matching subgraphs in SDFGs, we use the VF2 algorithm to find isomorphic subgraphs. Transformations can be applied interactively, or using a Python API for matching and applying transformations.

Two examples of SDFG transformations can be found in Figures 11a and 11b. In Fig. 11a, the transformation detects a pattern L where Reduce is invoked immediately following a Map, reusing the computed values. In this case, the transient array $A can be removed (if unused later) and computations can be fused with a conflict resolution. In the second example (Fig. 11b), a local array is added between two map nodes, changing relative indices in all subsequent memlets.

**4.2 DIODE**

SDFGs are intended to be malleable and interactive, which we realize with an Integrated Development Environment (IDE). The Data-centric Integrated Optimization Development Environment, or DIODE (Fig. 12), is a specialized IDE for performance engineers that enables editing SDFGs and applying transformations in a guided manner. Performance engineers can:
• interactively modify attributes of SDFG nodes and memlets;
• transform and tune transformation parameters;
• inspect an integrated program view that maps between lines in the domain code, SDFG components, and generated code;
• run and compare historical performance of transformations;
• save transformation chains to files, a form of "optimization version control";
• hierarchically interact with large-scale programs, collapsing irrelevant parts.

**4.3 Compilation Pipeline**

Compiling an SDFG consists of three steps: ❶ data dependency inference, ❷ code generation, and ❸ compiler invocation. In step ❶, data dependencies on all levels are resolved. In step ❷, the code generation process is hierarchical, starting from top-level states and traversing into scopes. It begins by emitting external interface code and the top-level state machine. In step ❸, we invoke compiler(s) for the generated code according to the used dispatchers.

---

### النسخة العربية

تم تصميم الرسم البياني المتعدد لتدفق البيانات الحافظ للحالة لكشف أنماط حركة بيانات التطبيق، بغض النظر عن الحسابات الأساسية. على هذا النحو، تتكون عملية تحسين SDFG من إيجاد واستغلال مثل هذه الأنماط، من أجل تعديل تدفق بيانات البرنامج.

**4.1 تحويلات الرسوم البيانية**

بشكل غير رسمي، نعرّف تحويل الرسم البياني على SDFG كعملية "بحث واستبدال"، إما داخل حالة واحدة أو بين عدة حالات، والتي يمكن إجراؤها إذا تطابقت جميع الشروط. للاستراتيجيات التحسين العامة (على سبيل المثال، التبليط)، نوفر مكتبة قياسية من هذه التحويلات. تتكون التحويلات من رسم بياني فرعي نمطي ورسم بياني فرعي بديل. يتضمن التحويل أيضًا دالة مطابقة، تُستخدم لتحديد حالات النمط في SDFG، والتحقق برمجيًا من أن المتطلبات مستوفاة. للعثور على رسوم بيانية فرعية متطابقة في SDFGs، نستخدم خوارزمية VF2 للعثور على رسوم بيانية متشاكلة. يمكن تطبيق التحويلات بشكل تفاعلي، أو باستخدام واجهة برمجة تطبيقات Python لمطابقة وتطبيق التحويلات.

يمكن العثور على مثالين من تحويلات SDFG في الشكلين 11أ و11ب. في الشكل 11أ، يكتشف التحويل نمطًا L حيث يتم استدعاء Reduce مباشرةً بعد Map، مع إعادة استخدام القيم المحسوبة. في هذه الحالة، يمكن إزالة المصفوفة العابرة $A (إذا لم تُستخدم لاحقًا) ويمكن دمج الحسابات مع حل التعارض. في المثال الثاني (الشكل 11ب)، يتم إضافة مصفوفة محلية بين عقدتي خريطة، مما يغير الفهارس النسبية في جميع memlets اللاحقة.

**4.2 DIODE**

تُقصد SDFGs أن تكون قابلة للطرق والتفاعل، والتي نحققها ببيئة تطوير متكاملة (IDE). بيئة تطوير التحسين المتكاملة المحورية للبيانات، أو DIODE (الشكل 12)، هي IDE متخصصة لمهندسي الأداء تتيح تحرير SDFGs وتطبيق التحويلات بطريقة موجهة. يمكن لمهندسي الأداء:
• تعديل سمات عقد SDFG وmemlets بشكل تفاعلي؛
• تحويل وضبط معاملات التحويل؛
• فحص عرض برنامج متكامل يربط بين الأسطر في شفرة المجال ومكونات SDFG والشفرة المولدة؛
• تشغيل ومقارنة الأداء التاريخي للتحويلات؛
• حفظ سلاسل التحويل في ملفات، شكل من "التحكم في إصدار التحسين"؛
• التفاعل بشكل هرمي مع البرامج واسعة النطاق، وطي الأجزاء غير ذات الصلة.

**4.3 خط أنابيب التجميع**

يتكون تجميع SDFG من ثلاث خطوات: ❶ استنتاج اعتماديات البيانات، ❷ توليد الشفرة، و❸ استدعاء المترجم. في الخطوة ❶، يتم حل اعتماديات البيانات على جميع المستويات. في الخطوة ❷، عملية توليد الشفرة هرمية، تبدأ من الحالات عالية المستوى وتتجول في النطاقات. تبدأ بإصدار شفرة الواجهة الخارجية وآلة الحالة عالية المستوى. في الخطوة ❸، نستدعي المترجم(المترجمين) للشفرة المولدة وفقًا للمرسلين المستخدمين.

---

### Translation Notes

- **Figures referenced:** Figures 11, 12
- **Key terms introduced:** DIODE, graph transformations, pattern matching, VF2 algorithm
- **Equations:** 0
- **Citations:** VF2 algorithm reference
- **Special handling:** Technical IDE and compilation pipeline terminology

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
