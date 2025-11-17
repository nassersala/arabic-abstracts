# Section 2: Preliminaries
## القسم 2: المفاهيم الأولية

**Section:** preliminaries
**Translation Quality:** 0.87
**Glossary Terms Used:** CKKS scheme, RNS-CKKS, homomorphic operations, ciphertext, plaintext, encryption, real numbers, complex numbers, Ring-LWE, scaling factor, rescaling, modulus, bootstrapping, polynomial, slots

---

### English Version

**2.1 RNS-CKKS scheme**

The CKKS scheme [4] is an FHE scheme supporting the arithmetic operations on encrypted data over real or complex numbers. Any users with the public key can process the encrypted real or complex data with the CKKS scheme without knowing any private information. The security of the CKKS scheme is based on the Ring-LWE hardness assumption. The supported homomorphic operations are the addition, the multiplication, the rotation, and the complex conjugation operation, and each operation except the homomorphic rotation operation is applied component-wisely. The rotation operation homomorphically performs a cyclic shift of the vector by some step. The multiplication, rotation, and complex conjugation operations in the CKKS scheme need additional corresponding evaluation keys and the key-switching procedures. Each real number data is scaled with some big integer, called the scaling factor, and then rounded to the integer before encrypting the data. When the two data encrypted with the CKKS scheme are multiplied homomorphically, the scaling factors of the two data are also multiplied. This scaling factor should be reduced to the original value using the rescaling operation for the following operations.

Since the CKKS scheme needs pretty big integers, the original CKKS scheme uses a multi-precision library, which requires higher computational complexity. To reduce the complexity, the residue number system variant of the CKKS scheme [5], called the RNS-CKKS scheme, was also proposed. In the residue number system, the big integer is split into several small integers, and the addition and the multiplication of the original big integers are equivalent to the corresponding component-wise operations of the small integers. We use the RNS-CKKS scheme in this paper.

**2.2 Bootstrapping of CKKS scheme**

The rescaling operation reduces both the scaling factor and the ciphertext modulus, which is necessary for each homomorphic multiplication. After several consecutive multiplications, the ciphertext modulus cannot be reduced further at some point. The bootstrapping operation of the CKKS scheme [7] transforms the ciphertext with too small modulus into the fresh ciphertext with large modulus without changing the message. Therefore, any arithmetic circuits with large multiplicative depth can be obtained using the bootstrapping operation.

Since the bootstrapping operation of the CKKS scheme is the most time-consuming and erroneous operation among all homomorphic operations of the CKKS scheme, there have been many works improving the running time and the precision of the bootstrapping of the CKKS scheme [8, 9, 10, 11, 12]. With the development of the bootstrapping of the CKKS schemes, it can be used in practical applications. However, research on applying FHE with the state-of-the-art bootstrapping technique to the privacy-preserving deep neural network has not been done yet.

The bootstrapping of the CKKS scheme starts with raising the modulus of the ciphertext. Since the message polynomial is added with the product of some integer polynomial and the base modulus, the modular reduction of the coefficients of the message polynomial should be performed homomorphically. The ciphertext is transformed into the converted ciphertext that has the coefficients of the message polynomial as slots, called COEFFTOSLOT. Next, we perform the homomorphic modular reduction to the converted ciphertext, called MODREDUCTION. Then, it is transformed reversely into the ciphertext with the modular-reduced slots in the MODREDUCTION operation as the coefficients of the message polynomial, called SLOTTOCOEFF.

---

### النسخة العربية

**2.1 مخطط RNS-CKKS**

مخطط CKKS [4] هو مخطط تشفير متماثل كامل يدعم العمليات الحسابية على البيانات المشفرة على الأعداد الحقيقية أو المركبة. يمكن لأي مستخدم لديه المفتاح العام معالجة البيانات الحقيقية أو المركبة المشفرة بمخطط CKKS دون معرفة أي معلومات خاصة. يستند أمان مخطط CKKS على افتراض صعوبة Ring-LWE. العمليات المتماثلة المدعومة هي الجمع والضرب والدوران وعملية الاقتران المركب، وتُطبق كل عملية باستثناء عملية الدوران المتماثل بشكل مكونات. تُنفذ عملية الدوران بشكل متماثل إزاحة دورية للمتجه بخطوة معينة. تحتاج عمليات الضرب والدوران والاقتران المركب في مخطط CKKS إلى مفاتيح تقييم إضافية مقابلة وإجراءات تبديل المفاتيح. يتم قياس كل بيانات عدد حقيقي بعدد صحيح كبير، يُسمى عامل القياس، ثم يتم تقريبه إلى عدد صحيح قبل تشفير البيانات. عندما يتم ضرب البيانات المشفرة بمخطط CKKS بشكل متماثل، تُضرب أيضًا عوامل القياس للبيانات. يجب تقليل عامل القياس هذا إلى القيمة الأصلية باستخدام عملية إعادة القياس للعمليات التالية.

