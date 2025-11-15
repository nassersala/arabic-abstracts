# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** deep learning, generative models, GANs, autoregressive models, variational autoencoders, diffusion probabilistic models, latent variable models, training, likelihood, sampling

---

### English Version

Deep generative models of all kinds have recently exhibited high quality samples in a wide variety of data modalities. Generative adversarial networks (GANs), autoregressive models, flows, and variational autoencoders (VAEs) have synthesized striking image and audio samples, and there have even been examples of empirical likelihood scores that surpass those of traditional likelihood-based models on certain datasets.

In this work, we present progress in diffusion probabilistic models. Diffusion models are a class of latent variable models defined using a Markov chain of diffusion steps to slowly add random noise to data and then learning to reverse the diffusion process to construct desired data samples from the noise. Unlike VAE or flow models, diffusion probabilistic models are learned with a fixed procedure and the latent variables have high dimensionality (same as the original data).

Despite their simplicity, diffusion models have not received the same attention as other classes of generative models. We present several novel enhancements to diffusion models that enable them to produce high quality samples. First, we show that a certain parameterization of diffusion models reveals an equivalence with denoising score matching over multiple noise levels during training and with annealed Langevin dynamics during sampling. Second, we find that even after training with a large number of noise scales, sample quality can be improved by using only a subset of the diffusion steps in a progressive manner to generate a sample.

Our diffusion models achieve the best quality reported so far for diffusion-based generative models on several image datasets. On CIFAR-10, we obtain a state-of-the-art FID score of 3.17, competitive with that of other generative modeling paradigms. On high-resolution datasets, we demonstrate that diffusion models produce high quality samples and retain their flexibility for tasks such as lossy compression, inpainting, and progressive generation.

---

### النسخة العربية

أظهرت النماذج التوليدية العميقة بجميع أنواعها مؤخراً عينات عالية الجودة في مجموعة واسعة من أنماط البيانات. فقد قامت الشبكات التنافسية التوليدية (GANs)، والنماذج الانحدارية الذاتية، والتدفقات، والمشفرات التلقائية التباينية (VAEs) بتوليد عينات مذهلة من الصور والصوت، بل وكانت هناك أمثلة على درجات احتمالية تجريبية تتفوق على تلك الخاصة بالنماذج التقليدية القائمة على الاحتمال في مجموعات بيانات معينة.

في هذا العمل، نقدم تقدماً في نماذج الانتشار الاحتمالية. نماذج الانتشار هي فئة من نماذج المتغيرات الكامنة المُعرّفة باستخدام سلسلة ماركوف من خطوات الانتشار لإضافة ضوضاء عشوائية ببطء إلى البيانات ثم تعلم عكس عملية الانتشار لبناء عينات البيانات المطلوبة من الضوضاء. على عكس نماذج VAE أو نماذج التدفق، يتم تعلم نماذج الانتشار الاحتمالية بإجراء ثابت وتكون المتغيرات الكامنة ذات بُعد عالٍ (مماثل للبيانات الأصلية).

على الرغم من بساطتها، لم تحظَ نماذج الانتشار بنفس الاهتمام الذي حظيت به الفئات الأخرى من النماذج التوليدية. نقدم العديد من التحسينات الجديدة لنماذج الانتشار التي تمكنها من إنتاج عينات عالية الجودة. أولاً، نُظهر أن معاملة معينة لنماذج الانتشار تكشف عن تكافؤ مع مطابقة النقاط لإزالة الضوضاء عبر مستويات ضوضاء متعددة أثناء التدريب ومع ديناميكيات لانجفين المُبرَّدة أثناء أخذ العينات. ثانياً، نجد أنه حتى بعد التدريب بعدد كبير من مقاييس الضوضاء، يمكن تحسين جودة العينات باستخدام مجموعة فرعية فقط من خطوات الانتشار بطريقة تدريجية لتوليد عينة.

تحقق نماذج الانتشار لدينا أفضل جودة تم الإبلاغ عنها حتى الآن للنماذج التوليدية القائمة على الانتشار على العديد من مجموعات بيانات الصور. على CIFAR-10، نحصل على نقاط FID متقدمة بقيمة 3.17، منافسة لتلك الخاصة بنماذج التوليد الأخرى. على مجموعات البيانات عالية الدقة، نوضح أن نماذج الانتشار تنتج عينات عالية الجودة وتحتفظ بمرونتها للمهام مثل الضغط بفقدان، وملء الفجوات، والتوليد التدريجي.

---

### Translation Notes

- **Key concepts introduced:**
  - Diffusion probabilistic models (نماذج الانتشار الاحتمالية)
  - Markov chain of diffusion steps (سلسلة ماركوف من خطوات الانتشار)
  - Denoising score matching (مطابقة النقاط لإزالة الضوضاء)
  - Annealed Langevin dynamics (ديناميكيات لانجفين المُبرَّدة)
  - Progressive generation (التوليد التدريجي)

- **Models mentioned:** GANs, autoregressive models, flows, VAEs
- **Datasets:** CIFAR-10, high-resolution datasets
- **Metrics:** FID score (3.17)
- **Applications:** lossy compression, inpainting, progressive generation

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.88
