# Section 2.4: Incorporating Ideas from Transformer-XL
## القسم 2.4: دمج أفكار من Transformer-XL

**Section:** transformer-xl-integration
**Translation Quality:** 0.86
**Glossary Terms Used:** autoregressive, Transformer-XL, relative positional encoding, segment recurrence, hidden states, memory, attention, factorization order, query stream, content stream

---

### English Version

Since our objective function fits in the AR framework, we incorporate the state-of-the-art AR language model, Transformer-XL [9], into our pretraining framework, and name our method after it. We integrate two important techniques in Transformer-XL, namely the relative positional encoding scheme and the segment recurrence mechanism. We apply relative positional encodings based on the original sequence as discussed earlier, which is straightforward. Now we discuss how to integrate the recurrence mechanism into the proposed permutation setting and enable the model to reuse hidden states from previous segments.

Without loss of generality, suppose we have two segments taken from a long sequence $s$; i.e., $\tilde{x} = s_{1:T}$ and $x = s_{T+1:2T}$. Let $\tilde{z}$ and $z$ be permutations of $[1 \cdots T]$ and $[T+1 \cdots 2T]$ respectively. Then, based on the permutation $\tilde{z}$, we process the first segment, and then cache the obtained content representations $\tilde{h}^{(m)}$ for each layer $m$. Then, for the next segment $x$, the attention update with memory can be written as:

$$h_{z_t}^{(m)} \leftarrow \text{Attention}(Q = h_{z_t}^{(m-1)}, KV = [\tilde{h}^{(m-1)}, h_{z_{\leq t}}^{(m-1)}]; \theta)$$

where $[., .]$ denotes concatenation along the sequence dimension. Notice that positional encodings only depend on the actual positions in the original sequence. Thus, the above attention update is independent of $\tilde{z}$ once the representations $\tilde{h}^{(m)}$ are obtained. This allows caching and reusing the memory without knowing the factorization order of the previous segment. In expectation, the model learns to utilize the memory over all factorization orders of the last segment. The query stream can be computed in the same way. Finally, Figure 1 (c) presents an overview of the proposed permutation language modeling with two-stream attention (see Appendix A.7 for more detailed illustration).

---

### النسخة العربية

نظراً لأن دالة الهدف الخاصة بنا تتناسب مع إطار الانحدار الذاتي، فإننا ندمج نموذج اللغة الانحداري الذاتي الأحدث، Transformer-XL [9]، في إطار التدريب المسبق الخاص بنا، ونسمي طريقتنا باسمه. ندمج تقنيتين مهمتين في Transformer-XL، وهما مخطط الترميز الموضعي النسبي وآلية تكرار القطاعات. نطبق الترميزات الموضعية النسبية بناءً على التسلسل الأصلي كما تمت مناقشته سابقاً، وهو أمر واضح ومباشر. الآن نناقش كيفية دمج آلية التكرار في إعداد التبديل المقترح وتمكين النموذج من إعادة استخدام الحالات المخفية من القطاعات السابقة.

دون فقدان العمومية، افترض أن لدينا قطاعين مأخوذين من تسلسل طويل $s$؛ أي $\tilde{x} = s_{1:T}$ و $x = s_{T+1:2T}$. دع $\tilde{z}$ و $z$ تكونان تبديلات لـ $[1 \cdots T]$ و $[T+1 \cdots 2T]$ على التوالي. بعد ذلك، بناءً على التبديل $\tilde{z}$، نعالج القطاع الأول، ثم نخزن مؤقتاً تمثيلات المحتوى المحصلة $\tilde{h}^{(m)}$ لكل طبقة $m$. بعد ذلك، بالنسبة للقطاع التالي $x$، يمكن كتابة تحديث الانتباه مع الذاكرة على النحو التالي:

$$h_{z_t}^{(m)} \leftarrow \text{Attention}(Q = h_{z_t}^{(m-1)}, KV = [\tilde{h}^{(m-1)}, h_{z_{\leq t}}^{(m-1)}]; \theta)$$

حيث $[., .]$ يشير إلى التسلسل على طول بُعد التسلسل. لاحظ أن الترميزات الموضعية تعتمد فقط على المواضع الفعلية في التسلسل الأصلي. وبالتالي، فإن تحديث الانتباه أعلاه مستقل عن $\tilde{z}$ بمجرد الحصول على التمثيلات $\tilde{h}^{(m)}$. يسمح هذا بالتخزين المؤقت وإعادة استخدام الذاكرة دون معرفة ترتيب التحليل العاملي للقطاع السابق. في التوقع، يتعلم النموذج استخدام الذاكرة على جميع ترتيبات التحليل العاملي للقطاع الأخير. يمكن حساب تدفق الاستعلام بنفس الطريقة. أخيراً، يقدم الشكل 1 (ج) نظرة عامة على النمذجة اللغوية بالتبديل المقترحة مع الانتباه ثنائي التدفق (انظر الملحق A.7 للحصول على توضيح أكثر تفصيلاً).

---

### Translation Notes

- **Figures referenced:** Figure 1 (c) - overview of permutation LM with two-stream attention
- **Key terms introduced:** Segment recurrence, memory caching, concatenation along sequence dimension
- **Equations:** Memory-augmented attention update equation
- **Citations:** [9] for Transformer-XL
- **Special handling:** Mathematical notation for segments and permutations

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86
