# Section 5: Experiments
## القسم 5: التجارب

**Section:** experiments
**Translation Quality:** 0.86
**Glossary Terms Used:** scaling, MobileNets, ResNet, compound scaling, ImageNet, accuracy, FLOPS, parameters, transfer learning, baseline, optimizer, batch normalization, activation function, dropout, regularization

---

### English Version

In this section, we will first evaluate our scaling method on existing ConvNets and the new proposed EfficientNets.

### 5.1. Scaling Up MobileNets and ResNets

As a proof of concept, we first apply our scaling method to the widely-used MobileNets (Howard et al., 2017; Sandler et al., 2018) and ResNet (He et al., 2016). Table 3 shows the ImageNet results of scaling them in different ways. Compared to other single-dimension scaling methods, our compound scaling method improves the accuracy on all these models, suggesting the effectiveness of our proposed scaling method for general existing ConvNets.

**Table 3. Scaling Up MobileNets and ResNet.**

| Model | FLOPS | Top-1 Acc. |
|-------|-------|------------|
| Baseline MobileNetV1 (Howard et al., 2017) | 0.6B | 70.6% |
| Scale MobileNetV1 by width (w=2) | 2.2B | 74.2% |
| Scale MobileNetV1 by resolution (r=2) | 2.2B | 72.7% |
| compound scale (d=1.4, w=1.2, r=1.3) | 2.3B | 75.6% |
| Baseline MobileNetV2 (Sandler et al., 2018) | 0.3B | 72.0% |
| Scale MobileNetV2 by depth (d=4) | 1.2B | 76.8% |
| Scale MobileNetV2 by width (w=2) | 1.1B | 76.4% |
| Scale MobileNetV2 by resolution (r=2) | 1.2B | 74.8% |
| MobileNetV2 compound scale | 1.3B | 77.4% |
| Baseline ResNet-50 (He et al., 2016) | 4.1B | 76.0% |
| Scale ResNet-50 by depth (d=4) | 16.2B | 78.1% |
| Scale ResNet-50 by width (w=2) | 14.7B | 77.7% |
| Scale ResNet-50 by resolution (r=2) | 16.4B | 77.5% |
| ResNet-50 compound scale | 16.7B | 78.8% |

### 5.2. ImageNet Results for EfficientNet

We train our EfficientNet models on ImageNet using similar settings as (Tan et al., 2019): RMSProp optimizer with decay 0.9 and momentum 0.9; batch norm momentum 0.99; weight decay 1e-5; initial learning rate 0.256 that decays by 0.97 every 2.4 epochs. We also use SiLU (Swish-1) activation (Ramachandran et al., 2018; Elfwing et al., 2018; Hendrycks & Gimpel, 2016), AutoAugment (Cubuk et al., 2019), and stochastic depth (Huang et al., 2016) with survival probability 0.8. As commonly known that bigger models need more regularization, we linearly increase dropout (Srivastava et al., 2014) ratio from 0.2 for EfficientNet-B0 to 0.5 for B7. We reserve 25K randomly picked images from the training set as a minival set, and perform early stopping on this minival; we then evaluate the early-stopped checkpoint on the original validation set to report the final validation accuracy.

Table 2 shows the performance of all EfficientNet models that are scaled from the same baseline EfficientNet-B0. Our EfficientNet models generally use an order of magnitude fewer parameters and FLOPS than other ConvNets with similar accuracy. In particular, our EfficientNet-B7 achieves 84.3% top1 accuracy with 66M parameters and 37B FLOPS, being more accurate but 8.4x smaller than the previous best GPipe (Huang et al., 2018). These gains come from both better architectures, better scaling, and better training settings that are customized for EfficientNet.

Figure 1 and Figure 5 illustrates the parameters-accuracy and FLOPS-accuracy curve for representative ConvNets, where our scaled EfficientNet models achieve better accuracy with much fewer parameters and FLOPS than other ConvNets. Notably, our EfficientNet models are not only small, but also computational cheaper. For example, our EfficientNet-B3 achieves higher accuracy than ResNeXt-101 (Xie et al., 2017) using 18x fewer FLOPS.

To validate the latency, we have also measured the inference latency for a few representative CovNets on a real CPU as shown in Table 4, where we report average latency over 20 runs. Our EfficientNet-B1 runs 5.7x faster than the widely used ResNet-152, while EfficientNet-B7 runs about 6.1x faster than GPipe (Huang et al., 2018), suggesting our EfficientNets are indeed fast on real hardware.

