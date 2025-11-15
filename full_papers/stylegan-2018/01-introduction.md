# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.89
**Glossary Terms Used:** generative adversarial networks (GAN), generator, latent space, style transfer, discriminator, loss function, embedding, disentanglement, dataset

---

### English Version

The resolution and quality of images produced by generative methods—especially generative adversarial networks (GAN)—have seen rapid improvement recently. Yet the generators continue to operate as black boxes, and despite recent efforts, the understanding of various aspects of the image synthesis process, e.g., the origin of stochastic features, is still lacking. The properties of the latent space are also poorly understood, and the commonly demonstrated latent space interpolations provide no quantitative way to compare different generators against each other.

Motivated by style transfer literature, we re-design the generator architecture in a way that exposes novel ways to control the image synthesis process. Our generator starts from a learned constant input and adjusts the "style" of the image at each convolution layer based on the latent code, therefore directly controlling the strength of image features at different scales. Combined with noise injected directly into the network, this architectural change leads to automatic, unsupervised separation of high-level attributes (e.g., pose, identity) from stochastic variation (e.g., freckles, hair) in the generated images, and enables intuitive scale-specific mixing and interpolation operations. We do not modify the discriminator or the loss function in any way, and our work is thus orthogonal to the ongoing discussion about GAN loss functions, regularization, and hyper-parameters.

Our generator embeds the input latent code into an intermediate latent space, which has a profound effect on how the factors of variation are represented in the network. The input latent space must follow the probability density of the training data, and we argue that this leads to some degree of unavoidable entanglement. Our intermediate latent space is free from that restriction and is therefore allowed to be disentangled. As previous methods for estimating the degree of latent space disentanglement are not directly applicable in our case, we propose two new automated metrics—perceptual path length and linear separability—for quantifying these aspects of the generator. Using these metrics, we show that compared to a traditional generator architecture, our generator admits a more linear, less entangled representation of different factors of variation.

Finally, we present a new dataset of human faces (Flickr-Faces-HQ, FFHQ) that offers much higher quality and covers considerably wider variation than existing high-resolution datasets (Appendix A). We have made this dataset publicly available, along with our source code and pre-trained networks. The accompanying video can be found under the same link.

---

### النسخة العربية

شهدت دقة وجودة الصور المنتجة بواسطة الأساليب التوليدية—خاصة الشبكات التوليدية التنافسية (GAN)—تحسناً سريعاً في الآونة الأخيرة. ومع ذلك، لا تزال المولدات تعمل كصناديق سوداء، وعلى الرغم من الجهود الأخيرة، لا يزال الفهم لمختلف جوانب عملية توليد الصور، مثل أصل الميزات العشوائية، ناقصاً. كما أن خصائص الفضاء الكامن مفهومة بشكل ضعيف، والاستيفاءات في الفضاء الكامن التي تُعرض عادةً لا توفر طريقة كمية لمقارنة المولدات المختلفة ببعضها البعض.

بدافع من أدبيات نقل الأنماط، أعدنا تصميم معمارية المولد بطريقة تكشف عن طرق جديدة للتحكم في عملية توليد الصور. يبدأ مولدنا من مدخل ثابت متعلم ويضبط "نمط" الصورة عند كل طبقة التفاف بناءً على الشفرة الكامنة، وبالتالي يتحكم مباشرة في قوة ميزات الصورة على مقاييس مختلفة. بالاقتران مع الضوضاء المحقونة مباشرة في الشبكة، يؤدي هذا التغيير المعماري إلى فصل تلقائي غير موجه للسمات عالية المستوى (مثل الوضعية والهوية) من التباين العشوائي (مثل النمش والشعر) في الصور المولدة، ويمكّن من عمليات المزج والاستيفاء الخاصة بكل مقياس بشكل بديهي. لا نعدل المميز أو دالة الخسارة بأي شكل من الأشكال، وبالتالي فإن عملنا متعامد مع النقاش الجاري حول دوال خسارة GAN والتنظيم والمعاملات الفائقة.

يضمّن مولدنا الشفرة الكامنة المدخلة في فضاء كامن وسيط، مما له تأثير عميق على كيفية تمثيل عوامل التباين في الشبكة. يجب أن يتبع الفضاء الكامن المدخل كثافة الاحتمال لبيانات التدريب، ونحن نجادل بأن هذا يؤدي إلى درجة معينة من الترابط الحتمي. فضاؤنا الكامن الوسيط متحرر من هذا القيد وبالتالي يُسمح له بأن يكون مفصولاً. نظراً لأن الأساليب السابقة لتقدير درجة فصل الفضاء الكامن غير قابلة للتطبيق مباشرة في حالتنا، نقترح مقياسين آليين جديدين—طول المسار الإدراكي والانفصال الخطي—لقياس هذه الجوانب من المولد. باستخدام هذه المقاييس، نُظهر أنه بالمقارنة مع معمارية مولد تقليدية، يقبل مولدنا تمثيلاً أكثر خطية وأقل ترابطاً لعوامل التباين المختلفة.

أخيراً، نقدم مجموعة بيانات جديدة لوجوه بشرية (Flickr-Faces-HQ، FFHQ) توفر جودة أعلى بكثير وتغطي تبايناً أوسع بكثير من مجموعات البيانات عالية الدقة الموجودة (الملحق A). لقد أتحنا مجموعة البيانات هذه للجمهور، جنباً إلى جنب مع شفرتنا المصدرية والشبكات المدربة مسبقاً. يمكن العثور على الفيديو المصاحب تحت نفس الرابط.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Black box (صندوق أسود)
  - Stochastic features (الميزات العشوائية)
  - Latent space interpolation (الاستيفاء في الفضاء الكامن)
  - Convolution layer (طبقة الالتفاف)
  - Intermediate latent space (الفضاء الكامن الوسيط)
  - Perceptual path length (طول المسار الإدراكي)
  - Linear separability (الانفصال الخطي)
  - Probability density (كثافة الاحتمال)
- **Equations:** 0
- **Citations:** Multiple references to prior work [Goodfellow2014, Karras2017, Miyato2018B, Brock2018, etc.]
- **Special handling:** References to appendix maintained

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.89
- Readability: 0.88
- Glossary consistency: 0.90
- **Overall section score:** 0.89
