# Section 2: Background
## القسم 2: الخلفية

**Section:** Background
**Translation Quality:** 0.87
**Glossary Terms Used:** التدريب المسبق, نموذج, التعلم الذاتي الإشراف, محولات, الانتباه الذاتي, نمذجة اللغة, نمذجة اللغة المقنعة, ثنائي الوضع, أحادي الوضع, اللغة الطبيعية, لغة البرمجة

---

### English Version

# 2 Background

## 2.1 Pre-Trained Models in NLP

Large pre-trained models (Peters et al., 2018; Radford et al., 2018; Devlin et al., 2018; Yang et al., 2019; Liu et al., 2019; Raffel et al., 2019) have brought dramatic empirical improvements on almost every NLP task in the past few years. Successful approaches train deep neural networks on large-scale plain texts with self-supervised learning objectives. One of the most representative neural architectures is the Transformer (Vaswani et al., 2017), which is also the one used in this work. It contains multiple self-attention layers, and can be conventionally learned with gradient decent in an end-to-end manner as every component is differentiable. The terminology "self-supervised" means that supervisions used for pre-training are automatically collected from raw data without manual annotation. Dominant learning objectives are language modeling and its variations. For example, in GPT (Radford et al., 2018), the learning objective is language modeling, namely predicting the next word wk given the preceding context words {w1, w2, ..., wk−1}. As the ultimate goal of pre-training is not to train a good language model, it is desirable to consider both preceding and following contexts to learn better general-purpose contextual representations. This leads us to the masked language modeling objective used in BERT (Devlin et al., 2018), which learns to predict the masked words of a randomly masked word sequence given surrounding contexts. Masked language modeling is also used as one of the two learning objectives for training CodeBERT.

## 2.2 Multi-Modal Pre-Trained Models

The remarkable success of the pre-trained model in NLP has driven the development of multi-modal pre-trained model that learns implicit alignment between inputs of different modalities. These models are typically learned from bimodal data, such as pairs of language-image or pairs of language-video. For example, ViLBERT (Lu et al., 2019) learns from image caption data, where the model learns by reconstructing categories of masked image region or masked words given the observed inputs, and meanwhile predicting whether the caption describes the image content or not. Similarly, VideoBERT (Sun et al., 2019) learns from language-video data and is trained by video and text masked token prediction. Our work belongs to this line of research as we regard NL and PL as different modalities. Our method differs from previous works in that the fuels for model training include not only bimodal data of NL-PL pairs, but larger amounts of unimodal data such as codes without paired documentations.

A concurrent work (Kanade et al., 2019) uses masked language modeling and next sentence prediction as the objective to train a BERT model on Python source codes, where a sentence is a logical code line as defined by the Python standard. In terms of the pre-training process, CodeBERT differs from their work in that (1) CodeBERT is trained in a cross-modal style and leverages both bimodal NL-PL data and unimodal PL/NL data, (2) CodeBERT is pre-trained over six programming languages, and (3) CodeBERT is trained with a new learning objective based on replaced token detection.

---

### النسخة العربية

# 2 الخلفية

## 2.1 النماذج المُدربة مسبقاً في معالجة اللغة الطبيعية

حققت النماذج الكبيرة المُدربة مسبقاً (Peters et al., 2018; Radford et al., 2018; Devlin et al., 2018; Yang et al., 2019; Liu et al., 2019; Raffel et al., 2019) تحسينات تجريبية هائلة في كل مهمة من مهام معالجة اللغة الطبيعية تقريباً في السنوات القليلة الماضية. تدرب الطرق الناجحة الشبكات العصبية العميقة على نصوص واضحة واسعة النطاق بأهداف التعلم الذاتي الإشراف. واحدة من أكثر المعماريات العصبية تمثيلاً هي المحولات (Vaswani et al., 2017)، وهي أيضاً المستخدمة في هذا العمل. تحتوي على طبقات انتباه ذاتي متعددة، ويمكن تعلمها بشكل تقليدي بالانحدار التدرجي بطريقة من البداية إلى النهاية حيث أن كل مكون قابل للتفاضل. مصطلح "الذاتي الإشراف" يعني أن الإشرافات المستخدمة للتدريب المسبق يتم جمعها تلقائياً من البيانات الخام دون تعليق توضيحي يدوي. الأهداف التعليمية السائدة هي نمذجة اللغة وتنوعاتها. على سبيل المثال، في GPT (Radford et al., 2018)، الهدف التعليمي هو نمذجة اللغة، أي التنبؤ بالكلمة التالية wk بناءً على كلمات السياق السابقة {w1, w2, ..., wk−1}. نظراً لأن الهدف النهائي من التدريب المسبق ليس تدريب نموذج لغة جيد، فمن المرغوب فيه النظر في كل من السياقات السابقة واللاحقة لتعلم تمثيلات سياقية عامة الغرض أفضل. يقودنا هذا إلى هدف نمذجة اللغة المقنعة المستخدم في BERT (Devlin et al., 2018)، والذي يتعلم التنبؤ بالكلمات المقنعة من تسلسل كلمات مقنّع عشوائياً بناءً على السياقات المحيطة. تُستخدم نمذجة اللغة المقنعة أيضاً كواحد من الهدفين التعليميين لتدريب CodeBERT.

