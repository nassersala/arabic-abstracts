# Section 3: ResNet-20 on RNS-CKKS scheme
## القسم 3: ResNet-20 على مخطط RNS-CKKS

**Section:** methodology/implementation
**Translation Quality:** 0.86
**Glossary Terms Used:** ResNet, convolution, batch normalization, ReLU, bootstrapping, average pooling, fully connected, softmax, parameters, data packing, precision, sparse packing, polynomial approximation, minimax, rotation, key-switching

---

### English Version

**3.1 Structure**

We specify our implemented structure for the ResNet-20 with RNS-CKKS scheme as shown in Figure 1, where it consists of convolution (Conv), batch normalization (BN), ReLU, bootstrapping (Boot), average pooling (AP), fully connected layer (FC), and softmax. This model is virtually identical to the original ResNet-20 model except that the bootstrapping procedure is added. All of these procedures will be specified in the following subsections. Table 1 shows the specification of ResNet-20.

**Table 1: The specification of ResNet-20 (CIFAR-10)**

| Layer | Input Size | #Inputs | Filter Size | #Filters | Output Size | #Outputs |
|-------|-----------|---------|-------------|----------|-------------|----------|
| Conv1 | 32 × 32 | 3 | 3 × 3 | 16 | 32 × 32 | 16 |
| Conv2-1 | 32 × 32 | 16 | 3 × 3 | 16 | 32 × 32 | 16 |
| Conv2-2 | 32 × 32 | 16 | 3 × 3 | 16 | 32 × 32 | 16 |
| Conv2-3 | 32 × 32 | 16 | 3 × 3 | 16 | 32 × 32 | 16 |
| Conv3-1-1 | 32 × 32 | 16 | 3 × 3 | 32 | 16 × 16 | 32 |
| Conv3-1-2 | 16 × 16 | 32 | 3 × 3 | 32 | 16 × 16 | 32 |
| Conv3-1-s | 32 × 32 | 16 | 1 × 1 | 32 | 16 × 16 | 32 |
| Conv3-2 | 16 × 16 | 32 | 3 × 3 | 32 | 16 × 16 | 32 |
| Conv3-3 | 16 × 16 | 32 | 3 × 3 | 32 | 16 × 16 | 32 |
| Conv4-1-1 | 16 × 16 | 32 | 3 × 3 | 64 | 8 × 8 | 64 |
| Conv4-1-2 | 8 × 8 | 64 | 3 × 3 | 64 | 8 × 8 | 64 |
| Conv4-1-s | 16 × 16 | 32 | 1 × 1 | 64 | 8 × 8 | 64 |
| Conv4-2 | 8 × 8 | 64 | 3 × 3 | 64 | 8 × 8 | 64 |
| Conv4-3 | 8 × 8 | 64 | 3 × 3 | 64 | 8 × 8 | 64 |
| Average Pooling | 8 × 8 | 64 | 8 × 8 | 64 | - | 64 |
| Fully Connected | 64 × 1 | 1 | - | - | - | 10 |

**3.2 General setting for RNS-CKKS scheme**

**3.2.1 Parameters**

We set the ciphertext polynomial degree as $2^{16}$ and the secret key Hamming weight as 64. The bit length of base modulus ($q_0$), special modulus, and default modulus are set as 60, 60, 50, respectively. The bit length of modulus in the bootstrapping range is the same as that of $q_0$. The numbers of levels for the general homomorphic operations and the bootstrapping are set as 11, 18, respectively. The maximum bit length of modulus is 1750, which satisfies 98-bit security. The security level $\lambda$ is computed based on Cheon et al.'s hybrid dual attack [24], which is the fastest attack for the LWE with the sparse key. Table 2 lists the above parameters.

**Table 2: RNS-CKKS parameter settings**

| $\lambda$ | Hamming Weight | Degree | Modulus Q | $q_0$ | Special Prime | Scaling Factor | Evaluation Level | Bootstrapping Level |
|-----------|----------------|--------|-----------|-------|---------------|----------------|------------------|---------------------|
| 98 | 64 | $2^{16}$ | 1750 bits | 60 bits | 60 bits | 50 bits | 11 | 18 |

