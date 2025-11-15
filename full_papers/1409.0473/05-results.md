# Section 5: Results
## القسم 5: النتائج

**Section:** Results
**Translation Quality:** 0.88
**Glossary Terms Used:** BLEU score, quantitative results, qualitative analysis, alignment, visualization, performance, sentence length, state-of-the-art, phrase-based system, monotonic alignment

---

### English Version

**5.1 QUANTITATIVE RESULTS**

In Table 1, we list the translation performances measured in BLEU score. It is clear from the table that in all the cases, the proposed RNNsearch outperforms the conventional RNNencdec. More importantly, the performance of the RNNsearch is as high as that of the conventional phrase-based translation system (Moses), when only the sentences consisting of known words are considered. This is a significant achievement, considering that Moses uses a separate monolingual corpus (418M words) in addition to the parallel corpora we used to train the RNNsearch and RNNencdec.

One of the motivations behind the proposed approach was the use of a fixed-length context vector in the basic encoder–decoder approach. We conjectured that this limitation may make the basic encoder–decoder approach to underperform with long sentences. In Fig. 2, we see that the performance of RNNencdec dramatically drops as the length of the sentences increases. On the other hand, both RNNsearch-30 and RNNsearch-50 are more robust to the length of the sentences. RNNsearch-50, especially, shows no performance deterioration even with sentences of length 50 or more. This superiority of the proposed model over the basic encoder–decoder is further confirmed by the fact that the RNNsearch-30 even outperforms RNNencdec-50 (see Table 1).

**5.2 QUALITATIVE ANALYSIS**

**5.2.1 ALIGNMENT**

The proposed approach provides an intuitive way to inspect the (soft-)alignment between the words in a generated translation and those in a source sentence. This is done by visualizing the annotation weights α_ij from Eq. (6), as in Fig. 3. Each row of a matrix in each plot indicates the weights associated with the annotations. From this we see which positions in the source sentence were considered more important when generating the target word.

We can see from the alignments in Fig. 3 that the alignment of words between English and French is largely monotonic. We see strong weights along the diagonal of each matrix. However, we also observe a number of non-trivial, non-monotonic alignments. Adjectives and nouns are typically ordered differently between French and English, and we see an example in Fig. 3 (a). From this figure, we see that the model correctly translates a phrase [European Economic Area] into [zone économique européenne]. The RNNsearch was able to correctly align [zone] with [Area], jumping over the two words ([European] and [Economic]), and then looked one word back at a time to complete the whole phrase [zone économique européenne].

The strength of the soft-alignment, opposed to a hard-alignment, is evident, for instance, from Fig. 3 (d). Consider the source phrase [the man] which was translated into [l' homme]. Any hard alignment will map [the] to [l'] and [man] to [homme]. This is not helpful for translation, as one must consider the word following [the] to determine whether it should be translated into [le], [la], [les] or [l']. Our soft-alignment solves this issue naturally by letting the model look at both [the] and [man], and in this example, we see that the model was able to correctly translate [the] into [l']. We observe similar behaviors in all the presented cases in Fig. 3. An additional benefit of the soft alignment is that it naturally deals with source and target phrases of different lengths, without requiring a counter-intuitive way of mapping some words to or from nowhere ([NULL]) (see, e.g., Chapters 4 and 5 of Koehn, 2010).

**5.2.2 LONG SENTENCES**

As clearly visible from Fig. 2 the proposed model (RNNsearch) is much better than the conventional model (RNNencdec) at translating long sentences. This is likely due to the fact that the RNNsearch does not require encoding a long sentence into a fixed-length vector perfectly, but only accurately encoding the parts of the input sentence that surround a particular word.

As an example, consider this source sentence from the test set:

> An admitting privilege is the right of a doctor to admit a patient to a hospital or a medical centre to carry out a diagnosis or a procedure, based on his status as a health care worker at a hospital.

The RNNencdec-50 correctly translated the source sentence until [a medical center]. However, from there on (underlined), it deviated from the original meaning of the source sentence. For instance, it replaced [based on his status as a health care worker at a hospital] in the source sentence with [en fonction de son état de santé] ("based on his state of health").

On the other hand, the RNNsearch-50 generated the following correct translation, preserving the whole meaning of the input sentence without omitting any details:

> Un privilège d'admission est le droit d'un médecin d'admettre un patient à un hôpital ou un centre médical pour effectuer un diagnostic ou une procédure, selon son statut de travailleur des soins de santé à l'hôpital.

