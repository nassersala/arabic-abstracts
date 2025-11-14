# Section 4: Why Self-Attention
## القسم 4: لماذا الانتباه الذاتي

**Section:** why-self-attention
**Translation Quality:** 0.86
**Glossary Terms Used:** self-attention, recurrent layers, convolutional layers, computational complexity, parallelization, long-range dependencies

---

### English Version

In this section we compare various aspects of self-attention layers to the recurrent and convolutional layers commonly used for mapping one variable-length sequence of symbol representations (x₁, ..., xₙ) to another sequence of equal length (z₁, ..., zₙ), with xᵢ, zᵢ ∈ ℝᵈ, such as a hidden layer in a typical sequence transduction encoder or decoder. Motivating our use of self-attention we consider three desiderata.

One is the total computational complexity per layer. Another is the amount of computation that can be parallelized, as measured by the minimum number of sequential operations required.

The third is the path length between long-range dependencies in the network. Learning long-range dependencies is a key challenge in many sequence transduction tasks. One key factor affecting the ability to learn such dependencies is the length of the paths forward and backward signals have to traverse in the network. The shorter these paths between any combination of positions in the input and output sequences, the easier it is to learn long-range dependencies [12]. Hence we also compare the maximum path length between any two input and output positions in networks composed of the different layer types.

As noted in Table 1, a self-attention layer connects all positions with a constant number of sequentially executed operations, whereas a recurrent layer requires O(n) sequential operations. In terms of computational complexity, self-attention layers are faster than recurrent layers when the sequence length n is smaller than the representation dimensionality d, which is most often the case with sentence representations used by state-of-the-art models in machine translations, such as word-piece [38] and byte-pair [31] representations. To improve computational performance for tasks involving very long sequences, self-attention could be restricted to considering only a neighborhood of size r in the input sequence centered around the respective output position. This would increase the maximum path length to O(n/r). We plan to investigate this approach further in future work.

A single convolutional layer with kernel width k < n does not connect all pairs of input and output positions. Doing so requires a stack of O(n/k) convolutional layers in the case of contiguous kernels, or O(log_k(n)) in the case of dilated convolutions [18], increasing the length of the longest paths between any two positions in the network. Convolutional layers are generally more expensive than recurrent layers, by a factor of k. Separable convolutions [6], however, decrease the complexity considerably, to O(k · n · d + n · d²). Even with k = n, however, the complexity of a separable convolution is equal to the combination of a self-attention layer and a point-wise feed-forward layer, the approach we take in our model.

As side benefit, self-attention could yield more interpretable models. We inspect attention distributions from our models and present and discuss examples in the appendix. Not only do individual attention heads clearly learn to perform different tasks, many appear to exhibit behavior related to the syntactic and semantic structure of the sentences.

---

### النسخة العربية

في هذا القسم، نقارن جوانب مختلفة من طبقات الانتباه الذاتي بالطبقات التكرارية والالتفافية المستخدمة عادة لتعيين تسلسل متغير الطول من تمثيلات الرموز (x₁, ..., xₙ) إلى تسلسل آخر بطول متساوٍ (z₁, ..., zₙ)، مع xᵢ, zᵢ ∈ ℝᵈ، مثل طبقة مخفية في مشفّر أو فك تشفير نموذجي لتحويل التسلسلات. من خلال تحفيز استخدامنا للانتباه الذاتي، نأخذ في الاعتبار ثلاثة متطلبات مرغوبة.

أحدها هو التعقيد الحسابي الإجمالي لكل طبقة. والآخر هو مقدار الحساب الذي يمكن توازيه، كما يُقاس بالحد الأدنى لعدد العمليات التسلسلية المطلوبة.

الثالث هو طول المسار بين التبعيات بعيدة المدى في الشبكة. يُعد تعلّم التبعيات بعيدة المدى تحدياً رئيسياً في العديد من مهام تحويل التسلسلات. أحد العوامل الرئيسية التي تؤثر على القدرة على تعلّم مثل هذه التبعيات هو طول المسارات التي يجب أن تجتازها الإشارات الأمامية والخلفية في الشبكة. كلما كانت هذه المسارات أقصر بين أي مجموعة من المواضع في تسلسلات الإدخال والإخراج، كان من الأسهل تعلّم التبعيات بعيدة المدى [12]. ومن ثم، نقارن أيضاً طول المسار الأقصى بين أي موضعي إدخال وإخراج في الشبكات المكونة من أنواع الطبقات المختلفة.