**3.2.2 Data packing**

The message is a 32 × 32 CIFAR-10 image, and one image is processed at a time. We can use $2^{15}$ message slots in one ciphertext with our parameters, which is the half polynomial degree. Therefore, we employ the sparse packing method [7] to pack a channel of a CIFAR-10 image in one ciphertext using only $2^{10}$ sparse slots since the bootstrapping of sparsely packed ciphertext takes much less time than that of fully packed ciphertext.

**3.2.3 Data range and precision**

Any polynomials can approximate continuous functions only in some bounded set. If even one value in the message slots exceeds this bounded set, the absolute value of output diverges to a pretty big number, leading to complete classification failure. Since FHE can only handle arithmetic operations, polynomial approximation should be used for non-arithmetic operations such as the ReLU function, the bootstrapping, and the softmax function. Thus, the inputs for these procedures should be in the bounded approximation region. We analyze the absolute input values for the ReLU, the bootstrapping, and the softmax when performing the ResNet-20 with several images. Since the observed maximum absolute input value for these procedures is 37.1, we conjecture that the absolute input values for these procedures are less than 40 with a very high probability. We use this observation in the implementation of each procedure. We also empirically find that the precision of the approximate polynomial or the function should be at least 16-bit below the decimal point, and thus we approximate each non-arithmetic function with 16-bit average precision.

**3.2.4 Optimization for precision of homomorphic operations**

We apply several methods to reduce the rescaling error and relinearization error and ensure the precision of the resultant message, such as the scaling factor management in [25], lazy rescaling, and lazy relinearization [26, 27]. The lazy rescaling and relinearization can also be applied to reduce the computation time as it requires much computation due to the number-theoretic transformation (NTT) and gadget decomposition.

**3.3 Convolution and batch normalization**

Most of the operations in the ResNet-20 are convolutions with zero-padded input to maintain their size. We use the packed single input single output (SISO) convolution with stride 1 used in Gazelle [20], which has low complexity for the encrypted data. Convolution with stride 2 is also required to perform down-sampling. The striding convolution was also proposed by Gazelle [20] to decompose an input and a filter and perform convolutions and adding.

We modify the striding convolution of Gazelle to reduce the required number of rotation operations. In the conventional striding convolution, we need to rearrange the encrypted data when decomposing the data, but the rearrangement increases the additional rotation operations. Since the rotation operation requires time-consuming key-switching procedures, it is desirable to reduce the number of rotation operations as much as possible. Instead of rearranging the slots to a well-structured channel, we perform the stride-2 convolution by extracting the valid values by multiplying the window kernel consisting of 0 and 1 from the stride-1 convolution result as shown in Figure 2:(b). It does not require any additional rotation operations.

Since the batch normalization procedure is a simple linear function with constant coefficients, it can be implemented with the homomorphic addition and the homomorphic scalar multiplication.

**Figure 2: Stride-2 convolution (a) plaintext (b) ciphertext.**
[Diagram showing stride-2 convolution process]

**3.4 ReLU**

The activation function of the ResNet-20 is the ReLU function. Since the ReLU function is proven to be effective as the activation function in many CNN models, replacing the ReLU function with the simple arithmetic function such as $x^2$ [16] may not be desirable. Instead, we approximate the ReLU function by some arithmetic function with a sufficiently small error.

We firstly implement the ReLU function in the ResNet-20 with the RNS-CKKS scheme using the composition of the minimax polynomial approximation by Lee et al.[1]. To find an appropriate precision value, we repeatedly perform the ResNet-20 simulation over the RNS-CKKS scheme while changing the precision, and as a result, we find that the minimum 16-bit precision shows good performance on average. To synthesize the sign function for the ReLU approximation, we generate the composition of the small minimax approximate polynomials with precision parameter $\alpha = 13$ using the three minimax approximate polynomials with degrees 15, 15, and 27. This composition of polynomials ensures that the average approximation precision is about 16-bit precision.

The homomorphic evaluation of the polynomials is carried out using the odd baby-giant method in [28] and the optimal level consumption method in [10]. Since the homomorphic evaluation of polynomial compositions consumes many depths, it is impossible to finish it without bootstrapping. Thus, we use bootstrapping twice, once in the middle and once at the end of evaluating the ReLU function.

