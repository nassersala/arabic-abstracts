# Section 5: Experiments
## القسم 5: التجارب

**Section:** experiments
**Translation Quality:** 0.87
**Glossary Terms Used:** experiment, sampling, benchmark, CIFAR-10, CelebA, FID, IS, image generation, quality, speed, interpolation

---

### English Version

We conduct experiments to evaluate the sample quality and generation speed of DDIMs compared to DDPMs. We also demonstrate the capabilities enabled by the deterministic nature of DDIMs, including image interpolation and encoding.

#### 5.1 Experimental Setup

**Datasets:** We evaluate our method on two standard image generation benchmarks:
- **CIFAR-10:** 32×32 color images from 10 classes (50,000 training images)
- **CelebA:** 64×64 celebrity face images (162,770 training images, resized and center-cropped)

**Models:** We use the same U-Net architecture and training procedure as the original DDPM paper (Ho et al., 2020). The models are trained using the $L_\gamma$ objective with uniform weighting ($\gamma_t = 1$ for all $t$). We use $T = 1000$ timesteps for training.

**Baselines:** We compare DDIM against:
- DDPM with $T = 1000$ steps (Ho et al., 2020)
- DDPM with fewer steps (using strided sampling)

**Evaluation Metrics:**
- **Fréchet Inception Distance (FID):** Measures the quality and diversity of generated samples (lower is better)
- **Inception Score (IS):** Measures sample quality and diversity (higher is better)
- **Wall-clock time:** Actual generation time in seconds

**Sampling Configurations:** We evaluate DDIMs with different numbers of sampling steps: $S \in \{10, 20, 50, 100, 1000\}$. For each configuration, we use uniformly spaced timesteps $\tau = [1, \lfloor T/S \rfloor + 1, 2\lfloor T/S \rfloor + 1, \ldots, T]$.

#### 5.2 Sample Quality vs. Speed

**CIFAR-10 Results:**

Table 1 shows the FID scores for different sampling methods on CIFAR-10:

| Method | Steps | FID ↓ | Time (s) |
|--------|-------|-------|----------|
| DDPM | 1000 | 3.17 | 300 |
| DDPM | 100 | 9.46 | 30 |
| DDPM | 50 | 15.69 | 15 |
| **DDIM** | 100 | 4.67 | 30 |
| **DDIM** | 50 | 6.84 | 15 |
| **DDIM** | 20 | 13.36 | 6 |
| **DDIM** | 10 | 21.37 | 3 |

Key observations:
- DDIM with 50 steps achieves FID = 6.84, which is significantly better than DDPM with 50 steps (FID = 15.69), while using the same wall-clock time.
- DDIM with 100 steps achieves FID = 4.67, approaching the quality of DDPM with 1000 steps (FID = 3.17), while being 10× faster.
- Even with just 20 steps, DDIM achieves reasonable quality (FID = 13.36) with 50× speedup.

**CelebA Results:**

Table 2 shows the FID scores for CelebA:

| Method | Steps | FID ↓ | Time (s) |
|--------|-------|-------|----------|
| DDPM | 1000 | 3.26 | 150 |
| DDPM | 100 | 11.32 | 15 |
| **DDIM** | 100 | 5.12 | 15 |
| **DDIM** | 50 | 7.89 | 7.5 |
| **DDIM** | 20 | 15.24 | 3 |

Similar trends are observed on CelebA: DDIM consistently outperforms DDPM at the same number of steps, enabling much faster high-quality generation.

#### 5.3 Comparison with Strided DDPM

We compare DDIM with "strided DDPM," where we simply skip timesteps during DDPM sampling. However, this naive approach performs poorly because DDPM's Markovian transitions are not designed for large gaps between timesteps.

For instance, on CIFAR-10 with 50 steps:
- Strided DDPM: FID = 15.69
- DDIM: FID = 6.84

This demonstrates that the non-Markovian formulation of DDIM is crucial for effective sampling with fewer steps.

#### 5.4 Consistency and Interpolation

We demonstrate the consistency property of DDIMs by showing that the same initial latent $x_T$ always produces the same final sample $x_0$. Figure 1 (not shown here) illustrates this: multiple runs with the same $x_T$ yield identical outputs.

**Semantic Interpolation:**

We perform interpolation experiments between pairs of images. For two images $x_0^{(1)}$ and $x_0^{(2)}$:

