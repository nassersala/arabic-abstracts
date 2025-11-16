# Abstract
## الملخص

**Section:** Abstract
**Translation Quality:** 0.94
**Glossary Terms Used:** transformer, abstract syntax tree, code completion, code summarization, code search

---

### English Version

Transformer-based models have demonstrated state-of-the-art performance in many intelligent coding tasks such as code comment generation and code completion. Previous studies show that deep learning models are sensitive to the input variations, but few studies have systematically studied the robustness of Transformer under perturbed input code. In this work, we empirically study the effect of semantic-preserving code transformation on the performance of Transformer. Specifically, 24 and 27 code transformation strategies are implemented for two popular programming languages, Java and Python, respectively. For facilitating analysis, the strategies are grouped into five categories: block transformation, insertion / deletion transformation, grammatical statement transformation, grammatical token transformation, and identifier transformation. Experiments on three popular code intelligence tasks, including code completion, code summarization and code search, demonstrate insertion / deletion transformation and identifier transformation show the greatest impact on the performance of Transformer. Our results also suggest that Transformer based on abstract syntax trees (ASTs) shows more robust performance than the model based on only code sequence under most code transformations. Besides, the design of positional encoding can impact the robustness of Transformer under code transformation. Based on our findings, we distill some insights about the challenges and opportunities for Transformer-based code intelligence.

---

### النسخة العربية

أظهرت النماذج المعتمدة على المحول أداءً متقدماً في العديد من مهام البرمجة الذكية مثل توليد تعليقات الشفرة وإكمال الشفرة. تظهر الدراسات السابقة أن نماذج التعلم العميق حساسة للتغيرات في المدخلات، لكن قلة من الدراسات درست بشكل منهجي متانة المحول تحت الشفرة المدخلة المضطربة. في هذا العمل، ندرس تجريبياً تأثير تحويل الشفرة الحافظ للدلالة على أداء المحول. على وجه التحديد، تم تنفيذ 24 و27 استراتيجية تحويل شفرة لِلغتَي برمجة شائعتَين، جافا وبايثون، على التوالي. لتسهيل التحليل، تم تجميع الاستراتيجيات في خمس فئات: تحويل الكتلة، وتحويل الإدراج/الحذف، وتحويل العبارة النحوية، وتحويل الرمز النحوي، وتحويل المعرف. تُظهر التجارب على ثلاث مهام ذكاء شفرة شائعة، بما في ذلك إكمال الشفرة وتلخيص الشفرة والبحث في الشفرة، أن تحويل الإدراج/الحذف وتحويل المعرف يُظهران أكبر تأثير على أداء المحول. تشير نتائجنا أيضاً إلى أن المحول المعتمد على أشجار البنية التركيبية المجردة (ASTs) يُظهر أداءً أكثر متانة من النموذج المعتمد على تسلسل الشفرة فقط تحت معظم تحويلات الشفرة. بالإضافة إلى ذلك، يمكن أن يؤثر تصميم الترميز الموضعي على متانة المحول تحت تحويل الشفرة. بناءً على نتائجنا، نستخلص بعض الرؤى حول التحديات والفرص لذكاء الشفرة المعتمد على المحول.

---

### Translation Notes

- **Key terms introduced:**
  - semantic-preserving transformation (تحويل حافظ للدلالة)
  - block transformation (تحويل الكتلة)
  - insertion/deletion transformation (تحويل الإدراج/الحذف)
  - grammatical statement transformation (تحويل العبارة النحوية)
  - grammatical token transformation (تحويل الرمز النحوي)
  - identifier transformation (تحويل المعرف)
  - positional encoding (ترميز موضعي)
  - robustness (متانة)

- **Special handling:** This is a pre-existing translation from translations/2207.04285.md

### Quality Metrics

- Semantic equivalence: 0.94
- Technical accuracy: 0.95
- Readability: 0.93
- Glossary consistency: 0.95
- **Overall section score:** 0.94
