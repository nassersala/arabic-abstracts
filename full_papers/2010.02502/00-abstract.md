---
# Denoising Diffusion Implicit Models
## نماذج الانتشار الضمنية لإزالة الضوضاء

**arXiv ID:** 2010.02502
**Authors:** Jiaming Song, Chenlin Meng, Stefano Ermon
**Year:** 2020
**Categories:** Machine Learning (cs.LG); Computer Vision and Pattern Recognition (cs.CV)
**Translation Quality:** 0.91
**Glossary Terms Used:** denoising, diffusion model, probabilistic, image generation, adversarial training, sampling, training, generative, latent space

### English Abstract
Denoising diffusion probabilistic models (DDPMs) have achieved high quality image generation without adversarial training, yet they require simulating a Markov chain for many steps to produce a sample. To accelerate sampling, we present denoising diffusion implicit models (DDIMs), a more efficient class of iterative implicit probabilistic models with the same training procedure as DDPMs. In DDPMs, the generative process is defined as the reverse of a Markovian diffusion process. We construct a class of non-Markovian diffusion processes that lead to the same training objective, but whose reverse process can be much faster to sample from. We empirically demonstrate that DDIMs can produce high quality samples 10× to 50× faster in terms of wall-clock time compared to DDPMs, allow us to trade off computation for sample quality, and can perform semantically meaningful image interpolation directly in the latent space.

### الملخص العربي
حققت نماذج الانتشار الاحتمالية لإزالة الضوضاء (DDPMs) توليد صور عالي الجودة دون تدريب خصامي، ومع ذلك فهي تتطلب محاكاة سلسلة ماركوف لخطوات عديدة لإنتاج عينة. لتسريع أخذ العينات، نقدم نماذج الانتشار الضمنية لإزالة الضوضاء (DDIMs)، وهي فئة أكثر كفاءة من النماذج الاحتمالية الضمنية التكرارية بنفس إجراء التدريب كما في DDPMs. في DDPMs، يتم تعريف العملية التوليدية على أنها عكس عملية انتشار ماركوفية. نقوم ببناء فئة من عمليات الانتشار غير الماركوفية التي تؤدي إلى نفس هدف التدريب، لكن عمليتها العكسية يمكن أن تكون أسرع بكثير في أخذ العينات منها. نوضح تجريبياً أن DDIMs يمكن أن تنتج عينات عالية الجودة أسرع بمقدار 10× إلى 50× من حيث الوقت الفعلي مقارنة بـ DDPMs، وتسمح لنا بالمفاضلة بين الحساب وجودة العينة، ويمكنها إجراء استيفاء صور ذات معنى دلالي مباشرة في الفضاء الكامن.

### Back-Translation (Validation)
Denoising diffusion probabilistic models (DDPMs) achieved high-quality image generation without adversarial training, however they require simulating a Markov chain for many steps to produce a sample. To accelerate sampling, we present denoising diffusion implicit models (DDIMs), a more efficient class of iterative implicit probabilistic models with the same training procedure as DDPMs. In DDPMs, the generative process is defined as the reverse of a Markovian diffusion process. We construct a class of non-Markovian diffusion processes that lead to the same training objective, but whose reverse process can be much faster to sample from. We empirically demonstrate that DDIMs can produce high-quality samples 10× to 50× faster in terms of wall-clock time compared to DDPMs, allow us to trade off between computation and sample quality, and can perform semantically meaningful image interpolation directly in the latent space.

### Translation Metrics
- Iterations: 1
- Final Score: 0.91
- Quality: High
---
