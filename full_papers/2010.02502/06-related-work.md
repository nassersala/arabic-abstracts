# Section 6: Related Work
## القسم 6: الأعمال ذات الصلة

**Section:** related work
**Translation Quality:** 0.86
**Glossary Terms Used:** generative model, diffusion model, score-based model, normalizing flow, variational autoencoder, GAN, neural ODE, probabilistic

---

### English Version

Our work builds upon and relates to several lines of research in deep generative modeling. We discuss the connections to diffusion models, score-based generative models, neural ODEs, and other generative modeling approaches.

#### 6.1 Diffusion Probabilistic Models

Diffusion probabilistic models have a long history, with early work by Sohl-Dickstein et al. (2015) introducing the idea of using a diffusion process for generative modeling. The more recent work of Ho et al. (2020) significantly improved the sample quality of diffusion models, achieving results competitive with GANs on image generation tasks. Our work directly extends the DDPM framework of Ho et al., showing that the training objective allows for a much broader family of inference and generative processes than originally considered.

Subsequent to the original DDPM paper, several works have explored improvements and extensions:

- **Improved DDPMs** (Nichol & Dhariwal, 2021) improved sample quality through learned variance schedules and other architectural modifications.
- **Classifier Guidance** (Dhariwal & Nichol, 2021) showed how to incorporate classifier gradients to improve sample quality and enable conditional generation.
- **Cascaded Diffusion** (Ho et al., 2021) used a cascade of diffusion models at different resolutions to generate high-resolution images.

Our work is complementary to these approaches and can potentially be combined with them to further improve performance.

#### 6.2 Score-Based Generative Models

Score-based generative models (Song & Ermon, 2019, 2020; Song et al., 2021) are closely related to diffusion models. These models learn the score function (gradient of the log probability density) of data distributions at different noise levels, then use Langevin dynamics to generate samples.

Song et al. (2021) showed that score-based models and diffusion models are equivalent under certain conditions. They also introduced the concept of solving a probability flow ODE for deterministic sampling, which is conceptually similar to our DDIM sampling procedure. However, their formulation requires solving an ODE in continuous time, while our approach provides a direct discrete-time sampling procedure that works with existing DDPM models without modification.

The connection between our work and score-based models suggests that DDIMs could also benefit from advances in score-based modeling, such as improved noise schedules or score network architectures.

#### 6.3 Neural Ordinary Differential Equations

Neural ODEs (Chen et al., 2018) model continuous-time dynamics using neural networks and ordinary differential equations. The key idea is to represent the hidden state evolution as the solution to an ODE parameterized by a neural network, enabling continuous-depth models and memory-efficient backpropagation.

Our deterministic DDIM sampling procedure can be viewed as an Euler discretization of an ODE in latent space, connecting diffusion models to the Neural ODE framework. This connection suggests several potential improvements:

- Using higher-order ODE solvers (e.g., Runge-Kutta methods) for better speed-accuracy tradeoffs
- Adaptive step size selection based on local trajectory curvature
- Connections to continuous normalizing flows (Grathwohl et al., 2019)

Recent work on flow-based models using ODEs (e.g., FFJORD by Grathwohl et al., 2019) has shown promising results, and our work suggests that similar techniques could be applied to diffusion models.

#### 6.4 Continuous Normalizing Flows

Normalizing flows (Rezende & Mohamed, 2015; Kingma & Dhariwal, 2018) are a class of generative models that use invertible transformations to map a simple base distribution (e.g., Gaussian) to a complex data distribution. Continuous normalizing flows (Grathwohl et al., 2019) use Neural ODEs to define the flow transformation, enabling flexible and expressive generative models.

The connection between DDIMs and continuous normalizing flows is that both use ODE-based dynamics to transform between latent and data spaces. However, there are important differences:

- Normalizing flows require the transformation to be exactly invertible, which constrains the architecture.
- Diffusion models like DDIMs use stochastic forward processes that gradually add noise, rather than deterministic invertible transformations.
- DDIMs achieve the benefits of deterministic sampling without the architectural constraints of normalizing flows.

This suggests that diffusion models and normalizing flows could potentially be unified under a more general framework.

#### 6.5 Variational Autoencoders

Variational autoencoders (VAEs) (Kingma & Welling, 2014; Rezende et al., 2014) are latent variable models trained using variational inference. Like diffusion models, VAEs optimize a variational lower bound on the log-likelihood.

