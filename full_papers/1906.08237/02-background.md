# Section 2.1: Background
## القسم 2.1: الخلفية

**Section:** background
**Translation Quality:** 0.87
**Glossary Terms Used:** autoregressive, language modeling, pretraining, BERT, denoising autoencoding, factorization, context representation, embedding, Transformer, masking, independence assumption, pretrain-finetune discrepancy, bidirectional context

---

### English Version

In this section, we first review and compare the conventional AR language modeling and BERT for language pretraining. Given a text sequence x = [x₁, · · · , xₜ], AR language modeling performs pretraining by maximizing the likelihood under the forward autoregressive factorization:

$$\max_{\theta} \log p_{\theta}(x) = \sum_{t=1}^{T} \log p_{\theta}(x_t | x_{<t}) = \sum_{t=1}^{T} \log \frac{\exp(h_{\theta}(x_{1:t-1})^{\top} e(x_t))}{\sum_{x'} \exp(h_{\theta}(x_{1:t-1})^{\top} e(x'))}$$  (1)

where $h_{\theta}(x_{1:t-1})$ is a context representation produced by neural models, such as RNNs or Transformers, and $e(x)$ denotes the embedding of $x$. In comparison, BERT is based on denoising auto-encoding. Specifically, for a text sequence $x$, BERT first constructs a corrupted version $\hat{x}$ by randomly setting a portion (e.g. 15%) of tokens in $x$ to a special symbol [MASK]. Let the masked tokens be $\bar{x}$. The training objective is to reconstruct $\bar{x}$ from $\hat{x}$:

$$\max_{\theta} \log p_{\theta}(\bar{x} | \hat{x}) \approx \sum_{t=1}^{T} m_t \log p_{\theta}(x_t | \hat{x}) = \sum_{t=1}^{T} m_t \log \frac{\exp(H_{\theta}(\hat{x})_t^{\top} e(x_t))}{\sum_{x'} \exp(H_{\theta}(\hat{x})_t^{\top} e(x'))}$$  (2)

where $m_t = 1$ indicates $x_t$ is masked, and $H_{\theta}$ is a Transformer that maps a length-T text sequence $x$ into a sequence of hidden vectors $H_{\theta}(x) = [H_{\theta}(x)_1, H_{\theta}(x)_2, \cdots, H_{\theta}(x)_T]$. The pros and cons of the two pretraining objectives are compared in the following aspects:

• **Independence Assumption:** As emphasized by the ≈ sign in Eq. (2), BERT factorizes the joint conditional probability $p(\bar{x} | \hat{x})$ based on an independence assumption that all masked tokens $\bar{x}$ are separately reconstructed. In comparison, the AR language modeling objective (1) factorizes $p_{\theta}(x)$ using the product rule that holds universally without such an independence assumption.

• **Input noise:** The input to BERT contains artificial symbols like [MASK] that never occur in downstream tasks, which creates a pretrain-finetune discrepancy. Replacing [MASK] with original tokens as in [10] does not solve the problem because original tokens can be only used with a small probability — otherwise Eq. (2) will be trivial to optimize. In comparison, AR language modeling does not rely on any input corruption and does not suffer from this issue.

• **Context dependency:** The AR representation $h_{\theta}(x_{1:t-1})$ is only conditioned on the tokens up to position $t$ (i.e. tokens to the left), while the BERT representation $H_{\theta}(x)_t$ has access to the contextual information on both sides. As a result, the BERT objective allows the model to be pretrained to better capture bidirectional context.

---

### النسخة العربية

في هذا القسم، نراجع أولاً ونقارن النمذجة اللغوية الانحدارية الذاتية التقليدية و BERT للتدريب المسبق اللغوي. بالنظر إلى تسلسل نصي x = [x₁, · · · , xₜ]، تقوم النمذجة اللغوية الانحدارية الذاتية بالتدريب المسبق من خلال تعظيم الاحتمالية في ظل التحليل العاملي الانحداري الذاتي الأمامي:

