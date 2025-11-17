# Section 4: Simulation result
## القسم 4: نتائج المحاكاة

**Section:** evaluation/results
**Translation Quality:** 0.87
**Glossary Terms Used:** simulation, model parameters, training, classification accuracy, agreement ratio, encrypted data, inference, pre-trained model, CIFAR-10, ResNet-20

---

### English Version

**4.1 Simulation setting and model parameters**

We simulate the proposed model by the SEAL library [14] released by Microsoft. Our simulation environment is a dual Intel Xeon Platinum 8280 CPU (112 cores) with 512GB memory. We allocate one thread per one channel of each layer by using the OpenMP library to improve the execution speed of the ResNet-20.

The model parameters are prepared by the following training method. We use 32 x 32 color images, subtract the mean of the pixels in the training dataset, and adopt a data argumentation method such as shifting and mirroring horizontally for training. We adopt the He initialization [30] as the weight initialization and no dropout. We train the model with 32 × 32 mini-batches and cross-entropy loss function. The learning rate starts with a 0.001 learning rate divided by 10 after 80 epochs and 100 after 120 epochs during training. The classification accuracy with the trained model parameters is 91.89%, which is tested with 10,000 images.

**4.2 Performance**

Table 4 shows the agreement ratio between the classification results of the implemented privacy-preserving ResNet-20 and that of the original ResNet-20, which shows almost the same results. We test the inference on 75 encrypted images, and the 95% confidence interval is suggested for each result. Only one result of our proposed model for the encrypted data shows a different result from that of the ResNet-20 model for plaintext data. In other words, the agreement ratio is 98.67%± 2.59%, which is a sufficiently high agreement result. The classification accuracy of the ResNet-20 for the encrypted data is 90.67%± 6.58%, while that of the original ResNet-20 for the corresponding plaintext image is 89.33%± 6.99%. Thus, we verify that the ResNet-20 can be successfully carried out using the RNS-CKKS scheme with sufficient accuracy for classification and the proper bootstrapping operation. Note that the highest classification accuracy of the previous model for the CIFAR-10 dataset over the word-wise FHE scheme is only 77% [19].

**Table 4: Classification accuracy of ResNet-20 for plaintext and ciphertext and agreement ratio**

| Model | ResNet-20¹ | ResNet-20² | PPML ResNet-20 | Agreement |
|-------|------------|------------|----------------|-----------|
| Accuracy | 91.89% ± 0.54% | 89.33% ± 6.99% | 90.67% ± 6.58% | 98.67%± 2.59% |

¹ Classification accuracy verified with 10,000 images.
² Classification accuracy verified with 75 images which are used to test ResNet-20 on encrypted images.

Table 5 shows the running time for the whole ResNet-20 and the portion for each component in the model. The proposed model takes about 4 hours to infer one image, and the most time-consuming components are the convolution, the ReLU, and the bootstrapping.

**Table 5: The running time of ResNet-20 and the percentage of time spent in each component relative to total time**

| Layer | PC | BN | CR | Boot | AP + FC | Softmax | Total time (s) |
|-------|----|----|----|----|---------|---------|----------------|
| Time ratio | 34.30% | 0.20% | 32.63% | 29.97% | 0.06% | 2.83% | 14,694 |

---

### النسخة العربية

**4.1 إعداد المحاكاة ومعاملات النموذج**

نحاكي النموذج المقترح بمكتبة SEAL [14] الصادرة عن Microsoft. بيئة المحاكاة لدينا هي معالج Intel Xeon Platinum 8280 المزدوج (112 نواة) مع ذاكرة 512 جيجابايت. نخصص خيطًا واحدًا لكل قناة من كل طبقة باستخدام مكتبة OpenMP لتحسين سرعة تنفيذ ResNet-20.

