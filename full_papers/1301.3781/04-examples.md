# Section 4: Examples of Learned Relationships
## القسم 4: أمثلة على العلاقات المتعلمة

**Section:** examples
**Translation Quality:** 0.89
**Glossary Terms Used:** vector, semantic, syntactic, word representation, linear relationships, vector arithmetic

---

### English Version

Table 3 shows words and their most similar words, computed using the Skip-gram model trained on 783 billion words from the Google News dataset. The similarity is measured by cosine distance between the word vectors.

As we can see from Table 3, the learned word representations capture a large number of precise syntactic and semantic word relationships. It is quite remarkable that the word vector for "France" has the similar relationship to "Paris" as "Italy" has to "Rome". Similarly, "big" has the similar relationship to "bigger" as "small" has to "smaller". These results demonstrate that the Skip-gram model learns more than just word similarity - it learns relationships between words that can be expressed through simple vector arithmetic.

To evaluate the learned word relationships more systematically, we present results for a few selected word pairs from the comprehensive test set. Table 4 shows examples of the relationship categories that are captured well by the Skip-gram vectors, with examples of correct answers found by the model.

It is interesting to note that the Skip-gram vectors can even capture relationships that are not strictly semantic or syntactic. For example, the model successfully learned the relationship between currencies and countries (Angola:kwanza :: Argentina:peso), and between cities and states (Chicago:Illinois :: Houston:Texas).

The vector representation also seems to encode some degree of temporal and spatial information. When given the analogy "Athens:Greece :: Baghdad:?", the model correctly produces "Iraq" as the most similar answer, showing that it has learned geographical relationships between capitals and their countries.

Perhaps the most famous example that emerged from this work is the vector arithmetic:

$$\text{vector("King")} - \text{vector("Man")} + \text{vector("Woman")} \approx \text{vector("Queen")}$$

This demonstrates that the learned word vectors capture not just semantic similarity, but also the underlying relationships and patterns in the data. Similar relationships hold for other pairs such as:

- vector("Paris") - vector("France") + vector("Italy") ≈ vector("Rome")
- vector("walking") - vector("walked") + vector("swam") ≈ vector("swimming")
- vector("bigger") - vector("big") + vector("small") ≈ vector("smaller")

These examples illustrate that the word vectors have learned to represent not just individual words, but the relationships and transformations between words in a consistent and predictable manner.

---

### النسخة العربية

يوضح الجدول 3 الكلمات والكلمات الأكثر تشابهاً معها، محسوبة باستخدام نموذج Skip-gram المدرب على 783 مليار كلمة من مجموعة بيانات أخبار جوجل. يتم قياس التشابه بمسافة جيب التمام بين متجهات الكلمات.

كما يمكننا أن نرى من الجدول 3، تلتقط تمثيلات الكلمات المتعلمة عدداً كبيراً من العلاقات الدقيقة النحوية والدلالية للكلمات. من الملحوظ جداً أن متجه الكلمة "فرنسا" له علاقة مماثلة بـ "باريس" كما أن "إيطاليا" لها علاقة بـ "روما". بالمثل، "كبير" له علاقة مماثلة بـ "أكبر" كما أن "صغير" له علاقة بـ "أصغر". توضح هذه النتائج أن نموذج Skip-gram يتعلم أكثر من مجرد تشابه الكلمات - فهو يتعلم العلاقات بين الكلمات التي يمكن التعبير عنها من خلال عمليات حسابية متجهية بسيطة.

لتقييم العلاقات المتعلمة للكلمات بشكل أكثر منهجية، نقدم نتائج لعدد قليل من أزواج الكلمات المختارة من مجموعة الاختبار الشاملة. يوضح الجدول 4 أمثلة على فئات العلاقات التي يتم التقاطها بشكل جيد بواسطة متجهات Skip-gram، مع أمثلة على الإجابات الصحيحة التي وجدها النموذج.

من المثير للاهتمام ملاحظة أن متجهات Skip-gram يمكنها حتى التقاط العلاقات التي ليست دلالية أو نحوية بشكل صارم. على سبيل المثال، تعلم النموذج بنجاح العلاقة بين العملات والدول (أنغولا:كوانزا :: الأرجنتين:بيزو)، وبين المدن والولايات (شيكاغو:إلينوي :: هيوستن:تكساس).

يبدو أن التمثيل المتجه يشفر أيضاً درجة معينة من المعلومات الزمنية والمكانية. عندما يُعطى التشبيه "أثينا:اليونان :: بغداد:؟"، ينتج النموذج بشكل صحيح "العراق" كإجابة أكثر تشابهاً، مما يدل على أنه تعلم العلاقات الجغرافية بين العواصم ودولها.

ربما المثال الأكثر شهرة الذي ظهر من هذا العمل هو الحساب المتجه:

$$\text{متجه("ملك")} - \text{متجه("رجل")} + \text{متجه("امرأة")} \approx \text{متجه("ملكة")}$$

يوضح هذا أن متجهات الكلمات المتعلمة لا تلتقط فقط التشابه الدلالي، ولكن أيضاً العلاقات والأنماط الأساسية في البيانات. تحمل علاقات مماثلة لأزواج أخرى مثل:

- متجه("باريس") - متجه("فرنسا") + متجه("إيطاليا") ≈ متجه("روما")
- متجه("يمشي") - متجه("مشى") + متجه("سبح") ≈ متجه("السباحة")
- متجه("أكبر") - متجه("كبير") + متجه("صغير") ≈ متجه("أصغر")

توضح هذه الأمثلة أن متجهات الكلمات تعلمت تمثيل ليس فقط الكلمات الفردية، ولكن أيضاً العلاقات والتحويلات بين الكلمات بطريقة متسقة ويمكن التنبؤ بها.

---

### Translation Notes

- **Tables referenced:** Table 3, Table 4
- **Key terms introduced:** vector arithmetic, word analogy, linear relationships, cosine similarity, geographical relationships
- **Equations:** 1 (the famous King - Man + Woman ≈ Queen equation)
- **Citations:** None
- **Special handling:** The famous word vector arithmetic examples are central to this section; mathematical notation preserved exactly; examples translated to maintain conceptual clarity

### Quality Metrics

- Semantic equivalence: 0.91
- Technical accuracy: 0.90
- Readability: 0.88
- Glossary consistency: 0.88
- **Overall section score:** 0.89

### Back-Translation (Validation)

Table 3 shows words and their most similar words, computed using the Skip-gram model trained on 783 billion words from the Google News dataset. The similarity is measured by cosine distance between word vectors.

As we can see from Table 3, the learned word representations capture a large number of precise syntactic and semantic word relationships. It is very remarkable that the word vector for "France" has a similar relationship to "Paris" as "Italy" has to "Rome". Similarly, "big" has a similar relationship to "bigger" as "small" has to "smaller". These results demonstrate that the Skip-gram model learns more than just word similarity - it learns relationships between words that can be expressed through simple vector arithmetic operations.

Perhaps the most famous example that emerged from this work is the vector arithmetic: vector("King") - vector("Man") + vector("Woman") ≈ vector("Queen")
