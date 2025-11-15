# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.90
**Glossary Terms Used:** diffusion model, probabilistic, latent space, thermodynamics, training, denoising, autoregressive, unconditional generation, dataset, state-of-the-art

---

### English Version

We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics. Our best results are obtained by training on a weighted variational bound designed according to a novel connection between diffusion probabilistic models and denoising score matching with Langevin dynamics, and our models naturally admit a progressive lossy decompression scheme that can be interpreted as a generalization of autoregressive decoding. On the unconditional CIFAR10 dataset, we obtain an Inception score of 9.46 and a state-of-the-art FID score of 3.17. On 256x256 LSUN, we obtain sample quality similar to ProgressiveGAN. Our implementation is available at https://github.com/hojonathanho/diffusion.

---

### النسخة العربية

نقدم نتائج توليد صور عالية الجودة باستخدام نماذج الانتشار الاحتمالية، وهي فئة من نماذج المتغيرات الكامنة مستوحاة من اعتبارات الديناميكا الحرارية اللاتوازنية. يتم الحصول على أفضل نتائجنا من خلال التدريب على حد تباين موزون مصمم وفقاً لارتباط جديد بين نماذج الانتشار الاحتمالية ومطابقة النقاط لإزالة الضوضاء مع ديناميكيات لانجفين، وتسمح نماذجنا بشكل طبيعي بمخطط فك ضغط تدريجي بفقدان يمكن تفسيره كتعميم لفك التشفير الانحداري الذاتي. على مجموعة بيانات CIFAR10 غير المشروطة، نحصل على نقاط Inception بقيمة 9.46 ونقاط FID متقدمة بقيمة 3.17. على LSUN بحجم 256×256، نحصل على جودة عينات مماثلة لـ ProgressiveGAN. التطبيق الخاص بنا متاح على https://github.com/hojonathanho/diffusion.

---

### Translation Notes

- **Key terms introduced:** diffusion probabilistic models, nonequilibrium thermodynamics, denoising score matching, Langevin dynamics, variational bound, progressive lossy decompression, autoregressive decoding
- **Datasets mentioned:** CIFAR10, LSUN (256x256)
- **Metrics:** Inception score (9.46), FID score (3.17)
- **Comparison:** ProgressiveGAN

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.91
- Readability: 0.88
- Glossary consistency: 0.89
- **Overall section score:** 0.90