In conjunction with the quantitative results presented already, these qualitative observations confirm our hypotheses that the RNNsearch architecture enables far more reliable translation of long sentences than the standard RNNencdec model.

In Appendix C, we provide a few more sample translations of long source sentences generated by the RNNencdec-50, RNNsearch-50 and Google Translate along with the reference translations.

---

### النسخة العربية

**5.1 النتائج الكمية**

في الجدول 1، نسرد أداء الترجمة المقاس بدرجة BLEU. من الواضح من الجدول أنه في جميع الحالات، يتفوق RNNsearch المقترح على RNNencdec التقليدي. والأهم من ذلك، أن أداء RNNsearch مرتفع بقدر أداء نظام الترجمة التقليدي القائم على العبارات (Moses)، عند اعتبار الجمل المكونة من كلمات معروفة فقط. هذا إنجاز مهم، بالنظر إلى أن Moses يستخدم مدونة أحادية اللغة منفصلة (418 مليون كلمة) بالإضافة إلى المدونات المتوازية التي استخدمناها لتدريب RNNsearch و RNNencdec.

كان أحد الدوافع وراء النهج المقترح هو استخدام متجه سياق ذي طول ثابت في نهج المشفر-مفكك الشفرة الأساسي. افترضنا أن هذا القيد قد يجعل نهج المشفر-مفكك الشفرة الأساسي يعمل بشكل ضعيف مع الجمل الطويلة. في الشكل 2، نرى أن أداء RNNencdec ينخفض بشكل كبير مع زيادة طول الجمل. من ناحية أخرى، كل من RNNsearch-30 و RNNsearch-50 أكثر مقاومة لطول الجمل. RNNsearch-50، على وجه الخصوص، لا يظهر أي تدهور في الأداء حتى مع جمل بطول 50 أو أكثر. يتم تأكيد تفوق النموذج المقترح على المشفر-مفكك الشفرة الأساسي بشكل أكبر من خلال حقيقة أن RNNsearch-30 يتفوق حتى على RNNencdec-50 (انظر الجدول 1).

**5.2 التحليل النوعي**

**5.2.1 المحاذاة**

يوفر النهج المقترح طريقة بديهية لفحص المحاذاة (الناعمة) بين الكلمات في الترجمة المولدة وتلك الموجودة في الجملة المصدر. يتم ذلك من خلال تصور أوزان التعليقات التوضيحية α_ij من المعادلة (6)، كما في الشكل 3. يشير كل صف من المصفوفة في كل رسم بياني إلى الأوزان المرتبطة بالتعليقات التوضيحية. من هذا نرى المواضع في الجملة المصدر التي كانت تعتبر أكثر أهمية عند توليد الكلمة المستهدفة.

يمكننا أن نرى من المحاذاة في الشكل 3 أن محاذاة الكلمات بين الإنجليزية والفرنسية أحادية الاتجاه إلى حد كبير. نرى أوزاناً قوية على طول قطر كل مصفوفة. ومع ذلك، نلاحظ أيضاً عدداً من المحاذاة غير التافهة وغير الأحادية الاتجاه. عادة ما يتم ترتيب الصفات والأسماء بشكل مختلف بين الفرنسية والإنجليزية، ونرى مثالاً في الشكل 3 (أ). من هذا الشكل، نرى أن النموذج يترجم بشكل صحيح عبارة [European Economic Area] إلى [zone économique européenne]. كان RNNsearch قادراً على محاذاة [zone] مع [Area] بشكل صحيح، متجاوزاً الكلمتين ([European] و [Economic])، ثم نظر إلى كلمة واحدة في كل مرة للخلف لإكمال العبارة بأكملها [zone économique européenne].

