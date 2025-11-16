# Section 2: Problem Setup
## القسم 2: إعداد المشكلة

**Section:** problem-setup
**Translation Quality:** 0.87
**Glossary Terms Used:** البرمجة التنافسية, خوارزمية, بنية البيانات, معيار, تقييم, عينات, اختبار, حل مقدم

---

### English Version

## 2.1 Competitive Programming

Programming competitions have existed since the 1970s and now attract hundreds of thousands of participants globally. The International Collegiate Programming Contest enrolls nearly 60,000 students from over 3,000 universities annually, while major technology companies like Google and Facebook host their own competitions. The Codeforces platform, featured prominently in this research, maintains over 500,000 active users and hosts weekly contests with tens of thousands of participants.

Competition format typically involves participants receiving 5-10 problem descriptions with approximately 3 hours to write correct solutions. Submissions undergo automatic evaluation against hidden test cases, with competitors receiving only pass/fail feedback. Solutions may be written in various programming languages, with C++ and Python being most popular. Problems receive difficulty ratings, with harder problems worth more points.

Solving a competitive programming problem requires three distinct steps. First, competitors must comprehend extended natural language descriptions containing narrative background, problem specifications, input/output format details, and example test cases. Second, they must devise efficient algorithms demonstrating understanding of diverse algorithmic approaches and data structures. Finally, they must implement precise solutions—sometimes exceeding 100 lines—that execute within specified time and memory constraints.

## 2.2 Evaluation

Rather than relying exclusively on live competition evaluation, the researchers developed a proxy measurement suitable for research iteration. This metric, denoted "n@k," represents "percentage of problems solved using n submissions from k samples per problem."

The metric permits generating k samples initially, then evaluating at most n of these against hidden tests. A problem counts as solved if any submission passes all tests. Filtering methodology must rely solely on information available to competitors, such as example tests, excluding hidden test data. The researchers employ bootstrapping across large sample sets exceeding k to reduce variance.

Restricting submissions to n emulates competition penalties for incorrect attempts while preventing metric exploitation. Fixing k enables meaningful comparisons across evaluations. The primary metric used is "10@k"—10 submissions from k samples—modeling realistic competition constraints. The "pass@k" metric, used for consistency with prior work, represents solving with unlimited submissions (equivalent to k@k) and serves as an upper bound.

---

### النسخة العربية

## 2.1 البرمجة التنافسية

وُجدت مسابقات البرمجة منذ السبعينيات وتجذب الآن مئات الآلاف من المشاركين على مستوى العالم. تسجل مسابقة البرمجة الجماعية الدولية (International Collegiate Programming Contest) ما يقرب من 60,000 طالب من أكثر من 3,000 جامعة سنوياً، بينما تستضيف شركات التكنولوجيا الكبرى مثل Google و Facebook مسابقاتها الخاصة. تحتفظ منصة Codeforces، المميزة بشكل بارز في هذا البحث، بأكثر من 500,000 مستخدم نشط وتستضيف مسابقات أسبوعية مع عشرات الآلاف من المشاركين.

يتضمن شكل المسابقة عادةً تلقي المشاركين 5-10 أوصاف مشاكل مع حوالي 3 ساعات لكتابة الحلول الصحيحة. تخضع الحلول المقدمة للتقييم التلقائي مقابل حالات اختبار مخفية، حيث يتلقى المتنافسون ملاحظات نجاح/فشل فقط. يمكن كتابة الحلول بلغات برمجة مختلفة، حيث تعد ++C وبايثون الأكثر شيوعاً. تتلقى المشاكل تقييمات صعوبة، مع منح المشاكل الأصعب نقاطاً أكثر.

يتطلب حل مشكلة برمجة تنافسية ثلاث خطوات متميزة. أولاً، يجب على المتنافسين فهم أوصاف اللغة الطبيعية الممتدة التي تحتوي على خلفية سردية، ومواصفات المشكلة، وتفاصيل تنسيق الإدخال/الإخراج، وحالات اختبار الأمثلة. ثانياً، يجب عليهم ابتكار خوارزميات فعالة تُظهر فهماً لأساليب خوارزمية متنوعة وبنى بيانات. أخيراً، يجب عليهم تنفيذ حلول دقيقة - تتجاوز أحياناً 100 سطر - تُنفذ ضمن قيود الوقت والذاكرة المحددة.

