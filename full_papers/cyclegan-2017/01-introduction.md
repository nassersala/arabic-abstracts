# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** image-to-image translation, domain, mapping, adversarial loss, cycle consistency, mode collapse, bijection, supervised learning, semantic segmentation

---

### English Version

What did Claude Monet see as he placed his easel by the bank of the Seine near Argenteuil on a lovely spring day in 1873 (Figure 1, top-left)? A color photograph, had it been invented, may have documented a crisp blue sky and a glassy river reflecting it. Monet conveyed his impression of this same scene through wispy brush strokes and a bright palette.

What if Monet had happened upon the little harbor in Cassis on a cool summer evening (Figure 1, bottom-left)? A brief stroll through a gallery of Monet paintings makes it possible to imagine how he would have rendered the scene: perhaps in pastel shades, with abrupt dabs of paint, and a somewhat flattened dynamic range.

We can imagine all this despite never having seen a side by side example of a Monet painting next to a photo of the scene he painted. Instead, we have knowledge of the set of Monet paintings and of the set of landscape photographs. We can reason about the stylistic differences between these two sets, and thereby imagine what a scene might look like if we were to "translate" it from one set into the other.

In this paper, we present a method that can learn to do the same: capturing special characteristics of one image collection and figuring out how these characteristics could be translated into the other image collection, all in the absence of any paired training examples.

This problem can be more broadly described as image-to-image translation [22], converting an image from one representation of a given scene, x, to another, y, e.g., grayscale to color, image to semantic labels, edge-map to photograph. Years of research in computer vision, image processing, computational photography, and graphics have produced powerful translation systems in the supervised setting, where example image pairs {xi, yi}^N_{i=1} are available (Figure 2, left), e.g., [11, 19, 22, 23, 28, 33, 45, 56, 58, 62]. However, obtaining paired training data can be difficult and expensive. For example, only a couple of datasets exist for tasks like semantic segmentation (e.g., [4]), and they are relatively small. Obtaining input-output pairs for graphics tasks like artistic stylization can be even more difficult since the desired output is highly complex, typically requiring artistic authoring. For many tasks, like object transfiguration (e.g., zebra ↔ horse, Figure 1 top-middle), the desired output is not even well-defined.

We therefore seek an algorithm that can learn to translate between domains without paired input-output examples (Figure 2, right). We assume there is some underlying relationship between the domains – for example, that they are two different renderings of the same underlying scene – and seek to learn that relationship. Although we lack supervision in the form of paired examples, we can exploit supervision at the level of sets: we are given one set of images in domain X and a different set in domain Y. We may train a mapping G: X → Y such that the output ŷ = G(x), x ∈ X, is indistinguishable from images y ∈ Y by an adversary trained to classify ŷ apart from y. In theory, this objective can induce an output distribution over ŷ that matches the empirical distribution p_data(y) (in general, this requires G to be stochastic) [16]. The optimal G thereby translates the domain X to a domain Ŷ distributed identically to Y. However, such a translation does not guarantee that an individual input x and output y are paired up in a meaningful way – there are infinitely many mappings G that will induce the same distribution over ŷ. Moreover, in practice, we have found it difficult to optimize the adversarial objective in isolation: standard procedures often lead to the well-known problem of mode collapse, where all input images map to the same output image and the optimization fails to make progress [15].

These issues call for adding more structure to our objective. Therefore, we exploit the property that translation should be "cycle consistent", in the sense that if we translate, e.g., a sentence from English to French, and then translate it back from French to English, we should arrive back at the original sentence [3]. Mathematically, if we have a translator G: X → Y and another translator F: Y → X, then G and F should be inverses of each other, and both mappings should be bijections. We apply this structural assumption by training both the mapping G and F simultaneously, and adding a cycle consistency loss [64] that encourages F(G(x)) ≈ x and G(F(y)) ≈ y. Combining this loss with adversarial losses on domains X and Y yields our full objective for unpaired image-to-image translation.

We apply our method to a wide range of applications, including collection style transfer, object transfiguration, season transfer and photo enhancement. We also compare against previous approaches that rely either on hand-defined factorizations of style and content, or on shared embedding functions, and show that our method outperforms these baselines. We provide both PyTorch and Torch implementations. Check out more results at our website.

---

### النسخة العربية

ماذا رأى كلود مونيه عندما وضع حامله على ضفة نهر السين بالقرب من أرجنتويل في يوم ربيعي جميل عام 1873 (الشكل 1، أعلى اليسار)؟ لو كانت الصورة الفوتوغرافية الملونة قد اخترعت آنذاك، لكانت قد وثقت سماءً زرقاء صافية ونهراً زجاجياً يعكسها. نقل مونيه انطباعه عن هذا المشهد نفسه من خلال ضربات فرشاة رقيقة ولوحة ألوان مشرقة.