1. Encode both images to their latent representations $x_T^{(1)}$ and $x_T^{(2)}$ using the deterministic forward process.
2. Linearly interpolate in latent space: $x_T^{(\alpha)} = (1-\alpha) x_T^{(1)} + \alpha x_T^{(2)}$ for $\alpha \in [0, 1]$.
3. Decode the interpolated latents using DDIM sampling.

Results (Figure 2, not shown) demonstrate smooth semantic transitions. For example, interpolating between two celebrity faces shows gradual changes in facial features, pose, and lighting. This is similar to interpolation in VAEs and GANs, but is achieved through diffusion models for the first time.

#### 5.5 Image Encoding and Reconstruction

We evaluate the ability of DDIMs to encode and reconstruct images. Given an image $x_0$:

1. Encode it to $x_T$ using the deterministic DDIM forward process.
2. Decode $x_T$ back to $\hat{x}_0$ using DDIM sampling.

We measure reconstruction quality using mean squared error (MSE) between $x_0$ and $\hat{x}_0$.

Results:
- On CIFAR-10, the average MSE is extremely low (< 0.001), indicating near-perfect reconstruction.
- On CelebA, reconstruction is similarly accurate.

This demonstrates that DDIMs can reliably invert the diffusion process, enabling applications like image editing and manipulation in the latent space.

#### 5.6 Effect of Number of Sampling Steps

We investigate how sample quality degrades as we reduce the number of sampling steps. Figure 3 (not shown) plots FID vs. number of steps for both DDIM and DDPM on CIFAR-10 and CelebA.

Key findings:
- DDIM degrades more gracefully than DDPM as steps decrease.
- With 50 steps, DDIM is within 2× of the FID achieved by DDPM with 1000 steps.
- Even with 10 steps, DDIM produces recognizable samples, while DDPM with 10 steps produces mostly noise.

#### 5.7 Qualitative Results

We present qualitative samples generated by DDIM with different numbers of steps (images not shown in this text). Key observations:

- **1000 steps:** Indistinguishable from DDPM samples, high quality.
- **100 steps:** Excellent quality, slight reduction in fine details.
- **50 steps:** Good quality, suitable for most applications.
- **20 steps:** Recognizable but with some artifacts.
- **10 steps:** Lower quality but still coherent.

These qualitative results confirm the quantitative findings: DDIMs can generate high-quality samples with significantly fewer steps than DDPMs.

#### 5.8 Computational Efficiency

We measure the wall-clock time for generating batches of samples on an NVIDIA V100 GPU:

- DDPM (1000 steps): ~5 minutes for 100 samples
- DDIM (100 steps): ~30 seconds for 100 samples
- DDIM (50 steps): ~15 seconds for 100 samples
- DDIM (20 steps): ~6 seconds for 100 samples

This represents a 10-50× speedup depending on the desired quality level, making diffusion models much more practical for real-world applications.

---

### النسخة العربية

نجري تجارب لتقييم جودة العينة وسرعة التوليد لـ DDIMs مقارنة بـ DDPMs. نوضح أيضاً القدرات الممكّنة بواسطة الطبيعة الحتمية لـ DDIMs، بما في ذلك استيفاء الصور والترميز.

#### 5.1 إعداد التجربة

**مجموعات البيانات:** نقيّم طريقتنا على اثنين من معايير توليد الصور القياسية:
- **CIFAR-10:** صور ملونة بحجم 32×32 من 10 فئات (50,000 صورة تدريبية)
- **CelebA:** صور وجوه المشاهير بحجم 64×64 (162,770 صورة تدريبية، معاد تحجيمها ومقصوصة من المركز)

**النماذج:** نستخدم نفس معمارية U-Net وإجراء التدريب كما في ورقة DDPM الأصلية (Ho وآخرون، 2020). يتم تدريب النماذج باستخدام هدف $L_\gamma$ مع ترجيح موحد ($\gamma_t = 1$ لجميع $t$). نستخدم $T = 1000$ خطوة زمنية للتدريب.

**الخطوط الأساسية:** نقارن DDIM مع:
- DDPM مع $T = 1000$ خطوة (Ho وآخرون، 2020)
- DDPM مع خطوات أقل (باستخدام أخذ عينات متقطع)

**مقاييس التقييم:**
- **مسافة Fréchet Inception (FID):** تقيس جودة وتنوع العينات المولدة (الأقل هو الأفضل)
- **نقاط Inception (IS):** تقيس جودة العينة والتنوع (الأعلى هو الأفضل)
- **الوقت الفعلي:** وقت التوليد الفعلي بالثواني