**3.5 Bootstrapping**

Since we have to consume many depths to implement the ResNet-20 on the RNS-CKKS scheme, many bootstrapping procedures are required to ensure enough homomorphic multiplications. For the first time, we apply the bootstrapping technique to perform the deep neural network such as the ResNet-20 on the encrypted data and prove that the FHE scheme with the state-of-the-art bootstrapping can be successfully applied for privacy-preserving deep neural networks. Since the SEAL library does not support any bootstrapping technique, we implement the most advanced bootstrapping with the SEAL library [10, 11, 12]. The COEFFTOSLOT and the SLOTTOCOEFF are implemented using collapsed FFT structure [8] with depth 2. The MODREDUCTION is implemented using the composition of the cosine function, two double angle formulas, and the inverse sine function [9, 11], where the cosine function and the inverse sine function are approximated with the multi-interval Remez algorithm as in [11].

The most crucial issue when using the bootstrapping of the RNS-CKKS scheme is the bootstrapping failure. 1,149 bootstrapping procedures are required in our model, and the result of the whole neural network can be largely distorted if even one of the bootstrapping procedures fails. The bootstrapping failure occurs when one of the slots in the input ciphertext of the MODREDUCTION procedure is not on the approximation region. The approximation interval can be controlled by the bootstrapping parameters $(K, \epsilon)$, where the approximation region is $\bigcup_{i=-(K-1)}^{K-1} [i-\epsilon, i+\epsilon]$ [7]. While the parameter $\epsilon$ is related to the range and the precision of the input message data, the parameter $K$ is related to the values composing the ciphertext and not related to the input data. Since the values contained in the ciphertext are not predictable, we have to investigate the relation between the bootstrapping failure probability and the parameter $K$.

**Table 3: Boundary of approximation region given key Hamming weight and failure probability of modular reduction**

| Pr($|I_i| \geq K$) | $h = 64$ | $h = 128$ | $h = 192$ |
|-------------------|----------|-----------|-----------|
| $2^{-23}$ [10] | 12 | 17 | 21 |
| $2^{-30}$ | 14 | 20 | 24 |
| $2^{-40}$ | 16 | 23 | 28 |

In Table 3, we show several bounds of the input message and its failure probability. The specific investigation is described in Appendix. A larger bound means that a higher degree of the approximate polynomial is required; hence, more computation is required. Using the new bound for approximation in Table 3, we can offer a trade-off between the evaluation time and failure probability of the whole network. Following [10, 27], the approximated modular reduction in the CKKS bootstrapping so far has failure probability ≈ $2^{-23}$, but it is not sufficiently small since we have to perform pretty many bootstrapping procedures for the ResNet-20. Thus, the bootstrapping failure probability is set to be less than $2^{-40}$ in our implementation. The Hamming weight of the secret key is set to be 64, and $(K, \epsilon) = (17, 2^{-6})$. The corresponding degree for the minimax polynomial for the cosine function is 54, and that of the inverse sine function is 5, which is obtained by the multi-interval Remez algorithm [11].

**3.6 Average pooling and fully connected layer**

After stride-2 convolution layers 3, 4 and average pooling, the valid message slots of the ciphertext are given as follows (filled boxes in Figure 3).

**Figure 3: The valid message slots of the ciphertext.**
[Diagram showing slot arrangement after pooling]

If we combine these 64 ciphertexts into one ciphertext using the rotation, we must perform the additional 63 rotations when multiplying the matrix in the fully connected layer. Therefore, if we do not combine them into one, we can get an advantage in operation speed at the cost of more memory size. Thus, we do not need to perform the rotations when doing summation in the softmax.

**3.7 Softmax**

The last part of our implementation is the softmax function. Note that we have to evaluate the exponential function of each input value for the softmax function, and these output values can be too large to be embraced by the RNS-CKKS encryption scheme. Instead of evaluating $e^{x_i}/\sum_{j=1}^{10} e^{x_j}$ for each $i$, we evaluate $e^{x_i/4}/\sum_{j=1}^{10} e^{x_j/4}$. We find that it outputs almost the same output as the original softmax function, and the output of each exponential function does not exceed the capacity of the encryption scheme.