**Table 4. Inference Latency Comparison** – Latency is measured with batch size 1 on a single core of Intel Xeon CPU E5-2690.

| Model | Acc. @ Latency | Model | Acc. @ Latency |
|-------|----------------|-------|----------------|
| ResNet-152 | 77.8% @ 0.554s | GPipe | 84.3% @ 19.0s |
| EfficientNet-B1 | 78.8% @ 0.098s | EfficientNet-B7 | 84.4% @ 3.1s |
| Speedup | 5.7x | Speedup | 6.1x |

### 5.3. Transfer Learning Results for EfficientNet

We have also evaluated our EfficientNet on a list of commonly used transfer learning datasets, as shown in Table 6. We borrow the same training settings from (Kornblith et al., 2019) and (Huang et al., 2018), which take ImageNet pretrained checkpoints and finetune on new datasets.

**Table 6. Transfer Learning Datasets.**

| Dataset | Train Size | Test Size | #Classes |
|---------|-----------|-----------|----------|
| CIFAR-10 (Krizhevsky & Hinton, 2009) | 50,000 | 10,000 | 10 |
| CIFAR-100 (Krizhevsky & Hinton, 2009) | 50,000 | 10,000 | 100 |
| Birdsnap (Berg et al., 2014) | 47,386 | 2,443 | 500 |
| Stanford Cars (Krause et al., 2013) | 8,144 | 8,041 | 196 |
| Flowers (Nilsback & Zisserman, 2008) | 2,040 | 6,149 | 102 |
| FGVC Aircraft (Maji et al., 2013) | 6,667 | 3,333 | 100 |
| Oxford-IIIT Pets (Parkhi et al., 2012) | 3,680 | 3,369 | 37 |
| Food-101 (Bossard et al., 2014) | 75,750 | 25,250 | 101 |

Table 5 shows the transfer learning performance: (1) Compared to public available models, such as NASNet-A (Zoph et al., 2018) and Inception-v4 (Szegedy et al., 2017), our EfficientNet models achieve better accuracy with 4.7x average (up to 21x) parameter reduction. (2) Compared to state-of-the-art models, including DAT (Ngiam et al., 2018) that dynamically synthesizes training data and GPipe (Huang et al., 2018) that is trained with specialized pipeline parallelism, our EfficientNet models still surpass their accuracy in 5 out of 8 datasets, but using 9.6x fewer parameters.

Figure 6 compares the accuracy-parameters curve for a variety of models. In general, our EfficientNets consistently achieve better accuracy with an order of magnitude fewer parameters than existing models, including ResNet (He et al., 2016), DenseNet (Huang et al., 2017), Inception (Szegedy et al., 2017), and NASNet (Zoph et al., 2018).

---

### النسخة العربية

في هذا القسم، سنقوم أولاً بتقييم طريقة التوسيع الخاصة بنا على الشبكات الالتفافية الموجودة وEfficientNets المقترحة الجديدة.

### 5.1. توسيع MobileNets وResNets

كإثبات للمفهوم، نطبق أولاً طريقة التوسيع الخاصة بنا على MobileNets المُستخدمة على نطاق واسع (Howard et al., 2017; Sandler et al., 2018) وResNet (He et al., 2016). يُظهر الجدول 3 نتائج ImageNet لتوسيعها بطرق مختلفة. بالمقارنة مع طرق التوسيع أحادية البُعد الأخرى، تحسن طريقة التوسيع المركب الخاصة بنا الدقة على جميع هذه النماذج، مما يشير إلى فعالية طريقة التوسيع المقترحة للشبكات الالتفافية العامة الموجودة.

**الجدول 3. توسيع MobileNets وResNet.**