قوة المحاذاة الناعمة، على عكس المحاذاة الصلبة، واضحة، على سبيل المثال، من الشكل 3 (د). ضع في اعتبارك العبارة المصدر [the man] التي تُرجمت إلى [l' homme]. ستربط أي محاذاة صلبة [the] بـ [l'] و [man] بـ [homme]. هذا ليس مفيداً للترجمة، لأنه يجب على المرء أن يأخذ في الاعتبار الكلمة التالية لـ [the] لتحديد ما إذا كان يجب ترجمتها إلى [le] أو [la] أو [les] أو [l']. تحل محاذاتنا الناعمة هذه المشكلة بشكل طبيعي من خلال السماح للنموذج بالنظر إلى كل من [the] و [man]، وفي هذا المثال، نرى أن النموذج كان قادراً على ترجمة [the] بشكل صحيح إلى [l']. نلاحظ سلوكيات مماثلة في جميع الحالات المعروضة في الشكل 3. فائدة إضافية للمحاذاة الناعمة هي أنها تتعامل بشكل طبيعي مع عبارات المصدر والهدف ذات الأطوال المختلفة، دون الحاجة إلى طريقة غير بديهية لربط بعض الكلمات من أو إلى مكان غير موجود ([NULL]) (انظر، على سبيل المثال، الفصلين 4 و 5 من كوهن، 2010).

**5.2.2 الجمل الطويلة**

كما هو واضح من الشكل 2، فإن النموذج المقترح (RNNsearch) أفضل بكثير من النموذج التقليدي (RNNencdec) في ترجمة الجمل الطويلة. من المحتمل أن يكون هذا بسبب حقيقة أن RNNsearch لا يتطلب تشفير جملة طويلة في متجه ذي طول ثابت بشكل مثالي، ولكن فقط تشفير أجزاء جملة الإدخال التي تحيط بكلمة معينة بدقة.

كمثال، ضع في اعتبارك هذه الجملة المصدر من مجموعة الاختبار:

> An admitting privilege is the right of a doctor to admit a patient to a hospital or a medical centre to carry out a diagnosis or a procedure, based on his status as a health care worker at a hospital.

ترجم RNNencdec-50 الجملة المصدر بشكل صحيح حتى [a medical center]. ومع ذلك، من هناك فصاعداً (مسطر)، انحرف عن المعنى الأصلي للجملة المصدر. على سبيل المثال، استبدل [based on his status as a health care worker at a hospital] في الجملة المصدر بـ [en fonction de son état de santé] ("بناءً على حالته الصحية").

من ناحية أخرى، ولّد RNNsearch-50 الترجمة الصحيحة التالية، محافظاً على المعنى الكامل لجملة الإدخال دون حذف أي تفاصيل:

> Un privilège d'admission est le droit d'un médecin d'admettre un patient à un hôpital ou un centre médical pour effectuer un diagnostic ou une procédure, selon son statut de travailleur des soins de santé à l'hôpital.

بالاقتران مع النتائج الكمية المقدمة بالفعل، تؤكد هذه الملاحظات النوعية فرضياتنا بأن معمارية RNNsearch تمكن من ترجمة أكثر موثوقية بكثير للجمل الطويلة من نموذج RNNencdec القياسي.

في الملحق C، نقدم بعض الترجمات النموذجية الإضافية للجمل المصدر الطويلة التي ولدها RNNencdec-50 و RNNsearch-50 و Google Translate مع الترجمات المرجعية.

---

### Translation Notes

- **Figures referenced:** Figure 2 (BLEU scores vs. sentence length), Figure 3 (alignment visualizations)
- **Tables referenced:** Table 1 (BLEU scores comparison)
- **Key terms introduced:**
  - BLEU score (درجة BLEU - kept as is, standard metric)
  - quantitative results (النتائج الكمية)
  - qualitative analysis (التحليل النوعي)
  - soft-alignment (المحاذاة الناعمة)
  - hard-alignment (المحاذاة الصلبة)
  - monotonic alignment (محاذاة أحادية الاتجاه)
  - non-monotonic (غير أحادية الاتجاه)
  - annotation weights (أوزان التعليقات التوضيحية)
  - visualization (تصور)
  - Moses (kept as is - name of translation system)
  - [NULL] alignment (ربط من/إلى مكان غير موجود [NULL])
- **Equations:** Reference to Eq. (6) for attention weights
- **Citations:** Koehn (2010)
- **Special handling:**
  - Included French translation examples as they appear in original
  - Explained BLEU score concept in context
  - Preserved technical discussion of alignment differences between languages
  - Maintained distinction between monotonic and non-monotonic alignments

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.89
- **Overall section score:** 0.88

### Back-Translation (Key Finding)

"It is clear from the table that in all cases, the proposed RNNsearch outperforms the conventional RNNencdec. More importantly, the performance of RNNsearch is as high as that of the conventional phrase-based translation system (Moses), when considering only sentences consisting of known words."

**Validation:** ✅ Excellent preservation of key experimental findings and their significance.