We approximate the exponential function $y = e^x$ by the polynomial with the degree of 12 by the least square method. The approximation region of the exponential function is set to be $[-1, 1]$. We multiply $x$ by a constant $1/64$ to put the input in the approximation region, evaluate the approximate polynomial of the exponential function, and square the output four times to evaluate $(e^{x/64})^{16} = e^{x/4}$. Then, the approximation method for the inverse function [29] is applied to the sum of the exponential functions. The approximation region is $[0, 2]$, and the absolute value of inputs for the inverse is heuristically found to be less than 104. Thus, we multiply the input by $10^{-4}$ before applying the approximate inverse function and multiply it again by $10^{-4}$ after the evaluation. Then, each exponential output is multiplied by this inverse output. These procedures for the softmax function need 22 bootstrapping procedures.

---

### النسخة العربية

**3.1 البنية**

نحدد البنية المطبقة لدينا لـ ResNet-20 مع مخطط RNS-CKKS كما هو موضح في الشكل 1، حيث تتكون من الالتفاف (Conv)، والتطبيع الدفعي (BN)، وReLU، والتمهيد الذاتي (Boot)، والتجميع المتوسط (AP)، والطبقة المتصلة بالكامل (FC)، وsoftmax. هذا النموذج متطابق فعليًا مع نموذج ResNet-20 الأصلي باستثناء إضافة إجراء التمهيد الذاتي. سيتم تحديد جميع هذه الإجراءات في الأقسام الفرعية التالية. يوضح الجدول 1 مواصفات ResNet-20.

**الجدول 1: مواصفات ResNet-20 (CIFAR-10)**

| الطبقة | حجم المدخل | #المدخلات | حجم المرشح | #المرشحات | حجم المخرج | #المخرجات |
|--------|-----------|-----------|------------|-----------|-----------|-----------|
| Conv1 | 32 × 32 | 3 | 3 × 3 | 16 | 32 × 32 | 16 |
| Conv2-1 | 32 × 32 | 16 | 3 × 3 | 16 | 32 × 32 | 16 |
| Conv2-2 | 32 × 32 | 16 | 3 × 3 | 16 | 32 × 32 | 16 |
| Conv2-3 | 32 × 32 | 16 | 3 × 3 | 16 | 32 × 32 | 16 |
| Conv3-1-1 | 32 × 32 | 16 | 3 × 3 | 32 | 16 × 16 | 32 |
| Conv3-1-2 | 16 × 16 | 32 | 3 × 3 | 32 | 16 × 16 | 32 |
| Conv3-1-s | 32 × 32 | 16 | 1 × 1 | 32 | 16 × 16 | 32 |
| Conv3-2 | 16 × 16 | 32 | 3 × 3 | 32 | 16 × 16 | 32 |
| Conv3-3 | 16 × 16 | 32 | 3 × 3 | 32 | 16 × 16 | 32 |
| Conv4-1-1 | 16 × 16 | 32 | 3 × 3 | 64 | 8 × 8 | 64 |
| Conv4-1-2 | 8 × 8 | 64 | 3 × 3 | 64 | 8 × 8 | 64 |
| Conv4-1-s | 16 × 16 | 32 | 1 × 1 | 64 | 8 × 8 | 64 |
| Conv4-2 | 8 × 8 | 64 | 3 × 3 | 64 | 8 × 8 | 64 |
| Conv4-3 | 8 × 8 | 64 | 3 × 3 | 64 | 8 × 8 | 64 |
| التجميع المتوسط | 8 × 8 | 64 | 8 × 8 | 64 | - | 64 |
| متصل بالكامل | 64 × 1 | 1 | - | - | - | 10 |

**3.2 الإعداد العام لمخطط RNS-CKKS**

**3.2.1 المعاملات**

