# Section 4: Experiments
## القسم 4: التجارب

**Section:** experiments
**Translation Quality:** 0.88
**Glossary Terms Used:** dataset, training, model architecture, neural network, U-Net, attention, FID score, Inception score, baseline, image generation, progressive generation

---

### English Version

We evaluate our diffusion models on several image datasets. Our model uses a U-Net backbone similar to an unmasked PixelCNN++ with group normalization throughout. Parameters are shared across time, which is specified to the network using the Transformer sinusoidal position embedding. We use self-attention at the 16×16 feature map resolution.

**Sample quality.** We first evaluate unconditional image generation on CIFAR-10, a dataset of 32×32 natural images across 10 classes with 50,000 training examples. We compare against other likelihood-based generative models and find that our model achieves an FID score of 3.17 and Inception score of 9.46, which are competitive with state-of-the-art GANs and better than other likelihood-based models.

We also evaluate on 256×256 images from LSUN and CelebA-HQ. On these high-resolution datasets, our diffusion models produce high-quality samples that are competitive with Progressive GAN and StyleGAN, as shown in Figure 3. The samples exhibit good diversity while maintaining high fidelity, without the mode collapse issues that can affect GANs.

**Progressive generation.** A key advantage of diffusion models is their natural support for progressive generation. We find that the reverse diffusion process proceeds in a coarse-to-fine manner: early denoising steps determine the overall composition and large-scale structure, while later steps refine details and add high-frequency information.

We demonstrate this by showing intermediate steps of the sampling process. Starting from pure noise, the model first generates low-frequency structure (rough shapes and layouts), then progressively adds finer details (textures, edges, small features) in later steps. This hierarchical generation process is an emergent property of the model, not explicitly designed.

**Lossy compression and interpolation.** The progressive nature of the generation process enables flexible lossy compression. By using fewer reverse diffusion steps, we can trade off reconstruction quality for compression rate. We show that diffusion models can perform smooth interpolations in latent space, with the latent code at different timesteps encoding information at different levels of abstraction.

Figure 4 shows interpolations between images in latent space at different noise levels. Interpolations at high noise levels (early in the reverse process) result in smooth transitions between high-level semantic content, while interpolations at low noise levels (late in the reverse process) preserve semantic content while varying fine details.

**Model architecture and hyperparameters.** We use a U-Net architecture with attention mechanisms. The number of timesteps T is set to 1000 for all experiments. The variance schedule $\beta_t$ is set to increase linearly from $\beta_1 = 10^{-4}$ to $\beta_T = 0.02$. We train with the simplified objective $L_{\text{simple}}$ using Adam optimizer with learning rate $2 \times 10^{-4}$.

**Comparison with other generative models.** Table 1 compares our results with other generative modeling approaches on CIFAR-10:

| Model | FID ↓ | Inception ↑ | Negative Log-Likelihood |
|-------|-------|-------------|-------------------------|
| Progressive GAN | 3.08 | 9.18 | - |
| StyleGAN2 | 2.92 | 9.21 | - |
| VAE | - | - | 4.5 |
| Flow-based model | - | - | 3.3 |
| **DDPM (ours)** | **3.17** | **9.46** | **≤ 3.7** |

Our model achieves competitive sample quality (FID and Inception scores) with state-of-the-art GANs while also providing tractable likelihood estimates, unlike GANs.

---

### النسخة العربية

نقيّم نماذج الانتشار الخاصة بنا على العديد من مجموعات بيانات الصور. يستخدم نموذجنا بنية أساسية من نوع U-Net مشابهة لـ PixelCNN++ بدون قناع مع التطبيع الجماعي في جميع الأنحاء. تُشارَك المعاملات عبر الزمن، والذي يتم تحديده للشبكة باستخدام تضمين الموضع الجيبي من Transformer. نستخدم الانتباه الذاتي عند دقة خريطة الميزات 16×16.

**جودة العينات.** نقيّم أولاً توليد الصور غير المشروط على CIFAR-10، وهي مجموعة بيانات من صور طبيعية بحجم 32×32 عبر 10 فئات مع 50,000 مثال تدريبي. نقارن مع النماذج التوليدية الأخرى القائمة على الاحتمالية ونجد أن نموذجنا يحقق نقاط FID بقيمة 3.17 ونقاط Inception بقيمة 9.46، وهي منافسة لشبكات GAN المتقدمة وأفضل من النماذج الأخرى القائمة على الاحتمالية.

