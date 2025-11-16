# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** diffusion model, denoising, generative, sampling, training, Markov chain, probabilistic, latent space, adversarial training, image generation

---

### English Version

Generative modeling is a fundamental task in unsupervised learning, where the goal is to learn a distribution that best represents a dataset. Recent advances in likelihood-based generative models have achieved impressive results on high-dimensional data such as images. Among these, denoising diffusion probabilistic models (DDPMs) have demonstrated remarkable performance in generating high-quality samples without adversarial training, matching or surpassing the perceptual quality of state-of-the-art generative adversarial networks (GANs) while maintaining mode coverage and having a more stable training procedure.

DDPMs belong to a class of latent variable models that are inspired by considerations from non-equilibrium thermodynamics. They work by gradually adding noise to data through a fixed forward diffusion process, and then learning to reverse this process to generate samples. The forward process is typically chosen to be a Markov chain that gradually adds Gaussian noise to the data according to a variance schedule, until the signal is completely destroyed. The generative model then learns to reverse this process, starting from pure noise and gradually denoising to produce a sample from the data distribution.

Despite their impressive sample quality, DDPMs have a significant limitation: sampling is very slow. To generate a single sample, DDPMs require simulating a Markov chain for thousands of steps. For example, on image datasets like CIFAR-10 and CelebA, the original DDPM paper uses 1000 steps, making sampling much slower than GANs, which can generate samples in a single forward pass. This computational inefficiency is a major obstacle to the widespread adoption of DDPMs for applications where generation speed matters.

In this paper, we present denoising diffusion implicit models (DDIMs), a more efficient class of iterative implicit probabilistic models with the same training procedure as DDPMs. Our key observation is that the DDPM objective only depends on the marginal distributions $q(x_t|x_0)$ at each timestep $t$, but not directly on the joint distribution $q(x_{1:T}|x_0)$ of the forward process. This insight enables us to construct a class of non-Markovian forward processes that lead to the same training objective as DDPMs, but with a reverse generative process that can be much faster to sample from.

We show that by choosing a particular family of non-Markovian forward processes, we can derive a generative model that allows us to trade off sample quality for sampling speed. In the deterministic limit, our model becomes a fully deterministic generative process, which we call the denoising diffusion implicit model (DDIM). This deterministic process can be interpreted as solving an ordinary differential equation (ODE) in the latent space, providing a connection to recent work on Neural ODEs and continuous normalizing flows.

Our contributions can be summarized as follows:

1. We propose a class of non-Markovian forward processes that share the same surrogate objective as DDPMs, allowing us to use pre-trained DDPM models without retraining.

2. We derive a corresponding family of generative sampling processes, including a deterministic variant (DDIM), that can generate high-quality samples much faster than DDPMs.

3. We empirically demonstrate that DDIMs can produce samples of comparable quality to DDPMs while being 10× to 50× faster in terms of wall-clock time on image generation tasks.

4. We show that DDIMs enable meaningful latent space interpolation and image encoding, capabilities that are not possible with stochastic DDPMs due to their Markovian nature.

5. We establish connections between DDIMs and Neural ODEs, providing theoretical insights into the deterministic sampling procedure.

The rest of the paper is organized as follows: Section 2 reviews the background on DDPMs and variational inference. Section 3 presents our generalization to non-Markovian forward processes and derives the corresponding variational bound. Section 4 describes the DDIM sampling procedure and its deterministic limit. Section 5 presents experimental results on image generation benchmarks. Section 6 discusses related work, and Section 7 concludes.

---

### النسخة العربية

النمذجة التوليدية هي مهمة أساسية في التعلم غير الموجه، حيث يتمثل الهدف في تعلم توزيع يمثل مجموعة البيانات على أفضل وجه. حققت التطورات الحديثة في النماذج التوليدية القائمة على الاحتمالية نتائج مبهرة على البيانات عالية الأبعاد مثل الصور. من بين هذه النماذج، أظهرت نماذج الانتشار الاحتمالية لإزالة الضوضاء (DDPMs) أداءً ملحوظاً في توليد عينات عالية الجودة دون تدريب خصامي، حيث تضاهي أو تتفوق على الجودة الإدراكية لأحدث الشبكات التوليدية الخصامية (GANs) مع الحفاظ على تغطية الأنماط ووجود إجراء تدريب أكثر استقراراً.

تنتمي DDPMs إلى فئة من نماذج المتغيرات الكامنة المستوحاة من اعتبارات الديناميكا الحرارية في حالة عدم التوازن. تعمل هذه النماذج عن طريق إضافة الضوضاء تدريجياً إلى البيانات من خلال عملية انتشار أمامية ثابتة، ثم تعلم عكس هذه العملية لتوليد العينات. عادةً ما يتم اختيار العملية الأمامية لتكون سلسلة ماركوف تضيف تدريجياً ضوضاء غاوسية إلى البيانات وفقاً لجدول زمني للتباين، حتى يتم تدمير الإشارة بالكامل. يتعلم النموذج التوليدي بعد ذلك عكس هذه العملية، بدءاً من الضوضاء النقية والإزالة التدريجية للضوضاء لإنتاج عينة من توزيع البيانات.

