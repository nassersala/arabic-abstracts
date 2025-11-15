# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.91
**Glossary Terms Used:** neural network, encoder, decoder, attention mechanism, sequence, synthesis

---

### English Version

A text-to-speech synthesis system typically consists of multiple stages, such as a text analysis frontend, an acoustic model and an audio synthesis module. Building these components often requires extensive domain expertise and may contain brittle design choices. In this paper, we present Tacotron, an end-to-end generative text-to-speech model that synthesizes speech directly from characters. Given <text, audio> pairs, the model can be trained completely from scratch with random initialization. We present several key techniques to make the sequence-to-sequence framework perform well for this challenging task. Tacotron achieves a 3.82 subjective 5-scale mean opinion score on US English, outperforming a production parametric system in terms of naturalness. In addition, since Tacotron generates speech at the frame level, it's substantially faster than sample-level autoregressive methods.

---

### النسخة العربية

يتكون نظام توليف الكلام من النص (text-to-speech) عادةً من مراحل متعددة، مثل الواجهة الأمامية لتحليل النص، والنموذج الصوتي، ووحدة توليف الصوت. غالباً ما يتطلب بناء هذه المكونات خبرة واسعة في المجال وقد يحتوي على خيارات تصميمية هشة. في هذا البحث، نقدم تاكوترون (Tacotron)، وهو نموذج توليدي من طرف إلى طرف لتوليف الكلام من النص يقوم بتوليف الكلام مباشرةً من الأحرف. عند إعطاء أزواج من <النص، الصوت>، يمكن تدريب النموذج بالكامل من الصفر مع التهيئة العشوائية. نقدم عدة تقنيات رئيسية لجعل إطار العمل من تسلسل إلى تسلسل (sequence-to-sequence) يعمل بشكل جيد لهذه المهمة الصعبة. يحقق تاكوترون درجة 3.82 في متوسط تقييم الرأي الذاتي على مقياس من 5 درجات للغة الإنجليزية الأمريكية، متفوقاً على نظام بارامتري إنتاجي من حيث الطبيعية. بالإضافة إلى ذلك، نظراً لأن تاكوترون يولد الكلام على مستوى الإطار (frame)، فإنه أسرع بكثير من الطرق الانحدارية الذاتية (autoregressive) على مستوى العينة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - text-to-speech synthesis: توليف الكلام من النص
  - end-to-end: من طرف إلى طرف
  - sequence-to-sequence: من تسلسل إلى تسلسل
  - mean opinion score (MOS): متوسط تقييم الرأي
  - frame level: مستوى الإطار
  - autoregressive: انحداري ذاتي
  - parametric system: نظام بارامتري
- **Equations:** 0
- **Citations:** 0
- **Special handling:** Kept technical term "Tacotron" in both Arabic and transliterated form for clarity

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.93
- Readability: 0.90
- Glossary consistency: 0.90
- **Overall section score:** 0.91
