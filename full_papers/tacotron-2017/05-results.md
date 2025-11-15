# Section 5: Results
## القسم 5: النتائج

**Section:** results
**Translation Quality:** 0.89
**Glossary Terms Used:** mean opinion score, baseline, attention mechanism, alignment, encoder, decoder, spectrogram, neural network

---

### English Version

We conduct mean opinion score tests, where the subjects were asked to rate the naturalness of the stimuli in a 5-point Likert scale score. The MOS tests were crowdsourced from native speakers. We present scores for Tacotron alongside various baselines: a parametric (based on LSTM), a concatenative system, and a vanilla seq2seq with scheduled sampling. All of the baselines are built with the same vocoder (Griffin-Lim) to isolate the effect of the model.

We keep the same text normalization and use the same audio preprocessing for all models. 100 unseen phrases are used for the tests and each phrase received 8 ratings. When computing MOS, we only include ratings where headphones were used. The results are shown in Table 1.

| System | MOS |
|--------|-----|
| Parametric | 3.69 ± 0.109 |
| Concatenative | 4.09 ± 0.119 |
| Vanilla seq2seq | 2.61 ± 0.087 |
| Tacotron | **3.82 ± 0.085** |

As we can see, the vanilla seq2seq with scheduled sampling performed significantly worse than Tacotron, which demonstrates the effectiveness of our improvements. The parametric system is a production model and considered as a strong baseline. Tacotron outperforms the parametric baseline with a small but statistically significant margin. Given that the same vocoder (Griffin-Lim) is used for both systems, we attribute the gap to better learning of the acoustic model. The concatenative system has the highest MOS but it requires carefully curated databases and is therefore less scalable.

**Ablation Analysis**

We conduct several ablation studies. First, we compare the CBHG-based encoder and decoder to simpler alternatives. We find that replacing the CBHG encoder with a 2-layer residual GRU encoder leads to noisier attention and makes pronunciation errors (as shown in Figure 3). Similarly, we find that a CBHG-based post-processing network produces better-resolved harmonics and high-frequency formant structure compared to a standard 3-layer convolutional network (as shown in Figure 4). Neither the CBHG encoder nor the post-processing network are strictly necessary for the model to work, but both of them improve model quality significantly.

Second, we compare the vanilla seq2seq model with and without scheduled sampling. Even with scheduled sampling, the vanilla seq2seq model tends to get stuck for many frames before moving forward, which causes bad speech intelligibility. This is different from Tacotron whose attention moves forward more consistently during training (as shown in Figure 5).

We also compare predicting r = 2 vs r = 1 frames per decoder step. We find that r = 2 gives 2× speed-up without affecting the audio quality. We suspect this is because neighboring speech frames are highly correlated. Predicting multiple frames at once makes it easier for the attention mechanism to focus on the corresponding characters.

---

### النسخة العربية

نُجري اختبارات متوسط تقييم الرأي (MOS)، حيث طُلب من المشاركين تقييم طبيعية المحفزات في درجة مقياس ليكرت من 5 نقاط. تم الحصول على اختبارات MOS من متحدثين أصليين عبر التعهيد الجماعي (crowdsourcing). نقدم درجات تاكوترون إلى جانب خطوط أساس مختلفة: نظام بارامتري (قائم على LSTM)، ونظام تسلسلي (concatenative)، وseq2seq أساسي مع أخذ عينات مجدولة. جميع خطوط الأساس مبنية باستخدام نفس المُركِّب الصوتي (Griffin-Lim) لعزل تأثير النموذج.

نحتفظ بنفس تطبيع النص ونستخدم نفس المعالجة المسبقة للصوت لجميع النماذج. يتم استخدام 100 عبارة غير مرئية للاختبارات وتلقت كل عبارة 8 تقييمات. عند حساب MOS، نضمن فقط التقييمات التي تم استخدام سماعات الرأس فيها. النتائج موضحة في الجدول 1.

