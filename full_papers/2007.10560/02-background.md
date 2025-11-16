# Section 2: Background
## القسم 2: الخلفية

**Section:** Background
**Translation Quality:** 0.87
**Glossary Terms Used:** federated learning, homomorphic encryption, privacy-preserving, distributed, neural network, deep learning, linear model, transfer learning, matrix factorization, activation function, approximation, Paillier cryptosystem, public key, private key, modular exponentiation, modular multiplication, Montgomery algorithm, FPGA

---

### English Version

## 2.1 Federated learning with HE

Federated learning is a privacy-preserving, decentralized distributed machine learning paradigm. One effective method of preserving privacy and securing computation is homomorphic encryption (HE), i.e. encryption schemes that allows encrypted values to be involved in computation. For the applications of HE in federated learning, we refer the readers to [Hardy et al., 2017], [Gilad-Bachrach et al., 2016], [Aono et al., 2017], [Liu et al., 2019], [Liu et al., 2018], [Chai et al., 2019], which broadly cover machine learning models including linear model, neural network and deep learning, boosting tree, transfer learning and matrix factorization. Typically, HE is employed to encrypt the intermediate data during computation, which will then be transferred and aggregated by homomorphic operation. For nonlinear operations composing the model, such as activation function in a neural network, these works usually rely on approximation to make the model agree with HE computation.

## 2.2 Privacy-preserving ML systems

