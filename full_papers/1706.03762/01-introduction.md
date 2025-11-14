# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** recurrent neural networks, long short-term memory (LSTM), gated recurrent, sequence modeling, machine translation, encoder-decoder, attention mechanism, parallelization

---

### English Version

Recurrent neural networks, long short-term memory [13] and gated recurrent [7] neural networks in particular, have been firmly established as state of the art approaches in sequence modeling and transduction problems such as language modeling and machine translation [35, 2, 5]. Numerous efforts have since continued to push the boundaries of recurrent language models and encoder-decoder architectures [38, 24, 15].

Recurrent models typically factor computation along the symbol positions of the input and output sequences. Aligning the positions to steps in computation time, they generate a sequence of hidden states h_t, as a function of the previous hidden state h_{t-1} and the input for position t. This inherently sequential nature precludes parallelization within training examples, which becomes critical at longer sequence lengths, as memory constraints limit batching across examples. Recent work has achieved significant improvements in computational efficiency through factorization tricks [21] and conditional computation [32], while also improving model performance in case of the latter. The fundamental constraint of sequential computation, however, remains.

Attention mechanisms have become an integral part of compelling sequence modeling and transduction models in various tasks, allowing modeling of dependencies without regard to their distance in the input or output sequences [2, 19]. In all but a few cases [27], however, such attention mechanisms are used in conjunction with a recurrent network.

In this work we propose the Transformer, a model architecture eschewing recurrence and instead relying entirely on an attention mechanism to draw global dependencies between input and output. The Transformer allows for significantly more parallelization and can reach a new state of the art in translation quality after being trained for as little as twelve hours on eight P100 GPUs.

---

### النسخة العربية

لقد تم ترسيخ الشبكات العصبية التكرارية (Recurrent Neural Networks)، ولا سيما الذاكرة القصيرة طويلة المدى [13] (LSTM) والشبكات العصبية التكرارية المسوّرة [7] (Gated Recurrent)، بقوة كمناهج متطورة في نمذجة التسلسلات ومسائل التحويل مثل نمذجة اللغة والترجمة الآلية [35، 2، 5]. واستمرت جهود عديدة منذ ذلك الحين في دفع حدود نماذج اللغة التكرارية ومعماريات المشفّر-فك التشفير [38، 24، 15].

تُجزّئ النماذج التكرارية عادةً الحسابات على طول مواضع الرموز في تسلسلات الإدخال والإخراج. من خلال مواءمة المواضع مع خطوات الوقت الحسابي، تولّد تسلسلاً من الحالات المخفية h_t، كدالة للحالة المخفية السابقة h_{t-1} والإدخال للموضع t. هذه الطبيعة التسلسلية المتأصلة تمنع التوازي ضمن أمثلة التدريب، مما يصبح حرجاً عند أطوال التسلسلات الأطول، حيث تحد قيود الذاكرة من التجميع عبر الأمثلة. حققت أعمال حديثة تحسينات كبيرة في الكفاءة الحسابية من خلال حيل التحليل العاملي [21] والحساب المشروط [32]، مع تحسين أداء النموذج أيضاً في حالة الأخير. ومع ذلك، يبقى القيد الأساسي للحساب التسلسلي.

أصبحت آليات الانتباه جزءاً لا يتجزأ من نماذج نمذجة وتحويل التسلسلات المقنعة في مهام مختلفة، مما يتيح نمذجة التبعيات دون اعتبار لمسافتها في تسلسلات الإدخال أو الإخراج [2، 19]. ومع ذلك، في كل الحالات باستثناء عدد قليل [27]، تُستخدم آليات الانتباه هذه بالاقتران مع شبكة تكرارية.

في هذا العمل، نقترح المحوّل (Transformer)، وهو معمارية نموذج تتجنب التكرار وتعتمد بدلاً من ذلك بالكامل على آلية انتباه لاستخلاص التبعيات الشاملة بين الإدخال والإخراج. يسمح المحوّل بقدر أكبر بكثير من التوازي ويمكنه الوصول إلى حالة متطورة جديدة في جودة الترجمة بعد التدريب لمدة لا تقل عن اثنتي عشرة ساعة فقط على ثمانية GPUs من طراز P100.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Recurrent neural networks (الشبكات العصبية التكرارية)
  - LSTM - Long Short-Term Memory (الذاكرة القصيرة طويلة المدى)
  - Gated Recurrent Networks (الشبكات العصبية التكرارية المسوّرة)
  - Sequence modeling (نمذجة التسلسلات)
  - Transduction (التحويل)
  - Hidden states (الحالات المخفية)
  - Factorization (التحليل العاملي)
  - Conditional computation (الحساب المشروط)
  - Global dependencies (التبعيات الشاملة)
- **Equations:** Mathematical notation h_t, h_{t-1} preserved
- **Citations:** [13], [7], [35], [2], [5], [38], [24], [15], [21], [32], [19], [27] all preserved
- **Special handling:** GPU model "P100" kept in English, citation numbers preserved in square brackets

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
