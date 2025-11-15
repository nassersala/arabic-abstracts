# Section 3: Method 1 - Multiple Hash Functions with Single Hash Area
## القسم 3: الطريقة 1 - دوال تجزئة متعددة مع منطقة تجزئة واحدة

**Section:** methodology-method-1
**Translation Quality:** 0.86
**Glossary Terms Used:** hash function, hash area, false positive, probability, bit vector

---

### English Version

**Method 1: Using d Independent Hash Functions**

The first new method uses d different hash functions h₁, h₂, ..., h_d, all mapping into the same hash area of m bits. Unlike conventional hash coding where each cell stores message identifiers, this method uses a simple bit array where each cell is just one bit.

**Setup Phase:**
1. Initialize all m bits to 0
2. For each message x in the set S:
   - Compute h₁(x), h₂(x), ..., h_d(x)
   - Set all these d bit positions to 1

**Query Phase:**
To test whether a message y is in S:
1. Compute h₁(y), h₂(y), ..., h_d(y)
2. Check if ALL d bit positions are set to 1
3. If all are 1, return "probably in S" (may be false positive)
4. If any is 0, return "definitely not in S" (no false negatives)

**Analysis**

After storing all n messages from S, each using d hash values, approximately nd bits will have been set to 1 (with some overlap). The probability that a random bit is still 0 after all insertions is:

$$P(\text{bit is 0}) = \left(1 - \frac{1}{m}\right)^{nd} \approx e^{-nd/m}$$

For a message y not in S, the probability of a false positive (all d bits happen to be 1) is:

$$P(\text{false positive}) = \left(1 - e^{-nd/m}\right)^d$$

Let k = nd/m (the expected number of bits set per message). Then:

$$P(\text{false positive}) = \left(1 - e^{-k}\right)^d$$

This can be minimized by choosing the optimal number of hash functions. Taking the derivative and setting it to zero shows that the optimal value is:

$$d_{opt} = \frac{m}{n} \ln 2 \approx 0.693 \frac{m}{n}$$

With this optimal choice:

$$P(\text{false positive}) = \left(\frac{1}{2}\right)^d = 2^{-m \ln 2 / n} \approx (0.6185)^{m/n}$$

**Space-Time Trade-off**

This method achieves a significant space advantage:
- **Space**: Only m bits total, regardless of message size. For n = 8,000 messages with m/n = 8 bits per message, only 64,000 bits = 8,000 bytes are needed (vs. 100,000 bytes for conventional method).
- **Time**: Exactly d hash function evaluations and d bit accesses per query - constant time regardless of load
- **Error**: Controllable false positive rate; can be made arbitrarily small by increasing m

**Example:**
- n = 8,000 messages
- m = 64,000 bits (8 bits per message)
- d_opt ≈ 5.5 ≈ 6 hash functions
- False positive rate ≈ 0.02 (2%)

**Advantages over conventional method:**
1. Dramatically smaller space (bits instead of bytes per message)
2. Constant query time independent of load factor
3. No collision resolution needed

**Disadvantages:**
1. False positives possible (though controllable)
2. Cannot retrieve the actual message, only test membership
3. Requires d independent hash functions

---

### النسخة العربية

**الطريقة 1: استخدام d دوال تجزئة مستقلة**

تستخدم الطريقة الجديدة الأولى d دوال تجزئة مختلفة h₁, h₂, ..., h_d، جميعها تُخطِّط إلى نفس منطقة التجزئة من m بت. على عكس ترميز التجزئة التقليدي حيث تخزن كل خلية معرفات الرسائل، تستخدم هذه الطريقة مصفوفة بت بسيطة حيث كل خلية هي مجرد بت واحد.

**مرحلة الإعداد:**
1. تهيئة جميع m بتات إلى 0
2. لكل رسالة x في المجموعة S:
   - حساب h₁(x), h₂(x), ..., h_d(x)
   - تعيين جميع مواقع d البت هذه إلى 1