There has also been machine learning systems that take privacy preservation into account, such as SecureML [Mohassel and Zhang, 2017] that proposes a system for two non-colluding party collectively training a model, and Sage [L'ecuyer et al., 2019] that presents a differentially private machine learning platform. Among them, FATE [FAT, 2019] introduces a federated learning framework that provides the abstraction and utilities for implementing algorithm and models, along with an architecture to enable distributed, multiparty machine learning. It mainly utilizes Paillier homomorphic encryption to guarantee data security. However, it purely relies on a software solution of encryption that greatly harms the execution efficiency of federated training. Our goal in the work is to find a hardware solution as a rescue to this issue.

## 2.3 Paillier Homomorphic Encryption

Paillier HE is an additive homomorphic encryption scheme allowing to perform addition and multiplication with scalar on encrypted values without decrypting them. In federated learning, usually multiple parties are involved, each one having a private dataset and wanting to maintain a local model learned from the aggregated dataset, and there may be a coordinator to manage the computation and data exchange among parties (Figure 1). The role of Paillier homomorphic encryption is to encrypt the intermediate data to transfer, so that in each training iteration the coordinator receives the encrypted local updates from parties, aggregates them with the homomorphic property, and sends back the result to each party for decryption and updating local model. In this way, each party obtain a model extracting information from the aggregate dataset, without leaking its private information.

The Paillier HE scheme associates each party with a public key $(n, g)$ and a private key $(\lambda, \mu)$, where $n, g, \lambda, \mu$ are large integers, typically 1024-bit in FATE. Messages and ciphertexts are also represented as long integers. A message $m$ can be encrypted into ciphertext $c$ by $c = g^m r^n \mod n^2$ with random number $r$, and decryption is performed by $m = ((c^\lambda \mod n^2) - 1) / n \mod n^2$.

We can see from the formulation that the majority of the computation of the Paillier en/decryption is related to modular exponentiation (ModExp), which can be further decomposed to a series of ModMult operations. Hence, the execution of ModMult has a decisive effect on the overall performance. We choose the Montgomery ModMult algorithm [Montgomery, 1985] to perform this operation because it is FPGA-friendly, in that it disposes of the costly integer division. The Montgomery algorithm, shown in Algorithm 1, computes $XY2^{-l} \mod M$ for $l$-bit integers $X, Y$ and $M$. It divides integers into $k$-bit words. The body of the algorithm is a two-level loop, where each outer iteration (line 2-8) aims to compute an intermediate result $S_i = XY_i2^{-k} \mod M$ for the $i$-th word of $Y$, and it further decomposes the computation by each word of $X$ and forms the inner loop (line 4-6).

**Algorithm 1:** Montgomery Algorithm for Modular Multiplication with Radix $2^k$

**Input:** $X = \sum_{j=0}^{l/k-1} X_j 2^{jk}$, $Y = \sum_{j=0}^{l/k-1} Y_j 2^{jk}$, $M = \sum_{j=0}^{l/k-1} M_j 2^{jk}$, $r = 2^k$

**Output:** $S = XY/2^l \mod M$

1. $S_0 \leftarrow 0$;
2. **for** $i = 0 \ldots l/k-1$ **do**
3. &nbsp;&nbsp;&nbsp;&nbsp;$q \leftarrow ((S_i + XY_i)(-M^{-1})) \mod r$;
4. &nbsp;&nbsp;&nbsp;&nbsp;**for** $j = 0 \ldots l/k$ **do**
5. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$S_{i+1}^j \leftarrow S_i^j + X_j Y_i + q M_j$;
6. &nbsp;&nbsp;&nbsp;&nbsp;**end**
7. &nbsp;&nbsp;&nbsp;&nbsp;$S_{i+1} \leftarrow S_{i+1}/2^k$
8. **end**
9. **if** $S_{l/k} > M$ **then**
10. &nbsp;&nbsp;&nbsp;&nbsp;$S_{l/k} \leftarrow S_{l/k} - M$;
11. **end**
12. **return** $S_{l/k}$

---

### النسخة العربية

## 2.1 التعلم الاتحادي مع التشفير المتماثل

التعلم الاتحادي هو نموذج تعلم آلي موزع لا مركزي يحافظ على الخصوصية. إحدى الطرق الفعالة للحفاظ على الخصوصية وتأمين الحساب هي التشفير المتماثل (HE)، أي أنظمة التشفير التي تسمح بإشراك القيم المشفرة في الحساب. بالنسبة لتطبيقات التشفير المتماثل في التعلم الاتحادي، نحيل القراء إلى [Hardy et al., 2017]، [Gilad-Bachrach et al., 2016]، [Aono et al., 2017]، [Liu et al., 2019]، [Liu et al., 2018]، [Chai et al., 2019]، والتي تغطي على نطاق واسع نماذج التعلم الآلي بما في ذلك النموذج الخطي، والشبكة العصبية والتعلم العميق، وشجرة التعزيز، والتعلم بالنقل، وتحليل المصفوفات. عادةً، يُستخدم التشفير المتماثل لتشفير البيانات الوسيطة أثناء الحساب، والتي يتم نقلها وتجميعها بعد ذلك بواسطة العملية المتماثلة. بالنسبة للعمليات غير الخطية المكونة للنموذج، مثل دالة التنشيط في الشبكة العصبية، تعتمد هذه الأعمال عادةً على التقريب لجعل النموذج متوافقاً مع حساب التشفير المتماثل.

## 2.2 أنظمة التعلم الآلي التي تحافظ على الخصوصية

كانت هناك أيضاً أنظمة تعلم آلي تأخذ الحفاظ على الخصوصية في الاعتبار، مثل SecureML [Mohassel and Zhang, 2017] الذي يقترح نظاماً لطرفين غير متواطئين لتدريب نموذج بشكل جماعي، وSage [L'ecuyer et al., 2019] الذي يقدم منصة تعلم آلي خاصة تفاضلياً. من بينها، يُقدم FATE [FAT, 2019] إطار عمل تعلم اتحادي يوفر التجريد والأدوات لتنفيذ الخوارزميات والنماذج، إلى جانب معمارية لتمكين التعلم الآلي الموزع متعدد الأطراف. يستخدم بشكل رئيسي تشفير Paillier المتماثل لضمان أمان البيانات. ومع ذلك، فإنه يعتمد بشكل كامل على حل برمجي للتشفير يضر بشكل كبير بكفاءة تنفيذ التدريب الاتحادي. هدفنا في العمل هو إيجاد حل أجهزة كإنقاذ لهذه المشكلة.

## 2.3 تشفير Paillier المتماثل

تشفير Paillier المتماثل هو نظام تشفير متماثل جمعي يسمح بإجراء الجمع والضرب بقيمة قياسية على القيم المشفرة دون فك تشفيرها. في التعلم الاتحادي، عادةً ما يكون هناك عدة أطراف متضمنة، كل واحد لديه مجموعة بيانات خاصة ويريد الحفاظ على نموذج محلي تم تعلمه من مجموعة البيانات المجمعة، وقد يكون هناك منسق لإدارة الحساب وتبادل البيانات بين الأطراف (الشكل 1). دور تشفير Paillier المتماثل هو تشفير البيانات الوسيطة للنقل، بحيث في كل تكرار تدريب يتلقى المنسق التحديثات المحلية المشفرة من الأطراف، ويجمعها بخاصية التماثل، ويرسل النتيجة إلى كل طرف لفك التشفير وتحديث النموذج المحلي. بهذه الطريقة، يحصل كل طرف على نموذج يستخرج المعلومات من مجموعة البيانات المجمعة، دون تسريب معلوماته الخاصة.

يربط نظام Paillier للتشفير المتماثل كل طرف بمفتاح عام $(n, g)$ ومفتاح خاص $(\lambda, \mu)$، حيث $n, g, \lambda, \mu$ هي أعداد صحيحة كبيرة، عادةً 1024-بت في FATE. يتم تمثيل الرسائل والنصوص المشفرة أيضاً كأعداد صحيحة طويلة. يمكن تشفير رسالة $m$ إلى نص مشفر $c$ بواسطة $c = g^m r^n \mod n^2$ مع عدد عشوائي $r$، ويتم فك التشفير بواسطة $m = ((c^\lambda \mod n^2) - 1) / n \mod n^2$.

يمكننا أن نرى من الصيغة أن غالبية حساب تشفير/فك تشفير Paillier يتعلق بالأسس المعياري (ModExp)، والذي يمكن تحليله بشكل أكبر إلى سلسلة من عمليات الضرب المعياري (ModMult). وبالتالي، فإن تنفيذ الضرب المعياري له تأثير حاسم على الأداء العام. نختار خوارزمية Montgomery للضرب المعياري [Montgomery, 1985] لتنفيذ هذه العملية لأنها ملائمة لـ FPGA، حيث تتخلص من القسمة الصحيحة المكلفة. خوارزمية Montgomery، الموضحة في الخوارزمية 1، تحسب $XY2^{-l} \mod M$ للأعداد الصحيحة $X, Y$ و$M$ بطول $l$-بت. تقسم الأعداد الصحيحة إلى كلمات بطول $k$-بت. جسم الخوارزمية عبارة عن حلقة من مستويين، حيث يهدف كل تكرار خارجي (السطر 2-8) إلى حساب نتيجة وسيطة $S_i = XY_i2^{-k} \mod M$ للكلمة $i$-ال من $Y$، وتحلل الحساب بشكل أكبر بواسطة كل كلمة من $X$ وتشكل الحلقة الداخلية (السطر 4-6).

**الخوارزمية 1:** خوارزمية Montgomery للضرب المعياري مع الأساس $2^k$

**المدخل:** $X = \sum_{j=0}^{l/k-1} X_j 2^{jk}$، $Y = \sum_{j=0}^{l/k-1} Y_j 2^{jk}$، $M = \sum_{j=0}^{l/k-1} M_j 2^{jk}$، $r = 2^k$

**المخرج:** $S = XY/2^l \mod M$

1. $S_0 \leftarrow 0$;
2. **لـ** $i = 0 \ldots l/k-1$ **نفذ**
3. &nbsp;&nbsp;&nbsp;&nbsp;$q \leftarrow ((S_i + XY_i)(-M^{-1})) \mod r$;
4. &nbsp;&nbsp;&nbsp;&nbsp;**لـ** $j = 0 \ldots l/k$ **نفذ**
5. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$S_{i+1}^j \leftarrow S_i^j + X_j Y_i + q M_j$;
6. &nbsp;&nbsp;&nbsp;&nbsp;**نهاية**
7. &nbsp;&nbsp;&nbsp;&nbsp;$S_{i+1} \leftarrow S_{i+1}/2^k$
8. **نهاية**
9. **إذا** $S_{l/k} > M$ **إذن**
10. &nbsp;&nbsp;&nbsp;&nbsp;$S_{l/k} \leftarrow S_{l/k} - M$;
11. **نهاية**
12. **أرجع** $S_{l/k}$

---

### Translation Notes

- **Figures referenced:** Figure 1 (Paillier HE workflow in federated learning)
- **Key terms introduced:** modular exponentiation (أسس معياري), Montgomery algorithm (خوارزمية Montgomery), two-level loop (حلقة من مستويين), word (كلمة)
- **Algorithms:** Algorithm 1 (Montgomery Algorithm)
- **Equations:**
  - Paillier encryption: $c = g^m r^n \mod n^2$
  - Paillier decryption: $m = ((c^\lambda \mod n^2) - 1) / n \mod n^2$
  - Montgomery ModMult output: $XY2^{-l} \mod M$
- **Citations:** 13 references cited
- **Special handling:**
  - Algorithm 1 pseudocode translated with mathematical notation preserved
  - System names preserved: SecureML, Sage, FATE
  - Technical terms like "non-colluding party" carefully translated

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.87