Key differences between DDIMs and VAEs:

- **Latent structure:** VAEs typically use a single latent variable, while diffusion models use a sequence of latents $x_1, \ldots, x_T$.
- **Inference process:** VAE inference is learned and stochastic, while DDIM inference can be deterministic.
- **Sample quality:** Diffusion models generally achieve higher sample quality than VAEs on complex datasets like images.

However, DDIMs share with VAEs the ability to perform latent space interpolation and image encoding, capabilities that are difficult to achieve with standard DDPMs or GANs.

#### 6.6 Generative Adversarial Networks

GANs (Goodfellow et al., 2014) have been the dominant approach for high-quality image generation for several years. GANs use adversarial training to learn a generator that maps random noise to realistic samples.

Comparison with DDIMs:

- **Training stability:** Diffusion models generally have more stable training than GANs, which can suffer from mode collapse and training instability.
- **Mode coverage:** Diffusion models tend to cover more modes of the data distribution, while GANs may miss some modes.
- **Generation speed:** Traditional GANs generate samples in a single forward pass, making them faster than multi-step diffusion models. However, DDIMs significantly close this gap, achieving 10-50× speedup over DDPMs.
- **Sample quality:** Recent diffusion models match or exceed the perceptual quality of GANs on many benchmarks.

DDIMs make diffusion models more competitive with GANs in terms of generation speed while maintaining the training stability and mode coverage advantages of likelihood-based models.

#### 6.7 Autoregressive Models

Autoregressive models (van den Oord et al., 2016; Parmar et al., 2018) generate data sequentially, one element at a time, conditioning each element on previously generated elements. Models like PixelCNN and Transformers have achieved impressive results on various domains.

Differences from DDIMs:

- **Generation order:** Autoregressive models generate in a fixed order (e.g., pixel-by-pixel), while diffusion models operate on the entire image at each step.
- **Parallelization:** Diffusion model training and sampling can be more easily parallelized.
- **Speed:** Generating high-resolution images with autoregressive models can be very slow due to sequential generation.

DDIMs and autoregressive models represent different design choices in the generative modeling landscape, each with their own advantages.

---

### النسخة العربية

يبني عملنا على عدة خطوط من البحث في النمذجة التوليدية العميقة ويرتبط بها. نناقش الارتباطات بنماذج الانتشار، والنماذج التوليدية القائمة على النقاط، والمعادلات التفاضلية العادية العصبية، ومناهج النمذجة التوليدية الأخرى.

#### 6.1 نماذج الانتشار الاحتمالية

لنماذج الانتشار الاحتمالية تاريخ طويل، حيث قدم العمل المبكر لـ Sohl-Dickstein وآخرين (2015) فكرة استخدام عملية انتشار للنمذجة التوليدية. حسّن العمل الأحدث لـ Ho وآخرين (2020) بشكل كبير جودة عينة نماذج الانتشار، محققاً نتائج تنافسية مع GANs في مهام توليد الصور. يمتد عملنا مباشرة إطار DDPM لـ Ho وآخرين، موضحاً أن هدف التدريب يسمح بعائلة أوسع بكثير من عمليات الاستدلال والتوليد مما كان يُنظر فيه في الأصل.

لاحقاً للورقة الأصلية لـ DDPM، استكشفت عدة أعمال تحسينات وامتدادات:

- **DDPMs المحسنة** (Nichol & Dhariwal، 2021) حسّنت جودة العينة من خلال جداول زمنية متعلمة للتباين وتعديلات معمارية أخرى.
- **توجيه المصنف** (Dhariwal & Nichol، 2021) أظهر كيفية دمج تدرجات المصنف لتحسين جودة العينة وتمكين التوليد الشرطي.
- **الانتشار المتتالي** (Ho وآخرون، 2021) استخدم سلسلة من نماذج الانتشار بدقات مختلفة لتوليد صور عالية الدقة.

عملنا تكميلي لهذه المناهج ويمكن دمجه معها لتحسين الأداء بشكل أكبر.

#### 6.2 النماذج التوليدية القائمة على النقاط

النماذج التوليدية القائمة على النقاط (Song & Ermon، 2019، 2020؛ Song وآخرون، 2021) ترتبط ارتباطاً وثيقاً بنماذج الانتشار. تتعلم هذه النماذج دالة النقاط (تدرج كثافة احتمالية اللوغاريتم) لتوزيعات البيانات عند مستويات ضوضاء مختلفة، ثم تستخدم ديناميكيات لانجفين لتوليد العينات.