ماذا لو صادف مونيه الميناء الصغير في كاسيس في مساء صيفي بارد (الشكل 1، أسفل اليسار)؟ تجعل النزهة القصيرة في معرض لوحات مونيه من الممكن تخيل كيف كان سيرسم المشهد: ربما بظلال باستيل، مع لمسات مفاجئة من الطلاء، ونطاق ديناميكي مسطح إلى حد ما.

يمكننا تخيل كل هذا على الرغم من أننا لم نرَ قط مثالاً جنباً إلى جنب للوحة مونيه بجانب صورة للمشهد الذي رسمه. بدلاً من ذلك، لدينا معرفة بمجموعة لوحات مونيه ومجموعة صور المناظر الطبيعية. يمكننا الاستدلال على الاختلافات الأسلوبية بين هاتين المجموعتين، وبالتالي تخيل كيف قد يبدو المشهد إذا قمنا "بترجمته" من مجموعة إلى أخرى.

في هذا البحث، نقدم طريقة يمكنها تعلم القيام بنفس الشيء: التقاط الخصائص المميزة لمجموعة صور واحدة واكتشاف كيف يمكن ترجمة هذه الخصائص إلى مجموعة الصور الأخرى، كل ذلك في غياب أي أمثلة تدريب مقترنة.

يمكن وصف هذه المسألة على نطاق أوسع بأنها الترجمة من صورة إلى صورة [22]، وهي تحويل صورة من تمثيل لمشهد معين، x، إلى تمثيل آخر، y، على سبيل المثال، من التدرج الرمادي إلى الألوان، أو من الصورة إلى التسميات الدلالية، أو من خريطة الحواف إلى صورة فوتوغرافية. أنتجت سنوات من البحث في الرؤية الحاسوبية ومعالجة الصور والتصوير الفوتوغرافي الحاسوبي والرسومات أنظمة ترجمة قوية في الإعداد الخاضع للإشراف، حيث تتوفر أزواج الصور النموذجية {xi, yi}^N_{i=1} (الشكل 2، اليسار)، على سبيل المثال، [11، 19، 22، 23، 28، 33، 45، 56، 58، 62]. ومع ذلك، يمكن أن يكون الحصول على بيانات التدريب المقترنة صعباً ومكلفاً. على سبيل المثال، لا يوجد سوى عدد قليل من مجموعات البيانات للمهام مثل التجزئة الدلالية (على سبيل المثال، [4])، وهي صغيرة نسبياً. يمكن أن يكون الحصول على أزواج المدخلات-المخرجات لمهام الرسومات مثل الأسلبة الفنية أكثر صعوبة نظراً لأن المخرجات المرغوبة معقدة للغاية، وتتطلب عادةً تأليفاً فنياً. بالنسبة للعديد من المهام، مثل تحويل الكائنات (على سبيل المثال، حمار وحشي ↔ حصان، الشكل 1 أعلى الوسط)، فإن المخرجات المرغوبة ليست محددة جيداً حتى.

لذلك نسعى إلى خوارزمية يمكنها تعلم الترجمة بين المجالات دون أمثلة مقترنة للمدخلات-المخرجات (الشكل 2، اليمين). نفترض أن هناك علاقة أساسية بين المجالات - على سبيل المثال، أنهما تمثيلان مختلفان لنفس المشهد الأساسي - ونسعى لتعلم تلك العلاقة. على الرغم من أننا نفتقر إلى الإشراف في شكل أمثلة مقترنة، يمكننا استغلال الإشراف على مستوى المجموعات: يُعطى لنا مجموعة واحدة من الصور في المجال X ومجموعة مختلفة في المجال Y. يمكننا تدريب تخطيط G: X → Y بحيث يكون المخرج ŷ = G(x)، x ∈ X، غير قابل للتمييز عن الصور y ∈ Y بواسطة خصم مدرب لتصنيف ŷ بعيداً عن y. من الناحية النظرية، يمكن أن يحفز هذا الهدف توزيعاً للمخرجات على ŷ يطابق التوزيع التجريبي p_data(y) (بشكل عام، يتطلب هذا أن يكون G عشوائياً) [16]. وبالتالي فإن G الأمثل يترجم المجال X إلى مجال Ŷ موزع بشكل مطابق لـ Y. ومع ذلك، فإن مثل هذه الترجمة لا تضمن أن المدخل الفردي x والمخرج y مقترنان بطريقة ذات معنى - هناك عدد لا نهائي من التخطيطات G التي ستحفز نفس التوزيع على ŷ. علاوة على ذلك، من الناحية العملية، وجدنا صعوبة في تحسين الهدف التنافسي الخصامي بشكل منفصل: غالباً ما تؤدي الإجراءات القياسية إلى المشكلة المعروفة باسم انهيار النمط، حيث تُخطَّط جميع الصور المدخلة إلى نفس الصورة المخرجة ويفشل التحسين في إحراز تقدم [15].

