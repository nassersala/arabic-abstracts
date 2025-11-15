# Section 4: Model Details
## القسم 4: تفاصيل النموذج

**Section:** experiments
**Translation Quality:** 0.88
**Glossary Terms Used:** optimizer, learning rate, batch normalization, hyperparameter, loss function, decoder, spectrogram

---

### English Version

We train Tacotron on an internal North American English dataset, which contains about 24.6 hours of speech data spoken by a professional female speaker. The phrases are text normalized, e.g. "16" is converted to "sixteen".

We use a pre-emphasis filter with coefficient 0.97. We compute 80-band mel-scale spectrogram using a 50 ms frame length, 12.5 ms frame shift, and Hann windowing. We use 2048-point FFT and use magnitude for the Griffin-Lim reconstruction. We use the predicted spectral magnitudes raised to the power 1.2 in Griffin-Lim. We found that this works better than the linear magnitudes. The sampling rate is 24 kHz.

We use r = 2 (output layer reduction factor) which means the decoder generates 2 frames at each step. Although this is only a 2× reduction, we observed that the model has stable alignments, faster training, and very few attention mistakes even when using r = 5. Also, since we use Griffin-Lim, a slight reduction in quality is introduced by the vocoder. We did not try r > 5 because the spectrogram magnitudes start to have too much compression.

We train using Adam optimizer with learning rate 0.001, decay starting after 500K steps, then 0.0005, 0.0003, and 0.0001. We use a simple ℓ1 loss for both seq2seq decoder (mel-scale spectrogram) and post-processing net (linear-scale spectrogram):

$$\mathcal{L} = \sum_t |y_t - \hat{y}_t|$$

where $y_t$ is the target spectrogram frame and $\hat{y}_t$ is the predicted frame at time step $t$. Both targets are equally weighted in the loss.

We use a batch size of 32, where all sequences are padded to a max length. It's a common practice to train sequence models with a loss mask, which masks loss on zero-padded frames. However, we found that models trained this way don't know when to stop emitting outputs, causing repeated sounds towards the end. One simple trick to get around this problem is to also reconstruct the zero-padded frames.

---

### النسخة العربية

نقوم بتدريب تاكوترون على مجموعة بيانات داخلية للغة الإنجليزية لأمريكا الشمالية، والتي تحتوي على حوالي 24.6 ساعة من بيانات الكلام التي تحدثت بها متحدثة محترفة. يتم تطبيع العبارات نصياً، على سبيل المثال يتم تحويل "16" إلى "sixteen".

نستخدم مرشح التأكيد المسبق (pre-emphasis filter) بمعامل 0.97. نحسب مخطط طيفي بمقياس ميل من 80 نطاقاً باستخدام طول إطار 50 مللي ثانية، وإزاحة إطار 12.5 مللي ثانية، وتنفيذ نافذة هان (Hann windowing). نستخدم تحويل فورييه السريع (FFT) من 2048 نقطة ونستخدم المقدار لإعادة بناء Griffin-Lim. نستخدم المقادير الطيفية المتنبأ بها مرفوعة للقوة 1.2 في Griffin-Lim. وجدنا أن هذا يعمل بشكل أفضل من المقادير الخطية. معدل أخذ العينات هو 24 كيلو هرتز.

نستخدم r = 2 (عامل تخفيض طبقة المخرج) مما يعني أن فك التشفير يولد إطارين في كل خطوة. على الرغم من أن هذا تخفيض بمقدار 2× فقط، لاحظنا أن النموذج لديه محاذاة مستقرة، وتدريب أسرع، وأخطاء انتباه قليلة جداً حتى عند استخدام r = 5. أيضاً، نظراً لأننا نستخدم Griffin-Lim، يتم إدخال انخفاض طفيف في الجودة بواسطة المُركِّب الصوتي. لم نجرب r > 5 لأن المقادير الطيفية تبدأ في الحصول على ضغط كبير جداً.

نقوم بالتدريب باستخدام محسِّن آدم (Adam optimizer) بمعدل تعلم 0.001، ويبدأ الاضمحلال بعد 500 ألف خطوة، ثم 0.0005 و0.0003 و0.0001. نستخدم دالة خسارة ℓ1 بسيطة لكل من فك تشفير seq2seq (مخطط طيفي بمقياس ميل) والشبكة اللاحقة (مخطط طيفي بمقياس خطي):

$$\mathcal{L} = \sum_t |y_t - \hat{y}_t|$$

حيث $y_t$ هو إطار المخطط الطيفي المستهدف و$\hat{y}_t$ هو الإطار المتنبأ به في الخطوة الزمنية $t$. يتم ترجيح كلا الهدفين بالتساوي في الخسارة.

نستخدم حجم دفعة قدره 32، حيث يتم حشو جميع التسلسلات إلى طول أقصى. من الممارسات الشائعة تدريب نماذج التسلسل مع قناع خسارة، والذي يخفي الخسارة على الإطارات المحشوة بالأصفار. ومع ذلك، وجدنا أن النماذج المدربة بهذه الطريقة لا تعرف متى تتوقف عن إصدار المخرجات، مما يتسبب في أصوات متكررة نحو النهاية. حيلة بسيطة واحدة للتغلب على هذه المشكلة هي إعادة بناء الإطارات المحشوة بالأصفار أيضاً.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - pre-emphasis filter: مرشح التأكيد المسبق
  - mel-scale spectrogram: مخطط طيفي بمقياس ميل
  - frame length: طول الإطار
  - frame shift: إزاحة الإطار
  - Hann windowing: تنفيذ نافذة هان
  - FFT (Fast Fourier Transform): تحويل فورييه السريع
  - Griffin-Lim reconstruction: إعادة بناء Griffin-Lim
  - sampling rate: معدل أخذ العينات
  - reduction factor: عامل التخفيض
  - Adam optimizer: محسِّن آدم
  - learning rate: معدل التعلم
  - decay: اضمحلال
  - ℓ1 loss: خسارة ℓ1
  - batch size: حجم الدفعة
  - loss mask: قناع الخسارة
  - zero-padded frames: الإطارات المحشوة بالأصفار
- **Equations:** 1 (loss function)
- **Citations:** 0
- **Special handling:**
  - Preserved mathematical notation and equations
  - Kept technical parameters in their original units (ms, kHz, etc.)
  - Maintained algorithm name "Griffin-Lim" in English

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.91
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88
