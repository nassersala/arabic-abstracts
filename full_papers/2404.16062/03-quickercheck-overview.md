# Section 3: QuickerCheck
## القسم 3: QuickerCheck

**Section:** quickercheck-overview
**Translation Quality:** 0.86
**Glossary Terms Used:** multi-core, property testing, I/O operations, thread-safety, race conditions, compiler testing

---

### English Version

## System F

The authors demonstrate testing a System F implementation's subject reduction property (types shouldn't change after evaluation). With sequential QuickCheck, users invoke `quickCheck prop_Preservation`. With QuickerCheck on a multi-core system, they call `quickCheckPar prop_Preservation` instead, producing identical output while distributing work across cores.

## Compiler Testing

Testing compilers requires I/O operations like invoking external processes. Metamorphic testing compares outputs between original and mutated programs. The naive approach creates race conditions when multiple threads write identical filenames.

Solutions include using temporary directories per worker or pipe-based approaches avoiding the filesystem entirely. QuickerCheck requires: (1) ensuring thread-safety for I/O properties, (2) compiling with threading options, (3) using `quickCheckPar` instead of `quickCheck`.

---

### النسخة العربية

## System F

يوضح المؤلفون اختبار خاصية الحفاظ على النوع في تطبيق System F (لا يجب أن تتغير الأنواع بعد التقييم). مع QuickCheck التسلسلي، يستدعي المستخدمون `quickCheck prop_Preservation`. مع QuickerCheck على نظام متعدد النوى، يستدعون بدلاً من ذلك `quickCheckPar prop_Preservation`، مما ينتج مخرجات متطابقة بينما يوزع العمل عبر النوى.

## اختبار المترجمات

يتطلب اختبار المترجمات عمليات إدخال/إخراج مثل استدعاء عمليات خارجية. يقارن الاختبار المتحول المخرجات بين البرامج الأصلية والبرامج المتحولة. ينشئ النهج الساذج ظروف تنافس عندما تكتب خيوط متعددة أسماء ملفات متطابقة.

تشمل الحلول استخدام دلائل مؤقتة لكل عامل أو نُهُج قائمة على الأنابيب تتجنب نظام الملفات تماماً. يتطلب QuickerCheck: (1) ضمان أمان الخيوط لخصائص الإدخال/إخراج، (2) الترجمة بخيارات الخيوط، (3) استخدام `quickCheckPar` بدلاً من `quickCheck`.

---

### Translation Notes

- **Key terms introduced:**
  - System F = System F (kept as proper noun for type system)
  - Subject reduction property = خاصية الحفاظ على النوع
  - Type evaluation = التقييم (في سياق الأنواع)
  - Multi-core system = نظام متعدد النوى
  - Distributing work across cores = توزيع العمل عبر النوى
  - Compiler testing = اختبار المترجمات
  - I/O operations = عمليات إدخال/إخراج
  - External processes = عمليات خارجية
  - Metamorphic testing = الاختبار المتحول
  - Mutated programs = البرامج المتحولة
  - Naive approach = النهج الساذج
  - Race conditions = ظروف تنافس
  - Identical filenames = أسماء ملفات متطابقة
  - Temporary directories = دلائل مؤقتة
  - Per worker = لكل عامل
  - Pipe-based approaches = نُهُج قائمة على الأنابيب
  - Filesystem = نظام الملفات
  - Threading options = خيارات الخيوط

- **Code elements:**
  - Preserved function names in English: `quickCheck`, `quickCheckPar`, `prop_Preservation`
  - These are API calls and should remain in original form

- **Technical concepts:**
  - Subject reduction in type systems
  - Metamorphic testing for compilers
  - Thread-safety challenges in parallel testing
  - Solutions for avoiding race conditions

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86

### Back-Translation Check

**System F**
The authors demonstrate testing the type preservation property in a System F implementation (types should not change after evaluation). With sequential QuickCheck, users invoke `quickCheck prop_Preservation`. With QuickerCheck on a multi-core system, they instead invoke `quickCheckPar prop_Preservation`, producing identical outputs while distributing work across cores.

**Compiler Testing**
Compiler testing requires I/O operations such as invoking external processes. Metamorphic testing compares outputs between original programs and mutated programs. The naive approach creates race conditions when multiple threads write identical filenames.

Solutions include using temporary directories per worker or pipe-based approaches that avoid the filesystem entirely. QuickerCheck requires: (1) ensuring thread-safety for I/O properties, (2) compilation with threading options, (3) using `quickCheckPar` instead of `quickCheck`.

✓ Back-translation preserves technical accuracy and key concepts.
