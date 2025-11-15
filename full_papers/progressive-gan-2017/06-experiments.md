# Section 6: Experiments
## القسم 6: التجارب

**Section:** Experiments
**Translation Quality:** 0.88
**Glossary Terms Used:** dataset (مجموعة بيانات), training (تدريب), resolution (دقة), quality (جودة), inception score (درجة inception), benchmark (معيار), architecture (معمارية), convergence (تقارب), GPU (وحدة معالجة الرسومات)

---

### English Version

We evaluate our contributions on several datasets and compare against the state-of-the-art methods. Our primary datasets are CelebA-HQ (our high-quality version of CelebA), LSUN bedroom, and CIFAR10.

**6.1 Datasets**

**CelebA-HQ.** We created a high-quality version of the CelebA dataset (Liu et al., 2015) that consists of 30,000 images at 1024² resolution. We selected the images that have good coverage of the data distribution and high visual quality. The dataset is available at our GitHub repository.

**LSUN.** We use the bedroom category from the LSUN dataset (Yu et al., 2015), which contains approximately 3 million training images. We train our models at resolutions up to 256².

**CIFAR10.** We use the standard CIFAR10 dataset (Krizhevsky & Hinton, 2009) at 32² resolution to compare Inception scores with previous work.

**6.2 Implementation Details**

We use the following setup for all our experiments:

- **Architecture:** We use the DCGAN-like architecture with some modifications. The generator starts with a 4×4 feature map that is progressively upsampled to the target resolution. The discriminator mirrors this structure.

- **Optimizer:** We use Adam (Kingma & Ba, 2015) with learning rate 0.001, β₁ = 0, β₂ = 0.99, and ε = 10⁻⁸.

- **Loss function:** We primarily use WGAN-GP (Gulrajani et al., 2017) loss, but also experimented with standard GAN loss and LSGAN loss.

- **Training schedule:** We train each resolution for a fixed number of images shown to the discriminator (e.g., 800k for lower resolutions, up to 10M for the highest resolution). The fade-in phase takes half of this budget.

- **Minibatch size:** We use smaller minibatches for higher resolutions due to memory constraints (e.g., 16 for 1024² images, 128 for 4×4).

- **Hardware:** All models were trained on NVIDIA Tesla P100 GPUs. Training a 1024² model takes approximately 4 days with 8 GPUs.

**6.3 Results on CelebA-HQ**

We trained our Progressive GAN on the CelebA-HQ dataset at 1024² resolution. Figure 2 shows example generated images. The results demonstrate unprecedented visual quality with fine details like hair strands, pores, and jewelry rendered convincingly.

**Quantitative evaluation.** We compute FID between 10,000 generated images and the training set, obtaining a FID of 8.04. For comparison, the best previously published result on CelebA at 128² resolution was approximately 20.0. Our MS-SSIM analysis shows good variation without mode collapse.

**Ablation study.** We conducted ablation studies to evaluate the contribution of each component:

1. **Without progressive growing:** Training directly at 1024² failed to converge to good results even after extended training.
2. **Without minibatch stddev:** The variation decreased noticeably, with FID increasing to 9.2.
3. **Without equalized learning rate:** Training became unstable, occasionally leading to mode collapse.
4. **Without pixelwise normalization:** Signal magnitudes grew uncontrollably, requiring early stopping.

These results confirm that all our proposed components contribute significantly to the final quality.

**6.4 Results on LSUN**

We trained Progressive GAN on the LSUN bedroom dataset at 256² resolution. Figure 3 shows example generated images of bedrooms. The model successfully generates diverse bedroom scenes with realistic furniture, lighting, and spatial layout.

Our FID on LSUN bedroom is 11.3, compared to 17.9 for the previous best method. The progressive training approach proves effective even on this challenging dataset with significant intra-class variation.

**6.5 Results on CIFAR10**

We trained Progressive GAN on CIFAR10 at 32² resolution to compare Inception scores with previous work. We achieve an Inception score of 8.80 ± 0.05, surpassing the previous best published score of 7.90 ± 0.09 (Gulrajani et al., 2017).

This improvement demonstrates that our method is not limited to high-resolution images but provides benefits across different resolutions and datasets.

**6.6 Training Time Analysis**

Progressive training is significantly faster than conventional training:

- Training time for 1024² resolution: ~4 days with 8 P100 GPUs
- Estimated time for conventional training at 1024²: >1 month (did not converge in our experiments)
- Training time for 256² resolution: ~12 hours with 1 P100 GPU

The speedup comes from the fact that most iterations happen at lower resolutions, which are much faster to compute. Even though we train at multiple resolutions sequentially, the total time is much less than training directly at the target resolution.

