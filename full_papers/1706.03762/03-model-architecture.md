# Section 3: Model Architecture
## القسم 3: معمارية النموذج

**Section:** model-architecture
**Translation Quality:** 0.87
**Glossary Terms Used:** encoder, decoder, attention mechanism, self-attention, multi-head attention, feed-forward network, residual connection, layer normalization, embedding, softmax, positional encoding

---

### English Version

Most competitive neural sequence transduction models have an encoder-decoder structure [5, 2, 35]. Here, the encoder maps an input sequence of symbol representations (x₁, ..., xₙ) to a sequence of continuous representations **z** = (z₁, ..., zₙ). Given **z**, the decoder then generates an output sequence (y₁, ..., yₘ) of symbols one element at a time. At each step the model is auto-regressive [10], consuming the previously generated symbols as additional input when generating the next.

The Transformer follows this overall architecture using stacked self-attention and point-wise, fully connected layers for both the encoder and decoder, shown in the left and right halves of Figure 1, respectively.

## 3.1 Encoder and Decoder Stacks

**Encoder:** The encoder is composed of a stack of N = 6 identical layers. Each layer has two sub-layers. The first is a multi-head self-attention mechanism, and the second is a simple, position-wise fully connected feed-forward network. We employ a residual connection [11] around each of the two sub-layers, followed by layer normalization [1]. That is, the output of each sub-layer is LayerNorm(x + Sublayer(x)), where Sublayer(x) is the function implemented by the sub-layer itself. To facilitate these residual connections, all sub-layers in the model, as well as the embedding layers, produce outputs of dimension d_model = 512.

**Decoder:** The decoder is also composed of a stack of N = 6 identical layers. In addition to the two sub-layers in each encoder layer, the decoder inserts a third sub-layer, which performs multi-head attention over the output of the encoder stack. Similar to the encoder, we employ residual connections around each of the sub-layers, followed by layer normalization. We also modify the self-attention sub-layer in the decoder stack to prevent positions from attending to subsequent positions. This masking, combined with fact that the output embeddings are offset by one position, ensures that the predictions for position i can depend only on the known outputs at positions less than i.

## 3.2 Attention

An attention function can be described as mapping a query and a set of key-value pairs to an output, where the query, keys, values, and output are all vectors. The output is computed as a weighted sum of the values, where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key.

### 3.2.1 Scaled Dot-Product Attention

We call our particular attention "Scaled Dot-Product Attention" (Figure 2). The input consists of queries and keys of dimension d_k, and values of dimension d_v. We compute the dot products of the query with all keys, divide each by √d_k, and apply a softmax function to obtain the weights on the values.

In practice, we compute the attention function on a set of queries simultaneously, packed together into a matrix Q. The keys and values are also packed together into matrices K and V. We compute the matrix of outputs as:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V \quad (1)$$

The two most commonly used attention functions are additive attention [2], and dot-product (multiplicative) attention. Dot-product attention is identical to our algorithm, except for the scaling factor of $\frac{1}{\sqrt{d_k}}$. Additive attention computes the compatibility function using a feed-forward network with a single hidden layer. While the two are similar in theoretical complexity, dot-product attention is much faster and more space-efficient in practice, since it can be implemented using highly optimized matrix multiplication code.

While for small values of d_k the two mechanisms perform similarly, additive attention outperforms dot product attention without scaling for larger values of d_k [3]. We suspect that for large values of d_k, the dot products grow large in magnitude, pushing the softmax function into regions where it has extremely small gradients. To counteract this effect, we scale the dot products by $\frac{1}{\sqrt{d_k}}$.

### 3.2.2 Multi-Head Attention

Instead of performing a single attention function with d_model-dimensional keys, values and queries, we found it beneficial to linearly project the queries, keys and values h times with different, learned linear projections to d_k, d_k and d_v dimensions, respectively. On each of these projected versions of queries, keys and values we then perform the attention function in parallel, yielding d_v-dimensional output values. These are concatenated and once again projected, resulting in the final values, as depicted in Figure 2.

Multi-head attention allows the model to jointly attend to information from different representation subspaces at different positions. With a single attention head, averaging inhibits this.

$$\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, ..., \text{head}_h)W^O$$

where $\text{head}_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)$

Where the projections are parameter matrices $W_i^Q \in \mathbb{R}^{d_{\text{model}} \times d_k}$, $W_i^K \in \mathbb{R}^{d_{\text{model}} \times d_k}$, $W_i^V \in \mathbb{R}^{d_{\text{model}} \times d_v}$ and $W^O \in \mathbb{R}^{hd_v \times d_{\text{model}}}$.

