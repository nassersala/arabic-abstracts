# Section 6: Conclusion
## القسم 6: الخلاصة

**Section:** conclusion
**Translation Quality:** 0.88
**Glossary Terms Used:** RNS-CKKS, FHE, PPML, ResNet-20, deep neural network, ReLU, bootstrapping, softmax, approximation, classification accuracy

---

### English Version

For the first time, we applied the RNS-CKKS scheme, one of the state-of-the-art FHE schemes, to the standard deep neural network ResNet-20 to implement the PPML. Since the precise approximation of the ReLU function, the bootstrapping, and the softmax function had not been applied to the PPML models until now, we applied these techniques with fine-tuned various parameters. Then, we showed that the implemented ResNet-20 with the RNS-CKKS scheme achieves almost the same result as the original ResNet-20 and reaches the highest classification accuracy among the PPML models with the word-wise FHE scheme introduced so far. This work firstly suggested that the word-wise FHE with the most advanced techniques can be applied to the state-of-the-art machine learning model without re-training it.

---

### النسخة العربية

للمرة الأولى، طبقنا مخطط RNS-CKKS، أحد مخططات FHE الحديثة، على الشبكة العصبية العميقة المعيارية ResNet-20 لتطبيق PPML. نظرًا لأن التقريب الدقيق لدالة ReLU والتمهيد الذاتي ودالة softmax لم يتم تطبيقه على نماذج PPML حتى الآن، فقد طبقنا هذه التقنيات بمعاملات متنوعة محسّنة بدقة. ثم أظهرنا أن ResNet-20 المطبق بمخطط RNS-CKKS يحقق نفس النتيجة تقريبًا مثل ResNet-20 الأصلي ويصل إلى أعلى دقة تصنيف بين نماذج PPML بمخطط FHE الكلمي المقدم حتى الآن. اقترح هذا العمل للمرة الأولى أن FHE الكلمي بالتقنيات الأكثر تقدمًا يمكن تطبيقه على نموذج تعلم الآلة الحديث دون إعادة تدريبه.

---

### Translation Notes

- **Key achievements summarized:**
  - First application of RNS-CKKS to standard deep networks
  - Precise approximation of ReLU, bootstrapping, and softmax
  - 98.67% agreement with plaintext ResNet-20
  - Highest accuracy (90.67%) among FHE-based PPML models
  - No retraining required - uses pre-trained models directly
- **Equations:** None
- **Citations:** None (summary section)
- **Special handling:**
  - Concise summary maintaining all key contributions
  - Emphasis on "first time" achievements

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.88
- Glossary consistency: 0.88
- **Overall section score:** 0.88
