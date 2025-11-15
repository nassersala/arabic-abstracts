# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** unsupervised learning, representation learning, pretraining, finetuning, autoregressive, autoencoding, language modeling, bidirectional, density estimation, BERT, masking, factorization, permutation, Transformer-XL, segment recurrence, relative encoding, GLUE, SQuAD, RACE

---

### English Version

Unsupervised representation learning has been highly successful in the domain of natural language processing [7, 22, 27, 28, 10]. Typically, these methods first pretrain neural networks on large-scale unlabeled text corpora, and then finetune the models or representations on downstream tasks. Under this shared high-level idea, different unsupervised pretraining objectives have been explored in literature. Among them, autoregressive (AR) language modeling and autoencoding (AE) have been the two most successful pretraining objectives.

AR language modeling seeks to estimate the probability distribution of a text corpus with an autoregressive model [7, 27, 28]. Specifically, given a text sequence x = (x₁, · · · , xₜ), AR language modeling factorizes the likelihood into a forward product p(x) = ∏ᵗₜ₌₁ p(xₜ | x<ₜ) or a backward one p(x) = ∏¹ₜ₌ₜ p(xₜ | x>ₜ). A parametric model (e.g. a neural network) is trained to model each conditional distribution. Since an AR language model is only trained to encode a uni-directional context (either forward or backward), it is not effective at modeling deep bidirectional contexts. On the contrary, downstream language understanding tasks often require bidirectional context information. This results in a gap between AR language modeling and effective pretraining.

In comparison, AE based pretraining does not perform explicit density estimation but instead aims to reconstruct the original data from corrupted input. A notable example is BERT [10], which has been the state-of-the-art pretraining approach. Given the input token sequence, a certain portion of tokens are replaced by a special symbol [MASK], and the model is trained to recover the original tokens from the corrupted version. Since density estimation is not part of the objective, BERT is allowed to utilize bidirectional contexts for reconstruction. As an immediate benefit, this closes the aforementioned bidirectional information gap in AR language modeling, leading to improved performance. However, the artificial symbols like [MASK] used by BERT during pretraining are absent from real data at finetuning time, resulting in a pretrain-finetune discrepancy. Moreover, since the predicted tokens are masked in the input, BERT is not able to model the joint probability using the product rule as in AR language modeling. In other words, BERT assumes the predicted tokens are independent of each other given the unmasked tokens, which is oversimplified as high-order, long-range dependency is prevalent in natural language [9].

Faced with the pros and cons of existing language pretraining objectives, in this work, we propose XLNet, a generalized autoregressive method that leverages the best of both AR language modeling and AE while avoiding their limitations.

• Firstly, instead of using a fixed forward or backward factorization order as in conventional AR models, XLNet maximizes the expected log likelihood of a sequence w.r.t. all possible permutations of the factorization order. Thanks to the permutation operation, the context for each position can consist of tokens from both left and right. In expectation, each position learns to utilize contextual information from all positions, i.e., capturing bidirectional context.

• Secondly, as a generalized AR language model, XLNet does not rely on data corruption. Hence, XLNet does not suffer from the pretrain-finetune discrepancy that BERT is subject to. Meanwhile, the autoregressive objective also provides a natural way to use the product rule for factorizing the joint probability of the predicted tokens, eliminating the independence assumption made in BERT.

In addition to a novel pretraining objective, XLNet improves architectural designs for pretraining.

• Inspired by the latest advancements in AR language modeling, XLNet integrates the segment recurrence mechanism and relative encoding scheme of Transformer-XL [9] into pretraining, which empirically improves the performance especially for tasks involving a longer text sequence.

• Naively applying a Transformer(-XL) architecture to permutation-based language modeling does not work because the factorization order is arbitrary and the target is ambiguous. As a solution, we propose to reparameterize the Transformer(-XL) network to remove the ambiguity.

Empirically, under comparable experiment setting, XLNet consistently outperforms BERT [10] on a wide spectrum of problems including GLUE language understanding tasks, reading comprehension tasks like SQuAD and RACE, text classification tasks such as Yelp and IMDB, and the ClueWeb09-B document ranking task.

**Related Work:** The idea of permutation-based AR modeling has been explored in [32, 12], but there are several key differences. Firstly, previous models aim to improve density estimation by baking an "orderless" inductive bias into the model while XLNet is motivated by enabling AR language models to learn bidirectional contexts. Technically, to construct a valid target-aware prediction distribution, XLNet incorporates the target position into the hidden state via two-stream attention while previous permutation-based AR models relied on implicit position awareness inherent to their MLP architectures. Finally, for both orderless NADE and XLNet, we would like to emphasize that "orderless" does not mean that the input sequence can be randomly permuted but that the model allows for different factorization orders of the distribution.