على الرغم من جودة العينات المبهرة، تعاني DDPMs من قيد كبير: أخذ العينات بطيء جداً. لتوليد عينة واحدة، تتطلب DDPMs محاكاة سلسلة ماركوف لآلاف الخطوات. على سبيل المثال، في مجموعات بيانات الصور مثل CIFAR-10 وCelebA، تستخدم ورقة DDPM الأصلية 1000 خطوة، مما يجعل أخذ العينات أبطأ بكثير من GANs، التي يمكنها توليد العينات في مرور أمامي واحد. هذه الكفاءة الحسابية المنخفضة هي عقبة رئيسية أمام الاعتماد الواسع النطاق لـ DDPMs في التطبيقات التي تهم فيها سرعة التوليد.

في هذه الورقة، نقدم نماذج الانتشار الضمنية لإزالة الضوضاء (DDIMs)، وهي فئة أكثر كفاءة من النماذج الاحتمالية الضمنية التكرارية بنفس إجراء التدريب كما في DDPMs. ملاحظتنا الأساسية هي أن هدف DDPM يعتمد فقط على التوزيعات الهامشية $q(x_t|x_0)$ عند كل خطوة زمنية $t$، ولكن ليس مباشرة على التوزيع المشترك $q(x_{1:T}|x_0)$ للعملية الأمامية. تمكننا هذه الرؤية من بناء فئة من عمليات الانتشار الأمامية غير الماركوفية التي تؤدي إلى نفس هدف التدريب كما في DDPMs، ولكن مع عملية توليدية عكسية يمكن أن تكون أسرع بكثير في أخذ العينات منها.

نُظهر أنه باختيار عائلة معينة من عمليات الانتشار الأمامية غير الماركوفية، يمكننا اشتقاق نموذج توليدي يسمح لنا بالمفاضلة بين جودة العينة وسرعة أخذ العينات. في الحد الحتمي، يصبح نموذجنا عملية توليدية حتمية بالكامل، نسميها نموذج الانتشار الضمني لإزالة الضوضاء (DDIM). يمكن تفسير هذه العملية الحتمية على أنها حل لمعادلة تفاضلية عادية (ODE) في الفضاء الكامن، مما يوفر ارتباطاً بالأعمال الحديثة حول المعادلات التفاضلية العادية العصبية والتدفقات المُطبعة المستمرة.

يمكن تلخيص مساهماتنا على النحو التالي:

1. نقترح فئة من عمليات الانتشار الأمامية غير الماركوفية التي تشترك في نفس الهدف البديل مع DDPMs، مما يسمح لنا باستخدام نماذج DDPM المدربة مسبقاً دون إعادة التدريب.

2. نشتق عائلة مقابلة من عمليات أخذ العينات التوليدية، بما في ذلك متغير حتمي (DDIM)، يمكنه توليد عينات عالية الجودة أسرع بكثير من DDPMs.

3. نوضح تجريبياً أن DDIMs يمكن أن تنتج عينات ذات جودة مماثلة لـ DDPMs بينما تكون أسرع بمقدار 10× إلى 50× من حيث الوقت الفعلي في مهام توليد الصور.

4. نُظهر أن DDIMs تمكّن من استيفاء الفضاء الكامن ذي المعنى وترميز الصور، وهي قدرات غير ممكنة مع DDPMs العشوائية بسبب طبيعتها الماركوفية.

5. نؤسس روابط بين DDIMs والمعادلات التفاضلية العادية العصبية، مما يوفر رؤى نظرية حول إجراء أخذ العينات الحتمي.

يتم تنظيم بقية الورقة على النحو التالي: يراجع القسم 2 الخلفية حول DDPMs والاستدلال التباين. يقدم القسم 3 تعميمنا لعمليات الانتشار الأمامية غير الماركوفية ويشتق الحد التبايني المقابل. يصف القسم 4 إجراء أخذ العينات DDIM وحده الحتمي. يقدم القسم 5 النتائج التجريبية على معايير توليد الصور. يناقش القسم 6 الأعمال ذات الصلة، ويختتم القسم 7.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:**
  - Denoising diffusion implicit models (DDIMs) - نماذج الانتشار الضمنية لإزالة الضوضاء
  - Denoising diffusion probabilistic models (DDPMs) - نماذج الانتشار الاحتمالية لإزالة الضوضاء
  - Non-Markovian forward processes - عمليات الانتشار الأمامية غير الماركوفية
  - Marginal distributions - التوزيعات الهامشية
  - Ordinary differential equation (ODE) - معادلة تفاضلية عادية
  - Continuous normalizing flows - التدفقات المُطبعة المستمرة
  - Neural ODEs - المعادلات التفاضلية العادية العصبية

- **Equations:** 2 inline equations referencing marginal and joint distributions
- **Citations:** References to DDPMs, GANs, Neural ODEs, normalizing flows
- **Special handling:** Mathematical notation preserved in LaTeX format

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.89
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