| النظام | MOS |
|--------|-----|
| البارامتري | 3.69 ± 0.109 |
| التسلسلي | 4.09 ± 0.119 |
| seq2seq أساسي | 2.61 ± 0.087 |
| تاكوترون | **3.82 ± 0.085** |

كما يمكننا أن نرى، أدى seq2seq الأساسي مع أخذ العينات المجدولة بشكل أسوأ بكثير من تاكوترون، مما يوضح فعالية تحسيناتنا. النظام البارامتري هو نموذج إنتاجي ويُعتبر خط أساس قوي. يتفوق تاكوترون على خط الأساس البارامتري بهامش صغير ولكنه ذو دلالة إحصائية. بالنظر إلى أن نفس المُركِّب الصوتي (Griffin-Lim) يُستخدم لكلا النظامين، فإننا نعزو الفجوة إلى تعلم أفضل للنموذج الصوتي. النظام التسلسلي لديه أعلى MOS لكنه يتطلب قواعد بيانات منسقة بعناية وبالتالي فهو أقل قابلية للتوسع.

**تحليل الاستئصال**

نُجري عدة دراسات استئصال (ablation studies). أولاً، نقارن المشفر وفك التشفير القائمين على CBHG ببدائل أبسط. نجد أن استبدال مشفر CBHG بمشفر GRU متبقي من طبقتين يؤدي إلى انتباه أكثر ضوضاءً ويرتكب أخطاء نطق (كما هو موضح في الشكل 3). وبالمثل، نجد أن شبكة المعالجة اللاحقة القائمة على CBHG تنتج توافقيات أفضل دقة وبنية تكوينية عالية التردد مقارنة بشبكة التفافية قياسية من 3 طبقات (كما هو موضح في الشكل 4). لا يُعد مشفر CBHG ولا شبكة المعالجة اللاحقة ضروريين بشكل صارم لعمل النموذج، لكن كلاهما يحسن جودة النموذج بشكل كبير.

ثانياً، نقارن نموذج seq2seq الأساسي مع وبدون أخذ العينات المجدولة. حتى مع أخذ العينات المجدولة، يميل نموذج seq2seq الأساسي إلى الانحصار لإطارات عديدة قبل المضي قدماً، مما يتسبب في سوء وضوح الكلام. هذا يختلف عن تاكوترون الذي يتحرك انتباهه للأمام بشكل أكثر اتساقاً أثناء التدريب (كما هو موضح في الشكل 5).

نقارن أيضاً التنبؤ بـ r = 2 مقابل r = 1 إطار لكل خطوة فك تشفير. نجد أن r = 2 يعطي تسريعاً بمقدار 2× دون التأثير على جودة الصوت. نشك في أن هذا بسبب أن إطارات الكلام المجاورة مترابطة بشدة. التنبؤ بإطارات متعددة في وقت واحد يجعل من الأسهل على آلية الانتباه التركيز على الأحرف المقابلة.

---

### Translation Notes

- **Figures referenced:** Figure 3, Figure 4, Figure 5, Table 1
- **Key terms introduced:**
  - mean opinion score (MOS): متوسط تقييم الرأي
  - Likert scale: مقياس ليكرت
  - crowdsourcing: التعهيد الجماعي
  - parametric system: نظام بارامتري
  - concatenative system: نظام تسلسلي
  - vanilla seq2seq: seq2seq أساسي
  - scheduled sampling: أخذ العينات المجدولة
  - baseline: خط الأساس
  - vocoder: مُركِّب صوتي
  - ablation studies: دراسات الاستئصال
  - harmonics: توافقيات
  - formant structure: بنية تكوينية
  - speech intelligibility: وضوح الكلام
  - statistically significant: ذو دلالة إحصائية
- **Equations:** 0
- **Citations:** Multiple references to Figures and Tables
- **Special handling:**
  - Preserved MOS scores and statistical values in their original format
  - Kept table structure for clarity
  - Maintained figure references

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.91
- Readability: 0.88
- Glossary consistency: 0.87
- **Overall section score:** 0.89