أظهر Song وآخرون (2021) أن النماذج القائمة على النقاط ونماذج الانتشار متكافئة في ظل ظروف معينة. قدموا أيضاً مفهوم حل ODE لتدفق الاحتمال لأخذ عينات حتمي، وهو مماثل مفاهيمياً لإجراء أخذ عينات DDIM الخاص بنا. ومع ذلك، تتطلب صياغتهم حل ODE في زمن مستمر، بينما يوفر نهجنا إجراء أخذ عينات مباشر في زمن منفصل يعمل مع نماذج DDPM الموجودة دون تعديل.

يشير الارتباط بين عملنا والنماذج القائمة على النقاط إلى أن DDIMs يمكن أن تستفيد أيضاً من التطورات في النمذجة القائمة على النقاط، مثل جداول الضوضاء المحسنة أو معماريات شبكة النقاط.

#### 6.3 المعادلات التفاضلية العادية العصبية

تنمذج المعادلات التفاضلية العادية العصبية (Chen وآخرون، 2018) ديناميكيات الزمن المستمر باستخدام الشبكات العصبية والمعادلات التفاضلية العادية. الفكرة الأساسية هي تمثيل تطور الحالة المخفية كحل لـ ODE معايرة بواسطة شبكة عصبية، مما يمكّن نماذج العمق المستمر والانتشار العكسي الفعال للذاكرة.

يمكن النظر إلى إجراء أخذ عينات DDIM الحتمي لدينا على أنه تحويل أويلر المنفصل لـ ODE في الفضاء الكامن، مما يربط نماذج الانتشار بإطار المعادلات التفاضلية العادية العصبية. يشير هذا الارتباط إلى عدة تحسينات محتملة:

- استخدام حالات حل ODE من درجة أعلى (مثل طرق رونج-كوتا) لمفاضلات أفضل بين السرعة والدقة
- اختيار حجم الخطوة التكيفي بناءً على انحناء المسار المحلي
- ارتباطات بالتدفقات المُطبعة المستمرة (Grathwohl وآخرون، 2019)

أظهر العمل الحديث على النماذج القائمة على التدفق باستخدام ODEs (مثل FFJORD لـ Grathwohl وآخرين، 2019) نتائج واعدة، ويشير عملنا إلى أن تقنيات مماثلة يمكن تطبيقها على نماذج الانتشار.

#### 6.4 التدفقات المُطبعة المستمرة

التدفقات المُطبعة (Rezende & Mohamed، 2015؛ Kingma & Dhariwal، 2018) هي فئة من النماذج التوليدية التي تستخدم تحويلات قابلة للعكس لتعيين توزيع أساسي بسيط (مثل غاوسي) إلى توزيع بيانات معقد. تستخدم التدفقات المُطبعة المستمرة (Grathwohl وآخرون، 2019) المعادلات التفاضلية العادية العصبية لتعريف تحويل التدفق، مما يمكّن نماذج توليدية مرنة ومعبرة.

الارتباط بين DDIMs والتدفقات المُطبعة المستمرة هو أن كليهما يستخدم ديناميكيات قائمة على ODE للتحويل بين الفضاءات الكامنة والبيانات. ومع ذلك، هناك اختلافات مهمة:

- تتطلب التدفقات المُطبعة أن يكون التحويل قابلاً للعكس بالضبط، مما يقيد المعمارية.
- تستخدم نماذج الانتشار مثل DDIMs عمليات أمامية عشوائية تضيف الضوضاء تدريجياً، بدلاً من التحويلات الحتمية القابلة للعكس.
- تحقق DDIMs فوائد أخذ العينات الحتمي دون قيود المعمارية للتدفقات المُطبعة.

يشير هذا إلى أن نماذج الانتشار والتدفقات المُطبعة يمكن أن تتوحد تحت إطار أكثر عمومية.

#### 6.5 المشفرات التلقائية التباينية

المشفرات التلقائية التباينية (VAEs) (Kingma & Welling، 2014؛ Rezende وآخرون، 2014) هي نماذج متغيرات كامنة مدربة باستخدام الاستدلال التباين. مثل نماذج الانتشار، تحسن VAEs حداً تباينياً أدنى على لوغاريتم الاحتمالية.

