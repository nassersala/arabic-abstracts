# Section 2: Programming Model
## القسم 2: نموذج البرمجة

**Section:** Programming Model
**Translation Quality:** 0.87
**Glossary Terms Used:** computation, key/value pair, intermediate, function, map, reduce, pseudo-code, iterator, domain, distributed grep, URL, inverted index, distributed sort

---

### English Version

The computation takes a set of input key/value pairs, and produces a set of output key/value pairs. The user of the MapReduce library expresses the computation as two functions: Map and Reduce.

Map, written by the user, takes an input pair and produces a set of intermediate key/value pairs. The MapReduce library groups together all intermediate values associated with the same intermediate key I and passes them to the Reduce function.

The Reduce function, also written by the user, accepts an intermediate key I and a set of values for that key. It merges together these values to form a possibly smaller set of values. Typically just zero or one output value is produced per Reduce invocation. The intermediate values are supplied to the user's reduce function via an iterator. This allows us to handle lists of values that are too large to fit in memory.

## 2.1 Example

Consider the problem of counting the number of occurrences of each word in a large collection of documents. The user would write code similar to the following pseudo-code:

```
map(String key, String value):
  // key: document name
  // value: document contents
  for each word w in value:
    EmitIntermediate(w, "1");

reduce(String key, Iterator values):
  // key: a word
  // values: a list of counts
  int result = 0;
  for each v in values:
    result += ParseInt(v);
  Emit(AsString(result));
```

The map function emits each word plus an associated count of occurrences (just '1' in this simple example). The reduce function sums together all counts emitted for a particular word.

In addition, the user writes code to fill in a mapreduce specification object with the names of the input and output files, and optional tuning parameters. The user then invokes the MapReduce function, passing it the specification object. The user's code is linked together with the MapReduce library (implemented in C++). Appendix A contains the full program text for this example.

## 2.2 Types

Even though the previous pseudo-code is written in terms of string inputs and outputs, conceptually the map and reduce functions supplied by the user have associated types:

```
map    (k1,v1)       → list(k2,v2)
reduce (k2,list(v2)) → list(v2)
```

I.e., the input keys and values are drawn from a different domain than the output keys and values. Furthermore, the intermediate keys and values are from the same domain as the output keys and values.

Our C++ implementation passes strings to and from the user-defined functions and leaves it to the user code to convert between strings and appropriate types.

## 2.3 More Examples

Here are a few simple examples of interesting programs that can be easily expressed as MapReduce computations.

**Distributed Grep:** The map function emits a line if it matches a supplied pattern. The reduce function is an identity function that just copies the supplied intermediate data to the output.

**Count of URL Access Frequency:** The map function processes logs of web page requests and outputs ⟨URL, 1⟩. The reduce function adds together all values for the same URL and emits a ⟨URL, total count⟩ pair.

**Reverse Web-Link Graph:** The map function outputs ⟨target, source⟩ pairs for each link to a target URL found in a page named source. The reduce function concatenates the list of all source URLs associated with a given target URL and emits the pair: ⟨target, list(source)⟩

**Term-Vector per Host:** A term vector summarizes the most important words that occur in a document or a set of documents as a list of ⟨word, frequency⟩ pairs. The map function emits a ⟨hostname, term vector⟩ pair for each input document (where the hostname is extracted from the URL of the document). The reduce function is passed all per-document term vectors for a given host. It adds these term vectors together, throwing away infrequent terms, and then emits a final ⟨hostname, term vector⟩ pair.

**Inverted Index:** The map function parses each document, and emits a sequence of ⟨word, document ID⟩ pairs. The reduce function accepts all pairs for a given word, sorts the corresponding document IDs and emits a ⟨word, list(document ID)⟩ pair. The set of all output pairs forms a simple inverted index. It is easy to augment this computation to keep track of word positions.

