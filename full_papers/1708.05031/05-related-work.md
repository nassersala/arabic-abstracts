# Section 5: Related Work
## القسم 5: الأعمال ذات الصلة

**Section:** related work
**Translation Quality:** 0.86
**Glossary Terms Used:** collaborative filtering, implicit feedback, explicit feedback, neural network, deep learning, Restricted Boltzmann Machine, autoencoder, matrix factorization, recommendation, embedding

---

### English Version

Our work is related to collaborative filtering, especially neural network based recommender systems. We briefly review related work in this section.

**Collaborative Filtering.** Collaborative filtering has a long history and plays an important role in the success of recommender systems. Early works mainly focused on explicit feedback. For example, memory-based methods measure the similarity between users and/or items for recommendation, which include user-based and item-based collaborative filtering. Model-based approaches include latent factor models, mixture model, topic model, latent Dirichlet allocation, and Markov decision process. To adapt to the ubiquitous implicit feedback, significant efforts have been devoted to designing CF models for implicit data. For example, one-class CF methods treat all missing data as negative instances or sample negative instances from missing data to formulate a binary classification problem. As a seminal work, Rendle et al. proposed BPR that optimizes matrix factorization with pairwise ranking loss. Recently, He et al. proposed to leverage item features to weight missing data, achieving state-of-the-art performance for implicit CF. Different from the above works that use a fixed function to model user-item interactions, we learn the interaction function from data using deep neural networks.

**Deep Learning for Recommendation.** Deep learning has been extensively applied in recommender systems. For example, Restricted Boltzmann Machines (RBMs) have been widely used for collaborative filtering. Salakhutdinov et al. proposed a two-layer RBM to model users' explicit ratings on items, while Wang et al. later extended RBMs by introducing a regression framework for implicit feedback. More recently, several works investigated using neural autoencoder for CF. For example, Sedhain et al. proposed AutoRec that learns hidden structures that can reconstruct a user's ratings, and Wu et al. proposed a Collaborative Denoising AutoEncoder (CDAE) that corrupts and reconstructs users' implicit feedback to make robust and more effective recommendations. Different from the above works that employ neural networks to reconstruct a user's historical interactions, our work focuses on using neural networks to estimate the interaction function for collaborative filtering.

More recently, deep learning has been extensively explored for improving recommendation systems. For example, van den Oord et al. employed CNNs to extract features from music signals and used the features as item representations for MF. Similarly, Kim et al. designed a CNN-based model for extracting image features for visual recommendations. Covington et al. applied deep neural networks for YouTube video recommendation, where two-step retrieval and ranking networks were designed to tackle the large corpus of YouTube videos. Wang et al. proposed a recurrent network model for session-based recommendations. Zheng et al. designed a deep network for news recommendation by jointly learning the representation of news and the propagation of news. Cheng et al. combined a wide linear model and a deep model for app recommendation. We note that all of these recent works have employed deep learning for extracting item features from rich sources of information. However, they primarily used deep learning to model auxiliary information and still resorted to MF for modelling CF signals. This is in contrast to our work which employs DNNs to learn the CF interaction function directly from the interaction data.

The most related work to ours is CDAE. Although CDAE employs a neural network for learning from user implicit feedback, it still applies a linear kernel (i.e., inner product) to model user-item interactions, a key component of CF. In addition, CDAE concatenates a user node with the input (corrupted) item vector and learns user-specific weights from the input layer to the hidden layer. This essentially embeds users into the same latent space of items in the input layer, limiting the model's flexibility in learning representations. In contrast, our NCF is a general framework that uses deep neural networks to model the user-item interaction, providing more flexibility to learn the interaction function.

---

### النسخة العربية

يرتبط عملنا بالتصفية التعاونية، وخاصة أنظمة التوصية القائمة على الشبكات العصبية. نستعرض بإيجاز الأعمال ذات الصلة في هذا القسم.

**التصفية التعاونية.** للتصفية التعاونية تاريخ طويل وتلعب دوراً مهماً في نجاح أنظمة التوصية. ركزت الأعمال المبكرة بشكل أساسي على التغذية الراجعة الصريحة. على سبيل المثال، تقيس الطرق القائمة على الذاكرة التشابه بين المستخدمين و/أو العناصر للتوصية، والتي تشمل التصفية التعاونية القائمة على المستخدم والقائمة على العنصر. تتضمن النهج القائمة على النموذج نماذج العوامل الكامنة، ونموذج المزيج، ونموذج الموضوع، وتخصيص ديريشليه الكامن، وعملية قرار ماركوف. للتكيف مع التغذية الراجعة الضمنية المنتشرة في كل مكان، تم تكريس جهود كبيرة لتصميم نماذج التصفية التعاونية للبيانات الضمنية. على سبيل المثال، تعامل طرق التصفية التعاونية من فئة واحدة جميع البيانات المفقودة كحالات سلبية أو تأخذ عينات من حالات سلبية من البيانات المفقودة لصياغة مشكلة تصنيف ثنائي. كعمل رائد، اقترح Rendle وآخرون BPR الذي يحسّن تحليل المصفوفات مع خسارة ترتيب زوجي. مؤخراً، اقترح He وآخرون الاستفادة من ميزات العنصر لوزن البيانات المفقودة، محققين أداء حديث للتصفية التعاونية الضمنية. على عكس الأعمال المذكورة أعلاه التي تستخدم دالة ثابتة لنمذجة تفاعلات المستخدم والعنصر، نتعلم دالة التفاعل من البيانات باستخدام الشبكات العصبية العميقة.