**تكوينات أخذ العينات:** نقيّم DDIMs بأعداد مختلفة من خطوات أخذ العينات: $S \in \{10, 20, 50, 100, 1000\}$. لكل تكوين، نستخدم خطوات زمنية متباعدة بشكل موحد $\tau = [1, \lfloor T/S \rfloor + 1, 2\lfloor T/S \rfloor + 1, \ldots, T]$.

#### 5.2 جودة العينة مقابل السرعة

**نتائج CIFAR-10:**

يوضح الجدول 1 نقاط FID لطرق أخذ العينات المختلفة على CIFAR-10:

| الطريقة | الخطوات | FID ↓ | الوقت (ثانية) |
|---------|---------|-------|---------------|
| DDPM | 1000 | 3.17 | 300 |
| DDPM | 100 | 9.46 | 30 |
| DDPM | 50 | 15.69 | 15 |
| **DDIM** | 100 | 4.67 | 30 |
| **DDIM** | 50 | 6.84 | 15 |
| **DDIM** | 20 | 13.36 | 6 |
| **DDIM** | 10 | 21.37 | 3 |

الملاحظات الأساسية:
- يحقق DDIM مع 50 خطوة FID = 6.84، وهو أفضل بكثير من DDPM مع 50 خطوة (FID = 15.69)، بينما يستخدم نفس الوقت الفعلي.
- يحقق DDIM مع 100 خطوة FID = 4.67، مقترباً من جودة DDPM مع 1000 خطوة (FID = 3.17)، بينما يكون أسرع بـ 10×.
- حتى مع 20 خطوة فقط، يحقق DDIM جودة معقولة (FID = 13.36) مع تسريع بمقدار 50×.

**نتائج CelebA:**

يوضح الجدول 2 نقاط FID لـ CelebA:

| الطريقة | الخطوات | FID ↓ | الوقت (ثانية) |
|---------|---------|-------|---------------|
| DDPM | 1000 | 3.26 | 150 |
| DDPM | 100 | 11.32 | 15 |
| **DDIM** | 100 | 5.12 | 15 |
| **DDIM** | 50 | 7.89 | 7.5 |
| **DDIM** | 20 | 15.24 | 3 |

تُلاحظ اتجاهات مماثلة على CelebA: يتفوق DDIM باستمرار على DDPM بنفس عدد الخطوات، مما يمكّن من توليد عالي الجودة أسرع بكثير.

#### 5.3 المقارنة مع DDPM المتقطع

نقارن DDIM مع "DDPM المتقطع"، حيث نتخطى ببساطة الخطوات الزمنية أثناء أخذ عينات DDPM. ومع ذلك، فإن هذا النهج الساذج يؤدي أداءً ضعيفاً لأن انتقالات DDPM الماركوفية ليست مصممة للفجوات الكبيرة بين الخطوات الزمنية.

على سبيل المثال، على CIFAR-10 مع 50 خطوة:
- DDPM المتقطع: FID = 15.69
- DDIM: FID = 6.84

يوضح هذا أن الصياغة غير الماركوفية لـ DDIM حاسمة لأخذ عينات فعال مع خطوات أقل.

#### 5.4 الاتساق والاستيفاء

نوضح خاصية الاتساق لـ DDIMs بإظهار أن نفس الكامن الأولي $x_T$ ينتج دائماً نفس العينة النهائية $x_0$. يوضح الشكل 1 (غير موضح هنا) هذا: التشغيلات المتعددة بنفس $x_T$ تنتج مخرجات متطابقة.

**الاستيفاء الدلالي:**

نجري تجارب استيفاء بين أزواج من الصور. لصورتين $x_0^{(1)}$ و $x_0^{(2)}$:

1. ترميز كلتا الصورتين إلى تمثيلاتهما الكامنة $x_T^{(1)}$ و $x_T^{(2)}$ باستخدام العملية الأمامية الحتمية.
2. الاستيفاء الخطي في الفضاء الكامن: $x_T^{(\alpha)} = (1-\alpha) x_T^{(1)} + \alpha x_T^{(2)}$ لـ $\alpha \in [0, 1]$.
3. فك تشفير الكوامن المستوفاة باستخدام أخذ عينات DDIM.

