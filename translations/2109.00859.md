---
# CodeT5: Identifier-aware Unified Pre-trained Encoder-Decoder Models for Code Understanding and Generation
## CodeT5: نماذج مشفر-فك تشفير موحدة مُدربة مسبقاً ومدركة للمعرفات لفهم الشفرة وتوليدها

**arXiv ID:** 2109.00859
**Authors:** Yue Wang, Weishi Wang, Shafiq Joty, Steven C.H. Hoi
**Year:** 2021 (EMNLP 2021)
**Categories:** Computation and Language (cs.CL); Programming Languages (cs.PL)
**Translation Quality:** 0.91
**Glossary Terms Used:** مشفر, فك التشفير, التدريب المسبق, محول, لغة البرمجة, اللغة الطبيعية, توليد البرامج, التمثيل, دلالي

### English Abstract
Pre-trained models for Natural Languages (NL) like BERT and GPT have been recently shown to transfer well to Programming Languages (PL) and largely benefit a broad set of code-related tasks. Despite their success, most current methods either rely on an encoder-only (or decoder-only) pre-training that is suboptimal for generation (resp. understanding) tasks or process the code snippet in the same way as NL, neglecting the special characteristics of PL such as syntactic structures. We present CodeT5, a unified pre-trained encoder-decoder Transformer model that better leverages the code semantics conveyed from the developer-assigned identifiers. Our model employs a unified framework to seamlessly support both code understanding and generation tasks and allows for multi-task learning. Besides, we propose a novel identifier-aware pre-training task that enables the model to distinguish which code tokens are identifiers and to recover them when they are masked. Furthermore, we propose to exploit the user-written code comments with a bimodal dual generation task for better NL-PL alignment. Comprehensive experiments show that CodeT5 significantly outperforms prior methods on understanding tasks such as code defect detection and clone detection, and generation tasks across various directions including PL-NL, NL-PL, and PL-PL.

### الملخص العربي
أظهرت النماذج المُدربة مسبقاً للغات الطبيعية مثل BERT و GPT مؤخراً أنها تنتقل بشكل جيد إلى لغات البرمجة وتفيد إلى حد كبير مجموعة واسعة من المهام المتعلقة بالشفرة. على الرغم من نجاحها، فإن معظم الأساليب الحالية إما تعتمد على التدريب المسبق بمشفر فقط (أو فك تشفير فقط) وهو دون المستوى الأمثل لمهام التوليد (أو الفهم على التوالي) أو تعالج مقتطف الشفرة بنفس الطريقة كاللغة الطبيعية، متجاهلة الخصائص الخاصة للغة البرمجة مثل البنى النحوية. نقدم CodeT5، وهو نموذج محول موحد مُدرب مسبقاً بمشفر وفك تشفير يستفيد بشكل أفضل من دلالات الشفرة المنقولة من المعرفات المُعينة من قبل المطور. يستخدم نموذجنا إطار عمل موحداً لدعم مهام فهم الشفرة وتوليدها بسلاسة ويسمح بالتعلم متعدد المهام. بالإضافة إلى ذلك، نقترح مهمة تدريب مسبق جديدة مدركة للمعرفات تمكّن النموذج من تمييز رموز الشفرة التي هي معرفات واستعادتها عندما تكون مخفية. علاوة على ذلك، نقترح استغلال تعليقات الشفرة المكتوبة من قبل المستخدم بمهمة توليد مزدوجة ثنائية الوضع لمحاذاة أفضل بين اللغة الطبيعية ولغة البرمجة. تُظهر التجارب الشاملة أن CodeT5 يتفوق بشكل كبير على الأساليب السابقة في مهام الفهم مثل كشف عيوب الشفرة وكشف الاستنساخ، ومهام التوليد عبر اتجاهات مختلفة بما في ذلك من لغة البرمجة إلى اللغة الطبيعية، ومن اللغة الطبيعية إلى لغة البرمجة، ومن لغة البرمجة إلى لغة البرمجة.

### Back-Translation (Validation)
Pre-trained models for natural languages such as BERT and GPT have recently been shown to transfer well to programming languages and largely benefit a wide set of code-related tasks. Despite their success, most current methods either rely on encoder-only (or decoder-only) pre-training which is suboptimal for generation (or understanding respectively) tasks or process the code snippet in the same way as natural language, ignoring the special characteristics of programming language such as syntactic structures. We present CodeT5, a unified pre-trained encoder-decoder Transformer model that better leverages code semantics conveyed from developer-assigned identifiers. Our model uses a unified framework to seamlessly support code understanding and generation tasks and allows for multi-task learning. Additionally, we propose a novel identifier-aware pre-training task that enables the model to distinguish code tokens that are identifiers and recover them when they are masked. Furthermore, we propose exploiting user-written code comments with a bimodal dual generation task for better alignment between natural language and programming language. Comprehensive experiments show that CodeT5 significantly outperforms previous methods on understanding tasks such as code defect detection and clone detection, and generation tasks across various directions including programming language to natural language, natural language to programming language, and programming language to programming language.

### Translation Metrics
- Iterations: 1
- Final Score: 0.91
- Quality: High
---
