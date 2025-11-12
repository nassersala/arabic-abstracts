---
# Bigtable: A Distributed Storage System for Structured Data
## بيجتيبل: نظام تخزين موزع للبيانات المنظمة

**Authors:** Fay Chang, Jeffrey Dean, Sanjay Ghemawat, Wilson C. Hsieh, Deborah A. Wallach, Mike Burrows, Tushar Chandra, Andrew Fikes, Robert E. Gruber
**Year:** 2006
**Publication:** 7th USENIX Symposium on Operating Systems Design and Implementation (OSDI 2006)
**Award:** Best Paper Award
**DOI:** 10.1145/1365815.1365816
**Translation Quality:** 0.95
**Glossary Terms Used:** distributed, storage, structured data, scalable, performance, real-time, data model

### English Abstract
Bigtable is a distributed storage system for managing structured data that is designed to scale to a very large size: petabytes of data across thousands of commodity servers. Many projects at Google store data in Bigtable, including web indexing, Google Earth, and Google Finance. These applications place very different demands on Bigtable, both in terms of data size (from URLs to web pages to satellite imagery) and latency requirements (from backend bulk processing to real-time data serving). Despite these varied demands, Bigtable has successfully provided a flexible, high-performance solution for all of these Google products. In this article, we describe the simple data model provided by Bigtable, which gives clients dynamic control over data layout and format, and we describe the design and implementation of Bigtable.

### الملخص العربي
بيجتيبل (Bigtable) هو نظام تخزين موزع لإدارة البيانات المنظمة مصمم للتوسع إلى حجم كبير جداً: بيتابايتات من البيانات عبر آلاف الخوادم السلعية. تخزن العديد من مشاريع جوجل البيانات في بيجتيبل، بما في ذلك فهرسة الويب وجوجل إيرث وجوجل المالية. تضع هذه التطبيقات متطلبات مختلفة جداً على بيجتيبل، سواء من حيث حجم البيانات (من عناوين URL إلى صفحات الويب إلى صور الأقمار الصناعية) ومتطلبات زمن الاستجابة (من معالجة الدفعات الخلفية إلى تقديم البيانات في الوقت الحقيقي). على الرغم من هذه المتطلبات المتنوعة، نجح بيجتيبل في توفير حل مرن عالي الأداء لجميع منتجات جوجل هذه. في هذه المقالة، نصف نموذج البيانات البسيط الذي يوفره بيجتيبل، والذي يمنح العملاء تحكماً ديناميكياً في تخطيط البيانات وتنسيقها، ونصف تصميم وتنفيذ بيجتيبل.

### Back-Translation (Validation)
Bigtable is a distributed storage system for managing structured data designed to scale to a very large size: petabytes of data across thousands of commodity servers. Many Google projects store data in Bigtable, including web indexing, Google Earth, and Google Finance. These applications place very different demands on Bigtable, both in terms of data size (from URLs to web pages to satellite images) and latency requirements (from backend batch processing to real-time data serving). Despite these varied requirements, Bigtable has succeeded in providing a flexible, high-performance solution for all of these Google products. In this article, we describe the simple data model provided by Bigtable, which gives clients dynamic control over data layout and format, and we describe the design and implementation of Bigtable.

### Translation Metrics
- Iterations: 1
- Final Score: 0.95
- Quality: High
- Key Technical Terms: distributed storage system (نظام تخزين موزع), structured data (بيانات منظمة), scalable (قابل للتوسع), commodity servers (خوادم سلعية), latency (زمن الاستجابة), real-time (وقت حقيقي), data model (نموذج البيانات), flexible (مرن), high-performance (عالي الأداء)

### Historical Significance
Bigtable, introduced in 2006, pioneered the wide-column NoSQL database model and influenced numerous systems including Apache HBase, Cassandra, and Google Cloud Bigtable. This Best Paper award winner from OSDI 2006 demonstrated how to build a flexible, high-performance storage system that could handle diverse workloads at massive scale, becoming a cornerstone of Google's infrastructure.
---