**التعلم العميق للتوصية.** تم تطبيق التعلم العميق على نطاق واسع في أنظمة التوصية. على سبيل المثال، تم استخدام آلات بولتزمان المقيدة (RBMs) على نطاق واسع للتصفية التعاونية. اقترح Salakhutdinov وآخرون RBM ذو طبقتين لنمذجة تقييمات المستخدمين الصريحة على العناصر، بينما قام Wang وآخرون لاحقاً بتوسيع RBMs من خلال تقديم إطار انحدار للتغذية الراجعة الضمنية. مؤخراً، حققت العديد من الأعمال في استخدام المشفر التلقائي العصبي للتصفية التعاونية. على سبيل المثال، اقترح Sedhain وآخرون AutoRec الذي يتعلم البنى المخفية التي يمكنها إعادة بناء تقييمات المستخدم، واقترح Wu وآخرون مشفراً تلقائياً تعاونياً لإزالة الضوضاء (CDAE) الذي يفسد ويعيد بناء التغذية الراجعة الضمنية للمستخدمين لجعل التوصيات أكثر قوة وفعالية. على عكس الأعمال المذكورة أعلاه التي تستخدم الشبكات العصبية لإعادة بناء تفاعلات المستخدم التاريخية، يركز عملنا على استخدام الشبكات العصبية لتقدير دالة التفاعل للتصفية التعاونية.

مؤخراً، تم استكشاف التعلم العميق على نطاق واسع لتحسين أنظمة التوصية. على سبيل المثال، استخدم van den Oord وآخرون الشبكات العصبية الالتفافية لاستخراج الميزات من إشارات الموسيقى واستخدموا الميزات كتمثيلات للعناصر لتحليل المصفوفات. وبالمثل، صمم Kim وآخرون نموذجاً قائماً على الشبكات العصبية الالتفافية لاستخراج ميزات الصورة للتوصيات المرئية. طبق Covington وآخرون الشبكات العصبية العميقة لتوصية فيديو YouTube، حيث تم تصميم شبكات الاسترجاع والترتيب ذات الخطوتين للتعامل مع المجموعة الكبيرة من مقاطع فيديو YouTube. اقترح Wang وآخرون نموذج شبكة متكررة للتوصيات القائمة على الجلسات. صمم Zheng وآخرون شبكة عميقة لتوصية الأخبار من خلال التعلم المشترك لتمثيل الأخبار وانتشار الأخبار. دمج Cheng وآخرون نموذجاً خطياً واسعاً ونموذجاً عميقاً لتوصية التطبيقات. نلاحظ أن جميع هذه الأعمال الحديثة استخدمت التعلم العميق لاستخراج ميزات العنصر من مصادر غنية من المعلومات. ومع ذلك، استخدموا بشكل أساسي التعلم العميق لنمذجة المعلومات المساعدة ولا يزالون يلجؤون إلى تحليل المصفوفات لنمذجة إشارات التصفية التعاونية. هذا يتناقض مع عملنا الذي يستخدم الشبكات العصبية العميقة لتعلم دالة تفاعل التصفية التعاونية مباشرة من بيانات التفاعل.

العمل الأكثر صلة بعملنا هو CDAE. على الرغم من أن CDAE يستخدم شبكة عصبية للتعلم من التغذية الراجعة الضمنية للمستخدم، إلا أنه لا يزال يطبق نواة خطية (أي حاصل الضرب الداخلي) لنمذجة تفاعلات المستخدم والعنصر، وهو مكون رئيسي في التصفية التعاونية. بالإضافة إلى ذلك، يدمج CDAE عقدة مستخدم مع متجه العنصر المدخل (الفاسد) ويتعلم أوزاناً خاصة بالمستخدم من طبقة الإدخال إلى الطبقة المخفية. هذا يضمن المستخدمين بشكل أساسي في نفس الفضاء الكامن للعناصر في طبقة الإدخال، مما يحد من مرونة النموذج في تعلم التمثيلات. في المقابل، فإن NCF الخاص بنا هو إطار عمل عام يستخدم الشبكات العصبية العميقة لنمذجة تفاعل المستخدم والعنصر، مما يوفر المزيد من المرونة لتعلم دالة التفاعل.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Collaborative Denoising AutoEncoder (CDAE)
  - Restricted Boltzmann Machines (RBMs)
  - AutoRec
  - BPR (Bayesian Personalized Ranking)
  - One-class CF
  - User-based and item-based collaborative filtering
  - Latent Dirichlet allocation
  - Markov decision process
- **Equations:** None
- **Citations:** Multiple references to prior work (Salakhutdinov, Rendle, He, Sedhain, Wu, van den Oord, Kim, Covington, Wang, Zheng, Cheng, etc.)
- **Special handling:**
  - Author names kept in English as per academic convention
  - Method/model names (RBM, CDAE, AutoRec, BPR) kept as acronyms
  - "Inner product" translated as "حاصل الضرب الداخلي" consistently with earlier sections
  - Technical terms like "corrupts and reconstructs" translated as "يفسد ويعيد بناء"

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.86
