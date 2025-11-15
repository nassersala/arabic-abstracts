# Section 1: Introduction
## القسم 1: المقدمة

**Section:** Introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** neural machine translation, phrase-based translation, encoder-decoder, fixed-length vector, alignment, translate, neural network, training corpus, context vector, source sentence, target word

---

### English Version

Neural machine translation is a newly emerging approach to machine translation, recently proposed by Kalchbrenner and Blunsom (2013), Sutskever et al. (2014) and Cho et al. (2014b). Unlike the traditional phrase-based translation system (see, e.g., Koehn et al., 2003) which consists of many small sub-components that are tuned separately, neural machine translation attempts to build and train a single, large neural network that reads a sentence and outputs a correct translation.

Most of the proposed neural machine translation models belong to a family of encoder–decoders (Sutskever et al., 2014; Cho et al., 2014a), with an encoder and a decoder for each language, or involve a language-specific encoder applied to each sentence whose outputs are then compared (Hermann and Blunsom, 2014). An encoder neural network reads and encodes a source sentence into a fixed-length vector. A decoder then outputs a translation from the encoded vector. The whole encoder–decoder system, which consists of the encoder and the decoder for a language pair, is jointly trained to maximize the probability of a correct translation given a source sentence.

A potential issue with this encoder–decoder approach is that a neural network needs to be able to compress all the necessary information of a source sentence into a fixed-length vector. This may make it difficult for the neural network to cope with long sentences, especially those that are longer than the sentences in the training corpus. Cho et al. (2014b) showed that indeed the performance of a basic encoder–decoder deteriorates rapidly as the length of an input sentence increases.

In order to address this issue, we introduce an extension to the encoder–decoder model which learns to align and translate jointly. Each time the proposed model generates a word in a translation, it (soft-)searches for a set of positions in a source sentence where the most relevant information is concentrated. The model then predicts a target word based on the context vectors associated with these source positions and all the previous generated target words.

---

### النسخة العربية

الترجمة الآلية العصبية هي نهج ناشئ حديثاً للترجمة الآلية، اقترحه مؤخراً كالشبرينر وبلانسوم (2013)، وسوتسكيفر وآخرون (2014)، وتشو وآخرون (2014ب). على عكس نظام الترجمة التقليدي القائم على العبارات (انظر، على سبيل المثال، كوهن وآخرون، 2003) الذي يتكون من العديد من المكونات الفرعية الصغيرة التي يتم ضبطها بشكل منفصل، تحاول الترجمة الآلية العصبية بناء وتدريب شبكة عصبية واحدة كبيرة تقرأ جملة وتخرج ترجمة صحيحة.

معظم نماذج الترجمة الآلية العصبية المقترحة تنتمي إلى عائلة المشفرات-مفككات الشفرة (سوتسكيفر وآخرون، 2014؛ تشو وآخرون، 2014أ)، مع مشفر ومفكك شفرة لكل لغة، أو تتضمن مشفراً خاصاً باللغة يُطبق على كل جملة ثم تُقارن مخرجاته (هيرمان وبلانسوم، 2014). تقرأ الشبكة العصبية المشفرة جملة مصدر وتشفرها إلى متجه ذي طول ثابت. ثم يخرج مفكك الشفرة ترجمة من المتجه المشفر. يتم تدريب نظام المشفر-مفكك الشفرة بأكمله، الذي يتكون من المشفر ومفكك الشفرة لزوج من اللغات، بشكل مشترك لتعظيم احتمالية الحصول على ترجمة صحيحة لجملة مصدر معينة.

المشكلة المحتملة في نهج المشفر-مفكك الشفرة هذا هي أن الشبكة العصبية تحتاج إلى أن تكون قادرة على ضغط جميع المعلومات الضرورية من جملة مصدر إلى متجه ذي طول ثابت. قد يجعل هذا من الصعب على الشبكة العصبية التعامل مع الجمل الطويلة، خاصة تلك التي تكون أطول من الجمل في مدونة التدريب. أظهر تشو وآخرون (2014ب) أن أداء المشفر-مفكك الشفرة الأساسي يتدهور بسرعة بالفعل مع زيادة طول الجملة المدخلة.

من أجل معالجة هذه المشكلة، نقدم امتداداً لنموذج المشفر-مفكك الشفرة يتعلم المحاذاة والترجمة بشكل مشترك. في كل مرة يولد فيها النموذج المقترح كلمة في الترجمة، فإنه يبحث (بشكل ناعم) عن مجموعة من المواضع في الجملة المصدر حيث تتركز المعلومات الأكثر صلة. ثم يتنبأ النموذج بكلمة مستهدفة بناءً على متجهات السياق المرتبطة بمواضع المصدر هذه وجميع الكلمات المستهدفة المولدة سابقاً.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:**
  - neural machine translation (الترجمة الآلية العصبية)
  - phrase-based translation (الترجمة القائمة على العبارات)
  - encoder-decoder (المشفر-مفكك الشفرة)
  - fixed-length vector (متجه ذي طول ثابت)
  - soft-search (البحث الناعم)
  - align and translate (المحاذاة والترجمة)
  - context vector (متجه السياق)
  - training corpus (مدونة التدريب)
- **Equations:** None
- **Citations:** Multiple references to Kalchbrenner and Blunsom (2013), Sutskever et al. (2014), Cho et al. (2014a, 2014b), Koehn et al. (2003), Hermann and Blunsom (2014)
- **Special handling:**
  - Distinguished between different citation years (2014a, 2014b) in Arabic (2014أ، 2014ب)
  - Maintained technical precision for "soft-search" (البحث الناعم)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87

### Back-Translation (Key Paragraph)

"In order to address this problem, we present an extension to the encoder-decoder model that learns alignment and translation jointly. Each time the proposed model generates a word in the translation, it searches (softly) for a set of positions in the source sentence where the most relevant information is concentrated. The model then predicts a target word based on the context vectors associated with these source positions and all previously generated target words."

**Validation:** ✅ Semantic match confirmed. The back-translation preserves the key innovation and technical details accurately.