نقيّم أيضاً على صور بحجم 256×256 من LSUN و CelebA-HQ. على مجموعات البيانات عالية الدقة هذه، تنتج نماذج الانتشار لدينا عينات عالية الجودة منافسة لـ Progressive GAN و StyleGAN، كما هو موضح في الشكل 3. تُظهر العينات تنوعاً جيداً مع الحفاظ على دقة عالية، دون مشاكل انهيار النمط التي يمكن أن تؤثر على شبكات GAN.

**التوليد التدريجي.** ميزة رئيسية لنماذج الانتشار هي دعمها الطبيعي للتوليد التدريجي. نجد أن عملية الانتشار العكسي تسير بطريقة من الخشن إلى الناعم: تحدد خطوات إزالة الضوضاء المبكرة التكوين العام والبنية واسعة النطاق، بينما تُحسّن الخطوات اللاحقة التفاصيل وتضيف معلومات عالية التردد.

نوضح ذلك من خلال إظهار خطوات وسيطة من عملية أخذ العينات. بدءاً من ضوضاء نقية، يولد النموذج أولاً بنية منخفضة التردد (أشكال تقريبية وتخطيطات)، ثم يضيف تدريجياً تفاصيل أدق (قوام، حواف، ميزات صغيرة) في الخطوات اللاحقة. عملية التوليد الهرمية هذه هي خاصية ناشئة للنموذج، وليست مصممة بشكل صريح.

**الضغط بفقدان والاستيفاء.** تمكّن الطبيعة التدريجية لعملية التوليد من ضغط مرن بفقدان. باستخدام خطوات انتشار عكسي أقل، يمكننا المقايضة بين جودة إعادة البناء ومعدل الضغط. نُظهر أن نماذج الانتشار يمكنها إجراء استيفاءات سلسة في الفضاء الكامن، مع ترميز الكود الكامن في خطوات زمنية مختلفة للمعلومات عند مستويات مختلفة من التجريد.

يُظهر الشكل 4 استيفاءات بين الصور في الفضاء الكامن عند مستويات ضوضاء مختلفة. تؤدي الاستيفاءات عند مستويات ضوضاء عالية (في وقت مبكر من العملية العكسية) إلى انتقالات سلسة بين المحتوى الدلالي عالي المستوى، بينما تحافظ الاستيفاءات عند مستويات ضوضاء منخفضة (في وقت متأخر من العملية العكسية) على المحتوى الدلالي مع تنويع التفاصيل الدقيقة.

**معمارية النموذج والمعاملات الفائقة.** نستخدم معمارية U-Net مع آليات الانتباه. يتم تعيين عدد الخطوات الزمنية T إلى 1000 لجميع التجارب. يتم تعيين جدول التباين $\beta_t$ للزيادة خطياً من $\beta_1 = 10^{-4}$ إلى $\beta_T = 0.02$. نتدرب بالهدف المبسط $L_{\text{simple}}$ باستخدام محسِّن Adam بمعدل تعلم $2 \times 10^{-4}$.

**المقارنة مع النماذج التوليدية الأخرى.** يقارن الجدول 1 نتائجنا مع أساليب النمذجة التوليدية الأخرى على CIFAR-10:

| النموذج | FID ↓ | Inception ↑ | اللوغاريتم السلبي للاحتمالية |
|-------|-------|-------------|-------------------------|
| Progressive GAN | 3.08 | 9.18 | - |
| StyleGAN2 | 2.92 | 9.21 | - |
| VAE | - | - | 4.5 |
| نموذج قائم على التدفق | - | - | 3.3 |
| **DDPM (نموذجنا)** | **3.17** | **9.46** | **≤ 3.7** |

يحقق نموذجنا جودة عينات منافسة (نقاط FID و Inception) مع شبكات GAN المتقدمة مع توفير تقديرات احتمالية قابلة للتتبع أيضاً، على عكس شبكات GAN.

---

### Translation Notes

- **Figures referenced:** Figure 3 (sample quality), Figure 4 (interpolations)
- **Tables:** Table 1 (comparison with baselines)
- **Datasets:** CIFAR-10 (32×32), LSUN (256×256), CelebA-HQ (256×256)
- **Metrics:**
  - FID score (Fréchet Inception Distance)
  - Inception score
  - Negative log-likelihood
- **Model architecture:**
  - U-Net backbone
  - Group normalization
  - Self-attention at 16×16
  - Transformer sinusoidal position embedding
  - T = 1000 timesteps
  - Linear variance schedule
- **Key capabilities:**
  - High-quality generation
  - Progressive/hierarchical generation
  - Lossy compression
  - Smooth interpolation

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.90
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.88