يتم إعداد معاملات النموذج بطريقة التدريب التالية. نستخدم صورًا ملونة 32 × 32، ونطرح متوسط البكسلات في مجموعة بيانات التدريب، ونعتمد طريقة مناقشة البيانات مثل الإزاحة والانعكاس الأفقي للتدريب. نعتمد تهيئة He [30] كتهيئة للوزن وعدم وجود dropout. ندرب النموذج بدفعات صغيرة 32 × 32 ودالة خسارة الإنتروبيا المتقاطعة. يبدأ معدل التعلم بمعدل تعلم 0.001 يُقسم على 10 بعد 80 فترة و100 بعد 120 فترة أثناء التدريب. دقة التصنيف بمعاملات النموذج المدرب هي 91.89%، والتي يتم اختبارها بـ 10,000 صورة.

**4.2 الأداء**

يوضح الجدول 4 نسبة التوافق بين نتائج التصنيف للنموذج ResNet-20 الحافظ للخصوصية المطبق ونتائج ResNet-20 الأصلي، مما يُظهر نتائج متطابقة تقريبًا. نختبر الاستدلال على 75 صورة مشفرة، ويُقترح فترة ثقة 95% لكل نتيجة. نتيجة واحدة فقط من نموذجنا المقترح للبيانات المشفرة تُظهر نتيجة مختلفة عن نتيجة نموذج ResNet-20 لبيانات النص الواضح. بعبارة أخرى، نسبة التوافق هي 98.67%± 2.59%، وهي نتيجة توافق عالية كافية. دقة التصنيف لـ ResNet-20 للبيانات المشفرة هي 90.67%± 6.58%، بينما دقة ResNet-20 الأصلي للصورة المقابلة بالنص الواضح هي 89.33%± 6.99%. وبالتالي، نتحقق من أن ResNet-20 يمكن تنفيذه بنجاح باستخدام مخطط RNS-CKKS بدقة كافية للتصنيف وعملية التمهيد الذاتي المناسبة. لاحظ أن أعلى دقة تصنيف للنموذج السابق لمجموعة بيانات CIFAR-10 على مخطط FHE الكلمي هي 77% فقط [19].

**الجدول 4: دقة تصنيف ResNet-20 للنص الواضح والنص المشفر ونسبة التوافق**

| النموذج | ResNet-20¹ | ResNet-20² | PPML ResNet-20 | التوافق |
|---------|------------|------------|----------------|---------|
| الدقة | 91.89% ± 0.54% | 89.33% ± 6.99% | 90.67% ± 6.58% | 98.67%± 2.59% |

¹ دقة التصنيف تم التحقق منها بـ 10,000 صورة.
² دقة التصنيف تم التحقق منها بـ 75 صورة والتي تُستخدم لاختبار ResNet-20 على الصور المشفرة.

يوضح الجدول 5 وقت التشغيل لـ ResNet-20 بالكامل ونسبة كل مكون في النموذج. يستغرق النموذج المقترح حوالي 4 ساعات للاستدلال على صورة واحدة، والمكونات الأكثر استهلاكًا للوقت هي الالتفاف وReLU والتمهيد الذاتي.

**الجدول 5: وقت تشغيل ResNet-20 والنسبة المئوية للوقت المستغرق في كل مكون بالنسبة للوقت الإجمالي**

| الطبقة | PC | BN | CR | Boot | AP + FC | Softmax | الوقت الإجمالي (ثانية) |
|--------|----|----|----|----|---------|---------|------------------------|
| نسبة الوقت | 34.30% | 0.20% | 32.63% | 29.97% | 0.06% | 2.83% | 14,694 |

---

### Translation Notes

- **Tables referenced:** Table 4 (accuracy comparison), Table 5 (runtime breakdown)
- **Key results:**
  - 98.67% agreement ratio with plaintext ResNet-20
  - 90.67% accuracy on encrypted data (vs. 77% previous best)
  - ~4 hours inference time (14,694 seconds)
  - Convolution (34.30%), ReLU (32.63%), and Bootstrapping (29.97%) are most expensive
- **Equations:** None
- **Citations:** [14, 19, 30]
- **Special handling:**
  - Statistical confidence intervals preserved
  - Performance metrics precisely translated
  - Component abbreviations: PC (Processing/Convolution), BN (Batch Normalization), CR (likely ConvReLU), Boot (Bootstrapping), AP (Average Pooling), FC (Fully Connected)

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.87
- **Overall section score:** 0.87