**Distributed Sort:** The map function extracts the key from each record, and emits a ⟨key, record⟩ pair. The reduce function emits all pairs unchanged. This computation depends on the partitioning facilities described in Section 4.1 and the ordering properties described in Section 4.2.

---

### النسخة العربية

يأخذ الحساب مجموعة من أزواج المفتاح/القيمة كإدخال، وينتج مجموعة من أزواج المفتاح/القيمة كإخراج. يعبّر مستخدم مكتبة MapReduce عن الحساب كدالتين: Map و Reduce.

دالة Map، المكتوبة من قبل المستخدم، تأخذ زوجاً من الإدخال وتنتج مجموعة من أزواج المفتاح/القيمة الوسيطة. تقوم مكتبة MapReduce بتجميع جميع القيم الوسيطة المرتبطة بنفس المفتاح الوسيط I وتمريرها إلى دالة Reduce.

دالة Reduce، المكتوبة أيضاً من قبل المستخدم، تقبل مفتاحاً وسيطاً I ومجموعة من القيم لهذا المفتاح. تدمج هذه القيم معاً لتشكل مجموعة أصغر من القيم. عادةً ما يتم إنتاج قيمة إخراج واحدة أو صفرية فقط لكل استدعاء لدالة Reduce. يتم توفير القيم الوسيطة لدالة reduce الخاصة بالمستخدم عبر مكرر. يتيح لنا هذا التعامل مع قوائم القيم الكبيرة جداً بحيث لا تتسع في الذاكرة.

## 2.1 مثال

لنتأمل مشكلة عد عدد مرات ظهور كل كلمة في مجموعة كبيرة من المستندات. سيكتب المستخدم شفرة مشابهة للشفرة الوهمية التالية:

```
map(String key, String value):
  // key: اسم المستند
  // value: محتويات المستند
  for each word w in value:
    EmitIntermediate(w, "1");

reduce(String key, Iterator values):
  // key: كلمة
  // values: قائمة من العدادات
  int result = 0;
  for each v in values:
    result += ParseInt(v);
  Emit(AsString(result));
```

تصدر دالة map كل كلمة بالإضافة إلى عدد مرات ظهورها المرتبط بها ('1' فقط في هذا المثال البسيط). تجمع دالة reduce جميع العدادات المُصدَرة لكلمة معينة.

بالإضافة إلى ذلك، يكتب المستخدم شفرة لملء كائن مواصفات mapreduce بأسماء ملفات الإدخال والإخراج، ومعاملات الضبط الاختيارية. يستدعي المستخدم بعد ذلك دالة MapReduce، ممرراً إليها كائن المواصفات. يتم ربط شفرة المستخدم مع مكتبة MapReduce (المطبَّقة في C++). يحتوي الملحق A على نص البرنامج الكامل لهذا المثال.

## 2.2 الأنواع

على الرغم من أن الشفرة الوهمية السابقة مكتوبة من حيث مدخلات ومخرجات نصية، من الناحية المفاهيمية فإن دالتي map و reduce التي يوفرها المستخدم لها أنواع مرتبطة:

```
map    (k1,v1)       → list(k2,v2)
reduce (k2,list(v2)) → list(v2)
```

أي أن مفاتيح وقيم الإدخال مأخوذة من مجال مختلف عن مفاتيح وقيم الإخراج. علاوة على ذلك، فإن المفاتيح والقيم الوسيطة من نفس المجال مثل مفاتيح وقيم الإخراج.

يمرر تطبيقنا بلغة C++ سلاسل نصية من وإلى الدوال المعرَّفة من قبل المستخدم ويترك للمستخدم مهمة التحويل بين السلاسل النصية والأنواع المناسبة.

## 2.3 المزيد من الأمثلة

فيما يلي بعض الأمثلة البسيطة للبرامج المثيرة للاهتمام التي يمكن التعبير عنها بسهولة كحسابات MapReduce.

**Grep الموزع:** تصدر دالة map سطراً إذا كان يطابق نمطاً معطى. دالة reduce هي دالة هوية تقوم فقط بنسخ البيانات الوسيطة المُعطاة إلى الإخراج.