كما هو مذكور في الجدول 1، تربط طبقة الانتباه الذاتي جميع المواضع بعدد ثابت من العمليات المنفذة تسلسلياً، بينما تتطلب الطبقة التكرارية عمليات تسلسلية O(n). من حيث التعقيد الحسابي، فإن طبقات الانتباه الذاتي أسرع من الطبقات التكرارية عندما يكون طول التسلسل n أصغر من بُعد التمثيل d، وهو ما يحدث في أغلب الأحيان مع تمثيلات الجمل المستخدمة بواسطة النماذج المتطورة في الترجمات الآلية، مثل تمثيلات قطع الكلمات (word-piece) [38] وأزواج البايتات (byte-pair) [31]. لتحسين الأداء الحسابي للمهام التي تتضمن تسلسلات طويلة جداً، يمكن تقييد الانتباه الذاتي للنظر فقط في حي بحجم r في تسلسل الإدخال متمركز حول موضع الإخراج المعني. سيزيد هذا من طول المسار الأقصى إلى O(n/r). نخطط لاستكشاف هذا النهج بشكل أكبر في العمل المستقبلي.

طبقة التفافية واحدة بعرض نواة k < n لا تربط جميع أزواج مواضع الإدخال والإخراج. يتطلب القيام بذلك مكدّساً من طبقات التفافية O(n/k) في حالة النوى المتجاورة، أو O(log_k(n)) في حالة الالتفافات المتوسّعة (dilated convolutions) [18]، مما يزيد من طول أطول المسارات بين أي موضعين في الشبكة. الطبقات الالتفافية أغلى عموماً من الطبقات التكرارية، بمعامل k. ومع ذلك، فإن الالتفافات القابلة للفصل (separable convolutions) [6] تقلل التعقيد بشكل كبير، إلى O(k · n · d + n · d²). حتى مع k = n، مع ذلك، فإن تعقيد الالتفاف القابل للفصل يساوي مجموع طبقة انتباه ذاتي وطبقة تغذية أمامية نقطية، النهج الذي نتبعه في نموذجنا.

كميزة جانبية، يمكن للانتباه الذاتي أن يُنتج نماذج أكثر قابلية للتفسير. نفحص توزيعات الانتباه من نماذجنا ونقدم ونناقش أمثلة في الملحق. لا تتعلم رؤوس الانتباه الفردية بوضوح أداء مهام مختلفة فحسب، بل يبدو أن الكثير منها يُظهر سلوكاً مرتبطاً بالبنية النحوية والدلالية للجمل.

---

### Translation Notes

- **Figures referenced:** None
- **Tables referenced:** Table 1 (الجدول 1)
- **Key terms introduced:**
  - Variable-length sequence (تسلسل متغير الطول)
  - Desiderata (متطلبات مرغوبة)
  - Computational complexity (التعقيد الحسابي)
  - Parallelization (التوازي)
  - Sequential operations (العمليات التسلسلية)
  - Long-range dependencies (التبعيات بعيدة المدى)
  - Path length (طول المسار)
  - Forward and backward signals (الإشارات الأمامية والخلفية)
  - Word-piece (قطع الكلمات)
  - Byte-pair (أزواج البايتات)
  - Neighborhood (حي)
  - Kernel width (عرض النواة)
  - Contiguous kernels (النوى المتجاورة)
  - Dilated convolutions (الالتفافات المتوسّعة)
  - Separable convolutions (الالتفافات القابلة للفصل)
  - Interpretable models (نماذج قابلة للتفسير)
  - Attention distributions (توزيعات الانتباه)
  - Syntactic and semantic structure (البنية النحوية والدلالية)

- **Equations:** Big-O notation preserved: O(n), O(n/k), O(log_k(n)), O(k · n · d + n · d²), O(n/r)
- **Citations:** [12], [38], [31], [18], [6] all preserved
- **Special handling:**
  - Mathematical notation preserved: xᵢ, zᵢ ∈ ℝᵈ
  - Variable names kept as in original: n, d, k, r
  - Appendix reference maintained
  - Big-O notation explained naturally in Arabic

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