**6.7 Comparison with State-of-the-Art**

Table 1 compares our method with recent GAN approaches on various metrics and datasets. Our Progressive GAN achieves state-of-the-art results on all evaluated benchmarks, with particularly significant improvements on high-resolution image generation tasks.

The key advantages of our approach are:
- **Highest quality:** Best FID scores across all datasets
- **Best variation:** Improved Inception scores and MS-SSIM metrics
- **Training efficiency:** Faster convergence and lower computational cost
- **Stability:** Reliable training without mode collapse

These results establish Progressive GAN as a robust and effective method for high-quality image generation.

---

### النسخة العربية

نقيم مساهماتنا على عدة مجموعات بيانات ونقارنها بأحدث الطرق. مجموعات البيانات الأساسية لدينا هي CelebA-HQ (نسختنا عالية الجودة من CelebA)، وLSUN bedroom، وCIFAR10.

**6.1 مجموعات البيانات**

**CelebA-HQ.** أنشأنا نسخة عالية الجودة من مجموعة بيانات CelebA (Liu et al., 2015) التي تتكون من 30,000 صورة بدقة 1024². اخترنا الصور التي تغطي بشكل جيد توزيع البيانات ولها جودة بصرية عالية. مجموعة البيانات متاحة في مستودع GitHub الخاص بنا.

**LSUN.** نستخدم فئة غرف النوم من مجموعة بيانات LSUN (Yu et al., 2015)، والتي تحتوي على حوالي 3 ملايين صورة تدريب. ندرب نماذجنا بدقة تصل إلى 256².

**CIFAR10.** نستخدم مجموعة بيانات CIFAR10 القياسية (Krizhevsky & Hinton, 2009) بدقة 32² لمقارنة درجات Inception مع الأعمال السابقة.

**6.2 تفاصيل التنفيذ**

نستخدم الإعداد التالي لجميع تجاربنا:

- **المعمارية:** نستخدم معمارية شبيهة بـ DCGAN مع بعض التعديلات. يبدأ المولد بخريطة ميزات 4×4 يتم رفع عيناتها تدريجياً إلى الدقة المستهدفة. يعكس المميز هذا الهيكل.

- **المحسن:** نستخدم Adam (Kingma & Ba, 2015) بمعدل تعلم 0.001، وβ₁ = 0، وβ₂ = 0.99، وε = 10⁻⁸.

- **دالة الخسارة:** نستخدم بشكل أساسي خسارة WGAN-GP (Gulrajani et al., 2017)، ولكننا جربنا أيضاً خسارة GAN القياسية وخسارة LSGAN.

- **جدول التدريب:** ندرب كل دقة لعدد ثابت من الصور المعروضة على المميز (على سبيل المثال، 800k للدقة الأقل، حتى 10M للدقة الأعلى). تستغرق مرحلة الظهور التدريجي نصف هذه الميزانية.

- **حجم الدفعة الصغيرة:** نستخدم دفعات صغيرة أصغر للدقة الأعلى بسبب قيود الذاكرة (على سبيل المثال، 16 لصور 1024²، و128 لـ 4×4).

- **الأجهزة:** تم تدريب جميع النماذج على وحدات معالجة الرسومات NVIDIA Tesla P100. يستغرق تدريب نموذج 1024² حوالي 4 أيام مع 8 وحدات معالجة رسومات.

**6.3 النتائج على CelebA-HQ**

دربنا Progressive GAN على مجموعة بيانات CelebA-HQ بدقة 1024². يوضح الشكل 2 أمثلة من الصور المولدة. تُظهر النتائج جودة بصرية غير مسبوقة مع تفاصيل دقيقة مثل خصلات الشعر والمسام والمجوهرات المقدمة بشكل مقنع.

**التقييم الكمي.** نحسب FID بين 10,000 صورة مولدة ومجموعة التدريب، ونحصل على FID بقيمة 8.04. للمقارنة، كانت أفضل نتيجة منشورة سابقاً على CelebA بدقة 128² حوالي 20.0. يُظهر تحليل MS-SSIM الخاص بنا تنوعاً جيداً بدون انهيار أنماط.

**دراسة الاستئصال.** أجرينا دراسات استئصال لتقييم مساهمة كل مكون:

1. **بدون النمو التدريجي:** فشل التدريب مباشرة عند 1024² في التقارب إلى نتائج جيدة حتى بعد تدريب ممتد.
2. **بدون الانحراف المعياري للدفعة الصغيرة:** انخفض التنوع بشكل ملحوظ، مع زيادة FID إلى 9.2.
3. **بدون معدل التعلم المتساوي:** أصبح التدريب غير مستقر، مما أدى أحياناً إلى انهيار الأنماط.
4. **بدون التطبيع لكل بكسل:** نمت مقادير الإشارة بشكل لا يمكن السيطرة عليه، مما تطلب إيقافاً مبكراً.

تؤكد هذه النتائج أن جميع مكوناتنا المقترحة تساهم بشكل كبير في الجودة النهائية.

**6.4 النتائج على LSUN**

دربنا Progressive GAN على مجموعة بيانات LSUN bedroom بدقة 256². يوضح الشكل 3 أمثلة من الصور المولدة لغرف النوم. ينجح النموذج في توليد مشاهد غرف نوم متنوعة مع أثاث واقعي وإضاءة وتخطيط مكاني.

FID الخاص بنا على LSUN bedroom هو 11.3، مقارنة بـ 17.9 لأفضل طريقة سابقة. يثبت نهج التدريب التدريجي فعاليته حتى على مجموعة البيانات الصعبة هذه مع تنوع كبير داخل الفئة.

**6.5 النتائج على CIFAR10**

دربنا Progressive GAN على CIFAR10 بدقة 32² لمقارنة درجات Inception مع الأعمال السابقة. حققنا درجة Inception بقيمة 8.80 ± 0.05، متجاوزين أفضل درجة منشورة سابقاً وهي 7.90 ± 0.09 (Gulrajani et al., 2017).

يوضح هذا التحسين أن طريقتنا ليست محدودة بالصور عالية الدقة ولكنها توفر فوائد عبر دقة ومجموعات بيانات مختلفة.

**6.6 تحليل وقت التدريب**

التدريب التدريجي أسرع بكثير من التدريب التقليدي:

- وقت التدريب لدقة 1024²: ~4 أيام مع 8 وحدات معالجة رسومات P100
- الوقت المقدر للتدريب التقليدي عند 1024²: >شهر واحد (لم يتقارب في تجاربنا)
- وقت التدريب لدقة 256²: ~12 ساعة مع وحدة معالجة رسومات P100 واحدة

يأتي التسريع من حقيقة أن معظم التكرارات تحدث عند دقة أقل، والتي تكون أسرع بكثير في الحساب. على الرغم من أننا ندرب بدقة متعددة بالتسلسل، فإن الوقت الإجمالي أقل بكثير من التدريب مباشرة عند الدقة المستهدفة.

**6.7 المقارنة مع أحدث التقنيات**

يقارن الجدول 1 طريقتنا بنهج GAN الحديثة على مقاييس ومجموعات بيانات مختلفة. يحقق Progressive GAN الخاص بنا نتائج متطورة على جميع المعايير المقيمة، مع تحسينات كبيرة بشكل خاص في مهام توليد الصور عالية الدقة.

المزايا الرئيسية لنهجنا هي:
- **أعلى جودة:** أفضل درجات FID عبر جميع مجموعات البيانات
- **أفضل تنوع:** تحسين درجات Inception ومقاييس MS-SSIM
- **كفاءة التدريب:** تقارب أسرع وتكلفة حسابية أقل
- **الاستقرار:** تدريب موثوق بدون انهيار أنماط

تؤسس هذه النتائج Progressive GAN كطريقة قوية وفعالة لتوليد صور عالية الجودة.

---

### Translation Notes

- **Figures referenced:** Figure 2 (CelebA-HQ examples), Figure 3 (LSUN bedroom examples), Table 1 (comparison with state-of-the-art)
- **Key terms introduced:**
  - Ablation study (دراسة الاستئصال)
  - State-of-the-art (أحدث التقنيات)
  - Intra-class variation (تنوع داخل الفئة)
  - Early stopping (إيقاف مبكر)
  - Training schedule (جدول التدريب)
  - Fade-in phase (مرحلة الظهور التدريجي)
  - DCGAN architecture (معمارية DCGAN)
  - LSGAN loss (خسارة LSGAN)
- **Equations:** None, but numerical results and hyperparameters listed
- **Citations:** Multiple references to datasets and previous work (Liu et al., Yu et al., Krizhevsky & Hinton, Kingma & Ba, Gulrajani et al.)
- **Special handling:**
  - Dataset names (CelebA-HQ, LSUN, CIFAR10) kept as proper nouns
  - GPU names (Tesla P100) kept in English
  - Numerical results with ± notation preserved
  - Greek letters (β, ε) kept in original form
  - Training times and computational details translated clearly

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.87
- **Overall section score:** 0.88
