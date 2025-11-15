# Section 5: Experiments
## القسم 5: التجارب

**Section:** experiments
**Translation Quality:** 0.88
**Glossary Terms Used:** accuracy, ImageNet, baseline, parameters, FLOPS, inference, transfer learning, fine-tuning, dataset, model scaling, convolutional neural networks

---

### English Version

#### 5.1 Scaling Up MobileNets and ResNets

As a proof of concept, we first apply our scaling method to the widely-used MobileNets and ResNets. Table 2 shows the ImageNet results of scaling them in different ways. Compared to other single-dimension scaling methods, our compound scaling method improves the accuracy on all these models, suggesting the effectiveness of our proposed scaling method for general existing ConvNets.

**Table 2. Scaling Up MobileNets and ResNets**

[Table showing comparison of different scaling methods on MobileNets and ResNets with accuracy and parameter counts]

#### 5.2 ImageNet Results for EfficientNet

We train our EfficientNet models on ImageNet using similar settings as MnasNet: RMSProp optimizer with decay 0.9 and momentum 0.9; batch norm momentum 0.99; weight decay 1e-5; initial learning rate 0.256 that decays by 0.97 every 2.4 epochs. We also use swish activation, fixed AutoAugment policy, and stochastic depth with survival probability 0.8. As commonly done, we linearly increase dropout ratio from 0.2 for EfficientNet-B0 to 0.5 for B7. All models are trained with image size from Table 1 using 4K TPU chips for up to 16K minibatch size.

Figure 5 illustrates the ImageNet accuracy-parameters curve and accuracy-FLOPS curve for representative ConvNets, where our proposed EfficientNets significantly outperform other ConvNets. In particular, our EfficientNet-B7 achieves 84.3% top-1 accuracy with 66M parameters and 37B FLOPS, being 8.4x smaller and 6.1x faster than the previous best GPipe, yet achieving higher accuracy. Compared to the widely used ResNet-50, EfficientNet-B4 improves the top-1 accuracy from 76.3% to 83.0% (+6.7%) with similar FLOPS.

Table 3 shows detailed comparison of our EfficientNet and other ConvNets on ImageNet. Our scaled EfficientNet models consistently achieve better accuracy with much fewer parameters and FLOPS than other ConvNets. In particular, our EfficientNet-B7 achieves 84.3% ImageNet top-1 accuracy with 66M parameters, while the best existing ConvNet GPipe achieves 84.3% accuracy but with 557M parameters, which is 8.4x larger.

**Table 3. Performance Results on ImageNet**

| Model | Top-1 Acc. | Top-5 Acc. | #Params | #FLOPS |
|-------|------------|------------|---------|---------|
| ResNet-50 | 76.3% | 93.0% | 26M | 4.1B |
| ResNet-152 | 77.8% | 93.8% | 60M | 11.3B |
| DenseNet-264 | 77.9% | 93.9% | 34M | 6.0B |
| Inception-v3 | 78.8% | 94.4% | 24M | 5.7B |
| Xception | 79.0% | 94.5% | 23M | 8.4B |
| SENet | 82.7% | 96.2% | 146M | 42B |
| NASNet-A | 82.7% | 96.2% | 89M | 24B |
| AmoebaNet-A | 82.8% | 96.1% | 87M | 24B |
| GPipe | 84.3% | - | 557M | - |
| **EfficientNet-B0** | **77.1%** | **93.3%** | **5.3M** | **0.39B** |
| **EfficientNet-B1** | **79.1%** | **94.4%** | **7.8M** | **0.70B** |
| **EfficientNet-B2** | **80.1%** | **94.9%** | **9.2M** | **1.0B** |
| **EfficientNet-B3** | **81.6%** | **95.7%** | **12M** | **1.8B** |
| **EfficientNet-B4** | **82.9%** | **96.4%** | **19M** | **4.2B** |
| **EfficientNet-B5** | **83.6%** | **96.7%** | **30M** | **9.9B** |
| **EfficientNet-B6** | **84.0%** | **96.8%** | **43M** | **19B** |
| **EfficientNet-B7** | **84.3%** | **97.0%** | **66M** | **37B** |

To further validate the latency performance, we have also measured the inference latency for a few representative CovNets on a real CPU as shown in Table 4. We measure latency on a single-thread Intel Xeon CPU with batch size 1 to better reflect real-world use cases. EfficientNets run 5.7x - 9.6x faster than previous ConvNets while being much more accurate.

#### 5.3 Transfer Learning Results

We have also evaluated our EfficientNet on a list of commonly used transfer learning datasets, as shown in Table 5. We borrow the same training settings from previous works and use the publicly available ImageNet pre-trained checkpoints. Table 5 shows EfficientNets achieve better accuracy than previous ConvNets on 5 out of 8 datasets, with 9.6x fewer parameters on average. This demonstrates that our EfficientNets generalize well on many transfer learning datasets.