In this work we employ h = 8 parallel attention layers, or heads. For each of these we use d_k = d_v = d_model/h = 64. Due to the reduced dimension of each head, the total computational cost is similar to that of single-head attention with full dimensionality.

### 3.2.3 Applications of Attention in our Model

The Transformer uses multi-head attention in three different ways:

• In "encoder-decoder attention" layers, the queries come from the previous decoder layer, and the memory keys and values come from the output of the encoder. This allows every position in the decoder to attend over all positions in the input sequence. This mimics the typical encoder-decoder attention mechanisms in sequence-to-sequence models such as [38, 2, 9].

• The encoder contains self-attention layers. In a self-attention layer all of the keys, values and queries come from the same place, in this case, the output of the previous layer in the encoder. Each position in the encoder can attend to all positions in the previous layer of the encoder.

• Similarly, self-attention layers in the decoder allow each position in the decoder to attend to all positions in the decoder up to and including that position. We need to prevent leftward information flow in the decoder to preserve the auto-regressive property. We implement this inside of scaled dot-product attention by masking out (setting to −∞) all values in the input of the softmax which correspond to illegal connections. See Figure 2.

## 3.3 Position-wise Feed-Forward Networks

In addition to attention sub-layers, each of the layers in our encoder and decoder contains a fully connected feed-forward network, which is applied to each position separately and identically. This consists of two linear transformations with a ReLU activation in between.

$$\text{FFN}(x) = \max(0, xW_1 + b_1)W_2 + b_2 \quad (2)$$

While the linear transformations are the same across different positions, they use different parameters from layer to layer. Another way of describing this is as two convolutions with kernel size 1. The dimensionality of input and output is d_model = 512, and the inner-layer has dimensionality d_ff = 2048.

## 3.4 Embeddings and Softmax

Similarly to other sequence transduction models, we use learned embeddings to convert the input tokens and output tokens to vectors of dimension d_model. We also use the usual learned linear transformation and softmax function to convert the decoder output to predicted next-token probabilities. In our model, we share the same weight matrix between the two embedding layers and the pre-softmax linear transformation, similar to [30]. In the embedding layers, we multiply those weights by √d_model.

## 3.5 Positional Encoding

Since our model contains no recurrence and no convolution, in order for the model to make use of the order of the sequence, we must inject some information about the relative or absolute position of the tokens in the sequence. To this end, we add "positional encodings" to the input embeddings at the bottoms of the encoder and decoder stacks. The positional encodings have the same dimension d_model as the embeddings, so that the two can be summed. There are many choices of positional encodings, learned and fixed [9].

In this work, we use sine and cosine functions of different frequencies:

$$PE_{(pos,2i)} = \sin(pos/10000^{2i/d_{\text{model}}})$$
$$PE_{(pos,2i+1)} = \cos(pos/10000^{2i/d_{\text{model}}})$$

where pos is the position and i is the dimension. That is, each dimension of the positional encoding corresponds to a sinusoid. The wavelengths form a geometric progression from 2π to 10000 · 2π. We chose this function because we hypothesized it would allow the model to easily learn to attend by relative positions, since for any fixed offset k, PE_pos+k can be represented as a linear function of PE_pos.

We also experimented with using learned positional embeddings [9] instead, and found that the two versions produced nearly identical results (see Table 3 row (E)). We chose the sinusoidal version because it may allow the model to extrapolate to sequence lengths longer than the ones encountered during training.

---

### النسخة العربية

تمتلك معظم نماذج تحويل التسلسلات العصبية التنافسية بنية مشفّر-فك تشفير [5، 2، 35]. هنا، يُعيّن المشفّر تسلسل إدخال من تمثيلات الرموز (x₁, ..., xₙ) إلى تسلسل من التمثيلات المستمرة **z** = (z₁, ..., zₙ). بالنظر إلى **z**، يولّد فك التشفير بعد ذلك تسلسل إخراج (y₁, ..., yₘ) من الرموز عنصراً واحداً في كل مرة. في كل خطوة، يكون النموذج انحدارياً تلقائياً [10]، يستهلك الرموز المولّدة مسبقاً كإدخال إضافي عند توليد الرمز التالي.

يتبع المحوّل هذه المعمارية الشاملة باستخدام الانتباه الذاتي المكدّس وطبقات متصلة بالكامل نقطية لكل من المشفّر وفك التشفير، الموضحة في النصفين الأيسر والأيمن من الشكل 1، على التوالي.