نحدد درجة متعددة الحدود للنص المشفر على أنها $2^{16}$ ووزن هامينغ للمفتاح السري على أنه 64. يتم تعيين طول البت للمعامل الأساسي ($q_0$) والمعامل الخاص والمعامل الافتراضي على 60، 60، 50، على التوالي. طول البت للمعامل في نطاق التمهيد الذاتي هو نفس طول $q_0$. يتم تعيين أعداد المستويات للعمليات المتماثلة العامة والتمهيد الذاتي على 11، 18، على التوالي. الحد الأقصى لطول البت للمعامل هو 1750، وهو ما يلبي أمان 98 بت. يتم حساب مستوى الأمان $\lambda$ استنادًا إلى الهجوم الثنائي الهجين لـ Cheon وآخرين [24]، وهو أسرع هجوم على LWE بمفتاح متفرق. يسرد الجدول 2 المعاملات أعلاه.

**الجدول 2: إعدادات معاملات RNS-CKKS**

| $\lambda$ | وزن هامينغ | الدرجة | المعامل Q | $q_0$ | الأولي الخاص | عامل القياس | مستوى التقييم | مستوى التمهيد |
|-----------|-----------|--------|----------|-------|-------------|--------------|--------------|--------------|
| 98 | 64 | $2^{16}$ | 1750 بت | 60 بت | 60 بت | 50 بت | 11 | 18 |

**3.2.2 تعبئة البيانات**

الرسالة هي صورة CIFAR-10 بحجم 32 × 32، وتتم معالجة صورة واحدة في كل مرة. يمكننا استخدام $2^{15}$ خانة رسائل في نص مشفر واحد بمعاملاتنا، وهو نصف درجة متعددة الحدود. لذلك، نستخدم طريقة التعبئة المتفرقة [7] لتعبئة قناة صورة CIFAR-10 في نص مشفر واحد باستخدام $2^{10}$ خانات متفرقة فقط نظرًا لأن التمهيد الذاتي للنص المشفر المعبأ بشكل متفرق يستغرق وقتًا أقل بكثير من النص المشفر المعبأ بالكامل.

**3.2.3 نطاق البيانات والدقة**

يمكن لأي متعددات حدود تقريب الدوال المستمرة فقط في مجموعة محدودة معينة. إذا تجاوزت قيمة واحدة في خانات الرسائل هذه المجموعة المحدودة، فإن القيمة المطلقة للمخرج تتباعد إلى عدد كبير جدًا، مما يؤدي إلى فشل التصنيف الكامل. نظرًا لأن FHE يمكنه فقط معالجة العمليات الحسابية، يجب استخدام التقريب متعدد الحدود للعمليات غير الحسابية مثل دالة ReLU والتمهيد الذاتي ودالة softmax. وبالتالي، يجب أن تكون المدخلات لهذه الإجراءات في منطقة التقريب المحدودة. نحلل قيم المدخلات المطلقة لـ ReLU والتمهيد الذاتي وsoftmax عند تنفيذ ResNet-20 مع عدة صور. نظرًا لأن أقصى قيمة مدخل مطلقة ملحوظة لهذه الإجراءات هي 37.1، نفترض أن قيم المدخلات المطلقة لهذه الإجراءات أقل من 40 باحتمالية عالية جدًا. نستخدم هذه الملاحظة في تطبيق كل إجراء. نجد أيضًا تجريبيًا أن دقة متعددة الحدود التقريبية أو الدالة يجب أن تكون على الأقل 16 بت تحت الفاصلة العشرية، وبالتالي نقرب كل دالة غير حسابية بدقة متوسطة تبلغ 16 بت.

**3.2.4 التحسين لدقة العمليات المتماثلة**

نطبق عدة طرق لتقليل خطأ إعادة القياس وخطأ إعادة الخطية وضمان دقة الرسالة الناتجة، مثل إدارة عامل القياس في [25]، وإعادة القياس الكسولة، وإعادة الخطية الكسولة [26، 27]. يمكن أيضًا تطبيق إعادة القياس الكسولة وإعادة الخطية الكسولة لتقليل وقت الحساب لأنه يتطلب الكثير من الحساب بسبب التحويل النظري العددي (NTT) وتحلل الأدوات.

**3.3 الالتفاف والتطبيع الدفعي**