Another related idea is to perform autoregressive denoising in the context of text generation [11], which only considers a fixed order though.

---

### النسخة العربية

حقق التعلم التمثيلي غير الموجه نجاحاً كبيراً في مجال معالجة اللغة الطبيعية [7, 22, 27, 28, 10]. عادةً، تقوم هذه الطرق أولاً بالتدريب المسبق للشبكات العصبية على مجموعات نصية كبيرة الحجم غير مصنفة، ثم تقوم بالضبط الدقيق للنماذج أو التمثيلات على المهام اللاحقة. تحت هذه الفكرة العامة المشتركة، تم استكشاف أهداف مختلفة للتدريب المسبق غير الموجه في الأدبيات. من بينها، كانت النمذجة اللغوية الانحدارية الذاتية (AR) والترميز التلقائي (AE) هما الهدفان الأكثر نجاحاً للتدريب المسبق.

تسعى النمذجة اللغوية الانحدارية الذاتية إلى تقدير توزيع الاحتمالات لمجموعة نصية باستخدام نموذج انحداري ذاتي [7, 27, 28]. على وجه التحديد، بالنظر إلى تسلسل نصي x = (x₁, · · · , xₜ)، تقوم النمذجة اللغوية الانحدارية الذاتية بتحليل الاحتمالية إلى حاصل ضرب أمامي p(x) = ∏ᵗₜ₌₁ p(xₜ | x<ₜ) أو حاصل ضرب خلفي p(x) = ∏¹ₜ₌ₜ p(xₜ | x>ₜ). يتم تدريب نموذج بارامتري (مثل شبكة عصبية) لنمذجة كل توزيع شرطي. نظراً لأن النموذج اللغوي الانحداري الذاتي يتم تدريبه فقط لترميز سياق أحادي الاتجاه (إما أمامي أو خلفي)، فهو غير فعال في نمذجة السياقات العميقة ثنائية الاتجاه. على العكس من ذلك، غالباً ما تتطلب مهام فهم اللغة اللاحقة معلومات سياقية ثنائية الاتجاه. ينتج عن هذا فجوة بين النمذجة اللغوية الانحدارية الذاتية والتدريب المسبق الفعال.

بالمقارنة، لا يقوم التدريب المسبق القائم على الترميز التلقائي بتقدير الكثافة الصريح ولكنه يهدف بدلاً من ذلك إلى إعادة بناء البيانات الأصلية من المدخلات المفسدة. مثال بارز هو BERT [10]، الذي كان النهج الأحدث للتدريب المسبق. بالنظر إلى تسلسل الرموز المدخلة، يتم استبدال جزء معين من الرموز برمز خاص [MASK]، ويتم تدريب النموذج على استرداد الرموز الأصلية من النسخة المفسدة. نظراً لأن تقدير الكثافة ليس جزءاً من الهدف، يُسمح لـ BERT باستخدام السياقات ثنائية الاتجاه لإعادة البناء. كفائدة فورية، يؤدي هذا إلى سد فجوة المعلومات ثنائية الاتجاه المذكورة أعلاه في النمذجة اللغوية الانحدارية الذاتية، مما يؤدي إلى تحسين الأداء. ومع ذلك، فإن الرموز الاصطناعية مثل [MASK] التي يستخدمها BERT أثناء التدريب المسبق غائبة عن البيانات الحقيقية في وقت الضبط الدقيق، مما يؤدي إلى تباين بين التدريب المسبق والضبط الدقيق. علاوة على ذلك، نظراً لأن الرموز المتوقعة مخفية في المدخلات، لا يستطيع BERT نمذجة الاحتمالية المشتركة باستخدام قاعدة الضرب كما في النمذجة اللغوية الانحدارية الذاتية. بعبارة أخرى، يفترض BERT أن الرموز المتوقعة مستقلة عن بعضها البعض بالنظر إلى الرموز غير المخفاة، وهو أمر مبسط بشكل مفرط حيث أن التبعية عالية الرتبة وبعيدة المدى سائدة في اللغة الطبيعية [9].