$$\max_{\theta} \log p_{\theta}(x) = \sum_{t=1}^{T} \log p_{\theta}(x_t | x_{<t}) = \sum_{t=1}^{T} \log \frac{\exp(h_{\theta}(x_{1:t-1})^{\top} e(x_t))}{\sum_{x'} \exp(h_{\theta}(x_{1:t-1})^{\top} e(x'))}$$  (1)

حيث $h_{\theta}(x_{1:t-1})$ هو تمثيل سياقي يتم إنتاجه بواسطة نماذج عصبية، مثل الشبكات العصبية المتكررة أو المحولات، و $e(x)$ يشير إلى تضمين $x$. بالمقارنة، يعتمد BERT على الترميز التلقائي لإزالة الضوضاء. على وجه التحديد، بالنسبة لتسلسل نصي $x$، يقوم BERT أولاً ببناء نسخة مفسدة $\hat{x}$ عن طريق تعيين جزء عشوائي (مثل 15٪) من الرموز في $x$ إلى رمز خاص [MASK]. لنفترض أن الرموز المخفاة هي $\bar{x}$. هدف التدريب هو إعادة بناء $\bar{x}$ من $\hat{x}$:

$$\max_{\theta} \log p_{\theta}(\bar{x} | \hat{x}) \approx \sum_{t=1}^{T} m_t \log p_{\theta}(x_t | \hat{x}) = \sum_{t=1}^{T} m_t \log \frac{\exp(H_{\theta}(\hat{x})_t^{\top} e(x_t))}{\sum_{x'} \exp(H_{\theta}(\hat{x})_t^{\top} e(x'))}$$  (2)

حيث $m_t = 1$ يشير إلى أن $x_t$ مخفي، و $H_{\theta}$ هو محول يرسم تسلسل نصي بطول T من $x$ إلى تسلسل من المتجهات المخفية $H_{\theta}(x) = [H_{\theta}(x)_1, H_{\theta}(x)_2, \cdots, H_{\theta}(x)_T]$. يتم مقارنة إيجابيات وسلبيات هدفي التدريب المسبق في الجوانب التالية:

• **افتراض الاستقلال:** كما يؤكد عليه رمز ≈ في المعادلة (2)، يحلل BERT احتمالية مشروطة مشتركة $p(\bar{x} | \hat{x})$ بناءً على افتراض الاستقلال بأن جميع الرموز المخفاة $\bar{x}$ يتم إعادة بنائها بشكل منفصل. بالمقارنة، يقوم هدف النمذجة اللغوية الانحدارية الذاتية (1) بتحليل $p_{\theta}(x)$ باستخدام قاعدة الضرب التي تحمل عالمياً دون مثل هذا الافتراض الاستقلالي.

• **ضوضاء المدخلات:** تحتوي المدخلات إلى BERT على رموز اصطناعية مثل [MASK] التي لا تحدث أبداً في المهام اللاحقة، مما يخلق تباين بين التدريب المسبق والضبط الدقيق. استبدال [MASK] بالرموز الأصلية كما في [10] لا يحل المشكلة لأن الرموز الأصلية يمكن استخدامها فقط باحتمال صغير — وإلا ستكون المعادلة (2) تافهة للتحسين. بالمقارنة، لا تعتمد النمذجة اللغوية الانحدارية الذاتية على أي إفساد للمدخلات ولا تعاني من هذه المشكلة.

• **تبعية السياق:** يعتمد التمثيل الانحداري الذاتي $h_{\theta}(x_{1:t-1})$ فقط على الرموز حتى الموضع $t$ (أي الرموز على اليسار)، بينما يتمتع تمثيل BERT $H_{\theta}(x)_t$ بالوصول إلى المعلومات السياقية من الجانبين. نتيجة لذلك، يسمح هدف BERT بتدريب النموذج مسبقاً لالتقاط السياق ثنائي الاتجاه بشكل أفضل.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** Forward/backward factorization, context representation, hidden vectors, independence assumption, input noise, context dependency
- **Equations:** 2 main equations (Eq. 1 for AR, Eq. 2 for BERT)
- **Citations:** [10] for BERT
- **Special handling:** Mathematical equations preserved with LaTeX formatting

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
