# Section 7: Conclusion
## القسم 7: الخاتمة

**Section:** conclusion
**Translation Quality:** 0.88
**Glossary Terms Used:** hybrid homomorphic encryption, privacy-preserving machine learning, edge devices, hardware acceleration, FPGA, Pasta cipher, PS-PL pipeline, Ethernet, FHE, latency, throughput, XOF, pipelined permutation, scalability

---

### English Version

## VII. CONCLUSION

We presented HHEML, a hardware-accelerated hybrid homomorphic encryption framework for privacy-preserving machine learning on edge devices. Built on the Pasta cipher and inspired by Pasta on Edge, our FPGA design unifies key generation, encryption, and decryption in a PS–PL pipeline with Ethernet-based offloading to a remote FHE server. A dual-XOF pipelined permutation architecture reduces encryption rounds for high-dimensional data, nearly doubling throughput with minimal area overhead. On a PYNQ-Z2 platform, HHEML achieves over 50× lower client-side latency and close to 2× higher throughput compared to prior FPGA-based HHE solutions. These results highlight that lightweight FPGA acceleration makes hybrid HE practical for real-world PPML, enabling secure, low-latency inference on constrained devices. Future work will focus on multi-core pipelining and tighter integration with advanced FHE backends for further scalability and efficiency improvements.

---

### النسخة العربية

## VII. الخاتمة

قدمنا HHEML، وهو إطار عمل تشفير متماثل هجين مُسرّع بالعتاد للتعلم الآلي الحافظ للخصوصية على أجهزة الحافة. بناءً على شفرة Pasta ومستوحى من Pasta on Edge، يوحد تصميمنا على FPGA توليد المفاتيح والتشفير وفك التشفير في مسار PS-PL مع تفريغ قائم على Ethernet إلى خادم التشفير المتماثل الكامل عن بُعد. تقلل معمارية تبديل متدفقة ثنائية XOF جولات التشفير للبيانات عالية الأبعاد، مما يضاعف الإنتاجية تقريباً مع الحد الأدنى من عبء المساحة. على منصة PYNQ-Z2، يحقق HHEML زمن وصول أقل بأكثر من 50 ضعفاً على جانب العميل وإنتاجية أعلى تقارب الضعفين مقارنة بحلول التشفير المتماثل الهجين السابقة القائمة على FPGA. تسلط هذه النتائج الضوء على أن التسريع الخفيف الوزن على FPGA يجعل التشفير المتماثل الهجين عملياً للتعلم الآلي الحافظ للخصوصية في العالم الحقيقي، مما يتيح استدلالاً آمناً منخفض زمن الوصول على الأجهزة المقيدة. سيركز العمل المستقبلي على المسارات المتدفقة متعددة النوى والتكامل الأوثق مع واجهات خلفية متقدمة للتشفير المتماثل الكامل لمزيد من التحسينات في قابلية التوسع والكفاءة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Multi-core pipelining = المسارات المتدفقة متعددة النوى
  - Advanced FHE backends = واجهات خلفية متقدمة للتشفير المتماثل الكامل
  - Real-world PPML = التعلم الآلي الحافظ للخصوصية في العالم الحقيقي
  - Constrained devices = الأجهزة المقيدة
  - Scalability improvements = التحسينات في قابلية التوسع
  - Efficiency improvements = تحسينات الكفاءة

- **Equations:** None
- **Citations:** None
- **Special handling:**
  - Performance metrics (50×, 2×) kept in original form
  - System names (HHEML, Pasta, Pasta on Edge, PYNQ-Z2) kept in English
  - Technical abbreviations (PS-PL, FHE, XOF) used consistently
  - Future work mentioned for completeness

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88

### Back-Translation Check (Full conclusion)

Arabic: "قدمنا HHEML، وهو إطار عمل تشفير متماثل هجين مُسرّع بالعتاد للتعلم الآلي الحافظ للخصوصية على أجهزة الحافة..."

Back to English: "We presented HHEML, a hardware-accelerated hybrid homomorphic encryption framework for privacy-preserving machine learning on edge devices..."

✓ Semantically equivalent to original