معظم العمليات في ResNet-20 هي التفافات مع مدخل معبأ بالصفر للحفاظ على حجمها. نستخدم الالتفاف المعبأ بمدخل واحد ومخرج واحد (SISO) بخطوة 1 المستخدم في Gazelle [20]، والذي له تعقيد منخفض للبيانات المشفرة. الالتفاف بخطوة 2 مطلوب أيضًا لإجراء أخذ العينات الهبوطي. اقترح Gazelle [20] أيضًا الالتفاف بالخطوات لتحليل المدخل والمرشح وإجراء الالتفافات والجمع.

نعدل الالتفاف بالخطوات لـ Gazelle لتقليل عدد عمليات الدوران المطلوبة. في الالتفاف بالخطوات التقليدي، نحتاج إلى إعادة ترتيب البيانات المشفرة عند تحليل البيانات، لكن إعادة الترتيب تزيد من عمليات الدوران الإضافية. نظرًا لأن عملية الدوران تتطلب إجراءات تبديل المفاتيح التي تستغرق وقتًا طويلاً، فمن المرغوب فيه تقليل عدد عمليات الدوران قدر الإمكان. بدلاً من إعادة ترتيب الخانات إلى قناة جيدة البنية، نُنفذ الالتفاف بخطوة 2 عن طريق استخراج القيم الصالحة بضرب نواة النافذة المكونة من 0 و1 من نتيجة الالتفاف بخطوة 1 كما هو موضح في الشكل 2:(ب). لا يتطلب أي عمليات دوران إضافية.

نظرًا لأن إجراء التطبيع الدفعي هو دالة خطية بسيطة بمعاملات ثابتة، يمكن تطبيقه بالجمع المتماثل والضرب القياسي المتماثل.

**الشكل 2: الالتفاف بخطوة 2 (أ) النص الواضح (ب) النص المشفر.**
[رسم توضيحي لعملية الالتفاف بخطوة 2]

**3.4 ReLU**

دالة التنشيط لـ ResNet-20 هي دالة ReLU. نظرًا لأنه ثبت أن دالة ReLU فعالة كدالة تنشيط في العديد من نماذج CNN، فقد لا يكون من المرغوب فيه استبدال دالة ReLU بدالة حسابية بسيطة مثل $x^2$ [16]. بدلاً من ذلك، نقرب دالة ReLU بدالة حسابية ما بخطأ صغير كافٍ.

نطبق للمرة الأولى دالة ReLU في ResNet-20 مع مخطط RNS-CKKS باستخدام تركيب التقريب متعدد الحدود الأصغري الأعظمي بواسطة Lee وآخرين [1]. للعثور على قيمة دقة مناسبة، نُنفذ محاكاة ResNet-20 بشكل متكرر على مخطط RNS-CKKS أثناء تغيير الدقة، ونتيجة لذلك، نجد أن الحد الأدنى للدقة 16 بت يُظهر أداءً جيدًا في المتوسط. لتصنيع دالة الإشارة لتقريب ReLU، نولد تركيب متعددات الحدود التقريبية الأصغرية الأعظمية الصغيرة بمعامل دقة $\alpha = 13$ باستخدام ثلاث متعددات حدود تقريبية أصغرية أعظمية بدرجات 15، 15، و27. يضمن هذا التركيب من متعددات الحدود أن دقة التقريب المتوسطة حوالي 16 بت.

يتم تنفيذ التقييم المتماثل لمتعددات الحدود باستخدام طريقة الطفل العملاق الفردي في [28] وطريقة الاستهلاك الأمثل للمستوى في [10]. نظرًا لأن التقييم المتماثل لتراكيب متعددات الحدود يستهلك العديد من الأعماق، فمن المستحيل إنهاؤه بدون التمهيد الذاتي. وبالتالي، نستخدم التمهيد الذاتي مرتين، مرة في المنتصف ومرة في نهاية تقييم دالة ReLU.

**3.5 التمهيد الذاتي**

