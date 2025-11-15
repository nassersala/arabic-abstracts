# Section 5: Related Work
## القسم 5: الأعمال ذات الصلة

**Section:** related_work
**Translation Quality:** 0.87
**Glossary Terms Used:** generative models, GANs, VAEs, autoregressive models, normalizing flows, diffusion models, score matching, energy-based models, Langevin dynamics, denoising

---

### English Version

**Generative models.** Diffusion probabilistic models belong to the family of latent variable models. Generative adversarial networks (GANs) have produced high-quality samples but can be difficult to train and may suffer from mode collapse. Variational autoencoders (VAEs) and normalizing flows provide tractable likelihood estimation but have historically produced samples of lower quality than GANs. Autoregressive models achieve strong likelihood performance but can be slow to sample from due to their sequential generation process.

Our work shows that diffusion models can achieve sample quality competitive with GANs while maintaining the benefits of likelihood-based models, including stable training and mode coverage.

**Score-based generative models.** There is a close connection between diffusion probabilistic models and score-based generative models that use Langevin dynamics for sampling. Score matching methods learn the gradient of the log data density (the score function) and use it for generation. Recent work has shown that training score models across multiple noise scales significantly improves sample quality.

Our simplified training objective can be interpreted as a form of denoising score matching. The connection between diffusion models and score matching provides theoretical grounding for why our training procedure works well.

**Energy-based models.** Energy-based models (EBMs) define probability distributions through an energy function. While EBMs are flexible and theoretically appealing, they often require expensive MCMC sampling during both training and generation. Diffusion models can be viewed as a special case of EBMs where the energy function has a particular structure that enables efficient training and sampling.

**Denoising autoencoders.** Denoising autoencoders learn to reconstruct clean data from corrupted inputs. Our work shows that diffusion models can be interpreted as a sequence of denoising autoencoders, each trained to remove a specific amount of noise. This connection helps explain the effectiveness of our simplified training objective.

**Progressive generation.** Several prior works have explored progressive or hierarchical generation, including Progressive GAN and hierarchical VAEs. However, in these models, the progressive structure must be explicitly designed into the architecture. In contrast, our diffusion models naturally exhibit coarse-to-fine generation as an emergent property of the reverse diffusion process, without requiring special architectural modifications.

**Non-equilibrium thermodynamics.** The original formulation of diffusion probabilistic models drew inspiration from non-equilibrium statistical physics. The forward diffusion process can be viewed as gradually increasing the entropy of the system, while the reverse process learns to decrease entropy and generate structured data from noise.

**Applications.** Since the development of diffusion models, they have been applied to various domains beyond image generation, including audio synthesis, video generation, molecular design, and 3D shape generation. The flexibility and stability of diffusion models make them suitable for many generative modeling tasks.

---

### النسخة العربية

**النماذج التوليدية.** تنتمي نماذج الانتشار الاحتمالية إلى عائلة نماذج المتغيرات الكامنة. أنتجت الشبكات التنافسية التوليدية (GANs) عينات عالية الجودة ولكن قد يكون من الصعب تدريبها وقد تعاني من انهيار النمط. توفر المشفرات التلقائية التباينية (VAEs) والتدفقات التطبيعية تقدير احتمالية قابل للتتبع لكنها أنتجت تاريخياً عينات ذات جودة أقل من شبكات GAN. تحقق النماذج الانحدارية الذاتية أداءً قوياً في الاحتمالية ولكن قد تكون بطيئة في أخذ العينات بسبب عملية التوليد المتسلسلة.

يُظهر عملنا أن نماذج الانتشار يمكن أن تحقق جودة عينات منافسة لشبكات GAN مع الحفاظ على فوائد النماذج القائمة على الاحتمالية، بما في ذلك التدريب المستقر وتغطية الأنماط.

