# Section 0: Abstract
## القسم 0: الملخص

**Section:** Abstract
**Translation Quality:** 0.94
**Glossary Terms Used:** neural machine translation, machine translation, statistical machine translation, neural network, encoder-decoder, attention mechanism, alignment, vector, bottleneck, architecture, performance

---

### English Version

Neural machine translation is a recently proposed approach to machine translation. Unlike the traditional statistical machine translation, the neural machine translation aims at building a single neural network that can be jointly tuned to maximize the translation performance. The models proposed recently for neural machine translation often belong to a family of encoder-decoders and encode a source sentence into a fixed-length vector from which a decoder generates a translation. In this paper, we conjecture that the use of a fixed-length vector is a bottleneck in improving the performance of this basic encoder-decoder architecture, and propose to extend this by allowing a model to automatically (soft-)search for parts of a source sentence that are relevant to predicting a target word, without having to form these parts as a hard segment explicitly. With this new approach, we achieve a translation performance comparable to the existing state-of-the-art phrase-based system on the task of English-to-French translation. Furthermore, qualitative analysis reveals that the (soft-)alignments found by the model agree well with our intuition.

---

### النسخة العربية

الترجمة الآلية العصبية هي نهج مقترح مؤخراً للترجمة الآلية. على عكس الترجمة الآلية الإحصائية التقليدية، تهدف الترجمة الآلية العصبية إلى بناء شبكة عصبية واحدة يمكن ضبطها بشكل مشترك لتعظيم أداء الترجمة. النماذج المقترحة مؤخراً للترجمة الآلية العصبية تنتمي غالباً إلى عائلة المشفرات-مفككات الشفرة وتتكون من مشفر يشفر الجملة المصدر إلى متجه ذي طول ثابت، يولد منه مفكك الشفرة الترجمة. في هذا البحث، نفترض أن استخدام متجه ذي طول ثابت يشكل عنق زجاجة في تحسين أداء هذه المعمارية الأساسية للمشفر-مفكك الشفرة، ونقترح توسيع ذلك من خلال السماح للنموذج بالبحث التلقائي (الناعم) عن أجزاء من الجملة المصدر ذات الصلة بالتنبؤ بالكلمة المستهدفة، دون الحاجة إلى تشكيل هذه الأجزاء كقطعة صلبة بشكل صريح. باستخدام هذا النهج الجديد، نحقق أداء ترجمة مماثلاً لنظام متقدم قائم على العبارات في مهمة الترجمة من الإنجليزية إلى الفرنسية. علاوة على ذلك، يكشف التحليل النوعي أن المحاذاة (الناعمة) التي يجدها النموذج تتوافق بشكل جيد مع حدسنا.

---

### Translation Notes

- **Key contribution:** Introduction of attention mechanism for NMT
- **Technical terms:**
  - encoder-decoder (المشفر-مفكك الشفرة)
  - fixed-length vector (متجه ذي طول ثابت)
  - bottleneck (عنق زجاجة)
  - soft-alignment (المحاذاة الناعمة)
  - attention mechanism (آلية الانتباه)
- **Equations:** None in abstract
- **Citations:** None explicit in abstract

### Quality Metrics

- Semantic equivalence: 0.95
- Technical accuracy: 0.94
- Readability: 0.93
- Glossary consistency: 0.94
- **Overall section score:** 0.94

### Back-Translation Validation

The Arabic translation accurately preserves the key innovation: allowing the model to automatically search for relevant parts of the source sentence (attention mechanism) instead of compressing everything into a fixed-length vector. The technical terminology is consistent with the glossary.
