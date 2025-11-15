# Section 1: Introduction
## القسم الأول: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** neural machine translation, statistical machine translation, encoder-decoder, fixed-length vector, bottleneck, bidirectional, RNN, alignment, attention mechanism, BLEU score

---

### English Version

Neural machine translation is a recently proposed approach to machine translation. Unlike the traditional statistical machine translation, the neural machine translation aims at building a single neural network that can be jointly tuned to maximize the translation performance.

The models proposed recently for neural machine translation often belong to a family of encoder–decoders and encode a variable-length source sentence into a fixed-length vector from which a decoder generates a translation. The most known models of this family are RNN Encoder–Decoder and a Mixture of Hidden Markov Models (HMMs).

A potential issue with this encoder–decoder approach is that a neural network needs to be able to compress all the necessary information of a source sentence into a fixed-length vector. This may make it difficult for the neural network to cope with long sentences, especially those that are longer than the sentences in the training corpus. Cho et al. (2014b) showed that indeed the performance of a basic encoder–decoder deteriorates rapidly as the length of an input sentence increases.

In order to address this issue, we introduce an extension to the encoder–decoder model which learns to align and translate jointly. Each time the proposed model generates a word in a translation, it (soft-)searches for a set of positions in a source sentence where the most relevant information is concentrated. The model then predicts a target word based on the context vectors associated with these source positions and all the previous generated target words.

The most important distinguishing feature of this approach from the basic encoder–decoder is that it does not attempt to encode a whole input sentence into a single fixed-length vector. Instead, it encodes the input sentence into a sequence of vectors and chooses a subset of these vectors adaptively while decoding the translation. This frees a neural translation model from having to squash all the information of a source sentence, regardless of its length, into a fixed-length vector. We show this allows a model to cope better with long sentences.

In this paper, we show that the proposed approach of jointly learning to align and translate achieves significantly improved translation performance over the basic encoder–decoder approach. The improvement is more apparent with longer sentences, but can be observed with sentences of any length. On the task of English-to-French translation, the proposed approach achieves, with a single model, a translation performance comparable, or close, to the existing state-of-the-art phrase-based system Moses. Furthermore, qualitative analysis reveals that the alignments found by the model agree well with our linguistic intuition.

---

### النسخة العربية

الترجمة الآلية العصبية هي نهج مقترح مؤخراً للترجمة الآلية. على عكس الترجمة الآلية الإحصائية التقليدية، تهدف الترجمة الآلية العصبية إلى بناء شبكة عصبية واحدة يمكن ضبطها بشكل مشترك لتعظيم أداء الترجمة.

النماذج المقترحة مؤخراً للترجمة الآلية العصبية تنتمي غالباً إلى عائلة المشفرات-مفككات الشفرة وتقوم بتشفير جملة مصدر ذات طول متغير إلى متجه ذي طول ثابت، يولد منه مفكك الشفرة الترجمة. أشهر نماذج هذه العائلة هي الشبكة العصبية المتكررة المشفرة-مفككة الشفرة ومزيج من نماذج ماركوف المخفية.

مشكلة محتملة في نهج المشفر-مفكك الشفرة هذا هي أن الشبكة العصبية تحتاج إلى القدرة على ضغط جميع المعلومات الضرورية من الجملة المصدر إلى متجه ذي طول ثابت. قد يجعل هذا من الصعب على الشبكة العصبية التعامل مع الجمل الطويلة، خاصة تلك التي تكون أطول من الجمل في مجموعة البيانات التدريبية. أظهر Cho وآخرون (2014b) أن أداء المشفر-مفكك الشفرة الأساسي يتدهور بسرعة مع زيادة طول الجملة المُدخلة.

من أجل معالجة هذه المشكلة، نقدم توسعة لنموذج المشفر-مفكك الشفرة تتعلم المحاذاة والترجمة بشكل مشترك. في كل مرة يولد فيها النموذج المقترح كلمة في الترجمة، يبحث (بشكل ناعم) عن مجموعة من المواضع في الجملة المصدر حيث تتركز المعلومات الأكثر صلة. ثم يتنبأ النموذج بكلمة مستهدفة بناءً على متجهات السياق المرتبطة بهذه المواضع المصدر وجميع الكلمات المستهدفة المُولدة مسبقاً.

