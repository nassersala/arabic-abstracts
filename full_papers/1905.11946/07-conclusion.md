# Section 7: Conclusion
## القسم 7: الخلاصة

**Section:** conclusion
**Translation Quality:** 0.88
**Glossary Terms Used:** ConvNet scaling, network width, depth, resolution, compound scaling, accuracy, efficiency, baseline, EfficientNet, state-of-the-art, parameters, FLOPS, ImageNet, transfer learning

---

### English Version

In this paper, we systematically study ConvNet scaling and identify that carefully balancing network width, depth, and resolution is an important but missing piece, preventing us from better accuracy and efficiency. To address this issue, we propose a simple and highly effective compound scaling method, which enables us to easily scale up a baseline ConvNet to any target resource constraints in a more principled way, while maintaining model efficiency. Powered by this compound scaling method, we demonstrate that a mobile-size EfficientNet model can be scaled up very effectively, surpassing state-of-the-art accuracy with an order of magnitude fewer parameters and FLOPS, on both ImageNet and five commonly used transfer learning datasets.

---

### النسخة العربية

في هذه الورقة، ندرس توسيع الشبكات الالتفافية بشكل منهجي ونحدد أن الموازنة الدقيقة بين عرض الشبكة وعمقها ودقة الوضوح هي قطعة مهمة ولكنها مفقودة، تمنعنا من تحقيق دقة وكفاءة أفضل. لمعالجة هذه المشكلة، نقترح طريقة توسيع مركب بسيطة وفعالة للغاية، والتي تمكننا من توسيع شبكة التفافية خط أساس بسهولة إلى أي قيود موارد مستهدفة بطريقة أكثر منهجية، مع الحفاظ على كفاءة النموذج. مدعومين بطريقة التوسيع المركب هذه، نوضح أنه يمكن توسيع نموذج EfficientNet بحجم الهاتف المحمول بفعالية كبيرة، متجاوزاً الدقة المتقدمة بمعاملات وFLOPS أقل بمرتبة من حيث الحجم، على كل من ImageNet وخمس مجموعات بيانات للتعلم بالنقل مستخدمة بشكل شائع.

---

### Translation Notes

- **Figures referenced:** None
- **Tables referenced:** None
- **Key terms introduced:** None (all previously introduced)
- **Equations:** None
- **Citations:** None (summary section)
- **Special handling:** Final summary of contributions; emphasis on key findings

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