## 3.1 مكدّسات المشفّر وفك التشفير

**المشفّر:** يتكون المشفّر من مكدّس من N = 6 طبقات متطابقة. كل طبقة لها طبقتان فرعيتان. الأولى هي آلية انتباه ذاتي متعدد الرؤوس، والثانية هي شبكة تغذية أمامية متصلة بالكامل بسيطة حسب الموضع. نستخدم اتصالاً متبقياً (residual connection) [11] حول كل من الطبقتين الفرعيتين، يليه تطبيع الطبقة (layer normalization) [1]. أي أن إخراج كل طبقة فرعية هو LayerNorm(x + Sublayer(x))، حيث Sublayer(x) هي الدالة التي تنفذها الطبقة الفرعية نفسها. لتسهيل هذه الاتصالات المتبقية، تنتج جميع الطبقات الفرعية في النموذج، بالإضافة إلى طبقات التضمين، مخرجات ذات بُعد d_model = 512.

**فك التشفير:** يتكون فك التشفير أيضاً من مكدّس من N = 6 طبقات متطابقة. بالإضافة إلى الطبقتين الفرعيتين في كل طبقة مشفّر، يُدرج فك التشفير طبقة فرعية ثالثة، تؤدي انتباهاً متعدد الرؤوس على إخراج مكدّس المشفّر. على غرار المشفّر، نستخدم اتصالات متبقية حول كل من الطبقات الفرعية، يليها تطبيع الطبقة. نعدّل أيضاً الطبقة الفرعية للانتباه الذاتي في مكدّس فك التشفير لمنع المواضع من الانتباه إلى المواضع اللاحقة. هذا الإخفاء، جنباً إلى جنب مع حقيقة أن تضمينات الإخراج منحازة بموضع واحد، يضمن أن التنبؤات للموضع i يمكن أن تعتمد فقط على المخرجات المعروفة في المواضع الأقل من i.

## 3.2 الانتباه

يمكن وصف دالة الانتباه على أنها تعيين استعلام (query) ومجموعة من أزواج المفتاح-القيمة (key-value pairs) إلى إخراج، حيث يكون الاستعلام والمفاتيح والقيم والإخراج جميعها متجهات. يُحسب الإخراج كمجموع موزون للقيم، حيث يُحسب الوزن المُخصص لكل قيمة بواسطة دالة توافق (compatibility function) للاستعلام مع المفتاح المقابل.

### 3.2.1 انتباه الجداء النقطي المقيّس

نسمي انتباهنا الخاص "انتباه الجداء النقطي المقيّس" (Scaled Dot-Product Attention) (الشكل 2). يتكون الإدخال من استعلامات ومفاتيح ذات بُعد d_k، وقيم ذات بُعد d_v. نحسب الجداءات النقطية للاستعلام مع جميع المفاتيح، ونقسم كل منها على √d_k، ونطبق دالة softmax للحصول على الأوزان على القيم.

في الممارسة العملية، نحسب دالة الانتباه على مجموعة من الاستعلامات في وقت واحد، معبأة معاً في مصفوفة Q. يتم أيضاً تعبئة المفاتيح والقيم معاً في مصفوفات K و V. نحسب مصفوفة المخرجات على النحو التالي:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V \quad (1)$$

دالتا الانتباه الأكثر استخداماً هما الانتباه الإضافي (additive attention) [2]، والانتباه الجدائي (dot-product/multiplicative attention). الانتباه الجدائي مطابق لخوارزميتنا، باستثناء معامل القياس $\frac{1}{\sqrt{d_k}}$. يحسب الانتباه الإضافي دالة التوافق باستخدام شبكة تغذية أمامية بطبقة مخفية واحدة. بينما الاثنان متشابهان في التعقيد النظري، فإن الانتباه الجدائي أسرع بكثير وأكثر كفاءة في المساحة في الممارسة العملية، حيث يمكن تنفيذه باستخدام كود ضرب المصفوفات المُحسّن للغاية.

بينما تؤدي الآليتان بشكل مماثل لقيم d_k الصغيرة، يتفوق الانتباه الإضافي على الانتباه الجدائي بدون قياس لقيم d_k الأكبر [3]. نشتبه في أنه لقيم d_k الكبيرة، تنمو الجداءات النقطية كبيرة من حيث الحجم، مما يدفع دالة softmax إلى مناطق ذات تدرجات صغيرة للغاية. لمواجهة هذا التأثير، نقيّس الجداءات النقطية بـ $\frac{1}{\sqrt{d_k}}$.

