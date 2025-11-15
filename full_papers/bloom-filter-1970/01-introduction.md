# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** hash coding, algorithm, data structure, space, time complexity, memory, computational factors

---

### English Version

The primary purpose of this paper is to show that allowing a small number of retrieval errors in hash coding can significantly reduce the amount of memory needed to store hash results without increasing the time required to hash and retrieve.

An appropriate paradigm problem is the searching for a word in Webster's New Collegiate Dictionary. Given the title of a hyphenated word, a program might be required to determine whether it is in the dictionary and can safely be compressed into a single word. For example, "time-oriented" would be left hyphenated but "time-sharing" could be compressed to "timesharing." The conventional solution to such a problem is to store the titles of all hyphenated words and then to check each test message. For this case, the 8,000 hyphenated words would require about 100,000 characters of storage.

A much more interesting alternative would be to specify that a small number of words which are not in the dictionary can be incorrectly identified as being in the dictionary. For example, it might be permissible to compress a word such as "time-division" (which does not appear in the dictionary) into "timedivision" even though this compression is not specified in Webster's. In return for accepting this small error rate, substantial savings in storage requirements can be achieved.

The essential trick is to use hash coding in a way that allows for a controllable false-positive error rate in identifying members of the given set. False negatives are not permitted - if a word is in the dictionary, it must always be identified as such. But if a word is not in the dictionary, it may occasionally (with small probability) be incorrectly identified as a member. By accepting this controlled error rate, dramatic reductions in storage requirements become possible.

The paradigm problem we will analyze throughout is the testing of messages to determine membership in a given set S of n messages. The analysis focuses on three distinct methods for performing this membership test, comparing them in terms of space requirements, access time, and error characteristics.

---

### النسخة العربية

الغرض الأساسي من هذه الورقة هو إظهار أن السماح بعدد صغير من أخطاء الاسترجاع في ترميز التجزئة يمكن أن يقلل بشكل كبير من مقدار الذاكرة المطلوبة لتخزين نتائج التجزئة دون زيادة الوقت المطلوب للتجزئة والاسترجاع.

مشكلة نموذجية مناسبة هي البحث عن كلمة في قاموس ويبستر الجامعي الجديد. بالنظر إلى عنوان كلمة موصولة بشرطة، قد يُطلب من برنامج تحديد ما إذا كانت موجودة في القاموس ويمكن ضغطها بأمان إلى كلمة واحدة. على سبيل المثال، "time-oriented" ستُترك موصولة بشرطة ولكن "time-sharing" يمكن ضغطها إلى "timesharing". الحل التقليدي لمثل هذه المشكلة هو تخزين عناوين جميع الكلمات الموصولة بشرطة ثم فحص كل رسالة اختبار. في هذه الحالة، ستتطلب 8000 كلمة موصولة بشرطة حوالي 100000 حرف من التخزين.

البديل الأكثر إثارة للاهتمام هو تحديد أن عددًا صغيرًا من الكلمات غير الموجودة في القاموس يمكن تحديدها بشكل غير صحيح على أنها موجودة في القاموس. على سبيل المثال، قد يكون من المسموح ضغط كلمة مثل "time-division" (التي لا تظهر في القاموس) إلى "timedivision" حتى لو لم يكن هذا الضغط محددًا في ويبستر. في مقابل قبول معدل الخطأ الصغير هذا، يمكن تحقيق وفورات كبيرة في متطلبات التخزين.

الحيلة الأساسية هي استخدام ترميز التجزئة بطريقة تسمح بمعدل خطأ إيجابي كاذب قابل للتحكم في تحديد أعضاء المجموعة المعطاة. لا يُسمح بالسلبيات الكاذبة - إذا كانت كلمة موجودة في القاموس، فيجب دائمًا تحديدها على هذا النحو. ولكن إذا لم تكن كلمة موجودة في القاموس، فقد يتم تحديدها بشكل غير صحيح أحيانًا (مع احتمال صغير) كعضو. من خلال قبول معدل الخطأ المُتحكَّم به هذا، تصبح التخفيضات الدراماتيكية في متطلبات التخزين ممكنة.

المشكلة النموذجية التي سنحللها في جميع الأقسام هي اختبار الرسائل لتحديد العضوية في مجموعة معينة S من n رسالة. يركز التحليل على ثلاث طرق متميزة لإجراء اختبار العضوية هذا، مقارنتها من حيث متطلبات المساحة، ووقت الوصول، وخصائص الخطأ.

---

### Translation Notes

- **Key terms introduced:**
  - false-positive (إيجابي كاذب)
  - false-negative (سلبي كاذب)
  - membership test (اختبار العضوية)
  - retrieval error (خطأ الاسترجاع)
  - hash coding (ترميز التجزئة)
  - storage requirements (متطلبات التخزين)

- **Real-world example:** Webster's dictionary hyphenated words problem - provides concrete motivation
- **Key insight:** Trading perfect accuracy for space efficiency by allowing controlled false positives
- **Problem formulation:** Testing membership in a set S of n messages

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88