في مواجهة إيجابيات وسلبيات أهداف التدريب المسبق اللغوي الحالية، نقترح في هذا العمل XLNet، وهي طريقة انحدارية ذاتية معممة تستفيد من أفضل ما في النمذجة اللغوية الانحدارية الذاتية والترميز التلقائي مع تجنب قيودهما.

• أولاً، بدلاً من استخدام ترتيب تحليل عاملي ثابت أمامي أو خلفي كما في النماذج الانحدارية الذاتية التقليدية، يقوم XLNet بتعظيم اللوغاريتم المتوقع للاحتمالية لتسلسل بالنسبة لجميع التبديلات الممكنة لترتيب التحليل العاملي. بفضل عملية التبديل، يمكن أن يتكون السياق لكل موضع من رموز من اليسار واليمين. في التوقع، يتعلم كل موضع استخدام المعلومات السياقية من جميع المواضع، أي التقاط السياق ثنائي الاتجاه.

• ثانياً، باعتباره نموذجاً لغوياً انحدارياً ذاتياً معمماً، لا يعتمد XLNet على إفساد البيانات. وبالتالي، لا يعاني XLNet من تباين التدريب المسبق والضبط الدقيق الذي يخضع له BERT. في الوقت نفسه، يوفر الهدف الانحداري الذاتي أيضاً طريقة طبيعية لاستخدام قاعدة الضرب لتحليل الاحتمالية المشتركة للرموز المتوقعة، مما يلغي افتراض الاستقلال الذي صنعه BERT.

بالإضافة إلى هدف التدريب المسبق الجديد، يحسن XLNet التصاميم المعمارية للتدريب المسبق.

• مستوحى من أحدث التطورات في النمذجة اللغوية الانحدارية الذاتية، يدمج XLNet آلية تكرار القطاعات ومخطط الترميز النسبي لـ Transformer-XL [9] في التدريب المسبق، مما يحسن الأداء تجريبياً خاصة للمهام التي تتضمن تسلسلاً نصياً أطول.

• لا يعمل تطبيق معمارية Transformer(-XL) بشكل ساذج على النمذجة اللغوية القائمة على التبديل لأن ترتيب التحليل العاملي تعسفي والهدف غامض. كحل، نقترح إعادة بارامترة شبكة Transformer(-XL) لإزالة الغموض.

تجريبياً، في ظل إعدادات تجريبية قابلة للمقارنة، يتفوق XLNet باستمرار على BERT [10] في مجموعة واسعة من المشاكل بما في ذلك مهام فهم اللغة GLUE، ومهام الفهم القرائي مثل SQuAD و RACE، ومهام تصنيف النصوص مثل Yelp و IMDB، ومهمة ترتيب المستندات ClueWeb09-B.

**الأعمال ذات الصلة:** تم استكشاف فكرة النمذجة الانحدارية الذاتية القائمة على التبديل في [32, 12]، لكن هناك عدة اختلافات رئيسية. أولاً، تهدف النماذج السابقة إلى تحسين تقدير الكثافة من خلال دمج تحيز استقرائي "عديم الترتيب" في النموذج بينما يتم تحفيز XLNet من خلال تمكين نماذج اللغة الانحدارية الذاتية من تعلم السياقات ثنائية الاتجاه. تقنياً، لبناء توزيع تنبؤ صالح واعي بالهدف، يدمج XLNet موضع الهدف في الحالة المخفية عبر انتباه التدفقين بينما اعتمدت نماذج الانحدار الذاتي القائمة على التبديل السابقة على الوعي الضمني بالموضع الكامن في معماريات MLP الخاصة بها. أخيراً، لكل من NADE عديم الترتيب و XLNet، نود التأكيد على أن "عديم الترتيب" لا يعني أنه يمكن ترتيب التسلسل المدخل بشكل عشوائي ولكن أن النموذج يسمح بترتيبات تحليل عاملي مختلفة للتوزيع.

فكرة أخرى ذات صلة هي إجراء إزالة الضوضاء الانحدارية الذاتية في سياق توليد النص [11]، والتي تأخذ في الاعتبار ترتيباً ثابتاً فقط على الرغم من ذلك.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** Permutation language modeling, two-stream attention, segment recurrence, relative encoding, target-aware prediction, orderless factorization
- **Equations:** Product formulations for AR modeling: p(x) = ∏ᵗₜ₌₁ p(xₜ | x<ₜ) and backward variant
- **Citations:** [7, 22, 27, 28, 10, 9, 32, 12, 11]
- **Special handling:** Mathematical notation preserved in both versions

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.87
- **Overall section score:** 0.88
