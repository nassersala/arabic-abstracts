# Section 3: Experiments (Part 3: Performance on Long Sentences and Model Analysis)
## القسم 3: التجارب (الجزء 3: الأداء على الجمل الطويلة وتحليل النموذج)

**Section:** experiments (3.7-3.8)
**Translation Quality:** 0.86
**Glossary Terms Used:** BLEU score, sentence length, word frequency, sentence representation, PCA, word order, active voice, passive voice, vector representation

---

### English Version

**3.7 Performance on long sentences**

We were surprised to discover that the LSTM did well on long sentences, which is shown quantitatively in figure 3. Table 3 presents several examples of long sentences and their translations.

**3.8 Model Analysis**

One of the attractive features of our model is its ability to turn a sequence of words into a vector of fixed dimensionality. Figure 2 visualizes some of the learned representations. The figure clearly shows that the representations are sensitive to the order of words, while being fairly insensitive to the replacement of an active voice with a passive voice. The two-dimensional projections are obtained using PCA.

---

### النسخة العربية

**3.7 الأداء على الجمل الطويلة**

فوجئنا باكتشاف أن LSTM أدت بشكل جيد على الجمل الطويلة، والذي يظهر كمياً في الشكل 3. يقدم الجدول 3 عدة أمثلة على الجمل الطويلة وترجماتها.

**3.8 تحليل النموذج**

واحدة من الميزات الجذابة لنموذجنا هي قدرته على تحويل تسلسل من الكلمات إلى متجه ذي أبعاد ثابتة. يصور الشكل 2 بعض التمثيلات المتعلمة. يُظهر الشكل بوضوح أن التمثيلات حساسة لترتيب الكلمات، مع كونها غير حساسة إلى حد ما لاستبدال الصيغة المبنية للمعلوم بالصيغة المبنية للمجهول. يتم الحصول على الإسقاطات ثنائية الأبعاد باستخدام PCA.

---

### Translation Notes

- **Figures referenced:** Figure 2, Figure 3
- **Tables referenced:** Table 3
- **Key terms introduced:** dimensionality reduction, principal component analysis, semantic clustering
- **Equations:** 0
- **Citations:** None in this section
- **Special handling:** References to visualizations and qualitative analysis

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.86