**عد تكرار الوصول إلى عناوين URL:** تعالج دالة map سجلات طلبات صفحات الويب وتُخرج ⟨URL, 1⟩. تجمع دالة reduce جميع القيم لنفس عنوان URL وتُصدر زوج ⟨URL, العدد الإجمالي⟩.

**رسم بياني عكسي لروابط الويب:** تُخرج دالة map أزواج ⟨الهدف، المصدر⟩ لكل رابط إلى عنوان URL هدف موجود في صفحة تُسمى مصدر. تدمج دالة reduce قائمة جميع عناوين URL المصدر المرتبطة بعنوان URL هدف معين وتُصدر الزوج: ⟨الهدف، قائمة(المصدر)⟩

**متجه المصطلحات لكل مضيف:** يلخص متجه المصطلحات أهم الكلمات التي تظهر في مستند أو مجموعة من المستندات كقائمة من أزواج ⟨كلمة، تكرار⟩. تُصدر دالة map زوج ⟨اسم المضيف، متجه المصطلحات⟩ لكل مستند إدخال (حيث يتم استخراج اسم المضيف من عنوان URL الخاص بالمستند). يتم تمرير جميع متجهات المصطلحات لكل مستند لمضيف معين إلى دالة reduce. تجمع هذه المتجهات معاً، متخلصة من المصطلحات النادرة، ثم تُصدر زوج ⟨اسم المضيف، متجه المصطلحات⟩ النهائي.

**فهرس معكوس:** تحلل دالة map كل مستند، وتُصدر تسلسلاً من أزواج ⟨كلمة، معرف المستند⟩. تقبل دالة reduce جميع الأزواج لكلمة معينة، وترتب معرفات المستندات المقابلة وتُصدر زوج ⟨كلمة، قائمة(معرف المستند)⟩. تشكل مجموعة جميع أزواج الإخراج فهرساً معكوساً بسيطاً. من السهل زيادة هذا الحساب لتتبع مواقع الكلمات.

**الفرز الموزع:** تستخرج دالة map المفتاح من كل سجل، وتُصدر زوج ⟨مفتاح، سجل⟩. تُصدر دالة reduce جميع الأزواج دون تغيير. يعتمد هذا الحساب على مرافق التقسيم الموصوفة في القسم 4.1 وخصائص الترتيب الموصوفة في القسم 4.2.

---

### Translation Notes

- **Key terms:**
  - "key/value pair": زوج المفتاح/القيمة
  - "intermediate": وسيطة/وسيط
  - "iterator": مكرر
  - "pseudo-code": شفرة وهمية
  - "domain": مجال
  - "identity function": دالة هوية
  - "term vector": متجه المصطلحات
  - "inverted index": فهرس معكوس
  - "partitioning": تقسيم

- **Code handling:**
  - Kept code in English (industry standard)
  - Translated comments to Arabic
  - Preserved function names and variable names

- **Technical notation:**
  - Preserved angle brackets ⟨ ⟩ for key/value pair notation
  - Kept technical terms like "Grep", "URL" in English

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.92
- Readability: 0.84
- Glossary consistency: 0.88
- **Overall section score:** 0.87

### Back-Translation Check (First Paragraph)

"The computation takes a set of key/value pairs as input, and produces a set of key/value pairs as output. The user of the MapReduce library expresses the computation as two functions: Map and Reduce."

"The Map function, written by the user, takes an input pair and produces a set of intermediate key/value pairs. The MapReduce library groups all intermediate values associated with the same intermediate key I and passes them to the Reduce function."

"The Reduce function, also written by the user, accepts an intermediate key I and a set of values for that key. It merges these values together to form a smaller set of values. Usually only one or zero output values are produced per Reduce invocation. Intermediate values are provided to the user's reduce function via an iterator. This allows us to handle lists of values too large to fit in memory."