| النموذج | FLOPS | دقة أفضل 1 |
|-------|-------|------------|
| Baseline MobileNetV1 (Howard et al., 2017) | 0.6B | 70.6% |
| توسيع MobileNetV1 بالعرض (w=2) | 2.2B | 74.2% |
| توسيع MobileNetV1 بدقة الوضوح (r=2) | 2.2B | 72.7% |
| توسيع مركب (d=1.4, w=1.2, r=1.3) | 2.3B | 75.6% |
| Baseline MobileNetV2 (Sandler et al., 2018) | 0.3B | 72.0% |
| توسيع MobileNetV2 بالعمق (d=4) | 1.2B | 76.8% |
| توسيع MobileNetV2 بالعرض (w=2) | 1.1B | 76.4% |
| توسيع MobileNetV2 بدقة الوضوح (r=2) | 1.2B | 74.8% |
| توسيع MobileNetV2 مركب | 1.3B | 77.4% |
| Baseline ResNet-50 (He et al., 2016) | 4.1B | 76.0% |
| توسيع ResNet-50 بالعمق (d=4) | 16.2B | 78.1% |
| توسيع ResNet-50 بالعرض (w=2) | 14.7B | 77.7% |
| توسيع ResNet-50 بدقة الوضوح (r=2) | 16.4B | 77.5% |
| توسيع ResNet-50 مركب | 16.7B | 78.8% |

### 5.2. نتائج ImageNet لـ EfficientNet

نقوم بتدريب نماذج EfficientNet الخاصة بنا على ImageNet باستخدام إعدادات مماثلة لـ (Tan et al., 2019): مُحسّن RMSProp مع اضمحلال 0.9 وزخم 0.9؛ زخم التطبيع الدفعي 0.99؛ اضمحلال الوزن 1e-5؛ معدل التعلم الأولي 0.256 الذي يضمحل بمقدار 0.97 كل 2.4 حقبة. نستخدم أيضاً تنشيط SiLU (Swish-1) (Ramachandran et al., 2018; Elfwing et al., 2018; Hendrycks & Gimpel, 2016)، وAutoAugment (Cubuk et al., 2019)، والعمق العشوائي (Huang et al., 2016) مع احتمال بقاء 0.8. كما هو معروف أن النماذج الأكبر تحتاج إلى مزيد من التنظيم، نزيد خطياً نسبة الانقطاع (Srivastava et al., 2014) من 0.2 لـ EfficientNet-B0 إلى 0.5 لـ B7. نحتفظ بـ 25 ألف صورة مُختارة عشوائياً من مجموعة التدريب كمجموعة تحقق صغيرة، ونجري إيقافاً مبكراً على هذه المجموعة الصغيرة؛ ثم نقوم بتقييم نقطة التفتيش الموقوفة مبكراً على مجموعة التحقق الأصلية للإبلاغ عن دقة التحقق النهائية.

يُظهر الجدول 2 أداء جميع نماذج EfficientNet التي تم توسيعها من نفس خط الأساس EfficientNet-B0. تستخدم نماذج EfficientNet الخاصة بنا بشكل عام مرتبة من حيث الحجم أقل من المعاملات وFLOPS من الشبكات الالتفافية الأخرى ذات الدقة المماثلة. على وجه الخصوص، يحقق EfficientNet-B7 الخاص بنا دقة 84.3% في أفضل 1 مع 66 مليون معامل و37 مليار FLOPS، كونه أكثر دقة ولكن أصغر بمقدار 8.4 مرة من أفضل GPipe السابق (Huang et al., 2018). تأتي هذه المكاسب من معماريات أفضل، وتوسيع أفضل، وإعدادات تدريب أفضل مُخصصة لـ EfficientNet.

يوضح الشكل 1 والشكل 5 منحنى المعاملات-الدقة ومنحنى FLOPS-الدقة للشبكات الالتفافية التمثيلية، حيث تحقق نماذج EfficientNet الموسعة الخاصة بنا دقة أفضل مع معاملات وFLOPS أقل بكثير من الشبكات الالتفافية الأخرى. والجدير بالذكر أن نماذج EfficientNet الخاصة بنا ليست صغيرة فحسب، بل أيضاً أرخص حسابياً. على سبيل المثال، يحقق EfficientNet-B3 الخاص بنا دقة أعلى من ResNeXt-101 (Xie et al., 2017) باستخدام FLOPS أقل بمقدار 18 مرة.

للتحقق من زمن الاستجابة، قمنا أيضاً بقياس زمن استجابة الاستنتاج لعدد قليل من الشبكات الالتفافية التمثيلية على وحدة معالجة مركزية حقيقية كما هو موضح في الجدول 4، حيث نُبلّغ عن متوسط زمن الاستجابة على مدى 20 تشغيلاً. يعمل EfficientNet-B1 الخاص بنا بسرعة أكبر بمقدار 5.7 مرة من ResNet-152 المُستخدم على نطاق واسع، بينما يعمل EfficientNet-B7 بسرعة أكبر بمقدار 6.1 مرة من GPipe (Huang et al., 2018)، مما يشير إلى أن EfficientNets الخاصة بنا سريعة بالفعل على الأجهزة الحقيقية.