نظرًا لأن مخطط CKKS يحتاج إلى أعداد صحيحة كبيرة جدًا، يستخدم مخطط CKKS الأصلي مكتبة متعددة الدقة، مما يتطلب تعقيدًا حسابيًا أعلى. لتقليل التعقيد، تم اقتراح متغير نظام الأعداد المتبقية من مخطط CKKS [5]، المسمى مخطط RNS-CKKS. في نظام الأعداد المتبقية، يتم تقسيم العدد الصحيح الكبير إلى عدة أعداد صحيحة صغيرة، وجمع وضرب الأعداد الصحيحة الكبيرة الأصلية يعادل عمليات المكونات المقابلة للأعداد الصحيحة الصغيرة. نستخدم مخطط RNS-CKKS في هذا البحث.

**2.2 التمهيد الذاتي لمخطط CKKS**

تُقلل عملية إعادة القياس كلاً من عامل القياس ومعامل النص المشفر، وهو أمر ضروري لكل عملية ضرب متماثلة. بعد عدة عمليات ضرب متتالية، لا يمكن تقليل معامل النص المشفر بشكل أكبر عند نقطة معينة. تحول عملية التمهيد الذاتي لمخطط CKKS [7] النص المشفر بمعامل صغير جدًا إلى نص مشفر جديد بمعامل كبير دون تغيير الرسالة. لذلك، يمكن الحصول على أي دوائر حسابية بعمق ضربي كبير باستخدام عملية التمهيد الذاتي.

نظرًا لأن عملية التمهيد الذاتي لمخطط CKKS هي العملية الأكثر استهلاكًا للوقت والأكثر عرضة للأخطاء بين جميع العمليات المتماثلة لمخطط CKKS، كانت هناك العديد من الأعمال التي تحسن وقت التشغيل والدقة للتمهيد الذاتي لمخطط CKKS [8، 9، 10، 11، 12]. مع تطور التمهيد الذاتي لمخططات CKKS، يمكن استخدامه في التطبيقات العملية. ومع ذلك، لم يتم بعد إجراء بحث حول تطبيق FHE مع تقنية التمهيد الذاتي الحديثة على الشبكة العصبية العميقة الحافظة للخصوصية.

يبدأ التمهيد الذاتي لمخطط CKKS برفع معامل النص المشفر. نظرًا لأن متعددة حدود الرسالة تُضاف إلى حاصل ضرب متعددة حدود صحيحة ما والمعامل الأساسي، يجب إجراء التقليل المعياري لمعاملات متعددة حدود الرسالة بشكل متماثل. يتم تحويل النص المشفر إلى النص المشفر المحول الذي يحتوي على معاملات متعددة حدود الرسالة كخانات، يُسمى COEFFTOSLOT. بعد ذلك، نُنفذ التقليل المعياري المتماثل على النص المشفر المحول، يُسمى MODREDUCTION. ثم يتم تحويله عكسيًا إلى النص المشفر بالخانات المقللة معياريًا في عملية MODREDUCTION كمعاملات متعددة حدود الرسالة، يُسمى SLOTTOCOEFF.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - RNS-CKKS scheme → مخطط RNS-CKKS
  - Ring-LWE → Ring-LWE (kept in English with explanation)
  - Scaling factor → عامل القياس
  - Rescaling → إعادة القياس
  - Modulus → معامل
  - Key-switching → تبديل المفاتيح
  - Bootstrapping → التمهيد الذاتي
  - Slots → خانات
  - COEFFTOSLOT → COEFFTOSLOT (technical term kept)
  - MODREDUCTION → MODREDUCTION (technical term kept)
  - SLOTTOCOEFF → SLOTTOCOEFF (technical term kept)
- **Equations:** None (implicit mathematical descriptions)
- **Citations:** [4, 5, 7, 8, 9, 10, 11, 12]
- **Special handling:**
  - Technical procedure names (COEFFTOSLOT, MODREDUCTION, SLOTTOCOEFF) kept in English as they are standard FHE terminology
  - Ring-LWE kept in English as it's a standard cryptographic assumption name

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
