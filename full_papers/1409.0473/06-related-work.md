# Section 6: Related Work
## القسم 6: الأعمال ذات الصلة

**Section:** Related Work
**Translation Quality:** 0.87
**Glossary Terms Used:** alignment, handwriting synthesis, neural probabilistic language model, feedforward neural network, statistical machine translation, neural networks, re-ranking

---

### English Version

**6.1 LEARNING TO ALIGN**

A similar approach of aligning an output symbol with an input symbol was proposed recently by Graves (2013) in the context of handwriting synthesis. Handwriting synthesis is a task where the model is asked to generate handwriting of a given sequence of characters. In his work, he used a mixture of Gaussian kernels to compute the weights of the annotations, where the location, width and mixture coefficient of each kernel was predicted from an alignment model. More specifically, his alignment was restricted to predict the location such that the location increases monotonically.

The main difference from our approach is that, in (Graves, 2013), the modes of the weights of the annotations only move in one direction. In the context of machine translation, this is a severe limitation, as (long-distance) reordering is often needed to generate a grammatically correct translation (for instance, English-to-German).

Our approach, on the other hand, requires computing the annotation weight of every word in the source sentence for each word in the translation. This drawback is not severe with the task of translation in which most of input and output sentences are only 15–40 words. However, this may limit the applicability of the proposed scheme to other tasks.

**6.2 NEURAL NETWORKS FOR MACHINE TRANSLATION**

Since Bengio et al. (2003) introduced a neural probabilistic language model which uses a neural network to model the conditional probability of a word given a fixed number of the preceding words, neural networks have widely been used in machine translation. However, the role of neural networks has been largely limited to simply providing a single feature to an existing statistical machine translation system or to re-rank a list of candidate translations provided by an existing system.

For instance, Schwenk (2012) proposed using a feedforward neural network to compute the score of a pair of source and target phrases and to use the score as an additional feature in the phrase-based statistical machine translation system. More recently, Kalchbrenner and Blunsom (2013) and Devlin et al. (2014) reported the successful use of the neural networks as a sub-component of the existing translation system. Traditionally, a neural network trained as a target-side language model has been used to rescore or rerank a list of candidate translations (see, e.g., Schwenk et al., 2006).

Although the above approaches were shown to improve the translation performance over the state-of-the-art machine translation systems, we are more interested in a more ambitious objective of designing a completely new translation system based on neural networks. The neural machine translation approach we consider in this paper is therefore a radical departure from these earlier works. Rather than using a neural network as a part of the existing system, our model works on its own and generates a translation from a source sentence directly.

---

### النسخة العربية

**6.1 التعلم للمحاذاة**

تم اقتراح نهج مماثل لمحاذاة رمز مخرج مع رمز إدخال مؤخراً من قبل جريفز (2013) في سياق تركيب الخط اليدوي. تركيب الخط اليدوي هو مهمة يُطلب فيها من النموذج توليد خط يدوي لتسلسل معين من الأحرف. في عمله، استخدم مزيجاً من نوى جاوسية لحساب أوزان التعليقات التوضيحية، حيث تم التنبؤ بالموقع والعرض ومعامل المزيج لكل نواة من نموذج المحاذاة. وبشكل أكثر تحديداً، كانت محاذاته مقيدة بالتنبؤ بالموقع بحيث يزداد الموقع بشكل أحادي الاتجاه.

الفرق الرئيسي عن نهجنا هو أنه في (جريفز، 2013)، تتحرك أنماط أوزان التعليقات التوضيحية في اتجاه واحد فقط. في سياق الترجمة الآلية، هذا قيد شديد، حيث غالباً ما تكون هناك حاجة إلى إعادة ترتيب (لمسافات طويلة) لتوليد ترجمة صحيحة نحوياً (على سبيل المثال، من الإنجليزية إلى الألمانية).

نهجنا، من ناحية أخرى، يتطلب حساب وزن التعليق التوضيحي لكل كلمة في الجملة المصدر لكل كلمة في الترجمة. هذا العيب ليس شديداً مع مهمة الترجمة التي تكون فيها معظم جمل الإدخال والمخرجات 15-40 كلمة فقط. ومع ذلك، قد يحد هذا من قابلية تطبيق المخطط المقترح على مهام أخرى.

**6.2 الشبكات العصبية للترجمة الآلية**

منذ أن قدم بينجيو وآخرون (2003) نموذج لغة عصبي احتمالي يستخدم شبكة عصبية لنمذجة الاحتمال الشرطي لكلمة بمعطى عدد ثابت من الكلمات السابقة، تم استخدام الشبكات العصبية على نطاق واسع في الترجمة الآلية. ومع ذلك، فقد اقتصر دور الشبكات العصبية إلى حد كبير على مجرد توفير ميزة واحدة لنظام ترجمة آلية إحصائي موجود أو لإعادة ترتيب قائمة من الترجمات المرشحة التي يوفرها نظام موجود.

على سبيل المثال، اقترح شوينك (2012) استخدام شبكة عصبية أمامية لحساب درجة زوج من عبارات المصدر والهدف واستخدام الدرجة كميزة إضافية في نظام الترجمة الآلية الإحصائية القائمة على العبارات. في الآونة الأخيرة، أفاد كالشبرينر وبلانسوم (2013) وديفلين وآخرون (2014) عن الاستخدام الناجح للشبكات العصبية كمكون فرعي من نظام الترجمة الموجود. تقليدياً، تم استخدام شبكة عصبية مدربة كنموذج لغة جانب الهدف لإعادة تسجيل أو إعادة ترتيب قائمة من الترجمات المرشحة (انظر، على سبيل المثال، شوينك وآخرون، 2006).

على الرغم من أن النُهج المذكورة أعلاه أظهرت تحسين أداء الترجمة على أنظمة الترجمة الآلية الحديثة، فإننا أكثر اهتماماً بهدف أكثر طموحاً وهو تصميم نظام ترجمة جديد تماماً يعتمد على الشبكات العصبية. لذلك فإن نهج الترجمة الآلية العصبية الذي نعتبره في هذا البحث يمثل خروجاً جذرياً عن هذه الأعمال السابقة. بدلاً من استخدام شبكة عصبية كجزء من النظام الموجود، يعمل نموذجنا بمفرده ويولد ترجمة من جملة مصدر مباشرة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - handwriting synthesis (تركيب الخط اليدوي)
  - Gaussian kernels (نوى جاوسية)
  - monotonically (بشكل أحادي الاتجاه)
  - long-distance reordering (إعادة ترتيب لمسافات طويلة)
  - neural probabilistic language model (نموذج لغة عصبي احتمالي)
  - feedforward neural network (شبكة عصبية أمامية)
  - sub-component (مكون فرعي)
  - re-ranking (إعادة الترتيب)
  - rescoring (إعادة التسجيل)
  - radical departure (خروج جذري)
- **Equations:** None
- **Citations:** Graves (2013), Bengio et al. (2003), Schwenk (2012), Kalchbrenner and Blunsom (2013), Devlin et al. (2014), Schwenk et al. (2006)
- **Special handling:**
  - Distinguished between using neural networks as features vs. end-to-end systems
  - Explained limitation of monotonic alignment for translation
  - Contrasted approach with prior work that used neural networks within existing MT systems

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87

### Back-Translation (Key Distinction)

"The neural machine translation approach we consider in this paper is therefore a radical departure from these earlier works. Rather than using a neural network as a part of the existing system, our model works on its own and generates a translation from a source sentence directly."

**Validation:** ✅ Clear distinction between end-to-end neural MT and hybrid approaches.