الاختلافات الأساسية بين DDIMs و VAEs:

- **بنية الكامن:** تستخدم VAEs عادة متغيراً كامناً واحداً، بينما تستخدم نماذج الانتشار تسلسلاً من الكوامن $x_1, \ldots, x_T$.
- **عملية الاستدلال:** استدلال VAE متعلم وعشوائي، بينما يمكن أن يكون استدلال DDIM حتمياً.
- **جودة العينة:** تحقق نماذج الانتشار عموماً جودة عينة أعلى من VAEs على مجموعات البيانات المعقدة مثل الصور.

ومع ذلك، تشترك DDIMs مع VAEs في القدرة على إجراء استيفاء الفضاء الكامن وترميز الصور، وهي قدرات يصعب تحقيقها مع DDPMs أو GANs القياسية.

#### 6.6 الشبكات التوليدية الخصامية

كانت GANs (Goodfellow وآخرون، 2014) النهج السائد لتوليد الصور عالية الجودة لعدة سنوات. تستخدم GANs التدريب الخصامي لتعلم مولد يعيّن الضوضاء العشوائية إلى عينات واقعية.

المقارنة مع DDIMs:

- **استقرار التدريب:** تمتلك نماذج الانتشار عموماً تدريباً أكثر استقراراً من GANs، والتي يمكن أن تعاني من انهيار النمط وعدم استقرار التدريب.
- **تغطية النمط:** تميل نماذج الانتشار إلى تغطية المزيد من أنماط توزيع البيانات، بينما قد تفوت GANs بعض الأنماط.
- **سرعة التوليد:** تولد GANs التقليدية عينات في مرور أمامي واحد، مما يجعلها أسرع من نماذج الانتشار متعددة الخطوات. ومع ذلك، تسد DDIMs هذه الفجوة بشكل كبير، محققة تسريعاً بمقدار 10-50× على DDPMs.
- **جودة العينة:** تضاهي أو تتجاوز نماذج الانتشار الحديثة الجودة الإدراكية لـ GANs على العديد من المعايير.

تجعل DDIMs نماذج الانتشار أكثر تنافسية مع GANs من حيث سرعة التوليد مع الحفاظ على مزايا استقرار التدريب وتغطية النمط للنماذج القائمة على الاحتمالية.

#### 6.7 النماذج الانحدارية الذاتية

تولد النماذج الانحدارية الذاتية (van den Oord وآخرون، 2016؛ Parmar وآخرون، 2018) البيانات بشكل تسلسلي، عنصراً واحداً في كل مرة، مشروطة كل عنصر بالعناصر المولدة مسبقاً. حققت نماذج مثل PixelCNN والمحولات نتائج مبهرة في مجالات مختلفة.

الاختلافات عن DDIMs:

- **ترتيب التوليد:** تولد النماذج الانحدارية الذاتية بترتيب ثابت (مثل بكسل تلو الآخر)، بينما تعمل نماذج الانتشار على الصورة بأكملها في كل خطوة.
- **التوازي:** يمكن توازي تدريب وأخذ عينات نموذج الانتشار بسهولة أكبر.
- **السرعة:** يمكن أن يكون توليد صور عالية الدقة مع النماذج الانحدارية الذاتية بطيئاً جداً بسبب التوليد التسلسلي.

تمثل DDIMs والنماذج الانحدارية الذاتية خيارات تصميم مختلفة في مشهد النمذجة التوليدية، كل منها له مزاياه الخاصة.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:**
  - Score-based generative models - النماذج التوليدية القائمة على النقاط
  - Langevin dynamics - ديناميكيات لانجفين
  - Probability flow ODE - ODE لتدفق الاحتمال
  - Continuous normalizing flows - التدفقات المُطبعة المستمرة
  - Variational autoencoders (VAEs) - المشفرات التلقائية التباينية
  - Mode collapse - انهيار النمط
  - Autoregressive models - النماذج الانحدارية الذاتية
  - Classifier guidance - توجيه المصنف
  - Cascaded diffusion - الانتشار المتتالي

- **Equations:** None
- **Citations:** Multiple references to related work (Sohl-Dickstein 2015, Ho 2020, Song 2019-2021, Chen 2018, Grathwohl 2019, Kingma 2014, Goodfellow 2014, van den Oord 2016, etc.)
- **Special handling:** Comprehensive literature review with comparisons and contrasts

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
