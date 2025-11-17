# Section 6: Conclusion
## القسم 6: الخاتمة

**Section:** conclusion
**Translation Quality:** 0.87
**Glossary Terms Used:** computation-enabled object storage, query offloading, columnar layout, array-aware expressions, query execution, storage layers, data movement

---

### English Version

In this work, we presented OASIS, a computation-enabled object storage (COS) system designed for high-throughput scientific analytics workloads. OASIS overcomes key limitations of existing COS systems by enabling fine-grained operator offloading, supporting complex array-aware expressions, and dynamically optimizing query execution across storage layers. Leveraging Substrait-based plan decomposition and dynamic execution path optimization, OASIS identifies optimal split points to minimize data movement while utilizing in-storage compute. Real-world HPC query evaluations show that OASIS not only reduces execution time but also significantly improves resource efficiency across the storage stack.

---

### النسخة العربية

في هذا العمل، قدمنا OASIS، وهو نظام تخزين كائنات ممكّن حسابياً (COS) مصمم لأحمال العمل التحليلية العلمية عالية الإنتاجية. يتغلب OASIS على القيود الرئيسية لأنظمة COS الحالية من خلال تمكين تفريغ المعاملات الدقيق، ودعم التعبيرات المعقدة الواعية بالمصفوفات، وتحسين تنفيذ الاستعلام ديناميكياً عبر طبقات التخزين. من خلال الاستفادة من تحليل الخطة القائم على Substrait وتحسين مسار التنفيذ الديناميكي، يحدد OASIS نقاط التقسيم المثلى لتقليل حركة البيانات مع استخدام الحساب داخل التخزين. تُظهر تقييمات استعلامات HPC الحقيقية أن OASIS لا يقلل من وقت التنفيذ فحسب، بل يحسن أيضاً بشكل كبير كفاءة الموارد عبر مكدس التخزين.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** None (summary section)
- **Equations:** None
- **Citations:** None
- **Special handling:** This is a brief conclusion section summarizing the main contributions

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