### 3.2.2 الانتباه متعدد الرؤوس

بدلاً من أداء دالة انتباه واحدة بمفاتيح وقيم واستعلامات ذات بُعد d_model، وجدنا أنه من المفيد إسقاط الاستعلامات والمفاتيح والقيم خطياً h مرات بإسقاطات خطية مختلفة ومُتعلّمة إلى أبعاد d_k و d_k و d_v، على التوالي. على كل من هذه الإصدارات المُسقطة من الاستعلامات والمفاتيح والقيم، نؤدي بعد ذلك دالة الانتباه بالتوازي، مما يُعطي قيم إخراج ذات بُعد d_v. يتم دمج هذه وإسقاطها مرة أخرى، مما ينتج عنه القيم النهائية، كما هو موضح في الشكل 2.

يسمح الانتباه متعدد الرؤوس للنموذج بالانتباه المشترك إلى المعلومات من فضاءات فرعية مختلفة للتمثيل في مواضع مختلفة. مع رأس انتباه واحد، يمنع المتوسط ذلك.

$$\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, ..., \text{head}_h)W^O$$

حيث $\text{head}_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)$

حيث الإسقاطات هي مصفوفات معاملات $W_i^Q \in \mathbb{R}^{d_{\text{model}} \times d_k}$، $W_i^K \in \mathbb{R}^{d_{\text{model}} \times d_k}$، $W_i^V \in \mathbb{R}^{d_{\text{model}} \times d_v}$ و $W^O \in \mathbb{R}^{hd_v \times d_{\text{model}}}$.

في هذا العمل، نستخدم h = 8 طبقات انتباه متوازية، أو رؤوس. لكل من هذه نستخدم d_k = d_v = d_model/h = 64. بسبب البُعد المُخفّض لكل رأس، فإن التكلفة الحسابية الإجمالية مشابهة لتلك الخاصة بالانتباه أحادي الرأس ذي البُعد الكامل.

### 3.2.3 تطبيقات الانتباه في نموذجنا

يستخدم المحوّل الانتباه متعدد الرؤوس بثلاث طرق مختلفة:

• في طبقات "انتباه المشفّر-فك التشفير"، تأتي الاستعلامات من طبقة فك التشفير السابقة، وتأتي مفاتيح الذاكرة والقيم من إخراج المشفّر. يسمح هذا لكل موضع في فك التشفير بالانتباه إلى جميع المواضع في تسلسل الإدخال. هذا يحاكي آليات انتباه المشفّر-فك التشفير النموذجية في نماذج التسلسل إلى التسلسل مثل [38، 2، 9].

• يحتوي المشفّر على طبقات انتباه ذاتي. في طبقة الانتباه الذاتي، تأتي جميع المفاتيح والقيم والاستعلامات من نفس المكان، في هذه الحالة، إخراج الطبقة السابقة في المشفّر. يمكن لكل موضع في المشفّر الانتباه إلى جميع المواضع في الطبقة السابقة من المشفّر.

• وبالمثل، تسمح طبقات الانتباه الذاتي في فك التشفير لكل موضع في فك التشفير بالانتباه إلى جميع المواضع في فك التشفير حتى وبما في ذلك ذلك الموضع. نحتاج إلى منع تدفق المعلومات لليسار في فك التشفير للحفاظ على الخاصية الانحدارية التلقائية. ننفذ هذا داخل انتباه الجداء النقطي المقيّس عن طريق إخفاء (ضبط على −∞) جميع القيم في إدخال softmax التي تتوافق مع اتصالات غير قانونية. انظر الشكل 2.

## 3.3 الشبكات التغذية الأمامية حسب الموضع

بالإضافة إلى الطبقات الفرعية للانتباه، تحتوي كل من الطبقات في المشفّر وفك التشفير على شبكة تغذية أمامية متصلة بالكامل، يتم تطبيقها على كل موضع بشكل منفصل ومتطابق. يتكون هذا من تحويلين خطيين مع تفعيل ReLU بينهما.

$$\text{FFN}(x) = \max(0, xW_1 + b_1)W_2 + b_2 \quad (2)$$

بينما التحويلات الخطية هي نفسها عبر مواضع مختلفة، فإنها تستخدم معاملات مختلفة من طبقة إلى طبقة. طريقة أخرى لوصف هذا هي كالتفافين بحجم نواة 1. بُعد الإدخال والإخراج هو d_model = 512، والطبقة الداخلية لها بُعد d_ff = 2048.