## 2.2 التقييم

بدلاً من الاعتماد حصرياً على تقييم المسابقة المباشرة، طور الباحثون قياساً بديلاً مناسباً لتكرار البحث. يمثل هذا المقياس، المشار إليه بـ "n@k"، "نسبة المشاكل المحلولة باستخدام n حلول مقدمة من k عينات لكل مشكلة".

يسمح المقياس بتوليد k عينات في البداية، ثم تقييم n على الأكثر من هذه العينات مقابل الاختبارات المخفية. تُحسب المشكلة على أنها محلولة إذا نجح أي حل مقدم في اجتياز جميع الاختبارات. يجب أن تعتمد منهجية التصفية فقط على المعلومات المتاحة للمتنافسين، مثل اختبارات الأمثلة، باستثناء بيانات الاختبار المخفية. يستخدم الباحثون التمهيد الذاتي عبر مجموعات عينات كبيرة تتجاوز k لتقليل التباين.

يحاكي تقييد الحلول المقدمة إلى n عقوبات المسابقة على المحاولات غير الصحيحة بينما يمنع استغلال المقياس. يمكّن تثبيت k من إجراء مقارنات ذات معنى عبر التقييمات. المقياس الأساسي المستخدم هو "10@k" - 10 حلول مقدمة من k عينات - الذي ينمذج قيود المسابقة الواقعية. يمثل مقياس "pass@k"، المستخدم للاتساق مع العمل السابق، الحل مع حلول مقدمة غير محدودة (يعادل k@k) ويعمل كحد أعلى.

---

### Translation Notes

- **Subsections:** 2.1 Competitive programming, 2.2 Evaluation
- **Key terms introduced:**
  - competitive programming (البرمجة التنافسية)
  - International Collegiate Programming Contest (مسابقة البرمجة الجماعية الدولية)
  - Codeforces platform (منصة Codeforces)
  - hidden test cases (حالات اختبار مخفية)
  - pass/fail feedback (ملاحظات نجاح/فشل)
  - difficulty ratings (تقييمات صعوبة)
  - time and memory constraints (قيود الوقت والذاكرة)
  - n@k metric (مقياس n@k)
  - filtering methodology (منهجية التصفية)
  - bootstrapping (التمهيد الذاتي)
  - pass@k metric (مقياس pass@k)

- **Numbers and statistics:**
  - 1970s preserved
  - 60,000 students from 3,000 universities preserved
  - 500,000 active users on Codeforces preserved
  - 5-10 problem descriptions preserved
  - 3 hours time limit preserved
  - 100 lines of code preserved
  - 10@k and k@k notation preserved

- **Company/Platform names:** Google, Facebook, Codeforces, International Collegiate Programming Contest (ICPC) - kept in English with Arabic translations where appropriate

- **Programming languages:** C++, Python - kept in English as standard practice

- **Special notation:**
  - "n@k" metric notation preserved in both versions
  - "10@k" preserved
  - "pass@k" preserved
  - "k@k" preserved

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.87

### Back-Translation Validation

The Arabic translation accurately conveys: the history and scale of competitive programming competitions (since 1970s, hundreds of thousands of participants, ICPC with 60,000 students from 3,000 universities, major tech companies hosting competitions, Codeforces with 500,000+ users), the competition format (5-10 problems, 3 hours, hidden test cases, pass/fail feedback, C++ and Python popularity, difficulty ratings), the three steps required to solve problems (comprehension of natural language descriptions, devising efficient algorithms, implementing precise solutions within constraints), and the evaluation methodology (n@k metric, filtering based on available information, bootstrapping to reduce variance, 10@k as primary metric, pass@k as upper bound).
