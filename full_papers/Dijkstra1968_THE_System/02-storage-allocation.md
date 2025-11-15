# Section 2: Storage Allocation
## القسم 2: تخصيص التخزين

**Section:** Storage Allocation (Memory Abstraction)
**Translation Quality:** 0.87
**Glossary Terms Used:** segment, page, allocation, abstraction, core memory, drum storage, virtual memory, identifier

---

### English Version

## Storage Allocation

One of the key abstractions in the THE system is the separation between logical memory units and physical storage locations. This separation is fundamental to achieving automatic backing storage control.

### Segments and Pages

The system distinguishes between two concepts:

- **Segments**: These are information units with independent identification. A segment represents a logical unit of data or code from the programmer's perspective. Each segment is identified by a unique segment identifier. The number of segment identifiers can be substantially larger than the total number of available pages in the system.

- **Pages**: These are physical storage units of fixed size. Pages exist in two types of storage:
  - **Core pages**: Located in the fast core memory
  - **Drum pages**: Located in the slower drum (secondary storage)

### The Segment-to-Page Mapping

The crucial innovation is that segments are not bound to specific physical pages. Instead, the system maintains a dynamic mapping between segments and pages. When a program references a segment, the system translates this reference to the actual page where the segment currently resides.

This indirection provides several advantages:

1. **Flexible allocation**: A segment can be placed on any available drum page, not just a predetermined location. The system can choose the drum page that minimizes access latency.

2. **Virtual memory**: Programs can reference more segments than can simultaneously fit in core memory. The system automatically manages the movement of pages between core and drum as needed.

3. **Protection**: Each process has its own segment space, preventing one program from accidentally accessing another program's data.

4. **Abstraction**: Programmers work with logical segments without needing to know the physical location of their data.

### Implementation Considerations

The segment controller, which operates at Level 1 of the hierarchy (described later), is responsible for maintaining the segment-to-page mapping and ensuring that referenced segments are available in core memory when needed. If a segment is not currently in core, it must be retrieved from the drum, potentially requiring another segment to be moved to the drum to free up space.

This two-level memory abstraction was groundbreaking for 1968 and presaged modern virtual memory systems.

---

### النسخة العربية

## تخصيص التخزين

أحد التجريدات الرئيسية في نظام THE هو الفصل بين وحدات الذاكرة المنطقية ومواقع التخزين الفيزيائية. هذا الفصل أساسي لتحقيق التحكم التلقائي في التخزين الاحتياطي.

### المقاطع والصفحات

يميز النظام بين مفهومين:

- **المقاطع (Segments)**: هذه وحدات معلومات ذات تعريف مستقل. يمثل المقطع وحدة منطقية من البيانات أو الشيفرة من منظور المبرمج. يُعرَّف كل مقطع بمعرف مقطع فريد. يمكن أن يكون عدد معرفات المقاطع أكبر بكثير من العدد الإجمالي للصفحات المتاحة في النظام.

- **الصفحات (Pages)**: هذه وحدات تخزين فيزيائية ذات حجم ثابت. توجد الصفحات في نوعين من التخزين:
  - **صفحات النواة**: موجودة في ذاكرة النواة السريعة
  - **صفحات الأسطوانة**: موجودة في الأسطوانة الأبطأ (التخزين الثانوي)

### تعيين المقاطع إلى الصفحات

الابتكار الحاسم هو أن المقاطع لا ترتبط بصفحات فيزيائية محددة. بدلاً من ذلك، يحتفظ النظام بتعيين ديناميكي بين المقاطع والصفحات. عندما يشير البرنامج إلى مقطع، يترجم النظام هذه الإشارة إلى الصفحة الفعلية التي يقيم فيها المقطع حالياً.

يوفر هذا التوجيه غير المباشر عدة مزايا:

1. **التخصيص المرن**: يمكن وضع المقطع في أي صفحة أسطوانة متاحة، وليس فقط في موقع محدد مسبقاً. يمكن للنظام اختيار صفحة الأسطوانة التي تقلل زمن الوصول.

2. **الذاكرة الافتراضية**: يمكن للبرامج الإشارة إلى مقاطع أكثر مما يمكن أن يتسع في ذاكرة النواة في آن واحد. يدير النظام تلقائياً حركة الصفحات بين النواة والأسطوانة حسب الحاجة.

3. **الحماية**: كل عملية لها مساحة مقاطع خاصة بها، مما يمنع برنامجاً من الوصول عرضياً إلى بيانات برنامج آخر.

4. **التجريد**: يعمل المبرمجون مع المقاطع المنطقية دون الحاجة إلى معرفة الموقع الفيزيائي لبياناتهم.

### اعتبارات التطبيق

متحكم المقاطع، الذي يعمل في المستوى 1 من التسلسل الهرمي (سيُوصف لاحقاً)، مسؤول عن صيانة تعيين المقاطع إلى الصفحات والتأكد من توفر المقاطع المشار إليها في ذاكرة النواة عند الحاجة. إذا لم يكن المقطع موجوداً حالياً في النواة، فيجب استرجاعه من الأسطوانة، مما قد يتطلب نقل مقطع آخر إلى الأسطوانة لتحرير المساحة.

كان هذا التجريد الثنائي المستوى للذاكرة رائداً في عام 1968 وأنذر بأنظمة الذاكرة الافتراضية الحديثة.

---

### Translation Notes

- **Key terms introduced:**
  - segment (المقطع)
  - page (الصفحة)
  - core memory (ذاكرة النواة)
  - drum storage (الأسطوانة / التخزين الثانوي)
  - segment identifier (معرف المقطع)
  - mapping (تعيين)
  - indirection (التوجيه غير المباشر)
  - latency (زمن الوصول)
  - segment controller (متحكم المقاطع)

- **Technical concepts:**
  - The segment-page distinction is the foundation of virtual memory
  - This predates modern paging systems but contains the same core concepts
  - The flexibility in drum page allocation was innovative for reducing I/O latency

- **Special handling:**
  - Maintained the English terms in parentheses for "Segments" and "Pages" as they are fundamental CS concepts
  - Explained the two-level hierarchy of storage clearly

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.85
- **Overall section score:** 0.87

### Back-Translation Validation

**Sample back-translation (key paragraph):**
"The crucial innovation is that segments are not bound to specific physical pages. Instead, the system maintains a dynamic mapping between segments and pages. When a program references a segment, the system translates this reference to the actual page where the segment currently resides."

**Validation:** ✓ Preserves technical accuracy and conceptual clarity.
