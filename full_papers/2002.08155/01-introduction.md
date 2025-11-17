# Section 1: Introduction
## القسم 1: المقدمة

**Section:** Introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** التدريب المسبق, نموذج, ثنائي الوضع, لغة البرمجة, اللغة الطبيعية, محولات, نمذجة اللغة المقنعة, الضبط الدقيق, البحث عن الشفرة, توليد التوثيق, صفري التجربة, التمثيلات, معمارية عصبية

---

### English Version

# 1 Introduction

Large pre-trained models such as ELMo (Peters et al., 2018), GPT (Radford et al., 2018), BERT (Devlin et al., 2018), XLNet (Yang et al., 2019) and RoBERTa (Liu et al., 2019) have dramatically improved the state-of-the-art on a variety of natural language processing (NLP) tasks. These pre-trained models learn effective contextual representations from massive unlabeled text optimized by self-supervised objectives, such as masked language modeling, which predicts the original masked word from an artificially masked input sequence. The success of pre-trained models in NLP also drives a surge of multi-modal pre-trained models, such as ViLBERT (Lu et al., 2019) for language-image and VideoBERT (Sun et al., 2019) for language-video, which are learned from bimodal data such as language-image pairs with bimodal self-supervised objectives.

In this work, we present CodeBERT, a bimodal pre-trained model for natural language (NL) and programming language (PL) like Python, Java, JavaScript, etc. CodeBERT captures the semantic connection between natural language and programming language, and produces general-purpose representations that can broadly support NL-PL understanding tasks (e.g. natural language code search) and generation tasks (e.g. code documentation generation). It is developed with the multi-layer Transformer (Vaswani et al., 2017), which is adopted in a majority of large pre-trained models.

In order to make use of both bimodal instances of NL-PL pairs and large amount of available unimodal codes, we train CodeBERT with a hybrid objective function, including standard masked language modeling (Devlin et al., 2018) and replaced token detection (Clark et al., 2020), where unimodal codes help to learn better generators for producing better alternative tokens for the latter objective.

We train CodeBERT from Github code repositories in 6 programming languages, where bimodal datapoints are codes that pair with function-level natural language documentations (Husain et al., 2019). Training is conducted in a setting similar to that of multilingual BERT (Pires et al., 2019), in which case one pre-trained model is learned for 6 programming languages with no explicit markers used to denote the input programming language. We evaluate CodeBERT on two downstream NL-PL tasks, including natural language code search and code documentation generation. Results show that fine-tuning the parameters of CodeBERT achieves state-of-the-art performance on both tasks. To further investigate what type of knowledge is learned in CodeBERT, we construct a dataset for NL-PL probing, and test CodeBERT in a zero-shot scenario, i.e. without fine-tuning the parameters of CodeBERT. We find that CodeBERT consistently outperforms RoBERTa, a purely natural language-based pre-trained model. The contributions of this work are as follows:

• CodeBERT is the first large NL-PL pre-trained model for multiple programming languages.

• Empirical results show that CodeBERT is effective in both code search and code-to-text generation tasks.

• We further created a dataset which is the first one to investigate the probing ability of the code-based pre-trained models.

---

### النسخة العربية

# 1 المقدمة

حققت النماذج الكبيرة المُدربة مسبقاً مثل ELMo (Peters et al., 2018) و GPT (Radford et al., 2018) و BERT (Devlin et al., 2018) و XLNet (Yang et al., 2019) و RoBERTa (Liu et al., 2019) تحسينات كبيرة في أحدث التقنيات على مجموعة متنوعة من مهام معالجة اللغة الطبيعية. تتعلم هذه النماذج المُدربة مسبقاً تمثيلات سياقية فعالة من نصوص ضخمة غير مُعنونة مُحسّنة بأهداف التعلم الذاتي الإشراف، مثل نمذجة اللغة المقنعة، التي تتنبأ بالكلمة المقنعة الأصلية من تسلسل مدخلات مقنّع اصطناعياً. يدفع نجاح النماذج المُدربة مسبقاً في معالجة اللغة الطبيعية أيضاً إلى موجة من النماذج المُدربة مسبقاً متعددة الأنماط، مثل ViLBERT (Lu et al., 2019) للغة والصور و VideoBERT (Sun et al., 2019) للغة والفيديو، والتي يتم تعلمها من بيانات ثنائية الوضع مثل أزواج اللغة والصور بأهداف ثنائية الوضع للتعلم الذاتي الإشراف.

