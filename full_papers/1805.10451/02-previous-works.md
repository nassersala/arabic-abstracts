# Section 2: Previous Works
## القسم 2: الأعمال السابقة

**Section:** related-work
**Translation Quality:** 0.86
**Glossary Terms Used:** autoencoder, deep learning, encoder, decoder, RBM, PCA, dimensionality reduction, sparse, denoising, contractive, VAE, GAN, generative model

---

### English Version

The literature of autoencoders is vast, in the following we only briefly review the most related ones as representatives.

**Traditional Autoencoders (AE)** The traditional autoencoder (AE) framework first appeared in [2], which was initially proposed to achieve dimensionality reduction. [2] use linear autoencoder to compare with PCA. With the same purpose, [14] proposed a deep autoencoder architecture, where the encoder and the decoder are multi-layer deep networks. Due to non-convexity of deep networks, they are easy to converge to poor local optima with random initialized weights. To solve this problem, [14] used restricted Boltzmann machines (RBMs) to pre-train the model layer by layer before fine-tuning. Later [4] used traditional AEs to pre-train each layer and got similar results.

**Sparse Encoders** The traditional AE uses bottleneck structure, the width of the middle later is less than that of the input layer. The sparse autoencoder (SAE) was introduced in [10], which uses over-complete latent space, that is the middle layer is wider than the input layer. Sparse autoencoders [19, 21, 20] were proposed.

Extra regularizations for sparsity was added in the object function, such as the KL divergence between the bottle neck layer output distribution and the desired distribution [18]. SAEs are used in a lot of classification tasks [31, 26], and feature tranfer learning [8].

**Denoising Autoencoder (DAE)** [30, 29] proposed denoising autoencoder (DAE) in order to improve the robustness from the corrupted input. DAEs add regularizations on inputs to reconstruct a "repaired" input from a corrupted version. Stacked denoising autoencoders (SDAEs) is constructed by stacking multiple layers of DAEs, where each layer is pre-trained by DAEs. The DAE/SDAE is suitable for denosing purposes, such as speech recognition [9, 9], and removing musics from speeches [33], medical image denoising [11] and super-resolutions [7].

**Contractive Autoencoders (CAEs)** [24] proposed contractive autoencoders (CAEs) to achieve robustness by minimizing the first order variation, the Jacobian. The concept of contraction ratio is introduced, which is similar to the Lipschitz constants. In order to learn the low-dimensional structure of the input data, the panelty of construction error encourages the contraction ratios on the tangential directions of the manifold to be close to 1, and on the orthogonal directions to the manifold close to 0. Their experiments showed that the learned representations performed as good as DAEs on classification problems and showed that their contraction properties are similar. Following this work, [23] proposed the higher-order CAE which adds an additional penalty on all higher derivatives.

**Generative Model** Autoencoders can be transformed into a generative model by sampling in the latent space and then decode the samples to obtain new data. [30] used Bernoulli sampling to AEs and DAEs to first implement this idea. [5] used Gibbs sampling to alternatively sample between the input space and the latent space, and transfered DAEs into generative models. They also proved that the generated distribution is consistent with the distribution of the dataset. [22] proposed a generative model by sampling from CADs. They used the information of the Jacobian to sample around the latent space.

The Variational autoencoder (VAE) [15] use probability perspective to interprete autoencoders. Suppose the real data distribution is $\mu$ in $\mathcal{X}$, the encoding map $\varphi_\theta : \mathcal{X} \to \mathcal{F}$ pushes $\mu$ forward to a distribution in the latent space $(\varphi_\theta)_*\mu$. VAE optimizes $\varphi_\theta$, such that $(\varphi_\theta)_*\mu$ is normal distributed $(\varphi_\theta)_*\mu \sim \mathcal{N}(0, 1)$ in the latent space.

Followed by the big success of GANs, [17] proposed adversarial autoencoders (AAEs), which use GANs to minimize the discrepancy between the push forward distribution $(\varphi_\theta)_*\mu$ and the desired distribution in the latent space.

---

### النسخة العربية

أدبيات المشفرات التلقائية واسعة، في ما يلي نراجع بإيجاز فقط الأعمال الأكثر صلة كممثلين.

**المشفرات التلقائية التقليدية (AE)** ظهر إطار المشفر التلقائي التقليدي (AE) لأول مرة في [2]، والذي تم اقتراحه في البداية لتحقيق تقليل الأبعاد. استخدم [2] مشفراً تلقائياً خطياً للمقارنة مع PCA. بنفس الغرض، اقترح [14] معمارية مشفر تلقائي عميق، حيث يكون المشفر وفك الترميز شبكات عميقة متعددة الطبقات. بسبب عدم تحدب الشبكات العميقة، من السهل أن تتقارب إلى أمثليات محلية ضعيفة مع أوزان مبدئية عشوائية. لحل هذه المشكلة، استخدم [14] آلات بولتزمان المقيدة (RBMs) للتدريب المسبق للنموذج طبقة تلو الأخرى قبل الضبط الدقيق. لاحقاً استخدم [4] مشفرات تلقائية تقليدية للتدريب المسبق لكل طبقة وحصل على نتائج مماثلة.

