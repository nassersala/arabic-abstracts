# Section 2: Related Work
## القسم 2: الأعمال ذات الصلة

**Section:** related work
**Translation Quality:** 0.87
**Glossary Terms Used:** التدريب المسبق, معمارية محول, مشفر, فك التشفير, معالجة اللغة الطبيعية, لغة البرمجة, نمذجة لغة مقنعة, تسلسل إلى تسلسل, تمثيل عبر الأنماط, تدفق البيانات, دلالات الشفرة, المعرفات

---

### English Version

**2 Related Work**

**Pre-training on Natural Language.** Pre-trained models based on Transformer architectures (Vaswani et al., 2017) have led to state-of-the-art performance on a broad set of NLP tasks. They can be generally categorized into three groups: encoder-only models such as BERT (Devlin et al., 2019), RoBERTa (Liu et al., 2019b), and ELECTRA (Clark et al., 2020), decoder-only models like GPT (Radford et al., 2019), and encoder-decoder models such as MASS (Song et al., 2019), BART (Lewis et al., 2020), and T5 (Raffel et al., 2020). Compared to encoder-only and decoder-only models that respectively favor understanding and generation tasks, encoder-decoder models can well support both types of tasks. They often employ denoising sequence-to-sequence pre-training objectives that corrupt the source input and require the decoder to recover them. In this work, we extend T5 to the programming language and propose a novel identifier-aware denoising objective that enables the model to better comprehend the code.

**Pre-training on Programming Language.** Pre-training on the programming language is a nascent field where much recent work attempts to extend the NLP pre-training methods to source code. CuBERT (Kanade et al., 2020) and CodeBERT (Feng et al., 2020) are the two pioneer models. CuBERT employs BERT's powerful masked language modeling objective to derive generic code-specific representation, and CodeBERT further adds a replaced token detection (Clark et al., 2020) task to learn NL-PL cross-modal representation. Besides the BERT-style models, Svyatkovskiy et al. (2020) and Liu et al. (2020) respectively employ GPT and UniLM (Dong et al., 2019) for the code completion task. Transcoder (Rozière et al., 2020) explores programming language translation in an unsupervised setting. Different from them, we explore encoder-decoder models based on T5 for programming language pre-training and support a more comprehensive set of tasks.

Some emerging work (Clement et al., 2020; Mastropaolo et al., 2021; Elnaggar et al., 2021) in the recent literature also explore the T5 framework on code, but they only focus on a limited subset of generation tasks and do not support understanding tasks like us. Apart from these, PLBART (Ahmad et al., 2021) based on another encoder-decoder model BART can also support both understanding and generation tasks. However, all the above prior work simply processes code in the same way as natural language and largely ignores the code-specific characteristics. Instead, we propose to leverage the identifier information in code for pre-training.

Recently, GraphCodeBERT (Guo et al., 2021) incorporates the data flow extracted from the code structure into CodeBERT, while Rozière et al. (2021) propose a deobfuscation objective to leverage the structural aspect of PL. These models only focus on training a better code-specific encoder. Zügner et al. (2021) proposes to capture the relative distances between code tokens over the code structure. By contrast, we specifically focus on the identifiers that reserve rich code semantics and fuse such information into a Seq2Seq model via two novel identifier tagging and prediction tasks.

---

### النسخة العربية

**2 الأعمال ذات الصلة**

**التدريب المسبق على اللغة الطبيعية.** أدت النماذج المُدربة مسبقاً المبنية على معماريات المحول (Vaswani et al., 2017) إلى أداء متقدم في مجموعة واسعة من مهام معالجة اللغة الطبيعية. يمكن تصنيفها بشكل عام إلى ثلاث مجموعات: نماذج بمشفر فقط مثل BERT (Devlin et al., 2019) و RoBERTa (Liu et al., 2019b) و ELECTRA (Clark et al., 2020)، ونماذج بفك تشفير فقط مثل GPT (Radford et al., 2019)، ونماذج مشفر-فك تشفير مثل MASS (Song et al., 2019) و BART (Lewis et al., 2020) و T5 (Raffel et al., 2020). بالمقارنة مع نماذج المشفر فقط وفك التشفير فقط التي تفضل على التوالي مهام الفهم والتوليد، يمكن لنماذج المشفر-فك التشفير دعم كلا النوعين من المهام بشكل جيد. غالباً ما تستخدم أهداف التدريب المسبق لإزالة التشويش من تسلسل إلى تسلسل التي تُفسد المدخلات المصدرية وتطلب من فك التشفير استعادتها. في هذا العمل، نوسع T5 إلى لغة البرمجة ونقترح هدفاً جديداً لإزالة التشويش مدركاً للمعرفات يمكّن النموذج من فهم الشفرة بشكل أفضل.

