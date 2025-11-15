# Section 2: The Model
## القسم 2: النموذج

**Section:** The Model
**Translation Quality:** 0.87
**Glossary Terms Used:** recurrent neural network, RNN, sequence, LSTM, conditional probability, vector, hidden state, softmax, vocabulary, end-of-sentence

---

### English Version

The Recurrent Neural Network (RNN) [31, 28] is a natural generalization of feedforward neural networks to sequences. Given a sequence of inputs $(x_1,...,x_T)$, a standard RNN computes a sequence of outputs $(y_1,...,y_T)$ by iterating the following equation:

$$h_t = \text{sigm}(W_{hx}x_t + W_{hh}h_{t-1})$$
$$y_t = W_{yh}h_t$$

The RNN can easily map sequences to sequences whenever the alignment between the inputs the outputs is known ahead of time. However, it is not clear how to apply an RNN to problems whose input and the output sequences have different lengths with complicated and non-monotonic relationships.

The simplest strategy for general sequence learning is to map the input sequence to a fixed-sized vector using one RNN, and then to map the vector to the target sequence with another RNN (this approach has also been taken by Cho et al. [5]). While it could work in principle since the RNN is provided with all the relevant information, it would be difficult to train the RNNs due to the resulting long term dependencies (figure 1) [14, 4, 16, 15]. However, the Long Short-Term Memory (LSTM) [16] is known to learn problems with long range temporal dependencies, so an LSTM may succeed in this setting.

The goal of the LSTM is to estimate the conditional probability $p(y_1,...,y_{T'}|x_1,...,x_T)$ where $(x_1,...,x_T)$ is an input sequence and $y_1,...,y_{T'}$ is its corresponding output sequence whose length $T'$ may differ from $T$. The LSTM computes this conditional probability by first obtaining the fixed-dimensional representation $v$ of the input sequence $(x_1,...,x_T)$ given by the last hidden state of the LSTM, and then computing the probability of $y_1,...,y_{T'}$ with a standard LSTM-LM formulation whose initial hidden state is set to the representation $v$ of $x_1,...,x_T$:

