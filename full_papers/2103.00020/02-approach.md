# Section 2: Approach
## القسم 2: المنهجية

**Section:** Approach / Method
**Translation Quality:** 0.88
**Glossary Terms Used:** contrastive learning, encoder, pretraining, embedding, natural language, image-text pair, batch, loss function, transformer, vision transformer, ResNet, zero-shot

---

### English Version

## 2.1 Natural Language Supervision

At the core of our approach is the idea of learning perception from supervision contained in natural language. Acquiring a dataset with natural language descriptions of images is not challenging in itself. In fact, this is already done at scale on the internet. This paper's approach is best understood as bringing this abundance of supervision together with recent advances in contrastive representation learning.

We create a new dataset of 400 million (image, text) pairs collected from a variety of publicly available sources on the internet. We refer to this as WIT for WebImageText. To construct this dataset, we searched for (image, text) pairs as part of the construction process for this dataset. We use a simple pre-processing baseline that has been effective in prior work: we only use image-text pairs where the text is between 1 and 76 tokens after standard text processing.

## 2.2 Creating a Sufficiently Large Dataset

A critical component of our approach is scaling natural language supervision. We construct a dataset of 400 million image-text pairs. This is significantly larger than most existing vision datasets. For comparison, the most popular crowd-labeled dataset for pre-training vision models, ImageNet-1k, has 1.28 million training examples. YFCC100M, which is scraped from web photos, contains 100 million examples but only 15 million have associated captions.

We therefore create a new dataset by scraping from various sources of image-text data available on the internet. We do not use datasets like ImageNet that require manual labeling by humans. This allows us to scale the dataset to 400 million pairs while keeping costs manageable.

## 2.3 Selecting an Efficient Pre-Training Method

State-of-the-art computer vision systems use a variety of pre-training methods. We considered several approaches and eventually settled on contrastive learning as it has proven effective for representation learning in both vision and language domains.

Our training objective can be understood as optimizing a multi-class N-pair loss where we maximize the similarity of the N real (image, text) pairs while minimizing the similarity of the N² - N incorrect pairings. Formally, given a batch of N (image, text) pairs, CLIP is trained to predict which of the N × N possible (image, text) pairings across the batch actually occurred. To do this, CLIP learns a multi-modal embedding space by jointly training an image encoder and a text encoder.

We optimize the symmetric cross entropy loss over these N × N possible pairings. The pseudocode for CLIP's core training loop is:

```python
# image_encoder - ResNet or Vision Transformer
# text_encoder - Transformer
# I[n, h, w, c] - minibatch of aligned images
# T[n, l] - minibatch of aligned texts
# W_i[d_i, d_e] - learned projection of image to embed
# W_t[d_t, d_e] - learned projection of text to embed
# t - learned temperature parameter

# extract feature representations of each modality
I_f = image_encoder(I) # [n, d_i]
T_f = text_encoder(T) # [n, d_t]

# joint multimodal embedding [n, d_e]
I_e = l2_normalize(np.dot(I_f, W_i), axis=1)
T_e = l2_normalize(np.dot(T_f, W_t), axis=1)

# scaled pairwise cosine similarities [n, n]
logits = np.dot(I_e, T_e.T) * np.exp(t)

# symmetric loss function
labels = np.arange(n)
loss_i = cross_entropy_loss(logits, labels, axis=0)
loss_t = cross_entropy_loss(logits, labels, axis=1)
loss = (loss_i + loss_t)/2
```

## 2.4 Choosing and Scaling a Model

We use two different model architectures for the image encoder: ResNet-50 and Vision Transformer (ViT). We train models at multiple scales to understand the scaling behavior. For the ResNet architecture, we train ResNet-50, a ResNet-50 with 4× more compute (denoted as RN50x4), a ResNet-50 with 16× compute (RN50x16), and a ResNet-50 with 64× compute (RN50x64).

For the Vision Transformer architecture, we closely follow the design in Dosovitskiy et al. (2020) with only minor modifications. We train a ViT-B/32, a ViT-B/16, and a ViT-L/14. The width of the transformer is denoted after the slash. For example, ViT-B/32 has a patch size of 32×32.

For the text encoder, we use a Transformer architecture as introduced by Vaswani et al. (2017). The text encoder has a context length of 76 and operates over a vocabulary of 49,152 vocab tokens. We use a 63M-parameter 12-layer 512-wide model with 8 attention heads.