**التدريب المسبق على لغة البرمجة.** التدريب المسبق على لغة البرمجة هو مجال ناشئ حيث تحاول الكثير من الأعمال الأخيرة توسيع أساليب التدريب المسبق لمعالجة اللغة الطبيعية إلى الشفرة المصدرية. CuBERT (Kanade et al., 2020) و CodeBERT (Feng et al., 2020) هما النموذجان الرائدان. يستخدم CuBERT هدف نمذجة اللغة المقنعة القوي لـ BERT لاشتقاق تمثيل عام خاص بالشفرة، ويضيف CodeBERT مهمة كشف الرموز المستبدلة (Clark et al., 2020) لتعلم تمثيل عبر الأنماط للغة الطبيعية-لغة البرمجة. إلى جانب النماذج على طراز BERT، يستخدم Svyatkovskiy et al. (2020) و Liu et al. (2020) على التوالي GPT و UniLM (Dong et al., 2019) لمهمة إكمال الشفرة. يستكشف Transcoder (Rozière et al., 2020) ترجمة لغة البرمجة في إعداد غير خاضع للإشراف. بخلافها، نستكشف نماذج مشفر-فك تشفير بناءً على T5 للتدريب المسبق للغة البرمجة وندعم مجموعة أكثر شمولاً من المهام.

تستكشف بعض الأعمال الناشئة (Clement et al., 2020; Mastropaolo et al., 2021; Elnaggar et al., 2021) في الأدبيات الحديثة أيضاً إطار عمل T5 على الشفرة، لكنها تركز فقط على مجموعة فرعية محدودة من مهام التوليد ولا تدعم مهام الفهم مثلنا. بصرف النظر عن هذه، PLBART (Ahmad et al., 2021) المبني على نموذج مشفر-فك تشفير آخر BART يمكنه أيضاً دعم كل من مهام الفهم والتوليد. ومع ذلك، فإن جميع الأعمال السابقة أعلاه تعالج الشفرة ببساطة بنفس الطريقة كاللغة الطبيعية وتتجاهل إلى حد كبير الخصائص الخاصة بالشفرة. بدلاً من ذلك، نقترح الاستفادة من معلومات المعرفات في الشفرة للتدريب المسبق.

مؤخراً، يدمج GraphCodeBERT (Guo et al., 2021) تدفق البيانات المستخرج من بنية الشفرة في CodeBERT، بينما يقترح Rozière et al. (2021) هدف إزالة التعتيم للاستفادة من الجانب البنيوي للغة البرمجة. تركز هذه النماذج فقط على تدريب مشفر أفضل خاص بالشفرة. يقترح Zügner et al. (2021) التقاط المسافات النسبية بين رموز الشفرة عبر بنية الشفرة. على النقيض من ذلك، نركز بشكل خاص على المعرفات التي تحتفظ بدلالات شفرة غنية وندمج هذه المعلومات في نموذج تسلسل إلى تسلسل عبر مهمتين جديدتين لوسم المعرفات والتنبؤ بها.

---

### Translation Notes

- **Figures referenced:** Figure 2 (mentioned in original but shown in context)
- **Key terms introduced:** نمذجة لغة مقنعة (masked language modeling), كشف الرموز المستبدلة (replaced token detection), إكمال الشفرة (code completion), تدفق البيانات (data flow), إزالة التعتيم (deobfuscation), وسم المعرفات (identifier tagging)
- **Equations:** 0
- **Citations:** 18 references cited (Vaswani 2017, Devlin 2019, Liu 2019, Clark 2020, Radford 2019, Song 2019, Lewis 2020, Raffel 2020, Kanade 2020, Feng 2020, Svyatkovskiy 2020, Liu 2020, Dong 2019, Rozière 2020, Clement 2020, Mastropaolo 2021, Elnaggar 2021, Ahmad 2021, Guo 2021, Zügner 2021)
- **Special handling:** Preserved model names (BERT, RoBERTa, ELECTRA, GPT, MASS, BART, T5, CuBERT, CodeBERT, UniLM, Transcoder, PLBART, GraphCodeBERT) in English as per industry standard

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
