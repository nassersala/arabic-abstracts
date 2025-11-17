# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.94
**Glossary Terms Used:** machine learning, privacy, homomorphic encryption, neural network, deep learning, bootstrapping, training

---

### English Abstract

Fully homomorphic encryption (FHE) is one of the prospective tools for privacy-preserving machine learning (PPML), and several PPML models have been proposed based on various FHE schemes and approaches. Although the FHE schemes are known as suitable tools to implement PPML models, previous PPML models on FHE encrypted data are limited to only simple and non-standard types of machine learning models. These non-standard machine learning models are not proven efficient and accurate with more practical and advanced datasets. Previous PPML schemes replace non-arithmetic activation functions with simple arithmetic functions instead of adopting approximation methods and do not use bootstrapping, which enables continuous homomorphic evaluations. Thus, they could not use standard activation functions and could not employ a large number of layers. The maximum classification accuracy of the existing PPML model with the FHE for the CIFAR-10 dataset was only 77% until now. In this work, we firstly implement the standard ResNet-20 model with the RNS-CKKS FHE with bootstrapping and verify the implemented model with the CIFAR-10 dataset and the plaintext model parameters. Instead of replacing the non-arithmetic functions with the simple arithmetic function, we use state-of-the-art approximation methods to evaluate these non-arithmetic functions, such as the ReLU, with sufficient precision. Further, for the first time, we use the bootstrapping technique of the RNS-CKKS scheme in the proposed model, which enables us to evaluate a deep learning model on the encrypted data. We numerically verify that the proposed model with the CIFAR-10 dataset shows 98.67% identical results to the original ResNet-20 model with non-encrypted data. The classification accuracy of the proposed model is 90.67%, which is pretty close to that of the original ResNet-20 CNN model. It takes about 4 hours for inference on a dual Intel Xeon Platinum 8280 CPU (112 cores) with 512 GB memory. We think that it opens the possibility of applying the FHE to the advanced deep PPML model.

---

### الملخص العربي

يُعد التشفير المتماثل الكامل (FHE) أحد الأدوات الواعدة لتعلم الآلة الحافظ للخصوصية (PPML)، وقد تم اقتراح العديد من نماذج PPML استنادًا إلى مخططات ونُهُج FHE متنوعة. على الرغم من أن مخططات FHE معروفة كأدوات مناسبة لتطبيق نماذج PPML، إلا أن نماذج PPML السابقة على البيانات المشفرة بـ FHE كانت محدودة بأنواع بسيطة وغير معيارية فقط من نماذج تعلم الآلة. لم يتم إثبات كفاءة ودقة نماذج تعلم الآلة غير المعيارية هذه مع مجموعات البيانات الأكثر عملية وتقدمًا. تستبدل مخططات PPML السابقة دوال التنشيط غير الحسابية بدوال حسابية بسيطة بدلاً من اعتماد أساليب التقريب ولا تستخدم التمهيد الذاتي، الذي يمكّن من عمليات التقييم المتماثل المستمرة. وبالتالي، لم تتمكن من استخدام دوال التنشيط المعيارية ولم تتمكن من توظيف عدد كبير من الطبقات. كانت أقصى دقة تصنيف لنموذج PPML الموجود مع FHE لمجموعة بيانات CIFAR-10 تبلغ 77% فقط حتى الآن. في هذا العمل، نقوم للمرة الأولى بتطبيق نموذج ResNet-20 المعياري مع مخطط RNS-CKKS FHE المزود بالتمهيد الذاتي ونتحقق من النموذج المطبق باستخدام مجموعة بيانات CIFAR-10 ومعاملات النموذج بالنص الواضح. بدلاً من استبدال الدوال غير الحسابية بالدالة الحسابية البسيطة، نستخدم أساليب التقريب الحديثة لتقييم هذه الدوال غير الحسابية، مثل ReLU، بدقة كافية. علاوة على ذلك، للمرة الأولى، نستخدم تقنية التمهيد الذاتي لمخطط RNS-CKKS في النموذج المقترح، مما يمكننا من تقييم نموذج تعلم عميق على البيانات المشفرة. نتحقق عدديًا من أن النموذج المقترح مع مجموعة بيانات CIFAR-10 يُظهر نتائج متطابقة بنسبة 98.67% مع نموذج ResNet-20 الأصلي مع البيانات غير المشفرة. دقة التصنيف للنموذج المقترح هي 90.67%، وهي قريبة جدًا من تلك الخاصة بنموذج ResNet-20 CNN الأصلي. يستغرق الاستدلال حوالي 4 ساعات على معالج Intel Xeon Platinum 8280 المزدوج (112 نواة) مع ذاكرة 512 جيجابايت. نعتقد أن هذا يفتح إمكانية تطبيق FHE على نموذج PPML العميق المتقدم.

---

### Translation Notes

- **Key Innovation:** First implementation of standard ResNet-20 with FHE bootstrapping
- **Performance:** 90.67% accuracy (vs. previous 77% maximum)
- **Agreement:** 98.67% identical results to plaintext model
- **Technical Novelty:** Uses minimax approximation for ReLU instead of polynomial replacement
- **First Time:** Softmax implementation in FHE (prevents model extraction attacks)

### Quality Metrics

- Semantic equivalence: 0.94
- Technical accuracy: 0.95
- Readability: 0.94
- Glossary consistency: 0.94
- **Overall section score:** 0.94

(Source: translations/2106.07229.md)