الميزة التمييزية الأهم لهذا النهج عن المشفر-مفكك الشفرة الأساسي هي أنه لا يحاول تشفير الجملة المُدخلة بأكملها إلى متجه واحد ذي طول ثابت. بدلاً من ذلك، يشفر الجملة المُدخلة إلى تسلسل من المتجهات ويختار مجموعة فرعية من هذه المتجهات بشكل تكيفي أثناء فك تشفير الترجمة. هذا يحرر نموذج الترجمة العصبية من الاضطرار لضغط جميع معلومات الجملة المصدر، بغض النظر عن طولها، في متجه ذي طول ثابت. نُظهر أن هذا يسمح للنموذج بالتعامل بشكل أفضل مع الجمل الطويلة.

في هذا البحث، نُظهر أن النهج المقترح للتعلم المشترك للمحاذاة والترجمة يحقق تحسناً ملحوظاً في أداء الترجمة مقارنة بنهج المشفر-مفكك الشفرة الأساسي. التحسن أكثر وضوحاً مع الجمل الأطول، لكن يمكن ملاحظته مع جمل من أي طول. في مهمة الترجمة من الإنجليزية إلى الفرنسية، يحقق النهج المقترح، باستخدام نموذج واحد، أداء ترجمة مماثل أو قريب من نظام Moses المتقدم القائم على العبارات. علاوة على ذلك، يكشف التحليل النوعي أن المحاذاة التي يجدها النموذج تتوافق بشكل جيد مع حدسنا اللغوي.

---

### Translation Notes

- **Problem Statement:** Fixed-length vector bottleneck in encoder-decoder models
- **Key Reference:** Cho et al. (2014b) on performance deterioration with long sentences
- **Proposed Solution:** Joint learning of alignment and translation through attention
- **Key Innovation:** Adaptive selection from sequence of vectors instead of single fixed vector
- **Results Preview:** Comparable to Moses phrase-based system on English-French translation
- **Figures referenced:** None in introduction
- **Key terms introduced:** soft-search, alignment, attention mechanism, context vectors
- **Citations:** Cho et al. (2014b), reference to Moses system

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.88

### Back-Translation Validation

Neural machine translation is a recently proposed approach to machine translation. Unlike traditional statistical machine translation, neural machine translation aims to build a single neural network that can be jointly tuned to maximize translation performance.

Recently proposed models for neural machine translation often belong to the family of encoder-decoders and encode a variable-length source sentence into a fixed-length vector, from which the decoder generates the translation. The most famous models in this family are the Recurrent Neural Network Encoder-Decoder and a mixture of Hidden Markov Models.

A potential problem with this encoder-decoder approach is that the neural network needs the ability to compress all necessary information from the source sentence into a fixed-length vector. This may make it difficult for the neural network to handle long sentences, especially those that are longer than sentences in the training dataset. Cho et al. (2014b) showed that the performance of the basic encoder-decoder deteriorates rapidly as the length of the input sentence increases.

To address this problem, we present an extension to the encoder-decoder model that learns alignment and translation jointly. Each time the proposed model generates a word in the translation, it (softly) searches for a set of positions in the source sentence where the most relevant information is concentrated. The model then predicts a target word based on the context vectors associated with these source positions and all previously generated target words.

The most important distinguishing feature of this approach from the basic encoder-decoder is that it does not attempt to encode the entire input sentence into a single fixed-length vector. Instead, it encodes the input sentence into a sequence of vectors and adaptively selects a subset of these vectors while decoding the translation. This frees the neural translation model from having to compress all information from the source sentence, regardless of its length, into a fixed-length vector. We show that this allows the model to better handle long sentences.

In this research, we show that the proposed approach of jointly learning alignment and translation achieves significant improvement in translation performance compared to the basic encoder-decoder approach. The improvement is more noticeable with longer sentences, but can be observed with sentences of any length. In the English-to-French translation task, the proposed approach achieves, using a single model, translation performance comparable or close to the advanced Moses phrase-based system. Furthermore, qualitative analysis reveals that the alignment found by the model agrees well with our linguistic intuition.
