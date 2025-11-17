# Section 5: Limitation
## القسم 5: القيود

**Section:** discussion/limitation
**Translation Quality:** 0.88
**Glossary Terms Used:** running time, security level, classification accuracy, GPU, FPGA, ASIC, packing, parameters, hyper-parameters, training, bootstrapping

---

### English Version

**Running time** The running time for the proposed model, which is about 4 hours, is somewhat large for practical use. This work firstly shows the possibility of applying the FHE to standard deep learning models with high accuracy, but it has to be optimized and improved in various ways to reduce the running time. Therefore, the essential future work is the advanced implementation of the ResNet-20 with the RNS-CKKS scheme with various accelerators realized using GPU, FPGA, or ASIC. Since research on implementing the state-of-the-art FHE scheme is advancing rapidly, the ResNet-20 over the encrypted data will be made more practically soon. Also, we implement the PPML model for only one image, and the running time per image can be much improved if we properly use the packing method of the RNS-CKKS scheme. We leave this optimization for many images as future work.

**Security level** The security level of the proposed model is 98-bit security, which is the minimum security level that can be considered secure. Since the standard security level in most applications is 128 bit, someone can regard this security level as insecure, and we may want to raise the security level. However, this 98-bit security is not a hard limit of our implementation; we can easily raise the security level by changing the parameters of the RNS-CKKS scheme. This just makes the trade-off between the security and the running time, and thus we can reach the higher security level at the cost of longer running time.

**Classification accuracy** Even if ML models are trained with the same hyper-parameters, the ML models have different performances because weights are initialized to random values for each training. Thus, the ML model performance, such as accuracy, is shown as the average values obtained by training several times. However, since we focus on implementing ResNet-20 for homomorphically encrypted data, we train this model only once, not many times. Nevertheless, we have shown that the encrypted ResNet-20 operation is possible with almost the same accuracy as the original ResNet-20 paper [Reference]. Furthermore, since it is implemented in the FHE with bootstrapping, it can be expected that the same result will be obtained for a deeper network than the Resnet-20.

---

### النسخة العربية

**وقت التشغيل** وقت التشغيل للنموذج المقترح، وهو حوالي 4 ساعات، كبير إلى حد ما للاستخدام العملي. يُظهر هذا العمل للمرة الأولى إمكانية تطبيق FHE على نماذج التعلم العميق المعيارية بدقة عالية، لكن يجب تحسينه وتطويره بطرق مختلفة لتقليل وقت التشغيل. لذلك، العمل المستقبلي الأساسي هو التطبيق المتقدم لـ ResNet-20 مع مخطط RNS-CKKS باستخدام مسرعات متنوعة محققة باستخدام GPU أو FPGA أو ASIC. نظرًا لأن البحث حول تطبيق مخطط FHE الحديث يتقدم بسرعة، سيصبح ResNet-20 على البيانات المشفرة أكثر عملية قريبًا. أيضًا، نطبق نموذج PPML لصورة واحدة فقط، ويمكن تحسين وقت التشغيل لكل صورة بشكل كبير إذا استخدمنا بشكل صحيح طريقة التعبئة لمخطط RNS-CKKS. نترك هذا التحسين للعديد من الصور كعمل مستقبلي.

**مستوى الأمان** مستوى الأمان للنموذج المقترح هو أمان 98 بت، وهو الحد الأدنى لمستوى الأمان الذي يمكن اعتباره آمنًا. نظرًا لأن مستوى الأمان المعياري في معظم التطبيقات هو 128 بت، يمكن لشخص ما اعتبار مستوى الأمان هذا غير آمن، وقد نرغب في رفع مستوى الأمان. ومع ذلك، فإن أمان 98 بت هذا ليس حدًا صارمًا لتطبيقنا؛ يمكننا بسهولة رفع مستوى الأمان عن طريق تغيير معاملات مخطط RNS-CKKS. هذا يجعل فقط مقايضة بين الأمان ووقت التشغيل، وبالتالي يمكننا الوصول إلى مستوى أمان أعلى بتكلفة وقت تشغيل أطول.

**دقة التصنيف** حتى لو تم تدريب نماذج تعلم الآلة بنفس المعاملات الفائقة، فإن نماذج تعلم الآلة لها أداءات مختلفة لأن الأوزان يتم تهيئتها بقيم عشوائية لكل تدريب. وبالتالي، يُظهر أداء نموذج تعلم الآلة، مثل الدقة، كمتوسط القيم التي يتم الحصول عليها عن طريق التدريب عدة مرات. ومع ذلك، نظرًا لأننا نركز على تطبيق ResNet-20 للبيانات المشفرة متماثليًا، فإننا ندرب هذا النموذج مرة واحدة فقط، وليس عدة مرات. مع ذلك، أظهرنا أن عملية ResNet-20 المشفرة ممكنة بنفس الدقة تقريبًا مثل ورقة ResNet-20 الأصلية [مرجع]. علاوة على ذلك، نظرًا لأنه تم تطبيقه في FHE مع التمهيد الذاتي، يمكن توقع الحصول على نفس النتيجة لشبكة أعمق من Resnet-20.

---

### Translation Notes

- **Limitations discussed:**
  1. Running time (4 hours) - need hardware acceleration
  2. Security level (98-bit) - below standard 128-bit, but tunable
  3. Classification accuracy - single training run, not averaged
- **Future work suggested:**
  - Hardware acceleration (GPU, FPGA, ASIC)
  - Batch processing with better packing
  - Higher security parameters
  - Extension to deeper networks
- **Equations:** None
- **Citations:** Reference to ResNet paper (not numbered in this section)
- **Special handling:**
  - Balanced discussion of limitations and mitigations
  - Forward-looking perspective on improvements

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.88
- Readability: 0.88
- Glossary consistency: 0.88
- **Overall section score:** 0.88