**Table 5. Transfer Learning Results**

| Dataset | Previous Best | EfficientNet-B7 | Params Reduction |
|---------|---------------|-----------------|------------------|
| CIFAR-10 | 98.5% | 98.9% | 8.8x |
| CIFAR-100 | 89.3% | 91.7% | 5.9x |
| Birdsnap | 84.3% | 88.3% | 23x |
| Stanford Cars | 94.7% | 94.7% | 21x |
| Flowers | 98.7% | 98.8% | 19x |
| FGVC Aircraft | 92.0% | 91.4% | 21x |
| Oxford-IIIT Pets | 94.9% | 94.7% | 4.5x |
| Food-101 | 90.1% | 89.2% | 5.3x |

#### 5.4 Discussion

To further understand why our compound scaling method is better than others, Figure 6 compares class activation map for several representative models with different scaling methods. All these models are scaled from the same baseline with the same number of FLOPS. Images show models with compound scaling tend to focus on more relevant regions with more object details, while other models are either lack of object details or unable to capture all objects in the images.

---

### النسخة العربية

#### 5.1 توسيع MobileNets وResNets

كإثبات للمفهوم، نطبق أولاً طريقة التوسيع الخاصة بنا على MobileNets وResNets المستخدمة على نطاق واسع. يوضح الجدول 2 نتائج ImageNet لتوسيعها بطرق مختلفة. بالمقارنة مع طرق التوسيع أحادية البُعد الأخرى، تحسن طريقة التوسيع المركبة الخاصة بنا الدقة على جميع هذه النماذج، مما يشير إلى فعالية طريقة التوسيع المقترحة للشبكات الالتفافية العامة الموجودة.

**الجدول 2. توسيع MobileNets وResNets**

[جدول يوضح مقارنة طرق التوسيع المختلفة على MobileNets وResNets مع أعداد الدقة والمعاملات]

#### 5.2 نتائج ImageNet لـ EfficientNet

ندرب نماذج EfficientNet على ImageNet باستخدام إعدادات مماثلة لـ MnasNet: محسّن RMSProp مع تحلل 0.9 وزخم 0.9؛ زخم التطبيع الدفعي 0.99؛ تحلل الوزن 1e-5؛ معدل تعلم أولي 0.256 يتحلل بمقدار 0.97 كل 2.4 عصر. نستخدم أيضاً تنشيط swish، وسياسة AutoAugment ثابتة، وعمق عشوائي مع احتمالية بقاء 0.8. كما هو شائع، نزيد خطياً نسبة dropout من 0.2 لـ EfficientNet-B0 إلى 0.5 لـ B7. يتم تدريب جميع النماذج بحجم الصورة من الجدول 1 باستخدام 4K رقاقة TPU لحجم دفعة صغيرة يصل إلى 16K.

يوضح الشكل 5 منحنى دقة-معاملات ImageNet ومنحنى دقة-FLOPS للشبكات الالتفافية التمثيلية، حيث تتفوق EfficientNets المقترحة بشكل كبير على الشبكات الالتفافية الأخرى. على وجه الخصوص، يحقق EfficientNet-B7 دقة 84.3% في أفضل 1 مع 66 مليون معامل و37 مليار FLOPS، كونه أصغر بمقدار 8.4 مرة وأسرع بمقدار 6.1 مرة من أفضل GPipe السابق، مع تحقيق دقة أعلى. بالمقارنة مع ResNet-50 المستخدم على نطاق واسع، يحسن EfficientNet-B4 دقة أفضل 1 من 76.3% إلى 83.0% (+6.7%) مع FLOPS مماثلة.

يوضح الجدول 3 مقارنة تفصيلية بين EfficientNet والشبكات الالتفافية الأخرى على ImageNet. تحقق نماذج EfficientNet الموسعة باستمرار دقة أفضل مع معاملات وFLOPS أقل بكثير من الشبكات الالتفافية الأخرى. على وجه الخصوص، يحقق EfficientNet-B7 دقة 84.3% في أفضل 1 على ImageNet مع 66 مليون معامل، بينما تحقق أفضل شبكة التفافية موجودة GPipe دقة 84.3% ولكن مع 557 مليون معامل، وهو أكبر بمقدار 8.4 مرة.

**الجدول 3. نتائج الأداء على ImageNet**

