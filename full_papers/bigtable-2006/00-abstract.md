# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.95
**Glossary Terms Used:** distributed, storage, structured data, scalable, performance, real-time, data model, flexible, high-performance

---

### English Version

Bigtable is a distributed storage system for managing structured data that is designed to scale to a very large size: petabytes of data across thousands of commodity servers. Many projects at Google store data in Bigtable, including web indexing, Google Earth, and Google Finance. These applications place very different demands on Bigtable, both in terms of data size (from URLs to web pages to satellite imagery) and latency requirements (from backend bulk processing to real-time data serving). Despite these varied demands, Bigtable has successfully provided a flexible, high-performance solution for all of these Google products. In this article, we describe the simple data model provided by Bigtable, which gives clients dynamic control over data layout and format, and we describe the design and implementation of Bigtable.

---

### النسخة العربية

بيجتيبل (Bigtable) هو نظام تخزين موزع لإدارة البيانات المنظمة مصمم للتوسع إلى حجم كبير جداً: بيتابايتات من البيانات عبر آلاف الخوادم السلعية. تخزن العديد من مشاريع جوجل البيانات في بيجتيبل، بما في ذلك فهرسة الويب وجوجل إيرث وجوجل المالية. تضع هذه التطبيقات متطلبات مختلفة جداً على بيجتيبل، سواء من حيث حجم البيانات (من عناوين URL إلى صفحات الويب إلى صور الأقمار الصناعية) ومتطلبات زمن الاستجابة (من معالجة الدفعات الخلفية إلى تقديم البيانات في الوقت الحقيقي). على الرغم من هذه المتطلبات المتنوعة، نجح بيجتيبل في توفير حل مرن عالي الأداء لجميع منتجات جوجل هذه. في هذه المقالة، نصف نموذج البيانات البسيط الذي يوفره بيجتيبل، والذي يمنح العملاء تحكماً ديناميكياً في تخطيط البيانات وتنسيقها، ونصف تصميم وتنفيذ بيجتيبل.

---

### Translation Notes

- **Key terms introduced:** distributed storage system (نظام تخزين موزع), structured data (بيانات منظمة), commodity servers (خوادم سلعية), latency (زمن الاستجابة), real-time (وقت حقيقي), data model (نموذج البيانات)
- **Special handling:** None
- **Source:** Copied from existing abstract translation in translations/bigtable-2006.md

### Quality Metrics

- Semantic equivalence: 0.95
- Technical accuracy: 0.95
- Readability: 0.95
- Glossary consistency: 0.95
- **Overall section score:** 0.95