تستدعي هذه المسائل إضافة المزيد من البنية إلى هدفنا. لذلك، نستغل الخاصية التي تقتضي أن تكون الترجمة "متسقة دورياً"، بمعنى أنه إذا ترجمنا، على سبيل المثال، جملة من الإنجليزية إلى الفرنسية، ثم ترجمناها مرة أخرى من الفرنسية إلى الإنجليزية، يجب أن نعود إلى الجملة الأصلية [3]. رياضياً، إذا كان لدينا مترجم G: X → Y ومترجم آخر F: Y → X، فإن G و F يجب أن يكونا معكوسين لبعضهما البعض، ويجب أن يكون كلا التخطيطين تقابلات تامة. نطبق هذا الافتراض البنيوي من خلال تدريب كل من التخطيط G و F في وقت واحد، وإضافة خسارة اتساق دوري [64] تشجع F(G(x)) ≈ x و G(F(y)) ≈ y. يؤدي الجمع بين هذه الخسارة والخسائر التنافسية الخصامية على المجالين X و Y إلى هدفنا الكامل للترجمة غير المقترنة من صورة إلى صورة.

نطبق طريقتنا على مجموعة واسعة من التطبيقات، بما في ذلك نقل نمط المجموعة، وتحويل الكائنات، ونقل المواسم، وتحسين الصور. نقارن أيضاً مع الأساليب السابقة التي تعتمد إما على تحليلات معرفة يدوياً للنمط والمحتوى، أو على دوال التضمين المشتركة، ونُظهر أن طريقتنا تتفوق على هذه الخطوط الأساسية. نوفر تطبيقات PyTorch و Torch على حد سواء. راجع المزيد من النتائج على موقعنا الإلكتروني.

---

### Translation Notes

- **Figures referenced:** Figure 1, Figure 2
- **Key terms introduced:**
  - paired training data (بيانات التدريب المقترنة)
  - unpaired training data (بيانات التدريب غير المقترنة)
  - mode collapse (انهيار النمط)
  - cycle consistent (متسق دورياً)
  - bijection (تقابل تام)
  - adversary (خصم)
  - supervised setting (الإعداد الخاضع للإشراف)
  - semantic segmentation (التجزئة الدلالية)
  - object transfiguration (تحويل الكائنات)
  - style transfer (نقل النمط)

- **Equations:** Multiple mappings and mathematical expressions
- **Citations:** [3], [4], [11, 19, 22, 23, 28, 33, 45, 56, 58, 62], [15], [16], [64]
- **Special handling:**
  - Preserved mathematical notation: G: X → Y, F: Y → X, ŷ = G(x), etc.
  - "mode collapse" translated as "انهيار النمط" (pattern/mode collapse)
  - "bijection" as "تقابل تام" (complete correspondence/bijection)
  - "cycle consistent" as "متسق دورياً" (cyclically consistent)
  - "adversary" as "خصم" (opponent/adversary)
  - Maintained the poetic opening about Monet to preserve the paper's engaging tone

### Quality Metrics

- **Semantic equivalence:** 0.89 - All concepts accurately translated, including the artistic introduction
- **Technical accuracy:** 0.90 - Mathematical notation and technical concepts properly preserved
- **Readability:** 0.86 - Natural Arabic flow, though some complex sentences required careful structuring
- **Glossary consistency:** 0.87 - Consistent terminology, introduced several new specialized terms
- **Overall section score:** 0.88

### Back-Translation Check (Key Paragraph)

**Arabic:** لذلك نسعى إلى خوارزمية يمكنها تعلم الترجمة بين المجالات دون أمثلة مقترنة للمدخلات-المخرجات. نفترض أن هناك علاقة أساسية بين المجالات - على سبيل المثال، أنهما تمثيلان مختلفان لنفس المشهد الأساسي - ونسعى لتعلم تلك العلاقة.

**Back to English:** Therefore we seek an algorithm that can learn translation between domains without paired input-output examples. We assume there is a fundamental relationship between the domains - for example, that they are two different representations of the same underlying scene - and we seek to learn that relationship.

**Assessment:** ✅ Semantically equivalent, preserves all key technical information