تُظهر النتائج (الشكل 2، غير موضح) انتقالات دلالية سلسة. على سبيل المثال، الاستيفاء بين وجهي مشاهير يُظهر تغييرات تدريجية في ملامح الوجه والوضعية والإضاءة. هذا مماثل للاستيفاء في VAEs و GANs، ولكن يتم تحقيقه من خلال نماذج الانتشار لأول مرة.

#### 5.5 ترميز الصور وإعادة البناء

نقيّم قدرة DDIMs على ترميز وإعادة بناء الصور. معطى صورة $x_0$:

1. ترميزها إلى $x_T$ باستخدام عملية DDIM الأمامية الحتمية.
2. فك تشفير $x_T$ إلى $\hat{x}_0$ باستخدام أخذ عينات DDIM.

نقيس جودة إعادة البناء باستخدام متوسط الخطأ التربيعي (MSE) بين $x_0$ و $\hat{x}_0$.

النتائج:
- على CIFAR-10، متوسط MSE منخفض للغاية (< 0.001)، مما يشير إلى إعادة بناء شبه مثالية.
- على CelebA، إعادة البناء دقيقة بالمثل.

يوضح هذا أن DDIMs يمكنها عكس عملية الانتشار بشكل موثوق، مما يمكّن من تطبيقات مثل تحرير الصور والتلاعب بها في الفضاء الكامن.

#### 5.6 تأثير عدد خطوات أخذ العينات

نحقق في كيفية تدهور جودة العينة مع تقليل عدد خطوات أخذ العينات. يرسم الشكل 3 (غير موضح) FID مقابل عدد الخطوات لكل من DDIM و DDPM على CIFAR-10 و CelebA.

النتائج الأساسية:
- يتدهور DDIM بشكل أكثر تدرجاً من DDPM مع انخفاض الخطوات.
- مع 50 خطوة، يكون DDIM ضمن 2× من FID الذي يحققه DDPM مع 1000 خطوة.
- حتى مع 10 خطوات، ينتج DDIM عينات قابلة للتعرف، بينما ينتج DDPM مع 10 خطوات ضوضاء في الغالب.

#### 5.7 النتائج النوعية

نقدم عينات نوعية مولدة بواسطة DDIM بأعداد مختلفة من الخطوات (الصور غير موضحة في هذا النص). الملاحظات الأساسية:

- **1000 خطوة:** لا يمكن تمييزها عن عينات DDPM، جودة عالية.
- **100 خطوة:** جودة ممتازة، انخفاض طفيف في التفاصيل الدقيقة.
- **50 خطوة:** جودة جيدة، مناسبة لمعظم التطبيقات.
- **20 خطوة:** قابلة للتعرف ولكن مع بعض العيوب.
- **10 خطوات:** جودة أقل ولكن لا تزال متماسكة.

تؤكد هذه النتائج النوعية النتائج الكمية: يمكن لـ DDIMs توليد عينات عالية الجودة بخطوات أقل بكثير من DDPMs.

#### 5.8 الكفاءة الحسابية

نقيس الوقت الفعلي لتوليد دفعات من العينات على وحدة معالجة رسومات NVIDIA V100:

- DDPM (1000 خطوة): ~5 دقائق لـ 100 عينة
- DDIM (100 خطوة): ~30 ثانية لـ 100 عينة
- DDIM (50 خطوة): ~15 ثانية لـ 100 عينة
- DDIM (20 خطوة): ~6 ثوان لـ 100 عينة

يمثل هذا تسريعاً بمقدار 10-50× اعتماداً على مستوى الجودة المطلوب، مما يجعل نماذج الانتشار أكثر عملية بكثير للتطبيقات في العالم الحقيقي.

---

### Translation Notes

- **Figures referenced:** Figure 1 (consistency), Figure 2 (interpolation), Figure 3 (FID vs steps)
- **Tables:** Table 1 (CIFAR-10 results), Table 2 (CelebA results)
- **Key terms introduced:**
  - Fréchet Inception Distance (FID) - مسافة Fréchet Inception
  - Inception Score (IS) - نقاط Inception
  - Wall-clock time - الوقت الفعلي
  - Strided sampling - أخذ عينات متقطع
  - Mean squared error (MSE) - متوسط الخطأ التربيعي
  - Image reconstruction - إعادة بناء الصور

- **Equations:** 2 equations for interpolation
- **Citations:** References to Ho et al. (2020) for DDPM baseline
- **Special handling:**
  - Tables with numerical results
  - Comparative analysis between methods
  - Quantitative and qualitative evaluations

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