**النماذج التوليدية القائمة على النقاط.** هناك ارتباط وثيق بين نماذج الانتشار الاحتمالية والنماذج التوليدية القائمة على النقاط التي تستخدم ديناميكيات لانجفين لأخذ العينات. تتعلم طرق مطابقة النقاط تدرج كثافة اللوغاريتم للبيانات (دالة النقاط) وتستخدمها للتوليد. أظهرت الأعمال الحديثة أن تدريب نماذج النقاط عبر مقاييس ضوضاء متعددة يُحسّن جودة العينات بشكل كبير.

يمكن تفسير هدف التدريب المبسط لدينا كشكل من أشكال مطابقة النقاط لإزالة الضوضاء. يوفر الارتباط بين نماذج الانتشار ومطابقة النقاط أساساً نظرياً لسبب نجاح إجراء التدريب الخاص بنا.

**النماذج القائمة على الطاقة.** تُعرّف النماذج القائمة على الطاقة (EBMs) توزيعات الاحتمالية من خلال دالة طاقة. بينما تكون نماذج EBM مرنة وجذابة نظرياً، فإنها غالباً ما تتطلب أخذ عينات MCMC مكلفة أثناء التدريب والتوليد. يمكن النظر إلى نماذج الانتشار كحالة خاصة من نماذج EBM حيث تمتلك دالة الطاقة بنية معينة تمكّن التدريب وأخذ العينات بكفاءة.

**مشفرات إزالة الضوضاء التلقائية.** تتعلم مشفرات إزالة الضوضاء التلقائية إعادة بناء البيانات النظيفة من المدخلات المفسدة. يُظهر عملنا أنه يمكن تفسير نماذج الانتشار على أنها سلسلة من مشفرات إزالة الضوضاء التلقائية، كل منها مدرب لإزالة كمية محددة من الضوضاء. يساعد هذا الارتباط في شرح فعالية هدف التدريب المبسط لدينا.

**التوليد التدريجي.** استكشفت العديد من الأعمال السابقة التوليد التدريجي أو الهرمي، بما في ذلك Progressive GAN ونماذج VAE الهرمية. ومع ذلك، في هذه النماذج، يجب تصميم البنية التدريجية بشكل صريح في المعمارية. في المقابل، تُظهر نماذج الانتشار لدينا بشكل طبيعي توليداً من الخشن إلى الناعم كخاصية ناشئة لعملية الانتشار العكسي، دون الحاجة إلى تعديلات معمارية خاصة.

**الديناميكا الحرارية اللاتوازنية.** استمدت الصياغة الأصلية لنماذج الانتشار الاحتمالية الإلهام من الفيزياء الإحصائية اللاتوازنية. يمكن النظر إلى عملية الانتشار الأمامية على أنها زيادة تدريجية لإنتروبيا النظام، بينما تتعلم العملية العكسية تقليل الإنتروبيا وتوليد بيانات منظمة من الضوضاء.

**التطبيقات.** منذ تطوير نماذج الانتشار، تم تطبيقها على مجالات مختلفة بخلاف توليد الصور، بما في ذلك توليف الصوت، وتوليد الفيديو، وتصميم الجزيئات، وتوليد الأشكال ثلاثية الأبعاد. تجعل مرونة واستقرار نماذج الانتشار منها مناسبة للعديد من مهام النمذجة التوليدية.

---

### Translation Notes

- **Related model types:**
  - GANs (الشبكات التنافسية التوليدية)
  - VAEs (المشفرات التلقائية التباينية)
  - Normalizing flows (التدفقات التطبيعية)
  - Autoregressive models (النماذج الانحدارية الذاتية)
  - Energy-based models (النماذج القائمة على الطاقة)
  - Score-based models (النماذج القائمة على النقاط)

- **Key concepts:**
  - Mode collapse (انهيار النمط)
  - Mode coverage (تغطية الأنماط)
  - Score function (دالة النقاط)
  - Langevin dynamics (ديناميكيات لانجفين)
  - Non-equilibrium thermodynamics (الديناميكا الحرارية اللاتوازنية)
  - Entropy (إنتروبيا)
  - MCMC sampling (أخذ عينات MCMC)

- **Applications mentioned:** image generation, audio synthesis, video generation, molecular design, 3D shape generation

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.87
