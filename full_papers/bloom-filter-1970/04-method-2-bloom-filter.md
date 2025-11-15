# Section 4: Method 2 - The Bloom Filter
## القسم 4: الطريقة 2 - مرشح بلوم

**Section:** methodology-bloom-filter
**Translation Quality:** 0.89
**Glossary Terms Used:** hash function, hash area, bit vector, false positive, probability, data structure

---

### English Version

**Method 2: Separate Hash Areas (The Bloom Filter)**

Method 2, the main contribution of this paper, modifies Method 1 by using d separate hash areas instead of one combined area. This is the data structure now known as the **Bloom filter**.

**Structure:**
- d independent hash functions: h₁, h₂, ..., h_d
- d separate bit arrays: A₁, A₂, ..., A_d
- Each array A_i has m_i bits (typically m_i = m/d for equal-sized arrays)
- Total space: m = m₁ + m₂ + ... + m_d bits

**Setup Phase:**
1. Initialize all d arrays to all 0's
2. For each message x in the set S:
   - Compute h₁(x) and set bit h₁(x) in array A₁ to 1
   - Compute h₂(x) and set bit h₂(x) in array A₂ to 1
   - ...
   - Compute h_d(x) and set bit h_d(x) in array A_d to 1

**Query Phase:**
To test whether a message y is in S:
1. For i = 1 to d:
   - Compute h_i(y)
   - Check if bit h_i(y) in array A_i is 1
2. If ALL d bits are 1, return "probably in S"
3. If ANY bit is 0, return "definitely not in S"

**Key Innovation:**

The crucial difference from Method 1 is that each hash function operates on its own separate bit array. This independence has important implications for the false positive probability.

**Analysis**

For equal-sized arrays with m_i = m/d:

After inserting all n messages, the probability that a specific bit in array A_i is still 0 is:

$$P(\text{bit in } A_i \text{ is 0}) = \left(1 - \frac{d}{m}\right)^n \approx e^{-nd/m}$$

For a message y not in S, since the d hash functions are independent and map to separate arrays, the probability of a false positive is:

$$P(\text{false positive}) = \left(1 - e^{-nd/m}\right)^d$$

This is identical to Method 1! However, Method 2 offers flexibility advantages that will become clear in the comparison.

**Optimal Configuration**

For fixed total space m and set size n, we want to choose d to minimize the false positive probability. As shown for Method 1, the optimal number of hash functions is:

$$d_{opt} = \frac{m}{n} \ln 2$$

And the resulting false positive probability is:

$$P(\text{false positive}) = \left(\frac{1}{2}\right)^{d_{opt}} = 2^{-(m/n) \ln 2} \approx 0.6185^{m/n}$$

**Example Configuration:**
- Set size: n = 8,000 messages
- Total space: m = 64,000 bits (8 bits per message)
- Optimal hash functions: d_opt ≈ 5.5 ≈ 6
- Array sizes: m_i = 64,000/6 ≈ 10,667 bits each
- False positive rate: ≈ 2%

**Comparison with Method 1:**

While Methods 1 and 2 achieve the same false positive rate for equal space, Method 2 has advantages:

1. **Modularity**: Each hash function's results are isolated in separate arrays
2. **Flexibility**: Can use different-sized arrays (m_i ≠ m_j) for asymmetric designs
3. **Incremental construction**: Can add hash functions/arrays gradually
4. **Parallelization**: The d hash lookups can be performed in parallel since they access separate memory regions
5. **Analysis**: Simpler to analyze when hash functions are truly independent

**Space Efficiency:**

Compared to conventional hash coding:
- Conventional: ~12 bytes per message × 8,000 = 96,000 bytes
- Bloom filter: 8 bits per message × 8,000 = 8,000 bytes (64,000 bits)
- **Space reduction: 92%** with only 2% false positive rate

**Time Complexity:**

- **Setup**: O(nd) to insert n messages with d hash functions
- **Query**: O(d) to check membership (constant time)
- **No collision resolution** overhead
- **Predictable**: Performance doesn't degrade with load factor

---

### النسخة العربية

**الطريقة 2: مناطق تجزئة منفصلة (مرشح بلوم)**

تعدل الطريقة 2، المساهمة الرئيسية لهذه الورقة، الطريقة 1 باستخدام d مناطق تجزئة منفصلة بدلاً من منطقة واحدة مجمعة. هذه هي بنية البيانات المعروفة الآن باسم **مرشح بلوم**.

**البنية:**
- d دوال تجزئة مستقلة: h₁, h₂, ..., h_d
- d مصفوفات بت منفصلة: A₁, A₂, ..., A_d
- كل مصفوفة A_i لديها m_i بتًا (عادةً m_i = m/d لمصفوفات ذات أحجام متساوية)
- المساحة الإجمالية: m = m₁ + m₂ + ... + m_d بتًا

**مرحلة الإعداد:**
1. تهيئة جميع d مصفوفات إلى جميع الأصفار
2. لكل رسالة x في المجموعة S:
   - حساب h₁(x) وتعيين البت h₁(x) في المصفوفة A₁ إلى 1
   - حساب h₂(x) وتعيين البت h₂(x) في المصفوفة A₂ إلى 1
   - ...
   - حساب h_d(x) وتعيين البت h_d(x) في المصفوفة A_d إلى 1