| النموذج | دقة أفضل 1 | دقة أفضل 5 | عدد المعاملات | عدد FLOPS |
|-------|------------|------------|---------|---------|
| ResNet-50 | 76.3% | 93.0% | 26M | 4.1B |
| ResNet-152 | 77.8% | 93.8% | 60M | 11.3B |
| DenseNet-264 | 77.9% | 93.9% | 34M | 6.0B |
| Inception-v3 | 78.8% | 94.4% | 24M | 5.7B |
| Xception | 79.0% | 94.5% | 23M | 8.4B |
| SENet | 82.7% | 96.2% | 146M | 42B |
| NASNet-A | 82.7% | 96.2% | 89M | 24B |
| AmoebaNet-A | 82.8% | 96.1% | 87M | 24B |
| GPipe | 84.3% | - | 557M | - |
| **EfficientNet-B0** | **77.1%** | **93.3%** | **5.3M** | **0.39B** |
| **EfficientNet-B1** | **79.1%** | **94.4%** | **7.8M** | **0.70B** |
| **EfficientNet-B2** | **80.1%** | **94.9%** | **9.2M** | **1.0B** |
| **EfficientNet-B3** | **81.6%** | **95.7%** | **12M** | **1.8B** |
| **EfficientNet-B4** | **82.9%** | **96.4%** | **19M** | **4.2B** |
| **EfficientNet-B5** | **83.6%** | **96.7%** | **30M** | **9.9B** |
| **EfficientNet-B6** | **84.0%** | **96.8%** | **43M** | **19B** |
| **EfficientNet-B7** | **84.3%** | **97.0%** | **66M** | **37B** |

للتحقق من أداء الكمون بشكل أكبر، قمنا أيضاً بقياس كمون الاستنتاج لعدد قليل من الشبكات الالتفافية التمثيلية على وحدة معالجة مركزية حقيقية كما هو موضح في الجدول 4. نقيس الكمون على وحدة معالجة مركزية Intel Xeon أحادية الخيط مع حجم دفعة 1 لتعكس بشكل أفضل حالات الاستخدام في العالم الحقيقي. تعمل EfficientNets أسرع بمقدار 5.7 - 9.6 مرة من الشبكات الالتفافية السابقة مع كونها أكثر دقة بكثير.

#### 5.3 نتائج التعلم بالنقل

قمنا أيضاً بتقييم EfficientNet على قائمة من مجموعات بيانات التعلم بالنقل المستخدمة بشكل شائع، كما هو موضح في الجدول 5. نستعير نفس إعدادات التدريب من الأعمال السابقة ونستخدم نقاط التحقق المدربة مسبقاً على ImageNet المتاحة للجمهور. يوضح الجدول 5 أن EfficientNets تحقق دقة أفضل من الشبكات الالتفافية السابقة على 5 من أصل 8 مجموعات بيانات، مع معاملات أقل بمقدار 9.6 مرة في المتوسط. يوضح هذا أن EfficientNets تعمم بشكل جيد على العديد من مجموعات بيانات التعلم بالنقل.

**الجدول 5. نتائج التعلم بالنقل**

| مجموعة البيانات | الأفضل السابق | EfficientNet-B7 | تقليل المعاملات |
|---------|---------------|-----------------|------------------|
| CIFAR-10 | 98.5% | 98.9% | 8.8x |
| CIFAR-100 | 89.3% | 91.7% | 5.9x |
| Birdsnap | 84.3% | 88.3% | 23x |
| Stanford Cars | 94.7% | 94.7% | 21x |
| Flowers | 98.7% | 98.8% | 19x |
| FGVC Aircraft | 92.0% | 91.4% | 21x |
| Oxford-IIIT Pets | 94.9% | 94.7% | 4.5x |
| Food-101 | 90.1% | 89.2% | 5.3x |

#### 5.4 المناقشة

لفهم أفضل لسبب كون طريقة التوسيع المركبة الخاصة بنا أفضل من الطرق الأخرى، يقارن الشكل 6 خريطة تنشيط الفئة لعدة نماذج تمثيلية بطرق توسيع مختلفة. تم توسيع جميع هذه النماذج من نفس خط الأساس بنفس عدد FLOPS. تُظهر الصور أن النماذج ذات التوسيع المركب تميل إلى التركيز على مناطق أكثر صلة مع المزيد من تفاصيل الكائن، بينما النماذج الأخرى إما تفتقر إلى تفاصيل الكائن أو غير قادرة على التقاط جميع الكائنات في الصور.

---

### Translation Notes

- **Figures referenced:** Figure 5 (accuracy curves), Figure 6 (class activation maps)
- **Tables:** Table 2 (scaling comparison), Table 3 (ImageNet results), Table 4 (latency), Table 5 (transfer learning)
- **Key terms introduced:** Class activation map, AutoAugment, stochastic depth, dropout, top-1 accuracy, top-5 accuracy, latency, minibatch
- **Equations:** 0
- **Citations:** MnasNet, ResNet, DenseNet, Inception, Xception, SENet, NASNet, AmoebaNet, GPipe
- **Special handling:** All tables translated with proper Arabic headers while preserving numerical data and model names

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88

### Back-Translation (Key Results)

"Our scaled EfficientNet models consistently achieve better accuracy with much fewer parameters and FLOPS than other convolutional networks. Specifically, our EfficientNet-B7 achieves 84.3% ImageNet top-1 accuracy with 66M parameters, while the best existing convolutional network GPipe achieves 84.3% accuracy but with 557M parameters, which is 8.4 times larger."