**الجدول 4. مقارنة زمن استجابة الاستنتاج** - يتم قياس زمن الاستجابة بحجم دفعة 1 على نواة واحدة من معالج Intel Xeon CPU E5-2690.

| النموذج | الدقة @ زمن الاستجابة | النموذج | الدقة @ زمن الاستجابة |
|-------|----------------|-------|----------------|
| ResNet-152 | 77.8% @ 0.554s | GPipe | 84.3% @ 19.0s |
| EfficientNet-B1 | 78.8% @ 0.098s | EfficientNet-B7 | 84.4% @ 3.1s |
| التسريع | 5.7x | التسريع | 6.1x |

### 5.3. نتائج التعلم بالنقل لـ EfficientNet

قمنا أيضاً بتقييم EfficientNet الخاص بنا على قائمة من مجموعات بيانات التعلم بالنقل المُستخدمة بشكل شائع، كما هو موضح في الجدول 6. نقترض نفس إعدادات التدريب من (Kornblith et al., 2019) و(Huang et al., 2018)، والتي تأخذ نقاط تفتيش ImageNet المُدربة مسبقاً وتضبطها بدقة على مجموعات بيانات جديدة.

**الجدول 6. مجموعات بيانات التعلم بالنقل.**

| مجموعة البيانات | حجم التدريب | حجم الاختبار | عدد الفئات |
|---------|-----------|-----------|----------|
| CIFAR-10 (Krizhevsky & Hinton, 2009) | 50,000 | 10,000 | 10 |
| CIFAR-100 (Krizhevsky & Hinton, 2009) | 50,000 | 10,000 | 100 |
| Birdsnap (Berg et al., 2014) | 47,386 | 2,443 | 500 |
| Stanford Cars (Krause et al., 2013) | 8,144 | 8,041 | 196 |
| Flowers (Nilsback & Zisserman, 2008) | 2,040 | 6,149 | 102 |
| FGVC Aircraft (Maji et al., 2013) | 6,667 | 3,333 | 100 |
| Oxford-IIIT Pets (Parkhi et al., 2012) | 3,680 | 3,369 | 37 |
| Food-101 (Bossard et al., 2014) | 75,750 | 25,250 | 101 |

يُظهر الجدول 5 أداء التعلم بالنقل: (1) بالمقارنة مع النماذج المتاحة للعامة، مثل NASNet-A (Zoph et al., 2018) وInception-v4 (Szegedy et al., 2017)، تحقق نماذج EfficientNet الخاصة بنا دقة أفضل مع تقليل معاملات بمتوسط 4.7 مرة (حتى 21 مرة). (2) بالمقارنة مع النماذج المتقدمة، بما في ذلك DAT (Ngiam et al., 2018) الذي يُركّب بيانات التدريب ديناميكياً وGPipe (Huang et al., 2018) الذي تم تدريبه باستخدام التوازي الأنبوبي المتخصص، لا تزال نماذج EfficientNet الخاصة بنا تتفوق على دقتها في 5 من أصل 8 مجموعات بيانات، لكن باستخدام معاملات أقل بمقدار 9.6 مرة.

يقارن الشكل 6 منحنى الدقة-المعاملات لمجموعة متنوعة من النماذج. بشكل عام، تحقق EfficientNets الخاصة بنا باستمرار دقة أفضل مع معاملات أقل بمرتبة من حيث الحجم من النماذج الموجودة، بما في ذلك ResNet (He et al., 2016)، وDenseNet (Huang et al., 2017)، وInception (Szegedy et al., 2017)، وNASNet (Zoph et al., 2018).

---

### Translation Notes

- **Figures referenced:** Figure 1, Figure 5, Figure 6
- **Tables referenced:** Table 2, Table 3, Table 4, Table 5, Table 6
- **Key terms introduced:** RMSProp optimizer (مُحسّن RMSProp), weight decay (اضمحلال الوزن), learning rate (معدل التعلم), stochastic depth (العمق العشوائي), survival probability (احتمال بقاء), early stopping (إيقاف مبكر), minival set (مجموعة تحقق صغيرة), finetune (ضبط بدقة)
- **Equations:** None
- **Citations:** Extensive references throughout all subsections
- **Special handling:** Three subsections with tables; preserved dataset names and technical terms in English

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
