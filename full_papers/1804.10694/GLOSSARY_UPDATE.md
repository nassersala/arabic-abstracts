# New Terms for Glossary - Tiramisu Paper (1804.10694)

This document lists new technical terms from the Tiramisu paper that should be added to the main glossary.

## New Terms to Add

| English Term | Arabic Translation | Confidence | Usage Count | Notes |
|--------------|-------------------|------------|-------------|-------|
| array packing | تعبئة المصفوفات | 0.9 | 4 | Compiler optimization technique |
| register blocking | حجب السجلات | 0.9 | 3 | Optimization for cache locality |
| data prefetching | الجلب المسبق للبيانات | 0.9 | 3 | Memory optimization |
| memory coalescing | دمج الذاكرة | 0.9 | 2 | GPU memory access optimization (already in glossary) |
| iteration space skewing | انحراف فضاء التكرار | 0.85 | 2 | Polyhedral transformation |
| producer-consumer relationship | علاقة منتج-مستهلك | 0.9 | 5 | Data flow relationship |
| affine transformation | تحويل أفيني | 0.95 | 8 | Polyhedral model transformation |
| affine constraints | قيود أفينية | 0.95 | 4 | Polyhedral model constraints |
| integer set | مجموعة أعداد صحيحة | 0.95 | 6 | Polyhedral model concept |
| ISL (Integer Set Library) | مكتبة مجموعات الأعداد الصحيحة (ISL) | 1.0 | 4 | Polyhedral library |
| Cloog | Cloog | 1.0 | 2 | Code generation algorithm |
| abstract syntax tree (AST) | شجرة بناء جملة مجردة (AST) | 0.95 | 3 | Compiler IR |
| lexicographical order | ترتيب معجمي | 0.95 | 4 | Ordering for execution |
| iteration domain | مجال التكرار | 0.95 | 15 | Polyhedral model concept |
| space dimensions | أبعاد المكان | 0.9 | 3 | Processor mapping |
| time dimensions | أبعاد الزمن | 0.9 | 3 | Execution ordering |
| overlapped tiling | تبليط متداخل | 0.85 | 2 | Optimization technique |
| struct-of-array (SOA) | بنية من المصفوفات (SOA) | 0.9 | 1 | Data layout pattern |
| array-of-structures (AOS) | مصفوفة من البنى (AOS) | 0.9 | 1 | Data layout pattern |
| full tiles | بلاطات كاملة | 0.85 | 3 | Loop optimization |
| partial tiles | بلاطات جزئية | 0.85 | 3 | Loop optimization |
| thread divergence | تباين الخيوط | 0.9 | 2 | GPU performance issue |
| bounds inference | استنتاج الحدود | 0.9 | 3 | Compiler analysis |
| cyclic dataflow graph | رسم بياني لتدفق البيانات الدوري | 0.85 | 2 | Program representation |
| non-rectangular iteration space | فضاء تكرار غير مستطيل | 0.85 | 4 | Polyhedral model concept |
| auto-tuning | ضبط تلقائي | 0.95 | 2 | Performance optimization |
| array expansion | توسيع المصفوفات | 0.85 | 2 | Compiler transformation |
| scatter/gather operations | عمليات التشتيت/التجميع | 0.85 | 1 | Vectorization operations |
| strong scaling | التوسع القوي | 0.9 | 2 | Distributed computing metric |
| synchronization primitives | بدائيات المزامنة | 0.9 | 2 | Concurrency control |
| constant memory | ذاكرة ثابتة | 0.95 | 2 | GPU memory type |
| shared memory (GPU) | ذاكرة مشتركة (GPU) | 0.95 | 5 | GPU memory type |
| global memory (GPU) | ذاكرة عامة (GPU) | 0.95 | 4 | GPU memory type |
| local memory (GPU) | ذاكرة محلية (GPU) | 0.95 | 3 | GPU memory type |
| four-level IR | تمثيل وسيط من أربعة مستويات | 0.9 | 3 | Tiramisu architecture |
| embedded DSL | لغة خاصة بالمجال مضمنة | 0.9 | 2 | Language design |
| MPI rank | رتبة MPI | 0.95 | 2 | Distributed computing |
| predicate | محمول | 0.9 | 2 | Conditional representation |
| over-approximation | تقدير مبالغ فيه | 0.85 | 3 | Compiler analysis |
| control overhead | عبء التحكم | 0.9 | 2 | Performance metric |
| edge detection | اكتشاف الحواف | 0.95 | 1 | Image processing |
| gaussian blur | ضبابية غاوسية | 0.9 | 2 | Image processing |
| affine warping | التواء أفيني | 0.85 | 1 | Image processing |
| tensor contraction | تقلص الموتر | 0.85 | 1 | Linear algebra operation |
| multigrid preconditioned conjugate gradient | التدرج المترافق المسبق الشرط متعدد الشبكات | 0.8 | 1 | Linear algebra algorithm |
| convolution filter | مرشح الالتفاف | 0.9 | 3 | Deep learning |
| batch size | حجم الدفعة | 0.95 | 1 | Deep learning |
| kernel execution | تنفيذ النواة | 0.95 | 2 | GPU programming |
| host code | شفرة المضيف | 0.95 | 2 | GPU programming |
| device code | شفرة الجهاز | 0.95 | 2 | GPU programming |

## Terms Already in Glossary (Confirmed Usage)

- polyhedral model | النموذج متعدد السطوح
- compiler | مترجم
- code generation | توليد الشفرة
- optimization | التحسين
- loop transformation | تحويلات الحلقات
- vectorization | التوجيه المتجه
- loop unrolling | فك الحلقات
- tiling | تبليط
- parallelization | التوازي
- scheduling | جدولة
- scheduling language | لغة الجدولة
- intermediate representation | تمثيل وسيط
- data layout | تخطيط البيانات
- memory hierarchy | تسلسل هرمي للذاكرة
- GPU | وحدة معالجة الرسومات
- multicore | متعدد الأنوية
- distributed system | نظام موزع

## Summary

- **New terms to add:** 48
- **Existing terms confirmed:** 17
- **Total technical terms used:** 65+
- **Domain focus:** Compilers, Polyhedral Model, Code Optimization, GPU/Distributed Computing
