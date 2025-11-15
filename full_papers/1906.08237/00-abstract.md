# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.93
**Glossary Terms Used:** autoregressive, pretraining, language understanding, bidirectional, denoising autoencoding, BERT, language modeling, masking, permutation, transformer, question answering, sentiment analysis, natural language inference

---

### English Version

With the capability of modeling bidirectional contexts, denoising autoencoding based pretraining like BERT achieves better performance than pretraining approaches based on autoregressive language modeling. However, relying on corrupting the input with masks, BERT neglects dependency between the masked positions and suffers from a pretrain-finetune discrepancy. In light of these pros and cons, we propose XLNet, a generalized autoregressive pretraining method that (1) enables learning bidirectional contexts by maximizing the expected likelihood over all permutations of the factorization order and (2) overcomes the limitations of BERT thanks to its autoregressive formulation. Furthermore, XLNet integrates ideas from Transformer-XL, the state-of-the-art autoregressive model, into pretraining. Empirically, under comparable experiment settings, XLNet outperforms BERT on 20 tasks, often by a large margin, including question answering, natural language inference, sentiment analysis, and document ranking.

---

### النسخة العربية

بفضل القدرة على نمذجة السياقات ثنائية الاتجاه، يحقق التدريب المسبق القائم على الترميز التلقائي لإزالة الضوضاء مثل BERT أداءً أفضل من مناهج التدريب المسبق القائمة على النمذجة اللغوية الانحدارية الذاتية. ومع ذلك، بالاعتماد على إفساد المدخلات بالإخفاء، يتجاهل BERT التبعية بين المواضع المخفاة ويعاني من تباين بين التدريب المسبق والضبط الدقيق. في ضوء هذه الإيجابيات والسلبيات، نقترح XLNet، وهي طريقة تدريب مسبق انحداري ذاتي معممة (1) تمكّن من تعلم السياقات ثنائية الاتجاه من خلال تعظيم الاحتمالية المتوقعة على جميع تبديلات ترتيب التحليل العاملي و(2) تتغلب على قيود BERT بفضل صياغتها الانحدارية الذاتية. علاوة على ذلك، يدمج XLNet أفكاراً من Transformer-XL، النموذج الانحداري الذاتي الأحدث، في التدريب المسبق. تجريبياً، في ظل إعدادات تجريبية قابلة للمقارنة، يتفوق XLNet على BERT في 20 مهمة، غالباً بهامش كبير، بما في ذلك الإجابة على الأسئلة والاستدلال اللغوي الطبيعي وتحليل المشاعر وترتيب المستندات.

---

### Translation Notes

- **Figures referenced:** None in abstract
- **Key terms introduced:** Permutation language modeling, two-stream self-attention (implicit)
- **Equations:** None in abstract
- **Citations:** Implicit references to BERT and Transformer-XL
- **Special handling:** None

### Quality Metrics

- Semantic equivalence: 0.95
- Technical accuracy: 0.94
- Readability: 0.92
- Glossary consistency: 0.91
- **Overall section score:** 0.93