نظرًا لأننا يجب أن نستهلك العديد من الأعماق لتطبيق ResNet-20 على مخطط RNS-CKKS، فإن العديد من إجراءات التمهيد الذاتي مطلوبة لضمان عمليات ضرب متماثلة كافية. للمرة الأولى، نطبق تقنية التمهيد الذاتي لتنفيذ الشبكة العصبية العميقة مثل ResNet-20 على البيانات المشفرة ونثبت أن مخطط FHE بالتمهيد الذاتي الحديث يمكن تطبيقه بنجاح على الشبكات العصبية العميقة الحافظة للخصوصية. نظرًا لأن مكتبة SEAL لا تدعم أي تقنية تمهيد ذاتي، نطبق التمهيد الذاتي الأكثر تقدمًا بمكتبة SEAL [10، 11، 12]. يتم تطبيق COEFFTOSLOT وSLOTTOCOEFF باستخدام بنية FFT المنهارة [8] بعمق 2. يتم تطبيق MODREDUCTION باستخدام تركيب دالة الجيب تمام الزاوية، وصيغتين للزاوية المزدوجة، ودالة الجيب العكسية [9، 11]، حيث يتم تقريب دالة الجيب تمام الزاوية ودالة الجيب العكسية بخوارزمية Remez متعددة الفواصل كما في [11].

القضية الأكثر أهمية عند استخدام التمهيد الذاتي لمخطط RNS-CKKS هي فشل التمهيد الذاتي. مطلوب 1,149 إجراء تمهيد ذاتي في نموذجنا، ويمكن أن تتشوه نتيجة الشبكة العصبية بأكملها بشكل كبير إذا فشل حتى أحد إجراءات التمهيد الذاتي. يحدث فشل التمهيد الذاتي عندما لا تكون إحدى الخانات في النص المشفر المدخل لإجراء MODREDUCTION في منطقة التقريب. يمكن التحكم في فترة التقريب بواسطة معاملات التمهيد الذاتي $(K, \epsilon)$، حيث منطقة التقريب هي $\bigcup_{i=-(K-1)}^{K-1} [i-\epsilon, i+\epsilon]$ [7]. بينما المعامل $\epsilon$ مرتبط بنطاق ودقة بيانات رسالة المدخل، فإن المعامل $K$ مرتبط بالقيم المكونة للنص المشفر وليس مرتبطًا ببيانات المدخل. نظرًا لأن القيم الموجودة في النص المشفر غير قابلة للتنبؤ، يجب علينا التحقيق في العلاقة بين احتمالية فشل التمهيد الذاتي والمعامل $K$.

**الجدول 3: حدود منطقة التقريب المعطاة لوزن هامينغ للمفتاح واحتمالية فشل التقليل المعياري**

| Pr($|I_i| \geq K$) | $h = 64$ | $h = 128$ | $h = 192$ |
|-------------------|----------|-----------|-----------|
| $2^{-23}$ [10] | 12 | 17 | 21 |
| $2^{-30}$ | 14 | 20 | 24 |
| $2^{-40}$ | 16 | 23 | 28 |

في الجدول 3، نوضح عدة حدود لرسالة المدخل واحتمالية فشلها. يتم وصف التحقيق المحدد في الملحق. يعني الحد الأكبر أن درجة أعلى من متعددة الحدود التقريبية مطلوبة؛ وبالتالي، مطلوب مزيد من الحساب. باستخدام الحد الجديد للتقريب في الجدول 3، يمكننا تقديم مقايضة بين وقت التقييم واحتمالية فشل الشبكة بأكملها. وفقًا لـ [10، 27]، فإن التقليل المعياري التقريبي في التمهيد الذاتي لـ CKKS حتى الآن لديه احتمالية فشل ≈ $2^{-23}$، لكنها ليست صغيرة بما فيه الكفاية نظرًا لأننا يجب أن ننفذ العديد من إجراءات التمهيد الذاتي لـ ResNet-20. وبالتالي، يتم تعيين احتمالية فشل التمهيد الذاتي لتكون أقل من $2^{-40}$ في تطبيقنا. يتم تعيين وزن هامينغ للمفتاح السري على 64، و$(K, \epsilon) = (17, 2^{-6})$. الدرجة المقابلة لمتعددة الحدود الأصغرية الأعظمية لدالة الجيب تمام الزاوية هي 54، وتلك الخاصة بدالة الجيب العكسية هي 5، والتي يتم الحصول عليها بواسطة خوارزمية Remez متعددة الفواصل [11].