**مرحلة الاستعلام:**
لاختبار ما إذا كانت رسالة y موجودة في S:
1. حساب h₁(y), h₂(y), ..., h_d(y)
2. التحقق مما إذا كانت جميع مواقع d البت معينة إلى 1
3. إذا كانت جميعها 1، إرجاع "ربما في S" (قد يكون إيجابيًا كاذبًا)
4. إذا كانت أي منها 0، إرجاع "بالتأكيد ليس في S" (لا توجد سلبيات كاذبة)

**التحليل**

بعد تخزين جميع n رسائل من S، كل منها يستخدم d قيم تجزئة، سيتم تعيين ما يقرب من nd بتًا إلى 1 (مع بعض التداخل). احتمال أن تظل بتة عشوائية 0 بعد جميع عمليات الإدراج هو:

$$P(\text{البت هو 0}) = \left(1 - \frac{1}{m}\right)^{nd} \approx e^{-nd/m}$$

بالنسبة لرسالة y ليست في S، احتمال حدوث إيجابي كاذب (جميع d بتات تصادف أن تكون 1) هو:

$$P(\text{إيجابي كاذب}) = \left(1 - e^{-nd/m}\right)^d$$

لنفترض k = nd/m (العدد المتوقع من البتات المعينة لكل رسالة). إذن:

$$P(\text{إيجابي كاذب}) = \left(1 - e^{-k}\right)^d$$

يمكن تقليل هذا إلى الحد الأدنى عن طريق اختيار العدد الأمثل من دوال التجزئة. أخذ المشتقة وتعيينها إلى الصفر يُظهر أن القيمة المثلى هي:

$$d_{opt} = \frac{m}{n} \ln 2 \approx 0.693 \frac{m}{n}$$

مع هذا الاختيار الأمثل:

$$P(\text{إيجابي كاذب}) = \left(\frac{1}{2}\right)^d = 2^{-m \ln 2 / n} \approx (0.6185)^{m/n}$$

**مقايضة المساحة والوقت**

تحقق هذه الطريقة ميزة مساحة كبيرة:
- **المساحة**: فقط m بتًا إجماليًا، بغض النظر عن حجم الرسالة. بالنسبة لـ n = 8000 رسالة مع m/n = 8 بتات لكل رسالة، يلزم فقط 64000 بت = 8000 بايت (مقابل 100000 بايت للطريقة التقليدية).
- **الوقت**: بالضبط d تقييمات لدالة التجزئة و d وصولات بت لكل استعلام - وقت ثابت بغض النظر عن التحميل
- **الخطأ**: معدل إيجابي كاذب قابل للتحكم؛ يمكن جعله صغيرًا تعسفيًا عن طريق زيادة m

**مثال:**
- n = 8000 رسالة
- m = 64000 بت (8 بتات لكل رسالة)
- d_opt ≈ 5.5 ≈ 6 دوال تجزئة
- معدل الإيجابيات الكاذبة ≈ 0.02 (2%)

**المزايا على الطريقة التقليدية:**
1. مساحة أصغر بكثير (بتات بدلاً من بايتات لكل رسالة)
2. وقت استعلام ثابت مستقل عن معامل التحميل
3. لا حاجة لحل التصادمات

**العيوب:**
1. إيجابيات كاذبة ممكنة (وإن كانت قابلة للتحكم)
2. لا يمكن استرجاع الرسالة الفعلية، فقط اختبار العضوية
3. يتطلب d دوال تجزئة مستقلة

---

### Translation Notes

- **Key terms introduced:**
  - bit array (مصفوفة بت)
  - bit vector (متجه البت)
  - independent hash functions (دوال تجزئة مستقلة)
  - optimal number (العدد الأمثل)
  - false positive rate (معدل الإيجابيات الكاذبة)

- **Mathematical analysis:**
  - Probability formulas for bit being 0
  - False positive probability calculation
  - Optimization to find d_opt
  - Space reduction analysis

- **Key insight:** Using multiple hash functions with a bit array instead of storing full messages

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86