## 3.4 التضمينات و Softmax

على غرار نماذج تحويل التسلسلات الأخرى، نستخدم تضمينات مُتعلّمة لتحويل رموز الإدخال ورموز الإخراج إلى متجهات ذات بُعد d_model. نستخدم أيضاً التحويل الخطي المُتعلّم المعتاد ودالة softmax لتحويل إخراج فك التشفير إلى احتمالات الرمز التالي المتنبأ به. في نموذجنا، نشارك نفس مصفوفة الأوزان بين طبقتي التضمين والتحويل الخطي قبل softmax، على غرار [30]. في طبقات التضمين، نضرب تلك الأوزان بـ √d_model.

## 3.5 الترميز الموضعي

نظراً لأن نموذجنا لا يحتوي على تكرار ولا التفاف، لكي يستفيد النموذج من ترتيب التسلسل، يجب أن نحقن بعض المعلومات حول الموضع النسبي أو المطلق للرموز في التسلسل. لهذه الغاية، نضيف "ترميزات موضعية" (positional encodings) إلى تضمينات الإدخال في قيعان مكدّسات المشفّر وفك التشفير. الترميزات الموضعية لها نفس البُعد d_model مثل التضمينات، بحيث يمكن جمع الاثنين. هناك العديد من الخيارات للترميزات الموضعية، المُتعلّمة والثابتة [9].

في هذا العمل، نستخدم دالتي الجيب وجيب التمام بترددات مختلفة:

$$PE_{(pos,2i)} = \sin(pos/10000^{2i/d_{\text{model}}})$$
$$PE_{(pos,2i+1)} = \cos(pos/10000^{2i/d_{\text{model}}})$$

حيث pos هو الموضع و i هو البُعد. أي أن كل بُعد من الترميز الموضعي يتوافق مع موجة جيبية. تشكّل الأطوال الموجية تقدماً هندسياً من 2π إلى 10000 · 2π. اخترنا هذه الدالة لأننا افترضنا أنها ستسمح للنموذج بتعلم الانتباه بسهولة حسب المواضع النسبية، حيث أنه لأي إزاحة ثابتة k، يمكن تمثيل PE_pos+k كدالة خطية لـ PE_pos.

جرّبنا أيضاً استخدام تضمينات موضعية مُتعلّمة [9] بدلاً من ذلك، ووجدنا أن النسختين أنتجتا نتائج متطابقة تقريباً (انظر الجدول 3 الصف (E)). اخترنا النسخة الجيبية لأنها قد تسمح للنموذج بالاستقراء إلى أطوال تسلسل أطول من تلك التي صودفت أثناء التدريب.

---

### Translation Notes

- **Figures referenced:** Figure 1 (الشكل 1), Figure 2 (الشكل 2)
- **Tables referenced:** Table 3 row (E) (الجدول 3 الصف (E))
- **Key terms introduced:**
  - Auto-regressive (انحداري تلقائي)
  - Stacked (مكدّس)
  - Point-wise (نقطي)
  - Residual connection (اتصال متبقي)
  - Layer normalization (تطبيع الطبقة)
  - Query (استعلام)
  - Key-value pairs (أزواج المفتاح-القيمة)
  - Compatibility function (دالة توافق)
  - Scaled Dot-Product Attention (انتباه الجداء النقطي المقيّس)
  - Additive attention (الانتباه الإضافي)
  - Multiplicative attention (الانتباه الجدائي)
  - Multi-head attention (الانتباه متعدد الرؤوس)
  - Representation subspaces (فضاءات فرعية للتمثيل)
  - Masking (الإخفاء)
  - Position-wise feed-forward (تغذية أمامية حسب الموضع)
  - ReLU activation (تفعيل ReLU)
  - Positional encodings (ترميزات موضعية)
  - Sinusoid (موجة جيبية)
  - Geometric progression (تقدم هندسي)

- **Equations:**
  - Equation (1): Attention function
  - Equation (2): Feed-forward network (FFN)
  - Positional encoding equations with sin/cos
  - All preserved in LaTeX format

- **Citations:** [5], [2], [35], [10], [11], [1], [38], [9], [3], [30] all preserved

- **Special handling:**
  - Mathematical notation preserved: d_model, d_k, d_v, d_ff, Q, K, V, W matrices
  - Subscripts and superscripts maintained in equations
  - Function names kept in English (softmax, LayerNorm, ReLU, Concat)
  - Greek letters preserved (π)
  - Section cross-references maintained (section 3.2)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
