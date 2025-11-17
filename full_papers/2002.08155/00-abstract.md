---
# CodeBERT: A Pre-Trained Model for Programming and Natural Languages
## CodeBERT: نموذج مُدرب مسبقاً للغات البرمجة واللغات الطبيعية

**arXiv ID:** 2002.08155
**Authors:** Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Linjun Shou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou
**Year:** 2020 (EMNLP 2020)
**Categories:** Computation and Language (cs.CL); Programming Languages (cs.PL)
**Translation Quality:** 0.92
**Glossary Terms Used:** التدريب المسبق, لغة البرمجة, اللغة الطبيعية, محول, التمثيل, ضبط دقيق, مجموعة بيانات

### English Abstract
We present CodeBERT, a bimodal pre-trained model for programming language (PL) and natural language (NL). CodeBERT learns general-purpose representations that support downstream NL-PL applications such as natural language code search, code documentation generation, etc. We develop CodeBERT with Transformer-based neural architecture, and train it with a hybrid objective function that incorporates the pre-training task of replaced token detection, which is to detect plausible alternatives sampled from generators. This enables us to utilize both "bimodal" data of NL-PL pairs and "unimodal" data, where the former is code snippet with its paired documentation, and the latter is code snippet without paired documentation. We evaluate CodeBERT on two NL-PL applications by fine-tuning model parameters. Results show that CodeBERT achieves state-of-the-art performance on both natural language code search and code documentation generation tasks. Furthermore, to investigate what type of knowledge is learned in CodeBERT, we construct a dataset for NL-PL probing, and evaluate in a zero-shot setting where parameters of pre-trained models are fixed. Results show that CodeBERT performs better than previous pre-trained models on NL-PL probing.

### الملخص العربي
نقدم CodeBERT، وهو نموذج ثنائي الوضع مُدرب مسبقاً للغة البرمجة واللغة الطبيعية. يتعلم CodeBERT تمثيلات عامة الغرض تدعم تطبيقات اللغة الطبيعية ولغة البرمجة المتتابعة مثل البحث عن الشفرة باللغة الطبيعية، وتوليد توثيق الشفرة، وما إلى ذلك. نطور CodeBERT بمعمارية عصبية قائمة على المحولات، وندربه بدالة هدفية هجينة تتضمن مهمة التدريب المسبق للكشف عن الرموز المستبدلة، وهي الكشف عن البدائل المحتملة المأخوذة من المولدات. يمكّننا هذا من استخدام كل من بيانات "ثنائية الوضع" لأزواج اللغة الطبيعية ولغة البرمجة والبيانات "أحادية الوضع"، حيث الأولى عبارة عن مقتطف شفرة مع توثيقه المقترن، والأخيرة هي مقتطف شفرة بدون توثيق مقترن. نقيّم CodeBERT على تطبيقين للغة الطبيعية ولغة البرمجة من خلال الضبط الدقيق لمعاملات النموذج. تظهر النتائج أن CodeBERT يحقق أداءً متقدماً على كل من مهام البحث عن الشفرة باللغة الطبيعية وتوليد توثيق الشفرة. علاوة على ذلك، للتحقق من نوع المعرفة التي تم تعلمها في CodeBERT، نبني مجموعة بيانات لاستكشاف اللغة الطبيعية ولغة البرمجة، ونقيّم في إعداد صفري التجربة حيث تكون معاملات النماذج المُدربة مسبقاً ثابتة. تُظهر النتائج أن CodeBERT يؤدي بشكل أفضل من النماذج المُدربة مسبقاً السابقة في استكشاف اللغة الطبيعية ولغة البرمجة.

### Back-Translation (Validation)
We present CodeBERT, a bimodal pre-trained model for programming language and natural language. CodeBERT learns general-purpose representations that support downstream natural language and programming language applications such as code search using natural language, code documentation generation, etc. We develop CodeBERT with a Transformer-based neural architecture, and train it with a hybrid objective function that includes the pre-training task of replaced token detection, which is detecting plausible alternatives sampled from generators. This enables us to use both "bimodal" data of natural language and programming language pairs and "unimodal" data, where the former is a code snippet with its paired documentation, and the latter is a code snippet without paired documentation. We evaluate CodeBERT on two natural language and programming language applications through fine-tuning model parameters. The results show that CodeBERT achieves state-of-the-art performance on both natural language code search and code documentation generation tasks. Furthermore, to investigate what type of knowledge was learned in CodeBERT, we build a dataset for exploring natural language and programming language, and evaluate in a zero-shot setting where the parameters of pre-trained models are fixed. The results show that CodeBERT performs better than previous pre-trained models in exploring natural language and programming language.

### Translation Metrics
- Iterations: 1
- Final Score: 0.92
- Quality: High
---