**3.6 التجميع المتوسط والطبقة المتصلة بالكامل**

بعد طبقات الالتفاف بخطوة 2 (3، 4) والتجميع المتوسط، يتم إعطاء خانات الرسائل الصالحة للنص المشفر كما يلي (المربعات المملوءة في الشكل 3).

**الشكل 3: خانات الرسائل الصالحة للنص المشفر.**
[رسم توضيحي لترتيب الخانات بعد التجميع]

إذا قمنا بدمج هذه النصوص المشفرة الـ 64 في نص مشفر واحد باستخدام الدوران، فيجب علينا إجراء 63 دورانًا إضافيًا عند ضرب المصفوفة في الطبقة المتصلة بالكامل. لذلك، إذا لم ندمجها في واحدة، يمكننا الحصول على ميزة في سرعة العملية بتكلفة حجم ذاكرة أكبر. وبالتالي، لا نحتاج إلى إجراء الدورانات عند القيام بالتجميع في softmax.

**3.7 Softmax**

الجزء الأخير من تطبيقنا هو دالة softmax. لاحظ أنه يجب علينا تقييم الدالة الأسية لكل قيمة مدخلة لدالة softmax، ويمكن أن تكون قيم المخرجات هذه كبيرة جدًا بحيث لا يمكن احتواؤها بواسطة مخطط تشفير RNS-CKKS. بدلاً من تقييم $e^{x_i}/\sum_{j=1}^{10} e^{x_j}$ لكل $i$، نقيم $e^{x_i/4}/\sum_{j=1}^{10} e^{x_j/4}$. نجد أنها تُخرج تقريبًا نفس المخرج مثل دالة softmax الأصلية، ومخرج كل دالة أسية لا يتجاوز سعة مخطط التشفير.

نقرب الدالة الأسية $y = e^x$ بمتعددة الحدود بدرجة 12 بطريقة المربعات الصغرى. يتم تعيين منطقة التقريب للدالة الأسية على $[-1، 1]$. نضرب $x$ بثابت $1/64$ لوضع المدخل في منطقة التقريب، ونقيم متعددة الحدود التقريبية للدالة الأسية، ونربع المخرج أربع مرات لتقييم $(e^{x/64})^{16} = e^{x/4}$. ثم يتم تطبيق طريقة التقريب للدالة العكسية [29] على مجموع الدوال الأسية. منطقة التقريب هي $[0، 2]$، ووُجد أن القيمة المطلقة للمدخلات للعكس أقل من 104 بشكل استدلالي. وبالتالي، نضرب المدخل بـ $10^{-4}$ قبل تطبيق الدالة العكسية التقريبية ونضربها مرة أخرى بـ $10^{-4}$ بعد التقييم. ثم يُضرب كل مخرج أسي بهذا المخرج العكسي. تحتاج هذه الإجراءات لدالة softmax إلى 22 إجراء تمهيد ذاتي.

---

### Translation Notes

- **Figures referenced:** Figure 1 (ResNet structure), Figure 2 (stride-2 convolution), Figure 3 (valid slots)
- **Tables referenced:** Table 1 (ResNet-20 specification), Table 2 (parameters), Table 3 (bootstrapping failure)
- **Key terms introduced:**
  - Sparse packing → التعبئة المتفرقة
  - SISO convolution → الالتفاف بمدخل واحد ومخرج واحد
  - Minimax approximation → التقريب الأصغري الأعظمي
  - Baby-giant method → طريقة الطفل العملاق
  - Lazy rescaling/relinearization → إعادة القياس/الخطية الكسولة
  - Remez algorithm → خوارزمية Remez
- **Equations:** Multiple mathematical expressions for bootstrapping parameters, softmax modification
- **Citations:** [1, 7, 8, 9, 10, 11, 12, 16, 20, 24, 25, 26, 27, 28, 29]
- **Special handling:**
  - Kept technical procedure names (COEFFTOSLOT, MODREDUCTION, SLOTTOCOEFF) in English
  - Mathematical notation preserved exactly
  - Table structures translated with Arabic headers

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