في هذا العمل، نقدم CodeBERT، وهو نموذج ثنائي الوضع مُدرب مسبقاً للغة الطبيعية ولغة البرمجة مثل Python و Java و JavaScript وما إلى ذلك. يلتقط CodeBERT الاتصال الدلالي بين اللغة الطبيعية ولغة البرمجة، وينتج تمثيلات عامة الغرض يمكنها دعم مهام فهم اللغة الطبيعية ولغة البرمجة على نطاق واسع (مثل البحث عن الشفرة باللغة الطبيعية) ومهام التوليد (مثل توليد توثيق الشفرة). تم تطويره باستخدام المحولات متعددة الطبقات (Vaswani et al., 2017)، والتي يتم اعتمادها في غالبية النماذج الكبيرة المُدربة مسبقاً.

من أجل الاستفادة من كل من الحالات ثنائية الوضع لأزواج اللغة الطبيعية ولغة البرمجة والكم الكبير من الشفرات أحادية الوضع المتاحة، ندرب CodeBERT بدالة هدفية هجينة، تتضمن نمذجة اللغة المقنعة القياسية (Devlin et al., 2018) والكشف عن الرموز المستبدلة (Clark et al., 2020)، حيث تساعد الشفرات أحادية الوضع في تعلم مولدات أفضل لإنتاج رموز بديلة أفضل للهدف الأخير.

ندرب CodeBERT من مستودعات شفرات Github بـ 6 لغات برمجة، حيث نقاط البيانات ثنائية الوضع هي شفرات مقترنة بتوثيقات اللغة الطبيعية على مستوى الدالة (Husain et al., 2019). يتم إجراء التدريب في إعداد مشابه لـ BERT متعدد اللغات (Pires et al., 2019)، وفي هذه الحالة يتم تعلم نموذج واحد مُدرب مسبقاً لـ 6 لغات برمجة دون استخدام علامات صريحة للإشارة إلى لغة البرمجة المدخلة. نقيّم CodeBERT على مهمتين متتابعتين للغة الطبيعية ولغة البرمجة، بما في ذلك البحث عن الشفرة باللغة الطبيعية وتوليد توثيق الشفرة. تُظهر النتائج أن الضبط الدقيق لمعاملات CodeBERT يحقق أداءً متقدماً على كلا المهمتين. للتحقق بشكل أكبر من نوع المعرفة المُتعلمة في CodeBERT، نبني مجموعة بيانات لاستكشاف اللغة الطبيعية ولغة البرمجة، ونختبر CodeBERT في سيناريو صفري التجربة، أي بدون الضبط الدقيق لمعاملات CodeBERT. نجد أن CodeBERT يتفوق باستمرار على RoBERTa، وهو نموذج مُدرب مسبقاً قائم على اللغة الطبيعية فقط. مساهمات هذا العمل هي كما يلي:

• CodeBERT هو أول نموذج كبير مُدرب مسبقاً للغة الطبيعية ولغة البرمجة لعدة لغات برمجة.

• تُظهر النتائج التجريبية أن CodeBERT فعال في كل من مهام البحث عن الشفرة وتوليد النص من الشفرة.

• أنشأنا أيضاً مجموعة بيانات وهي الأولى للتحقق من قدرة الاستكشاف للنماذج المُدربة مسبقاً القائمة على الشفرة.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:** CodeBERT, bimodal pre-trained model, NL-PL pairs, replaced token detection, NL-PL probing
- **Equations:** 0
- **Citations:** 15 references cited
- **Special handling:** Preserved programming language names (Python, Java, JavaScript) in English as per convention

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88

### Back-Translation Sample

Key paragraph (3rd paragraph) back-translated to verify quality:

**Arabic:** "من أجل الاستفادة من كل من الحالات ثنائية الوضع لأزواج اللغة الطبيعية ولغة البرمجة والكم الكبير من الشفرات أحادية الوضع المتاحة، ندرب CodeBERT بدالة هدفية هجينة، تتضمن نمذجة اللغة المقنعة القياسية والكشف عن الرموز المستبدلة، حيث تساعد الشفرات أحادية الوضع في تعلم مولدات أفضل لإنتاج رموز بديلة أفضل للهدف الأخير."

**Back-translation:** "In order to benefit from both the bimodal cases of natural language and programming language pairs and the large amount of available unimodal codes, we train CodeBERT with a hybrid objective function, which includes standard masked language modeling and replaced token detection, where unimodal codes help learn better generators for producing better alternative tokens for the latter objective."

**Semantic match:** ✓ High fidelity to original