**مرحلة الاستعلام:**
لاختبار ما إذا كانت رسالة y موجودة في S:
1. لـ i = 1 إلى d:
   - حساب h_i(y)
   - التحقق مما إذا كانت البت h_i(y) في المصفوفة A_i هو 1
2. إذا كانت جميع d بتات 1، إرجاع "ربما في S"
3. إذا كانت أي بتة 0، إرجاع "بالتأكيد ليس في S"

**الابتكار الأساسي:**

الفرق الحاسم عن الطريقة 1 هو أن كل دالة تجزئة تعمل على مصفوفة بت منفصلة خاصة بها. هذا الاستقلال له آثار مهمة على احتمال الإيجابيات الكاذبة.

**التحليل**

للمصفوفات ذات الأحجام المتساوية مع m_i = m/d:

بعد إدراج جميع n رسائل، فإن احتمال أن تظل بتة معينة في المصفوفة A_i هي 0 هو:

$$P(\text{البت في } A_i \text{ هو 0}) = \left(1 - \frac{d}{m}\right)^n \approx e^{-nd/m}$$

بالنسبة لرسالة y ليست في S، نظرًا لأن d دوال التجزئة مستقلة وتُخطِّط إلى مصفوفات منفصلة، فإن احتمال حدوث إيجابي كاذب هو:

$$P(\text{إيجابي كاذب}) = \left(1 - e^{-nd/m}\right)^d$$

هذا مطابق للطريقة 1! ومع ذلك، تقدم الطريقة 2 مزايا مرونة ستصبح واضحة في المقارنة.

**التكوين الأمثل**

بالنسبة للمساحة الإجمالية الثابتة m وحجم المجموعة n، نريد اختيار d لتقليل احتمال الإيجابيات الكاذبة. كما هو موضح للطريقة 1، فإن العدد الأمثل من دوال التجزئة هو:

$$d_{opt} = \frac{m}{n} \ln 2$$

واحتمال الإيجابيات الكاذبة الناتج هو:

$$P(\text{إيجابي كاذب}) = \left(\frac{1}{2}\right)^{d_{opt}} = 2^{-(m/n) \ln 2} \approx 0.6185^{m/n}$$

**مثال على التكوين:**
- حجم المجموعة: n = 8000 رسالة
- المساحة الإجمالية: m = 64000 بت (8 بتات لكل رسالة)
- دوال التجزئة المثلى: d_opt ≈ 5.5 ≈ 6
- أحجام المصفوفات: m_i = 64000/6 ≈ 10667 بتًا لكل منها
- معدل الإيجابيات الكاذبة: ≈ 2%

**المقارنة مع الطريقة 1:**

بينما تحقق الطريقتان 1 و 2 نفس معدل الإيجابيات الكاذبة للمساحة المتساوية، فإن الطريقة 2 لها مزايا:

1. **النمطية**: نتائج كل دالة تجزئة معزولة في مصفوفات منفصلة
2. **المرونة**: يمكن استخدام مصفوفات ذات أحجام مختلفة (m_i ≠ m_j) للتصميمات غير المتماثلة
3. **البناء التدريجي**: يمكن إضافة دوال تجزئة/مصفوفات تدريجيًا
4. **التوازي**: يمكن إجراء d عمليات بحث تجزئة بالتوازي لأنها تصل إلى مناطق ذاكرة منفصلة
5. **التحليل**: أبسط في التحليل عندما تكون دوال التجزئة مستقلة حقًا

**كفاءة المساحة:**

مقارنة بترميز التجزئة التقليدي:
- التقليدي: ~12 بايت لكل رسالة × 8000 = 96000 بايت
- مرشح بلوم: 8 بتات لكل رسالة × 8000 = 8000 بايت (64000 بت)
- **تخفيض المساحة: 92%** مع معدل إيجابيات كاذبة 2% فقط

**التعقيد الزمني:**

- **الإعداد**: O(nd) لإدراج n رسائل مع d دوال تجزئة
- **الاستعلام**: O(d) للتحقق من العضوية (وقت ثابت)
- **لا يوجد** عبء حل التصادمات
- **متوقع**: الأداء لا يتدهور مع معامل التحميل

---

### Translation Notes

- **Key terms introduced:**
  - Bloom filter (مرشح بلوم)
  - separate arrays (مصفوفات منفصلة)
  - modularity (النمطية)
  - incremental construction (البناء التدريجي)
  - parallelization (التوازي)
  - space reduction (تخفيض المساحة)

- **Main contribution**: This section introduces the Bloom filter data structure
- **Mathematical formulas**: Identical false positive probability to Method 1, but with architectural advantages
- **Key advantages**: Modularity, flexibility, parallelization potential
- **Practical impact**: 92% space reduction vs. conventional hashing with only 2% error rate

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.91
- Readability: 0.88
- Glossary consistency: 0.87
- **Overall section score:** 0.89
