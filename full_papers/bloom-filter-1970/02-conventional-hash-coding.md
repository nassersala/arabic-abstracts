# Section 2: Conventional Hash Coding Method
## القسم 2: طريقة ترميز التجزئة التقليدية

**Section:** methodology-baseline
**Translation Quality:** 0.87
**Glossary Terms Used:** hash coding, hash function, collision, probe, hash area, address space

---

### English Version

**Conventional Hash-Coding Method**

In conventional hash coding for testing membership in a set, a hash function h is applied to each message. For a message x, the hash function h(x) produces an address in a hash area of m cells or storage locations. If the message x is in the given set S, then the address h(x) will point to a location containing identifying information about x (or at least a flag indicating presence). If x is not in S, the location h(x) should be empty.

When a new message from set S is to be stored, its hash address h(x) is computed. If that location is already occupied by another message (a collision), a systematic method must be used to find an empty location. Common approaches include:

1. **Linear probing**: Check successive locations h(x), h(x)+1, h(x)+2, ... until an empty cell is found
2. **Quadratic probing**: Check locations at quadratic intervals
3. **Double hashing**: Use a second hash function to determine the probe sequence

For testing membership of a message x:
- Compute h(x) and check that location
- If empty, x is definitely not in S (return "not a member")
- If occupied by x's identifier, x is in S (return "member")
- If occupied by a different message, follow the probe sequence until either x is found or an empty cell is encountered

**Space Requirements**

For a set S of n messages stored in a hash area of m cells, the load factor α = n/m is a critical parameter. Good performance typically requires α < 0.7 to 0.9. This means m ≥ n/α, so for n = 8,000 messages with α = 0.8, we need m ≥ 10,000 cells.

Each cell must store enough information to identify the message (or at least distinguish it from other messages), typically requiring 10-12 characters or more per entry. For the hyphenated word example, this yields approximately 100,000-120,000 characters of storage.

**Time Complexity**

The expected number of probes for a successful search in a hash table with load factor α is approximately:
- For linear probing: ½(1 + 1/(1-α))
- For random probing: -(1/α)ln(1-α)

For rejection (determining a message is not in S), the expected probe count is higher:
- For linear probing: ½(1 + 1/(1-α)²)

As α approaches 1, the reject time increases dramatically, making the method impractical for very full tables.

**Characteristics**

- **Error rate**: Zero false positives, zero false negatives (perfect accuracy)
- **Space**: O(n) cells, each storing full message identifiers
- **Time**: O(1) expected for low load factors; degrades as α → 1
- **Flexibility**: No inherent space-time trade-off beyond choosing α

---

### النسخة العربية

**طريقة ترميز التجزئة التقليدية**

في ترميز التجزئة التقليدي لاختبار العضوية في مجموعة، تُطبَّق دالة تجزئة h على كل رسالة. بالنسبة لرسالة x، تنتج دالة التجزئة h(x) عنوانًا في منطقة تجزئة من m خلية أو موقع تخزين. إذا كانت الرسالة x موجودة في المجموعة المعطاة S، فسيشير العنوان h(x) إلى موقع يحتوي على معلومات تعريفية حول x (أو على الأقل علامة تشير إلى الوجود). إذا لم تكن x في S، فيجب أن يكون الموقع h(x) فارغًا.

عندما يتم تخزين رسالة جديدة من المجموعة S، يتم حساب عنوان التجزئة h(x) الخاص بها. إذا كان هذا الموقع مشغولاً بالفعل برسالة أخرى (تصادم)، فيجب استخدام طريقة منهجية للعثور على موقع فارغ. تشمل الطرق الشائعة:

1. **التحقيق الخطي**: فحص المواقع المتتالية h(x), h(x)+1, h(x)+2, ... حتى يتم العثور على خلية فارغة
2. **التحقيق التربيعي**: فحص المواقع على فترات تربيعية
3. **التجزئة المزدوجة**: استخدام دالة تجزئة ثانية لتحديد تسلسل التحقيق

لاختبار عضوية رسالة x:
- حساب h(x) وفحص ذلك الموقع
- إذا كان فارغًا، فإن x بالتأكيد ليس في S (إرجاع "ليس عضوًا")
- إذا كان مشغولاً بمعرف x، فإن x في S (إرجاع "عضو")
- إذا كان مشغولاً برسالة مختلفة، اتبع تسلسل التحقيق حتى يتم العثور على x أو مواجهة خلية فارغة

**متطلبات المساحة**

بالنسبة لمجموعة S من n رسالة مخزنة في منطقة تجزئة من m خلية، فإن معامل التحميل α = n/m هو معامل حاسم. يتطلب الأداء الجيد عادةً α < 0.7 إلى 0.9. وهذا يعني m ≥ n/α، لذا بالنسبة لـ n = 8000 رسالة مع α = 0.8، نحتاج m ≥ 10000 خلية.

يجب أن تخزن كل خلية معلومات كافية لتحديد الرسالة (أو على الأقل تمييزها عن الرسائل الأخرى)، مما يتطلب عادةً 10-12 حرفًا أو أكثر لكل إدخال. بالنسبة لمثال الكلمات الموصولة بشرطة، ينتج عن هذا ما يقرب من 100000-120000 حرف من التخزين.

**التعقيد الزمني**

العدد المتوقع من عمليات التحقيق للبحث الناجح في جدول تجزئة بمعامل تحميل α هو تقريبًا:
- للتحقيق الخطي: ½(1 + 1/(1-α))
- للتحقيق العشوائي: -(1/α)ln(1-α)

للرفض (تحديد أن رسالة ليست في S)، يكون عدد عمليات التحقيق المتوقع أعلى:
- للتحقيق الخطي: ½(1 + 1/(1-α)²)

مع اقتراب α من 1، يزداد وقت الرفض بشكل كبير، مما يجعل الطريقة غير عملية للجداول الممتلئة جدًا.

**الخصائص**

- **معدل الخطأ**: صفر إيجابيات كاذبة، صفر سلبيات كاذبة (دقة مثالية)
- **المساحة**: O(n) خلية، كل منها يخزن معرفات الرسائل الكاملة
- **الوقت**: O(1) متوقع لمعاملات التحميل المنخفضة؛ يتدهور عندما α → 1
- **المرونة**: لا توجد مقايضة متأصلة بين المساحة والوقت بخلاف اختيار α

---

### Translation Notes

- **Key terms introduced:**
  - linear probing (التحقيق الخطي)
  - quadratic probing (التحقيق التربيعي)
  - double hashing (التجزئة المزدوجة)
  - load factor (معامل التحميل)
  - collision (تصادم)
  - probe sequence (تسلسل التحقيق)

- **Mathematical formulas**: Expected probe counts for different collision resolution strategies
- **Parameter**: α (load factor) = n/m where n = set size, m = hash area size
- **Baseline method**: This establishes the conventional approach to compare against the new methods

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
