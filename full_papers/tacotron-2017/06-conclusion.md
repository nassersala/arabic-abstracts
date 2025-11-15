# Section 6: Conclusion and Future Work
## القسم 6: الخاتمة والعمل المستقبلي

**Section:** conclusion
**Translation Quality:** 0.90
**Glossary Terms Used:** end-to-end, spectrogram, attention mechanism, neural network, autoregressive

---

### English Version

We have proposed Tacotron, an integrated end-to-end generative TTS model that takes a character sequence as input and outputs the corresponding spectrogram. With a very simple waveform synthesis module, it achieves a 3.82 MOS score on US English, outperforming a production parametric system in terms of naturalness. Since Tacotron generates speech at the frame-level, it's substantially faster than sample-level autoregressive methods.

Tacotron is an integrated end-to-end TTS system and achieves state-of-the-art naturalness without using any linguistic features. We have shown that our model learns pronunciation of words based purely on spelling, does not require hand-designed components such as an HMM aligner, and can be trained from scratch with random initialization. Our model is easy to train and can benefit from large amounts of acoustic data with transcripts.

Since the network is built on generic machine learning frameworks, we believe many design choices can be further improved. For instance, the current output layer, attention mechanism, loss function, and the Griffin-Lim-based waveform synthesizer are by no means optimal and can be replaced with better alternatives. For example, it's well known that Griffin-Lim outputs may have audible artifacts; we are currently working on fast and high-quality neural-network-based spectrogram inversion.

---

### النسخة العربية

لقد اقترحنا تاكوترون، وهو نموذج توليدي متكامل من طرف إلى طرف لتوليف الكلام من النص يأخذ تسلسل أحرف كمدخل ويُخرج المخطط الطيفي المقابل. مع وحدة توليف موجي بسيطة جداً، يحقق درجة MOS قدرها 3.82 للغة الإنجليزية الأمريكية، متفوقاً على نظام بارامتري إنتاجي من حيث الطبيعية. نظراً لأن تاكوترون يولد الكلام على مستوى الإطار، فإنه أسرع بكثير من الطرق الانحدارية الذاتية على مستوى العينة.

تاكوترون هو نظام متكامل من طرف إلى طرف لتوليف الكلام من النص ويحقق طبيعية على مستوى أحدث ما توصل إليه العلم دون استخدام أي ميزات لغوية. لقد أظهرنا أن نموذجنا يتعلم نطق الكلمات بناءً على الإملاء فقط، ولا يتطلب مكونات مصممة يدوياً مثل محاذي HMM، ويمكن تدريبه من الصفر مع التهيئة العشوائية. نموذجنا سهل التدريب ويمكن أن يستفيد من كميات كبيرة من البيانات الصوتية مع النصوص المكتوبة.

نظراً لأن الشبكة مبنية على أطر عمل تعلم آلي عامة، نعتقد أن العديد من خيارات التصميم يمكن تحسينها بشكل أكبر. على سبيل المثال، طبقة المخرج الحالية، وآلية الانتباه، ودالة الخسارة، ومُركِّب الموجة القائم على Griffin-Lim ليست بأي حال من الأحوال مثالية ويمكن استبدالها ببدائل أفضل. على سبيل المثال، من المعروف جيداً أن مخرجات Griffin-Lim قد تحتوي على عيوب سمعية؛ نحن نعمل حالياً على انعكاس المخطط الطيفي السريع وعالي الجودة القائم على الشبكات العصبية.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - state-of-the-art: أحدث ما توصل إليه العلم
  - linguistic features: ميزات لغوية
  - HMM aligner: محاذي HMM
  - random initialization: التهيئة العشوائية
  - machine learning frameworks: أطر عمل تعلم آلي
  - output layer: طبقة المخرج
  - loss function: دالة الخسارة
  - waveform synthesizer: مُركِّب الموجة
  - spectrogram inversion: انعكاس المخطط الطيفي
  - audible artifacts: عيوب سمعية
- **Equations:** 0
- **Citations:** 0
- **Special handling:**
  - Preserved MOS score value
  - Kept algorithm name "Griffin-Lim" in English
  - Maintained technical acronyms (HMM, MOS)

### Quality Metrics

- Semantic equivalence: 0.91
- Technical accuracy: 0.92
- Readability: 0.89
- Glossary consistency: 0.88
- **Overall section score:** 0.90