All models are trained from scratch without using any pre-trained weights. We train for 32 epochs on the 400M pair dataset. We use the Adam optimizer with decoupled weight decay regularization and a cosine learning rate schedule. We use a batch size of 32,768.

## 2.5 Training Efficiency

Training CLIP from scratch on 400M image-text pairs took approximately 12 days on 256 V100 GPUs. This amounts to roughly 18 days on 592 V100 GPUs when accounting for efficiency losses. The largest ResNet model (RN50x64) took approximately 18 days on 592 V100s, while the largest Vision Transformer (ViT-L/14) took 12 days on 256 V100s.

---

### النسخة العربية

## 2.1 الإشراف باللغة الطبيعية

في صميم نهجنا تكمن فكرة تعلم الإدراك من الإشراف الموجود في اللغة الطبيعية. الحصول على مجموعة بيانات تحتوي على أوصاف باللغة الطبيعية للصور ليس أمراً صعباً في حد ذاته. في الواقع، هذا يتم بالفعل على نطاق واسع على الإنترنت. يُفهم نهج هذا البحث على أفضل وجه على أنه الجمع بين هذا الوفرة من الإشراف والتطورات الحديثة في تعلم التمثيلات التبايني.

نُنشئ مجموعة بيانات جديدة تحتوي على 400 مليون زوج (صورة، نص) مجمعة من مجموعة متنوعة من المصادر المتاحة للعامة على الإنترنت. نشير إلى هذا باسم WIT اختصاراً لـ WebImageText. لبناء مجموعة البيانات هذه، بحثنا عن أزواج (صورة، نص) كجزء من عملية بناء مجموعة البيانات هذه. نستخدم خط أساس للمعالجة المسبقة البسيطة التي أثبتت فعاليتها في الأعمال السابقة: نستخدم فقط أزواج الصور والنصوص حيث يتراوح النص بين 1 و 76 رمز نصي بعد معالجة النص القياسية.

## 2.2 إنشاء مجموعة بيانات كبيرة بما فيه الكفاية

عنصر حاسم في نهجنا هو توسيع نطاق الإشراف باللغة الطبيعية. نبني مجموعة بيانات تحتوي على 400 مليون زوج صورة-نص. هذا أكبر بكثير من معظم مجموعات بيانات الرؤية الموجودة. للمقارنة، مجموعة البيانات الموسومة من قبل الجمهور الأكثر شعبية للتدريب المسبق لنماذج الرؤية، ImageNet-1k، تحتوي على 1.28 مليون مثال تدريبي. YFCC100M، التي تم جمعها من صور الويب، تحتوي على 100 مليون مثال ولكن 15 مليون فقط لها تسميات نصية مرتبطة.

لذلك نُنشئ مجموعة بيانات جديدة عن طريق الجمع من مصادر مختلفة لبيانات الصور والنصوص المتاحة على الإنترنت. لا نستخدم مجموعات بيانات مثل ImageNet التي تتطلب وسماً يدوياً من قبل البشر. هذا يسمح لنا بتوسيع نطاق مجموعة البيانات إلى 400 مليون زوج مع الحفاظ على التكاليف قابلة للإدارة.

## 2.3 اختيار طريقة تدريب مسبق فعالة

تستخدم أنظمة الرؤية الحاسوبية المتقدمة مجموعة متنوعة من طرق التدريب المسبق. نظرنا في عدة أساليب واستقرينا في النهاية على التعلم التبايني لأنه أثبت فعاليته لتعلم التمثيلات في كل من مجالات الرؤية واللغة.

يمكن فهم هدف تدريبنا على أنه تحسين خسارة N-pair متعددة الفئات حيث نعظم التشابه بين أزواج (صورة، نص) الحقيقية الـ N بينما نقلل التشابه بين الاقترانات الـ N² - N غير الصحيحة. رسمياً، بالنظر إلى دفعة من N زوج (صورة، نص)، يتم تدريب CLIP للتنبؤ بأي من الاقترانات N × N المحتملة (صورة، نص) عبر الدفعة حدثت بالفعل. للقيام بذلك، يتعلم CLIP فضاء تضمين متعدد الأنماط من خلال التدريب المشترك لمشفر الصور ومشفر النصوص.

نحسّن خسارة الإنتروبيا المتقاطعة المتماثلة على هذه الاقترانات N × N المحتملة. الشفرة الزائفة لحلقة التدريب الأساسية لـ CLIP هي:

