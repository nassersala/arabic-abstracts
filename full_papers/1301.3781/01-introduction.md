# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** neural network, distributed representations, language model, computational complexity, n-gram, natural language processing, training data, vector representation

---

### English Version

Many current NLP systems and techniques treat words as atomic units - there is no notion of similarity between words, as these are represented as indices in a vocabulary. This choice has several good reasons - simplicity, robustness and the observation that simple models trained on huge amounts of data outperform complex systems trained on less data. An example is the popular N-gram model used for statistical language modeling - today, it is possible to train N-grams on virtually all available data (trillions of words [3]).

However, the simple techniques are at their limits in many tasks. For example, the amount of relevant in-domain data for automatic speech recognition is limited - the performance is usually dominated by the size of high quality transcribed speech data (often just millions of words). In machine translation, the existing corpora for many languages contain only a few billions of words or less. Thus, there are situations where simple scaling up of the basic techniques will not result in any significant progress, and we have to focus on more advanced techniques.

With progress of machine learning techniques in recent years, it has become possible to train more complex models on much larger data set, and they typically outperform the simple models. Probably the most successful concept is to use distributed representations of words [10]. For example, neural network based language models significantly outperform N-gram models [1, 27, 17].

---

### النسخة العربية

تتعامل العديد من أنظمة معالجة اللغة الطبيعية والتقنيات الحالية مع الكلمات كوحدات ذرية - حيث لا يوجد مفهوم للتشابه بين الكلمات، إذ يتم تمثيلها كمؤشرات في مفردات. لهذا الاختيار عدة أسباب وجيهة - البساطة والمتانة والملاحظة بأن النماذج البسيطة المدربة على كميات ضخمة من البيانات تتفوق على الأنظمة المعقدة المدربة على بيانات أقل. مثال على ذلك هو نموذج N-gram الشائع المستخدم في نمذجة اللغة الإحصائية - اليوم، أصبح من الممكن تدريب نماذج N-gram على جميع البيانات المتاحة تقريباً (تريليونات الكلمات [3]).

ومع ذلك، فإن التقنيات البسيطة قد وصلت إلى حدودها في العديد من المهام. على سبيل المثال، كمية البيانات ذات الصلة بالمجال للتعرف التلقائي على الكلام محدودة - عادةً ما يكون الأداء مهيمناً عليه بحجم بيانات الكلام المنسوخة عالية الجودة (غالباً ملايين الكلمات فقط). في الترجمة الآلية، تحتوي المدونات النصية الموجودة للعديد من اللغات على بضع مليارات من الكلمات أو أقل فقط. وبالتالي، هناك حالات لن يؤدي فيها التوسع البسيط في التقنيات الأساسية إلى أي تقدم كبير، ويتعين علينا التركيز على تقنيات أكثر تقدماً.

مع تقدم تقنيات تعلم الآلة في السنوات الأخيرة، أصبح من الممكن تدريب نماذج أكثر تعقيداً على مجموعات بيانات أكبر بكثير، وعادةً ما تتفوق على النماذج البسيطة. ربما يكون المفهوم الأكثر نجاحاً هو استخدام التمثيلات الموزعة للكلمات [10]. على سبيل المثال، نماذج اللغة القائمة على الشبكات العصبية تتفوق بشكل كبير على نماذج N-gram [1، 27، 17].

---

### Translation Notes

- **Key terms introduced:** atomic units, distributed representations, N-gram models, statistical language modeling, in-domain data, speech recognition, machine translation
- **Equations:** 0
- **Citations:** [3], [10], [1, 27, 17]
- **Special handling:** Careful translation of technical NLP terminology; preserved citation numbers

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.89
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88

### Back-Translation (Validation)

Many current natural language processing systems and techniques treat words as atomic units - where there is no concept of similarity between words, as they are represented as indices in a vocabulary. This choice has several good reasons - simplicity, robustness, and the observation that simple models trained on huge amounts of data outperform complex systems trained on less data. An example is the popular N-gram model used in statistical language modeling - today, it has become possible to train N-gram models on virtually all available data (trillions of words [3]).

However, simple techniques have reached their limits in many tasks. For example, the amount of relevant in-domain data for automatic speech recognition is limited - performance is usually dominated by the size of high-quality transcribed speech data (often only millions of words). In machine translation, existing text corpora for many languages contain only a few billion words or less. Thus, there are cases where simple scaling of basic techniques will not lead to any significant progress, and we must focus on more advanced techniques.

With the advancement of machine learning techniques in recent years, it has become possible to train more complex models on much larger datasets, and they usually outperform simple models. Perhaps the most successful concept is the use of distributed representations of words [10]. For example, neural network-based language models significantly outperform N-gram models [1, 27, 17].