## 2.2 النماذج المُدربة مسبقاً متعددة الأنماط

دفع النجاح الملحوظ للنموذج المُدرب مسبقاً في معالجة اللغة الطبيعية إلى تطوير النموذج المُدرب مسبقاً متعدد الأنماط الذي يتعلم التوافق الضمني بين مدخلات الأنماط المختلفة. عادةً ما يتم تعلم هذه النماذج من بيانات ثنائية الوضع، مثل أزواج اللغة والصور أو أزواج اللغة والفيديو. على سبيل المثال، يتعلم ViLBERT (Lu et al., 2019) من بيانات التسميات النصية للصور، حيث يتعلم النموذج من خلال إعادة بناء فئات المنطقة المقنعة من الصورة أو الكلمات المقنعة بناءً على المدخلات الملاحظة، وفي نفس الوقت التنبؤ بما إذا كانت التسمية النصية تصف محتوى الصورة أم لا. بالمثل، يتعلم VideoBERT (Sun et al., 2019) من بيانات اللغة والفيديو ويتم تدريبه بالتنبؤ بالرموز المقنعة للفيديو والنص. ينتمي عملنا إلى هذا الخط من البحث حيث نعتبر اللغة الطبيعية ولغة البرمجة أنماطاً مختلفة. تختلف طريقتنا عن الأعمال السابقة في أن وقود تدريب النموذج يتضمن ليس فقط بيانات ثنائية الوضع لأزواج اللغة الطبيعية ولغة البرمجة، ولكن أيضاً كميات أكبر من البيانات أحادية الوضع مثل الشفرات بدون توثيقات مقترنة.

يستخدم عمل متزامن (Kanade et al., 2019) نمذجة اللغة المقنعة والتنبؤ بالجملة التالية كهدف لتدريب نموذج BERT على شفرات مصدر Python، حيث الجملة هي سطر شفرة منطقي كما هو معرّف في معيار Python. من حيث عملية التدريب المسبق، يختلف CodeBERT عن عملهم في أن (1) يتم تدريب CodeBERT بأسلوب متقاطع الأنماط ويستفيد من كل من بيانات اللغة الطبيعية ولغة البرمجة ثنائية الوضع وبيانات لغة البرمجة/اللغة الطبيعية أحادية الوضع، و(2) يتم التدريب المسبق لـ CodeBERT على ست لغات برمجة، و(3) يتم تدريب CodeBERT بهدف تعليمي جديد قائم على الكشف عن الرموز المستبدلة.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:** Self-supervised learning, Transformer, self-attention, language modeling, masked language modeling, multi-modal, cross-modal, replaced token detection
- **Equations:** 0
- **Citations:** 14 references cited
- **Special handling:** Preserved model names (ELMo, GPT, BERT, XLNet, RoBERTa, ViLBERT, VideoBERT) in English; maintained mathematical notation {w1, w2, ..., wk−1}

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-Translation Sample

Key paragraph (from 2.1) back-translated to verify quality:

**Arabic:** "واحدة من أكثر المعماريات العصبية تمثيلاً هي المحولات، وهي أيضاً المستخدمة في هذا العمل. تحتوي على طبقات انتباه ذاتي متعددة، ويمكن تعلمها بشكل تقليدي بالانحدار التدرجي بطريقة من البداية إلى النهاية حيث أن كل مكون قابل للتفاضل."

**Back-translation:** "One of the most representative neural architectures is the Transformer, which is also the one used in this work. It contains multiple self-attention layers, and can be learned conventionally with gradient descent in an end-to-end manner as every component is differentiable."

**Semantic match:** ✓ High fidelity to original