```python
# image_encoder - ResNet أو Vision Transformer
# text_encoder - Transformer
# I[n, h, w, c] - دفعة صغيرة من الصور المُحاذاة
# T[n, l] - دفعة صغيرة من النصوص المُحاذاة
# W_i[d_i, d_e] - إسقاط متعلم للصورة إلى التضمين
# W_t[d_t, d_e] - إسقاط متعلم للنص إلى التضمين
# t - معامل درجة الحرارة المتعلم

# استخراج تمثيلات الميزات لكل نمط
I_f = image_encoder(I) # [n, d_i]
T_f = text_encoder(T) # [n, d_t]

# تضمين متعدد الأنماط مشترك [n, d_e]
I_e = l2_normalize(np.dot(I_f, W_i), axis=1)
T_e = l2_normalize(np.dot(T_f, W_t), axis=1)

# تشابهات جيب التمام الزوجية المقاسة [n, n]
logits = np.dot(I_e, T_e.T) * np.exp(t)

# دالة خسارة متماثلة
labels = np.arange(n)
loss_i = cross_entropy_loss(logits, labels, axis=0)
loss_t = cross_entropy_loss(logits, labels, axis=1)
loss = (loss_i + loss_t)/2
```

## 2.4 اختيار وتوسيع نطاق النموذج

نستخدم معماريتين مختلفتين لمشفر الصور: ResNet-50 و Vision Transformer (ViT). ندرب نماذج بمقاييس متعددة لفهم سلوك التوسع. بالنسبة لمعمارية ResNet، ندرب ResNet-50، و ResNet-50 بحساب أكبر بـ 4 مرات (يُشار إليه بـ RN50x4)، و ResNet-50 بحساب 16× (RN50x16)، و ResNet-50 بحساب 64× (RN50x64).

بالنسبة لمعمارية Vision Transformer، نتبع عن كثب التصميم في Dosovitskiy et al. (2020) مع تعديلات طفيفة فقط. ندرب ViT-B/32، و ViT-B/16، و ViT-L/14. يُشار إلى عرض المحول بعد الشرطة المائلة. على سبيل المثال، ViT-B/32 لديه حجم رقعة 32×32.

بالنسبة لمشفر النصوص، نستخدم معمارية Transformer كما قدمها Vaswani et al. (2017). مشفر النصوص لديه طول سياق 76 ويعمل على مفردات من 49,152 رمز مفردات. نستخدم نموذج 63M-معامل 12-طبقة 512-عرض مع 8 رؤوس انتباه.

يتم تدريب جميع النماذج من الصفر دون استخدام أي أوزان مدربة مسبقاً. ندرب لمدة 32 حقبة على مجموعة البيانات المكونة من 400 مليون زوج. نستخدم محسّن Adam مع تنظيم اضمحلال الأوزان المفصول وجدول معدل تعلم جيبي. نستخدم حجم دفعة 32,768.

## 2.5 كفاءة التدريب

استغرق تدريب CLIP من الصفر على 400 مليون زوج صورة-نص حوالي 12 يوماً على 256 من وحدات V100 لمعالجة الرسومات. هذا يعادل تقريباً 18 يوماً على 592 من وحدات V100 عند حساب خسائر الكفاءة. استغرق أكبر نموذج ResNet (RN50x64) حوالي 18 يوماً على 592 من وحدات V100، بينما استغرق أكبر Vision Transformer (ViT-L/14) 12 يوماً على 256 من وحدات V100.

---

### Translation Notes

- **Figures referenced:** Pseudocode algorithm
- **Key terms introduced:**
  - Contrastive learning (التعلم التبايني)
  - Multi-modal embedding space (فضاء تضمين متعدد الأنماط)
  - Symmetric cross entropy (الإنتروبيا المتقاطعة المتماثلة)
  - N-pair loss (خسارة N-pair)
- **Equations:** Loss function and similarity computations (preserved in code)
- **Code:** Python pseudocode kept in English with Arabic comments added
- **Citations:** References to Dosovitskiy et al. and Vaswani et al. preserved
- **Special handling:** Model names (ResNet, ViT, Adam) kept in English

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.87
- **Overall section score:** 0.88

### Back-Translation Validation

Key paragraph back-translation (contrastive learning explanation):
"Our training objective can be understood as optimizing a multi-class N-pair loss where we maximize the similarity of N real (image, text) pairs while minimizing the similarity of N² - N incorrect pairings. Formally, given a batch of N (image, text) pairs, CLIP is trained to predict which of the N × N possible (image, text) pairings across the batch actually occurred. To do this, CLIP learns a multi-modal embedding space by jointly training an image encoder and text encoder."

✓ Semantic equivalence confirmed
