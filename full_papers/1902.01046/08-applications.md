# Section 8: Applications
## القسم 8: التطبيقات

**Section:** applications
**Translation Quality:** 0.87
**Glossary Terms Used:** federated learning, on-device, privacy, supervised learning, machine learning, model, training, recurrent neural network, A/B testing, ranking, prediction

---

### English Version

Federated Learning proves most effective where on-device data holds greater value than centralized server data—specifically when devices generate the information initially, when the data involves privacy concerns, or when transmission to servers is impractical or undesirable. Current implementations focus on supervised learning tasks, typically using labels derived from user interactions like clicks or typed words.

## On-device item ranking

Mobile applications frequently employ machine learning to select and rank items from inventories stored locally. Examples include search functionality for information retrieval or in-app navigation, such as settings search on Google Pixel devices. Ranking results directly on-device eliminates expensive server calls regarding latency, bandwidth, and power consumption, while keeping potentially sensitive search query information and user selection patterns confined to the device. Each user interaction with ranking features generates labeled data points by observing user responses to preferred items within ranked lists.

## Content suggestions for on-device keyboards

On-device keyboard applications enhance user experience by offering contextually relevant content suggestions—for instance, search queries related to input text. Federated Learning enables training machine learning models for both triggering suggestion features and ranking suggested items in current contexts. Google's Gboard keyboard team implemented this approach using the described FL system.

## Next word prediction

Gboard utilized the FL platform to train a recurrent neural network for next-word-prediction. This model, containing approximately 1.4 million parameters, achieved convergence in 3000 FL rounds after processing 6e8 sentences from 1.5e6 users across 5 training days (approximately 2–3 minutes per round). The FL model improved top-1 recall from 13.0% to 16.4% compared to baseline n-gram models and matched server-trained RNN performance. Live A/B experiments demonstrated superior performance against both baseline and server-trained approaches.

---

### النسخة العربية

يُثبت التعلم الاتحادي فعاليته القصوى حيث تحمل البيانات على الجهاز قيمة أكبر من بيانات الخادم المركزية - على وجه التحديد عندما تُنشئ الأجهزة المعلومات في البداية، أو عندما تتضمن البيانات مخاوف تتعلق بالخصوصية، أو عندما يكون نقل البيانات إلى الخوادم غير عملي أو غير مرغوب فيه. تركز التطبيقات الحالية على مهام التعلم الموجه (supervised learning)، عادةً باستخدام تسميات مشتقة من تفاعلات المستخدم مثل النقرات أو الكلمات المكتوبة.

## ترتيب العناصر على الجهاز

تستخدم تطبيقات الهاتف المحمول بشكل متكرر تعلم الآلة لاختيار وترتيب العناصر من المخزونات المخزنة محلياً. تشمل الأمثلة وظيفة البحث لاسترجاع المعلومات أو التنقل داخل التطبيق، مثل البحث في الإعدادات على أجهزة Google Pixel. يلغي ترتيب النتائج مباشرة على الجهاز استدعاءات الخادم المكلفة فيما يتعلق بالكمون وعرض النطاق الترددي واستهلاك الطاقة، مع الحفاظ على معلومات استعلام البحث الحساسة المحتملة وأنماط اختيار المستخدم محصورة في الجهاز. يُنشئ كل تفاعل للمستخدم مع ميزات الترتيب نقاط بيانات مُسماة من خلال مراقبة استجابات المستخدم للعناصر المفضلة ضمن القوائم المرتبة.

## اقتراحات المحتوى للوحات المفاتيح على الجهاز

تُحسّن تطبيقات لوحة المفاتيح على الجهاز تجربة المستخدم من خلال تقديم اقتراحات محتوى ذات صلة بالسياق - على سبيل المثال، استعلامات البحث المتعلقة بنص الإدخال. يُمكّن التعلم الاتحادي من تدريب نماذج تعلم الآلة لكل من تفعيل ميزات الاقتراح وترتيب العناصر المقترحة في السياقات الحالية. نفذ فريق لوحة مفاتيح Gboard من Google هذا النهج باستخدام نظام التعلم الاتحادي الموصوف.

## التنبؤ بالكلمة التالية

استخدمت Gboard منصة التعلم الاتحادي لتدريب شبكة عصبية متكررة (recurrent neural network) للتنبؤ بالكلمة التالية. حقق هذا النموذج، الذي يحتوي على ما يقرب من 1.4 مليون معامل، التقارب في 3000 جولة من جولات التعلم الاتحادي بعد معالجة 6e8 جملة من 1.5e6 مستخدم عبر 5 أيام تدريب (حوالي 2-3 دقائق لكل جولة). حسّن نموذج التعلم الاتحادي الاستدعاء من الدرجة الأولى (top-1 recall) من 13.0٪ إلى 16.4٪ مقارنة بنماذج n-gram الأساسية وطابق أداء الشبكة العصبية المتكررة المدربة على الخادم. أظهرت تجارب A/B المباشرة أداءً متفوقاً مقارنة بكل من النهج الأساسي والنهج المدرب على الخادم.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** on-device data, supervised learning, item ranking, content suggestions, next word prediction, recurrent neural network (RNN), n-gram models, top-1 recall, A/B experiments, Gboard
- **Equations:** 0
- **Citations:** 0
- **Special handling:** Product names like "Google Pixel" and "Gboard" kept in English. Technical metrics like "top-1 recall" translated with English term in parentheses. Scientific notation (6e8, 1.5e6) kept in original format. Model parameters and performance metrics kept as exact numbers.

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