**المشفرات المتناثرة** يستخدم المشفر التلقائي التقليدي بنية عنق الزجاجة، حيث يكون عرض الطبقة الوسطى أقل من عرض طبقة المدخلات. تم تقديم المشفر التلقائي المتناثر (SAE) في [10]، والذي يستخدم فضاءً كامناً زائداً عن الحاجة، أي أن الطبقة الوسطى أوسع من طبقة المدخلات. تم اقتراح مشفرات تلقائية متناثرة [19، 21، 20].

تمت إضافة تنظيمات إضافية للتناثر في دالة الهدف، مثل تباعد KL بين توزيع مخرجات طبقة عنق الزجاجة والتوزيع المطلوب [18]. تُستخدم المشفرات التلقائية المتناثرة في العديد من مهام التصنيف [31، 26]، وتعلم نقل الميزات [8].

**المشفر التلقائي لإزالة الضوضاء (DAE)** اقترح [30، 29] المشفر التلقائي لإزالة الضوضاء (DAE) من أجل تحسين المتانة من المدخلات التالفة. تضيف مشفرات DAE تنظيمات على المدخلات لإعادة بناء مدخل "مُصلح" من نسخة تالفة. يتم بناء المشفرات التلقائية المكدسة لإزالة الضوضاء (SDAEs) عن طريق تكديس طبقات متعددة من DAEs، حيث يتم التدريب المسبق لكل طبقة بواسطة DAEs. المشفر DAE/SDAE مناسب لأغراض إزالة الضوضاء، مثل التعرف على الكلام [9، 9]، وإزالة الموسيقى من الخطابات [33]، وإزالة الضوضاء من الصور الطبية [11] والدقة الفائقة [7].

**المشفرات التلقائية الانكماشية (CAEs)** اقترح [24] المشفرات التلقائية الانكماشية (CAEs) لتحقيق المتانة عن طريق تقليل التباين من الدرجة الأولى، وهو الجاكوبي. تم تقديم مفهوم نسبة الانكماش، والذي يشبه ثوابت ليبشيتز. من أجل تعلم البنية منخفضة الأبعاد لبيانات المدخلات، تشجع عقوبة خطأ البناء نسب الانكماش على الاتجاهات المماسية للمتعدد لتكون قريبة من 1، وعلى الاتجاهات العمودية للمتعدد قريبة من 0. أظهرت تجاربهم أن التمثيلات المتعلمة أدت أداءً جيداً مثل DAEs في مشاكل التصنيف وأظهرت أن خصائص الانكماش الخاصة بها متشابهة. بعد هذا العمل، اقترح [23] المشفر التلقائي الانكماشي من الدرجة الأعلى والذي يضيف عقوبة إضافية على جميع المشتقات الأعلى.

**نموذج توليدي** يمكن تحويل المشفرات التلقائية إلى نموذج توليدي عن طريق أخذ العينات في الفضاء الكامن ثم فك تشفير العينات للحصول على بيانات جديدة. استخدم [30] عينات برنولي للمشفرات التلقائية AEs و DAEs لتنفيذ هذه الفكرة أولاً. استخدم [5] عينات جيبس لأخذ العينات بالتناوب بين فضاء المدخلات والفضاء الكامن، ونقل DAEs إلى نماذج توليدية. كما أثبتوا أن التوزيع المولد متسق مع توزيع مجموعة البيانات. اقترح [22] نموذجاً توليدياً عن طريق أخذ العينات من CADs. استخدموا معلومات الجاكوبي لأخذ العينات حول الفضاء الكامن.

يستخدم المشفر التلقائي المتغير (VAE) [15] منظوراً احتمالياً لتفسير المشفرات التلقائية. افترض أن توزيع البيانات الحقيقي هو $\mu$ في $\mathcal{X}$، فإن خريطة الترميز $\varphi_\theta : \mathcal{X} \to \mathcal{F}$ تدفع $\mu$ إلى الأمام إلى توزيع في الفضاء الكامن $(\varphi_\theta)_*\mu$. يحسن VAE $\varphi_\theta$، بحيث يكون $(\varphi_\theta)_*\mu$ موزعاً طبيعياً $(\varphi_\theta)_*\mu \sim \mathcal{N}(0, 1)$ في الفضاء الكامن.

بعد النجاح الكبير لشبكات GANs، اقترح [17] المشفرات التلقائية الخصامية (AAEs)، والتي تستخدم GANs لتقليل التباين بين التوزيع المدفوع للأمام $(\varphi_\theta)_*\mu$ والتوزيع المطلوب في الفضاء الكامن.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:**
  - bottleneck structure → بنية عنق الزجاجة
  - over-complete → زائد عن الحاجة
  - KL divergence → تباعد KL
  - Jacobian → الجاكوبي
  - contraction ratio → نسبة الانكماش
  - Lipschitz constants → ثوابت ليبشيتز
  - push forward → يدفع للأمام

- **Equations:** Several inline LaTeX equations (preserved)
- **Citations:** [2], [4], [5], [7], [8], [9], [10], [11], [14], [15], [17], [18], [19], [20], [21], [22], [23], [24], [26], [29], [30], [31], [33]
- **Special handling:** Abbreviations (AE, SAE, DAE, SDAE, CAE, VAE, AAE, GAN, RBM, PCA) kept in English

### Back-Translation Check (Last Paragraph)

"Following the great success of GANs, [17] proposed adversarial autoencoders (AAEs), which use GANs to minimize the discrepancy between the push-forward distribution $(\varphi_\theta)_*\mu$ and the desired distribution in the latent space."

✓ Semantic match verified

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