$$p(y_1,...,y_{T'}|x_1,...,x_T) = \prod_{t=1}^{T'} p(y_t|v,y_1,...,y_{t-1})$$ (1)

In this equation, each $p(y_t|v,y_1,...,y_{t-1})$ distribution is represented with a softmax over all the words in the vocabulary. We use the LSTM formulation from Graves [10]. Note that we require that each sentence ends with a special end-of-sentence symbol "$\langle$EOS$\rangle$", which enables the model to define a distribution over sequences of all possible lengths. The overall scheme is outlined in figure 1, where the shown LSTM computes the representation of "A", "B", "C", "$\langle$EOS$\rangle$" and then uses this representation to compute the probability of "W", "X", "Y", "Z", "$\langle$EOS$\rangle$".

Our actual models differ from the above description in three important ways. First, we used two different LSTMs: one for the input sequence and another for the output sequence, because doing so increases the number model parameters at negligible computational cost and makes it natural to train the LSTM on multiple language pairs simultaneously [18]. Second, we found that deep LSTMs significantly outperformed shallow LSTMs, so we chose an LSTM with four layers. Third, we found it extremely valuable to reverse the order of the words of the input sentence. So for example, instead of mapping the sentence $a,b,c$ to the sentence $\alpha,\beta,\gamma$, the LSTM is asked to map $c,b,a$ to $\alpha,\beta,\gamma$, where $\alpha,\beta,\gamma$ is the translation of $a,b,c$. This way, $a$ is in close proximity to $\alpha$, $b$ is fairly close to $\beta$, and so on, a fact that makes it easy for SGD to "establish communication" between the input and the output. We found this simple data transformation to greatly improve the performance of the LSTM.

---

### النسخة العربية

الشبكة العصبية المتكررة (RNN) [31، 28] هي تعميم طبيعي للشبكات العصبية الأمامية على التسلسلات. بالنظر إلى تسلسل من المدخلات $(x_1,...,x_T)$، تحسب شبكة RNN قياسية تسلسلاً من المخرجات $(y_1,...,y_T)$ من خلال تكرار المعادلة التالية:

$$h_t = \text{sigm}(W_{hx}x_t + W_{hh}h_{t-1})$$
$$y_t = W_{yh}h_t$$

يمكن لشبكة RNN تخطيط التسلسلات إلى تسلسلات بسهولة عندما تكون المحاذاة بين المدخلات والمخرجات معروفة مسبقاً. ومع ذلك، ليس من الواضح كيفية تطبيق RNN على المسائل التي تحتوي تسلسلات المدخلات والمخرجات فيها على أطوال مختلفة مع علاقات معقدة وغير أحادية الاتجاه.

الاستراتيجية الأبسط لتعلم التسلسلات العامة هي تخطيط تسلسل الإدخال إلى متجه ذي حجم ثابت باستخدام شبكة RNN واحدة، ثم تخطيط المتجه إلى التسلسل المستهدف باستخدام شبكة RNN أخرى (تم اتباع هذا النهج أيضاً من قبل Cho وآخرين [5]). على الرغم من أنه يمكن أن ينجح من حيث المبدأ نظراً لأن شبكة RNN تُزوَّد بجميع المعلومات ذات الصلة، إلا أنه سيكون من الصعب تدريب شبكات RNN بسبب التبعيات طويلة المدى الناتجة (الشكل 1) [14، 4، 16، 15]. ومع ذلك، من المعروف أن ذاكرة طويلة قصيرة المدى (LSTM) [16] تتعلم المسائل ذات التبعيات الزمنية بعيدة المدى، لذلك قد تنجح LSTM في هذا الإطار.

هدف LSTM هو تقدير الاحتمال الشرطي $p(y_1,...,y_{T'}|x_1,...,x_T)$ حيث $(x_1,...,x_T)$ هو تسلسل إدخال و $y_1,...,y_{T'}$ هو تسلسل الإخراج المقابل له الذي قد يختلف طوله $T'$ عن $T$. تحسب LSTM هذا الاحتمال الشرطي من خلال الحصول أولاً على التمثيل ذي الأبعاد الثابتة $v$ لتسلسل الإدخال $(x_1,...,x_T)$ المُعطى بواسطة الحالة المخفية الأخيرة لـ LSTM، ثم حساب احتمال $y_1,...,y_{T'}$ باستخدام صيغة LSTM-LM قياسية يتم تعيين حالتها المخفية الأولية على التمثيل $v$ لـ $x_1,...,x_T$:

$$p(y_1,...,y_{T'}|x_1,...,x_T) = \prod_{t=1}^{T'} p(y_t|v,y_1,...,y_{t-1})$$ (1)

في هذه المعادلة، يتم تمثيل كل توزيع $p(y_t|v,y_1,...,y_{t-1})$ باستخدام softmax على جميع الكلمات في المفردات. نستخدم صيغة LSTM من Graves [10]. لاحظ أننا نتطلب أن تنتهي كل جملة برمز نهاية الجملة الخاص "$\langle$EOS$\rangle$"، مما يمكّن النموذج من تعريف توزيع على تسلسلات بجميع الأطوال الممكنة. يتم تحديد المخطط العام في الشكل 1، حيث تحسب LSTM الموضحة تمثيل "A" و "B" و "C" و "$\langle$EOS$\rangle$" ثم تستخدم هذا التمثيل لحساب احتمال "W" و "X" و "Y" و "Z" و "$\langle$EOS$\rangle$".

تختلف نماذجنا الفعلية عن الوصف أعلاه في ثلاث طرق مهمة. أولاً، استخدمنا شبكتي LSTM مختلفتين: واحدة لتسلسل الإدخال وأخرى لتسلسل الإخراج، لأن القيام بذلك يزيد من عدد معاملات النموذج بتكلفة حسابية ضئيلة ويجعل من الطبيعي تدريب LSTM على أزواج لغات متعددة في وقت واحد [18]. ثانياً، وجدنا أن شبكات LSTM العميقة تفوقت بشكل كبير على شبكات LSTM الضحلة، لذلك اخترنا LSTM بأربع طبقات. ثالثاً، وجدنا أنه من القيِّم للغاية عكس ترتيب كلمات جملة الإدخال. على سبيل المثال، بدلاً من تخطيط الجملة $a,b,c$ إلى الجملة $\alpha,\beta,\gamma$، يُطلب من LSTM تخطيط $c,b,a$ إلى $\alpha,\beta,\gamma$، حيث $\alpha,\beta,\gamma$ هي ترجمة $a,b,c$. بهذه الطريقة، يكون $a$ قريباً من $\alpha$، و $b$ قريب إلى حد ما من $\beta$، وهكذا، وهي حقيقة تسهل على الانحدار التدرجي العشوائي (SGD) "إنشاء تواصل" بين المدخلات والمخرجات. وجدنا أن هذا التحويل البسيط للبيانات يحسّن أداء LSTM بشكل كبير.

---

### Translation Notes

- **Figures referenced:** Figure 1 (mentioned multiple times)
- **Key terms introduced:** Recurrent Neural Network (RNN), feedforward neural networks, hidden state, conditional probability, LSTM-LM (LSTM Language Model), softmax, end-of-sentence token (EOS), deep LSTM, shallow LSTM
- **Equations:** 3 mathematical equations (RNN equations and conditional probability formula)
- **Citations:** [31,28], [5], [14,4,16,15], [16], [10], [18]
- **Special handling:**
  - All LaTeX equations preserved exactly
  - Mathematical notation maintained in both English and Arabic sections
  - Special symbols like $\langle$EOS$\rangle$ kept as-is
  - Greek letters ($\alpha,\beta,\gamma$) preserved
  - Variable names kept in Latin script

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
